#!/usr/bin/env python3
"""
Kibana Screenshot Tool using browser-use
Captures screenshot of Kibana dashboard after login
"""

import asyncio
import os
import base64
from datetime import datetime
from browser_use import Browser

# Kibana connection details
KIBANA_URL = "http://10.4.4.87:5601"
USERNAME = "elastic"
PASSWORD = "telehouse"
HEADLESS = True  # Set to False for headed mode

async def take_screenshot():
    """Navigate to Kibana, login, and take screenshot"""
    
    # Create screenshot filename with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_file = f"kibana_dashboard_{timestamp}.png"
    
    print(f"Starting browser (headless={HEADLESS})...")
    
    # Initialize browser with larger viewport
    browser = Browser(headless=HEADLESS)
    await browser.start()
    
    try:
        print(f"Navigating to {KIBANA_URL}...")
        page = await browser.new_page(KIBANA_URL)
        
        # Wait for page to fully load
        print("Waiting for page to load (5 seconds)...")
        await asyncio.sleep(5)
        
        # Get page info
        current_url = await page.get_url()
        current_title = await page.get_title()
        print(f"Current URL: {current_url}")
        print(f"Current Title: {current_title}")
        
        # Check if we're on login page
        if "/login" in current_url:
            print("Login page detected - authenticating...")
            
            # Get all input elements
            inputs = await page.get_elements_by_css_selector("input")
            
            if len(inputs) >= 2:
                # First input is username, second is password
                username_field = inputs[0]
                password_field = inputs[1]
                
                # Fill username
                print(f"Filling username: {USERNAME}")
                await username_field.click()
                await asyncio.sleep(0.5)
                await username_field.fill(USERNAME)
                
                # Fill password
                print("Filling password...")
                await password_field.click()
                await asyncio.sleep(0.5)
                await password_field.fill(PASSWORD)
                
                # Find and click login button
                buttons = await page.get_elements_by_css_selector("button")
                for btn in buttons:
                    try:
                        await btn.click()
                        print("Clicked login button")
                        break
                    except:
                        continue
                
                # Wait for dashboard to load
                print("Waiting for Kibana dashboard to load (25 seconds)...")
                await asyncio.sleep(25)
                
                # Check final URL
                final_url = await page.get_url()
                print(f"Final URL after login: {final_url}")
            else:
                print(f"Warning: Only found {len(inputs)} input fields")
        
        # Take screenshot
        print("Taking screenshot...")
        screenshot_b64 = await page.screenshot()
        screenshot_bytes = base64.b64decode(screenshot_b64)
        
        # Save screenshot
        with open(screenshot_file, "wb") as f:
            f.write(screenshot_bytes)
        
        print(f"Screenshot saved to: {screenshot_file}")
        print(f"Full path: {os.path.abspath(screenshot_file)}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("Stopping browser...")
        await browser.stop()
        print("Done!")

if __name__ == "__main__":
    asyncio.run(take_screenshot())
