## Table of Contents

- [How to add node retry policies¶](#how-to-add-node-retry-policies)
  - [Setup¶](#setup)
  - [Passing a retry policy to a node¶](#passing-a-retry-policy-to-a-node)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add node retry policies

Initializing search

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 
  * Conceptual Guides 
  * Reference 

GitHub

  * Home 
  * Tutorials 
  * How-to Guides 

How-to Guides

    * LangGraph  LangGraph 
      * LangGraph 
      * Controllability 
      * Persistence 
      * Memory 
      * Human-in-the-loop 
      * Streaming 
      * Tool calling 
      * Subgraphs 
      * Multi-agent 
      * State Management 
      * Other  Other 
        * Other 
        * How to run a graph asynchronously 
        * How to visualize your graph 
        * How to add runtime configuration to your graph 
        * How to add node retry policies  How to add node retry policies  Table of contents 
          * Setup 
          * Passing a retry policy to a node 
        * How to return structured output with a ReAct style agent 
        * How to pass custom run ID or set tags and metadata for graph runs in LangSmith 
        * How to return state before hitting recursion limit 
      * Prebuilt ReAct Agent 
    * LangGraph Platform  LangGraph Platform 
      * LangGraph Platform 
      * Application Structure 
      * Deployment 
      * Authentication & Access Control 
      * Assistants 
      * Threads 
      * Runs 
      * Streaming 
      * Human-in-the-loop 
      * Double-texting 
      * Webhooks 
      * Cron Jobs 
      * LangGraph Studio 
    * Troubleshooting 

Troubleshooting

      * Troubleshooting 
      * GRAPH_RECURSION_LIMIT 
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Setup 
  * Passing a retry policy to a node 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Other 

# How to add node retry policies¶

Prerequisites

This guide assumes familiarity with the following:

  * LangGraph Glossary 

There are many use cases where you may wish for your node to have a custom
retry policy, for example if you are calling an API, querying a database, or
calling an LLM, etc.

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain_anthropic langchain_community
    
    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("ANTHROPIC_API_KEY")
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

In order to configure the retry policy, you have to pass the `retry` parameter
to the add_node. The `retry` parameter takes in a `RetryPolicy` named tuple
object. Below we instantiate a `RetryPolicy` object with the default
parameters:

    
    
    from langgraph.pregel import RetryPolicy
    
    RetryPolicy()
    
    
    
    RetryPolicy(initial_interval=0.5, backoff_factor=2.0, max_interval=128.0, max_attempts=3, jitter=True, retry_on=<function default_retry_on at 0x78b964b89940>)
    

By default, the `retry_on` parameter uses the `default_retry_on` function,
which retries on any exception except for the following:

  * `ValueError`
  * `TypeError`
  * `ArithmeticError`
  * `ImportError`
  * `LookupError`
  * `NameError`
  * `SyntaxError`
  * `RuntimeError`
  * `ReferenceError`
  * `StopIteration`
  * `StopAsyncIteration`
  * `OSError`

In addition, for exceptions from popular http request libraries such as
`requests` and `httpx` it only retries on 5xx status codes.

## Passing a retry policy to a node¶

Lastly, we can pass `RetryPolicy` objects when we call the add_node function.
In the example below we pass two different retry policies to each of our
nodes:

    
    
    import operator
    import sqlite3
    from typing import Annotated, Sequence
    from typing_extensions import TypedDict
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.messages import BaseMessage
    
    from langgraph.graph import END, StateGraph, START
    from langchain_community.utilities import SQLDatabase
    from langchain_core.messages import AIMessage
    
    db = SQLDatabase.from_uri("sqlite:///:memory:")
    
    model = ChatAnthropic(model_name="claude-2.1")
    
    
    class AgentState(TypedDict):
        messages: Annotated[Sequence[BaseMessage], operator.add]
    
    
    def query_database(state):
        query_result = db.run("SELECT * FROM Artist LIMIT 10;")
        return {"messages": [AIMessage(content=query_result)]}
    
    
    def call_model(state):
        response = model.invoke(state["messages"])
        return {"messages": [response]}
    
    
    # Define a new graph
    builder = StateGraph(AgentState)
    builder.add_node(
        "query_database",
        query_database,
        retry=RetryPolicy(retry_on=sqlite3.OperationalError),
    )
    builder.add_node("model", call_model, retry=RetryPolicy(max_attempts=5))
    builder.add_edge(START, "model")
    builder.add_edge("model", "query_database")
    builder.add_edge("query_database", END)
    
    graph = builder.compile()
    

API Reference: ChatAnthropic | BaseMessage | SQLDatabase | AIMessage | END | StateGraph | START

## Comments

Back to top

Previous

How to add runtime configuration to your graph

Next

How to return structured output with a ReAct style agent

Made with  Material for MkDocs Insiders