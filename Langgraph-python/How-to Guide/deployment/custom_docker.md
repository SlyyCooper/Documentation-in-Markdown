## Table of Contents

- [How to customize Dockerfile¶](#how-to-customize-dockerfile)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to customize Dockerfile

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
      * Application Structure  Application Structure 
        * Application Structure 
        * How to Set Up a LangGraph Application for Deployment 
        * How to Set Up a LangGraph Application for Deployment 
        * How to Set Up a LangGraph.js Application for Deployment 
        * How to add semantic search to your LangGraph deployment 
        * How to customize Dockerfile 
        * How to test a LangGraph app locally 
        * Rebuild Graph at Runtime 
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

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Application Structure 

# How to customize Dockerfile¶

Users can add an array of additional lines to add to the Dockerfile following
the import from the parent LangGraph image. In order to do this, you simply
need to modify your `langgraph.json` file by passing in the commands you want
run to the `dockerfile_lines` key. For example, if we wanted to use `Pillow`
in our graph you would need to add the following dependencies:

    
    
    {
        "dependencies": ["."],
        "graphs": {
            "openai_agent": "./openai_agent.py:agent",
        },
        "env": "./.env",
        "dockerfile_lines": [
            "RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libpng-dev",
            "RUN pip install Pillow"
        ]
    }
    

This would install the system packages required to use Pillow if we were
working with `jpeq` or `png` image formats.

## Comments

Back to top

Previous

How to add semantic search to your LangGraph deployment

Next

How to test a LangGraph app locally

Made with  Material for MkDocs Insiders