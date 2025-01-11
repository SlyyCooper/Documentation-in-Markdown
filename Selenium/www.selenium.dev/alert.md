## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.alert](#seleniumwebdrivercommonalert)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.alert

# selenium.webdriver.common.alert

The Alert implementation.

Classes

`Alert`(driver) | Allows to work with alerts.  
---|---  
  
_class _selenium.webdriver.common.alert.Alert(_driver_)[source]

    

Allows to work with alerts.

Use this class to interact with alert prompts. It contains methods for
dismissing, accepting, inputting, and getting text from alert prompts.

Accepting / Dismissing alert prompts:

    
    
    Alert(driver).accept()
    Alert(driver).dismiss()
    

Inputting a value into an alert prompt:

    
    
    name_prompt = Alert(driver)
    name_prompt.send_keys("Willian Shakesphere")
    name_prompt.accept()
    

Reading a the text of a prompt for verification:

    
    
    alert_text = Alert(driver).text
    self.assertEqual("Do you wish to quit?", alert_text)
    

Creates a new Alert.

Args:

    

  * driver: The WebDriver instance which performs user actions.

_property _text _: str_

    

Gets the text of the Alert.

dismiss() -> None[source]

    

Dismisses the alert available.

accept() -> None[source]

    

Accepts the alert available.

Usage:

    
    
    
    Alert(driver).accept() # Confirm a alert dialog.
    

send_keys(_keysToSend : str_) -> None[source]

    

Send Keys to the Alert.

Args:

    

  * keysToSend: The text to be sent to Alert.

### Table of Contents

  * selenium.webdriver.common.alert
    * `Alert`
      * `Alert.text`
      * `Alert.dismiss()`
      * `Alert.accept()`
      * `Alert.send_keys()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.alert

(C) Copyright 2009-2024 Software Freedom Conservancy.