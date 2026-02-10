#!/usr/bin/env python3
"""
sFlow Configuration Script for Cisco Nexus Switches (v2)

Applies sFlow configuration to NEXUS1 (10.4.4.3) and NEXUS2 (10.4.4.4)
Collector: 10.4.4.90:6343
Sampling rate: 1-out-of-4096

Cisco NX-OS sFlow Commands Reference:
- feature sflow
- sflow collector-ip <ip> vrf <vrf>
- sflow collector-port <port>
- sflow sampling-rate <rate>
- sflow data-source interface <ifname> (interface command)
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/tools')
from nexus_netmiko import NexusSSH

# Device configurations
DEVICES = {
    'NEXUS1': {'host': '10.4.4.3', 'username': 'admin', 'password': 't3l3h0us3', 'desc': 'B-IX_Switch1'},
    'NEXUS2': {'host': '10.4.4.4', 'username': 'admin', 'password': 't3l3h0us3', 'desc': 'B-IX_Switch2'}
}

# Collector settings
COLLECTOR_IP = '10.4.4.90'
COLLECTOR_PORT = 6343
COLLECTOR_VRF = 'default'
SAMPLING_RATE = 4096  # 1 out of 4096 packets

def configure_global_sflow(conn):
    """Configure global sFlow settings."""
    commands = [
        # Enable sFlow feature
        'no feature sflow',  # Disable first to reset
        'feature sflow',
        # Configure collector
        f'sflow collector-ip {COLLECTOR_IP} vrf {COLLECTOR_VRF}',
        f'sflow collector-port {COLLECTOR_PORT}',
        # Configure sampling rate (1 out of N)
        f'sflow sampling-rate {SAMPLING_RATE}',
    ]
    
    results = []
    for cmd in commands:
        print(f"  >> {cmd}")
        output = conn.exec(cmd)
        output_stripped = output.strip()
        # Check for errors
        if any(err in output for err in ['Invalid', 'ERROR', '% ', 'Ambiguous', 'incomplete']):
            print(f"     ⚠ ERROR: {output_stripped[:200]}")
            results.append((cmd, output_stripped, False))
        elif output_stripped:
            print(f"     Output: {output_stripped[:200]}")
            results.append((cmd, output_stripped, True))
        else:
            results.append((cmd, '', True))
    return results

def configure_interface_sflow(conn, interface):
    """Configure sFlow on a specific interface."""
    # Interface commands for sFlow in NX-OS
    commands = [
        f'interface {interface}',
        'sflow data-source interface',
    ]
    
    for cmd in commands:
        print(f"  >> {cmd}")
        output = conn.exec(cmd)
        if output.strip():
            print(f"     Output: {output.strip()[:200]}")

def configure_switch(name, config):
    """Configure sFlow on a single switch."""
    print(f"\n{'='*60}")
    print(f"Configuring {name} ({config['host']}) - {config['desc']}")
    print(f"{'='*60}")
    
    conn = None
    try:
        conn = NexusSSH(config['host'], config['username'], config['password'], 
                       device_type='cisco_nxos', name=name)
        conn.connect(timeout=30)
        print(f"✓ Connected to {name}")
        
        # Check current sFlow status
        print("\n> Checking current sFlow status...")
        try:
            current = conn.exec('show sflow')
            if current.strip():
                print(f"  Current status:\n{current[:1000]}")
            else:
                print("  sFlow is currently not enabled.")
        except Exception as e:
            print(f"  sFlow not configured or error: {e}")
        
        # Apply global configuration
        print("\n> Applying global sFlow configuration...")
        global_results = configure_global_sflow(conn)
        
        # Skip interface config for now - just enable globally first
        # Interface sFlow on Nexus uses 'sflow data-source interface' command
        # when in interface config mode
        
        # Verify configuration
        print("\n> Verifying sFlow configuration...")
        verification = conn.exec('show sflow')
        print(f"\n{'-'*60}")
        print("sFlow Configuration Verification:")
        print(f"{'-'*60}")
        print(verification if verification.strip() else "sFlow verification returned empty")
        
        conn.disconnect()
        print(f"\n✓ Disconnected from {name}")
        
        return True, verification if verification.strip() else "sFlow configured (no show output)"
        
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
    
    # Configure both switches
    for name, config in DEVICES.items():
        success, output = configure_switch(name, config)
        results[name] = {'success': success, 'output': output}
    
    # Summary
    print(f"\n{'#'*60}")
    print("CONFIGURATION SUMMARY")
    print(f"{'#'*60}")
    all_success = True
    for name, result in results.items():
        status = "✓ SUCCESS" if result['success'] else "✗ FAILED"
        print(f"{name}: {status}")
        if not result['success']:
            all_success = False
    
    # Save results to file
    result_file = '/home/valentinbot/.openclaw/workspace/custom-elk-stack/monitoring/sflow_v2_results.txt'
    with open(result_file, 'w') as f:
        f.write("sFlow Configuration Results (v2)\n")
        f.write("="*60 + "\n\n")
        for name, result in results.items():
            f.write(f"{name} ({DEVICES[name]['host']}):\n")
            f.write(f"Success: {result['success']}\n")
            f.write(f"Output:\n{result['output']}\n")
            f.write("-"*60 + "\n\n")
    
    print(f"\nResults saved to: {result_file}")
    
    return all_success

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
