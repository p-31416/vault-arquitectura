---
tipo: log
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [sesion, wf-curso, marca-agua, comfyui, dashboard, flux, civitai, sistema-estudio]
idioma: es
---

# 2026-11-02 — Sesión WF-curso consolidado + marca de agua + WF-watermark01 al tablero

Más nuevo → más arriba.

## Qué se hizo

1. **WF-curso unificado**: `flujos/` + `workflows/sdxl-vista/` → `WF-curso/` canónico (00-index + fichas WF-01..WF-07), 8 `.json` copiados, detalle SDXL y verbatim movidos, carpetas origen borradas, 28+29 archivos re-apuntados, movido a `workflows/WF-curso/`.
2. **`workflows/00-conclusiones.md`** (§1–§11): Check+LoRA, formatos, Flux cuantizado, prompting, CivitAI vs pod.
3. **Preguntas respondidas**: Flux solo GGUF Q4_K_S en AMD DirectML; CivitAI = entrenar estilo propio con fotos del estudio vs pod efímero; watermarks se automatizan con flujo nativo (sin editor).
4. **`n_08-marca-agua/WF-marca-agua/`** (00-README, 01-index, 02-log, 03-nodos, 04-backlog, `workflow_marca_agua.json` v1.1, salidas, PLANS/SPECS): diagnóstico bug fondo negro (`LoadImage` entrega máscara `1-alfa`, fix con `ImageInvert`, verificado en `nodes.py` + `nodes_mask.py`); A-01 bug + A-02 OK logueadas; escala/posición (0.25→173px, 0.35→243px recomendado, centro con fórmula).
5. **`proyectos/00-sistema-estudio.md`** (§1–§8 con marca de agua + envío).
6. **Dashboard**: 10 PNG marca-agua (00001–00010) a `activos/.../marca-agua/wf-watermark01-a01..a10.png`; parámetros exactos por corrida extraídos de `/history` (scale/x/y/blend); 10 entradas `WF-watermark01` en `ITEMS` con `prompt_id` + `segundos_fijo`; regenerados `activos/web/concurso/index.html` (18 imgs) y embebido Emilia.

## Archivos tocados / creados

| Archivo | Qué |
|---|---|
| `proyectos/concurso-gaudi-nexus/workflows/WF-curso/` | nuevo — carpeta canónica (ver §1) |
| `proyectos/concurso-gaudi-nexus/workflows/00-conclusiones.md` | nuevo |
| `proyectos/MVP_04-comfyui-arquitectura/n_08-marca-agua/WF-marca-agua/` | nuevo — flujo + docs + `workflow_marca_agua.json` v1.1 |
| `proyectos/00-sistema-estudio.md` | nuevo |
| `scripts/dashboard-concurso.py` | 10 entradas WF-watermark01 |
| `activos/proyectos/concurso-gaudi-nexus/marca-agua/` | nuevo — 10 PNG (fuera de git) |
| `activos/web/concurso/` | regenerado 18 imgs (fuera de git) |
| `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-concurso.html` | regenerado embebido |
| `raw/sessions/2026-11-02-sesion-marca-agua-dashboard.md` | este cierre |

## Análisis cerebro-digital

- **Topics**: reorg WF-curso, conclusiones checkpoint-LoRA, flux-gguf-directml, civitai-vs-pod, marca-agua-nativa, bug 1-alfa ImageInvert, dashboard ITEMS con prompt_id.
- **Entidades**: WF-curso, WF-marca-agua v1.1, ImageInvert, ImageCompositeMasked, dashboard-concurso.py, /history, ISOLOGO_PITAU, r-01-baseline.
- **Hechos**: 10 corridas marca-agua 2,57 s (frío) y resto <0,5 s — overlay nativo vuela sin GPU pesada; tablero concurso pasa de 8 a 18 imágenes; pendiente probar scale 0.35 (recomendado).
