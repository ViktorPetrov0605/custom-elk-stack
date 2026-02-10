# Chapter: D Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_0100.html
**Type:** Show Commands  
**Chapter:** Group-100 Commands  
**Total Commands:** 21

## Command List

- `show dampening interface`
- `show diagnostic bootup level`
- `show diagnostic content module`
- `show diagnostic description module test all`
- `show diagnostic events`
- `show diagnostic ondemand setting`
- `show diagnostic result module`
- `show diagnostic result module all`
- `show diagnostic simulation module`
- `show diagnostic status module`
- `show diff rollback-patch`
- `show dot1q-tunnel`
- `show dot1q-tunnel interface`
- `show dot1x`
- `show dot1x all`
- `show dot1x all details`
- `show dot1x all statistics`
- `show dot1x all summary`
- `show dot1x interface`
- `show dot1x interface client statistics`
- `show dot1x interface client statistics address`

---

## Detailed Command Reference

# Command: show dampening interface

## Syntax
```
show dampening interface [ __readonly__ { <DampenedInterfaceCount> <SuppressedInterfaceCount> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| dampening | Display dampening information |
| interface | Display interface dampening general information |
| __readonly__ | (Optional) |
| DampenedInterfaceCount | (Optional) Count of interfaces configured with dampening |
| SuppressedInterfaceCount | (Optional) Count of interfaces in suppressed state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1256394987

---

# Command: show diagnostic bootup level

## Syntax
```
show diagnostic bootup level [ __readonly__ <bootup_level> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| bootup | Show diagnostic bootup information |
| level | Show diagnostic bootup level information |
| __readonly__ | (Optional) |
| bootup_level | (Optional) Bootup level |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp1632717645

---

# Command: show diagnostic content module

## Syntax
```
show diagnostic content module { all &#124; <module> } [ __readonly__ <attr_descr> { TABLE_Module <module_id> <module_type> { TABLE_test
 <test_id> <testname> <test_attr> <test_interval> } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| content | Show diagnostic test content |
| module | Module Keyword |
| all | Select all module ID |
| module | Module number |
| __readonly__ | (Optional) |
| attr_descr | (Optional) Attribute description |
| TABLE_Module | (Optional) All modules table |
| module_id | (Optional) Module Number |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1137478110

---

# Command: show diagnostic description module test all

## Syntax
```
show diagnostic description module <module> test { all &#124; <name> &#124; <test-id> } [ __readonly__ { TABLE_desc <testname> <testdesc>
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| description | Show diagnostic test desc |
| module | Module keyword |
| module | Module Number |
| test | Diagnostic test selection |
| all | Select all test ID |
| name | Test name |
| __readonly__ | (Optional) |
| TABLE_desc | (Optional) Table of test description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp4948378610

---

# Command: show diagnostic events

## Syntax
```
show diagnostic events [ error &#124; info ] [ __readonly__ { TABLE_events <event_text> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| events | Diagnostic events |
| error | (Optional) Error event-type |
| info | (Optional) Information event-type |
| __readonly__ | (Optional) |
| TABLE_events | (Optional) list of events logged |
| event_text | (Optional) Text of one event |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1938414419

---

# Command: show diagnostic ondemand setting

## Syntax
```
show diagnostic ondemand setting [ __readonly__ <test_iteration_count> <action_on_failure> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| ondemand | Show diagnostic on demand information |
| setting | Show diagnostic on demand settings |
| __readonly__ | (Optional) |
| test_iteration_count | (Optional) Iteration Count |
| action_on_failure | (Optional) Action on failure |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1419578549

---

# Command: show diagnostic result module

## Syntax
```
show diagnostic result module <module> [ test { <name> &#124; <test-id> } ] { [ detail ] &#124; [ statistics ] } [ __readonly__ <module_id>
 <curr_diag_level> <module_name> [ <bootup_diag_level> ] [ { TABLE_TestStat <stat_testid> <stat_testname> { TABLE_StatDetail
 <port_no> <packet_tx> <packet_rx> <packet_loss> } } ] [ { TABLE_Test <test_id> <testname> [ <testresult> ] [ { <passed_ports>
 <failed_ports> <incomplete_ports> <untested_ports> <aborted_ports> <err_disabled_ports> } ] [ { <err_code> <total_run_count>
 <last_execution_time> <first_failure_time> <last_failure_time> <last_pass_time> <total_fail_count> <consequtive_fail_count>
 <last_fail_reason> <next_execution_time> } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| result | Show diagnostic test result |
| module | Module keyword |
| module | Module number |
| test | (Optional) Diagnostic test selection |
| test-id | (Optional) |
| name | (Optional) Test name |
| detail | (Optional) Detailed result |
| statistics | (Optional) Result statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1265675436

---

# Command: show diagnostic result module all

## Syntax
```
show diagnostic result module all [ detail ] [ __readonly__ { TABLE_Module <module_id> <curr_diag_level> <module_name> [ <bootup_diag_level>
 ] { TABLE_Test <test_id> <testname> [ <testresult> ] [ { <passed_ports> <failed_ports> <incomplete_ports> <untested_ports>
 <aborted_ports> <err_disabled_ports> } ] [ { <err_code> <total_run_count> <last_execution_time> <first_failure_time> <last_failure_time>
 <last_pass_time> <total_fail_count> <consequtive_fail_count> <last_fail_reason> <next_execution_time> } ] } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| result | Show diagnostic test result |
| module | Module keyword |
| all | Select all test ID |
| detail | (Optional) Detailed result |
| __readonly__ | (Optional) |
| TABLE_Module | (Optional) Table of modules |
| module_id | (Optional) Module ID |
| curr_diag_level | (Optional) Current diag level |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp4179835760

---

# Command: show diagnostic simulation module

## Syntax
```
show diagnostic simulation module <module> [ __readonly__ <module_id> <module_name> [ { TABLE_detail <serial_no> <testid>
 [ <portid> ] <mode> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| simulation | Simulating Diagnostic result |
| module | Module keyword |
| module | Module Number |
| __readonly__ | (Optional) |
| module_id | (Optional) Module ID |
| module_name | (Optional) Module Name |
| TABLE_detail | (Optional) Table of simulation details |
| serial_no | (Optional) serial no |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3545765701

---

# Command: show diagnostic status module

## Syntax
```
show diagnostic status module <module> [ __readonly__ <test_runby_mapping> <module_id> <module_name> { TABLE_current <cur_test_name>
 <cur_run_by> } { TABLE_enqued <enq_test_name> <enq_run_by> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diagnostic | Diagnostic commands |
| status | Show test status(running/enqueued) |
| module | Module keyword |
| module | Module number |
| __readonly__ | (Optional) |
| test_runby_mapping | (Optional) Test type expansion |
| module_id | (Optional) Module Id |
| module_name | (Optional) Module name |
| TABLE_current | (Optional) Table of currently running test |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3036244147

---

# Command: show diff rollback-patch

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| diff | Show diff between configuration files or checkpoints |
| rollback-patch | Show rollback patch between configuration files or checkpoints |
| src-checkpoint | Use checkpoint as source configuration |
| chkpoint_name | Checkpoint name |
| src-running-cfg | Use running configuration as source |
| src-startup-cfg | Use startup configuration as source |
| src-file | Src Checkpoint file |
| srcfile_uri | Src Checkpoint file path |
| dst-checkpoint | Use checkpoint as destination configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2113341273

---

# Command: show dot1q-tunnel

## Syntax
```
show dot1q-tunnel [ __readonly__ TABLE_interface <interface> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| dot1q-tunnel | Show if port mode is dot1q-tunnel |
| __readonly__ | (Optional) Read Only |
| interface | (Optional) Interface index |
| TABLE_interface | (Optional) show interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3442138390

---

# Command: show dot1q-tunnel interface

## Syntax
```
show dot1q-tunnel interface <ifid_eth_dot1q_tunnel> [ __readonly__ TABLE_interface <interface> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| dot1q-tunnel | Show if port mode is dot1q-tunnel |
| interface | Show interface status and information |
| ifid_eth_dot1q_tunnel | Enter interface type and number in module/slot format |
| __readonly__ | (Optional) Read Only |
| interface | (Optional) Interface index |
| TABLE_interface | (Optional) show interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3807104554

---

# Command: show dot1x

## Syntax
```
show dot1x [ __readonly__ <sys_auth_ctrl> <proto_ver> <mac_move> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| __readonly__ | (Optional) |
| sys_auth_ctrl | (Optional) show system auth control |
| proto_ver | (Optional) show protocol version |
| mac_move | (Optional) show mac move |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1972396002

---

# Command: show dot1x all

## Syntax
```
show dot1x all [ __readonly__ <sys_auth_ctrl> <proto_ver> <mac_move> TABLE_all <if_index> TABLE_allpae <pae_type> [ <port_control>
 ] [ <host_mode> ] [ <quiet_period> ] [ <inactivity_period> ] [ <tx_period> ] [ <max_req> ] [ <reauth> ] [ <rate_limit_period>
 ] [ <supp_timeout> ] [ <server_timeout> ] [ <reauth_server> ] [ <reauth_period> ] [ <reauth_max> ] [ <mac_auth_bypass> ] [
 <start_period> ] [ <auth_period> ] [ <held_period> ] [ <max_start> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| all | Show information for all interfaces |
| __readonly__ | (Optional) |
| TABLE_all | (Optional) |
| TABLE_allpae | (Optional) |
| if_index | (Optional) Interface Index |
| sys_auth_ctrl | (Optional) Show System Auth Control |
| proto_ver | (Optional) Show Protocol Version |
| mac_move | (Optional) Show Mac Move |
| pae_type | (Optional) Show PAE Type |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2329217342

---

# Command: show dot1x all details

## Syntax
```
show dot1x all details [ __readonly__ <sys_auth_ctrl> <proto_ver> <mac_move> TABLE_alldetail <if_index> TABLE_allpaedetail
 <pae_type> [ <port_control> ] [ <host_mode> ] [ <quiet_period> ] [ <inactivity_period> ] [ <tx_period> ] [ <max_req> ] [ <reauth>
 ] [ <rate_limit_period> ] [ <supp_timeout> ] [ <server_timeout> ] [ <reauth_server> ] [ <reauth_period> ] [ <reauth_max> ]
 [ <mac_auth_bypass> ] [ <no_of_clients> ] [ <port_status_no_clients> ] [ { TABLE_if_auth_clients [ <supp_mac_addr> ] [ <auth_domain>
 ] [ <auth_sm_state> ] [ <auth_bend_sm_state> ] [ <port_status> ] [ <authentication_method> ] [ <authenticated_by> ] [ <reauth_period_client>
 ] [ <reauth_action> ] [ <time_to_next_reauth> ] [ <auth_vlan> ] } ] [ <start_period> ] [ <auth_period> ] [ <held_period> ]
 [ <max_start> ] [ <no_of_supp_clients> ] [ <auth_mac_addr> ] [ <supp_sm_state> ] [ <supp_bend_sm_state> ] [ <supp_port_status>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| all | Show information for all interfaces |
| details | 802.1x details |
| __readonly__ | (Optional) |
| TABLE_alldetail | (Optional) |
| TABLE_allpaedetail | (Optional) |
| TABLE_if_auth_clients | (Optional) |
| if_index | (Optional) Interface Index |
| sys_auth_ctrl | (Optional) Show System Auth Control |
| proto_ver | (Optional) Show Protocol Version |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1438229800

---

# Command: show dot1x all statistics

## Syntax
```
show dot1x all statistics [ __readonly__ TABLE_allstat <if_index> TABLE_allpaestat <pae_type> [ <rxstart> ] [ <rxlogoff> ]
 [ <rxresp> ] [ <rxrespid> ] [ <rxinvalid> ] [ <rxlenerr> ] [ <rxtotal> ] [ <txreq> ] [ <txreqid> ] [ <txtotal> ] [ <rxversion>
 ] [ <lastrxsourcemac> ] [ <rxreq> ] [ <rxsuppinvalid> ] [ <rxsupplenerr> ] [ <rxsupptotal> ] [ <txstart> ] [ <txlogoff> ]
 [ <txresp> ] [ <txsupptotal> ] [ <rxsuppversion> ] [ <lastrxsrcmac> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| all | Show information for all interfaces |
| statistics | 802.1x statistics |
| __readonly__ | (Optional) |
| TABLE_allstat | (Optional) |
| TABLE_allpaestat | (Optional) |
| if_index | (Optional) Interface Index |
| pae_type | (Optional) Show PAE Type |
| rxstart | (Optional) Show Received EAPOL-Start |
| rxlogoff | (Optional) Show Received EAPOL-Logoff |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1669469779

---

# Command: show dot1x all summary

## Syntax
```
show dot1x all summary [ __readonly__ TABLE_allsummary <if_index> <pae_type> [ <port_status_no_clients> ] [ { TABLE_if_auth_clients
 [ <auth_mac_addr> ] [ <port_status> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| all | Show information for all interfaces |
| summary | 802.1x summary |
| __readonly__ | (Optional) |
| TABLE_allsummary | (Optional) |
| TABLE_if_auth_clients | (Optional) |
| if_index | (Optional) Interface Index |
| pae_type | (Optional) Show PAE Type |
| auth_mac_addr | (Optional) Show Authenticator MAC Address |
| port_status_no_clients | (Optional) Show Port Status if there are no clients |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2469311967

---

# Command: show dot1x interface

## Syntax
```
{ show dot1x interface <if> [ __readonly__ <if_index> <pae_type> [ <port_control> ] [ <host_mode> ] [ <quiet_period> ] [ <inactivity_period>
 ] [ <tx_period> ] [ <max_req> ] [ <reauth> ] [ <rate_limit_period> ] [ <supp_timeout> ] [ <server_timeout> ] [ <reauth_server>
 ] [ <reauth_period> ] [ <reauth_max> ] [ <mac_auth_bypass> ] [ <start_period> ] [ <auth_period> ] [ <held_period> ] [ <max_start>
 ] ] } &#124; { show dot1x interface <if> details [ __readonly__ <if_index_detail> <pae_type_detail> [ <port_control_detail> ] [
 <host_mode_detail> ] [ <quiet_period_detail> ] [ <inactivity_period_detail> ] [ <tx_period_detail> ] [ <max_req_detail> ]
 [ <reauth_detail> ] [ <rate_limit_period_detail> ] [ <supp_timeout_detail> ] [ <server_timeout_detail> ] [ <reauth_server_detail>
 ] [ <reauth_period_detail> ] [ <reauth_max_detail> ] [ <mac_auth_bypass_detail> ] [ <no_of_clients> ] [ <port_status_no_clients_detail>
 ] [ { TABLE_if_auth_clients_detail [ <supp_mac_addr_detail> ] [ <auth_domain> ] [ <auth_sm_state> ] [ <auth_bend_sm_state>
 ] [ <port_status> ] [ <authentication_method> ] [ <authenticated_by> ] [ <reauth_period_client> ] [ <reauth_action> ] [ <time_to_next_reauth>
 ] [ <auth_vlan> ] } ] [ <start_period_detail> ] [ <auth_period_detail> ] [ <held_period_detail> ] [ <max_start_detail> ] [
 <no_of_supp_clients> ] [ <auth_mac_addr_detail> ] [ <supp_sm_state> ] [ <supp_bend_sm_state> ] [ <supp_port_status> ] ] }
 &#124; { show dot1x interface <if> statistics [ __readonly__ <if_index_stat> <pae_type_stat> [ <rxstart> ] [ <rxlogoff> ] [ <rxresp>
 ] [ <rxrespid> ] [ <rxinvalid> ] [ <rxlenerr> ] [ <rxtotal> ] [ <txreq> ] [ <txreqid> ] [ <txtotal> ] [ <rxversion> ] [ <lastrxsourcemac>
 ] [ <rxreq> ] [ <rxsuppinvalid> ] [ <rxsupplenerr> ] [ <rxsupptotal> ] [ <txstart> ] [ <txlogoff> ] [ <txresp> ] [ <txsupptotal>
 ] [ <rxsuppversion> ] [ <lastrxsrcmac> ] ] } &#124; { show dot1x interface <if> summary [ __readonly__ <if_index_summary> <pae_type_summary>
 [ <port_status_no_clients_summary> ] [ { TABLE_if_auth_clients_summary [ <auth_mac_addr> ] [ <port_status_summary> ] } ] [
 <supp_mac_addr> ] [ <supp_port_status_summary> ] ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| details | 802.1x details |
| statistics | 802.1x statistics |
| summary | 802.1x summary |
| TABLE_if_auth_clients_detail | (Optional) |
| TABLE_if_auth_clients_summary | (Optional) |
| __readonly__ | (Optional) |
| if_index | (Optional) Interface Index |
| if_index_detail | (Optional) Interface Index |
| if_index_stat | (Optional) Interface Index |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1313116622

---

# Command: show dot1x interface client statistics

## Syntax
```
show dot1x interface <if> client statistics [ __readonly__ <if_index_stat> <pae_type_stat> [ { TABLE_mac_address [ <macaddr>
 ] [ <rxstart> ] [ <rxlogoff> ] [ <rxresp> ] [ <rxrespid> ] [ <rxinvalid> ] [ <rxlenerr> ] [ <rxtotal> ] [ <txreq> ] [ <txreqid>
 ] [ <txtotal> ] [ <rxversion> ] [ <lastrxsourcemac> ] } ] [ <spurious_rxstart> ] [ <spurious_rxlogoff> ] [ <spurious_rxresp>
 ] [ <spurious_rxrespid> ] [ <spurious_rxinvalid> ] [ <spurious_rxlenerr> ] [ <spurious_rxtotal> ] [ <spurious_txreq> ] [ <spurious_txreqid>
 ] [ <spurious_txtotal> ] [ <spurious_rxversion> ] [ <spurious_lastrxsourcemac> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| client | 802.1x client |
| statistics | 802.1x statistics |
| __readonly__ | (Optional) |
| TABLE_mac_address | (Optional) |
| if_index_stat | (Optional) Interface Index |
| pae_type_stat | (Optional) Show PAE Type |
| macaddr | (Optional) mac-address of the client |
| rxstart | (Optional) Show Received EAPOL-Start |
| rxlogoff | (Optional) Show Received EAPOL-Logoff |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp8421481050

---

# Command: show dot1x interface client statistics address

## Syntax
```
show dot1x interface <if> client statistics address <mac-address> [ __readonly__ <if_index_stat> <pae_type_stat> [ <rxstart>
 ] [ <rxlogoff> ] [ <rxresp> ] [ <rxrespid> ] [ <rxinvalid> ] [ <rxlenerr> ] [ <rxtotal> ] [ <txreq> ] [ <txreqid> ] [ <txtotal>
 ] [ <rxversion> ] [ <lastrxsourcemac> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| dot1x | dot1x configuration commands |
| client | 802.1x client |
| statistics | 802.1x statistics |
| address | 802.1x client address |
| mac-address | mac address EE:EE:EE:EE:EE:EE |
| __readonly__ | (Optional) |
| if_index_stat | (Optional) Interface Index |
| pae_type_stat | (Optional) Show PAE Type |
| rxstart | (Optional) Show Received EAPOL-Start |
| rxlogoff | (Optional) Show Received EAPOL-Logoff |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_0100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2308628962

---

