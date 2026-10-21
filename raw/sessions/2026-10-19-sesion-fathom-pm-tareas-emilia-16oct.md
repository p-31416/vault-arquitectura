---
tipo: log
fecha_creacion: 2026-10-19
ultima_actualizacion: 2026-10-19
tags: [sesion, fathom-pm, emilia, tareas, leantime, pomodoros, concurso]
---

# Sesión 2026-10-19 — @fathom-pm: tareas de las 2 últimas reuniones del 16/10 con Emilia

## Qué se hizo

- Leí completas las 2 reuniones pedidas (las más recientes en orden cronológico inverso):
  - `raw/reuniones/2026-10-16_emilia-proyectopi_193660891.md` — 20:33 AR "OS Emilia: agentes de Telegram + ComfyUI" (720 turnos).
  - `raw/reuniones/2026-10-16_emilia-proyectopi_193639289.md` — 19:31 AR "Concurso Gaudí Nexus" (592 turnos).
- La API de Fathom devuelve `action_items` **vacío** en ambas: extraje las tareas del `## Resumen` (Próximos pasos) y de la `## Transcripcion` completa, marcando en cada task el origen (`resumen ts N` / `transcripción mm:ss`).
- Leí el material vigente para no duplicar: `specs/` (8 vivos + `specs/archived/README.md`), [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n v2.0]], resumenes de flujo (Router / Voz / Agenda Sub TEST), [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] y el dashboard de cierre Mes 1.
- Generé 2 specs (1 por tema, según el flujo del agente):
  - `specs/261019-plan-agentes-telegram-agenda-emilia.md` — 19 tareas · milestones M-A1…M-A4 · 19 cards de Leantime en el proyecto 4 (`O.S_ARQ-Emi`).
  - `specs/261019-plan-concurso-gaudi-nexus-ia.md` — 13 tareas · milestones M-B1…M-B6 · 13 cards en tablero propio (línea del estudio, fuera del contrato Studio OS).
- Regla pomodoro aplicada: subtasks de ≤25 min, tope 16 pomodoros/día por persona (Emilia 42 pom · Sol 56 pom en la semana 19→25/10, con el domingo de jornada), WIP ≤2, cada task cita milestone + OKR o `sin-alineacion`.
- Preparé el plan de carga a Leantime (sprint `S1`, milestones, cards con `planHours` 0,42 h por pomodoro, orden de carga de 15 min). **No ejecuté la carga**: queda esperando el "s" de Sol.
- Actualicé el dashboard de cierre Mes 1 (23 → 26 reuniones transcriptas + links a los 2 specs + §7 de la semana).

## Hallazgos

- **Doble cuenta con el plan existente:** el alta de Emilia al grupo de Telegram aparece como próximo paso del resumen de la reunión 19:31 y se ejecutó dentro de la reunión 20:33 (00:05:31-00:05:58). Queda como hecho, no como tarea.
- **No se duplicó la instalación del stack en el PC de Emilia:** ya especificada en [[specs/261013-plan-fuentes-emilia-inbox|plan inbox §11]]; en el plan nuevo se marca la ejecución (B7) y se dice que la card vive en el plan previo.
- **Puntaje de Pomodoro del plan:** carga total de la semana por debajo del tope diario en las dos personas; el excedente corresponde al carril propio del estudio (concurso) más la cita presencial del miércoles 21/10 13:00.
- **Cifras a verificar contra la convocatoria:** el resumen dice €175 de inscripción y €10.000 de premio; la transcripción nombra "175 dólares por equipo" y no menciona el premio. Queda en `## Preguntas` de ambos specs, sin afirmarlo como dato.
- **Fechas sin confirmar:** la entrega del trabajo del curso aparece como "hasta fin de octubre" (00:19:15) y en un "martes 18:30" (00:59:16) sin saber a qué entrega se refiere. M-A1 queda con fecha provisional y la pregunta abierta.

## Análisis cerebro-digital

**Topics:** fathom-pm, derivación-de-tareas-sin-action-items, plan-semanal-pomodoros, carga-leantime-preparada, gaudi-nexus, tokenizacion, propiedad-intelectual, agenda-cal-com-google-calendar, comfyui-modelos, biblioteca-personal.

**Entidades:** reunión 193660891 · reunión 193639289 · recording 193621124 (fuera de alcance en esta tanda) · bot `OS.emi-pi` · grupo Fuentes `-5417177870` · Sheet `Fuentes-Inbox` `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI` · tool `leer_calendario` · `eventTypeId 7467793` (Sol) · proyecto Leantime 4 `O.S_ARQ-Emi` · MCP Leantime local (sin tools expuestas en esta sesión).

**Hechos:** las 2 reuniones del 16/10 vienen sin `action_items`; el bot de agenda espera el mensaje de activación de Emilia; la credencial de cal.com de Emilia ya está del lado de Sol y falta la de Google Calendar; el curso/TCC sigue con el tópico 5, la conclusión y el listado de referencias; la entrega protegida se define como JPG/PNG de resolución limitada y nunca PDF con cotas.

## Queda

- Visto bueno de Sol (`s`) para cargar las 32 cards en Leantime.
- Responder las 7 preguntas del plan agentes + 8 del plan concurso (fecha de entrega, moneda de la inscripción, rol de Kiki, token `OS.emi-pi` vs `emiliaospi_bot`, canal de avisos, tablero del concurso).
- Revisión trimestral: los 2 specs nuevos entran al barrido de "8 vivos" del plan unificado.
