# Chapter: F Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_0110.html
**Type:** Show Commands  
**Chapter:** Group-110 Commands  
**Total Commands:** 135

## Command List

- `show fabric database dci`
- `show fabric database host`
- `show fabric database host statistics`
- `show fabric database host summary`
- `show fabric database profile-map`
- `show fabric database static-host`
- `show fabric database statistics`
- `show fabric forwarding host-db`
- `show fabric forwarding ip local`
- `show fabric forwarding ipv6 local`
- `show fabric multicast`
- `show fabric multicast event-history`
- `show fabric multicast globals`
- `show fabric multicast ipv4 l2 vni`
- `show fabric multicast ipv4 rp`
- `show fabric multicast statistics`
- `show fabric multicast vrf`
- `show fc2 bind`
- `show fc2 classf`
- `show fc2 exchange`
- `show fc2 exchresp`
- `show fc2 flogi`
- `show fc2 nport`
- `show fc2 plogi`
- `show fc2 plogi_pwwn`
- `show fc2 port brief`
- `show fc2 port drops`
- `show fc2 port state`
- `show fc2 socket`
- `show fc2 sockexch`
- `show fc2 socknotify`
- `show fc2 socknport`
- `show fc2 vsan`
- `show fcdroplatency`
- `show fcoe-npv issu-impact`
- `show fcoe`
- `show fcoe database`
- `show fctimer`
- `show fctimer D_S_TOV`
- `show fctimer E_D_TOV`
- `show fctimer F_S_TOV`
- `show fctimer R_A_TOV`
- `show fctimer last action status`
- `show fctimer pending-diff`
- `show fctimer pending`
- `show fctimer session status`
- `show fctimer status`
- `show fctimer vsan`
- `show feature-set`
- `show feature-set services`
- `show feature`
- `show fhrp`
- `show fhrp verbose`
- `show file`
- `show fips status`
- `show flow cache`
- `show flow cache`
- `show flow exporter`
- `show flow exporter`
- `show flow filter`
- `show flow interface`
- `show flow monitor`
- `show flow monitor`
- `show flow profile`
- `show flow record`
- `show flow record`
- `show flow rtp`
- `show flow rtp timeout`
- `show flow system`
- `show flow timeout`
- `show flow tracer`
- `show forwarding`
- `show forwarding adjacency`
- `show forwarding distribution clients`
- `show forwarding distribution fib-state`
- `show forwarding distribution ip igmp snooping`
- `show forwarding distribution ipv6 multicast route`
- `show forwarding distribution l2 multicast`
- `show forwarding distribution lisp counters`
- `show forwarding distribution lisp vrf enabled`
- `show forwarding distribution multicast`
- `show forwarding distribution multicast client-ack-db`
- `show forwarding distribution multicast client`
- `show forwarding distribution multicast download`
- `show forwarding distribution multicast mfib`
- `show forwarding distribution multicast outgoing-interface-list`
- `show forwarding distribution multicast outgoing-interface-list L2_PRIME`
- `show forwarding distribution multicast resp-ack-timer-msgs`
- `show forwarding distribution multicast route`
- `show forwarding distribution multicast vxlan dsg-db`
- `show forwarding distribution nve overlay-vlan`
- `show forwarding distribution peer-id`
- `show forwarding distribution trace`
- `show forwarding ecmp`
- `show forwarding ecmp recursive`
- `show forwarding interfaces`
- `show forwarding ipv6 adjacency`
- `show forwarding ipv6 inconsistency`
- `show forwarding ipv6 multicast route`
- `show forwarding ipv6 route`
- `show forwarding kvfib cache on`
- `show forwarding l2 multicast`
- `show forwarding l2vpn label vpls`
- `show forwarding l2vpn label xconnect`
- `show forwarding l2vpn vlan`
- `show forwarding mpls`
- `show forwarding mpls aggregate`
- `show forwarding mpls cbts`
- `show forwarding mpls drop-stats`
- `show forwarding mpls ecmp`
- `show forwarding mpls eompls`
- `show forwarding mpls eompls ir`
- `show forwarding mpls option_b`
- `show forwarding mpls srte module`
- `show forwarding mpls summary`
- `show forwarding mpls te`
- `show forwarding multicast-sr loopback interface`
- `show forwarding multicast outgoing-interface-list`
- `show forwarding multicast route`
- `show forwarding nve l2 ingress-replication-peers`
- `show forwarding nve l3 adjacency tunnel`
- `show forwarding nve l3 adjacency v6-tunnel`
- `show forwarding nve l3 ecmp`
- `show forwarding nve l3 peers`
- `show forwarding nve underlay-interfaces`
- `show forwarding otv`
- `show forwarding security group-tag`
- `show forwarding security mac`
- `show forwarding trace`
- `show forwarding trace profile`
- `show forwarding trace profile funcstats`
- `show fte event`
- `show fte exporter`
- `show fte monitor`
- `show fte record`

---

## Detailed Command Reference

# Command: show fabric database dci

