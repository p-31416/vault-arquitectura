---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-04, txt2img, keyframe, video]
idioma: es
---

# WF-04 — Keyframe de video 1280×768

> JSON: `workflow_WF-04_sdxl.json` · 7 nodos · 1280×768 · seed 100 · 30 steps · cfg 4
> Estado: sin validar contra servidor (R4 pendiente).

## 1. Qué tipo de flujo es

**Txt2img 16:9 con vocación de fotograma.** Genera el primer cuadro de un plano fijo al atardecer. La imagen no es el entregable: es la entrada del flujo imagen→video (`n_07-img2video`, LTX 2.3 i2v).

Por eso el prompt insiste en "wide establishing shot", "fixed tripod view" y "cinematic keyframe": busca un cuadro quieto, sin figuras en movimiento, que el modelo de video pueda animar sin inventar geometría.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

Alternativa directa: **RealVisXL v5.0**, que da una piel de imagen más limpia para animar. Para la etapa de video el modelo cambia por completo: LTX 2.3 o WAN 2.2 I2V en RunPod.

Detalle de modelos: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "wide establishing shot, catenary arches pavilion at dusk, fixed tripod view, warm interior glow, still air, cinematic keyframe, photorealistic, 8k uhd, masterpiece" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo del set **+ "moving people, motion blur"** |
| 4 | `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | 1280×768 (16:9), batch 1 |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, denoise 1,0, seed 100 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF04-keyframe` |

## 4. Parámetros y por qué

| Parámetro | Valor | Razón |
|---|---|---|
| Resolución | 1280×768 | 16:9 exacto: el formato que espera el modelo de video |
| Steps | 30 | Base suficiente para un cuadro que después se anima |
| CFG | 4 | Coherencia de luz sin dureza |
| Seed | 100 | Fija el plano |
| Negativo extra | `moving people, motion blur` | Un keyframe con gente en movimiento anima mal |

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Plano más abierto | 1280×768 → 1344×768 | Más contexto de parque |
| Vertical para reels | 768×1280 | Cambia toda la composición |
| Atardecer más marcado | Añadir "orange sky, long shadows" | Más contraste de hora |
| Amanecer | Cambiar "dusk" por "dawn, blue hour" | Paleta fría |
| Movimiento sugerido | Añadir "distant walking figures" **solo** si el video los va a animar | Riesgo de figuras deformes |
| Serie de keyframes | Cambiar seed manteniendo todo lo demás | Tres cuadros distintos para tres planos |

Regla: el keyframe define el encuadre del video. Todo lo que se quiera ver moverse tiene que existir ya en el cuadro.

## 6. Qué mirar en el resultado

Horizonte recto, simetría del pabellón estable, ausencia de figuras y de árboles movidos, luz interior encendida contra cielo del atardecer. Si hay elementos a medio dibujar, el modelo de video los va a amplificar.

## 7. Pendientes

- R4 contra `/object_info`.
- Encadenar con `n_07-img2video` (LTX 2.3 i2v, R4 pendiente) o WAN 2.2 I2V en RunPod.
