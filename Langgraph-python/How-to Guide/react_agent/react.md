## Table of Contents

- [How to return structured output with a ReAct style agent¶](#how-to-return-structured-output-with-a-react-style-agent)
  - [Setup¶](#setup)
  - [Define model, tools, and graph state¶](#define-model-tools-and-graph-state)
  - [Option 1: Bind output as tool¶](#option-1-bind-output-as-tool)
    - [Define Graph¶](#define-graph)
    - [Usage¶](#usage)
  - [Option 2: 2 LLMs¶](#option-2-2-llms)
    - [Define Graph¶](#define-graph)
    - [Usage¶](#usage)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to return structured output with a ReAct style agent

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
      * Other  Other 
        * Other 
        * How to run a graph asynchronously 
        * How to visualize your graph 
        * How to add runtime configuration to your graph 
        * How to add node retry policies 
        * How to return structured output with a ReAct style agent  How to return structured output with a ReAct style agent  Table of contents 
          * Setup 
          * Define model, tools, and graph state 
          * Option 1: Bind output as tool 
            * Define Graph 
            * Usage 
          * Option 2: 2 LLMs 
            * Define Graph 
            * Usage 
        * How to pass custom run ID or set tags and metadata for graph runs in LangSmith 
        * How to return state before hitting recursion limit 
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
  * Define model, tools, and graph state 
  * Option 1: Bind output as tool 
    * Define Graph 
    * Usage 
  * Option 2: 2 LLMs 
    * Define Graph 
    * Usage 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Other 

# How to return structured output with a ReAct style agent¶

Prerequisites

This guide assumes familiarity with the following:

  * Structured Output 
  * Tool calling agent 
  * Chat Models 
  * Messages 
  * LangGraph Glossary 

You might want your agent to return its output in a structured format. For
example, if the output of the agent is used by some other downstream software,
you may want the output to be in the same structured format every time the
agent is invoked to ensure consistency.

This notebook will walk through two different options for forcing a tool
calling agent to structure its output. We will be using a basic ReAct agent (a
model node and a tool-calling node) together with a third node at the end that
will format response for the user. Both of the options will use the same graph
structure as shown in the diagram below, but will have different mechanisms
under the hood.

**Option 1**

The first way you can force your tool calling agent to have structured output
is to bind the output you would like as an additional tool for the `agent`
node to use. In contrast to the basic ReAct agent, the `agent` node in this
case is not selecting between `tools` and `END` but rather selecting between
the specific tools it calls. The expected flow in this case is that the LLM in
the `agent` node will first select the action tool, and after receiving the
action tool output it will call the response tool, which will then route to
the `respond` node which simply structures the arguments from the `agent` node
tool call.

**Pros and Cons**

The benefit to this format is that you only need one LLM, and can save money
and latency because of this. The downside to this option is that it isn't
guaranteed that the single LLM will call the correct tool when you want it to.
We can help the LLM by setting `tool_choice` to `any` when we use `bind_tools`
which forces the LLM to select at least one tool at every turn, but this is
far from a fool proof strategy. In addition, another downside is that the
agent might call _multiple_ tools, so we need to check for this explicitly in
our routing function (or if we are using OpenAI we an set
`parallell_tool_calling=False` to ensure only one tool is called at a time).

**Option 2**

The second way you can force your tool calling agent to have structured output
is to use a second LLM (in this case `model_with_structured_output`) to
respond to the user.

In this case, you will define a basic ReAct agent normally, but instead of
having the `agent` node choose between the `tools` node and ending the
conversation, the `agent` node will choose between the `tools` node and the
`respond` node. The `respond` node will contain a second LLM that uses
structured output, and once called will return directly to the user. You can
think of this method as basic ReAct with one extra step before responding to
the user.

**Pros and Cons**

The benefit of this method is that it guarantees structured output (as long as
`.with_structured_output` works as expected with the LLM). The downside to
using this approach is that it requires making an additional LLM call before
responding to the user, which can increase costs as well as latency. In
addition, by not providing the `agent` node LLM with information about the
desired output schema there is a risk that the `agent` LLM will fail to call
the correct tools required to answer in the correct output schema.

Note that both of these options will follow the exact same graph structure
(see the diagram above), in that they are both exact replicas of the basic
ReAct architecture but with a `respond` node before the end.

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain_anthropic
    
    
    
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

## Define model, tools, and graph state¶

Now we can define how we want to structure our output, define our graph state,
and also our tools and the models we are going to use.

To use structured output, we will use the `with_structured_output` method from
LangChain, which you can read more about here.

We are going to use a single tool in this example for finding the weather, and
will return a structured weather response to the user.

    
    
    from pydantic import BaseModel, Field
    from typing import Literal
    from langchain_core.tools import tool
    from langchain_anthropic import ChatAnthropic
    from langgraph.graph import MessagesState
    
    
    class WeatherResponse(BaseModel):
        """Respond to the user with this"""
    
        temperature: float = Field(description="The temperature in fahrenheit")
        wind_directon: str = Field(
            description="The direction of the wind in abbreviated form"
        )
        wind_speed: float = Field(description="The speed of the wind in km/h")
    
    
    # Inherit 'messages' key from MessagesState, which is a list of chat messages
    class AgentState(MessagesState):
        # Final structured response from the agent
        final_response: WeatherResponse
    
    
    @tool
    def get_weather(city: Literal["nyc", "sf"]):
        """Use this to get weather information."""
        if city == "nyc":
            return "It is cloudy in NYC, with 5 mph winds in the North-East direction and a temperature of 70 degrees"
        elif city == "sf":
            return "It is 75 degrees and sunny in SF, with 3 mph winds in the South-East direction"
        else:
            raise AssertionError("Unknown city")
    
    
    tools = [get_weather]
    
    model = ChatAnthropic(model="claude-3-opus-20240229")
    
    model_with_tools = model.bind_tools(tools)
    model_with_structured_output = model.with_structured_output(WeatherResponse)
    

API Reference: tool | ChatAnthropic

## Option 1: Bind output as tool¶

Let's now examine how we would use the single LLM option.

### Define Graph¶

The graph definition is very similar to the one above, the only difference is
we no longer call an LLM in the `response` node, and instead bind the
`WeatherResponse` tool to our LLM that already contains the `get_weather`
tool.

    
    
    from langgraph.graph import StateGraph, END
    from langgraph.prebuilt import ToolNode
    
    tools = [get_weather, WeatherResponse]
    
    # Force the model to use tools by passing tool_choice="any"
    model_with_response_tool = model.bind_tools(tools, tool_choice="any")
    
    
    # Define the function that calls the model
    def call_model(state: AgentState):
        response = model_with_response_tool.invoke(state["messages"])
        # We return a list, because this will get added to the existing list
        return {"messages": [response]}
    
    
    # Define the function that responds to the user
    def respond(state: AgentState):
        # Construct the final answer from the arguments of the last tool call
        weather_tool_call = state["messages"][-1].tool_calls[0]
        response = WeatherResponse(**weather_tool_call["args"])
        # Since we're using tool calling to return structured output,
        # we need to add  a tool message corresponding to the WeatherResponse tool call,
        # This is due to LLM providers' requirement that AI messages with tool calls
        # need to be followed by a tool message for each tool call
        tool_message = {
            "type": "tool",
            "content": "Here is your structured response",
            "tool_call_id": weather_tool_call["id"],
        }
        # We return the final answer
        return {"final_response": response, "messages": [tool_message]}
    
    
    # Define the function that determines whether to continue or not
    def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        # If there is only one tool call and it is the response tool call we respond to the user
        if (
            len(last_message.tool_calls) == 1
            and last_message.tool_calls[0]["name"] == "WeatherResponse"
        ):
            return "respond"
        # Otherwise we will use the tool node again
        else:
            return "continue"
    
    
    # Define a new graph
    workflow = StateGraph(AgentState)
    
    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("respond", respond)
    workflow.add_node("tools", ToolNode(tools))
    
    # Set the entrypoint as `agent`
    # This means that this node is the first one called
    workflow.set_entry_point("agent")
    
    # We now add a conditional edge
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "tools",
            "respond": "respond",
        },
    )
    
    workflow.add_edge("tools", "agent")
    workflow.add_edge("respond", END)
    graph = workflow.compile()
    

API Reference: StateGraph | END | ToolNode

### Usage¶

Now we can run our graph to check that it worked as intended:

    
    
    answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
        "final_response"
    ]
    
    
    
    answer
    
    
    
    WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=3.0)
    

Again, the agent returned a `WeatherResponse` object as we expected.

## Option 2: 2 LLMs¶

Let's now dive into how we would use a second LLM to force structured output.

### Define Graph¶

We can now define our graph:

    
    
    from langgraph.graph import StateGraph, END
    from langgraph.prebuilt import ToolNode
    from langchain_core.messages import HumanMessage
    
    
    # Define the function that calls the model
    def call_model(state: AgentState):
        response = model_with_tools.invoke(state["messages"])
        # We return a list, because this will get added to the existing list
        return {"messages": [response]}
    
    
    # Define the function that responds to the user
    def respond(state: AgentState):
        # We call the model with structured output in order to return the same format to the user every time
        # state['messages'][-2] is the last ToolMessage in the convo, which we convert to a HumanMessage for the model to use
        # We could also pass the entire chat history, but this saves tokens since all we care to structure is the output of the tool
        response = model_with_structured_output.invoke(
            [HumanMessage(content=state["messages"][-2].content)]
        )
        # We return the final answer
        return {"final_response": response}
    
    
    # Define the function that determines whether to continue or not
    def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        # If there is no function call, then we respond to the user
        if not last_message.tool_calls:
            return "respond"
        # Otherwise if there is, we continue
        else:
            return "continue"
    
    
    # Define a new graph
    workflow = StateGraph(AgentState)
    
    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("respond", respond)
    workflow.add_node("tools", ToolNode(tools))
    
    # Set the entrypoint as `agent`
    # This means that this node is the first one called
    workflow.set_entry_point("agent")
    
    # We now add a conditional edge
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "tools",
            "respond": "respond",
        },
    )
    
    workflow.add_edge("tools", "agent")
    workflow.add_edge("respond", END)
    graph = workflow.compile()
    

API Reference: HumanMessage | StateGraph | END | ToolNode

### Usage¶

We can now invoke our graph to verify that the output is being structured as
desired:

    
    
    answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
        "final_response"
    ]
    
    
    
    answer
    
    
    
    WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=4.83)
    

As we can see, the agent returned a `WeatherResponse` object as we expected.
If would now be easy to use this agent in a more complex software stack
without having to worry about the output of the agent not matching the format
expected from the next step in the stack.

## Comments

Back to top

Previous

How to add node retry policies

Next

How to pass custom run ID or set tags and metadata for graph runs in LangSmith

Made with  Material for MkDocs Insiders