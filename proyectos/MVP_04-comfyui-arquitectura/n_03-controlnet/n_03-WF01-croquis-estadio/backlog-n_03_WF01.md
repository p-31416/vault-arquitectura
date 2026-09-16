---
tipo: backlog
nivel: n_03-controlnet
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-19 22:00
tags: [backlog, pruebas, controlnet, canny, scribble]
---

# Backlog de Pruebas — n_03-controlnet

| # | Propuesta | Origen | Prioridad | Estado |
|---|-----------|--------|-----------|--------|
| 1 | ~~Probar con foto de fachada real como input~~ ✅ | v1.0.0_01 | alta | hecho |
| 2 | Probar MLSD en vez de Canny — mejor para edificios rectos | v1.0.0_01 | media | pendiente |
| 3 | Probar strength 0.5 vs 0.7 vs 0.85 — comparar fidelidad | v1.0.0_01 | media | pendiente |
| 4 | Probar guidance_end 0.5 vs 0.7 vs 1.0 — texturas libres vs fijas | v1.0.0_01 | baja | pendiente |
| 5 | Probar depth map (MiDaS) en vez de Canny — preservar perspectiva | v1.0.0_01 | media | pendiente |
| 6 | Probar lineart para croquis → render | v1.0.0_01 | baja | pendiente |
| 7 | Documentar en wiki/glosario/software/comfyui.md técnica ControlNet completa | vault | alta | pendiente |
| 8 | Pipeline completo end-to-end: txt2img → img2img → ControlNet en cadena | sistema | alta | pendiente |
| 9 | Probar ControlNet con depth map de recorte de croquis (no foto real) | v1.0.0_02 | media | pendiente |
| 10 | ~~Reorganizar carpeta de workflows — separar/mover BAKs a subcarpeta~~ ✅ | sistema | alta | hecho |
| 11 | ~~Crear archivo nodos.md por workflow (no global), vinculado a wiki/glosario/software/comfyui.md con fuentes oficiales~~ ✅ | sistema | media | hecho |
| 12 | ~~Crear carpeta de ADRs para decisiones técnicas del MVP~~ ✅ | sistema | media | hecho |
| 13 | ~~Reescribir prompt interior del estadio + subir strength/end a 0.85~~ ✅ | v1.1a_02 | alta | hecho |
| 14 | ~~Evaluar v1.1a.1 con prompt interior + strength 0.85 — ¿sigue el croquis?~~ ✅ — No: siguió generando exterior | v1.1a.1 | alta | hecho |
| 15 | ~~Probar strength 1.0 si 0.85 no alcanza para forzar composición del croquis~~ ✅ → v1.1a.2 | v1.1a.1 | media | hecho |
| 16 | Evaluar v1.1a.2 — strength 1.0, prompt sin "stadium" — ¿respeta composición interior? | v1.1a.2 | alta | pendiente |


[[index-n_03_WF01]] — [[prompts_log-n_03_WF01]] — [[proyectos/MVP_04-comfyui-arquitectura/n_02-img2img/tests/README|tests n_02 (referencia)]]
