#!/usr/bin/env python3
"""
Cisco Configuration Guides Processor - Agent #2
Processes HTML configuration guides to clean Markdown
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

SOURCE_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3/"
TARGET_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent2_Config_Guides/"

class HTMLCleaner(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer'}
        self.skip_classes = ['cisco-header', 'navigation', 'breadcrumb', 'toolbar', 
                            'related-links', 'prev-next', 'copyright', 'feedback']
        self.in_skip = 0
        self.current_tag = None
        self.current_attrs = {}
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_tag = tag
        self.current_attrs = attrs_dict
        
        # Check if we should skip this tag
        if tag in self.skip_tags:
            self.in_skip += 1
            return
            
        # Check class-based skipping
        class_attr = attrs_dict.get('class', '')
        if class_attr:
            for skip_class in self.skip_classes:
                if skip_class in class_attr:
                    self.in_skip += 1
                    return
        
        # Handle headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.text.append(f"\n{'#' * level} ")
        elif tag == 'p':
            self.text.append("\n\n")
        elif tag == 'br':
            self.text.append("\n")
        elif tag in ['ul', 'ol']:
            self.text.append("\n")
        elif tag == 'li':
            self.text.append("\n- ")
        elif tag == 'code':
            self.text.append("`")
        elif tag == 'pre':
            self.text.append("\n```\n")
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            if href:
                self.text.append(f"[{href}] ")
        elif tag == 'strong' or tag == 'b':
            self.text.append("**")
        elif tag == 'em' or tag == 'i':
            self.text.append("*")
        elif tag == 'table':
            self.text.append("\n")
            
    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.in_skip -= 1
            return
            
        if self.in_skip > 0:
            # Check if this is the closing tag for a skipped element
            class_attr = self.current_attrs.get('class', '')
            for skip_class in self.skip_classes:
                if skip_class in class_attr:
                    self.in_skip -= 1
                    return
                    
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.text.append("\n")
        elif tag == 'p':
            self.text.append("\n")
        elif tag == 'pre':
            self.text.append("\n```\n")
        elif tag == 'code':
            self.text.append("`")
        elif tag == 'strong' or tag == 'b':
            self.text.append("**")
        elif tag == 'em' or tag == 'i':
            self.text.append("*")
        elif tag == 'table':
            self.text.append("\n")
            
    def handle_data(self, data):
        if self.in_skip == 0:
            # Clean up whitespace but preserve structure
            cleaned = data.replace('\r\n', ' ').replace('\n', ' ')
            self.text.append(cleaned)
            
    def get_text(self):
        text = ''.join(self.text)
        # Clean up multiple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        return text.strip()


def extract_title(html_content, filename):
    """Extract title from HTML"""
    # Try to find title tag
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        # Clean up Cisco title noise
        title = re.sub(r' - Cisco$', '', title)
        title = re.sub(r'\s+', ' ', title)
        return title
    
    # Try h1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)
    if h1_match:
        h1_text = re.sub(r'<[^>]+>', '', h1_match.group(1))
        return h1_text.strip()
    
    # Fallback to filename
    return filename.replace('.html', '').replace('-', ' ').title()


def generate_tags(filename, title, content):
    """Generate relevant tags based on content"""
    tags = []
    text_lower = (title + ' ' + content[:5000]).lower()
    
    # Guide type tags
    if 'interface' in filename.lower():
        tags.extend(['interfaces', 'ethernet', 'port-channels', 'switchport'])
    if 'layer-2' in filename.lower() or 'layer_2' in filename.lower():
        tags.extend(['layer2', 'vlan', 'trunk', 'stp', 'spanning-tree'])
    if 'security' in filename.lower():
        tags.extend(['security', 'acl', 'radius', 'tacacs', 'aaa', 'ssh', 'tls'])
    if 'quality-of-service' in filename.lower() or 'qos' in filename.lower():
        tags.extend(['qos', 'quality-of-service', 'marking', 'queuing', 'classification'])
    if 'san-switching' in filename.lower():
        tags.extend(['san', 'fcoe', 'fiber-channel', 'storage', 'vsan'])
    if 'vxlan' in filename.lower():
        tags.extend(['vxlan', 'overlay', 'evpn', 'tunneling'])
    if 'unicast-routing' in filename.lower():
        tags.extend(['routing', 'unicast', 'bgp', 'ospf', 'eigrp', 'static-routes'])
    if 'multicast-routing' in filename.lower():
        tags.extend(['multicast', 'pim', 'igmp', 'routing'])
    if 'fundamentals' in filename.lower():
        tags.extend(['fundamentals', 'basics', 'getting-started'])
    if 'system-management' in filename.lower():
        tags.extend(['system-management', 'monitoring', 'logging', 'snmp'])
        
    # Content-based tags
    if 'ethernet' in text_lower:
        tags.append('ethernet')
    if 'port-channel' in text_lower or 'port channel' in text_lower:
        tags.append('port-channels')
    if 'vlan' in text_lower:
        tags.append('vlan')
    if 'vxlan' in text_lower:
        tags.append('vxlan')
    if 'acl' in text_lower or 'access list' in text_lower:
        tags.append('acl')
    if 'bgp' in text_lower:
        tags.append('bgp')
    if 'ospf' in text_lower:
        tags.append('ospf')
    if 'fcoe' in text_lower:
        tags.append('fcoe')
        
    # Remove duplicates while preserving order
    seen = set()
    unique_tags = []
    for tag in tags:
        if tag not in seen:
            seen.add(tag)
            unique_tags.append(tag)
    
    return unique_tags[:12]  # Limit to 12 tags


def process_html_file(filepath):
    """Process a single HTML file to Markdown"""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()
    
    # Extract title
    title = extract_title(html_content, filename)
    
    # Parse and clean HTML
    cleaner = HTMLCleaner()
    try:
        cleaner.feed(html_content)
        clean_text = cleaner.get_text()
    except Exception as e:
        clean_text = f"[Error parsing HTML: {e}]\n\n"
        # Fallback: strip tags manually
        clean_text += re.sub(r'<[^>]+>', '', html_content)
    
    # Generate tags
    tags = generate_tags(filename, title, clean_text)
    
    # Build Markdown content
    markdown = f"""# {title}

