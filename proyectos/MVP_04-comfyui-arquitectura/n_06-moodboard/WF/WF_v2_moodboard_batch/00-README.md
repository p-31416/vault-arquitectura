---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [mvp_04, n_06, moodboard, comfyui, directml, batch]
---

# WF_v2_moodboard_batch — Moodboard local (copia del referente)

Réplica local DirectML de `Advertising1 - Moodboard Creation.json` (Recraft + GPT-Image con costo → nodos locales sin costo). El v1 queda intacto para tu uso.

- SELECTS: 3x LoadImage (`croquis001.jpg`, `estadio_futbol_00001_.png`, `IMG_2305 (1).jpg`) + ImageScale lanczos 512 (R1).
- METHOD 1 VARIATION (reemplaza Recraft): ImageBatch 2 refs → VAEEncode → KSampler denoise 0.6 seed 100 → `n_06-B-02` (batch de 2).
- METHOD 2 ALTERATION (reemplaza GPT-image): producto + Canny 0.12/0.39 + CN canny 0.8 + VAEEncode → KSampler denoise 0.75 seed 200 → `n_06-B-03`.
- Librería Comfy: `n_06-moodboard-WF_v2_batch.json` (abre en canvas).
- Estado: `prompt_id ceac85df` encolado vía MCP 2026-09-10.
