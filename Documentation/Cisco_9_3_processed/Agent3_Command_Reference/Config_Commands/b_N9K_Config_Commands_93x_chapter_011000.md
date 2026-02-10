# Chapter: X Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_011000.html
**Type:** Configuration Commands  
**Chapter:** Group-11000 Commands  
**Total Commands:** 15

## Command List

- `xconnect`
- `xml`
- `xml`
- `xml server max-session`
- `xml server rm-shm`
- `xml server terminate session`
- `xml server timeout`
- `xml server validate`
- `xml server xml-debug`
- `xmlagent`
- `xmlin`
- `xmlin`
- `xmlin`
- `xmlin`
- `xmlout`

---

## Detailed Command Reference

# Command: xconnect

## Syntax
```
xconnect &#124; no xconnect
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| xconnect | Enable cross connect on this VLAN |

**Command Mode:** /exec/configure/vlan

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp1995932671

---

# Command: xml

## Syntax
```
&#124; xml
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| xml | output in xml format (according to .xsd definitions) |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3206043878

---

# Command: xml

## Syntax
```
&#124; xml
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| xml | output in xml format (according to .xsd definitions) |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp1501924363

---

# Command: xml server max-session

## Syntax
```
[no] xml server max-session <number>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| xml | xml agent |
| server | xml agent server |
| max-session | configure maximum number of xml sessions allowed |
| number | number of the sessions |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3403214564

---

# Command: xml server rm-shm

## Syntax
```
xml server rm-shm
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xml | xml agent |
| server | xml agent server |
| rm-shm | remove shmem. SHOULD BE USED WITH CAUTION |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3296854426

---

# Command: xml server terminate session

## Syntax
```
xml server terminate session <session_id>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xml | xml agent |
| server | xml agent server |
| terminate | command to terminate an XML session |
| session | terminate an XML session |
| session_id | sessions number |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3735178871

---

# Command: xml server timeout

## Syntax
```
[no] xml server timeout <value> [ <session_id> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| xml | xml agent |
| server | xml agent server |
| timeout | configure xml agent session timeout |
| value | timeout in seconds |
| session_id | (Optional) xml agent session id |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, system, X-commands
**Command ID:** wp2110535027

---

# Command: xml server validate

## Syntax
```
[no] xml server validate { all &#124; <session_id> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| xml | xml agent |
| server | xml agent server |
| validate | command to validate an XML session |
| all | all sessions |
| session_id | session number |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp2298899680

---

# Command: xml server xml-debug

## Syntax
```
[no] xml server xml-debug
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| xml | xml agent |
| server | xml server |
| xml-debug | xml server xml-debug |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp1181970527

---

# Command: xmlagent

## Syntax
```
xmlagent
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xmlagent | to run xmlagent |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp2454647943

---

# Command: xmlin

## Syntax
```
&#124; xmlin
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| xmlin | Convert CLI show commands to their XML formats |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp1471206786

---

# Command: xmlin

## Syntax
```
xmlin
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xmlin | Convert CLI commands to their XML formats |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3474055012

---

# Command: xmlin

## Syntax
```
xmlin
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| xmlin | Convert CLI commands to their XML formats |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp2828330827

---

# Command: xmlin

## Syntax
```
&#124; xmlin
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| xmlin | Convert CLI show commands to their XML formats |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3066940250

---

# Command: xmlout

## Syntax
```
&#124; xmlout
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| | | Pipe command output to filter |
| xmlout | output in xml format (according to the latest .xsd version) |

**Command Mode:** /output

**Source:** b_N9K_Config_Commands_93x_chapter_011000.html
**Tags:** config-mode, X-commands
**Command ID:** wp3590754817

---

