Below is an **enhanced and consolidated** **Selenium 4.25 for Python** documentation, **combining** references from the official API style listings **plus** an expanded usage guide, best practices, and comprehensive examples. This resource strives to be the **ultimate** up-to-date single doc (as of January 2025). It covers:

- **Installation and Setup**  
- **Browser Drivers (Chrome, Firefox, Edge, Safari, WebKitGTK, etc.)**  
- **Key Classes and Usage**  
- **Advanced Topics** (Actions, BiDi, DevTools, Virtual Authenticator, FedCM, Proxy, Print PDF, etc.)  
- **Code Snippets, How-Tos, and Best Practices**  

Enjoy and happy automation!

---

# **Selenium 4.25 for Python – Comprehensive Reference & How-To**

## 1. Introduction & Overview

**Selenium** is a suite of libraries and tools to **automate web browsers**. In Python, it allows you to:

- Spin up and manage browser sessions (Chrome, Firefox, Edge, Safari, IE, etc.).
- Perform actions (click, type, drag, scroll, etc.) on web elements.
- Integrate advanced features (headless mode, remote execution on Selenium Grid, mobile emulation, network throttling, more).
- Handle modern scenarios (federated sign-on dialogs, webauthn virtual devices, DevTools logging, etc.).

**This single doc merges** official “API references” with practical how-to instructions for both **new** and **advanced** Python developers looking to automate browsers with Selenium 4.25.

---

## 2. Installation and Basic Setup

### 2.1. Install Selenium with pip

```bash
pip install selenium
```

### 2.2. Browser Drivers

Each browser requires a driver:
- **Chrome**: `chromedriver`
- **Firefox**: `geckodriver`
- **Edge**: `msedgedriver`
- **Safari**: Built-in on macOS or use `safaridriver`
- **IE**: `IEDriverServer` (though IE is deprecated)

Selenium can also use the **Selenium Manager**, an internal helper that auto-finds or downloads the matching driver version for your installed browser. Often, you won’t need to specify `executable_path` if you rely on that approach.

### 2.3. Minimal Code Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # or Firefox(), Edge(), Safari(), etc.
driver.get("https://www.example.com")

element = driver.find_element(By.ID, "example-element-id")
print("Element text:", element.text)

driver.quit()
```

---

## 3. Key Browser Classes and Examples

Selenium provides specialized classes in `selenium.webdriver`:

- `webdriver.Chrome`
- `webdriver.Firefox`
- `webdriver.Edge`
- `webdriver.Ie`
- `webdriver.Safari`
- `webdriver.WebKitGTK`
- `webdriver.WPEWebKit`
- `webdriver.Remote` (for remote or Grid usage)

### 3.1. Chrome Usage Example

```python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

chrome_service = Service()  # or specify path: Service("/path/to/chromedriver")
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = Chrome(service=chrome_service, options=chrome_options)
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium 4.25")
search_box.submit()

driver.quit()
```

### 3.2. Firefox Usage Example

```python
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

firefox_service = Service("/path/to/geckodriver")
firefox_options = Options()
firefox_options.headless = True

driver = Firefox(service=firefox_service, options=firefox_options)
driver.get("https://www.mozilla.org")
driver.quit()
```

*(Edge, Safari, IE, WebKitGTK, WPEWebKit follow a similar pattern.)*

### 3.3. Remote WebDriver (e.g., Selenium Grid)

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME.copy()
caps['browserName'] = 'chrome'
caps['platformName'] = 'ANY'

driver = webdriver.Remote(
  command_executor='http://your-grid-url:4444/wd/hub',
  desired_capabilities=caps
)
driver.get("https://selenium.dev")
driver.quit()
```

---

## 4. Fundamental Modules & Classes

### 4.1. `By` Locators

```python
from selenium.webdriver.common.by import By

# Supported: By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR, By.TAG_NAME, ...
driver.find_element(By.ID, "main")
driver.find_elements(By.CSS_SELECTOR, "div.article")
```

### 4.2. `Keys`

```python
from selenium.webdriver.common.keys import Keys

element.send_keys("Selenium" + Keys.ENTER)
element.send_keys(Keys.CONTROL, 'a')  # select all
```

### 4.3. `DesiredCapabilities`

Predefined dicts:
```python
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX.copy()
caps['platform'] = "WINDOWS"
caps['version'] = "latest"
```

### 4.4. `Proxy` and Network Proxy

