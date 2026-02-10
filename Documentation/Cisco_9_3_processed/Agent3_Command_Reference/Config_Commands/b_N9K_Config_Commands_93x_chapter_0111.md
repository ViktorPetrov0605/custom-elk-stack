# Chapter: G Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_0111.html
**Type:** Configuration Commands  
**Chapter:** Group-111 Commands  
**Total Commands:** 37

## Command List

- `generate type7_encrypted_secret`
- `getnext`
- `global-block`
- `global-block`
- `global ingress-replication protocol bgp`
- `global mcast-group L2`
- `global suppress-arp`
- `graceful-restart-helper`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart`
- `graceful-restart grace-period`
- `graceful-restart grace-period`
- `graceful-restart helper-disable`
- `graceful-restart helper-disable`
- `graceful-restart restart-time`
- `graceful-restart stalepath-time`
- `graceful-restart t3 manual`
- `graceful-restart t3 manual`
- `graceful-restart t3 manual`
- `graceful-shutdown activate`
- `graceful-shutdown activate`
- `graceful-shutdown aware`
- `graceful consistency-check`
- `grep`
- `grep`
- `grep`
- `group drop-events`
- `group latency-events`
- `guestshell`
- `gunzip`
- `gzip`

---

## Detailed Command Reference

# Command: generate type7_encrypted_secret

## Syntax
```
generate type7_encrypted_secret
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| generate | generate |
| type7_encrypted_secret | Type 7 Encrypted Secret |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3927946880

---

# Command: getnext

