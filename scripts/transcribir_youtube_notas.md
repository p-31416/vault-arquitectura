# Notas — `transcribir_youtube.py` (archivo paralelo didáctico)

_Cómo leer: cada sección explica un bloque del script en español simple. El script es runnable; este archivo es para aprender._

## Idea general (1 frase)

El script trae el **transcript verbatim** de un video de YouTube por el camino más barato posible: primero pide los **subtítulos** (1-2 requests, sin descargar nada) y solo si no hay, baja el audio y lo transcribe localmente con Whisper.

## Bloques del script

- **`video_id(arg)`** — acepta ID suelto (`RAMs89SS6cM`) o URL completa; la regex extrae los 11 caracteres. Así da igual lo que pegues.
- **`fetch_subtitles(vid, tmp)`** — dos intentos con `yt-dlp`: primero subtítulos manuales (`manual-sub`, los que subió el autor = mejor calidad), después automáticos (`auto-sub`). Pide `es` y luego `en`. Si llega `.vtt`, lo convierte a `.srt` (ver abajo). No descarga video ni audio: `skip_download=True`, por eso no gasta casi nada ni calienta la IP.
- **`vtt_to_srt(vtt)`** — YouTube a veces entrega VTT (formato web con cabecera `WEBVTT`). La función tira la cabecera, saca etiquetas `<...>`, renumera los cues y cambia el punto decimal por coma (formato SRT). Conversión mínima pero suficiente para transcript.
- **`srt_to_txt(srt)`** — genera el `.txt` con el **mismo formato que `transcribir_ghl.py`**: una línea `[HH:MM:SS] texto` por cue. Así `@contenidos` lee igual un transcript de GHL que uno de YouTube.
- **`whisper_transcribe(...)`** — fallback pesado: baja **solo audio** (`bestaudio`, sin video = archivo chico), lo pasa por `faster-whisper` en CPU int8 (igual que el molde GHL), genera el SRT con el mismo formato de timestamps y **borra el audio temporal** (el crudo es el transcript, no el mp3).
- **`main()`** — idempotente: si el `.srt` ya existe, no re-genera (hay que borrarlo a mano para forzar). Hace `sleep(5)` antes de pedir (throttling liviano), crea `raw/yt/transcripts/` si falta y deja 3 archivos: `.srt` + `.txt` + `.origen.json` (qué fuente se usó y cuándo — trazabilidad §10 del spec).
- **`.origen.json`** — dice `auto-sub`, `manual-sub` o `whisper`. Si un transcript se ve raro, este archivo explica por qué (los auto-sub tienen más errores que Whisper small).
- **Limpieza de artefactos** (`clean_sub_text` + decodificación por intentos utf-8-sig→utf-8→cp1252): los subs YT traen NBSP, guiones inseparables y apóstrofes mutilados a `à` (solo se restauran entre letras — el `voilà` legítimo del video 1 sobrevivió como testigo). Bugs cazados el primer día: regex con `0-0` en vez de `0-9` y línea muerta en `vtt_to_srt`.

## Archivos que genera (4 por video, prefijo fecha ISO)

`YYYY-MM-DD_<id>.<lang>.md/.srt/.txt` + `YYYY-MM-DD_<id>.origen.json` — el prefijo da orden cronológico nativo por texto en Obsidian y Explorer (opción A, sin subcarpetas: la carpeta es territorio IA). El caché tolera nombres con o sin prefijo (`*{vid}.*.srt`).

- **`.md`** — el envoltorio visible en Obsidian: frontmatter (`tipo: raw`, `video_id`, `url`, `idioma`, `fuente_origen`, links a `.srt`/`.txt`) + transcript verbatim. Es lo que abrís para leer; mismo rol que el `wiki/raw/*.md` del molde GHL.
- **`.srt` / `.txt`** — el crudo máquina: `.srt` con timestamps exactos, `.txt` con formato `[HH:MM:SS]` que lee `@contenidos`.
- **`.origen.json`** — trazabilidad mínima para scripts (qué fuente se usó y cuándo); la misma info vive en el frontmatter del `.md` para lectura humana.

## Decisiones tomadas (y por qué)

1. **Subs antes que Whisper**: 10 segundos vs. varios minutos, y cero cómputo local.
2. **Manuales antes que automáticos**: los del autor tienen puntuación y términos correctos.
3. **`small` como modelo fallback** (no `medium` como GHL): videos YT en inglés se transcriben bien con `small` y tardan la mitad; se puede subir con `--model medium`.
4. **Sin `ffmpeg` requerido**: al no post-procesar audio (se transcribe el `.m4a`/`.webm` directo vía `av`), el script no depende del PATH de ffmpeg.
5. **Tope ~10 Whisper/día**: el límite lo pone la CPU (varios minutos por video), no YouTube — documentado en el docstring.
