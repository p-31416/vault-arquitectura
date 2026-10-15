---
tipo: spec
mvp: 04.02
wf: WF-03-serie-controles
fecha_creacion: 2026-10-09
ultima_actualizacion: 2026-10-09
tags: [mvp_04.02, comfyui, spec, img2img, controlnet, canny, scribble, depth, lora]
estado: activo
---

# SPEC — WF-03 serie de controles (5 flujos, 1 imagen)

> Cómo va a ser cada flujo, qué nodos tiene y de qué fuente oficial sale cada decisión. Todas las referencias fueron verificadas con 200 antes de citarse (regla del vault).

- [[#1. Objetivo]]
- [[#2. Imagen base]]
- [[#3. Base común de los 5 flujos]]
- [[#4. F-A — img2img sin ControlNet]]
- [[#5. F-B — ControlNet general (Scribble)]]
- [[#6. F-C — ControlNet Canny]]
- [[#7. F-D — ControlNet Depth (bloqueado)]]
- [[#8. F-E — LoRA de estilo]]
- [[#9. Orden de ejecución]]
- [[#10. Referencias oficiales verificadas]]

## 1. Objetivo

Comparar 5 niveles de control sobre la MISMA imagen, del más libre al más dirigido, para decidir qué flujo usar en cada caso del estudio. Seed fijo (42) en todos para que la única variable sea el control.

## 2. Imagen base

- Archivo: `inputs/base-01.png` (copia en `P:\00-repos\ComfyUI\input\base-01.png` para los nodos LoadImage)
- Origen: txt2img con `workflow_base_txt2img_v1.json` (ArchitectureRealmix, 768×512, seed 42, prompt_id `da812717`, 101 s)
- Contenido: casa moderna minimalist (hormigón + madera + vidrio, volúmenes geométricos, techo plano y a dos aguas)

## 3. Base común de los 5 flujos

| Parámetro | Valor | Por qué |
|---|---|---|
| Checkpoint | `architecturerealmix_v11.safetensors` (SD1.5) | El que anda en RX 570 8GB, ecosistema ControlNet SD1.5 completo |
| Resolución | 768×512 (aspecto de la base, sin aplastar) | Lección WF-01: aplastar a cuadrado deforma formas |
| Sampler | euler + normal, steps 30, cfg 7, seed 42 | Baseline del vault, comparable con WF-01/WF-02 |
| Licencia checkpoint | OpenRAIL-M | Comercial OK con atribución |

## 4. F-A — img2img sin ControlNet

**Qué hace:** re-estiliza la imagen con solo prompt. El mando es `denoise` 0.6: 0 = idéntica, 1 = ignora la base.

**Nodos:** LoadImage (`base-01.png`) → ImageScale (768×512, lanczos) → VAEEncode → KSampler (denoise 0.6) → VAEDecode → SaveImage (`n_03-F-01.png`).

**Fuente:** tutorial oficial img2img — *"The key lies in the `denoise` parameter: the smaller the value, the smaller the difference vs the reference"* (https://docs.comfy.org/tutorials/basic/image-to-image.md, verificado 200 el 2026-10-09).

## 5. F-B — ControlNet general (Scribble)

**Qué hace:** guía con trazo suelto. Es el ejemplo canónico de la doc oficial (su tutorial usa Scribble).

**Nodos:** base F-A + ControlNetLoader (`control_v11p_sd15_scribble.safetensors`, 1.378 MB, instalado) + ControlNetApplyAdvanced (strength 0.7, 0.0-0.75). Sin preprocesador (el trazo va directo, validado en `n_03-WF01` v1.1a).

**Fuente:** tutorial oficial ControlNet — ejemplo scribble + *"strength: higher values increase ControlNet's influence"* + tabla start/end_percent (https://docs.comfy.org/tutorials/controlnet/controlnet.md, verificado 200 el 2026-10-09).

## 6. F-C — ControlNet Canny

**Qué hace:** bordes exactos. Mismos parámetros validados en WF-01 F-03.

**Nodos:** base F-A + Canny (0.25/0.55) + ControlNetLoader (`control_v11p_sd15_canny.safetensors`, instalado) + ControlNetApplyAdvanced (strength 0.9, 0.0-1.0).

**Fuente:** mismo tutorial ControlNet + *"The workflows for other V1.1 models are similar, only select the appropriate model"* (misma página verificada).

## 7. F-D — ControlNet Depth (bloqueado)

**Qué hace:** volumen y sombras desde mapa de profundidad.

**Nodos (cuando se desbloquee):** base F-A + estimador de profundidad (dpt_hybrid) + ControlNetLoader (`control_v11f1p_sd15_depth_fp16.safetensors`, 689 MB, instalado) + ControlNetApplyAdvanced (strength 0.75, 0.0-0.85).

**Bloqueo real:** no hay nodo estimador de profundidad instalado (sin `comfyui_controlnet_aux`) y ComfyUI-Manager no responde → install manual git+pip+reinicio. La propia doc oficial lo anticipa: *"Comfy Core nodes do not include all preprocessors… you may need custom nodes"* + enlaza `comfyui_controlnet_aux` (https://github.com/Fannovel16/comfyui_controlnet_aux, referenciado por la doc verificada). **Decisión SOL: instalar junto a Fase B, un solo reinicio, F-D corre último.**

## 8. F-E — LoRA de estilo

**Qué hace:** LoraLoader sobre la base F-C para enfatizar estilo sin cambiar geometría.

**Nodos:** base F-C + LoraLoader (strength_model 0.6-0.8, strength_clip 0.6-0.8, en serie tras el checkpoint).

**LoRAs elegidos (A+B, decisión SOL):**

| # | LoRA | Peso | Trigger | Licencia | Rol |
|---|---|---|---|---|---|
| A | [Architectural Sketch](https://civitai.com/models/791004/architectural-sketch) (verificado 200 el 2026-10-08) | 18 MB | `smref sketch` (+`watercolor effect`/`monochrome`) | Open RAIL-M | Estilo arq (acuarela/mono/iso) |
| B | [Detail Enhancement SD1.5](https://civitai.com/models/1911622/sd15detail-enhancement-sd15) (verificado 200 el 2026-10-08) | 36 MB | — | Open RAIL-M | Más detalle sin cambiar estilo |

**Fuente:** tutorial oficial LoRA — tabla `strength_model`/`strength_clip` + nodos encadenables en serie (https://docs.comfy.org/tutorials/basic/lora.md, verificado 200 el 2026-10-09).

**Nota de higiene del vault:** el `modelos-recomendados.md` cita "CivitAI 119936" como LoRA de arquitectura SD1.5 — verificado el 2026-10-08: ese ID es un LyCORIS de otra temática. Queda pendiente corregir esa referencia.

## 9. Orden de ejecución

1. ✅ Base txt2img generada (`n/a`, 101 s)
2. ⏳ F-A → `salidas/n_03-F-01.png`
3. ⏳ F-B → `salidas/n_03-F-02.png`
4. ⏳ F-C → `salidas/n_03-F-03.png`
5. ⏳ Descarga A+B (~54 MB) + verificación safetensors
6. ⏳ F-E (×2, un LoRA por corrida) → `salidas/n_03-F-04/05.png`
7. ⏳ Install aux pack + reinicio → F-D → `salidas/n_03-F-06.png`
8. ⏳ Registro §5+§6 en `WF-03-serie-controles.md` (archivo único, a crear tras tu lectura)

**VRAM:** cada flujo usa 1 checkpoint SD1.5 + máximo 1 ControlNet + opcional 1 LoRA (<200 MB) — entra en RX 570 8GB. Regla vigente: de a una corrida por vez + `clear_vram` si se tilda.

## 10. Referencias oficiales verificadas

- img2img: https://docs.comfy.org/tutorials/basic/image-to-image.md (200, 2026-10-09)
- ControlNet (+Scribble, strength, start/end, chain, aux-pack): https://docs.comfy.org/tutorials/controlnet/controlnet.md (200, 2026-10-09)
- LoRA (strength_model/clip, serie): https://docs.comfy.org/tutorials/basic/lora.md (200, 2026-10-09)
- Inpainting + MaskEditor: https://docs.comfy.org/tutorials/basic/inpaint.md (200, 2026-10-08)
- Índices: https://docs.comfy.org/llms.txt y https://docs.comfy.org/_llms/en/get-started.md (200, 2026-10-09)
- Aux pack (vía doc oficial): https://github.com/Fannovel16/comfyui_controlnet_aux
- LoRA A: https://civitai.com/models/791004/architectural-sketch (200, 2026-10-08)
- LoRA B: https://civitai.com/models/1911622/sd15detail-enhancement-sd15 (200, 2026-10-08)
