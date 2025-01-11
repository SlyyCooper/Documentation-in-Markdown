## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.timeouts¶](#seleniumwebdrivercommontimeouts)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.timeouts

# selenium.webdriver.common.timeouts¶

Classes

`Timeouts`([implicit_wait, page_load, script]) | Create a new Timeouts object.  
---|---  
  
_class _selenium.webdriver.common.timeouts.Timeouts(_implicit_wait : float =
0_, _page_load : float = 0_, _script : float = 0_)[source]¶

    

Create a new Timeouts object.

This implements https://w3c.github.io/webdriver/#timeouts.

Args:

    

  * implicit_wait - Either an int or a float. Set how many
    

seconds to wait when searching for elements before throwing an error.

  * page_load - Either an int or a float. Set how many seconds
    

to wait for a page load to complete before throwing an error.

  * script - Either an int or a float. Set how many seconds to
    

wait for an asynchronous script to finish execution before throwing an error.

implicit_wait¶

    

Get or set how many seconds to wait when searching for elements.

This does not set the value on the remote end.

## Usage¶

  * Get
    
    * self.implicit_wait

  * Set
    
    * self.implicit_wait = value

## Parameters¶

value: float

page_load¶

    

Get or set how many seconds to wait for the page to load.

This does not set the value on the remote end.

## Usage¶

  * Get
    
    * self.page_load

  * Set
    
    * self.page_load = value

## Parameters¶

value: float

script¶

    

Get or set how many seconds to wait for an asynchronous script to finish
execution.

This does not set the value on the remote end.

## Usage¶

  * Get
    
    * self.script

  * Set
    
    * self.script = value

## Parameters¶

value: float

### Table of Contents

  * selenium.webdriver.common.timeouts
    * `Timeouts`
      * `Timeouts.implicit_wait`
      * `Timeouts.page_load`
      * `Timeouts.script`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.timeouts

(C) Copyright 2009-2024 Software Freedom Conservancy.