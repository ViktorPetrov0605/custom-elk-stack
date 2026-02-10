#!/usr/bin/env python3
"""
Cisco Nexus 9.3.X Command Reference Processor
Agent #3: Processes Config and Show command reference files
Improved parser for Cisco HTML command reference structure
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3/"
TARGET_CONF_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent3_Command_Reference/Config_Commands"
TARGET_SHOW_DIR = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent3_Command_Reference/Show_Commands"


class CommandProcessor:
    def __init__(self):
        self.total_files = 0
        self.processed_files = 0
        self.total_commands = 0
        self.processed_commands = 0
        self.large_files = []
        self.current_file_commands = 0
        self.start_time = datetime.now()
        self.status_file = "/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent3_Command_Reference/processing_status.json"

    def save_status(self, message):
        """Save current processing status"""
        status = {
            'timestamp': datetime.now().isoformat(),
            'message': message,
            'processed_files': self.processed_files,
            'total_files': self.total_files,
            'total_commands': self.total_commands,
            'processed_commands': self.processed_commands,
            'large_files': len(self.large_files)
        }
        with open(self.status_file, 'w') as f:
            json.dump(status, f, indent=2)

    def strip_html_tags(self, html):
        """Remove HTML tags from text"""
        # First replace common block elements with newlines
        text = re.sub(r'</(p|div|section|article|tr|li|h[1-6])>', '\n', html, flags=re.IGNORECASE)
        # Remove remaining tags
        text = re.sub(r'<[^>]+>', '', text)
        # Unescape HTML entities
        text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        text = text.replace('&quot;', '"').replace('&#39;', "'")
        text = text.replace('&nbsp;', ' ')
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    def extract_command_details(self, article_html):
        """Extract command details from an article section"""
        # Extract command name from h2
        cmd_match = re.search(r'<h2[^>]*class=["\'][^"\']*topictitle2[^"\']*["\'][^>]*>([^<]+)</h2>', article_html, re.IGNORECASE)
        if not cmd_match:
            cmd_match = re.search(r'<h2[^>]*>([^<]+)</h2>', article_html, re.IGNORECASE)
        
        if not cmd_match:
            return None
        
        cmd_name = self.strip_html_tags(cmd_match.group(1)).strip()
        
        # Extract syntax from first <p class="p"> with command-like content
        syntax_patterns = [
            r'<p class="p">([^<]+(?:<[^/]|</[^p]){0,200})</p>',  # First paragraph after heading
            r'<p[^>]*>\s*([^<]{5,200})\s*</p>'  # Any p with reasonable content
        ]
        
        syntax = ""
        for pattern in syntax_patterns:
            syn_match = re.search(pattern, article_html, re.IGNORECASE | re.DOTALL)
            if syn_match:
                potential_syntax = self.strip_html_tags(syn_match.group(1)).strip()
                # Verify it looks like a command (contains alphanumeric and spaces)
                if len(potential_syntax) > 3 and re.match(r'^[\w\s\-\|\(\)\<\>\{\}\[\]\*\?\/\.\:;,]+$', potential_syntax):
                    syntax = potential_syntax
                    break
        
        # Extract parameter table rows
        params = []
        table_rows = re.findall(r'<tr>(.*?)</tr>', article_html, re.IGNORECASE | re.DOTALL)
        for row in table_rows:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.IGNORECASE | re.DOTALL)
            if len(cells) >= 2:
                param_name = self.strip_html_tags(cells[0]).strip()
                param_desc = self.strip_html_tags(cells[1]).strip()
                if param_name and param_desc:
                    params.append((param_name, param_desc))
        
        # Extract command mode info
        mode = ""
        mode_match = re.search(r'<strong[^>]*>Command Mode.*?</strong>.*?<p[^>]*>(.*?)</p>', article_html, re.IGNORECASE | re.DOTALL)
        if mode_match:
            mode = self.strip_html_tags(mode_match.group(1)).strip()
        if not mode:
            # Try ul/li pattern
            mode_match = re.search(r'<strong[^>]*>Command Mode.*?</strong>.*?<li[^>]*>(.*?)</li>', article_html, re.IGNORECASE | re.DOTALL)
            if mode_match:
                mode = self.strip_html_tags(mode_match.group(1)).strip()
        
        # Extract command history/version info
        history = []
        hist_match = re.search(r'<strong[^>]*>Command History.*?</strong>(.*?)</section>', article_html, re.IGNORECASE | re.DOTALL)
        if hist_match:
            hist_section = hist_match.group(1)
            hist_rows = re.findall(r'<tr>(.*?)</tr>', hist_section, re.IGNORECASE | re.DOTALL)
            for row in hist_rows[1:] if len(hist_rows) > 1 else hist_rows:  # Skip header if present
                cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.IGNORECASE | re.DOTALL)
                if len(cells) >= 2:
                    version = self.strip_html_tags(cells[0]).strip()
                    change = self.strip_html_tags(cells[1]).strip()
                    if version and change:
                        history.append((version, change))
        
        # Extract usage guidelines
        guidelines = ""
        guide_match = re.search(r'<strong[^>]*>Usage Guidelines.*?</strong>.*?<p[^>]*>(.*?)</p>', article_html, re.IGNORECASE | re.DOTALL)
        if guide_match:
            guidelines = self.strip_html_tags(guide_match.group(1)).strip()
        
        return {
            'name': cmd_name,
            'syntax': syntax,
            'parameters': params,
            'mode': mode,
            'history': history,
            'guidelines': guidelines
        }

    def parse_commands(self, content):
        """Parse all commands from HTML content"""
        commands = []
        
        # Find all article sections with command details
        # Pattern: <article class="topic reference nested1" ... id="wpXXXX">
        articles = re.findall(r'<article[^>]*class=["\'][^"\']*topic[^"\']*["\'][^>]*id=["\'](wp\d+)["\'][^>]*>(.*?)</article>', 
                             content, re.IGNORECASE | re.DOTALL)
        
        for article_id, article_content in articles:
            cmd_details = self.extract_command_details(article_content)
            if cmd_details:
                cmd_details['id'] = article_id
                commands.append(cmd_details)
        
        return commands

    def format_command_markdown(self, cmd, source_file):
        """Format a command as markdown"""
        cmd_name = cmd['name'].replace('|', '&#124;')
        syntax = cmd.get('syntax', '').replace('|', '&#124;')
        
        md = f"""# Command: {cmd_name}

