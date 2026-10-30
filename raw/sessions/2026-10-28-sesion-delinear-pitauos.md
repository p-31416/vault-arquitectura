---
tipo: log
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [sesion, pitauos, plan-hermes, arquitectura, mcp, diagnostico, delinear]
---

# Sesión 2026-10-28 — Delineado del sistema pitauOS (lectura de `plan-hermes.md` + diagnóstico del vault)

## Qué se hizo

- **Leí completo** `raw/docs/plan-hermes.md` (1013 líneas): briefing técnico PITAUTECH/pitauOS sobre integración de Hermes Agent con automatización, CAD, modelado 3D, BIM, visualización y documentación de obra.
- **Relevé el estado real del vault** para no proponer en abstracto: `opencode.json` (8 servidores MCP), `proyectos/00-index.md`, `proyectos/MVP_04-comfyui-arquitectura/evolucion-asistente-estudio.md`, `scripts/` (colector de renders, extracción de atributos DWG, puente Rhino), `raw/reports/*.audit.json`, research `2026-10-15-cad-abierto-mcp-opencode`, `wiki/legal/anexo-stack-subencargados.md`.
- **Contrasté el briefing contra lo existente** y delineé el sistema siguiente: 3 piezas (contrato de tarea · registro central · riesgo/HITL), con lo que queda deliberadamente afuera (Hermes, Gradio, Twinmotion, IFC, base de grafos).
- **No escribí en `wiki/`, no ejecuté código, no toqué servicios** — todo lo anterior fue lectura y propuesta (HITL vigente).

## Diagnóstico: el briefing describe en gran parte lo que ya existe

**Confirmado (hecho comprobable en el vault):**

| Pieza del briefing | Estado real | Evidencia |
|---|---|---|
| Capa de integración (MCP) | ✅ 8 MCP conectados: comfyui, n8n (remoto VPS), fathom, fathom-proyectopi, leantime, autodesk-help, autocad, rhino | `opencode.json:3-60` |
| AutoCAD: inspección + auditoría | ✅ existe y produce informes | `scripts/extrae-atributos-dwg.py`, `raw/reports/barcelona-2d.audit.json`, `audit-REP-ARAOZ.copia-trabajo.json` |
| Rhino: inspección + geometría | ✅ puente MCP operativo (puerto 9876) + playbook | `proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp.md`, `scripts/rhino-mcp-server-rhino.py` |
| ComfyUI: submit/watch/collect | ✅ MCP local + índice con metadata (80 renders) | `scripts/indice-renders-comfy.py`, `INDICE-RENDERS.md/.json` |
| Registro de proyecto | ⚠️ parcial y disperso: metadata dentro del PNG, del JSON de auditoría y del markdown | `INDICE-RENDERS.json` + `raw/reports/` + `wiki/` |
| n8n como orquestador de procesos | ✅ autohospedado en VPS + MCP remoto | `opencode.json:12-19`, `wiki/legal/anexo-stack-subencargados.md:17-21` |
| Hermes como eje | ❌ nunca instalado; y el veredicto ya escrito dice que la capacidad está en MCP + contrato + índice | `evolucion-asistente-estudio.md:110-126` |

**Pendiente real (0 implementación, solo research):** IFC/BIM (IfcMCP oficial y Bonsai existen pero no instalados), Twinmotion (sin API local; el MCP remoto de terceros cobra créditos y tarda 5-60 min), ejecución de Grasshopper, interfaz Gradio (capa 3), agente por Telegram (capa 4), contrato común de tareas, registro relacional central, política de riesgo A-D ejecutable.

**Hecho clave del diagnóstico:** el briefing pone a Hermes como pieza central (§4) pero su propio §188 pide prueba de concepto antes de adoptarlo, y el veredicto del vault ya había concluido que *opencode + MCP resuelve el 90%* y que el orden correcto es *índice → interfaz → agente*. El sistema siguiente no es "instalar Hermes": es **el esqueleto que hace que Hermes (o Gradio, o Twinmotion) se enchufe después sin rehacer nada**.

## Delineado del sistema siguiente: Núcleo de Ejecución y Trazabilidad

1. **Contrato de tarea (el sobre).** Un único esquema —`task_id`, `project`, `tool`, `input{file_ref}`, `risk`, `approval`, `requested_by`, `idem_key`— con 4 verbos que mapean a los 4 niveles de riesgo del briefing (§16): `inspect` (A) · `generate` (B) · `modify` (C) · `publish` (D). Implementación: adapter propio + wrapper MCP `run_task` que envuelve cualquier MCP existente, de modo que el heterogéneo (`autocad_*`, `rhino_*`, `comfyui_*`) se vuelve homogéneo. *Por qué:* hoy cada herramienta tiene su propia forma; sin sobre común el registro no se puede llenar.
2. **Registro central (Postgres que ya existe en el VPS).** Tablas `proyecto, archivo, version, tarea, ejecucion, artefacto, relacion, aprobacion` + relaciones del briefing (§11): `derived_from`, `depends_on`, `generated_by`, `validated_by`, `approved_by`, `supersedes`. Relacional primero; grafo solo si aparece el caso que lo justifique (§11:618).
3. **Riesgo y HITL ejecutable.** Mapa herramienta → nivel A/B/C/D. Los niveles C y D dejan la tarea en `awaiting_approval` y exigen aprobación humana (regla que el vault ya aplica como texto en `AGENTS.md`; acá pasa a mecanismo, con evidencia registrada). Imprescindible porque los planos son documento legal (Ley 24.335).

**Fuera de este sistema, a propósito:** Hermes/OpenClaw (son shell; la decisión queda como ADR posterior y el contrato/registro son agnósticos al shell) · Gradio (después del contrato) · Twinmotion (proceso asistido, no automatización) · IFC (falta un IFC real del estudio) · base de grafos · ejecución distribuida.

**MVP de cierre de círculo:** tomar el `audit_dwg` que **ya funciona**, envolverlo en el contrato, escribir su ejecución + artefacto + relación en el registro, y cerrar con el caso del briefing (§11:609-616): cambiar un parámetro → el sistema marca qué auditoría/render queda desactualizado y con qué aprobación hay que rehacerlo.

## Archivos

**Nuevos**
- `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` (este archivo)

**Modificados:** ninguno.

**Leídos (sin cambios):** `raw/docs/plan-hermes.md`, `opencode.json`, `proyectos/00-index.md`, `proyectos/MVP_04-comfyui-arquitectura/evolucion-asistente-estudio.md`, `raw/research/2026-10-15-cad-abierto-mcp-opencode.md`, `wiki/legal/anexo-stack-subencargados.md`, `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md`.

## Análisis cerebro-digital

- **Topics:** pitauOS · plan-hermes · contrato de tarea · registro central · trazabilidad · grafo de dependencias · niveles de riesgo A-D · HITL · Hermes vs OpenClaw · MCP heterogeneous wrappers · índice de renders · auditoría DWG · puente Rhino · IfcOpenShell/IfcMCP · Bonsai · Twinmotion APS · Postgres en VPS · n8n como orquestador.
- **Entidades:** PITAUTECH (encargado técnico) · Estudio de Emilia Pimenta (CLIENTE) · Nous Research / Hermes Agent · Fundación / OpenClaw · opencode · MCP (comfyui, n8n, fathom, leantime, autodesk-help, autocad, rhino) · Contabo VPS (4vCPU/8GB) · Postgres/MySQL/Redis/Qdrant · Leantime 3.12 · Chatwoot 4.12 · ComfyUI local (RX 570 8 GB, DirectML) · AutoCAD · Rhino 8 / Grasshopper · IfcOpenShell · Bonsai · Twinmotion (Epic) · RunPod · Ley 24.335 (planos como instrumento legal).
- **Hechos:** (1) el briefing describe un 40-50% ya construido y lo que falta es el esqueleto, no los motores; (2) el veredicto interno previo ya resolvió que la capacidad vive en MCP + contrato + índice, y que el orden es índice → interfaz → agente; (3) la trazabilidad actual está fragmentada en tres formatos (metadata del PNG, JSON de auditoría, markdown); (4) Twinmotion no tiene API local utilizable y su único MCP disponible es remoto, con créditos y latencia de 5-60 min → no automatizable; (5) el riesgo de este sistema no es técnico sino de gobierno: sin nivel de riesgo explícito, un agente que ejecuta puede tocar un plano que es instrumento contractual.
- **Pendiente de decisión (para el usuario):** nombre y carpeta del proyecto nuevo (`MVP_07-pitauos-nucleo`, el número 05 y 06 están ocupados), alcance del MVP (¿audit_dwg o render ComfyUI como primer flujo por el contrato?), y si el registro arranca en Postgres del VPS o en SQLite local para el MVP.

## Continuación — Vision en 4 decisiones + auditoría Runpod

**Respuestas del usuario (2026-10-28):** (1) "RAMPO" era **Runpod** → el nodo GPU cloud entra al diseño; (2) identidad: **Studio OS como producto** (pitauOS queda interno de PITAUTECH); (3) registro: **híbrido** (Postgres VPS para lo vivo + vault para lo narrativo); (4) primer horizonte: **el caso real como demo**, y el caso elegido es **AIZ** (`proyectos/MVP_05-rhino-mcp/01-AIZ/`).

