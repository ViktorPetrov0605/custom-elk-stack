# Browser-Use.com Feasibility Report
## Persistent Browser Automation for Kibana Use Case

**Research Date:** 2026-02-10  
**Purpose:** Evaluate browser-use for running persistent browser sessions with API/script control, screenshot capabilities, authentication persistence, and multi-step workflows.

---

## 1. What is Browser-Use? (Library, API, Service?)

**Answer: All three - it's a hybrid platform:**

### Open Source Library (Free)
- **GitHub:** https://github.com/browser-use/browser-use
- **Type:** Python package (`pip install browser-use` or `uv add browser-use`)
- **License:** Open source
- **Core:** Python async library wrapping browser automation (Playwright-based)

### Cloud Service (Paid)
- **Browser Use Cloud:** https://cloud.browser-use.com
- **SDK:** `pip install browser-use-sdk`
- **Features:** Managed stealth browsers, CAPTCHA bypass, proxies, session persistence
- **Free tier:** $10 credits for new signups
- **Pricing:** ~53 tasks per dollar with their custom LLM

### CLI Tool
- Command-line interface for persistent browser sessions
- Keeps browser running between commands (~50ms latency)
- Supports Python scripting within the session

---

## 2. How Does It Maintain Persistent Browser Sessions?

### Local Mode (Open Source)
```python
browser = Browser(
    keep_alive=True,                    # Keep browser running after agent completes
    user_data_dir='~/browser_profile',  # Persistent profile directory
    storage_state='cookies.json',       # Save/load cookies & localStorage
)
```

**Session Persistence Options:**
- `keep_alive=True` - Browser stays open after agent.run() completes
- `user_data_dir` - Persistent Chrome profile (cookies, localStorage, login state)
- `storage_state` - JSON file for cookie/localStorage synchronization
- `cdp_url` - Connect to existing browser instance via Chrome DevTools Protocol

### Cloud Mode
```python
browser = Browser(use_cloud=True)  # Uses Browser Use Cloud infrastructure
```

**Cloud Features:**
- Sub-second browser initialization
- Persistent profiles ("Login to any website. Stay authenticated.")
- Session resumption across API calls

### CLI Persistent Sessions
```bash
# Browser stays open between commands using session server
browser-use open https://kibana.example.com  # Starts server + browser
browser-use screenshot kibana.png            # Uses same session
browser-use close                            # Closes when done
```

---

## 3. Can It Run Headless BUT Capture Screenshots?

**YES - Explicitly supported:**

```python
browser = Browser(
    headless=True,                      # No UI, runs in background
    device_scale_factor=2.0,            # High-res screenshots (optional)
)

# Agent with screenshot capability
agent = Agent(
    task="Navigate to dashboard and capture screenshot",
    llm=llm,
    browser=browser,
    use_vision=True,                    # Screenshots available to LLM
)
```

**Screenshot Options:**
- **Agent vision:** `use_vision=True/"auto"` - screenshots for AI processing
- **CLI:** `browser-use screenshot output.png --full` (full page)
- **Video recording:** `record_video_dir='./recordings'`
- **High DPI:** `device_scale_factor=2.0` or `3.0` for crisp screenshots

### CLI Screenshot Commands
```bash
browser-use screenshot page.png              # Viewport screenshot
browser-use screenshot --full page.png       # Full page screenshot
```

**Note:** `headless` parameter auto-detects display availability (None = auto, True = force headless, False = show window)

---

## 4. Does It Support Multi-Tab Workflows with Shared Auth?

**YES - Built-in support:**

```python
async def multi_tab_workflow():
    browser = Browser(
        user_data_dir='~/kibana_profile',  # Shared auth across tabs
        keep_alive=True,
    )
    
    task = """
    1. Go to https://kibana.example.com/login
    2. Login with credentials
    3. Open dashboard in new tab
    4. Open another view in another tab
    5. Switch between tabs and take screenshots of each
    """
    
    agent = Agent(task=task, browser=browser, llm=llm)
    await agent.run()
```

