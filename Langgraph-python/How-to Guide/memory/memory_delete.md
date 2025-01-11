## Table of Contents

- [How to delete messages¶](#how-to-delete-messages)
  - [Setup¶](#setup)
  - [Build the agent¶](#build-the-agent)
  - [Manually deleting messages¶](#manually-deleting-messages)
  - [Programmatically deleting messages¶](#programmatically-deleting-messages)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to delete messages

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
        * How to manage conversation history 
        * How to delete messages  How to delete messages  Table of contents 
          * Setup 
          * Build the agent 
          * Manually deleting messages 
          * Programmatically deleting messages 
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
  * Manually deleting messages 
  * Programmatically deleting messages 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Memory 

# How to delete messages¶

One of the common states for a graph is a list of messages. Usually you only
add messages to that state. However, sometimes you may want to remove messages
(either by directly modifying the state or as part of the graph). To do that,
you can use the `RemoveMessage` modifier. In this guide, we will cover how to
do that.

The key idea is that each state key has a `reducer` key. This key specifies
how to combine updates to the state. The default `MessagesState` has a
messages key, and the reducer for that key accepts these `RemoveMessage`
modifiers. That reducer then uses these `RemoveMessage` to delete messages
from the key.

So note that just because your graph state has a key that is a list of
messages, it doesn't mean that that this `RemoveMessage` modifier will work.
You also have to have a `reducer` defined that knows how to work with this.

**NOTE** : Many models expect certain rules around lists of messages. For
example, some expect them to start with a `user` message, others expect all
messages with tool calls to be followed by a tool message. **When deleting
messages, you will want to make sure you don't violate these rules.**

## Setup¶

First, let's build a simple graph that uses messages. Note that it's using the
`MessagesState` which has the required `reducer`.

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_anthropic
    

Next, we need to set API keys for Anthropic (the LLM we will use)

    
    
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
        response = model.invoke(state["messages"])
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
    
    It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. I'm here to help out with any questions or tasks you might have. Please let me know if there's anything I can assist you with.
    ================================[1m Human Message [0m=================================
    
    what's my name?
    ==================================[1m Ai Message [0m==================================
    
    You said your name is Bob.
    

## Manually deleting messages¶

First, we will cover how to manually delete messages. Let's take a look at the
current state of the thread:

    
    
    messages = app.get_state(config).values["messages"]
    messages
    
    
    
    [HumanMessage(content="hi! I'm bob", additional_kwargs={}, response_metadata={}, id='db576005-3a60-4b3b-8925-dc602ac1c571'),
     AIMessage(content="It's nice to meet you, Bob! I'm an AI assistant created by Anthropic. I'm here to help out with any questions or tasks you might have. Please let me know if there's anything I can assist you with.", additional_kwargs={}, response_metadata={'id': 'msg_01BKAnYxmoC6bQ9PpCuHk8ZT', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 52}}, id='run-3a60c536-b207-4c56-98f3-03f94d49a9e4-0', usage_metadata={'input_tokens': 12, 'output_tokens': 52, 'total_tokens': 64}),
     HumanMessage(content="what's my name?", additional_kwargs={}, response_metadata={}, id='2088c465-400b-430b-ad80-fad47dc1f2d6'),
     AIMessage(content='You said your name is Bob.', additional_kwargs={}, response_metadata={'id': 'msg_013UWTLTzwZi81vke8mMQ2KP', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 72, 'output_tokens': 10}}, id='run-3a6883be-0c52-4938-af98-e9e7476659eb-0', usage_metadata={'input_tokens': 72, 'output_tokens': 10, 'total_tokens': 82})]
    

We can call `update_state` and pass in the id of the first message. This will
delete that message.

    
    
    from langchain_core.messages import RemoveMessage
    
    app.update_state(config, {"messages": RemoveMessage(id=messages[0].id)})
    

API Reference: RemoveMessage

    
    
    {'configurable': {'thread_id': '2',
      'checkpoint_ns': '',
      'checkpoint_id': '1ef75157-f251-6a2a-8005-82a86a6593a0'}}
    

If we now look at the messages, we can verify that the first one was deleted.

    
    
    messages = app.get_state(config).values["messages"]
    messages
    
    
    
    [AIMessage(content="It's nice to meet you, Bob! I'm Claude, an AI assistant created by Anthropic. How can I assist you today?", response_metadata={'id': 'msg_01XPSAenmSqK8rX2WgPZHfz7', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 32}}, id='run-1c69af09-adb1-412d-9010-2456e5a555fb-0', usage_metadata={'input_tokens': 12, 'output_tokens': 32, 'total_tokens': 44}),
     HumanMessage(content="what's my name?", id='f3c71afe-8ce2-4ed0-991e-65021f03b0a5'),
     AIMessage(content='Your name is Bob, as you introduced yourself at the beginning of our conversation.', response_metadata={'id': 'msg_01BPZdwsjuMAbC1YAkqawXaF', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 52, 'output_tokens': 19}}, id='run-b2eb9137-2f4e-446f-95f5-3d5f621a2cf8-0', usage_metadata={'input_tokens': 52, 'output_tokens': 19, 'total_tokens': 71})]
    

## Programmatically deleting messages¶

We can also delete messages programmatically from inside the graph. Here we'll
modify the graph to delete any old messages (longer than 3 messages ago) at
the end of a graph run.

    
    
    from langchain_core.messages import RemoveMessage
    from langgraph.graph import END
    
    
    def delete_messages(state):
        messages = state["messages"]
        if len(messages) > 3:
            return {"messages": [RemoveMessage(id=m.id) for m in messages[:-3]]}
    
    
    # We need to modify the logic to call delete_messages rather than end right away
    def should_continue(state: MessagesState) -> Literal["action", "delete_messages"]:
        """Return the next node to execute."""
        last_message = state["messages"][-1]
        # If there is no function call, then we call our delete_messages function
        if not last_message.tool_calls:
            return "delete_messages"
        # Otherwise if there is, we continue
        return "action"
    
    
    # Define a new graph
    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)
    
    # This is our new node we're defining
    workflow.add_node(delete_messages)
    
    
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
    )
    workflow.add_edge("action", "agent")
    
    # This is the new edge we're adding: after we delete messages, we finish
    workflow.add_edge("delete_messages", END)
    app = workflow.compile(checkpointer=memory)
    

API Reference: RemoveMessage | END

We can now try this out. We can call the graph twice and then check the state

    
    
    from langchain_core.messages import HumanMessage
    
    config = {"configurable": {"thread_id": "3"}}
    input_message = HumanMessage(content="hi! I'm bob")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        print([(message.type, message.content) for message in event["messages"]])
    
    
    input_message = HumanMessage(content="what's my name?")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        print([(message.type, message.content) for message in event["messages"]])
    

API Reference: HumanMessage

    
    
    [('human', "hi! I'm bob")]
    [('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you.")]
    [('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?")]
    [('human', "hi! I'm bob"), ('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?"), ('ai', 'You said your name is Bob, so that is the name I have for you.')]
    [('ai', "Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you."), ('human', "what's my name?"), ('ai', 'You said your name is Bob, so that is the name I have for you.')]
    

If we now check the state, we should see that it is only three messages long.
This is because we just deleted the earlier messages - otherwise it would be
four!

    
    
    messages = app.get_state(config).values["messages"]
    messages
    
    
    
    [AIMessage(content="Hello Bob! It's nice to meet you. I'm an AI assistant created by Anthropic. I'm here to help with any questions or tasks you might have. Please let me know how I can assist you.", response_metadata={'id': 'msg_01XPEgPPbcnz5BbGWUDWTmzG', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 48}}, id='run-eded3820-b6a9-4d66-9210-03ca41787ce6-0', usage_metadata={'input_tokens': 12, 'output_tokens': 48, 'total_tokens': 60}),
     HumanMessage(content="what's my name?", id='a0ea2097-3280-402b-92e1-67177b807ae8'),
     AIMessage(content='You said your name is Bob, so that is the name I have for you.', response_metadata={'id': 'msg_01JGT62pxhrhN4SykZ57CSjW', 'model': 'claude-3-haiku-20240307', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 68, 'output_tokens': 20}}, id='run-ace3519c-81f8-45fe-a777-91f42d48b3a3-0', usage_metadata={'input_tokens': 68, 'output_tokens': 20, 'total_tokens': 88})]
    

Remember, when deleting messages you will want to make sure that the remaining
message list is still valid. This message list **may actually not be** \- this
is because it currently starts with an AI message, which some models do not
allow.

## Comments

Back to top

Previous

How to manage conversation history

Next

How to add summary of the conversation history

Made with  Material for MkDocs Insiders