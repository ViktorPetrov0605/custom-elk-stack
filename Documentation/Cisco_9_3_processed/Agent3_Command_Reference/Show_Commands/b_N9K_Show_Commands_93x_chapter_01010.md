# Chapter: K Show Commands

**Source File:** b_N9K_Show_Commands_93x_chapter_01010.html
**Type:** Show Commands  
**Chapter:** Group-1010 Commands  
**Total Commands:** 5

## Command List

- `show key chain`
- `show key chain mode decrypt`
- `show keystore`
- `show kim inconsistency`
- `show kubernetes containers`

---

## Detailed Command Reference

# Command: show key chain

## Syntax
```
{ show key chain [ <keychain> ] } [ __readonly__ TABLE_keychain <chain_name> { TABLE_key [ <key_id> ] [ <key_string> ] [ <crypto_algo>
 ] [ <accept_utc_zone> ] [ <accept_start> ] [ <accept_end> ] [ <accept_valid> ] [ <send_utc_zone> ] [ <send_start> ] [ <send_end>
 ] [ <send_valid> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| key | Display Key Information |
| chain | Display Keychain Information |
| keychain | (Optional) Keychain name |
| __readonly__ | (Optional) |
| TABLE_keychain | (Optional) |
| TABLE_key | (Optional) |
| chain_name | (Optional) |
| key_id | (Optional) |
| key_string | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01010.html
**Tags:** show-mode, S-commands
**Command ID:** wp1506529154

---

# Command: show key chain mode decrypt

## Syntax
```
{ show key chain [ <keychain> ] mode decrypt } [ __readonly__ TABLE_keychain_decrypt <chain_name> { TABLE_key [ <key_id> ]
 [ <key_string> ] [ <crypto_algo> ] [ <accept_utc_zone> ] [ <accept_start> ] [ <accept_end> ] [ <accept_valid> ] [ <send_utc_zone>
 ] [ <send_start> ] [ <send_end> ] [ <send_valid> ] } ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| key | Display Key Information |
| chain | Display Keychain Information |
| keychain | (Optional) Keychain name |
| mode | Mode of display |
| decrypt | Display Decrypted Keystrings |
| __readonly__ | (Optional) |
| TABLE_keychain_decrypt | (Optional) |
| TABLE_key | (Optional) |
| chain_name | (Optional) |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01010.html
**Tags:** show-mode, S-commands
**Command ID:** wp4084730453

---

# Command: show keystore

## Syntax
```
show keystore [ __readonly__ { TABLE_sksd_state_entries <index> <handle> } <keystore_type> <keystore_ver> <fw_panics> <fw_resets>
 <rx_fifo_underruns> <rx_timeouts> <rx_bad_checksums> <rx_bad_fragment_lengths> <keystore_corruption> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| keystore | keystore stats |
| __readonly__ | (Optional) |
| TABLE_sksd_state_entries | (Optional) Displays handles of the keys stored |
| index | (Optional) Index value |
| handle | (Optional) Handle Name |
| keystore_type | (Optional) Type of storage h/w or s/w |
| keystore_ver | (Optional) Version |
| fw_panics | (Optional) Number of panics |
| fw_resets | (Optional) Number of Resets |
| rx_fifo_underruns | (Optional) Rx FIFO Underruns |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01010.html
**Tags:** show-mode, S-commands
**Command ID:** wp1366407531

---

# Command: show kim inconsistency

## Syntax
```
show kim inconsistency
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| kim | Display KIM information |
| inconsistency | KIM inconsistency |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01010.html
**Tags:** show-mode, S-commands
**Command ID:** wp1054231671

---

# Command: show kubernetes containers

## Syntax
```
show kubernetes containers [ brief &#124; interface <if_name> ]
```

### Syntax Description

| Parameter | Description |
|-----------|-------------|
| show | Show running system information |
| kubernetes | Show kubernetes |
| containers | containers |
| brief | (Optional) Show brief information |
| interface | (Optional) Interface name |
| if_name | (Optional) Physical interface |

**Command Mode:** /exec

**Source:** b_N9K_Show_Commands_93x_chapter_01010.html
**Tags:** show-mode, S-commands
**Command ID:** wp6092488230

---

