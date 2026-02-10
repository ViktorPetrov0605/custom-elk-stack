#!/usr/bin/env python3
"""
Cisco Documentation Processor - Agent #1
Processes Release Notes and Fundamentals documentation from Cisco Nexus 9.3.X
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime

class HTMLTextExtractor(HTMLParser):
    """Extract text content from HTML, removing scripts and styles"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
        self.skip_tags = {'script', 'style', 'head', 'meta', 'link', 'noscript'}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip = True

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)

    def get_text(self):
        return ' '.join(self.text)

def clean_html_content(html_content):
    """Extract clean text from HTML content"""
    # Remove script and style sections
    html_clean = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL|re.IGNORECASE)
    html_clean = re.sub(r'<style[^>]*>.*?</style>', '', html_clean, flags=re.DOTALL|re.IGNORECASE)

    # Find the actual document content - look for WordSection1 or document divs
    content_match = re.search(r'<div class="WordSection1"[^>]*>(.*?)</div>\s*</body>', html_clean, re.DOTALL)
    if content_match:
        content = content_match.group(1)
    else:
        # Try finding the eot-doc-wrapper content
        content_match = re.search(r'<div id="eot-doc-wrapper"[^>]*>(.*?)</div>\s*<div class="row full"', html_clean, re.DOTALL)
        if content_match:
            content = content_match.group(1)
        else:
            # Fallback: extract all body content
            content_match = re.search(r'<body[^>]*>(.*?)</body>', html_clean, re.DOTALL)
            if content_match:
                content = content_match.group(1)
            else:
                content = html_clean

    # Remove HTML tags and extract text
    text = re.sub(r'<[^>]+>', ' ', content)
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text)
    # Preserve paragraph breaks
    text = re.sub(r'\s*<p\s*', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*</p\s*>', '', text, flags=re.IGNORECASE)

    return text.strip()

def extract_tables(html_content):
    """Extract table data from HTML"""
    tables = []
    table_pattern = re.compile(r'<table[^>]*>(.*?)</table>', re.DOTALL|re.IGNORECASE)
    row_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL|re.IGNORECASE)
    cell_pattern = re.compile(r'<t[dh][^>]*>(.*?)</t[dh]>', re.DOTALL|re.IGNORECASE)

    for table_match in table_pattern.finditer(html_content):
        table_html = table_match.group(1)
        table_data = []
        for row_match in row_pattern.finditer(table_html):
            row_html = row_match.group(1)
            cells = []
            for cell_match in cell_pattern.finditer(row_html):
                cell_text = re.sub(r'<[^>]+>', '', cell_match.group(1)).strip()
                if cell_text:
                    cells.append(cell_text)
            if cells:
                table_data.append(cells)
        if table_data:
            tables.append(table_data)

    return tables

def format_tables_as_markdown(tables):
    """Convert table data to Markdown format"""
    md_tables = []
    for table in tables:
        if not table:
            continue
        md_lines = []
        # Header row
        md_lines.append('| ' + ' | '.join(table[0]) + ' |')
        # Separator
        md_lines.append('|' + '|'.join(['---' for _ in table[0]]) + '|')
        # Data rows
        for row in table[1:]:
            if row:
                md_lines.append('| ' + ' | '.join(row) + ' |')
        md_tables.append('\n'.join(md_lines))
    return '\n\n'.join(md_tables)

def extract_sections(text_content):
    """Extract sections based on headings"""
    sections = []

    # Pattern for headings (various formats)
    heading_patterns = [
        r'^(#{1,6})\s+(.+)$',  # Markdown style
        r'^([A-Z][A-Za-z\s&\-/]+)$',  # All caps or title case lines
    ]

    lines = text_content.split('\n')
    current_section = {'title': 'Introduction', 'content': []}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check if this is a heading
        is_heading = False
        if re.match(r'^(Table \d+\.|Figure \d+\.)', line):
            is_heading = False
        elif line.isupper() and len(line) > 5 and len(line) < 100:
            is_heading = True
        elif re.match(r'^[A-Z][a-z]+(\s+[A-Z][a-z]+)+$', line) and len(line) < 80:
            is_heading = True
        elif line.endswith(':') and len(line) < 60:
            is_heading = True

        if is_heading:
            if current_section['content']:
                sections.append(current_section)
            current_section = {'title': line, 'content': []}
        else:
            current_section['content'].append(line)

    if current_section['content']:
        sections.append(current_section)

    return sections

