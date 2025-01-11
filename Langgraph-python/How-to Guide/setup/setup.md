## Table of Contents

- [How to Set Up a LangGraph Application for Deployment¶](#how-to-set-up-a-langgraph-application-for-deployment)
  - [Specify Dependencies¶](#specify-dependencies)
  - [Specify Environment Variables¶](#specify-environment-variables)
  - [Define Graphs¶](#define-graphs)
  - [Create LangGraph API Config¶](#create-langgraph-api-config)
  - [Next¶](#next)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to Set Up a LangGraph Application for Deployment

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
        * How to Set Up a LangGraph Application for Deployment  How to Set Up a LangGraph Application for Deployment  Table of contents 
          * Specify Dependencies 
          * Specify Environment Variables 
          * Define Graphs 
          * Create LangGraph API Config 
          * Next 
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

Table of contents

  * Specify Dependencies 
  * Specify Environment Variables 
  * Define Graphs 
  * Create LangGraph API Config 
  * Next 

  1. Home 
  2. How-to Guides 
  3. LangGraph Platform 
  4. Application Structure 

# How to Set Up a LangGraph Application for Deployment¶

A LangGraph application must be configured with a LangGraph API configuration
file in order to be deployed to LangGraph Cloud (or to be self-hosted). This
how-to guide discusses the basic steps to setup a LangGraph application for
deployment using `requirements.txt` to specify project dependencies.

This walkthrough is based on this repository, which you can play around with
to learn more about how to setup your LangGraph application for deployment.

Setup with pyproject.toml

If you prefer using poetry for dependency management, check out this how-to
guide on using `pyproject.toml` for LangGraph Cloud.

Setup with a Monorepo

If you are interested in deploying a graph located inside a monorepo, take a
look at this repository for an example of how to do so.

The final repo structure will look something like this:

    
    
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for you graph
    │   │   └── state.py # state definition of your graph
    │   ├── requirements.txt # package dependencies
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    └── langgraph.json # configuration file for LangGraph
    

After each step, an example file directory is provided to demonstrate how code
can be organized.

## Specify Dependencies¶

Dependencies can optionally be specified in one of the following files:
`pyproject.toml`, `setup.py`, or `requirements.txt`. If none of these files is
created, then dependencies can be specified later in the LangGraph API
configuration file.

The dependencies below will be included in the image, you can also use them in
your code, as long as with a compatible version range:

    
    
    langgraph>=0.2.56,<0.3.0
    langgraph-checkpoint>=2.0.5,<3.0
    langchain-core>=0.2.38,<0.4.0
    langsmith>=0.1.63
    orjson>=3.9.7
    httpx>=0.25.0
    tenacity>=8.0.0
    uvicorn>=0.26.0
    sse-starlette>=2.1.0
    uvloop>=0.18.0
    httptools>=0.5.0
    jsonschema-rs>=0.16.3
    croniter>=1.0.1
    structlog>=23.1.0
    redis>=5.0.0,<6.0.0
    

Example `requirements.txt` file:

    
    
    langgraph
    langchain_anthropic
    tavily-python
    langchain_community
    langchain_openai
    

Example file directory:

    
    
    my-app/
    ├── my_agent # all project code lies within here
    │   └── requirements.txt # package dependencies
    

## Specify Environment Variables¶

Environment variables can optionally be specified in a file (e.g. `.env`). See
the Environment Variables reference to configure additional variables for a
deployment.

Example `.env` file:

    
    
    MY_ENV_VAR_1=foo
    MY_ENV_VAR_2=bar
    OPENAI_API_KEY=key
    

Example file directory:

    
    
    my-app/
    ├── my_agent # all project code lies within here
    │   └── requirements.txt # package dependencies
    └── .env # environment variables
    

## Define Graphs¶

Implement your graphs! Graphs can be defined in a single file or multiple
files. Make note of the variable names of each CompiledGraph to be included in
the LangGraph application. The variable names will be used later when creating
the LangGraph API configuration file.

Example `agent.py` file, which shows how to import from other modules you
define (code for the modules is not shown here, please see this repo to see
their implementation):

    
    
    # my_agent/agent.py
    from typing import Literal
    from typing_extensions import TypedDict
    
    from langgraph.graph import StateGraph, END, START
    from my_agent.utils.nodes import call_model, should_continue, tool_node # import nodes
    from my_agent.utils.state import AgentState # import state
    
    # Define the config
    class GraphConfig(TypedDict):
        model_name: Literal["anthropic", "openai"]
    
    workflow = StateGraph(AgentState, config_schema=GraphConfig)
    workflow.add_node("agent", call_model)
    workflow.add_node("action", tool_node)
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "continue": "action",
            "end": END,
        },
    )
    workflow.add_edge("action", "agent")
    
    graph = workflow.compile()
    

API Reference: StateGraph | END | START

Assign `CompiledGraph` to Variable

The build process for LangGraph Cloud requires that the `CompiledGraph` object
be assigned to a variable at the top-level of a Python module (alternatively,
you can provide a function that creates a graph).

Example file directory:

    
    
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for you graph
    │   │   └── state.py # state definition of your graph
    │   ├── requirements.txt # package dependencies
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    └── .env # environment variables
    

## Create LangGraph API Config¶

Create a LangGraph API configuration file called `langgraph.json`. See the
LangGraph CLI reference for detailed explanations of each key in the JSON
object of the configuration file.

Example `langgraph.json` file:

    
    
    {
      "dependencies": ["./my_agent"],
      "graphs": {
        "agent": "./my_agent/agent.py:graph"
      },
      "env": ".env"
    }
    

Note that the variable name of the `CompiledGraph` appears at the end of the
value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

Configuration Location

The LangGraph API configuration file must be placed in a directory that is at
the same level or higher than the Python files that contain compiled graphs
and associated dependencies.

Example file directory:

    
    
    my-app/
    ├── my_agent # all project code lies within here
    │   ├── utils # utilities for your graph
    │   │   ├── __init__.py
    │   │   ├── tools.py # tools for your graph
    │   │   ├── nodes.py # node functions for you graph
    │   │   └── state.py # state definition of your graph
    │   ├── requirements.txt # package dependencies
    │   ├── __init__.py
    │   └── agent.py # code for constructing your graph
    ├── .env # environment variables
    └── langgraph.json # configuration file for LangGraph
    

## Next¶

After you setup your project and place it in a github repo, it's time to
deploy your app.

## Comments

Back to top

Previous

How to create a ReAct agent from scratch

Next

How to Set Up a LangGraph Application for Deployment

Made with  Material for MkDocs Insiders