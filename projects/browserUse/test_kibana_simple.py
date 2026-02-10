#!/usr/bin/env python3
"""Simple Playwright test for Kibana"""

import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

# Paths
SCREENSHOTS_DIR = Path("/home/valentinbot/.openclaw/workspace/projects/browserUse/screenshots")
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Config
KIBANA_URL = "http://10.4.4.87:5601"
DASHBOARD_URL = "http://10.4.4.87:5601/app/dashboards#/view/unified-flow-1770732722"
USERNAME = "elastic"
PASSWORD = "telehouse"

async def test_kibana():
    print("=" * 60)
    print("Kibana Browser Test (Playwright)")
    print("=" * 60)
    
    async with async_playwright() as p:
        print("\n1. Launching browser...")
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
        )
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        print("   ✓ Browser launched")
        
        # Step 1: Navigate to Kibana login
        print(f"\n2. Opening Kibana: {KIBANA_URL}")
        await page.goto(KIBANA_URL, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(10)  # Wait for JS
        
        # Screenshot login page
        login_path = SCREENSHOTS_DIR / "01_login.png"
        await page.screenshot(path=str(login_path), full_page=True)
        print(f"   ✓ Screenshot saved: {login_path}")
        
        # Step 2: Try to login
        print(f"\n3. Attempting to login...")
        try:
            # Try various selectors for username
            username_selectors = [
                'input[name="username"]',
                'input[data-test-subj="loginUsername"]',
                'input[placeholder*="username" i]',
                'input[type="text"]'
            ]
            
            for sel in username_selectors:
                try:
                    await page.fill(sel, USERNAME, timeout=5000)
                    print(f"   ✓ Entered username using: {sel}")
                    break
                except:
                    continue
            
            # Try various selectors for password
            password_selectors = [
                'input[name="password"]',
                'input[data-test-subj="loginPassword"]',
                'input[placeholder*="password" i]',
                'input[type="password"]'
            ]
            
            for sel in password_selectors:
                try:
                    await page.fill(sel, PASSWORD, timeout=5000)
                    print(f"   ✓ Entered password using: {sel}")
                    break
                except:
                    continue
            
            # Try to click login button
            btn_selectors = [
                'button[type="submit"]',
                'button[data-test-subj="loginSubmit"]',
                'button:has-text("Log in")',
                'button:has-text("Login")'
            ]
            
            for sel in btn_selectors:
                try:
                    await page.click(sel, timeout=5000)
                    print(f"   ✓ Clicked login button using: {sel}")
                    break
                except:
                    continue
            
            print("   Waiting 20s for login...")
            await asyncio.sleep(20)
            
        except Exception as e:
            print(f"   ⚠ Login form interaction failed: {e}")
        
        # Screenshot post-login
        post_login_path = SCREENSHOTS_DIR / "02_post_login.png"
        await page.screenshot(path=str(post_login_path), full_page=True)
        print(f"   ✓ Screenshot saved: {post_login_path}")
        
        # Step 3: Navigate to dashboard
        print(f"\n4. Navigating to dashboard...")
        await page.goto(DASHBOARD_URL, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(15)
        
        dashboard_path = SCREENSHOTS_DIR / "03_dashboard.png"
        await page.screenshot(path=str(dashboard_path), full_page=True)
        print(f"   ✓ Screenshot saved: {dashboard_path}")
        
        await browser.close()
        
        print("\n" + "=" * 60)
        print("✓ TEST COMPLETE")
        print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_kibana())
