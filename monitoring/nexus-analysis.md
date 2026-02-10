# Cisco Nexus Switch Analysis for ELK Monitoring Dashboard

**Analysis Date:** 2026-02-09 20:51 GMT+2  
**Analyst:** OpenClaw Automation  
**Scope:** READ-ONLY analysis of NEXUS1 (10.4.4.3) and NEXUS2 (10.4.4.4)

---

## 1. Executive Summary

| Metric | NEXUS1 | NEXUS2 |
|--------|--------|--------|
| **Hostname** | B-IX_Switch1 | B-IX_Switch2 |
| **IP Address** | 10.4.4.3 | 10.4.4.4 |
| **NX-OS Version** | 9.3(12) | 9.3(12) |
| **Uptime** | 444d 20h 14m | 444d 20h 15m |
| **vPC Role** | Primary | Secondary |
| **Environment** | ✅ Healthy | ✅ Healthy |

### 🔴 Critical Issues Found
1. **Po111 (1-IX) DOWN on NEXUS2** - Port-channel is UP on NEXUS1 but DOWN on NEXUS2
   - Status: `down*` (No operational members)
   - Impact: Potential asymmetric traffic flow for 1-IX peering (100G)
   
### 🟡 Warning Issues
1. **Type-2 vPC Consistency Check FAILED on both switches**
   - Reason: SVI type-2 configuration incompatible
   - Impact: Cosmetic - peer-gateway and L3 routing still functional
   - vPC peer-link is UP and forwarding

2. **Buffer Threshold Exceeded (NEXUS2)**
   - Multiple `TAHUSD-SLOT1-4-BUFFER_THRESHOLD_EXCEEDED` alerts
   - 90% pool-group buffer threshold exceeded
   - Module 1 Instance 0 and 1 affected

3. **VLAN Suspension Events (NEXUS2)**
   - VLAN 1379 suspended on Po599 due to "Vlan is not configured on remote vPC interface"
   - Auto-recovered but indicates vPC config drift

---

## 2. Alarm Status

### Environmental Alarms
| Component | NEXUS1 Status | NEXUS2 Status |
|-----------|---------------|---------------|
| **Fans** | ✅ 4x NXA-FAN-30CFM-B OK | ✅ 4x NXA-FAN-30CFM-B OK |
| **Power Supply 1** | ✅ 650W OK (79W output) | ✅ 650W OK (80W output) |
| **Power Supply 2** | ✅ 650W OK (83W output) | ✅ 650W OK (81W output) |
| **Redundancy Mode** | PS-Redundant | PS-Redundant |
| **Front Temp** | ✅ 26°C (thresh: 70°C) | ✅ 26°C (thresh: 70°C) |
| **Back Temp** | ✅ 30°C (thresh: 80°C) | ✅ 28°C (thresh: 80°C) |
| **CPU Temp** | ✅ 42°C (thresh: 90°C) | ✅ 43°C (thresh: 90°C) |
| **Sugarbowl Temp** | ✅ 53°C (thresh: 100°C) | ✅ 52°C (thresh: 100°C) |

### vPC Status
| Parameter | NEXUS1 | NEXUS2 |
|-----------|--------|--------|
| **Peer Status** | ✅ peer adjacency formed ok | ✅ peer adjacency formed ok |
| **Keep-alive** | ✅ peer is alive | ✅ peer is alive |
| **Config Consistency** | ✅ success | ✅ success |
| **Per-VLAN Consistency** | ✅ success | ✅ success |
| **Type-2 Consistency** | ⚠️ failed | ⚠️ failed |
| **Peer-link (Po200)** | ✅ UP | ✅ UP |

---

## 3. Port Health Analysis

### Down/Suspended Ports

#### NEXUS1
| Port | Status | Reason |
|------|--------|--------|
| Eth1/6 | xcvrAbsen | No transceiver (empty slot) |
| Eth1/13 | xcvrAbsen | No transceiver |
| Eth1/14 | xcvrAbsen | No transceiver |
| Eth1/18-24 | xcvrAbsen | No transceivers (expected) |
| Eth1/27-46 | xcvrAbsen | No transceivers (expected) |
| Vlan1 | down | Administratively down |
| Vlan1420 | down | Administratively down |

