---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [mvp_04, n_06, moodboard, comfyui, directml, txt2img, parque]
---

# WF_v4_parque_pajareras — Parque con pajareras de hierro

Adaptación del referente Advertising1 a parque con pajareras de hierro. Como `input/` no tiene foto de parque, va en txt2img puro (sin Canny): Realmimix euler_ancestral/karras/30/cfg 7/seed 400 → `n_06-B-05`.

- Prompt+: parque público, grandes pajareras de hierro forjado ornamental, senderos de grava, césped, árboles maduros, bancos, luz diurna suave.
- Librería Comfy: `n_06-moodboard-WF_v4_parque_pajareras.json`.
- Mejora pendiente: subir fotos del parque a `input/` y correr rama alteration (Canny + denoise 0.75) para re-estilo fiel.
- Estado: `prompt_id 39c9886a` encolado vía MCP 2026-09-10.
