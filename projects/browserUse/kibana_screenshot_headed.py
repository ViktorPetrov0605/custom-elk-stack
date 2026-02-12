#!/usr/bin/env python3
"""
Kibana Screenshot Tool - HEADED MODE
Captures screenshot of Kibana dashboard after login (visible browser)
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
HEADLESS = False  # HEADED MODE - visible browser

async def take_screenshot():
    """Navigate to Kibana, login, and take screenshot"""
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_file = f"kibana_dashboard_headed_{timestamp}.png"
    
    print(f"Starting browser in HEADED mode (visible window)...")
    print(f"You should see a Chrome window open...")
    
    browser = Browser(headless=HEADLESS)
    await browser.start()
    
    try:
        print(f"Navigating to {KIBANA_URL}...")
        page = await browser.new_page(KIBANA_URL)
        
        print("Waiting 5 seconds for page load...")
        await asyncio.sleep(5)
        
        current_url = await page.get_url()
        print(f"Current URL: {current_url}")
        
        if "/login" in current_url:
            print("Login page detected - filling credentials...")
            
            # Get all inputs
            inputs = await page.get_elements_by_css_selector("input")
            print(f"Found {len(inputs)} input fields")
            
            if len(inputs) >= 2:
                # Fill username
                print("Clicking username field...")
                await inputs[0].click()
                await asyncio.sleep(0.5)
                print(f"Typing username: {USERNAME}")
                await inputs[0].fill(USERNAME)
                await asyncio.sleep(0.5)
                
                # Fill password
                print("Clicking password field...")
                await inputs[1].click()
                await asyncio.sleep(0.5)
                print(f"Typing password...")
                await inputs[1].fill(PASSWORD)
                await asyncio.sleep(1)
                
                # Click login button using JavaScript
                print("Clicking login button via JavaScript...")
                await page.evaluate("""() => {
                    const buttons = document.querySelectorAll('button');
                    for (let btn of buttons) {
                        if (btn.textContent.toLowerCase().includes('log')) {
                            btn.click();
                            return 'Login button clicked';
                        }
                    }
                    return 'No login button found';
                }""")
                
                # Wait for navigation
                print("Waiting 25 seconds for dashboard to load...")
                await asyncio.sleep(25)
                
                final_url = await page.get_url()
                print(f"Final URL: {final_url}")
        
        # Take screenshot
        print("Taking screenshot...")
        screenshot_b64 = await page.screenshot()
        screenshot_bytes = base64.b64decode(screenshot_b64)
        
        with open(screenshot_file, "wb") as f:
            f.write(screenshot_bytes)
        
        print(f"Screenshot saved: {screenshot_file}")
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
