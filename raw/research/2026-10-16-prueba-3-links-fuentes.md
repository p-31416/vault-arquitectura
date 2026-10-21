---
tipo: investigacion-sherlock
fecha: 2026-10-16
fuentes: 3 (1 YT + 2 IG desde Sheet Fuentes-Inbox)
idioma: EN (YT) / ES (IG reel) / EN (IG post)
tags: [sherlock, fuentes-inbox, instagram, youtube, prueba]
estado: propuesta
---

# Prueba extractores — 3 links del Sheet Fuentes-Inbox

> Prueba pedida por SOL 2026-10-16: qué trae cada extractor por tipo. Destino de estos crudos: `raw/research/` (NO wiki directo).

## 1. YouTube `5O-4dqUchsE` — VERDE

- Transcript `raw/yt/transcripts/2026-10-15_5O-4dqUchsE.en.*` vía `auto-sub (en)` (es dio 429, el fallback por idioma funcionó).
- Contenido: workflow ComfyUI para animación — concept art → proxy 3D (Trypo/GLB) → rotar/posar → still o video con GPT image. Afín a MVP_04 y línea "comfy" del Tema.
- Nota extractor: `transcribir_youtube.py` con fix singular + loop por idioma, verificado 2.º video.

## 2. Instagram reel `DecvjfcJ314` — VERDE (vía lector)

- `webfetch` directo: MURO login (solo "Instagram"). Vía lector `r.jina.ai`: autor `todo_sobre_arquitectura` + caption completa + hashtags + comentarios.
- Contenido: Shenzhen Financial Culture Center, 64.000 m², volúmenes triangulares, estructura acero, BIM (800 choques resueltos pre-obra). Tags `#arquitectura #ingenieriaestructural #shenzhen`.
- Patrón IG confirmado (spec ingesta §3.3 opción 1): caption = epígrafe natural para tags.

## 3. Instagram post `DeXAMs2Eqgh` — VERDE parcial (vía lector)

- Autor `divyannshisharma`, caption mínima ("Comment SEND…", tags `#openclaw #ai #claude #aiagents`). Post anzuelo sin contenido propio.
- Lección: caption pobre → el valor está en la IMAGEN (ver) o se descarta. Criterio: sin caption útil y sin nota de SOL, prioridad baja.

## Conclusión extractores

| Tipo | Directo | Vía lector | Recomendado pipeline |
|---|---|---|---|
| YT | subs vía yt-dlp | — | `transcribir_youtube.py` |
| IG post/reel | login wall | caption+autor+tags+comentarios | lector + ficha (caption=epígrafe) |
| IG sin caption | — | solo autor/tags | pedir nota a SOL o descartar |

## Propuestas wiki (esqueleto, con s)

- Referente: Shenzhen Financial Culture Center → `wiki/glosario/referentes/` (ficha obra + estructura + BIM).
- Fuente YT ComfyUI-animación → `wiki/fuentes/` (línea comfy).
