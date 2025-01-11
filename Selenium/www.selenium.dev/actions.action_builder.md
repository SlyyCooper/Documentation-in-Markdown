## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.action_builder](#seleniumwebdrivercommonactionsaction_builder)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.action_builder

# selenium.webdriver.common.actions.action_builder

Classes

`ActionBuilder`(driver[, mouse, wheel, ...]) |   
---|---  
  
_class _selenium.webdriver.common.actions.action_builder.ActionBuilder(_driver_ , _mouse : PointerInput | None = None_, _wheel : WheelInput | None = None_, _keyboard : KeyInput | None = None_, _duration : int = 250_)[source]
    

get_device_with(_name : str_) -> WheelInput | PointerInput | KeyInput | None[source]
    

_property _pointer_inputs _: List[PointerInput]_

    

_property _key_inputs _: List[KeyInput]_

    

_property _key_action _: KeyActions_

    

_property _pointer_action _: PointerActions_

    

_property _wheel_action _: WheelActions_

    

add_key_input(_name : str_) -> KeyInput[source]

    

add_pointer_input(_kind : str_, _name : str_) -> PointerInput[source]

    

add_wheel_input(_name : str_) -> WheelInput[source]

    

perform() -> None[source]

    

clear_actions() -> None[source]

    

Clears actions that are already stored on the remote end.

### Table of Contents

  * selenium.webdriver.common.actions.action_builder
    * `ActionBuilder`
      * `ActionBuilder.get_device_with()`
      * `ActionBuilder.pointer_inputs`
      * `ActionBuilder.key_inputs`
      * `ActionBuilder.key_action`
      * `ActionBuilder.pointer_action`
      * `ActionBuilder.wheel_action`
      * `ActionBuilder.add_key_input()`
      * `ActionBuilder.add_pointer_input()`
      * `ActionBuilder.add_wheel_input()`
      * `ActionBuilder.perform()`
      * `ActionBuilder.clear_actions()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.action_builder

(C) Copyright 2009-2024 Software Freedom Conservancy.