---
tipo: indice
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-10-08
tags: [scripts, automatizacion]
---

# Scripts y automatizaciones

_Automatizaciones para gestión del vault y flujos de trabajo._

## Curación de contenido (YouTube/Chrome)

- `transcribir_youtube.py` — Transcript de un video YT a `raw/yt/transcripts/YYYY-MM-DD_<id>.<lang>.md+.srt+.txt+.origen.json` (.md = envoltorio visible en Obsidian con frontmatter; prefijo ISO = orden cronológico nativo; subs manuales→automáticos primero, fallback faster-whisper local si no hay). Limpieza de artefactos (NBSP, apóstrofes). Notas en `transcribir_youtube_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir_youtube.py <video_id|URL>`.

- `yt_takeout_parser.py` — Parsea Google Takeout (YouTube + Chrome) y genera un documento único con todos los videos guardados agrupados por lista + los canales fuera de scope para revisión. Salida: `raw/yt/videos-y-canales-guardados.md`. Notas en `yt_takeout_parser_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py`. Úsalo cada vez que exportes un Takeout nuevo.
- `yt_titles.py` — Completa título + canal + duración de los videos vía YouTube Data API v3. Cachea en `raw/yt/cache-titulos.json` (solo pide los IDs que faltan, así el gasto de cuota tiende a cero). Requiere `YOUTUBE_API_KEY` en `.env`. Guías: [[wiki/glosario/interno/youtube-data-api-key|youtube-data-api-key]]. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py`.
- `yt_revision.py` — Genera el archivo de revisión manual con SOLO lo pendiente: WL sin clasificar + canales fuera de scope, con columnas vacías para el veredicto del estudio. Salida: `raw/yt/revision-manual.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_revision.py`.
- `yt_creadores.py` — Cruza los canales de Watch Later con suscripciones: suscriptos en scope + creadores solo-WL (no suscriptos) con veredicto agregado + suscriptos fuera. Salida: `raw/yt/creadores.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_creadores.py`.
- `yt_build_index.py` — Genera el índice único `wiki/fuentes/00-index-yt.md` (3 vistas: por listado, por creador, por tag) filtrado por tag. Estado pendiente/procesado desde `raw/yt/index-state.json` (tras el OK, la ruta apunta a `wiki/fuentes/<slug>.md`). Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_build_index.py [tag|all]`.

**Orden de ejecución tras un Takeout nuevo:**
```
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

## Utilidades

- `genera-template-set01.py` — Genera el DXF base del template SET_01-REP (29 capas, 8 estilos, 3 dimstyles, metros) para convertir a DWT/DWS vía ODA. Notas en `genera-template-set01_notas.md`. Uso: `python scripts\genera-template-set01.py`.

- `inventario-hardware.ps1` — Relevamiento Semana 0 (Vault Cerebro): CPU, RAM por slot, GPU + VRAM real (WMI), discos, monitores EDID, red, Python/Git/Node/VSCode/OpenCode, ComfyUI (`P:\00-repos\ComfyUI`), CAD/BIM instalado. Salida: consola + `.md` + `.json` en `raw/sessions/`. Uso: `powershell -ExecutionPolicy Bypass -File scripts\inventario-hardware.ps1`.

## Pendientes
- [ ] Script de indexación automática de proyectos
- [ ] Script de extracción de metadatos de DWG (capa, escala, fecha)
- [ ] OCR para planos escaneados (Tesseract)
- [ ] Workflow n8n: Slack/Teams → raw/ → ingest automático
- [ ] Script de lint del vault
- [ ] Generación de reporte de estado de proyectos
- [ ] `yt_rss_check.py` — chequea RSS de canales vigilados (Nivel 2, sin YouTube API key)
- [ ] `yt_briefing_gen.py` — genera el briefing semanal desde RSS (Nivel 2)
- [ ] Workflow n8n CRON lunes 8:00 → briefing + Telegram/email (Nivel 2)
