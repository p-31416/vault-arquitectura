# mux_lecciones_curso — notas

Script que extrae las transcripciones de las lecciones del curso "AI×Gaudí" (Archademy) desde la página del área de participantes.

> Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\mux_lecciones_curso.py "G:\Mi unidad\OS-Emilia\AIxGaudi\My account - Archademy.ai.html" --out raw\yt\transcripts`

---

## 1. Cómo están escondidos los videos

El área de participantes (`/my-account/my-competitions/214/?tab=course`) es **WooCommerce**: la pestaña arma 8 paneles (uno por módulo) y cada video es un **iframe de Mux** (el CDN de video de Mux, antes Stream):

```html
<div class="archademy-course-panel is-active" data-module="intro-generative-ai" role="tabpanel">
  <div class="archademy-course-video" data-module="intro-generative-ai">
    <div class="archademy-video-ratio">
      <iframe data-src="https://iframe.mediadelivery.net/embed/719269/35e568e8-...?autoplay=false&..." >
```

Claves:

- El **`data-module`** del panel es el slug del módulo (`intro-generative-ai`, `text-to-image`, `image-to-image`, `image-to-video`, `image-to-3d`, `round-table`, `gaudi-workflow`).
- El título legible está en el nav: `<span class="archademy-course-nav-title">`.
- El **playback id** de Mux es el último tramo de la URL del iframe: `.../embed/{env}/{playback_id}`.

> Trampa: `data-module` aparece **también en los tabs del nav**. Por eso el script empareja cada iframe con el **panel** que lo contiene (primer iframe entre ese panel y el siguiente), no con el primer `data-module` que aparece.

## 2. Los subtítulos son la transcripción

Dentro del player de Mux, cada video tiene sus pistas de subtítulos:

```html
<track kind="captions" label="English" src="https://vz-4ced3a48-15e.b-cdn.net/{PLAYBACK_ID}/captions/en.vtt?ver=3" srclang="en">
<track kind="captions" label="Español" src="https://vz-4ced3a48-15e.b-cdn.net/{PLAYBACK_ID}/captions/es.vtt?ver=3" srclang="es">
```

El patrón de URL es:

```
https://{prefijo}.b-cdn.net/{PLAYBACK_ID}/captions/{idioma}.vtt
```

- El prefijo (`vz-4ced3a48-15e`) **cambia por entorno**: el script lo deduce del propio HTML.
- **No pide token ni cabeceras**: un `GET` simple devuelve **200** con el VTT completo. (El `playlist.m3u8` sí da 403, pero no hace falta: con los subtítulos ya tenemos la transcripción.)
- El curso tiene **subtítulos en inglés y en español** → las dos pistas sirven.

## 3. Conversión WebVTT → SRT → TXT

El script reusa el criterio de `scripts/transcribir_youtube.py` para que ambos caminos produzcan lo mismo:

- `.srt` — cues numerados con `HH:MM:SS,mmm --> HH:MM:SS,mmm`
- `.txt` — una línea por cue: `[HH:MM:SS] texto`
- `.md` — envoltorio con frontmatter (tipo `transcript`, módulo, idioma, fecha) + el texto plano
- `.origen.json` — metadatos de la ingesta

## 4. Salida

```
raw/yt/transcripts/2026-10-21_mux-<slug>.<lang>.md
raw/yt/transcripts/2026-10-21_mux-<slug>.<lang>.srt
raw/yt/transcripts/2026-10-21_mux-<slug>.<lang>.txt
raw/yt/transcripts/indice-curso-ai-gaudi.json   (incluye tablero Miro + contraseña)
```

## 5. Resultados medidos (2026-10-21)

| Módulo | Cues EN | Cues ES |
|--------|---------|---------|
| Introduction to Generative AI | 1268 | 1268 |
| Text-to-Image | 659 | 659 |
| Image-to-Image | 1047 | 1047 |
| Image-to-Video | 333 | 333 |
| Image-to-3D | 249 | 249 |
| The Gaudí Workflow | 454 | 454 |
| Round Table | — (404, sin subtítulos) | — |

El módulo `miro-board` no tiene video (es el panel de acceso al tablero).

**De paso**: la página trae la **contraseña del tablero Miro** (`archademy-miro-pw-code`) y su URL, así que el tablero se puede abrir sin pedirle nada a nadie.

## 6. Qué falta

- **Round Table**: sin subtítulos. Para transcribirlo hay que bajar el audio (`playlist.m3u8` → `yt-dlp -f bestaudio` → `faster-whisper`). Es una mesa redonda, de valor documental más que operativo.
