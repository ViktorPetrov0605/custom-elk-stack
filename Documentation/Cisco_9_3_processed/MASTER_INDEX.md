# Cisco Nexus 9.3.X Documentation - Master Index

**Generated:** 2026-02-06  
**Total Files:** 136+ processed documents  
**Total Commands:** ~7,000 (configuration + show)  
**Source:** Documentation/Cisco_9_3/ (196 raw HTML files)

---

## Quick Navigation

| Topic | Location | Files |
|-------|----------|-------|
| [Release Notes](#release-notes) | Agent1_Release_Fundamentals/ | 8 |
| [Fundamentals](#fundamentals) | Agent1_Release_Fundamentals/ | 3 |
| [Configuration Guides](#configuration-guides) | Agent2_Config_Guides/ | 54 |
| [Command Reference](#command-reference) | Agent3_Command_Reference/ | 58 |
| [Programmability](#programmability) | Agent4_Prog_Upgrade_Misc/programmability/ | 2 |
| [Upgrade/Downgrade](#upgrade) | Agent4_Prog_Upgrade_Misc/upgrade/ | 1 |
| [Troubleshooting](#troubleshooting) | Agent4_Prog_Upgrade_Misc/troubleshooting/ | 1 |
| [Miscellaneous](#miscellaneous) | Agent4_Prog_Upgrade_Misc/misc/ | 9 |

---

## Release Notes

**Location:** `Agent1_Release_Fundamentals/`

| Version | File | Size | Coverage |
|---------|------|------|----------|
| 9.3(1) | `release_notes_9.3_1.md` | 7.1 KB | Initial release |
| 9.3(3) | `release_notes_9.3_3.md` | 76.4 KB | Features, caveats |
| 9.3(9) | `release_notes_9.3_9.md` | 62.9 KB | Features, caveats |
| 9.3(16) | `release_notes_9.3_16.md` | 13.7 KB | Security fixes only |
| 9.3(8) | `epld_release_notes_9.3.8.md` | 15.6 KB | EPLD updates |

**Use for:** Version comparisons, feature availability, known issues, bug fixes

---

## Fundamentals

**Location:** `Agent1_Release_Fundamentals/`

| File | Coverage |
|------|----------|
| `fundamentals_configuration_guide.md` | NX-OS basics, architecture |
| `fundamentals_configuration_guide_alt.md` | Alt version (check differences) |
| `fundamentals_preface.md` | Getting started, document structure |

**Use for:** New to Nexus 9000, basic configuration workflow

---

## Configuration Guides

**Location:** `Agent2_Config_Guides/` (organized by topic)

### Interfaces
**Path:** `Agent2_Config_Guides/interfaces/`  
**Files:** 21  
**Coverage:** Ethernet, port-channels, vPC, Layer 2/3 interfaces, BFD, NAT

Key files:
- Ethernet interfaces
- Port-channel configuration
- Virtual Port Channels (vPC)
- Layer 3 interfaces
- Bidirectional Forwarding Detection (BFD)
- Network Address Translation (NAT)

### Layer 2 Switching
**Path:** `Agent2_Config_Guides/layer2/`  
**Files:** 18  
**Coverage:** VLANs, STP variants, VTP, private VLANs, Flex Links

Key topics:
- VLAN configuration
- Spanning Tree (STP/Rapid PVST+/MST)
- VLAN Trunking Protocol (VTP)
- Private VLANs
- Flex Links

### Security
**Path:** `Agent2_Config_Guides/security/`  
**Files:** 2  
**Coverage:** ACLs, AAA, SSH, TLS

### Quality of Service (QoS)
**Path:** `Agent2_Config_Guides/qos/`  
**Files:** 2  
**Coverage:** Marking, queuing, policing

### SAN Switching (FCoE)
**Path:** `Agent2_Config_Guides/san/`  
**Files:** 2  
**Coverage:** FCoE, VSAN, Fiber Channel

### VXLAN / Overlay
**Path:** `Agent2_Config_Guides/vxlan/`  
**Files:** 1  
**Coverage:** VXLAN, EVPN, BGP, overlay networking

### Routing - Unicast
**Path:** `Agent2_Config_Guides/unicast-routing/`  
**Files:** 1  
**Coverage:** BGP, OSPF, EIGRP, static routes

### Routing - Multicast
**Path:** `Agent2_Config_Guides/multicast-routing/`  
**Files:** 1  
**Coverage:** PIM, IGMP, multicast configuration

### System Management
**Path:** `Agent2_Config_Guides/system-management/`  
**Files:** 1  
**Coverage:** Monitoring, logging, SNMP

### Other Config Guides
**Path:** `Agent2_Config_Guides/other/`  
**Files:** 3  
**Coverage:** Catena, iCAM, label switching

---

## Command Reference

**Location:** `Agent3_Command_Reference/`

**Summary Report:** `SUMMARY_REPORT.md`

### Configuration Commands
**Path:** `Agent3_Command_Reference/Config_Commands/`  
**Files:** 30 (organized alphabetically A-Z)  
**Total Commands:** ~4,806

Structure: Commands grouped by letter (A through X chapters)

**Use for:** CLI command syntax, parameters, configuration examples

### Show Commands
**Path:** `Agent3_Command_Reference/Show_Commands/`  
**Files:** 28 (organized alphabetically A-Z)  
**Total Commands:** ~2,182

Structure: Show commands grouped by letter

**Use for:** Verification, troubleshooting, monitoring commands

---

## Programmability

**Location:** `Agent4_Prog_Upgrade_Misc/programmability/`

| File | Coverage |
|------|----------|
| `programmability-guide-93x.md` | NX-API, REST, Python, automation basics |
| `websocket-subscription.md` | WebSocket-based telemetry subscription |

**Also see:**
- `misc/programmability-rfcs.md` - Supported RFCs

---

## Upgrade / Downgrade

**Location:** `Agent4_Prog_Upgrade_Misc/upgrade/`

| File | Coverage |
|------|----------|
| `upgrade-downgrade-guide-93x.md` | Software upgrade/downgrade procedures |

---

## Troubleshooting

**Location:** `Agent4_Prog_Upgrade_Misc/troubleshooting/`

| File | Coverage |
|------|----------|
| `troubleshooting-guide-93x.md` | General troubleshooting methodology |
| `misc/nexus-9000v-troubleshooting.md` | 9000v virtual switch specific |

---

## Miscellaneous

**Location:** `Agent4_Prog_Upgrade_Misc/misc/`

| File | Coverage | Tags |
|------|----------|------|
| `icam-configuration-guide-93x.md` | iCAM telemetry | telemetry, streaming |
| `catena-configuration-guide-93x.md` | Service chaining | catena, services |
| `label-switching-configuration-guide-93x.md` | MPLS/Label Switching | mpls, segment-routing |
| `verified-scalability-guide-931.md` | Scale limits, capacity | scale, limits |
| `itd-configuration-guide-93x.md` | Intelligent Traffic Director | itd, load-balancing |
| `programmability-rfcs.md` | Supported RFCs | rfc, standards |
| `unidirectional-ethernet.md` | UDLD configuration | udld, ethernet |
| `nexus-9000v-deployment.md` | Virtual switch deployment | 9000v, virtualization |
| `nexus-9000v-troubleshooting.md` | Virtual switch issues | 9000v, troubleshooting |

---

## Search Tags Reference

Common tags used across documentation:

| Tag | Topics |
|-----|--------|
| interfaces | Ethernet, port-channel, vPC, physical layer |
| layer2 | VLANs, STP, spanning-tree, switching |
| routing | BGP, OSPF, EIGRP, static, unicast |
| vxlan | Overlay, EVPN, VTEP |
| security | ACL, AAA, SSH, TLS, RADIUS, TACACS |
| qos | Quality of Service, marking, queuing |
| san | FCoE, VSAN, fiber channel, storage |
| programmability | NX-API, REST, Python, automation |
| telemetry | ICAM, streaming, monitoring |
| monitoring | SNMP, logging, system management |

---

## How to Use This Library

### For Quick Questions
1. Check MASTER_INDEX (this file) for topic location
2. Navigate to relevant Agent folder
3. Check `index.json` for specific file mappings
4. Read the relevant .md file

### For Command Lookup
1. Go to `Agent3_Command_Reference/`
2. Check SUMMARY_REPORT.md for command counts
3. Navigate to Config_Commands/ or Show_Commands/
4. Find by first letter of command
5. Search within file for specific command

### For Configuration Examples
1. Identify topic (interfaces, routing, security, etc.)
2. Go to `Agent2_Config_Guides/[topic]/`
3. Find relevant chapter or guide
4. Look for configuration examples in code blocks

### For Troubleshooting
1. Check `troubleshooting-guide-93x.md` for methodology
2. Use command reference to find show commands
3. Check release notes for known issues

---

## File Count Summary

| Agent | Category | Files |
|-------|----------|-------|
| Agent1 | Release Notes + Fundamentals | 11 |
| Agent2 | Configuration Guides | 54 |
| Agent3 | Command Reference | 58 |
| Agent4 | Prog/Upgrade/Misc | 13 |
| **Total** | | **136+** |

---

## Notes

- All files are Markdown format (.md)
- Source attribution included in each file (`**Source:** filename`)
- Tags included for keyword search
- HTML cruft removed (scripts, navigation, headers)
- Command syntax preserved exactly in code blocks
- Original HTML preserved in `../Cisco_9_3/` (not modified)
