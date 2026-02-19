# Task Plan: Fix NetFlow Dynamism and Restore Flow Data

## Context
Data stopped appearing in Kibana after refactoring `logstash-unified.conf` for dynamic labeling.
Hypothesis: `[host][ip]` field in Logstash (NetFlow codec) is either missing, named differently, or nesting is incorrect for the `mutate` copy operation.

## 1. Investigation
- [x] Check Logstash container logs on `10.4.4.21` (port 2332) for errors.
- [x] Capture a raw sample of a processed event to verify available fields (using `stdout { codec => rubydebug }` if needed, or searching ES).

## 2. Implementation
- [x] Refactor `logstash-unified.conf` based on log findings:
    - Likely change: use `[host]` or `@metadata` fields if `[host][ip]` isn't present for this codec version.
    - Ensure Juniper scaling (10.4.4.93) remains intact.
- [x] Implement robust error handling (check if field exists before copying).

## 3. Deployment
- [x] Deploy to Backend N1 (`10.4.4.21` port 2332).
- [x] Deploy to Backend N2 (`10.4.4.90` port 22).
- [x] Restart containers.

## 4. Verification
- [x] Query ES for documents indexed in the last 2 minutes.
- [x] Verify `device.name` and `device.ip` are correctly populated with the collector's source IP.
- [x] Check Kibana dashboard for visualization updates.
- [x] Check and fix ILM policy (Fixed rollover_alias error).
- [x] Update ILM to 7-day retention.
- [x] Set replicas to 0 and shards to 1 for data locality.

## 5. Documentation
- [x] Update `tasks/lessons.md` with the field mapping discovery.
- [x] Update `memory/2026-02-19.md` with ILM resolution.
- [x] Push final config, tasks, and lessons to GitHub.
