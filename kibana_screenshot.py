#!/usr/bin/env python3
"""Kibana Dashboard Screenshot Tool using undetected-chromedriver"""
import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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

def setup_driver():
    """Setup undetected Chrome driver"""
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1200')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    # Use Chromium 144 explicitly
    driver = uc.Chrome(
        options=options, 
        browser_executable_path='/usr/bin/chromium',
        version_main=144,
        use_subprocess=True
    )
    return driver

def login(driver):
    """Login to Kibana"""
    print("Navigating to Kibana...")
    driver.get(KIBANA_URL)
    
    # Wait for login page to load
    print("Waiting for login page...")
    wait = WebDriverWait(driver, 30)
    
    # Check if we're on login page or already logged in
    time.sleep(3)
    
    # Look for username field
    try:
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "password")
        
        print("Entering credentials...")
        username_field.clear()
        username_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)
        
        # Click login button
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()
        
        print("Waiting for login to complete...")
        time.sleep(5)
    except Exception as e:
        print(f"Login form not found or already logged in: {e}")

def capture_dashboard(driver, name, dashboard_id):
    """Navigate to dashboard and take screenshot"""
    dashboard_url = f"{KIBANA_URL}/app/dashboards#/view/{dashboard_id}"
    print(f"\nNavigating to '{name}' dashboard...")
    driver.get(dashboard_url)
    
    # Wait for page to load and visualizations to render
    print(f"Waiting for dashboard to load...")
    time.sleep(10)
    
    # Take full page screenshot
    screenshot_path = os.path.join(OUTPUT_DIR, f"{dashboard_id}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    # Check for errors in page source
    page_source = driver.page_source
    errors_found = []
    
    error_patterns = [
        "can't access property 'map', e is undefined",
        "e is undefined",
        "Cannot read property",
        "TypeError",
        "Error:",
        "errorThrown",
    ]
    
    for pattern in error_patterns:
        if pattern in page_source:
            errors_found.append(pattern)
    
    # Also look for visible error messages on the page
    try:
        error_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'error') or contains(text(), 'Error') or contains(@class, 'error')]")
        for elem in error_elements[:5]:  # Limit to first 5
            try:
                text = elem.text.strip()
                if text and len(text) < 200:  # Reasonable length
                    errors_found.append(text)
            except:
                pass
    except:
        pass
    
    return errors_found

def main():
    """Main function"""
    print("=" * 60)
    print("Kibana Dashboard Screenshot Tool")
    print("=" * 60)
    
    driver = setup_driver()
    all_errors = {}
    
    try:
        # Login
        login(driver)
        
        # Capture each dashboard
        for name, dashboard_id in DASHBOARDS:
            errors = capture_dashboard(driver, name, dashboard_id)
            all_errors[name] = errors
            
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()
    
    # Report errors
    print("\n" + "=" * 60)
    print("ERROR REPORT")
    print("=" * 60)
    
    any_errors = False
    for name, errors in all_errors.items():
        if errors:
            any_errors = True
            print(f"\n[name]: {name}")
            for err in set(errors):  # Remove duplicates
                print(f"  - {err}")
        else:
            print(f"\n[name]: No errors detected")
    
    if not any_errors:
        print("\nNo errors detected on any dashboards.")
    
    print("\n" + "=" * 60)
    print("Screenshots saved to:", OUTPUT_DIR)
    print("=" * 60)

if __name__ == "__main__":
    main()
