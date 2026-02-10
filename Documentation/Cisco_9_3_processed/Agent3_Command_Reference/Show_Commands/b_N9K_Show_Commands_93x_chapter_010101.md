# Chapter: V Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010101.html
**Type:** Show Commands  
**Chapter:** Group-10101 Commands  
**Total Commands:** 66

## Command List

- `show vdc`
- `show vdc current-vdc`
- `show vdc fcoe-vlan-range`
- `show vdc resource`
- `show vdc resource`
- `show vdc resource template`
- `show version`
- `show version epld`
- `show version image`
- `show version module`
- `show version module epld`
- `show virtual-service`
- `show virtual-service storage pool list`
- `show virtual-service tech-support`
- `show virtual-service utilization name`
- `show virtual-service version`
- `show vlan`
- `show vlan access-list`
- `show vlan access-map`
- `show vlan all-ports`
- `show vlan counters`
- `show vlan dot1Q tag native`
- `show vlan fcoe`
- `show vlan filter`
- `show vlan id`
- `show vlan id counters`
- `show vlan id vn-segment`
- `show vlan name`
- `show vlan private-vlan`
- `show vlan private-vlan type`
- `show vlan xbrief`
- `show vlan xsummary`
- `show vmtracker`
- `show vmtracker certificate`
- `show vmtracker fabric auto-config`
- `show vmtracker status`
- `show vpc`
- `show vpc`
- `show vpc consistency-parameters`
- `show vpc consistency-parameters vlans`
- `show vpc fabric-ports`
- `show vpc orphan-ports`
- `show vpc peer-keepalive`
- `show vpc role`
- `show vpc statistics peer-keepalive`
- `show vpc statistics vpc`
- `show vpc virtual-peerlink dest reachable`
- `show vpc virtual-peerlink vlan consistency`
- `show vrf`
- `show vrf`
- `show vrrp`
- `show vrrp bfd-sessions`
- `show vrrpv3`
- `show vrrs client`
- `show vrrs pathway`
- `show vrrs pathway address`
- `show vrrs server`
- `show vrrs tag`
- `show vsan`
- `show vsan membership`
- `show vsan membership interface`
- `show vsan usage`
- `show vtp counters`
- `show vtp interface`
- `show vtp password`
- `show vtp status`

---

## Detailed Command Reference

# Command: show vdc

