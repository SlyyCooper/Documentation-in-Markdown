## Table of Contents

- [How to add and use subgraphs¶](#how-to-add-and-use-subgraphs)
  - [Setup¶](#setup)
  - [Add a node with the compiled subgraph¶](#add-a-node-with-the-compiled-subgraph)
  - [Add a node function that invokes the subgraph¶](#add-a-node-function-that-invokes-the-subgraph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add and use subgraphs

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
      * Subgraphs  Subgraphs 
        * Subgraphs 
        * How to add and use subgraphs  How to add and use subgraphs  Table of contents 
          * Setup 
          * Add a node with the compiled subgraph 
          * Add a node function that invokes the subgraph 
        * How to view and update state in subgraphs 
        * How to transform inputs and outputs of a subgraph 
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
  * Add a node with the compiled subgraph 
  * Add a node function that invokes the subgraph 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Subgraphs 

# How to add and use subgraphs¶

Prerequisites

This guide assumes familiarity with the following:

  * Subgraphs 
  * State 

Subgraphs allow you to build complex systems with multiple components that are
themselves graphs. A common use case for using subgraphs is building multi-
agent systems.

The main question when adding subgraphs is how the parent graph and subgraph
communicate, i.e. how they pass the state between each other during the graph
execution. There are two scenarios:

  * parent graph and subgraph **share schema keys**. In this case, you can add a node with the compiled subgraph
  * parent graph and subgraph have **different schemas**. In this case, you have to add a node function that invokes the subgraph: this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph

Below we show to to add subgraphs for each scenario.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Add a node with the compiled subgraph¶

A common case is for the parent graph and subgraph to communicate over a
shared state key (channel). For example, in multi-agent systems, the agents
often communicate over a shared messages key.

If your subgraph shares state keys with the parent graph, you can follow these
steps to add it to your graph:

  1. Define the subgraph workflow (`subgraph_builder` in the example below) and compile it
  2. Pass compiled subgraph to the `.add_node` method when defining the parent graph workflow

Let's take a look at a simple example.

    
    
    from langgraph.graph import START, StateGraph
    from typing import TypedDict
    
    
    # Define subgraph
    class SubgraphState(TypedDict):
        foo: str  # note that this key is shared with the parent graph state
        bar: str
    
    
    def subgraph_node_1(state: SubgraphState):
        return {"bar": "bar"}
    
    
    def subgraph_node_2(state: SubgraphState):
        # note that this node is using a state key ('bar') that is only available in the subgraph
        # and is sending update on the shared state key ('foo')
        return {"foo": state["foo"] + state["bar"]}
    
    
    subgraph_builder = StateGraph(SubgraphState)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_node(subgraph_node_2)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
    subgraph = subgraph_builder.compile()
    
    
    # Define parent graph
    class ParentState(TypedDict):
        foo: str
    
    
    def node_1(state: ParentState):
        return {"foo": "hi! " + state["foo"]}
    
    
    builder = StateGraph(ParentState)
    builder.add_node("node_1", node_1)
    # note that we're adding the compiled subgraph as a node to the parent graph
    builder.add_node("node_2", subgraph)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    graph = builder.compile()
    

API Reference: START | StateGraph
    
    
    for chunk in graph.stream({"foo": "foo"}):
        print(chunk)
    
    
    
    {'node_1': {'foo': 'hi! foo'}}
    {'node_2': {'foo': 'hi! foobar'}}
    

You can see that the final output from the parent graph includes the results
of subgraph invocation (i.e. string `"bar"`). If you would like to see outputs
from the subgraph, you can specify `subgraphs=True` when streaming. See more
on streaming from subgraphs in this how-to guide.

    
    
    for chunk in graph.stream({"foo": "foo"}, subgraphs=True):
        print(chunk)
    
    
    
    ((), {'node_1': {'foo': 'hi! foo'}})
    (('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_1': {'bar': 'bar'}})
    (('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_2': {'foo': 'hi! foobar'}})
    ((), {'node_2': {'foo': 'hi! foobar'}})
    

## Add a node function that invokes the subgraph¶

For more complex systems you might want to define subgraphs that have a
completely different schema from the parent graph (no shared keys). For
example, in a multi-agent RAG system, a search agent might only need to keep
track of queries and retrieved documents.

If that's the case for your application, you need to define a node **function
that invokes the subgraph**. This function needs to transform the input
(parent) state to the subgraph state before invoking the subgraph, and
transform the results back to the parent state before returning the state
update from the node.

Below we show how to modify our original example to call a subgraph from
inside the node.

Warning

You **cannot** invoke more than one subgraph inside the same node.

    
    
    # Define subgraph
    class SubgraphState(TypedDict):
        # note that none of these keys are shared with the parent graph state
        bar: str
        baz: str
    
    
    def subgraph_node_1(state: SubgraphState):
        return {"baz": "baz"}
    
    
    def subgraph_node_2(state: SubgraphState):
        return {"bar": state["bar"] + state["baz"]}
    
    
    subgraph_builder = StateGraph(SubgraphState)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_node(subgraph_node_2)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
    subgraph = subgraph_builder.compile()
    
    
    # Define parent graph
    class ParentState(TypedDict):
        foo: str
    
    
    def node_1(state: ParentState):
        return {"foo": "hi! " + state["foo"]}
    
    
    def node_2(state: ParentState):
        # transform the state to the subgraph state
        response = subgraph.invoke({"bar": state["foo"]})
        # transform response back to the parent state
        return {"foo": response["bar"]}
    
    
    builder = StateGraph(ParentState)
    builder.add_node("node_1", node_1)
    # note that instead of using the compiled subgraph we are using `node_2` function that is calling the subgraph
    builder.add_node("node_2", node_2)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    graph = builder.compile()
    
    
    
    for chunk in graph.stream({"foo": "foo"}, subgraphs=True):
        print(chunk)
    
    
    
    ((), {'node_1': {'foo': 'hi! foo'}})
    (('node_2:c47d7ea3-7798-87c4-adf4-2543a91d6891',), {'subgraph_node_1': {'baz': 'baz'}})
    (('node_2:c47d7ea3-7798-87c4-adf4-2543a91d6891',), {'subgraph_node_2': {'bar': 'hi! foobaz'}})
    ((), {'node_2': {'foo': 'hi! foobaz'}})
    

## Comments

Back to top

Previous

How to handle large numbers of tools

Next

How to view and update state in subgraphs

Made with  Material for MkDocs Insiders