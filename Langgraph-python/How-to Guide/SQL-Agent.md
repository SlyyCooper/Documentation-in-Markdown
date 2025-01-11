An agent for interacting with a SQL database¶
In this tutorial, we will walk through how to build an agent that can answer questions about a SQL database.

At a high level, the agent will: 1. Fetch the available tables from the database 2. Decide which tables are relevant to the question 3. Fetch the DDL for the relevant tables 4. Generate a query based on the question and information from the DDL 5. Double-check the query for common mistakes using an LLM 6. Execute the query and return the results 7. Correct mistakes surfaced by the database engine until the query is successful 8. Formulate a response based on the results

The end-to-end workflow will look something like below:

sql-agent-diagram.png

Setup¶
First let's install our required packages and set our API keys


%%capture --no-stderr
%pip install -U langgraph langchain_openai langchain_community

import getpass
import os


def _set_env(key: str):
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")


_set_env("OPENAI_API_KEY")
Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here.

Configure the database¶
We will be creating a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the chinook database, which is a sample database that represents a digital media store. Find more information about the database here.

For convenience, we have hosted the database (Chinook.db) on a public GCS bucket.


import requests

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"

response = requests.get(url)

if response.status_code == 200:
    # Open a local file in binary write mode
    with open("Chinook.db", "wb") as file:
        # Write the content of the response (the file) to the local file
        file.write(response.content)
    print("File downloaded and saved as Chinook.db")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

File downloaded and saved as Chinook.db
We will use a handy SQL database wrapper available in the langchain_community package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results. We will also use the langchain_openai package to interact with the OpenAI API for language models later in the tutorial.

%%capture --no-stderr --no-display
!pip install langgraph langchain_community langchain_openai

from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")
API Reference: SQLDatabase


sqlite
['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']

"[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]"
Utility functions¶
We will define a few utility functions to help us with the agent implementation. Specifically, we will wrap a ToolNode with a fallback to handle errors and surface them to the agent.


from typing import Any

from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableLambda, RunnableWithFallbacks
from langgraph.prebuilt import ToolNode


def create_tool_node_with_fallback(tools: list) -> RunnableWithFallbacks[Any, dict]:
    """
    Create a ToolNode with a fallback to handle errors and surface them to the agent.
    """
    return ToolNode(tools).with_fallbacks(
        [RunnableLambda(handle_tool_error)], exception_key="error"
    )


def handle_tool_error(state) -> dict:
    error = state.get("error")
    tool_calls = state["messages"][-1].tool_calls
    return {
        "messages": [
            ToolMessage(
                content=f"Error: {repr(error)}\n please fix your mistakes.",
                tool_call_id=tc["id"],
            )
            for tc in tool_calls
        ]
    }
API Reference: ToolMessage | RunnableLambda | RunnableWithFallbacks | ToolNode

Define tools for the agent¶
We will define a few tools that the agent will use to interact with the database.

list_tables_tool: Fetch the available tables from the database
get_schema_tool: Fetch the DDL for a table
db_query_tool: Execute the query and fetch the results OR return an error message if the query fails
For the first two tools, we will grab them from the SQLDatabaseToolkit, also available in the langchain_community package.


from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

toolkit = SQLDatabaseToolkit(db=db, llm=ChatOpenAI(model="gpt-4o"))
tools = toolkit.get_tools()

list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")

print(list_tables_tool.invoke(""))

print(get_schema_tool.invoke("Artist"))
API Reference: SQLDatabaseToolkit | ChatOpenAI


Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track

CREATE TABLE "Artist" (
    "ArtistId" INTEGER NOT NULL, 
    "Name" NVARCHAR(120), 
    PRIMARY KEY ("ArtistId")
)

/*
3 rows from Artist table:
ArtistId    Name
1   AC/DC
2   Accept
3   Aerosmith
*/
The third will be defined manually. For the db_query_tool, we will execute the query against the database and return the results.

from langchain_core.tools import tool


@tool
def db_query_tool(query: str) -> str:
    """
    Execute a SQL query against the database and get back the result.
    If the query is not correct, an error message will be returned.
    If an error is returned, rewrite the query, check the query, and try again.
    """
    result = db.run_no_throw(query)
    if not result:
        return "Error: Query failed. Please rewrite your query and try again."
    return result


print(db_query_tool.invoke("SELECT * FROM Artist LIMIT 10;"))
API Reference: tool


