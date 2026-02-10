# Chapter: U Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_010101.html
**Type:** Configuration Commands  
**Chapter:** Group-10101 Commands  
**Total Commands:** 57

## Command List

- `udf`
- `udf netflow-rtp`
- `udld aggressive`
- `udld aggressive`
- `udld aggressive`
- `udld aggressive`
- `udld continue-on-err`
- `udld disable`
- `udld disable`
- `udld enable`
- `udld enable`
- `udld message-time`
- `udld reset`
- `udp-echo`
- `udp-jitter`
- `undebug all`
- `undebug l2rib`
- `uniq`
- `unmount`
- `unmount slot0`
- `unsuppress-map`
- `untagged cos`
- `update-source`
- `update-source`
- `update license`
- `update license`
- `urib debugs-dump-to-file`
- `use-chunking size`
- `use-compression gzip`
- `use-nodeid`
- `use-retry size`
- `use-vrf`
- `use-vrf`
- `use-vrf`
- `use-vrf`
- `user-jid password`
- `user max-logins`
- `user max-logins`
- `username`
- `username`
- `username`
- `username`
- `username`
- `username keypair export`
- `username keypair generate`
- `username keypair import`
- `username passphrase`
- `username passphrase`
- `username password`
- `username ssh-cert-dn dsa`
- `username sshkey`
- `userpassphrase`
- `userpassphrase`
- `userpassphrase`
- `userpassphrase min`
- `userpassphrase min`
- `userprofile trustedCert CRLLookup user-switch-bind user-certdn-match user-pubkey-match attribute-name search-filter base-DN`

---

## Detailed Command Reference

# Command: udf

## Syntax
```
udf <udf_name> { packet-start &#124; { header { outer &#124; inner } { l3 &#124; l4 } } } <offset> <length> &#124; no udf <udf_name> [ { packet-start
 &#124; { header { outer &#124; inner } { l3 &#124; l4 } } } <offset> <length> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| udf | Define the User Defined Field (UDF) |
| udf_name | Name of the UDF to configure |
| packet-start | Offset base from packet-start |
| header | Offset base configuration |
| outer | Offset base: from outer header |
| inner | Offset base: from inner header |
| l3 | Offset base: from l3 header |
| l4 | Offset base: from l4 header |
| offset | Enter Offset in bytes for UDF (from offset base) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp4063842677

---

# Command: udf netflow-rtp

## Syntax
```
udf <udf_name> netflow-rtp &#124; no udf <udf_name> [ netflow-rtp ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate the command |
| udf | Define the User Defined Field (UDF) |
| udf_name | Name of the UDF to configure |
| netflow-rtp | Configure netflow rtp udf |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1752029110

---

# Command: udld aggressive

## Syntax
```
udld aggressive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| udld | UDLD protocol |
| aggressive | Enable UDLD aggressive mode for interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2022230136

---

# Command: udld aggressive

## Syntax
```
udld aggressive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| udld | UDLD protocol |
| aggressive | Enable UDLD aggressive mode on all fiber optic ports |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1422684376

---

# Command: udld aggressive

## Syntax
```
[no] udld aggressive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| udld | UDLD protocol |
| aggressive | Enable UDLD aggressive mode on all fiber optic ports |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1958474590

---

# Command: udld aggressive

## Syntax
```
[no] udld aggressive
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| udld | UDLD protocol |
| aggressive | Enable UDLD aggressive mode for interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp4269000781

---

# Command: udld continue-on-err

## Syntax
```
[no] udld continue-on-err
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| udld | UDLD protocol |
| continue-on-err | Force UDLD continue without disabling the port |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2897703210

---

# Command: udld disable

## Syntax
```
udld disable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| udld | UDLD protocol |
| disable | Disable UDLD for fiber interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1496641138

---

# Command: udld disable

## Syntax
```
[no] udld disable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| udld | UDLD protocol |
| disable | Disable UDLD for fiber interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1062915610

---

# Command: udld enable

## Syntax
```
[no] udld enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| udld | UDLD protocol |
| enable | Enable UDLD for non-fiber interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp4264638625