#### NEXUS2
| Port | Status | Reason |
|------|--------|--------|
| Eth1/6 | xcvrAbsen | No transceiver |
| Eth1/14 | xcvrAbsen | No transceiver |
| Eth1/15 | xcvrAbsen | No transceiver |
| Eth1/18-24 | xcvrAbsen | No transceivers |
| Eth1/27-32 | xcvrAbsen | No transceivers |
| **Eth1/33** | **⚠️ disabled** | Administratively down |
| Eth1/35-46 | xcvrAbsen | No transceivers |
| Eth1/51,53-54 | xcvrAbsen | No transceivers |
| Vlan1 | down | Administratively down |

### Critical Port Issues

| Switch | Port/Port-Channel | Issue | Severity |
|--------|-------------------|-------|----------|
| NEXUS2 | **Po111** | **DOWN - No operational members** | 🔴 CRITICAL |
| NEXUS2 | Eth1/15 | Novelcomm - XCVR absent but port expecting trunk | 🟡 WARNING |
| NEXUS2 | Eth1/33 | SFP-don't-show-rig - Admin disabled | 🟡 WARNING |
| NEXUS2 | Eth1/34 | INALAN - Recently flapped (config changes) | 🟡 INFO |

---

## 4. Port Channel Status

### NEXUS1 Port-Channels
| Port-Channel | Status | Members | Speed | Connected To |
|--------------|--------|---------|-------|--------------|
| Po4 | ✅ U | Eth1/17 | 1G | B-IX-RS-BG2 |
| Po6 | ✅ U | Eth1/1-4 | 10G | SOX-80G |
| Po10 | ✅ U | Eth1/5 | 10G | Google-20G |
| Po31 | ✅ U | Eth1/25-26 | 10G | Telepoint |
| Po62 | ✅ U | Eth1/7-8 | 10G | RETN |
| Po71 | ✅ U | Eth1/9 | 10G | TelecomArmenia |
| **Po111** | ✅ **U** | **Eth1/51** | **100G** | **1-IX** |
| Po200 | ✅ U | Eth1/47-48 | 25G | VPC Peer-Link |
| Po599 | ✅ U | Eth1/49 | 100G | TH-DS5/6-VPC |
| Po871 | ✅ U | Eth1/10 | 10G | A1BG_AS8717 |
| Po902 | ✅ U | Eth1/20-22 | 10G | TH-SOF-DS1/2 |

### NEXUS2 Port-Channels
| Port-Channel | Status | Members | Speed | Connected To |
|--------------|--------|---------|-------|--------------|
| Po4 | ✅ U | Eth1/17 | 1G | B-IX-RS-BG2 |
| Po6 | ✅ U | Eth1/1-4 | 10G | SOX-80G |
| Po10 | ✅ U | Eth1/5 | 10G | TurkIX |
| Po31 | ✅ U | Eth1/25-26 | 10G | Telepoint |
| Po62 | ✅ U | Eth1/7-8 | 10G | RETN |
| Po71 | ✅ U | Eth1/9 | 10G | TelecomArmenia |
| **Po111** | 🔴 **D** | **--** | **auto** | **1-IX (DOWN)** |
| Po200 | ✅ U | Eth1/47-48 | 25G | VPC Peer-Link |
| Po599 | ✅ U | Eth1/49 | 100G | TH-DS6 |
| Po871 | ✅ U | Eth1/10 | 10G | A1BG_AS8717 |
| Po902 | ✅ U | Eth1/20-22 | 10G | TH-SOF-DS1/2 |

### Summary
- **Total vPCs:** 10 configured on both switches
- **Healthy vPCs:** 9 (all UP on NEXUS1, Po111 DOWN on NEXUS2)
- **Degraded vPCs:** 1 (Po111 - asymmetric state)

---

## 5. ELK Monitoring Targets

### Interfaces to Monitor in ELK Dashboard

#### 🔴 CRITICAL - Immediate Attention Required

1. **NEXUS2: Po111 (1-IX)** - **DOWN/DEGRADED**
   - **Reason:** Port-channel DOWN on secondary, UP on primary
   - **Impact:** Potential 100G peering traffic issues for 1-IX
   - **Action:** Check physical cable (Eth1/51) and LACP configuration

2. **NEXUS2: Eth1/51** (member of Po111)
   - **Reason:** XCVR absent - Po111 has no operational members
   - **Impact:** 1-IX 100G peering unavailable on NEXUS2
   - **Action:** Verify transceiver installation

