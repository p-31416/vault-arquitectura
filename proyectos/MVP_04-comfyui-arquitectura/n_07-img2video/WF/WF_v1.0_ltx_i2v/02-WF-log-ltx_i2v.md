---
tipo: log
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, img2video, log, corridas]
---

# Log de corridas — WF_ltx_i2v

Más nuevo → más arriba.

---

## 2026-11-01 — v1.0.0 creado, sin corrida

**Qué:** se diseña y guarda el JSON `workflow_ltx_i2v.json` de la ruta de construcción aprobada (1 txt2img → 2 img2img → 3 img2video-nube → 4 img2 3D). txt2img e img2img ya existían (ver `A-txt2img/`, `n_02-img2img/`), así que arranco en el flujo 3.

**Cadena de nodos:** CheckpointLoaderSimple (ltx-2.3-22b-dev) → LTXAVTextEncoderLoader (gemma fp8) → 2× LoRAs distill → CLIP ×2 (pos/neg) → LTXVConditioning 25fps → LoadImage {render} → ImageScale 768×512 bilinear (R2) → LTXVImgToVideo → RandomNoise → LTXVScheduler 8 steps → CFGGuider 1 → euler → SamplerCustomAdvanced → VAEDecode → CreateVideo → SaveVideo.

**Pendientes antes de la primera corrida (R4):**
- ARRANCAR ComfyUI y validar cada `class_type` + widget contra `/object_info` (transferencia no alcanzado a la fecha: `127.0.0.1:8188` ECONNREFUSED)
- Validar el succésor de `LTXVImgToVideo` en la build 0.39.x (tras la Liberación de LTX 2.3, el nombre exacto del nodo puede variar a una variante sin )— si cambia, ajustar y re-crear desde `create_workflow` action:**validate**
- Localizar o instalar checkpoint LTX-2.3 + text encoder + LoRAs (no en la instalación local; descargar ~24-46GB vía `apply_manifest` pack `ltx-2.3-img2vid` pendiente de `s`) — o correr en **nube** (RunPod, comandos pendientes)
- Seed fijo en `RandomNoise.noise_seed` (272479515887637) para *baseline A reproducible*

**Corridas:** 0
