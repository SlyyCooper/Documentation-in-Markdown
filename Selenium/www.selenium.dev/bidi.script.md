## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.script](#seleniumwebdrivercommonbidiscript)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.script

# selenium.webdriver.common.bidi.script

Classes

`ConsoleLogEntry`(level, text, timestamp, ...) |   
---|---  
`JavaScriptLogEntry`(level, text, timestamp, ...) |   
`LogEntryAdded`() |   
`Script`(conn) |   
  
_class _selenium.webdriver.common.bidi.script.Script(_conn_)[source]

    

add_console_message_handler(_handler_)[source]

    

add_javascript_error_handler(_handler_)[source]

    

remove_console_message_handler(_id_)[source]

    

remove_javascript_error_handler(_id_)

    

_class _selenium.webdriver.common.bidi.script.LogEntryAdded[source]

    

event_class _ = 'log.entryAdded'_

    

_classmethod _from_json(_json_)[source]

    

_class _selenium.webdriver.common.bidi.script.ConsoleLogEntry(_level : str_,
_text : str_, _timestamp : str_, _method : str_, _args : List[dict]_, _type_ :
str_)[source]

    

level _: str_

    

text _: str_

    

timestamp _: str_

    

method _: str_

    

args _: List[dict]_

    

type__: str_

    

_classmethod _from_json(_json_)[source]

    

_class _selenium.webdriver.common.bidi.script.JavaScriptLogEntry(_level :
str_, _text : str_, _timestamp : str_, _stacktrace : dict_, _type_ :
str_)[source]

    

level _: str_

    

text _: str_

    

timestamp _: str_

    

stacktrace _: dict_

    

type__: str_

    

_classmethod _from_json(_json_)[source]

    

### Table of Contents

  * selenium.webdriver.common.bidi.script
    * `Script`
      * `Script.add_console_message_handler()`
      * `Script.add_javascript_error_handler()`
      * `Script.remove_console_message_handler()`
      * `Script.remove_javascript_error_handler()`
    * `LogEntryAdded`
      * `LogEntryAdded.event_class`
      * `LogEntryAdded.from_json()`
    * `ConsoleLogEntry`
      * `ConsoleLogEntry.level`
      * `ConsoleLogEntry.text`
      * `ConsoleLogEntry.timestamp`
      * `ConsoleLogEntry.method`
      * `ConsoleLogEntry.args`
      * `ConsoleLogEntry.type_`
      * `ConsoleLogEntry.from_json()`
    * `JavaScriptLogEntry`
      * `JavaScriptLogEntry.level`
      * `JavaScriptLogEntry.text`
      * `JavaScriptLogEntry.timestamp`
      * `JavaScriptLogEntry.stacktrace`
      * `JavaScriptLogEntry.type_`
      * `JavaScriptLogEntry.from_json()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.script

(C) Copyright 2009-2024 Software Freedom Conservancy.