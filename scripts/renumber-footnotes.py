#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renumera las notas [^n] del Kit temático (sección 4) para que no choquen
con las del master. El master usa [^1]-[^67]. El Kit usaba [^1]-[^40].
Ahora el Kit usa [^68]-[^107] en el cuerpo y las definiciones ya están
numeradas como [^68]-[^105] en el fondo.
"""
import re
from pathlib import Path

f = Path(r'P:\00-repos\proyecto-pi\vault-arquitectura\raw\docs\autocad-documento-maestro.md')
content = f.read_text(encoding='utf-8')
lines = content.split('\n')

# Find section boundaries
sec4_start = None
sec5_start = None
for i, line in enumerate(lines):
    if '## 4. SETs de estándar CAD (Kit Estudio Pi)' in line:
        sec4_start = i
    if '## 5. C1: AutoCAD Base' in line:
        sec5_start = i
        break

if sec4_start is None or sec5_start is None:
    print(f"ERROR: sec4_start={sec4_start}, sec5_start={sec5_start}")
    exit(1)

print(f"Section 4: lines {sec4_start} to {sec5_start-1}")

# Count current definitions to know the offset
# Master has [^1]-[^67], Kit definitions start at [^68]
# The Kit's body text references [^1]-[^40] need to become [^68]-[^107]
# But we need to check what definitions actually exist

# First, let's find all definitions and their numbers
all_defs = {}
for i, line in enumerate(lines):
    m = re.match(r'^(\[\^\d+\]):', line.strip())
    if m:
        all_defs[m.group(1)] = i

# Find the max master definition number
master_nums = []
for k in all_defs:
    num = int(k.replace('[^', '').replace(']', ''))
    if num <= 67:
        master_nums.append(num)

# Find what Kit definitions exist (68+)
kit_def_nums = sorted([int(k.replace('[^', '').replace(']', '')) for k in all_defs if int(k.replace('[^', '').replace(']', '')) > 67])
print(f"Master defs: [^1] to [^67] ({len(master_nums)} total)")
print(f"Kit defs at bottom: {kit_def_nums}")

# Now renumber section 4 body text
# Map: old Kit [^n] -> new [^n+67]
# But we need to handle cases where a Kit [^n] already has a definition at [^n+67]
# and cases where it doesn't

renumbered = 0
skipped = 0

for i in range(sec4_start, sec5_start):
    new_line = lines[i]
    
    def replace_ref(m):
        global renumbered, skipped
        old_num = int(m.group(1))
        new_num = old_num + 67
        new_ref = f'[^{new_num}]'
        
        # Check if definition exists
        if new_ref in all_defs:
            renumbered += 1
            return new_ref
        else:
            # Definition doesn't exist - this reference has no definition
            # This means we need to add it or it's a broken reference
            skipped += 1
            return new_ref
    
    new_line = re.sub(r'\[\^(\d+)\]', replace_ref, new_line)
    lines[i] = new_line

print(f"\nRenumbered: {renumbered}, Missing defs: {skipped}")
print(f"New range: [^68] to [^107]")

# Write back
f.write_text('\n'.join(lines), encoding='utf-8')
print("\nDone. File updated.")
