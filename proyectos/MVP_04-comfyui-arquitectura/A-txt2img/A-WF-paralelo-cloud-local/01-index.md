---
tipo: indice
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, txt2img, paralelo, comfy-cloud, api-nodes, indice]
---

# 01-index — 4 vías de la comparación txt2img en paralelo

**Fuente de la verdad**: [[PLANS/matriz-pruebas-paralelo-txt2img]] (la matrizeso con tests enumerados). Aquí solo calálogo y configs mínimas.

## Matriz en 3 líneas

| | Modelo ABIERTO | Modelo PRIVATIVO |
|---|---|---|
| **LOCAL (RX 570)** | L1 · SD1.5 (`architecturerealmix_v11`) / L2 · SDXL (Juggernaut XL v9) — ya construidos | L4 · API nodes: NANO Banana (Gemini), GPT Image, Seedream, Recraft (pago por request desde el server local) |
| **CLOUD (Comfy Cloud)** | L3 · mismo grafo L1/L2 retesoographed al cloud GPU | L4-cloud · mismos API nodes con los 4.200 créditos de la sub $20/mes |

**Qué se compara en cada cruz**: imagen resultante (f.x. dif del arco), tiempo de corrida, costo implícito (por corredor si eso se apunta en el log L4), reproducibilidad (seed determinista vs providers sin seed).

## Configs mínimas declaradas

| Vía | Checkpoint/Modelo | Res | Steps/Cfg | Seed A |
|---|---|---|---|---|
| L1 | `architecturerealmix_v11` (SD1.5, en disco) | 512×512 (R2) | 30 / 4.5 | 42 |
| L2 | Juggernaut-XL v9 | 1216×832 | 35 / 4 | 42 |
| L3 | igual L1/L2 en el librarian del cloud — **identidad del model a verificar en la lib de Comfy Cloud** | igual | igual | 42 |
| L4 | API nodes (nano-banana/OpenAI/Seedream) — cada una tiene res/step propias internas; **pero sincronizar: describirlo en 03-nodos** | default API | default API | declarado si el provider seed; sino "sin seed" |

## Orden de corrida recomendado

L2 (referido local de referencia) → L1 (ruido AMD) → L3 (cloud open) → L4 (API privativos) — cada uno con baseline A primero (3 idénticas), arrancadas de modification B/C/D/E/F.