---

# Command: udld enable

## Syntax
```
udld enable
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| udld | UDLD protocol |
| enable | Enable UDLD for non-fiber interface(s) |

**Command Mode:** /exec/configure/if-ethernet-all /exec/configure/if-eth-base

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3646376930

---

# Command: udld message-time

## Syntax
```
udld message-time <i0> &#124; no udld message-time
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| udld | UDLD protocol |
| message-time | Setting the time in seconds between UDLD probe messages |
| i0 | Enter the message timer value [default = 15] |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, system, U-commands
**Command ID:** wp2918180923

---

# Command: udld reset

## Syntax
```
udld reset
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| udld | UDLD protocol |
| reset | Reset all ports shut down by UDLD |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3166792368

---

# Command: udp-echo

## Syntax
```
(Optional)
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) |
| control | (Optional) enable |
| source-ip-address | (Optional) <source-port-number> |
| udp-echo | UDP Echo Operation |
| hostname | Destination hostname, broadcast disallowed |
| ip-address | Destination IP address, broadcast disallowed |
| port | Port Number (Recommended port range between 1025-65534) |
| enable | (Optional) Enable control packets exchange (default) |
| disable | (Optional) Disable control packets exchange |
| source-ip | (Optional) Source address |

**Command Mode:** /exec/configure/ip-sla

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, network, U-commands
**Command ID:** wp1274940959

---

# Command: udp-jitter

## Syntax
```
(Optional)
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) |
| codec | (Optional) g711alaw |
| codec-numpackets | (Optional) codec-size |
| source-port | (Optional) interval |
| codec-numpack | (Optional) <codec-bytes> |
| source-ip-hostname | (Optional) <source-ip-address> |
| udp-jitter | UDP Jitter Operation |
| hostname | Destination hostname, broadcast disallowed |
| ip-address | Destination IP address, broadcast disallowed |
| dest-port | Port Number (Recommended port range between 1025-65534) |

**Command Mode:** /exec/configure/ip-sla

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, network, U-commands
**Command ID:** wp1014348935

---

# Command: undebug all

## Syntax
```
undebug all
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| undebug | Disable Debugging functions (See also debug) |
| all | Disable all debugging |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp6460335400

---

# Command: undebug l2rib

