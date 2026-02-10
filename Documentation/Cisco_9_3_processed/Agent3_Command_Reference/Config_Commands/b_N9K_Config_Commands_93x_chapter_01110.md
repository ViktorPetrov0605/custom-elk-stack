# Chapter: N Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_01110.html
**Type:** Configuration Commands  
**Chapter:** Group-1110 Commands  
**Total Commands:** 120

## Command List

- `name-lookup`
- `name-lookup`
- `name`
- `name`
- `name`
- `nat destination`
- `nat destination`
- `nbm external-link`
- `nbm flow-definition`
- `nbm flow-definition`
- `nbm flow-policy`
- `nbm flow-policy`
- `nbm flow asm range`
- `nbm flow asm range`
- `nbm flow bandwidth immediate-recovery`
- `nbm flow bandwidth immediate-recovery`
- `nbm flow bandwidth kbps mbps gbps`
- `nbm flow bandwidth kbps mbps gbps`
- `nbm flow dscp`
- `nbm flow dscp`
- `nbm flow policer`
- `nbm flow policer`
- `nbm host-policy`
- `nbm host-policy`
- `nbm mode pim-active`
- `nbm reserve unicast fabric bandwidth`
- `nbm vrf`
- `nbm vrf default`
- `negotiate auto`
- `negotiate auto 25000`
- `neighbor-down fib-accelerate`
- `neighbor`
- `neighbor`
- `neighbor`
- `neighbor`
- `neighbor`
- `neighbor maximum-prefix`
- `nemo config address port interval`
- `net`
- `net`
- `net`
- `network`
- `network`
- `network`
- `network`
- `next-address exclude-address`
- `next-hop-self`
- `next-hop-third-party`
- `next-hop-third-party`
- `next-hop out-label explicit-null implicit-null next-hop auto-resolve out-label explicit-null implicit-null`
- `next-hop out-label explicit-null implicit-null next-hop auto-resolve out-label explicit-null implicit-null`
- `nexthop route-map`
- `nexthop suppress-default-resolution`
- `nexthop trigger-delay critical non-critical`
- `ngoam authentication-key`
- `ngoam connect-check`
- `ngoam install acl`
- `ngoam profile`
- `ngoam xconnect hb-interval`
- `no-more`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `no`
- `node`
- `node ip`
- `node ip`
- `node ip`
- `node ip`
- `npiv enable`
- `npv auto-load-balance disruptive`
- `npv traffic-map server-interface external-interface`
- `nsf await-redist-proto-convergence`
- `ntp access-group`
- `ntp access-group match-all`
- `ntp allow private`
- `ntp authenticate`
- `ntp authentication-key md5`
- `ntp drop-aged-packet`
- `ntp logging`
- `ntp master`
- `ntp passive`
- `ntp peer`
- `ntp rts-update`
- `ntp server`
- `ntp source-interface`
- `ntp source`
- `ntp sync-retry`
- `ntp trusted-key`
- `nv overlay evpn`
- `nve event-history size`
- `nve interface remap-replication-servers`
- `nve interface replication-server up`
- `nve oam mode draft-pang`
- `nxapi certificate`
- `nxapi flow`
- `nxapi http port`
- `nxapi ssl ciphers weak`
- `nxapi ssl protocols`
- `nxapi use-vrf management default`
- `nxsdk profile`
- `nxsdk remote port`
- `nxsdk service-name`

---

## Detailed Command Reference

# Command: name-lookup

## Syntax
```
[no] name-lookup
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| name-lookup | Enable Name Lookup for OSPF Neighbors |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1392311650

---

# Command: name-lookup

## Syntax
```
[no] name-lookup
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| name-lookup | Display OSPF router ids as DNS names |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1226319705

---

# Command: name

## Syntax
```
name <vlan-name> &#124; no name
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| name | Ascii name of the VLAN |
| vlan-name | The ascii name for the VLAN |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2691591039

---

# Command: name

## Syntax
```
name [ <name> ] &#124; no name
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| name | Redundancy name string |
| name | (Optional) name string |

**Command Mode:** /exec/configure/if-eth-any/hsrp_ipv4 /exec/configure/if-eth-any/hsrp_ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1443745963

---

# Command: name

## Syntax
```
name <name-val> &#124; no name [ <name-val> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| name | Set configuration name |
| name-val | Configuration name |

**Command Mode:** /exec/configure/spanning-tree/mst/configuration

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp8493446460

---

# Command: nat destination

## Syntax
```
{ nat destination } &#124; { no nat destination }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nat | Network Address Translation |
| destination | Destination NAT |

**Command Mode:** /exec/configure/plb

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1894657427

---

# Command: nat destination

## Syntax
```
{ nat destination } &#124; { no nat destination }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nat | Network Address Translation |
| destination | Destination NAT |

**Command Mode:** /exec/configure/itd

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1278049203

---

# Command: nbm external-link

## Syntax
```
[no] nbm external-link
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| external-link | link connected to external router. Configuring this will flap the interface |

**Command Mode:** /exec/configure/if-igp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp9079309780

---

# Command: nbm flow-definition

