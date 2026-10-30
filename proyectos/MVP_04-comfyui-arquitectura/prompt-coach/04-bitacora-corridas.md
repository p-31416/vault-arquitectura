---
tipo: log
mvp: 04
carpeta: prompt-coach
origen: definicion de @tim con SOL, sesion 2026-10-30
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [mvp_04, comfyui, bitacora, corridas, prompts, log]
idioma: es
---

# Bitácora de corridas — índice central

> Registro de las corridas que valieron la pena. Cada línea apunta al log completo del WF y a la salida, para repetir lo que funcionó y descartar lo que no.
>
> **Más nuevo → más arriba.** Las entradas se agregan debajo del encabezado de tabla. El detalle completo (todas las corridas, incluso las descartadas) queda en el `02-WF-log-WF<nombre>.md` del WF correspondiente.

## Formato de fila

| Fecha | Receta (recortada) | Modelo · params clave | Log completo | Salida | Veredicto |
|---|---|---|---|---|---|
| `YYYY-MM-DD` | `@tim <qué se pidió>` | modelo · seed · steps · cfg · strength | wikilink al `02-WF-log-*` | ruta de `n_XX-*` | qué funcionó / qué cambiar |

"Veredicto" es una línea: qué quedó bien y la primera variable a probar si se repite.

## Corridas

| Fecha | Receta (recortada) | Modelo · params clave | Log completo | Salida | Veredicto |
|---|---|---|---|---|---|
| — | (sin corridas registradas aún; la primera va arriba) | — | — | — | — |

## Cómo se alimenta

1. SOL da el `s` y la corrida se ejecuta (`comfyui_execute_workflow`).
2. `@tim` escribe el log completo en el `02-WF-log-WF<nombre>.md` del WF.
3. Si el resultado es repetible, `@tim` agrega la fila aquí, al principio.
4. El playbook [[wiki/glosario/interno/pbooks/pbk-comfy-agent|pbk-comfy-agent]] enlaza acá desde las recetas, así aprendés qué receta dio qué foto.

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/00-README|Prompt Coach del curso — archivo]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] — R1–R4 y nomenclatura `n_XX-{A–G}-{NN}.png`
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — flujos y parámetros de base
