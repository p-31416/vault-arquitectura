---
tipo: log
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, paralelo, log, corridas]
---

# Log de corridas — WF paralelo cloud ⊕ local

Más nuevo → más arriba.

Corridas totales: **3 en curso** (2026-11-01) — batch `batch_39ffb281-2ed6-4b03-a7f3-5c203f8348cf`

## 2026-11-01 — T2-01 (L2 · A) R-01 baseline ×3 :: Juggernaut XL v9, vivienda, seed 42 — EN COLA/EJECUCIÓN

- Workflow validado R4 (0 errores) antes de encolar. `filename_prefix: paralelo-R01-baseline`
- batch: job1 `abafea6c-…` running · job2 `cee1d6b7-…` pending · job3 `f9e66751-…` pending (estado 23:16 UTC)
- seed 42 fija (`disable_random_seed: true`), 1216×832, 35 steps, cfg 4, dpmpp_2m/karras
- Estimado: ~11 min/corrida en RX 570 (~33 min tanda). Veredicto y salidas: pendientes al cierre de la tanda

## 2026-11-01 — creado sin corrida (diseño)

- Se diseña la matriz de pruebas: [[PLANS/matriz-pruebas-paralelo-txt2img]] — 4 vías (L1/L2/L3/L4) × ~12/10 tests
- Server local **apagado** al cerrar (ECONNREFUSED 127.0.0.1:8188) → R4 del corre no reached charging
- comfy-cli env: workspace P:\00-repos\ComfyUI (default), server running=false — cloud **sin login aún**
- Workflowos fuente reutilizados de `A-WF-estadio/` y `WF-vivienda/` — de sesiones anteriores validados con corridas previas en `INDICE-RENDERS.json` (re-verificar al retomar)
- JSON de la vía L4 (API nodes privativos) riesgo scoping de **class_type desde /object_info** porque los nombres de los nodos API cost variants

## Registro por corrida (template — rellenado a cada corrida)

```
## YYYY-MM-DD — T?-{nn} ({via} · letra?) :: {desc}
- prompt_id: · seed: · duración: · costo:
- files: salidas/n_XX-?-??.png
- veredicto:
```
