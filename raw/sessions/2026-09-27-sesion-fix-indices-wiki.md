---
fecha: 2026-09-27
herramientas: [opencode]
---

# Sesión 2026-09-27 — Corrección de índices wiki

## Qué se hizo

1. **Identificación del problema**: `wiki/glosario/software/autocad.md` usaba `[Texto](#slug)` manual en su índice, con slugs que no coincidían con headings que contienen `—` (em-dash) y `í` (tilde). El link `[Comandos — PLINE](#pline--polilinea)` no saltaba en Obsidian porque el heading real es `## PLINE — Polilínea`.

2. **Conversión masiva**: Escritura de `scripts/fix-index-links.py` que escanea todos los `.md` bajo `wiki/glosario/`, extrae headings `##`, identifica el índice (lista de guiones antes del primer `##`), y reemplaza `[Texto](#slug)` por `[[#Encabezado exacto]]`.

3. **Resultado**: 28 archivos corregidos en `wiki/glosario/` (software, referentes, conceptos, pbooks). Quedan sin tocar solo las cross-references en tablas (`[§ texto](#slug)` en `pbk-comfyui.md`), que no son índices.

## Archivos modificados (wiki/glosario/)
- software/: autocad, comfyui, faster-whisper, git, github, github-cli, n8n, opencode, pandoc, telegram
- referentes/: jacob-van-rijs, nils-peter-fischer, patrik-schumacher, shajay-bhooshan, ulrich-blum
- conceptos/: agile-arquitectura, cinco-s-5s-archivos, kaizen, last-planner-system, lean, okr-goals, payback, pm-project-management, retrospectivas
- pbooks/: pbk-agentes-vaultarq, pbk-comfyui, pbk-pm_vault, pbk-sherlock

## Convención establecida
- Índice interno: `[[#Encabezado exacto]]` — nunca `[Texto](#slug)`
- Entre archivos: `[[ruta/desde/raíz|alias]]` sin extensión ni `../`
- Carpetas no se enlazan (se enlaza a su `00-index.md`)

## Fuentes en raw/docs/autocad-documento-maestro.md (mismo día, continuación)
- **Problema**: el consolidado unió 5 archivos con numeración `[^n]` propia; el contenido del Kit (`### 3.2` + `## 4`) apuntaba a definiciones del master (ej: `[^39]` junto a "Assistant" caía en AEA). El plugin de footnotes además no responde en este vault.
- **Solución**: reemplazo de notación — cuerpo `[^64]` → `[[#^f64|64]]` (en tablas `\|` escapado) + ancla `^f64` al final de cada una de las 105 definiciones en `## 15. Fuentes`. Sin plugin: usa el motor de links de Obsidian.
- **Mapeo validado por URL** en `scripts/convert-fuentes-wikilinks.py` (con NOTA ES): cada ref del Kit se cotejó contra el Kit original por URL exacta; aborta sin escribir si algo no cuadra. Correcciones destacadas: `[^39]`→`[^104]` (Assistant), `[^40]`→`[^105]` (Wiley), desfases `5→71`, `10→72`, `12→78`, `13→79`, `16→82`, `21→87`, `24→89`, `25→90`, `26→91`, `27→92`, `28→93`, `29→94`.
- **Verificación del script**: 103 refs convertidas, 105 anclas, cero `[^n]` sueltos en cuerpo, cero alias sin ancla, índice intacto.
- **Limpieza**: borrado `raw/docs/__test-footnotes.md` (test mínimo de footnotes).
- **Uso**: Vista de Lectura (`Ctrl+E`), click en el numerito salta a la fuente exacta; volver con `Alt+←`.
