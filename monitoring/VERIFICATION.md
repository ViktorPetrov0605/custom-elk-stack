# sFlow Configuration - Verification Steps

## Configuration Status: ✓ COMPLETED (2026-02-09)

Both Cisco Nexus switches have been successfully configured with sFlow:
- **Collector:** 10.4.4.90:6343 (UDP)
- **Sampling Rate:** 1-out-of-4096
- **Status:** Active on both NEXUS1 (10.4.4.3) and NEXUS2 (10.4.4.4)

---

## Post-Configuration Verification (Required in 5 minutes)

### Step 1: Verify sFlow Feature Status
On each switch, run:
```
show sflow
```

Expected output should show:
- `sflow collector-ip : 10.4.4.90 , vrf : default`
- `sflow collector-port : 6343`
- `sflow sampling-rate : 4096`

### Step 2: Verify Interface Configuration
```
show running-config | include sflow
```

### Step 3: Verify Collector is Receiving Data (on collector host 10.4.4.90)

#### Option A: tcpdump
```bash
sudo tcpdump -i eth0 udp port 6343 -n
```

You should see UDP packets arriving from:
- 10.4.4.3 (NEXUS1)
- 10.4.4.4 (NEXUS2)

#### Option B: netcat listener (quick test)
```bash
nc -u -l 6343 | xxd
```

#### Option C: Check with ss/netstat
```bash
ss -lun | grep 6343
```

### Step 4: Verify Collector Application
If using an sFlow collector (e.g., sFlow-RT, pmacct, or ELK stack):
1. Check the collector's web interface
2. Verify flows are being received from both switches
3. Confirm interface statistics are being populated

---

## Quick Reference: Switch Show Commands

```
show sflow
show sflow statistics
show running-config | include sflow
```

---

## Notes

- **NEXUS2 Warning:** During configuration, a notice appeared about `span-egress rate-limiter`. Check if this needs to be disabled:
  ```
  show running-config | include span-egress
  ```

- **NEXUS2 Agent IP:** Shows 0.0.0.0 initially - will auto-detect source IP when sending traffic.

- **Po111 (1-IX):** Not configured on NEXUS2 as it's DOWN (no operational members).

---

## Documentation Location

Full configuration details saved to:
- `nexus-sflow-config.md`
