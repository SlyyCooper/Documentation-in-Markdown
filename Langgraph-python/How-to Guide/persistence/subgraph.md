## Table of Contents

- [How to add thread-level persistence to subgraphs¶](#how-to-add-thread-level-persistence-to-subgraphs)
  - [Setup¶](#setup)
  - [Define the graph with persistence¶](#define-the-graph-with-persistence)
  - [Verify persistence works¶](#verify-persistence-works)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add thread-level persistence to subgraphs

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
      * Persistence  Persistence 
        * Persistence 
        * How to add thread-level persistence to your graph 
        * How to add thread-level persistence to subgraphs  How to add thread-level persistence to subgraphs  Table of contents 
          * Setup 
          * Define the graph with persistence 
          * Verify persistence works 
        * How to add cross-thread persistence to your graph 
        * How to use Postgres checkpointer for persistence 
        * How to use MongoDB checkpointer for persistence 
        * How to create a custom checkpointer using Redis 
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
  * Define the graph with persistence 
  * Verify persistence works 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Persistence 

# How to add thread-level persistence to subgraphs¶

Prerequisites

This guide assumes familiarity with the following:

  * Subgraphs 
  * Persistence 

This guide shows how you can add thread-level persistence to graphs that use
subgraphs.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define the graph with persistence¶

To add persistence to a graph with subgraphs, all you need to do is pass a
checkpointer when **compiling the parent graph**. LangGraph will automatically
propagate the checkpointer to the child subgraphs.

Note

You **shouldn't provide** a checkpointer when compiling a subgraph. Instead,
you must define a **single** checkpointer that you pass to
`parent_graph.compile()`, and LangGraph will automatically propagate the
checkpointer to the child subgraphs. If you pass the checkpointer to the
`subgraph.compile()`, it will simply be ignored. This also applies when you
add a node function that invokes the subgraph.

Let's define a simple graph with a single subgraph node to show how to do
this.

    
    
    from langgraph.graph import START, StateGraph
    from langgraph.checkpoint.memory import MemorySaver
    from typing import TypedDict
    
    
    # subgraph
    
    
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
    
    
    # parent graph
    
    
    class State(TypedDict):
        foo: str
    
    
    def node_1(state: State):
        return {"foo": "hi! " + state["foo"]}
    
    
    builder = StateGraph(State)
    builder.add_node("node_1", node_1)
    # note that we're adding the compiled subgraph as a node to the parent graph
    builder.add_node("node_2", subgraph)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    

API Reference: START | StateGraph | MemorySaver
    
    
    <langgraph.graph.state.StateGraph at 0x106d2fa10>
    

We can now compile the graph with an in-memory checkpointer (`MemorySaver`).

    
    
    checkpointer = MemorySaver()
    # You must only pass checkpointer when compiling the parent graph.
    # LangGraph will automatically propagate the checkpointer to the child subgraphs.
    graph = builder.compile(checkpointer=checkpointer)
    

## Verify persistence works¶

Let's now run the graph and inspect the persisted state for both the parent
graph and the subgraph to verify that persistence works. We should expect to
see the final execution results for both the parent and subgraph in
`state.values`.

    
    
    config = {"configurable": {"thread_id": "1"}}
    
    
    
    for _, chunk in graph.stream({"foo": "foo"}, config, subgraphs=True):
        print(chunk)
    
    
    
    {'node_1': {'foo': 'hi! foo'}}
    {'subgraph_node_1': {'bar': 'bar'}}
    {'subgraph_node_2': {'foo': 'hi! foobar'}}
    {'node_2': {'foo': 'hi! foobar'}}
    

We can now view the parent graph state by calling `graph.get_state()` with the
same config that we used to invoke the graph.

    
    
    graph.get_state(config).values
    
    
    
    {'foo': 'hi! foobar'}
    

To view the subgraph state, we need to do two things:

  1. Find the most recent config value for the subgraph
  2. Use `graph.get_state()` to retrieve that value for the most recent subgraph config.

To find the correct config, we can examine the state history from the parent
graph and find the state snapshot before we return results from `node_2` (the
node with subgraph):

    
    
    state_with_subgraph = [
        s for s in graph.get_state_history(config) if s.next == ("node_2",)
    ][0]
    

The state snapshot will include the list of `tasks` to be executed next. When
using subgraphs, the `tasks` will contain the config that we can use to
retrieve the subgraph state:

    
    
    subgraph_config = state_with_subgraph.tasks[0].state
    subgraph_config
    
    
    
    {'configurable': {'thread_id': '1',
      'checkpoint_ns': 'node_2:6ef111a6-f290-7376-0dfc-a4152307bc5b'}}
    
    
    
    graph.get_state(subgraph_config).values
    
    
    
    {'foo': 'hi! foobar', 'bar': 'bar'}
    

If you want to learn more about how to modify the subgraph state for human-in-
the-loop workflows, check out this how-to guide.

## Comments

Back to top

Previous

How to add thread-level persistence to your graph

Next

How to add cross-thread persistence to your graph

Made with  Material for MkDocs Insiders