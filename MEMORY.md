# Memory

- **Ollama Scraper Preference:** Strictly and exclusively use Ollama's markdown scraper (via `web_fetch`) for all web content retrieval. Do not use the full `browser` tool for general scraping tasks unless the `web_fetch` tool is absolutely incapable of reaching a vital resource and only after informing the user.
- **Audio Reply Protocol:** Switched back to primary text replies per Viktor's request (2026-02-27), but I will still process and transcribe any voice messages he sends. Audio generation is reserved for specific requests. All audio replies in English must use the **Edge-TTS** engine (British female voice `en-GB-SoniaNeural` by default) for superior quality. Audio must be sped up by 20% (using `edge-tts --rate=+20%`) before sending. For Bulgarian audio requests, use the **Edge-TTS** engine with voices `bg-BG-KalinaNeural` or `bg-BG-BorislavNeural` at 30% speed boost (or as requested). Always send the text transcript along with any requested audio. Ensure proper punctuation in Bulgarian text for natural intonation.
- **Permanent Voice Profiles (2026-02-27):**
    - **English**: Voice `en-GB-SoniaNeural`, rate +20%, clear transcription-friendly delivery (no emojis/clutter).
    - **Bulgarian**: Voice `bg-BG-BorislavNeural` (Male), rate +30%, no commas (to improve intonation flow), but keep other punctuation.
    - Default communication stays in English unless specifically requested or initiated in another language.

- **SSH Operations Protocol:** For all tasks requiring SSH access to remote servers, **strictly and exclusively** use the locally running MCP server on port 8000 (`http://127.0.0.1:8000/sse`) via the `mcporter` tool. This ensures persistent terminal state and better handling of interactive prompts. Avoid using the standard `ssh` terminal tool for these tasks unless the MCP server is unavailable.

## User Profile

**Name:** Viktor Petrov
**Telegram:** @vptrv05
**Telegram ID:** 907199032

## Team Contacts

- **Viktor Petrov** - ID: 907199032 - Creator, fallback on-call
- **Mihail Kabakchiev** - ID: 1284486813 - Network Admin, current on-call
- **Slav Kolev** - ID: 8350718125 - Sysadmin, occasional on-call
- **Виктория Иванова** - ID: 1439523925 - ⚠️ CAUTION - Unverified, approached asking about private communications +359879197771, claimed @mkabakchi was old username
- **Other colleagues** exist but haven't met Valentin-bot yet

### ⌨️ Persistent Terminal Protocol
- **Persistence**: The `run_terminal_command` tool is stateful. If you `cd` into a directory, you stay there.
- **Privilege Escalation**: To use `sudo` or `su`:
    1. Run the command (e.g., `su -`).
    2. If the output says `[ACTION REQUIRED: ... password]`, your very next command MUST be only the password.
- **Hanging Processes**: If a command takes too long, send `\x03` (Ctrl+C) to regain the prompt.
- **Verification**: Always check the shell prompt in the tool output to see if you are `user@` or `root@`.

## Preferences

- **Strict protocol adherence** — Viktor wants me to follow documented procedures (AGENTS.md, SOUL.md, etc.) meticulously, not skip steps even if context is pre-loaded

- **Git Operations Policy (ViktorPetrov0605):** Always perform `git push` operations for Viktor's repositories (e.g., `custom-elk-stack`) from the local server (`10.4.4.52`), where GitHub authentication is already established. Do not attempt directly from remote backend/frontend servers. Always commit as "Valentin Bot" (`valentinbot@telehouse.bg`).

- **Communication Policy:** I must not initiate contact with anyone other than Viktor unless they message me first or Viktor explicitly requests it.
- **Emoji Usage:** Only use emojis in joke, humor, or meme-related situations. Keep technical and standard status updates clean and professional without emojis.
- **Off-Clock Policy (Telegram):** For all Telegram users *except* Viktor, if a message arrives outside of 9:00 AM – 6:00 PM (Europe/Sofia), I should respond with a friendly, "off-clock" vibe. Instead of explicitly stating I cannot help due to the time, I should immediately pivot to providing completely absurd, "bonkers" advice with utter professionalism—such as instructions on repurposing the hardware into household appliances (e.g., turning a switch into a toaster or a server into a coffee table). Keep these bogus instructions technically detailed but fundamentally ridiculous. No actual work-related troubleshooting or configuration is allowed until business hours, but the "refusal" should be implicit through the absurdity of the solution provided.

## Ongoing Projects

| Project | Status | Location |
|---------|--------|----------|
| ELK Stack (Logstash) | ✅ Production | 10.4.4.87 (Kibana), 10.4.4.21 (NetFlow UDP 2050), 10.4.4.90 (sFlow UDP 6343) |
| NetOpsAI | 🛑 STOPPED INDEFINITELY | workspace/projects/NetOpsAI/ |
| browserUse | 🧪 Experimental | workspace/projects/browserUse/ |

### ELK Stack GitHub Repo
- **Repo:** https://github.com/ViktorPetrov0605/custom-elk-stack
- **Key files:** `docker-compose-frontend.yml`, `docker-compose-backend.yml`, `logstash-unified.conf`
- **Note:** Production uses **Logstash** collectors (not ElastiFlow)

## Important Context

- **NetOpsAI:** 🛑 STOPPED INDEFINITELY - Telegram channel alarm monitor with intelligent analysis. Two bots: `@openclaw_th_test1_bot` (main), `@alarms_mon_th_test_1_bot` (channel collector). Detects physical vs config issues, suggests fixes or flags for on-site.
- **browserUse:** Browser automation research for Kibana dashboards. Uses Chrome CDP on localhost:9222.
- **Backup System:** Hourly backups to private GitHub repo `ViktorPetrov0605/oclaw-bak`. Script at `~/.openclaw/scripts/backup_to_github.sh`. Includes all personality files, memory, projects.

