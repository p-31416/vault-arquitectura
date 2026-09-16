---
tipo: log
fase: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [mvp_04, n_06, log]
---

# 02-WF-log — Más nuevo → más arriba

## 2026-09-10 — v2 COMPLETO vía MCP (221s, success)

- Salidas: `salidas/n_06-B-02a.png` + `n_06-B-02b.png` (variation batch, denoise 0.6 seed 100) + `salidas/n_06-B-03.png` (alteration, denoise 0.75 seed 200).
- Lectura: B-02a villa travertino con pérgola y pileta (toscana lograda); B-02b casa patio nocturna con deck (fiel al estadio/vista); B-03 atrio vidriado con piedra (alteration golden hour).
- Flujo en librería Comfy: `n_06-moodboard-WF_v2_batch.json`.

## 2026-09-10 — v2 encolado vía MCP (render en curso)

- `prompt_id ceac85df-66a8-4c7e-a53c-d3abb216d0bf` (validate OK 23 nodos, enqueue OK).
- Rama B-02 (variation): batch croquis001 + estadio, denoise 0.6, seed 100, Realmimix euler_ancestral/karras/30/cfg 7.
- Rama B-03 (alteration): IMG_2305 + Canny 0.12/0.39 + CN 0.8/0.0-0.80 + denoise 0.75, seed 200, prompt "new photography golden hour".
- Salidas esperadas: `salidas/n_06-B-02-*.png` (x2) + `salidas/n_06-B-03.png`.
