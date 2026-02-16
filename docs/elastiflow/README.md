# ElastiFlow Deployment Guide

> **DEPRECATED:** This documentation is for ElastiFlow which has been replaced by Logstash Unified Flow Collector.
> > **See:** [Logstash Documentation](/docs/logstash/README.md) for current deployment
> **See:** [Migration Guide](/MIGRATION.md) for transitioning from ElastiFlow

---

## Migration Notice

This project has migrated from **ElastiFlow** to **Logstash** for the following reasons:

| Feature | ElastiFlow | Logstash (Current) |
|---------|------------|-------------------|
| License Limit | 4000 RPS (free tier) | Unlimited |
| Max Devices | ~20-30 | 50+ |
| Cost | Commercial license required | Open source (free) |
| Schema | ECS-compliant | ECS-compliant |
| Dashboards | ElastiFlow-specific | Compatible with migration |

## Quick Migration

```bash
# 1. Deploy Logstash (see docs/logstash/README.md)
./deploy.sh --collectors

# 2. Update dashboards to use logstash-flow-*
# 3. Stop ElastiFlow containers
# 4. Verify data flowing
```

Full migration guide: [MIGRATION.md](/MIGRATION.md)

## Legacy Documentation

The following ElastiFlow-specific files are preserved for reference but are no longer maintained:

- `configs/elastiflow/docker-compose-n1.yml` - Primary collector config
- `configs/elastiflow/docker-compose-n2.yml` - Secondary collector config
- `configs/elastiflow/ilm-policy.json` - Original ILM policy

## Current Architecture

```
Frontend (ES + Kibana)
    │
    ▼
Logstash Collectors (NetFlow + sFlow unified)
    │
    ▼
Index: logstash-flow-*
```

## Support

For new deployments, use the Logstash collector documented at:

- [Logstash Documentation](/docs/logstash/README.md)
- [Deployment Guide](/DEPLOYMENT.md)

---

*ElastiFlow deprecated: 2026-02-16*
*Logstash migration completed: 2026-02-16*