[(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]
While not strictly a tool, we will prompt an LLM to check for common mistakes in the query and later add this as a node in the workflow.

from langchain_core.prompts import ChatPromptTemplate

query_check_system = """You are a SQL expert with a strong attention to detail.
Double check the SQLite query for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query.

You will call the appropriate tool to execute the query after running this check."""

query_check_prompt = ChatPromptTemplate.from_messages(
    [("system", query_check_system), ("placeholder", "{messages}")]
)
query_check = query_check_prompt | ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
    [db_query_tool], tool_choice="required"
)

query_check.invoke({"messages": [("user", "SELECT * FROM Artist LIMIT 10;")]})
API Reference: ChatPromptTemplate


AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_la8JTjHox6P1VjTqc15GSgdk', 'function': {'arguments': '{"query":"SELECT * FROM Artist LIMIT 10;"}', 'name': 'db_query_tool'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 221, 'total_tokens': 241}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'stop', 'logprobs': None}, id='run-dd7873ef-d2f7-4769-a5c0-e6776ec2c515-0', tool_calls=[{'name': 'db_query_tool', 'args': {'query': 'SELECT * FROM Artist LIMIT 10;'}, 'id': 'call_la8JTjHox6P1VjTqc15GSgdk', 'type': 'tool_call'}], usage_metadata={'input_tokens': 221, 'output_tokens': 20, 'total_tokens': 241})
Define the workflow¶
We will then define the workflow for the agent. The agent will first force-call the list_tables_tool to fetch the available tables from the database, then follow the steps mentioned at the beginning of the tutorial.

Using Pydantic with LangChain

This notebook uses Pydantic v2 BaseModel, which requires langchain-core >= 0.3. Using langchain-core < 0.3 will result in errors due to mixing of Pydantic v1 and v2 BaseModels.


from typing import Annotated, Literal

from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field
from typing_extensions import TypedDict

from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import AnyMessage, add_messages


# Define the state for the agent
class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


# Define a new graph
workflow = StateGraph(State)


# Add a node for the first tool call
def first_tool_call(state: State) -> dict[str, list[AIMessage]]:
    return {
        "messages": [
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "sql_db_list_tables",
                        "args": {},
                        "id": "tool_abcd123",
                    }
                ],
            )
        ]
    }


def model_check_query(state: State) -> dict[str, list[AIMessage]]:
    """
    Use this tool to double-check if your query is correct before executing it.
    """
    return {"messages": [query_check.invoke({"messages": [state["messages"][-1]]})]}


workflow.add_node("first_tool_call", first_tool_call)

# Add nodes for the first two tools
workflow.add_node(
    "list_tables_tool", create_tool_node_with_fallback([list_tables_tool])
)
workflow.add_node("get_schema_tool", create_tool_node_with_fallback([get_schema_tool]))

# Add a node for a model to choose the relevant tables based on the question and available tables
model_get_schema = ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
    [get_schema_tool]
)
workflow.add_node(
    "model_get_schema",
    lambda state: {
        "messages": [model_get_schema.invoke(state["messages"])],
    },
)


# Describe a tool to represent the end state
class SubmitFinalAnswer(BaseModel):
    """Submit the final answer to the user based on the query results."""

    final_answer: str = Field(..., description="The final answer to the user")


# Add a node for a model to generate a query based on the question and schema
query_gen_system = """You are a SQL expert with a strong attention to detail.

Given an input question, output a syntactically correct SQLite query to run, then look at the results of the query and return the answer.

DO NOT call any tool besides SubmitFinalAnswer to submit the final answer.

When generating the query:

Output the SQL query that answers the input question without a tool call.

Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.

If you get an error while executing a query, rewrite the query and try again.

If you get an empty result set, you should try to rewrite the query to get a non-empty result set. 
NEVER make stuff up if you don't have enough information to answer the query... just say you don't have enough information.

If you have enough information to answer the input question, simply invoke the appropriate tool to submit the final answer to the user.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database."""
query_gen_prompt = ChatPromptTemplate.from_messages(
    [("system", query_gen_system), ("placeholder", "{messages}")]
)
query_gen = query_gen_prompt | ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(
    [SubmitFinalAnswer]
)


