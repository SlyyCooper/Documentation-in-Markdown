1/11/25, 3:43 PM

SDK (Python)

Home

Reference

LangGraph Platform

Python SDK Reference

The LangGraph client implementations connect to the LangGraph API.

This module provides both asynchronous (LangGraphClient) and synchronous

(SyncLanggraphClient) clients to interacting with the LangGraph API's core resources such as

Assistants, Threads, Runs, and Cron jobs, as well as its persistent document Store.

class LangGraphClient

Top-level client for LangGraph API.

Attributes:

assistants  – Manages versioned con guration for your graphs.

threads  – Handles (potentially) multi-turn interactions, such as conversational threads.

runs  – Controls individual invocations of the graph.

crons  – Manages scheduled operations.

store  – Interfaces with persistent, shared data storage.

class HttpClient

Handle async requests to the LangGraph API.

Adds additional error messaging & content handling above the provided httpx client.

Attributes:

client  ( AsyncClient ) – Underlying HTTPX async client.

meth   get(path: str, *, params: Optional[QueryParamTypes] = None) ->
Any

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

1/121

async1/11/25, 3:43 PM

SDK (Python)

Send a GET request.

meth   post(path: str, *, json: Optional[dict]) -> Any

Send a POST request.

meth   put(path: str, *, json: dict) -> Any

Send a PUT request.

meth   patch(path: str, *, json: dict) -> Any

Send a PATCH request.

meth   delete(path: str, *, json: Optional[Any] = None) -> None

Send a DELETE request.

meth   stream(path: str, method: str, *, json: Optional[dict] = None,
params: Optional[QueryParamTypes] = None) ->

AsyncIterator[StreamPart]

Stream results using SSE.

class AssistantsClient

Client for managing assistants in LangGraph.

This class provides methods to interact with assistants, which are versioned con gurations of

your graph.

Example:

client = get_client()
assistant = await client.assistants.get("assistant_id_123")

meth   get(assistant_id: str) -> Assistant

Get an assistant by ID.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

2/121

asyncasyncasyncasyncasyncasync1/11/25, 3:43 PM

SDK (Python)

Parameters:

assistant_id  ( str ) – The ID of the assistant to get.

Returns:

Assistant  (  Assistant  ) – Assistant Object.

Example Usage:

assistant = await client.assistants.get(

assistant_id="my_assistant_id"

)
print(assistant)

----------------------------------------------------

{

}

'assistant_id': 'my_assistant_id',
'graph_id': 'agent',
'created_at': '2024-06-25T17:10:33.109781+00:00',
'updated_at': '2024-06-25T17:10:33.109781+00:00',
'config': {},
'metadata': {'created_by': 'system'}

meth   get_graph(assistant_id: str, *, xray: Union[int, bool] = False)
-> dict[str, list[dict[str, Any]]]

Get the graph of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the graph of.

xray  ( Union[int, bool] , default:  False  ) – Include graph representation of subgraphs. If

an integer value is provided, only subgraphs with a depth less than or equal to the value

will be included.

Returns:

Graph  (  dict[str, list[dict[str, Any]]]  ) – The graph information for the assistant in

JSON format.

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

3/121

async1/11/25, 3:43 PM

SDK (Python)

graph_info = await client.assistants.get_graph(

assistant_id="my_assistant_id"

)
print(graph_info)

---------------------------------------------------------------------------------
-----------------------------------------

{

'nodes':
[

{'id': '__start__', 'type': 'schema', 'data': '__start__'},
{'id': '__end__', 'type': 'schema', 'data': '__end__'},
{'id': 'agent','type': 'runnable','data': {'id': ['langgraph',

'utils', 'RunnableCallable'],'name': 'agent'}},

],

'edges':
[

]

}

{'source': '__start__', 'target': 'agent'},
{'source': 'agent','target': '__end__'}

meth   get_schemas(assistant_id: str) -> GraphSchema

Get the schemas of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the schema of.

Returns:

GraphSchema  (  GraphSchema  ) – The graph schema for the assistant.

Example Usage:

schema = await client.assistants.get_schemas(

assistant_id="my_assistant_id"

)
print(schema)

---------------------------------------------------------------------------------
-------------------------------------------

{

'graph_id': 'agent',
'state_schema':

{

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

4/121

async1/11/25, 3:43 PM

SDK (Python)

'title': 'LangGraphInput',
'$ref': '#/definitions/AgentState',
'definitions':

{

'BaseMessage':

{

are the inputs and outputs of ChatModels.',

'title': 'BaseMessage',
'description': 'Base abstract Message class. Messages

'type': 'object',
'properties':

{

'content':

{

[{'type': 'string'}, {'type': 'object'}]}}

'title': 'Content',
'anyOf': [

{'type': 'string'},
{'type': 'array','items': {'anyOf':

]

},

'additional_kwargs':

{

},

'title': 'Additional Kwargs',
'type': 'object'

'response_metadata':

{

},

'type':

{

},

'name':

{

},

'id':
{

}

},

'title': 'Response Metadata',
'type': 'object'

'title': 'Type',
'type': 'string'

'title': 'Name',
'type': 'string'

'title': 'Id',
'type': 'string'

'required': ['content', 'type']

},

'AgentState':

{

'title': 'AgentState',
'type': 'object',

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

5/121

1/11/25, 3:43 PM

SDK (Python)

'properties':

{

'messages':

'title': 'Messages',
'type': 'array',
'items': {'$ref':

{

}

'#/definitions/BaseMessage'}

},

'required': ['messages']

}

}

},

'config_schema':

{

}

}

'title': 'Configurable',
'type': 'object',
'properties':

{

}

'model_name':

{

}

'title': 'Model Name',
'enum': ['anthropic', 'openai'],
'type': 'string'

meth   get_subgraphs(assistant_id: str, namespace: Optional[str] =
None, recurse: bool = False) -> Subgraphs

Get the schemas of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the schema of.

Returns:

Subgraphs  (  Subgraphs  ) – The graph schema for the assistant.

meth   create(graph_id: Optional[str], config: Optional[Config] = None,
*, metadata: Json = None, assistant_id: Optional[str] = None,

if_exists: Optional[OnConflictBehavior] = None, name: Optional[str] =

None) -> Assistant

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

6/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

Create a new assistant.

Useful when graph is con gurable and you want to create different assistants based on

different con gurations.

Parameters:

graph_id  ( Optional[str] ) – The ID of the graph the assistant should use. The graph ID is

normally set in your langgraph.json con guration.

config  ( Optional[Config] , default:  None  ) – Con guration to use for the graph.

metadata  ( Json , default:  None  ) – Metadata to add to assistant.

assistant_id  ( Optional[str] , default:  None  ) – Assistant ID to use, will default to a

random UUID if not provided.

if_exists  ( Optional[OnConflictBehavior] , default:  None  ) – How to handle duplicate

creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate),

or 'do_nothing' (return existing assistant).

name  ( Optional[str] , default:  None  ) – The name of the assistant. Defaults to 'Untitled'

under the hood.

Returns:

Assistant  (  Assistant  ) – The created assistant.

Example Usage:

assistant = await client.assistants.create(

graph_id="agent",
config={"configurable": {"model_name": "openai"}},
metadata={"number":1},
assistant_id="my-assistant-id",
if_exists="do_nothing",
name="my_name"

)

meth   update(assistant_id: str, *, graph_id: Optional[str] = None,
config: Optional[Config] = None, metadata: Json = None, name:

Optional[str] = None) -> Assistant

Update an assistant.

Use this to point to a different graph, update the con guration, or change the metadata of an

assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

7/121

async1/11/25, 3:43 PM

SDK (Python)

Parameters:

assistant_id  ( str ) – Assistant to update.

graph_id  ( Optional[str] , default:  None  ) – The ID of the graph the assistant should use.

The graph ID is normally set in your langgraph.json con guration. If None, assistant will

keep pointing to same graph.

config  ( Optional[Config] , default:  None  ) – Con guration to use for the graph.

metadata  ( Json , default:  None  ) – Metadata to merge with existing assistant metadata.

name  ( Optional[str] , default:  None  ) – The new name for the assistant.

Returns:

Assistant  (  Assistant  ) – The updated assistant.

Example Usage:

assistant = await client.assistants.update(

assistant_id='e280dad7-8618-443f-87f1-8e41841c180f',
graph_id="other-graph",
config={"configurable": {"model_name": "anthropic"}},
metadata={"number":2}

)

meth   delete(assistant_id: str) -> None

Delete an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to delete.

Returns:

None  – None

Example Usage:

await client.assistants.delete(

assistant_id="my_assistant_id"

)

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

8/121

async1/11/25, 3:43 PM

SDK (Python)

meth   search(*, metadata: Json = None, graph_id: Optional[str] = None,
limit: int = 10, offset: int = 0) -> list[Assistant]

Search for assistants.

Parameters:

metadata  ( Json , default:  None  ) – Metadata to  lter by. Exact match  lter for each KV pair.

graph_id  ( Optional[str] , default:  None  ) – The ID of the graph to  lter by. The graph ID is

normally set in your langgraph.json con guration.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

Returns:

list[Assistant]  – list[Assistant]: A list of assistants.

Example Usage:

assistants = await client.assistants.search(

metadata = {"name":"my_name"},
graph_id="my_graph_id",
limit=5,
offset=5

)

meth   get_versions(assistant_id: str, metadata: Json = None, limit:
int = 10, offset: int = 0) -> list[AssistantVersion]

List all versions of an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to get versions for.

metadata  ( Json , default:  None  ) – Metadata to  lter versions by. Exact match  lter for

each KV pair.

limit  ( int , default:  10  ) – The maximum number of versions to return.

offset  ( int , default:  0  ) – The number of versions to skip.

Returns:

list[AssistantVersion]  – list[Assistant]: A list of assistants.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

9/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

Example Usage:

assistant_versions = await client.assistants.get_versions(

assistant_id="my_assistant_id"

)

meth   set_latest(assistant_id: str, version: int) -> Assistant

Change the version of an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to delete.

version  ( int ) – The version to change to.

Returns:

Assistant  (  Assistant  ) – Assistant Object.

Example Usage:

new_version_assistant = await client.assistants.set_latest(

assistant_id="my_assistant_id",
version=3

)

class ThreadsClient

Client for managing threads in LangGraph.

A thread maintains the state of a graph across multiple interactions/invocations (aka runs). It

accumulates and persists the graph's state, allowing for continuity between separate

invocations of the graph.

Example:

client = get_client()
new_thread = await client.threads.create(metadata={"user_id": "123"})

meth   get(thread_id: str) -> Thread

Get a thread by ID.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

10/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

Parameters:

thread_id  ( str ) – The ID of the thread to get.

Returns:

Thread  (  Thread  ) – Thread object.

Example Usage:

thread = await client.threads.get(

thread_id="my_thread_id"

)
print(thread)

-----------------------------------------------------

{

}

'thread_id': 'my_thread_id',
'created_at': '2024-07-18T18:35:15.540834+00:00',
'updated_at': '2024-07-18T18:35:15.540834+00:00',
'metadata': {'graph_id': 'agent'}

meth   create(*, metadata: Json = None, thread_id: Optional[str] =
None, if_exists: Optional[OnConflictBehavior] = None) -> Thread

Create a new thread.

Parameters:

metadata  ( Json , default:  None  ) – Metadata to add to thread.

thread_id  ( Optional[str] , default:  None  ) – ID of thread. If None, ID will be a randomly

generated UUID.

if_exists  ( Optional[OnConflictBehavior] , default:  None  ) – How to handle duplicate

creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate),

or 'do_nothing' (return existing thread).

Returns:

Thread  (  Thread  ) – The created thread.

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

11/121

async1/11/25, 3:43 PM

SDK (Python)

thread = await client.threads.create(

metadata={"number":1},
thread_id="my-thread-id",
if_exists="raise"

)

meth   update(thread_id: str, *, metadata: dict[str, Any]) -> Thread

Update a thread.

Parameters:

thread_id  ( str ) – ID of thread to update.

metadata  ( dict[str, Any] ) – Metadata to merge with existing thread metadata.

Returns:

Thread  (  Thread  ) – The created thread.

Example Usage:

thread = await client.threads.update(

thread_id="my-thread-id",
metadata={"number":1},

)

meth   delete(thread_id: str) -> None

Delete a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to delete.

Returns:

None  – None

Example Usage:

await client.threads.delete(
thread_id="my_thread_id"

)

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

12/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

meth   search(*, metadata: Json = None, values: Json = None, status:
Optional[ThreadStatus] = None, limit: int = 10, offset: int = 0) ->

list[Thread]

Search for threads.

Parameters:

metadata  ( Json , default:  None  ) – Thread metadata to  lter on.

values  ( Json , default:  None  ) – State values to  lter on.

status  ( Optional[ThreadStatus] , default:  None  ) – Thread status to  lter on. Must be one

of 'idle', 'busy', 'interrupted' or 'error'.

limit  ( int , default:  10  ) – Limit on number of threads to return.

offset  ( int , default:  0  ) – Offset in threads table to start search from.

Returns:

list[Thread]  – list[Thread]: List of the threads matching the search parameters.

Example Usage:

threads = await client.threads.search(

metadata={"number":1},
status="interrupted",
limit=15,
offset=5

)

meth   copy(thread_id: str) -> None

Copy a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to copy.

Returns:

None  – None

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

13/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

await client.threads.copy(

thread_id="my_thread_id"

)

meth   get_state(thread_id: str, checkpoint: Optional[Checkpoint] =
None, checkpoint_id: Optional[str] = None, *, subgraphs: bool =

False) -> ThreadState

Get the state of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to get the state of.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to get the state of.

subgraphs  ( bool , default:  False  ) – Include subgraphs states.

Returns:

ThreadState  (  ThreadState  ) – the thread of the state.

Example Usage:

thread_state = await client.threads.get_state(

thread_id="my_thread_id",
checkpoint_id="my_checkpoint_id"

)
print(thread_state)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
----

