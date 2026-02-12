#!/usr/bin/env python3
"""
Kibana Screenshot Tool - DEBUG MODE
Uses headed browser with step-by-step screenshots
"""

import asyncio
import os
import base64
from datetime import datetime
from browser_use import Browser

KIBANA_URL = "http://10.4.4.87:5601"
USERNAME = "elastic"
PASSWORD = "telehouse"

async def save_screenshot(page, name):
    """Helper to save screenshot with timestamp"""
    timestamp = datetime.now().strftime("%H-%M-%S")
    filename = f"debug_{name}_{timestamp}.png"
    
    screenshot_b64 = await page.screenshot()
    screenshot_bytes = base64.b64decode(screenshot_b64)
    
    with open(filename, "wb") as f:
        f.write(screenshot_bytes)
    
    print(f"  Saved: {filename}")
    return filename

async def main():
    print("="*60)
    print("KIBANA LOGIN DEBUG - HEADED MODE")
    print("A Chrome window should appear - watch it carefully!")
    print("="*60)
    
    browser = Browser(headless=False)
    await browser.start()
    
    try:
        # Step 1: Navigate to Kibana
        print("\n[1/6] Opening Kibana login page...")
        page = await browser.new_page(KIBANA_URL)
        print("  Waiting 15 seconds for Kibana to fully load...")
        await asyncio.sleep(15)  # Kibana takes time to load
        await save_screenshot(page, "01_initial_load")
        
        url = await page.get_url()
        print(f"  Current URL: {url}")
        
        # Step 2: Find form fields
        print("\n[2/6] Locating form fields...")
        inputs = await page.get_elements_by_css_selector("input")
        print(f"  Found {len(inputs)} input elements")
        
        if len(inputs) < 2:
            print("  ERROR: Not enough input fields found!")
            return
        
        username_field = inputs[0]
        password_field = inputs[1]
        
        # Step 3: Fill username
        print("\n[3/6] Filling username field...")
        await username_field.click()
        await asyncio.sleep(0.5)
        await username_field.fill(USERNAME)
        print(f"  Entered: {USERNAME}")
        await asyncio.sleep(1)
        await save_screenshot(page, "02_username_filled")
        
        # Step 4: Fill password
        print("\n[4/6] Filling password field...")
        await password_field.click()
        await asyncio.sleep(0.5)
        await password_field.fill(PASSWORD)
        print(f"  Entered: {PASSWORD}")
        await asyncio.sleep(1)
        await save_screenshot(page, "03_password_filled")
        
        # Step 5: Click login button
        print("\n[5/6] Attempting to click login button...")
        
        # Try multiple methods to click
        print("  Method 1: Finding button by CSS...")
        buttons = await page.get_elements_by_css_selector("button[type='submit'], .euiButton--fill")
        
        if buttons:
            print(f"  Found {len(buttons)} button(s)")
            for i, btn in enumerate(buttons):
                try:
                    print(f"    Clicking button {i+1}...")
                    await btn.click()
                    print(f"    Click succeeded on button {i+1}")
                    break
                except Exception as e:
                    print(f"    Button {i+1} click failed: {e}")
        else:
            print("  No buttons found with CSS selectors")
        
        print("  Method 2: JavaScript click...")
        result = await page.evaluate("""() => {
            // Look for login button
            const buttons = document.querySelectorAll('button');
            for (let btn of buttons) {
                const text = btn.textContent.toLowerCase();
                if (text.includes('log') || text.includes('sign')) {
                    btn.click();
                    return 'Clicked button with text: ' + btn.textContent;
                }
            }
            
            // Try form submission
            const form = document.querySelector('form');
            if (form) {
                form.submit();
                return 'Submitted form';
            }
            
            return 'No button or form found';
        }""")
        print(f"  JavaScript result: {result}")
        
        await save_screenshot(page, "04_after_click_attempt")
        
        # Step 6: Wait and check result
        print("\n[6/6] Waiting 30 seconds for navigation...")
        print("  Watch the browser window - does it navigate to the dashboard?")
        
        for i in range(30):
            await asyncio.sleep(1)
            if i % 5 == 0:
                current_url = await page.get_url()
                print(f"  [{i}s] URL: {current_url}")
        
        final_url = await page.get_url()
        print(f"\n  Final URL after 30s: {final_url}")
        
        if "/login" in final_url:
            print("  ⚠️  Still on login page - login may have failed")
        else:
            print("  ✅ Successfully navigated away from login!")
        
        await save_screenshot(page, "05_final_result")
        
        # Try pressing Enter as last resort
        if "/login" in final_url:
            print("\n[EXTRA] Trying Enter key...")
            await page.press("Enter")
            await asyncio.sleep(5)
            await save_screenshot(page, "06_after_enter_key")
            
            final_url2 = await page.get_url()
            print(f"  URL after Enter: {final_url2}")
        
        print("\n" + "="*60)
        print("DEBUG COMPLETE")
        print("Check all the debug_*.png files to see what happened")
        print("="*60)
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        print("\nStopping browser (you can close the Chrome window)...")
        await browser.stop()
        print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
