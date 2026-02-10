#!/usr/bin/env python3
"""
Kibana ElastiFlow Dashboard Automation
"""
import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/browser-venv/lib/python3.13/site-packages')

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json

def wait_and_log(msg, secs=25):
    print(f"[WAIT] {msg} ({secs}s)")
    time.sleep(secs)

def main():
    print("=== Starting Kibana Dashboard Automation ===")
    
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    
    print("[1/7] Starting Chrome driver...")
    driver = uc.Chrome(options=options, version_main=144)
    
    try:
        # Step 1: Navigate to Kibana
        print("[2/7] Navigating to Kibana...")
        driver.get('http://10.4.4.87:5601')
        wait_and_log("Initial page load")
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step1_login.png')
        
        # Step 2: Login
        print("[3/7] Logging in...")
        
        # Find and fill username
        username_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username'], input[data-test-subj='loginUsername'], #username, input[type='text']"))
        )
        username_field.clear()
        username_field.send_keys("elastic")
        print("   - Username entered")
        
        # Find and fill password
        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password'], input[data-test-subj='loginPassword'], #password, input[type='password']")
        password_field.clear()
        password_field.send_keys("telehouse")
        print("   - Password entered")
        
        # Click login button
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button[data-test-subj='loginSubmit'], .euiButton--primary")
        login_button.click()
        print("   - Login button clicked")
        
        wait_and_log("Login processing")
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step2_logged_in.png')
        
        # Step 3: Navigate to Dashboard
        print("[4/7] Navigating to Analytics → Dashboard...")
        
        # Try to find Analytics menu item
        try:
            # Look for "Analytics" in the left sidebar
            analytics_link = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Analytics')] | //span[contains(text(), 'Analytics')]//parent::a | //div[contains(text(), 'Analytics')]"))
            )
            analytics_link.click()
            print("   - Analytics menu clicked")
            wait_and_log("Analytics menu expanding")
        except:
            print("   - Could not find Analytics menu, trying direct URL...")
            driver.get('http://10.4.4.87:5601/app/dashboards')
            wait_and_log("Dashboard page loading")
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step3_analytics.png')
        
        # Step 4: Try to go directly to Create Dashboard
        print("[5/7] Creating new dashboard...")
        
        # Try direct URL for creating dashboard
        driver.get('http://10.4.4.87:5601/app/dashboards/create')
        wait_and_log("Dashboard create page loading", 30)
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step4_create_dashboard.png')
        
        # Step 5: Add panels - look for "Add panel" or "Create visualization" button
        print("[6/7] Adding ElastiFlow panels...")
        
        # Wait for the dashboard to fully load
        wait_and_log("Dashboard UI loading", 30)
        
        # Look for add panel button
        try:
            add_panel_btn = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-subj='dashboardAddPanelButton'], button[aria-label*='Add'], button[class*='addPanel']"))
            )
            add_panel_btn.click()
            print("   - Add panel button clicked")
            wait_and_log("Add panel dialog opening")
        except TimeoutException:
            # Try alternative - look for "Create visualization" 
            try:
                create_vis_btn = driver.find_element(By.CSS_SELECTOR, "[data-test-subj='dashboardCreateNewButton'], button[aria-label*='Create']")
                create_vis_btn.click()
                print("   - Create new button clicked")
                wait_and_log("Create dialog opening")
            except:
                print("   - Could not find add panel button, trying to find any clickable elements...")
                # Save page source for debugging
                with open('/home/valentinbot/.openclaw/workspace/kibana_step5_html.html', 'w') as f:
                    f.write(driver.page_source)
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step5_panels.png')
        
        # Step 6: Look for ElastiFlow visualizations or indices
        print("[7/7] Looking for ElastiFlow data...")
        
        # Search for ElastiFlow
        try:
            search_box = driver.find_element(By.CSS_SELECTOR, "input[data-test-subj='savedObjectFinderSearchInput'], input[placeholder*='Search']")
            search_box.clear()
            search_box.send_keys("elastiflow")
            print("   - Searching for ElastiFlow")
            wait_and_log("Search results loading")
        except:
            print("   - No search box found")
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_step6_elastiflow.png')
        
        # Try to save dashboard
        print("Attempting to save dashboard...")
        try:
            # Look for save button
            save_btn = driver.find_element(By.CSS_SELECTOR, "[data-test-subj='dashboardSaveButton'], button[aria-label*='Save']")
            save_btn.click()
            print("   - Save button clicked")
            wait_and_log("Save dialog opening")
            
            # Enter dashboard name
            name_field = driver.find_element(By.CSS_SELECTOR, "input[data-test-subj='dashboardTitle'], input[placeholder*='title']")
            name_field.clear()
            name_field.send_keys("ElastiFlow Dashboard")
            print("   - Dashboard name entered")
            
            # Confirm save
            confirm_btn = driver.find_element(By.CSS_SELECTOR, "button[data-test-subj='confirmSaveSavedObjectButton'], button[class*='save']")
            confirm_btn.click()
            print("   - Dashboard saved!")
            wait_and_log("Save processing")
        except Exception as e:
            print(f"   - Could not save dashboard: {e}")
        
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_final_dashboard.png')
        
        # Get current URL
        final_url = driver.current_url
        print(f"\n=== Final URL: {final_url} ===")
        
        # Save final HTML
        with open('/home/valentinbot/.openclaw/workspace/kibana_final_html.html', 'w') as f:
            f.write(driver.page_source)
        
        print("=== Automation Complete ===")
        print("Screenshots saved:")
        print("  - kibana_step1_login.png")
        print("  - kibana_step2_logged_in.png")
        print("  - kibana_step3_analytics.png")
        print("  - kibana_step4_create_dashboard.png")
        print("  - kibana_step5_panels.png")
        print("  - kibana_step6_elastiflow.png")
        print("  - kibana_final_dashboard.png")
        
    except Exception as e:
        print(f"ERROR: {e}")
        driver.save_screenshot('/home/valentinbot/.openclaw/workspace/kibana_error.png')
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
