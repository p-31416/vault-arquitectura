---
tipo: arquitectura
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [sistema, backend, obsidian, hermes, karpathy-llm-wiki, n8n, meetily, dashboard, humano-ia]
idioma: es
---

# Sistema backend vault — Obsidian como backend, Hermes como operador

> Diseño de sistema basado en 2 videos + el vault-arquitectura real. Reemplaza al agente del video por **Hermes en el VPS + n8n donde sea necesario**. Estructura canónica: VISION → ESTRUCTURA → REQUISITOS. No modifica [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] ni fundacionales; los extiende.
> Compañeros: [[specs/261110-manifiesto-fundacional-studio-os|manifiesto fundacional]] · [[specs/261111-convergencia-mvps-hermes|convergencia MVPs]].

## Fuentes analizadas hoy

| Video | Idea central | Qué aporta acá |
|---|---|---|
| [Construye tu backend con Obsidian (no un segundo cerebro) — Nico CMW](https://www.youtube.com/watch?v=XwEbK3JX5mc) | Obsidian como backend del sistema: las apps empujan info desde afuera, el vault la ordena y **sabe qué hacer con ella** | El dashboard, el inbox único, la captura como puerta de entrada |
| [La LLM Wiki de Karpathy — Articulator ES](https://www.youtube.com/watch?v=4U2FESAGoHg) | La IA compila fuentes en una wiki enlazada en vez de buscar en RAG sin estado: *Obsidian es el IDE; el LLM es el programador; la wiki es el código* | Arquitectura 3 capas + 3 operaciones (ingesta / consulta / lint) + índice + log append-only |

Hallazgo clave: **el vault-arquitectura ya cumple el patrón LLM Wiki**. `raw/` = fuentes inmutables, `wiki/` = compilada, `AGENTS.md` = esquema, `log.md` = append-only, lint trimestral en [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]. Lo que falta formalizar: las 3 operaciones como skills Hermes, el dashboard de humanos y el reemplazo de Fathom. Hermes Agent ya trae el patrón como skill oficial (verificado en el video 2).

---

# VISION

## 1 · Qué es

**El backend del estudio es el vault.** Obsidian deja de ser "app de notas" y pasa a ser el lugar por donde entra todo: fuentes de Telegram, transcripciones de reuniones, archivos de Drive, salidas de ComfyUI. El vault recibe, ficha, decide destino y dispara acción.

Sobre ese backend operan dos capas de dueños:

| Capa | Dueño | Formato | Ejemplo |
|---|---|---|---|
| **Humano** | Sol, Emilia, junior | wiki legible, dashboard visual, portal de renders, cuaderno | [[wiki/00-index|wiki]], dashboard HTML, lámina |
| **Máquina** | Hermes + n8n | frontmatter, JSON cache, SQLite, log crudo, raw | `raw/`, `state.db`, Qdrant, `research-cache/` |

**Principio humano/IA (regla dura, pedida explícitamente):** la UI existe **solo para los archivos que el humano alguna vez lee**. Los archivos de la IA quedan en formato de máquina, sin UI, sin esfuerzo de presentación. Un archivo o es contenido humano con formato Obsidian (frontmatter + wikilinks + tablas), o es insumo de IA crudo. La frontera entre ambos se declara en la estructura de carpetas.

## 2 · Para qué

1. **Probar herramientas y una nueva forma de trabajo** que sirva al estudio — cada herramienta entra con tarea de nivel A-B, deja rastro, y se queda si acelera diseño.
2. **Que el conocimiento compile en vez de acumularse**: cada fuente que entra deja ficha, actualiza índice y toca páginas de entidades y conceptos — la wiki crece con sentido, no como cementerio markdown.
3. **Que la máquina ejecute y el humano decida**: n8n y Hermes corren lo repetible; Sol aprueba criterio, firma y entrega.

## 3 · El problema que resuelve

1. Apps sueltas que se hablan por mano humana — Telegram, Drive, Fathom, Comfy, AutoCAD.
2. RAG sin estado: cada consulta arranca de cero — compilado una vez, el conocimiento persiste.
3. Pruebas IA sin rastro: sin semilla, log y ficha, el trabajo se repite.

## 4 · El norte

> Una fuente entra una sola vez. Salió ficha, índice y páginas actualizadas. Se consulta contra lo compilado, y el humano ve el rastro en el dashboard.

---

# ESTRUCTURA

## 1 · Las 3 capas adaptadas (ya existen, se formalizan)

| Capa Karpathy | En el vault | Regla |
|---|---|---|
| Fuentes en bruto | `raw/` (sessions, research, yt, docs, pdf) | Inmutable. La IA lee; el humano no abre. Formato de máquina |
| Wiki compilada | `wiki/` + `proyectos/` + `specs/` | La IA escribe con aprobación `s`. El humano lee y consulta. Formato Obsidian humano |
| Esquema | `AGENTS.md` + nomenclatura + frontmatter canónico | Lo editan humano + agente juntos |

## 2 · Las 3 operaciones (de hoy a skills Hermes)

| Operación | Hoy (OpenCode + Sol) | Mañana (Hermes skill) |
|---|---|---|
| **Ingesta** | fuente → ficha → índice → log (`@sherlock` + `@contenidos`) | skill `analizar-fuente` + cron 07:00; toca 10-15 archivos por fuente |
| **Consulta** | Obsidian search + grep + lectura dirigida | skill `diagnosticar-proyecto-arquitectonico`: responde contra wiki con citas |
| **Lint** | trimestral manual (pbk-agentes-vaultarq) | skill `lint-vault`: contradicciones, huérfanos, enlaces rotos, conceptos sin página |

## 3 · Dónde vive cada pieza

| Pieza | Ahora (local, esta PC) | Futuro (Hermes VPS N1) |
|---|---|---|
| Vault | `P:\...\vault-arquitectura` (git) | espejo canónico en VPS |
| Captura | Telegram grupo Fuentes → n8n Router → Sheet → raw | igual, n8n es la puerta |
| Reuniones | Fathom (nube, free tier) | **Meetily local** (ver §4) |
| Agente | OpenCode + Antigravity | Hermes `config.yaml` [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#13. Configuración propuesta (config.yaml del estudio)|IMPLEMENTACION §13]] |
| Dashboard | HTML estático local | mismo HTML servido en la red privada |
| Búsqueda | Obsidian + grep | + Qmd (buscador híbrido BM25+vectores, local, del artículo Karpathy) |
| ComfyUI | RX 570 local | MCP runner / pod nube |

## 4 · Reemplazo de Fathom — evaluación open source

Fathom es cloud-only (transcripts en servidores del vendor). Alternativas self-hosted verificadas hoy:

| Opción | Licencia | Cómo captura | Transcripción | Por qué sí / no |
|---|---|---|---|---|
| **Meetily Community** | MIT | sin bot, captura audio de sistema | Whisper/Parakeet local + resumen | **Recomendada como base**: $0, Windows ya, platform-agnostic. Su MCP/CLI/webhooks y diarización son Pro ($10/user/mes) — el MCP queda redundante con nuestro worker propio |
| Meet2Notes | open source | micro + loopback + import | local + **diarización incluida gratis** + RAG BGE-M3 | alternativa si la diarización es esencial sin pagar Pro |
| Verbatium | Elastic 2.0 | bot se une a Meet/Zoom | whisper.cpp local, resumen LLM propio | bot visible; bien si Meetily falla |
| heed | MIT | canales separados | Parakeet local | solo macOS/Linux |

**Decisión propuesta**: Fathom hoy (ya integrado en n8n) → **Meetily Community + worker propio** que lee su storage local y deja la ficha en el vault (el resumen lo hace nuestra skill `minuta-reunion` con los parámetros del estudio; su resumen nativo queda como segundo motor) → swap completo cuando el flujo iguale al de Fathom. Si la diarización (quién dijo qué) resulta esencial: Meet2Notes gratis o Meetily Pro $10/mes como excepción. Minuta pasa por la misma skill `preparar-compromisos`.

## 5 · MCPs instalados (inventario hoy)

| MCP | Estado | Rol en el sistema |
|---|---|---|
| n8n MCP (`n8n.pitau.tech/mcp-server/http`) | activo | Hermes crea/actualiza flujos sin abrir la app |
| ComfyUI MCP (`comfyui_comfy_cli`) | activo N3 | genera, valida contra `/object_info`, encola |
| Rhino MCP (reer-rhino-mcp) | activo N3 | modela, ejecuta GH, exporta |
| vault-mcp (leer/buscar/índice) | activo | acceso a memoria y cuaderno |
| AutoCAD MCP | MVP_01 | runner CAD |
| Drive MCP Google | planificado (OAuth agéntico, trampa 11/11) | lectura |
| registry MCP | planificado | registro Postgres de tareas/artefactos |

## 6 · El dashboard (estilo video, versión estudio)

HTML estático sobre el vault, **solo lee archivos humanos**, sin backend pesado:

```text
┌──────────────────────────────────────────────────────────────┐
│  IZQUIERDA              CENTRO                DERECHA        │
│  Tabs:                  Grafo del vault       Preview del   │
│  · Inbox (Fuentes-      (nodo=nota humana,    .md humano    │
│    Inbox pendientes)     arista=wikilink,                    │
│  · Digest (cron 07:00)   color por carpeta)                  │
│  · Reuniones (minutas)                                      │
│  · Proyectos (estado)                                       │
│  · Ask (después, Hermes)                                    │
└──────────────────────────────────────────────────────────────┘
```

* **Lee**: `wiki/**`, `proyectos/**/index`, minutas, digest, Fuentes-Inbox. Todo formato humano.
* **No toca**: `raw/`, cache JSON, `state.db`, logs — archivos de IA quedan sin UI por diseño.
* Respuesta con rastro: cuando llegue Ask, ilumina las páginas que usó — respuesta trazable, no caja negra.
* Construcción: HTML + JS vanilla + D3 sobre JSON generado por script del vault; el JSON de grafo es formato de máquina regenerable, nunca editado a mano.

## 7 · n8n donde sea necesario

n8n queda como el **determinista**: Router Telegram, Fathom/Meetily sync, cron digest 07:00, recordatorios de compromisos, avisos de salud del VPS. Hermes lo invoca por MCP y lo alimenta con contenido; la lógica conversacional y de criterio vive en Hermes.

---

# REQUISITOS

## RF (funcionales)

| # | Requisito | Criterio de aceptación |
|---|---|---|
| RF-1 | Toda fuente entra por un solo camino (Telegram/Drive/Meetily) y deja fila en inbox | 0 fuentes por chat privado de Sol |
| RF-2 | Toda ingesta produce ficha + actualiza índice + línea de log | fila nueva → 3 artefactos en ≤1 día |
| RF-3 | Consulta se responde contra wiki compilada con citas | respuesta lista páginas usadas |
| RF-4 | Lint mensual con reporte de contradicciones, huérfanos y huecos | reporte `raw/sessions/` con propuesta |
| RF-5 | Dashboard lee solo archivos humanos y refresca sin reinicio | cambio en wiki visible en recarga |
| RF-6 | Meetily produce transcripción + minuta local para 1 reunión de prueba | transcript + resumen en vault |
| RF-7 | Nivel de todo archivo declarado humano o máquina por carpeta | cero ambigüedad en árbol |

## RNF (no funcionales)

1. Local-primero: nube solo como excepción justificada (texto de transcript, nunca audio).
2. Trazabilidad: cada resultado con origen, versión y aprobación — [[proyectos/MVP_07-studio-os-sistema/VISION#1.4 El norte (el único criterio de éxito)|VISION §1.4]].
3. Formato Obsidian nativo para lo humano: frontmatter, wikilinks absolutos sin extensión, log más nuevo arriba.
4. Reproducibilidad: corrida repetible con mismos parámetros.

## Métricas

* Fuentes ingestadas vs fichas creadas: ≥ 95%
* Tiempo ingesta manual: de ~20 min hoy a < 5 min (Hermes propone, Sol aprueba)
* Páginas huérfanas tras lint: < 5%
* Reuniones con minuta ≤ 24h: 100%

## Qué NO decide este documento

* Modelo del cuaderno digital (queda en [[proyectos/MVP_07-studio-os-sistema/VISION#3 · El cuaderno digital|VISION §3]])
* Tailscale vs alternativas, backend Docker/SSH (ESTRUCTURA MVP_07)
* Migración completa Meetily — gate tras piloto
* Implementación del dashboard (scripts y comandos se entregan aparte con HITL: `scripts/<slug>.py` + `_explicado.py`)

---

## Próximos pasos (propongo orden)

1. **S1**: Meetily instalado en N3 + 1 reunión real de prueba → minuta al vault
2. **S1**: grafo JSON del vault vía script didáctico (`scripts/grafo-vault.py` + `_explicado.py`) — base del dashboard
3. **S2**: dashboard v1 (Inbox + Grafo + Preview) servido local
4. **S2**: skill `analizar-fuente` probada en OpenCode como se ejecutará en Hermes
5. **S3**: lint mensual automatizado + Qmd como búsqueda híbrida
6. **S4**: demo concurso Gaudí operando el sistema completo

¿Avanzo? s/N — si `s`, arranco por el script del grafo en formato didáctico y el piloto Meetily.
