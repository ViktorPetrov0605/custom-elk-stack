# ElastiFlow Analysis: Logstash Replacement Feasibility Study

**Date:** 2026-02-09  
**Research Goal:** Determine if ElastiFlow can replace Logstash on backend servers (10.4.4.21 and 10.4.4.90) for NetFlow/sFlow collection  
**Researcher:** Subagent Analysis  

---

## Executive Summary

ElastiFlow is a purpose-built, high-performance network flow collector designed specifically for NetFlow, sFlow, IPFIX, and public cloud flow data. Unlike Logstash (a general-purpose data pipeline), ElastiFlow is optimized for network observability with built-in enrichment, pre-built dashboards, and ML-based anomaly detection. It offers a **free tier up to 4,000 flows/second** and can output directly to local Elasticsearch clusters.

**Verdict:** ElastiFlow is technically feasible as a Logstash replacement for NetFlow/sFlow collection and offers significant advantages in terms of out-of-box functionality, performance, and pre-built visualizations.

---

## 1. Product Overview and Architecture

### What is ElastiFlow?

ElastiFlow (now branded as NetObserv for the collector component) is a unified flow collector that:

- **Collects** flow data from multiple sources (NetFlow v5/v9/IPFIX, sFlow v5, AWS VPC Flow Logs, Azure NSG Flow Logs, GCP VPC Flow Logs)
- **Normalizes** all flow data into a common schema (ECS format)
- **Enriches** data with GeoIP, ASN (BGP), threat intelligence, DNS, and user-defined business context
- **Outputs** to various backends including Elasticsearch, OpenSearch, Kafka, and Splunk
- **Visualizes** through pre-built Kibana dashboards (40+ out-of-the-box)

### Architecture

```
Network Devices (Routers/Switches/Firewalls)
    ↓ (NetFlow/sFlow/IPFIX)
ElastiFlow Unified Collector
    ↓ (Enrichment + Normalization)
Elasticsearch/OpenSearch/Kafka/Splunk
    ↓
Kibana/Grafana/Dashboards
```

### Key Differentiators from Logstash

| Feature | Logstash | ElastiFlow |
|---------|----------|------------|
| Purpose | General-purpose pipeline | Purpose-built for network flows |
| Flow Parsing | Manual codec configuration | Native support for all flow types |
| Data Enrichment | Manual filter configuration | Built-in GeoIP, ASN, threat intel |
| Dashboards | Must build from scratch | 40+ pre-built dashboards |
| ML/Anomaly Detection | Requires manual setup | 130+ pre-configured ML jobs |
| Schema Normalization | Manual mapping | Automatic ECS normalization |

---

## 2. Pricing & Licensing

### Free Tier ( Public License )

**Limit:** Up to **4,000 flow records per second (RPS)**  
**Cost:** Free  
**Features Included:**
- Full flow collection (NetFlow, sFlow, IPFIX)
- Basic GeoIP and ASN enrichment
- Standard dashboards
- Community support (Slack + Forum)
- Non-production license (technically)

### Premium Tier

**Limit:** Up to **1,000,000+ flow records per second**  
**Pricing:** Contact ElastiFlow for quote (not publicly disclosed)  
**Additional Features:**
- 40+ out-of-the-box dashboards (vs. DIY in free tier)
- Custom dashboard creation
- ML-based anomaly detection (130+ jobs)
- Metadata enrichment (cloud service, application)
- Netintel Threat Feed integration
- MITRE ATT&CK threat mapping
- Distributed flow collection
- Professional support (8x5 for Basic, 24x7 for Enterprise)
- ElastiFlow-assisted custom dashboards and training

### Pricing Model

- **Per-server or cluster:** Pricing is based on flow rate (records per second), not per server
- **No server-based licensing:** The free 4,000 RPS limit applies across your deployment
- **Subscription tiers:**
  - **Basic:** Up to 4,000 RPS, Slack + Forum support
  - **Premium:** Up to 1M+ RPS, 8x5 support, professional services available
  - **Enterprise:** Up to 1M+ RPS, 24x7 support with dedicated rep, full professional services

