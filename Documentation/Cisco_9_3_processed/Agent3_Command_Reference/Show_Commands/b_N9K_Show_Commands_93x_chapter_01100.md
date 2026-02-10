# Chapter: M Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01100.html
**Type:** Show Commands  
**Chapter:** Group-1100 Commands  
**Total Commands:** 57

## Command List

- `show mac-list`
- `show mac address-table`
- `show mac address-table`
- `show mac address-table aging-time`
- `show mac address-table count`
- `show mac address-table count es`
- `show mac address-table learning-mode`
- `show mac address-table limit`
- `show mac address-table limit user-defined`
- `show mac address-table loop-detect`
- `show mac address-table multicast`
- `show mac address-table notification mac-move`
- `show mac scalar`
- `show macsec mka`
- `show macsec mka session`
- `show macsec mka statistics`
- `show macsec policy`
- `show macsec secy statistics`
- `show maintenance maint-delay`
- `show maintenance on-reload reset-reasons`
- `show maintenance profile`
- `show maintenance snapshot-delay`
- `show maintenance timeout`
- `show module`
- `show module bandwidth-fairness`
- `show module uptime`
- `show monitor`
- `show monitor session`
- `show mpls extended-ecmp`
- `show mpls forwarding statistics`
- `show mpls interfaces`
- `show mpls interfaces detail`
- `show mpls interfaces statistics`
- `show mpls ip bindings`
- `show mpls ip bindings summary`
- `show mpls ip ttl`
- `show mpls label range`
- `show mpls load-sharing`
- `show mpls oam echo statistics`
- `show mpls static binding`
- `show mpls static binding`
- `show mpls static binding vrf per-vrf`
- `show mpls static trace`
- `show mpls strip labels`
- `show mpls switching`
- `show mpls switching clients`
- `show mvpn bgp mdt`
- `show mvpn mdt encap`
- `show mvpn mdt route`
- `show mvr`
- `show mvr groups`
- `show mvr interface`
- `show mvr members`
- `show mvr members count`
- `show mvr members vlan`
- `show mvr receiver-ports`
- `show mvr source-ports`

---

## Detailed Command Reference

# Command: show mac-list

## Syntax
```
show mac-list { [ { <maclist-name> &#124; <maclist-cfg-name> } [ { seq <seq_no> &#124; { <mac_addr> [ <mac_mask> ] } } ] ] } [ __readonly__
 TABLE_mac_list <name> <seq> <action> <rule> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mac-list | Show mac-lists |
| maclist-name | (Optional) Name of mac-list |
| maclist-cfg-name | (Optional) Known mac-list name |
| seq | (Optional) Sequence number |
| seq_no | (Optional) Sequence number |
| mac_addr | (Optional) MAC address |
| mac_mask | (Optional) MAC mask |
| __readonly__ | (Optional) |
| TABLE_mac_list | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1837661970

---

# Command: show mac address-table

## Syntax
```
MAC configuration commands
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| module | Module Number |
| count | (Optional) Number of entries |
| static | (Optional) Display Static Entries |
| dynamic | (Optional) Display Dynamic Entries |
| secure | (Optional) Display Secure Entries |
| address | (Optional) address |
| address1 | (Optional) address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1081566755

---

# Command: show mac address-table

