---
title: Www.Selenium.Dev 20250105 151049
type: reference
---

## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.chrome.options](#seleniumwebdriverchromeoptions)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.chrome.options

# selenium.webdriver.chrome.options

Classes

`Options`() |   
---|---  
  
_class _selenium.webdriver.chrome.options.Options[source]

    

_property _default_capabilities _: dict_

    

Return minimal capabilities necessary as a dictionary.

enable_mobile(_android_package : str | None = 'com.android.chrome'_, _android_activity : str | None = None_, _device_serial : str | None = None_) → None[source]
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

BINARY_LOCATION_ERROR _ = 'Binary Location Must be a String'_

    

KEY _ = 'goog:chromeOptions'_

    

add_argument(_argument_) → None

    

Adds an argument to the list.

Args:

    

  * Sets the arguments

add_encoded_extension(_extension : str_) → None

    

Adds Base64 encoded string with extension data to a list that will be used to
extract it to the ChromeDriver.

Args:

    

  * extension: Base64 encoded string with extension data

add_experimental_option(_name : str_, _value : str | int | dict | List[str]_) → None
    

Adds an experimental option which is passed to chromium.

Args:

    

name: The experimental option name. value: The option value.

add_extension(_extension : str_) → None

    

Adds the path to the extension to a list that will be used to extract it to
the ChromeDriver.

Args:

    

  * extension: path to the *.crx file

_property _arguments

    

Returns:

    

A list of arguments needed for the browser.

_property _binary_location _: str_

    

Returns:

    

The location of the binary, otherwise an empty string.

_property _capabilities

    

_property _debugger_address _: str | None_
    

Returns:

    

The address of the remote devtools instance.

_property _experimental_options _: dict_

    

Returns:

    

A dictionary of experimental options for chromium.

_property _extensions _: List[str]_

    

Returns:

    

A list of encoded extensions that will be loaded.

ignore_local_proxy_environment_variables() → None

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

set_capability(_name_ , _value_) → None

    

Sets a capability.

to_capabilities() → dict

    

Creates a capabilities with all the options that have been set :Returns: A
dictionary with everything.

browser_version

    

Gets and Sets the version of the browser.

## Usage

  * Get
    
    * self.browser_version

  * Set
    
    * self.browser_version = value

## Parameters

value: str

## Returns

  * Get
    
    * str

  * Set
    
    * None

platform_name

    

Gets and Sets name of the platform.

## Usage

  * Get
    
    * self.platform_name

  * Set
    
    * self.platform_name = value

## Parameters

value: str

## Returns

  * Get
    
    * str

  * Set
    
    * None

accept_insecure_certs

    

Gets and Set whether the session accepts insecure certificates.

## Usage

  * Get
    
    * self.accept_insecure_certs

  * Set
    
    * self.accept_insecure_certs = value

## Parameters

value: bool

## Returns

  * Get
    
    * bool

  * Set
    
    * None

strict_file_interactability

    

Gets and Sets whether session is about file interactability.

## Usage

  * Get
    
    * self.strict_file_interactability

  * Set
    
    * self.strict_file_interactability = value

## Parameters

value: bool

## Returns

  * Get
    
    * bool

  * Set
    
    * None

set_window_rect

    

Gets and Sets window size and position.

## Usage

  * Get
    
    * self.set_window_rect

  * Set
    
    * self.set_window_rect = value

## Parameters

value: bool

## Returns

  * Get
    
    * bool

  * Set
    
    * None

enable_bidi

    

Gets and Set whether the session has WebDriverBiDi enabled.

## Usage

  * Get
    
    * self.enable_bidi

  * Set
    
    * self.enable_bidi = value

## Parameters

value: bool

## Returns

  * Get
    
    * bool

  * Set
    
    * None

web_socket_url

    

Gets and Sets WebSocket URL.

## Usage

  * Get
    
    * self.web_socket_url

  * Set
    
    * self.web_socket_url = value

## Parameters

value: bool

## Returns

  * Get
    
    * bool

  * Set
    
    * None

page_load_strategy

    

:Gets and Sets page load strategy, the default is “normal”.

## Usage

  * Get
    
    * self.page_load_strategy

  * Set
    
    * self.page_load_strategy = value

## Parameters

value: str

## Returns

  * Get
    
    * str

  * Set
    
    * None

unhandled_prompt_behavior

    

:Gets and Sets unhandled prompt behavior, the default is “dismiss and notify”.

## Usage

  * Get
    
    * self.unhandled_prompt_behavior

  * Set
    
    * self.unhandled_prompt_behavior = value

## Parameters

value: str

## Returns

  * Get
    
    * str

  * Set
    
    * None

timeouts

    

:Gets and Sets implicit timeout, pageLoad timeout and script timeout if set
(in milliseconds)

## Usage

  * Get
    
    * self.timeouts

  * Set
    
    * self.timeouts = value

## Parameters

value: dict

## Returns

  * Get
    
    * dict

  * Set
    
    * None

proxy

    

Sets and Gets Proxy.

## Usage

  * Get
    
    * self.proxy

  * Set
    
    * self.proxy = value

## Parameters

value: Proxy

## Returns

  * Get
    
    * Proxy

  * Set
    
    * None

enable_downloads

    

Gets and Sets whether session can download files.

## Usage

  * Get
    
    * self.enable_downloads

  * Set
    
    * self.enable_downloads = value

## Parameters

value: bool

## Returns

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