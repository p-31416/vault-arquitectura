---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [mvp_04, n_06, nodos, fachada, hamad]
---

# 03-nodos — WF_v5_fachada_hormigon_madera

## Corrección vs WF_v2_batch

| Aspecto | WF_v2 (falló 30/09) | WF_v5 (corrige) | Por qué |
|---|---|---|---|
| Prompt+ | `tuscan country kitchen / tuscan stone facade, cypress` | `exposed concrete texture, dark oiled wood slats, elevated volume on pilotis, steel bridge` (x3 variantes) | Tuscan sobreescribía Hamad |
| Prompt- | genérico blurry/watermark | agrega `tuscan, stone villa, cypress, travertine` bloqueado | evita deriva villa |
| ImageBatch | `ImageBatch(20+21)` mezcla 2 refs | eliminado: 1 ref = 1 rama (`20→30→60→70→80` etc.) | batch hibridaba |
| ImageScale | `512x512 crop:center` (3 iguales) | `01 768x512, 02 512x768, 03 768x512` lanczos center | respeta orientación, no recorta puente/voladizo |
| Canny | `0.12/0.39` (M2) | `0.31/0.59` (los 3) | umbral WF_v1 validado, ancla líneas hormigón/madera |
| ControlNet | `0.80 / 0.0-0.80` | `0.90 / 0.0-0.85` | más adherencia a aristas |
| Denoise | `0.60 / 0.75` | `0.40` (x3, seeds 42/77/123) | 0.6 inventaba villa; 0.4 preserva volumen Hamad |
| Sampler | `euler_ancestral/karras 30 cfg 7` | idem | estable en RX 570 |

## Grafo (27 nodos, 3 ramas paralelas)

```
Checkpoint architecturerealmix_v11
├─01hamad → ImageScale 768x512 → Canny 0.31/0.59 → CN 0.90 ─┐
├─02hamad → ImageScale 512x768 → Canny 0.31/0.59 → CN 0.90 ─┤
└─03hamad → ImageScale 768x512 → Canny 0.31/0.59 → CN 0.90 ─┤
           ├─ VAEEncode (por rama) → KSampler denoise 0.40 → VAEDecode → SaveImage n_06-C-01/02/03
```

Docs: `CheckpointLoaderSimple`, `ImageScale`, `Canny`, `ControlNetLoader/ApplyAdvanced`, `CLIPTextEncode`, `VAEEncode`, `KSampler`, `VAEDecode`, `SaveImage` en `https://docs.comfy.org/built-in-nodes/<PascalCase>`.