{

'values': {

'messages': [

'content': 'how are you?',
'additional_kwargs': {},
'response_metadata': {},
'type': 'human',
'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10',
'example': False

{

},
{

assistant created by Anthropic to be helpful, honest, and harmless.",

'content': "I'm doing well, thanks for asking! I'm an AI

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

14/121

async1/11/25, 3:43 PM

SDK (Python)

'additional_kwargs': {},
'response_metadata': {},
'type': 'ai',
'name': None,
'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
'example': False,
'tool_calls': [],
'invalid_tool_calls': [],
'usage_metadata': None

}

]

},
'next': [],
'checkpoint':

{

}

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1'

'metadata':

{

'step': 1,
'run_id': '1ef4a9b8-d7da-679a-a45a-872054341df2',
'source': 'loop',
'writes':
{

'agent':
{

'messages': [

{

cef87798fe8b',

'id': 'run-159b782c-b679-4830-83c6-

'name': None,
'type': 'ai',
'content': "I'm doing well, thanks for

asking! I'm an AI assistant created by Anthropic to be helpful, honest, and
harmless.",

'example': False,
'tool_calls': [],
'usage_metadata': None,
'additional_kwargs': {},
'response_metadata': {},
'invalid_tool_calls': []

}

]

}

},

'user_id': None,
'graph_id': 'agent',
'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'created_by': 'system',
'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'},
'created_at': '2024-07-25T15:35:44.184703+00:00',

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

15/121

1/11/25, 3:43 PM

SDK (Python)

'parent_config':

{

}

}

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-d80d-6fa7-8000-9300467fad0f'

meth   update_state(thread_id: str, values: Optional[Union[dict,
Sequence[dict]]], *, as_node: Optional[str] = None, checkpoint:

Optional[Checkpoint] = None, checkpoint_id: Optional[str] = None) ->

ThreadUpdateStateResponse

Update the state of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to update.

values  ( Optional[Union[dict, Sequence[dict]]] ) – The values to update the state with.

as_node  ( Optional[str] , default:  None  ) – Update the state as if this node had just

executed.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to update the state

of.

Returns:

ThreadUpdateStateResponse  (  ThreadUpdateStateResponse  ) – Response after updating a

thread's state.

Example Usage:

response = await client.threads.update_state(

thread_id="my_thread_id",
values={"messages":[{"role": "user", "content": "hello!"}]},
as_node="my_node",

)
print(response)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
----

{

'checkpoint': {

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

16/121

async1/11/25, 3:43 PM

SDK (Python)

'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1',
'checkpoint_map': {}

}

}

meth   get_history(thread_id: str, *, limit: int = 10, before:
Optional[str | Checkpoint] = None, metadata: Optional[dict] = None,

checkpoint: Optional[Checkpoint] = None) -> list[ThreadState]

Get the state history of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to get the state history for.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – Return states for this subgraph. If

empty defaults to root.

limit  ( int , default:  10  ) – The maximum number of states to return.

before  ( Optional[str | Checkpoint] , default:  None  ) – Return states before this

checkpoint.

metadata  ( Optional[dict] , default:  None  ) – Filter states by metadata key-value pairs.

Returns:

list[ThreadState]  – list[ThreadState]: the state history of the thread.

Example Usage:

thread_state = await client.threads.get_history(

thread_id="my_thread_id",
limit=5,

)

class RunsClient

Client for managing runs in LangGraph.

A run is a single assistant invocation with optional input, con g, and metadata. This client

manages runs, which can be stateful (on threads) or stateless.

Example:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

17/121

async1/11/25, 3:43 PM

SDK (Python)

client = get_client()
run = await client.runs.create(assistant_id="asst_123", thread_id="thread_456",
input={"query": "Hello"})

meth   stream(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None,

stream_mode: Union[StreamMode, Sequence[StreamMode]] = 'values',

stream_subgraphs: bool = False, metadata: Optional[dict] = None,

config: Optional[Config] = None, checkpoint: Optional[Checkpoint] =

None, checkpoint_id: Optional[str] = None, interrupt_before:

Optional[Union[All, Sequence[str]]] = None, interrupt_after:

Optional[Union[All, Sequence[str]]] = None, feedback_keys:

Optional[Sequence[str]] = None, on_disconnect:

Optional[DisconnectMode] = None, on_completion:

Optional[OnCompletionBehavior] = None, webhook: Optional[str] = None,

multitask_strategy: Optional[MultitaskStrategy] = None,

if_not_exists: Optional[IfNotExists] = None, after_seconds:

Optional[int] = None) -> AsyncIterator[StreamPart]

Create a run and stream the results.

Parameters:

thread_id  ( Optional[str] ) – the thread ID to assign to the thread. If None will create a

stateless run.

assistant_id  ( str ) – The assistant ID or graph name to stream from. If using graph name,

will default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – A command to execute. Cannot be

combined with input.

stream_mode  ( Union[StreamMode, Sequence[StreamMode]] , default:  'values'  ) – The

stream mode(s) to use.

stream_subgraphs  ( bool , default:  False  ) – Whether to stream output from subgraphs.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

18/121

1/11/25, 3:43 PM

SDK (Python)

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

feedback_keys  ( Optional[Sequence[str]] , default:  None  ) – Feedback keys to assign to

run.

on_disconnect  ( Optional[DisconnectMode] , default:  None  ) – The disconnect mode to use.

Must be one of 'cancel' or 'continue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

AsyncIterator[StreamPart]  – AsyncIterator[StreamPart]: Asynchronous iterator of stream

results.

Example Usage:

async for chunk in client.runs.stream(

thread_id=None,
assistant_id="agent",
input={"messages": [{"role": "user", "content": "how are you?"}]},
stream_mode=["values","debug"],
metadata={"name":"my_run"},
config={"configurable": {"model_name": "anthropic"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
feedback_keys=["my_feedback_key_1","my_feedback_key_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

):

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

19/121

1/11/25, 3:43 PM

SDK (Python)

print(chunk)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
------------------------------------------------------------------------------

StreamPart(event='metadata', data={'run_id': '1ef4a9b8-d7da-679a-a45a-
872054341df2'})
StreamPart(event='values', data={'messages': [{'content': 'how are you?',
'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}]})
StreamPart(event='values', data={'messages': [{'content': 'how are you?',
'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}, {'content': "I'm
doing well, thanks for asking! I'm an AI assistant created by Anthropic to be
helpful, honest, and harmless.", 'additional_kwargs': {}, 'response_metadata':
{}, 'type': 'ai', 'name': None, 'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata':
None}]})
StreamPart(event='end', data=None)

meth   create(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None,

stream_mode: Union[StreamMode, Sequence[StreamMode]] = 'values',

stream_subgraphs: bool = False, metadata: Optional[dict] = None,

config: Optional[Config] = None, checkpoint: Optional[Checkpoint] =

None, checkpoint_id: Optional[str] = None, interrupt_before:

Optional[Union[All, Sequence[str]]] = None, interrupt_after:

Optional[Union[All, Sequence[str]]] = None, webhook: Optional[str] =

None, multitask_strategy: Optional[MultitaskStrategy] = None,

if_not_exists: Optional[IfNotExists] = None, on_completion:

Optional[OnCompletionBehavior] = None, after_seconds: Optional[int] =

None) -> Run

Create a background run.

Parameters:

thread_id  ( Optional[str] ) – the thread ID to assign to the thread. If None will create a

stateless run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

20/121

async1/11/25, 3:43 PM

SDK (Python)

assistant_id  ( str ) – The assistant ID or graph name to stream from. If using graph name,

will default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – A command to execute. Cannot be

combined with input.

stream_mode  ( Union[StreamMode, Sequence[StreamMode]] , default:  'values'  ) – The

stream mode(s) to use.

stream_subgraphs  ( bool , default:  False  ) – Whether to stream output from subgraphs.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

Run  (  Run  ) – The created background run.

Example Usage:

background_run = await client.runs.create(

thread_id="my_thread_id",
assistant_id="my_assistant_id",
input={"messages": [{"role": "user", "content": "hello!"}]},

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

21/121

1/11/25, 3:43 PM

SDK (Python)

metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)
print(background_run)

--------------------------------------------------------------------------------

{

'run_id': 'my_run_id',
'thread_id': 'my_thread_id',
'assistant_id': 'my_assistant_id',
'created_at': '2024-07-25T15:35:42.598503+00:00',
'updated_at': '2024-07-25T15:35:42.598503+00:00',
'metadata': {},
'status': 'pending',
'kwargs':
{

'input':
{

'messages': [

{

}

'role': 'user',
'content': 'how are you?'

]

},
'config':
{

'metadata':

{

},

'created_by': 'system'

'configurable':

{

}

'run_id': 'my_run_id',
'user_id': None,
'graph_id': 'agent',
'thread_id': 'my_thread_id',
'checkpoint_id': None,
'model_name': "openai",
'assistant_id': 'my_assistant_id'

},

'webhook': "https://my.fake.webhook.com",
'temporary': False,
'stream_mode': ['values'],
'feedback_keys': None,
'interrupt_after': ["node_to_stop_after_1","node_to_stop_after_2"],
'interrupt_before': ["node_to_stop_before_1","node_to_stop_before_2"]

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

22/121

1/11/25, 3:43 PM

SDK (Python)

},

'multitask_strategy': 'interrupt'

}

meth   create_batch(payloads: list[RunCreate]) -> list[Run]

Create a batch of stateless background runs.

meth   wait(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None, metadata:

Optional[dict] = None, config: Optional[Config] = None, checkpoint:

Optional[Checkpoint] = None, checkpoint_id: Optional[str] = None,

interrupt_before: Optional[Union[All, Sequence[str]]] = None,

interrupt_after: Optional[Union[All, Sequence[str]]] = None, webhook:

Optional[str] = None, on_disconnect: Optional[DisconnectMode] = None,

on_completion: Optional[OnCompletionBehavior] = None,

multitask_strategy: Optional[MultitaskStrategy] = None,

if_not_exists: Optional[IfNotExists] = None, after_seconds:

Optional[int] = None, raise_error: bool = True) -> Union[list[dict],

dict[str, Any]]

Create a run, wait until it  nishes and return the  nal state.

Parameters:

thread_id  ( Optional[str] ) – the thread ID to create the run on. If None will create a

stateless run.

assistant_id  ( str ) – The assistant ID or graph name to run. If using graph name, will

default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – A command to execute. Cannot be

combined with input.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

23/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

on_disconnect  ( Optional[DisconnectMode] , default:  None  ) – The disconnect mode to use.

Must be one of 'cancel' or 'continue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

Union[list[dict], dict[str, Any]]  – Union[list[dict], dict[str, Any]]: The output of the run.

Example Usage:

final_state_of_run = await client.runs.wait(

thread_id=None,
assistant_id="agent",
input={"messages": [{"role": "user", "content": "how are you?"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "anthropic"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)
print(final_state_of_run)

---------------------------------------------------------------------------------
----------------------------------------------------------

{

'messages': [

{

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

24/121

1/11/25, 3:43 PM

SDK (Python)

'content': 'how are you?',
'additional_kwargs': {},
'response_metadata': {},
'type': 'human',
'name': None,
'id': 'f51a862c-62fe-4866-863b-b0863e8ad78a',
'example': False

},
{

'content': "I'm doing well, thanks for asking! I'm an AI assistant

created by Anthropic to be helpful, honest, and harmless.",

'additional_kwargs': {},
'response_metadata': {},
'type': 'ai',
'name': None,
'id': 'run-bf1cd3c6-768f-4c16-b62d-ba6f17ad8b36',
'example': False,
'tool_calls': [],
'invalid_tool_calls': [],
'usage_metadata': None

}

]

}

meth   list(thread_id: str, *, limit: int = 10, offset: int = 0,
status: Optional[RunStatus] = None) -> List[Run]

List runs.

Parameters:

thread_id  ( str ) – The thread ID to list runs for.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

status  ( Optional[RunStatus] , default:  None  ) – The status of the run to  lter by.

Returns:

List[Run]  – List[Run]: The runs for the thread.

Example Usage:

await client.runs.delete(

thread_id="thread_id_to_delete",
limit=5,

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

25/121

async1/11/25, 3:43 PM

SDK (Python)

offset=5,

)

meth   get(thread_id: str, run_id: str) -> Run

Get a run.

Parameters:

thread_id  ( str ) – The thread ID to get.

run_id  ( str ) – The run ID to get.

Returns:

Run  (  Run  ) – Run object.

Example Usage:

run = await client.runs.get(

thread_id="thread_id_to_delete",
run_id="run_id_to_delete",

)

meth   cancel(thread_id: str, run_id: str, *, wait: bool = False,
action: CancelAction = 'interrupt') -> None

Get a run.

Parameters:

thread_id  ( str ) – The thread ID to cancel.

run_id  ( str ) – The run ID to cancel.

wait  ( bool , default:  False  ) – Whether to wait until run has completed.

action  ( CancelAction , default:  'interrupt'  ) – Action to take when cancelling the run.

Possible values are  interrupt  or  rollback . Default is  interrupt .

Returns:

None  – None

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

26/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

await client.runs.cancel(

thread_id="thread_id_to_cancel",
run_id="run_id_to_cancel",
wait=True,
action="interrupt"

)

meth   join(thread_id: str, run_id: str) -> dict

Block until a run is done. Returns the  nal state of the thread.

Parameters:

thread_id  ( str ) – The thread ID to join.

run_id  ( str ) – The run ID to join.

Returns:

dict  – None

Example Usage:

result =await client.runs.join(

thread_id="thread_id_to_join",
run_id="run_id_to_join"

)

meth   join_stream(thread_id: str, run_id: str, *,
cancel_on_disconnect: bool = False) -> AsyncIterator[StreamPart]

Stream output from a run in real-time, until the run is done. Output is not buffered, so any

output produced before this call will not be received here.

Parameters:

thread_id  ( str ) – The thread ID to join.

run_id  ( str ) – The run ID to join.

cancel_on_disconnect  ( bool , default:  False  ) – Whether to cancel the run when the

stream is disconnected.

Returns:

AsyncIterator[StreamPart]  – None

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

27/121

async1/11/25, 3:43 PM

SDK (Python)

Example Usage:

await client.runs.join_stream(

thread_id="thread_id_to_join",
run_id="run_id_to_join"

)

meth   delete(thread_id: str, run_id: str) -> None

Delete a run.

Parameters:

thread_id  ( str ) – The thread ID to delete.

run_id  ( str ) – The run ID to delete.

Returns:

None  – None

Example Usage:

await client.runs.delete(

thread_id="thread_id_to_delete",
run_id="run_id_to_delete"

)

class CronClient

Client for managing recurrent runs (cron jobs) in LangGraph.

A run is a single invocation of an assistant with optional input and con g. This client allows

scheduling recurring runs to occur automatically.

Example:

client = get_client()
cron_job = await client.crons.create_for_thread(

thread_id="thread_123",
assistant_id="asst_456",
schedule="0 9 * * *",
input={"message": "Daily update"}

)

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

28/121

async1/11/25, 3:43 PM

SDK (Python)

meth   create_for_thread(thread_id: str, assistant_id: str, *,
schedule: str, input: Optional[dict] = None, metadata: Optional[dict]

= None, config: Optional[Config] = None, interrupt_before:

Optional[Union[All, list[str]]] = None, interrupt_after:

Optional[Union[All, list[str]]] = None, webhook: Optional[str] =

None, multitask_strategy: Optional[str] = None) -> Run

Create a cron job for a thread.

Parameters:

thread_id  ( str ) – the thread ID to run the cron job on.

assistant_id  ( str ) – The assistant ID or graph name to use for the cron job. If using graph

name, will default to  rst assistant created from that graph.

schedule  ( str ) – The cron schedule to execute this job on.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the cron job runs.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

interrupt_before  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to Nodes to

interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[str] , default:  None  ) – Multitask strategy to use. Must be

one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

Returns:

Run  (  Run  ) – The cron run.

Example Usage:

cron_run = await client.crons.create_for_thread(

thread_id="my-thread-id",
assistant_id="agent",
schedule="27 15 * * *",
input={"messages": [{"role": "user", "content": "hello!"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

29/121

async1/11/25, 3:43 PM

SDK (Python)

interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)

meth   create(assistant_id: str, *, schedule: str, input:
Optional[dict] = None, metadata: Optional[dict] = None, config:

Optional[Config] = None, interrupt_before: Optional[Union[All,

list[str]]] = None, interrupt_after: Optional[Union[All, list[str]]]

= None, webhook: Optional[str] = None, multitask_strategy:

Optional[str] = None) -> Run

Create a cron run.

Parameters:

assistant_id  ( str ) – The assistant ID or graph name to use for the cron job. If using graph

name, will default to  rst assistant created from that graph.

schedule  ( str ) – The cron schedule to execute this job on.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the cron job runs.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

interrupt_before  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to Nodes to

interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[str] , default:  None  ) – Multitask strategy to use. Must be

one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

Returns:

Run  (  Run  ) – The cron run.

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

30/121

async1/11/25, 3:43 PM

SDK (Python)

cron_run = client.crons.create(

assistant_id="agent",
schedule="27 15 * * *",
input={"messages": [{"role": "user", "content": "hello!"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)

meth   delete(cron_id: str) -> None

Delete a cron.

Parameters:

cron_id  ( str ) – The cron ID to delete.

Returns:

None  – None

Example Usage:

await client.crons.delete(

cron_id="cron_to_delete"

)

meth   search(*, assistant_id: Optional[str] = None, thread_id:
Optional[str] = None, limit: int = 10, offset: int = 0) -> list[Cron]

Get a list of cron jobs.

Parameters:

assistant_id  ( Optional[str] , default:  None  ) – The assistant ID or graph name to search

for.

thread_id  ( Optional[str] , default:  None  ) – the thread ID to search for.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

31/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

Returns:

list[Cron]  – list[Cron]: The list of cron jobs returned by the search,

Example Usage:

cron_jobs = await client.crons.search(
assistant_id="my_assistant_id",
thread_id="my_thread_id",
limit=5,
offset=5,

)
print(cron_jobs)

----------------------------------------------------------

[

{

}

]

'cron_id': '1ef3cefa-4c09-6926-96d0-3dc97fd5e39b',
'assistant_id': 'my_assistant_id',
'thread_id': 'my_thread_id',
'user_id': None,
'payload':
{

'input': {'start_time': ''},
'schedule': '4 * * * *',
'assistant_id': 'my_assistant_id'

},

'schedule': '4 * * * *',
'next_run_date': '2024-07-25T17:04:00+00:00',
'end_time': None,
'created_at': '2024-07-08T06:02:23.073257+00:00',
'updated_at': '2024-07-08T06:02:23.073257+00:00'

class StoreClient

Client for interacting with the graph's shared storage.

The Store provides a key-value storage system for persisting data across graph executions,

allowing for stateful operations and data sharing across threads.

Example:

client = get_client()
await client.store.put_item(["users", "user123"], "mem-123451342", {"name":
"Alice", "score": 100})

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

32/121

1/11/25, 3:43 PM

SDK (Python)

meth   put_item(namespace: Sequence[str], /, key: str, value: dict[str,
Any], index: Optional[Union[Literal[False], list[str]]] = None) ->

None

Store or update an item.

Parameters:

namespace  ( Sequence[str] ) – A list of strings representing the namespace path.

key  ( str ) – The unique identi er for the item within the namespace.

value  ( dict[str, Any] ) – A dictionary containing the item's data.

index  ( Optional[Union[Literal[False], list[str]]] , default:  None  ) – Controls search

indexing - None (use defaults), False (disable), or list of  eld paths to index.

Returns:

None  – None

Example Usage:

await client.store.put_item(

["documents", "user123"],
key="item456",
value={"title": "My Document", "content": "Hello World"}

)

meth   get_item(namespace: Sequence[str], /, key: str) -> Item

Retrieve a single item.

Parameters:

key  ( str ) – The unique identi er for the item.

namespace  ( Sequence[str] ) – Optional list of strings representing the namespace path.

Returns:

Item  (  Item  ) – The retrieved item.

Example Usage:

item = await client.store.get_item(

["documents", "user123"],

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

33/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

key="item456",

)
print(item)

----------------------------------------------------------------

{

}

'namespace': ['documents', 'user123'],
'key': 'item456',
'value': {'title': 'My Document', 'content': 'Hello World'},
'created_at': '2024-07-30T12:00:00Z',
'updated_at': '2024-07-30T12:00:00Z'

meth   delete_item(namespace: Sequence[str], /, key: str) -> None

Delete an item.

Parameters:

key  ( str ) – The unique identi er for the item.

namespace  ( Sequence[str] ) – Optional list of strings representing the namespace path.

Returns:

None  – None

Example Usage:

await client.store.delete_item(

["documents", "user123"],
key="item456",

)

meth   search_items(namespace_prefix: Sequence[str], /, filter:
Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0,

query: Optional[str] = None) -> SearchItemsResponse

Search for items within a namespace pre x.

Parameters:

namespace_prefix  ( Sequence[str] ) – List of strings representing the namespace pre x.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

34/121

asyncasync1/11/25, 3:43 PM

SDK (Python)

filter  ( Optional[dict[str, Any]] , default:  None  ) – Optional dictionary of key-value

pairs to  lter results.

limit  ( int , default:  10  ) – Maximum number of items to return (default is 10).

offset  ( int , default:  0  ) – Number of items to skip before returning results (default is 0).

query  ( Optional[str] , default:  None  ) – Optional query for natural language search.

Returns:

SearchItemsResponse  – List[Item]: A list of items matching the search criteria.

Example Usage:

items = await client.store.search_items(

["documents"],
filter={"author": "John Doe"},
limit=5,
offset=0

)
print(items)

----------------------------------------------------------------

{

"items": [
{

"namespace": ["documents", "user123"],
"key": "item789",
"value": {

"title": "Another Document",
"author": "John Doe"

},
"created_at": "2024-07-30T12:00:00Z",
"updated_at": "2024-07-30T12:00:00Z"

},
# ... additional items ...

]

}

meth   list_namespaces(prefix: Optional[List[str]] = None, suffix:
Optional[List[str]] = None, max_depth: Optional[int] = None, limit:

int = 100, offset: int = 0) -> ListNamespaceResponse

List namespaces with optional match conditions.

Parameters:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

35/121

async1/11/25, 3:43 PM

SDK (Python)

prefix  ( Optional[List[str]] , default:  None  ) – Optional list of strings representing the

pre x to  lter namespaces.

suffix  ( Optional[List[str]] , default:  None  ) – Optional list of strings representing the

suf x to  lter namespaces.

max_depth  ( Optional[int] , default:  None  ) – Optional integer specifying the maximum

depth of namespaces to return.

limit  ( int , default:  100  ) – Maximum number of namespaces to return (default is 100).

offset  ( int , default:  0  ) – Number of namespaces to skip before returning results

(default is 0).

Returns:

ListNamespaceResponse  – List[List[str]]: A list of namespaces matching the criteria.

Example Usage:

namespaces = await client.store.list_namespaces(

prefix=["documents"],
max_depth=3,
limit=10,
offset=0

)
print(namespaces)

----------------------------------------------------------------

[

]

["documents", "user123", "reports"],
["documents", "user456", "invoices"],
...

class SyncLangGraphClient

Synchronous client for interacting with the LangGraph API.

This class provides synchronous access to LangGraph API endpoints for managing assistants,

threads, runs, cron jobs, and data storage.

Example:

client = get_sync_client()
assistant = client.assistants.get("asst_123")

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

36/121

1/11/25, 3:43 PM

SDK (Python)

class SyncHttpClient

meth   get(path: str, *, params: Optional[QueryParamTypes] = None) ->
Any

Send a GET request.

meth   post(path: str, *, json: Optional[dict]) -> Any

Send a POST request.

meth   put(path: str, *, json: dict) -> Any

Send a PUT request.

meth   patch(path: str, *, json: dict) -> Any

Send a PATCH request.

meth   delete(path: str, *, json: Optional[Any] = None) -> None

Send a DELETE request.

meth   stream(path: str, method: str, *, json: Optional[dict] = None,
params: Optional[QueryParamTypes] = None) -> Iterator[StreamPart]

Stream the results of a request using SSE.

class SyncAssistantsClient

Client for managing assistants in LangGraph synchronously.

This class provides methods to interact with assistants, which are versioned con gurations of

your graph.

Example:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

37/121

1/11/25, 3:43 PM

SDK (Python)

client = get_client()
assistant = client.assistants.get("assistant_id_123")

meth   get(assistant_id: str) -> Assistant

Get an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get.

Returns:

Assistant  (  Assistant  ) – Assistant Object.

Example Usage:

assistant = client.assistants.get(
assistant_id="my_assistant_id"

)
print(assistant)

----------------------------------------------------

{

}

'assistant_id': 'my_assistant_id',
'graph_id': 'agent',
'created_at': '2024-06-25T17:10:33.109781+00:00',
'updated_at': '2024-06-25T17:10:33.109781+00:00',
'config': {},
'metadata': {'created_by': 'system'}

meth   get_graph(assistant_id: str, *, xray: Union[int, bool] = False)
-> dict[str, list[dict[str, Any]]]

Get the graph of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the graph of.

xray  ( Union[int, bool] , default:  False  ) – Include graph representation of subgraphs. If

an integer value is provided, only subgraphs with a depth less than or equal to the value

will be included.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

38/121

1/11/25, 3:43 PM

SDK (Python)

Returns:

Graph  (  dict[str, list[dict[str, Any]]]  ) – The graph information for the assistant in

JSON format.

Example Usage:

graph_info = client.assistants.get_graph(

assistant_id="my_assistant_id"

)
print(graph_info)

---------------------------------------------------------------------------------
-----------------------------------------

{

'nodes':
[

{'id': '__start__', 'type': 'schema', 'data': '__start__'},
{'id': '__end__', 'type': 'schema', 'data': '__end__'},
{'id': 'agent','type': 'runnable','data': {'id': ['langgraph',

'utils', 'RunnableCallable'],'name': 'agent'}},

],

'edges':
[

]

}

{'source': '__start__', 'target': 'agent'},
{'source': 'agent','target': '__end__'}

meth   get_schemas(assistant_id: str) -> GraphSchema

Get the schemas of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the schema of.

Returns:

GraphSchema  (  GraphSchema  ) – The graph schema for the assistant.

Example Usage:

schema = client.assistants.get_schemas(
assistant_id="my_assistant_id"

)
print(schema)

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

39/121

1/11/25, 3:43 PM

SDK (Python)

---------------------------------------------------------------------------------
-------------------------------------------

{

'graph_id': 'agent',
'state_schema':

{

'title': 'LangGraphInput',
'$ref': '#/definitions/AgentState',
'definitions':

{

'BaseMessage':

{

are the inputs and outputs of ChatModels.',

'title': 'BaseMessage',
'description': 'Base abstract Message class. Messages

'type': 'object',
'properties':

{

'content':

{

[{'type': 'string'}, {'type': 'object'}]}}

'title': 'Content',
'anyOf': [

{'type': 'string'},
{'type': 'array','items': {'anyOf':

]

},

'additional_kwargs':

{

},

'title': 'Additional Kwargs',
'type': 'object'

'response_metadata':

{

},

'type':

{

},

'name':

{

},

'id':
{

'title': 'Response Metadata',
'type': 'object'

'title': 'Type',
'type': 'string'

'title': 'Name',
'type': 'string'

'title': 'Id',
'type': 'string'

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

40/121

1/11/25, 3:43 PM

SDK (Python)

}

},

'required': ['content', 'type']

},

'AgentState':

{

'title': 'AgentState',
'type': 'object',
'properties':

'#/definitions/BaseMessage'}

{

},

'messages':

'title': 'Messages',
'type': 'array',
'items': {'$ref':

{

}

'required': ['messages']

}

}

},

'config_schema':

{

}

}

'title': 'Configurable',
'type': 'object',
'properties':

{

}

'model_name':

{

}

'title': 'Model Name',
'enum': ['anthropic', 'openai'],
'type': 'string'

meth   get_subgraphs(assistant_id: str, namespace: Optional[str] =
None, recurse: bool = False) -> Subgraphs

Get the schemas of an assistant by ID.

Parameters:

assistant_id  ( str ) – The ID of the assistant to get the schema of.

Returns:

Subgraphs  (  Subgraphs  ) – The graph schema for the assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

41/121

1/11/25, 3:43 PM

SDK (Python)

meth   create(graph_id: Optional[str], config: Optional[Config] = None,
*, metadata: Json = None, assistant_id: Optional[str] = None,

if_exists: Optional[OnConflictBehavior] = None, name: Optional[str] =

None) -> Assistant

Create a new assistant.

Useful when graph is con gurable and you want to create different assistants based on

different con gurations.

Parameters:

graph_id  ( Optional[str] ) – The ID of the graph the assistant should use. The graph ID is

normally set in your langgraph.json con guration.

config  ( Optional[Config] , default:  None  ) – Con guration to use for the graph.

metadata  ( Json , default:  None  ) – Metadata to add to assistant.

assistant_id  ( Optional[str] , default:  None  ) – Assistant ID to use, will default to a

random UUID if not provided.

if_exists  ( Optional[OnConflictBehavior] , default:  None  ) – How to handle duplicate

creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate),

or 'do_nothing' (return existing assistant).

name  ( Optional[str] , default:  None  ) – The name of the assistant. Defaults to 'Untitled'

under the hood.

Returns:

Assistant  (  Assistant  ) – The created assistant.

Example Usage:

assistant = client.assistants.create(

graph_id="agent",
config={"configurable": {"model_name": "openai"}},
metadata={"number":1},
assistant_id="my-assistant-id",
if_exists="do_nothing",
name="my_name"

)

meth   update(assistant_id: str, *, graph_id: Optional[str] = None,
config: Optional[Config] = None, metadata: Json = None, name:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

42/121

1/11/25, 3:43 PM

SDK (Python)

Optional[str] = None) -> Assistant

Update an assistant.

Use this to point to a different graph, update the con guration, or change the metadata of an

assistant.

Parameters:

assistant_id  ( str ) – Assistant to update.

graph_id  ( Optional[str] , default:  None  ) – The ID of the graph the assistant should use.

The graph ID is normally set in your langgraph.json con guration. If None, assistant will

keep pointing to same graph.

config  ( Optional[Config] , default:  None  ) – Con guration to use for the graph.

metadata  ( Json , default:  None  ) – Metadata to merge with existing assistant metadata.

name  ( Optional[str] , default:  None  ) – The new name for the assistant.

Returns:

Assistant  (  Assistant  ) – The updated assistant.

Example Usage:

assistant = client.assistants.update(

assistant_id='e280dad7-8618-443f-87f1-8e41841c180f',
graph_id="other-graph",
config={"configurable": {"model_name": "anthropic"}},
metadata={"number":2}

)

meth   delete(assistant_id: str) -> None

Delete an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to delete.

Returns:

None  – None

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

43/121

1/11/25, 3:43 PM

SDK (Python)

client.assistants.delete(

assistant_id="my_assistant_id"

)

meth   search(*, metadata: Json = None, graph_id: Optional[str] = None,
limit: int = 10, offset: int = 0) -> list[Assistant]

Search for assistants.

Parameters:

metadata  ( Json , default:  None  ) – Metadata to  lter by. Exact match  lter for each KV pair.

graph_id  ( Optional[str] , default:  None  ) – The ID of the graph to  lter by. The graph ID is

normally set in your langgraph.json con guration.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

Returns:

list[Assistant]  – list[Assistant]: A list of assistants.

Example Usage:

assistants = client.assistants.search(
metadata = {"name":"my_name"},
graph_id="my_graph_id",
limit=5,
offset=5

)

meth   get_versions(assistant_id: str, metadata: Json = None, limit:
int = 10, offset: int = 0) -> list[AssistantVersion]

List all versions of an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to get versions for.

metadata  ( Json , default:  None  ) – Metadata to  lter versions by. Exact match  lter for

each KV pair.

limit  ( int , default:  10  ) – The maximum number of versions to return.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

44/121

1/11/25, 3:43 PM

SDK (Python)

offset  ( int , default:  0  ) – The number of versions to skip.

Returns:

list[AssistantVersion]  – list[Assistant]: A list of assistants.

Example Usage:

assistant_versions = await client.assistants.get_versions(

assistant_id="my_assistant_id"

)

meth   set_latest(assistant_id: str, version: int) -> Assistant

Change the version of an assistant.

Parameters:

assistant_id  ( str ) – The assistant ID to delete.

version  ( int ) – The version to change to.

Returns:

Assistant  (  Assistant  ) – Assistant Object.

Example Usage:

new_version_assistant = await client.assistants.set_latest(

assistant_id="my_assistant_id",
version=3

)

class SyncThreadsClient

Synchronous client for managing threads in LangGraph.

This class provides methods to create, retrieve, and manage threads, which represent

conversations or stateful interactions.

Example:

client = get_sync_client()
thread = client.threads.create(metadata={"user_id": "123"})

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

45/121

1/11/25, 3:43 PM

SDK (Python)

meth   get(thread_id: str) -> Thread

Get a thread by ID.

Parameters:

thread_id  ( str ) – The ID of the thread to get.

Returns:

Thread  (  Thread  ) – Thread object.

Example Usage:

thread = client.threads.get(
thread_id="my_thread_id"

)
print(thread)

-----------------------------------------------------

{

}

'thread_id': 'my_thread_id',
'created_at': '2024-07-18T18:35:15.540834+00:00',
'updated_at': '2024-07-18T18:35:15.540834+00:00',
'metadata': {'graph_id': 'agent'}

meth   create(*, metadata: Json = None, thread_id: Optional[str] =
None, if_exists: Optional[OnConflictBehavior] = None) -> Thread

Create a new thread.

Parameters:

metadata  ( Json , default:  None  ) – Metadata to add to thread.

thread_id  ( Optional[str] , default:  None  ) – ID of thread. If None, ID will be a randomly

generated UUID.

if_exists  ( Optional[OnConflictBehavior] , default:  None  ) – How to handle duplicate

creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate),

or 'do_nothing' (return existing thread).

Returns:

Thread  (  Thread  ) – The created thread.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

46/121

1/11/25, 3:43 PM

SDK (Python)

Example Usage:

thread = client.threads.create(
metadata={"number":1},
thread_id="my-thread-id",
if_exists="raise"

)

meth   update(thread_id: str, *, metadata: dict[str, Any]) -> Thread

Update a thread.

Parameters:

thread_id  ( str ) – ID of thread to update.

metadata  ( dict[str, Any] ) – Metadata to merge with existing thread metadata.

Returns:

Thread  (  Thread  ) – The created thread.

Example Usage:

thread = client.threads.update(

thread_id="my-thread-id",
metadata={"number":1},

)

meth   delete(thread_id: str) -> None

Delete a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to delete.

Returns:

None  – None

Example Usage:

client.threads.delete(

thread_id="my_thread_id"

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

47/121

1/11/25, 3:43 PM

SDK (Python)

)

meth   search(*, metadata: Json = None, values: Json = None, status:
Optional[ThreadStatus] = None, limit: int = 10, offset: int = 0) ->

list[Thread]

Search for threads.

Parameters:

metadata  ( Json , default:  None  ) – Thread metadata to  lter on.

values  ( Json , default:  None  ) – State values to  lter on.

status  ( Optional[ThreadStatus] , default:  None  ) – Thread status to  lter on. Must be one

of 'idle', 'busy', 'interrupted' or 'error'.

limit  ( int , default:  10  ) – Limit on number of threads to return.

offset  ( int , default:  0  ) – Offset in threads table to start search from.

Returns:

list[Thread]  – list[Thread]: List of the threads matching the search parameters.

Example Usage:

threads = client.threads.search(

metadata={"number":1},
status="interrupted",
limit=15,
offset=5

)

meth   copy(thread_id: str) -> None

Copy a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to copy.

Returns:

None  – None

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

48/121

1/11/25, 3:43 PM

SDK (Python)

Example Usage:

client.threads.copy(

thread_id="my_thread_id"

)

meth   get_state(thread_id: str, checkpoint: Optional[Checkpoint] =
None, checkpoint_id: Optional[str] = None, *, subgraphs: bool =

False) -> ThreadState

Get the state of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to get the state of.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to get the state of.

subgraphs  ( bool , default:  False  ) – Include subgraphs states.

Returns:

ThreadState  (  ThreadState  ) – the thread of the state.

Example Usage:

thread_state = client.threads.get_state(

thread_id="my_thread_id",
checkpoint_id="my_checkpoint_id"

)
print(thread_state)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
----

{

'values': {

'messages': [

{

},

'content': 'how are you?',
'additional_kwargs': {},
'response_metadata': {},
'type': 'human',
'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10',
'example': False

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

49/121

1/11/25, 3:43 PM

SDK (Python)

{

assistant created by Anthropic to be helpful, honest, and harmless.",

'content': "I'm doing well, thanks for asking! I'm an AI

'additional_kwargs': {},
'response_metadata': {},
'type': 'ai',
'name': None,
'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
'example': False,
'tool_calls': [],
'invalid_tool_calls': [],
'usage_metadata': None

}

]

},
'next': [],
'checkpoint':

{

}

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1'

'metadata':

{

'step': 1,
'run_id': '1ef4a9b8-d7da-679a-a45a-872054341df2',
'source': 'loop',
'writes':
{

'agent':
{

'messages': [

{

cef87798fe8b',

'id': 'run-159b782c-b679-4830-83c6-

'name': None,
'type': 'ai',
'content': "I'm doing well, thanks for

asking! I'm an AI assistant created by Anthropic to be helpful, honest, and
harmless.",

'example': False,
'tool_calls': [],
'usage_metadata': None,
'additional_kwargs': {},
'response_metadata': {},
'invalid_tool_calls': []

}

]

}

},

'user_id': None,
'graph_id': 'agent',
'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

50/121

1/11/25, 3:43 PM

SDK (Python)

'created_by': 'system',
'assistant_id': 'fe096781-5601-53d2-b2f6-0d3403f7e9ca'},
'created_at': '2024-07-25T15:35:44.184703+00:00',
'parent_config':

{

}

}

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-d80d-6fa7-8000-9300467fad0f'

meth   update_state(thread_id: str, values: Optional[Union[dict,
Sequence[dict]]], *, as_node: Optional[str] = None, checkpoint:

Optional[Checkpoint] = None, checkpoint_id: Optional[str] = None) ->

ThreadUpdateStateResponse

Update the state of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to update.

values  ( Optional[Union[dict, Sequence[dict]]] ) – The values to update the state with.

as_node  ( Optional[str] , default:  None  ) – Update the state as if this node had just

executed.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to update the state

of.

Returns:

ThreadUpdateStateResponse  (  ThreadUpdateStateResponse  ) – Response after updating a

thread's state.

Example Usage:

response = client.threads.update_state(

thread_id="my_thread_id",
values={"messages":[{"role": "user", "content": "hello!"}]},
as_node="my_node",

)
print(response)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
----

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

51/121

1/11/25, 3:43 PM

SDK (Python)

{

}

'checkpoint': {

'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
'checkpoint_ns': '',
'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1',
'checkpoint_map': {}

}

meth   get_history(thread_id: str, *, limit: int = 10, before:
Optional[str | Checkpoint] = None, metadata: Optional[dict] = None,

checkpoint: Optional[Checkpoint] = None) -> list[ThreadState]

Get the state history of a thread.

Parameters:

thread_id  ( str ) – The ID of the thread to get the state history for.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – Return states for this subgraph. If

empty defaults to root.

limit  ( int , default:  10  ) – The maximum number of states to return.

before  ( Optional[str | Checkpoint] , default:  None  ) – Return states before this

checkpoint.

metadata  ( Optional[dict] , default:  None  ) – Filter states by metadata key-value pairs.

Returns:

list[ThreadState]  – list[ThreadState]: the state history of the thread.

Example Usage:

thread_state = client.threads.get_history(

thread_id="my_thread_id",
limit=5,
before="my_timestamp",
metadata={"name":"my_name"}

)

class SyncRunsClient

Synchronous client for managing runs in LangGraph.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

52/121

1/11/25, 3:43 PM

SDK (Python)

This class provides methods to create, retrieve, and manage runs, which represent individual

executions of graphs.

Example:

client = get_sync_client()
run = client.runs.create(thread_id="thread_123", assistant_id="asst_456")

meth   stream(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None,

stream_mode: Union[StreamMode, Sequence[StreamMode]] = 'values',

stream_subgraphs: bool = False, metadata: Optional[dict] = None,

config: Optional[Config] = None, checkpoint: Optional[Checkpoint] =

None, checkpoint_id: Optional[str] = None, interrupt_before:

Optional[Union[All, Sequence[str]]] = None, interrupt_after:

Optional[Union[All, Sequence[str]]] = None, feedback_keys:

Optional[Sequence[str]] = None, on_disconnect:

Optional[DisconnectMode] = None, on_completion:

Optional[OnCompletionBehavior] = None, webhook: Optional[str] = None,

multitask_strategy: Optional[MultitaskStrategy] = None,

if_not_exists: Optional[IfNotExists] = None, after_seconds:

Optional[int] = None) -> Iterator[StreamPart]

Create a run and stream the results.

Parameters:

thread_id  ( Optional[str] ) – the thread ID to assign to the thread. If None will create a

stateless run.

assistant_id  ( str ) – The assistant ID or graph name to stream from. If using graph name,

will default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – The command to execute.

stream_mode  ( Union[StreamMode, Sequence[StreamMode]] , default:  'values'  ) – The

stream mode(s) to use.

stream_subgraphs  ( bool , default:  False  ) – Whether to stream output from subgraphs.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

53/121

1/11/25, 3:43 PM

SDK (Python)

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

feedback_keys  ( Optional[Sequence[str]] , default:  None  ) – Feedback keys to assign to

run.

on_disconnect  ( Optional[DisconnectMode] , default:  None  ) – The disconnect mode to use.

Must be one of 'cancel' or 'continue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

Iterator[StreamPart]  – Iterator[StreamPart]: Iterator of stream results.

Example Usage:

async for chunk in client.runs.stream(

thread_id=None,
assistant_id="agent",
input={"messages": [{"role": "user", "content": "how are you?"}]},
stream_mode=["values","debug"],
metadata={"name":"my_run"},
config={"configurable": {"model_name": "anthropic"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
feedback_keys=["my_feedback_key_1","my_feedback_key_2"],
webhook="https://my.fake.webhook.com",

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

54/121

1/11/25, 3:43 PM

SDK (Python)

multitask_strategy="interrupt"

):

print(chunk)

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
------------------------------------------------------------------------------

StreamPart(event='metadata', data={'run_id': '1ef4a9b8-d7da-679a-a45a-
872054341df2'})
StreamPart(event='values', data={'messages': [{'content': 'how are you?',
'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}]})
StreamPart(event='values', data={'messages': [{'content': 'how are you?',
'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None,
'id': 'fe0a5778-cfe9-42ee-b807-0adaa1873c10', 'example': False}, {'content': "I'm
doing well, thanks for asking! I'm an AI assistant created by Anthropic to be
helpful, honest, and harmless.", 'additional_kwargs': {}, 'response_metadata':
{}, 'type': 'ai', 'name': None, 'id': 'run-159b782c-b679-4830-83c6-cef87798fe8b',
'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata':
None}]})
StreamPart(event='end', data=None)

meth   create(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None,

stream_mode: Union[StreamMode, Sequence[StreamMode]] = 'values',

stream_subgraphs: bool = False, metadata: Optional[dict] = None,

config: Optional[Config] = None, checkpoint: Optional[Checkpoint] =

None, checkpoint_id: Optional[str] = None, interrupt_before:

Optional[Union[All, Sequence[str]]] = None, interrupt_after:

Optional[Union[All, Sequence[str]]] = None, webhook: Optional[str] =

None, multitask_strategy: Optional[MultitaskStrategy] = None,

on_completion: Optional[OnCompletionBehavior] = None, if_not_exists:

Optional[IfNotExists] = None, after_seconds: Optional[int] = None) ->

Run

Create a background run.

Parameters:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

55/121

1/11/25, 3:43 PM

SDK (Python)

thread_id  ( Optional[str] ) – the thread ID to assign to the thread. If None will create a

stateless run.

assistant_id  ( str ) – The assistant ID or graph name to stream from. If using graph name,

will default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – The command to execute.

stream_mode  ( Union[StreamMode, Sequence[StreamMode]] , default:  'values'  ) – The

stream mode(s) to use.

stream_subgraphs  ( bool , default:  False  ) – Whether to stream output from subgraphs.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

Run  (  Run  ) – The created background run.

Example Usage:

background_run = client.runs.create(

thread_id="my_thread_id",
assistant_id="my_assistant_id",

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

56/121

1/11/25, 3:43 PM

SDK (Python)

input={"messages": [{"role": "user", "content": "hello!"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)
print(background_run)

--------------------------------------------------------------------------------

{

'run_id': 'my_run_id',
'thread_id': 'my_thread_id',
'assistant_id': 'my_assistant_id',
'created_at': '2024-07-25T15:35:42.598503+00:00',
'updated_at': '2024-07-25T15:35:42.598503+00:00',
'metadata': {},
'status': 'pending',
'kwargs':
{

'input':
{

'messages': [

{

}

'role': 'user',
'content': 'how are you?'

]

},
'config':
{

'metadata':

{

},

'created_by': 'system'

'configurable':

{

}

'run_id': 'my_run_id',
'user_id': None,
'graph_id': 'agent',
'thread_id': 'my_thread_id',
'checkpoint_id': None,
'model_name': "openai",
'assistant_id': 'my_assistant_id'

},

'webhook': "https://my.fake.webhook.com",
'temporary': False,
'stream_mode': ['values'],
'feedback_keys': None,
'interrupt_after': ["node_to_stop_after_1","node_to_stop_after_2"],

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

57/121

1/11/25, 3:43 PM

SDK (Python)

'interrupt_before': ["node_to_stop_before_1","node_to_stop_before_2"]

},

'multitask_strategy': 'interrupt'

}

meth   create_batch(payloads: list[RunCreate]) -> list[Run]

Create a batch of stateless background runs.

meth   wait(thread_id: Optional[str], assistant_id: str, *, input:
Optional[dict] = None, command: Optional[Command] = None, metadata:

Optional[dict] = None, config: Optional[Config] = None, checkpoint:

Optional[Checkpoint] = None, checkpoint_id: Optional[str] = None,

interrupt_before: Optional[Union[All, Sequence[str]]] = None,

interrupt_after: Optional[Union[All, Sequence[str]]] = None, webhook:

Optional[str] = None, on_disconnect: Optional[DisconnectMode] = None,

on_completion: Optional[OnCompletionBehavior] = None,

multitask_strategy: Optional[MultitaskStrategy] = None,

if_not_exists: Optional[IfNotExists] = None, after_seconds:

Optional[int] = None) -> Union[list[dict], dict[str, Any]]

Create a run, wait until it  nishes and return the  nal state.

Parameters:

thread_id  ( Optional[str] ) – the thread ID to create the run on. If None will create a

stateless run.

assistant_id  ( str ) – The assistant ID or graph name to run. If using graph name, will

default to  rst assistant created from that graph.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

command  ( Optional[Command] , default:  None  ) – The command to execute.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the run.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

checkpoint  ( Optional[Checkpoint] , default:  None  ) – The checkpoint to resume from.

interrupt_before  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

58/121

1/11/25, 3:43 PM

SDK (Python)

interrupt_after  ( Optional[Union[All, Sequence[str]]] , default:  None  ) – Nodes to

Nodes to interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

on_disconnect  ( Optional[DisconnectMode] , default:  None  ) – The disconnect mode to use.

Must be one of 'cancel' or 'continue'.

on_completion  ( Optional[OnCompletionBehavior] , default:  None  ) – Whether to delete or

keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

multitask_strategy  ( Optional[MultitaskStrategy] , default:  None  ) – Multitask strategy

to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

if_not_exists  ( Optional[IfNotExists] , default:  None  ) – How to handle missing thread.

Defaults to 'reject'. Must be either 'reject' (raise error if missing), or 'create' (create new

thread).

after_seconds  ( Optional[int] , default:  None  ) – The number of seconds to wait before

starting the run. Use to schedule future runs.

Returns:

Union[list[dict], dict[str, Any]]  – Union[list[dict], dict[str, Any]]: The output of the run.

Example Usage:

final_state_of_run = client.runs.wait(

thread_id=None,
assistant_id="agent",
input={"messages": [{"role": "user", "content": "how are you?"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "anthropic"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)
print(final_state_of_run)

---------------------------------------------------------------------------------
----------------------------------------------------------

{

'messages': [

{

'content': 'how are you?',
'additional_kwargs': {},
'response_metadata': {},
'type': 'human',

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

59/121

1/11/25, 3:43 PM

SDK (Python)

'name': None,
'id': 'f51a862c-62fe-4866-863b-b0863e8ad78a',
'example': False

},
{

'content': "I'm doing well, thanks for asking! I'm an AI assistant

created by Anthropic to be helpful, honest, and harmless.",

'additional_kwargs': {},
'response_metadata': {},
'type': 'ai',
'name': None,
'id': 'run-bf1cd3c6-768f-4c16-b62d-ba6f17ad8b36',
'example': False,
'tool_calls': [],
'invalid_tool_calls': [],
'usage_metadata': None

}

]

}

meth   list(thread_id: str, *, limit: int = 10, offset: int = 0) ->
List[Run]

List runs.

Parameters:

thread_id  ( str ) – The thread ID to list runs for.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

Returns:

List[Run]  – List[Run]: The runs for the thread.

Example Usage:

client.runs.delete(

thread_id="thread_id_to_delete",
limit=5,
offset=5,

)

meth   get(thread_id: str, run_id: str) -> Run

Get a run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

60/121

1/11/25, 3:43 PM

SDK (Python)

Parameters:

thread_id  ( str ) – The thread ID to get.

run_id  ( str ) – The run ID to get.

Returns:

Run  (  Run  ) – Run object.

Example Usage:

run = client.runs.get(

thread_id="thread_id_to_delete",
run_id="run_id_to_delete",

)

meth   cancel(thread_id: str, run_id: str, *, wait: bool = False,
action: CancelAction = 'interrupt') -> None

Get a run.

Parameters:

thread_id  ( str ) – The thread ID to cancel.

run_id  ( str ) – The run ID to cancel.

wait  ( bool , default:  False  ) – Whether to wait until run has completed.

action  ( CancelAction , default:  'interrupt'  ) – Action to take when cancelling the run.

Possible values are  interrupt  or  rollback . Default is  interrupt .

Returns:

None  – None

Example Usage:

client.runs.cancel(

thread_id="thread_id_to_cancel",
run_id="run_id_to_cancel",
wait=True,
action="interrupt"

)

meth   join(thread_id: str, run_id: str) -> dict

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

61/121

1/11/25, 3:43 PM

SDK (Python)

Block until a run is done. Returns the  nal state of the thread.

Parameters:

thread_id  ( str ) – The thread ID to join.

run_id  ( str ) – The run ID to join.

Returns:

dict  – None

Example Usage:

client.runs.join(

thread_id="thread_id_to_join",
run_id="run_id_to_join"

)

meth   join_stream(thread_id: str, run_id: str) ->
Iterator[StreamPart]

Stream output from a run in real-time, until the run is done. Output is not buffered, so any

output produced before this call will not be received here.

Parameters:

thread_id  ( str ) – The thread ID to join.

run_id  ( str ) – The run ID to join.

Returns:

Iterator[StreamPart]  – None

Example Usage:

client.runs.join_stream(

thread_id="thread_id_to_join",
run_id="run_id_to_join"

)

meth   delete(thread_id: str, run_id: str) -> None

Delete a run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

62/121

1/11/25, 3:43 PM

SDK (Python)

Parameters:

thread_id  ( str ) – The thread ID to delete.

run_id  ( str ) – The run ID to delete.

Returns:

None  – None

Example Usage:

client.runs.delete(

thread_id="thread_id_to_delete",
run_id="run_id_to_delete"

)

class SyncCronClient

Synchronous client for managing cron jobs in LangGraph.

This class provides methods to create and manage scheduled tasks (cron jobs) for automated

graph executions.

Example:

client = get_sync_client()
cron_job = client.crons.create_for_thread(thread_id="thread_123",
assistant_id="asst_456", schedule="0 * * * *")

meth   create_for_thread(thread_id: str, assistant_id: str, *,
schedule: str, input: Optional[dict] = None, metadata: Optional[dict]

= None, config: Optional[Config] = None, interrupt_before:

Optional[Union[All, list[str]]] = None, interrupt_after:

Optional[Union[All, list[str]]] = None, webhook: Optional[str] =

None, multitask_strategy: Optional[str] = None) -> Run

Create a cron job for a thread.

Parameters:

thread_id  ( str ) – the thread ID to run the cron job on.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

63/121

1/11/25, 3:43 PM

SDK (Python)

assistant_id  ( str ) – The assistant ID or graph name to use for the cron job. If using graph

name, will default to  rst assistant created from that graph.

schedule  ( str ) – The cron schedule to execute this job on.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the cron job runs.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

interrupt_before  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to Nodes to

interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[str] , default:  None  ) – Multitask strategy to use. Must be

one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

Returns:

Run  (  Run  ) – The cron run.

Example Usage:

cron_run = client.crons.create_for_thread(

thread_id="my-thread-id",
assistant_id="agent",
schedule="27 15 * * *",
input={"messages": [{"role": "user", "content": "hello!"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)

meth   create(assistant_id: str, *, schedule: str, input:
Optional[dict] = None, metadata: Optional[dict] = None, config:

Optional[Config] = None, interrupt_before: Optional[Union[All,

list[str]]] = None, interrupt_after: Optional[Union[All, list[str]]]

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

64/121

1/11/25, 3:43 PM

SDK (Python)

= None, webhook: Optional[str] = None, multitask_strategy:

Optional[str] = None) -> Run

Create a cron run.

Parameters:

assistant_id  ( str ) – The assistant ID or graph name to use for the cron job. If using graph

name, will default to  rst assistant created from that graph.

schedule  ( str ) – The cron schedule to execute this job on.

input  ( Optional[dict] , default:  None  ) – The input to the graph.

metadata  ( Optional[dict] , default:  None  ) – Metadata to assign to the cron job runs.

config  ( Optional[Config] , default:  None  ) – The con guration for the assistant.

interrupt_before  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to

interrupt immediately before they get executed.

interrupt_after  ( Optional[Union[All, list[str]]] , default:  None  ) – Nodes to Nodes to

interrupt immediately after they get executed.

webhook  ( Optional[str] , default:  None  ) – Webhook to call after LangGraph API call is

done.

multitask_strategy  ( Optional[str] , default:  None  ) – Multitask strategy to use. Must be

one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

Returns:

Run  (  Run  ) – The cron run.

Example Usage:

cron_run = client.crons.create(

assistant_id="agent",
schedule="27 15 * * *",
input={"messages": [{"role": "user", "content": "hello!"}]},
metadata={"name":"my_run"},
config={"configurable": {"model_name": "openai"}},
interrupt_before=["node_to_stop_before_1","node_to_stop_before_2"],
interrupt_after=["node_to_stop_after_1","node_to_stop_after_2"],
webhook="https://my.fake.webhook.com",
multitask_strategy="interrupt"

)

meth   delete(cron_id: str) -> None

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

65/121

1/11/25, 3:43 PM

SDK (Python)

Delete a cron.

Parameters:

cron_id  ( str ) – The cron ID to delete.

Returns:

None  – None

Example Usage:

client.crons.delete(

cron_id="cron_to_delete"

)

meth   search(*, assistant_id: Optional[str] = None, thread_id:
Optional[str] = None, limit: int = 10, offset: int = 0) -> list[Cron]

Get a list of cron jobs.

Parameters:

assistant_id  ( Optional[str] , default:  None  ) – The assistant ID or graph name to search

for.

thread_id  ( Optional[str] , default:  None  ) – the thread ID to search for.

limit  ( int , default:  10  ) – The maximum number of results to return.

offset  ( int , default:  0  ) – The number of results to skip.

Returns:

list[Cron]  – list[Cron]: The list of cron jobs returned by the search,

Example Usage:

cron_jobs = client.crons.search(

assistant_id="my_assistant_id",
thread_id="my_thread_id",
limit=5,
offset=5,

)
print(cron_jobs)

----------------------------------------------------------

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

66/121

1/11/25, 3:43 PM

SDK (Python)

[

{

}

]

'cron_id': '1ef3cefa-4c09-6926-96d0-3dc97fd5e39b',
'assistant_id': 'my_assistant_id',
'thread_id': 'my_thread_id',
'user_id': None,
'payload':
{

'input': {'start_time': ''},
'schedule': '4 * * * *',
'assistant_id': 'my_assistant_id'

},

'schedule': '4 * * * *',
'next_run_date': '2024-07-25T17:04:00+00:00',
'end_time': None,
'created_at': '2024-07-08T06:02:23.073257+00:00',
'updated_at': '2024-07-08T06:02:23.073257+00:00'

class SyncStoreClient

A client for synchronous operations on a key-value store.

Provides methods to interact with a remote key-value store, allowing storage and retrieval of

items within namespaced hierarchies.

Example:

client = get_sync_client()
client.store.put_item(["users", "profiles"], "user123", {"name": "Alice", "age":
30})

meth   put_item(namespace: Sequence[str], /, key: str, value: dict[str,
Any], index: Optional[Union[Literal[False], list[str]]] = None) ->

None

Store or update an item.

Parameters:

namespace  ( Sequence[str] ) – A list of strings representing the namespace path.

key  ( str ) – The unique identi er for the item within the namespace.

value  ( dict[str, Any] ) – A dictionary containing the item's data.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

67/121

1/11/25, 3:43 PM

SDK (Python)

index  ( Optional[Union[Literal[False], list[str]]] , default:  None  ) – Controls search

indexing - None (use defaults), False (disable), or list of  eld paths to index.

Returns:

None  – None

Example Usage:

client.store.put_item(

["documents", "user123"],
key="item456",
value={"title": "My Document", "content": "Hello World"}

)

meth   get_item(namespace: Sequence[str], /, key: str) -> Item

Retrieve a single item.

Parameters:

key  ( str ) – The unique identi er for the item.

namespace  ( Sequence[str] ) – Optional list of strings representing the namespace path.

Returns:

Item  (  Item  ) – The retrieved item.

Example Usage:

item = client.store.get_item(
["documents", "user123"],
key="item456",

)
print(item)

----------------------------------------------------------------

{

}

'namespace': ['documents', 'user123'],
'key': 'item456',
'value': {'title': 'My Document', 'content': 'Hello World'},
'created_at': '2024-07-30T12:00:00Z',
'updated_at': '2024-07-30T12:00:00Z'

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

68/121

1/11/25, 3:43 PM

SDK (Python)

meth   delete_item(namespace: Sequence[str], /, key: str) -> None

Delete an item.

Parameters:

key  ( str ) – The unique identi er for the item.

namespace  ( Sequence[str] ) – Optional list of strings representing the namespace path.

Returns:

None  – None

Example Usage:

client.store.delete_item(

["documents", "user123"],
key="item456",

)

meth   search_items(namespace_prefix: Sequence[str], /, filter:
Optional[dict[str, Any]] = None, limit: int = 10, offset: int = 0,

query: Optional[str] = None) -> SearchItemsResponse

Search for items within a namespace pre x.

Parameters:

namespace_prefix  ( Sequence[str] ) – List of strings representing the namespace pre x.

filter  ( Optional[dict[str, Any]] , default:  None  ) – Optional dictionary of key-value

pairs to  lter results.

limit  ( int , default:  10  ) – Maximum number of items to return (default is 10).

offset  ( int , default:  0  ) – Number of items to skip before returning results (default is 0).

query  ( Optional[str] , default:  None  ) – Optional query for natural language search.

Returns:

SearchItemsResponse  – List[Item]: A list of items matching the search criteria.

Example Usage:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

69/121

1/11/25, 3:43 PM

SDK (Python)

items = client.store.search_items(

["documents"],
filter={"author": "John Doe"},
limit=5,
offset=0

)
print(items)

----------------------------------------------------------------

{

"items": [
{

"namespace": ["documents", "user123"],
"key": "item789",
"value": {

"title": "Another Document",
"author": "John Doe"

},
"created_at": "2024-07-30T12:00:00Z",
"updated_at": "2024-07-30T12:00:00Z"

},
# ... additional items ...

]

}

meth   list_namespaces(prefix: Optional[List[str]] = None, suffix:
Optional[List[str]] = None, max_depth: Optional[int] = None, limit:

int = 100, offset: int = 0) -> ListNamespaceResponse

List namespaces with optional match conditions.

Parameters:

prefix  ( Optional[List[str]] , default:  None  ) – Optional list of strings representing the

pre x to  lter namespaces.

suffix  ( Optional[List[str]] , default:  None  ) – Optional list of strings representing the

suf x to  lter namespaces.

max_depth  ( Optional[int] , default:  None  ) – Optional integer specifying the maximum

depth of namespaces to return.

limit  ( int , default:  100  ) – Maximum number of namespaces to return (default is 100).

offset  ( int , default:  0  ) – Number of namespaces to skip before returning results

(default is 0).

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

70/121

1/11/25, 3:43 PM

SDK (Python)

Returns:

ListNamespaceResponse  – List[List[str]]: A list of namespaces matching the criteria.

Example Usage:

namespaces = client.store.list_namespaces(

prefix=["documents"],
max_depth=3,
limit=10,
offset=0

)
print(namespaces)

----------------------------------------------------------------

[

]

["documents", "user123", "reports"],
["documents", "user456", "invoices"],
...

func get_headers(api_key: Optional[str],

custom_headers: Optional[dict[str, str]]) -> dict[str,

str]

Combine api_key and custom user-provided headers.

func get_client(*, url: Optional[str] = None, api_key:

Optional[str] = None, headers: Optional[dict[str, str]]

= None) -> LangGraphClient

Get a LangGraphClient instance.

Parameters:

url  ( Optional[str] , default:  None  ) – The URL of the LangGraph API.

api_key  ( Optional[str] , default:  None  ) – The API key. If not provided, it will be read from

the environment. Precedence: 1. explicit argument 2. LANGGRAPH_API_KEY 3.

LANGSMITH_API_KEY 4. LANGCHAIN_API_KEY

headers  ( Optional[dict[str, str]] , default:  None  ) – Optional custom headers

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

71/121

1/11/25, 3:43 PM

SDK (Python)

Returns:

LangGraphClient  (  LangGraphClient  ) – The top-level client for accessing AssistantsClient,

LangGraphClient  – ThreadsClient, RunsClient, and CronClient.

Example:

from langgraph_sdk import get_client

# get top-level LangGraphClient
client = get_client(url="http://localhost:8123")

# example usage: client.<model>.<method_name>()
assistants = await client.assistants.get(assistant_id="some_uuid")

func get_sync_client(*, url: Optional[str] = None,

api_key: Optional[str] = None, headers:

Optional[dict[str, str]] = None) -> SyncLangGraphClient

Get a synchronous LangGraphClient instance.

Parameters:

url  ( Optional[str] , default:  None  ) – The URL of the LangGraph API.

api_key  ( Optional[str] , default:  None  ) – The API key. If not provided, it will be read from

the environment. Precedence: 1. explicit argument 2. LANGGRAPH_API_KEY 3.

LANGSMITH_API_KEY 4. LANGCHAIN_API_KEY

headers  ( Optional[dict[str, str]] , default:  None  ) – Optional custom headers

Returns: SyncLangGraphClient: The top-level synchronous client for accessing

AssistantsClient, ThreadsClient, RunsClient, and CronClient.

Example:

from langgraph_sdk import get_sync_client

# get top-level synchronous LangGraphClient
client = get_sync_client(url="http://localhost:8123")

# example usage: client.<model>.<method_name>()
assistant = client.assistants.get(assistant_id="some_uuid")

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

72/121

1/11/25, 3:43 PM

SDK (Python)

Data models for interacting with the LangGraph API.

attr Json = Optional[dict[str, Any]]

Represents a JSON-like structure, which can be None or a dictionary with string keys and any

values.

attr RunStatus = Literal['pending', 'error', 'success',

'timeout', 'interrupted']

Represents the status of a run: - "pending": The run is waiting to start. - "error": The run

encountered an error and stopped. - "success": The run completed successfully. - "timeout": The

run exceeded its time limit. - "interrupted": The run was manually stopped or interrupted.

attr ThreadStatus = Literal['idle', 'busy',

'interrupted', 'error']

Represents the status of a thread: - "idle": The thread is not currently processing any task. -

"busy": The thread is actively processing a task. - "interrupted": The thread's execution was

interrupted. - "error": An exception occurred during task processing.

attr StreamMode = Literal['values', 'messages',

'updates', 'events', 'debug', 'custom', 'messages-

tuple']

De nes the mode of streaming: - "values": Stream only the values. - "messages": Stream

complete messages. - "updates": Stream updates to the state. - "events": Stream events

occurring during execution. - "debug": Stream detailed debug information. - "custom": Stream

custom events.

attr DisconnectMode = Literal['cancel', 'continue']

Speci es behavior on disconnection: - "cancel": Cancel the operation on disconnection. -

"continue": Continue the operation even if disconnected.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

73/121

module-attributemodule-attributemodule-attributemodule-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

attr MultitaskStrategy = Literal['reject', 'interrupt',

'rollback', 'enqueue']

De nes how to handle multiple tasks: - "reject": Reject new tasks when busy. - "interrupt":

Interrupt current task for new ones. - "rollback": Roll back current task and start new one. -

"enqueue": Queue new tasks for later execution.

attr OnConflictBehavior = Literal['raise',

'do_nothing']

Speci es behavior on con ict: - "raise": Raise an exception when a con ict occurs. -

"do_nothing": Ignore con icts and proceed.

attr OnCompletionBehavior = Literal['delete', 'keep']

De nes action after completion: - "delete": Delete resources after completion. - "keep": Retain

resources after completion.

attr All = Literal['*']

Represents a wildcard or 'all' selector.

attr IfNotExists = Literal['create', 'reject']

Speci es behavior if the thread doesn't exist: - "create": Create a new thread if it doesn't exist. -

"reject": Reject the operation if the thread doesn't exist.

attr CancelAction = Literal['interrupt', 'rollback']

Action to take when cancelling the run. - "interrupt": Simply cancel the run. - "rollback": Cancel

the run. Then delete the run and associated checkpoints.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

74/121

module-attributemodule-attributemodule-attributemodule-attributemodule-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

class Config

Bases:  TypedDict

Con guration options for a call.

attr   tags: list[str]

Tags for this call and any sub-calls (eg. a Chain calling an LLM). You can use these to  lter

calls.

attr   recursion_limit: int

Maximum number of times a call can recurse. If not provided, defaults to 25.

attr   configurable: dict[str, Any]

Runtime values for attributes previously made con gurable on this Runnable, or sub-

Runnables, through .con gurable_ elds() or .con gurable_alternatives(). Check

.output_schema() for a description of the attributes that have been made con gurable.

class Checkpoint

Bases:  TypedDict

Represents a checkpoint in the execution process.

attr   thread_id: str

Unique identi er for the thread associated with this checkpoint.

attr   checkpoint_ns: str

Namespace for the checkpoint, used for organization and retrieval.

attr   checkpoint_id: Optional[str]

Optional unique identi er for the checkpoint itself.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

75/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   checkpoint_map: Optional[dict[str, Any]]

Optional dictionary containing checkpoint-speci c data.

class GraphSchema

Bases:  TypedDict

De nes the structure and properties of a graph.

attr   graph_id: str

The ID of the graph.

attr   input_schema: Optional[dict]

The schema for the graph input. Missing if unable to generate JSON schema from graph.

attr   output_schema: Optional[dict]

The schema for the graph output. Missing if unable to generate JSON schema from graph.

attr   state_schema: Optional[dict]

The schema for the graph state. Missing if unable to generate JSON schema from graph.

attr   config_schema: Optional[dict]

The schema for the graph con g. Missing if unable to generate JSON schema from graph.

class AssistantBase

Bases:  TypedDict

Base model for an assistant.

attr   assistant_id: str

The ID of the assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

76/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   graph_id: str

The ID of the graph.

attr   config: Config

The assistant con g.

attr   created_at: datetime

The time the assistant was created.

attr   metadata: Json

The assistant metadata.

attr   version: int

The version of the assistant

class AssistantVersion

Bases:  AssistantBase

Represents a speci c version of an assistant.

attr   assistant_id: str

The ID of the assistant.

attr   graph_id: str

The ID of the graph.

attr   config: Config

The assistant con g.

attr   created_at: datetime

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

77/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

The time the assistant was created.

attr   metadata: Json

The assistant metadata.

attr   version: int

The version of the assistant

class Assistant

Bases:  AssistantBase

Represents an assistant with additional properties.

attr   assistant_id: str

The ID of the assistant.

attr   graph_id: str

The ID of the graph.

attr   config: Config

The assistant con g.

attr   created_at: datetime

The time the assistant was created.

attr   metadata: Json

The assistant metadata.

attr   version: int

The version of the assistant

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

78/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   updated_at: datetime

The last time the assistant was updated.

attr   name: str

The name of the assistant

class Interrupt

Bases:  TypedDict

Represents an interruption in the execution  ow.

attr   value: Any

The value associated with the interrupt.

attr   when: Literal['during']

When the interrupt occurred.

attr   resumable: bool

Whether the interrupt can be resumed.

attr   ns: Optional[list[str]]

Optional namespace for the interrupt.

class Thread

Bases:  TypedDict

Represents a conversation thread.

attr   thread_id: str

The ID of the thread.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

79/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   created_at: datetime

The time the thread was created.

attr   updated_at: datetime

The last time the thread was updated.

attr   metadata: Json

The thread metadata.

attr   status: ThreadStatus

The status of the thread, one of 'idle', 'busy', 'interrupted'.

attr   values: Json

The current state of the thread.

attr   interrupts: Dict[str, list[Interrupt]]

Interrupts which were thrown in this thread

class ThreadTask

Bases:  TypedDict

Represents a task within a thread.

class ThreadState

Bases:  TypedDict

Represents the state of a thread.

attr   values: Union[list[dict], dict[str, Any]]

The state values.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

80/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   next: Sequence[str]

The next nodes to execute. If empty, the thread is done until new input is received.

attr   checkpoint: Checkpoint

The ID of the checkpoint.

attr   metadata: Json

Metadata for this state

attr   created_at: Optional[str]

Timestamp of state creation

attr   parent_checkpoint: Optional[Checkpoint]

The ID of the parent checkpoint. If missing, this is the root checkpoint.

attr   tasks: Sequence[ThreadTask]

Tasks to execute in this step. If already attempted, may contain an error.

class ThreadUpdateStateResponse

Bases:  TypedDict

Represents the response from updating a thread's state.

attr   checkpoint: Checkpoint

Checkpoint of the latest state.

class Run

Bases:  TypedDict

Represents a single execution run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

81/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   run_id: str

The ID of the run.

attr   thread_id: str

The ID of the thread.

attr   assistant_id: str

The assistant that was used for this run.

attr   created_at: datetime

The time the run was created.

attr   updated_at: datetime

The last time the run was updated.

attr   status: RunStatus

The status of the run. One of 'pending', 'running', "error", 'success', "timeout", "interrupted".

attr   metadata: Json

The run metadata.

attr   multitask_strategy: MultitaskStrategy

Strategy to handle concurrent runs on the same thread.

class Cron

Bases:  TypedDict

Represents a scheduled task.

attr   cron_id: str

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

82/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

The ID of the cron.

attr   thread_id: Optional[str]

The ID of the thread.

attr   end_time: Optional[datetime]

The end date to stop running the cron.

attr   schedule: str

The schedule to run, cron format.

attr   created_at: datetime

The time the cron was created.

attr   updated_at: datetime

The last time the cron was updated.

attr   payload: dict

The run payload to use for creating new run.

class RunCreate

Bases:  TypedDict

De nes the parameters for initiating a background run.

attr   thread_id: Optional[str]

The identi er of the thread to run. If not provided, the run is stateless.

attr   assistant_id: str

The identi er of the assistant to use for this run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

83/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   input: Optional[dict]

Initial input data for the run.

attr   metadata: Optional[dict]

Additional metadata to associate with the run.

attr   config: Optional[Config]

Con guration options for the run.

attr   checkpoint_id: Optional[str]

The identi er of a checkpoint to resume from.

attr   interrupt_before: Optional[list[str]]

List of node names to interrupt execution before.

attr   interrupt_after: Optional[list[str]]

List of node names to interrupt execution after.

attr   webhook: Optional[str]

URL to send webhook noti cations about the run's progress.

attr   multitask_strategy: Optional[MultitaskStrategy]

Strategy for handling concurrent runs on the same thread.

class Item

Bases:  TypedDict

Represents a single document or data entry in the graph's Store.

Items are used to store cross-thread memories.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

84/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   namespace: list[str]

The namespace of the item. A namespace is analogous to a document's directory.

attr   key: str

The unique identi er of the item within its namespace.

In general, keys needn't be globally unique.

attr   value: dict[str, Any]

The value stored in the item. This is the document itself.

attr   created_at: datetime

The timestamp when the item was created.

attr   updated_at: datetime

The timestamp when the item was last updated.

class ListNamespaceResponse

Bases:  TypedDict

Response structure for listing namespaces.

attr   namespaces: list[list[str]]

A list of namespace paths, where each path is a list of strings.

class SearchItem

Bases:  Item

Item with an optional relevance score from search operations.

Attributes:

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

85/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

score  ( Optional[float] ) – Relevance/similarity score. Included when searching a

compatible store with a natural language query.

attr   namespace: list[str]

The namespace of the item. A namespace is analogous to a document's directory.

attr   key: str

The unique identi er of the item within its namespace.

In general, keys needn't be globally unique.

attr   value: dict[str, Any]

The value stored in the item. This is the document itself.

attr   created_at: datetime

The timestamp when the item was created.

attr   updated_at: datetime

The timestamp when the item was last updated.

class SearchItemsResponse

Bases:  TypedDict

Response structure for searching items.

attr   items: list[SearchItem]

A list of items matching the search criteria.

class StreamPart

Bases:  NamedTuple

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

86/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Represents a part of a stream response.

attr   event: str

The type of event for this stream part.

attr   data: dict

The data payload associated with the event.

class Auth

Add custom authentication and authorization management to your LangGraph application.

The Auth class provides a uni ed system for handling authentication and authorization in

LangGraph applications. It supports custom user authentication protocols and  ne-grained

authorization rules for different resources and actions.

To use, create a separate python  le and add the path to the  le to your LangGraph API

con guration  le ( langgraph.json ). Within that  le, create an instance of the Auth class and

register authentication and authorization handlers as needed.

Example  langgraph.json   le:

{

"dependencies": ["."],
"graphs": {

"agent": "./my_agent/agent.py:graph"

},
"env": ".env",
"auth": {

"path": "./auth.py:my_auth"

}

Then the LangGraph server will load your auth  le and run it server-side whenever a request

comes in.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

87/121

instance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Basic Usage

from langgraph_sdk import Auth

my_auth = Auth()

async def verify_token(token: str) -> str:
# Verify token and return user_id
# This would typically be a call to your auth server
return "user_id"

@auth.authenticate
async def authenticate(authorization: str) -> str:

# Verify token and return user_id
result = await verify_token(authorization)
if result != "user_id":

raise Auth.exceptions.HTTPException(

status_code=401, detail="Unauthorized"

)

return result

# Global fallback handler
@auth.on
async def authorize_default(params: Auth.on.value):

return False # Reject all requests (default behavior)

@auth.on.threads.create
async def authorize_thread_create(params: Auth.on.threads.create.value):

# Allow the allowed user to create a thread
assert params.get("metadata", {}).get("owner") == "allowed_user"

@auth.on.store
async def authorize_store(ctx: Auth.types.AuthContext, value: Auth.types.on):

assert ctx.user.identity in value["namespace"], "Not authorized"

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

88/121

1/11/25, 3:43 PM

SDK (Python)

Request Processing Flow

   Authentication (your  @auth.authenticate  handler) is performed  rst on every request

   For authorization, the most speci c matching handler is called:

If a handler exists for the exact resource and action, it is used (e.g.,
@auth.on.threads.create )

Otherwise, if a handler exists for the resource with any action, it is used (e.g.,

@auth.on.threads )

Finally, if no speci c handlers match, the global handler is used (e.g.,  @auth.on )

If no global handler is set, the request is accepted

This allows you to set default behavior with a global handler while overriding speci c routes as

needed.

attr   types = types

Reference to auth type de nitions.

Provides access to all type de nitions used in the auth system, like ThreadsCreate,

AssistantsRead, etc.

attr   exceptions = exceptions

Reference to auth exception de nitions.

Provides access to all exception de nitions used in the auth system, like HTTPException, etc.

attr   on = _On(self)

Entry point for authorization handlers that control access to speci c resources.

The on class provides a  exible way to de ne authorization rules for different resources and

actions in your application. It supports three main usage patterns:

   Global handlers that run for all resources and actions

   Resource-speci c handlers that run for all actions on a resource

   Resource and action speci c handlers for  ne-grained control

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

89/121

class-attributeinstance-attributeclass-attributeinstance-attributeinstance-attribute

1/11/25, 3:43 PM

SDK (Python)

Each handler must be an async function that accepts two parameters

ctx (AuthContext): Contains request context and authenticated user info

value: The data being authorized (type varies by endpoint)

The handler should return one of:

- None or True: Accept the request
- False: Reject with 403 error
- FilterType: Apply filtering rules to the response

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

90/121

1/11/25, 3:43 PM

SDK (Python)

Examples

Global handler for all requests:

@auth.on
async def reject_unhandled_requests(ctx: AuthContext, value: Any) -> None:

print(f"Request to {ctx.path} by {ctx.user.identity}")
return False

Resource-speci c handler. This would take precedence over the global handler for all actions on
the  threads  resource:

@auth.on.threads
async def check_thread_access(ctx: AuthContext, value: Any) -> bool:

# Allow access only to threads created by the user
return value.get("created_by") == ctx.user.identity

Resource and action speci c handler:

@auth.on.threads.delete
async def prevent_thread_deletion(ctx: AuthContext, value: Any) -> bool:

# Only admins can delete threads
return "admin" in ctx.user.permissions

Multiple resources or actions:

@auth.on(resources=["threads", "runs"], actions=["create", "update"])
async def rate_limit_writes(ctx: AuthContext, value: Any) -> bool:

# Implement rate limiting for write operations
return await check_rate_limit(ctx.user.identity)

Auth for the  store  resource is a bit different since its structure is developer de ned. You

typically want to enforce user creds in the namespace. Y

@auth.on.store
async def check_store_access(ctx: AuthContext, value: Auth.types.on) -> bool:

# Assuming you structure your store like (store.aput((user_id,

application_context), key, value))

assert value["namespace"][0] == ctx.user.identity

meth   authenticate(fn: AH) -> AH

Register an authentication handler function.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

91/121

1/11/25, 3:43 PM

SDK (Python)

The authentication handler is responsible for verifying credentials and returning user scopes.

It can accept any of the following parameters by name:

- request (Request): The raw ASGI request object
- body (dict): The parsed request body
- path (str): The request path, e.g., "/threads/abcd-1234-abcd-1234/runs/abcd-
1234-abcd-1234/stream"
- method (str): The HTTP method, e.g., "GET"
- path_params (dict[str, str]): URL path parameters, e.g., {"thread_id": "abcd-
1234-abcd-1234", "run_id": "abcd-1234-abcd-1234"}
- query_params (dict[str, str]): URL query parameters, e.g., {"stream": "true"}
- headers (dict[bytes, bytes]): Request headers
- authorization (str | None): The Authorization header value (e.g., "Bearer
<token>")

Parameters:

fn  ( Callable ) – The authentication handler function to register. Must return a

representation of the user. This could be a: - string (the user id) - dict containing {"identity":

str, "permissions": list[str]} - or an object with identity and permissions properties

Permissions can be optionally used by your handlers downstream.

Returns:

AH  – The registered handler function.

Raises:

ValueError  – If an authentication handler is already registered.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

92/121

1/11/25, 3:43 PM

SDK (Python)

Examples

Basic token authentication:

@auth.authenticate
async def authenticate(authorization: str) -> str:

user_id = verify_token(authorization)
return user_id

Accept the full request context:

@auth.authenticate
async def authenticate(

method: str,
path: str,
headers: dict[str, bytes]

) -> str:

user = await verify_request(method, path, headers)
return user

Return user name and permissions:

@auth.authenticate
async def authenticate(

method: str,
path: str,
headers: dict[str, bytes]
) -> Auth.types.MinimalUserDict:

permissions, user = await verify_request(method, path, headers)
# Permissions could be things like ["runs:read", "runs:write", "threads:read",

"threads:write"]
return {

"identity": user["id"],
"permissions": permissions,
"display_name": user["name"],

}

Authentication and authorization types for LangGraph.

This module de nes the core types used for authentication, authorization, and request

handling in LangGraph. It includes user protocols, authentication contexts, and typed

dictionaries for various API operations.

Note

All typing.TypedDict classes use total=False to make all  elds typing.Optional by default.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

93/121

1/11/25, 3:43 PM

SDK (Python)

attr RunStatus = typing.Literal['pending', 'error',

'success', 'timeout', 'interrupted']

Status of a run execution.

Values

pending: Run is queued or in progress

error: Run failed with an error

success: Run completed successfully

timeout: Run exceeded time limit

interrupted: Run was manually interrupted

attr MultitaskStrategy = typing.Literal['reject',

'rollback', 'interrupt', 'enqueue']

Strategy for handling multiple concurrent tasks.

Values

reject: Reject new tasks while one is in progress

rollback: Cancel current task and start new one

interrupt: Interrupt current task and start new one

enqueue: Queue new tasks to run after current one

attr OnConflictBehavior = typing.Literal['raise',

'do_nothing']

Behavior when encountering con icts.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

94/121

module-attributemodule-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

Values

raise: Raise an exception on con ict

do_nothing: Silently ignore con icts

attr IfNotExists = typing.Literal['create', 'reject']

Behavior when an entity doesn't exist.

Values

create: Create the entity

reject: Reject the operation

attr FilterType = typing.Union[typing.Dict[str,

typing.Union[str, typing.Dict[typing.Literal['$eq',

'$contains'], str]]], typing.Dict[str, str]]

Response type for authorization handlers.

Supports exact matches and operators

Exact match shorthand: {" eld": "value"}

Exact match: {" eld": {"$eq": "value"}}

Contains: {" eld": {"$contains": "value"}}

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

95/121

module-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

Examples

Simple exact match  lter for the resource owner:

filter = {"owner": "user-abcd123"}

Explicit version of the exact match  lter:

filter = {"owner": {"$eq": "user-abcd123"}}

Containment:

filter = {"participants": {"$contains": "user-abcd123"}}

Combining  lters (treated as a logical  AND ):

filter = {"owner": "user-abcd123", "participants": {"$contains": "user-efgh456"}}

attr ThreadStatus = typing.Literal['idle', 'busy',

'interrupted', 'error']

Status of a thread.

Values

idle: Thread is available for work

busy: Thread is currently processing

interrupted: Thread was interrupted

error: Thread encountered an error

attr MetadataInput = typing.Dict[str, typing.Any]

Type for arbitrary metadata attached to entities.

Allows storing custom key-value pairs with any entity. Keys must be strings, values can be any

JSON-serializable type.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

96/121

module-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

Examples

metadata = {

"created_by": "user123",
"priority": 1,
"tags": ["important", "urgent"]

}

attr HandlerResult = typing.Union[None, bool,

FilterType]

The result of a handler can be: * None | True: accept the request. * False: reject the request

with a 403 error * FilterType:  lter to apply

attr Authenticator = Callable[...,

Awaitable[typing.Union[MinimalUser, str, BaseUser,

MinimalUserDict, typing.Mapping[str, typing.Any]]]]

Type for authentication functions.

An authenticator can return either: 1. A string (user_id) 2. A dict containing {"identity": str,

"permissions": list[str]} 3. An object with identity and permissions properties

Permissions can be used downstream by your authorization logic to determine access

permissions to different resources.

The authenticate decorator will automatically inject any of the following parameters by name if

they are included in your function signature:

Parameters:

request  ( Request ) – The raw ASGI request object

body  ( dict ) – The parsed request body

path  ( str ) – The request path

method  ( str ) – The HTTP method (GET, POST, etc.)

path_params  ( dict[str, str] | None ) – URL path parameters

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

97/121

module-attributemodule-attribute1/11/25, 3:43 PM

SDK (Python)

query_params  ( dict[str, str] | None ) – URL query parameters

headers  ( dict[str, bytes] | None ) – Request headers

authorization  ( str | None ) – The Authorization header value (e.g. "Bearer ")

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

98/121

1/11/25, 3:43 PM

SDK (Python)

Examples

Basic authentication with token:

from langgraph_sdk import Auth

auth = Auth()

@auth.authenticate
async def authenticate1(authorization: str) -> Auth.types.MinimalUserDict:

return await get_user(authorization)

Authentication with multiple parameters:

@auth.authenticate
async def authenticate2(
    method: str,
    path: str,
    headers: dict[str, bytes]
) -> Auth.types.MinimalUserDict:
    # Custom auth logic using method, path and headers
    user = verify_request(method, path, headers)
    return user

Accepting the raw ASGI request:

MY_SECRET = "my-secret-key"
@auth.authenticate
async def get_current_user(request: Request) -> Auth.types.MinimalUserDict:

try:

token = (request.headers.get("authorization") or "").split(" ", 1)[1]
payload = jwt.decode(token, MY_SECRET, algorithms=["HS256"])

except (IndexError, InvalidTokenError):

raise HTTPException(
status_code=401,
detail="Invalid token",
headers={"WWW-Authenticate": "Bearer"},

)

async with httpx.AsyncClient() as client:

response = await client.get(

f"https://api.myauth-provider.com/auth/v1/user",
headers={"Authorization": f"Bearer {MY_SECRET}"}

)
if response.status_code != 200:

raise HTTPException(status_code=401, detail="User not found")

user_data = response.json()
return {

"identity": user_data["id"],
"display_name": user_data.get("name"),
"permissions": user_data.get("permissions", []),

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

99/121

1/11/25, 3:43 PM

SDK (Python)

"is_authenticated": True,

}

class MinimalUser

Bases:  Protocol

User objects must at least expose the identity property.

attr   identity: str

The unique identi er for the user.

This could be a username, email, or any other unique identi er used to distinguish between

different users in the system.

class MinimalUserDict

Bases:  TypedDict

The dictionary representation of a user.

attr   identity: typing_extensions.Required[str]

The required unique identi er for the user.

attr   display_name: str

The typing.Optional display name for the user.

attr   is_authenticated: bool

Whether the user is authenticated. Defaults to True.

attr   permissions: Sequence[str]

A list of permissions associated with the user.

You can use these in your  @auth.on  authorization logic to determine access permissions to

different resources.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

100/121

propertyinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

class BaseUser

Bases:  Protocol

The base ASGI user protocol

attr   is_authenticated: bool

Whether the user is authenticated.

attr   display_name: str

The display name of the user.

attr   identity: str

The unique identi er for the user.

attr   permissions: Sequence[str]

The permissions associated with the user.

class StudioUser

A user object that's populated from authenticated requests from the LangGraph studio.

Note: Studio auth can be disabled in your  langgraph.json  con g.

{

}

"auth": {

"disable_studio_auth": true

}

You can use  isinstance  checks in your authorization handlers ( @auth.on ) to control access

speci cally for developers accessing the instance from the LangGraph Studio UI.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

101/121

propertypropertypropertyproperty1/11/25, 3:43 PM

SDK (Python)

Examples

@auth.on
async def allow_developers(ctx: Auth.types.AuthContext, value: Any) -> None:

if isinstance(ctx.user, Auth.types.StudioUser):

return None

...
return False

class BaseAuthContext

Base class for authentication context.

Provides the fundamental authentication information needed for authorization decisions.

attr   permissions: Sequence[str]

The permissions granted to the authenticated user.

attr   user: BaseUser

The authenticated user.

class AuthContext

Bases:  BaseAuthContext

Complete authentication context with resource and action information.

Extends BaseAuthContext with speci c resource and action being accessed, allowing for  ne-

grained access control decisions.

attr   permissions: Sequence[str]

The permissions granted to the authenticated user.

attr   user: BaseUser

The authenticated user.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

102/121

instance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   resource: typing.Literal['runs', 'threads', 'crons',
'assistants', 'store']

The resource being accessed.

attr   action: typing.Literal['create', 'read', 'update', 'delete',
'search', 'create_run', 'put', 'get', 'list_namespaces']

The action being performed on the resource.

Most resources support the following actions: - create: Create a new resource - read: Read

information about a resource - update: Update an existing resource - delete: Delete a resource -

search: Search for resources

The store supports the following actions: - put: Add or update a document in the store - get: Get

a document from the store - list_namespaces: List the namespaces in the store

class ThreadsCreate

Bases:  TypedDict

Parameters for creating a new thread.

Examples

create_params = {

"thread_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"metadata": {"owner": "user123"},
"if_exists": "do_nothing"

}

attr   thread_id: UUID

Unique identi er for the thread.

attr   metadata: MetadataInput

typing.Optional metadata to attach to the thread.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

103/121

instance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   if_exists: OnConflictBehavior

Behavior when a thread with the same ID already exists.

class ThreadsRead

Bases:  TypedDict

Parameters for reading thread state or run information.

This type is used in three contexts: 1. Reading thread, thread version, or thread state

information: Only thread_id is provided 2. Reading run information: Both thread_id and run_id

are provided

attr   thread_id: UUID

Unique identi er for the thread.

attr   run_id: typing.Optional[UUID]

Run ID to  lter by. Only used when reading run information within a thread.

class ThreadsUpdate

Bases:  TypedDict

Parameters for updating a thread or run.

Called for updates to a thread, thread version, or run cancellation.

attr   thread_id: UUID

Unique identi er for the thread.

attr   metadata: MetadataInput

typing.Optional metadata to update.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

104/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   action: typing.Optional[typing.Literal['interrupt',
'rollback']]

typing.Optional action to perform on the thread.

class ThreadsDelete

Bases:  TypedDict

Parameters for deleting a thread.

Called for deletes to a thread, thread version, or run

attr   thread_id: UUID

Unique identi er for the thread.

attr   run_id: typing.Optional[UUID]

typing.Optional run ID to  lter by.

class ThreadsSearch

Bases:  TypedDict

Parameters for searching threads.

Called for searches to threads or runs.

attr   metadata: MetadataInput

typing.Optional metadata to  lter by.

attr   values: MetadataInput

typing.Optional values to  lter by.

attr   status: typing.Optional[ThreadStatus]

typing.Optional status to  lter by.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

105/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   limit: int

Maximum number of results to return.

attr   offset: int

Offset for pagination.

attr   thread_id: typing.Optional[UUID]

typing.Optional thread ID to  lter by.

class RunsCreate

Bases:  TypedDict

Payload for creating a run.

Examples

create_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"thread_id": UUID("123e4567-e89b-12d3-a456-426614174001"),
"run_id": UUID("123e4567-e89b-12d3-a456-426614174002"),
"status": "pending",
"metadata": {"owner": "user123"},
"prevent_insert_if_inflight": True,
"multitask_strategy": "reject",
"if_not_exists": "create",
"after_seconds": 10,
"kwargs": {"key": "value"},
"action": "interrupt"

}

attr   assistant_id: typing.Optional[UUID]

typing.Optional assistant ID to use for this run.

attr   thread_id: typing.Optional[UUID]

typing.Optional thread ID to use for this run.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

106/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   run_id: typing.Optional[UUID]

typing.Optional run ID to use for this run.

attr   status: typing.Optional[RunStatus]

typing.Optional status for this run.

attr   metadata: MetadataInput

typing.Optional metadata for the run.

attr   prevent_insert_if_inflight: bool

Prevent inserting a new run if one is already in  ight.

attr   multitask_strategy: MultitaskStrategy

Multitask strategy for this run.

attr   if_not_exists: IfNotExists

IfNotExists for this run.

attr   after_seconds: int

Number of seconds to wait before creating the run.

attr   kwargs: typing.Dict[str, typing.Any]

Keyword arguments to pass to the run.

attr   action: typing.Optional[typing.Literal['interrupt',
'rollback']]

Action to take if updating an existing run.

class AssistantsCreate

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

107/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Bases:  TypedDict

Payload for creating an assistant.

Examples

create_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"graph_id": "graph123",
"config": {"key": "value"},
"metadata": {"owner": "user123"},
"if_exists": "do_nothing",
"name": "Assistant 1"

}

attr   assistant_id: UUID

Unique identi er for the assistant.

attr   graph_id: str

Graph ID to use for this assistant.

attr   config: typing.Optional[typing.Union[typing.Dict[str,
typing.Any], typing.Any]]

typing.Optional con guration for the assistant.

attr   metadata: MetadataInput

typing.Optional metadata to attach to the assistant.

attr   if_exists: OnConflictBehavior

Behavior when an assistant with the same ID already exists.

attr   name: str

Name of the assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

108/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

class AssistantsRead

Bases:  TypedDict

Payload for reading an assistant.

Examples

read_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"metadata": {"owner": "user123"}

}

attr   assistant_id: UUID

Unique identi er for the assistant.

attr   metadata: MetadataInput

typing.Optional metadata to  lter by.

class AssistantsUpdate

Bases:  TypedDict

Payload for updating an assistant.

Examples

update_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"graph_id": "graph123",
"config": {"key": "value"},
"metadata": {"owner": "user123"},
"name": "Assistant 1",
"version": 1

}

attr   assistant_id: UUID

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

109/121

instance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Unique identi er for the assistant.

attr   graph_id: typing.Optional[str]

typing.Optional graph ID to update.

attr   config: typing.Optional[typing.Union[typing.Dict[str,
typing.Any], typing.Any]]

typing.Optional con guration to update.

attr   metadata: MetadataInput

typing.Optional metadata to update.

attr   name: typing.Optional[str]

typing.Optional name to update.

attr   version: typing.Optional[int]

typing.Optional version to update.

class AssistantsDelete

Bases:  TypedDict

Payload for deleting an assistant.

Examples

delete_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000")

}

attr   assistant_id: UUID

Unique identi er for the assistant.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

110/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

class AssistantsSearch

Bases:  TypedDict

Payload for searching assistants.

Examples

search_params = {

"graph_id": "graph123",
"metadata": {"owner": "user123"},
"limit": 10,
"offset": 0

}

attr   graph_id: typing.Optional[str]

typing.Optional graph ID to  lter by.

attr   metadata: MetadataInput

typing.Optional metadata to  lter by.

attr   limit: int

Maximum number of results to return.

attr   offset: int

Offset for pagination.

class CronsCreate

Bases:  TypedDict

Payload for creating a cron job.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

111/121

instance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Examples

create_params = {

"payload": {"key": "value"},
"schedule": "0 0 * * *",
"cron_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"thread_id": UUID("123e4567-e89b-12d3-a456-426614174001"),
"user_id": "user123",
"end_time": datetime(2024, 3, 16, 10, 0, 0)

}

attr   payload: typing.Dict[str, typing.Any]

Payload for the cron job.

attr   schedule: str

Schedule for the cron job.

attr   cron_id: typing.Optional[UUID]

typing.Optional unique identi er for the cron job.

attr   thread_id: typing.Optional[UUID]

typing.Optional thread ID to use for this cron job.

attr   user_id: typing.Optional[str]

typing.Optional user ID to use for this cron job.

attr   end_time: typing.Optional[datetime]

typing.Optional end time for the cron job.

class CronsDelete

Bases:  TypedDict

Payload for deleting a cron job.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

112/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Examples

delete_params = {

"cron_id": UUID("123e4567-e89b-12d3-a456-426614174000")

}

attr   cron_id: UUID

Unique identi er for the cron job.

class CronsRead

Bases:  TypedDict

Payload for reading a cron job.

Examples

read_params = {

"cron_id": UUID("123e4567-e89b-12d3-a456-426614174000")

}

attr   cron_id: UUID

Unique identi er for the cron job.

class CronsUpdate

Bases:  TypedDict

Payload for updating a cron job.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

113/121

instance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Examples

update_params = {

"cron_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"payload": {"key": "value"},
"schedule": "0 0 * * *"

}

attr   cron_id: UUID

Unique identi er for the cron job.

attr   payload: typing.Optional[typing.Dict[str, typing.Any]]

typing.Optional payload to update.

attr   schedule: typing.Optional[str]

typing.Optional schedule to update.

class CronsSearch

Bases:  TypedDict

Payload for searching cron jobs.

Examples

search_params = {

"assistant_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
"thread_id": UUID("123e4567-e89b-12d3-a456-426614174001"),
"limit": 10,
"offset": 0

}

attr   assistant_id: typing.Optional[UUID]

typing.Optional assistant ID to  lter by.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

114/121

instance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   thread_id: typing.Optional[UUID]

typing.Optional thread ID to  lter by.

attr   limit: int

Maximum number of results to return.

attr   offset: int

Offset for pagination.

class StoreGet

Bases:  TypedDict

Operation to retrieve a speci c item by its namespace and key.

attr   namespace: tuple[str, ...]

Hierarchical path that uniquely identi es the item's location.

attr   key: str

Unique identi er for the item within its speci c namespace.

class StoreSearch

Bases:  TypedDict

Operation to search for items within a speci ed namespace hierarchy.

attr   namespace: tuple[str, ...]

Pre x  lter for de ning the search scope.

attr   filter: typing.Optional[dict[str, typing.Any]]

Key-value pairs for  ltering results based on exact matches or comparison operators.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

115/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   limit: int

Maximum number of items to return in the search results.

attr   offset: int

Number of matching items to skip for pagination.

attr   query: typing.Optional[str]

Naturalj language search query for semantic search capabilities.

class StoreListNamespaces

Bases:  TypedDict

Operation to list and  lter namespaces in the store.

attr   namespace: typing.Optional[tuple[str, ...]]

Pre x  lter namespaces.

attr   suffix: typing.Optional[tuple[str, ...]]

Optional conditions for  ltering namespaces.

attr   max_depth: typing.Optional[int]

Maximum depth of namespace hierarchy to return.

Note

Namespaces deeper than this level will be truncated.

attr   limit: int

Maximum number of namespaces to return.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

116/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

attr   offset: int

Number of namespaces to skip for pagination.

class StorePut

Bases:  TypedDict

Operation to store, update, or delete an item in the store.

attr   namespace: tuple[str, ...]

Hierarchical path that identi es the location of the item.

attr   key: str

Unique identi er for the item within its namespace.

attr   value: typing.Optional[dict[str, typing.Any]]

The data to store, or None to mark the item for deletion.

attr   index: typing.Optional[typing.Union[typing.Literal[False],
list[str]]]

Optional index con guration for full-text search.

class StoreDelete

Bases:  TypedDict

Operation to delete an item from the store.

attr   namespace: tuple[str, ...]

Hierarchical path that uniquely identi es the item's location.

attr   key: str

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

117/121

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:43 PM

SDK (Python)

Unique identi er for the item within its speci c namespace.

class on

Namespace for type de nitions of different API operations.

This class organizes type de nitions for create, read, update, delete, and search operations

across different resources (threads, assistants, crons).

Usage

from langgraph_sdk import Auth

auth = Auth()

@auth.on
def handle_all(params: Auth.on.value):

raise Exception("Not authorized")

@auth.on.threads.create
def handle_thread_create(params: Auth.on.threads.create.value):

# Handle thread creation
pass

@auth.on.assistants.search
def handle_assistant_search(params: Auth.on.assistants.search.value):

# Handle assistant search
pass

class   threads

Types for thread-related operations.

class create

Type for thread creation parameters.

class create_run

Type for creating or streaming a run.

class read

Type for thread read parameters.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

118/121

1/11/25, 3:43 PM

SDK (Python)

class update

Type for thread update parameters.

class delete

Type for thread deletion parameters.

class search

Type for thread search parameters.

class   assistants

Types for assistant-related operations.

class create

Type for assistant creation parameters.

class read

Type for assistant read parameters.

class update

Type for assistant update parameters.

class delete

Type for assistant deletion parameters.

class search

Type for assistant search parameters.

class   crons

Types for cron-related operations.

class create

Type for cron creation parameters.

class read

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

119/121

1/11/25, 3:43 PM

SDK (Python)

Type for cron read parameters.

class update

Type for cron update parameters.

class delete

Type for cron deletion parameters.

class search

Type for cron search parameters.

class   store

Types for store-related operations.

class put

Type for store put parameters.

class get

Type for store get parameters.

class search

Type for store search parameters.

class delete

Type for store delete parameters.

class list_namespaces

Type for store list namespaces parameters.

Exceptions used in the auth system.

class HTTPException

Bases:  Exception

HTTP exception that you can raise to return a speci c HTTP error response.

https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/

120/121

1/11/25, 3:43 PM

SDK (Python)

Since this is de ned in the auth module, we default to a 401 status code.

Parameters:

status_code  ( int , default:  401  ) – HTTP status code for the error. Defaults to 401

"Unauthorized".

detail  ( str | None , default:  None  ) – Detailed error message. If None, uses a default

message based on the status code.

headers  ( Mapping[str, str] | None , default:  None  ) – Additional HTTP headers to include

in the error response.

Example

Default:

raise HTTPException()
# HTTPException(status_code=401, detail='Unauthorized')

Add headers:

raise HTTPException(headers={"X-Custom-Header": "Custom Value"})
# HTTPException(status_code=401, detail='Unauthorized', headers={"WWW-
Authenticate": "Bearer"})

Custom error:

raise HTTPException(status_code=404, detail="Not found")


