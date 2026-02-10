# Chapter: N Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01101.html
**Type:** Show Commands  
**Chapter:** Group-1101 Commands  
**Total Commands:** 59

## Command List

- `show nat itd`
- `show nbm defaults`
- `show nbm flow-policy`
- `show nbm flows`
- `show nbm flows static`
- `show nbm flows statistics`
- `show nbm flows summary`
- `show nbm host-policy all`
- `show nbm host-policy applied receiver`
- `show nbm host-policy applied sender`
- `show nbm interface bandwidth`
- `show ngoam interface statistics`
- `show ngoam loopback`
- `show ngoam mct-stats`
- `show ngoam pathtrace`
- `show ngoam probe`
- `show ngoam traceroute statistics`
- `show ngoam xconnect session`
- `show npv external-interface-usage`
- `show npv flogi-table`
- `show npv status`
- `show npv traffic-map`
- `show ntp access-groups`
- `show ntp authentication-keys`
- `show ntp authentication-status`
- `show ntp information`
- `show ntp logging-status`
- `show ntp peer-status`
- `show ntp peers`
- `show ntp rts-update`
- `show ntp session status`
- `show ntp source-interface`
- `show ntp source`
- `show ntp statistics`
- `show ntp status`
- `show ntp trusted-keys`
- `show nve adjacency mpls`
- `show nve bfd neighbors`
- `show nve core-links`
- `show nve ethernet-segment`
- `show nve evi`
- `show nve interface`
- `show nve mpls`
- `show nve multisite dci-links`
- `show nve multisite fabric-links`
- `show nve peers`
- `show nve peers interface counters`
- `show nve peers mpls`
- `show nve peers vni interface counters`
- `show nve replication-servers`
- `show nve vni`
- `show nve vni counters`
- `show nve vni ingress-replication`
- `show nve vni peer-vtep`
- `show nve vrf`
- `show nve vxlan-params`
- `show nxapi-server logs`
- `show nxapi`
- `show nxapi syntax`

---

## Detailed Command Reference

# Command: show nat itd