#### 🟡 HIGH PRIORITY - vPC Interconnects & Peer Links

3. **Po200** (vPC Peer-Link) - Both Switches
   - **Members:** Eth1/47, Eth1/48 (25G each = 50G aggregate)
   - **Status:** UP on both
   - **Monitor:** Bandwidth utilization, errors, LACP flaps
   - **Criticality:** vPC fabric depends on this link

4. **Po599** (TH-DS5/6-VPC) - Both Switches
   - **Members:** Eth1/49 (100G)
   - **Status:** UP
   - **Monitor:** Buffer threshold alerts, VLAN suspension events
   - **Note:** VLAN 1379 suspension events observed (NEXUS2)
   - **Criticality:** 100G spine interconnect

#### 🟢 PEERING LINKS - Monitor for Traffic & Errors

5. **Po6 (SOX-80G)** - Both Switches
   - **Members:** Eth1/1-4 (4x10G)
   - **Connected To:** SOX peering
   - **Status:** UP
   - **Monitor:** Traffic volume, LACP member status

6. **Po10** - Google/TurkIX Peering
   - NEXUS1: Eth1/5 (Google-20G)
   - NEXUS2: Eth1/5 (TurkIX)
   - **Status:** UP
   - **Note:** Different peers on each switch (expected design)

7. **Po62 (RETN)** - Both Switches
   - NEXUS1: Eth1/7-8 (RETN-1, RETN-2)
   - NEXUS2: Eth1/7-8 (RETN-3, RETN_Cross-Connect)
   - **Status:** UP

8. **Po71 (TelecomArmenia)** - Both Switches
   - **Members:** Eth1/9
   - **Status:** UP

9. **Po871 (A1BG_AS8717)** - Both Switches
   - **Members:** Eth1/10
   - **Status:** UP

10. **Po902 (TH-SOF-DS1/2)** - Both Switches
    - **Members:** Eth1/20-22 (3x10G)
    - **Status:** UP

#### 🟢 MANAGEMENT INTERFACES

11. **mgmt0** - Both Switches
    - NEXUS1: 172.16.4.2
    - NEXUS2: 172.16.4.1
    - **Status:** UP
    - **Monitor:** ICMP reachability, SSH access logs

#### 🟠 BACKPLANE/SYSTEM INTERFACES

12. **Po4 (B-IX-RS-BG2)** - Both Switches
    - **Members:** Eth1/17 (1G copper)
    - **Status:** UP
    - **Monitor:** Out-of-band management traffic

13. **Po31 (Telepoint)** - Both Switches
    - **Members:** Eth1/25-26
    - **Status:** UP

#### 🔴 INTERFACES WITH ERRORS TO MONITOR

14. **Eth1/34 (INALAN)** - NEXUS2 ONLY
    - **Status:** UP but recently flapped
    - **Events:** Multiple config change events, speed/duplex changes
    - **Action:** Monitor for interface resets and flaps

15. **VLAN Interfaces (SVI)** - Both Switches
    - Vlan4: UP (Peering VLAN - B-IX_BG-peering on NEXUS1)
    - Vlan6: UP (Inband MGMT)
    - Monitor: ICMP reachability, routing protocol adjacencies

---

## Appendix: Raw Command Output

### NEXUS1 (10.4.4.3) Full Output

<details>
<summary>Click to expand NEXUS1 raw data</summary>