## Syntax
```
MAC configuration commands
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| static | (Optional) Display Static Entries |
| dynamic | (Optional) Display Dynamic Entries |
| secure | (Optional) Display Secure Entries |
| local | (Optional) Display MAC Entries Learned Locally and Not on the Overlay/VXLAN |
| address | (Optional) address |
| address1 | (Optional) address |
| address2 | (Optional) address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp4096640433

---

# Command: show mac address-table aging-time

## Syntax
```
show mac address-table aging-time [ __readonly__ <age_str> <age> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| aging-time | Configured/default age |
| __readonly__ | (Optional) |
| age_str | (Optional) Age info |
| age | (Optional) Age time |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2510468058

---

# Command: show mac address-table count

## Syntax
```
MAC configuration commands
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| count | Number of MAC entries |
| static | (Optional) Display Static Entries |
| dynamic | (Optional) Display Dynamic Entries |
| secure | (Optional) Display Secure Entries |
| local | (Optional) Display MAC Entries Learned Locally and Not on the Overlay/VXLAN |
| vlan | (Optional) VLAN |
| id | (Optional) VLAN ID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3083391702

---

# Command: show mac address-table count es

## Syntax
```
show mac address-table count es { <es-id> &#124; <es-id2> &#124; all } [ __readonly__ { [ <es-id> ] [ <count> ] [ TABLE_macaddtblcount
 <es-idx> <es-count> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| count | Number of MAC entries |
| es | EVPN Remote ESID |
| es-id | EE:EE:EE:EE:EE:EE:EE:EE:EE:EE ESID |
| es-id2 | EEEE.EEEE.EEEE.EEEE.EEEE ESID |
| all | all ESIs |
| __readonly__ | (Optional) |
| es-id | (Optional) Specfic ESID |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1797610184

---

# Command: show mac address-table learning-mode

## Syntax
```
show mac address-table learning-mode [ vlan <id> ] [ __readonly__ <learning_mode_str> <vlan_id> <mode_str> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| learning-mode | Learning Mode |
| vlan | (Optional) VLAN |
| id | (Optional) VLAN ID |
| __readonly__ | (Optional) |
| learning_mode_str | (Optional) Learning Mode |
| vlan_id | (Optional) VLAN ID |
| mode_str | (Optional) Mode |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2791422569

---

# Command: show mac address-table limit

## Syntax
```
show mac address-table limit { all &#124; system &#124; vlan &#124; interface } [ __readonly__ <limit_str> <limit> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| limit | Configured/default mac limit |
| __readonly__ | (Optional) |
| limit_str | (Optional) Limit info |
| limit | (Optional) Mac limit |
| all | Display Mac Limit All |
| system | System-wide |
| vlan | VLAN |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3087411343

---

# Command: show mac address-table limit user-defined

## Syntax
```
show mac address-table limit user-defined [ __readonly__ <user_cnt> <fhrp_cnt> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| limit | mac limit |
| user-defined | limit the number of unique mac addresses used on any type of L3 interface |
| __readonly__ | (Optional) |
| user_cnt | (Optional) user defined mac limit |
| fhrp_cnt | (Optional) fhrp limit |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp6624603370

---

# Command: show mac address-table loop-detect

## Syntax
```
show mac address-table loop-detect [ __readonly__ <port_loop_detect> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| loop-detect | Display Action for Mac Loop Detection |
| __readonly__ | (Optional) |
| port_loop_detect | (Optional) Display Port Down Action Mac Loop Detect is enabled or disabled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3219709027

---

# Command: show mac address-table multicast

## Syntax
```
show mac address-table multicast [ vlan <vlan> &#124; bridge-domain <bdid> ] [ __readonly__ [ TABLE_mac [ <vlan-id> ] [ <mac-addr>
 ] [ <type> ] [ <age> ] [ TABLE_oif [ <oifs> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| multicast | mcast mac OIF Static Entry |
| vlan | (Optional) VLAN |
| vlan | (Optional) VLAN |
| bridge-domain | (Optional) BD |
| bdid | (Optional) BD |
| __readonly__ | (Optional) |
| TABLE_mac | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp6790203530

---

# Command: show mac address-table notification mac-move

## Syntax
```
show mac address-table notification mac-move [ __readonly__ TABLE_mac_notif <disp_mm_status> <disp_mm_triggers> <disp_macs_added>
 <disp_macs_moved> <disp_macs_removed> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | show |
| mac | MAC configuration commands |
| address-table | MAC Address Table |
| notification | Display Notification Information |
| mac-move | Mac Move Notification |
| __readonly__ | (Optional) Read Only |
| TABLE_mac_notif | (Optional) Mac address notification table |
| disp_mm_status | (Optional) Mac Move Status |
| disp_mm_triggers | (Optional) # of triggers |
| disp_macs_added | (Optional) Number of MACs added since system bring up |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1250928480

---

# Command: show mac scalar

## Syntax
```
show mac scalar [ __readonly__ <cmnMACMoveAddress> <cmnMACMoveVlanNumber> <cmnMACMoveFromPortId> <cmnMACMoveToPortId> <cmnMACMoveTime>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mac | MAC configuration commands |
| scalar | cmn mib scalars |
| __readonly__ | (Optional) |
| cmnMACMoveAddress | (Optional) mac move address |
| cmnMACMoveVlanNumber | (Optional) mac vlan number |
| cmnMACMoveFromPortId | (Optional) from port id |
| cmnMACMoveToPortId | (Optional) to port id |
| cmnMACMoveTime | (Optional) move time |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2809657174

---

# Command: show macsec mka

## Syntax
```
show macsec mka [ summary ] [ __readonly__ [ <macsec_status> ] [ TABLE_mka_summary <ifname> <status> <cipher> <keyserver>
 <policy> <keychain> <fallback_keychain> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| macsec | Show MACSEC information |
| mka | Show MKA information |
| summary | (Optional) Show MKA summary information |
| __readonly__ | (Optional) |
| macsec_status | (Optional) Macsec status |
| TABLE_mka_summary | (Optional) |
| ifname | (Optional) Interface |
| status | (Optional) MACSEC Session status |
| cipher | (Optional) Operational MACSEC Cipher-suite |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp7252616650

---

# Command: show macsec mka session

## Syntax
```
show macsec mka session [ interface <ifname> ] [ details ] [ __readonly__ [ <macsec_status> ] [ TABLE_mka_session <ifname>
 <sci> <peers> <status> <keyserver><ca_auth_mode> ] [ <sessions> <active_sessions> <pending_sessions> ] [ TABLE_mka_session_details
 <ifname> <status> <sci> <ssci> <port_id> <ckn> <ca_auth_mode> <mi> <mn> <policy> <ks_prio> <keyserver> <include_icv_indicator>
 <cipher> <cipher_operational> <window> <conf_offset> <conf_offset_operational> <sak_status> <sak_an> <sak_ki> <sak_kn> <last_sak_rekey_time>
 <peer_count> <mac_addr> <ether_type> [ TABLE_mka_peer_status <peer_mi> <rxsci> <icv_status> <last_rx_time> ] [ TABLE_mka_fallback
 <fallback_ckn> <fallback_mi> <fallback_mn> [ TABLE_mka_fallback_peer <fallback_peer_mi> <fallback_rxsci> <fallback_icv_status>
 <fallback_last_rx_time> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| macsec | Show MACSEC information |
| mka | Show MKA information |
| session | Show MKA session information |
| interface | (Optional) Specify interface |
| ifname | (Optional) Interface list |
| details | (Optional) Show MKA detailed information |
| __readonly__ | (Optional) |
| macsec_status | (Optional) macsec status |
| TABLE_mka_session | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3502819349

---

# Command: show macsec mka statistics

## Syntax
```
show macsec mka statistics [ interface <ifname> ] [ __readonly__ [ <macsec_status> ] [ TABLE_mka_intf_stats [ [ <ifname2>
 ] [ TABLE_ca_stats [ [ <ca_stat_ckn> ] [ <ca_stat_pairwise_cak_rekey> ] [ <sa_stat_sak_generated> ] [ <sa_stat_sak_rekey>
 ] [ <sa_stat_sak_received> ] [ <sa_stat_sak_response_rx> ] [ <mkpdu_stat_mkpdu_tx> ] [ <mkpdu_stat_mkpdu_tx_distsak> ] [ <mkpdu_stat_mkpdu_rx>
 ] [ <mkpdu_stat_mkpdu_rx_distsak> ] ] ] [ TABLE_idb_stats [ [ <ca_stat_pairwise_cak_rekey> ] [ <sa_stat_sak_generated> ] [
 <sa_stat_sak_rekey> ] [ <sa_stat_sak_received> ] [ <sa_stat_sak_response_rx> ] [ <mkpdu_stat_mkpdu_tx> ] [ <mkpdu_stat_mkpdu_tx_distsak>
 ] [ <mkpdu_stat_mkpdu_rx> ] [ <mkpdu_stat_mkpdu_rx_distsak> ] [ <idb_stat_mkpdu_tx_success> ] [ <idb_stat_mkpdu_tx_fail> ]
 [ <idb_stat_mkpdu_tx_pkt_build_fail> ] [ <idb_stat_mkpdu_no_tx_on_intf_down> ] [ <idb_stat_mkpdu_no_rx_on_intf_down> ] [ <idb_stat_mkpdu_rx_ca_notfound>
 ] [ <idb_stat_mkpdu_rx_error> ] [ <idb_stat_mkpdu_rx_success> ] [ <idb_stat_mkpdu_failure_rx_integrity_check_error> ] [ <idb_stat_mkpdu_failure_invalid_peer_mn_error>
 ] [ <idb_stat_mkpdu_failure_nonrecent_peerlist_mn_error> ] [ <idb_stat_mkpdu_failure_sakuse_kn_mismatch_error> ] [ <idb_stat_mkpdu_failure_sakuse_rx_not_set_error>
 ] [ <idb_stat_mkpdu_failure_sakuse_key_mi_mismatch_error> ] [ <idb_stat_mkpdu_failure_sakuse_an_not_in_use_error> ] [ <idb_stat_mkpdu_failure_sakuse_ks_rx_tx_not_set_error>
 ] [ <idb_stat_mkpdu_failure_sakuse_eapol_ethertype_mismatch_error> ] [ <idb_stat_mkpdu_failure_sakuse_eapol_destmac_mismatch_error>
 ] [ <idb_stat_sak_failure_sak_generate_error> ] [ <idb_stat_sak_failure_hash_generate_error> ] [ <idb_stat_sak_failure_sak_encryption_error>
 ] [ <idb_stat_sak_failure_sak_decryption_error> ] [ <idb_stat_sak_failure_ick_derivation_error> ] [ <idb_stat_sak_failure_kek_derivation_error>
 ] [ <idb_stat_sak_failure_invalid_macsec_capability_error> ] [ <idb_stat_macsec_failure_rx_sa_create_error> ] [ <idb_stat_macsec_failure_tx_sa_create_error>
 ] ] ] ] [ TABLE_mka_gbl_stats [ [ <session_secured> ] [ <session_deleted> ] [ <session_keepalive_timeout> ] [ <ca_stat_pairwise_cak_rekey>
 ] [ <sa_stat_sak_generated> ] [ <sa_stat_sak_rekey> ] [ <sa_stat_sak_received> ] [ <sa_stat_sak_response_rx> ] [ <mkpdu_stat_mkpdu_rx>
 ] [ <mkpdu_stat_mkpdu_rx_distsak> ] [ <mkpdu_stat_mkpdu_tx> ] [ <mkpdu_stat_mkpdu_tx_distsak> ] [ <mka_error_session_failure_bring_up_error>
 ] [ <mka_error_sak_failure_sak_generate_error> ] [ <mka_error_sak_failure_hash_generate_error> ] [ <mka_error_sak_failure_sak_encryption_error>
 ] [ <mka_error_sak_failure_sak_decryption_error> ] [ <mka_error_sak_failure_sak_cipher_mismatch_error> ] [ <mka_error_ca_failure_ick_derivation_error>
 ] [ <mka_error_ca_failure_kek_derivation_error> ] [ <mka_error_ca_failure_invalid_macsec_capability_error> ] [ <mka_error_macsec_failure_rx_sa_create_error>
 ] [ <mka_error_macsec_failure_tx_sa_create_error> ] [ <mka_error_mkpdu_failure_mkpdu_tx_error> ] [ <mka_error_mkpdu_failure_mkpdu_rx_integrity_check_error>
 ] [ <mka_error_mkpdu_failure_mkpdu_invalid_peer_mn_error> ] [ <mka_error_mkpdu_failure_mkpdu_nonrecent_peerlist_mn_error>
 ] [ <mka_error_mkpdu_failure_sakuse_kn_mismatch_error> ] [ <mka_error_mkpdu_failure_sakuse_rx_not_set_error> ] [ <mka_error_mkpdu_failure_sakuse_key_mi_mismatch_error>
 ] [ <mka_error_mkpdu_failure_sakuse_an_not_in_use_error> ] [ <mka_error_mkpdu_failure_sakuse_ks_rx_tx_not_set_error> ] [ <global_stats_mkpdu_rx_invalid_ckn>
 ] [ <global_stats_mkpdu_tx_pkt_build_fail> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| macsec | Show MACSEC information |
| mka | Show MKA information |
| statistics | Show MKA statistics |
| interface | (Optional) Specify interface |
| ifname | (Optional) Interface list |
| __readonly__ | (Optional) |
| macsec_status | (Optional) Macsec status |
| TABLE_mka_intf_stats | (Optional) MKA Interface statistics |
| TABLE_ca_stats | (Optional) CA Statistics |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3893353492

---

# Command: show macsec policy

## Syntax
```
show macsec policy [ <policy_name> ] [ __readonly__ { TABLE_macsec_policy <name> <cipher_suite> <keyserver_priority> <window_size>
 <conf_offset> <security_policy> <sak-expiry-time> <include_icv_indicator> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| macsec | Show MACSEC policy information |
| policy | Show MACSEC policy information |
| policy_name | (Optional) Name of MACSEC Policy |
| __readonly__ | (Optional) |
| TABLE_macsec_policy | (Optional) |
| name | (Optional) MACSEC Policy Name |
| cipher_suite | (Optional) Cipher Suite |
| keyserver_priority | (Optional) KeyServer Priority |
| window_size | (Optional) Window Size |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3503083003

---

# Command: show macsec secy statistics

## Syntax
```
show macsec secy statistics [ interface <ifname> ] [ __readonly__ [ <macsec_status> ] [ TABLE_statistics <ifname2> [ <in_pkts_unicast_uncontrolled>
 ] [ <in_pkts_multicast_uncontrolled> ] [ <in_pkts_broadcast_uncontrolled> ] [ <in_rx_drop_pkts_uncontrolled> ] [ <in_rx_err_pkts_uncontrolled>
 ] [ <in_pkts_unicast_controlled> ] [ <in_pkts_multicast_controlled> ] [ <in_pkts_broadcast_controlled> ] [ <in_pkts_controlled>
 ] [ <in_rx_drop_pkts_controlled> ] [ <in_rx_err_pkts_controlled> ] [ <in_octets_uncontrolled> ] [ <in_octets_controlled> ]
 [ <input_rate_uncontrolled_pps> ] [ <input_rate_uncontrolled_bps> ] [ <input_rate_controlled_pps> ] [ <input_rate_controlled_bps>
 ] [ <out_pkts_unicast_uncontrolled> ] [ <out_pkts_multicast_uncontrolled> ] [ <out_pkts_broadcast_uncontrolled> ] [ <out_rx_drop_pkts_uncontrolled>
 ] [ <out_rx_err_pkts_uncontrolled> ] [ <out_pkts_unicast_controlled> ] [ <out_pkts_multicast_controlled> ] [ <out_pkts_broadcast_controlled>
 ] [ <out_pkts_controlled> ] [ <out_rx_drop_pkts_controlled> ] [ <out_rx_err_pkts_controlled> ] [ <out_octets_uncontrolled>
 ] [ <out_octets_controlled> ] [ <out_octets_common> ] [ <output_rate_uncontrolled_pps> ] [ <output_rate_uncontrolled_bps>
 ] [ <output_rate_controlled_pps> ] [ <output_rate_controlled_bps> ] [ <in_pkts_transform_error> ] [ <in_pkts_control> ] [
 <in_pkts_untagged> ] [ <in_pkts_no_tag> ] [ <in_pkts_badtag> ] [ <in_pkts_no_sci> ] [ <in_pkts_unknown_sci> ] [ <in_pkts_tagged_ctrl>
 ] [ <out_pkts_transform_error> ] [ <out_pkts_control> ] [ <out_pkts_untagged> ] [ TABLE_rx_sa_an <rx_sa_an> [ <in_pkts_unchecked>
 ] [ <in_pkts_delayed> ] [ <in_pkts_late> ] [ <in_pkts_ok> ] [ <in_pkts_invalid> ] [ <in_pkts_not_valid> ] [ <in_pkts_not_using_sa>
 ] [ <in_pkts_unused_sa> ] [ <in_octets_decrypted> ] [ <in_octets_validated> ] ] [ TABLE_tx_sa_an <tx_sa_an> [ <out_pkts_encrypted_protected>
 ] [ <out_pkts_too_long> ] [ <out_pkts_sa_not_inuse> ] [ <out_octets_encrypted_protected> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| macsec | Show MACSEC information |
| secy | Show MACSEC secy entity information |
| statistics | Show MACSEC secy statistics |
| interface | (Optional) Specify interface |
| ifname | (Optional) Interface list |
| __readonly__ | (Optional) |
| macsec_status | (Optional) Macsec status |
| TABLE_statistics | (Optional) MACsec secy statistics |
| in_pkts_unicast_uncontrolled | (Optional) In Pkts Unicast Uncontrolled |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2676088800

---

# Command: show maintenance maint-delay

## Syntax
```
show maintenance maint-delay [ __readonly__ <delay> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| maintenance | maintenance |
| maint-delay | maintenance mode CLI release delay value |
| __readonly__ | (Optional) |
| delay | (Optional) delay value in seconds |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1483896020

---

# Command: show maintenance on-reload reset-reasons

## Syntax
```
show maintenance on-reload reset-reasons [ __readonly__ [ TABLE_reset_reason <reset_reason> ] <rr_bitmap> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| maintenance | maintenance |
| on-reload | on reload maintenance mode configuration |
| reset-reasons | system reset reasons |
| __readonly__ | (Optional) |
| TABLE_reset_reason | (Optional) |
| rr_bitmap | (Optional) reset reason bitmap |
| reset_reason | (Optional) system reset reason |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1801305134

---

# Command: show maintenance profile

## Syntax
```
show maintenance profile [ <mode> ] [ __readonly__ TABLE_profile <name> [ TABLE_cfg <cfg> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| maintenance | maintenance |
| profile | maintenance profile |
| mode | (Optional) |
| __readonly__ | (Optional) |
| TABLE_profile | (Optional) |
| name | (Optional) profile name |
| TABLE_cfg | (Optional) |
| cfg | (Optional) profile config |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1863660713

---

# Command: show maintenance snapshot-delay

## Syntax
```
show maintenance snapshot-delay [ __readonly__ <delay> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| maintenance | maintenance |
| snapshot-delay | after_maintenance snapshot delay value |
| __readonly__ | (Optional) |
| delay | (Optional) delay value in seconds |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3633403998

---

# Command: show maintenance timeout

## Syntax
```
show maintenance timeout [ __readonly__ <timeout> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| maintenance | maintenance |
| timeout | timeout value |
| __readonly__ | (Optional) |
| timeout | (Optional) timeout value |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp1530848901

---

# Command: show module

## Syntax
```
show module [ { <module> } &#124; { <s0> [ <santa-cruz-range> ] } &#124; { fabric [ <module> ] } ] [ __readonly__ { TABLE_modinfo <modinf>
 <ports> <modtype> <model> <status> } [ { TABLE_modpwrinfo <modpwr> <pwrstat> <reason> } ] { TABLE_modwwninfo <modwwn> <sw>
 <hw> <slottype> } [ { TABLE_modapplinfo <modappl> <desc> <applver> } ] { TABLE_modmacinfo <modmac> <mac> <serialnum> } { TABLE_moddiaginfo
 <mod> <diagstatus> } [ { TABLE_xbarinfo <xbarinf> <xbarports> <xbartype> <xbarmodel> <xbarstatus> } ] [ { TABLE_xbarpwrinfo
 <xbarpwr> <xbarpwrstat> <xbarreason> } ] [ { TABLE_xbarwwninfo <xbarwwn> <xbarsw> <xbarhw> <xbarwwnstr> } ] [ { TABLE_xbarmacinfo
 <xbarmac> <xbarmacaddr> <xbarserialnum> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| module | Show module information |
| module | (Optional) Enter module number |
| s0 | (Optional) Show xbar information |
| santa-cruz-range | (Optional) please enter the xbar number |
| fabric | (Optional) Show fabric information |
| __readonly__ | (Optional) |
| TABLE_modinfo | (Optional) Show Module info |
| modinf | (Optional) Module |
| ports | (Optional) Num Ports |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1597313255

---

# Command: show module bandwidth-fairness

## Syntax
```
show module <module> bandwidth-fairness [ __readonly__ { TABLE_fairness <statement> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| module | Show module information |
| module | Enter module number |
| bandwidth-fairness | Show bandwidth fairness status |
| __readonly__ | (Optional) |
| TABLE_fairness | (Optional) |
| statement | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, qos, S-commands
**Command ID:** wp3151976169

---

# Command: show module uptime

## Syntax
```
show module uptime [ __readonly__ { TABLE_uptimeinf <slot> <starttime> <daysup> <hoursup> <minutesup> <secondsup> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| module | Show module information |
| uptime | Show how long the module has been up and running |
| __readonly__ | (Optional) |
| TABLE_uptimeinf | (Optional) Show uptime info |
| slot | (Optional) Slot |
| starttime | (Optional) Start Time |
| daysup | (Optional) Days Up |
| hoursup | (Optional) Hours Up |
| minutesup | (Optional) Minutes Up |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2260026928

---

# Command: show monitor

## Syntax
```
show monitor [ __readonly__ TABLE_session <session_number> <state> <state_reason> <description> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| monitor | Show Ethernet SPAN information |
| __readonly__ | (Optional) Read only |
| TABLE_session | (Optional) show monitor |
| session_number | (Optional) session id |
| state | (Optional) State |
| state_reason | (Optional) State reason |
| description | (Optional) Session Description |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp8115520390

---

# Command: show monitor session

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| monitor | Show Ethernet SPAN information |
| session | Show session info |
| all | All sessions |
| warp | warp session |
| range | Specify a range |
| brief | (Optional) Brief information |
| drops | (Optional) show drop count |
| __readonly__ | (Optional) Read only |
| TABLE_session | (Optional) show monitor |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, monitoring, S-commands
**Command ID:** wp2696874400

---

# Command: show mpls extended-ecmp

## Syntax
```
show mpls extended-ecmp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | MPLS routing ECMP mode |
| extended-ecmp | extended-ecmp mode (default) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1336249021

---

# Command: show mpls forwarding statistics

## Syntax
```
show mpls forwarding statistics [ interface { <interface> &#124; all } ] [ __readonly__ { TABLE_mpls_stats [ <intf_name> ] <mpls_packets_sent>
 <mpls_bytes_sent> <mpls_packets_received> <mpls_bytes_received> <mpls_packets_forwarded> <mpls_bytes_forwarded> <mpls_packets_originated>
 <mpls_bytes_originated> <mpls_packets_consumed> <mpls_bytes_consumed> <mpls_packets_input_dropped> <mpls_bytes_input_dropped>
 <mpls_packets_output_dropped> <mpls_bytes_output_dropped> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | MPLS information |
| forwarding | Display MPLS software forwarded |
| statistics | Traffic statistics |
| interface | (Optional) Interface specific information |
| interface | (Optional) Interface chosen to display statistics |
| all | (Optional) All interfaces |
| __readonly__ | (Optional) |
| TABLE_mpls_stats | (Optional) MPLS forwarding statistics |
| intf_name | (Optional) Interace name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2837020090

---

# Command: show mpls interfaces

## Syntax
```
show mpls interfaces [ __readonly__ TABLE_mpls_interface <intf> <oper> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| interfaces | Display MPLS Interfaces |
| __readonly__ | (Optional) |
| TABLE_mpls_interface | (Optional) |
| intf | (Optional) |
| oper | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp3352416120

---

# Command: show mpls interfaces detail

## Syntax
```
show mpls interfaces detail [ __readonly__ TABLE_mpls_interface_det <intf> <client_name> <oper_str> <ls_id> <mpls_sublayer_name>
 <mpls_sublayer_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| interfaces | Interfaces |
| detail | Detail |
| __readonly__ | (Optional) |
| TABLE_mpls_interface_det | (Optional) |
| intf | (Optional) |
| client_name | (Optional) |
| oper_str | (Optional) |
| ls_id | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2772795880

---

# Command: show mpls interfaces statistics

## Syntax
```
show mpls interfaces <ifname> statistics [ __readonly__ TABLE_mpls_interface_stats <intf> <enabled> [ <pkts_in> ] [ <bytes_in>
 ] [ <pkts_out> ] [ <bytes_out> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| interfaces | Interfaces |
| ifname | Interface Name |
| statistics | statistics |
| __readonly__ | (Optional) |
| TABLE_mpls_interface_stats | (Optional) |
| intf | (Optional) |
| enabled | (Optional) |
| pkts_in | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1191247641

---

# Command: show mpls ip bindings

## Syntax
```
show mpls ip bindings [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ generic ] [ { <prefix> { <mask> &#124; <mask-length> }
 &#124; <prefix-mask> } [ longer-prefix ] ] [ neighbor <addr> &#124; local ] [ [ local-label <local-label> [ local-to <local-label-max>
 ] ] &#124; [ remote-label <remote-label> [ remote-to <remote-label-max> ] ] ] [ advertisement-prefix-list &#124; detail ] [ __readonly__
 { TABLE_bnd [ <ldp_ctx> ] [ <llaf> ] [ { TABLE_bnd_acl_list <oldstyle> <prefix_acl> <peer_acl> } ] [ { TABLE_bnd_rec <lib_addr>
 <lib_mask> [ <lcl_bnd_rev> ] [ <no_route> ] [ <chkpt> ] [ <local_label> ] [ <withdraw> ] [ { TABLE_bnd_peer_list <peer_ident>
 } ] [ <remote_label> ] [ <remote_lsr> ] [ <rem_lbl_in_use> ] [ <stale_gr> ] [ <advert_acl_pending> ] [ <peer_acl> ] [ <prefix_acl>
 ] } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| ip | MPLS IP information |
| bindings | Show the MPLS IP Label Information Base (LIB) |
| vrf | (Optional) VRF Routing/Forwarding instance information |
| vrf-name | (Optional) VPN Routing/Forwarding instance name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display LIB information in all VRFs |
| generic | (Optional) Display generic labels |
| prefix | (Optional) Destination prefix |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp4031816974

---

# Command: show mpls ip bindings summary

## Syntax
```
show mpls ip bindings summary [ __readonly__ { TABLE_bnd [ <total_prefixes> ] [ <assigned_bindings> ] [ <local_bindings> ]
 [ <rem_bindings> ] [ <total_rt_info> ] [ <current_prev_lbl_entries> ] [ <total_prev_lbl_entries> ] [ <current_prev_lbl_queues>
 ] [ <total_prev_lbl_queues> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| ip | MPLS IP information |
| bindings | Show the MPLS IP Label Information Base (LIB) |
| summary | Show summary information |
| __readonly__ | (Optional) Read Only |
| TABLE_bnd | (Optional) Show bindings or tib summary for a vrf |
| total_prefixes | (Optional) Total number of prefixes |
| assigned_bindings | (Optional) Total number of assigned bindings |
| total_rt_info | (Optional) Total tib route info alloced |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp3581038548

---

# Command: show mpls ip ttl

## Syntax
```
show mpls ip ttl [ __readonly__ TABLE_mpls_ip_ttl <prop_or_exp> [ <forwarded> ] [ <local> ] [ <exp_count> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| ip | Display IP information |
| ttl | TTL related information |
| __readonly__ | (Optional) |
| TABLE_mpls_ip_ttl | (Optional) |
| prop_or_exp | (Optional) |
| forwarded | (Optional) |
| local | (Optional) |
| exp_count | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, network, S-commands
**Command ID:** wp3869166279

---

# Command: show mpls label range

## Syntax
```
show mpls label range [ __readonly__ <dynamic-min> <dynamic-max> [ <static-min> <static-max> ] [ <srgb-min> <srgb-max> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | MPLS configuration commands |
| label | Label properties |
| range | Label range |
| __readonly__ | (Optional) |
| dynamic-min | (Optional) |
| dynamic-max | (Optional) |
| static-min | (Optional) |
| static-max | (Optional) |
| srgb-min | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp6334768640

---

# Command: show mpls load-sharing

## Syntax
```
show mpls load-sharing [ __readonly__ TABLE_mpls_load_sharing [ <label-ip> ] [ <label-only> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | MPLS information |
| load-sharing | Show mpls load sharing options |
| __readonly__ | (Optional) |
| TABLE_mpls_load_sharing | (Optional) Table for MPLS Load Sharing |
| label-ip | (Optional) Label IP load sharing |
| label-only | (Optional) Label only load sharing |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3336905900

---

# Command: show mpls oam echo statistics

## Syntax
```
show mpls oam echo statistics [ summary ] [ __readonly__ <rq_sent> <rq_timeout> <rq_unsent> <rq_rcvd> <rx_sent> <rx_unsent>
 <rx_rcvd> <rc_zero> <rc_one> <rc_two> <rc_three> <rc_four> <rc_five> <rc_six> <rc_seven> <rc_eight> <rc_nine> <rc_ten> <rc_eleven>
 <rc_twelve> <rc_thirteen> <rc_fourteen> <summary_flag> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| oam | Display OAM information |
| echo | Echo request information |
| statistics | Detailed Echo packet statistics |
| summary | (Optional) Echo packet statistics summary |
| __readonly__ | (Optional) |
| rq_sent | (Optional) Requests sent |
| rq_timeout | (Optional) Requests timeout |
| rq_unsent | (Optional) Requests unsent |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1235594922

---

# Command: show mpls static binding

## Syntax
```
show mpls static binding [ vrf { <vrf-name> &#124; <vrf-known-name> } ] { { ipv4 [ <prefix> { <mask> &#124; <mask-length> } &#124; <prefix-mask>
 ] [ local &#124; remote ] [ nexthop <addr> ] [ inconsistency ] [ lsp <slb_name> ] } &#124; { ipv6 [ <ipv6-prefix> ] [ local &#124; remote
 ] [ ipv6-nexthop <ipv6-addr> ] [ inconsistency ] } &#124; all [ inconsistency ] } [ __readonly__ [ TABLE_slb [ <slb_name> ] [ <slb_prefix>
 ] [ <slb_mask> ] <slb_vrf> <slb_inlabel> [ <slb_type> ] [ TABLE_slb_outlbl_list [ <slb_nh_path_num> ] <slb_nhop> <slb_outlabel>
 ] [ <inconsistency_reason> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| static | Show MPLS static information |
| binding | Show static label bindings |
| ipv4 | Show ipv4 static label bindings |
| ipv6 | Show ipv6 static label bindings |
| all | Show all static label bindings |
| vrf | (Optional) VRF Routing/Forwarding instance information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2634424925

---

# Command: show mpls static binding

## Syntax
```
show mpls static binding [ ipv4 ] [ vrf { <vrf-name> &#124; <vrf-known-name> } ] [ <prefix> { <mask> &#124; <mask-length> } &#124; <prefix-mask>
 ] [ local &#124; remote ] [ nexthop <addr> ] [ __readonly__ { TABLE_slb [ <slb_prefix> <slb_mask> ] <slb_vrf> <slb_inlabel> [ {
 TABLE_slb_outlbl_list <slb_nhop> <slb_outlabel> } ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| static | Show MPLS static information |
| binding | Show static label bindings |
| ipv4 | (Optional) Show ipv4 static label bindings |
| vrf | (Optional) VRF Routing/Forwarding instance information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| prefix | (Optional) Destination prefix |
| mask | (Optional) Destination prefix mask |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp4175973467

---

# Command: show mpls static binding vrf per-vrf

## Syntax
```
show mpls static binding [ ipv4 ] vrf { <vrf-name> &#124; <vrf-known-name> } per-vrf [ __readonly__ { TABLE_slb_per_vrf <slb_vrf_per_vrf>
 <slb_inlabel_per_vrf> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| static | Show MPLS static information |
| binding | Show static label bindings |
| ipv4 | (Optional) Show ipv4 static label bindings |
| vrf | VRF Routing/Forwarding instance information |
| vrf-name | VRF name |
| vrf-known-name | Known VRF name |
| per-vrf | per-vrf static label bindings |
| __readonly__ | (Optional) Read Only |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, overlay, S-commands
**Command ID:** wp3395173008

---

# Command: show mpls static trace

## Syntax
```
show mpls static trace { error &#124; warning &#124; event } [ size ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| static | Static Label Bindings |
| trace | MPLS static trace |
| error | MPLS static error trace |
| warning | MPLS static warning trace |
| event | MPLS static event trace |
| size | (Optional) trace buffer size in Kbytes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1711600376

---

# Command: show mpls strip labels

## Syntax
```
show mpls strip labels [ all &#124; static &#124; dynamic &#124; <label_val> ] [ __readonly__ <disp_summary> [ TABLE_labels <disp_label>
 <disp_age> <disp_interface> <disp_pkt_cnt> <disp_stats> <disp_static> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | MPLS information |
| strip | Stripping of MPLS headers |
| labels | labels added in the system |
| all | (Optional) all labels [default] |
| static | (Optional) labels programmed using cli |
| dynamic | (Optional) dynamically learned |
| label_val | (Optional) Label to show |
| __readonly__ | (Optional) Read Only |
| disp_summary | (Optional) Summary |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, routing, network, S-commands
**Command ID:** wp3524868200

---

# Command: show mpls switching

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| switching | Display the MPLS label switching database |
| traffic-eng | (Optional) Show traffic-engineering related entries |
| srpath | (Optional) Show traffic-engineering segment-routing path entries |
| ip-addr | (Optional) Match destination address |
| ipv4-prefix | (Optional) Specify an IP prefix/mask |
| fec | (Optional) Show FEC information in the ULIB |
| private | (Optional) Show more detailed information in the ULIB |
| labels | (Optional) Show a specific label-related information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2022638407

---

# Command: show mpls switching clients

## Syntax
```
show mpls switching clients [ __readonly__ [ TABLE_client <pib-name> <pib-index> <pib-uuid> <pib-sap> <stale-time> <pib-flag>
 [ <stale-due> ] <reg-msg> <conv-msg> [ <inv-conv> ] <fec-msg> <fec-add> <ile-add> <fec-del> <ile-del> <last-xid> <fec-ack>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mpls | Display MPLS status and configuration |
| switching | Display the MPLS label switching database |
| clients | Display ULIB client components |
| __readonly__ | (Optional) |
| TABLE_client | (Optional) |
| pib-name | (Optional) Name of the client(pib) |
| pib-index | (Optional) PIB Index |
| pib-uuid | (Optional) PIB UUID |
| pib-sap | (Optional) MTS SAP for the pib |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3264974745

---

# Command: show mvpn bgp mdt

## Syntax
```
show mvpn bgp { mdt-safi &#124; auto-discovery } [ mdt-source <src-addr> ] [ __readonly__ { TABLE_entry <bgp_rd> <mdt_src> <mdt_grp>
 <local> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvpn | Display Multicast VPN information |
| bgp | Display BGP related information |
| mdt-safi | Display Auto-discovered BGP MDT-SAFI database |
| auto-discovery | Display Auto-discovered BGP MDT-SAFI database |
| mdt-source | (Optional) Source address of MVPN neighbor |
| src-addr | (Optional) Source Address |
| __readonly__ | (Optional) |
| TABLE_entry | (Optional) |
| bgp_rd | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1373268719

---

# Command: show mvpn mdt encap

## Syntax
```
show mvpn mdt encap [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; all } ] [ __readonly__ TABLE_vrf <out_context> { TABLE_encap <encap_index>
 <mdt_grp> <mdt_src> <mdt_src_if> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvpn | Display Multicast VPN information |
| mdt | Display MDT information |
| encap | Display MDT Encap table |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| all | (Optional) Display information for all VRFs |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2995181830

---

# Command: show mvpn mdt route

## Syntax
```
show mvpn mdt route [ detail ] [ __readonly__ TABLE_vrf <out_context> [ TABLE_mroute <src_addr> <grp_addr> <uptime> <ref_count>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvpn | Display Multicast VPN information |
| mdt | Display MDT information |
| route | Display MDT route information |
| detail | (Optional) Display detailed information |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) |
| out_context | (Optional) |
| TABLE_mroute | (Optional) |
| src_addr | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2195593796

---

# Command: show mvr

## Syntax
```
show mvr [ verbose ] [ __readonly__ <mvr-status> <mvr-default-vlan> <number-of-mvr-vlans> [ <mvr-group-list> <cfg-nodes> <interface-cfg-nodes>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| verbose | (Optional) Show in detail |
| __readonly__ | (Optional) |
| mvr-status | (Optional) |
| mvr-default-vlan | (Optional) |
| number-of-mvr-vlans | (Optional) |
| mvr-group-list | (Optional) |
| cfg-nodes | (Optional) |
| interface-cfg-nodes | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp1491950313

---

# Command: show mvr groups

## Syntax
```
show mvr groups [ __readonly__ [ TABLE_group_list <ip-address> <ip-max-addr> <rn-count-char> <rn-count> <mvr-vlan-string>
 <if-name> ] [ [ <interface-name> ] [ <mvr-vlan> ] [ TABLE_mvr_vlan <global-mvr-vlan> ] <mvr-groups> <mvr-receiver-type> <mvr-source-type>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| groups | show mvr groups config |
| __readonly__ | (Optional) |
| TABLE_group_list | (Optional) |
| ip-address | (Optional) |
| ip-max-addr | (Optional) |
| rn-count-char | (Optional) |
| rn-count | (Optional) |
| mvr-vlan-string | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2548932386

---

# Command: show mvr interface

## Syntax
```
show mvr interface [ <if0> ] [ __readonly__ [ TABLE_if_name <interface-name> <access-vlan> <src-rcvr> <igmp-mvr-port-status>
 <mvr-vlan-str> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| interface | show mvr interfaces |
| if0 | (Optional) Interface name |
| __readonly__ | (Optional) |
| TABLE_if_name | (Optional) |
| interface-name | (Optional) |
| access-vlan | (Optional) |
| src-rcvr | (Optional) |
| igmp-mvr-port-status | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp1049888130

---

# Command: show mvr members

## Syntax
```
show mvr members [ interface <if0> ] [ __readonly__ [ TABLE_mvr_vlan <mvr-vlan> <group> <status> [ TABLE_members_if <if-name>
 ] ] [ <vlan> <mvr-group> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| members | show active mvr groups |
| interface | (Optional) show active mvr groups config on interface |
| if0 | (Optional) Interface name |
| __readonly__ | (Optional) |
| TABLE_mvr_vlan | (Optional) |
| mvr-vlan | (Optional) |
| group | (Optional) |
| status | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3041739130

---

# Command: show mvr members count

## Syntax
```
show mvr members count [ __readonly__ [ TABLE_mvr_vlan <mvr-vlan> <mvr-members-count> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| members | show active mvr groups |
| count | Active mvr groups on each mvr-vlan |
| __readonly__ | (Optional) |
| TABLE_mvr_vlan | (Optional) |
| mvr-vlan | (Optional) |
| mvr-members-count | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3410357129

---

# Command: show mvr members vlan

## Syntax
```
show mvr members { vlan <vlan-id> } [ __readonly__ [ TABLE_mvr_vlan <mvr-vlan> <grp> <stat> [ TABLE_interface_vlan <interface-name>
 ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| members | show active mvr groups |
| vlan | vlan |
| vlan-id | Enter MVR Vlan |
| __readonly__ | (Optional) |
| TABLE_mvr_vlan | (Optional) |
| mvr-vlan | (Optional) |
| grp | (Optional) |
| stat | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2540946819

---

# Command: show mvr receiver-ports

## Syntax
```
show mvr receiver-ports [ <if0> ] [ __readonly__ [ TABLE_mvr_if_name <mvr-if-name> <mvr-vlan-str> <igmp-port-status> <rx_reports>
 <rx_leaves> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| receiver-ports | List MVR receiver ports |
| if0 | (Optional) Interface name |
| __readonly__ | (Optional) |
| TABLE_mvr_if_name | (Optional) |
| mvr-if-name | (Optional) |
| mvr-vlan-str | (Optional) |
| igmp-port-status | (Optional) |
| rx_reports | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2969385440

---

# Command: show mvr source-ports

## Syntax
```
show mvr source-ports [ <if0> ] [ __readonly__ [ TABLE_mvr_if_name <mvr-if-name> <interface-name> <igmp-port-status> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| mvr | show mvr info |
| source-ports | List MVR source ports |
| if0 | (Optional) Interface name |
| __readonly__ | (Optional) |
| TABLE_mvr_if_name | (Optional) |
| mvr-if-name | (Optional) |
| interface-name | (Optional) |
| igmp-port-status | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01100.html
**Tags:** show-mode, interface, S-commands
**Command ID:** wp2537972679

---

