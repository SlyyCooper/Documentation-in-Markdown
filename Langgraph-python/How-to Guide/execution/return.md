## Table of Contents

- [How to return state before hitting recursion limit¶](#how-to-return-state-before-hitting-recursion-limit)
  - [Setup¶](#setup)
  - [Without returning state¶](#without-returning-state)
  - [With returning state¶](#with-returning-state)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to return state before hitting recursion limit

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
        * How to return structured output with a ReAct style agent 
        * How to pass custom run ID or set tags and metadata for graph runs in LangSmith 
        * How to return state before hitting recursion limit  How to return state before hitting recursion limit  Table of contents 
          * Setup 
          * Without returning state 
          * With returning state 
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
  * Without returning state 
  * With returning state 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Other 

# How to return state before hitting recursion limit¶

Prerequisites

This guide assumes familiarity with the following:

  * Graphs 
  * Recursion Limit 
  * Nodes 

Setting the graph recursion limit can help you control how long your graph
will stay running, but if the recursion limit is hit your graph returns an
error - which may not be ideal for all use cases. Instead you may wish to
return the value of the state _just before_ the recursion limit is hit. This
how-to will show you how to do this.

## Setup¶

First, let's installed the required packages:

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Without returning state¶

We are going to define a dummy graph in this example that will always hit the
recursion limit. First, we will implement it without returning the state and
show that it hits the recursion limit. This graph is based on the ReAct
architecture, but instead of actually making decisions and taking actions it
just loops forever.

    
    
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph
    from langgraph.graph import START, END
    
    
    class State(TypedDict):
        value: str
        action_result: str
    
    
    def router(state: State):
        if state["value"] == "end":
            return END
        else:
            return "action"
    
    
    def decision_node(state):
        return {"value": "keep going!"}
    
    
    def action_node(state: State):
        # Do your action here ...
        return {"action_result": "what a great result!"}
    
    
    workflow = StateGraph(State)
    workflow.add_node("decision", decision_node)
    workflow.add_node("action", action_node)
    workflow.add_edge(START, "decision")
    workflow.add_conditional_edges("decision", router, ["action", END])
    workflow.add_edge("action", "decision")
    app = workflow.compile()
    

API Reference: StateGraph | START | END
    
    
    from IPython.display import Image, display
    
    display(Image(app.get_graph().draw_mermaid_png()))
    

Let's verify that our graph will always hit the recursion limit:

    
    
    from langgraph.errors import GraphRecursionError
    
    try:
        app.invoke({"value": "hi!"})
    except GraphRecursionError:
        print("Recursion Error")
    
    
    
    Recursion Error
    

## With returning state¶

To avoid hitting the recursion limit, we can introduce a new key to our state
called `remaining_steps`. It will keep track of number of steps until reaching
the recursion limit. We can then check the value of `remaining_steps` to
determine whether we should terminate the graph execution and return the state
to the user without causing the `RecursionError`.

To do so, we will use a special `RemainingSteps` annotation. Under the hood,
it creates a special `ManagedValue` channel -- a state channel that will exist
for the duration of our graph run and no longer.

Since our `action` node is going to always induce at least 2 extra steps to
our graph (since the `action` node ALWAYS calls the `decision` node
afterwards), we will use this channel to check if we are within 2 steps of the
limit.

Now, when we run our graph we should receive no errors and instead get the
last value of the state before the recursion limit was hit.

    
    
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph
    from typing import Annotated
    
    from langgraph.managed.is_last_step import RemainingSteps
    
    
    class State(TypedDict):
        value: str
        action_result: str
        remaining_steps: RemainingSteps
    
    
    def router(state: State):
        # Force the agent to end
        if state["remaining_steps"] <= 2:
            return END
        if state["value"] == "end":
            return END
        else:
            return "action"
    
    
    def decision_node(state):
        return {"value": "keep going!"}
    
    
    def action_node(state: State):
        # Do your action here ...
        return {"action_result": "what a great result!"}
    
    
    workflow = StateGraph(State)
    workflow.add_node("decision", decision_node)
    workflow.add_node("action", action_node)
    workflow.add_edge(START, "decision")
    workflow.add_conditional_edges("decision", router, ["action", END])
    workflow.add_edge("action", "decision")
    app = workflow.compile()
    

API Reference: StateGraph

    
    
    app.invoke({"value": "hi!"})
    
    
    
    {'value': 'keep going!', 'action_result': 'what a great result!'}
    

Perfect! Our code ran with no error, just as we expected!

## Comments

Back to top

Previous

How to pass custom run ID or set tags and metadata for graph runs in LangSmith

Next

How to use the prebuilt ReAct agent

Made with  Material for MkDocs Insiders