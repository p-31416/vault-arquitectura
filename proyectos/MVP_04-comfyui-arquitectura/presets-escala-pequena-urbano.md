---
tipo: guia
mvp: 04
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_04, presets, escala-pequena, urbano, gaudi, gratis]
idioma: es
---

# Presets escala pequeña → urbano Gaudí (todo $0)

> Uso no diario: flujos predefinidos para no re-armar. Base: RX 570 DirectML + Pollinations free + Comfy Cloud Free. Sin pod pago, sin APIs pagas.
> Origen: [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-vivienda/01-index|WF-vivienda]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01|n_03 controlnet]] · [[proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v5_fachada_hormigon_madera/01-index|WF_v5]] · [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz Gaudí]].

## Escala pequeña (interior / objeto / casa)

| Preset | Para que | Reusa | Cambias solo | Modelo $0 | Tiempo |
|---|---|---|---|---|---|
| P1-angulo | cambiar ángulo visión | n_03 dual Canny+Depth | `image` croquis + prompt `eye-level / aerial / axon 30/60` | Realmix SD1.5 local | ~90s |
| P2-camara | cambiar lente | WF-vivienda SDXL | prompt `24mm tilt-shift / 35mm / 50mm, depth of field f/4` | Juggernaut XL v9 local | ~6-10min |
| P3-luz | mañana / tarde / noche | IC-Light `iclight_sd15_fc` + DA3 | `lighting: morning soft / golden hour / night interior warm` + strength | Realmix local | ~2min |
| P4-muebles | agregar muebles | sd-v1-5-inpainting + mask 75% | máscara zona + `add wooden chair, linen sofa, keep walls` | inpainting local | ~2min |
| P5-material | cambiar sol/muro | WF_v5 hormigon-madera | prompt material + denoise 0.4-0.6 | Juggernaut / RealVisXL Lightning | ~2-7min |
| P6-fondo | cielo / patio | img2img denoise 0.45 | `keep geometry, replace background with planted patio` | RealVisXL Lightning 4-6 steps | ~1-5min |

Prompt EN base P1-P6: `keep geometry exactly, MATCH CAMERA OF INPUT, {cambio}, architectural photography, raw photo`.

## Puente a urbano Gaudí (misma lógica, otra escala)

| Urbano | Equivale a pequeño | Corre $0 donde |
|---|---|---|
| U1-plaza 1:500 | P1-angulo + P6-fondo | SDXL + ControlNet canny sobre DXF export PNG |
| U2-massing | P1 + P5-material | croquis → render denoise 0.6 local, final pod free (Cloud Free 400cr) si pesa |
| U3-sol plaza | P3-luz | IC-Light tarde oeste Pasión / mañana este |
| U4-mobiliario premio | P4-muebles | inpaint banco/farola/barandilla en foto plaza real |
| U5-hero A1 | P2-camara + P5 | vista hiperreal 1216x832 + upscale RealESRGAN x4 + hires denoise 0.25 |
| U6-workflow | — | diagrama SVG gratis, no IA |

## Loop Telegram $0 sin agente

Foto Rhino / croquis + caption = prompt directo. n8n IF: si trae máscara → P4/U4 inpaint, si no → P1/P5 img2img. Sin Claude, sin copy-paste, sin Hermes paralelo. Pollinations `flux.1-schnell` para borrador, local para keeper.

## Regla uso ocasional

No re-armar grafo: duplica preset, cambia 1 variable (seed fija, 1 param), registra en `02-WF-log` con veredicto keeper/descartar. Lo urbano reusa preset chico con `megapixels` 1MP y `STRICT CAMERA LOCK`.
