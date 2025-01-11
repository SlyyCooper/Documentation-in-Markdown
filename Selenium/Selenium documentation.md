Now create your own documentation based on this documentation that does not refer to any files that contains how to's references how to use each and every aspect of it how to call every every aspect of it and everything possible that you can think of to make it complete and accurate and user friendly for both developers of high skills and beginners. You are the to improve and add to that documentation by learning and adding the Python related documentation or creating Python related documentation off the API references based on the documentation below. Make it complete, accurate, and all references be included. If by some odd chance this exceeds your context limit you can do it in two parts but you are only allowed to do that if you max out your context limit within a range of 50 tokens. That's the only way you can do a part two. So go into this as if there is no context limit. Make it all inclusive complete and accurate based on the documentation I gave you as if I were going to audit it for such.

# Selenium Documentation

## Table of Contents

- [Bidi.Session](#bidi.session)
- [Actions.Interaction](#actions.interaction)
- [Action Chains](#action-chains)
- [Actions.Key Input](#actions.key-input)
- [Utils](#utils)
- [Actions.Pointer Input](#actions.pointer-input)
- [Virtual Authenticator](#virtual-authenticator)
- [Actions.Action Builder](#actions.action-builder)
- [Bidi.Cdp](#bidi.cdp)
- [Alert](#alert)
- [Driver Finder](#driver-finder)
- [Bidi.Console](#bidi.console)
- [Actions.Wheel Actions](#actions.wheel-actions)
- [Desired Capabilities](#desired-capabilities)
- [By](#by)
- [Actions.Mouse Button](#actions.mouse-button)
- [Log](#log)
- [Bidi.Script](#bidi.script)
- [Window](#window)
- [Actions.Key Actions](#actions.key-actions)
- [Options](#options)
- [Actions.Wheel Input](#actions.wheel-input)
- [Service](#service)
- [Keys](#keys)
- [Actions.Input Device](#actions.input-device)
- [Actions.Pointer Actions](#actions.pointer-actions)
- [Timeouts](#timeouts)
- [Proxy](#proxy)
- [Print Page Options](#print-page-options)
- [Selenium Manager](#selenium-manager)

- [Chrome.Service](#chrome.service)
- [Chrome.Options](#chrome.options)
- [Chrome.Webdriver](#chrome.webdriver)
---



## Bidi.Session

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.session¶](#seleniumwebdrivercommonbidisession)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.session


Functions

`session_subscribe`(*events[, browsing_contexts]) |   
---|---  
`session_unsubscribe`(*events[, browsing_contexts]) |   
  
selenium.webdriver.common.bidi.session.session_subscribe(_* events_,
_browsing_contexts =[]_)[source]¶

    

selenium.webdriver.common.bidi.session.session_unsubscribe(_* events_,
_browsing_contexts =[]_)[source]¶

    

### Table of Contents

  * selenium.webdriver.common.bidi.session
    * `session_subscribe()`
    * `session_unsubscribe()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.session

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Interaction

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.interaction¶](#seleniumwebdrivercommonactionsinteraction)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.interaction


Classes

`Interaction`(source) |   
---|---  
`Pause`(source[, duration]) |   
  
_class _selenium.webdriver.common.actions.interaction.Interaction(_source :
str_)[source]¶

    

PAUSE _ = 'pause'_¶

    

_class _selenium.webdriver.common.actions.interaction.Pause(_source_ ,
_duration : float = 0_)[source]¶

    

encode() -> Dict[str, str | int][source]¶
    

PAUSE _ = 'pause'_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.interaction
    * `Interaction`
      * `Interaction.PAUSE`
    * `Pause`
      * `Pause.encode()`
      * `Pause.PAUSE`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.interaction

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Action Chains

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

## Actions.Key Input

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.key_input¶](#seleniumwebdrivercommonactionskey_input)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.key_input


Classes

`KeyInput`(name) |   
---|---  
`TypingInteraction`(source, type_, key) |   
  
_class _selenium.webdriver.common.actions.key_input.KeyInput(_name :
str_)[source]¶

    

encode() -> dict[source]¶

    

create_key_down(_key_) -> None[source]¶

    

create_key_up(_key_) -> None[source]¶

    

create_pause(_pause_duration : float = 0_) -> None[source]¶

    

add_action(_action : Any_) -> None¶

    

clear_actions() -> None¶

    

_class _selenium.webdriver.common.actions.key_input.TypingInteraction(_source_
, _type__ , _key_)[source]¶

    

encode() -> dict[source]¶

    

PAUSE _ = 'pause'_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.key_input
    * `KeyInput`
      * `KeyInput.encode()`
      * `KeyInput.create_key_down()`
      * `KeyInput.create_key_up()`
      * `KeyInput.create_pause()`
      * `KeyInput.add_action()`
      * `KeyInput.clear_actions()`
    * `TypingInteraction`
      * `TypingInteraction.encode()`
      * `TypingInteraction.PAUSE`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.key_input

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Utils

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

## Actions.Pointer Input

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.pointer_input¶](#seleniumwebdrivercommonactionspointer_input)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.pointer_input


Classes

`PointerInput`(kind, name) |   
---|---  
  
_class _selenium.webdriver.common.actions.pointer_input.PointerInput(_kind_ ,
_name_)[source]¶

    

DEFAULT_MOVE_DURATION _ = 250_¶

    

create_pointer_move(_duration =250_, _x : float = 0_, _y : float = 0_, _origin : WebElement | None = None_, _** kwargs_)[source]¶
    

create_pointer_down(_** kwargs_)[source]¶

    

create_pointer_up(_button_)[source]¶

    

create_pointer_cancel()[source]¶

    

create_pause(_pause_duration : int | float = 0_) -> None[source]¶
    

encode()[source]¶

    

add_action(_action : Any_) -> None¶

    

clear_actions() -> None¶

    

### Table of Contents

  * selenium.webdriver.common.actions.pointer_input
    * `PointerInput`
      * `PointerInput.DEFAULT_MOVE_DURATION`
      * `PointerInput.create_pointer_move()`
      * `PointerInput.create_pointer_down()`
      * `PointerInput.create_pointer_up()`
      * `PointerInput.create_pointer_cancel()`
      * `PointerInput.create_pause()`
      * `PointerInput.encode()`
      * `PointerInput.add_action()`
      * `PointerInput.clear_actions()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.pointer_input

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Virtual Authenticator

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.virtual_authenticator¶](#seleniumwebdrivercommonvirtual_authenticator)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.virtual_authenticator


Functions

`required_chromium_based_browser`(func) | A decorator to ensure that the client used is a chromium based browser.  
---|---  
`required_virtual_authenticator`(func) | A decorator to ensure that the function is called with a virtual authenticator.  
  
Classes

`Credential`(credential_id, ...) | Constructor.  
---|---  
`Protocol`(value) | Protocol to communicate with the authenticator.  
`Transport`(value) | Transport method to communicate with the authenticator.  
`VirtualAuthenticatorOptions`([protocol, ...]) | Constructor.  
  
_class
_selenium.webdriver.common.virtual_authenticator.Protocol(_value_)[source]¶

    

Protocol to communicate with the authenticator.

CTAP2 _: str_ _ = 'ctap2'_¶

    

U2F _: str_ _ = 'ctap1/u2f'_¶

    

_class
_selenium.webdriver.common.virtual_authenticator.Transport(_value_)[source]¶

    

Transport method to communicate with the authenticator.

BLE _: str_ _ = 'ble'_¶

    

USB _: str_ _ = 'usb'_¶

    

NFC _: str_ _ = 'nfc'_¶

    

INTERNAL _: str_ _ = 'internal'_¶

    

_class
_selenium.webdriver.common.virtual_authenticator.VirtualAuthenticatorOptions(_protocol
: str = Protocol.CTAP2_, _transport : str = Transport.USB_, _has_resident_key
: bool = False_, _has_user_verification : bool = False_, _is_user_consenting :
bool = True_, _is_user_verified : bool = False_)[source]¶

    

Constructor.

Initialize VirtualAuthenticatorOptions object.

_class _Protocol(_value_)¶

    

Protocol to communicate with the authenticator.

CTAP2 _: str_ _ = 'ctap2'_¶

    

U2F _: str_ _ = 'ctap1/u2f'_¶

    

_class _Transport(_value_)¶

    

Transport method to communicate with the authenticator.

BLE _: str_ _ = 'ble'_¶

    

USB _: str_ _ = 'usb'_¶

    

NFC _: str_ _ = 'nfc'_¶

    

INTERNAL _: str_ _ = 'internal'_¶

    

to_dict() -> Dict[str, str | bool][source]¶
    

_class _selenium.webdriver.common.virtual_authenticator.Credential(_credential_id : bytes_, _is_resident_credential : bool_, _rp_id : str_, _user_handle : bytes | None_, _private_key : bytes_, _sign_count : int_)[source]¶
    

Constructor. A credential stored in a virtual authenticator.
https://w3c.github.io/webauthn/#credential-parameters.

Args:

    

  * credential_id (bytes): Unique base64 encoded string.

is_resident_credential (bool): Whether the credential is client-side
discoverable. rp_id (str): Relying party identifier. user_handle (bytes):
userHandle associated to the credential. Must be Base64 encoded string. Can be
None. private_key (bytes): Base64 encoded PKCS#8 private key. sign_count
(int): intital value for a signature counter.

_property _id _: str_¶

    

_property _is_resident_credential _: bool_¶

    

_property _rp_id _: str_¶

    

_property _user_handle _: str | None_¶
    

_property _private_key _: str_¶

    

_property _sign_count _: int_¶

    

_classmethod _create_non_resident_credential(_id : bytes_, _rp_id : str_,
_private_key : bytes_, _sign_count : int_) -> Credential[source]¶

    

Creates a non-resident (i.e. stateless) credential.

Args:

    

  * id (bytes): Unique base64 encoded string.

  * rp_id (str): Relying party identifier.

  * private_key (bytes): Base64 encoded PKCS

  * sign_count (int): intital value for a signature counter.

Returns:

    

  * Credential: A non-resident credential.

_classmethod _create_resident_credential(_id : bytes_, _rp_id : str_, _user_handle : bytes | None_, _private_key : bytes_, _sign_count : int_) -> Credential[source]¶
    

Creates a resident (i.e. stateful) credential.

Args:

    

  * id (bytes): Unique base64 encoded string.

  * rp_id (str): Relying party identifier.

  * user_handle (bytes): userHandle associated to the credential. Must be Base64 encoded string.

  * private_key (bytes): Base64 encoded PKCS

  * sign_count (int): intital value for a signature counter.

Returns:

    

  * Credential: A resident credential.

to_dict() -> Dict[str, Any][source]¶

    

_classmethod _from_dict(_data : Dict[str, Any]_) -> Credential[source]¶

    

selenium.webdriver.common.virtual_authenticator.required_chromium_based_browser(_func_)[source]¶

    

A decorator to ensure that the client used is a chromium based browser.

selenium.webdriver.common.virtual_authenticator.required_virtual_authenticator(_func_)[source]¶

    

A decorator to ensure that the function is called with a virtual
authenticator.

### Table of Contents

  * selenium.webdriver.common.virtual_authenticator
    * `Protocol`
      * `Protocol.CTAP2`
      * `Protocol.U2F`
    * `Transport`
      * `Transport.BLE`
      * `Transport.USB`
      * `Transport.NFC`
      * `Transport.INTERNAL`
    * `VirtualAuthenticatorOptions`
      * `VirtualAuthenticatorOptions.Protocol`
        * `VirtualAuthenticatorOptions.Protocol.CTAP2`
        * `VirtualAuthenticatorOptions.Protocol.U2F`
      * `VirtualAuthenticatorOptions.Transport`
        * `VirtualAuthenticatorOptions.Transport.BLE`
        * `VirtualAuthenticatorOptions.Transport.USB`
        * `VirtualAuthenticatorOptions.Transport.NFC`
        * `VirtualAuthenticatorOptions.Transport.INTERNAL`
      * `VirtualAuthenticatorOptions.to_dict()`
    * `Credential`
      * `Credential.id`
      * `Credential.is_resident_credential`
      * `Credential.rp_id`
      * `Credential.user_handle`
      * `Credential.private_key`
      * `Credential.sign_count`
      * `Credential.create_non_resident_credential()`
      * `Credential.create_resident_credential()`
      * `Credential.to_dict()`
      * `Credential.from_dict()`
    * `required_chromium_based_browser()`
    * `required_virtual_authenticator()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.virtual_authenticator

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Action Builder

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.action_builder¶](#seleniumwebdrivercommonactionsaction_builder)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.action_builder


Classes

`ActionBuilder`(driver[, mouse, wheel, ...]) |   
---|---  
  
_class _selenium.webdriver.common.actions.action_builder.ActionBuilder(_driver_ , _mouse : PointerInput | None = None_, _wheel : WheelInput | None = None_, _keyboard : KeyInput | None = None_, _duration : int = 250_)[source]¶
    

get_device_with(_name : str_) -> WheelInput | PointerInput | KeyInput | None[source]¶
    

_property _pointer_inputs _: List[PointerInput]_¶

    

_property _key_inputs _: List[KeyInput]_¶

    

_property _key_action _: KeyActions_¶

    

_property _pointer_action _: PointerActions_¶

    

_property _wheel_action _: WheelActions_¶

    

add_key_input(_name : str_) -> KeyInput[source]¶

    

add_pointer_input(_kind : str_, _name : str_) -> PointerInput[source]¶

    

add_wheel_input(_name : str_) -> WheelInput[source]¶

    

perform() -> None[source]¶

    

clear_actions() -> None[source]¶

    

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

## Bidi.Cdp

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.cdp¶](#seleniumwebdrivercommonbidicdp)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.cdp


Functions

`connect_cdp`(nursery, url) | Connect to the browser specified by `url` and spawn a background task in the specified nursery.  
---|---  
`connection_context`(connection) | This context manager installs `connection` as the session context for the current Trio task.  
`get_connection_context`(fn_name) | Look up the current connection.  
`get_session_context`(fn_name) | Look up the current session.  
`import_devtools`(ver) | Attempt to load the current latest available devtools into the module cache for use later.  
`open_cdp`(url) | This async context manager opens a connection to the browser specified by `url` before entering the block, then closes the connection when the block exits.  
`session_context`(session) | This context manager installs `session` as the session context for the current Trio task.  
`set_global_connection`(connection) | Install `connection` in the root context so that it will become the default connection for all tasks.  
`set_global_session`(session) | Install `session` in the root context so that it will become the default session for all tasks.  
  
Classes

`CdpBase`(ws, session_id, target_id) |   
---|---  
`CdpConnection`(ws) | Contains the connection state for a Chrome DevTools Protocol server.  
`CdpSession`(ws, session_id, target_id) | Contains the state for a CDP session.  
`CmEventProxy`([value]) | A proxy object returned by `CdpBase.wait_for()`()`.  
  
Exceptions

`BrowserError`(obj) | This exception is raised when the browser's response to a command indicates that an error occurred.  
---|---  
`CdpConnectionClosed`(reason) | Raised when a public method is called on a closed CDP connection.  
`InternalError` | This exception is only raised when there is faulty logic in TrioCDP or the integration with PyCDP.  
  
selenium.webdriver.common.bidi.cdp.import_devtools(_ver_)[source]¶

    

Attempt to load the current latest available devtools into the module cache
for use later.

selenium.webdriver.common.bidi.cdp.get_connection_context(_fn_name_)[source]¶

    

Look up the current connection.

If there is no current connection, raise a `RuntimeError` with a helpful
message.

selenium.webdriver.common.bidi.cdp.get_session_context(_fn_name_)[source]¶

    

Look up the current session.

If there is no current session, raise a `RuntimeError` with a helpful message.

selenium.webdriver.common.bidi.cdp.connection_context(_connection_)[source]¶

    

This context manager installs `connection` as the session context for the
current Trio task.

selenium.webdriver.common.bidi.cdp.session_context(_session_)[source]¶

    

This context manager installs `session` as the session context for the current
Trio task.

selenium.webdriver.common.bidi.cdp.set_global_connection(_connection_)[source]¶

    

Install `connection` in the root context so that it will become the default
connection for all tasks.

This is generally not recommended, except it may be necessary in certain use
cases such as running inside Jupyter notebook.

selenium.webdriver.common.bidi.cdp.set_global_session(_session_)[source]¶

    

Install `session` in the root context so that it will become the default
session for all tasks.

This is generally not recommended, except it may be necessary in certain use
cases such as running inside Jupyter notebook.

_exception _selenium.webdriver.common.bidi.cdp.BrowserError(_obj_)[source]¶

    

This exception is raised when the browser’s response to a command indicates
that an error occurred.

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_exception
_selenium.webdriver.common.bidi.cdp.CdpConnectionClosed(_reason_)[source]¶

    

Raised when a public method is called on a closed CDP connection.

Constructor.

Parameters:

    

**reason** (_wsproto.frame_protocol.CloseReason_) –

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_exception _selenium.webdriver.common.bidi.cdp.InternalError[source]¶

    

This exception is only raised when there is faulty logic in TrioCDP or the
integration with PyCDP.

args¶

    

with_traceback()¶

    

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

_class _selenium.webdriver.common.bidi.cdp.CmEventProxy(_value : Any | None = None_)[source]¶
    

A proxy object returned by `CdpBase.wait_for()`()`.

After the context manager executes, this proxy object will have a value set
that contains the returned event.

value _: Any_ _ = None_¶

    

_class _selenium.webdriver.common.bidi.cdp.CdpBase(_ws_ , _session_id_ ,
_target_id_)[source]¶

    

_async _execute(_cmd : Generator[dict, T, Any]_) -> T[source]¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)[source]¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None][source]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

_class _selenium.webdriver.common.bidi.cdp.CdpSession(_ws_ , _session_id_ ,
_target_id_)[source]¶

    

Contains the state for a CDP session.

Generally you should not instantiate this object yourself; you should call
`CdpConnection.open_session()`.

Constructor.

Parameters:

    

  * **ws** (_trio_websocket.WebSocketConnection_) – 

  * **session_id** (_devtools.target.SessionID_) – 

  * **target_id** (_devtools.target.TargetID_) – 

dom_enable()[source]¶

    

A context manager that executes `dom.enable()` when it enters and then calls
`dom.disable()`.

This keeps track of concurrent callers and only disables DOM events when all
callers have exited.

page_enable()[source]¶

    

A context manager that executes `page.enable()` when it enters and then calls
`page.disable()` when it exits.

This keeps track of concurrent callers and only disables page events when all
callers have exited.

_async _execute(_cmd : Generator[dict, T, Any]_) -> T¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

_class _selenium.webdriver.common.bidi.cdp.CdpConnection(_ws_)[source]¶

    

Contains the connection state for a Chrome DevTools Protocol server.

CDP can multiplex multiple “sessions” over a single connection. This class
corresponds to the “root” session, i.e. the implicitly created session that
has no session ID. This class is responsible for reading incoming WebSocket
messages and forwarding them to the corresponding session, as well as handling
messages targeted at the root session itself. You should generally call the
`open_cdp()` instead of instantiating this class directly.

Constructor.

Parameters:

    

**ws** (_trio_websocket.WebSocketConnection_) –

_async _aclose()[source]¶

    

Close the underlying WebSocket connection.

This will cause the reader task to gracefully exit when it tries to read the
next message from the WebSocket. All of the public APIs (`execute()`,
`listen()`, etc.) will raise `CdpConnectionClosed` after the CDP connection is
closed. It is safe to call this multiple times.

open_session(_target_id_) -> AsyncIterator[CdpSession][source]¶

    

This context manager opens a session and enables the “simple” style of calling
CDP APIs.

For example, inside a session context, you can call `await dom.get_document()`
and it will execute on the current session automatically.

_async _connect_session(_target_id_) -> CdpSession[source]¶

    

Returns a new `CdpSession` connected to the specified target.

_async _execute(_cmd : Generator[dict, T, Any]_) -> T¶

    

Execute a command on the server and wait for the result.

Parameters:

    

**cmd** – any CDP command

Returns:

    

a CDP result

listen(_* event_types_, _buffer_size =10_)¶

    

Return an async iterator that iterates over events matching the indicated
types.

wait_for(_event_type : Type[T]_, _buffer_size =10_) ->
AsyncGenerator[CmEventProxy, None]¶

    

Wait for an event of the given type and return it.

This is an async context manager, so you should open it inside an async with
block. The block will not exit until the indicated event is received.

selenium.webdriver.common.bidi.cdp.open_cdp(_url_) ->
AsyncIterator[CdpConnection][source]¶

    

This async context manager opens a connection to the browser specified by
`url` before entering the block, then closes the connection when the block
exits.

The context manager also sets the connection as the default connection for the
current task, so that commands like `await target.get_targets()` will run on
this connection automatically. If you want to use multiple connections
concurrently, it is recommended to open each on in a separate task.

_async _selenium.webdriver.common.bidi.cdp.connect_cdp(_nursery_ , _url_) ->
CdpConnection[source]¶

    

Connect to the browser specified by `url` and spawn a background task in the
specified nursery.

The `open_cdp()` context manager is preferred in most situations. You should
only use this function if you need to specify a custom nursery. This
connection is not automatically closed! You can either use the connection
object as a context manager (`async with conn:`) or else call `await
conn.aclose()` on it when you are done with it. If `set_context` is True, then
the returned connection will be installed as the default connection for the
current task. This argument is for unusual use cases, such as running inside
of a notebook.

### Table of Contents

  * selenium.webdriver.common.bidi.cdp
    * `import_devtools()`
    * `get_connection_context()`
    * `get_session_context()`
    * `connection_context()`
    * `session_context()`
    * `set_global_connection()`
    * `set_global_session()`
    * `BrowserError`
      * `BrowserError.args`
      * `BrowserError.with_traceback()`
    * `CdpConnectionClosed`
      * `CdpConnectionClosed.args`
      * `CdpConnectionClosed.with_traceback()`
    * `InternalError`
      * `InternalError.args`
      * `InternalError.with_traceback()`
    * `CmEventProxy`
      * `CmEventProxy.value`
    * `CdpBase`
      * `CdpBase.execute()`
      * `CdpBase.listen()`
      * `CdpBase.wait_for()`
    * `CdpSession`
      * `CdpSession.dom_enable()`
      * `CdpSession.page_enable()`
      * `CdpSession.execute()`
      * `CdpSession.listen()`
      * `CdpSession.wait_for()`
    * `CdpConnection`
      * `CdpConnection.aclose()`
      * `CdpConnection.open_session()`
      * `CdpConnection.connect_session()`
      * `CdpConnection.execute()`
      * `CdpConnection.listen()`
      * `CdpConnection.wait_for()`
    * `open_cdp()`
    * `connect_cdp()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.cdp

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Alert

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.alert¶](#seleniumwebdrivercommonalert)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.alert


The Alert implementation.

Classes

`Alert`(driver) | Allows to work with alerts.  
---|---  
  
_class _selenium.webdriver.common.alert.Alert(_driver_)[source]¶

    

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

_property _text _: str_¶

    

Gets the text of the Alert.

dismiss() -> None[source]¶

    

Dismisses the alert available.

accept() -> None[source]¶

    

Accepts the alert available.

Usage:

    
    
    
    Alert(driver).accept() # Confirm a alert dialog.
    

send_keys(_keysToSend : str_) -> None[source]¶

    

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

## Driver Finder

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.driver_finder¶](#seleniumwebdrivercommondriver_finder)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.driver_finder


Classes

`DriverFinder`(service, options) | A Driver finding class responsible for obtaining the correct driver and associated browser.  
---|---  
  
_class _selenium.webdriver.common.driver_finder.DriverFinder(_service :
Service_, _options : BaseOptions_)[source]¶

    

A Driver finding class responsible for obtaining the correct driver and
associated browser.

Parameters:

    

  * **service** – instance of the driver service class.

  * **options** – instance of the browser options class.

get_browser_path() -> str[source]¶

    

get_driver_path() -> str[source]¶

    

### Table of Contents

  * selenium.webdriver.common.driver_finder
    * `DriverFinder`
      * `DriverFinder.get_browser_path()`
      * `DriverFinder.get_driver_path()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.driver_finder

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Bidi.Console

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.console¶](#seleniumwebdrivercommonbidiconsole)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.console


Classes

`Console`(value) | An enumeration.  
---|---  
  
_class _selenium.webdriver.common.bidi.console.Console(_value_)[source]¶

    

An enumeration.

ALL _ = 'all'_¶

    

LOG _ = 'log'_¶

    

ERROR _ = 'error'_¶

    

### Table of Contents

  * selenium.webdriver.common.bidi.console
    * `Console`
      * `Console.ALL`
      * `Console.LOG`
      * `Console.ERROR`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.console

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Wheel Actions

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.wheel_actions¶](#seleniumwebdrivercommonactionswheel_actions)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.wheel_actions


Classes

`WheelActions`([source]) |   
---|---  
  
_class _selenium.webdriver.common.actions.wheel_actions.WheelActions(_source : WheelInput | None = None_)[source]¶
    

pause(_duration : float = 0_)[source]¶

    

scroll(_x =0_, _y =0_, _delta_x =0_, _delta_y =0_, _duration =0_, _origin
='viewport'_)[source]¶

    

PAUSE _ = 'pause'_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.wheel_actions
    * `WheelActions`
      * `WheelActions.pause()`
      * `WheelActions.scroll()`
      * `WheelActions.PAUSE`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.wheel_actions

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Desired Capabilities

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.desired_capabilities¶](#seleniumwebdrivercommondesired_capabilities)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.desired_capabilities


The Desired Capabilities implementation.

Classes

`DesiredCapabilities`() | Set of default supported desired capabilities.  
---|---  
  
_class
_selenium.webdriver.common.desired_capabilities.DesiredCapabilities[source]¶

    

Set of default supported desired capabilities.

Use this as a starting point for creating a desired capabilities object for
requesting remote webdrivers for connecting to selenium server or selenium
grid.

Usage Example:

    
    
    from selenium import webdriver
    
    selenium_grid_url = "http://198.0.0.1:4444/wd/hub"
    
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"
    
    driver = webdriver.Remote(desired_capabilities=capabilities,
                              command_executor=selenium_grid_url)
    

Note: Always use ‘.copy()’ on the DesiredCapabilities object to avoid the side
effects of altering the Global class instance.

FIREFOX _ = {'acceptInsecureCerts': True, 'browserName': 'firefox',
'moz:debuggerAddress': True}_¶

    

INTERNETEXPLORER _ = {'browserName': 'internet explorer', 'platformName':
'windows'}_¶

    

EDGE _ = {'browserName': 'MicrosoftEdge'}_¶

    

CHROME _ = {'browserName': 'chrome'}_¶

    

SAFARI _ = {'browserName': 'safari', 'platformName': 'mac'}_¶

    

HTMLUNIT _ = {'browserName': 'htmlunit', 'platform': 'ANY', 'version': ''}_¶

    

HTMLUNITWITHJS _ = {'browserName': 'htmlunit', 'javascriptEnabled': True,
'platform': 'ANY', 'version': 'firefox'}_¶

    

IPHONE _ = {'browserName': 'iPhone', 'platform': 'mac', 'version': ''}_¶

    

IPAD _ = {'browserName': 'iPad', 'platform': 'mac', 'version': ''}_¶

    

WEBKITGTK _ = {'browserName': 'MiniBrowser'}_¶

    

WPEWEBKIT _ = {'browserName': 'MiniBrowser'}_¶

    

### Table of Contents

  * selenium.webdriver.common.desired_capabilities
    * `DesiredCapabilities`
      * `DesiredCapabilities.FIREFOX`
      * `DesiredCapabilities.INTERNETEXPLORER`
      * `DesiredCapabilities.EDGE`
      * `DesiredCapabilities.CHROME`
      * `DesiredCapabilities.SAFARI`
      * `DesiredCapabilities.HTMLUNIT`
      * `DesiredCapabilities.HTMLUNITWITHJS`
      * `DesiredCapabilities.IPHONE`
      * `DesiredCapabilities.IPAD`
      * `DesiredCapabilities.WEBKITGTK`
      * `DesiredCapabilities.WPEWEBKIT`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.desired_capabilities

(C) Copyright 2009-2024 Software Freedom Conservancy.

## By

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.by¶](#seleniumwebdrivercommonby)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.by


The By implementation.

Classes

`By`() | Set of supported locator strategies.  
---|---  
  
_class _selenium.webdriver.common.by.By[source]¶

    

Set of supported locator strategies.

ID _ = 'id'_¶

    

XPATH _ = 'xpath'_¶

    

LINK_TEXT _ = 'link text'_¶

    

PARTIAL_LINK_TEXT _ = 'partial link text'_¶

    

NAME _ = 'name'_¶

    

TAG_NAME _ = 'tag name'_¶

    

CLASS_NAME _ = 'class name'_¶

    

CSS_SELECTOR _ = 'css selector'_¶

    

### Table of Contents

  * selenium.webdriver.common.by
    * `By`
      * `By.ID`
      * `By.XPATH`
      * `By.LINK_TEXT`
      * `By.PARTIAL_LINK_TEXT`
      * `By.NAME`
      * `By.TAG_NAME`
      * `By.CLASS_NAME`
      * `By.CSS_SELECTOR`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.by

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Mouse Button

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.mouse_button¶](#seleniumwebdrivercommonactionsmouse_button)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.mouse_button


Classes

`MouseButton`() |   
---|---  
  
_class _selenium.webdriver.common.actions.mouse_button.MouseButton[source]¶

    

LEFT _ = 0_¶

    

MIDDLE _ = 1_¶

    

RIGHT _ = 2_¶

    

BACK _ = 3_¶

    

FORWARD _ = 4_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.mouse_button
    * `MouseButton`
      * `MouseButton.LEFT`
      * `MouseButton.MIDDLE`
      * `MouseButton.RIGHT`
      * `MouseButton.BACK`
      * `MouseButton.FORWARD`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.mouse_button

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Log

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

## Bidi.Script

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.bidi.script¶](#seleniumwebdrivercommonbidiscript)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.bidi.script


Classes

`ConsoleLogEntry`(level, text, timestamp, ...) |   
---|---  
`JavaScriptLogEntry`(level, text, timestamp, ...) |   
`LogEntryAdded`() |   
`Script`(conn) |   
  
_class _selenium.webdriver.common.bidi.script.Script(_conn_)[source]¶

    

add_console_message_handler(_handler_)[source]¶

    

add_javascript_error_handler(_handler_)[source]¶

    

remove_console_message_handler(_id_)[source]¶

    

remove_javascript_error_handler(_id_)¶

    

_class _selenium.webdriver.common.bidi.script.LogEntryAdded[source]¶

    

event_class _ = 'log.entryAdded'_¶

    

_classmethod _from_json(_json_)[source]¶

    

_class _selenium.webdriver.common.bidi.script.ConsoleLogEntry(_level : str_,
_text : str_, _timestamp : str_, _method : str_, _args : List[dict]_, _type_ :
str_)[source]¶

    

level _: str_¶

    

text _: str_¶

    

timestamp _: str_¶

    

method _: str_¶

    

args _: List[dict]_¶

    

type__: str_¶

    

_classmethod _from_json(_json_)[source]¶

    

_class _selenium.webdriver.common.bidi.script.JavaScriptLogEntry(_level :
str_, _text : str_, _timestamp : str_, _stacktrace : dict_, _type_ :
str_)[source]¶

    

level _: str_¶

    

text _: str_¶

    

timestamp _: str_¶

    

stacktrace _: dict_¶

    

type__: str_¶

    

_classmethod _from_json(_json_)[source]¶

    

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

## Window

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.window¶](#seleniumwebdrivercommonwindow)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.window


The WindowTypes implementation.

Classes

`WindowTypes`() | Set of supported window types.  
---|---  
  
_class _selenium.webdriver.common.window.WindowTypes[source]¶

    

Set of supported window types.

TAB _ = 'tab'_¶

    

WINDOW _ = 'window'_¶

    

### Table of Contents

  * selenium.webdriver.common.window
    * `WindowTypes`
      * `WindowTypes.TAB`
      * `WindowTypes.WINDOW`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.window

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Key Actions

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.key_actions¶](#seleniumwebdrivercommonactionskey_actions)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.key_actions


Classes

`KeyActions`([source]) |   
---|---  
  
_class _selenium.webdriver.common.actions.key_actions.KeyActions(_source : KeyInput | PointerInput | WheelInput | None = None_)[source]¶
    

key_down(_letter : str_) -> KeyActions[source]¶

    

key_up(_letter : str_) -> KeyActions[source]¶

    

pause(_duration : int = 0_) -> KeyActions[source]¶

    

send_keys(_text : str | list_) -> KeyActions[source]¶
    

PAUSE _ = 'pause'_¶

    

### Table of Contents

  * selenium.webdriver.common.actions.key_actions
    * `KeyActions`
      * `KeyActions.key_down()`
      * `KeyActions.key_up()`
      * `KeyActions.pause()`
      * `KeyActions.send_keys()`
      * `KeyActions.PAUSE`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.key_actions

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Options

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.options¶](#seleniumwebdrivercommonoptions)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.options


Classes

`ArgOptions`() |   
---|---  
`BaseOptions`() | Base class for individual browser options.  
`PageLoadStrategy`(value) | Enum of possible page load strategies.  
  
_class _selenium.webdriver.common.options.PageLoadStrategy(_value_)[source]¶

    

Enum of possible page load strategies.

Selenium support following strategies:

    

  * normal (default) - waits for all resources to download

  * eager - DOM access is ready, but other resources like images may still be loading

  * none - does not block WebDriver at all

Docs:
https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy.

normal _ = 'normal'_¶

    

eager _ = 'eager'_¶

    

none _ = 'none'_¶

    

_class _selenium.webdriver.common.options.BaseOptions[source]¶

    

Base class for individual browser options.

browser_version¶

    

Gets and Sets the version of the browser.

## Usage¶

  * Get
    
    * self.browser_version

  * Set
    
    * self.browser_version = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

platform_name¶

    

Gets and Sets name of the platform.

## Usage¶

  * Get
    
    * self.platform_name

  * Set
    
    * self.platform_name = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

accept_insecure_certs¶

    

Gets and Set whether the session accepts insecure certificates.

## Usage¶

  * Get
    
    * self.accept_insecure_certs

  * Set
    
    * self.accept_insecure_certs = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

strict_file_interactability¶

    

Gets and Sets whether session is about file interactability.

## Usage¶

  * Get
    
    * self.strict_file_interactability

  * Set
    
    * self.strict_file_interactability = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

set_window_rect¶

    

Gets and Sets window size and position.

## Usage¶

  * Get
    
    * self.set_window_rect

  * Set
    
    * self.set_window_rect = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

enable_bidi¶

    

Gets and Set whether the session has WebDriverBiDi enabled.

## Usage¶

  * Get
    
    * self.enable_bidi

  * Set
    
    * self.enable_bidi = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

page_load_strategy¶

    

:Gets and Sets page load strategy, the default is “normal”.

## Usage¶

  * Get
    
    * self.page_load_strategy

  * Set
    
    * self.page_load_strategy = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

unhandled_prompt_behavior¶

    

:Gets and Sets unhandled prompt behavior, the default is “dismiss and notify”.

## Usage¶

  * Get
    
    * self.unhandled_prompt_behavior

  * Set
    
    * self.unhandled_prompt_behavior = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

timeouts¶

    

:Gets and Sets implicit timeout, pageLoad timeout and script timeout if set
(in milliseconds)

## Usage¶

  * Get
    
    * self.timeouts

  * Set
    
    * self.timeouts = value

## Parameters¶

value: dict

## Returns¶

  * Get
    
    * dict

  * Set
    
    * None

proxy¶

    

Sets and Gets Proxy.

## Usage¶

  * Get
    
    * self.proxy

  * Set
    
    * self.proxy = value

## Parameters¶

value: Proxy

## Returns¶

  * Get
    
    * Proxy

  * Set
    
    * None

enable_downloads¶

    

Gets and Sets whether session can download files.

## Usage¶

  * Get
    
    * self.enable_downloads

  * Set
    
    * self.enable_downloads = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

web_socket_url¶

    

Gets and Sets WebSocket URL.

## Usage¶

  * Get
    
    * self.web_socket_url

  * Set
    
    * self.web_socket_url = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

_property _capabilities¶

    

set_capability(_name_ , _value_) -> None[source]¶

    

Sets a capability.

enable_mobile(_android_package : str | None = None_, _android_activity : str | None = None_, _device_serial : str | None = None_) -> None[source]¶
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

_abstract _to_capabilities()[source]¶

    

Convert options into capabilities dictionary.

_abstract property _default_capabilities¶

    

Return minimal capabilities necessary as a dictionary.

ignore_local_proxy_environment_variables() -> None[source]¶

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

_class _selenium.webdriver.common.options.ArgOptions[source]¶

    

_property _capabilities¶

    

enable_mobile(_android_package : str | None = None_, _android_activity : str | None = None_, _device_serial : str | None = None_) -> None¶
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

set_capability(_name_ , _value_) -> None¶

    

Sets a capability.

browser_version¶

    

Gets and Sets the version of the browser.

## Usage¶

  * Get
    
    * self.browser_version

  * Set
    
    * self.browser_version = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

platform_name¶

    

Gets and Sets name of the platform.

## Usage¶

  * Get
    
    * self.platform_name

  * Set
    
    * self.platform_name = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

accept_insecure_certs¶

    

Gets and Set whether the session accepts insecure certificates.

## Usage¶

  * Get
    
    * self.accept_insecure_certs

  * Set
    
    * self.accept_insecure_certs = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

strict_file_interactability¶

    

Gets and Sets whether session is about file interactability.

## Usage¶

  * Get
    
    * self.strict_file_interactability

  * Set
    
    * self.strict_file_interactability = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

set_window_rect¶

    

Gets and Sets window size and position.

## Usage¶

  * Get
    
    * self.set_window_rect

  * Set
    
    * self.set_window_rect = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

enable_bidi¶

    

Gets and Set whether the session has WebDriverBiDi enabled.

## Usage¶

  * Get
    
    * self.enable_bidi

  * Set
    
    * self.enable_bidi = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

web_socket_url¶

    

Gets and Sets WebSocket URL.

## Usage¶

  * Get
    
    * self.web_socket_url

  * Set
    
    * self.web_socket_url = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

page_load_strategy¶

    

:Gets and Sets page load strategy, the default is “normal”.

## Usage¶

  * Get
    
    * self.page_load_strategy

  * Set
    
    * self.page_load_strategy = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

unhandled_prompt_behavior¶

    

:Gets and Sets unhandled prompt behavior, the default is “dismiss and notify”.

## Usage¶

  * Get
    
    * self.unhandled_prompt_behavior

  * Set
    
    * self.unhandled_prompt_behavior = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

timeouts¶

    

:Gets and Sets implicit timeout, pageLoad timeout and script timeout if set
(in milliseconds)

## Usage¶

  * Get
    
    * self.timeouts

  * Set
    
    * self.timeouts = value

## Parameters¶

value: dict

## Returns¶

  * Get
    
    * dict

  * Set
    
    * None

proxy¶

    

Sets and Gets Proxy.

## Usage¶

  * Get
    
    * self.proxy

  * Set
    
    * self.proxy = value

## Parameters¶

value: Proxy

## Returns¶

  * Get
    
    * Proxy

  * Set
    
    * None

enable_downloads¶

    

Gets and Sets whether session can download files.

## Usage¶

  * Get
    
    * self.enable_downloads

  * Set
    
    * self.enable_downloads = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

BINARY_LOCATION_ERROR _ = 'Binary Location Must be a String'_¶

    

_property _arguments¶

    

Returns:

    

A list of arguments needed for the browser.

add_argument(_argument_) -> None[source]¶

    

Adds an argument to the list.

Args:

    

  * Sets the arguments

ignore_local_proxy_environment_variables() -> None[source]¶

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

to_capabilities()[source]¶

    

Convert options into capabilities dictionary.

_property _default_capabilities¶

    

Return minimal capabilities necessary as a dictionary.

### Table of Contents

  * selenium.webdriver.common.options
    * `PageLoadStrategy`
      * `PageLoadStrategy.normal`
      * `PageLoadStrategy.eager`
      * `PageLoadStrategy.none`
    * `BaseOptions`
      * `BaseOptions.browser_version`
      * `BaseOptions.platform_name`
      * `BaseOptions.accept_insecure_certs`
      * `BaseOptions.strict_file_interactability`
      * `BaseOptions.set_window_rect`
      * `BaseOptions.enable_bidi`
      * `BaseOptions.page_load_strategy`
      * `BaseOptions.unhandled_prompt_behavior`
      * `BaseOptions.timeouts`
      * `BaseOptions.proxy`
      * `BaseOptions.enable_downloads`
      * `BaseOptions.web_socket_url`
      * `BaseOptions.capabilities`
      * `BaseOptions.set_capability()`
      * `BaseOptions.enable_mobile()`
      * `BaseOptions.to_capabilities()`
      * `BaseOptions.default_capabilities`
      * `BaseOptions.ignore_local_proxy_environment_variables()`
    * `ArgOptions`
      * `ArgOptions.capabilities`
      * `ArgOptions.enable_mobile()`
      * `ArgOptions.set_capability()`
      * `ArgOptions.browser_version`
      * `ArgOptions.platform_name`
      * `ArgOptions.accept_insecure_certs`
      * `ArgOptions.strict_file_interactability`
      * `ArgOptions.set_window_rect`
      * `ArgOptions.enable_bidi`
      * `ArgOptions.web_socket_url`
      * `ArgOptions.page_load_strategy`
      * `ArgOptions.unhandled_prompt_behavior`
      * `ArgOptions.timeouts`
      * `ArgOptions.proxy`
      * `ArgOptions.enable_downloads`
      * `ArgOptions.BINARY_LOCATION_ERROR`
      * `ArgOptions.arguments`
      * `ArgOptions.add_argument()`
      * `ArgOptions.ignore_local_proxy_environment_variables()`
      * `ArgOptions.to_capabilities()`
      * `ArgOptions.default_capabilities`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.options

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Wheel Input

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.wheel_input¶](#seleniumwebdrivercommonactionswheel_input)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.wheel_input


Classes

`ScrollOrigin`(origin, x_offset, y_offset) |   
---|---  
`WheelInput`(name) |   
  
_class _selenium.webdriver.common.actions.wheel_input.ScrollOrigin(_origin : str | WebElement_, _x_offset : int_, _y_offset : int_)[source]¶
    

_classmethod _from_element(_element : WebElement_, _x_offset : int = 0_,
_y_offset : int = 0_)[source]¶

    

_classmethod _from_viewport(_x_offset : int = 0_, _y_offset : int =
0_)[source]¶

    

_property _origin _: str | WebElement_¶
    

_property _x_offset _: int_¶

    

_property _y_offset _: int_¶

    

_class
_selenium.webdriver.common.actions.wheel_input.WheelInput(_name_)[source]¶

    

encode() -> dict[source]¶

    

create_scroll(_x : int_, _y : int_, _delta_x : int_, _delta_y : int_,
_duration : int_, _origin_) -> None[source]¶

    

create_pause(_pause_duration : int | float = 0_) -> None[source]¶
    

add_action(_action : Any_) -> None¶

    

clear_actions() -> None¶

    

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

## Service

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.service¶](#seleniumwebdrivercommonservice)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.service


Classes

`Service`([executable_path, port, log_output, env]) | The abstract base class for all service objects.  
---|---  
  
_class _selenium.webdriver.common.service.Service(_executable_path : str | None = None_, _port : int = 0_, _log_output : int | str | IO[Any] | None = None_, _env : Mapping[Any, Any] | None = None_, _** kwargs_)[source]¶
    

The abstract base class for all service objects. Services typically launch a
child program in a new process as an interim process to communicate with a
browser.

Parameters:

    

  * **executable** – install path of the executable.

  * **port** – Port for the service to run on, defaults to 0 where the operating system will decide.

  * **log_output** – (Optional) int representation of STDOUT/DEVNULL, any IO instance or String path to file.

  * **env** – (Optional) Mapping of environment variables for the new process, defaults to os.environ.

_property _service_url _: str_¶

    

Gets the url of the Service.

_abstract _command_line_args() -> List[str][source]¶

    

A List of program arguments (excluding the executable).

_property _path _: str_¶

    

start() -> None[source]¶

    

Starts the Service.

Exceptions:

    

  * WebDriverException : Raised either when it can’t start the service or when it can’t connect to the service

assert_process_still_running() -> None[source]¶

    

Check if the underlying process is still running.

is_connectable() -> bool[source]¶

    

Establishes a socket connection to determine if the service running on the
port is accessible.

send_remote_shutdown_command() -> None[source]¶

    

Dispatch an HTTP request to the shutdown endpoint for the service in an
attempt to stop it.

stop() -> None[source]¶

    

Stops the service.

### Table of Contents

  * selenium.webdriver.common.service
    * `Service`
      * `Service.service_url`
      * `Service.command_line_args()`
      * `Service.path`
      * `Service.start()`
      * `Service.assert_process_still_running()`
      * `Service.is_connectable()`
      * `Service.send_remote_shutdown_command()`
      * `Service.stop()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.service

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Keys

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.keys¶](#seleniumwebdrivercommonkeys)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.keys


The Keys implementation.

Classes

`Keys`() | Set of special keys codes.  
---|---  
  
_class _selenium.webdriver.common.keys.Keys[source]¶

    

Set of special keys codes.

NULL _ = '\ue000'_¶

    

CANCEL _ = '\ue001'_¶

    

HELP _ = '\ue002'_¶

    

BACKSPACE _ = '\ue003'_¶

    

BACK_SPACE _ = '\ue003'_¶

    

TAB _ = '\ue004'_¶

    

CLEAR _ = '\ue005'_¶

    

RETURN _ = '\ue006'_¶

    

ENTER _ = '\ue007'_¶

    

SHIFT _ = '\ue008'_¶

    

LEFT_SHIFT _ = '\ue008'_¶

    

CONTROL _ = '\ue009'_¶

    

LEFT_CONTROL _ = '\ue009'_¶

    

ALT _ = '\ue00a'_¶

    

LEFT_ALT _ = '\ue00a'_¶

    

PAUSE _ = '\ue00b'_¶

    

ESCAPE _ = '\ue00c'_¶

    

SPACE _ = '\ue00d'_¶

    

PAGE_UP _ = '\ue00e'_¶

    

PAGE_DOWN _ = '\ue00f'_¶

    

END _ = '\ue010'_¶

    

HOME _ = '\ue011'_¶

    

LEFT _ = '\ue012'_¶

    

ARROW_LEFT _ = '\ue012'_¶

    

UP _ = '\ue013'_¶

    

ARROW_UP _ = '\ue013'_¶

    

RIGHT _ = '\ue014'_¶

    

ARROW_RIGHT _ = '\ue014'_¶

    

DOWN _ = '\ue015'_¶

    

ARROW_DOWN _ = '\ue015'_¶

    

INSERT _ = '\ue016'_¶

    

DELETE _ = '\ue017'_¶

    

SEMICOLON _ = '\ue018'_¶

    

EQUALS _ = '\ue019'_¶

    

NUMPAD0 _ = '\ue01a'_¶

    

NUMPAD1 _ = '\ue01b'_¶

    

NUMPAD2 _ = '\ue01c'_¶

    

NUMPAD3 _ = '\ue01d'_¶

    

NUMPAD4 _ = '\ue01e'_¶

    

NUMPAD5 _ = '\ue01f'_¶

    

NUMPAD6 _ = '\ue020'_¶

    

NUMPAD7 _ = '\ue021'_¶

    

NUMPAD8 _ = '\ue022'_¶

    

NUMPAD9 _ = '\ue023'_¶

    

MULTIPLY _ = '\ue024'_¶

    

ADD _ = '\ue025'_¶

    

SEPARATOR _ = '\ue026'_¶

    

SUBTRACT _ = '\ue027'_¶

    

DECIMAL _ = '\ue028'_¶

    

DIVIDE _ = '\ue029'_¶

    

F1 _ = '\ue031'_¶

    

F2 _ = '\ue032'_¶

    

F3 _ = '\ue033'_¶

    

F4 _ = '\ue034'_¶

    

F5 _ = '\ue035'_¶

    

F6 _ = '\ue036'_¶

    

F7 _ = '\ue037'_¶

    

F8 _ = '\ue038'_¶

    

F9 _ = '\ue039'_¶

    

F10 _ = '\ue03a'_¶

    

F11 _ = '\ue03b'_¶

    

F12 _ = '\ue03c'_¶

    

META _ = '\ue03d'_¶

    

COMMAND _ = '\ue03d'_¶

    

ZENKAKU_HANKAKU _ = '\ue040'_¶

    

### Table of Contents

  * selenium.webdriver.common.keys
    * `Keys`
      * `Keys.NULL`
      * `Keys.CANCEL`
      * `Keys.HELP`
      * `Keys.BACKSPACE`
      * `Keys.BACK_SPACE`
      * `Keys.TAB`
      * `Keys.CLEAR`
      * `Keys.RETURN`
      * `Keys.ENTER`
      * `Keys.SHIFT`
      * `Keys.LEFT_SHIFT`
      * `Keys.CONTROL`
      * `Keys.LEFT_CONTROL`
      * `Keys.ALT`
      * `Keys.LEFT_ALT`
      * `Keys.PAUSE`
      * `Keys.ESCAPE`
      * `Keys.SPACE`
      * `Keys.PAGE_UP`
      * `Keys.PAGE_DOWN`
      * `Keys.END`
      * `Keys.HOME`
      * `Keys.LEFT`
      * `Keys.ARROW_LEFT`
      * `Keys.UP`
      * `Keys.ARROW_UP`
      * `Keys.RIGHT`
      * `Keys.ARROW_RIGHT`
      * `Keys.DOWN`
      * `Keys.ARROW_DOWN`
      * `Keys.INSERT`
      * `Keys.DELETE`
      * `Keys.SEMICOLON`
      * `Keys.EQUALS`
      * `Keys.NUMPAD0`
      * `Keys.NUMPAD1`
      * `Keys.NUMPAD2`
      * `Keys.NUMPAD3`
      * `Keys.NUMPAD4`
      * `Keys.NUMPAD5`
      * `Keys.NUMPAD6`
      * `Keys.NUMPAD7`
      * `Keys.NUMPAD8`
      * `Keys.NUMPAD9`
      * `Keys.MULTIPLY`
      * `Keys.ADD`
      * `Keys.SEPARATOR`
      * `Keys.SUBTRACT`
      * `Keys.DECIMAL`
      * `Keys.DIVIDE`
      * `Keys.F1`
      * `Keys.F2`
      * `Keys.F3`
      * `Keys.F4`
      * `Keys.F5`
      * `Keys.F6`
      * `Keys.F7`
      * `Keys.F8`
      * `Keys.F9`
      * `Keys.F10`
      * `Keys.F11`
      * `Keys.F12`
      * `Keys.META`
      * `Keys.COMMAND`
      * `Keys.ZENKAKU_HANKAKU`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.keys

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Input Device

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.actions.input_device¶](#seleniumwebdrivercommonactionsinput_device)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.input_device


Classes

`InputDevice`([name]) | Describes the input device being used for the action.  
---|---  
  
_class _selenium.webdriver.common.actions.input_device.InputDevice(_name : str | None = None_)[source]¶
    

Describes the input device being used for the action.

add_action(_action : Any_) -> None[source]¶

    

clear_actions() -> None[source]¶

    

create_pause(_duration : float = 0_) -> None[source]¶

    

### Table of Contents

  * selenium.webdriver.common.actions.input_device
    * `InputDevice`
      * `InputDevice.add_action()`
      * `InputDevice.clear_actions()`
      * `InputDevice.create_pause()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.actions.input_device

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Actions.Pointer Actions

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

## Timeouts

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

## Proxy

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.proxy¶](#seleniumwebdrivercommonproxy)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
  - [Usage¶](#usage)
  - [Parameter¶](#parameter)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.proxy


The Proxy implementation.

Classes

`Proxy`([raw]) | Proxy contains information about proxy type and necessary proxy settings.  
---|---  
`ProxyType`() | Set of possible types of proxy.  
`ProxyTypeFactory`() | Factory for proxy types.  
  
_class _selenium.webdriver.common.proxy.ProxyTypeFactory[source]¶

    

Factory for proxy types.

_static _make(_ff_value_ , _string_)[source]¶

    

_class _selenium.webdriver.common.proxy.ProxyType[source]¶

    

Set of possible types of proxy.

Each proxy type has 2 properties: ‘ff_value’ is value of Firefox profile
preference, ‘string’ is id of proxy type.

DIRECT _ = {'ff_value': 0, 'string': 'DIRECT'}_¶

    

MANUAL _ = {'ff_value': 1, 'string': 'MANUAL'}_¶

    

PAC _ = {'ff_value': 2, 'string': 'PAC'}_¶

    

RESERVED_1 _ = {'ff_value': 3, 'string': 'RESERVED1'}_¶

    

AUTODETECT _ = {'ff_value': 4, 'string': 'AUTODETECT'}_¶

    

SYSTEM _ = {'ff_value': 5, 'string': 'SYSTEM'}_¶

    

UNSPECIFIED _ = {'ff_value': 6, 'string': 'UNSPECIFIED'}_¶

    

_classmethod _load(_value_)[source]¶

    

_class _selenium.webdriver.common.proxy.Proxy(_raw =None_)[source]¶

    

Proxy contains information about proxy type and necessary proxy settings.

Creates a new Proxy.

Args:

    

  * raw: raw proxy data. If None, default class values are used.

proxyType _ = {'ff_value': 6, 'string': 'UNSPECIFIED'}_¶

    

autodetect _ = False_¶

    

ftpProxy _ = ''_¶

    

httpProxy _ = ''_¶

    

noProxy _ = ''_¶

    

proxyAutoconfigUrl _ = ''_¶

    

socksProxy _ = ''_¶

    

socksUsername _ = ''_¶

    

socksPassword _ = ''_¶

    

socksVersion _ = None_¶

    

ssl_proxy¶

    

Gets and Sets ssl_proxy

## Usage¶

  * Get
    
    * self.ssl_proxy

  * Set
    
    * self.ssl_proxy = value

## Parameter¶

value: str

ftp_proxy¶

    

Gets and Sets ftp_proxy

## Usage¶

  * Get
    
    * self.ftp_proxy

  * Set
    
    * self.ftp_proxy = value

## Parameters¶

value: str

http_proxy¶

    

Gets and Sets http_proxy

## Usage¶

  * Get
    
    * self.http_proxy

  * Set
    
    * self.http_proxy = value

## Parameters¶

value: str

no_proxy¶

    

Gets and Sets no_proxy

## Usage¶

  * Get
    
    * self.no_proxy

  * Set
    
    * self.no_proxy = value

## Parameters¶

value: str

proxy_autoconfig_url¶

    

Gets and Sets proxy_autoconfig_url

## Usage¶

  * Get
    
    * self.proxy_autoconfig_url

  * Set
    
    * self.proxy_autoconfig_url = value

## Parameter¶

value: str

sslProxy _ = ''_¶

    

auto_detect¶

    

Gets and Sets auto_detect

## Usage¶

  * Get
    
    * self.auto_detect

  * Set
    
    * self.auto_detect = value

## Parameters¶

value: str

socks_proxy¶

    

Gets and Sets socks_proxy

## Usage¶

  * Get
    
    * self.sock_proxy

  * Set
    
    * self.socks_proxy = value

## Parameter¶

value: str

socks_username¶

    

Gets and Sets socks_password

## Usage¶

  * Get
    
    * self.socks_password

  * Set
    
    * self.socks_password = value

## Parameter¶

value: str

socks_password¶

    

Gets and Sets socks_password

## Usage¶

  * Get
    
    * self.socks_password

  * Set
    
    * self.socks_password = value

## Parameter¶

value: str

socks_version¶

    

Gets and Sets socks_version

## Usage¶

  * Get
    
    * self.socks_version

  * Set
    
    * self.socks_version = value

## Parameter¶

value: str

_property _proxy_type¶

    

Returns proxy type as ProxyType.

to_capabilities()[source]¶

    

### Table of Contents

  * selenium.webdriver.common.proxy
    * `ProxyTypeFactory`
      * `ProxyTypeFactory.make()`
    * `ProxyType`
      * `ProxyType.DIRECT`
      * `ProxyType.MANUAL`
      * `ProxyType.PAC`
      * `ProxyType.RESERVED_1`
      * `ProxyType.AUTODETECT`
      * `ProxyType.SYSTEM`
      * `ProxyType.UNSPECIFIED`
      * `ProxyType.load()`
    * `Proxy`
      * `Proxy.proxyType`
      * `Proxy.autodetect`
      * `Proxy.ftpProxy`
      * `Proxy.httpProxy`
      * `Proxy.noProxy`
      * `Proxy.proxyAutoconfigUrl`
      * `Proxy.socksProxy`
      * `Proxy.socksUsername`
      * `Proxy.socksPassword`
      * `Proxy.socksVersion`
      * `Proxy.ssl_proxy`
      * `Proxy.ftp_proxy`
      * `Proxy.http_proxy`
      * `Proxy.no_proxy`
      * `Proxy.proxy_autoconfig_url`
      * `Proxy.sslProxy`
      * `Proxy.auto_detect`
      * `Proxy.socks_proxy`
      * `Proxy.socks_username`
      * `Proxy.socks_password`
      * `Proxy.socks_version`
      * `Proxy.proxy_type`
      * `Proxy.to_capabilities()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.proxy

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Print Page Options

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.print_page_options¶](#seleniumwebdrivercommonprint_page_options)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.print_page_options


Classes

`PrintOptions`() |   
---|---  
  
_class _selenium.webdriver.common.print_page_options.PrintOptions[source]¶

    

page_height¶

    

Gets and Sets page_height:

## Usage¶

  * Get
    
    * self.page_height

  * Set
    
    * self.page_height = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

page_width¶

    

Gets and Sets page_width:

## Usage¶

  * Get
    
    * self.page_width

  * Set
    
    * self.page_width = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

margin_top¶

    

Gets and Sets margin_top:

## Usage¶

  * Get
    
    * self.margin_top

  * Set
    
    * self.margin_top = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

margin_bottom¶

    

Gets and Sets margin_bottom:

## Usage¶

  * Get
    
    * self.margin_bottom

  * Set
    
    * self.margin_bottom = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

margin_left¶

    

Gets and Sets margin_left:

## Usage¶

  * Get
    
    * self.margin_left

  * Set
    
    * self.margin_left = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

margin_right¶

    

Gets and Sets margin_right:

## Usage¶

  * Get
    
    * self.margin_right

  * Set
    
    * self.margin_right = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

scale¶

    

Gets and Sets scale:

## Usage¶

  * Get
    
    * self.scale

  * Set
    
    * self.scale = value

## Parameters¶

value: float

## Returns¶

  * Get
    
    * Optional[float]

  * Set
    
    * None

orientation¶

    

Gets and Sets orientation:

## Usage¶

  * Get
    
    * self.orientation

  * Set
    
    * self.orientation = value

## Parameters¶

value: Orientation

## Returns¶

  * Get
    
    * Optional[Orientation]

  * Set
    
    * None

background¶

    

Gets and Sets background:

## Usage¶

  * Get
    
    * self.background

  * Set
    
    * self.background = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * Optional[bool]

  * Set
    
    * None

shrink_to_fit¶

    

Gets and Sets shrink_to_fit:

## Usage¶

  * Get
    
    * self.shrink_to_fit

  * Set
    
    * self.shrink_to_fit = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * Optional[bool]

  * Set
    
    * None

page_ranges¶

    

Gets and Sets page_ranges:

## Usage¶

  * Get
    
    * self.page_ranges

  * Set
    
    * self.page_ranges = value

## Parameters¶

value: ` List[str]`

## Returns¶

  * Get
    
    * Optional[List[str]]

  * Set
    
    * None

to_dict() -> Dict[str, Any][source]¶

    

Returns:

    

A hash of print options configured.

### Table of Contents

  * selenium.webdriver.common.print_page_options
    * `PrintOptions`
      * `PrintOptions.page_height`
      * `PrintOptions.page_width`
      * `PrintOptions.margin_top`
      * `PrintOptions.margin_bottom`
      * `PrintOptions.margin_left`
      * `PrintOptions.margin_right`
      * `PrintOptions.scale`
      * `PrintOptions.orientation`
      * `PrintOptions.background`
      * `PrintOptions.shrink_to_fit`
      * `PrintOptions.page_ranges`
      * `PrintOptions.to_dict()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.print_page_options

(C) Copyright 2009-2024 Software Freedom Conservancy.

## Selenium Manager

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.selenium_manager¶](#seleniumwebdrivercommonselenium_manager)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.selenium_manager


Classes

`SeleniumManager`() | Wrapper for getting information from the Selenium Manager binaries.  
---|---  
  
_class _selenium.webdriver.common.selenium_manager.SeleniumManager[source]¶

    

Wrapper for getting information from the Selenium Manager binaries.

This implementation is still in beta, and may change.

binary_paths(_args : List_) -> dict[source]¶

    

Determines the locations of the requested assets.

Args:

    

  * args: the commands to send to the selenium manager binary.

Returns:

    

dictionary of assets and their path

### Table of Contents

  * selenium.webdriver.common.selenium_manager
    * `SeleniumManager`
      * `SeleniumManager.binary_paths()`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.selenium_manager

(C) Copyright 2009-2024 Software Freedom Conservancy.


## Chrome.Service

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

## Chrome.Options

---
title: Www.Selenium.Dev 20250105 151049
type: reference
---

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.chrome.options¶](#seleniumwebdriverchromeoptions)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
  - [Usage¶](#usage)
  - [Parameters¶](#parameters)
  - [Returns¶](#returns)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.options


Classes

`Options`() |   
---|---  
  
_class _selenium.webdriver.chrome.options.Options[source]¶

    

_property _default_capabilities _: dict_¶

    

Return minimal capabilities necessary as a dictionary.

enable_mobile(_android_package : str | None = 'com.android.chrome'_, _android_activity : str | None = None_, _device_serial : str | None = None_) → None[source]¶
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

BINARY_LOCATION_ERROR _ = 'Binary Location Must be a String'_¶

    

KEY _ = 'goog:chromeOptions'_¶

    

add_argument(_argument_) → None¶

    

Adds an argument to the list.

Args:

    

  * Sets the arguments

add_encoded_extension(_extension : str_) → None¶

    

Adds Base64 encoded string with extension data to a list that will be used to
extract it to the ChromeDriver.

Args:

    

  * extension: Base64 encoded string with extension data

add_experimental_option(_name : str_, _value : str | int | dict | List[str]_) → None¶
    

Adds an experimental option which is passed to chromium.

Args:

    

name: The experimental option name. value: The option value.

add_extension(_extension : str_) → None¶

    

Adds the path to the extension to a list that will be used to extract it to
the ChromeDriver.

Args:

    

  * extension: path to the *.crx file

_property _arguments¶

    

Returns:

    

A list of arguments needed for the browser.

_property _binary_location _: str_¶

    

Returns:

    

The location of the binary, otherwise an empty string.

_property _capabilities¶

    

_property _debugger_address _: str | None_¶
    

Returns:

    

The address of the remote devtools instance.

_property _experimental_options _: dict_¶

    

Returns:

    

A dictionary of experimental options for chromium.

_property _extensions _: List[str]_¶

    

Returns:

    

A list of encoded extensions that will be loaded.

ignore_local_proxy_environment_variables() → None¶

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

set_capability(_name_ , _value_) → None¶

    

Sets a capability.

to_capabilities() → dict¶

    

Creates a capabilities with all the options that have been set :Returns: A
dictionary with everything.

browser_version¶

    

Gets and Sets the version of the browser.

## Usage¶

  * Get
    
    * self.browser_version

  * Set
    
    * self.browser_version = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

platform_name¶

    

Gets and Sets name of the platform.

## Usage¶

  * Get
    
    * self.platform_name

  * Set
    
    * self.platform_name = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

accept_insecure_certs¶

    

Gets and Set whether the session accepts insecure certificates.

## Usage¶

  * Get
    
    * self.accept_insecure_certs

  * Set
    
    * self.accept_insecure_certs = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

strict_file_interactability¶

    

Gets and Sets whether session is about file interactability.

## Usage¶

  * Get
    
    * self.strict_file_interactability

  * Set
    
    * self.strict_file_interactability = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

set_window_rect¶

    

Gets and Sets window size and position.

## Usage¶

  * Get
    
    * self.set_window_rect

  * Set
    
    * self.set_window_rect = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

enable_bidi¶

    

Gets and Set whether the session has WebDriverBiDi enabled.

## Usage¶

  * Get
    
    * self.enable_bidi

  * Set
    
    * self.enable_bidi = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

web_socket_url¶

    

Gets and Sets WebSocket URL.

## Usage¶

  * Get
    
    * self.web_socket_url

  * Set
    
    * self.web_socket_url = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

page_load_strategy¶

    

:Gets and Sets page load strategy, the default is “normal”.

## Usage¶

  * Get
    
    * self.page_load_strategy

  * Set
    
    * self.page_load_strategy = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

unhandled_prompt_behavior¶

    

:Gets and Sets unhandled prompt behavior, the default is “dismiss and notify”.

## Usage¶

  * Get
    
    * self.unhandled_prompt_behavior

  * Set
    
    * self.unhandled_prompt_behavior = value

## Parameters¶

value: str

## Returns¶

  * Get
    
    * str

  * Set
    
    * None

timeouts¶

    

:Gets and Sets implicit timeout, pageLoad timeout and script timeout if set
(in milliseconds)

## Usage¶

  * Get
    
    * self.timeouts

  * Set
    
    * self.timeouts = value

## Parameters¶

value: dict

## Returns¶

  * Get
    
    * dict

  * Set
    
    * None

proxy¶

    

Sets and Gets Proxy.

## Usage¶

  * Get
    
    * self.proxy

  * Set
    
    * self.proxy = value

## Parameters¶

value: Proxy

## Returns¶

  * Get
    
    * Proxy

  * Set
    
    * None

enable_downloads¶

    

Gets and Sets whether session can download files.

## Usage¶

  * Get
    
    * self.enable_downloads

  * Set
    
    * self.enable_downloads = value

## Parameters¶

value: bool

## Returns¶

  * Get
    
    * bool

  * Set
    
    * None

### Table of Contents

  * selenium.webdriver.chrome.options
    * `Options`
      * `Options.default_capabilities`
      * `Options.enable_mobile()`
      * `Options.BINARY_LOCATION_ERROR`
      * `Options.KEY`
      * `Options.add_argument()`
      * `Options.add_encoded_extension()`
      * `Options.add_experimental_option()`
      * `Options.add_extension()`
      * `Options.arguments`
      * `Options.binary_location`
      * `Options.capabilities`
      * `Options.debugger_address`
      * `Options.experimental_options`
      * `Options.extensions`
      * `Options.ignore_local_proxy_environment_variables()`
      * `Options.set_capability()`
      * `Options.to_capabilities()`
      * `Options.browser_version`
      * `Options.platform_name`
      * `Options.accept_insecure_certs`
      * `Options.strict_file_interactability`
      * `Options.set_window_rect`
      * `Options.enable_bidi`
      * `Options.web_socket_url`
      * `Options.page_load_strategy`
      * `Options.unhandled_prompt_behavior`
      * `Options.timeouts`
      * `Options.proxy`
      * `Options.enable_downloads`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.options

© Copyright 2009-2024 Software Freedom Conservancy.

## Chrome.Webdriver

---
title: Www.Selenium.Dev 20250105 151122
type: reference
---

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.chrome.webdriver¶](#seleniumwebdriverchromewebdriver)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.webdriver


Classes

`WebDriver`([options, service, keep_alive]) | Controls the ChromeDriver and allows you to drive the browser.  
---|---  
  
_class _selenium.webdriver.chrome.webdriver.WebDriver(_options : Options | None = None_, _service : Service | None = None_, _keep_alive : bool = True_)[source]¶
    

Controls the ChromeDriver and allows you to drive the browser.

Creates a new instance of the chrome driver. Starts the service and then
creates new instance of chrome driver.

Args:

    

  * options - this takes an instance of ChromeOptions

  * service - Service object for handling the browser driver if you need to pass extra details

  * keep_alive - Whether to configure ChromeRemoteConnection to use HTTP keep-alive.

add_cookie(_cookie_dict_) → None[source]¶

    

Adds a cookie to your current session.

Args:

    

  * cookie_dict: A dictionary object, with required keys - “name” and “value”;
    

optional keys - “path”, “domain”, “secure”, “httpOnly”, “expiry”, “sameSite”

Usage:

    
    
    
    driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
    driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})
    driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure' : True})
    driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'sameSite' : 'Strict'})
    

add_credential(_credential : Credential_) → None[source]¶

    

Injects a credential into the authenticator.

add_virtual_authenticator(_options : VirtualAuthenticatorOptions_) →
None[source]¶

    

Adds a virtual authenticator with the given options.

back() → None[source]¶

    

Goes one step backward in the browser history.

Usage:

    
    
    
    driver.back()
    

bidi_connection()[source]¶

    

_property _capabilities _: dict_¶

    

Returns the drivers current capabilities being used.

close() → None[source]¶

    

Closes the current window.

Usage:

    
    
    
    driver.close()
    

create_web_element(_element_id : str_) → WebElement[source]¶

    

Creates a web element with the specified element_id.

_property _current_url _: str_¶

    

Gets the URL of the current page.

Usage:

    
    
    
    driver.current_url
    

_property _current_window_handle _: str_¶

    

Returns the handle of the current window.

Usage:

    
    
    
    driver.current_window_handle
    

delete_all_cookies() → None[source]¶

    

Delete all cookies in the scope of the session.

Usage:

    
    
    
    driver.delete_all_cookies()
    

delete_cookie(_name_) → None[source]¶

    

Deletes a single cookie with the given name.

Usage:

    
    
    
    driver.delete_cookie('my_cookie')
    

delete_downloadable_files() → None[source]¶

    

Deletes all downloadable files.

delete_network_conditions() → None¶

    

Resets Chromium network emulation settings.

download_file(_file_name : str_, _target_directory : str_) → None[source]¶

    

Downloads a file with the specified file name to the target directory.

file_name: The name of the file to download. target_directory: The path to the
directory to save the downloaded file.

execute(_driver_command : str_, _params : dict | None = None_) → dict[source]¶
    

Sends a command to be executed by a command.CommandExecutor.

Args:

    

  * driver_command: The name of the command to execute as a string.

  * params: A dictionary of named parameters to send with the command.

Returns:

    

The command’s JSON response loaded into a dictionary object.

execute_async_script(_script : str_, _* args_)[source]¶

    

Asynchronously Executes JavaScript in the current window/frame.

Args:

    

  * script: The JavaScript to execute.

  * *args: Any applicable arguments for your JavaScript.

Usage:

    
    
    
    script = "var callback = arguments[arguments.length - 1]; " \
             "window.setTimeout(function(){ callback('timeout') }, 3000);"
    driver.execute_async_script(script)
    

execute_cdp_cmd(_cmd : str_, _cmd_args : dict_)¶

    

Execute Chrome Devtools Protocol command and get returned result The command
and command args should follow chrome devtools protocol domains/commands,
refer to link https://chromedevtools.github.io/devtools-protocol/

Args:

    

  * cmd: A str, command name

  * cmd_args: A dict, command args. empty dict {} if there is no command args

Usage:

    
    
    
    driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
    

Returns:

    

A dict, empty dict {} if there is no result to return. For example to
getResponseBody: {‘base64Encoded’: False, ‘body’: ‘response body string’}

execute_script(_script_ , _* args_)[source]¶

    

Synchronously Executes JavaScript in the current window/frame.

Args:

    

  * script: The JavaScript to execute.

  * *args: Any applicable arguments for your JavaScript.

Usage:

    
    
    
    driver.execute_script('return document.title;')
    

_property _file_detector _: FileDetector_¶

    

file_detector_context(_file_detector_class_ , _* args_, _** kwargs_)[source]¶

    

Overrides the current file detector (if necessary) in limited context. Ensures
the original file detector is set afterwards.

Example:

    
    
    with webdriver.file_detector_context(UselessFileDetector):
        someinput.send_keys('/etc/hosts')
    

Args:

    

  * file_detector_class - Class of the desired file detector. If the class is different
    

from the current file_detector, then the class is instantiated with args and
kwargs and used as a file detector during the duration of the context manager.

  * args - Optional arguments that get passed to the file detector class during
    

instantiation.

  * kwargs - Keyword arguments, passed the same way as args.

find_element(_by ='id'_, _value : str | None = None_) → WebElement[source]¶
    

Find an element given a By strategy and locator.

Usage:

    
    
    
    element = driver.find_element(By.ID, 'foo')
    

Return type:

    

WebElement

find_elements(_by ='id'_, _value : str | None = None_) → List[WebElement][source]¶
    

Find elements given a By strategy and locator.

Usage:

    
    
    
    elements = driver.find_elements(By.CLASS_NAME, 'foo')
    

Return type:

    

list of WebElement

forward() → None[source]¶

    

Goes one step forward in the browser history.

Usage:

    
    
    
    driver.forward()
    

fullscreen_window() → None[source]¶

    

Invokes the window manager-specific ‘full screen’ operation.

get(_url : str_) → None[source]¶

    

Loads a web page in the current browser session.

get_cookie(_name_) → Dict | None[source]¶
    

Get a single cookie by name. Returns the cookie if found, None if not.

Usage:

    
    
    
    driver.get_cookie('my_cookie')
    

get_cookies() → List[dict][source]¶

    

Returns a set of dictionaries, corresponding to cookies visible in the current
session.

Usage:

    
    
    
    driver.get_cookies()
    

get_credentials() → List[Credential][source]¶

    

Returns the list of credentials owned by the authenticator.

get_downloadable_files() → dict[source]¶

    

Retrieves the downloadable files as a map of file names and their
corresponding URLs.

get_issue_message()¶

    

Returns:

    

An error message when there is any issue in a Cast

session.

get_log(_log_type_)[source]¶

    

Gets the log for a given log type.

Args:

    

  * log_type: type of log that which will be returned

Usage:

    
    
    
    driver.get_log('browser')
    driver.get_log('driver')
    driver.get_log('client')
    driver.get_log('server')
    

get_network_conditions()¶

    

Gets Chromium network emulation settings.

Returns:

    

A dict. For example: {‘latency’: 4,

‘download_throughput’: 2, ‘upload_throughput’: 2, ‘offline’: False}

get_pinned_scripts() → List[str][source]¶

    

get_screenshot_as_base64() → str[source]¶

    

Gets the screenshot of the current window as a base64 encoded string which is
useful in embedded images in HTML.

Usage:

    
    
    
    driver.get_screenshot_as_base64()
    

get_screenshot_as_file(_filename_) → bool[source]¶

    

Saves a screenshot of the current window to a PNG image file. Returns False if
there is any IOError, else returns True. Use full paths in your filename.

Args:

    

  * filename: The full path you wish to save your screenshot to. This should end with a .png extension.

Usage:

    
    
    
    driver.get_screenshot_as_file('/Screenshots/foo.png')
    

get_screenshot_as_png() → bytes[source]¶

    

Gets the screenshot of the current window as a binary data.

Usage:

    
    
    
    driver.get_screenshot_as_png()
    

get_sinks() → list¶

    

Returns:

    

A list of sinks available for Cast.

get_window_position(_windowHandle ='current'_) → dict[source]¶

    

Gets the x,y position of the current window.

Usage:

    
    
    
    driver.get_window_position()
    

get_window_rect() → dict[source]¶

    

Gets the x, y coordinates of the window as well as height and width of the
current window.

Usage:

    
    
    
    driver.get_window_rect()
    

get_window_size(_windowHandle : str = 'current'_) → dict[source]¶

    

Gets the width and height of the current window.

Usage:

    
    
    
    driver.get_window_size()
    

implicitly_wait(_time_to_wait : float_) → None[source]¶

    

Sets a sticky timeout to implicitly wait for an element to be found, or a
command to complete. This method only needs to be called one time per session.
To set the timeout for calls to execute_async_script, see set_script_timeout.

Args:

    

  * time_to_wait: Amount of time to wait (in seconds)

Usage:

    
    
    
    driver.implicitly_wait(30)
    

launch_app(_id_)¶

    

Launches Chromium app specified by id.

_property _log_types¶

    

Gets a list of the available log types. This only works with w3c compliant
browsers.

Usage:

    
    
    
    driver.log_types
    

maximize_window() → None[source]¶

    

Maximizes the current window that webdriver is using.

minimize_window() → None[source]¶

    

Invokes the window manager-specific ‘minimize’ operation.

_property _mobile _: Mobile_¶

    

_property _name _: str_¶

    

Returns the name of the underlying browser for this instance.

Usage:

    
    
    
    name = driver.name
    

_property _orientation¶

    

Gets the current orientation of the device.

Usage:

    
    
    
    orientation = driver.orientation
    

_property _page_source _: str_¶

    

Gets the source of the current page.

Usage:

    
    
    
    driver.page_source
    

pin_script(_script : str_, _script_key =None_) → ScriptKey[source]¶

    

Store common javascript scripts to be executed later by a unique hashable ID.

print_page(_print_options : PrintOptions | None = None_) → str[source]¶
    

Takes PDF of the current page.

The driver makes a best effort to return a PDF based on the provided
parameters.

quit() → None¶

    

Closes the browser and shuts down the ChromiumDriver executable.

refresh() → None[source]¶

    

Refreshes the current page.

Usage:

    
    
    
    driver.refresh()
    

remove_all_credentials() → None[source]¶

    

Removes all credentials from the authenticator.

remove_credential(_credential_id : str | bytearray_) → None[source]¶
    

Removes a credential from the authenticator.

remove_virtual_authenticator() → None[source]¶

    

Removes a previously added virtual authenticator.

The authenticator is no longer valid after removal, so no methods may be
called.

save_screenshot(_filename_) → bool[source]¶

    

Saves a screenshot of the current window to a PNG image file. Returns False if
there is any IOError, else returns True. Use full paths in your filename.

Args:

    

  * filename: The full path you wish to save your screenshot to. This should end with a .png extension.

Usage:

    
    
    
    driver.save_screenshot('/Screenshots/foo.png')
    

_property _script¶

    

set_network_conditions(_** network_conditions_) → None¶

    

Sets Chromium network emulation settings.

Args:

    

  * network_conditions: A dict with conditions specification.

Usage:

    
    
    
    driver.set_network_conditions(
        offline=False,
        latency=5,  # additional latency (ms)
        download_throughput=500 * 1024,  # maximal throughput
        upload_throughput=500 * 1024)  # maximal throughput
    

Note: ‘throughput’ can be used to set both (for download and upload).

set_page_load_timeout(_time_to_wait : float_) → None[source]¶

    

Set the amount of time to wait for a page load to complete before throwing an
error.

Args:

    

  * time_to_wait: The amount of time to wait

Usage:

    
    
    
    driver.set_page_load_timeout(30)
    

set_permissions(_name : str_, _value : str_) → None¶

    

Sets Applicable Permission.

Args:

    

  * name: The item to set the permission on.

  * value: The value to set on the item

Usage:

    
    
    
    driver.set_permissions('clipboard-read', 'denied')
    

set_script_timeout(_time_to_wait : float_) → None[source]¶

    

Set the amount of time that the script should wait during an
execute_async_script call before throwing an error.

Args:

    

  * time_to_wait: The amount of time to wait (in seconds)

Usage:

    
    
    
    driver.set_script_timeout(30)
    

set_sink_to_use(_sink_name : str_) → dict¶

    

Sets a specific sink, using its name, as a Cast session receiver target.

Args:

    

  * sink_name: Name of the sink to use as the target.

set_user_verified(_verified : bool_) → None[source]¶

    

Sets whether the authenticator will simulate success or fail on user
verification.

verified: True if the authenticator will pass user verification, False
otherwise.

set_window_position(_x : float_, _y : float_, _windowHandle : str =
'current'_) → dict[source]¶

    

Sets the x,y position of the current window. (window.moveTo)

Args:

    

  * x: the x-coordinate in pixels to set the window position

  * y: the y-coordinate in pixels to set the window position

Usage:

    
    
    
    driver.set_window_position(0,0)
    

set_window_rect(_x =None_, _y =None_, _width =None_, _height =None_) →
dict[source]¶

    

Sets the x, y coordinates of the window as well as height and width of the
current window. This method is only supported for W3C compatible browsers;
other browsers should use set_window_position and set_window_size.

Usage:

    
    
    
    driver.set_window_rect(x=10, y=10)
    driver.set_window_rect(width=100, height=200)
    driver.set_window_rect(x=10, y=10, width=100, height=200)
    

set_window_size(_width_ , _height_ , _windowHandle : str = 'current'_) →
None[source]¶

    

Sets the width and height of the current window. (window.resizeTo)

Args:

    

  * width: the width in pixels to set the window to

  * height: the height in pixels to set the window to

Usage:

    
    
    
    driver.set_window_size(800,600)
    

start_client()[source]¶

    

Called before starting a new session.

This method may be overridden to define custom startup behavior.

start_desktop_mirroring(_sink_name : str_) → dict¶

    

Starts a desktop mirroring session on a specific receiver target.

Args:

    

  * sink_name: Name of the sink to use as the target.

start_devtools()[source]¶

    

start_session(_capabilities : dict_) → None[source]¶

    

Creates a new session with the desired capabilities.

Args:

    

  * capabilities - a capabilities dict to start the session with.

start_tab_mirroring(_sink_name : str_) → dict¶

    

Starts a tab mirroring session on a specific receiver target.

Args:

    

  * sink_name: Name of the sink to use as the target.

stop_casting(_sink_name : str_) → dict¶

    

Stops the existing Cast session on a specific receiver target.

Args:

    

  * sink_name: Name of the sink to stop the Cast session.

stop_client()[source]¶

    

Called after executing a quit command.

This method may be overridden to define custom shutdown behavior.

_property _switch_to _: SwitchTo_¶

    

Returns:

    

  * SwitchTo: an object containing all options to switch focus into

Usage:

    
    
    
    element = driver.switch_to.active_element
    alert = driver.switch_to.alert
    driver.switch_to.default_content()
    driver.switch_to.frame('frame_name')
    driver.switch_to.frame(1)
    driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
    driver.switch_to.parent_frame()
    driver.switch_to.window('main')
    

_property _timeouts _: Timeouts_¶

    

Get all the timeouts that have been set on the current session.

Usage:

    
    
    
    driver.timeouts
    

Return type:

    

Timeout

_property _title _: str_¶

    

Returns the title of the current page.

Usage:

    
    
    
    title = driver.title
    

unpin(_script_key : ScriptKey_) → None[source]¶

    

Remove a pinned script from storage.

_property _virtual_authenticator_id _: str_¶

    

Returns the id of the virtual authenticator.

_property _window_handles _: List[str]_¶

    

Returns the handles of all windows within the current session.

Usage:

    
    
    
    driver.window_handles
    

### Table of Contents

  * selenium.webdriver.chrome.webdriver
    * `WebDriver`
      * `WebDriver.add_cookie()`
      * `WebDriver.add_credential()`
      * `WebDriver.add_virtual_authenticator()`
      * `WebDriver.back()`
      * `WebDriver.bidi_connection()`
      * `WebDriver.capabilities`
      * `WebDriver.close()`
      * `WebDriver.create_web_element()`
      * `WebDriver.current_url`
      * `WebDriver.current_window_handle`
      * `WebDriver.delete_all_cookies()`
      * `WebDriver.delete_cookie()`
      * `WebDriver.delete_downloadable_files()`
      * `WebDriver.delete_network_conditions()`
      * `WebDriver.download_file()`
      * `WebDriver.execute()`
      * `WebDriver.execute_async_script()`
      * `WebDriver.execute_cdp_cmd()`
      * `WebDriver.execute_script()`
      * `WebDriver.file_detector`
      * `WebDriver.file_detector_context()`
      * `WebDriver.find_element()`
      * `WebDriver.find_elements()`
      * `WebDriver.forward()`
      * `WebDriver.fullscreen_window()`
      * `WebDriver.get()`
      * `WebDriver.get_cookie()`
      * `WebDriver.get_cookies()`
      * `WebDriver.get_credentials()`
      * `WebDriver.get_downloadable_files()`
      * `WebDriver.get_issue_message()`
      * `WebDriver.get_log()`
      * `WebDriver.get_network_conditions()`
      * `WebDriver.get_pinned_scripts()`
      * `WebDriver.get_screenshot_as_base64()`
      * `WebDriver.get_screenshot_as_file()`
      * `WebDriver.get_screenshot_as_png()`
      * `WebDriver.get_sinks()`
      * `WebDriver.get_window_position()`
      * `WebDriver.get_window_rect()`
      * `WebDriver.get_window_size()`
      * `WebDriver.implicitly_wait()`
      * `WebDriver.launch_app()`
      * `WebDriver.log_types`
      * `WebDriver.maximize_window()`
      * `WebDriver.minimize_window()`
      * `WebDriver.mobile`
      * `WebDriver.name`
      * `WebDriver.orientation`
      * `WebDriver.page_source`
      * `WebDriver.pin_script()`
      * `WebDriver.print_page()`
      * `WebDriver.quit()`
      * `WebDriver.refresh()`
      * `WebDriver.remove_all_credentials()`
      * `WebDriver.remove_credential()`
      * `WebDriver.remove_virtual_authenticator()`
      * `WebDriver.save_screenshot()`
      * `WebDriver.script`
      * `WebDriver.set_network_conditions()`
      * `WebDriver.set_page_load_timeout()`
      * `WebDriver.set_permissions()`
      * `WebDriver.set_script_timeout()`
      * `WebDriver.set_sink_to_use()`
      * `WebDriver.set_user_verified()`
      * `WebDriver.set_window_position()`
      * `WebDriver.set_window_rect()`
      * `WebDriver.set_window_size()`
      * `WebDriver.start_client()`
      * `WebDriver.start_desktop_mirroring()`
      * `WebDriver.start_devtools()`
      * `WebDriver.start_session()`
      * `WebDriver.start_tab_mirroring()`
      * `WebDriver.stop_casting()`
      * `WebDriver.stop_client()`
      * `WebDriver.switch_to`
      * `WebDriver.timeouts`
      * `WebDriver.title`
      * `WebDriver.unpin()`
      * `WebDriver.virtual_authenticator_id`
      * `WebDriver.window_handles`

### This Page

  * Show Source

### Quick search

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.webdriver

© Copyright 2009-2024 Software Freedom Conservancy.