**Multi-Tab Features:**
- Agent can open/manage multiple tabs
- Shared authentication via `user_data_dir` (all tabs share cookies)
- `switch_tab` events supported
- CLI: `browser-use switch <tab_index>`

**CLI Multi-Session (Isolated):**
```bash
browser-use --session kibana1 open https://kibana.example.com
browser-use --session kibana2 open https://kibana.example.com
# Each session has isolated cookies/state
```

---

## 5. System Requirements

### Minimum Requirements (Local Mode)
- **Python:** >= 3.11
- **Package manager:** uv (recommended) or pip
- **Browser:** Chromium/Chrome (auto-installed via `uvx browser-use install`)
- **OS:** Linux, macOS, Windows
- **RAM:** ~2-4GB per browser instance (Chrome-based)
- **Docker:** Supported (with chromium_sandbox disabled)

### Example Setup
```bash
# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project
uv init kibana-automation
cd kibana-automation

# Install browser-use
uv add browser-use
uv sync

# Install Chromium browser
uvx browser-use install

# Optional: Get API key for cloud features
# https://cloud.browser-use.com/new-api-key
```

### Cloud Mode Requirements
- SDK: `pip install browser-use-sdk`
- API key from cloud.browser-use.com
- No local browser needed (runs on their infrastructure)

---

## 6. Is It Suitable for Kibana Automation?

### ✅ Feasibility: **YES - Well Suited**

| Requirement | Browser-Use Support | Notes |
|-------------|-------------------|-------|
| **Persistent background session** | ✅ `keep_alive`, `user_data_dir` | Browser stays open, state preserved |
| **API/Script commands** | ✅ Python SDK + CLI | Both programmatic and command-line control |
| **Screenshots on demand** | ✅ Multiple methods | CLI, Python API, or agent tasks |
| **Auth persistence** | ✅ `storage_state`, `user_data_dir` | Cookies/localStorage saved/restored |
| **Multi-step workflows** | ✅ Agent tasks | Natural language or scripted actions |
| **Headless operation** | ✅ `headless=True` | Background operation works perfectly |
| **Low-latency control** | ✅ CLI session server | ~50ms command latency |

### Kibana-Specific Use Cases

**Example 1: CLI-Based Screenshot Service**
```bash
# Login once (interactive or scripted)
browser-use open https://kibana.example.com
browser-use type "admin"
browser-use keys "Tab"
browser-use type "$PASSWORD"
browser-use keys "Enter"
browser-use screenshot logged_in.png

# Later: Navigate to specific dashboards and screenshot
browser-use open https://kibana.example.com/app/dashboards#/view/sales
browser-use screenshot sales_dashboard.png --full

browser-use open https://kibana.example.com/app/dashboards#/view/ops
browser-use screenshot ops_dashboard.png --full
```

**Example 2: Python API for Workflow Automation**
```python
from browser_use import Agent, Browser, ChatGoogle
import asyncio

async def kibana_workflow():
    browser = Browser(
        user_data_dir='~/kibana_profile',  # Persist auth
        headless=True,                      # Background
        keep_alive=True,
    )
    
    llm = ChatGoogle(model='gemini-flash-lite-latest')
    
    agent = Agent(
        task="""
        1. Navigate to Kibana at https://kibana.example.com
        2. If on login page, enter credentials from environment
        3. Wait for Discover page to load
        4. Navigate to the 'Security Events' dashboard
        5. Take a screenshot of the dashboard
        6. Apply time filter for last 24 hours
        7. Take another screenshot
        8. Export the filtered view as CSV if export button exists
        """,
        llm=llm,
        browser=browser,
        sensitive_data={
            'kibana_username': '${KIBANA_USER}',
            'kibana_password': '${KIBANA_PASS}'
        }
    )
    
    result = await agent.run()
    return result

if __name__ == '__main__':
    asyncio.run(kibana_workflow())
```