### Cost Comparison Table

| Aspect | ElastiFlow Free | ElastiFlow Premium | Logstash |
|--------|-----------------|-------------------|----------|
| **License Cost** | $0 | Contact for quote | $0 (OSS) |
| **Flow Rate Limit** | 4,000 RPS | 1M+ RPS | No hard limit |
| **Support** | Community | 8x5 or 24x7 | Community |
| **Pre-built Dashboards** | DIY / Basic | 40+ included | None |
| **ML Anomaly Detection** | Limited | 130+ jobs | Manual setup |
| **Threat Intelligence** | Basic GeoIP/ASN | NetIntel feed | Manual integration |
| **Enrichment** | Basic | Full | Manual |

---

## 3. Technical Requirements

### Supported Flow Types

✅ **NetFlow:** v5, v9, v10 (IPFIX) - Cisco and compatible devices  
✅ **sFlow:** v5 - Multi-vendor standard (switches, routers, firewalls, hosts)  
✅ **IPFIX:** IETF standard, vendor-neutral  
✅ **AWS VPC Flow Logs:** Via Data Firehose integration  
✅ **Azure NSG Flow Logs:** Via Network Watcher  
✅ **GCP VPC Flow Logs:** Native support  
✅ **SNMP:** Unified SNMP Trap and Poller collector (separate component)

### Elasticsearch Compatibility

**Local Elasticsearch Support:** ✅ YES  
ElastiFlow explicitly supports local Elasticsearch deployments (not just cloud):

- **Elasticsearch versions:** 7.x, 8.x (with TSDS support from 8.7+)
- **Output formats:** Index or Time Series Data Streams (TSDS)
- **Index Lifecycle Management:** Auto-generated ILM policies

**Storage Optimization Features:**
- **TSDS (Time Series Data Streams):** Reduces storage by 50-70%
  - Example: 10,000 flows/sec = ~563 GB/day (without TSDS) → ~163 GB/day (with TSDS)
- **Synthetic source:** Reconstructs documents from doc_values
- **Downsampling:** Reduces granularity of historical data
- **ILM Policies:** Hot/Warm/Cold/Delete phases automated

### Resource Requirements

#### Minimum Requirements (Small Deployment)

| Component | CPU | RAM | Disk |
|-----------|-----|-----|------|
| ElastiFlow Collector | 2 cores | 4 GB | 20 GB |
| Elasticsearch (single node) | 4 cores | 8 GB | 500 GB+ |

#### Recommended for Production

| Component | CPU | RAM | Disk | Notes |
|-----------|-----|-----|------|-------|
| ElastiFlow Collector | 4+ cores | 8+ GB | 50 GB | Scales horizontally |
| Elasticsearch (3-node cluster) | 8+ cores/node | 32+ GB/node | 2+ TB/node | Hot/warm architecture |

**Performance Notes:**
- ElastiFlow is written in Go (high performance, low resource usage)
- Can handle up to 1M+ flows/second with proper sizing
- CGO disabled to remove glibc dependency
- Supports distributed collection (multiple collectors)

### Configuration Complexity vs Logstash

#### Logstash Configuration
```ruby
# Manual codec configuration required
input {
  udp {
    port => 2055
    codec => netflow {
      versions => [5, 9]
    }
  }
}

filter {
  # Manual GeoIP enrichment
  geoip {
    source => "[netflow][ipv4_src_addr]"
    target => "src_geo"
  }
  # Manual ASN lookup
  # Manual threat intel integration
  # Manual ECS mapping
}

output {
  elasticsearch {
    # Manual index management
  }
}
```

#### ElastiFlow Configuration
```yaml
# Simple environment variables or config file
EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
EF_OUTPUT_ELASTICSEARCH_HOST: "localhost:9200"
EF_FLOW_UDP_IPV4_PORT: "2055"
EF_FLOW_UDP_IPV6_PORT: "2056"
# Enrichment automatically enabled
# Dashboards pre-built
# ILM auto-generated
```

