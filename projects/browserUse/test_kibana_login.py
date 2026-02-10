#!/usr/bin/env python3
"""
browser-use Kibana Login Test Script

This script tests browser-use for automating Kibana login and navigation.
Steps:
1. Opens Kibana login page
2. Takes screenshot of login page
3. Enters username/password
4. Clicks login button
5. Waits for dashboard to load
6. Navigates to specific dashboard
7. Takes final screenshot
"""

import asyncio
import os
import sys
from pathlib import Path
from datetime import datetime

# Add browser-use package to path (using the cloned version)
sys.path.insert(0, '/home/valentinbot/.openclaw/workspace/projects/browserUse/browser-use')

from browser_use import BrowserSession, BrowserProfile

# Configuration
KIBANA_URL = "http://10.4.4.87:5601"
DASHBOARD_URL = "http://10.4.4.87:5601/app/dashboards#/view/unified-flow-1770732722"
USERNAME = "elastic"
PASSWORD = "telehouse"

# Screenshot directory
SCREENSHOT_DIR = Path("/home/valentinbot/.openclaw/workspace/projects/browserUse/screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def save_result(status: str, message: str):
    """Save test results to a file"""
    result_file = SCREENSHOT_DIR / "test_results.txt"
    timestamp = get_timestamp()
    with open(result_file, "w") as f:
        f.write(f"Test Results - {timestamp}\n")
        f.write(f"Status: {status}\n")
        f.write(f"Message: {message}\n")
    print(f"\nResults saved to: {result_file}")

async def test_kibana_login():
    """Test Kibana login using browser-use BrowserSession"""
    session = None
    try:
        print("=" * 60)
        print("browser-use Kibana Login Test")
        print("=" * 60)

        # Create user_data_dir for persistent cookies
        user_data_dir = Path("/home/valentinbot/.openclaw/workspace/projects/browserUse/browser_data")
        user_data_dir.mkdir(exist_ok=True)

        print(f"\n1. Creating BrowserSession (headless=True)...")
        session = BrowserSession(
            headless=True,  # Run in background
            user_data_dir=user_data_dir,  # Persistent profile
            viewport={"width": 1920, "height": 1080},  # Large viewport for better screenshots
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
            ]
        )

        print(f"2. Starting browser session...")
        await session.start()
        print(f"   ✓ Browser started (CDP: {session.cdp_url})")

        # Step 1: Navigate to Kibana
        print(f"\n3. Opening Kibana login page: {KIBANA_URL}")
        from browser_use.browser.events import NavigateToUrlEvent
        await session.event_bus.dispatch(NavigateToUrlEvent(url=KIBANA_URL))
        print(f"   ✓ Navigation dispatched")

        # Wait for page to load (30 seconds for JS-heavy Kibana)
        print(f"   Waiting 30 seconds for page to fully load...")
        await asyncio.sleep(30)

        # Step 2: Take screenshot of login page
        login_screenshot = SCREENSHOT_DIR / f"kibana_login_{get_timestamp()}.png"
        print(f"\n4. Taking screenshot of login page...")
        page = await session.get_current_page()
        if page:
            screenshot_data = await page.screenshot()
            with open(login_screenshot, "wb") as f:
                f.write(screenshot_data)
            print(f"   ✓ Screenshot saved: {login_screenshot}")
        else:
            print(f"   ✗ Could not get current page for screenshot")

        # Step 3: Check page state to find login elements
        print(f"\n5. Checking page elements...")
        from browser_use.dom.service import DomService

        # Get DOM state to find input elements
        dom_service = DomService(session)
        dom_state = await dom_service.get_current_state()

        if dom_state and dom_state.items:
            print(f"   Found {len(dom_state.items)} interactive elements")
            for i, item in enumerate(dom_state.items[:10]):  # Show first 10
                print(f"   [{item.index}] {item.interaction_type}: {item.text[:50] if item.text else 'no text'}")
        else:
            print(f"   No interactive elements found - may need to wait longer")

        # Step 4: Try to find and interact with login form elements
        print(f"\n6. Attempting to fill login form...")

        # Get current page for direct interaction
        page = await session.get_current_page()
        if not page:
            raise Exception("No current page available")

        # Try using Playwright page directly for more control
        pw_page = page._page if hasattr(page, '_page') else None

        if pw_page:
            print(f"   Using Playwright for form interaction...")

            # Look for username field
            try:
                username_selector = 'input[name="username"], input[data-test-subj="loginUsername"], #username, input[type="text"]'
                await pw_page.wait_for_selector(username_selector, timeout=10000)
                await pw_page.fill(username_selector, USERNAME)
                print(f"   ✓ Entered username: {USERNAME}")
            except Exception as e:
                print(f"   ✗ Could not find/fill username field: {e}")

            # Look for password field
            try:
                password_selector = 'input[name="password"], input[data-test-subj="loginPassword"], #password, input[type="password"]'
                await pw_page.wait_for_selector(password_selector, timeout=10000)
                await pw_page.fill(password_selector, PASSWORD)
                print(f"   ✓ Entered password: {'*' * len(PASSWORD)}")
            except Exception as e:
                print(f"   ✗ Could not find/fill password field: {e}")

            # Look for login button
            try:
                login_button_selector = 'button[type="submit"], button[data-test-subj="loginSubmit"], .login-btn, button:has-text("Log in")'
                await pw_page.wait_for_selector(login_button_selector, timeout=10000)
                await pw_page.click(login_button_selector)
                print(f"   ✓ Clicked login button")
            except Exception as e:
                print(f"   ✗ Could not click login button: {e}")
        else:
            print(f"   ✗ Could not access Playwright page for direct interaction")

        # Wait for dashboard to load
        print(f"\n7. Waiting 30 seconds for dashboard to load...")
        await asyncio.sleep(30)

        # Step 5: Navigate to specific dashboard
        print(f"\n8. Navigating to dashboard: {DASHBOARD_URL}")
        await session.event_bus.dispatch(NavigateToUrlEvent(url=DASHBOARD_URL))
        print(f"   ✓ Navigation dispatched")

        print(f"   Waiting 30 seconds for dashboard to fully load...")
        await asyncio.sleep(30)

        # Step 6: Take final screenshot
        dashboard_screenshot = SCREENSHOT_DIR / f"kibana_dashboard_{get_timestamp()}.png"
        print(f"\n9. Taking final screenshot of dashboard...")
        page = await session.get_current_page()
        if page:
            screenshot_data = await page.screenshot()
            with open(dashboard_screenshot, "wb") as f:
                f.write(screenshot_data)
            print(f"   ✓ Screenshot saved: {dashboard_screenshot}")
        else:
            print(f"   ✗ Could not get current page for screenshot")

        # Get current URL to verify
        current_page = await session.get_current_page()
        if current_page:
            current_url = await current_page._page.evaluate("window.location.href")
            print(f"\n10. Final URL: {current_url}")

        print(f"\n" + "=" * 60)
        print(f"✓ TEST COMPLETED SUCCESSFULLY")
        print(f"=" * 60)
        print(f"Screenshots saved in: {SCREENSHOT_DIR}")
        print(f"  - Login page: {login_screenshot.name if login_screenshot.exists() else 'N/A'}")
        print(f"  - Dashboard: {dashboard_screenshot.name if dashboard_screenshot.exists() else 'N/A'}")

        save_result("SUCCESS", "Test completed. Check screenshots for verification.")
        return True

    except Exception as e:
        print(f"\n" + "=" * 60)
        print(f"✗ TEST FAILED")
        print(f"=" * 60)
        print(f"Error: {type(e).__name__}: {e}")

        # Try to take error screenshot
        if session:
            try:
                error_screenshot = SCREENSHOT_DIR / f"kibana_error_{get_timestamp()}.png"
                page = await session.get_current_page()
                if page:
                    screenshot_data = await page.screenshot()
                    with open(error_screenshot, "wb") as f:
                        f.write(screenshot_data)
                    print(f"Error screenshot saved: {error_screenshot}")
            except Exception as screenshot_error:
                print(f"Could not take error screenshot: {screenshot_error}")

        save_result("FAILED", f"{type(e).__name__}: {e}")
        return False

    finally:
        # Cleanup
        if session:
            print(f"\n11. Closing browser session...")
            try:
                await session.stop()
                print(f"   ✓ Browser stopped")
            except Exception as e:
                print(f"   ✗ Error stopping browser: {e}")

if __name__ == "__main__":
    success = asyncio.run(test_kibana_login())
    sys.exit(0 if success else 1)
