---
tipo: guia
proyecto: MVP_04-comfyui-arquitectura
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [mvp_04, comfyui, marca-de-agua, overlay, transparencia, n_08]
idioma: es
---

# WF-marca-agua — overlay de marca con transparencia

> Superpone un PNG con alfa sobre una foto: escala la marca, invierte su máscara (Comfy entrega `1-alfa`), la pega en (x, y) y regula opacidad. Solo nodos nativos, sin sampler ni checkpoint. JSON: `workflow_marca_agua.json` (10 nodos, API format). Estado: v1.1 con R4 de clases verificada en `nodes.py` del servidor.

## Uso (3 pasos)

1. Copiar la foto a `ComfyUI/input/` y la marca (PNG con transparencia) a `ComfyUI/input/`.
2. Reemplazar `PONER-foto.jpg` (nodo 1) y `PONER-marca.png` (nodo 2).
3. Encolar. Salida: `n_08-marca-agua_00001_.png`.

## Variables

| Qué | Dónde | Default |
|-----|-------|---------|
| Tamaño de marca | nodo 3 y 5, `scale_by` (los dos iguales) | 0.25 |
| Posición | nodo 8, `x` / `y` (esquina superior izquierda de la marca) | 40 / 40 |
| Opacidad | nodo 9, `blend_factor` (0 = marca plena, 1 = invisible) | 0.3 |

## Cadena

```
foto ─┬────────────────────────────────→ composite → blend → save
      │                                      ↑          ↑
marca → scale ─→ composite                marca+mask   foto
      └ mask → a imagen → scale → INVIERTE → a mask ─┘
```

Detalle: [[proyectos/MVP_04-comfyui-arquitectura/n_08-marca-agua/WF-marca-agua/03-nodos-WFmarca_agua|03-nodos]] · log: [[proyectos/MVP_04-comfyui-arquitectura/n_08-marca-agua/WF-marca-agua/02-WF-log-WFmarca_agua|02-WF-log]] · pendientes: [[proyectos/MVP_04-comfyui-arquitectura/n_08-marca-agua/WF-marca-agua/04-backlog|04-backlog]]
