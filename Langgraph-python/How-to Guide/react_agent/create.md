## Table of Contents

- [How to use the prebuilt ReAct agent¶](#how-to-use-the-prebuilt-react-agent)
  - [Setup¶](#setup)
  - [Code¶](#code)
  - [Usage¶](#usage)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to use the prebuilt ReAct agent

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
      * Other 
      * Prebuilt ReAct Agent  Prebuilt ReAct Agent 
        * Prebuilt ReAct Agent 
        * How to use the prebuilt ReAct agent  How to use the prebuilt ReAct agent  Table of contents 
          * Setup 
          * Code 
          * Usage 
        * How to add memory to the prebuilt ReAct agent 
        * How to add a custom system prompt to the prebuilt ReAct agent 
        * How to add human-in-the-loop processes to the prebuilt ReAct agent 
        * How to create a ReAct agent from scratch 
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
  * Code 
  * Usage 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Prebuilt ReAct Agent 

# How to use the prebuilt ReAct agent¶

Prerequisites

This guide assumes familiarity with the following:

  * Agent Architectures 
  * Chat Models 
  * Tools 

In this how-to we'll create a simple ReAct agent app that can check the
weather. The app consists of an agent (LLM) and tools. As we interact with the
app, we will first call the agent (LLM) to decide if we should use tools. Then
we will run a loop:

  1. If the agent said to take an action (i.e. call tool), we'll run the tools and pass the results back to the agent
  2. If the agent did not ask to run tools, we will finish (respond to the user)

Prebuilt Agent

Please note that here will we use a prebuilt agent. One of the big benefits of
LangGraph is that you can easily create your own agent architectures. So while
it's fine to start here to build an agent quickly, we would strongly recommend
learning how to build your own agent so that you can take full advantage of
LangGraph.

## Setup¶

First let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain-openai
    
    
    
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

## Code¶

    
    
    # First we initialize the model we want to use.
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    
    
    # For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
    
    from typing import Literal
    
    from langchain_core.tools import tool
    
    
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
    
    
    # Define the graph
    
    from langgraph.prebuilt import create_react_agent
    
    graph = create_react_agent(model, tools=tools)
    

API Reference: ChatOpenAI | tool | create_react_agent

## Usage¶

First, let's visualize the graph we just created

    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    
    def print_stream(stream):
        for s in stream:
            message = s["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()
    

Let's run the app with an input that needs a tool call

    
    
    inputs = {"messages": [("user", "what is the weather in sf")]}
    print_stream(graph.stream(inputs, stream_mode="values"))
    
    
    
    ================================[1m Human Message [0m=================================
    
    what is the weather in sf
    ==================================[1m Ai Message [0m==================================
    Tool Calls:
      get_weather (call_zVvnU9DKr6jsNnluFIl59mHb)
     Call ID: call_zVvnU9DKr6jsNnluFIl59mHb
      Args:
        city: sf
    =================================[1m Tool Message [0m=================================
    Name: get_weather
    
    It's always sunny in sf
    ==================================[1m Ai Message [0m==================================
    
    The weather in San Francisco is currently sunny.
    

Now let's try a question that doesn't need tools

    
    
    inputs = {"messages": [("user", "who built you?")]}
    print_stream(graph.stream(inputs, stream_mode="values"))
    
    
    
    ================================[1m Human Message [0m=================================
    
    who built you?
    ==================================[1m Ai Message [0m==================================
    
    I was created by OpenAI, a research organization focused on developing and advancing artificial intelligence technology.
    

## Comments

Back to top

Previous

How to return state before hitting recursion limit

Next

How to add memory to the prebuilt ReAct agent

Made with  Material for MkDocs Insiders