---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-19
ultima_actualizacion: 2026-10-19
estado: borrador
tags: [agentes-telegram, agenda, cal-com, google-calendar, comfyui, biblioteca, pomodoros, leantime, studio-os]
idioma: es
---

# Agentes Telegram + agenda de Emilia + ComfyUI — OS Emilia

> Origen: reunión del 16/10/2026 20:33 AR "OS Emilia: agentes de Telegram + ComfyUI" (720 turnos), importada de la cuenta Fathom Proyecto Pi → [[raw/reuniones/2026-10-16_emilia-proyectopi_193660891|transcript 193660891]]. Contexto de import: [[raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct|sesión import 19/10]]. La API de Fathom devuelve `action_items` vacío para esta reunión: cada tarea de este plan sale del `## Resumen` (sección Próximos pasos) o del `## Transcripcion` completo, con el timestamp de origen marcado.
>
> Relacionado: [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso Gaudí Nexus]] (misma tanda, tema hermano) · [[specs/261016-plan-unificado-studio-os-quickwins|plan unificado quick wins]] (QW1-QW8 + Mes 2 S1-S4) · [[specs/261013-plan-fuentes-emilia-inbox|plan inbox de fuentes]] (§9-11) · [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n OS Emilia v2.0]] · [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]].

## 1. SPEC

### 1.1 Objetivo

Cerrar la configuración del sistema en el lado de Emilia: que su agente de Telegram catalogue los enlaces que ella encuentra, que el bot de agenda funcione con **su** cal.com y **su** Google Calendar, y que ella sepa elegir modelos en ComfyUI. Cada tarea cabe en un pomodoro de 25 minutos y se sube a Leantime como card con subtareas verificables.

### 1.2 Lo que la reunión dejó en pie

| Pieza | Estado al 16/10 | Evidencia |
|---|---|---|
| Grupo de enlaces con agente IA → Sheet | Operativo en demo | Transcripción 00:06:14-00:07:14 (fila real en la planilla: título, tipo, contenido, nota) |
| Emilia dentro del grupo + ID leído | Hecho en la reunión | Transcripción 00:05:31-00:05:58 + 00:22:41-00:22:57 |
| Bot `OS.emi-pi` respondiendo a Emilia | A la espera del mensaje de activación | Resumen (ts 1487) + transcripción 00:24:47 / 00:25:33 |
| cal.com de Emilia conectada | Falta conectar (la credencial ya está del lado Sol) | Resumen (ts 1831) + transcripción 00:30:31 / 00:32:00 |
| Google Calendar de Emilia | Pendiente presencial (clave desde su mail) | Transcripción 00:32:05-00:32:26 |
| Flujo de investigación en 3 etapas (raw → Obsidian → wiki) | Armado y en uso por Sol | Resumen (ts 2565) + transcripción 00:43:00-00:44:03 |
| Biblioteca de libros/revistas | Sin sistema; Emilia pide copia de su carpeta | Transcripción 00:39:12 / 00:50:42 |
| Modelos ComfyUI (luz cálida vs naranja saturado) | Emilia empieza a elegir modelo | Transcripción 00:56:50 / 00:58:16-00:58:38 |

### 1.3 Alcance

- Dentro: tareas con dueño y criterio de cierre que se pueden verificar esta semana (19/10 → 25/10).
- Fuera (se mantiene vivo en su propio plan): Fathom Core 07:00, worker de fuentes en nube ([[specs/261016-worker-sherlock-fuentes|worker sherlock-fuentes]]), Sheet `Fuentes-Inbox` como cola, instalación presencial ya especificada en [[specs/261013-plan-fuentes-emilia-inbox|plan inbox §11]] (se marca, no se duplica).
- Fuera de esta tanda: la reunión del 16/10 18:34 (obra y flujo CAD) y la del 16/10 19:31 (concurso), que van en [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso]].

### 1.4 Criterio de cierre del plan

Los tres flujos quedan en manos de Emilia desde su celu con fricción cero (1 mensaje), el bot agenda con sus dos calendarios, y existe un método de catalogación escrito por ella. Con eso Emilia opera el sistema y Sol conserva la curaduría ([[proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n|playbook OS Emilia v2.0]]).

