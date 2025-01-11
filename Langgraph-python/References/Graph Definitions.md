Graph Definitions

Table of contents
 class Graph
 meth add_conditional_edges
 meth set_entry_point 
 meth set_conditional_entry_point
 meth set_finish_point
 class CompiledGraph
 attr stream_mode
 attr stream_channels
 attr step_timeout
 attr debug
 attr checkpointer
 attr store
 attr retry_policy
 meth get_state
 meth aget_state
 meth update_state
 meth aupdate_state
 meth stream
 meth astream
 meth invoke
 meth ainvoke
 meth get_graph
 class StateGraph
 meth add_conditional_edges
 meth set_entry_point
 meth set_conditional_entry_point
 meth set_finish_point
 meth add_node
 meth add_edge
 meth add_sequence
 meth compile
 class CompiledStateGraph
 attr stream_mode: StreamMode
 attr stream_channels: list[str]
 attr step_timeout: float
 attr debug: bool
 attr checkpointer: Optional[Checkpointer]
 attr store: Optional[Store]
 attr retry_policy: RetryPolicy
 meth get_graph() -> Graph
 meth get_state(thread_id: str) -> StateSnapshot
 meth aget_state(thread_id: str) -> Awaitable[StateSnapshot]
 meth update_state(thread_id: str, state: StateSnapshot) -> None
 meth aupdate_state(thread_id: str, state: StateSnapshot) -> Awaitable[None]
 meth stream(input: Any, config: Optional[dict] = None) -> Iterator[Any]
 meth astream(input: Any, config: Optional[dict] = None) -> AsyncIterator[Any]
 meth invoke(input: Any, config: Optional[dict] = None) -> Any
 meth ainvoke(input: Any, config: Optional[dict] = None) -> Awaitable[Any]
 func add_messages(messages: list[Message]) -> None

 
 Graph
 add_conditional_edges(source: str, path: Union[Callable[..., Union[Hashable, list[Hashable]]], Callable[..., Awaitable[Union[Hashable, list[Hashable]]]], Runnable[Any, Union[Hashable, list[Hashable]]]], path_map: Optional[Union[dict[Hashable, str], list[str]]] = None, then: Optional[str] = None) -> Self
Add a conditional edge from the starting node to any number of destination nodes.

Parameters:

source (str) – The starting node. This conditional edge will run when exiting this node.
path (Union[Callable, Runnable]) – The callable that determines the next node or nodes. If not specifying path_map it should return one or more nodes. If it returns END, the graph will stop execution.
path_map (Optional[dict[Hashable, str]], default: None ) – Optional mapping of paths to node names. If omitted the paths returned by path should be node names.
then (Optional[str], default: None ) – The name of a node to execute after the nodes selected by path.
Returns:

Self – None
Without typehints on the path function's return value (e.g., -> Literal["foo", "__end__"]:)
or a path_map, the graph visualization assumes the edge could transition to any node in the graph.

 set_entry_point(key: str) -> Self
Specifies the first node to be called in the graph.

Equivalent to calling add_edge(START, key).

Parameters:

key (str) – The key of the node to set as the entry point.
Returns:

Self – None
 set_conditional_entry_point(path: Union[Callable[..., Union[Hashable, list[Hashable]]], Callable[..., Awaitable[Union[Hashable, list[Hashable]]]], Runnable[Any, Union[Hashable, list[Hashable]]]], path_map: Optional[Union[dict[Hashable, str], list[str]]] = None, then: Optional[str] = None) -> Self
Sets a conditional entry point in the graph.

Parameters:

path (Union[Callable, Runnable]) – The callable that determines the next node or nodes. If not specifying path_map it should return one or more nodes. If it returns END, the graph will stop execution.
path_map (Optional[dict[str, str]], default: None ) – Optional mapping of paths to node names. If omitted the paths returned by path should be node names.
then (Optional[str], default: None ) – The name of a node to execute after the nodes selected by path.
Returns:

Self – None
 set_finish_point(key: str) -> Self
Marks a node as a finish point of the graph.

If the graph reaches this node, it will cease execution.

Parameters:

key (str) – The key of the node to set as the finish point.
Returns:

Self – None
 CompiledGraph
Bases: Pregel

 stream_mode: StreamMode = stream_mode class-attribute instance-attribute
Mode to stream output, defaults to 'values'.

 stream_channels: Optional[Union[str, Sequence[str]]] = stream_channels class-attribute instance-attribute
Channels to stream, defaults to all channels not in reserved channels

 step_timeout: Optional[float] = step_timeout class-attribute instance-attribute
Maximum time to wait for a step to complete, in seconds. Defaults to None.

 debug: bool = debug if debug is not None else get_debug() instance-attribute
Whether to print debug information during execution. Defaults to False.

 checkpointer: Checkpointer = checkpointer class-attribute instance-attribute
Checkpointer used to save and load graph state. Defaults to None.

 store: Optional[BaseStore] = store class-attribute instance-attribute
Memory store to use for SharedValues. Defaults to None.

 retry_policy: Optional[RetryPolicy] = retry_policy class-attribute instance-attribute
Retry policy to use when running tasks. Set to None to disable.

 get_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot
Get the current state of the graph.

 aget_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot async
Get the current state of the graph.

 update_state(config: RunnableConfig, values: Optional[Union[dict[str, Any], Any]], as_node: Optional[str] = None) -> RunnableConfig
Update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous.

 aupdate_state(config: RunnableConfig, values: dict[str, Any] | Any, as_node: Optional[str] = None) -> RunnableConfig async
Update the state of the graph asynchronously with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous.

 stream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> Iterator[Union[dict[str, Any], Any]]
Stream graph steps for a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input to the graph.
config (Optional[RunnableConfig], default: None ) – The configuration to use for the run.
stream_mode (Optional[Union[StreamMode, list[StreamMode]]], default: None ) – The mode to stream output, defaults to self.stream_mode. Options are 'values', 'updates', and 'debug'. values: Emit the current values of the state for each step. updates: Emit only the updates to the state for each step. Output is a dict with the node name as key and the updated values as value. debug: Emit debug events for each step.
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – The keys to stream, defaults to all non-context channels.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt before, defaults to all nodes in the graph.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt after, defaults to all nodes in the graph.
debug (Optional[bool], default: None ) – Whether to print debug information during execution, defaults to False.
subgraphs (bool, default: False ) – Whether to stream subgraphs, defaults to False.
Yields:

Union[dict[str, Any], Any] – The output of each step in the graph. The output shape depends on the stream_mode.
Examples:

Using different stream modes with a graph:


>>> import operator
>>> from typing_extensions import Annotated, TypedDict
>>> from langgraph.graph import StateGraph
>>> from langgraph.constants import START
...
>>> class State(TypedDict):
...     alist: Annotated[list, operator.add]
...     another_list: Annotated[list, operator.add]
...
>>> builder = StateGraph(State)
>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
>>> builder.add_edge("a", "b")
>>> builder.add_edge(START, "a")
>>> graph = builder.compile()
With stream_mode="values":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
...     print(event)
{'alist': ['Ex for stream_mode="values"'], 'another_list': []}
{'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
{'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}
With stream_mode="updates":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
...     print(event)
{'a': {'another_list': ['hi']}}
{'b': {'alist': ['there']}}
With stream_mode="debug":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
...     print(event)
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}
 astream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> AsyncIterator[Union[dict[str, Any], Any]] async
Stream graph steps for a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input to the graph.
config (Optional[RunnableConfig], default: None ) – The configuration to use for the run.
stream_mode (Optional[Union[StreamMode, list[StreamMode]]], default: None ) – The mode to stream output, defaults to self.stream_mode. Options are 'values', 'updates', and 'debug'. values: Emit the current values of the state for each step. updates: Emit only the updates to the state for each step. Output is a dict with the node name as key and the updated values as value. debug: Emit debug events for each step.
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – The keys to stream, defaults to all non-context channels.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt before, defaults to all nodes in the graph.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt after, defaults to all nodes in the graph.
debug (Optional[bool], default: None ) – Whether to print debug information during execution, defaults to False.
subgraphs (bool, default: False ) – Whether to stream subgraphs, defaults to False.
Yields:

AsyncIterator[Union[dict[str, Any], Any]] – The output of each step in the graph. The output shape depends on the stream_mode.
Examples:

Using different stream modes with a graph:


>>> import operator
>>> from typing_extensions import Annotated, TypedDict
>>> from langgraph.graph import StateGraph
>>> from langgraph.constants import START
...
>>> class State(TypedDict):
...     alist: Annotated[list, operator.add]
...     another_list: Annotated[list, operator.add]
...
>>> builder = StateGraph(State)
>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
>>> builder.add_edge("a", "b")
>>> builder.add_edge(START, "a")
>>> graph = builder.compile()
With stream_mode="values":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
...     print(event)
{'alist': ['Ex for stream_mode="values"'], 'another_list': []}
{'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
{'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}
With stream_mode="updates":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
...     print(event)
{'a': {'another_list': ['hi']}}
{'b': {'alist': ['there']}}
With stream_mode="debug":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
...     print(event)
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}
 invoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any]
Run the graph with a single input and config.

Parameters:

input (Union[dict[str, Any], Any]) – The input data for the graph. It can be a dictionary or any other type.
config (Optional[RunnableConfig], default: None ) – Optional. The configuration for the graph run.
stream_mode (StreamMode, default: 'values' ) – Optional[str]. The stream mode for the graph run. Default is "values".
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – Optional. The output keys to retrieve from the graph run.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt the graph run before.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt the graph run after.
debug (Optional[bool], default: None ) – Optional. Enable debug mode for the graph run.
**kwargs (Any, default: {} ) – Additional keyword arguments to pass to the graph run.
Returns:

Union[dict[str, Any], Any] – The output of the graph run. If stream_mode is "values", it returns the latest output.
Union[dict[str, Any], Any] – If stream_mode is not "values", it returns a list of output chunks.
 ainvoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any] async
Asynchronously invoke the graph on a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input data for the computation. It can be a dictionary or any other type.
config (Optional[RunnableConfig], default: None ) – Optional. The configuration for the computation.
stream_mode (StreamMode, default: 'values' ) – Optional. The stream mode for the computation. Default is "values".
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – Optional. The output keys to include in the result. Default is None.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt before. Default is None.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt after. Default is None.
debug (Optional[bool], default: None ) – Optional. Whether to enable debug mode. Default is None.
**kwargs (Any, default: {} ) – Additional keyword arguments.
Returns:

Union[dict[str, Any], Any] – The result of the computation. If stream_mode is "values", it returns the latest value.
Union[dict[str, Any], Any] – If stream_mode is "chunks", it returns a list of chunks.
 get_graph(config: Optional[RunnableConfig] = None, *, xray: Union[int, bool] = False) -> DrawableGraph
Returns a drawable representation of the computation graph.

 StateGraph
Bases: Graph

A graph whose nodes communicate by reading and writing to a shared state. The signature of each node is State -> Partial.

Each state key can optionally be annotated with a reducer function that will be used to aggregate the values of that key received from multiple nodes. The signature of a reducer function is (Value, Value) -> Value.

Parameters:

state_schema (Type[Any], default: None ) – The schema class that defines the state.
config_schema (Optional[Type[Any]], default: None ) – The schema class that defines the configuration. Use this to expose configurable parameters in your API.
Examples:


>>> from langchain_core.runnables import RunnableConfig
>>> from typing_extensions import Annotated, TypedDict
>>> from langgraph.checkpoint.memory import MemorySaver
>>> from langgraph.graph import StateGraph
>>>
>>> def reducer(a: list, b: int | None) -> list:
...     if b is not None:
...         return a + [b]
...     return a
>>>
>>> class State(TypedDict):
...     x: Annotated[list, reducer]
>>>
>>> class ConfigSchema(TypedDict):
...     r: float
>>>
>>> graph = StateGraph(State, config_schema=ConfigSchema)
>>>
>>> def node(state: State, config: RunnableConfig) -> dict:
...     r = config["configurable"].get("r", 1.0)
...     x = state["x"][-1]
...     next_value = x * r * (1 - x)
...     return {"x": next_value}
>>>
>>> graph.add_node("A", node)
>>> graph.set_entry_point("A")
>>> graph.set_finish_point("A")
>>> compiled = graph.compile()
>>>
>>> print(compiled.config_specs)
[ConfigurableFieldSpec(id='r', annotation=<class 'float'>, name=None, description=None, default=None, is_shared=False, dependencies=None)]
>>>
>>> step1 = compiled.invoke({"x": 0.5}, {"configurable": {"r": 3.0}})
>>> print(step1)
{'x': [0.5, 0.75]}
 add_conditional_edges(source: str, path: Union[Callable[..., Union[Hashable, list[Hashable]]], Callable[..., Awaitable[Union[Hashable, list[Hashable]]]], Runnable[Any, Union[Hashable, list[Hashable]]]], path_map: Optional[Union[dict[Hashable, str], list[str]]] = None, then: Optional[str] = None) -> Self
Add a conditional edge from the starting node to any number of destination nodes.

Parameters:

source (str) – The starting node. This conditional edge will run when exiting this node.
path (Union[Callable, Runnable]) – The callable that determines the next node or nodes. If not specifying path_map it should return one or more nodes. If it returns END, the graph will stop execution.
path_map (Optional[dict[Hashable, str]], default: None ) – Optional mapping of paths to node names. If omitted the paths returned by path should be node names.
then (Optional[str], default: None ) – The name of a node to execute after the nodes selected by path.
Returns:

Self – None
Without typehints on the path function's return value (e.g., -> Literal["foo", "__end__"]:)
or a path_map, the graph visualization assumes the edge could transition to any node in the graph.

 set_entry_point(key: str) -> Self
Specifies the first node to be called in the graph.

Equivalent to calling add_edge(START, key).

Parameters:

key (str) – The key of the node to set as the entry point.
Returns:

Self – None
 set_conditional_entry_point(path: Union[Callable[..., Union[Hashable, list[Hashable]]], Callable[..., Awaitable[Union[Hashable, list[Hashable]]]], Runnable[Any, Union[Hashable, list[Hashable]]]], path_map: Optional[Union[dict[Hashable, str], list[str]]] = None, then: Optional[str] = None) -> Self
Sets a conditional entry point in the graph.

Parameters:

path (Union[Callable, Runnable]) – The callable that determines the next node or nodes. If not specifying path_map it should return one or more nodes. If it returns END, the graph will stop execution.
path_map (Optional[dict[str, str]], default: None ) – Optional mapping of paths to node names. If omitted the paths returned by path should be node names.
then (Optional[str], default: None ) – The name of a node to execute after the nodes selected by path.
Returns:

Self – None
 set_finish_point(key: str) -> Self
Marks a node as a finish point of the graph.

If the graph reaches this node, it will cease execution.

Parameters:

key (str) – The key of the node to set as the finish point.
Returns:

Self – None
 add_node(node: Union[str, RunnableLike], action: Optional[RunnableLike] = None, *, metadata: Optional[dict[str, Any]] = None, input: Optional[Type[Any]] = None, retry: Optional[RetryPolicy] = None) -> Self
Adds a new node to the state graph.

Will take the name of the function/runnable as the node name.

Parameters:

node (Union[str, RunnableLike)]) – The function or runnable this node will run.
action (Optional[RunnableLike], default: None ) – The action associated with the node. (default: None)
metadata (Optional[dict[str, Any]], default: None ) – The metadata associated with the node. (default: None)
input (Optional[Type[Any]], default: None ) – The input schema for the node. (default: the graph's input schema)
retry (Optional[RetryPolicy], default: None ) – The policy for retrying the node. (default: None)
Raises: ValueError: If the key is already being used as a state key.

Examples:


>>> from langgraph.graph import START, StateGraph
...
>>> def my_node(state, config):
...    return {"x": state["x"] + 1}
...
>>> builder = StateGraph(dict)
>>> builder.add_node(my_node)  # node name will be 'my_node'
>>> builder.add_edge(START, "my_node")
>>> graph = builder.compile()
>>> graph.invoke({"x": 1})
{'x': 2}
Customize the name:

>>> builder = StateGraph(dict)
>>> builder.add_node("my_fair_node", my_node)
>>> builder.add_edge(START, "my_fair_node")
>>> graph = builder.compile()
>>> graph.invoke({"x": 1})
{'x': 2}
Returns:

Self – StateGraph
 add_edge(start_key: Union[str, list[str]], end_key: str) -> Self
Adds a directed edge from the start node (or list of start nodes) to the end node.

When a single start node is provided, the graph will wait for that node to complete before executing the end node. When multiple start nodes are provided, the graph will wait for ALL of the start nodes to complete before executing the end node.

Parameters:

start_key (Union[str, list[str]]) – The key(s) of the start node(s) of the edge.
end_key (str) – The key of the end node of the edge.
Raises:

ValueError – If the start key is 'END' or if the start key or end key is not present in the graph.
Returns:

Self – StateGraph
 add_sequence(nodes: Sequence[Union[RunnableLike, tuple[str, RunnableLike]]]) -> Self
Add a sequence of nodes that will be executed in the provided order.

Parameters:

nodes (Sequence[Union[RunnableLike, tuple[str, RunnableLike]]]) – A sequence of RunnableLike objects (e.g. a LangChain Runnable or a callable) or (name, RunnableLike) tuples. If no names are provided, the name will be inferred from the node object (e.g. a runnable or a callable name). Each node will be executed in the order provided.
Raises:

ValueError – if the sequence is empty.
ValueError – if the sequence contains duplicate node names.
Returns:

Self – StateGraph
 compile(checkpointer: Checkpointer = None, *, store: Optional[BaseStore] = None, interrupt_before: Optional[Union[All, list[str]]] = None, interrupt_after: Optional[Union[All, list[str]]] = None, debug: bool = False) -> CompiledStateGraph
Compiles the state graph into a CompiledGraph object.

The compiled graph implements the Runnable interface and can be invoked, streamed, batched, and run asynchronously.

Parameters:

checkpointer (Optional[Union[Checkpointer, Literal[False]]], default: None ) – A checkpoint saver object or flag. If provided, this Checkpointer serves as a fully versioned "short-term memory" for the graph, allowing it to be paused, resumed, and replayed from any point. If None, it may inherit the parent graph's checkpointer when used as a subgraph. If False, it will not use or inherit any checkpointer.
interrupt_before (Optional[Sequence[str]], default: None ) – An optional list of node names to interrupt before.
interrupt_after (Optional[Sequence[str]], default: None ) – An optional list of node names to interrupt after.
debug (bool, default: False ) – A flag indicating whether to enable debug mode.
Returns:

CompiledStateGraph ( CompiledStateGraph ) – The compiled state graph.
 CompiledStateGraph
Bases: CompiledGraph

 stream_mode: StreamMode = stream_mode class-attribute instance-attribute
Mode to stream output, defaults to 'values'.

 stream_channels: Optional[Union[str, Sequence[str]]] = stream_channels class-attribute instance-attribute
Channels to stream, defaults to all channels not in reserved channels

 step_timeout: Optional[float] = step_timeout class-attribute instance-attribute
Maximum time to wait for a step to complete, in seconds. Defaults to None.

 debug: bool = debug if debug is not None else get_debug() instance-attribute
Whether to print debug information during execution. Defaults to False.

 checkpointer: Checkpointer = checkpointer class-attribute instance-attribute
Checkpointer used to save and load graph state. Defaults to None.

 store: Optional[BaseStore] = store class-attribute instance-attribute
Memory store to use for SharedValues. Defaults to None.

 retry_policy: Optional[RetryPolicy] = retry_policy class-attribute instance-attribute
Retry policy to use when running tasks. Set to None to disable.

 get_graph(config: Optional[RunnableConfig] = None, *, xray: Union[int, bool] = False) -> DrawableGraph
Returns a drawable representation of the computation graph.

 get_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot
Get the current state of the graph.

 aget_state(config: RunnableConfig, *, subgraphs: bool = False) -> StateSnapshot async
Get the current state of the graph.

 update_state(config: RunnableConfig, values: Optional[Union[dict[str, Any], Any]], as_node: Optional[str] = None) -> RunnableConfig
Update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous.

 aupdate_state(config: RunnableConfig, values: dict[str, Any] | Any, as_node: Optional[str] = None) -> RunnableConfig async
Update the state of the graph asynchronously with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous.

 stream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> Iterator[Union[dict[str, Any], Any]]
Stream graph steps for a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input to the graph.
config (Optional[RunnableConfig], default: None ) – The configuration to use for the run.
stream_mode (Optional[Union[StreamMode, list[StreamMode]]], default: None ) – The mode to stream output, defaults to self.stream_mode. Options are 'values', 'updates', and 'debug'. values: Emit the current values of the state for each step. updates: Emit only the updates to the state for each step. Output is a dict with the node name as key and the updated values as value. debug: Emit debug events for each step.
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – The keys to stream, defaults to all non-context channels.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt before, defaults to all nodes in the graph.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt after, defaults to all nodes in the graph.
debug (Optional[bool], default: None ) – Whether to print debug information during execution, defaults to False.
subgraphs (bool, default: False ) – Whether to stream subgraphs, defaults to False.
Yields:

Union[dict[str, Any], Any] – The output of each step in the graph. The output shape depends on the stream_mode.
Examples:

Using different stream modes with a graph:


>>> import operator
>>> from typing_extensions import Annotated, TypedDict
>>> from langgraph.graph import StateGraph
>>> from langgraph.constants import START
...
>>> class State(TypedDict):
...     alist: Annotated[list, operator.add]
...     another_list: Annotated[list, operator.add]
...
>>> builder = StateGraph(State)
>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
>>> builder.add_edge("a", "b")
>>> builder.add_edge(START, "a")
>>> graph = builder.compile()
With stream_mode="values":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
...     print(event)
{'alist': ['Ex for stream_mode="values"'], 'another_list': []}
{'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
{'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}
With stream_mode="updates":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
...     print(event)
{'a': {'another_list': ['hi']}}
{'b': {'alist': ['there']}}
With stream_mode="debug":

>>> for event in graph.stream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
...     print(event)
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}
 astream(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: Optional[Union[StreamMode, list[StreamMode]]] = None, output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, subgraphs: bool = False) -> AsyncIterator[Union[dict[str, Any], Any]] async
Stream graph steps for a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input to the graph.
config (Optional[RunnableConfig], default: None ) – The configuration to use for the run.
stream_mode (Optional[Union[StreamMode, list[StreamMode]]], default: None ) – The mode to stream output, defaults to self.stream_mode. Options are 'values', 'updates', and 'debug'. values: Emit the current values of the state for each step. updates: Emit only the updates to the state for each step. Output is a dict with the node name as key and the updated values as value. debug: Emit debug events for each step.
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – The keys to stream, defaults to all non-context channels.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt before, defaults to all nodes in the graph.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Nodes to interrupt after, defaults to all nodes in the graph.
debug (Optional[bool], default: None ) – Whether to print debug information during execution, defaults to False.
subgraphs (bool, default: False ) – Whether to stream subgraphs, defaults to False.
Yields:

AsyncIterator[Union[dict[str, Any], Any]] – The output of each step in the graph. The output shape depends on the stream_mode.
Examples:

Using different stream modes with a graph:


>>> import operator
>>> from typing_extensions import Annotated, TypedDict
>>> from langgraph.graph import StateGraph
>>> from langgraph.constants import START
...
>>> class State(TypedDict):
...     alist: Annotated[list, operator.add]
...     another_list: Annotated[list, operator.add]
...
>>> builder = StateGraph(State)
>>> builder.add_node("a", lambda _state: {"another_list": ["hi"]})
>>> builder.add_node("b", lambda _state: {"alist": ["there"]})
>>> builder.add_edge("a", "b")
>>> builder.add_edge(START, "a")
>>> graph = builder.compile()
With stream_mode="values":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="values"']}, stream_mode="values"):
...     print(event)
{'alist': ['Ex for stream_mode="values"'], 'another_list': []}
{'alist': ['Ex for stream_mode="values"'], 'another_list': ['hi']}
{'alist': ['Ex for stream_mode="values"', 'there'], 'another_list': ['hi']}
With stream_mode="updates":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="updates"']}, stream_mode="updates"):
...     print(event)
{'a': {'another_list': ['hi']}}
{'b': {'alist': ['there']}}
With stream_mode="debug":

>>> async for event in graph.astream({"alist": ['Ex for stream_mode="debug"']}, stream_mode="debug"):
...     print(event)
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': []}, 'triggers': ['start:a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 1, 'payload': {'id': '...', 'name': 'a', 'result': [('another_list', ['hi'])]}}
{'type': 'task', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'input': {'alist': ['Ex for stream_mode="debug"'], 'another_list': ['hi']}, 'triggers': ['a']}}
{'type': 'task_result', 'timestamp': '2024-06-23T...+00:00', 'step': 2, 'payload': {'id': '...', 'name': 'b', 'result': [('alist', ['there'])]}}
 invoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any]