```python
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_obj = Proxy()
proxy_obj.proxy_type = ProxyType.MANUAL
proxy_obj.http_proxy = "localhost:8080"
proxy_obj.ssl_proxy = "localhost:8080"
```

### 4.5. `Options` Classes

Each browser has its own: `ChromeOptions`, `FirefoxOptions`, etc. In general, you can do:

```python
options = ChromeOptions()
options.add_argument("--headless")
options.page_load_strategy = "eager"
```

### 4.6. `Service`

Each browser typically has a `Service` class that manages the driver binary:
```python
from selenium.webdriver.chrome.service import Service
service = Service("/path/to/chromedriver")
service.start()
driver = Chrome(service=service)
```

### 4.7. `Timeouts` and Waits

- **Implicit Wait**: `driver.implicitly_wait(10)`
- **Explicit Wait**: 
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  wait = WebDriverWait(driver, 10)
  wait.until(EC.presence_of_element_located((By.ID, "someId")))
  ```

### 4.8. `WebElement` interactions

- `element.click()`
- `element.send_keys("text")`
- `element.text`
- `element.get_attribute("value")`
- `element.is_displayed()` / `element.is_enabled()`

### 4.9. `Alert` (JavaScript alerts and prompts)

```python
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("some input")
alert.accept()  # or alert.dismiss()
```

### 4.10. `SwitchTo` for Frames, Windows, or Alerts

- `driver.switch_to.frame("frameName")`
- `driver.switch_to.window("handle")`
- `driver.switch_to.new_window('tab' or 'window')`

---

## 5. Advanced User Actions

### 5.1. ActionChains

Chainable interface:
```python
from selenium.webdriver import ActionChains

actions = ActionChains(driver)
actions.move_to_element(menu).click(submenu).perform()
```
Common methods: `.click()`, `.double_click()`, `.context_click()`, `.drag_and_drop()`, `.send_keys()`, `.perform()`, etc.

### 5.2. Low-Level Actions.* Modules

- **PointerInput / PointerActions** for mouse-like actions: `.pointer_down()`, `.pointer_up()`, `.move_to()`, `.click()`.
- **KeyInput / KeyActions** for direct keyboard press/release.
- **WheelInput / WheelActions** for scrolling.

Usually not needed unless building custom actions beyond what `ActionChains` offers.

---

## 6. BiDi / DevTools / Logging

### 6.1. DevTools Protocol (CDP)

For Chrome-based browsers:
```python
driver.execute_cdp_cmd("Network.emulateNetworkConditions", {
    "offline": False,
    "latency": 100,
    "downloadThroughput": 500 * 1024,
    "uploadThroughput": 500 * 1024
})
```

### 6.2. Bidi Logging / console

```python
logs = driver.get_log("browser")
for entry in logs:
    print(entry)
```
**Alternatively**: `driver.log` can add JS error listener, console message listener, etc.

---

## 7. Virtual Authenticator & WebAuthn

Simulate hardware security tokens for testing passkeys or FIDO flows:

```python
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions, Credential

options = VirtualAuthenticatorOptions(protocol="ctap2", transport="usb", has_resident_key=True)
driver.add_virtual_authenticator(options)

cred = Credential.create_resident_credential(
    id=b'byte_id',
    rp_id='example.com',
    user_handle=b'user_name',
    private_key=b'base64EncodedKey==',
    sign_count=0
)
driver.add_credential(cred)
driver.remove_virtual_authenticator()
```

---

## 8. FedCM Dialog Testing

FedCM (Federated Credential Management) support:
```python
driver.fedcm.title
driver.fedcm.subtitle
driver.fedcm.accept()   # or driver.fedcm.dismiss()
driver.fedcm.select_account(index=0)
```

---

## 9. Print Page (PDF Generation)

For Chromium-based browsers, you can print the page as PDF:

```python
from selenium.webdriver.common.print_page_options import PrintOptions

print_options = PrintOptions()
print_options.page_ranges = ["1-2"]
pdf_base64 = driver.print_page(print_options)
# Now decode or save to file
with open("page.pdf", "wb") as f:
    f.write(base64.b64decode(pdf_base64))
```

---

## 10. Selenium Manager

**Selenium Manager** tries to automatically find or fetch driver executables:

```python
from selenium.webdriver.common.selenium_manager import SeleniumManager

