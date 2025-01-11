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

# selenium.webdriver.common.desired_capabilities¶

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
    
    # Create a desired capabilities object as a starting point.
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"
    
    # Instantiate an instance of Remote WebDriver with the desired capabilities.
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