---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [mvp_04, n_06, moodboard, comfyui, directml, fachada, hormigon, madera, hamad]
---

# WF_v5_fachada_hormigon_madera — Fachada hormigón visto + madera oscura (corrección Hamad)

Corrección de `WF_v2_batch` tras corrida `351ff3db` (30/09/2026): los outputs derivaron a villa toscana. Este WF alinea prompts a casa Hamad (hormigón visto, madera oscura, volumen elevado, puente, bosque pinos).

- **Base:** `WF_v2_batch` (`n_06-moodboard-WF_v2_batch.json`) — 12 nodos, Canny + Realmimix. R1 ImageScale 512 → ajustado a 768x512 / 512x768 según orientación para no recortar puente/voladizo.
- **Cambios clave:** 1 imagen = 1 rama (elimina `ImageBatch` híbrido), prompt Hormigón+Madera (3 variantes), `Canny 0.31/0.59 + ControlNet 0.90 / 0.0-0.85`, `denoise 0.40` (antes 0.6/0.75), negativo bloquea `tuscan/stone villa/cypress/travertine`.
- **Inputs:** `01hamad.JPG` (768x512), `02hamad.JPG` (512x768), `03hamad.JPG` (768x512) en `ComfyUI\input\`.
- **Outputs:** `n_06-C-01`/`C-02`/`C-03` (1 por ref, letra C = variación parámetros según `reglas-workflows-comfy.md`), seeds 42/77/123.
- **Estado:** workflow listo en `workflow_fachada_hormigon_madera.json` + librería Comfy `n_06-moodboard-WF_v5_fachada_hormigon_madera.json`. Encolar vía MCP.
- Ver `01-index.md`, `02-WF-log-WFv5.md`, `03-nodos-WFv5.md`, `03-log-mvp_04.md` (v1.0.2).
