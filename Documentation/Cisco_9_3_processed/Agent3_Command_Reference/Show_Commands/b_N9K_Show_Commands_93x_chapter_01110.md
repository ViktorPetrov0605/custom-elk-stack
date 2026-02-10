# Chapter: O Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01110.html
**Type:** Show Commands  
**Chapter:** Group-1110 Commands  
**Total Commands:** 28

## Command List

- `show object-group`
- `show openflow hardware capabilities`
- `show openflow switch`
- `show openflow switch flows`
- `show ospfv3`
- `show ospfv3 border-routers`
- `show ospfv3 database`
- `show ospfv3 database database-summary`
- `show ospfv3 database detail`
- `show ospfv3 event-history`
- `show ospfv3 event-history detail`
- `show ospfv3 interface`
- `show ospfv3 interface brief`
- `show ospfv3 memory`
- `show ospfv3 neighbors`
- `show ospfv3 neighbors detail`
- `show ospfv3 neighbors summary`
- `show ospfv3 policy statistics`
- `show ospfv3 request-list`
- `show ospfv3 retransmission-list`
- `show ospfv3 route`
- `show ospfv3 route summary`
- `show ospfv3 statistics`
- `show ospfv3 summary-address`
- `show ospfv3 traffic`
- `show ospfv3 virtual-links`
- `show ospfv3 virtual-links brief`
- `show otv`

---

## Detailed Command Reference

# Command: show object-group