## Syntax
```
{ show vdc [ <e-vdc2> ] [ feature-set &#124; detail &#124; membership [ all &#124; status &#124; module <module> ] &#124; shared membership ] [ __readonly__
 [ detail2 ] [ <swmode> ] { TABLE_vdc <vdc_id> <vdc_name> <state> <mac> <hap> <sw> <boot_order> [ <prio> <prio_per> ] [ <create_time>
 ] [ <reload_count> ] [ <restart_count> ] [ <restart_time> ] [ <restart_reason> ] <vtype> <lc-support> [ TABLE_fs <fs_id> <fs_name>
 ] [ TABLE_port <port-list> ] } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show Virtual Device Contexts |
| vdc | Show Virtual Device Contexts |
| e-vdc2 | (Optional) Enter Virtual Device Context <vdc-id> |
| detail | (Optional) Show detailed vdc information |
| membership | (Optional) Show vdc interface membership information |
| shared | (Optional) Show the shared interfaces in a vdc |
| membership | (Optional) Show the shared interfaces in a vdc |
| module | (Optional) Show vdc interface membership information for a specific module only |
| module | (Optional) Show vdc interface membership information for a specific module only |
| status | (Optional) Show vdc related port-status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2534411530

---

# Command: show vdc current-vdc

## Syntax
```
show vdc current-vdc [ __readonly__ <mode> <name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show Virtual Device Contexts |
| vdc | Show Virtual Device Contexts |
| current-vdc | Show which vdc you are currently in |
| __readonly__ | (Optional) Read Only |
| mode | (Optional) cli mode |
| name | (Optional) vdc name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3059255270

---

# Command: show vdc fcoe-vlan-range

## Syntax
```
show vdc fcoe-vlan-range [ __readonly__ <fcoe-vdc> [ <fcoe-vlans> ] [ <sharing-vdcs> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show Virtual Device Contexts |
| vdc | Show Virtual Device Contexts |
| fcoe-vlan-range | vlans reserved for FCoE |
| __readonly__ | (Optional) Read Only |
| fcoe-vdc | (Optional) |
| sharing-vdcs | (Optional) |
| fcoe-vlans | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp6261105000

---

# Command: show vdc resource

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vdc | Show Virtual Device Contexts |
| resource | Show resource configuration across VDCs |
| res-mgr-res-known-name | (Optional) Resource name |
| detail | (Optional) Show detail resource configuration |
| hidden-too | (Optional) Also show hidden resources |
| with-flags | (Optional) Also show resource flags |
| __readonly__ | (Optional) Read Only |
| TABLE_resource | (Optional) |
| resource_name | (Optional) Resource Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1458904822

---

# Command: show vdc resource

## Syntax
```
show vdc <id> resource [ <res-mgr-res-known-name> ] [ __readonly__ { TABLE_vdc_resource_single_vdc <res_name> <min> <max>
 <used> <unused> <free> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vdc | Show Virtual Device Contexts |
| id | Enter Virtual Device Context <vdc-id> |
| resource | Show resource configuration for VDC |
| res-mgr-res-known-name | (Optional) Resource name |
| __readonly__ | (Optional) Read Only |
| res_name | (Optional) Resource Name |
| min | (Optional) Resource min configuration |
| max | (Optional) Resource max configuration |
| used | (Optional) Resource current usage for this VDC |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2596644790

---

# Command: show vdc resource template

## Syntax
```
show vdc resource template [ <res-mgr-template-known-name-all> ] [ __readonly__ TABLE_template <template_name> { TABLE_resource
 <resource_name> <min> <max> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vdc | Show Virtual Device Contexts |
| resource | Show resource configuration for VDC |
| template | Resource template configuration |
| res-mgr-template-known-name-all | (Optional) Resource template name |
| __readonly__ | (Optional) Read Only |
| TABLE_template | (Optional) |
| template_name | (Optional) Resource Template Name |
| TABLE_resource | (Optional) |
| resource_name | (Optional) Resource Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3057984616

---

# Command: show version

## Syntax
```
version
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| version | Show the software version |
| __readonly__ | (Optional) |
| header_str | (Optional) |
| bios_ver_str | (Optional) |
| loader_ver_str | (Optional) |
| kickstart_ver_str | (Optional) |
| nxos_ver_str | (Optional) |
| sys_ver_str | (Optional) |
| bios_cmpl_time | (Optional) |
| kick_file_name | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1575589997

---

# Command: show version epld

## Syntax
```
show version epld <uri0> [ __readonly__ <image-info> [ { TABLE_module_info <module-type> <model> <epld-device> <version> }
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| version | Show the software version |
| epld | Show EPLD versions available in EPLD image |
| uri0 | Local URI containing EPLD Image |
| __readonly__ | (Optional) |
| image-info | (Optional) image file info |
| TABLE_module_info | (Optional) |
| module-type | (Optional) module type |
| model | (Optional) model |
| epld-device | (Optional) epld device |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3275694101

---

# Command: show version image

## Syntax
```
show version image <uri0> [ __readonly__ <md5_str> <img_file_name> [ <bios_ver_str> ] <sys_ver_str> <img_cmpl_time> [ <img_tmstmp>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| version | Show the software version |
| image | Show the software version of a given image |
| uri0 | Enter URI |
| __readonly__ | (Optional) |
| md5_str | (Optional) |
| img_file_name | (Optional) |
| bios_ver_str | (Optional) |
| sys_ver_str | (Optional) |
| img_cmpl_time | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3176125437

---

# Command: show version module

## Syntax
```
show version module <module> [ __readonly__ { TABLE_version <slot> <type> <sw> <interim> <bios> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| version | Show the software version |
| module | Show the software version of a Module |
| module | Enter module number |
| __readonly__ | (Optional) |
| TABLE_version | (Optional) Show version info |
| slot | (Optional) Slot |
| type | (Optional) image type |
| sw | (Optional) SW version |
| interim | (Optional) SW interim version |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3150868199

---

# Command: show version module epld

## Syntax
```
show version module <module> epld [ __readonly__ { [ <header_info> ] [ <module> ] [ <mi_iofpga> <version> ] [ <io_fpga> <version>
 ] [ <mi_iofpga2> <version> ] [ <mi_iofpga3> <version> ] [ <mi_iofpga4> <version> ] [ <mi_iofpga5> <version> ] [ <mi_iofpga6>
 <version> ] [ <cpu_iofpga> <version> ] [ <db_fpga> <version> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| version | Show the software version |
| module | Show the software version of a Module |
| module | Enter module number |
| epld | Show a module's current EPLD versions |
| __readonly__ | (Optional) |
| header_info | (Optional) |
| module | (Optional) |
| mi_iofpga | (Optional) |
| io_fpga | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2613555540

---

# Command: show virtual-service

## Syntax
```
show virtual-service [ { list } &#124; { global } &#124; { detail [ name <virt_serv_name> ] } &#124; { core [ name <virt_serv_name_core>
 ] } ] [ __readonly__ [ <infrastructure_major_version> <infrastructure_minor_version> <total_virtual_services_installed> <total_virtual_services_activated>
 <machine_types_supported> <machine_types_disabled> <maximum_vcpus_per_virtual_service> TABLE_resource_limits <media_name>
 <quota> <committed> <available> ] [ TABLE_list <name> <status> <package_name> ] [ TABLE_detail <name> <state> <package_name>
 <ova_path> <application_name> <application_version> <application_description> <key_type> <signing_method> <licensing_name>
 <licensing_version> <disk_reservation> <memory_reservation> <cpu_reservation> TABLE_attached_devices <type> <name> <alias>
 ] [ TABLE_core <name> <name_core> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| virtual-service | Display virtualization service information |
| global | (Optional) Virtual service global information |
| list | (Optional) List virtual services |
| detail | (Optional) Detailed information |
| core | (Optional) Core information |
| name | (Optional) Information for a specific virtual service |
| virt_serv_name | (Optional) Name of a virtual service |
| virt_serv_name_core | (Optional) Name of a virtual service |
| __readonly__ | (Optional) Read Only |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3625956847

---

# Command: show virtual-service storage pool list

## Syntax
```
show virtual-service storage pool list [ __readonly__ [ TABLE_storage <pool_name> <pool_type> <pool_path> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| virtual-service | Display virtualization service storage pool information |
| storage | Storage information about virtual service |
| pool | Storage pool information about virtual service |
| list | List storage pool for virtual service |
| __readonly__ | (Optional) Read Only |
| TABLE_storage | (Optional) Virtual service storage pool list table |
| pool_name | (Optional) Virtual service storage pool name |
| pool_type | (Optional) Virtual service storage pool type |
| pool_path | (Optional) Virtual service storage pool path |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1593832329

---

# Command: show virtual-service tech-support

## Syntax
```
show virtual-service tech-support
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| virtual-service | Gather information for virtualization services trouble shooting |
| tech-support | Gather information for trouble shooting |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1150519528

---

# Command: show virtual-service utilization name

## Syntax
```
show virtual-service utilization name <virt_serv_name> [ __readonly__ [ TABLE_cpu <request> <actual> <state> ] [ TABLE_memory
 <allocation> <used> ] [ TABLE_storage <name> <alias> <capacity> <used> <available> <usage> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| virtual-service | Display virtualization service utilization information |
| utilization | Utilization information about virtual service |
| name | Utilization of a virtual service |
| virt_serv_name | Name of a virtual service |
| __readonly__ | (Optional) Read Only |
| TABLE_storage | (Optional) Virtual service storage utilization |
| name | (Optional) storage device name |
| alias | (Optional) storage device alias |
| capacity | (Optional) Capacity 1k blocks |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3730982812

---

# Command: show virtual-service version

## Syntax
```
show virtual-service version { { installed } &#124; { name <virt_serv_name> installed } } [ __readonly__ <virt_service_name> <application_name>
 <application_version> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| virtual-service | Display virtualization service version information |
| version | Version information about virtual service |
| installed | Installed version |
| name | Version of a virtual service |
| virt_serv_name | Name of a virtual service |
| __readonly__ | (Optional) Read Only |
| virt_service_name | (Optional) Virtual service name |
| application_name | (Optional) Application name |
| application_version | (Optional) Application version |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3603302442

---

# Command: show vlan

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| controller | (Optional) Controller VLAN status |
| __readonly__ | (Optional) Read Only |
| TABLE_vlanbrief | (Optional) VLAN brief table format |
| TABLE_mtuinfo | (Optional) MTU information table format |
| vlanshowbr-hdr | (Optional) VLAN brief header |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanid-utf | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanname | (Optional) VLAN brief VLAN name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2396746259

---

# Command: show vlan access-list

## Syntax
```
show vlan access-list <name> [ <inp_seqno> ] [ __readonly__ TABLE_vacl <vacl_name> [ <vacl_seqno> ] [ TABLE_list <ip_ipv6_mac>
 <acl_name> [ TABLE_seqno <seqno> { <permitdeny> [ <proto_str> &#124; <proto> &#124; <ip> &#124; <ipv6> ] { <src_any> &#124; <src_ip_prefix> &#124;
 <src_ip_addr> <src_ip_mask> &#124; <src_ipv6_prefix> &#124; <src_ipv6_addr> <src_ipv6_mask> &#124; <mac_src> <mac_src_wild> &#124; <src_addrgrp>
 } [ <src_port_op> [ <src_port1_str> ] { <src_port1_num> } [ <src_port2_str> &#124; <src_port2_num> ] &#124; <src_portgrp> ] { <dest_any>
 &#124; <dest_ip_prefix> &#124; <dest_ip_addr> <dest_ip_mask> &#124; <dest_ipv6_prefix> &#124; <dest_ipv6_addr> <dest_ipv6_mask> &#124; <mac_dest> <mac_dest_wild>
 &#124; <dest_addrgrp> } [ <dest_port_op> [ <dest_port1_str> ] { <dest_port1_num> } [ <dest_port2_str> &#124; <dest_port2_num> ] &#124; <dest_portgrp>
 ] [ { <icmp_type> [ <icmp_code> ] &#124; <icmp_str> } &#124; { <icmpv6_type> [ <icmpv6_code> ] &#124; <icmpv6_str> } ] [ <igmp_type> &#124; <igmp_type_str>
 ] [ [ <precedence> &#124; <precedence_str> ] [ <tos> &#124; <tos_str> ] &#124; [ <dscp> &#124; <dscp_str> ] &#124; [ <ttl> ] ] [ <log> ] [ <udfs> ]
 [ <capture_session> ] [ <fragments> ] [ <plen_op> <plen1> [ <plen2> ] ] [ <urg> ] [ <ack> ] [ <psh> ] [ <rst> ] [ <syn> ]
 [ <fin> ] [ <established> ] [ <http-method> &#124; <http_opt_str> ] [ <tcp-option-length> ] [ <tcp-flags-mask> ] [ <flow_label>
 ] [ <timerange> ] [ <eth_proto> &#124; <eth_proto_str> ] [ <vlan> ] [ <cos> ] [ <match_count> ] &#124; [ TABLE_match <module> <module_match_count>
 ] &#124; [ <nve_vni> ] &#124; [ <nve_vni> ] &#124; [ <label1> [ <label2> <label3> <label4> ] ] <remark> } ] [ <action> <actionid> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Vlan commands |
| access-list | Vlan access list |
| name | List name |
| inp_seqno | (Optional) Sequence number |
| vacl_name | (Optional) List name |
| __readonly__ | (Optional) |
| vacl_seqno | (Optional) Sequence number |
| TABLE_vacl | (Optional) |
| TABLE_list | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, security, S-commands
**Command ID:** wp1929406533

---

# Command: show vlan access-map

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Vlan commands |
| access-map | List VLAN access maps |
| name | (Optional) List name |
| vacl_name | (Optional) List name |
| __readonly__ | (Optional) |
| seqno | (Optional) Sequence number |
| TABLE_vacl | (Optional) |
| TABLE_seqno | (Optional) |
| ip_ipv6_mac | (Optional) IP/iIPV6/MAC |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1190154331

---

# Command: show vlan all-ports

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| all-ports | Show all ports on VLAN |
| __readonly__ | (Optional) Read Only |
| TABLE_vlanbriefallports | (Optional) VLAN brief table format |
| vlanshowbr-hdr | (Optional) VLAN brief header |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanid-utf | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanname | (Optional) VLAN brief VLAN name |
| vlanshowbr-vlanstate | (Optional) VLAN brief VLAN state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp8235698700

---

# Command: show vlan counters

## Syntax
```
show vlan counters [ __readonly__ { TABLE_vlancounters <vlanshowbr-vlanid> [ <l2_ing_ucast_b> ] [ <l2_ing_ucast_p> ] [ <l2_ing_mcast_b>
 ] [ <l2_ing_mcast_p> ] [ <l2_ing_bcast_b> ] [ <l2_ing_bcast_p> ] [ <l2_egr_ucast_b> ] [ <l2_egr_ucast_p> ] [ <l3_ucast_rcv_b>
 ] [ <l3_ucast_rcv_p> ] [ <total_rcv_b> ] [ <total_rcv_p> ] [ <total_sent_b> ] [ <total_sent_p> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Vlan commands |
| counters | display counters |
| __readonly__ | (Optional) Read Only |
| TABLE_vlancounters | (Optional) vlan counters table format |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| l2_ing_ucast_b | (Optional) L2 Ingress unicast octets |
| l2_ing_ucast_p | (Optional) L2 Ingress unicast packets |
| l2_ing_mcast_b | (Optional) L2 Ingress multicast octets |
| l2_ing_mcast_p | (Optional) L2 Ingress multicast packets |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4719730960

---

# Command: show vlan dot1Q tag native

## Syntax
```
show vlan dot1Q tag native [ __readonly__ <tag_native_mode> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VTP VLAN status |
| dot1Q | Display dot1q parameters |
| tag | Display tag parameters |
| native | Display native vlan tagging |
| __readonly__ | (Optional) Read Only |
| tag_native_mode | (Optional) Native vlan tagging mode |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp5971283750

---

# Command: show vlan fcoe

## Syntax
```
show vlan fcoe [ <vlan-id> ] [ __readonly__ { TABLE_assoc <orig-id> <tran-id> <assoc-state> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fcoe | FCOE Congiguration |
| vlan | Original VLAN Status |
| __readonly__ | (Optional) Read Only |
| TABLE_assoc | (Optional) Association Table Format |
| vlan-id | (Optional) VLAN ID <1-4094> |
| orig-id | (Optional) Enter original VLAN-ID being associated with translated ID |
| tran-id | (Optional) Enter VSAN-ID being associated with VLAN-ID |
| assoc-state | (Optional) Show Association Status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2400306009

---

# Command: show vlan filter

## Syntax
```
show vlan filter [ access-map <name> &#124; vlan <vlan> ] [ __readonly__ TABLE_vlan_filter <vacl_name> <configured_vlans> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Vlan commands |
| filter | Information about VLAN filters |
| access-map | (Optional) Show the VLANs where an access-map is applied |
| name | (Optional) List name |
| vlan | (Optional) Show the access-map applied to a VLAN |
| vlan | (Optional) VLAN number |
| __readonly__ | (Optional) |
| TABLE_vlan_filter | (Optional) |
| vacl_name | (Optional) List name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3974990290

---

# Command: show vlan id

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| id | VLAN status by VLAN id |
| vlan-id | VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |
| __readonly__ | (Optional) Read Only |
| TABLE_vlanbriefid | (Optional) VLAN brief table format |
| TABLE_mtuinfoid | (Optional) MTU information table format |
| vlanshowbr-hdr | (Optional) VLAN brief header |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanid-utf | (Optional) VLAN brief VLAN ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1596526070

---

# Command: show vlan id counters

## Syntax
```
show vlan id <vlan-id> counters [ __readonly__ { TABLE_vlancounters <vlanshowbr-vlanid> [ <l2_ing_ucast_b> ] [ <l2_ing_ucast_p>
 ] [ <l2_ing_mcast_b> ] [ <l2_ing_mcast_p> ] [ <l2_ing_bcast_b> ] [ <l2_ing_bcast_p> ] [ <l2_egr_ucast_b> ] [ <l2_egr_ucast_p>
 ] [ <l3_ucast_rcv_b> ] [ <l3_ucast_rcv_p> ] [ <total_rcv_b> ] [ <total_rcv_p> ] [ <total_sent_b> ] [ <total_sent_p> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | Vlan commands |
| id | VLAN status by VLAN id |
| counters | display counters |
| vlan-id | VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |
| __readonly__ | (Optional) Read Only |
| TABLE_vlancounters | (Optional) vlan counters table format |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| l2_ing_ucast_b | (Optional) L2 Ingress unicast octets |
| l2_ing_ucast_p | (Optional) L2 Ingress unicast packets |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2612339617

---

# Command: show vlan id vn-segment

## Syntax
```
show vlan id <vlan-id> vn-segment [ __readonly__ <vlanshowinfo-segid-hdr> { TABLE_seginfoid <vlanshowinfo-seg-vlanid> <vlanshowinfo-segment-id>
 } <show-end> [ <true-end> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| id | VLAN status by VLAN id |
| vn-segment | Show vn-segment mapping |
| vlan-id | VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |
| __readonly__ | (Optional) Read Only |
| TABLE_seginfoid | (Optional) Segment id information table format |
| vlanshowinfo-segid-hdr | (Optional) Vlan info segment id header |
| vlanshowinfo-seg-vlanid | (Optional) Vlan info VLAN ID |
| vlanshowinfo-segment-id | (Optional) Vlan info SEGMENT ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3087135990

---

# Command: show vlan name

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| name | VLAN status by VLAN name |
| vname | A vlan name with size 32 (128 if long vlan name enabled) |
| __readonly__ | (Optional) Read Only |
| TABLE_vlanbriefname | (Optional) VLAN brief table format |
| TABLE_mtuinfoname | (Optional) MTU information table format |
| vlanshowbr-hdr | (Optional) VLAN brief header |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanid-utf | (Optional) VLAN brief VLAN ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2055631708

---

# Command: show vlan private-vlan

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| id | (Optional) VLAN status by VLAN id |
| vlan-id | (Optional) VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |
| private-vlan | Private VLAN information |
| __readonly__ | (Optional) Read Only |
| TABLE_pvlan_primary | (Optional) Pvlan primary vlan table |
| vlan-key | (Optional) Vlan key |
| primary | (Optional) Primary VLAN |
| secondary | (Optional) Secondary VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1764146514

---

# Command: show vlan private-vlan type

## Syntax
```
show vlan [ id <vlan-id> ] private-vlan type [ __readonly__ [ { TABLE_pvlantype <vlan-num> <pvlan-type> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| id | (Optional) VLAN status by VLAN id |
| vlan-id | (Optional) VLAN ID 1-4094 or range(s): 1-5, 10 or 2-5,7-19 |
| private-vlan | Private VLAN information |
| type | Private VLAN type information |
| __readonly__ | (Optional) Read Only |
| TABLE_pvlantype | (Optional) Pvlan type table |
| vlan-num | (Optional) vlan |
| pvlan-type | (Optional) PVLAN Type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2066947937

---

# Command: show vlan xbrief

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| xbrief | All VLAN status in brief |
| controller | (Optional) Controller VLAN status |
| cli | (Optional) CLI VLAN status |
| __readonly__ | (Optional) Read Only |
| TABLE_vlanbriefxbrief | (Optional) VLAN brief table format |
| vlanshowbr-hdr | (Optional) VLAN brief header |
| vlanshowbr-vlanid | (Optional) VLAN brief VLAN ID |
| vlanshowbr-vlanid-utf | (Optional) VLAN brief VLAN ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3454226779

---

# Command: show vlan xsummary

## Syntax
```
show vlan xsummary [ __readonly__ <vlansum-all-vlan> <vlansum-vtp-vlan> <vlansum-ext-vlan> <vlansum-max-supported-vlan> <vlansum-carved-vlan>
 <show-end> [ <true-end> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vlan | VLAN status |
| xsummary | VLAN summary information |
| __readonly__ | (Optional) Read Only |
| vlansum-all-vlan | (Optional) Show vlan summary Total |
| vlansum-vtp-vlan | (Optional) Show vlan summary Number of normal vlans |
| vlansum-ext-vlan | (Optional) Show vlan summary Number of extended vlans |
| vlansum-max-supported-vlan | (Optional) Show vlan summary Max supported vlans |
| vlansum-carved-vlan | (Optional) Show vlan summary Number of carved sdn vlans |
| show-end | (Optional) Show vlan end marker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1223003805

---

# Command: show vmtracker

## Syntax
```
show vmtracker [ connection <conn_name> ] { { info { { [ interface <intf_id> ] { summary &#124; detail &#124; host &#124; vm &#124; port-group
 } } &#124; { vxlan-segment &#124; vxlan-vms } } } &#124; event-history } [ __readonly__ TABLE_info <intf_name> <host_or_ip> <vmnic> <vm_name>
 <vm_state> <port_group> <pg_type> <vlan_range> <virt_wire_name> <multicast_ip> <vdn_id> <vtep_ip> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| __readonly__ | (Optional) |
| TABLE_info | (Optional) |
| intf_name | (Optional) |
| host_or_ip | (Optional) |
| vmnic | (Optional) |
| vm_name | (Optional) |
| vm_state | (Optional) |
| port_group | (Optional) |
| pg_type | (Optional) |
| vlan_range | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2828232054

---

# Command: show vmtracker certificate

## Syntax
```
show vmtracker certificate [ __readonly__ TABLE_cert <certificate> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| __readonly__ | (Optional) |
| TABLE_cert | (Optional) |
| certificate | (Optional) |
| show | Show running system information |
| vmtracker | VMTRACKER commands |
| certificate | Show the default certificate used |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp9997331500

---

# Command: show vmtracker fabric auto-config

## Syntax
```
show vmtracker fabric auto-config [ interface <intf_id> ] [ vlan <vlan_id> ] [ status { success &#124; pending &#124; failure &#124; skipped
 } ] [ __readonly__ TABLE_autoconfig <interface_name> <port_group_name> <vlan_range> <config_status> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| __readonly__ | (Optional) |
| TABLE_autoconfig | (Optional) |
| interface_name | (Optional) |
| port_group_name | (Optional) |
| vlan_range | (Optional) |
| config_status | (Optional) |
| show | Show running system information |
| vmtracker | VMTRACKER commands |
| fabric | VM Tracker Fabric paramters |
| auto-config | VM Tracker Fabric AutoConfiguration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3786662831

---

# Command: show vmtracker status

## Syntax
```
show vmtracker [ connection <conn_name> ] status [ __readonly__ { TABLE_connection <name> <host_or_ip> <conn_status> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| __readonly__ | (Optional) |
| TABLE_connection | (Optional) |
| name | (Optional) |
| host_or_ip | (Optional) |
| conn_status | (Optional) |
| show | Show running system information |
| vmtracker | Show vmtracker info |
| connection | (Optional) Show vmtracker configured connections |
| conn_name | (Optional) Show vmtracker Connection name |
| status | Show vmtracker connection status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp5101203210

---

# Command: show vpc

## Syntax
```
show vpc [ brief ] [ __readonly__ <vpc-domain-id> [ <vpc-l2mp-switch-id> ] <vpc-peer-status> <vpc-peer-status-reason> <vpc-peer-keepalive-status>
 [ <vpc-peer-l2mp-status> ] <vpc-peer-consistency> { [ <vpc-peer-consistency-reason> ] [ <vpc-per-vlan-peer-consistency> ]
 <vpc-peer-consistency-status> } <vpc-type-2-consistency> { [ <vpc-type-2-consistency-reason> ] <vpc-type-2-consistency-status>
 } <vpc-role> <num-of-vpcs> [ <track-obj> ] [ <peer-gateway> ] [ <peer-gateway-excluded-vlans> ] <dual-active-excluded-vlans>
 <vpc-graceful-consistency-check-status> [ <vpc-auto-recovery-status> ] [ <vpc-delay-restore-status> ] [ <vpc-delay-restore-svi-status>
 ] [ <vpc-delay-peer-link-status> ] <operational-l3-peer> [ <vpc-scale-high-status> ] [ <fp-enhanced-load-balancing> ] [ <vpc-per-vlan-peer-consistency>
 ] [ <virtual-peerlink> ] [ <vpc-peer-link-hdr> [ { TABLE_peerlink <peer-link-id> <peerlink-ifindex> <peer-link-port-state>
 <peer-up-vlan-bitset> } ] <vpc-end> ] [ <vpc-hdr> [ <vpc-is-es> ] [ <vpc-not-es> ] [ { TABLE_vpc <vpc-id> <vpc-ifindex> <vpc-port-state>
 <phy-port-if-removed><vpc-thru-peerlink> <vpc-consistency> { [ <vpc-consistency-reason> ] [ <vpc-consistency-status> ] } <up-vlan-bitset>
 <es-attr> } ] <vpc-end> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| brief | (Optional) Brief display of vPC status |
| __readonly__ | (Optional) Read Only |
| TABLE_peerlink | (Optional) vPC peerlink table |
| TABLE_vpc | (Optional) vPC table |
| vpc-domain-id | (Optional) vPC domain id |
| vpc-l2mp-switch-id | (Optional) vPC+ switch ID |
| vpc-peer-status | (Optional) vPC peer status |
| vpc-peer-status-reason | (Optional) vPC peer status reason |
| vpc-peer-keepalive-status | (Optional) vpc peer keepalive status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp2283616677

---

# Command: show vpc

## Syntax
```
show vpc { <vpc-number> &#124; brief vpc <vpc-number> } [ __readonly__ [ <vpc-hdr> ] [ <vpc-is-es> ] [ <vpc-not-es> ] [ TABLE_vpc
 <vpc-id> <vpc-ifindex> <vpc-port-state> <phy-port-if-removed><vpc-thru-peerlink> <vpc-consistency> { [ <vpc-consistency-reason>
 ] [ <vpc-consistency-status> ] } <up-vlan-bitset> <es-attr> ] <vpc-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| brief | Brief display of vPC status |
| vpc-number | Enter a Virtual Port Channel number |
| __readonly__ | (Optional) Read Only |
| vpc-hdr | (Optional) Start of vPC table |
| vpc-is-es | (Optional) Flag to indicate vPC+ complex |
| vpc-not-es | (Optional) Flag to indicate vPC complex |
| TABLE_vpc | (Optional) vPC table |
| vpc-id | (Optional) vPC id |
| vpc-ifindex | (Optional) vPC ifindex |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp1487390324

---

# Command: show vpc consistency-parameters

## Syntax
```
show vpc consistency-parameters { global &#124; vni &#124; interface <if> &#124; vpc <vpc-num> } [ __readonly__ TABLE_vpc_consistency <vpc-param-name>
 <vpc-param-type> <vpc-param-local-val> <vpc-param-peer-val> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| consistency-parameters | Show vPC Consistency Parameters |
| global | Global Parameters |
| vni | Show vPC Consistency Parameters vni |
| vpc-num | Enter a Virtual Port Channel number |
| __readonly__ | (Optional) Read Only |
| TABLE_vpc_consistency | (Optional) vPC table |
| vpc-param-name | (Optional) |
| vpc-param-type | (Optional) |
| vpc-param-local-val | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp3547109403

---

# Command: show vpc consistency-parameters vlans

## Syntax
```
show vpc consistency-parameters vlans [ vnseg ] [ __readonly__ TABLE_vpc_consistency <vpc-param-name> <vpc-param-type> [ <reason_code>
 ] [ <syserr> ] <vpc-pass-vlans> [ <reason_code> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| consistency-parameters | Show vPC Consistency Parameters |
| vlans | vlans |
| vnseg | (Optional) Display vlan to vn-segment map |
| __readonly__ | (Optional) Read Only |
| TABLE_vpc_consistency | (Optional) vPC table |
| vpc-param-name | (Optional) |
| vpc-param-type | (Optional) |
| vpc-pass-vlans | (Optional) |
| syserr | (Optional) vPC consistency reason |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, vpc, S-commands
**Command ID:** wp4254208832

---

# Command: show vpc fabric-ports

## Syntax
```
show vpc fabric-ports [ __readonly__ [ { TABLE_fabric_ports <vpc-fabric-ports> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| fabric-ports | Show ports that are part of uplink virtual-peerlink |
| __readonly__ | (Optional) Read Only |
| TABLE_fabric_ports | (Optional) vPC fabric ports table |
| vpc-fabric-ports | (Optional) description of the port |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, vpc, S-commands
**Command ID:** wp8868514910

---

# Command: show vpc orphan-ports

## Syntax
```
show vpc orphan-ports [ __readonly__ [ { TABLE_orphan_ports <vpc-vlan> <vpc-orphan-ports> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| orphan-ports | Show ports that are not part of vPC but have common VLANs |
| __readonly__ | (Optional) Read Only |
| TABLE_orphan_ports | (Optional) vPC orphan ports table |
| vpc-vlan | (Optional) port vlan |
| vpc-orphan-ports | (Optional) description of the port |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, vpc, S-commands
**Command ID:** wp3531922018

---

# Command: show vpc peer-keepalive

## Syntax
```
show vpc peer-keepalive [ __readonly__ <vpc-peer-keepalive-status> <vpc-keepalive-dest> <vpc-keepalive-send-interface> <vpc-keepalive-receive-interface>
 <vpc-keepalive-send-tstamp> <vpc-keepalive-receive-tstamp> <vpc-peer-keepalive-up-time> <vpc-keepalive-send-status> <vpc-keepalive-receive-status>
 <vpc-keepalive-lastupdate> [ <vpc-keepalive-dest> ] <vpc-keepalive-interval> <vpc-keepalive-timeout> <vpc-keepalive-hold-timeout>
 <vpc-keepalive-vrf> <vpc-keepalive-udp-port> <vpc-keepalive-tos> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| peer-keepalive | vPC keepalive status |
| __readonly__ | (Optional) Read Only |
| vpc-peer-keepalive-status | (Optional) vpc peer keepalive status |
| vpc-keepalive-dest | (Optional) vPC keepalive destination ip address |
| vpc-keepalive-send-status | (Optional) vPC keepalive send status |
| vpc-keepalive-receive-status | (Optional) vPC keepalive receive status |
| vpc-peer-keepalive-up-time | (Optional) keepalive- alive time |
| vpc-keepalive-send-tstamp | (Optional) vPC keepalive last send timestamp |
| vpc-keepalive-send-interface | (Optional) vPC keepalive send interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp2992053601

---

# Command: show vpc role

## Syntax
```
show vpc role [ __readonly__ <vpc-peer-status> <vpc-peer-status-reason> [ <vpc-current-role> ] [ <vpc-es-current-role> ] <dual-active-detected>
 <vpc-system-mac> <vpc-system-prio> <vpc-local-system-mac> <vpc-local-system-prio><vpc-local-role-prio> <vpc-peer-system-mac>
 <vpc-peer-system-prio><vpc-peer-role-prio> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| role | vPC role status |
| __readonly__ | (Optional) Read Only |
| vpc-peer-status | (Optional) vPC peer status |
| vpc-peer-status-reason | (Optional) vPC peer status reason |
| vpc-current-role | (Optional) vPC role |
| vpc-es-current-role | (Optional) vPC role |
| dual-active-detected | (Optional) Dual active detection status |
| vpc-system-mac | (Optional) vPC system mac |
| vpc-local-system-mac | (Optional) vPC local system mac |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp8775110540

---

# Command: show vpc statistics peer-keepalive

## Syntax
```
show vpc statistics peer-keepalive [ __readonly__ <vpc-peer-keepalive-status> <vpc-keepalive-counters-tx> <vpc-keepalive-counters-rx>
 <vpc-keepalive-avg-rx-interval> <vpc-keepalive-peer-state-changes> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| statistics | Statistics |
| peer-keepalive | peer keepalive module related statistics |
| __readonly__ | (Optional) Read Only |
| vpc-peer-keepalive-status | (Optional) vpc peer keepalive status |
| vpc-keepalive-counters-tx | (Optional) tx counters |
| vpc-keepalive-counters-rx | (Optional) rx counters |
| vpc-keepalive-avg-rx-interval | (Optional) avg rx interval in ms |
| vpc-keepalive-peer-state-changes | (Optional) peer state changes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp2701775803

---

# Command: show vpc statistics vpc

## Syntax
```
show vpc statistics { vpc <vpc_num> &#124; peer-link }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vpc | Virtual Port Channel configuration |
| statistics | Statistics |
| vpc_num | Virtual Port Channel number |
| peer-link | stats for peer-link |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp3574784829

---

# Command: show vpc virtual-peerlink dest reachable

## Syntax
```
show vpc virtual-peerlink dest reachable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vpc | vPC related information |
| virtual-peerlink | virtual-peerlink Related show commands |
| dest | dest info |
| reachable | dest reachability |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, vpc, S-commands
**Command ID:** wp2392175827

---

# Command: show vpc virtual-peerlink vlan consistency

## Syntax
```
show vpc virtual-peerlink vlan consistency
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vpc | vPC related information |
| virtual-peerlink | virtual-peerlink Related show commands |
| vlan | vlan info for vPC |
| consistency | vlan vni consistency |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, vpc, S-commands
**Command ID:** wp3181931156

---

# Command: show vrf

## Syntax
```
show vrf [ <vrf-name> &#124; <vrf-known-name> &#124; all ] [ order id ] [ detail ] [ passive ] [ __readonly__ TABLE_vrf <vrf_name> <vrf_id>
 <vrf_state> [ <vrf_reason> ] [ <vrf_pend> ] [ <vpnid> <rd> [ <vni> ] <max_routes> <mid_threshold> ] [ { TABLE_tib <tib_id>
 <tib_af> <tib_nonce> <tib_state> [ <tib_reason> ] [ <tib_pend> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vrf | Display VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display VRF information for all VRFs |
| order | (Optional) Specify ordering |
| id | (Optional) Order by ID |
| detail | (Optional) Display VRF detail information |
| passive | (Optional) Display passive VRF information |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp7204833890

---

# Command: show vrf

## Syntax
```
show vrf [ <vrf-name> &#124; <vrf-known-name> &#124; all ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vrf | Display VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display VRF information for all VRFs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3436775871

---

# Command: show vrrp

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vrrp | Show vrrp information |
| summary | (Optional) Show vrrp summary |
| statistics | (Optional) Show vrrp statistics |
| detail | (Optional) Show detailed information |
| interface | (Optional) Show vrrp info for the interface |
| interface_id | (Optional) |
| vr | (Optional) Show vrrp info for the group |
| vr_id | (Optional) [1-255] enter IPv4 vr group |
| master | (Optional) Groups in Master state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1553981713

---

# Command: show vrrp bfd-sessions

## Syntax
```
show vrrp bfd-sessions [ interface <interface-id> [ to <ipaddress> ] ] [ __readonly__ TABLE_bfd_sess <interface> { <src_addr>
 &#124; <src_addr_v6> } { <dst_addr> &#124; <dst_addr_v6> } <session_state> <ref_count> <displayed_interface> { TABLE_groups <group_id>
 <vrrp_state> <bfd_status> <operation> <time> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vrrp | Show vrrp information |
| bfd-sessions | BFD sessions |
| interface | (Optional) Groups on this interface |
| interface-id | (Optional) Interface |
| to | (Optional) To IP address |
| ipaddress | (Optional) Sessions to IP address |
| __readonly__ | (Optional) |
| TABLE_bfd_sess | (Optional) |
| interface | (Optional) Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp1934677861

---

# Command: show vrrpv3

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vrrpv3 | VRRPv3 Show commands |
| all | (Optional) All VRRPV3 information |
| brief | (Optional) Brief output |
| detail | (Optional) Detail output |
| statistics | (Optional) Statistics output |
| opt_v4_or_v6 | (Optional) Enter ipv4 or ipv6 |
| intf | (Optional) Interface |
| group_num | (Optional) Group Number |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp5105492370

---

# Command: show vrrs client

## Syntax
```
show vrrs client [ <cname> ] [ __readonly__ { TABLE_client <name> <id> <all> <priority> { TABLE_tags <tname> } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrs | VRRS Show commands |
| show | Show running system information |
| client | Information about VRRS clients |
| cname | (Optional) VRRS client name |
| __readonly__ | (Optional) |
| TABLE_client | (Optional) VRRS clients |
| TABLE_tags | (Optional) VRRS tags |
| name | (Optional) VRRS client name |
| id | (Optional) VRRS client id |
| priority | (Optional) Priority |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1133094103

---

# Command: show vrrs pathway

## Syntax
```
show vrrs pathway [ <intf> ] [ __readonly__ { TABLE_pws <name> <state> <vrrs_push_state> <vmac> <vmac_state> <vmac_dbg> [
 <pvmac> ] [ <pvmac_state> ] [ <pvmac_dbg> ] <af> [ <desc> ] <opt> <eval> [ { TABLE_vips <addr> [ <flags> ] } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrs | VRRS Show commands |
| show | Show running system information |
| pathway | Information about VRRS pathways |
| intf | (Optional) Interface |
| __readonly__ | (Optional) |
| TABLE_pws | (Optional) Show VRRS pathways |
| TABLE_vips | (Optional) Pathway vIP addresses |
| name | (Optional) Pathway name |
| state | (Optional) Pathway state |
| vrrs_push_state | (Optional) VRRS push state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2167474050

---

# Command: show vrrs pathway address

## Syntax
```
show vrrs pathway [ <intf> ] address
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrs | VRRS Show commands |
| show | Show running system information |
| pathway | Information about VRRS pathways |
| intf | (Optional) Interface |
| address | Internal information about pathway addresses |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1176705955

---

# Command: show vrrs server

## Syntax
```
show vrrs server [ __readonly__ { TABLE_srv <name> <af> <intf> <state> <vmac> <vip> [ { TABLE_tag <tag> } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrs | VRRS Show commands |
| show | Show running system information |
| server | Information about VRRS servers |
| __readonly__ | (Optional) |
| TABLE_srv | (Optional) VRRS Servers |
| TABLE_tag | (Optional) VRRS tags associated with each server |
| name | (Optional) VRRS server name |
| af | (Optional) Address-family |
| intf | (Optional) Interface |
| state | (Optional) VRRS server state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp8337997790

---

# Command: show vrrs tag

## Syntax
```
show vrrs tag [ <tagname> ] [ __readonly__ { TABLE_tag <name> <server> [ { TABLE_client <id> <client> <all> } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vrrs | VRRS Show commands |
| show | Show running system information |
| tag | Information about VRRS tags |
| tagname | (Optional) VRRS tag |
| __readonly__ | (Optional) |
| TABLE_tag | (Optional) Known VRRS tags |
| TABLE_client | (Optional) VRRS clients listening |
| name | (Optional) VRRS tag name |
| server | (Optional) VRRS server name |
| id | (Optional) VRRS client id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3637755987

---

# Command: show vsan

## Syntax
```
show vsan [ <id_in> ] [ __readonly__ { TABLE_vsan <id> { [ <name> <state> <interop_mode> <load_balancing> <operational_state>
 ] &#124; <inactive_vsan_name> &#124; <evfp_control_vsan_name> } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vsan | Vsan commands |
| id_in | (Optional) VSAN ID range |
| __readonly__ | (Optional) Read Only |
| TABLE_vsan | (Optional) Table of VSAN's |
| id | (Optional) VSAN ID |
| name | (Optional) VSAN name |
| state | (Optional) VSAN state |
| interop_mode | (Optional) Interoperability mode |
| load_balancing | (Optional) Load balancing |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3113798612

---

# Command: show vsan membership

## Syntax
```
show vsan [ <id_in> ] membership [ __readonly__ { TABLE_vsan <id> [ <inactive_vsan_name> ] [ <evfp_control_vsan_name> ] [
 TABLE_interface <name> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vsan | Vsan commands |
| id_in | (Optional) VSAN ID range |
| membership | VSAN membership information |
| __readonly__ | (Optional) Read Only |
| TABLE_vsan | (Optional) VSAN table |
| id | (Optional) VSAN ID |
| inactive_vsan_name | (Optional) Isolated VSAN |
| evfp_control_vsan_name | (Optional) EVFP isolated VSAN |
| TABLE_interface | (Optional) List of interface members |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp1652786599

---

# Command: show vsan membership interface

## Syntax
```
show vsan membership interface <if_in> [ __readonly__ { TABLE_interface <name> <vsan_id_memb> [ <inactive_vsan_name> &#124; <evfp_control_vsan_name>
 ] <allowed_vsan_list> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vsan | Vsan commands |
| membership | VSAN membership information |
| interface | Show interface status and information |
| if_in | Interface range |
| __readonly__ | (Optional) Read Only |
| TABLE_interface | (Optional) Interface VSAN table |
| name | (Optional) Interface Name |
| vsan_id_memb | (Optional) VSAN ID to which interface belongs |
| inactive_vsan_name | (Optional) Isolated VSAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, network, S-commands
**Command ID:** wp1268054789

---

# Command: show vsan usage

## Syntax
```
show vsan usage [ __readonly__ { <num_vsans_configured> <configured_range_of_vsans> <vsans_available_to_configure> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vsan | Vsan commands |
| usage | show VSAN usage in the system |
| __readonly__ | (Optional) Read Only |
| num_vsans_configured | (Optional) Total VSAN's configured |
| configured_range_of_vsans | (Optional) Range of VSAN's configured |
| vsans_available_to_configure | (Optional) VSAN range available to configure |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2021723672

---

# Command: show vtp counters

## Syntax
```
show vtp counters [ __readonly__ <start> <summary_rx> <subset_rx> <request_rx> <summary_tx> <subset_tx> <request_tx> <num_config_rev_error>
 <num_config_digest_error> <num_v1_summary_error> [ { TABLE_pruning_counters <if_index> <join_tx> <join_rx> <summary_adv_v1_rx>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vtp | VTP information |
| counters | VTP statistics |
| __readonly__ | (Optional) Read Only |
| start | (Optional) Start |
| summary_rx | (Optional) Summary advertisements received |
| subset_rx | (Optional) Subset advertisements received |
| request_rx | (Optional) Request advertisements received |
| summary_tx | (Optional) Summary advertisements transmitted |
| subset_tx | (Optional) Subset advertisements transmitted |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3740597793

---

# Command: show vtp interface

## Syntax
```
show vtp interface [ <interface_range> ] [ __readonly__ [ <start> ] { TABLE_vtp_interface <if_index> <status> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vtp | VTP information |
| interface | VTP interface status and configuration |
| interface_range | (Optional) Enter interfaces |
| __readonly__ | (Optional) Read Only |
| start | (Optional) Start |
| TABLE_vtp_interface | (Optional) VTP interface configuration in table format |
| if_index | (Optional) Trunk |
| status | (Optional) VTP interface status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4264424171

---

# Command: show vtp password

## Syntax
```
show vtp password [ domain <domain-id> ] [ __readonly__ <start> <passwd> <password-type> <secret-key> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vtp | VTP information |
| password | VTP password |
| domain | (Optional) VTP administrative domain |
| domain-id | (Optional) Domian index(Domain-id) |
| __readonly__ | (Optional) Read Only |
| start | (Optional) Start |
| passwd | (Optional) VTP Domain Password |
| password-type | (Optional) Password Type (1=plaintxt, 2=hidden) |
| secret-key | (Optional) Secret Key for the password |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1446840563

---

# Command: show vtp status

## Syntax
```
show vtp status [ __readonly__ <start> <version> <config_rev> <max_vlan_supported_local> <num_current_vlans> <oper_mode> <domain_name>
 <pruning_mode> <oper_pruning_mode> <v2_mode> <trap_enabled> <md5_digest> <last_modified_ip> <last_modified_time> <running-version>
 <updater_id> <updater_reason> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| vtp | VTP information |
| status | VTP domain status |
| __readonly__ | (Optional) Read Only |
| start | (Optional) Start |
| version | (Optional) VTP version |
| config_rev | (Optional) Configuration Revision |
| max_vlan_supported_local | (Optional) Maximum VLANs supported locally |
| num_current_vlans | (Optional) Number of existing VLANs |
| oper_mode | (Optional) VTP Mode |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3382702241

---

