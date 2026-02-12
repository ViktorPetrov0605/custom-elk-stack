#!/usr/bin/env python3
"""
MCP Browser Interactive Shell
Interactive terminal for controlling Chrome via CDP
"""

import asyncio
import json
import os
import base64
from datetime import datetime
from browser_use import Browser

CDP_URL = "http://localhost:9222"

class MCPBrowserShell:
    def __init__(self):
        self.browser = None
        self.page = None
        
    async def start(self):
        """Start shell and connect to Chrome"""
        print("="*60)
        print("MCP Browser Interactive Shell")
        print("="*60)
        print("Connecting to Chrome...")
        
        self.browser = Browser(
            cdp_url=CDP_URL,
            headless=False
        )
        await self.browser.start()
        
        # Get or create page
        pages = await self.browser.get_pages()
        if pages:
            self.page = pages[0]
        else:
            self.page = await self.browser.new_page()
        
        print(f"Connected to Chrome at {CDP_URL}")
        print(f"Current URL: {await self.page.get_url()}")
        print("="*60)
        print("Commands: navigate, screenshot, fill, click, jsclick")
        print("          url, title, elements, wait, exit")
        print("="*60)
        
        await self.interactive_loop()
    
    async def interactive_loop(self):
        """Main interactive loop"""
        while True:
            try:
                # Get command
                print("\n> ", end="", flush=True)
                cmd_line = await asyncio.get_event_loop().run_in_executor(None, input)
                cmd_line = cmd_line.strip()
                
                if not cmd_line:
                    continue
                
                parts = cmd_line.split(maxsplit=1)
                cmd = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                # Execute command
                if cmd == "exit" or cmd == "quit":
                    print("Exiting...")
                    break
                
                elif cmd == "help":
                    self.show_help()
                
                elif cmd == "navigate" or cmd == "goto":
                    await self.cmd_navigate(args)
                
                elif cmd == "screenshot" or cmd == "ss":
                    await self.cmd_screenshot(args)
                
                elif cmd == "fill":
                    await self.cmd_fill(args)
                
                elif cmd == "click":
                    await self.cmd_click(args)
                
                elif cmd == "jsclick" or cmd == "btn":
                    await self.cmd_js_click(args)
                
                elif cmd in ["url", "get_url"]:
                    url = await self.page.get_url()
                    print(f"Current URL: {url}")
                
                elif cmd in ["title"]:
                    title = await self.page.get_title()
                    print(f"Page title: {title}")
                
                elif cmd == "elements" or cmd == "count":
                    await self.cmd_elements(args)
                
                elif cmd == "wait":
                    seconds = int(args) if args.isdigit() else 2
                    print(f"Waiting {seconds} seconds...")
                    await asyncio.sleep(seconds)
                    print("Done waiting.")
                
                else:
                    print(f"Unknown command: {cmd}")
                    print("Type 'help' for available commands.")
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def show_help(self):
        """Show available commands"""
        help_text = """
        Available Commands:
        
        navigate <url>      Navigate to URL (e.g., navigate http://10.4.4.87:5601)
        screenshot [name]   Take screenshot (auto-named if no arg)
        fill <text>         Fill first input field with text
        click <selector>    Click element by CSS selector
        jsclick <text>      Click button by text content
        url                 Get current URL
        title               Get page title
        elements <selector> Count elements matching selector
        wait <seconds>      Wait for specified seconds
        help                Show this help
        exit                Exit shell
        
        Examples:
        > navigate http://10.4.4.87:5601
        > screenshot login_page
        > fill elastic
        > jsclick Log in
        > wait 5
        """
        print(help_text)
    
    async def cmd_navigate(self, url):
        """Navigate to URL"""
        if not url:
            print("Usage: navigate <url>")
            return
        print(f"Navigating to: {url}")
        await self.page.goto(url)
        await asyncio.sleep(2)
        print(f"Loaded: {await self.page.get_url()}")
        print(f"Title: {await self.page.get_title()}")
    
    async def cmd_screenshot(self, filename):
        """Take screenshot"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        elif not filename.endswith('.png'):
            filename += '.png'
        
        print(f"Taking screenshot...")
        screenshot_b64 = await self.page.screenshot()
        screenshot_bytes = base64.b64decode(screenshot_b64)
        
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, "wb") as f:
            f.write(screenshot_bytes)
        
        print(f"Saved: {filename} ({len(screenshot_bytes)} bytes)")
    
    async def cmd_fill(self, text):
        """Fill first input field"""
        if not text:
            print("Usage: fill <text>")
            return
        
        inputs = await self.page.get_elements_by_css_selector("input[type='text'], input[type='email'], input:not([type])")
        if not inputs:
            print("No text input fields found.")
            return
        
        print(f"Filling input with: {text}")
        await inputs[0].click()
        await inputs[0].fill(text)
        print("Filled successfully.")
    
    async def cmd_click(self, selector):
        """Click element by selector"""
        if not selector:
            print("Usage: click <css_selector>")
            return
        
        elements = await self.page.get_elements_by_css_selector(selector)
        if not elements:
            print(f"No elements found for: {selector}")
            return
        
        print(f"Clicking {len(elements)} element(s)")
        await elements[0].click()
        print("Clicked successfully.")
    
    async def cmd_js_click(self, text):
        """Click button by text"""
        if not text:
            print("Usage: jsclick <button_text>")
            return
        
        print(f"Clicking button with text: {text}")
        result = await self.page.evaluate(f"""() => {{
            const buttons = document.querySelectorAll('button, a');
            for (let btn of buttons) {{
                if (btn.textContent.toLowerCase().includes('{text.lower()}')) {{
                    btn.click();
                    return 'Clicked button: ' + btn.textContent.trim();
                }}
            }}
            return 'No button found with text: {text}';
        }}""")
        print(result)
    
    async def cmd_elements(self, selector):
        """Count elements"""
        selector = selector if selector else "*"
        elements = await self.page.get_elements_by_css_selector(selector)
        print(f"Found {len(elements)} elements for selector: {selector}")
    
    async def stop(self):
        if self.browser:
            await self.browser.stop()

async def main():
    shell = MCPBrowserShell()
    await shell.start()
    await shell.stop()

if __name__ == "__main__":
    asyncio.run(main())
