---
tipo: adr
numero: 001
workflow: n_03-controlnet
fecha: 2026-07-19
ultima_actualizacion: 2026-07-19 21:00
status: accepted
tags: [adr, controlnet, scribble, depth, canny, comfyui]
---

# ADR-001: Bifurcación del Workflow ControlNet

## Contexto

El workflow `n_03` genera renders arquitectónicos desde un croquis esquemático de estadio usando ControlNet Canny. El croquis es incompleto y lineal — líneas sueltas, sin relleno, sin textura — ideal para un esquema conceptual pero no para un render fotorrealista.

### Problemas detectados

1. **Canny fuerza líneas fragmentadas** — el edge detector produce bordes discontinuos que el modelo se ve forzado a seguir, generando líneas cortadas en el render.
2. **El croquis es esquemático, no realista** — Canny intenta bordes exactos, pero el croquis no los tiene. Necesitamos un ControlNet que entienda "esto es un boceto, completá el resto".
3. **Falta de información espacial 3D** — Canny solo da bordes 2D. No hay profundidad, masas, ni volumetría.

### Opciones evaluadas

| Opción | Rama | ControlNet | VRAM extra | Mejor para |
|--------|------|-----------|------------|------------|
| v1.0.x | Canny suave (strength ~0.3) | Canny baseline | 0 GB | Ajuste mínimo, ya instalado |
| **v1.1a** | **Scribble** | Scribble — garabatos/bocetos | ~689 MB | Croquis incompletos, bocetos |
| **v1.1b** | **Dual Canny+Depth** | Canny + Depth | ~689 MB (ya instalado) | Estructura 2D + 3D combinada |

## Decisión

Bifurcar el workflow `v1.0.2` en **dos variantes paralelas**:

```
v1.0.x (canny baseline — deprecado)
    ├── v1.1a → Scribble ControlNet  (bocetos → render directo)
    └── v1.1b → Dual Canny + Depth   (bordes + profundidad)
```

Ambas son experimentales. La que dé mejor resultado se consolidará como la línea principal.

### v1.1a: Scribble ControlNet

Usa `control_v11p_sd15_scribble.safetensors`, diseñado para garabatos y bocetos esquemáticos. El modelo interpreta el croquis como "intención" y completa texturas, luces y detalles.

Pipeline: `LoadImage → ImageScale → ControlNetApply (Scribble) → KSampler` — sin preprocesador, el croquis se alimenta directo al modelo Scribble.

### v1.1b: Dual Canny + Depth

Usa dos ControlNet en paralelo sobre el mismo KSampler:
- **Canny** (strength ~0.3): bordes gruesos como guía de composición
- **Depth (Depth Anything 3 Small)** (strength ~0.6): estructura espacial 3D, masas, profundidad

Pipeline: 
```
LoadImage → ImageScale ──┬──→ Canny ──→ ControlNetApply (Canny) ──┐
                          │                                        │
                          └──→ DA3Inference → DA3Render ──→ ControlNetApply (Depth) ──→ KSampler
```

Ambos controlnets caben en 8GB VRAM con SD 1.5 (verificado en AGENTS.md).

## Consecuencias

- **Positivo:** Cada workflow se puede optimizar independientemente sin romper el otro.
- **Positivo:** Comparación directa A/B para decidir el enfoque definitivo.
- **Negativo:** Mantenimiento de dos grafos separados (se duplica el log de corridas).
- **Negativo:** Si v1.1a funciona, el modelo Scribble se descarga automáticamente al ejecutarse el workflow.

## Convención de nombrado

### Workflows activos

```
WF_v{mayor}.{patch}__{desc}.json      (flujo único — v1.0.x)
WF_v{mayor}{rama}.{patch}__{desc}.json (bifurcación — v1.1a, v1.1b)
```

Ejemplos:
- `WF_v1.0.2__stadium-prompt-tuned.json` — baseline Canny
- `WF_v1.1a.0__scribble.json` — Scribble
- `WF_v1.1b.0__dual-canny-depth.json` — Dual

### Backups

```
BAK_v{version}__{desc}.json
```

### Imágenes en outputs-salidas/

Para trazabilidad, el prefijo en SaveImage incluye la variante:

| Workflow | Prefijo SaveImage | Ejemplo archivo |
|----------|-------------------|-----------------|
| Baseline Canny (v1.0.x) | `n_03-v{version}_{corrida}` | `n_03-v1.0.2_01.png` |
| Scribble (v1.1a) | `n_03-v1.1a-scribble-` | `n_03-v1.1a-scribble-01.png` |
| Dual (v1.1b) | `n_03-v1.1b-dual-` | `n_03-v1.1b-dual-01.png` |

Las letras (A, B, C) siguen la leyenda existente:
- **A** = Baseline del workflow
- **B** = Variación de parámetros
- **C** = Variación mayor de configuración

## Referencias

- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/workflow_log-n_03_WF01|Workflow Changelog]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01|n_03-WF01-croquis-estadio]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/nodos-n_03_WF01|Índice de nodos]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/adr/00-index|ADRs]]
- [[reglas-workflows-comfy|Reglas de Workflows ComfyUI]]
- [ControlNet Scribble — ComfyUI Docs](https://docs.comfy.org/controlnet-guide)