manager = SeleniumManager()
result = manager.binary_paths(["--browser", "chrome"])
print(result)  # e.g. { "driver_path": "...", "browser_path": "..." }
```

---

## 11. Support, Waits, Conditions, and Events

### 11.1. WebDriverWait & ExpectedConditions

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
elem = wait.until(EC.visibility_of_element_located((By.ID, "target")))
```

### 11.2. `RelativeLocator` for “above”, “below”, etc.

```python
from selenium.webdriver.support.relative_locator import locate_with

driver.find_elements(locate_with(By.TAG_NAME, "p").above(footer_element))
```

### 11.3. Event Listeners

```python
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyListener(AbstractEventListener):
    def before_click(self, element, driver):
        print("About to click:", element)

driver = EventFiringWebDriver(driver, MyListener())
driver.find_element(By.ID, "someID").click()
```

---

## 12. Code Snippets and Example Patterns

### 12.1. Cookie Management

```python
driver.add_cookie({"name": "test_cookie", "value": "cookie_value"})
print(driver.get_cookies())
driver.delete_cookie("test_cookie")
driver.delete_all_cookies()
```

### 12.2. Screenshots

```python
driver.save_screenshot("homepage.png")
elem = driver.find_element(By.ID, "logo")
elem.screenshot("logo.png")
```

### 12.3. Basic Drag & Drop

```python
from selenium.webdriver import ActionChains

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(source, target).perform()
```

### 12.4. Window / Tab Management

```python
driver.switch_to.new_window('tab')
print(driver.window_handles)
driver.close()
driver.switch_to.window(driver.window_handles[0])
```

---

## 13. Common Exceptions

- **`NoSuchElementException`**: element not found
- **`ElementNotInteractableException`**: hidden or disabled element
- **`TimeoutException`**: wait times out
- **`WebDriverException`**: base for many unexpected errors
- **`StaleElementReferenceException`**: DOM changed, old element reference invalid

Use `try/except` or `WebDriverWait` to handle gracefully.

---

## 14. Summaries of Many Classes / Methods

**(A consolidated reference)**

- **`selenium.webdriver.common.by.By`**:
  - `By.ID`, `By.NAME`, `By.CSS_SELECTOR`, `By.XPATH`, etc.

- **`selenium.webdriver.common.keys.Keys`**:
  - `Keys.ENTER`, `Keys.TAB`, `Keys.CONTROL`, `Keys.SHIFT`, etc.

- **`selenium.webdriver.common.action_chains.ActionChains`**:
  - `click()`, `double_click()`, `send_keys()`, `drag_and_drop()`, `perform()`, etc.

- **`selenium.webdriver.common.actions.*`** (lower-level):
  - `PointerInput`, `PointerActions`, `KeyInput`, `KeyActions`, `WheelActions`, etc.

- **`selenium.webdriver.common.alert.Alert`**:
  - `accept()`, `dismiss()`, `send_keys()`, `text`.

- **`selenium.webdriver.common.service.Service`**:
  - Base for `ChromeService`, `FirefoxService`, etc. methods: `start()`, `stop()`.

- **`selenium.webdriver.common.options.BaseOptions`**:
  - For setting capabilities, timeouts, platform name, acceptInsecureCerts, pageLoadStrategy, etc.

- **`selenium.webdriver.common.desired_capabilities.DesiredCapabilities`**:
  - `CHROME`, `FIREFOX`, `EDGE`, etc. built-in dictionaries.

- **`selenium.webdriver.common.proxy.Proxy`**:
  - `ssl_proxy`, `http_proxy`, `socks_proxy`, `proxy_type`, etc.

- **`selenium.webdriver.common.virtual_authenticator.VirtualAuthenticatorOptions`** / `Credential`**:
  - For simulating FIDO/webauthn keys.

- **`selenium.webdriver.common.print_page_options.PrintOptions`**:
  - For printing to PDF (`driver.print_page()`).

- **`selenium.webdriver.remote.webdriver.WebDriver`** (the base):
  - `.get(url)`, `.close()`, `.quit()`, `.find_element()`, `.find_elements()`
  - `.execute_script()`, `.switch_to`, `.window_handles`, `.add_cookie()`, etc.

- **`selenium.webdriver.support.wait.WebDriverWait`**:
  - `.until(condition)`, `.until_not(condition)`

- **`selenium.webdriver.support.expected_conditions`**:
  - `EC.presence_of_element_located(...)`, `EC.visibility_of_element_located(...)`, etc.