## 2. PLAN semanal (Lun 19/10 → Dom 25/10)

Carga por persona y día en pomodoros de 25 minutos (máx. 16 por persona por día, WIP máx. 2 en curso — [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]]).

| Día | Foco | Emilia (pom) | Sol (pom) | Hito del día |
|---|---|---|---|---|
| **Lun 19/10** | Entrega del curso + 1er bloque de fotos + llamada corta | 9 | 6 | A1 cierra + D1 (llamada 30 min) |
| **Mar 20/10** | Identidad en el Router + cal.com de Emilia + inscripción | 7 | 7 | C2 + C1 + F1 |
| **Mié 21/10** | **Cita presencial 13:00** — credencial de Calendar + método + stack en su PC | 11 | 12 | D2 + M-A2 |
| **Jue 22/10** | Modelos ComfyUI + biblioteca + flujo de libros | 8 | 12 | M-A3 |
| **Vie 23/10** | IP/entrega + modelo de honorarios + agente semanal | 3 | 15 | M-A4 |
| **Dom 25/10** | Jornada del concurso (carril del plan hermano) | 4 | 4 | M-B1 (plan concurso) |

Totales: Emilia 42 pomodoros (≈17,5 h) · Sol 56 pomodoros (≈23 h) — el ritmo trimestral vigente es de 6 pomodoros/día de capacidad contractual, y la carga extra corresponde a la línea propia del estudio (concurso) más la cita presencial.

Hitos de la semana: **M-A1** curso entregado + chat compartido (lun-mar) · **M-A2** agenda de Emilia viva con sus dos calendarios (mié 21/10) · **M-A3** método de catalogación + biblioteca (jue 22/10) · **M-A4** modelos Comfy con luz cálida + agente semanal cerrado (vie 23/10).

## 3. TASKS

> Cada línea dice de dónde sale. `resumen ts N` = sección Próximos pasos del resumen de Fathom (segundo en la URL). `transcripción mm:ss` = turno literal. Alineación: cada task cita su milestone (M-Ax) y su OKR o queda en `sin-alineacion`.

### A. Emilia · curso, tesis y entrega

- [ ] **A1 — Terminar y entregar el trabajo del curso y compartir el enlace del chat con Pi** · 5 pom · Emilia · M-A1 · Mes 2 S1 (adopción real del sistema)
  - [ ] A1.1 Cerrar el tópico 5 (imágenes + escritura) — 25 min · `transcripción 00:18:00, 00:37:45`
  - [ ] A1.2 Escribir la conclusión — 25 min · `transcripción 00:18:00, 00:39:00`
  - [ ] A1.3 Regenerar el PDF y subirlo a la plataforma — 25 min · `transcripción 00:18:00`
  - [ ] A1.4 Pagar la tasa y escribir la solicitud de prórroga con el motivo — 25 min · `transcripción 00:19:21-00:19:44`
  - [ ] A1.5 Compartir el link del chat con Sol — 10 min · `resumen ts 1292` + `transcripción 00:22:45`
  - **Cierre:** plataforma con la entrega + tasa pagada + solicitud de prórroga escrita + link del chat compartido con Sol.
  - **Criterio:** el link del chat es el mismo que usa el agente de Sol para leer el trabajo (transcripción 00:18:48).

- [ ] **A2 — Consolidar el listado de referencias por tópico en un listado único** · 2 pom · Emilia · M-A1
  - [ ] A2.1 Pedir a la IA el listado unificado sin perder ninguna referencia — 10 min · `transcripción 00:39:00-00:39:08`
  - [ ] A2.2 Chequear que estén todas las citas leídas — 15 min · `transcripción 00:39:17-00:39:24`
  - **Cierre:** listado único pegado + cotejo firmado de que no falta ninguna fuente.

### B. Emilia · su lado del sistema

- [ ] **B1 — Mandar un mensaje al bot `OS.emi-pi` para activar la configuración** · 1 pom · Emilia · M-A2
  - [ ] B1.1 Mensaje al bot y lectura de la respuesta ("hablame en privado…") — 5 min · `resumen ts 1487` + `transcripción 00:24:47, 00:25:20`
  - **Cierre:** el bot responde con el menú de comandos y el `chat_id` de Emilia queda visible para Sol.
  - **Nota:** en la reunión Sol pidió el mensaje "para que se activara y yo pudiera ver" (`transcripción 00:25:33`); el resumen lo deja como próximo paso, así que se verifica al ejecutar.

