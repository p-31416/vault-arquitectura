---
name: excalidraw-skill
description: "Diagramas Excalidraw (fases concurso→entrega, organigrama equipo remoto, esquemas, flujos vault/Fathom→specs→Leantime, detalles). Se activa con diagrama, esquema, excalidraw, mermaid. CLI npx mcp-excalidraw-server; en vault Obsidian exportar como .excalidraw.md. Verificar con screenshot antes de seguir."
---

# Excalidraw — estudio de arquitectura

> Portado de `vault-lidia`. Uso típico acá: flujo de fases, organigrama, partido/esquema, arquitectura vault (`Meet→Fathom→raw→specs→Leantime`), CAD→BIM, pipeline ComfyUI. Referencia completa en `references/cheatsheet.md`. Si el vault es Obsidian (hay `.obsidian/`), exportar `.excalidraw.md` (formato nativo plugin), no `.excalidraw` crudo.

## Step 0: Interfaz
1. **MCP `excalidraw/*`** si existe → preferirla
2. **CLI** (default): `npx -y mcp-excalidraw-server <command>` (auto-levanta canvas `http://127.0.0.1:3000`; abrir esa URL en browser — screenshot/mermaid/export la necesitan; exit 4 = falta tab)
3. **REST** último recurso (ver cheatsheet)

## CLI mínimo
| Tarea | Comando |
|---|---|
| estado/start/stop | `status`, `start`, `stop` |
| crear | `add elements.json` / stdin / `add --one '{...}'` |
| patch multi-op | `apply patch.json` |
| leer | `get <id>`, `query`, `describe` (texto) |
| ver | `screenshot [--out f.png]` / `--format svg` |
| layout | `arrange align\|distribute\|group\|lock\|duplicate --ids a,b` |
| archivos | `export [--out d.excalidraw.md]`, `import f.excalidraw.md [--replace]` |
| mermaid→canvas | `mermaid [d.mmd\|-]` |
| snapshots | `snapshot save\|list\|restore <n>` |
| limpiar | `clear --yes` |

Formato agente: `"text"` en shapes (se convierte a bound-label), flechas con `startElementId/endElementId`, ids propios (`"id":"partido"`). Ancho ≈ `max(160, chars*12)`, alto 60/80, gaps ≥40px, títulos ≥20px, cuerpo ≥16px, `"fillStyle":"solid"`.

## Anti-patrones
1. NO `text` en rectángulo-fondo grande (queda centrado y tapa todo) → texto libre arriba (`x+20,y+10`)
2. NO flechas diagonales cruzando zonas → dentro de zona/tier, o codo por perímetro
3. Labels de flecha solo si aportan (≤12 chars) — si todas llevan, es ruido

## Workflow
1. Planificar grilla (tiers, x) antes del JSON
2. `add` por lotes → `screenshot` → checklist (truncado, overlap, cruces, labels, spacing) → fix → seguir
3. Mermaid cuando el diagrama es flowchart/seq/ER puro; directo cuando hay layout preciso (implantación, zonificación)
4. Guardar en repo: `diagramas/<tema>.excalidraw.md` + `screenshot --out diagramas/<tema>.png` para el `.md` que lo referencia (`activos/` no — el `.excalidraw.md` es texto, sí va a git)
5. `snapshot save` antes de cambios riesgosos

## Diagrams vault → referenciar
```markdown
![flujo reuniones](diagramas/fathom-specs-leantime.png)
> Fuente editable: `diagramas/fathom-specs-leantime.excalidraw.md`
```

## References
- `references/cheatsheet.md` (copiado de Lidia): CLI completo, 26 tools MCP, REST, guía diseño/colores

## Origen
Portado de `P:\00-repos\pitau-tech\vault-lidia\.opencode\skills\excalidraw-skill\SKILL.md` + `references/cheatsheet.md`.
