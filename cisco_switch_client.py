#!/usr/bin/env python3
"""
Cisco Nexus SSH Interactive Client
Handles User Access Verification prompt with manual password entry simulation
"""

import paramiko
import time
import sys
import os

class CiscoSSHClient:
    def __init__(self, hostname, username, password, port=22):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.client = None
        self.shell = None
        
    def connect(self):
        """Connect with keyboard-interactive authentication"""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Custom handler for keyboard-interactive auth
        def handler(title, instructions, prompt_list):
            print(f"Auth prompt: {title}")
            responses = []
            for prompt, show_input in prompt_list:
                print(f"Prompt: {prompt.strip()}")
                if 'password' in prompt.lower() or 'pass' in prompt.lower():
                    responses.append(self.password)
                else:
                    responses.append('')
            return responses
        
        try:
            # First try standard password auth
            self.client.connect(
                self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                look_for_keys=False,
                allow_agent=False,
                timeout=30
            )
        except paramiko.AuthenticationException:
            # Fall back to keyboard-interactive
            print("Using keyboard-interactive authentication...")
            self.client.connect(
                self.hostname,
                port=self.port,
                username=self.username,
                look_for_keys=False,
                allow_agent=False,
                timeout=30
            )
            
        # Open interactive shell
        self.shell = self.client.invoke_shell()
        self.shell.settimeout(30)
        
        # Handle initial prompts (User Access Verification + password)
        buffer = ""
        auth_complete = False
        max_attempts = 50
        
        for _ in range(max_attempts):
            try:
                if self.shell.recv_ready():
                    data = self.shell.recv(4096).decode('utf-8', errors='ignore')
                    buffer += data
                    print(data, end='', flush=True)
                    
                    # Detect password prompt and send password
                    if not auth_complete and ('User Access Verification' in data or 
                                              'Password:' in data or 
                                              'password:' in data.lower()):
                        time.sleep(0.5)
                        self.shell.send(self.password + '\n')
                        print("\n[Password sent]")
                        auth_complete = True
                        
                    # Detect shell prompt (success)
                    if data.strip().endswith('#') or data.strip().endswith('>'):
                        print("\n[Connected successfully]")
                        return True
                        
                time.sleep(0.1)
            except Exception as e:
                print(f"\nError during connection: {e}")
                break
                
        return False
    
    def send_command(self, command, wait_time=2):
        """Send command and get output"""
        if not self.shell:
            return None
            
        self.shell.send(command + '\n')
        time.sleep(wait_time)
        
        output = ""
        while self.shell.recv_ready():
            chunk = self.shell.recv(4096).decode('utf-8', errors='ignore')
            output += chunk
            if chunk.strip().endswith('#') or chunk.strip().endswith('>'):
                break
            time.sleep(0.2)
            
        return output
    
    def get_interface_info(self):
        """Get interface brief from switch"""
        commands = [
            ('terminal_length', 'terminal length 0'),
            ('version', 'show version'),
            ('interfaces', 'show interface brief'),
            ('ip_interfaces', 'show ip interface brief'),
            ('features', 'show running-config | include feature'),
            ('sflow_status', 'show sflow'),
            ('netflow_status', 'show netflow')
        ]
        
        results = {}
        for name, cmd in commands:
            print(f"\n>>> Executing: {cmd}")
            output = self.send_command(cmd, wait_time=3)
            results[name] = output
            print(f"[Got {len(output)} chars of output]")
            
        return results
    
    def generate_sflow_config(self, collector_ip, collector_port=6343, sample_rate=4096):
        """Generate sFlow configuration commands"""
        
        # Parse interface brief to find active trunk ports
        interfaces_output = self.send_command('show interface brief', wait_time=3)
        
        active_interfaces = []
        for line in interfaces_output.split('\n'):
            if line.startswith('Eth') and 'up' in line and 'trunk' in line:
                parts = line.split()
                if len(parts) >= 2:
                    iface = parts[0]
                    active_interfaces.append(iface)
        
        # Generate sFlow config
        config = f"""! sFlow Configuration for {self.hostname}
! Generated automatically
!
configure terminal

! Enable sFlow
feature sflow

! Set sampling rate (1/{sample_rate})
sflow sampling-rate {sample_rate}

! Set collector
sflow collector-ip {collector_ip} vrf default
sflow collector-port {collector_port}

! Set sample size
sflow max-sampled-size 128
sflow counter-poll-interval 20

! Enable sFlow on active interfaces (trunk ports)
"""
        
        for iface in active_interfaces[:10]:  # Limit to first 10 for example
            config += f"sflow data-source interface {iface}\n"
            
        config += """
! Verify configuration
show sflow

end
"""
        
        return config, active_interfaces
    
    def close(self):
        """Close connection"""
        if self.shell:
            self.shell.close()
        if self.client:
            self.client.close()


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 cisco_switch_client.py <IP> <username> <password>")
        print("Example: python3 cisco_switch_client.py 10.4.4.3 admin t3l3lh0us3")
        sys.exit(1)
        
    ip = sys.argv[1]
    user = sys.argv[2]
    pwd = sys.argv[3]
    
    print(f"Connecting to Cisco Nexus at {ip}...")
    print("="*60)
    
    client = CiscoSSHClient(ip, user, pwd)
    
    try:
        # Connect
        if not client.connect():
            print("Failed to connect!")
            sys.exit(1)
            
        # Get interface info
        print("\n" + "="*60)
        print("COLLECTING INTERFACE INFORMATION")
        print("="*60)
        
        results = client.get_interface_info()
        
        # Display results
        print("\n" + "="*60)
        print("RESULTS")
        print("="*60)
        
        for name, output in results.items():
            print(f"\n--- {name.upper()} ---")
            print(output[:2000])  # Limit display
            
        # Generate sFlow config
        print("\n" + "="*60)
        print("GENERATING SFLOW CONFIGURATION")
        print("="*60)
        
        sflow_config, active_ifaces = client.generate_sflow_config(
            collector_ip='10.4.4.21',  # Backend N1
            collector_port=6343,
            sample_rate=4096
        )
        
        print(f"\nFound {len(active_ifaces)} active interfaces")
        print("\nSample sFlow Config:")
        print(sflow_config)
        
        # Save config to file
        filename = f"/tmp/sflow_config_{ip.replace('.', '_')}.txt"
        with open(filename, 'w') as f:
            f.write(sflow_config)
        print(f"\nConfig saved to: {filename}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        client.close()


if __name__ == '__main__':
    main()
