---
tipo: indice
mvp: 09
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_09, croquis-render, flujos, sdxl, local]
idioma: es
---

# MVP 09 — flujos croquis → render (todo local $0)

> Base: RealVisXL v5.0 estándar, 1216x832, seed 42. Salidas: `casa-{S}-v{NN}-{variante}.png`.
> La S0 se genera con LoRA de sketch; S1/S3 la renderizan sin ControlNet; S2 le pone geometría exacta.

## Cómo abrir y ver antes de correr

1. Arrastrar el JSON a `http://127.0.0.1:8188`. Leer nodos y params. Recién entonces encolar.
2. S1/S3 piden el croquis en LoadImage: copiar `salidas/casa-S0cro-v01-*.png` a `P:\00-repos\ComfyUI\input\`.
3. S2 requiere preprocesadores canny (custom node pendiente de instalar — ver abajo).

## Los 4 flujos

### S0 — croquis base (`workflow_S0-croquis.json`)
Descripción: txt2img con LoRA `markerhandsketch-V1` 0.7 sobre RealVis, 32 steps cfg 4 seed 42.
Objetivo: el croquis de la misma casa (volumetría, vanos, patio) en línea suelta. Prompt: [[proyectos/MVP_09-croquis-render/flujos/S0-croquis|S0-croquis]].

### S1 — croquis → render directo (`workflow_S1-croquis-render.json`, denoise 0.55)
Descripción: img2img del croquis con el prompt render del F0, RealVis puro 20 steps cfg 4.
Objetivo: mide respeto de geometría SIN ControlNet (prueba 2 del miércoles). Si inventa de más: bajar a 0.4; si queda dibujo: subir a 0.65.

### S2 — geometría exacta ControlNet (`workflow_S2-controlnet.json`, ⚠️ GATED)
Descripción: croquis → mapa canny → `control_sdxl_canny_fp16` + RealVis.
Objetivo: lock geométrico (prueba 4). ⛔ Requiere instalar `ComfyUI-ControlNet-Aux` (preprocesador Canny, gratis) — pedir `s` antes de instalar. Dual canny+depth (`XL_controlnet-union`) queda para pod (9.4GB).

### S3 — render con LoRA Arq (`workflow_S3-lora.json`, denoise 0.55)
Descripción: igual que S1 + LoRA `ArcvizXL_V01` 0.6.
Objetivo: estilo + material sin romper geometría (prueba 5). Alternativas: `Architectural_Massing` (volumetría), `JJ_Archvizcg_v2`.

## Registro

Cada corrida: `salidas/casa-{S}-v{NN}-{variante}.png` con nomenclatura `casa-{S}-v{NN}-{variante}` (T1, keeper, etc.).
