#!/usr/bin/env python3
"""
Recursive Spider for Cisco Nexus 9.3 Documentation
Downloads all linked pages from the documentation
"""

import sys
import os
import re
import time
import subprocess
from urllib.parse import urljoin, urlparse, urldefrag
from collections import deque

# Configuration
DOC_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3"
MAX_DEPTH = 3
MAX_FILES = 500
CISCO_DOMAINS = [
    'www.cisco.com',
    'cisco.com',
]

# Track downloaded and queued URLs
downloaded = set()
queue = deque()


def normalize_url(url):
    """Normalize URL - remove fragment, normalize path"""
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    
    # Only process HTTP/HTTPS
    if parsed.scheme not in ('http', 'https'):
        return None
    
    # Must be cisco.com domain
    if parsed.netloc not in CISCO_DOMAINS:
        return None
    
    # Focus on Nexus 9.3 documentation
    if '/nexus9000/sw/93x/' not in url and '/nexus3000/sw/93x/' not in url:
        return None
    
    # Skip non-HTML resources
    path = parsed.path.lower()
    if any(path.endswith(ext) for ext in ['.pdf', '.zip', '.tar', '.gz', '.jpg', '.png', '.gif', '.css', '.js']):
        return None
    
    # Add .html if no extension
    if not path.endswith('.html') and not path.endswith('/'):
        url += '.html'
    
    return url


def extract_links(filepath, base_url):
    """Extract all links from a downloaded HTML file"""
    links = []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find all href links
        href_pattern = r'href="([^"]+)"'
        for match in re.finditer(href_pattern, content):
            href = match.group(1)
            absolute_url = urljoin(base_url, href)
            normalized = normalize_url(absolute_url)
            if normalized:
                links.append(normalized)
        
        # Find action links
        action_pattern = r'action="([^"]+)"'
        for match in re.finditer(action_pattern, content):
            href = match.group(1)
            absolute_url = urljoin(base_url, href)
            normalized = normalize_url(absolute_url)
            if normalized:
                links.append(normalized)
                
    except Exception as e:
        print(f"Error extracting links from {filepath}: {e}")
    
    return links


def download_url(url, directory):
    """Download a single URL using curl"""
    # Create safe filename
    parsed = urlparse(url)
    path = parsed.path
    
    # Extract last part of path as filename
    filename = os.path.basename(path)
    if not filename or filename == '':
        filename = 'index.html'
    if not filename.endswith('.html'):
        filename += '.html'
    
    # Make unique if needed by adding hash
    filepath = os.path.join(directory, filename)
    counter = 1
    original_filename = filename
    while os.path.exists(filepath) and counter < 100:
        name, ext = os.path.splitext(original_filename)
        filename = f"{name}_{counter:02d}{ext}"
        filepath = os.path.join(directory, filename)
        counter += 1
    
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', 
             '-A', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
             '--connect-timeout', '15',
             '--max-time', '45',
             '-o', filepath,
             url],
            timeout=60,
            capture_output=True
        )
        
        if result.returncode == 0 and os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 100:  # Minimum valid HTML size
                return filepath, size
            else:
                os.remove(filepath)
                return None, 0
        else:
            return None, 0
            
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout: {url}")
        return None, 0
    except Exception as e:
        print(f"  ✗ Error: {url} - {e}")
        return None, 0


def main():
    print("=" * 70)
    print("CISCO NEXUS 9.3 DOCUMENTATION RECURSIVE SPIDER")
    print("=" * 70)
    
    # Ensure directory exists
    os.makedirs(DOC_DIR, exist_ok=True)
    
    # Seed URLs - start with already downloaded files
    seed_files = [f for f in os.listdir(DOC_DIR) if f.endswith('.html')]
    print(f"\nFound {len(seed_files)} seed files\n")
    
    # Build initial queue from existing files
    for seed_file in seed_files:
        seed_path = os.path.join(DOC_DIR, seed_file)
        
        # Determine the original URL from the file
        # Cisco docs follow a pattern, construct URL from filepath
        # For simplicity, construct based on common patterns
        base_url = f"https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/93x/"
        
        # Extract links from seed file
        links = extract_links(seed_path, base_url)
        for link in links:
            if link not in downloaded:
                queue.append((link, 1))  # (url, depth)
    
    print(f"Initial queue size: {len(queue)} URLs")
    print(f"Max depth: {MAX_DEPTH}")
    print(f"Max files: {MAX_FILES}")
    print()
    
    # Process queue
    total_downloaded = len(seed_files)
    new_downloaded = 0
    failed = 0
    
    while queue and total_downloaded < MAX_FILES:
        url, depth = queue.popleft()
        
        if url in downloaded:
            continue
        
        if depth > MAX_DEPTH:
            continue
        
        downloaded.add(url)
        
        # Download
        print(f"[{total_downloaded + 1}/{MAX_FILES}] Depth {depth}: {url[:80]}...")
        filepath, size = download_url(url, DOC_DIR)
        
        if filepath:
            print(f"  ✓ Saved: {os.path.basename(filepath)} ({size} bytes)")
            total_downloaded += 1
            new_downloaded += 1
            
            # Extract more links from this file if not at max depth
            if depth < MAX_DEPTH:
                new_links = extract_links(filepath, url)
                for link in new_links:
                    if link not in downloaded:
                        queue.append((link, depth + 1))
            
            # Rate limiting - be nice to Cisco
            time.sleep(0.3)
        else:
            print(f"  ✗ Failed")
            failed += 1
    
    # Summary
    print()
    print("=" * 70)
    print("DOWNLOAD COMPLETE")
    print("=" * 70)
    print(f"Total files in directory: {len(os.listdir(DOC_DIR))}")
    print(f"New files downloaded: {new_downloaded}")
    print(f"Failed downloads: {failed}")
    print(f"Total size:")
    
    result = subprocess.run(['du', '-sh', DOC_DIR], capture_output=True, text=True)
    print(result.stdout.strip())


if __name__ == '__main__':
    main()
