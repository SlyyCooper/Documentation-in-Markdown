## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.wheel_input](#seleniumwebdrivercommonactionswheel_input)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.wheel_input

# selenium.webdriver.common.actions.wheel_input

Classes

`ScrollOrigin`(origin, x_offset, y_offset) |   
---|---  
`WheelInput`(name) |   
  
_class _selenium.webdriver.common.actions.wheel_input.ScrollOrigin(_origin : str | WebElement_, _x_offset : int_, _y_offset : int_)[source]
    

_classmethod _from_element(_element : WebElement_, _x_offset : int = 0_,
_y_offset : int = 0_)[source]

    

_classmethod _from_viewport(_x_offset : int = 0_, _y_offset : int =
0_)[source]

    

_property _origin _: str | WebElement_
    

_property _x_offset _: int_

    

_property _y_offset _: int_

    

_class
_selenium.webdriver.common.actions.wheel_input.WheelInput(_name_)[source]

    

encode() -> dict[source]

    

create_scroll(_x : int_, _y : int_, _delta_x : int_, _delta_y : int_,
_duration : int_, _origin_) -> None[source]

    

create_pause(_pause_duration : int | float = 0_) -> None[source]
    

add_action(_action : Any_) -> None

    

clear_actions() -> None

    

### Table of Contents

  * selenium.webdriver.common.actions.wheel_input
    * `ScrollOrigin`
      * `ScrollOrigin.from_element()`
      * `ScrollOrigin.from_viewport()`
      * `ScrollOrigin.origin`
      * `ScrollOrigin.x_offset`
      * `ScrollOrigin.y_offset`
    * `WheelInput`
      * `WheelInput.encode()`
      * `WheelInput.create_scroll()`
      * `WheelInput.create_pause()`
      * `WheelInput.add_action()`
      * `WheelInput.clear_actions()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.wheel_input

(C) Copyright 2009-2024 Software Freedom Conservancy.