#!/bin/bash
# Download Cisco Nexus 9.3.X Documentation

DOC_DIR="/home/valentinbot/.openclaw/workspace/Documentation/Cisxo_9_3"
mkdir -p "$DOC_DIR"

echo "=== Starting Cisco Nexus 9.3 Documentation Download ==="
echo "Target directory: $DOC_DIR"
echo ""

# Array of URLs to download
declare -a URLS=(
  # Release Notes
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/release/notes/cisco-nexus-9000-nxos-release-notes-9316.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/release/notes/cisco-nexus-9000-nxos-release-notes-939.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/release/notes/931_9000_nxos_rn.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/release/notes/cisco-nexus-9000-nxos-release-notes-933.html"
  
  # Configuration Guides
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/fundamentals/configuration/guide/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/security/configuration/guide/b-cisco-nexus-9000-nx-os-security-configuration-guide-93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/qos/configuration/guide/b-cisco-nexus-9000-nx-os-quality-of-service-configuration-guide-93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/san_switching/configuration/guide/b-cisco-nexus-9000-nx-os-san-switching-configuration-guide-933.html"
  
  # Command References
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/command/reference/config/b_N9K_Config_Commands_93x.html"
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/command/reference/show/b_N9K_Show_Commands_93x.html"
  
  # Programmability
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x.html"
  
  # Upgrade Guides
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/upgrade/guide/b-cisco-nexus-9000-nx-os-software-upgrade-downgrade-guide-93x.html"
  
  # Virtual Platform
  "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/nx-osv-93-95/configuration/guide/cisco-nexus-9000v-9300v-9500v-guide-93x/m-overview.html"
)

# Download counter
downloaded=0
failed=0

for url in "${URLS[@]}"; do
  # Extract filename from URL
  filename=$(basename "$url" | sed 's/\?.*//')
  
  # Add .html extension if not present
  if [[ ! "$filename" =~ \.(html|pdf)$ ]]; then
    filename="${filename}.html"
  fi
  
  echo "Downloading: $url"
  echo "  → $filename"
  
  # Download with curl
  if curl -s -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
       --connect-timeout 10 \
       --max-time 60 \
       -o "$DOC_DIR/$filename" \
       "$url"; then
    # Check if file was actually downloaded (not empty)
    if [ -s "$DOC_DIR/$filename" ]; then
      size=$(stat -c%s "$DOC_DIR/$filename" 2>/dev/null || stat -f%z "$DOC_DIR/$filename" 2>/dev/null)
      echo "  ✓ Success (${size} bytes)"
      ((downloaded++))
    else
      echo "  ✗ Failed (empty file)"
      rm -f "$DOC_DIR/$filename"
      ((failed++))
    fi
  else
    echo "  ✗ Failed (download error)"
    ((failed++))
  fi
  echo ""
  
  # Small delay to be nice to the server
  sleep 0.5
done

echo "=== Download Complete ==="
echo "Downloaded: $downloaded files"
echo "Failed: $failed files"
echo "Location: $DOC_DIR"
ls -lh "$DOC_DIR"
