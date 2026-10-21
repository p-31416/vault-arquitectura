---
tipo: plan
proyecto: Proyecto Pi
cliente: Estudio (línea propia)
fecha_creacion: 2026-10-19
ultima_actualizacion: 2026-10-19
estado: borrador
tags: [concurso, gaudi-nexus, comfyui, rhino, tokenizacion, propiedad-intelectual, honorarios, ip, pomodoros, leantime]
idioma: es
---

# Concurso Gaudí Nexus + modelo de honorarios por propiedad intelectual

> Origen: reunión del 16/10/2026 19:31 AR "Concurso Gaudí Nexus" (592 turnos), importada de la cuenta Fathom Proyecto Pi → [[raw/reuniones/2026-10-16_emilia-proyectopi_193639289|transcript 193639289]]. Contexto de import: [[raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct|sesión import 19/10]]. La API de Fathom devuelve `action_items` vacío para esta reunión: cada tarea sale del `## Resumen` (Próximos pasos) o de la `## Transcripcion` completa, con el timestamp de origen marcado.
>
> Relacionado: [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes Telegram + agenda]] (misma tanda, tema hermano) · [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04 ComfyUI]] · [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|MVP_05 Rhino MCP]] · [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]].

## 1. SPEC

### 1.1 Objetivo

Entrar al concurso "Gaudí Nexus" con el flujo de IA de punta a punta (Rhino → ComfyUI → SD) y, en paralelo, resolver la pregunta de fondo que la reunión abrió: **cómo se cobra la arquitectura cuando el cliente puede replicar el concepto con IA**. Dos entregables: la propuesta del concurso y una nota de modelo de honorarios por propiedad intelectual + tokenización.

### 1.2 Lo que la reunión dejó en pie

| Pieza | Estado al 16/10 | Evidencia |
|---|---|---|
| Decisión de participar | Tomada: "yo dije que sí" | Transcripción 00:13:12-00:13:20 |
| Inscripción | **Hecha** (19/10): ya están inscriptos Sol + Emilia | Confirmación de Sol, 19/10 |
| Fecha de entrega | **16/12/2026** | Confirmación de Sol, 19/10 |
| Tablero del carril | **Proyecto Leantime propio** (línea propia del estudio, fuera del contrato Studio OS × Emilia) | Decisión de Sol, 19/10 |
| Bases y entregables | Leídos y traducidos a tareas en la conversación | Transcripción 00:12:33-00:13:00, 00:05:00-00:06:14 |
| Requisitos técnicos del concurso | Texto→imagen, edición de imágenes con IA, video de IA para presentación, reconstrucción 3D desde imágenes IA, modelo IA entrenado con artículos de la Fundación Antoni Gaudí | Transcripción 00:12:33-00:13:00 |
| Lógica constructiva paramétrica de Gaudí | Requisito explícito, no estética | Resumen (ts 385) + transcripción 00:06:25-00:07:00 |
| Protección de IP en la entrega | Criterio acordado: JPG/PNG de resolución limitada, nunca PDF con cotas | Transcripción 00:24:26-00:24:56, 00:26:32-00:27:00, 00:54:00 |
| Honorarios por m² → propiedad intelectual | Planteado, sin cierre | Transcripción 00:56:00-00:57:40 |
| Tokenización de diseños | En investigación (el socio cursa posgrado en tokenización de activos inmobiliarios) | Resumen (ts 3240) + transcripción 00:29:00-00:29:18, 00:54:00-00:55:16 |
| Tesis de neuroarquitectura con IA | En curso: falta el tópico 5, la conclusión y el listado de referencias | Resumen (ts 1864) + transcripción 00:37:45-00:39:30 |

### 1.3 Alcance

- Dentro: inscripción, checklist de entregables, procedimiento de entrega protegida, flujo Rhino+Comfy con estilo propio, y la nota de honorarios/tokenización.
- Fuera: el modelo de render "notoriamente IA" (se apunta a estilo propio, tarea F5), la ejecución del material que ya vive en el plan hermano (tarea A1 de [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes Telegram]]), y la ampliación de la tesis a otros idiomas.
- Línea propia del estudio: este plan no se factura dentro del contrato Studio OS × Emilia; las horas se registran aparte.

### 1.4 Criterio de cierre del plan

Inscripción pagada y registrada con los dos nombres, checklist de entregables del concurso en una hoja, un flujo Rhino+Comfy con sello propio funcionando sobre un caso real, el procedimiento de entrega protegida documentado y probado, y la nota de honorarios por propiedad intelectual con el caso de tokenización resuelto.

