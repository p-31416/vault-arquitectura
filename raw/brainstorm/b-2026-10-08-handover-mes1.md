# Brainstorm — Handover Mes 1 · Studio OS · Emilia · 16/10/2026

> Fecha: 2026-10-08
> Solicitante: Sol
> Estado: **PROPUESTA CANDIDATA** (sin `s` aún — no se ejecuta nada del Bloque A/B/C hasta aprobación explícita)
> Guardada en `raw/brainstorm/` para lectura detenida antes de iterar o ejecutar.

---

## Frameworks activos

Doble Diamante (Discover→Define→Develop→Deliver, 8 días hasta 16/10) + SCAMPER sobre el entregable + JTBD desde el trabajo de Emilia el 16/10 + pensamiento lateral (analogías: el handover como *muestra de embarazo médico* — la prueba de que el sistema está vivo, no una promesa; inversión: ¿qué pasa si el Mes 2 no ocurre? → el handover pasa a ser portfolio público).

---

## BLOQUE A — Organización del vault para que "cuente" el Mes 1

### A.1 · Cambios de naming/index nivel 1 (5 acciones, cada una ≤1 click)

| # | Archivo | Acción | Razón (1 línea) |
|---|---|---|---|
| 1 | `00-index.md` (raíz) | Crear sección `## Mes 1 — Studio OS · entrega 16/10/2026` arriba del todo, antes de `## Wiki`, con 3 wikilinks: `[[proyectos/STUDIO_OS-Emilia/00-index]]`, `[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]`, `[[legal/contrato-studio-os-emilia-2026-09-24]]` | Cero clics desde la raíz al caso. Hoy la raíz solo apunta a `wiki/` y `proyectos/`. |
| 2 | `proyectos/STUDIO_OS-Emilia/00-index.md` | Crear bloque nuevo arriba `## Handover Mes 1 (16/10)` con índice a 5 entregables: deck HTML, one-pager, 4 Excalidraw, glosario transversal, `[[raw/reuniones]]` (carpeta con 11 reuniones) | Entry point único del caso. Hoy conviven cuestionario + plan v0.1 + playbooks + contrato; sin orden narrativo. |
| 3 | **Nuevo** `proyectos/STUDIO_OS-Emilia/00-handover-mes1.md` | Crear mapa de calor 1-página: 3 columnas (hecho / en curso / se ve el 16/10), con links a cada artefacto | Mapa mental para Sol antes de la demo: qué abrir, qué esconder, qué falta. |
| 4 | `wiki/00-index.md` | Crear bloque `## Glosario Mes 1 — conceptos activos en el caso` con 6 entradas priorizadas: `[[wiki/glosario/conceptos/meta-arquitecto]]`, `[[wiki/glosario/conceptos/hitl-human-in-the-loop]]`, `[[wiki/glosario/conceptos/design-thinking]]`, `[[wiki/glosario/conceptos/kanban]]`, `[[wiki/glosario/conceptos/lean]]`, `[[wiki/glosario/conceptos/design-sprint]]` | Muestra dominio metodológico al cliente, no solo ejecución operativa. |
| 5 | `proyectos/00-index.md` | Marcar los 4 `MVP_*` pre-Mes 1 con `estado: archivado` en frontmatter y mover `MVP_01-dibujo_ia`, `MVP_04-comfyui-arquitectura` a `proyectos/archived/2026-08-pre-studio-os/` | Limpia ruido pre-contrato Emilia. `proyectos/00-index.md` queda con foco en casos activos. |

### A.2 · Banner "Estado al 16/10" — doble capa (frontmatter + footer)

**Decisión:** ambas capas a la vez, no una u otra. La sinergia importa.

