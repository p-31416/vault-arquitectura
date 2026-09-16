---
tipo: metodologia
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [automatizacion, ghl, transcripcion, obs, faster-whisper, ingest]
---

# Plan — Extracción automática de academia GHL (OBS → vault, sin licencia)

> Cómo grabar con OBS y que **el resto sea automático**: audio → transcript → `wiki/raw/` → vault + glosario + servicios Pitau Tech.

## Objetivo

Cada video útil de academia GHL (portal/membership sin descarga) debe quedar en 1 comando como conocimiento permanente, sin trabajo manual repetitivo. Vos solo grabás con OBS; el script hace el resto hasta `wiki/raw/` y yo (o un job local) distribuye al vault.

## Flujo automático (100% libre)

```
[vos]  Play academia GHL  ──OBS──►  activos/videos/ghl-2026-09-07-6-etapas.mkv
                                    │
[script]  scripts/transcribir_ghl.py ──ffmpeg──► .mp3 ──faster-whisper (CPU medium, es)──►
                                    ├──► .txt + .srt (mismo dir)
                                    └──► wiki/raw/YYYY-MM-DD-ghl-<stem>.md  (frontmatter + transcript)
                                    │
[ingest]  yo / o script ingest ─────►  wiki/estudio/metodologia-ciclo-6-etapas.md
                                    ├──► wiki/glosario/software/gohighlevel/*.md (6 etapas + términos nuevos)
                                    ├──► wiki/estudio/servicios-pitau-tech-arquitectura.md
                                    └──► proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-*.md
                                    └──► log.md + índices
```

**Vos hacés solo el primer cuadro (OBS). El resto es 1 comando.**

## Requisitos (una vez, sin licencia)

1. **ffmpeg portable** (MIT): bajar `ffmpeg-master-latest-win64-gpl.zip` de [FFmpeg-Builds](https://github.com/BtbN/FFmpeg-Builds/releases) → extraer `bin/ffmpeg.exe` a `P:\00-repos\ffmpeg\bin\ffmpeg.exe` (o `vault/ffmpeg/bin/`). No requiere instalador.

2. **faster-whisper** (MIT, CPU):
```bash
P:\Anaconda\envs\comfyenv\python.exe -m pip install faster-whisper
```

## Uso diario (30 segundos por video)

```bash
# 1. Grabar con OBS: fuente "Captura de pantalla" + "Captura de audio de salida" → Iniciar grabación → reproducir lección → Detener
#    Guardar como: activos/videos/ghl-2026-09-07-nombre-leccion.mkv

# 2. Un comando (extrae audio + transcribe + crea raw):
P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ghl-2026-09-07-nombre-leccion.mkv" --model medium --language es

# Salida:
#   activos/videos/ghl-2026-09-07-nombre-leccion.mp3
#   activos/videos/ghl-2026-09-07-nombre-leccion.txt
#   activos/videos/ghl-2026-09-07-nombre-leccion.srt
#   wiki/raw/ghl-2026-09-07-nombre-leccion.md  â† pegame este para el ingest
```

**Opciones:** `--model small` (más rápido, menos preciso), `--model large-v3` (más preciso, más lento), `--language es` (default).

## Qué hace el script `transcribir_ghl.py:1`

- Busca `ffmpeg` en `P:\00-repos\ffmpeg\bin\`, `vault/ffmpeg/bin/`, o `PATH` — no falla si lo movés
- Extrae audio con `ffmpeg -y -i video -vn -acodec libmp3lame -q:a 2` — si el archivo ya tiene `.mp3` más nuevo, lo reutiliza
- Transcribe con `WhisperModel(medium, device=cpu, compute_type=int8, vad_filter=True)` — diarización básica + timestamps
- Escribe `wiki/raw/*.md` con frontmatter `tipo: raw` + transcript verbatim + referencia al binario en `activos/` (gitignored, regla `AGENTS.md: Prioridad máxima`)

## De `wiki/raw/` al vault (automático paso 2)

Cuando me pegás el `wiki/raw/*.md` (o el `.txt`), yo ejecuto sin preguntar:

1. **Metodología:** actualizo/creo `wiki/estudio/metodologia-ciclo-6-etapas.md` con las 6 etapas limpias
2. **Glosario:** creo/actualizo `wiki/glosario/software/gohighlevel/*.md` — una entrada por **cada término nuevo** que aparezca en el transcript (no solo las 6 etapas: si el video menciona "workflow", "pipeline", "snapshot", etc., cada uno va al glosario con definición + link oficial verificado con `webfetch`)
3. **Servicios:** actualizo `wiki/estudio/servicios-pitau-tech-arquitectura.md` — mapeo a estudios ARG (libro obra papel → digital, fotos celular → registro estructurado, planos Ley 24.335)
4. **Cliente:** actualizo/creo `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-*.md` si aplica a Emilia
5. **Ãndices:** `wiki/estudio/index.md`, `wiki/glosario/software/gohighlevel/index.md`, `proyectos/STUDIO_OS-Emilia/index.md`, `log.md` (entrada nueva arriba)

> **Automatización total futura (opcional, también libre):** agregar al script un `watch` con `watchdog` (`pip install watchdog`) que observe `activos/videos/ghl-*.mkv` y dispare `transcribir_ghl.py` solo + `ollama run qwen2.5:7b` para resumir a `wiki/estudio/` sin intervención. Queda para Fase 2 si lo pedís.

## Glosario — qué se registra

Cada video aporta términos. El plan base ya contempla 6, pero **todo término nuevo se registra** en `wiki/glosario/software/gohighlevel/` o `wiki/glosario/software/<software>/` según corresponda:

- Obligatorios ciclo 6: `relevamiento-requerimientos`, `analisis-diseno-solucion`, `implementacion-tecnica`, `pruebas-internas`, `entrenamiento-agentes`, `puesta-produccion`
- Derivados esperados: `workflow`, `trigger`, `pipeline`, `snapshot`, `subcuenta`, `membership`, `portal` — cada uno con frontmatter, definición 2 líneas, uso en Pitau Tech, y link oficial GHL verificado (404 check)

## Checklist implementación

- [ ] Descargar ffmpeg portable → `P:\00-repos\ffmpeg\bin\ffmpeg.exe`
- [ ] `pip install faster-whisper` en `comfyenv`
- [ ] Probar con 1 video corto (2 min) → verificar `wiki/raw/*.md` se crea
- [ ] Pegar raw para primer ingest completo → validar glosario + metodología
- [ ] (Opcional) `pip install watchdog` + modo watch para 100% automático

## Referencias

- Plan detallado: [[specs/260907-ghl-ingest-6-etapas]]
- Script: `scripts/transcribir_ghl.py`
- Sesión: [[raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault]]