**Decisiones tomadas en la conversación:**
- **Interfaz:** Telegram como chat con el agente, con **temas** (1 grupo por obra, temas por frente: AutoCAD / Rhino-3D / Render-IA / Obra / Comercial) + **1 canal** broadcast de bitácora + chat privado para aprobaciones. Fathom queda como tronco (reunión → minuta → decisiones → Leantime → vault). Discord queda para **mesa de iteración visual** y **canal de método** (material sensible no sale del Drive/vault). WhatsApp sigue para clientes.
- **Agendado:** se reusa el agente Cal.com que **ya funciona** (3 event types de Emilia + Google Calendar ya conectado, sin OAuth pendiente); regla vigente: el bot solo agenda, nunca desde Google.
- **Notificaciones en 3 capas:** Telegram inmediato (accionable) → digest diario por mail (movimiento + desactualizados + aprobaciones pendientes + costo GPU) → mail al cliente solo en entrega (nivel D, con aprobación).
- **Hermes en el VPS: DECISIÓN DEL USUARIO = arrancar con él** (contenedor en el mismo VPS que n8n/Postgres; esta PC queda como banco de pruebas; nodo GPU = Runpod Secure; un agente del estudio). Hechos verificados en su documentación oficial (imagen oficial, `/opt/data`, gateway 8642/9119/9120, 1-4 GB RAM). Riesgos a atender al instalarlo: el shell Telegram ya existe en n8n; los MCP de AutoCAD/Rhino/ComfyUI son stdio en la PC y no se alcanzan desde el VPS sin envolverlos en HTTP; duplicaría la memoria contra el vault; y 8 GB de RAM no dejan margen. Si se evalúa: PoC de 2 semanas, `--memory=2g`, sin gateway expuesto, con el **mismo contrato**. Ojo de seguridad: en junio 2026 los escáneres entraron a dashboards de Hermes expuestos y plantaron una backdoor SSH → dashboard exige auth en bind no-loopback y solo por Tailscale.
- **Runpod: política endurecida** (auditoría de @sherlock, 29 fuentes oficiales, `raw/research/2026-10-28-runpod-auditoria-pi.md`). Hallazgos que corrigen el vault: **no existe cláusula de no-entrenamiento** en ToS/Privacy Policy/DPA (hay que pedirla por escrito); **el DPA no está firmado por defecto** → sin él Runpod es controller con fines propios; **los "Performance Data" (logs/telemetría) quedan fuera del DPA** (retención no acotada); **Community Cloud deja de aceptar hosts nuevos** → el precio barato ($0,22/h) está en retirada y Secure cuesta ×2,3; cifrado solo en volume disk; 28 datacenters (5 UE, 2 EEE, 12 US, 3 CA, 2 APAC), sin UK ni LATAM; **Runpod no documenta Tailscale** (su red privada oficial es *Global networking* + SSH por `ssh.runpod.io`); sin SLA público de Pods. Alternativas con residencia UE verificadas: **Scaleway FR** (L4 €0,75/h per-minute, SLO 99,5%) y **OVHcloud FR** (L4 €0,75/h, notebooks efímeros); Nebius y Hetzner DE como otras; Vast.ai solo para precio. Tabla de material: planos legales / material de cliente confidential / material de concurso con PI de terceros = **NO PUEDE**; cálculos y presupuestos = condicional; renders IA y LoRA = condicional (5 condiciones).
- **Corrección de nomenclatura:** desde junio 2025 el nombre oficial es **Runpod** (una sola R mayúscula); "RunPod" está deprecado y el vault lo usa en ~15 lugares (ficha de entidad, glosarios, pbooks, presentaciones). Corrección pendiente.
- **Hecho nuevo (interfaz):** Telegram soporta temas/canales y el bot de n8n necesita pasar a entender `message_thread_id` → requerimiento concreto, no idea.

**Archivos de esta continuación**
- `raw/research/2026-10-28-runpod-auditoria-pi.md` + `-crudo.md` + `raw/research-cache/2026-10-28-runpod-auditoria-pi.json` (producidos por `@sherlock`)
- `raw/research/00-index.md` (fila nueva del research)
- `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` (este archivo, ampliado)

**Topics:** Studio OS (producto) · topics de Telegram · canal de broadcast · digest por mail · Cal.com + Google Calendar · Fathom trunk · Dispatcher n8n por chat_id · Runpod Secure Cloud vs Community Cloud · DPA y Performance Data · Scaleway/OVHcloud FR como nodo GPU UE · tailscaled sidecar en pod (sin respaldo oficial) · Hermes gateway/s6/perfiles · state.db WAL · incidente de dashboard Hermes · AIZ como caso demo.

**Entidades:** Runpod (Secure Cloud, Community Cloud, network volume, Global networking) · Scaleway · OVHcloud · Nebius · Hetzner · Nous Research / Hermes Agent · Telegram (foros, canales, message_thread_id) · Cal.com · Fathom · Scaleway → nodo N4 UE.

**Hechos:** (1) el shell de Telegram + agenda + digest ya existe y funciona en n8n → el hueco real es la capa de ejecución CAD/3D y el registro, no el chat; (2) el nodo GPU cloud tiene una alternativa europea con precio casi equivalente al Secure de Runpod; (3) el mandato de PI admite Runpod solo como cómputo efímero con DPA firmado y material derivado no sensible; (4) un dashboard de Hermes expuesto es un riesgo de backdoor SSH documentado, no teórico.

**Pendiente de decisión:** perfil de despliegue primario (local first / cloud first / dos perfiles) · política de PI en la nube (firme vs excepción Secure con autorización) · nodo GPU por defecto (Scaleway/OVH UE vs Runpod Secure) · un agente o uno por persona para el producto.

## Continuación 2 — Estructura: decisiones, medición del VPS y vía sin PC 24/7

**Decisiones del usuario:** (1) **Hermes desde el arranque en el mismo VPS** que n8n/Postgres, con esta PC (P:) como banco de pruebas; (2) nodo GPU = **Runpod Secure**; (3) **un agente del estudio** (no uno por persona); (4) **transición por etapas** en Telegram: hoy sigue el bot de n8n (agenda) y el estado final es que **todo corra en automatización con Hermes hablando por Telegram**; (5) puente MCP = **P1 + P3** (mcp-proxy HTTP sobre Tailscale para lectura + runner propio con API de tareas para escritura); (6) **medir el VPS antes de decidir capacidad**.

**Medición del VPS (SSH `contabo`, 2026-10-28 02:10 AR, solo lectura):** 7.941 MB RAM total / **4.858 MB disponibles** · load 0,15 en 4 vCPU · swap 2.047 MB sin uso · disco 72 GB con 50 GB libres · **Docker Swarm sobre EasyPanel + Traefik**, 12 servicios. Consumo: n8n 736 MB · Chatwoot+sidekiq+db 945 MB · Leantime+mysql 691 MB · easypanel+traefik 191 MB · qdrant 61 MB. **Veredicto: no hace falta ampliar el VPS** → Hermes con `--memory=3g --cpus=2`, sin Playwright al inicio, como servicio Swarm más (no `docker run` suelto). Riesgo anotado: `n8nio/n8n:latest` sin versión pineada → upgrades no controlados.

**Vía para no depender de la PC 24/7 (hechos verificados):** **Rhino.Compute** es un servicio REST headless (Rhino + Grasshopper SDK, Windows y Linux, autohospedable o en Azure/AWS con billing por core-hour) y trae **Hops**, el componente headless oficial de Grasshopper en Rhino 8 → la geometría no necesita el escritorio, sí una licencia Rhino en un servidor siempre encendido. **APS Design Automation** es la vía cloud oficial de AutoCAD, **pero no cubre AutoCAD LT** (el estudio tiene LT 2027) → a verificar en la doc de productos soportados antes de planearlo. ComfyUI ya está en Runpod. **Twinmotion sigue sin API** → queda como trabajo asistido.

**Estructura derivada:** tres perfiles de ejecución — **C1 nube oficial** (APS DA para AutoCAD; Rhino.Compute+Hops para geometría) · **C2 nube propia GPU** (Runpod Secure) · **L local** (PC del estudio: AutoCAD LT GUI, Rhino 8, Twinmotion, Unreal) — y el contrato **no distingue entre ellos**: lo único que cambia es el perfil (herramienta, datos permitidos, costo). La PC del estudio pasa a ser **recurso elástico** (Wake-on-LAN / smart plug) y lugar de interacción humana, no servidor.

