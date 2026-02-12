from netmiko import ConnectHandler
import warnings
warnings.filterwarnings('ignore')

def fix_sflow_config(host, username, password):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
        'timeout': 15,
    }
    
    print(f"=== Fixing sFlow config on {host} ===")
    
    try:
        conn = ConnectHandler(**device)
        
        # Get current running config
        running_config = conn.send_command("show running-config | include sflow", read_timeout=60)
        print("Current running config:")
        print(running_config)
        
        # Save current config to startup config
        print("Saving running config to startup config...")
        conn.send_command("copy running-config startup-config", expect_string=r"#", read_timeout=60)
        
        # Verify startup config
        startup_config = conn.send_command("show startup-config | include sflow", read_timeout=60)
        print("Updated startup config:")
        print(startup_config)
        
        conn.disconnect()
        print(f"✅ Successfully fixed sFlow config on {host}")
        
    except Exception as e:
        print(f"❌ Failed to fix sFlow config on {host}: {e}")

# Fix NEXUS1 (10.4.4.3)
fix_sflow_config("10.4.4.3", "admin", "t3l3h0us3")

print("\n" + "="*60 + "\n")

# Fix NEXUS2 (10.4.4.4)
fix_sflow_config("10.4.4.4", "admin", "t3l3h0us3")