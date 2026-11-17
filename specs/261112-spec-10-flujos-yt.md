---
tipo: spec
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador
tags: [spec, comfyui, youtube, flujos, arq, casa-moderna, gaudi]
---

# Spec — 10 flujos distintos extraídos de YT (conceptual, sin implementar)

> Fuente: [[wiki/fuentes/00-index-yt|00-index-yt]] (71 videos) + ficha procesada [[wiki/fuentes/comfyui-for_architects-architutors|architutors]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index|WF-Comfy-YT]] + transcripciones curso `raw/yt/transcripts/`. Solo concepto: qué entra, qué sale, qué decide. La campaña de pruebas vive en [[specs/261112-plan-pruebas-casa-moderna-3d|plan casa-moderna-3D]].

## F1 — txt2img base casa moderna

Descripción: el flujo más simple. Sin imagen de entrada: solo prompt + seed generan la casa moderna desde cero. Sirve para fijar estilo, materiales y encuadre antes de cualquier edición.
Objetivo: producir el keeper `casa-base.png` (Juggernaut/RealVisXL, seed 42) que alimenta todos los demás flujos.
Videos: architutors `RAMs89SS6cM` · curso M2 · `WF-curso/WF-01..02`.
Nodos: Checkpoint + CLIP + EmptyLatent + KSampler + VAEDecode.
Local RX 570: sí (Lightning 4-6 pasos para iterar).

## F2 — img2img 3D→render con freno de fidelidad

Descripción: toma una captura 3D o croquis y la vuelve render fotorreal. Un solo parámetro (denoise / Kontext Scale) regula cuánto respeta la geometría base y cuánto inventa.
Objetivo: convertir volumetría Rhino o croquis en render sin perder la geometría (0.4 calco / 0.6 re-estilo / 0.8 reinvención).
Videos: architutors (Kontext Scale) · curso M3 (ReferenceLatent + STRICT CAMERA LOCK) · YT-03-vista.
Nodos: LoadImage + VAEEncode + denoise + KSampler.
Local: sí SDXL.

## F3 — cambio de punto de vista desde un render

Descripción: el mismo render + un texto de cámara nueva devuelven la misma obra desde otro ángulo, sin remodelar nada en 3D.
Objetivo: sacar variantes de cámara para la lámina (±15°, low-angle, aérea, noche) en minutos. Giro real >30° queda para pod/3D.
Videos: YT-03-vista-nueva T1–T4 · Comfy `Keyframe Exploration at Any Camera Angle` · `Concept Art to Any Angle` · `Blender video defines camera`.
Nodos: img2img denoise 0.6-0.7 + prompt cámara; upgrade pod: CameraAngleSelector + LoRA multi-ángulo Qwen (96 poses).
Local: sí ±15°.

## F4 — inpaint con máscara

Descripción: se pinta una zona de la imagen y solo esa zona se regenera con el prompt; el resto queda píxel a píxel.
Objetivo: agregar muebles, borrar autos, abrir una loggia o cambiar un material por zona sin tocar el resto del render.
Videos: za_Lab `Simple SDXL Inpainting` (YT-01) · pixaroma `CropAndStitch` (YT-03) · curso M3 loggia.
Nodos: LoadImage + máscara + SetLatentNoiseMask / VAEEncodeForInpaint + denoise 0.8.
Local: sí (inpainting-fp16 2GB).

## F5 — relight / cambio de sol

Descripción: la misma imagen se re-ilumina a otra hora del día (mañana/tarde/noche) sin regenerar geometría ni materiales.
Objetivo: serie mañana-tarde-noche de la casa y sol tarde oeste Pasión para la plaza, manteniendo encuadre.
Videos/líneas: backlog L1–L4 (IC-Light `fc`/`fbc`, CinelightX/Chiaroscuro) · YT-03 T4 noche.
Nodos: IC-Light (`LoadAndApplyICLightUnet` + `ICLightConditioning`) o 2º sampler bajo denoise + prompt luz.
Local: sí (IC-Light en disco).

## F6 — sketch→render con ControlNet

