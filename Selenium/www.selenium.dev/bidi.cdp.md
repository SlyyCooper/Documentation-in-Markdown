## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.cdp¶](#seleniumwebdrivercommonbidicdp)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.cdp

# selenium.webdriver.common.bidi.cdp¶

Functions

`connect_cdp`(nursery, url) | Connect to the browser specified by `url` and spawn a background task in the specified nursery.  
---|---  
`connection_context`(connection) | This context manager installs `connection` as the session context for the current Trio task.  
`get_connection_context`(fn_name) | Look up the current connection.  
`get_session_context`(fn_name) | Look up the current session.  
`import_devtools`(ver) | Attempt to load the current latest available devtools into the module cache for use later.  
`open_cdp`(url) | This async context manager opens a connection to the browser specified by `url` before entering the block, then closes the connection when the block exits.  
`session_context`(session) | This context manager installs `session` as the session context for the current Trio task.  
`set_global_connection`(connection) | Install `connection` in the root context so that it will become the default connection for all tasks.  
`set_global_session`(session) | Install `session` in the root context so that it will become the default session for all tasks.  
  
Classes

`CdpBase`(ws, session_id, target_id) |   
---|---  
`CdpConnection`(ws) | Contains the connection state for a Chrome DevTools Protocol server.  
`CdpSession`(ws, session_id, target_id) | Contains the state for a CDP session.  
`CmEventProxy`([value]) | A proxy object returned by `CdpBase.wait_for()`()`.  
  
Exceptions

`BrowserError`(obj) | This exception is raised when the browser's response to a command indicates that an error occurred.  
---|---  
`CdpConnectionClosed`(reason) | Raised when a public method is called on a closed CDP connection.  
`InternalError` | This exception is only raised when there is faulty logic in TrioCDP or the integration with PyCDP.  
  
selenium.webdriver.common.bidi.cdp.import_devtools(_ver_)[source]¶

    

Attempt to load the current latest available devtools into the module cache
for use later.

selenium.webdriver.common.bidi.cdp.get_connection_context(_fn_name_)[source]¶

    

Look up the current connection.

If there is no current connection, raise a `RuntimeError` with a helpful
message.

selenium.webdriver.common.bidi.cdp.get_session_context(_fn_name_)[source]¶

    

Look up the current session.

If there is no current session, raise a `RuntimeError` with a helpful message.

selenium.webdriver.common.bidi.cdp.connection_context(_connection_)[source]¶

    

This context manager installs `connection` as the session context for the
current Trio task.

selenium.webdriver.common.bidi.cdp.session_context(_session_)[source]¶

    

This context manager installs `session` as the session context for the current
Trio task.

selenium.webdriver.common.bidi.cdp.set_global_connection(_connection_)[source]¶

    

Install `connection` in the root context so that it will become the default
connection for all tasks.

This is generally not recommended, except it may be necessary in certain use
cases such as running inside Jupyter notebook.

selenium.webdriver.common.bidi.cdp.set_global_session(_session_)[source]¶

    

Install `session` in the root context so that it will become the default
session for all tasks.

This is generally not recommended, except it may be necessary in certain use
cases such as running inside Jupyter notebook.

_exception _selenium.webdriver.common.bidi.cdp.BrowserError(_obj_)[source]¶

    

This exception is raised when the browser’s response to a command indicates
that an error occurred.

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_exception
_selenium.webdriver.common.bidi.cdp.CdpConnectionClosed(_reason_)[source]¶

    

Raised when a public method is called on a closed CDP connection.

Constructor.

Parameters:

    

**reason** (_wsproto.frame_protocol.CloseReason_) –

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_exception _selenium.webdriver.common.bidi.cdp.InternalError[source]¶

    

This exception is only raised when there is faulty logic in TrioCDP or the
integration with PyCDP.

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_class _selenium.webdriver.common.bidi.cdp.CmEventProxy(_value : Any | None = None_)[source]¶
    

A proxy object returned by `CdpBase.wait_for()`()`.

After the context manager executes, this proxy object will have a value set
that contains the returned event.

value _: Any_ _ = None_¶

    

_class _selenium.webdriver.common.bidi.cdp.CdpBase(_ws_ , _session_id_ ,
_target_id_)[source]¶

    

_async _execute(_cmd : Generator[dict, T, Any]_) -> T[source]¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)[source]¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None][source]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

_class _selenium.webdriver.common.bidi.cdp.CdpSession(_ws_ , _session_id_ ,
_target_id_)[source]¶

    

Contains the state for a CDP session.

Generally you should not instantiate this object yourself; you should call
`CdpConnection.open_session()`.

