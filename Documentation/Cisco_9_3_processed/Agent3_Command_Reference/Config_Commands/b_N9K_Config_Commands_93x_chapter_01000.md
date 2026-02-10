# Chapter: H Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_01000.html
**Type:** Configuration Commands  
**Chapter:** Group-1000 Commands  
**Total Commands:** 122

## Command List

- `ha-policy single`
- `hardware-telemetry fte`
- `hardware-telemetry inband-telemetry`
- `hardware-telemetry postcard-telemetry`
- `hardware-telemetry ssx`
- `hardware access-list lou resource threshold`
- `hardware access-list match inner-header`
- `hardware access-list module`
- `hardware access-list tcam label ing-racl 9`
- `hardware access-list tcam region`
- `hardware access-list tcam region double-wide`
- `hardware access-list tcam region ing-flow-redirect`
- `hardware access-list tcam region qualify udf`
- `hardware access-list tcam region tcp-nat`
- `hardware ecmp hash-offset`
- `hardware ecmp hash-polynomial`
- `hardware ejector enable`
- `hardware fan-zone raise-speed`
- `hardware forwarding l3 resource route non-deterministic`
- `hardware forwarding unicast trace`
- `hardware ip glean throttle`
- `hardware ip glean throttle maximum`
- `hardware ip glean throttle syslog`
- `hardware ip glean throttle timeout`
- `hardware ipv6 glean throttle`
- `hardware ipv6 glean throttle maximum`
- `hardware ipv6 glean throttle syslog`
- `hardware ipv6 glean throttle timeout`
- `hardware module boot-order reverse`
- `hardware multicast global-tx-span`
- `hardware profile buffer info poll-interval timer`
- `hardware profile buffer info port-threshold threshold`
- `hardware profile buffer monitor unicast`
- `hardware profile buffer qosgroup threshold`
- `hardware profile buffer span-threshold`
- `hardware profile ecmp auto-recovery threshold`
- `hardware profile ecmp resilient`
- `hardware profile ecmp template module`
- `hardware profile forwarding-mode`
- `hardware profile front portmode`
- `hardware profile ipv6 alpm carve-value`
- `hardware profile ipv6 lpm-entries maximum`
- `hardware profile latency monitor`
- `hardware profile module`
- `hardware profile mpls adjacency-stats bytes`
- `hardware profile mpls extended-ecmp`
- `hardware profile multicast flex-stats-enable`
- `hardware profile multicast max-limit`
- `hardware profile multicast max-limit lpm-entries`
- `hardware profile multicast nlb`
- `hardware profile multicast optimization disable`
- `hardware profile multicast rpf-check-optimization`
- `hardware profile multicast service-reflect port`
- `hardware profile multicast slow-receiver port`
- `hardware profile multicast syslog-threshold`
- `hardware profile openflow`
- `hardware profile packet-drop`
- `hardware profile pbr ecmp paths`
- `hardware profile pbr skip-selfip`
- `hardware profile pfc mmu buffer-reservation`
- `hardware profile portmode`
- `hardware profile racl priority toggle`
- `hardware profile statistics pstat`
- `hardware profile svi flex-stats-enable`
- `hardware profile tcam ipv6-sup-tcam match-inner`
- `hardware profile tcam mcast racl-bridge`
- `hardware profile tcam region`
- `hardware profile tcam region span qualify udf`
- `hardware profile tcam region spanv6-l2 qualify udf`
- `hardware profile tcam region spanv6 qualify udf`
- `hardware profile tcam resource service-template`
- `hardware profile tcam resource template`
- `hardware profile ucast6 lpm-65-to-127-max-limit`
- `hardware profile ucast6 max-limit`
- `hardware profile unicast enable-host-ecmp`
- `hardware profile unicast syslog-threshold`
- `hardware qos dynamic-buffer-sharing`
- `hardware qos fc rate-shaper`
- `hardware qos pfc mc-drop`
- `hardware sample-redirect module redirect-interface`
- `head`
- `header-type 2`
- `hello-interval`
- `hello-interval`
- `hello-interval`
- `history`
- `history`
- `history`
- `history`
- `history`
- `history`
- `holdtime`
- `hop-limit maximum`
- `hop-limit minimum`
- `hop`
- `host-reachability protocol`
- `host`
- `host group permit`
- `host group permit`
- `host source group permit`
- `host source group permit`
- `hostname`
- `hostname dynamic`
- `hostname dynamic`
- `hostname dynamic`
- `hsrp`
- `hsrp anycast`
- `hsrp bfd`
- `hsrp bfd all-interfaces`
- `hsrp delay minimum`
- `hsrp force state vlan`
- `hsrp ipv6`
- `hsrp mac-refresh`
- `hsrp timers extended-hold`
- `hsrp use-bia`
- `hsrp version 1`
- `http get`
- `http proxy server`
- `human`
- `human`
- `hw-module logging onboard`
- `hw-module logging onboard`

---

## Detailed Command Reference

# Command: ha-policy single

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ha-policy | Change HA policy for this VDC |
| hap-change | Change HA policy for this VDC |
| single-sup | Change HA policy for this VDC for single-sup situations |
| dual-sup | Change HA policy for this VDC for dual-sup situations |
| sw-change | Set hap policy |

**Command Mode:** /exec/configure/vdc

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, qos, H-commands
**Command ID:** wp3137034680

---

# Command: hardware-telemetry fte

## Syntax
```
[no] hardware-telemetry fte
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hardware-telemetry | Hardware telemetry configuration |
| fte | Enable/Disable Flow Table Events configuration |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3070497008

---

# Command: hardware-telemetry inband-telemetry

## Syntax
```
[no] hardware-telemetry inband-telemetry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hardware-telemetry | Hardware telemetry configuration |
| inband-telemetry | Enable/Disable inband telemetry configuration |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2619016311

---

# Command: hardware-telemetry postcard-telemetry

## Syntax
```
[no] hardware-telemetry postcard-telemetry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hardware-telemetry | Hardware telemetry configuration |
| postcard-telemetry | Enable/Disable postcard telemetry configuration |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1557184481

---

# Command: hardware-telemetry ssx

## Syntax
```
[no] hardware-telemetry ssx
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hardware-telemetry | Hardware Telemetry Configurations |
| ssx | enable Streaming Statistics Exporter Configurations |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp7943260780

---

# Command: hardware access-list lou resource threshold

