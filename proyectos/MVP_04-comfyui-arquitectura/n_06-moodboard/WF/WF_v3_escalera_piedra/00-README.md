---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [mvp_04, n_06, moodboard, comfyui, directml, canny, interior]
---

# WF_v3_escalera_piedra — Interior residencial desde croquis2

Alteration local sobre `croquis2.jpg`: vista de frente, escalera de piedra a la derecha, comedor moderno (mesa + sillas) a la izquierda, mesa en primer plano, barra desayunador al fondo.

- Pipeline: LoadImage croquis2 → ImageScale lanczos 512 → Canny 0.31/0.59 → CN canny 0.85/0.0-0.80 + VAEEncode → KSampler denoise 0.75 seed 300 (Realmimix euler_ancestral/karras/30/cfg 7) → `n_06-B-04`.
- Librería Comfy: `n_06-moodboard-WF_v3_escalera_piedra.json` (abre en canvas).
- Estado: `prompt_id e90e858a` encolado vía MCP 2026-09-10.
