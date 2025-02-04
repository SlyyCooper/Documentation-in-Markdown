Checkpointers

Table of contents
 class CheckpointMetadata
 attr source
 attr step
 attr writes
 attr parents
 class Checkpoint
 attr v
 attr id
 attr ts
 attr channel_values
 attr channel_versions
 attr versions_seen
 attr pending_sends
 class BaseCheckpointSaver
 attr config_specs
 meth get
 meth get_tuple
 meth list
 meth put
 meth put_writes
 meth aget
 meth aget_tuple
 meth alist
 meth aput
 meth aput_writes
 meth get_next_version
 meth create_checkpoint
 class SerializerProtocol
 class JsonPlusSerializer
 class MemorySaver
 attr config_specs
 meth get()
 meth aget()
 meth get_tuple()
 meth list()
 meth put()
 meth put_writes()
 meth aget_tuple()
 meth alist()
 meth aput()
 meth aput_writes()

 class PersistentDict
 meth sync()

 class SqliteSaver
 attr config_specs
 meth get()
 meth aget()
 meth aput_writes()
 meth from_conn_string()
 meth setup()
 meth cursor()
 meth get_tuple()
 meth list()
 meth put()
 meth put_writes()
 meth aget_tuple()
 meth alist()
 meth aput()
 meth get_next_version()
 class AsyncSqliteSaver
 attr config_specs
 meth get
 meth aget
 meth from_conn_string
 meth get_tuple
 meth list
 meth put
 meth setup
 meth aget_tuple
 meth alist
 meth aput
 meth aput_writes
 meth get_next_version

 class BasePostgresSaver
 attr config_specs
 meth get
 meth get_tuple
 meth list
 meth put
 meth put_writes
 meth aget
 meth aget_tuple
 meth alist
 meth aput
 meth aput_writes
 class ShallowPostgresSaver
 attr config_specs
 meth get
 meth aget
 meth aget_tuple
 meth alist
 meth aput
 meth aput_writes
 meth from_conn_string
 meth setup
 meth list
 meth get_tuple
 meth put
 meth put_writes
 class PostgresSaver
 attr config_specs
 meth get
 meth aget
 meth aget_tuple
 meth alist
 meth aput
 meth aput_writes
 meth from_conn_string
 meth setup
 meth list
 meth get_tuple
 meth put
 meth put_writes
 class AsyncShallowPostgresSaver
 attr config_specs
 meth get
 meth aget
 meth from_conn_string
 meth setup
 meth alist
 meth aget_tuple
 meth aput
 meth aput_writes
 meth list
 meth get_tuple
 meth put
 meth put_writes
 class AsyncPostgresSaver
 attr config_specs
 meth get
 meth aget
 meth from_conn_string
 meth setup
 meth alist
 meth aget_tuple
 meth aput
 meth aput_writes
 meth list
 meth get_tuple
 meth put
 meth put_writes

 
Checkpointing

Home

Reference

Library

Checkpointers

class CheckpointMetadata

Bases:  TypedDict

Metadata associated with a checkpoint.

attr   source: Literal['input', 'loop', 'update', 'fork']

The source of the checkpoint.

"input": The checkpoint was created from an input to invoke/stream/batch.

"loop": The checkpoint was created from inside the pregel loop.

"update": The checkpoint was created from a manual state update.

"fork": The checkpoint was created as a copy of another checkpoint.

attr   step: int

The step number of the checkpoint.

-1 for the  rst "input" checkpoint. 0 for the  rst "loop" checkpoint. ... for the nth checkpoint

afterwards.

attr   writes: dict[str, Any]

The writes that were made between the previous checkpoint and this one.

Mapping from node name to writes emitted by that node.

attr   parents: dict[str, str]

https://langchain-ai.github.io/langgraph/reference/checkpoints/

1/54

instance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:50 PM

Checkpointing

The IDs of the parent checkpoints.

Mapping from checkpoint namespace to checkpoint ID.

class Checkpoint

Bases:  TypedDict

State snapshot at a given point in time.

attr   v: int

The version of the checkpoint format. Currently 1.

attr   id: str

The ID of the checkpoint. This is both unique and monotonically increasing, so can be used for

sorting checkpoints from  rst to last.

attr   ts: str

The timestamp of the checkpoint in ISO 8601 format.

attr   channel_values: dict[str, Any]

The values of the channels at the time of the checkpoint. Mapping from channel name to

deserialized channel snapshot value.

attr   channel_versions: ChannelVersions

The versions of the channels at the time of the checkpoint. The keys are channel names and

