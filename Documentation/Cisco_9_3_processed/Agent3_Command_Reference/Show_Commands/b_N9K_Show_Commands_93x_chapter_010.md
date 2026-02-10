# Chapter: B Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010.html
**Type:** Show Commands  
**Chapter:** Group-10 Commands  
**Total Commands:** 59

## Command List

- `show background`
- `show banner exec`
- `show banner motd`
- `show bash-shell`
- `show bfd-app session status`
- `show bfd addrmap`
- `show bfd clients`
- `show bfd discrmap`
- `show bfd intfipmap`
- `show bfd neighbors`
- `show bfd scalar`
- `show bfd session`
- `show bgp`
- `show bgp`
- `show bgp`
- `show bgp`
- `show bgp`
- `show bgp`
- `show bgp`
- `show bgp bmp server`
- `show bgp community`
- `show bgp convergence`
- `show bgp convergence private`
- `show bgp dampening dampened`
- `show bgp dampening flap-statistics`
- `show bgp dampening parameters`
- `show bgp event-history`
- `show bgp evi`
- `show bgp extcommunity`
- `show bgp l3vpn`
- `show bgp neighbors`
- `show bgp neighbors`
- `show bgp neighbors commands`
- `show bgp neighbors flap-statistics`
- `show bgp neighbors paths`
- `show bgp paths`
- `show bgp peer-template`
- `show bgp peer`
- `show bgp prefix-list`
- `show bgp private`
- `show bgp private attr`
- `show bgp private damp`
- `show bgp private debug history`
- `show bgp process`
- `show bgp received-paths`
- `show bgp regexp`
- `show bgp self-originated`
- `show bgp sessions`
- `show bgp statistics`
- `show bgp summary`
- `show bgp summary`
- `show boot`
- `show boot auto-copy`
- `show boot auto-copy list`
- `show boot current`
- `show boot mode`
- `show boot order`
- `show boot timings`
- `show boot variables`

---

## Detailed Command Reference

# Command: show background