## Syntax
```
[no] hardware access-list lou resource threshold <threshold>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| lou | LOU |
| resource | hardware resource |
| threshold | port expansion threshold |
| threshold | value of threshold |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp1510668458

---

# Command: hardware access-list match inner-header

## Syntax
```
[no] hardware access-list match inner-header
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command or set its defaults |
| hardware | Change hardware usage settings |
| access-list | Access Control List |
| match | Match criteria in ACL |
| inner-header | Match inner header fields in IPinIP/GRE packets |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp3323318938

---

# Command: hardware access-list module

## Syntax
```
[no] hardware access-list { resource-pooling &#124; resource pooling } module <module-number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Show hardware information |
| access-list | Access Control List |
| resource-pooling | Enable ACL programming across TCAM banks |
| resource | hardware resource |
| pooling | Enable ACL programming across TCAM banks |
| module | module number |
| module-number | specify module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp3616979645

---

# Command: hardware access-list tcam label ing-racl 9

## Syntax
```
[no] hardware access-list tcam label ing-racl 9
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| label | Tcam entry label info |
| ing-racl | Ingress RACL region |
| 9 | Size in bits for BD-Labels allocated to Ingress-RACL region |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp2892781887

---

# Command: hardware access-list tcam region

## Syntax
```
[no] hardware access-list tcam region <type> <tcam_size>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| type | Region type |
| tcam_size | Enter tcam size |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp3332318112

---

# Command: hardware access-list tcam region double-wide

## Syntax
```
[no] hardware access-list tcam region <double-wide-region> <tcam_size> double-wide
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| double-wide-region | Region type |
| tcam_size | Enter tcam size |
| double-wide | Double Width |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp7472078120

---

# Command: hardware access-list tcam region ing-flow-redirect

## Syntax
```
[no] hardware access-list tcam region ing-flow-redirect <tcam_size>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| ing-flow-redirect | Egress region in ACX |
| tcam_size | Enter tcam size |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp1717782504

---

# Command: hardware access-list tcam region qualify udf

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| udf_tcam_type | Region type |
| qualify | Configure UDFs to be qualified for span region |
| udf | Configure UDF names |
| v6udf | Configure IPv6 UDF names |
| udf_name | UDF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp2493196587

---

# Command: hardware access-list tcam region tcp-nat

## Syntax
```
[no] hardware access-list tcam region tcp-nat <tcam_size>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| access-list | Access Control List |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| tcp-nat | TCP NAT region within NAT region |
| tcam_size | Enter tcam size |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, network, H-commands
**Command ID:** wp3733711984

---

# Command: hardware ecmp hash-offset

## Syntax
```
[no] hardware ecmp hash-offset <value> [ concatenation ] &#124; no hardware ecmp hash-offset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| ecmp | ECMP configuration |
| hash-offset | Configure hash offset |
| value | Hash offset 0-15 non-concatenate mode, 0-63 concatenate mode |
| concatenation | (Optional) Configure hash concatenation |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2777663009

---

# Command: hardware ecmp hash-polynomial

## Syntax
```
hardware ecmp hash-polynomial <poly-type> &#124; no hardware ecmp hash-polynomial
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| ecmp | ECMP configuration |
| hash-polynomial | Configure hash polynomial |
| poly-type | Polynomial type |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2724864175

---

# Command: hardware ejector enable

## Syntax
```
[no] hardware ejector enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| ejector | Card ejector functionality |
| enable | enabled means when both ejectors are open, card is powered down |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2374201910

---

# Command: hardware fan-zone raise-speed

## Syntax
```
[no] hardware fan-zone <fan_zone_id> raise-speed <speed-to-raise>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| fan-zone | Fan Zone supported in the switch |
| fan_zone_id | please enter fan zone id whose speed needs to be increased |
| raise-speed | Speed to be added for current fan zone speed |
| speed-to-raise | please enter additional fan speed |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2701612216

---

# Command: hardware forwarding l3 resource route non-deterministic

## Syntax
```
[no] hardware forwarding l3 resource route non-deterministic
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | hardware information |
| forwarding | forwarding information |
| l3 | Layer-3 |
| resource | hardware resources |
| route | TCAM capacity to hold prefixes |
| non-deterministic | extend upto 1M |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, routing, H-commands
**Command ID:** wp2764738307

---

# Command: hardware forwarding unicast trace

## Syntax
```
[no] hardware forwarding unicast trace
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| forwarding | Hardware forwarding |
| unicast | Hardware Unicast forwarding |
| trace | Debug traces |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3773489524

---

# Command: hardware ip glean throttle

## Syntax
```
[no] hardware ip glean throttle
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware information |
| ip | IP |
| glean | Glean |
| throttle | Throttle |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp3195746574

---

# Command: hardware ip glean throttle maximum

## Syntax
```
{ hardware ip glean throttle maximum <count> } &#124; { no hardware ip glean throttle maximum }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ip | IP |
| glean | Glean |
| throttle | Throttle |
| maximum | Maximum number of entries |
| count | Count |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp1264245481

---

# Command: hardware ip glean throttle syslog

## Syntax
```
{ hardware ip glean throttle syslog <pkt-count> } &#124; { no hardware ip glean throttle syslog }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ip | IP |
| glean | Glean |
| throttle | Throttle |
| syslog | Threshold for syslog for number of packets hitting the entry |
| pkt-count | Packet count |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, management, H-commands
**Command ID:** wp4050497528

---

# Command: hardware ip glean throttle timeout

## Syntax
```
{ hardware ip glean throttle timeout <timeout-in-sec> } &#124; { no hardware ip glean throttle timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ip | IP |
| glean | Glean |
| throttle | Throttle |
| timeout | Timeout |
| timeout-in-sec | Timeout value in seconds (should be multiple of 30, else will be rounded off to nearest boundary) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, system, H-commands
**Command ID:** wp1397359997

---

# Command: hardware ipv6 glean throttle

## Syntax
```
[no] hardware ipv6 glean throttle
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware information |
| ipv6 | IPv6 |
| glean | Glean |
| throttle | Throttle |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp2214721108

---

# Command: hardware ipv6 glean throttle maximum

## Syntax
```
{ hardware ipv6 glean throttle maximum <count> } &#124; { no hardware ipv6 glean throttle maximum }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ipv6 | IPv6 |
| glean | Glean |
| throttle | Throttle |
| maximum | Maximum number of entries |
| count | Count |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp2123081058

