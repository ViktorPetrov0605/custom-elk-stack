# Chapter: O Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_01111.html
**Type:** Configuration Commands  
**Chapter:** Group-1111 Commands  
**Total Commands:** 38

## Command List

- `oam-channel`
- `object-group ip address`
- `object-group ip port`
- `object-group ipv6 address`
- `object-group udp relay ip address`
- `object-group udp relay ip address`
- `object-track`
- `of-port interface`
- `on-demand color`
- `openflow`
- `operation-packet-priority normal`
- `option exporter-stats timeout`
- `option interface-table timeout`
- `orib event-history`
- `orib orib_api_init`
- `ospfv3 authentication`
- `ospfv3 bfd`
- `ospfv3 cost`
- `ospfv3 dead-interval`
- `ospfv3 event-history`
- `ospfv3 event-history cli size`
- `ospfv3 event-history detail`
- `ospfv3 event-history detail`
- `ospfv3 hello-interval`
- `ospfv3 instance`
- `ospfv3 mtu-ignore`
- `ospfv3 network broadcast`
- `ospfv3 network point-to-point`
- `ospfv3 passive-interface`
- `ospfv3 priority`
- `ospfv3 retransmit-interval`
- `ospfv3 shutdown`
- `ospfv3 transmit-delay`
- `other-config-flag`
- `otv-isis`
- `overlay-encapsulation`
- `overwrite-vlan`
- `owner`

---

## Detailed Command Reference

# Command: oam-channel

## Syntax
```
{ oam-channel <val> } &#124; { no oam-channel }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| oam-channel | oam-channel used |
| val | 2 - nvo3 tissa |

**Command Mode:** /exec/configure/configngoamprofile

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1360103720

---

# Command: object-group ip address

## Syntax
```
[no] object-group ip address <name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| object-group | Configure ACL object groups |
| ip | IP Object groups |
| address | Address object group |
| name | object-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, network, O-commands
**Command ID:** wp9587778550

---

# Command: object-group ip port

## Syntax
```
[no] object-group ip port <name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| object-group | Configure ACL object groups |
| ip | IP Object groups |
| port | IP port object group (can be used in IPv4 and IPv6 access-lists) |
| name | object-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, network, O-commands
**Command ID:** wp2037883887

---

# Command: object-group ipv6 address

## Syntax
```
[no] object-group ipv6 address <name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| object-group | Configure ACL object groups |
| ipv6 | IPv6 Object groups |
| address | Address object group |
| name | object-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, network, O-commands
**Command ID:** wp2519081474

---

# Command: object-group udp relay ip address

## Syntax
```
object-group udp relay ip address <obj-grp-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| object-group | Configure object groups |
| udp | Configure UDP |
| relay | Configure UDP Relay |
| ip | IP Object groups |
| address | Address object group |
| obj-grp-name | object-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, network, O-commands
**Command ID:** wp2066220227

---

# Command: object-group udp relay ip address

## Syntax
```
[no] object-group udp relay ip address <obj-grp-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| object-group | Configure object groups |
| udp | Configure UDP |
| relay | Configure UDP Relay |
| ip | IP Object groups |
| address | Address object group |
| obj-grp-name | object-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, network, O-commands
**Command ID:** wp3243778023

---

# Command: object-track

## Syntax
```
[no] object-track <object-number> [ decrement <value> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| object-track | Associates track object to VRRP group |
| object-number | Set the object number to the group |
| decrement | (Optional) Decrements vrrp group priority when tracked object goes down |
| value | (Optional) Set the value to decrement from priority |

**Command Mode:** /exec/configure/if-eth-any/vrrpv3

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1892907887

---

# Command: of-port interface

## Syntax
```
[no] of-port interface <ifname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| of-port | Add interfaces to openflow switch |
| interface | Interface |
| ifname | interface name |

**Command Mode:** /exec/configure/openflow/switch

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, O-commands
**Command ID:** wp1094633379

---

# Command: on-demand color

## Syntax
```
[no] on-demand color <color>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| on-demand | Configure on-demand color |
| color | Color |
| color | Color |

**Command Mode:** /exec/configure/sr/te

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1647135515

---

# Command: openflow

## Syntax
```
[no] openflow
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| openflow | OpenFlow configuration |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1759577154

---

# Command: operation-packet-priority normal

