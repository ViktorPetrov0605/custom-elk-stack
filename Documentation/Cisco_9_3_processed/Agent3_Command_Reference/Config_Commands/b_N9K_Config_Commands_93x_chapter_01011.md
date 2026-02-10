# Chapter: K Commands

**Source File:** b_N9K_Config_Commands_93x_chapter_01011.html
**Type:** Configuration Commands  
**Chapter:** Group-1011 Commands  
**Total Commands:** 17

## Command List

- `key-chain macsec-psk no-show`
- `key-octet-string 7 cryptographic-algorithm AES_128_CMAC`
- `key-octet-string 7 cryptographic-algorithm AES_256_CMAC`
- `key-octet-string cryptographic-algorithm AES_128_CMAC`
- `key-octet-string cryptographic-algorithm AES_256_CMAC`
- `key-server-priority`
- `key-string`
- `key-string 7`
- `key`
- `key`
- `key chain`
- `key chain macsec`
- `key config-key hex`
- `kill-everyone`
- `kill background`
- `kstack multicast-udp`
- `kubernetes server ip-address port`

---

## Detailed Command Reference

# Command: key-chain macsec-psk no-show

## Syntax
```
[no] key-chain macsec-psk no-show
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key-chain | Keychain Management |
| macsec-psk | Macsec Pre-shared key |
| no-show | do not show |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp3900707072

---

# Command: key-octet-string 7 cryptographic-algorithm AES_128_CMAC

## Syntax
```
{ key-octet-string 7 <keystring> cryptographic-algorithm AES_128_CMAC }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| key-octet-string | Set key octet string |
| 7 | Encryption Type - Proprietary |
| keystring | key octet string |
| cryptographic-algorithm | Select CMAC algorithm for authentication |
| AES_128_CMAC | cryptographic-algorithm AES-128-CMAC |

**Command Mode:** /exec/configure/macseckeychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1243658111

---

# Command: key-octet-string 7 cryptographic-algorithm AES_256_CMAC

## Syntax
```
{ key-octet-string 7 <keystring> cryptographic-algorithm AES_256_CMAC }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| key-octet-string | Set key octet string |
| 7 | Encryption Type - Proprietary |
| keystring | key octet string |
| cryptographic-algorithm | Select CMAC algorithm for authentication |
| AES_256_CMAC | cryptographic-algorithm AES-256-CMAC |

**Command Mode:** /exec/configure/macseckeychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp3510529222

---

# Command: key-octet-string cryptographic-algorithm AES_128_CMAC

## Syntax
```
{ key-octet-string [ 0 ] <keystring> cryptographic-algorithm AES_128_CMAC &#124; no key-octet-string [ 0 ] <keystring> cryptographic-algorithm
 AES_128_CMAC }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| key-octet-string | Set key octet string |
| 0 | (Optional) Encryption Type - No Encryption(default) |
| keystring | key octet string |
| cryptographic-algorithm | Select CMAC algorithm for authentication |
| AES_128_CMAC | cryptographic-algorithm AES-128-CMAC |

**Command Mode:** /exec/configure/macseckeychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp3971581447

---

# Command: key-octet-string cryptographic-algorithm AES_256_CMAC

## Syntax
```
{ key-octet-string [ 0 ] <keystring> cryptographic-algorithm AES_256_CMAC &#124; no key-octet-string [ 0 ] <keystring> cryptographic-algorithm
 AES_256_CMAC }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| key-octet-string | Set key octet string |
| 0 | (Optional) Encryption Type - No Encryption(default) |
| keystring | key octet string |
| cryptographic-algorithm | Select CMAC algorithm for authentication |
| AES_256_CMAC | cryptographic-algorithm AES-256-CMAC |

**Command Mode:** /exec/configure/macseckeychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1200421893

---

# Command: key-server-priority

## Syntax
```
[no] key-server-priority <pri>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| key-server-priority | Configure Key-Server priority |
| pri | key-server priority value |

**Command Mode:** /exec/configure/macsec-policy

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, qos, K-commands
**Command ID:** wp2044561797

---

# Command: key-string

## Syntax
```
{ key-string [ 0 ] <keystring> &#124; no key-string }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| key-string | Set key string |
| 0 | (Optional) Encryption Type - No Encryption(default) |
| keystring | key string |

**Command Mode:** /exec/configure/keychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1593929282

---

# Command: key-string 7

## Syntax
```
{ key-string 7 <keystring> }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| key-string | Set key string |
| 7 | Encryption Type - Proprietary |
| keystring | key string |

**Command Mode:** /exec/configure/keychain-key

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1899901998

---

# Command: key

## Syntax
```
[no] key <keyid>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key | Configure a key |
| keyid | Key identifier |

**Command Mode:** /exec/configure/keychain

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp3674124449

---

# Command: key

## Syntax
```
[no] key <macsec_keyid>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key | Configure a macsec key |
| macsec_keyid | MACsec Key identifier ranging from 1 octet to 32 |

**Command Mode:** /exec/configure/macseckeychain

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1667340078

---

# Command: key chain

## Syntax
```
[no] key chain <keychain>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key | Key Management |
| chain | Keychain Management |
| keychain | key-chain name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp2067518640

---

# Command: key chain macsec

## Syntax
```
[no] key chain <keychain> macsec
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key | Key Management |
| chain | Keychain Management |
| keychain | macsec key-chain name |
| macsec | Macsec Keychain |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp3933801769

---

# Command: key config-key hex

## Syntax
```
[no] key config-key { hex &#124; ascii } [ <master-key> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| key | Encryption key for strong encryption |
| config-key | Master-key for strong encryption of secrets in config |
| hex | Key followed should be in hex format |
| ascii | Key followed should be in ascii format |
| master-key | (Optional) Enter the Master-key |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1316037093

---

# Command: kill-everyone

## Syntax
```
[no] [ eigrp ] kill-everyone
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| eigrp | (Optional) EIGRP router configuration commands |
| kill-everyone | Kill all adjacencies on SIA |

**Command Mode:** /exec/configure/router-eigrp/router-eigrp-vrf-common /exec/configure/router-eigrp/router-eigrp-af-common

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp1322602263

---

# Command: kill background

## Syntax
```
kill background <pid>
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| kill | terminate processes |
| background | kill background processes (started with 'source background <file>' command) |
| pid | background script to terminate, by process-id or just a regex matching any line from 'show background' command |

**Command Mode:** /exec

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, K-commands
**Command ID:** wp2295080242

---

# Command: kstack multicast-udp

## Syntax
```
{ { no kstack multicast-udp } &#124; { kstack multicast-udp { enable &#124; disable } } }
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | Negate a command or set its defaults |
| kstack | Enable/Disable kstack feature |
| multicast-udp | Clone UDP dest Multicast packets to kstack |

**Command Mode:** /exec/configure /exec/configure/config-mgmt

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, network, K-commands
**Command ID:** wp8177227530

---

# Command: kubernetes server ip-address port

## Syntax
```
[no] kubernetes server ip-address <ip-addr> port <s0> [ vrf <vrf-name> ] &#124; no kubernetes server
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| no | (Optional) Negate a command or set its defaults |
| kubernetes | kubernetes |
| server | kubernetes server |
| ip-address | IP address of the kubernetes host |
| ip-addr | ip address of kubernetes Host |
| port | Port number of the host |
| s0 | port number |
| vrf | (Optional) Display per-VRF information |
| vrf-name | (Optional) VRF name |

**Command Mode:** /exec/configure

**Source:** b_N9K_Config_Commands_93x_chapter_01011.html
**Tags:** config-mode, interface, network, K-commands
**Command ID:** wp6315328470

---