**Vistas Hermes confirmadas en su documentación oficial (verificado 2026-10-28):** imagen `nousresearch/hermes-agent`; estado íntegro en `/opt/data` (config, `.env`, sessions, memories, skills, cron, logs, `state.db` SQLite WAL → **volumen nombrado, no bind mount**, porque WAL sobre 9p/virtiofs se corrompe); gateway con s6 (auto-restart, multi-perfil en un contenedor); API OpenAI-compatible en 8642, dashboard 9119, webapp 9120; `mcp_servers` en `config.yaml` (stdio + HTTP, filtros por tool, `${ENV}`, lazy, reload automático del gateway ~1 min); entrada oficial **`n8n-official`** → conecta con nuestro `https://n8n.pitau.tech/mcp-server/http` (el bridge de terceros de n8n fue retirado); recursos: 1 GB mín / 2-4 GB rec, 1 core / 2 cores rec; **el dashboard exige auth en bind no-loopback** desde el endurecimiento de junio 2026 (escáneres entraron por dashboards expuestos y plantaron una backdoor SSH) → solo tailnet + basic auth.

**Interfaz (decidido):** Telegram = chat del agente · **1 grupo por obra con temas** (AutoCAD / Rhino-3D / Render-IA / Obra / Comercial) · **1 canal broadcast** de bitácora del sistema · chat privado para aprobaciones · **botones inline** Aprobar/Aprobar con cambios/Rechazar (cierran el HITL y quedan en el registro) · notificaciones en 3 capas (Telegram inmediato → digest diario por mail → mail al cliente solo en entrega, nivel D) · Discord queda para mesa de iteración visual y canal de método (material sensible no sale del Drive/vault) · WhatsApp sigue para clientes · Fathom = tronco (reunión → minuta → decisiones → Leantime → vault) · el agente de Cal.com ya funciona y se reusa.

**Decisiones de estructura tomadas:** Telegram → transición por etapas (n8n ahora, Hermes después) · puente → P1+P3 · runner local → recurso elástico con WOL + perfiles cloud C1/C2 · capacidad → medir primero (medido: entra sin ampliar).

**Pendiente:** perfil del runner del estudio (PC a demanda vs mini-servidor con licencias vs cloud) · cómo consume Hermes el vault · confirmación del alcance del MVP (AIZ de punta a punta) · verificación de productos soportados por APS Design Automation.

**Archivos de esta continuación:** ninguno nuevo en el vault (solo lecturas + medición SSH). El research de Runpod quedó en `raw/research/2026-10-28-runpod-auditoria-pi.md`.

**Topics:** Docker Swarm + EasyPanel + Traefik · límite de memoria por servicio · SQLite WAL y volúmenes nombrados · Wake-on-LAN y smart plug · Rhino.Compute · Hops (Grasshopper headless) · APS Design Automation · AutoCAD LT vs AutoCAD completo · skills de n8n y entrypoint `n8n-official` · comandos de approval inline · topics de Telegram · digest por mail · Studio OS como producto.

**Hechos:** (1) el VPS tiene 4,8 GB libres: Hermes entra sin ampliar; (2) Rhino.Compute + Hops hacen que la geometría sea ejecutable sin el escritorio, con licencia en un servidor; (3) la nube oficial de AutoCAD no cubre LT, así que para el estudio la vía cloud de AutoCAD queda bloqueada por licencia; (4) el estado final de Telegram (Hermes) y el presente (n8n) pueden convivir sin conflicto si el token migra de forma explícita en una etapa con criterio de rollback.

**Pendiente de decisión:** runner del estudio (PC a demanda / mini-servidor con licencias / cloud) · consumo del vault por Hermes · alcance del MVP · verificación de APS.

## Continuación 3 — Cierre: ADRs, proyecto MVP_07 y documentos

**Escritos (con el "s" del usuario al elegir "Primero los ADRs"):**

- `specs/ADR-2026-10-28-agente-hermes-en-vps.md` — Hermes en el mismo VPS como agente único del estudio
- `specs/ADR-2026-10-28-nodo-gpu-runpod-secure.md` — Runpod Secure bajo 5 condiciones previas
- `specs/ADR-2026-10-28-puente-mcp-p1-p3.md` — puente P1 (proxy MCP-http) + P3 (runner con API de tareas)
- `specs/ADR-2026-10-28-registro-hibrido-postgres-vault.md` — Postgres `studio_os` + vault, escritor único
- `specs/ADR-2026-10-28-un-agente-por-estudio.md` — un agente con perfiles por rol
- `specs/ADR-2026-10-28-vault-canónico-en-vps.md` — remoto git bare en el VPS, GitHub privado como espejo
- `specs/ADR-2026-10-28-telegram-como-interfase.md` — Telegram (temas + canal), n8n hoy y Hermes después
- `specs/ADR-2026-10-28-perfiles-de-ejecucion.md` — tres perfiles de ejecución
- `proyectos/MVP_07-studio-os-sistema/readme-mvp_07.md` — puerta de entrada del proyecto
- `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` — documento vivo: visión → estructura → requerimientos (R1-R8) → roadmap F0-F6 → cierre del MVP (5 criterios) → 8 decisiones → 8 preguntas abiertas
- `proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07.md` — sobre de tarea (JSON + reglas), DDL `studio_os` (8 tablas), selección de ejecutor, API del runner, perfil de pod GPU, `SOUL.md` con las 4 reglas de Karpathy, configuración MCP, sincronización del vault, métricas
- `proyectos/00-index.md` — fila del MVP_07 agregada
- `log.md` — entrada de la sesión al principio (archivo append-only)

**Verificado al escribir**: los wikilinks a `wiki/glosario/software/{autocad,comfyui,git,leantime,n8n,opencode,telegram,twinmotion}`, `wiki/glosario/entidades/runpod` y `wiki/glosario/conceptos/cerebro-digital-karpathy` existen; **no existen** fichas de software para `fathom`, `postgres` ni `tailscale` → esos enlaces se corrigieron por `n8n` y `ADR-INFRA-001`. Queda como tarea de curaduría crear esas tres fichas.

**Pendiente para la próxima sesión** (requieren `s` para `wiki/`): crear `wiki/glosario/software/{fathom,postgres,tailscale}.md` · actualizar `wiki/estudio/analisis/00-index.md` (la pregunta abierta "Tailscale vs Cloudflare Tunnel" ya está resuelta: Tailscale) · renombrar "RunPod" → "Runpod" en los ~15 lugares del vault · documentar la decisión de PI en `wiki/estudio/decision-arquitectura-ia-privacidad.md` (hoy dice "nunca planos legales/concurso en cloud" y hay que incorporar la tabla de 6 clases de material de la auditoría).

**Hechos nuevos de esta sesión:** (1) el nombre oficial del proveedor es **Runpod** desde junio 2025 (una sola R mayúscula) y "RunPod" está deprecado; (2) el VPS tiene 4.858 MB de RAM disponibles → Hermes entra sin ampliar; (3) Rhino.Compute + Hops hacen posible la geometría headless con licencia en servidor; (4) APS Design Automation no cubre AutoCAD LT ni la versión estudiantes → la vía cloud de AutoCAD está bloqueada por licencia para el estudio y para el banco; (5) no hay ficha de software para fathom/postgres/tailscale en el glosario: hueco de curaduría.

**Entidades:** Studio OS (producto) · APS Design Automation · Rhino.Compute · Hops · Scaleway · OVHcloud · Runpod Secure Cloud · EasyPanel + Traefik + Docker Swarm · Tailscale · MCP proxy (P1) · studio-os-runner (P3) · registry API · schema `studio_os`.

## Continuación 4 — Plan de construcción (02-ft) y cierre de la sesión

- `proyectos/MVP_07-studio-os-sistema/02-ft-mvp_07.md` — plan técnico de construcción: reglas del juego (HITL, el agente escribe y vos corrés, sin dependencias nuevas, reversión antes que explicación), **F0 con 11 tareas** (baseline → remoto canónico del vault → clon de trabajo → Tailscale → servicio Hermes en EasyPanel → setup → modelo → MCP de n8n → `SOUL.md` + skills → MCP de lectura del vault → cierre), **F1** (schema, API del registro, validador del sobre, primer tool `audit_dwg`, detección de desactualizados), **F2** (camino corto con backend SSH, elección de proxy MCP, API de tareas del runner, idempotencia, "no disponible", perfil de pod), F3-F6 con su riesgo y su decisión pendiente, **inventario de 7 scripts** con el comando exacto para cada uno, **13 pruebas de aceptación**, métricas, matriz de riesgos con reversión, 7 decisiones pendientes con fecha, y **los primeros 90 minutos** de mañana.
- Ajustes de consistencia: F0 ahora incluye el remoto canónico del vault (el agente lo necesita desde el día 1) y F5 conserva solo el runner gemelo y la sincronización del clon del estudio; el `readme` y el `log.md` updated con el nuevo archivo.

**Hechos verificados hoy (documentación oficial):** Tailscale en Linux → `curl -fsSL https://tailscale.com/install.sh | sh` + `sudo tailscale up`; para servidores hay que **desactivar la expiración de clave**; `tailscale set --ssh` habilita SSH por la red privada. **Hermes**: `~/.hermes/` contiene `config.yaml`, `.env`, `auth.json`, `SOUL.md`, `memories/`, `skills/`, `cron/`, `sessions/`, `logs/`; `hermes config set` separa secretos (UPPER_SNAKE → `.env`) de ajustes (dotted → `config.yaml`); `hermes setup --portal` deja listo proveedor + gateway; `state.db` usa WAL salvo en montajes 9p/virtiofs; y tiene **seis backends de terminal**: local, docker, **ssh**, modal, daytona, vercel_sandbox. Proxies MCP para el puente, en orden de simplicidad: **TBXark/mcp-proxy** (un endpoint HTTP para N servidores stdio, imagen Docker, config por archivo) · **sparfenyuk/mcp-proxy** (puente simple stdio↔streamable HTTP) · como opciones pesadas, `agentgateway` (RBC) e `IBM-mcp-context-forge` con auth y auditoría.