the values are monotonically increasing version strings for each channel.

attr   versions_seen: dict[str, ChannelVersions]

Map from node ID to map from channel name to version seen. This keeps track of the versions

of the channels that each node has seen. Used to determine which nodes to execute next.

attr   pending_sends: List[SendProtocol]

https://langchain-ai.github.io/langgraph/reference/checkpoints/

2/54

instance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attributeinstance-attribute1/11/25, 3:50 PM

Checkpointing

List of inputs pushed to nodes but not yet processed. Cleared by the next checkpoint.

class BaseCheckpointSaver

Bases:  Generic[V]

Base class for creating a graph checkpointer.

Checkpointers allow LangGraph agents to persist their state within and across multiple

interactions.

Attributes:

serde  ( SerializerProtocol ) – Serializer for encoding/decoding checkpoints.

Note

When creating a custom checkpoint saver, consider implementing async versions to avoid

blocking the main thread.

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

3/54

property1/11/25, 3:50 PM

Checkpointing

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Returns:

Iterator[CheckpointTuple]  – Iterator[CheckpointTuple]: Iterator of matching checkpoint

tuples.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

https://langchain-ai.github.io/langgraph/reference/checkpoints/

4/54

1/11/25, 3:50 PM

Checkpointing

Store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   put_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

5/54

async1/11/25, 3:50 PM

Checkpointing

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Asynchronously fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

Asynchronously list checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Returns:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: Async iterator of

matching checkpoint tuples.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

6/54

asyncasync1/11/25, 3:50 PM

Checkpointing

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Asynchronously store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

7/54

asyncasync1/11/25, 3:50 PM

Checkpointing

meth   get_next_version(current: Optional[V], channel: ChannelProtocol)
-> V

Generate the next version ID for a channel.

Default is to use integer versions, incrementing by 1. If you override, you can use str/int/ oat

versions, as long as they are monotonically increasing.

Parameters:

current  ( Optional[V] ) – The current version identi er (int,  oat, or str).

channel  ( BaseChannel ) – The channel being versioned.

Returns:

V  (  V  ) – The next version identi er, which must be increasing.

func create_checkpoint(checkpoint: Checkpoint,

channels: Optional[Mapping[str, ChannelProtocol]],

step: int, *, id: Optional[str] = None) -> Checkpoint

Create a checkpoint for the given channels.

class SerializerProtocol

Bases:  Protocol

Protocol for serialization and deserialization of objects.

dumps : Serialize an object to bytes.

dumps_typed : Serialize an object to a tuple (type, bytes).

loads : Deserialize an object from bytes.

loads_typed : Deserialize an object from a tuple (type, bytes).

Valid implementations include the  pickle ,  json  and  orjson  modules.

class JsonPlusSerializer

Bases:  SerializerProtocol

https://langchain-ai.github.io/langgraph/reference/checkpoints/

8/54

1/11/25, 3:50 PM

Checkpointing

class MemorySaver

Bases:  BaseCheckpointSaver[str] ,  AbstractContextManager ,  AbstractAsyncContextManager

An in-memory checkpoint saver.

This checkpoint saver stores checkpoints in memory using a defaultdict.

Note

Only use  MemorySaver  for debugging or testing purposes. For production use cases we

recommend installing langgraph-checkpoint-postgres and using  PostgresSaver  /
AsyncPostgresSaver .

Parameters:

serde  ( Optional[SerializerProtocol] , default:  None  ) – The serializer to use for

serializing and deserializing checkpoints. Defaults to None.

Examples:

import asyncio

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

builder = StateGraph(int)
builder.add_node("add_one", lambda x: x + 1)
builder.set_entry_point("add_one")
builder.set_finish_point("add_one")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)
coro = graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
asyncio.run(coro)  # Output: 2

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

9/54

property1/11/25, 3:50 PM

Checkpointing

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the in-memory storage.

This method retrieves a checkpoint tuple from the in-memory storage based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and timestamp is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

10/54

async1/11/25, 3:50 PM

Checkpointing

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the in-memory storage.

This method retrieves a list of checkpoint tuples from the in-memory storage based on the

provided criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Yields:

CheckpointTuple  – Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the in-memory storage.

This method saves a checkpoint to the in-memory storage. The checkpoint is associated with

the provided con g.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( dict ) – New versions as of this write

https://langchain-ai.github.io/langgraph/reference/checkpoints/

11/54

1/11/25, 3:50 PM

Checkpointing

Returns:

RunnableConfig  (  RunnableConfig  ) – The updated con g containing the saved

checkpoint's timestamp.

meth   put_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Save a list of writes to the in-memory storage.

This method saves a list of writes to the in-memory storage. The writes are associated with the

provided con g.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the writes.

writes  ( list[tuple[str, Any]] ) – The writes to save.

task_id  ( str ) – Identi er for the task creating the writes.

Returns:

RunnableConfig  (  None  ) – The updated con g containing the saved writes' timestamp.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Asynchronous version of get_tuple.

This method is an asynchronous wrapper around get_tuple that runs the synchronous method

in a separate thread using asyncio.

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

https://langchain-ai.github.io/langgraph/reference/checkpoints/

12/54

async1/11/25, 3:50 PM

Checkpointing

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

Asynchronous version of list.

This method is an asynchronous wrapper around list that runs the synchronous method in a

separate thread using asyncio.

Parameters:

config  ( RunnableConfig ) – The con g to use for listing the checkpoints.

Yields:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: An asynchronous

iterator of checkpoint tuples.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Asynchronous version of put.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( dict ) – New versions as of this write

Returns:

RunnableConfig  (  RunnableConfig  ) – The updated con g containing the saved

checkpoint's timestamp.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronous version of put_writes.

This method is an asynchronous wrapper around put_writes that runs the synchronous method

in a separate thread using asyncio.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

13/54

asyncasyncasync1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – The con g to associate with the writes.

