---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [reunion, agenda, fuentes, agentes-telegram, cad, comfy, leantime, estudio, indice]
---

# Sesión 2026-10-21 (madrugada) — Índice de la reunión + documentos que registran la forma de trabajo

## Qué se pidió

Sol: **generar los documentos que registren esta forma de trabajo** y, aparte, **un solo documento** con el ítem de los temas a ver en la reunión (sesiones trabajadas, `.md` creados y dashboards) sobre fuentes, agentes Telegram, CAD/SET, Comfy, etc.

## Qué se hizo

### 1. El documento único de la reunión

`proyectos/STUDIO_OS-Emilia/presentacion/09-agenda-reunion-2026-10-21.md` (nuevo, 8 secciones):

| § | Tema | Contenido |
|---|---|---|
| 1 | **Fuentes** (AI×Gaudí) | 7 sesiones · 65 `.md` (32 fichas + 31 transcripciones + índice + plan + doc de ChatGPT) · 2 grafos |
| 2 | **Agentes Telegram** (n8n) | 6 sesiones · 20 `.md` (spec, MVP 06, 4 fichas técnicas, 8 de Studio OS) · 1 dashboard |
| 3 | **CAD / SET** (AutoCAD) | 6 sesiones · 22 `.md` (filo/spec/ft/log/ADR + SET_01/02/03 + playbooks + revisión + propuesta mes 2) · `dashboard-autocad.html` (50 KB) |
| 4 | **Comfy** (imagen + LoRA) | 5 sesiones · 28 `.md` (MVP 04 + 04.02 WF-01..06 + n_03 ControlNet + n_05 rhino-to-image + MVP 01/05) · `dashboard-comfy.html` (43 KB) |
| 5 | **Leantime** (tablero) | 5 sesiones · 7 `.md` (2 planes, cliente de horas, glosario, estado de carga) · `dashboard-mes1-emilia.html` |
| 6 | **Estudio** (propuestas) | 3 sesiones · 14 `.md` (plan, cuestionario, 8 de presentación, 3 diagramas, legal) · 2 dashboards |
| 7 | **Los 3 pendientes de Emilia** | `chat_id` (2 lugares) · dirección del estudio · compartir su calendario |
| 8 | **Orden sugerido (60 min)** | 0-5 contexto · 5-20 fuentes · 20-35 agentes · 35-50 CAD · 50-57 Comfy · 57-60 Leantime |

El inventario es **medido sobre el vault**, no de memoria: 88 sesiones en `raw/sessions/`, 10 specs, 5 dashboards HTML y 2 grafos VR.

### 2. Los documentos que registran la forma de trabajo (actualizados)

| Documento | Cambio |
|---|---|
| `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` | nueva **§2.b "la forma más simple: un documento compartido en el Drive"**: un solo `.md` (índice + por fuente metadata, extracto y figuras + punteros) en `OS-Emilia/AIxGaudi/Fuentes-Visibles/`; ella lo abre o adjunta en ChatGPT (web o celular); el vault sigue siendo el original y sus ediciones vuelven por la sincronización → importador → commit. El proyecto de ChatGPT queda como **envoltorio opcional**. Se recuerda que al Drive compartido van **extractos** (copyright), no las transcripciones enteras |
| `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` | **v2.1**: mapa de 9 workflows (los 3 nuevos de Emilia), diagrama con las dos ramas, y **§5.b** con el detalle de los flujos de Emilia (allowlist con `String()`, Redis `studio_os_emilia_<chat_id>`, memoria `studio_os_emilia`, credenciales, `Tool Agenda Emilia` directo, `agendar_presencial` sin `location`, eventos `7563141`/`7563142`/`7563143`, schedule `2527411`, y las pruebas end-to-end) |
| `proyectos/STUDIO_OS-Emilia/00-index.md` | sección **"Documentación vigente (21/10)"** con los 8 documentos de trabajo → se llega a todo desde la puerta del proyecto |

## Archivos del vault

- `proyectos/STUDIO_OS-Emilia/presentacion/09-agenda-reunion-2026-10-21.md` (nuevo)
- `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` (§2.b nueva)
- `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` (v2.1 + §5.b)
- `proyectos/STUDIO_OS-Emilia/00-index.md` (sección nueva)
- `log.md` (entrada del 21/10)

## Cerebro-digital

**Topics:** índice de reunión por temas · inventario de sesiones y `.md` · forma de trabajo de las fuentes (Doc compartido en Drive) · forma de trabajo de los agentes (un flujo por persona).

**Entidades:** `09-agenda-reunion-2026-10-21.md` · `raw/sessions/` (88) · `specs/` (10) · `proyectos/STUDIO_OS-Emilia/presentacion/` (9 documentos + 5 dashboards + 3 diagramas) · `dashboard-autocad.html` (50 KB) · `dashboard-comfy.html` (43 KB) · `dashboard-mes1-emilia.html` (32 KB) · `dashboard-estudio-os.html` (22 KB) · `dashboard-vault.html` (17 KB).

**Hechos verificados:** (1) el vault tiene 88 sesiones, 10 specs y 5 dashboards HTML de presentación; (2) el tema CAD/SET concentra 22 `.md` entre el replanteo de SET_01 (2 playbooks), SET_02 y SET_03, más la revisión del 22/10 y la propuesta de mes 2; (3) el tema Comfy concentra 28 `.md` entre MVP 04, la línea 04.02 (WF-01..06) y los workflows de ControlNet y rhino-to-image; (4) la forma más simple de compartir el corpus es **un `.md` en el Drive**, sin proyecto de ChatGPT y sin plan de pago; (5) al Drive compartido van extractos con atribución, no el texto completo (la transcripción entera se queda en `raw/`).