## 2. PLAN semanal (Lun 19/10 → Dom 25/10)

Pomodoros de 25 minutos por persona y día (máx. 16/día). La carga conjunta con el plan hermano se mantiene dentro del tope: ver §2 de [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes Telegram]].

| Día | Foco del carril del concurso | Emilia (pom) | Sol (pom) |
|---|---|---|---|
| **Lun 19/10** | Pago de la inscripción + links de la convocatoria | — | 2 |
| **Mar 20/10** | Datos de inscripción + checklist de entregables | 3 | 2 |
| **Mié 21/10** | Repaso de bases con Sol (en la cita presencial) | 2 | 2 |
| **Jue 22/10** | Flujo Rhino + ComfyUI con estilo propio | — | 4 |
| **Vie 23/10** | IP de entrega + modelo de honorarios + flujo documentado | 3 | 14 |
| **Dom 25/10** | Jornada de trabajo del concurso (cadencia acordada) | 4 | 4 |

Totales del carril: Emilia 14 pomodoros (≈5,8 h, 4 de ellos el domingo) · Sol 28 pomodoros (≈11,7 h, 4 de ellos el domingo).

Hitos: **M-B1** inscripción pagada y registrada (cerrado 19/10) · **M-B2** bases → checklist de entregables (mar 20/10) · **M-B3** flujo Rhino+Comfy con estilo propio (jue 22/10) · **M-B4** entrega protegida documentada (vie 23/10) · **M-B5** nota de honorarios por PI + tokenización (vie 23/10) · **M-B6** entrega del concurso (**mié 16/12/2026**).

> La entrega real es el **16/12**: la semana del 19/10 es la de arranque (bases, flujo y criterios) y no la de producción final. El plan operativo se abre en sprints quincenales hasta el 16/12 cuando se defina la cadencia; esta versión cubre el arranque.

## 3. TASKS

> `resumen ts N` = Próximos pasos del resumen de Fathom. `transcripción mm:ss` = turno literal. Alineación: `sin-alineacion` para el carril propio del estudio; el objetivo interno es el que el resumen define en ts 2581 ("base de conocimiento para entrenar modelos de IA personalizados que capturen el estilo de un arquitecto").

### E. Emilia

- [ ] **E1 — Inscribirse en el concurso con los datos de los dos** · 3 pom · Emilia · M-B1 · **CERRADO 19/10** (ya inscriptos Sol + Emilia)
  - [x] E1.1 Leer la convocatoria y confirmar qué datos pide por persona — 25 min · `resumen ts 792` + `transcripción 00:55:47-00:56:00`
  - [x] E1.2 Completar la inscripción con el nombre de Sol y un mail accesible por él — 25 min · `transcripción 00:55:47` ("cuatro personas pueden estar inscritas")
  - [ ] E1.3 Guardar el comprobante y volcar los plazos a la agenda — 15 min
  - **Cierre:** comprobante con los 2 inscritos + plazos cargados en la agenda (falta solo el comprobante en el vault y los plazos en la agenda).

- [ ] **E2 — Enviar el TCC a Sol para lectura** · 1 pom · Emilia · M-B1
  - [ ] E2.1 Mandar el artículo con el listado de referencias por tópico — 25 min · `transcripción 00:32:40, 00:37:23`
  - **Cierre:** Sol tiene el material para leer.
  - **Dependencia:** depende de A1 (terminar y subir el trabajo) del [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes Telegram]] — se coordina, no se duplica.

- [ ] **E3 — Conversar con Kiki sobre el reparto de honorarios por etapas** · 2 pom · Emilia · M-B5
  - [ ] E3.1 Preparar el planteo: qué etapa vale qué y por qué el proyecto no puede seguir pesando 40% — 25 min · `transcripción 00:20:16-00:20:32, 00:53:00-00:53:30`
  - [ ] E3.2 Reunión de trabajo con Kiki y registro del criterio acordado — 25 min
  - **Cierre:** criterio de reparto por etapas anotado por escrito y compartido con Sol.

- [ ] **E4 — Fijar el criterio de estilo de la entrega** · 1 pom · Emilia + Sol · M-B3
  - [ ] E4.1 Anotar la regla de entrega: croquis + variación leve de perspectiva, sin render realista ni recorte repetido — 25 min · `transcripción 00:52:31-00:52:43`
  - **Cierre:** regla escrita que se puede pasar a cualquier entrega.

### F. Sol

