#!/usr/bin/env python3
"""
Kibana Dashboard Screenshot Tool
Takes screenshots of all 3 unified flow dashboards
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Output directory
output_dir = '/home/valentinbot/.openclaw/workspace/kibana-screenshots'
os.makedirs(output_dir, exist_ok=True)

# Kibana config
kibana_url = 'http://10.4.4.87:5601'
username = 'elastic'
password = 'telehouse'

dashboards = [
    ('unified-flow-detailed-dashboard', '01-detailed-traffic'),
    ('unified-flow-top-n', '02-top-n-analysis'),
    ('unified-flow-conversations', '03-conversation-partners')
]

print("Starting Chrome...")
options = uc.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,2000')  # Tall window for full dashboard

driver = uc.Chrome(options=options, version_main=144)

try:
    # Navigate to Kibana
    print(f"Navigating to {kibana_url}...")
    driver.get(f"{kibana_url}/login")
    time.sleep(3)
    
    # Check if already logged in
    if "login" in driver.current_url.lower():
        print("Logging in...")
        # Fill login form
        try:
            username_field = driver.find_element(By.NAME, 'username')
            password_field = driver.find_element(By.NAME, 'password')
            
            username_field.send_keys(username)
            password_field.send_keys(password)
            
            # Click login button
            login_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            login_btn.click()
            
            # Wait for login
            time.sleep(5)
            print(f"After login: {driver.current_url}")
        except Exception as e:
            print(f"Login form error (might be logged in): {e}")
    else:
        print("Already logged in or no login page")
    
    # Take screenshots of each dashboard
    for dashboard_id, filename in dashboards:
        try:
            print(f"\n--- Screenshotting {filename} ---")
            url = f"{kibana_url}/app/dashboards#/view/{dashboard_id}"
            driver.get(url)
            
            # Wait for dashboard to load
            time.sleep(8)  # Dashboard needs time to load visualizations
            
            # Scroll to capture full dashboard
            print("Scrolling to capture full dashboard...")
            last_height = driver.execute_script("return document.body.scrollHeight")
            scroll_pause = 2
            
            # First scroll to load all content
            for _ in range(5):
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(scroll_pause)
            
            # Scroll back to top
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            
            # Take screenshot
            screenshot_path = f"{output_dir}/{filename}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Saved: {screenshot_path}")
            
            # Check for errors in page source
            page_source = driver.page_source
            if "can't access property" in page_source or "e is undefined" in page_source:
                print(f"⚠️  ERROR FOUND in {filename}: JavaScript error detected!")
            if 'map", e is undefined' in page_source or "e is undefined" in page_source:
                print(f"⚠️  ERROR FOUND in {filename}: 'e is undefined' error!")
                
        except Exception as e:
            print(f"Error screenshotting {filename}: {e}")
            # Take error screenshot anyway
            driver.save_screenshot(f"{output_dir}/{filename}-error.png")
    
    print("\n✅ All screenshots completed!")
    print(f"Screenshots saved to: {output_dir}")
    
    # List files
    files = os.listdir(output_dir)
    for f in files:
        filepath = os.path.join(output_dir, f)
        size = os.path.getsize(filepath)
        print(f"  - {f} ({size} bytes)")

finally:
    driver.quit()
    print("\nBrowser closed.")
