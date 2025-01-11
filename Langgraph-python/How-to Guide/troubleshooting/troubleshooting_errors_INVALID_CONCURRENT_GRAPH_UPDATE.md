## Table of Contents

- [INVALID_CONCURRENT_GRAPH_UPDATE¶](#invalid_concurrent_graph_update)
  - [Troubleshooting¶](#troubleshooting)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

INVALID_CONCURRENT_GRAPH_UPDATE

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
      * INVALID_CONCURRENT_GRAPH_UPDATE  INVALID_CONCURRENT_GRAPH_UPDATE  Table of contents 
        * Troubleshooting 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Troubleshooting 

  1. Home 
  2. How-to Guides 
  3. Troubleshooting 

# INVALID_CONCURRENT_GRAPH_UPDATE¶

A LangGraph `StateGraph` received concurrent updates to its state from
multiple nodes to a state property that doesn't support it.

One way this can occur is if you are using a fanout or other parallel
execution in your graph and you have defined a graph like this:

    
    
    class State(TypedDict):
        some_key: str
    
    def node(state: State):
        return {"some_key": "some_string_value"}
    
    def other_node(state: State):
        return {"some_key": "some_string_value"}
    
    
    builder = StateGraph(State)
    builder.add_node(node)
    builder.add_node(other_node)
    builder.add_edge(START, "node")
    builder.add_edge(START, "other_node")
    graph = builder.compile()
    

If a node in the above graph returns `{ "some_key": "some_string_value" }`,
this will overwrite the state value for `"some_key"` with
`"some_string_value"`. However, if multiple nodes in e.g. a fanout within a
single step return values for `"some_key"`, the graph will throw this error
because there is uncertainty around how to update the internal state.

To get around this, you can define a reducer that combines multiple values:

    
    
    import operator
    from typing import Annotated
    
    class State(TypedDict):
        # The operator.add reducer fn makes this append-only
        some_key: Annotated[list, operator.add]
    

This will allow you to define logic that handles the same key returned from
multiple nodes executed in parallel.

## Troubleshooting¶

The following may help resolve this error:

  * If your graph executes nodes in parallel, make sure you have defined relevant state keys with a reducer.

## Comments

Back to top

Previous

GRAPH_RECURSION_LIMIT

Next

INVALID_GRAPH_NODE_RETURN_VALUE

Made with  Material for MkDocs Insiders