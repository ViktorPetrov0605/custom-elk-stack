#!/usr/bin/env python3
"""
Simple sFlow configuration for Cisco Nexus switches.
"""

import sys
sys.path.insert(0, '/home/valentinbot/.openclaw/tools')
from nexus_netmiko import NexusSSH

# Configuration
COLLECTOR_IP = '10.4.4.90'
COLLECTOR_PORT = 6343
COLLECTOR_VRF = 'default'
SAMPLING_RATE = 4096

# NEXUS1 already has sFlow with collector - just add interfaces
NEXUS1_INTFS = [
    'interface port-channel 200',
    ' interface port-channel 200',
    'sflow data-source interface port-channel200',
    'interface port-channel 599',
    'sflow data-source interface port-channel599',
    'interface port-channel 111',
    'sflow data-source interface port-channel111',
    'interface port-channel 62',
    'sflow data-source interface port-channel62',
    'interface port-channel 71',
    'sflow data-source interface port-channel71',
    'interface port-channel 871',
    'sflow data-source interface port-channel871',
    'interface port-channel 902',
    'sflow data-source interface port-channel902',
]

# NEXUS2 needs full config + interfaces (Po111 is DOWN)
NEXUS2_CONFIG = [
    # Global config
    'feature sflow',
    f'sflow collector-ip {COLLECTOR_IP} vrf {COLLECTOR_VRF}',
    f'sflow collector-port {COLLECTOR_PORT}',
    f'sflow sampling-rate {SAMPLING_RATE}',
    # Interfaces (Po111 skipped as it's DOWN)
    'sflow data-source interface port-channel200',
    'sflow data-source interface port-channel599',
    'sflow data-source interface port-channel6',
    'sflow data-source interface port-channel10', 
    'sflow data-source interface port-channel62',
    'sflow data-source interface port-channel71',
    'sflow data-source interface port-channel871',
    'sflow data-source interface port-channel902',
]

def configure_nexus1():
    """Configure NEXUS1 - add missing interfaces."""
    print("="*60)
    print("Configuring NEXUS1 (10.4.4.3) - Adding interfaces")
    print("="*60)
    
    try:
        with NexusSSH('10.4.4.3', 'admin', 't3l3h0us3', device_type='cisco_nxos', name='NEXUS1') as conn:
            print("\n> Current sFlow status:")
            print(conn.exec('show sflow'))
            
            print("\n> Adding interfaces to sFlow...")
            for intf_cmd in NEXUS1_INTFS[::2]:  # Take interface commands
                # Use send_config_set to configure
                output = conn.configure([intf_cmd, 'sflow data-source interface'])
                print(f"  Added {intf_cmd}")
            
            print("\n> Verification:")
            print(conn.exec('show sflow'))
            
            return True, "Updated"
    except Exception as e:
        print(f"Error: {e}")
        return False, str(e)

def configure_nexus2():
    """Configure NEXUS2 - full config."""
    print("="*60)
    print("Configuring NEXUS2 (10.4.4.4) - Full configuration")
    print("="*60)
    
    try:
        with NexusSSH('10.4.4.4', 'admin', 't3l3h0us3', device_type='cisco_nxos', name='NEXUS2') as conn:
            print("\n> Applying full sFlow configuration...")
            output = conn.configure(NEXUS2_CONFIG)
            print(f"Config output: {output[:500] if output else 'None'}")
            
            print("\n> Verification:")
            verif = conn.exec('show sflow')
            print(verif)
            
            return True, verif if verif else "Config applied"
    except Exception as e:
        print(f"Error: {e}")
        return False, str(e)

def main():
    """Main function."""
    results = {'NEXUS1': configure_nexus1(), 'NEXUS2': configure_nexus2()}
    
    print("\n" + "#"*60)
    print("SUMMARY")
    print("#"*60)
    for name, (success, _) in results.items():
        print(f"{name}: {'✓ SUCCESS' if success else '✗ FAILED'}")
    
    # Save documentation
    doc_path = '/home/valentinbot/.openclaw/workspace/custom-elk-stack/monitoring/nexus-sflow-config.md'
    with open(doc_path, 'w') as f:
        f.write("# Cisco Nexus sFlow Configuration\n\n")
        f.write("**Date:** 2026-02-09\n\n")
        f.write(f"**Collector:** {COLLECTOR_IP}:{COLLECTOR_PORT}\n\n")
        f.write(f"**Sampling Rate:** 1-out-of-{SAMPLING_RATE}\n\n")
        f.write("## Status\n\n")
        for name, (success, output) in results.items():
            f.write(f"### {name}\n")
            f.write(f"- **Status:** {'✓ SUCCESS' if success else '✗ FAILED'}\n")
            f.write(f"- **Output:** `{output[:200]}`\n\n")
    
    print(f"\n✓ Documentation saved to {doc_path}")
    return all(r[0] for r in results.values())

if __name__ == '__main__':
    sys.exit(0 if main() else 1)
