---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [reunion, agenda, fuentes, agentes-telegram, cad, comfy, leantime, estudio, indice]
---

# Ítem de la reunión — miércoles 21/10 (13:00) · qué mirar de cada tema

Un solo documento para recorrer los temas: por cada uno, **las sesiones trabajadas**, **los .md creados** y **los dashboards**. Al final, los 3 pendientes que bloquean a Emilia.

Los dashboards se abren con doble clic (son HTML autocontenidos: se abren en el navegador, sin servidor).

---

## 1. Fuentes — corpus AI×Gaudí (31 PDF → 32 fichas)

**Sesiones trabajadas**
- `raw/sessions/2026-10-13-sesion-baudrillard-pdf-pipeline.md` — el piloto del pipeline de PDF (Baudrillard)
- `raw/sessions/2026-10-20-sesion-procesado-pdfs-gaudi.md` — Gate 0 v2 sobre los 31 PDF + el plan de la revisión
- `raw/sessions/2026-10-21-sesion-fuentes-contexto-chatgpt.md` — cómo el corpus llega a ser contexto de trabajo de Emilia
- `raw/sessions/2026-09-27-mvp_02-fuentes.md` · `2026-09-28-sesion-fuentes-wikilinks.md` · `2026-10-09-sesion-fuentes-agentes-grafo.md` · `2026-10-16-sesion-dashboard-vault-fuentes.md` — la línea de fichas, wikilinks y grafo

**.md creados**
- `raw/pdf/00-index.md` — índice de las 32 fichas
- `raw/pdf/2026-10-20-<slug>-ficha.md` — 32 fichas (metadata, índice, stats, figuras con página)
- `raw/pdf/2026-10-20-<slug>-transcripcion.md` — 31 transcripciones (texto por página, con aviso de copyright)
- `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` — el plan de la revisión (4 gates, 15 tareas, 7 riesgos)
- `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` — la forma de compartirlo (proyecto de ChatGPT + Drive, o un solo Doc compartido)

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-vault.html` — grafo VR de las fuentes y el vault
- `scripts/grafo-yt-vr.html` — el grafo navegable (filtro por `path: wiki/fuentes`)

**Estado**: Gate 0 v2 **hecho** (31 PDF → 32 fichas + 31 transcripciones, 1.062 páginas, ~479.000 palabras, 116 MB en `activos/`). Faltan los gates 1-3 (sherlock → contenidos → wiki) y **decidir el soporte del contexto compartido** (es la pregunta 6 del plan).

---

## 2. Agentes Telegram — el bot de agenda (n8n)

**Sesiones trabajadas**
- `raw/sessions/2026-10-08-sesion-n8n-fathom-agenda.md` — el diseño del nodo de agenda
- `raw/sessions/2026-10-13-sesion-mvp06-agente-voz.md` — el agente de voz (MVP 06)
- `raw/sessions/2026-10-14-sesion-router-v2-inbox.md` — el router único del bot
- `raw/sessions/2026-10-19-sesion-guion-agente-agenda-emilia.md` — el guion de la sesión
- `raw/sessions/2026-10-20-sesion-agenda-emilia-cal-com-n8n.md` — Cal.com de Emilia + clones + pruebas
- `raw/sessions/2026-10-21-sesion-flujo-propio-emilia.md` — **Emilia con su propio flujo**

**.md creados**
- `specs/261019-plan-agentes-telegram-agenda-emilia.md` — el plan (20 cards + 52 subtasks en Leantime)
- `proyectos/MVP_06-agente-voz/01-spec-mvp_06.md` · `03-log-mvp_06.md` · `documentacion/` (4 fichas: credenciales, manual de uso, onboarding de perfiles, referencia del workflow)
- `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` — el mapa técnico del stack
- `proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21.md` — el plan de mañana
- `proyectos/STUDIO_OS-Emilia/documentacion/que-le-pedimos-a-emilia-2026-10-21.md` — los datos a pedirle
- `proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia.md` · `playbook-os-emilia-n8n.md` · `resumen-flujo-{router,voz,agenda-sub,fathom,set01}.md`

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-estudio-os.html` — panorama del estudio

**Estado**: el bot funciona de punta a punta y **cada persona tiene su flujo** (Sol: `Gpd6NHB4HQdU7ary` · Emilia: `Fa2AlIDqUntSWMrw` · el despachador `Msh31moofBKBwZId` reparte por `chat_id`; los subagentes de agenda: `ygdjqRfXpxKMFWEN` y `2JogeOoT3Wjq2ncH`). En Cal.com de Emilia: 3 tipos de reunión (`7563141`/`7563142`/`7563143`) + schedule 24/7. **Falta**: cargar su `chat_id` real (2 lugares) y la dirección del estudio.

