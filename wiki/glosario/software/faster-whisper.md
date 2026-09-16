---
tipo: software
software: faster-whisper
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, faster-whisper]
---

# faster-whisper

> Fork optimizado de OpenAI Whisper (CTranslate2) para transcripción local en CPU/GPU. Migrado de `faster-whisper/` (index.md + transcribe.md) a archivo único.

- [Descripción](#descripcion)
- [transcribe](#transcribe)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Descripción

> Fuente: `faster-whisper/index.md` — `tipo: indice` (2026-09-07).

Fork optimizado de OpenAI Whisper (CTranslate2) para transcripción local en CPU/GPU. Usado en pipeline GHL → vault para transcribir capturas OBS de academia GoHighLevel.

## transcribe

> Fuente: `faster-whisper/transcribe.md` — `comando: transcribe, software: faster-whisper, tipo: comando` (2026-09-07).

Transcribe audio mp3 a texto con timestamps, en CPU sin GPU.

### Sintaxis

```python
from faster_whisper import WhisperModel
model = WhisperModel("medium", device="cpu", compute_type="int8")
segments, info = model.transcribe("captura.mp3", language="es", vad_filter=True)
for seg in segments:
    print(f"[{seg.start:.1f} → {seg.end:.1f}] {seg.text}")
```

- `medium` balance es/co para acento argentino; `small` más rápido, `large-v3` más preciso
- `compute_type=int8` liviano para 32GB RAM; `vad_filter=True` filtra silencios

### Instalación libre

```bash
P:\Anaconda\envs\comfyenv\python.exe -m pip install faster-whisper
```

### Uso en vault

`scripts/transcribir_ghl.py: transcribe()` — genera `.txt` + `.srt` + `wiki/raw/*.md` desde capturas OBS de academia GHL. Pipeline: `OBS mkv → ffmpeg mp3 → faster-whisper txt`.

---

## Conceptos relacionados

- [[wiki/glosario/conceptos/cerebro-digital-karpathy]]
- [[wiki/glosario/software/ffmpeg|ffmpeg]]

## Referencias

- [SYSTRAN faster-whisper](https://github.com/SYSTRAN/faster-whisper) (verificado 2026-09-07 — migrado de `transcribe.md`)
- [OpenAI whisper (modelo base)](https://github.com/openai/whisper) (verificado 2026-09-07)
