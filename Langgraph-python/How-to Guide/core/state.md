## Table of Contents

- [How to use Pydantic model as state¶](#how-to-use-pydantic-model-as-state)
  - [Setup¶](#setup)
  - [Input Validation¶](#input-validation)
  - [Multiple Nodes¶](#multiple-nodes)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to use Pydantic model as state

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
        * How to use Pydantic model as state  How to use Pydantic model as state  Table of contents 
          * Setup 
          * Input Validation 
          * Multiple Nodes 
        * How to define input/output schema for your graph 
        * How to pass private state between nodes 
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
  * Input Validation 
  * Multiple Nodes 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. State Management 

# How to use Pydantic model as state¶

Prerequisites

This guide assumes familiarity with the following:

  * State 
  * Nodes 
  * Pydantic : this is a popular Python library for run time validation. 

A StateGraph accepts a `state_schema` argument on initialization that
specifies the "shape" of the state that the nodes in the graph can access and
update.

In our examples, we typically use a python-native `TypedDict` for
`state_schema` (or in the case of MessageGraph, a list), but `state_schema`
can be any type.

In this how-to guide, we'll see how a Pydantic BaseModel. can be used for
`state_schema` to add run time validation on **inputs**.

Known Limitations

  * This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 
  * Currently, the `output` of the graph will **NOT** be an instance of a pydantic model. 
  * Run-time validation only occurs on **inputs** into nodes, not on the outputs. 
  * The validation error trace from pydantic does not show which node the error arises in. 

## Setup¶

First we need to install the packages required

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph
    
    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("OPENAI_API_KEY")
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Input Validation¶

    
    
    from langgraph.graph import StateGraph, START, END
    from typing_extensions import TypedDict
    
    from pydantic import BaseModel
    
    
    # The overall state of the graph (this is the public state shared across nodes)
    class OverallState(BaseModel):
        a: str
    
    
    def node(state: OverallState):
        return {"a": "goodbye"}
    
    
    # Build the state graph
    builder = StateGraph(OverallState)
    builder.add_node(node)  # node_1 is the first node
    builder.add_edge(START, "node")  # Start the graph with node_1
    builder.add_edge("node", END)  # End the graph after node_1
    graph = builder.compile()
    
    # Test the graph with a valid input
    graph.invoke({"a": "hello"})
    

API Reference: StateGraph | START | END
    
    
    {'a': 'goodbye'}
    

Invoke the graph with an **invalid** input

    
    
    try:
        graph.invoke({"a": 123})  # Should be a string
    except Exception as e:
        print("An exception was raised because `a` is an integer rather than a string.")
        print(e)
    
    
    
    An exception was raised because `a` is an integer rather than a string.
    1 validation error for OverallState
    a
      Input should be a valid string [type=string_type, input_value=123, input_type=int]
        For further information visit https://errors.pydantic.dev/2.9/v/string_type
    

## Multiple Nodes¶

Run-time validation will also work in a multi-node graph. In the example below
`bad_node` updates `a` to an integer.

Because run-time validation occurs on **inputs** , the validation error will
occur when `ok_node` is called (not when `bad_node` returns an update to the
state which is inconsistent with the schema).

    
    
    from langgraph.graph import StateGraph, START, END
    from typing_extensions import TypedDict
    
    from pydantic import BaseModel
    
    
    # The overall state of the graph (this is the public state shared across nodes)
    class OverallState(BaseModel):
        a: str
    
    
    def bad_node(state: OverallState):
        return {
            "a": 123  # Invalid
        }
    
    
    def ok_node(state: OverallState):
        return {"a": "goodbye"}
    
    
    # Build the state graph
    builder = StateGraph(OverallState)
    builder.add_node(bad_node)
    builder.add_node(ok_node)
    builder.add_edge(START, "bad_node")
    builder.add_edge("bad_node", "ok_node")
    builder.add_edge("ok_node", END)
    graph = builder.compile()
    
    # Test the graph with a valid input
    try:
        graph.invoke({"a": "hello"})
    except Exception as e:
        print("An exception was raised because bad_node sets `a` to an integer.")
        print(e)
    

API Reference: StateGraph | START | END
    
    
    An exception was raised because bad_node sets `a` to an integer.
    1 validation error for OverallState
    a
      Input should be a valid string [type=string_type, input_value=123, input_type=int]
        For further information visit https://errors.pydantic.dev/2.9/v/string_type
    

## Comments

Back to top

Previous

How to add multi-turn conversation in a multi-agent application

Next

How to define input/output schema for your graph

Made with  Material for MkDocs Insiders