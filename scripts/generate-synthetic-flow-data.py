#!/usr/bin/env python3
"""
Synthetic NetFlow data generator for ELK stack testing.
Generates flow documents matching the logstash-flow-* schema and ingests
them directly into Elasticsearch via the _bulk API.

Usage:
  python3 scripts/generate-synthetic-flow-data.py
  python3 scripts/generate-synthetic-flow-data.py --count 10000 --seed 42
"""

import argparse
import base64
import json
import random
import ssl
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta

# Default ES connection
DEFAULT_ES_URL = "https://192.168.122.160:9200"
DEFAULT_PASSWORD = "telehouse"

# Realistic IPs for source/destination pairs
SOURCE_IPS = [
    "10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4",
    "192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40",
    "172.16.0.5", "172.16.0.6", "172.16.0.7", "172.16.0.8",
]
DESTINATION_IPS = [
    "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1",
    "185.148.163.50", "10.57.144.162",
    "142.250.80.4", "157.240.16.35",
    "52.84.123.45", "34.120.8.2",
]
DEVICE_IPS = [
    "192.168.36.21", "192.168.36.22", "192.168.36.25",
    "192.168.36.26", "192.168.36.70", "192.168.36.71",
]
PROTOCOLS = [
    ("tcp", "6"), ("udp", "17"), ("icmp", "1"),
]
DEST_PORTS = [80, 443, 53, 22, 8080, 8443, 123, 389, 993, 3306]


def make_doc(timestamp=None, rng=None):
    """Generate a single flow document matching the Logstash ECS schema."""
    if rng is None:
        rng = random
    if timestamp is None:
        timestamp = datetime.now(timezone.utc)

    src = rng.choice(SOURCE_IPS)
    dst = rng.choice(DESTINATION_IPS)
    proto, iana = rng.choice(PROTOCOLS)
    dest_port = rng.choice(DEST_PORTS)
    src_port = rng.randint(1024, 65535)
    # Use lognormal distribution for bytes to create realistic variance
    bytes_val = int(rng.lognormvariate(12, 1.8))  # 10KB - 10's of MB
    packets_val = max(1, bytes_val // rng.randint(500, 1500))

    return {
        "@timestamp": timestamp.isoformat(),
        "source.ip": src,
        "source.port": src_port,
        "destination.ip": dst,
        "destination.port": dest_port,
        "network.bytes": bytes_val,
        "network.packets": packets_val,
        "network.transport": proto,
        "network.iana_number": iana,
        "device.ip": rng.choice(DEVICE_IPS),
        "device.name": rng.choice(DEVICE_IPS),
        "event.type": "netflow",
    }


def generate_bulk_payload(count, seed=None):
    """Build an NDJSON _bulk payload string."""
    rng = random.Random(seed) if seed else random
    body = ""
    now = datetime.now(timezone.utc)
    for i in range(count):
        # Spread timestamps over last 15 minutes
        ts = now - timedelta(seconds=rng.randint(0, 900))
        doc = make_doc(timestamp=ts, rng=rng)
        action = json.dumps({"index": {"_index": "logstash-flow-write"}})
        body += action + "\n" + json.dumps(doc) + "\n"
    return body


def main():
    parser = argparse.ArgumentParser(
        description="Generate synthetic NetFlow data and ingest into ES"
    )
    parser.add_argument("--es-url", default=DEFAULT_ES_URL)
    parser.add_argument("--password", default=DEFAULT_PASSWORD)
    parser.add_argument("--count", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    print(f"Generating {args.count} synthetic flow documents...")
    if args.seed:
        print(f"  Seed: {args.seed}")

    body = generate_bulk_payload(args.count, args.seed)
    print(f"  Payload: {len(body):,} bytes")

    # Build request with basic auth
    url = f"{args.es_url}/_bulk"
    auth = base64.b64encode(f"elastic:{args.password}".encode()).decode()
    req = urllib.request.Request(url, data=body.encode("utf-8"),
        headers={
            "Content-Type": "application/x-ndjson",
            "Authorization": f"Basic {auth}",
        })

    print(f"Ingesting to {url} ...")
    start = time.time()
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        resp = urllib.request.urlopen(req, context=ctx, timeout=30)
        result = json.loads(resp.read().decode())
        elapsed = time.time() - start

        if result.get("errors"):
            err_count = sum(1 for item in result.get("items", [])
                          if "error" in item.get("index", {}))
            print(f"Imported with {err_count} errors ({elapsed:.1f}s)")
            for item in result["items"]:
                idx = item.get("index", {})
                if "error" in idx:
                    print(f"  Error: {idx['error']['reason']}")
        else:
            ingested = len(result.get("items", []))
            print(f"Successfully ingested {ingested} docs ({elapsed:.1f}s)")
    except Exception as e:
        print(f"Failed: {e}")
        sys.exit(1)

    if args.verify:
        print("\nVerifying...")
        time.sleep(2)
        req2 = urllib.request.Request(
            f"{args.es_url}/logstash-flow-write/_count",
            headers={"Content-Type": "application/json", "Authorization": f"Basic {auth}"})
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            resp2 = urllib.request.urlopen(req2, context=ctx)
            count = json.loads(resp2.read().decode()).get("count", 0)
            print(f"Total documents in index: {count}")
        except Exception as e:
            print(f"Count failed: {e}")

    print("\nOpen http://192.168.122.160:5601 to see data!")


if __name__ == "__main__":
    main()