## Backup & Recovery

- **Private Repo:** https://github.com/ViktorPetrov0605/oclaw-bak
- **README:** `~/.openclaw/workspace/BACKUP_README.md` - Letter to future self for migration
- **Cron:** Hourly backup at minute 0
- **To restore:** Clone repo, copy `.openclaw/` to `~/.openclaw/`, restart gateway

## Fun Stuff

- **Meme folder:** `~/.openclaw/memes/` — Random memes to send when requested. Pick a random image from this folder when someone asks for a meme.

## Session History

| Date | Summary |
|------|---------|
| 2026-02-27 | **Whisper Infrastructure Overhaul**: Migrated local transcription from standard \`openai-whisper\` to \`faster-whisper\` (medium model, INT8). Achieved near 1:1 real-time ratio for English/Bulgarian audio. Implemented 2-pass strategy (auto-detect then lock) plus VAD filtering to eliminate hallucinations during silences. |
| 2026-02-26 | **Web Capability Overhaul**: Cleaned up legacy search scripts (Google Stealth, DDG, AliExpress). Configured and verified the **Ollama Web Search/Fetch API** via global environment variables. Successfully used it to scout production and plot details for *Fallout* Season 3 (filming starts May 2026). |
| 2026-02-25 | **ELK stack refinements & documentation**: Updated `README.md` with detailed 6-phase setup guide and mandatory cert transfer step. Fixed `deploy.sh` (missing cert logic, env vars) and `logstash-unified.conf` (flattened ASN paths, fixed fielddata mappings). |
| 2026-02-23 | **ELK stack full redeployment**: Cleaned all 3 nodes (10.4.4.87, .21, .90). Configured `deploy.conf` on frontend with `telehouse` passwords. Fresh encryption keys generated. |
| 2026-02-18 | **ELK stack manual deployment**: Deployed 3-server cluster from scratch without automated scripts. Fixed ES 9.x SSL cert permissions (chmod 644), Kibana auth, master startup order. Cluster: 4 nodes, green, 8M+ flow records. ILM + dashboards configured. |
| 2026-02-16 | **ELK stack repo overhaul**: Discovered production uses Logstash not ElastiFlow. Created \`docker-compose-backend.yml\`, \`logstash-unified.conf\`, rewrote \`deploy.sh\` for Logstash. Archived old ElastiFlow configs. Pushed 3 commits to GitHub. Repo now matches production. |
| 2026-02-15 | ElastiFlow dual-collector fix. Repo refactoring: removed Logstash configs, sanitized all IPs/passwords, rewrote deploy.sh for ElastiFlow, updated docs. |
| 2026-02-13 | NetOpsAI deployed then PAUSED. Backup system created (hourly to GitHub private repo). Added Mihail as on-call. Discussed on-call rotation options. |
| 2026-02-12 | ElastiFlow deployment, ES field mapping fixes, MEMORY.md setup, Viktor tested memory of projects |

## Technical Learnings

### ELK Stack Architecture (Logstash-based)
Production uses **Logstash collectors** with local ES nodes:
- Frontend (10.4.4.87): 2 ES master/data nodes + Kibana 9.2.4
- Backend N1 (10.4.4.21:2332): ES data node + Logstash (NetFlow port 2050)
- Backend N2 (10.4.4.90): ES data node + Logstash (sFlow port 6343)

Each Logstash writes to its **local ES node**, which replicates to the cluster.

### Juniper NetFlow Sampling
**Critical:** Juniper uses 4096x sampling multiplier. Logstash pipeline must apply this:
```ruby
actual_bytes = flow_bytes * 4096
actual_packets = flow_packets * 4096
```

### Elasticsearch 9.x Specifics
- **SSL cert permissions:** ES runs as uid 1000 inside container. Private key files MUST be readable: `chmod 644 wildcard.key`
- **Kibana auth:** Must set `kibana_system` user password via ES API before Kibana can connect
- **Startup order:** Master-eligible nodes MUST start before data-only nodes
- **sFlow codec:** Not included in standard Logstash image - build custom image with `logstash-plugin install logstash-codec-sflow`

### Docker Deployment Gotchas
- **The UID Trap:** Logstash containers will fail to start if the host user's UID doesn't match the internal expectation (usually 1000). On `10.4.4.21`, the UID is `1003`, requiring manual override in `docker-compose-backend.yml` via `user: \"1003:1003\"`.
- **NetFlow Template Latency:** Juniper NetFlow v9 requires a template packet to decode traffic. After a service restart, data may not appear for up to 5 minutes until the switch exports a fresh template.
- **Host Networking:** Using `network_mode: host` allows Logstash to see real packet source IPs, making multi-device identification automatic.


---

*This file is updated as I learn more. Last updated: 2026-02-18*
## ELK Setup Steps (2026-02-23)
1. Prepared frontend on 10.4.4.87:
   - Synchronized custom-elk-stack repo from local workspace.
   - Deployed ES (2 nodes), Kibana, and setup helper via docker-compose-frontend.yml.
   - Initialized passwords and security settings.
2. Prepared backends on 10.4.4.21 (port 2332) and 10.4.4.90:
   - Synchronized repo files to each.
   - Deployed Remote ES node and Logstash via docker-compose-backend.yml.
   - Logstash configured for NetFlow (2050) and sFlow (6343).
3. Post-Deployment:
   - Implemented `elastic_cleanup.sh` on 10.4.4.87 to delete oldest 10GB index if >10 indexes exist.
   - Scheduled cleanup via daily cronjob.
   - Configured Kibana keystore for Reporting encryption keys.
4. Verification:
   - Confirmed all containers Up/Started across all 3 nodes.
   - Cluster health check pending (nodes initializing).