## Syntax
```
{syntax}
```

"""
        # Add syntax description/parameters
        if cmd.get('parameters'):
            md += "### Syntax Description\n\n"
            md += "| Parameter | Description |\n"
            md += "|-----------|-------------|\n"
            for param_name, param_desc in cmd['parameters'][:10]:  # Limit to first 10
                md += f"| {param_name} | {param_desc} |\n"
            md += "\n"
        
        # Add command mode
        if cmd.get('mode'):
            md += f"**Command Mode:** {cmd['mode']}\n\n"
        
        # Add usage guidelines as description
        if cmd.get('guidelines'):
            md += f"## Description\n{cmd['guidelines']}\n\n"
        
        # Add command history
        if cmd.get('history'):
            md += "### Command History\n\n"
            md += "| Release | Modification |\n"
            md += "|---------|--------------|\n"
            for version, change in cmd['history'][:5]:
                md += f"| {version} | {change} |\n"
            md += "\n"
        
        # Determine tags
        tags = self.generate_tags(cmd['name'])
        
        md += f"""**Source:** {source_file}
**Tags:** {', '.join(tags)}
**Command ID:** {cmd.get('id', 'N/A')}

---

"""
        return md

    def generate_tags(self, cmd_name):
        """Generate relevant tags for a command"""
        tags = []
        cmd_lower = cmd_name.lower()
        
        # Mode detection
        if 'show ' in cmd_lower or cmd_lower.startswith('show'):
            tags.append('show-mode')
        else:
            tags.append('config-mode')
        
        # Feature detection
        if any(x in cmd_lower for x in ['interface', 'eth', 'port', 'vlan', 'switchport']):
            tags.append('interface')
        if any(x in cmd_lower for x in ['bgp', 'ospf', 'eigrp', 'isis', 'rip', 'route', 'routing']):
            tags.append('routing')
        if any(x in cmd_lower for x in ['acl', 'access-list', 'ip access']):
            tags.append('security')
        if any(x in cmd_lower for x in ['qos', 'class', 'policy', 'bandwidth', 'priority']):
            tags.append('qos')
        if any(x in cmd_lower for x in ['span', 'erspan', 'monitor session']):
            tags.append('monitoring')
        if any(x in cmd_lower for x in ['vrf', 'vni', 'vxlan']):
            tags.append('overlay')
        if any(x in cmd_lower for x in ['vpc', 'peer-link']):
            tags.append('vpc')
        if any(x in cmd_lower for x in ['lacp', 'port-channel']):
            tags.append('layer2')
        if any(x in cmd_lower for x in ['ip', 'ipv4', 'ipv6', 'tcp', 'udp']):
            tags.append('network')
        if any(x in cmd_lower for x in ['ntp', 'clock', 'time']):
            tags.append('system')
        if any(x in cmd_lower for x in ['snmp', 'syslog', 'logging']):
            tags.append('management')
        if any(x in cmd_lower for x in ['bfd']):
            tags.append('bfd')
        if any(x in cmd_lower for x in ['boot', 'bootmode']):
            tags.append('boot')
        
        # First letter tag
        first_char = cmd_name[0].upper() if cmd_name and cmd_name[0].isalpha() else 'Other'
        tags.append(f'{first_char}-commands')
        
        return tags

    def get_chapter_letter(self, filename):
        """Extract chapter letter from filename"""
        match = re.search(r'chapter_0*([\d]+)\.html', filename)
        if match:
            chapter_digits = match.group(1)
            # Parse the binary-like pattern to get letter
            if len(chapter_digits) == 1:
                return chr(ord('A') + int(chapter_digits))
            elif len(chapter_digits) >= 2:
                # Multi-digit pattern A=01, B=010, C=011, etc.
                mapping = {
                    '1': 'A', '01': 'A',
                    '010': 'B', '011': 'C', 
                    '0100': 'D', '0101': 'E',
                    '0110': 'F', '0111': 'G',
                    '01000': 'H', '01001': 'I',
                    '01010': 'J', '01011': 'K',
                    '01100': 'L', '01101': 'M',
                    '01110': 'N', '01111': 'O',
                    '010000': 'P', '010001': 'Q',
                    '010010': 'R', '010011': 'S',
                    '010100': 'T', '010101': 'U',
                    '010110': 'V', '010111': 'W',
                    '011000': 'X'
                }
                return mapping.get(chapter_digits, f"Group-{chapter_digits}")
        
        lower_name = filename.lower()
        if 'preface' in lower_name:
            return "Preface"
        if 'clt' in lower_name:
            return "Index"
        if 'new-changed' in lower_name:
            return "New/Changed"
        if any(x in lower_name for x in ['_01.html', '_02.html']):
            return "Introduction"
        
        return "Reference"

    def process_single_file(self, filepath, target_dir, is_config=True):
        """Process a single HTML file"""
        try:
            filename = os.path.basename(filepath)
            file_size = os.path.getsize(filepath)
            
            # Track large files
            if file_size > 2 * 1024 * 1024:  # 2MB
                self.large_files.append((filename, file_size))

            # Read file
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Extract chapter title
            chapter_title = "Command Reference"
            title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
            if title_match:
                chapter_title = title_match.group(1)
                chapter_title = re.sub(r'Cisco Nexus 9000 Series NX-OS Command Reference.*-\s*', '', chapter_title)
                chapter_title = re.sub(r'\s*-\s*Cisco$', '', chapter_title)
            
            h2_match = re.search(r'<h2[^>]*class=["\'][^"\']*chapter-title[^"\']*["\'][^>]*>([^<]+)</h2>', content, re.IGNORECASE)
            if h2_match:
                h2_text = self.strip_html_tags(h2_match.group(1))
                if h2_text:
                    chapter_title = h2_text
            
            chapter_letter = self.get_chapter_letter(filename)
            
            # Skip files that are not command chapters
            lower_name = filename.lower()
            if any(x in lower_name for x in ['preface', '_01.html', '_02.html', 'clt', 'new-changed', 'changed-93']):
                # These are navigation/index files - process differently
                return self.process_navigation_file(filename, chapter_title, content, target_dir, is_config)
            
            # Parse commands
            commands = self.parse_commands(content)
            self.current_file_commands = len(commands)
            self.total_commands += len(commands)
            
            if commands:
                # Create markdown
                md_content = f"""# {chapter_title}