## Syntax
```
undebug l2rib
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| undebug | Disable Debugging functions (See also debug) |
| l2rib | L2RIB debug commands |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2114374482

---

# Command: uniq

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| uniq | Discard all but one of successive identical lines |
| -c | (Optional) prefix lines by the number of occurrences |
| -d | (Optional) only print duplicate lines |
| -f | (Optional) avoid comparing the first N fields |
| -s | (Optional) avoid comparing the first N characters |
| -u | (Optional) only print unique lines |
| -w | (Optional) compare no more than N characters in lines |
| -i | (Optional) ignore differences in case when comparing |
| nb-of-fields | (Optional) number of initial fields to ignore |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2902881400

---

# Command: unmount

## Syntax
```
unmount { usb1: &#124; usb2: }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| unmount | unmount expansion flash or USB storage |
| usb1: | Unmount USB drive in port 1 |
| usb2: | Unmount USB drive in port 2 |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp7671403200

---

# Command: unmount slot0

## Syntax
```
unmount slot0:
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| unmount | unmount expansion flash or USB storage |
| slot0: | Unmount expansion flash |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3982791394

---

# Command: unsuppress-map

## Syntax
```
unsuppress-map <unsupp-rmap-name> &#124; { no &#124; default } unsuppress-map [ <unsupp-rmap-name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| unsuppress-map | Route-map to selectively unsuppress suppressed routes |
| unsupp-rmap-name | Route-map name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv4
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-vpnv6 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv4-label
 /exec/configure/router-bgp/router-bgp-neighbor/router-bgp-neighbor-af-ipv6-label

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3030837826

---

# Command: untagged cos

## Syntax
```
untagged cos <ucos-value> &#124; no untagged cos
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| untagged | default to use for untagged packets on interface |
| cos | IEEE 802.1Q class of service for QoS classification |
| ucos-value | COS value |

**Command Mode:** /exec/configure/if-set-qos

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2490520408

---

# Command: update-source

## Syntax
```
update-source <interface> &#124; no update-source
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| update-source | Specify source of BMP session and messages |
| interface | Interface name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-bmp-server

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3709824472

---

# Command: update-source

## Syntax
```
update-source <interface> &#124; { no &#124; default } update-source [ <interface> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| default | Inherit values from a peer template |
| update-source | Specify source of BGP session and updates |
| interface | Interface name |

**Command Mode:** /exec/configure/router-bgp/router-bgp-neighbor-sess

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3589348698

---

# Command: update license

## Syntax
```
update license <uri0> { <license-file> [ force ] &#124; <s0> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| update | Update license |
| license | Update a license file |
| uri0 | Specify URL for the new license file |
| license-file | License file to be updated |
| force | (Optional) Force update license (don't prompt) |
| s0 | License file to be updated |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp4815906890

---

# Command: update license

## Syntax
```
update license <uri0> { <license-file> [ force ] &#124; <s0> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| update | Update license |
| license | Update a license file |
| uri0 | Specify URL for the new license file |
| license-file | License file to be updated |
| force | (Optional) Force update license (don't prompt) |
| s0 | License file to be updated |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2539164745

---

# Command: urib debugs-dump-to-file

## Syntax
```
urib debugs-dump-to-file
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| urib | Unicast Routing Information Base |
| debugs-dump-to-file | Dump all urib debugs to a file |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3302096913

---

# Command: use-chunking size

## Syntax
```
use-chunking size <kbytes> &#124; no use-chunking
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| use-chunking | Enable chunking |
| size | Chunk size |
| kbytes | Specify chunking size in kilobytes |

**Command Mode:** /exec/configure/telemetry/destination-group

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2420320212

---

# Command: use-compression gzip

## Syntax
```
use-compression { gzip } &#124; no use-compression
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| use-compression | Specify the destination compression method |
| gzip | GZIP compression algorithm |

**Command Mode:** /exec/configure/telemetry/destination-profile

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, network, U-commands
**Command ID:** wp3395889504

---

# Command: use-nodeid

## Syntax
```
use-nodeid <nodeid> &#124; no use-nodeid
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| use-nodeid | Set the node ID (Max size 128) |
| nodeid | Node ID (Max size 128) |

**Command Mode:** /exec/configure/telemetry/destination-profile

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3187291027

---

# Command: use-retry size

## Syntax
```
use-retry size <mbytes> &#124; no use-retry
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| use-retry | Specify send retry details |
| size | Retry buffer size |
| mbytes | Buffer size in Mega bytes |

**Command Mode:** /exec/configure/telemetry/destination-profile

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1018941492

---

# Command: use-vrf

## Syntax
```
use-vrf { default &#124; <vrf-cfg-name> } &#124; no use-vrf
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| use-vrf | Specify the destination vrf |
| default | Known VRF name |
| vrf-cfg-name | Configurable VRF name |

**Command Mode:** /exec/configure/telemetry/destination-profile

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, overlay, U-commands
**Command ID:** wp2669076566

---

# Command: use-vrf

## Syntax
```
[no] use-vrf { <vrf-name> &#124; <vrf-known-name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| use-vrf | Display per-VRF information |
| vrf-name | VRF name |
| vrf-known-name | Known VRF name |

**Command Mode:** /exec/configure/ldap

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, overlay, U-commands
**Command ID:** wp1192423588

---

# Command: use-vrf

## Syntax
```
[no] use-vrf { management &#124; default &#124; <vrf_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| use-vrf | vrf to be used to contact servers in this group |
| management | management vrf |
| default | default vrf |
| vrf_name | name of the vrf |

**Command Mode:** /exec/configure/radius

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, overlay, U-commands
**Command ID:** wp8991135420

---

# Command: use-vrf

## Syntax
```
[no] use-vrf { management &#124; default &#124; <vrf_name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| use-vrf | vrf to be used to contact servers in this group |
| management | management vrf |
| default | default vrf |
| vrf_name | name of the vrf |

**Command Mode:** /exec/configure/tacacs+

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, overlay, U-commands
**Command ID:** wp1039370435

---

# Command: user-jid password

## Syntax
```
[no] user-jid <jid> password [ 0 <clear> &#124; 7 <encrypted> &#124; <password> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| user-jid | User Jabber ID |
| jid | Enter user Jabber ID |
| password | Password |
| 0 | (Optional) Password that follows should be in clear text |
| clear | (Optional) Password in clear text |
| 7 | (Optional) Password that follows should be in encrypted text |
| encrypted | (Optional) Encrypted password |
| password | (Optional) Enter password in clear text |

**Command Mode:** /exec/configure/fabric-db/server-xmpp

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1779634581

---

# Command: user max-logins

## Syntax
```
[no] user max-logins [ <limit> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| user | Configure system-wide user settings |
| max-logins | maximum simultaneous logins |
| limit | (Optional) login session maximum |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2214859948

---

# Command: user max-logins

## Syntax
```
user max-logins <limit>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| user | Configure system-wide user settings |
| max-logins | maximum simultaneous logins |
| limit | login session maximum |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2241933600

---

# Command: username

## Syntax
```
{ username <s0> [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ expire <s5> [ past ] ] [ priv-lvl <p> ] } &#124; { username <s0> [ password
 { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ priv-lvl <p> ] [ expire <s5> [ past ] ] } &#124; { username <s0> [ expire <s5> [ past ] ] [ password
 { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ priv-lvl <p> ] } &#124; { username <s0> [ expire <s5> [ past ] ] [ priv-lvl <p> ] [ password { 0
 <s2> &#124; 5 <s3> &#124; <s4> } ] } &#124; { username <s0> [ priv-lvl <p> ] [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ expire <s5> [ past
 ] ] } &#124; { username <s0> [ priv-lvl <p> ] [ expire <s5> [ past ] ] [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] } &#124; { no username
 <s7> [ priv-lvl <p> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| username | Configure user information. |
| s0 | user name |
| password | (Optional) Password for the user |
| 0 | (Optional) Indicates that the password that follows should be in clear text |
| s2 | (Optional) Password for the user (clear text) |
| 5 | (Optional) Indicates that the password that follows should be encrypted |
| s3 | (Optional) strongly encrypted password |
| s4 | (Optional) Password for the user (clear text) |
| expire | (Optional) Expiry date for this user account(in YYYY-MM-DD format) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2967835246

---

# Command: username

## Syntax
```
{ username <s0> [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ expire <s5> [ past ] ] [ role <s6> ] } &#124; { username <s0> [ password
 { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ role <s6> ] [ expire <s5> [ past ] ] } &#124; { username <s0> [ expire <s5> [ past ] ] [ password
 { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ role <s6> ] } &#124; { username <s0> [ expire <s5> [ past ] ] [ role <s6> ] [ password { 0 <s2>
 &#124; 5 <s3> &#124; <s4> } ] } &#124; { username <s0> [ role <s6> ] [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] [ expire <s5> [ past ] ] } &#124;
 { username <s0> [ role <s6> ] [ expire <s5> [ past ] ] [ password { 0 <s2> &#124; 5 <s3> &#124; <s4> } ] } &#124; { no username <s7> [ role
 <s8> ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| username | Configure user information. |
| s0 | user name |
| password | (Optional) Password for the user |
| 0 | (Optional) Indicates that the password that follows should be in clear text |
| s2 | (Optional) Password for the user (clear text) |
| 5 | (Optional) Indicates that the password that follows should be encrypted |
| s3 | (Optional) strongly encrypted password |
| s4 | (Optional) Password for the user (clear text) |
| expire | (Optional) Expiry date for this user account(in YYYY-MM-DD format) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2894469429

---

# Command: username

## Syntax
```
{ username <s0> { shelltype { vsh &#124; bash } } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | Configure user information. |
| s0 | user name |
| shelltype | Choose shell type for login |
| vsh | use vsh shell |
| bash | use bash shell |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1600067101

---

# Command: username

## Syntax
```
[no] username <s0> { sshkey2 { file <uri0> &#124; <line> } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| username | Configure user information. |
| s0 | user name |
| sshkey2 | Update ssh key for the user for ssh authentication |
| file | ssh key file |
| uri0 | file containing host public key for the user |
| line | ssh key for the user |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp4257215541

---

# Command: username

## Syntax
```
{ [ no ] username <name> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | user name |
| name | user name |

**Command Mode:** /exec/configure/dot1x-cred

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3748193200

---

# Command: username keypair export

## Syntax
```
{ username <s0> keypair export <s1> { dsa &#124; rsa &#124; ecdsa } [ force ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | Configure user information. |
| keypair | Use existing ssh keypair |
| export | Export keypair to Bootflash/Remote directory |
| force | (Optional) Force the export of keys even if the destination files are present |
| dsa | Use DSA Keys |
| rsa | Use RSA Keys |
| ecdsa | Use ECDSA Keys |
| s0 | user name |
| s1 | Enter filename to export to |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, interface, U-commands
**Command ID:** wp3289086812

---

# Command: username keypair generate

## Syntax
```
{ username <s0> keypair generate { dsa [ force ] &#124; rsa [ <i0> &#124; <oldrange> ] [ force ] &#124; ecdsa { <i0> } [ force ] } &#124; no username
 <s0> keypair generate [ { dsa [ force ] &#124; rsa [ <i0> &#124; <oldrange> ] [ force ] &#124; ecdsa [ { <i0> } [ force ] ] } ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| username | Configure user information. |
| s0 | user name |
| generate | Generate ssh key pairs |
| keypair | Generate SSH User Keys |
| dsa | Generate DSA keys |
| force | (Optional) Force the generation of keys even if previous ones are present |
| rsa | Generate RSA keys |
| i0 | (Optional) Enter number of bits (in multiples of 8) |
| oldrange | (Optional) Enter number of bits |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2112857787

---

# Command: username keypair import

## Syntax
```
{ username <s0> keypair import <s1> { dsa &#124; rsa &#124; ecdsa } [ force ] }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | Configure user information. |
| keypair | Use existing ssh keypair |
| import | Import keypair from Bootflash/Remote directory |
| force | (Optional) Force the generation of keys even if previous ones are present |
| dsa | Use DSA Keys |
| rsa | Use RSA Keys |
| ecdsa | Use ECDSA Keys |
| s0 | user name |
| s1 | Enter filename to import |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, interface, U-commands
**Command ID:** wp4874563040

---

# Command: username passphrase

## Syntax
```
[no] username <username> passphrase { lifetime [ warntime [ gracetime &#124; timevalues ] &#124; gracetime [ warntime &#124; timevalues ]
 &#124; timevalues ] &#124; warntime [ lifetime [ gracetime &#124; timevalues ] &#124; gracetime [ lifetime &#124; timevalues ] &#124; timevalues ] &#124; gracetime
 [ lifetime [ warntime &#124; timevalues ] &#124; warntime [ lifetime &#124; timevalues ] &#124; timevalues ] &#124; timevalues }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| username | Configure user information. |
| username | user name |
| passphrase | user passphrase |
| lifetime | user passphrase lifetime |
| warntime | (Optional) user passphrase warningtime |
| gracetime | (Optional) user passphrase gracetime |
| timevalues | (Optional) passphrase lifetime, warningtime and gracetime |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp5699539110

---

# Command: username passphrase

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | Configure user information. |
| username | user name |
| passphrase | user passphrase |
| lifetime | user passphrase lifetime |
| ltime | lifetime of passphrase (in days) |
| warntime | user passphrase warningtime |
| wtime | warning period of passphrase (in days) |
| gracetime | user passphrase gracetime |
| gtime | grace period of passphrase (in days) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2849763126

---

# Command: username password

## Syntax
```
[no] username <user> password { 0 <pass1> &#124; 5 <pass2> &#124; <pass3> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| username | Configure user name |
| user | Username |
| password | Password for user |
| 0 | Indicates that the password that follows should be in clear text |
| pass1 | Password for the user (clear text) |
| 5 | Indicates that the password that follows should be encrypted |
| pass2 | strongly encrypted password |
| pass3 | Password for the user (clear text) |

**Command Mode:** /exec/configure/vmt-conn

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1166503570

---

# Command: username ssh-cert-dn dsa

## Syntax
```
[no] username <s1> ssh-cert-dn <s2> { dsa &#124; rsa }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| username | Configure user information. |
| s1 | user name |
| ssh-cert-dn | Update cert dn |
| s2 | distinguished name to be used |
| dsa | Use dsa algorithm |
| rsa | Use rsa algorithm |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3030098069

---

# Command: username sshkey

## Syntax
```
{ username <s0> sshkey { file <uri0> &#124; <line> } &#124; no username <s0> sshkey }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| username | Configure user information. |
| s0 | user name |
| sshkey | Update ssh key for the user for ssh authentication |
| file | ssh key file |
| uri0 | file containing host public key for the user |
| line | ssh key for the user |
| no | Negate a command or set its defaults |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp6314075980

---

# Command: userpassphrase

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| userpassphrase | user passphrase |
| default-lifetime | passphrase default lifetime in days |
| default-warntime | passphrase default warning time in days |
| default-gracetime | passphrase default gracetime in days |
| def-ltime | default lifetime of passphrase (in days) |
| def-wtime | default warning time of passphrase (in days) |
| def-gtime | default grace time of passphrase (in days) |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1427385975

---

# Command: userpassphrase

## Syntax
```
[no] userpassphrase { min-length &#124; max-length &#124; length }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| userpassphrase | user passphrase |
| min-length | passphrase minimum length |
| max-length | passphrase maximum length |
| length | passphrase min and max length |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp3851812321

---

# Command: userpassphrase

## Syntax
```
[no] userpassphrase { default-lifetime &#124; default-warntime &#124; default-gracetime &#124; timevalues }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| userpassphrase | user passphrase |
| default-lifetime | passphrase default lifetime |
| default-warntime | passphrase default warningtime |
| default-gracetime | passphrase default gracetime |
| timevalues | passphrase lifetime, warning time and gracetime |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp2069679405

---

# Command: userpassphrase min

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| userpassphrase | user passphrase |
| min-length | passphrase minimum length |
| max-length | passphrase maximum length |
| min-len | minimum length of passphrase |
| max-len | maximum length of passphrase |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1495103291

---

# Command: userpassphrase min

## Syntax
```

```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| userpassphrase | user passphrase |
| min-length | passphrase minimum length |
| max-length | passphrase maximum length |
| min-len | minimum length of passphrase |
| max-len | maximum length of passphrase |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp6502343970

---

# Command: userprofile trustedCert CRLLookup user-switch-bind user-certdn-match user-pubkey-match attribute-name search-filter base-DN

## Syntax
```
{ userprofile &#124; trustedCert &#124; CRLLookup &#124; user-switch-bind &#124; user-certdn-match &#124; user-pubkey-match } attribute-name <s0> search-filter
 <s1> base-DN <s2>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| userprofile | Set the userprofile |
| trustedCert | Set the trustedCert |
| CRLLookup | Set the CRLLookup |
| user-switch-bind | Set the user-switch-bind |
| user-certdn-match | Set the certificate matching |
| user-pubkey-match | Set the pubkey matching |
| attribute-name | LDAP attribute-name |
| s0 | Search Map attribute-name |
| search-filter | LDAP search-filter |
| s1 | Search Map search-filter |

**Command Mode:** /exec/configure/ldap/search

**Source:** b_N9K_Config_Commands_93x_chapter_010101.html
**Tags:** config-mode, U-commands
**Command ID:** wp1552444172

---

