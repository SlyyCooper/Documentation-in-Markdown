## Table of Contents

- [How to pass config to tools¶](#how-to-pass-config-to-tools)
  - [Setup¶](#setup)
  - [Define tools and model¶](#define-tools-and-model)
  - [ReAct Agent¶](#react-agent)
  - [Use it!¶](#use-it)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to pass config to tools

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
      * Tool calling  Tool calling 
        * Tool calling 
        * How to call tools using ToolNode 
        * How to handle tool calling errors 
        * How to pass runtime values to tools 
        * How to update graph state from tools 
        * How to pass config to tools  How to pass config to tools  Table of contents 
          * Setup 
          * Define tools and model 
          * ReAct Agent 
          * Use it! 
        * How to handle large numbers of tools 
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
      * MULTIPLE_SUBGRAPHS 
  * Conceptual Guides 
  * Reference 

Table of contents

  * Setup 
  * Define tools and model 
  * ReAct Agent 
  * Use it! 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Tool calling 

# How to pass config to tools¶

Prerequisites

This guide assumes familiarity with the following:

  * Runnable Interface 
  * Tool calling agent 
  * Tools 
  * Streaming 
  * Chat Models 

At runtime, you may need to pass values to a tool, like a user ID, which
should be set by the application logic, not controlled by the LLM, for
security reasons. The LLM should only manage its intended parameters.

LangChain tools use the `Runnable` interface, where methods like `invoke`
accept runtime information through the config argument with a `RunnableConfig`
type annotation.

In the following example, we’ll set up an agent with tools to manage a user's
favorite pets—adding, reading, and deleting entries—while fixing the user ID
through application logic and letting the chat model control other parameters

## Setup¶

First, let's install the required packages and set our API keys

    
    
    %%capture --no-stderr
    %pip install --quiet -U langgraph langchain_anthropic
    
    
    
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

## Define tools and model¶

Config type annotations

Each tool function can take a `config` argument. In order for the config to be
correctly propagated to the function, you MUST always add a `RunnableConfig`
type annotation for your `config` argument. For example:

    
    
    def my_tool(tool_arg: str, config: RunnableConfig):
        ...
    
    
    
    from typing import List
    
    from langchain_core.tools import tool
    from langchain_core.runnables.config import RunnableConfig
    
    from langgraph.prebuilt import ToolNode
    
    user_to_pets = {}
    
    
    @tool(parse_docstring=True)
    def update_favorite_pets(
        # NOTE: config arg does not need to be added to docstring, as we don't want it to be included in the function signature attached to the LLM
        pets: List[str],
        config: RunnableConfig,
    ) -> None:
        """Add the list of favorite pets.
    
        Args:
            pets: List of favorite pets to set.
        """
        user_id = config.get("configurable", {}).get("user_id")
        user_to_pets[user_id] = pets
    
    
    @tool
    def delete_favorite_pets(config: RunnableConfig) -> None:
        """Delete the list of favorite pets."""
        user_id = config.get("configurable", {}).get("user_id")
        if user_id in user_to_pets:
            del user_to_pets[user_id]
    
    
    @tool
    def list_favorite_pets(config: RunnableConfig) -> None:
        """List favorite pets if asked to."""
        user_id = config.get("configurable", {}).get("user_id")
        return ", ".join(user_to_pets.get(user_id, []))
    
    
    tools = [update_favorite_pets, delete_favorite_pets, list_favorite_pets]
    

API Reference: tool | RunnableConfig | ToolNode

We'll be using a small chat model from Anthropic in our example.

    
    
    from langchain_anthropic import ChatAnthropic
    from langgraph.graph import StateGraph, MessagesState
    from langgraph.prebuilt import ToolNode
    
    
    model = ChatAnthropic(model="claude-3-5-haiku-latest")
    

API Reference: ChatAnthropic | StateGraph | ToolNode

## ReAct Agent¶

Let's set up a graph implementation of the ReAct agent. This agent takes some
query as input, then repeatedly call tools until it has enough information to
resolve the query. We'll be using prebuilt `create_react_agent` and the
Anthropic model with tools we just defined. Note: the tools are automatically
added to the model via `model.bind_tools` inside the `create_react_agent`
implementation.

    
    
    from langgraph.prebuilt import create_react_agent
    from IPython.display import Image, display
    
    graph = create_react_agent(model, tools)
    
    try:
        display(Image(graph.get_graph().draw_mermaid_png()))
    except Exception:
        # This requires some extra dependencies and is optional
        pass
    

API Reference: create_react_agent

## Use it!¶

    
    
    from langchain_core.messages import HumanMessage
    
    user_to_pets.clear()  # Clear the state
    
    print(f"User information prior to run: {user_to_pets}")
    
    inputs = {"messages": [HumanMessage(content="my favorite pets are cats and dogs")]}
    for chunk in graph.stream(
        inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
    
    print(f"User information after the run: {user_to_pets}")
    

API Reference: HumanMessage

    
    
    User information prior to run: {}
    ================================[1m Human Message [0m=================================
    
    my favorite pets are cats and dogs
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "I'll help you update your favorite pets using the `update_favorite_pets` function.", 'type': 'text'}, {'id': 'toolu_015jtecJ4jnosAfXEC3KADS2', 'input': {'pets': ['cats', 'dogs']}, 'name': 'update_favorite_pets', 'type': 'tool_use'}]
    Tool Calls:
      update_favorite_pets (toolu_015jtecJ4jnosAfXEC3KADS2)
     Call ID: toolu_015jtecJ4jnosAfXEC3KADS2
      Args:
        pets: ['cats', 'dogs']
    =================================[1m Tool Message [0m=================================
    Name: update_favorite_pets
    
    null
    ==================================[1m Ai Message [0m==================================
    
    Great! I've added cats and dogs to your list of favorite pets. Would you like to confirm the list or do anything else with it?
    User information after the run: {'123': ['cats', 'dogs']}
    
    
    
    from langchain_core.messages import HumanMessage
    
    print(f"User information prior to run: {user_to_pets}")
    
    inputs = {"messages": [HumanMessage(content="what are my favorite pets")]}
    for chunk in graph.stream(
        inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
    
    print(f"User information prior to run: {user_to_pets}")
    

API Reference: HumanMessage

    
    
    User information prior to run: {'123': ['cats', 'dogs']}
    ================================[1m Human Message [0m=================================
    
    what are my favorite pets
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "I'll help you check your favorite pets by using the list_favorite_pets function.", 'type': 'text'}, {'id': 'toolu_01EMTtX5WtKJXMJ4WqXpxPUw', 'input': {}, 'name': 'list_favorite_pets', 'type': 'tool_use'}]
    Tool Calls:
      list_favorite_pets (toolu_01EMTtX5WtKJXMJ4WqXpxPUw)
     Call ID: toolu_01EMTtX5WtKJXMJ4WqXpxPUw
      Args:
    =================================[1m Tool Message [0m=================================
    Name: list_favorite_pets
    
    cats, dogs
    ==================================[1m Ai Message [0m==================================
    
    Based on the results, your favorite pets are cats and dogs.
    
    Is there anything else you'd like to know about your favorite pets, or would you like to update the list?
    User information prior to run: {'123': ['cats', 'dogs']}
    
    
    
    print(f"User information prior to run: {user_to_pets}")
    
    inputs = {
        "messages": [
            HumanMessage(content="please forget what i told you about my favorite animals")
        ]
    }
    for chunk in graph.stream(
        inputs, {"configurable": {"user_id": "123"}}, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
    
    print(f"User information prior to run: {user_to_pets}")
    
    
    
    User information prior to run: {'123': ['cats', 'dogs']}
    ================================[1m Human Message [0m=================================
    
    please forget what i told you about my favorite animals
    ==================================[1m Ai Message [0m==================================
    
    [{'text': "I'll help you delete the list of favorite pets. I'll use the delete_favorite_pets function to remove any previously saved list.", 'type': 'text'}, {'id': 'toolu_01JqpxgxdsDJFMzSLeogoRtG', 'input': {}, 'name': 'delete_favorite_pets', 'type': 'tool_use'}]
    Tool Calls:
      delete_favorite_pets (toolu_01JqpxgxdsDJFMzSLeogoRtG)
     Call ID: toolu_01JqpxgxdsDJFMzSLeogoRtG
      Args:
    =================================[1m Tool Message [0m=================================
    Name: delete_favorite_pets
    
    null
    ==================================[1m Ai Message [0m==================================
    
    The list of favorite pets has been deleted. If you'd like to create a new list of favorite pets in the future, just let me know.
    User information prior to run: {}
    

## Comments

Back to top

Previous

How to update graph state from tools

Next

How to handle large numbers of tools

Made with  Material for MkDocs Insiders