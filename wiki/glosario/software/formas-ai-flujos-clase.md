---
tipo: software
software: formas-ai-flujos-clase
categoria: analisis
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [glosario, software, formas-ai, deconstruccion, lineart, vectorizado, video, astra, cartesian, creadores]
idioma: es
---

# Formas.ai — deconstrucción de la clase, flujo por flujo + video

> Toma de notas de SOL (demo 2026-11-15) + emulación abierta de cada flujo + video + creadores. Página madre: [[wiki/glosario/software/formas-ai|formas-ai]]. Plan: [[specs/261116-plan-agentes-hermes|plan agentes + Hermes]].

## 1. Extraer Edges — líneas tipo Photoshop

Lo que hace: de una foto saca las líneas (estilo "extraer líneas" de Photoshop) y las pasa a vectorizado o a imagen de referencia del modelo.

Emulación abierta (todo verificado): preprocesadores **Canny / MLSD / lineart / Anyline / TEED** vía `controlnet_aux` + `comfyui_controlnet_aux` (nodo AIO + nodos con umbrales), y vectorizado con **potrace / VTracer → SVG**. MLSD = solo rectas = arquitectura. Criterio: Canny para calco exacto, lineart_realistic para croquis a mano, MLSD para plantas/fachadas.

## 2. Extraer textura desde foto (2 visiones + prompt enhancer)

Lo que hace: le mandan una foto y extrae la textura; por detrás, dos modelos de visión deciden qué ve + un agente mejora el prompt.

Emulación: segmentación (**SAM-3**, $0.005 en fal) o recorte por zona → VLM que describe (Qwen-VL del stack) → prompt enhancer = subagente S3 (trae 3 opciones, elección por texto). Sin caza manual en Google: el agente trae y muestra.

## 3. Formas paramétricas (unir rectángulos) + Rhino

Ventaja real: paramétrico editable. Emulación: editor de esquemas + **modelar en Rhino** (nativo, no imagen). Conexión por MCP (Rhino + Claude/Astra, ver §9 y creadores). Lo que es geometría se modela; lo que es imagen se genera.

## 4. Detail-edit con 2 visiones detrás

Un "GPT" que escribe el detalle con dos modelos de visión por detrás = **agente wrapper con loop VLM** (mira → propone → verifica). Replicable como tool: edit + VLM que controla el resultado contra el pedido. Lección de la clase: el valor está en el loop, no en el modelo.

## 5. Collage: extraer PNG, blend, capas, borrar uniones

Combinar y extraer en PNG, blend con capas, borrado de uniones. Emulación: **Edit Image composite** (n8n, gratis) + **BiRefNet** (recorte, $0 en fal) + SAM-3 para selecciones. Todo en el subagente de entrega (S7).

## 6. Canvas infinito — crítica + Hermes al control

El canvas sin sistema dispersa: nadie sabe qué pensó el otro. Decisión: **un agente controla todo (Hermes)**; los humanos se conectan por **Tailscale**; entradas concurrentes → **cola del runner** con `file_ref + riesgo + idem_key` (contratos ya definidos en ingeniería C4). Dos pedidos a la vez: uno responde, el otro espera turno visible. Ya diseñado en ESTRUCTURA §9 + pi-system-ingenieria.

## 7. Style transfer + notas

Transferencia de estilo con notas = **LoRA de proyecto** (S5) + brief en el vault como memoria. La nota vive en la wiki, el estilo vive en el `.safetensors`. Propiedad del estudio.

## 8. Quadraditos en planta (zoning + prompt) → mini-entrenamiento

Marcan con cuadraditos los espacios a construir, lo cruzan con un prompt, y esas imágenes se usan como contexto de estilo = **mini-entrenamiento con imágenes de referencia**. Nativo abierto equivalente: **segmentación semántica** (preprocesador ADE20K: cada clase un color) + LoRA. Prueba propuesta: aplicarlo a **una lámina** del estudio.

## 9. Vectores hairline "Astra" — esquemático por materiales