**Source File:** {filename}
**Type:** {'Configuration' if is_config else 'Show'} Commands  
**Chapter:** {chapter_letter} Commands  
**Total Commands:** {len(commands)}

## Command List

"""
                for cmd in commands:
                    cmd_name = cmd['name'].replace('|', '\\|')
                    md_content += f"- `{cmd_name}`\n"
                
                md_content += "\n---\n\n## Detailed Command Reference\n\n"
                
                for cmd in commands:
                    md_content += self.format_command_markdown(cmd, filename)
                    self.processed_commands += 1
                
                # Write output
                output_filename = filename.replace('.html', '.md')
                output_path = os.path.join(target_dir, output_filename)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                return len(commands)
            else:
                # No commands found - create reference file
                output_filename = filename.replace('.html', '.md')
                output_path = os.path.join(target_dir, output_filename)
                
                md_content = f"""# {chapter_title}

**Source File:** {filename}
**Type:** {'Configuration' if is_config else 'Show'} Commands  
**Chapter:** {chapter_letter}

This file does not contain individual command documentation entries. It may contain:
- Navigation links
- Table of contents
- Reference information

---

**Note:** {len(content)} characters of HTML content preserved.
"""
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                return 0
                
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            import traceback
            traceback.print_exc()
            return 0

    def process_navigation_file(self, filename, chapter_title, content, target_dir, is_config):
        """Process navigation/index files"""
        try:
            # Extract links
            links = re.findall(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>([^<]+)</a>', content, re.IGNORECASE)
            
            # Clean up the text content
            content_text = self.strip_html_tags(content)[:1500]  # First 1500 chars
            
            output_filename = filename.replace('.html', '.md')
            output_path = os.path.join(target_dir, output_filename)
            
            md_content = f"""# {chapter_title}

