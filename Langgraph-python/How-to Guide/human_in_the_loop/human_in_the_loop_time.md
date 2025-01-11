## Table of Contents

- [How to view and update past graph state¶](#how-to-view-and-update-past-graph-state)
  - [Setup¶](#setup)
  - [Build the agent¶](#build-the-agent)
  - [Interacting with the Agent¶](#interacting-with-the-agent)
  - [Checking history¶](#checking-history)
  - [Replay a state¶](#replay-a-state)
  - [Branch off a past state¶](#branch-off-a-past-state)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to view and update past graph state

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
      * Human-in-the-loop  Human-in-the-loop 
        * Human-in-the-loop 
        * How to add breakpoints 
        * How to add dynamic breakpoints with NodeInterrupt 
        * How to edit graph state 
        * How to wait for user input using interrupt 
        * How to view and update past graph state  How to view and update past graph state  Table of contents 
          * Setup 
          * Build the agent 
          * Interacting with the Agent 
          * Checking history 
          * Replay a state 
          * Branch off a past state 
        * How to Review Tool Calls 
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
  * Interacting with the Agent 
  * Checking history 
  * Replay a state 
  * Branch off a past state 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Human-in-the-loop 

# How to view and update past graph state¶

Prerequisites

This guide assumes familiarity with the following concepts:

  * Time Travel
  * Breakpoints
  * LangGraph Glossary

Once you start checkpointing your graphs, you can easily **get** or **update**
the state of the agent at any point in time. This permits a few things:

  1. You can surface a state during an interrupt to a user to let them accept an action.
  2. You can **rewind** the graph to reproduce or avoid issues.
  3. You can **modify** the state to embed your agent into a larger system, or to let the user better control its actions.

The key methods used for this functionality are:

  * get_state: fetch the values from the target config
  * update_state: apply the given values to the target state

**Note:** this requires passing in a checkpointer.

Below is a quick example.

## Setup¶

First we need to install the packages required

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_openai
    

Next, we need to set API keys for OpenAI (the LLM we will use)

    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("OPENAI_API_KEY")
    
    
    
    ANTHROPIC_API_KEY:  ········
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Build the agent¶

We can now build the agent. We will build a relatively simple ReAct-style
agent that does tool calling. We will use Anthropic's models and fake tools
(just for demo purposes).

    
    
    # Set up the tool
    from langchain_openai import ChatOpenAI
    from langchain_core.tools import tool
    from langgraph.graph import MessagesState, START
    from langgraph.prebuilt import ToolNode
    from langgraph.graph import END, StateGraph
    from langgraph.checkpoint.memory import MemorySaver
    
    
    @tool
    def play_song_on_spotify(song: str):
        """Play a song on Spotify"""
        # Call the spotify API ...
        return f"Successfully played {song} on Spotify!"
    
    
    @tool
    def play_song_on_apple(song: str):
        """Play a song on Apple Music"""
        # Call the apple music API ...
        return f"Successfully played {song} on Apple Music!"
    
    
    tools = [play_song_on_apple, play_song_on_spotify]
    tool_node = ToolNode(tools)
    
    # Set up the model
    
    model = ChatOpenAI(model="gpt-4o-mini")
    model = model.bind_tools(tools, parallel_tool_calls=False)
    
    
    # Define nodes and conditional edges
    
    
    # Define the function that determines whether to continue or not
    def should_continue(state):
        messages = state["messages"]
        last_message = messages[-1]
        # If there is no function call, then we finish
        if not last_message.tool_calls:
            return "end"
        # Otherwise if there is, we continue
        else:
            return "continue"
    
    
    # Define the function that calls the model
    def call_model(state):
        messages = state["messages"]
        response = model.invoke(messages)
        # We return a list, because this will get added to the existing list
        return {"messages": [response]}
    
    
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
        # Finally we pass in a mapping.
        # The keys are strings, and the values are other nodes.
        # END is a special node marking that the graph should finish.
        # What will happen is we will call `should_continue`, and then the output of that
        # will be matched against the keys in this mapping.
        # Based on which one it matches, that node will then be called.
        {
            # If `tools`, then we call the tool node.
            "continue": "action",
            # Otherwise we finish.
            "end": END,
        },
    )
    
    # We now add a normal edge from `tools` to `agent`.
    # This means that after `tools` is called, `agent` node is called next.
    workflow.add_edge("action", "agent")
    
    # Set up memory
    memory = MemorySaver()
    
    # Finally, we compile it!
    # This compiles it into a LangChain Runnable,
    # meaning you can use it as you would any other runnable
    
    # We add in `interrupt_before=["action"]`
    # This will add a breakpoint before the `action` node is called
    app = workflow.compile(checkpointer=memory)
    

API Reference: ChatOpenAI | tool | START | ToolNode | END | StateGraph | MemorySaver

## Interacting with the Agent¶

We can now interact with the agent. Let's ask it to play Taylor Swift's most
popular song:

    
    
    from langchain_core.messages import HumanMessage
    
    config = {"configurable": {"thread_id": "1"}}
    input_message = HumanMessage(content="Can you play Taylor Swift's most popular song?")
    for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
        event["messages"][-1].pretty_print()
    

API Reference: HumanMessage

    
    
    ================================[1m Human Message [0m=================================
    
    Can you play Taylor Swift's most popular song?
    ==================================[1m Ai Message [0m==================================
    Tool Calls:
      play_song_on_apple (call_uhGY6Fv6Mr4ZOhSokintuoD7)
     Call ID: call_uhGY6Fv6Mr4ZOhSokintuoD7
      Args:
        song: Anti-Hero by Taylor Swift
    =================================[1m Tool Message [0m=================================
    Name: play_song_on_apple
    
    Succesfully played Anti-Hero by Taylor Swift on Apple Music!
    ==================================[1m Ai Message [0m==================================
    
    I've successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!
    

## Checking history¶

Let's browse the history of this thread, from start to finish.

    
    
    app.get_state(config).values["messages"]
    
    
    
    [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
     AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}),
     ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7'),
     AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]
    
    
    
    all_states = []
    for state in app.get_state_history(config):
        print(state)
        all_states.append(state)
        print("--")
    
    
    
    StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}), ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7'), AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}, next=(), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-364f-6228-8003-dd67a426334e'}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='I\'ve successfully played "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-bfee6b28-9f16-49cc-8d28-bfb5a5b9aea1-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}}, 'step': 3, 'parents': {}}, created_at='2024-09-05T21:37:39.955948+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-318f-6dc8-8002-dbdf9aaeac83'}}, tasks=())
    --
    StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102}), ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}, next=('agent',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-318f-6dc8-8002-dbdf9aaeac83'}}, metadata={'source': 'loop', 'writes': {'action': {'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', id='43a39ca7-326a-4033-8607-bf061615ed6b', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}}, 'step': 2, 'parents': {}}, created_at='2024-09-05T21:37:39.458185+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-3185-663e-8001-12b1ec3114b8'}}, tasks=(PregelTask(id='3a4c5ddb-14b2-5def-a766-02ddc32948ba', name='agent', error=None, interrupts=(), state=None),))
    --
    StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}, next=('action',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-3185-663e-8001-12b1ec3114b8'}}, metadata={'source': 'loop', 'writes': {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}}, 'step': 1, 'parents': {}}, created_at='2024-09-05T21:37:39.453898+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b8-6370-8000-f9f6e7ca1b06'}}, tasks=(PregelTask(id='01f1dc72-5a39-5876-97a6-abdc12f70c2a', name='action', error=None, interrupts=(), state=None),))
    --
    StateSnapshot(values={'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b')]}, next=('agent',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b8-6370-8000-f9f6e7ca1b06'}}, metadata={'source': 'loop', 'writes': None, 'step': 0, 'parents': {}}, created_at='2024-09-05T21:37:38.635849+00:00', parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b3-6514-bfff-fe07fb36f14f'}}, tasks=(PregelTask(id='348e1ba7-95c6-5b89-80c9-1fc4720e35ef', name='agent', error=None, interrupts=(), state=None),))
    --
    StateSnapshot(values={'messages': []}, next=('__start__',), config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1ef6bcf1-29b3-6514-bfff-fe07fb36f14f'}}, metadata={'source': 'input', 'writes': {'__start__': {'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?")]}}, 'step': -1, 'parents': {}}, created_at='2024-09-05T21:37:38.633849+00:00', parent_config=None, tasks=(PregelTask(id='f1cfbb8c-7792-5cf9-9d28-ae3ac7724cf3', name='__start__', error=None, interrupts=(), state=None),))
    --
    

## Replay a state¶

We can go back to any of these states and restart the agent from there! Let's
go back to right before the tool call gets executed.

    
    
    to_replay = all_states[2]
    
    
    
    to_replay.values
    
    
    
    {'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
      AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'function': {'arguments': '{"song":"Anti-Hero by Taylor Swift"}', 'name': 'play_song_on_apple'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 80, 'total_tokens': 102}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0', tool_calls=[{'name': 'play_song_on_apple', 'args': {'song': 'Anti-Hero by Taylor Swift'}, 'id': 'call_uhGY6Fv6Mr4ZOhSokintuoD7', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 22, 'total_tokens': 102})]}
    
    
    
    to_replay.next
    
    
    
    ('action',)
    

To replay from this place we just need to pass its config back to the agent.
Notice that it just resumes from right where it left all - making a tool call.

    
    
    for event in app.stream(None, to_replay.config):
        for v in event.values():
            print(v)
    
    
    
    {'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Apple Music!', name='play_song_on_apple', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}
    {'messages': [AIMessage(content='I\'ve started playing "Anti-Hero" by Taylor Swift on Apple Music! Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 126, 'total_tokens': 146}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-dc338bbd-d623-40bb-b824-5d2307954b57-0', usage_metadata={'input_tokens': 126, 'output_tokens': 20, 'total_tokens': 146})]}
    

## Branch off a past state¶

Using LangGraph's checkpointing, you can do more than just replay past states.
You can branch off previous locations to let the agent explore alternate
trajectories or to let a user "version control" changes in a workflow.

Let's show how to do this to edit the state at a particular point in time.
Let's update the state to instead of playing the song on Apple to play it on
Spotify:

    
    
    # Let's now get the last message in the state
    # This is the one with the tool calls that we want to update
    last_message = to_replay.values["messages"][-1]
    
    
    # Let's now update the tool we are calling
    last_message.tool_calls[0]["name"] = "play_song_on_spotify"
    
    branch_config = app.update_state(
        to_replay.config,
        {"messages": [last_message]},
    )
    

We can then invoke with this new `branch_config` to resume running from here
with changed state. We can see from the log that the tool was called with
different input.

    
    
    for event in app.stream(None, branch_config):
        for v in event.values():
            print(v)
    
    
    
    {'messages': [ToolMessage(content='Succesfully played Anti-Hero by Taylor Swift on Spotify!', name='play_song_on_spotify', tool_call_id='call_uhGY6Fv6Mr4ZOhSokintuoD7')]}
    {'messages': [AIMessage(content='I\'ve started playing "Anti-Hero" by Taylor Swift on Spotify. Enjoy the music!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 125, 'total_tokens': 144}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'stop', 'logprobs': None}, id='run-7d8d5094-7029-4da3-9e0e-ef9d18b63615-0', usage_metadata={'input_tokens': 125, 'output_tokens': 19, 'total_tokens': 144})]}
    

Alternatively, we could update the state to not even call a tool!

    
    
    from langchain_core.messages import AIMessage
    
    # Let's now get the last message in the state
    # This is the one with the tool calls that we want to update
    last_message = to_replay.values["messages"][-1]
    
    # Let's now get the ID for the last message, and create a new message with that ID.
    new_message = AIMessage(
        content="It's quiet hours so I can't play any music right now!", id=last_message.id
    )
    
    branch_config = app.update_state(
        to_replay.config,
        {"messages": [new_message]},
    )
    

API Reference: AIMessage

    
    
    branch_state = app.get_state(branch_config)
    
    
    
    branch_state.values
    
    
    
    {'messages': [HumanMessage(content="Can you play Taylor Swift's most popular song?", id='7e32f0f3-75f5-48e1-a4ae-d38ccc15973b'),
      AIMessage(content="It's quiet hours so I can't play any music right now!", id='run-af077bc4-f03c-4afe-8d92-78bdae394412-0')]}
    
    
    
    branch_state.next
    
    
    
    ()
    

You can see the snapshot was updated and now correctly reflects that there is
no next step.

## Comments

Back to top

Previous

How to wait for user input using interrupt

Next

How to Review Tool Calls

Made with  Material for MkDocs Insiders