- **Capa 1 — Frontmatter** (machine-readable, queryable por `@vaultworm-arq`):

  ```yaml
  entregable_mes1: true
  fecha_handover: 2026-10-16
  visibilidad: cliente-studio-os
  ```

  Aplicar a los 12 archivos centrales: `proyectos/STUDIO_OS-Emilia/00-index`, `specs/260910-plan-trimestral-unificado-studio-os-emilia`, `specs/260909-esquema-mes1-60hs-studio-os-emilia`, 4 Excalidraw (frontmatter `.excalidraw.md`), contrato PDF (metadata), `legal/contrato-studio-studio-os-emilia-2026-09-24.md` (wrapper MD del PDF), deck HTML (`README.md` del handover), one-pager MD.

- **Capa 2 — Footer visible** (human-readable, una línea al final del `.md`):

  ```markdown
  > **Handover Mes 1 — Studio OS · Estado al 16/10/2026** · ver [[proyectos/STUDIO_OS-Emilia/00-handover-mes1]]
  ```

  Aplicar **solo** a los 5 documentos que se abren en vivo el 16/10, NO a los 14 specs. Contaminar todo mata la señal.

### A.3 · Diagramas Excalidraw — los 2 (máx 3) que faltan

Ya están: anillo trimestral, ROI, flujo vault, ROI payback. Faltan:

| # | Diagrama | Justificación | Cuándo |
|---|---|---|---|
| 1 | **Mapa del Handover** | Vista 1-página con los 5 entregables del 16/10, timeline horizontal 28/08 → 16/10, hits clave por semana, links a artefactos. **Es el que un partner externo miraría primero** — cuenta la historia visualmente en 5 segundos, sin entrar al vault. | Día 3 (10/10) |
| 2 | **Anatomía del Glosario Transversal** | Grafo de los 6-8 conceptos metodológicos clave con sus wikilinks: meta-arquitecto → hitl → design-thinking → kanban → lean → retrospectivas → kaizen → cinco-s. Demuestra coherencia teórica, no solo ejecución. | Día 5 (12/10) |
| 3 (opcional) | **Stack técnico del estudio** | Qué corre hoy: vault + 7 MCPs + ComfyUI + n8n + Leantime + Fathom + GHL. Muestra infraestructura operativa. **Candidato a eliminar si la demo en vivo funciona** (SCAMPER letra E: mostrar, no contar). | Día 5 (12/10) si hay margen |

### A.4 · Lo que sobra / ensucia (3 archivos, decisión: archivar con nota)

| Archivo | Destino | Nota de baja (1 línea) |
|---|---|---|
| `[[specs/260907-ghl-ingest-6-etapas]]` | → `specs/archived/2026-09-pre-firma/` | "Superado comercialmente por la propuesta firmada el 24/09; entra a Mes 3 si复活" |
| `[[specs/260907-telegram-vault]]` | → `specs/archived/2026-09-pre-firma/` | "Reemplazado por n8n (`[[specs/260924-plan-os-emilia-n8n]]`)" |
| `proyectos/MVP_01-dibujo_ia/`, `proyectos/MVP_04-comfyui-arquitectura/` | → `proyectos/archived/2026-08-pre-studio-os/` | "Sprints internos pre-contrato Emilia; conservan valor histórico, no protagonismo en Mes 1" |

**No archivar** (mantener vigentes pese a pendientes): `[[specs/260909-moodboard-vault-visual-local]]` y `[[specs/260909-plan-accion-web-research-moodboard-youtube]]` — unificarlos en `specs/260909-moodboard-unificado.md` o marcarlos como backlog Mes 2 explícito en frontmatter, sin mover de carpeta.

---

## BLOQUE B — Priorización de los 14 specs en 8 días

**Ordenado por impacto en la demo del 16/10, no por fecha de creación.** Resultado: **5 críticos · 7 diferibles · 2 archivar**.

### B.1 · Tabla de priorización