- [ ] **F1 — Pagar la inscripción y pasar los links de la convocatoria** · 2 pom · Sol · M-B1 · **CERRADO 19/10** (inscripción hecha)
  - [x] F1.1 Pagar la inscripción con la tarjeta — 25 min · `transcripción 00:55:33` ("yo voy a pagar porque tengo que poner la tarjeta")
  - [ ] F1.2 Reenviar los links y el comprobante a Emilia — 15 min
  - **Cierre:** comprobante en manos de Emilia para completar E1.
  - **Nota:** la cifra del resumen es €175; en la transcripción se nombra "175 dólares por equipo" (00:14:00) → queda por confirmar contra la convocatoria si hace falta (pregunta 1).

- [ ] **F2 — Traducir las bases a una lista de tareas para Emilia** · 2 pom · Sol · M-B2
  - [ ] F2.1 Volcar los requisitos del concurso como checklist con responsable — 25 min · `resumen ts 3543` + `transcripción 00:12:33-00:13:00, 00:59:25`
  - [ ] F2.2 Enviar la lista y acordar en la llamada del lunes qué falta — 20 min
  - **Cierre:** checklist de entregables enviada, con responsable y fecha por ítem.

- [ ] **F3 — Armar el procedimiento de entrega protegida (PDF → imagen de resolución limitada)** · 4 pom · Sol · M-B4
  - [ ] F3.1 Definir los criterios de la imagen entregable (formato, píxeles, qué se ve y qué no) — 25 min · `transcripción 00:26:32-00:26:48, 00:54:00`
  - [ ] F3.2 Construir el paso a paso local (sin subir el plano a un conversor online) — 50 min · `transcripción 00:26:48-00:27:15` (la alternativa iLovePDF en la nube queda descartada)
  - [ ] F3.3 Probarlo con 1 plano real del estudio — 25 min · `transcripción 00:25:23-00:25:34`
  - [ ] F3.4 Documentarlo como ficha de estudio — 25 min
  - **Cierre:** 1 PDF convertido en imagen plana no ampliable + ficha con el procedimiento.

- [ ] **F4 — Nota de honorarios por propiedad intelectual + tokenización de diseños** · 5 pom · Sol · M-B5
  - [ ] F4.1 Relevar cómo se cobran hoy y dónde se rompe el modelo por m² — 50 min · `transcripción 00:56:00-00:57:40`
  - [ ] F4.2 Modelar la licencia limitada (ej. 10 usos únicos) como unidad de valor — 50 min · `transcripción 00:54:41-00:55:16`
  - [ ] F4.3 Contrastar con el marco que ya estudia el socio (tokenización de activos inmobiliarios) — 25 min · `transcripción 00:29:00-00:29:18`
  - [ ] F4.4 Escribir la nota con 3 opciones de cobro y su dificultad de aplicación — 25 min
  - [ ] F4.5 Compartir la nota con Emilia y Kiki como insumo de E3 — 15 min
  - **Cierre:** nota de 1-2 carillas con 3 opciones y una recomendación.

- [ ] **F5 — Armar el flujo Rhino + ComfyUI con estilo propio** · 4 pom · Sol + Emilia · M-B3
  - [ ] F5.1 Definir el encadenamiento Rhino → viewport ComfyUI → imagen y video — 25 min · `transcripción 00:43:07-00:43:34`
  - [ ] F5.2 Probar el flujo sobre un caso real del estudio — 50 min
  - [ ] F5.3 Aplicar el criterio de estilo propio (E4) y descartar el look "IA notoria" — 25 min · `transcripción 00:51:04-00:51:14`
  - [ ] F5.4 Guardar los parámetros como preset reutilizable — 25 min
  - **Cierre:** 1 entrega con sello propio, reproducible desde los presets.

- [ ] **F8 — Dejar el flujo documentado para que el que venga después tenga el trabajo resuelto** · 2 pom · Sol · M-B3
  - [ ] F8.1 Escribir la secuencia de trabajo como reglas (qué va antes, qué se revisa, qué se entrega) — 50 min · `transcripción 00:48:51-00:49:48`
  - [ ] F8.2 Dejar el crudo y los links de referencia accesibles — 25 min · `transcripción 00:49:20-00:49:40`
  - **Cierre:** documento de reglas + crudo accesible.

### G. Ambos

