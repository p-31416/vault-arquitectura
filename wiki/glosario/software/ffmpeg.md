---
tipo: software
software: ffmpeg
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [glosario, software, ffmpeg]
---

# FFmpeg

> Herramienta libre (GPL) para extraer/convertir audio/video. Usada en pipeline GHL → vault para extraer audio de capturas OBS. Migrado de `ffmpeg/` (index.md + ffmpeg-extract-audio.md) a archivo único.

- [[#Descripción]]
- [[#ffmpeg-extract-audio]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Descripción

> Fuente: `ffmpeg/index.md` — `tipo: indice` (2026-09-07).

Herramienta libre (GPL) para extraer/convertir audio/video. Usada en pipeline GHL → vault para extraer audio de capturas OBS.

## ffmpeg-extract-audio

> Fuente: `ffmpeg/ffmpeg-extract-audio.md` — `comando: ffmpeg-extract-audio, software: ffmpeg, tipo: comando` (2026-09-07).

Extrae audio mp3 de video mkv/mp4 capturado con OBS para transcripción.

### Sintaxis

```bash
ffmpeg -y -i "activos/videos/ghl-2026-09-09-captura.mkv" -vn -acodec libmp3lame -q:a 2 "activos/videos/ghl-2026-09-09-captura.mp3"
```

- `-y` sobrescribe, `-vn` sin video, `-acodec libmp3lame -q:a 2` mp3 VBR alta calidad.

### Instalación libre (portable, sin licencia)

Bajar `ffmpeg-master-latest-win64-gpl.zip` de [FFmpeg-Builds Releases](https://github.com/BtbN/FFmpeg-Builds/releases) → extraer `bin/ffmpeg.exe` a `P:\00-repos\ffmpeg\bin\ffmpeg.exe`. Agregar a PATH o usar ruta completa.

### Uso en vault

Pipeline `scripts/transcribir_ghl.py: extract_audio()` — auto-reutiliza mp3 si ya existe y es más nuevo que el video.

---

## Conceptos relacionados

- [[wiki/glosario/software/faster-whisper|faster-whisper]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- [FFmpeg — documentación oficial](https://ffmpeg.org/documentation.html) (verificado 2026-09-07 — migrado de `ffmpeg-extract-audio.md`)
- [FFmpeg-Builds Releases (binarios Windows)](https://github.com/BtbN/FFmpeg-Builds/releases)
