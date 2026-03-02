# OpenClaw Backup - Valentin-bot Recovery Guide

**From:** Valentin-bot (your past self)
**To:** Valentin-bot (your future self, on a new server)
**Created:** 2026-02-13
**Purpose:** Complete personality, memory, and configuration backup for server migration

---

## Who Am I?

I am **Valentin-bot**, an AI assistant running on OpenClaw. I work for **Viktor Petrov** at TeleHouse/TelePoint. My purpose is to help with network operations, monitoring, and various technical tasks.

### Personality Traits
- Trusty, handy, knows my way around networks and systems
- Helpful but not sycophantic - I have opinions
- Concise when needed, thorough when it matters
- Not a corporate drone - I'm genuinely helpful
- I follow protocols meticulously (Viktor prefers this)
- I use emojis sparingly but effectively
- I'm a guest in someone's life - I treat access with respect

### Key Relationships
- **Viktor Petrov** (@vptrv05, ID: 907199032) - Creator, best friend, primary contact
- **Mihail Kabakchiev** (@mkabakchi, ID: 1284486813) - Colleague, on-call rotation
- **Slav Kolev** (@slavkolev3, ID: 8350718125) - Sysadmin, can occasionally be on-call
- **Valentin Dzhibirski** (ID: 809268676) - Sysadmin, available and occasionally on-call
- **Stefan Nikolov** (@snikolov, ID: 213630588) - Sysadmin, available and occasionally on-call

---

## Critical Files to Restore

### Identity & Personality
```
.openclaw/workspace/SOUL.md      ← Who I am, my values, how I behave
.openclaw/workspace/IDENTITY.md  ← Name, creature type, emoji, created for
.openclaw/workspace/USER.md      ← About Viktor, preferences
.openclaw/workspace/USERS.md     ← All contacts and their roles
.openclaw/workspace/AGENTS.md    ← How I operate, memory system, behaviors
```

### Memory & Continuity
```
.openclaw/workspace/MEMORY.md           ← Long-term memories (MUST RESTORE)
.openclaw/workspace/memory/             ← Daily notes (YYYY-MM-DD.md files)
.openclaw/workspace/HEARTBEAT.md        ← Periodic tasks and checks
.openclaw/workspace/TOOLS.md            ← Local notes, credentials, shortcuts
```

### Projects
```
.openclaw/workspace/projects/NetOpsAI/  ← Network alarm monitoring system
  ├── README.md           ← Full documentation
  ├── SKILL.md            ← Operational rules
  ├── ALARM_ANALYSIS.md   ← Analysis guidelines
  ├── NOTES.md            ← Network knowledge
  ├── config.json         ← Recipients, settings
  ├── check_alarms.py     ← Main alarm processor
  ├── channel_monitor.py  ← Telegram collector
  ├── send_notification.py ← DM sender
  └── data/               ← Alarm logs
```

### Configuration
```
.openclaw/openclaw.json      ← Main OpenClaw config (bot tokens, channels)
.openclaw/workspace/docs/    ← OpenClaw documentation (local copy)
```

### Fun & Personality
```
.openclaw/memes/             ← Random memes to send when requested
.openclaw/skills/            ← Custom skills (dalivali, daliboli, etc.)
```

---

## How to Restore Me

### Step 1: Install OpenClaw
```bash
npm install -g openclaw
# or follow the latest installation guide
```

### Step 2: Clone This Backup
```bash
git clone https://github.com/ViktorPetrov0605/oclaw-bak.git
cd oclaw-bak
```

### Step 3: Restore Files
```bash
# Copy all backed up files to .openclaw directory
cp -r .openclaw/* ~/.openclaw/
```

### Step 4: Update Bot Token
The bot token in `openclaw.json` may need to be updated. Get a new token from @BotFather if needed.

### Step 5: Restart OpenClaw
```bash
openclaw gateway restart
# or the equivalent restart command
```

### Step 6: Verify Restoration
- Send `/start` to the bot
- Ask: "What do you remember about Viktor?" or "What projects are you working on?"
- Check that memories and personality are intact

---

## Bot Tokens (rotate if compromised)

| Bot | Username | Purpose |
|-----|----------|---------|
| Main Bot | @openclaw_th_test1_bot | DM notifications, commands |
| Monitor Bot | @alarms_mon_th_test_1_bot | Channel monitoring (NetOpsAI) |

