## Table of Contents

- [How to control graph recursion limit¶](#how-to-control-graph-recursion-limit)
  - [Setup¶](#setup)
  - [Define the graph¶](#define-the-graph)
  - [Use the graph¶](#use-the-graph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to control graph recursion limit

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
      * Controllability  Controllability 
        * Controllability 
        * How to create branches for parallel node execution 
        * How to create map-reduce branches for parallel execution 
        * How to control graph recursion limit  How to control graph recursion limit  Table of contents 
          * Setup 
          * Define the graph 
          * Use the graph 
        * How to combine control flow and state updates with Command 
      * Persistence 
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
  * Define the graph 
  * Use the graph 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Controllability 

# How to control graph recursion limit¶

Prerequisites

This guide assumes familiarity with the following:

  * Graphs 
  * Recursion Limit 
  * Nodes 

You can set the graph recursion limit when invoking or streaming the graph.
The recursion limit sets the number of **supersteps** that the graph is
allowed to execute before it raises an error. Read more about the concept of
recursion limits here. Let's see an example of this in a simple graph with
parallel branches to better understand exactly how the recursion limit works.

If you want to see an example of how you can return the last value of your
state instead of receiving a recursion limit error form your graph, read this
how-to.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define the graph¶

    
    
    import operator
    from typing import Annotated, Any
    
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph, START, END
    
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        aggregate: Annotated[list, operator.add]
    
    
    def node_a(state):
        return {"aggregate": ["I'm A"]}
    
    
    def node_b(state):
        return {"aggregate": ["I'm B"]}
    
    
    def node_c(state):
        return {"aggregate": ["I'm C"]}
    
    
    def node_d(state):
        return {"aggregate": ["I'm A"]}
    
    
    builder = StateGraph(State)
    builder.add_node("a", node_a)
    builder.add_edge(START, "a")
    builder.add_node("b", node_b)
    builder.add_node("c", node_c)
    builder.add_node("d", node_d)
    builder.add_edge("a", "b")
    builder.add_edge("a", "c")
    builder.add_edge("b", "d")
    builder.add_edge("c", "d")
    builder.add_edge("d", END)
    graph = builder.compile()
    

API Reference: StateGraph | START | END
    
    
    from IPython.display import Image, display
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    

As we can see, our graph will execute nodes `b` and `c` in parallel (i.e. in a
single super-step), which means that if we run this graph it should take
exactly 3 steps. We can set the recursion limit to 3 first to check that it
raises an error (the recursion limit is inclusive, so if the limit is 3 the
graph will raise an error when it reaches step 3) as expected:

## Use the graph¶

    
    
    from langgraph.errors import GraphRecursionError
    
    try:
        graph.invoke({"aggregate": []}, {"recursion_limit": 3})
    except GraphRecursionError:
        print("Recursion Error")
    
    
    
    Recursion Error
    

Success! The graph raised an error as expected - now let's test setting the
recursion limit to 4 and ensure that the graph succeeds in this case:

    
    
    try:
        graph.invoke({"aggregate": []}, {"recursion_limit": 4})
    except GraphRecursionError:
        print("Recursion Error")
    

Perfect, just as we expected the graph runs successfully in this case.

Setting the correct graph recursion limit is important for avoiding graph runs
stuck in long-running loops and thus helps minimize unnecessary costs

## Comments

Back to top

Previous

How to create map-reduce branches for parallel execution

Next

How to combine control flow and state updates with Command

Made with  Material for MkDocs Insiders