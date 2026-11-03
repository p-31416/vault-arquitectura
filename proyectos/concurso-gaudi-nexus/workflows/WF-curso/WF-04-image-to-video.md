---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 4
slug: image-to-video
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-04, curso-ai-gaudi, sdxl, video, keyframe]
idioma: es
---

# WF-04 — Image-to-Video + keyframe 1280×768

> Unifica [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/flujo-04-image-to-video\|flujo-04]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/WF-04_sdxl\|WF-04_sdxl]].

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame módulo 4 | pendiente link Sol |
| Video módulo 4 (26 min 22 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-image-to-video\|transcripción]] |

## 2. Flujo del curso (resumen)

Seedance 2.0 vía API en ComfyUI: plantilla 1 imagen (bypass ramas extra) · adaptive · 7-8 s prueba / 15 s duplica costo · 720 prueba · 480/1080 concurso · 4K final · `generate audio` no abarata · seed irrelevante.

Costo: 320 créditos 720p/7s · 148 baja · 1600 4K · 3400-3500 4K/15s ≈ 30 €/video. Prompt coach con `Seedance 2.0` + duración → JSON largo (releer, borrar chino si molesta) o prompt corto cuando el largo no rinde. Anotación dos colores + flecha para dirigir zoom · `transición suave / plano continuo / sin cortes` · plan B dos clips 4 s + montaje · time-lapse trípode fijo · interpolación 7 s → 14 s.

## 3. WF SDXL vista

JSON: `workflow_WF-04_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · txt2img 1280×768 16:9 · seed 100 · prefijo `gx-WF04-keyframe`. Es el **keyframe previo al video** (etapa imagen, el video corre en `n_07-img2video` LTX 2.3 i2v).

+ `wide establishing shot, catenary arches pavilion at dusk, fixed tripod view, warm interior glow, still air, cinematic keyframe, photorealistic, 8k uhd, masterpiece` · − casa + `moving people, motion blur`.

## 4. Cómo lo adaptamos

Video con LTX en pod RunPod (iteración sin créditos) · Seedance como referencia con calibración Comfy Cloud Free 400/mes · interpolación open-source · time-lapse y secuencia multi-imagen con plantillas locales.

## 5. Checks jurado

Edificio estático, entorno en movimiento · zoom a barandilla/loggia y montante-esquina a altura de ojos · costo por clip registrado (resolución/duración/modelo) · continuidad de plano.
