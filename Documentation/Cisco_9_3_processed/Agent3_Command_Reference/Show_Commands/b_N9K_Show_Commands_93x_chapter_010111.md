# Chapter: X Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_010111.html
**Type:** Show Commands  
**Chapter:** Group-10111 Commands  
**Total Commands:** 2

## Command List

- `show xml server logging configuration`
- `show xml server status`

---

## Detailed Command Reference

# Command: show xml server logging configuration

## Syntax
```
show xml server logging configuration
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| xml | Show xmlagent logging configuration |
| server | xml agent server |
| logging | Show logging configuration and contents of logfile |
| configuration | Show facility logging configuration |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010111.html
**Tags:** show-mode, management, S-commands
**Command ID:** wp3538293166

---

# Command: show xml server status

## Syntax
```
show xml server status [ __readonly__ { operational_status <o_status> } { maximum_sessions_configured <max_session> } [ {
 TABLE_sessions <session_id> <user_name> <start_time> <sap_id> <timeout> <time_remaining_to_timeout> <ip_addr> } ] ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | to display xml agent information |
| xml | xml agent |
| server | xml agent server |
| status | display xml agent information |
| __readonly__ | (Optional) |
| operational_status | (Optional) run-time info about xml |
| o_status | (Optional) operational status of the xml |
| maximum_sessions_configured | (Optional) the max session configured |
| max_session | (Optional) max sessions number |
| TABLE_sessions | (Optional) all xml sessions |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_010111.html
**Tags:** show-mode, S-commands
**Command ID:** wp9097742360

---

