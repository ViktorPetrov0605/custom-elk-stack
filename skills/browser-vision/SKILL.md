# Browser Vision Skill

Specialized agent for browser automation with vision capabilities.

## Usage

Spawn this agent for visual web analysis tasks:

```bash
sessions_spawn --agentId browser-vision --task "Check Kibana dashboards for errors"
```

## Requirements

- Model: `qwen3-vl:235b-instruct-cloud` (ollama)
- Chrome with remote debugging enabled
- MCP browser tools available

## Capabilities

- Screenshot analysis
- Element interaction via CDP
- Error detection in web UIs
- Form filling and navigation
- Console log inspection