---

# Command: hardware ipv6 glean throttle syslog

## Syntax
```
{ hardware ipv6 glean throttle syslog <pkt-count> } &#124; { no hardware ipv6 glean throttle syslog }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ipv6 | IPv6 |
| glean | Glean |
| throttle | Throttle |
| syslog | Threshold for syslog for number of packets hitting the entry |
| pkt-count | Packet count |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, management, H-commands
**Command ID:** wp5634304980

---

# Command: hardware ipv6 glean throttle timeout

## Syntax
```
{ hardware ipv6 glean throttle timeout <timeout-in-sec> } &#124; { no hardware ipv6 glean throttle timeout }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Hardware information |
| ipv6 | IPv6 |
| glean | Glean |
| throttle | Throttle |
| timeout | Timeout |
| timeout-in-sec | Timeout value in seconds (should be multiple of 30, else will be rounded off to nearest boundary) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, system, H-commands
**Command ID:** wp3021428586

---

# Command: hardware module boot-order reverse

## Syntax
```
[no] hardware module boot-order reverse
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| module | applies on all the modules |
| boot-order | Configure order of module power-up |
| reverse | reverse order of module power-up |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, boot, H-commands
**Command ID:** wp3203091783

---

# Command: hardware multicast global-tx-span

## Syntax
```
[no] hardware multicast global-tx-span
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| multicast | Change multicast setting |
| global-tx-span | Modify table programming to support TX multicast SPAN across slices |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, monitoring, H-commands
**Command ID:** wp1319610742

---

# Command: hardware profile buffer info poll-interval timer

## Syntax
```
[no] hardware profile buffer info poll-interval [ module <module> ] timer <msec>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| buffer | Buffer |
| info | Information |
| poll-interval | System buffer status polling interval |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| timer | Polling timer |
| msec | Polling timer value in msecs |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, system, H-commands
**Command ID:** wp1387114755

---

# Command: hardware profile buffer info port-threshold threshold

## Syntax
```
[no] hardware profile buffer info port-threshold [ module <module> ] threshold <value>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| buffer | Buffer |
| info | Information |
| port-threshold | Set port egress buffer usage threshold |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| threshold | threshold value |
| value | percentage of maximum usage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp1306079040

---

# Command: hardware profile buffer monitor unicast

## Syntax
```
hardware profile buffer monitor { unicast &#124; multicast } [ internal ] [ sampling <sampling> ] [ threshold <threshold> ] [ interface
 <intf-num> &#124; sclass <sclass> ] &#124; no hardware profile buffer monitor
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Configure hardware profile buffer monitor settings |
| profile | profile buffer monitor settings |
| buffer | Buffer |
| monitor | buffer monitor |
| unicast | unicast |
| multicast | multicast |
| internal | (Optional) enable buffer monitoring internal mode |
| sampling | (Optional) sampling interval in nano-seconds |
| sampling | (Optional) sampling interval in nano-seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2175486393

---

# Command: hardware profile buffer qosgroup threshold

## Syntax
```
[no] hardware profile buffer qosgroup <groupid> threshold <percentage>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | N3500 |
| profile | Profile |
| buffer | Buffer |
| qosgroup | Qos-group |
| groupid | Group-id |
| threshold | Threshold |
| percentage | Percentage of maximum usage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, qos, H-commands
**Command ID:** wp6679376200

---

# Command: hardware profile buffer span-threshold

## Syntax
```
[no] hardware profile buffer span-threshold <percentage>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | N3500 |
| profile | Profile |
| buffer | Buffer |
| span-threshold | Span Threshold |
| percentage | Percentage of maximum usage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, monitoring, H-commands
**Command ID:** wp2367262820

---

# Command: hardware profile ecmp auto-recovery threshold

## Syntax
```
hardware profile ecmp auto-recovery threshold <percentage> &#124; no hardware profile ecmp auto-recovery threshold
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ecmp | ECMP settings |
| auto-recovery | ECMP auto-recovery settings |
| threshold | ECMP table free percentage threshold for auto-recovery |
| percentage | Percentage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2962344435

---

# Command: hardware profile ecmp resilient

## Syntax
```
[no] hardware profile ecmp resilient
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ecmp | ECMP settings |
| resilient | Configure ECMP resilient mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp7565022050

---

# Command: hardware profile ecmp template module

## Syntax
```
[no] hardware profile ecmp template [ l3vpn ] module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Set hardware profile |
| profile | Profile settings |
| ecmp | set the ecmp template profile |
| template | set the ecmp template profile |
| l3vpn | (Optional) set the l3vpn ecmp template profile |
| module | Enter module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3424001565

---

# Command: hardware profile forwarding-mode

## Syntax
```
[no] hardware profile forwarding-mode { warp [ lpm-entry <lpm_warp> host-entry <host> l2-entry <l2> mcast-entry <mcst_warp>
 ] &#124; openflow-hybrid &#124; openflow-only &#124; normal [ lpm-entry <ipv4> mcast-entry <mcst> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| forwarding-mode | Forwarding mode setting |
| warp | Warp forwarding mode setting |
| openflow-hybrid | Openflow hybrid forwarding mode setting |
| openflow-only | Openflow only forwarding mode setting |
| normal | Normal forwarding mode setting |
| lpm-entry | (Optional) 4K aligned total IPv4 entries |
| ipv4 | (Optional) 4K aligned total IPv4 entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3597183338

---

# Command: hardware profile front portmode

## Syntax
```
hardware profile front portmode <port-mode> &#124; no hardware profile front portmode
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| front | port 1 QSFP/SFP+ settings |
| portmode | QSFP or SFP+ |
| port-mode | Configure QSFP/sfp+ port mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp1047450790

---

# Command: hardware profile ipv6 alpm carve-value

## Syntax
```
[no] hardware profile ipv6 alpm carve-value <ipv6_alpm_carve_value>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ipv6 | ipv6 |
| alpm | alpm mode |
| carve-value | carve value |
| ipv6_alpm_carve_value | maximum entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp1314484722

---

# Command: hardware profile ipv6 lpm-entries maximum

## Syntax
```
[no] hardware profile ipv6 lpm-entries maximum <ipv6_lpm_max_entry>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ipv6 | ipv6 |
| lpm-entries | lpm(non-host) entries |
| maximum | maximum limit |
| ipv6_lpm_max_entry | maximum entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp1120222110

