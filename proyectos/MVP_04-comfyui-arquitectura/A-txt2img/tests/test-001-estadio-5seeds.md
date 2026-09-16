---
tipo: test
id: 001
tema: estadio-5seeds
fecha: 2026-07-17
workflow: ../workflow_txt2img_estadio.json
modelo: architecturerealmix_v11.safetensors
nivel: n_01-txt2img
tags: [test, txt2img, estadio, baseline]
---

# Test 001: Estadio — 5 seeds (baseline)

## Objetivo

Ejecutar el mismo prompt 5 veces variando únicamente la **seed**. Establecer una línea de base (baseline) para entender la variabilidad natural del modelo ArchitectureRealmix y tener referencias para tests futuros.

## Prompt positivo

```
architecturerealmix style, modern football stadium, aerial view, curved steel roof,
floodlights, green pitch, photorealistic, architectural photography, 8K,
highly detailed, dramatic lighting, sunset golden hour
```

## Prompt negativo

```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed
```

## Parámetros fijos

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| resolución | 768x512 |
| denoise | 1 |

## Parámetro variable: seed

| # | seed | Imagen | Observaciones |
|---|------|--------|---------------|
| 1 | 42 | `[activos/proyectos/mvp04-tests/prompts/test-001_estadio_seed42.png]` | Primer render — composición equilibrada, cielo con tonos cálidos. ~114s en AMD DirectML |
| 2 | — | — | Pendiente ejecutar |
| 3 | — | — | Pendiente ejecutar |
| 4 | — | — | Pendiente ejecutar |
| 5 | — | — | Pendiente ejecutar |

## Conclusiones (provisorias)

_Pendiente completar tras ejecutar las 5 variantes._

## Referencias

- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/00-README]] — Documentación del workflow
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/02-WF-log-WFestadio]] — Log versionado de corridas
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/03-nodos-WFestadio]] — Documentación de nodos
- [[README]] — Índice de tests
