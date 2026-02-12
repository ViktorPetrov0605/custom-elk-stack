#!/usr/bin/env python3
"""Quick dashboard capture - no persistence"""
import asyncio
import os
import base64
from datetime import datetime
from browser_use import Browser

async def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_file = f"kibana_dashboard_capture_{timestamp}.png"
    
    print("Starting browser for dashboard capture...")
    browser = Browser(headless=False)
    await browser.start()
    
    try:
        page = await browser.new_page("http://10.4.4.87:5601")
        await asyncio.sleep(15)
        
        # Login
        inputs = await page.get_elements_by_css_selector("input")
        if len(inputs) >= 2:
            await inputs[0].fill("elastic")
            await inputs[1].fill("telehouse")
            buttons = await page.get_elements_by_css_selector("button")
            if buttons:
                await buttons[0].click()
            await asyncio.sleep(25)
        
        # Navigate to Dashboards
        print("Navigating to Dashboards list...")
        await page.goto("http://10.4.4.87:5601/app/dashboards")
        await asyncio.sleep(10)
        
        # Take screenshot of whatever we see
        print("Taking screenshot...")
        screenshot_b64 = await page.screenshot()
        screenshot_bytes = base64.b64decode(screenshot_b64)
        
        with open(screenshot_file, "wb") as f:
            f.write(screenshot_bytes)
        
        print(f"Saved: {screenshot_file} ({len(screenshot_bytes)} bytes)")
        print(f"Full path: {os.path.abspath(screenshot_file)}")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        await browser.stop()
        print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