---

## 3. CAD / SET — AutoCAD (MVP 02)

**Sesiones trabajadas**
- `raw/sessions/2026-10-05-sesion-set02-gest-dgiur-uso.md` — SET_02 (gestión de DWG de uso)
- `raw/sessions/2026-10-13-sesion-set01-replanteo.md` — el replanteo de SET_01
- `raw/sessions/2026-10-16-sesion-set01-playbooks-adr.md` — los playbooks y el ADR de SET_01
- `raw/sessions/2026-10-16-sesion-cocina-tagle-set03.md` — SET_03 (arquitectura de cocina)
- `raw/sessions/2026-10-20-sesion-rep-araoz-horizontalizacion.md` · `2026-10-20-sesion-simb-loc-id-v2.md` — laFUENTE y el símbolo de localisation
- `raw/sessions/2026-10-21-sesion-dashboard-autocad-v2.md` — **dashboard v2** (el de esta reunión)

**.md creados**
- `proyectos/MVP_02-autocad-standards/00-filo-mvp_02.md` · `01-spec-mvp_02.md` · `02-ft-mvp_02.md` · `03-log-mvp_02.md` (19 KB) · `03-adr-SET_01.md` · `PLAN-implementacion-MVP_02.md` (18 KB)
- `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/` — `01-spec-SET_01.md` (25 KB) + `docs/` (7 fichas: bloques, cuadros, configuración, planillas) + `lisp/` (4 fichas) + `playbooks/` (**PB-01** informe · **PB-02** replanteo desde 0)
- `proyectos/MVP_02-autocad-standards/SET_02-GEST_DGIUR_USO/01-spec-SET_02.md` (41 KB) · `SET_03-ARQ-COC/01-spec-SET_03.md`
- `proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md` (13 KB) — la revisión del día 22
- `proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano.md` (16 KB)

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html` — **el dashboard v2** (50 KB): el trabajo de AutoCAD del estudio en una pantalla

**Estado**: SET_01 replanteado con 2 playbooks operativos, SET_02 y SET_03 especificados, dashboard v2 actualizado. **Es el tema de la revisión del 22/10.**

---

## 4. Comfy — generación de imagen + LoRA rhino-to-image

**Sesiones trabajadas**
- `raw/sessions/2026-09-09-sesion-pm-comfyui-plan-semanal.md` — el plan semanal
- `raw/sessions/2026-10-08-sesion-comfyui-plan-tests-bat-fix.md` · `2026-10-08-sesion-wf01-corridas-ipadapter.md` — la batería de tests
- `raw/sessions/2026-10-13-sesion-comfyui-demo-manana.md` — la demo
- `raw/sessions/2026-10-16-sesion-comfyui-bateria-dashboard-emilia.md` — la batería y el dashboard
- `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` — **la LoRA rhino-to-image** (FLUX.2 klein 9B)

**.md creados**
- `proyectos/MVP_04-comfyui-arquitectura/` — `00-filo` · `01-spec` · `02-ft` · `03-log` · `INDICE-RENDERS.md` (29 KB) · `modelos-recomendados.md` · `extraccion-material-curso-ai-gaudi.md` · `evolucion-asistente-estudio.md` · `PLANS/2026-10-08-plan-tests-24h.md` (36 KB)
- `proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/` — el workflow de ControlNet (ADR-001, logs, nodos)
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/` — el workflow Rhino→imagen + sus 3 prompts
- `proyectos/MVP_04.02-comfyui-arquitectura/` — `WF-01` a `WF-06` (planta ilustrada, inpainting de ventanas, serie de controles, txt2img, img2img croquis, inpaint/outpaint) + `PLANS/PLAN-F1-F8-lora-inpaint-outpaint.md`
- `proyectos/MVP_01-dibujo_ia/` — el MVP de dibujo con IA (n_01 local, n_02 con MCP)
- `proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp.md`

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html` (43 KB) — los renders y los flujos

**Estado**: 3 modelos con luz cálida, WF-03 (serie de controles) funcionando, la LoRA rhino-to-image analizada y documentada, el material del curso AI×Gaudí extraído.

---

## 5. Leantime — el tablero (Fathom → specs → tablero)

**Sesiones trabajadas**
- `raw/sessions/2026-09-28-sesion-alta-emilia-leantime.md` · `2026-10-09-sesion-alta-emilia-leantime.md` — el alta de Emilia
- `raw/sessions/2026-10-05-sesion-fix-mcp-leantime.md` — el MCP roto y su arreglo
- `raw/sessions/2026-10-19-sesion-fathom-pm-tareas-emilia-16oct.md` — el PM de las 3 reuniones del 16/10
- `raw/sessions/2026-10-20-sesion-registro-horas-leantime.md` — **el registro de horas**

**.md creados**
- `specs/261019-plan-agentes-telegram-agenda-emilia.md` · `specs/261019-plan-concurso-gaudi-nexus-ia.md` — los 2 planes
- `scripts/leantime_registrar_horas.py` + `_notas.md` — el cliente de horas (timesheets)
- `wiki/glosario/software/leantime.md` — la API JSON-RPC documentada (+ la sección de horas)
- `raw/reuniones/leantime-carga-261019-estado.json` — el estado de la carga

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-mes1-emilia.html` (32 KB) — el cierre del mes 1

