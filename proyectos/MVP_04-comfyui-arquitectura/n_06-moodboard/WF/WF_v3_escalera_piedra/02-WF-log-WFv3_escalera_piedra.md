---
tipo: log
fase: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [mvp_04, n_06, log]
---

# 02-WF-log — Más nuevo → más arriba

## 2026-09-10 — v3 COMPLETO vía MCP (88s, success)

- Salida: `salidas/n_06-B-04.png` (prompt `e90e858a`, 88.63s).
- Lectura: comedor doble altura luminoso, escalera de piedra a la derecha, mesa + sillas en primer plano, barra al fondo entre vidrios, travertino + madera. Layout del croquis2 respetado.
- Flujo en librería Comfy: `n_06-moodboard-WF_v3_escalera_piedra.json`.

## 2026-09-10 — v3 encolado vía MCP (render en curso)

- `prompt_id e90e858a-ebfa-42ad-956c-6f60738f5c34` (validate OK 12 nodos, enqueue OK).
- Input: `croquis2.jpg` (nuevo en `input/`, confirmado vía `node_info LoadImage verbose`).
- Prompt+: front view residencial, stone staircase derecha, comedor moderno + mesa/sillas izquierda, mesa primer plano, barra desayunador fondo, travertino + madera, luz natural.
- Params: Canny 0.31/0.59, CN 0.85/0.0-0.80, denoise 0.75, seed 300.
- Salida esperada: `salidas/n_06-B-04.png`.
