---
tipo: software
software: obs
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [glosario, software, obs]
---

# OBS Studio

> Software libre (GPL) para captura pantalla + audio. Migrado de `obs/` (index.md + captura-pantalla-audio.md) a archivo único.

- [[#Descripción]]
- [[#captura-pantalla-audio]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Descripción

> Fuente: `obs/index.md` — `tipo: indice` (2026-09-07).

Software libre (GPL) para captura pantalla + audio.

## captura-pantalla-audio

> Fuente: `obs/captura-pantalla-audio.md` — `comando: captura-pantalla-audio, software: obs, tipo: comando` (2026-09-07).

Grabar academia GHL que bloquea descarga directa.

### Pasos

1. Fuentes `+` → `Captura de pantalla` + `Captura de audio de salida`
2. Configuración → Salida → `mkv` o `mp4`, Audio 44.1 kHz
3. `Iniciar grabación` → reproducir lección → `Detener` → guarda en `activos/videos/` como `<prefijo>-YYYY-MM-DD-<slug>.mkv` (ej. `ghl-...`, futuro `ytb-...`)

### Tips

- Desactivar aceleración hardware Chrome `Configuración > Sistema` para evitar pantalla negra
- Atajo Windows sin OBS: `Win+Alt+R` (Xbox Game Bar)

### Uso en vault

Paso 1 de `specs/260907-ghl-extraccion-automatica.md` → entrada a `scripts/transcribir_ghl.py`

---

## Conceptos relacionados

- [[wiki/glosario/software/ffmpeg|ffmpeg]]
- [[wiki/glosario/software/faster-whisper|faster-whisper]]

## Referencias

- [OBS Project (español)](https://obsproject.com/es) (verificado 2026-09-07 — migrado de `captura-pantalla-audio.md`)