**Hallazgo de diseño (Karpathy: simplicidad primero):** el **backend SSH de Hermes** permite ejecutar en la PC del estudio por la red privada desde el primer día, sin construir el proxy MCP: el proxy (P1) pasa a ser una optimización posterior y el runner con API de tareas (P3) queda como la única pieza nueva de código que hay que escribir para las operaciones de escritura.

**Cierre de la sesión:** el diseño de Studio OS queda documentado (visión, estructura, requerimientos, paso a paso, 8 ADRs, contratos técnicos y plan de construcción). Mañana arranca F0 con el `s` del usuario.

**Topics:** backend SSH de Hermes · proxy MCP stdio↔HTTP · TBXark/mcp-proxy · expiración de claves Tailscale · WAL de state.db · EasyPanel como lugar del despliegue · plan por tareas con verificación y reversión.

**Entidades:** TBXark/mcp-proxy · sparfenyuk/mcp-proxy · agentgateway · mcpgateway · EasyPanel · Tailscale.

**Hechos:** (1) el plan no requiere proxy MCP para el primer circuito → menos piezas antes de valor; (2) la instalación de Tailscale en un servidor exige desactivar la expiración de clave; (3) Hermes separa secretos de configuración por diseño, lo que encaja con la regla del vault de que los secretos no van al repo; (4) el F0 tiene 11 tareas y ninguna toca Telegram: la interfaz del estudio no se arriesga hasta que el circuito funcione por API.

## Continuación 5 — Kit de F0 armado (código y comandos listos)

**Escrito (con la aprobación del usuario: "sí quiero que armes el plan"):**

- `scripts/studio_os_verificar_vps.py` — script **de solo lectura** que inventaría el VPS por SSH (alias `contabo`) usando solo biblioteca estándar: RAM total/usada/disponible, swap, disco, carga, memoria por contenedor y **veredicto** sobre si entran los 3 GB de Hermes con margen. Incluye comentarios `# NOTA ES:` línea por línea, como pide el `AGENTS.md`.
- `scripts/studio_os_verificar_vps_notas.md` — notas didácticas: qué pregunta cada bloque, qué esperar (con el resultado real del 28/10), errores frecuentes y qué NO hace a propósito.
- `proyectos/MVP_07-studio-os-sistema/deploy/00-f0-comandos.md` — los 7 pasos de F0 con comandos copiables, verificación y reversión: inventario → remoto canónico del vault (bare + clon de trabajo + espejo GitHub) → Tailscale → servicio Hermes → setup/modelo/MCP de n8n → `SOUL.md` + skills + MCP de lectura → cierre con checklist.
- `proyectos/MVP_07-studio-os-sistema/deploy/hermes.compose.yml` — el servicio para EasyPanel: imagen `stable`, comando `gateway run`, **volumen nombrado** para `/opt/data` (el `state.db` usa WAL y un bind sobre 9p/virtiofs se corrompe), el clon del vault montado **de solo lectura** en `/vault`, límite de 3 GB / 2 CPU y **cero puertos publicados**.
- `proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md` — identidad completa del agente: las 4 reglas de Karpathy, el mandato de PI por clase de dato, los niveles A-D, cómo se pide y se registra la aprobación, qué no hacer y el bucle de conocimiento.
- `proyectos/MVP_07-studio-os-sistema/hermes/skills/auditar-documentacion-cad/SKILL.md` — primera habilidad en formato Hermes: objetivo, entradas, herramientas autorizadas, precondiciones, procedimiento, criterios de validación, permisos, acciones que requieren aprobación, formato de salida, errores y evidencias.
- `scripts/00-index.md` — sección "Studio OS (MVP_07)" con el script nuevo y los 6 scripts planeados para F1/F2/F4.
- `02-ft-mvp_07.md` y `readme-mvp_07.md` — enlazan el kit y el árbol de archivos actualizado.

**Decisiones de diseño que salieron al armar el kit:**
- **Cero puertos publicados en F0**: el gateway de Telegram hace long polling (sale, no entra), la API 8642 y el dashboard 9119 quedan apagados. La razón es el incidente real de junio 2026 (escáneres entrando por dashboards expuestos y plantando una backdoor SSH). Cuando haga falta exponer la API, va por la red privada (`host_ip` de la 100.x o `tailscale serve`).
- **El vault se monta de solo lectura en el contenedor**: el agente lee; las escrituras pasan por el MCP del vault con aprobación, no por el contenedor. Evita que el agente toque el repo por la puerta de atrás.
- **El script de inventario no decide, muestra**: devuelve el veredicto en texto y la decisión se toma con el número a la vista. Es el script más aburrido del sistema a propósito.

**Pendiente de una decisión del usuario (para el paso 5 de F0):** modelo del agente — **OpenRouter** (recomendado: ya está declarado como subencargado en la política de privacidad del estudio y el agente razona sobre código y documentos) u **Ollama local en el VPS** (privacidad, pero compite por RAM con Hermes y n8n).

**Archivos de esta continuación:** `scripts/studio_os_verificar_vps.py` · `scripts/studio_os_verificar_vps_notas.md` · `proyectos/MVP_07-studio-os-sistema/deploy/00-f0-comandos.md` · `proyectos/MVP_07-studio-os-sistema/deploy/hermes.compose.yml` · `proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md` · `proyectos/MVP_07-studio-os-sistema/hermes/skills/auditar-documentacion-cad/SKILL.md` · modifications a `scripts/00-index.md`, `02-ft-mvp_07.md`, `readme-mvp_07.md`, `log.md`.

**Topics:** long polling de Telegram · cero puertos publicados · volumen nombrado y WAL · vault montado de solo lectura · EasyPanel como lugar del despliegue · script de inventario como baseline · SOUL.md versionado · skills en formato Hermes · OpenRouter vs Ollama.

**Hechos:** (1) el primer circuito del sistema se puede verificar sin abrir un solo puerto en el VPS; (2) el clon del vault se publica en el host y se monta de solo lectura: el agente no puede escribir en el repo sin pasar por el MCP con aprobación; (3) el inventario del VPS ya se corrió a mano (04.858 MB disponibles) y quedó encapsulado en un script reproducible con su veredicto; (4) el modelo del agente es la única decisión de F0 que falta y es del usuario (costo vs privacidad).

**Entidades:** OpenRouter · Ollama · EasyPanel · Tailscale · SOUL.md · Hermes skills.

## Continuación 6 — Consolidación en un único documento

**Pedido del usuario:** "tiene que ser un único documento". Todo el sistema quedó fusionado en **un solo archivo**: `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md`, con nueve secciones — 1 Visión · 2 Estructura · 3 Requerimientos · 4 Roadmap y cierre del MVP · 5 Contratos técnicos · 6 Decisiones (las 8 ADRs en formato Nygard completo) · 7 Plan de construcción · 8 Comandos de F0 · 9 Anexos (compose, `SOUL.md`, skill, script).

**Archivos fusionados (pendientes de borrar, requieren `s`):** `proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07.md` · `02-ft-mvp_07.md` · `deploy/00-f0-comandos.md` · `deploy/hermes.compose.yml` · `hermes/SOUL.md` · `hermes/skills/auditar-documentacion-cad/SKILL.md` · `specs/ADR-2026-10-28-agente-hermes-en-vps.md` · `specs/ADR-2026-10-28-nodo-gpu-runpod-secure.md` · `specs/ADR-2026-10-28-puente-mcp-p1-p3.md` · `specs/ADR-2026-10-28-registro-hibrido-postgres-vault.md` · `specs/ADR-2026-10-28-un-agente-por-estudio.md` · `specs/ADR-2026-10-28-vault-canónico-en-vps.md` · `specs/ADR-2026-10-28-telegram-como-interfase.md` · `specs/ADR-2026-10-28-perfiles-de-ejecucion.md`.

**Nuevo:** `scripts/studio_os_publicar_hermes.py` + `_notas.md` — hace que "un único documento" sea técnicamente cierto: extrae del maestro los bloques marcados con `<!-- archivo: ... -->` (§9.2 `SOUL.md` y §9.3 skill) y los publica dentro del contenedor del agente por SSH (`docker exec -i <id> sh -c 'cat > ...'`), con verificación posterior. Modo `--dry-run` para ver qué haría sin tocar el VPS.