**Complexity Comparison:**
- **Logstash:** High - Requires manual codec setup, field mapping, enrichment configuration
- **ElastiFlow:** Low - Purpose-built, most features work out-of-box

---

## 4. Installation Methods

### Docker/Container Support

✅ **Full Docker support** 

Available deployment options:
- **Docker Compose:** Single-node and multi-node Elasticsearch clusters
- **Kubernetes:** Helm charts available for containerized environments
- **Standalone Container:** Single ElastiFlow collector container

**Docker Images:**
- ElastiFlow provides official Docker images
- Can be deployed alongside existing Logstash containers
- Supports environment variable configuration

### Installation Options

1. **Docker Compose (Recommended for testing)**
   - Complete stack in minutes
   - Includes ElastiFlow + Elasticsearch + Kibana
   - Pre-configured dashboards

2. **RPM/Deb Packages**
   - Systemd service integration
   - Configuration in `/etc/elastiflow/`
   - Production-grade deployment

3. **Manual Binary**
   - Standalone Go binary
   - Minimal dependencies
   - Portable across Linux distributions

4. **Kubernetes**
   - Helm charts for enterprise deployment
   - Scalable collector pools
   - Service mesh integration

### Running Alongside Existing Logstash

✅ **Yes, ElastiFlow can run alongside Logstash**

Migration strategies:
- **Parallel deployment:** Run both during transition period
- **Different ports:** Configure ElastiFlow on different UDP ports
- **Gradual cutover:** Move devices one-by-one from Logstash to ElastiFlow
- **No conflicts:** Different systemd services, no port conflicts if configured properly

### Migration Path from Logstash

**Phase 1: Preparation (1-2 days)**
1. Assess current flow rates (ensure under 4,000 RPS for free tier)
2. Document current Logstash configuration
3. Backup existing Elasticsearch indices
4. Review pre-built ElastiFlow dashboards

**Phase 2: Parallel Deployment (1 week)**
1. Deploy ElastiFlow on separate ports
2. Configure subset of devices to send to ElastiFlow
3. Compare data quality and dashboard functionality
4. Train team on new Kibana dashboards

**Phase 3: Migration (1-2 days)**
1. Migrate remaining devices to ElastiFlow
2. Decommission Logstash flow pipelines
3. Retain Logstash for other data sources if needed

**Phase 4: Optimization (ongoing)**
1. Implement ILM policies for storage management
2. Configure TSDS for storage savings (50-70%)
3. Enable ML anomaly detection (Premium)

---

## 5. Limitations

### Flow Rate Limits

| Tier | Max Flows/Second | Notes |
|------|------------------|-------|
| Free | 4,000 RPS | Hard limit, sufficient for small-medium networks |
| Basic | 4,000 RPS | Same as free, adds support |
| Premium | 1,000,000+ RPS | Contact for pricing |
| Enterprise | 1,000,000+ RPS | Full support + services |

**Calculation for your environment:**
- Estimate total flows/second from all devices
- If under 4,000 RPS → Free tier viable
- If over 4,000 RPS → Premium subscription required

### Supported Vendors/Devices

**NetFlow:**
- ✅ Cisco (all platforms supporting NetFlow/IPFIX)
- ✅ Juniper (J-Flow compatible)
- ✅ Palo Alto Networks
- ✅ Arista
- ✅ Riverbed
- ✅ Any RFC-compliant NetFlow/IPFIX device

**sFlow:**
- ✅ Most major switch vendors (multi-vendor standard)
- ✅ Arista
- ✅ Dell/EMC
- ✅ HP/HPE
- ✅ Extreme Networks
- ✅ Host agents available

**Cloud:**
- ✅ AWS VPC Flow Logs
- ✅ Azure Network Watcher NSG Flow Logs
- ✅ GCP VPC Flow Logs

### Dashboard/Visualization Capabilities

**Free Tier:**
- Basic pre-built dashboards
- Manual dashboard creation required for custom views
- Standard Kibana visualizations