**Estado**: 2 planes cargados (proyecto 4 `O.S_ARQ-Emi` sprint 27 con 20 cards + 52 subtasks · proyecto 6 `Proyecto Pi - Concurso Gaudi Nexus` sprint 28 con 13 cards + 33 subtasks = **33 cards, 85 subtasks, 75,11 h**). **15 h registradas** (8 h el lunes, 4 h el martes, 3 h el miércoles). Ítem nuevo para el corpus: card `589` + 8 subtareas.

---

## 6. Estudio — propuestas y comercial

**Sesiones trabajadas**
- `raw/sessions/2026-10-13-sesion-cierre-mes1-emilia.md` — el cierre del mes 1
- `raw/sessions/2026-10-16-sesion-mes1-presentacion-emilia.md` — la presentación de cierre
- `raw/sessions/2026-10-20-sesion-procesado-pdfs-gaudi.md` (la parte de curso) · `2026-10-21-sesion-dashboard-autocad-v2.md`

**.md creados**
- `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md` (16 KB) · `03-cuestionario-plan-studio-os.md`
- `proyectos/STUDIO_OS-Emilia/presentacion/` — `00-presentacion-studio-os.md` · `01-guion-presentacion.md` · `02-anexo-sprint.md` · `05-propuesta-comercial-viernes.md` · `06-dashboard-cierre-mes1.md` · `07-revision-autocad-2026-10-22.md` · `08-propuesta-mes2-cad-urbano.md`
- `proyectos/STUDIO_OS-Emilia/presentacion/diagramas/` — 3 diagramas editables (anillo trimestral, ROI, flujo del vault)
- `proyectos/STUDIO_OS-Emilia/legal/mod-contrato.md` · `README.md`

**Dashboards**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-estudio-os.html` (22 KB)
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-mes1-emilia.html` (32 KB)

**Estado**: la propuesta comercial del viernes (`05`) y la del mes 2 de CAD urbano (`08`) están escritas; la revisión del 22/10 tiene su documento (`07`).

---

## 7. Los 3 pendientes que bloquean a Emilia (13:00)

| # | Qué | Dónde | Quién |
|---|---|---|---|
| 1 | Cargar su **`chat_id` real** (placeholder `999999999`) | 2 lugares: Router `YWpuV5p0vCDTbIHz` (regla 2 → `rightValue`) y `Fa2AlIDqUntSWMrw` (`Detectar Entrada Emilia` → `PERMITIDO`) → **publicar** | Sol (sale de que ella mande un mensaje) |
| 2 | Cargar la **dirección del estudio** | Cal.com → event type `7563141` → Location → Address | Sol |
| 3 | Que comparta su **calendario** con `proyectopi.31416@gmail.com` | Google Calendar → compartir | Emilia |

Y la pestaña de **ChatGPT** para el tema 1: `chatgpt.com` → Settings → **Plugins** → **Google Drive** → conectar → proyecto "AI×Gaudí" → *Add source* → link de la carpeta. Detalle en [[proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia]].

---

## 8. Orden sugerido de la reunión (60 min)

| Min | Tema | Documento |
|---|---|---|
| 0-5 | Contexto: qué se hizo desde el 13/10 | este documento |
| 5-20 | **Fuentes**: el corpus y cómo lo comparte ella | `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` + `fuentes-contexto-chatgpt-emilia.md` + `dashboard-vault.html` |
| 20-35 | **Agentes Telegram**: el bot de Emilia | `plan-minimo-sesion-2026-10-21.md` + `que-le-pedimos-a-emilia-2026-10-21.md` + prueba en vivo |
| 35-50 | **CAD / SET**: el dashboard v2 | `07-revision-autocad-2026-10-22.md` + `dashboard-autocad.html` |
| 50-57 | **Comfy**: la LoRA y los renders | `dashboard-comfy.html` + la sesión de la LoRA |
| 57-60 | **Leantime**: el tablero y las horas | `dashboard-mes1-emilia.html` + card `589` |