## Syntax
```
{ { no &#124; default } operation-packet-priority &#124; operation-packet-priority { normal &#124; high } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| operation-packet-priority | Set operation packet properties |
| high | Priority high |
| normal | Priority normal |

**Command Mode:** /exec/configure/ip-sla/jitter

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, qos, O-commands
**Command ID:** wp3086322424

---

# Command: option exporter-stats timeout

## Syntax
```
{ [ no ] option exporter-stats timeout <time> &#124; no option exporter-stats timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| option | Version 9 Option Templates and Data |
| exporter-stats | Exporter Statistics Option |
| timeout | Option resend time |
| time | Time in seconds |

**Command Mode:** /exec/configure/nfm-exporter-v9

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, system, O-commands
**Command ID:** wp4307397370

---

# Command: option interface-table timeout

## Syntax
```
{ [ no ] option interface-table timeout <time> &#124; no option interface-table timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| option | Version 9 Option Templates and Data |
| interface-table | Interface Table Option |
| timeout | Option resend time |
| time | Time in seconds |

**Command Mode:** /exec/configure/nfm-exporter-v9

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, system, O-commands
**Command ID:** wp2484078872

---

# Command: orib event-history

## Syntax
```
[no] orib event-history { cli &#124; ipc &#124; uroute &#124; mroute &#124; mroute_only &#124; uhw &#124; mhw &#124; ha &#124; internal } { size { <size_in_text>
 &#124; <size_in_kbytes> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| orib | Display ORIB information |
| event-history | ORIB event logs |
| cli | ORIB cli logs |
| ipc | ORIB ipc logs |
| uroute | ORIB unicast route logs |
| mroute | ORIB multicast route logs |
| mroute_only | ORIB multicast route logs without mhw |
| uhw | ORIB unicast platform logs |
| mhw | ORIB multicast platform logs |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1113253735

---

# Command: orib orib_api_init

## Syntax
```
{ orib orib_api_init <client-name> } &#124; { orib orib_api_close } &#124; { orib orib_add_route <client-name> <mac> [ <nh> &#124; <nh6>
 ] <if-name> } &#124; { orib orib_delete_route <client-name> <mac> [ <nh> &#124; <nh6> ] <if-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| orib | Use ORIB API routines from OTV process |
| orib_api_init | Call orib_api_init() from the OTV process |
| orib_api_close | Call orib_api_close() from the OTV process |
| orib_add_route | Call orib_add_route() from OTV process |
| orib_delete_route | Call orib_delete_route() from OTV process |
| client-name | Client name registered to ORIB process |
| mac | VLAN-ID/MAC Address tuple in vvvv-aaaa.bbbb.cccc format |
| nh | (Optional) Next-hop IPv4 address |
| if-name | Next-hop interface (iod) |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp2857125352

---

# Command: ospfv3 authentication

## Syntax
```
ospfv3 authentication { disable &#124; ipsec spi <spi_id> { md5 <akey> &#124; sha1 <akey> } } &#124; no ospfv3 authentication { disable &#124;
 ipsec spi <spi_id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| authentication | Enable Authentication |
| disable | Disable Authentication |
| ipsec | IPSec |
| spi | Security Parameter Index |
| spi_id | SPI Value |
| md5 | Use the MD5 algorithim |
| akey | Authentication Key |
| sha1 | Use the SHA1 algorithim |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp1017925167

---

# Command: ospfv3 bfd

## Syntax
```
[no] ospfv3 bfd [ disable ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| bfd | Enable BFD on this interface |
| disable | (Optional) Disable BFD on this interface |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, bfd, O-commands
**Command ID:** wp1959657607

---

# Command: ospfv3 cost

## Syntax
```
{ ospfv3 cost <cost> } &#124; { no ospfv3 cost [ <cost> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| cost | Cost associated with interface |
| cost | Cost value |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp2376163542

---

# Command: ospfv3 dead-interval

## Syntax
```
{ ospfv3 dead-interval <interval> } &#124; { no ospfv3 dead-interval [ <interval> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| dead-interval | Dead interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp2525959438

---

# Command: ospfv3 event-history

## Syntax
```
[ no ospfv3 event-history { adjacency &#124; event &#124; ha &#124; flooding &#124; lsa &#124; spf &#124; redistribution &#124; hello &#124; spf-trigger } ] &#124; [ ospfv3
 event-history { adjacency &#124; event &#124; ha &#124; flooding &#124; lsa &#124; spf &#124; redistribution &#124; hello &#124; spf-trigger } size { <size_in_text>
 &#124; <size_in_Kbytes> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | (Optional) Debugging functions |
| event-history | (Optional) log debug events into event history buffer |
| adjacency | (Optional) Adjacency formation logs |
| event | (Optional) Internal event logs |
| ha | (Optional) HA and GR logs |
| flooding | (Optional) LSA flooding logs |
| lsa | (Optional) LSA generation and databse logs |
| spf | (Optional) SPF calculation logs |
| redistribution | (Optional) Redistribution logs |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp2194235828

---

# Command: ospfv3 event-history cli size

## Syntax
```
[ no ospfv3 event-history cli ] &#124; [ ospfv3 event-history cli size { <size_in_text> &#124; <size_in_Kbytes> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | (Optional) Debugging functions |
| event-history | (Optional) log debug events into event history buffer |
| cli | (Optional) Cli logs |
| size | (Optional) Configure the size of the event-hist buffer |
| size_in_text | (Optional) Buffer size |
| size_in_Kbytes | (Optional) Size of the file in kbytes |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp5111646350

---

# Command: ospfv3 event-history detail

## Syntax
```
[no] ospfv3 event-history detail
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | Debugging functions |
| event-history | log debug events into event history buffer |
| detail | Detailed event history buffer |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp3966931790

---

# Command: ospfv3 event-history detail

## Syntax
```
[ no ospfv3 event-history detail ] &#124; [ ospfv3 event-history detail size { <size_in_text> &#124; <size_in_Kbytes> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | (Optional) Debugging functions |
| event-history | (Optional) log debug events into event history buffer |
| detail | (Optional) Detailed event history buffer |
| size | (Optional) Configure the size of the event-hist buffer |
| size_in_text | (Optional) Buffer size |
| size_in_Kbytes | (Optional) Size of the file in kbytes |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp2887515764

---

# Command: ospfv3 hello-interval

## Syntax
```
{ ospfv3 hello-interval <interval> } &#124; { no ospfv3 hello-interval [ <interval> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| hello-interval | Hello interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp2070534670

---

# Command: ospfv3 instance

## Syntax
```
{ ospfv3 instance <instance-id> } &#124; { no ospfv3 instance [ <instance-id> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| instance | Instance identifier |
| instance-id | Instance identifier value |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp3325874797

---

# Command: ospfv3 mtu-ignore

## Syntax
```
[no] ospfv3 mtu-ignore
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| mtu-ignore | Disable OSPF MTU mismatch detection |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp1846896550

---

# Command: ospfv3 network broadcast

## Syntax
```
{ ospfv3 network { broadcast &#124; point-to-point } } &#124; { no ospfv3 network [ { broadcast &#124; point-to-point } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| network | Network type |
| broadcast | Specify OSPF broadcast multi-access network |
| point-to-point | Specify OSPF point-to-point network |

**Command Mode:** /exec/configure/if-broadcast /exec/configure/if-p2p /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp3388369205

---

# Command: ospfv3 network point-to-point

## Syntax
```
{ ospfv3 network point-to-point } &#124; { no ospfv3 network [ point-to-point ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| network | Network type |
| point-to-point | Specify OSPF point-to-point network |

**Command Mode:** /exec/configure/if-loopback

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp8328900610

---

# Command: ospfv3 passive-interface

## Syntax
```
[ default &#124; no ] ospfv3 passive-interface
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | (Optional) Undo a command |
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| passive-interface | Suppress routing updates on the interface |

**Command Mode:** /exec/configure/if-broadcast /exec/configure/if-p2p /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, routing, O-commands
**Command ID:** wp1730620453

---

# Command: ospfv3 priority

## Syntax
```
{ ospfv3 priority <prio> } &#124; { no ospfv3 priority [ <prio> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| priority | Router priority |
| prio | Router priority |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, qos, O-commands
**Command ID:** wp2497442633

---

# Command: ospfv3 retransmit-interval

## Syntax
```
{ ospfv3 retransmit-interval <interval> } &#124; { no ospfv3 retransmit-interval [ <interval> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| retransmit-interval | Packet retransmission interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp3438006902

---

# Command: ospfv3 shutdown

## Syntax
```
[no] ospfv3 shutdown
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| shutdown | Shutdown ospf on this interface |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp3960554257

---

# Command: ospfv3 transmit-delay

## Syntax
```
{ ospfv3 transmit-delay <delay> } &#124; { no ospfv3 transmit-delay [ <delay> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| ospfv3 | OSPFv3 configuration commands |
| transmit-delay | Packet transmission delay |
| delay | (seconds) |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-gre-tunnel /exec/configure/if-mpls-tunnel /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp1972836078

---

# Command: other-config-flag

## Syntax
```
[no] other-config-flag <state>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |

**Command Mode:** /exec/configure/config-ra-guard

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp3086214641

---

# Command: otv-isis

## Syntax
```
otv-isis <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| otv-isis | Intermediate System to Intermediate System (IS-IS) |
| tag | Routing process tag |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, routing, O-commands
**Command ID:** wp1076868268

---

# Command: overlay-encapsulation

## Syntax
```
overlay-encapsulation <encap-type> [ tunnel-control-frames [ <layer2-prot> ] ] &#124; no overlay-encapsulation
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| overlay-encapsulation | NVE Overlay Encapsulation |
| encap-type | Configure encapsulation type |
| tunnel-control-frames | (Optional) tunnel protocol |
| layer2-prot | (Optional) configure specific protocol |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp1566294222

---

# Command: overwrite-vlan

## Syntax
```
[no] overwrite-vlan <ow-vlan-id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| overwrite-vlan | Overwrite the system generated vlan |

**Command Mode:** /exec/configure/static-host/vni

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, interface, O-commands
**Command ID:** wp4028758539

---

# Command: owner

## Syntax
```
{ { no &#124; default } owner &#124; owner <text> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| owner | Owner of Entry |
| text | Owner String |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/jitter /exec/configure/ip-sla/tcp /exec/configure/ip-sla/icmpEcho /exec/configure/ip-sla/dns
 /exec/configure/ip-sla/fabricPathEcho /exec/configure/ip-sla/http

**Source:** b_N9K_Config_Commands_93x_chapter_01111.html
**Tags:** config-mode, O-commands
**Command ID:** wp8315896580

---