writes  ( List[Tuple[str, Any]] ) – The writes to save, each as a (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

return self.put_writes(con g, writes, task_id)

class PersistentDict

Bases:  defaultdict

Persistent dictionary with an API compatible with shelve and anydbm.

The dict is kept in memory, so the dictionary operations run as fast as a regular dictionary.

Write to disk is delayed until close or sync (similar to gdbm's fast mode).

Input  le format is automatically discovered. Output  le format is selectable between pickle,

json, and csv. All three serialization formats are backed by fast C implementations.

Adapted from https://code.activestate.com/recipes/576642-persistent-dict-with-multiple-

standard- le-format/

meth   sync() -> None

Write dict to disk

class SqliteSaver

Bases:  BaseCheckpointSaver[str]

A checkpoint saver that stores checkpoints in a SQLite database.

Note

This class is meant for lightweight, synchronous use cases (demos and small projects) and does
not scale to multiple threads. For a similar sqlite saver with  async  support, consider using

AsyncSqliteSaver.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

14/54

1/11/25, 3:50 PM

Checkpointing

Parameters:

conn  ( Connection ) – The SQLite database connection.

serde  ( Optional[SerializerProtocol] , default:  None  ) – The serializer to use for

serializing and deserializing checkpoints. Defaults to JsonPlusSerializerCompat.

Examples:

>>> import sqlite3
>>> from langgraph.checkpoint.sqlite import SqliteSaver
>>> from langgraph.graph import StateGraph
>>>
>>> builder = StateGraph(int)
>>> builder.add_node("add_one", lambda x: x + 1)
>>> builder.set_entry_point("add_one")
>>> builder.set_finish_point("add_one")
>>> conn = sqlite3.connect("checkpoints.sqlite")
>>> memory = SqliteSaver(conn)
>>> graph = builder.compile(checkpointer=memory)
>>> config = {"configurable": {"thread_id": "1"}}
>>> graph.get_state(config)
>>> result = graph.invoke(3, config)
>>> graph.get_state(config)
StateSnapshot(values=4, next=(), config={'configurable': {'thread_id': '1',
'checkpoint_ns': '', 'checkpoint_id': '0c62ca34-ac19-445d-bbb0-5b4984975b2a'}},
parent_config=None)

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

15/54

property1/11/25, 3:50 PM

Checkpointing

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   from_conn_string(conn_string: str) -> Iterator[SqliteSaver]

Create a new SqliteSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The SQLite connection string.

Yields:

SqliteSaver  (  SqliteSaver  ) – A new SqliteSaver instance.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

16/54

asyncasyncclassmethod1/11/25, 3:50 PM

Checkpointing

Examples:

In memory:

with SqliteSaver.from_conn_string(":memory:") as memory:

...

To disk:

with SqliteSaver.from_conn_string("checkpoints.sqlite") as memory:

...

meth   setup() -> None

Set up the checkpoint database.

This method creates the necessary tables in the SQLite database if they don't already exist. It

is called automatically when needed and should not be called directly by the user.

meth   cursor(transaction: bool = True) -> Iterator[sqlite3.Cursor]

Get a cursor for the SQLite database.

This method returns a cursor for the SQLite database. It is used internally by the SqliteSaver

and should not be called directly by the user.

Parameters:

transaction  ( bool , default:  True  ) – Whether to commit the transaction when the cursor

is closed. Defaults to True.

Yields:

Cursor  – sqlite3.Cursor: A cursor for the SQLite database.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the SQLite database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

17/54

1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

Examples:

Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

With checkpoint ID:

>>> config = {
...    "configurable": {
...        "thread_id": "1",
...        "checkpoint_ns": "",
...        "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...    }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the SQLite database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( RunnableConfig ) – The con g to use for listing the checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata. Defaults to None.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

18/54

1/11/25, 3:50 PM

Checkpointing

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – The maximum number of checkpoints to return.

Defaults to None.

Yields:

CheckpointTuple  – Iterator[CheckpointTuple]: An iterator of checkpoint tuples.

Examples:

>>> from langgraph.checkpoint.sqlite import SqliteSaver
>>> with SqliteSaver.from_conn_string(":memory:") as memory:
... # Run a graph, then list the checkpoints
>>>
>>>
>>> print(checkpoints)
[CheckpointTuple(...), CheckpointTuple(...)]

config = {"configurable": {"thread_id": "1"}}
checkpoints = list(memory.list(config, limit=2))

>>> config = {"configurable": {"thread_id": "1"}}
>>> before = {"configurable": {"checkpoint_id": "1ef4f797-8335-6428-8001-
8a1503f9b875"}}
>>> with SqliteSaver.from_conn_string(":memory:") as memory:
... # Run a graph, then list the checkpoints
>>>
>>> print(checkpoints)
[CheckpointTuple(...), ...]

checkpoints = list(memory.list(config, before=before))

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the

provided con g and its parent con g (if any).

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

19/54

1/11/25, 3:50 PM

Checkpointing

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Examples:

>>> from langgraph.checkpoint.sqlite import SqliteSaver
>>> with SqliteSaver.from_conn_string(":memory:") as memory:
>>>     config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>     checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-
8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>     saved_config = memory.put(config, checkpoint, {"source": "input", "step":
1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id':
'1ef4f797-8335-6428-8001-8a1503f9b875'}}

meth   put_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the SQLite database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use get_tuple() instead, or

consider using AsyncSqliteSaver.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

https://langchain-ai.github.io/langgraph/reference/checkpoints/

20/54

async1/11/25, 3:50 PM

Checkpointing

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

List checkpoints from the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use list() instead, or consider using

AsyncSqliteSaver.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database asynchronously.

Note

This async method is not supported by the SqliteSaver class. Use put() instead, or consider using

AsyncSqliteSaver.

meth   get_next_version(current: Optional[str], channel:
ChannelProtocol) -> str

Generate the next version ID for a channel.

This method creates a new version identi er for a channel based on its current version.

Parameters:

current  ( Optional[str] ) – The current version identi er of the channel.

channel  ( BaseChannel ) – The channel being versioned.

Returns:

str  (  str  ) – The next version identi er, which is guaranteed to be monotonically

increasing.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

21/54

asyncasync1/11/25, 3:50 PM

Checkpointing

class AsyncSqliteSaver

Bases:  BaseCheckpointSaver[str]

An asynchronous checkpoint saver that stores checkpoints in a SQLite database.

This class provides an asynchronous interface for saving and retrieving checkpoints using a

SQLite database. It's designed for use in asynchronous environments and offers better

performance for I/O-bound operations compared to synchronous alternatives.

Attributes:

conn  ( Connection ) – The asynchronous SQLite database connection.

serde  ( SerializerProtocol ) – The serializer used for encoding/decoding checkpoints.

Tip

Requires the aiosqlite package. Install it with  pip install aiosqlite .

Warning

While this class supports asynchronous checkpointing, it is not recommended for production

workloads due to limitations in SQLite's write performance. For production use, consider a more

robust database like PostgreSQL.

Tip

Remember to close the database connection after executing your code, otherwise, you may see

the graph "hang" after execution (since the program will not exit until the connection is closed).

The easiest way is to use the  async with  statement as shown in the examples.

async with AsyncSqliteSaver.from_conn_string("checkpoints.sqlite") as saver:

# Your code here
graph = builder.compile(checkpointer=saver)
config = {"configurable": {"thread_id": "thread-1"}}
async for event in graph.astream_events(..., config, version="v1"):

print(event)

Examples:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

22/54

1/11/25, 3:50 PM

Checkpointing

Usage within StateGraph:

>>> import asyncio
>>>
>>> from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
>>> from langgraph.graph import StateGraph
>>>
>>> builder = StateGraph(int)
>>> builder.add_node("add_one", lambda x: x + 1)
>>> builder.set_entry_point("add_one")
>>> builder.set_finish_point("add_one")
>>> async with AsyncSqliteSaver.from_conn_string("checkpoints.db") as memory:
>>>
>>>
>>>
Output: 2

graph = builder.compile(checkpointer=memory)
coro = graph.ainvoke(1, {"configurable": {"thread_id": "thread-1"}})
print(asyncio.run(coro))

Raw usage:

async with aiosqlite.connect("checkpoints.db") as conn:

>>> import asyncio
>>> import aiosqlite
>>> from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
>>>
>>> async def main():
>>>
...
...
...
...
...
>>> asyncio.run(main())
{"configurable": {"thread_id": "1", "checkpoint_id": "0c62ca34-ac19-445d-bbb0-
5b4984975b2a"}}

saver = AsyncSqliteSaver(conn)
config = {"configurable": {"thread_id": "1"}}
checkpoint = {"ts": "2023-05-03T10:00:00Z", "data": {"key": "value"}}
saved_config = await saver.aput(config, checkpoint, {}, {})
print(saved_config)

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

23/54

property1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   from_conn_string(conn_string: str) ->
AsyncIterator[AsyncSqliteSaver]

Create a new AsyncSqliteSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The SQLite connection string.

Yields:

AsyncSqliteSaver  (  AsyncIterator[AsyncSqliteSaver]  ) – A new AsyncSqliteSaver

instance.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the SQLite database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

24/54

asyncasyncclassmethod
1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the SQLite database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Yields:

CheckpointTuple  – Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the

provided con g and its parent con g (if any).

Parameters:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

25/54

1/11/25, 3:50 PM

Checkpointing

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   setup() -> None

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the SQLite database if they don't already exist. It

is called automatically when needed and should not be called directly by the user.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the SQLite database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and checkpoint ID is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

List checkpoints from the database asynchronously.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

26/54

asyncasyncasync1/11/25, 3:50 PM

Checkpointing

This method retrieves a list of checkpoint tuples from the SQLite database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Yields:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: An asynchronous

iterator of matching checkpoint tuples.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the SQLite database. The checkpoint is associated with the

provided con g and its parent con g (if any).

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

https://langchain-ai.github.io/langgraph/reference/checkpoints/

27/54

asyncasync1/11/25, 3:50 PM

Checkpointing

Store intermediate writes linked to a checkpoint asynchronously.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

meth   get_next_version(current: Optional[str], channel:
ChannelProtocol) -> str

Generate the next version ID for a channel.

This method creates a new version identi er for a channel based on its current version.

Parameters:

current  ( Optional[str] ) – The current version identi er of the channel.

channel  ( BaseChannel ) – The channel being versioned.

Returns:

str  (  str  ) – The next version identi er, which is guaranteed to be monotonically

increasing.

class BasePostgresSaver

Bases:  BaseCheckpointSaver[str]

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

https://langchain-ai.github.io/langgraph/reference/checkpoints/

28/54

property1/11/25, 3:50 PM

Checkpointing

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

29/54

1/11/25, 3:50 PM

Checkpointing

Iterator[CheckpointTuple]  – Iterator[CheckpointTuple]: Iterator of matching checkpoint

tuples.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   put_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

30/54

1/11/25, 3:50 PM

Checkpointing

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Asynchronously fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

Asynchronously list checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

31/54

asyncasyncasync1/11/25, 3:50 PM

Checkpointing

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Returns:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: Async iterator of

matching checkpoint tuples.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Asynchronously store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

32/54

asyncasync1/11/25, 3:50 PM

Checkpointing

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

class ShallowPostgresSaver

Bases:  BasePostgresSaver

A checkpoint saver that uses Postgres to store checkpoints.

This checkpointer ONLY stores the most recent checkpoint and does NOT retain any history. It

is meant to be a light-weight drop-in replacement for the PostgresSaver that supports most of

the LangGraph persistence functionality with the exception of time travel.

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

33/54

propertyasync1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Asynchronously fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

Asynchronously list checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

34/54

asyncasync1/11/25, 3:50 PM

Checkpointing

Returns:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: Async iterator of

matching checkpoint tuples.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Asynchronously store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

35/54

asyncasync1/11/25, 3:50 PM

Checkpointing

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   from_conn_string(conn_string: str, *, pipeline: bool = False) ->
Iterator[ShallowPostgresSaver]

Create a new ShallowPostgresSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The Postgres connection info string.

pipeline  ( bool , default:  False  ) – whether to use Pipeline

Returns:

ShallowPostgresSaver  (  Iterator[ShallowPostgresSaver]  ) – A new

ShallowPostgresSaver instance.

meth   setup() -> None

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist

and runs database migrations. It MUST be called directly by the user the  rst time

checkpointer is used.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. For ShallowPostgresSaver, this method returns a list with ONLY the most

recent checkpoint.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g (matching the thread ID in the con g).

https://langchain-ai.github.io/langgraph/reference/checkpoints/

36/54

classmethod1/11/25, 3:50 PM

Checkpointing

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

Examples:

Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

With timestamp:

>>> config = {
...    "configurable": {
...        "thread_id": "1",
...        "checkpoint_ns": "",
...        "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...    }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g. For ShallowPostgresSaver, this method saves ONLY the most recent

checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

37/54

1/11/25, 3:50 PM

Checkpointing

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Examples:

>>> from langgraph.checkpoint.postgres import ShallowPostgresSaver
>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?
sslmode=disable"
>>> with ShallowPostgresSaver.from_conn_string(DB_URI) as memory:
>>>     config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>     checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-
8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>     saved_config = memory.put(config, checkpoint, {"source": "input", "step":
1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id':
'1ef4f797-8335-6428-8001-8a1503f9b875'}}

meth   put_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the Postgres database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

class PostgresSaver

Bases:  BasePostgresSaver

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

38/54

property1/11/25, 3:50 PM

Checkpointing

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Asynchronously fetch a checkpoint tuple using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The requested checkpoint tuple,

or None if not found.

Raises:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

39/54

asyncasync1/11/25, 3:50 PM

Checkpointing

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[Dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

Asynchronously list checkpoints that match the given criteria.

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – List checkpoints created before this

con guration.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Returns:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: Async iterator of

matching checkpoint tuples.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Asynchronously store a checkpoint with its con guration and metadata.

Parameters:

config  ( RunnableConfig ) – Con guration for the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to store.

metadata  ( CheckpointMetadata ) – Additional metadata for the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

40/54

asyncasync1/11/25, 3:50 PM

Checkpointing

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   aput_writes(config: RunnableConfig, writes: Sequence[Tuple[str,
Any]], task_id: str) -> None

Asynchronously store intermediate writes linked to a checkpoint.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

Raises:

NotImplementedError  – Implement this method in your custom checkpoint saver.

meth   from_conn_string(conn_string: str, *, pipeline: bool = False) ->
Iterator[PostgresSaver]

Create a new PostgresSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The Postgres connection info string.

pipeline  ( bool , default:  False  ) – whether to use Pipeline

Returns:

PostgresSaver  (  Iterator[PostgresSaver]  ) – A new PostgresSaver instance.

meth   setup() -> None

Set up the checkpoint database asynchronously.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

41/54

asyncclassmethod1/11/25, 3:50 PM

Checkpointing

This method creates the necessary tables in the Postgres database if they don't already exist

and runs database migrations. It MUST be called directly by the user the  rst time

checkpointer is used.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( RunnableConfig ) – The con g to use for listing the checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata. Defaults to None.

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – The maximum number of checkpoints to return.

Defaults to None.

Yields:

CheckpointTuple  – Iterator[CheckpointTuple]: An iterator of checkpoint tuples.

Examples:

>>> from langgraph.checkpoint.postgres import PostgresSaver
>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?
sslmode=disable"
>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
... # Run a graph, then list the checkpoints
>>>
>>>
>>> print(checkpoints)
[CheckpointTuple(...), CheckpointTuple(...)]

config = {"configurable": {"thread_id": "1"}}
checkpoints = list(memory.list(config, limit=2))

>>> config = {"configurable": {"thread_id": "1"}}
>>> before = {"configurable": {"checkpoint_id": "1ef4f797-8335-6428-8001-
8a1503f9b875"}}

https://langchain-ai.github.io/langgraph/reference/checkpoints/

42/54

1/11/25, 3:50 PM

Checkpointing

>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
... # Run a graph, then list the checkpoints
>>>
>>> print(checkpoints)
[CheckpointTuple(...), ...]

checkpoints = list(memory.list(config, before=before))

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and timestamp is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

Examples:

Basic:
>>> config = {"configurable": {"thread_id": "1"}}
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

With timestamp:

>>> config = {
...    "configurable": {
...        "thread_id": "1",
...        "checkpoint_ns": "",
...        "checkpoint_id": "1ef4f797-8335-6428-8001-8a1503f9b875",
...    }
... }
>>> checkpoint_tuple = memory.get_tuple(config)
>>> print(checkpoint_tuple)
CheckpointTuple(...)

https://langchain-ai.github.io/langgraph/reference/checkpoints/

43/54

1/11/25, 3:50 PM

Checkpointing

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g and its parent con g (if any).

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

Examples:

>>> from langgraph.checkpoint.postgres import PostgresSaver
>>> DB_URI = "postgres://postgres:postgres@localhost:5432/postgres?
sslmode=disable"
>>> with PostgresSaver.from_conn_string(DB_URI) as memory:
>>>     config = {"configurable": {"thread_id": "1", "checkpoint_ns": ""}}
>>>     checkpoint = {"ts": "2024-05-04T06:32:42.235444+00:00", "id": "1ef4f797-
8335-6428-8001-8a1503f9b875", "channel_values": {"key": "value"}}
>>>     saved_config = memory.put(config, checkpoint, {"source": "input", "step":
1, "writes": {"key": "value"}}, {})
>>> print(saved_config)
{'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id':
'1ef4f797-8335-6428-8001-8a1503f9b875'}}

meth   put_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the Postgres database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

44/54

1/11/25, 3:50 PM

Checkpointing

writes  ( List[Tuple[str, Any]] ) – List of writes to store.

task_id  ( str ) – Identi er for the task creating the writes.

class AsyncShallowPostgresSaver

Bases:  BasePostgresSaver

A checkpoint saver that uses Postgres to store checkpoints asynchronously.

This checkpointer ONLY stores the most recent checkpoint and does NOT retain any history. It

is meant to be a light-weight drop-in replacement for the AsyncPostgresSaver that supports

most of the LangGraph persistence functionality with the exception of time travel.

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

45/54

propertyasync1/11/25, 3:50 PM

Checkpointing

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   from_conn_string(conn_string: str, *, pipeline: bool = False,
serde: Optional[SerializerProtocol] = None) ->

AsyncIterator[AsyncShallowPostgresSaver]

Create a new AsyncShallowPostgresSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The Postgres connection info string.

pipeline  ( bool , default:  False  ) – whether to use AsyncPipeline

Returns:

AsyncShallowPostgresSaver  (  AsyncIterator[AsyncShallowPostgresSaver]  ) – A new

AsyncShallowPostgresSaver instance.

meth   setup() -> None

Set up the checkpoint database asynchronously.

This method creates the necessary tables in the Postgres database if they don't already exist

and runs database migrations. It MUST be called directly by the user the  rst time

checkpointer is used.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. For ShallowPostgresSaver, this method returns a list with ONLY the most

recent checkpoint.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

46/54

asyncclassmethodasyncasync
1/11/25, 3:50 PM

Checkpointing

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g (matching the thread ID in the con g).

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g. For AsyncShallowPostgresSaver, this method saves ONLY the most recent

checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   aput_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint asynchronously.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

47/54

asyncasyncasync1/11/25, 3:50 PM

Checkpointing

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. For ShallowPostgresSaver, this method returns a list with ONLY the most

recent checkpoint.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g (matching the thread ID in the con g).

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g. For AsyncShallowPostgresSaver, this method saves ONLY the most recent

https://langchain-ai.github.io/langgraph/reference/checkpoints/

48/54

1/11/25, 3:50 PM

Checkpointing

checkpoint and overwrites a previous checkpoint, if it exists.

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   put_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

class AsyncPostgresSaver

Bases:  BasePostgresSaver

attr   config_specs: list[ConfigurableFieldSpec]

De ne the con guration options for the checkpoint saver.

Returns:

list[ConfigurableFieldSpec]  – list[Con gurableFieldSpec]: List of con guration  eld

specs.

meth   get(config: RunnableConfig) -> Optional[Checkpoint]

https://langchain-ai.github.io/langgraph/reference/checkpoints/

49/54

property1/11/25, 3:50 PM

Checkpointing

Fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   aget(config: RunnableConfig) -> Optional[Checkpoint]

Asynchronously fetch a checkpoint using the given con guration.

Parameters:

config  ( RunnableConfig ) – Con guration specifying which checkpoint to retrieve.

Returns:

Optional[Checkpoint]  – Optional[Checkpoint]: The requested checkpoint, or None if not

found.

meth   from_conn_string(conn_string: str, *, pipeline: bool = False,
serde: Optional[SerializerProtocol] = None) ->

AsyncIterator[AsyncPostgresSaver]

Create a new AsyncPostgresSaver instance from a connection string.

Parameters:

conn_string  ( str ) – The Postgres connection info string.

pipeline  ( bool , default:  False  ) – whether to use AsyncPipeline

Returns:

AsyncPostgresSaver  (  AsyncIterator[AsyncPostgresSaver]  ) – A new AsyncPostgresSaver

instance.

meth   setup() -> None

Set up the checkpoint database asynchronously.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

50/54

asyncasyncclassmethodasync
1/11/25, 3:50 PM

Checkpointing

This method creates the necessary tables in the Postgres database if they don't already exist

and runs database migrations. It MUST be called directly by the user the  rst time

checkpointer is used.

meth   alist(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> AsyncIterator[CheckpointTuple]

List checkpoints from the database asynchronously.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Yields:

AsyncIterator[CheckpointTuple]  – AsyncIterator[CheckpointTuple]: An asynchronous

iterator of matching checkpoint tuples.

meth   aget_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database asynchronously.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and "checkpoint_id" is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

Parameters:

https://langchain-ai.github.io/langgraph/reference/checkpoints/

51/54

asyncasync1/11/25, 3:50 PM

Checkpointing

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

meth   aput(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database asynchronously.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g and its parent con g (if any).

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   aput_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint asynchronously.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

52/54

asyncasync1/11/25, 3:50 PM

Checkpointing

meth   list(config: Optional[RunnableConfig], *, filter:
Optional[dict[str, Any]] = None, before: Optional[RunnableConfig] =

None, limit: Optional[int] = None) -> Iterator[CheckpointTuple]

List checkpoints from the database.

This method retrieves a list of checkpoint tuples from the Postgres database based on the

provided con g. The checkpoints are ordered by checkpoint ID in descending order (newest

 rst).

Parameters:

config  ( Optional[RunnableConfig] ) – Base con guration for  ltering checkpoints.

filter  ( Optional[Dict[str, Any]] , default:  None  ) – Additional  ltering criteria for

metadata.

before  ( Optional[RunnableConfig] , default:  None  ) – If provided, only checkpoints before

the speci ed checkpoint ID are returned. Defaults to None.

limit  ( Optional[int] , default:  None  ) – Maximum number of checkpoints to return.

Yields:

CheckpointTuple  – Iterator[CheckpointTuple]: An iterator of matching checkpoint tuples.

meth   get_tuple(config: RunnableConfig) -> Optional[CheckpointTuple]

Get a checkpoint tuple from the database.

This method retrieves a checkpoint tuple from the Postgres database based on the provided

con g. If the con g contains a "checkpoint_id" key, the checkpoint with the matching thread ID

and "checkpoint_id" is retrieved. Otherwise, the latest checkpoint for the given thread ID is

retrieved.

Parameters:

config  ( RunnableConfig ) – The con g to use for retrieving the checkpoint.

Returns:

Optional[CheckpointTuple]  – Optional[CheckpointTuple]: The retrieved checkpoint tuple,

or None if no matching checkpoint was found.

https://langchain-ai.github.io/langgraph/reference/checkpoints/

53/54

1/11/25, 3:50 PM

Checkpointing

meth   put(config: RunnableConfig, checkpoint: Checkpoint, metadata:
CheckpointMetadata, new_versions: ChannelVersions) -> RunnableConfig

Save a checkpoint to the database.

This method saves a checkpoint to the Postgres database. The checkpoint is associated with

the provided con g and its parent con g (if any).

Parameters:

config  ( RunnableConfig ) – The con g to associate with the checkpoint.

checkpoint  ( Checkpoint ) – The checkpoint to save.

metadata  ( CheckpointMetadata ) – Additional metadata to save with the checkpoint.

new_versions  ( ChannelVersions ) – New channel versions as of this write.

Returns:

RunnableConfig  (  RunnableConfig  ) – Updated con guration after storing the checkpoint.

meth   put_writes(config: RunnableConfig, writes: Sequence[tuple[str,
Any]], task_id: str) -> None

Store intermediate writes linked to a checkpoint.

This method saves intermediate writes associated with a checkpoint to the database.

Parameters:

config  ( RunnableConfig ) – Con guration of the related checkpoint.

writes  ( Sequence[Tuple[str, Any]] ) – List of writes to store, each as (channel, value) pair.

task_id  ( str ) – Identi er for the task creating the writes.