| # | Spec | Acción | Sesión (8 días) | Justificación de impacto |
|---|---|---|---|---|
| 6 | `[[specs/260909-esquema-mes1-60hs-studio-os-emilia]]` | **Crítico 16/10** | Día 1-2 (08-09/10) | Base narrativa del handover. Ya está `entregado`; verificar que cite plan trimestral + playbook Windows + 11 reuniones. |
| 11 | `[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]` | **Crítico 16/10** | Día 2 (09/10) | El norte del trimestre. Imprimir el diagrama de anillo Excalidraw para llevar a la mesa. |
| 14 | `[[specs/260929-alta-emilia-leantime]]` | **Crítico 16/10** | Día 3-4 (10-11/10) | MCP Leantime recién reparado (05/10): mostrar panel cargado con tareas reales es wow-factor accesible hoy. |
| 5 | `[[specs/260909-agente-reuniones-fathom-specs]]` | **Crítico 16/10** | Día 4 (11/10) | Prueba formal en vivo: 1 reunión de las 11 → SPEC → push a Leantime. Demuestra el loop completo, no un agente aislado. |
| 4 | `[[specs/260907-vault_cerebro]]` | **Crítico 16/10** | Día 5 (12/10) | Visión Mes 1 vigente. Verificar que las 4 semanas tengan estado real (no愿景) en `00-handover-mes1.md`. |
| 13 | `[[specs/260924-plan-os-emilia-n8n]]` | Diferible Mes 2 | Sprint 16/10–16/11 | §16.4-16.5 pendientes, pero la demo del 16/10 cierra con "esto entra Mes 2". No bloquea. |
| 1 | `[[specs/260907-ghl-extraccion-automatica]]` | Diferible Mes 2 | Sprint 16/10–16/11 | `transcribir_ghl.py` ya existe; solo falta E2E con ffmpeg + whisper. Backlog Mes 2. |
| 7 | `[[specs/260909-github-actions-agentes-online]]` | Diferible Mes 2 | Sprint 16/10–16/11 | Backlog intacto, no impacta demo. |
| 8 | `[[specs/260909-moodboard-vault-visual-local]]` | Diferible Mes 2 | Sprint 16/10–16/11 | Unificar con #9 antes de ejecutar. |
| 9 | `[[specs/260909-plan-accion-web-research-moodboard-youtube]]` | Diferible Mes 2 | Sprint 16/10–16/11 | Pilotos pendientes, no crítico. |
| 10 | `[[specs/260909-threads-sherlock-contenidos-moodboard]]` | Diferible Mes 2 | Sprint 16/10–16/11 | Threads 2-3 quedan Mes 2. |
| 12 | `[[specs/260917-backlog-nextcloud-vps-storage]]` | Diferible Mes 3 | — | Explícitamente Mes 3, mantener visible. |
| 2 | `[[specs/260907-ghl-ingest-6-etapas]]` | **Archivar** | Día 6 (13/10) | Superado por la propuesta comercial 24/09. → `specs/archived/2026-09-pre-firma/`. |
| 3 | `[[specs/260907-telegram-vault]]` | **Archivar** | Día 6 (13/10) | Reemplazado por n8n. → `specs/archived/2026-09-pre-firma/`. |

### B.2 · Carga semanal derivada (8 días)

| Día | Fecha | Sesión | Entregable |
|---|---|---|---|
| 1 | Hoy 08/10 (jue) | Inventario + clasificación 14 specs | Tabla B.1 ejecutada en `00-handover-mes1.md` |
| 2 | 09/10 (vie) | Refinar 5 críticos: #6, #11 | Banner `entregable_mes1: true` en frontmatter de los 12 archivos |
| 3 | 10/10 (sáb) | Diagrama **Mapa del Handover** Excalidraw + refinar `proyectos/STUDIO_OS-Emilia/00-index` | 2 nuevos `.excalidraw.md` |
| 4 | 11/10 (dom) | Demo en vivo del loop Fathom→SPEC→Leantime (probar con 1 reunión real) | Video interno de 5 min como backup |
| 5 | 12/10 (lun) | Diagrama **Anatomía Glosario** Excalidraw | Refinar wiki `00-index` |
| 6 | 13/10 (mar) | Archivar 2 specs obsoletas + mover `MVP_*` a `archived/` | `specs/archived/2026-09-pre-firma/` con 2 specs |
| 7 | 14/10 (mié) | **Rehearsal completo en seco** del bloque C | Notas de ajuste |
| 8 | 15/10 (jue) | Buffer + **envío del PDF + one-pager a Emilia 24h antes** | Mail con adjuntos |
| 9 | 16/10 (vie) | **Demo en vivo** | — |

