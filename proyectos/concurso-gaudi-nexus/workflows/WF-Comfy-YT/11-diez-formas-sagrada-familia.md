---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: 10 formas de insertar Sagrada Familia sin que el modelo invente
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: borrador-activo
tags: [concurso, gaudi-nexus, sagrada-familia, controlnet, ipadapter, fondo]
idioma: es
---

# 10 formas de insertar Sagrada Familia sin que el modelo invente

> Objetivo Sol: Sagrada bien de fondo, sin que el modelo la redibuje. Ordenadas de más fiel (1–3) a más libre (9–10). Cada una: visión / estructura / requisitos / cuándo usar. Prompts base en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/10-prompts-prueba-nexus|10-prompts-prueba-nexus]]. Resultados en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]].

## F-01 fondo foto real + inpaint solo plaza (la más fiel)

- **Visión:** foto CC BY-SA plaza con Sagrada intacta, solo se pinta suelo/puestos.
- **Estructura:** LoadImage foto → máscara excluye Sagrada (todo menos silueta) → inpainting `sd-v1-5-inpainting-fp16` denoise 0.8.
- **Requisitos:** local RX 570, 512 R1.
- **Usar cuando:** entrega final fondo creíble, cero invento.

## F-02 Rhino massing + foto fondo por máscara (composit)

- **Visión:** render propuesta recortado por máscara, pegado sobre foto real Sagrada.
- **Estructura:** render WF-03 con fondo transparente / máscara → ImageComposite sobre foto → color match leve.
- **Requisitos:** local, sin IA generativa en fondo.
- **Usar cuando:** control total perspectiva.

## F-03 ControlNet depth fijado desde foto (lock geométrico)

- **Visión:** misma profundidad foto, solo cambia material primer plano.
- **Estructura:** Depth Anything 3 → ControlNet depth weight 0.85–1.0 + KSampler denoise 0.35–0.45.
- **Requisitos:** local SDXL + `models/controlnet/` + depth.
- **Usar cuando:** P-01/P-07, probar 0.4 calco / 0.6 re-estilo / 0.8 reinvención.

## F-04 ControlNet canny bordes Sagrada

- **Visión:** bordes torres como andamio, IA rellena sin mover silueta.
- **Estructura:** Canny low 100 high 200 → ControlNet canny 0.7 + depth 0.5 dual.
- **Requisitos:** local SDXL.
- **Usar cuando:** croquis a fotorrealista con Sagrada al fondo.

## F-05 IPAdapter referencia Sagrada (guía visual)

- **Visión:** 1–2 fotos Sagrada como referencia estilo/luz, sin copiar píxeles.
- **Estructura:** LoadImage ref → CLIP Vision → IPAdapter weight 0.4–0.6 + prompt `keep silhouette intact`.
- **Requisitos:** local `models/ipadapter/` + `clip_vision/` (ya en disco).
- **Usar cuando:** atardecer Pasión cálido coherente.

## F-06 LoRA Gaudí solo material, geometría propia

- **Visión:** lógica constructiva Gaudí en puestos/piso, Sagrada intacta.
- **Estructura:** LoRA curso 0.5 vs 1.0 (gx-G-01/02 matriz) sobre WF-03.
- **Requisitos:** `models/loras/rhino-to-image-lora.basic.safetensors` + pod FLUX o local SDXL según base.
- **Usar cuando:** dial intensidad WF-07, sin que LoRA toque fondo (máscara fondo si hace falta).

## F-07 foto placa + ControlNet scribble puente/piso dibujado

- **Visión:** captura Google con trazo puente/piso a mano, IA lo vuelve fino y construido.
- **Estructura:** scribble del trazo → ControlNet scribble 0.6 + prompt piso fino patrón.
- **Requisitos:** local Lightning para iterar.
- **Usar cuando:** P-10 lengua-puente.

## F-08 doble KSampler: fondo bajo denoise + primer plano alto

- **Visión:** fondo casi copia (denoise 0.25), plaza/puestos más libres (0.65), fundido por máscara.
- **Estructura:** 2 ramas KSampler misma seed → ImageBlend por máscara Sagrada.
- **Requisitos:** local SDXL, cuesta 2× tiempo pero salva fondo.
- **Usar cuando:** fondo se derrite con denoise único.

## F-09 upscale con máscara (no tocar Sagrada)

- **Visión:** upscale RealESRGAN solo plaza, Sagrada por Lanczos simple.
- **Estructura:** máscara Sagrada invertida → upscale model + 2º denoise 0.15–0.35 solo fuera máscara.
- **Requisitos:** `models/upscale_models/RealESRGAN_x4plus.pth` local.
- **Usar cuando:** final A1 15 MB sin artefactos torres.

## F-10 Flux Redux / Qwen-Image-Edit guiado (cuando haya pod)

- **Visión:** edición por instrucción "mantén Sagrada idéntica, cambia solo suelo a triangular".
- **Estructura:** pod FLUX.2 + Redux referencia o Qwen-Image-Edit.
- **Requisitos:** pod 24 GB, stack 18.3 GB.
- **Usar cuando:** SDXL no logra fidelidad y hay presupuesto pod $0.89/h.

Tabla decisión rápida: ¿fondo perfecto? F-01/F-02. ¿Diseño integrado? F-03/F-04 + F-08. ¿Luz/material? F-05/F-06. ¿Puente dibujado? F-07. ¿Final nítido? F-09. ¿Nada rinde? F-10 pod.

---
*Más nuevo → más arriba. Log: 2026-11-02 creación 10 formas desde pedido Sol "insertar Sagrada sin que invente".*
