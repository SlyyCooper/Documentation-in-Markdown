## Table of Contents

- [How to call tools using ToolNode¶](#how-to-call-tools-using-toolnode)
  - [Setup¶](#setup)
  - [Define tools¶](#define-tools)
  - [Manually call `ToolNode`¶](#manually-call-toolnode)
  - [Using with chat models¶](#using-with-chat-models)
  - [ReAct Agent¶](#react-agent)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to call tools using ToolNode

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
      * Tool calling  Tool calling 
        * Tool calling 
        * How to call tools using ToolNode  How to call tools using ToolNode  Table of contents 
          * Setup 
          * Define tools 
          * Manually call ToolNode 
          * Using with chat models 
          * ReAct Agent 
        * How to handle tool calling errors 
        * How to pass runtime values to tools 
        * How to update graph state from tools 
        * How to pass config to tools 
        * How to handle large numbers of tools 
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
  * Define tools 
  * Manually call ToolNode 
  * Using with chat models 
  * ReAct Agent 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Tool calling 

# How to call tools using ToolNode¶

This guide covers how to use LangGraph's prebuilt `ToolNode` for tool calling.

`ToolNode` is a LangChain Runnable that takes graph state (with a list of
messages) as input and outputs state update with the result of tool calls. It
is designed to work well out-of-box with LangGraph's prebuilt ReAct agent, but
can also work with any `StateGraph` as long as its state has a `messages` key
with an appropriate reducer (see `MessagesState`).

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_anthropic
    
    
    
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

## Define tools¶

    
    
    from langchain_core.messages import AIMessage
    from langchain_core.tools import tool
    
    from langgraph.prebuilt import ToolNode
    

API Reference: AIMessage | tool | ToolNode
    
    
    @tool
    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."
    
    
    @tool
    def get_coolest_cities():
        """Get a list of coolest cities"""
        return "nyc, sf"
    
    
    
    tools = [get_weather, get_coolest_cities]
    tool_node = ToolNode(tools)
    

## Manually call `ToolNode`¶

`ToolNode` operates on graph state with a list of messages. It expects the
last message in the list to be an `AIMessage` with `tool_calls` parameter.

Let's first see how to invoke the tool node manually:

    
    
    message_with_single_tool_call = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id",
                "type": "tool_call",
            }
        ],
    )
    
    tool_node.invoke({"messages": [message_with_single_tool_call]})
    
    
    
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id')]}
    

Note that typically you don't need to create `AIMessage` manually, and it will
be automatically generated by any LangChain chat model that supports tool
calling.

You can also do parallel tool calling using `ToolNode` if you pass multiple
tool calls to `AIMessage`'s `tool_calls` parameter:

    
    
    message_with_multiple_tool_calls = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_coolest_cities",
                "args": {},
                "id": "tool_call_id_1",
                "type": "tool_call",
            },
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id_2",
                "type": "tool_call",
            },
        ],
    )
    
    tool_node.invoke({"messages": [message_with_multiple_tool_calls]})
    
    
    
    {'messages': [ToolMessage(content='nyc, sf', name='get_coolest_cities', tool_call_id='tool_call_id_1'),
      ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id_2')]}
    

## Using with chat models¶

We'll be using a small chat model from Anthropic in our example. To use chat
models with tool calling, we need to first ensure that the model is aware of
the available tools. We do this by calling `.bind_tools` method on
`ChatAnthropic` moodel

    
    
    from typing import Literal
    
    from langchain_anthropic import ChatAnthropic
    from langgraph.graph import StateGraph, MessagesState
    from langgraph.prebuilt import ToolNode
    
    
    model_with_tools = ChatAnthropic(
        model="claude-3-haiku-20240307", temperature=0
    ).bind_tools(tools)
    

API Reference: ChatAnthropic | StateGraph | ToolNode
    
    
    model_with_tools.invoke("what's the weather in sf?").tool_calls
    
    
    
    [{'name': 'get_weather',
      'args': {'location': 'San Francisco'},
      'id': 'toolu_01Fwm7dg1mcJU43Fkx2pqgm8',
      'type': 'tool_call'}]
    

As you can see, the AI message generated by the chat model already has
`tool_calls` populated, so we can just pass it directly to `ToolNode`

    
    
    tool_node.invoke({"messages": [model_with_tools.invoke("what's the weather in sf?")]})
    
    
    
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='toolu_01LFvAVT3xJMeZS6kbWwBGZK')]}
    

## ReAct Agent¶

