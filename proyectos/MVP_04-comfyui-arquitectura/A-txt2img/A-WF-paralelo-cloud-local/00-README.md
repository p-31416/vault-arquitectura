# 00-README — Paralelo txt2img: Local ↔ ComfyUI Cloud (abiertos + privativos)

Demo aprobado por Sol el 2026-11-01: mostrar **cómo se parte de un txt2img en Comfy Cloud y local en paralelo**, con **modelos abiertos y privativos**.

## Navegación

| Qué | Dónde |
|---|---|
| **Las 4 vías de la comparación** | [[01-index]] |
| **MATRIZ DE PRUEBAS paso a paso** (la estrella, ≥10 tests por WF) | `PLANS/matriz-pruebas-paralelo-txt2img.md` |
| Log de corridas | [[02-WF-log-paralelo]] |
| Configs por vía | [[03-nodos-paralelo]] |
| Pendientes/decisions abiertas | [[04-backlog]] |

## Workflows fuente (reutilizados, ese WF no duplica graphs)

| Vía | Workflow JSON | Árbol |
|---|---|---|
| L1 · Local SD1.5 | `../A-WF-estadio/workflow_txt2img_estadio.json` | [[#Vía L1]] |
| L2 · Local SDXL | `../A-WF-estadio/workflow_txt2img_estadio_sdxl.json` · `../WF-vivienda/workflow_txt2img_vivienda_sdxl.json` | [[#Vía L2]] |
| L3 · Cloud abierto | mismo grafo L1/L2, retarget a Comfy Cloud | [[#Vía L3]] |
| L4 · Privativos (API nodes) | *(JSON se genera cuando el server esté up — nombres de clase al against `/object_info`, R4)* | [[#Vía L4]] |

## Pre-requisitos para arrancar

1. ComfyUI local up (`127.0.0.1:8188`) — al cierre 2026-11-01 estaba down
2. Cuenta Comfy Cloud con login vite (`comfy cloud` de comfy-cli) — estado por confirmar
3. API key de credited-credits para L4 (nano-banana/GPT-Image/…) — ruta de facturacion/expenses en [[04-backlog]]
4. Nomenclatura salidas: `n_XX-{LETRA}-{NN}.png` (tabla completa en reglas); este WF usa prefijos `paralelo-*`
