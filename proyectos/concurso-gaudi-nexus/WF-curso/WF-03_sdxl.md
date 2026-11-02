---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-03, img2img, rhino, render]
idioma: es
---

# WF-03 — Rhino → render (img2img, denoise 0,65)

> JSON: `workflow_WF-03_sdxl.json` · 10 nodos · 1024×1024 · seed 11 · 30 steps · denoise 0,65
> Estado: sin validar contra servidor (R4 pendiente). `LoadImage` trae ruta `PONER-RUTA-rhino_vista.png`.

## 1. Qué tipo de flujo es

**Img2img desde una captura de viewport de Rhino.** Toma la vista del modelo, la reduce a 1024², la codifica a latente y la vuelve a muestrear con `denoise 0,65`. El 65 % de ruido nuevo permite que el modelo invente material y luz, y el 35 % restante conserva la geometría dibujada.

Es el flujo con más peso conceptual del set: convierte el modelo de Rhino en imagen de concurso.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

**El mismo trabajo tiene un segundo camino**, que corre en RunPod: **FLUX.2 klein 9B + `rhino-to-image-lora.basic.safetensors`**. Ese LoRA está entrenado específicamente para viewport de Rhino → imagen, con 121 MB y rank 16. Comparar los dos caminos es la decisión de mayor peso del día 2.

| Pieza Flux | Archivo | Carpeta |
|---|---|---|
| Base | `flux-2-klein-9b-fp8.safetensors` | `models/diffusion_models/` |
| Encoder | `qwen_3_8b_fp8mixed.safetensors` | `models/text_encoders/` |
| VAE | `flux2-vae.safetensors` | `models/vae/` |
| LoRA | `rhino-to-image-lora.basic.safetensors` | `models/loras/` |

Detalle: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 8 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Abre la captura de Rhino desde `input/` |
| 9 | `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | 1024×1024, `bilinear`, recorte centrado |
| 10 | `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Píxeles → latente (reemplaza al `EmptyLatentImage`) |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "photorealistic render of catenary pavilion, branching stone columns, glass roof between arches, park context, golden hour, architectural photography, 8k uhd, masterpiece" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo compartido |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, **denoise 0,65**, seed 11 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF03` |

```
8 → 9 → 10 ─ latent ─→ 5 ─→ 6 ─→ 7
1 → 2/3 ─ conditioning ─→ 5
1 ─ VAE ─→ 10 y 6
```

## 4. El dial: denoise

Es la única perilla que cambia el resultado de fondo.

| Denoise | Qué hace | Cuándo usarlo |
|---|---|---|
| 0,35 | Repinta la superficie y respeta la geometría al pixel | Textura sobre geometría exacta |
| 0,55 | Material creíble, la silueta manda | **WF-07** (geometría → piedra) |
| 0,65 | Material y luz nuevos, composición conservada | **Este WF**: vista general del pabellón |
| 0,80 | Re-imagina: sirve para explorar, la geometría se afloja | Concepto abierto |

Sobre 0,75 el modelo empieza a torcer las catenarias. Bajo 0,45 la imagen se queda en render de viewport con textura.

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Respetar más el Rhino | `denoise` 0,65 → 0,5 | Geometría fiel, material tímido |
| Soltar la geometría | `denoise` 0,65 → 0,75 | Más atmósfera, menos fidelidad |
| Cambiar el encuadre | `ImageScale` a `crop: disabled` o cambiar 1024 por 1216×832 | Conserva el aspecto original del viewport |
| Ver el original | `crop: center` → `disabled` | Comparar lado a lado sin recorte |
| Otra captura | `image` en nodo 8 | Nuevo viewport |
| Estilo de archviz | `LoraLoader` con `ArcvizXL_V01` a 0,6 | Lenguaje de visualización |
| Control de bordes | `ControlNetLoader` + `ControlNetApplyAdvanced` ([Union SDXL](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0)) | Fija la silueta con más dureza que denoise |

Requisito técnico: lado mayor ≤1024 px en la entrada, porque el VAE corre en CPU en la RX 570.

## 6. Qué mirar en el resultado

Las catenarias del Rhino siguen ahí, las columnas ramificadas conservan su lógica, la luz de hora dorada cae coherente, el parque se lee como contexto real. Señal de falla: ventanas o vanos inventados donde el modelo tenía superficie lisa.

## 7. Pendientes

- R4 contra `/object_info`.
- Primer `.png` real del `mcp-plaza.3dm` exportado como viewport, en `input/`.
- Comparación medida contra el camino Flux 9B + LoRA en RunPod.