```
=== show interface status ===
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
mgmt0         --                 connected routed    full    1000    --         
Eth1/1        SOX_1of8_Po6       connected trunk     full    10G     10Gbase-LR 
Eth1/2        SOX_1of8_Po6       connected trunk     full    10G     10Gbase-LR 
Eth1/3        SOX_1of8_Po6       connected trunk     full    10G     10Gbase-LR 
Eth1/4        SOX_1of8_Po6       connected trunk     full    10G     10Gbase-LR 
Eth1/5        Google-20G         connected trunk     full    10G     10Gbase-LR 
Eth1/6        --                 xcvrAbsen routed    auto    auto    --         
Eth1/7        RETN-1             connected trunk     full    10G     10Gbase-LR 
Eth1/8        RETN-2             connected trunk     full    10G     10Gbase-LR 
Eth1/9        TelecomArmenia-1   connected trunk     full    10G     10Gbase-LR 
Eth1/10       A1BG-1             connected trunk     full    10G     10Gbase-ER 
Eth1/11       Digsys-1G-CWDM     connected trunk     full    10G     10Gbase-LR 
Eth1/12       SBB-10G            connected trunk     full    10G     10Gbase-LR 
Eth1/13       --                 xcvrAbsen routed    auto    auto    --         
Eth1/14       Shuteted DOWN      xcvrAbsen routed    auto    auto    --         
Eth1/15       TH-MulticastTV-COR connected trunk     full    10G     10Gbase-SR 
Eth1/16       SpeedyNet-10G      connected trunk     full    10G     10Gbase-LR 
Eth1/17       --                 connected trunk     full    1000    1000base-T 
Eth1/18-24    --                 xcvrAbsen routed    auto    auto    --         
Eth1/25-26    Telepoint          connected trunk     full    10G     10Gbase-SR
Eth1/27-46    --                 xcvrAbsen routed    auto    auto    --         
Eth1/47-48    TP1-B-IX-VPC1/2-Pe connected trunk     full    25G     SFP-H25GB-SR
Eth1/49       TH-DS5-Eth1/56     connected trunk     full    100G    QSFP-100G-LR4
Eth1/50       --                 xcvrAbsen routed    auto    auto    --         
Eth1/51       1-IX               connected trunk     full    100G    QSFP-100G-CWDM4
Eth1/52       Lankom-Exchange    connected trunk     full    100G    QSFP-100G-LR4
Eth1/53       BalkanGate/B-IX-Th connected trunk     full    100G    QSFP-100G-LR4
Eth1/54       Vivacom            connected 4         full    100G    QSFP-100G-LR4
Po4           B-IX-RS-BG2        connected trunk     full    1000    --         
Po6           SOX-80G            connected trunk     full    10G     --         
Po10          Google-20G         connected trunk     full    10G     --         
Po31          Telepoint          connected trunk     full    10G     --         
Po62          RETN               connected trunk     full    10G     --         
Po71          TelecomArmenia     connected trunk     full    10G     --         
Po111         1-IX               connected trunk     full    100G    --         
Po200         TP1-B-IX-VPC1/2-Pe connected trunk     full    25G     --         
Po599         TH-DS5/6-VPCtoVPC  connected trunk     full    100G    --         
Po871         A1BG_AS8717        connected trunk     full    10G     --         
Po902         TH-SOF-DS1/2-VPCto connected trunk     full    10G     --         

=== show version (summary) ===
NXOS: version 9.3(12)
Device: cisco Nexus9000 C93180YC-EX
Kernel uptime: 444 day(s), 20 hour(s), 14 minute(s)
```
</details>

### NEXUS2 (10.4.4.4) Full Output

<details>
<summary>Click to expand NEXUS2 raw data</summary>

