## Table of Contents

- [How to add cross-thread persistence to your graph¶](#how-to-add-cross-thread-persistence-to-your-graph)
  - [Setup¶](#setup)
  - [Define store¶](#define-store)
  - [Create graph¶](#create-graph)
  - [Run the graph!¶](#run-the-graph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add cross-thread persistence to your graph

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
        * How to add thread-level persistence to your graph 
        * How to add thread-level persistence to subgraphs 
        * How to add cross-thread persistence to your graph  How to add cross-thread persistence to your graph  Table of contents 
          * Setup 
          * Define store 
          * Create graph 
          * Run the graph! 
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
  * Define store 
  * Create graph 
  * Run the graph! 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Persistence 

# How to add cross-thread persistence to your graph¶

Prerequisites

This guide assumes familiarity with the following:

  * Persistence 
  * Memory 
  * Chat Models 

In the previous guide you learned how to persist graph state across multiple
interactions on a single thread. LangGraph also allows you to persist data
across **multiple threads**. For instance, you can store information about
users (their names or preferences) in a shared memory and reuse them in the
new conversational threads.

In this guide, we will show how to construct and use a graph that has a shared
memory implemented using the Store interface.

Note

Support for the `Store` API that is used in this guide was added in LangGraph
`v0.2.32`.

Support for **index** and **query** arguments of the `Store` API that is used
in this guide was added in LangGraph `v0.2.54`.

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langchain_openai langgraph
    
    
    
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
started here

## Define store¶

In this example we will create a graph that will be able to retrieve
information about a user's preferences. We will do so by defining an
`InMemoryStore` \- an object that can store data in memory and query that
data. We will then pass the store object when compiling the graph. This allows
each node in the graph to access the store: when you define node functions,
you can define `store` keyword argument, and LangGraph will automatically pass
the store object you compiled the graph with.

When storing objects using the `Store` interface you define two things:

  * the namespace for the object, a tuple (similar to directories)
  * the object key (similar to filenames)

In our example, we'll be using `("memories", <user_id>)` as namespace and
random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `user_id` via the
config keyword argument of the node function.

Let's first define an `InMemoryStore` already populated with some memories
about the users.

    
    
    from langgraph.store.memory import InMemoryStore
    from langchain_openai import OpenAIEmbeddings
    
    in_memory_store = InMemoryStore(
        index={
            "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
            "dims": 1536,
        }
    )
    

API Reference: OpenAIEmbeddings

## Create graph¶

    
    
    import uuid
    from typing import Annotated
    from typing_extensions import TypedDict
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.runnables import RunnableConfig
    from langgraph.graph import StateGraph, MessagesState, START
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.store.base import BaseStore
    
    
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    
    
    # NOTE: we're passing the Store param to the node --
    # this is the Store we compile the graph with
    def call_model(state: MessagesState, config: RunnableConfig, *, store: BaseStore):
        user_id = config["configurable"]["user_id"]
        namespace = ("memories", user_id)
        memories = store.search(namespace, query=str(state["messages"][-1].content))
        info = "\n".join([d.value["data"] for d in memories])
        system_msg = f"You are a helpful assistant talking to the user. User info: {info}"
    
        # Store new memories if the user asks the model to remember
        last_message = state["messages"][-1]
        if "remember" in last_message.content.lower():
            memory = "User name is Bob"
            store.put(namespace, str(uuid.uuid4()), {"data": memory})
    
        response = model.invoke(
            [{"type": "system", "content": system_msg}] + state["messages"]
        )
        return {"messages": response}
    
    
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_edge(START, "call_model")
    
    # NOTE: we're passing the store object here when compiling the graph
    graph = builder.compile(checkpointer=MemorySaver(), store=in_memory_store)
    # If you're using LangGraph Cloud or LangGraph Studio, you don't need to pass the store or checkpointer when compiling the graph, since it's done automatically.
    

API Reference: ChatAnthropic | RunnableConfig | StateGraph | START | MemorySaver

Note

If you're using LangGraph Cloud or LangGraph Studio, you **don't need** to
pass store when compiling the graph, since it's done automatically.

## Run the graph!¶

Now let's specify a user ID in the config and tell the model our name:

    
    
    config = {"configurable": {"thread_id": "1", "user_id": "1"}}
    input_message = {"type": "user", "content": "Hi! Remember: my name is Bob"}
    for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    Hi! Remember: my name is Bob
    ==================================[1m Ai Message [0m==================================
    
    Hello Bob! It's nice to meet you. I'll remember that your name is Bob. How can I assist you today?
    
    
    
    config = {"configurable": {"thread_id": "2", "user_id": "1"}}
    input_message = {"type": "user", "content": "what is my name?"}
    for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what is my name?
    ==================================[1m Ai Message [0m==================================
    
    Your name is Bob.
    

We can now inspect our in-memory store and verify that we have in fact saved
the memories for the user:

    
    
    for memory in in_memory_store.search(("memories", "1")):
        print(memory.value)
    
    
    
    {'data': 'User name is Bob'}
    

Let's now run the graph for another user to verify that the memories about the
first user are self contained:

    
    
    config = {"configurable": {"thread_id": "3", "user_id": "2"}}
    input_message = {"type": "user", "content": "what is my name?"}
    for chunk in graph.stream({"messages": [input_message]}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what is my name?
    ==================================[1m Ai Message [0m==================================
    
    I apologize, but I don't have any information about your name. As an AI assistant, I don't have access to personal information about users unless it has been specifically shared in our conversation. If you'd like, you can tell me your name and I'll be happy to use it in our discussion.
    

## Comments

Back to top

Previous

How to add thread-level persistence to subgraphs

Next

How to use Postgres checkpointer for persistence

Made with  Material for MkDocs Insiders