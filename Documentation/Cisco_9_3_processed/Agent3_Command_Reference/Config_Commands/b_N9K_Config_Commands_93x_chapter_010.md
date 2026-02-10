# Chapter: B Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010.html
**Type:** Configuration Commands  
**Chapter:** Group-10 Commands  
**Total Commands:** 101

## Command List

- `backoff`
- `backup-bw`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth`
- `bandwidth kbps mbps gbps`
- `bandwidth kbps mbps gbps`
- `banner exec`
- `banner motd`
- `bcm-shell module`
- `bcm-shell module`
- `beacon`
- `begin exclude include end`
- `bestpath`
- `bfd-app session auto-expiry timeout`
- `bfd-app session remove`
- `bfd-app session src-ip dest intf`
- `bfd`
- `bfd`
- `bfd`
- `bfd`
- `bfd`
- `bfd`
- `bfd`
- `bfd authentication interop`
- `bfd authentication key-id key`
- `bfd echo-interface`
- `bfd echo-rx-interval`
- `bfd echo`
- `bfd interval`
- `bfd interval`
- `bfd interval min_rx multiplier`
- `bfd interval min_rx multiplier`
- `bfd move-session target`
- `bfd multihop authentication key-id key`
- `bfd multihop hosting-linecard add module`
- `bfd multihop hosting-linecard add module`
- `bfd multihop interval`
- `bfd multihop interval min_rx multiplier`
- `bfd multihop interval min_rx multiplier`
- `bfd neighbor src-ip dest`
- `bfd optimize subinterface`
- `bfd per-link`
- `bfd session-store remove client`
- `bfd session-store source-ip dest-ip intf client`
- `bfd session state state`
- `bfd slow-timer`
- `bfd startup-timer bfd startup-timer`
- `bfshell`
- `bfshell cmd`
- `bfshell module`
- `bfshell module cmd`
- `binary-location`
- `bind interface`
- `bind mac-address`
- `blink`
- `bloggerd live-process-core sap`
- `bloggerd log-dump all`
- `bloggerd log-dump once log-buffer sap event-history`
- `bloggerd log-dump once pss uuid`
- `bloggerd log-throttle`
- `bloggerd log-transfer`
- `bloggerd log-transfer`
- `bloggerd parse log-buffer file`
- `bloggerd parse log-buffer file sap`
- `bloggerd parse pss file`
- `bmp-activate-server`
- `bmp-server`
- `boot-install nxos`
- `boot-order`
- `boot`
- `boot aci`
- `boot auto-copy`
- `boot kickstart`
- `boot mode docker_cluster`
- `boot mode docker_standalone`
- `boot mode lxc`
- `boot nxos`
- `boot nxos sup-1`
- `boot nxos sup-1 sup-2`
- `boot nxos sup-2`
- `boot order bootflash`
- `boot order pxe`
- `boot poap enable`
- `boot system`
- `bootmode boot`
- `bootmode extruntime`
- `bootmode hitless`
- `bootmode module`
- `bootmode nodiagruntime`
- `bootmode runtime`
- `buffer-boost`
- `buffer-delete`
- `buffer-move`
- `burst-detect enable`
- `burst-detect rise-threshold bytes fall-threshold bytes2`

---

## Detailed Command Reference

# Command: backoff

## Syntax
```
backoff <initial-backoff> <maximum-backoff> &#124; no backoff
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| backoff | Set LDP session backoff parameters |
| initial-backoff | Initial session backoff time (seconds) |
| maximum-backoff | Maximum session backoff time (seconds) |

**Command Mode:** /exec/configure/ldp

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2143762874

---

# Command: backup-bw

