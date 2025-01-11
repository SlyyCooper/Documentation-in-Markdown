## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.options](#seleniumwebdrivercommonoptions)
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
  * selenium.webdriver.common.options

# selenium.webdriver.common.options

Classes

`ArgOptions`() |   
---|---  
`BaseOptions`() | Base class for individual browser options.  
`PageLoadStrategy`(value) | Enum of possible page load strategies.  
  
_class _selenium.webdriver.common.options.PageLoadStrategy(_value_)[source]

    

Enum of possible page load strategies.

Selenium support following strategies:

    

  * normal (default) - waits for all resources to download

  * eager - DOM access is ready, but other resources like images may still be loading

  * none - does not block WebDriver at all

Docs:
https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy.

normal _ = 'normal'_

    

eager _ = 'eager'_

    

none _ = 'none'_

    

_class _selenium.webdriver.common.options.BaseOptions[source]

    

Base class for individual browser options.

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

_property _capabilities

    

set_capability(_name_ , _value_) -> None[source]

    

Sets a capability.

enable_mobile(_android_package : str | None = None_, _android_activity : str | None = None_, _device_serial : str | None = None_) -> None[source]
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

_abstract _to_capabilities()[source]

    

Convert options into capabilities dictionary.

_abstract property _default_capabilities

    

Return minimal capabilities necessary as a dictionary.

ignore_local_proxy_environment_variables() -> None[source]

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

_class _selenium.webdriver.common.options.ArgOptions[source]

    

_property _capabilities

    

enable_mobile(_android_package : str | None = None_, _android_activity : str | None = None_, _device_serial : str | None = None_) -> None
    

Enables mobile browser use for browsers that support it.

Args:

    

android_activity: The name of the android package to start

set_capability(_name_ , _value_) -> None

    

Sets a capability.

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

BINARY_LOCATION_ERROR _ = 'Binary Location Must be a String'_

    

_property _arguments

    

Returns:

    

A list of arguments needed for the browser.

add_argument(_argument_) -> None[source]

    

Adds an argument to the list.

Args:

    

  * Sets the arguments

ignore_local_proxy_environment_variables() -> None[source]

    

By calling this you will ignore HTTP_PROXY and HTTPS_PROXY from being picked
up and used.

to_capabilities()[source]

    

Convert options into capabilities dictionary.

_property _default_capabilities

    

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