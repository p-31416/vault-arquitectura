---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-01, txt2img, baseline]
idioma: es
---

# WF-01 — Baseline txt2img 1024² (protocolo de comparación)

> JSON: `workflow_WF-01_sdxl.json` · 7 nodos · 1024×1024 · seed 7 · 30 steps · cfg 4
> Estado: sin validar contra servidor (R4 pendiente).

## 1. Qué tipo de flujo es

**Txt2img puro.** Es el control del set: la corrida contra la que se miden los otros seis. Su función es fijar una imagen de referencia con un prompt cerrado, para que cualquier cambio posterior (modelo, LoRA, sampler) tenga contra qué compararse.

Se usa como **protocolo**: mismo prompt, misma seed, mismo grafo; se cambia una sola pieza por corrida.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, CreativeML Open RAIL-M.

- Hugging Face: https://huggingface.co/RunDiffusion/Juggernaut-XL-v9
- Civitai: https://civitai.com/models/133005/juggernaut-xl

Modelos alternativos para este mismo WF: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función en este WF |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga Juggernaut; salidas MODEL/CLIP/VAE |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "architectural concept render, catenary arches pavilion inspired by Gaudi, stone and brick, fractal branching columns, park background, soft daylight, photorealistic, 8k uhd, masterpiece" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo: "blurry, low quality, distorted, watermark, text, cartoon, illustration, oversaturated" |
| 4 | `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | 1024×1024, batch 1 |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, denoise 1,0, seed 7 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles con el VAE del slot 2 |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF01` |

```
1 ─ MODEL ─→ 5
1 ─ CLIP  ─→ 2 ─→ 5 (positive)
1 ─ CLIP  ─→ 3 ─→ 5 (negative)
4 ─ latent ─→ 5 ─→ 6 ─→ 7
1 ─ VAE   ─→ 6
```

## 4. Parámetros y por qué

| Parámetro | Valor | Razón |
|---|---|---|
| Resolución | 1024×1024 | Cuadrado neutro, ~1 MP: el rango donde SDXL rinde |
| Steps | 30 | Mínimo recomendado por el autor (30–40) |
| CFG | 4 | Franja baja (3–7): más realismo, menos rigidez |
| Sampler | `dpmpp_2m` + `karras` | El combo recomendado por RunDiffusion |
| Seed | 7 | Fija el baseline; repetir el grafo devuelve el mismo PNG por caché |
| Denoise | 1,0 | Lienzo vacío: se parte de ruido puro |

## 5. Cambios factibles

| Quiero | Cómo | Efecto | Costo |
|---|---|---|---|
| Probar otro modelo | Cambiar `ckpt_name` en nodo 1 | Comparación limpia modelo vs modelo | 7–10 min por SDXL en la RX 570 |
| Otra semilla | `seed` en nodo 5 | Escena distinta, mismo prompt | Igual |
| 16:9 | `EmptyLatentImage` 1216×832 | Encuadre de lámina | Igual (es el de WF-02) |
| Más detalle | `steps` 30 → 40 | Microdetalle en piedra y vegetación | +25 % de tiempo |
| Estilo propio | `LoraLoader` entre nodo 1 y 5 | Aplica un LoRA sin tocar el modelo | +1–2 min |
| Nitidez | `UpscaleModelLoader` + `ImageUpscaleWithModel` tras nodo 6 | Sube resolución en píxeles | +2–4 min |

Cambios que rompen el protocolo: tocar simultáneamente prompt, seed y modelo. Una variable por corrida.

## 6. Qué mirar en el resultado

Catenarias que cierran, columnas ramificadas con lógica estructural, piedra y ladrillo legibles, fondo de parque sin edificios inventados, luz suave coherente. Este WF define el piso de calidad del set.

## 7. Pendientes

- R4: verificar `ckpt_name` y los `class_type` contra `/object_info` antes de encolar.
- Registrar la corrida en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|la matriz]] con segundos medidos.

## 8. Historial de corridas (van 3)

Protocolo: una variable por corrida; el resto del grafo intacto.

| # | Fecha | Checkpoint | Sampler | Steps | CFG | Negativo | Seed | Resolución | Segundos | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | 2026-11-02 | Juggernaut v9 | `dpmpp_2m` + `karras` | 30 | 4 | casa (7 términos) | 7 | 1024×1024 | pendiente | control del set |
| R2 | 2026-11-02 | RealVisXL v5.0 | `dpmpp_2m` + `karras` | 30 | 4 | casa (7 términos) | 7 | 1024×1024 | pendiente | mide modelo bajo receta de la casa (el autor pide 50+ para 2M) |
| R3 | 2026-11-02 | RealVisXL Lightning | `dpmpp_sde` + `karras` | 5 | 1,5 | autor (Civitai 139562) | 7 | 1024×1024 | pendiente | **descartado 2026-11-02: resultado pésimo, fuera del set** |

### Prompt v2 — plaza + mosaico Escher (2026-11-02)

Variante de escena: cambia prompt y encuadre a propósito (la comparación modelo vs modelo ya quedó fijada en R1–R3). Vista lejana desde la plaza de la Sagrada Familia, camino de mosaicos teselados triangulares tipo Escher con paleta tierra de la fachada de la Pasión, templo de fondo.

Positivo:

```
Distant wide view across the plaza facing the Passion facade of the Sagrada Familia in Barcelona, rising in the background against a pale sky. Foreground dominated by a tessellated mosaic pathway of interlocking triangular tiles in Escher-like geometric patterns, varied ochre, sandstone, rust, umber and bone-white tones drawn from the facade's earthy palette. Shot on Canon EOS R5, 24mm tilt-shift lens, golden hour raking light, sharp focus throughout, Architecture Photography, Hyperdetailed Photography
```

Negativo: según checkpoint (tabla §6.7 de [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]; Lightning quedó fuera del set.

Sampler/steps/CFG según checkpoint (tabla §6.7 de [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]). Encuadre sugerido 1216×832, prefijo `gx-WF01-plaza`. Estado: pendiente de corrida (R4).
