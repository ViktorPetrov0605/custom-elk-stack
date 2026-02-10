# Chapter: C Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_011.html
**Type:** Show Commands  
**Chapter:** Group-11 Commands  
**Total Commands:** 133

## Command List

- `show callhome`
- `show callhome destination-profile`
- `show callhome destination-profile profile`
- `show callhome destination-profile profile CiscoTAC-1`
- `show callhome destination-profile profile full-txt-destination`
- `show callhome destination-profile profile short-txt-destination`
- `show callhome transport-email`
- `show callhome transport`
- `show callhome user-def-cmds`
- `show catena`
- `show catena analytics`
- `show cdp`
- `show cdp all`
- `show cdp global`
- `show cdp neighbors`
- `show cdp neighbors detail`
- `show cdp traffic interface2`
- `show cdp traffic interface2 all`
- `show cfs application`
- `show cfs lock`
- `show cfs merge status`
- `show cfs peers`
- `show cfs regions`
- `show cfs status`
- `show checkpoint`
- `show checkpoint`
- `show checkpoint summary`
- `show class-map`
- `show class-map type control-plane`
- `show class-map type network-qos`
- `show cli alias`
- `show cli dynamic-cmd`
- `show cli dynamic integers`
- `show cli dynamic strings`
- `show cli history`
- `show cli interface table`
- `show cli list`
- `show cli syntax`
- `show cli variables`
- `show clock`
- `show config-profile`
- `show config-profile applied`
- `show config-replace log exec`
- `show config-replace status`
- `show config-template`
- `show configuration session`
- `show configuration session`
- `show configuration session global-info`
- `show configuration session status`
- `show configuration session summary`
- `show consistency-checker copp`
- `show consistency-checker egress-xlate private-vlan`
- `show consistency-checker fex-interfaces fex`
- `show consistency-checker forwarding ipv6`
- `show consistency-checker forwarding show forwarding inconsistency`
- `show consistency-checker forwarding single-route ipv4 vrf`
- `show consistency-checker gwmacdb`
- `show consistency-checker hardware-telemetry inband brief`
- `show consistency-checker hardware-telemetry postcard brief`
- `show consistency-checker kim`
- `show consistency-checker kim interface`
- `show consistency-checker l2-tahoe mac-address`
- `show consistency-checker l2-tahoe module`
- `show consistency-checker l2-tahoe switchport interface`
- `show consistency-checker l2 multicast group source vlan`
- `show consistency-checker l3-interface module`
- `show consistency-checker l3 multicast source vrf`
- `show consistency-checker link-state fabric-ieth`
- `show consistency-checker link-state module`
- `show consistency-checker membership port-channels`
- `show consistency-checker membership vlan`
- `show consistency-checker pacl extended ingress ipv6 interface`
- `show consistency-checker pacl extended ingress ip module`
- `show consistency-checker pacl extended ingress ipv6 module`
- `show consistency-checker pacl extended ingress ip interface`
- `show consistency-checker pacl extended ingress mac module`
- `show consistency-checker pacl extended ingress mac interface`
- `show consistency-checker pacl module`
- `show consistency-checker pacl port-channels`
- `show consistency-checker port-state`
- `show consistency-checker port-state fabric-ieth`
- `show consistency-checker racl extended egress ipv6 interface`
- `show consistency-checker racl extended egress ip interface`
- `show consistency-checker racl extended ingress ipv6 module`
- `show consistency-checker racl extended ingress ip module`
- `show consistency-checker racl extended ingress ip interface`
- `show consistency-checker racl extended ingress ipv6 interface`
- `show consistency-checker racl module`
- `show consistency-checker racl port-channels`
- `show consistency-checker racl svi interface`
- `show consistency-checker segment-routing mpls ip mask vrf`
- `show consistency-checker selective-qinq`
- `show consistency-checker selective-qinq interface`
- `show consistency-checker stp-state vlan`
- `show consistency-checker vacl`
- `show consistency-checker vacl extended ingress ipv6 vlan`
- `show consistency-checker vacl extended ingress ip vlan`
- `show consistency-checker vacl extended ingress mac vlan`
- `show consistency-checker vpc`
- `show consistency-checker vxlan config-check`
- `show consistency-checker vxlan flood_list`
- `show consistency-checker vxlan infra`
- `show consistency-checker vxlan l2 module`
- `show consistency-checker vxlan l3 vrf start`
- `show consistency-checker vxlan mh mac-addresses`
- `show consistency-checker vxlan mh pathlist`
- `show consistency-checker vxlan pv`
- `show consistency-checker vxlan qinq-qinvni`
- `show consistency-checker vxlan selective-qinvni`
- `show consistency-checker vxlan selective-qinvni interface`
- `show consistency-checker vxlan vlan`
- `show consistency-checker vxlan xconnect`
- `show`
- `show controller accounting log`
- `show copp diff profile profile2`
- `show copp profile`
- `show copp status`
- `show copyright`
- `show cores`
- `show crypto ca certificates`
- `show crypto ca certificates`
- `show crypto ca certstore`
- `show crypto ca crl`
- `show crypto ca remote-certstore`
- `show crypto ca trustpoints`
- `show crypto ca trustpool`
- `show crypto ca trustpool last download status`
- `show crypto ca trustpool policy`
- `show crypto certificatemap`
- `show crypto key mypubkey rsa`
- `show crypto ssh-auth-map`
- `show cts`
- `show current`

---

## Detailed Command Reference

# Command: show callhome

