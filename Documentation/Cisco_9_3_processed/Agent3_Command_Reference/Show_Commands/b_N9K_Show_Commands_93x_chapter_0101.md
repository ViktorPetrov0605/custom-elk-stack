# Chapter: E Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_0101.html
**Type:** Show Commands  
**Chapter:** Group-101 Commands  
**Total Commands:** 17

## Command List

- `show ecp`
- `show elam report`
- `show email`
- `show encryption service stat`
- `show environment`
- `show errdisable detect`
- `show errdisable flap`
- `show evb`
- `show evb hosts`
- `show evb vsi`
- `show event manager environment`
- `show event manager event-types`
- `show event manager events action-log`
- `show event manager history events`
- `show event manager policy-state`
- `show event manager script system`
- `show event manager system-policy`

---

## Detailed Command Reference

# Command: show ecp

## Syntax
```
show ecp [ detail ] [ __readonly__ <ecp_rte> <ecp_retries> [ <ecp_mode> ] <ecp_cnt_rx_pkt> <ecp_cnt_tx_pkt> [ { TABLE_ecp_plugin
 <plugin_id> <plugin_desc> <plugin_status> } ] [ { TABLE_ecp_session <session_id> <session_interface> <session_svlan> [ <session_peer_mac>
 ] <session_rx_seq> <session_tx_seq> [ <session_cnt_rx_pkt> ] [ <session_cnt_rx_dup> ] [ <session_cnt_rx_drop> ] [ <session_cnt_tx_pkt>
 ] [ <session_cnt_tx_retry> ] [ <session_cnt_tx_err> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ecp | ECP (Edge Control Protocol) |
| detail | (Optional) Detailed information |
| __readonly__ | (Optional) |
| ecp_rte | (Optional) Retransmission timer init exponent |
| ecp_retries | (Optional) Maximal number of retransmissions |
| ecp_mode | (Optional) ECP mode |
| ecp_cnt_rx_pkt | (Optional) No. received packet |
| ecp_cnt_tx_pkt | (Optional) No. trasmitted packet |
| TABLE_ecp_plugin | (Optional) ECP plugin table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3039871536

---

# Command: show elam report

## Syntax
```
show elam report [ l2 &#124; l3 &#124; l4 &#124; aclqos &#124; mcast &#124; mpls ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| elam | elam |
| report | Show ELAM report |
| l2 | (Optional) Layer 2 header report |
| l3 | (Optional) Layer 3 header report |
| l4 | (Optional) Layer 4 header report |
| aclqos | (Optional) Aclqos report |
| mcast | (Optional) Multicast report |
| mpls | (Optional) MPLS report |

**Command Mode:** /exec/elamtah/outsel2

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2069626831

---

# Command: show email

## Syntax
```
show email [ __readonly__ [ <ipv4> ] [ <ipv6> ] [ <host> ] [ <port> ] [ <reply> ] [ <from> ] [ <vrfname> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| email | Pipe email configuration |
| __readonly__ | (Optional) |
| ipv4 | (Optional) |
| host | (Optional) |
| port | (Optional) |
| reply | (Optional) |
| from | (Optional) |
| vrfname | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2473147062

---

# Command: show encryption service stat

## Syntax
```
show encryption service stat [ __readonly__ [ <encryptionService> <MasterKeyEncryption> <Type6Encryption> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| encryption | Encryption service |
| service | Encryption service |
| stat | Encrytpin service status |
| __readonly__ | (Optional) |
| encryptionService | (Optional) Encryption service status |
| MasterKeyEncryption | (Optional) Master key status |
| Type6Encryption | (Optional) Is type 6 encryption used? |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1752154747

---

# Command: show environment

## Syntax
```
show environment [ fan [ detail1 ] &#124; power [ detail ] [ ampere ] [ input ] &#124; temperature [ module <module> &#124; <s0> <santa-cruz-range>
 &#124; psu ] ] [ __readonly__ [ { TABLE_clockinfo <clockname> <clkmodel> <clkhwver> <clkstatus> <act_standby> } ] [ { fandetails
 [ { TABLE_faninfo <fanname> <fanmodel> <fanhwver> <fandir> <fanstatus> } ] { TABLE_fan_zone_speed <zone> <zonespeed> } <fan_filter_status>
 [ { TABLE_fantray <fanname> <trayfannum> <fandir> <fanperc> <fanrpm> } ] [ { TABLE_psufan <fanname> <fan1rpm> <fan2rpm> }
 ] } ] [ { powersup [ <voltage_level> ] [ { TABLE_psinfo <psnum> <psmodel> [ <actual_out> ] [ <actual_input> ] [ <tot_capa>
 ] [ <input_type> ] [ <watts> ] [ <amps> ] [ <ps_status> ] [ <ps_status_3k> ] } ] [ { TABLE_mod_pow_info <modnum> <mod_model>
 [ <actual_draw> ] [ <allocated> ] [ <watts_requested> ] [ <amps_requested> ] [ <watts_alloced> ] [ <amps_alloced> ] [ <modstatus>
 ] [ <modstatus_3k> ] } ] [ { power_summary [ <ps_redun_mode> ] [ <ps_redun_mode_3k> ] [ <ps_oper_mode> ] [ <ps_redun_op_mode>
 ] <tot_pow_capacity> [ <tot_gridA_capacity> ] [ <tot_gridB_capacity> ] [ <cumulative_power> ] [ <tot_pow_out_actual_draw>
 ] [ <tot_pow_input_actual_draw> ] [ <tot_pow_alloc_budgeted> ] [ <reserve_sup> ] [ <pow_used_by_mods> ] <available_pow> }
 ] [ { powersup_detail <reserve_sup> <reserve_xbar> <reserve_fan> <reserve_supxbarfan> <pow_used_by_mods> } ] [ <all_inlets_connected>
 ] [ { TABLE_ps_detail_info <det_name> <det_total_cap> <det_volt> <det_pintot> [ <det_pina> ] <det_vin> <det_iin> <det_pout>
 <det_vout> <det_iout> [ <det_pinb> ] [ <det_iinb> ] [ <det_vinb> ] [ <det_cord> ] <det_sw_alarm> [ { TABLE_det_hw_alarm_regval
 <regnum> <regval> } ] [ { TABLE_det_hw_alarm_str <regnumstr> <bitnumstr> <alarm_str> } ] } ] [ { TABLE_psinputinfo_n3k <ps_slot>
 <ps_input_voltage> <ps_input_current> <ps_in_power> [ <ps_output_voltage> ] [ <ps_output_current> ] <ps_state> } ] } ] [ {
 fandetails_3k [ { TABLE_faninfo <fanname> <fanmodel> <fanhwver> <fandir> <fanstatus> } ] { TABLE_fan_zone_speed <zone> <speed>
 } <fan_filter_status> [ { TABLE_fantray <fanname> <fannum> <fandir> <fanperc> <fanrpm> } ] [ { TABLE_psufan <fanname> <fan1rpm>
 <fan2rpm> } ] } ] [ { TABLE_tempinfo <tempmod> <sensor> <majthres> <minthres> <curtemp> <alarmstatus> [ <temptype> ] } ] [
 { TABLE_psutempinfo <psumod> <inlet_temp> <outlet_temp> <heatsink_temp> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| environment | system environment information |
| fan | (Optional) Fan information |
| power | (Optional) Power capacity and power distribution information |
| detail | (Optional) Detail Fan-tray information when used with Fan. Detail Power capacity and power distribution information when used
 with Power |
| detail1 | (Optional) Detail Fan-tray information when used with Fan |
| ampere | (Optional) Ampere Power capacity and power distribution information |
| input | (Optional) Power supply power input |
| temperature | (Optional) temperature sensor information |
| module | (Optional) enter a module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2367567463

---

# Command: show errdisable detect

## Syntax
```
show errdisable { detect &#124; recovery } [ __readonly__ TABLE_errdisable <cause> <state> [ <time_interval> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| errdisable | Error disable |
| detect | Show errdisable detect |
| recovery | Show errdisable recovery |
| __readonly__ | (Optional) Read Only |
| TABLE_errdisable | (Optional) show errdisable |
| cause | (Optional) errdisable cause |
| state | (Optional) Interface state |
| time_interval | (Optional) err revovery time interval |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp7564055980

---

# Command: show errdisable flap

## Syntax
```
show errdisable flap
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| errdisable | Error disable |
| flap | linkstate flapping |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2795534682

---

# Command: show evb

## Syntax
```
show evb [ __readonly__ <evb_role> <evb_vdp_mac> [ <evb_cisco_mac> ] [ <evb_user_mac> ] <evb_rwd> <evb_rka> <evb_cnt_recv_vdpdu>
 <evb_cnt_drop_vdpdu> <evb_cnt_recv_tlv> <evb_cnt_recv_mgr_tlv> <evb_cnt_recv_assoc_tlv> <evb_cnt_recv_cmd> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| evb | EVB (Edge Virtual Bridge) |
| __readonly__ | (Optional) |
| evb_role | (Optional) EVB role |
| evb_vdp_mac | (Optional) VDP Mac address |
| evb_cisco_mac | (Optional) Cisco Mac address |
| evb_user_mac | (Optional) User mac address |
| evb_rwd | (Optional) Resource wait init exponent |
| evb_rka | (Optional) Keep-alive init exponent |
| evb_cnt_recv_vdpdu | (Optional) No. received vdpdu |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2604303060

---

# Command: show evb hosts

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| evb | EVB (Edge Virtual Bridge) |
| hosts | Host information |
| summary | (Optional) Display summary information |
| detail | (Optional) Display detailed information |
| internal-info | (Optional) Display detailed and internal information |
| mac | (Optional) Display hosts by MAC address |
| mac-addr | (Optional) MAC Address |
| interface | (Optional) Display hosts by interface |
| intf-name | (Optional) Interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2399213531

---

# Command: show evb vsi

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| evb | EVB (Edge Virtual Bridge) |
| vsi | Virtual Station Interface (VSI) information |
| summary | (Optional) Display summary information |
| detail | (Optional) Display detailed information |
| internal-info | (Optional) Display detailed and internal information |
| mac | (Optional) Display VSI by MAC address |
| mac-addr | (Optional) MAC Address |
| interface | (Optional) Display VSI by interface |
| intf-name | (Optional) Interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1405697648

---

# Command: show event manager environment

## Syntax
```
show event manager environment { all &#124; <varname> } [ __readonly__ <environment-details> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| environment | Show information about environment variables |
| all | Show information about all the configured environment variables |
| varname | The environment variable name on which information is required |
| __readonly__ | (Optional) |
| environment-details | (Optional) Show information about environment variables |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1382595931

---

# Command: show event manager event-types

## Syntax
```
show event manager event-types [ all &#124; <event-type-name> ] [ module <module-id> ] [ __readonly__ { <event-types> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| event-types | Show information about registered event types |
| all | (Optional) Show information about advanced event types as well |
| event-type-name | (Optional) Show information about the specified event type |
| module | (Optional) Show information about event types on other modules |
| module-id | (Optional) Module Id |
| __readonly__ | (Optional) |
| event-types | (Optional) Show information about registered event types |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2365720768

---

# Command: show event manager events action-log

## Syntax
```
show event manager events action-log [ policy <policy-name> &#124; event-type <event-type-name> ] [ __readonly__ { <action-log-data>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| events | Show information about the history of past events |
| action-log | Show policy action logs |
| policy | (Optional) Name of policy |
| policy-name | (Optional) Enter policy name |
| event-type | (Optional) Name of event |
| event-type-name | (Optional) Enter event type |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2253199783

---

# Command: show event manager history events

## Syntax
```
show event manager history events [ detail ] [ maximum <n-events> ] [ severity <sev> ] [ __readonly__ { <history-events> }
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| history | Show information about the history of past activity |
| events | Show information about the history of past events |
| detail | (Optional) Show information about the event parameters as well |
| maximum | (Optional) Specify an upper limit on the number of events to be shown |
| n-events | (Optional) Specify the maximum number of events to be shown |
| severity | (Optional) Show only those events whose severity is >= specified severity |
| sev | (Optional) Enter the severity threshold |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3023623619

---

# Command: show event manager policy-state

## Syntax
```
show event manager policy-state <name> [ module <module-id> ] [ __readonly__ { <policy-state> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| policy-state | Show information about the state of a policy |
| name | Name of the policy |
| module | (Optional) Get the information from a module |
| module-id | (Optional) Module Id |
| __readonly__ | (Optional) |
| policy-state | (Optional) Show information about the state of a policy |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3818399527

---

# Command: show event manager script system

## Syntax
```
show event manager script system { all &#124; <script-name> } [ __readonly__ <script_system_details> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| script | Show information about a script policy |
| system | Show information about a system script policy |
| all | Show all the available system script policies |
| script-name | Name of the system script policy |
| __readonly__ | (Optional) |
| script_system_details | (Optional) Show Information about system script policies |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp4221778305

---

# Command: show event manager system-policy

## Syntax
```
show event manager system-policy [ all &#124; <policy-name> ] [ __readonly__ { [ TABLE_eem [ <thresh_min> ] [ <thresh_max> ] <event_name>
 <event_description> <event_overridable> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| event | Event Manager commands |
| manager | Event Manager commands |
| system-policy | Show information about default system policies |
| all | (Optional) Show all policies (including advanced and non-overridable ones) |
| policy-name | (Optional) Show detailed information about the specified policy |
| __readonly__ | (Optional) |
| TABLE_eem | (Optional) |
| thresh_min | (Optional) |
| thresh_max | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1964847827

---