- [ ] **G1 — Definir los dos problemas que la propuesta tiene que resolver** · 2 pom · Emilia + Sol · M-B2
  - [ ] G1.1 Formular el problema del exceso de turismo en la plaza — 25 min · `resumen ts 300` + `transcripción 00:05:00-00:06:14`
  - [ ] G1.2 Formular el problema del desplazamiento de los vecinos y el vínculo entre ambos mundos — 25 min · `transcripción 00:06:14`
  - **Cierre:** 2 enunciados de problema escritos, con el requisito de "no tapar ni impedir la vista de la Sagrada Família" incluido.

- [ ] **G2 — Repasar las bases y fijar la lista de entregables** · 2 pom · Emilia + Sol · M-B2
  - [ ] G2.1 Leer juntos los requisitos técnicos (texto→imagen, edición de imágenes, video, 3D desde imágenes, modelo IA de la Fundación) — 25 min · `transcripción 00:12:33-00:13:00`
  - [ ] G2.2 Marcar el modelo de IA de la Fundación: qué acceso exige y qué se entrega — 25 min
  - **Cierre:** la lista de entregables de F2 queda cerrada con Emilia.

- [ ] **G3 — Jornada de trabajo del concurso los domingos** · 4 pom c/u · Emilia + Sol · M-B3
  - [ ] G3.1 Cerrar la agenda del domingo con el entregable del día — 25 min · `transcripción 00:13:17-00:13:42` ("va a obligar a usarlo en algo")
  - [ ] G3.2 Preparar el material de arranque de la jornada — 25 min
  - [ ] G3.3 Guardar el avance en el vault al cerrar cada jornada — 25 min
  - **Cierre:** 1 jornada hecha con entregable por sesión, registrada en `raw/sessions/`.

## 4. MILESTONES y OKRs

### Milestones (Go/No-Go)

- [ ] **M-B1 Inscripción pagada y registrada** (cerrado 19/10): Sol + Emilia inscriptos. Go/No-Go: sin inscripción no hay bases firmadas.
- [ ] **M-B2 Bases → checklist de entregables** (mar 20/10): 2 problemas formulados + requisitos técnicos leídos + lista con responsable y fecha.
- [ ] **M-B3 Flujo Rhino + ComfyUI con estilo propio** (jue 22/10): 1 entrega con sello propio reproducible + reglas de trabajo escritas.
- [ ] **M-B4 Entrega protegida documentada** (vie 23/10): 1 PDF convertido en imagen plana no ampliable + ficha del procedimiento (el formato JPG/PNG de resolución limitada es el criterio acordado, `transcripción 00:25:23`).
- [ ] **M-B5 Nota de honorarios por propiedad intelectual** (vie 23/10): 3 opciones de cobro + criterio de escasez + insumo compartido con Emilia y Kiki.
- [ ] **M-B6 Entrega del concurso** (mié 16/12/2026): entregables del concurso cerrados y archivos subidos a la plataforma. Depende del checklist de M-B2 y del flujo de M-B3.

### Goals / OKRs

- [ ] **Objetivo interno de la línea (resumen ts 2581):** base de conocimiento del estudio que sirva para entrenar modelos propios que capturen el estilo del arquitecto → tareas F5, F8, G3.
- [ ] **KR de control:** 1 card de Leantime por tarea con `planHours` = 0,42 h por pomodoro; 1 entregable verificable por milestone (comprobante, checklist, imagen no ampliable, entrega con estilo propio, nota).

## 5. Carga a Leantime (plan listo — pendiente de "s")

> MCP Leantime instalado localmente pero sin tools expuestas en esta sesión → carga manual (15 min, [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] al lado). No se ejecuta nada sin el visto bueno de Sol.

**Tablero destino (decidido 19/10):** **proyecto Leantime propio** `Proyecto Pi — Concurso Gaudí Nexus` — este carril es línea propia del estudio (fuera del contrato Studio OS × Emilia), así que se separa del proyecto 4 (`O.S_ARQ-Emi`). Emilia es miembro del proyecto 4, así que hay que invitarla también al nuevo proyecto. **Criterio de separación:** todo lo que se factura dentro del contrato va al proyecto 4; el concurso se registra aparte con sus horas.

**Sprint:** `S1 Bases + primer flujo (19/10–23/10)` · **Columnas:** Backlog → Make-ready → Sprint actual → En curso → Revisión → Bloqueado ⚠️ → Hecho ✓.

**Listas (cards) a crear — 13 cards:**