Run the graph with a single input and config.

Parameters:

input (Union[dict[str, Any], Any]) – The input data for the graph. It can be a dictionary or any other type.
config (Optional[RunnableConfig], default: None ) – Optional. The configuration for the graph run.
stream_mode (StreamMode, default: 'values' ) – Optional[str]. The stream mode for the graph run. Default is "values".
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – Optional. The output keys to retrieve from the graph run.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt the graph run before.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt the graph run after.
debug (Optional[bool], default: None ) – Optional. Enable debug mode for the graph run.
**kwargs (Any, default: {} ) – Additional keyword arguments to pass to the graph run.
Returns:

Union[dict[str, Any], Any] – The output of the graph run. If stream_mode is "values", it returns the latest output.
Union[dict[str, Any], Any] – If stream_mode is not "values", it returns a list of output chunks.
 ainvoke(input: Union[dict[str, Any], Any], config: Optional[RunnableConfig] = None, *, stream_mode: StreamMode = 'values', output_keys: Optional[Union[str, Sequence[str]]] = None, interrupt_before: Optional[Union[All, Sequence[str]]] = None, interrupt_after: Optional[Union[All, Sequence[str]]] = None, debug: Optional[bool] = None, **kwargs: Any) -> Union[dict[str, Any], Any] async
