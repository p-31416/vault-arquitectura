---
tipo: spec
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-16
tags: [spec, plan, pruebas, modelos, comfyui, realvis, trellis, miercoles, estudio, integrado]
idioma: es
---

> **INTEGRADO** en [[specs/261116-plan-agentes-hermes|plan agentes + Hermes]] §7 (carril miércoles) el 2026-11-16. Este archivo queda como antecedente; no duplicar contenido acá.

# Plan de pruebas rumbo al miércoles (base RealVis + loop 3D)

> De la ADR [[specs/261112-adr-modelo-antes-que-flujo|modelo-antes-que-flujo]]: modelo → hardware → flujo. Decisiones fijadas 2026-11-12: **base SDXL RealVisXL V5.0 BakedVAE** (no Juggernaut, no Lightning), **SD1.5 y sus customs descartados**, sin video este año. Objetivo: croquis → render por partes con consistencia → 3D (Trellis) → Rhino → iterar.

## Base fijada

- Checkpoint: `realvisxlV50_v50Bakedvae.safetensors` (SDXL fp16, 6.46 GB, ya instalado). Juggernaut y Lightning quedan como referencia histórica, no se prueban más.
- ControlNets y customs SD1.5 (Canny/Depth lllyasviel v1.1, etc.): descartados. Solo **ControlNets SDXL** (Union / xinsir canny-depth).
- LoRAs: solo base SDXL/RealVis (Arcviz, Massing, colección adondlin) o entrenado propio después. Nada SD1.5, nada FLUX-dev NC.

## El camino (validado por referentes): croquis → partes → 3D → Rhino

1. **Croquis/esquema** (general a modo esquema cuando el nivel de detalle es alto, ej. Sagrada).
2. **Render por partes** con RealVis: img2img + edición sobre lo generado (inpaint), fijando seed y referencia para **consistencia** entre cámara y cámara en vez de regenerar.
3. **Imagen → 3D con Trellis** → GLB → montaje en Rhino → captura/viewport → vuelta al paso 2.
4. **Consistencia** = editar sobre el archivo (kontext/klein-edit o inpaint), no generar de cero.

### Trellis: qué es

- Microsoft Research,MIT (comercial libre). Imagen → mesh GLB / splat / radiance field en ~30 s.
- v1 (dic-2024, 1.2B): piso 24 GB (3090 mínimo viable).
- **v2 (dic-2025, 4B) + Pixal3D: nativos en ComfyUI core** (sin custom nodes), PBR completo, Pixal3D con fidelidad casi-reconstrucción — ideal para consistencia.
- v2 piso 24 GB → **no entra en las 12–16 GB del estudio: Trellis va en pod** (3090 $0.22/h), no el miércoles.
- GLB importa directo a Rhino: cierra el loop 2D→3D→BIM.

## Batería máxima de pruebas con RealVis (local + API)

| # | Prueba | Dónde | Qué mide |
|---|---|---|---|
| 1 | txt2img × 3 seeds (esquema general) | Local RX 570 | Línea base RealVis baked |
| 2 | Croquis → render img2img (denoise 0.4–0.6) | Local | Respeto de geometría sin ControlNet |
| 3 | Inpaint por partes (vana, lamas, zócalo) | Local | Edición con consistencia, seed fijo |
| 4 | ControlNet SDXL Union canny+depth | Local/pod | Geometría exacta (descargar pesos SDXL) |
| 5 | LoRA Arcviz / Massing sobre RealVis | Local | Estilo + material sin romper geometría |
| 6 | klein edit multi-ref (volumetría + material) | API Cloudflare | Referencia externa; ¿respeta geometría? |
| 7 | Kontext loop conserva+cambia | API Pollinations | Consistencia entre tomas |
| 8 | Imagen → Trellis → GLB → Rhino | **Pod 24 GB** | El loop 3D completo (no el miércoles) |

## Miércoles en el estudio (12–16 GB): qué llevar y qué correr

Llevar listo: workflow JSON RealVis img2img+inpaint, workflow JSON SDXL ControlNet (Union), volumetría PNG + 1–2 fotos ref, prompts/seeds ganadores, modelos en pendrive (RealVis baked, Union SDXL). LoRA del curso: no se usa por ahora.

Correr: pruebas 1–5 en GPU real (minutos en vez de horas), medir tiempo/VRAM, traer renders + workflow validado + notas. Trellis y klein 9B quedan para el pod.

## Referentes que validan el camino

| Referente | Flujo | Coincide con |
|---|---|---|
| denkaTa599 Advanced Flux Arch (16 GB) | Viewport 3D → Canny+Depth dual + 3-LoRA + upscale | Viewport→render con doble control |
| ArchiGen (RTX 3090, sep-2026) | Qwen + ControlNet Union, denoise 0.3–0.55, revisión humana | Control guía, no impone; el ojo decide |
| Laurent Lescop AI/Archi05 | Sketch→render (Kontext, Flux+CN, SD3.5) | Croquis como punto de partida |
| Desktop Architect (jun-2026) | SDXL+LoRA+ControlNet → Hunyuan3D-2/TRELLIS.2 | El loop imagen→3D |
| eCAADe 2025 (paper) | SDXL + LoRA propio + img2img + ControlNet para fachadas | LoRA propio sobre SDXL |

## Trazabilidad

- ADR: [[specs/261112-adr-modelo-antes-que-flujo|modelo-antes-que-flujo]] | flujos: `n_02-img2img` · `n_03-controlnet` · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image]] | mapa: [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] | proveedor: [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]]