- [ ] **B2 — Generar la credencial de Google Calendar con su mail** · 1 pom · Emilia + Sol (presencial) · M-A2
  - [ ] B2.1 Emilia autoriza Google Calendar desde la UI de n8n (OAuth2 → Connect con su cuenta) — 20 min · `transcripción 00:32:05`
  - [ ] B2.2 Sol la pega en la tool `leer_calendario` del agente de agenda — 5 min · `transcripción 00:30:42, 00:32:26` + [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-agenda-sub|flujo Agenda Sub TEST]]
  - **Cierre:** el agente de agenda lee el calendario de Emilia y devuelve un slot real.
  - **Guion:** [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §3.1 (P2) y §4.1 (`leer_calendario`).

- [ ] **B3 — Copiar la carpeta de revistas/biblioteca en su propio Drive** · 1 pom · Emilia · M-A3
  - [ ] B3.1 Duplicar la carpeta compartida y verificar que tiene acceso completo — 25 min · `transcripción 00:39:12-00:39:19`
  - **Cierre:** Emilia tiene copia propia y deja de depender del acceso de un tercero.

- [ ] **B4 — Catalogar fotos propias de obras de arquitectura y publicar una** · 4 pom · Emilia · M-A3
  - [ ] B4.1 Elegir 30 fotos (criterio: material propio, sin derechos de terceros) — 25 min · `transcripción 00:44:40-00:44:58`
  - [ ] B4.2 Catalogarlas con tema + lugar + año — 50 min · `transcripción 00:44:52-00:45:00`
  - [ ] B4.3 Escribir el pie de foto de la primera tanda — 25 min
  - [ ] B4.4 Publicar una tanda — 25 min · `transcripción 00:44:54` ("mañana quiero publicar algo")
  - **Cierre:** catálogo de 30 fotos con metadata + 1 publicación hecha.

- [ ] **B5 — Elegir y validar 3 modelos de ComfyUI con luz cálida** · 4 pom · Emilia + Sol · M-A4
  - [ ] B5.1 Listar los modelos disponibles y sus estilos — 25 min · `transcripción 00:56:50-00:57:00`
  - [ ] B5.2 Probar 3 modelos sobre el mismo croquis y comparar — 50 min · `transcripción 00:58:00-00:58:16`
  - [ ] B5.3 Guardar el prompt + modelo ganador como preset — 25 min
  - [ ] B5.4 Escribir una nota de 5 líneas con el criterio de luz elegido — 25 min
  - **Cierre:** 3 comparaciones documentadas + preset guardado con luz cálida (en lugar del naranja saturado que marca los modelos por defecto, `transcripción 00:56:26-00:56:41`).
  - **Contexto:** el LoRA propio de firma (estilo dibujado a mano) viene del carril del 09/10; se retoma en el flujo del concurso ([[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso]] §3 F5).

- [ ] **B6 — Definir el método de catalogación (campos, vocabulario y regla de selección)** · 2 pom · Emilia + Sol · M-A3 · Mes 2 S1
  - [ ] B6.1 Emilia escribe qué campos quiere ver en cada fuente — 25 min · `transcripción 00:08:07-00:08:26, 00:41:32`
  - [ ] B6.2 Definir la regla de selección (sí / no / revisar) y su vocabulario de tags — 25 min · `transcripción 00:43:00-00:44:03`
  - [ ] B6.3 Contrastar con las columnas vivas del Sheet `Fuentes-Inbox` y dejar la diferencia anotada — 25 min
  - **Cierre:** método de una carilla, con la diferencia contra la Sheet anotada para el siguiente ajuste.

- [ ] **B7 — Instalar el stack de trabajo en el PC de Emilia** · 4 pom · Emilia + Sol (presencial mié 21/10) · M-A2
  - [ ] B7.1 Actualizar Obsidian + `git pull` del vault — 25 min · `transcripción 00:42:21`
  - [ ] B7.2 Conectar su ChatGPT al sistema — 25 min · `transcripción 00:21:04`
  - [ ] B7.3 `codex mcp list` con Fathom visible — 25 min
  - [ ] B7.4 1 ficha del vault alimentada por ella con verificación de Sol — 25 min · [[specs/261013-plan-fuentes-emilia-inbox|plan inbox §11]]
  - **Cierre:** la cita del miércoles cierra con Emilia operando sobre su propio vault.
  - **Nota:** tarea ya especificada en [[specs/261013-plan-fuentes-emilia-inbox|plan inbox §11]]; aquí se marca la ejecución, no se duplica la card.

### C. Sol · cableado del sistema

- [ ] **C1 — Conectar la cuenta de cal.com de Emilia al sistema de agenda** · 3 pom · Sol · M-A2
  - [ ] C1.1 Cargar la API key de la cuenta de Emilia — 25 min · `resumen ts 1831` + `transcripción 00:30:31`
  - [ ] C1.2 Crear su `eventType` propio con durations 30/60/120 min — 25 min · `transcripción 00:33:11` + `eventTypeId 7467793` (el de Sol) como referencia
  - [ ] C1.3 Prueba de booking real + link de Meet — 25 min · `transcripción 00:29:03, 00:29:57`
  - **Cierre:** 1 reserva real a nombre de Emilia, con Meet en el mail.
  - **Guion:** [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §3.1 (P1, P3) y §4.1 (las 6 tools de Cal.com).

- [ ] **C1b — Clonar el agente + subflujo de agenda para Emilia y cablear su perfil** · 5 pom · Sol · M-A2
  - [ ] C1b.1 Clonar `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`) → `OS-Studio — Agenda Sub Emilia` y cambiar las 6 credenciales de Cal.com + `leer_calendario` — 50 min
  - [ ] C1b.2 Clonar `OS-Studio — Agent Voz TEST` (`Gpd6NHB4HQdU7ary`) → `OS-Studio — Agent Voz Emilia` y cambiar allowlist, key Redis, tabla Postgres, prompt y `Tool Agenda` — 50 min
  - [ ] C1b.3 Agregar la rama de Emilia en `Route Identidad` del Router con su `chat_id` leído de la ejecución — 25 min
  - [ ] C1b.4 Publicar los 3 workflows (borrador ≠ activo) y correr las 10 pruebas de aceptación — 25 min
  - **Cierre:** los 2 clones activos con perfil Emilia + 1 reserva real creada desde el chat de Emilia.
  - **Guion:** [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §4 (cambios nodo a nodo), §5 (guion de la sesión) y §6 (pruebas).

- [ ] **C2 — Cargar el `chat_id` de Emilia en el Router para que la columna "De" registre `emi`** · 1 pom · Sol · M-A2
  - [ ] C2.1 Leer el `chat_id` desde la ejecución del trigger y pegarlo en el nodo de identidad — 25 min · `transcripción 00:06:38, 00:22:57`
  - **Cierre:** 1 link enviado por Emilia aparece en el Sheet con `De = emi` (columnas Fecha/De/Link/Tipo/Título/Estado/Destino/Nota/Tags, [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-router|flujo Router]]).

- [ ] **C3 — Configurar qué calendario lee el agente y el evento de 60 min con Meet** · 3 pom · Sol · M-A2
  - [ ] C3.1 Definir el calendario de trabajo de Emilia (profesional / personal) — 25 min · `transcripción 00:31:00-00:31:36, 00:33:40-00:34:14`
  - [ ] C3.2 Ajustar el evento 60 min con Meet — 25 min · `transcripción 00:33:13` + §12 de la arquitectura v2.0
  - [ ] C3.3 Verificar que el filtro por `chat_id` deja pasar a Emilia — 25 min
  - **Cierre:** el agente devuelve slots de los calendarios correctos y Emilia ya no cae en el fallback de comandos.

- [ ] **C4 — Compartir el Sheet `Fuentes-Inbox` con Emilia y moverlo a `OS-Emilia/`** · 1 pom · Sol · M-A3
  - [ ] C4.1 Compartir la hoja con el mail de Emilia + moverla a la carpeta `OS-Emilia/` — 25 min · `transcripción 00:06:05-00:06:13` + [[specs/261016-plan-unificado-studio-os-quickwins|plan unificado QW1]]
  - **Cierre:** Emilia abre la hoja desde el celu y ve sus filas.

- [ ] **C5 — Armar el sistema de procesamiento de libros/biblioteca** · 4 pom · Sol + Emilia · M-A3
  - [ ] C5.1 Separar el tema en su propia carpeta (misma lógica que el sistema de Telegram) — 25 min · `transcripción 00:50:42-00:51:05`
  - [ ] C5.2 Definir la ficha por libro (título, tema, índice/glosario, tapa) replicando el modelo de la biblioteca física — 50 min · `transcripción 00:16:03-00:16:33`
  - [ ] C5.3 Definir el pipeline (entrada → crudo → Obsidian → wiki) para material ya digitalizado — 50 min · `resumen ts 2565` + `transcripción 00:51:28-00:51:37`
  - [ ] C5.4 Probar con 1 libro y 1 revista — 25 min
  - **Cierre:** 1 libro procesado de punta a punta con su ficha y su crudo.

- [ ] **C6 — Probar el pipeline con textos sin imágenes (revistas escaneadas)** · 2 pom · Sol · M-A3
  - [ ] C6.1 Corrida con 1 revista escaneada sin imágenes — 25 min · `transcripción 00:39:30-00:39:40`
  - [ ] C6.2 Medir cuánto se automatiza vs. lo que queda curaduría — 25 min
  - **Cierre:** el pipeline rinde con material sin imágenes y el tiempo de revisión queda anotado.

- [ ] **C7 — Decidir el canal de avisos al cliente y dejar la decisión escrita** · 1 pom · Sol · M-A3 · `sin-alineacion` (criterio de estudio)
  - [ ] C7.1 Comparar Telegram propio vs. WhatsApp Business (costo de mensajes salientes) — 25 min · `transcripción 00:36:05-00:36:44`
  - **Cierre:** 1 párrafo con el canal elegido y su costo mensual estimado.

- [ ] **C8 — Cerrar el agente semanal de arquitectura (reporte + aceptar/rechazar + imagen)** · 3 pom · Sol · M-A4
  - [ ] C8.1 Cerrar el informe semanal con el botón de quedarse/rechazar por tema — 50 min · `transcripción 00:14:19-00:15:00`
  - [ ] C8.2 Verificar el worker que toma la imagen y la publica — 25 min · `transcripción 00:15:08-00:15:17`
  - [ ] C8.3 Documentarlo en el playbook — 25 min
  - **Cierre:** el lunes Emilia recibe el reporte con sus 2 botones funcionando.

### D. Ambos · citas

- [ ] **D1 — Llamada corta el lunes 19/10 (30 min)** · 1 pom c/u · Emilia + Sol · M-A1
  - [ ] D1.1 Confirmar la fecha real de entrega del curso — 25 min · `transcripción 00:59:20` + `00:19:15`
  - **Cierre:** fecha de entrega anotada en el plan y en Leantime.

- [ ] **D2 — Cita presencial del miércoles 21/10 13:00: conectar el calendario de Google y cerrar la configuración** · 2 pom c/u · Emilia + Sol · M-A2 · Mes 2 S1
  - [ ] D2.1 Ejecutar B2 (credencial de Calendar) — 25 min · `resumen ts 3543` + `transcripción 00:55:24`
  - [ ] D2.2 Ejecutar C1b (clones de agente + subflujo con perfil Emilia) — 75 min · [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|guion de la sesión]]
  - [ ] D2.3 Revisar qué queda abierto del bot de agenda y de la biblioteca — 25 min
  - **Cierre:** agenda viva con los dos calendarios + lista de lo que sigue con dueño y fecha.
  - **Guion completo (8 bloques, 2 h):** [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §5.

## 4. MILESTONES y OKRs

### Milestones (Go/No-Go)

- [ ] **M-A1 Curso entregado + chat compartido** (lun 19/10 → mar 20/10): entrega subida con tasa pagada + solicitud de prórroga + link del chat con Sol. Sin este milestone, A1-A2 y el ítem de la tesis del plan hermano quedan en espera.
- [ ] **M-A2 Agenda de Emilia viva** (mié 21/10 13:00): bot `OS.emi-pi` respondiendo, cal.com de Emilia con su evento, Calendar de Emilia leída desde su mail, `chat_id` en el Router, clones de agente + subflujo con perfil Emilia publicados. Go/No-Go: 1 reserva real creada desde el chat de Emilia. Guion: [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]].
- [ ] **M-A3 Método de catalogación + biblioteca** (jue 22/10): método escrito por Emilia, copia de la biblioteca en su Drive, Sheet compartido, sistema de libros con 1 libro procesado.
- [ ] **M-A4 Modelos Comfy + agente semanal** (vie 23/10): 3 modelos comparados con luz cálida + preset + agente semanal con botones funcionando.

