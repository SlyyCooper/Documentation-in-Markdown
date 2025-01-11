---
title: Www.Selenium.Dev 20250105 151113
type: reference
---

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.chrome.service¶](#seleniumwebdriverchromeservice)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.service

# selenium.webdriver.chrome.service¶

Classes

`Service`([executable_path, port, ...]) | A Service class that is responsible for the starting and stopping of chromedriver.  
---|---  
  
_class _selenium.webdriver.chrome.service.Service(_executable_path =None_, _port : int = 0_, _service_args : List[str] | None = None_, _log_output : int | str | IO[Any] | None = None_, _env : Mapping[str, str] | None = None_, _** kwargs_)[source]¶
    

A Service class that is responsible for the starting and stopping of
chromedriver.

Parameters:

    

  * **executable_path** – install path of the chromedriver executable, defaults to chromedriver.

  * **port** – Port for the service to run on, defaults to 0 where the operating system will decide.

  * **service_args** – (Optional) List of args to be passed to the subprocess when launching the executable.

  * **log_output** – (Optional) int representation of STDOUT/DEVNULL, any IO instance or String path to file.

  * **env** – (Optional) Mapping of environment variables for the new process, defaults to os.environ.

assert_process_still_running() → None[source]¶

    

Check if the underlying process is still running.

command_line_args() → List[str]¶

    

A List of program arguments (excluding the executable).

is_connectable() → bool[source]¶

    

Establishes a socket connection to determine if the service running on the
port is accessible.

_property _path _: str_¶

    

send_remote_shutdown_command() → None[source]¶

    

Dispatch an HTTP request to the shutdown endpoint for the service in an
attempt to stop it.

_property _service_url _: str_¶

    

Gets the url of the Service.

start() → None[source]¶

    

Starts the Service.

Exceptions:

    

  * WebDriverException : Raised either when it can’t start the service or when it can’t connect to the service

stop() → None[source]¶

    

Stops the service.

### Table of Contents

  * selenium.webdriver.chrome.service
    * `Service`
      * `Service.assert_process_still_running()`
      * `Service.command_line_args()`
      * `Service.is_connectable()`
      * `Service.path`
      * `Service.send_remote_shutdown_command()`
      * `Service.service_url`
      * `Service.start()`
      * `Service.stop()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.service

© Copyright 2009-2024 Software Freedom Conservancy.