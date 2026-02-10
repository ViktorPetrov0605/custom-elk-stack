# Chapter: F Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_0110.html
**Type:** Configuration Commands  
**Chapter:** Group-110 Commands  
**Total Commands:** 214

## Command List

- `fabric-soo`
- `fabric database auto-pull dci node-id`
- `fabric database auto-pull dci vrf node-id`
- `fabric database auto-pull vni interface`
- `fabric database inherit-profile-map`
- `fabric database mobility-domain`
- `fabric database override-profile`
- `fabric database override-vrf-profile`
- `fabric database profile-map`
- `fabric database profile-map global`
- `fabric database refresh dot1q`
- `fabric database refresh vni`
- `fabric database static-host`
- `fabric database timer`
- `fabric database type bl-dci`
- `fabric database type cabling`
- `fabric database type host`
- `fabric database type network`
- `fabric database type partition`
- `fabric database type profile`
- `fabric forwarding admin-distance`
- `fabric forwarding anycast-gateway-mac`
- `fabric forwarding dup-host-ip-addr-detection`
- `fabric forwarding dup-host-recovery-timer recover-count`
- `fabric forwarding limit-vlan-mac`
- `fabric forwarding mode anycast-gateway`
- `fabric forwarding selective-host-probe`
- `fabric multicast event-history bgp`
- `fabric multicast event-history ha`
- `fabric multicast event-history hmm`
- `fabric multicast event-history isis`
- `fabric multicast event-history l2rib`
- `fabric multicast event-history m2rib`
- `fabric multicast event-history m6rib`
- `fabric multicast event-history mrib`
- `fabric multicast event-history pim`
- `fabric multicast event-history pim6`
- `failaction`
- `failaction`
- `fast-convergence`
- `fast-convergence`
- `fast-external-fallover`
- `fast-flood enable`
- `fast-flood enable`
- `fast-flood enable`
- `fast-flood interval`
- `fast-flood interval`
- `fast-flood interval`
- `fast-reload`
- `fast-reload network-os`
- `fast-reroute`
- `fast-reroute backup-prot-preempt optimize-bw`
- `fcdroplatency network`
- `fcoe`
- `fcoe`
- `fcoe enable-fex`
- `fcoe fcf-priority`
- `fcoe fcmap`
- `fcoe fka-adv-period`
- `fcoe veloopback`
- `fcoe vsan`
- `fctimer D_S_TOV`
- `fctimer E_D_TOV`
- `fctimer R_A_TOV`
- `fctimer abort`
- `fctimer commit`
- `fctimer distribute`
- `feature-set`
- `feature-set`
- `feature`
- `feature analytics`
- `feature bash-shell`
- `feature bfd`
- `feature bgp`
- `feature catena`
- `feature container-tracker`
- `feature dhcp`
- `feature dot1x`
- `feature eigrp`
- `feature evb`
- `feature evmed`
- `feature fabric forwarding`
- `feature flexlink`
- `feature grpc`
- `feature hardware-telemetry`
- `feature hsrp`
- `feature icam`
- `feature imp`
- `feature interface-vlan`
- `feature isis`
- `feature itd`
- `feature lacp`
- `feature ldap`
- `feature lldp`
- `feature macsec`
- `feature mpls evpn`
- `feature mpls l3vpn`
- `feature mpls ldp`
- `feature mpls oam`
- `feature mpls segment-routing`
- `feature mpls segment-routing traffic-engineering`
- `feature mpls static`
- `feature mpls traffic-engineering`
- `feature msdp`
- `feature mvpn`
- `feature nat`
- `feature nbm`
- `feature netconf`
- `feature netflow`
- `feature ngmvpn`
- `feature ngoam`
- `feature ngoam`
- `feature npiv`
- `feature ntp`
- `feature nv overlay`
- `feature nxapi`
- `feature nxdb`
- `feature nxsdk`
- `feature openflow`
- `feature ospf`
- `feature ospfv3`
- `feature password encryption aes`
- `feature pbr`
- `feature pim`
- `feature pim6`
- `feature plb`
- `feature pnp`
- `feature poap`
- `feature poe`
- `feature pong`
- `feature port-security`
- `feature private-vlan`
- `feature privilege`
- `feature ptp`
- `feature restconf`
- `feature rip`
- `feature scheduler`
- `feature scp-server`
- `feature sflow`
- `feature sftp-server`
- `feature signature-verification`
- `feature sla responder`
- `feature sla sender`
- `feature sla twamp-server`
- `feature smart-channel`
- `feature srv6`
- `feature ssh`
- `feature tacacs`
- `feature telemetry`
- `feature telnet`
- `feature tunnel`
- `feature udld`
- `feature vmtracker`
- `feature vn-segment-vlan-based`
- `feature vpc`
- `feature vrrp`
- `feature vrrpv3`
- `feature vtp`
- `fec`
- `fec`
- `fec`
- `fhrp delay minimum`
- `fhrp delay reload`
- `filter`
- `filter`
- `filter access-group`
- `filter ip`
- `filter ipv6 access-group`
- `filter out`
- `filter tx control-packets`
- `filter vlan`
- `filter vlan include-untagged`
- `find`
- `fips debug errors debug`
- `fips mode enable`
- `flow-count`
- `flow-count`
- `flow exporter`
- `flow exporter`
- `flow filter`
- `flow forward`
- `flow monitor`
- `flow monitor`
- `flow profile`
- `flow record`
- `flow record`
- `flow rtp timeout`
- `flow system config`
- `flow timeout`
- `flowcontrol hardware`
- `flowcontrol receive`
- `flush-routes`
- `flush-routes`
- `flush-routes`
- `flush-routes`
- `flush-routes`
- `flush-routes`
- `follow`
- `format`
- `format bootflash`
- `format bootflash check-filesystem`
- `format usb1`
- `forward`
- `forwarding-adjacency`
- `fragments`
- `frequency`
- `from to`
- `from to`
- `fte event`
- `fte exporter`
- `fte monitor`
- `fte record`
- `fte system monitor`
- `ftrace`

---

## Detailed Command Reference

# Command: fabric-soo

## Syntax
```
[no] fabric-soo { <ext-comm-soo-aa2nn4> &#124; <ext-comm-soo-aa4nn2> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric-soo | Fabric Site of Origin |
| ext-comm-soo-aa4nn2 | VPN extcommunity in aa4:fabric_id format |
| ext-comm-soo-aa2nn4 | VPN extcommunity in aa:fabric_id format |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4135271148

---

# Command: fabric database auto-pull dci node-id

## Syntax
```
fabric database auto-pull dci node-id <mgmt-ip-address>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fabric | Fabric |
| database | Fabric Database |
| auto-pull | Pull configuration |
| dci | DCI profile |
| node-id | management ip address of this node |
| mgmt-ip-address | IP address in CIDR format |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1558311496

