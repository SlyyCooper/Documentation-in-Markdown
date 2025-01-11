## Table of Contents

    - [Navigation](#navigation)
- [selenium.webdriver.common.proxy](#seleniumwebdrivercommonproxy)
  - [Usage](#usage)
  - [Parameter](#parameter)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Usage](#usage)
  - [Parameter](#parameter)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Usage](#usage)
  - [Parameter](#parameter)
  - [Usage](#usage)
  - [Parameter](#parameter)
  - [Usage](#usage)
  - [Parameter](#parameter)
  - [Usage](#usage)
  - [Parameter](#parameter)
    - [Table of Contents](#table-of-contents)
    - [This Page](#this-page)
    - [Quick search](#quick-search)
    - [Navigation](#navigation)

### Navigation

  * index
  * modules |
  * Selenium 4.25.0 documentation »
  * selenium.webdriver.common.proxy

# selenium.webdriver.common.proxy

The Proxy implementation.

Classes

`Proxy`([raw]) | Proxy contains information about proxy type and necessary proxy settings.  
---|---  
`ProxyType`() | Set of possible types of proxy.  
`ProxyTypeFactory`() | Factory for proxy types.  
  
_class _selenium.webdriver.common.proxy.ProxyTypeFactory[source]

    

Factory for proxy types.

_static _make(_ff_value_ , _string_)[source]

    

_class _selenium.webdriver.common.proxy.ProxyType[source]

    

Set of possible types of proxy.

Each proxy type has 2 properties: ‘ff_value’ is value of Firefox profile
preference, ‘string’ is id of proxy type.

DIRECT _ = {'ff_value': 0, 'string': 'DIRECT'}_

    

MANUAL _ = {'ff_value': 1, 'string': 'MANUAL'}_

    

PAC _ = {'ff_value': 2, 'string': 'PAC'}_

    

RESERVED_1 _ = {'ff_value': 3, 'string': 'RESERVED1'}_

    

AUTODETECT _ = {'ff_value': 4, 'string': 'AUTODETECT'}_

    

SYSTEM _ = {'ff_value': 5, 'string': 'SYSTEM'}_

    

UNSPECIFIED _ = {'ff_value': 6, 'string': 'UNSPECIFIED'}_

    

_classmethod _load(_value_)[source]

    

_class _selenium.webdriver.common.proxy.Proxy(_raw =None_)[source]

    

Proxy contains information about proxy type and necessary proxy settings.

Creates a new Proxy.

Args:

    

  * raw: raw proxy data. If None, default class values are used.

proxyType _ = {'ff_value': 6, 'string': 'UNSPECIFIED'}_

    

autodetect _ = False_

    

ftpProxy _ = ''_

    

httpProxy _ = ''_

    

noProxy _ = ''_

    

proxyAutoconfigUrl _ = ''_

    

socksProxy _ = ''_

    

socksUsername _ = ''_

    

socksPassword _ = ''_

    

socksVersion _ = None_

    

ssl_proxy

    

Gets and Sets ssl_proxy

## Usage

  * Get
    
    * self.ssl_proxy

  * Set
    
    * self.ssl_proxy = value

## Parameter

value: str

ftp_proxy

    

Gets and Sets ftp_proxy

## Usage

  * Get
    
    * self.ftp_proxy

  * Set
    
    * self.ftp_proxy = value

## Parameters

value: str

http_proxy

    

Gets and Sets http_proxy

## Usage

  * Get
    
    * self.http_proxy

  * Set
    
    * self.http_proxy = value

## Parameters

value: str

no_proxy

    

Gets and Sets no_proxy

## Usage

  * Get
    
    * self.no_proxy

  * Set
    
    * self.no_proxy = value

## Parameters

value: str

proxy_autoconfig_url

    

Gets and Sets proxy_autoconfig_url

## Usage

  * Get
    
    * self.proxy_autoconfig_url

  * Set
    
    * self.proxy_autoconfig_url = value

## Parameter

value: str

sslProxy _ = ''_

    

auto_detect

    

Gets and Sets auto_detect

## Usage

  * Get
    
    * self.auto_detect

  * Set
    
    * self.auto_detect = value

## Parameters

value: str

socks_proxy

    

Gets and Sets socks_proxy

## Usage

  * Get
    
    * self.sock_proxy

  * Set
    
    * self.socks_proxy = value

## Parameter

value: str

socks_username

    

Gets and Sets socks_password

## Usage

  * Get
    
    * self.socks_password

  * Set
    
    * self.socks_password = value

## Parameter

value: str

socks_password

    

Gets and Sets socks_password

## Usage

  * Get
    
    * self.socks_password

  * Set
    
    * self.socks_password = value

## Parameter

value: str

socks_version

    

Gets and Sets socks_version

## Usage

  * Get
    
    * self.socks_version

  * Set
    
    * self.socks_version = value

## Parameter

value: str

_property _proxy_type

    

Returns proxy type as ProxyType.

to_capabilities()[source]

    

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