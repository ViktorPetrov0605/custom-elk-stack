# Troubleshooting the Cisco Nexus 9000v

**Source:** m-troubleshooting-the-cisco-nexus-9000v-93x.html

**Tags:** nexus-9000v, troubleshooting, virtual, diagnostics, kvm, vmware, debug

---

## Overview

This document provides troubleshooting procedures specific to the Cisco Nexus 9000v virtual switch platform running NX-OS Release 9.3(x).

---

## Common Issues

### Boot Problems
- VM fails to start
- Kernel panic on boot
- Filesystem errors
- Initial configuration issues

### Connectivity Issues
- No management connectivity
- Data plane issues
- Interface problems
- vPC simulation issues

### Performance Issues
- High CPU utilization
- Memory exhaustion
- Packet loss
- Latency issues

---

## Diagnostic Commands

### System Information
```
show version
show system resources
show processes cpu
show processes memory
```

### Virtual-Specific Commands
```
show platform
show hardware
show virtual-service
```

---

## KVM-Specific Troubleshooting

### Checking VM Status
- virsh commands
- QEMU monitor
- Console access

### Network Troubleshooting
- Bridge configuration
- vNIC configuration
- MAC address issues

---

## VMware-Specific Troubleshooting

### vSphere Troubleshooting
- VM console access
- vNIC configuration
- Resource allocation checks
- vSwitch configuration

---

## Log Collection

### NX-OS Logs
- System log (syslog)
- Kernel messages
- Process logs

### Hypervisor Logs
- KVM: /var/log/libvirt
- VMware: vmware.log

---

## Known Limitations

- Hardware features not supported
- Scale limitations
- Performance variations
- Specific unsupported features

---

## Support and Resources

- Cisco Support Community
- Virtual platform documentation
- Feature compatibility matrix

---

*Part of Cisco Nexus 9000 Series NX-OS Documentation, Release 9.3(x)*
