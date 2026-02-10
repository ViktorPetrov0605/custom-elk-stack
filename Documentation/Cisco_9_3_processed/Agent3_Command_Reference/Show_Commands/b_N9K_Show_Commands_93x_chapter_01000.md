# Chapter: H Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01000.html
**Type:** Show Commands  
**Chapter:** Group-1000 Commands  
**Total Commands:** 60

## Command List

- `show hardware`
- `show hardware access-list lou resource threshold`
- `show hardware access-list resource pooling`
- `show hardware access-list tcam`
- `show hardware capacity`
- `show hardware capacity eobc`
- `show hardware capacity fabric-utilization`
- `show hardware capacity forwarding`
- `show hardware capacity interface`
- `show hardware capacity module`
- `show hardware capacity power`
- `show hardware fabricpath mac-learning module`
- `show hardware feature-capability`
- `show hardware flow aging`
- `show hardware flow entry address type`
- `show hardware flow etrap`
- `show hardware flow ip`
- `show hardware flow ipv6`
- `show hardware flow l2`
- `show hardware flow mpls`
- `show hardware flow sampler`
- `show hardware flow utilization`
- `show hardware forwarding interface statistics mode`
- `show hardware forwarding memory health detail`
- `show hardware forwarding memory health summary`
- `show hardware ip verify`
- `show hardware profile buffer monitor show hardware profile buffer monitor internal`
- `show hardware profile forwarding-mode`
- `show hardware profile latency monitor sampling show hardware profile latency monitor`
- `show hardware profile module`
- `show hardware profile packet-drop`
- `show hardware profile status`
- `show hardware profile tcam region`
- `show hardware qos afd profile`
- `show hardware qos burst-detect max-records`
- `show hardware qos eoq stats-class`
- `show hardware qos include ipg`
- `show hardware qos ing-pg-hdrm-reserve`
- `show hardware qos ing-pg-no-min`
- `show hardware qos ing-pg-share`
- `show hardware qos min-buffer`
- `show hardware qos ns-buffer-profile`
- `show hardware qos ns-mcq3-alias`
- `show hardware rate-limiter`
- `show hardware rate-limiter`
- `show hardware rate-limiter span-egress`
- `show hardware rl snmp class-id`
- `show hardware rl snmp global class-id`
- `show hardware rl snmp local snmp-index class-id`
- `show hostname`
- `show hosts`
- `show hsrp`
- `show hsrp anycast`
- `show hsrp anycast interface vlan`
- `show hsrp anycast remote-db`
- `show hsrp anycast summary`
- `show hsrp bfd-sessions`
- `show hsrp delay`
- `show hsrp mgo`
- `show hsrp summary`

---

## Detailed Command Reference

# Command: show hardware

