# Chapter: V Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010110.html
**Type:** Configuration Commands  
**Chapter:** Group-10110 Commands  
**Total Commands:** 92

## Command List

- `validate-json`
- `validate-xml`
- `validate-xml`
- `vdc`
- `vdc`
- `vdc combined-hostname`
- `vdc_id`
- `vdc resource template`
- `vdc suspend`
- `vdc suspend`
- `vdp dot1q default static`
- `vdp dot1q static`
- `vdp vni default static`
- `vdp vni static`
- `verify-data`
- `verify-host`
- `verify`
- `verify profile`
- `verify verbose`
- `version`
- `version 9`
- `virtual-rmac`
- `virtual-service`
- `virtual-service`
- `virtual-service`
- `virtual-service move name log to`
- `virtual-service reset force`
- `virtual IPv6`
- `virtual IPv6`
- `virtual ip`
- `virtual ip`
- `virtual peer-link destination source`
- `vlan-consistency-check`
- `vlan-pruning enable`
- `vlan2`
- `vlan`
- `vlan`
- `vlan access-map`
- `vlan configuration`
- `vlan designated priority`
- `vlan filter vlan`
- `vlan root priority`
- `vmtracker connection`
- `vmtracker connection refresh`
- `vmtracker enable`
- `vmtracker fabric auto-config`
- `vn-segment`
- `vni`
- `vni`
- `vni`
- `vni default dynamic`
- `vni l2`
- `vpc`
- `vpc domain`
- `vpc orphan-port suspend`
- `vpc peer-link`
- `vpc role preempt`
- `vpn`
- `vpn id`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf`
- `vrf context`
- `vrf default static`
- `vrf member`
- `vrf member`
- `vrf static`
- `vrrp`
- `vrrp bfd`
- `vrrpv2`
- `vrrpv3`
- `vrrpv3 address-family`
- `vrrpv3 address-family`
- `vrrs leader`
- `vrrs pathway`
- `vsh`
- `vtp`
- `vtp domain`
- `vtp file`
- `vtp password`
- `vtp pruning`
- `vtp version`

---

## Detailed Command Reference

# Command: validate-json

## Syntax
```
&#124; validate-json
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| validate-json | validate json output according to .xsd definitions |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3022607430

---

# Command: validate-xml

## Syntax
```
&#124; validate-xml
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| validate-xml | validate an xml output according to .xsd definitions |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1556880971

---

# Command: validate-xml

## Syntax
```
&#124; validate-xml
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| validate-xml | validate an xml output according to .xsd definitions |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2584700986

---

# Command: vdc

