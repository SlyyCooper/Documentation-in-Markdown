## Table of Contents

- [MULTIPLE_SUBGRAPHS¶](#multiple_subgraphs)
  - [Troubleshooting¶](#troubleshooting)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

MULTIPLE_SUBGRAPHS

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
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS  MULTIPLE_SUBGRAPHS  Table of contents 
        * Troubleshooting 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Troubleshooting 

  1. Home 
  2. How-to Guides 
  3. Troubleshooting 

# MULTIPLE_SUBGRAPHS¶

You are calling the same subgraph multiple times within a single LangGraph
node with checkpointing enabled for each subgraph.

This is currently not allowed due to internal restrictions on how checkpoint
namespacing for subgraphs works.

## Troubleshooting¶

The following may help resolve this error:

  * If you don't need to interrupt/resume from a subgraph, pass `checkpointer=False` when compiling it like this: `.compile(checkpointer=False)`
  * Don't imperatively call graphs multiple times in the same node, and instead use the `Send` API.

## Comments

Back to top

Previous

INVALID_GRAPH_NODE_RETURN_VALUE

Next

Concepts

Made with  Material for MkDocs Insiders