# Chapter: R Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010010.html
**Type:** Configuration Commands  
**Chapter:** Group-10010 Commands  
**Total Commands:** 200

## Command List

- `radius-server deadtime`
- `radius-server directed-request`
- `radius-server host key 0 6 7`
- `radius-server host test`
- `radius-server key 0 6 7`
- `radius-server pss-clean`
- `radius-server retransmit`
- `radius-server test`
- `radius-server timeout`
- `random-detect`
- `random-detect2 minimum-threshold2 maximum-threshold2`
- `random-detect2 non-ecn minimum-threshold2 maximum-threshold2 drop`
- `random-detect`
- `random-detect cos-based`
- `rate-limit`
- `rate-limit cpu direction input output both pps action log`
- `rate-limit cpu direction input output both pps action log`
- `rate-limit packet_in burst`
- `rate-limit packet_in burst`
- `rate-mode`
- `rd`
- `rd auto`
- `rd auto`
- `receiver`
- `receiver`
- `reconnect-interval`
- `record-route`
- `record-route`
- `record`
- `record`
- `record`
- `record`
- `record`
- `record netflow-original`
- `record netflow`
- `record netflow`
- `record netflow`
- `record netflow protocol-port`
- `redistribute bgp`
- `redistribute bgp eigrp isis ospf rip static direct amt lisp route-map`
- `redistribute filter route-map`
- `redistribute filter route-map`
- `redistribute maximum-prefix`
- `redistribute maximum-prefix`
- `redistribute maximum-prefix`
- `redistribute maximum-prefix`
- `redistribute maximum-prefix`
- `redistribute maximum-prefix`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redistribute route-map`
- `redownload forwarding state`
- `redundancy-group`
- `reference-bandwidth`
- `reference-bandwidth`
- `refresh profile`
- `register-database-mapping`
- `register-route-notifications`
- `reload`
- `reload cancel`
- `reload in`
- `reload module`
- `reload module force-dnld`
- `reload non-interruptive`
- `reload sync-adjacency`
- `reload sync-adjacency`
- `reload timer`
- `reload vdc`
- `reload vdc`
- `remark`
- `remark`
- `remark`
- `remote-as`
- `remote-span`
- `remote`
- `remove-private-as`
- `reoptimize events link-up`
- `replay-protection`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `report`
- `request-data-size`
- `request-data-size`
- `request-data-size`
- `resequence access`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `reset`
- `restart amt`
- `restart bgp`
- `restart eigrp`
- `restart fabric_mcast`
- `restart igmp`
- `restart isis`
- `restart msdp`
- `restart ospf`
- `restart ospfv3`
- `restart otv-isis`
- `restart pim`
- `restart pim6`
- `restart rip`
- `restart rsvp`
- `resync-database`
- `retain route-target all`
- `retain route-target all`
- `retransmit-interval`
- `retransmit-interval`
- `retransmit-interval`
- `revision`
- `revocation-check crl`
- `rewrite-evpn-rt-asn`
- `rewrite-rt-asn`
- `rfc1583compatibility`
- `rip shutdown`
- `rmdir`
- `rmon alarm absolute rising-threshold falling-threshold`
- `rmon event`
- `rmon hcalarm absolute startupalarm rising-threshold falling-threshold owner`
- `roaming-eid-prefix`
- `role feature-group name`
- `role name`
- `role priority`
- `rollback running-config checkpoint`
- `root-priority`
- `route-map`
- `route-map`
- `route-map`
- `route-map`
- `route-map out`
- `route-map pbr-statistics`
- `route-reflector-client`
- `route-reflector-client`
- `route-target both`
- `route-target both auto`
- `route-target both auto`
- `route-target export`
- `route-target export`
- `route-target export auto`
- `route-target import`
- `route-target import`
- `route-target import auto`
- `route delete dampen interval`
- `router-guard ip multicast`
- `router-guard ip multicast switchports`
- `router-id`
- `router-id`
- `router-id`
- `router-id`
- `router-id`
- `router-id`
- `router-preference maximum`
- `router bgp`
- `router eigrp`
- `router isis`
- `router ospf`
- `router ospfv3`
- `router rip`
- `routing-context vrf`
- `rsakeypair`
- `rtr etr eid`
- `rule`
- `rule command`
- `rule oid`
- `run-script`
- `run2 guestshell`
- `run bash`

---

## Detailed Command Reference

# Command: radius-server deadtime

## Syntax
```
[no] radius-server deadtime <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| deadtime | duration for which non-reachable server is skipped |
| i0 | Length of time, in minutes |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, system, R-commands
**Command ID:** wp2208553890

---

# Command: radius-server directed-request

## Syntax
```
[no] radius-server directed-request
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| directed-request | enable direct authentication requests to server |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3892496732

---

# Command: radius-server host key 0 6 7

## Syntax
```
{ { [ no ] radius-server host <hostipname> { { key { 0 <s0> &#124; 6 <s6> &#124; 7 <s1> &#124; <s2> } [ pac ] [ auth-port <i0> [ acct-port
 <i1> ] ] } &#124; { [ auth-port1 <i2> ] [ acct-port1 <i3> ] } } [ { authentication [ accounting [ timeout <i4> ] [ retransmit <i5>
 ] ] } &#124; { [ accounting1 ] [ timeout1 <i6> ] [ retransmit1 <i7> ] } ] } &#124; { no radius-server host <hostipname> key } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| key | 0 |
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| host | RADIUS server's DNS name or its IP address |
| hostipname | IPV4/IPV6 address or DNS name |
| key | RADIUS shared secret |
| pac | (Optional) Secure Radius Enable |
| 0 | RADIUS shared secret(clear text) |
| s0 | RADIUS shared secret(clear text) |
| accounting | (Optional) Use for accounting |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3332948760

---

# Command: radius-server host test