### Goals / OKRs (trimestre vigente)

- [ ] **O1 Adopción — Emilia opera el sistema desde el celu** (del plan trimestral Mes 2 S1, [[specs/261016-plan-unificado-studio-os-quickwins|plan unificado §6]]): 1 flujo de agenda y 1 de fuentes operados por ella sin asistencia → tareas B1, B2, B6, B7, D2.
- [ ] **O3 Herramientas — un paso más de sistema** (Mes 2 S1): sistema de biblioteca + agente semanal cerrados → tareas C5, C6, C8.
- [ ] **KR de control:** 1 card de Leantime por tarea, con `planHours` = 0,42 h por pomodoro y cierre verificado con evidencia (link, captura o reserva real).

## 5. Carga a Leantime (plan listo — pendiente de "s")

> Estado: MCP Leantime instalado localmente pero sin tools expuestas en esta sesión → carga manual (15 min, [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] al lado). Ninguna carga se ejecuta sin el visto bueno de Sol.

**Tablero destino:** proyecto Leantime `O.S_ARQ-Emi` (id 4, `STUDIO_OS-Emilia`) — es el contrato vivo con Emilia.

**Sprint:** `S1 Agentes + agenda Emilia (19/10–23/10)` · **Columnas (mapa pbk):** Backlog (debe) → Make-ready (puede) → Sprint actual (hará) → En curso → Revisión → Bloqueado ⚠️ → Hecho ✓.