---

# Command: fabric database auto-pull dci vrf node-id

## Syntax
```
fabric database auto-pull dci vrf <vrf-name> node-id <mgmt-ip-address> [ peer-id <peer-ip-address> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fabric | Fabric |
| database | Fabric Database |
| auto-pull | Pull configuration |
| dci | DCI profile |
| vrf | Display per-VRF information |
| vrf-name | VRF name |
| node-id | management ip address of this node |
| mgmt-ip-address | IP address in CIDR format |
| peer-id | (Optional) management ip address of peer |
| peer-ip-address | (Optional) IP address in CIDR format |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, overlay, F-commands
**Command ID:** wp1671032228

---

# Command: fabric database auto-pull vni interface

## Syntax
```
fabric database auto-pull { vni <vni-id> &#124; dot1q <vlan-id> } interface <interface-id> [ { overwrite-vlan &#124; overwrite-bd }
 <ow-vlan-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fabric | Fabric |
| database | Fabric Database |
| auto-pull | Pull configuration |
| vni | Pull ethernet-tag vni configuration |
| dot1q | Pull ethernet-tag dot1q configuration |
| interface | Applied interface |
| interface-id | Name of interface |
| overwrite-vlan | (Optional) Overwrite the system generate vlan |
| overwrite-bd | (Optional) Overwrite the system generate bd |
| ow-vlan-id | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, overlay, F-commands
**Command ID:** wp3231867292

---

# Command: fabric database inherit-profile-map

## Syntax
```
{ fabric database inherit-profile-map <id> } &#124; { no fabric database inherit-profile-map }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| inherit-profile-map | Inherit a profile map. All non-global mappings will be inherited. |
| id | Profile Map ID |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-port-channel

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3862567883

---

# Command: fabric database mobility-domain

## Syntax
```
[no] fabric database mobility-domain <name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| mobility-domain | Tag to identify mobility domain name |
| name | Mobility Domain Name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3120948492

---

# Command: fabric database override-profile

## Syntax
```
[no] fabric database override-profile <profilename>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| override-profile | Override the network profile name |
| profilename | Enter the profile name to override network profile |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3581691418

---

# Command: fabric database override-vrf-profile

## Syntax
```
[no] fabric database override-vrf-profile <profilename>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| override-vrf-profile | Override the VRF (partition) profile name |
| profilename | Enter the profile name to override VRF profile |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, overlay, F-commands
**Command ID:** wp9517887380

---

# Command: fabric database profile-map

## Syntax
```
[no] fabric database profile-map <id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| profile-map | Configure a profile map |
| id | Profile Map ID |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1527558771

---

# Command: fabric database profile-map global

## Syntax
```
[no] fabric database profile-map global
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| profile-map | Configure a profile map |
| global | Global profile (apply to all interfaces) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2398577977

---

# Command: fabric database refresh dot1q

## Syntax
```
fabric database refresh dot1q <vlan-id> [ { mobility-domain <name> &#124; interface <interface-id> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fabric | Fabric |
| database | Fabric Database |
| refresh | Refresh profile configuration |
| dot1q | Dot1Q Encapsulation |
| interface | (Optional) Applied interface |
| interface-id | (Optional) Name of interface |
| mobility-domain | (Optional) Tag to identify mobility domain name |
| name | (Optional) Mobility Domain Name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2974479730

---

# Command: fabric database refresh vni

## Syntax
```
fabric database refresh { vni <vni-id> &#124; include-vrf { <vrf-name> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fabric | Fabric |
| database | Fabric Database |
| refresh | Refresh profile configuration |
| vni | Virtual Network Identifier |
| include-vrf | Include VRF name |
| vrf-name | VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, overlay, F-commands
**Command ID:** wp2885065179

---

# Command: fabric database static-host

## Syntax
```
[no] fabric database static-host
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Fabric Database |
| static-host | Configure a static host |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3069054126

---

# Command: fabric database timer

## Syntax
```
[no] fabric database timer { aging &#124; cleanup &#124; recovery &#124; re-add } <timeout>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| timer | HMM timers |
| cleanup | Delay in minutes before profile is deleted |
| recovery | Delay in minutes before recovered profile is deleted |
| re-add | Delay in minutes before new client requests (after un-apply) are accepted |
| aging | Delay in minutes before profile is checked for aging |
| timeout | Set timeout in minutes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2596944357

---

# Command: fabric database type bl-dci

## Syntax
```
[no] fabric database type bl-dci
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| bl-dci | Border Leaf - DCI |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1738936700

---

# Command: fabric database type cabling

## Syntax
```
[no] fabric database type cabling
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| cabling | Cable Management Database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1813372440

---

# Command: fabric database type host

## Syntax
```
[no] fabric database type host
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| host | Host Database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3750153120

---

# Command: fabric database type network

## Syntax
```
[no] fabric database type network
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| network | Network Database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1468539199

---

# Command: fabric database type partition

## Syntax
```
[no] fabric database type partition
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| partition | Partition Database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2479694616

---

# Command: fabric database type profile

## Syntax
```
[no] fabric database type profile
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| database | Configure Fabric Database |
| type | Configure database type |
| profile | Port or Switch Profile Database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1257999261

---

# Command: fabric forwarding admin-distance

## Syntax
```
{ fabric forwarding admin-distance <distance> } &#124; { no fabric forwarding admin-distance }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| admin-distance | Administrative distance for HMM host routes |
| distance | Set the administrative distance for HMM (default is 190) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1028144108

---

# Command: fabric forwarding anycast-gateway-mac

## Syntax
```
{ fabric forwarding anycast-gateway-mac <mac-addr> } &#124; { no fabric forwarding anycast-gateway-mac }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| anycast-gateway-mac | Anycast Gateway MAC of the Switch |
| mac-addr | MAC address |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1828739040

---

# Command: fabric forwarding dup-host-ip-addr-detection

## Syntax
```
{ fabric forwarding dup-host-ip-addr-detection <mmoves> <nsecs> &#124; no fabric forwarding dup-host-ip-addr-detection }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| dup-host-ip-addr-detection | To detect duplicate host address in n secs |
| mmoves | Set Number of host moves to be allowed in n secs. Default is 5 |
| nsecs | Set the duplicate detection timeout in secs for host moves. Default is 180 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, network, F-commands
**Command ID:** wp2308469285

---

# Command: fabric forwarding dup-host-recovery-timer recover-count

## Syntax
```
{ fabric forwarding dup-host-recovery-timer <timeout> recover-count <count> &#124; no fabric forwarding dup-host-recovery-timer
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| dup-host-recovery-timer | Refresh the frozen duplicate host |
| timeout | Set the timeout in secs to refresh the duplicate host. Default is 30 secs |
| recover-count | Maximum number of refreshes |
| count | Set the maximum number of host refresh. Default is 5. |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp3975338774

---

# Command: fabric forwarding limit-vlan-mac

## Syntax
```
[no] fabric forwarding limit-vlan-mac <max-limit>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| limit-vlan-mac | Maximum number of end-hosts allowed to have the same (vlan, MAC) mapping in a given vrf (Default is 2048) |
| max-limit | Set max-limit |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp8241295530

---

# Command: fabric forwarding mode anycast-gateway

## Syntax
```
{ fabric forwarding mode anycast-gateway } &#124; { no fabric forwarding mode }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| mode | Forwarding Modes |
| anycast-gateway | Anycast Gateway Forwarding Mode |

**Command Mode:** /exec/configure/if-vlan /exec/configure/if-vlan-range

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3853585763

---

# Command: fabric forwarding selective-host-probe

## Syntax
```
[no] fabric forwarding selective-host-probe
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| selective-host-probe | Trigger unconditional host probe |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3395855507

---

# Command: fabric multicast event-history bgp

## Syntax
```
[no] fabric multicast event-history bgp { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| bgp | BGP events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp1464973456

---

# Command: fabric multicast event-history ha

## Syntax
```
[no] fabric multicast event-history ha { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| ha | ha events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1391152043

---

# Command: fabric multicast event-history hmm

## Syntax
```
[no] fabric multicast event-history hmm { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| hmm | HMM events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1060796220

---

# Command: fabric multicast event-history isis

## Syntax
```
[no] fabric multicast event-history isis { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| isis | ISIS events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp1571667337

---

# Command: fabric multicast event-history l2rib

## Syntax
```
[no] fabric multicast event-history l2rib { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| l2rib | l2rib events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3314660793

---

# Command: fabric multicast event-history m2rib

## Syntax
```
[no] fabric multicast event-history m2rib { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| m2rib | M2RIB events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2954714203

---

# Command: fabric multicast event-history m6rib

## Syntax
```
[no] fabric multicast event-history m6rib { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| m6rib | M6RIB events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3988867224

---

# Command: fabric multicast event-history mrib

## Syntax
```
[no] fabric multicast event-history mrib { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| mrib | MRIB events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4263092857

---

# Command: fabric multicast event-history pim

## Syntax
```
[no] fabric multicast event-history pim { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| pim | PIM events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3683984174

---

# Command: fabric multicast event-history pim6

## Syntax
```
[no] fabric multicast event-history pim6 { size { <size_in_text> &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fabric | Fabric |
| multicast | Configure multicast |
| event-history | Configure event-history buffer |
| pim6 | PIM6 events for fabric multicast |
| size | Configure size |
| size_in_text | Buffer size |
| size_in_kbytes | Size in kbytes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2571881078

---

# Command: failaction

## Syntax
```
[no] failaction { { node { reassign &#124; drop &#124; least-bucket &#124; per-bucket } } &#124; { bucket { distribute } } &#124; { cluster drop }
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| failaction | ITD failaction |
| node | ITD failaction node |
| reassign | ITD failaction reassign |
| drop | ITD failaction drop |
| least-bucket | ITD failaction least-bucket node |
| per-bucket | ITD failaction per-bucket node |
| bucket | ITD failaction bucket reassign |
| distribute | ITD failaction distribute reassign |
| cluster | ITD failaction cluster |

**Command Mode:** /exec/configure/itd

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2771371915

---

# Command: failaction

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| failaction | Configure failaction for PLB service |
| node | PLB failaction node |
| reassign | PLB failaction reassign |
| drop | PLB failaction drop |
| cluster | PLB failaction cluster |

**Command Mode:** /exec/configure/plb

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2383614186

---

# Command: fast-convergence

## Syntax
```
[no] fast-convergence
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-convergence | Configure vPC fast convergence |

**Command Mode:** /exec/configure/vpc-domain

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4231877440

---

# Command: fast-convergence

## Syntax
```
fast-convergence &#124; no fast-convergence
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fast-convergence | Enable vPC fast-convergence |

**Command Mode:** /exec/configure/vpc-domain

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4183392306

---

# Command: fast-external-fallover

## Syntax
```
[no] fast-external-fallover
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-external-fallover | Immediately reset the session if the link to a directly connected BGP peer goes down |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3214088203

---

# Command: fast-flood enable

## Syntax
```
[no] fast-flood enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| enable | Turn on fast-flooding |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2898671880

---

# Command: fast-flood enable

## Syntax
```
[no] fast-flood enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| enable | Turn on fast-flooding |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp5422658900

---

# Command: fast-flood enable

## Syntax
```
[no] fast-flood enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| enable | Turn on fast-flooding |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4262983841

---

# Command: fast-flood interval

## Syntax
```
[no] fast-flood interval <interval>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| interval | Duration/interval of the fast-flood timer. |
| interval | Specify the value (ms) |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp8910108780

---

# Command: fast-flood interval

## Syntax
```
[no] fast-flood interval <interval>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| interval | Duration/interval of the fast-flood timer. |
| interval | Specify the value (ms) |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3128790447

---

# Command: fast-flood interval

## Syntax
```
[no] fast-flood interval <interval>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-flood | Fast flood the LSP's |
| interval | Duration/interval of the fast-flood timer. |
| interval | Specify the value (ms) |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1473057074

---

# Command: fast-reload

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fast-reload | fast-reload software |
| nxos | (Optional) boot-variable name |
| uri | (Optional) Enter image uri |
| non-interruptive | (Optional) Non-Interruptive image upgrade |
| nosrg | (Optional) nosrg |
| override | (Optional) Do fast-reload without impact check |
| trigger-gr | (Optional) Enable BGP GR for compatible peers |
| save-config | (Optional) Save running-config to startup-config before fast-reload |
| force-all | Force upgrade the system |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3605139808

---

# Command: fast-reload network-os

## Syntax
```
fast-reload network-os <uri>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fast-reload | fast-reload software |
| network-os | non-cisco OS |
| uri | Enter image uri |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp5597213660

---

# Command: fast-reroute

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fast-reroute | Specify mpls tunnel can be fast-rerouted |
| node-protect | (Optional) node protection desired |
| bw-protect | (Optional) bandwidth protection desired |

**Command Mode:** /exec/configure/if-te /exec/configure/tunnel-te/cbts-member

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2031019598

---

# Command: fast-reroute backup-prot-preempt optimize-bw

## Syntax
```
[no] fast-reroute backup-prot-preempt optimize-bw &#124; no fast-reroute timers promotion &#124; fast-reroute timers promotion <seconds>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fast-reroute | fast-reroute parameters |
| backup-prot-preempt | Preemption algorithm for backup tunnels |
| optimize-bw | Reduce bandwidth wastage (default: minimize LSPs preempted) |
| timers | configure fast-reroute timer |
| promotion | Configure how often we scan for LSP backup promotion |
| seconds | seconds between promotions (0 disables promotion.) |

**Command Mode:** /exec/configure/te

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2263135571

---

# Command: fcdroplatency network

## Syntax
```
[no] fcdroplatency { network <i0> [ vsan <i1> ] &#124; switch <i2> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fcdroplatency | configure switch or network latency |
| network | network latency in milliseconds |
| i0 | network latency in milliseconds |
| vsan | (Optional) VSAN id range |
| i1 | (Optional) |
| switch | switch latency in milliseconds |
| i2 | switch latency in milliseconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2131454380

---

# Command: fcoe

## Syntax
```
[no] fcoe
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fcoe | create fcoe associate between fex and switch |

**Command Mode:** /exec/configure/fex

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2340830775

---

# Command: fcoe

## Syntax
```
[no] fcoe
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| fcoe | FCOE Congiguration |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3015694053

---

# Command: fcoe enable-fex

## Syntax
```
[no] fcoe enable-fex
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fcoe | FCOE command |
| enable-fex | Enables FCoE over FEX HIF interfaces |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp7932297730

---

# Command: fcoe fcf-priority

## Syntax
```
fcoe fcf-priority <i0> &#124; no fcoe fcf-priority
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fcoe | FCOE command |
| fcf-priority | FCF priority specification |
| i0 | Enter FCF prirority |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, qos, F-commands
**Command ID:** wp4232237000

---

# Command: fcoe fcmap

## Syntax
```
fcoe fcmap <i0> &#124; no fcoe fcmap
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fcoe | FCOE command |
| fcmap | FC MAP specification |
| i0 | Enter FCMAP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1530761422

---

# Command: fcoe fka-adv-period

## Syntax
```
fcoe fka-adv-period <i0> &#124; no fcoe fka-adv-period
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fcoe | FCOE command |
| fka-adv-period | FKA Advertisement Period |
| i0 | FKA Advertisement Period (in sec) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1833877351

---

# Command: fcoe veloopback

## Syntax
```
fcoe veloopback &#124; no fcoe veloopback
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fcoe | FCOE command |
| veloopback | VFID check for VE ports |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3368227812

---

# Command: fcoe vsan

## Syntax
```
fcoe vsan <tran-id> &#124; no fcoe vsan
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its default |
| fcoe | FCOE Congiguration |
| vsan | Translated VSAN Status |
| tran-id | Enter VSAN-ID being associated with VLAN-ID |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp9519065910

---

# Command: fctimer D_S_TOV

## Syntax
```
[no] fctimer D_S_TOV <i0> [ vsan <i1> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| D_S_TOV | D_S_TOV in milliseconds(5000-10000) |
| i0 | D_S_TOV in milliseconds(5000-10000) |
| vsan | (Optional) Specify VSAN id |
| i1 | (Optional) VSAN id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp7612428260

---

# Command: fctimer E_D_TOV

## Syntax
```
[no] fctimer E_D_TOV <i0> [ vsan <i1> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| E_D_TOV | E_D_TOV in milliseconds(1000-4000) |
| i0 | E_D_TOV in milliseconds(1000-4000) |
| vsan | (Optional) Specify VSAN id |
| i1 | (Optional) VSAN id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2918504284

---

# Command: fctimer R_A_TOV

## Syntax
```
[no] fctimer R_A_TOV <i0> [ vsan <i1> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| R_A_TOV | R_A_TOV in milliseconds(5000-10000) |
| i0 | R_A_TOV in milliseconds(5000-10000) |
| vsan | (Optional) Specify VSAN id |
| i1 | (Optional) VSAN id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp3996416021

---

# Command: fctimer abort

## Syntax
```
[no] fctimer abort
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| abort | abort the fctimer configuration commands |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2458094296

---

# Command: fctimer commit

## Syntax
```
[no] fctimer commit
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| commit | commit the fctimer configuration commands |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2460065856

---

# Command: fctimer distribute

## Syntax
```
[no] fctimer distribute
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fctimer | configure fibre channel timers |
| distribute | Enable distribution of fctimer configuration using CFS |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2202052035

---

# Command: feature-set

## Syntax
```
feature-set <fs>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| feature-set | Enable feature-set |
| fs | allow feature-set |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2609918640

---

# Command: feature-set

## Syntax
```
[no] feature-set <fs>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| feature-set | Enable feature-set |
| fs | allow feature-set |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2705080326

---

# Command: feature

## Syntax
```
[no] feature <arg1>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Feature name |
| arg1 | Enter feature name |

**Command Mode:** /exec/configure/rolefeaturegrp

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3901825842

---

# Command: feature analytics

## Syntax
```
[no] feature analytics
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| analytics | Enable/Disable Analytics!!! |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3076689780

---

# Command: feature bash-shell

## Syntax
```
[no] feature bash-shell
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| bash-shell | Enable/Disable bash-shell |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2019956334

---

# Command: feature bfd

## Syntax
```
[no] feature bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| bfd | bfd |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, bfd, F-commands
**Command ID:** wp9452633010

---

# Command: feature bgp

## Syntax
```
[no] feature bgp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| bgp | Enable/Disable Border Gateway Protocol (BGP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp7500607850

---

# Command: feature catena

## Syntax
```
[no] feature catena
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| catena | Enable/Disable catena |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp6314575120

---

# Command: feature container-tracker

## Syntax
```
[no] feature container-tracker
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| container-tracker | Enable/Disable NXOS Container Tracker |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3514325589

---

# Command: feature dhcp

## Syntax
```
[no] feature dhcp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| dhcp | Enable/Disable DHCP Manager |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp6990890620

---

# Command: feature dot1x

## Syntax
```
[no] feature dot1x
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| dot1x | Enable/Disable dot1x |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3222966709

---

# Command: feature eigrp

## Syntax
```
[no] feature eigrp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| eigrp | Enable/Disable Enhanced Interior Gateway Routing Protocol (EIGRP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp1540177332

---

# Command: feature evb

## Syntax
```
[no] feature evb
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| evb | Enable/Disable Edge Virtual Bridge (EVB) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp7542315400

---

# Command: feature evmed

## Syntax
```
[no] feature evmed
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| evmed | Enable/Disable Generic event detectors |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1567812066

---

# Command: feature fabric forwarding

## Syntax
```
[no] feature fabric forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| fabric | Enable/Disable Fabric Services |
| forwarding | Enable/Disable Fabric Forwarding Protocol: Host Mobility Manager (HMM) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1311103385

---

# Command: feature flexlink

## Syntax
```
[no] feature flexlink
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| flexlink | Enable/Disable Flexlink |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4193567808

---

# Command: feature grpc

## Syntax
```
[no] feature grpc
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| grpc | Enable/Disable grpc Services |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp9717559760

---

# Command: feature hardware-telemetry

## Syntax
```
[no] feature hardware-telemetry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| hardware-telemetry | Enable/Disable Hardware Telemetry |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3861135750

---

# Command: feature hsrp

## Syntax
```
[no] feature hsrp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| hsrp | Enable/Disable Hot Standby Router Protocol (HSRP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4623185050

---

# Command: feature icam

## Syntax
```
[no] feature icam
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| icam | Enable/Disable icam |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3459919503

---

# Command: feature imp

## Syntax
```
[no] feature imp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| imp | Enable/Disable IMP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1964792997

---

# Command: feature interface-vlan

## Syntax
```
[no] feature interface-vlan
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| interface-vlan | Enable/Disable interface vlan |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp2865158665

---

# Command: feature isis

## Syntax
```
[no] feature isis
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| isis | Enable/Disable IS-IS Unicast Routing Protocol (IS-IS) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp3506287809

---

# Command: feature itd

## Syntax
```
[no] feature itd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| itd | Enable/Disable ITD |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3234141588

---

# Command: feature lacp

## Syntax
```
[no] feature lacp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| lacp | Enable/Disable LACP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, layer2, F-commands
**Command ID:** wp3652857984

---

# Command: feature ldap

## Syntax
```
[no] feature ldap
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ldap | Enable/Disable ldap |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1333791738

---

# Command: feature lldp

## Syntax
```
[no] feature lldp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| lldp | Enable/Disable LLDP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3515950865

---

# Command: feature macsec

## Syntax
```
[no] feature macsec
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| macsec | Enable/Disable CTS |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3441169013

---

# Command: feature mpls evpn

## Syntax
```
[no] feature mpls evpn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| evpn | Enable MPLS EVPN |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2057074133

---

# Command: feature mpls l3vpn

## Syntax
```
[no] feature mpls l3vpn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| l3vpn | Enable/Disable Layer 3 Virtual Private Networks |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1585748452

---

# Command: feature mpls ldp

## Syntax
```
[no] feature mpls ldp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| ldp | Enable/Disable Label Distribution Protocol |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1428364653

---

# Command: feature mpls oam

## Syntax
```
[no] feature mpls oam
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| oam | Enable MPLS OAM |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2912269543

---

# Command: feature mpls segment-routing

## Syntax
```
[no] feature mpls segment-routing
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| segment-routing | Enable Segment-routing |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2828603326

---

# Command: feature mpls segment-routing traffic-engineering

## Syntax
```
[no] feature mpls segment-routing traffic-engineering
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| segment-routing | Enable Segment-routing |
| traffic-engineering | Enable/Disable segment-routing traffic-engineering |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp3491652600

---

# Command: feature mpls static

## Syntax
```
[no] feature mpls static
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| static | Enable/Disable Static Labeled Paths |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp6260088870

---

# Command: feature mpls traffic-engineering

## Syntax
```
[no] feature mpls traffic-engineering
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mpls | Enable/Disable MPLS Services |
| traffic-engineering | Enable/Disable MPLS Traffic Engineering |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2376141635

---

# Command: feature msdp

## Syntax
```
[no] feature msdp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| msdp | Enable/Disable Multicast Source Discovery Protocol (MSDP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1499491641

---

# Command: feature mvpn

## Syntax
```
[no] feature mvpn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| mvpn | Multicast Virtual Private Networks. |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4911632450

---

# Command: feature nat

## Syntax
```
[no] feature nat
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| nat | Enable/Disable NAT |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3286652554

---

# Command: feature nbm

## Syntax
```
[no] feature nbm
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable a feature |
| nbm | Enable/Disable Non Blocking Multicast (NBM) feature |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4002479500

---

# Command: feature netconf

## Syntax
```
[no] feature netconf
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| netconf | Enable/Disable netconf Services |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp7278080930

---

# Command: feature netflow

## Syntax
```
[no] feature netflow
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| netflow | Enable/Disable NetFlow |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1169736819

---

# Command: feature ngmvpn

## Syntax
```
[no] feature ngmvpn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ngmvpn | Enable/Disable EVPN/MVPN features |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3618137350

---

# Command: feature ngoam

## Syntax
```
[no] feature ngoam
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ngoam | Enable/Disable ngoam |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1841447092

---

# Command: feature ngoam

## Syntax
```
[no] feature ngoam
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ngoam | Enable/Disable ngoam |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3939796088

---

# Command: feature npiv

## Syntax
```
[no] feature npiv
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4195798793

---

# Command: feature ntp

## Syntax
```
[no] feature ntp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| feature | Command to enable/disable features |
| ntp | Enable/Disable NTP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2454383323

---

# Command: feature nv overlay

## Syntax
```
[no] feature nv overlay
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| nv | Enable/Disable VxLAN |
| overlay | Enable/Disable VxLAN |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1323027345

---

# Command: feature nxapi

## Syntax
```
[no] feature nxapi
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| nxapi | Enable/Disable nxapi |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3883841870

---

# Command: feature nxdb

## Syntax
```
[no] feature nxdb
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| nxdb | Enable/Disable nxdb |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4277579580

---

# Command: feature nxsdk

## Syntax
```
[no] feature nxsdk
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| nxsdk | Enable/Disable nxsdk Services |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2195149272

---

# Command: feature openflow

## Syntax
```
[no] feature openflow
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| openflow | Enable/Disable OpenFlow agent |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1781196929

---

# Command: feature ospf

## Syntax
```
[no] feature ospf
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ospf | Enable/Disable Open Shortest Path First Protocol (OSPF) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2374119928

---

# Command: feature ospfv3

## Syntax
```
[no] feature ospfv3
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ospfv3 | Enable/Disable Open Shortest Path First Version 3 Protocol (OSPFv3) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp5448676960

---

# Command: feature password encryption aes

## Syntax
```
[no] feature password encryption aes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Enable the feature |
| password | Credential(s) for the user(s)/device(s) |
| encryption | Strong encryption for credential(s) |
| aes | Encrypt using AES encryption standard |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2284251151

---

# Command: feature pbr

## Syntax
```
[no] feature pbr
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| pbr | Enable/Disable Policy Based Routing(PBR) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1186844435

---

# Command: feature pim

## Syntax
```
[no] feature pim
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| pim | Enable/Disable Protocol Independent Multicast (PIM) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3479339991

---

# Command: feature pim6

## Syntax
```
[no] feature pim6
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| pim6 | Enable/Disable Protocol Independent Multicast(PIM) for IPv6 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1025107063

---

# Command: feature plb

## Syntax
```
[no] feature plb
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| plb | Enable/Disable Pervasive Load Balancing feature |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2803383923

---

# Command: feature pnp

## Syntax
```
[no] feature pnp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| pnp | Enable/Disable PNP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3727797360

---

# Command: feature poap

## Syntax
```
[no] feature poap
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| poap | Enable/Disable POAP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1786576049

---

# Command: feature poe

## Syntax
```
[no] feature poe
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable a feature |
| poe | Enable/Disable Power over Ethernet(PoE) feature |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2722647728

---

# Command: feature pong

## Syntax
```
[no] feature pong
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| pong | Enable/Disable Pong |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2505216813

---

# Command: feature port-security

## Syntax
```
[no] feature port-security
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable eth port security features |
| port-security | Enable/Disable port-security |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp3762908096

---

# Command: feature private-vlan

## Syntax
```
[no] feature private-vlan
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| private-vlan | Enable/Disable private-vlan |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp1080163683

---

# Command: feature privilege

## Syntax
```
[no] feature privilege
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| privilege | Enable/Disable IOS type privilege level support |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1391203948

---

# Command: feature ptp

## Syntax
```
[no] feature ptp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ptp | Enable/Disable PTP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2916765780

---

# Command: feature restconf

## Syntax
```
[no] feature restconf
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| restconf | Enable/Disable restconf Services |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp6727467020

---

# Command: feature rip

## Syntax
```
[no] feature rip
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| rip | Enable/Disable Routing Information Protocol (RIP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, network, F-commands
**Command ID:** wp1235505971

---

# Command: feature scheduler

## Syntax
```
[no] feature scheduler
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| scheduler | Enable/Disable scheduler |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1138011950

---

# Command: feature scp-server

## Syntax
```
[no] feature scp-server
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| scp-server | Enable/Disable SCP server |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1761078106

---

# Command: feature sflow

## Syntax
```
[no] feature sflow
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| sflow | Enable/Disable sFlow agent |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1641884798

---

# Command: feature sftp-server

## Syntax
```
[no] feature sftp-server
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| sftp-server | Enable/Disable SFTP server |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3624778599

---

# Command: feature signature-verification

## Syntax
```
[no] feature signature-verification
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| signature-verification | Enable image signature verification |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3705313554

---

# Command: feature sla responder

## Syntax
```
[no] feature sla responder
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| sla | Enable/Disable SLA |
| responder | Enable/Disable responder part of SLA |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2553864806

---

# Command: feature sla sender

## Syntax
```
[no] feature sla sender
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| sla | Enable/Disable SLA |
| sender | Enable/Disable sender part of SLA |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2168610474

---

# Command: feature sla twamp-server

## Syntax
```
[no] feature sla twamp-server
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| sla | Enable/Disable SLA |
| twamp-server | Enable/Disable twamp-server part of SLA |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2842371944

---

# Command: feature smart-channel

## Syntax
```
[no] feature smart-channel
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| smart-channel | Enable/Disable smart-channel |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2487788400

---

# Command: feature srv6

## Syntax
```
[no] feature srv6
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| srv6 | Enable/Disable SRv6 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3270352419

---

# Command: feature ssh

## Syntax
```
[no] feature ssh
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| ssh | Enable/Disable ssh |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2914553725

---

# Command: feature tacacs

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2767008200

---

# Command: feature telemetry

## Syntax
```
[no] feature telemetry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| telemetry | Enable/Disable Telemetry |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3009153331

---

# Command: feature telnet

## Syntax
```
[no] feature telnet
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| telnet | Enable/Disable telnet |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4185884310

---

# Command: feature tunnel

## Syntax
```
[no] feature tunnel
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| tunnel | Enable/Disable Tunnel Manager |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3879992527

---

# Command: feature udld

## Syntax
```
[no] feature udld
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| udld | Enable/Disable UDLD |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1960251184

---

# Command: feature vmtracker

## Syntax
```
[no] feature vmtracker
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vmtracker | Enable/Disable VM Tracker feature |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3585443544

---

# Command: feature vn-segment-vlan-based

## Syntax
```
[no] feature vn-segment-vlan-based
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vn-segment-vlan-based | Enable/Disable VLAN based VN segment |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp1971714173

---

# Command: feature vpc

## Syntax
```
[no] feature vpc
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vpc | Enable/Disable VPC (Virtual Port Channel) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, vpc, F-commands
**Command ID:** wp2596773620

---

# Command: feature vrrp

## Syntax
```
[no] feature vrrp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vrrp | Enable/Disable Virtual Router Redundancy Protocol (VRRP) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1196629225

---

# Command: feature vrrpv3

## Syntax
```
[no] feature vrrpv3
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vrrpv3 | Enable/Disable Virtual Router Redundancy Protocol (VRRP) version 3 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp8302797180

---

# Command: feature vtp

## Syntax
```
[no] feature vtp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| feature | Command to enable/disable features |
| vtp | Enable/Disable VTP |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp7491634900

---

# Command: fec

## Syntax
```
fec <fec_val_old> &#124; no fec [ <fec_val_old> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fec | Forwarding error correction |
| fec_val_old | Interface FEC options |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1434730100

---

# Command: fec

## Syntax
```
fec <fec_val> &#124; no fec [ <fec_val> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fec | Forwarding error correction |
| fec_val | Interface FEC options |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1858333274

---

# Command: fec

## Syntax
```
fec <fec_val> &#124; no fec [ <fec_val> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fec | Forwarding error correction |
| fec_val | Interface FEC options |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3547800745

---

# Command: fhrp delay minimum

## Syntax
```
[no] fhrp delay minimum &#124; fhrp delay minimum <delay>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fhrp | FHRP interface configuration commands |
| delay | Configure FHRP delay |
| minimum | minimum delay |
| delay | Seconds to delay |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3658804953

---

# Command: fhrp delay reload

## Syntax
```
[no] fhrp delay reload &#124; fhrp delay reload <delay>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| fhrp | FHRP interface configuration commands |
| delay | Configure FHRP delay |
| reload | reload delay |
| delay | Seconds to delay |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4223980259

---

# Command: filter

## Syntax
```
[no] filter <filtername>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| filter | Specify the filter to be applied |
| filtername | filter name to be applied |

**Command Mode:** /exec/configure/nfm-system

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3745507083

---

# Command: filter

## Syntax
```
[no] filter [ subject-name <s0> &#124; altname-email <s1> &#124; altname-upn <s2> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Configure mapping filter |
| subject-name | (Optional) Subject name of the certificate |
| s0 | (Optional) Subject name |
| altname-email | (Optional) Email id as an alternate name |
| s1 | (Optional) Email id |
| altname-upn | (Optional) User principal name as an alternate name |
| s2 | (Optional) User principal name |

**Command Mode:** /exec/configure/certmap-filter

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2389970102

---

# Command: filter access-group

## Syntax
```
[no] filter access-group <acl-name> [ allow-sharing ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Filter configuration |
| access-group | access control group |
| acl-name | access control list name |
| allow-sharing | (Optional) allow up to 4 access control groups on same source interface |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3375648961

---

# Command: filter ip

## Syntax
```
[no] filter ip <src_ip> <src_mask> <dst_ip> <dst_mask>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Set SPAN filter options |
| ip | Set SPAN IP filtering options |
| src_ip | Set source IP address |
| src_mask | Set source IP mask |
| dst_ip | Set destination IP address |
| dst_mask | Set destination IP mask |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, network, F-commands
**Command ID:** wp1122168815

---

# Command: filter ipv6 access-group

## Syntax
```
[no] filter ipv6 access-group <acl-name> [ allow-sharing ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Filter configuration |
| ipv6 | ipv6 access group |
| access-group | access control group |
| acl-name | access control list name |
| allow-sharing | (Optional) allow up to 4 access control groups on same source interface |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, network, F-commands
**Command ID:** wp4249827571

---

# Command: filter out

## Syntax
```
[ no &#124; default ] { filter-list <fltrlist-name> } { out &#124; in }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| filter-list | Apply AS-PATH filter-list |
| fltrlist-name | Name of filter-list |
| out | Apply policy to outgoing routes |
| in | Apply policy to incoming routes |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-vpls /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mvpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-mvpn /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-evpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3379931011

---

# Command: filter tx control-packets

## Syntax
```
[no] filter tx control-packets
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Set SPAN filter options |
| tx | Set SPAN tx filtering options |
| control-packets | Filter out CPU generated packets and SPAN only data packets |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1173463306

---

# Command: filter vlan

## Syntax
```
[no] filter vlan <vlan_mrange> [ include-untagged ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Filter configuration |
| vlan | Vlan type |
| include-untagged | (Optional) Include untagged frames on port with Layer 3 subinterfaces |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp2282826755

---

# Command: filter vlan include-untagged

## Syntax
```
[no] filter vlan include-untagged
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| filter | Filter configuration |
| vlan | Vlan type |
| include-untagged | Include untagged frames on port with Layer 3 subinterfaces |

**Command Mode:** /exec/configure/config-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp3681475369

---

# Command: find

## Syntax
```
find <s0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| find | Find a file below the current directory |
| s0 | Enter the filename prefix to search |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1958342849

---

# Command: fips debug errors debug

## Syntax
```
[no] fips debug errors { debug-lc-post-on-maint &#124; reset-debug-lc-post-on-maint }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fips | Enable/Disable FIPS mode |
| debug | Introduce errors into FIPS tests |
| errors | Introduce errors |
| debug-lc-post-on-maint | Run the switch on debug mode for fips maintenance state |
| reset-debug-lc-post-on-maint | Reset the mode from debug-lc-post-on-maint |

**Command Mode:** /exec/

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, network, F-commands
**Command ID:** wp3605440487

---

# Command: fips mode enable

## Syntax
```
[no] fips mode enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| fips | Enable/Disable FIPS mode |
| mode | FIPS mode |
| enable | Enable/Disable FIPS mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, network, F-commands
**Command ID:** wp3002047280

---

# Command: flow-count

## Syntax
```
[no] flow-count <count>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow-count | Flow count throttle for drop events |
| count | <1-32767> |

**Command Mode:** /exec/configure/config-fte-event/group-drop-events

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4024945765

---

# Command: flow-count

## Syntax
```
[no] flow-count <count>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow-count | Flow count throttle for drop events |
| count | <1-32767> |

**Command Mode:** /exec/configure/config-fte-event/group-latency-events

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1618211659

---

# Command: flow exporter

## Syntax
```
[no] flow exporter <exportername>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| exporter | Define a Flow Exporter |
| exportername | Name of Flow Exporter |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp2254644290

---

# Command: flow exporter

## Syntax
```
[no] flow exporter <exportername>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| exporter | Define a Flow Exporter |
| exportername | Name of Flow Exporter |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp2797786587

---

# Command: flow filter

## Syntax
```
[no] flow filter <filtername>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| filter | Define a Flow filter |
| filtername | Filter name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3373284690

---

# Command: flow forward

## Syntax
```
[no] flow { forward &#124; reverse }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flow | Configure ngoam flow |
| forward | Ngoam forward flow |
| reverse | Ngoam reverse flow |

**Command Mode:** /exec/configure/configngoamprofile

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2201890126

---

# Command: flow monitor

## Syntax
```
[no] flow monitor <monitorname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| monitor | Define a Flow Monitor |
| monitorname | Name of Flow Monitor |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1494396497

---

# Command: flow monitor

## Syntax
```
[no] flow monitor <monitorname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| monitor | Define a Flow Monitor |
| monitorname | Name of Flow Monitor |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3417231908

---

# Command: flow profile

## Syntax
```
[no] flow profile <profilename>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| profile | Define a Flow Profile |
| profilename | Profile name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3659497950

---

# Command: flow record

## Syntax
```
[no] flow record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| record | Define a Flow Record |
| recordname | Record name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3376173864

---

# Command: flow record

## Syntax
```
[no] flow record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| record | Define a Flow Record |
| recordname | Record name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1742083820

---

# Command: flow rtp timeout

## Syntax
```
{ [ no ] flow rtp timeout <time> &#124; no flow rtp timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| rtp | Real-time Transport Protocol |
| timeout | Define RTP Flow Error Monitoring Duration |
| time | Time in Minutes. Enter 0 to keep the flows even if they are idle |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp1097912580

---

# Command: flow system config

## Syntax
```
[no] flow system config
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| system | Define a Flow system |
| config | Define a Flow system config |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4183903533

---

# Command: flow timeout

## Syntax
```
{ [ no ] flow timeout <time> &#124; no flow timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| flow | Enable/Disable NetFlow configuration |
| timeout | Define a Flow Timeout |
| time | Time in seconds (flush-cache-Only) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, system, F-commands
**Command ID:** wp2857493950

---

# Command: flowcontrol hardware

## Syntax
```
[no] flowcontrol hardware
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flowcontrol | Set flow control |
| hardware | Set hardware flowcontrol |

**Command Mode:** /exec/configure/com1

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2080829402

---

# Command: flowcontrol receive

## Syntax
```
flowcontrol { receive { <rx_flowctrl> } &#124; send { <tx_flowctrl> } } &#124; no flowcontrol { receive [ { <rx_flowctrl> } ] &#124; send
 [ { <tx_flowctrl> } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| flowcontrol | Configure interface flowcontrol |
| receive | Receive pause frames |
| rx_flowctrl | Receive flow control |
| send | Send pause frames |
| tx_flowctrl | Send flow control |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-non-member /exec/configure/if-port-channel

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1798799942

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes in RIB during restart |

**Command Mode:** /exec/configure/router-eigrp

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp3201157542

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes in RIB during restart |

**Command Mode:** /exec/configure/router-rip

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp3136840506

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes on non-graceful controlled restart |

**Command Mode:** /exec/configure/router-isis

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp6856173170

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes on a non-graceful controlled restart |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp3933846513

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes on a non-graceful controlled restart |

**Command Mode:** /exec/configure/router-ospf

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2230255881

---

# Command: flush-routes

## Syntax
```
[no] flush-routes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| flush-routes | Flush routes in RIB upon controlled restart |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, routing, F-commands
**Command ID:** wp2280638403

---

# Command: follow

## Syntax
```
follow <name> &#124; no follow
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| follow | Group to be followed |
| name | master name string to follow |

**Command Mode:** /exec/configure/if-eth-any/hsrp_ipv4 /exec/configure/if-eth-any/hsrp_ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp8197216980

---

# Command: format

## Syntax
```
format <uri1>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| format | Format disks |
| uri1 | destination filesystem path |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1851051524

---

# Command: format bootflash

## Syntax
```
format bootflash:
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| format | Format disks |
| bootflash: | Format bootflash: |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, boot, F-commands
**Command ID:** wp1830045243

---

# Command: format bootflash check-filesystem

## Syntax
```
format bootflash: check-filesystem
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| format | Format disks |
| bootflash: | Format bootflash: |
| check-filesystem | Format bootflash: and fix any errors in file system |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, boot, F-commands
**Command ID:** wp1245020320

---

# Command: format usb1

## Syntax
```
format usb1:
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| format | Format disks |
| usb1: | Format usb1: |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1033213089

---

# Command: forward

## Syntax
```
[no] forward
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| forward | Configure paths |

**Command Mode:** /exec/configure/mpls_static/ipv4/lsp/inlabel

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp4449166030

---

# Command: forwarding-adjacency

## Syntax
```
[no] forwarding-adjacency &#124; forwarding-adjacency [ holdtime <msec> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| forwarding-adjacency | Treat this tunnel as a Forwarding Adjacency |
| holdtime | (Optional) How long in msecs to wait upon flooding a down Forwarding Adjacency |
| msec | (Optional) Holdtime on MPLS TE Down |

**Command Mode:** /exec/configure/if-te

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2327577803

---

# Command: fragments

## Syntax
```
[no] fragments <opt_type>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| opt_type | frag_op_type |

**Command Mode:** /exec/configure/ipacl /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3166424543

---

# Command: frequency

## Syntax
```
{ { no &#124; default } frequency &#124; frequency <seconds> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| frequency | Frequency of an operation |
| seconds | Frequency in seconds |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/jitter /exec/configure/ip-sla/tcp /exec/configure/ip-sla/icmpEcho /exec/configure/ip-sla/dns
 /exec/configure/ip-sla/fabricPathEcho /exec/configure/ip-sla/http

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3511194598

---

# Command: from to

## Syntax
```
{ [ no ] { { from <frm-list> to <to-val> } &#124; { default <value> } } } &#124; default copy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| from | Map values from this |
| frm-list | Original list of values which are to be mapped |
| to | Map values to this |
| to-val | New mapped value |
| default | map default values |
| value | default value to be set |
| copy | Do a default copy |

**Command Mode:** /exec/configure/def-tmap

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3226292262

---

# Command: from to

## Syntax
```
[no] { { from <frm-list> to <to-val> } &#124; { default { <value> &#124; copy &#124; ignore } } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| from | Map values from this |
| frm-list | Original list of values which are to be mapped |
| to | Map values to this |
| to-val | New mapped value |
| default | map default values |
| value | default value to be set |
| copy | Do a default copy |
| ignore | Ignore any unspecified values |

**Command Mode:** /exec/configure/table-map

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp1312968647

---

# Command: fte event

## Syntax
```
[no] fte event <eventname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fte | Enable/Disable FTE configuration |
| event | Define a FTE event |
| eventname | Event name |

**Command Mode:** /exec/configure/config-fte

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp5745195550

---

# Command: fte exporter

## Syntax
```
[no] fte exporter <exportername>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fte | Enable/Disable Flow Table Events configuration |
| exporter | Define a events Exporter |
| exportername | Name of event Exporter |

**Command Mode:** /exec/configure/config-fte

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, interface, F-commands
**Command ID:** wp4126593691

---

# Command: fte monitor

## Syntax
```
[no] fte monitor <monitorname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fte | Enable/Disable FTE configuration |
| monitor | Define a FTE Monitor |
| monitorname | Name of FTE Monitor |

**Command Mode:** /exec/configure/config-fte

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp8684485130

---

# Command: fte record

## Syntax
```
[no] fte record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fte | Enable/Disable FTE configuration |
| record | Define a FTE Record |
| recordname | Record name |

**Command Mode:** /exec/configure/config-fte

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp3988698284

---

# Command: fte system monitor

## Syntax
```
[no] fte system monitor <monitorname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fte | change fte global settings |
| system | global config |
| monitor | fte Monitor to be applied |
| monitorname | ssx Monitor to be applied |

**Command Mode:** /exec/configure/config-fte

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2456304061

---

# Command: ftrace

## Syntax
```
ftrace [ { set-opt { option <n0> <v0> &#124; filter <f0> <v0> } { proc <p0> &#124; buf_size <b0> } [ <s0> ] } &#124; { reset { all &#124; filter
 <f0> &#124; trace &#124; <s0> } } &#124; { enable { inband &#124; kernel &#124; lcnd <i0> &#124; process <i0> &#124; trace } } &#124; { list { filters <f0> &#124; curr_tracer
 &#124; all } } &#124; { debug { on &#124; off } } &#124; { dump { all &#124; traces } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ftrace | Run ftrace tool to enable/disable kernel/process tracing |
| set-opt | (Optional) Set ftrace tracing options available |
| reset | (Optional) Reset ftrace options to defaults, disable tracing |
| enable | (Optional) Enable ftrace tracing with given options |
| list | (Optional) List ftrace available options/filters/events |
| debug | (Optional) Ftrace based debug trace enable/disable |
| dump | (Optional) Dump traces collected in ftrace circular buffer |
| all | (Optional) Act on all available datasets |
| lcnd | (Optional) Trace proc/pid specific lcnd inband driver calls |
| inband | (Optional) Trace inband driver + netstack functions |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0110.html
**Tags:** config-mode, F-commands
**Command ID:** wp2398258381

---

