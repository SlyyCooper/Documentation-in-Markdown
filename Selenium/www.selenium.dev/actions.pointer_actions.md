## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.pointer_actions¶](#seleniumwebdrivercommonactionspointer_actions)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.pointer_actions

# selenium.webdriver.common.actions.pointer_actions¶

Classes

`PointerActions`([source, duration]) | Args: - source: PointerInput instance - duration: override the default 250 msecs of DEFAULT_MOVE_DURATION in source  
---|---  
  
_class _selenium.webdriver.common.actions.pointer_actions.PointerActions(_source : PointerInput | None = None_, _duration : int = 250_)[source]¶
    

Args: \- source: PointerInput instance \- duration: override the default 250
msecs of DEFAULT_MOVE_DURATION in source

pointer_down(_button =0_, _width =None_, _height =None_, _pressure =None_,
_tangential_pressure =None_, _tilt_x =None_, _tilt_y =None_, _twist =None_,
_altitude_angle =None_, _azimuth_angle =None_)[source]¶

    

pointer_up(_button =0_)[source]¶

    

move_to(_element_ , _x =0_, _y =0_, _width =None_, _height =None_, _pressure
=None_, _tangential_pressure =None_, _tilt_x =None_, _tilt_y =None_, _twist
=None_, _altitude_angle =None_, _azimuth_angle =None_)[source]¶

    

move_by(_x_ , _y_ , _width =None_, _height =None_, _pressure =None_,
_tangential_pressure =None_, _tilt_x =None_, _tilt_y =None_, _twist =None_,
_altitude_angle =None_, _azimuth_angle =None_)[source]¶

    

move_to_location(_x_ , _y_ , _width =None_, _height =None_, _pressure =None_,
_tangential_pressure =None_, _tilt_x =None_, _tilt_y =None_, _twist =None_,
_altitude_angle =None_, _azimuth_angle =None_)[source]¶

    

click(_element : WebElement | None = None_, _button =0_)[source]¶
    

context_click(_element : WebElement | None = None_)[source]¶
    

click_and_hold(_element : WebElement | None = None_, _button =0_)[source]¶
    

release(_button =0_)[source]¶

    

double_click(_element : WebElement | None = None_)[source]¶
    

pause(_duration : float = 0_)[source]¶

    

PAUSE _ = 'pause'_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.pointer_actions
    * `PointerActions`
      * `PointerActions.pointer_down()`
      * `PointerActions.pointer_up()`
      * `PointerActions.move_to()`
      * `PointerActions.move_by()`
      * `PointerActions.move_to_location()`
      * `PointerActions.click()`
      * `PointerActions.context_click()`
      * `PointerActions.click_and_hold()`
      * `PointerActions.release()`
      * `PointerActions.double_click()`
      * `PointerActions.pause()`
      * `PointerActions.PAUSE`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.pointer_actions

(C) Copyright 2009-2024 Software Freedom Conservancy.