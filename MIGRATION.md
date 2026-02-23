# Migration Guide (ElastiFlow -> Logstash)

This guide details migrating to the unified Logstash collector.

## Key Differences

*   **Capacity:** Unlimited (no 4k RPS cap).
*   **Identification:** sFlow uses internal payload IP; NetFlow uses `netflow.exporter.ipv4_address`.
*   **Multipliers:** Juniper's 4096x sampling factor is applied manually in the Logstash Ruby filter.

## Clean Room Setup

1.  **Stop ElastiFlow:** Remove all containers and prune the `elastiflow-data` volumes.
2.  **Clean ES Mapping:** Delete any indices matching `elastiflow-*` or `logstash-flow-*` to prevent mapping conflicts with old data.
3.  **Deploy Template:** Run `./deploy.sh --frontend` first. This is critical as it defines the `ip` type for `device.ip` before any data arrives.

## Troubleshooting

If sFlow data shows up but NetFlow doesn't:
1.  Verify the port (2050).
2.  Check for "Waiting for template" warnings in `docker logs`.
3.  Ensure the switch can reach the Backend server (ping/tcpdump).