## Syntax
```
show callhome [ __readonly__ <output_state> <info> <per_name> [ <name> ] <email_info> [ <email_conf> ] <ph_info> [ <ph_conf>
 ] <str_addr> [ <str_conf> ] <site_id> [ <site_id_conf> ] <cust_id> [ <cus_id_conf> ] <contr_id> [ <contr_id_conf> ] <swi_pri>
 [ <swi_pri_value> ] <dup_mess> <per_inv> <per_time> <per_timeofday> <dist> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| __readonly__ | (Optional) |
| output_state | (Optional) |
| info | (Optional) |
| per_name | (Optional) |
| name | (Optional) |
| email_info | (Optional) |
| email_conf | (Optional) |
| ph_info | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1415480673

---

# Command: show callhome destination-profile

## Syntax
```
show callhome destination-profile [ __readonly__ { TABLE_call_info [ <dest_full_info> ] [ <dest_short_info> ] [ <dest_xml_info>
 ] [ <dest_def_info> ] <max_mess_size> <mess_format> <mess_level> <trans_method> <email_info> [ <index> <email_conf> ] <url_info>
 [ <index> <url_conf> ] <alert_groups> [ <alert_conf> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| destination-profile | Show callhome destination profile information |
| __readonly__ | (Optional) |
| TABLE_call_info | (Optional) |
| dest_full_info | (Optional) |
| dest_short_info | (Optional) |
| dest_xml_info | (Optional) |
| dest_def_info | (Optional) |
| max_mess_size | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1662622233

---

# Command: show callhome destination-profile profile

## Syntax
```
show callhome destination-profile profile <s0> [ __readonly__ <user_txt_info> <max_mess_size> <mess_format> <mess_level> <trans_method>
 <email_info> [ TABLE_email [ <index> <email_conf> ] ] <url_info> [ TABLE_url [ <index> <url_conf> ] ] <alert_groups> [ TABLE_alert
 [ <alert_conf> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| destination-profile | Show callhome destination profile information |
| profile | Specify the destination profile |
| s0 | Show information for user defined destination profile |
| __readonly__ | (Optional) |
| user_txt_info | (Optional) |
| max_mess_size | (Optional) |
| mess_format | (Optional) |
| mess_level | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2071635654

---

# Command: show callhome destination-profile profile CiscoTAC-1

## Syntax
```
show callhome destination-profile profile CiscoTAC-1 [ __readonly__ <tac_xml_info> <max_mess_size> <mess_level> <trans_method>
 <email_info> [ <index> <email_conf> ] <url_info> [ <index> <url_conf> ] <alert_groups> [ <alert_conf> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| destination-profile | Show callhome destination profile information |
| profile | Specify the destination profile |
| CiscoTAC-1 | Show information for CiscoTAC-1 destination profile |
| __readonly__ | (Optional) |
| tac_xml_info | (Optional) |
| max_mess_size | (Optional) |
| mess_level | (Optional) |
| trans_method | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp8206863100

---

# Command: show callhome destination-profile profile full-txt-destination

## Syntax
```
show callhome destination-profile profile full-txt-destination [ __readonly__ <full_txt_info> <max_mess_size> <mess_level>
 <trans_method> <email_info> [ <index> <email_conf> ] <url_info> [ <index> <url_conf> ] <alert_groups> [ <alert_conf> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| destination-profile | Show callhome destination profile information |
| profile | Specify the destination profile |
| full-txt-destination | Show information for full-txt-destination destination profile |
| __readonly__ | (Optional) |
| full_txt_info | (Optional) |
| max_mess_size | (Optional) |
| mess_level | (Optional) |
| trans_method | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4104946326

---

# Command: show callhome destination-profile profile short-txt-destination

## Syntax
```
show callhome destination-profile profile short-txt-destination [ __readonly__ <shrt_txt_info> <max_mess_size> <mess_level>
 <trans_method> <email_info> [ <index> <email_conf> ] <url_info> [ <index> <url_conf> ] <alert_groups> [ <alert_conf> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| destination-profile | Show callhome destination profile information |
| profile | Specify the destination profile |
| short-txt-destination | Show information for short-txt-destination destination profile |
| __readonly__ | (Optional) |
| shrt_txt_info | (Optional) |
| max_mess_size | (Optional) |
| mess_level | (Optional) |
| trans_method | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp7976240300

---

# Command: show callhome transport-email

## Syntax
```
show callhome transport-email [ __readonly__ { <from_email> } [ <reply_to_email> ] [ <return_receipt_addr> ] { <smtp_server>
 } [ <smtp_server_port> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| __readonly__ | (Optional) |
| show | Show running system information |
| callhome | Show callhome information |
| transport-email | Show callhome email transport configuration |
| from_email | (Optional) |
| reply_to_email | (Optional) |
| return_receipt_addr | (Optional) |
| smtp_server | (Optional) |
| smtp_server_port | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1455498390

---

# Command: show callhome transport

## Syntax
```
show callhome transport [ __readonly__ <vrf> <from_email> [ <rep_email> ] [ <ret_email> ] [ <smtp_ser> ] [ <smtp_ser_port>
 ] [ <smtp_ser_vrf> ] [ <smtp_ser_prior> ] [ <smtp_ser_do> ] [ <smtp_ser_port_do> ] [ <smtp_ser_vrf_do> ] [ <smtp_ser_prior_do>
 ] [ <smtp_ser_got> ] [ <smtp_ser_port_got> ] [ <smtp_ser_vrf_got> ] [ <smtp_ser_prior_got> ] <http_prox> <http_port> <http_state>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| transport | Show callhome transport configuration (email and http) |
| __readonly__ | (Optional) |
| vrf | (Optional) |
| from_email | (Optional) |
| rep_email | (Optional) |
| ret_email | (Optional) |
| smtp_ser | (Optional) |
| smtp_ser_port | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2018851383

---

# Command: show callhome user-def-cmds

## Syntax
```
show callhome user-def-cmds [ __readonly__ { <user_configured_cmds> } [ { TABLE_user_def_cmds <alert_group> <index> <user_defined_cmds>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| callhome | Show callhome information |
| user-def-cmds | Show the cli commands configured for each alert group |
| __readonly__ | (Optional) |
| user_configured_cmds | (Optional) List of user configured commands |
| TABLE_user_def_cmds | (Optional) |
| index | (Optional) |
| alert_group | (Optional) |
| user_defined_cmds | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp8954148040

---

# Command: show catena

## Syntax
```
show catena <instance-name> [ brief ] [ __readonly__ <instance_name> <state> { TABLE_chain <chain> [ TABLE_rule <seqno> <aclname>
 <whichconfig> [ <vlan_group> ] [ <ingress_port> ] [ <egress_port> ] [ <egress_device> ] [ <mode> ] [ <l2_lb> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| catena | catena |
| instance-name | instance name |
| brief | (Optional) brief |
| __readonly__ | (Optional) Read Only |
| instance_name | (Optional) instance_name |
| state | (Optional) status |
| TABLE_chain | (Optional) |
| chain | (Optional) chain |
| TABLE_rule | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2112076763

---

# Command: show catena analytics

## Syntax
```
show catena analytics { per-acl { per-node &#124; per-device-group &#124; per-vlan-group &#124; per-port-group &#124; total } &#124; per-catena-instance
 <instance-name> [ per-chain [ <chain-id> ] ] } [ __readonly__ <instance_name> <per_node> <per_node_total> <per_node_total_val>
 <per_intf_total_val> <per_vlan_total_val> <chain_id> <per_device_group> <per_device_group_hdr> <per_device_group_val> <per_vlan_group>
 <per_vlan_group_hdr> <per_vlan_group_val> <per_port_group> <per_port_group_val> <per_port_group_hdr> <total_val> <stats_counter>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| catena | catena |
| analytics | show analytics for catena |
| per-acl | per ACL |
| per-node | per Node |
| per-device-group | per Device group |
| per-vlan-group | per Vlan Group |
| per-port-group | per EgressPort Group |
| total | per ACL Total |
| per-catena-instance | per Catena Instance |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1457335597

---

# Command: show cdp

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| entry | Show CDP entries in database |
| all1 | Show all CDP entries in database |
| name | Show a specific CDP entry matching a name |
| __readonly__ | (Optional) Read only |
| TABLE_cdp_entry_all | (Optional) output of show cdp entry all |
| device_id | (Optional) Device Identifier |
| sysname | (Optional) System Name |
| v4addr | (Optional) Interface IP V4 Address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2659214916

---

# Command: show cdp all

## Syntax
```
show cdp { all &#124; interface <if0> } [ __readonly__ TABLE_cdp_all <intf_id> <port_up> [ <cdp_global_enabled> ] <cdp_intf_enabled>
 [ <oper_mode> ] <refresh_time> <ttl> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| all | Show all interfaces in CDP database |
| interface | Show CDP parameters for an interface |
| __readonly__ | (Optional) Read only |
| TABLE_cdp_all | (Optional) output of show cdp all |
| intf_id | (Optional) Interface Id |
| port_up | (Optional) Port status |
| cdp_global_enabled | (Optional) CDP global status |
| cdp_intf_enabled | (Optional) CDP interface status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3018526700

---

# Command: show cdp global

## Syntax
```
show cdp global [ __readonly__ <cdp_global_enabled> <refresh_time> <ttl> <v2_advertisement> <deviceid_format> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| global | Show CDP global parameters |
| __readonly__ | (Optional) Read only |
| cdp_global_enabled | (Optional) CDP global status |
| refresh_time | (Optional) Refresh Time |
| ttl | (Optional) Hold Time |
| v2_advertisement | (Optional) Show v2 advertisement |
| deviceid_format | (Optional) Show deviceId Format |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1291624810

---

# Command: show cdp neighbors

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| neighbors | Show CDP neighbors |
| interface | (Optional) Show CDP neighbors on an interface |
| if | (Optional) Specify Interface |
| __readonly__ | (Optional) Read only |
| TABLE_cdp_neighbor_brief_info | (Optional) output of show cdp neighbor - in breif |
| ifindex | (Optional) Interface index |
| device_id | (Optional) System Name (or) Device Identifier |
| intf_id | (Optional) Interface Id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1923154762

---

# Command: show cdp neighbors detail

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| neighbors | Show CDP neighbors |
| detail | Show CDP neighbors detailed |
| interface | (Optional) Show CDP neighbors on an interface |
| if | (Optional) Specify Interface |
| __readonly__ | (Optional) Read only |
| TABLE_cdp_neighbor_detail_info | (Optional) output of show cdp neighbor detail |
| ifindex | (Optional) Interface index |
| device_id | (Optional) Device Identifier |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3202262804

---

# Command: show cdp traffic interface2

## Syntax
```
show cdp traffic interface2 <if2> [ __readonly__ <intf_id> <total_input_packets> <valid_cdp_packets> <input_v1_packets> <input_v2_packets>
 <invalid_cdp_packets> <unsupported_version> <checksum_errors> <malformed_packets> <total_output_packets> <output_v1_packets>
 <output_v2_packets> <send_errors> <flap_cnt> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| traffic | Show CDP traffic statistics |
| interface2 | Show CDP traffic statistics on an interface |
| __readonly__ | (Optional) Read only |
| intf_id | (Optional) Interface Id |
| total_input_packets | (Optional) Total input cdp packets |
| valid_cdp_packets | (Optional) Total valid cdp packets |
| input_v1_packets | (Optional) Input vesrion1 packets |
| input_v2_packets | (Optional) Input vesrion2 packets |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2156884989

---

# Command: show cdp traffic interface2 all

## Syntax
```
show cdp traffic interface2 all [ __readonly__ TABLE_cdp_traffic <intf_id> <total_input_packets> <valid_cdp_packets> <input_v1_packets>
 <input_v2_packets> <invalid_cdp_packets> <unsupported_version> <checksum_errors> <malformed_packets> <total_output_packets>
 <output_v1_packets> <output_v2_packets> <send_errors> <flap_cnt> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cdp | Show Cisco Discovery Protocol information |
| traffic | Show CDP traffic statistics |
| interface2 | Show CDP traffic statistics on an interface |
| all | Display all interface traffic |
| __readonly__ | (Optional) Read only |
| TABLE_cdp_traffic | (Optional) output of show cdp traffic |
| intf_id | (Optional) Interface Id |
| total_input_packets | (Optional) Total input cdp packets |
| valid_cdp_packets | (Optional) Total valid cdp packets |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp6136370110

---

# Command: show cfs application

## Syntax
```
show cfs application [ { name <cfs-dyn-app-name> &#124; sap <i0> } ] [ __readonly__ [ <enabled> <timeout> <merge_capable> <scope>
 <region> ] [ { TABLE_apps <app_name> <app_enabled> <app_scope> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| application | Show locally registered applications |
| name | (Optional) Show local application information by name |
| cfs-dyn-app-name | (Optional) Registered name of the local application |
| sap | (Optional) Show local application information by sap |
| i0 | (Optional) Registered sap of the local application |
| __readonly__ | (Optional) |
| enabled | (Optional) whether application is CFS enabled |
| timeout | (Optional) timeout |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3134328753

---

# Command: show cfs lock

## Syntax
```
show cfs lock [ { name <cfs-dyn-app-name> &#124; sap <i1> } ] [ __readonly__ [ { TABLE_locks [ <app_name> ] <app_scope> [ <vsan>
 ] [ <domain> ] [ <wwn> ] <ip_addr> <u_name> <u_type> [ <hostname> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| lock | Show state of application's logical/physical locks |
| name | (Optional) Application name for which the lock status is required |
| cfs-dyn-app-name | (Optional) Registered name of the local application |
| sap | (Optional) Application sap for which the lock status is required |
| i1 | (Optional) Application SAP |
| __readonly__ | (Optional) |
| TABLE_locks | (Optional) table of all CFS locks |
| app_name | (Optional) name of CFS application |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2393610354

---

# Command: show cfs merge status

## Syntax
```
show cfs merge status [ { name <cfs-dyn-app-name> [ detail ] &#124; sap <i1> [ detail2 ] } ] [ __readonly__ [ { scope <scope> }
 ] [ { merge_status <status> } ] [ { failure_reason <reason> } ] [ { TABLE_all_merge <app_name> <scope> <vsan> <status> } ]
 [ { TABLE_local_fabric [ <domain> ] <wwn> <ip_addr> <app_scope> [ <master> ] [ <hostname> ] } ] [ { TABLE_remote_fabric [
 <domain> ] <wwn> <ip_addr> <app_scope> [ <master> ] [ <hostname> ] } ] [ { TABLE_remaining_fabric [ <domain> ] <wwn> <ip_addr>
 [ <hostname> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| merge | Show cfs merge information |
| status | Show status of merge |
| name | (Optional) Show merge status by name |
| cfs-dyn-app-name | (Optional) Registered name of the local application |
| detail | (Optional) Show merge status by name in detail |
| sap | (Optional) Show merge status by sap |
| i1 | (Optional) Application sap |
| detail2 | (Optional) Show merge status by sap in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2653508642

---

# Command: show cfs peers

## Syntax
```
show cfs peers [ { name <cfs-dyn-app-name> &#124; sap <i1> } ] [ __readonly__ [ { scope <scope> } ] [ { TABLE_peers <wwn> <ip_addr>
 [ <local> ] [ <hostname> ] [ <domain> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| peers | Show all the peers in the physical fabric |
| name | (Optional) Show peers for given application name |
| cfs-dyn-app-name | (Optional) Registered name of the local application |
| sap | (Optional) Show peers for given application sap |
| i1 | (Optional) Application sap |
| __readonly__ | (Optional) |
| scope | (Optional) scope |
| scope | (Optional) scope |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1732906961

---

# Command: show cfs regions

## Syntax
```
show cfs regions [ { brief [ region <i0> ] &#124; name <cfs-dyn-app-name> &#124; region1 <i1> } ] [ __readonly__ [ { region <id> } ]
 [ { application <name> } ] [ { scope <scope> } ] [ { TABLE_PEERS <wwn> <ip_addr> <local> [ <hostname> ] [ <domain> ] } ] [
 { TABLE_switches [ <wwn> ] [ <ip_addr> ] <region> <app_name> <enabled> [ <scope> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| regions | Show all the applications with peers and region information |
| brief | (Optional) Show all configured regions and applications(no peers) |
| region | (Optional) Show all configured applications(no peers) |
| i0 | (Optional) Region Id |
| name | (Optional) Show peers and region information for a given application |
| cfs-dyn-app-name | (Optional) Registered name of the local application |
| region1 | (Optional) Show all configured applications with peers |
| i1 | (Optional) Region Id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1128077688

---

# Command: show cfs status

## Syntax
```
show cfs status [ __readonly__ <distribution> <dist_over_ip> <ipv4_mcast_addr> <ipv6_mcast_addr> <dist_over_eth> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cfs | CFS Show Command handler |
| status | Show current status of CFS |
| __readonly__ | (Optional) |
| distribution | (Optional) operational status of CFS distribution |
| dist_over_ip | (Optional) operational status of CFS overIP |
| ipv4_mcast_addr | (Optional) ipv4 multicast address |
| ipv6_mcast_addr | (Optional) ipv6 multicast address |
| dist_over_eth | (Optional) operations status of CFSoE |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2702989571

---

# Command: show checkpoint

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| checkpoint | Show configuration rollback checkpoint contents |
| chkpoint_name | Checkpoint name |
| all | (Optional) Show default config |
| __readonly__ | (Optional) Read only |
| TABLE_checkpoint_details | (Optional) Checkpoint details |
| name1 | (Optional) Checkpoint name |
| checkpoint_config | (Optional) Configuration entry from checkpoint |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2728828632

---

# Command: show checkpoint

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| checkpoint | Show configuration rollback checkpoints |
| all | (Optional) Show default config |
| user | (Optional) Show only user configuration rollback checkpoints |
| system | (Optional) Show only system configuration rollback checkpoints |
| __readonly__ | (Optional) Read only |
| TABLE_checkpoint_details | (Optional) checkpoint details |
| name | (Optional) Checkpoint name |
| checkpoint_config | (Optional) Configuration entry from checkpoint |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1215241910

---

# Command: show checkpoint summary

## Syntax
```
show checkpoint summary [ user &#124; system ] [ __readonly__ TABLE_checkpoint_header_info <name> <user_name> <timestamp> <file_path>
 <chkpt_type> <description> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| checkpoint | Show configuration rollback checkpoints |
| summary | Show configuration rollback checkpoints summary |
| user | (Optional) Show only user configuration rollback checkpoints summary |
| system | (Optional) Show only system configuration rollback checkpoints summary |
| __readonly__ | (Optional) Read only |
| TABLE_checkpoint_header_info | (Optional) Checkpoint header info |
| user_name | (Optional) Username |
| name | (Optional) Checkpoint name |
| file_path | (Optional) Checkpoint name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2008555015

---

# Command: show class-map

## Syntax
```
show class-map [ { [ type qos ] [ <cmap-name> &#124; xxx <color-map-enum-name> ] } &#124; { type queuing [ yyy <cmap-enum-name> &#124; zzz
 <default-cmap-enum-name> &#124; <cmap-dce-name> &#124; <cmap-name-hque> ] } ] [ __readonly__ { [ <display-all> ] [ TABLE_cmap [ <cmap-key>
 ] [ <nq-cmap-key> ] [ <nq-cmap-name> ] [ <nq-cos-list> ] [ <nq-qos-group-list> ] [ <protocol> ] [ <id> ] <xqos-or-q> [ <any_or_all>
 ] <cmap-name-out> [ <desc> ] [ <nq-desc> ] [ TABLE_match <match-key> [ <not> ] [ <dscp-list> ] [ <precedence-list> ] [ <cos-list>
 ] [ <qos-group-list> ] [ <discard-class-list> ] [ <vlan-list> ] [ <match-cmap-name> ] [ <match-acl-name> ] [ <note-string>
 ] [ <pkt-len-list> ] [ <rtp-port-list> ] [ <roce-port-list> ] [ <prot> ] [ <input-iface-list> ] [ <exp-list> ] [ <cl-def>
 ] ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xxx | (Optional) xxx |
| yyy | (Optional) yyy |
| zzz | (Optional) zzz |
| show | Show running system information |
| class-map | Show class maps |
| type | (Optional) Type of the class-map |
| qos | (Optional) type qos |
| queuing | (Optional) type queuing |
| cmap-name | (Optional) class map name |
| cmap-enum-name | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1281128836

---

# Command: show class-map type control-plane

## Syntax
```
show class-map type control-plane [ <cmap-name> ] [ __readonly__ [ { TABLE_cmap <cmap-key> <cmap-name-out> <opt_any_or_all>
 [ TABLE_match <match-key> [ access_grp <acc_grp_name> ] [ redirect <opt_match_redirect> ] [ exception <opt_match_excpt> ]
 [ protocol <opt_match_protocol> ] ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| class-map | Show class maps |
| type | Type of the class-map |
| control-plane | This is for copp policy |
| cmap-name | (Optional) Name of the class-map |
| __readonly__ | (Optional) |
| TABLE_cmap | (Optional) all cmap xml sessions |
| cmap-name-out | (Optional) Name of the class-map |
| cmap-key | (Optional) Class-map name: xml key |
| opt_any_or_all | (Optional) Enter match-any or match-all |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3419985532

---

# Command: show class-map type network-qos

## Syntax
```
show class-map type network-qos [ <cmap-name-nq> ] [ __readonly__ { [ <display-all> ] [ TABLE_cmap <cmap-key> <xcmap-name>
 [ <desc> ] [ <cos-list> ] [ <qos-group-list> ] [ <protocol> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| class-map | Show class maps |
| type | Type of the class-map |
| cmap-name-nq | (Optional) Class-map name |
| network-qos | type network-qos |
| __readonly__ | (Optional) |
| display-all | (Optional) Display all network-qos class-maps |
| TABLE_cmap | (Optional) all network-qos cmap xml sessions |
| cmap-key | (Optional) Class-map name: xml key |
| desc | (Optional) Description string |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2958412430

---

# Command: show cli alias

## Syntax
```
show cli alias [ name <s0> ] [ __readonly__ { TABLE_cli_alias <alias> <name> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | Show CLI information |
| alias | Display the alias configuration |
| name | (Optional) Display a specific alias |
| s0 | (Optional) Specify the alias |
| __readonly__ | (Optional) |
| TABLE_cli_alias | (Optional) cli alias table |
| alias | (Optional) alias |
| name | (Optional) name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3518003250

---

# Command: show cli dynamic-cmd

## Syntax
```
show cli dynamic-cmd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | CLI commands |
| dynamic-cmd | Display the list of dynamic commands(cli) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2101780788

---

# Command: show cli dynamic integers

## Syntax
```
show cli dynamic integers [ <name> ] [ __readonly__ TABLE_dynamic_integers <name-o> <min> <max> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | CLI commands |
| dynamic | Display current range of dynamic parameters |
| integers | Display current range of dynamic integer parameters |
| name | (Optional) name of the dynamic parameter |
| __readonly__ | (Optional) |
| TABLE_dynamic_integers | (Optional) |
| name-o | (Optional) |
| min | (Optional) |
| max | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp9355840600

---

# Command: show cli dynamic strings

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | CLI commands |
| dynamic | Display current range of dynamic parameters |
| strings | Display current range of dynamic string parameters |
| name | (Optional) name of the dynamic parameter |
| __readonly__ | (Optional) |
| TABLE_dynamic_strings | (Optional) |
| name-o | (Optional) |
| value | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3487405415

---

# Command: show cli history

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | debug cli |
| history | history of cli commands |
| count | (Optional) number of lines to display (from end) |
| unformatted | (Optional) display just the commands |
| this-mode-only | (Optional) display history from current mode only |
| exec-mode | (Optional) display history of exec commands only |
| config-mode | (Optional) display history of config commands only |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4220701298

---

# Command: show cli interface table

## Syntax
```
show cli interface table
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| cli | cli |
| interface | interface |
| table | table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1685166320

---

# Command: show cli list

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | Show CLI information |
| list | show |
| component | (Optional) component |
| max-per-cmd | (Optional) max |
| has-xml-out | (Optional) show |
| recurse | (Optional) go |
| detail | (Optional) formats |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3054523283

---

# Command: show cli syntax

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | Show CLI information |
| syntax | show |
| long | (Optional) use |
| recurse | (Optional) also |
| has-xml-out | (Optional) show |
| has-no-xml-out | (Optional) show |
| is-data-modeled | (Optional) show |
| roles | (Optional) show |
| network-admin | (Optional) show |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4079826830

---

# Command: show cli variables

## Syntax
```
show cli variables [ __readonly__ <switchname> <timestamp> [ { TABLE_variable <key> <value> } ] [ { TABLE_session_variable
 <key> <value> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cli | Show CLI information |
| variables | Show CLI variables |
| __readonly__ | (Optional) |
| switchname | (Optional) Switch Name |
| timestamp | (Optional) Timestamp |
| TABLE_variable | (Optional) Variable table |
| key | (Optional) key |
| value | (Optional) value |
| TABLE_session_variable | (Optional) Session variable table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1235544141

---

# Command: show clock

## Syntax
```
show clock [ detail ] [ __readonly__ { <simple_time> <time_source> [ <daylight_zone> <daylight_start_week> <daylight_start_weekday>
 <daylight_start_month> <daylight_start_time> <daylight_end_week> <daylight_end_weekday> <daylight_end_month> <daylight_end_time>
 <daylight_utc_min_offset> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| clock | Display current Date |
| detail | (Optional) Display current date and summertime configuration |
| __readonly__ | (Optional) |
| simple_time | (Optional) simple clock format |
| time_source | (Optional) Time source |
| daylight_zone | (Optional) summer-time daylight zone |
| daylight_start_week | (Optional) daylight start week |
| daylight_start_weekday | (Optional) daylight start weekday |
| daylight_start_month | (Optional) daylight start month |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3555282458

---

# Command: show config-profile

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| config-profile | Show config-profiles |
| name | (Optional) config-profile name |
| all_conf_profile_name | (Optional) Enter the name of configuration profile |
| __readonly__ | (Optional) |
| TABLE_conf_profile_all | (Optional) |
| conf_profile_name | (Optional) |
| conf_profile_desc | (Optional) |
| conf_profile_cfg | (Optional) |
| conf_profile_applied | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2835674879

---

# Command: show config-profile applied

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| config-profile | Show config-profiles |
| applied | List of config-profiles that are applied |
| auto | (Optional) List of config-profiles that are applied via auto-config |
| manually | (Optional) List of all config-profiles which were applied directly from cli |
| non-applied | List of config-profiles that are not applied |
| match-name | (Optional) List of all config-profiles that have matching sub-string |
| __readonly__ | (Optional) |
| profiles | (Optional) |
| profile_substring | (Optional) Enter a substring to match with config-profile name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp6787691250

---

# Command: show config-replace log exec

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| config-replace | Show config-replace |
| log | show config-replace log |
| exec | show config-replace execution log |
| verify | show config-replace verify log |
| __readonly__ | (Optional) Read only |
| log_entry | (Optional) log entry from configure replace log |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3404285200

---

# Command: show config-replace status

## Syntax
```
show config-replace status [ __readonly__ <last_operation> [ <config_replace_type> ] [ <name> ] [ <start_time> ] [ <end_time>
 ] [ <operation_status> ] [ <commit_status> ] [ <commit_timeout_remaining> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| config-replace | show config-replace |
| status | show status of last configure replace operation |
| __readonly__ | (Optional) Read only |
| last_operation | (Optional) last operation |
| config_replace_type | (Optional) config-replace type |
| name | (Optional) name |
| start_time | (Optional) start time |
| end_time | (Optional) end time |
| operation_status | (Optional) operation status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1354529912

---

# Command: show config-template

## Syntax
```
show config-template [ [ <template-name> ] [ status [ { vrf <vrf-name> } ] ] ] [ __readonly__ { TABLE_profile <name> <refcount>
 <type> [ TABLE_cfg <cfg> ] [ TABLE_status <vrfname> <status> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| config-template | config-template |
| template-name | (Optional) config-template name |
| status | (Optional) config-template status |
| vrf | (Optional) VRF referencing config-template |
| vrf-name | (Optional) config-template name |
| __readonly__ | (Optional) |
| TABLE_profile | (Optional) |
| name | (Optional) config-template name |
| refcount | (Optional) Ref count of VRFs using this config-template |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp6163300600

---

# Command: show configuration session

## Syntax
```
show configuration session <s3> [ __readonly__ <ssn-name> [ TABLE_session_details [ <ssn-cmd-num> ] [ <command> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| configuration | Show information about configuration sessions |
| session | Show active configuration sessions |
| s3 | Shows configuration session given a name |
| __readonly__ | (Optional) Read only |
| ssn-name | (Optional) |
| TABLE_session_details | (Optional) Show session details for given name |
| ssn-cmd-num | (Optional) |
| command | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2816469521

---

# Command: show configuration session

## Syntax
```
show configuration session [ __readonly__ [ TABLE_session_all <ssn-name> [ TABLE_session_all_cmd [ <ssn-cmd-num> ] [ <command>
 ] ] ] <activesesscnt> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| configuration | Show information about configuration sessions |
| session | Show active configuration sessions |
| __readonly__ | (Optional) Read only |
| TABLE_session_all | (Optional) Show session table |
| ssn-name | (Optional) |
| TABLE_session_all_cmd | (Optional) Show session related commands |
| ssn-cmd-num | (Optional) |
| command | (Optional) |
| activesesscnt | (Optional) Number of active configuration sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1458240898

---

# Command: show configuration session global-info

## Syntax
```
show configuration session global-info [ __readonly__ <max-ssns> <max-cmds> <curr-num-ssns> <curr-num-cmds> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| configuration | Show information about configuration sessions |
| session | Show active configuration sessions |
| global-info | Show configuration sessions global-info |
| __readonly__ | (Optional) Read only |
| max-ssns | (Optional) |
| max-cmds | (Optional) |
| curr-num-ssns | (Optional) |
| curr-num-cmds | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp8320932880

---

# Command: show configuration session status

## Syntax
```
show configuration session status [ <s3> ] [ __readonly__ [ TABLE_session_status <ssn-name> <last-action> <ac-status> <ac-reason>
 <ac-tstamp> [ <failed-cmd-num> ] [ <failed-cmd> ] [ <last-vfy-cmd-num> ] [ <last-vfy-cmd> ] [ <last-vfy-tstamp> ] [ <rollback-status>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| configuration | Show information about configuration sessions |
| session | Show active configuration sessions |
| status | Show configuration session-mgr status |
| s3 | (Optional) Shows configuration session status given a name |
| __readonly__ | (Optional) Read only |
| TABLE_session_status | (Optional) Show session status table |
| ssn-name | (Optional) |
| last-action | (Optional) Last Action |
| ac-status | (Optional) Last Action Status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2853153510

---

# Command: show configuration session summary

## Syntax
```
show configuration session summary [ __readonly__ [ TABLE_session_summary <ssn-name> <username> <tstamp> ] [ <activesesscnt>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| configuration | Show information about configuration sessions |
| session | Show active configuration sessions |
| summary | Show summary of the active configuration sessions |
| __readonly__ | (Optional) Read only |
| TABLE_session_summary | (Optional) Show session summary table |
| ssn-name | (Optional) |
| username | (Optional) Session Owner |
| tstamp | (Optional) Creation Time |
| activesesscnt | (Optional) Number of active configuration sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1287768327

---

# Command: show consistency-checker copp

## Syntax
```
show consistency-checker copp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| copp | Verify copp programming from software context |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3810701593

---

# Command: show consistency-checker egress-xlate private-vlan

## Syntax
```
show consistency-checker egress-xlate private-vlan <vlan>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| egress-xlate | Check PVLAN egress-xlate |
| private-vlan | Verifies private-vlan egress-xlate in the hardware |
| vlan | Enter private-vlan id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3587921881

---

# Command: show consistency-checker fex-interfaces fex

## Syntax
```
show consistency-checker fex-interfaces { fex <id> &#124; interface <ifid> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| fex-interfaces | Compares software and hardware state of fex interfaces |
| fex | Limit display to interfaces on this fex |
| id | Enter module number |
| interface | Limit display to FEX interface |
| ifid | FEX interface name |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3966106033

---

# Command: show consistency-checker forwarding ipv6

## Syntax
```
show consistency-checker forwarding ipv6 [ unicast ] [ suppress-transient ] [ vrf { <vrf-name> &#124; all_vrfs } ] [ module { <module>
 &#124; all_modules } ] [ __readonly__ [ <err_str> ] [ <cc_header> ] [ <table_id> ] [ <slot_id> ] [ <exec_time> ] [ <elapsed_time>
 ] [ <inconsis_adjs> ] [ TABLE_inconsistency_adjs { <idipv6> <slotipv6> [ <unitipv6> ] <vrfipv6> [ <ipv6addr> ] [ <ipv6prefix>
 ] [ <interfaceipv6> ] <reasonipv6> } ] [ <inconsis_routes> ] [ TABLE_inconsistency_routes { <idipv6> <slotipv6> [ <unitipv6>
 ] <vrfipv6> [ <ipv6addr> ] [ <ipv6prefix> ] [ <interfaceipv6> ] <reasonipv6> } ] [ <run_status> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| consistency-checker | Consistency Checker |
| forwarding | Display Forwarding Information |
| ipv6 | ipv6 |
| unicast | (Optional) unicast |
| suppress-transient | (Optional) Supress Transient state |
| vrf | (Optional) check routes for a specific VRF |
| vrf-name | (Optional) VRF name |
| module | (Optional) check routes for a specific module |
| module | (Optional) module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp3156985339

---

# Command: show consistency-checker forwarding show forwarding inconsistency

## Syntax
```
show consistency-checker forwarding [ ip &#124; ipv4 ] [ unicast ] [ suppress-transient ] [ vrf { <vrf-name> &#124; all_vrfs } ] [ module
 { <module> &#124; all_modules } ] &#124; show forwarding [ ip &#124; ipv4 ] [ unicast ] inconsistency [ suppress-transient ] [ vrf { <vrf-name>
 &#124; all_vrfs } ] [ module { <module> &#124; all_modules } ] [ __readonly__ TABLE_inconsistency <id> <slot> [ <unit> ] <vrf> [ <ipaddr>
 ] [ <ipprefix> ] [ <interface> ] <reason> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| consistency-checker | Consistency Checker |
| forwarding | Display Forwarding Information |
| inconsistency | route inconsistency check |
| ip | (Optional) ipv4 |
| ipv4 | (Optional) ipv4 |
| unicast | (Optional) unicast |
| suppress-transient | (Optional) Supress Transient state |
| vrf | (Optional) check routes for a specific VRF |
| vrf-name | (Optional) VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4078901678

---

# Command: show consistency-checker forwarding single-route ipv4 vrf

## Syntax
```
show consistency-checker forwarding single-route { ipv4 &#124; ipv6 } <ip-prefix> vrf <vrf-name> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| forwarding | Display Forwarding Information |
| single-route | Run the consistency checker for a single route |
| ipv4 | IPv4 address |
| ipv6 | IPv6 address |
| ip-prefix | Specify an IP prefix/mask |
| vrf | check routes for a specific VRF |
| vrf-name | vrf name |
| brief | (Optional) Show consistency checker structured output in brief |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, routing, overlay, network, S-commands
**Command ID:** wp3154066774

---

# Command: show consistency-checker gwmacdb

## Syntax
```
show consistency-checker gwmacdb
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| gwmacdb | Check gateway mac table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1278309475

---

# Command: show consistency-checker hardware-telemetry inband brief

## Syntax
```
show consistency-checker hardware-telemetry inband { brief &#124; detail }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| hardware-telemetry | feature hardware-telemetry |
| inband | inband-telemetry version |
| brief | Show consistency checker structured output in brief |
| detail | Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2210571519

---

# Command: show consistency-checker hardware-telemetry postcard brief

## Syntax
```
show consistency-checker hardware-telemetry postcard { brief &#124; detail }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| hardware-telemetry | feature hardware-telemetry |
| postcard | postcard-telemetry version |
| brief | Show consistency checker structured output in brief |
| detail | Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4293339824

---

# Command: show consistency-checker kim

## Syntax
```
show consistency-checker kim
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| kim | Kernel Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3421651160

---

# Command: show consistency-checker kim interface

## Syntax
```
show consistency-checker kim { interface <ifid> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| kim | kernel interface |
| interface | Limit display to interface |
| ifid | Interface |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1032927170

---

# Command: show consistency-checker l2-tahoe mac-address

## Syntax
```
show consistency-checker l2-tahoe mac-address <mac-addr> [ module <module> ] [ unit <unit> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l2-tahoe | Verify l2 mac programming in the hardware |
| mac-address | MAC address |
| mac-addr | address |
| module | (Optional) Module to run the consistency-checker on |
| module | (Optional) Module number |
| unit | (Optional) Unit to run the consistency checker on |
| unit | (Optional) Enter Unit Number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1044716450

---

# Command: show consistency-checker l2-tahoe module

## Syntax
```
show consistency-checker l2-tahoe module <module> [ unit <unit> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l2-tahoe | Verify l2 mac programming in the hardware |
| module | Module to run the consistency-checker on |
| module | Enter module number |
| unit | (Optional) Unit to run the consistency checker on |
| unit | (Optional) Enter unit number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3791942010

---

# Command: show consistency-checker l2-tahoe switchport interface

## Syntax
```
show consistency-checker l2-tahoe switchport interface <if_name> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l2-tahoe | Verify l2 mac programming in the hardware |
| switchport | Switchport Interface |
| interface | interface |
| if_name | Physical or Logical interface |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2310519066

---

# Command: show consistency-checker l2 multicast group source vlan

## Syntax
```
show consistency-checker l2 multicast group <grp-address> source <src-address> vlan <vlan-id> [ debug-logs ] [ brief &#124; detail
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l2 | Verify l2 mac programming in the hardware |
| multicast | multicast related information |
| group | Do consistency check for group |
| grp-address | group IP address |
| source | Do consistency check for source |
| src-address | source IP address |
| vlan | Do consistency check for vlan |
| vlan-id | vlan number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2712023590

---

# Command: show consistency-checker l3-interface module

## Syntax
```
show consistency-checker l3-interface { module <moduleid> &#124; interface <ifid> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l3-interface | Compares software and hardware properties of L3 interfaces |
| module | Limit display to interfaces on module |
| moduleid | Module number |
| interface | Limit display to interface |
| ifid | Interface name |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4586264070

---

# Command: show consistency-checker l3 multicast source vrf

## Syntax
```
show consistency-checker l3 multicast [ group { <grp-address> [ <mask> ] &#124; <gprefix> } ] source <src-address> vrf <vrf-string>
 [ debug-logs ] [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| l3 | l3 consistency |
| multicast | multicast related information |
| group | (Optional) Do consistency check for group |
| grp-address | (Optional) group IP address |
| mask | (Optional) mask for group ip address |
| gprefix | (Optional) IPv4 Multicast Group Prefix |
| source | Do consistency check for source |
| src-address | source IP address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1296533327

---

# Command: show consistency-checker link-state fabric-ieth

## Syntax
```
show consistency-checker link-state fabric-ieth { [ module <module> ] } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| link-state | Compares software and hardware link state of interfaces |
| fabric-ieth | Internal Fabric ports |
| module | (Optional) Limit display to interfaces on module |
| module | (Optional) Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2492564879

---

# Command: show consistency-checker link-state module

## Syntax
```
show consistency-checker link-state { module <module> &#124; interface <ifid> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| link-state | Compares software and hardware link state of interfaces |
| module | Limit display to interfaces on module |
| module | Module number |
| interface | Limit display to interface |
| ifid | Interface name |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2392348155

---

# Command: show consistency-checker membership port-channels

## Syntax
```
show consistency-checker membership port-channels [ interface <ch-id> ] [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| membership | Check various memberships |
| port-channels | Verifies port channel membership in the hardware |
| interface | (Optional) Port-channel number |
| ch-id | (Optional) Port-Channel name |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, layer2, network, S-commands
**Command ID:** wp3332114383

---

# Command: show consistency-checker membership vlan

## Syntax
```
show consistency-checker membership vlan <vlanid> [ private-vlan [ interface [ <int-id> &#124; <ch-id> ] ] ] [ native-vlan ] [
 brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Verifies vlan membership in the hardware |
| vlanid | Enter vlan id |
| consistency-checker | Consistency Checker |
| membership | Check various memberships |
| private-vlan | (Optional) Check private-vlan primary vlan |
| interface | (Optional) Interface |
| int-id | (Optional) Interface name |
| ch-id | (Optional) Port-Channel name |
| native-vlan | (Optional) Check for native vlans |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, network, S-commands
**Command ID:** wp1286469151

---

# Command: show consistency-checker pacl extended ingress ipv6 interface

## Syntax
```
show consistency-checker pacl extended ingress ipv6 interface { <int-id> &#124; <ch-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ipv6 | ipv6 protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| brief | (Optional) Show consistency checker structured output in brief |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp3223891143

---

# Command: show consistency-checker pacl extended ingress ip module

## Syntax
```
show consistency-checker pacl extended ingress ip module <module-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ip | ip protocol |
| module | Limit display to L2 interfaces on this module |
| module-id | Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, network, S-commands
**Command ID:** wp6808217500

---

# Command: show consistency-checker pacl extended ingress ipv6 module

## Syntax
```
show consistency-checker pacl extended ingress ipv6 module <module-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ipv6 | ipv6 protocol |
| module | Limit display to L2 interfaces on this module |
| module-id | Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, network, S-commands
**Command ID:** wp3497155720

---

# Command: show consistency-checker pacl extended ingress ip interface

## Syntax
```
show consistency-checker pacl extended ingress ip interface { <int-id> &#124; <ch-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ip | ip protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| brief | (Optional) Show consistency checker structured output in brief |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp4013932939

---

# Command: show consistency-checker pacl extended ingress mac module

## Syntax
```
show consistency-checker pacl extended ingress mac module <module-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| mac | ethernet protocol |
| module | Limit display to L2 interfaces on this module |
| module-id | Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp3972495354

---

# Command: show consistency-checker pacl extended ingress mac interface

## Syntax
```
show consistency-checker pacl extended ingress mac interface { <int-id> &#124; <ch-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| mac | ethernet protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| brief | (Optional) Show consistency checker structured output in brief |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, S-commands
**Command ID:** wp8110218100

---

# Command: show consistency-checker pacl module

## Syntax
```
show consistency-checker pacl module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| module | Limit display to L2 interfaces on this module |
| module | Enter module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp3505305439

---

# Command: show consistency-checker pacl port-channels

## Syntax
```
show consistency-checker pacl port-channels [ interface <ch-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| pacl | Verify pacl programming in the hardware |
| port-channels | Verifies port channel pacl programming in the hardware |
| interface | (Optional) Port-channel number |
| ch-id | (Optional) Port-Channel name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, layer2, S-commands
**Command ID:** wp1815606949

---

# Command: show consistency-checker port-state

## Syntax
```
show consistency-checker port-state [ { module <module> &#124; interface <ifid> } ] [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| port-state | Validates SI, MTU and IPG Settings |
| module | (Optional) Limit display to interfaces on module |
| module | (Optional) Enter module number |
| interface | (Optional) Limit display to interface |
| ifid | (Optional) Interface name |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1762746919

---

# Command: show consistency-checker port-state fabric-ieth

## Syntax
```
show consistency-checker port-state fabric-ieth [ module <module> [ ieth-port <ieth-port> ] ] [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| port-state | Validates SI, FEC and MTU Settings |
| fabric-ieth | Internal Fabric ports |
| module | (Optional) Limit display to interfaces on module |
| module | (Optional) Enter module number |
| ieth-port | (Optional) Enter ieth-port number |
| ieth-port | (Optional) Enter ieth-port number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3527379472

---

# Command: show consistency-checker racl extended egress ipv6 interface

## Syntax
```
show consistency-checker racl extended egress ipv6 interface { <int-id> &#124; <ch-id> &#124; <vlan-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| egress | egress direction |
| ipv6 | ipv6 protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| vlan-id | SVI VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp1583446354

---

# Command: show consistency-checker racl extended egress ip interface

## Syntax
```
show consistency-checker racl extended egress ip interface { <int-id> &#124; <ch-id> &#124; <vlan-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| egress | egress direction |
| ip | ip protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| vlan-id | SVI VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp3748768433

---

# Command: show consistency-checker racl extended ingress ipv6 module

## Syntax
```
show consistency-checker racl extended ingress ipv6 module <module-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ipv6 | ipv6 protocol |
| module | Limit display to L3 interfaces on this module |
| module-id | Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, network, S-commands
**Command ID:** wp3270320420

---

# Command: show consistency-checker racl extended ingress ip module

## Syntax
```
show consistency-checker racl extended ingress ip module <module-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ip | ip protocol |
| module | Limit display to L3 interfaces on this module |
| module-id | Enter module number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, network, S-commands
**Command ID:** wp9367138700

---

# Command: show consistency-checker racl extended ingress ip interface

## Syntax
```
show consistency-checker racl extended ingress ip interface { <int-id> &#124; <ch-id> &#124; <vlan-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ip | ip protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| vlan-id | SVI VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp1722253560

---

# Command: show consistency-checker racl extended ingress ipv6 interface

## Syntax
```
show consistency-checker racl extended ingress ipv6 interface { <int-id> &#124; <ch-id> &#124; <vlan-id> } [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ipv6 | ipv6 protocol |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |
| vlan-id | SVI VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp5435503450

---

# Command: show consistency-checker racl module

## Syntax
```
show consistency-checker racl module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| module | Limit display to L3 interfaces on this module |
| module | Enter module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp3916141804

---

# Command: show consistency-checker racl port-channels

## Syntax
```
show consistency-checker racl port-channels [ interface <ch-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| port-channels | Verifies port channel racl programming in the hardware |
| interface | (Optional) Port-channel number |
| ch-id | (Optional) Port-Channel name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, layer2, S-commands
**Command ID:** wp1437672621

---

# Command: show consistency-checker racl svi interface

## Syntax
```
show consistency-checker racl svi interface <vlan-id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| racl | Verify racl programming in the hardware |
| svi | Verifies SVI racl programming in the hardware |
| interface | SVI number |
| vlan-id | SVI VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, S-commands
**Command ID:** wp1782403580

---

# Command: show consistency-checker segment-routing mpls ip mask vrf

## Syntax
```
show consistency-checker segment-routing mpls ip <ip-address> mask <ip-mask> vrf <vrf-name> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| segment-routing | Segment-routing |
| mpls | MPLS Information |
| ip | IP Information |
| ip-address | IP Address |
| mask | Mask Information |
| ip-mask | Subnet Mask |
| vrf | VRF Information |
| vrf-name | VRF Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, routing, overlay, network, S-commands
**Command ID:** wp1655593032

---

# Command: show consistency-checker selective-qinq

## Syntax
```
show consistency-checker selective-qinq
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| selective-qinq | Selective QinQ consistency checker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1523559783

---

# Command: show consistency-checker selective-qinq interface

## Syntax
```
show consistency-checker selective-qinq interface { <int-id> &#124; <ch-id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| selective-qinq | Selective QinQ consistency checker |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4043005900

---

# Command: show consistency-checker stp-state vlan

## Syntax
```
show consistency-checker stp-state vlan <vlan> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Verifies spanning tree state in the hardware for all interfaces in the vlan |
| vlan | Enter vlan id |
| consistency-checker | Consistency Checker |
| stp-state | Verify spanning tree state in the hardware |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1474256944

---

# Command: show consistency-checker vacl

## Syntax
```
show consistency-checker vacl
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vacl | Verify vacl programming in the hardware |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, security, S-commands
**Command ID:** wp2193023500

---

# Command: show consistency-checker vacl extended ingress ipv6 vlan

## Syntax
```
show consistency-checker vacl extended ingress ipv6 vlan <vlan-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vacl | Verify vacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ipv6 | ipv6 protocol |
| vlan | VLAN |
| vlan-id | vlan number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp5175329540

---

# Command: show consistency-checker vacl extended ingress ip vlan

## Syntax
```
show consistency-checker vacl extended ingress ip vlan <vlan-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vacl | Verify vacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| ip | ip protocol |
| vlan | VLAN |
| vlan-id | vlan number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, network, S-commands
**Command ID:** wp2945634990

---

# Command: show consistency-checker vacl extended ingress mac vlan

## Syntax
```
show consistency-checker vacl extended ingress mac vlan <vlan-id> [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vacl | Verify vacl programming in the hardware |
| extended | extended |
| ingress | ingress direction |
| mac | ethernet protocol |
| vlan | VLAN |
| vlan-id | vlan number |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, security, S-commands
**Command ID:** wp3377039139

---

# Command: show consistency-checker vpc

## Syntax
```
show consistency-checker vpc [ source-interface [ <int-id> &#124; <ch-id> ] ] [ brief &#124; detail ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vpc | vPC related information |
| source-interface | (Optional) Source vPC member |
| int-id | (Optional) Eth Interface |
| ch-id | (Optional) Port-Channel |
| brief | (Optional) Show consistency checker structured output in brief |
| detail | (Optional) Show consistency checker structured output in detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp3354650440

---

# Command: show consistency-checker vxlan config-check

## Syntax
```
show consistency-checker vxlan config-check [ verbose-mode ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| config-check | Check the inconsistencies in the config |
| verbose-mode | (Optional) config-check detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3644766500

---

# Command: show consistency-checker vxlan flood_list

## Syntax
```
show consistency-checker vxlan flood_list
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| flood_list | Display VxLAN Floodlist consistency information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1995124552

---

# Command: show consistency-checker vxlan infra

## Syntax
```
show consistency-checker vxlan infra [ verbose-mode ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vxlan | VxLAN consistency checker |
| consistency-checker | Consistency Checker |
| infra | infra |
| verbose-mode | (Optional) detailed CC output |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3522075039

---

# Command: show consistency-checker vxlan l2 module

## Syntax
```
show consistency-checker vxlan l2 module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| l2 | Check L2 inconsistencies |
| module | Module to run the consistency-checker on |
| module | Enter module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1107874492

---

# Command: show consistency-checker vxlan l3 vrf start

## Syntax
```
show consistency-checker vxlan l3 vrf { <vrf-name> &#124; all } { start-scan &#124; report }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vxlan | VxLAN consistency checker |
| consistency-checker | Consistency Checker |
| l3 | l3 |
| vrf | VRF |
| vrf-name | vrf name |
| all | All VRFs |
| start-scan | Start Route CC |
| report | Show Route CC report |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3264637563

---

# Command: show consistency-checker vxlan mh mac-addresses

## Syntax
```
show consistency-checker vxlan mh mac-addresses
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| mh | VxLAN BGP EVPN Multi Homing CC commands |
| mac-addresses | Check mac address consistency between L2RIB and L2FM |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp2788453042

---

# Command: show consistency-checker vxlan mh pathlist

## Syntax
```
show consistency-checker vxlan mh pathlist
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| mh | VxLAN BGP EVPN Multi Homing CC commands |
| pathlist | Check Vxlan BGP EVPN MH Control plane and resultant pathlists consistency |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1423306422

---

# Command: show consistency-checker vxlan pv

## Syntax
```
show consistency-checker vxlan pv
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| pv | pv consistency checker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3792325057

---

# Command: show consistency-checker vxlan qinq-qinvni

## Syntax
```
show consistency-checker vxlan qinq-qinvni
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vxlan | VxLAN consistency checker |
| consistency-checker | Consistency Checker |
| qinq-qinvni | QinQ consistency checker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1334862789

---

# Command: show consistency-checker vxlan selective-qinvni

## Syntax
```
show consistency-checker vxlan selective-qinvni
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| selective-qinvni | Selective QinVNI consistency checker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp4132070306

---

# Command: show consistency-checker vxlan selective-qinvni interface

## Syntax
```
show consistency-checker vxlan selective-qinvni interface { <int-id> &#124; <ch-id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| selective-qinvni | Selective QinVNI consistency checker |
| interface | Interface |
| int-id | Interface |
| ch-id | Port-Channel name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, overlay, S-commands
**Command ID:** wp1253990070

---

# Command: show consistency-checker vxlan vlan

## Syntax
```
show consistency-checker vxlan vlan { <vlanid> &#124; all } [ verbose-mode ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vxlan | VxLAN consistency checker |
| vlan | Verifies flood list programming for vxlan vlans |
| consistency-checker | Consistency Checker |
| vlanid | Enter vlan id |
| all | Check CC for all vxlans |
| verbose-mode | (Optional) detailed CC output |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, interface, overlay, S-commands
**Command ID:** wp1682981403

---

# Command: show consistency-checker vxlan xconnect

## Syntax
```
show consistency-checker vxlan xconnect
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| consistency-checker | Consistency Checker |
| vxlan | VxLAN consistency checker |
| xconnect | Cross-Connect consistency checker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp4567442510

---

# Command: show

## Syntax
```
show { consistency-checker l2 module <modnum> &#124; forwarding consistency l2 <modnum> } [ __readonly__ <status> [ <l2entry> [
 TABLE_mac_address <disp_mac_addr><disp_type><disp_vlan><disp_is_static><disp_age><disp_is_secure><disp_is_ntfy><disp_port>
 ] ] [ <l2entry_ext> [ TABLE_mac_address <disp_mac_addr><disp_type><disp_vlan><disp_is_static><disp_age><disp_is_secure><disp_is_ntfy><disp_port>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| consistency-checker | Consistency Checker |
| forwarding | Forwarding information |
| consistency | consistency |
| l2 | Verify l2 mac programming in the hardware |
| module | Module number |
| modnum | Module Number |
| __readonly__ | (Optional) |
| status | (Optional) Result of Consistency Checker |
| l2entry | (Optional) L2 entry |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2339860030

---

# Command: show controller accounting log

## Syntax
```
show controller <ctrl-id> accounting log
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| controller | Controller command |
| ctrl-id | Controller id value |
| accounting | Accounting |
| log | Show log information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1491195208

---

# Command: show copp diff profile profile2

## Syntax
```
show copp diff profile <profile_type> [ prior-ver ] profile2 <profile_type2>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| copp | Control-Plane Policing |
| diff | Difference between CoPP Profiles |
| profile | CoPP Profile |
| profile_type | CoPP Profile Types |
| prior-ver | (Optional) Previous Configured Version |
| profile2 | CoPP Profile |
| profile_type2 | CoPP Profile Types |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2464195117

---

# Command: show copp profile

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| copp | Control-Plane Policing |
| profile | CoPP Profile |
| strict | display strict profile |
| moderate | display moderate profile |
| lenient | display lenient profile |
| dense | display dense profile |
| __readonly__ | (Optional) Read Only |
| acl-type | (Optional) access-list type |
| TABLE_coppprof | (Optional) copp profile |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1621667501

---

# Command: show copp status

## Syntax
```
show copp status [ __readonly__ { last_config_operation <last_cfg_oper> } { last_config_operation_time <last_cfg_oper_time>
 } { last_config_operation_status <last_cfg_oper_status> } [ last_config_operation_error_time <last_cfg_oper_error_time> ]
 [ last_config_operation_error <last_cfg_oper_error> ] { service_policy <srv_policy> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| copp | Control-Plane Policing |
| status | Show the internal status of CoPP |
| __readonly__ | (Optional) |
| last_config_operation | (Optional) last config operation |
| last_cfg_oper | (Optional) last config operation |
| last_config_operation_time | (Optional) timestamp of last config operation |
| last_cfg_oper_time | (Optional) timestamp of last config operation |
| last_config_operation_status | (Optional) status of last config operation |
| last_cfg_oper_status | (Optional) status of last config operation |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3034876229

---

# Command: show copyright

## Syntax
```
show copyright [ __readonly__ { <content> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| copyright | Copyright information |
| __readonly__ | (Optional) |
| content | (Optional) Copyrigh information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2069230298

---

# Command: show cores

## Syntax
```
show cores [ vdc-all &#124; { vdc [ <e-vdc2> &#124; <vdc-id> ] } ] [ __readonly__ { [ TABLE_cores <vdc_id> <module_id> <instance> <process_name>
 <pid> <sys_time> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| cores | show all core dumps for the current vdc |
| vdc-all | (Optional) show core dumps from all vdcs |
| vdc | (Optional) show all core dumps for the vdc |
| __readonly__ | (Optional) |
| TABLE_cores | (Optional) |
| vdc_id | (Optional) vdc id |
| module_id | (Optional) module id |
| instance | (Optional) instance number |
| process_name | (Optional) name of the process |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2228088303

---

# Command: show crypto ca certificates

## Syntax
```
show crypto ca certificates [ __readonly__ [ { TABLE_ca_certificates <trustpoint> [ <certificate> ] [ { TABLE_ca_cert_chains
 <index> <ca_certificate> } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| ca | show trustpoint configuration |
| certificates | show various certificates |
| __readonly__ | (Optional) |
| TABLE_ca_certificates | (Optional) Table of CA certificates |
| trustpoint | (Optional) Trustpoint name |
| certificate | (Optional) Certificate |
| TABLE_ca_cert_chains | (Optional) Table of CA certificates in chain |
| index | (Optional) CA Certificate Index |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3759764000

---

# Command: show crypto ca certificates

## Syntax
```
show crypto ca certificates <s0> [ __readonly__ { Trustpoint <trustpoint> } [ { Certificate <certificate> } ] [ { TABLE_ca_cert_chains
 <index> <ca_certificate> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| ca | show trustpoint configuration |
| certificates | show various certificates |
| s0 | trustpoint label |
| __readonly__ | (Optional) |
| Trustpoint | (Optional) Trustpoint |
| trustpoint | (Optional) Trustpoint |
| Certificate | (Optional) Certificate |
| certificate | (Optional) Certificate |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2758249731

---

# Command: show crypto ca certstore

## Syntax
```
show crypto ca certstore [ __readonly__ { certstore_lookup <lookup_type> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | Show crypto configuration |
| ca | show crypto ca configuration |
| certstore | Show the configured certstore |
| __readonly__ | (Optional) |
| certstore_lookup | (Optional) Certificate strore lookup |
| lookup_type | (Optional) Lookup type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2967369033

---

# Command: show crypto ca crl

## Syntax
```
show crypto ca crl <s0> [ __readonly__ { Trustpoint <trustpoint> } [ { CRL <crl> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| ca | show trustpoint configuration |
| crl | show CRL |
| s0 | trustpoint label |
| __readonly__ | (Optional) |
| Trustpoint | (Optional) Trustpoint |
| trustpoint | (Optional) Trustpoint |
| CRL | (Optional) Certificate Revocation List |
| crl | (Optional) Certificate Revocation List |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp1621246332

---

# Command: show crypto ca remote-certstore

## Syntax
```
show crypto ca remote-certstore [ __readonly__ { remote_cert_store <rem_cert_store> } [ { crl_timer <crltimer> } { ldap_server_group
 <ldap_server_grp> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | Show crypto configuration |
| ca | show crypto ca configuration |
| remote-certstore | Show remote certstore configuration |
| __readonly__ | (Optional) |
| remote_cert_store | (Optional) Remote cert store |
| rem_cert_store | (Optional) Remote certificate store |
| crl_timer | (Optional) CRL timer |
| crltimer | (Optional) CRL timer |
| ldap_server_group | (Optional) LDAP Server Group |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2132612278

---

# Command: show crypto ca trustpoints

## Syntax
```
show crypto ca trustpoints [ __readonly__ [ { TABLE_ca_truspoints <trustpoint> <key-pair> [ { TABLE_revocation_methods <revocation-method>
 } ] [ <ocsp-url> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| ca | show trustpoint configuration |
| trustpoints | show trustpoint configuration |
| __readonly__ | (Optional) |
| trustpoint | (Optional) Trustpoint |
| key-pair | (Optional) Key pair |
| TABLE_revocation_methods | (Optional) Table of revocation methods |
| revocation-method | (Optional) Revocation mehtod |
| ocsp-url | (Optional) OCSP URL |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3676893825

---

# Command: show crypto ca trustpool

## Syntax
```
show crypto ca trustpool [ __readonly__ [ { TABLE_ca_trustpool <serial-number> <subject> <issued-by> <validity-start> <validity-end>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto information |
| ca | show trustpool data |
| trustpool | trustpool contents |
| __readonly__ | (Optional) |
| TABLE_ca_trustpool | (Optional) Table of CA trustpool |
| serial-number | (Optional) Serial number |
| subject | (Optional) subject |
| issued-by | (Optional) Issued by |
| validity-start | (Optional) validity start date |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3920296865

---

# Command: show crypto ca trustpool last download status

## Syntax
```
show crypto ca trustpool last download status [ __readonly__ [ http_url <http_url> ] [ download_time <download_time> ] [ trustpool_download_status
 <status> ] [ download_failure <reason> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto information |
| ca | show trustpool data |
| trustpool | trustpool data |
| last | last trustpool download status |
| download | download of trustpool |
| status | download status |
| __readonly__ | (Optional) |
| http_url | (Optional) http url configured |
| http_url | (Optional) HTTP url |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp4954330210

---

# Command: show crypto ca trustpool policy

## Syntax
```
show crypto ca trustpool policy [ __readonly__ [ http_url <http_url> ] [ config_vrf [ <config_vrf> ] [ <src_intf> ] ] [ proxy_server
 [ <proxy_server> ] [ <proxy_server_port> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto information |
| ca | show Certificate authority related config |
| trustpool | show trustpool policy |
| policy | trustpool configuration |
| __readonly__ | (Optional) |
| http_url | (Optional) http url configured |
| http_url | (Optional) HTTP url |
| config_vrf | (Optional) Configured vrf |
| config_vrf | (Optional) vrf configured |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1965763864

---

# Command: show crypto certificatemap

## Syntax
```
show crypto certificatemap [ __readonly__ [ { TABLE_certmap <map_name> <subject_name> <alternate_email> <alternate_upn> }
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| certificatemap | show certificatemap filters |
| __readonly__ | (Optional) |
| TABLE_certmap | (Optional) Table of Certificate Map |
| map_name | (Optional) Map name |
| subject_name | (Optional) Subject name |
| alternate_email | (Optional) Alternate Email |
| alternate_upn | (Optional) Alternate UPN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2536671029

---

# Command: show crypto key mypubkey rsa

## Syntax
```
show crypto key mypubkey rsa [ __readonly__ [ { TABLE_rsa_keys <key_label> <key_size> <exportable> <err_string> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| key | show key configuration |
| mypubkey | show my public keys configuration |
| rsa | show my rsa public keys configuration |
| __readonly__ | (Optional) |
| TABLE_rsa_keys | (Optional) Table of RSA keys |
| key_label | (Optional) Key Lable |
| key_size | (Optional) Key size |
| exportable | (Optional) Exportable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp3370717690

---

# Command: show crypto ssh-auth-map

## Syntax
```
show crypto ssh-auth-map [ __readonly__ [ { TABLE_ssh_auth_map <issuer_name> <map1> [ <map2> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| crypto | show crypto configuration |
| ssh-auth-map | show mapping filters applied for ssh authentication |
| __readonly__ | (Optional) |
| TABLE_ssh_auth_map | (Optional) Table of SSH Auth MAP |
| issuer_name | (Optional) Issuer Name |
| map1 | (Optional) Map 1 |
| map2 | (Optional) Map 2 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2164442954

---

# Command: show cts

## Syntax
```
show cts [ __readonly__ <device-id> <cache_en> <num-dot1x> <num-man> <sgt> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| cts | Show CTS global configuration |
| __readonly__ | (Optional) |
| device-id | (Optional) name |
| cache_en | (Optional) enable/disable |
| num-dot1x | (Optional) number of interfaces in dot1x mode |
| num-man | (Optional) number of interfaces in manual mode |
| sgt | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2663891836

---

# Command: show current

## Syntax
```
show current
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display region configurations |
| current | Display mst configuration currently used |

**Command Mode:** /exec/configure/spanning-tree/mst/configuration

**Source:** b_N9K_Show_Commands_93x_chapter_011.html
**Tags:** show-mode, S-commands
**Command ID:** wp2148231110

---