## Syntax
```
show fabric database dci [ { vrf { <vrf-name> &#124; <vrf-known-name> } [ peer-id <peer-ip-address> ] [ detail ] } ] [ __readonly__
 [ TABLE_database_dci <vrf_name> <state> <flags> <profile> <instance> ] [ TABLE_database_dci_detail <packet_arrival_time> <sent_to_database_manager_at>
 <received_parameters_from_database_manager_at> <sent_apply_to_configuration_manager_at> <completed_executing_all_commands_at>
 <sent_un_apply_to_configuration_manager_at> <completed_unapplying_all_commands_at> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| dci | DCI Profile Database |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| peer-id | (Optional) management ip address of peer |
| peer-ip-address | (Optional) IP address in CIDR format |
| detail | (Optional) Show detailed information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4265331279

---

# Command: show fabric database host

## Syntax
```
show fabric database host [ detail ] [ { vni <vni-id> } &#124; { dot1q <vlan-id> } ] [ __readonly__ [ TABLE_database_host [ <trigger_source>
 ] [ <client_type> ] [ <got_trigger_at> ] [ <number_of_client_hosts> ] [ <number_of_associated_interfaces> ] [ <profile_be_un_applied_in_seconds>
 ] [ <new_vdp_requests_be_accepted_in_seconds> ] [ <recovered_profile_be_checked_for_validity_in_seconds> ] [ <mac_aging_checked_in_seconds>
 ] [ <sent_to_database_manager_at> ] [ <received_parameters_from_database_manager_at> ] [ <displaying_parameters_for_profile>
 ] [ <displaying_parameters_for_instance> ] [ <no_parameters_for_the_profile> ] [ <displaying_re_written_parameters_for_vpc_role>
 ] [ TABLE_parameter [ <parameter_index> ] [ <parameter> ] ] [ TABLE_static_profile <profile> <instance> <no_parameters_for_the_profile>
 ] [ TABLE_migrated_profile <profile> <instance_index> <previous_profile> <previous_instance_index> ] [ TABLE_rollback_profile
 <profile> <instance_index> ] [ <got_vlan_allocated_from_vlan_manager_at> ] [ <sent_apply_to_configuration_manager_at> ] [
 <completed_executing_all_commands_at> ] [ <sent_to_vpc_peer_at> ] [ <completed_executing_all_commands_on_vpc_peer_at> ] [
 <sent_un_apply_to_configuration_manager_at> ] [ <completed_unapplying_all_commands_at> ] ] [ TABLE_database_host_vni { [ <vni_id>
 ] [ <vlan_id> ] [ <state> <flag> <profile_name> <instance_name> ] [ <packet_arrival_time> <request_profile_time> <got_profile_time>
 <sent_to_PPM_time> <profile_apply_time> <del_to_PPM_time> ] [ { TABLE_database_host_detail <interface> <encap> <flags> <state>
 [ <vsi_id> ] [ <client> ] [ <host> ] } ] } ] [ TABLE_database_host_vlan { [ <vlan_id> ] [ <vni_id> ] [ <state> <flag> <profile_name>
 <instance_name> ] [ <packet_arrival_time> <request_profile_time> <got_profile_time> <sent_to_PPM_time> <profile_apply_time>
 <del_to_PPM_time> ] [ { TABLE_database_host_detail <interface> <encap> <flags> <state> [ <vsi_id> ] } ] } ] [ TABLE_extranet_vrf_entries
 { <vrf> <l3_vni> <state> <profile> <instance> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| host | Host to profile mapping |
| detail | (Optional) Show hosts and interfaces |
| vni | (Optional) Virtual Network Identifier |
| vni-id | (Optional) |
| dot1q | (Optional) Dot1Q Encapsulation |
| vlan-id | (Optional) |
| __readonly__ | (Optional) Read Only |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp6373812850

---

# Command: show fabric database host statistics

## Syntax
```
show fabric database host statistics [ __readonly__ [ TABLE_database_host_statistics { [ <data_snoop_triggers> ] [ <data_snoop_deletes>
 ] [ <data_snoop_responses> ] [ <vdp_association_requests> ] [ <vdp_deassociation_requests> ] [ <vdp_association_responses>
 ] [ <vdp_error_responses> ] [ <unsupported_interfaces> ] [ <no_profile_map_errors> ] [ <outstanding_delete_retry_add> ] [
 <duplicate_add_existing_host> ] [ <hmm_api_error_cannot_add_host> ] [ <existing_profile_new_host> ] [ <profile_apply_from_vpc_peer>
 ] [ <profile_un_apply_from_vpc_peer> ] [ <host_apply_from_vpc_peer> ] [ <host_un_apply_from_vpc_peer> ] [ <early_delete_cancel_add>
 ] [ <dhcp_requests> ] [ <dhcp_responses> ] [ <dhcp_error_responses> ] [ <adbm_requests> ] [ <adbm_responses> ] [ <adbm_error_responses>
 ] [ <adbm_error_requests> ] [ <adbm_db_notifications> ] [ <vnseg_no_bridge_domain> ] [ <vnseg_encap_responses> ] [ <vnseg_vni_responses>
 ] [ <vnseg_unknown_responses> ] [ <vnseg_bd_down_notif> ] [ <bd_mgr_requests> ] [ <bd_mgr_success_responses> ] [ <bd_mgr_failure_responses>
 ] [ <bd_mgr_unreserve> ] [ <bd_mgr_inconsistencies> ] [ <no_mac_on_bd_notif> ] [ <refresh_failures> ] [ <profile_apply_received>
 ] [ <profile_vpc_queued> ] [ <profile_local_apply_queued> ] [ <profile_local_unapply_queued> ] [ <profile_apply_sent> ] [
 <profile_apply_responses> ] [ <profile_apply_success> ] [ <profile_unapply_success> ] [ <profile_apply_failure> ] [ <profile_commands>
 ] [ <profile_error_incomplete_configs> ] [ <profile_api_error> ] [ <profile_unapply_sent> ] [ <profile_top_queue_adds> ] [
 <profile_high_queue_adds> ] [ <profile_low_queue_adds> ] [ <profile_unapply_failure> ] [ <outstanding_vlan_requests> ] [ <outstanding_adbm_requests>
 ] [ <outstanding_profile_applies> ] [ <outstanding_vpc_profile_applies> ] [ <node_recon_pending> ] [ <node_recon_attempts>
 ] [ <node_recon_failures> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| host | Auto-configured Hosts |
| statistics | Statistics - Mostly shows non-zero values |
| __readonly__ | (Optional) Read Only |
| TABLE_database_host_statistics | (Optional) table show fabric database host statistics |
| data_snoop_triggers | (Optional) TODO |
| data_snoop_deletes | (Optional) TODO |
| data_snoop_responses | (Optional) TODO |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp8529961220

---

# Command: show fabric database host summary

## Syntax
```
show fabric database host summary [ __readonly__ [ TABLE_database_host_summary { <number_of_instances_applied> <number_of_client_hosts>
 <recovery_timeout_minute> <cleanup_timeout_minute> <client_add_suppression_timeout_minute> <mac_aging_timeout_minute> <autoid_support>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| host | Auto-configured Hosts |
| summary | Summary |
| __readonly__ | (Optional) Read Only |
| TABLE_database_host_summary | (Optional) table show fabric database host summary |
| number_of_instances_applied | (Optional) TODO |
| number_of_client_hosts | (Optional) TODO |
| recovery_timeout_minute | (Optional) TODO |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1940752472

---

# Command: show fabric database profile-map

## Syntax
```
show fabric database profile-map { global &#124; [ <id> &#124; interface <interface-id> ] } [ __readonly__ [ TABLE_database_profile_map
 { <map> <proto> <vni> <dot1q> <flags> <profile_name> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| profile-map | Profile Map |
| global | Global profile (apply to all interfaces) |
| id | (Optional) Profile Map ID |
| interface | (Optional) Specified interface to display |
| interface-id | (Optional) Name of interface |
| __readonly__ | (Optional) Read Only |
| TABLE_database_profile_map | (Optional) table show fabric database profile-map |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3705735583

---

# Command: show fabric database static-host

## Syntax
```
show fabric database static-host [ __readonly__ { TABLE_database_static_host <host_key> <interface> <state> <retry_delay>
 <retry_attempts> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Fabric Database |
| static-host | Configured Static Hosts |
| __readonly__ | (Optional) Read Only |
| TABLE_database_static_host | (Optional) table show fabric database static-host |
| host_key | (Optional) static-host key |
| interface | (Optional) interface name |
| state | (Optional) static-host state |
| retry_delay | (Optional) seconds until next retry |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp6699548890

---

# Command: show fabric database statistics

## Syntax
```
show fabric database statistics [ type { network &#124; profile &#124; cabling &#124; partition &#124; bl-dci &#124; host } ] [ __readonly__ { TABLE_types
 <dbtype> <requests> <dispatched> <not_dispatched> <re_dispatched> } [ { TABLE_dbs <is_active> <type> <prot> <serverdb> [ <reqs>
 <ok> <nores> <err> <tmout> <pend> ] } ] { LastPollTime <poll_time> } { LastUpdateTime <update_time> } [ { TABLE_updates <update_type>
 <update_status> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| database | Show Fabric Database |
| statistics | Show database statistics |
| type | (Optional) Enter database type |
| network | (Optional) Network Database |
| profile | (Optional) Port or Switch Profile Database |
| cabling | (Optional) Cable Management Database |
| partition | (Optional) Partition Database |
| bl-dci | (Optional) Border Leaf - DCI |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3591778745

---

# Command: show fabric forwarding host-db

## Syntax
```
show fabric forwarding host-db [ { vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } } ] [ __readonly__ [ TABLE_forwarding_host_db_vrf
 { <vrf> <vrf_id> <vrf_state> <vrf_reason> <vni_id> <refcount> <conversational_learning> [ TABLE_limit_type <limit_type> <enable>
 <threshold> <action> ] [ TABLE_ipv4 <address_family> <vrf> <table_id> <table_state> <refcount> <local_hosts> <remote_hosts>
 <aggregates> [ TABLE_aggregate_list <aggregate_subnet_prefix_list> <aggregate_subnet_prefix_state> ] ] [ TABLE_ipv6 <address_family>
 <vrf> <table_id> <table_state> <refcount> <local_hosts> <remote_hosts> <aggregates> [ TABLE_aggregate_list <aggregate_subnet_prefix_list>
 <aggregate_subnet_prefix_state> ] ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| host-db | Host Database info |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| __readonly__ | (Optional) Read Only |
| TABLE_forwarding_host_db_vrf | (Optional) table show fabric forwarding host-db vrf |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3946558698

---

# Command: show fabric forwarding ip local

## Syntax
```
show fabric forwarding ip { local-host-db [ { vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } } ] [ <ip-prefix> ] } [ __readonly__
 [ TABLE_forwarding_ip_local_host_db_vrf { <hmm_host> <vrf> <status_in> { TABLE_hosts <host> <mac_address> <svi> <flags_0x>
 <physical_interface> <status> } } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| ip | Display IP information |
| local-host-db | HMM Local Host Database |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| ip-prefix | (Optional) IP prefix in CIDR format |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp3349056024

---

# Command: show fabric forwarding ipv6 local

## Syntax
```
show fabric forwarding ipv6 { local-host-db [ { vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } } ] [ <ipv6-prefix> ] } [ __readonly__
 [ TABLE_forwarding_ipv6_local_host_db_vrf { <hmm_host> <vrf> <status_in> { TABLE_hosts <host> <mac_address> <svi> <flags_0x>
 <physical_interface> <status> } } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| forwarding | Fabric Forwarding Protocol: Host Mobility Manager (HMM) |
| ipv6 | Display IPv6 information |
| local-host-db | HMM Local Host Database |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| __readonly__ | (Optional) Read Only |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp6866047810

---

# Command: show fabric multicast

## Syntax
```
show fabric multicast { ipv4 { mroute [ { <v4_group> [ <v4_source> ] } ] &#124; ssm-range &#124; rp-grange &#124; sa-ad-route [ { <v4_group>
 [ <v4_source> ] } ] } &#124; ipv6 { mroute [ { <v6_group> [ <v6_source> ] } ] &#124; ssm-range &#124; rp-grange &#124; sa-ad-route [ { <v4_group>
 [ <v4_source> ] } ] } } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_vrf <context_name> <nlri_type>
 <vnid> [ TABLE_mroute <mroute> <mroute_uptime> { TABLE_node <node_addr> <core-interest> <fabric-interest> <node_uptime> <real_join>
 <sim_join> <rpf_nbr> } ] [ TABLE_rp <border_leaf_addr> { TABLE_rp_grange <rp_grange_desc> } ] [ TABLE_ssm <border_leaf_addr>
 { TABLE_ssm_range <ssm_range_desc> } ] [ TABLE_sa_ad_route <sa_ad_desc> <sa_ad_route_uptime> [ TABLE_intrstd_node <intrstd_node_addrs>
 <intrstd_node_uptime> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| ipv4 | Display IP information |
| ipv6 | Display IPv6 information |
| mroute | display fabric mroutes |
| sa-ad-route | display Src Active AD routes |
| ssm-range | display SSM ranges |
| rp-grange | display RP granges |
| v4_group | (Optional) IPV4 Group address to display |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1004324013

---

# Command: show fabric multicast event-history

## Syntax
```
show fabric multicast [ internal ] event-history { errors &#124; msgs &#124; <ngmvpn-event-hist-buf-name> &#124; statistics }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| internal | (Optional) Commands for internal use |
| event-history | Show various event logs of NGMVPN |
| errors | Show error logs of NGMVPN |
| msgs | Show various message logs of NGMVPN |
| ngmvpn-event-hist-buf-name | Show event hist buffer name |
| statistics | Show the state and size of the buffer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2840734361

---

# Command: show fabric multicast globals

## Syntax
```
show fabric multicast globals [ __readonly__ <pruning> <switch_role> <fabric_control_seg> <peer_fabric_ctrl_addr> <advertise_vpc_rpf_routes>
 <created_vni_list> <fwd_encap> <mrib_sync_delay> <bgp_eor_rcvd> <bgp_eor_rcvd_ts> <cli_done_rcvd> <cli_done_rcvd_ts> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| globals | show the global settings |
| __readonly__ | (Optional) |
| pruning | (Optional) |
| switch_role | (Optional) |
| fabric_control_seg | (Optional) |
| peer_fabric_ctrl_addr | (Optional) |
| advertise_vpc_rpf_routes | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3124269224

---

# Command: show fabric multicast ipv4 l2 vni

## Syntax
```
show fabric multicast { ipv4 &#124; ipv6 } { l2-mroute } vni { <vni-id> &#124; all } [ __readonly__ TABLE_vni <vnid> [ TABLE_mroute
 <mroute_desc> [ TABLE_fabric <fabric_node_addr> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| ipv4 | Display IP information |
| ipv6 | Display IPv6 information |
| l2-mroute | display l2-mroute status |
| vni | Virtual Network Identifier |
| vni-id | VNI number |
| all | Display all L2 VNI NGMVPN is aware of |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, overlay, network, S-commands
**Command ID:** wp4563216670

---

# Command: show fabric multicast ipv4 rp

## Syntax
```
show fabric multicast { ipv4 &#124; ipv6 } { rp-route } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| ipv4 | Display IP information |
| ipv6 | Display IPv6 information |
| rp-route | display fabric rp-routes |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display all VRFs NGMVPN is aware of |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp1394607900

---

# Command: show fabric multicast statistics

## Syntax
```
show fabric multicast [ internal ] statistics
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| internal | (Optional) Commands for internal use |
| statistics | Show the state and size of the buffer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3378735109

---

# Command: show fabric multicast vrf

## Syntax
```
show fabric multicast vrf [ { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ { TABLE_vrf <context_name><context_id><vprime_iod><vnid>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fabric | Fabric |
| multicast | Multicast information |
| vrf | Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display all VRFs NGMVPN is aware of |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp2136898790

---

# Command: show fc2 bind

## Syntax
```
show fc2 bind [ __readonly__ { TABLE_fc2bind <SOCKET> <FLAGS> <NLEVEL> <RULE> <SINDEX> <VSAN> <D_ID> <MASK> <TYPE> <SUBTYPE>
 <M_VALUES> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| bind | show fc2 socket bindings |
| __readonly__ | (Optional) Read only |
| TABLE_fc2bind | (Optional) show fc2 bind |
| SOCKET | (Optional) socket |
| FLAGS | (Optional) flags |
| NLEVEL | (Optional) nlevel |
| RULE | (Optional) rule |
| SINDEX | (Optional) sidnex |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3407090745

---

# Command: show fc2 classf

## Syntax
```
show fc2 classf [ __readonly__ { TABLE_fc2classf <HIX> <VSAN> <S_ID> <D_ID> <IFIDX> <R_A_TOV> <E_D_TOV> <F-SO> <RC> <RS> <CS>
 <EE> <2-SO> <RS> <3-SO> <RS> <EECNT> <TCCNT> <FCNT> <REFCNT> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| classf | show fc2 classf sessions |
| __readonly__ | (Optional) Read only |
| TABLE_fc2classf | (Optional) show fc2 classf |
| HIX | (Optional) hix |
| VSAN | (Optional) vsan |
| S_ID | (Optional) sid |
| D_ID | (Optional) did |
| IFIDX | (Optional) ifidx |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp4130007662

---

# Command: show fc2 exchange

## Syntax
```
show fc2 exchange [ __readonly__ { TABLE_ExchngInfo [ <ECB_INUSE> ] [ <ECB_DROPPED> ] [ <ECB_TOTAL> ] [ <ECB_MAX> ] } [ TABLE_fc2exchange
 <HIX> <VSAN> <X_ID> <OX_ID> <RX_ID> <O_ID> <R_ID> <ESTAT> <STATE> <SOCKET> <DIFINDEX> <CS> <TYPE> <SEQID> <TCNT> <RCNT> <LO>
 <HI> <SSTAT> <LOGIN> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| exchange | show fc2 active exchanges |
| __readonly__ | (Optional) Read only |
| TABLE_ExchngInfo | (Optional) ecb info |
| ECB_INUSE | (Optional) ecb in use |
| ECB_DROPPED | (Optional) ecb dropped |
| ECB_TOTAL | (Optional) ecb total |
| ECB_MAX | (Optional) ecb threshold |
| TABLE_fc2exchange | (Optional) show fc2 exchange |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3486669877

---

# Command: show fc2 exchresp

## Syntax
```
show fc2 exchresp [ __readonly__ { TABLE_fc2exchresp <HIX> <VSAN> <OX_ID> <S_ID> <CS> <SIFINDEX> <OX_ID2> <RX_ID2> <O_ID>
 <R_ID> <ESTAT> <STATE> <SOCKET> <TYPE> <SEQID> <TCNT> <RCNT> <LO> <HI> <SSTAT> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| exchresp | show fc2 active responder exchanges |
| __readonly__ | (Optional) Read only |
| TABLE_fc2exchresp | (Optional) show fc2 exchresp |
| HIX | (Optional) hix |
| VSAN | (Optional) vsan |
| OX_ID | (Optional) oxid |
| S_ID | (Optional) sid |
| CS | (Optional) cs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2177826084

---

# Command: show fc2 flogi

## Syntax
```
show fc2 flogi [ __readonly__ { TABLE_fc2flogi <HIX> <VSAN> <S_ID> <FLOGI> <IFINDEX> <TYPE> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| flogi | show fc2 flogi table |
| __readonly__ | (Optional) Read only |
| TABLE_fc2flogi | (Optional) show fc2 flogi |
| HIX | (Optional) hix |
| VSAN | (Optional) vsan |
| S_ID | (Optional) sid |
| FLOGI | (Optional) flogi |
| IFINDEX | (Optional) ifindex |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4227543454

---

# Command: show fc2 nport

## Syntax
```
show fc2 nport [ __readonly__ { TABLE_fc2nport <REF> <VSAN> <D_ID> <MASK> <FL> <ST> <IFINDEX> <CF> <TC> <2-SO> <IC> <RC> <RS>
 <CS> <EE> <3-SO> <3-SO-IC> <3-SO-RC> <3-SO-RS> <3-SO-CS> <3-SO-EE> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| nport | show fc2 local nports |
| __readonly__ | (Optional) Read only |
| TABLE_fc2nport | (Optional) show fc2 nport |
| REF | (Optional) ref |
| VSAN | (Optional) vsan |
| D_ID | (Optional) did |
| MASK | (Optional) mask |
| FL | (Optional) fl |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2256771354

---

# Command: show fc2 plogi

## Syntax
```
show fc2 plogi [ __readonly__ { TABLE_fc2plogi <HIX> <ADDRESS> <VSAN> <S_ID> <D_ID> <IF_INDEX> <FL> <STATE> <CF> <TC> <2-SO>
 <IC> <RC> <RS> <CS> <EE> <3-SO> <3SO_IC> <3SO_RC> <3SO_RS> <3SO_CS> <3SO_EE> <EECNT> <TCCNT> <2CNT> <3CNT> <REFCNT> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| plogi | show fc2 plogi sessions |
| __readonly__ | (Optional) Read only |
| TABLE_fc2plogi | (Optional) show fc2 plogi |
| HIX | (Optional) hix |
| ADDRESS | (Optional) address |
| VSAN | (Optional) vsan |
| S_ID | (Optional) sid |
| D_ID | (Optional) did |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp6927504290

---

# Command: show fc2 plogi_pwwn

## Syntax
```
show fc2 plogi_pwwn [ __readonly__ { TABLE_fc2plogi_pwwn <HIX> <ADDRESS> <VSAN> <S_ID> <D_ID> <IFINDEX> <FL> <STATE> <PWWN>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| plogi_pwwn | show fc2 plogi pwwn entries |
| __readonly__ | (Optional) Read only |
| TABLE_fc2plogi_pwwn | (Optional) show fc2 plogi_pwwn |
| HIX | (Optional) hix |
| ADDRESS | (Optional) address |
| VSAN | (Optional) vsan |
| S_ID | (Optional) s_id |
| D_ID | (Optional) d_id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4598732010

---

# Command: show fc2 port brief

## Syntax
```
show fc2 port brief [ __readonly__ { TABLE_fc2portbrief <BAD_FRAME_RX> } [ TABLE_FCSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP>
 <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_LBSTAT <IX> <ST> <MOD> <EMUL> <TXLBPKTS> <TXLBDROP> <RXLBPKTS> <RXLBDROP> ] [ TABLE_VFCSTAT
 <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP> <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_VFCPOSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP>
 <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_VFCSLOTSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP> <TXERR> <RXPKTS> <RXDROP> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| port | show fc2 physical port table |
| brief | display only active port counters |
| __readonly__ | (Optional) Read only |
| TABLE_fc2portbrief | (Optional) bad frames received |
| BAD_FRAME_RX | (Optional) fc2 bad frames rx |
| TABLE_FCSTAT | (Optional) FC Stat table |
| IX | (Optional) index |
| ST | (Optional) status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2772840548

---

# Command: show fc2 port drops

## Syntax
```
show fc2 port drops [ __readonly__ [ TABLE_FCSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP> <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_LBSTAT
 <IX> <ST> <MOD> <EMUL> <TXLBPKTS> <TXLBDROP> <RXLBPKTS> <RXLBDROP> ] [ TABLE_VFCSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP>
 <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_VFCPOSTAT <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP> <TXERR> <RXPKTS> <RXDROP> ] [ TABLE_VFCSLOTSTAT
 <IX> <ST> <MOD> <EMUL> <TXPKTS> <TXDROP> <TXERR> <RXPKTS> <RXDROP> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| port | show fc2 physical port table |
| drops | display active port drop counters |
| __readonly__ | (Optional) Read only |
| TABLE_FCSTAT | (Optional) FC Stat table |
| IX | (Optional) index |
| ST | (Optional) status |
| MOD | (Optional) mode |
| EMUL | (Optional) TEemul |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3485177559

---

# Command: show fc2 port state

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| port | show fc2 physical port table |
| state | display port state history |
| __readonly__ | (Optional) Read only |
| TABLE_FCPORTSTATE | (Optional) fc port state change history |
| PORT_STRING | (Optional) port name |
| PORT_NO | (Optional) port number |
| UP_DOWN_CNTR | (Optional) up-down counter |
| UP_STRING | (Optional) up |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1026897628

---

# Command: show fc2 socket

## Syntax
```
show fc2 socket [ __readonly__ { TABLE_fc2socket <SOCKET> <REFCNT> <PROTOCOL> <FLAGS> <PID> <RCVBUF> <RMEM_USED> <QLEN> <NOTSK>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| socket | show fc2 active sockets |
| __readonly__ | (Optional) Read only |
| TABLE_fc2socket | (Optional) show fc2 socket |
| SOCKET | (Optional) socket |
| REFCNT | (Optional) refcnt |
| PROTOCOL | (Optional) protocol |
| FLAGS | (Optional) flags |
| PID | (Optional) pid |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2537267658

---

# Command: show fc2 sockexch

## Syntax
```
show fc2 sockexch [ __readonly__ { TABLE_fc2sockexch <SOCKET> <VSAN> <X_ID> <OX_ID> <RX_ID> <O_ID> <R_ID> <ESTAT> <STATE>
 <CS> <TYPE> <SK> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| sockexch | show fc2 active exchanges for each socket |
| __readonly__ | (Optional) Read only |
| TABLE_fc2sockexch | (Optional) show fc2 sockexch |
| SOCKET | (Optional) socket |
| VSAN | (Optional) vsan |
| X_ID | (Optional) x_id |
| OX_ID | (Optional) oxid |
| RX_ID | (Optional) rxid |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2385956455

---

# Command: show fc2 socknotify

## Syntax
```
show fc2 socknotify [ __readonly__ { TABLE_fc2socknotify <SOCKET> <ADDRESS> <REF> <VSAN> <D_ID> <MASK> <FL> <ST> <IFINDEX>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| socknotify | show fc2 local nport plogi/logo notifications per each socket |
| __readonly__ | (Optional) Read only |
| TABLE_fc2socknotify | (Optional) show fc2 socknotify |
| SOCKET | (Optional) socket |
| ADDRESS | (Optional) address |
| REF | (Optional) ref |
| VSAN | (Optional) vsan |
| D_ID | (Optional) d_id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3810186371

---

# Command: show fc2 socknport

## Syntax
```
show fc2 socknport [ __readonly__ { TABLE_fc2socknport <SOCKET> <ADDRESS> <REF> <VSAN> <D_ID> <MASK> <FL> <ST> <IFINDEX> }
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| socknport | show fc2 local nports per each socket |
| __readonly__ | (Optional) Read only |
| TABLE_fc2socknport | (Optional) show fc2 socknport |
| SOCKET | (Optional) socket |
| ADDRESS | (Optional) address |
| REF | (Optional) ref |
| VSAN | (Optional) vsan |
| D_ID | (Optional) d_id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3818262812

---

# Command: show fc2 vsan

## Syntax
```
show fc2 vsan [ __readonly__ { TABLE_fc2vsan <VSAN> <X_ID> <E_D_TOV> <R_A_TOV> <WWN> <IOP_MODE> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fc2 | show fc2 tables and statistics |
| vsan | show fc2 vsan table |
| __readonly__ | (Optional) Read only |
| TABLE_fc2vsan | (Optional) show fc2 vsan |
| VSAN | (Optional) vsan |
| X_ID | (Optional) xid |
| E_D_TOV | (Optional) e_d_tov |
| R_A_TOV | (Optional) r_a_tov |
| WWN | (Optional) wwn |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1949200328

---

# Command: show fcdroplatency

## Syntax
```
show fcdroplatency [ { network &#124; switch } ] [ __readonly__ [ <switch_latency> ] [ <global_network_latency> ] [ TABLE_vsan_network_latency
 { <vsan-no> <network-latency> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fcdroplatency | show switch or network latency |
| network | (Optional) network latency in milliseconds |
| switch | (Optional) switch latency in milliseconds |
| __readonly__ | (Optional) |
| switch_latency | (Optional) Switch latency value |
| global_network_latency | (Optional) global network latency value |
| TABLE_vsan_network_latency | (Optional) VSAN specific network latency settings |
| vsan-no | (Optional) vsan number |
| network-latency | (Optional) VSAN specific network latency |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp5185429200

---

# Command: show fcoe-npv issu-impact

## Syntax
```
show fcoe-npv issu-impact [ __readonly__ { <is_impact> } [ TABLE_interface <vfc_intf> <fc_id> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system informationrunning system information |
| fcoe-npv | feature fcoe-npv |
| issu-impact | Show feature fcoe-npv config issues if attempting to do non-disruptive ISSU |
| __readonly__ | (Optional) Read Only |
| is_impact | (Optional) show issu impact |
| TABLE_interface | (Optional) show fcoe database |
| vfc_intf | (Optional) vfc port Interface index |
| fc_id | (Optional) vfc port FCID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3651594447

---

# Command: show fcoe

## Syntax
```
show fcoe [ __readonly__ { TABLE_fcf <fcf_if_index> <fcf_mac> <fc_map> <fcf_priority> <fka_Advertisement> } [ TABLE_vfc <vfc_name>
 <vfcf_mac> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fcoe | Show FCOE paramaters |
| __readonly__ | (Optional) Read Only |
| TABLE_fcf | (Optional) fcf table |
| fcf_if_index | (Optional) fcf if index |
| fcf_mac | (Optional) fcf mac |
| fc_map | (Optional) fc map |
| fcf_priority | (Optional) fcf priority |
| fka_Advertisement | (Optional) fka Advertisement |
| TABLE_vfc | (Optional) vfc details table for sup |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3286516465

---

# Command: show fcoe database

## Syntax
```
show fcoe database [ __readonly__ { TABLE_interface <interface> [ <fcid> ] [ <port_name> ] <mac_address> } <flogi_count> [
 TABLE_veport <interface> <mac_address> <vsan> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fcoe | Show FCOE paramaters |
| database | Show FCOE database |
| __readonly__ | (Optional) Read Only |
| interface | (Optional) Interface index |
| TABLE_interface | (Optional) show fcoe database |
| fcid | (Optional) fcid |
| port_name | (Optional) port name |
| mac_address | (Optional) mac address |
| interface | (Optional) ve port Interface index |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4105636862

---

# Command: show fctimer

## Syntax
```
show fctimer [ __readonly__ { <F_S_TOV> <D_S_TOV> <E_D_TOV> <R_A_TOV> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show running system information |
| fctimer | show Fibre Channel timers |
| __readonly__ | (Optional) Read only |
| F_S_TOV | (Optional) F_S_TOV |
| D_S_TOV | (Optional) D_S_TOV |
| E_D_TOV | (Optional) E_D_TOV |
| R_A_TOV | (Optional) R_A_TOV |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3457077953

---

# Command: show fctimer D_S_TOV

## Syntax
```
show fctimer D_S_TOV [ vsan <i0> ] [ __readonly__ [ TABLE_D_S_TOV [ <vsan-no> ] <D_S_TOV> ] [ <non-exist-vsan> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| D_S_TOV | D_S_TOV in milliseconds |
| vsan | (Optional) Specify VSAN id |
| i0 | (Optional) VSAN id range |
| __readonly__ | (Optional) |
| TABLE_D_S_TOV | (Optional) table D_S_TOV |
| vsan-no | (Optional) vsan number |
| D_S_TOV | (Optional) D_S_TOV |
| non-exist-vsan | (Optional) non configured vsans |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp5100911690

---

# Command: show fctimer E_D_TOV

## Syntax
```
show fctimer E_D_TOV [ vsan <i0> ] [ __readonly__ [ TABLE_E_D_TOV [ <vsan-no> ] <E_D_TOV> ] [ <non-exist-vsan> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| E_D_TOV | E_D_TOV in milliseconds |
| vsan | (Optional) Specify VSAN id |
| i0 | (Optional) VSAN id range |
| __readonly__ | (Optional) |
| TABLE_E_D_TOV | (Optional) table |
| vsan-no | (Optional) vsan number |
| E_D_TOV | (Optional) E_D_TOV |
| non-exist-vsan | (Optional) not exist vsans |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3813299317

---

# Command: show fctimer F_S_TOV

## Syntax
```
show fctimer F_S_TOV [ vsan <i0> ] [ __readonly__ [ TABLE_F_S_TOV [ <vsan-no> ] <F_S_TOV> ] [ <non-exist-vsan> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| F_S_TOV | F_S_TOV in milliseconds |
| vsan | (Optional) Specify VSAN id |
| i0 | (Optional) VSAN id range |
| __readonly__ | (Optional) |
| TABLE_F_S_TOV | (Optional) table |
| vsan-no | (Optional) vsan number |
| F_S_TOV | (Optional) F_S_TOV |
| non-exist-vsan | (Optional) not exist vsans |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2344364340

---

# Command: show fctimer R_A_TOV

## Syntax
```
show fctimer R_A_TOV [ vsan <i0> ] [ __readonly__ [ TABLE_R_A_TOV [ <vsan-no> ] <R_A_TOV> ] [ <non-exist-vsan> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| R_A_TOV | R_A_TOV in milliseconds |
| vsan | (Optional) Specify VSAN id |
| i0 | (Optional) VSAN id range |
| __readonly__ | (Optional) |
| TABLE_R_A_TOV | (Optional) table |
| vsan-no | (Optional) vsan number |
| R_A_TOV | (Optional) R_A_TOV |
| non-exist-vsan | (Optional) non exist vsans |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2902991154

---

# Command: show fctimer last action status

## Syntax
```
show fctimer last action status [ __readonly__ [ <vsan> ] <last_action_timestamp> <last_action> <last_action_result> <last_action_failure_reason>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| last | Show the status of the last cfs commit/abort operation |
| action | Show the status of the last cfs commit/abort operation |
| status | Show the status of the last cfs commit/abort operation |
| __readonly__ | (Optional) Readonly |
| vsan | (Optional) Vsan |
| last_action_timestamp | (Optional) Last action timestamp |
| last_action | (Optional) Last action |
| last_action_result | (Optional) Last action result |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1080766605

---

# Command: show fctimer pending-diff

## Syntax
```
show fctimer pending-diff [ __readonly__ <status_fctimer> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| pending-diff | Show the difference between pending database and running config |
| __readonly__ | (Optional) |
| status_fctimer | (Optional) Show the difference between pending database and running config |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp4455297090

---

# Command: show fctimer pending

## Syntax
```
show fctimer pending [ __readonly__ <status_fctimer> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| pending | Show the status of pending fctimer commands |
| __readonly__ | (Optional) |
| status_fctimer | (Optional) Show the status of pending fctimer commands |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3730545621

---

# Command: show fctimer session status

## Syntax
```
show fctimer session status [ __readonly__ [ <vsan> ] <last_action_timestamp> <last_action> <last_action_result> <last_action_failure_reason>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| session | Show the state of fctimer cfs session |
| status | Show the status of the last cfs commit/abort operation |
| __readonly__ | (Optional) Readonly |
| vsan | (Optional) Vsan |
| last_action_timestamp | (Optional) Last action timestamp |
| last_action | (Optional) Last action |
| last_action_result | (Optional) Last action result |
| last_action_failure_reason | (Optional) Last action failure reason |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1778922825

---

# Command: show fctimer status

## Syntax
```
show fctimer status [ __readonly__ <Distribution> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| status | cfs distribution is enabled or disabled |
| __readonly__ | (Optional) read only |
| Distribution | (Optional) distribution |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp8433263570

---

# Command: show fctimer vsan

## Syntax
```
show fctimer vsan <i0> [ __readonly__ { TABLE_fctimer <vsan-no> <F_S_TOV> <D_S_TOV> <E_D_TOV> <R_A_TOV> } [ <non-exist-vsan>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fctimer | show Fibre Channel timers |
| vsan | Specify VSAN id |
| i0 | VSAN id range |
| __readonly__ | (Optional) Read only |
| TABLE_fctimer | (Optional) table |
| vsan-no | (Optional) vsan number |
| F_S_TOV | (Optional) F_S_TOV |
| D_S_TOV | (Optional) D_S_TOV |
| E_D_TOV | (Optional) E_D_TOV |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2976272101

---

# Command: show feature-set

## Syntax
```
show feature-set [ <name> ] [ <id> ] [ __readonly__ TABLE_cfcFeatureSetTable <cfcFeatureSetIndex> <cfcFeatureSetName> <cfcFeatureSetAction>
 <cfcFeatureSetLastAction> <cfcFeatureSetLastActionResult> <cfcFeatureSetLastFailureReason> <cfcFeatureSetOpStatus> <cfcFeatureSetOpStatusReason>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| feature-set | Show feature set status |
| name | (Optional) feature-set name |
| id | (Optional) feature-set id |
| __readonly__ | (Optional) |
| TABLE_cfcFeatureSetTable | (Optional) feature-set table |
| cfcFeatureSetIndex | (Optional) feature-set table index |
| cfcFeatureSetName | (Optional) feature-set name |
| cfcFeatureSetAction | (Optional) action |
| cfcFeatureSetLastAction | (Optional) last action |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1333112240

---

# Command: show feature-set services

## Syntax
```
show feature-set services <s0> [ __readonly__ [ { TABLE_services <service_name> } ] { <count> <feature_set> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| feature-set | Show feature set status |
| services | Show services in feature set |
| __readonly__ | (Optional) |
| TABLE_services | (Optional) all service names in feature set |
| service_name | (Optional) name of the service |
| count | (Optional) number of services in the feature set |
| feature_set | (Optional) feature set name |
| s0 | Name of feature set |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3835925494

---

# Command: show feature

## Syntax
```
show feature [ __readonly__ [ { TABLE_cfcFeatureCtrlTable <cfcFeatureCtrlIndex2> <cfcFeatureCtrlInstanceNum2> <cfcFeatureCtrlName2>
 <cfcFeatureCtrlAction2> <cfcFeatureCtrlLastAction2> <cfcFeatureCtrlLastActionResult2> <cfcFeatureCtrlLastFailureReason2> <cfcFeatureCtrlOpStatus2>
 <cfcFeatureCtrlOpStatusReason2> <cfcFeatureCtrlTag2> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| feature | Show feature status |
| __readonly__ | (Optional) |
| TABLE_cfcFeatureCtrlTable | (Optional) feature table |
| cfcFeatureCtrlIndex2 | (Optional) feature table index |
| cfcFeatureCtrlInstanceNum2 | (Optional) instance number |
| cfcFeatureCtrlName2 | (Optional) feature name |
| cfcFeatureCtrlAction2 | (Optional) Action to be triggered for the feature |
| cfcFeatureCtrlLastAction2 | (Optional) Last action triggered for the feature |
| cfcFeatureCtrlLastActionResult2 | (Optional) The result of execution of the last action |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3735366530

---

# Command: show fhrp

## Syntax
```
show fhrp [ <intf> ] [ __readonly__ { TABLE_brief <intf_name> <intf_state> <ipv4_state> <ipv6_state> <hardware_status> <refcount>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fhrp | FHRP Show commands |
| show | Show running system information |
| intf | (Optional) Specify a single interface |
| __readonly__ | (Optional) |
| TABLE_brief | (Optional) Show brief FHRP interface information |
| intf_name | (Optional) Interface name |
| intf_state | (Optional) Interface state |
| ipv4_state | (Optional) Interface IPv4 state |
| ipv6_state | (Optional) Interface IPv6 state |
| hardware_status | (Optional) Interface hardware status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1779842615

---

# Command: show fhrp verbose

## Syntax
```
show fhrp [ <intf> ] verbose [ __readonly__ { TABLE_det <intf_name> <handle> <refcount> { TABLE_clients <client_id> <client_name>
 } <running> <expired> <v_retries> <v_time> <r_delay> <min_delay> <remaining_delay> <i_state> <ipv4_state> <ipv6_state> <h_state>
 <int_l2> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| fhrp | FHRP Show commands |
| show | Show running system information |
| intf | (Optional) Specify a single interface |
| verbose | Display detailed information |
| __readonly__ | (Optional) |
| TABLE_det | (Optional) Detailed FHRP interface information |
| intf_name | (Optional) Interface name |
| handle | (Optional) Interface handle |
| refcount | (Optional) Reference count |
| TABLE_clients | (Optional) FHRP clients present on interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1919392147

---

# Command: show file

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| file | Displays content of files |
| uri0 | Filename to be displayed |
| cksum | (Optional) Displays CRC checksum for a file |
| md5sum | (Optional) Displays MD5 checksum for a file |
| sha256sum | (Optional) Displays SHA256 checksum for a file |
| sha512sum | (Optional) Displays SHA512 checksum for a file |
| __readonly__ | (Optional) Read only |
| file_content | (Optional) uri file content buffer string |
| file_content_cksum | (Optional) uri file content checksum |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3076486049

---

# Command: show fips status

## Syntax
```
show fips status [ __readonly__ { operation_status <o_status> } { mode_state <m_state> } [ TABLE_sessions <lc_num> <lc_status>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fips | Show if FIPS mode is enabled or disabled |
| status | Whether FIPS mode is enabled or disabled |
| __readonly__ | (Optional) |
| operation_status | (Optional) run-time information about fips |
| o_status | (Optional) operational status of fips |
| mode_state | (Optional) mode state |
| m_state | (Optional) fips or non-fips state |
| TABLE_sessions | (Optional) all lc status |
| lc_num | (Optional) the lc number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp2591093861

---

# Command: show flow cache

## Syntax
```
show flow cache [ ipv4 &#124; ipv6 &#124; ce ] [ __readonly__ TABLE_flow_cache <flow-type> <source-ip> <destination-ip> <bridge-domain-id>
 <source-port> <destination-port> <protocol> <ipv6-flowlabel> <byte-count> <packet-count> <tcp-flags> <tos> <if-id> <flow-start>
 <flow-end> <source-mac> <destination-mac> <ether-type> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| cache | Show NetFlow Exporter Cache |
| ipv4 | (Optional) Show ipv4 cache entries |
| ipv6 | (Optional) Show ipv6 cache entries |
| ce | (Optional) Show ce cache entries |
| __readonly__ | (Optional) |
| TABLE_flow_cache | (Optional) The XML flow cache table |
| flow-type | (Optional) Flow type - v4,v6 or MAC |
| source-ip | (Optional) Source IP |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2028068830

---

# Command: show flow cache

## Syntax
```
show flow cache [ ipv4 &#124; ipv6 &#124; ce ] [ __readonly__ [ { TABLE_flow_cache <flow-cache-index> [ <flow-type> ] [ <source-ip>
 ] [ <destination-ip> ] [ <source-mac> ] [ <destination-mac> ] [ <bridge-domain-id> ] [ <ether-type> ] [ <source-port> ] [
 <destination-port> ] [ <protocol> ] [ <ipv6-flowlabel> ] [ <byte-count> ] [ <packet-count> ] [ <tcp-flags> ] [ <tos> ] [ <if-id>
 ] [ <output-if-id> ] [ <flow-start> ] [ <flow-end> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| cache | Show NetFlow Exporter Cache |
| ipv4 | (Optional) Show ipv4 cache entries |
| ipv6 | (Optional) Show ipv6 cache entries |
| ce | (Optional) Show ce cache entries |
| __readonly__ | (Optional) |
| TABLE_flow_cache | (Optional) The XML flow cache table |
| flow-cache-index | (Optional) Flow Index |
| flow-type | (Optional) Flow type - v4,v6 or MAC |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2111842839

---

# Command: show flow exporter

## Syntax
```
show flow exporter [ name ] [ <exporter> ] [ __readonly__ { TABLE_flow_exporter <exporter> <description> <dest> <vrf> <vrf_id>
 <vrf_resolved> <dest_udp> <source_intf> <source_ip> <dscp> <exp_vers> <seqnum> <samp_table_to> <if_table_to> <stats_to> <temp_to>
 <rec_sent> <temp_sent> <pkts_sent> <bytes_sent> <dest_unreach> <buff_events> <pkts_drop_no_route> <pkts_drop_other> <pkts_drop_lc_rp>
 <pkts_drop_op_drops> <time_last_cleared> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| exporter | Show NetFlow Exporter Configuration and Statistics |
| name | (Optional) Show a specific Flow Exporter |
| exporter | (Optional) Specify an exporter |
| __readonly__ | (Optional) |
| TABLE_flow_exporter | (Optional) |
| exporter | (Optional) |
| description | (Optional) |
| dest | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4012861333

---

# Command: show flow exporter

## Syntax
```
show flow exporter [ name ] [ <exporter> ] [ __readonly__ { TABLE_flow_exporter <exporter> <description> <dest> <vrf> <vrf_id>
 <vrf_resolved> <dest_udp> <source_intf> <source_ip> <dscp> <exp_vers> <seqnum> <samp_table_to> <if_table_to> <stats_to> <temp_to>
 <rec_sent> <temp_sent> <pkts_sent> <bytes_sent> <dest_unreach> <buff_events> <pkts_drop_no_route> <pkts_drop_other> <pkts_drop_lc_rp>
 <pkts_drop_op_drops> <time_last_cleared> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| exporter | Show NetFlow Exporter Configuration and Statistics |
| name | (Optional) Show a specific Flow Exporter |
| exporter | (Optional) Specify an exporter |
| __readonly__ | (Optional) |
| TABLE_flow_exporter | (Optional) |
| exporter | (Optional) |
| description | (Optional) |
| dest | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3023857366

---

# Command: show flow filter

## Syntax
```
show flow filter [ __readonly__ [ { TABLE_flow_filter <name> <ipv4acl> <ipv6acl> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show Analytics information |
| filter | Show filter Configuration |
| __readonly__ | (Optional) |
| TABLE_flow_filter | (Optional) flow filter data |
| name | (Optional) Filter Name |
| ipv4acl | (Optional) IPv4 ACL |
| ipv6acl | (Optional) IPv4 ACL |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2036701502

---

# Command: show flow interface

## Syntax
```
show flow { interface [ <intf> ] &#124; vlan [ <vlan> ] } [ __readonly__ [ { TABLE_flow_interface [ <intf_name> ] [ <vlan_id> ]
 [ <v4in_mon_name> ] [ <v4in_direction> ] [ <v4in_profile_id> ] [ <v6in_mon_name> ] [ <v6in_direction> ] [ <v6in_profile_id>
 ] [ <l2in_mon_name> ] [ <l2in_direction> ] [ <l2in_profile_id> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| interface | Flow interface information |
| intf | (Optional) Interface |
| vlan | Flow vlan information |
| vlan | (Optional) Vlan number |
| __readonly__ | (Optional) |
| TABLE_flow_interface | (Optional) flow interface data |
| intf_name | (Optional) Interface |
| vlan_id | (Optional) VLAN ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp5086476130

---

# Command: show flow monitor

## Syntax
```
show flow monitor [ name ] [ <monitor> [ cache [ detailed ] ] ] [ __readonly__ [ { TABLE_flow_monitor <monitor> <use_count>
 [ <description> ] <record> <exporter1> <exporter2> <bucket_id> <src_addr> <dest_addr> <direction> <pkt_count> <byte_count>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| monitor | Show Monitor Configuration |
| name | (Optional) Show a specific Flow Monitor |
| monitor | (Optional) Specify a monitor |
| cache | (Optional) Flow monitor cache contents |
| detailed | (Optional) Show the entire cache contents |
| __readonly__ | (Optional) |
| TABLE_flow_monitor | (Optional) |
| monitor | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2670869312

---

# Command: show flow monitor

## Syntax
```
show flow monitor [ name ] [ <monitor> [ cache [ detailed ] ] ] [ __readonly__ [ { TABLE_flow_monitor <monitor> <use_count>
 [ <description> ] <record> <exporter1> <exporter2> <bucket_id> <src_addr> <dest_addr> <direction> <pkt_count> <byte_count>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| monitor | Show Monitor Configuration |
| name | (Optional) Show a specific Flow Monitor |
| monitor | (Optional) Specify a monitor |
| cache | (Optional) Flow monitor cache contents |
| detailed | (Optional) Show the entire cache contents |
| __readonly__ | (Optional) |
| TABLE_flow_monitor | (Optional) |
| monitor | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3880562989

---

# Command: show flow profile

## Syntax
```
show flow profile [ __readonly__ [ { TABLE_flow_profile <name> [ <desc> ] <number-of-users> <export-intvl> <source-port> <packet-id-shift>
 <burst-intvl-shift> <mtu> [ <guess-threshold-lo> ] [ <guess-threshold-hi> ] [ { TABLE_payload_bin <payload-bin-num> <payload-bin-lo>
 <payload-bin-hi> } ] [ { TABLE_tcpopthdr_bin <tcpopthdr-bin-num> <tcpopthdr-bin-lo> <tcpopthdr-bin-hi> } ] [ { TABLE_rcvwinsize_bin
 <rcvwinsize-bin-num> <rcvwinsize-bin-lo> <rcvwinsize-bin-hi> } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show Analytics information |
| profile | Show profile Configuration |
| __readonly__ | (Optional) |
| TABLE_flow_profile | (Optional) HW flow profile |
| name | (Optional) HW profile name |
| desc | (Optional) Description of HW profile |
| number-of-users | (Optional) No. of users |
| export-intvl | (Optional) Export Interval |
| source-port | (Optional) Source Port |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3719550250

---

# Command: show flow record

## Syntax
```
show flow record [ name ] [ { <record> } &#124; { netflow-original } &#124; { netflow { protocol-port &#124; layer2-switched { input } &#124;
 { ipv4 &#124; ipv6 &#124; l2 } { original-input } } } ] [ __readonly__ [ { TABLE_flow_record <record> [ <description> ] <use_count>
 <template> [ <match_ip_src> ] [ <match_ip_dst> ] [ <match_proto> ] [ <match_tos> ] [ <match_l4_src> ] [ <match_l4_dst> ] [
 <match_ingress> ] [ <match_egress> ] [ <match_src_as_peer> ] [ <match_dst_as_peer> ] [ <match_ipv6_src> ] [ <match_ipv6_dst>
 ] [ <match_ipv6_flow> ] [ <match_ipv6_option> ] [ <match_ipv6_traffic> ] [ <match_l2_src> ] [ <match_l2_dst> ] [ <match_l2_src_vlan>
 ] [ <match_l2_dst_vlan> ] [ <match_l2_1q> ] [ <match_l2_cos> ] [ <match_l2_etype> ] [ <match_flow_dir_match> ] [ <match_ipv4v6_src>
 ] [ <match_ipv4v6_dst> ] [ <collect_src_as> ] [ <collect_dst_as> ] [ <collect_src_as_peer> ] [ <collect_dst_as_peer> ] [ <collect_fwd_status>
 ] [ <collect_ipv4_next_hop> ] [ <collect_ipv4_bgp_next> ] [ <collect_ipv6_next_hop> ] [ <collect_ipv6_bgp_next> ] [ <collect_tcp_flags>
 ] [ <collect_flow_dir> ] [ <collect_bytes> ] [ <collect_bytes_long> ] [ <collect_packets> ] [ <collect_packets_long> ] [ <collect_time_first>
 ] [ <collect_time_last> ] [ <collect_ingress_coll> ] [ <collect_egress_coll> ] [ <collect_sampler_id> ] [ <collect_ip_ver>
 ] [ <collect_packet_disp> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| record | Show Record Configuration |
| name | (Optional) Show the configuration for a specific Flow Record |
| record | (Optional) Specify a record |
| netflow-original | (Optional) Traditional IPv4 input NetFlow with origin ASs |
| netflow | (Optional) Traditional NetFlow collection schemes |
| ipv4 | (Optional) IPv4 collection schemes |
| ipv6 | (Optional) IPv6 collection schemes |
| l2 | (Optional) L2 collection schemes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1131621202

---

# Command: show flow record

## Syntax
```
show flow record [ name ] [ { <record> } &#124; { netflow-original } &#124; { netflow { protocol-port &#124; layer2-switched { input } &#124;
 { ipv4 &#124; ipv6 &#124; l2 } { original-input } } } ] [ __readonly__ [ { TABLE_flow_record <record> [ <description> ] <use_count>
 <template> [ <match_ip_src> ] [ <match_ip_dst> ] [ <match_proto> ] [ <match_tos> ] [ <match_l4_src> ] [ <match_l4_dst> ] [
 <match_ingress> ] [ <match_egress> ] [ <match_src_as_peer> ] [ <match_dst_as_peer> ] [ <match_ipv6_src> ] [ <match_ipv6_dst>
 ] [ <match_ipv6_flow> ] [ <match_ipv6_option> ] [ <match_ipv6_traffic> ] [ <match_l2_src> ] [ <match_l2_dst> ] [ <match_l2_src_vlan>
 ] [ <match_l2_dst_vlan> ] [ <match_l2_1q> ] [ <match_l2_cos> ] [ <match_l2_etype> ] [ <match_flow_dir_match> ] [ <match_ipv4v6_src>
 ] [ <match_ipv4v6_dst> ] [ <collect_src_as> ] [ <collect_dst_as> ] [ <collect_src_as_peer> ] [ <collect_dst_as_peer> ] [ <collect_fwd_status>
 ] [ <collect_ipv4_next_hop> ] [ <collect_ipv4_bgp_next> ] [ <collect_ipv6_next_hop> ] [ <collect_ipv6_bgp_next> ] [ <collect_tcp_flags>
 ] [ <collect_flow_dir> ] [ <collect_bytes> ] [ <collect_bytes_long> ] [ <collect_packets> ] [ <collect_packets_long> ] [ <collect_time_first>
 ] [ <collect_time_last> ] [ <collect_ingress_coll> ] [ <collect_egress_coll> ] [ <collect_sampler_id> ] [ <collect_ip_ver>
 ] [ <collect_packet_disp> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| record | Show Record Configuration |
| name | (Optional) Show the configuration for a specific Flow Record |
| record | (Optional) Specify a record |
| netflow-original | (Optional) Traditional IPv4 input NetFlow with origin ASs |
| netflow | (Optional) Traditional NetFlow collection schemes |
| ipv4 | (Optional) IPv4 collection schemes |
| ipv6 | (Optional) IPv6 collection schemes |
| l2 | (Optional) L2 collection schemes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3320649455

---

# Command: show flow rtp

## Syntax
```
show flow rtp { errors { active &#124; history } &#124; details } [ ipv4 &#124; ipv6 ] [ __readonly__ [ <flow-timeout> ] [ { TABLE_flow_rtp
 <flow-rtp-index> [ <flow-type> ] [ <source-ip> ] [ <destination-ip> ] [ <bridge-domain-id> ] [ <source-port> ] [ <destination-port>
 ] [ <protocol> ] [ <packet-count> ] [ <bytes-per-sec> ] [ <start-time> ] [ <if-name> ] [ { TABLE_flow_rtp_errors <loss-start>
 [ <loss-end> ] [ <packet-loss> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| rtp | Real-time Transport Protocol |
| errors | Show NetFlow RTP flows error information |
| active | Show RTP flows with active losses |
| history | Show RTP flows with loss history |
| details | Show NetFlow RTP detailed information |
| ipv4 | (Optional) Show ipv4 RTP entries |
| ipv6 | (Optional) Show ipv6 RTP entries |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3102097946

---

# Command: show flow rtp timeout

## Syntax
```
show flow rtp timeout [ __readonly__ { <flush_cache_to> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| rtp | Real-time Transport Protocol |
| timeout | Show NetFlow RTP flow error monitoring timeout values |
| __readonly__ | (Optional) |
| flush_cache_to | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1657842868

---

# Command: show flow system

## Syntax
```
show flow system [ __readonly__ <system_exporter_id> [ { TABLE_flow_interface [ <intf_name> ] [ <exporter_id> ] [ <profile_name>
 ] [ <v4in_mon_name> ] [ <v4in_direction> ] [ <v6in_mon_name> ] [ <v6in_direction> ] [ <filter_name> ] [ <ipv4_hit> ] [ <ipv4_create>
 ] [ <ipv6_hit> ] [ <ipv6_create> ] [ <ce_hit> ] [ <ce_create> ] [ <packets_seen> ] [ <skip_collect> ] [ <export_count> ] }
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show Analytics information |
| system | Show system Configuration |
| __readonly__ | (Optional) |
| system_exporter_id | (Optional) System Exporter ID |
| TABLE_flow_interface | (Optional) flow interface data |
| intf_name | (Optional) Interface |
| exporter_id | (Optional) Exporter ID |
| profile_name | (Optional) HW Profile Name |
| v4in_mon_name | (Optional) IPv4 Input monitor name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1037189184

---

# Command: show flow timeout

## Syntax
```
show flow timeout [ __readonly__ [ <active_to> ] [ <inactive_to> ] [ <fast_to> ] [ <th_pkts> ] [ <agg_age_to> ] <flush_cache_to>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| timeout | Show NetFlow flow cache timeout values |
| __readonly__ | (Optional) |
| active_to | (Optional) |
| inactive_to | (Optional) |
| fast_to | (Optional) |
| th_pkts | (Optional) |
| agg_age_to | (Optional) |
| flush_cache_to | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3706309375

---

# Command: show flow tracer

## Syntax
```
show flow tracer [ __readonly__ [ { TABLE_flow_tracer <flow-tracer-index> [ <source-ip> ] [ <destination-ip> ] [ <bridge-domain-id>
 ] [ <source-port> ] [ <destination-port> ] [ <protocol> ] [ <packet-count> ] [ <if-name> ] [ <fwd-drop> ] [ <rpf-fail> ] [
 <policing-drop> ] [ <ids-drop> ] [ <policy-drop> ] [ <buffer-drop> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| flow | Show NetFlow information |
| tracer | Show packet tracer information |
| __readonly__ | (Optional) |
| TABLE_flow_tracer | (Optional) |
| flow-tracer-index | (Optional) Flow Index |
| source-ip | (Optional) Source IP |
| destination-ip | (Optional) Destination IP |
| bridge-domain-id | (Optional) Bridge Domain ID |
| source-port | (Optional) Source Port |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2646505740

---

# Command: show forwarding

## Syntax
```
show forwarding [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; <vrf-all> } &#124; table <table_id> ] [ ipv4 ] [ route &#124; rnhdb ] [ recursive
 ] [ summary &#124; [ [ detail &#124; platform &#124; partial &#124; ipsg ] [ max-display-count <display_count> ] ] &#124; [ <prefix> [ longer-prefixes
 ] [ detail &#124; platform ] &#124; <address> [ detail &#124; platform ] &#124;
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table id in hex |
| ipv4 | (Optional) ipv4 |
| route | (Optional) display IP routing table |
| ipsg | (Optional) display IPv4 IPSG routes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2403888408

---

# Command: show forwarding adjacency

## Syntax
```
show forwarding [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; <vrf-all> } ] [ ipv4 ] adjacency [ mpls ] [ lisp ] [ nve ] [ <aif>
 ] [ <anh> ] [ detail &#124; stats &#124; platform ] [ module <module> ] [ __readonly__ [ <adj-count> ] [ TABLE_adj { [ <fec> ] [ <nexthop>
 ] [ <intf> ] [ <rewinfo> ] [ <interface> ] [ <bgp_rnh> ] [ <bgp_orig_as> ] [ <bgp_peer_as> ] [ <pkts> ] [ <bytes> ] [ <exp>
 ] [ <src_addr> ] [ <dest_addr> ] [ <lisp_flags> ] [ <lisp_inst_id> ] [ <pltfm_key> ] [ <hh> ] [ <refcount> ] } ] [ TABLE_ip_adjacency
 { [ <nh> ] [ <rwinfo> ] [ <intf> ] [ <intf_idx> ] [ <hhandle> ] [ <refcnt> ] [ <flags> ] [ <holder> ] [ <pbr_cnt> ] [ <wccp_cnt>
 ] [ <rewrite-p> ] [ TABLE_index { [ <hw_adj> ] [ <cmn-idx> ] [ <lif> ] [ <buf-idx> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| ipv4 | (Optional) ipv4 |
| adjacency | display adjacency information |
| platform | (Optional) one command to show pi and pd info together |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| mpls | (Optional) mpls adjacency information |
| lisp | (Optional) LISP adjacency information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp8903620640

---

# Command: show forwarding distribution clients

## Syntax
```
show forwarding distribution clients [ __readonly__ <id><pid><name><shms><shme><shmn> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | fib distribution info |
| clients | unicast client information |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3805179550

---

# Command: show forwarding distribution fib-state

## Syntax
```
show forwarding distribution fib-state [ __readonly__ <slot> <state><ttc><tprc><tv4ac><tv6ac> { TABLE_fib_state <tid><tafi><prc><pc><tname>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | fib distribution info |
| fib-state | unicast fib state info |
| __readonly__ | (Optional) |
| slot | (Optional) slot number |
| TABLE_fib_state | (Optional) fib-state table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4206513284

---

# Command: show forwarding distribution ip igmp snooping

## Syntax
```
show forwarding distribution ip igmp snooping [ vlan <vlan-id> [ group [ <grpaddr> &#124; <mac-grpaddr> ] [ source <srcaddr> ]
 ] ] [ detail ] [ __readonly__ <refcount> <oiflist_id> <last_oiflist_id> <ftag-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| ip | IPV4 information |
| igmp | MFDM IGMP information |
| snooping | L2 mcast snooping related information |
| vlan | (Optional) Info specific to a vlan |
| vlan-id | (Optional) Vlan id value |
| group | (Optional) Group specific information |
| grpaddr | (Optional) Group address |
| mac-grpaddr | (Optional) Group MAC address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp2469206217

---

# Command: show forwarding distribution ipv6 multicast route

## Syntax
```
show forwarding distribution ipv6 multicast route [ table <table_id> &#124; vrf <vrf-name> ] [ [ group { <group> } ] [ source {
 <source> } ] &#124; summary ] [ __readonly__ TABLE_vrf [ <vrf-name> ] [ <table-name> ] [ <table-id> ] [ <total-num-groups> ] [
 TABLE_route_summary [ <vrf-name> ] [ <total-num-routes> ] [ <num-star-g-route> ] [ <num-sg-route> ] [ <num-star-g-prfx> ]
 [ <num-group-count> ] ] [ TABLE_one_route [ <source-addrs> ] [ <source-len> ] [ <group-addrs> ] [ <group-len> ] [ <df-ordinal>
 ] [ <rpf-intf> ] [ <flags> ] [ <stats-pkts> ] [ <stats-bytes> ] [ <oif-count> ] [ <oiflist-index> ] [ TABLE_oif [ <oif-name>
 ] [ <mti-src-intf> ] [ <mti-grp-ip> ] [ <mti-src-ip> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | display fib distribution information |
| ipv6 | IPV6 related information |
| multicast | display IPv6 multicast information |
| route | display routing table |
| vrf | (Optional) display routes for a specific VRF |
| vrf-name | (Optional) VRF name |
| table | (Optional) table |
| table_id | (Optional) table number |
| group | (Optional) Multicast IPv6 Group Address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp5168165850

---

# Command: show forwarding distribution l2 multicast

## Syntax
```
show forwarding distribution l2 multicast [ ip-based &#124; mac-based ] [ vlan <vlan-id> [ { group <grpaddr> [ source <srcaddr>
 ] } &#124; destination-mac <dmac> ] ] [ summary ] [ __readonly__ [ TABLE_sum [ <mode> ] [ <num_vlan> ] [ <num_starg> ] [ <num_sg>
 ] [ <num_aggstarg> ] [ TABLE_sum_info [ <ftag_id> ] [ <vlan_id> ] [ <routable_flag> ] [ <num_starg> ] [ <num_sg> ] [ <num_aggstarg>
 ] [ <total_route> ] ] ] [ TABLE_route [ <vlan> ] [ <grp_str> ] [ <src_str> ] [ <grp_mac> ] [ <src_mac> ] [ TABLE_oif [ <oiflist_id>
 ] [ <refcount> ] [ <l3_usage> ] [ <plt_index> ] [ <num_oif> ] [ <oif_name> ] [ <flags> ] [ <dvif> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| l2 | L2 information |
| multicast | L2 multicast information |
| ip-based | (Optional) IPv4 based |
| mac-based | (Optional) MAC based |
| vlan | (Optional) Info specific to a vlan |
| vlan-id | (Optional) Vlan id value |
| group | (Optional) Group specific information |
| grpaddr | (Optional) Group address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2097481530

---

# Command: show forwarding distribution lisp counters

## Syntax
```
show forwarding distribution lisp counters [ __readonly__ <count> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | fib distribution information |
| lisp | for lisp application |
| counters | counters |
| __readonly__ | (Optional) |
| count | (Optional) count |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2134581667

---

# Command: show forwarding distribution lisp vrf enabled

## Syntax
```
show forwarding distribution lisp vrf enabled [ __readonly__ { TABLE_lisp_vrf_enabled <vrf> <lisp_enabled> <req_id> <operation>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | fib distribution information |
| lisp | for lisp application |
| vrf | vrf |
| enabled | enabled |
| __readonly__ | (Optional) |
| TABLE_lisp_vrf_enabled | (Optional) |
| vrf | (Optional) vrf key |
| lisp_enabled | (Optional) lisp enabled status |
| req_id | (Optional) req id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3928341139

---

# Command: show forwarding distribution multicast

## Syntax
```
show forwarding distribution multicast [ messages ] [ __readonly__ <num_accepting_routes> <slot> <fibstate> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast FIB distribution information |
| messages | (Optional) Outstanding Message Information |
| __readonly__ | (Optional) |
| num_accepting_routes | (Optional) Number of fibs accepting routes |
| slot | (Optional) Slot |
| fibstate | (Optional) IP Multicast FIB process state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp5024107390

---

# Command: show forwarding distribution multicast client-ack-db

## Syntax
```
show forwarding distribution multicast client-ack-db [ __readonly__ <xid> <num_recepients> <num_responses> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast |
| client-ack-db | Displays the client ack db |
| __readonly__ | (Optional) |
| xid | (Optional) XID |
| num_recepients | (Optional) Number of recepients |
| num_responses | (Optional) Number of responses |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1680147150

---

# Command: show forwarding distribution multicast client

## Syntax
```
show forwarding distribution multicast client [ __readonly__ <num-clients> <client-name> <client-id> <shmem-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast information |
| client | Show multicast distribution client information |
| __readonly__ | (Optional) |
| num-clients | (Optional) Number of Clients registered |
| client-name | (Optional) Client Name |
| client-id | (Optional) Client-id |
| shmem-name | (Optional) Shared Memory Segment Name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1641637255

---

# Command: show forwarding distribution multicast download

## Syntax
```
show forwarding distribution multicast download
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | forwarding information |
| distribution | FIB distribution information |
| multicast | Multicast FIB distribution information |
| download | show download queues |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3097376011

---

# Command: show forwarding distribution multicast mfib

## Syntax
```
show forwarding distribution multicast { mfib-txlist [ vrf <vrf-name> ] &#124; mfib-buffers } [ __readonly__ <no-free-buffers>
 <no-used-buffers> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast information |
| mfib-txlist | Show MFIB transmission-list information |
| vrf | (Optional) Specify VRF |
| vrf-name | (Optional) Specify VRF name |
| mfib-buffers | Show MFIB route buffer information |
| __readonly__ | (Optional) |
| no-free-buffers | (Optional) Number of Free txlist MFIB buffers |
| no-used-buffers | (Optional) Number of Used txlist MFIB buffers |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4092310500

---

# Command: show forwarding distribution multicast outgoing-interface-list

## Syntax
```
show forwarding distribution multicast outgoing-interface-list { L2 &#124; L3 &#124; OTV } [ <index> ] [ __readonly__ [ <total_oif>
 ] [ TABLE_oif [ <oiflist_id> ] [ <refcount> ] [ <l3_usage> ] [ <plt_index> ] [ <num_oif> ] [ <oif_name> ] [ <flags> ] [ <dvif>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast FIB distribution information |
| outgoing-interface-list | Outgoing interface list |
| L2 | Layer 2 oiflist |
| L3 | Layer 3 oiflist |
| OTV | OTV oiflist |
| index | (Optional) Outgoing Interface List index |
| __readonly__ | (Optional) |
| total_oif | (Optional) Total outgoing interface list |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3360622475

---

# Command: show forwarding distribution multicast outgoing-interface-list L2_PRIME

## Syntax
```
show forwarding distribution multicast outgoing-interface-list L2_PRIME [ <index> ] [ __readonly__ <dvif> <platform_index>
 <ref_count> <l2-oifs> <port_set> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast FIB distribution information |
| outgoing-interface-list | Outgoing interface list |
| L2_PRIME | Layer 2 oiflist |
| index | (Optional) Outgoing Interface List index |
| __readonly__ | (Optional) |
| dvif | (Optional) Destination VIF |
| platform_index | (Optional) Platform index |
| ref_count | (Optional) Reference count |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2003235533

---

# Command: show forwarding distribution multicast resp-ack-timer-msgs

## Syntax
```
show forwarding distribution multicast resp-ack-timer-msgs
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast information |
| resp-ack-timer-msgs | show response ack timers for MFDM |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp6967850500

---

# Command: show forwarding distribution multicast route

## Syntax
```
show forwarding distribution [ ip ] multicast route [ table <id> &#124; vrf { <vrf_name> &#124; <vrf-known-name> &#124; all } ] [ [ group
 { <gaddr> [ <mask> ] &#124; <gprefix> } ] [ source { <saddr> [ <smask> ] &#124; <sprefix> } ] &#124; summary ] [ __readonly__ TABLE_vrf [
 <vrf-name> ] [ <table-name> ] [ <table-id> ] [ <table-wildcard> ] [ <total-num-groups> ] [ TABLE_route_summary [ <vrf-name>
 ] [ <total-num-routes> ] [ <num-star-g-route> ] [ <num-sg-route> ] [ <num-star-g-prfx> ] [ <num-group-count> ] ] [ TABLE_one_route
 [ <source-addrs> ] [ <source-len> ] [ <group-addrs> ] [ <group-len> ] [ <df-ordinal> ] [ <rpf-intf> ] [ <flags> ] [ <stats-pkts>
 ] [ <stats-bytes> ] [ <oif-count> ] [ <oiflist-index> ] [ TABLE_oif [ <oif-name> ] [ <mti-src-intf> ] [ <mti-grp-ip> ] [ <mti-src-ip>
 ] [ <next-hop> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| ip | (Optional) IPV4 information |
| multicast | Multicast information |
| route | Multicast route related information |
| vrf | (Optional) Specify VRF |
| vrf_name | (Optional) Specify VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| table | (Optional) Specify Multicast Routing Table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2959314527

---

# Command: show forwarding distribution multicast vxlan dsg-db

## Syntax
```
show forwarding distribution multicast vxlan dsg-db
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | Display Forwarding Information |
| distribution | FIB distribution information |
| multicast | Multicast |
| vxlan | vxlan |
| dsg-db | delivery group/source db |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1606992015

---

# Command: show forwarding distribution nve overlay-vlan

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| forwarding | forwarding information |
| distribution | fib distribution info |
| nve | nve distribution info |
| overlay-vlan | overlay-vlan adjacency info |
| __readonly__ | (Optional) |
| TABLE_overlay_vlan_peer_id | (Optional) overlay vlan peer id table |
| Vlan | (Optional) VLAN |
| SVP | (Optional) SVP |
| install | (Optional) install |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1565218278

---

# Command: show forwarding distribution peer-id

## Syntax
```
show forwarding distribution peer-id [ vpls &#124; otv ] [ __readonly__ <header> TABLE_peer_id <app> <vlan> <id> <peer_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| forwarding | forwarding information |
| distribution | fib distribution info |
| peer-id | HW Peer-id allocation info |
| vpls | (Optional) VPLS |
| otv | (Optional) OTV |
| __readonly__ | (Optional) |
| header | (Optional) Header |
| TABLE_peer_id | (Optional) Peer ID table |
| app | (Optional) OTV/VPLS |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1266842313

---

# Command: show forwarding distribution trace

## Syntax
```
show forwarding distribution trace
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display Forwarding Information |
| distribution | fib distribution info |
| trace | unicast trace information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp7817513430

---

# Command: show forwarding ecmp

## Syntax
```
show forwarding ecmp [ { [ vrf { <vrf-name> &#124; <vrf-known-name> } ] lisp } ] [ platform ] [ module <module> ] [ partial ] [
 __readonly__ [ <header> <ecmp_hash> <intf> <nh> <v6nh> <hw_index> <num_mpls> <holder> <refcount> <num_paths> <sw_ptr> <ecmp_partial>
 ] [ TABLE_ecmp { [ <hash> ] [ <num_paths> ] [ <hwindex> ] [ <ecmppartial> ] [ TABLE_index { [ <ecmp_idx> ] [ <cmn_idx> ] }
 ] [ <refcnt> ] [ <ecmp_holder> ] } [ TABLE_adjacency { [ <intf> ] [ <nh> ] [ <v6nh> ] [ <hw_adj_idx> ] [ <hw_cmn_idx> ] [
 <lif> ] [ <hw_nve_adj_idx> ] [ <hw_nve_cmn_idx> ] [ <nve_lif> ] } ] [ <vobj_count> ] [ <vxlan_vobj_count> ] [ <vxlan> ] [
 <vobj_list_header> ] [ <vobj-id> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display fib information |
| ecmp | Show information about ECMPs |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| lisp | (Optional) Show information about LISP ECMPs |
| platform | (Optional) one command to show pi and pd info together |
| module | (Optional) slot |
| module | (Optional) slot number |
| partial | (Optional) Show partially installed ECMPs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1274386471

---

# Command: show forwarding ecmp recursive

## Syntax
```
show forwarding ecmp recursive [ platform ] [ max-display-count <display_count> ] [ module <module> ] [ partial ] [ __readonly__
 [ TABLE_vobj { [ <header_vobj> ] [ <header_ecmp> ] } [ TABLE_vobj_idx { [ <hw_vobj_index> ] [ <cmn_index> ] } ] [ <num_pfxs>
 ] [ <ecmp_partial> ] [ <activepath_hdr> ] [ TABLE_active { [ TABLE_activepath { [ <ap_nh> ] [ <ap_v6nh> ] [ <ap_rnh_len> ]
 [ <ap_nh_vpn_label> ] [ <ap_rnh_table_id> ] [ <ap_nh_weight> ] } ] } ] [ <backuppath_hdr> ] [ TABLE_backuppath { [ <bp_nh>
 ] [ <bp_v6nh> ] [ <bp_nh_vpn_label> ] [ <bp_rnh_table_id> ] [ <bp_nh_weight> ] } ] [ <cnh_hdr> ] [ TABLE_cnh { [ <nh> ] [
 <v6nh> ] [ <intf> ] [ TABLE_cnh_adj { [ <hw_adj> ] [ <hw_cmn_index> ] [ <lif> ] } ] } ] [ <hw_inst_n> ] [ <ls_count_n> ] [
 <hw_inst_o> ] [ <ls_count_o> ] [ <fec_type> ] [ <header_fec_ecmp> ] [ <hw_vobj_fec_idx> ] [ <cmn_idx> ] [ <vobj_hw_inst_n>
 ] [ <vobj_ls_count_n> ] [ <vobj_hw_inst_o> ] [ <vobj_ls_count_o> ] [ <vobj_refcount> ] [ TABLE_vobj_ecmp { [ <ec_hash> ] [
 <ec_num_paths> ] [ <ec_hwindex> ] [ <ec_ecmppartial> ] [ <ec_refcnt> ] [ <ec_ecmp_holder> ] } [ TABLE_adjacency_ec { [ <ec_intf>
 ] [ <ec_nh> ] [ <ec_v6nh> ] [ <ec_hw_adj_idx> ] [ <ec_hw_cmn_idx> ] [ <ec_lif> ] [ <ec_hw_nve_adj_idx> ] [ <ec_hw_nve_cmn_idx>
 ] [ <ec_nve_lif> ] } ] [ <ec_vobj_count> ] [ <ec_vxlan_vobj_count> ] [ <ec_vxlan> ] [ <ec_vobj_list_header> ] ] ] [ <header>
 <num_pfxs> <rnh_table_id> <nh> <rnh_len> <v6nh> <hw_instance> <nh_vpn_label> <nh_weight> <cnh_intf> <ecmp_partial> ] [ TABLE_ecmp
 { [ <hash> ] [ <num_paths> ] [ <hwindex> ] [ <ecmppartial> ] [ TABLE_index { [ <ecmp_idx> ] [ <cmn_idx> ] } ] [ <refcnt> ]
 [ <ecmp_holder> ] } [ TABLE_adjacency { [ <intf> ] [ <nh> ] [ <v6nh> ] [ <hw_adj_idx> ] [ <hw_cmn_idx> ] [ <lif> ] [ <hw_nve_adj_idx>
 ] [ <hw_nve_cmn_idx> ] [ <nve_lif> ] } ] [ <vobj_count> ] [ <vxlan_vobj_count> ] [ <vxlan> ] [ <vobj_list_header> ] [ TABLE_vobj_id
 { [ <vobj-id> ] } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Display fib information |
| ecmp | Show information about ECMPs |
| recursive | Show information about recursive ECMPs |
| platform | (Optional) one command to show pi and pd info together |
| module | (Optional) slot |
| partial | (Optional) Show partially installed ECMPs |
| module | (Optional) slot number |
| max-display-count | (Optional) displays max # of routes |
| display_count | (Optional) count |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2608441980

---

# Command: show forwarding interfaces

## Syntax
```
show forwarding interfaces [ module <module> ] [ __readonly__ TABLE_intf_str <intf> <v4adjcnt> <v6adjcnt> <v4rpfmode> <v6rpfmode>
 <mac> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | fib information |
| interfaces | show fib interface info |
| __readonly__ | (Optional) |
| TABLE_intf_str | (Optional) show interface string |
| intf | (Optional) interface name |
| module | (Optional) slot |
| module | (Optional) slot number |
| v4adjcnt | (Optional) count of v4 adjacencies |
| v6adjcnt | (Optional) count of v6 adjacencies |
| mac | (Optional) mac address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1904958842

---

# Command: show forwarding ipv6 adjacency

## Syntax
```
show forwarding [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; <vrf-all> } ] ipv6 adjacency [ mpls ] [ nve ] [ <aif> ] [ <anh> ]
 [ detail &#124; stats &#124; platform ] [ module <module> ] [ __readonly__ [ <adj-count> ] [ TABLE_adj { [ <fec> ] <nexthop> <rewinfo>
 [ <interface> ] [ <pkts> ] [ <bytes> ] [ <bgp_rnh> ] [ <bgp_orig_as> ] [ <bgp_peer_as> ] [ <hh> ] [ <refcount> ] } ] [ TABLE_v6_adj
 { [ <nh> ] [ <rwinfo> ] [ <intf> ] [ <intf_idx> ] [ <hh> ] [ <refcnt> ] [ <flags> ] [ <holder> ] [ <pbr_cnt> ] [ <wccp_cnt>
 ] [ TABLE_index { [ <hw_adj> ] [ <cmn-idx> ] [ <lif> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| ipv6 | ipv6 |
| adjacency | display adjacency information |
| platform | (Optional) one command to show pi and pd info together |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| mpls | (Optional) mpls adjacency information |
| nve | (Optional) nve adjacency information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp4018719694

---

# Command: show forwarding ipv6 inconsistency

## Syntax
```
show forwarding ipv6 [ unicast ] inconsistency [ suppress-transient ] [ vrf { <vrf-name> &#124; all_vrfs } ] [ module { <module>
 &#124; all_modules } ] [ __readonly__ [ <err_str> ] [ <cc_header> ] [ <table_id> ] [ <slot_id> ] [ <exec_time> ] [ <elapsed_time>
 ] [ <inconsis_adjs> ] [ TABLE_inconsistency_adjs { <idipv6> <slotipv6> [ <unitipv6> ] <vrfipv6> [ <ipv6addr> ] [ <ipv6prefix>
 ] [ <interfaceipv6> ] <reasonipv6> } ] [ <inconsis_routes> ] [ TABLE_inconsistency_routes { <idipv6> <slotipv6> [ <unitipv6>
 ] <vrfipv6> [ <ipv6addr> ] [ <ipv6prefix> ] [ <interfaceipv6> ] <reasonipv6> } ] [ <run_status> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | Display Forwarding Information |
| ipv6 | ipv6 |
| unicast | (Optional) unicast |
| inconsistency | route inconsistency check |
| suppress-transient | (Optional) Supress Transient state |
| vrf | (Optional) check routes for a specific VRF |
| vrf-name | (Optional) VRF name |
| module | (Optional) check routes for a specific module |
| module | (Optional) module number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp8580795390

---

# Command: show forwarding ipv6 multicast route

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| ipv6 | ipv6 |
| multicast | IPV6 related Multicast information |
| route | Multicast route information |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| tab_id | (Optional) table number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp1888988220

---

# Command: show forwarding ipv6 route

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table id in hex |
| ipv6 | ipv6 |
| route | display IP routing table |
| platform | (Optional) one command to show pi and pd info together |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp3034642294

---

# Command: show forwarding kvfib cache on

## Syntax
```
show forwarding kvfib cache { on &#124; off }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | fib information |
| kvfib | kvfib |
| cache | cache |
| on | set variable |
| off | reset variable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3251946450

---

# Command: show forwarding l2 multicast

## Syntax
```
show forwarding l2 multicast { [ { vlan <vlan-id> [ { group <grpaddr> source <srcaddr> } &#124; destination-mac <dstmac> ] } ]
 } [ vdc <vdc-id> ] [ module <num> ] [ __readonly__ [ TABLE_L2_MCAST_INFO <vlan_id> [ <group> ] [ <source> ] [ <dmac> ] <epoch>
 <resource_id> <dest_index> [ <hw_handle> ] [ <text> ] [ <value> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| forwarding | Forwarding information |
| l2 | L2 related information |
| multicast | Multicast related information |
| vlan | (Optional) Information Specific to a Vlan |
| vlan-id | (Optional) Vlan id value |
| group | (Optional) (S,G) specific information |
| grpaddr | (Optional) Group address |
| source | (Optional) source specific information |
| srcaddr | (Optional) Source address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1099165901

---

# Command: show forwarding l2vpn label vpls

## Syntax
```
show forwarding l2vpn label [ <label_id> ] vpls [ module module ] [ __readonly__ <label_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| l2vpn | l2vpn forwarding |
| label | VC label |
| label_id | (Optional) VC label |
| vpls | VPLS |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| label_id | (Optional) Label ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3369113880

---

# Command: show forwarding l2vpn label xconnect

## Syntax
```
show forwarding l2vpn label [ <label_id> ] xconnect [ module module ] [ __readonly__ <label_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| l2vpn | l2vpn forwarding |
| label | VC label |
| label_id | (Optional) VC label |
| xconnect | xconnect or VPWS |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| label_id | (Optional) Label ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4211979457

---

# Command: show forwarding l2vpn vlan

## Syntax
```
show forwarding l2vpn vlan [ <vlan_id> ] [ module <module> ] [ __readonly__ <vlan> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| l2vpn | l2vpn forwarding |
| vlan | vlan |
| vlan_id | (Optional) vlan id |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| vlan | (Optional) vlan |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2930967570

---

# Command: show forwarding mpls

## Syntax
```
show forwarding mpls [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; <vrf-all> } [ label <label-id> &#124; <prefix> &#124; <v6prefix> ] &#124; table
 <table_id> [ label <label-id> &#124; <prefix> &#124; <v6prefix> ] &#124; label-space <label-space-id> &#124; label <label-id> &#124; <prefix> &#124; <v6prefix>
 ] [ stats ] [ module <module> ] [ implicit ] [ platform ] [ __readonly__ [ { TABLE_mpls <label> [ { TABLE_table_id [ <out-table-id>
 ] [ <fec> ] [ <out-ip> ] [ <out-intf> ] [ <out-label> ] [ <out-op> ] [ <hh> ] [ <ref-count> ] } ] [ <in-pkts> ] [ <in-bytes>
 ] [ <swap-out-pkts> ] [ <swap-out-bytes> ] [ <tunnel-out-pkts> ] [ <tunnel-out-bytes> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| mpls | mpls forwarding |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known vrf name |
| vrf-all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table number |
| label-space | (Optional) label space |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3814525651

---

# Command: show forwarding mpls aggregate

## Syntax
```
show forwarding mpls aggregate [ label { <label-id> &#124; all } ] [ detail ] [ module <module> ] [ __readonly__ [ { TABLE_label_info
 <label> <id> [ <sw_index> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| mpls | mpls forwaring |
| aggregate | aggregate label |
| label | (Optional) label |
| label-id | (Optional) label-id |
| all | (Optional) all |
| detail | (Optional) detail |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1852918314

---

# Command: show forwarding mpls cbts

## Syntax
```
show forwarding mpls cbts [ module <module> ] [ __readonly__ [ { TABLE_cbts <label> [ <out-intf> ] [ <out-table-id> ] [ <out-ip>
 ] [ <out-op> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| mpls | mpls forwaring |
| cbts | cbts labels |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| TABLE_cbts | (Optional) |
| label | (Optional) mpls label value |
| out-intf | (Optional) Output Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2456252431

---

# Command: show forwarding mpls drop-stats

## Syntax
```
show forwarding mpls drop-stats [ platform &#124; label0-fwd-stats ] [ __readonly__ [ { TABLE_drop_stats <unit-number> <pkts> <bytes>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| mpls | mpls forwarding |
| drop-stats | MPLS dropped packets |
| platform | (Optional) command to display stats per chip |
| label0-fwd-stats | (Optional) command to display stats for label0 |
| __readonly__ | (Optional) |
| TABLE_drop_stats | (Optional) Table for mpls drop stats |
| unit-number | (Optional) unit number |
| pkts | (Optional) Label Packet Stats |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1421595864

---

# Command: show forwarding mpls ecmp

## Syntax
```
show forwarding mpls ecmp [ module <module> ] [ platform ] [ __readonly__ [ { TABLE_ecmp [ <type> ] [ <num_paths> ] [ <ip_paths>
 ] [ <mpls_paths> ] [ <ecmp_hash> ] [ <holder> ] [ <refcount> ] [ <hw_index> ] [ <fec> ] [ { TABLE_ecmp_paths [ <out-intf>
 ] [ <out-ip> ] [ <label-info> ] [ <refcount> ] [ <hh> ] [ <ecmp-type> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | display fib information |
| mpls | mpls forwarding |
| ecmp | mpls ecmps |
| module | (Optional) slot |
| module | (Optional) slot number |
| platform | (Optional) show pd info |
| __readonly__ | (Optional) |
| TABLE_ecmp | (Optional) |
| type | (Optional) ecmp type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1694234311

---

# Command: show forwarding mpls eompls

## Syntax
```
show forwarding mpls eompls [ peers { <addr> &#124; all } ] [ __readonly__ [ { TABLE_peer_ip <peer_ip> <peer_id> <vlan_bmp> <rx_pkts>
 <rx_bytes> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show |
| forwarding | Forwarding information |
| mpls | mpls forwarding |
| eompls | eompls |
| peers | (Optional) nve peers |
| addr | (Optional) peer ipaddress |
| all | (Optional) Display peer info for all peers |
| __readonly__ | (Optional) |
| TABLE_peer_ip | (Optional) |
| peer_ip | (Optional) peer address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1355734379

---

# Command: show forwarding mpls eompls ir

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| forwarding | Forwarding information |
| mpls | mpls |
| eompls | eompls |
| ir | ir |
| vlan | (Optional) vlans all |
| all | (Optional) all |
| vlan_id | (Optional) vlan-id |
| peer | (Optional) peers-all |
| all | (Optional) all |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2506183247

---

# Command: show forwarding mpls option_b

## Syntax
```
show forwarding mpls option_b [ label <label> ] [ module <module> ] [ platform ] [ __readonly__ [ { TABLE_mpls_opt_b <label>
 [ <prefix> ] [ <v6prefix> ] [ <nxhop> ] [ <out-interface> ] [ <out-op> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | forwarding |
| mpls | mpls forwarding |
| option_b | Option B |
| label | (Optional) mpls labels |
| label | (Optional) mpls label value |
| module | (Optional) slot |
| module | (Optional) slot number |
| platform | (Optional) show pd info |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2938226350

---

# Command: show forwarding mpls srte module

## Syntax
```
show forwarding mpls srte module [ <module> ] [ __readonly__ [ { TABLE_srte <table-id> [ { TABLE_binding_label <binding-label>
 <parent-table-id> <parent-vobj-id> [ { TABLE_prefix <prefix> <vrf> } ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show |
| forwarding | Forwarding information |
| mpls | mpls forwaring |
| srte | SR Traffic Engineering |
| module | slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| TABLE_srte | (Optional) |
| table-id | (Optional) table id |
| TABLE_binding_label | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2926080414

---

# Command: show forwarding mpls summary

## Syntax
```
show forwarding mpls summary [ module <module> ] [ __readonly__ [ { TABLE_labels <space> <count> } <total_deagg_labels> <feature_evpn_status>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | display fib information |
| mpls | mpls forwarding |
| summary | summary |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| TABLE_labels | (Optional) |
| space | (Optional) label space |
| count | (Optional) number of labels |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3943290610

---

# Command: show forwarding mpls te

## Syntax
```
show forwarding mpls te [ <te_if> ] [ detail ] [ module <module> ] [ __readonly__ { TABLE_te <id> [ <midpoint_source> ] [
 <dest> ] [ <tunnel_id> ] [ <ext_tunnel_id> ] [ <lisp_id> ] [ <adjacency> ] [ <hh> ] [ <lfib_adj> ] [ <adj_refcount> ] [ <obj_refcount>
 ] [ <te_state> ] [ <next_hop> ] [ <next_if_index> ] [ <op_label> ] [ <backup_tunnel> ] [ <adj_key_id> ] [ <frr_label> ] [
 <local_label> ] [ <adj_count> ] [ <type> ] [ <out_if> ] [ <out_lbl> ] [ <backup_if> ] [ <backup_lbl> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| mpls | mpls forwarding |
| te | Traffic Engineering |
| detail | (Optional) detail |
| module | (Optional) slot |
| te_if | (Optional) tunnel-te number |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| TABLE_te | (Optional) |
| id | (Optional) headend if index |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2555597010

---

# Command: show forwarding multicast-sr loopback interface

## Syntax
```
show forwarding multicast-sr loopback interface [ __readonly__ [ <port-num> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| multicast-sr | multicast service reflect information |
| interface | loopback interface |
| loopback | loopback interface |
| __readonly__ | (Optional) |
| port-num | (Optional) Port number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4148263567

---

# Command: show forwarding multicast outgoing-interface-list

## Syntax
```
show forwarding multicast outgoing-interface-list { L2 &#124; L3 &#124; vxlan-encap &#124; vxlan-ir-dci-encap } [ platform ] [ module <module>
 ] [ <index> ] [ __readonly__ [ <refcount> ] [ <total_l2_oiflist> ] [ <total_l3_oiflist> ] [ <slot> ] [ TABLE_MCAST_OIF_INFO
 <oiflist_idx> [ <vlan> ] [ <num_oif> ] [ TABLE_MCAST_OIF_INTF_INFO [ <intf> ] [ <dvif> ] ] [ <encap_id> ] <hw_oiflist_idx>
 [ <mcidx> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Forwarding information |
| multicast | Multicast IPv4 information |
| outgoing-interface-list | show outgoing interface list info |
| L2 | Layer 2 oiflist |
| L3 | Layer 3 oiflist |
| vxlan-encap | vxlan-encap oiflist |
| vxlan-ir-dci-encap | vxlan-ir-dci-encap oiflist |
| platform | (Optional) Display PI/PD |
| module | (Optional) slot |
| module | (Optional) slot number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp9391462670

---

# Command: show forwarding multicast route

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | Forwarding information |
| ipv4 | (Optional) ipv4 |
| multicast | Multicast IPv4 information |
| route | Mcast route information |
| platform | (Optional) Platform Details |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table number |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3700798890

---

# Command: show forwarding nve l2 ingress-replication-peers

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | display fib information |
| nve | nve related info |
| l2 | L2 info |
| ingress-replication-peers | ingress replication peer info |
| ipv4 | (Optional) ipv4 peer |
| peer_ip | (Optional) show detailed info of a peer |
| ipv6 | (Optional) ipv6 peer |
| __readonly__ | (Optional) |
| TABLE_VLAN | (Optional) vlan peer ids table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2976609212

---

# Command: show forwarding nve l3 adjacency tunnel

## Syntax
```
show forwarding nve l3 adjacency tunnel [ <tunnel_id> &#124; all ] [ bd <bd_id> &#124; detail &#124; module <module> &#124; table <table_id> ]
 [ __readonly__ TABLE_nvel3adj <tunnel_id> <bd_id> <table_id> <VNI> <Drop> <Refcount> <Origin> <State> <Del> [ <sw_index> <hw_index0>
 <hw_index1> <hw_index2> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| nve | nve related info |
| l3 | Layer 3 |
| adjacency | Adjacency info |
| tunnel | VXLAN tunnel |
| tunnel_id | (Optional) tunnel_id |
| all | (Optional) show adjacency info for all peers |
| bd | (Optional) BD info |
| bd_id | (Optional) bd id |
| detail | (Optional) Show detailed information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3509641883

---

# Command: show forwarding nve l3 adjacency v6-tunnel

## Syntax
```
show forwarding nve l3 adjacency v6-tunnel [ <peer-ip> &#124; all ] [ bd <bd_id> &#124; detail &#124; module <num> &#124; table <table_id> ] [
 __readonly__ TABLE_nvel3adj <peer-ip> <bd_id> <table_id> <VNI> <Drop> <Refcount> <Origin> <State> <Del> <sw_index> <hw_index0>
 <hw_index1> <hw_index2> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| nve | nve related info |
| l3 | Layer 3 |
| adjacency | Adjacency info |
| v6-tunnel | VXLAN V6 tunnel |
| all | (Optional) Show adjacency for all peers |
| bd | (Optional) BD info |
| bd_id | (Optional) bd id |
| detail | (Optional) Show detailed information |
| module | (Optional) Slot/module |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3485943361

---

# Command: show forwarding nve l3 ecmp

## Syntax
```
show forwarding nve l3 ecmp [ __readonly__ { TABLE_nvel3ecmp <hw_index> <ecmp_hash> <num_paths> <table_id> <flags> <adj_flags>
 <ref_count> { TABLE_tunnel_info [ <tunnel_id> &#124; <tunnel_ip> ] <segment_id> } <hw_ecmp_index0> <hw_ecmp_index1> <hw_ecmp_index2>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| nve | nve related info |
| l3 | Layer 3 |
| ecmp | nve ecmp info |
| __readonly__ | (Optional) |
| TABLE_nvel3ecmp | (Optional) nve l3 ecmp table |
| hw_index | (Optional) hw_index address pointer |
| ecmp_hash | (Optional) ecmp hash |
| num_paths | (Optional) numer of members in ECMP |
| table_id | (Optional) table id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2438066933

---

# Command: show forwarding nve l3 peers

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | display fib information |
| nve | nve related info |
| l3 | Layer 3 |
| peers | nve peers |
| peer_id | (Optional) nve peer-id |
| tunnel | (Optional) VXLAN tunnel |
| tunnel_id | (Optional) Unique identifier for the tunnel |
| detail | (Optional) Show detailed information |
| module | (Optional) Slot/module |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1051746671

---

# Command: show forwarding nve underlay-interfaces

## Syntax
```
show forwarding nve underlay-interfaces [ __readonly__ { <broadcast_status> <broadcast_level> <multicast_status> <multicast_level>
 <unicast_status> <unicast_level> <no_of_uplink_interfaces> } [ { TABLE_uplinks <ifindex> <peerid_bmp> <is_dci> [ <phy_if>
 ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| forwarding | display fib information |
| nve | NVE related info |
| underlay-interfaces | underlay interfaces info |
| __readonly__ | (Optional) |
| broadcast_status | (Optional) status |
| broadcast_level | (Optional) broadcast level |
| multicast_status | (Optional) multicast status |
| multicast_level | (Optional) multicast level |
| unicast_status | (Optional) unitcast status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2649924145

---

# Command: show forwarding otv

## Syntax
```
show forwarding otv <intf> [ peer <peer-id> ] [ module <module> ] [ __readonly__ <vlan> <peer-id> <peer_vlan_count><tunnel_ifindex><tunnel_ifname>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | fib information |
| otv | overlay-transport-virtualization |
| intf | overlay interface |
| peer | (Optional) overlay peer |
| peer-id | (Optional) overlay peer-id |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| vlan | (Optional) Vlan information |
| peer-id | (Optional) peer-id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp2244671348

---

# Command: show forwarding security group-tag

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table number |
| vlan | (Optional) vlan |
| vlan_id | (Optional) vlan number |
| ipv4 | (Optional) ipv4 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3735207989

---

# Command: show forwarding security mac

## Syntax
```
forwarding
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| vrf | (Optional) display info per VRF |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| vrf-all | (Optional) Display information for all VRFs |
| table | (Optional) display info per vpn-id |
| table_id | (Optional) table number |
| ipv4 | (Optional) ipv4 |
| security | display IP security information |
| mac | ip_address->mac_address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4208108211

---

# Command: show forwarding trace

## Syntax
```
show forwarding trace [ clear ] [ module <module> ] [ __readonly__ <op> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| trace | display trace buffer |
| clear | (Optional) clear the trace buffer |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| op | (Optional) output |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp8487426230

---

# Command: show forwarding trace profile

## Syntax
```
show forwarding trace profile
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| trace | display trace buffer |
| profile | show the collection profiling information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp4078110517

---

# Command: show forwarding trace profile funcstats

## Syntax
```
show forwarding trace profile funcstats [ enable &#124; disable ] [ module <module> ] [ __readonly__ <op> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| forwarding | display fib information |
| trace | display trace buffer |
| profile | show the collection profiling information |
| funcstats | function statistics |
| enable | (Optional) enable function statistics |
| disable | (Optional) disable function statistics |
| module | (Optional) slot |
| module | (Optional) slot number |
| __readonly__ | (Optional) |
| op | (Optional) output |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3283816116

---

# Command: show fte event

## Syntax
```
show fte event [ name ] [ { <eventname> } ] [ __readonly__ <event> <description> <use_count> <latency_threshold> <latency_unit>
 <analytics_changed_flow_count> <latency_flow_count> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fte | Show FTE information |
| event | Show Event Configuration |
| name | (Optional) Show the configuration for a specific FTE Event |
| eventname | (Optional) Specify a event |
| __readonly__ | (Optional) |
| event | (Optional) |
| description | (Optional) |
| use_count | (Optional) |
| latency_threshold | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1712543387

---

# Command: show fte exporter

## Syntax
```
show fte exporter [ name ] [ <exportername> ] [ __readonly__ <exporter> <description> <dest> <vrf> <vrf_id> <vrf_resolved>
 <dest_udp> <source_intf> <source_ip> <exporter-id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fte | Show FTE information |
| exporter | Show FTE Exporter Configuration |
| name | (Optional) Show a specific FTE Exporter |
| exportername | (Optional) Specify an exporter |
| __readonly__ | (Optional) |
| exporter | (Optional) |
| description | (Optional) |
| dest | (Optional) |
| vrf | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1721863969

---

# Command: show fte monitor

## Syntax
```
show fte monitor [ name ] [ <monitorname> [ cache [ detailed ] ] ] [ __readonly__ <monitor> <use_count> <description> <record>
 <event> <exporter1> <exporter2> <bucket_id> <src_addr> <dest_addr> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fte | Show FTE information |
| monitor | Show Monitor Configuration |
| name | (Optional) Show a specific FTE Monitor |
| monitorname | (Optional) Specify a monitor |
| cache | (Optional) Flow monitor cache contents |
| detailed | (Optional) Show the entire cache contents |
| __readonly__ | (Optional) |
| monitor | (Optional) |
| use_count | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp3562090252

---

# Command: show fte record

## Syntax
```
show fte record [ name ] [ { <recordname> } &#124; { fte-original } &#124; { fte { protocol-port &#124; layer2-switched { input } &#124; { ipv4
 &#124; ipv6 &#124; l2 } { original-input } } } ] [ __readonly__ <record> <description> <use_count> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| fte | Show FTE information |
| record | Show Record Configuration |
| name | (Optional) Show the configuration for a specific FTE Record |
| recordname | (Optional) Specify a record |
| fte-original | (Optional) Traditional IPv4 input FTE with origin ASs |
| fte | (Optional) Traditional FTE collection schemes |
| ipv4 | (Optional) IPv4 collection schemes |
| ipv6 | (Optional) IPv6 collection schemes |
| l2 | (Optional) L2 collection schemes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0110.html
**Tags:** show-mode, S-commands
**Command ID:** wp1495935137

---