**Source File:** {filename}
**Type:** {'Configuration' if is_config else 'Show'} Commands - Navigation/Index

## Content Summary

```
{content_text}
```

## Document Structure

This file contains navigation and reference material for the Cisco Nexus 9000 NX-OS Command Reference.

---

**Note:** Original navigation file processed. Contains {len(links)} links to other sections.
"""
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            return 0
        except Exception as e:
            print(f"Error processing navigation file {filename}: {e}")
            return 0

    def process_all_files(self):
        """Process all command reference files"""
        # Get lists of files
        config_files = sorted([f for f in os.listdir(SOURCE_DIR) 
                              if f.startswith('b_N9K_Config_Commands') and f.endswith('.html')])
        show_files = sorted([f for f in os.listdir(SOURCE_DIR) 
                            if f.startswith('b_N9K_Show_Commands') and f.endswith('.html')])
        clt_files = [f for f in os.listdir(SOURCE_DIR) 
                     if 'CLT' in f and f.endswith('.html')]
        eot_files = [f for f in os.listdir(SOURCE_DIR) 
                    if 'EOTResponsiveContent' in f and f.endswith('.html')]
        
        self.total_files = len(config_files) + len(show_files) + len(clt_files) + len(eot_files)
        
        print(f"=" * 70)
        print("Cisco Nexus 9.3.X Command Reference Processor - Agent #3")
        print(f"=" * 70)
        print(f"Source: {SOURCE_DIR}")
        print(f"Config Target: {TARGET_CONF_DIR}")
        print(f"Show Target: {TARGET_SHOW_DIR}")
        print(f"-" * 70)
        print(f"Total files: {self.total_files}")
        print(f"  Config command files: {len(config_files)}")
        print(f"  Show command files: {len(show_files)}")
        print(f"  CLT/Index files: {len(clt_files)}")
        print(f"  EOT/Syntax files: {len(eot_files)}")
        print(f"=" * 70)
        print()
        
        # Process Config Commands
        print("[Phase 1/4] Processing Configuration Command Reference...")
        for i, filename in enumerate(config_files, 1):
            filepath = os.path.join(SOURCE_DIR, filename)
            count = self.process_single_file(filepath, TARGET_CONF_DIR, is_config=True)
            self.processed_files += 1
            
            if i % 5 == 0 or i == len(config_files):
                pct = (i / len(config_files)) * 100
                msg = f"Config: {i}/{len(config_files)} ({pct:.1f}%) | Commands: {self.processed_commands}"
                print(f"  {msg}")
                self.save_status(msg)
        
        # Process Show Commands
        print("\n[Phase 2/4] Processing Show Command Reference...")
        for i, filename in enumerate(show_files, 1):
            filepath = os.path.join(SOURCE_DIR, filename)
            count = self.process_single_file(filepath, TARGET_SHOW_DIR, is_config=False)
            self.processed_files += 1
            
            if i % 5 == 0 or i == len(show_files):
                pct = (i / len(show_files)) * 100
                msg = f"Show: {i}/{len(show_files)} ({pct:.1f}%) | Commands: {self.processed_commands}"
                print(f"  {msg}")
                self.save_status(msg)
        
        # Process CLT files
        print("\n[Phase 3/4] Processing Index/CLT files...")
        for i, filename in enumerate(clt_files, 1):
            filepath = os.path.join(SOURCE_DIR, filename)
            if 'Config' in filename:
                self.process_single_file(filepath, TARGET_CONF_DIR, is_config=True)
            elif 'Show' in filename:
                self.process_single_file(filepath, TARGET_SHOW_DIR, is_config=False)
            else:
                self.process_single_file(filepath, TARGET_CONF_DIR, is_config=True)
                self.process_single_file(filepath, TARGET_SHOW_DIR, is_config=False)
            self.processed_files += 1
            print(f"  CLT: {i}/{len(clt_files)} - {filename}")
        
        # Process EOT files
        print("\n[Phase 4/4] Processing EOT content files...")
        for i, filename in enumerate(eot_files, 1):
            filepath = os.path.join(SOURCE_DIR, filename)
            # Determine type from content
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    sample = f.read(1000).lower()
                    is_show = 'show' in sample[:500]
            except:
                is_show = False
            target = TARGET_SHOW_DIR if is_show else TARGET_CONF_DIR
            self.process_single_file(filepath, target, is_config=not is_show)
            self.processed_files += 1
            print(f"  EOT: {i}/{len(eot_files)} - {filename}")
        
        # Summary
        elapsed = datetime.now() - self.start_time
        print(f"\n{'=' * 70}")
        print("PROCESSING COMPLETE")
        print(f"{'=' * 70}")
        print(f"Files processed: {self.processed_files}/{self.total_files}")
        print(f"Commands extracted: {self.processed_commands}")
        print(f"Large files (>2MB): {len(self.large_files)}")
        if self.large_files:
            print("\nLarge files encountered:")
            for f, size in sorted(self.large_files, key=lambda x: x[1], reverse=True)[:10]:
                print(f"  - {f}: {size / (1024*1024):.2f} MB")
        print(f"\nElapsed time: {elapsed}")
        print(f"{'=' * 70}")
        
        self.save_status(f"Complete - {self.processed_commands} commands extracted")
        return self.processed_commands


def main():
    processor = CommandProcessor()
    processor.process_all_files()


if __name__ == "__main__":
    main()