**Listas (cards) a crear — 20 cards**, con `milestoneid` y `planHours` (0,42 h por pomodoro):

| # | Card | Dueño | Subtasks | Pom | Milestone | Columna inicial |
|---|---|---|---|---|---|---|
| 1 | Entregar trabajo del curso + compartir chat (dom 20/10) | Emilia | A1.1-A1.5 | 5 | M-A1 | Sprint actual |
| 2 | Listado de referencias consolidado | Emilia | A2.1-A2.2 | 2 | M-A1 | Sprint actual |
| 3 | Activar bot OS.emi-pi con mensaje | Emilia | B1.1 | 1 | M-A2 | Sprint actual |
| 4 | Credencial de Google Calendar de Emilia | Emilia+Sol | B2.1-B2.2 | 1 | M-A2 | Make-ready |
| 5 | Copia de biblioteca de revistas en su Drive | Emilia | B3.1 | 1 | M-A3 | Sprint actual |
| 6 | Catálogo + publicación de fotos de obras | Emilia | B4.1-B4.4 | 4 | M-A3 | Sprint actual |
| 7 | 3 modelos Comfy con luz cálida | Emilia+Sol | B5.1-B5.4 | 4 | M-A4 | Sprint actual |
| 8 | Método de catalogación acordado | Emilia+Sol | B6.1-B6.3 | 2 | M-A3 | Sprint actual |
| 9 | Stack de trabajo en el PC de Emilia | Emilia+Sol | B7.1-B7.4 | 4 | M-A2 | Make-ready |
| 10 | Conectar cal.com de Emilia | Sol | C1.1-C1.3 | 3 | M-A2 | Sprint actual |
| 10b | Clonar agente + subflujo de agenda con perfil Emilia | Sol | C1b.1-C1b.4 | 5 | M-A2 | Sprint actual |
| 11 | Cargar chat_id de Emilia en el Router | Sol | C2.1 | 1 | M-A2 | Sprint actual |
| 12 | Calendario que lee el agente + evento 60 min | Sol | C3.1-C3.3 | 3 | M-A2 | Make-ready |
| 13 | Compartir Sheet + mover a OS-Emilia/ | Sol | C4.1 | 1 | M-A3 | Backlog |
| 14 | Sistema de procesamiento de libros | Sol+Emilia | C5.1-C5.4 | 4 | M-A3 | Backlog |
| 15 | Prueba con textos sin imágenes | Sol | C6.1-C6.2 | 2 | M-A3 | Backlog |
| 16 | Canal de avisos al cliente (decisión) | Sol | C7.1 | 1 | M-A3 | Backlog |
| 17 | Cerrar agente semanal de arquitectura | Sol | C8.1-C8.3 | 3 | M-A4 | Backlog |
| 18 | Llamada corta lunes 19/10 | Ambos | D1.1 | 1 | M-A1 | Sprint actual |
| 19 | Cita presencial miércoles 21/10 13:00 | Ambos | D2.1-D2.3 | 3 | M-A2 | Sprint actual |

