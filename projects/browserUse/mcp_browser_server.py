#!/usr/bin/env python3
"""
MCP Browser Server
Connects to Chrome via CDP and accepts JSON commands via stdin
"""

import asyncio
import json
import sys
import os
import base64
from datetime import datetime
from browser_use import Browser

# Configuration
CDP_URL = "http://localhost:9222"
USER_DATA_DIR = "/home/valentinbot/.openclaw/workspace/projects/browserUse/chrome-profile"

class MCPBrowserServer:
    def __init__(self):
        self.browser = None
        self.page = None
        self.connected = False
        
    async def start(self):
        """Start the MCP server and connect to Chrome"""
        print(json.dumps({"status": "connecting", "message": f"Connecting to Chrome at {CDP_URL}"}), flush=True)
        
        try:
            # Connect to existing Chrome instance
            self.browser = Browser(
                cdp_url=CDP_URL,
                headless=False,
                user_data_dir=USER_DATA_DIR
            )
            await self.browser.start()
            
            # Get or create a page
            pages = await self.browser.get_pages()
            if pages:
                self.page = pages[0]
            else:
                self.page = await self.browser.new_page()
            
            self.connected = True
            print(json.dumps({"status": "ready", "message": "Connected to Chrome", "websocket": CDP_URL}), flush=True)
            
            # Process commands
            await self.process_commands()
            
        except Exception as e:
            print(json.dumps({"status": "error", "message": str(e)}), flush=True)
            raise
    
    async def process_commands(self):
        """Read commands from stdin and execute them"""
        while True:
            try:
                # Read line from stdin
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                
                if not line:
                    break
                
                line = line.strip()
                if not line:
                    continue
                
                # Parse command
                try:
                    command = json.loads(line)
                except json.JSONDecodeError:
                    self.send_error("Invalid JSON command")
                    continue
                
                # Execute command
                result = await self.execute_command(command)
                print(json.dumps(result), flush=True)
                
            except Exception as e:
                self.send_error(f"Command processing error: {str(e)}")
    
    async def execute_command(self, command):
        """Execute a browser command"""
        cmd = command.get("command")
        params = command.get("params", {})
        
        try:
            if cmd == "navigate":
                url = params.get("url", "about:blank")
                await self.page.goto(url)
                await asyncio.sleep(params.get("wait", 2))
                return {
                    "status": "success",
                    "command": cmd,
                    "url": await self.page.get_url(),
                    "title": await self.page.get_title()
                }
            
            elif cmd == "screenshot":
                screenshot_b64 = await self.page.screenshot()
                screenshot_bytes = base64.b64decode(screenshot_b64)
                
                # Save to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = params.get("filename", f"screenshot_{timestamp}.png")
                filepath = os.path.join(os.path.dirname(__file__), filename)
                
                with open(filepath, "wb") as f:
                    f.write(screenshot_bytes)
                
                return {
                    "status": "success",
                    "command": cmd,
                    "filename": filename,
                    "filepath": filepath,
                    "size": len(screenshot_bytes)
                }
            
            elif cmd == "fill":
                selector = params.get("selector", "input")
                text = params.get("text", "")
                
                elements = await self.page.get_elements_by_css_selector(selector)
                if elements:
                    await elements[0].click()
                    await elements[0].fill(text)
                    return {
                        "status": "success",
                        "command": cmd,
                        "selector": selector,
                        "text": text,
                        "elements_found": len(elements)
                    }
                else:
                    return {
                        "status": "error",
                        "command": cmd,
                        "message": f"No elements found for selector: {selector}"
                    }
            
            elif cmd == "click":
                selector = params.get("selector", "button")
                
                elements = await self.page.get_elements_by_css_selector(selector)
                if elements:
                    await elements[0].click()
                    return {
                        "status": "success",
                        "command": cmd,
                        "selector": selector,
                        "elements_found": len(elements)
                    }
                else:
                    return {
                        "status": "error",
                        "command": cmd,
                        "message": f"No elements found for selector: {selector}"
                    }
            
            elif cmd == "get_url":
                return {
                    "status": "success",
                    "command": cmd,
                    "url": await self.page.get_url()
                }
            
            elif cmd == "get_title":
                return {
                    "status": "success",
                    "command": cmd,
                    "title": await self.page.get_title()
                }
            
            elif cmd == "get_elements":
                selector = params.get("selector", "*")
                elements = await self.page.get_elements_by_css_selector(selector)
                return {
                    "status": "success",
                    "command": cmd,
                    "selector": selector,
                    "count": len(elements)
                }
            
            elif cmd == "wait":
                seconds = params.get("seconds", 1)
                await asyncio.sleep(seconds)
                return {
                    "status": "success",
                    "command": cmd,
                    "waited": seconds
                }
            
            elif cmd == "js_click":
                # JavaScript click
                text = params.get("text", "Log in")
                result = await self.page.evaluate(f"""() => {{
                    const buttons = document.querySelectorAll('button');
                    for (let btn of buttons) {{
                        if (btn.textContent.toLowerCase().includes('{text.lower()}')) {{
                            btn.click();
                            return 'Clicked: ' + btn.textContent;
                        }}
                    }}
                    return 'Button not found';
                }}""")
                return {
                    "status": "success",
                    "command": cmd,
                    "result": result
                }
            
            elif cmd == "help":
                return {
                    "status": "success",
                    "command": cmd,
                    "help": {
                        "navigate": {"params": ["url", "wait"], "description": "Navigate to URL"},
                        "screenshot": {"params": ["filename"], "description": "Take screenshot"},
                        "fill": {"params": ["selector", "text"], "description": "Fill input field"},
                        "click": {"params": ["selector"], "description": "Click element"},
                        "js_click": {"params": ["text"], "description": "Click button by text via JS"},
                        "get_url": {"params": [], "description": "Get current URL"},
                        "get_title": {"params": [], "description": "Get page title"},
                        "get_elements": {"params": ["selector"], "description": "Count elements"},
                        "wait": {"params": ["seconds"], "description": "Wait for seconds"},
                        "help": {"params": [], "description": "Show this help"}
                    }
                }
            
            else:
                return {
                    "status": "error",
                    "command": cmd,
                    "message": f"Unknown command: {cmd}. Type help for available commands."
                }
        
        except Exception as e:
            return {
                "status": "error",
                "command": cmd,
                "message": str(e)
            }
    
    def send_error(self, message):
        """Send error response"""
        print(json.dumps({"status": "error", "message": message}), flush=True)
    
    async def stop(self):
        """Stop the server"""
        if self.browser:
            await self.browser.stop()

async def main():
    server = MCPBrowserServer()
    try:
        await server.start()
    except KeyboardInterrupt:
        print(json.dumps({"status": "stopped", "message": "Server stopped by user"}), flush=True)
    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())
