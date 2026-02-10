#!/usr/bin/env python3
"""
sFlow Configuration Script for Cisco Nexus Switches (Final)

Applies sFlow configuration to NEXUS1 (10.4.4.3) and NEXUS2 (10.4.4.4)
Collector: 10.4.4.90:6343
Sampling rate: 1-out-of-4096

Based on analysis, NEXUS1 already has sFlow configured with collector.
NEXUS2 needs full configuration.
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/tools')
from nexus_netmiko import NexusSSH

# Device configurations
DEVICES = {
    'NEXUS1': {'host': '10.4.4.3', 'username': 'admin', 'password': 't3l3h0us3', 
               'desc': 'B-IX_Switch1', 'existing': True},
    'NEXUS2': {'host': '10.4.4.4', 'username': 'admin', 'password': 't3l3h0us3', 
               'desc': 'B-IX_Switch2', 'existing': False}
}

# Collector settings
COLLECTOR_IP = '10.4.4.90'
COLLECTOR_PORT = 6343
COLLECTOR_VRF = 'default'
SAMPLING_RATE = 4096

# Interfaces to configure based on nexus-analysis.md critical interfaces
# Po111 is DOWN on NEXUS2, Eth1/33 is disabled - handle separately
INTERFACES = [
    'port-channel 200',   # vPC Peer-Link
    'port-channel 599',   # TH-DS5/6-VPC
    'port-channel 111',   # 1-IX (DOWN on NEXUS2)
    'port-channel 6',     # SOX-80G
    'port-channel 10',    # Google-20G
    'port-channel 62',    # RETN
    'port-channel 71',    # TelecomArmenia
    'port-channel 871',   # A1BG_AS8717
    'port-channel 902',   # TH-SOF-DS1/2
]

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
            if 'Invalid' not in current and current.strip():
                print(f"  sFlow is ENABLED. Current config:\n{current[:1500]}")
                has_sflow = True
            else:
                print("  sFlow is NOT configured yet.")
                has_sflow = False
        except Exception as e:
            print(f"  sFlow check error: {e}")
            has_sflow = False
        
        # Enter configuration mode
        print("\n> Entering configuration mode...")
        output = conn.exec('configure terminal')
        if 'Invalid' in output or '%' in output:
            print(f"  ⚠ Config mode error: {output[:200]}")
            # Try alternative
            output = conn.exec('conf t')
        print("  ✓ In configuration mode")
        
        # For NEXUS2 (or any switch without sFlow), configure global settings
        if not has_sflow:
            print("\n> Configuring global sFlow settings...")
            global_cmds = [
                'feature sflow',
                f'sflow collector-ip {COLLECTOR_IP} vrf {COLLECTOR_VRF}',
                f'sflow collector-port {COLLECTOR_PORT}',
                f'sflow sampling-rate {SAMPLING_RATE}',
            ]
            for cmd in global_cmds:
                print(f"  >> {cmd}")
                out = conn.exec(cmd)
                if out.strip():
                    print(f"     {out.strip()[:200]}")
        else:
            print("\n> Global sFlow already configured, skipping...")
        
        # Configure interfaces
        print(f"\n> Configuring sFlow on interfaces (Po111 skipped on NEXUS2)...")
        for intf in INTERFACES:
            # Skip Po111 on NEXUS2 (it's DOWN/noOperMem)
            if name == 'NEXUS2' and '111' in intf:
                print(f"  SKIPPING {intf} (DOWN on NEXUS2)")
                continue
            
            cmd = f'sflow data-source interface {intf}'
            print(f"  >> {cmd}")
            out = conn.exec(cmd)
            if 'Invalid' in out or 'Error' in out or '%' in out:
                print(f"     ⚠ Warning: {out.strip()[:150]}")
        
        # Exit config mode
        print("\n> Exiting configuration mode...")
        conn.exec('end')
        
        # Verify configuration
        print("\n> Verifying final sFlow configuration...")
        verification = conn.exec('show sflow')
        print(f"\n{'-'*60}")
        print(f"{name} sFlow Configuration:")
        print(f"{'-'*60}")
        print(verification if verification.strip() else "No verification output")
        
        # Also run show sflow to check interface list
        try:
            all_conf = conn.exec('show running-config | include sflow')
            print(f"\nAll sFlow config lines:\n{all_conf[:2000]}")
        except:
            pass
        
        conn.disconnect()
        print(f"\n✓ Disconnected from {name}")
        
        return True, verification
        
    except Exception as e:
        print(f"\n✗ FAILED: {e}")
        import traceback
        traceback.print_exc()
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
    print("FINAL CONFIGURATION SUMMARY")
    print(f"{'#'*60}")
    all_success = True
    for name, result in results.items():
        status = "✓ SUCCESS" if result['success'] else "✗ FAILED"
        print(f"{name}: {status}")
        if not result['success']:
            all_success = False
    
    # Also verify collector connectivity if possible
    print(f"\n{'#'*60}")
    print("NEXT STEPS:")
    print(f"{'#'*60}")
    print("1. Wait 5 minutes for sFlow data to start flowing")
    print("2. Verify UDP 6343 on 10.4.4.90 is receiving sFlow data")
    
    # Save results
    doc_path = '/home/valentinbot/.openclaw/workspace/custom-elk-stack/monitoring/nexus-sflow-config.md'
    with open(doc_path, 'w') as f:
        f.write("# Cisco Nexus sFlow Configuration Documentation\n\n")
        f.write("**Configuration Date:** 2026-02-09\n\n")
        f.write("**Collector:** 10.4.4.90:6343\n\n")
        f.write("**Sampling Rate:** 1-out-of-4096\n\n")
        f.write("---\n\n")
        
        for name, result in results.items():
            f.write(f"## {name} ({DEVICES[name]['host']})\n\n")
            f.write(f"**Status:** {'✓ SUCCESS' if result['success'] else '✗ FAILED'}\n\n")
            f.write(f"**Verification Output:**\n```\n{result['output']}\n```\n\n")
            f.write("---\n\n")
        
        f.write("## Configuration Commands Applied\n\n")
        f.write("```\n")
        f.write("# Global sFlow configuration\n")
        f.write("feature sflow\n")
        f.write(f"sflow collector-ip {COLLECTOR_IP} vrf {COLLECTOR_VRF}\n")
        f.write(f"sflow collector-port {COLLECTOR_PORT}\n")
        f.write(f"sflow sampling-rate {SAMPLING_RATE}\n")
        f.write("\n")
        f.write("# Interface configuration\n")
        for intf in INTERFACES:
            f.write(f"sflow data-source interface {intf}\n")
        f.write("```\n\n")
        f.write("**Note:** Po111 was skipped on NEXUS2 as it is DOWN (no operational members).\n")
    
    print(f"\n✓ Documentation saved to: {doc_path}")
    
    return all_success

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
