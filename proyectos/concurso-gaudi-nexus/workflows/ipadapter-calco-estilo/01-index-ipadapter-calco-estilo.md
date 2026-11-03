---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: IPAdapter calco→estilo — croquis línea + editado Photoshop
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: listo-para-probar
tags: [concurso, gaudi-nexus, comfyui, ipadapter, sdxl, calco, estilo]
idioma: es
---

# IPAdapter calco→estilo — del calco al editado sin LoRA (todavía)

> Pedido Sol 2026-11-02: probar IPAdapter para copiar el estilo de sus editados Photoshop sobre sus calcos de líneas, como paso previo al LoRA. Grafo: `workflow_ipadapter_calco_estilo.json` (API format, R4 validado contra `/object_info` 2026-11-02: clases, enums, adaptador y canny SDXL OK en dropdowns). **v2 vigente: todo 512 (política Sol), calidad máxima, rama ControlNet, prompt edificio real. NO correr sin su `s` — la gx-A se canceló por lenta.**

## Visión

Tu dibujo de calco sale con el acabado de tu Photoshop: parasoles sunscreen metálico perforado al frente + bloque hormigón casetonado y vidrio con cubierta verde detrás. El ControlNet canny clava tu línea (gx-A se deformó); el `strong style transfer` 0.85 pasa color y material de verdad (gx-A casi no pasó color).

## Estructura v2 (512 max)

Calco → `ImageScale` 512² → doble uso: `VAEEncode` (img2img denoise 0.45) + `ControlNetApply` canny strength 1.0 sobre el positive (el calco entra directo como mapa de bordes, sin preprocesador) + editado 512² → `IPAdapterAdvanced` `strong style transfer` 0.85 → `KSampler` 50 pasos CFG 3.0 seed 42 → salida `gx-B-01`.

## Visión

Tu dibujo de calco sale con el acabado de tu Photoshop: misma geometría, otro material/luz. Perilla principal: `weight` 0.5–0.8 (más = más Photoshop, menos = más calco).

## Estructura

Calco → `ImageScale` 1216×832 → `VAEEncode` (img2img denoise 0.55, geometría clavada) + editado → `ImageScale` 768² → `IPAdapterAdvanced` con `weight_type: style transfer` (copia estilo, no contenido) → `KSampler` 30 pasos CFG 4 → salida `gx-A-01`.

Sin ControlNet a propósito: solo hay SD1.5 en disco y la base es SDXL; la geometría la fija el img2img.

## Requisitos (descarga hecha 2026-11-02, 847.517.512 bytes = byte exacto del remoto)

1. ✅ `ip-adapter-plus_sdxl_vit-h.safetensors` en `P:\00-repos\ComfyUI\models\ipadapter\` — visible en dropdown del servidor (verificado vía `/object_info`). Origen verificado 200: `https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors` (la API de CivitAI no hizo falta: el archivo vive en HuggingFace público).
2. En disco ya: Juggernaut v9, `CLIP-ViT-H-14` (el que pide este adaptador), RX 570 con flags `--lowvram`.
3. Poner tus imágenes en `P:\00-repos\ComfyUI\input\` con estos nombres (o editar nodos 4 y 7): `calco-lineas.png` + `estilo-photoshop.png`.
4. Canny SDXL ✅ `control_sdxl_canny_fp16.safetensors` (2.502.139.136 bytes = byte exacto, en dropdown verificado 2026-11-02). Origen: `https://huggingface.co/diffusers/controlnet-canny-sdxl-1.0` (fp16).
5. Arrastrar el JSON al canvas y encolar **solo con `s` de Sol**. Salidas en `salidas/` (fuera de git). Política: siempre 512 max.

## Qué probamos (una variable por corrida, veredicto Sol en reporte)

| Test | Variable | Qué miro |
|---|---|---|
| gx-A-01..03 | weight {0.5, 0.7, 0.9} | punto donde el estilo aparece sin comerse la línea |
| gx-B-01 | denoise {0.4} vs 0.55 | calco fino se respeta con menos denoise |
| gx-C-01 | RealVisXL v5.0 en nodo 1 | ¿mejor material que Juggernaut para tu estilo? |

Anotar en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]]: probamos / sucedió / keeper-descartar / solución.

## Doble valor

Cada par calco+editado que keeperes es mañana una muestra del dataset `gaudinexusstyle` (ver [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §2 + [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-02-lora-sdxl-pocas-imagenes|YT-02]]).

---
*Más nuevo → más arriba. Log: 2026-11-02 v2 512 max + rama CN + prompt edificio real + strong style 0.85, canny descargado byte-exacto, R4 OK, gx-A cancelada por lenta (no correr sin s). 2026-11-02 descarga adaptador SDXL + dropdown OK. 2026-11-02 creación JSON + ficha, gx-A-01 salió deforme y pálida.*
