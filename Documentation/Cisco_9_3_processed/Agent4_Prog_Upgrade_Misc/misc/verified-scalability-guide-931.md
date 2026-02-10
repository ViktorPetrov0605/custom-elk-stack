# Cisco Nexus 9000 Series NX-OS Verified Scalability Guide, Release 9.3(1)

**Source:** b-Cisco_Nexus-9000-Series-NX-OS-Verified-Scalability-Guide-931.html

**Tags:** scalability, performance, limits, scale, verified, capacity-planning

**Updated:** November 2, 2020

---

## Introduction

This document describes the Cisco NX-OS configuration limits for Cisco Nexus 9000 Series switches. The values provided in this guide should not be interpreted as theoretical system limits for Cisco NX-OS hardware or software. These limits refer to values that have been validated by Cisco. They can increase over time as more testing and validation is done.

---

## Verified Scalability Limits - Unidimensional

The tables in this section list the verified scalability limits for the Cisco Nexus 9000 Series switches for Cisco NX-OS Release 9.3(1).

### FEX (Fabric Extenders) Verified Scalability Limits

| Feature | Supported Platforms | Verified Limits |
|---------|---------------------|-----------------|
| Fabric Extenders and FEX server interfaces | Nexus 9300, 9300-EX, -FX switches | 16 and 768 |
| Fabric Extenders and FEX server interfaces | Nexus 9500 switches | 32 and 1536 |
| VLANs across all Fabric Extenders | Nexus 9300 and 9500 switches | 2,000 |
| VLANs across all Fabric Extenders | Nexus 9300-EX and 9300-FX switches | 562 |
| Port channels | Nexus 9300 switches | 256 |
| Port channels | Nexus 9300-EX and 9300-FX/FX2 switches + FEX | 511 |
| Port channels | Nexus 9500 switches | 426 |

### FCoE Verified Scalability Limits

| Feature | Supported Platforms | Verified Limits |
|---------|---------------------|-----------------|
| FLOGI per port | Nexus 93180YC-FX | 256 |
| FLOGI per switch | Nexus 93180YC-FX | 1,000 |
| Port channels | Nexus 93180YC-FX switches | 8 |
| Maximum member ports in port channel | Nexus 93180YC-FX switches | 16 |
| VFCs | Nexus 93180YC-FX switches | 544 |
| VSANs | Nexus 93180YC-FX switches | 32 |

---

## Verified Scalability Limits - Multidimensional

Multidimensional scale testing validates limits when multiple features are used simultaneously.

---

## Deployment Case Studies

### Layer 2/Layer 3 Aggregation Topology (Max-Host Routing Mode)
- Maximum host routing configuration
- Scale parameters for aggregation deployments
- Platform-specific considerations

### Layer 2/Layer 3 Aggregation Topology (Default Routing Mode)
- Default routing scale parameters
- Feature interaction testing

### FEX System Topology
- FEX deployment at scale
- Host interface scaling
- Uplink considerations

### Multicast System Topology
- Multicast replication scaling
- IGMP/MLD snooping limits
- PIM scale parameters

### VXLAN BGP/eVPN iBGP Centric Topology
- VXLAN tunnel scale
- EVPN route scale
- BGP sessions and routes

---

## Document Download Options

- **PDF** (1.1 MB)

---

## Important Notes

1. If only one number is provided, the verified limit applies to all supported platforms and line cards.
2. Verified limits are provided only for supported platforms.
3. If a feature is not supported for a particular platform, the verified limit is not provided.
4. Results might differ from the values listed when trying to achieve maximum scalability with multiple features enabled.

---

*This document applies to: Nexus 9000 Series Switches*