## Syntax
```
show nat itd [ __readonly__ [ { TABLE_NAT_ITD_configurations [ <nat_itd_acl_name> ] [ <nat_itd_globalip> ] [ <nat_itd_globalport>
 ] [ <nat_itd_localip> ] [ <nat_itd_localport> ] [ <nat_itd_proto> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nat | IP NAT information |
| itd | IP NAT ITD |
| __readonly__ | (Optional) |
| TABLE_NAT_ITD_configurations | (Optional) NAT ITD Configurations |
| nat_itd_acl_name | (Optional) NAT ITD ACL name |
| nat_itd_globalip | (Optional) NAT ITD Global Ip address |
| nat_itd_globalport | (Optional) NAT ITD Global port |
| nat_itd_localip | (Optional) NAT ITD Local Ip address |
| nat_itd_localport | (Optional) NAT ITD Local port |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2959720881

---

# Command: show nbm defaults

## Syntax
```
show nbm defaults [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all } ] [ __readonly__ TABLE_vrf <vrfName> { <contextId> <bandwidthInKbps>
 <dscp> <qid> <policer> <operModeCache> <operMode> <unicastFabricBandwidth> <numAsmGroup> } [ TABLE_ASM <groupId> { <groupPrefix>
 <groupMaskLen> } ] { <senderPolicy> <localReceiverPolicy> <externalReceiverPolicy> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| defaults | Default config |
| vrf | (Optional) Display per-VRF information |
| all | (Optional) Display all VRFs |
| vrf-name | (Optional) VRF name |
| nbm-vrf-known-name | (Optional) NBM VRF Name |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) VRF table |
| vrfName | (Optional) VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp4063985059

---

# Command: show nbm flow-policy

## Syntax
```
show nbm flow-policy [ name { <policy-name> } ] [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all } ] [ __readonly__ TABLE_vrf
 { <vrfName> [ <policyName> ] [ { <defaultBandwidthKbps> <defaultDscp> <defaultQos> <defaultPolicer> } ] [ { TABLE_flow_policy
 <groupRange> <bandwidthKbps> <dscp> <qos> <policer> <policyName> } ] <numGroupRanges> <numPolicies> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| flow-policy | Flow policy show command |
| name | (Optional) Policy name |
| policy-name | (Optional) Policy name value |
| vrf | (Optional) Display per-VRF information |
| all | (Optional) Display all VRFs |
| vrf-name | (Optional) VRF name |
| nbm-vrf-known-name | (Optional) NBM VRF Name |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1835478876

---

# Command: show nbm flows

## Syntax
```
show nbm flows [ group-based [ group <group-ip> ] &#124; { flow-policy { <cfg-pol-name> &#124; <unknown-pol-name> } } &#124; source <source-ip>
 [ group <group-ip> ] &#124; group <group-ip> [ source <source-ip> ] &#124; interface <if-name> &#124; logical-id { none &#124; any &#124; <lid-val>
 } &#124; profile-id <prof-id> ] [ all &#124; active &#124; inactive &#124; no-receiver ] [ detail ] [ vrf { <vrf-name> &#124; <nbm-vrf-known-name>
 &#124; all } ] [ __readonly__ [ TABLE_vrf <vrf-name> [ TABLE_flows { <mcast_grp> <src_ip> [ <start_time> ] <uptime> <src_intf>
 <src_nbr_device> [ <lid> <profile> <status> ] <num_rx> <bw_mbps> [ <cfg_mbps> ] <src_slot> <src_unit> <src_slice> } [ { <act_slot>
 <act_unit> <stdby_slot> <stdby_unit> } ] { <dscp> <qos> [ <owner_type> ] <policed> [ <is_fhr> ] <pol_name> } [ <flag> ] [
 TABLE_num_int_links { <n_link> <num_links> } ] [ TABLE_int_links { <iiod> <ilink> <i_ifidx> <fab_iiod> <fab_oiod> <fab_ifidx>
 <oiod> <olink> <i_ieth_port> <fab_ieth_port> } ] [ TABLE_oifs { [ <oif_num> ] <oif_slot> <oif_unit> <oif_slot_unit_num_rx>
 <oif_if_idx> <oif_iod> <oif_name> <oif_nbr_device> } ] [ { <end_timestr> <flow_rate_bps> <packets> <bytes> } ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| flows | NBM flows (default will be active flows) |
| active | (Optional) Active flows (default) |
| inactive | (Optional) Inactive flows |
| no-receiver | (Optional) Flows without any receiver |
| all | (Optional) Both active and inactive flows |
| group-based | (Optional) Multicast group based (*,G) flows to IGMP receivers |
| flow-policy | (Optional) Flow policy |
| cfg-pol-name | (Optional) Policy name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1429562795

---

# Command: show nbm flows static

## Syntax
```
show nbm flows static [ group <grp> ] [ source <src> ] [ stitched &#124; unstitched ] [ vrf { <vrf-name> &#124; <nbm-vrf-known-name>
 &#124; all } ] [ __readonly__ { [ TABLE_vrf <vrf-name> [ TABLE_stitched { <stitchedSrc> <stitchedGrp> [ TABLE_stitchedEgress {
 <stitchedEgressIntf> } ] [ TABLE_stitchedHost { <stitchedHostIp> } ] } ] [ TABLE_unstitched { <unstitchedSrc> <unstitchedGrp>
 [ TABLE_unstitchedEgress { <unstitchedEgressIntf> } ] [ TABLE_unstitchedHost { <unstitchedHostIp> } ] } ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| flows | NBM flows (default will be active flows) |
| static | Static NBM Flows |
| group | (Optional) Multicast group |
| grp | (Optional) Multicast group address |
| source | (Optional) Source ip of sender |
| src | (Optional) Source address |
| stitched | (Optional) Show only successfully provisioned oif |
| unstitched | (Optional) Show only failed to provision oif |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp4753908950

---

# Command: show nbm flows statistics

## Syntax
```
show nbm flows statistics [ group-based [ group <group-ip> ] &#124; source <source-ip> [ group <group-ip> ] &#124; group <group-ip>
 [ source <source-ip> ] &#124; { flow-policy { <cfg-pol-name> &#124; <unknown-pol-name> } } &#124; interface <if-name> &#124; logical-id { none
 &#124; any &#124; <lid-val> } &#124; profile-id <prof-id> ] [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all } ] [ __readonly__ { [ TABLE_vrf
 <vrf-name> [ TABLE_stats { <mcast_grp> <src_ip> [ <start_time> ] <uptime> <src_intf> <packets> <bytes> <allow_bytes> <drop_bytes>
 } ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| flows | NBM flows |
| statistics | Flow statistics |
| group-based | (Optional) Multicast group based (*,G) flows to IGMP receivers |
| source | (Optional) Source IP address |
| source-ip | (Optional) Source IP address value |
| group | (Optional) Multicast group |
| group-ip | (Optional) Multicast group address value |
| flow-policy | (Optional) Flow policy |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp5403584650

---

# Command: show nbm flows summary

## Syntax
```
show nbm flows summary [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all } ] [ __readonly__ [ TABLE_vrf <vrf-name> [ TABLE_flows_summary
 <flow_type> <starg> <sg> <total> ] [ TABLE_flows_summary_per_rpf <if-name> <starg> <sg> <total> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| flows | NBM Flows |
| summary | NBM Flow Summary |
| vrf | (Optional) Display per-VRF information |
| all | (Optional) Display all VRFs |
| vrf-name | (Optional) VRF name |
| nbm-vrf-known-name | (Optional) NBM VRF Name |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) VRF table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1354905137

---

# Command: show nbm host-policy all

## Syntax
```
show nbm host-policy all { sender &#124; { receiver { local &#124; external } } } [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all }
 ] [ __readonly__ [ TABLE_vrf <vrf-name> <policyType> <defaultHostPolicy> [ TABLE_host_policies <seqNum> <source> <group> <groupMask>
 [ <host> ] <permission> ] <numPolicies> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| host-policy | Host policy |
| all | All policies on switch |
| sender | Sender Policy |
| receiver | Receiver Policy |
| local | Local receiver policy |
| external | External receiver policy |
| vrf | (Optional) Display per-VRF information |
| all | (Optional) Display all VRFs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp2627352527

---

# Command: show nbm host-policy applied receiver

## Syntax
```
show nbm host-policy applied receiver { { { local { all &#124; wildcard } &#124; external } [ vrf { <vrf-name> &#124; <nbm-vrf-known-name>
 &#124; all } ] } &#124; { local interface <if-name> } } [ __readonly__ [ TABLE_vrf <vrf-name> <policyType> <defaultHostPolicy> [ TABLE_interface
 <ifName> [ TABLE_host_policies <seqNum> <source> <group> <groupMask> <permission> <denyCounter> ] ] [ TABLE_wildcard_policies
 <seqNumWildcard> <sourceWildcard> <groupWildcard> <groupMaskWildcard> <permissionWildcard> <denyCounterWildcard> ] <numPolicies>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| host-policy | Host policy |
| applied | Applied policies only |
| receiver | Receiver Policy |
| local | Local receiver policy |
| all | All policies on switch |
| wildcard | All wildcard policies |
| external | External receiver policy |
| vrf | (Optional) Display per-VRF information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp1858845049

---

# Command: show nbm host-policy applied sender

## Syntax
```
show nbm host-policy applied sender { { { all &#124; wildcard } [ vrf { <vrf-name> &#124; <nbm-vrf-known-name> &#124; all } ] } &#124; { interface
 <if-name> } } [ __readonly__ [ TABLE_vrf <vrf-name> <policyType> <defaultHostPolicy> [ TABLE_interface <ifName> [ TABLE_host_policies
 <seqNum> <source> <group> <groupMask> <permission> ] ] [ TABLE_wildcard_policies <seqNumWildcard> <sourceWildcard> <groupWildcard>
 <groupMaskWildcard> <permissionWildcard> ] <numPolicies> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| host-policy | Host policy |
| applied | Applied policies only |
| sender | Sender Policy |
| all | All policies on switch |
| wildcard | Wildcard host policy |
| vrf | (Optional) Display per-VRF information |
| all | (Optional) Display all VRFs |
| vrf-name | (Optional) VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3004460605

---

# Command: show nbm interface bandwidth

## Syntax
```
show nbm interface bandwidth [ __readonly__ [ TABLE_bw { <index> <ifname> <iod> <slot> <unit> <slice> <ingr_fl_bw_available>
 <ingr_fl_bw_usable> <ingr_fl_bw_capacity> <egr_fl_bw_available> <egr_fl_bw_usable> <egr_fl_bw_capacity> <nbr_dev_id> <nbr_dev_name>
 <external> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nbm | Non Blocking Multicast |
| interface | interface |
| bandwidth | Bandwidth interface table |
| __readonly__ | (Optional) |
| TABLE_bw | (Optional) TABLE Bandwidth |
| index | (Optional) Index |
| ifname | (Optional) Interface |
| iod | (Optional) IOD |
| slot | (Optional) SLOT |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, qos, S-commands
**Command ID:** wp1816656838

---

# Command: show ngoam interface statistics

## Syntax
```
show ngoam interface statistics [ __readonly__ [ TABLE_stats { <interface-name> <tx> <rx> } <statistics-end> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| TABLE_stats | (Optional) interface statistics table |
| interface-name | (Optional) interface namestring |
| tx | (Optional) ngoam probe transmit on the interface |
| rx | (Optional) ngoam probe receive on the interface |
| show | Show running system information |
| ngoam | ngoam |
| interface | probe packet interface |
| statistics | ngoam probe interface statistics |
| __readonly__ | (Optional) Read Only |
| statistics-end | (Optional) statistics table end marker |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4069319387

---

# Command: show ngoam loopback

## Syntax
```
show ngoam loopback { { statistics { session { <handle> &#124; all } &#124; summary } } &#124; { status { session { <handle> &#124; all } } }
 } [ __readonly__ [ TABLE_statistics { <sender-handle> [ <connect-check-id> ] <last-clear-stats> TABLE_stats_attr { <stat-attr>
 <stat-value> } } ] [ TABLE_status { <st-sender-handle> <type> <state> } ] [ TABLE_statistics_summary { <last-clear-summary-stats>
 <tx> <rx> <timeout> <unsent> <req-sw-fwd> <req-drop> <resp-tx> <resp-rx> <resp-unsent> <resp-dup> <resp-sw-fwd> <resp-drop>
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | ngoam |
| loopback | ngoam loopback |
| statistics | ngoam loopback statistics |
| summary | ngoam loopback statistics summary |
| status | ngoam loopback status |
| session | ngoam loopback session |
| session | ngoam loopback session |
| handle | ngoam loopback session handle |
| handle | ngoam loopback session handle |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3607870280

---

# Command: show ngoam mct-stats

## Syntax
```
show ngoam mct-stats [ __readonly__ <sent> <rcvd> <resp-sent> <resp-rcvd> <send-fail> <rcv-fail> <send-rel-fail> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | Configure ngoam |
| mct-stats | Print MCT stats |
| __readonly__ | (Optional) Read Only |
| sent | (Optional) Counters |
| rcvd | (Optional) Counters |
| resp-sent | (Optional) Counters |
| resp-rcvd | (Optional) Counters |
| send-fail | (Optional) Counters |
| rcv-fail | (Optional) Counters |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1017042150

---

# Command: show ngoam pathtrace

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | ngoam |
| pathtrace | ngoam pathtrace |
| statistics | ngoam pathtrace statistics |
| summary | ngoam pathtrace statistics summary |
| session | ngoam pathtrace session |
| handle | ngoam pathtrace session handle |
| all | Display results for all pathtrace sessions |
| database | ngoam pathtrace results from the database |
| session | ngoam pathtrace session |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2370263671

---

# Command: show ngoam probe

## Syntax
```
show ngoam probe { { statistics { summary &#124; { session { <handle> &#124; all } } } } } [ __readonly__ [ TABLE_stats { <sender-handle>
 <transaction-id> <dst-vip> <vni> <oam-type> <flow-str> <last-clear-stats> <req-sent> <req-not-sent> } <statistics-end> ] [
 TABLE_summary { <last-clear-summary-stats> <tx> <rx> <timeout> <unsent> <resp-tx> <resp-rx> <resp-unsent> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | ngoam |
| probe | ngoam probe |
| statistics | ngoam probe statistics |
| summary | ngoam probe statistics summary |
| session | ngoam probe session |
| handle | ngoam probe session handle |
| all | Display results for all probe sessions |
| TABLE_stats | (Optional) statistics table |
| sender-handle | (Optional) sender handle |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1496202905

---

# Command: show ngoam traceroute statistics

## Syntax
```
show ngoam traceroute statistics { summary &#124; { session { <handle> &#124; all } } } [ __readonly__ [ TABLE_stats { <sender-handle>
 <last-clear-stats> TABLE_stats_attr { <stat-attr> <stat-value> } } ] [ TABLE_summary { <last-clear-summary-stats> <tx> <rx>
 <timeout> <unsent> <resp-tx> <resp-rx> <resp-unsent> <resp-dup> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | ngoam |
| traceroute | ngoam traceroute |
| statistics | ngoam traceroute statistics |
| summary | ngoam traceroute statistics summary |
| session | ngoam traceroute session |
| handle | ngoam traceroute session handle |
| all | Display results for all traceroute sessions |
| TABLE_stats | (Optional) statistics table |
| sender-handle | (Optional) sender handle |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3944231969

---

# Command: show ngoam xconnect session

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ngoam | ngoam information |
| xconnect | crossconnect info |
| session | xc session id |
| id | Vlan-id of the xc |
| iodb | (Optional) Iodb |
| all | show summary info for all sessions |
| __readonly__ | (Optional) Read Only |
| TABLE_xc_db_summary | (Optional) XC Db table |
| ENTRY_xc_db_detail | (Optional) XC Db detail |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2493172081

---

# Command: show npv external-interface-usage

## Syntax
```
show npv external-interface-usage [ server-interface <if0> ] [ __readonly__ { TABLE_intf_usage <svr_intf> <ext_intf> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| npv | Show information about NPV |
| external-interface-usage | Show external interface usage by server interfaces |
| server-interface | (Optional) Show external interface usage by a server interface |
| if0 | (Optional) |
| __readonly__ | (Optional) Read Only |
| TABLE_intf_usage | (Optional) External Interfaces Usage Table |
| svr_intf | (Optional) Server Interface |
| ext_intf | (Optional) External Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp4654422810

---

# Command: show npv flogi-table

## Syntax
```
show npv flogi-table [ { interface <if0> &#124; vsan <i0> } ] [ __readonly__ [ [ TABLE_flogi <svr_intf> <vsan_id> <fcid> <pwwn>
 <ext_intf> <nwwn> ] [ <flogi_count> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| npv | Show information about NPV |
| flogi-table | Show information about FLOGI sessions |
| interface | (Optional) Show information about FLOGI sessions for a server interface |
| if0 | (Optional) |
| vsan | (Optional) Show information about FLOGI sessions for a VSAN |
| i0 | (Optional) |
| __readonly__ | (Optional) Read Only |
| TABLE_flogi | (Optional) FLOGI Table |
| svr_intf | (Optional) Server Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2624055820

---

# Command: show npv status

## Syntax
```
show npv status [ vsan <i0> ] [ __readonly__ [ [ <npiv_status> ] [ <load_balance> ] [ { TABLE_extintf <ext_intf> [ <ext_vsan>
 ] [ <ext_fcid> ] <ext_state> [ { TABLE_vsan <vsan_vsan> <vsan_state> [ <vsan_fcid> ] } ] } ] <ext_intf_count> [ { TABLE_svrintf
 <svr_intf> <svr_vsan> <svr_state> } ] <svr_intf_count> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| npv | Show information about NPV |
| status | Show NPV status |
| vsan | (Optional) Show NPV status for a specific VSAN |
| i0 | (Optional) |
| __readonly__ | (Optional) Read Only |
| npiv_status | (Optional) NPIV enable/disable status |
| load_balance | (Optional) disruptive load balance status |
| TABLE_extintf | (Optional) External Interfaces Table |
| ext_intf | (Optional) External Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp5197966530

---

# Command: show npv traffic-map

## Syntax
```
show npv traffic-map [ server-interface <if0> ] [ __readonly__ [ { TABLE_traffic_map <svr_intf> <ext_intf> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| npv | Show information about NPV |
| traffic-map | Show information about Traffic Map |
| server-interface | (Optional) Show information about Traffic map for a server interface |
| if0 | (Optional) |
| __readonly__ | (Optional) Read Only |
| TABLE_traffic_map | (Optional) Traffic Map Table |
| svr_intf | (Optional) Server Interface |
| ext_intf | (Optional) External Interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2899333685

---

# Command: show ntp access-groups

## Syntax
```
show ntp access-groups [ __readonly__ [ <matchall> ] [ { TABLE_accessgroups <accesslist> [ <type> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| access-groups | Display NTP access groups |
| __readonly__ | (Optional) |
| matchall | (Optional) matchall |
| TABLE_accessgroups | (Optional) accessgroups |
| accesslist | (Optional) accesslist |
| type | (Optional) type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2426925954

---

# Command: show ntp authentication-keys

## Syntax
```
show ntp authentication-keys [ __readonly__ [ { TABLE_authkeys <Authkey> [ <MD5String> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| authentication-keys | Display authentication keys |
| __readonly__ | (Optional) |
| TABLE_authkeys | (Optional) authentication keys |
| Authkey | (Optional) authentication key |
| MD5String | (Optional) password |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp5827503660

---

# Command: show ntp authentication-status

## Syntax
```
show ntp authentication-status [ __readonly__ [ <authentication> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| authentication-status | NTP Authentication Status |
| __readonly__ | (Optional) |
| authentication | (Optional) authentication enabled/disabled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp9432564270

---

# Command: show ntp information

## Syntax
```
show ntp information [ __readonly__ [ <system_type> ] [ <software_version> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| information | Show ntp information |
| __readonly__ | (Optional) |
| system_type | (Optional) Ntp System Type |
| software_version | (Optional) Ntp Software Version |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3363717446

---

# Command: show ntp logging-status

## Syntax
```
show ntp logging-status [ __readonly__ [ <loggingstatus> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| logging-status | Display NTP logging status |
| __readonly__ | (Optional) |
| loggingstatus | (Optional) logging enabled/disabled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, management, S-commands
**Command ID:** wp2825302005

---

# Command: show ntp peer-status

## Syntax
```
show ntp peer-status [ __readonly__ [ <totalpeers> ] [ { TABLE_peersstatus <syncmode> <remote> <local> <st> <poll> <reach>
 <delay> [ <vrf> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| peer-status | Show the status for all the server/peers |
| __readonly__ | (Optional) |
| totalpeers | (Optional) totalpeers |
| TABLE_peersstatus | (Optional) peersstatus |
| syncmode | (Optional) peermode |
| remote | (Optional) remote addr |
| local | (Optional) local addr |
| st | (Optional) stratum |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3165397088

---

# Command: show ntp peers

## Syntax
```
show ntp peers [ __readonly__ [ { TABLE_peers <PeerIPAddress> <serv_peer> <conf_flag> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| peers | Show all the peers. |
| __readonly__ | (Optional) |
| TABLE_peers | (Optional) peers |
| PeerIPAddress | (Optional) peer Ip addr |
| serv_peer | (Optional) server or peer |
| conf_flag | (Optional) configured or dynamic |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2860070915

---

# Command: show ntp rts-update

## Syntax
```
show ntp rts-update [ __readonly__ [ <rtsupdate> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| rts-update | Show if the RTS update is enabled |
| __readonly__ | (Optional) |
| rtsupdate | (Optional) rts update enabled/disabled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1210004053

---

# Command: show ntp session status

## Syntax
```
show ntp session status [ __readonly__ [ <session_status> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| session | Show the session information |
| status | Show the session status |
| __readonly__ | (Optional) |
| session_status | (Optional) last session status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp3194323150

---

# Command: show ntp source-interface

## Syntax
```
show ntp source-interface [ __readonly__ [ <sourceinterface> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| source-interface | Source interface configured |
| __readonly__ | (Optional) |
| sourceinterface | (Optional) source interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, system, S-commands
**Command ID:** wp1795171222

---

# Command: show ntp source

## Syntax
```
show ntp source [ __readonly__ [ { TABLE_sourceip <sourceip> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| source | Source IP address configured |
| __readonly__ | (Optional) |
| TABLE_sourceip | (Optional) source ip table |
| sourceip | (Optional) source ip addr |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2301313906

---

# Command: show ntp statistics

## Syntax
```
show ntp statistics { [ io ] &#124; [ local ] &#124; [ memory ] &#124; peer { ipaddr { <ipv4_0> &#124; <ipv6_1> } &#124; name <s0> } } [ __readonly__
 [ { <iotimesincereset> <ioreceivebuffers> <iofreereceivebuffers> <iousedreceivebuffers> <iolowwaterrefills> <iodroppedpackets>
 <ioignoredpackets> <ioreceivedpackets> <iopacketssent> <iopacketsnotsent> <iointerruptshandled> <ioreceivedbyint> } ] [ {
 <localsystemuptime> <localtimesincereset> <localoldversionpackets> <localnewversionpackets> <localunknownversionnumber> <localbadpacketformat>
 <localpacketsprocessed> <localbadauthentication> [ <localpacketsrejected> ] } ] [ { <memtimesincereset> <memtotalpeermemory>
 <memfreepeermemory> <memcallstofindpeer> <memnewpeerallocations> <mempeerdemobilizations> <memhashtablecounts> } ] [ { <peeripremotehost>
 <peeriplocalinterface> <peeriptimelastreceived> <peeriptimeuntilnextsend> <peeripreachabilitychange> <peerippacketssent> <peerippacketsreceived>
 <peeripbadauthentication> <peeripbogusorigin> <peeripduplicate> <peeripbaddispersion> <peeripbadreferencetime> <peeripcandidateorder>
 } ] [ { <peernameremotehost> <peernamelocalinterface> <peernametimelastreceived> <peernametimeuntilnextsend> <peernamereachabilitychange>
 <peernamepacketssent> <peernamepacketsreceived> <peernamebadauthentication> <peernamebogusorigin> <peernameduplicate> <peernameduplicate>
 <peernamebaddispersion> <peernamebadreferencetime> <peernamecandidateorder> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| statistics | Show the NTP statistics |
| io | (Optional) Show the input-output statistics. |
| local | (Optional) Show the counters maintained by the local NTP. |
| memory | (Optional) Show the statistics counters related to memory code. |
| peer | Show the per-peer statistics counter of a peer. |
| ipaddr | Peer's IP address |
| name | Peer's Name |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2685229590

---

# Command: show ntp status

## Syntax
```
show ntp status [ __readonly__ [ <distribution> ] [ <operational_state> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| status | Show the NTP distribution status |
| __readonly__ | (Optional) |
| distribution | (Optional) distribution enabled/disabled |
| operational_state | (Optional) last operation status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1657488126

---

# Command: show ntp trusted-keys

## Syntax
```
show ntp trusted-keys [ __readonly__ [ { TABLE_trustkeys <key> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ntp | Show NTP information |
| trusted-keys | Display trusted keys |
| __readonly__ | (Optional) |
| TABLE_trustkeys | (Optional) trusted keys |
| key | (Optional) trusted key |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2467166904

---

# Command: show nve adjacency mpls

## Syntax
```
show nve adjacency mpls [ __readonly__ TABLE_nve_mpls_adj [ { <peer-ip> &#124; <peer-ipv6> } <evi> <label-sr> <learn-mask> <pending-state>
 <adj-state> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| adjacency | Downstream Adjacencies |
| mpls | Segment routing |
| __readonly__ | (Optional) |
| TABLE_nve_mpls_adj | (Optional) xml schema for sr nve parameters |
| peer-ip | (Optional) Peer IP address v4 |
| evi | (Optional) EVI value |
| label-sr | (Optional) SR Label |
| learn-mask | (Optional) Learn mask for the peer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1647310983

---

# Command: show nve bfd neighbors

## Syntax
```
show nve bfd neighbors [ __readonly__ [ TABLE_nve_bfd_neighbors <if-name> [ { <neighbor-vtep-ip> <neighbor-inner-ip> <neighbor-inner-mac>
 <neighbor-cc-state> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| bfd | BFD |
| neighbors | neighbors |
| __readonly__ | (Optional) |
| TABLE_nve_bfd_neighbors | (Optional) BFD neighbors schema |
| if-name | (Optional) if-name |
| neighbor-vtep-ip | (Optional) Remote VTEP IP address |
| neighbor-inner-ip | (Optional) Remote VTEP Inner IP address |
| neighbor-inner-mac | (Optional) Remote VTEP Inner MAC address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp2263368881

---

# Command: show nve core-links

## Syntax
```
show nve core-links [ __readonly__ [ TABLE_core_link <if-name> [ { <if-state> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| core-links | Core-links |
| __readonly__ | (Optional) |
| TABLE_core_link | (Optional) xml schema for show nve core-links |
| if-name | (Optional) core-link interface name |
| if-state | (Optional) core-link interface oper state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3737581768

---

# Command: show nve ethernet-segment

## Syntax
```
show nve ethernet-segment [ summary ] [ { esi <esi-id> } ] [ __readonly__ [ TABLE_es { <esi> <if-name> <es-state> [ { <po-state>
 <nve-if-name> <nve-state> <host-reach-mode> <active-vlans> <df-vlans> <active-vnis> <cc-failed-vlans> <cc-timer-left> <num-es-mem>
 <local-ordinal> <df-timer-st> <config-status> <df-list> <es-rt-added> <ead-rt-added> <ead-evi-rt-timer-age> } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| ethernet-segment | Ethernet-segment |
| summary | (Optional) Ethernet-segment summary |
| esi | (Optional) ESI Value |
| esi-id | (Optional) ESI ID |
| __readonly__ | (Optional) |
| TABLE_es | (Optional) xml schema for show nve ethernet-segment |
| esi | (Optional) ESI value |
| if-name | (Optional) port-channel interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp5057741940

---

# Command: show nve evi

## Syntax
```
show nve evi [ __readonly__ TABLE_nve_evi [ <evi> <sw-bd> <label-sr> <oper-state> <evi-state> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| evi | Ethernet Virtual Identifier |
| __readonly__ | (Optional) |
| TABLE_nve_evi | (Optional) xml schema for nve evis |
| evi | (Optional) EVI value |
| sw-bd | (Optional) VLAN information |
| label-sr | (Optional) SR Label |
| oper-state | (Optional) EVI up or down |
| evi-state | (Optional) EVI state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp4259035876

---

# Command: show nve interface

## Syntax
```
show nve interface [ <nve-if> [ detail ] ] [ __readonly__ [ TABLE_nve_if { <if-name> <if-state> <encap-type> <vpc-capability>
 <local-rmac> <host-reach-mode> <source-if> { <primary-ip> &#124; <primary-ipv6> } [ <secondary-ip> &#124; <secondary-ipv6> ] [ { <anycast-if>
 } { <anycast-ip> &#124; <anycast-ipv6> } ] [ { <src-if-state> [ <anyc-if-state> ] <adv-vmac> <nve-flags> <nve-if-handle> <src-if-holddown-tm>
 <src-if-holdup-tm> <src-if-holddown-left> <vpc-compat-check> <vip-rmac> [ <vip-rmac-ro> ] <sm-state> [ <es-delay-restore-time>
 <es-delay-restore-time-left> ] [ <multisite-convergence-time> <multisite-convergence-time-left> ] [ <multisite-bgw-if> <multisite-bgw-if-ip>
 <multisite-bgw-if-admin-state> <multisite-bgw-if-oper-state> <multisite-bgw-if-oper-state-down-reason> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| interface | Interface |
| nve-if | (Optional) NVE interface |
| detail | (Optional) Detailed information |
| __readonly__ | (Optional) |
| TABLE_nve_if | (Optional) xml schema for show nve interfaces |
| if-name | (Optional) interface name |
| if-state | (Optional) interface oper state |
| encap-type | (Optional) encap-type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1589551190

---

# Command: show nve mpls

## Syntax
```
show nve mpls [ __readonly__ [ TABLE_nve_mpls { <source-if> { <primary-ip> &#124; <primary-ipv6> } { <secondary-ip> &#124; <secondary-ipv6>
 } <sm-state> [ <down-reason> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| mpls | Segment routing |
| __readonly__ | (Optional) |
| TABLE_nve_mpls | (Optional) xml schema for sr nve parameters |
| source-if | (Optional) source-interface |
| primary-ip | (Optional) primary-ip |
| secondary-ip | (Optional) secondary-ip |
| sm-state | (Optional) sm state |
| down-reason | (Optional) down reason |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2687763987

---

# Command: show nve multisite dci-links

## Syntax
```
show nve multisite dci-links [ __readonly__ [ TABLE_multisite_dci_link <if-name> [ { <if-state> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| multisite | multisite |
| dci-links | dci-links |
| __readonly__ | (Optional) |
| TABLE_multisite_dci_link | (Optional) xml schema for show nve multisite dci-links |
| if-name | (Optional) dci-link interface name |
| if-state | (Optional) dci-link interface oper state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp4064993201

---

# Command: show nve multisite fabric-links

## Syntax
```
show nve multisite fabric-links [ __readonly__ [ TABLE_multisite_fabric_link <if-name> [ { <if-state> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| multisite | multisite |
| fabric-links | fabric-links |
| __readonly__ | (Optional) |
| TABLE_multisite_fabric_link | (Optional) xml schema for show nve multisite fabric-links |
| if-name | (Optional) fabric-link interface name |
| if-state | (Optional) fabric-link interface oper state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp2033580889

---

# Command: show nve peers

## Syntax
```
show nve peers [ [ [ interface <nve-if> &#124; peer-ip { <user-peer-ip> &#124; <user-peer-ipv6> } &#124; control-plane &#124; data-plane ] [ detail
 ] ] &#124; [ control-plane-vni [ vni <vni-id> &#124; peer-ip { <user-peer-ip> &#124; <user-peer-ipv6> } ] ] &#124; [ controller ] ] [ __readonly__
 TABLE_nve_peers [ [ <detail> ] [ <control-plane-vni> ] [ <if-name> ] { <peer-ip> &#124; <peer-ipv6> } [ <peer-state> ] [ <learn-type>
 ] [ <uptime> ] [ <router-mac> ] [ { <first-vni> <create-ts> <config-vnis> <provision-state> <cp-vni> <vni-assignment-mode>
 <dci-fabric-location> [ <stale-timer> ] } ] [ { <vni> <learn-src> <vni-gw-mac> <peer-type> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| peers | Show peers |
| interface | (Optional) Interface |
| nve-if | (Optional) NVE interface |
| detail | (Optional) Detailed information |
| peer-ip | (Optional) Show a specific peer |
| user-peer-ip | (Optional) Remote Peer IP address |
| control-plane | (Optional) Show peers learned via control plane |
| data-plane | (Optional) Show peers learned via data plane |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1807648848

---

# Command: show nve peers interface counters

## Syntax
```
show nve peers { <addr> &#124; <addr-v6> } interface <nve-if> counters [ __readonly__ { <peer-ip> &#124; <peer-ipv6> } <tx_ucastpkts>
 <tx_ucastbytes> <tx_mcastpkts> <tx_mcastbytes> <rx_ucastpkts> <rx_ucastbytes> <rx_mcastpkts> <rx_mcastbytes> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| peers | NVE Peer |
| addr | Remote Peer IP Address |
| counters | Counters |
| interface | Interface |
| nve-if | NVE interface |
| __readonly__ | (Optional) |
| peer-ip | (Optional) |
| tx_ucastpkts | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1107658602

---

# Command: show nve peers mpls

## Syntax
```
show nve peers mpls [ peer-ip { <user-peer-ip> &#124; <user-peer-ipv6> } ] [ detail ] [ __readonly__ TABLE_nve_mpls_peers [ [ <detail>
 ] { <peer-ip> &#124; <peer-ipv6> } [ <peer-state> ] [ <uptime> ] [ <create-ts> ] [ <provision-state> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| peers | Show peers |
| mpls | Segment routing peers |
| detail | (Optional) Detailed information |
| peer-ip | (Optional) Show a specific peer |
| user-peer-ip | (Optional) Remote Peer IP address |
| __readonly__ | (Optional) |
| detail | (Optional) detail |
| TABLE_nve_mpls_peers | (Optional) schema peer |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp8560993220

---

# Command: show nve peers vni interface counters

## Syntax
```
show nve peers { { <addr> &#124; <addr-v6> } &#124; all } vni { <vni-id> &#124; all } interface <nve-if> counters [ __readonly__ TABLE_nve_peer_vni_counters
 { <peer-ip> &#124; <peer-ipv6> } <vni> <tx_ucastpkts> <tx_ucastbytes> <tx_mcastpkts> <tx_mcastbytes> <rx_ucastpkts> <rx_ucastbytes>
 <rx_mcastpkts> <rx_mcastbytes> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| peers | NVE Peer |
| addr | Remote Peer IP Address |
| all | Show counters for all peers/VNIs |
| vni | Virtual Network Identifier |
| vni-id | Virtual Network Identifier |
| counters | Counters |
| interface | Interface |
| nve-if | NVE interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, interface, overlay, S-commands
**Command ID:** wp3164914407

---

# Command: show nve replication-servers

## Syntax
```
show nve replication-servers [ __readonly__ [ TABLE_nve_replication_servers <if-name> [ { <server-ip> <server-state> <server-ready>
 } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| replication-servers | replication-servers |
| __readonly__ | (Optional) |
| TABLE_nve_replication_servers | (Optional) replcation servers schema |
| if-name | (Optional) if-name |
| server-ip | (Optional) Server IP address |
| server-state | (Optional) Server reachability state |
| server-ready | (Optional) Server ready state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1077057403

---

# Command: show nve vni

## Syntax
```
show nve vni [ { { interface <nve-if> &#124; <vni-id> } [ detail ] } &#124; control-plane &#124; data-plane &#124; summary &#124; controller ] [ __readonly__
 [ TABLE_nve_vni [ [ <detail> ] [ <if-name> <vni> <mcast> <vni-state> <mode> <type> <flags> [ { <prvsn-state> <vlan-bd> <svi-state>
 <vpc-compat-check> } ] ] ] [ [ <summary> ] <cp-vni-count> <cp-vni-up> <cp-vni-down> <dp-vni-count> <dp-vni-up> <dp-vni-down>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vni | Virtual Network Identifier |
| vni-id | (Optional) Virtual Network Identifier |
| interface | (Optional) Interface |
| nve-if | (Optional) NVE interface |
| detail | (Optional) Detailed information |
| control-plane | (Optional) show vni learned via BGP |
| data-plane | (Optional) show vni learned via data plane |
| summary | (Optional) show vni summary |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp5673056630

---

# Command: show nve vni counters

## Syntax
```
show nve vni <vni-id> counters [ __readonly__ <vni> <tx_ucastpkts> <tx_ucastbytes> <tx_mcastpkts> <tx_mcastbytes> <rx_ucastpkts>
 <rx_ucastbytes> <rx_mcastpkts> <rx_mcastbytes> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vni | Virtual Network Identifier |
| vni-id | Virtual Network Identifier |
| counters | Counters |
| __readonly__ | (Optional) |
| vni | (Optional) |
| tx_ucastpkts | (Optional) |
| tx_ucastbytes | (Optional) |
| tx_mcastpkts | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp8940560170

---

# Command: show nve vni ingress-replication

## Syntax
```
Display NVE information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vni | Virtual Network Identifier |
| ingress-replication | ingress-replication |
| vni-id | (Optional) Virtual Network Identifier |
| interface | (Optional) Interface |
| nve-if | (Optional) NVE interface |
| __readonly__ | (Optional) |
| TABLE_nve_vni_ingr_repl | (Optional) vni ingress repl schema |
| if-name | (Optional) if-name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1483952551

---

# Command: show nve vni peer-vtep

## Syntax
```
show nve vni peer-vtep [ { interface <nve-if> &#124; <vni-id> } ] [ __readonly__ [ TABLE_nve_vni_peer_vtep <if-name> <vni> [ {
 <vtep-ip> <source> <up-time> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vni | Virtual Network Identifier |
| peer-vtep | Show static peer-vtep configured per vni |
| vni-id | (Optional) Virtual Network Identifier |
| interface | (Optional) Interface |
| nve-if | (Optional) NVE interface |
| __readonly__ | (Optional) |
| TABLE_nve_vni_peer_vtep | (Optional) vni peer vtep schema |
| if-name | (Optional) if-name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp1435751172

---

# Command: show nve vrf

## Syntax
```
show nve vrf [ vrf-name ] [ __readonly__ [ TABLE_nve_vrf <vrf-name> <vni> <if-name> <gateway-mac> [ { <ipv4-tblid> <ipv6-tblid>
 <vni-sw-bd> <flags> } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vrf | VRF name |
| vrf-name | (Optional) vrf name |
| __readonly__ | (Optional) |
| TABLE_nve_vrf | (Optional) vrf schema |
| vrf-name | (Optional) vrf-name |
| vni | (Optional) vni |
| if-name | (Optional) if-name |
| gateway-mac | (Optional) gateway-mac |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp8957254670

---

# Command: show nve vxlan-params

## Syntax
```
show nve vxlan-params [ __readonly__ <vxlan-port> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Display NVE information |
| nve | Configure NVE information |
| vxlan-params | VxLAN Parameters |
| __readonly__ | (Optional) |
| vxlan-port | (Optional) vxlan-params |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp9660627110

---

# Command: show nxapi-server logs

## Syntax
```
show nxapi-server logs
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nxapi-server | Show NX-API Server |
| logs | Show NX-API Server logs |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp3521619614

---

# Command: show nxapi

## Syntax
```
show nxapi [ __readonly__ <nxapi_status> [ configuration_error <c_error> ] [ <http_port> ] [ <https_port> <ssl_issuer> <ssl_enddate>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nxapi | Show nxapi status |
| __readonly__ | (Optional) |
| nxapi_status | (Optional) NX-API enabled status |
| configuration_error | (Optional) config syntax error |
| c_error | (Optional) confg syntax error |
| http_port | (Optional) Configured HTTP port |
| https_port | (Optional) Configured HTTPS port |
| ssl_issuer | (Optional) Issuer information for current certificate |
| ssl_enddate | (Optional) Expiration date of current certificate |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1682408232

---

# Command: show nxapi syntax

## Syntax
```
show nxapi syntax <cli>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| nxapi | Show nxapi status |
| syntax | Display syntax for given command |
| cli | the exact cli to look-up |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01101.html
**Tags:** show-mode, S-commands
**Command ID:** wp1110975285

---