- **`selenium.webdriver.support.relative_locator`**:
  - `locate_with(By.TAG_NAME, "div").above(some_element)`, etc.

---

## 15. Best Practices & Tips

1. **Use Waits**: Avoid `time.sleep()`, prefer `WebDriverWait` or at least `implicitly_wait`.
2. **Structure Tests**: With Python’s `unittest` or `pytest`, set up driver in `setUp()`, tear down in `tearDown()`.
3. **Manage Locators**: Keep them in well-named constants or use Page Objects.
4. **Headless**: If no GUI needed, pass `--headless`.
5. **Grid**: If tests scale up, consider Selenium Grid or remote services. Provide capabilities carefully.
6. **Exceptions**: Catch `NoSuchElementException` or `TimeoutException` for robust error handling.

---

## 16. Summary

**Selenium 4.25** for Python is a powerful, flexible way to automate any major browser. In this single doc, we’ve merged the **API references** with advanced usage tips. Key steps:

1. **Install** (`pip install selenium`)
2. **Obtain or rely on Selenium Manager** to find browser drivers
3. **Create a driver** (Chrome, Firefox, Edge, Safari, etc.)
4. **Locate elements** using `By` or relative locators
5. **Interact** (click, type, drag, etc.) via direct calls or advanced `ActionChains`
6. **Use waits** to sync with dynamic pages
7. **Explore** advanced features: network conditions, CDP, BiDi logs, console, FedCM, virtual authenticators, etc.
8. **Conclude** with `driver.quit()`.

Below is the **ultimate** comprehensive, merged documentation for **Selenium Python 4.25** (January 2025). It encapsulates **everything** from previous references—APIs, classes, methods, usage examples, advanced features—and organizes it all in a single, thorough resource. Enjoy!

---

# **Selenium for Python 4.25 – The Definitive Documentation**

## **Table of Contents**

