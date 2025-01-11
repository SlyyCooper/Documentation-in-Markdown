## Table of Contents

- [How to Review Tool Calls¶](#how-to-review-tool-calls)
  - [Setup¶](#setup)
  - [Simple Usage¶](#simple-usage)
  - [Example with no review¶](#example-with-no-review)
  - [Example of approving tool¶](#example-of-approving-tool)
  - [Edit Tool Call¶](#edit-tool-call)
  - [Give feedback to a tool call¶](#give-feedback-to-a-tool-call)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to Review Tool Calls

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
        * How to view and update past graph state 
        * How to Review Tool Calls  How to Review Tool Calls  Table of contents 
          * Setup 
          * Simple Usage 
          * Example with no review 
          * Example of approving tool 
          * Edit Tool Call 
          * Give feedback to a tool call 
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
  * Simple Usage 
  * Example with no review 
  * Example of approving tool 
  * Edit Tool Call 
  * Give feedback to a tool call 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Human-in-the-loop 

# How to Review Tool Calls¶

Prerequisites

This guide assumes familiarity with the following concepts:

  * Tool calling
  * Human-in-the-loop
  * LangGraph Glossary

Human-in-the-loop (HIL) interactions are crucial for agentic systems. A common
pattern is to add some human in the loop step after certain tool calls. These
tool calls often lead to either a function call or saving of some information.
Examples include:

  * A tool call to execute SQL, which will then be run by the tool
  * A tool call to generate a summary, which will then be saved to the State of the graph

Note that using tool calls is common **whether actually calling tools or
not**.

There are typically a few different interactions you may want to do here:

  1. Approve the tool call and continue
  2. Modify the tool call manually and then continue
  3. Give natural language feedback, and then pass that back to the agent

We can implement these in LangGraph using the `interrupt()` function.
`interrupt` allows us to stop graph execution to collect input from a user and
continue execution with collected input:

    
    
    def human_review_node(state) -> Command[Literal["call_llm", "run_tool"]]:
        # this is the value we'll be providing via Command(resume=<human_review>)
        human_review = interrupt(
            {
                "question": "Is this correct?",
                # Surface tool calls for review
                "tool_call": tool_call
            }
        )
    
        review_action, review_data = human_review
    
        # Approve the tool call and continue
        if review_action == "continue":
            return Command(goto="run_tool")
    
        # Modify the tool call manually and then continue
        elif review_action == "update":
            ...
            updated_msg = get_updated_msg(review_data)
            return Command(goto="run_tool", update={"messages": [updated_message]})
    
        # Give natural language feedback, and then pass that back to the agent
        elif review_action == "feedback":
            ...
            feedback_msg = get_feedback_msg(review_data)
            return Command(goto="call_llm", update={"messages": [feedback_msg]})
    

## Setup¶

First we need to install the packages required

    
    
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

## Simple Usage¶

Let's set up a very simple graph that facilitates this. First, we will have an
LLM call that decides what action to take. Then we go to a human node. This
node actually doesn't do anything - the idea is that we interrupt before this
node and then apply any updates to the state. After that, we check the state
and either route back to the LLM or to the correct tool.

Let's see this in action!

    
    
    from typing_extensions import TypedDict, Literal
    from langgraph.graph import StateGraph, START, END, MessagesState
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.types import Command, interrupt
    from langchain_anthropic import ChatAnthropic
    from langchain_core.tools import tool
    from langchain_core.messages import AIMessage
    from IPython.display import Image, display
    
    
    @tool
    def weather_search(city: str):
        """Search for the weather"""
        print("----")
        print(f"Searching for: {city}")
        print("----")
        return "Sunny!"
    
    
    model = ChatAnthropic(model_name="claude-3-5-sonnet-latest").bind_tools(
        [weather_search]
    )
    
    
    class State(MessagesState):
        """Simple state."""
    
    
    def call_llm(state):
        return {"messages": [model.invoke(state["messages"])]}
    
    
    def human_review_node(state) -> Command[Literal["call_llm", "run_tool"]]:
        last_message = state["messages"][-1]
        tool_call = last_message.tool_calls[-1]
    
        # this is the value we'll be providing via Command(resume=<human_review>)
        human_review = interrupt(
            {
                "question": "Is this correct?",
                # Surface tool calls for review
                "tool_call": tool_call,
            }
        )
    
        review_action = human_review["action"]
        review_data = human_review.get("data")
    
        # if approved, call the tool
        if review_action == "continue":
            return Command(goto="run_tool")
    
        # update the AI message AND call tools
        elif review_action == "update":
            updated_message = {
                "role": "ai",
                "content": last_message.content,
                "tool_calls": [
                    {
                        "id": tool_call["id"],
                        "name": tool_call["name"],
                        # This the update provided by the human
                        "args": review_data,
                    }
                ],
                # This is important - this needs to be the same as the message you replacing!
                # Otherwise, it will show up as a separate message
                "id": last_message.id,
            }
            return Command(goto="run_tool", update={"messages": [updated_message]})
    
        # provide feedback to LLM
        elif review_action == "feedback":
            # NOTE: we're adding feedback message as a ToolMessage
            # to preserve the correct order in the message history
            # (AI messages with tool calls need to be followed by tool call messages)
            tool_message = {
                "role": "tool",
                # This is our natural language feedback
                "content": review_data,
                "name": tool_call["name"],
                "tool_call_id": tool_call["id"],
            }
            return Command(goto="call_llm", update={"messages": [tool_message]})
    
    
    def run_tool(state):
        new_messages = []
        tools = {"weather_search": weather_search}
        tool_calls = state["messages"][-1].tool_calls
        for tool_call in tool_calls:
            tool = tools[tool_call["name"]]
            result = tool.invoke(tool_call["args"])
            new_messages.append(
                {
                    "role": "tool",
                    "name": tool_call["name"],
                    "content": result,
                    "tool_call_id": tool_call["id"],
                }
            )
        return {"messages": new_messages}
    
    
    def route_after_llm(state) -> Literal[END, "human_review_node"]:
        if len(state["messages"][-1].tool_calls) == 0:
            return END
        else:
            return "human_review_node"
    
    
    builder = StateGraph(State)
    builder.add_node(call_llm)
    builder.add_node(run_tool)
    builder.add_node(human_review_node)
    builder.add_edge(START, "call_llm")
    builder.add_conditional_edges("call_llm", route_after_llm)
    builder.add_edge("run_tool", "call_llm")
    
    # Set up memory
    memory = MemorySaver()
    
    # Add
    graph = builder.compile(checkpointer=memory)
    
    # View
    display(Image(graph.get_graph().draw_mermaid_png()))
    

API Reference: ChatAnthropic | tool | AIMessage | StateGraph | START | END | MemorySaver | Command | interrupt

## Example with no review¶

Let's look at an example when no review is required (because no tools are
called)

    
    
    # Input
    initial_input = {"messages": [{"role": "user", "content": "hi!"}]}
    
    # Thread
    thread = {"configurable": {"thread_id": "1"}}
    
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="updates"):
        print(event)
        print("\n")
    
    
    
    {'call_llm': {'messages': [AIMessage(content="Hello! I'm here to help you. I can assist you with checking the weather in different cities using the weather search tool. Would you like to know the weather for a specific city? Just let me know which city you're interested in!", additional_kwargs={}, response_metadata={'id': 'msg_01XHvA3ZWpsq4PdyiruWFLBs', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 374, 'output_tokens': 52}}, id='run-c3ff5fea-0135-4d66-8ec1-f8ed6a88356b-0', usage_metadata={'input_tokens': 374, 'output_tokens': 52, 'total_tokens': 426, 'input_token_details': {}})]}}
    

If we check the state, we can see that it is finished

## Example of approving tool¶

Let's now look at what it looks like to approve a tool call

    
    
    # Input
    initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
    
    # Thread
    thread = {"configurable": {"thread_id": "2"}}
    
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="updates"):
        print(event)
        print("\n")
    
    
    
    {'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_013eJXUAEA2ANvYLkDUQFRPo', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-e8174b94-f681-4688-967f-a32295412f91-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
    
    
    {'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:be252162-5b29-0a98-1ed2-c807c1fc64c6'], when='during'),)}
    

If we now check, we can see that it is waiting on human review

    
    
    print("Pending Executions!")
    print(graph.get_state(thread).next)
    
    
    
    Pending Executions!
    ('human_review_node',)
    

To approve the tool call, we can just continue the thread with no edits. To do
so, we need to let `human_review_node` know what value to use for the
`human_review` variable we defined inside the node. We can provide this value
by invoking the graph with a `Command(resume=<human_review>)` input. Since
we're approving the tool call, we'll provide `resume` value of `{"action":
"continue"}` to navigate to `run_tool` node:

    
    
    for event in graph.stream(
        # provide value
        Command(resume={"action": "continue"}),
        thread,
        stream_mode="updates",
    ):
        print(event)
        print("\n")
    
    
    
    {'human_review_node': None}
    
    
    ----
    Searching for: sf
    ----
    {'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_01Kn67GmQAA3BEF1cfYdNW3c'}]}}
    
    
    {'call_llm': {'messages': [AIMessage(content="According to the search, it's sunny in San Francisco today!", additional_kwargs={}, response_metadata={'id': 'msg_01FJTbC8oK5fkD73rUBmAtUx', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 457, 'output_tokens': 17}}, id='run-c21af72d-3cc5-4b74-bb7c-fbeb8f88bd6d-0', usage_metadata={'input_tokens': 457, 'output_tokens': 17, 'total_tokens': 474, 'input_token_details': {}})]}}
    

