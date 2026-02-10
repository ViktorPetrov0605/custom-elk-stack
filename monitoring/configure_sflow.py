#!/usr/bin/env python3
"""
sFlow Configuration Script for Cisco Nexus Switches

Applies sFlow configuration to NEXUS1 (10.4.4.3) and NEXUS2 (10.4.4.4)
Collector: 10.4.4.90:6343
Sampling rate: 1-out-of-4096
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/tools')
from nexus_netmiko import NexusSSH

# Device configurations
DEVICES = {
    'NEXUS1': {'host': '10.4.4.3', 'username': 'admin', 'password': 't3l3h0us3'},
    'NEXUS2': {'host': '10.4.4.4', 'username': 'admin', 'password': 't3l3h0us3'}
}

# Base sFlow configuration commands (global)
BASE_CONFIG = [
    # Enable sFlow feature
    'feature sflow',
    # Configure sFlow collector
    'collect-sflow 10.4.4.90 vrf default port 6343',
    # Set sampling rate globally (1 out of 4096)
    'sflow sampling 4096'
]

# Interfaces to configure with sFlow
# Based on nexus-analysis.md: all critical interfaces
INTERFACES = [
    'interface port-channel 200',   # vPC Peer-Link
    'interface port-channel 599',   # TH-DS5/6-VPC
    'interface port-channel 111',   # 1-IX (Note: DOWN on NEXUS2)
    'interface port-channel 6',     # SOX-80G
    'interface port-channel 10',    # Google-20G
    'interface port-channel 62',    # RETN
    'interface port-channel 71',    # TelecomArmenia
    'interface port-channel 871',   # A1BG_AS8717
    'interface port-channel 902',   # TH-SOF-DS1/2
    'interface ethernet 1/1'        # All ethernet 1/1-48 (we'll do range)
]

# Individual port-channel interface commands
INTERFACE_CONFIG_CMDS = [
    'interface port-channel 200',
    '  sflow sampling 4096',
    'interface port-channel 599',
    '  sflow sampling 4096',
    'interface port-channel 111',
    '  sflow sampling 4096',
    'interface port-channel 6',
    '  sflow sampling 4096',
    'interface port-channel 10',
    '  sflow sampling 4096',
    'interface port-channel 62',
    '  sflow sampling 4096',
    'interface port-channel 71',
    '  sflow sampling 4096',
    'interface port-channel 871',
    '  sflow sampling 4096',
    'interface port-channel 902',
    '  sflow sampling 4096',
    'interface ethernet 1/1-48',
    '  sflow sampling 4096'
]

def configure_switch(name: str, host: str, username: str, password: str, skip_interface: str = None):
    """
    Configure sFlow on a single switch.
    
    Args:
        name: Friendly name of the switch
        host: IP address
        username: SSH username
        password: SSH password
        skip_interface: Interface to skip (e.g., 'port-channel 111' for NEXUS2)
    """
    print(f"\n{'='*60}")
    print(f"Configuring {name} ({host})")
    print(f"{'='*60}")
    
    conn = None
    try:
        conn = NexusSSH(host, username, password, device_type='cisco_nxos', name=name)
        conn.connect(timeout=30)
        print(f"✓ Connected to {name}")
        
        # Check current sFlow status
        print("\n> Checking current sFlow status...")
        current = conn.exec('show sflow')
        if 'sFlow is not enabled' in current or not current.strip():
            print("  sFlow is currently not configured.")
        else:
            print(f"  Current status:\n{current[:500]}...")
        
        # Apply global configuration
        print("\n> Applying global sFlow configuration...")
        for cmd in BASE_CONFIG:
            print(f"  >> {cmd}")
            output = conn.exec(cmd)
            if output.strip():
                print(f"     Output: {output[:200]}")
        
        # Apply interface-specific configuration
        print("\n> Applying interface sFlow configuration...")
        for i, cmd in enumerate(INTERFACE_CONFIG_CMDS):
            # Skip Po111 on NEXUS2 since it's DOWN
            if name == 'NEXUS2' and 'port-channel 111' in cmd:
                print(f"  SKIPPING (interface DOWN on this switch): {cmd}")
                continue
            
            print(f"  >> {cmd}")
            output = conn.exec(cmd)
            if 'Invalid' in output or 'Error' in output or '%' in output:
                print(f"     ⚠ Warning: {output[:200]}")
            elif output.strip():
                print(f"     Output: {output[:200]}")
        
        # Verify configuration
        print("\n> Verifying sFlow configuration...")
        verification = conn.exec('show sflow all')
        print(f"\n{'='*60}")
        print(f"{name} - sFlow Configuration")
        print(f"{'='*60}")
        print(verification)
        
        conn.disconnect()
        print(f"\n✓ Disconnected from {name}")
        return True, verification
        
    except Exception as e:
        print(f"\n✗ FAILED: {e}")
        if conn:
            try:
                conn.disconnect()
            except:
                pass
        return False, str(e)


def main():
    """Main execution function."""
    results = {}
    
    # Configure NEXUS1
    success1, output1 = configure_switch(
        'NEXUS1',
        DEVICES['NEXUS1']['host'],
        DEVICES['NEXUS1']['username'],
        DEVICES['NEXUS1']['password']
    )
    results['NEXUS1'] = {'success': success1, 'output': output1}
    
    # Configure NEXUS2
    success2, output2 = configure_switch(
        'NEXUS2',
        DEVICES['NEXUS2']['host'],
        DEVICES['NEXUS2']['username'],
        DEVICES['NEXUS2']['password']
    )
    results['NEXUS2'] = {'success': success2, 'output': output2}
    
    # Summary
    print(f"\n{'#'*60}")
    print("CONFIGURATION SUMMARY")
    print(f"{'#'*60}")
    for name, result in results.items():
        status = "✓ SUCCESS" if result['success'] else "✗ FAILED"
        print(f"{name}: {status}")
    
    # Save results to file
    with open('/home/valentinbot/.openclaw/workspace/custom-elk-stack/monitoring/sflow_results.txt', 'w') as f:
        f.write("sFlow Configuration Results\n")
        f.write("="*60 + "\n\n")
        for name, result in results.items():
            f.write(f"{name}:\n")
            f.write(f"Success: {result['success']}\n")
            f.write(f"Output:\n{result['output']}\n")
            f.write("-"*60 + "\n\n")
    
    print("\nResults saved to: sflow_results.txt")
    
    return all(r['success'] for r in results.values())

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