Constructor.

Parameters:

    

  * **ws** (_trio_websocket.WebSocketConnection_) – 

  * **session_id** (_devtools.target.SessionID_) – 

  * **target_id** (_devtools.target.TargetID_) – 

dom_enable()[source]¶

    

A context manager that executes `dom.enable()` when it enters and then calls
`dom.disable()`.

This keeps track of concurrent callers and only disables DOM events when all
callers have exited.

page_enable()[source]¶

    

A context manager that executes `page.enable()` when it enters and then calls
`page.disable()` when it exits.

This keeps track of concurrent callers and only disables page events when all
callers have exited.

_async _execute(_cmd : Generator[dict, T, Any]_) -> T¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

_class _selenium.webdriver.common.bidi.cdp.CdpConnection(_ws_)[source]¶

    

Contains the connection state for a Chrome DevTools Protocol server.

CDP can multiplex multiple “sessions” over a single connection. This class
corresponds to the “root” session, i.e. the implicitly created session that
has no session ID. This class is responsible for reading incoming WebSocket
messages and forwarding them to the corresponding session, as well as handling
messages targeted at the root session itself. You should generally call the
`open_cdp()` instead of instantiating this class directly.

Constructor.

Parameters:

    

**ws** (_trio_websocket.WebSocketConnection_) –

_async _aclose()[source]¶

    

Close the underlying WebSocket connection.

This will cause the reader task to gracefully exit when it tries to read the
next message from the WebSocket. All of the public APIs (`execute()`,
`listen()`, etc.) will raise `CdpConnectionClosed` after the CDP connection is
closed. It is safe to call this multiple times.

open_session(_target_id_) -> AsyncIterator[CdpSession][source]¶

    

This context manager opens a session and enables the “simple” style of calling
CDP APIs.

For example, inside a session context, you can call `await dom.get_document()`
and it will execute on the current session automatically.

_async _connect_session(_target_id_) -> CdpSession[source]¶

    

Returns a new `CdpSession` connected to the specified target.

_async _execute(_cmd : Generator[dict, T, Any]_) -> T¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

selenium.webdriver.common.bidi.cdp.open_cdp(_url_) ->
AsyncIterator[CdpConnection][source]¶

    

This async context manager opens a connection to the browser specified by
`url` before entering the block, then closes the connection when the block
exits.

The context manager also sets the connection as the default connection for the
current task, so that commands like `await target.get_targets()` will run on
this connection automatically. If you want to use multiple connections
concurrently, it is recommended to open each on in a separate task.

_async _selenium.webdriver.common.bidi.cdp.connect_cdp(_nursery_ , _url_) ->
CdpConnection[source]¶

    

Connect to the browser specified by `url` and spawn a background task in the
specified nursery.

The `open_cdp()` context manager is preferred in most situations. You should
only use this function if you need to specify a custom nursery. This
connection is not automatically closed! You can either use the connection
object as a context manager (`async with conn:`) or else call `await
conn.aclose()` on it when you are done with it. If `set_context` is True, then
the returned connection will be installed as the default connection for the
current task. This argument is for unusual use cases, such as running inside
of a notebook.

### Table of Contents

  * selenium.webdriver.common.bidi.cdp
    * `import_devtools()`
    * `get_connection_context()`
    * `get_session_context()`
    * `connection_context()`
    * `session_context()`
    * `set_global_connection()`
    * `set_global_session()`
    * `BrowserError`
      * `BrowserError.args`
      * `BrowserError.with_traceback()`
    * `CdpConnectionClosed`
      * `CdpConnectionClosed.args`
      * `CdpConnectionClosed.with_traceback()`
    * `InternalError`
      * `InternalError.args`
      * `InternalError.with_traceback()`
    * `CmEventProxy`
      * `CmEventProxy.value`
    * `CdpBase`
      * `CdpBase.execute()`
      * `CdpBase.listen()`
      * `CdpBase.wait_for()`
    * `CdpSession`
      * `CdpSession.dom_enable()`
      * `CdpSession.page_enable()`
      * `CdpSession.execute()`
      * `CdpSession.listen()`
      * `CdpSession.wait_for()`
    * `CdpConnection`
      * `CdpConnection.aclose()`
      * `CdpConnection.open_session()`
      * `CdpConnection.connect_session()`
      * `CdpConnection.execute()`
      * `CdpConnection.listen()`
      * `CdpConnection.wait_for()`
    * `open_cdp()`
    * `connect_cdp()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.cdp

(C) Copyright 2009-2024 Software Freedom Conservancy.