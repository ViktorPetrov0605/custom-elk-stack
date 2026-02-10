#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

print("Starting Kibana automation...")

options = uc.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=options, version_main=144)

try:
    # Navigate to Kibana
    print("Navigating to Kibana...")
    driver.get('http://10.4.4.87:5601')
    time.sleep(15)
    driver.save_screenshot('/home/valentinbot/.openclaw/workspace/step1.png')
    print("Screenshot saved: step1.png")
    
    # Find all input elements
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"Found {len(inputs)} input elements")
    
    # Try to find username field by placeholder or type
    username_found = False
    password_found = False
    
    for inp in inputs:
        try:
            placeholder = inp.get_attribute("placeholder") or ""
            input_type = inp.get_attribute("type") or ""
            name = inp.get_attribute("name") or ""
            
            print(f"Input: type={input_type}, name={name}, placeholder={placeholder}")
            
            if "user" in name.lower() or "user" in placeholder.lower() or input_type == "text":
                if not username_found:
                    inp.clear()
                    inp.send_keys("elastic")
                    print("  -> Entered username")
                    username_found = True
            
            if "pass" in name.lower() or "pass" in placeholder.lower() or input_type == "password":
                if not password_found:
                    inp.clear()
                    inp.send_keys("telehouse")
                    print("  -> Entered password")
                    password_found = True
        except Exception as e:
            print(f"Error with input: {e}")
    
    time.sleep(2)
    driver.save_screenshot('/home/valentinbot/.openclaw/workspace/step2_creds.png')
    
    # Find and click login button
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Found {len(buttons)} buttons")
    
    for btn in buttons:
        try:
            text = btn.text or ""
            print(f"Button text: {text}")
            if "log" in text.lower() or "sign" in text.lower():
                btn.click()
                print("  -> Clicked login button")
                break
        except Exception as e:
            pass
    
    print("Waiting for login...")
    time.sleep(25)
    driver.save_screenshot('/home/valentinbot/.openclaw/workspace/step3_loggedin.png')
    
    # Navigate to dashboards directly
    print("Navigating to dashboards...")
    driver.get('http://10.4.4.87:5601/app/dashboards/list')
    time.sleep(20)
    driver.save_screenshot('/home/valentinbot/.openclaw/workspace/step4_dashboards.png')
    
    # Try to create new dashboard
    print("Creating new dashboard...")
    driver.get('http://10.4.4.87:5601/app/dashboards/create')
    time.sleep(20)
    driver.save_screenshot('/home/valentinbot/.openclaw/workspace/step5_create.png')
    
    # Save HTML for analysis
    with open('/home/valentinbot/.openclaw/workspace/page_final.html', 'w') as f:
        f.write(driver.page_source)
    
    print(f"Final URL: {driver.current_url}")
    print("Screenshots saved:")
    print("  - step1.png (initial page)")
    print("  - step2_creds.png (credentials entered)")
    print("  - step3_loggedin.png (after login)")
    print("  - step4_dashboards.png (dashboards list)")
    print("  - step5_create.png (create dashboard)")
    
finally:
    driver.quit()
    print("Done!")