## Syntax
```
&#124; getnext
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| getnext | return next instance instead of specified one, or first instance if none specified (if supported by feature) |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2715324004

---

# Command: global-block

## Syntax
```
{ { global-block <min-srgb-label> <max-srgb-label> } &#124; { no global-block } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| global-block | Specify global block range for Segment Routing bindings |
| min-srgb-label | Minimum label value |
| max-srgb-label | Maximum label value |

**Command Mode:** /exec/configure/config-sr-mpls

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2790224363

---

# Command: global-block

## Syntax
```
{ { global-block <min-srgb-label> <max-srgb-label> } &#124; { no global-block } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| global-block | Specify global block range for Segment Routing bindings |
| min-srgb-label | Minimum label value |
| max-srgb-label | Maximum label value |

**Command Mode:** /exec/configure/config-sr

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2527451080

---

# Command: global ingress-replication protocol bgp

## Syntax
```
[no] global ingress-replication protocol bgp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| global | Global configurations for nve, inherited by VNIs |
| ingress-replication | Configure ingress replication |
| protocol | Control protocol to use |
| bgp | Border Gateway Protocol |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, routing, G-commands
**Command ID:** wp4050460710

---

# Command: global mcast-group L2

## Syntax
```
global mcast-group { <maddr> } { L2 &#124; L3 } &#124; no global mcast-group { L2 &#124; L3 }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| global | Global configurations for nve, inherited by VNIs |
| mcast-group | NVE Multicast Group |
| L2 | Global mcast-group <arg> for L2 VNIs |
| L3 | Global mcast-group <arg> for L3 VNIs |
| maddr | Multicast IP Prefix |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1001511798

---

# Command: global suppress-arp

## Syntax
```
[no] global suppress-arp
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| global | Global configurations for nve, inherited by VNIs |
| suppress-arp | Enable ARP suppression |

**Command Mode:** /exec/configure/if-nve

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2488609635

---

# Command: graceful-restart-helper

## Syntax
```
[no] graceful-restart-helper
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart-helper | Configure Graceful Restart Helper mode functionality |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1377897653

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart [ planned-only ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| planned-only | (Optional) Enable graceful restart only for a planned restart |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2991182341

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3116075942

---

# Command: graceful-restart

## Syntax
```
{ { [ no ] [ eigrp ] graceful-restart } &#124; { [ no ] nsf } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| eigrp | (Optional) EIGRP router configuration commands |
| graceful-restart | Peer resync without adjancency reset |
| nsf | Non-stop forwarding |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp7117354610

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart [ planned-only ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| planned-only | (Optional) Enable graceful restart only for a planned restart |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2166096744

---

# Command: graceful-restart

## Syntax
```
graceful-restart [ timers { forwarding-holding <fwdg-holdtime> &#124; max-recovery <recovery-time> &#124; neighbor-liveness <peer-liveness-time>
 } ] &#124; no graceful-restart [ timers { forwarding-holding &#124; max-recovery &#124; neighbor-liveness } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Configure LDP Graceful Restart |
| timers | (Optional) Configure Graceful Restart timers |
| forwarding-holding | (Optional) Forwarding State Holding time |
| fwdg-holdtime | (Optional) seconds |
| max-recovery | (Optional) Max-Recovery time |
| recovery-time | (Optional) seconds |
| neighbor-liveness | (Optional) Neighbor-Liveness time |
| peer-liveness-time | (Optional) seconds |

**Command Mode:** /exec/configure/ldp

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1686729929

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure Graceful Restart functionality |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp4589143540

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3347832122

---

# Command: graceful-restart

## Syntax
```
[no] graceful-restart
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2469265439

---

# Command: graceful-restart grace-period

## Syntax
```
[no] graceful-restart grace-period <grace-period>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| grace-period | Configure maximum interval to restart gracefully |
| grace-period | Grace period in seconds |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1210789029

---

# Command: graceful-restart grace-period

## Syntax
```
[no] graceful-restart grace-period <grace-period>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| grace-period | Configure maximum interval to restart gracefully |
| grace-period | Grace period in seconds |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3555359630

---

# Command: graceful-restart helper-disable

## Syntax
```
[no] graceful-restart helper-disable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| helper-disable | Disable helper mode |

**Command Mode:** /exec/configure/router-ospf3 /exec/configure/router-ospf3/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp5557022270

---

# Command: graceful-restart helper-disable

## Syntax
```
[no] graceful-restart helper-disable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-restart | Configure graceful restart |
| helper-disable | Disable helper mode |

**Command Mode:** /exec/configure/router-ospf /exec/configure/router-ospf/vrf

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3164781772

---

# Command: graceful-restart restart-time

## Syntax
```
graceful-restart restart-time <restart-time> &#124; no graceful-restart restart-time [ <restart-time> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Configure Graceful Restart functionality |
| restart-time | Maximum time for restart advertised to peers |
| restart-time | Restart time (seconds) |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, system, G-commands
**Command ID:** wp2546903200

---

# Command: graceful-restart stalepath-time

## Syntax
```
graceful-restart stalepath-time <stalepath-time> &#124; no graceful-restart stalepath-time [ <stalepath-time> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Configure Graceful Restart functionality |
| stalepath-time | Maximum time to keep a restarting peer's stale routes |
| stalepath-time | Stalepath time (seconds) |

**Command Mode:** /exec/configure/router-bgp/vrf-cmds

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, system, G-commands
**Command ID:** wp2279741485

---

# Command: graceful-restart t3 manual

## Syntax
```
graceful-restart t3 manual <sec> &#124; no graceful-restart t3 manual [ <sec> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |
| t3 | Set the T3 (RFC 3847) graceful restart timer |
| manual | Change manually T3 default value |
| sec | Specify T3 value (secs) |

**Command Mode:** /exec/configure/l2mp-isis/l2mp-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2954604096

---

# Command: graceful-restart t3 manual

## Syntax
```
graceful-restart t3 manual <sec> &#124; no graceful-restart t3 manual [ <sec> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |
| t3 | Set the T3 (RFC 3847) graceful restart timer |
| manual | Change manually T3 default value |
| sec | Specify T3 value (secs) |

**Command Mode:** /exec/configure/router-isis/router-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3872211334

---

# Command: graceful-restart t3 manual

## Syntax
```
graceful-restart t3 manual <sec> &#124; no graceful-restart t3 manual [ <sec> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| graceful-restart | Enable graceful restart for IS-IS |
| t3 | Set the T3 (RFC 3847) graceful restart timer |
| manual | Change manually T3 default value |
| sec | Specify T3 value (secs) |

**Command Mode:** /exec/configure/otv-isis/otv-isis-vrf-common

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2797842710

---

# Command: graceful-shutdown activate

## Syntax
```
[ no &#124; default ] graceful-shutdown activate [ route-map <rmap-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| default | (Optional) Inherit values from a peer template |
| graceful-shutdown | Graceful-shutdown for this neighbor |
| activate | Send graceful-shutdown community |
| route-map | (Optional) Apply route-map to modify attributes for outbound |
| rmap-name | (Optional) Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1733906880

---

# Command: graceful-shutdown activate

## Syntax
```
[no] graceful-shutdown activate [ route-map <rmap-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-shutdown | Graceful-shutdown for BGP protocol |
| activate | Send graceful-shutdown community on all routes |
| route-map | (Optional) Apply route-map to modify attributes for outbound |
| rmap-name | (Optional) Route-map name |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2687425517

---

# Command: graceful-shutdown aware

## Syntax
```
[no] graceful-shutdown aware
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful-shutdown | Graceful-shutdown for BGP protocol |
| aware | Lower preference of routes carrying graceful-shutdown community |

**Command Mode:** /exec/configure/router-bgp

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2196627418

---

# Command: graceful consistency-check

## Syntax
```
[no] graceful consistency-check
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| graceful | Enable graceful features |
| consistency-check | Enable graceful type-1 consistency check |

**Command Mode:** /exec/configure/vpc-domain

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3055526697

---

# Command: grep

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| grep | Grep |
| egrep | Egrep |
| -c | (Optional) Print a total count of matching lines only |
| -i | (Optional) Ignore case difference when comparing strings |
| -n | (Optional) Print each match preceded by its line number |
| -v | (Optional) Print only lines that contain no matches for <expr> |
| -w | (Optional) Print only lines where the match is a complete word |
| -x | (Optional) Print only lines where the match is a whole line |
| ctx | (Optional) Print <num> lines of context on each side of every match |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1169663175

---

# Command: grep

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| grep | Grep - print lines matching a pattern |
| egrep | Egrep - print lines matching a pattern |
| count | (Optional) Print a total count of matching lines only |
| ignore-case | (Optional) Ignore case difference when comparing strings |
| line-number | (Optional) Print each match preceded by its line number |
| invert-match | (Optional) Print only lines that contain no matches for <expr> |
| word-exp | (Optional) Print only lines where the match is a complete word |
| line-exp | (Optional) Print only lines where the match is a whole line |
| ctx | (Optional) Print <num> lines of context on each side of every match |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp3210133878

---

# Command: grep

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| grep | Grep - print lines matching a pattern |
| egrep | Egrep - print lines matching a pattern |
| -c | (Optional) Print a total count of matching lines only |
| -i | (Optional) Ignore case difference when comparing strings |
| -n | (Optional) Print each match preceded by its line number |
| -v | (Optional) Print only lines that contain no matches for <expr> |
| -w | (Optional) Print only lines where the match is a complete word |
| -x | (Optional) Print only lines where the match is a whole line |
| ctx | (Optional) Print <num> lines of context on each side of every match |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2879651210

---

# Command: group drop-events

## Syntax
```
[no] group drop-events
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| group | Group for which the events need to be set |
| drop-events | Set events for drops |

**Command Mode:** /exec/configure/config-fte-event

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp1063711572

---

# Command: group latency-events

## Syntax
```
[no] group latency-events
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| group | Group for which the events need to be set |
| latency-events | Set events for latency events |

**Command Mode:** /exec/configure/config-fte-event

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2521027024

---

# Command: guestshell

## Syntax
```
guestshell [ { enable [ { package <enable_uri> } ] } &#124; { upgrade [ { package <upgrade_uri> } ] } &#124; { export { rootfs package
 <export_uri> } } &#124; { disable } &#124; { destroy } &#124; { reboot } &#124; <sync_cmd_name> &#124; { resize { rootfs <gsh_rootfs> &#124; cpu <gsh_cpu>
 &#124; memory <gsh_memory> } } &#124; { run { <cmd_args> } } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| guestshell | Request a guest shell |
| enable | (Optional) Enable the guest shell service |
| upgrade | (Optional) Upgrade the guest shell service package to a different version |
| export | (Optional) Export the guest shell |
| export_uri | (Optional) Destination file or directory path |
| disable | (Optional) Disable the guest shell service package |
| destroy | (Optional) Disable and uninstall the guest shell service package |
| sync_cmd_name | (Optional) Synchronize the contents of the guest shell to standby supervisor |
| reboot | (Optional) Deactivate and reactivate the guest shell service |
| resize | (Optional) Resize the existing/default guest shell parameters |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, G-commands
**Command ID:** wp2181788681

---

# Command: gunzip

## Syntax
```
gunzip <uri0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| gunzip | Uncompresses LZ77 coded files |
| uri0 | Enter filename (filename must have .gz extension) |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, network, G-commands
**Command ID:** wp3012161180

---

# Command: gzip

## Syntax
```
gzip <uri0>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| gzip | Compresses file using LZ77 coding |
| uri0 | Enter filename |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_0111.html
**Tags:** config-mode, network, G-commands
**Command ID:** wp3684486239

---