Next, let's see how to use `ToolNode` inside a LangGraph graph. Let's set up a
graph implementation of the ReAct agent. This agent takes some query as input,
then repeatedly call tools until it has enough information to resolve the
query. We'll be using `ToolNode` and the Anthropic model with tools we just
defined

    
    
    from typing import Literal
    
    from langgraph.graph import StateGraph, MessagesState, START, END
    
    
    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END
    
    
    def call_model(state: MessagesState):
        messages = state["messages"]
        response = model_with_tools.invoke(messages)
        return {"messages": [response]}
    
    
    workflow = StateGraph(MessagesState)
    
    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)
    
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")
    
    app = workflow.compile()
    

API Reference: StateGraph | START | END
    
    
    from IPython.display import Image, display
    
    try:
        display(Image(app.get_graph().draw_mermaid_png()))
    except Exception:
        # This requires some extra dependencies and is optional
        pass
    

Let's try it out!

    
    
    # example with a single tool call
    for chunk in app.stream(
        {"messages": [("human", "what's the weather in sf?")]}, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what's the weather in sf?
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "Okay, let's check the weather in San Francisco:", 'type': 'text'}, {'id': 'toolu_01LdmBXYeccWKdPrhZSwFCDX', 'input': {'location': 'San Francisco'}, 'name': 'get_weather', 'type': 'tool_use'}]
    Tool Calls:
      get_weather (toolu_01LdmBXYeccWKdPrhZSwFCDX)
     Call ID: toolu_01LdmBXYeccWKdPrhZSwFCDX
      Args:
        location: San Francisco
    =================================[1m Tool Message [0m=================================
    Name: get_weather
    
    It's 60 degrees and foggy.
    ==================================[1m Ai Message [0m==================================
    
    The weather in San Francisco is currently 60 degrees with foggy conditions.
    
    
    
    # example with a multiple tool calls in succession
    
    for chunk in app.stream(
        {"messages": [("human", "what's the weather in the coolest cities?")]},
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()
    
    
    
    ================================[1m Human Message [0m=================================
    
    what's the weather in the coolest cities?
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "Okay, let's find out the weather in the coolest cities:", 'type': 'text'}, {'id': 'toolu_01LFZUWTccyveBdaSAisMi95', 'input': {}, 'name': 'get_coolest_cities', 'type': 'tool_use'}]
    Tool Calls:
      get_coolest_cities (toolu_01LFZUWTccyveBdaSAisMi95)
     Call ID: toolu_01LFZUWTccyveBdaSAisMi95
      Args:
    =================================[1m Tool Message [0m=================================
    Name: get_coolest_cities
    
    nyc, sf
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "Now let's get the weather for those cities:", 'type': 'text'}, {'id': 'toolu_01RHPQBhT1u6eDnPqqkGUpsV', 'input': {'location': 'nyc'}, 'name': 'get_weather', 'type': 'tool_use'}]
    Tool Calls:
      get_weather (toolu_01RHPQBhT1u6eDnPqqkGUpsV)
     Call ID: toolu_01RHPQBhT1u6eDnPqqkGUpsV
      Args:
        location: nyc
    =================================[1m Tool Message [0m=================================
    Name: get_weather
    
    It's 90 degrees and sunny.
    ==================================[1m Ai Message [0m==================================
    
    [{'id': 'toolu_01W5sFGF8PfgYzdY4CqT5c6e', 'input': {'location': 'sf'}, 'name': 'get_weather', 'type': 'tool_use'}]
    Tool Calls:
      get_weather (toolu_01W5sFGF8PfgYzdY4CqT5c6e)
     Call ID: toolu_01W5sFGF8PfgYzdY4CqT5c6e
      Args:
        location: sf
    =================================[1m Tool Message [0m=================================
    Name: get_weather
    
    It's 60 degrees and foggy.
    ==================================[1m Ai Message [0m==================================
    
    Based on the results, it looks like the weather in the coolest cities is:
    - New York City: 90 degrees and sunny
    - San Francisco: 60 degrees and foggy
    
    So the weather in the coolest cities is a mix of warm and cool temperatures, with some sunny and some foggy conditions.
    

`ToolNode` can also handle errors during tool execution. You can enable /
disable this by setting `handle_tool_errors=True` (enabled by default). See
our guide on handling errors in `ToolNode` here

## Comments

Back to top

Previous

How to disable streaming for models that don't support it

Next

How to handle tool calling errors

Made with  Material for MkDocs Insiders