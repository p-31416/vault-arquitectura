---
tipo: log
fecha: 2026-09-07
sesion: ghl-transcripcion-vault
participantes: [SOL, opencode]
tags: [ghl, transcripcion, vault, ingest, studio-os, emilia, automatizacion, obs, faster-whisper]
---

# 2026-09-07 — Sesión GHL academia → vault Pitau Tech (ciclo 6 etapas)

## Objetivo
Definir cómo transcribir videos de la academia creada con Go High Level (sin descarga) para alimentar el vault sin desperdiciar conocimiento. Solo videos útiles para propuesta comercial agencia IA. Caso inmediato: definir **propuesta diagnóstico para Emilia** (asociada estudio grande) usando el ciclo del video: 1.relevamiento 2.análisis-diseño 3.implementación 4.pruebas 5.entrenamiento 6.producción.

## Qué se hizo

### 1. Búsqueda web (3 queries)
- `GoHighLevel transcribe meetings` → hallada transcripción nativa solo para **llamadas** (`Phone System > Voice > Call Transcription` $0.024/min + workflow `Transcript Generated > AI Summarize`) — no sirve para videos academia [help.gohighlevel.com](https://help.gohighlevel.com/support/solutions/articles/155000002841-how-to-enable-call-transcriptions-for-recorded-calls)
- `GoHighLevel academy video download disabled` → hallada extensión **GoHighLevel Downloader** (SERP, Chrome Web Store) que detecta HLS nativo + Wistia/Vimeo/Loom → MP4, 3 descargas gratis [github.com/serpapps/gohighlevel-downloader](https://github.com/serpapps/gohighlevel-downloader)
- `grabar audio sistema Windows OBS WASAPI` → confirmado OBS + Audacity WASAPI loopback como alternativas libres

### 2. Decisión arquitectura vault
- Usuario rechazó `wiki/software` para esto — correcto: es **metodología de implementación**, no herramienta
- Destino definido: `wiki/raw/` (verbatim) → `wiki/estudio/metodologia-ciclo-6-etapas.md` + `wiki/estudio/servicios-pitau-tech-arquitectura.md` + 6 entradas `wiki/glosario/software/gohighlevel/` + `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md`
- Mapeo 6 etapas GHL → Pitau Tech arquitectura documentado (tabla Sprint 30d USD 600 = etapas 1+2)

### 3. Restricción "sin licencia" + OBS
- Usuario: OBS ya instalado, quiere resto automático y sin licencia paga
- Verificado: `ffmpeg` y `faster-whisper` no instalados en `comfyenv` → creadas instrucciones instalación portable
- Creado `scripts/transcribir_ghl.py` (100% libre MIT/Apache): `OBS mkv → ffmpeg extrae mp3 → faster-whisper CPU int8 → wiki/raw/*.md + .txt + .srt`

### 4. Plan documentado
- Creado `specs/260907-ghl-ingest-6-etapas.md` — pipeline completo con 3 opciones captura (A extensión, B OBS, C Audacity loopback), 2 opciones transcripción (local faster-whisper / nube TurboScribe), estructura archivos, checklist HOY, framing comercial diagnóstico
- Directorios creados: `wiki/raw/`, `wiki/glosario/software/gohighlevel/`, `proyectos/STUDIO_OS-Emilia/documentacion/`
- `log.md` actualizado con entrada 2026-09-07 arriba + `ultima_actualizacion`
- `proyectos/STUDIO_OS-Emilia/index.md` actualizado con link a 06-plan

### 5. Script automatización
- `scripts/transcribir_ghl.py` creado — uso: `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/reuniones/ghl-academia/captura.mkv" --model medium --language es`
- Busca ffmpeg en `P:\00-repos\ffmpeg\bin\`, `VAULT/ffmpeg/bin/`, o PATH; auto-reutiliza audio si ya existe

### 6. Cierre solicitado
- Usuario va a probar con primer video por su cuenta → queda pendiente que pegue transcript para ejecutar ingest completo (§5-§7 del plan) y glosario
- Este archivo documenta sesión como raw/sessions obligatorio (AGENTS.md: Cierre de sesión)

## Archivos modificados

- `specs/260907-ghl-ingest-6-etapas.md` — creado
- `scripts/transcribir_ghl.py` — creado
- `log.md:1-18` — entrada 2026-09-07 + ultima_actualizacion
- `proyectos/STUDIO_OS-Emilia/index.md:40` — link a 06-plan
- `wiki/raw/` — directorio creado (vacío, listo para raw verbatim)
- `wiki/glosario/software/gohighlevel/` — directorio creado (vacío, 6 entradas pendientes)
- `raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault.md` — este archivo

## Archivos binarios referenciados (no en git)

- `activos/reuniones/ghl-academia/` — destino capturas OBS (gitignored, a crear por usuario)
- `P:\00-repos\ffmpeg\bin\ffmpeg.exe` — ffmpeg portable pendiente de descargar por usuario

## Análisis cerebro digital (Karpathy — extrapolación)

### Topics candidatos a `wiki/glosario/software/`

**Software (herramientas libres):**
- `ffmpeg` → `wiki/glosario/software/ffmpeg/ffmpeg-extract-audio.md` — `ffmpeg -i video.mkv -vn -acodec libmp3lame -q:a 2 audio.mp3`
- `faster-whisper` → `wiki/glosario/software/faster-whisper/transcribe.md` — `WhisperModel(medium, device=cpu, compute_type=int8)` + `vad_filter=True`, idioma es
- `OBS Studio` → `wiki/glosario/software/obs/captura-pantalla-audio.md` — fuente Captura pantalla + Captura audio salida, mkv/mp4
- `Audacity WASAPI loopback` → `wiki/glosario/software/audacity/wasapi-loopback.md` — host WASAPI Windows, dispositivo loopback para grabar sistema sin mic

**Software (GoHighLevel):**
- `GoHighLevel Call Transcription` → `wiki/glosario/software/gohighlevel/call-transcription.md` — Phone System > Voice > toggle, $0.024/min, trigger Transcript Generated
- `GoHighLevel Downloader` (extensión SERP) → `wiki/glosario/software/gohighlevel/downloader.md` — detecta HLS/Wistia/Vimeo/Loom → MP4, 3 gratis, store link verificado
- `GoHighLevel Workflow AI Summarize` → `wiki/glosario/software/gohighlevel/workflow-ai-summarize.md` — acción Workflow AI Summarize Text con transcript como input

**Conceptos (metodología 6 etapas — transversales, no solo GHL):**
- `relevamiento-requerimientos` → `wiki/glosario/software/gohighlevel/relevamiento-requerimientos.md` — etapa 1: input entrevistas/shadowing, output mapa AS-IS
- `analisis-diseno-solucion` → `.../analisis-diseno-solucion.md` — etapa 2: blueprint TO-BE, arquitectura Drive+Vault+Discord→ComfyUI
- `implementacion-tecnica` → `.../implementacion-tecnica.md` — etapa 3: build vertical slice, no big bang
- `pruebas-internas` → `.../pruebas-internas.md` — etapa 4: QA interno Pitau Tech, check licencias OpenRAIL
- `entrenamiento-agentes` → `.../entrenamiento-agentes.md` — etapa 5: capacitación 30min, 1 comando, junior librarian
- `puesta-produccion` → `.../puesta-produccion.md` — etapa 6: go-live + métricas baseline + Go/No-Go Fase 2
- `ingest-raw-vault` → concepto `wiki/estudio/metodologia-ingest.md` — raw verbatim → procesado temático → glosario → servicios

### Entidades

- Personas: SOL (arquitecta/consultora IA, vault manager), Emilia Pimenta (cliente, asociada estudio grande, caso diagnóstico HOY)
- Proyecto: `STUDIO_OS-Emilia` — Sprint 30 días USD 600, fase briefing → diagnostico, 04-plan-studio-os.md como base
- Herramientas: OBS Studio (tiene), ffmpeg (pendiente), faster-whisper (pendiente), GoHighLevel Academia (portal/membership), Vault Obsidian, ComfyUI local 24GB (estudio Emilia)
- Vault: `wiki/raw/`, `wiki/estudio/`, `wiki/glosario/software/gohighlevel/`, `activos/reuniones/ghl-academia/`, `scripts/transcribir_ghl.py`

### Hechos/decisiones reutilizables

- Decisión: academia GHL no tiene descarga directa — pipeline oficial es **OBS + ffmpeg + faster-whisper** (0 licencia), extensión GoHighLevel Downloader queda como opción B paga pero no requerida
- Decisión: conocimiento metodología NO va a `wiki/software` — va a `wiki/estudio/` (metodología) + glosario puntual en `gohighlevel/` — patrón para futuros ingests de academias/cursos
- Decisión: Sprint diagnóstico Emilia = etapas 1+2 completas del ciclo 6, con demo mini de 3-6 — framing "30 días para entender y dejar prototipo, acreditable"
- Hecho: `faster-whisper` medium en CPU int8 tarda 2-5 min para 30 min audio es — viable en máquina 32GB RAM sin GPU
- Hecho: binarios siempre en `activos/` gitignored, md solo referencias — regla AGENTS.md Prioridad máxima respetada
- Reutilizable: script `transcribir_ghl.py` auto-detecta ffmpeg en 3 rutas, reutiliza audio si ya existe, genera raw con frontmatter listo para ingest — template para futuros cursos

## Pendiente

- [ ] Usuario captura primer video con OBS → corre `transcribir_ghl.py` → pega transcript → yo ejecuto ingest completo (metodología + 6 glosario + servicios + 07-propuesta-diagnostico)
- [ ] Descargar ffmpeg portable a `P:\00-repos\ffmpeg\bin\` y `pip install faster-whisper` en comfyenv
- [ ] Crear 6 entradas glosario + 2 páginas estudio cuando llegue primer transcript (no inventar contenido sin fuente verbatim)
- [ ] Validar enlaces oficiales con webfetch antes de publicar glosario (regla AGENTS.md)

## Referencias

- Plan: [[specs/260907-ghl-ingest-6-etapas]]
- Script: `scripts/transcribir_ghl.py`
- Vault: [[proyectos/STUDIO_OS-Emilia/index]] · [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os]] · [[AGENTS.md]]
- Web: https://help.gohighlevel.com/support/solutions/articles/155000002841-how-to-enable-call-transcriptions-for-recorded-calls
- Web: https://github.com/serpapps/gohighlevel-downloader
- Web: https://obsproject.com/es