Descripción: el croquis entra como andamio de líneas y el modelo lo materializa respetando cada trazo exacto.
Objetivo: croquis mejorado (P-03) y lock geométrico de Sagrada (F-03/F-04) donde la línea manda y el prompt solo viste.
Videos: Urban Decoders `Sketch to Render` + `Style transfer with IPAdapter` · curso M3 (canny/depth/scribble) · Comfy `LoRAs, Style Transfer & ControlNets`.
Nodos: croquis → preproceso + ControlNetApply + KSampler.
Local: parcial — canny sí; dual SDXL+Union 9.4GB excede 8GB → pod.

## F7 — upscale final

Descripción: la imagen de prueba chica se amplía a tamaño lámina con microdetalle nuevo, sin cambiar composición.
Objetivo: pasar de 512-1K de iteración a 2K/A1 nítido para `12345.jpg` ≤15MB, con máscara para no tocar Sagrada (F-09).
Videos: Monzon `Flux Upscale` · Ai Underground `Upscale Low VRAM AMD` · curso Topaz/Magnific/Krea.
Nodos: UpscaleModelLoader (RealESRGAN_x4plus en disco) + ImageUpscaleWithModel + 2º denoise 0.2-0.35.
Local: sí por partes; full 4K reservado al cierre.

## F8 — imagen↔3D (ida y vuelta)

Descripción: ida — una imagen genera una malla 3D conceptual; vuelta — viewport Rhino genera render (ver F2). Cierra el loop 2D↔3D.
Objetivo: maqueta volumétrica del concurso y giro real de cámara >30° que F3 no cubre.
Videos: Urban Decoders `Hunyuan 3D` · AIFuzz `2D to stylized 3D` · curso M5 (Tripo/Hunyuan + 9 preparaciones) · `Comfy to Blender`.
Nodos: Tripo/Hunyuan3D (pod, pack pendiente); vuelta: captura viewport + F2.
Local: preparación (maqueta blanca, normal, AO/DA3) sí; malla no.

## F9 — imagen→video / cámara animada

Descripción: una imagen fija cobra movimiento de cámara o timelapse y sale un clip corto para presentación.
Objetivo: clip 15s de la plaza y timelapse de obra para la entrega (WF-04), no para iterar diseño.
Videos: Paul Hansen `IMG2VIDEO` · `Timelapse from frames` · LTX Founders · Comfy `Image-to-Video & Upscaling` · `split-stack one click`.
Nodos: LTX i2v (JSON existe, modelos ausentes) o Seedance/Wan vía pod.
Local RX 570: no (video excede 8GB) → fase pod.

## F10 — automatización n8n/Telegram + viewport vivo

Descripción: la foto o captura llega por Telegram, Comfy genera y la imagen vuelve al chat, sin LLM ni copy-paste en el medio (el caption es el prompt).
Objetivo: loop diario del estudio — captura Rhino/croquis → img2img → dibujo arriba → reenvío — usable por otra persona y pod que se enciende solo al generar.
Videos: DorianAI `n8n to ComfyUI on Runpod` · MindlyNova `Best Method` · Morfeo `ComfyUI+n8n+Vercel` · Ahmad `NOCODE` · Comfy MCP local · YT-04 rhino-vivo + watcher.
Nodos: Telegram Trigger → HTTP/queue ComfyUI → SaveImage → Telegram Send; Rhino `capture_rhino_viewport`.
Local: sí (pollinations free + n8n + ComfyUI LAN).

## Mapa a tu pedido (casa moderna → urbano)

| Necesidad | Flujo | Local $0 |
|---|---|---|
| base casa | F1 | sí |
| cámara/ángulo | F3 (+F8 giro real pod) | ±15° sí |
| iluminación/sol | F5 | sí |
| muebles | F4 | sí |
| material | F2 denoise medio | sí |
| desde 3D | F2 + F10 viewport | captura sí, malla no |
| perspectiva locked | F6 | canny sí, dual no |
| texto/marcas sin agente | F10 caption=prompt | sí |
| final nítido | F7 | por partes sí |
| urbano Gaudí | F1–F8 + matriz WF-01–07 | base sí, Flux/LTX pod |

Gates: G0 F1 keeper casa-base → G1 un keeper por F3/F4/F5 → G2 YT-04 captura→render → G3 P-01+F-01 plaza → lámina A1.
