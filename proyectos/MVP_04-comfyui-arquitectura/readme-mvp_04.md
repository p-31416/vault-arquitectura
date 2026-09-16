---
tipo: readme
mvp: 04
version: 1.0.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, readme]
---

# MVP 04: ComfyUI MCP — Creación de Arquitectura desde Texto

Integrar ComfyUI como motor de generación arquitectónica orquestado vía MCP. Resuelve el problema de **iteración lenta de renders**: de horas a segundos.

## Contenido

- [[00-filo-mvp_04]] — Manifiesto y filosofía AMV
- [[01-spec-mvp_04]] — Especificaciones y alcance por nivel
- [[02-ft-mvp_04]] — Plan técnico detallado
- [[03-log-mvp_04]] — Bitácora v1.0.0
- [[modelos-recomendados]] — Guía de modelos para arquitectura

### Setup

- [[setup_comfy_mcp]] — Configuración del MCP server
- [[pbook-comfy_setup]] — Playbook de opciones de instalación
- [[comfy-tratamiento-datos]] — Privacidad y propiedad intelectual

### Workflows

- [[workflow_croquis_a_render]] — Concepto técnico del pipeline
- [[reglas-workflows-comfy]] — Reglas obligatorias para creación de workflows (escalamiento, validación, etc.)

## Niveles de implementación

| Nivel | Flujo | Estado |
|-------|-------|--------|
| n_01 | Texto → Render (txt2img) | 🔜 Pendiente |
| n_02 | Croquis → Render (img2img) | 🔜 Pendiente |
| n_03 | ControlNet (Depth/Canny/Sketch) | 🔜 Pendiente |
| n_04 | Video (walkthrough animado) | 📅 Futuro |
| n_05 | Rhino MCP (tiempo real) | 📅 Futuro |