## Syntax
```
show hardware [ __readonly__ <header_str> <bios_ver_str> [ <loader_ver_str> ] <kickstart_ver_str> <nxos_ver_str> [ <sys_ver_str>
 ] <bios_cmpl_time> <kick_file_name> <nxos_file_name> <kick_cmpl_time> <nxos_cmpl_time> <kick_tmstmp> <nxos_tmstmp> [ <isan_file_name>
 ] [ <isan_cmpl_time> ] [ <isan_tmstmp> ] <chassis_id> [ <module_id> ] <cpu_name> <memory> <mem_type> <proc_board_id> [ <host_name>
 ] <bootflash_size> [ <slot0_size> ] [ <slot1_size> ] <kern_uptm_days> <kern_uptm_hrs> <kern_uptm_mins> <kern_uptm_secs> [
 <rr_usecs> ] [ <rr_ctime> ] <rr_reason> [ <rr_sys_ver> ] [ <rr_service> ] <plugins> [ <manufacturer> ] { TABLE_slot [ TABLE_slot_info
 [ [ <num_slot_str> ] [ <status_ok_empty> ] [ [ <type> [ <num_submods> ] ] <model_num> <hw_ver> <part_num> <part_revision>
 <manuf_date> <serial_num> <CLEI_code> [ <num_slot_str> ] ] ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| __readonly__ | (Optional) |
| header_str | (Optional) |
| bios_ver_str | (Optional) |
| loader_ver_str | (Optional) |
| kickstart_ver_str | (Optional) |
| nxos_ver_str | (Optional) |
| sys_ver_str | (Optional) |
| bios_cmpl_time | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp4734633620

---

# Command: show hardware access-list lou resource threshold

## Syntax
```
show hardware access-list lou resource threshold [ __readonly__ { current [ { lou [ { resource [ { threshold [ { <threshold_value>
 } ] } ] } ] } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| access-list | Access Control List |
| lou | LOU |
| resource | hardware resource |
| threshold | port expansion threshold |
| __readonly__ | (Optional) |
| current | (Optional) |
| lou | (Optional) |
| resource | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp2957833171

---

# Command: show hardware access-list resource pooling

## Syntax
```
show hardware access-list resource pooling [ __readonly__ <mod-num> <status> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| access-list | Access Control List |
| resource | Hardware resource |
| pooling | ACL programming across TCAM banks |
| __readonly__ | (Optional) |
| mod-num | (Optional) module number |
| status | (Optional) Banchaining status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp2120381967

---

# Command: show hardware access-list tcam

## Syntax
```
show hardware access-list tcam { { template { nfe &#124; nfe2 &#124; l2-l3 &#124; l3 &#124; <name> &#124; all } } &#124; { region } } [ __readonly__ { TCAM_Region
 [ { TABLE_Sizes <type> <tcam_size> <tcam_width> } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| access-list | Access Control List |
| tcam | Show tcam parameters |
| region | Show tcam region sizes |
| __readonly__ | (Optional) |
| TCAM_Region | (Optional) |
| TABLE_Sizes | (Optional) |
| type | (Optional) |
| tcam_size | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp9839347060

---

# Command: show hardware capacity

## Syntax
```
show hardware capacity
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | Hardware usage levels for Power, Switching Fabric, Flash, etc |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp4081766045

---

# Command: show hardware capacity eobc

## Syntax
```
show hardware capacity eobc [ __readonly__ { eobc_usage [ <eobc_tx_pps> ] [ <eobc_tx_packets> ] [ <eobc_tx_dropped> ] [ <eobc_rx_pps>
 ] [ <eobc_rx_packets> ] [ <eobc_rx_dropped> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | resource inventory and/or usage level |
| eobc | EOBC resources |
| __readonly__ | (Optional) |
| eobc_usage | (Optional) |
| eobc_tx_packets | (Optional) |
| eobc_tx_dropped | (Optional) |
| eobc_tx_pps | (Optional) |
| eobc_rx_packets | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2810642210

---

# Command: show hardware capacity fabric-utilization

## Syntax
```
show hardware capacity fabric-utilization [ __readonly__ { TABLE_fabutil <mod> <bandwidth> <ingress> <egress> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| capacity | resource inventory and/or usage level |
| fabric-utilization | Show per module Fabric utilization |
| __readonly__ | (Optional) |
| TABLE_fabutil | (Optional) fabric utilization table |
| mod | (Optional) |
| bandwidth | (Optional) |
| ingress | (Optional) |
| egress | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1625046945

---

# Command: show hardware capacity forwarding

## Syntax
```
show hardware capacity forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | Hardware usage levels for Power, Switching Fabric, Flash, etc |
| forwarding | L2/L3 Forwarding resources |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3306232922

---

# Command: show hardware capacity interface

## Syntax
```
show hardware capacity interface [ __readonly__ { TABLE_moddrops <mod_num_drops> <tx_drops> <rx_drops> <max_tx_port> <max_rx_port>
 } { TABLE_modbuffers <mod_num_buffers> <tx_buffers> <rx_buffers> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | Usage levels |
| interface | Interface Resources - Tx/Rx drops and Tx/Rx buffers |
| __readonly__ | (Optional) Read Only |
| mod_num_drops | (Optional) Module number for Tx/Rx drops |
| TABLE_moddrops | (Optional) show module |
| tx_drops | (Optional) Tx drops |
| rx_drops | (Optional) Rx drops |
| max_tx_port | (Optional) Port with max Tx drops |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3366554284

---

# Command: show hardware capacity module

## Syntax
```
show hardware capacity module [ __readonly__ { sup_ha_status [ <sup_ha_admin_status> ] [ <sup_ha_oper_status> ] [ <dual_sup_hw_state>
 ] [ <redundancy_state> ] } { switch_resouces { TABLE_lcinfo <mod_num> <model_num> <part_num> <serial_num> } [ { TABLE_xbarinfo
 <mod_num1> <model_num1> <part_num1> <serial_num1> } ] } { TABLE_flash_nvram_info <mod_num2> <dev_name> <total_bytes> <free_bytes>
 <percent_used> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | resource inventory and/or usage level |
| module | SUP, LC, XBAR |
| __readonly__ | (Optional) |
| sup_ha_status | (Optional) |
| sup_ha_admin_status | (Optional) |
| sup_ha_oper_status | (Optional) |
| dual_sup_hw_state | (Optional) |
| redundancy_state | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3124473716

---

# Command: show hardware capacity power

## Syntax
```
show hardware capacity power [ __readonly__ { power_summary <ps_redun_mode_admin> <ps_redun_mode_oper> <power_total> <power_rsvd>
 <power_rsvd_percent> <power_given_mod> <power_given_mod_percent> <power_avail> <power_avail_percent> <power_out_actual_draw>
 <power_input_actual_draw> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Hardware related |
| capacity | resource inventory and/or usage level |
| power | power summary |
| __readonly__ | (Optional) |
| power_summary | (Optional) |
| ps_redun_mode_admin | (Optional) Mode: Redundant or Non-redundant |
| ps_redun_mode_oper | (Optional) Mode: Redundant or Non-redundant |
| power_total | (Optional) |
| power_rsvd | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp4057629126

---

# Command: show hardware fabricpath mac-learning module

## Syntax
```
show hardware fabricpath mac-learning module <module> [ __readonly__ { [ { TABLE_module <module_num> <port_group> <mac_learning>
 } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| fabricpath | Fabric Path |
| mac-learning | MAC Learning |
| module | Specify a module number |
| module | Specify a module number |
| __readonly__ | (Optional) |
| TABLE_module | (Optional) |
| module_num | (Optional) Specify a module number |
| port_group | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1138228687

---

# Command: show hardware feature-capability

## Syntax
```
show hardware feature-capability [ detailed ] [ __readonly__ [ { TABLE_feature_support <feature_name> [ { TABLE_mod_support
 <mod_inst> <support> } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| feature-capability | show registered features supported |
| detailed | (Optional) detailed |
| __readonly__ | (Optional) Read_Only |
| TABLE_feature_support | (Optional) show features supported |
| feature_name | (Optional) feature name |
| TABLE_mod_support | (Optional) show registered features supported |
| mod_inst | (Optional) module instance |
| support | (Optional) support details |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3605470340

---

# Command: show hardware flow aging

## Syntax
```
show hardware flow aging [ instance <inst> ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| aging | Aging Info |
| instance | (Optional) Instance |
| inst | (Optional) Earl Instance |
| module | (Optional) Line card module |
| num | (Optional) slot number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1701778157

---

# Command: show hardware flow entry address type

## Syntax
```
show hardware flow entry address <addr> type { ip &#124; ipv6 &#124; l2 &#124; mpls } [ instance <inst> ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| entry | Netflow Table Entry |
| address | Netflow Table Address |
| addr | Netflow Table Address |
| type | Flow Type |
| ip | Internet Protocol Version 4 |
| ipv6 | Internet Protocol Version 6 |
| l2 | Layer 2 Protocol |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2972207807

---

# Command: show hardware flow etrap

## Syntax
```
show hardware flow etrap [ module <module> ] [ { unit <unit> slice <slice> } ] [ __readonly__ [ { TABLE_etrap_flows <unit>
 <slice> <index> <keytype> <src_addr> <dst_addr> <src_port> <dst_port> <proto> <rate> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Traffic flow information |
| etrap | Elephant Trap information |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| unit | (Optional) Asic Number |
| unit | (Optional) Asic Number on the module |
| slice | (Optional) slice num on asic |
| slice | (Optional) slice number on asic |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2018337895

---

# Command: show hardware flow ip

## Syntax
```
show hardware flow ip [ { { monitor <mname> } &#124; { profile <prof_id> } &#124; { vlan <vlan_id> } &#124; { interface <interface> } } ]
 [ instance <inst> ] [ detail ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| ip | Internet Protocol Version 4 |
| monitor | (Optional) Netflow Flow Monitor |
| mname | (Optional) Netflow Flow Monitor Name |
| profile | (Optional) Flow Profile |
| prof_id | (Optional) Netflow Profile ID |
| vlan | (Optional) Vlan commands |
| vlan_id | (Optional) VLAN ID 1-4094 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp3642945305

---

# Command: show hardware flow ipv6

## Syntax
```
show hardware flow ipv6 [ { { monitor <mname> } &#124; { profile <prof_id> } &#124; { vlan <vlan_id> } &#124; { interface <interface> } }
 ] [ instance <inst> ] [ detail ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| ipv6 | Internet Protocol Version 6 |
| monitor | (Optional) Netflow Flow Monitor |
| mname | (Optional) Netflow Flow Monitor Name |
| profile | (Optional) Flow Profile |
| prof_id | (Optional) Netflow Profile ID |
| vlan | (Optional) Vlan commands |
| vlan_id | (Optional) VLAN ID 1-4094 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp2814487329

---

# Command: show hardware flow l2

## Syntax
```
show hardware flow l2 [ { { monitor <mname> } &#124; { profile <prof_id> } &#124; { vlan <vlan_id> } } ] [ instance <inst> ] [ detail
 ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| l2 | Layer 2 Protocol |
| monitor | (Optional) Netflow Flow Monitor |
| mname | (Optional) Netflow Flow Monitor Name |
| profile | (Optional) Flow Profile |
| prof_id | (Optional) Netflow Profile ID |
| vlan | (Optional) Vlan commands |
| vlan_id | (Optional) VLAN ID 1-4094 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2207876520

---

# Command: show hardware flow mpls

## Syntax
```
show hardware flow mpls [ { { monitor <mname> } &#124; { profile <prof_id> } &#124; { vlan <vlan_id> } &#124; { interface <interface> } }
 ] [ instance <inst> ] [ detail ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| mpls | MPLS Protocol |
| monitor | (Optional) Netflow Flow Monitor |
| mname | (Optional) Netflow Flow Monitor Name |
| profile | (Optional) Flow Profile |
| prof_id | (Optional) Netflow Profile ID |
| vlan | (Optional) Vlan commands |
| vlan_id | (Optional) VLAN ID 1-4094 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1475479780

---

# Command: show hardware flow sampler

## Syntax
```
show hardware flow sampler { all &#124; count &#124; index <index> &#124; name <sname> } [ detail ] [ instance <inst> ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| sampler | Flow Sampler |
| all | Netflow Sampler Usage |
| count | Netflow Sampler Utilization |
| index | Netflow Sampler Index |
| index | Netflow Sampler Index |
| name | Netflow Sampler Name |
| sname | Netflow Sampler Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp5812727350

---

# Command: show hardware flow utilization

## Syntax
```
show hardware flow utilization [ instance <inst> ] [ module <num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| flow | Netflow Module |
| utilization | NT Table Utilization |
| instance | (Optional) Instance |
| inst | (Optional) Earl Instance |
| module | (Optional) Line card module |
| num | (Optional) slot number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp7927451400

---

# Command: show hardware forwarding interface statistics mode

## Syntax
```
show hardware forwarding interface statistics mode [ __readonly__ { system [ { <sysmode> } ] [ { TABLE_module <module> <modmode>
 } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| forwarding | Show hardware information for forwarding path |
| interface | Interface |
| statistics | Statistics |
| mode | Statistics mode |
| __readonly__ | (Optional) |
| system | (Optional) |
| sysmode | (Optional) |
| TABLE_module | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3644438809

---

# Command: show hardware forwarding memory health detail

## Syntax
```
show hardware forwarding memory health detail [ __readonly__ { memscan_interval <mscan_interval> } { memscan_rate <mscan_rate>
 } [ TABLE_ser <table_name> <entry_count> <table_head> <table_tail> [ TABLE_ser_entry_new <n_entry_index> [ <reg_id> ] [ <reg_port>
 ] [ <reg_index> ] [ <table_id> ] [ <table_index> ] <detections> <corrections> [ <last_detection_ts> ] [ <last_correction_ts>
 ] ] [ TABLE_ser_entry_old <o_entry_index> <mem_addr> <cause_bits> <event_type> <last_event> <last_time> ] ] [ { parity_detect_counter
 <parity_detect_cnt> } ] [ { parity_correct_counter <parity_correct_cnt> } ] [ { reg_parity_detect_counter <reg_parity_detect_cnt>
 } ] [ { reg_parity_correct_counter <reg_parity_correct_cnt> } ] [ { tcam_parity_detect_counter <tcam_parity_detect_cnt> }
 ] [ { tcam_parity_correct_counter <tcam_parity_correct_cnt> } ] [ { sram_parity_detect_counter <sram_parity_detect_cnt> }
 ] [ { sram_parity_correct_counter <sram_parity_correct_cnt> } ] [ { TABLE_ser_tbl_parity <table_id> <detections> <corrections>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| forwarding | forwarding information |
| memory | memory information |
| health | memory health information |
| detail | show the detail |
| __readonly__ | (Optional) Read Only |
| memscan_interval | (Optional) memory scan interval value |
| mscan_interval | (Optional) mem scan interval |
| memscan_rate | (Optional) memory scan rate value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1864193339

---

# Command: show hardware forwarding memory health summary

## Syntax
```
show hardware forwarding memory health summary [ __readonly__ [ { parity_detect_counter <parity_detect_cnt> } ] [ { parity_correct_counter
 <parity_correct_cnt> } ] [ { reg_parity_detect_counter <reg_parity_detect_cnt> } ] [ { reg_parity_correct_counter <reg_parity_correct_cnt>
 } ] [ { tcam_parity_detect_counter <tcam_parity_detect_cnt> } ] [ { tcam_parity_correct_counter <tcam_parity_correct_cnt>
 } ] [ { sram_parity_detect_counter <sram_parity_detect_cnt> } ] [ { sram_parity_correct_counter <sram_parity_correct_cnt>
 } ] [ { TABLE_ser_tbl_parity <table_id> <detections> <corrections> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| forwarding | forwarding information |
| memory | memory information |
| health | memory health information |
| summary | show the summary |
| __readonly__ | (Optional) Read Only |
| parity_detect_counter | (Optional) parity detect count |
| parity_detect_cnt | (Optional) count of parity detect |
| parity_correct_counter | (Optional) parity correct count |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp9074453090

---

# Command: show hardware ip verify

## Syntax
```
show hardware [ forwarding ] ip verify [ module <module> ] [ __readonly__ <info_str> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| forwarding | (Optional) Show hardware information for forwarding path |
| ip | IP |
| verify | Show IP packet verification checks enabled in hardware |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| info_str | (Optional) IDS Check Stats |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp1315628200

---

# Command: show hardware profile buffer monitor show hardware profile buffer monitor internal

## Syntax
```
show hardware profile buffer monitor [ interface <intf-num> &#124; buffer-block <buf-blk> &#124; multicast <mcst-blk> ] { brief &#124; detail
 [ last <samples-per-intf> ] &#124; sampling } [ module <module> ] &#124; show hardware profile buffer monitor { internal-raw &#124; summary
 [ module <module> ] } [ __readonly__ <cmd_name> <cmd_issue_time> [ TABLE_summary <summary_util_name> <summary_1sec_util> <summary_5sec_util>
 <summary_60sec_util> <summary_5min_util> <summary_1hr_util> <summary_total_buffer> <summary_class_threshold> ] [ TABLE_ucst_hdr
 <ucst_hdr_util_name> <ucst_hdr_1sec_util> <ucst_hdr_5sec_util> <ucst_hdr_60sec_util> <ucst_hdr_5min_util> <ucst_hdr_1hr_util>
 <ucst_hdr_total_buffer> <ucst_hdr_class_threshold> ] [ TABLE_brief_entry <brief_util_name> <brief_1sec_util> <brief_5sec_util>
 <brief_60sec_util> <brief_5min_util> <brief_1hr_util> ] [ TABLE_mcst_hdr <mcst_hdr_util_name> <mcst_hdr_1sec_util> <mcst_hdr_5sec_util>
 <mcst_hdr_60sec_util> <mcst_hdr_5min_util> <mcst_hdr_1hr_util> <mcst_hdr_total_buffer> <mcst_hdr_class_threshold> ] [ TABLE_detail_entry
 <detail_util_name> <detail_util_state> <time_stamp> <384k_util> <768k_util> <1152k_util> <1536k_util> <1920k_util> <2304k_util>
 <2688k_util> <3072k_util> <3456k_util> <3840k_util> <4224k_util> <4608k_util> <4992k_util> <5376k_util> <5760k_util> <6144k_util>
 ] [ TABLE_sampling <sampling_interval> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware profile buffer monitor data |
| profile | profile buffer monitor data |
| buffer | buffer |
| monitor | buffer monitor |
| interface | (Optional) show buffer monitoring data of an interface |
| intf-num | (Optional) show buffer monitoring data of an interface |
| buffer-block | (Optional) buffer block |
| buf-blk | (Optional) buffer block |
| multicast | (Optional) multicast buffer block |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3680455381

---

# Command: show hardware profile forwarding-mode

## Syntax
```
show hardware profile forwarding-mode [ __READONLY__ <forwarding-mode> [ <host-size> ] [ <unicast-size> ] [ <unicast-rpf-size>
 ] [ <unicast-ipv4-size> ] [ <unicast-ipv4-rpf-size> ] [ <unicast-ipv6-size> ] [ <multicast-size> ] [ <l2-size> ] [ <unified-size>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware profile forwarding-mode |
| profile | profile forwarding-mode |
| forwarding-mode | forwarding-mode |
| __READONLY__ | (Optional) |
| forwarding-mode | (Optional) |
| host-size | (Optional) |
| unicast-size | (Optional) |
| unicast-rpf-size | (Optional) |
| unicast-ipv4-size | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2286510151

---

# Command: show hardware profile latency monitor sampling show hardware profile latency monitor

## Syntax
```
show hardware profile latency monitor { sampling &#124; threshold } [ module <module> ] &#124; show hardware profile latency monitor
 { { summary [ detail &#124; clear-timestamp ] } [ interface <intf-num> ] &#124; { summary [ brief &#124; sort &#124; top ] } &#124; { raw [ verbose
 ] } [ module <module> ] } [ __readonly__ <cmd_issue_time> <device_instance> [ TABLE_sampling <sampling_interval> ] [ TABLE_threshold
 <threshold_avg> <threshold_max> ] [ TABLE_summary <summary_egress_port> <summary_sampling_interval> <summary_min_latency>
 <summary_max_latency> <summary_avg_latency> <summary_std_deviation> ] [ TABLE_detail <detail_timestamp> <detail_ifindex> <detail_fcnt>
 <detail_min_latency> <detail_max_latency> <detail_avg_latency> ] [ TABLE_brief <brief_egress_port> <brief_avg_latency> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware profile latency monitor data |
| profile | profile latency monitor data |
| latency | latency |
| monitor | latency monitor |
| sampling | show sampling interval |
| threshold | show threshold configured |
| summary | show switch-wide latency monitor data |
| detail | (Optional) show switch-wide or per-interface raw latency monitor data |
| clear-timestamp | (Optional) show switch-wide or per-interface latency clear timestamp |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1686853115

---

# Command: show hardware profile module

## Syntax
```
show hardware profile module <module> [ __readonly__ { TABLE_profile <slot> <type> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware profile |
| profile | Profile settings |
| module | Enter module number |
| __readonly__ | (Optional) |
| TABLE_profile | (Optional) Show version info |
| slot | (Optional) Slot |
| type | (Optional) Profile type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp4080997898

---

# Command: show hardware profile packet-drop

## Syntax
```
show hardware profile packet-drop { status &#124; data [ instance <cap_instance> ] &#124; event [ instance <cap_instance> ] } [ __readonly__
 [ <enable><state> <cap-scope><drop-trigger> <cap-count><cap-time> <file-inst> ] [ TABLE_hardware_packet_drop_status <profile-name><start-thres><stop-thres>
 ] [ TABLE_hardware_packet_drop_data <src-port><dst-port> <qos-grp><que-depth> <payload> ] [ TABLE_hardware_packet_drop_event
 <src-port><dst-port> <qos-grp><que-depth> <drop-reason> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Change hardware usage settings |
| profile | Profile settings |
| packet-drop | Packet Drop parameters |
| status | Packet Drop status |
| data | Packet Drop circular-buffer data |
| instance | (Optional) Packet Drop captured instance |
| cap_instance | (Optional) Value 1-5 |
| event | Packet Drop event-buffer data |
| instance | (Optional) Packet Drop captured instance |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1354595549

---

# Command: show hardware profile status

## Syntax
```
show hardware profile status [ module <module> ] [ detail ] [ __readonly__ { <total_lpm> <total_host> <reserved_lpm> <max_host4_limit>
 <max_host6_limit> <max_mcast_limit> <max_mcast6_limit> [ <max_mcast_transit_route_limit> ] [ <max_v6_lpm_limit> ] [ <max_v6_lpm_65_to_127_limit>
 ] [ <used_lpm_total> ] <used_v4_lpm> <used_v6_lpm> [ <used_v6_lpm_128> ] <used_host_lpm_total> <used_host_v4_lpm> <used_host_v6_lpm>
 <used_mcast> <used_mcast6> [ <used_mcast_transit_routes> ] <used_mcast_oifl> <used_host_in_host_total> <used_host4_in_host>
 <used_host6_in_host> <max_ecmp_table_limit> <used_ecmp_table> <max_ecmp_nh_table_limit> <used_ecmp_nh_table> [ <mfib_fd_status>
 ] [ <mfib_fd_maxroute> ] [ <mfib_fd_count> ] [ <lpm_to_host_migrate_table> ] [ <host_to_lpm_migrate_table> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware usage settings |
| profile | Show current table usage |
| status | Show status of dynamic resource allocation |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| detail | (Optional) Show detailed information |
| __readonly__ | (Optional) Read only |
| total_lpm | (Optional) Total LPM Entries |
| total_host | (Optional) Total Host Entries |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp8065187600

---

# Command: show hardware profile tcam region

## Syntax
```
show hardware profile tcam region [ __readonly__ { TCAM_Region [ { TABLE_Sizes <tcam_compat_type> <tcam_compat_size> <tcam_compat_width>
 } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| profile | profile |
| tcam | Show tcam parameters |
| region | Show tcam region sizes |
| __readonly__ | (Optional) |
| TCAM_Region | (Optional) |
| TABLE_Sizes | (Optional) |
| tcam_compat_type | (Optional) |
| tcam_compat_size | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1277757194

---

# Command: show hardware qos afd profile

## Syntax
```
show hardware qos afd profile [ module <module> ] [ __readonly__ TABLE_qos_afd_profile <module> <prof-desc> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| afd | Show Approximate Fair Dropping config |
| profile | Show AFD profile config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_afd_profile | (Optional) the xml qos_afd_profile configuration |
| prof-desc | (Optional) profile description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2688311339

---

# Command: show hardware qos burst-detect max-records

## Syntax
```
show hardware qos burst-detect max-records [ __readonly__ TABLE_qos_burstdetect_maxrecords ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| burst-detect | Show oobst burst-detect info |
| max-records | Show oobst burst-detect max-records |
| __readonly__ | (Optional) |
| TABLE_qos_burstdetect_maxrecords | (Optional) the xml qos_burst-detect max-records configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2037198629

---

# Command: show hardware qos eoq stats-class

## Syntax
```
show hardware qos eoq stats-class [ module <module> ] [ __readonly__ TABLE_qos_eoq_stats_class [ <module> ] <eoq-stats-class-desc>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show QoS related information |
| eoq | Show Extended Output Queue(EOQ) related information |
| stats-class | Show EOQ Statistics class selection config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_eoq_stats_class | (Optional) the xml qos_eoq_stats_class configuration |
| eoq-stats-class-desc | (Optional) selected class description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3731615116

---

# Command: show hardware qos include ipg

## Syntax
```
show hardware qos include ipg [ module <module> ] [ __readonly__ TABLE_qos_include_ipg <module> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| include | Show inlcude config |
| ipg | Show whether to include IPG in Shaping/Policing config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_include_ipg | (Optional) the xml qos_include_ipg configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, network, S-commands
**Command ID:** wp1207842898

---

# Command: show hardware qos ing-pg-hdrm-reserve

## Syntax
```
show hardware qos ing-pg-hdrm-reserve [ module <module> ] [ __readonly__ TABLE_qos_ing_pg_hdrm_reserve <module> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| ing-pg-hdrm-reserve | Show ing-pg-hdrm-reserve config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_ing_pg_hdrm_reserve | (Optional) the xml qos_ing_pg_hdrm_reserve configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1914763769

---

# Command: show hardware qos ing-pg-no-min

## Syntax
```
show hardware qos ing-pg-no-min [ module <module> ] [ __readonly__ TABLE_qos_ing_pg_no_min [ <module> ] <ingress_pg_min> <pg_min_value>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| ing-pg-no-min | Show ing-pg-no-min config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_ing_pg_no_min | (Optional) the xml qos_ing_pg_no_min configuration |
| ingress_pg_min | (Optional) Enable/Disable PG Min |
| pg_min_value | (Optional) PG Min Value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3996183495

---

# Command: show hardware qos ing-pg-share

## Syntax
```
show hardware qos ing-pg-share [ module <module> ] [ __readonly__ TABLE_qos_ing_pg_share <module> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| ing-pg-share | Show ing-pg-share config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_ing_pg_share | (Optional) the xml qos_ing_pg_share configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3198312825

---

# Command: show hardware qos min-buffer

## Syntax
```
show hardware qos min-buffer [ module <module> ] [ __readonly__ TABLE_qos_min_buffer_profile [ <module> ] <buff-prof-desc>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| min-buffer | Show min-buffer config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_min_buffer_profile | (Optional) the xml qos_min_buffer_profile configuration |
| buff-prof-desc | (Optional) buffer profile description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3511308210

---

# Command: show hardware qos ns-buffer-profile

## Syntax
```
show hardware qos ns-buffer-profile [ module <module> ] [ __readonly__ TABLE_qos_ns_buffer_profile <module> <buff-prof-desc>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show qos related information |
| ns-buffer-profile | Show ns-buffer-profile config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_ns_buffer_profile | (Optional) the xml qos_ns_buffer_profile configuration |
| buff-prof-desc | (Optional) buffer profile description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2033642299

---

# Command: show hardware qos ns-mcq3-alias

## Syntax
```
show hardware qos ns-mcq3-alias [ module <module> ] [ __readonly__ TABLE_qos_ns_mcq3_alias <module> <ns-mcq3-alias-desc> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| qos | Show QoS related information |
| ns-mcq3-alias | Show NS mc-queue-3 alias class selection config |
| module | (Optional) Specify a module number |
| module | (Optional) Specify a module number |
| __readonly__ | (Optional) |
| TABLE_qos_ns_mcq3_alias | (Optional) the xml qos_ns_mcq3_alias configuration |
| ns-mcq3-alias-desc | (Optional) selected class description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3891865782

---

# Command: show hardware rate-limiter

## Syntax
```
show hardware rate-limiter [ module <module> ] [ layer-3 { <l3-opts> &#124; multicast <mcast-opts> } &#124; layer-2 <l2-opts> &#124; <opts>
 &#124; f1 <f1-opts> &#124; span-egress &#124; urpf-fail ] [ __readonly__ TABLE_hardware_rate_limiter <rate-limit-class> <class-descr> <module>
 <rate-limit-configured> [ <rate-limit-allowed> ] [ <rate-limit-dropped> ] [ <rate-limit-total> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rate-limiter | Show Rate-Limiter configs and statistics |
| layer-3 | (Optional) Layer-3 control and Routed packets |
| l3-opts | (Optional) |
| multicast | (Optional) Multicast data packets |
| mcast-opts | (Optional) |
| layer-2 | (Optional) Layer-2 control and Bridged packets |
| l2-opts | (Optional) |
| opts | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2370598246

---

# Command: show hardware rate-limiter

## Syntax
```
show hardware rate-limiter [ module <module> ] [ layer-3 { <l3-opts> &#124; multicast <mcast-opts> } &#124; layer-2 <l2-opts> &#124; <opts>
 &#124; f1 <f1-opts> &#124; span-egress &#124; urpf-fail ] [ __readonly__ TABLE_hardware_rate_limiter <rate-limit-class> <class-descr> <module>
 <rate-limit-configured> [ <rate-limit-allowed> ] [ <rate-limit-dropped> ] [ <rate-limit-total> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rate-limiter | Show Rate-Limiter configs and statistics |
| layer-3 | (Optional) Layer-3 control and Routed packets |
| l3-opts | (Optional) |
| multicast | (Optional) Multicast data packets |
| mcast-opts | (Optional) |
| layer-2 | (Optional) Layer-2 control and Bridged packets |
| l2-opts | (Optional) |
| opts | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1390171738

---

# Command: show hardware rate-limiter span-egress

## Syntax
```
show hardware rate-limiter span-egress [ __readonly__ TABLE_hardware_rate_limiter <rate-limit-class> <class-descr> <module>
 <rate-limit-configured> <rate-limit-allowed> <rate-limit-dropped> <rate-limit-total> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rate-limiter | Show Rate-Limiter configs and statistics |
| span-egress | SPAN/ERSPAN egress packets |
| __readonly__ | (Optional) |
| TABLE_hardware_rate_limiter | (Optional) the xml Rate-Limiter configuration and statistics |
| rate-limit-class | (Optional) the xml rate limiter class |
| class-descr | (Optional) class description |
| module | (Optional) the xml module number |
| rate-limit-configured | (Optional) the xml rate-limit-configured |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, monitoring, S-commands
**Command ID:** wp2340099885

---

# Command: show hardware rl snmp class-id

## Syntax
```
show hardware rl snmp class-id <class-id> [ __readonly__ TABLE-classRateLimiterTable <class-id-out> <class-descr> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rl | Show Rate-Limiter configs and statistics |
| snmp | Show Rate-Limiter snmp information |
| class-id | rate-limiter class-id |
| class-id | rate-limiter class |
| __readonly__ | (Optional) |
| TABLE-classRateLimiterTable | (Optional) Class Rate Limiter Table |
| class-id-out | (Optional) class if out |
| class-descr | (Optional) class description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, management, S-commands
**Command ID:** wp5996346640

---

# Command: show hardware rl snmp global class-id

## Syntax
```
show hardware rl snmp global class-id <class-id> [ __readonly__ TABLE-globalRateLimiterTable <class-id-out> <rate-limit-configured>
 <rate-limit-allowed> <rate-limit-dropped> <rate-limit-total> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rl | Show Rate-Limiter configs and statistics |
| snmp | Show Rate-Limiter snmp information |
| global | Show Global information |
| class-id | rate-limiter class-id |
| class-id | rate-limiter class |
| __readonly__ | (Optional) |
| TABLE-globalRateLimiterTable | (Optional) Global Rate Limiter Table |
| class-id-out | (Optional) class if out |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, management, S-commands
**Command ID:** wp2102098105

---

# Command: show hardware rl snmp local snmp-index class-id

## Syntax
```
show hardware rl snmp local snmp-index <snmp-index> class-id <class-id> [ __readonly__ TABLE-localRateLimiterTable <snmp-index-out>
 <class-id-out> <rate-limit-configured> <rate-limit-configured-source> <rate-limit-allowed> <rate-limit-dropped> <rate-limit-total>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hardware | Show hardware information |
| rl | Show Rate-Limiter configs and statistics |
| snmp | Show Rate-Limiter snmp information |
| local | Show Local information |
| snmp-index | snmp physical index |
| snmp-index | physical index |
| class-id | rate-limiter class-id |
| class-id | rate-limiter class |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, qos, management, S-commands
**Command ID:** wp3633418166

---

# Command: show hostname

## Syntax
```
show { hostname &#124; switchname } [ __readonly__ { <hostname> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hostname | show the system's hostname |
| switchname | show the system's hostname |
| __readonly__ | (Optional) Read Only |
| hostname | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2269622221

---

# Command: show hosts

## Syntax
```
show hosts [ __readonly__ [ <dnslookup> ] [ <dnsnameservice> ] [ { TABLE_vrf <vrfname> [ <defaultdomains> ] [ <additionaldomainserver>
 ] [ <domainservers> ] [ <nameservice> ] [ <dhcpdomains> ] [ <dhcpdomainservers> ] } ] [ { TABLE_dnsconfigvrf <dnsvrfname>
 [ <usevrf> ] [ <token> ] [ { TABLE_dnsconfigvrfconfig <config> } ] } ] [ { TABLE_hosts <host> [ <address> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hosts | Show information about DNS |
| __readonly__ | (Optional) |
| dnslookup | (Optional) dns lookup enable status |
| dnsnameservice | (Optional) name service |
| TABLE_vrf | (Optional) vrf domain servers |
| vrfname | (Optional) vrf name |
| defaultdomains | (Optional) default domain |
| additionaldomainserver | (Optional) additionaldomain |
| domainservers | (Optional) domain server |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2081340400

---

# Command: show hsrp

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| interface | (Optional) Groups on this interface |
| interface-id | (Optional) Interface |
| active | (Optional) Groups in active state |
| init | (Optional) Groups in init state |
| listen | (Optional) Groups in listen state |
| standby | (Optional) Groups in standby state |
| learn | (Optional) Groups in learn state |
| speak | (Optional) Groups in speak state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3982732726

---

# Command: show hsrp anycast

## Syntax
```
show hsrp anycast [ <id> { ipv4 &#124; ipv6 &#124; both } ] [ brief ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| anycast | Anycast related commands |
| id | (Optional) Bundle number |
| ipv4 | (Optional) Associate IP Version 4 for the bundle |
| ipv6 | (Optional) Associate IP Version 6 for the bundle |
| both | (Optional) Associate IP Version 4 and 6 for the bundle |
| brief | (Optional) Brief output |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3795603975

---

# Command: show hsrp anycast interface vlan

## Syntax
```
show hsrp anycast interface { vlan &#124; bdi } <id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| anycast | Anycast related commands |
| interface | Bundle on this interface Interface |
| vlan | VLAN interface |
| bdi | Bridge-Domain interface |
| id | VLAN number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3078582886

---

# Command: show hsrp anycast remote-db

## Syntax
```
show hsrp anycast remote-db [ <id> { ipv4 &#124; ipv6 &#124; both } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| anycast | Anycast related commands |
| remote-db | Remote data base for the bundle |
| id | (Optional) Bundle number |
| ipv4 | (Optional) Associate IP Version 4 for the bundle |
| ipv6 | (Optional) Associate IP Version 6 for the bundle |
| both | (Optional) Associate IP Version 4 and 6 for the bundle |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp1384924006

---

# Command: show hsrp anycast summary

## Syntax
```
show hsrp anycast summary
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| anycast | Anycast related commands |
| summary | Show HSRP summary |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2258053890

---

# Command: show hsrp bfd-sessions

## Syntax
```
show hsrp bfd-sessions [ interface <interface-id> [ to <ipaddress> ] ] [ __readonly__ [ TABLE_bfd_sess [ <interface> ] [ <list_size>
 ] { [ <src_addr> ] } { [ <dst_addr> ] } [ <ref_count> ] { [ TABLE_ref_groups [ <ref_group_id> ] ] } { [ TABLE_hist_groups
 [ <hist_group_id> ] [ <hist_operation> ] [ <hist_rel_time> ] [ <hist_abs_time> ] [ <hist_ref_count> ] [ <hist_group_state>
 ] [ <hist_status> ] [ <hist_op_reason> ] ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| bfd-sessions | BFD sessions |
| interface | (Optional) Groups on this interface |
| interface-id | (Optional) Interface |
| to | (Optional) To IP address |
| ipaddress | (Optional) Sessions to IP address |
| __readonly__ | (Optional) |
| TABLE_bfd_sess | (Optional) |
| interface | (Optional) Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp7740236620

---

# Command: show hsrp delay

## Syntax
```
show hsrp delay [ interface <interface-id> ] [ __readonly__ TABLE_delay <interface> <min_delay> <reload_delay> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| delay | Group initialisation delay |
| interface | (Optional) Groups on this interface |
| interface-id | (Optional) Interface |
| __readonly__ | (Optional) |
| TABLE_delay | (Optional) |
| interface | (Optional) Interface |
| min_delay | (Optional) Min delay |
| reload_delay | (Optional) Reload delay |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp8836529640

---

# Command: show hsrp mgo

## Syntax
```
show hsrp mgo [ name <name> &#124; brief ] [ __readonly__ TABLE_hsrp_mgo <master_name> <master_interface> <master_address_family>
 <master_group_id> [ <master_version> ] <master_state> [ <master_down_reason> ] [ { TABLE_slave <slave_interface> <slave_group_id>
 <slave_state> [ <slave_down_reason> ] } ] [ <num_slave_group> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| mgo | Show HSRP mgo details |
| name | (Optional) Redundancy name string |
| name | (Optional) name string |
| brief | (Optional) show HSPR mgo brief |
| __readonly__ | (Optional) |
| TABLE_hsrp_mgo | (Optional) |
| master_name | (Optional) HSRP master name |
| master_interface | (Optional) HSRP master interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3665630952

---

# Command: show hsrp summary

## Syntax
```
show hsrp summary [ __readonly__ <switchover_notify_rxed> <bfd_enabled> <num_of_groups> <num_of_v4_v1_groups> <num_of_v4_v2_groups>
 <num_of_v6_v2_groups> <num_of_active_groups> <num_of_standby_groups> <num_of_listen_groups> <num_of_v6_active_groups> <num_of_v6_standby_groups>
 <num_of_v6_listen_groups> <num_of_hsrp_enabled_ifs> <counter_pkts_tx> <counter_pkts_tx_failure> <counter_pkts_in> <counter_pkts_bad_vr>
 <counter_mts_rx> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| hsrp | Hot Standby Router Protocol (HSRP) information |
| summary | Show HSRP summary |
| __readonly__ | (Optional) |
| switchover_notify_rxed | (Optional) Switchover notification received (1 => active) |
| bfd_enabled | (Optional) BFD status |
| num_of_groups | (Optional) Total number of groups |
| num_of_v4_v1_groups | (Optional) Number of IPv4 V1 groups |
| num_of_v4_v2_groups | (Optional) Number of IPv4 V2 groups |
| num_of_v6_v2_groups | (Optional) Number of IPv6 V2 groups |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2467687161

---

