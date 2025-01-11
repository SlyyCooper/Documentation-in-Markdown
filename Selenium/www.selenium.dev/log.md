## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.log¶](#seleniumwebdrivercommonlog)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.log

# selenium.webdriver.common.log¶

Functions

`import_cdp`() |   
---|---  
  
Classes

`Log`(driver, bidi_session) | This class allows access to logging APIs that use the new WebDriver Bidi protocol.  
---|---  
  
selenium.webdriver.common.log.import_cdp()[source]¶

    

_class _selenium.webdriver.common.log.Log(_driver_ , _bidi_session_)[source]¶

    

This class allows access to logging APIs that use the new WebDriver Bidi
protocol.

This class is not to be used directly and should be used from the webdriver
base classes.

mutation_events() -> AsyncGenerator[Dict[str, Any], None][source]¶

    

Listen for mutation events and emit them as they are found.

Usage:

    
    
    
    async with driver.log.mutation_events() as event:
         pages.load("dynamic.html")
         driver.find_element(By.ID, "reveal").click()
         WebDriverWait(driver, 5)                        .until(EC.visibility_of(driver.find_element(By.ID, "revealed")))
    
     assert event["attribute_name"] == "style"
     assert event["current_value"] == ""
     assert event["old_value"] == "display:none;"
    

add_js_error_listener() -> AsyncGenerator[Dict[str, Any], None][source]¶

    

Listen for JS errors and when the contextmanager exits check if there were JS
Errors.

Usage:

    
    
    
    async with driver.log.add_js_error_listener() as error:
        driver.find_element(By.ID, "throwing-mouseover").click()
    assert bool(error)
    assert error.exception_details.stack_trace.call_frames[0].function_name == "onmouseover"
    

add_listener(_event_type_) -> AsyncGenerator[Dict[str, Any], None][source]¶

    

Listen for certain events that are passed in.

Args:

    

  * event_type: The type of event that we want to look at.

Usage:

    
    
    
    async with driver.log.add_listener(Console.log) as messages:
        driver.execute_script("console.log('I like cheese')")
    assert messages["message"] == "I love cheese"
    

### Table of Contents

  * selenium.webdriver.common.log
    * `import_cdp()`
    * `Log`
      * `Log.mutation_events()`
      * `Log.add_js_error_listener()`
      * `Log.add_listener()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.log

(C) Copyright 2009-2024 Software Freedom Conservancy.