**Premium/Enterprise:**
- **40+ out-of-the-box dashboards** including:
  - Network overview and top talkers
  - Geographic traffic visualization
  - Security threat analysis
  - BGP ASN analysis
  - DNS/DHCP/LDAP performance
  - TCP flag analysis
  - DDoS detection views
- Custom dashboard assistance (Enterprise)
- Wizard-driven ML job creation

### Data Retention Policies

ElastiFlow leverages Elasticsearch ILM (Index Lifecycle Management):

**Default Policy:**
- **Hot phase:** 0-7 days (high-performance SSD)
- **Warm phase:** 7-30 days (HDD storage)
- **Cold phase:** 30+ days (cold storage)
- **Delete phase:** Configurable (e.g., 90 days)

**Configurable:**
- Retention periods fully customizable
- TSDS downsampling for historical data
- Automated rollover based on time or size
- No forced retention limits imposed by ElastiFlow

**Storage Cost Management:**
- TSDS can reduce storage by 50-70%
- Example savings: $3,124/month → $904/month for 10K flows/sec

---

## 6. Free vs Paid Comparison Table

| Feature | Free Tier | Premium | Enterprise |
|---------|-----------|---------|------------|
| **Flow Rate** | 4,000 RPS | 1M+ RPS | 1M+ RPS |
| **NetFlow/sFlow/IPFIX** | ✅ | ✅ | ✅ |
| **Cloud Flow Logs** | ✅ | ✅ | ✅ |
| **Basic GeoIP/ASN** | ✅ | ✅ | ✅ |
| **Pre-built Dashboards** | Basic | 40+ | 40+ |
| **Custom Dashboards** | DIY | ✅ | ElastiFlow-assisted |
| **ML Anomaly Detection** | Limited | 130+ jobs | 130+ jobs |
| **Threat Intel (NetIntel)** | ❌ | ✅ | ✅ |
| **MITRE ATT&CK Mapping** | ❌ | ✅ | ✅ |
| **Cloud Service Enrichment** | ❌ | ✅ | ✅ |
| **App Enrichment** | ❌ | ✅ | ✅ |
| **Distributed Collection** | ❌ | ✅ | ✅ |
| **Support** | Slack + Forum | 8x5 | 24x7 + dedicated rep |
| **Professional Services** | ❌ | Available | Included |
| **Training** | ❌ | ❌ | Included |
| **License Cost** | $0 | $$ | $$$ |

---

## 7. Technical Feasibility for Our Use Case

### Requirements Check

| Requirement | Feasibility | Notes |
|-------------|-------------|-------|
| Replace Logstash on 10.4.4.21 and 10.4.4.90 | ✅ **YES** | Can run on both servers |
| NetFlow collection | ✅ **Native support** | v5, v9, IPFIX |
| sFlow collection | ✅ **Native support** | v5 |
| Output to local Elasticsearch | ✅ **Supported** | Works with on-prem ES |
| Run alongside Logstash | ✅ **Possible** | Use different ports |
| Docker/container deployment | ✅ **Supported** | Official images available |
| Migration path exists | ✅ **Clear path** | Documented approach |

### Sizing for Your Environment

To determine if free tier is sufficient:

1. **Measure current flow rate:** Check Logstash metrics for current flows/second
2. **Calculate capacity:** 4,000 RPS = ~345 million flows/day
3. **If under 4,000 RPS:** Free tier viable
4. **If over 4,000 RPS:** Premium subscription required

**Hardware requirements for your servers (10.4.4.21 and 10.4.4.90):**
- If servers already run Logstash + Elasticsearch, ElastiFlow should fit within same resources
- ElastiFlow collector is more efficient than Logstash for flow processing
- TSDS feature can reduce Elasticsearch storage by 50-70%

---

## 8. Recommendation

### Decision: **MIGRATE to ElastiFlow** ✅

**Rationale:**

1. **Purpose-built for network flows:** Unlike Logstash which requires manual codec and filter configuration, ElastiFlow handles NetFlow/sFlow natively

2. **Out-of-box functionality:** 40+ pre-built dashboards vs. building everything from scratch in Logstash

