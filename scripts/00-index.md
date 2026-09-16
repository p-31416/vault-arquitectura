---
tipo: indice
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-06-28
tags: [scripts, automatizacion]
---

# Scripts y automatizaciones

_Automatizaciones para gestión del vault y flujos de trabajo._

## Utilidades

- `inventario-hardware.ps1` — Relevamiento Semana 0 (Vault Cerebro): CPU, RAM por slot, GPU + VRAM real (WMI), discos, monitores EDID, red, Python/Git/Node/VSCode/OpenCode, ComfyUI (`P:\00-repos\ComfyUI`), CAD/BIM instalado. Salida: consola + `.md` + `.json` en `raw/sessions/`. Uso: `powershell -ExecutionPolicy Bypass -File scripts/inventario-hardware.ps1`.

## Pendientes
- [ ] Script de indexación automática de proyectos
- [ ] Script de extracción de metadatos de DWG (capa, escala, fecha)
- [ ] OCR para planos escaneados (Tesseract)
- [ ] Workflow n8n: Slack/Teams → raw/ → ingest automático
- [ ] Script de lint del vault
- [ ] Generación de reporte de estado de proyectos