---

## BLOQUE C — Deliverable concreto para la reunión del 16/10

### C.1 · Formato principal + alternativa

**Principal:** **Mixto** — deck HTML (narrativa) + walkthrough Obsidian en vivo (profundidad) + 1 demo en vivo del loop Fathom→SPEC→Leantime (credibilidad).

- **Duración:** 60-75 min total (50 min contenido + 15 min Q&A).
- **Por qué mixto:** deck solo = PPT sin sustancia; walkthrough solo = se pierde la narrativa; demo sola = frágil. El mixto cubre las 3 y el cliente ve el sistema correr, no un reporte sobre el sistema.

**Alternativa de backup** (si hay riesgo técnico el día): **walkthrough Obsidian puro** (sin demo en vivo) + envío del deck HTML por mail 24h antes + ofrecimiento de demo en vivo en sesión 2 (martes 20/10).

### C.2 · Secciones del entregable (en orden de aparición)

| # | Sección | Duración | Qué se muestra |
|---|---|---|---|
| 0 | **Apertura — gancho 30"** | 5 min | Ver C.3 |
| 1 | **El Mes 1 en 1 imagen** | 8 min | Diagrama **Anillo trimestral** Excalidraw, hitos semana por semana, 3 fechas clave (24/09 firma, 05/10 fix MCPs, 16/10 handover) |
| 2 | **Lo que ya corre** | 12 min | Stack operativo (vault + 7 MCPs + ComfyUI + n8n + Leantime + Fathom); abrir el vault en vivo: 1 entrada de glosario (`[[wiki/glosario/conceptos/meta-arquitecto]]`), 1 proyecto (`[[proyectos/STUDIO_OS-Emilia/00-index]]`), 1 spec (`[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]`) |
| 3 | **Demo en vivo** | 10 min | Loop Fathom→SPEC→Leantime: 1 reunión real → SPEC generado → push a Leantime → tarea visible. Mostrar la página de Leantime cargada. |
| 4 | **Lo que queda + Mes 2** | 10 min | Tabla B.1 proyectada: 5 críticos hechos, 7 diferibles agrupados por sprint, 2 archivados con nota. Proponer plan Mes 2 con el **ROI payback** Excalidraw. |
| 5 | **Cierre + entregable físico** | 5 min | Ver C.5 y C.6 |
| 6 | Q&A | 15 min | — |

### C.3 · Gancho 30 segundos (la apertura)

> "Emilia, hace 22 días firmamos un contrato trimestral con 3 ideas fuerza: que el estudio funcione como un sistema operativo, que cada reunión deje rastro, y que el conocimiento no dependa de una cabeza. Hoy te muestro las 3 cosas funcionando: el vault, los agentes y el panel. Después decidís si Mes 2 los activamos a full."

**Por qué funciona** (JTBD): el trabajo de Emilia el 16/10 es **decidir con confianza si renueva/amplía Mes 2**. El gancho le entrega las 3 evidencias en una frase, y el resto de la reunión es prueba, no promesa.

### C.4 · SCAMPER sobre el entregable (1 línea por letra)