---

## Limitations & Concerns

### ❌ Potential Issues

1. **LLM Dependency**
   - Browser-use is AI-agent-based (uses LLMs for decision-making)
   - You can use local LLMs (Ollama) to avoid API costs
   - Direct programmatic control (CLI) doesn't require LLM

2. **Chrome Memory Usage**
   - Chrome can consume 2-4GB+ RAM per instance
   - For production scale, use Cloud service or container limits

3. **CAPTCHA/Enterprise SSO**
   - Local mode may hit CAPTCHAs or bot detection
   - Cloud service has "stealth mode" for bypassing
   - Enterprise SSO (SAML/OIDC) may need manual setup

4. **Selenium vs Playwright**
   - Browser-use uses Playwright under the hood
   - Some edge cases may differ from Selenium behavior

5. **Learning Curve**
   - Natural language tasks = simpler but less deterministic
   - CLI/scripted approach = more predictable for automation

### ⚠️ Recommendations for Kibana

| Approach | Best For | Trade-off |
|----------|----------|-----------|
| **CLI Mode** | Simple screenshot service | Fast, no LLM needed |
| **Python SDK** | Complex workflows | Full control, programmatic |
| **Agent Mode** | Adaptive scraping | LLM-based, more flexible |
| **Cloud Service** | Production scale | Costs, but handles CAPTCHAs |

---

## Alternative: Hybrid Approach

For maximum reliability, combine approaches:

```python
# 1. Use CLI for persistent background session
# 2. Use Python SDK for complex interactions
# 3. Use Agent for adaptive/unknown UI changes
```

---

## Example Implementation: Minimal Screenshot Service

```python
# kibana_screenshot.py
import asyncio
from browser_use import Browser
from playwright.async_api import async_playwright

async def screenshot_dashboard(url: str, output_path: str, cookies_file: str = None):
    """Simple non-agent screenshot of Kibana dashboard."""
    
    browser = Browser(
        headless=True,
        user_data_dir='./kibana_profile',  # Persistent login
        window_size={'width': 1920, 'height': 1080},
    )
    
    # Get underlying playwright browser/page
    context = await browser.get_context()
    page = await context.new_page()
    
    await page.goto(url)
    await page.wait_for_selector('.dashboard-container, [data-test-subj]')  # Wait for Kibana
    await asyncio.sleep(2)  # Let visualizations render
    
    await page.screenshot(path=output_path, full_page=True)
    await browser.close()
    
    return output_path

# Run
asyncio.run(screenshot_dashboard(
    'https://kibana.example.com/app/dashboards',
    'dashboard.png'
))
```

---

## Feasibility Verdict

### ✅ **YES - HIGHLY FEASIBLE**

**Rationale:**
- Persistent sessions: ✅ `keep_alive` + `user_data_dir`
- API control: ✅ Both Python SDK and CLI
- Screenshots: ✅ Multiple methods supported
- Auth persistence: ✅ Profile + storage_state
- Multi-step workflows: ✅ Agent or scripted
- Headless: ✅ Fully supported
- Low latency: ✅ CLI session server (~50ms)

**Suggested Approach for Kibana:**
1. **Start with CLI mode** for quick prototyping and screenshot service
2. **Use `user_data_dir`** to persist authentication across restarts
3. **Use Python SDK** for more complex multi-page workflows
4. **Consider Cloud service** if hitting CAPTCHA/stealth issues at scale

**Installation Command:**
```bash
uv init kibana-bot && cd kibana-bot && uv add browser-use && uvx browser-use install
```

---

## References

- **Website:** https://browser-use.com
- **GitHub:** https://github.com/browser-use/browser-use
- **Documentation:** https://docs.browser-use.com
- **Cloud:** https://cloud.browser-use.com
- **CLI Docs:** https://github.com/browser-use/browser-use/tree/main/browser_use/skill_cli
