# Chapter: Q Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010000.html
**Type:** Show Commands  
**Chapter:** Group-10000 Commands  
**Total Commands:** 11

## Command List

- `show qos dcbxp incompatibility interface`
- `show qos dcbxp info`
- `show qos dcbxp interface`
- `show qos shared-policer`
- `show queuing`
- `show queuing burst-detect`
- `show queuing pfc-queue`
- `show queuing pfc-queue interface snmp watchdogIfQueueTable ifIndex`
- `show queuing pfc-queue snmp ifIndex`
- `show queuing tabular`
- `show queuing tah-pfc-queue`

---

## Detailed Command Reference

# Command: show qos dcbxp incompatibility interface

## Syntax
```
show qos dcbxp incompatibility interface <iface-num> [ __readonly__ { [ { TABLE_local_pfc <vl_id_lpfc> [ <lpfc> ] } ] [ {
 TABLE_remote_pfc <vl_id_rpfc> [ <rpfc> ] } ] [ <mtu> ] [ { TABLE_lpg <vl_id_lpg> [ <cos_list_lpg> ] [ <bandwidth_lpg> ] }
 ] [ { TABLE_rpg <vl_id_rpg> [ <cos_list_rpg> ] [ <bandwidth_rpg> ] } ] [ <bw> ] [ <lfcoe> ] [ <rfcoe> ] [ <liscsi> ] [ <riscsi>
 ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| dcbxp | DCBXP |
| incompatibility | incompatibility information |
| interface | incompatibility info for interface |
| iface-num | Interface |
| __readonly__ | (Optional) |
| TABLE_local_pfc | (Optional) loacal pfc table |
| vl_id_lpfc | (Optional) vl ID for local PFC |
| lpfc | (Optional) local pfc |
| TABLE_remote_pfc | (Optional) remote pfc table |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, interface, qos, S-commands
**Command ID:** wp2198682499

---

# Command: show qos dcbxp info

## Syntax
```
show qos dcbxp info [ __readonly__ { TABLE_dcbxp <intf> <pfcr> <pfcc> <pgr> <pgc> <mtur> <mtuc> <fcoer> <fcoec> <iscsir> <iscsic>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| dcbxp | DCBXP |
| info | information |
| __readonly__ | (Optional) |
| TABLE_dcbxp | (Optional) dxcbxp info |
| intf | (Optional) Interface |
| pfcr | (Optional) pfc recvd |
| pfcc | (Optional) pfc compatible |
| pgr | (Optional) pg received |
| pgc | (Optional) pg compatible |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3987501403

---

# Command: show qos dcbxp interface

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| qos | QoS |
| dcbxp | DCBXP |
| interface | Per-interface information |
| iface | (Optional) Interface |
| __readonly__ | (Optional) |
| intf | (Optional) Interface |
| info_absent | (Optional) No information is present for this Interface. |
| local_pfc_cap | (Optional) Number of Local Flows |
| local_pfc_enable_list | (Optional) List of Local Flows Enabled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, interface, qos, S-commands
**Command ID:** wp3600229515

---

# Command: show qos shared-policer

## Syntax
```
show qos shared-policer [ type qos1 ] [ <policer-name> ] [ __readonly__ { [ TABLE_policer <policer-name2> [ <cir-spec> ] [
 <bc-spec> ] [ <be-spec> ] [ <cir-rate-units> ] [ <cir> ] [ <bc-size-units> ] [ <bc> ] [ <pir-rate-units> ] [ <pir> ] [ <be-size-units>
 ] [ <be> ] [ <cnf-col-cmap> ] [ <exc-col-cmap> ] [ TABLE_action <action-key> [ <cnf-act> ] [ <exc-act> ] [ <vio-act> ] [ <set-type>
 ] [ <enum-spec> ] [ <set-val> ] [ <tmap-from> ] [ <tmap-to> ] [ <tmap-name> ] ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| shared-policer | Shared policer |
| type | (Optional) Type of shared policer |
| qos1 | (Optional) type qos |
| policer-name | (Optional) Shared policer name |
| __readonly__ | (Optional) |
| TABLE_policer | (Optional) all police xml sessions |
| policer-name2 | (Optional) Policer Name |
| TABLE_action | (Optional) all police actions xml sessions |
| action-key | (Optional) Count |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3052240514

---

# Command: show queuing

## Syntax
```
show queuing [ interface [ <if_list> ] ] [ summary ] [ module <module> ] [ __readonly__ [ TABLE_interface_mtu <intf_name>
 <mtu_val> ] [ TABLE_queuing_interface <dir> <if_name_str> [ TABLE_qosgrp_cfg <qosgrp> [ <bandwidth> ] [ <priority> ] [ <shape-min>
 ] [ <shape-max> ] [ <shape-units> ] [ <buffer-size> ] [ <pause-threshold> ] [ <resume-threshold> ] [ <q-limit> ] [ <q-limit-type>
 ] ] [ <mc-drop-pkt> ] [ TABLE_qosgrp_egress_stats <eq-qosgrp> [ TABLE_qosgrp_egress_stats_entry <eq-stat-type> <eq-stat-units>
 <eq-uc-stat-value> [ <eq-oobfc-uc-stat-value> ] [ <eq-mc-stat-value> ] ] ] [ TABLE_egress_stats_entry <ep-stat-type> <ep-stat-units>
 <ep-stat-value> ] [ TABLE_ingress_stats_entry <ip-stat-type> <ip-stat-units> <ip-stat-value> ] [ <tx-ppp> <rx-ppp> [ TABLE_pfc_stats
 <cos> [ <pfc-qosgrp> ] [ <pfc-pg> ] <tx-pause-state> <tx-pause-count> <rx-pause-state> <rx-pause-count> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| interface | (Optional) Interface for displaying queuing config |
| if_list | (Optional) List of interfaces |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| summary | (Optional) summary |
| __readonly__ | (Optional) |
| TABLE_interface_mtu | (Optional) mtu values of each interface |
| intf_name | (Optional) interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2169094011

---

# Command: show queuing burst-detect

## Syntax
```
show queuing burst-detect [ interface <if_name> [ queue <queue_num> ] ] [ module <module> ] [ detail ] [ __readonly__ [ TABLE_instance
 [ <if-str> ] [ <queue> ] [ <pipe> ] [ <threshold> ] [ <start-time> ] [ <peak> ] [ <peak-time> ] [ <end-depth> ] [ <end-time>
 ] [ <duration> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| burst-detect | Out of Band micro-burst queue statistics |
| interface | (Optional) Interface |
| if_name | (Optional) interface name |
| queue | (Optional) Queue number for displaying statistics |
| queue_num | (Optional) Queue number |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| detail | (Optional) detailed statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, S-commands
**Command ID:** wp3561393864

---

# Command: show queuing pfc-queue

## Syntax
```
show queuing pfc-queue [ interface <if_list> ] [ module <module> ] [ detail ] [ __readonly__ <glb-wd-status> <glb-wd-force-status>
 <glb-wd-timer> <glb-wd-timer-thresh> <glb-auto-restore> <glb-fixed-restore> <glb-int-intf-multi> [ TABLE_queuing_interface
 <if_name_str> <wd-status> [ <disable-action> ] [ <intf-multi> ] [ <vl-bmp> ] [ <qosgrp_7_state> ] [ <qosgrp_6_state> ] [ <qosgrp_5_state>
 ] [ <qosgrp_4_state> ] [ <qosgrp_3_state> ] [ <qosgrp_2_state> ] [ <qosgrp_1_state> ] [ <qosgrp_0_state> ] [ TABLE_qosgrp_stats
 <eq-qosgrp> <eq-qosgrp-state> <pfc-configured> <pfc-cos> TABLE_qosgrp_stats_entry <q-stat-type> [ <q-shutdown> ] [ <q-restored>
 ] [ <q-pkt-drained> ] [ <q-pkt-dropped> ] [ <q-pkt-drained-n-dropped> ] [ <q-aggr-pkt-dropped> ] [ <q-ing-pkt-dropped> ] [
 <q-ing-aggr-pkt-dropped> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| pfc-queue | PFC Queuing related information |
| interface | (Optional) Interface for displaying queuing config |
| if_list | (Optional) List of interfaces |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| detail | (Optional) Show detailed PFC Queuing WD information |
| __readonly__ | (Optional) |
| glb-wd-status | (Optional) Global watch-dog timer status |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2075340328

---

# Command: show queuing pfc-queue interface snmp watchdogIfQueueTable ifIndex

## Syntax
```
show queuing pfc-queue interface snmp watchdogIfQueueTable ifIndex <ifindex> [ __readonly__ [ TABLE_watchdogIfQueueTable <ifindex>
 [ TABLE_qosgrp_stats <eq-qosgrp> <state> <shutdowns> <restores> <dropPkts> <totaldropPkts> <ingDropPkts> <totalIngDropPkts>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| pfc-queue | PFC Queuing related information |
| interface | Interface for displaying queuing config |
| snmp | commands for snmp |
| watchdogIfQueueTable | Table |
| ifIndex | port ifIndex |
| ifindex | interfaces ifIndex |
| __readonly__ | (Optional) |
| TABLE_watchdogIfQueueTable | (Optional) PFC Queuing information of an interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, interface, management, S-commands
**Command ID:** wp4266941530

---

# Command: show queuing pfc-queue snmp ifIndex

## Syntax
```
show queuing pfc-queue snmp ifIndex <ifidx> [ __readonly__ TABLE-cpfcWatchdogIfQueueInfoTable <ifidx_out> <queueno_out> <q-state>
 <q-shutdown> <q-restored> <q-pkt-dropped> <q-aggr-pkt-dropped> <q-ing-pkt-dropped> <q-ing-aggr-pkt-dropped> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| queuing | Queuing related information |
| pfc-queue | PFC Queuing related information |
| snmp | Snmp information |
| ifIndex | Interface index |
| ifidx | Index |
| __readonly__ | (Optional) Read Only |
| TABLE-cpfcWatchdogIfQueueInfoTable | (Optional) SNMP table |
| ifidx_out | (Optional) Interface index out |
| queueno_out | (Optional) Queue number out |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, management, S-commands
**Command ID:** wp1243966365

---

# Command: show queuing tabular

## Syntax
```
show queuing tabular [ non-zero [ drop-only ] ] [ interface <if_list> ] [ module <module> ] [ __readonly__ [ TABLE_queuing_interface
 <if_name_str> <qos_group_name_0> <qos_group_name_1> <qos_group_name_2> <qos_group_name_3> <qos_group_name_4> <qos_group_name_5>
 <qos_group_name_6> <qos_group_name_7> <qos_group_name_cpu> <qos_group_name_span> <tx_uc_pkt_qos_0> <tx_uc_byte_qos_0> <tx_uc_drop_pkt_qos_0>
 <tx_uc_drop_byte_qos_0> <tx_uc_ecn_pkt_qos_0> <tx_uc_ecn_byte_qos_0> <tx_oobfc_uc_pkt_qos_0> <tx_oobfc_uc_byte_qos_0> <tx_oobfc_uc_drop_pkt_qos_0>
 <tx_oobfc_uc_drop_byte_qos_0> <tx_fld_pkt_qos_0> <tx_fld_byte_qos_0> <tx_fld_drop_pkt_qos_0> <tx_fld_drop_byte_qos_0> <tx_mc_pkt_qos_0>
 <tx_mc_byte_qos_0> <tx_mc_drop_pkt_qos_0> <tx_mc_drop_byte_qos_0> <pfc_rx_qos_0> <pfc_tx_qos_0> <qos_grp_1> <qos_grp_2> <qos_grp_3>
 <qos_grp_4> <qos_grp_5> <qos_grp_6> <qos_grp_7> <qos_grp_cpu> <qos_grp_span> <ing_drop_pkt> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| tabular | QoS stats in tabular form |
| non-zero | (Optional) Interface for non-zero stats |
| drop-only | (Optional) Interface for non-zero drop-only stats |
| interface | (Optional) Interface for displaying queuing config |
| if_list | (Optional) List of interfaces |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2334145053

---

# Command: show queuing tah-pfc-queue

## Syntax
```
show queuing tah-pfc-queue [ interface <if_list> ] [ module <module> ] [ detail ] [ __readonly__ [ TABLE_queuing_interface
 <if_name_str> [ TABLE_qosgrp_stats <eq-qosgrp> [ TABLE_qosgrp_stats_entry <q-stat-type> <q-shutdown> <q-restored> <q-pkt-drained>
 <q-pkt-dropped> <q-total-pkt-dropped> <q-aggr-pkt-dropped> <q-ingr-pkt-dropped> <q-aggr-ingr-pkt-dropped> ] ] [ TABLE_qosgrp_stats_summary
 <qosgrp-summary> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | commands to display |
| queuing | Queuing related information |
| tah-pfc-queue | PFC Queuing related information |
| interface | (Optional) Interface for displaying queuing config |
| if_list | (Optional) List of interfaces |
| module | (Optional) Slot/module |
| module | (Optional) Slot/module number |
| detail | (Optional) Show detailed PFC Queuing WD information |
| __readonly__ | (Optional) |
| if_name_str | (Optional) interface name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010000.html
**Tags:** show-mode, S-commands
**Command ID:** wp2218504450

---