## Syntax
```
[no] radius-server host { <hostipname> } test { { username <s0> { [ password { <s1> &#124; 0 <s2> &#124; 7 <s7> } [ idle-time <i1> ]
 ] &#124; [ idle-time <i1> ] } } &#124; { password { <s1> &#124; 0 <s2> &#124; 7 <s7> } [ idle-time <i1> ] } &#124; { idle-time <i1> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | <s0> |
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| host | RADIUS server's DNS name or its IP address |
| hostipname | IPV4/IPV6 address or DNS name |
| test | Parameters to send test packets |
| s0 | user name |
| password | (Optional) user password in test packets |
| s1 | (Optional) user password |
| 0 | (Optional) RADIUS shared secret(clear text) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4179246773

---

# Command: radius-server key 0 6 7

## Syntax
```
{ { [ no ] radius-server key { 0 <s0> &#124; 6 <s6> &#124; 7 <s1> &#124; <s2> } } &#124; { no radius-server key } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| key | Global RADIUS server shared secret |
| 0 | default RADIUS shared secret(clear text) |
| s0 | default RADIUS shared secret(clear text) |
| 6 | default RADIUS shared secret(type-6 encrypted) |
| s6 | default RADIUS shared secret(type-6 encrypted) |
| 7 | default RADIUS shared secret(encrypted) |
| s1 | default RADIUS shared secret(encrypted) |
| s2 | default RADIUS shared secret(clear text) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp9559816020

---

# Command: radius-server pss-clean

## Syntax
```
[no] radius-server pss-clean
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| pss-clean | Erase PSS |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2875016027

---

# Command: radius-server retransmit

## Syntax
```
[no] radius-server retransmit <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| retransmit | Global RADIUS server retransmit count |
| i0 | Global RADIUS server retransmit count |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1844148614

---

# Command: radius-server test

## Syntax
```
[no] radius-server test { { username <s0> { [ password { <s1> &#124; 0 <s2> &#124; 7 <s7> } [ idle-time <i1> ] ] &#124; [ idle-time <i1>
 ] } } &#124; { password { <s1> &#124; 0 <s2> &#124; 7 <s7> } [ idle-time <i1> ] } &#124; { idle-time <i1> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | <s0> |
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| test | Parameters to send test packets |
| s0 | user name |
| password | (Optional) user password in test packets |
| s1 | (Optional) user password |
| 0 | (Optional) RADIUS shared secret(clear text) |
| s2 | (Optional) RADIUS shared secret(clear text) |
| 7 | (Optional) RADIUS shared secret(encrypted) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2324048836

---

# Command: radius-server timeout

## Syntax
```
[no] radius-server timeout <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| radius-server | Configure RADIUS related parameters |
| timeout | Global RADIUS server timeout period in seconds |
| i0 | RADIUS server timeout period in seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, system, R-commands
**Command ID:** wp2018207074

---

# Command: random-detect

## Syntax
```
[no] random-detect { cos <cos-list> [ minimum-threshold ] { <min-thresh> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us ] &#124;
 percent <min-percent-of-qsize> } [ maximum-threshold ] { <max-thresh> [ packets1 &#124; bytes1 &#124; kbytes1 &#124; mbytes1 &#124; ms1 &#124; us1
 ] &#124; percent1 <max-percent-of-qsize> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| random-detect | Configure WRED parameters |
| cos | Parameters for each cos value |
| cos-list | List of class-of-service values |
| minimum-threshold | (Optional) Specify minimum threshold for WRED |
| maximum-threshold | (Optional) Specify maximum threshold for WRED |
| max-thresh | Maximum threshold value |
| percent | Specify thresholds in percent |
| percent1 | Specify thresholds in percent |
| min-percent-of-qsize | Minimum threshold percent of queue size |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1925706462

---

# Command: random-detect2 minimum-threshold2 maximum-threshold2

## Syntax
```
[no] random-detect2 minimum-threshold2 <min-thresh2> { packets2 &#124; bytes2 &#124; kbytes2 &#124; mbytes2 } maximum-threshold2 <max-thresh2>
 { packets3 &#124; bytes3 &#124; kbytes3 &#124; mbytes3 } [ drop-probability2 <drop-prob2> weight2 <weight2> [ cap-average2 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| random-detect2 | Configure WRED parameters |
| minimum-threshold2 | Specify minimum threshold for WRED |
| maximum-threshold2 | Specify maximum threshold for WRED |
| packets2 | Packets |
| bytes2 | Bytes |
| kbytes2 | Kilo Bytes |
| mbytes2 | Mega Bytes |
| packets3 | Packets |
| bytes3 | Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3469128506

---

# Command: random-detect2 non-ecn minimum-threshold2 maximum-threshold2 drop

## Syntax
```
[no] random-detect2 non-ecn minimum-threshold2 <min-thresh2> { packets2 &#124; bytes2 &#124; kbytes2 &#124; mbytes2 } maximum-threshold2
 <max-thresh2> { packets3 &#124; bytes3 &#124; kbytes3 &#124; mbytes3 } { drop-probability2 <drop-prob2> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| random-detect2 | Configure WRED parameters |
| non-ecn | Configure WRED parameters for non-ecn |
| minimum-threshold2 | Specify minimum threshold for WRED |
| maximum-threshold2 | Specify maximum threshold for WRED |
| packets2 | Packets |
| bytes2 | Bytes |
| kbytes2 | Kilo Bytes |
| mbytes2 | Mega Bytes |
| packets3 | Packets |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4158861023

---

# Command: random-detect

## Syntax
```
[no] random-detect [ { minimum-threshold <min-thresh> { packets &#124; bytes &#124; kbytes &#124; mbytes } maximum-threshold <max-thresh>
 { packets1 &#124; bytes1 &#124; kbytes1 &#124; mbytes1 } drop-probability <drop-prob> weight <weight> [ cap-average ] } &#124; threshold { burst-optimized
 &#124; mesh-optimized } ] [ ecn ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| random-detect | Configure WRED parameters |
| threshold | (Optional) Threshold |
| burst-optimized | (Optional) Threshold optimized for bursty traffic |
| mesh-optimized | (Optional) Threshold optimized for mesh traffic |
| minimum-threshold | (Optional) Specify minimum threshold for WRED |
| maximum-threshold | (Optional) Specify maximum threshold for WRED |
| max-thresh | (Optional) Maximum threshold value |
| packets | (Optional) Packets |
| bytes | (Optional) Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2817438089

---

# Command: random-detect cos-based

## Syntax
```
[no] random-detect cos-based [ aggregate [ minimum-threshold ] { <min-thresh> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us
 ] &#124; percent <min-percent-of-qsize> } [ maximum-threshold ] { <max-thresh> [ packets1 &#124; bytes1 &#124; kbytes1 &#124; mbytes1 &#124; ms1 &#124;
 us1 ] &#124; percent1 <max-percent-of-qsize> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| random-detect | Configure WRED parameters |
| cos-based | Configure WRED parameters for cos-based mode |
| aggregate | (Optional) Configure WRED parameters to same value for all sub-classes |
| minimum-threshold | (Optional) Specify minimum threshold for WRED |
| maximum-threshold | (Optional) Specify maximum threshold for WRED |
| max-thresh | (Optional) Maximum threshold value |
| percent | (Optional) Specify thresholds in percent |
| percent1 | (Optional) Specify thresholds in percent |
| min-percent-of-qsize | (Optional) Minimum threshold percent of queue size |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1673976564

---

# Command: rate-limit

## Syntax
```
rate-limit { auto &#124; <rate_value> } &#124; no rate-limit
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-limit | Set the Rate limit for SPAN packets |
| auto | Set the Rate limit using auto value |
| rate_value | Enter the percentage of the maximum rate for SPAN packets |

**Command Mode:** /exec/configure/monitor-local-src /exec/configure/config-monitor /exec/configure/config-monitor-erspan-src

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2703286844

---

# Command: rate-limit cpu direction input output both pps action log

## Syntax
```
{ rate-limit cpu direction { input &#124; output &#124; both } pps <pps-val> action log } &#124; { no rate-limit cpu direction [ { input
 &#124; output &#124; both } pps <pps-val> action log ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-limit | set packet per second rate limit |
| cpu | Supervisor CPU limits |
| direction | input/output direction |
| input | set max input packet rate |
| output | set max output packet rate |
| both | set max input and output packet rate |
| pps | packet per second |
| pps-val | pps value |
| action | log action |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3400870981

---

# Command: rate-limit cpu direction input output both pps action log

## Syntax
```
{ rate-limit cpu direction { input &#124; output &#124; both } pps <pps-val> action log } &#124; { no rate-limit cpu direction [ { input
 &#124; output &#124; both } pps <pps-val> action log ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-limit | set packet per second rate limit |
| cpu | Supervisor CPU limits |
| direction | input/output direction |
| input | set max input packet rate |
| output | set max output packet rate |
| both | set max input and output packet rate |
| pps | packet per second |
| pps-val | pps value |
| action | log action |

**Command Mode:** /exec/configure/if-eth-base /exec/configure/if-eth-any /exec/configure/if-mgmt-config

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3164710366

---

# Command: rate-limit packet_in burst

## Syntax
```
rate-limit packet_in <packetin-val> burst <burst-val> &#124; no rate-limit
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-limit | OpenFlow rate limit to controller |
| packet_in | packet in rate (pps) |
| packetin-val | packets per second |
| burst | Maximum number of packets to controller (pps) |
| burst-val | packets per second |

**Command Mode:** /exec/configure/openflow/switch

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3813071946

---

# Command: rate-limit packet_in burst

## Syntax
```
rate-limit packet_in <packetin-val> burst <burst-val> &#124; no rate-limit
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-limit | OpenFlow rate limit to controller |
| packet_in | packet in rate (pps) |
| packetin-val | packets per second |
| burst | Maximum number of packets to controller (pps) |
| burst-val | packets per second |

**Command Mode:** /exec/configure/openflow/switch/sub-switch

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3906432927

---

# Command: rate-mode

## Syntax
```
rate-mode <ratemode> [ force ] &#124; no rate-mode [ <ratemode> ] [ force ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rate-mode | Enter the rate mode |
| force | (Optional) This option will shutdown all ports in port-group momentarily |
| ratemode | Interface port speed |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3738952349

---

# Command: rd

## Syntax
```
{ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } } &#124; { no rd [ { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rd | VPN Route Distinguisher |
| ext-comm-rd-aa4nn2 | VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | VPN route distinguisher in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi-sr

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3075984959

---

# Command: rd auto

## Syntax
```
{ rd { auto &#124; <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } } &#124; { no rd [ { auto &#124; <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rd | VPN Route Distinguisher |
| auto | Generate RD automatically |
| ext-comm-rd-aa4nn2 | VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | VPN route distinguisher in aa:nn format |

**Command Mode:** /exec/configure/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1764234994

---

# Command: rd auto

## Syntax
```
{ rd { auto &#124; <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } } &#124; { no rd [ { auto &#124; <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rd | VPN Route Distinguisher |
| auto | Generate RD automatically |
| ext-comm-rd-aa4nn2 | VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | VPN route distinguisher in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2187806567

---

# Command: receiver

## Syntax
```
[no] receiver
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| receiver | Policies for a Local Receiver |

**Command Mode:** /exec/configure/nbm-host-policy

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1389422524

---

# Command: receiver

## Syntax
```
[no] receiver
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| receiver | Policies for a Local Receiver |

**Command Mode:** /exec/configure/nbm-vrf/nbm-host-policy

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2993551776

---

# Command: reconnect-interval

## Syntax
```
reconnect-interval <interval> &#124; no reconnect-interval [ <interval> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| reconnect-interval | Configure connection reconnect interval |
| interval | Interval in seconds |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3781646380

---

# Command: record-route

## Syntax
```
[no] record-route
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| record-route | Record the route used by the LSP |

**Command Mode:** /exec/configure/te/lsp-attr

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2062004720

---

# Command: record-route

## Syntax
```
[no] record-route
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| record-route | record the route used by the tunnel |

**Command Mode:** /exec/configure/if-te /exec/configure/tunnel-te/cbts-member

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3830950751

---

# Command: record

## Syntax
```
[no] record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Record to be monitored |
| recordname | Record name to be configured |

**Command Mode:** /exec/configure/config-ssx-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1343444460

---

# Command: record

## Syntax
```
[no] record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify INT Record to use |
| recordname | Name of record |

**Command Mode:** /exec/configure/config-int-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1038584470

---

# Command: record

## Syntax
```
[no] record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify FTE Record to use |
| recordname | Name of record |

**Command Mode:** /exec/configure/config-fte-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4459975120

---

# Command: record

## Syntax
```
[no] record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| recordname | Name of record |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2675228929

---

# Command: record

## Syntax
```
[no] record <recordname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| recordname | Name of record |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2377732366

---

# Command: record netflow-original

## Syntax
```
[no] record netflow-original
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| netflow-original | Traditional IPv4 input NetFlow with origin ASs |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2270925180

---

# Command: record netflow

## Syntax
```
[no] record netflow { ipv6 { original-input } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| netflow | Traditional NetFlow collection schemes |
| ipv6 | IPv6 collection schemes |
| original-input | Input NetFlow |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3759939055

---

# Command: record netflow

## Syntax
```
[no] record netflow { ipv4 { original-input } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| netflow | Traditional NetFlow collection schemes |
| ipv4 | Traditional IPv4 NetFlow collection schemes |
| original-input | Traditional IPv4 input NetFlow |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1000234080

---

# Command: record netflow

## Syntax
```
[no] record netflow { layer2-switched { input } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| netflow | Traditional NetFlow collection schemes |
| layer2-switched | Traditional L2 NetFlow collection schemes |
| input | Input NetFlow |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3504017408

---

# Command: record netflow protocol-port

## Syntax
```
[no] record netflow protocol-port
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| record | Specify Flow Record to use |
| netflow | Traditional NetFlow collection schemes |
| protocol-port | Protocol and Ports aggregation scheme |

**Command Mode:** /exec/configure/nfm-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp2987078202

---

# Command: redistribute bgp

## Syntax
```
{ redistribute { { bgp <as> } &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <ptag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map { <policy-name>
 &#124; <rtr_pol_name> } } &#124; { no redistribute { { bgp <as> } &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <ptag> &#124; static &#124; direct &#124; amt &#124;
 lisp } [ route-map { <policy-name> &#124; <rtr_pol_name> } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| eigrp | Enhanced Interior Gateway Protocol (EIGRP) |
| isis | ISO Intermediate-to-Intermediate (IS-IS) |
| ospfv3 | Open Shortest Path First (OSPFv3) |
| rip | Routing Information Protocol (RIP) |
| ptag | Process Tag |
| static | Static |

**Command Mode:** /exec/configure/router-ospf3/router-ospf3-af-ipv6 /exec/configure/router-ospf3/vrf/router-ospf3-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1566753456

---

# Command: redistribute bgp eigrp isis ospf rip static direct amt lisp route-map

## Syntax
```
{ redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <ptag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map { <policy-name>
 &#124; <rtr_pol_name> } } &#124; { no redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <ptag> &#124; static &#124; direct &#124; amt &#124; lisp
 } [ route-map { <policy-name> &#124; <rtr_pol_name> } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | ISO Intermediate-to-Intermediate (IS-IS) |
| ospf | Open Shortest Path First (OSPFv2) |
| eigrp | Enhanced Interior Gateway Protocol (EIGRP) |
| rip | Routing Information Protocol (RIP) |
| ptag | Protocol Tag |
| static | Static |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp1774988855

---

# Command: redistribute filter route-map

## Syntax
```
[no] redistribute filter route-map { <map-name> &#124; <rtr_pol_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| filter | Filter redistributed routes |
| route-map | Route-map to constrain redistribution |
| map-name | A 'routing-rules' route-map name |
| rtr_pol_name | An existing routing-rules policy |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1107818860

---

# Command: redistribute filter route-map

## Syntax
```
[no] redistribute filter route-map { <map-name> &#124; <rtr_pol_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| filter | Filter redistributed routes |
| route-map | Route-map to constrain redistribution |
| map-name | A 'routing-rules' route-map name |
| rtr_pol_name | An existing routing-rules policy |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp5899288090

---

# Command: redistribute maximum-prefix

## Syntax
```
redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] &#124; no redistribute
 maximum-prefix [ <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Max number of prefixes redistributed |
| maximum | max number |
| threshold | (Optional) Threshold in %, at which message is generated |
| warning-only | (Optional) Warning msg is logged when max is reached |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) No of times to retry to get redist routes again |
| timeout | (Optional) Time between the retries |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1219819822

---

# Command: redistribute maximum-prefix

## Syntax
```
redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] &#124; no redistribute
 maximum-prefix [ <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Max number of prefixes redistributed |
| maximum | max number |
| threshold | (Optional) Threshold in %, at which message is generated |
| warning-only | (Optional) Warning msg is logged when max is reached |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) No of times to retry to get redist routes again |
| timeout | (Optional) Time between the retries |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3741048743

---

# Command: redistribute maximum-prefix

## Syntax
```
redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] &#124; no redistribute
 maximum-prefix [ <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Max number of prefixes redistributed |
| maximum | max number |
| threshold | (Optional) Threshold in %, at which message is generated |
| warning-only | (Optional) Warning msg is logged when max is reached |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) No of times to retry to get redist routes again |
| timeout | (Optional) Time between the retries |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3672063265

---

# Command: redistribute maximum-prefix

## Syntax
```
{ redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] } &#124; { no redistribute
 maximum-prefix }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Maximum number of prefixes redistributed to protocol |
| maximum | Maximum number of IP prefixes redistributed |
| threshold | (Optional) Threshold value (%) at which to generate a warning message |
| warning-only | (Optional) Log a warning message when limit is exceeded |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) Number of times to retry to get the redistributed routes again |
| timeout | (Optional) Timeout between each retries |

**Command Mode:** /exec/configure/router-ospf3/router-ospf3-af-ipv6 /exec/configure/router-ospf3/vrf/router-ospf3-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3067090813

---

# Command: redistribute maximum-prefix

## Syntax
```
redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] &#124; no redistribute
 maximum-prefix [ <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Max number of prefixes redistributed |
| maximum | max number |
| threshold | (Optional) Threshold in %, at which message is generated |
| warning-only | (Optional) Warning msg is logged when threshold is reached |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) Number of attempts to receive redistributed routes after max is reached |
| timeout | (Optional) Retry interval |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3928726142

---

# Command: redistribute maximum-prefix

## Syntax
```
{ redistribute maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] } &#124; { no redistribute
 maximum-prefix <maximum> [ <threshold> ] [ warning-only &#124; withdraw [ <retries> <timeout> ] ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| maximum-prefix | Maximum number of prefixes redistributed to protocol |
| maximum | Maximum number of IP prefixes redistributed |
| threshold | (Optional) Threshold value (%) at which to generate a warning message |
| warning-only | (Optional) Log a warning message when limit is exceeded |
| withdraw | (Optional) Withdraw all redistributed routes |
| retries | (Optional) Number of times to retry to get the redistributed routes again |
| timeout | (Optional) Timeout between each retries |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3289721912

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> &#124; static &#124; direct &#124; amt } route-map { <map-name> &#124; <rtr_pol_name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv6 |
| ospfv3 | Open Shortest Path First (OSPF) V3 |
| eigrp | Enhanced Interior Gateway Protocol |
| rip | RIP for IPv6 (RIPNG) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2296326395

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map <map-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | RIP redistribute routes from other routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| isis | Intermediate-to-intermediate (ISIS) |
| rip | Routing Information Protocol (RIP) |
| ospfv3 | Open Shortest Path First (OSPFv3) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-rip/router-rip-af-ipv6 /exec/configure/router-rip/router-rip-vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1333392216

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <tag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map <map-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | RIP redistribute routes from other routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| as | Autonomous system number |
| isis | Intermediate-to-intermediate (ISIS) |
| rip | Routing Information Protocol (RIP) |
| ospf | Open Shortest Path First (OSPFv2) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-rip/router-rip-af-ipv4 /exec/configure/router-rip/router-rip-vrf-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp8701867310

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <tag> &#124; static &#124; direct &#124; amt } route-map { <map-name> &#124; <rtr_pol_name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv4 |
| ospf | Open Shortest Path First (OSPF) |
| eigrp | Enhanced Interior Gateway Protocol |
| rip | RIP for IPv4 |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1933086365

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <tag> &#124; static &#124; direct &#124; amt } route-map { <map-name> &#124; <rtr_pol_name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv4 |
| ospf | Open Shortest Path First (OSPF) |
| eigrp | Enhanced Interior Gateway Protocol |
| rip | RIP for IPv4 |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3319041978

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <tag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map { <map-name>
 &#124; <rtr_pol_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv4 |
| ospf | Open Shortest Path First (OSPF) |
| rip | Routing Information Protocol (RIP) |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp8121488320

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> &#124; static &#124; direct &#124; amt &#124; lisp } route-map { <map-name>
 &#124; <rtr_pol_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv4 |
| ospfv3 | Open Shortest Path First (OSPF) V3 |
| rip | Routing Information Protocol (RIP) |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp4942565660

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { static &#124; direct &#124; amt &#124; lisp &#124; am &#124; hmm &#124; { { eigrp &#124; isis &#124; ospf &#124; rip } <tag> } } route-map <rmap-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Configure redistribution |
| static | Static routes |
| direct | Directly connected |
| isis | ISO IS-IS |
| ospf | Open Shortest Path First (OSPF) |
| rip | Routing Information Protocol (RIP) |
| eigrp | Enhanced Interior Gateway Protocol |
| amt | AMT anycast prefix |
| lisp | LISP EID-prefixes in the non-default VRF |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-ipv4 /exec/configure/router-bgp/router-bgp-vrf-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2761284526

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { static &#124; direct &#124; amt &#124; lisp &#124; am &#124; hmm &#124; { { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> } } route-map <rmap-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Configure redistribution |
| static | Static routes |
| direct | Directly connected |
| isis | ISO IS-IS |
| ospfv3 | Open Shortest Path First, version 3 (OSPFv3) |
| rip | Routing Information Protocol (RIP) |
| eigrp | Enhanced Interior Gateway Protocol |
| amt | AMT anycast prefix |
| lisp | LISP EID-prefixes in the non-default VRF |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-ipv6 /exec/configure/router-bgp/router-bgp-vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1805334826

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospf &#124; rip } <tag> &#124; static &#124; direct &#124; amt } route-map { <map-name> &#124; <rtr_pol_name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv4 |
| ospf | Open Shortest Path First (OSPF) |
| eigrp | Enhanced Interior Gateway Protocol |
| rip | RIP for IPv4 |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3995907380

---

# Command: redistribute route-map

## Syntax
```
[no] redistribute { bgp <as> &#124; { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> &#124; static &#124; direct &#124; amt } route-map { <map-name> &#124; <rtr_pol_name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redistribute | Redistribute information from another routing protocol |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous system number |
| isis | IS-IS Routing for IPv6 |
| ospfv3 | Open Shortest Path First (OSPF) V3 |
| eigrp | Enhanced Interior Gateway Protocol |
| rip | RIP for IPv6 (RIPNG) |
| tag | Process tag |
| static | Static routes |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp7321314170

---

# Command: redownload forwarding state

## Syntax
```
redownload forwarding [ ipv4 &#124; ipv6 &#124; all ] state
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| redownload | redownload |
| forwarding | forwarding |
| ipv4 | (Optional) ipv4 |
| ipv6 | (Optional) ipv6 |
| all | (Optional) both ipv4 and ipv6 |
| state | state |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1069024747

---

# Command: redundancy-group

## Syntax
```
[no] redundancy-group
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| redundancy-group | Configure a redundancy-group node |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3692927149

---

# Command: reference-bandwidth

## Syntax
```
[no] reference-bandwidth { <ref-bw-mbps> [ Mbps ] &#124; <ref-bw-gbps> Gbps }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| reference-bandwidth | Change reference bandwidth used for setting interface metric |
| ref-bw-mbps | Bandwidth in Mbps (Default) |
| Mbps | (Optional) Specify in Mbps |
| ref-bw-gbps | Bandwidth in Gbps |
| Gbps | Specify in Gbps |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, qos, R-commands
**Command ID:** wp1324398898

---

# Command: reference-bandwidth

## Syntax
```
[no] reference-bandwidth { <ref-bw-mbps> [ Mbps ] &#124; <ref-bw-gbps> Gbps }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| reference-bandwidth | Change reference bandwidth used for setting interface metric |
| ref-bw-mbps | Bandwidth in Mbps (Default) |
| Mbps | (Optional) Specify in Mbps |
| ref-bw-gbps | Bandwidth in Gbps |
| Gbps | Specify in Gbps |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common /exec/configure/l2mp-isis/l2mp-isis-l2-topo

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, qos, R-commands
**Command ID:** wp4607543650

---

# Command: refresh profile

## Syntax
```
[no] refresh profile <profile> <dest-profile> [ overwrite ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| refresh | Refresh config-profile |
| profile | Refresh an applied config-profile |
| profile | Enter the name of an applied profile as the source profile |
| dest-profile | Enter the name of an unapplied profile as the destination profile |
| overwrite | (Optional) Override the source profile with the destination profile |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3221944870

---

# Command: register-database-mapping

## Syntax
```
{ [ no ] register-database-mapping }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| register-database-mapping | Register database-mapping EID-prefix to Map-Server |

**Command Mode:** /exec/configure/lisp-dynamic-eid /exec/configure/vrf/lisp-dynamic-eid

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2080317575

---

# Command: register-route-notifications

## Syntax
```
{ [ no ] register-route-notifications }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| register-route-notifications | Register more-specific routes of the database-mapping EID-prefix to Map-Server |

**Command Mode:** /exec/configure/lisp-dynamic-eid /exec/configure/vrf/lisp-dynamic-eid

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2529659797

---

# Command: reload

## Syntax
```
reload
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1880644260

---

# Command: reload cancel

## Syntax
```
reload cancel
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| cancel | Cancel scheduling of the reload |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4109366431

---

# Command: reload in

## Syntax
```
reload in <secs>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| in | Schedule a reload after some time |
| secs | Reload after n seconds |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4211992681

---

# Command: reload module

## Syntax
```
reload module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| module | reboot a specific module |
| module | please enter the module number |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp9951209970

---

# Command: reload module force-dnld

## Syntax
```
reload module <module> force-dnld
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| module | reboot a specific module |
| module | please enter the module number |
| force-dnld | reboot a specific module to force NetBoot and image download |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2204882537

---

# Command: reload non-interruptive

## Syntax
```
reload non-interruptive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| non-interruptive | Reboot without interruption |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1058797155

---

# Command: reload sync-adjacency

## Syntax
```
reload sync-adjacency
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reload with sync adjacency |
| sync-adjacency | Reload with ARP/ND sync adjacency |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3260161000

---

# Command: reload sync-adjacency

## Syntax
```
reload sync-adjacency
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| sync-adjacency | Reload with sync adjacency |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3352943276

---

# Command: reload timer

## Syntax
```
reload timer <secs>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reload | reboot the entire box |
| timer | reboot after a delay <5-3600> seconds |
| secs | delay in seconds |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, system, R-commands
**Command ID:** wp5550680810

---

# Command: reload vdc

## Syntax
```
reload vdc
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vdc | Restart the current vdc |
| reload | Power cycle |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3797652263

---

# Command: reload vdc

## Syntax
```
reload vdc <d-vdc>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vdc | Restart the current vdc |
| reload | Power cycle |
| d-vdc | Enter Virtual Device Context <vdc-id> |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2649476401

---

# Command: remark

## Syntax
```
{ [ <seqno> ] &#124; no } remark <comment>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | (Optional) Sequence number |
| remark | Access list entry comment |
| comment | Comment, up to 100 characters |

**Command Mode:** /exec/configure/arpacl /exec/configure/timerange

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1608971492

---

# Command: remark

## Syntax
```
{ [ <seqno> ] &#124; no } remark <comment>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | (Optional) Sequence number |
| remark | Access list entry comment |
| comment | Comment, up to 100 characters |

**Command Mode:** /exec/configure/ipacl /exec/configure/ipv6acl

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2583741127

---

# Command: remark

## Syntax
```
{ [ <seqno> ] &#124; no } remark <comment>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| seqno | (Optional) Sequence number |
| remark | Access list entry comment |
| comment | Comment, up to 100 characters |

**Command Mode:** /exec/configure/macacl

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1164387636

---

# Command: remote-as

## Syntax
```
{ remote-as <asn> } &#124; { { no &#124; default } remote-as [ <asn> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| remote-as | Specify Autonomous System Number of the neighbor |
| asn | Autonomous System Number |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1324963170

---

# Command: remote-span

## Syntax
```
[no] remote-span
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| remote-span | Enable remote span VLAN |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, monitoring, R-commands
**Command ID:** wp2977845740

---

# Command: remote

## Syntax
```
remote { { ip address { <ipaddress> } &#124; hostname <host_name> } [ port <port_no> ] [ vrf { <vrf-name> &#124; <vrf-known-name> }
 ] &#124; port <port_no> &#124; vrf { <vrf-name> &#124; <vrf-known-name> } } &#124; no remote { ip address &#124; hostname &#124; port }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| remote | Configure remote machine information |
| ip | Configure IP features |
| address | Configure IP address |
| ipaddress | Enter ipv4 address information |
| hostname | Configure remote host name |
| host_name | Enter name of the remote host |
| port | (Optional) Configure remote host tcp port |
| port_no | (Optional) Configure the host tcp port number |
| vrf | (Optional) vrf via which the vCenter Server is reachable |

**Command Mode:** /exec/configure/vmt-conn

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp5495781120

---

# Command: remove-private-as

## Syntax
```
[ no &#124; default ] remove-private-as [ all &#124; replace-as ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| remove-private-as | Remove private AS number from outbound updates |
| all | (Optional) All |
| replace-as | (Optional) Replace |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2683765776

---

# Command: reoptimize events link-up

## Syntax
```
[no] reoptimize events link-up &#124; no reoptimize timers { delay { cleanup &#124; installation } &#124; frequency } &#124; reoptimize timers
 { delay { cleanup <clean_sec> &#124; installation <inst_sec> } &#124; frequency <freq_sec> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| reoptimize | Reoptimization parameters |
| events | Reoptimization triggers |
| link-up | Reoptimize tunnels on link up events |
| timers | Reoptimization timers |
| delay | Delay reoptimization action |
| cleanup | Delay cleanup of reoptimized LSP |
| clean_sec | seconds to delay cleanup of replaced tunnel LSP |
| installation | Delay replacement of current LSP by reoptimized LSP |
| inst_sec | seconds to delay replacement of tunnel LSP |

**Command Mode:** /exec/configure/te

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4072171015

---

# Command: replay-protection

## Syntax
```
[no] replay-protection
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| replay-protection | Enable replay-protection (the default use the no form to disable) |

**Command Mode:** /exec/configure/cts-dot1x /exec/configure/cts-manual

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1599231382

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/sel5

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp3860611110

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1025528597

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel7

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1084691605

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel8

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp3958004313

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel9

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp2222756367

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel10

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1009820373

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/insel19

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1600627003

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/outsel0

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp2110958711

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/outsel1

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp6276295180

---

# Command: report

## Syntax
```
report [ detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report summary |
| detail | (Optional) Show detailed trigger report |

**Command Mode:** /exec/elamtah/outsel2

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp4951029970

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/sel3

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1104718086

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/sel4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1034523013

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/sel6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp3353884900

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/sel7

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1217358506

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/outsel0

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp1515791456

---

# Command: report

## Syntax
```
report
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| report | Show trigger report |

**Command Mode:** /exec/elamns/outsel5

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, R-commands
**Command ID:** wp3461399754

---

# Command: request-data-size

## Syntax
```
{ { no &#124; default } request-data-size &#124; request-data-size <bytes-in-payload> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| request-data-size | Request data size |
| bytes-in-payload | Number of bytes in payload |

**Command Mode:** /exec/configure/ip-sla/icmpEcho

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2769886609

---

# Command: request-data-size

## Syntax
```
{ { no &#124; default } request-data-size &#124; request-data-size <bytes-in-payload> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| request-data-size | Request data size |
| bytes-in-payload | Number of bytes in payload |

**Command Mode:** /exec/configure/ip-sla/udp

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2517140029

---

# Command: request-data-size

## Syntax
```
{ { no &#124; default } request-data-size &#124; request-data-size <bytes-in-payload> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| default | Set a command to its defaults |
| request-data-size | Request data size |
| bytes-in-payload | Number of bytes in payload |

**Command Mode:** /exec/configure/ip-sla/jitter

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2134375750

---

# Command: resequence access

## Syntax
```
resequence { { <ip_ipv6_mac_arp> access-list } &#124; time-range } <name> <number> <increment>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| resequence | Resequence a list with sequence numbers |
| ip_ipv6_mac_arp | IP/IPv6/MAC/ARP |
| access-list | Resequence an access list |
| time-range | Resequence a time-range |
| name | List name |
| number | Starting sequence number |
| increment | Step to increment the sequence number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3621616202

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel9

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1308333080

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4158483269

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel7

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2357022698

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel8

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp8463221560

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel10

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3883270815

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger Filters |

**Command Mode:** /exec/elamtah/insel19

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1723217642

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamtah/outsel0

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp7327748850

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamtah/outsel1

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp6543966930

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamtah/outsel2

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3384331111

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/sel3

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3205605875

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/sel4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2127572390

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/sel5

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1422971174

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/sel6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1328776966

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/sel7

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1701384617

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/outsel0

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp8508172570

---

# Command: reset

## Syntax
```
reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| reset | Reset Trigger conditions |

**Command Mode:** /exec/elamns/outsel5

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1354825280

---

# Command: restart amt

## Syntax
```
restart amt
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| amt | Restart the AMT multicast routing protocol |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1695949601

---

# Command: restart bgp

## Syntax
```
restart bgp <as>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp4130573428

---

# Command: restart eigrp

## Syntax
```
restart eigrp <eigrp-ptag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| eigrp-ptag | Process tag |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp8857650920

---

# Command: restart fabric_mcast

## Syntax
```
restart { fabric_mcast &#124; ngmvpn }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| fabric_mcast | Restart NGMVPN |
| ngmvpn | Restart NGMVPN |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2815378353

---

# Command: restart igmp

## Syntax
```
restart igmp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| igmp | Restart the IGMP multicast routing protocol |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3637782784

---

# Command: restart isis

## Syntax
```
restart isis <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| isis | Intermediate System to Intermediate System (IS-IS) |
| tag | Routing process tag |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2111513188

---

# Command: restart msdp

## Syntax
```
restart msdp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| msdp | Restart the MSDP multicast routing protocol |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3464490827

---

# Command: restart ospf

## Syntax
```
restart ospf <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| ospf | Open Shortest Path First (OSPF) |
| tag | Process tag |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2422379805

---

# Command: restart ospfv3

## Syntax
```
restart ospfv3 <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| ospfv3 | Open Shortest Path First (OSPF) (Version 3) |
| tag | Process tag |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1149060280

---

# Command: restart otv-isis

## Syntax
```
restart otv-isis <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| otv-isis | Intermediate System to Intermediate System (IS-IS) |
| tag | Routing process tag |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1872080828

---

# Command: restart pim

## Syntax
```
restart pim
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| pim | Restart the PIM multicast routing protocol |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3377113812

---

# Command: restart pim6

## Syntax
```
restart pim6
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| pim6 | Restart the PIM6 multicast routing protocol |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2860687881

---

# Command: restart rip

## Syntax
```
restart rip <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a component |
| rip | Routing Information Protocol (RIP) |
| tag | Process ID |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp3068721870

---

# Command: restart rsvp

## Syntax
```
restart rsvp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| restart | Manually restart a process |
| rsvp | RSVP process |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3570960084

---

# Command: resync-database

## Syntax
```
resync-database
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| resync-database | Re-synchronize switch-profile database |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1973166295

---

# Command: retain route-target all

## Syntax
```
[no] retain route-target { all &#124; route-map <rmap-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| retain | Retain the routes based on Target VPN Extended Communities |
| route-target | Specify Target VPN Extended Communities |
| all | All the routes regardless of Target-VPN community |
| route-map | Apply route-map to filter routes |
| rmap-name | Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-l2vpn-vpls

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp7626241020

---

# Command: retain route-target all

## Syntax
```
[no] retain route-target { all &#124; route-map <rmap-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| retain | Retain the routes based on Target VPN Extended Communities |
| route-target | Specify Target VPN Extended Communities |
| all | All the routes regardless of Target-VPN community |
| route-map | Apply route-map to filter routes |
| rmap-name | Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-vpnv4 /exec/configure/router-bgp/router-bgp-af-vpnv6 /exec/configure/router-bgp/router-bgp-af-link-state
 /exec/configure/router-bgp/router-bgp-af-l2vpn-evpn /exec/configure/router-bgp/router-bgp-af-ipv4-mvpn /exec/configure/router-bgp/router-bgp-af-ipv6-mvpn

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3982969556

---

# Command: retransmit-interval

## Syntax
```
{ { retransmit-interval <interval> } &#124; { no retransmit-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| retransmit-interval | Packet retransmission interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf/router-ospf-vlink /exec/configure/router-ospf/vrf/router-ospf-vlink

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp5332152640

---

# Command: retransmit-interval

## Syntax
```
{ { retransmit-interval <interval> } &#124; { no retransmit-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| retransmit-interval | Packet retransmission interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf3/router-ospf3-vlink /exec/configure/router-ospf3/vrf/router-ospf3-vlink

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp9606147960

---

# Command: retransmit-interval

## Syntax
```
{ { retransmit-interval <interval> } &#124; { no retransmit-interval [ <interval> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| retransmit-interval | Packet retransmission interval |
| interval | (seconds) |

**Command Mode:** /exec/configure/router-ospf/vrf/router-ospf-slink

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2627155782

---

# Command: revision

## Syntax
```
revision <rev-id> &#124; no revision [ <rev-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| revision | Set configuration revision number |
| rev-id | Configuration revision number |

**Command Mode:** /exec/configure/spanning-tree/mst/configuration

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4185512129

---

# Command: revocation-check crl

## Syntax
```
[no] revocation-check { crl [ none ] &#124; none }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| revocation-check | Configure trustpoint revocation check methods |
| crl | Configure revocation check using crl |
| none | (Optional) Configure revocation check using none |
| none | Configure revocation check using none |

**Command Mode:** /exec/configure/trustpoint

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3571139257

---

# Command: rewrite-evpn-rt-asn

## Syntax
```
[ no &#124; default ] rewrite-evpn-rt-asn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| rewrite-evpn-rt-asn | Auto generate RTs for EBGP neighbor |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-evpn

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4077569044

---

# Command: rewrite-rt-asn

## Syntax
```
[ no &#124; default ] rewrite-rt-asn
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| rewrite-rt-asn | Auto generate RTs for EBGP neighbor |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mvpn /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-mvpn

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1467772954

---

# Command: rfc1583compatibility

## Syntax
```
[no] rfc1583compatibility
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| rfc1583compatibility | Configure 1583 compatibility for external path preferences |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp5876314600

---

# Command: rip shutdown

## Syntax
```
[no] rip shutdown
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| rip | RIP configuration commands |
| shutdown | Shutdown RIP on this interface |

**Command Mode:** /exec/configure/if-igp

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp1695493492

---

# Command: rmdir

## Syntax
```
rmdir { <uri0> &#124; <uri1> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| rmdir | Delete a directory |
| uri0 | Delete a directory |
| uri1 | Delete a directory on expansion flash |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp5314770940

---

# Command: rmon alarm absolute rising-threshold falling-threshold

## Syntax
```
rmon alarm <i0> <s0> <i1> { absolute &#124; delta } rising-threshold <i2> [ <i3> ] falling-threshold <i4> [ <i5> ] [ owner <s1>
 ] &#124; no rmon alarm <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rmon | Remote Monitoring |
| alarm | Configure an RMON alarm |
| i0 | Alarm number |
| s0 | MIB object to monitor |
| i1 | Sample interval |
| absolute | Test each sample directly |
| delta | Test delta between samples |
| rising-threshold | Configure the rising threshold |
| i2 | Rising threshold value |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2919079382

---

# Command: rmon event

## Syntax
```
rmon event <i0> [ log ] [ trap <s0> ] [ description <s1> ] [ owner <s2> ] &#124; no rmon event <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rmon | Remote Monitoring |
| event | Configure an RMON event |
| i0 | Event number |
| log | (Optional) Generate RMON log when the event fires |
| trap | (Optional) Generate SNMP trap when event fires |
| s0 | (Optional) SNMP community string |
| description | (Optional) Specify a description of the event |
| s1 | (Optional) Event description |
| owner | (Optional) Specify an owner for the event |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2241621809

---

# Command: rmon hcalarm absolute startupalarm rising-threshold falling-threshold owner

## Syntax
```
rmon hcalarm <i0> <s0> <i1> { absolute &#124; delta } startupalarm <i2> rising-threshold <i3> <i4> falling-threshold <i5> <i6>
 owner <s1> &#124; no rmon hcalarm <i0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rmon | Remote Monitoring |
| hcalarm | Configure an High Capacity RMON alarm |
| i0 | Alarm number |
| s0 | MIB object to monitor |
| i1 | Sample interval |
| absolute | Test each sample directly |
| delta | Test delta between samples |
| startupalarm | Configure alarm type |
| i2 | Startup alarm type, rising(1) falling(2) risingorfalling(3) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3997836166

---

# Command: roaming-eid-prefix

## Syntax
```
{ [ no ] roaming-eid-prefix { <eid-prefix> &#124; <eid-prefix6> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| roaming-eid-prefix | Configures what EID-prefixes allowed to roam |
| eid-prefix | IPv4 roaming EID-prefix |

**Command Mode:** /exec/configure/lisp-dynamic-eid /exec/configure/vrf/lisp-dynamic-eid

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3227090742

---

# Command: role feature-group name

## Syntax
```
[no] role feature-group name <arg6>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| role | Configure roles |
| feature-group | Configure role feature-group |
| name | Feature-group name |
| arg6 | Enter feature-group name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3580138033

---

# Command: role name

## Syntax
```
[no] role name <arg2>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| role | Configure roles |
| name | Enter the role name |
| arg2 | Enter the role name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1424397720

---

# Command: role priority

## Syntax
```
role priority <priority_value> &#124; no role priority
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| role | Role related configuration |
| priority | Configure priority to be used during vPC role (primary/secondary) election |
| priority_value | specify priority value |

**Command Mode:** /exec/configure/vpc-domain

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, qos, R-commands
**Command ID:** wp3419477593

---

# Command: rollback running-config checkpoint

## Syntax
```
rollback running-config { checkpoint <chkpoint_name> &#124; file <file_uri> } [ best-effort &#124; stop-at-first-failure &#124; atomic ]
 [ verbose ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| rollback | Rollback configuration |
| running-config | Rollback running configuration |
| checkpoint | Rollback running configuration to checkpoint |
| chkpoint_name | Checkpoint name |
| file | Rollback running configuration to configuration file |
| file_uri | Checkpoint file path |
| best-effort | (Optional) Skip errors and proceed with rollback |
| stop-at-first-failure | (Optional) Stop rollback at the first error |
| atomic | (Optional) Stop rollback and revert to original configuration (default) |
| verbose | (Optional) Show the execution log |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp4019084536

---

# Command: root-priority

## Syntax
```
[no] root-priority <root-pri>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| root-priority | Set priority with which nodes becomes root |
| root-pri | Root priority value per topology |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common /exec/configure/l2mp-isis/l2mp-isis-l2-topo

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, qos, R-commands
**Command ID:** wp1981641720

---

# Command: route-map

## Syntax
```
route-map <rtmap-name> [ permit &#124; deny ] <seq>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| route-map | Create route-map or enter route-map command mode |
| rtmap-name | Route-map name |
| permit | (Optional) Route map permits set operations |
| deny | (Optional) Route map denies set operations |
| seq | Sequence to insert to/delete from existing route-map entry |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3537469926

---

# Command: route-map

## Syntax
```
route-map <rtmap-name> [ permit &#124; deny ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| route-map | Create route-map or enter route-map command mode |
| rtmap-name | Route-map name |
| permit | (Optional) Route map permits set operations |
| deny | (Optional) Route map denies set operations |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3962865144

---

# Command: route-map

## Syntax
```
[no] route-map { <rtmap-name> &#124; <rtmap-name> } [ permit &#124; deny ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-map | Create route-map or enter route-map command mode |
| rtmap-name | Route-map name |
| rtmap-name | Known route-map name |
| permit | (Optional) Route map permits set operations |
| deny | (Optional) Route map denies set operations |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp4108786540

---

# Command: route-map

## Syntax
```
[no] route-map { <rtmap-name> &#124; <rtmap-name> } [ permit &#124; deny ] <seq>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-map | Create route-map or enter route-map command mode |
| rtmap-name | Route-map name |
| rtmap-name | Known route-map name |
| permit | (Optional) Route map permits set operations |
| deny | (Optional) Route map denies set operations |
| seq | Sequence to insert to/delete from existing route-map entry |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3621374140

---

# Command: route-map out

## Syntax
```
[ no &#124; default ] route-map <rmap-name> { out &#124; in }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| route-map | Apply route-map to neighbor |
| rmap-name | Route-map name |
| out | Apply policy to outgoing routes |
| in | Apply policy to incoming routes |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-vpls /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mvpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-mvpn /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-evpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2208112480

---

# Command: route-map pbr-statistics

## Syntax
```
route-map <route-map-name> pbr-statistics &#124; no route-map { <route-map-name> &#124; <route-map-name> } pbr-statistics
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-map | Create route-map or enter route-map command mode |
| route-map-name | Route-map name |
| route-map-name | Route-map name |
| route-map-name | Known route-map name |
| pbr-statistics | Statistics for policy based routing |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3311125541

---

# Command: route-reflector-client

## Syntax
```
[ no &#124; default ] route-reflector-client
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| route-reflector-client | Configure a neighbor as Route reflector client |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-vpls

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2383914523

---

# Command: route-reflector-client

## Syntax
```
[ no &#124; default ] route-reflector-client
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| route-reflector-client | Configure a neighbor as Route reflector client |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-l2vpn-evpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mvpn /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-mvpn
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-link-state /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1896170140

---

# Command: route-target both

## Syntax
```
{ route-target both { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target both { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2>
 } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| both | Export and Import Target-VPN community |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi-sr

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3190575174

---

# Command: route-target both auto

## Syntax
```
{ route-target both { auto &#124; <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target both { auto &#124; <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| auto | Generate RT automatically |
| both | Export and Import Target-VPN community |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2054610984

---

# Command: route-target both auto

## Syntax
```
{ route-target both { auto &#124; <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } [ evpn &#124; mvpn ] } &#124; { no route-target both [ auto
 [ evpn &#124; mvpn ] &#124; <ext-comm-rt-aa2nn4> [ evpn &#124; mvpn ] &#124; <ext-comm-rt-aa4nn2> [ evpn &#124; mvpn ] ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| both | Export And Import Target-VPN community |
| auto | Generate route target automatically |
| evpn | (Optional) Specify Target for EVPN routes |
| mvpn | (Optional) Specify Target for MVPN routes |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/vrf-af-ipv4 /exec/configure/vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1213846177

---

# Command: route-target export

## Syntax
```
{ route-target export { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target export { <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| export | Export Target-VPN community |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi-sr

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp2650564301

---

# Command: route-target export

## Syntax
```
{ route-target export { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } [ evpn &#124; mvpn ] } &#124; { no route-target export { <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } [ evpn &#124; mvpn ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| export | Export Target-VPN community |
| evpn | (Optional) Specify Target for EVPN routes |
| mvpn | (Optional) Specify Target for MVPN routes |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/vrf-af-ipv4 /exec/configure/vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp7911425100

---

# Command: route-target export auto

## Syntax
```
{ route-target export { auto &#124; <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target export { auto &#124; <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| auto | Generate RT automatically |
| export | Export Target-VPN community |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp3600193114

---

# Command: route-target import

## Syntax
```
{ route-target import { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target import { <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| import | Import Target-VPN community |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi-sr

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp3092949913

---

# Command: route-target import

## Syntax
```
{ route-target import { <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } [ evpn &#124; mvpn ] } &#124; { no route-target import { <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } [ evpn &#124; mvpn ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| import | Import Target-VPN community |
| evpn | (Optional) Specify Target for EVPN routes |
| mvpn | (Optional) Specify Target for MVPN routes |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/vrf-af-ipv4 /exec/configure/vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp2285751225

---

# Command: route-target import auto

## Syntax
```
{ route-target import { auto &#124; <ext-comm-rt-aa2nn4> &#124; <ext-comm-rt-aa4nn2> } } &#124; { no route-target import { auto &#124; <ext-comm-rt-aa2nn4>
 &#124; <ext-comm-rt-aa4nn2> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| route-target | Specify Target VPN Extended Communities |
| import | Import Target-VPN community |
| auto | Generate RT automatically |
| ext-comm-rt-aa4nn2 | RT extcommunity in aa4:nn or ip:nn format |
| ext-comm-rt-aa2nn4 | RT extcommunity in aa:nn format |

**Command Mode:** /exec/configure/evpn/evi

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, R-commands
**Command ID:** wp3777417011

---

# Command: route delete dampen interval

## Syntax
```
[no] route delete dampen interval <time>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| route | Display routing information |
| delete | Dampen route delete update to hardware |
| dampen | Dampen update to hardware |
| interval | Dampen interval |
| time | Dampen interval in seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3494566825

---

# Command: router-guard ip multicast

## Syntax
```
[no] router-guard ip multicast [ vlan <vlan_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router-guard | Configures router guard for all interfaces |
| ip | Configure IP features |
| multicast | router-guard for multicast packet processing |
| vlan | (Optional) Configures router guard for specified vlan only(only in trunk ports) |
| vlan_id | (Optional) Specify vlan-id |

**Command Mode:** /exec/configure/if-switching

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp1921249545

---

# Command: router-guard ip multicast switchports

## Syntax
```
[no] router-guard ip multicast switchports
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router-guard | Configures router guard for all interfaces |
| ip | Configure IP features |
| multicast | router-guard for multicast packet processing |
| switchports | configures on all switchports globally |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, interface, routing, network, R-commands
**Command ID:** wp1985468520

---

# Command: router-id

## Syntax
```
[no] router-id <router-id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router-id | Specify the IP address to use as router-id |
| router-id | Manually configured router identifier |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp4202391238

---

# Command: router-id

## Syntax
```
[no] router-id { <interface> &#124; <rid> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router-id | Router-ID |
| interface | Interface to provide IP address for router-id |
| rid | IP address to become router-id |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv4

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1749244601

---

# Command: router-id

## Syntax
```
{ { router-id <id> } &#124; { no router-id [ <id> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| router-id | Set OSPFv3 process router-id |
| id | Router ID Value |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp6076239940

---

# Command: router-id

## Syntax
```
{ { [ eigrp ] router-id <id> } &#124; { no [ eigrp ] router-id [ <id> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| eigrp | (Optional) EIGRP router configuration commands |
| router-id | router-id for this EIGRP process |
| id | EIGRP Router-ID in IP address format |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2481725106

---

# Command: router-id

## Syntax
```
{ { router-id <id> } &#124; { no router-id [ <id> ] } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| router-id | Set OSPF process router-id |
| id | Router ID Value |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1499762400

---

# Command: router-id

## Syntax
```
router-id [ vrf { <vrf-name> &#124; <vrf-known-name> } ] <interface> [ force ] &#124; no router-id [ { vrf { <vrf-name> &#124; <vrf-known-name>
 } &#124; <interface> [ force ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| router-id | Select interface to prefer for LDP identifier address |
| vrf | (Optional) VRF Routing/Forwarding instance information |
| vrf-name | (Optional) VPN Routing/Forwarding instance name |
| vrf-known-name | (Optional) Known VRF name |
| force | (Optional) Forcibly change the LDP router id |

**Command Mode:** /exec/configure/ldp

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp8773856750

---

# Command: router-preference maximum

## Syntax
```
[no] router-preference maximum <prefopts>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |

**Command Mode:** /exec/configure/config-ra-guard

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp4827599150

---

# Command: router bgp

## Syntax
```
[no] router bgp <as>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| bgp | Border Gateway Protocol (BGP) |
| as | Autonomous |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3804148310

---

# Command: router eigrp

## Syntax
```
[no] router eigrp <eigrp-ptag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| eigrp | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| eigrp-ptag | Process tag |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1260376711

---

# Command: router isis

## Syntax
```
[no] router isis <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| isis | Intermediate System to Intermediate System (IS-IS) |
| tag | Routing process tag |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp3211882956

---

# Command: router ospf

## Syntax
```
[no] router ospf <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| ospf | Open Shortest Path First (OSPF) |
| tag | Process tag |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp1829547252

---

# Command: router ospfv3

## Syntax
```
[no] router ospfv3 <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| ospfv3 | Open Shortest Path First (OSPF) (Version 3) |
| tag | Process tag |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, R-commands
**Command ID:** wp2426487147

---

# Command: router rip

## Syntax
```
[no] router rip <tag>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| router | Enable a routing process |
| rip | Routing Information Protocol (RIP) |
| tag | Process ID |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp4246424729

---

# Command: routing-context vrf

## Syntax
```
routing-context vrf <vrf-known-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| routing-context | Set the routing context |
| vrf | The new routing-context VRF |
| vrf-known-name | Known VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, overlay, R-commands
**Command ID:** wp3917870080

---

# Command: rsakeypair

## Syntax
```
[no] rsakeypair <s0> [ <i0> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| rsakeypair | Configure trustpoint rsa key-pair details |
| s0 | key-pair label |
| i0 | (Optional) key-pair size |

**Command Mode:** /exec/configure/trustpoint

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2687126713

---

# Command: rtr etr eid

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| rtr | Configure RTR in ELP ordered list |
| etr | Configure ETR in ELP ordered list |
| eid | Configure EID in ELP ordered list |
| locator | IPv4 locator for RTR/ETR or EID |
| strict | (Optional) ELP hop must be used in Explicit Locator Path |
| probe | (Optional) RLOC-probe next-hop in ELP |
| seq | Sequence to insert or delete RTR/ETR/EID ELP entry |

**Command Mode:** /exec/configure/lisp-elp /exec/configure/vrf/lisp-elp

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp2297006737

---

# Command: rule

## Syntax
```
rule <number> { <action> } { { <permission> [ <featuretype> <name> ] } } &#124; no rule <number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rule | Enter the rule number |
| number | Enter the rule number |
| action | Action |
| permission | Permission |
| featuretype | (Optional) Feature type |
| name | (Optional) Enter the access entity name |

**Command Mode:** /exec/configure/role

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1485085880

---

# Command: rule command

## Syntax
```
rule <number> { <action> } { command <cmd_line> } &#124; no rule <number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rule | Enter the rule number |
| number | Enter the rule number |
| action | Action |
| command | Command line |
| cmd_line | Enter the command (use space+' ' for command separator) e.g. config t role * |

**Command Mode:** /exec/configure/role

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3594279824

---

# Command: rule oid

## Syntax
```
rule <number> <action> <permission> oid <snmp_oid> &#124; no rule <number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| rule | Enter the rule number |
| number | Enter the rule number |
| action | Action |
| permission | Permission |
| oid | SNMP oid (up to 32 elements) |
| snmp_oid | Enter snmp oid instance name |

**Command Mode:** /exec/configure/role

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp1792245975

---

# Command: run-script

## Syntax
```
run-script <uri0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| run-script | Run shell scripts |
| uri0 | Enter script file name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, routing, network, R-commands
**Command ID:** wp3106586065

---

# Command: run2 guestshell

## Syntax
```
run2 guestshell [ { <cmd_args> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| run2 | execute/run program |
| guestshell | The guest shell Linux-bash |
| cmd_args | (Optional) The command to execute |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp7257875900

---

# Command: run bash

## Syntax
```
run bash [ <cmd> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| run | execute/run program |
| bash | linux-bash |
| cmd | (Optional) the command to execute |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010010.html
**Tags:** config-mode, R-commands
**Command ID:** wp3624186409

---