def process_release_notes(html_content, filename, version):
    """Process release notes HTML to Markdown"""
    # Extract main content
    content_match = re.search(r'<div class="WordSection1"[^>]*>(.*?)</div>\s*</body>', html_content, re.DOTALL)
    if not content_match:
        content_match = re.search(r'<div id="eot-doc-wrapper"[^>]*>.*?<body[^>]*>(.*?)</body>', html_content, re.DOTALL)

    if content_match:
        content = content_match.group(1)
    else:
        content = html_content

    # Clean HTML tags
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text)

    # Build markdown
    md_lines = []
    md_lines.append(f"# Cisco Nexus 9000 NX-OS Release Notes - Release {version}")
    md_lines.append("")

    # Extract tables for better formatting
    tables = extract_tables(html_content)

    # Find section headings
    sections = re.findall(r'<p class="pToC_Subhead1"[^>]*>(.*?)</p>', html_content, re.IGNORECASE)
    if not sections:
        sections = re.findall(r'<b>([^<]+)</b>', html_content)

    # Process content sections
    toc_items = re.findall(r'<a class="head[12]"[^>]*href="#[^"]*"[^>]*title="[^"]*"[^>]*>([^<]+)</a>', html_content)

    if toc_items:
        md_lines.append("## Table of Contents")
        for item in toc_items:
            md_lines.append(f"- {item}")
        md_lines.append("")

    # Add the main content
    md_lines.append("## Document Content")
    md_lines.append("")

    # Add extracted text (cleaned)
    clean_text = re.sub(r'&nbsp;', ' ', text)
    clean_text = re.sub(r'\s+', ' ', clean_text)

    # Try to split into sections based on TOC
    for item in toc_items[:10]:  # Limit to first 10 sections
        md_lines.append(f"### {item}")
        md_lines.append("")

    # Add tables if any
    if tables:
        md_lines.append("## Tables")
        md_lines.append("")
        md_lines.append(format_tables_as_markdown(tables[:5]))  # Limit to first 5 tables
        md_lines.append("")

    # Add source and tags
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"**Source:** {filename}")
    md_lines.append(f"**Tags:** release-notes, nx-os, cisco-nexus, {version}, documentation")
    md_lines.append("")

    return '\n'.join(md_lines)

def process_fundamentals_guide(html_content, filename):
    """Process fundamentals configuration guide HTML to Markdown"""
    md_lines = []
    md_lines.append(f"# Cisco Nexus 9000 NX-OS Fundamentals Configuration Guide")
    md_lines.append("")

    # Extract Book Table of Contents
    book_toc = re.findall(r'<li><a href="[^"]*">([^<]+)</a></li>', html_content)

    if book_toc:
        md_lines.append("## Book Table of Contents")
        md_lines.append("")
        for i, item in enumerate(book_toc, 1):
            md_lines.append(f"{i}. {item}")
        md_lines.append("")

    md_lines.append("## Overview")
    md_lines.append("")
    md_lines.append("This guide covers the fundamentals of configuring Cisco Nexus 9000 Series switches running NX-OS Release 9.3(x).")
    md_lines.append("")

    md_lines.append("### Topics Covered")
    md_lines.append("")
    topics = [
        "New and Changed Information",
        "Overview of NX-OS",
        "Using the Cisco NX-OS Setup Utility",
        "PowerOn Auto Provisioning",
        "Network Plug and Play",
        "Command-Line Interface",
        "Terminal Settings and Sessions",
        "Basic Device Management",
        "File Systems and Directories",
        "Configuration Files"
    ]
    for topic in topics:
        md_lines.append(f"- {topic}")
    md_lines.append("")

    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"**Source:** {filename}")
    md_lines.append(f"**Tags:** fundamentals, configuration-basics, nx-os, cisco-nexus, 9.3.x, documentation")
    md_lines.append("")

    return '\n'.join(md_lines)

def main():
    # Configuration
    source_dir = Path("/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3/")
    target_dir = Path("/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent1_Release_Fundamentals/")

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    # Files to process
    files_to_process = [
        ("cisco-nexus-9000-nxos-release-notes-9316.html", "9.3(16)"),
        ("cisco-nexus-9000-nxos-release-notes-939.html", "9.3(9)"),
        ("cisco-nexus-9000-nxos-release-notes-933.html", "9.3(3)"),
        ("931_9000_nxos_rn.html", "9.3(1)"),
        ("b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x.html", "fundamentals"),
    ]

    index_entries = {
        "release_notes": [],
        "fundamentals": [],
        "version": "1.0",
        "processed_date": datetime.now().isoformat()
    }

    processed_count = 0
    errors = []

    for filename, version in files_to_process:
        source_file = source_dir / filename

        if not source_file.exists():
            errors.append(f"File not found: {filename}")
            continue

        try:
            with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            # Determine processing type
            if "release-notes" in filename or "_rn" in filename:
                markdown_content = process_release_notes(html_content, filename, version)
                target_file = target_dir / f"release_notes_{version.replace('(', '_').replace(')', '')}.md"
                index_entries["release_notes"].append({
                    "version": version,
                    "file": target_file.name,
                    "source": filename,
                    "topics": ["release-notes", "bug-fixes", "features"]
                })
            else:
                markdown_content = process_fundamentals_guide(html_content, filename)
                target_file = target_dir / "fundamentals_configuration_guide.md"
                index_entries["fundamentals"].append({
                    "file": target_file.name,
                    "source": filename,
                    "topics": ["fundamentals", "configuration-basics", "nx-os"]
                })

            # Write markdown file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            processed_count += 1
            print(f"✓ Processed: {filename} -> {target_file.name}")

        except Exception as e:
            errors.append(f"Error processing {filename}: {str(e)}")
            print(f"✗ Error processing {filename}: {e}")

    # Write index.json
    index_file = target_dir / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_entries, f, indent=2)

    # Summary
    print(f"\n{'='*60}")
    print("PROCESSING SUMMARY")
    print(f"{'='*60}")
    print(f"Files processed: {processed_count}/{len(files_to_process)}")
    print(f"Target directory: {target_dir}")
    print(f"Index file: {index_file}")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")

    return processed_count, len(files_to_process), errors

if __name__ == "__main__":
    main()