**Corregido en el proceso:**
- **Trampa de Docker Swarm**: los contenedores de EasyPanel se llaman `servicio.1.tarea`, así que `docker exec hermes ...` **no funciona**. Todos los comandos del maestro ahora resuelven primero el ID real (`docker ps --filter name=hermes --format '{{.ID}}' | head -1`) y lo usan como `<ID_HERMES>`.
- El `readme-mvp_07.md` quedó como puerta mínima (el maestro es el documento) y `proyectos/00-index.md` apunta al maestro.
- `scripts/00-index.md` suma el script de publicación y deja los 6 scripts de F1/F2/F4 como pendientes.

**Nota de método:** el maestro es la fuente de verdad del diseño; el código queda en `scripts/` porque se ejecuta, y el research y las sesiones quedan en `raw/` porque son evidencia. La regla "un documento" aplica al **diseño**, no a los artefactos que tienen que existir como archivos.

**Pendiente de una decisión del usuario (paso F0.7):** modelo del agente — OpenRouter (recomendado) u Ollama local en el VPS.

**Archivos de esta continuación:** `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` (reescrito como maestro único) · `readme-mvp_07.md` (reescrito como puerta) · `scripts/studio_os_publicar_hermes.py` + `_notas.md` · modifications a `proyectos/00-index.md`, `scripts/00-index.md`, `log.md`.

**Topics:** documento maestro único · publicación por extracción · marcadores HTML en markdown · Docker Swarm y resolución de container ID · consolidation de ADRs en un documento.

**Hechos:** (1) un solo documento puede contener visión, contratos, plan y decisiones sin perder trazabilidad, siempre que los artefactos ejecutables (código, research, sesiones) sigan fuera; (2) el publish script elimina el paso manual de copiar `SOUL.md` al contenedor y garantiza que el agente y el documento no se separen; (3) el error de `docker exec <servicio>` en Swarm afecta a todos los comandos de operación: queda documentado en el maestro como `<ID_HERMES>`; (4) la consolidación deja el vault con 14 archivos menos que mantener y un solo lugar donde leer el sistema.

## Cierre de sesión

**Qué quedó hecho**
- Diseño completo de Studio OS en **un solo documento**: `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` (9 secciones: visión · estructura · requerimientos · roadmap y cierre del MVP · contratos técnicos · 8 decisiones Nygard · plan de construcción · comandos de F0 · anexos).
- Auditoría de Runpod (29 fuentes oficiales) que endurece la política de PI y fija Runpod Secure bajo 5 condiciones.
- Medición del VPS (solo lectura): 4.858 MB de RAM disponibles → **Hermes entra sin ampliar**.
- Verificación de la documentación oficial de Hermes (Docker, MCP, configuración, backends de terminal) y de Tailscale; corrección de la trampa de Swarm (`docker exec <servicio>` no existe).
- Kit de F0: `scripts/studio_os_verificar_vps.py` (+ notas) y `scripts/studio_os_publicar_hermes.py` (+ notas), compose del servicio, comandos paso a paso, `SOUL.md` y skill `auditar-documentacion-cad`.

**Decisiones tomadas**
Studio OS como producto · Hermes en el VPS desde el arranque · un agente del estudio · Telegram como interfase (n8n ahora, Hermes después) · registro híbrido (Postgres `studio_os` + vault) · puente P1+P3 · vault canónico en el VPS con GitHub como espejo · Runpod Secure · tres perfiles de ejecución · MVP = caso AIZ + render IA.

**Pendiente que necesita un `s`**
- **Borrar los 14 archivos fusionados** (contenido ya dentro del maestro): `01-spec-mvp_07.md`, `02-ft-mvp_07.md`, `deploy/00-f0-comandos.md`, `deploy/hermes.compose.yml`, `hermes/SOUL.md`, `hermes/skills/auditar-documentacion-cad/SKILL.md` y los 8 `specs/ADR-2026-10-28-*.md`. Hasta que se borren conviven con el maestro: el contenido es el mismo, no hay contradicción, solo duplicación.
- Curaduría en `wiki/` (3 fichas de software: `fathom`, `postgres`, `tailscale` · renombrar RunPod → Runpod · actualizar la decisión de PI con la tabla de 6 clases de material · cerrar la pregunta abierta de Tailscale vs Cloudflare).

**Punto de reanudación (mañana)**
`00-filo-mvp_07.md` §8 → paso 1: `P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py` (baseline, modo lectura). Antes del paso 5 hace falta decidir el **modelo del agente: OpenRouter (recomendado) u Ollama local**.

**Regla de la sesión:** cada paso se ejecuta con un `s` explícito y con reversión definida antes de tocar nada.

## Continuación 7 — Reset: el proyecto se documenta en VISION · ESTRUCTURA · REQUISITOS

**Pedido del usuario:** "necesito que revises raw/docs/plan-hermes.md y vayamos delineandolo uno a uno... porque creaste muchos archivos y no entiendo nada. empecemos de cero y que en este proyecto los archivos se nomenclen VISION - ESTRUCTURA - REQUISITOS". Luego: "ve por partes", "máximo 25 líneas para leer en la terminal" y "el doc es un referente para que definamos y analicemos opciones, con el stack tiene que estar delineado completo primero vision... conceptualmente".

**Decisiones tomadas en esta ronda**
- El proyecto se documenta con **tres archivos**: `VISION.md` · `ESTRUCTURA.md` · `REQUISITOS.md`. Cero archivos extra.
- **El stack va en tabla**, con las alternativas **libres y open source primero** en cada pieza, la elegida hoy, el costo y la licencia. Principio nuevo incorporado: *"libre y open source cuando se pueda"* (el costo se paga solo cuando no hay alternativa equivalente).
- **GPU local primero**: la nube (Runpod Secure) queda como excepción para 9B, LoRA y video.
- **n8n se mantiene**; las alternativas libres (Node-RED, Windmill) quedan anotadas como candidatas, no como reemplazo.
- **Ollama local en vez de modelo en la nube** — con un dato nuevo: la PC de desarrollo tiene 32 GB de RAM, el VPS 8 GB. Queda como pregunta abierta §13.1 (dónde vive el modelo).
- **Conectar opencode ↔ Hermes**: dos direcciones a evaluar en ESTRUCTURA (opencode usando la API OpenAI-compatible de Hermes · Hermes invocando opencode por MCP · Hermes operando la PC por SSH). Pregunta abierta §13.2.
- **El orden de fases se rearma desde cero**, una vez escritas VISION y ESTRUCTURA (no se copia el doc §14).
- REQUISITOS.md se escribe con estilo de desarrollo de software: alcance, actores, casos como historias, RF/RNF con trazabilidad, criterios de aceptación Given/When/Then, gobernanza por nivel de riesgo, métricas y plan por fases.

**Escrito**
- `proyectos/MVP_07-studio-os-sistema/VISION.md` — 14 secciones en 5 bloques: (1) qué es y por qué, el problema, el norte; (2) el recorrido del trabajo del estudio en 11 pasos con la columna "dónde entra el agente" y quién decide; (3) Hermes conceptualmente: qué es, qué hace, cómo se conecta, qué no hace, alternativas evaluadas; (4) el stack delineado en tabla de 22 piezas (agente, modelos, imágenes, GPU, orquestación, red, registro, memoria, búsqueda, CAD, 3D, BIM, visualización, reuniones, agenda, tablero, chat, soporte, secretos, backup, acceso remoto) con las tres notas honestas sobre licencias que el estudio ya paga, el costo real (GPU) y la pieza que falta y va a costar (licencia de Rhino en servidor); (5) los 9 principios, las 7 habilidades, los 5 modos de ejecución y los 3 perfiles, los niveles A-D, el camino en 3 tramos, las 8 decisiones tomadas y 5 preguntas abiertas con opciones.

**Borrado (16 archivos, con la aprobación del plan)**
`readme-mvp_07.md` · `01-spec-mvp_07.md` · `02-ft-mvp_07.md` · `deploy/00-f0-comandos.md` · `deploy/hermes.compose.yml` · `hermes/SOUL.md` · `hermes/skills/auditar-documentacion-cad/SKILL.md` · los 8 `specs/ADR-2026-10-28-*.md` · `scripts/studio_os_publicar_hermes.py` + notas.

**Conservado**: `raw/research/2026-10-28-runpod-auditoria-pi.md` (evidencia) · `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` (bitácora) · `scripts/studio_os_verificar_vps.py` + notas (el inventario del VPS) · `00-filo-mvp_07.md`, reetiquetado como **borrador técnico** que se borra cuando existan ESTRUCTURA y REQUISITOS (tiene el material ya desarrollado: contrato de tarea, DDL, API del runner, perfil de pod, plan de F0).

**Punto de reanudación**: escribir `ESTRUCTURA.md` (9 secciones: vista general · dónde vive cada pieza · el agente y su vínculo con los usos · las integraciones una por una · el contrato común · registro y grafo · seguridad y despliegue · decisiones técnicas · qué no decide). Después `REQUISITOS.md`.

**Topics:** reset de documentación · nomenclatura VISION-ESTRUCTURA-REQUISITOS · stack libre first · Ollama local · opencode ↔ Hermes · rearmado de fases.

