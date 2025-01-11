## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.service](#seleniumwebdrivercommonservice)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.service

# selenium.webdriver.common.service

Classes

`Service`([executable_path, port, log_output, env]) | The abstract base class for all service objects.  
---|---  
  
_class _selenium.webdriver.common.service.Service(_executable_path : str | None = None_, _port : int = 0_, _log_output : int | str | IO[Any] | None = None_, _env : Mapping[Any, Any] | None = None_, _** kwargs_)[source]
    

The abstract base class for all service objects. Services typically launch a
child program in a new process as an interim process to communicate with a
browser.

Parameters:

    

  * **executable** – install path of the executable.

  * **port** – Port for the service to run on, defaults to 0 where the operating system will decide.

  * **log_output** – (Optional) int representation of STDOUT/DEVNULL, any IO instance or String path to file.

  * **env** – (Optional) Mapping of environment variables for the new process, defaults to os.environ.

_property _service_url _: str_

    

Gets the url of the Service.

_abstract _command_line_args() -> List[str][source]

    

A List of program arguments (excluding the executable).

_property _path _: str_

    

start() -> None[source]

    

Starts the Service.

Exceptions:

    

  * WebDriverException : Raised either when it can’t start the service or when it can’t connect to the service

assert_process_still_running() -> None[source]

    

Check if the underlying process is still running.

is_connectable() -> bool[source]

    

Establishes a socket connection to determine if the service running on the
port is accessible.

send_remote_shutdown_command() -> None[source]

    

Dispatch an HTTP request to the shutdown endpoint for the service in an
attempt to stop it.

stop() -> None[source]

    

Stops the service.

### Table of Contents

  * selenium.webdriver.common.service
    * `Service`
      * `Service.service_url`
      * `Service.command_line_args()`
      * `Service.path`
      * `Service.start()`
      * `Service.assert_process_still_running()`
      * `Service.is_connectable()`
      * `Service.send_remote_shutdown_command()`
      * `Service.stop()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.service

(C) Copyright 2009-2024 Software Freedom Conservancy.