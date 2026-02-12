#!/usr/bin/env python3
"""
Kibana Dashboard Screenshot - Persistent Headed Browser
Navigates to an actual dashboard and captures it
"""

import asyncio
import os
import base64
from datetime import datetime
from browser_use import Browser

KIBANA_URL = "http://10.4.4.87:5601"
USERNAME = "elastic"
PASSWORD = "telehouse"
HEADLESS = False  # Keep headed for persistence

async def capture_dashboard():
    """Login and navigate to a dashboard"""
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_file = f"kibana_actual_dashboard_{timestamp}.png"
    
    print("="*60)
    print("KIBANA DASHBOARD CAPTURE - Persistent Browser")
    print("="*60)
    print(f"Starting browser (headed={HEADLESS})...")
    print("Browser will stay open after script completes!")
    print("Press Ctrl+C when done viewing to close manually.")
    print("="*60)
    
    browser = Browser(headless=HEADLESS)
    await browser.start()
    
    try:
        # Step 1: Navigate to Kibana
        print("\n[1/5] Opening Kibana...")
        page = await browser.new_page(KIBANA_URL)
        await asyncio.sleep(15)  # Wait for Kibana to fully load
        
        # Check current URL
        current_url = await page.get_url()
        print(f"  Current URL: {current_url}")
        
        # Step 2: Login if needed
        if "/login" in current_url:
            print("\n[2/5] Logging in...")
            inputs = await page.get_elements_by_css_selector("input")
            
            if len(inputs) >= 2:
                # Fill credentials
                await inputs[0].fill(USERNAME)
                await inputs[1].fill(PASSWORD)
                print(f"  Entered: {USERNAME} / {PASSWORD}")
                
                # Click login button
                buttons = await page.get_elements_by_css_selector("button")
                if buttons:
                    await buttons[0].click()
                    print("  Clicked login button")
                
                # Wait for navigation
                print("  Waiting 25 seconds for Kibana to load...")
                await asyncio.sleep(25)
        else:
            print("\n[2/5] Already logged in (session persisted)!")
        
        # Step 3: Navigate to dashboards
        print("\n[3/5] Navigating to dashboards...")
        
        # Option 1: Navigate directly to dashboards list
        await page.goto(f"{KIBANA_URL}/app/dashboards")
        print(f"  Navigated to: {KIBANA_URL}/app/dashboards")
        await asyncio.sleep(5)
        
        # Option 2: Or try to open a specific dashboard
        # Try the unified-flow-detailed-v2 dashboard or similar
        unified_dashboard_url = f"{KIBANA_URL}/app/dashboards#/view/unified-flow-detailed-v2"
        print(f"\n[4/5] Trying unified flow dashboard...")
        print(f"  URL: {unified_dashboard_url}")
        
        await page.goto(unified_dashboard_url)
        await asyncio.sleep(15)  # Wait for dashboard to fully load
        
        # Check final URL
        final_url = await page.get_url()
        print(f"  Final URL: {final_url}")
        
        # Step 4: Take screenshot
        print("\n[5/5] Taking dashboard screenshot...")
        screenshot_b64 = await page.screenshot()
        screenshot_bytes = base64.b64decode(screenshot_b64)
        
        with open(screenshot_file, "wb") as f:
            f.write(screenshot_bytes)
        
        full_path = os.path.abspath(screenshot_file)
        print(f"  Screenshot saved: {screenshot_file}")
        print(f"  Full path: {full_path}")
        
        # Keep browser open
        print("\n" + "="*60)
        print("DASHBOARD CAPTURED!")
        print("="*60)
        print(f"File: {screenshot_file}")
        print(f"Browser is still running - you can continue interacting")
        print(f"Press Ctrl+C to stop the script and close browser")
        print("="*60)
        
        # Wait indefinitely (keep browser open)
        print("\nKeeping browser open. Press Ctrl+C to exit...")
        while True:
            await asyncio.sleep(1)
        
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("\nStopping browser...")
        await browser.stop()
        print("Browser stopped!")

if __name__ == "__main__":
    asyncio.run(capture_dashboard())
