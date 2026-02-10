#!/usr/bin/env python3
"""
Cisco Documentation Processor - Agent #1 (Enhanced)
Processes Release Notes and Fundamentals documentation from Cisco Nexus 9.3.X
Extracts full content from HTML files.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

def extract_release_notes_content(html_content, version):
    """Extract full content from release notes HTML"""
    md_lines = []
    md_lines.append(f"# Cisco Nexus 9000 NX-OS Release Notes - Release {version}")
    md_lines.append("")

    # Extract the main document content from WordSection1
    section1_match = re.search(r'<div class="WordSection1"[^>]*>(.*?)</div>\s*</body>', html_content, re.DOTALL)

    if section1_match:
        content = section1_match.group(1)

        # Extract all pToC_Subhead1 sections (main headings)
        head1_pattern = re.compile(r'<p class="pToC_Subhead1"[^>]*>(.*?)</p>\s*<p class="(pBody|pNote|Imagetable)"[^>]*>(.*?)</p>', re.DOTALL|re.IGNORECASE)

        # Get document revision date table
        date_table = re.findall(r'<td>\s*<p[^>]*>([^<]+)</p>\s*</td>\s*<td>\s*<p[^>]*>([^<]+)</p>\s*</td>', content)

        if date_table:
            md_lines.append("## Revision History")
            md_lines.append("")
            md_lines.append("| Date | Description |")
            md_lines.append("|---|---|")
            for row in date_table[:3]:  # Show first 3 revisions
                date = re.sub(r'<[^>]+>', '', row[0]).strip()
                desc = re.sub(r'<[^>]+>', '', row[1]).strip()
                if date and desc and 'Date' not in date:
                    md_lines.append(f"| {date} | {desc} |")
            md_lines.append("")

        # Extract main sections with their content
        # Find all subheadings and their following content
        sections = re.split(r'<p class="pToC_Subhead1"[^>]*>', content)

        for section in sections[1:]:  # Skip first part before first heading
            # Get the heading text
            heading_match = re.match(r'(<a[^>]*>)?([^<]+)', section)
            if heading_match:
                heading = heading_match.group(2).strip()
                heading = re.sub(r'<[^>]+>', '', heading)

                # Get content until next heading or end
                content_part = re.split(r'<p class="pToC_Subhead1"', section)[0]

                # Clean HTML
                clean_content = re.sub(r'<[^>]+>', ' ', content_part)
                clean_content = re.sub(r'&nbsp;', ' ', clean_content)
                clean_content = re.sub(r'\s+', ' ', clean_content).strip()

                if heading and len(heading) < 100:
                    md_lines.append(f"## {heading}")
                    md_lines.append("")
                    if clean_content and len(clean_content) > 10:
                        md_lines.append(clean_content[:2000])  # Limit content length
                        md_lines.append("")

        # Add all tables
        tables = extract_tables_from_html(content)
        if tables:
            md_lines.append("## Hardware Support Tables")
            md_lines.append("")
            for i, table in enumerate(tables[:10], 1):  # First 10 tables
                if len(table) > 1:
                    md_lines.append(format_table_to_md(table))
                    md_lines.append("")

    return '\n'.join(md_lines)

def extract_tables_from_html(html_content):
    """Extract all tables from HTML"""
    tables = []

    # Find all table elements
    table_pattern = re.compile(r'<table[^>]*>(.*?)</table>', re.DOTALL|re.IGNORECASE)

    for table_match in table_pattern.finditer(html_content):
        table_html = table_match.group(1)

        # Extract rows
        rows = []
        row_pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL|re.IGNORECASE)

        for row_match in row_pattern.finditer(table_html):
            row_html = row_match.group(1)

            # Extract cells
            cells = []
            cell_pattern = re.compile(r'<t[dh][^>]*>(.*?)</t[dh]>', re.DOTALL|re.IGNORECASE)

            for cell_match in cell_pattern.finditer(row_html):
                cell_html = cell_match.group(1)
                # Clean HTML tags
                cell_text = re.sub(r'<[^>]+>', ' ', cell_html)
                cell_text = re.sub(r'&nbsp;', ' ', cell_text)
                cell_text = re.sub(r'\s+', ' ', cell_text).strip()
                if cell_text:
                    cells.append(cell_text)

            if cells:
                rows.append(cells)

        if rows and len(rows) > 1:
            tables.append(rows)

    return tables

def format_table_to_md(table):
    """Format table data as Markdown"""
    if not table:
        return ""

    md_lines = []

    # Header
    if table[0]:
        md_lines.append('| ' + ' | '.join(table[0]) + ' |')
        md_lines.append('|' + '|'.join(['---' for _ in table[0]]) + '|')

    # Rows
    for row in table[1:]:
        if row:
            md_lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(md_lines)

def process_fundamentals_detailed(html_content):
    """Process fundamentals guide with detailed chapter extraction"""
    md_lines = []
    md_lines.append("# Cisco Nexus 9000 NX-OS Fundamentals Configuration Guide")
    md_lines.append("")
    md_lines.append("Release 9.3(x)")
    md_lines.append("")

    # Extract Book Table of Contents
    book_toc = re.findall(r'<li><a href="[^"]*">([^<]+)</a></li>', html_content)

    if book_toc:
        md_lines.append("## Book Table of Contents")
        md_lines.append("")
        for i, item in enumerate(book_toc, 1):
            md_lines.append(f"{i}. {item}")
        md_lines.append("")

    # Extract chapters content if available
    # Looking for chapter links that reference other HTML files
    chapter_links = re.findall(r'<a[^>]*href="([^"]*chapter[^"]*)"[^>]*>([^<]+)</a>', html_content)

    if chapter_links:
        md_lines.append("## Available Chapters")
        md_lines.append("")
        for link, title in chapter_links:
            md_lines.append(f"- **{title}**: `{link}`")
        md_lines.append("")

    md_lines.append("## Guide Overview")
    md_lines.append("")
    md_lines.append("This guide covers the fundamentals of configuring Cisco Nexus 9000 Series switches running NX-OS Release 9.3(x). It includes information on setup utilities, provisioning, CLI usage, file systems, and configuration management.")
    md_lines.append("")

    md_lines.append("### Key Topics")
    md_lines.append("")
    topics = [
        ("New and Changed Information", "Summary of new features and changes in this release"),
        ("Overview", "Introduction to NX-OS architecture and features"),
        ("Using the Cisco NX-OS Setup Utility", "Initial device setup and configuration"),
        ("Using PowerOn Auto Provisioning", "Automated provisioning at power-on"),
        ("Using Network Plug and Play", "PnP for automated network configuration"),
        ("Understanding the Command-Line Interface", "CLI structure and usage patterns"),
        ("Configuring Terminal Settings and Sessions", "Terminal configuration options"),
        ("Basic Device Management", "Device administration and management"),
        ("Using the Device File Systems", "File system navigation and management"),
        ("Working with Configuration Files", "Configuration file management"),
        ("Understanding the Startup Configuration", "Startup configuration details"),
        ("Managing Software Packages", "Software installation and management")
    ]

    for topic, desc in topics:
        md_lines.append(f"**{topic}**: {desc}")
        md_lines.append("")

    return '\n'.join(md_lines)

def main():
    # Configuration
    source_dir = Path("/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3/")
    target_dir = Path("/home/valentinbot/.openclaw/workspace/Documentation/Cisco_9_3_processed/Agent1_Release_Fundamentals/")

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    # Find all relevant files
    release_note_files = [
        ("cisco-nexus-9000-nxos-release-notes-9316.html", "9.3(16)"),
        ("cisco-nexus-9000-nxos-release-notes-939.html", "9.3(9)"),
        ("cisco-nexus-9000-nxos-release-notes-939_01.html", "9.3(9)"),  # Alt version
        ("cisco-nexus-9000-nxos-release-notes-933.html", "9.3(3)"),
        ("cisco-nexus-9000-nxos-release-notes-933_01.html", "9.3(3)"),  # Alt version
        ("931_9000_nxos_rn.html", "9.3(1)"),
        ("931_9000_nxos_rn_01.html", "9.3(1)"),  # Alt version
    ]

    fundamentals_files = [
        ("b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x.html", "main"),
        ("b-cisco-nexus-9000-nx-os-fundamentals-configuration-guide-93x_01.html", "alt"),
        ("preface.html", "preface"),
        ("preface_01.html", "preface_alt"),
    ]

    index_entries = {
        "release_notes": [],
        "fundamentals": [],
        "version": "2.0",
        "processed_date": datetime.now().isoformat()
    }

    processed_count = 0
    errors = []

    print("="*70)
    print("CISCO DOCUMENTATION PROCESSOR - AGENT #1")
    print("Processing Release Notes and Fundamentals")
    print("="*70)
    print()

    # Process release notes
    print("PROCESSING RELEASE NOTES...")
    print("-"*70)

    for filename, version in release_note_files:
        source_file = source_dir / filename

        if not source_file.exists():
            continue  # Skip if not found

        try:
            with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            # Generate unique output filename
            if "_01" in filename:
                suffix = "_alt"
            else:
                suffix = ""

            version_clean = version.replace('(', '_').replace(')', '')
            target_file = target_dir / f"release_notes_{version_clean}{suffix}.md"

            markdown_content = extract_release_notes_content(html_content, version)

            # Add source and tags
            markdown_content += f"\n\n---\n\n**Source:** {filename}\n"
            markdown_content += f"**Tags:** release-notes, nx-os, cisco-nexus, {version}, hardware-support, documentation\n"

            # Write markdown file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            processed_count += 1
            index_entries["release_notes"].append({
                "version": version,
                "file": target_file.name,
                "source": filename,
                "topics": ["release-notes", "hardware-support", "features", "nx-os"]
            })

            print(f"✓ {filename} -> {target_file.name}")

        except Exception as e:
            errors.append(f"Error processing {filename}: {str(e)}")
            print(f"✗ {filename}: {e}")

    print()
    print("PROCESSING FUNDAMENTALS GUIDE...")
    print("-"*70)

    # Process fundamentals guide
    for filename, ftype in fundamentals_files:
        source_file = source_dir / filename

        if not source_file.exists():
            continue

        try:
            with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            if ftype == "main":
                target_file = target_dir / "fundamentals_configuration_guide.md"
            elif ftype == "alt":
                target_file = target_dir / "fundamentals_configuration_guide_alt.md"
            elif ftype == "preface":
                target_file = target_dir / "fundamentals_preface.md"
            else:
                continue

            markdown_content = process_fundamentals_detailed(html_content)

            # Add source and tags
            markdown_content += f"\n\n---\n\n**Source:** {filename}\n"
            markdown_content += f"**Tags:** fundamentals, configuration-basics, nx-os, cisco-nexus, 9.3.x, documentation\n"

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            processed_count += 1
            index_entries["fundamentals"].append({
                "file": target_file.name,
                "source": filename,
                "type": ftype,
                "topics": ["fundamentals", "configuration-basics", "nx-os"]
            })

            print(f"✓ {filename} -> {target_file.name}")

        except Exception as e:
            errors.append(f"Error processing {filename}: {str(e)}")
            print(f"✗ {filename}: {e}")

    # Also process EPLD release notes if available
    epld_file = source_dir / "nxos_n9K_epldRN_938.html"
    if epld_file.exists():
        try:
            with open(epld_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            target_file = target_dir / "epld_release_notes_9.3.8.md"

            # Basic processing for EPLD
            md_lines = []
            md_lines.append("# Cisco Nexus 9000 NX-OS EPLD Release Notes - Release 9.3(8)")
            md_lines.append("")

            # Extract content
            content_match = re.search(r'<div class="WordSection1"[^>]*>(.*?)</div>\s*</body>', html_content, re.DOTALL)
            if content_match:
                tables = extract_tables_from_html(content_match.group(1))
                for table in tables[:5]:
                    md_lines.append(format_table_to_md(table))
                    md_lines.append("")

            md_lines.append(f"\n\n---\n\n**Source:** nxos_n9K_epldRN_938.html\n")
            md_lines.append(f"**Tags:** epld, release-notes, nx-os, hardware-upgrade\n")

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(md_lines))

            processed_count += 1
            index_entries["release_notes"].append({
                "version": "9.3(8) EPLD",
                "file": target_file.name,
                "source": "nxos_n9K_epldRN_938.html",
                "topics": ["epld", "release-notes", "hardware-upgrade"]
            })

            print(f"✓ nxos_n9K_epldRN_938.html -> {target_file.name}")

        except Exception as e:
            errors.append(f"Error processing EPLD file: {str(e)}")

    # Write index.json
    index_file = target_dir / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_entries, f, indent=2)

    # Summary
    print()
    print("="*70)
    print("PROCESSING COMPLETE")
    print("="*70)
    print(f"Files processed: {processed_count}")
    print(f"Output directory: {target_dir}")
    print(f"Index file: {index_file}")
    print()
    print("FILES CREATED:")
    for file in sorted(target_dir.glob("*.md")):
        size = file.stat().st_size
        print(f"  - {file.name} ({size} bytes)")

    if errors:
        print()
        print(f"ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  ! {error}")

    return processed_count, errors, index_entries

if __name__ == "__main__":
    main()
