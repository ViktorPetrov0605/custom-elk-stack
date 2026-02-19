# Session Lessons - 2026-02-19

## Technical Discoveries

### 1. Logstash `mutate` Type Mismatch
- **Observation:** `mutate { copy => { "[field]" => "[target]" } }` failed with `Cannot cast org.jruby.RubyArray to org.jruby.RubyString`.
- **Cause:** In some Logstash environments/codecs, the `[host]` or `[host][ip]` field is an **Array** (e.g., `["1.2.3.4"]`), and the `mutate` filter expects a String when copying to certain targets or when concatenated.
- **Fix:** Use a `ruby` filter to check the type and convert to string:
  ```ruby
  ruby {
    code => "
      val = event.get('[host][ip]')
      if val.is_a?(Array); event.set('[target]', val[0].to_s); else; event.set('[target]', val.to_s); end
    "
  }
  ```

### 2. Docker Service Discovery / NAT for NetFlow
- **Observation:** When running Logstash in a Docker container behind a bridge network, the `[host][ip]` or `[@metadata][ip_address]` often shows the **Docker Gateway IP** (e.g., `172.23.0.1`) rather than the true external source IP of the UDP packets.
- **Cause:** Docker NAT hides the original source IP unless using `network_mode: host`.
- **Mitigation:** If `network_mode: host` is not feasible, implement a mapping in Logstash to translate known gateway IPs back to the expected device IP based on the deployment context.
- **Pattern:** `if [device][ip] == "172.23.0.1" { replace => { "[device][ip]" => "10.4.4.93" } }`

### 3. Logstash NetFlow Metadata
- **Deep Dive:** `@metadata[ip_address]` is the most reliable field for the source packet IP in the official `netflow` codec, but it must be manually moved into the event body to be indexed/used in later filters (like multipliers).

## Corrective Actions
- **Rule:** Never assume `[host][ip]` is a string. Always verify or cast for `mutate` operations.
- **Rule:** When deploying to dual backends with different SSH ports, verify availability before bulk deployment. (10.4.4.21:2332 vs 10.4.4.90:22).