- **S**ustituir el deck PPT por deck HTML con links internos al vault (navegable, no plano).
- **C**ombinar narrativa + walkthrough + demo en una sola sesión (no 3 reuniones separadas).
- **A**daptar la estructura del **Caso Fundador #01** (que ya existe) para consistencia metodológica con futuros casos.
- **M**odificar el centro de gravedad: de "presentar el Mes 1" → "validar el Mes 2 en 60 min" (lo que viene, no lo que fue).
- **P**oner otro uso: el handover sirve también de **portfolio público** (sanitizando nombres sensibles — versión paralela en `proyectos/portfolio/2026-q4-studio-os/`).
- **E**liminar la sección "stack técnico" del deck **si la demo en vivo funciona** (mostrar, no contar).
- **R**eordenar: el gancho va primero (no el contexto), el cierre va antes del Q&A para no quedar sin tiempo.

### C.5 · Qué se deja (cierre y siguiente paso concreto)

**Siguiente paso concreto (anunciar al final):** agendar **30 min el lunes 19/10** para kick-off Mes 2, con agenda cerrada: (a) sprint 1 cargado en Leantime, (b) §16.4-16.5 de n8n activado, (c) prueba E2E de `transcribir_ghl.py` con 1 reunión real.

**Decisión que se lleva Emilia:** confirmar o ajustar 3 palancas del Mes 2 — alcance (5 críticos heredados vs recortar), velocidad (sprint 2 semanas vs 4), profundidad (3 agentes full vs 1 agente + 2 en piloto).

### C.6 · Cómo cerrar con entregable físico

Emilia se va con 4 cosas en la mano (o en su mail al salir):

| # | Artefacto | Formato | Carpeta vault |
|---|---|---|---|
| 1 | **PDF del deck HTML** | 8-12 págs, branding estudio, generado día 8 | `proyectos/STUDIO_OS-Emilia/handover/16-10/deck-studio-os-mes1.pdf` |
| 2 | **One-pager Mes 2** | 1 hoja A4, vista 10.000 ft del sprint 1, ROI incluido | `proyectos/STUDIO_OS-Emilia/handover/16-10/one-pager-mes2.pdf` |
| 3 | **Carta de acceso al vault** | Link Obsidian Publish o instrucciones de clonado (ZIP sanitizado) | `proyectos/STUDIO_OS-Emilia/handover/16-10/acceso-vault.md` |
| 4 | **Contrato original** | Impreso, recordatorio del origen | ya existe en `legal/contrato-studio-os-emilia-2026-09-24.pdf` |

**Convención:** toda la carpeta `handover/16-10/` se sella el día 8 (15/10) a las 18h. Cambios después = v1.1 con nota.

---

## Resumen ejecutivo (1 párrafo)

**5 acciones de vault** (A.1), **doble capa de banner** (A.2), **2 Excalidraw nuevos** (A.3), **3 archivos a archivar** (A.4). **5 specs críticos + 7 diferibles + 2 a archivar** (B.1), distribuidos en **8 días con 1 rehearsal el día 7** (B.2). **Formato mixto de 60-75 min** con deck HTML + walkthrough Obsidian + demo en vivo del loop Fathom→SPEC→Leantime (C.1-C.2), **gancho de 30"** anclado a las 3 ideas fuerza del contrato (C.3), **4 artefactos físicos** para que Emilia se vaya con evidencia, no promesas (C.6), y **kick-off Mes 2 agendado el lunes 19/10** como siguiente paso concreto (C.5).

---

## Preguntas abiertas para Sol

1. ¿Aceptás el plan tal cual, o querés cambiar el alcance de algún Bloque?
2. ¿Empezamos hoy con Bloque A (organización vault) — cambios mecánicos, sin reinterpretar nada?
3. El Bloque C (formato de la reunión) tiene un trade-off: si la demo en vivo falla el 16/10, hay backup walkthrough Obsidian. ¿Te sirve esa jerarquía de formatos, o preferís otro fallback?
4. ¿Querés que archive MVP_01 y MVP_04 (Bloque A.4), o los dejamos donde están porque tienen valor de portfolio pre-Emilia?

---

*Generado por @brainstormy — 2026-10-08 America/Argentina/Buenos_Aires — pendiente `s` de Sol para ejecutar.*
