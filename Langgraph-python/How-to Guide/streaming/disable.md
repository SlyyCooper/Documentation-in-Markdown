## Table of Contents

- [How to disable streaming for models that don't support it¶](#how-to-disable-streaming-for-models-that-dont-support-it)
  - [Without disabling streaming¶](#without-disabling-streaming)
  - [Disabling streaming¶](#disabling-streaming)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to disable streaming for models that don't support it

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
        * How to stream state updates of your graph 
        * How to stream LLM tokens from your graph 
        * How to stream LLM tokens (without LangChain LLMs) 
        * How to stream custom data 
        * How to configure multiple streaming modes at the same time 
        * How to stream data from within a tool 
        * How to stream events from within a tool (without LangChain LLMs / tools) 
        * How to stream from the final node 
        * How to stream from subgraphs 
        * How to disable streaming for models that don't support it  How to disable streaming for models that don't support it  Table of contents 
          * Without disabling streaming 
          * Disabling streaming 
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

  * Without disabling streaming 
  * Disabling streaming 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Streaming 

# How to disable streaming for models that don't support it¶

Prerequisites

This guide assumes familiarity with the following:

  * streaming 
  * Chat Models 

Some chat models, including the new O1 models from OpenAI (depending on when
you're reading this), do not support streaming. This can lead to issues when
using the astream_events API, as it calls models in streaming mode, expecting
streaming to function properly.

In this guide, we’ll show you how to disable streaming for models that don’t
support it, ensuring they they're never called in streaming mode, even when
invoked through the astream_events API.

    
    
    from langchain_openai import ChatOpenAI
    from langgraph.graph import MessagesState
    from langgraph.graph import StateGraph, START, END
    
    llm = ChatOpenAI(model="o1-preview", temperature=1)
    
    graph_builder = StateGraph(MessagesState)
    
    
    def chatbot(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}
    
    
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()
    

API Reference: ChatOpenAI | StateGraph | START | END
    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    

## Without disabling streaming¶

Now that we've defined our graph, let's try to call `astream_events` without
disabling streaming. This should throw an error because the `o1` model does
not support streaming natively:

    
    
    input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
    try:
        async for event in graph.astream_events(input, version="v2"):
            if event["event"] == "on_chat_model_end":
                print(event["data"]["output"].content, end="", flush=True)
    except:
        print("Streaming not supported!")
    
    
    
    Streaming not supported!
    

An error occurred as we expected, luckily there is an easy fix!

## Disabling streaming¶

Now without making any changes to our graph, let's set the disable_streaming
parameter on our model to be `True` which will solve the problem:

    
    
    llm = ChatOpenAI(model="o1-preview", temperature=1, disable_streaming=True)
    
    graph_builder = StateGraph(MessagesState)
    
    
    def chatbot(state: MessagesState):
        return {"messages": [llm.invoke(state["messages"])]}
    
    
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()
    

And now, rerunning with the same input, we should see no errors:

    
    
    input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
    async for event in graph.astream_events(input, version="v2"):
        if event["event"] == "on_chat_model_end":
            print(event["data"]["output"].content, end="", flush=True)
    
    
    
    There are three "r"s in the word "strawberry".
    

## Comments

Back to top

Previous

How to stream from subgraphs

Next

How to call tools using ToolNode

Made with  Material for MkDocs Insiders