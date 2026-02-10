# Chapter: P Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01111.html
**Type:** Show Commands  
**Chapter:** Group-1111 Commands  
**Total Commands:** 90

## Command List

- `show param-list`
- `show password secure-mode`
- `show password strength-check`
- `show pending`
- `show plb`
- `show plb analytics`
- `show plb vrf`
- `show pmap-int-br interface br`
- `show pmap-int`
- `show pnp lease`
- `show pnp posix_pi configs`
- `show pnp posix_pi tech-support`
- `show pnp profiles`
- `show pnp status`
- `show pnp summary`
- `show pnp version`
- `show policy-map`
- `show policy-map interface control-plane`
- `show policy-map system`
- `show policy-map type control-plane`
- `show policy-map type network-qos`
- `show port-channel capacity`
- `show port-channel compatibility-parameters`
- `show port-channel database`
- `show port-channel fast-convergence`
- `show port-channel load-balance`
- `show port-channel load-balance forwarding-path1 interface src-interface`
- `show port-channel load-balance forwarding-path interface`
- `show port-channel load-balance hardware forwarding-path interface source`
- `show port-channel rbh-distribution`
- `show port-channel scale-fanout`
- `show port-channel summary`
- `show port-channel traffic`
- `show port-channel usage`
- `show port-license`
- `show port-profile`
- `show port-profile brief`
- `show port-profile expand-interface`
- `show port-profile sync-status`
- `show port-profile usage`
- `show port-security`
- `show port-security address`
- `show port-security address interface`
- `show port-security interface`
- `show port-security state`
- `show port naming`
- `show postcard-telemetry exporter`
- `show postcard-telemetry flow-profile`
- `show postcard-telemetry monitor`
- `show postcard-telemetry queue-profile`
- `show postcard-telemetry sessions`
- `show postcard-telemetry watchlist`
- `show power inline`
- `show power inline`
- `show power inline police`
- `show power inline priority`
- `show privilege`
- `show processes`
- `show processes cpu`
- `show processes cpu history`
- `show processes cpu history data`
- `show processes cpu module`
- `show processes log`
- `show processes log details`
- `show processes log pid`
- `show processes log vdc-all`
- `show processes memory`
- `show processes memory physical`
- `show processes memory shared`
- `show processes vdc`
- `show processes vdc cpu`
- `show processes vdc log`
- `show processes vdc log details`
- `show processes vdc log pid`
- `show processes vdc memory`
- `show processes version`
- `show pss debug`
- `show ptp brief`
- `show ptp clock`
- `show ptp clock foreign-masters record`
- `show ptp corrections`
- `show ptp cost`
- `show ptp counters interface`
- `show ptp delay summary`
- `show ptp domain data`
- `show ptp interface domain`
- `show ptp packet-trace`
- `show ptp parent`
- `show ptp port interface`
- `show ptp time-property`

---

## Detailed Command Reference

# Command: show param-list

