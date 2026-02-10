# Configuring Unidirectional Ethernet

**Source:** m-n9000-configuring-unidirectional-ethernet.html

**Tags:** ethernet, unidirectional, link-fault, detection, physical-layer, diagnostics

---

## Overview

Unidirectional Ethernet is a network fault detection mechanism that allows for the detection of unidirectional link failures in Layer 2 networks. This feature helps prevent issues such as spanning tree loops and broadcast storms that can occur when a link fails in one direction only.

---

## Key Concepts

### Unidirectional Link Detection (UDLD)
- Protocol for detecting unidirectional links
- Helps prevent Layer 2 network issues
- Works by exchanging packets with neighbor devices

### Physical Layer Considerations
- Fiber optic cable issues
- Transceiver failures
- One-way communication problems

---

## Configuration Steps

### Enabling UDLD
- Global configuration
- Per-interface configuration
- Mode settings (normal vs. aggressive)

### Verification Commands
```
show udld global
show udld interface
```

---

## Use Cases

- Data center interconnects
- Long-haul fiber connections
- Critical infrastructure links
- Spanning tree protection

---

## Related Topics

- Layer 2 switching
- Spanning Tree Protocol (STP)
- Interface configuration
- Troubleshooting physical layer issues

---

*Part of Cisco Nexus 9000 Series NX-OS Documentation, Release 9.3(x)*
