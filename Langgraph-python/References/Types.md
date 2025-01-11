Table of contents
 attr All
 attr StreamMode
 attr StreamWriter
 class RetryPolicy
   attr initial_interval
   attr backoff_factor
   attr max_interval
   attr max_attempts
   attr jitter
   attr retry_on
 class CachePolicy
 class Interrupt
 class PregelTask
 class PregelExecutableTask
 class StateSnapshot
   attr values
   attr next
   attr config
   attr metadata
   attr created_at
   attr parent_config
   attr tasks
 class Send
   meth __init__
 class Command
   func interrupt

Types
 All = Literal['*'] module-attribute
Special value to indicate that graph should interrupt on all nodes.

 StreamMode = Literal['values', 'updates', 'debug', 'messages', 'custom'] module-attribute
How the stream method should emit outputs.

'values': Emit all values of the state for each step.
'updates': Emit only the node name(s) and updates that were returned by the node(s) after each step.
'debug': Emit debug events for each step.
'messages': Emit LLM messages token-by-token.
'custom': Emit custom output write: StreamWriter kwarg of each node.
 StreamWriter = Callable[[Any], None] module-attribute
Callable that accepts a single argument and writes it to the output stream. Always injected into nodes if requested as a keyword argument, but it's a no-op when not using stream_mode="custom".

 RetryPolicy
Bases: NamedTuple

Configuration for retrying nodes.

 initial_interval: float = 0.5 class-attribute instance-attribute
Amount of time that must elapse before the first retry occurs. In seconds.

 backoff_factor: float = 2.0 class-attribute instance-attribute
Multiplier by which the interval increases after each retry.

 max_interval: float = 128.0 class-attribute instance-attribute
Maximum amount of time that may elapse between retries. In seconds.

 max_attempts: int = 3 class-attribute instance-attribute
Maximum number of attempts to make before giving up, including the first.

 jitter: bool = True class-attribute instance-attribute
Whether to add random jitter to the interval between retries.

 retry_on: Union[Type[Exception], Sequence[Type[Exception]], Callable[[Exception], bool]] = default_retry_on class-attribute instance-attribute
List of exception classes that should trigger a retry, or a callable that returns True for exceptions that should trigger a retry.

 CachePolicy
Bases: NamedTuple

Configuration for caching nodes.

 Interrupt dataclass
 PregelTask
Bases: NamedTuple

 PregelExecutableTask
Bases: NamedTuple

 StateSnapshot
Bases: NamedTuple

Snapshot of the state of the graph at the beginning of a step.

 values: Union[dict[str, Any], Any] instance-attribute
Current values of channels

 next: tuple[str, ...] instance-attribute
The name of the node to execute in each task for this step.

 config: RunnableConfig instance-attribute
Config used to fetch this snapshot

 metadata: Optional[CheckpointMetadata] instance-attribute
Metadata associated with this snapshot

 created_at: Optional[str] instance-attribute
Timestamp of snapshot creation

 parent_config: Optional[RunnableConfig] instance-attribute
Config used to fetch the parent snapshot, if any

 tasks: tuple[PregelTask, ...] instance-attribute
Tasks to execute in this step. If already attempted, may contain an error.

 Send
A message or packet to send to a specific node in the graph.

The Send class is used within a StateGraph's conditional edges to dynamically invoke a node with a custom state at the next step.

Importantly, the sent state can differ from the core graph's state, allowing for flexible and dynamic workflow management.

One such example is a "map-reduce" workflow where your graph invokes the same node multiple times in parallel with different states, before aggregating the results back into the main graph's state.

Attributes:

node (str) – The name of the target node to send the message to.
arg (Any) – The state or message to send to the target node.
Examples:


>>> from typing import Annotated
>>> import operator
>>> class OverallState(TypedDict):
...     subjects: list[str]
...     jokes: Annotated[list[str], operator.add]
...
>>> from langgraph.types import Send
>>> from langgraph.graph import END, START
>>> def continue_to_jokes(state: OverallState):
...     return [Send("generate_joke", {"subject": s}) for s in state['subjects']]
...
>>> from langgraph.graph import StateGraph
>>> builder = StateGraph(OverallState)
>>> builder.add_node("generate_joke", lambda state: {"jokes": [f"Joke about {state['subject']}"]})
>>> builder.add_conditional_edges(START, continue_to_jokes)
>>> builder.add_edge("generate_joke", END)
>>> graph = builder.compile()
>>>
>>> # Invoking with two subjects results in a generated joke for each
>>> graph.invoke({"subjects": ["cats", "dogs"]})
{'subjects': ['cats', 'dogs'], 'jokes': ['Joke about cats', 'Joke about dogs']}
 __init__(node: str, arg: Any) -> None
Initialize a new instance of the Send class.

Parameters:

node (str) – The name of the target node to send the message to.
arg (Any) – The state or message to send to the target node.
 Command dataclass
Bases: Generic[N], ToolOutputMixin

One or more commands to update the graph's state and send messages to nodes.

Parameters:

graph (Optional[str], default: None ) – graph to send the command to. Supported values are:
None: the current graph (default)
Command.PARENT: closest parent graph
update (Optional[Any], default: None ) – update to apply to the graph's state.
resume (Optional[Union[Any, dict[str, Any]]], default: None ) – value to resume execution with. To be used together with interrupt().
goto (Union[Send, Sequence[Union[Send, str]], str], default: () ) – can be one of the following:
name of the node to navigate to next (any node that belongs to the specified graph)
sequence of node names to navigate to next
Send object (to execute a node with the input provided)
sequence of Send objects
 interrupt(value: Any) -> Any
Interrupt the graph with a resumable exception from within a node.

The interrupt function enables human-in-the-loop workflows by pausing graph execution and surfacing a value to the client. This value can communicate context or request input required to resume execution.

In a given node, the first invocation of this function raises a GraphInterrupt exception, halting execution. The provided value is included with the exception and sent to the client executing the graph.

A client resuming the graph must use the Command primitive to specify a value for the interrupt and continue execution. The graph resumes from the start of the node, re-executing all logic.

If a node contains multiple interrupt calls, LangGraph matches resume values to interrupts based on their order in the node. This list of resume values is scoped to the specific task executing the node and is not shared across tasks.

To use an interrupt, you must enable a checkpointer, as the feature relies on persisting the graph state.

Example

import uuid
from typing import Optional
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.types import interrupt


class State(TypedDict):
    """The graph state."""

    foo: str
    human_value: Optional[str]
    """Human value will be updated using an interrupt."""


def node(state: State):
    answer = interrupt(
        # This value will be sent to the client
        # as part of the interrupt information.
        "what is your age?"
    )
    print(f"> Received an input from the interrupt: {answer}")
    return {"human_value": answer}


builder = StateGraph(State)
builder.add_node("node", node)
builder.add_edge(START, "node")

# A checkpointer must be enabled for interrupts to work!
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": uuid.uuid4(),
    }
}

for chunk in graph.stream({"foo": "abc"}, config):
    print(chunk)

{'__interrupt__': (Interrupt(value='what is your age?', resumable=True, ns=['node:62e598fa-8653-9d6d-2046-a70203020e37'], when='during'),)}

command = Command(resume="some input from a human!!!")

for chunk in graph.stream(Command(resume="some input from a human!!!"), config):
    print(chunk)

Received an input from the interrupt: some input from a human!!!
{'node': {'human_value': 'some input from a human!!!'}}