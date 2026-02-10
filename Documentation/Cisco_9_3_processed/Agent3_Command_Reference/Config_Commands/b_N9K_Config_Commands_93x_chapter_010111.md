# Chapter: W Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010111.html
**Type:** Configuration Commands  
**Chapter:** Group-10111 Commands  
**Total Commands:** 22

## Command List

- `wait-igp-convergence`
- `watch`
- `watch service action apply-acl`
- `watchlist`
- `watchlist`
- `wc`
- `wedge bmc ip-addr`
- `weight`
- `weight`
- `weight`
- `weight`
- `where`
- `where detail`
- `window-size`
- `wred-queue qos-group-map queue-only`
- `write erase`
- `write erase boot`
- `write erase debug`
- `write erase poap`
- `wrr-queue qos-group-map`
- `wrr unicast-bandwidth`
- `wwn vsan vsan-wwn`

---

## Detailed Command Reference

# Command: wait-igp-convergence

## Syntax
```
[no] wait-igp-convergence
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| wait-igp-convergence | Delay initial bestpath until redistributed IGPs have converged |

**Command Mode:** /exec/configure/router-bgp/router-bgp-af-ipv4 /exec/configure/router-bgp/router-bgp-vrf-af-ipv4 /exec/configure/router-bgp/router-bgp-af-ipv6
 /exec/configure/router-bgp/router-bgp-vrf-af-ipv6

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp1703116164

---

# Command: watch

## Syntax
```
watch [ differences ] [ interval <time> ] <watch_cmd>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| watch | execute a program periodically |
| differences | (Optional) highlight the differences |
| interval | (Optional) watch interval |
| time | (Optional) interval in seconds |
| watch_cmd | enter the command you want to watch |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp2712107902

---

# Command: watch service action apply-acl

## Syntax
```
[no] watch service <service-name> action apply-acl <acl-name> &#124; no watch service
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| watch | Watch a pod/service |
| service | The pod or service to watch |
| service-name | Name of the service/pod to watch |
| action | Action to be applied |
| apply-acl | Change ACL config |
| acl-name | Name of the acl to apply |

**Command Mode:** /exec/configure/kubernetes

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, security, W-commands
**Command ID:** wp3083382462

---

# Command: watchlist

## Syntax
```
[no] watchlist <watchlistname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| watchlist | Specify INT watchlist to use |
| watchlistname | Name of watchlist |

**Command Mode:** /exec/configure/config-int-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp2871338223

---

# Command: watchlist

## Syntax
```
[no] watchlist <watchlistname>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| watchlist | Specify POSTCARD watchlist to use |
| watchlistname | Name of watchlist |

**Command Mode:** /exec/configure/config-postcard-monitor

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp1609899270

---

# Command: wc

## Syntax
```
&#124; wc [ -c &#124; -l &#124; -w ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| wc | Count words, lines, characters |
| -c | (Optional) Output character count |
| -l | (Optional) Output line count |
| -w | (Optional) Output word count |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp3892199700

---

# Command: wedge bmc ip-addr

## Syntax
```
[no] wedge bmc ip-addr { <ip> &#124; <ip_v6> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| wedge | Configure wedge Board Management controller ip address |
| bmc | Board Management Controller ip address |
| ip-addr | BMC ip address |
| ip | ip adddress |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, network, W-commands
**Command ID:** wp7359336940

---

# Command: weight

## Syntax
```
{ weight <weight> } &#124; { { no &#124; default } weight [ <weight> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| weight | Set default weight for routes from this neighbor |
| weight | Default weight |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-mdt

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp2494328860

---

# Command: weight

## Syntax
```
[no] weight <weight-value>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| weight | weight for traffic distribution |
| weight-value | weight value |

**Command Mode:** /exec/configure/itd-dg-node

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp4044935457

---

# Command: weight

## Syntax
```
{ weight <weight> } &#124; { { no &#124; default } weight [ <weight> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| weight | Set default weight for routes from this neighbor |
| weight | Default weight |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp5906534000

---

# Command: weight

## Syntax
```
weight <weight-value> &#124; no weight
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| weight | Configure weight of node for traffic distribution |
| weight-value | weight value |

**Command Mode:** /exec/configure/plb-dg-node

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp6552830850

---

# Command: where

## Syntax
```
where
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| where | shows the cli context you are in |

**Command Mode:** /global

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp2739386886

---

# Command: where detail

## Syntax
```
where detail
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| where | shows the cli context you are in |
| detail | shows each entry on separate line |

**Command Mode:** /global

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp6741987590

---

# Command: window-size

## Syntax
```
[no] window-size <size>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| window-size | Configure Window size |
| size | window size value |

**Command Mode:** /exec/configure/macsec-policy

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp4919548750

---

# Command: wred-queue qos-group-map queue-only

## Syntax
```
[no] wred-queue qos-group-map queue-only { <qid> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| wred-queue | Enable queue based ECN marking for specific qos-group |
| queue-only | Enable queue based ECN marking |
| qos-group-map | Qid value |
| qid | Provide qos-group value |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, qos, W-commands
**Command ID:** wp2311219190

---

# Command: write erase

## Syntax
```
write erase
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| write | Write current configuration |
| erase | Destroys the configuration on persistent media |

**Command Mode:** /exec

## Description
You can erase the configuration on your device to return to the configuration defaults. In this context, configuration refers to the startup configuration as displayed by the show startup command. No other internal application or process states are cleared. To remove all application persistency files such as
 patch rpms, third party rpms, and application configuration in the /etc directory other than configuration, use the install reset command.

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp2863203612

---

# Command: write erase boot

## Syntax
```
write erase boot
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| write | Write current configuration |
| erase | Destroys the configuration on persistent media |
| boot | Destroys boot configuration on persistent media |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, boot, W-commands
**Command ID:** wp2750850363

---

# Command: write erase debug

## Syntax
```
write erase debug
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| write | Write current configuration |
| erase | Destroys the configuration on persistent media |
| debug | Destroys debug configuration on persistent media |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp3298510545

---

# Command: write erase poap

## Syntax
```
write erase poap
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| write | Write current configuration |
| erase | Destroys the configuration on persistent media |
| poap | Removes System-wide POAP disable configuration on persistent media |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp1758868959

---

# Command: wrr-queue qos-group-map

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| wrr-queue | Map traffic priority (QG) values to L3 Multicast Queues |
| qos-group-map | Qid value |
| qid | Provide qid value |
| cos | Provide qos-group-map value |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, qos, W-commands
**Command ID:** wp1247768314

---

# Command: wrr unicast-bandwidth

## Syntax
```
[no] wrr unicast-bandwidth <bw>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate the command |
| wrr | Configure Unicast Traffic Bandwidth Percentage |
| unicast-bandwidth | Specify rate as percentage of interface data-rate |
| bw | Value in percentage (Default is set to 50) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, qos, W-commands
**Command ID:** wp1855265081

---

# Command: wwn vsan vsan-wwn

## Syntax
```
wwn vsan <i0> vsan-wwn <wwn1> &#124; no
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| vsan | <i0> |
| no | Negate a command or set its defaults |
| wwn | Set secondary base MAC addr and range for additional WWNs |
| i0 | Enter the vsan id |
| vsan-wwn | vsan-wwn for vsan in interop mode 4 |
| wwn1 | Enter wwn for vsan in interop mode 4 |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010111.html
**Tags:** config-mode, W-commands
**Command ID:** wp1396750320

---

