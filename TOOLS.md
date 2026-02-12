# TOOLS.md - Local Notes

## Browser Automation (Chrome CDP)

**Location:** `/home/valentinbot/.openclaw/workspace/projects/browserUse/`

### Tools Available

1. **mcp_browser_server.py** - JSON-based MCP server for programmatic control
2. **mcp_browser_shell.py** - Interactive terminal shell for manual exploration

### How to Use

**Step 1: Start Chrome with remote debugging**
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/home/valentinbot/.openclaw/workspace/projects/browserUse/chrome-profile
```

**Step 2: Run the interactive shell**
```bash
cd /home/valentinbot/.openclaw/workspace/projects/browserUse
python3 mcp_browser_shell.py
```

**Commands available:**
- `navigate <url>` - Open a webpage
- `screenshot <name>` - Capture screenshot
- `click <element>` - Click an element
- `fill <ref> <text>` - Fill a form field
- `jsclick <text>` - Click by text content
- `get_url` - Show current URL
- `get_title` - Show page title
- `wait <seconds>` - Wait
- `help` - Show all commands

### Use Cases
- Kibana dashboard screenshots
- Form automation
- Data extraction
- Visual regression testing

## SSH Infrastructure

- **Backend N1 (NetFlow):** `telehouse@10.4.4.21:2332` / `T3l3h0us#`
- **Backend N2 (sFlow):** `telehouse@10.4.4.90:22` / `T3l3h0us#`
- **Cisco Nexus 1:** `admin@10.4.4.3` / `t3l3h0us3`
- **Cisco Nexus 2:** `admin@10.4.4.4` / `t3l3h0us3`

## Elasticsearch

- **Frontend:** `https://10.4.4.87:5601` (Kibana) / `9200` (ES)
- **User:** `elastic`
- **Password:** `telehouse`

## Notes

- This file persists across sessions
- Add new tools/infrastructure details here