## Edit Tool Call¶

Let's now say we want to edit the tool call. E.g. change some of the
parameters (or even the tool called!) but then execute that tool.

    
    
    # Input
    initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
    
    # Thread
    thread = {"configurable": {"thread_id": "3"}}
    
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="updates"):
        print(event)
        print("\n")
    
    
    
    {'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_013ruFpCRNZKX3cDeBAH8rEb', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-13df3982-ce6d-4fe2-9e5c-ea6ce30a63e4-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
    
    
    {'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:da717c23-60a0-2a1a-45de-cac5cff308bb'], when='during'),)}
    
    
    
    print("Pending Executions!")
    print(graph.get_state(thread).next)
    
    
    
    Pending Executions!
    ('human_review_node',)
    

To do this, we will use `Command` with a different resume value of `{"action":
"update", "data": <tool call args>}`. This will do the following:

  * combine existing tool call with user-provided tool call arguments and update the existing AI message with the new tool call
  * navigate to `run_tool` node with the updated AI message and continue execution

    
    
    # Let's now continue executing from here
    for event in graph.stream(
        Command(resume={"action": "update", "data": {"city": "San Francisco, USA"}}),
        thread,
        stream_mode="updates",
    ):
        print(event)
        print("\n")
    
    
    
    {'human_review_node': {'messages': [{'role': 'ai', 'content': [{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], 'tool_calls': [{'id': 'toolu_013eUXow3jwM6eekcDJdrjDa', 'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}}], 'id': 'run-13df3982-ce6d-4fe2-9e5c-ea6ce30a63e4-0'}]}}
    
    
    ----
    Searching for: San Francisco, USA
    ----
    {'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_013eUXow3jwM6eekcDJdrjDa'}]}}
    
    
    {'call_llm': {'messages': [AIMessage(content="According to the search, it's sunny in San Francisco right now!", additional_kwargs={}, response_metadata={'id': 'msg_01QssVtxXPqr8NWjYjTaiHqN', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 460, 'output_tokens': 18}}, id='run-8ab865c8-cc9e-4300-8e1d-9eb673e8445c-0', usage_metadata={'input_tokens': 460, 'output_tokens': 18, 'total_tokens': 478, 'input_token_details': {}})]}}
    

## Give feedback to a tool call¶

Sometimes, you may not want to execute a tool call, but you also may not want
to ask the user to manually modify the tool call. In that case it may be
better to get natural language feedback from the user. You can then insert
this feedback as a mock **RESULT** of the tool call.

There are multiple ways to do this:

  1. You could add a new message to the state (representing the "result" of a tool call)
  2. You could add TWO new messages to the state - one representing an "error" from the tool call, other HumanMessage representing the feedback

Both are similar in that they involve adding messages to the state. The main
difference lies in the logic AFTER the `human_review_node` and how it handles
different types of messages.

For this example we will just add a single tool call representing the feedback
(see `human_review_node` implementation). Let's see this in action!

    
    
    # Input
    initial_input = {"messages": [{"role": "user", "content": "what's the weather in sf?"}]}
    
    # Thread
    thread = {"configurable": {"thread_id": "4"}}
    
    # Run the graph until the first interruption
    for event in graph.stream(initial_input, thread, stream_mode="updates"):
        print(event)
        print("\n")
    
    
    
    {'call_llm': {'messages': [AIMessage(content=[{'text': "I'll help you check the weather in San Francisco.", 'type': 'text'}, {'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'input': {'city': 'sf'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_01DjwkVxgfqT2K329rGkycx6', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 379, 'output_tokens': 65}}, id='run-c57bee36-9f5f-4d2e-85df-758b56d3cc05-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'type': 'tool_call'}], usage_metadata={'input_tokens': 379, 'output_tokens': 65, 'total_tokens': 444, 'input_token_details': {}})]}}
    
    
    {'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'sf'}, 'id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:47a3f541-b630-5f8a-32d7-5a44826d99da'], when='during'),)}
    
    
    
    print("Pending Executions!")
    print(graph.get_state(thread).next)
    
    
    
    Pending Executions!
    ('human_review_node',)
    

To do this, we will use `Command` with a different resume value of `{"action":
"feedback", "data": <feedback string>}`. This will do the following:

  * create a new tool message that combines existing tool call from LLM with the with user-provided feedback as content
  * navigate to `call_llm` node with the updated tool message and continue execution

    
    
    # Let's now continue executing from here
    for event in graph.stream(
        # provide our natural language feedback!
        Command(
            resume={
                "action": "feedback",
                "data": "User requested changes: use <city, country> format for location",
            }
        ),
        thread,
        stream_mode="updates",
    ):
        print(event)
        print("\n")
    
    
    
    {'human_review_node': {'messages': [{'role': 'tool', 'content': 'User requested changes: use <city, country> format for location', 'name': 'weather_search', 'tool_call_id': 'toolu_01QxXNTCasnNLQCGAiVoNUBe'}]}}
    
    
    {'call_llm': {'messages': [AIMessage(content=[{'text': 'Let me try again with the full city name.', 'type': 'text'}, {'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'input': {'city': 'San Francisco, USA'}, 'name': 'weather_search', 'type': 'tool_use'}], additional_kwargs={}, response_metadata={'id': 'msg_0141KCdx6KhJmWXyYwAYGvmj', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'tool_use', 'stop_sequence': None, 'usage': {'input_tokens': 468, 'output_tokens': 68}}, id='run-60c8267a-52c7-4b6e-87ca-16aa3bd6266b-0', tool_calls=[{'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'type': 'tool_call'}], usage_metadata={'input_tokens': 468, 'output_tokens': 68, 'total_tokens': 536, 'input_token_details': {}})]}}
    
    
    {'__interrupt__': (Interrupt(value={'question': 'Is this correct?', 'tool_call': {'name': 'weather_search', 'args': {'city': 'San Francisco, USA'}, 'id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ', 'type': 'tool_call'}}, resumable=True, ns=['human_review_node:621fc4a9-bbf1-9a99-f50b-3bf91675234e'], when='during'),)}
    

We can see that we now get to another interrupt - because it went back to the
model and got an entirely new prediction of what to call. Let's now approve
this one and continue.

    
    
    print("Pending Executions!")
    print(graph.get_state(thread).next)
    
    
    
    Pending Executions!
    ('human_review_node',)
    
    
    
    for event in graph.stream(
        Command(resume={"action": "continue"}), thread, stream_mode="updates"
    ):
        print(event)
        print("\n")
    
    
    
    {'human_review_node': None}
    
    
    ----
    Searching for: San Francisco, USA
    ----
    {'run_tool': {'messages': [{'role': 'tool', 'name': 'weather_search', 'content': 'Sunny!', 'tool_call_id': 'toolu_01WBGTKBWusaPNZYJi5LKmeQ'}]}}
    
    
    {'call_llm': {'messages': [AIMessage(content='The weather in San Francisco is sunny!', additional_kwargs={}, response_metadata={'id': 'msg_01JrfZd8SYyH51Q8rhZuaC3W', 'model': 'claude-3-5-sonnet-20241022', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 549, 'output_tokens': 12}}, id='run-09a198b2-79fa-484d-9d9d-f12432978488-0', usage_metadata={'input_tokens': 549, 'output_tokens': 12, 'total_tokens': 561, 'input_token_details': {}})]}}
    

## Comments

Back to top

Previous

How to view and update past graph state

Next

How to stream full state of your graph

Made with  Material for MkDocs Insiders