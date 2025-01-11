# Browser Use - Browser Settings Documentation

## Table of Contents
---
- [Browser Settings](#browser-settings)
  - [Browser Configuration](#browser-configuration)
    - [Core Settings](#core-settings)
    - [Additional Settings](#additional-settings)
    - [Alternative Initialization](#alternative-initialization)
      - [External Browser Provider (wss)](#external-browser-provider-wss)
      - [Local Chrome Instance (binary)](#local-chrome-instance-binary)
  - [Context Configuration](#context-configuration)
    - [Configuration Options](#configuration-options)
      - [Page Load Settings](#page-load-settings)
      - [Display Settings](#display-settings)
      - [Debug and Recording](#debug-and-recording)

## Browser Settings

This section details how to configure browser behavior and context settings using `BrowserConfig` and `BrowserContextConfig`. These settings allow you to customize everything from headless mode to proxy settings and page load behavior.

**Note:** We are currently transitioning to a "1 agent, 1 browser, 1 context" model for improved stability and developer experience.

### Browser Configuration

The `BrowserConfig` class controls the core browser behavior and connection settings.

```python
from browser_use import BrowserConfig

# Basic configuration
config = BrowserConfig(
    headless=False,
    disable_security=True
)
```

#### Core Settings

*   **`headless`** (default: `False`): Runs the browser without a visible UI. Be aware that some websites may detect headless mode.
*   **`disable_security`** (default: `True`): Disables browser security features. This can resolve certain functionality issues (like cross-site iFrames) but should be used cautiously, especially with untrusted websites.

#### Additional Settings

*   **`extra_chromium_args`** (default: `[]`): A list of additional arguments passed to the browser at launch. Refer to the [Chromium command-line switches](https://peter.sh/experiments/chromium-command-line-switches/) for a full list of available arguments.
*   **`proxy`** (default: `None`): Standard Playwright proxy settings for using external proxy services.
*   **`new_context_config`** (default: `BrowserContextConfig()`): Default settings for new browser contexts. See [Context Configuration](#context-configuration) below.

**Recommendation:** For web scraping tasks on sites that restrict automated access, consider using external browser or proxy providers for better reliability.

#### Alternative Initialization

These settings allow you to connect to external browser providers or use a local Chrome instance.

##### External Browser Provider (wss)

Connect to cloud-based browser services for enhanced reliability and proxy capabilities.

```python
config = BrowserConfig(
    wss_url="wss://your-browser-provider.com/ws"
)
```

*   **`wss_url`** (default: `None`): WebSocket URL for connecting to external browser providers (e.g., `anchorbrowser.com`, `steel.dev`, `browserbase.com`, `browserless.io`). This setting overrides local browser settings and uses the provider’s configuration. Refer to the provider's documentation for specific settings.

##### Local Chrome Instance (binary)

Connect to your existing Chrome installation to access saved states and cookies.

```python
config = BrowserConfig(
    chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
```

*   **`chrome_instance_path`** (default: `None`): Path to connect to an existing Chrome installation. This is useful for workflows requiring existing login states or browser preferences. This setting will overwrite other browser settings.

### Context Configuration

The `BrowserContextConfig` class controls settings for individual browser contexts.

```python
from browser_use.config import BrowserContextConfig

config = BrowserContextConfig(
    cookies_file="path/to/cookies.json",
    wait_for_network_idle_page_load_time=3.0,
    browser_window_size={'width': 1280, 'height': 1100}
)
```

#### Configuration Options

##### Page Load Settings

*   **`minimum_wait_page_load_time`** (default: `0.5`): Minimum time to wait before capturing page state for LLM input.
*   **`wait_for_network_idle_page_load_time`** (default: `1.0`): Time to wait for network activity to cease. Increase to 3-5 seconds for slower websites. This tracks essential content loading, not dynamic elements like videos.
*   **`maximum_wait_page_load_time`** (default: `5.0`): Maximum time to wait for page load before proceeding.

##### Display Settings

*   **`browser_window_size`** (default: `{'width': 1280, 'height': 1100}`): Browser window dimensions. The default size is optimized for general use cases and interaction with common UI elements like cookie banners.

##### Debug and Recording

*   **`save_recording_path`** (default: `None`): Directory path for saving video recordings.
*   **`trace_path`** (default: `None`): Directory path for saving trace files. Files are automatically named as `{trace_path}/{context_id}.zip`.