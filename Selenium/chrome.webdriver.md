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

# selenium.webdriver.chrome.webdriver¶

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