1. [Overview and Installation](#overview-install)
2. [Fundamental Classes and Concepts](#fundamental-classes-concepts)
   - [By](#by)
   - [Keys](#keys)
   - [WebDriver (Chrome/Firefox/Edge/Etc.)](#webdriver)
   - [Service](#service)
   - [Options, DesiredCapabilities, Proxy, Timeouts](#options-proxy-timeouts)
   - [WebElement Basics](#webelement)
   - [Alert Handling](#alert)
   - [Switching Contexts (Frames, Windows, Alerts)](#switching-contexts)
   - [Driver Finder](#driver-finder)
   - [Selenium Manager](#selenium-manager)
   - [Common Exceptions](#exceptions)
3. [Working with Specific Browsers](#browser-specifics)
   - [Chrome](#chrome)
   - [Firefox](#firefox)
   - [Edge](#edge)
   - [IE](#ie)
   - [Safari](#safari)
   - [WebKitGTK / WPEWebKit](#webkitgtk)
4. [Advanced Topics](#advanced-topics)
   - [Actions (Mouse, Keyboard, Wheel)](#actions)
     - [ActionChains & ActionBuilder](#actionchains-actionbuilder)
     - [Pointer Actions & MouseButton Enum](#pointer-actions)
     - [KeyInput, KeyActions](#keyinput-keyactions)
     - [WheelInput & WheelActions](#wheelinput)
   - [Mobile Class & Network Emulation](#mobile-network)
   - [Bidi / DevTools / CDP](#bidi-devtools-cdp)
     - [Script, Console, Log, etc.](#script-console-log)
   - [Virtual Authenticator & Credentials](#virtual-authenticator)
   - [Print Page Options / PDF Generation](#print-page)
   - [Selenium Grid / RemoteWebDriver](#grid-remote)
   - [File Upload & FileDetector](#file-upload)
5. [Utility Modules & Functions](#utility-modules)
   - [Utils (Connectivity, Ports, etc.)](#utils)
6. [Support: Waits, Relative Locators, Event Listeners](#support-waits)
   - [WebDriverWait & Expected Conditions](#webdriverwait)
   - [Relative Locators](#relative-locators)
   - [AbstractEventListener & EventFiringWebDriver](#eventfiring)
7. [Common Pitfalls & Best Practices](#pitfalls)
8. [Examples and Snippets](#examples)

---

## 1. Overview and Installation <a name="overview-install"></a>

**Selenium** automates web browsers to test or script user interactions.  
- **Install** via `pip install selenium`.
- **Drivers**: Each browser (Chrome, Firefox, Edge, etc.) needs its own driver (like `chromedriver`, `geckodriver`, etc.).
- **Basic code snippet**:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By

  driver = webdriver.Chrome()
  driver.get("https://www.example.com")
  elem = driver.find_element(By.ID, "myid")
  print(elem.text)
  driver.quit()
  ```

Selenium 4.25 adds new features including advanced **BiDi** (bidirectional) logs, **virtual authenticator** for WebAuthn, **FedCM** testing, and more.

---

## 2. Fundamental Classes and Concepts <a name="fundamental-classes-concepts"></a>

### 2.1. **By** <a name="by"></a>
Specifies location strategies:
- `By.ID`
- `By.CSS_SELECTOR`
- `By.XPATH`
- `By.NAME`
- `By.CLASS_NAME`
- `By.LINK_TEXT`
- `By.PARTIAL_LINK_TEXT`
- `By.TAG_NAME`

**Usage**:
```python
driver.find_element(By.ID, "login")
driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
```

### 2.2. **Keys** <a name="keys"></a>
Represents keyboard special keys:
- `Keys.ENTER`
- `Keys.TAB`
- `Keys.ESCAPE`
- `Keys.CONTROL`
- `Keys.SHIFT`
- etc.

**Usage**:
```python
element.send_keys("Hello World" + Keys.ENTER)
```

### 2.3. **WebDriver** <a name="webdriver"></a>
Central class for controlling the browser. For instance:
- `driver.get("url")`
- `driver.back()`, `driver.forward()`, `driver.refresh()`
- `driver.quit()`
- `driver.execute_script("some JS")`
- `driver.find_element(By.X, "locator")`

Each browser has its own child class: `Chrome`, `Firefox`, `Edge`, etc. Under the hood, they derive from `RemoteWebDriver`.

### 2.4. **Service** <a name="service"></a>
Abstract base for launching/stopping the driver process. Each browser’s driver can be wrapped in a specialized service class:

```python
from selenium.webdriver.chrome.service import Service
chrome_service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=chrome_service)
```

### 2.5. **Options, DesiredCapabilities, Proxy, Timeouts** <a name="options-proxy-timeouts"></a>

- **Options** (e.g., `ChromeOptions`, `FirefoxOptions`) let you set command-line args or preferences.  
- **DesiredCapabilities** store sets of default capabilities like `DesiredCapabilities.CHROME`.  
- **Proxy** sets up a proxy for your test sessions.  
- **Timeouts** manage implicit waits, pageLoad, and script timeouts.

### 2.6. **WebElement** <a name="webelement"></a>
Represents an individual DOM element. Supports:
```python
element.click()
element.send_keys("abc")
element.text
element.get_attribute("href")
```

### 2.7. **Alert** <a name="alert"></a>
Interacts with JavaScript alerts, prompts, or confirms:
```python
alert = driver.switch_to.alert
alert_text = alert.text
alert.send_keys("Some text")
alert.accept()  # or alert.dismiss()
```

### 2.8. **Switching Contexts (Frames, Windows, Alerts)** <a name="switching-contexts"></a>
Use `driver.switch_to`:
```python
driver.switch_to.frame("frameName")
driver.switch_to.default_content()
driver.switch_to.window("windowHandle")
driver.switch_to.alert.accept()
```
**`driver.switch_to.new_window('tab')`** can also open a new tab or window.

### 2.9. **Driver Finder** <a name="driver-finder"></a>
Helps automatically find browser drivers. Typically, you either specify an absolute path or rely on **Selenium Manager**.

### 2.10. **Selenium Manager** <a name="selenium-manager"></a>
Automatically attempts to locate or download the correct driver version for your browser:
```python
from selenium.webdriver.common.selenium_manager import SeleniumManager

mgr = SeleniumManager()
paths = mgr.binary_paths(["--browser", "chrome"])
```
Usually, this is invoked behind the scenes if you don’t provide an `executable_path`.

### 2.11. **Common Exceptions** <a name="exceptions"></a>
- `NoSuchElementException`
- `ElementNotInteractableException`
- `TimeoutException`
- `WebDriverException`
- `StaleElementReferenceException`
- etc.

---

## 3. Working with Specific Browsers <a name="browser-specifics"></a>

### 3.1. **Chrome** <a name="chrome"></a>
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opts = Options()
opts.add_argument("--headless")
service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=opts)
driver.get("https://www.google.com")
driver.quit()
```

### 3.2. **Firefox** <a name="firefox"></a>
```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

ff_opts = Options()
ff_opts.headless = True
service = Service("/path/to/geckodriver")
driver = webdriver.Firefox(service=service, options=ff_opts)
driver.get("https://www.mozilla.org")
driver.quit()
```

### 3.3. **Edge** <a name="edge"></a>
```python
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

edge_opts = Options()
service = Service("/path/to/msedgedriver")
driver = webdriver.Edge(service=service, options=edge_opts)
driver.get("https://www.microsoft.com")
driver.quit()
```

### 3.4. **IE** <a name="ie"></a>
Internet Explorer is largely deprecated. If needed:
```python
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.options import Options

service = Service("/path/to/IEDriverServer.exe")
opts = Options()
driver = webdriver.Ie(service=service, options=opts)
driver.quit()
```

### 3.5. **Safari** <a name="safari"></a>
```python
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options

service = Service()
opts = Options()
driver = webdriver.Safari(service=service, options=opts)
driver.get("https://www.apple.com")
driver.quit()
```

### 3.6. **WebKitGTK / WPEWebKit** <a name="webkitgtk"></a>
Used on certain Linux distros:
```python
from selenium.webdriver.webkitgtk.webdriver import WebDriver as WebKitGTK
from selenium.webdriver.webkitgtk.options import Options as WebKitGTKOptions
from selenium.webdriver.webkitgtk.service import Service as WebKitGTKService

opts = WebKitGTKOptions()
service = WebKitGTKService()
driver = WebKitGTK(service=service, options=opts)
driver.get("https://webkit.org")
driver.quit()
```
Similar for `WPEWebKit`.

---

## 4. Advanced Topics <a name="advanced-topics"></a>

### 4.1. **Actions** <a name="actions"></a>
Perform low-level user interactions:

#### 4.1.1. ActionChains & ActionBuilder <a name="actionchains-actionbuilder"></a>
```python
from selenium.webdriver import ActionChains

actions = ActionChains(driver)
actions.move_to_element(menu_element).click(submenu_element).perform()
```
Common chain methods:
- `click([on_element])`
- `double_click([on_element])`
- `context_click([on_element])`
- `key_down(value, [element])`
- `key_up(value, [element])`
- `drag_and_drop(source, target)`
- `move_by_offset(x, y)`
- `pause(seconds)`
- `perform()`

#### 4.1.2. Pointer Actions & MouseButton Enum <a name="pointer-actions"></a>
You can create pointer-based interactions, specifying button = `MouseButton.LEFT` or `MouseButton.RIGHT`.

#### 4.1.3. KeyInput, KeyActions <a name="keyinput-keyactions"></a>
Lower-level classes if you need granular “press key down” vs “release key.” Typically `ActionChains` suffices.

#### 4.1.4. WheelInput & WheelActions <a name="wheelinput"></a>
Scrolling actions:
```python
actions.wheel_action.scroll(x=0, y=0, delta_x=0, delta_y=-200).perform()
```

### 4.2. **Mobile Class & Network Emulation** <a name="mobile-network"></a>
Chromium-based drivers can emulate network conditions:
```python
driver.set_network_conditions(
  offline=False,
  latency=100,
  download_throughput=500*1024,
  upload_throughput=500*1024
)
```
The `Mobile` class also helps with certain contexts if needed.

### 4.3. **Bidi / DevTools / CDP** <a name="bidi-devtools-cdp"></a>
Selenium 4+ supports hooking into Chrome DevTools or BiDi:

```python
driver.execute_cdp_cmd("Network.clearBrowserCache", {})
# or advanced
driver.log.add_js_error_listener()
```

#### 4.3.1. Script, Console, Log, etc. <a name="script-console-log"></a>
- `driver.log.mutation_events()`
- `driver.log.add_listener(...)`
- `Script` class for adding console error handlers.

### 4.4. **Virtual Authenticator** <a name="virtual-authenticator"></a>
Simulate WebAuthn credentials. Example:
```python
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions, Credential

options = VirtualAuthenticatorOptions()
driver.add_virtual_authenticator(options)

cred = Credential.create_resident_credential(
  id=b'unique_id', rp_id='example.com', user_handle=b'user1',
  private_key=b'...', sign_count=0
)
driver.add_credential(cred)
driver.remove_virtual_authenticator()
```

### 4.5. **Print Page Options / PDF** <a name="print-page"></a>
Chromium-based drivers can generate PDFs:
```python
from selenium.webdriver.common.print_page_options import PrintOptions

opts = PrintOptions()
opts.page_ranges = ["1-2"]
pdf_base64 = driver.print_page(opts)
```
`pdf_base64` is a base64-encoded string of the PDF data.

### 4.6. **Selenium Grid / RemoteWebDriver** <a name="grid-remote"></a>
Connect to a remote server or grid:
```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME.copy()
driver = webdriver.Remote(
    command_executor='http://grid.example.com:4444/wd/hub',
    desired_capabilities=caps
)
driver.get("https://selenium.dev")
driver.quit()
```

### 4.7. **File Upload & FileDetector** <a name="file-upload"></a>
In remote contexts, set a `FileDetector`:
```python
from selenium.webdriver.remote.file_detector import LocalFileDetector

driver.file_detector = LocalFileDetector()
element = driver.find_element(By.ID, "upload")
element.send_keys("/path/to/file")
```

---

## 5. Utility Modules & Functions <a name="utility-modules"></a>

### 5.1. **Utils** <a name="utils"></a>
- `free_port()` picks an available port.
- `is_connectable(port, host="localhost")` checks if a TCP socket is listening.
- `keys_to_typing(value)` processes keystroke lists.

---

## 6. Support: Waits, Relative Locators, Event Listeners <a name="support-waits"></a>

### 6.1. **WebDriverWait & Expected Conditions** <a name="webdriverwait"></a>
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
element.click()
```
Common exceptions to ignore can be passed in `ignored_exceptions`.

### 6.2. **Relative Locators** <a name="relative-locators"></a>
Find elements relative to others:
```python
from selenium.webdriver.support.relative_locator import locate_with

above_el = driver.find_element(By.ID, "someElement")
elements = driver.find_elements(
  locate_with(By.TAG_NAME, "p").above(above_el)
)
```

### 6.3. **AbstractEventListener & EventFiringWebDriver** <a name="eventfiring"></a>
For hooking driver events:
```python
from selenium.webdriver.support.events import (
    EventFiringWebDriver, AbstractEventListener
)

class MyListener(AbstractEventListener):
    def before_click(self, element, driver):
        print("Clicking on:", element)

driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
driver.get("https://example.com")
driver.find_element(By.ID, "btn").click()
```

---

## 7. Common Pitfalls & Best Practices <a name="pitfalls"></a>
1. **Implicit vs. Explicit Wait**: Avoid mixing them too heavily; prefer explicit (`WebDriverWait`).
2. **Using a single driver instance** for multiple tests can cause flakiness. Usually, create a fresh instance per test.
3. **Headless** mode might differ slightly from a normal browser—test carefully.
4. **IE** is no longer recommended; use Edge or another modern browser if possible.
5. **Selenium Grid**: match your local Selenium version with the remote server’s if possible.

---

## 8. Examples and Snippets <a name="examples"></a>

### 8.1. Simple Google Search
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium 4.25" + Keys.ENTER)

time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for r in results[:5]:
    print(r.text)

driver.quit()
```

### 8.2. ActionChains Drag & Drop
```python
from selenium.webdriver import ActionChains

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
```

### 8.3. Using a Virtual Authenticator
```python
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions, Credential

options = VirtualAuthenticatorOptions(protocol="ctap2", transport="usb", has_resident_key=True)
driver.add_virtual_authenticator(options)

credential = Credential.create_resident_credential(
    id=b'test_id', rp_id="my.site", user_handle=b'user123',
    private_key=b'base64Key==', sign_count=0
)
driver.add_credential(credential)
driver.remove_virtual_authenticator()
```

### 8.4. Printing Page to PDF
```python
from selenium.webdriver.common.print_page_options import PrintOptions

driver.get("https://www.example.com/article")
opts = PrintOptions()
opts.orientation = 'landscape'
pdf_base64 = driver.print_page(opts)
with open("article.pdf", "wb") as f:
    f.write(base64.b64decode(pdf_base64))
```

---

**Congratulations!** You have now navigated the **most comprehensive** Selenium 4.25 for Python documentation. It includes:

- Essential classes and usage (WebDriver, By, Keys, Options, Service, etc.).
- Advanced features (BiDi, network emulation, virtual authenticators, printing).
- Best practices and usage patterns for stable, maintainable automation.

**Happy testing and automating with Selenium Python 4.25!**