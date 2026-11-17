---
tipo: indice
mvp: 09
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_09, croquis-render, realvis, sdxl, controlnet, lora, local]
idioma: es
---

# MVP 09 — croquis → render (RealVis, todo local $0)

> Batería del spec [[specs/261112-plan-pruebas-rumbo-miercoles|rumbo miércoles]] pruebas 2–5 (la 1 ya es la serie F0 del MVP 08).
> Regla: píxel final siempre RealVisXL v5.0 estándar. SD1.5 descartado como base.

## Puerta de entrada

- Flujos: [[proyectos/MVP_09-croquis-render/flujos/00-README|00-README]] (S0 croquis → S1 render → S2 ControlNet → S3 LoRA).
- Prompt croquis + seed: [[proyectos/MVP_09-croquis-render/flujos/S0-croquis|S0-croquis]].
- Keeper F0 que alimenta referencias: `proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T3-steps40-keeper.png`.
