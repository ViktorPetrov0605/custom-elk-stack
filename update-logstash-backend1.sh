#!/bin/bash
# Update Backend N1 (10.4.4.21) Logstash configuration

echo "=== BACKEND N1: Updating Logstash Config ==="

# Create the new config
ssh -p 2332 telehouse@10.4.4.21 << 'EOF'
PASSWORD="T3l3h0us#"
echo "Creating backup of current config..."
sudo cp /etc/logstash/conf.d/logstash-unified-netflow.conf /etc/logstash/conf.d/logstash-unified-netflow.conf.backup.$(date +%Y%m%d)

echo "Writing new multi-device config..."
sudo tee /etc/logstash/conf.d/logstash-unified-netflow.conf > /dev/null <<'LOGBACK'
# Unified Logstash Configuration for NetFlow (Juniper) - Multi-Device Support
# Backend N1 (10.4.4.21)

input {
  udp {
    port => 2050
    type => "netflow"
    codec => netflow {
      versions => [9]
    }
    receive_buffer_bytes => 16777216
    workers => 8
  }
}

filter {
  # Device identification based on exporter IP
  if [host] == "10.4.4.93" {
    mutate {
      add_field => {
        "[device][name]" => "juniper-bix-backend1-1"
        "[device][ip]" => "10.4.4.93"
        "[device][location]" => "bix-backend1"
        "[device][index]" => "1"
        "[device][type]" => "router"
        "[event][type]" => "netflow"
        "[observer][type]" => "netflow_exporter"
        "[sampling][rate]" => 4096
        "[sampling][algorithm]" => 1
      }
    }
  } else {
    mutate {
      add_field => {
        "[device][name]" => "unknown-netflow-device"
        "[device][ip]" => "%{host}"
        "[device][type]" => "router"
        "[event][type]" => "netflow"
        "[observer][type]" => "netflow_exporter"
        "[sampling][rate]" => 4096
        "[sampling][algorithm]" => 1
      }
    }
  }

  # NetFlow v9 field mapping
  if [netflow] {
    if [netflow][ipv4_src_addr] {
      mutate { add_field => { "[source][ip]" => "%{[netflow][ipv4_src_addr]}" } }
    }
    if [netflow][ipv4_dst_addr] {
      mutate { add_field => { "[destination][ip]" => "%{[netflow][ipv4_dst_addr]}" } }
    }
    
    if [netflow][l4_src_port] {
      mutate { add_field => { "[source][port]" => "%{[netflow][l4_src_port]}" } }
    }
    if [netflow][l4_dst_port] {
      mutate { add_field => { "[destination][port]" => "%{[netflow][l4_dst_port]}" } }
    }
    
    if [netflow][protocol] {
      mutate { add_field => { "[network][iana_number]" => "%{[netflow][protocol]}" } }
      translate {
        field => "[network][iana_number]"
        destination => "[network][transport]"
        dictionary => {
          "6" => "tcp"
          "17" => "udp"
          "1" => "icmp"
          "47" => "gre"
          "50" => "esp"
          "51" => "ah"
        }
        fallback => "other"
      }
    }
    
    if [netflow][input_snmp] {
      mutate { add_field => { "[interface][input]" => "%{[netflow][input_snmp]}" } }
    }
    if [netflow][output_snmp] {
      mutate { add_field => { "[interface][output]" => "%{[netflow][output_snmp]}" } }
    }
    
    if [netflow][src_as] {
      mutate { add_field => { "[source][as][number]" => "%{[netflow][src_as]}" } }
    }
    if [netflow][dst_as] {
      mutate { add_field => { "[destination][as][number]" => "%{[netflow][dst_as]}" } }
    }
    
    if [netflow][in_bytes] {
      ruby {
        code => "event.set('[network][bytes]', event.get('[netflow][in_bytes]').to_i * 4096)"
      }
    }
    if [netflow][in_pkts] {
      ruby {
        code => "event.set('[network][packets]', event.get('[netflow][in_pkts]').to_i * 4096)"
      }
    }
    
    mutate { remove_field => [ "[netflow]" ] }
  }
  
  if ![network][bytes] {
    mutate { add_field => { "[network][bytes]" => 0 } }
  }
  if ![network][packets] {
    mutate { add_field => { "[network][packets]" => 0 } }
  }
  
  mutate {
    convert => {
      "[network][bytes]" => "integer"
      "[network][packets]" => "integer"
      "[source][port]" => "integer"
      "[destination][port]" => "integer"
      "[source][as][number]" => "integer"
      "[destination][as][number]" => "integer"
      "[interface][input]" => "integer"
      "[interface][output]" => "integer"
      "[sampling][rate]" => "integer"
      "[sampling][algorithm]" => "integer"
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
