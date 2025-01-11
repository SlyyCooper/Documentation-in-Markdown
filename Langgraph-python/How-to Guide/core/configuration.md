## Table of Contents

- [How to add runtime configuration to your graph¶](#how-to-add-runtime-configuration-to-your-graph)
  - [Setup¶](#setup)
  - [Define graph¶](#define-graph)
  - [Configure the graph¶](#configure-the-graph)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to add runtime configuration to your graph

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
      * Other  Other 
        * Other 
        * How to run a graph asynchronously 
        * How to visualize your graph 
        * How to add runtime configuration to your graph  How to add runtime configuration to your graph  Table of contents 
          * Setup 
          * Define graph 
          * Configure the graph 
        * How to add node retry policies 
        * How to return structured output with a ReAct style agent 
        * How to pass custom run ID or set tags and metadata for graph runs in LangSmith 
        * How to return state before hitting recursion limit 
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
  * Define graph 
  * Configure the graph 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Other 

# How to add runtime configuration to your graph¶

Sometimes you want to be able to configure your agent when calling it.
Examples of this include configuring which LLM to use. Below we walk through
an example of doing so.

Prerequisites

This guide assumes familiarity with the following:

  * LangGraph State 
  * Chat Models 

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain_anthropic
    
    
    
    import getpass
    import os
    
    
    def _set_env(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"{var}: ")
    
    
    _set_env("ANTHROPIC_API_KEY")
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

## Define graph¶

First, let's create a very simple graph

    
    
    import operator
    from typing import Annotated, Sequence
    from typing_extensions import TypedDict
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.messages import BaseMessage, HumanMessage
    
    from langgraph.graph import END, StateGraph, START
    
    model = ChatAnthropic(model_name="claude-2.1")
    
    
    class AgentState(TypedDict):
        messages: Annotated[Sequence[BaseMessage], operator.add]
    
    
    def _call_model(state):
        state["messages"]
        response = model.invoke(state["messages"])
        return {"messages": [response]}
    
    
    # Define a new graph
    builder = StateGraph(AgentState)
    builder.add_node("model", _call_model)
    builder.add_edge(START, "model")
    builder.add_edge("model", END)
    
    graph = builder.compile()
    

API Reference: ChatAnthropic | BaseMessage | HumanMessage | END | StateGraph | START

## Configure the graph¶

Great! Now let's suppose that we want to extend this example so the user is
able to choose from multiple llms. We can easily do that by passing in a
config. Any configuration information needs to be passed inside `configurable`
key as shown below. This config is meant to contain things are not part of the
input (and therefore that we don't want to track as part of the state).

    
    
    from langchain_openai import ChatOpenAI
    from typing import Optional
    from langchain_core.runnables.config import RunnableConfig
    
    openai_model = ChatOpenAI()
    
    models = {
        "anthropic": model,
        "openai": openai_model,
    }
    
    
    def _call_model(state: AgentState, config: RunnableConfig):
        # Access the config through the configurable key
        model_name = config["configurable"].get("model", "anthropic")
        model = models[model_name]
        response = model.invoke(state["messages"])
        return {"messages": [response]}
    
    
    # Define a new graph
    builder = StateGraph(AgentState)
    builder.add_node("model", _call_model)
    builder.add_edge(START, "model")
    builder.add_edge("model", END)
    
    graph = builder.compile()
    

API Reference: ChatOpenAI | RunnableConfig

If we call it with no configuration, it will use the default as we defined it
(Anthropic).

    
    
    graph.invoke({"messages": [HumanMessage(content="hi")]})
    
    
    
    {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
      AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01WFXkfgK8AvSckLvYYrHshi', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-ece54b16-f8fc-4201-8405-b97122edf8d8-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}
    

We can also call it with a config to get it to use a different model.

    
    
    config = {"configurable": {"model": "openai"}}
    graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)
    
    
    
    {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
      AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 8, 'total_tokens': 17, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-f8331964-d811-4b44-afb8-56c30ade7c15-0', usage_metadata={'input_tokens': 8, 'output_tokens': 9, 'total_tokens': 17})]}
    

We can also adapt our graph to take in more configuration! Like a system
message for example.

    
    
    from langchain_core.messages import SystemMessage
    
    
    # We can define a config schema to specify the configuration options for the graph
    # A config schema is useful for indicating which fields are available in the configurable dict inside the config
    class ConfigSchema(TypedDict):
        model: Optional[str]
        system_message: Optional[str]
    
    
    def _call_model(state: AgentState, config: RunnableConfig):
        # Access the config through the configurable key
        model_name = config["configurable"].get("model", "anthropic")
        model = models[model_name]
        messages = state["messages"]
        if "system_message" in config["configurable"]:
            messages = [
                SystemMessage(content=config["configurable"]["system_message"])
            ] + messages
        response = model.invoke(messages)
        return {"messages": [response]}
    
    
    # Define a new graph - note that we pass in the configuration schema here, but it is not necessary
    workflow = StateGraph(AgentState, ConfigSchema)
    workflow.add_node("model", _call_model)
    workflow.add_edge(START, "model")
    workflow.add_edge("model", END)
    
    graph = workflow.compile()
    

API Reference: SystemMessage

    
    
    graph.invoke({"messages": [HumanMessage(content="hi")]})
    
    
    
    {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
      AIMessage(content='Hello!', additional_kwargs={}, response_metadata={'id': 'msg_01VgCANVHr14PsHJSXyKkLVh', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 6}}, id='run-f8c5f18c-be58-4e44-9a4e-d43692d7eed1-0', usage_metadata={'input_tokens': 10, 'output_tokens': 6, 'total_tokens': 16})]}
    
    
    
    config = {"configurable": {"system_message": "respond in italian"}}
    graph.invoke({"messages": [HumanMessage(content="hi")]}, config=config)
    
    
    
    {'messages': [HumanMessage(content='hi', additional_kwargs={}, response_metadata={}),
      AIMessage(content='Ciao!', additional_kwargs={}, response_metadata={'id': 'msg_011YuCYQk1Rzc8PEhVCpQGr6', 'model': 'claude-2.1', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 14, 'output_tokens': 7}}, id='run-a583341e-5868-4e8c-a536-881338f21252-0', usage_metadata={'input_tokens': 14, 'output_tokens': 7, 'total_tokens': 21})]}
    

## Comments

Back to top

Previous

How to visualize your graph

Next

How to add node retry policies

Made with  Material for MkDocs Insiders