**Entidades:** Vision/Estr/Req como los tres documentos del proyecto · Ollama · Headscale · Netbird · Node-RED · Windmill · Mattermost · Radicale · Vikunja · SOPS · restic · MeshCentral · RustDesk · QCAD · LibreCAD · ezdxf · ODA File Converter · CadQuery · IfcMCP · Bonsai · FreeCAD · Jitsi · Quartz · Zettlr · Logseq · sqllite-vec · Meilisearch.

**Hechos:** (1) el stack completo se puede ordenar en 22 piezas, y solo 3 tienen licencia paga del estudio (AutoCAD LT, Rhino 8, Twinmotion); (2) el costo real del sistema es la GPU, no el software: con GPU local el stack es enteramente libre; (3) el recorrido del trabajo muestra que el agente entra en 9 de los 11 pasos y en ninguno decide el criterio; (4) la documentación del proyecto se puede reducir a 3 archivos sin perder el trabajo, porque el detalle técnico se escribe el día que exista código.

## Continuación 8 — VISION.md con el recorrido real del estudio

**El usuario pasó su propio ciclo de trabajo** (nota: la idea del cuaderno viene del video *"El hábito de Leonardo da Vinci que me ha quitado el móvil de las manos | Commonplace book"*, Maialen Lleó, 12:35 — que el vault ya tenía anotado como idea de proyecto *"#14 davinci-notebook: cuaderno digital tipo Da Vinci con todo"*).

**Cambios en `proyectos/MVP_07-studio-os-sistema/VISION.md`:**
- **Nuevo §1.5 "El cuaderno digital"**: todo lo que el estudio piensa, dibuja, mide y genera termina en un cuaderno; la parte manual es del arquitecto (croquis, escalas investigadas, decisiones) y la automatizada es de Hermes (indexar, etiquetar, conectar, resumir). Tres efectos: se puede buscar, se puede reusar, el agente lo mejora.
- **§2 recorrido reescrito con su versión (10 pasos)**: 1 cliente → 2 reunión → 3 compromisos → 4 cuaderno → 5 planos → 6 3D → 7 render → 8 obra → 9 entregas → 10 memoria.
  - El **CRM no es un CRM**: una hoja con nombre, contacto, mail (Instagram a futuro).
  - **Fathom a veces repite la misma reunión en varios "meetings"** → el agente los agrupa antes de resumir.
  - Los **compromisos llevan qué entregar y qué fecha** → recordatorio por Telegram + mail al cliente con el formato del estudio (lo manda una persona).
  - Un **agente experto en ComfyUI** con sus skills, y las iteraciones a un **portal** porque por mail pesan demasiado.
  - **Obra**: fotos indexadas con tags; aparece la pregunta de **visión por computadora**.
  - **Entregas**: el agente arma el paquete, la persona escribe el mail y adjunta, queda registro con fecha.
  - **Memoria**: la del sistema, que Hermes mejora cada vez.
- **Stack +6 filas** (siempre libres primero): Google Sheets/Baserow/NocoDB/Directus · Quartz/MkDocs/Obsidian Publish/Zettlr · PhotoPrism/Piwigo/Nextcloud+Memories · Nextcloud+Memories/Immich · Qwen-VL/CLIP/SigLIP/exiftool/OpenCV · plantillas+Gmail API. Y una cuarta nota: cuaderno, portal y fotos **salen gratis** con software libre.
- **Habilidades**: reorganizadas en tres grupos (cliente y relación / diseño / obra y conocimiento) y ampliadas con `gestionar-clientes`, `preparar-compromisos`, `redactar-correo-cliente`, `experto-comfyui`, `publicar-iteraciones`, `curar-cuaderno`.
- **Decisiones (+5)** y **preguntas abiertas (+2)**: visión por computadora en obra y dónde viven las fotos de obra.

**Nota de método:** la visión se define a partir de **cómo trabaja el estudio**, no al revés. El stack y las habilidades son consecuencia: por eso el "CRM" terminó siendo una hoja y el render terminó siendo un portal.

**Pendiente:** `ESTRUCTURA.md` (9 secciones) y después `REQUISITOS.md`. `00-filo-mvp_07.md` queda como borrador técnico y se borra cuando existan.

**Topics:** commonplace book · cuaderno digital · mini CRM · compromisos con fecha · portal de iteraciones · agente experto en ComfyUI · visión por computadora · fotos de obra con tags.

**Entidades:** Maialen Lleó · Qwen-VL · CLIP/SigLIP · exiftool · OpenCV · Nextcloud Memories · Immich · PhotoPrism · Baserow · NocoDB · Directus · Quartz · MkDocs.

