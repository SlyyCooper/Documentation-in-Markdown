## Table of Contents

- [Adding nodes as dataset examples in Studio¶](#adding-nodes-as-dataset-examples-in-studio)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

Adding nodes as dataset examples in Studio

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
      * LangGraph Studio  LangGraph Studio 
        * LangGraph Studio 
        * Test Cloud Deployment 
        * LangGraph Studio With Local Deployment 
        * Invoke Assistant 
        * Interacting with Threads in Studio 
        * Adding nodes as dataset examples in Studio 
    * Troubleshooting 

Troubleshooting

      * Troubleshooting 
      * GRAPH_RECURSION_LIMIT 
      * INVALID_CONCURRENT_GRAPH_UPDATE 
      * INVALID_GRAPH_NODE_RETURN_VALUE 
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. LangGraph Studio 

# Adding nodes as dataset examples in Studio¶

In LangGraph Studio you can create dataset examples from the thread history in
the right-hand pane. This can be especially useful when you want to evaluate
intermediate steps of the agent.

  1. Click on the `Add to Dataset` button to enter the dataset mode.
  2. Select nodes which you want to add to dataset.
  3. Select the target dataset to create the example in.

You can edit the example payload before sending it to the dataset, which is
useful if you need to make changes to conform the example to the dataset
schema.

Finally, you can customise the target dataset by clicking on the `Settings`
button.

See Evaluating intermediate steps for more details on how to evaluate
intermediate steps.

## Comments

Back to top

Previous

Interacting with Threads in Studio

Next

Error reference

Made with  Material for MkDocs Insiders