## Syntax
```
[no] nbm flow-definition <group> [ <source> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow-definition | Define a multicast flow |
| group | Multicast Group Address |
| source | (Optional) Source IP address to use |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2504858579

---

# Command: nbm flow-definition

## Syntax
```
[no] nbm flow-definition <group> [ <source> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow-definition | Define a multicast flow |
| group | Multicast Group Address |
| source | (Optional) Source IP address to use |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp6784759810

---

# Command: nbm flow-policy

## Syntax
```
[no] nbm flow-policy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow-policy | Flow Policy Characteristics |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp1600936791

---

# Command: nbm flow-policy

## Syntax
```
[no] nbm flow-policy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow-policy | Flow Policy Characteristics |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp3467817528

---

# Command: nbm flow asm range

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| asm | Any-Source Multicast (ASM) groups |
| range | Configure explicit group ranges |
| group | List of group range prefixes |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3703696335

---

# Command: nbm flow asm range

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| asm | Any-Source Multicast (ASM) groups |
| range | Configure explicit group ranges |
| group | List of group range prefixes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4690598460

---

# Command: nbm flow bandwidth immediate-recovery

## Syntax
```
[no] nbm flow bandwidth immediate-recovery
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| bandwidth | Bandwidth per flow |
| immediate-recovery | Free up used BW immediately on last OIF removal |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp1895808502

---

# Command: nbm flow bandwidth immediate-recovery

## Syntax
```
[no] nbm flow bandwidth immediate-recovery
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| bandwidth | Bandwidth per flow |
| immediate-recovery | Free up used BW immediately on last OIF removal |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp7033121220

---

# Command: nbm flow bandwidth kbps mbps gbps

## Syntax
```
{ nbm flow bandwidth { <val_kbps> kbps &#124; <val_mbps> mbps &#124; <val_gbps> gbps } } &#124; { no nbm flow bandwidth }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| bandwidth | Bandwidth per flow |
| val_kbps | Per Flow Bandwidth in Kbps |
| kbps | Bandwidth value in Kbps |
| val_mbps | Per Flow Bandwidth in Mbps |
| mbps | Bandwidth value in Mbps |
| val_gbps | Per Flow Bandwidth in Gbps |
| gbps | Bandwidth value in Gbps |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp3629315522

---

# Command: nbm flow bandwidth kbps mbps gbps

## Syntax
```
{ nbm flow bandwidth { <val_kbps> kbps &#124; <val_mbps> mbps &#124; <val_gbps> gbps } } &#124; { no nbm flow bandwidth }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| bandwidth | Bandwidth per flow |
| val_kbps | Per Flow Bandwidth in Kbps |
| kbps | Bandwidth value in Kbps |
| val_mbps | Per Flow Bandwidth in Mbps |
| mbps | Bandwidth value in Mbps |
| val_gbps | Per Flow Bandwidth in Gbps |
| gbps | Bandwidth value in Gbps |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp2828687412

---

# Command: nbm flow dscp

## Syntax
```
{ nbm flow dscp <val_dscp> } &#124; { no nbm flow dscp }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| dscp | DSCP for the flow |
| val_dscp | Integer value |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2785278439

---

# Command: nbm flow dscp

## Syntax
```
{ nbm flow dscp <val_dscp> } &#124; { no nbm flow dscp }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| dscp | DSCP for the flow |
| val_dscp | Integer value |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp9110821980

---

# Command: nbm flow policer

## Syntax
```
[no] nbm flow policer
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| policer | Flow rate limiter installed in hardware |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1286938930

---

# Command: nbm flow policer

## Syntax
```
[no] nbm flow policer
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| flow | Flow Characteristics |
| policer | Flow rate limiter installed in hardware |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1514301915

---

# Command: nbm host-policy

## Syntax
```
[no] nbm host-policy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| host-policy | NBM SW Host Admission Policy |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp1626688577

---

# Command: nbm host-policy

## Syntax
```
[no] nbm host-policy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| host-policy | NBM SW Host Admission Policy |

**Command Mode:** /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp1114815109

---

# Command: nbm mode pim-active

## Syntax
```
nbm mode pim-active [ __readonly__ <output> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nbm | Non Blocking Multicast |
| mode | Set pmn mode |
| pim-active | Bandwidth engine running in fabric |
| __readonly__ | (Optional) |
| output | (Optional) |

**Command Mode:** /exec/configure /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2933577751

---

# Command: nbm reserve unicast fabric bandwidth

## Syntax
```
nbm reserve unicast fabric bandwidth <percentage> &#124; no nbm reserve unicast fabric bandwidth
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| reserve | reserve bandwidth |
| unicast | unicast |
| fabric | fabric |
| bandwidth | percentage of bandwidth for unicast flow |
| percentage | percentage value |

**Command Mode:** /exec/configure /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, qos, N-commands
**Command ID:** wp1927149821

---

# Command: nbm vrf

## Syntax
```
[no] nbm vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| vrf | Display per-VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, overlay, N-commands
**Command ID:** wp2335093977

---

# Command: nbm vrf default

## Syntax
```
[no] nbm vrf default
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nbm | Non Blocking Multicast |
| vrf | Display per-VRF information |
| default | Default VRF |

**Command Mode:** /exec/configure /exec/configure/nbm-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, overlay, N-commands
**Command ID:** wp2622660282

---

# Command: negotiate auto

## Syntax
```
negotiate auto &#124; no negotiate auto
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| negotiate | Configure link negotiation parameters |
| auto | Configure auto-negotiation |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-non-member /exec/configure/if-port-channel

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3689124835

---

# Command: negotiate auto 25000

## Syntax
```
[no] negotiate auto 25000
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| negotiate | Configure link negotiation parameters |
| auto | Configure auto-negotiation |
| 25000 | Force auto-negotiate to only 25000 and change fec to auto |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-non-member /exec/configure/if-port-channel

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1174070015

---

# Command: neighbor-down fib-accelerate

## Syntax
```
[no] neighbor-down fib-accelerate
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| neighbor-down | Handle BGP neighbor down event, due to various reasons |
| fib-accelerate | Accelerate the hardware updates for IP/IPv6 adjacencies for neighbor |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3301378060

---

# Command: neighbor

## Syntax
```
[no] neighbor { <neighbor-prefix> &#124; <ipv6-neighbor-prefix> } [ remote-as [ <asn> &#124; route-map <rmap-name> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| neighbor | Configure a BGP neighbor |
| neighbor-prefix | IP prefix for neighbors |
| remote-as | (Optional) Specify Autonomous System Number of the neighbor |
| asn | (Optional) Autonomous System Number |
| route-map | (Optional) Route-map to match prefix peer AS number |
| rmap-name | (Optional) Route-map name |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2927162208

---

# Command: neighbor

## Syntax
```
neighbor [ vrf { <vrf-name> &#124; <vrf-known-name> } ] <ipaddr> { implicit-withdraw &#124; labels accept <pfx-list> &#124; targeted } &#124;
 no neighbor [ vrf { <vrf-name> &#124; <vrf-known-name> } ] <ipaddr> [ implicit-withdraw &#124; labels accept &#124; targeted ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| neighbor | Configure neighbor parameters |
| vrf | (Optional) VRF Routing/Forwarding instance information |
| vrf-name | (Optional) VPN Routing/Forwarding instance name |
| vrf-known-name | (Optional) Known VRF name |
| ipaddr | IP address for LDP neighbor |
| implicit-withdraw | Enable LDP Implicit Withdraw Label |
| labels | Configure label binding exchange controls |
| accept | Specify label bindings to accept |
| pfx-list | Name of prefix list |

**Command Mode:** /exec/configure/ldp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1802692110

---

# Command: neighbor

## Syntax
```
[no] neighbor { <neighbor-id> &#124; <ipv6-neighbor-id> } [ remote-as <asn> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| neighbor | Configure a BGP neighbor |
| neighbor-id | IP address of the neighbor |
| remote-as | (Optional) Specify Autonomous System Number of the neighbor |
| asn | (Optional) Autonomous System Number |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2685189284

---

# Command: neighbor

## Syntax
```
[no] neighbor { <neighbor-id> &#124; <ipv6-neighbor-id> } [ remote-as <asn> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| neighbor | Configure a BGP neighbor |
| neighbor-id | IP address of the neighbor |
| remote-as | (Optional) Specify Autonomous System Number of the neighbor |
| asn | (Optional) Autonomous System Number |

**Command Mode:** /exec/configure/router-bgp/router-bgp-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4360993850

---

# Command: neighbor

## Syntax
```
[no] neighbor { <neighbor-prefix> &#124; <ipv6-neighbor-prefix> } [ remote-as [ <asn> &#124; route-map <rmap-name> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| neighbor | Configure a BGP neighbor |
| neighbor-prefix | IP prefix for neighbors |
| remote-as | (Optional) Specify Autonomous System Number of the neighbor |
| asn | (Optional) Autonomous System Number |
| route-map | (Optional) Route-map to match prefix peer AS number |
| rmap-name | (Optional) Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-vrf

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1351900160

---

# Command: neighbor maximum-prefix

## Syntax
```
{ { neighbor <address> { <interface> &#124; maximum-prefix <value> [ warning-only ] } } &#124; { no neighbor <address> [ <interface>
 &#124; maximum-prefix <value> [ warning-only ] ] } } &#124; { { neighbor maximum-prefix <value> [ <threshold> ] [ warning-only ] [ restart
 <time1> ] [ restart-count <count> ] [ reset-time <time2> ] [ dampened ] } &#124; { no neighbor maximum-prefix [ <value> [ <threshold>
 ] [ warning-only ] [ restart <time1> ] [ restart-count <count> ] ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| neighbor | Specify a neighbor router |
| interface | Interface |
| address | Neighbor address |
| maximum-prefix | Maximum number of IP prefixes acceptable from a neighbor |
| value | Number of IP prefixes for maximum-prefix limit |
| threshold | (Optional) Threshold value (%) at which to generate a warning message |
| warning-only | (Optional) Only give warning message when limit is exceeded |
| restart | (Optional) Duration for which a prefix source is ignored |
| time1 | (Optional) Restart interval in minutes |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3179747456

---

# Command: nemo config address port interval

## Syntax
```
[no] nemo config address <ip_address> port <portnum> interval <interval-num>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nemo | Nemo switch onboarding enabler |
| config | Configure Nemo for switch onboarding |
| address | IP address of the Nemo platform |
| ip_address | IP Address |
| port | Port number of the Nemo platform |
| portnum | Port number |
| interval | Config interval in millisecond |
| interval-num | Config interval in millisecond |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp1233386903

---

# Command: net

## Syntax
```
[no] net <net>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| net | Configure Network Entity Title for IS-IS |
| net | NET in form of XX.XXXX. ... .XXXX[.00] |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3750650403

---

# Command: net

## Syntax
```
[no] net <net>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| net | Configure Network Entity Title for IS-IS |
| net | NET in form of XX.XXXX. ... .XXXX[.00] |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3764372730

---

# Command: net

## Syntax
```
[no] net <net>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| net | Configure Network Entity Title for IS-IS |
| net | NET in form of XX.XXXX. ... .XXXX[.00] |

**Command Mode:** /exec/configure/otv-isis

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3374287684

---

# Command: network

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| network | Configure an IPv6 prefix to advertise |
| route-map | (Optional) Apply route-map to modify attributes |
| rmap-name | (Optional) Route-map name |
| summarize | (Optional) Summarize more specific prefixes from routing table |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-ipv6 /exec/configure/router-bgp/router-bgp-vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3760600926

---

# Command: network

## Syntax
```
[no] network { <ip-dest> <ip-mask> &#124; <ip-prefix> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| network | RIP IP network |
| ip-dest | IP addr format |
| ip-mask | IP network mask format |
| ip-prefix | Exact prefix |

**Command Mode:** /exec/configure/router-rip/router-rip-af-ipv4 /exec/configure/router-rip/router-rip-vrf-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1636241008

---

# Command: network

## Syntax
```
[no] network { { <address> <mask> } &#124; <prefix> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| network | Enable routing on an IP network |
| address | Network number |
| mask | EIGRP wild card bits |
| prefix | IP prefix in slash format |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1755670500

---

# Command: network

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| network | Configure an IP prefix to advertise |
| ip-addr | IP network to advertise |
| mask | Configure the mask of the IP prefix to advertise |
| ip-mask | Dotted 4-octet mask |
| ip-prefix | IP prefix in CIDR format |
| route-map | (Optional) Apply route-map to modify attributes |
| rmap-name | (Optional) Route-map name |
| summarize | (Optional) Summarize more specific prefixes from routing table |
| evpn | (Optional) Only advertise route towards evpn side |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-ipv4 /exec/configure/router-bgp/router-bgp-vrf-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1281165540

---

# Command: next-address exclude-address

## Syntax
```
{ next-address [ loose &#124; strict ] <ipaddr> &#124; exclude-address <ipaddr> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| next-address | Specify the next address in the path |
| loose | (Optional) Target address is loose |
| strict | (Optional) Target address is strict |
| exclude-address | Exclude an address from subsequent partial path segments |
| ipaddr | Enter IP address (A.B.C.D) |

**Command Mode:** /exec/configure/te/expl-path

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp5247116380

---

# Command: next-hop-self

## Syntax
```
[ no &#124; default ] next-hop-self [ all ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| next-hop-self | Set our address as nexthop (non-reflected) |
| all | (Optional) Set our address as nexthop for all routes |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3821511600

---

# Command: next-hop-third-party

## Syntax
```
[ no &#124; default ] next-hop-third-party
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| next-hop-third-party | Compute a third-party nexthop if possible |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3248901651

---

# Command: next-hop-third-party

## Syntax
```
[ no &#124; default ] next-hop-third-party
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| next-hop-third-party | Compute a third-party nexthop if possible |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2930612890

---

# Command: next-hop out-label explicit-null implicit-null next-hop auto-resolve out-label explicit-null implicit-null

## Syntax
```
[no] { next-hop [ backup <interface> ] <next-hop> out-label { <static-outlabel> &#124; explicit-null &#124; implicit-null } &#124; next-hop
 auto-resolve out-label { <static-outlabel> &#124; explicit-null &#124; implicit-null } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| next-hop | Nexthop |
| next-hop | Destination IPv4 next hop |
| static-outlabel | Label Value |
| interface | (Optional) Back up interface |
| out-label | Output label |
| explicit-null | IETF MPLS IPv4 explicit null label (0) |
| implicit-null | IETF MPLS implicit null label (3) |
| auto-resolve | auto resolve the destination path |
| backup | (Optional) Backup destination |

**Command Mode:** /exec/configure/mpls_static/ipv4/input

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2930458749

---

# Command: next-hop out-label explicit-null implicit-null next-hop auto-resolve out-label explicit-null implicit-null

## Syntax
```
[no] { next-hop [ backup <interface> ] <ipv6-next-hop> out-label { <static-outlabel> &#124; explicit-null &#124; implicit-null } &#124; next-hop
 auto-resolve out-label { <static-outlabel> &#124; explicit-null &#124; implicit-null } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| next-hop | Nexthop |
| static-outlabel | Label Value |
| interface | (Optional) Back up interface |
| out-label | Output label |
| explicit-null | IETF MPLS IPv6 explicit null label (2) |
| implicit-null | IETF MPLS implicit null label (3) |
| auto-resolve | auto resolve the destination path |
| backup | (Optional) Backup destination |

**Command Mode:** /exec/configure/mpls_static/ipv6/input

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2940290430

---

# Command: nexthop route-map

## Syntax
```
[no] nexthop route-map <rmap-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nexthop | Nexthop tracking |
| route-map | Route map for valid nexthops |
| rmap-name | Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af /exec/configure/router-bgp/router-bgp-af-l2vpn-evpn /exec/configure/router-bgp/router-bgp-af-link-state
 /exec/configure/router-bgp/router-bgp-af-ipv4-mvpn /exec/configure/router-bgp/router-bgp-af-ipv6-mvpn /exec/configure/router-bgp/router-bgp-af-ipv4-mdt
 /exec/configure/router-bgp/router-bgp-af-l2vpn-vpls

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, routing, N-commands
**Command ID:** wp3570903351

---

# Command: nexthop suppress-default-resolution

## Syntax
```
[no] nexthop suppress-default-resolution
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nexthop | Nexthop resolution options |
| suppress-default-resolution | Prohibit use of default route for nexthop address resolution |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2011301258

---

# Command: nexthop trigger-delay critical non-critical

## Syntax
```
{ nexthop trigger-delay critical <criticaldelay> non-critical <noncriticaldelay> } &#124; { no nexthop trigger-delay }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nexthop | Nexthop tracking |
| trigger-delay | Set the delay to trigger nexthop tracking |
| critical | Nexthop changes affecting reachability |
| non-critical | Other nexthop changes |
| noncriticaldelay | Delay value (miliseconds) |
| criticaldelay | Delay value (miliseconds) |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af /exec/configure/router-bgp/router-bgp-af-ipv4-mdt /exec/configure/router-bgp/router-bgp-af-vpnv4
 /exec/configure/router-bgp/router-bgp-af-vpnv6 /exec/configure/router-bgp/router-bgp-af-link-state /exec/configure/router-bgp/router-bgp-af-l2vpn-vpls
 /exec/configure/router-bgp/router-bgp-af-ipv4-mvpn /exec/configure/router-bgp/router-bgp-af-ipv6-mvpn /exec/configure/router-bgp/router-bgp-af-l2vpn-evpn

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1249274677

---

# Command: ngoam authentication-key

## Syntax
```
{ ngoam authentication-key <value> } &#124; { no ngoam authentication-key [ <value> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ngoam | Configure ngoam |
| authentication-key | Ngoam authentication-key |
| value | authentication key |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1619917934

---

# Command: ngoam connect-check

## Syntax
```
[no] ngoam connect-check <id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ngoam | Configure ngoam |
| connect-check | Configure ngoam oam connectivity check |
| id | connect check id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1261290365

---

# Command: ngoam install acl

## Syntax
```
[no] ngoam install acl
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ngoam | Configure ngoam |
| install | Ngoam install |
| acl | Ngoam install acl |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, security, N-commands
**Command ID:** wp1962247222

---

# Command: ngoam profile

## Syntax
```
[no] ngoam profile <profile-id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ngoam | Configure ngoam |
| profile | Configure ngoam oam profile |
| profile-id | ngoam profile id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2266349971

---

# Command: ngoam xconnect hb-interval

## Syntax
```
{ ngoam xconnect hb-interval <ms> } &#124; { no ngoam xconnect hb-interval [ <ms> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ngoam | Configure ngoam |
| xconnect | Configure xconnect parameters |
| hb-interval | Configure xconnect heartbeat interval |
| ms | interval in ms, 3 failures triggers failure default is 190 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2052705700

---

# Command: no-more

## Syntax
```
&#124; no-more
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| no-more | Turn-off pagination for command output |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3182822022

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| ethertype | Configure match based on ethertype |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| ethertypeid | Configure the ethertype value |
| vlanid | (Optional) VLAN number |
| intfid | (Optional) Interface index |

**Command Mode:** /exec/configure/ipacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3289267000

---

# Command: no

## Syntax
```
[no] <seqno>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | Sequence number |

**Command Mode:** /exec/configure/arpacl /exec/configure/ipgroup /exec/configure/ipv6group /exec/configure/portgroup /exec/configure/timerange

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1022135087

---

# Command: no

## Syntax
```
[no] <seqno>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | Sequence number |

**Command Mode:** /exec/configure/macacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3218213960

---

# Command: no

## Syntax
```
[no] <seqno>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | Sequence number |

**Command Mode:** /exec/configure/mplsacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1614672620

---

# Command: no

## Syntax
```
[no] <seqno>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | Sequence number |

**Command Mode:** /exec/configure/ipacl /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1090280328

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| ethertype | Configure match based on ethertype |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| ethertypeid | Configure the ethertype value |
| vlanid | (Optional) VLAN number |
| intfid | (Optional) Interface index |

**Command Mode:** /exec/configure/ipacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1025314723

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| ethertype | Configure match based on ethertype |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| ethertypeid | Configure the ethertype value |
| vlanid | (Optional) VLAN number |
| intfid | (Optional) Interface index |

**Command Mode:** /exec/configure/ipacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp5080976320

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| proto_igmp | Protocol |
| src_any | Any |
| src_addr | Source network address |
| src_wild | Source wildcard bits |
| src_prefix | Source network prefix |
| src_key_host | A single source host |
| src_host | Source address |

**Command Mode:** /exec/configure/ipacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4849584580

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| ethertype | Configure match based on ethertype |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| ethertypeid | Configure the ethertype value |
| vlanid | (Optional) VLAN number |
| intfid | (Optional) Interface index |

**Command Mode:** /exec/configure/ipacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2069405013

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| ipv6 | Any IPV6 protocol |
| proto | A protocol number |
| ipv6_other_proto | ipv6_other_proto |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| udf | (Optional) User defined field match |

**Command Mode:** /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2691693695

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| proto_tcp | Protocol |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| udf | (Optional) User defined field match |
| udf_name | (Optional) UDF name |
| udf_val | (Optional) UDF value to match |

**Command Mode:** /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4067899380

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| proto_udp | Protocol |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| udf | (Optional) User defined field match |
| udf_name | (Optional) UDF name |
| udf_val | (Optional) UDF value to match |

**Command Mode:** /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3414827610

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| proto_sctp | Protocol |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| udf | (Optional) User defined field match |
| udf_name | (Optional) UDF name |
| udf_val | (Optional) UDF value to match |

**Command Mode:** /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2607220904

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| proto_icmpv6 | Protocol |
| vlan | (Optional) Configure match based on vlan |
| ingress_intf | (Optional) Configure match based on ingress interface |
| vlan_priority | (Optional) Configure match based on priority |
| udf | (Optional) User defined field match |
| udf_name | (Optional) UDF name |
| udf_val | (Optional) UDF value to match |

**Command Mode:** /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2747214550

---

# Command: no

## Syntax
```
{ { [ <seqno> ] &#124; no } <permitdeny> { { [ <arp_request> ] req_ip { <sender1_ip_any> &#124; { { <sender1_host> <sender1_ip> &#124; {
 <sender1_net_ip> <sender1_ip_mask> } } } } mac { <sender1_mac_any> &#124; { { <sender1_mac_host> <sender1_mac> &#124; { <sender1_net_mac>
 <sender1_mac_mask> } } } } } &#124; { <arp_response> resp_ip { <sender2_ip_any> &#124; { { <sender2_host> <sender2_ip> &#124; { <sender2_net_ip>
 <sender2_ip_mask> } } } } { <target_ip_any> &#124; { { <target_host> <target_ip> &#124; { <target_net_ip> <target_ip_mask> } } } } mac
 { <sender2_mac_any> &#124; { { <sender2_mac_host> <sender2_mac> &#124; { <sender2_net_mac> <sender2_mac_mask> } } } } [ { <target_mac_any>
 &#124; { { <target_mac_host> <target_mac> &#124; { <target_net_mac> <target_mac_mask> } } } } ] } } [ <arp_log> ] [ capture session
 <session-id> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| req_ip | Any IP protocol |
| resp_ip | Any IP protocol |
| arp_request | (Optional) ARP_Request |
| arp_response | ARP_Response |
| sender1_ip_any | Any |
| sender1_host | Host |
| sender1_ip | IP address <a.b.c.d> |

**Command Mode:** /exec/configure/arpacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1965323361

---

# Command: no

## Syntax
```
{ [ <seqno> ] &#124; no } { <addr> <wild> &#124; <prefix> &#124; host <hostaddr> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| addr | A.B.C.D Network address of object-group member |
| wild | A.B.C.D wildcard |
| prefix | A.B.C.D/nn Network prefix of the object-group member |
| host | Host address of the object-group member |
| hostaddr | A.B.C.D Host address |

**Command Mode:** /exec/configure/ipgroup

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1896302962

---

# Command: no

## Syntax
```
{ [ <seqno> ] &#124; no } { <addr> <wild> &#124; <prefix> &#124; host <hostaddr> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| host | Host address of the object-group member |

**Command Mode:** /exec/configure/ipv6group

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3714025006

---

# Command: no

## Syntax
```
{ [ <seqno> ] &#124; no } { <_port_op> <port0_num> &#124; <_port_range> <port1_num> <port2_num> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| _port_op | Port operator |
| _port_range | Port range |
| port0_num | Port number |
| port1_num | Port number |
| port2_num | Port number |

**Command Mode:** /exec/configure/portgroup

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2382750802

---

# Command: no

## Syntax
```
(Optional) Sequence number
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| seqno | (Optional) Sequence number |
| no | Negate a command or set its defaults |
| permitdeny | Permit/deny |
| src_any | Any |
| src_addr | Source MAC address |
| src_wild | Source wildcard bits |
| dst_any | Any |
| dst_addr | Destination MAC address |
| dst_wild | Destination wildcard bits |
| mac_proto | (Optional) MAC protocol number |

**Command Mode:** /exec/configure/macacl

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3179815597

---

# Command: no

## Syntax
```
[no] { userprofile &#124; trustedCert &#124; CRLLookup &#124; user-switch-bind &#124; user-certdn-match &#124; user-pubkey-match }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| userprofile | Delete the userprofile |
| trustedCert | Delete the trustedCert |
| CRLLookup | Delete the CRLLookup |
| user-switch-bind | Delete the user-switch-bind |
| user-certdn-match | Delete the certificate matching |
| user-pubkey-match | Delete the pubkey matching |

**Command Mode:** /exec/configure/ldap/search

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4115855504

---

# Command: no

## Syntax
```
Negate a command or set its defaults
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |

**Command Mode:** /exec/configure/vsan-db

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp2750682709

---

# Command: node

## Syntax
```
[no] node [ ip <ip-addr> &#124; IPv6 <ip-addrv6> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| node | Catena device-group node |
| ip | (Optional) Catena device-group node IPv4 address |
| ip-addr | (Optional) Catena device-group node IP4 prefix in format i.i.i.i |
| IPv6 | (Optional) Catena device-group node IPv6 address |

**Command Mode:** /exec/configure/catena-device-grp

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp9642286310

---

# Command: node ip

## Syntax
```
[no] node { ip <ip-addr> &#124; IPv6 <ip-addrv6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| node | ITD node |
| ip | ITD node IPv4 address |
| ip-addr | ITD node IP4 prefix in format i.i.i.i |
| IPv6 | ITD node IPv6 address |

**Command Mode:** /exec/configure/itd-session-device-group

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, network, N-commands
**Command ID:** wp2801152154

---

# Command: node ip

## Syntax
```
[no] node { ip <ip-addr> &#124; IPv6 <ip-addrv6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| node | ITD node |
| ip | ITD node IPv4 address |
| ip-addr | ITD node IP4 prefix in format i.i.i.i |
| IPv6 | ITD node IPv6 address |

**Command Mode:** /exec/configure/itd-device-group

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, network, N-commands
**Command ID:** wp5551161300

---

# Command: node ip

## Syntax
```
[no] node { ip <ip-addr> &#124; IPv6 <ip-addrv6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| node | Configure nodes for PLB device group |
| ip | node IPv4 address |
| ip-addr | IP4 prefix in format i.i.i.i |
| IPv6 | node IPv6 address |

**Command Mode:** /exec/configure/plb-session-device-group

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, network, N-commands
**Command ID:** wp3961122609

---

# Command: node ip

## Syntax
```
[no] node { ip <ip-addr> &#124; IPv6 <ip-addrv6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| node | Configure nodes for PLB device group |
| ip | node IPv4 address |
| ip-addr | IP4 prefix in format i.i.i.i |
| IPv6 | node IPv6 address |

**Command Mode:** /exec/configure/plb-device-group

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, network, N-commands
**Command ID:** wp1081551034

---

# Command: npiv enable

## Syntax
```
[no] npiv enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| enable | Enable/Disable Nx port Id Virtualization (NPIV) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3920190873

---

# Command: npv auto-load-balance disruptive

## Syntax
```
[no] npv auto-load-balance disruptive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| npv | Config commands for FC N_port Virtualizer |
| auto-load-balance | configure auto load balancing among preferred external links |
| disruptive | enable disruptive auto load balancing among external links |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp8676934940

---

# Command: npv traffic-map server-interface external-interface

## Syntax
```
[no] npv traffic-map server-interface <if1> external-interface <interface>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| npv | Config commands for FC N_port Virtualizer |
| traffic-map | Configure NPV traffic engineering |
| server-interface | Configure server interface based traffic engineering |
| external-interface | Configure preferred external interface(s) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp3795001934

---

# Command: nsf await-redist-proto-convergence

## Syntax
```
{ [ no ] nsf await-redist-proto-convergence }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nsf | Non-stop forwarding |
| await-redist-proto-convergence | Specify whether EIGRP should wait for other protocols to converge before advertising routes |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4241952003

---

# Command: ntp access-group

## Syntax
```
[no] ntp access-group { peer &#124; serve-only &#124; serve &#124; query-only } <acl-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| access-group | NTP access-group |
| peer | access-group peer |
| serve | access-group serve |
| serve-only | access-group serve-only |
| query-only | access-group query-only |
| acl-name | Name of access list |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp3106154607

---

# Command: ntp access-group match-all

## Syntax
```
[no] ntp access-group match-all
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| access-group | NTP access-group |
| match-all | Scan ACLs present in all ntp access groups |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp2524989138

---

# Command: ntp allow private

## Syntax
```
[no] ntp allow { private &#124; control [ rate-limit <delay> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| allow | Enable/Disable the packets |
| private | Enable/Disable Private mode packets |
| control | Enable/Disable Control mode packets |
| rate-limit | (Optional) Rate-limit the control packets |
| delay | (Optional) Rate-limit delay (Default 3) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp1454791518

---

# Command: ntp authenticate

## Syntax
```
[no] ntp authenticate
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| authenticate | Enable/Disable authentication |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp3802252217

---

# Command: ntp authentication-key md5

## Syntax
```
[no] ntp authentication-key <number> md5 <md5> [ 0 &#124; 7 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| authentication-key | NTP authentication key |
| number | authentication key number (range 1-65535) |
| md5 | use md5 authentication scheme |
| md5 | MD5 string |
| 0 | (Optional) clear text |
| 7 | (Optional) encrypted |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp9592594100

---

# Command: ntp drop-aged-packet

## Syntax
```
[no] ntp drop-aged-packet
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ntp | NTP Configuration |
| drop-aged-packet | Enable or disable Riviera Timestamp Check. |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp2561815988

---

# Command: ntp logging

## Syntax
```
[no] ntp logging
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| logging | Enable/Disable logging of NTPD Events |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, management, N-commands
**Command ID:** wp2201262531

---

# Command: ntp master

## Syntax
```
[no] ntp master [ <stratum-no> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| master | Act as NTP master clock |
| stratum-no | (Optional) Stratum number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp1759218475

---

# Command: ntp passive

## Syntax
```
[no] ntp passive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| passive | NTP passive command |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp1274836827

---

# Command: ntp peer

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ntp | NTP Configuration |
| peer | NTP Peer address |
| host0 | Hostname/IP address of the NTP Peer |
| prefer | (Optional) Preferred Server |
| key | (Optional) Keyid to be used while communicating to this server |
| keyid | (Optional) Value of keyid 1-65535 |
| use-vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp3515093261

---

# Command: ntp rts-update

## Syntax
```
[no] ntp rts-update
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ntp | NTP Configuration |
| rts-update | Enable or disable RTS update to linecards. |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp2372196977

---

# Command: ntp server

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ntp | NTP Configuration |
| server | NTP server address |
| host0 | Hostname/IP address of the NTP Server |
| prefer | (Optional) Preferred Server |
| key | (Optional) Keyid to be used while communicating to this server |
| keyid | (Optional) Value of keyid 1-65535 |
| use-vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp2377027359

---

# Command: ntp source-interface

## Syntax
```
[no] ntp source-interface <interface>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| source-interface | Source interface sending NTP packets |
| interface | Source interface |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, system, N-commands
**Command ID:** wp6003741500

---

# Command: ntp source

## Syntax
```
[no] ntp source <ip-addr>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP Configuration |
| source | Source of NTP packets |
| ip-addr | IPv4/IPv6 address |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp7995616220

---

# Command: ntp sync-retry

## Syntax
```
ntp sync-retry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ntp | NTP configuration |
| sync-retry | Retry synchronization with configured servers |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp3279828657

---

# Command: ntp trusted-key

## Syntax
```
[no] ntp trusted-key <number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its default |
| ntp | NTP configuration |
| trusted-key | NTP trusted-key |
| number | trusted-key number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, system, N-commands
**Command ID:** wp1184384991

---

# Command: nv overlay evpn

## Syntax
```
[no] nv overlay evpn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nv | Command to enable/disable features |
| overlay | Command to enable/disable features |
| evpn | Enable/Disable Ethernet VPN (EVPN) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp5285712630

---

# Command: nve event-history size

## Syntax
```
nve event-history { <buffer-name> } size { <size_in_text> &#124; <size_in_bytes> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nve | Display NVE information |
| event-history | Configure the event-history buffers |
| buffer-name | Event history buffer whose size is to be configured |
| size | Configure the buffer sizes |
| size_in_text | Size of event history buffer |
| size_in_bytes | Size in bytes in the renage 1-5000000 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp4269737461

---

# Command: nve interface remap-replication-servers

## Syntax
```
nve interface <nve-if> remap-replication-servers
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nve | Configure NVE information |
| interface | Interface |
| nve-if | NVE interface |
| remap-replication-servers | Remap Replication servers to VNIs |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp3466192392

---

# Command: nve interface replication-server up

## Syntax
```
nve interface <nve-if> replication-server <rep-addr> { up &#124; down }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nve | Configure NVE information |
| interface | Interface |
| nve-if | NVE interface |
| replication-server | Configure a replication server |
| rep-addr | Replication Server IP Address |
| up | mark replication-server up |
| down | mark replication-server down |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp6391240130

---

# Command: nve oam mode draft-pang

## Syntax
```
[no] nve oam mode draft-pang
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nve | VxLAN functionality |
| oam | VxLAN OAM functionality |
| mode | Choose operation mode for OAM |
| draft-pang | OAM implementation as per Draft Pang |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1698005029

---

# Command: nxapi certificate

## Syntax
```
{ nxapi certificate { { httpskey { keyfile <uri0> [ password <passphrase> ] } } &#124; { httpscrt { certfile <uri1> } } &#124; { enable
 } } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nxapi | Configure nxapi |
| certificate | Https certificate configuration |
| httpskey | Https private key |
| httpscrt | Https certificate |
| keyfile | Https key file |
| certfile | Https certificate file |
| password | (Optional) Https encrypted key passphrase |
| enable | Enable the current certificate |
| uri0 | File containing https private key for the user |
| passphrase | (Optional) Https encrypted private key passphrase |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3871698150

---

# Command: nxapi flow

## Syntax
```
{ [ no ] nxapi flow }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nxapi | Configure nxapi |
| flow | allow frontend to access /sys/flow/ |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp6129402450

---

# Command: nxapi http port

## Syntax
```
{ nxapi { http &#124; https } port <s0> } &#124; { no nxapi { http &#124; https } } &#124; { no nxapi { http &#124; https } port <s0> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nxapi | Configure nxapi |
| http | Http configuration |
| https | Https configuration |
| port | Port number |
| s0 | Port number. Please do not use well-known protocol ports |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp4109637450

---

# Command: nxapi ssl ciphers weak

## Syntax
```
{ [ no ] nxapi ssl ciphers weak }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nxapi | Configure nxapi |
| ssl | Configure ssl parameters |
| ciphers | Configure allowed ciphers for ssl |
| weak | Allow weak ciphers |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, network, N-commands
**Command ID:** wp2940523679

---

# Command: nxapi ssl protocols

## Syntax
```
{ nxapi ssl protocols <prot_string> } &#124; { no nxapi ssl protocols }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nxapi | Configure nxapi |
| ssl | Configure ssl parameters |
| protocols | Configure allowed ssl protocols |
| prot_string | String of supported protocols, Ex: TLSv1 TLSv1.1 TLSv1.2 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp8710004900

---

# Command: nxapi use-vrf management default

## Syntax
```
{ nxapi use-vrf { management &#124; default &#124; <vrf_name> } } &#124; { no nxapi use-vrf { management &#124; default &#124; <vrf_name> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| nxapi | Configure nxapi |
| use-vrf | vrf to be used for nxapi communication |
| management | management vrf |
| default | default vrf |
| vrf_name | name of the vrf |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, overlay, N-commands
**Command ID:** wp1953794244

---

# Command: nxsdk profile

## Syntax
```
[no] nxsdk profile <nxsdk-profile-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nxsdk | NXOS SDK |
| profile | service profile |
| nxsdk-profile-name | NxSDK service profile name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp1609274144

---

# Command: nxsdk remote port

## Syntax
```
[no] nxsdk remote port <port> [ namespace { <vrf-name> &#124; <vrf-known-name> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| nxsdk | NXOS SDK |
| remote | To run NX-SDK service as a remote service |
| port | Port to accept remote NX-SDK connections |
| port | Port |
| namespace | (Optional) Namespace to run the remote server on. Default is Vrf: Default |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, interface, N-commands
**Command ID:** wp8745570080

---

# Command: nxsdk service-name

## Syntax
```
[no] nxsdk service-name <nxsdk-service-name> [ profile <nxsdk-profile-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| nxsdk | NXOS SDK |
| service-name | Complete path and name of file to execute |
| nxsdk-service-name | Service name |
| profile | (Optional) Service profile |
| nxsdk-profile-name | (Optional) Name of the profile |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01110.html
**Tags:** config-mode, N-commands
**Command ID:** wp3603191592

---