**Hechos:** (1) el "cuaderno digital" ya estaba registrado en el vault como idea (#14 davinci-notebook) y nunca se hizo — ahora es el eje conceptual del producto; (2) el ciclo real del estudio tiene 10 pasos y el agente entra en 8 de ellos, siempre preparando o registrando; (3) el CRM no se justifica: la solución es una hoja; (4) el portal de iteraciones es la pieza que evita enviar renders por mail, y sale gratis con Quartz; (5) todo lo nuevo que se incorporó al stack (cuaderno, portal, fotos, visión, clientes) tiene alternativa libre y self-hosted.

## Continuación 10 — Separación de los tres documentos (VISIÓN · ESTRUCTURA · REQUISITOS)

**Pedido del usuario:** "necesito que definamos qué va a contener la visión, la estructura y los requisitos, porque creo que se están mezclando".

**Regla de reparto definida** (va al inicio de los tres archivos, y es el criterio para decidir dónde cae cualquier idea nueva):

| | **VISION** | **ESTRUCTURA** | **REQUISITOS** |
|---|---|---|---|
| La pregunta | ¿qué es y para qué? | ¿dónde vive y cómo se conecta? | ¿qué tiene que cumplir y cómo se mide? |
| Qué contiene | el problema · el recorrido · el cuaderno digital · Hermes en conceptual · el stack con sus alternativas · las decisiones de producto | los 4 nodos · dónde vive cada pieza · el agente y sus conexiones · cada integración con sus opciones · el contrato entre componentes · el modelo de datos · seguridad, secretos, backup y acceso remoto · puesta en marcha | alcance · actores · casos de uso · RF y RNF · criterios de aceptación · gobernanza A-D · regla automatizar/persona · métricas · plan de entrega · decisiones abiertas |

**Idea → archivo (ejemplo de reparto):** el problema, el norte y la pregunta del junior → VISION. El recorrido del estudio y el cuaderno digital → VISION (qué se digitaliza) y ESTRUCTURA (cómo se escanea, publica y navega). La lista de habilidades → VISION (qué sabe hacer) y REQUISITOS (cómo se sabe que está). El stack con alternativas → VISION; dónde vive y cómo se conecta → ESTRUCTURA. Niveles A-D y quién aprueba → REQUISITOS. La regla automatizar/persona → VISION (la frase) y REQUISITOS (la matriz). El plan por fases, métricas y pruebas → REQUISITOS.

**Movido desde VISION.md a los otros documentos:**
- §"Cómo se conecta" del agente → ESTRUCTURA §3.2.
- §"Qué modelo usa" (OpenCode Go → Ollama en el estudio → OpenRouter) → ESTRUCTURA §3.3.
- §"Los modos de ejecución" (L, R1-R4 y los tres perfiles) → ESTRUCTURA §3.4.
- §"Cuándo Telegram y cuándo Discord" (tabla completa) → VISION conserva la regla; el detalle → ESTRUCTURA.
- §"Niveles de riesgo" (tabla A-D) → VISION conserva la regla en una línea; el detalle → REQUISITOS §7.
- §"La regla de automatizar vs. persona" (matriz) → VISION conserva la frase; la matriz → REQUISITOS §8.
- §"Camino en tres tramos" → VISION conserva el por qué; el plan con criterios de entrada y salida → REQUISITOS §11.
- §"Preguntas abiertas" → VISION conserva las 3 de producto; las de construcción (modelo, n8n, red, Rhino 8/9, DPA) → REQUISITOS §10 con impacto y momento.
- Secretos, backup y acceso remoto → ESTRUCTURA §4.9 y §7.

**Archivos**
- `proyectos/MVP_07-studio-os-sistema/VISION.md` — depurado (338 → ~300 líneas): ahora es solo visión.
- `proyectos/MVP_07-studio-os-sistema/ESTRUCTURA.md` — nuevo, 11 secciones.
- `proyectos/MVP_07-studio-os-sistema/REQUISITOS.md` — nuevo, 12 secciones, estilo software.
- Borrado `00-filo-mvp_07.md` (el borrador técnico): su contenido quedó distribuido en ESTRUCTURA y REQUISITOS, y sigue en el historial de git y en el log de sesión.
- `proyectos/00-index.md` apunta a los tres documentos.

**Topics:** reparto de documentos · regla de pertenencia · dado/when/entonces · RF y RNF con trazabilidad · baseline · criterios de salida por tramo.

**Hechos:** (1) el problema de la mezcla no era de contenido sino de **criterio**: sin una regla explícita, cualquier idea nueva cae en el archivo que uno tiene abierto; (2) VISION, ESTRUCTURA y REQUISITOS se distinguen por la pregunta que contestan, y eso alcanza como test para cualquier idea nueva; (3) el nivel de detalle técnico (SQL, JSON, comandos) no pertenece a ninguno de los tres: sale con el código; (4) con la separación hecha, VISION tiene ~300 líneas, ESTRUCTURA ~400 y REQUISITOS ~380: ningún documento exige leer los otros dos para entenderse.

**Pendiente:** revisión conjunta de ESTRUCTURA y REQUISITOS (el usuario los tiene que leer y ajustar), y después arrancar la construcción por el tramo T0.

## Cierre de sesión (2) — 28/10, ~5 h de trabajo

**Estado del proyecto:** los tres documentos existen y están separados. `VISION.md` (~300 líneas) · `ESTRUCTURA.md` (~400) · `REQUISITOS.md` (~380). Nada más en la carpeta.

**Lo hecho hoy, en orden**: lectura de `raw/docs/plan-hermes.md` (1013 líneas) → auditoría de Runpod con 29 fuentes oficiales → medición del VPS (4.858 MB de RAM disponibles) → verificación de la documentación de Hermes (Docker, MCP, configuración, backends de terminal) y de Tailscale → 8 decisiones en formato Nygard → el diseño del sistema con sus 3 perfiles de ejecución y el contrato de tarea → el reset a tres documentos (VISIÓN / ESTRUCTURA / REQUISITOS) con el cuaderno digital como eje → la separación por criterio de pertenencia.

**Para retomar** (en este orden):
1. Leer **ESTRUCTURA.md** y **REQUISITOS.md** y anotar qué hay que corregir (VISION ya está revisado por el usuario).
2. Cerrar las 3 preguntas de producto de VISION §6.8: qué se automatiza primero · cómo se publica el cuaderno para Emilia · qué se hace con las fotos de obra.
3. Cerrar las decisiones de construcción de REQUISITOS §10 antes del tramo correspondiente (la primera, "dónde vive el modelo del agente", bloquea T1).
4. Arrancar el tramo **T0 · Inventario**: `P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py` (ya escrito, modo solo lectura) y el mismo relevamiento del equipo local.

**Estado del vault**: `proyectos/MVP_07-studio-os-sistema/` con 3 archivos · `scripts/studio_os_verificar_vps.py` + notas (listo para correr) · research de Runpod y este log como evidencia · **pendientes de `s`**: curaduría en `wiki/` (fichas de `fathom`, `postgres`, `tailscale` · renombrar RunPod → Runpod · actualizar la decisión de PI · cerrar la pregunta de Tailscale vs Cloudflare).

## Continuación 9 — VISION.md con el criterio del usuario (revisión conjunta)

**Correcciones del usuario sobre el documento:**
- **El problema**: *"las soluciones son de herramientas y no estamos hablando de sistemas"* (+ comunicación, auditabilidad y conocimiento accesible a un junior para que le cueste menos horas al senior). Se reescribió §1.3 y se agregó §1.5 con esa segunda pregunta como métrica.
- **Cuaderno digital**: es un **desarrollo interno**; tiene que verse **tipo libro, a pantalla completa, en horizontal**, para recorrer cómo se fue hablando y planificando; con **croquis escaneados**; **ligado a las entradas de la wiki** (es la capa visual de la wiki) más una interfaz gráfica auxiliar. Pasó a ser sección propia (§3).
- **Hermes**: se quería el **por qué no OpenClaw y por qué no Claude Code ni Codex** en la entrada de la decisión → §4.5. Aclaración de roles: **OpenCode + Antigravity** para el desarrollo propio, **Hermes de cara al cliente**.
- **Modelos**: hoy **OpenCode Go** (suscripción USD 10) → después **segunda instancia de Hermes en el estudio con Ollama** → después **OpenRouter** con API y precio definidos.
- **Stack**: **AutoCAD versión completa** (no LT) · **FreeCAD** como opción libre y siempre abierta (también BIM, corre en Linux en la otra PC de desarrollo) · **Rhino 8 vs Rhino 9 + Hops** · **Unreal** para lo custom y escalable a VR · Postgres + MySQL (Leantime) · Leantime como gestor de proyectos · alternativas libres para reuniones (Jitsi/LiveKit + faster-whisper ya instalado) y agenda self-hosted · Chatwoot, Instagram y WhatsApp **fuera por ahora** · imágenes: primero en la PC local (RX 570), después flujos en la infraestructura del estudio (cada 15 días) y cloud de Comfy o Runpod como excepción.
- **No entendía "secretos" ni "backup"**: se sacaron del stack de visión (son de ESTRUCTURA) y se dijo por qué.
- **Pidió diferenciar qué va en cada documento**: se agregó al inicio de los tres archivos la tabla de reparto (pregunta / qué contiene / qué no contiene) y en VISION §6.10 qué queda para ESTRUCTURA y REQUISITOS.
- **Pidió saber cuándo automatizar y cuándo no**: nueva §6.2 con la tabla de reparto y la frase *"se automatiza el trabajo, no la responsabilidad"*.
- **Telegram vs Discord**: nueva §6.5 con el criterio (Telegram = chat interno y avisos; Discord = material visual compartido) y la regla de no duplicar el mismo tema en las dos.

**Preguntas abiertas que quedaron (9 en total, §6.8)**: las nuevas son visión por computadora en obra, dónde viven las fotos de obra, Rhino 8 vs Rhino 9, y cómo se publica el cuaderno digital para que lo use Emilia sin conocimientos técnicos.

**Pendiente:** `ESTRUCTURA.md` (9 secciones, incluye ahora secretos, backup y acceso remoto) y después `REQUISITOS.md`. `00-filo-mvp_07.md` sigue como borrador técnico hasta que existan.

**Topics:** herramientas vs sistemas · conocimiento accesible al junior · cuaderno digital como capa visual de la wiki · Hermes vs OpenClaw vs Claude Code · AutoCAD completo vs LT · FreeCAD como alternativa libre en Linux · Rhino 8 vs 9 · Hops · Unreal hacia VR · Jitsi/LiveKit/faster-whisper · regla automatizar vs persona · Telegram vs Discord.

**Entidades:** Quartz · MkDocs · Nextcloud Pages · SilverBullet · Joplin · Jitsi · LiveKit · Radicale · Vikunja · Taiga · OpenProject · Directus · Baserow · NocoDB · Immich · exiftool · OpenCV · Qwen-VL · Anthropic Antigravity · Rhino 9.

**Hechos:** (1) el problema del estudio no es la falta de herramientas sino la falta de sistema, y el síntoma caro es el tiempo del senior que se gasta en transferencia; (2) el cuaderno digital solo tiene valor si está atado a la wiki: si vive aparte, vuelve a ser un archivo más; (3) cambiar de AutoCAD LT a la versión completa habilita la vía cloud oficial para el trabajo desatendido; (4) el agente se paga (modelo + GPU + mantenimiento), así que la automatización tiene que filtrarse por repetición, no por moda; (5) Telegram y Discord tienen las dos cosas (canales y temas/hilos): lo que las diferencia no es la función, es el tipo de conversación y el material que se comparte.

## Continuación 11 — IMPLEMENTACION-HERMES.md: la arquitectura traducida a piezas reales

**Pedido:** verificar contra la documentación oficial de Hermes qué de lo que habíamos escrito era cierto, y escribir el cuarto documento que mapea cada pieza de `ESTRUCTURA.md` a algo que Hermes ya hace (sin escribir código propio).

**Documento nuevo** `proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES.md` (569 líneas, 15 secciones):
1. Qué resuelve Hermes sin código · 2. Las 5 piezas a configurar (`config.yaml`, `SOUL.md`, `AGENTS.md`, skills, cron + webhooks) · 3. Flujo A, fuentes de Drive (A1 MCP oficial, A2 skill `google-workspace`, A3 espejo con rclone) · 4. Flujo B, mantener la wiki en 4 capas · 5. Flujo C, seguridad y mapeo A-D · 6. Flujo D, registro · 7. Flujo E, cuaderno y croquis · 8. Flujo F, compromisos · 9. Flujo G, webhooks y Fathom · 10. Flujo H, entregas y aprobaciones · 11. Lo que Hermes no hace · 12. Los 10 hallazgos que cambian el diseño · 13. `config.yaml` completo propuesto · 14. Cinco decisiones que se abren · 15. Referencias.

**Hallazgos que corrigen supuestos nuestros:**
- Hermes guarda en **SQLite `state.db` + FTS5**, no en Postgres. El registro del estudio (Postgres) es una pieza aparte: conviven, no se reemplazan.
- El backend **Docker saltea las aprobaciones de comandos peligrosos**: el gobierno A-D tiene que vivir en el toolset (qué herramientas existen) y no solo en `approvals`.
- La memoria persistente es chica a propósito: **2.200 caracteres** en `MEMORY.md` y **1.375** en `USER.md`. No es un lugar para el conocimiento del estudio; eso va a la wiki.
- **Un agente por `HERMES_HOME`**: el segundo perfil (Ollama en el estudio) necesita perfil propio, no un segundo proceso sobre el mismo home.
- Los jobs de cron **no pueden preguntar** (`cron_mode: deny`), corren en sesión nueva y **no recuerdan la corrida anterior**; la memoria persistente sí se carga.
- `read_file` convierte pdf/docx/xlsx/pptx/odt/epub y **avisa** cuando el PDF está escaneado, pero **no hace OCR**: el OCR sigue siendo un paso nuestro.
- `AGENTS.md` se descubre por subdirectorio (progresivo) y pasa por un escáner de inyección; `HERMES_WRITE_SAFE_ROOT=/opt/data` en la imagen oficial.
- Webhooks en el puerto **8644** con HMAC obligatorio, filtros, `coalesce`, `deliver_only` y toolset mínimo por ruta.
- El curador corre cada 168 h, `stale_after_days 14`, `archive_after_days 30`, **nunca borra** (archiva), deja ledger en `.curator_ledger.jsonl` y no toca skills de proyecto ni escritas a mano.

**Correcciones de configuración (claves inventadas → claves reales):** contra `/docs/reference/mcp-config-reference` se reemplazó `tools_allow` por `tools.include`, `auth: bearer` por `headers.Authorization: Bearer ${N8N_MCP_TOKEN}`, `trust: trusted` por `trust: untrusted` (valores válidos: `full` | `untrusted`), se agregó `auth: oauth` con PKCE para Drive y se quitó `soul:` (no existe: `SOUL.md` se carga si está en `HERMES_HOME`). Los secretos van por `${env:VAR}` desde `~/.hermes/.env`.

**Riesgo con fecha:** el MCP oficial de Google Drive (`https://drivemcp.googleapis.com/mcp/v1`) está en *Developer Preview* y desde el **11/11/2026** Google rechaza clientes OAuth no marcados como *"AI-powered agent"*. Queda como A3 (rclone) para el archivo y A1 para lo nuevo.

**Barrido de basura CJK en el vault** (pedido explícito): 20 caracteres sueltos en 8 archivos (`specs/`, `raw/`, `wiki/estudio/adrs/00-index.md`, `.opencode/plans/`), todos reemplazados por la palabra española que faltaba. Quedan solo dos usos legítimos: `改善` en [[wiki/glosario/conceptos/kaizen]] y la bibliografía en coreano de la transcripción del PDF de Gaudí (fidelidad de fuente, no se toca). También se corrigió un `sin|ComfyUI` que rompía una tabla en el research de FLUX.2.

**Enlaces:** `ESTRUCTURA.md` (encabezado) y `proyectos/00-index.md` apuntan al cuarto documento.

**Topics:** Hermes Agent como plataforma vs código propio · MCP oficial de Drive · OAuth 2.1 con PKCE · `AGENTS.md` progresivo · skills con `write_approval` · curador de memoria · webhooks con HMAC · aprobaciones por nivel de riesgo · SQLite vs Postgres · OCR como paso propio.

**Entidades:** Hermes Agent · Nous Research · `state.db` · FTS5 · Google Drive MCP · rclone · n8n MCP · Traefik · Docker Swarm · EasyPanel · Ollama · OpenRouter · Fathom · Quartz · Tailscale.

**Hechos:** (1) la arquitectura de `ESTRUCTURA.md` se sostiene, pero cambia de dueño: varias piezas que íbamos a construir ya existen como primitiva de Hermes y lo que falta es configuración; (2) el gobierno de riesgo no puede delegarse en `approvals` cuando el terminal corre en Docker, porque ese backend saltea la confirmación de comandos peligrosos; (3) la memoria del agente es deliberadamente corta, así que el conocimiento durable vive en la wiki y no en el prompt; (4) un cron que no puede preguntar obliga a que todo job termine en un mensaje o en un archivo, nunca en una espera; (5) la dependencia con fecha más urgente es el OAuth de Drive (11/11/2026), y por eso el espejo con rclone queda como base.

**Pendiente:** revisión del cuarto documento por el usuario · decidir entre SQLite de Hermes y Postgres propio para el registro · confirmar la variante de Drive (A1/A2/A3) · enlazar el documento desde `wiki/` cuando se cure · y sigue abierto el tramo T0 (`scripts/studio_os_verificar_vps.py`).

---

## Continuación 12 — La guía de lectura para explicar el sistema, y el agente con nombre y dirección (2026-10-30, tarde)

**Qué se hizo.** Cierre corto de la ronda: convertir los cuatro documentos en algo que se pueda **explicar** sin leerlos enteros, y dejar resuelto el nombre del agente.

1. **`GUIA-LECTURA.md`** (nuevo, 82 líneas, en `proyectos/MVP_07-studio-os-sistema/`): los cuatro documentos en una línea cada uno · **12 recorridos por tema**, cada uno con la sección, el ancla y la línea exacta (el sistema en 10 minutos · qué cambia en el día a día · qué es Hermes y qué no hace · dónde vive cada cosa · cómo se conectan AutoCAD/Rhino/ComfyUI · el cuaderno digital · quién decide · qué se compromete y cómo se mide · plazos · qué se configura el día uno · trazabilidad y Ley 24.335 · costos de nube y GPU) · el orden mínimo para leerlo todo en una hora y qué se puede saltear · **7 preguntas que va a hacer Emilia** con la respuesta corta y el lugar donde está · lo que todavía no está escrito · y el contexto que vive fuera de la carpeta.
2. **Nombre del agente:** se decidió usar **Hermes** como plataforma *y* como persona, con dirección **`hermes@agents.pitau.tech`**. Evita renombrar 122 menciones en los cuatro documentos y mantiene una sola palabra en la cabeza de la gente.
3. **DNS verificado, solo lectura:** `pitau.tech` **no tiene registros MX**, así que sumar el del subdominio no toca el correo existente del estudio · A `pitau.tech` = `89.117.73.109` · **`agents.pitau.tech` ya resuelve** al VPS por el comodín `*.pitau.tech` · los NS están en **Donweb**, no en Cloudflare, así que el MX se agrega en el panel del registrador y no pasa por proxy.
4. **Academia de Nico (pymbu), no extraíble:** `academy.pymbu.com` es un portal de membresía de **GoHighLevel** y responde un SPA. Se probaron cinco rutas de API (`/api/v1/posts/…`, `/api/posts/…`, `/membership/api/posts/…`, `/communities/…`, `/api/communities/posts/…`): todas caen en el catch-all que sirve el HTML. `?source=communities` es una pista que el cliente lee después de autenticar, no un permiso. No se intentó saltar el login. Queda que el usuario guarde la clase como PDF/HTML en `raw/pdf/` o la transcriba.

**Decisiones.** El agente se llama **Hermes** y su dirección es `hermes@agents.pitau.tech` · el correo del agente va al VPS y el correo del estudio no se migra · la explicación del sistema se hace con la guía, no leyendo los cuatro documentos.

**Correcciones.** Tres anclas de la guía usaban guion en lugar del **em dash (U+2014)** que realmente tienen los encabezados de `IMPLEMENTACION-HERMES` · el enlace a `specs/260909-esquema-mes1-60hs-studio-os-emilia` (que no existe) se reemplazó por `specs/261013-plan-cierre-mes1-calculadora-emilia` · `VISION.md` y `REQUISITOS.md` ahora nombran al cuarto documento, aunque la tabla de "tres documentos" queda igual · `proyectos/00-index.md` arranca la fila de MVP_07 con la guía.

**Verificación.** Script de enlaces sobre la guía (62 wikilinks), `VISION.md` (21) y `REQUISITOS.md` (16): **0 rotos**, contando archivos y anclas contra los encabezados reales.

**Topics:** explicar un sistema vs documentarlo · guía de lectura por audiencia · anclas de Obsidian y em dash · nombre de producto vs nombre de persona · correo self-hosted en subdominio · MX en el registrador · portales de membresía GoHighLevel · extracción de contenido detrás de login.

**Entidades:** Studio OS · Hermes · Emilia Pimenta · PITAUTECH · `agents.pitau.tech` · Donweb · GoHighLevel · LeadConnector · Pymbú Academy · Nico Dubois · Stalwart · `himalaya`.

**Hechos:** (1) el sistema ya está documentado; lo que faltaba era una ruta de lectura, y esa ruta es lo que convierte cuatro documentos en una explicación; (2) separar plataforma de persona no hizo falta: usar el mismo nombre evita 122 renombrados y no confunde a nadie; (3) `pitau.tech` sin MX significa que el correo del agente se puede montar sin riesgo para el correo del estudio; (4) el contenido de la academia no se puede leer desde afuera y no conviene intentarlo: el camino es que el alumno lo exporte; (5) los enlaces con ancla se rompen por un guion contra un em dash, y eso solo se detecta comparando contra los encabezados reales, no a ojo.

**Pendiente:** que el usuario guarde la primera clase como PDF/HTML (o la transcriba) para extraer el método de Nico · redactar los flujos de ComfyUI y de correo propio en `IMPLEMENTACION-HERMES` · sumar la sección de skills opcionales · ADR del correo propio (requiere `s`) · tramo T0 (`scripts/studio_os_verificar_vps.py`).
