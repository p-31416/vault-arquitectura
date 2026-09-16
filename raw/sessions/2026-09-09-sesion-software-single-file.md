# Sesión 2026-09-09 — software/ a UNICO .md

## Qué se hizo

- Pedido Sol: `wiki/glosario/software/` tenía carpetas por software; regla AGENTS.md exige UNICO .md navegable.
- Creados: `ffmpeg.md` (fold index+extract-audio), `obs.md` (fold index+captura), `gohighlevel.md` (fold index+6 etapas como secciones ⏳), 6 singles stub (revit/rhino/grasshopper/twinmotion/unreal/impresion-3d).
- Verificado sin pérdida: `autocad.md` (pline+entmake+pendientes), `comfyui.md` (594 líneas), `faster-whisper.md` cubrían su legado (carpetas ya eliminadas en reorg previa).
- Eliminadas 10 carpetas. Retargets mínimos (00-index, faster-whisper→ffmpeg, telegram-spec→obs, opencode→pbk renombrado).
- `template.md` y bloque "Crear entrada nueva" actualizados a patrón single-file. `AGENTS.md` sin excepción legado.
- Auditoría final: 267 links → 0 rotos.

## Análisis cerebro digital (Karpathy)

- **Topics:** ninguno nuevo.
- **Entidades:** —.
- **Hechos:** migración single-file completa en software/; patrón a replicar si aparecen carpetas en otras ramas (índice+entradas → secciones `##` + `[[#...]]`); links a carpetas eliminadas caen en auditoría automáticamente.
