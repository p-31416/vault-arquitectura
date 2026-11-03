---
tipo: guia
proyecto: MVP_04-comfyui-arquitectura
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [mvp_04, comfyui, marca-de-agua, nodos, n_08]
idioma: es
---

# 03-nodos-WFmarca_agua — configs propias

> Solo lo no genérico. Docs oficiales: [ImageCompositeMasked](https://docs.comfy.org/built-in-nodes/ImageCompositeMasked) · [ImageBlend](https://docs.comfy.org/built-in-nodes/ImageBlend).

| # | Nodo | Rol y valores |
|---|------|---------------|
| 1 | `LoadImage` | foto base, `image: PONER-foto.jpg` (se usa solo IMAGE; su MASK se ignora) |
| 2 | `LoadImage` | marca PNG con alfa, `image: PONER-marca.png` (IMAGE + MASK del alfa) |
| 3 | `ImageScaleBy` | marca a `scale_by` 0.25, `bilinear` (conserva aspecto) |
| 4-7 | `MaskToImage` → `ImageScaleBy` → `ImageInvert` → `ImageToMask` | máscara del alfa al mismo factor + **invertida** (canal `red`); `LoadImage` entrega `1-alfa` (`nodes.py:1771`), sin invertir se pegan los píxeles transparentes = fondo negro |
| 8 | `ImageCompositeMasked` | pega marca sobre foto en `x` 40 / `y` 40, `resize_source: false`, `mask` de 7 |
| 9 | `ImageBlend` | `image1` composite + `image2` foto, `normal`, `blend_factor` 0.3 (0 = marca plena, 1 = invisible) |
| 10 | `SaveImage` | prefijo `n_08-marca-agua` |

Sin sampler ni checkpoint: R1 (escala 512) no aplica; el composite corre a resolución original.
