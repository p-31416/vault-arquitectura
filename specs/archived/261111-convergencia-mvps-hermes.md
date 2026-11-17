---
tipo: arquitectura
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [studio-os, mvp_07, hermes, convergencia, mvps, mapa]
idioma: es
---

# Convergencia MVPs en Hermes — cómo todo confluye

> Pieza compañera de [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]. Describe cómo cada MVP y tema trabajado vive dentro de Hermes. Deja VISION y fundacionales intactos.

## 1. Puntos oficiales Hermes que sostienen la convergencia

Verificado base 2026-11-11 en `https://hermes-agent.nousresearch.com/docs/` — 200. Detalle verificado 2026-10-29 en [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#15. Referencias verificadas (29/10/2026)|IMPLEMENTACION §15]].

| Capacidad Hermes            | Documento oficial                                                                    | Uso en Studio OS                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Configuración `config.yaml` | `https://hermes-agent.nousresearch.com/docs/user-guide/configuration`                | Modelo, terminal Docker, aprobaciones, memoria, skills, cron en un solo archivo                               |
| Memoria persistente         | `https://hermes-agent.nousresearch.com/docs/user-guide/features/memory`              | `MEMORY.md` + `USER.md` + `session_search` FTS5. Memoria de trabajo, la wiki conserva conocimiento            |
| Skills                      | `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills`              | Procedimientos del estudio: auditar CAD, preparar entrega, experto-ComfyUI, curar cuaderno                    |
| Curador                     | `https://hermes-agent.nousresearch.com/docs/user-guide/features/curator`             | Mejora skills con aprobación, archiva lo obsoleto                                                             |
| Cron                        | `https://hermes-agent.nousresearch.com/docs/user-guide/features/cron`                | Digest 07:00, recordatorios con fecha, barridos. Sesión nueva autosuficiente, sin memoria de corrida anterior |
| Webhooks                    | `https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks`           | Reacción a eventos n8n, Fathom, Drive con HMAC y toolset mínimo                                               |
| Extracción documentos       | `https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction` | `read_file` convierte PDF, docx, xlsx, pptx, odt, epub. Avisa en escaneado y propone visión u OCR             |
| Archivos contexto           | `https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files`       | `SOUL.md` + `AGENTS.md` del vault como contexto vivo                                                          |
| Referencias contexto        | `https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references`  | Enlaces `vault://` y rutas `/opt/data/` dentro de prompts y skills                                            |
| MCP                         | `https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp`                 | Conexión a n8n, vault, registro, runner CAD Rhino Comfy                                                       |
| Seguridad                   | `https://hermes-agent.nousresearch.com/docs/user-guide/security`                     | Aprobaciones manual, deny list, allowlist, gobierno A-D                                                       |
| Drive MCP Google            | `https://developers.google.com/workspace/drive/api/guides/configure-mcp-server`      | Lectura Drive oficial con OAuth marcado como agente                                                           |

## 2. Mapa MVP por MVP hacia Hermes

| MVP / tema | Qué aporta al estudio | Dónde vive en Hermes | Pieza oficial |
|---|---|---|---|
| [[proyectos/MVP_01-dibujo_ia/readme-mvp_01|MVP_01 dibujo IA]] | Lenguaje natural hacia AutoCAD | Skill `auditar-documentacion-cad` + MCP runner hacia Core Console. Hermes interpreta, el runner ejecuta | Skills + MCP + Seguridad |
| [[proyectos/MVP_02-autocad-standards/readme-mvp_02|MVP_02 estándares AutoCAD]] | Layers, CTB, templates, regla de dibujo | Contexto `AGENTS.md` + skill `comparar-versiones-documentacion`. Regla versionada, no memoria suelta | Archivos contexto + Skills |
| [[proyectos/MVP_03-calhon-gest/readme-mvp_03|MVP_03 CalHon Gest]] + 03b | Honorarios y gestiones TAD, PyDO | Skill `preparar-entrega-proyecto` + MCP registro Postgres. Cálculo trazable con fecha y responsable | Cron + MCP + Extracción documentos |
| [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04 ComfyUI]] | Motor imagen local SD SDXL FLUX ControlNet | Skill `experto-comfyui` + MCP ComfyUI. Cada corrida con modelo, prompt, seed, sampler y `02-WF-log` según [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows]] | Skills + MCP + Referencias contexto |
| [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|MVP_05 Rhino MCP]] | Rhino Grasshopper por Hops sin pantalla | MCP runner + skill `validar-modelo-ifc`. Hermes prepara definición, Hops computa, Hermes registra | MCP + Seguridad |
| [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|MVP_06 agente voz]] | Telegram voz y texto hacia Cal.com y Fathom | MCP `n8n-official` hacia flujos `Agent Voz` y `Agenda Sub`. Hermes invoca, n8n ejecuta determinista | MCP + Webhooks + Cron |
| [[proyectos/MVP_07-studio-os-sistema/VISION|MVP_07 Studio OS]] | Sistema completo con memoria y reglas | `config.yaml` + `SOUL.md` + 5 piezas [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#2. Las cinco piezas que hay que configurar|IMPLEMENTACION §2]] | Configuración + Memoria + Curador |
| [[proyectos/concurso-gaudi-nexus/index|Concurso Gaudí Nexus]] | Banco de pruebas con 7 workflows y lámina A1 | Flujo transversal: Rhino hacia Comfy hacia portal hacia entrega. Jurado como checklist en skill | Skills + Extracción documentos + MCP |
| Cuaderno digital | Memoria de la casa tipo libro | Skill `curar-cuaderno` + publicación Quartz. Hermes escanea, indexa, etiqueta y devuelve | Memoria + Curador + Archivos contexto |
| Registro y grafo | Trazabilidad legal Ley 24.335 | `state.db` para turno + Postgres nuestro para negocio. Skill escribe versión plano, parámetros, aprobación | Seguridad + MCP |

## 3. Tres flujos que muestran la confluencia

**A. Reunión hacia compromiso:**
Fathom transcribe. Webhook despierta Hermes. Skill `preparar-compromisos` extrae qué entregar con fecha. Cron avisa por Telegram. Referencia: Webhooks + Cron + Skills.

**B. Croquis hacia render para concurso:**
Rhino MCP entrega geometría. ComfyUI MCP genera variantes con ControlNet. Portal publica con log. Skill `publicar-iteraciones` conserva semilla. Referencia: MCP + Skills + Referencias contexto.

**C. Conocimiento hacia junior:**
Wiki guarda procedimiento. `MEMORY.md` guarda preferencia durable. Curador propone mejora con `s`. Junior opera skill sin preguntar al senior. Referencia: Memoria + Curador + Archivos contexto.

## 4. Lo que Hermes orquesta y lo que sigue nuestro

Hermes orquesta, no modela. CAD, render, cuaderno como interfaz, portal, Postgres de negocio y sincronización Drive con rclone conservan implementación propia. Ver [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#11. Lo que Hermes no hace (y sigue siendo nuestro)|IMPLEMENTACION §11]].

## Referencias

* [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]
* [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]]
* [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]]
* [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]]
* [[specs/261110-manifiesto-fundacional-studio-os|Manifiesto fundacional]]
* [[specs/261102-plan-maestro-pi-por-temas|Plan maestro T1-T9]]
* [[specs/261102-system-overview-pi|System overview]]
