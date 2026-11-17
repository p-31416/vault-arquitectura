# Sesión 2026-11-17 — System First, V.E.R, diagrama y research Hermes

Fecha: 2026-11-17 · Cierre de sesión obligatorio

## Qué se hizo

- Filosofía System First elevada a manifiesto citable (16 aportes) y pasada de filo MVP_01 a VISION.
- V.E.R actualizado: VISION §1.6 + principio 10, ESTRUCTURA §3.3 routing Ollama + §7 roles + §10 2 ADR, REQUISITOS diagnosticado a medias.
- Visión por computadora alineada: Hermes trae `vision_analyze`, VISION definía modelo/política — cerrado a croquis ya + fotos en piloto.
- Tableros: Leantime humano + Hermes Kanban sintético con 3 refs oficiales, agregado a ESTRUCTURA §4.7.
- Costos imagen verificados OpenRouter (Nano Banana 2 $60/M out, Seedream $0.045) volcados a ESTRUCTURA §4.4.
- Research 20 fuentes sept-nov 2026 + doc aparte Hermes AI API image-to-image (19 modelos, MCP `https://api.hermes-ai.net/mcp`).
- Diagrama todo v2 compacto: cerebro Hermes intercambiable, MCP HUB, brazos N8N e imagen, Tailscale.

## Archivos modificados

- `proyectos/MVP_07-studio-os-sistema/VISION.md` — §1.6, §6.1 p10, §5 visión + research link, §6.8.3
- `proyectos/MVP_07-studio-os-sistema/ESTRUCTURA.md` — §3.3, §7, §10 2 ADR, §4.7 Kanban, §4.4 costos, §8 escaneo
- `wiki/glosario/conceptos/system-first-piezas-intercambiables.md` — nuevo
- `wiki/glosario/conceptos/00-index.md` — fila nueva
- `diagramas/sistema-studio-os-todo.mmd` + `.excalidraw.md` + `.png` — v2 compacto
- `raw/research/2026-11-17-hermes-sistemas-imagen-video.md` — 20 fuentes
- `raw/research/2026-11-17-hermes-ai-api-image-to-image.md` — evaluación aparte

## Cerebro-digital

Topics: System-First, loop-engineering-2027, Hermes-Kanban, vision_analyze-Qwen-VL, OpenRouter-costos, Hermes-AI-API-MIMOS
Entidades: Sol (propia, aprueba C/D), Emilia (opera, aviso solo modificación), Hermes-Agent-Nous (VPS), Hermes-AI-API-MIMOS (proveedor), Ollama-chico-VPS, OpenCode-Go-Sol, Leantime-humano, Kanban-sintético, Tailscale, ComfyUI, Seedream, Nano-Banana-2
Hechos:
- Ollama chico en VPS + cuenta OpenCode propia decididos 16/11
- Roles Sol/Emilia con autoría usuario+hilo y aviso solo C/D decididos 16/11
- Video excluido hasta T5+, imagen con router por `usage.cost`
- Hermes AI API requiere conectar agente Hermes, no reemplaza
- Cuaderno y publicación interfaz quedan para después