def query_gen_node(state: State):
    message = query_gen.invoke(state)

    # Sometimes, the LLM will hallucinate and call the wrong tool. We need to catch this and return an error message.
    tool_messages = []
    if message.tool_calls:
        for tc in message.tool_calls:
            if tc["name"] != "SubmitFinalAnswer":
                tool_messages.append(
                    ToolMessage(
                        content=f"Error: The wrong tool was called: {tc['name']}. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.",
                        tool_call_id=tc["id"],
                    )
                )
    else:
        tool_messages = []
    return {"messages": [message] + tool_messages}


workflow.add_node("query_gen", query_gen_node)

# Add a node for the model to check the query before executing it
workflow.add_node("correct_query", model_check_query)

# Add node for executing the query
workflow.add_node("execute_query", create_tool_node_with_fallback([db_query_tool]))


# Define a conditional edge to decide whether to continue or end the workflow
def should_continue(state: State) -> Literal[END, "correct_query", "query_gen"]:
    messages = state["messages"]
    last_message = messages[-1]
    # If there is a tool call, then we finish
    if getattr(last_message, "tool_calls", None):
        return END
    if last_message.content.startswith("Error:"):
        return "query_gen"
    else:
        return "correct_query"


# Specify the edges between the nodes
workflow.add_edge(START, "first_tool_call")
workflow.add_edge("first_tool_call", "list_tables_tool")
workflow.add_edge("list_tables_tool", "model_get_schema")
workflow.add_edge("model_get_schema", "get_schema_tool")
workflow.add_edge("get_schema_tool", "query_gen")
workflow.add_conditional_edges(
    "query_gen",
    should_continue,
)
workflow.add_edge("correct_query", "execute_query")
workflow.add_edge("execute_query", "query_gen")

# Compile the workflow into a runnable
app = workflow.compile()
API Reference: AIMessage | ChatOpenAI | END | StateGraph | START | add_messages

Visualize the graph¶

from IPython.display import Image, display
from langchain_core.runnables.graph import MermaidDrawMethod

display(
    Image(
        app.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        )
    )
)
API Reference: MermaidDrawMethod



Run the agent¶

messages = app.invoke(
    {"messages": [("user", "Which sales agent made the most in sales in 2009?")]}
)
json_str = messages["messages"][-1].tool_calls[0]["args"]["final_answer"]
json_str

'The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34.'

for event in app.stream(
    {"messages": [("user", "Which sales agent made the most in sales in 2009?")]}
):
    print(event)

