## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.utils¶](#seleniumwebdrivercommonutils)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.utils

# selenium.webdriver.common.utils¶

The Utils methods.

Functions

`find_connectable_ip`(host[, port]) | Resolve a hostname to an IP, preferring IPv4 addresses.  
---|---  
`free_port`() | Determines a free port using sockets.  
`is_connectable`(port[, host]) | Tries to connect to the server at port to see if it is running.  
`is_url_connectable`(port) | Tries to connect to the HTTP server at /status path and specified port to see if it responds successfully.  
`join_host_port`(host, port) | Joins a hostname and port together.  
`keys_to_typing`(value) | Processes the values that will be typed in the element.  
  
selenium.webdriver.common.utils.free_port() -> int[source]¶

    

Determines a free port using sockets.

selenium.webdriver.common.utils.find_connectable_ip(_host : str | bytes | bytearray | None_, _port : int | None = None_) -> str | None[source]¶
    

Resolve a hostname to an IP, preferring IPv4 addresses.

We prefer IPv4 so that we don’t change behavior from previous IPv4-only
implementations, and because some drivers (e.g., FirefoxDriver) do not support
IPv6 connections.

If the optional port number is provided, only IPs that listen on the given
port are considered.

Args:

    

  * host - A hostname.

  * port - Optional port number.

Returns:

    

A single IP address, as a string. If any IPv4 address is found, one is
returned. Otherwise, if any IPv6 address is found, one is returned. If
neither, then None is returned.

selenium.webdriver.common.utils.join_host_port(_host : str_, _port : int_) ->
str[source]¶

    

Joins a hostname and port together.

This is a minimal implementation intended to cope with IPv6 literals. For
example, _join_host_port(‘::1’, 80) == ‘[::1]:80’.

Args:

    

  * host - A hostname.

  * port - An integer port.

selenium.webdriver.common.utils.is_connectable(_port : int_, _host : str | None = 'localhost'_) -> bool[source]¶
    

Tries to connect to the server at port to see if it is running.

Args:

    

  * port - The port to connect.

selenium.webdriver.common.utils.is_url_connectable(_port : int | str_) -> bool[source]¶
    

Tries to connect to the HTTP server at /status path and specified port to see
if it responds successfully.

Args:

    

  * port - The port to connect.

selenium.webdriver.common.utils.keys_to_typing(_value : Iterable[str | int | float]_) -> List[str][source]¶
    

Processes the values that will be typed in the element.

### Table of Contents

  * selenium.webdriver.common.utils
    * `free_port()`
    * `find_connectable_ip()`
    * `join_host_port()`
    * `is_connectable()`
    * `is_url_connectable()`
    * `keys_to_typing()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.utils

(C) Copyright 2009-2024 Software Freedom Conservancy.