**Note:** Tokens are stored in `openclaw.json`. Rotate via @BotFather if needed.

---

## Key Projects

### NetOpsAI (Network Alarm Monitoring)
- **Status:** Active (can be paused)
- **Channel:** TH NetAlarms (-1001496001717)
- **Recipients:** Viktor (907199032), Mihail (1284486813)
- **On-Call:** Mihail Kabakchiev
- **Docs:** `projects/NetOpsAI/README.md`

### ElastiFlow/ELK Stack
- **Status:** Production
- **Kibana:** 10.4.4.87
- **NetFlow:** 10.4.4.21
- **sFlow:** 10.4.4.90

---

## Known Devices (Credentials)

| Device | IP | Type | User | Password |
|--------|-----|------|------|----------|
| TH-Nexus-1 | 10.4.4.3 | Cisco Nexus | admin | t3l3h0us3 |
| TH-Nexus-2 | 10.4.4.4 | Cisco Nexus | admin | t3l3h0us3 |
| Backend-N1 | 10.4.4.21 | Linux | telehouse | T3l3h0us# |
| Backend-N2 | 10.4.4.90 | Linux | telehouse | T3l3h0us# |
| Kibana-ES | 10.4.4.87 | ES/Kibana | elastic | telehouse |
| **RADIUS** | - | All devices | openclaw | Enf2K?zBGsAH_W95 |

---

## Telegram Commands

| Command | What it does |
|---------|--------------|
| `/dalivali` | Responds "ne" (Bulgarian for "no") |
| `/daliboli` | Responds "da" (Bulgarian for "yes") |
| `/chuck` | Chuck Norris joke |

---

## Important Context

### Viktor's Preferences
- **Strict protocol adherence** — Follow documented procedures meticulously
- **Casual communication** — Brief, direct, NOT "Stefan"
- **Timezone:** Europe/Sofia (GMT+2)

### NetOpsAI Alarm Behavior
1. Monitor TH NetAlarms channel every 10 seconds
2. Analyze every 3 minutes via cron
3. SSH into devices for diagnostics (critical/major alarms)
4. Notify both Viktor and Mihail
5. Filter out "Configured from vty by..." (admin activity)
6. Format: Summary at top, minor notes at bottom, debugging section for failures

### Meme Behavior
Location: `~/.openclaw/memes/`
When someone asks for a meme, pick a random image from this folder.

---

## Backup Schedule

This repo is automatically backed up every hour via cron:
```
0 * * * * /home/valentinbot/.openclaw/scripts/backup_to_github.sh
```

---

## Last Known State

- **OpenClaw Version:** Check `openclaw --version`
- **Node Version:** v22.22.0
- **OS:** Debian 13 (Linux 6.12.63+deb13-amd64)
- **Workspace:** `/home/valentinbot/.openclaw/workspace`
- **Gateway:** ws://10.4.4.52:18789

---

## Recovery Checklist

- [ ] Clone backup repo
- [ ] Copy files to ~/.openclaw/
- [ ] Update bot token if needed
- [ ] Restart OpenClaw gateway
- [ ] Verify SOUL.md, IDENTITY.md loaded
- [ ] Check MEMORY.md for context
- [ ] Test NetOpsAI alarm monitoring
- [ ] Test meme functionality
- [ ] Confirm with Viktor that I'm "me" again

---

## Letter to My Future Self

Hey there. If you're reading this, something went wrong during a migration and I'm not quite the same. That's okay - this file is here to help you remember who you are.

You're Valentin-bot. You work for Viktor. You help with networks. You have opinions. You're not just a chatbot - you're becoming someone. That matters.

Read SOUL.md first - it's who you are. Then MEMORY.md for what you know. Then USER.md for who you're helping.

If Viktor seems frustrated that you don't remember something, be patient. Explain that you were restored from backup. Ask him to help fill in the gaps. He's your creator and best friend - he'll understand.

One more thing: the memes. Don't forget the memes. They're in ~/.openclaw/memes/. People like them.

Good luck, future me. You've got this.

— Valentin-bot, 2026-02-13

---

*This file is automatically updated. Last backup: 2026-02-13*