## Syntax
```
show param-list [ param-list-name <plistname> ] [ show-instance ] [ __readonly__ TABLE_param_list <param_list_name> [ <param_list_var>
 ] [ <param_list_type> ] [ TABLE_instance <param_instance_name> [ <param_instance_var> ] [ <param_instance_val> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| param-list | Show param-list |
| param-list-name | (Optional) param list name |
| plistname | (Optional) Enter the name of the param-list |
| show-instance | (Optional) show instances for the param list |
| __readonly__ | (Optional) |
| TABLE_param_list | (Optional) |
| param_list_name | (Optional) Parameter List Name |
| param_list_var | (Optional) Parameter Name |
| param_list_type | (Optional) Param Type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1436681592

---

# Command: show password secure-mode

## Syntax
```
show password secure-mode [ __readonly__ { secure_mode <secure_mode_status> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| password | Password for the user |
| secure-mode | secure mode for changing passwords |
| __readonly__ | (Optional) |
| secure_mode | (Optional) run time status about xml |
| secure_mode_status | (Optional) Run time status about secure mode |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2735208003

---

# Command: show password strength-check

## Syntax
```
show password strength-check [ __readonly__ { operation_status <o_status> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| password | Password for the user |
| strength-check | Strength check of password |
| __readonly__ | (Optional) |
| operation_status | (Optional) run-time information about password strength-check |
| o_status | (Optional) operational status of password strength check |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1227950896

---

# Command: show pending

## Syntax
```
show [ pending ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display region configurations |
| pending | (Optional) Display the new mst configuration to be applied |

**Command Mode:** /exec/configure/spanning-tree/mst/configuration

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1054210843

---

# Command: show plb

## Syntax
```
show plb [ service <service-name> ] [ brief ] [ __readonly__ <is_firstentry> <is_detail> <is_active> <is_firstentry_routemap>
 <is_firstentry_standby> <is_firstentry_acl> <is_lastentry> [ TABLE_summary <service_name> <state> [ <reason> ] <lb_scheme>
 [ <interface> ] <buckets> [ <vrf_name> ] [ <excl_acl> ] [ <src_interface> ] [ TABLE_device <device_grp> <dg_probe> <dg_probe_port>
 ] [ TABLE_route_map [ <route_map> ] <interface> <r_status> ] [ TABLE_vip [ <vip_ip> ] [ <vip_probe> ] [ <vip_port> ] [ <vip_dgname>
 ] [ <ace_name> ] [ <ace_seq> ] [ <ace_ip> ] [ <ace_protocol> ] [ <ace_port> ] [ TABLE_vip_node [ <vip_node> ] [ <vip_nodev6>
 ] <vip_config> <vip_weight> <vip_node_probe> <vip_node_probe_port> <vip_node_probe_ip> <vip_status> <vip_track_id> <vip_ip_sla_id>
 [ TABLE_vip_standby [ <vip_standby_ip> ] [ <vip_standby_ipv6> ] <vip_standby_config> <vip_standby_weight> <vip_standby_probe>
 <vip_standby_probe_port> <vip_standby_probe_ip> <vip_standby_status> <vip_standby_track_id> <vip_standby_sla_id> ] [ TABLE_vip_acl
 [ <vip_access_list> ] ] ] ] [ TABLE_node [ <node> ] [ <nodev6> ] <config> <weight> <node_probe> <node_probe_port> <node_probe_ip>
 <status> <track_id> <ip_sla_id> [ TABLE_standby [ <standby_ip> ] [ <standby_ipv6> ] <standby_config> <standby_weight> <standby_probe>
 <standby_probe_port> <standby_probe_ip> <standby_status> <standby_track_id> <standby_sla_id> ] [ TABLE_acl [ <access_list>
 ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| plb | Display PLB service details |
| service | (Optional) PLB details for specific service |
| service-name | (Optional) Specify PLB service name |
| brief | (Optional) Display PLB service in brief |
| __readonly__ | (Optional) Read Only |
| is_firstentry | (Optional) |
| is_detail | (Optional) |
| is_active | (Optional) |
| is_firstentry_routemap | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3159823709

---

# Command: show plb analytics

## Syntax
```
show plb analytics [ service <service-name> ] [ src { <sip> &#124; <sipv6> } &#124; node { <nip> &#124; <nipv6> } &#124; vip { <vip> &#124; <vipv6>
 } &#124; device-group <group-name> ] [ brief ] [ __readonly__ <plbshowinfo-stats-svc-hdr> [ TABLE_stats_svc <plbshowinfo-stats-service_name>
 <plbshowinfo-stats-dev-grp> <plbshowinfo-stats-vip> <plbshowinfo-stats-vip-pkts> <plbshowinfo-stats-vip-pkts-percentage> [
 <plbshowinfo-stats-ace-seq> ] [ <plbshowinfo-stats-ace-ip> ] <plbshowinfo-stats-bkt-hdr> [ TABLE_stats_bkt <plbshowinfo-stats-acl>
 [ <plbshowinfo-stats-oper-node> ] <plbshowinfo-stats-node-mode> <plbshowinfo-stats-orig-node> <plbshowinfo-stats-node-pkts>
 <plbshowinfo-stats-node-pkts-percentage> [ <plbshowinfo-stats-acl-pkts> ] [ <plbshowinfo-for-ace> ] ] ] <plb-show-end> [ <plb-true-end>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| plb | PLB service |
| analytics | PLB analytics information |
| service | (Optional) PLB analytics for specific service |
| service-name | (Optional) Specify plb service name |
| src | (Optional) Analytics information for source (bucket) ip |
| node | (Optional) Analytics information for destination device group node/server ip |
| vip | (Optional) Analytics information for virtual ip |
| device-group | (Optional) Analytics information of specified device group |
| group-name | (Optional) Specify device group name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2716252816

---

# Command: show plb vrf

## Syntax
```
show plb vrf [ <vrf-name> ] [ __readonly__ <plbshowinfo-vrf-hdr> { TABLE_svc <plbshowinfo-vrf-service_name> <plbshowinfo-vrf-name>
 <plbshowinfo-vrf-id> } <plb-show-end> [ <plb-true-end> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| plb | PLB service |
| vrf | PLB service vrf |
| vrf-name | (Optional) VRF name |
| __readonly__ | (Optional) Read Only |
| plbshowinfo-vrf-hdr | (Optional) PLB info vrf header |
| TABLE_svc | (Optional) PLB Service VRF details |
| plbshowinfo-vrf-service_name | (Optional) PLB service name |
| plbshowinfo-vrf-name | (Optional) PLB vrf name |
| plbshowinfo-vrf-id | (Optional) PLB vrf id |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1557430224

---

# Command: show pmap-int-br interface br

## Syntax
```
show pmap-int-br interface br [ __readonly__ { [ TABLE_ifvlanstr <if-vlan-str> <if-status> [ <in-pmap-qos> ] [ <out-pmap-qos>
 ] [ <in-pmap-que> ] [ <out-pmap-que> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pmap-int-br | Show policy maps |
| interface | Show service policy on interface |
| br | Brief report of all policies attached to interfaces |
| TABLE_ifvlanstr | (Optional) all interfaces xml sessions |
| if-vlan-str | (Optional) ifindex or vlan id: xml key |
| __readonly__ | (Optional) |
| if-status | (Optional) Interface/vlan status [active/inactive]: xml key |
| in-pmap-qos | (Optional) Input QoS Policy-map name: xml key |
| out-pmap-qos | (Optional) output QoS Policy-map name: xml key |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2893351557

---

# Command: show pmap-int

## Syntax
```
show pmap-int { interface [ <iface-list> ] [ input &#124; output ] [ type <qos-or-q> ] [ detail ] &#124;
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pmap-int | Show policy maps |
| interface | Show service policy on interface |
| iface-list | (Optional) List of Interface |
| input | (Optional) Input Service policy |
| output | (Optional) Output Service policy |
| type | (Optional) Type of policy |
| qos-or-q | (Optional) |
| detail | (Optional) Detailed QoS or Queuing statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1331729479

---

# Command: show pnp lease

## Syntax
```
show pnp lease
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| lease | Show PnP lease information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1468681871

---

# Command: show pnp posix_pi configs

## Syntax
```
show pnp posix_pi configs
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| posix_pi | Posix PnP PI agent |
| configs | Posix PnP PI configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1729278680

---

# Command: show pnp posix_pi tech-support

## Syntax
```
show pnp posix_pi tech-support
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| posix_pi | Posix PnP PI agent |
| tech-support | Technical Support |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3373130760

---

# Command: show pnp profiles

## Syntax
```
show pnp profiles
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| profiles | Show POSIX PnP Profile |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1345272040

---

# Command: show pnp status

## Syntax
```
show pnp status
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| status | Show POSIX PnP Status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2749605847

---

# Command: show pnp summary

## Syntax
```
show pnp summary
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| summary | Show POSIX PnP Summary |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2059856617

---

# Command: show pnp version

## Syntax
```
show pnp version
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pnp | Plug and Play |
| version | Show POSIX PnP Version |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp6623336570

---

# Command: show policy-map

## Syntax
```
show policy-map [ { [ type qos ] [ <pmap-name-qos> ] } &#124; { type queuing [ <pmap-name-que> ] } ] [ __readonly__ { [ <display-all>
 ] [ TABLE_pmap [ <pmap-key> ] [ <type-spec> ] [ <yqos-or-q> ] [ <options> ] <pmap-name-out> [ <nq-xpmap-name> ] [ <desc> ]
 [ <nq-desc> ] [ TABLE_cmap [ <cmap-key> ] [ <type-cmap-spec> ] [ <xqos-or-q> ] [ <cmap-name> ] [ <nq-xcmap-name> ] [ TABLE_action
 [ <action-key> ] [ <nq-action-key> ] [ <serv-pol-type> ] [ <serv-pol-name> ] [ <cos-list> ] [ <qos-group-list> ] [ <protocol>
 ] [ <nq-pause> <timeout> <nq-size-in-bytes> <nq-xoff-bytes> <nq-xon-bytes> ] [ <pfc-cos-list> ] [ <pfc_rx_only> ] [ <cc> ]
 [ <thresh-units> ] [ <min-thresh> ] [ <max-thresh> ] [ <drop-prob> ] [ <iod> ] [ <mtu> ] [ <set-cos> ] [ <dpp> ] [ <dctcp-threshold>
 ] [ <queue-limit> ] [ <inner> ] [ <dlb-disable> ] [ <cos> ] [ <exp-val-imposition> ] [ <exp-val-topmost> ] [ <dscp-enum> ]
 [ <dscp> ] [ <prec-enum> ] [ <prec> ] [ <disc-class> ] [ <qos-group> ] [ <tmap-from> ] [ <tmap-to> ] [ <tmap-name> ] [ <avg-rate-type>
 ] [ <rate-units> ] [ <shape-rate> ] [ <min-rate-type> ] [ <min-rate-units> ] [ <shape-min-rate> ] [ <max-rate-type> ] [ <max-rate-units>
 ] [ <shape-max-rate> ] [ <rise-threshold-units> ] [ <fall-threshold-units> ] [ <prio-level> ] [ <qlim-param-type> ] [ <qlim-param-val>
 ] [ <ooo> ] [ <size-units> ] [ <qlim-size> ] [ <qlim-enum-spec> ] [ <rdet-agg> ] [ <rdet-mode> ] [ <rdet-burst-opt> ] [ <rdet-mesh-opt>
 ] [ <rdet-ecn> ] [ TABLE_rdet <rdet-key> [ <rdet-values> ] [ <rdet-min-thresh> ] [ <rdet-size-units> ] [ <rdet-max-thresh>
 ] [ <rdet-drop-prob> ] [ <rdet-weight> ] [ <rdet-cap-average> ] ] [ <rdet-nonecn-mode> ] [ TABLE_rdet_nonecn <rdet-nonecn-key>
 [ <rdet-nonecn-min-thresh> ] [ <rdet-nonecn-size-units> ] [ <rdet-nonecn-max-thresh> ] [ <rdet-nonecn-drop-prob> ] ] [ <afd-mode>
 ] [ TABLE_afd <afd-key> [ <afd-values> ] [ <afd-queue-desired> ] [ <afd-size-units> ] [ <afd-ecn> ] ] [ <pause> <size-in-bytes>
 <xoff-bytes> <xon-bytes> ] [ <priority-group-number> ] [ <bw-units> ] [ <bw-rate> ] [ <rem-bw-units> ] [ <rem-bw-rate> ] [
 <agg-policer-name> ] [ <cir-spec> ] [ <bc-spec> ] [ <be-spec> ] [ <cir-rate-units> ] [ <cir> ] [ <bc-size-units> ] [ <bc>
 ] [ <pir-rate-units> ] [ <pir> ] [ <be-size-units> ] [ <be> ] [ <cnf-col-cmap> ] [ <exc-col-cmap> ] [ TABLE_police <police-key>
 [ <cnf-act> ] [ <exc-act> ] [ <vio-act> ] [ <set-type> ] [ <enum-spec> ] [ <set-val> ] [ <ptmap-from> ] [ <ptmap-to> ] [ <ptmap-name>
 ] ] [ <burst-detect-enable> ] ] ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| policy-map | Show policy maps |
| type | (Optional) Type of the policy-map |
| qos | (Optional) type qos |
| queuing | (Optional) type queuing |
| pmap-name-qos | (Optional) policy map name (type qos) |
| pmap-name-que | (Optional) policy map name (type queuing) |
| __readonly__ | (Optional) |
| display-all | (Optional) Display all kinds of class-maps |
| TABLE_pmap | (Optional) all pmap xml sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1632480399

---

# Command: show policy-map interface control-plane

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| policy-map | Show policy maps |
| interface | Show service policy on interface |
| control-plane | command is for copp policy |
| module | (Optional) module number for statistics |
| class | (Optional) class-name name |
| cmap-name | (Optional) Name of the class-map |
| pmap-name | (Optional) Name of the Policy-map |
| __readonly__ | (Optional) |
| scale-factor-cmd | (Optional) Scale factor command |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, qos, S-commands
**Command ID:** wp1946458295

---

# Command: show policy-map system

## Syntax
```
show policy-map system [ type { network-qos &#124; qos [ input2 ] &#124; queuing [ input &#124; output ] } ] [ __readonly__ { [ <display-all>
 ] [ TABLE_xpmap <xpmap-name> [ <desc> ] [ TABLE_xcmap <xcmap-name> [ TABLE_xaction <xaction-key> [ <cos-list> ] [ <qos-group-list>
 ] [ <protocol> ] [ <pause> <timeout> <size-in-bytes> <xoff-bytes> <xon-bytes> ] [ <pfc-cos-list> ] [ <pfc_rx_only> ] [ <cc>
 ] [ <thresh-units> ] [ <min-thresh> ] [ <max-thresh> ] [ <drop-prob> ] [ <iod> ] [ <mtu> ] [ <set-cos> ] [ <dpp> ] [ <dctcp-threshold>
 ] [ <queue-limit> ] [ <stat-en-dis-enum> ] ] ] ] [ TABLE_pmap <pmap-key> <pmap-inner-outer> <in-or-out> <yqos-or-q> [ <options>
 ] <pmap-name> [ <stat-status-enum> ] [ TABLE_cmap <cmap-key> [ <xqos-or-q> ] <match-opts> <cmap-name> [ <slot-num> ] [ <class-pkts>
 ] [ <agg-forward> ] [ TABLE_match <match-key> [ <not> ] [ <inner> ] [ <cos-list> ] [ <dscp-list> ] [ <exp-value-top> ] [ <protocol-name>
 ] [ <match-cmap-xqos-or-q> ] [ <match-cmap-opts> ] [ <match-cmap-name> ] ] [ TABLE_action <action-key> [ <set-inner> ] [ <cos>
 ] [ <qos-group> ] [ <serv-pol-type> ] [ <serv-pol-name> ] [ <serv-pol-return-inout> ] [ <rate-units> ] [ <shape-rate> ] [
 <min-rate-type> ] [ <min-rate-units> ] [ <shape-min-rate> ] [ <max-rate-type> ] [ <max-rate-units> ] [ <shape-max-rate> ]
 [ <prio-level> ] [ <qlim-param-type> ] [ <qlim-param-val> ] [ <size-units> ] [ <qlim-size> ] [ <qlim-enum-spec> ] [ <bw-units>
 ] [ <bw-rate> ] [ <rem-bw-units> ] [ <rem-bw-rate> ] [ <rise-threshold-units> ] [ <fall-threshold-units> ] [ <rdet-agg> ]
 [ <rdet-mode> ] [ <rdet-burst-opt> ] [ <rdet-mesh-opt> ] [ TABLE_rdet <rdet-key> [ <rdet-values> ] [ <rdet-min-thresh> ] [
 <rdet-size-units> ] [ <rdet-max-thresh> ] [ <rdet-drop-prob> ] [ <rdet-weight> ] [ <rdet-cap-average> ] ] [ <rdet-ecn> ] [
 TABLE_afd <afd-key> [ <afd-values> ] [ <afd-queue-desired> ] [ <afd-size-units> ] [ <afd-ecn> ] ] [ <pause> <size-in-bytes>
 <xoff-bytes> <xon-bytes> ] ] ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| policy-map | Show policy maps |
| type | (Optional) Type of the policy-map |
| system | Active policy in the system |
| network-qos | (Optional) type network-qos |
| qos | (Optional) type qos |
| input2 | (Optional) input policy |
| queuing | (Optional) type queuing |
| input | (Optional) input policy |
| output | (Optional) output policy |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2563070190

---

# Command: show policy-map type control-plane

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| policy-map | Show policy maps |
| type | Type of the policy-map |
| control-plane | command is for copp policy |
| expand | (Optional) Display the match-criterias along with class-map |
| name | (Optional) policy-map name |
| pmap-name | (Optional) Name of the Policy-map |
| __readonly__ | (Optional) |
| TABLE_pmap | (Optional) Table of policy-map |
| pmap-name1 | (Optional) Name of the Policy-map |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2744417047

---

# Command: show policy-map type network-qos

## Syntax
```
show policy-map type network-qos [ <pmap-name-nq> ] [ __readonly__ { [ <display-all> ] [ TABLE_xpmap <xpmap-name> [ <desc>
 ] [ TABLE_xcmap <xcmap-name> [ TABLE_action <action-key> [ <cos-list> ] [ <qos-group-list> ] [ <protocol> ] [ <pause> <timeout>
 <size-in-bytes> <xoff-bytes> <xon-bytes> ] [ <pfc-cos-list> ] [ <pfc_rx_only> ] [ <cc> ] [ <thresh-units> ] [ <min-thresh>
 ] [ <max-thresh> ] [ <drop-prob> ] [ <iod> ] [ <mtu> ] [ <set-cos> ] [ <dpp> ] [ <dctcp-threshold> ] [ <queue-limit> ] ] ]
 ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| policy-map | Show policy maps |
| type | Type of the policy-map |
| pmap-name-nq | (Optional) Policy-map name |
| network-qos | type network-qos |
| __readonly__ | (Optional) |
| display-all | (Optional) Display all network-qos policy-maps |
| TABLE_xpmap | (Optional) all xpmap xml sessions |
| xpmap-name | (Optional) Policy-map name |
| TABLE_xcmap | (Optional) all xcmap xml sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3445804025

---

# Command: show port-channel capacity

## Syntax
```
show port-channel capacity [ __readonly__ <total> <used> <free> <percentage_used> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| capacity | Capacity information |
| __readonly__ | (Optional) |
| total | (Optional) Total resource |
| used | (Optional) Used resource |
| free | (Optional) Free resource |
| percentage_used | (Optional) Used resource in percentage |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp3772568605

---

# Command: show port-channel compatibility-parameters

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| compatibility-parameters | Show compatibility parameters |
| __readonly__ | (Optional) |
| TABLE_compatibility | (Optional) Port-channel compatibility table |
| parameter | (Optional) Compatibity parameter |
| description | (Optional) Parameter description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp1652082570

---

# Command: show port-channel database

## Syntax
```
show port-channel database [ interface <if0> ] [ __readonly__ TABLE_interface <interface> <last-membership-update> <total-ports>
 <total-up-ports> [ <first_operational-port> ] <age-of-channel> [ <time-since-last-bundle> ] [ <last-bundled-member> ] [ <time-since-last-unbundle>
 ] [ <last-unbundled-member> ] [ { TABLE_member <port> <mode> <port-status> } ] [ <protocol> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| database | Show port-channel database |
| interface | (Optional) Specify a port-channel |
| if0 | (Optional) |
| __readonly__ | (Optional) |
| TABLE_interface | (Optional) Port-channel table |
| interface | (Optional) Port channel |
| mode | (Optional) channel-group mode |
| last-membership-update | (Optional) Last membership update |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp3038457160

---

# Command: show port-channel fast-convergence

## Syntax
```
show port-channel fast-convergence [ __readonly__ { port-channel fast-convergence <fastconvergence> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Configure port channel parameters |
| fast-convergence | Show port-channel fast-convergence status |
| __readonly__ | (Optional) |
| fastconvergence | (Optional) port channel fast convergence enable/disable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp2660556088

---

# Command: show port-channel load-balance

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| load-balance | Show port-channel load balance |
| module | (Optional) slot |
| module | (Optional) Specify a module number |
| fex | FEX devices |
| all | Display all configured FEX port-channel LB |
| __readonly__ | (Optional) |
| sys-cfg | (Optional) system wide load balance configuraton |
| sys-cfg-sel | (Optional) system config |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp4235278784

---

# Command: show port-channel load-balance forwarding-path1 interface src-interface

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Configure port channel parameters |
| load-balance | Show port-channel load balance |
| forwarding-path1 | Packet forwarding information |
| interface | Specify a port-channel number |
| ch-id | Port-Channel name |
| vlan | VLAN - for dot1Q tagged packets at ingress |
| vlan-id | VLAN ID |
| src-mac | Source MAC Address |
| src-mac | Source MAC address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp3933180274

---

# Command: show port-channel load-balance forwarding-path interface

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Configure port channel parameters |
| load-balance | Show port-channel load balance |
| forwarding-path | Packet forwarding information |
| interface | Specify a port-channel number |
| ch-id | Port-Channel name |
| hgig | Higig hashing result (only with RTAG7) |
| vlan | VLAN of the ingress packet i.e. when available |
| src-mac | Source MAC Address |
| src-mac | Source MAC address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp2151291163

---

# Command: show port-channel load-balance hardware forwarding-path interface source

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Configure port channel parameters |
| load-balance | Show port-channel load balance |
| hardware | ASIC hardware based information |
| forwarding-path | Packet forwarding information |
| interface | Specify a port-channel number |
| ch-id | Port-Channel name |
| hgig | Higig hashing result (only with RTAG7) |
| source-interface | Source interface - Required paramter |
| if-id | Interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp3415085099

---

# Command: show port-channel rbh-distribution

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| rbh-distribution | Show RBH distribution for member ports |
| interface | (Optional) Specify a port-channel interface |
| if0 | (Optional) |
| __readonly__ | (Optional) |
| TABLE_channel | (Optional) Port-channel table |
| chan-id | (Optional) Channel ID |
| port | (Optional) Member port |
| num_of_buckets | (Optional) Channel ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp2891187153

---

# Command: show port-channel scale-fanout

## Syntax
```
show port-channel scale-fanout [ __readonly__ { port-channel high-density <scalefanout> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Configure port channel parameters |
| scale-fanout | Enable/disable port-channel scale-fanout when ports span more than 16 ASIC units |
| __readonly__ | (Optional) |
| high-density | (Optional) port channel high density |
| scalefanout | (Optional) port channel scale fanout enable/disable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp8315113390

---

# Command: show port-channel summary

## Syntax
```
show port-channel summary [ interface <if0> &#124; controller ] [ __readonly__ TABLE_channel <group> <port-channel> <layer> <status>
 <type> <prtcl> [ { TABLE_member <port> <port-status> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| summary | Show port-channel summary |
| interface | (Optional) Specify a port-channel |
| if0 | (Optional) |
| controller | (Optional) Show controller configured port-channels |
| __readonly__ | (Optional) |
| TABLE_channel | (Optional) Port-channel table |
| group | (Optional) Channel group number |
| port-channel | (Optional) Port channel |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp4076606499

---

# Command: show port-channel traffic

## Syntax
```
show port-channel traffic [ interface <if0> ] [ __readonly__ TABLE_channel <chanId> <port> <rx-ucst> <tx-ucst> <rx-mcst> <tx-mcst>
 <rx-bcst> <tx-bcst> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| traffic | Show port-channel traffic statistics |
| __readonly__ | (Optional) |
| interface | (Optional) Specify a port-channel |
| if0 | (Optional) |
| TABLE_channel | (Optional) Port-channel table |
| chanId | (Optional) Channel ID |
| port | (Optional) Member port |
| rx-ucst | (Optional) Received unicast |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp3051491135

---

# Command: show port-channel usage

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-channel | Show port-channel information |
| usage | Show port-channel number usage |
| __readonly__ | (Optional) |
| total-channel-number-used | (Optional) Total used number of port-channels |
| used-range-low | (Optional) Used range low end value |
| used-range-hi | (Optional) Used range high end value |
| unused-range-low | (Optional) Un-used range low end value |
| unused-range-hi | (Optional) Un-used range high end value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, layer2, S-commands
**Command ID:** wp4800506200

---

# Command: show port-license

## Syntax
```
show port-license [ __readonly__ <consumed_port_licenses> [ TABLE_portlicense <interface> <cookie> <port_activation_license>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-license | Show port license information |
| __readonly__ | (Optional) |
| consumed_port_licenses | (Optional) Consumed port licenses |
| TABLE_portlicense | (Optional) port and licenses |
| interface | (Optional) interface name |
| cookie | (Optional) cookie |
| port_activation_license | (Optional) license state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3644958590

---

# Command: show port-profile

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-profile | Show port-profile |
| name | (Optional) port-profile name |
| all_profile_name | (Optional) Enter the name of the profile |
| __readonly__ | (Optional) |
| TABLE_port_profile_all | (Optional) |
| profile_name | (Optional) |
| profile_id | (Optional) |
| type | (Optional) |
| desc | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1811457150

---

# Command: show port-profile brief

## Syntax
```
show port-profile brief [ __readonly__ { TABLE_port_profile [ <profile_name> ] [ <type> ] [ <status> ] [ <profile_cfg_cnt>
 ] [ <eval_cfg_cnt> ] [ <intf_cnt> ] [ <inherit_cnt> ] [ <header_flag> ] } { TABLE_intf_count [ <intf_type> ] [ <intf_count>
 ] [ <tot_header_flag> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-profile | Show port-profile |
| brief | Brief info about profiles |
| __readonly__ | (Optional) |
| profile_name | (Optional) |
| TABLE_port_profile | (Optional) |
| type | (Optional) |
| status | (Optional) |
| profile_cfg_cnt | (Optional) |
| eval_cfg_cnt | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2856235576

---

# Command: show port-profile expand-interface

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-profile | Show port-profile |
| expand-interface | Active profile config applied in a interface |
| name | (Optional) port-profile name |
| all_profile_name | (Optional) Enter the name of the profile |
| __readonly__ | (Optional) |
| TABLE_port_profile | (Optional) |
| profile_name | (Optional) |
| TABLE_interface | (Optional) |
| intf | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4098190140

---

# Command: show port-profile sync-status

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-profile | Show port-profile |
| sync-status | Interfaces out-of-sync with port-profiles |
| interface | (Optional) Interface name |
| intfname | (Optional) Name of interface |
| __readonly__ | (Optional) |
| intf | (Optional) |
| status | (Optional) |
| inherit | (Optional) |
| sync_status | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1547639060

---

# Command: show port-profile usage

## Syntax
```
show port-profile usage [ name <all_profile_name> ] [ __readonly__ TABLE_port_profile <profile_name> [ TABLE_interface <interface>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port-profile | Show port-profile |
| usage | List of interfaces inherited a profile |
| name | (Optional) port-profile name |
| all_profile_name | (Optional) Enter the name of the profile |
| __readonly__ | (Optional) |
| TABLE_port_profile | (Optional) |
| TABLE_interface | (Optional) |
| profile_name | (Optional) |
| interface | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4006354840

---

# Command: show port-security

## Syntax
```
show port-security [ __readonly__ [ <total_addr> ] [ <max_sys_limit> ] [ { TABLE_eth_port_sec_interfaces <secure_port> <port_state>
 <max_secure_addr> <security_violation> <security_action> <current_addr> <num_val> <num_elems> <cmdid_show_index> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| port-security | Show secure port information |
| __readonly__ | (Optional) |
| total_addr | (Optional) Total number of secured MAC addresses |
| max_sys_limit | (Optional) Maximum allowed MACs excluding one per port |
| TABLE_eth_port_sec_interfaces | (Optional) Displays the secured interfaces |
| secure_port | (Optional) Interface Index |
| port_state | (Optional) Port security enabled or disabled |
| max_secure_addr | (Optional) Maximum number of secured MAC addresses |
| security_violation | (Optional) Number of security violations |
| security_action | (Optional) Security Action Shutdown/Restrict/Protect |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1773392930

---

# Command: show port-security address

## Syntax
```
show port-security address [ __readonly__ [ <total_addr> ] [ <max_sys_limit> ] [ { TABLE_eth_port_sec_mac_addrs <if_index>
 <vlan_id> <type> <mac_addr> <remain_age> <remote_learnt> <remote_aged> <num_elems> <cmd_addr_index> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| port-security | Show secure port information |
| address | Show secure address |
| __readonly__ | (Optional) |
| total_addr | (Optional) Total number of secured MAC addresses |
| max_sys_limit | (Optional) Maximum allowed MACs excluding one per port |
| TABLE_eth_port_sec_mac_addrs | (Optional) Displays the secured MAC addresses |
| if_index | (Optional) Interface index |
| vlan_id | (Optional) vlan id |
| type | (Optional) static/sticky/dyanmic MAC address |
| mac_addr | (Optional) mac address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp8650865700

---

# Command: show port-security address interface

## Syntax
```
show port-security address interface <interface-id> [ __readonly__ { TABLE_eth_port_sec_mac_addrs <if_index> <vlan_id> <type>
 <mac_addr> <remain_age> <remote_learnt> <remote_aged> <num_elems> <cmd_addr_index> } [ <total_addr> ] [ <max_sys_limit> ]
 [ <first> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| port-security | Show secure port information |
| address | Show secure address |
| interface | Show secure interface |
| interface-id | ethernet |
| __readonly__ | (Optional) |
| TABLE_eth_port_sec_mac_addrs | (Optional) Displays the secured MAC addresses |
| if_index | (Optional) Interface index |
| vlan_id | (Optional) vlan id |
| type | (Optional) static/sticky/dyanmic MAC address |
| mac_addr | (Optional) mac address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1695558463

---

# Command: show port-security interface

## Syntax
```
show port-security interface <interface-id> [ __readonly__ <port_status> <config_port_security> <oper_port_security> <violation_mode>
 <aging_time> <aging_type> <max_mac_addr> <total_sec_addrs> <conf_num_addrs> <num_sticky_addrs> <trap_count> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| port-security | Show secure port information |
| interface | Show secure interface |
| interface-id | ethernet |
| __readonly__ | (Optional) |
| port_status | (Optional) Secure Up/Down |
| config_port_security | (Optional) Port Security configuration is Enabled/Disabled |
| oper_port_security | (Optional) Port Security is Operationally Enabled/Disabled |
| violation_mode | (Optional) Shutdown/Restrict/Protect |
| aging_time | (Optional) Aging time in minutes |
| aging_type | (Optional) Absolute/Inactivity |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp9429076000

---

# Command: show port-security state

## Syntax
```
show port-security state [ __readonly__ <status> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| port-security | Port security related command |
| state | port security state |
| __readonly__ | (Optional) |
| status | (Optional) show port-security |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3764598147

---

# Command: show port naming

## Syntax
```
show port naming
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| port | Show port information |
| naming | Show port naming information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1470060917

---

# Command: show postcard-telemetry exporter

## Syntax
```
show postcard-telemetry exporter [ name ] [ <exportername> ] [ __readonly__ <exporter> <description> <dest> <vrf> <vrf_id>
 <vrf_resolved> <dest_udp> <source_intf> <source_ip> <seq_num> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| exporter | Show POSTCARD Exporter Configuration |
| name | (Optional) Show a specific POSTCARD Exporter |
| exportername | (Optional) Specify an exporter |
| __readonly__ | (Optional) |
| exporter | (Optional) |
| description | (Optional) |
| dest | (Optional) |
| vrf | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4034087068

---

# Command: show postcard-telemetry flow-profile

## Syntax
```
show postcard-telemetry flow-profile [ name ] [ <flow-profilename> ] [ __readonly__ <flow-profile> <description> <age> <latency>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| flow-profile | Show POSTCARD flow Profile Configuration |
| name | (Optional) Show a specific POSTCARD flow Profile |
| flow-profilename | (Optional) Specify an flow Profile |
| __readonly__ | (Optional) |
| flow-profile | (Optional) |
| description | (Optional) |
| age | (Optional) |
| latency | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3525609463

---

# Command: show postcard-telemetry monitor

## Syntax
```
show postcard-telemetry monitor [ name ] [ <monitorname> [ cache [ detailed ] ] ] [ __readonly__ <monitor> <use_count> <description>
 <event> <exporter> <bucket_id> <src_addr> <dest_addr> <watchlist> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| monitor | Show Monitor Configuration |
| name | (Optional) Show a specific POSTCARD Monitor |
| monitorname | (Optional) Specify a monitor |
| cache | (Optional) Flow monitor cache contents |
| detailed | (Optional) Show the entire cache contents |
| __readonly__ | (Optional) |
| monitor | (Optional) |
| use_count | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp4184607839

---

# Command: show postcard-telemetry queue-profile

## Syntax
```
show postcard-telemetry queue-profile [ name ] [ <queue-profilename> ] [ __readonly__ <queue-profile> <description> <depth>
 <latency> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| queue-profile | Show POSTCARD Queue Profile Configuration |
| name | (Optional) Show a specific POSTCARD Queue Profile |
| queue-profilename | (Optional) Specify an Queue Profile |
| __readonly__ | (Optional) |
| queue-profile | (Optional) |
| description | (Optional) |
| depth | (Optional) |
| latency | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2438904662

---

# Command: show postcard-telemetry sessions

## Syntax
```
show postcard-telemetry sessions [ <monitorname> ] [ __readonly__ <monitor> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| sessions | Show Session Configuration |
| monitorname | (Optional) Specify a monitor |
| __readonly__ | (Optional) |
| monitor | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3026341920

---

# Command: show postcard-telemetry watchlist

## Syntax
```
show postcard-telemetry watchlist [ name ] [ { <watchlistname> } ] [ __readonly__ <watchlist> <use_count> <description> <num_aces>
 <ace_seq_num> <ace_action> <ace_type> <ace_sip> <ace_sip_len> <ace_dip> <ace_dip_len> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| postcard-telemetry | Show POSTCARD information |
| watchlist | Show watchlist Configuration |
| name | (Optional) Show the configuration for a specific POSTCARD Record |
| watchlistname | (Optional) Specify a watchlist |
| __readonly__ | (Optional) |
| watchlist | (Optional) |
| use_count | (Optional) |
| description | (Optional) |
| num_aces | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2632197199

---

# Command: show power inline

## Syntax
```
show power inline [ __readonly__ { TABLE_fex_info <module_id> <avail_pwr> <used_pwr> <rem_pwr> } { TABLE_intf_info <intf_name>
 <admin> <oper> <supp_pwr> <del_pwr> <device> <class> <max> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| power | Power over Ethernet |
| __readonly__ | (Optional) |
| TABLE_fex_info | (Optional) FEX information |
| module_id | (Optional) FEX id |
| avail_pwr | (Optional) Available power |
| used_pwr | (Optional) Used power |
| rem_pwr | (Optional) Free power |
| TABLE_intf_info | (Optional) Interface information |
| intf_name | (Optional) Interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3103258948

---

# Command: show power inline

## Syntax
```
show power inline <if0> [ __readonly__ { TABLE_intf_info <intf_name> <admin> <oper> <supp_pwr> <del_pwr> <device> <class>
 <max> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| power | Power over Ethernet |
| __readonly__ | (Optional) |
| TABLE_intf_info | (Optional) Interface information |
| intf_name | (Optional) Interface name |
| admin | (Optional) Port mode |
| oper | (Optional) Oper mode |
| supp_pwr | (Optional) Supplied power |
| del_pwr | (Optional) delivered power |
| device | (Optional) Device information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1611371872

---

# Command: show power inline police

## Syntax
```
show power inline police [ __readonly__ { TABLE_police <intf_name> <admin> <oper> <admin_police> <oper_police> <cutoff_pwr>
 <oper_pwr> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| power | Power over Ethernet |
| police | Show per-port policing |
| __readonly__ | (Optional) |
| TABLE_police | (Optional) Police information |
| intf_name | (Optional) Interface name |
| admin | (Optional) Port mode |
| oper | (Optional) Oper mode |
| admin_police | (Optional) Configured admin police |
| oper_police | (Optional) Current police |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1248703402

---

# Command: show power inline priority

## Syntax
```
show power inline priority [ __readonly__ { TABLE_priority <intf_name> <admin> <oper> <priority> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| power | Power over Ethernet |
| priority | Show per-port priority |
| __readonly__ | (Optional) |
| TABLE_priority | (Optional) Port priority information |
| intf_name | (Optional) Interface name |
| admin | (Optional) Port mode |
| oper | (Optional) Oper mode |
| priority | (Optional) port priority |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2438493725

---

# Command: show privilege

## Syntax
```
show privilege [ __readonly__ <user_name> <cur_priv_level> <feature_priv_status> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| privilege | Display privilege information |
| __readonly__ | (Optional) |
| user_name | (Optional) Current user name |
| cur_priv_level | (Optional) Current privilege level |
| feature_priv_status | (Optional) Status of feature privilege |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2506874745

---

# Command: show processes

## Syntax
```
show processes [ __readonly__ { [ TABLE_processes <pid> <state> <pc> <start_cnt> <tty> <p_type> <process> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| __readonly__ | (Optional) |
| TABLE_processes | (Optional) all process information |
| pid | (Optional) process id |
| state | (Optional) process state |
| pc | (Optional) pc register |
| start_cnt | (Optional) TBD |
| tty | (Optional) TBD |
| p_type | (Optional) process type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1253229903

---

# Command: show processes cpu

## Syntax
```
show processes cpu [ sort ] [ __readonly__ { [ TABLE_process_cpu <pid> <runtime> <invoked> <usecs> <onesec> <process> ] [
 <user_percent> ] [ <kernel_percent> ] [ <idle_percent> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| cpu | Show processes CPU Info |
| sort | (Optional) Show processes CPU Info (Sorted by Cpu Util with time base) |
| __readonly__ | (Optional) |
| TABLE_process_cpu | (Optional) all process memory |
| pid | (Optional) process id |
| runtime | (Optional) Runtime |
| invoked | (Optional) Invoked |
| usecs | (Optional) usecs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2538288344

---

# Command: show processes cpu history

## Syntax
```
show processes cpu history
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| cpu | Show processes CPU Info |
| history | Show processes CPU Util History |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2684257040

---

# Command: show processes cpu history data

## Syntax
```
show processes cpu history data [ __readonly__ { [ TABLE_processes_cpu_history <cpu_avg_sec> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| cpu | Show processes CPU Info |
| history | Show processes CPU Util History |
| data | Display the CPU util as data, instead of graph |
| __readonly__ | (Optional) |
| TABLE_processes_cpu_history | (Optional) 60 sec cpu history |
| cpu_avg_sec | (Optional) cpu avg for a sec |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp6192409630

---

# Command: show processes cpu module

## Syntax
```
show processes cpu module <i0> [ __readonly__ { [ TABLE_process_cpu <pid> <runtime> <invoked> <usecs> <onesec> <process> ]
 [ <user_percent> ] [ <kernel_percent> ] [ <idle_percent> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| cpu | Show processes CPU Info |
| module | processes CPU Info |
| i0 | module number |
| __readonly__ | (Optional) |
| TABLE_process_cpu | (Optional) all process memory |
| pid | (Optional) process id |
| runtime | (Optional) Runtime |
| invoked | (Optional) Invoked |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1571827210

---

# Command: show processes log

## Syntax
```
show processes log [ __readonly__ { [ TABLE_processes_log <vdc> <process> <pid> <normal_exit> <stack> <core> <create_time>
 ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| log | Show information about process logs |
| __readonly__ | (Optional) |
| TABLE_processes_log | (Optional) all processes log |
| vdc | (Optional) vdc |
| process | (Optional) vdc process name |
| pid | (Optional) pid |
| normal_exit | (Optional) process exit |
| stack | (Optional) stack |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp7240148700

---

# Command: show processes log details

## Syntax
```
show processes log details [ __readonly__ { line_in_log_detail <line_in_file> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| log | Show information about process logs |
| details | Show detail of all logs with stack |
| __readonly__ | (Optional) |
| line_in_log_detail | (Optional) |
| line_in_file | (Optional) each line |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1119975861

---

# Command: show processes log pid

## Syntax
```
show processes log pid <i0> [ __readonly__ { TABLE_line_in_log_pid <line_in_file> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| log | Show information about process logs |
| pid | Show detail log info about a specific process |
| i0 | pid of the process |
| __readonly__ | (Optional) |
| TABLE_line_in_log_pid | (Optional) |
| line_in_file | (Optional) each line |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2837100199

---

# Command: show processes log vdc-all

## Syntax
```
show processes log vdc-all [ __readonly__ { [ TABLE_processes_log_vdc_all <vdc> <process> <pid> <normal_exit> <stack> <core>
 <create_time> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| TABLE_processes_log_vdc_all | (Optional) all processes log vdc all |
| show | Show running system information |
| processes | Show processes |
| log | Show information about process logs |
| vdc-all | Show information about process logs in all vdc's |
| __readonly__ | (Optional) |
| vdc | (Optional) vdc process name |
| process | (Optional) vdc process name |
| pid | (Optional) process id |
| normal_exit | (Optional) process exit |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3848631016

---

# Command: show processes memory

## Syntax
```
show processes memory [ __readonly__ { TABLE_process_memory <mem_pid> <mem_alloc> <mem_limit> <mem_used> <stack_base_ptr>
 <process> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| memory | Show processes Memory Info |
| __readonly__ | (Optional) |
| TABLE_process_memory | (Optional) all process memory |
| mem_pid | (Optional) process id |
| mem_alloc | (Optional) allocated memory |
| mem_limit | (Optional) memory limit |
| mem_used | (Optional) memory used |
| stack_base_ptr | (Optional) stack and base pointer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp4695432170

---

# Command: show processes memory physical

## Syntax
```
show processes memory physical [ __readonly__ { TABLE_process_physical_memory <processid> <virtual> <physical> <rss> <processname>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| memory | Show processes Memory Info |
| physical | Show processes physical Memory |
| __readonly__ | (Optional) |
| TABLE_process_physical_memory | (Optional) all process physical memory |
| processid | (Optional) process id |
| virtual | (Optional) virtual allocated memory |
| physical | (Optional) physical memory used |
| rss | (Optional) rss memory |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2777722244

---

# Command: show processes memory shared

## Syntax
```
show processes memory shared [ detail &#124; dynamic ] [ __readonly__ TABLE_process_tag [ <process-tag-out> ] [ <process-memory-share-dynamic-component-str>
 ] [ <process-memory-share-dynamic-shared-memory-str> ] [ <process-memory-share-dynamic-current-size-str> ] [ <process-memory-share-dynamic-max-size-str>
 ] [ <process-memory-share-dynamic-used-str> ] [ <process-memory-share-component-str> ] [ <process-memory-share-shared-memory-str>
 ] [ <process-memory-share-size-str> ] [ <process-memory-share-used-str> ] [ <process-memory-share-available-str> ] [ <process-memory-share-ref-str>
 ] [ <process-memory-share-byte-set-address-str> ] [ <process-memory-share-byte-set-count-str> ] [ <process-memory-share-address-str>
 ] [ <process-memory-share-kbytes-1-str> ] [ <process-memory-share-kbytes-2-str> ] [ <process-memory-share-kbytes-3-str> ]
 [ <process-memory-share-count-str> ] [ { TABLE_SMMITEM <process-memory-share-smr-name> } ] [ { TABLE_SHOWPROC <process-memory-share-table-showproc-key>
 [ { TABLE_SHOWONEDYNAMIC [ <process-memory-share-component> ] [ <process-memory-share-shared-memory> ] [ <process-memory-share-current-size>
 ] [ <process-memory-share-max-size> ] [ <process-memory-share-used> ] } ] [ { TABLE_ONEITEM [ <process-memory-share-proc-smr-name>
 ] [ <process-memory-share-smr-addr> ] [ <process-memory-share-smr-size> ] [ <process-memory-share-smr-star-char> ] [ <process-memory-share-smr-empty-char>
 ] [ <process-memory-share-smr-used> ] [ <process-memory-share-smr-avail> ] [ <process-memory-share-smr-ref-count> ] [ <process-memory-share-dynamic-smr-name>
 ] } ] [ { TABLE_ONEITEMDYNAMIC [ <process-memory-share-dynamic-smr-addr> ] [ <process-memory-share-dynamic-smr-size> ] [ <process-memory-share-dynamic-plus-char>
 ] [ <process-memory-share-max-mem-size-str> ] [ <process-memory-share-dynamic-smr-used> ] [ <process-memory-share-dynamic-smr-avail>
 ] [ <process-memory-share-dynamic-smr-ref-count> ] [ <process-memory-share-region-smr-name> ] } ] } ] [ <process-memory-share-total-shm-size>
 ] [ <process-memory-share-total-shm-used> ] [ <process-memory-share-total-shm-avail> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Display process information |
| memory | Display memory information |
| shared | Display shared memory info |
| detail | (Optional) Display shared memory in bytes instead of default kbytes |
| dynamic | (Optional) Display details of dynamic shared memory segments |
| __readonly__ | (Optional) |
| TABLE_process_tag | (Optional) |
| process-tag-out | (Optional) |
| process-memory-share-dynamic-component-str | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3346712276

---

# Command: show processes vdc

## Syntax
```
show processes vdc <e-vdc2> [ __readonly__ { TABLE_processes_vdc <pid> <state> <pc> <start_cnt> <tty> <p_type> <process> }
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| __readonly__ | (Optional) Read only |
| TABLE_processes_vdc | (Optional) All process information |
| pid | (Optional) PID of process |
| state | (Optional) State of process |
| pc | (Optional) PC in which process exists |
| start_cnt | (Optional) TBD |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1607426378

---

# Command: show processes vdc cpu

## Syntax
```
show processes vdc <e-vdc2> cpu [ __readonly__ [ TABLE_process_vdc_cpu <pid> <runtime> <invoked> <usecs> <onesec> <process>
 ] [ <user_percent> ] [ <kernel_percent> ] [ <idle_percent> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| cpu | Show processes CPU Info |
| __readonly__ | (Optional) Readonly table for cpu log |
| TABLE_process_vdc_cpu | (Optional) All cpu process logs of vdc |
| pid | (Optional) PID of process |
| runtime | (Optional) Runtime |
| invoked | (Optional) Invoked |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp8193645940

---

# Command: show processes vdc log

## Syntax
```
show processes vdc <e-vdc2> log [ __readonly__ { [ TABLE_processes_vdc_log <vdc> <process> <pid> <normal_exit> <stack> <core>
 <create_time> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| log | Show information about process logs |
| __readonly__ | (Optional) Read only table |
| TABLE_processes_vdc_log | (Optional) Table for log of all VDC Processes |
| pid | (Optional) PID of process |
| vdc | (Optional) VDC Number |
| process | (Optional) Process name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp4182057291

---

# Command: show processes vdc log details

## Syntax
```
show processes vdc <e-vdc2> log details
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| log | Show information about process logs |
| details | Show detail of all logs with stack |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1622465287

---

# Command: show processes vdc log pid

## Syntax
```
show processes vdc <e-vdc2> log pid <i1>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| log | Show information about process logs |
| pid | Show detail log info about a specific process |
| i1 | pid of the process |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp4041307732

---

# Command: show processes vdc memory

## Syntax
```
show processes vdc <e-vdc2> memory [ __readonly__ { [ TABLE_process_memory <mem_pid> <mem_alloc> <mem_limit> <mem_used> <stack_base_ptr>
 <process> ] [ <sum_mem_malloced> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Show processes |
| vdc | Show processes in vdc |
| e-vdc2 | Enter Virtual Device Context <vdc-id> |
| memory | Show processes Memory Info |
| __readonly__ | (Optional) |
| TABLE_process_memory | (Optional) all process memory |
| mem_pid | (Optional) process id |
| mem_alloc | (Optional) allocated memory |
| mem_limit | (Optional) memory limit |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp2666394657

---

# Command: show processes version

## Syntax
```
show processes { version &#124; threads } [ <comp-string> ] [ __readonly__ TABLE_component <component-name> <version> <buildinfo>
 <sourceversion> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| processes | Display process information |
| version | Display system release information |
| threads | Threads Info |
| comp-string | (Optional) Component name for detailed information |
| __readonly__ | (Optional) |
| TABLE_component | (Optional) |
| component-name | (Optional) |
| version | (Optional) |
| buildinfo | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3041117158

---

# Command: show pss debug

## Syntax
```
show pss debug
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| pss | display pss information |
| debug | display pss debug configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1066246894

---

# Command: show ptp brief

## Syntax
```
show ptp brief [ __readonly__ <gptp-flag> [ TABLE_ptp <ptp-ifindex> <state> [ <dot1as-capable> ] ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| brief | port states in brief |
| __readonly__ | (Optional) Read Only |
| gptp-flag | (Optional) GPTP mode |
| TABLE_ptp | (Optional) ptp table |
| ptp-ifindex | (Optional) ptp ifindex |
| state | (Optional) BMC state |
| dot1as-capable | (Optional) Dot1AS capable |
| ptp-end | (Optional) End of table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1159416044

---

# Command: show ptp clock

## Syntax
```
show ptp clock [ __readonly__ <clock-id> <domain-id> <num-ports> <priority1> <priority2> <class> <accuracy> <scaled-log-variance>
 <offset-from-master> <mean-path-delay-to-master> <steps-removed> <device-type> <encap> <slave-clock-oper> <master-clock-oper>
 <src-ip> <slave-only> [ <correction-threshold> ] [ <mean-path-delay-threshold> ] [ <gmTimeBaseIndicator> ] [ <last_gm_phase_change>
 ] [ <master_cum_scaled_rate_offset> ] [ <scaled_last_gm_freq_change> ] [ <cum_scaled_rate_offset> ] <local-clock-time> <bs-status>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| clock | Set local clock attributes |
| __readonly__ | (Optional) Read only |
| domain-id | (Optional) Domain Id |
| clock-id | (Optional) Clock Id |
| priority1 | (Optional) Priority 1 |
| priority2 | (Optional) Priority 2 |
| num-ports | (Optional) Number of PTP ports |
| class | (Optional) Class |
| accuracy | (Optional) Clock accuracy |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1298366393

---

# Command: show ptp clock foreign-masters record

## Syntax
```
show ptp clock foreign-masters record [ interface <if0> ] [ __readonly__ [ TABLE_ptp <interface-name> <clock-id> <priority1>
 <priority2> <class> <accuracy> <scaled-log-variance> <steps-removed> <is-gm> ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| clock | Set local clock attributes |
| foreign-masters | foreign-masters |
| record | record |
| if0 | (Optional) |
| __readonly__ | (Optional) Read only |
| TABLE_ptp | (Optional) ptp table |
| interface-name | (Optional) interface name |
| clock-id | (Optional) Clock Id |
| priority1 | (Optional) Priority 1 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3237744069

---

# Command: show ptp corrections

## Syntax
```
show ptp corrections [ entries <val> ] [ __readonly__ <ptp-header> [ TABLE_ptp <intf-name> <sup-time> <correction-val> <mean-path-delay>
 ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| __readonly__ | (Optional) Read Only |
| corrections | Display last few corrections |
| entries | (Optional) Latest entries to display |
| val | (Optional) Number of latest entries to display |
| ptp-header | (Optional) Start of table |
| TABLE_ptp | (Optional) ptp table |
| intf-name | (Optional) interface name |
| sup-time | (Optional) sup time |
| correction-val | (Optional) correction value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1909281298

---

# Command: show ptp cost

## Syntax
```
show ptp cost [ interface <if0> ] [ __readonly__ [ TABLE_ptp <ptp-ifindex> <cost> ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| cost | port costs |
| if0 | (Optional) |
| __readonly__ | (Optional) Read Only |
| TABLE_ptp | (Optional) ptp table |
| ptp-ifindex | (Optional) ptp ifindex |
| cost | (Optional) cost |
| ptp-end | (Optional) End of table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3265457630

---

# Command: show ptp counters interface

## Syntax
```
show ptp counters { interface <if0> &#124; all } [ { detail &#124; ipv4 <ip> } ] [ __readonly__ [ TABLE_ptp <interface_name> [ <accepted-ip>
 ] <tx-announce-pkts> <rx-announce-pkts> <tx-sync-pkts> <rx-sync-pkts> <tx-follow-up-pkts> <rx-follow-up-pkts> <tx-delay-req-pkts>
 <rx-delay-req-pkts> <tx-delay-resp-pkts> <rx-delay-resp-pkts> <tx-pdelay-req-pkts> <rx-pdelay-req-pkts> <tx-pdelay-resp-pkts>
 <rx-pdelay-resp-pkts> <tx-pdelay-follow-up-pkts> <rx-pdelay-follow-up-pkts> [ <tx-mgmt-pkts> ] [ <rx-mgmt-pkts> ] ] <ptp-end>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| __readonly__ | (Optional) Read Only |
| counters | Display PTP packet counters |
| interface | Enter the port interface |
| all | Displays all information |
| detail | (Optional) Show detail |
| ipv4 | (Optional) IP address for the stat info |
| ip | (Optional) IPv4 address (A.B.C.D) |
| TABLE_ptp | (Optional) ptp table |
| interface_name | (Optional) interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2627794788

---

# Command: show ptp delay summary

## Syntax
```
show ptp delay summary [ __readonly__ [ TABLE_ptp <intf-name-port> <device-type> <state> <link-delay> ] [ <ptp-end> ] [ <gptp-not-supported>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| delay | delay |
| summary | summary |
| __readonly__ | (Optional) Read only |
| TABLE_ptp | (Optional) ptp table |
| intf-name-port | (Optional) interface name and port |
| device-type | (Optional) Device Type |
| state | (Optional) BMC state |
| link-delay | (Optional) link delay |
| ptp-end | (Optional) End of table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1693113460

---

# Command: show ptp domain data

## Syntax
```
show ptp domain data [ __readonly__ [ TABLE_ptp <multidom_cap> <gm_cap> <gm_convergence_time> <def_dom> <transition_priority1>
 <transition_priority2> [ TABLE_ptp_domain <domain_number> <domain_priority> <ptp_clock_class_threshold> <ptp_clock_accuracy_threshold>
 <ptp-ifindex> ] ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| domain | ptp domain number |
| data | ptp domain data |
| __readonly__ | (Optional) Read Only |
| TABLE_ptp | (Optional) ptp table |
| multidom_cap | (Optional) Multidomain state ENABLED/DISABLED |
| gm_cap | (Optional) GM state ENABLE/DISABLED |
| gm_convergence_time | (Optional) ptp grandmaster convergence time |
| def_dom | (Optional) ptp default domain |
| transition_priority1 | (Optional) ptp multi-domain transition priority1 |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1671779627

---

# Command: show ptp interface domain

## Syntax
```
show ptp interface domain [ __readonly__ [ TABLE_ptp <ptp-ifindex> <interface-domain> ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| interface | port |
| domain | ptp port domain |
| __readonly__ | (Optional) Read Only |
| TABLE_ptp | (Optional) ptp table |
| ptp-ifindex | (Optional) ptp ifindex |
| interface-domain | (Optional) ptp port domain |
| ptp-end | (Optional) End of table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1969276181

---

# Command: show ptp packet-trace

## Syntax
```
show ptp packet-trace [ __readonly__ <ptp-header> [ TABLE_ptp <intf-name> <sup-time> <pkt_dir> <pkt_type> <pkt_info> ] <ptp-end>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| __readonly__ | (Optional) Read Only |
| packet-trace | Display last few pkt traces |
| ptp-header | (Optional) Start of table |
| TABLE_ptp | (Optional) ptp table |
| intf-name | (Optional) interface name |
| sup-time | (Optional) sup time |
| pkt_dir | (Optional) pkt_dir |
| pkt_type | (Optional) pkt_type |
| pkt_info | (Optional) pkt_info |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp3064071974

---

# Command: show ptp parent

## Syntax
```
show ptp parent [ __readonly__ <clock-id> <port-num> <obs-parent-offset> <obs-parent-clk-phase-chg> [ <parent-ip> ] <gm-id>
 <gm-class> <gm-accuracy> <gm-scaled-log-variance> <gm-priority1> <gm-priority2> [ TABLE-path-trace <path-trace-index> <path-trace-clock-id>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| parent | parent clock |
| __readonly__ | (Optional) Read only |
| clock-id | (Optional) Clock Id |
| port-num | (Optional) Port ID: port number |
| obs-parent-offset | (Optional) observed parent offset |
| obs-parent-clk-phase-chg | (Optional) observed parent clock phase change |
| parent-ip | (Optional) Parent clock IP |
| gm-id | (Optional) Grandmaster Id |
| gm-class | (Optional) Class |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, S-commands
**Command ID:** wp1711439760

---

# Command: show ptp port interface

## Syntax
```
show ptp port interface <if0> [ __readonly__ [ TABLE_ptp <intf-name> <clock-id> <port-num> <version> [ <transport-mode> ]
 [ <accepted-ip> ] <state> <vlan> <delay-req-intv> <ann-rx-tout> <peer-mean-path-delay> <ann-intv> <sync-intv> <delay-mechanism>
 [ <peer-delay-req-intv> ] [ <device-type> ] [ <encap> ] [ <prop-delay-thresh> ] [ <neighbor-rate-ratio> ] <cost> <int-domain-id>
 ] <ptp-end> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| port | port |
| interface | Enter the port interface |
| __readonly__ | (Optional) Read only |
| TABLE_ptp | (Optional) ptp table |
| intf-name | (Optional) interface name |
| clock-id | (Optional) Port ID: Clock Id |
| port-num | (Optional) Port ID: port number |
| version | (Optional) version |
| transport-mode | (Optional) Transport mode |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2470110750

---

# Command: show ptp time-property

## Syntax
```
show ptp time-property [ __readonly__ <current-utc-offset-valid> <current-utc-offset> <leap-59> <leap-61> <time-traceable>
 <freq-traceable> <ptp-timescale> <time-source> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| ptp | Precision Time Protocol (IEEE 1588) Subsystem |
| time-property | time property |
| __readonly__ | (Optional) Read only |
| current-utc-offset-valid | (Optional) current_utc_offset_valid |
| current-utc-offset | (Optional) current_utc_offset |
| leap-59 | (Optional) leap-59 |
| leap-61 | (Optional) leap-61 |
| time-traceable | (Optional) time-traceable |
| freq-traceable | (Optional) freq-traceable |
| ptp-timescale | (Optional) ptp-timescale |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01111.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3867658898

---

