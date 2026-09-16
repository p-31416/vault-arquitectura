---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [mvp_04, n_06, moodboard, comfyui, directml, canny]
---

# WF_v1_local_Canny_IPA — Moodboard L1+L2 local

Variante local DirectML de `Advertising1 - Moodboard Creation.json` (Recraft + GPT-Image con costo → Canny + Realmimix sin costo). Base: `pbk-comfyui` pipeline Canny + R1 ImageScale 512.

- L1 Variation: este JSON (`workflow_moodboard_local.json`) — Canny 0.31/0.59 + CN 0.85/0.0-0.80 + Realmimix euler_ancestral karras 30 cfg 7 seed 42.
- L2 Alteration: misma base, Canny producto 0.12/0.39 + IPAdapter product 0.8 + denoise 0.75. IPA documentado en `03-nodos`, activo cuando el pack esté instalado.
- Fallback cuando IPAdapter ausente: VAEEncode img2img denoise 0.65.
- Estado MCP 2026-09-09: Comfy `http://127.0.0.1:8188` inalcanzable + `P:\00-repos\ComfyUI\main.py` falla por `ModuleNotFoundError: sqlalchemy`. Encolar pendiente a instalar dependencia y arrancar con `corre_comfyui.bat`.
- Ver `01-index.md`, `02-WF-log-WFv1_local_Canny_IPA.md`, `03-nodos-WFv1.md`, `specs/260909-moodboard-vault-visual-local.md`.
