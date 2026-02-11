#!/usr/bin/env python3
"""Kibana Dashboard Screenshot Tool using Playwright"""
import sys
import os

KIBANA_URL = "http://10.4.4.87:5601"
USERNAME = "elastic"
PASSWORD = "telehouse"
OUTPUT_DIR = "/home/valentinbot/.openclaw/workspace/kibana-screenshots"

DASHBOARDS = [
    ("Detailed Traffic Analysis", "unified-flow-detailed-dashboard"),
    ("Top-N Analysis", "unified-flow-top-n"),
    ("Conversation Partners", "unified-flow-conversations"),
]

async def main():
    from playwright.async_api import async_playwright
    
    print("=" * 60)
    print("Kibana Dashboard Screenshot Tool (Playwright)")
    print("=" * 60)
    
    all_errors = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = await browser.new_context(viewport={'width': 1920, 'height': 1200})
        page = await context.new_page()
        
        try:
            # Login
            print("Navigating to Kibana...")
            await page.goto(KIBANA_URL, wait_until='networkidle')
            
            # Check for login form
            print("Checking for login page...")
            await page.wait_for_timeout(3000)
            
            username_field = await page.query_selector('input[name="username"]')
            if username_field:
                print("Entering credentials...")
                await page.fill('input[name="username"]', USERNAME)
                await page.fill('input[name="password"]', PASSWORD)
                await page.click('button[type="submit"]')
                print("Waiting for login...")
                await page.wait_for_timeout(5000)
            
            # Capture each dashboard
            for name, dashboard_id in DASHBOARDS:
                dashboard_url = f"{KIBANA_URL}/app/dashboards#/view/{dashboard_id}"
                print(f"\nNavigating to '{name}' dashboard...")
                
                await page.goto(dashboard_url, wait_until='networkidle')
                print(f"Waiting for dashboard to render...")
                await page.wait_for_timeout(10000)
                
                # Take screenshot
                screenshot_path = os.path.join(OUTPUT_DIR, f"{dashboard_id}.png")
                await page.screenshot(path=screenshot_path, full_page=True)
                print(f"Screenshot saved: {screenshot_path}")
                
                # Check for errors
                page_content = await page.content()
                errors_found = []
                
                error_patterns = [
                    "can't access property 'map', e is undefined",
                    "e is undefined",
                    "Cannot read property",
                    "TypeError",
                    "errorThrown",
                ]
                
                for pattern in error_patterns:
                    if pattern in page_content:
                        errors_found.append(pattern)
                
                all_errors[name] = errors_found
                
        finally:
            await browser.close()
    
    # Report errors
    print("\n" + "=" * 60)
    print("ERROR REPORT")
    print("=" * 60)
    
    any_errors = False
    for name, errors in all_errors.items():
        if errors:
            any_errors = True
            print(f"\n{name}:")
            for err in set(errors):
                print(f"  - {err}")
        else:
            print(f"\n{name}: No errors detected")
    
    if not any_errors:
        print("\nNo errors detected on any dashboards.")
    
    print("\n" + "=" * 60)
    print("Screenshots saved to:", OUTPUT_DIR)
    print("=" * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
