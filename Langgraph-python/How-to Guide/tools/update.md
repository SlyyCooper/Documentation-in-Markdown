## Table of Contents

- [How to update graph state from tools¶](#how-to-update-graph-state-from-tools)
  - [Setup¶](#setup)
  - [Define tool¶](#define-tool)
  - [Define prompt¶](#define-prompt)
  - [Define graph¶](#define-graph)
  - [Use it!¶](#use-it)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to update graph state from tools

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
        * How to update graph state from tools  How to update graph state from tools  Table of contents 
          * Setup 
          * Define tool 
          * Define prompt 
          * Define graph 
          * Use it! 
        * How to pass config to tools 
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
  * Define tool 
  * Define prompt 
  * Define graph 
  * Use it! 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Tool calling 

# How to update graph state from tools¶

Prerequisites

This guide assumes familiarity with the following:

  * Command

A common use case is updating graph state from inside a tool. For example, in
a customer support application you might want to look up customer account
number or ID in the beginning of the conversation. To update the graph state
from the tool, you can return `Command(update={"my_custom_key": "foo",
"messages": [...]})` from the tool:

    
    
    @tool
    def lookup_user_info(tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig):
        """Use this to look up user information to better assist them with their questions."""
        user_info = get_user_info(config)
        return Command(
            update={
                # update the state keys
                "user_info": user_info,
                # update the message history
                "messages": [ToolMessage("Successfully looked up user information", tool_call_id=tool_call_id)]
            }
        )
    

Important

If you want to use tools that return `Command` and update graph state, you can
either use prebuilt `create_react_agent` / `ToolNode` components, or implement
your own tool-executing node that collects `Command` objects returned by the
tools and returns a list of them, e.g.:

    
    
    def call_tools(state):
        ...
        commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
        return commands
    

This guide shows how you can do this using LangGraph's prebuilt components
(`create_react_agent` / `ToolNode`).

Note

Support for tools that return `Command` was added in LangGraph `v0.2.59`.

## Setup¶

First, let's install the required packages and set our API keys:

    
    
    %%capture --no-stderr
    %pip install -U langgraph langchain-openai
    
    
    
    import os
    import getpass
    
    
    def _set_if_undefined(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"Please provide your {var}")
    
    
    _set_if_undefined("OPENAI_API_KEY")
    
    
    
    Please provide your OPENAI_API_KEY ········
    

Set up LangSmith for LangGraph development

Sign up for LangSmith to quickly spot issues and improve the performance of
your LangGraph projects. LangSmith lets you use trace data to debug, test, and
monitor your LLM apps built with LangGraph — read more about how to get
started here.

Let's create a simple ReAct style agent that can look up user information and
personalize the response based on the user info.

## Define tool¶

First, let's define the tool that we'll be using to look up user information.
We'll use a naive implementation that simply looks user information up using a
dictionary:

    
    
    USER_INFO = [
        {"user_id": "1", "name": "Bob Dylan", "location": "New York, NY"},
        {"user_id": "2", "name": "Taylor Swift", "location": "Beverly Hills, CA"},
    ]
    
    USER_ID_TO_USER_INFO = {info["user_id"]: info for info in USER_INFO}
    
    
    
    from langgraph.prebuilt.chat_agent_executor import AgentState
    from langgraph.types import Command
    from langchain_core.tools import tool
    from langchain_core.tools.base import InjectedToolCallId
    from langchain_core.messages import ToolMessage
    from langchain_core.runnables import RunnableConfig
    
    from typing_extensions import Any, Annotated
    
    
    class State(AgentState):
        # updated by the tool
        user_info: dict[str, Any]
    
    
    @tool
    def lookup_user_info(
        tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig
    ):
        """Use this to look up user information to better assist them with their questions."""
        user_id = config.get("configurable", {}).get("user_id")
        if user_id is None:
            raise ValueError("Please provide user ID")
    
        if user_id not in USER_ID_TO_USER_INFO:
            raise ValueError(f"User '{user_id}' not found")
    
        user_info = USER_ID_TO_USER_INFO[user_id]
        return Command(
            update={
                # update the state keys
                "user_info": user_info,
                # update the message history
                "messages": [
                    ToolMessage(
                        "Successfully looked up user information", tool_call_id=tool_call_id
                    )
                ],
            }
        )
    

API Reference: tool | InjectedToolCallId | ToolMessage | RunnableConfig | Command

## Define prompt¶

Let's now add personalization: we'll respond differently to the user based on
the state values AFTER the state has been updated from the tool. To achieve
this, let's define a function that will dynamically construct the system
prompt based on the graph state. It will be called ever time the LLM is called
and the function output will be passed to the LLM:

    
    
    def state_modifier(state: State):
        user_info = state.get("user_info")
        if user_info is None:
            return state["messages"]
    
        system_msg = (
            f"User name is {user_info['name']}. User lives in {user_info['location']}"
        )
        return [{"role": "system", "content": system_msg}] + state["messages"]
    

## Define graph¶

Finally, let's combine this into a single graph using the prebuilt
`create_react_agent`:

    
    
    from langgraph.prebuilt import create_react_agent
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-4o")
    
    agent = create_react_agent(
        model,
        # pass the tool that can update state
        [lookup_user_info],
        state_schema=State,
        # pass dynamic prompt function
        state_modifier=state_modifier,
    )
    

API Reference: ChatOpenAI | create_react_agent

## Use it!¶

Let's now try running our agent. We'll need to provide user ID in the config
so that our tool knows what information to look up:

    
    
    for chunk in agent.stream(
        {"messages": [("user", "hi, what should i do this weekend?")]},
        # provide user ID in the config
        {"configurable": {"user_id": "1"}},
    ):
        print(chunk)
        print("\n")
    
    
    
    {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_7LSUh6ZDvGJAUvlWvXiCK4Gf', 'function': {'arguments': '{}', 'name': 'lookup_user_info'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 56, 'total_tokens': 67, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_9d50cd990b', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-57eeb216-e35d-4501-aaac-b5c6b26fb17c-0', tool_calls=[{'name': 'lookup_user_info', 'args': {}, 'id': 'call_7LSUh6ZDvGJAUvlWvXiCK4Gf', 'type': 'tool_call'}], usage_metadata={'input_tokens': 56, 'output_tokens': 11, 'total_tokens': 67, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
    
    
    {'tools': {'user_info': {'user_id': '1', 'name': 'Bob Dylan', 'location': 'New York, NY'}, 'messages': [ToolMessage(content='Successfully looked up user information', name='lookup_user_info', id='168d8ff8-b021-4c8b-a11a-3b50c30a072c', tool_call_id='call_7LSUh6ZDvGJAUvlWvXiCK4Gf')]}}
    
    
    {'agent': {'messages': [AIMessage(content="Hi Bob! Since you're in New York, NY, there are plenty of exciting things to do over the weekend. Here are some suggestions:\n\n1. **Explore Central Park**: Take a leisurely walk, rent a bike, or have a picnic in this iconic park.\n\n2. **Visit a Museum**: Check out The Metropolitan Museum of Art or the Museum of Modern Art (MoMA) for an enriching cultural experience.\n\n3. **Broadway Show**: Catch a Broadway show or an off-Broadway performance for some world-class entertainment.\n\n4. **Food Tour**: Explore different neighborhoods like Greenwich Village or Williamsburg for diverse culinary experiences.\n\n5. **Brooklyn Bridge Walk**: Take a walk across the Brooklyn Bridge for stunning views of the city skyline.\n\n6. **Visit a Rooftop Bar**: Enjoy a drink with a view at one of New York’s many rooftop bars.\n\n7. **Explore a New Neighborhood**: Discover the unique charm of areas like SoHo, Chelsea, or Astoria.\n\n8. **Live Music**: Check out live music venues for a night of great performances.\n\n9. **Art Galleries**: Visit some of the smaller art galleries around Chelsea or the Lower East Side.\n\n10. **Attend a Local Event**: Look up any local events or festivals happening this weekend.\n\nFeel free to let me know if you want more details on any of these activities!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 285, 'prompt_tokens': 95, 'total_tokens': 380, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_9d50cd990b', 'finish_reason': 'stop', 'logprobs': None}, id='run-f13ce15b-02b6-40e6-8264-c4d9edd0d03a-0', usage_metadata={'input_tokens': 95, 'output_tokens': 285, 'total_tokens': 380, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
    

We can see that the model correctly recommended some New York activities for
Bob Dylan! Let's try getting recommendations for Taylor Swift:

    
    
    for chunk in agent.stream(
        {"messages": [("user", "hi, what should i do this weekend?")]},
        {"configurable": {"user_id": "2"}},
    ):
        print(chunk)
        print("\n")
    
    
    
    {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_5HLtJtzcgmKbtmK6By21wW5Y', 'function': {'arguments': '{}', 'name': 'lookup_user_info'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 56, 'total_tokens': 67, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_c7ca0ebaca', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-bacacd7d-76cc-4f6b-9e9b-d9e6f00b9391-0', tool_calls=[{'name': 'lookup_user_info', 'args': {}, 'id': 'call_5HLtJtzcgmKbtmK6By21wW5Y', 'type': 'tool_call'}], usage_metadata={'input_tokens': 56, 'output_tokens': 11, 'total_tokens': 67, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
    
    
    {'tools': {'user_info': {'user_id': '2', 'name': 'Taylor Swift', 'location': 'Beverly Hills, CA'}, 'messages': [ToolMessage(content='Successfully looked up user information', name='lookup_user_info', id='d81ef31e-6d77-4f13-ae86-e2e6ba567e3d', tool_call_id='call_5HLtJtzcgmKbtmK6By21wW5Y')]}}
    
    
    {'agent': {'messages': [AIMessage(content="Hi Taylor! Since you're in Beverly Hills, here are a few suggestions for a fun weekend:\n\n1. **Hiking at Runyon Canyon**: Enjoy a scenic hike with beautiful views of Los Angeles. It's a great way to get some exercise and enjoy the outdoors.\n\n2. **Visit Rodeo Drive**: Spend some time shopping or window shopping at the famous Rodeo Drive. You might even spot some celebrities!\n\n3. **Explore the Getty Center**: Check out the art collections and beautiful gardens at the Getty Center. The architecture and views are stunning.\n\n4. **Relax at a Spa**: Treat yourself to a relaxing day at one of Beverly Hills' luxurious spas.\n\n5. **Dining Out**: Try a new restaurant or visit your favorite spot for a delicious meal. Beverly Hills has a fantastic dining scene.\n\n6. **Attend a Local Event**: Check out any local events or concerts happening this weekend. Beverly Hills often hosts exciting events.\n\nEnjoy your weekend!", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 198, 'prompt_tokens': 95, 'total_tokens': 293, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_c7ca0ebaca', 'finish_reason': 'stop', 'logprobs': None}, id='run-2057df76-f192-4c69-a66a-1f0a86bf5d66-0', usage_metadata={'input_tokens': 95, 'output_tokens': 198, 'total_tokens': 293, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}}
    

## Comments

Back to top

Previous

How to pass runtime values to tools

Next

How to pass config to tools

Made with  Material for MkDocs Insiders