```
=== show interface status ===
Port          Name               Status    Vlan      Duplex  Speed   Type
--------------------------------------------------------------------------------
mgmt0         --                 connected routed    full    1000    --         
Eth1/1-4      SOX_1of8_Po6       connected trunk     full    10G     10Gbase-LR 
Eth1/5        TurkIX             connected trunk     full    10G     10Gbase-LR 
Eth1/6        --                 xcvrAbsen routed    auto    auto    --         
Eth1/7        RETN-3             connected trunk     full    10G     10Gbase-LR 
Eth1/8        RETN_Cross-Connect connected trunk     full    10G     10Gbase-LR 
Eth1/9        TelecomArmenia-2   connected trunk     full    10G     10Gbase-LR 
Eth1/10       A1BG-2             connected trunk     full    10G     10Gbase-ER 
Eth1/11       Bulgartel          connected trunk     full    10G     10Gbase-LR 
Eth1/12       GCN                connected trunk     full    10G     10Gbase-LR 
Eth1/13       Speedy-Net-TV-NEW- connected trunk     full    10G     SFP-10G-BXU-I
Eth1/14       --                 xcvrAbsen routed    auto    auto    --         
Eth1/15       Novelcomm          xcvrAbsen trunk     auto    auto    --         
Eth1/16       Bulsatcom          connected 4         full    10G     10Gbase-ER 
Eth1/17       --                 connected trunk     full    1000    1000base-T 
Eth1/18-24    --                 xcvrAbsen routed    auto    auto    --         
Eth1/25-26    Telepoint          connected trunk     full    10G     10Gbase-LR
Eth1/27-32    --                 xcvrAbsen routed    auto    auto    --         
Eth1/33       SFP-don't-show-rig disabled  routed    auto    auto    10Gbase-LR 
Eth1/34       INALAN             connected trunk     full    10G     10Gbase-LR 
Eth1/35-46    --                 xcvrAbsen routed    auto    auto    --         
Eth1/47-48    TP1-B-IX-VPC1/2-Pe connected trunk     full    25G     SFP-H25GB-SR
Eth1/49       TH-DS6-Eth1/56     connected trunk     full    100G    QSFP-100G-LR4
Eth1/50       Turk-IX            connected trunk     full    100G    QSFP-100G-LR4
Eth1/51       --                 xcvrAbsen routed    auto    auto    --         
Eth1/52       GNM                connected trunk     full    100G    QSFP-100G-LR4
Eth1/53-54    --                 xcvrAbsen routed    auto    auto    --         
Po4           B-IX-RS-BG2        connected trunk     full    1000    --         
Po6           SOX-80G            connected trunk     full    10G     --         
Po10          Google-20G         connected trunk     full    10G     --         
Po31          Telepoint          connected trunk     full    10G     --         
Po62          RETN               connected trunk     full    10G     --         
Po71          TelecomArmenia     connected trunk     full    10G     --         
Po111         1-IX               noOperMem trunk     auto    auto    --         
Po200         TP1-B-IX-VPC1/2-Pe connected trunk     full    25G     --         
Po599         --                 connected trunk     full    100G    --         
Po871         A1BG_AS8717        connected trunk     full    10G     --         
Po902         TH-SOF-DS1/2-VPCto connected trunk     full    10G     --         

=== show vpc brief (Critical Section) ===
vPC domain id                     : 200 
Peer status                       : peer adjacency formed ok      
vPC keep-alive status             : peer is alive                 
Configuration consistency status  : success 
Type-2 consistency status         : failed  
Type-2 inconsistency reason       : SVI type-2 configuration incompatible
vPC role                          : secondary                     
Number of vPCs configured         : 10  

vPC Peer-link status
---------------------------------------------------------------------
id    Port   Status Active vlans    
--    ----   ------ -------------------------------------------------
1     Po200  up     1,4,6,35,124,185,200-205,208,212,225,242-243,...

vPC status
---------------------------------------------------------------------------
Id    Port          Status Consistency Reason                Active vlans
--    ------------  ------ ----------- ------                ---------------
4     Po4           up     success     success               4,6         
6     Po6           up     success     success               4           
10    Po10          up     success     success               4           
31    Po31          up     success     success               4,201       
62    Po62          up     success     success               124,200-204...
71    Po71          up     success     success               4           
**111**   **Po111**   **down***  **Not**     **Consistency Check Not** **-**
599   Po599         up     success     success               4,6,450,888...
871   Po871         up     success     success               4           
902   Po902         up     success     success               124,203-205...

=== show version (summary) ===
NXOS: version 9.3(12)
Device: cisco Nexus9000 C93180YC-EX
Kernel uptime: 444 day(s), 20 hour(s), 15 minute(s)
```
</details>

---

## Recommendations

### Immediate Actions Required
1. **Investigate Po111 on NEXUS2** - Check why Eth1/51 has no transceiver while NEXUS1 Eth1/51 has QSFP-100G-CWDM4
2. **Review 1-IX peering configuration** - Ensure both switches have matching transceivers

### Monitoring Configuration Priority
1. **HIGH:** Po111 (1-IX), Po200 (vPC Peer-Link), Po599 (TH-DS5/6)
2. **MEDIUM:** All peering port-channels (Po6, Po10, Po62, Po71, Po871, Po902)
3. **LOW:** Management interfaces, unused ports for capacity planning

### Long-term Health Checks
1. Monitor buffer utilization trends (NEXUS2 showing 90% threshold exceeded)
2. Track vPC consistency check status (Type-2 failures may mask real issues)
3. Review authentication failure patterns (10.4.4.52 repeated failures)

---
*Generated by OpenClaw Network Analysis Tool*
