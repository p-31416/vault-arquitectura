---
tipo: log
mvp: 04
version: 1.0.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, log, bitacora]
---

# MVP 04 — Bitácora v1.0.0

## v1.0.1 (2026-07-18)

### Eventos

| Fecha | Nivel | Evento | Detalle | Solución |
|-------|-------|--------|---------|----------|
| 2026-07-17 | n_01 | ✅ A-01 render txt2img | Seed=42, 768×512, ~114s AMD DirectML | — |
| 2026-07-18 | n_01 | ✅ A-02 corrido | Misma config, seed distinta (archivo dif. ~741KB vs 731KB), 88s con caché | — |
| 2026-07-18 | n_01 | ✅ B-01 prompt nocturno | "night match, floodlights on" — 1ra variación de atmósfera | — |
| 2026-07-18 | n_02 | ❌ Error VRAM | Croquis 1600×1350 saturó VRAM al codificar VAE (~1GB tensor falló) | ImageScale agregado como nodo 5 entre LoadImage y VAEEncode. Resize a 512×512 crop=center. |
| 2026-07-18 | n_02 | 🔧 Workflow img2img actualizado | ImageScale cambió de 768×512 crop=disabled a 512×512 crop=center para tolerar cualquier input | — |
| 2026-07-18 | n_02 | ✅ A-01 render img2img exitoso | croquis001.jpg → render 512×512, ~74s, denoise=0.7 | sin OOM gracias a ImageScale |

### Decisión técnica

El ImageScale con 512×512 crop=center es el `default safe` para img2img en hardware limitado (AMD 8GB DirectML). A futuro, para renders de alta resolución, se upscaleará post-generación con nodo dedicado o externamente.

### Pendientes arrastrados

- A-03 (3er baseline n_01)
- Descargar Z-Image Turbo GGUF
- Descargar 4x_foolhardy_Remacri

## v1.0.0 (2026-07-17)

### Logros

- Plan completo y estructura documental del MVP04 creada
- **Primer render exitoso**: estadio de fútbol generado desde texto vía ComfyUI MCP
  - Workflow: `workflow_txt2img_estadio.json` — SD 1.5 txt2img
  - Modelo: ArchitectureRealmix v1.1
  - Tiempo: ~114 segundos (AMD DirectML)
  - Resolución: 768x512, 30 steps, cfg 7, sampler euler
  - Output: `activos/proyectos/mvp04-tests/renders/estadio_futbol_v001.png`
- Workflow guardado como AMV (API JSON) en `n_01-txt2img/`
- Instalación y configuración de artokun/comfyui-mcp como MCP server
- ComfyUI v0.28.0 operativo en `http://127.0.0.1:8188`
- ADR-001 adoptado: artokun/comfyui-mcp seleccionado sobre 4 alternativas
- Documentación fundacional: manifiesto, setup, playbook, privacidad de datos
- Spec v1.0.0 con 5 niveles progresivos definidos
- Plan técnico detallado con pipelines por nivel
- Guía de modelos recomendados para AMD 8GB y hardware ideal (NVIDIA 24GB+)
- Modelo ArchitectureRealmix v1.1 instalado y listo para tests

### Desafíos

- **AMD DirectML**: ComfyUI no detecta GPU AMD como CUDA (solo `privateuseone` con 1024MB reportados). Se necesita flag `--directml`. Posibles incompatibilidades con algunos nodos.
- **VRAM limitada**: 8GB AMD excluye modelos grandes como Flux Dev (24GB) o WAN (24GB). La estrategia es Z-Image Turbo GGUF (~4GB) para iteración y RunPod para renders pesados.
- **Sin modelos turbo instalados**: ArchitectureRealmix es SD 1.5 (bueno pero lento vs modelos turbo modernos). Pendiente descargar Z-Image Turbo GGUF.

### Decisiones tomadas

1. ArchitectureRealmix v1.1 como modelo primario inmediato (ya instalado)
2. Z-Image Turbo GGUF Q4_K_S como modelo secundario prioritario (descarga pendiente)
3. Todos los workflows guardados en formato API JSON (AMV)
4. Outputs guardados en `activos/proyectos/<cliente>/renders/`
5. RunPod como opción cloud escalable (vs Comfy Cloud más caro)

### Próximos pasos (n_01-txt2img)

1. Descargar Z-Image Turbo GGUF Q4_K_S
2. Descargar 4x_foolhardy_Remacri (upscaler)
3. Completar test-001: ejecutar 5 seeds restantes y documentar cada imagen
4. Tests 002-010: cfg, sampler, steps, scheduler, prompt, resolución, batch
5. Extraer conclusiones por test → prompt óptimo compuesto
6. Pasar a n_02-img2img (croquis → render + composición paisaje+estadio)

### Referencias

- [[01-spec-mvp_04]]
- [[02-ft-mvp_04]]
- [[modelos-recomendados]]
