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

### Message Handling
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

## Key Design Questions (To Be Answered)

1. **Device types?** (Cisco, Juniper, MikroTik, Linux-based?) — determines SSH commands
2. **Credential storage?** (SSH keys, passwords, jump hosts?)
3. **False positive tolerance?** (Over-alert vs. under-alert preference?)
4. **Authorization levels?** (Read-only diagnostics vs. permitted fixes?)
5. **Escalation paths?** (Just Telegram, or email/SMS/Signal for critical?)

---

## Notes

This is essentially a **Network Operations AI** that sits between the monitoring stack (Telegram bots) and infrastructure. The challenge isn't monitoring—it's **noise reduction** and **trust calibration**.

---

*Document created by Valentin-bot as a starting point for future implementation.*
