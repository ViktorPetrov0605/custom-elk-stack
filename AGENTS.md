
## Research Workflow (Tool Priority)

When conducting web research, follow this tool priority:

### 1. SearXNG (DEFAULT - USE FIRST)
- **Script:** `node ~/.openclaw/scripts/searxng_local.js "query"`
- **Why:** Fast, private, no API keys, 30+ engines
- **Returns:** Structured JSON with title, URL, snippet, source engine
- **Best for:** Initial discovery, finding relevant pages

### 2. web_fetch (SECONDARY)
- **Use:** After SearXNG finds relevant URLs
- **Why:** Fast static content extraction (HTML → markdown)
- **Best for:** Reading documentation, articles, blog posts

### 3. Browser (undetected-chromedriver) - LAST RESORT
- **Use:** JavaScript-heavy pages that web_fetch can't handle
- **Why:** Full browser engine, executes JS, can interact
- **Modes:** Headless (default) or Non-headless (requires display)
- **Best for:** SPAs, dynamic content, screenshots, form interaction

### Workflow Example
```
1. Search: searxng_local.js "ElastiFlow pricing"
2. Analyze results, pick relevant URLs
3. Fetch content: web_fetch https://elastiflow.com/pricing
4. If page uses heavy JS: browser screenshot/navigate
```

### Bias: Local > Remote
- Prefer SearXNG (local) over web_search (remote API)
- Prefer web_fetch (text extraction) over browser (full render)
- Only use browser when necessary
