# Chapter: Q Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010001.html
**Type:** Configuration Commands  
**Chapter:** Group-10001 Commands  
**Total Commands:** 14

## Command List

- `qos-mode pipe`
- `qos copy policy-map type network-qos prefix`
- `qos copy policy-map type queuing prefix`
- `qos qos-policies statistics`
- `qos shared-policer`
- `qos statistics`
- `qualify udf`
- `queue-limit`
- `queue-limit2`
- `queue-limit3`
- `queue-limit4`
- `queue-limit bytes`
- `queue-limit retransmit`
- `queue-limit retransmit`

---

## Detailed Command Reference

# Command: qos-mode pipe

## Syntax
```
[no] qos-mode pipe
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| qos-mode | qos-mode |
| pipe | pipe mode |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, network, Q-commands
**Command ID:** wp1232402268

---

# Command: qos copy policy-map type network-qos prefix

## Syntax
```
qos copy policy-map type network-qos <pmap-nq-enum-name-dc3> { prefix &#124; suffix } <ix-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| copy | Copy (Clone) template |
| policy-map | Configure a policy map |
| type | Specify the type of this policy-map |
| network-qos | Network QoS policy |
| prefix | Policy map name prefix |
| suffix | Policy map name suffix |
| ix-name | Suffix/Prefix name, max size counted together with policy name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, Q-commands
**Command ID:** wp2468861999

---

# Command: qos copy policy-map type queuing prefix

## Syntax
```
qos copy policy-map type queuing <pmap-name-que-temp> { prefix &#124; suffix } <ix-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| copy | Copy (Clone) template |
| policy-map | Configure a policy map |
| type | Specify the type of this policy-map |
| queuing | Queuing policy |
| pmap-name-que-temp | Policy-map name |
| prefix | Policy map name prefix |
| suffix | Policy map name suffix |
| ix-name | Suffix/Prefix name, max size counted together with policy name |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, Q-commands
**Command ID:** wp2073296149

---

# Command: qos qos-policies statistics

## Syntax
```
[no] qos qos-policies statistics
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| qos-policies | All qos type policies |
| statistics | statistics |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, Q-commands
**Command ID:** wp1759192595

---

# Command: qos shared-policer

## Syntax
```
{ qos shared-policer [ type qos ] <policer-name> { [ cir ] { <cir-val> [ bps &#124; kbps &#124; mbps &#124; gbps &#124; pps ] &#124; percent <cir-perc>
 } [ [ bc ] { <committed-burst> [ bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us &#124; packets ] } ] [ pir { <pir-val> [ bps2 &#124; kbps2 &#124; mbps2
 &#124; gbps2 &#124; pps2 ] &#124; percent <pir-perc> } [ [ be ] { <extended-burst> [ bytes2 &#124; kbytes2 &#124; mbytes2 &#124; ms2 &#124; us2 &#124; packets2 ]
 } ] ] [ conform { transmit &#124; set-prec-transmit { <prec-val> &#124; <prec-enum> } &#124; set-dscp-transmit { <dscp-val> &#124; <dscp-enum>
 } &#124; set-cos-transmit <cos-val> &#124; set-discard-class-transmit <disc-class-val> &#124; set-qos-transmit <qos-grp-val> &#124; set-mpls-exp-imposition-transmit
 <exp-value-imp> &#124; set-mpls-exp-topmost-transmit <exp-value-top> } ] [ exceed { transmit1 &#124; drop1 &#124; set <exc-frm-field> <exc-to-field>
 table cir-markdown-map &#124; set-prec-transmit1 { <prec-val1> &#124; <prec-enum1> } &#124; set-dscp-transmit1 { <dscp-val1> &#124; <dscp-enum1>
 } &#124; set-cos-transmit1 <cos-val1> &#124; set-discard-class-transmit1 <disc-class-val1> &#124; set-qos-transmit1 <qos-grp-val1> &#124; set-mpls-exp-imposition-transmit1
 <exp-value-imp1> &#124; set-mpls-exp-topmost-transmit1 <exp-value-top1> } ] [ violate { drop2 &#124; set <vio-frm-field> <vio-to-field>
 table2 pir-markdown-map &#124; set-prec-transmit2 { <prec-val2> &#124; <prec-enum2> } &#124; set-dscp-transmit2 { <dscp-val2> &#124; <dscp-enum2>
 } &#124; set-cos-transmit2 <cos-val2> &#124; set-discard-class-transmit2 <disc-class-val2> &#124; set-qos-transmit2 <qos-grp-val2> &#124; set-mpls-exp-imposition-transmit2
 <exp-value-imp2> &#124; set-mpls-exp-topmost-transmit2 <exp-value-top2> } ] } &#124; no qos shared-policer [ type qos ] <policer-name>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| shared-policer | Shared policer |
| policer-name | Shared policer name |
| type | (Optional) Specify the type of shared-policer |
| qos | QoS Global Commands |
| cir | (Optional) Specify committed information rate |
| bc | (Optional) Specify committed burst |
| percent | Specify rate as percentage of interface data-rate |
| cir-perc | Percentage |
| pir-perc | (Optional) Percentage |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, Q-commands
**Command ID:** wp2030656790

---

# Command: qos statistics

## Syntax
```
[no] qos statistics
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| statistics | statistics |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, qos, Q-commands
**Command ID:** wp2992706426

---

# Command: qualify udf

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| udf_tcam_type | Region type |
| qualify | Configure UDFs to be qualified for span region |
| udf | Configure UDF names |
| udf_name | UDF name |

**Command Mode:** /exec/configure/tcam-templ

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp6203668620

---

# Command: queue-limit

## Syntax
```
[no] queue-limit [ cos <cos-val> ] { <q-size> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us ] &#124; percent <perc-q-size> &#124; dynamic
 <alpha> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| queue-limit | Configure queue size for the class |
| cos | (Optional) IEEE 802.1Q Class of Service |
| cos-val | (Optional) 802.1Q Class of Service value |
| percent | Specify queue size in Percentage |
| perc-q-size | Queue size in percentage of total tx/rx buffer size |
| dynamic | Queue size in dynamic alpha factor |
| alpha | 0-1/128, 1-1/64, 2-1/32, 3-1/16, 4-1/8, 5-1/4, 6-1/2, 7-1, 8-2, 9-4, 10-8 |
| packets | (Optional) Packets |
| bytes | (Optional) Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp3143590994

---

# Command: queue-limit2

## Syntax
```
[no] queue-limit2 [ cos2 <cos-val> ] { <q-size> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us ] &#124; percent2 <perc-q-size> &#124;
 dynamic2 <alpha> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| queue-limit2 | Configure queue size for the class |
| cos2 | (Optional) IEEE 802.1Q Class of Service |
| cos-val | (Optional) 802.1Q Class of Service value |
| percent2 | Specify queue size in Percentage |
| perc-q-size | Queue size in percentage of total tx/rx buffer size |
| dynamic2 | Queue size in dynamic alpha factor |
| alpha | 0-1/128, 1-1/64, 2-1/32, 3-1/16, 4-1/8, 5-1/4, 6-1/2, 7-1, 8-2, 9-4, 10-8 |
| packets | (Optional) Packets |
| bytes | (Optional) Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp8302854180

---

# Command: queue-limit3

## Syntax
```
[no] queue-limit3 [ cos3 <cos-val> ] { <q-size> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us ] &#124; percent3 <perc-q-size> &#124;
 dynamic3 <alpha> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| queue-limit3 | Configure queue size for the class |
| cos3 | (Optional) IEEE 802.1Q Class of Service |
| cos-val | (Optional) 802.1Q Class of Service value |
| percent3 | Specify queue size in Percentage |
| perc-q-size | Queue size in percentage of total tx/rx buffer size |
| dynamic3 | Queue size in dynamic alpha factor |
| alpha | 0-1/8, 1-1/4, 2-1/2, 3-3/4, 4-9/8, 5-15/8, 6-3, 7-5, 8-8, 9-14, 10-18 |
| packets | (Optional) Packets |
| bytes | (Optional) Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp4876645470

---

# Command: queue-limit4

## Syntax
```
[no] queue-limit4 [ cos4 <cos-val> ] { <q-size> [ packets &#124; bytes &#124; kbytes &#124; mbytes &#124; ms &#124; us ] &#124; percent4 <perc-q-size> &#124;
 dynamic4 <alpha> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| queue-limit4 | Configure queue size for the class |
| cos4 | (Optional) IEEE 802.1Q Class of Service |
| cos-val | (Optional) 802.1Q Class of Service value |
| percent4 | Specify queue size in Percentage |
| perc-q-size | Queue size in percentage of total tx/rx buffer size |
| dynamic4 | Queue size in dynamic alpha factor |
| alpha | 0-3/2, 1-3, 2-6, 3-11, 4-20, 5-33, 6-50, 7-66, 8-80 |
| packets | (Optional) Packets |
| bytes | (Optional) Bytes |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp3155288635

---

# Command: queue-limit bytes

## Syntax
```
[no] queue-limit { <q-size> bytes }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| queue-limit | Configure queue size for the class |
| bytes | Bytes |

**Command Mode:** /exec/configure/policy-map/type/uf/class

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp2960985642

---

# Command: queue-limit retransmit

## Syntax
```
queue-limit retransmit { <qlimit> &#124; unlimited } &#124; no queue-limit retransmit [ <qlimit> &#124; unlimited ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| queue-limit | Set maximum queue size |
| retransmit | Set maximum size of retransmit queue |
| qlimit | Maximum number of LSPs in retransmit queue |
| unlimited | Unlimited retransmit queue |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp2937383073

---

# Command: queue-limit retransmit

## Syntax
```
queue-limit retransmit { <qlimit> &#124; unlimited } &#124; no queue-limit retransmit [ <qlimit> &#124; unlimited ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| queue-limit | Set maximum queue size |
| retransmit | Set maximum size of retransmit queue |
| qlimit | Maximum number of LSPs in retransmit queue |
| unlimited | Unlimited retransmit queue |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010001.html
**Tags:** config-mode, Q-commands
**Command ID:** wp5053388640

---

