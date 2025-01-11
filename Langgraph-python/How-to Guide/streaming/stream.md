## Table of Contents

- [How to stream state updates of your graph¶](#how-to-stream-state-updates-of-your-graph)
  - [Setup¶](#setup)
  - [Define the graph¶](#define-the-graph)
  - [Stream updates¶](#stream-updates)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to stream state updates of your graph

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
      * Streaming  Streaming 
        * Streaming 
        * How to stream full state of your graph 
        * How to stream state updates of your graph  How to stream state updates of your graph  Table of contents 
          * Setup 
          * Define the graph 
          * Stream updates 
        * How to stream LLM tokens from your graph 
        * How to stream LLM tokens (without LangChain LLMs) 
        * How to stream custom data 
        * How to configure multiple streaming modes at the same time 
        * How to stream data from within a tool 
        * How to stream events from within a tool (without LangChain LLMs / tools) 
        * How to stream from the final node 
        * How to stream from subgraphs 
        * How to disable streaming for models that don't support it 
      * Tool calling 
      * Subgraphs 
      * Multi-agent 
      * State Management 
      * Other 
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
  * Define the graph 
  * Stream updates 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Streaming 

# How to stream state updates of your graph¶

LangGraph supports multiple streaming modes. The main ones are:

  * `values`: This streaming mode streams back values of the graph. This is the **full state of the graph** after each node is called.
  * `updates`: This streaming mode streams back updates to the graph. This is the **update to the state of the graph** after each node is called.

This guide covers `stream_mode="updates"`.

## Setup¶

First, let's install the required package and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain-openai langchain-community
    
    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("OPENAI_API_KEY")
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define the graph¶

We'll be using a simple ReAct agent for this guide.

    
    
    from typing import Literal
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain_core.runnables import ConfigurableField
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    from langgraph.prebuilt import create_react_agent
    
    
    @tool
    def get_weather(city: Literal["nyc", "sf"]):
        """Use this to get weather information."""
        if city == "nyc":
            return "It might be cloudy in nyc"
        elif city == "sf":
            return "It's always sunny in sf"
        else:
            raise AssertionError("Unknown city")
    
    
    tools = [get_weather]
    
    model = ChatOpenAI(model_name="gpt-4o", temperature=0)
    graph = create_react_agent(model, tools)
    

API Reference: TavilySearchResults | ConfigurableField | tool | ChatOpenAI | create_react_agent

## Stream updates¶

    
    
    inputs = {"messages": [("human", "what's the weather in sf")]}
    async for chunk in graph.astream(inputs, stream_mode="updates"):
        for node, values in chunk.items():
            print(f"Receiving update from node: '{node}'")
            print(values)
            print("\n\n")
    
    
    
    Receiving update from node: 'agent'
    {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_kc6cvcEkTAUGRlSHrP4PK9fn', 'function': {'arguments': '{"city":"sf"}', 'name': 'get_weather'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 14, 'prompt_tokens': 57, 'total_tokens': 71}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_3e7d703517', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-cd68b3a0-86c3-4afa-9649-1b962a0dd062-0', tool_calls=[{'name': 'get_weather', 'args': {'city': 'sf'}, 'id': 'call_kc6cvcEkTAUGRlSHrP4PK9fn'}], usage_metadata={'input_tokens': 57, 'output_tokens': 14, 'total_tokens': 71})]}
    
    
    
    Receiving update from node: 'tools'
    {'messages': [ToolMessage(content="It's always sunny in sf", name='get_weather', tool_call_id='call_kc6cvcEkTAUGRlSHrP4PK9fn')]}
    
    
    
    Receiving update from node: 'agent'
    {'messages': [AIMessage(content='The weather in San Francisco is currently sunny.', response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 84, 'total_tokens': 94}, 'model_name': 'gpt-4o-2024-05-13', 'system_fingerprint': 'fp_3e7d703517', 'finish_reason': 'stop', 'logprobs': None}, id='run-009d83c4-b874-4acc-9494-20aba43132b9-0', usage_metadata={'input_tokens': 84, 'output_tokens': 10, 'total_tokens': 94})]}
    

## Comments

Back to top

Previous

How to stream full state of your graph

Next

How to stream LLM tokens from your graph

Made with  Material for MkDocs Insiders