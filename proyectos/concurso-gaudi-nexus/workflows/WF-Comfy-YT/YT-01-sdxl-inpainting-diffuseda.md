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

## 3. Modelo y LoRA

| Pieza | Dato del video | Link / estado |
|---|---|---|
| Checkpoint | Juggernaut XL | https://civitai.com/models/133005/juggernaut-xl · espejo HF https://huggingface.co/RunDiffusion/Juggernaut-XL-v9 |
| Base | SDXL 1.0 | corre en la RX 570 local |
| LoRA | "custom LoRA for archviz", sin nombre ni link en el video | sin identificar; candidatos del estudio en [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] |
| Licencia checkpoint | Open RAIL-M + cláusula RunDiffusion | ver §2 de 00-modelos-sdxl-a-probar |

La reconstrucción usa solo el checkpoint (sin LoRA) para que valide y corra tal cual; el LoRA se agrega como paso opcional.

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

Escalera de denoise si el relleno no cierra: 0,5 (conservador) → 0,65 → 0,8 (libre). Variante de modelo: repetir T1–T2 con RealVisXL v5.0 (`dpmpp_sde` + `karras`, 30 steps, negativo del autor, §6.3 de [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]).

## 7. Pendientes

- Identificar el LoRA de archviz del video (no publicado) o fijar uno del estudio.
- Probar la rama ControlNet opcional cuando el relleno ignore la morfología.
- Registrar corridas en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|la matriz]] con modelo, segundos y veredicto.

## Referencias

- Video: https://www.youtube.com/watch?v=px8POauudLY
- Patreon del autor (archivo original, pago): https://www.patreon.com/posts/simple-sdxl-135304292
- Juggernaut XL: https://civitai.com/models/133005/juggernaut-xl
- Curso gratuito del canal: https://www.udemy.com/course/introducing-stablediffusion-comfyui-for-architectsdesigners/
- Inpainting oficial ComfyUI: https://docs.comfy.org/tutorials/basic/inpaint
