## Table of Contents

- [How to add thread-level persistence to your graph¶](#how-to-add-thread-level-persistence-to-your-graph)
  - [Setup¶](#setup)
  - [Define graph¶](#define-graph)
  - [Add persistence¶](#add-persistence)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add thread-level persistence to your graph

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
      * Persistence  Persistence 
        * Persistence 
        * How to add thread-level persistence to your graph  How to add thread-level persistence to your graph  Table of contents 
          * Setup 
          * Define graph 
          * Add persistence 
        * How to add thread-level persistence to subgraphs 
        * How to add cross-thread persistence to your graph 
        * How to use Postgres checkpointer for persistence 
        * How to use MongoDB checkpointer for persistence 
        * How to create a custom checkpointer using Redis 
      * Memory 
      * Human-in-the-loop 
      * Streaming 
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
  * Define graph 
  * Add persistence 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Persistence 

# How to add thread-level persistence to your graph¶

Prerequisites

This guide assumes familiarity with the following:

  * Persistence 
  * Memory 
  * Chat Models 

Many AI applications need memory to share context across multiple
interactions. In LangGraph, this kind of memory can be added to any StateGraph
using thread-level persistence .

When creating any LangGraph graph, you can set it up to persist its state by
adding a checkpointer when compiling the graph:

    
    
    from langgraph.checkpoint.memory import MemorySaver
    
    checkpointer = MemorySaver()
    graph.compile(checkpointer=checkpointer)
    

API Reference: MemorySaver

This guide shows how you can add thread-level persistence to your graph.

Note

If you need memory that is **shared** across multiple conversations or users
(cross-thread persistence), check out this how-to guide.

## Setup¶

First we need to install the packages required

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_anthropic
    

Next, we need to set API keys for OpenAI (the LLM we will use) and Tavily (the
search tool we will use)

    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("ANTHROPIC_API_KEY")
    
    
    
    ANTHROPIC_API_KEY:  ········
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define graph¶

We will be using a single-node graph that calls a chat model.

Let's first define the model we'll be using:

    
    
    from langchain_anthropic import ChatAnthropic
    
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    

API Reference: ChatAnthropic

Now we can define our `StateGraph` and add our model-calling node:

    
    
    from typing import Annotated
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph, MessagesState, START
    
    
    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}
    
    
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_edge(START, "call_model")
    graph = builder.compile()
    

API Reference: StateGraph | START

If we try to use this graph, the context of the conversation will not be
persisted across interactions:

    
    
    input_message = {"type": "user", "content": "hi! I'm bob"}
    for chunk in graph.stream({"messages": [input_message]}, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    input_message = {"type": "user", "content": "what's my name?"}
    for chunk in graph.stream({"messages": [input_message]}, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    hi! I'm bob
    ==================================[1m Ai Message [0m==================================
    
    Hello Bob! It's nice to meet you. How are you doing today? Is there anything I can help you with or would you like to chat about something in particular?
    ================================[1m Human Message [0m=================================
    
    what's my name?
    ==================================[1m Ai Message [0m==================================
    
    I apologize, but I don't have access to your personal information, including your name. I'm an AI language model designed to provide general information and answer questions to the best of my ability based on my training data. I don't have any information about individual users or their personal details. If you'd like to share your name, you're welcome to do so, but I won't be able to recall it in future conversations.
    

## Add persistence¶

To add in persistence, we need to pass in a Checkpointer when compiling the
graph.

    
    
    from langgraph.checkpoint.memory import MemorySaver
    
    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)
    # If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the checkpointer when compiling the graph, since it's done automatically.
    

API Reference: MemorySaver

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to
pass checkpointer when compiling the graph, since it's done automatically.

We can now interact with the agent and see that it remembers previous
messages!

    
    
    config = {"configurable": {"thread_id": "1"}}
    input_message = {"type": "user", "content": "hi! I'm bob"}
    for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    hi! I'm bob
    ==================================[1m Ai Message [0m==================================
    
    Hello Bob! It's nice to meet you. How are you doing today? Is there anything in particular you'd like to chat about or any questions you have that I can help you with?
    

You can always resume previous threads:

    
    
    input_message = {"type": "user", "content": "what's my name?"}
    for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what's my name?
    ==================================[1m Ai Message [0m==================================
    
    Your name is Bob, as you introduced yourself at the beginning of our conversation.
    

If we want to start a new conversation, we can pass in a different
`thread_id`. Poof! All the memories are gone!

    
    
    input_message = {"type": "user", "content": "what's my name?"}
    for chunk in graph.stream(
        {"messages": [input_message]},
        {"configurable": {"thread_id": "2"}},
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what's is my name?
    ==================================[1m Ai Message [0m==================================
    
    I apologize, but I don't have access to your personal information, including your name. As an AI language model, I don't have any information about individual users unless it's provided within the conversation. If you'd like to share your name, you're welcome to do so, but otherwise, I won't be able to know or guess it.
    

## Comments

Back to top

Previous

How to combine control flow and state updates with Command

Next

How to add thread-level persistence to subgraphs

Made with  Material for MkDocs Insiders