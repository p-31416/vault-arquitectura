---
tipo: backlog
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, workflow, backlog, flux2, klein, lora]
---

# WF-rhino-to-image — backlog

## Bloqueantes (antes de la primera corrida)

- [ ] Copiar `rhino-to-image-lora.basic.safetensors` a `P:\00-repos\ComfyUI\models\loras\`
- [ ] Descargar el stack FLUX.2 klein 9B (transformer + text encoder Qwen3-8B + VAE) en el pod
- [ ] Exportar desde Rhino las 3 pasadas (`geo_shaded`, `geo_lines`) + foto de material
- [ ] Confirmar con el instructor: trigger word, modelo base (Base vs Destilado), variante `.advanced`, licencia
- [ ] Validar el grafo en vivo contra `/object_info` del ComfyUI del pod

## Experimentos

- [ ] A/B/C/D con `strength_model` 0,0 / 0,6 / 0,8 / 1,0 (mismo seed)
- [ ] Destilado (4/1) vs base (20/5) con el LoRA activo
- [ ] Efecto de la tercera referencia (`geo_lines.png`) como `ReferenceLatent` adicional
- [ ] `FluxKVCache` (experimental) para acelerar multi-referencia
- [ ] Método de referencia: `index` vs `offset` vs `uxo/uno`
- [ ] Resolución de trabajo 1024×1024 vs 1024×768 (aspecto de la vista de Rhino)
- [ ] 3 fotos de material distintas (principal, mood, secundario) para evitar el efecto "todos los edificios se parecen"
- [ ] Variante GGUF Q4 en la PC local con offload del text encoder a RAM

## Producción (concurso, entrega 16/12)

- [ ] 20-40 imágenes finales a 1024-2048 px en el pod
- [ ] Upscale a lámina A1 (≤15 MB, JPEG) — `UltimateSDUpscale` o `4x_NMKD-Superscale` (comercial)
- [ ] Lámina con el antes/después del workflow Rhino-to-image (demuestra el método ante el jurado)
- [ ] Anotar en la lámina que las imágenes son generadas con IA y la licencia del material de la Fundació

## Decisiones a registrar (ADR)

- [ ] ADR: nube como ruta de render (RunPod 24 GB) frente a local 8 GB
- [ ] ADR: uso de FLUX.2 klein 9B (Non-Commercial) para el concurso y reentrenamiento en 4B (Apache 2.0) para clientes
