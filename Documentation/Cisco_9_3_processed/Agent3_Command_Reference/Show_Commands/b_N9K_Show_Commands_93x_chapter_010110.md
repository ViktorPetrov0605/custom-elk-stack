# Chapter: W Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010110.html
**Type:** Show Commands  
**Chapter:** Group-10110 Commands  
**Total Commands:** 7

## Command List

- `show wred-queue qos-group-map`
- `show wrr-queue qos-group-map`
- `show wrr unicast-bandwidth`
- `show wwn status`
- `show wwn switch`
- `show wwn test`
- `show wwn vsan-wwn`

---

## Detailed Command Reference

# Command: show wred-queue qos-group-map

## Syntax
```
show wred-queue qos-group-map [ __readonly__ TABLE_wred_queue_qos_group_map <wred-queue><qos-group-map> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wred-queue | Show WRED qos-group information |
| qos-group-map | Display mapping of the qos-group information |
| __readonly__ | (Optional) |
| TABLE_wred_queue_qos_group_map | (Optional) XML show wred-queue qos-group-map |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp7987045300

---

# Command: show wrr-queue qos-group-map

## Syntax
```
show wrr-queue qos-group-map [ __readonly__ <mcast_queue_id> [ TABLE_wrr_queue <wrr_queue> [ TABLE_qos_group <qos_group> ]
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wrr-queue | Display mapping of traffic priority (CoS) values to L3 Multicast |
| qos-group-map | Show wrr-queue qos-group-map |
| __readonly__ | (Optional) |
| mcast_queue_id | (Optional) MCAST Queue ID |
| TABLE_wrr_queue | (Optional) Table wrr queue |
| wrr_queue | (Optional) Traffic priority values |
| TABLE_qos_group | (Optional) Table qos group |
| qos_group | (Optional) QoS-Group-Map |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3104942039

---

# Command: show wrr unicast-bandwidth

## Syntax
```
show wrr unicast-bandwidth [ __readonly__ TABLE_wrr_unicast_bandwidth <unicast-bandwidth> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wrr | unicast bandwidth configuration |
| unicast-bandwidth | rate in precentage of data rate |
| __readonly__ | (Optional) |
| TABLE_wrr_unicast_bandwidth | (Optional) XML show wrr unicast-bandwidth |
| unicast-bandwidth | (Optional) unicast bandwidth value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp6537549410

---

# Command: show wwn status

## Syntax
```
show wwn status [ { backplane-prom &#124; block-id <i0> &#124; non-volatile-pss &#124; volatile-pss } ] [ __readonly__ [ TABLE_status <type>
 <configured> <available> <avbl_percent> <resd> <alarm> ] [ <wwn_start> <wwn_end> <num_of_wwn> <allocated_wwn> <available_wwn>
 <alloc_status> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wwn | show wwn information |
| status | Show overall WWN Usage and Alarm Status |
| backplane-prom | (Optional) Show WWN block in backplane PROM |
| block-id | (Optional) Enter a block id. |
| i0 | (Optional) Enter a block id. |
| non-volatile-pss | (Optional) Show contents of non-volatile PSS |
| volatile-pss | (Optional) Show contents of volatile PSS |
| __readonly__ | (Optional) Read Only |
| TABLE_status | (Optional) show wwn status table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2833133397

---

# Command: show wwn switch

## Syntax
```
show wwn switch [ __readonly__ { <sw_wwn> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wwn | show wwn information |
| switch | Show switch WWN |
| __readonly__ | (Optional) Read Only |
| sw_wwn | (Optional) The Switch WWN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1372130683

---

# Command: show wwn test

## Syntax
```
show wwn test { get_swwn_from_pwwn <wwn0> &#124; get_pwwn_from_swwn <wwn1> if_index <i0> &#124; get_ifindex_from_fwwn <wwn2> &#124; get_ifindex_from_pwwn
 <wwn3> &#124; validate_pwwn_given_swwn <wwn4> pwwn <wwn5> &#124; get_all_pwwn_for_slot <i1> &#124; get_kc_type_given_swwn <wwn6> pwwn <wwn7>
 &#124; get_ifindex_from_pwwn_swwn <wwn8> pwwn <wwn9> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show running system information |
| wwn | show wwn information |
| test | show wwn information for testing |
| get_swwn_from_pwwn | show switch wwn from port wwn |
| wwn0 | port wwn |
| get_pwwn_from_swwn | show port wwn from switch wwn |
| wwn1 | switch wwn |
| if_index | interface index |
| i0 | Interface index |
| get_ifindex_from_fwwn | show ifindex from fabric wwn |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1441540450

---

# Command: show wwn vsan-wwn

## Syntax
```
show wwn vsan-wwn [ __readonly__ [ TABLE_wwnvsan <vsan_id> <wwn_conf> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| wwn | show wwn information |
| vsan-wwn | Show all user configured vsan wwn |
| __readonly__ | (Optional) Read Only |
| TABLE_wwnvsan | (Optional) vsan-wwn table |
| vsan_id | (Optional) VSAN ID |
| wwn_conf | (Optional) wwn configured by user |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2961417390

---

