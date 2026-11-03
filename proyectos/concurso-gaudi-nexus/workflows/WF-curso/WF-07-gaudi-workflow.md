---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 7
slug: gaudi-workflow
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-07, curso-ai-gaudi, gaudi, img2img]
idioma: es
---

# WF-07 — Gaudí Workflow + geometría → piedra denoise 0,55

> Unifica [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/flujo-07-gaudi-workflow\|flujo-07]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/WF-07_sdxl\|WF-07_sdxl]].

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame Gaudí workflow + INSTRUCTION.md variante B | pendiente link Sol |
| Video módulo 7 (35 min 42 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow\|transcripción]] |

## 2. Flujo del curso (resumen)

Dos pasos image-to-image separados: **paso 1 geometría** (agente `Rhino to Image Gaudí` con INSTRUCTION.md variante B + Nano Banana 2, 2K / reasoning high, `Compare Images`, doble corrida) → **paso 2 estética** (workflow Rhino-to-Image + LoRA premium/basic, prompt materialidad, geometría intacta).

Dial Escala Gaudí 0-10: 7 ejemplo 1 · 8 ejemplo 2 · default 7 (6-8 catenarias completas, columnas arbóreas, interior abovedado). Encuadre: detalle/primer plano a altura de ojos, no vista lejana. Prompt del agente siempre leído antes de pegar.

## 3. WF SDXL vista

JSON: `workflow_WF-07_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · 10 nodos · img2img · seed 77 · **denoise 0,55** · prefijo `gx-WF07`. `LoadImage PONER-RUTA-boceto_geometria.png` → 1024² → `VAEEncode` → `KSampler` → `VAEDecode`.

+ `gaudi workflow pass, catenary geometry emerging from sketch lines, charcoal construction lines with photorealistic stone fill, medium intensity, branching columns taking shape, architectural render`. Dial: 0,40 color · **0,55 este WF** · 0,65 WF-03 · 0,75 explora. Con ControlNet clava la geometría.

## 4. Cómo lo adaptamos

Paso 1 con FLUX.2 klein 9B edición en pod + INSTRUCTION.md variante B ya en vault · paso 2 reutiliza WF-rhino-to-image con LoRA · dial como parámetro de proyecto (tabla 0-2/3-5/6-8/9-10, default 7) · 2K + high como línea base · basic hoy, premium cuando se resuelva descarga.

## 5. Checks jurado

Re-escultura con reglas constructivas (no imitación) · dial registrado · prompt leído (anti-alucinación) · estética como decisión documentada · detalle a altura de ojos.