## Syntax
```
[no] vdc <e-vdc> [ force ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdc | Manage Virtual Device Context |
| e-vdc | Enter Virtual Device Context <vdc-id> |
| force | (Optional) Force ungraceful cleanup |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3427504500

---

# Command: vdc

## Syntax
```
vdc <e-vdc> [ id <new_id> ] [ type <vtype> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vdc | Manage Virtual Device Context |
| e-vdc | Enter Virtual Device Context <vdc-id> |
| id | (Optional) force this vdc into a specific id |
| new_id | (Optional) force this vdc into a specific id |
| type | (Optional) Create vdc with a special set of services |
| vtype | (Optional) type of vdc |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp4189694856

---

# Command: vdc combined-hostname

## Syntax
```
[no] vdc combined-hostname
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vdc | Manage Virtual Device Context |
| combined-hostname | The hostname of non-default vdcs will be <default vdc name>-<nondefault vdc name> |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1438807476

---

# Command: vdc_id

## Syntax
```
[no] vdc_id <id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdc_id | Manage Virtual Device Context |
| id | Enter Virtual Device Context <vdc-id> |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2765532369

---

# Command: vdc resource template

## Syntax
```
[no] vdc resource template { <name> &#124; <res-mgr-template-known-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vdc | Manage Virtual Device Context |
| resource | Configure resource template |
| template | Configure resource template |
| name | Resource template name |
| res-mgr-template-known-name | Resource template name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp4117759430

---

# Command: vdc suspend

## Syntax
```
[no] vdc <en-vdc> suspend
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vdc | Manage Virtual Device Context |
| en-vdc | Enter Virtual Device Context <vdc-id> |
| suspend | Put the vdc in a paused stated. When resumed vdc will use its startup config |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1175736824

---

# Command: vdc suspend

## Syntax
```
vdc <en-vdc> suspend
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vdc | Manage Virtual Device Context |
| en-vdc | Enter Virtual Device Context <vdc-id> |
| suspend | Put the vdc in a paused state. When resumed vdc will come up with its startup config |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1529380696

---

# Command: vdp dot1q default static

## Syntax
```
{ vdp dot1q default { static <profile-name> &#124; dynamic } } &#124; { no vdp dot1q default }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdp | VDP protocol triggers |
| static | Static Profile Map: Configure profile name via CLI |
| profile-name | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |
| dot1q | Dot1Q Encapsulation |
| default | Default (wildcard). Match any dot1q when there is no specific dot1q mapping configured |

**Command Mode:** /exec/configure/profile-map /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1986576731

---

# Command: vdp dot1q static

## Syntax
```
{ vdp dot1q <vlan-id> { static <profile-name> &#124; dynamic } } &#124; { no vdp dot1q <vlan-id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdp | VDP protocol triggers |
| static | Static Profile Map: Configure profile name via CLI |
| profile-name | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |
| dot1q | Dot1Q Encapsulation |

**Command Mode:** /exec/configure/profile-map /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2299905594

---

# Command: vdp vni default static

## Syntax
```
{ vdp vni default { static <profile-name> &#124; dynamic } } &#124; { no vdp vni default }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdp | VDP protocol triggers |
| vni | Virtual Network Identifier |
| static | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |
| profile-name | Static Profile Map: Configure profile name via CLI |
| default | Default (wildcard). Match any vni when there is no specific vni mapping configured |

**Command Mode:** /exec/configure/profile-map /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp7126774890

---

# Command: vdp vni static

## Syntax
```
{ vdp vni <vni-id> { static <profile-name> &#124; dynamic } } &#124; { no vdp vni <vni-id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vdp | VDP protocol triggers |
| vni | Virtual Network Identifier |
| static | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |
| profile-name | Static Profile Map: Configure profile name via CLI |

**Command Mode:** /exec/configure/profile-map /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3236325768

---

# Command: verify-data

## Syntax
```
{ { no &#124; default } verify-data &#124; verify-data }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| verify-data | Verify data |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/jitter /exec/configure/ip-sla/icmpEcho

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2337481253

---

# Command: verify-host

## Syntax
```
{ verify-host &#124; no verify-host }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| verify-host | Verify host reachability - payload info mandatory |

**Command Mode:** /exec/configure/configngoamconnectcheck

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2298246560

---

# Command: verify

## Syntax
```
verify
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| verify | Verify the current configuration session |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2857708330

---

# Command: verify profile

## Syntax
```
verify profile <all_conf_profile_name> [ __readonly__ TABLE_profile_name <missing_param> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| verify | Verify the instance with a configuration profile |
| profile | Name of the configuration profile |
| all_conf_profile_name | Enter the name of configuration profile |
| __readonly__ | (Optional) |
| TABLE_profile_name | (Optional) |
| missing_param | (Optional) |

**Command Mode:** /exec/configure/param-inst

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp9043832300

---

# Command: verify verbose

## Syntax
```
verify verbose
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| verify | Verify the current configuration session |
| verbose | Verify the current configuration session with more details |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1722457777

---

# Command: version

## Syntax
```
[no] version <s0> [ <s1> ] [ <s2> ] [ <s3> ] [ <s4> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| version | Version info |
| s0 | Version |
| s1 | (Optional) Version1 |
| s2 | (Optional) Version2 |
| s3 | (Optional) Version3 |
| s4 | (Optional) Version4 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp8523963790

---

# Command: version 9

## Syntax
```
version 9
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| version | Specify the export version |
| 9 | Version 9 Export |

**Command Mode:** /exec/configure/nfm-exporter

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3277829400

---

# Command: virtual-rmac

## Syntax
```
[no] virtual-rmac <mac> &#124; no virtual-rmac
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual-rmac | Static Virtual RMAC configuration |
| mac | Specify Virtual Router MAC Address |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1585117111

---

# Command: virtual-service

## Syntax
```
[no] virtual-service
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual-service | Virtual service global settings |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2263699531

---

# Command: virtual-service

## Syntax
```
[no] virtual-service <virt_serv_name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual-service | Configure a virtual service |
| virt_serv_name | Virtual service name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2106232117

---

# Command: virtual-service

## Syntax
```
virtual-service { { install name <virt_serv_name> package <file_uri> [ media <target_media> ] } &#124; { upgrade name <virt_serv_name>
 package <file_uri> } &#124; { uninstall name <virt_serv_name> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| virtual-service | Virtualization manager actions |
| install | Add a virtual service to install database |
| upgrade | Upgrade a virtual service package to a different version |
| name | Name of the virtual service |
| virt_serv_name | Virtual service name |
| package | Package location |
| file_uri | File name (with .ova extension) for the virtual service |
| media | (Optional) Target media to use to explode the virtual service package |
| target_media | (Optional) Target media |
| uninstall | Remove a virtual service from the install database |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3539967700

---

# Command: virtual-service move name log to

## Syntax
```
virtual-service move name <virt_serv_name> { log &#124; core } to <dir_uri>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| virtual-service | Virtualization service actions |
| move | Move a virtual service log or core files |
| name | Name of the virtual service |
| virt_serv_name | Name of existing virtual service |
| log | Move log files |
| core | Move core files |
| to | Destination directory to move log or core files to |
| dir_uri | Destination directory name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1587104533

---

# Command: virtual-service reset force

## Syntax
```
virtual-service reset force
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| virtual-service | Virtualization service actions |
| reset | Virtualization reset commands |
| force | Force a non-recoverable reset of all virtualization files |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2328074858

---

# Command: virtual IPv6

## Syntax
```
[no] virtual IPv6 { <ip-addr> { <prefix> &#124; <netmask> } } [ ip &#124; { { udp &#124; tcp } { <port_num> &#124; any } } ] [ { arp &#124; advertise
 } { enable &#124; disable } ] [ device-group <group-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual | Configure Virtual IP of server nodes for redirection |
| IPv6 | IPv6 address |
| prefix | IPV6 prefix length |
| ip | (Optional) IP address |
| udp | (Optional) UDP port |
| tcp | (Optional) TCP port |
| port_num | (Optional) Port Number |
| any | (Optional) Any Port Number |
| arp | (Optional) ARP |

**Command Mode:** /exec/configure/plb

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, network, V-commands
**Command ID:** wp1213316806

---

# Command: virtual IPv6

## Syntax
```
[no] virtual IPv6 { <ip-addr> { <prefix> &#124; <netmask> } } [ { <proto> { <port_num> &#124; <port_any> } } ] [ { advertise } { enable
 &#124; disable } [ active ] ] [ device-group <dgrp_name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual | ITD virtual ip configuration |
| IPv6 | ITD virtual IPv6 |
| prefix | IPV6 prefix length |
| proto | (Optional) Protocol for vip |
| port_num | (Optional) Port Number |
| port_any | (Optional) Port any |
| advertise | (Optional) advertise |
| enable | (Optional) Enable |
| disable | (Optional) Disable |

**Command Mode:** /exec/configure/itd

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, network, V-commands
**Command ID:** wp2481600315

---

# Command: virtual ip

## Syntax
```
[no] virtual ip { <ip-addr> <ip-mask> } [ ip &#124; { { udp &#124; tcp } { <port_num> &#124; any } } ] [ { arp &#124; advertise } { enable &#124; disable
 } ] [ device-group <group-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual | Configure Virtual IP of server nodes for redirection |
| ip | IPv4 address |
| ip-addr | IPv4 prefix in format i.i.i.i |
| ip-mask | IPv4 prefix mask in format m.m.m.m |
| ip | (Optional) IPv4 address |
| udp | (Optional) UDP port |
| tcp | (Optional) TCP port |
| port_num | (Optional) Port Number |
| any | (Optional) Any Port Number |

**Command Mode:** /exec/configure/plb

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, network, V-commands
**Command ID:** wp2278025837

---

# Command: virtual ip

## Syntax
```
[no] virtual ip { <ip-addr> <ip-mask> } [ { <proto> { <port_num> &#124; <port_any> } } ] [ { advertise } { enable &#124; disable } [
 active ] ] [ device-group <dgrp_name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| virtual | ITD virtual ip configuration |
| ip | ITD virtual ip |
| ip-addr | IP address in format i.i.i.i |
| ip-mask | IP network mask in format m.m.m.m |
| proto | (Optional) Protocol for vip |
| port_num | (Optional) Port Number |
| port_any | (Optional) Port any |
| advertise | (Optional) advertise |
| enable | (Optional) Enable |

**Command Mode:** /exec/configure/itd

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, network, V-commands
**Command ID:** wp2700794489

---

# Command: virtual peer-link destination source

## Syntax
```
virtual peer-link destination <dst-ip> source <src-ip> [ dscp <dscp-val> ] &#124; no virtual peer-link
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| virtual | Virtual peer-link |
| peer-link | peer-link to peer switch |
| destination | specify destination ip address of peer switch |
| dst-ip | IPv4 address (A.B.C.D) of destination |
| source | source interface for peer-link |
| src-ip | IPv4 address (A.B.C.D) of source |
| dscp | (Optional) Set dscp value |
| dscp-val | (Optional) dscp value |

**Command Mode:** /exec/configure/vpc-domain

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, vpc, V-commands
**Command ID:** wp3171915794

---

# Command: vlan-consistency-check

## Syntax
```
[no] vlan-consistency-check
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan-consistency-check | enable vlan consistency check |

**Command Mode:** /exec/configure/evpn-esi-mh

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp5230818090

---

# Command: vlan-pruning enable

## Syntax
```
vlan-pruning enable &#124; no vlan-pruning enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vlan-pruning | Configure Vlan-pruning feature |
| enable | Set the mode for vlan-pruning |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp9060622940

---

# Command: vlan2

## Syntax
```
[no] vlan2 <vlan-id-create-delete>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan2 | Vlan commands |
| vlan-id-create-delete | VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp3153308854

---

# Command: vlan

## Syntax
```
[no] vlan <vlan-range>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan | add vlan to vlan group |
| vlan-range | range of vlans |

**Command Mode:** /exec/configure/itd-vlan-grp

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp1237336750

---

# Command: vlan

## Syntax
```
[no] vlan <vlan-range>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan | vlan |
| vlan-range | range of vlans |

**Command Mode:** /exec/configure/smartc /exec/configure/smartc

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp2543705190

---

# Command: vlan access-map

## Syntax
```
[no] vlan access-map <name> [ <seqno> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan | Vlan commands |
| name | List name |
| access-map | Configure a VLAN access map |
| seqno | (Optional) Sequence number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp1673697375

---

# Command: vlan configuration

## Syntax
```
[no] vlan configuration <vlan-id-create-delete>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan | Vlan commands |
| configuration | vlan feature configuration mode |
| vlan-id-create-delete | VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp1265290341

---

# Command: vlan designated priority

## Syntax
```
{ vlan <vlan-id> &#124; bridge-domain <bd-id> } designated priority <prio> &#124; no { vlan <vlan-id> &#124; bridge-domain <bd-id> } designated
 priority [ <prio> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vlan | VLAN Switch Spanning Trees |
| bridge-domain | Bridge-Domain Switch Spanning Trees |
| vlan-id | vlan range, Example: 1,3-5,7,9-11 |
| bd-id | Bridge-Domain range, Example: 2,4-5,7,9-11 |
| designated | Set the designated bridge priority for the spanning tree |
| priority | Set the bridge priority for the spanning tree |
| prio | bridge priority in increments of 4096 |

**Command Mode:** /exec/configure/spanning-tree/pseudo

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, qos, V-commands
**Command ID:** wp8456504420

---

# Command: vlan filter vlan

## Syntax
```
[no] vlan filter <name> { vlan-list <vlans> &#124; vlan-list-include-reserved <vlans-include-reserved> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vlan | Vlan commands |
| filter | Specify access control for packets |
| name | List name |
| vlan-list | Specify list of VLANs to apply access control |
| vlans | List of VLANs |
| vlan-list-include-reserved | Specify list of VLANs to apply access control |
| vlans-include-reserved | List of VLANs |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, V-commands
**Command ID:** wp3795729256

---

# Command: vlan root priority

## Syntax
```
{ vlan <vlan-id> &#124; bridge-domain <bd-id> } root priority <prio> &#124; no { vlan <vlan-id> &#124; bridge-domain <bd-id> } root priority
 [ <prio> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vlan | VLAN Switch Spanning Trees |
| bridge-domain | Bridge-Domain Switch Spanning Trees |
| vlan-id | vlan range, Example: 1,3-5,7,9-11 |
| bd-id | Bridge-Domain range, Example: 2,4-5,7,9-11 |
| root | Set the root bridge priority for the spanning tree |
| priority | Set the bridge priority for the spanning tree |
| prio | bridge priority in increments of 4096 |

**Command Mode:** /exec/configure/spanning-tree/pseudo

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, qos, V-commands
**Command ID:** wp1879540125

---

# Command: vmtracker connection

## Syntax
```
[no] vmtracker connection <connection-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vmtracker | Configure vmtracker parameters |
| connection | Specify a host to connect |
| connection-name | VM host name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3541346667

---

# Command: vmtracker connection refresh

## Syntax
```
[no] vmtracker connection <connection-name> refresh
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vmtracker | Configure vmtracker parameters |
| connection | Specify a host to connect |
| connection-name | VM host name |
| refresh | Refresh all host related information |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp4903722260

---

# Command: vmtracker enable

## Syntax
```
[no] vmtracker enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vmtracker | Configure vmtracker feature |
| enable | Enable vmtracker feature on interface |

**Command Mode:** /exec/configure/if-switching

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1350834307

---

# Command: vmtracker fabric auto-config

## Syntax
```
[no] vmtracker fabric auto-config
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vmtracker | Configure vmtracker parameters |
| fabric | Enable VM Tracker Fabric paramters |
| auto-config | Enable VM Tracker Fabric AutoConfiguration |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp4129880979

---

# Command: vn-segment

## Syntax
```
vn-segment { <segment-id> &#124; <zero-segment-id> } &#124; no vn-segment
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vn-segment | VN Segment id of the VLAN |
| segment-id | segment-id |
| zero-segment-id | segment-id |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3538007838

---

# Command: vni

## Syntax
```
[no] vni <vni-id-sh>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vni | Configure a vni-based static host |

**Command Mode:** /exec/configure/static-host

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3619102841

---

# Command: vni

## Syntax
```
{ vni <vni-id> &#124; no vni }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vni | Vni |
| vni-id | Configure vni id |

**Command Mode:** /exec/configure/configngoamconnectcheck

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp2609904120

---

# Command: vni

## Syntax
```
{ vni <id> } &#124; { no vni [ <id> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vni | Virtual Network Identifier |
| id | vni, Example: 4096,6099 |

**Command Mode:** /exec/configure/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp7789782730

---

# Command: vni default dynamic

## Syntax
```
{ vni default dynamic } &#124; { no vni default }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |
| vni | Virtual Network Identifier |
| default | Default (wildcard). Match any vni when there is no specific vni mapping configured |

**Command Mode:** /exec/configure/profile-map /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp2951520928

---

# Command: vni l2

## Syntax
```
[no] vni <vni_id> l2
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vni | Configure Ethernet VPN ID |
| vni_id | Specify VNI ID |
| l2 | Layer-2 VNI |

**Command Mode:** /exec/configure/evpn

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp8857545750

---

# Command: vpc

## Syntax
```
vpc [ <vpc_num> ] &#124; no vpc [ <vpc_num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vpc | Virtual Port Channel configuration |
| vpc_num | (Optional) specify a Virtual Port Channel number |

**Command Mode:** /exec/configure/if-eth-port-channel-switch

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, vpc, V-commands
**Command ID:** wp8466930410

---

# Command: vpc domain

## Syntax
```
vpc domain <domain_id> &#124; no vpc domain <domain_id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vpc | Virtual Port Channel configuration |
| domain | Specify domain |
| domain_id | domain id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, vpc, V-commands
**Command ID:** wp3366907376

---

# Command: vpc orphan-port suspend

## Syntax
```
[no] vpc orphan-port suspend
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vpc | Virtual Port Channel configuration |
| orphan-port | orphan-port (non-vpc port) |
| suspend | suspend - when vPC secondary peerlink goes down |

**Command Mode:** /exec/configure/if-eth-phy /exec/configure/if-eth-port-channel-switch /exec/configure/if-eth-port-channel /exec/configure/if-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, interface, vpc, V-commands
**Command ID:** wp3161227455

---

# Command: vpc peer-link

## Syntax
```
vpc peer-link &#124; no vpc peer-link
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vpc | Virtual Port Channel configuration |
| peer-link | specify if this link is used for peer communication |

**Command Mode:** /exec/configure/if-eth-port-channel-switch

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, vpc, V-commands
**Command ID:** wp1941015377

---

# Command: vpc role preempt

## Syntax
```
vpc role preempt
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| role | vPC role related command |
| preempt | Enable/Trigger preemption of lower priority master |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, vpc, V-commands
**Command ID:** wp3528556824

---

# Command: vpn

## Syntax
```
[no] vpn <otv-isis-vpn-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vpn | Configure IS-IS VPN name eg: Overlay<x> |
| otv-isis-vpn-name | Overlay name |

**Command Mode:** /exec/configure/otv-isis

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1894335270

---

# Command: vpn id

## Syntax
```
vpn id <vpn-id> &#124; no vpn id [ <vpn-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vpn | Configure VPN ID in rfc2685 format |
| id | Configure VPN ID in rfc2685 format |
| vpn-id | OUI:VPN-Index, format (hex) <3 bytes OUI:4 bytes VPN-Index> |

**Command Mode:** /exec/configure/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2073352551

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Configure ISIS VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-isis

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3937102774

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Configure RIP VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-rip

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp6215807800

---

# Command: vrf

## Syntax
```
[no] vrf [ <name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Catena service vrf |
| name | (Optional) Catena Service VRF name |

**Command Mode:** /exec/configure/catena-device-grp

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp2407887866

---

# Command: vrf

## Syntax
```
{ { vrf { <vrf-name> &#124; <vrf-known-name> } } &#124; no vrf }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | Display per-VRF information |
| vrf-name | VRF name |
| vrf-known-name | Known VRF name |

**Command Mode:** /exec/configure/configngoamconnectcheck

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3110132106

---

# Command: vrf

## Syntax
```
[no] vrf { <vrf-name> &#124; <vrf-known-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | set vrf membership |
| vrf-name | VRF name |
| vrf-known-name | Known VRF name |

**Command Mode:** /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp5106298740

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Display per-VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-ospf3

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp1907865848

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Configure VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-eigrp

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp1081995299

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Display per-VRF information |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-ospf

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp2960204145

---

# Command: vrf

## Syntax
```
{ vrf <name> } &#124; { no vrf <name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | ITD service vrf |
| name | ITD Service VRF name |

**Command Mode:** /exec/configure/itd

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3560533080

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-cfg-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrf-cfg-name | VRF name |
| vrf | Virtual Router Context |
| no | (Optional) Negate a command or set its defaults |

**Command Mode:** /exec/configure/router-bgp/router-bgp-bmp-server

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp1330288920

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Virtual Router Context |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3812660783

---

# Command: vrf

## Syntax
```
[no] vrf <vrf-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrf | Configure vrf for PLB service |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/plb

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp6779316780

---

# Command: vrf

## Syntax
```
{ { no &#124; default } vrf &#124;
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| vrf | Configure IP SLAs for a VPN Routing/Forwarding instance |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/jitter /exec/configure/ip-sla/tcp /exec/configure/ip-sla/icmpEcho /exec/configure/ip-sla/dns
 /exec/configure/ip-sla/http

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3661289516

---

# Command: vrf context

## Syntax
```
vrf context <vrf-name> &#124; no vrf context { <vrf-name> &#124; <vrf-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | Configure VRF parameters |
| context | Create VRF and enter VRF mode |
| vrf-name | VRF name |
| vrf-name | VRF name |
| vrf-name | VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp8861493660

---

# Command: vrf default static

## Syntax
```
{ vrf default { static <profile-name> &#124; dynamic } } &#124; { no vrf default }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | VRF name |
| default | Default (wildcard). Match any vrf when there is no specific vrf mapping configured |
| static | Static Profile Map: Configure profile name via CLI |
| profile-name | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |

**Command Mode:** /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp8630052300

---

# Command: vrf member

## Syntax
```
vrf member <vrf-name> &#124; no vrf member [ <vrf-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | Configure VRF parameters |
| member | Set interface's VRF membership |
| vrf-name | VRF name |

**Command Mode:** /exec/configure/if-igp /exec/configure/if-mgmt-ether

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp1075683567

---

# Command: vrf member

## Syntax
```
vrf member { <vrf_name> &#124; <vrf-known-name> } &#124; no vrf member [ <vrf_name> &#124; <vrf-known-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | Configure VPN Routing/Forwarding table |
| member | Set route's VRF membership |
| vrf_name | VRF name |
| vrf-known-name | Known VRF name |

**Command Mode:** /exec/configure/track

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp2631581791

---

# Command: vrf static

## Syntax
```
{ vrf <vrf-name> { static <profile-name> &#124; dynamic } } &#124; { no vrf <vrf-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vrf | VRF name |
| vrf-name | VRF name |
| static | Static Profile Map: Configure profile name via CLI |
| profile-name | Static Profile Map: Configure profile name via CLI |
| dynamic | Dynamic Profile Map: Retrieve profile name from the external server |

**Command Mode:** /exec/configure/profile-map-global

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, overlay, V-commands
**Command ID:** wp3666278995

---

# Command: vrrp

## Syntax
```
[no] vrrp <vr_id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrp | VRRP configuration commands |
| vr_id | IPv4 VR group number |

**Command Mode:** /exec/configure/if-legacy-eth /exec/configure/if-ethernet /exec/configure/if-port-channel /exec/configure/if-vlan-common /exec/configure/if-eth-any

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3190220648

---

# Command: vrrp bfd

## Syntax
```
{ vrrp bfd <peer_intf_ip> &#124; no vrrp bfd [ <peer_intf_ip> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrp | VRRP configuration commands |
| bfd | BFD protocol |
| peer_intf_ip | Neighbor IP address |
| no | Negate a command or set its defaults |

**Command Mode:** /exec/configure/if-eth-any/vrrp

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, bfd, V-commands
**Command ID:** wp3959401478

---

# Command: vrrpv2

## Syntax
```
[no] vrrpv2
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrpv2 | Enable VRRPv2 compatibility mode |

**Command Mode:** /exec/configure/if-eth-any/vrrpv3

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3008220910

---

# Command: vrrpv3

## Syntax
```
[no] vrrpv3
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrpv3 | VRRPv3 configuration commands |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3907116497

---

# Command: vrrpv3 address-family

## Syntax
```
[no] vrrpv3 <group_id> address-family <opt_v6>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrpv3 | Configure VRRPv3 group parameters |
| address-family | IPV6 address family |
| opt_v6 | Enter ipv6 |
| group_id | VRRP Group ID |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3216231031

---

# Command: vrrpv3 address-family

## Syntax
```
[no] vrrpv3 <group_id> address-family <opt_v4>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrpv3 | Configure VRRPv3 group parameters |
| address-family | IPV4 address family |
| opt_v4 | Enter ipv4 |
| group_id | VRRP Group ID |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3256044110

---

# Command: vrrs leader

## Syntax
```
[no] vrrs leader <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrs | VRRS-related commands |
| leader | Name of VRRS tag for which this group is the leader |
| tag | VRRS tag to lead |

**Command Mode:** /exec/configure/if-eth-any/vrrpv3

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2364078884

---

# Command: vrrs pathway

## Syntax
```
[no] vrrs pathway <name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vrrs | VRRS Interface configuration commands |
| pathway | Configure a VRRS pathway |
| name | Name of the VRRS tag to associate with pathway |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp6661295500

---

# Command: vsh

## Syntax
```
&#124; vsh
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| vsh | the shell that understands cli command |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2265161850

---

# Command: vtp

## Syntax
```
[no] vtp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| vtp | Enable VTP on this interface |

**Command Mode:** /exec/configure/if-switching

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp6890142870

---

# Command: vtp domain

## Syntax
```
vtp domain <domain_name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vtp | Configure global VTP state |
| domain | Set the name of the VTP administrative domain |
| domain_name | The ascii name for the VTP administrative domain |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp1206491896

---

# Command: vtp file

## Syntax
```
vtp file <file_name> &#124; no vtp file
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vtp | Configure global VTP state |
| file | Set the name of the VTP file name |
| file_name | URI for vlan.dat |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2840501556

---

# Command: vtp password

## Syntax
```
vtp password <password_name> &#124; no vtp password
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vtp | Configure global VTP state |
| password | Set the password for the VTP administrative domain |
| password_name | The ascii password for the VTP administrative domain |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp3808807822

---

# Command: vtp pruning

## Syntax
```
vtp pruning &#124; no vtp pruning
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vtp | Configure global VTP state |
| pruning | Set the adminstrative domain to permit pruning |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2803755927

---

# Command: vtp version

## Syntax
```
vtp version <version_num> &#124; no vtp version
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| vtp | Configure global VTP state |
| version | Set the adminstrative domain to VTP version |
| version_num | Set the adminstrative domain to VTP version |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010110.html
**Tags:** config-mode, V-commands
**Command ID:** wp2249369743

---