Asynchronously invoke the graph on a single input.

Parameters:

input (Union[dict[str, Any], Any]) – The input data for the computation. It can be a dictionary or any other type.
config (Optional[RunnableConfig], default: None ) – Optional. The configuration for the computation.
stream_mode (StreamMode, default: 'values' ) – Optional. The stream mode for the computation. Default is "values".
output_keys (Optional[Union[str, Sequence[str]]], default: None ) – Optional. The output keys to include in the result. Default is None.
interrupt_before (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt before. Default is None.
interrupt_after (Optional[Union[All, Sequence[str]]], default: None ) – Optional. The nodes to interrupt after. Default is None.
debug (Optional[bool], default: None ) – Optional. Whether to enable debug mode. Default is None.
**kwargs (Any, default: {} ) – Additional keyword arguments.
Returns:

Union[dict[str, Any], Any] – The result of the computation. If stream_mode is "values", it returns the latest value.
Union[dict[str, Any], Any] – If stream_mode is "chunks", it returns a list of chunks.
 add_messages(left: Messages, right: Messages, *, format: Optional[Literal['langchain-openai']] = None) -> Messages
Merges two lists of messages, updating existing messages by ID.

By default, this ensures the state is "append-only", unless the new message has the same ID as an existing message.

Parameters:

left (Messages) – The base list of messages.
right (Messages) – The list of messages (or single message) to merge into the base list.
format (Optional[Literal['langchain-openai']], default: None ) – The format to return messages in. If None then messages will be returned as is. If 'langchain-openai' then messages will be returned as BaseMessage objects with their contents formatted to match OpenAI message format, meaning contents can be string, 'text' blocks, or 'image_url' blocks and tool responses are returned as their own ToolMessages.
REQUIREMENT: Must have langchain-core>=0.3.11 installed to use this feature.

Returns:

Messages – A new list of messages with the messages from right merged into left.
Messages – If a message in right has the same ID as a message in left, the
Messages – message from right will replace the message from left.
Examples:


>>> from langchain_core.messages import AIMessage, HumanMessage
>>> msgs1 = [HumanMessage(content="Hello", id="1")]
>>> msgs2 = [AIMessage(content="Hi there!", id="2")]
>>> add_messages(msgs1, msgs2)
[HumanMessage(content='Hello', id='1'), AIMessage(content='Hi there!', id='2')]

>>> msgs1 = [HumanMessage(content="Hello", id="1")]
>>> msgs2 = [HumanMessage(content="Hello again", id="1")]
>>> add_messages(msgs1, msgs2)
[HumanMessage(content='Hello again', id='1')]

>>> from typing import Annotated
>>> from typing_extensions import TypedDict
>>> from langgraph.graph import StateGraph
>>>
>>> class State(TypedDict):
...     messages: Annotated[list, add_messages]
...
>>> builder = StateGraph(State)
>>> builder.add_node("chatbot", lambda state: {"messages": [("assistant", "Hello")]})
>>> builder.set_entry_point("chatbot")
>>> builder.set_finish_point("chatbot")
>>> graph = builder.compile()
>>> graph.invoke({})
{'messages': [AIMessage(content='Hello', id=...)]}

>>> from typing import Annotated
>>> from typing_extensions import TypedDict
>>> from langgraph.graph import StateGraph, add_messages
>>>
>>> class State(TypedDict):
...     messages: Annotated[list, add_messages(format='langchain-openai')]
...
>>> def chatbot_node(state: State) -> list:
...     return {"messages": [
...         {
...             "role": "user",
...             "content": [
...                 {
...                     "type": "text",
...                     "text": "Here's an image:",
...                     "cache_control": {"type": "ephemeral"},
...                 },
...                 {
...                     "type": "image",
...                     "source": {
...                         "type": "base64",
...                         "media_type": "image/jpeg",
...                         "data": "1234",
...                     },
...                 },
...             ]
...         },
...     ]}
>>> builder = StateGraph(State)
>>> builder.add_node("chatbot", chatbot_node)
>>> builder.set_entry_point("chatbot")
>>> builder.set_finish_point("chatbot")
>>> graph = builder.compile()
>>> graph.invoke({"messages": []})
{
    'messages': [
        HumanMessage(
            content=[
                {"type": "text", "text": "Here's an image:"},
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/jpeg;base64,1234"},
                },
            ],
        ),
    ]
}
..versionchanged:: 0.2.61


Support for 'format="langchain-openai"' flag added.