{'first_tool_call': {'messages': [AIMessage(content='', tool_calls=[{'name': 'sql_db_list_tables', 'args': {}, 'id': 'tool_abcd123', 'type': 'tool_call'}])]}}
{'list_tables_tool': {'messages': [ToolMessage(content='Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track', name='sql_db_list_tables', tool_call_id='tool_abcd123')]}}
{'model_get_schema': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_z1tyC7cEAawi5oIQn731Uknp', 'function': {'arguments': '{"table_names":"Employee, Invoice"}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 177, 'total_tokens': 195}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-c91a5aad-fc05-4881-87f9-0662d703c3c8-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': 'Employee, Invoice'}, 'id': 'call_z1tyC7cEAawi5oIQn731Uknp', 'type': 'tool_call'}], usage_metadata={'input_tokens': 177, 'output_tokens': 18, 'total_tokens': 195})]}}
{'get_schema_tool': {'messages': [ToolMessage(content='\nCREATE TABLE "Employee" (\n\t"EmployeeId" INTEGER NOT NULL, \n\t"LastName" NVARCHAR(20) NOT NULL, \n\t"FirstName" NVARCHAR(20) NOT NULL, \n\t"Title" NVARCHAR(30), \n\t"ReportsTo" INTEGER, \n\t"BirthDate" DATETIME, \n\t"HireDate" DATETIME, \n\t"Address" NVARCHAR(70), \n\t"City" NVARCHAR(40), \n\t"State" NVARCHAR(40), \n\t"Country" NVARCHAR(40), \n\t"PostalCode" NVARCHAR(10), \n\t"Phone" NVARCHAR(24), \n\t"Fax" NVARCHAR(24), \n\t"Email" NVARCHAR(60), \n\tPRIMARY KEY ("EmployeeId"), \n\tFOREIGN KEY("ReportsTo") REFERENCES "Employee" ("EmployeeId")\n)\n\n/*\n3 rows from Employee table:\nEmployeeId\tLastName\tFirstName\tTitle\tReportsTo\tBirthDate\tHireDate\tAddress\tCity\tState\tCountry\tPostalCode\tPhone\tFax\tEmail\n1\tAdams\tAndrew\tGeneral Manager\tNone\t1962-02-18 00:00:00\t2002-08-14 00:00:00\t11120 Jasper Ave NW\tEdmonton\tAB\tCanada\tT5K 2N1\t+1 (780) 428-9482\t+1 (780) 428-3457\tandrew@chinookcorp.com\n2\tEdwards\tNancy\tSales Manager\t1\t1958-12-08 00:00:00\t2002-05-01 00:00:00\t825 8 Ave SW\tCalgary\tAB\tCanada\tT2P 2T3\t+1 (403) 262-3443\t+1 (403) 262-3322\tnancy@chinookcorp.com\n3\tPeacock\tJane\tSales Support Agent\t2\t1973-08-29 00:00:00\t2002-04-01 00:00:00\t1111 6 Ave SW\tCalgary\tAB\tCanada\tT2P 5M5\t+1 (403) 262-3443\t+1 (403) 262-6712\tjane@chinookcorp.com\n*/\n\n\nCREATE TABLE "Invoice" (\n\t"InvoiceId" INTEGER NOT NULL, \n\t"CustomerId" INTEGER NOT NULL, \n\t"InvoiceDate" DATETIME NOT NULL, \n\t"BillingAddress" NVARCHAR(70), \n\t"BillingCity" NVARCHAR(40), \n\t"BillingState" NVARCHAR(40), \n\t"BillingCountry" NVARCHAR(40), \n\t"BillingPostalCode" NVARCHAR(10), \n\t"Total" NUMERIC(10, 2) NOT NULL, \n\tPRIMARY KEY ("InvoiceId"), \n\tFOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId")\n)\n\n/*\n3 rows from Invoice table:\nInvoiceId\tCustomerId\tInvoiceDate\tBillingAddress\tBillingCity\tBillingState\tBillingCountry\tBillingPostalCode\tTotal\n1\t2\t2009-01-01 00:00:00\tTheodor-Heuss-Straße 34\tStuttgart\tNone\tGermany\t70174\t1.98\n2\t4\t2009-01-02 00:00:00\tUllevålsveien 14\tOslo\tNone\tNorway\t0171\t3.96\n3\t8\t2009-01-03 00:00:00\tGrétrystraat 63\tBrussels\tNone\tBelgium\t1000\t5.94\n*/', name='sql_db_schema', tool_call_id='call_z1tyC7cEAawi5oIQn731Uknp')]}}
{'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_ErWLktUfxKsHGNGr74m72yYD', 'function': {'arguments': '{"table_names":"Customer"}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 16, 'prompt_tokens': 1179, 'total_tokens': 1195}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-19e02169-5e1e-40d9-90a2-384336ca5069-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': 'Customer'}, 'id': 'call_ErWLktUfxKsHGNGr74m72yYD', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1179, 'output_tokens': 16, 'total_tokens': 1195}), ToolMessage(content='Error: The wrong tool was called: sql_db_schema. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.', id='de5d25f5-b891-4e47-8282-d04dc9b93e9e', tool_call_id='call_ErWLktUfxKsHGNGr74m72yYD')]}}
{'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_TFaA52SbhgEqm3ElEAd4HCsn', 'function': {'arguments': '{"table_names":["Customer"]}', 'name': 'sql_db_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 1245, 'total_tokens': 1262}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2c5f800f-43dc-4224-847b-49b5079efd2a-0', tool_calls=[{'name': 'sql_db_schema', 'args': {'table_names': ['Customer']}, 'id': 'call_TFaA52SbhgEqm3ElEAd4HCsn', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1245, 'output_tokens': 17, 'total_tokens': 1262}), ToolMessage(content='Error: The wrong tool was called: sql_db_schema. Please fix your mistakes. Remember to only call SubmitFinalAnswer to submit the final answer. Generated queries should be outputted WITHOUT a tool call.', id='6c962a35-fc24-4f27-86f0-6ec05256d478', tool_call_id='call_TFaA52SbhgEqm3ElEAd4HCsn')]}}
{'query_gen': {'messages': [AIMessage(content="To determine which sales agent made the most in sales in 2009, we need to join the `Invoice`, `Customer`, and `Employee` tables. Here is the query to find the top sales agent:\n\n\`\`\`sql\nSELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\nFROM Invoice i\nJOIN Customer c ON i.CustomerId = c.CustomerId\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\nWHERE strftime('%Y', i.InvoiceDate) = '2009'\nGROUP BY e.EmployeeId\nORDER BY TotalSales DESC\nLIMIT 1;\n\`\`\`", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 125, 'prompt_tokens': 1312, 'total_tokens': 1437}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_3aa7262c27', 'finish_reason': 'stop', 'logprobs': None}, id='run-6cacd10d-d3aa-49ae-b9d7-8cc209fc4ccc-0', usage_metadata={'input_tokens': 1312, 'output_tokens': 125, 'total_tokens': 1437})]}}
{'correct_query': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_FwCE2c7WORU7lKHdSWqMv0ON', 'function': {'arguments': '{"query":"SELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\\nFROM Invoice i\\nJOIN Customer c ON i.CustomerId = c.CustomerId\\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\\nWHERE strftime(\'%Y\', i.InvoiceDate) = \'2009\'\\nGROUP BY e.EmployeeId\\nORDER BY TotalSales DESC\\nLIMIT 1;"}', 'name': 'db_query_tool'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 90, 'prompt_tokens': 337, 'total_tokens': 427}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_a2ff031fb5', 'finish_reason': 'stop', 'logprobs': None}, id='run-71067e75-80f6-4356-8239-518e466b3526-0', tool_calls=[{'name': 'db_query_tool', 'args': {'query': "SELECT e.FirstName, e.LastName, SUM(i.Total) as TotalSales\nFROM Invoice i\nJOIN Customer c ON i.CustomerId = c.CustomerId\nJOIN Employee e ON c.SupportRepId = e.EmployeeId\nWHERE strftime('%Y', i.InvoiceDate) = '2009'\nGROUP BY e.EmployeeId\nORDER BY TotalSales DESC\nLIMIT 1;"}, 'id': 'call_FwCE2c7WORU7lKHdSWqMv0ON', 'type': 'tool_call'}], usage_metadata={'input_tokens': 337, 'output_tokens': 90, 'total_tokens': 427})]}}
{'execute_query': {'messages': [ToolMessage(content="[('Steve', 'Johnson', 164.34)]", name='db_query_tool', tool_call_id='call_FwCE2c7WORU7lKHdSWqMv0ON')]}}
{'query_gen': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_fHJ4lvdiFM9HY6gupE6vLZV4', 'function': {'arguments': '{"final_answer":"The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34."}', 'name': 'SubmitFinalAnswer'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 41, 'prompt_tokens': 1553, 'total_tokens': 1594}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_cb7cc8e106', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-2ec7bf3a-2a16-47bd-aa9c-b7d6dc531c1b-0', tool_calls=[{'name': 'SubmitFinalAnswer', 'args': {'final_answer': 'The sales agent who made the most in sales in 2009 is Steve Johnson with total sales of 164.34.'}, 'id': 'call_fHJ4lvdiFM9HY6gupE6vLZV4', 'type': 'tool_call'}], usage_metadata={'input_tokens': 1553, 'output_tokens': 41, 'total_tokens': 1594})]}}
Eval¶
Now, we can evaluate this agent! We previously defined simple SQL agent as part of our LangSmith evaluation cookbooks, and evaluated responses to 5 questions about our database. We can compare this agent to our prior one on the same dataset. Agent evaluation can focus on 3 things:

Response: The inputs are a prompt and a list of tools. The output is the agent response.
Single tool: As before, the inputs are a prompt and a list of tools. The output the tool call.
Trajectory: As before, the inputs are a prompt and a list of tools. The output is the list of tool calls
Screenshot 2024-06-13 at 2.13.30 PM.png

Response¶
We'll evaluate end-to-end responses of our agent relative to reference answers. Let's run response evaluation on the same dataset.


import json


def predict_sql_agent_answer(example: dict):
    """Use this for answer evaluation"""
    msg = {"messages": ("user", example["input"])}
    messages = app.invoke(msg)
    json_str = messages["messages"][-1].tool_calls[0]["args"]
    response = json_str["final_answer"]
    return {"response": response}

from langchain import hub
from langchain_openai import ChatOpenAI

# Grade prompt
grade_prompt_answer_accuracy = prompt = hub.pull("langchain-ai/rag-answer-vs-reference")


def answer_evaluator(run, example) -> dict:
    """
    A simple evaluator for RAG answer accuracy
    """

    # Get question, ground truth answer, chain
    input_question = example.inputs["input"]
    reference = example.outputs["output"]
    prediction = run.outputs["response"]

    # LLM grader
    llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

    # Structured prompt
    answer_grader = grade_prompt_answer_accuracy | llm

    # Run evaluator
    score = answer_grader.invoke(
        {
            "question": input_question,
            "correct_answer": reference,
            "student_answer": prediction,
        }
    )
    score = score["Score"]

    return {"key": "answer_v_reference_score", "score": score}
API Reference: ChatOpenAI


from langsmith.evaluation import evaluate

dataset_name = "SQL Agent Response"
try:
    experiment_results = evaluate(
        predict_sql_agent_answer,
        data=dataset_name,
        evaluators=[answer_evaluator],
        num_repetitions=3,
        experiment_prefix="sql-agent-multi-step-response-v-reference",
        metadata={"version": "Chinook, gpt-4o multi-step-agent"},
    )
except:
    print("Please setup LangSmith")
Summary metrics (see dataset here):

The multi-step agent here out performs the previously defined base case SQL agent
Screenshot 2024-06-13 at 2.09.57 PM.png

Trajectory¶
Let's run trajectory evaluation on this same dataset.


# These are the tools that we expect the agent to use
expected_trajectory = [
    "sql_db_list_tables",  # first: list_tables_tool node
    "sql_db_schema",  # second: get_schema_tool node
    "db_query_tool",  # third: execute_query node
    "SubmitFinalAnswer",
]  # fourth: query_gen

def predict_sql_agent_messages(example: dict):
    """Use this for answer evaluation"""
    msg = {"messages": ("user", example["input"])}
    messages = app.invoke(msg)
    return {"response": messages}

from langsmith.schemas import Example, Run


def find_tool_calls(messages):
    """
    Find all tool calls in the messages returned
    """
    tool_calls = [
        tc["name"] for m in messages["messages"] for tc in getattr(m, "tool_calls", [])
    ]
    return tool_calls


def contains_all_tool_calls_in_order_exact_match(
    root_run: Run, example: Example
) -> dict:
    """
    Check if all expected tools are called in exact order and without any additional tool calls.
    """
    expected_trajectory = [
        "sql_db_list_tables",
        "sql_db_schema",
        "db_query_tool",
        "SubmitFinalAnswer",
    ]
    messages = root_run.outputs["response"]
    tool_calls = find_tool_calls(messages)

    # Print the tool calls for debugging
    print("Here are my tool calls:")
    print(tool_calls)

    # Check if the tool calls match the expected trajectory exactly
    if tool_calls == expected_trajectory:
        score = 1
    else:
        score = 0

    return {"score": int(score), "key": "multi_tool_call_in_exact_order"}


def contains_all_tool_calls_in_order(root_run: Run, example: Example) -> dict:
    """
    Check if all expected tools are called in order,
    but it allows for other tools to be called in between the expected ones.
    """
    messages = root_run.outputs["response"]
    tool_calls = find_tool_calls(messages)

    # Print the tool calls for debugging
    print("Here are my tool calls:")
    print(tool_calls)

    it = iter(tool_calls)
    if all(elem in it for elem in expected_trajectory):
        score = 1
    else:
        score = 0
    return {"score": int(score), "key": "multi_tool_call_in_order"}

try:
    experiment_results = evaluate(
        predict_sql_agent_messages,
        data=dataset_name,
        evaluators=[
            contains_all_tool_calls_in_order,
            contains_all_tool_calls_in_order_exact_match,
        ],
        num_repetitions=3,
        experiment_prefix="sql-agent-multi-step-tool-calling-trajecory-in-order",
        metadata={"version": "Chinook, gpt-4o multi-step-agent"},
    )
except:
    print("Please setup LangSmith")
The aggregate scores show that we never correctly call the tools in exact order:

Screenshot 2024-06-13 at 2.46.34 PM.png

Looking at the logging, we can see something interesting -


['sql_db_list_tables', 'sql_db_schema', 'sql_db_query', 'db_query_tool', 'SubmitFinalAnswer']
We appear to inject a hallucinated tool call, sql_db_query, into our trajectory for most of the runs.

This is why multi_tool_call_in_exact_order fails, but multi_tool_call_in_order still passes.

We will explore ways to resolve this using LangGraph in future cookbooks!