**Source:** `{filename}`
**Tags:** {', '.join(tags)}

---

{clean_text}
"""
    
    return {
        'title': title,
        'filename': filename,
        'tags': tags,
        'markdown': markdown
    }


def generate_output_filename(filename):
    """Generate clean output filename"""
    # Remove .html extension
    name = filename.replace('.html', '')
    
    # Extract guide type and section
    parts = name.split('_')
    
    # Determine the main guide category
    if 'interfaces' in name.lower():
        category = 'interfaces'
    elif 'layer-2' in name.lower():
        category = 'layer2'
    elif 'security' in name.lower():
        category = 'security'
    elif 'quality-of-service' in name.lower() or 'qos' in name.lower():
        category = 'qos'
    elif 'san-switching' in name.lower():
        category = 'san'
    elif 'vxlan' in name.lower():
        category = 'vxlan'
    elif 'unicast-routing' in name.lower():
        category = 'unicast-routing'
    elif 'multicast-routing' in name.lower():
        category = 'multicast-routing'
    elif 'fundamentals' in name.lower():
        category = 'fundamentals'
    elif 'system-management' in name.lower():
        category = 'system-management'
    else:
        category = 'other'
    
    # Build output path
    output_name = name.replace('b-cisco-nexus-9000-nx-os-', '').replace('b-cisco-nexus-9000-series-nx-os-', '')
    output_name = re.sub(r'[-_]+', '-', output_name).strip('-')
    
    return f"{category}/{output_name}.md"


def main():
    # Get all configuration guide files
    all_files = [f for f in os.listdir(SOURCE_DIR) 
                 if f.startswith('b-cisco-nexus-9000') and 'configuration-guide' in f]
    all_files.sort()
    
    total = len(all_files)
    print(f"Found {total} configuration guide files to process")
    
    index = {}
    processed = 0
    errors = []
    
    for i, filename in enumerate(all_files, 1):
        filepath = os.path.join(SOURCE_DIR, filename)
        
        try:
            # Process the file
            result = process_html_file(filepath)
            
            # Generate output path
            output_rel_path = generate_output_filename(filename)
            output_path = os.path.join(TARGET_DIR, output_rel_path)
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write Markdown file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result['markdown'])
            
            # Add to index
            guide_key = filename.replace('.html', '')
            index[guide_key] = {
                'file': output_rel_path,
                'title': result['title'],
                'tags': result['tags']
            }
            
            processed += 1
            
            # Progress report every 5 files
            if i % 5 == 0 or i == total:
                pct = (i / total) * 100
                print(f"[{i}/{total}] {pct:.1f}% - Processed: {filename}")
                
        except Exception as e:
            errors.append(f"{filename}: {str(e)}")
            print(f"ERROR processing {filename}: {e}")
    
    # Write index.json
    index_path = os.path.join(TARGET_DIR, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_files': total,
            'processed': processed,
            'errors': errors,
            'guides': index
        }, f, indent=2)
    
    print(f"\n=== COMPLETE ===")
    print(f"Processed: {processed}/{total} files")
    print(f"Errors: {len(errors)}")
    print(f"Index saved to: {index_path}")
    
    if errors:
        print("\nErrors encountered:")
        for err in errors:
            print(f"  - {err}")


if __name__ == '__main__':
    main()
