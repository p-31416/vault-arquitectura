---
tipo: backlog
nivel: n_02-img2img
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-19
tags: [backlog, pruebas, img2img, croquis]
---

# Backlog de Pruebas — n_02-img2img

Sugerencias recolectadas de las evaluaciones de cada corrida.

| # | Propuesta | Origen | Prioridad | Estado |
|---|-----------|--------|-----------|--------|
| 1 | Probar denoise=0.3 vs 0.5 vs 0.9 para ver cuánta transformación es ideal | A-01 | alta | pendiente |
| 2 | Probar prompt más descriptivo (no el base genérico) para mejor adherencia | A-01 | media | pendiente |
| 3 | Probar scheduler karras para mejorar contraste en el render | A-01 | baja | pendiente |
| ⚠ | **NEEDED: AI con visión para evaluar renders automáticamente** — revisar calidad, composición, fidelidad arquitectónica y comparar variantes sin depender de inspección manual | sistema | alta | pendiente |
| 4 | Usar render de n_01-txt2img como input de img2img (encadenar flujos) | sistema | alta | pendiente |
| 5 | Probar resize+padding en croquis desiguales antes de pasarlos al workflow | E-01 | media | pendiente |

[[index]] — [[prompts-log]]