## Syntax
```
show object-group [ <name> ] [ __readonly__ TABLE_ogroup <group_type> <group_name> [ TABLE_seqno <seqno> { <_port_op> <port0_num>
 &#124; <_port_range> <port1_num> <port2_num> &#124; <hostaddr> &#124; <net_ip> &#124; <mask_ip_addr> <mask_ip_mask> &#124; <hostipv6> &#124; <net_ipv6>
 &#124; <mask_ipv6_addr> <mask_ipv6_mask> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| object-group | Show configured ACL object groups |
| name | (Optional) object-group name |
| __readonly__ | (Optional) |
| group_type | (Optional) Object group type |
| group_name | (Optional) Object group name |
| seqno | (Optional) Sequence number |
| TABLE_ogroup | (Optional) |
| TABLE_seqno | (Optional) |
| _port_op | (Optional) Port operator |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1753531604

---

# Command: show openflow hardware capabilities

## Syntax
```
show openflow hardware capabilities [ pipeline <pipeline-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| openflow | Show OpenFlow information |
| hardware | Hardware |
| capabilities | Capabilities |
| pipeline | (Optional) Pipeline id |
| pipeline-id | (Optional) Pipeline id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2101800036

---

# Command: show openflow switch

## Syntax
```
show openflow switch <switch-id> [ { controllers [ stats &#124; { role { master &#124; slave &#124; equal } } ] &#124; ports } ] [ __readonly__
 <cli_output> <ctrlv4> <ctrlport> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| openflow | Show OpenFlow information |
| switch | Logical switch id |
| switch-id | Logical switch-id to enter |
| controllers | (Optional) Controllers |
| stats | (Optional) Stats |
| ports | (Optional) Ports |
| role | (Optional) Controller role |
| master | (Optional) Master |
| slave | (Optional) Slave |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2613431198

---

# Command: show openflow switch flows

## Syntax
```
show openflow switch <switch-id> flows [ [ table-id <table-id> ] [ [ pending &#124; pending-del &#124; controller &#124; configured &#124; default
 &#124; fixed ] [ brief &#124; list &#124; summary ] ] &#124; stats &#124; compare statistics { snapshot &#124; report [ brief &#124; list ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| openflow | Show OpenFlow information |
| switch | Logical switch id |
| switch-id | Logical switch-id to enter |
| flows | Flows |
| brief | (Optional) Brief |
| summary | (Optional) Summary |
| pending | (Optional) Pending |
| pending-del | (Optional) Pending delete |
| controller | (Optional) Controller |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3909818443

---

# Command: show ospfv3

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <instance_number>
 <cname> <rid> <stateful_ha> <gr_ha> [ [ <gr_planned_only> ] [ <gr_grace_period> ] [ <gr_state> ] [ <gr_last_status> ] ] [
 <gr_helper_mode> ] <support_tos0_only> <support_opaque_lsa> [ <low_mem_cond> ] <is_abr> <is_asbr> [ <max_lsa_non_self_number>
 ] [ <max_lsa_state> ] [ <max_lsa_warning_only> ] [ <max_lsa_current_non_self_lsa_number> ] [ <max_lsa_threshold_pct> ] [ <max_lsa_ignore_time>
 ] [ <max_lsa_reset_time> ] [ <max_lsa_ignore_count> ] [ <max_lsa_current_ignore_count> ] [ <max_lsa_ignore_time_left> ] [
 <max_lsa_reset_time_left> ] [ <max_lsa_permanent_ignore> ] [ { TABLE_redist <proto> [ <max_lsas> ] [ <warning> ] [ <threshold>
 ] [ <current_count> ] } ] <admin_dist> <ref_bw> <spf_start_time> <spf_hold_time> <spf_max_time> <lsa_start_time> <lsa_hold_time>
 <lsa_max_time> <min_lsa_arr_time> <lsa_aging_pace> <spf_max_paths> <max_metric_adver> [ [ <max_metric_time_left> ] [ <max_metric_wait_bgp>
 ] [ <max_metric_timeout> ] [ <max_metric_always> ] [ <max_metric_sum_lsa> ] [ <max_metric_ext_lsa> ] ] <asext_lsa_cnt> <asext_lsa_crc>
 <area_total> <area_normal> <area_stub> <area_nssa> <act_area_total> <act_area_normal> <act_area_stub> <act_area_nssa> [ <name_lookup>
 ] <no_discard_rt_ext> <no_discard_rt_int> [ <passive_dflt> ] [ <bfd_enabled> ] [ <ipsec_sa_type> ] [ <ipsec_sa_algorithm>
 ] [ <ipsec_sa_spi> ] [ { TABLE_area <aname> [ <backbone_active> ] [ <active> ] <age> <total_intf> <act_intf> <passive_intf>
 <loopback_intf> [ <gr_nbr_cnt> ] <stub> [ <stub_def_cost> ] <nssa> [ <no_redist> ] [ <nssa_trans> ] <no_summary> [ <ipsec_sa_type>
 ] [ <ipsec_sa_algorithm> ] [ <ipsec_sa_spi> ] <spf_runs> <last_spf_run_time> [ TABLE_range <addr> <masklen> <state> <nets>
 <advertise> [ <cost> ] ] [ <filter_in> ] [ <filter_out> ] <lsa_cnt> <lsa_crc> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| __readonly__ | (Optional) |
| TABLE_ctx | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2628502072

---

# Command: show ospfv3 border-routers

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] border-routers [ all_routes ] [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> [ TABLE_br <type> <addr> <cost> <asbr> <abr> <area> <spf_inst>
 [ <vlink_unresolved> ] [ TABLE_br_ubest_nh [ <ubest_nh_addr> ] [ <ubest_nh_intf> ] ] [ TABLE_br_mbest_nh [ <mbest_nh_addr>
 ] [ <mbest_nh_intf> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| border-routers | Border routers |
| all_routes | (Optional) Display all OSPFv3 routes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2950622538

---

# Command: show ospfv3 database

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] database [ [ [ [ router &#124; network &#124; intra-area-prefix
 &#124; inter-area { irouter &#124; iprefix } &#124; nssa-external &#124; area-unknown &#124; [ [ { link &#124; link-unknown &#124; grace } [ <interface> ] ]
 ] ] [ area <area-id-ip> ] ] &#124; external [ tag <tag_val> ] &#124; as-unknown ] [ <lsid> ] [ self-originated &#124; adv-router <advid>
 &#124; adv-router-name <adv-name> ] ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <rid> <ptag> <cname>
 [ TABLE_db3_lsa [ <name> ] [ <area> ] [ <id> ] [ <advrtr> ] [ <age> ] [ <seqno> ] [ <corrupt> ] [ <rtr_num_links> ] [ <net_num_rtr>
 ] [ <prefix> ] [ <inter_rid> ] [ <link_if> ] [ <intra_ref_type> ] [ <intra_ref_lsid> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| database | Link-state Database Summary |
| router | (Optional) Display router LSAs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2408733182

---

# Command: show ospfv3 database database-summary

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] database database-summary [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <rid> <ptag> <cname> [ TABLE_dbsum [ TABLE_dbsum_area <area> [ TABLE_dbsum_area_lsa
 <area_lsa_name> <area_lsa_count> ] <area_lsa_total> ] [ TABLE_dbsum_all [ TABLE_dbsum_lsa_all <lsa_name> <lsa_count> ] <non_self_lsa_total>
 <lsa_total> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| database | Link-state Database Summary |
| database-summary | Summary of database |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1931736162

---

# Command: show ospfv3 database detail

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] database [ [ [ router &#124; network &#124; intra-area-prefix
 &#124; inter-area { irouter &#124; iprefix } &#124; nssa-external &#124; area-unknown &#124; [ [ { link &#124; link-unknown &#124; grace } [ <interface> ] ]
 ] ] [ area <area-id-ip> ] ] &#124; external [ tag <tag_val> ] &#124; as-unknown ] [ <lsid> ] [ self-originated &#124; adv-router <advid>
 &#124; adv-router-name <adv-name> ] detail [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <rid> <ptag>
 <cname> [ TABLE_db3_lsa [ <name> ] [ <area> ] [ TABLE_lsdb <age> <maxage> <wrapping> <dummy> <flush_pending> <type> [ <intf>
 ] <id> <advrtr> <seqno> <cksum> <len> [ <corrupt> ] [ <rtr_abr> ] [ <rtr_asbr> ] [ <rtr_translate> ] [ <rtr_vlink_end> ] [
 <rtr_options> ] [ <rtr_num_links> ] [ TABLE_rlsa [ <rtr_link_type> ] [ <rtr_link_metric> ] [ <rtr_link_ifid> ] [ <rtr_link_nbr_ifid>
 ] [ <rtr_link_nbr_rid> ] ] [ <net_options> ] [ TABLE_nlsa [ <net_rtr> ] ] [ <ia_prefix> ] [ <ia_prefix_options> ] [ <ia_prefix_metric>
 ] [ <ia_rtr_options> ] [ <ia_rtr_metric> ] [ <ia_rtr_rid> ] [ <asext_prefix> ] [ <asext_options> ] [ <asext_metric_type2>
 ] [ <asext_metric> ] [ <asext_fwd_addr> ] [ <asext_tag> ] [ <asext_ref_lstype> ] [ <asext_ref_lsid> ] [ <link_priority> ]
 [ <link_options> ] [ <link_laddr> ] [ <link_num_prefix> ] [ TABLE_linklsa [ <link_prefix> ] [ <link_prefix_options> ] ] [
 <intra_num_prefix> ] [ <intra_ref_lstype> ] [ <intra_ref_lsid> ] [ <intra_ref_advrtr> ] [ TABLE_iaplsa [ <intra_prefix> ]
 [ <intra_prefix_options> ] [ <intra_prefix_metric> ] [ <corrupted_length> ] ] [ <tlv_type> ] [ <tlv_len> ] [ <tlv_data> ]
 [ <tlv_unknown> ] [ <gr_interval> ] [ <gr_reason> ] [ <unknown> ] [ <data_len> ] [ <data> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| database | Link-state Database Summary |
| router | (Optional) Display router LSAs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1414679686

---

# Command: show ospfv3 event-history

## Syntax
```
show ospfv3 [ <tag> ] [ internal ] event-history { errors &#124; msgs &#124; statistics &#124; adjacency &#124; event &#124; ha &#124; flooding &#124; lsa &#124;
 spf &#124; redistribution &#124; hello &#124; spf-trigger &#124; cli &#124; rib }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| internal | (Optional) Commands for internal use |
| event-history | Show various event logs of OSPF |
| errors | Error logs |
| msgs | IPC logs |
| statistics | Show the state and size of the buffers |
| adjacency | Adjacency formation logs |
| event | Internal event logs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3680090540

---

# Command: show ospfv3 event-history detail

## Syntax
```
show ospfv3 [ <tag> ] [ internal ] event-history detail [ statistics ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| internal | (Optional) Commands for internal use |
| event-history | Show event history of OSPF |
| detail | Show detailed event history information |
| statistics | (Optional) Show the state and size of the verbose history buffer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3828038068

---

# Command: show ospfv3 interface

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] interface [ <interface> &#124; vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; all } ] [ private ] [ __readonly__ TABLE_ctx <ptag> <cname> [ TABLE_intf <ifname> <admin_status> <proto_status>
 <addr> [ <masklen> ] [ <inst_id> ] <area> [ <if_cfg> ] <state_str> <type_str> <cost> [ <ipsec_sa_type> ] [ <ipsec_sa_algorithm>
 ] [ <ipsec_sa_spi> ] [ <bfd_enabled> ] <index> [ <passive> ] [ <mpls> ] [ <transmit_delay> ] [ <if_priority> ] [ <dr_rid>
 ] [ <dr_addr> ] [ <bdr_rid> ] [ <bdr_addr> ] [ <nbr_total> ] [ <nbr_flood> ] [ <nbr_adjs> ] [ <gr_nbr> ] [ <hello_interval>
 ] [ <dead_interval> ] [ <wait_interval> ] [ <rxmt_interval> ] [ <hello_timer> ] [ <wait_timer> ] [ <lsu_timer> ] [ <lsack_timer>
 ] [ <link_lsa_cnt> ] [ <link_lsa_crc> ] [ <multi_area_cnt> ] [ <multi_area_adj> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| interface | OSPF enabled interface |
| interface | (Optional) OSPF enabled interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, interface, routing, S-commands
**Command ID:** wp3201140831

---

# Command: show ospfv3 interface brief

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] interface brief [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> <intf_count> TABLE_intf <ifname> <index> <area> <cost> <state_str> <nbr_total>
 <admin_status> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| interface | OSPF enabled interface |
| brief | Display summary of OSPFv3 interfaces |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, interface, routing, S-commands
**Command ID:** wp2340061164

---

# Command: show ospfv3 memory

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] memory [ __readonly__ TABLE_mem <ptag> <byte_total> <byte_consumed> <byte_overhead> <byte_allocated>
 <alloc_current> <alloc_created> <alloc_failed> <alloc_free> <bf_current> <bf_created> <bf_failed> <bf_free> <bf_byte_consumed>
 <bf_32_current> <bf_32_created> <bf_32_failed> <bf_32_free> <bf_32_byte_consumed> <slab_current> <slab_created> <slab_failed>
 <slab_free> <slab_byte_consumed> <if_index_alloc_failed> <nbr_index_alloc_failed> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| memory | Memory usage statistics |
| __readonly__ | (Optional) |
| TABLE_mem | (Optional) |
| ptag | (Optional) |
| byte_total | (Optional) |
| byte_consumed | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1960341743

---

# Command: show ospfv3 neighbors

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] neighbors [ { { <interface> [ <neighbor> &#124;
 <neighbor-name> ] } &#124; { [ <neighbor> &#124; <neighbor-name> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] } } ] [ __readonly__
 TABLE_ctx <ptag> <cname> <nbrcount> [ TABLE_nbr <rid> <priority> <state> <drstate> <uptime> <ifid> <intf> [ <multiarea> ]
 <addr> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| neighbors | Neighbor list |
| interface | (Optional) OSPF enabled interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3739819692

---

# Command: show ospfv3 neighbors detail

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] neighbors [ <interface> ] [ <neighbor> ] detail
 [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ private ] [ __readonly__ TABLE_ctx <ptag> <cname> [ TABLE_nbr <rid> <addr>
 <area> <intf> <state> <transition> <lastchange> [ <bfd_state> ] [ <priority> ] [ <ifid> ] [ <dr> ] [ <bdr> ] [ <master> ]
 [ <seqno> ] [ <dbdallsentacked> ] [ <dbdallsent> ] [ <dbdallacked> ] [ <lsaonreqlist> ] [ <lsafromlastreq> ] [ <lsreqrxmts>
 ] <helloptions> <dbdoptions> <lastnonhello> [ <deadtimer> ] [ <pacingtimer> ] [ <dbdrxmtimer> ] [ <reqrxmtimer> ] [ <lsutimer>
 ] [ <rerxmtimer> ] [ <fastrerxmtimer> ] [ <lsacktimer> ] [ <grtimer> ] [ <helpermode> ] [ <helpercand> ] [ <helperterm> ]
 [ <senddbd> ] [ <sendlsreq> ] [ <sendlsu> ] [ <sendlsurxmt> ] [ <sendlsack> ] [ <sendlsreqreply> ] [ <sradjsid> ] [ <sradjflags>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| neighbors | Neighbor list |
| interface | (Optional) OSPF enabled interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp6274387400

---

# Command: show ospfv3 neighbors summary

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] neighbors [ <interface> ] summary [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> TABLE_intf { <ifname> &#124; <total> } <down> <attempt> <init>
 <twoway> <exstart> <exchange> <loading> <full> <if_total> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| neighbors | Neighbor list |
| interface | (Optional) OSPF enabled interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3765008037

---

# Command: show ospfv3 policy statistics

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] policy statistics { { redistribute { bgp <as>
 &#124; { isis &#124; rip } <tag> &#124; static &#124; direct &#124; amt } } &#124; { area <area-id-ip> filter-list { in &#124; out } } } [ vrf { <vrf-name> &#124;
 <vrf-known-name> &#124; all } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| policy | Display Policy related information |
| statistics | Display Route Filter statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, qos, S-commands
**Command ID:** wp2427304361

---

# Command: show ospfv3 request-list

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] request-list { <ip-addr> &#124; <neighbor-name> } <interface> [ __readonly__ [ TABLE_ctx <ptag>
 <cname> [ TABLE_lsreq <nbr_rid> <intf> <nbr_addr> <total> [ TABLE_lsa [ <type> ] [ <lsid> ] [ <advrtr> ] [ <seqno> ] [ <cksum>
 ] [ <age> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| request-list | Link state request list |
| interface | OSPF enabled interface |
| ip-addr | Neighbor router ID |
| neighbor-name | DNS Name of the neighbor |
| __readonly__ | (Optional) |
| TABLE_ctx | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp6357389410

---

# Command: show ospfv3 retransmission-list

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] retransmission-list { <routerid> &#124; <router-name> } <interface> [ __readonly__ [ TABLE_ctx <ptag>
 <cname> [ TABLE_rxmit <nbr_rid> <intf> <nbr_addr> [ <timer_running> ] [ <timer_due> ] [ TABLE_lsa [ <type> ] [ <lsid> ] [
 <advrtr> ] [ <seqno> ] [ <cksum> ] [ <age> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| retransmission-list | Link state retransmission list |
| routerid | Neighbor router ID |
| router-name | DNS Name of the router |
| interface | OSPF enabled interface |
| __readonly__ | (Optional) |
| TABLE_ctx | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2354989000

---

# Command: show ospfv3 route

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] route [ <ipv6-prefix> [ longer-prefixes ] ]
 [ all_routes ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> [ <hdr_addr> ] [ <hdr_masklen>
 ] [ TABLE_route <addr> <masklen> <type> [ <in_ulib> ] <in_rib> <direct> [ <area> ] [ <tag> ] [ <vlink_unresolved> ] [ TABLE_route_ubest_nh
 [ <ubest_nh_addr> ] [ <ubest_nh_intf> ] [ <ubest_cost> ] [ <distance> ] [ <ubest_nh_direct> ] [ <ubest_nh_sham_link> ] [ <ubest_nh_te_tun>
 ] [ <ubest_nh_in_rib> ] ] [ TABLE_route_mbest_nh [ <mbest_nh_addr> ] [ <mbest_nh_intf> ] [ <mbest_cost> ] [ <mbest_nh_direct>
 ] [ <mbest_nh_in_rib> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| route | Internal OSPF routes |
| longer-prefixes | (Optional) Show exact match and more specific routes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3642216340

---

# Command: show ospfv3 route summary

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] route [ <ipv6-prefix> [ longer-prefixes ] ]
 summary [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> [ TABLE_route <total_routes>
 <total_paths> [ TABLE_route_type <path_type> <path_routes> <path_paths> ] [ TABLE_route_masklen <masklen> <masklen_routes>
 <masklen_paths> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| route | Internal OSPF routes |
| longer-prefixes | (Optional) Show exact match and more specific routes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2263383338

---

# Command: show ospfv3 statistics

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] statistics [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; all } ] [ __readonly__ TABLE_stats <ptag> <cname> <last_clear> <rid_change> <dr_elections> <older_lsa_recv> <nbr_state_change>
 <nbr_dead_postpone> <nbr_dead_expire> <nbr_bad_lsreq> <nbr_seqno_mismatch> <spf_full> <spf_summary> <spf_external> <spf_extsummary>
 <rtr_generate> <rtr_refresh> <rtr_flush> <rtr_other_flush> <net_generate> <net_refresh> <net_flush> <net_other_flush> <inter_prefix_generate>
 <inter_prefix_refresh> <inter_prefix_flush> <inter_prefix_other_flush> <inter_router_generate> <inter_router_refresh> <inter_router_flush>
 <inter_router_other_flush> <asext_generate> <asext_refresh> <asext_flush> <asext_other_flush> <link_generate> <link_refresh>
 <link_flush> <link_other_flush> <intra_prefix_generate> <intra_prefix_refresh> <intra_prefix_flush> <intra_prefix_other_flush>
 <unknown_generate> <unknown_refresh> <unknown_flush> <unknown_other_flush> <limbo_lsa_count> <limbo_lsa_hwm> <limbo_lsa_deleted>
 <limbo_lsa_revived> <limbo_runs> <limbo_lsa_last_time_hwm> [ <limbo_timer> ] <helloq_size> <helloq_max_size> <helloq_hwm>
 <helloq_drops> <helloq_last_hwm_time> <floodq_size> <floodq_max_size> <floodq_hwm> <floodq_drops> <floodq_last_hwm_time> <lsdb_add_fail>
 [ TABLE_buffer_detail [ <buf_size> ] [ <buf_size_huge> ] <buf_in_use> <buf_hwm> <buf_perm> <buf_alloc> <buf_free> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| statistics | Event counters |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3135618990

---

# Command: show ospfv3 summary-address

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] summary-address [ private ] [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; all } ] [ __readonly__ [ TABLE_ctx <ptag> <cname> <rid> [ TABLE_sum <addr> <masklen> [ <metric> ] [ <tag>
 ] [ <pending> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| summary-address | Summary-address redistribution information |
| private | (Optional) Developer-only statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp5981323100

---

# Command: show ospfv3 traffic

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] traffic [ <interface> [ detail ] &#124; [ detail
 ] &#124; [ detail ] vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_traf <ptag> <cname> <last_clear> [ <ifname>
 ] <pkt_in> <pkt_out> <lsu_first_trans> <lsu_retrans> <lsu_for_lsreq> <lsu_nbr_trans> <throttle_out> <throttle_out_token> <throttle_out_ip>
 <lsa_ignored> <lsa_dropped_spf> <lsa_dropped_gr> <pkt_drops_in> <pkt_drops_out> <pkt_errors_in> <pkt_errors_out> <hello_errors_in>
 <dbds_errors_in> <lsreqs_errors_in> <lsus_errors_in> <lsacks_errors_in> <pkt_unknown_in> <pkt_unknown_out> <pkt_no_ospf_intf>
 <bad_version> <bad_crc> <dup_rtr_id> <dup_src_addr> <invalid_src_addr> <invalid_dst_addr> <non_existing_nbr> <pkt_passive_intf>
 <wrong_area> <invalid_pkt_len> <nbr_changed_routerid_ipaddr> <nbr_changed_interfaceid> [ <bad_auth> ] [ <bad_reserved> ] [
 <pkt_no_vrf> ] <hellos_in> <dbds_in> <lsreqs_in> <lsus_in> <lsacks_in> <hellos_out> <dbds_out> <lsreqs_out> <lsus_out> <lsacks_out>
 [ <hellos_in_hq> <dbds_in_hq> <lsreqs_in_flq> <lsus_in_flq> <lsacks_in_flq> <lsas_in_dbds_in> <lsas_in_lsreqs_in> <lsas_in_lsus_in>
 <lsas_in_lsacks_in> <lsas_in_dbds_out> <lsas_in_lsreqs_out> <lsas_in_lsus_out> <lsas_in_lsacks_out> <lsas_in_rxmt_lsus_out>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| interface | (Optional) OSPF enabled interface |
| detail | (Optional) Display detailed information |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3756285924

---

# Command: show ospfv3 virtual-links

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] virtual-links [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> [ TABLE_vlink <name> <nbr_rid> <if_state> <transit_area> <nh_intf> <nbr_addr>
 [ <transit_area_stub> ] [ <transit_area_nssa> ] <addr> [ <masklen> ] <inst_id> <area> [ <if_cfg> ] <state_str> <type_str>
 <cost> <index> [ <passive> ] [ <mpls> ] [ <transmit_delay> ] [ <if_priority> ] [ <dr_rid> ] [ <dr_addr> ] [ <bdr_rid> ] [
 <bdr_addr> ] [ <nbr_total> ] [ <nbr_flood> ] [ <nbr_adjs> ] [ <gr_nbr> ] [ <hello_interval> ] [ <dead_interval> ] [ <wait_interval>
 ] [ <rxmt_interval> ] [ <hello_timer> ] [ <wait_timer> ] [ <pacing_timer> ] [ <lsu_timer> ] [ <lsack_timer> ] [ <netlsa_throt_timer>
 ] [ <link_lsa_cnt> ] [ <link_lsa_crc> ] [ <state> ] [ <transition> ] [ <lastchange> ] [ <priority> ] [ <ifid> ] [ <dr> ] [
 <bdr> ] [ <master> ] [ <seqno> ] [ <dbdallsentacked> ] [ <dbdallsent> ] [ <dbdallacked> ] [ <lsaonreqlist> ] [ <lsafromlastreq>
 ] [ <lsreqrxmts> ] [ <helloptions> ] [ <dbdoptions> ] [ <lastnonhello> ] [ <deadtimer> ] [ <pacingtimer> ] [ <dbdrxmtimer>
 ] [ <reqrxmtimer> ] [ <lsutimer> ] [ <rerxmtimer> ] [ <fastrerxmtimer> ] [ <lsacktimer> ] [ <grtimer> ] [ <helpermode> ] [
 <helpercand> ] [ <helperterm> ] [ <senddbd> ] [ <sendlsreq> ] [ <sendlsu> ] [ <sendlsurxmt> ] [ <sendlsack> ] [ <sendlsreqreply>
 ] [ <ipsec_sa_type> ] [ <ipsec_sa_algorithm> ] [ <ipsec_sa_spi> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| virtual-links | Virtual link information |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2633793999

---

# Command: show ospfv3 virtual-links brief

## Syntax
```
show [ ipv6 ] ospfv3 [ <tag> ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] virtual-links brief [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; all } ] [ __readonly__ TABLE_ctx <ptag> <cname> <vlink_count> [ TABLE_vlink <nbr_rid> <vlink_num> <transit_area> <cost>
 <if_state> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ipv6 | (Optional) Display IPv6 information |
| ospfv3 | Display OSPFv3 status and configuration |
| tag | (Optional) Process tag |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| virtual-links | Virtual link information |
| brief | Display summary of OSPFv3 virtual links |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2828406370

---

# Command: show otv

## Syntax
```
show otv [ <overlay-if> [ vpn <vpn-name> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display OTV information |
| otv | Configure OTV information |
| overlay-if | (Optional) Overlay interface |
| vpn | (Optional) Overlay VPN name |
| vpn-name | (Optional) OTV VPN Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3516666797

---

