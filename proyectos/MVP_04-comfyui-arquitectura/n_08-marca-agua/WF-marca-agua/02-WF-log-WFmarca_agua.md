---
tipo: log
proyecto: MVP_04-comfyui-arquitectura
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [mvp_04, comfyui, marca-de-agua, log, n_08]
idioma: es
---

# 02-WF-log-WFmarca_agua

> Primera corrida hecha por Sol con v1.0: bug + fix documentados abajo.

## R4 — validación estática

Clases verificadas en el código del servidor (`nodes.py` + `comfy_extras/nodes_mask.py`): `LoadImage` (máscara = `1-alfa`, línea 1771) · `ImageScaleBy` · `MaskToImage` · `ImageInvert` · `ImageToMask` · `ImageCompositeMasked` · `ImageBlend` · `SaveImage`. Archivos de entrada existen en `input/`: `ISOLOGO_PITAU (2).png` (RGBA 693×378) + `w01-realvisxl-512.png` (RGB 512²).

## Corridas

| # | Fecha | Foto | Marca | scale | x,y | blend | Resultado |
|---|-------|------|-------|-------|-----|-------|-----------|
| A-01 (v1.0) | 2026-11-02 | w01-realvisxl-512.png | ISOLOGO_PITAU (2).png | 0.25 | 40,40 | 0.3 | **bug**: marca con rectángulo negro → `salidas/n_08-A-01.png`. Causa: máscara sin invertir pegó los píxeles transparentes |
| A-02 (v1.1) | — | misma | misma | 0.25 | 40,40 | 0.3 | pendiente re-corrida con `ImageInvert` |
