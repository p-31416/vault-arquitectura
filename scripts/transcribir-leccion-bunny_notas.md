# transcribir-leccion-bunny.py — notas

> Transcribe en local una lección del curso AI×Gaudí **que no tiene subtítulos**. Hoy el caso es el módulo 6 (Round Table, con Cas Esbach del jurado), que es el insumo del checklist de cierre de los siete workflows del concurso.

## Por qué existe

El CDN del curso (Bunny Stream) expone los subtítulos `.vtt` de cada módulo sin token, y `scripts/mux_lecciones_curso.py` los baja. El módulo 6 responde **404 en sus dos pistas**: es el único que queda fuera.

Alternativas y por qué se descartan:

| Alternativa | Por qué no va |
|-------------|--------------|
| Transcribir con una API de pago | manda el material del curso a un tercero y suma costo |
| Subir el módulo a YouTube y transcribirlo con `transcribir_youtube.py` | el video es de un curso con derechos;Sumarlo a otra plataforma es una decisión del titular, nuestra |
| Mirar el video y transcribir a mano | 35 minutos de video, con el costo de tiempo que implica |

La vía local (descargar → ffmpeg → faster-whisper en CPU) es la que ya usa `scripts/transcribir_ghl.py` para las capturas OBS del estudio: mismo motor, misma salida, cero costo.

## Requisitos (ya instalados)

- `P:\Anaconda\envs\comfyenv\python.exe` con **faster-whisper** (`pip install faster-whisper` si falta).
- **ffmpeg** portable: `P:\00-repos\ffmpeg\bin\ffmpeg.exe` (el script lo busca ahí y en el PATH).
- Espacio en disco: ~540 MB para el mp4 + ~50 MB para el mp3.

## Uso

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir-leccion-bunny.py --modulo round-table --language en
```

Opciones:

| Flag | Por defecto | Para qué |
|------|-------------|----------|
| `--modulo` | (obligatorio) | el slug del módulo tal como aparece en `indice-curso-ai-gaudi.json` (ej: `round-table`, `text-to-image`) |
| `--language` | `en` | idioma del audio. El curso se publica en inglés con subtítulos, así que `en` |
| `--model` | `medium` | `tiny` / `base` / `small` / `medium` / `large-v3`. `medium` es el equilibrio en CPU; `large-v3` afina nombres propios a costa de tiempo |
| `--out` | `raw/yt/transcripts` | carpeta de salida |

## Qué hace, en orden

1. Lee `raw/yt/transcripts/indice-curso-ai-gaudi.json` y busca el **playback id** del módulo.
2. Baja el video del CDN a `activos/curso-ai-gaudi/videos/mux-<slug>.mp4` con el header `Referer: https://iframe.mediadelivery.net/`, que es lo que el CDN exige (sin él responde 403).
3. Extrae el audio a `.mp3` con ffmpeg.
4. Transcribe con faster-whisper en CPU (`int8`), con filtro de voz activa.
5. Escribe `.md` + `.srt` + `.txt` en `raw/yt/transcripts/` con la convención del vault (`YYYY-MM-DD_mux-<slug>.<lang>`), la misma que usa `mux_lecciones_curso.py`.

Si el video ya está descargado, el script lo reutiliza: una segunda corrida no vuelve a bajar los 538 MB.

## Salida esperada

```
[video] bajando (puede tardar varios minutos): https://vz-.../68e094ac-.../play_720p.mp4
[video] listo: mux-round-table.mp4 (537.9 MB)
[audio] extrayendo con ffmpeg: mux-round-table.mp4
[whisper] modelo=medium idioma=en (corre en CPU, puede tardar)
[whisper] detectado: idioma=en prob=0.98 duracion=2104.3s
[out] md:  raw/yt/transcripts/2026-10-29_mux-round-table.en.md
[out] srt: raw/yt/transcripts/2026-10-29_mux-round-table.en.srt
[out] txt: raw/yt/transcripts/2026-10-29_mux-round-table.en.txt
```

## Qué hacer después

1. Volcar la transcripción a `proyectos/concurso-gaudi-nexus/flujos/flujo-06-round-table.md` (misma estructura que las otras seis fichas: ficha → flujo → "Cómo lo adaptamos" → "Checks contra el criterio del jurado").
2. Completar `proyectos/concurso-gaudi-nexus/criterio/criterio-jurado.md` con los criterios que el jurado explicita.
3. Copiar los checks al `04-backlog.md` de cada uno de los siete workflows.

## Notas de aprendizaje

- **El `Referer` no es opcional**: el CDN de Bunny valida que la petición venga del player. Es la misma razón por la que `mux_lecciones_curso.py` funcionó con los `.vtt`.
- **`WhisperModel(modelo, device="cpu", compute_type="int8")`** es el patrón que ya usan `transcribir_ghl.py` y `transcribir_youtube.py`: en una PC sin GPU dedicada, int8 es lo que hace viable el tiempo de cómputo.
- **`vad_filter=True`** descarta los tramos de silencio: en una mesa redonda con silencios largos, recorta el cálculo y evita los segmentos inventados.
- El video se guarda en `activos/`, que está en el `.gitignore`: el material del curso no entra al repositorio.

## Conceptos relacionados

- [[scripts/mux_lecciones_curso|mux_lecciones_curso.py]] · [[scripts/transcribir_youtube|transcribir_youtube.py]] · [[scripts/transcribir_ghl|transcribir_ghl.py]] · [[proyectos/concurso-gaudi-nexus/flujos/flujo-06-round-table|Ficha del módulo 6]] · [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado|Criterio del jurado]] · [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|Plan maestro de workflows]]
