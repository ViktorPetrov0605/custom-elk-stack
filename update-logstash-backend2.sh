#!/bin/bash
# Update Backend N2 (10.4.4.90) Logstash configuration

echo "=== BACKEND N2: Updating Logstash Config ==="

ssh telehouse@10.4.4.90 << 'EOF'
echo "Creating backup of current config..."
sudo cp /etc/logstash/conf.d/logstash-unified-sflow.conf /etc/logstash/conf.d/logstash-unified-sflow.conf.backup.$(date +%Y%m%d)

echo "Writing new multi-device config..."
sudo tee /etc/logstash/conf.d/logstash-unified-sflow.conf > /dev/null <<'LOGBACK'
# Unified Logstash Configuration for sFlow (Cisco Nexus) - Multi-Device Support  
# Backend N2 (10.4.4.90)

input {
  udp {
    port => 6343
    type => "sflow"
    receive_buffer_bytes => 16777216
    workers => 4
  }
}

filter {
  # Device identification - currently configured for 10.4.4.3
  # To add cisco-nexus-bix-backend2-2, add another block with: else if [host] == "10.4.4.X"
  
  if [host] == "10.4.4.3" {
    mutate {
      add_field => {
        "[device][name]" => "cisco-nexus-bix-backend2-1"
        "[device][ip]" => "10.4.4.3"
        "[device][location]" => "bix-backend2"
        "[device][index]" => "1"
        "[device][type]" => "switch"
        "[device][vendor]" => "cisco"
        "[device][model]" => "nexus"
        "[event][type]" => "sflow"
        "[observer][type]" => "sflow_exporter"
        "[sampling][rate]" => 1
        "[sampling][algorithm]" => 0
      }
    }
  } else {
    # Unknown device - will show up in dashboards with device.name = unknown-sflow-device
    mutate {
      add_field => {
        "[device][name]" => "unknown-sflow-device"
        "[device][ip]" => "%{host}"
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
  
  if [sflow] {
    if [sflow][src_ip] {
      mutate { add_field => { "[source][ip]" => "%{[sflow][src_ip]}" } }
    }
    if [sflow][dst_ip] {
      mutate { add_field => { "[destination][ip]" => "%{[sflow][dst_ip]}" } }
    }
    
    if [sflow][src_port] {
      mutate { add_field => { "[source][port]" => "%{[sflow][src_port]}" } }
    }
    if [sflow][dst_port] {
      mutate { add_field => { "[destination][port]" => "%{[sflow][dst_port]}" } }
    }
    
    if [sflow][protocol] {
      mutate { add_field => { "[network][iana_number]" => "%{[sflow][protocol]}" } }
      translate {
        field => "[network][iana_number]"
        destination => "[network][transport]"
        dictionary => {
          "6" => "tcp"
          "17" => "udp"
          "1" => "icmp"
        }
        fallback => "other"
      }
    }
    
    if [sflow][input_ifindex] {
      mutate { add_field => { "[interface][input]" => "%{[sflow][input_ifindex]}" } }
    }
    if [sflow][output_ifindex] {
      mutate { add_field => { "[interface][output]" => "%{[sflow][output_ifindex]}" } }
    }
    
    if [sflow][src_as] {
      mutate { add_field => { "[source][as][number]" => "%{[sflow][src_as]}" } }
    }
    if [sflow][dst_as] {
      mutate { add_field => { "[destination][as][number]" => "%{[sflow][dst_as]}" } }
    }
    
    if [sflow][frame_length] {
      mutate { add_field => { "[network][bytes]" => "%{[sflow][frame_length]}" } }
    } else {
      mutate { add_field => { "[network][bytes]" => 0 } }
    }
    
    mutate { add_field => { "[network][packets]" => 1 } }
    
    mutate { remove_field => [ "[sflow]" ] }
  }
  
  mutate {
    convert => {
      "[network][bytes]" => "integer"
      "[network][packets]" => "integer"
      "[source][port]" => "integer"
      "[destination][port]" => "integer"
      "[interface][input]" => "integer"
      "[interface][output]" => "integer"
      "[sampling][rate]" => "integer"
    }
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    index => "unified-flow-%{+YYYY.MM.dd}"
    ssl => true
    ssl_certificate_authorities => "/usr/share/logstash/ca.crt"
    user => "elastic"
    password => "${ELASTIC_PASSWORD}"
    ilm_enabled => true
    ilm_rollover_alias => "unified-flow"
    ilm_pattern => "{now/d}-000001"
    ilm_policy => "flow-data-1-day-retention"
  }
}
LOGBACK

echo "Restarting Logstash..."
sudo systemctl restart logstash

echo "Waiting for Logstash to start..."
sleep 10

if sudo systemctl is-active logstash > /dev/null 2>&1; then
    echo "Logstash is running"
else
    echo "Logstash failed to start - checking status:"
    sudo systemctl status logstash
    exit 1
fi
EOF" 2>&1
