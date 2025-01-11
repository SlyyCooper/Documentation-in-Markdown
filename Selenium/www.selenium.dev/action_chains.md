## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.action_chains¶](#seleniumwebdrivercommonaction_chains)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.action_chains

# selenium.webdriver.common.action_chains¶

The ActionChains implementation.

Classes

`ActionChains`(driver[, duration, devices]) | ActionChains are a way to automate low level interactions such as mouse movements, mouse button actions, key press, and context menu interactions.  
---|---  
  
_class _selenium.webdriver.common.action_chains.ActionChains(_driver : WebDriver_, _duration : int = 250_, _devices : list[AnyDevice] | None = None_)[source]¶
    

ActionChains are a way to automate low level interactions such as mouse
movements, mouse button actions, key press, and context menu interactions.
This is useful for doing more complex actions like hover over and drag and
drop.

Generate user actions.

    

When you call methods for actions on the ActionChains object, the actions are
stored in a queue in the ActionChains object. When you call perform(), the
events are fired in the order they are queued up.

ActionChains can be used in a chain pattern:

    
    
    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
    
    ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
    

Or actions can be queued up one by one, then performed.:

    
    
    menu = driver.find_element(By.CSS_SELECTOR, ".nav")
    hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
    
    actions = ActionChains(driver)
    actions.move_to_element(menu)
    actions.click(hidden_submenu)
    actions.perform()
    

Either way, the actions are performed in the order they are called, one after
another.

Creates a new ActionChains.

Args:

    

  * driver: The WebDriver instance which performs user actions.

  * duration: override the default 250 msecs of DEFAULT_MOVE_DURATION in PointerInput

perform() -> None[source]¶

    

Performs all stored actions.

reset_actions() -> None[source]¶

    

Clears actions that are already stored locally and on the remote end.

click(_on_element : WebElement | None = None_) -> ActionChains[source]¶
    

Clicks an element.

Args:

    

  * on_element: The element to click. If None, clicks on current mouse position.

click_and_hold(_on_element : WebElement | None = None_) -> ActionChains[source]¶
    

Holds down the left mouse button on an element.

Args:

    

  * on_element: The element to mouse down. If None, clicks on current mouse position.

context_click(_on_element : WebElement | None = None_) -> ActionChains[source]¶
    

Performs a context-click (right click) on an element.

Args:

    

  * on_element: The element to context-click. If None, clicks on current mouse position.

double_click(_on_element : WebElement | None = None_) -> ActionChains[source]¶
    

Double-clicks an element.

Args:

    

  * on_element: The element to double-click. If None, clicks on current mouse position.

drag_and_drop(_source : WebElement_, _target : WebElement_) ->
ActionChains[source]¶

    

Holds down the left mouse button on the source element, then moves to the
target element and releases the mouse button.

Args:

    

  * source: The element to mouse down.

  * target: The element to mouse up.

drag_and_drop_by_offset(_source : WebElement_, _xoffset : int_, _yoffset :
int_) -> ActionChains[source]¶

    

Holds down the left mouse button on the source element, then moves to the
target offset and releases the mouse button.

Args:

    

  * source: The element to mouse down.

  * xoffset: X offset to move to.

  * yoffset: Y offset to move to.

key_down(_value : str_, _element : WebElement | None = None_) -> ActionChains[source]¶
    

Sends a key press only, without releasing it. Should only be used with
modifier keys (Control, Alt and Shift).

Args:

    

  * value: The modifier key to send. Values are defined in Keys class.

  * element: The element to send keys. If None, sends a key to current focused element.

Example, pressing ctrl+c:

    
    
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    

key_up(_value : str_, _element : WebElement | None = None_) -> ActionChains[source]¶
    

Releases a modifier key.

Args:

    

  * value: The modifier key to send. Values are defined in Keys class.

  * element: The element to send keys. If None, sends a key to current focused element.

Example, pressing ctrl+c:

    
    
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    

move_by_offset(_xoffset : int_, _yoffset : int_) -> ActionChains[source]¶

    

Moving the mouse to an offset from current mouse position.

Args:

    

  * xoffset: X offset to move to, as a positive or negative integer.

  * yoffset: Y offset to move to, as a positive or negative integer.

move_to_element(_to_element : WebElement_) -> ActionChains[source]¶

    

Moving the mouse to the middle of an element.

Args:

    

  * to_element: The WebElement to move to.

move_to_element_with_offset(_to_element : WebElement_, _xoffset : int_,
_yoffset : int_) -> ActionChains[source]¶

    

Move the mouse by an offset of the specified element. Offsets are relative to
the in-view center point of the element.

Args:

    

  * to_element: The WebElement to move to.

  * xoffset: X offset to move to, as a positive or negative integer.

  * yoffset: Y offset to move to, as a positive or negative integer.

pause(_seconds : float | int_) -> ActionChains[source]¶
    

Pause all inputs for the specified duration in seconds.

release(_on_element : WebElement | None = None_) -> ActionChains[source]¶
    

Releasing a held mouse button on an element.

Args:

    

  * on_element: The element to mouse up. If None, releases on current mouse position.

send_keys(_* keys_to_send: str_) -> ActionChains[source]¶

    

Sends keys to current focused element.

Args:

    

  * keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.

send_keys_to_element(_element : WebElement_, _* keys_to_send: str_) ->
ActionChains[source]¶

    

Sends keys to an element.

Args:

    

  * element: The element to send keys.

  * keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.

scroll_to_element(_element : WebElement_) -> ActionChains[source]¶

    

If the element is outside the viewport, scrolls the bottom of the element to
the bottom of the viewport.

Args:

    

  * element: Which element to scroll into the viewport.

scroll_by_amount(_delta_x : int_, _delta_y : int_) -> ActionChains[source]¶

    

Scrolls by provided amounts with the origin in the top left corner of the
viewport.

Args:

    

  * delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.

  * delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.

scroll_from_origin(_scroll_origin : ScrollOrigin_, _delta_x : int_, _delta_y :
int_) -> ActionChains[source]¶

    

Scrolls by provided amount based on a provided origin. The scroll origin is
either the center of an element or the upper left of the viewport plus any
offsets. If the origin is an element, and the element is not in the viewport,
the bottom of the element will first be scrolled to the bottom of the
viewport.

Args:

    

  * origin: Where scroll originates (viewport or element center) plus provided offsets.

  * delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.

  * delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.

Raises:

    

If the origin with offset is outside the viewport. \-
MoveTargetOutOfBoundsException - If the origin with offset is outside the
viewport.

### Table of Contents

  * selenium.webdriver.common.action_chains
    * `ActionChains`
      * `ActionChains.perform()`
      * `ActionChains.reset_actions()`
      * `ActionChains.click()`
      * `ActionChains.click_and_hold()`
      * `ActionChains.context_click()`
      * `ActionChains.double_click()`
      * `ActionChains.drag_and_drop()`
      * `ActionChains.drag_and_drop_by_offset()`
      * `ActionChains.key_down()`
      * `ActionChains.key_up()`
      * `ActionChains.move_by_offset()`
      * `ActionChains.move_to_element()`
      * `ActionChains.move_to_element_with_offset()`
      * `ActionChains.pause()`
      * `ActionChains.release()`
      * `ActionChains.send_keys()`
      * `ActionChains.send_keys_to_element()`
      * `ActionChains.scroll_to_element()`
      * `ActionChains.scroll_by_amount()`
      * `ActionChains.scroll_from_origin()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.action_chains

(C) Copyright 2009-2024 Software Freedom Conservancy.