# NetOpsAI - Autonomous Network Alarm Monitoring

**Status:** Concept / Design Phase  
**Created:** 2026-02-08  
**Purpose:** Autonomous monitoring, diagnosis, and reporting of network device alarms from multiple Telegram channels.

---

## Overview

This project outlines an AI-powered system to monitor Telegram channels receiving network device alarms, aggregate sporadic alarms from multiple sources, detect patterns, autonomously diagnose issues by logging into devices, and report findings to the network administrator.

---

## 1. Telegram Channel Monitoring

### Multi-Channel Ingestion
- Add bot to multiple Telegram channels (network alarm channels)
- Configure `channels.telegram.groups` with `requireMention: false` to see all messages
- Each channel gets isolated context or shared alarm processing context
- Use `groupAllowFrom` to restrict to specific alarm bot IDs (process only legitimate alarms)

### Message Handling — BATCH PROCESSING (Not Real-Time)
**⚠️ Do NOT analyze every message individually. Use batch processing:**

| Trigger Type | Value | Description |
|--------------|-------|-------------|
| Time-based | **3 min** | Analyze buffered messages every 3 minutes |
| Count-based | **15 messages** | Trigger when buffer reaches 15 messages |
| Hybrid | Whichever first | Time OR count — whichever triggers first |

**Batch Settings (Configurable):**
- Check interval: **3 minutes**
- Message batch size: **15 messages**

**Why batch?**
- Single messages lack context for correlation
- Reduces LLM API calls (cost + speed)
- Enables multi-alarm pattern detection in one pass
- Deduplication happens before analysis

**Implementation:**
```
Message Buffer (SQLite or JSON)
├── Incoming messages → append with timestamp
├── Check trigger conditions
│   ├── Last analysis > 5 min ago? → TRIGGER
│   └── Buffer size >= 20? → TRIGGER
├── Flush buffer → batch analysis
└── Clear buffer after processing
```

**Message Extraction:**
- Alarm bots post structured text (SNMP traps, syslog, monitoring alerts)
- Parse using regex or natural language understanding
- Extract: device ID, severity, timestamp, alarm type, affected interfaces/services

---

## 2. Alarm Aggregation & Pattern Detection

### State Management
Maintain alarm state database (SQLite or JSON) tracking:
- Device ID → last alarm timestamp → alarm count in window → severity trend
- Channel → device mapping → escalation history

### Pattern Recognition
| Pattern | Detection |
|---------|-----------|
| Spike | 5+ alarms from same device in 10 minutes |
| Correlation | Alarms from multiple devices in same subnet |
| Flapping | Rapid on/off alarms (interface flapping) |
| Time-based | Business hours only = scheduled maintenance |

### Noise Reduction
- Deduplicate similar alarms within time windows
- Filter "info" level unless correlated with "critical"
- Maintain "blackout" list for known maintenance windows

---

## 3. Autonomous Diagnostic Decision Making

### Trigger Conditions (Configurable)

```
IF device_alarm_count[window=5min] >= 3
   AND alarm_severity IN [critical, major]
   AND last_manual_check > 30min
THEN trigger_autonomous_check(device_id)
```

### Diagnostics Capabilities
- SSH into device (if credentials configured)
- Run `show interfaces`, `show logging`, `show environment`
- Ping/Traceroute to affected destinations
- Check interface statistics (errors, drops, utilization)
- Compare current config vs. baseline snapshot

### Decision Tree
| Scenario | Action |
|----------|--------|
| Simple issue (interface down) | Report with suggested fix |
| Complex issue (routing loop) | Escalate immediately |
| False positive (monitoring glitch) | Log but don't alert |

---

## 4. Reporting & Escalation

### To Viktor (Network Admin)
- **Immediate:** Critical alarms with no clear resolution
- **Digest:** Hourly summary of minor alarms with trends
- **Investigation reports:** Findings from autonomous checks

### Report Format Example
```
🚨 Alarm Spike Detected
Device: core-router-01
Pattern: 4 BGP alarms in 5 minutes
Action Taken: SSH check (show ip bgp summary)
Finding: 2 peers down, likely upstream ISP issue
Recommendation: Contact ISP NOC, check fiber path
```

---

## 5. Technical Implementation Components

| Component | Approach |
|-----------|----------|
| Channel monitoring | Telegram groups config, message queue with debouncing |
| Alarm parser | Regex patterns per device type (Cisco, Juniper, etc.) |
| State store | SQLite file in workspace or simple JSON |
| Decision engine | Rule-based + LLM for complex patterns |
| Device access | SSH tool with credential profiles |
| Scheduler | Cron for periodic checks + heartbeat |
| Rate limiter | Max 1 check per device per 5 minutes |

