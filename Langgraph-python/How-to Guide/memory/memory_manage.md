## Table of Contents

- [How to manage conversation history¶](#how-to-manage-conversation-history)
  - [Setup¶](#setup)
  - [Build the agent¶](#build-the-agent)
  - [Filtering messages¶](#filtering-messages)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to manage conversation history

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
      * Memory  Memory 
        * Memory 
        * How to manage conversation history  How to manage conversation history  Table of contents 
          * Setup 
          * Build the agent 
          * Filtering messages 
        * How to delete messages 
        * How to add summary of the conversation history 
        * How to add semantic search to your agent's memory 
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
  * Build the agent 
  * Filtering messages 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Memory 

# How to manage conversation history¶

One of the most common use cases for persistence is to use it to keep track of
conversation history. This is great - it makes it easy to continue
conversations. As conversations get longer and longer, however, this
conversation history can build up and take up more and more of the context
window. This can often be undesirable as it leads to more expensive and longer
calls to the LLM, and potentially ones that error. In order to prevent this
from happening, you need to probably manage the conversation history.

Note: this guide focuses on how to do this in LangGraph, where you can fully
customize how this is done. If you want a more off-the-shelf solution, you can
look into functionality provided in LangChain:

  * How to filter messages
  * How to trim messages

## Setup¶

First, let's set up the packages we're going to want to use

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_anthropic
    

Next, we need to set API keys for Anthropic (the LLM we will use)

    
    
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

## Build the agent¶

Let's now build a simple ReAct style agent.

    
    
    from typing import Literal
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.tools import tool
    
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.graph import MessagesState, StateGraph, START, END
    from langgraph.prebuilt import ToolNode
    
    memory = MemorySaver()
    
    
    @tool
    def search(query: str):
        """Call to surf the web."""
        # This is a placeholder for the actual implementation
        # Don't let the LLM know this though 😊
        return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
    
    
    tools = [search]
    tool_node = ToolNode(tools)
    model = ChatAnthropic(model_name="claude-3-haiku-20240307")
    bound_model = model.bind_tools(tools)
    
    
    def should_continue(state: MessagesState):
        """Return the next node to execute."""
        last_message = state["messages"][-1]
        # If there is no function call, then we finish
        if not last_message.tool_calls:
            return END
        # Otherwise if there is, we continue
        return "action"
    
    
    # Define the function that calls the model
    def call_model(state: MessagesState):
        response = bound_model.invoke(state["messages"])
        # We return a list, because this will get added to the existing list
        return {"messages": response}
    
    
    # Define a new graph
    workflow = StateGraph(MessagesState)
    
    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)
    
    # Set the entrypoint as `agent`
    # This means that this node is the first one called
    workflow.add_edge(START, "agent")
    
    # We now add a conditional edge
    workflow.add_conditional_edges(
        # First, we define the start node. We use `agent`.
        # This means these are the edges taken after the `agent` node is called.
        "agent",
        # Next, we pass in the function that will determine which node is called next.
        should_continue,
        # Next, we pass in the path map - all the possible nodes this edge could go to
        ["action", END],
    )
    
    # We now add a normal edge from `tools` to `agent`.
    # This means that after `tools` is called, `agent` node is called next.
    workflow.add_edge("action", "agent")
    
    # Finally, we compile it!
    # This compiles it into a LangChain Runnable,
    # meaning you can use it as you would any other runnable
    app = workflow.compile(checkpointer=memory)
    

API Reference: ChatAnthropic | tool | MemorySaver | StateGraph | START | END | ToolNode
    
    
    from langchain_core.messages import HumanMessage
    
    config = {"configurable": {"thread_id": "2"}}
    input_message = HumanMessage(content="hi! I'm bob")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        event["messages"][-1].pretty_print()
    
    
    input_message = HumanMessage(content="what's my name?")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        event["messages"][-1].pretty_print()
    

API Reference: HumanMessage

    
    
    ================================[1m Human Message [0m=================================
    
    hi! I'm bob
    ==================================[1m Ai Message [0m==================================
    
    Nice to meet you, Bob! As an AI assistant, I don't have a physical form, but I'm happy to chat with you and try my best to help out however I can. Please feel free to ask me anything, and I'll do my best to provide useful information or assistance.
    ================================[1m Human Message [0m=================================
    
    what's my name?
    ==================================[1m Ai Message [0m==================================
    
    You said your name is Bob, so that is the name I have for you.
    

## Filtering messages¶

The most straight-forward thing to do to prevent conversation history from
blowing up is to filter the list of messages before they get passed to the
LLM. This involves two parts: defining a function to filter messages, and then
adding it to the graph. See the example below which defines a really simple
`filter_messages` function and then uses it.

    
    
    from typing import Literal
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.tools import tool
    
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.graph import MessagesState, StateGraph, START
    from langgraph.prebuilt import ToolNode
    
    memory = MemorySaver()
    
    
    @tool
    def search(query: str):
        """Call to surf the web."""
        # This is a placeholder for the actual implementation
        # Don't let the LLM know this though 😊
        return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
    
    
    tools = [search]
    tool_node = ToolNode(tools)
    model = ChatAnthropic(model_name="claude-3-haiku-20240307")
    bound_model = model.bind_tools(tools)
    
    
    def should_continue(state: MessagesState):
        """Return the next node to execute."""
        last_message = state["messages"][-1]
        # If there is no function call, then we finish
        if not last_message.tool_calls:
            return END
        # Otherwise if there is, we continue
        return "action"
    
    
    def filter_messages(messages: list):
        # This is very simple helper function which only ever uses the last message
        return messages[-1:]
    
    
    # Define the function that calls the model
    def call_model(state: MessagesState):
        messages = filter_messages(state["messages"])
        response = bound_model.invoke(messages)
        # We return a list, because this will get added to the existing list
        return {"messages": response}
    
    
    # Define a new graph
    workflow = StateGraph(MessagesState)
    
    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)
    
    # Set the entrypoint as `agent`
    # This means that this node is the first one called
    workflow.add_edge(START, "agent")
    
    # We now add a conditional edge
    workflow.add_conditional_edges(
        # First, we define the start node. We use `agent`.
        # This means these are the edges taken after the `agent` node is called.
        "agent",
        # Next, we pass in the function that will determine which node is called next.
        should_continue,
        # Next, we pass in the pathmap - all the possible nodes this edge could go to
        ["action", END],
    )
    
    # We now add a normal edge from `tools` to `agent`.
    # This means that after `tools` is called, `agent` node is called next.
    workflow.add_edge("action", "agent")
    
    # Finally, we compile it!
    # This compiles it into a LangChain Runnable,
    # meaning you can use it as you would any other runnable
    app = workflow.compile(checkpointer=memory)
    

API Reference: ChatAnthropic | tool | MemorySaver | StateGraph | START | ToolNode
    
    
    from langchain_core.messages import HumanMessage
    
    config = {"configurable": {"thread_id": "2"}}
    input_message = HumanMessage(content="hi! I'm bob")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        event["messages"][-1].pretty_print()
    
    # This will now not remember the previous messages
    # (because we set `messages[-1:]` in the filter messages argument)
    input_message = HumanMessage(content="what's my name?")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        event["messages"][-1].pretty_print()
    

API Reference: HumanMessage

    
    
    ================================[1m Human Message [0m=================================
    
    hi! I'm bob
    ==================================[1m Ai Message [0m==================================
    
    Nice to meet you, Bob! I'm Claude, an AI assistant created by Anthropic. It's a pleasure to chat with you. Feel free to ask me anything, I'm here to help!
    ================================[1m Human Message [0m=================================
    
    what's my name?
    ==================================[1m Ai Message [0m==================================
    
    I'm afraid I don't actually know your name. As an AI assistant, I don't have information about the specific identities of the people I talk to. I only know what is provided to me during our conversation.
    

In the above example we defined the `filter_messages` function ourselves. We
also provide off-the-shelf ways to trim and filter messages in LangChain.

  * How to filter messages
  * How to trim messages

## Comments

Back to top

Previous

How to create a custom checkpointer using Redis

Next

How to delete messages

Made with  Material for MkDocs Insiders