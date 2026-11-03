---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, sdxl, inpainting, juggernaut]
idioma: es
---

# YT-01 — SDXL Inpainting para arquitectura (Diffused.A Studio)

> Video: "ComfyUI For Architecture - Simple SDXL Inpainting Workflow" · canal Diffused.A Studio (z.a.Lab) · 2:56 · https://www.youtube.com/watch?v=px8POauudLY · playlist `PLmQpFKkkTXQFj2NLaW8H1wjwQYGCbdZnc`. Transcripción propia vía subtítulos del video.

## 1. Qué hace el video

Inpainting simple con SDXL para arquitectura: se pinta una máscara sobre la foto, se regenera solo esa zona y el resto queda intacto. Dos demos en el video: **plantar un árbol** en un área vacía y **convertir un paño en muro cortina de vidrio**, con el resultado respetando la morfología del edificio. Los nodos de ControlNet aparecen como **opcionales**.

## 2. JSON

- `workflow_YT-01-sdxl-inpainting.json` (misma carpeta): **reconstrucción local** a partir de la transcripción, no el archivo del autor.
- Archivo del autor (`Inpaint-SDXL-Architecture.json`): tras paywall de Patreon (USD 7,99, https://www.patreon.com/posts/simple-sdxl-135304292). Sin acceso: no copiar ni redistribuir; la reconstrucción es trabajo propio.
- Checkpoint del video: **Juggernaut XL versión Ragnarok** (Civitai 133005, modelVersionId 1759168, `juggernautXL_ragnarok.safetensors`, 6,62 GiB). La reconstrucción usa v9 (instalado local); el swap es solo `ckpt_name` tras descargar Ragnarok.

## 3. Modelo y LoRA

| Pieza | Dato del video | Link / estado |
|---|---|---|
| Checkpoint | **EXACTO (pantalla)**: `juggernautXL_ragnarokBy.safetensors` = Ragnarok oficial (mismo SHA256 `dd08fa32…`, 6,62 GiB; el "By" es renombre de réplica, mismos bytes) | https://civitai.com/models/133005 (versión Ragnarok, modelVersionId 1759168; con tu token descarga directo) |
| Base | SDXL 1.0 | corre en la RX 570 local |
| LoRA | **EXACTO (pantalla)**: `XL_sdxlaang_Aerial-Render.safetensors`, strength_model 0,85 / strength_clip 1,00 — archivo del autor, no publicado en abierto (sale del pack Patreon/Udemy). Ver §3.1 | variantes descargables en §3.2 |
| ControlNet | **EXACTO (pantalla)**: `XL_controlnet-union-sdxl_promax.safetensors` (Union de xinsir) + `DepthAnythingPreprocessor` (comfyui_controlnet_aux), strength 0,15 | https://huggingface.co/xinsir/controlnet-union-sdxl-1.0 |
| Licencia checkpoint | Open RAIL-M + cláusula RunDiffusion | ver §2 de 00-modelos-sdxl-a-probar |

La reconstrucción usa checkpoint v9 (instalado) sin LoRA para que valide y corra tal cual; Ragnarok y LoRA se agregan como paso opcional.

### 3.1 Receta exacta del video (leída en pantalla, frames verificados)

- `VAE Encode (for Inpainting)` con `grow_mask_by 6` (no `SetLatentNoiseMask`: el video usa el nodo de inpainting dedicado a denoise 1,0).
- `KSampler`: `uni_pc_bh2` + `normal`, 30 steps, cfg 3,5, denoise 1,00, seed aleatoria.
- `Image Resize by Longer Side` (comfyui-various): lado mayor a 1024, bicúbico — así entra la foto y la máscara coincide con el latente.
- `Apply ControlNet`: strength **0,15** (solo ata morfología, no manda).
- Positivo demo 1 (visible): "Tree, greenery…"; negativo visible: "watermark, text…".
- Nodos extra a instalar: `comfyui-various` (resize) y `comfyui_controlnet_aux` (DepthAnything); el resto es core.

### 3.2 Variantes descargables (cuando el exacto no está en abierto)

El video menciona un LoRA de archviz y usa renders aéreos; ninguno con nombre público. Candidatos verificados en Civitai (requieren `CIVITAI_API_TOKEN`; hoy sin configurar las descargas dan 401):

| LoRA | Uso | Trigger | Tamaño | Link |
|---|---|---|---|---|
| JJ's Archviz Birdview (XL v2.0) | vistas aéreas / birdview archviz | — (sin trigger publicado) | 435 MB | https://civitai.com/models/194584 |
| Aerial Simulation \| Virtual Aerial Camera (v2.0) | cámara aérea virtual | `aerial photography` | 169 MB | https://civitai.com/models/123756 |
| JJ's Archiviz architectural perspective (XL v2.0) | perspectiva arquitectónica | `Archiviz` | 870 MB | https://civitai.com/models/191596 |
| Arcviz_Interior&Exterior (ArchvizXL_V01) | interior + exterior (el citado en WF-02) | `archviz 1` | 870 MB | https://civitai.com/models/549260 |
| JZCGXL026-Aerial view (v1.0) | vista aérea | `jzcgxl001, aerial view` | 435 MB | https://civitai.com/models/363965 |
| ArchViz Workflow (v1.0) | liviano para probar la cadena | `archviz` | 36 MB | https://civitai.com/models/2280607 |

Uso: `LoraLoader` entre checkpoint y sampler, strength 0,6–0,8, y el trigger en el positivo. Probar primero el liviano (36 MB) para validar la cadena y después el pesado.

## 4. Nodos y docs oficiales

| # | Nodo | Doc | Función en este flujo |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga Juggernaut; salidas MODEL/CLIP/VAE |
| 2 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Foto base; su salida MASK (MaskEditor) alimenta al nodo 5 |
| 3 | `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | Reescala a 1024×1024 (lanczos): el video escala a 1024 para ir más rápido |
| 4 | `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Foto → latente con el VAE del checkpoint |
| 5 | `SetLatentNoiseMask` | [doc](https://docs.comfy.org/built-in-nodes/SetLatentNoiseMask) | Aplica la máscara al latente: solo esa zona se regenera |
| 6 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: qué aparece dentro de la máscara |
| 7 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo de la casa |
| 8 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` + `karras`, 30 steps, cfg 4, denoise 0,75, seed 7 |
| 9 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 10 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-YT01-inpaint` |

Extensiones del video (opcionales, no incluidas en el JSON): `LoraLoader` ([doc](https://docs.comfy.org/built-in-nodes/LoraLoader)) con el LoRA de archviz entre nodo 1 y 8; `ControlNetLoader` + `ControlNetApplyAdvanced` ([doc](https://docs.comfy.org/built-in-nodes/ControlNetLoader) · [doc](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)) con su conditioning positivo/negativo como entradas para atar el relleno a la morfología del edificio.

```
2 ─ IMAGE ─→ 3 ─→ 4 ─ latent ─→ 5 ─→ 8 ─→ 9 ─→ 10
2 ─ MASK ───────────────→ 5
1 ─ MODEL ─→ 8 · 1 ─ CLIP ─→ 6 ─→ 8 (+) · 1 ─ CLIP ─→ 7 ─→ 8 (−) · 1 ─ VAE ─→ 4/9
```

## 5. Cómo se usa (3 pasos)

1. Subir la foto al `input/` (idealmente ya a 1024; si es cuadrada, el `ImageScale` es no-op y la máscara coincide con el latente).
2. En el LoadImage → *Open in MaskEditor* → pintar la zona a regenerar.
3. Encolar. Salida: `gx-YT01-inpaint`.

## 6. Cuadro de pruebas

Una variable por corrida; el resto del grafo intacto.

| # | Prueba | Máscara | Prompt + (extracto) | Denoise | Qué mirar |
|---|---|---|---|---|---|
| T1 | Agregar un árbol | zona vacía junto al edificio | "leafy deciduous tree, full crown, natural trunk, planted soil bed, same daylight" | 0,75 | copa completa, tronco anclado, sombra coherente |
| T2 | Muro cortina de vidrio | paño de fachada | "glass curtain wall, floor-to-ceiling glazing, slim dark mullions, sky reflection" | 0,7 | respeta el ritmo del edificio, reflejo creíble |
| T3 | Borrar un árbol | copa + tronco | describir el fondo (césped, vereda, fachada vecina) | 0,6 | sin fantasma, textura continua |
| T4 | Agregar una ventana | paño ciego | "punched window, dark aluminum frame, glass with interior hint, aligned sill height" | 0,7 | antepecho alineado, marco a plomo |
| T5 | Cambiar material | paño | "travertine stone cladding" vs "board-formed concrete" | 0,7 | junta y escala del material |

Escalera de denoise si el relleno no cierra: 0,5 (conservador) → 0,65 → 0,8 (libre). Variante de modelo: repetir T1–T2 con RealVisXL v5.0 (`dpmpp_sde` + `karras`, 30 steps, negativo del autor, §6.3 de [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]).

## 7. Pendientes

- ✅ Descargado 2026-11-02: Ragnarok (SHA256 `dd08fa32…` verificado, mismos bytes que el video) + Union promax (`XL_controlnet-union-sdxl_promax.safetensors`, el del video) + LoRA liviano (`ArteFactoryLab_LORA-10.safetensors`, 36 MB, trigger `archviz`).
- El LoRA exacto (`XL_sdxlaang_Aerial-Render`) solo sale del pack del autor (Patreon/Udemy); mientras tanto las variantes de §3.2 cubren el rol.
- Probar la rama ControlNet opcional cuando el relleno ignore la morfología.
- Registrar corridas en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|la matriz]] con modelo, segundos y veredicto.

## Referencias

- Video: https://www.youtube.com/watch?v=px8POauudLY
- Patreon del autor (archivo original, pago): https://www.patreon.com/posts/simple-sdxl-135304292
- Juggernaut XL versión Ragnarok (video): https://civitai.com/models/133005 (versión Ragnarok, modelVersionId 1759168, `juggernautXL_ragnarok.safetensors`)
- LoRAs candidatos: https://civitai.com/models/194584 (birdview) · https://civitai.com/models/123756 (aerial) · https://civitai.com/models/191596 (perspectiva) · https://civitai.com/models/549260 (archviz int+ext) · https://civitai.com/models/2280607 (liviano)
- Curso gratuito del canal: https://www.udemy.com/course/introducing-stablediffusion-comfyui-for-architectsdesigners/
- Inpainting oficial ComfyUI: https://docs.comfy.org/tutorials/basic/inpaint
