---
tipo: indice
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, txt2img, hires, fractal, gaudi, indice]
---

# A-WF-fractal-hires — txt2img de máxima definición (prompt fractal Gaudí)

Prompt fuente: [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal#11. Prompt Gemini — listo para copiar|prompt Gemini §11]] (vista aérea mandala). Adaptado a dialecto SDXL (sin `--ar/--no`, negativos a Negative).

## Variantes (misma seed 42/43, mismo prompt — la variable es el checkpoint)

| JSON | Checkpoint | Pasada base | Hires ×1.5 | Estado |
|---|---|---|---|---|
| `workflow_fractal_hires_juggernaut.json` | Juggernaut XL v9 | 30 steps, cfg 4 | 20 steps, denoise 0.35 | ⏳ encolado |
| `workflow_fractal_hires_realvisxl.json` | RealVisXL V5.0 | 30 steps, cfg 4 | 20 steps, denoise 0.35 | ⏳ encolado |
| `workflow_fractal_hires_lightning.json` | RealVisXL V5-Lightning | 6 steps, cfg 1.5 | 4 steps, denoise 0.4 | ⏳ encolado |
| `workflow_fractal_nanobanana.json` | Nano Banana (GeminiImageNode) | API, 16:9 | — | ⛔ requiere login Comfy org con créditos |

- Log: [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-fractal-hires/02-WF-log-fractal-hires|02-WF-log]]
- Nodos: [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-fractal-hires/03-nodos-fractal-hires|03-nodos]]
- Backlog: [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-fractal-hires/04-backlog|04-backlog]]
- Flux: ningún checkpoint Flux en disco → fuera de esta tanda (vía RunPod/cloud cuando se active)
