#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick debug of fix_index_links on comfyui.md"""
import re
from pathlib import Path

def get_all_headings(content):
    headings = []
    for line in content.split('\n'):
        m = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if m:
            headings.append(m.group(2).strip())
    return headings

def normalize(s):
    return s.lower().strip()

def test():
    md_file = Path(r'P:\00-repos\proyecto-pi\vault-arquitectura\wiki\glosario\software\comfyui.md')
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headings = get_all_headings(content)
    print("HEADINGS FOUND:")
    for h in headings:
        print(f"  '{h}'")
    
    heading_lookup = {}
    for h in headings:
        heading_lookup[normalize(h)] = h
    
    print("\nHEADING LOOKUP (first 5):")
    for k, v in list(heading_lookup.items())[:5]:
        print(f"  '{k}' -> '{v}'")
    
    # Test matching on index lines
    lines = content.split('\n')
    in_index = True
    matched = 0
    for i, line in enumerate(lines[:35]):
        if in_index and re.match(r'^#{1,6}\s+', line.strip()):
            in_index = False
            print(f"\nIndex ends at line {i}: {line.strip()}")
        
        if in_index:
            m = re.match(r'^(\s*-\s+\[)([^\]]+)(\]\()([^)]+)(\))', line)
            if m:
                link_text = m.group(2)
                norm_text = normalize(link_text)
                if norm_text in heading_lookup:
                    exact_heading = heading_lookup[norm_text]
                    print(f"  MATCH: link_text='{link_text}' -> [[#{exact_heading}]]")
                    matched += 1
                else:
                    print(f"  NO MATCH: link_text='{link_text}' (norm='{norm_text}')")
    
    print(f"\nTotal matched: {matched}")

test()