### Safety Mechanisms
- **Dry-run mode:** Test logic without SSH initially
- **Approval gate:** Require human approval for destructive commands
- **Escalation timeout:** If unresolved in X minutes, escalate to human
- **Audit log:** Every autonomous action logged for review

---

## 6. Handling Different Alarm Patterns

### Sporadic (30 min intervals)
- Aggregate into daily digest unless severity increases
- Track trend over days

### Flood (30 second intervals)
- Immediate grouping by device type
- Pause ingestion if >100 alarms/minute
- Fast-path for "site down" scenarios

---

## Infrastructure & Credentials

### Authentication Policy
**⚠️ DEFAULT: All devices use RADIUS authentication unless specified otherwise.**

### RADIUS Authentication
| User | Password |
|------|----------|
| openclaw | Enf2K?zBGsAH_W95 |

### SSH Command Syntax (sshpass)
```bash
# Basic SSH with password
sshpass -p 'PASSWORD' ssh -t USERNAME@IP_ADDRESS "COMMAND"

# Example - Cisco switch
sshpass -p 't3l3h0us3' ssh -t admin@10.4.4.3 "show version"

# Example - Linux/Backend server
sshpass -p 'T3l3h0us#' ssh -t telehouse@10.4.4.90 "docker ps"
```

### Device Inventory

| Device | IP | Type | SSH User | SSH Password | Purpose |
|--------|-----|------|----------|--------------|---------|
| Cisco Nexus 1 | 10.4.4.3 | Switch | admin | t3l3h0us3 | sFlow source |
| Cisco Nexus 2 | 10.4.4.4 | Switch | admin | t3l3h0us3 | sFlow source |
| Backend N1 | 10.4.4.21 | Server | telehouse | T3l3h0us# | NetFlow collector |
| Backend N2 | 10.4.4.90 | Server | telehouse | T3l3h0us# | sFlow collector |
| Frontend/Kibana | 10.4.4.87 | ES/Kibana | elastic | telehouse | Visualization |

### Elasticsearch
- **URL:** https://10.4.4.87:5601 (Kibana) / 9200 (ES)
- **User:** elastic
- **Password:** telehouse
- **Flow Indices:** `netflow-*`, `unified-flow-*`

---

## Key Design Questions (To Be Answered)

1. **Device types?** ✅ Cisco Nexus, Linux servers
2. **Credential storage?** ✅ Documented above (consider Vault for production)
3. **False positive tolerance?** (Over-alert vs. under-alert preference?)
4. **Authorization levels?** (Read-only diagnostics vs. permitted fixes?)
5. **Escalation paths?** (Just Telegram, or email/SMS/Signal for critical?)

---

## Shift-Based Operations Control

### Config File: `NetOpsAI/config.json`

```json
{
  "alarm_processing": {
    "enabled": true,
    "interval_minutes": 3,
    "batch_size": 15
  },
  "recipients": {
    "active": ["@vptrv05"],
    "notify_on": ["critical", "major", "digest"]
  },
  "shifts": {
    "current_oncall": "@vptrv05",
    "fallback": null
  }
}
```

### Controls

| Setting | Description | How to Change |
|---------|-------------|---------------|
| `alarm_processing.enabled` | On/Off for processing | `true` / `false` |
| `recipients.active` | Who gets alerts | Array of Telegram usernames |
| `shifts.current_oncall` | Current person on shift | Single username |
| `shifts.fallback` | Backup if oncall doesn't respond | Single username |

### Notification Routing

- **Critical/Major** → `recipients.active` (everyone on list)
- **Digest/Summary** → `shifts.current_oncall` (just on-call person)
- **Escalation** → `shifts.fallback` if no response in N minutes

### Telegram Commands

| Command | Action |
|---------|--------|
| `/alarmson` | Enable alarm processing |
| `/alarmsoff` | Disable alarm processing |
| `/netops` | Show current NetOpsAI status & config |
| `/oncall @user` | Set current on-call person |
| `/addrecipient @user` | Add to notification list |
| `/removerecipient @user` | Remove from list |

**Usage:** Just send the command in our chat — I'll update the config and confirm.

### Questions for Viktor

1. **Who manages shifts?** Manual update, or scheduled rotation (Mon-Fri vs weekends)?
2. **Multiple on-call?** Should `recipients.active` always get everything, or just on-call person?
3. **Escalation timeout?** If on-call doesn't acknowledge in X minutes, escalate to fallback?

---

## Notes

This is essentially a **Network Operations AI** that sits between the monitoring stack (Telegram bots) and infrastructure. The challenge isn't monitoring—it's **noise reduction** and **trust calibration**.

---

*Document created by Valentin-bot as a starting point for future implementation.*
