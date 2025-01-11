Multi-agent supervisor¶
The previous example routed messages automatically based on the output of the initial researcher agent.

We can also choose to use an LLM to orchestrate the different agents.

Below, we will create an agent group, with an agent supervisor to help delegate tasks.

diagram

To simplify the code in each agent node, we will use LangGraph's prebuilt create_react_agent. This and other "advanced agent" notebooks are designed to show how you can implement certain design patterns in LangGraph. If the pattern suits your needs, we recommend combining it with some of the other fundamental patterns described elsewhere in the docs for best performance.

Setup¶
First, let's install required packages and set our API keys


%%capture --no-stderr
%pip install -U langgraph langchain_community langchain_anthropic langchain_experimental

import getpass
import os


def _set_if_undefined(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Please provide your {var}")


_set_if_undefined("ANTHROPIC_API_KEY")
_set_if_undefined("TAVILY_API_KEY")
Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here.

Create tools¶
For this example, you will make an agent to do web research with a search engine, and one agent to create plots. Define the tools they'll use below:


from typing import Annotated

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

tavily_tool = TavilySearchResults(max_results=5)

# This executes code locally, which can be unsafe
repl = PythonREPL()


@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    """Use this to execute python code and do math. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user."""
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Successfully executed:\n\`\`\`python\n{code}\n\`\`\`\nStdout: {result}"
    return result_str
API Reference: TavilySearchResults | tool | PythonREPL

Create Agent Supervisor¶
It will use LLM with structured output to choose the next worker node OR finish processing.


from typing import Literal
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic
from langgraph.graph import MessagesState, END
from langgraph.types import Command


members = ["researcher", "coder"]
# Our team supervisor is an LLM node. It just picks the next agent to process
# and decides when the work is completed
options = members + ["FINISH"]

system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    f" following workers: {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)


class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""

    next: Literal[*options]


llm = ChatAnthropic(model="claude-3-5-sonnet-latest")


def supervisor_node(state: MessagesState) -> Command[Literal[*members, "__end__"]]:
    messages = [
        {"role": "system", "content": system_prompt},
    ] + state["messages"]
    response = llm.with_structured_output(Router).invoke(messages)
    goto = response["next"]
    if goto == "FINISH":
        goto = END

    return Command(goto=goto)
API Reference: ChatAnthropic | END | Command

Construct Graph¶
We're ready to start building the graph. Below, define the state and worker nodes using the function we just defined.


from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent


research_agent = create_react_agent(
    llm, tools=[tavily_tool], state_modifier="You are a researcher. DO NOT do any math."
)


def research_node(state: MessagesState) -> Command[Literal["supervisor"]]:
    result = research_agent.invoke(state)
    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="researcher")
            ]
        },
        goto="supervisor",
    )


# NOTE: THIS PERFORMS ARBITRARY CODE EXECUTION, WHICH CAN BE UNSAFE WHEN NOT SANDBOXED
code_agent = create_react_agent(llm, tools=[python_repl_tool])


def code_node(state: MessagesState) -> Command[Literal["supervisor"]]:
    result = code_agent.invoke(state)
    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="coder")
            ]
        },
        goto="supervisor",
    )


builder = StateGraph(MessagesState)
builder.add_edge(START, "supervisor")
builder.add_node("supervisor", supervisor_node)
builder.add_node("researcher", research_node)
builder.add_node("coder", code_node)
graph = builder.compile()
API Reference: HumanMessage | StateGraph | START | END | create_react_agent


from IPython.display import display, Image

display(Image(graph.get_graph().draw_mermaid_png()))


Invoke the team¶
With the graph created, we can now invoke it and see how it performs!


for s in graph.stream(
    {"messages": [("user", "What's the square root of 42?")]}, subgraphs=True
):
    print(s)
    print("----")

((), {'supervisor': {'next': 'coder'}})
----
``````output
Python REPL can execute arbitrary code. Use with caution.
``````output
(('coder:a0c2a6de-4a2d-3573-4049-cba490183bc1',), {'agent': {'messages': [AIMessage(content=[{'text': "I'll help you calculate the square root of 42 using Python.", 'type': 'text'}, {'id': 'toolu_011Nsa2En2Qk1SsYBdG6zveY', 'input': {'code': 'import math\nprint(math.sqrt(42))'}, 'name': 'python_repl_tool', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_016CdBcK9JKm39tsuGH6skhN', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 435, 'output_tokens': 82}}, id='run-f9be84c7-1569-4f53-9063-b1244339755b-0', tool_calls=[{'name': 'python_repl_tool', 'args': {'code': 'import math\nprint(math.sqrt(42))'}, 'id': 'toolu_011Nsa2En2Qk1SsYBdG6zveY', 'type': 'tool_call'}], usage_metadata={'input_tokens': 435, 'output_tokens': 82, 'total_tokens': 517, 'input_token_details': {}})]}})
----
(('coder:a0c2a6de-4a2d-3573-4049-cba490183bc1',), {'tools': {'messages': [ToolMessage(content='Successfully executed:\n\`\`\`python\nimport math\nprint(math.sqrt(42))\n\`\`\`\nStdout: 6.48074069840786\n', name='python_repl_tool', id='8b6bd229-5c63-43a4-9d63-e3b4a8468e21', tool_call_id='toolu_011Nsa2En2Qk1SsYBdG6zveY')]}})
----
(('coder:a0c2a6de-4a2d-3573-4049-cba490183bc1',), {'agent': {'messages': [AIMessage(content='The square root of 42 is approximately 6.4807 (rounded to 4 decimal places).', additional_kwargs={}, response_metadata={'id': 'msg_01QYQtz84F1Mgqyp2ecw4TEu', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 561, 'output_tokens': 28}}, id='run-b9dfff5d-f1c4-44d6-98d7-80f0e8548bcd-0', usage_metadata={'input_tokens': 561, 'output_tokens': 28, 'total_tokens': 589, 'input_token_details': {}})]}})
----
((), {'coder': {'messages': [HumanMessage(content='The square root of 42 is approximately 6.4807 (rounded to 4 decimal places).', additional_kwargs={}, response_metadata={}, name='coder')]}})
----
((), {'supervisor': {'next': '__end__'}})
----

for s in graph.stream(
    {
        "messages": [
            (
                "user",
                "Find the latest GDP of New York and California, then calculate the average",
            )
        ]
    },
    subgraphs=True,
):
    print(s)
    print("----")

    ---
    ((), {'supervisor': {'next': 'researcher'}})
----
(('researcher:7daea379-a5b6-6d3d-ef85-fffc96d7472e',), {'agent': {'messages': [AIMessage(content=[{'text': "I'll help you search for the GDP data of New York and California using the search tool. Then I'll note the values, but as instructed, I won't perform the mathematical calculation myself.", 'type': 'text'}, {'id': 'toolu_01S9hPD5nFsW1A2nE4fwCvRc', 'input': {'query': 'latest GDP of New York state 2023'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01RetKetMGpP2Q51w4R8N81e', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 442, 'output_tokens': 107}}, id='run-6e738192-18ae-4c1a-bbc0-f8b8509fe656-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'latest GDP of New York state 2023'}, 'id': 'toolu_01S9hPD5nFsW1A2nE4fwCvRc', 'type': 'tool_call'}], usage_metadata={'input_tokens': 442, 'output_tokens': 107, 'total_tokens': 549, 'input_token_details': {}})]}})
----
(('researcher:7daea379-a5b6-6d3d-ef85-fffc96d7472e',), {'tools': {'messages': [ToolMessage(content='[{"url": "https://usafacts.org/metrics/gross-domestic-product-gdp-by-state-new-york/", "content": "Gross domestic product (GDP) state — New York (dollars) Adjustment. None. Adjustment. Frequency. Yearly. Frequency. In 2022 (most recent), Gross domestic product (GDP) was $2,053,179,700,000 in the United States for New York (state). ... August 25, 2023. Suggested citation: Explore in... Less detail"}, {"url": "https://www.osc.ny.gov/reports/finance/2023-fcr/economic-and-demographic-trends", "content": "These include, but are not limited to:\\nBecause Google Translate™ is intellectual property owned by Google Inc., you must use Google Translate™ in accord with the Google license agreement, which includes potential liability for misuse: Google Terms of Service.\\nOffice of the NEW YORK\\nSTATE COMPTROLLER\\nNYS Comptroller Thomas P. DiNapoli\\nMain navigation\\nGET to KnowNew York State ComptrollerThomas P. DiNapoli\\nRead BIO\\nGET to KnowNew York State ComptrollerThomas P. DiNapoli\\nMenu\\nEconomic and Demographic Trends\\n2023 Financial Condition Report For Fiscal Year Ended March 31, 2023\\nEmployment Still Below Pre- Pandemic Levels in 2022\\nNew York Ranked 45th Nationwide for Personal Income Growth in 2022\\nNYS GDP Nearly $1.6 Trillion in 2022\\nA state’s Gross Domestic Product (GDP) is the value of production originating from all industries in the state, as defined by the U.S. Bureau of Economic Analysis.\\n The State of New York, its officers, employees, and/or agents are not liable to you, or to third parties, for damages or losses of any kind arising out of, or in connection with, the use or performance of such information. New York’s Population Continued to Decline in 2022\\nBook traversal links for Economic and Demographic Trends\\nTell us more about you to receive content related to your area or interests.\\n The Office of the State Comptroller does not warrant, promise, assure or guarantee the accuracy of the translations provided."}, {"url": "https://www.statista.com/statistics/188087/gdp-of-the-us-federal-state-of-new-york-since-1997/", "content": "Industry Overview\\nDigital & Trend reports\\nOverview and forecasts on trending topics\\nIndustry & Market reports\\nIndustry and market insights and forecasts\\nCompanies & Products reports\\nKey figures and rankings about companies and products\\nConsumer & Brand reports\\nConsumer and brand insights and preferences in various industries\\nPolitics & Society reports\\nDetailed information about political and social topics\\nCountry & Region reports\\nAll key figures about countries and regions\\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\\nInsights on consumer attitudes and behavior worldwide\\nBusiness information on 100m+ public and private companies\\nExplore Company Insights\\nDetailed information for 39,000+ online stores and marketplaces\\nDirectly accessible data for 170 industries from 150+ countries\\nand over 1\xa0Mio. facts.\\n Transforming data into design:\\nStatista Content & Design\\nStrategy and business building for the data-driven economy:\\nU.S. real GDP of New York 2000-2022\\nReal gross domestic product of New York in the United States\\nfrom 2000 to 2022\\n(in billion U.S. dollars)\\nAdditional Information\\nShow sources information\\nShow publisher information\\nUse Ask Statista Research Service\\nMarch 2023\\nUnited States\\n2000 to 2022\\nData presented here is in 2012 chained U.S. dollars.\\n Statistics on\\n\\"\\nNew York\\n\\"\\nOther statistics that may interest you New York\\nPopulation\\nEconomy\\nEmployment & Earnings\\nState & Local Government\\nNew York City\\nFurther related statistics\\nFurther Content: You might find this interesting as well\\nStatistics\\nTopics Other statistics on the topic\\nEconomy\\nU.S. real gross domestic product 2022, by state\\nPolitics & Government\\nU.S. state and local government outstanding debt 2021, by state\\nDemographics\\nResident population in New York 1960-2022\\nEconomy\\nU.S. New York metro area GDP 2001-2022\\nYou only have access to basic statistics.\\n Customized Research & Analysis projects:\\nGet quick analyses with our professional research service\\nThe best of the best: the portal for top lists & rankings:\\n"}, {"url": "https://www.statista.com/statistics/306777/new-york-gdp-growth/", "content": "Industry Overview\\nDigital & Trend reports\\nOverview and forecasts on trending topics\\nIndustry & Market reports\\nIndustry and market insights and forecasts\\nCompanies & Products reports\\nKey figures and rankings about companies and products\\nConsumer & Brand reports\\nConsumer and brand insights and preferences in various industries\\nPolitics & Society reports\\nDetailed information about political and social topics\\nCountry & Region reports\\nAll key figures about countries and regions\\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\\nInsights on consumer attitudes and behavior worldwide\\nBusiness information on 100m+ public and private companies\\nExplore Company Insights\\nDetailed information for 39,000+ online stores and marketplaces\\nDirectly accessible data for 170 industries from 150+ countries\\nand over 1\xa0Mio. facts.\\n Other statistics on the topic\\nEconomy\\nU.S. real gross domestic product 2022, by state\\nPolitics & Government\\nU.S. state and local government outstanding debt 2021, by state\\nDemographics\\nResident population in New York 1960-2022\\nEconomy\\nU.S. New York metro area GDP 2001-2022\\nTo download this statistic in XLS format you need a Statista Account\\nTo download this statistic in PNG format you need a Statista Account\\nTo download this statistic in PDF format you need a Statista Account\\nTo download this statistic in PPT format you need a Statista Account\\nAs a Premium user you get access to the detailed source references and background information about this statistic.\\n Statistics on\\n\\"\\nNew York\\n\\"\\nOther statistics that may interest you New York\\nPopulation\\nEconomy\\nEmployment & Earnings\\nState & Local Government\\nNew York City\\nFurther related statistics\\nFurther Content: You might find this interesting as well\\nStatistics\\nTopics U.S. annual GDP growth in New York 2000-2022\\nAnnual percent change in the real gross domestic product of New York in the United States from 2000 to 2022\\nAdditional Information\\nShow sources information\\nShow publisher information\\nUse Ask Statista Research Service\\nOctober 2023\\nUnited States (New York)\\n2000 to 2022\\n Transforming data into design:\\nStatista Content & Design\\nStrategy and business building for the data-driven economy:\\nIndustry-specific and extensively researched technical data (partially from exclusive partnerships)."}, {"url": "https://www.bea.gov/news/2024/gross-domestic-product-state-and-personal-income-state-4th-quarter-2023-and-preliminary", "content": "Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the fourth quarter of 2023, with the percent change ranging from 6.7 percent in Nevada to 0.2 percent in Nebraska (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 49 states and the District of Columbia."}]', name='tavily_search_results_json', id='a7ba20fa-57d5-43e9-9d15-29e4e6476edf', tool_call_id='toolu_01S9hPD5nFsW1A2nE4fwCvRc', artifact={'query': 'latest GDP of New York state 2023', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'title': 'Gross domestic product (GDP) - USAFacts', 'url': 'https://usafacts.org/metrics/gross-domestic-product-gdp-by-state-new-york/', 'content': 'Gross domestic product (GDP) state — New York (dollars) Adjustment. None. Adjustment. Frequency. Yearly. Frequency. In 2022 (most recent), Gross domestic product (GDP) was $2,053,179,700,000 in the United States for New York (state). ... August 25, 2023. Suggested citation: Explore in... Less detail', 'score': 0.99883956, 'raw_content': None}, {'title': 'Economic and Demographic Trends - Office of the New York State Comptroller', 'url': 'https://www.osc.ny.gov/reports/finance/2023-fcr/economic-and-demographic-trends', 'content': 'These include, but are not limited to:\nBecause Google Translate™ is intellectual property owned by Google Inc., you must use Google Translate™ in accord with the Google license agreement, which includes potential liability for misuse: Google Terms of Service.\nOffice of the NEW YORK\nSTATE COMPTROLLER\nNYS Comptroller Thomas P. DiNapoli\nMain navigation\nGET to KnowNew York State ComptrollerThomas P. DiNapoli\nRead BIO\nGET to KnowNew York State ComptrollerThomas P. DiNapoli\nMenu\nEconomic and Demographic Trends\n2023 Financial Condition Report For Fiscal Year Ended March 31, 2023\nEmployment Still Below Pre- Pandemic Levels in 2022\nNew York Ranked 45th Nationwide for Personal Income Growth in 2022\nNYS GDP Nearly $1.6 Trillion in 2022\nA state’s Gross Domestic Product (GDP) is the value of production originating from all industries in the state, as defined by the U.S. Bureau of Economic Analysis.\n The State of New York, its officers, employees, and/or agents are not liable to you, or to third parties, for damages or losses of any kind arising out of, or in connection with, the use or performance of such information. New York’s Population Continued to Decline in 2022\nBook traversal links for Economic and Demographic Trends\nTell us more about you to receive content related to your area or interests.\n The Office of the State Comptroller does not warrant, promise, assure or guarantee the accuracy of the translations provided.', 'score': 0.97339284, 'raw_content': None}, {'title': 'Real GDP New York U.S. 2023 | Statista', 'url': 'https://www.statista.com/statistics/188087/gdp-of-the-us-federal-state-of-new-york-since-1997/', 'content': 'Industry Overview\nDigital & Trend reports\nOverview and forecasts on trending topics\nIndustry & Market reports\nIndustry and market insights and forecasts\nCompanies & Products reports\nKey figures and rankings about companies and products\nConsumer & Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics & Society reports\nDetailed information about political and social topics\nCountry & Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Transforming data into design:\nStatista Content & Design\nStrategy and business building for the data-driven economy:\nU.S. real GDP of New York 2000-2022\nReal gross domestic product of New York in the United States\nfrom 2000 to 2022\n(in billion U.S. dollars)\nAdditional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nMarch 2023\nUnited States\n2000 to 2022\nData presented here is in 2012 chained U.S. dollars.\n Statistics on\n"\nNew York\n"\nOther statistics that may interest you New York\nPopulation\nEconomy\nEmployment & Earnings\nState & Local Government\nNew York City\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics Other statistics on the topic\nEconomy\nU.S. real gross domestic product 2022, by state\nPolitics & Government\nU.S. state and local government outstanding debt 2021, by state\nDemographics\nResident population in New York 1960-2022\nEconomy\nU.S. New York metro area GDP 2001-2022\nYou only have access to basic statistics.\n Customized Research & Analysis projects:\nGet quick analyses with our professional research service\nThe best of the best: the portal for top lists & rankings:\n', 'score': 0.76454014, 'raw_content': None}, {'title': 'Annual GDP growth New York U.S. 2023 | Statista', 'url': 'https://www.statista.com/statistics/306777/new-york-gdp-growth/', 'content': 'Industry Overview\nDigital & Trend reports\nOverview and forecasts on trending topics\nIndustry & Market reports\nIndustry and market insights and forecasts\nCompanies & Products reports\nKey figures and rankings about companies and products\nConsumer & Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics & Society reports\nDetailed information about political and social topics\nCountry & Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Other statistics on the topic\nEconomy\nU.S. real gross domestic product 2022, by state\nPolitics & Government\nU.S. state and local government outstanding debt 2021, by state\nDemographics\nResident population in New York 1960-2022\nEconomy\nU.S. New York metro area GDP 2001-2022\nTo download this statistic in XLS format you need a Statista Account\nTo download this statistic in PNG format you need a Statista Account\nTo download this statistic in PDF format you need a Statista Account\nTo download this statistic in PPT format you need a Statista Account\nAs a Premium user you get access to the detailed source references and background information about this statistic.\n Statistics on\n"\nNew York\n"\nOther statistics that may interest you New York\nPopulation\nEconomy\nEmployment & Earnings\nState & Local Government\nNew York City\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics U.S. annual GDP growth in New York 2000-2022\nAnnual percent change in the real gross domestic product of New York in the United States from 2000 to 2022\nAdditional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nOctober 2023\nUnited States (New York)\n2000 to 2022\n Transforming data into design:\nStatista Content & Design\nStrategy and business building for the data-driven economy:\nIndustry-specific and extensively researched technical data (partially from exclusive partnerships).', 'score': 0.7212526, 'raw_content': None}, {'title': 'Gross Domestic Product by State and Personal Income by State, 4th ...', 'url': 'https://www.bea.gov/news/2024/gross-domestic-product-state-and-personal-income-state-4th-quarter-2023-and-preliminary', 'content': 'Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the fourth quarter of 2023, with the percent change ranging from 6.7 percent in Nevada to 0.2 percent in Nebraska (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 49 states and the District of Columbia.', 'score': 0.36139008, 'raw_content': None}], 'response_time': 2.31})]}})
----
(('researcher:7daea379-a5b6-6d3d-ef85-fffc96d7472e',), {'agent': {'messages': [AIMessage(content=[{'id': 'toolu_015fdnpWUiuEshsEwn2nBJ1g', 'input': {'query': 'latest GDP of California state 2023'}, 'name': 'tavily_search_results_json', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01Cksgb2aaqcD2bPtam5HDPF', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 2534, 'output_tokens': 66}}, id='run-11d924ba-a494-49d6-b649-ac961e31c79c-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'latest GDP of California state 2023'}, 'id': 'toolu_015fdnpWUiuEshsEwn2nBJ1g', 'type': 'tool_call'}], usage_metadata={'input_tokens': 2534, 'output_tokens': 66, 'total_tokens': 2600, 'input_token_details': {}})]}})
----
(('researcher:7daea379-a5b6-6d3d-ef85-fffc96d7472e',), {'tools': {'messages': [ToolMessage(content='[{"url": "https://www.gov.ca.gov/2024/04/16/california-remains-the-worlds-5th-largest-economy/", "content": "California remains the 5th largest economy in the world since 2017. California is the 5th largest economy in the world for the seventh consecutive year, with a nominal GDP of nearly $3.9 trillion in 2023 and a growth rate of 6.1% since the year prior, according to the U.S. Bureau of Economic Analysis (BEA). On a per capita basis, California is"}, {"url": "https://usafacts.org/metrics/gross-domestic-product-gdp-by-state-california/", "content": "USAFacts -- In 2022 (most recent), Gross domestic product (GDP) was 3598102700000.0 in the United States for California (state). This increased by 224,862,000,000 or 6.67% from 2021. Highest: 3,598,102,700,000 in 2022."}, {"url": "https://www.statista.com/statistics/187834/gdp-of-the-us-federal-state-of-california-since-1997/", "content": "Industry Overview\\nDigital & Trend reports\\nOverview and forecasts on trending topics\\nIndustry & Market reports\\nIndustry and market insights and forecasts\\nCompanies & Products reports\\nKey figures and rankings about companies and products\\nConsumer & Brand reports\\nConsumer and brand insights and preferences in various industries\\nPolitics & Society reports\\nDetailed information about political and social topics\\nCountry & Region reports\\nAll key figures about countries and regions\\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\\nInsights on consumer attitudes and behavior worldwide\\nBusiness information on 100m+ public and private companies\\nExplore Company Insights\\nDetailed information for 39,000+ online stores and marketplaces\\nDirectly accessible data for 170 industries from 150+ countries\\nand over 1\xa0Mio. facts.\\n Statistics on\\n\\"\\nCalifornia\\n\\"\\nOther statistics that may interest you California\\nPopulation\\nEconomy\\nEmployment & Earnings\\nState & Local Government\\nMetro Areas\\nFurther related statistics\\nFurther Content: You might find this interesting as well\\nStatistics\\nTopics Other statistics on the topicCalifornia\\nEconomy\\nU.S. leading companies headquartered in California 2023, by number of employees\\nEconomy\\nU.S. average annual wages in California 2018-2026\\nEconomy\\nU.S. California fastest growing private companies 2023, by three year growth rate\\nResidential Real Estate\\nHourly wages needed to afford a two-bedroom apartment in California 2021-23, by metro\\nYou only have access to basic statistics.\\n Additional Information\\nShow sources information\\nShow publisher information\\nUse Ask Statista Research Service\\nMarch 2023\\nUnited States\\n2000 to 2022\\nData presented here is in 2012 chained U.S. dollars.\\n Transforming data into design:\\nStatista Content & Design\\nStrategy and business building for the data-driven economy:\\nU.S. real GDP of California 2000-2022\\nReal gross domestic product of California in the United States from 2000 to 2022\\n(in billion U.S. dollars)\\n"}, {"url": "https://www.bea.gov/news/2024/gross-domestic-product-state-and-personal-income-state-4th-quarter-2023-and-preliminary", "content": "Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the fourth quarter of 2023, with the percent change ranging from 6.7 percent in Nevada to 0.2 percent in Nebraska (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 49 states and the District of Columbia."}, {"url": "https://www.bea.gov/news/2023/gross-domestic-product-state-and-personal-income-state-1st-quarter-2023", "content": "Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the first quarter of 2023, with the percent change ranging from 12.4 percent in North Dakota to 0.1 percent in Rhode Island and Alabama (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 47 states and the District of Columbia"}]', name='tavily_search_results_json', id='77de7955-ba39-4db3-9460-1a2bd7f602fb', tool_call_id='toolu_015fdnpWUiuEshsEwn2nBJ1g', artifact={'query': 'latest GDP of California state 2023', 'follow_up_questions': None, 'answer': None, 'images': [], 'results': [{'title': "California Remains the World's 5th Largest Economy", 'url': 'https://www.gov.ca.gov/2024/04/16/california-remains-the-worlds-5th-largest-economy/', 'content': 'California remains the 5th largest economy in the world since 2017. California is the 5th largest economy in the world for the seventh consecutive year, with a nominal GDP of nearly $3.9 trillion in 2023 and a growth rate of 6.1% since the year prior, according to the U.S. Bureau of Economic Analysis (BEA). On a per capita basis, California is', 'score': 0.99338466, 'raw_content': None}, {'title': 'Gross domestic product (GDP) - USAFacts', 'url': 'https://usafacts.org/metrics/gross-domestic-product-gdp-by-state-california/', 'content': 'USAFacts -- In 2022 (most recent), Gross domestic product (GDP) was 3598102700000.0 in the United States for California (state). This increased by 224,862,000,000 or 6.67% from 2021. Highest: 3,598,102,700,000 in 2022.', 'score': 0.99128854, 'raw_content': None}, {'title': 'Real GDP California U.S. 2023 | Statista', 'url': 'https://www.statista.com/statistics/187834/gdp-of-the-us-federal-state-of-california-since-1997/', 'content': 'Industry Overview\nDigital & Trend reports\nOverview and forecasts on trending topics\nIndustry & Market reports\nIndustry and market insights and forecasts\nCompanies & Products reports\nKey figures and rankings about companies and products\nConsumer & Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics & Society reports\nDetailed information about political and social topics\nCountry & Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries & territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Statistics on\n"\nCalifornia\n"\nOther statistics that may interest you California\nPopulation\nEconomy\nEmployment & Earnings\nState & Local Government\nMetro Areas\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics Other statistics on the topicCalifornia\nEconomy\nU.S. leading companies headquartered in California 2023, by number of employees\nEconomy\nU.S. average annual wages in California 2018-2026\nEconomy\nU.S. California fastest growing private companies 2023, by three year growth rate\nResidential Real Estate\nHourly wages needed to afford a two-bedroom apartment in California 2021-23, by metro\nYou only have access to basic statistics.\n Additional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nMarch 2023\nUnited States\n2000 to 2022\nData presented here is in 2012 chained U.S. dollars.\n Transforming data into design:\nStatista Content & Design\nStrategy and business building for the data-driven economy:\nU.S. real GDP of California 2000-2022\nReal gross domestic product of California in the United States from 2000 to 2022\n(in billion U.S. dollars)\n', 'score': 0.58112484, 'raw_content': None}, {'title': 'Gross Domestic Product by State and Personal Income by State, 4th ...', 'url': 'https://www.bea.gov/news/2024/gross-domestic-product-state-and-personal-income-state-4th-quarter-2023-and-preliminary', 'content': 'Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the fourth quarter of 2023, with the percent change ranging from 6.7 percent in Nevada to 0.2 percent in Nebraska (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 49 states and the District of Columbia.', 'score': 0.5455884, 'raw_content': None}, {'title': 'Gross Domestic Product by State and Personal Income by State, 1st ...', 'url': 'https://www.bea.gov/news/2023/gross-domestic-product-state-and-personal-income-state-1st-quarter-2023', 'content': 'Real gross domestic product (GDP) increased in all 50 states and the District of Columbia in the first quarter of 2023, with the percent change ranging from 12.4 percent in North Dakota to 0.1 percent in Rhode Island and Alabama (table 1), according to statistics released today by the U.S. Bureau of Economic Analysis (BEA). Current-dollar GDP increased in 47 states and the District of Columbia', 'score': 0.40857172, 'raw_content': None}], 'response_time': 3.04})]}})
----
(('researcher:7daea379-a5b6-6d3d-ef85-fffc96d7472e',), {'agent': {'messages': [AIMessage(content="Based on the search results, I can provide you with the latest GDP figures for both states:\n\nNew York:\n- GDP: $2.053 trillion (2022 figures)\n\nCalifornia:\n- GDP: $3.9 trillion (2023 figures)\n\nAs instructed, I won't calculate the average, but I've provided you with the most recent GDP figures for both states. Note that the figures are from different years (2022 for NY and 2023 for CA), which should be considered when calculating the average.", additional_kwargs={}, response_metadata={'id': 'msg_013yuy2PoBUNSGNDCYXvUL27', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 3748, 'output_tokens': 120}}, id='run-d775159b-c114-4db5-b425-416f0f2f957c-0', usage_metadata={'input_tokens': 3748, 'output_tokens': 120, 'total_tokens': 3868, 'input_token_details': {}})]}})
----
((), {'researcher': {'messages': [HumanMessage(content="Based on the search results, I can provide you with the latest GDP figures for both states:\n\nNew York:\n- GDP: $2.053 trillion (2022 figures)\n\nCalifornia:\n- GDP: $3.9 trillion (2023 figures)\n\nAs instructed, I won't calculate the average, but I've provided you with the most recent GDP figures for both states. Note that the figures are from different years (2022 for NY and 2023 for CA), which should be considered when calculating the average.", additional_kwargs={}, response_metadata={}, name='researcher')]}})
----
((), {'supervisor': {'next': 'coder'}})
----
(('coder:2c47a596-d75b-143e-9b4a-a99f78779aec',), {'agent': {'messages': [AIMessage(content=[{'text': "I'll help calculate the average GDP between New York ($2.053 trillion) and California ($3.9 trillion).", 'type': 'text'}, {'id': 'toolu_019yGU4aBc9H73jfRWr1iKtf', 'input': {'code': 'ny_gdp = 2.053\nca_gdp = 3.9\n\naverage_gdp = (ny_gdp + ca_gdp) / 2\n\nprint(f"New York GDP: ${ny_gdp} trillion")\nprint(f"California GDP: ${ca_gdp} trillion")\nprint(f"Average GDP: ${average_gdp:.3f} trillion")'}, 'name': 'python_repl_tool', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01PGbexsWGaf4LQbKDH8toJs', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 558, 'output_tokens': 175}}, id='run-355dc875-adcc-436c-b0f3-675dc1c099bd-0', tool_calls=[{'name': 'python_repl_tool', 'args': {'code': 'ny_gdp = 2.053\nca_gdp = 3.9\n\naverage_gdp = (ny_gdp + ca_gdp) / 2\n\nprint(f"New York GDP: ${ny_gdp} trillion")\nprint(f"California GDP: ${ca_gdp} trillion")\nprint(f"Average GDP: ${average_gdp:.3f} trillion")'}, 'id': 'toolu_019yGU4aBc9H73jfRWr1iKtf', 'type': 'tool_call'}], usage_metadata={'input_tokens': 558, 'output_tokens': 175, 'total_tokens': 733, 'input_token_details': {}})]}})
----
(('coder:2c47a596-d75b-143e-9b4a-a99f78779aec',), {'tools': {'messages': [ToolMessage(content='Successfully executed:\n\`\`\`python\nny_gdp = 2.053\nca_gdp = 3.9\n\naverage_gdp = (ny_gdp + ca_gdp) / 2\n\nprint(f"New York GDP: ${ny_gdp} trillion")\nprint(f"California GDP: ${ca_gdp} trillion")\nprint(f"Average GDP: ${average_gdp:.3f} trillion")\n\`\`\`\nStdout: New York GDP: $2.053 trillion\nCalifornia GDP: $3.9 trillion\nAverage GDP: $2.976 trillion\n', name='python_repl_tool', id='39106042-eb3e-485c-8d62-bb2f572fbf8b', tool_call_id='toolu_019yGU4aBc9H73jfRWr1iKtf')]}})
----
(('coder:2c47a596-d75b-143e-9b4a-a99f78779aec',), {'agent': {'messages': [AIMessage(content="Based on the calculations:\n- New York's GDP: $2.053 trillion (2022)\n- California's GDP: $3.9 trillion (2023)\n- The average GDP between the two states is $2.976 trillion\n\nNote: As mentioned earlier, these GDP figures are from different years (2022 for NY and 2023 for CA), which should be taken into consideration when interpreting the average.", additional_kwargs={}, response_metadata={'id': 'msg_016GGgrPRH3psSoWUw7TzTQu', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 877, 'output_tokens': 98}}, id='run-55436cea-0fab-4fa3-a691-3a80a0afb431-0', usage_metadata={'input_tokens': 877, 'output_tokens': 98, 'total_tokens': 975, 'input_token_details': {}})]}})
----
((), {'coder': {'messages': [HumanMessage(content="Based on the calculations:\n- New York's GDP: $2.053 trillion (2022)\n- California's GDP: $3.9 trillion (2023)\n- The average GDP between the two states is $2.976 trillion\n\nNote: As mentioned earlier, these GDP figures are from different years (2022 for NY and 2023 for CA), which should be taken into consideration when interpreting the average.", additional_kwargs={}, response_metadata={}, name='coder')]}})
----
((), {'supervisor': {'next': '__end__'}})
----