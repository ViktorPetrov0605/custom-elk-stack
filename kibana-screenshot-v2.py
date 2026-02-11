#!/usr/bin/env python3
"""
Kibana Dashboard Screenshot Tool v2 - Improved login handling
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import os

output_dir = '/home/valentinbot/.openclaw/workspace/kibana-screenshots-v2'
os.makedirs(output_dir, exist_ok=True)

kibana_url = 'http://10.4.4.87:5601'

print("🚀 Starting Chrome...")
options = uc.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,4000')  # Very tall for full dashboard

# Create profile directory for persistence
profile_dir = '/tmp/kibana-profile'
os.makedirs(profile_dir, exist_ok=True)
options.add_argument(f'--user-data-dir={profile_dir}')

driver = uc.Chrome(options=options, version_main=144)

try:
    # Step 1: Navigate to login page
    print("🌐 Navigating to Kibana...")
    driver.get(f"{kibana_url}/login")
    time.sleep(5)
    print(f"Current URL: {driver.current_url}")
    
    # Save login page screenshot
    driver.save_screenshot(f"{output_dir}/00-login-page.png")
    print("💾 Saved login page screenshot")
    
    # Step 2: Dismiss any welcome/tutorial popup
    try:
        # Try various selectors for "Skip" or "Dismiss" buttons
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        for btn in buttons:
            text = btn.text.lower()
            if 'skip' in text or 'dismiss' in text or 'got it' in text:
                print(f"Clicking button: {btn.text}")
                btn.click()
                time.sleep(2)
    except Exception as e:
        print(f"No popup to dismiss: {e}")
    
    # Step 3: Find and fill login form
    print("🔑 Attempting login...")
    try:
        # Try multiple selectors for username field
        username_field = None
        for selector in [
            ('name', 'username'),
            ('id', 'username'),
            ('css selector', 'input[data-test-subj="loginUsername"]'),
            ('css selector', 'input[type="text"]'),
            ('xpath', '//input[@type="text"]')
        ]:
            try:
                if selector[0] == 'name':
                    username_field = driver.find_element(By.NAME, selector[1])
                elif selector[0] == 'id':
                    username_field = driver.find_element(By.ID, selector[1])
                elif selector[0] == 'css selector':
                    username_field = driver.find_element(By.CSS_SELECTOR, selector[1])
                elif selector[0] == 'xpath':
                    username_field = driver.find_element(By.XPATH, selector[1])
                if username_field:
                    print(f"✅ Found username field with {selector[0]}={selector[1]}")
                    break
            except:
                continue
        
        if not username_field:
            print("❌ Could not find username field")
            driver.save_screenshot(f"{output_dir}/error-no-username-field.png")
            sys.exit(1)
        
        # Find password field
        password_field = None
        for selector in [
            ('name', 'password'),
            ('id', 'password'),
            ('css selector', 'input[data-test-subj="loginPassword"]'),
            ('css selector', 'input[type="password"]')
        ]:
            try:
                if selector[0] == 'name':
                    password_field = driver.find_element(By.NAME, selector[1])
                elif selector[0] == 'id':
                    password_field = driver.find_element(By.ID, selector[1])
                elif selector[0] == 'css selector':
                    password_field = driver.find_element(By.CSS_SELECTOR, selector[1])
                if password_field:
                    print(f"✅ Found password field with {selector[0]}={selector[1]}")
                    break
            except:
                continue
        
        if not password_field:
            print("❌ Could not find password field")
            driver.save_screenshot(f"{output_dir}/error-no-password-field.png")
            sys.exit(1)
        
        # Enter credentials
        username_field.send_keys('elastic')
        password_field.send_keys('telehouse')  
        
        # Submit form
        login_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_btn.click()
        print("⏳ Waiting for login...")
        time.sleep(8)  # Wait longer for login
        
        print(f"📝 After login URL: {driver.current_url}")
        
    except Exception as e:
        print(f"⚠️ Login error: {e}")
        driver.save_screenshot(f"{output_dir}/error-login.png")
        # Continue anyway - might already be logged in via cookie
    
    # Step 4: Check if we're actually logged in
    if 'login' in driver.current_url.lower():
        print("❌ Still on login page - trying with URL-encoded credentials...")
        # Alternative: Try basic auth URL
        driver.get(f"http://elastic:telehouse@10.4.4.87:5601/app/home")
        time.sleep(8)
        print(f"📝 After basic auth URL: {driver.current_url}")
    
    # Step 5: Navigate to each dashboard
    dashboards = [
        ('/app/dashboards#/view/unified-flow-detailed-dashboard', '01-detailed-traffic'),
        ('/app/dashboards#/view/unified-flow-top-n', '02-top-n-analysis'),
        ('/app/dashboards#/view/unified-flow-conversations', '03-conversation-partners')
    ]
    
    for path, filename in dashboards:
        try:
            print(f"\n📊 Opening {filename}...")
            url = kibana_url + path
            driver.get(url)
            time.sleep(10)  # Wait for dashboard to load
            
            print(f"Current URL: {driver.current_url}")
            
            # Check if redirected to login
            if 'login' in driver.current_url.lower():
                print(f"⚠️ Redirected to login - cannot screenshot {filename}")
                driver.save_screenshot(f"{output_dir}/{filename}-login-redirect.png")
                continue
            
            # Scroll to load all visualizations
            print("📜 Scrolling to load all panels...")
            for i in range(8):
                driver.execute_script("window.scrollBy(0, 800);")
                time.sleep(1)
            
            # Scroll back to top
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            
            # Take full page screenshot
            screenshot_path = f"{output_dir}/{filename}.png"
            driver.save_screenshot(screenshot_path)
            
            # Get file size
            size = os.path.getsize(screenshot_path)
            print(f"✅ Saved: {screenshot_path} ({size} bytes)")
            
            # Check for errors in page source
            page_source = driver.page_source
            errors_found = []
            if "can't access property" in page_source.lower() or "e is undefined" in page_source.lower():
                errors_found.append("JavaScript 'e is undefined' error")
            if "no data" in page_source.lower():
                errors_found.append("'No data' panels")
            if "no results" in page_source.lower():
                errors_found.append("'No results' panels")
                
            if errors_found:
                print(f"⚠️  Issues found: {', '.join(errors_found)}")
            else:
                print("✨ No obvious errors detected in page")
                
            # Additional scrolling screenshot for long dashboards
            if filename == '01-detailed-traffic':
                print("📜 Taking additional scrolled screenshots...")
                scroll_height = 800
                for i in range(3):
                    driver.execute_script(f"window.scrollTo(0, {scroll_height * (i+1)});")
                    time.sleep(2)
                    driver.save_screenshot(f"{output_dir}/{filename}-scroll-{i+1}.png")
            
        except Exception as e:
            print(f"❌ Error screenshotting {filename}: {e}")
            driver.save_screenshot(f"{output_dir}/{filename}-error.png")
    
    print("\n🎉 Screenshot session complete!")
    print(f"📁 Screenshots saved to: {output_dir}")
    
    # List all files
    files = os.listdir(output_dir)
    print(f"📂 Total files: {len(files)}")
    for f in sorted(files):
        size = os.path.getsize(os.path.join(output_dir, f))
        print(f"  - {f} ({size:,} bytes)")

finally:
    print("🔚 Closing browser...")
    driver.quit()
