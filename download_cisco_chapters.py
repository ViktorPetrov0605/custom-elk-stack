#!/usr/bin/env python3
"""
Download all Cisco Nexus 9.3 documentation chapters
Uses SearXNG to find all chapter pages, then downloads them
"""

import subprocess
import json
import re
import os
from urllib.parse import urljoin, urlparse

DOC_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisxo_9_3"

def search_for_chapters(base_url):
    """Search for all chapter pages of a documentation set"""
    # Extract the document name pattern
    parsed = urlparse(base_url)
    base_path = parsed.path.rsplit('/', 1)[0]
    doc_name = base_path.split('/')[-1]
    
    # Search for all pages with this document name
    search_query = f"{doc_name} site:cisco.com 9.3"
    
    try:
        result = subprocess.run(
            ['node', '/home/valentinbot/.openclaw/scripts/searxng_local.js', 
             search_query, '--limit', '30'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout + result.stderr
        
        # Extract URLs
        urls = re.findall(r'https://www\.cisco\.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x[^\s\]]+\.html', output)
        
        # Filter to only include pages that seem related to this doc
        related = [u for u in urls if doc_name.replace('b-', '').replace('.html', '') in u or 'chapter' in u]
        
        return list(set(related))  # Remove duplicates
    except Exception as e:
        print(f"Search error: {e}")
        return []

def download_url(url, directory):
    """Download a single URL"""
    filename = os.path.basename(urlparse(url).path)
    if not filename.endswith('.html'):
        filename += '.html'
    
    filepath = os.path.join(directory, filename)
    
    # Skip if already exists and has content
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        print(f"  ⏭ Skipping (exists): {filename}")
        return True
    
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', '-A', 
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
             '--connect-timeout', '10',
             '--max-time', '30',
             '-o', filepath,
             url],
            timeout=35
        )
        
        if result.returncode == 0 and os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 0:
                print(f"  ✓ Downloaded: {filename} ({size} bytes)")
                return True
            else:
                print(f"  ✗ Empty file: {filename}")
                os.remove(filepath)
                return False
    except Exception as e:
        print(f"  ✗ Error: {filename} - {e}")
        return False

def main():
    # Base documentation pages that have chapters
    base_docs = [
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/fundamentals/configuration/guide/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/security/configuration/guide/b-cisco-nexus-9000-nx-os-security-configuration-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/qos/configuration/guide/b-cisco-nexus-9000-nx-os-quality-of-service-configuration-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/san_switching/configuration/guide/b-cisco-nexus-9000-nx-os-san-switching-configuration-guide-933.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x.html",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/command/reference/config/b_N9K_Config_Commands_93x.html",
    ]
    
    print("=== Cisco Nexus 9.3 Documentation Chapter Downloader ===\n")
    
    all_urls = set()
    
    # Search for chapters for each base document
    for base_url in base_docs:
        doc_name = os.path.basename(urlparse(base_url).path)
        print(f"Searching chapters for: {doc_name}")
        chapters = search_for_chapters(base_url)
        print(f"  Found {len(chapters)} related pages")
        all_urls.update(chapters)
        print()
    
    # Also add some known chapter patterns
    known_patterns = []
    base_urls = [
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/fundamentals/configuration/guide/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/security/configuration/guide/b-cisco-nexus-9000-nx-os-security-configuration-guide-93x",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/interfaces/configuration/guide/b-cisco-nexus-9000-nx-os-interfaces-configuration-guide-93x",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/layer-2-switching/configuration/guide/b-cisco-nexus-9000-nx-os-layer-2-switching-configuration-guide-93x",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/qos/configuration/guide/b-cisco-nexus-9000-nx-os-quality-of-service-configuration-guide-93x",
        "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/progammability/guide/b-cisco-nexus-9000-series-nx-os-programmability-guide-93x",
    ]
    
    for base in base_urls:
        for i in range(0, 50):  # Try chapter numbers 0-49
            known_patterns.append(f"{base}/b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x_chapter_{i:02d}.html")
            known_patterns.append(f"{base}_chapter_{i:02d}.html")
            known_patterns.append(f"{base}_chapter_{i}.html")
            known_patterns.append(f"{base}_chapter_{i:03d}.html")
    
    all_urls.update(known_patterns)
    
    print(f"\nTotal unique URLs to download: {len(all_urls)}\n")
    
    # Download all unique URLs
    downloaded = 0
    failed = 0
    skipped = 0
    
    for url in sorted(all_urls):
        filename = os.path.basename(urlparse(url).path)
        filepath = os.path.join(DOC_DIR, filename)
        
        # Skip if already downloaded
        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            skipped += 1
            continue
        
        if download_url(url, DOC_DIR):
            downloaded += 1
        else:
            failed += 1
        
        # Limit to avoid overwhelming the system
        if downloaded >= 100:
            print("\n⚠ Reached download limit (100 files)")
            break
    
    print(f"\n=== Summary ===")
    print(f"Downloaded: {downloaded}")
    print(f"Skipped (already exists): {skipped}")
    print(f"Failed: {failed}")
    print(f"Total files in directory: {len(os.listdir(DOC_DIR))}")

if __name__ == '__main__':
    main()