## Syntax
```
backup-bw { <kbps> } &#124; no backup-bw
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| backup-bw | Represents bw for Fast Reroute backup |
| kbps | Amount of allocatable backup bw, any lsp may use |

**Command Mode:** /exec/configure/if-te

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp4014104600

---

# Command: bandwidth

## Syntax
```
bandwidth { <bandwidth_val> &#124; inherit [ <inherit_val> ] } &#124; no bandwidth { [ <bandwidth_val> ] &#124; inherit [ <inherit_val> ]
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Set bandwidth informational parameter |
| bandwidth_val | Bandwidth in kilobits |
| inherit | Specify that bandwidth is inherited |
| inherit_val | (Optional) Bandwidth in kilobits |

**Command Mode:** /exec/configure/if-ether-sub /exec/configure/if-ether-sub-p2p /exec/configure/if-port-channel-sub /exec/configure/if-ethernet-p2p
 /exec/configure/if-ethernet-all /exec/configure/if-eth-non-member /exec/configure/if-gig-ether-sub /exec/configure/if-remote-ethernet-sub

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp4141276059

---

# Command: bandwidth

## Syntax
```
bandwidth <bandwidth_val> &#124; no bandwidth
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Set bandwidth informational parameter |
| bandwidth_val | Bandwidth in kilobits |

**Command Mode:** /exec/configure/if-any-tunnel

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp1385534950

---

# Command: bandwidth

## Syntax
```
[no] bandwidth { { xxx <bw-value> [ bps &#124; kbps &#124; mbps &#124; gbps ] &#124; percent <percentage> } &#124; { remaining percent <rem-perc> }
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bandwidth | Specify bandwidth for the class |
| xxx | xxx |
| bps | (Optional) Bits per second |
| kbps | (Optional) Kilo bits per second |
| mbps | (Optional) Mega bits per second |
| gbps | (Optional) Giga bits per second |
| percent | Percentage of available bandwidth |
| percentage | Value in percentage |
| remaining | % of remaining bandwidth |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp1849228037

---

# Command: bandwidth

## Syntax
```
bandwidth <bandwidth_val> &#124; no bandwidth
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Set bandwidth informational parameter |
| bandwidth_val | Bandwidth in kilobits |

**Command Mode:** /exec/configure/if-vlan-common

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp4258246500

---

# Command: bandwidth

## Syntax
```
bandwidth { <bandwidth_val> &#124; inherit [ <inherit_val> ] } &#124; no bandwidth { [ <bandwidth_val> ] &#124; inherit [ <inherit_val> ]
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Set bandwidth informational parameter |
| inherit | Specify that bandwidth is inherited |

**Command Mode:** /exec/configure/if-eth-port-channel /exec/configure/if-port-channel-range /exec/configure/if-port-channel-sub /exec/configure/if-eth-port-channel-switch
 /exec/configure/if-eth-port-channel-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp2386355031

---

# Command: bandwidth

## Syntax
```
[no] bandwidth { { <bw-value> [ bps &#124; kbps &#124; mbps &#124; gbps ] &#124; percent <percentage> } &#124; { remaining percent <rem-perc> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bandwidth | Specify bandwidth for the class |
| bps | (Optional) Bits per second |
| kbps | (Optional) Kilo bits per second |
| mbps | (Optional) Mega bits per second |
| gbps | (Optional) Giga bits per second |
| percent | Percentage of available bandwidth |
| percentage | Value in percentage |
| remaining | % of remaining bandwidth |
| rem-perc | Value in percentage |

**Command Mode:** /exec/configure/policy-map/type/plc/class

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp4984568400

---

# Command: bandwidth

## Syntax
```
[no] bandwidth &#124; bandwidth { <bw> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Specify LSP bandwidth |
| bw | bandwidth requirement in kbps |

**Command Mode:** /exec/configure/te/lsp-attr

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp2025480145

---

# Command: bandwidth

## Syntax
```
[no] bandwidth &#124; bandwidth { <kbps> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | tunnel bandwidth requirement |
| kbps | bandwidth requirement in kbps |

**Command Mode:** /exec/configure/if-te /exec/configure/tunnel-te/cbts-member

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp2524574636

---

# Command: bandwidth kbps mbps gbps

## Syntax
```
{ { bandwidth { <val_kbps> kbps &#124; <val_mbps> mbps &#124; <val_gbps> gbps } } &#124; { dscp <dscp_val> } } &#124; { no { bandwidth &#124; dscp
 } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Bandwidth per flow |
| val_kbps | Per Flow Bandwidth in Kbps |
| kbps | Bandwidth value in Kbps |
| val_mbps | Per Flow Bandwidth in Mbps |
| mbps | Bandwidth value in Mbps |
| val_gbps | Per Flow Bandwidth in Gbps |
| gbps | Bandwidth value in Gbps |
| dscp | DSCP per flow |
| dscp_val | Per Flow DSCP |

**Command Mode:** /exec/configure/nbm-flow-policy/attr

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp3476672202

---

# Command: bandwidth kbps mbps gbps

## Syntax
```
{ { bandwidth { <val_kbps> kbps &#124; <val_mbps> mbps &#124; <val_gbps> gbps } } &#124; { dscp <dscp_val> } } &#124; { no { bandwidth &#124; dscp
 } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bandwidth | Bandwidth per flow |
| val_kbps | Per Flow Bandwidth in Kbps |
| kbps | Bandwidth value in Kbps |
| val_mbps | Per Flow Bandwidth in Mbps |
| mbps | Bandwidth value in Mbps |
| val_gbps | Per Flow Bandwidth in Gbps |
| gbps | Bandwidth value in Gbps |
| dscp | DSCP per flow |
| dscp_val | Per Flow DSCP |

**Command Mode:** /exec/configure/nbm-vrf/nbm-flow-policy/attr

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, qos, B-commands
**Command ID:** wp1178463751

---

# Command: banner exec

## Syntax
```
{ banner exec <lineNo> } &#124; { no banner exec }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| banner | Configure banner message |
| exec | Configure banner exec message |
| lineNo | Delimiter char (first char is delimiter char) followed by message ending with delimiter |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3877294584

---

# Command: banner motd

## Syntax
```
{ banner motd <line> } &#124; { no banner motd }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| banner | Configure banner message |
| motd | Configure banner motd message |
| line | Delimiter char (Very first char is delimiter char) followed by message ending with delimiter |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2999990459

---

# Command: bcm-shell module

## Syntax
```
bcm-shell module <module> <quoted-cmd>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bcm-shell | bcm shell/cmd |
| module | Module number of the linecard |
| module | Enter module number |
| quoted-cmd | the command to run on bcm-shell |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1583541003

---

# Command: bcm-shell module

## Syntax
```
bcm-shell module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bcm-shell | bcm shell/cmd |
| module | Module number of the linecard |
| module | Enter module number |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp7901724660

---

# Command: beacon

## Syntax
```
[no] beacon
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| beacon | Disable/enable the beacon for an interface |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1114044845

---

# Command: begin exclude include end

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| begin | Begin with the line that matches |
| exclude | Exclude lines that match |
| include | Include lines that match |
| end | End with the line that matches |
| -i | (Optional) Ignore case difference when comparing strings |
| -x | (Optional) Print only lines where the match is a whole line |
| expr | Search for the expression |
| next | (Optional) Print <num> lines of context after every matching line |
| prev | (Optional) Print <num> lines of context before every matching line |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2259974527

---

# Command: bestpath

## Syntax
```
[no] bestpath { always-compare-med &#124; med { missing-as-worst &#124; non-deterministic &#124; confed } &#124; compare-routerid &#124; compare-neighborid
 &#124; cost-community ignore &#124; as-path { multipath-relax &#124; ignore } &#124; igp-metric ignore }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bestpath | Change default bestpath selection algorithm |
| always-compare-med | Compare MED on paths from different AS |
| med | MED |
| missing-as-worst | Treat missing MED as highest MED |
| non-deterministic | Not always pick the best-MED path among paths from same AS |
| compare-routerid | Compare router-id for identical EBGP paths |
| compare-neighborid | When more paths available than max path config, use neighborid tibreaker |
| cost-community | cost community |
| ignore | Ignore cost communities in bestpath selection |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2949157398

---

# Command: bfd-app session auto-expiry timeout

## Syntax
```
bfd-app session auto-expiry { timeout <millis> &#124; now }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd-app | BFD application commands |
| auto-expiry | auto expiry start/end |
| session | session operation |
| timeout | timeout after |
| now | expiry reached, dont wait to timeout, do them now |
| millis | milli-secs later |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, bfd, B-commands
**Command ID:** wp3207483223

---

# Command: bfd-app session remove

## Syntax
```
bfd-app session remove { all &#124; intf <intf_id> &#124; iod <iod_id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd-app | BFD application commands |
| session | session operation |
| remove | Remove sessions |
| all | Remove all sessions |
| intf | Remove all sessions on interface |
| intf_id | Interface Id |
| iod | interface iod |
| iod_id | Interface iod in hex |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2350085292

---

# Command: bfd-app session src-ip dest intf

## Syntax
```
[no] bfd-app session src-ip { <src_ip> dest-ip <dest_ip> &#124; <src_ipv6> dest-ip <dest_ipv6> } { intf <intf_id> &#124; iod <iod_id>
 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd-app | BFD application commands |
| session | session operation |
| src-ip | Source ip |
| src_ip | Source ip value |
| dest-ip | Destination ip |
| dest_ip | Destination ip value |
| iod | interface iod |
| iod_id | Interface iod in hex |
| intf | interface |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp1270507519

---

# Command: bfd

## Syntax
```
[no] bfd [ ipv4 &#124; ipv6 ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| ipv4 | (Optional) ipv4 sessions |
| ipv6 | (Optional) ipv6 sessions |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-vlan /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp4242135436

---

# Command: bfd

## Syntax
```
[ no &#124; default ] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| bfd | Bidirectional Fast Detection for the neighbor |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp9136067580

---

# Command: bfd

## Syntax
```
[no] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | Enable IPv4 BFD on all ISIS interfaces |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3647258914

---

# Command: bfd

## Syntax
```
[no] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | Enable IPv4 BFD on all ISIS interfaces |

**Command Mode:** /exec/configure/router-isis/router-isis-af-ipv4 /exec/configure/router-isis/router-isis-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp4052295450

---

# Command: bfd

## Syntax
```
[no] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | Enable BFD on all OSPF interfaces |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp1328194025

---

# Command: bfd

## Syntax
```
[no] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | Enable BFD on all EIGRP interfaces |

**Command Mode:** /exec/configure/router-eigrp /exec/configure/router-eigrp/router-eigrp-vrf /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2389123500

---

# Command: bfd

## Syntax
```
[no] bfd
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | Enable BFD on all OSPF interfaces |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp6364141640

---

# Command: bfd authentication interop

## Syntax
```
bfd authentication interop &#124; no bfd authentication interop
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| authentication | Configure BFD authentication parameters |
| interop | Allows keys to be sent in network format to interop with non N3k/N9K switches |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-vlan /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp4015322289

---

# Command: bfd authentication key-id key

## Syntax
```
bfd [ { ipv4 &#124; ipv6 } ] authentication <auth_name> key-id <key_id_val> { key <key_val> &#124; hex-key <h_key_val> } &#124; no bfd [
 { ipv4 &#124; ipv6 } ] authentication
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| authentication | Configure BFD authentication parameters |
| ipv4 | (Optional) ipv4 sessions |
| ipv6 | (Optional) ipv6 sessions |
| auth_name | auth algorithm |
| key-id | Key ID to use in BFD frames |
| key_id_val | Key ID value |
| key | ASCII SHA1 secret |
| hex-key | HEX binary SHA1 secret |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-vlan /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3411375919

---

# Command: bfd echo-interface

## Syntax
```
[no] bfd echo-interface <ifindex>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| echo-interface | Configure interface used for bfd echo frames |
| ifindex | loopback interface |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, interface, bfd, B-commands
**Command ID:** wp1377586380

---

# Command: bfd echo-rx-interval

## Syntax
```
bfd [ ipv4 &#124; ipv6 ] echo-rx-interval <intv> &#124; no bfd [ ipv4 &#124; ipv6 ] echo-rx-interval
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| ipv6 | (Optional) ipv6 sessions |
| ipv4 | (Optional) ipv4 sessions |
| echo-rx-interval | Configure BFD session echo rx interval |
| intv | Echo Rx Interval in milliseconds |

**Command Mode:** /exec/configure /exec/configure/if-ma /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3948935235

---

# Command: bfd echo

## Syntax
```
[no] bfd [ { ipv4 &#124; ipv6 } ] echo
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| echo | Configure Echo function for all address families |
| ipv4 | (Optional) ipv4 sessions |
| ipv6 | (Optional) ipv6 sessions |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-vlan /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2297090272

---

# Command: bfd interval

## Syntax
```
[no] bfd [ ipv4 &#124; ipv6 ] interval [ <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| interval | Configure BFD session interval parameters |
| ipv6 | (Optional) ipv6 sessions |
| ipv4 | (Optional) ipv4 sessions |
| min_tx_mills | (Optional) TX interval in milliseconds |
| min_rx | (Optional) Minimum RX interval |
| min_rx_mills | (Optional) RX interval in milliseconds |
| multiplier | (Optional) Configure detect multiplier for bfd sessions |
| int_mult | (Optional) Detect Multiplier |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2392302119

---

# Command: bfd interval

## Syntax
```
[no] bfd [ ipv4 &#124; ipv6 ] interval [ <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| interval | Configure BFD session interval parameters |
| ipv6 | (Optional) ipv6 sessions |
| ipv4 | (Optional) ipv4 sessions |
| min_tx_mills | (Optional) TX interval in milliseconds |
| min_rx | (Optional) Minimum RX interval |
| min_rx_mills | (Optional) RX interval in milliseconds |
| multiplier | (Optional) Configure detect multiplier for bfd sessions |
| int_mult | (Optional) Detect Multiplier |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base /exec/configure/if-port-channel /exec/configure/if-ma /exec/configure/if-vlan
 /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3384244870

---

# Command: bfd interval min_rx multiplier

## Syntax
```
bfd [ ipv6 &#124; ipv4 ] interval <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| interval | Configure BFD session interval parameters |
| ipv6 | (Optional) ipv6 sessions |
| ipv4 | (Optional) ipv4 sessions |
| min_tx_mills | TX interval in milliseconds |
| min_rx | Minimum RX interval |
| min_rx_mills | RX interval in milliseconds |
| multiplier | Configure detect multiplier for bfd sessions |
| int_mult | Detect Multiplier |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base /exec/configure/if-port-channel /exec/configure/if-ma /exec/configure/if-vlan
 /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp2629185346

---

# Command: bfd interval min_rx multiplier

## Syntax
```
bfd [ ipv6 &#124; ipv4 ] interval <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| interval | Configure BFD session interval parameters |
| ipv6 | (Optional) ipv6 sessions |
| ipv4 | (Optional) ipv4 sessions |
| min_tx_mills | TX interval in milliseconds |
| min_rx | Minimum RX interval |
| min_rx_mills | RX interval in milliseconds |
| multiplier | Configure detect multiplier for bfd sessions |
| int_mult | Detect Multiplier |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp3137894554

---

# Command: bfd move-session target

## Syntax
```
bfd move-session target <module> [ <discr> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| move-session | move a session |
| target | Target module |
| module | Module number |
| discr | (Optional) Session discriminator |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3713828811

---

# Command: bfd multihop authentication key-id key

## Syntax
```
bfd multihop authentication <auth_name> key-id <key_id_val> { key <key_val> &#124; hex-key <h_key_val> } &#124; { no &#124; default } bfd
 multihop authentication [ <auth_name> key-id <key_id_val> { key <key_val> &#124; hex-key <h_key_val> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| bfd | Bidirectional Fast Detection for the neighbor |
| multihop | For Multihop sessions |
| authentication | Configure BFD authentication parameters |
| auth_name | auth algorithm |
| key-id | Key ID to use in BFD frames |
| key_id_val | Key ID value |
| key | ASCII SHA1 secret |
| hex-key | HEX binary SHA1 secret |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2952053009

---

# Command: bfd multihop hosting-linecard add module

## Syntax
```
[no] bfd multihop hosting-linecard add module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| multihop | Configure BFD Multihop session interval parameters |
| hosting-linecard | Add the linecard to hosting-linecard for multihop sessions |
| add | Add the linecard to hosting-linecard list for multihop sessions |
| module | Linecard or module number |
| module | Module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp4135995238

---

# Command: bfd multihop hosting-linecard add module

## Syntax
```
bfd multihop hosting-linecard add module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| multihop | Configure BFD Multihop session interval parameters |
| hosting-linecard | Add the linecard to hosting-linecard for multihop sessions |
| add | Add the linecard to hosting-linecard list for multihop sessions |
| module | Linecard or module number |
| module | Module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp1915496790

---

# Command: bfd multihop interval

## Syntax
```
[no] bfd multihop interval [ <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| multihop | Configure BFD Multihop session interval parameters |
| interval | Configure BFD multihop session interval parameters |
| min_tx_mills | (Optional) TX interval in milliseconds |
| min_rx | (Optional) Minimum RX interval |
| min_rx_mills | (Optional) RX interval in milliseconds |
| multiplier | (Optional) Configure detect multiplier for bfd multihop sessions |
| int_mult | (Optional) Detect Multiplier |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp3622260243

---

# Command: bfd multihop interval min_rx multiplier

## Syntax
```
bfd multihop interval <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| multihop | Configure BFD Multihop session interval parameters |
| interval | Configure BFD multihop session interval parameters |
| min_tx_mills | TX interval in milliseconds |
| min_rx | Minimum RX interval |
| min_rx_mills | RX interval in milliseconds |
| multiplier | Configure detect multiplier for bfd multihop sessions |
| int_mult | Detect Multiplier |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp2379444100

---

# Command: bfd multihop interval min_rx multiplier

## Syntax
```
bfd multihop interval <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult> &#124; { no &#124; default } bfd multihop interval
 [ <min_tx_mills> min_rx <min_rx_mills> multiplier <int_mult> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| bfd | Bidirectional Fast Detection for the neighbor |
| multihop | For Multihop sessions |
| interval | Configure BFD session interval parameters |
| min_tx_mills | TX interval in milliseconds |
| min_rx | Minimum RX interval |
| min_rx_mills | RX interval in milliseconds |
| multiplier | Configure detect multiplier for bfd sessions |
| int_mult | Detect Multiplier |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp1008612471

---

# Command: bfd neighbor src-ip dest

## Syntax
```
[no] bfd neighbor src-ip { <src_ip> dest-ip <dest_ip> &#124; <src_ipv6> dest-ip <dest_ipv6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| neighbor | BFD neighbor configuration commands (simulate client) |
| src-ip | Source ip |
| src_ip | Source ip value |
| dest-ip | Destination ip |
| dest_ip | Destination ip value |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp1161802706

---

# Command: bfd optimize subinterface

## Syntax
```
[no] bfd [ ipv4 ] optimize subinterface
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| optimize | optimize |
| subinterface | optimize subinterfaces |
| ipv4 | (Optional) ipv4 sessions |

**Command Mode:** /exec/configure/if-ma /exec/configure/if-ma-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, interface, bfd, B-commands
**Command ID:** wp1331902163

---

# Command: bfd per-link

## Syntax
```
[no] bfd [ { ipv4 &#124; ipv6 } ] per-link
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| per-link | Run BFD sessions on each port-channel link |
| ipv4 | (Optional) ipv4 sessions |
| ipv6 | (Optional) ipv6 sessions |

**Command Mode:** /exec/configure/if-eth-port-channel /exec/configure/if-port-channel-sub /exec/configure/if-eth-port-channel-p2p

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp2955753890

---

# Command: bfd session-store remove client

## Syntax
```
bfd session-store remove <hex_disc> client <int_cl>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| session-store | session store operation |
| remove | Remove session from session store |
| hex_disc | Session discriminator |
| client | Client Id |
| int_cl | client |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp4961169540

---

# Command: bfd session-store source-ip dest-ip intf client

## Syntax
```
bfd session-store source-ip <src_ip> dest-ip <dest_ip> intf <intf_id> client <int_cl>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| session-store | Session store operation |
| source-ip | source ip |
| src_ip | source ip value |
| dest-ip | dest ip |
| dest_ip | source ip value |
| intf | interface |
| intf_id | Interface Id |
| client | Client Id |
| int_cl | client |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, network, bfd, B-commands
**Command ID:** wp3717607684

---

# Command: bfd session state state

## Syntax
```
bfd session state <hex_disc> state <state_up_down>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfd | BFD commands |
| session | session related test |
| state | Change session state |
| hex_disc | Session discriminator |
| state | Change to state |
| state_up_down | UP/DOWN |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, bfd, B-commands
**Command ID:** wp1941225110

---

# Command: bfd slow-timer

## Syntax
```
bfd [ { ipv4 &#124; ipv6 } ] slow-timer <int_slow_timer> &#124; no bfd [ { ipv4 &#124; ipv6 } ] slow-timer
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bfd | BFD commands |
| slow-timer | Configure slow mode timer for sessions |
| int_slow_timer | Slow rate timer in milliseconds |
| ipv4 | (Optional) ipv4 sessions |
| ipv6 | (Optional) ipv6 sessions |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, bfd, B-commands
**Command ID:** wp3342937254

---

# Command: bfd startup-timer bfd startup-timer

## Syntax
```
bfd startup-timer <int_startup_timer> &#124; [ no ] bfd startup-timer
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bfd | BFD commands |
| startup-timer | Configure Delayed Start Up timer for sessions |
| int_startup_timer | Start Up timer in seconds |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, bfd, B-commands
**Command ID:** wp3127204600

---

# Command: bfshell

## Syntax
```
bfshell
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfshell | bfshell |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3550505604

---

# Command: bfshell cmd

## Syntax
```
bfshell cmd <cmd>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfshell | bfshell |
| cmd | Specify command |
| cmd | Quoted commands to be exec |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3282296371

---

# Command: bfshell module

## Syntax
```
bfshell module <module>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfshell | bfshell |
| module | Select module |
| module | Module number |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp5867248040

---

# Command: bfshell module cmd

## Syntax
```
bfshell module <module> cmd <cmd>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bfshell | bfshell |
| module | Select module |
| cmd | Specify command |
| module | Module number |
| cmd | Quoted commands to be exec |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2264862720

---

# Command: binary-location

## Syntax
```
[no] binary-location <source-uri>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| binary-location | the location binaries are downloaded from |
| source-uri | Location for restoration to pick up binaries |

**Command Mode:** /exec/configure/personality

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3651673767

---

# Command: bind interface

## Syntax
```
[no] bind interface <interface-name>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bind | Bind the VFC |
| interface | Bind the VFC to an interface |
| interface-name | Interface name |

**Command Mode:** /exec/configure/if-vfc

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, interface, B-commands
**Command ID:** wp3536346471

---

# Command: bind mac-address

## Syntax
```
[no] bind mac-address <mac0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bind | Bind the VFC |
| mac-address | Bind the VFC to a MAC Address |
| mac0 | Enter MAC addrress in dotted hex format |

**Command Mode:** /exec/configure/if-vfc

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1406074361

---

# Command: blink

## Syntax
```
[no] blink { module <module> &#124; <s0> <santa-cruz-range> &#124; chassis &#124; powersupply <psnum> &#124; fan <fan_num> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| blink | blink locator led |
| module | blink module led |
| module | please enter the module number |
| s0 | blink a specific xbar |
| santa-cruz-range | please enter the xbar number |
| chassis | blink chassis led |
| powersupply | blink powersupply led |
| psnum | powersupply number |
| fan | blink Fan led |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1966189931

---

# Command: bloggerd live-process-core sap

## Syntax
```
bloggerd live-process-core sap <sap>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| live-process-core | Dump the core of the live-process |
| sap | Dump core for a particular SAP |
| sap | Enter a valid SAP. Enter 0 for ALL SAPs in this VDC |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3274101795

---

# Command: bloggerd log-dump all

## Syntax
```
[no] bloggerd log-dump { all &#124; [ module <module> ] sap <sap_num> [ vdc <new_id> &#124; vdc-all ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bloggerd | Blogger commands |
| log-dump | Dump Log Buffer |
| all | Log Dump for ALL services across ALL modules in the switch on reaching threshold |
| module | (Optional) Enable Buffer Dump for particular Module |
| module | (Optional) Enter a valid Module Number |
| sap | Enable Buffer Dump for a particular sap |
| sap_num | Enter a valid SAP. Enter 0 for ALL SAPs in this VDC |
| vdc | (Optional) Enable Log Dump for a particular VDC. DEFAULT_VDC by default |
| new_id | (Optional) Enter a valid VDC ID |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1920556311

---

# Command: bloggerd log-dump once log-buffer sap event-history

## Syntax
```
bloggerd log-dump once log-buffer sap <sap> event-history { errors &#124; msgs &#124; { app-specific <uuid> instance <buffer-instance>
 } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| log-dump | Dump Log Buffer |
| once | Dump Log Buffer once immediately |
| log-buffer | Dump Log buffer |
| sap | Enable Buffer Dump for a particular sap |
| sap | Enter a valid SAP. Enter 0 for ALL SAPs in this VDC |
| event-history | Event-History Buffers |
| errors | event-history errors |
| msgs | event-history messages |
| app-specific | application specific event history |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3663639293

---

# Command: bloggerd log-dump once pss uuid

## Syntax
```
bloggerd log-dump once pss uuid <uuid>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| log-dump | Dump Log Buffer |
| once | Dump Log Buffer once immediately |
| pss | Dump PSS |
| uuid | Dump PSS for a particular UUID |
| uuid | Enter a app's UUID |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3001725132

---

# Command: bloggerd log-throttle

## Syntax
```
[no] bloggerd log-throttle [ min-rollover <min-rollover> max-rollover-per-minute <max-rollover-per-minute> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bloggerd | Blogger commands |
| log-throttle | Enable Log Dump Throttling for all NxOS services |
| min-rollover | (Optional) Number of minimum buffer rollovers before starting to throttle. Default: 5 |
| min-rollover | (Optional) Enter the mininum number of roll-overs before throttleing log-dump. Default: 5 |
| max-rollover-per-minute | (Optional) Maximum allowed buffer rollovers per minute. Default: 1 |
| max-rollover-per-minute | (Optional) Enter the maximum allowed roll-overs per minute before throttling. Default: 1 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3952426806

---

# Command: bloggerd log-transfer

## Syntax
```
[no] bloggerd log-transfer
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| bloggerd | Blogger commands |
| log-transfer | Configure log transfer |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2728184746

---

# Command: bloggerd log-transfer

## Syntax
```
bloggerd log-transfer { <ip-addr> <path> &#124; logflash }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| log-transfer | Configure log transfer |
| ip-addr | IP addr of logging server |
| path | Path in tftp server to store logs. Eg: logOutput |
| logflash | Move all log-files to logflash |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp4285270457

---

# Command: bloggerd parse log-buffer file

## Syntax
```
bloggerd parse log-buffer { file &#124; directory } <uri0> [ dsf_table <uri1> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| parse | Parse a file |
| log-buffer | Parse buffer log file |
| directory | Enter path of directory |
| file | Enter file name. Please unzip file before parsing! |
| uri0 | Linux path to file/directory (Eg: /bootflash/abc) |
| dsf_table | (Optional) Enter dsf table file name. |
| uri1 | (Optional) Linux path to file/directory (Eg: /bootflash/abc) |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2236355635

---

# Command: bloggerd parse log-buffer file sap

## Syntax
```
bloggerd parse log-buffer file <uri0> sap <sap-num>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| parse | Parse a file |
| log-buffer | Parse buffer log file |
| file | Enter file name. Please unzip file before parsing! |
| uri0 | Linux path to file (Eg: /bootflash/abc) |
| sap | SAP of the application which should parse the file |
| sap-num | Enter a valid SAP. Enter 0 for ALL SAPs in this VDC |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2700581401

---

# Command: bloggerd parse pss file

## Syntax
```
bloggerd parse pss file <uri0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| bloggerd | Blogger commands |
| parse | Parse a file |
| pss | Parse a dumped PSS File |
| file | Enter file name (without pss extensions). Please unzip file before parsing! |
| uri0 | Linux path to file/directory (Eg: /bootflash/abc) |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp3453224508

---

# Command: bmp-activate-server

## Syntax
```
bmp-activate-server <server-number> &#124; { no &#124; default } bmp-activate-server <server-number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| bmp-activate-server | Activate BMP monitoring for the peer |
| server-number | Server Id |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp4161033680

---

# Command: bmp-server

## Syntax
```
[no] bmp-server <server-number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bmp-server | Configure bmp-server |
| server-number | server number value |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp6561882450

---

# Command: boot-install nxos

## Syntax
```
{ boot-install nxos <uri0> &#124; no boot-install nxos [ <uri0> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot-install | Configure boot variables |
| nxos | Configure NXOS image |
| uri0 | Enter NXOS image uri |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1095273851

---

# Command: boot-order

## Syntax
```
boot-order <new_id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| boot-order | The order at which a vdc will boot up. VDCs at the same level will be started parallely |
| new_id | The order at which a vdc will boot up. VDCs at the same level will be started parallely |

**Command Mode:** /exec/configure/vdc

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1582617396

---

# Command: boot

## Syntax
```
{ boot <s0> <uri0> [ module [ <module> ] ] &#124; no boot <s0> [ <uri0> [ module [ <module> ] ] ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| s0 | use [show boot variables] for list of keywords |
| uri0 | Enter module image uri |
| module | (Optional) Enter module number for the image |
| module | (Optional) Enter module number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1989376040

---

# Command: boot aci

## Syntax
```
{ boot aci <uri0> &#124; no boot aci [ <uri0> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| aci | Configure ACI image |
| uri0 | Enter ACI image uri |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3837418472

---

# Command: boot auto-copy

## Syntax
```
[no] boot auto-copy
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| boot | Configure boot variables |
| auto-copy | Turns on/off autocopy of bootvar images |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp4242396838

---

# Command: boot kickstart

## Syntax
```
{ boot kickstart <uri0> &#124; no boot kickstart [ <uri0> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| kickstart | Configure kickstart image |
| uri0 | Enter Kickstart image uri |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp2462384818

---

# Command: boot mode docker_cluster

## Syntax
```
[no] boot mode docker_cluster [ dhcp <option> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| boot | Configure boot mode |
| mode | boot mode |
| docker_cluster | Turns on/off docker_cluster mode |
| dhcp | (Optional) Custom DHCP option |
| option | (Optional) Option, default is 250 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1524836970

---

# Command: boot mode docker_standalone

## Syntax
```
[no] boot mode docker_standalone
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| boot | Configure boot mode |
| mode | boot mode |
| docker_standalone | Turns on/off docker_standalone mode (for internal use only) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1068549749

---

# Command: boot mode lxc

## Syntax
```
[no] boot mode lxc
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| boot | Configure boot mode |
| mode | boot mode |
| lxc | Turns on/off lxc mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp2630463377

---

# Command: boot nxos

## Syntax
```
{ boot nxos <uri0> &#124; no boot nxos [ <uri0> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| nxos | Configure NXOS image |
| uri0 | Enter nxos image uri |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3699241335

---

# Command: boot nxos sup-1

## Syntax
```
{ boot nxos <uri0> sup-1 &#124; no boot nxos <uri0> sup-1 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| nxos | Configure NXOS image |
| uri0 | Enter nxos image uri |
| sup-1 | Enter sup-1 to configure the 1st sup |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3325509639

---

# Command: boot nxos sup-1 sup-2

## Syntax
```
{ boot nxos <uri0> sup-1 sup-2 &#124; no boot nxos <uri0> sup-1 sup-2 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| nxos | Configure NXOS image |
| uri0 | Enter nxos image uri |
| sup-1 | Enter sup-1 to configure the 1st sup |
| sup-2 | Enter sup-2 to configure the 2nd sup |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1026312515

---

# Command: boot nxos sup-2

## Syntax
```
{ boot nxos <uri0> sup-2 &#124; no boot nxos <uri0> sup-2 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| nxos | Configure NXOS image |
| uri0 | Enter nxos image uri |
| sup-2 | Enter sup-2 to configure the 2nd sup |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp2956530346

---

# Command: boot order bootflash

## Syntax
```
{ boot order bootflash [ pxe ] &#124; no boot order bootflash [ pxe ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| order | Configure loader fallback order |
| bootflash | Boot from Bootflash |
| pxe | (Optional) Pxe Boot |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1159892171

---

# Command: boot order pxe

## Syntax
```
{ boot order pxe [ bootflash ] &#124; no boot order pxe [ bootflash ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| order | Configure loader fallback order |
| pxe | Pxe Boot |
| bootflash | (Optional) Boot from Bootflash |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp2978389810

---

# Command: boot poap enable

## Syntax
```
{ boot poap enable &#124; no boot poap enable }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| poap | feature poap |
| enable | Enable Perpetual POAP making POAP kick in on reload even with startup-config |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3268024771

---

# Command: boot system

## Syntax
```
{ boot system <uri0> &#124; no boot system [ <uri0> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| boot | Configure boot variables |
| system | Configure system image |
| uri0 | Enter system image uri |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp1813128782

---

# Command: bootmode boot

## Syntax
```
[no] bootmode boot
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| boot | boot in boot mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3533507090

---

# Command: bootmode extruntime

## Syntax
```
[no] bootmode extruntime
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| extruntime | boot in runtime mode with extended diags |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, boot, B-commands
**Command ID:** wp6314946580

---

# Command: bootmode hitless

## Syntax
```
[no] bootmode hitless
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| hitless | boot in hitless mode |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp3521352810

---

# Command: bootmode module

## Syntax
```
[no] bootmode module <module> { boot &#124; extruntime &#124; hitless &#124; netboot &#124; nodiagruntime &#124; runtime }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| module | set bootmode for a given module in the switch |
| module | please enter module number |
| boot | boot in boot mode |
| extruntime | boot in runtime mode with extended diags |
| hitless | boot in hitless mode |
| netboot | boot using boot netboot in runtime mode |
| nodiagruntime | boot in runtime mode without running any diags |
| runtime | boot in runtime mode with normal diags |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, boot, B-commands
**Command ID:** wp5883168790

---

# Command: bootmode nodiagruntime

## Syntax
```
[no] bootmode nodiagruntime
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| nodiagruntime | boot in runtime mode without running any diags |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, boot, B-commands
**Command ID:** wp4027973245

---

# Command: bootmode runtime

## Syntax
```
[no] bootmode runtime
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| bootmode | set bootmode for all modules in the switch |
| runtime | boot in runtime mode with normal diags |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, system, boot, B-commands
**Command ID:** wp1623063492

---

# Command: buffer-boost

## Syntax
```
[no] buffer-boost
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| buffer-boost | Enable extra buffers for this interface |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-non-member /exec/configure/if-port-channel

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp2975832716

---

# Command: buffer-delete

## Syntax
```
buffer-delete { <id-range> &#124; <id> &#124; all }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| buffer-delete | delete buffered command(s) |
| id-range | Range(whole-number) of command id(s) to be deleted from switch-profile buffer |
| id | Exact command id (x.x.x format) to be deleted from switch-profile buffer |
| all | delete all buffered commands |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1500779794

---

# Command: buffer-move

## Syntax
```
buffer-move <fromid> <toid>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| buffer-move | move buffered command(s) |
| fromid | Command id of command(s) to be moved in switch-profile buffer |
| toid | New command id to be assigned in switch-profile buffer |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1668022441

---

# Command: burst-detect enable

## Syntax
```
[no] burst-detect enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| burst-detect | Specify OOBST burst-detect thresholds for the class |
| enable | enable |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1774110782

---

# Command: burst-detect rise-threshold bytes fall-threshold bytes2

## Syntax
```
[no] burst-detect rise-threshold <value-in-bytes> bytes fall-threshold <value-in-bytes> bytes2
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| burst-detect | Specify OOBST burst-detect thresholds for the class |
| rise-threshold | Threshold bytes(queue depth) to start monitoring burst |
| bytes | bytes |
| fall-threshold | Threshold bytes(queue depth) to stop monitoring burst |
| bytes2 | bytes2 |

**Command Mode:** /exec/configure/policy-map/type/queuing/class

**Source:** b_N9K_Config_Commands_93x_chapter_010.html
**Tags:** config-mode, B-commands
**Command ID:** wp1394009638

---

