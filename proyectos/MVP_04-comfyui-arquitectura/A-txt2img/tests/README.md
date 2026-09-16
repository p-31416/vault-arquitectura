---
tipo: indice-tests
nivel: n_01-txt2img
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [tests, indice, txt2img]
---

# Tests — Nivel 01: txt2img

Cada test es una corrida documentada del workflow con un conjunto de parámetros. Un test puede tener múltiples variantes ejecutadas en ComfyUI (3-5 corridas por test).

## Nomenclatura

```
test-{nnn}-{tema}.md
```

| Parte | Descripción |
|-------|-------------|
| `nnn` | Número secuencial (001, 002...) |
| `tema` | Palabra clave del experimento |

## Convención de imágenes

Cada test genera `N` imágenes. Se guardan con la misma nomenclatura:

```
test-{nnn}_{tema}_{variable}{valor}.png
```

**Ejemplos:**
- `test-001_estadio_seed42.png` — test 001, seed 42
- `test-001_estadio_seed12345.png` — test 001, seed 12345

**Ruta:** `activos/proyectos/mvp04-tests/prompts/`

## Tests planificados (txt2img)

| # | Archivo | Variable | Descripción | Estado |
|---|---------|----------|-------------|--------|
| 001 | [[test-001-estadio-5seeds]] | seed (5 valores) | Mismo prompt 5 veces para ver variabilidad | ✅ Documentado |
| 002 | — | cfg | Probar cfg 5, 7, 10, 14 | 🔜 Pendiente |
| 003 | — | sampler | Comparar euler vs dpmpp_2m vs dpmpp_sde | 🔜 Pendiente |
| 004 | — | steps | 15 vs 30 vs 45 pasos | 🔜 Pendiente |
| 005 | — | scheduler | normal vs karras vs exponential | 🔜 Pendiente |
| 006 | — | prompt | Cambiar atmósfera/estilo del prompt | 🔜 Pendiente |
| 007 | — | resolución | 512x512 vs 768x512 vs 768x768 | 🔜 Pendiente |
| 008 | — | composición | Prompt combinado (material + entorno + estilo) | 🔜 Pendiente |
| 009 | — | batch | Generar 4 imágenes a la vez | 🔜 Pendiente |
| 010 | — | mejor práctica | Prompt optimizado + cfg + sampler ideal | 🔜 Pendiente |

## Navegación

- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/01-index]] — Índice con tabla de variantes
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/02-WF-log-WFestadio]] — Log detallado de corridas
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/04-backlog]] — Próximas pruebas pendientes