---

# Command: hardware profile latency monitor

## Syntax
```
hardware profile latency monitor [ threshold-avg <threshold-avg> ] [ threshold-max <threshold-max> ] [ sampling <sampling>
 ] &#124; no hardware profile latency monitor
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Configure hardware profile latency monitor settings |
| profile | profile latency monitor settings |
| latency | latency |
| monitor | latency monitor |
| threshold-avg | (Optional) average latency threshold in nano-seconds |
| threshold-avg | (Optional) average latency threshold in nano-seconds |
| threshold-max | (Optional) maximum latency threshold in nano-seconds |
| threshold-max | (Optional) maximum latency threshold in nano-seconds |
| sampling | (Optional) sampling interval in seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1886714407

---

# Command: hardware profile module

## Syntax
```
[no] hardware profile { vxlan &#124; mpls &#124; acl-stats } module { all &#124; <module> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Set hardware profile |
| profile | Profile settings |
| vxlan | Set the hardware profile for module to vxlan |
| mpls | Set the hardware profile for module to mpls |
| acl-stats | Set the hardware profile for module to acl |
| module | Enter module number |
| all | All modules |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp5074596420

---

# Command: hardware profile mpls adjacency-stats bytes

## Syntax
```
[no] hardware profile mpls adjacency-stats bytes
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| profile | Profile |
| mpls | MPLS Statistics Mode |
| adjacency-stats | adjacency-stats |
| bytes | Bytes Only |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2225663078

---

# Command: hardware profile mpls extended-ecmp

## Syntax
```
[no] hardware profile mpls extended-ecmp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| profile | Profile |
| mpls | MPLS routing ECMP mode |
| extended-ecmp | extended-ecmp mode (default) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2353759869

---

# Command: hardware profile multicast flex-stats-enable

## Syntax
```
[no] hardware profile multicast flex-stats-enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| flex-stats-enable | Enable real time stats |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2359720854

---

# Command: hardware profile multicast max-limit

## Syntax
```
{ hardware profile multicast max-limit <mcast-ent> } &#124; { no hardware profile multicast max-limit }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| max-limit | maximum limit for multicast entries |
| mcast-ent | Mcast Table Entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2230023211

---

# Command: hardware profile multicast max-limit lpm-entries

## Syntax
```
[no] hardware profile multicast max-limit lpm-entries <ipv4_mcast_lpm_max_entry>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| max-limit | maximum limit for multicast entries |
| lpm-entries | lpm(non-host) entries |
| ipv4_mcast_lpm_max_entry | maximum entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1969385229

---

# Command: hardware profile multicast nlb

## Syntax
```
[no] hardware profile multicast nlb
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| nlb | network load balancing for multicast entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1535447489

---

# Command: hardware profile multicast optimization disable

## Syntax
```
[no] hardware profile multicast optimization disable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Set hardware profile |
| profile | Profile settings |
| multicast | set multicast profile |
| optimization | set multicast optimization profile |
| disable | set the multicast optimization disable profile |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3618168782

---

# Command: hardware profile multicast rpf-check-optimization

## Syntax
```
{ hardware profile multicast rpf-check-optimization } &#124; { no hardware profile multicast rpf-check-optimization }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| rpf-check-optimization | RPF Check optimization on Monticello ASIC |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp4012670734

---

# Command: hardware profile multicast service-reflect port

## Syntax
```
{ hardware profile multicast service-reflect port <port-num> } &#124; { no hardware profile multicast service-reflect }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| service-reflect | service-reflect settings |
| port | loopback port |
| port-num | loopback port-num |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp2366217620

---

# Command: hardware profile multicast slow-receiver port

## Syntax
```
hardware profile multicast slow-receiver port <port> &#124; no hardware profile multicast slow-receiver port <port>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | Profile |
| multicast | Multicast settings |
| slow-receiver | Multicast slow receiver |
| port | Port |
| port | Port number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp2056257633

---

# Command: hardware profile multicast syslog-threshold

## Syntax
```
[no] hardware profile multicast syslog-threshold <percentage>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| multicast | Multicast settings |
| syslog-threshold | MROUTE table syslog threshold |
| percentage | Percentage (Default is 90) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, management, H-commands
**Command ID:** wp3393272201

---

# Command: hardware profile openflow

## Syntax
```
[no] hardware profile { openflow [ agent default { drop &#124; normal } ] &#124; { tap-aggregation [ l2drop ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Hardware Internal Information |
| profile | Profile |
| openflow | Openflow |
| tap-aggregation | Tap Aggregation |
| l2drop | (Optional) Drop non IP traffic ingress on mode tap interfaces |
| agent | (Optional) Act as Openflow Agent |
| default | (Optional) Specify default action for frames which don't match any flow |
| drop | (Optional) Drop all frames that miss MAC |
| normal | (Optional) [default]Flood unknown traffic |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp4287849410

---

# Command: hardware profile packet-drop

## Syntax
```
[no] hardware profile packet-drop
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| packet-drop | Configure Packet Drop parameters |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2096821283

---

# Command: hardware profile pbr ecmp paths

## Syntax
```
[no] hardware profile pbr ecmp paths <maxpath>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| pbr | Policy based routing |
| ecmp | Equal cost multi path |
| paths | ecmp path |
| maxpath | Maximum ecmp paths |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2502836256

---

# Command: hardware profile pbr skip-selfip

## Syntax
```
[no] hardware profile pbr skip-selfip
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| pbr | PBR feature settings |
| skip-selfip | Configure Skipping PBR for self-ip packets |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp1385590576

---

# Command: hardware profile pfc mmu buffer-reservation

## Syntax
```
[no] hardware profile pfc mmu buffer-reservation <percentage>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Hardware Internal Information |
| profile | profile settings |
| pfc | System level priority-flow-control settings |
| mmu | Hardware memory management unit configuration |
| buffer-reservation | Shared pool buffer reservation |
| percentage | Percentage of shared pool buffers to be reserved |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp8860268030

---

# Command: hardware profile portmode

## Syntax
```
{ hardware profile portmode <port-mode> [ 2-tuple ] } &#124; no hardware profile portmode
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| portmode | QSFP port mode setting |
| port-mode | Configure QSFP port mode |
| 2-tuple | (Optional) Display QSFP portnames in 2-tuple mode even in 10G mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp1272424986

---

# Command: hardware profile racl priority toggle

## Syntax
```
[no] hardware profile racl priority toggle
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| racl | RACL settings |
| priority | Configure tcam parameters |
| toggle | High Priority for RACL than NAT and VACL |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, qos, H-commands
**Command ID:** wp1262812776

---

# Command: hardware profile statistics pstat

## Syntax
```
[no] hardware profile statistics pstat [ peak ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Configure hardware profile setting |
| profile | profile settings |
| statistics | hardware stats |
| pstat | Enable Pstat default is instantaneous |
| peak | (Optional) Peak stats |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1021075544

---

# Command: hardware profile svi flex-stats-enable

## Syntax
```
[no] hardware profile svi flex-stats-enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | profile settings |
| svi | SVI settings |
| flex-stats-enable | Enable real time stats |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3646866735

---

# Command: hardware profile tcam ipv6-sup-tcam match-inner

## Syntax
```
{ hardware profile tcam ipv6-sup-tcam match-inner } &#124; { no hardware profile tcam ipv6-sup-tcam match-inner }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| ipv6-sup-tcam | IPv6 SUP TCAM parameters |
| match-inner | match inner payload for tunnel packets |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp4291131849

---

# Command: hardware profile tcam mcast racl-bridge

## Syntax
```
{ hardware profile tcam mcast racl-bridge } &#124; { no hardware profile tcam mcast racl-bridge }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| mcast | multicast address acess |
| racl-bridge | apply permit/drop for mcast bridged pkt |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, security, H-commands
**Command ID:** wp1091859586

---

# Command: hardware profile tcam region

## Syntax
```
[no] hardware profile tcam region { <tcam_compat_type> <tcam_compat_size> &#124; ifacl <tcam_compat_size> [ double-wide ] &#124; nat
 <tcam_compat_size> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| profile | profile |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| ifacl | IPV4 PACL size |
| double-wide | (Optional) Configure tcam as double wide |
| nat | NAT size |
| tcam_compat_size | Enter tcam size |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1657403549

---

# Command: hardware profile tcam region span qualify udf

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| span | Configure for span region |
| qualify | Configure UDFs to be qualified for span region |
| udf | Configure UDF names |
| udf_name | UDF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, monitoring, H-commands
**Command ID:** wp2647881150

---

# Command: hardware profile tcam region spanv6-l2 qualify udf

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| spanv6-l2 | Configure for span region |
| qualify | Configure UDFs to be qualified for span region |
| udf | Configure UDF names |
| udf_name | UDF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, monitoring, H-commands
**Command ID:** wp1979087207

---

# Command: hardware profile tcam region spanv6 qualify udf

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| region | Configure tcam region |
| spanv6 | Configure for span region |
| qualify | Configure UDFs to be qualified for span region |
| udf | Configure UDF names |
| udf_name | UDF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, monitoring, H-commands
**Command ID:** wp3035543086

---

# Command: hardware profile tcam resource service-template

## Syntax
```
[no] hardware profile tcam resource service-template { <name> } [ module { <lc> &#124; <fm> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| resource | Configure tcam hardware resources |
| service-template | Commit template |
| name | Select name of template |
| module | (Optional) Specify a module number |
| lc | (Optional) line card number |
| fm | (Optional) fabric module number |

**Command Mode:** /exec/configure handle auto 424

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1923117619

---

# Command: hardware profile tcam resource template

## Syntax
```
[no] hardware profile tcam resource template { <name> { ref-template <temp-nontahoe> &#124; ref-template-tahoe <temp-tahoe> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| tcam | Configure tcam parameters |
| resource | Configure tcam hardware resources |
| template | Configure template based tcam carving parameters |
| ref-template | Select a default template as reference |
| ref-template-tahoe | Select a default template as reference |
| name | Create/Select name of custom template |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1684389113

---

# Command: hardware profile ucast6 lpm-65-to-127-max-limit

## Syntax
```
{ hardware profile ucast6 lpm-65-to-127-max-limit <unicast-ent> } &#124; { no hardware profile ucast6 lpm-65-to-127-max-limit }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ucast6 | unicast ipv6 settings |
| lpm-65-to-127-max-limit | maximum limit for unicast ipv6 lpm-65-to-127 entries, default is 256 |
| unicast-ent | Unicast ipv6 lpm-65-to-127 Table Entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2463564299

---

# Command: hardware profile ucast6 max-limit

## Syntax
```
{ hardware profile ucast6 max-limit <unicast-ent> } &#124; { no hardware profile ucast6 max-limit }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| ucast6 | unicast ipv6 settings |
| max-limit | maximum limit for unicast ipv6 entries |
| unicast-ent | Unicast ipv6 Table Entries |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2931206030

---

# Command: hardware profile unicast enable-host-ecmp

## Syntax
```
[no] hardware profile unicast enable-host-ecmp [ arp-nd &#124; [ ipv4 [ arp ] ] &#124; [ ipv6 [ nd ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| unicast | Unicast settings |
| enable-host-ecmp | Enable ECMP support for /32 (IPv4) and /128 (IPv6) routes |
| ipv4 | (Optional) Enable ECMP support for /32 (IPv4 Only) Routes |
| ipv6 | (Optional) Enable ECMP support for /128 (IPv6 Only) Routes |
| arp-nd | (Optional) Retain ARP (IPv4) and ND (IPv6) Routes in Host-Table |
| arp | (Optional) Retain ARP Entries in Host-Table |
| nd | (Optional) Retain ND Entries in Host-Table |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1988049036

---

# Command: hardware profile unicast syslog-threshold

## Syntax
```
{ hardware profile unicast syslog-threshold <percentage> } &#124; { no hardware profile unicast syslog-threshold }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| hardware | Change hardware usage settings |
| profile | profile settings |
| unicast | Unicast settings |
| syslog-threshold | Unicast Route table syslog threshold |
| percentage | Percentage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, management, H-commands
**Command ID:** wp2332331414

---

# Command: hardware qos dynamic-buffer-sharing

## Syntax
```
[no] hardware qos dynamic-buffer-sharing
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| qos | Configure qos related configuration |
| dynamic-buffer-sharing | Enable dynamic buffer sharing |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, qos, H-commands
**Command ID:** wp2015785739

---

# Command: hardware qos fc rate-shaper

## Syntax
```
[no] hardware qos fc rate-shaper [ low ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| qos | Configure qos related configuration |
| fc | Fibre Channel interface related configuration |
| rate-shaper | Rate Shaper for FC interface |
| low | (Optional) Configure FC interface low rate shaper |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, qos, H-commands
**Command ID:** wp2522767236

---

# Command: hardware qos pfc mc-drop

## Syntax
```
[no] hardware qos pfc mc-drop
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hardware | Hardware Internal Information |
| qos | Configure qos related configuration |
| pfc | Priority-flow-control specific configuration |
| mc-drop | Multicast packets are droped in lossless queue |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, qos, H-commands
**Command ID:** wp1299777392

---

# Command: hardware sample-redirect module redirect-interface

## Syntax
```
hardware sample-redirect module <num> redirect-interface <interface>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hardware | Change hardware usage settings |
| sample-redirect | Redirect netflow sampled data |
| module | Line card module |
| num | slot number |
| redirect-interface | Interface for redirecting the traffic |
| interface | Interface Name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp1188929757

---

# Command: head

## Syntax
```
&#124; head [ -n <lines> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| head | Display first lines |
| -n | (Optional) modify number of lines (default 10) |
| lines | (Optional) number of lines to print |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp8098218160

---

# Command: header-type 2

## Syntax
```
[no] header-type { 2 &#124; 3 [ rfc-compliant ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| header-type | Set ERSPAN Source version |
| 2 | ERSPAN Source Version 2 |
| 3 | ERSPAN Source Version 3 |
| rfc-compliant | (Optional) ERSPAN V3 header rfc-compliant |

**Command Mode:** /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1271580525

---

# Command: hello-interval

## Syntax
```
{ { hello-interval <interval> } &#124; { no hello-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hello-interval | Hello interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf/router-ospf-vlink /exec/configure/router-ospf/vrf/router-ospf-vlink

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp5171294720

---

# Command: hello-interval

## Syntax
```
{ { hello-interval <interval> } &#124; { no hello-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hello-interval | Hello interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf3/router-ospf3-vlink /exec/configure/router-ospf3/vrf/router-ospf3-vlink

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3536359700

---

# Command: hello-interval

## Syntax
```
{ { hello-interval <interval> } &#124; { no hello-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hello-interval | Hello interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf/vrf/router-ospf-slink

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2988784055

---

# Command: history

## Syntax
```
history { { buckets-kept <num-buckets-kept> } &#124; { distributions-of-statistics-kept <num-dist-stats> } &#124; { enhanced [ interval
 [ <interval-seconds> [ buckets [ <num-buckets> ] ] ] ] } &#124; { filter { all &#124; failures &#124; none &#124; overThreshold } } &#124; { hours-of-statistics-kept
 <num-hours-of-stats> } &#124; { lives-kept <life-size-value> } &#124; { statistics-distribution-interval <dist-interval> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| interval | (Optional) buckets |
| interval-seconds | (Optional) <num-buckets> |
| life-size-value | <dist-interval> |
| history | History and Distribution Data |
| buckets-kept | Maximum number of history buckets to collect |
| num-buckets-kept | Bucket size value (default 15) |
| distributions-of-statistics-kept | Maximum number of statistics distribution buckets to capture |
| num-dist-stats | Distribution bucket size value (default 1) |
| enhanced | Enable enhanced history collection |
| buckets | (Optional) Number of buckets to collect data |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/tcp /exec/configure/ip-sla/icmpEcho

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp8736361980

---

# Command: history

## Syntax
```
{ no &#124; default } history { { buckets-kept } &#124; { distributions-of-statistics-kept } &#124; { enhanced [ interval [ <interval-seconds>
 [ buckets [ <num-buckets> ] ] ] ] } &#124; { filter } &#124; { hours-of-statistics-kept } &#124; { lives-kept } &#124; { statistics-distribution-interval
 } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| interval | (Optional) buckets |
| default | Set a command to its defaults |
| history | History and Distribution Data |
| buckets-kept | Maximum number of history buckets to collect |
| distributions-of-statistics-kept | Maximum number of statistics distribution buckets to capture |
| enhanced | Enable enhanced history collection |
| interval-seconds | (Optional) Interval in seconds |
| buckets | (Optional) Number of buckets to collect data |
| num-buckets | (Optional) Number of buckets |
| filter | Add operation to History when... |

**Command Mode:** /exec/configure/ip-sla/udp /exec/configure/ip-sla/tcp /exec/configure/ip-sla/icmpEcho

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2985333996

---

# Command: history

## Syntax
```
{ no &#124; default } history { { buckets-kept } &#124; { distributions-of-statistics-kept } &#124; { filter } &#124; { hours-of-statistics-kept
 } &#124; { lives-kept } &#124; { statistics-distribution-interval } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| history | History and Distribution Data |
| buckets-kept | Maximum number of history buckets to collect |
| distributions-of-statistics-kept | Maximum number of statistics distribution buckets to capture |
| filter | Add operation to History when... |
| hours-of-statistics-kept | Maximum number of statistics hour groups to capture |
| lives-kept | Maximum number of history lives to collect |
| statistics-distribution-interval | Statistics distribution interval size |

**Command Mode:** /exec/configure/ip-sla/dns /exec/configure/ip-sla/fabricPathEcho /exec/configure/ip-sla/http

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2858993700

---

# Command: history

## Syntax
```
history { { buckets-kept <num-buckets-kept> } &#124; { distributions-of-statistics-kept <num-dist-stats> } &#124; { filter { all &#124; failures
 &#124; none &#124; overThreshold } } &#124; { hours-of-statistics-kept <num-hours-of-stats> } &#124; { lives-kept <life-size-value> } &#124; { statistics-distribution-interval
 <dist-interval> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dist-interval | <num-buckets-kept> |
| num-hours-of-stats | <life-size-value> |
| distributions-of-statistics-kept | hours-of-statistics-kept |
| history | History and Distribution Data |
| buckets-kept | Maximum number of history buckets to collect |
| num-buckets-kept | Bucket size value (default 15) |
| num-dist-stats | Distribution bucket size value (default 1) |
| filter | Add operation to History when... |
| all | Collect every operation in History |
| failures | Collect operations that fail in History |

**Command Mode:** /exec/configure/ip-sla/dns /exec/configure/ip-sla/fabricPathEcho /exec/configure/ip-sla/http

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1186740000

---

# Command: history

## Syntax
```
{ no &#124; default } history { { distributions-of-statistics-kept } &#124; { enhanced [ interval [ <interval-seconds> [ buckets [ <num-buckets>
 ] ] ] ] } &#124; { hours-of-statistics-kept } &#124; { statistics-distribution-interval } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| interval | (Optional) buckets |
| distributions-of-statistics-kept | hours-of-statistics-kept |
| default | Set a command to its defaults |
| history | History and Distribution Data |
| enhanced | Enable enhanced history collection |
| interval-seconds | (Optional) Interval in seconds |
| buckets | (Optional) Number of buckets to collect data |
| num-buckets | (Optional) Number of buckets |
| hours-of-statistics-kept | Maximum number of statistics hour groups to capture |

**Command Mode:** /exec/configure/ip-sla/jitter

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp4120665543

---

# Command: history

## Syntax
```
history { { distributions-of-statistics-kept <num-dist-stats> } &#124; { enhanced [ interval [ <interval-seconds> [ buckets [ <num-buckets>
 ] ] ] ] } &#124; { hours-of-statistics-kept <num-hours-of-stats> } &#124; { statistics-distribution-interval <dist-interval> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| interval | (Optional) buckets |
| num-buckets | (Optional) <num-hours-of-stats> |
| enhanced | hours-of-statistics-kept |
| history | History and Distribution Data |
| distributions-of-statistics-kept | Maximum number of statistics distribution buckets to capture |
| num-dist-stats | Distribution bucket size value (default 1) |
| interval-seconds | (Optional) Interval in seconds |
| buckets | (Optional) Number of buckets to collect data |
| hours-of-statistics-kept | Maximum number of statistics hour groups to capture |
| num-hours-of-stats | Hour groups size value (default 2) |

**Command Mode:** /exec/configure/ip-sla/jitter

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3151493867

---

# Command: holdtime

## Syntax
```
holdtime { infinite &#124; <secs> } &#124; no holdtime
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| holdtime | LDP session holdtime |
| infinite | Ignore LDP session holdtime |
| secs | Holdtime in seconds |

**Command Mode:** /exec/configure/ldp

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, system, H-commands
**Command ID:** wp2388793592

---

# Command: hop-limit maximum

## Syntax
```
[no] hop-limit maximum <limit>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| limit | Maximum hop count value allowed |

**Command Mode:** /exec/configure/config-ra-guard

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1847278097

---

# Command: hop-limit minimum

## Syntax
```
[no] hop-limit minimum <limit>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| limit | Minimum hop count value allowed |

**Command Mode:** /exec/configure/config-ra-guard

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3922901229

---

# Command: hop

## Syntax
```
{ hop <val> } &#124; { no hop }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hop | Configure ngoam hop count |
| val | Configure ngoam service hop count value |

**Command Mode:** /exec/configure/configngoamprofile

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp8999136170

---

# Command: host-reachability protocol

## Syntax
```
[no] host-reachability protocol { bgp &#124; openflow &#124; openflow-ir }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| host-reachability | Configure host reachability advertisement |
| protocol | Control protocol to use |
| bgp | Border Gateway Protocol |
| openflow | OpenFlow |
| openflow-ir | OpenFlow-IR |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2794136278

---

# Command: host

## Syntax
```
[no] { host <hostaddr> &#124; <prefix> &#124; <addr> <mask> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| host | Host address of the object-group member |
| hostaddr | A.B.C.D Host address |
| addr | A.B.C.D Network address of object-group member |
| mask | A.B.C.D wildcard |
| prefix | A.B.C.D/nn Network prefix of the object-group member |

**Command Mode:** /exec/configure/objgroup

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2474227354

---

# Command: host group permit

## Syntax
```
{ <seq> host <hostip> group <range> { permit &#124; deny } } &#124; { no <seq> [ host <hostip> group <range> { permit &#124; deny } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seq | Sequence Number |
| host | Host IP Address |
| hostip | Host IP Address |
| group | Configure explicit group ranges |
| range | Group Prefix |
| permit | Admission Permitted |
| deny | Admission Denied |

**Command Mode:** /exec/configure/nbm-vrf/nbm-host-policy/sender

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3515267741

---

# Command: host group permit

## Syntax
```
{ <seq> host <hostip> group <range> { permit &#124; deny } } &#124; { no <seq> [ host <hostip> group <range> { permit &#124; deny } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seq | Sequence Number |
| host | Host IP Address |
| hostip | Host IP Address |
| group | Configure explicit group ranges |
| range | Group Prefix |
| permit | Admission Permitted |
| deny | Admission Denied |

**Command Mode:** /exec/configure/nbm-host-policy/sender

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3424672846

---

# Command: host source group permit

## Syntax
```
{ <seq> host <hostip> source <sourceip> group <range> { permit &#124; deny } } &#124; { no <seq> [ host <hostip> source <sourceip> group
 <range> { permit &#124; deny } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seq | Sequence Number |
| host | Host IP Address |
| hostip | Host IP Address value |
| source | Source IP Address |
| sourceip | Source IP Address value |
| group | Configure explicit group ranges |
| range | Group Prefix |
| permit | Admission Permitted |
| deny | Admission Denied |

**Command Mode:** /exec/configure/nbm-vrf/nbm-host-policy/receiver

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1028764304

---

# Command: host source group permit

## Syntax
```
{ <seq> host <hostip> source <sourceip> group <range> { permit &#124; deny } } &#124; { no <seq> [ host <hostip> source <sourceip> group
 <range> { permit &#124; deny } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seq | Sequence Number |
| host | Host IP Address |
| hostip | Host IP Address value |
| source | Source IP Address |
| sourceip | Source IP Address value |
| group | Configure explicit group ranges |
| range | Group Prefix |
| permit | Admission Permitted |
| deny | Admission Denied |

**Command Mode:** /exec/configure/nbm-host-policy/receiver

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3682458633

---

# Command: hostname

## Syntax
```
{ hostname &#124; switchname } <name> &#124; no { hostname &#124; switchname }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hostname | Configure system's host name |
| switchname | Configure system's host name |
| name | Enter switchname |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2591473172

---

# Command: hostname dynamic

## Syntax
```
[no] hostname dynamic
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hostname | Set dynamic hostname for IS-IS |
| dynamic | Dynamic hostname |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1579571467

---

# Command: hostname dynamic

## Syntax
```
[no] hostname dynamic
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hostname | Set dynamic hostname for IS-IS |
| dynamic | Dynamic hostname |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1513614642

---

# Command: hostname dynamic

## Syntax
```
[no] hostname dynamic
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hostname | Set dynamic hostname for IS-IS |
| dynamic | Dynamic hostname |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp5776316160

---

# Command: hsrp

## Syntax
```
[no] hsrp <group-id> [ ipv4 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| group-id | Group number (0-255 for HSRPv1) |
| ipv4 | (Optional) Configure IP Version 4 group |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1969644858

---

# Command: hsrp anycast

## Syntax
```
[no] hsrp anycast <id> { ipv4 &#124; ipv6 &#124; both }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP configuration commands |
| anycast | Anycast related commands |
| id | Bundle number |
| ipv4 | Associate IP Version 4 for the bundle |
| ipv6 | Associate IP Version 6 for the bundle |
| both | Associate IP Version 4 and 6 for the bundle |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1173669353

---

# Command: hsrp bfd

## Syntax
```
[no] hsrp bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| bfd | BFD protocol |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, bfd, H-commands
**Command ID:** wp9146103990

---

# Command: hsrp bfd all-interfaces

## Syntax
```
[no] hsrp bfd all-interfaces
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| bfd | BFD protocol |
| all-interfaces | On all interfaces |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, bfd, H-commands
**Command ID:** wp1959842103

---

# Command: hsrp delay minimum

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| delay | HSRP initialisation delay |
| minimum | Minimum delay |
| reload | Delay after reload |
| min-delay | <0-10000> Delay in seconds |
| reload-delay | <0-10000> Delay in seconds |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp3570820367

---

# Command: hsrp force state vlan

## Syntax
```
hsrp force state vlan { <vlans> &#124; all }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| hsrp | Hot Standby Router Protocol (HSRP) information |
| force | Move the HSRP state |
| state | HSRP state |
| vlan | HSRP state changes for these vlans |
| all | Include all HSRP configured VLANs |
| vlans | VLAN IDs of the VLAN for which state change will affect |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, interface, H-commands
**Command ID:** wp3787888041

---

# Command: hsrp ipv6

## Syntax
```
[no] hsrp <group-id> ipv6
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| group-id | Group number |
| ipv6 | Configure IP Version 6 group |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, network, H-commands
**Command ID:** wp1578715187

---

# Command: hsrp mac-refresh

## Syntax
```
hsrp mac-refresh [ <time> ] &#124; no hsrp mac-refresh
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| mac-refresh | Interface mac-refresh time |
| time | (Optional) Timeout value (0-10000) in sec |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2751820646

---

# Command: hsrp timers extended-hold

## Syntax
```
[no] hsrp timers extended-hold [ <extended-hold> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| timers | Global Timers |
| extended-hold | Extended Hold |
| extended-hold | (Optional) Time in seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, system, H-commands
**Command ID:** wp1083327050

---

# Command: hsrp use-bia

## Syntax
```
[no] hsrp use-bia [ scope interface ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| use-bia | HSRP uses interface's burned in address |
| scope | (Optional) Specify the scope of use-bia |
| interface | (Optional) Use-bia applies to all groups on this interface or sub-interface |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2872543995

---

# Command: hsrp version 1

## Syntax
```
hsrp version { 1 &#124; 2 } &#124; no hsrp version
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| hsrp | HSRP interface configuration commands |
| version | HSRP version |
| 1 | Version 1 |
| 2 | Version 2 |

**Command Mode:** /exec/configure/if-eth-any /exec/configure/if-vlan-common /exec/configure/if-port-channel /exec/configure/if-sub /exec/configure/if-ethernet-all

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp2709591550

---

# Command: http get

## Syntax
```
(Optional)
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) |
| cache | (Optional) enable |
| proxy | (Optional) <proxy-info> |
| source-ip | (Optional) <source-ip-hostname> |
| source-port | (Optional) <src-port> |
| version | (Optional) <http-version> |
| http | HTTP Operation |
| get | HTTP get operation |
| WORD | URL |
| enable | (Optional) enable download of cached entries (default) |

**Command Mode:** /exec/configure/ip-sla

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp4233148185

---

# Command: http proxy server

## Syntax
```
[no] http proxy server <hostipname> [ port <port-num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| http | Configure http related parameters |
| proxy | Http Proxy related parameters |
| server | Server address |
| hostipname | IPV4/IPV6 address or DNS name of proxy server |
| port | (Optional) Http proxy server port |
| port-num | (Optional) port number |

**Command Mode:** /exec/configure/trustpool

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1563107450

---

# Command: human

## Syntax
```
&#124; human
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| human | output in human format |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp4286717056

---

# Command: human

## Syntax
```
&#124; human
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| human | output in human format |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, H-commands
**Command ID:** wp1450413255

---

# Command: hw-module logging onboard

## Syntax
```
[no] hw-module logging onboard [ { environmental-history &#124; error-stats &#124; interrupt-stats &#124; module <module> [ { environmental-history
 &#124; error-stats &#124; interrupt-stats &#124; obfl-logs &#124; cpuhog } ] &#124; obfl-logs &#124; cpuhog } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hw-module | Enable/Disable OBFL information |
| logging | Enable/Disable OBFL information |
| onboard | Enable/Disable OBFL information |
| environmental-history | (Optional) Enable/Disable OBFL environmental history |
| error-stats | (Optional) Enable/Disable OBFL error statistics |
| interrupt-stats | (Optional) Enable/Disable OBFL interrupt statistics |
| cpuhog | (Optional) Enable/Disable OBFL cpu hog events |
| module | (Optional) Enable/Disable OBFL information for Module |
| module | (Optional) Enter module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, management, H-commands
**Command ID:** wp3853822709

---

# Command: hw-module logging onboard

## Syntax
```
[no] hw-module logging onboard [ { counter-stats &#124; module <module> [ { counter-stats } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| hw-module | Enable/Disable OBFL information |
| logging | Enable/Disable OBFL information |
| onboard | Enable/Disable OBFL information |
| counter-stats | (Optional) Enable/Disable OBFL counter statistics |
| module | (Optional) Enable/Disable OBFL information for Module |
| module | (Optional) Enter module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01000.html
**Tags:** config-mode, management, H-commands
**Command ID:** wp5197184800

---

