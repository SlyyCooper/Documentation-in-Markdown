## Table of Contents

- [How to pass private state between nodes¶](#how-to-pass-private-state-between-nodes)
  - [Setup¶](#setup)
  - [Define and use the graph¶](#define-and-use-the-graph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to pass private state between nodes

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
      * State Management  State Management 
        * State Management 
        * How to use Pydantic model as state 
        * How to define input/output schema for your graph 
        * How to pass private state between nodes  How to pass private state between nodes  Table of contents 
          * Setup 
          * Define and use the graph 
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
  * Define and use the graph 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. State Management 

# How to pass private state between nodes¶

Prerequisites

This guide assumes familiarity with the following:

  * Multiple Schemas 

In some cases, you may want nodes to exchange information that is crucial for
intermediate logic but doesn’t need to be part of the main schema of the
graph. This private data is not relevant to the overall input/output of the
graph and should only be shared between certain nodes.

In this how-to guide, we'll create an example sequential graph consisting of
three nodes (node_1, node_2 and node_3), where private data is passed between
the first two steps (node_1 and node_2), while the third step (node_3) only
has access to the public overall state.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define and use the graph¶

    
    
    from langgraph.graph import StateGraph, START, END
    from typing_extensions import TypedDict
    
    
    # The overall state of the graph (this is the public state shared across nodes)
    class OverallState(TypedDict):
        a: str
    
    
    # Output from node_1 contains private data that is not part of the overall state
    class Node1Output(TypedDict):
        private_data: str
    
    
    # The private data is only shared between node_1 and node_2
    def node_1(state: OverallState) -> Node1Output:
        output = {"private_data": "set by node_1"}
        print(f"Entered node `node_1`:\n\tInput: {state}.\n\tReturned: {output}")
        return output
    
    
    # Node 2 input only requests the private data available after node_1
    class Node2Input(TypedDict):
        private_data: str
    
    
    def node_2(state: Node2Input) -> OverallState:
        output = {"a": "set by node_2"}
        print(f"Entered node `node_2`:\n\tInput: {state}.\n\tReturned: {output}")
        return output
    
    
    # Node 3 only has access to the overall state (no access to private data from node_1)
    def node_3(state: OverallState) -> OverallState:
        output = {"a": "set by node_3"}
        print(f"Entered node `node_3`:\n\tInput: {state}.\n\tReturned: {output}")
        return output
    
    
    # Build the state graph
    builder = StateGraph(OverallState)
    builder.add_node(node_1)  # node_1 is the first node
    builder.add_node(
        node_2
    )  # node_2 is the second node and accepts private data from node_1
    builder.add_node(node_3)  # node_3 is the third node and does not see the private data
    builder.add_edge(START, "node_1")  # Start the graph with node_1
    builder.add_edge("node_1", "node_2")  # Pass from node_1 to node_2
    builder.add_edge(
        "node_2", "node_3"
    )  # Pass from node_2 to node_3 (only overall state is shared)
    builder.add_edge("node_3", END)  # End the graph after node_3
    graph = builder.compile()
    
    # Invoke the graph with the initial state
    response = graph.invoke(
        {
            "a": "set at start",
        }
    )
    
    print()
    print(f"Output of graph invocation: {response}")
    

API Reference: StateGraph | START | END
    
    
    Entered node `node_1`:
        Input: {'a': 'set at start'}.
        Returned: {'private_data': 'set by node_1'}
    Entered node `node_2`:
        Input: {'private_data': 'set by node_1'}.
        Returned: {'a': 'set by node_2'}
    Entered node `node_3`:
        Input: {'a': 'set by node_2'}.
        Returned: {'a': 'set by node_3'}
    
    Output of graph invocation: {'a': 'set by node_3'}
    

## Comments

Back to top

Previous

How to define input/output schema for your graph

Next

How to run a graph asynchronously

Made with  Material for MkDocs Insiders