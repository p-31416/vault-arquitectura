---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
slug: earth2rhino-video-01
video_id: uIhX4IYBobc
titulo_video: "Google Earth to Rhino Made Easy – Free Workflow (2026)"
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [earth2rhino, rhino, google-earth, plugin, sitio, sagrada-familia]
idioma: es
generado_por: scripts/transcribir_youtube.py
transcript: raw/yt/transcripts/2026-10-29_uIhX4IYBobc.en.md
---

# Ficha video 01 — Google Earth to Rhino Free Workflow (2026)

> Fuente verbatim: `raw/yt/transcripts/2026-10-29_uIhX4IYBobc.en.md` (generado por `scripts/transcribir_youtube.py`, fuente `manual-sub`, 1 cue). Video: `https://www.youtube.com/watch?v=uIhX4IYBobc`. Duración medida por `yt-dlp`: 128 s.

## Lo que el transcript dice (todo lo audible)

| # | Dato | Valor literal | Timestamp |
|---|---|---|---|
| 1 | Requisito previo plugin | "Before of starting the plugin remember that Google Chrome must be completely closed" | [00:00:42] |

## Lo que el título promete (no dicho en el audio)

- Flujo gratuito 2026 de Google Earth → Rhino.
- El requisito de cerrar Chrome indica plugin que automatiza Chrome (navegador embebido o scrape de tiles). Nombre del plugin: **no dicho en el video** (ver en pantalla).
- Formato exportado (OBJ/FBX/malla/textura): **no dicho en el video** (ver en pantalla).
- Georreferencia, escala, LOD, tamaño de área: **no dicho en el video** (ver en pantalla).

## Lectura para el estudio

- Este video es **demo visual con música**, sin narración. El transcript de 1 cue es correcto y completo en lo audible; lo técnico está en imagen, no en audio.
- Hipótesis a validar viendo el video a mano: plugin tipo scrape de Earth (requiere Chrome cerrado para tomar el puerto/perfil). Si es scrape de Google Earth, arrastra la misma restricción de licencia que el video 02 (ver comparativa).
- Para la Sagrada Família sirve como vía rápida de massing de manzanas Eixample, no como base legal de entrega.

## Vacíos (ver en pantalla antes de Fase C)

1. Nombre + versión del plugin y dónde se instala (PackageManager / `rhi` / Grasshopper).
2. Pasos en pantalla: selección de área, LOD, export, import a Rhino, unidades.
3. Si trae textura y georreferencia o solo malla cruda.
4. Licencia del material resultante (ToS Google Earth).

## Cómo lo adaptamos

| Lo que hace el video | Lo que hacemos nosotros | Por qué |
|---|---|---|
| Plugin gratuito con Chrome cerrado, demo visual | Ver el video a mano 2 min y anotar nombre del plugin + pasos en esta ficha | Sin ese dato no hay workflow repetible |
| Import directo de Earth | Usarlo solo como capa `SF-CONTEXTO-GOOGLE` de calibración, apagable | La entrega final se construye sobre open-data (ver comparativa) |
| Sin narración | No transcribir más: el crudo queda como está (1 cue válido) | Whisper local ya probado: 0 cues (sin voz) |

## Checks contra el criterio del jurado

- [ ] Lógica constructiva: el massing importado no sustituye criterio propio — pendiente.
- [ ] Trazabilidad: fuente + licencia anotadas antes de modelar — pendiente.
