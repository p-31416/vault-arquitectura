#!/usr/bin/env python3
"""
Convierte [Texto](#slug) en el índice interno de archivos wiki a [[#Encabezado exacto]].
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

def get_all_headings(content):
    """Extrae todos los headings ##...## del archivo."""
    headings = []
    for line in content.split('\n'):
        m = re.match(r'^(#{2,6})\s+(.+)$', line.strip())
        if m:
            headings.append(m.group(2).strip())
    return headings

def normalize(s):
    """Normaliza texto para comparación aproximada."""
    return s.lower().strip()

def fix_index_links(content):
    """Reemplaza [Texto](#slug) en el índice por [[#Heading exacto]]."""
    headings = get_all_headings(content)
    
    # Crear mapa normalized -> exact heading
    heading_lookup = {}
    for h in headings:
        heading_lookup[normalize(h)] = h
    
    lines = content.split('\n')
    new_lines = []
    changed = False
    in_index = True
    
    for line in lines:
        # Detectar fin del índice (primer heading ##)
        if in_index and re.match(r'^#{2,6}\s+', line.strip()):
            in_index = False
        
        if in_index:
            # Intentar parsear: - [Texto](#slug)
            m = re.match(r'^(\s*-\s+)(\[)([^\]]+)(\]\()([^)]+)(\))', line)
            if m:
                prefix = m.group(1)
                bracket_open = m.group(2)
                link_text = m.group(3)
                bracket_close_slug = m.group(4)
                old_slug = m.group(5)
                suffix = m.group(6)
                
                # Buscar coincidencia exacta de heading
                norm_text = normalize(link_text)
                if norm_text in heading_lookup:
                    exact_heading = heading_lookup[norm_text]
                    new_line = f'{prefix}[[{exact_heading}]]'
                    new_lines.append(new_line)
                    if new_line != line:
                        changed = True
                    continue
        
        new_lines.append(line)
    
    return '\n'.join(new_lines), changed

def main():
    base = Path(r'P:\00-repos\proyecto-pi\vault-arquitectura\wiki\glosario')
    all_md = list(base.rglob('*.md'))
    
    fixed = []
    skipped = []
    errors = []
    
    for md_file in sorted(all_md):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, changed = fix_index_links(content)
            
            if changed:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed.append(str(md_file))
            else:
                skipped.append(str(md_file))
        except Exception as e:
            errors.append((str(md_file), str(e)))
    
    print(f"\n{'='*60}")
    print(f"  CORRECCION DE INDICES: [[#Encabezado exacto]]")
    print(f"{'='*60}")
    print(f"\nARCHIVOS CORREGIDOS ({len(fixed)}):")
    for f in fixed:
        print(f"   {f}")
    
    if errors:
        print(f"\nERRORES ({len(errors)}):")
        for path, err in errors:
            print(f"   {path}: {err}")
    
    print(f"\n{'='*60}\n")
    
    # Resumen final
    print(f"Total corregidos: {len(fixed)}")
    print(f"Total errores: {len(errors)}")
    return len(fixed) > 0

if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
