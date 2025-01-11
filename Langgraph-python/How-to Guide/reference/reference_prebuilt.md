## Table of Contents

- [Prebuilt¶](#prebuilt)
  - [`` `create_react_agent(model: LanguageModelLike, tools:](#-create_react_agentmodel-languagemodellike-tools)
  - [`` `ToolNode` ¶](#-toolnode-)
  - [`` `InjectedState` ¶](#-injectedstate-)
  - [`` `InjectedStore` ¶](#-injectedstore-)
  - [`` `tools_condition(state: Union[list[AnyMessage], dict[str, Any],](#-tools_conditionstate-unionlistanymessage-dictstr-any)
  - [`` `ValidationNode` ¶](#-validationnode-)
  - [Comments](#comments)

Skip to content

To learn more about LangGraph, check out our first LangChain Academy course,
_Introduction to LangGraph_ , available for free here.

Prebuilt Components

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
  * Conceptual Guides 
  * Reference 

Reference

    * Library  Library 
      * Graphs 
      * Checkpointing 
      * Storage 
      * Prebuilt Components  Prebuilt Components  Table of contents 
        * `` create_react_agent 
        * `` ToolNode 
        * `` InjectedState 
        * `` InjectedStore 
        * `` tools_condition 
        * `` ValidationNode 
      * Channels 
      * Errors 
      * Types 
      * Constants 
    * LangGraph Platform  LangGraph Platform 
      * Server API 
      * CLI 
      * SDK (Python) 
      * SDK (JS/TS) 
      * RemoteGraph 
      * Environment Variables 

Table of contents

  * `` create_react_agent 
  * `` ToolNode 
  * `` InjectedState 
  * `` InjectedStore 
  * `` tools_condition 
  * `` ValidationNode 

  1. Home 
  2. Reference 
  3. Library 

# Prebuilt¶

##  `` `create_react_agent(model: LanguageModelLike, tools:
Union[ToolExecutor, Sequence[BaseTool], ToolNode], *, state_schema:
Optional[StateSchemaType] = None, messages_modifier:
Optional[MessagesModifier] = None, state_modifier: Optional[StateModifier] =
None, response_format: Optional[Union[StructuredResponseSchema, tuple[str,
StructuredResponseSchema]]] = None, checkpointer: Optional[Checkpointer] =
None, store: Optional[BaseStore] = None, interrupt_before: Optional[list[str]]
= None, interrupt_after: Optional[list[str]] = None, debug: bool = False) ->
CompiledGraph` ¶

Creates a graph that works with a chat model that utilizes tool calling.

Parameters:

  * **`model`** (`LanguageModelLike`) – 

The `LangChain` chat model that supports tool calling.

  * **`tools`** (`Union[ToolExecutor, Sequence[BaseTool], ToolNode]`) – 

A list of tools, a ToolExecutor, or a ToolNode instance. If an empty list is
provided, the agent will consist of a single LLM node without tool calling.

  * **`state_schema`** (`Optional[StateSchemaType]`, default: `None` ) – 

An optional state schema that defines graph state. Must have `messages` and
`is_last_step` keys. Defaults to `AgentState` that defines those two keys.

  * **`messages_modifier`** (`Optional[MessagesModifier]`, default: `None` ) – 

An optional messages modifier. This applies to messages BEFORE they are passed
into the LLM.

Can take a few different forms:

    * SystemMessage: this is added to the beginning of the list of messages.
    * str: This is converted to a SystemMessage and added to the beginning of the list of messages.
    * Callable: This function should take in a list of messages and the output is then passed to the language model.
    * Runnable: This runnable should take in a list of messages and the output is then passed to the language model.

Warning

`messages_modifier` parameter is deprecated as of version 0.1.9 and will be
removed in 0.2.0

  * **`state_modifier`** (`Optional[StateModifier]`, default: `None` ) – 

An optional state modifier. This takes full graph state BEFORE the LLM is
called and prepares the input to LLM.

Can take a few different forms:

    * SystemMessage: this is added to the beginning of the list of messages in state["messages"].
    * str: This is converted to a SystemMessage and added to the beginning of the list of messages in state["messages"].
    * Callable: This function should take in full graph state and the output is then passed to the language model.
    * Runnable: This runnable should take in full graph state and the output is then passed to the language model.

  * **`response_format`** (`Optional[Union[StructuredResponseSchema, tuple[str, StructuredResponseSchema]]]`, default: `None` ) – 

An optional schema for the final agent output.

If provided, output will be formatted to match the given schema and returned
in the 'structured_response' state key. If not provided, `structured_response`
will not be present in the output state. Can be passed in as:

    
        - an OpenAI function/tool schema,
    - a JSON Schema,
    - a TypedDict class,
    - or a Pydantic class.
    - a tuple (prompt, schema), where schema is one of the above.
        The prompt will be used together with the model that is being used to generate the structured response.
    

Important

`response_format` requires the model to support `.with_structured_output`

Note

The graph will make a separate call to the LLM to generate the structured
response after the agent loop is finished. This is not the only strategy to
get structured responses, see more options in this guide.

  * **`checkpointer`** (`Optional[Checkpointer]`, default: `None` ) – 

An optional checkpoint saver object. This is used for persisting the state of
the graph (e.g., as chat memory) for a single thread (e.g., a single
conversation).

  * **`store`** (`Optional[BaseStore]`, default: `None` ) – 

An optional store object. This is used for persisting data across multiple
threads (e.g., multiple conversations / users).

  * **`interrupt_before`** (`Optional[list[str]]`, default: `None` ) – 

An optional list of node names to interrupt before. Should be one of the
following: "agent", "tools". This is useful if you want to add a user
confirmation or other interrupt before taking an action.

  * **`interrupt_after`** (`Optional[list[str]]`, default: `None` ) – 

An optional list of node names to interrupt after. Should be one of the
following: "agent", "tools". This is useful if you want to return directly or
run additional processing on an output.

  * **`debug`** (`bool`, default: `False` ) – 

A flag indicating whether to enable debug mode.

Returns:

  * `CompiledGraph` – 

A compiled LangChain runnable that can be used for chat interactions.

The resulting graph looks like this:

    
    
    stateDiagram-v2
        [*] --> Start
        Start --> Agent
        Agent --> Tools : continue
        Tools --> Agent
        Agent --> End : end
        End --> [*]
    
        classDef startClass fill:#ffdfba;
        classDef endClass fill:#baffc9;
        classDef otherClass fill:#fad7de;
    
        class Start startClass
        class End endClass
        class Agent,Tools otherClass

The "agent" node calls the language model with the messages list (after
applying the messages modifier). If the resulting AIMessage contains
`tool_calls`, the graph will then call the "tools". The "tools" node executes
the tools (1 tool per `tool_call`) and adds the responses to the messages list
as `ToolMessage` objects. The agent node then calls the language model again.
The process repeats until no more `tool_calls` are present in the response.
The agent then returns the full list of messages as a dictionary containing
the key "messages".

    
    
        sequenceDiagram
            participant U as User
            participant A as Agent (LLM)
            participant T as Tools
            U->>A: Initial input
            Note over A: Messages modifier + LLM
            loop while tool_calls present
                A->>T: Execute tools
                T-->>A: ToolMessage for each tool_calls
            end
            A->>U: Return final state

Examples:

Use with a simple tool:

    
    
    >>> from datetime import datetime
    >>> from langchain_openai import ChatOpenAI
    >>> from langgraph.prebuilt import create_react_agent
    
    
    ... def check_weather(location: str, at_time: datetime | None = None) -> str:
    ...     '''Return the weather forecast for the specified location.'''
    ...     return f"It's always sunny in {location}"
    >>>
    >>> tools = [check_weather]
    >>> model = ChatOpenAI(model="gpt-4o")
    >>> graph = create_react_agent(model, tools=tools)
    >>> inputs = {"messages": [("user", "what is the weather in sf")]}
    >>> for s in graph.stream(inputs, stream_mode="values"):
    ...     message = s["messages"][-1]
    ...     if isinstance(message, tuple):
    ...         print(message)
    ...     else:
    ...         message.pretty_print()
    ('user', 'what is the weather in sf')
    ================================== Ai Message ==================================
    Tool Calls:
    check_weather (call_LUzFvKJRuaWQPeXvBOzwhQOu)
    Call ID: call_LUzFvKJRuaWQPeXvBOzwhQOu
    Args:
        location: San Francisco
    ================================= Tool Message =================================
    Name: check_weather
    It's always sunny in San Francisco
    ================================== Ai Message ==================================
    The weather in San Francisco is sunny.
    

Add a system prompt for the LLM:

    
    
    >>> system_prompt = "You are a helpful bot named Fred."
    >>> graph = create_react_agent(model, tools, state_modifier=system_prompt)
    >>> inputs = {"messages": [("user", "What's your name? And what's the weather in SF?")]}
    >>> for s in graph.stream(inputs, stream_mode="values"):
    ...     message = s["messages"][-1]
    ...     if isinstance(message, tuple):
    ...         print(message)
    ...     else:
    ...         message.pretty_print()
    ('user', "What's your name? And what's the weather in SF?")
    ================================== Ai Message ==================================
    Hi, my name is Fred. Let me check the weather in San Francisco for you.
    Tool Calls:
    check_weather (call_lqhj4O0hXYkW9eknB4S41EXk)
    Call ID: call_lqhj4O0hXYkW9eknB4S41EXk
    Args:
        location: San Francisco
    ================================= Tool Message =================================
    Name: check_weather
    It's always sunny in San Francisco
    ================================== Ai Message ==================================
    The weather in San Francisco is currently sunny. If you need any more details or have other questions, feel free to ask!
    

Add a more complex prompt for the LLM:

    
    
    >>> from langchain_core.prompts import ChatPromptTemplate
    >>> prompt = ChatPromptTemplate.from_messages([
    ...     ("system", "You are a helpful bot named Fred."),
    ...     ("placeholder", "{messages}"),
    ...     ("user", "Remember, always be polite!"),
    ... ])
    >>> def format_for_model(state: AgentState):
    ...     # You can do more complex modifications here
    ...     return prompt.invoke({"messages": state["messages"]})
    >>>
    >>> graph = create_react_agent(model, tools, state_modifier=format_for_model)
    >>> inputs = {"messages": [("user", "What's your name? And what's the weather in SF?")]}
    >>> for s in graph.stream(inputs, stream_mode="values"):
    ...     message = s["messages"][-1]
    ...     if isinstance(message, tuple):
    ...         print(message)
    ...     else:
    ...         message.pretty_print()
    

Add complex prompt with custom graph state:

    
    
    >>> from typing_extensions import TypedDict
    >>>
    >>> from langgraph.managed import IsLastStep
    >>> prompt = ChatPromptTemplate.from_messages(
    ...     [
    ...         ("system", "Today is {today}"),
    ...         ("placeholder", "{messages}"),
    ...     ]
    ... )
    >>>
    >>> class CustomState(TypedDict):
    ...     today: str
    ...     messages: Annotated[list[BaseMessage], add_messages]
    ...     is_last_step: IsLastStep
    >>>
    >>> graph = create_react_agent(model, tools, state_schema=CustomState, state_modifier=prompt)
    >>> inputs = {"messages": [("user", "What's today's date? And what's the weather in SF?")], "today": "July 16, 2004"}
    >>> for s in graph.stream(inputs, stream_mode="values"):
    ...     message = s["messages"][-1]
    ...     if isinstance(message, tuple):
    ...         print(message)
    ...     else:
    ...         message.pretty_print()
    

Add thread-level "chat memory" to the graph:

    
    
    >>> from langgraph.checkpoint.memory import MemorySaver
    >>> graph = create_react_agent(model, tools, checkpointer=MemorySaver())
    >>> config = {"configurable": {"thread_id": "thread-1"}}
    >>> def print_stream(graph, inputs, config):
    ...     for s in graph.stream(inputs, config, stream_mode="values"):
    ...         message = s["messages"][-1]
    ...         if isinstance(message, tuple):
    ...             print(message)
    ...         else:
    ...             message.pretty_print()
    >>> inputs = {"messages": [("user", "What's the weather in SF?")]}
    >>> print_stream(graph, inputs, config)
    >>> inputs2 = {"messages": [("user", "Cool, so then should i go biking today?")]}
    >>> print_stream(graph, inputs2, config)
    ('user', "What's the weather in SF?")
    ================================== Ai Message ==================================
    Tool Calls:
    check_weather (call_ChndaktJxpr6EMPEB5JfOFYc)
    Call ID: call_ChndaktJxpr6EMPEB5JfOFYc
    Args:
        location: San Francisco
    ================================= Tool Message =================================
    Name: check_weather
    It's always sunny in San Francisco
    ================================== Ai Message ==================================
    The weather in San Francisco is sunny. Enjoy your day!
    ================================ Human Message =================================
    Cool, so then should i go biking today?
    ================================== Ai Message ==================================
    Since the weather in San Francisco is sunny, it sounds like a great day for biking! Enjoy your ride!
    

Add an interrupt to let the user confirm before taking an action:

    
    
    >>> graph = create_react_agent(
    ...     model, tools, interrupt_before=["tools"], checkpointer=MemorySaver()
    >>> )
    >>> config = {"configurable": {"thread_id": "thread-1"}}
    
    >>> inputs = {"messages": [("user", "What's the weather in SF?")]}
    >>> print_stream(graph, inputs, config)
    >>> snapshot = graph.get_state(config)
    >>> print("Next step: ", snapshot.next)
    >>> print_stream(graph, None, config)
    

Add cross-thread memory to the graph:

    
    
    >>> from langgraph.prebuilt import InjectedStore
    >>> from langgraph.store.base import BaseStore
    
    >>> def save_memory(memory: str, *, config: RunnableConfig, store: Annotated[BaseStore, InjectedStore()]) -> str:
    ...     '''Save the given memory for the current user.'''
    ...     # This is a **tool** the model can use to save memories to storage
    ...     user_id = config.get("configurable", {}).get("user_id")
    ...     namespace = ("memories", user_id)
    ...     store.put(namespace, f"memory_{len(store.search(namespace))}", {"data": memory})
    ...     return f"Saved memory: {memory}"
    
    >>> def prepare_model_inputs(state: AgentState, config: RunnableConfig, store: BaseStore):
    ...     # Retrieve user memories and add them to the system message
    ...     # This function is called **every time** the model is prompted. It converts the state to a prompt
    ...     user_id = config.get("configurable", {}).get("user_id")
    ...     namespace = ("memories", user_id)
    ...     memories = [m.value["data"] for m in store.search(namespace)]
    ...     system_msg = f"User memories: {', '.join(memories)}"
    ...     return [{"role": "system", "content": system_msg)] + state["messages"]
    
    >>> from langgraph.checkpoint.memory import MemorySaver
    >>> from langgraph.store.memory import InMemoryStore
    >>> store = InMemoryStore()
    >>> graph = create_react_agent(model, [save_memory], state_modifier=prepare_model_inputs, store=store, checkpointer=MemorySaver())
    >>> config = {"configurable": {"thread_id": "thread-1", "user_id": "1"}}
    
    >>> inputs = {"messages": [("user", "Hey I'm Will, how's it going?")]}
    >>> print_stream(graph, inputs, config)
    ('user', "Hey I'm Will, how's it going?")
    ================================== Ai Message ==================================
    Hello Will! It's nice to meet you. I'm doing well, thank you for asking. How are you doing today?
    
    >>> inputs2 = {"messages": [("user", "I like to bike")]}
    >>> print_stream(graph, inputs2, config)
    ================================ Human Message =================================
    I like to bike
    ================================== Ai Message ==================================
    That's great to hear, Will! Biking is an excellent hobby and form of exercise. It's a fun way to stay active and explore your surroundings. Do you have any favorite biking routes or trails you enjoy? Or perhaps you're into a specific type of biking, like mountain biking or road cycling?
    
    >>> config = {"configurable": {"thread_id": "thread-2", "user_id": "1"}}
    >>> inputs3 = {"messages": [("user", "Hi there! Remember me?")]}
    >>> print_stream(graph, inputs3, config)
    ================================ Human Message =================================
    Hi there! Remember me?
    ================================== Ai Message ==================================
    User memories:
    Hello! Of course, I remember you, Will! You mentioned earlier that you like to bike. It's great to hear from you again. How have you been? Have you been on any interesting bike rides lately?
    

Add a timeout for a given step:

    
    
    >>> import time
    ... def check_weather(location: str, at_time: datetime | None = None) -> float:
    ...     '''Return the weather forecast for the specified location.'''
    ...     time.sleep(2)
    ...     return f"It's always sunny in {location}"
    >>>
    >>> tools = [check_weather]
    >>> graph = create_react_agent(model, tools)
    >>> graph.step_timeout = 1 # Seconds
    >>> for s in graph.stream({"messages": [("user", "what is the weather in sf")]}):
    ...     print(s)
    TimeoutError: Timed out at step 2
    

##  `` `ToolNode` ¶

Bases: `RunnableCallable`

A node that runs the tools called in the last AIMessage.

It can be used either in StateGraph with a "messages" state key (or a custom
key passed via ToolNode's 'messages_key'). If multiple tool calls are
requested, they will be run in parallel. The output will be a list of
ToolMessages, one for each tool call.

Parameters:

  * **`tools`** (`Sequence[Union[BaseTool, Callable]]`) – 

A sequence of tools that can be invoked by the ToolNode.

  * **`name`** (`str`, default: `'tools'` ) – 

The name of the ToolNode in the graph. Defaults to "tools".

  * **`tags`** (`Optional[list[str]]`, default: `None` ) – 

Optional tags to associate with the node. Defaults to None.

  * **`handle_tool_errors`** (`Union[bool, str, Callable[..., str], tuple[type[Exception], ...]]`, default: `True` ) – 

How to handle tool errors raised by tools inside the node. Defaults to True.
Must be one of the following:

    * True: all errors will be caught and a ToolMessage with a default error message (TOOL_CALL_ERROR_TEMPLATE) will be returned.
    * str: all errors will be caught and a ToolMessage with the string value of 'handle_tool_errors' will be returned.
    * tuple[type[Exception], ...]: exceptions in the tuple will be caught and a ToolMessage with a default error message (TOOL_CALL_ERROR_TEMPLATE) will be returned.
    * Callable[..., str]: exceptions from the signature of the callable will be caught and a ToolMessage with the string value of the result of the 'handle_tool_errors' callable will be returned.
    * False: none of the errors raised by the tools will be caught

  * **`messages_key`** (`str`, default: `'messages'` ) – 

The state key in the input that contains the list of messages. The same key
will be used for the output from the ToolNode. Defaults to "messages".

The `ToolNode` is roughly analogous to:

    
    
    tools_by_name = {tool.name: tool for tool in tools}
    def tool_node(state: dict):
        result = []
        for tool_call in state["messages"][-1].tool_calls:
            tool = tools_by_name[tool_call["name"]]
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
        return {"messages": result}
    

Important

  * The state MUST contain a list of messages.
  * The last message MUST be an `AIMessage`.
  * The `AIMessage` MUST have `tool_calls` populated.

##  `` `InjectedState` ¶

Bases: `InjectedToolArg`

Annotation for a Tool arg that is meant to be populated with the graph state.

Any Tool argument annotated with InjectedState will be hidden from a tool-
calling model, so that the model doesn't attempt to generate the argument. If
using ToolNode, the appropriate graph state field will be automatically
injected into the model-generated tool args.

Parameters:

  * **`field`** (`Optional[str]`, default: `None` ) – 

The key from state to insert. If None, the entire state is expected to be
passed in.

Example

    
    
    from typing import List
    from typing_extensions import Annotated, TypedDict
    
    from langchain_core.messages import BaseMessage, AIMessage
    from langchain_core.tools import tool
    
    from langgraph.prebuilt import InjectedState, ToolNode
    
    
    class AgentState(TypedDict):
        messages: List[BaseMessage]
        foo: str
    
    @tool
    def state_tool(x: int, state: Annotated[dict, InjectedState]) -> str:
        '''Do something with state.'''
        if len(state["messages"]) > 2:
            return state["foo"] + str(x)
        else:
            return "not enough messages"
    
    @tool
    def foo_tool(x: int, foo: Annotated[str, InjectedState("foo")]) -> str:
        '''Do something else with state.'''
        return foo + str(x + 1)
    
    node = ToolNode([state_tool, foo_tool])
    
    tool_call1 = {"name": "state_tool", "args": {"x": 1}, "id": "1", "type": "tool_call"}
    tool_call2 = {"name": "foo_tool", "args": {"x": 1}, "id": "2", "type": "tool_call"}
    state = {
        "messages": [AIMessage("", tool_calls=[tool_call1, tool_call2])],
        "foo": "bar",
    }
    node.invoke(state)
    
    
    
    [
        ToolMessage(content='not enough messages', name='state_tool', tool_call_id='1'),
        ToolMessage(content='bar2', name='foo_tool', tool_call_id='2')
    ]
    

##  `` `InjectedStore` ¶

Bases: `InjectedToolArg`

Annotation for a Tool arg that is meant to be populated with LangGraph store.

Any Tool argument annotated with InjectedStore will be hidden from a tool-
calling model, so that the model doesn't attempt to generate the argument. If
using ToolNode, the appropriate store field will be automatically injected
into the model-generated tool args. Note: if a graph is compiled with a store
object, the store will be automatically propagated to the tools with
InjectedStore args when using ToolNode.

Warning

`InjectedStore` annotation requires `langchain-core >= 0.3.8`

Example

    
    
    from typing import Any
    from typing_extensions import Annotated
    
    from langchain_core.messages import AIMessage
    from langchain_core.tools import tool
    
    from langgraph.store.memory import InMemoryStore
    from langgraph.prebuilt import InjectedStore, ToolNode
    
    store = InMemoryStore()
    store.put(("values",), "foo", {"bar": 2})
    
    @tool
    def store_tool(x: int, my_store: Annotated[Any, InjectedStore()]) -> str:
        '''Do something with store.'''
        stored_value = my_store.get(("values",), "foo").value["bar"]
        return stored_value + x
    
    node = ToolNode([store_tool])
    
    tool_call = {"name": "store_tool", "args": {"x": 1}, "id": "1", "type": "tool_call"}
    state = {
        "messages": [AIMessage("", tool_calls=[tool_call])],
    }
    
    node.invoke(state, store=store)
    
    
    
    {
        "messages": [
            ToolMessage(content='3', name='store_tool', tool_call_id='1'),
        ]
    }
    

##  `` `tools_condition(state: Union[list[AnyMessage], dict[str, Any],
BaseModel], messages_key: str = 'messages') -> Literal['tools', '__end__']` ¶

Use in the conditional_edge to route to the ToolNode if the last message

has tool calls. Otherwise, route to the end.

Parameters:

  * **`state`** (`Union[list[AnyMessage], dict[str, Any], BaseModel]`) – 

The state to check for tool calls. Must have a list of messages (MessageGraph)
or have the "messages" key (StateGraph).

Returns:

  * `Literal['tools', '__end__']` – 

The next node to route to.

Examples:

Create a custom ReAct-style agent with tools.

    
    
    >>> from langchain_anthropic import ChatAnthropic
    >>> from langchain_core.tools import tool
    ...
    >>> from langgraph.graph import StateGraph
    >>> from langgraph.prebuilt import ToolNode, tools_condition
    >>> from langgraph.graph.message import add_messages
    ...
    >>> from typing import Annotated
    >>> from typing_extensions import TypedDict
    ...
    >>> @tool
    >>> def divide(a: float, b: float) -> int:
    ...     """Return a / b."""
    ...     return a / b
    ...
    >>> llm = ChatAnthropic(model="claude-3-haiku-20240307")
    >>> tools = [divide]
    ...
    >>> class State(TypedDict):
    ...     messages: Annotated[list, add_messages]
    >>>
    >>> graph_builder = StateGraph(State)
    >>> graph_builder.add_node("tools", ToolNode(tools))
    >>> graph_builder.add_node("chatbot", lambda state: {"messages":llm.bind_tools(tools).invoke(state['messages'])})
    >>> graph_builder.add_edge("tools", "chatbot")
    >>> graph_builder.add_conditional_edges(
    ...     "chatbot", tools_condition
    ... )
    >>> graph_builder.set_entry_point("chatbot")
    >>> graph = graph_builder.compile()
    >>> graph.invoke({"messages": {"role": "user", "content": "What's 329993 divided by 13662?"}})
    

This module provides a ValidationNode class that can be used to validate tool
calls in a langchain graph. It applies a pydantic schema to tool_calls in the
models' outputs, and returns a ToolMessage with the validated content. If the
schema is not valid, it returns a ToolMessage with the error message. The
ValidationNode can be used in a StateGraph with a "messages" key or in a
MessageGraph. If multiple tool calls are requested, they will be run in
parallel.

##  `` `ValidationNode` ¶

Bases: `RunnableCallable`

A node that validates all tools requests from the last AIMessage.

It can be used either in StateGraph with a "messages" key or in MessageGraph.

Note

This node does not actually **run** the tools, it only validates the tool
calls, which is useful for extraction and other use cases where you need to
generate structured output that conforms to a complex schema without losing
the original messages and tool IDs (for use in multi-turn conversations).

Parameters:

  * **`schemas`** (`Sequence[Union[BaseTool, Type[BaseModel], Callable]]`) – 

A list of schemas to validate the tool calls with. These can be any of the
following: \- A pydantic BaseModel class \- A BaseTool instance (the
args_schema will be used) \- A function (a schema will be created from the
function signature)

  * **`format_error`** (`Optional[Callable[[BaseException, ToolCall, Type[BaseModel]], str]]`, default: `None` ) – 

A function that takes an exception, a ToolCall, and a schema and returns a
formatted error string. By default, it returns the exception repr and a
message to respond after fixing validation errors.

  * **`name`** (`str`, default: `'validation'` ) – 

The name of the node.

  * **`tags`** (`Optional[list[str]]`, default: `None` ) – 

A list of tags to add to the node.

Returns:

  * `Union[Dict[str, List[ToolMessage]], Sequence[ToolMessage]]` – 

A list of ToolMessages with the validated content or error messages.

Examples:

Example usage for re-prompting the model to generate a valid response:

    
    
    >>> from typing import Literal, Annotated
    >>> from typing_extensions import TypedDict
    ...
    >>> from langchain_anthropic import ChatAnthropic
    >>> from pydantic import BaseModel, validator
    ...
    >>> from langgraph.graph import END, START, StateGraph
    >>> from langgraph.prebuilt import ValidationNode
    >>> from langgraph.graph.message import add_messages
    ...
    ...
    >>> class SelectNumber(BaseModel):
    ...     a: int
    ...
    ...     @validator("a")
    ...     def a_must_be_meaningful(cls, v):
    ...         if v != 37:
    ...             raise ValueError("Only 37 is allowed")
    ...         return v
    ...
    ...
    >>> class State(TypedDict):
    ...     messages: Annotated[list, add_messages]
    ...
    >>> builder = StateGraph(State)
    >>> llm = ChatAnthropic(model="claude-3-haiku-20240307").bind_tools([SelectNumber])
    >>> builder.add_node("model", llm)
    >>> builder.add_node("validation", ValidationNode([SelectNumber]))
    >>> builder.add_edge(START, "model")
    ...
    ...
    >>> def should_validate(state: list) -> Literal["validation", "__end__"]:
    ...     if state[-1].tool_calls:
    ...         return "validation"
    ...     return END
    ...
    ...
    >>> builder.add_conditional_edges("model", should_validate)
    ...
    ...
    >>> def should_reprompt(state: list) -> Literal["model", "__end__"]:
    ...     for msg in state[::-1]:
    ...         # None of the tool calls were errors
    ...         if msg.type == "ai":
    ...             return END
    ...         if msg.additional_kwargs.get("is_error"):
    ...             return "model"
    ...     return END
    ...
    ...
    >>> builder.add_conditional_edges("validation", should_reprompt)
    ...
    ...
    >>> graph = builder.compile()
    >>> res = graph.invoke(("user", "Select a number, any number"))
    >>> # Show the retry logic
    >>> for msg in res:
    ...     msg.pretty_print()
    ================================ Human Message =================================
    Select a number, any number
    ================================== Ai Message ==================================
    [{'id': 'toolu_01JSjT9Pq8hGmTgmMPc6KnvM', 'input': {'a': 42}, 'name': 'SelectNumber', 'type': 'tool_use'}]
    Tool Calls:
    SelectNumber (toolu_01JSjT9Pq8hGmTgmMPc6KnvM)
    Call ID: toolu_01JSjT9Pq8hGmTgmMPc6KnvM
    Args:
        a: 42
    ================================= Tool Message =================================
    Name: SelectNumber
    ValidationError(model='SelectNumber', errors=[{'loc': ('a',), 'msg': 'Only 37 is allowed', 'type': 'value_error'}])
    Respond after fixing all validation errors.
    ================================== Ai Message ==================================
    [{'id': 'toolu_01PkxSVxNxc5wqwCPW1FiSmV', 'input': {'a': 37}, 'name': 'SelectNumber', 'type': 'tool_use'}]
    Tool Calls:
    SelectNumber (toolu_01PkxSVxNxc5wqwCPW1FiSmV)
    Call ID: toolu_01PkxSVxNxc5wqwCPW1FiSmV
    Args:
        a: 37
    ================================= Tool Message =================================
    Name: SelectNumber
    {"a": 37}
    

## Comments

Back to top

Previous

Storage

Next

Channels

Made with  Material for MkDocs Insiders