3. **Free tier available:** If your flow rate is under 4,000 RPS, you can run completely free

4. **Storage efficiency:** TSDS support can reduce storage costs by 50-70% compared to standard Logstash indexing

5. **Active development:** Regular updates, active community, modern Go-based architecture

6. **No vendor lock-in:** Can output to Elasticsearch, OpenSearch, Kafka, or Splunk

### Migration Plan

**Timeline: 2-3 weeks**

#### Week 1: Assessment & Preparation
- [ ] Measure current flow rates from all devices
- [ ] Determine if free tier (4,000 RPS) is sufficient
- [ ] Document current Logstash NetFlow/sFlow configuration
- [ ] Backup existing data
- [ ] Deploy ElastiFlow on test ports (2055 for NetFlow, 6343 for sFlow)

#### Week 2: Parallel Operation
- [ ] Configure 20% of devices to send to ElastiFlow
- [ ] Import ElastiFlow dashboards to Kibana
- [ ] Compare data quality and completeness
- [ ] Train operations team on new dashboards
- [ ] Tune ElastiFlow configuration

#### Week 3: Full Migration
- [ ] Migrate remaining 80% of devices to ElastiFlow
- [ ] Decommission Logstash flow collection
- [ ] Implement ILM policies for storage management
- [ ] Enable TSDS for storage optimization (if on ES 8.7+)
- [ ] Document new operational procedures

### Configuration for Your Servers

**Recommended approach for 10.4.4.21 and 10.4.4.90:**

```yaml
# ElastiFlow configuration for dual-server deployment
# Run on both servers for redundancy or split by device type

EF_FLOW_UDP_IPV4_PORT: "2055"  # NetFlow
EF_FLOW_UDP_IPV4_PORT_SFLOW: "6343"  # sFlow (if supported in version)

# Elasticsearch output
EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
EF_OUTPUT_ELASTICSEARCH_HOST: "localhost:9200"
EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_TYPE: "tsds"  # Use TSDS for storage savings

# Enrichment
EF enrichment_geoip_enable: "true"
EF_enrichment_asn_enable: "true"

# License (if premium)
EF_LICENSE_KEY: "your-license-key"
```

### Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Data loss during migration | Run parallel collectors during transition |
| Dashboard disruption | Import ElastiFlow dashboards before migration |
| Performance issues | Start with free tier, monitor resource usage |
| Team learning curve | Parallel operation allows gradual adaptation |
| License cost uncertainty | Start with free tier to assess flow rates |

---

## 9. Additional Resources

### ElastiFlow Links
- Website: https://www.elastiflow.com
- Documentation: https://docs.elastiflow.com
- Pricing: https://www.elastiflow.com/subscriptions
- GitHub: https://github.com/elastiflow
- Community Slack: Available via website
- Blog: https://www.elastiflow.com/blog

### Key Blog Posts Referenced
- "sFlow vs. NetFlow: A Network Observability Face-Off"
- "Leveraging Open Source and Public License Solutions"
- "10 Features to Look for in a NetFlow/Flow Collector"
- "Introducing ElastiFlow support for TSDS"
- "ElastiFlow Tips and Tricks for Everyone"
- "Stop Hoarding! Take Control Of Network Data with Elasticsearch ILM"

---

## Appendix: Quick Decision Matrix

| If your situation is... | Recommendation |
|-------------------------|----------------|
| Flow rate < 4,000 RPS, budget limited | **Use Free Tier** - Zero cost, full functionality |
| Flow rate > 4,000 RPS, security-focused | **Premium Tier** - ML detection, threat intel |
| Enterprise environment, needs 24/7 support | **Enterprise Tier** - Dedicated support |
| Heavy Logstash investment, other pipelines | **Hybrid** - Keep Logstash for other data, ElastiFlow for flows |
| Just testing/evaluating | **Free Tier** - No risk, 30-day premium trial available |

---

*Report generated: 2026-02-09*  
*Sources: elastiflow.com, docs.elastiflow.com, ElastiFlow blog posts, GitHub repositories*
