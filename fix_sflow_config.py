#!/usr/bin/env python3
"""
Fix sFlow configuration on Cisco Nexus switches
"""

import paramiko
import time
import sys

def configure_switch(hostname, username, password, collector_ip, collector_port=6343):
    """Configure sFlow on a Cisco Nexus switch"""
    print(f"\n{'='*60}")
    print(f"Configuring {hostname}")
    print('='*60)
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname, username=username, password=password, 
                      look_for_keys=False, allow_agent=False, timeout=30)
    except Exception as e:
        print(f"Connection error: {e}")
        return False
    
    shell = client.invoke_shell()
    shell.settimeout(30)
    
    # Wait for initial prompt
    time.sleep(2)
    
    # Clear buffer
    while shell.recv_ready():
        shell.recv(4096)
    
    # Send config commands
    commands = [
        'configure terminal',
        f'sflow collector-ip {collector_ip} vrf default',
        f'sflow collector-port {collector_port}',
        'end',
        'copy running-config startup-config',
        'show sflow'
    ]
    
    output = ""
    for cmd in commands:
        print(f"\n>> {cmd}")
        shell.send(cmd + '\n')
        time.sleep(1)
        
        # Collect output
        while shell.recv_ready():
            chunk = shell.recv(4096).decode('utf-8', errors='ignore')
            output += chunk
            if '[confirm]' in chunk or '(y/n)' in chunk.lower() or 'confirm' in chunk.lower():
                shell.send('y\n')
                time.sleep(0.5)
    
    print("\n--- Output ---")
    print(output[-2000:])  # Last 2000 chars
    
    shell.close()
    client.close()
    return True

if __name__ == '__main__':
    # Configure both switches
    switches = [
        ('10.4.4.3', 'admin', 't3l3h0us3', '10.4.4.90'),
        ('10.4.4.4', 'admin', 't3l3h0us3', '10.4.4.90'),
    ]
    
    for ip, user, pwd, collector in switches:
        try:
            configure_switch(ip, user, pwd, collector, 6343)
        except Exception as e:
            print(f"❌ Failed to configure {ip}: {e}")

    print("\n" + "="*60)
    print("sFlow configuration complete!")
    print("="*60)