**Orden de carga (15 min):** 1) abrir sprint `S1` · 2) crear los 2 milestones nuevos (M-A2, M-A3) y linkearlos a mano en Goals (la API no expone Goals y Leantime admite 1 milestone por goal — [[specs/261013-plan-cierre-mes1-calculadora-emilia|plan cierre §GOAL]]) · 3) cargar las 20 cards con subtareas y `planHours` · 4) asentar la sesión en `log.md`.

**No se duplica:** la card 9 ya tiene su equivalente en [[specs/261013-plan-fuentes-emilia-inbox|plan inbox §11]] — se deja esa como dueña y esta queda como referencia.

## 6. Preguntas (para Emilia / Sol)

1. **¿Cuál es la fecha real de entrega del trabajo del curso?** La transcripción dice "hasta fin de octubre" (00:19:15) y más tarde aparece un "martes 18:30" (00:59:16) sin aclarar a qué entrega se refiere. De ahí depende M-A1.
2. **¿El bot `OS.emi-pi` es el mismo token que `emiliaospi_bot`** del Router documentado en la arquitectura v2.0, o es un token nuevo? La transcripción los nombra por separado (00:24:38).
3. **¿Qué calendarios debe leer Emilia** y cómo se separa lo profesional de lo personal? (00:31:00-00:34:14). → Se resuelve en la sesión del miércoles: campo *Calendar* de la tool `leer_calendario` (ver [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §3.1 P3 y §8.1).
4. **¿Se abre una cuenta de Telegram propia para los avisos a clientes** (propuesta de Emilia, 00:36:30)? Queda con el costo de WhatsApp Business sobre la mesa.
5. **¿El método de catalogación reemplaza las columnas vivas del Sheet `Fuentes-Inbox`** o conviven? La reunión describe un catálogo más rico (00:08:07) que el de 9 columnas ya implementado.
6. **La copia de la biblioteca de revistas**, ¿la hace Emilia en su Drive o la baja Sol? (00:39:12).
7. **¿La cita del miércoles es presencial en la PC de Emilia?** El plan vigente la tenía prevista (plan inbox §11) y la reunión la confirma para las 13:00 → **confirmada: presencial, miércoles 21/10 13:00**. Guion de 2 h: [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia|config-agente-agenda-emilia]] §5.

## 7. Fuentes

- [[raw/reuniones/2026-10-16_emilia-proyectopi_193660891|Transcripción 16/10 20:33 — "OS Emilia: agentes de Telegram + ComfyUI"]] (720 turnos; `## Resumen` + `## Transcripcion`).
- [[raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct|Sesión 19/10 — import 3 reuniones 16/10 desde Fathom Proyecto Pi]].
- [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia v2.0]] (Router, Voz, Agenda Sub TEST, `leer_calendario`, Sheet `Fuentes-Inbox`).
- [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-router|resumen-flujo-router]] + [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-voz|resumen-flujo-voz]] + [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-agenda-sub|resumen-flujo-agenda-sub]].
- [[proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n|playbook-os-emilia-n8n v2.0]].
- [[specs/261016-plan-unificado-studio-os-quickwins|plan unificado quick wins]] · [[specs/261013-plan-fuentes-emilia-inbox|plan inbox de fuentes]] · [[specs/261013-plan-cierre-mes1-calculadora-emilia|plan cierre Mes 1]].
- [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] (Kanban + LPS, PPC, DoD, WIP ≤ 2, pomodoro ≤ 25 min).
- [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04 ComfyUI]] (flujos y modelos).