## Syntax
```
show background [ __readonly__ [ { TABLE_jobs <pid> <user_name> <terminal> <start> <time> <script> <args> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| background | show background processes (started with 'source background <file>' command) |
| __readonly__ | (Optional) |
| TABLE_jobs | (Optional) All background jobs |
| pid | (Optional) Process ID of the job |
| user_name | (Optional) User name of the process |
| terminal | (Optional) Termianl where job is running |
| start | (Optional) Start time of job |
| time | (Optional) Time |
| script | (Optional) Script name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, S-commands
**Command ID:** wp7207236820

---

# Command: show banner exec

## Syntax
```
show banner exec [ __readonly__ { banner_msg <b_msg> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| banner | Show current banner message |
| exec | Show current exec banner message |
| __readonly__ | (Optional) |
| banner_msg | (Optional) The banner message |
| b_msg | (Optional) The banner message |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, S-commands
**Command ID:** wp3499456721

---

# Command: show banner motd

## Syntax
```
show banner motd [ __readonly__ { banner_msg <b_msg> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| banner | Show current banner message |
| motd | Show current motd banner message |
| __readonly__ | (Optional) |
| banner_msg | (Optional) The banner message |
| b_msg | (Optional) The banner message |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, S-commands
**Command ID:** wp6364743110

---

# Command: show bash-shell

## Syntax
```
show bash-shell [ __readonly__ { operation_status <o_status> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bash-shell | Show bash shell status |
| __readonly__ | (Optional) |
| operation_status | (Optional) Bash shell status |
| o_status | (Optional) operational status of bash shell |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, S-commands
**Command ID:** wp1377851373

---

# Command: show bfd-app session status

## Syntax
```
show bfd-app session status { src-ip { <src_ip> dest-ip <dest_ip> &#124; <src_ipv6> dest-ip <dest_ipv6> } { iod <iod_id> &#124; intf
 <intf_id> } &#124; <all> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd-app | BFD application commands |
| session | session operation |
| src-ip | Source ip |
| src_ip | Source ip value |
| dest-ip | Destination ip |
| dest_ip | Destination ip value |
| iod | interface iod |
| iod_id | Interface iod in hex |
| intf | interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp2262087949

---

# Command: show bfd addrmap

## Syntax
```
show bfd addrmap [ application <appid> discriminator <discr> address-type <addrtype> address <addr> ] [ __readonly__ TABLE_bfdSessMapTable
 <ciscoBfdSessApplicationId> <ciscoBfdSessDiscriminator> <ciscoBfdSessAddrType> <ciscoBfdSessAddr> <ciscoBfdSessMapBfdIndex>
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| addrmap | Session |
| application | (Optional) |
| discriminator | (Optional) |
| address-type | (Optional) |
| address | (Optional) |
| appid | (Optional) |
| discr | (Optional) |
| addrtype | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp3141436583

---

# Command: show bfd clients

## Syntax
```
show bfd clients [ __readonly__ <header> [ { TABLE_bfdClients <client_name> <num_sess> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| clients | bfd client list |
| __readonly__ | (Optional) |
| header | (Optional) print header |
| TABLE_bfdClients | (Optional) BFD Client table |
| client_name | (Optional) client name |
| num_sess | (Optional) Number of sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp2178451466

---

# Command: show bfd discrmap

## Syntax
```
show bfd discrmap [ <discr> ] [ __readonly__ TABLE_bfdDiscMapTable <ciscoBfdSessDiscMapIndex> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| discrmap | Session |
| discr | (Optional) |
| __readonly__ | (Optional) |
| TABLE_bfdDiscMapTable | (Optional) Discriminator map table |
| ciscoBfdSessDiscMapIndex | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp4263360173

---

# Command: show bfd intfipmap

## Syntax
```
show bfd intfipmap [ interface <intf> address-type <addrtype> address <addr> ] [ __readonly__ TABLE_ipMapTable <ciscoBfdSessInterface>
 <ciscoBfdSessAddrType> <ciscoBfdSessAddr> <ciscoBfdSessIpMapIndex> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| intfipmap | Session |
| interface | (Optional) |
| address-type | (Optional) |
| address | (Optional) |
| intf | (Optional) |
| addrtype | (Optional) |
| addr | (Optional) |
| __readonly__ | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, network, bfd, S-commands
**Command ID:** wp3753969158

---

# Command: show bfd neighbors

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| ip_type | (Optional) ipv4 or ipv6 |
| neighbors | neighbors |
| multihop | (Optional) Display Multihop sessions only |
| module | (Optional) module |
| module | (Optional) module number |
| interface | (Optional) interface |
| intf_id | (Optional) show bfd sessions based on interface id |
| application | (Optional) application |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp3927382153

---

# Command: show bfd scalar

## Syntax
```
show bfd scalar [ __readonly__ <adminStatus> <version> <notifEnable> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| scalar | bfd mib scalars |
| __readonly__ | (Optional) |
| adminStatus | (Optional) bfd admin status |
| version | (Optional) bfd version number |
| notifEnable | (Optional) Enable bfd traps |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp3672000637

---

# Command: show bfd session

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bfd | BFD commands |
| session | Session |
| discriminator | (Optional) Session local discriminator |
| sessionIndex | (Optional) |
| interface | (Optional) interface |
| intf_id | (Optional) show bfd sessions based on interface id |
| application | (Optional) application |
| app_name | (Optional) show bfd session based on application name |
| src-ip | (Optional) Source ip |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, bfd, S-commands
**Command ID:** wp9169344870

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; all } { rib-install &#124; rib-uninstall &#124; rib-pending } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234
 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |
| all | Display BGP information for all address families |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2632692672

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } policy statistics
 { { redistribute [ { { eigrp &#124; isis &#124; ospf &#124; rip } <tag> } &#124; static &#124; direct &#124; amt &#124; lisp &#124; hmm &#124; am ] } &#124; { neighbor <neighbor-id>
 [ default-originate &#124; { route-map &#124; filter-list &#124; prefix-list } { in &#124; out } ] } &#124; { dampening } &#124; { network { <ip-addr> mask
 <ip-mask> &#124; <ip-prefix> } } &#124; { aggregate-address { <ip-addr> <ip-mask> &#124; <ip-prefix> } { suppress-map &#124; advertise-map } }
 } &#124; vpnv4 unicast policy statistics { neighbor <neighbor-id> [ { route-map &#124; filter-list &#124; prefix-list } { in &#124; out } ] }
 &#124; ipv6 { unicast &#124; multicast } policy statistics { { redistribute [ { { eigrp &#124; isis &#124; ospfv3 &#124; rip } <tag> } &#124; static &#124; direct
 &#124; amt &#124; lisp &#124; hmm &#124; am ] } &#124; { neighbor { <neighbor-id> &#124; <ipv6-neighbor-id> } [ default-originate &#124; { route-map &#124; filter-list
 &#124; prefix-list } { in &#124; out } ] } &#124; { dampening } &#124; { network <ipv6-prefix> } &#124; { aggregate-address <ipv6-prefix> { suppress-map
 &#124; advertise-map } } } } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-polstats>
 [ <rpm-handle-count> ] [ { TABLE_rmap <name> <action> <seqnum> [ { TABLE_cmd <command> <comparecount> <matchcount> } ] [ <totalacceptcount>
 ] [ <totalrejectcount> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| vpnv4 | Display BGP information for VPNv4 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1045132413

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { { ipv4 { unicast &#124; multicast } &#124; vpnv4 unicast
 [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 labeled-unicast } [ <ip-addr> [ <ip-mask> [ longer-prefixes
 ] ] [ detail ] &#124; <ip-prefix> [ longer-prefixes ] [ detail ] &#124; labels &#124; exported &#124; imported &#124; detail ] &#124; { ipv6 { unicast &#124;
 multicast } &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast } [ <ipv6-prefix>
 [ longer-prefixes ] [ detail ] &#124; labels &#124; exported &#124; imported &#124; detail ] &#124; { ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] } [ <ip-addr> [ <ip-mask> ] &#124; <ip-prefix> &#124; labels &#124; mdt-group <mdt-group> ] &#124; { ipv4 &#124; ipv6 } unicast [ injected-routes
 ] &#124; link-state [ route-type <rt-type> &#124; <ipv4-ls-rt> &#124; <ipv6-ls-rt> ] &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } [ { <ip-addr> [ <ip-mask> ] &#124; <ip-prefix> } &#124; { ve-id <ve-id> block-offset <ve-bs> } ] ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } [ join <v4src-addr> <v4grp-addr> <src-asn> &#124; rp <v4src-addr> <grp-v4prefix> <pe-addr> <rp-flags>
 <rp-priority> <hashlen> &#124; sa <grp-v4prefix> &#124; sa-ad <v4src-addr> <v4grp-addr> &#124; route-type { 1 &#124; 2 &#124; 3 &#124; 4 &#124; 5 &#124; 6 &#124; 7 } [
 detail ] ] &#124; route-type { 1 &#124; 2 &#124; 3 &#124; 4 &#124; 5 &#124; 6 &#124; 7 } [ detail ] &#124; join [ detail ] &#124; sa-ad [ detail ] &#124; i-pmsi [ detail ]
 ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } [ join <v6src-addr> <v6grp-addr> <src-asn> &#124; rp <v6src-addr>
 <grp-v6prefix> <pe-addr> <rp-flags> <rp-priority> <hashlen> &#124; sa <grp-v6prefix> &#124; sa-ad <v6src-addr> <v6grp-addr> &#124; route-type
 { 1 &#124; 2 &#124; 3 &#124; 4 &#124; 5 &#124; 6 &#124; 7 } [ detail ] ] &#124; route-type { 1 &#124; 2 &#124; 3 &#124; 4 &#124; 5 &#124; 6 &#124; 7 } [ detail ] &#124; join [ detail ] &#124; sa-ad
 [ detail ] &#124; i-pmsi [ detail ] ] &#124; l2vpn evpn [ route-type <rtype> [ etid <et> ] &#124; rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } [ route-type <rtype> [ etid <et> ] &#124; <ipv4-evpn-rt> &#124; <ipv6-evpn-rt> &#124; <mac-address> ] &#124; vni-id <vni_id> [ route-type <rtype>
 ] &#124; es <es-id> [ route-type <rtype> [ etid <et> ] ] &#124; <ipv4-evpn-rt> &#124; <ipv6-evpn-rt> &#124; <mac-address> ] &#124; all [ detail ] }
 [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi>
 TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix
 { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed>
 <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist> <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr>
 ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type> <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop>
 } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight> <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete>
 <pathvalid> <pathbest> <pathdeleted> <pathstaled> <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ]
 [ <importsource> [ <originalimportsource> ] ] [ <importdestscount> ] [ TABLE_importdests <importdest> ] [ <existpath> ] [
 <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric> { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin>
 [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate> ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community
 <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid> { TABLE_clusterlist <clusterlist> } ] [ <flappenalty>
 <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife> <flapreuse> <flapsuppress> <flapmax> ] [ <con_type>
 <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag> <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid>
 ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end> ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid>
 <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len> ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto
 <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ip-addr | (Optional) Display one particular network from the BRIB in detail |
| ip-mask | (Optional) Mask for one particular prefix in the BRIB |
| ip-prefix | (Optional) Display one particular prefix from the BRIB in detail |
| longer-prefixes | (Optional) Display route and more specific routes |
| labels | (Optional) Display BGP labels for prefixes |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp6383135890

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast &#124;
 link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv4 labeled-unicast &#124; all } { route-map { <rmap-name> &#124; <rmap-name> } &#124; filter-list { <fltrlist-name> &#124; <test_pol_name>
 } &#124; { community-list { <commlist-name> &#124; <test_pol_name> } &#124; extcommunity-list { <extcommlist-name> &#124; <test_pol_name> } }
 [ exact-match ] } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out>
 TABLE_afi <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid>
 ] ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths> <bestpathnr> [ <on-newlist>
 <on-xmitlist> <suppressed> <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist> <export-on-xmitlist> ]
 [ <locallabel> ] [ <labelhldwstr> ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type> <statuscode> <bestcode>
 <typecode> { <ipnexthop> &#124; <ipv6nexthop> } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight> <aspath> <origin> [ <metric>
 ] [ <localpref> ] } } } &#124; { [ <policyincomplete> <pathvalid> <pathbest> <pathdeleted> <pathstaled> <pathhistory> <pathovermaxaslimit>
 <pathmultipath> <pathnolabeledrnh> ] [ <importsource> [ <originalimportsource> ] ] [ <importdestscount> ] [ TABLE_importdests
 <importdest> ] [ <existpath> ] [ <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric> { <neighbor> &#124; <ipv6neighbor>
 } <neighborid> <origin> [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate> ] [ <inlabel> ]
 [ <originflag> ] [ { TABLE_community <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid> { TABLE_clusterlist
 <clusterlist> } ] [ <flappenalty> <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife> <flapreuse> <flapsuppress>
 <flapmax> ] [ <con_type> <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag> <psid_lindx> ] [
 <psid_v6sid_len> <psid_v6sid> ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end> ] ] [
 <remotenh> <remotenh_encap> <remotenh_vnid> <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len>
 ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| route-map | Display routes matching the route-map |
| rmap-name | Route-map name |
| rmap-name | Known route-map name |
| filter-list | Display routes matching the filter-list |
| fltrlist-name | Name of filter-list |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2932425096

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { { ipv4 { unicast &#124; multicast } &#124; ipv4 mdt
 [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 labeled-unicast } nexthop
 <ipnexthop> &#124; { ipv6 { unicast &#124; multicast } &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6
 labeled-unicast &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] } nexthop <ipv6nexthop> } [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi>
 <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix { <ipprefix>
 &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed> <needsresync>
 <locked> ] [ <table-map-filtered> ] [ <export-on-newlist> <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr> ] [ <mpath>
 ] ] { TABLE_path <pathnr> { { <status> <best> <type> <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop> } {
 { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight> <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete>
 <pathvalid> <pathbest> <pathdeleted> <pathstaled> <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ]
 [ <importsource> [ <originalimportsource> ] ] [ <importdestscount> ] [ TABLE_importdests <importdest> ] [ <existpath> ] [
 <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric> { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin>
 [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate> ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community
 <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid> { TABLE_clusterlist <clusterlist> } ] [ <flappenalty>
 <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife> <flapreuse> <flapsuppress> <flapmax> ] [ <con_type>
 <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag> <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid>
 ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end> ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid>
 <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len> ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto
 <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| nexthop | Display routes matching the nexthop |
| ipnexthop | Nexthop address |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3683252587

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { { { ipv4 { unicast &#124; multicast } &#124; vpnv4 unicast
 &#124; ipv4 mdt &#124; link-state &#124; l2vpn vpls &#124; l2vpn evpn &#124; ipv4 mvpn } nexthop-database [ <ipnexthop> ] } &#124; { { ipv6 { unicast &#124;
 multicast } &#124; vpnv6 unicast &#124; ipv6 mvpn } nexthop-database [ <ipv6nexthop> ] } &#124; { all nexthop-database } } [ vrf { <vrf-name>
 &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_nhvrf <nhvrf-name-out> TABLE_nhafi <nhafi> TABLE_nhsafi
 <nhsafi> <af-name> <nhcriticaldelay> <nhnoncriticaldelay> [ { TABLE_nexthop { <ipnexthop-out> &#124; <ipv6nexthop-out> } <refcount>
 <igpmetric> <multipath> <igptype> <igppref> [ { TABLE_attachedhops { <attachedhop> &#124; <ipv6attachedhop> } <interface> [ { TABLE_labels
 <index> <label> } ] } ] <attached> <local> <reachable> <labeled> <filtered> <suppressed> <resolvetime> { <ribroute> &#124; <ipv6ribroute>
 } { <pendingupdate> &#124; <pendingtime> } <nextadvertise> <rnhepoch> [ <pendingrnhepoch> ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| link-state | Display BGP information for link-state address family |
| l2vpn | Display BGP information for L2VPN address family |
| vpls | Display BGP information for L2VPN VPLS address family |
| nexthop-database | Display nexthop database |
| ipv4 | Display BGP information for IPv4 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3770822454

---

# Command: show bgp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } flap-statistics
 [ <ip-prefix> &#124; <ip-addr> [ <ip-mask> ] ] &#124; ipv6 { unicast &#124; multicast } flap-statistics [ <ipv6-prefix> ] &#124; all flap-statistics
 } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> [ TABLE_afi
 <afi> TABLE_safi <safi> <af-name> [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ <dampening> <historypaths> <dampenedpaths>
 ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <status> ] [ <pathtype> ] [ <peer> &#124; <ipv6peer> ] [ <flapcount>
 ] [ <duration> ] [ <reuse> ] [ <penalty> ] [ <suppresslimit> ] [ <reuselimit> ] [ <best> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| flap-statistics | Display route flap statistics |
| ip-prefix | (Optional) Display flap statistics for one prefix |
| ip-addr | (Optional) Display flap statistics for one network |
| ip-mask | (Optional) Network mask |
| ipv4 | Display BGP information for IPv4 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2291519280

---

# Command: show bgp bmp server

## Syntax
```
show bgp bmp server [ <server-id> ] [ detail ] [ __readonly__ { system_name <sys_name> } { system_description <sys_description>
 } [ { TABLE_servers <server_id> <server_addr> <port> <admin_state> <oper_state> [ <description> ] <vrf> [ <update_src> ] <initial_delay>
 <refresh_interval> <stats_interval> [ { <initiation> <termination> <peer_up> <peer_down> <route_monitor> <route_mirror> <stats>
 <messages_dropped> } ] [ <monitored_peers> ] [ { TABLE_peer <peer_addr> [ { <refresh_interval> <peer_up> <peer_down> <route_monitor>
 <route_mirror> <stats> <messages_dropped> } ] [ <prefixes_denied> <dup_pfx_advmnt> <pfx_dup_wdr_count> <cluster_list_loops>
 <as_path_loops> <as_confed_loops> <invalid_originator> <adj_rib_in> <loc-rib> ] } ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| bmp | Display BMP state |
| server | Display BMP server information |
| server-id | (Optional) Display server specific information |
| detail | (Optional) Display detailed information |
| __readonly__ | (Optional) |
| system_name | (Optional) bmp-server global information |
| sys_name | (Optional) system name |
| system_description | (Optional) bmp-server global information |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3186493512

---

# Command: show bgp community

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3576394342

---

# Command: show bgp convergence

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] convergence [ detail ] [ vrf { <vrf-name> &#124;
 <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ <starttime> <configdonetime> <juststarted> [ <initwaittime>
 ] [ <ldpconverged> ] [ <ulibconvergencesent> ] [ TABLE_vrf <vrf-name-out> <bestpathtimeout> <configuredtimeout> <updatedelay>
 [ <firstpeerup> ] <timerrunning> [ <timerexpires> ] [ TABLE_afi <afi> TABLE_safi <safi> <af-name> <total_configured_peers>
 <total_capable_peers> <firstbestpathsignalled> [ <firstbestpathsignalledtime> ] <firstbestpathdone> [ <firstbestpathdonetime>
 [ <lastbestpathsignalledtime> <lastbestpathdonetime> ] ] [ <riblibconvergencesent> ] [ <importtimerrunning> ] [ <importtimerexpires>
 ] [ { TABLE_rcvdpeers [ <peer> ] [ <ipv6peer> ] [ <signalledtimepeer> ] } ] [ { TABLE_notrcvdpeers [ <notpeer> ] [ <notipv6peer>
 ] [ <nokeepalive> ] [ <notsignalledtime> ] } ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| convergence | Display information about convergence |
| detail | (Optional) Display detailed information about convergence |
| __readonly__ | (Optional) |
| starttime | (Optional) |
| configdonetime | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3317241905

---

# Command: show bgp convergence private

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] convergence private [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; ALL_VRFS_012345678901234 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| convergence | Display information about convergence |
| private | Display private information about convergence |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp4229937612

---

# Command: show bgp dampening dampened

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast &#124;
 link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv4 labeled-unicast &#124; all } dampening { dampened-paths [ regexp <regexp-str> ] &#124; history-paths [ regexp <regexp-str>
 ] } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi
 <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix
 { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed>
 <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist> <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr>
 ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type> <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop>
 } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight> <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete>
 <pathvalid> <pathbest> <pathdeleted> <pathstaled> <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ]
 [ <importsource> [ <originalimportsource> ] ] [ <importdestscount> ] [ TABLE_importdests <importdest> ] [ <existpath> ] [
 <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric> { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin>
 [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate> ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community
 <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid> { TABLE_clusterlist <clusterlist> } ] [ <flappenalty>
 <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife> <flapreuse> <flapsuppress> <flapmax> ] [ <con_type>
 <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag> <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid>
 ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end> ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid>
 <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len> ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto
 <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| dampened-paths | Display all dampened paths |
| history-paths | Display all history paths |
| dampening | Display dampening info |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3918170000

---

# Command: show bgp dampening flap-statistics

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast &#124;
 link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv4 labeled-unicast &#124; all } dampening flap-statistics [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234
 } ] [ __readonly__ TABLE_vrf <vrf-name-out> [ TABLE_afi <afi> TABLE_safi <safi> <af-name> [ TABLE_rd [ <rd_val> [ <rd_vrf>
 ] [ <rd_vniid> ] ] [ <dampening> <historypaths> <dampenedpaths> ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix>
 } [ <status> ] [ <pathtype> ] [ <peer> &#124; <ipv6peer> ] [ <flapcount> ] [ <duration> ] [ <reuse> ] [ <penalty> ] [ <suppresslimit>
 ] [ <reuselimit> ] [ <best> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| dampening | Display dampening info |
| flap-statistics | Display flap statistics for routes |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2903901098

---

# Command: show bgp dampening parameters

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast &#124;
 link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv4 labeled-unicast &#124; all } dampening parameters [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 }
 ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ TABLE_rd [ <rd_val> ] [ <rd_vrf> ]
 [ <rd_vniid> ] [ <rpmname> ] [ TABLE_rpm <rpmindex> <rpmdamphalflife> <rpmdampsuppress> <rpmdampreuse> <rpmdampsuppresstime>
 <rpmdampmaxpenalty> ] [ <dampconfigured> <damphalflife> <dampsuppress> <dampreuse> <dampsuppresstime> <dampmaxpenalty> ] ]
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| dampening | Display dampening info |
| parameters | Display dampening parameters |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2421166561

---

# Command: show bgp event-history

## Syntax
```
show bgp [ internal ] event-history { <bgp-event-hist> &#124; msgs &#124; sdwrap-errors }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| internal | (Optional) Commands for internal use |
| event-history | Show various event logs of BGP |
| bgp-event-hist | Show BGP event log |
| msgs | Show various message logs of BGP |
| sdwrap-errors | Show SDWRAP library error logs of BGP |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp4201470763

---

# Command: show bgp evi

## Syntax
```
show bgp evi [ <evi-id> ] [ __readonly__ [ TABLE_ctx <evid> <rd> <numlocalprefixes> <numtotalprefixes> <created> <lastoperup>
 <lastoperdown> <enabled> [ <associatedvrf> ] [ TABLE_activeexportrts <exportrt> ] [ TABLE_activeimportrts <importrt> ] [ TABLE_evpnactiveexportrts
 <evpnexportrt> ] [ TABLE_evpnactiveimportrts <evpnimportrt> ] [ TABLE_mvpnactiveexportrts <mvpnexportrt> ] [ TABLE_mvpnactiveimportrts
 <mvpnimportrt> ] [ TABLE_activeexportrtsv6 <exportrtv6> ] [ TABLE_activeimportrtsv6 <importrtv6> ] [ TABLE_evpnactiveexportrtsv6
 <evpnexportrtv6> ] [ TABLE_evpnactiveimportrtsv6 <evpnimportrtv6> ] [ TABLE_mvpnactiveexportrtsv6 <mvpnexportrtv6> ] [ TABLE_mvpnactiveimportrtsv6
 <mvpnimportrtv6> ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| evi | Display information about EVI database |
| evi-id | (Optional) EVI Id |
| __readonly__ | (Optional) |
| TABLE_ctx | (Optional) |
| evid | (Optional) |
| rd | (Optional) |
| numlocalprefixes | (Optional) |
| numtotalprefixes | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1486445097

---

# Command: show bgp extcommunity

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1297639025

---

# Command: show bgp l3vpn

## Syntax
```
show bgp l3vpn [ detail ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out>
 [ <vrf-id> ] [ <vrf-rd> ] [ <vrf-state> ] [ <vrf-state-rsn> ] [ <vrf-pending-rd> ] [ { TABLE_af <af-id> [ <af-name> ] [ <af-table-id>
 ] [ <af-state> ] [ <af-state-rsn> ] [ <af-num-peers> ] [ <af-num-active-peers> ] [ <af-peer-routes> ] [ <af-peer-paths> ]
 [ <af-peer-networks> ] [ <af-peer-aggregates> ] [ <af-export-rmap> ] [ <af-import-rmap> ] [ <af-retain-rt> ] [ TABLE_export_rt
 <export-rt> ] [ TABLE_import_rt <import-rt> ] [ TABLE_evpn_export_rt <evpn-export-rt> ] [ TABLE_evpn_import_rt <evpn-import-rt>
 ] [ TABLE_mvpn_export_rt <mvpn-export-rt> ] [ TABLE_mvpn_import_rt <mvpn-import-rt> ] [ <af-label-mode> ] [ <af-aggregate-label>
 ] } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| l3vpn | BGP l3vpn information |
| vrf | (Optional) Virtual Router Context |
| detail | (Optional) Detailed information |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| __readonly__ | (Optional) Read Only |
| TABLE_vrf | (Optional) |
| vrf-name-out | (Optional) VRF name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3040526882

---

# Command: show bgp neighbors

## Syntax
```
show bgp { { [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 {
 unicast &#124; multicast } &#124; all } } &#124; vpnv4 unicast &#124; vpnv6 unicast &#124; ipv6 labeled-unicast &#124; ipv4 labeled-unicast &#124; l2vpn evpn
 } neighbors { <neighbor-id> &#124; <ipv6-neighbor-id> } { routes [ advertised &#124; received &#124; dampened ] &#124; advertised-routes &#124; received-routes
 } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi>
 TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix
 { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed>
 <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist> <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr>
 ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type> <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop>
 } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight> <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete>
 <pathvalid> <pathbest> <pathdeleted> <pathstaled> <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ]
 [ <importsource> [ <originalimportsource> ] ] [ <importdestscount> ] [ TABLE_importdests <importdest> ] [ <existpath> ] [
 <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric> { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin>
 [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate> ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community
 <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid> { TABLE_clusterlist <clusterlist> } ] [ <flappenalty>
 <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife> <flapreuse> <flapsuppress> <flapmax> ] [ <con_type>
 <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag> <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid>
 ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end> ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid>
 <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len> ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto
 <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| neighbors | Display all configured BGP neighbors |
| neighbor-id | Display one particular BGP neighbor |
| ipv4 | Display BGP information for IPv4 address family |
| vpnv4 | Display BGP information for VPNv4 address family |
| vpnv6 | Display BGP information for VPNv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3175341533

---

# Command: show bgp neighbors

## Syntax
```
show bgp { { [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 {
 unicast &#124; multicast } &#124; all } } &#124; vpnv4 unicast &#124; vpnv6 unicast &#124; ipv6 labeled-unicast &#124; link-state &#124; l2vpn vpls &#124; l2vpn evpn
 &#124; ipv4 mvpn &#124; ipv6 mvpn &#124; ipv4 labeled-unicast } neighbors [ { <neighbor-id> &#124; <ipv6-neighbor-id> &#124; <neighbor-prefix-id> &#124;
 <ipv6-neighbor-prefix-id> } ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ [ TABLE_neighbor
 { <neighbor> &#124; <ipv6neighbor> &#124; <templatepeer> &#124; <ipv4prefixneighbor> &#124; <ipv6prefixneighbor> } [ <remoteas> ] [ <localas>
 ] <link> [ <peertype> ] [ <index> ] [ TABLE_peer <peer> ] [ <maxprefixpeers> ] [ <configpeer> ] [ <inherit-template> ] [ <inherit-session-template>
 ] [ { <prefix-parent> &#124; <ipv6prefix-parent> } ] [ <description> ] [ <version> <remote-id> <state> <up> [ <elapsedtime> ] [
 <restarttime> ] ] [ <sourceif> ] [ <connectedif> ] [ <connectedcheck> ] [ <lowmemexempt> ] [ <bfd> ] [ <bfdmintxinterval>
 ] [ <bfdminrxinterval> ] [ <bfdmultiplier> ] [ <bfdauthenticationtype> ] [ <ttlsecurity> ] [ <ttllimit> ] [ <dscp> ] [ <password>
 ] [ <passiveonly> ] [ <activepeers> <closingpeers> <maxconcurrentpeers> ] [ <allocatedpeers> ] [ <totalpeersaccepted> ] [
 <localas-inactive> ] <remove-privateas> [ <gshut-activate> ] [ <gshut-map> ] { { [ <lastread> ] <holdtime> <keepalivetime>
 [ <lastwrite> ] [ <keepalive> ] <msgrecvd> <notificationsrcvd> <recvbufbytesinq> <msgsent> <notificationssent> <sentbytesoutstanding>
 <sentbytespacked> <connsestablished> <connsdropped> [ <connattempts> ] { { [ <peerresettime> ] <peerresetreason> [ <resettime>
 ] <resetreason> } &#124; { [ <resettime> ] <resetreason> [ <peerresettime> ] <peerresetreason> } } [ <capsnegotiated> <capmpadvertised>
 [ <caprefreshadvertised> <capgrdynamicadvertised> ] [ <capmprecvd> <caprefreshrecvd> <capgrdynamicrecvd> ] [ <capolddynamicadvertised>
 <capolddynamicrecvd> <caprradvertised> <caprrrecvd> <capoldrradvertised> <capoldrrrecvd> <capas4advertised> <capas4recvd>
 ] [ { TABLE_af <af-afi> TABLE_saf <af-safi> <af-advertised> <af-recvd> <af-name> } ] [ <capgradvertised> <capgrrecvd> ] [
 { TABLE_graf <gr-afi> TABLE_grsaf <gr-safi> <gr-af-name> <gr-adv> <gr-recv> <gr-fwd> } ] [ <grrestarttime> <grstaletime> ]
 [ <grrecvdrestarttime> ] [ [ { TABLE_addpathscapaf <addpathscap-afi> TABLE_addpathscapsaf <addpathscap-safi> <addpathscap-af-name>
 <addpathssendcap-adv> <addpathsrecvcap-adv> <addpathssendcap-recv> <addpathsrecvcap-recv> } ] [ <capaddpathsadvertised> <capaddpathsrecvd>
 ] ] [ <capextendednhadvertised> <capextendednhrecvd> ] [ { TABLE_capextendednhaf <capextendednh-afi> TABLE_capextendednhsaf
 <capextendednh-safi> <capextendednh-af-name> } ] ] } &#124; { [ <configholdtime> <configkeepalivetime> ] } } [ <epe> ] [ <epe-adj-sids>
 ] [ <epe-peer-rpc-set> ] [ <epe-peer-sid> ] [ <epe-peer-set-name> ] [ <epe-peer-set-rpc-set> ] [ <epe-peer-set-sid> ] [ {
 TABLE_epe-adj { { <epe-adj-ip-local> <epe-adj-ip-remote> } &#124; { <epe-adj-ipv6-local> <epe-adj-ipv6-remote> } } [ <epe-adj-ifindex>
 <epe-adj-rpc-set> <epe-adj-sid> ] } ] [ <grstate> <grexpiry> ] [ <firstkeepalive> ] [ <openssent> <opensrecvd> <updatessent>
 <updatesrecvd> <keepalivesent> <keepaliverecvd> <rtrefreshsent> <rtrefreshrecvd> <capabilitiessent> <capabilitiesrecvd> <bytessent>
 <bytesrecvd> ] [ TABLE_peraf <per-afi> TABLE_persaf <per-safi> <per-af-name> [ <tableversion> ] [ <neighbortableversion> ]
 [ <pfxrecvd> ] [ <pathsrecvd> ] [ <pfxbytes> ] [ <pfxsent> ] [ <pathssent> ] [ <conditionmap> <advertisemap> <advertisemapstatus>
 ] <insoftreconfigallowed> [ <insoftreconfigallowedalways> ] [ <sendcommunity> ] [ <sendextcommunity> ] [ { <localnexthop>
 &#124; <ipv6localnexthop> } ] [ <thirdpartynexthop> ] [ <maxpfx> ] [ <maxpfx_threshold> ] [ <soo> ] [ <weight> ] [ <allowasin>
 ] <asoverride> <peerascheckdisabled> [ <vplssignalingprotocol> ] [ { TABLE_inpolicy <inpolicynr> <inpolicytype> <inpolicyname>
 [ <inpolicyhandle> ] } ] [ { TABLE_outpolicy <outpolicynr> <outpolicytype> <outpolicyname> [ <outpolicyhandle> ] } ] <rrconfigured>
 <defaultoriginate> [ <defaultoriginatermap> ] [ <defaultsent> ] [ <grpathssaved> ] [ <firsteorrecvd> ] [ <firsteortime> ]
 [ <pathsflushed> ] [ <lasteorrecvtime> ] [ <lasteorsenttime> ] [ <firstconvgtime> ] [ <pfxsentfirsteor> ] [ <unsuppress-map>
 ] [ { TABLE_policy_template <preference> <inherit-policy-template> } ] ] [ [ <threadid> ] [ <passivethreadid> <passivefd>
 ] [ { <localaddr> &#124; <ipv6localaddr> } <localport> { <remoteaddr> &#124; <ipv6remoteaddr> } <remoteport> <fd> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| neighbors | Display all configured BGP neighbors |
| neighbor-id | (Optional) Display one particular BGP neighbor |
| neighbor-prefix-id | (Optional) Display details for a prefix peering |
| ipv4 | Display BGP information for IPv4 address family |
| vpnv4 | Display BGP information for VPNv4 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2462092500

---

# Command: show bgp neighbors commands

## Syntax
```
show bgp { { [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 {
 unicast &#124; multicast } &#124; all } } &#124; vpnv4 unicast &#124; vpnv6 unicast &#124; l2vpn evpn } neighbors { <neighbor-id> &#124; <ipv6-neighbor-id>
 } commands [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ [ { TABLE_sesscmd <sessioncmd>
 <sessioncmdstatus> [ <sessioncmdtemplate> ] } ] [ TABLE_af <af-afi> TABLE_saf <af-safi> <af-name> [ { TABLE_polcmd <policycmd>
 <policycmdstatus> [ <policycmdtemplate> ] } ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| neighbor-id | Display one particular BGP neighbor |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| vpnv4 | Display BGP information for VPNv4 address family |
| vpnv6 | Display BGP information for VPNv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2304905917

---

# Command: show bgp neighbors flap-statistics

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; all } neighbors { <neighbor-id> &#124; <ipv6-neighbor-id> } flap-statistics [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> [ TABLE_afi <afi> TABLE_safi <safi> <af-name> [ TABLE_rd
 [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ <dampening> <historypaths> <dampenedpaths> ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix>
 &#124; <nonipprefix> } [ <status> ] [ <pathtype> ] [ <peer> &#124; <ipv6peer> ] [ <flapcount> ] [ <duration> ] [ <reuse> ] [ <penalty>
 ] [ <suppresslimit> ] [ <reuselimit> ] [ <best> ] ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| neighbors | Display all configured BGP neighbors |
| neighbor-id | Display one particular BGP neighbor |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3421726642

---

# Command: show bgp neighbors paths

## Syntax
```
show bgp { { [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 {
 unicast &#124; multicast } &#124; all } } &#124; vpnv4 unicast &#124; vpnv6 unicast &#124; ipv6 labeled-unicast &#124; ipv4 labeled-unicast &#124; link-state
 &#124; l2vpn evpn } neighbors { <neighbor-id> &#124; <ipv6-neighbor-id> } paths [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234
 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ TABLE_id <id> <hashvalue> <refcount>
 <metric> <aspath> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| neighbors | Display all configured BGP neighbors |
| neighbor-id | Display one particular BGP neighbor |
| ipv4 | Display BGP information for IPv4 address family |
| vpnv4 | Display BGP information for VPNv4 address family |
| vpnv6 | Display BGP information for VPNv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1727042947

---

# Command: show bgp paths

## Syntax
```
show [ ip ] bgp paths [ __readonly__ TABLE_id <id> <hashvalue> <refcount> <metric> <aspath> <origin> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ip | (Optional) Display IP information |
| bgp | Display BGP status and configuration |
| paths | Display Path information |
| __readonly__ | (Optional) |
| TABLE_id | (Optional) |
| id | (Optional) |
| hashvalue | (Optional) |
| refcount | (Optional) |
| metric | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3886023549

---

# Command: show bgp peer-template

## Syntax
```
show [ ip ] bgp peer-template [ <peer-template-name> ] [ __readonly__ { TABLE_neighbor <templatepeer> [ <remoteas> ] [ <inherit-template>
 ] [ <inherit-session-template> ] [ { <prefix-parent> &#124; <ipv6prefix-parent> } ] [ <description> ] [ <sourceif> ] [ <connectedcheck>
 ] [ <lowmemexempt> ] [ <bfd> ] [ <bfdmintxinterval> ] [ <bfdminrxinterval> ] [ <bfdmultiplier> ] [ <bfdauthenticationtype>
 ] [ <ttlsecurity> ] [ <ttllimit> ] [ <dscp> ] [ <password> ] [ <passiveonly> ] <localas-inactive> [ <remove-privateas> ] [
 <configholdtime> <configkeepalivetime> ] [ TABLE_peraf <per-afi> TABLE_persaf <per-safi> <per-af-name> [ <tableversion> ]
 [ <neighbortableversion> ] [ <pfxrecvd> ] [ <pathsrecvd> ] [ <pfxbytes> ] [ <pfxsent> ] [ <pathssent> ] [ <conditionmap> <advertisemap>
 <advertisemapstatus> ] <insoftreconfigallowed> [ <insoftreconfigallowedalways> ] [ <sendcommunity> ] [ <sendextcommunity>
 ] [ { <localnexthop> &#124; <ipv6localnexthop> } ] [ <thirdpartynexthop> ] [ <maxpfx> ] [ <maxpfx_threshold> ] [ <soo> ] [ <weight>
 ] [ <allowasin> ] <asoverride> <peerascheckdisabled> [ <vplssignalingprotocol> ] [ { TABLE_inpolicy <inpolicynr> <inpolicytype>
 <inpolicyname> [ <inpolicyhandle> ] } ] [ { TABLE_outpolicy <outpolicynr> <outpolicytype> <outpolicyname> [ <outpolicyhandle>
 ] } ] <rrconfigured> <defaultoriginate> [ <defaultoriginatermap> ] [ <defaultsent> ] [ <grpathssaved> ] [ <firsteorrecvd>
 ] [ <firsteortime> ] [ <pathsflushed> ] [ <lasteorrecvtime> ] [ <lasteorsenttime> ] [ <firstconvgtime> ] [ <pfxsentfirsteor>
 ] [ <unsuppress-map> ] [ { TABLE_policy_template <preference> <inherit-policy-template> } ] ] [ TABLE_vrf <vrf-name> [ TABLE_inheritingpeer
 <inheritingpeer> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ip | (Optional) Display IP information |
| bgp | Display BGP status and configuration |
| peer-template | Display information about a peer-template |
| peer-template-name | (Optional) Peer-template name |
| __readonly__ | (Optional) |
| TABLE_neighbor | (Optional) |
| templatepeer | (Optional) |
| remoteas | (Optional) |
| inherit-template | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2103324202

---

# Command: show bgp peer

## Syntax
```
show [ ip ] bgp { peer-session [ <session-template-name> ] &#124; peer-policy [ <policy-template-name> ] } [ __readonly__ TABLE_template
 <template> <present> [ { TABLE_command <command> [ <polarity> ] [ <updatesource> ] [ <description> ] [ <multihop> ] [ <holdtime>
 ] [ <keepalive> ] [ <dscp> ] [ <routemapin> ] [ <routemapout> ] [ <filterlistin> ] [ <filterlistout> ] [ <prefixlistin> ]
 [ <prefixlistout> ] [ <maxprefixlimit> ] [ <defaultorigin> ] } ] [ { TABLE_vrf <vrf-name> { TABLE_peer <inheritingpeer> }
 } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| ip | (Optional) Display IP information |
| bgp | Display BGP status and configuration |
| peer-session | Display information about a peer-session |
| peer-policy | Display information about a peer-policy |
| session-template-name | (Optional) Peer-session name |
| policy-template-name | (Optional) Peer-policy name |
| __readonly__ | (Optional) |
| TABLE_template | (Optional) |
| template | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp5335970480

---

# Command: show bgp prefix-list

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } } prefix-list { <prfxlist-name> &#124; <test_pol_name> } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234
 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [
 TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion>
 <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed> <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist>
 <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr> ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type>
 <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop> } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight>
 <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete> <pathvalid> <pathbest> <pathdeleted> <pathstaled>
 <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ] [ <importsource> [ <originalimportsource> ] ] [ <importdestscount>
 ] [ TABLE_importdests <importdest> ] [ <existpath> ] [ <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric>
 { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin> [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate>
 ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid>
 { TABLE_clusterlist <clusterlist> } ] [ <flappenalty> <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife>
 <flapreuse> <flapsuppress> <flapmax> ] [ <con_type> <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag>
 <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid> ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end>
 ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid> <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len>
 ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| prefix-list | Display routes matching the prefix-list |
| prfxlist-name | Name of prefix-list |
| test_pol_name | An existing test-list policy |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1997498683

---

# Command: show bgp private

## Syntax
```
show bgp private [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { all_private &#124; session &#124; ipc &#124; rnh
 &#124; lists &#124; rpm-info [ route-map <rpm-name> { <ip-prefix> &#124; <ipv6-prefix> } ] &#124; attr [ { <ip-prefix> } ] &#124; rpm-attribute-cache
 &#124; rpm-comm-attr-cache &#124; virtual [ summary ] } [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| private | Show BGP information intended for developer eyes only |
| all_private | Show all info |
| session | Show session info |
| lists | Show BGP internal lists |
| route-map | (Optional) Show information for route-map |
| rpm-info | Show BGP policy outbound info |
| ip-prefix | (Optional) Show attribute for a prefix |
| rpm-name | (Optional) Route-map name |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3979036903

---

# Command: show bgp private attr

## Syntax
```
show bgp private attr [ remote-nh ] [ [ [ ipv4 { unicast &#124; multicast } <ip-prefix> ] &#124; [ ipv6 { unicast &#124; multicast } <ipv6-prefix>
 ] ] [ detail ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| private | Show BGP information intended for developer eyes only |
| attr | Show BGP attributes |
| remote-nh | (Optional) Show Remote NH Attr |
| ipv4 | (Optional) Display BGP information for IPv4 address family |
| ipv6 | (Optional) Display BGP information for IPv6 address family |
| unicast | (Optional) Display BGP information for unicast address family |
| multicast | (Optional) Display BGP information for multicast address family |
| detail | (Optional) Show detailed info |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3727701826

---

# Command: show bgp private damp

## Syntax
```
show bgp private [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6
 { unicast &#124; multicast } &#124; all } damp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| private | Show BGP information intended for developer eyes only |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3544693097

---

# Command: show bgp private debug history

## Syntax
```
show bgp private debug history { all &#124; ead-es &#124; es &#124; mac }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| private | Show BGP information intended for developer eyes only |
| debug | Debug |
| history | history |
| all | all |
| ead-es | ead-es |
| es | es |
| mac | mac |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3522672430

---

# Command: show bgp process

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] process [ detail ] [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ [ <processid> <protocolstartedreason> <protocoltag> <protocolstate> <isolatemode>
 <gshut-aware> <gshut-activate> [ <gshut-map> ] <mmode> <memorystate> [ <mallocmemorystate> ] [ <platformmemorystate> ] [ <lowmemorytimer>
 ] [ <issu> ] <forwardingstatesaved> <asformat> [ <fabricsoo> ] [ <srgbmin> <srgbmax> ] [ <epeconfiguredpeers> <epeactivepeers>
 ] <attributeentries> <hwmattributeentries> <bytesused> <entriespendingdelete> <hwmentriespendingdelete> <pathsperattribute>
 <aspathentries> <aspathbytes> ] TABLE_vrf <vrf-name-out> [ <vrf-id> ] [ <vrf-state> ] [ <vrf-state-rsn> ] [ <vrf-delete-pending>
 ] [ <vrf-evpn-mpls> ] [ <vrf-vni-id> ] [ <vrf-vni-id-valid> ] [ <vrf-topo-id> ] [ <vrf-encap-type> ] [ <vrf-vtep-ip> ] [ <vrf-vtep-virtual-ip>
 ] [ <vrf-vtep-vipr> ] [ <vrf-router-mac> ] [ <vrf-vip-router-mac> ] [ <vrf-vipr-router-mac> ] [ <vrf-router-id> ] [ <vrf-cfgd-id>
 ] [ <vrf-local-as> ] [ <vrf-confed-id> ] [ <vrf-cluster-id> ] [ <vrf-reconnect-interval> ] [ <vrf-peers> ] [ <vrf-pending-peers>
 ] [ <vrf-est-peers> ] [ <vrf-cfgd-max-as-limit> ] [ <vrf-max-as-limit> ] [ <vrf-rd-configured> ] [ <vrf-rd> ] [ <vrf-pending-rd>
 ] { TABLE_af <af-id> [ <af-name> ] [ <af-table-id> ] [ <af-state> ] [ <af-state-rsn> ] [ <af-num-peers> ] [ <af-num-active-peers>
 ] [ <af-peer-routes> ] [ <af-peer-paths> ] [ <af-peer-networks> ] [ <af-peer-aggregates> ] [ <af-export-rmap> ] [ <af-import-rmap>
 ] [ <af-retain-rt> ] [ { TABLE_redist <protocol> <route-map> } ] <wait-igp-convergence> [ { TABLE_add_paths_selection <route-map>
 } ] [ TABLE_export_rt <export-rt> ] [ TABLE_import_rt <import-rt> ] [ TABLE_evpn_export_rt <evpn-export-rt> ] [ TABLE_evpn_import_rt
 <evpn-import-rt> ] [ TABLE_mvpn_export_rt <mvpn-export-rt> ] [ TABLE_mvpn_import_rt <mvpn-import-rt> ] [ <af-label-mode> ]
 [ <af-aggregate-label> ] [ <srv6-alloc-mode> ] [ <srv6-end-function> ] [ <importdefault_prefixlimit> <importdefault_prefixcount>
 <importdefault_map> <importdefault_advertisevpn> ] <import_vrf_advertisevpn> [ <exportdefault_prefixlimit> <exportdefault_prefixcount>
 <exportdefault_map> <exportdefault_allowvpn> ] <export_vrf_allowvpn> <af-rr> <default-information-enabled> [ <default-information-rd>
 <default-information-rt> ] <nexthop-trigger-delay-critical> <nexthop-trigger-delay-non-critical> [ <nexthop-route-map> ] }
 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| process | BGP global information |
| detail | (Optional) Detailed information |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| __readonly__ | (Optional) Read Only |
| processid | (Optional) |
| protocolstartedreason | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp9243889970

---

# Command: show bgp received-paths

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; ipv4 mdt [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv4 unicast [ rd { <ext-comm-rd-aa2nn4>
 &#124; <ext-comm-rd-aa4nn2> } ] &#124; vpnv6 unicast [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv6 labeled-unicast &#124;
 link-state &#124; l2vpn vpls [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; ipv4 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv6 mvpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2> } ] &#124; l2vpn evpn [ rd { <ext-comm-rd-aa2nn4> &#124; <ext-comm-rd-aa4nn2>
 } ] &#124; ipv4 labeled-unicast &#124; all } received-paths [ private ] [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234
 } ] [ __readonly__ TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [
 TABLE_rd [ <rd_val> [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion>
 <totalpaths> <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed> <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist>
 <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr> ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type>
 <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop> } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight>
 <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete> <pathvalid> <pathbest> <pathdeleted> <pathstaled>
 <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ] [ <importsource> [ <originalimportsource> ] ] [ <importdestscount>
 ] [ TABLE_importdests <importdest> ] [ <existpath> ] [ <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric>
 { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin> [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate>
 ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid>
 { TABLE_clusterlist <clusterlist> } ] [ <flappenalty> <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife>
 <flapreuse> <flapsuppress> <flapmax> ] [ <con_type> <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag>
 <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid> ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end>
 ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid> <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len>
 ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| received-paths | Display paths stored for soft-reconfig |
| rd | (Optional) Display information for a route distinguisher |
| ext-comm-rd-aa4nn2 | (Optional) VPN route distinguisher in aa4:nn or ip:nn format |
| ext-comm-rd-aa2nn4 | (Optional) VPN route distinguisher in aa:nn format |
| ipv4 | Display BGP information for IPv4 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1357048943

---

# Command: show bgp regexp

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; all } regexp <regexp-str> [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__
 TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val>
 [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths>
 <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed> <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist>
 <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr> ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type>
 <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop> } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight>
 <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete> <pathvalid> <pathbest> <pathdeleted> <pathstaled>
 <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ] [ <importsource> [ <originalimportsource> ] ] [ <importdestscount>
 ] [ TABLE_importdests <importdest> ] [ <existpath> ] [ <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric>
 { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin> [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate>
 ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid>
 { TABLE_clusterlist <clusterlist> } ] [ <flappenalty> <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife>
 <flapreuse> <flapsuppress> <flapmax> ] [ <con_type> <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag>
 <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid> ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end>
 ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid> <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len>
 ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |
| all | Display BGP information for all address families |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3817225100

---

# Command: show bgp self-originated

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; all } self-originated [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__
 TABLE_vrf <vrf-name-out> TABLE_afi <afi> TABLE_safi <safi> <af-name> [ <table-version> <router-id> ] [ TABLE_rd [ <rd_val>
 [ <rd_vrf> ] [ <rd_vniid> ] ] [ TABLE_prefix { <ipprefix> &#124; <ipv6prefix> &#124; <nonipprefix> } [ <prefixversion> <totalpaths>
 <bestpathnr> [ <on-newlist> <on-xmitlist> <suppressed> <needsresync> <locked> ] [ <table-map-filtered> ] [ <export-on-newlist>
 <export-on-xmitlist> ] [ <locallabel> ] [ <labelhldwstr> ] [ <mpath> ] ] { TABLE_path <pathnr> { { <status> <best> <type>
 <statuscode> <bestcode> <typecode> { <ipnexthop> &#124; <ipv6nexthop> } { { <inlabel> <outlabel> <vpn> <hold_down> } &#124; { <weight>
 <aspath> <origin> [ <metric> ] [ <localpref> ] } } } &#124; { [ <policyincomplete> <pathvalid> <pathbest> <pathdeleted> <pathstaled>
 <pathhistory> <pathovermaxaslimit> <pathmultipath> <pathnolabeledrnh> ] [ <importsource> [ <originalimportsource> ] ] [ <importdestscount>
 ] [ TABLE_importdests <importdest> ] [ <existpath> ] [ <aspath> <source> ] { <ipnexthop> &#124; <ipv6nexthop> } <nexthopmetric>
 { <neighbor> &#124; <ipv6neighbor> } <neighborid> <origin> [ <metric> ] <localpref> <weight> [ <aggregator> <aggregatoras> <atomicaggregate>
 ] [ <inlabel> ] [ <originflag> ] [ { TABLE_community <community> } ] [ { TABLE_extcommunity <extcommunity> } ] [ <originatorid>
 { TABLE_clusterlist <clusterlist> } ] [ <flappenalty> <dampenedtime> <flaps> <flaptime> <flapflags> <flapindex> <flaphalflife>
 <flapreuse> <flapsuppress> <flapmax> ] [ <con_type> <con_len> <con_rd> <con_ip> ] [ <psid_len> [ <psid_lindx_len> <psid_lindx_flag>
 <psid_lindx> ] [ <psid_v6sid_len> <psid_v6sid> ] [ <psid_origsrgb_len> <psid_origsrgb_flag> <psid_origsrgb_base> <psid_origsrgb_end>
 ] ] [ <remotenh> <remotenh_encap> <remotenh_vnid> <remotenh_mac> ] [ <pmsi> ] [ <evpn-esi> ] [ <link-state-attr> <link-state-attr-len>
 ] [ <mdt_grp_addr> ] } } } [ TABLE_advertisedto <advertisedto> ] [ TABLE_scheduledto <scheduledto> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |
| all | Display BGP information for all address families |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp1614417030

---

# Command: show bgp sessions

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] sessions [ vrf { <vrf-name> &#124; <vrf-known-name>
 &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ <totalpeers> <totalestablishedpeers> <localas> TABLE_vrf <vrf-name-out> <local-as>
 <vrfpeers> <vrfestablishedpeers> <router-id> [ TABLE_neighbor <neighbor-id> <connectionsdropped> <remoteas> [ <lastflap> ]
 [ <lastread> ] [ <lastwrite> ] <state> <localport> <remoteport> <notificationssent> <notificationsreceived> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| sessions | Display session information for all peers |
| __readonly__ | (Optional) |
| TABLE_vrf | (Optional) |
| vrf-name-out | (Optional) |
| local-as | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp9297550560

---

# Command: show bgp statistics

## Syntax
```
show bgp statistics [ __readonly__ <msgsent> <msgrecvd> <bytesent> <byterecvd> <opensent> <openrecvd> <updatesent> <updaterecvd>
 <kasent> <karecvd> <notifsent> <notifrecvd> <rrefreshsent> <rrefreshrecvd> <capsent> <caprecvd> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| statistics | BGP global statistics |
| __readonly__ | (Optional) |
| msgsent | (Optional) |
| msgrecvd | (Optional) |
| bytesent | (Optional) |
| byterecvd | (Optional) |
| opensent | (Optional) |
| openrecvd | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2787603068

---

# Command: show bgp summary

## Syntax
```
show bgp [ vrf { <vrf-name> &#124; <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast
 &#124; multicast } &#124; all } summary [ __readonly__ TABLE_vrf <vrf-name-out> [ <vrf-id> ] [ <vrf-state> ] [ <vrf-state-rsn> ] [ <vrf-delete-pending>
 ] [ <vrf-evpn-mpls> ] [ <vrf-vni-id> ] [ <vrf-vni-id-valid> ] [ <vrf-topo-id> ] [ <vrf-encap-type> ] [ <vrf-vtep-ip> ] [ <vrf-vtep-virtual-ip>
 ] [ <vrf-vtep-vipr> ] [ <vrf-router-mac> ] [ <vrf-vip-router-mac> ] [ <vrf-vipr-router-mac> ] [ <vrf-router-id> ] [ <vrf-cfgd-id>
 ] [ <vrf-local-as> ] [ <vrf-confed-id> ] [ <vrf-cluster-id> ] [ <vrf-reconnect-interval> ] [ <vrf-peers> ] [ <vrf-pending-peers>
 ] [ <vrf-est-peers> ] [ <vrf-cfgd-max-as-limit> ] [ <vrf-max-as-limit> ] [ <vrf-rd-configured> ] [ <vrf-rd> ] [ <vrf-pending-rd>
 ] [ TABLE_af <af-id> [ <af-name> ] [ <af-table-id> ] [ <af-state> ] [ <af-state-rsn> ] [ <af-num-peers> ] [ <af-num-active-peers>
 ] [ <af-peer-routes> ] [ <af-peer-paths> ] [ <af-peer-networks> ] [ <af-peer-aggregates> ] [ <af-export-rmap> ] [ <af-import-rmap>
 ] [ <af-retain-rt> ] TABLE_saf <safi> [ <af-name> ] [ <tableversion> ] [ <configuredpeers> ] [ <capablepeers> ] [ <totalnetworks>
 ] [ <totalpaths> ] [ <memoryused> ] [ <numberattrs> ] [ <bytesattrs> ] [ <numberpaths> ] [ <bytespaths> ] [ <numbercommunities>
 ] [ <bytescommunities> ] [ <numberclusterlist> ] [ <bytesclusterlist> ] [ <dampening> ] [ <historypaths> ] [ <dampenedpaths>
 ] [ <softreconfigrecvdpaths> ] [ <softreconfigidenticalpaths> ] [ <softreconfigcombopaths> ] [ <softreconfigfilteredrecvd>
 ] [ <softreconfigbytes> ] [ TABLE_neighbor <neighborid> [ <neighborversion> ] [ <msgrecvd> ] [ <msgsent> ] [ <neighbortableversion>
 ] [ <inq> ] [ <outq> ] [ <neighboras> ] [ <time> ] [ <state> ] [ <prefixreceived> ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| summary | Display summarized information of BGP state |
| ipv4 | Display BGP information for IPv4 address family |
| ipv6 | Display BGP information for IPv6 address family |
| unicast | Display BGP information for unicast address family |
| multicast | Display BGP information for multicast address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp2953529259

---

# Command: show bgp summary

## Syntax
```
show bgp { ipv4 { unicast &#124; multicast } &#124; ipv6 { unicast &#124; multicast } &#124; ipv4 mdt &#124; vpnv4 unicast &#124; vpnv6 unicast &#124; ipv6 labeled-unicast
 &#124; link-state &#124; l2vpn vpls &#124; ipv4 mvpn &#124; ipv6 mvpn &#124; l2vpn evpn &#124; ipv4 labeled-unicast &#124; all } summary [ vrf { <vrf-name> &#124;
 <vrf-known-name> &#124; ALL_VRFS_012345678901234 } ] [ __readonly__ TABLE_vrf <vrf-name-out> [ <vrf-id> ] [ <vrf-state> ] [ <vrf-state-rsn>
 ] [ <vrf-delete-pending> ] [ <vrf-evpn-mpls> ] [ <vrf-vni-id> ] [ <vrf-vni-id-valid> ] [ <vrf-topo-id> ] [ <vrf-encap-type>
 ] [ <vrf-vtep-ip> ] [ <vrf-vtep-virtual-ip> ] [ <vrf-vtep-vipr> ] [ <vrf-router-mac> ] [ <vrf-vip-router-mac> ] [ <vrf-vipr-router-mac>
 ] [ <vrf-router-id> ] [ <vrf-cfgd-id> ] [ <vrf-local-as> ] [ <vrf-confed-id> ] [ <vrf-cluster-id> ] [ <vrf-reconnect-interval>
 ] [ <vrf-peers> ] [ <vrf-pending-peers> ] [ <vrf-est-peers> ] [ <vrf-cfgd-max-as-limit> ] [ <vrf-max-as-limit> ] [ <vrf-rd-configured>
 ] [ <vrf-rd> ] [ <vrf-pending-rd> ] [ TABLE_af <af-id> [ <af-name> ] [ <af-table-id> ] [ <af-state> ] [ <af-state-rsn> ] [
 <af-num-peers> ] [ <af-num-active-peers> ] [ <af-peer-routes> ] [ <af-peer-paths> ] [ <af-peer-networks> ] [ <af-peer-aggregates>
 ] [ <af-export-rmap> ] [ <af-import-rmap> ] [ <af-retain-rt> ] TABLE_saf <safi> [ <af-name> ] [ <tableversion> ] [ <configuredpeers>
 ] [ <capablepeers> ] [ <totalnetworks> ] [ <totalpaths> ] [ <memoryused> ] [ <numberattrs> ] [ <bytesattrs> ] [ <numberpaths>
 ] [ <bytespaths> ] [ <numbercommunities> ] [ <bytescommunities> ] [ <numberclusterlist> ] [ <bytesclusterlist> ] [ <dampening>
 ] [ <historypaths> ] [ <dampenedpaths> ] [ <softreconfigrecvdpaths> ] [ <softreconfigidenticalpaths> ] [ <softreconfigcombopaths>
 ] [ <softreconfigfilteredrecvd> ] [ <softreconfigbytes> ] [ TABLE_neighbor <neighborid> [ <neighborversion> ] [ <msgrecvd>
 ] [ <msgsent> ] [ <neighbortableversion> ] [ <inq> ] [ <outq> ] [ <neighboras> ] [ <time> ] [ <state> ] [ <prefixreceived>
 ] ] ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| bgp | Display BGP status and configuration |
| vrf | (Optional) Virtual Router Context |
| vrf-name | (Optional) VRF name |
| vrf-known-name | (Optional) Known VRF name |
| summary | Display summarized information of BGP state |
| ipv4 | Display BGP information for IPv4 address family |
| vpnv4 | Display BGP information for VPNv4 address family |
| vpnv6 | Display BGP information for VPNv6 address family |
| ipv6 | Display BGP information for IPv6 address family |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, routing, S-commands
**Command ID:** wp3046265659

---

# Command: show boot

## Syntax
```
show boot [ __readonly__ { [ TABLE_bootvar_show <Str1> ] [ TABLE_Current_Bootvar <current_sup_module> <current_image> [ <current_sup_module>
 ] [ <current_image> ] <current_poap_status> ] [ TABLE_Startup_Bootvar <start_sup_module> <start_image> [ <start_sup_module>
 ] [ <start_image> ] <start_poap_status> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| __readonly__ | (Optional) |
| TABLE_bootvar_show | (Optional) Bootvar table |
| TABLE_Current_Bootvar | (Optional) Table for current boot variables |
| TABLE_Startup_Bootvar | (Optional) Table for boot variables on next reload |
| Str1 | (Optional) |
| current_sup_module | (Optional) Current boot variable supervisor module |
| current_image | (Optional) Current image set for boot variable |
| current_poap_status | (Optional) Current status for poap |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp3353116132

---

# Command: show boot auto-copy

## Syntax
```
show boot auto-copy [ __readonly__ { [ TABLE_auto_copy <Str1> <status> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| auto-copy | See if autocopy is turned on |
| __readonly__ | (Optional) |
| TABLE_auto_copy | (Optional) Auto copy table |
| Str1 | (Optional) |
| status | (Optional) status of auto copy is enable/disable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp3347998150

---

# Command: show boot auto-copy list

## Syntax
```
show boot auto-copy list [ __readonly__ { [ TABLE_auto_copy_list <Str1> <file> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| auto-copy | See if autocopy is turned on |
| list | Show the list of files to be auto-copied |
| __readonly__ | (Optional) |
| TABLE_auto_copy_list | (Optional) Auto copy table |
| Str1 | (Optional) |
| file | (Optional) file in the auto copy list |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp1849226489

---

# Command: show boot current

## Syntax
```
show boot current [ __readonly__ { [ TABLE_bootvar_current <Str1> ] [ TABLE_current_bootvar <current_sup_module> <current_image>
 [ <current_sup_module> ] [ <current_image> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| current | Show Current Bootvar Variables |
| __readonly__ | (Optional) |
| TABLE_bootvar_current | (Optional) Bootvar current table |
| TABLE_current_bootvar | (Optional) Current booted image table |
| Str1 | (Optional) |
| current_sup_module | (Optional) Current boot variable supervisor module |
| current_image | (Optional) Current image set for boot variable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp5174086190

---

# Command: show boot mode

## Syntax
```
show boot mode [ __readonly__ { [ TABLE_mode <Str1> <current_boot_mode> [ <configured_boot_mode> ] ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show boot mode information |
| boot | Show boot mode |
| mode | See if lxc boot is turned on |
| __readonly__ | (Optional) |
| TABLE_mode | (Optional) boot mode table |
| Str1 | (Optional) |
| current_boot_mode | (Optional) current running boot mode |
| configured_boot_mode | (Optional) configured boot mode in running config |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp7544990810

---

# Command: show boot order

## Syntax
```
show boot order [ __readonly__ { [ TABLE_bootvar_order <Str1> ] [ TABLE_boot_order <current_order> <next_order> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| order | Show Boot Order |
| __readonly__ | (Optional) |
| TABLE_bootvar_order | (Optional) Boot order table |
| TABLE_boot_order | (Optional) Current boot order table |
| Str1 | (Optional) |
| current_order | (Optional) order of the boot location |
| next_order | (Optional) order of the boot location |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp1358640800

---

# Command: show boot timings

## Syntax
```
show boot timings
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | show boot information |
| timings | show boot timings |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp4233186480

---

# Command: show boot variables

## Syntax
```
show boot variables [ __readonly__ { [ TABLE_boot_vars <Str1> <boot_variable> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| boot | Show Bootvar Variables |
| variables | Display the list of boot variables |
| __readonly__ | (Optional) |
| TABLE_boot_vars | (Optional) Show boot variables table |
| Str1 | (Optional) |
| boot_variable | (Optional) available boot variable |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010.html
**Tags:** show-mode, boot, S-commands
**Command ID:** wp1449323290

---

