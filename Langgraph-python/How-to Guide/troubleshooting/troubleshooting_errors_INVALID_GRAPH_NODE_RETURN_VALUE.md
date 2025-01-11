## Table of Contents

- [INVALID_GRAPH_NODE_RETURN_VALUE¶](#invalid_graph_node_return_value)
  - [Troubleshooting¶](#troubleshooting)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

INVALID_GRAPH_NODE_RETURN_VALUE

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
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE  INVALID_GRAPH_NODE_RETURN_VALUE  Table of contents 
        * Troubleshooting 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Troubleshooting 

  1. Home 
  2. How-to Guides 
  3. Troubleshooting 

# INVALID_GRAPH_NODE_RETURN_VALUE¶

A LangGraph `StateGraph` received a non-dict return type from a node. Here's
an example:

    
    
    class State(TypedDict):
        some_key: str
    
    def bad_node(state: State):
        # Should return an dict with a value for "some_key", not a list
        return ["whoops"]
    
    builder = StateGraph(State)
    builder.add_node(bad_node)
    ...
    
    graph = builder.compile()
    

Invoking the above graph will result in an error like this:

    
    
    graph.invoke({ "some_key": "someval" });
    
    
    
    InvalidUpdateError: Expected dict, got ['whoops']
    For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/INVALID_GRAPH_NODE_RETURN_VALUE
    

Nodes in your graph must return an dict containing one or more keys defined in
your state.

## Troubleshooting¶

The following may help resolve this error:

  * If you have complex logic in your node, make sure all code paths return an appropriate dict for your defined state.

## Comments

Back to top

Previous

INVALID_CONCURRENT_GRAPH_UPDATE

Next

MULTIPLE_SUBGRAPHS

Made with  Material for MkDocs Insiders