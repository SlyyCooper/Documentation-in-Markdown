## Table of Contents

- [GRAPH_RECURSION_LIMIT¶](#graph_recursion_limit)
  - [Troubleshooting¶](#troubleshooting)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

GRAPH_RECURSION_LIMIT

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
      * GRAPH_RECURSION_LIMIT  GRAPH_RECURSION_LIMIT  Table of contents 
        * Troubleshooting 
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Troubleshooting 

  1. Home 
  2. How-to Guides 
  3. Troubleshooting 

# GRAPH_RECURSION_LIMIT¶

Your LangGraph `StateGraph` reached the maximum number of steps before hitting
a stop condition. This is often due to an infinite loop caused by code like
the example below:

    
    
    class State(TypedDict):
        some_key: str
    
    builder = StateGraph(State)
    builder.add_node("a", ...)
    builder.add_node("b", ...)
    builder.add_edge("a", "b")
    builder.add_edge("b", "a")
    ...
    
    graph = builder.compile()
    

However, complex graphs may hit the default limit naturally.

## Troubleshooting¶

  * If you are not expecting your graph to go through many iterations, you likely have a cycle. Check your logic for infinite loops.
  * If you have a complex graph, you can pass in a higher `recursion_limit` value into your `config` object when invoking your graph like this:

    
    
    graph.invoke({...}, {"recursion_limit": 100})
    

## Comments

Back to top

Previous

Error reference

Next

INVALID_CONCURRENT_GRAPH_UPDATE

Made with  Material for MkDocs Insiders