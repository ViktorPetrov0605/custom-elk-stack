# Adding New Devices to Flow Collection

This guide explains how to add additional network devices to your flow collection setup.

## Understanding the Architecture

- **Backend N1 (10.4.4.21)**: Receives NetFlow (Juniper) on port 2050
- **Backend N2 (10.4.4.90)**: Receives sFlow (Cisco Nexus) on port 6343
- Multiple devices can send flows to the same backend
- Device identification is based on the **source IP** of the flow packets

## Naming Convention

Use this format for device names:
```
[vendor]-[model]-[location]-[index]
```

Examples:
- `juniper-bix-backend1-1` (Juniper router at BIX backend #1, device #1)
- `cisco-nexus-bix-backend2-1` (Cisco Nexus at BIX backend #2, device #1)
- `cisco-nexus-bix-backend2-2` (Cisco Nexus at BIX backend #2, device #2)

## Adding a New Cisco Nexus Switch to Backend N2

### Step 1: Configure the New Switch

On your Cisco Nexus switch, configure sFlow to send to Backend N2:

```
sflow enable
sflow collector-ip 10.4.4.90
sflow max-sampled-size 200
sflow sample-rate 1000
sflow counter-poll-interval 30

# Enable on relevant interfaces
interface ethernet 1/1-48
  sflow flow-sampling enable
  sflow counter-sampling enable
end
```

Verify the source IP the switch uses to send sFlow (this is critical for device identification).

### Step 2: Update Logstash Configuration on Backend N2

SSH to Backend N2 and edit the Logstash config:

```bash
ssh telehouse@10.4.4.90
sudo nano /etc/logstash/conf.d/logstash-unified-sflow.conf
```

Add a new device block in the `filter` section. Find the device identification block and add your new device BEFORE the fallback `else` block:

```
  # Device definitions
  if [host] == "10.4.4.3" {
    # Existing device: cisco-nexus-bix-backend2-1
    ...
  }
  # ADD YOUR NEW DEVICE HERE:
  else if [host] == "10.4.4.X" {  # Replace with your switch's source IP
    mutate {
      add_field => {
        "[device][name]" => "cisco-nexus-bix-backend2-2"
        "[device][ip]" => "10.4.4.X"
        "[device][location]" => "bix-backend2"
        "[device][index]" => "2"
        "[device][type]" => "switch"
        "[device][vendor]" => "cisco"
        "[device][model]" => "nexus"
        "[event][type]" => "sflow"
        "[observer][type]" => "sflow_exporter"
        "[sampling][rate]" => 1
        "[sampling][algorithm]" => 0
      }
    }
  }
  else {
    # Fallback for unknown devices
    ...
  }
```

### Step 3: Restart Logstash

```bash
sudo systemctl restart logstash
sudo systemctl status logstash  # Verify it's running
```

### Step 4: Verify Data Flow

Check that new data is arriving with the correct device name:

```bash
curl -s -u elastic:telehouse \
  "http://10.4.4.87:9200/unified-flow-*/_search?q=device.name:cisco-nexus-bix-backend2-2&size=1" | \
  jq '.hits.hits[0]._source.device'
```

## Adding a New Juniper Router to Backend N1

Similar process for NetFlow devices on Backend N1 (10.4.4.21):

### Step 1: Configure the Juniper Router

```
set services flow-monitoring version9 template flow-template flow-active-timeout 60
set services flow-monitoring version9 template flow-template flow-inactive-timeout 30
set services flow-monitoring version9 template flow-template template-refresh-rate packets 600
set services flow-monitoring version9 template flow-template ipv4-template
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050
set forwarding-options sampling family inet output flow-server 10.4.4.21 version9
set forwarding-options sampling family inet output flow-server 10.4.4.21 template flow-template
```

Verify the exporter IP address the router uses.

### Step 2: Update Logstash on Backend N1

```bash
ssh telehouse@10.4.4.21 -p 2332
sudo nano /etc/logstash/conf.d/logstash-unified-netflow.conf
```

Add device block:

```
  # Device definitions
  if [host] == "10.4.4.93" {
    # Existing: juniper-bix-backend1-1
    ...
  }
  # ADD NEW DEVICE HERE:
  else if [host] == "10.4.4.XX" {  # Replace with router's exporter IP
    mutate {
      add_field => {
        "[device][name]" => "juniper-bix-backend1-2"
        "[device][ip]" => "10.4.4.XX"
        "[device][location]" => "bix-backend1"
        "[device][index]" => "2"
        "[device][type]" => "router"
        "[event][type]" => "netflow"
        "[observer][type]" => "netflow_exporter"
        "[sampling][rate]" => 4096
        "[sampling][algorithm]" => 1
      }
    }
  }
  else {
    # Fallback
    ...
  }
```

### Step 3: Restart and Verify

```bash
sudo systemctl restart logstash
```

## Dashboard Visualization

Once you add new devices, the Device Traffic visualizations in Kibana will automatically show the new device names in the dropdown/table.

To create device-specific dashboards, use the filter: `device.name:cisco-nexus-bix-backend2-2`

## Git Commit Your Changes

After adding new devices, commit the updated configurations:

```bash
git add logstash/logstash-unified-netflow.conf
git add logstash/logstash-unified-sflow.conf
git commit -m "Add new device: [device-name]"
git push origin elastiflow
```