Aclaración clave: **Astra = GPT-6 Astra**, el modelo agente de OpenAI para CAD vía MCP (Revit/Rhino/Blender/SketchUp): escribe código o llama tools, inspecciona y corrige. Hechos verificados ([AEC Magazine, Martyn Day](https://aecmag.com/ai/gpt-6-astra-and-the-future-of-bim-modelling/)): lo que el conector expone decide (muros nativos vs sólidos genéricos); primer modelo impactante, **revisiones débiles**; mejor resultado medido = **revisión de planos (13/14 errores)**; costo real ~$10 y 20 min por detalle (BIM Pure); nTop prevé equivalentes open-weights on-premise en ~6 meses. Alternativa barata para el esquemático vectorial por materiales: **VTracer/potrace → SVG hairline** (a probar), no un modelo caro.

## 10. Floor plan: veredicto malo

La propia clase lo muestra flojo: el plano alucina. Decisión del estudio: **no usar IA para el plano final**; en su lugar el pipeline S8 (VLM + ControlNet + canvas fijo + calibración ezdxf/APS + firma humana).

## 11. Cartesian + panorama 3D + upscaler

Cartesian = 3D editable avanzado con **multiview que todavía alucina** (en desarrollo). Upscaler: Topaz / SeedVR2 / Real-ESRGAN local. Panorama con navegación 3D = **efecto sobre imagen** (no reconstrucción): replicable con panorama + foto-3D + Trellis ($0.02 en fal) / Tripo ($0.01). Puerta de entrada 3D barata ya disponible.

## 12. Video — expansión (S9 propuesto, decisión vigente: excluido hasta fin de año)

Análisis listo para cuando se habilite. Vía única: **fal.ai** (una key, cola + webhooks). Precios verificados hoy en [fal.ai/pricing](https://fal.ai/pricing) + [overview video API](https://fal.ai/docs/model-api-reference/video-generation-api/overview):

| Modelo | Uso estudio | Precio (fal) |
|---|---|---|
| Kling 3.0/4.0, O3 (edit + reference) | recorridos fotorrealistas, edición de clip | $0.07–0.14/s (4K $0.42) |
| Seedance 2.0/2.5 (nativo audio, 30 s, multi-shot) | presentación con sonido, multi-toma | tokens (~$0.15–0.47/s 720p) |
| MiniMax H3/Hailuo (first+last frame, refs) | loop palanca entre dos vistas | $0.015–0.06/s |
| Google Veo 3.1 / Gemini Omni Flash | máxima calidad / más barato con audio | $0.40/s / ~$0.10/s 720p |
| Grok Imagine 1.5 Lite / PixVerse V6 | pruebas baratas | $0.01 / $0.005/s |
| Topaz / SeedVR2 upscale | entrega | por MP |

Nota: Sora 2 discontinuado (sep-2026). Integración MVPs: **S9 video** (render→clip de recorrido) en T5+, cuelga de S7 entrega; MVP_04 ya prevé LTX i2v en pod.

## 13. Creadores del rubro (referencia, 12)

1. **ThinkParametric** — stack Midjourney + NanoBanana Pro + FLUX, Rhino→render, privacidad local ([workflow](https://www.youtube.com/watch?v=uJN59t3SvGI)).
2. **ArchViz / cadman.dk** — SD + ControlNet en arquitectura (txt2img/img2img/inpaint) ([video](https://www.youtube.com/watch?v=FJKJPSa0HC4)).
3. **Parametric** — ComfyUI + ControlNet + IPAdapter desde Rhino ([tutorial](https://www.youtube.com/watch?v=IApOVLuPeqU)).
4. **The Architecture Grind** — Rhino + MCP, skills para arquitectura ([Rhino MCP](https://www.youtube.com/watch?hl=en&v=MmeyQVMBIcc)).
5. **Andy Christoforou (ArchViz & AI Academy)** — Claude 3D en SketchUp desde planos ([test](https://www.youtube.com/watch?hl=en&v=MhJRhel2_yA)).
6. **ArchiTech Network** — GPT Astra construyendo proyecto en un día (canal YouTube, nov-2026).
7. **LandSpace Architecture** — workspace Rendair SketchUp→render ([workflow](https://www.youtube.com/watch?v=hsNtcYtgc3g)).
8. **Melos Azemi** — floor plan 2D→render + prompt engineering ([tutorial](https://www.youtube.com/watch?v=WpRGRPsMDhc)).
9. **FORMAS AI (canal oficial)** — workshop sketch→building 2 h, Cartesian, video ([workshop](https://www.youtube.com/watch?v=CesfXvCAdns)).
10. **Chaos Veras** — agentic modeling GPT-6 Astra/Claude en Revit/Rhino/SketchUp + bake a CAD (guía oficial Chaos).
11. **BIM Pure (Nicolas Catellier)** — Astra sketch→detail en Revit vía MCP, costo real por experimento.
12. **AEC Magazine (Martyn Day)** — benchmark y criterio editorial Astra/BIM ([artículo](https://aecmag.com/ai/gpt-6-astra-and-the-future-of-bim-modelling/)).

Vault: denkaTa, ArchiGen, Lescop, Desktop Architect, eCAADE 2025, za_Lab, Morfeo, Dorian Oslov (ficha completa en [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]]).

## 14. Bibliografía oficial por programa

- [BFL FLUX 3 Klein](https://docs.bfl.ai/flux_3/flux3_image_klein) · [ComfyUI ControlNet](https://docs.comfy.org/tutorials/controlnet/controlnet) · [controlnet_aux](https://github.com/huggingface/controlnet_aux) · [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) · [ControlNet repo](https://github.com/lllyasviel/ControlNet)
- [fal video overview](https://fal.ai/docs/model-api-reference/video-generation-api/overview) · [fal pricing](https://fal.ai/pricing) · [fal Kling guide](https://fal.ai/learn/tools/kling-api)
- [OpenRouter Images API](https://openrouter.ai/docs/guides/overview/multimodal/image-generation) · [Seedream 5.0 Pro](https://openrouter.ai/bytedance-seed/seedream-5-0-pro)
- [APS Automation](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/) · [DevCon MCPs](https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services)
- [FORMAS workshop oficial](https://www.youtube.com/watch?v=CesfXvCAdns) · [AEC Astra](https://aecmag.com/ai/gpt-6-astra-and-the-future-of-bim-modelling/)

## Conceptos relacionados

- [[wiki/glosario/software/formas-ai|formas-ai]] · [[specs/261116-plan-agentes-hermes|plan agentes + Hermes]] · [[wiki/glosario/software/modelos-imagen-arquitectura|modelos]] · [[wiki/glosario/software/capacidades-agente-imagenes|capacidades + router]]
