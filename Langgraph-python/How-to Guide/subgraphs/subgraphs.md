## Table of Contents

- [How to view and update state in subgraphs¶](#how-to-view-and-update-state-in-subgraphs)
  - [Setup¶](#setup)
  - [Define subgraph¶](#define-subgraph)
  - [Define parent graph¶](#define-parent-graph)
  - [Resuming from breakpoints¶](#resuming-from-breakpoints)
    - [Resuming from specific subgraph node¶](#resuming-from-specific-subgraph-node)
  - [Modifying state¶](#modifying-state)
    - [Update the state of a subgraph¶](#update-the-state-of-a-subgraph)
    - [Acting as a subgraph node¶](#acting-as-a-subgraph-node)
    - [Acting as the entire subgraph¶](#acting-as-the-entire-subgraph)
  - [Double nested subgraphs¶](#double-nested-subgraphs)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

How to view and update state in subgraphs

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
      * Subgraphs  Subgraphs 
        * Subgraphs 
        * How to add and use subgraphs 
        * How to view and update state in subgraphs  How to view and update state in subgraphs  Table of contents 
          * Setup 
          * Define subgraph 
          * Define parent graph 
          * Resuming from breakpoints 
            * Resuming from specific subgraph node 
          * Modifying state 
            * Update the state of a subgraph 
            * Acting as a subgraph node 
            * Acting as the entire subgraph 
          * Double nested subgraphs 
        * How to transform inputs and outputs of a subgraph 
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
  * Define subgraph 
  * Define parent graph 
  * Resuming from breakpoints 
    * Resuming from specific subgraph node 
  * Modifying state 
    * Update the state of a subgraph 
    * Acting as a subgraph node 
    * Acting as the entire subgraph 
  * Double nested subgraphs 

  1. Home 
  2. How-to Guides 
  3. LangGraph 
  4. Subgraphs 

# How to view and update state in subgraphs¶

Prerequisites

This guide assumes familiarity with the following:

  * Subgraphs 
  * Human-in-the-loop 
  * State 

Once you add persistence, you can easily view and update the state of the
subgraph at any point in time. This enables a lot of the human-in-the-loop
interaction patterns:

  * You can surface a state during an interrupt to a user to let them accept an action.
  * You can rewind the subgraph to reproduce or avoid issues.
  * You can modify the state to let the user better control its actions.

This guide shows how you can do this.

## Setup¶

First, let's install the required packages

    
    
    %%capture --no-stderr
    %pip install -U langgraph
    

Next, we need to set API keys for OpenAI (the LLM we will use):

    
    
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

## Define subgraph¶

First, let's set up our subgraph. For this, we will create a simple graph that
can get the weather for a specific city. We will compile this graph with a
breakpoint before the `weather_node`:

    
    
    from langgraph.graph import StateGraph, END, START, MessagesState
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    
    
    @tool
    def get_weather(city: str):
        """Get the weather for a specific city"""
        return f"It's sunny in {city}!"
    
    
    raw_model = ChatOpenAI()
    model = raw_model.with_structured_output(get_weather)
    
    
    class SubGraphState(MessagesState):
        city: str
    
    
    def model_node(state: SubGraphState):
        result = model.invoke(state["messages"])
        return {"city": result["city"]}
    
    
    def weather_node(state: SubGraphState):
        result = get_weather.invoke({"city": state["city"]})
        return {"messages": [{"role": "assistant", "content": result}]}
    
    
    subgraph = StateGraph(SubGraphState)
    subgraph.add_node(model_node)
    subgraph.add_node(weather_node)
    subgraph.add_edge(START, "model_node")
    subgraph.add_edge("model_node", "weather_node")
    subgraph.add_edge("weather_node", END)
    subgraph = subgraph.compile(interrupt_before=["weather_node"])
    

API Reference: tool | ChatOpenAI | StateGraph | END | START

## Define parent graph¶

We can now setup the overall graph. This graph will first route to the
subgraph if it needs to get the weather, otherwise it will route to a normal
LLM.

    
    
    from typing import Literal
    from typing_extensions import TypedDict
    from langgraph.checkpoint.memory import MemorySaver
    
    
    memory = MemorySaver()
    
    
    class RouterState(MessagesState):
        route: Literal["weather", "other"]
    
    
    class Router(TypedDict):
        route: Literal["weather", "other"]
    
    
    router_model = raw_model.with_structured_output(Router)
    
    
    def router_node(state: RouterState):
        system_message = "Classify the incoming query as either about weather or not."
        messages = [{"role": "system", "content": system_message}] + state["messages"]
        route = router_model.invoke(messages)
        return {"route": route["route"]}
    
    
    def normal_llm_node(state: RouterState):
        response = raw_model.invoke(state["messages"])
        return {"messages": [response]}
    
    
    def route_after_prediction(
        state: RouterState,
    ) -> Literal["weather_graph", "normal_llm_node"]:
        if state["route"] == "weather":
            return "weather_graph"
        else:
            return "normal_llm_node"
    
    
    graph = StateGraph(RouterState)
    graph.add_node(router_node)
    graph.add_node(normal_llm_node)
    graph.add_node("weather_graph", subgraph)
    graph.add_edge(START, "router_node")
    graph.add_conditional_edges("router_node", route_after_prediction)
    graph.add_edge("normal_llm_node", END)
    graph.add_edge("weather_graph", END)
    graph = graph.compile(checkpointer=memory)
    

API Reference: MemorySaver

    
    
    from IPython.display import Image, display
    
    # Setting xray to 1 will show the internal structure of the nested graph
    display(Image(graph.get_graph(xray=1).draw_mermaid_png()))
    

Let's test this out with a normal query to make sure it works as intended!

    
    
    config = {"configurable": {"thread_id": "1"}}
    inputs = {"messages": [{"role": "user", "content": "hi!"}]}
    for update in graph.stream(inputs, config=config, stream_mode="updates"):
        print(update)
    
    
    
    {'router_node': {'route': 'other'}}
    {'normal_llm_node': {'messages': [AIMessage(content='Hello! How can I assist you today?', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 9, 'prompt_tokens': 9, 'total_tokens': 18, 'completion_tokens_details': {'reasoning_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-35de4577-2117-40e4-ab3b-cd2ac6e27b4c-0', usage_metadata={'input_tokens': 9, 'output_tokens': 9, 'total_tokens': 18})]}}
    

Great! We didn't ask about the weather, so we got a normal response from the
LLM.

## Resuming from breakpoints¶

Let's now look at what happens with breakpoints. Let's invoke it with a query
that should get routed to the weather subgraph where we have the interrupt
node.

    
    
    config = {"configurable": {"thread_id": "2"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in graph.stream(inputs, config=config, stream_mode="updates"):
        print(update)
    
    
    
    {'router_node': {'route': 'weather'}}
    

Note that the graph stream doesn't include subgraph events. If we want to
stream subgraph events, we can pass `subgraphs=True` and get back subgraph
events like so:

    
    
    config = {"configurable": {"thread_id": "3"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in graph.stream(inputs, config=config, stream_mode="values", subgraphs=True):
        print(update)
    
    
    
    ((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
    ((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})
    

If we get the state now, we can see that it's paused on `weather_graph`

    
    
    state = graph.get_state(config)
    state.next
    
    
    
    ('weather_graph',)
    

If we look at the pending tasks for our current state, we can see that we have
one task named `weather_graph`, which corresponds to the subgraph task.

    
    
    state.tasks
    
    
    
    (PregelTask(id='0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', name='weather_graph', path=('__pregel_pull', 'weather_graph'), error=None, interrupts=(), state={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20'}}),)
    

However since we got the state using the config of the parent graph, we don't
have access to the subgraph state. If you look at the `state` value of the
`PregelTask` above you will note that it is simply the configuration of the
parent graph. If we want to actually populate the subgraph state, we can pass
in `subgraphs=True` to `get_state` like so:

    
    
    state = graph.get_state(config, subgraphs=True)
    state.tasks[0]
    
    
    
    PregelTask(id='0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', name='weather_graph', path=('__pregel_pull', 'weather_graph'), error=None, interrupts=(), state=StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'}, next=('weather_node',), config={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', 'checkpoint_id': '1ef75ee0-d9c3-6242-8001-440e7a3fb19f', 'checkpoint_map': {'': '1ef75ee0-d4e8-6ede-8001-2542067239ef', 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20': '1ef75ee0-d9c3-6242-8001-440e7a3fb19f'}}}, metadata={'source': 'loop', 'writes': {'model_node': {'city': 'San Francisco'}}, 'step': 1, 'parents': {'': '1ef75ee0-d4e8-6ede-8001-2542067239ef'}}, created_at='2024-09-18T18:44:36.278105+00:00', parent_config={'configurable': {'thread_id': '3', 'checkpoint_ns': 'weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20', 'checkpoint_id': '1ef75ee0-d4ef-6dec-8000-5d5724f3ef73'}}, tasks=(PregelTask(id='26f4384a-41d7-5ca9-cb94-4001de62e8aa', name='weather_node', path=('__pregel_pull', 'weather_node'), error=None, interrupts=(), state=None),)))
    

Now we have access to the subgraph state! If you look at the `state` value of
the `PregelTask` you can see that it has all the information we need, like the
next node (`weather_node`) and the current state values (e.g. `city`).

To resume execution, we can just invoke the outer graph as normal:

    
    
    for update in graph.stream(None, config=config, stream_mode="values", subgraphs=True):
        print(update)
    
    
    
    ((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc'), AIMessage(content="It's sunny in San Francisco!", additional_kwargs={}, response_metadata={}, id='c996ce37-438c-44f4-9e60-5aed8bcdae8a')], 'city': 'San Francisco'})
    ((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc'), AIMessage(content="It's sunny in San Francisco!", additional_kwargs={}, response_metadata={}, id='c996ce37-438c-44f4-9e60-5aed8bcdae8a')], 'route': 'weather'})
    

### Resuming from specific subgraph node¶

In the example above, we were replaying from the outer graph - which
automatically replayed the subgraph from whatever state it was in previously
(paused before the `weather_node` in our case), but it is also possible to
replay from inside a subgraph. In order to do so, we need to get the
configuration from the exact subgraph state that we want to replay from.

We can do this by exploring the state history of the subgraph, and selecting
the state before `model_node` \- which we can do by filtering on the `.next`
parameter.

To get the state history of the subgraph, we need to first pass in

    
    
    parent_graph_state_before_subgraph = next(
        h for h in graph.get_state_history(config) if h.next == ("weather_graph",)
    )
    
    
    
    subgraph_state_before_model_node = next(
        h
        for h in graph.get_state_history(parent_graph_state_before_subgraph.tasks[0].state)
        if h.next == ("model_node",)
    )
    
    # This pattern can be extended no matter how many levels deep
    # subsubgraph_stat_history = next(h for h in graph.get_state_history(subgraph_state_before_model_node.tasks[0].state) if h.next == ('my_subsubgraph_node',))
    

We can confirm that we have gotten the correct state by comparing the `.next`
parameter of the `subgraph_state_before_model_node`.

    
    
    subgraph_state_before_model_node.next
    
    
    
    ('model_node',)
    

Perfect! We have gotten the correct state snaphshot, and we can now resume
from the `model_node` inside of our subgraph:

    
    
    for value in graph.stream(
        None,
        config=subgraph_state_before_model_node.config,
        stream_mode="values",
        subgraphs=True,
    ):
        print(value)
    
    
    
    ((), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'route': 'weather'})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')]})
    (('weather_graph:0c47aeb3-6f4d-5e68-ccf4-42bd48e8ef20',), {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='108eb27a-2cbf-48d2-a6e7-6e07e82eafbc')], 'city': 'San Francisco'})
    

Great, this subsection has shown how you can replay from any node, no matter
how deeply nested it is inside your graph - a powerful tool for testing how
deterministic your agent is.

## Modifying state¶

### Update the state of a subgraph¶

What if we want to modify the state of a subgraph? We can do this similarly to
how we update the state of normal graphs, just being careful to pass in the
config of the subgraph to `update_state`.

    
    
    config = {"configurable": {"thread_id": "4"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in graph.stream(inputs, config=config, stream_mode="updates"):
        print(update)
    
    
    
    {'router_node': {'route': 'weather'}}
    
    
    
    state = graph.get_state(config, subgraphs=True)
    state.values["messages"]
    
    
    
    [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='05ee2159-3b25-4d6c-97d6-82beda3cabd4')]
    

In order to update the state of the **inner** graph, we need to pass the
config for the **inner** graph, which we can get by accessing calling
`state.tasks[0].state.config` \- since we interrupted inside the subgraph, the
state of the task is just the state of the subgraph.

    
    
    graph.update_state(state.tasks[0].state.config, {"city": "la"})
    
    
    
    {'configurable': {'thread_id': '4',
      'checkpoint_ns': 'weather_graph:67f32ef7-aee0-8a20-0eb0-eeea0fd6de6e',
      'checkpoint_id': '1ef75e5a-0b00-6bc0-8002-5726e210fef4',
      'checkpoint_map': {'': '1ef75e59-1b13-6ffe-8001-0844ae748fd5',
       'weather_graph:67f32ef7-aee0-8a20-0eb0-eeea0fd6de6e': '1ef75e5a-0b00-6bc0-8002-5726e210fef4'}}}
    

We can now resume streaming the outer graph (which will resume the subgraph!)
and check that we updated our search to use LA instead of SF.

    
    
    for update in graph.stream(None, config=config, stream_mode="updates", subgraphs=True):
        print(update)
    
    
    
    (('weather_graph:9e512e8e-bac5-5412-babe-fe5c12a47cc2',), {'weather_node': {'messages': [{'role': 'assistant', 'content': "It's sunny in la!"}]}})
    ((), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", id='35e331c6-eb47-483c-a63c-585877b12f5d'), AIMessage(content="It's sunny in la!", id='c3d6b224-9642-4b21-94d5-eef8dc3f2cc9')]}})
    

Fantastic! The AI responded with "It's sunny in LA!" as we expected.

### Acting as a subgraph node¶

Another way we could update the state is by acting as the `weather_node`
ourselves instead of editing the state before `weather_node` is ran as we did
above. We can do this by passing the subgraph config and also the `as_node`
argument, which allows us to update the state as if we are the node we
specify. Thus by setting an interrupt before the `weather_node` and then using
the update state function as the `weather_node`, the graph itself never calls
`weather_node` directly but instead we decide what the output of
`weather_node` should be.

    
    
    config = {"configurable": {"thread_id": "14"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in graph.stream(
        inputs, config=config, stream_mode="updates", subgraphs=True
    ):
        print(update)
    # Graph execution should stop before the weather node
    print("interrupted!")
    
    state = graph.get_state(config, subgraphs=True)
    
    # We update the state by passing in the message we want returned from the weather node, and make sure to use as_node
    graph.update_state(
        state.tasks[0].state.config,
        {"messages": [{"role": "assistant", "content": "rainy"}]},
        as_node="weather_node",
    )
    for update in graph.stream(None, config=config, stream_mode="updates", subgraphs=True):
        print(update)
    
    print(graph.get_state(config).values["messages"])
    
    
    
    ((), {'router_node': {'route': 'weather'}})
    (('weather_graph:c7eb1fc7-efab-b0e3-12ed-8586f37bc7a2',), {'model_node': {'city': 'San Francisco'}})
    interrupted!
    ((), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='ad694c4e-8aac-4e1f-b5ca-790c60c1775b'), AIMessage(content='rainy', additional_kwargs={}, response_metadata={}, id='98a73aaf-3524-482a-9d07-971407df0389')]}})
    [HumanMessage(content="what's the weather in sf", additional_kwargs={}, response_metadata={}, id='ad694c4e-8aac-4e1f-b5ca-790c60c1775b'), AIMessage(content='rainy', additional_kwargs={}, response_metadata={}, id='98a73aaf-3524-482a-9d07-971407df0389')]
    

Perfect! The AI responded with the message we passed in ourselves.

### Acting as the entire subgraph¶

Lastly, we could also update the graph just acting as the **entire** subgraph.
This is similar to the case above but instead of acting as just the
`weather_node` we are acting as the entire subgraph. This is done by passing
in the normal graph config as well as the `as_node` argument, where we specify
the we are acting as the entire subgraph node.

    
    
    config = {"configurable": {"thread_id": "8"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in graph.stream(
        inputs, config=config, stream_mode="updates", subgraphs=True
    ):
        print(update)
    # Graph execution should stop before the weather node
    print("interrupted!")
    
    # We update the state by passing in the message we want returned from the weather graph, making sure to use as_node
    # Note that we don't need to pass in the subgraph config, since we aren't updating the state inside the subgraph
    graph.update_state(
        config,
        {"messages": [{"role": "assistant", "content": "rainy"}]},
        as_node="weather_graph",
    )
    for update in graph.stream(None, config=config, stream_mode="updates"):
        print(update)
    
    print(graph.get_state(config).values["messages"])
    
    
    
    ((), {'router_node': {'route': 'weather'}})
    (('weather_graph:53ab3fb1-23e8-5de0-acc6-9fb904fd4dc4',), {'model_node': {'city': 'San Francisco'}})
    interrupted!
    [HumanMessage(content="what's the weather in sf", id='64b1b683-778b-4623-b783-4a8f81322ec8'), AIMessage(content='rainy', id='c1d1a2f3-c117-41e9-8c1f-8fb0a02a3b70')]
    

Again, the AI responded with "rainy" as we expected.

## Double nested subgraphs¶

This same functionality continues to work no matter the level of nesting. Here
is an example of doing the same things with a double nested subgraph (although
any level of nesting will work). We add another router on top of our already
defined graphs.

    
    
    from typing import Literal
    from typing_extensions import TypedDict
    from langgraph.checkpoint.memory import MemorySaver
    
    
    memory = MemorySaver()
    
    
    class RouterState(MessagesState):
        route: Literal["weather", "other"]
    
    
    class Router(TypedDict):
        route: Literal["weather", "other"]
    
    
    router_model = raw_model.with_structured_output(Router)
    
    
    def router_node(state: RouterState):
        system_message = "Classify the incoming query as either about weather or not."
        messages = [{"role": "system", "content": system_message}] + state["messages"]
        route = router_model.invoke(messages)
        return {"route": route["route"]}
    
    
    def normal_llm_node(state: RouterState):
        response = raw_model.invoke(state["messages"])
        return {"messages": [response]}
    
    
    def route_after_prediction(
        state: RouterState,
    ) -> Literal["weather_graph", "normal_llm_node"]:
        if state["route"] == "weather":
            return "weather_graph"
        else:
            return "normal_llm_node"
    
    
    graph = StateGraph(RouterState)
    graph.add_node(router_node)
    graph.add_node(normal_llm_node)
    graph.add_node("weather_graph", subgraph)
    graph.add_edge(START, "router_node")
    graph.add_conditional_edges("router_node", route_after_prediction)
    graph.add_edge("normal_llm_node", END)
    graph.add_edge("weather_graph", END)
    graph = graph.compile()
    

API Reference: MemorySaver

    
    
    from langgraph.checkpoint.memory import MemorySaver
    
    memory = MemorySaver()
    
    
    class GrandfatherState(MessagesState):
        to_continue: bool
    
    
    def router_node(state: GrandfatherState):
        # Dummy logic that will always continue
        return {"to_continue": True}
    
    
    def route_after_prediction(state: GrandfatherState):
        if state["to_continue"]:
            return "graph"
        else:
            return END
    
    
    grandparent_graph = StateGraph(GrandfatherState)
    grandparent_graph.add_node(router_node)
    grandparent_graph.add_node("graph", graph)
    grandparent_graph.add_edge(START, "router_node")
    grandparent_graph.add_conditional_edges(
        "router_node", route_after_prediction, ["graph", END]
    )
    grandparent_graph.add_edge("graph", END)
    grandparent_graph = grandparent_graph.compile(checkpointer=MemorySaver())
    

API Reference: MemorySaver

    
    
    from IPython.display import Image, display
    
    # Setting xray to 1 will show the internal structure of the nested graph
    display(Image(grandparent_graph.get_graph(xray=2).draw_mermaid_png()))
    

If we run until the interrupt, we can now see that there are snapshots of the
state of all three graphs

    
    
    config = {"configurable": {"thread_id": "2"}}
    inputs = {"messages": [{"role": "user", "content": "what's the weather in sf"}]}
    for update in grandparent_graph.stream(
        inputs, config=config, stream_mode="updates", subgraphs=True
    ):
        print(update)
    
    
    
    ((), {'router_node': {'to_continue': True}})
    (('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8',), {'router_node': {'route': 'weather'}})
    (('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8', 'weather_graph:12bd3069-de24-5bc6-b4f1-f39527605781'), {'model_node': {'city': 'San Francisco'}})
    
    
    
    state = grandparent_graph.get_state(config, subgraphs=True)
    print("Grandparent State:")
    print(state.values)
    print("---------------")
    print("Parent Graph State:")
    print(state.tasks[0].state.values)
    print("---------------")
    print("Subgraph State:")
    print(state.tasks[0].state.tasks[0].state.values)
    
    
    
    Grandparent State:
    {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'to_continue': True}
    ---------------
    Parent Graph State:
    {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'route': 'weather'}
    ---------------
    Subgraph State:
    {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848')], 'city': 'San Francisco'}
    

We can now continue, acting as the node three levels down

    
    
    grandparent_graph_state = state
    parent_graph_state = grandparent_graph_state.tasks[0].state
    subgraph_state = parent_graph_state.tasks[0].state
    grandparent_graph.update_state(
        subgraph_state.config,
        {"messages": [{"role": "assistant", "content": "rainy"}]},
        as_node="weather_node",
    )
    for update in grandparent_graph.stream(
        None, config=config, stream_mode="updates", subgraphs=True
    ):
        print(update)
    
    print(grandparent_graph.get_state(config).values["messages"])
    
    
    
    (('graph:e18ecd45-5dfb-53b0-bcb7-db793924e9a8',), {'weather_graph': {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]}})
    ((), {'graph': {'messages': [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]}})
    [HumanMessage(content="what's the weather in sf", id='3bb28060-3d30-49a7-9f84-c90b6ada7848'), AIMessage(content='rainy', id='be926b59-c647-4355-88fd-a429b9e2b420')]
    

As in the cases above, we can see that the AI responds with "rainy" as we
expect.

We can explore the state history to see how the state of the grandparent graph
was updated at each step.

    
    
    for state in grandparent_graph.get_state_history(config):
        print(state)
        print("-----")
    
    
    
    StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720'), AIMessage(content='rainy', id='7c80f847-248d-4b8f-8238-633ed757b353')], 'to_continue': True}, next=(), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f40-7a2c-6f9e-8002-a37a61b26709'}}, metadata={'source': 'loop', 'writes': {'graph': {'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720'), AIMessage(content='rainy', id='7c80f847-248d-4b8f-8238-633ed757b353')]}}, 'step': 2, 'parents': {}}, created_at='2024-08-30T17:19:35.793847+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f312-6338-8001-766acddc781e'}}, tasks=())
    -----
    StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720')], 'to_continue': True}, next=('graph',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f312-6338-8001-766acddc781e'}}, metadata={'source': 'loop', 'writes': {'router_node': {'to_continue': True}}, 'step': 1, 'parents': {}}, created_at='2024-08-30T17:19:21.627097+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f303-61d0-8000-1945c8a74e9e'}}, tasks=(PregelTask(id='b59fe96f-fdce-5afe-aa58-bd2876a0d592', name='graph', error=None, interrupts=(), state={'configurable': {'thread_id': '2', 'checkpoint_ns': 'graph:b59fe96f-fdce-5afe-aa58-bd2876a0d592'}}),))
    -----
    StateSnapshot(values={'messages': [HumanMessage(content="what's the weather in sf", id='5ff89e4d-8255-4d23-8b55-01633c112720')]}, next=('router_node',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f303-61d0-8000-1945c8a74e9e'}}, metadata={'source': 'loop', 'writes': None, 'step': 0, 'parents': {}}, created_at='2024-08-30T17:19:21.620923+00:00', parent_config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f2f9-6d6a-bfff-c8b76e5b2462'}}, tasks=(PregelTask(id='e3d4a97a-f4ca-5260-801e-e65b02907825', name='router_node', error=None, interrupts=(), state=None),))
    -----
    StateSnapshot(values={'messages': []}, next=('__start__',), config={'configurable': {'thread_id': '2', 'checkpoint_ns': '', 'checkpoint_id': '1ef66f3f-f2f9-6d6a-bfff-c8b76e5b2462'}}, metadata={'source': 'input', 'writes': {'messages': [{'role': 'user', 'content': "what's the weather in sf"}]}, 'step': -1, 'parents': {}}, created_at='2024-08-30T17:19:21.617127+00:00', parent_config=None, tasks=(PregelTask(id='f0538638-b794-58fc-a406-980d2fea28a1', name='__start__', error=None, interrupts=(), state=None),))
    -----
    

## Comments

Back to top

Previous

How to add and use subgraphs

Next

How to transform inputs and outputs of a subgraph

Made with  Material for MkDocs Insiders