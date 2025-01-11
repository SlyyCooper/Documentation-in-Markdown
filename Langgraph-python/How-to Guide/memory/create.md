## Table of Contents

- [How to add memory to the prebuilt ReAct agent¶](#how-to-add-memory-to-the-prebuilt-react-agent)
  - [Setup¶](#setup)
  - [Code¶](#code)
  - [Usage¶](#usage)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add memory to the prebuilt ReAct agent

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
        * How to use the prebuilt ReAct agent 
        * How to add memory to the prebuilt ReAct agent  How to add memory to the prebuilt ReAct agent  Table of contents 
          * Setup 
          * Code 
          * Usage 
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

# How to add memory to the prebuilt ReAct agent¶

Prerequisites

This guide assumes familiarity with the following:

  * LangGraph Persistence 
  * Checkpointer interface 
  * Agent Architectures 
  * Chat Models 
  * Tools 

This guide will show how to add memory to the prebuilt ReAct agent. Please see
this tutorial for how to get started with the prebuilt ReAct agent

We can add memory to the agent, by passing a checkpointer to the
create_react_agent function.

## Setup¶

First, let's install the required packages and set our API keys

    
    
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
    
    # We can add "chat memory" to the graph with LangGraph's checkpointer
    # to retain the chat context between interactions
    from langgraph.checkpoint.memory import MemorySaver
    
    memory = MemorySaver()
    
    # Define the graph
    
    from langgraph.prebuilt import create_react_agent
    
    graph = create_react_agent(model, tools=tools, checkpointer=memory)
    

API Reference: ChatOpenAI | tool | MemorySaver | create_react_agent

## Usage¶

Let's interact with it multiple times to show that it can remember

    
    
    def print_stream(stream):
        for s in stream:
            message = s["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()
    
    
    
    config = {"configurable": {"thread_id": "1"}}
    inputs = {"messages": [("user", "What's the weather in NYC?")]}
    
    print_stream(graph.stream(inputs, config=config, stream_mode="values"))
    
    
    
    ================================[1m Human Message [0m=================================
    
    What's the weather in NYC?
    ==================================[1m Ai Message [0m==================================
    Tool Calls:
      get_weather (call_xM1suIq26KXvRFqJIvLVGfqG)
     Call ID: call_xM1suIq26KXvRFqJIvLVGfqG
      Args:
        city: nyc
    =================================[1m Tool Message [0m=================================
    Name: get_weather
    
    It might be cloudy in nyc
    ==================================[1m Ai Message [0m==================================
    
    The weather in NYC might be cloudy.
    

Notice that when we pass the same the same thread ID, the chat history is
preserved

    
    
    inputs = {"messages": [("user", "What's it known for?")]}
    print_stream(graph.stream(inputs, config=config, stream_mode="values"))
    
    
    
    ================================[1m Human Message [0m=================================
    
    What's it known for?
    ==================================[1m Ai Message [0m==================================
    
    New York City (NYC) is known for a variety of iconic landmarks, cultural institutions, and vibrant neighborhoods. Some of the most notable aspects include:
    
    1. **Statue of Liberty**: A symbol of freedom and democracy.
    2. **Times Square**: Known for its bright lights, Broadway theaters, and bustling atmosphere.
    3. **Central Park**: A large urban park offering a green oasis in the middle of the city.
    4. **Empire State Building**: An iconic skyscraper with an observation deck offering panoramic views of the city.
    5. **Broadway**: Famous for its world-class theater productions.
    6. **Wall Street**: The financial hub of the United States.
    7. **Museums**: Including the Metropolitan Museum of Art, the Museum of Modern Art (MoMA), and the American Museum of Natural History.
    8. **Diverse Cuisine**: A melting pot of culinary experiences from around the world.
    9. **Cultural Diversity**: A rich tapestry of cultures, languages, and traditions.
    10. **Fashion**: A global fashion capital, home to New York Fashion Week.
    
    These are just a few highlights of what makes NYC a unique and vibrant city.
    
    
    
    

## Comments

Back to top

Previous

How to use the prebuilt ReAct agent

Next

How to add a custom system prompt to the prebuilt ReAct agent

Made with  Material for MkDocs Insiders