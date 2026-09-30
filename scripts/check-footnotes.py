#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica que todas las referencias [^n] en el cuerpo tengan definiciones"""
import re
from pathlib import Path

f = Path(r'P:\00-repos\proyecto-pi\vault-arquitectura\raw\docs\autocad-documento-maestro.md')
content = f.read_text(encoding='utf-8')
lines = content.split('\n')

# Find all footnote definitions at the bottom (after section 15)
defs = {}
in_footnotes = False
for i, line in enumerate(lines):
    if '## 15. Fuentes' in line:
        in_footnotes = True
        continue
    if in_footnotes:
        m = re.match(r'^(\[\^\d+\]):', line.strip())
        if m:
            defs[m.group(1)] = i

# Find all footnote references in body (before section 15)
refs = {}
for i, line in enumerate(lines):
    if '## 15. Fuentes' in line:
        break
    for m in re.finditer(r'\[\^(\d+)\]', line):
        num = m.group(1)
        if num not in refs:
            refs[num] = []
        refs[num].append(i)

# Find all footnote definitions at the bottom (after section 15)
defs = {}
in_footnotes = False
for i, line in enumerate(lines):
    if '## 15. Fuentes' in line:
        in_footnotes = True
        continue
    if in_footnotes:
        m = re.match(r'^(\[\^\d+\]):', line.strip())
        if m:
            defs[m.group(1)] = i

# Find all footnote references in body (before section 15)
refs = {}
for i, line in enumerate(lines):
    if '## 15. Fuentes' in line:
        break
    for m in re.finditer(r'\[\^(\d+)\]', line):
        num = m.group(1)
        if num not in refs:
            refs[num] = []
        refs[num].append(i)

# Find missing definitions
missing = [n for n in sorted(refs.keys(), key=int) if f'[^{n}]' not in defs]
# Defs not referenced in body (from master section)
extra_defs = [k for k in sorted(defs.keys(), key=lambda x: int(x.replace('[^', '').replace(']', ''))) if k.replace('[^', '').replace(']', '') not in refs]

print(f"Reference numbers in body: {sorted(refs.keys(), key=int)}")
print(f"Definition numbers: {sorted(defs.keys(), key=lambda x: int(x))}")
print(f"Refs WITHOUT definitions: {missing}")
print(f"Defs NOT referenced in body: {extra_defs}")
print(f"Total body refs: {sum(len(v) for v in refs.values())}")
print(f"Total defs: {len(defs)}")