| # | Card | Dueño | Subtasks | Pom | Milestone | Columna inicial |
|---|---|---|---|---|---|---|
| 1 | Inscribirse en el concurso con los datos de los dos | Emilia | E1.1-E1.3 | 3 | M-B1 | Sprint actual |
| 2 | Pagar inscripción y pasar links | Sol | F1.1-F1.2 | 2 | M-B1 | Sprint actual |
| 3 | Enviar el TCC a Sol | Emilia | E2.1 | 1 | M-B1 | Make-ready |
| 4 | Traducir bases a lista de tareas | Sol | F2.1-F2.2 | 2 | M-B2 | Sprint actual |
| 5 | Repasar bases y fijar entregables | Ambos | G2.1-G2.2 | 2 | M-B2 | Sprint actual |
| 6 | Definir los 2 problemas del concurso | Ambos | G1.1-G1.2 | 2 | M-B2 | Sprint actual |
| 7 | Flujo Rhino + ComfyUI con estilo propio | Sol+Emilia | F5.1-F5.4 | 4 | M-B3 | Make-ready |
| 8 | Criterio de estilo de la entrega | Emilia+Sol | E4.1 | 1 | M-B3 | Sprint actual |
| 9 | Flujo documentado (reglas + crudo) | Sol | F8.1-F8.2 | 2 | M-B3 | Backlog |
| 10 | Procedimiento de entrega protegida (PDF→imagen) | Sol | F3.1-F3.4 | 4 | M-B4 | Make-ready |
| 11 | Nota de honorarios por PI + tokenización | Sol | F4.1-F4.5 | 5 | M-B5 | Backlog |
| 12 | Conversación con Kiki sobre reparto de honorarios | Emilia | E3.1-E3.2 | 2 | M-B5 | Backlog |
| 13 | Jornada dominical del concurso | Ambos | G3.1-G3.3 | 4 | M-B3 | Backlog |

**Orden de carga (15 min):** 1) crear el proyecto + invitar a Emilia · 2) crear sprint `S1` y los milestones M-B1 a M-B5 (Goal por milestone a mano en la UI: la API no expone Goals) · 3) cargar las 13 cards con subtareas y `planHours` · 4) asentar la sesión en `log.md`.

## 6. Preguntas (para Emilia / Sol)

1. **¿Cuál es la moneda y el alcance de la inscripción?** El resumen dice €175 y la transcripción dice "175 dólares por equipo" (00:14:00) → confirmar contra la convocatoria. *(La inscripción ya está hecha desde el 19/10; el dato queda para el comprobante.)*
2. **¿Quiénes son los hasta 4 inscritos y qué datos exactos pide la plataforma?** (00:55:47-00:56:00). *(Ya están inscriptos Sol + Emilia; falta definir si suman a alguien más.)*
3. **¿Cuál es el "martes 18:30"** que quedó anotado en la otra reunión del 16/10 (00:59:16)? La fecha de entrega ya está confirmada: **16/12**.
4. **¿Qué exige el "modelo IA entrenado con los artículos de la Fundación Antoni Gaudí"**: acceso al modelo, uso del material o solo mención? (00:12:48).
5. **~~¿El carril del concurso vive en un proyecto Leantime propio o dentro del proyecto 4?~~** → **Resuelto 19/10: proyecto Leantime propio** `Proyecto Pi — Concurso Gaudí Nexus`, separado del contrato Studio OS × Emilia.
6. **¿Kiki es colega del Colegio de Arquitectos, asesor o cliente?** El rol exacto define qué se puede negociar en E3 (00:20:16-00:20:32).
7. **¿El premio de 10.000 € que figura en el resumen se confirma contra la convocatoria?** (resumen ts 20) — queda pendiente de verificación documental.
8. **¿La línea de tokenización se abre como investigación propia con el socio** (posgrado en tokenización de activos inmobiliarios iniciado en el mes, 00:29:00-00:29:18) o se mantiene como exploración interna del plan?

## 7. Fuentes

- [[raw/reuniones/2026-10-16_emilia-proyectopi_193639289|Transcripción 16/10 19:31 — "Concurso Gaudí Nexus"]] (592 turnos; `## Resumen` + `## Transcripcion`).
- [[raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct|Sesión 19/10 — import 3 reuniones 16/10 desde Fathom Proyecto Pi]].
- [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04 ComfyUI]] · [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|MVP_05 Rhino MCP]].
- [[specs/261019-plan-agentes-telegram-agenda-emilia|Plan agentes Telegram + agenda + ComfyUI (misma tanda)]] · [[specs/261013-plan-cierre-mes1-calculadora-emilia|plan cierre Mes 1]] (convenciones de Leantime y Goals).
- [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] (Kanban + LPS, PPC, DoD, WIP ≤ 2, pomodoro ≤ 25 min).
