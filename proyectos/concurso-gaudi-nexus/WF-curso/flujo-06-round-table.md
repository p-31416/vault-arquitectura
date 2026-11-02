---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 6
slug: round-table
titulo_curso: "Round Table: Gaudí and the Architect's Role in the Age of AI"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: pendiente-transcripcion
tags: [mvp_04, curso-ai-gaudi, modulo-6, round-table, gaudi-nexus, jurado]
idioma: es
---

# Módulo 6 — Round Table (flujo del curso)

> Ficha de flujo del módulo 6 del curso AI×Gaudí. **Estado: transcripción pendiente.** El video no expone subtítulos en ninguna de sus dos pistas, así que el material se obtiene bajando el audio del CDN del curso y transcribiéndolo en local con faster-whisper.
>
> Fuente prevista: el audio del módulo `round-table` del CDN del curso (Bunny Stream, library `719269`, playback `68e094ac-771c-44fe-a821-d5fe13b32075`). Procedimiento y comando: [[scripts/transcribir-leccion-bunny_notas|transcribir-leccion-bunny_notas]].

## Qué es este módulo

Una mesa redonda con **Cas Esbach** (SCAD; antes arquitecto en BIG y MVRDV; miembro del jurado del concurso) sobre el papel del arquitecto en la era de la IA. Es el módulo que fija el criterio con el que el jurado va a mirar las entregas, y por eso su transcripción es el insumo del **checklist de cierre de los siete workflows**.

El módulo 7 ya deja expuesta la tesis central que Cas Esbach sostiene en la apertura: la **transferencia conceptual** (la lógica constructiva) por encima de la **transferencia estilística** (la apariencia), y que la ensayo de reducir la esencia de Gaudí a un LoRA deja algo sin-pandemic.

## Procedimiento (3 pasos)

| # | Paso | Comando | Resultado |
|---|------|---------|-----------|
| 1 | Bajar el audio del módulo a `activos/` | `curl.exe -L -H "Referer: https://iframe.mediadelivery.net/" -o "activos\curso-ai-gaudi\videos\mux-round-table.mp4" "https://vz-4ced3a48-15e.b-cdn.net/68e094ac-771c-44fe-a821-d5fe13b32075/play_720p.mp4"` | el mp4 (538 MB), fuera de git |
| 2 | Transcribir en local | `P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir-leccion-bunny.py --modulo round-table --language en` | `raw/yt/transcripts/YYYY-MM-DD_mux-round-table.en.md` + `.srt` + `.txt` |
| 3 | Volcar a flujo y escribir el checklist | ficha esta + [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado\|criterio-jurado]] | el checklist que cierra cada WF |

## Qué tiene que salir de acá

1. La transcripción verbatim en inglés, con timestamps, en la convención del vault.
2. Un resumen en español de los criterios que el jurado explicita.
3. El **checklist de cierre** (5 a 7 puntos), que se copia en el `04-backlog.md` de cada workflow como criterio de aceptación.
4. La confirmación de si el jurado valora el before/after del método en la lámina (dato abierto en el vault: `261019` pide croquis con variación leve de perspectiva y `research:672` propone axonometría renderizada con before/after).

## Vacíos declarados

| Vacío | Estado |
|-------|--------|
| Duración del módulo | sin medir (el subtítulo no está; se mide con la transcripción) |
| Intervenientes y orden de las voces | pendiente de la transcripción |
| Criterios explícitos del jurado | pendiente de la transcripción |
| Si el jurado valora el before/after | pendiente de la transcripción |

## Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/WF-curso/00-index-flujos-origen|Fichas de flujo]] · [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado|Criterio del jurado]] · [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|Plan maestro de workflows]] · [[raw/yt/transcripts/indice-curso-ai-gaudi|Índice del curso]] · [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso]]
