# Chapter: U Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010100.html
**Type:** Show Commands  
**Chapter:** Group-10100 Commands  
**Total Commands:** 9

## Command List

- `show udld`
- `show udld global`
- `show udld neighbors`
- `show user-account`
- `show username keypair`
- `show username passphrase timevalues`
- `show userpassphrase`
- `show userpassphrase`
- `show users`

---

## Detailed Command Reference

# Command: show udld

## Syntax
```
Show running system information
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| udld | UDLD status and configuration on one or all interfaces |
| if0 | (Optional) Enter an interface name if only one single interface status is desired |
| __readonly__ | (Optional) |
| TABLE_interface | (Optional) |
| interface | (Optional) Interface ID |
| mib-port-status | (Optional) Port MIB enable status |
| mib-oper-status | (Optional) Port MIB Operational status |
| mib-aggresive-mode | (Optional) Port MIB aggresive mode |
| admin-port-mode | (Optional) Port enable administration configuration setting |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp8346454490

---

# Command: show udld global

## Syntax
```
show udld global [ __readonly__ <udld-global-mode> <message-interval> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| udld | UDLD protocol |
| global | UDLD global status and configuration on all interfaces |
| __readonly__ | (Optional) |
| udld-global-mode | (Optional) UDLD global configuration setting |
| message-interval | (Optional) UDLD probe messsage interval |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3322076660

---

# Command: show udld neighbors

## Syntax
```
show udld neighbors [ __readonly__ TABLE_entry <local-port-id> <neighbor-echo-device-name> <device-id> <neighbor-echo-port-id>
 <neighbor-state> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| udld | UDLD protocol |
| neighbors | UDLD neighbor interfaces |
| __readonly__ | (Optional) |
| TABLE_entry | (Optional) |
| local-port-id | (Optional) Local port ID |
| neighbor-echo-device-name | (Optional) Echo device name |
| device-id | (Optional) Device ID |
| neighbor-echo-port-id | (Optional) Echo port ID |
| neighbor-state | (Optional) Current neighbor state |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2225606782

---

# Command: show user-account

## Syntax
```
show user-account [ <s0> ] [ __readonly__ TABLE_template <usr_name> [ <expire_date> ] { TABLE_role <role> } [ <remote_login>
 ] [ <sshkey_info> ] { [ TABLE_keys <ssh_keys> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| TABLE_template | (Optional) |
| TABLE_role | (Optional) |
| TABLE_keys | (Optional) |
| __readonly__ | (Optional) |
| usr_name | (Optional) Name of the user |
| expire_date | (Optional) Expiry date for this user account(in YYYY-MM-DD format) |
| role | (Optional) role/s which the user is to be assigned to |
| remote_login | (Optional) Remote account information for a remote user |
| sshkey_info | (Optional) SSH key information of user |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp7065730180

---

# Command: show username keypair

## Syntax
```
show username <s0> keypair [ __readonly__ { TABLE_sessions <t_type> <t_time> <t_keys> <t_bitcount> <t_fingerprint> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| username | Show user information. |
| keypair | Show SSH keypairs |
| s0 | user name |
| __readonly__ | (Optional) |
| TABLE_sessions | (Optional) username keypair |
| t_type | (Optional) keys type |
| t_time | (Optional) timestamp |
| t_keys | (Optional) ssh key |
| t_bitcount | (Optional) bitcount |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3561740599

---

# Command: show username passphrase timevalues

## Syntax
```
show username <username> passphrase timevalues [ __readonly__ [ timevalues [ <tvalue> ] ] [ passphrase_change <last_passphrase_change>
 ] [ Default_lifetime <def_ltime> ] [ Default_warntime <def_wrntime> ] [ Default_gracetime <def_gtime> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| username | Configure user information. |
| username | user name |
| passphrase | user passphrase |
| timevalues | passphrase lifetime, warningtime and gracetime |
| __readonly__ | (Optional) |
| timevalues | (Optional) Timevalues of the Passphrase |
| tvalue | (Optional) Absolute time values of the Passphrase |
| passphrase_change | (Optional) passphrase last change date |
| last_passphrase_change | (Optional) absolute last passphrase change date |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, system, S-commands
**Command ID:** wp2763576785

---

# Command: show userpassphrase

## Syntax
```
show userpassphrase { min-length &#124; max-length &#124; length } [ __readonly__ [ Minimum_length <min_length> ] [ Maximum_length <max_length>
 ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| userpassphrase | user passphrase |
| min-length | passphrase minimum length |
| max-length | passphrase maximum length |
| length | passphrase min and max length |
| __readonly__ | (Optional) |
| Minimum_length | (Optional) minimum length of the passphrase |
| min_length | (Optional) Absolute value of the Minimum length |
| Maximum_length | (Optional) Maximum length of the passphrase |
| max_length | (Optional) Absolute value of max length |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp2759573204

---

# Command: show userpassphrase

## Syntax
```
show userpassphrase { default-lifetime &#124; default-warntime &#124; default-gracetime &#124; timevalues } [ __readonly__ [ Default_warntime
 <def_wrntime> ] [ Default_gracetime <def_gtime> ] [ Default_lifetime <def_ltime> ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| userpassphrase | user passphrase |
| default-lifetime | passphrase default lifetime |
| default-warntime | passphrase default warningtime |
| default-gracetime | passphrase default gracetime |
| timevalues | passphrase lifetime, warning time and gracetime |
| __readonly__ | (Optional) |
| Default_warntime | (Optional) Default Warningtime of the Passphrase |
| def_wrntime | (Optional) Absolute warning time value of the Passphrase |
| Default_gracetime | (Optional) Default Grace time of the Passphrase |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp3783229201

---

# Command: show users

## Syntax
```
show users [ __readonly__ { TABLE_sessions <u_name> <t_terminal> <t_time> <t_idle> <p_pid> <c_comment> } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| users | Show the current users logged in the system |
| __readonly__ | (Optional) |
| TABLE_sessions | (Optional) users table |
| u_name | (Optional) user name |
| t_terminal | (Optional) terminal |
| t_time | (Optional) time |
| t_idle | (Optional) idle |
| p_pid | (Optional) pid |
| c_comment | (Optional) comment |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010100.html
**Tags:** show-mode, S-commands
**Command ID:** wp6622284270

---

