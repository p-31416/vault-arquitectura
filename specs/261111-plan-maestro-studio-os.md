---
tipo: plan-maestro
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-12
tags: [plan-maestro, studio-os, asistente-sintetico, hermes, generico, piloto-emilia, 35d, 2-dias]
idioma: es
---

# Plan maestro Studio OS — el asistente sintético del arquitecto

> **El documento único.** VISION, ESTRUCTURA y REQUISITOS son genéricos del asistente sintético del arquitecto. La instancia concreta (piloto Emilia, sprint 2 días, calendario) vive en Operación. Canon intacto: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]].
> **Instancia piloto (nov 2026)**: estudio de Emilia Pimenta. Los nombres concretos viven en Operación; el resto vale para cualquier arquitecto.
> Absorbió (archivados en `specs/archived/`): manifiesto fundacional · filosofía Hermes · filo-vault-v2 · sistema filosófico práctico · convergencia MVPs · backend vault · dos caminos · plan migración · hermes agentes y usos.

---

# VISION — el asistente sintético del arquitecto

## 1 · Qué es

**El asistente sintético del arquitecto**: un agente (Hermes) operando en el VPS del estudio, al que el arquitecto le habla por Telegram desde el celular — con la computadora apagada si quiere — y que ejecuta por él el trabajo repetible del estudio: agenda reuniones, transcribe y resume con contexto, redacta minutas y mails, re-rende imágenes con indicación, audita planos AutoCAD, computa partidas y prepara entregas.

**La tesis** ([[raw/sessions/2026-11-11-sesion-fuerza-motriz-arquitectura|sesión fuerza motriz]]):

> *"La fuerza motriz la pone la ejecución del humano. Esta es mi gran tesis de arquitectura… Nosotros lo que necesitamos es la arquitectura de la arquitectura."*

> *"Tener todo el sistema funcionando: los archivos que va a leer la IA, los scripts de Python que necesite, los flujos de n8n. Esas van a ser bracitos de nuestra gente. Yo solo tengo que ver cómo se va construyendo gráficamente."*

Los estudios suman IA como botón aislado; esa capa ya es norma. La ventaja avanza en otro plano: **sistema con memoria, registro y reglas** — un estudio chico trabajando como uno grande, con el costo de uno chico. Menos del 20% del sector aplica IA en flujo real; la ventana permanece abierta para quien llega con sistema auditable. ComfyUI y n8n avanzan hacia commodity; el valor migra a **diseñar el sistema que elige, valida, registra y mantiene**.

**El manifiesto** (3 líneas, ensayo [[specs/archived/261029-filosofia-hermes|filosofía Hermes]]):

1. Automatizamos el trabajo repetido, honramos la responsabilidad del diseño.
2. Cada hora liberada vuelve al tablero: más diseño, mejor obra.
3. Memoria propia, criterio propio, tiempo propio: estudio que diseña su futuro.

**El filtro tren / hype / aporte** — criterio único: *un resultado suma cuando deja rastro explicable y acelera el paso de junior a senior*. Tren: se incorpora con skill y registro · Hype: queda en observación · Aporte: parámetros versionados, portal, memoria curada.

## 2 · Para quién

| Actor | Qué obtiene |
|---|---|
| **El arquitecto titular** | asistente que responde por Telegram en su idioma; opera desde el celular sin abrir n8n ni aprender nada técnico |
| **PITAUTECH** (operadora del sistema) | instala, mantiene y evoluciona; acceso de administración con acciones registradas |
| **El junior / dibujante** (capa operador) | agente local junto a sus herramientas — ver §6 |
| **El estudio** | conocimiento de la casa en el vault, trazable y auditable |

**Quién recibe la instancia piloto**: un estudio de 2-4 personas sin equipo técnico interno. La escala no cambia el diseño: un asistente más = skills y un runtime.

## 3 · El problema

Un estudio chico pierde el día en trabajo que la máquina puede ejecutar: agendar y confirmar, pasar de audio a minuta, escribir el mail, esperar renders, revisar capas de DWG a mano, computar partidas a mano, recordar compromisos. Cada tarea es chota de 20 minutos; juntas comen la jornada. Y nada deja rastro: qué se decidió, qué versión, quién aprobó. El conocimiento vive en la cabeza de los seniors y se va con ellos.

## 4 · El norte

> El arquitecto pide por Telegram; el asistente prepara y ejecuta lo verificable; toda decisión y toda entrega quedan con rastro; la computadora del arquitecto puede estar apagada.

## 5 · Principios fijos

1. **Máquina ejecuta, humano decide y firma.** Niveles: A lectura auto · B generación aislada auto · C modificación con aprobación · D publicación externa con aprobación explícita ([[proyectos/MVP_07-studio-os-sistema/VISION#6.6 Los niveles de riesgo (la regla de gobierno)|VISION §6.6]]). El envío de mails lo hace la persona; el plano lo firma el arquitecto (Ley 24.335).
2. **Formato humano vs formato de máquina.** La UI existe solo para lo que el humano lee. Archivo humano = Obsidian (frontmatter + wikilinks + tablas). Archivo de IA = crudo (raw/, cache JSON, SQLite, logs) — sin UI, por diseño. La frontera se declara por carpeta.
3. **Patrón Karpathy (LLM Wiki)** — *Obsidian es el IDE; el LLM es el programador; la wiki es el código*:
   * 3 capas: `raw/` fuentes inmutables → `wiki/` compilada → `AGENTS.md` esquema
   * 3 operaciones: **ingesta** (fuente → ficha → índice → log, toca 10-15 archivos) · **consulta** (contra lo compilado, con citas) · **lint** (contradicciones, huérfanos, huecos)
   * La wiki es **fractal** (cada nodo se desmenuza en hijos del mismo tipo), **iterable** (mismo pipeline para 1 o 100 fuentes) y **rizomática** (se entra por cualquier punto — un render, un plano, una reunión). Fuente: video [LLM Wiki de Karpathy](https://www.youtube.com/watch?v=4U2FESAGoHg) + [[specs/archived/261029-filo-vault-v2|filo-vault-v2]].
4. **Sin RAG.** La wiki es la memoria compilada: se consulta por índice contra páginas enteras, no por fragmentos. **Qmd** (buscador híbrido local palabras+vectores) entra opcional cuando el vault crezca.
5. **Corte por vía** ([[specs/archived/261029-filo-vault-v2|filo-vault-v2 §1.6]]): **determinista sin IA** (archivar, indexar, auditar — scripts) · **agéntico con `s`** (buscar, sintetizar, proponer) · **contractual humano siempre** (publicar, enviar, sobrescribir).
6. **Local primero; nube como excepción justificada** (texto de transcript, render on-demand) — nunca audio grabado sin condiciones, nunca planos crudos a terceros.
7. **Libre primero.** Jitsi, Meetily Community, Meet2Notes, ezdxf, n8n self-hosted; pago solo excepción con justificación ([[proyectos/MVP_07-studio-os-sistema/VISION#5 · El stack delineado|VISION §5]]). Matiz: **Obsidian es el visor, no el formato** — el vault es markdown + git (formato abierto, reemplazable por cualquier editor); lo que es FLOSS es el dato.
8. **Trazabilidad total.** De qué archivo salió, con qué versión, con qué parámetros, quién aprobó.
9. **El estándar hace posible el cómputo.** MVP_02 (bloques con atributos, capas) es la condición del cómputo automático.

## 6 · Las dos capas del estudio + el recorrido de 10 pasos

| | **Capa operador** (dibujante, junior) | **Capa arquitecto** (titular) |
|---|---|---|
| Relación con la máquina | toda la jornada en su PC | arriba, decide, a veces lejos |
| Asistente | **agente local** junto a su AutoCAD/Rhino/Comfy | **agente cloud** (Hermes VPS + n8n): celular, PC apagada, 24/7 |
| Qué hace el asistente | ejecuta con él: audita mientras dibuja, computa, compara versiones | ejecuta para él: agenda, minutas, informes, entregas, recordatorios |

**El contrato es uno**: las mismas skills `.md` corren en ambas capas — cambia el runtime, no el procedimiento. Extrapolable a un estudio con N humanos + N asistentes sintéticos.

El recorrido completo del estudio con el sistema:

| Paso | Sistema | Decide |
|---|---|---|
| 1 Entra cliente | mini CRM: hoja con nombre, contacto, mail | titular |
| 2 Reunión | graba, agrupa meetings repetidos, minuta con decisiones | titular |
| 3 Compromisos | cada compromiso con entrega y fecha, aviso previo, mail armado | titular (manda persona) |
| 4 Cuaderno | escalas, croquis, resultados IA con referencia | arquitecto |
| 5 Planos | auditoría DWG clasificada, original intacto | arquitecto (D) |
| 6 Modelo 3D | inspección, medición, Hops headless, exportación | arquitecto |
| 7 Render IA | variantes con semilla, iteraciones en portal | arquitecto |
| 8 Obra | fotos indexadas con tags, incidencias con resolución | arquitecto |
| 9 Entregas | paquete con índice, envío por persona, registro con fecha | arquitecto (D) |
| 10 Memoria | cada sesión deja entidades, topics, hechos; mejora con aprobación | estudio |

## 7 · Las capacidades (genéricas)

1. **Re-rendir con indicación**: render + texto/marca → 2-3 variantes con semilla y parámetros
2. **Informe AutoCAD**: DWG subido → auditoría server-side (capas, escalas, xrefs, bloques, estándares MVP_02) → informe PDF — sin AutoCAD y sin la PC del arquitecto encendida
3. **Cómputos**: bloques con atributos → tabla de partidas (unidades, m²) → planilla
4. **Impresión / entrega**: PDF con formato de impresión para gestoría o imprenta (impresora propia: mes 2+)
5. **El bot pide la reunión**: agenda con invitación por mail (Cal.com)
6. **Transcripción + minuta con contexto**: audio al bot (o Meet grabada) → STT server-side → resumen con tipo **interna vs cliente** → minuta + borrador de mail
7. **PC apagada**: STT y auditoría corren en servidor; la PC solo entra cuando el arquitecto quiere

## 7bis · AI-first en arquitectura

AI-first en arquitectura significa diseñar el estudio alrededor del colaborador sintético, con humano al mando.

Primero el sistema que propone, luego la herramienta que ejecuta, siempre con firma humana.

El colaborador trae mano ilimitada que propone opciones y sostiene trazabilidad. El humano trae dirección, criterio y firma. Hermes trae ejecución y memoria.

Manifestaciones por momento de ejercicio:

* Tablero: Sol esboza intención, el colaborador devuelve tres rumbos con referentes, Sol elige.
* Planos: el colaborador chequea capas y rótulos, Hermes registra hash y fecha, el arquitecto firma documento legal Ley 24.335.
* Modelo: el colaborador parametriza, Hermes versiona con provenance, el arquitecto valida.
* Render: el colaborador sugiere prompt por modelo, Hermes encola con semilla, el arquitecto cura keeper en portal.
* Obra: foto y cómputo enlazados a `file_ref`, el colaborador alerta desvíos, el arquitecto decide.
* Entrega: paquete trazable con índice y registro, envío por persona.
* Memoria: cada sesión deja entidades y hechos, el colaborador propone síntesis, el estudio firma lo memorable.

Estudio chico con costo chico y madurez de oficina grande: trazabilidad total, checklist CABA conurbano Europa, costo visible por ejecución.

## 8 · Las herramientas del asistente (qué hace / qué no / nivel)

| # | Herramienta | Qué hace | Qué NO hace | Nivel |
|---|---|---|---|---|
| 1 | Telegram (bot propio) | la puerta: habla, audio, fotos, DWG, avisos | no almacén eterno | A-C |
| 2 | Agenda Cal.com | agenda, mueve, cancela, lista, invitación | sin email ni confirmación no agenda | C |
| 3 | STT server-side | audio → texto (free → pago con swap de 1 nodo) | no graba sola; requiere el audio | B |
| 4 | Transcripción Meet (Fathom hoy) | transcripts de reuniones Meet | no reemplaza audio propio | B |
| 5 | Minuta con contexto | transcript → resumen por tipo → minuta + borrador mail | no manda el mail | B / D mail |
| 6 | Redacción correo | mail con formato del estudio | persona lo envía | D |
| 7 | Render con indicación | variantes con semilla (API imagen) | no elige keeper | B |
| 8 | Portal iteraciones | página con parámetros y semilla | nada público | B |
| 9 | Auditoría DWG (dwg-worker) | informe capas/escalas/xrefs/bloques/estándares | no toca el original | B |
| 10 | Cómputos | partidas desde bloques estandarizados | avisa qué falta estandarizar | B |
| 11 | Impresión / PDF | PDF listo para gestoría | no imprime en impresora propia al inicio | C |
| 12 | Compromisos + cron | qué entregar con fecha; avisa antes de vencer; digest 07:00 | no reagenda solo | B |
| 13 | Memoria (vault + registro) | fichas, minutas, versiones, aprobaciones por proyecto | la memoria del asistente es de trabajo; el conocimiento vive en el vault | A |
| 14 | Mini CRM (hoja + contactos con contexto) | alta y seguimiento de clientes; ficha de quién es quién | no es CRM completo | B |

## 9 · Reuniones abiertas (no solo Meet)

* **Jitsi vía Cal.com**: app "Jitsi Video" del app store (free ≤25 usuarios/mes, verificada) → ubicación Jitsi → link auto-generado en la invitación. Cero código. Ad-hoc: `https://meet.jit.si/<estudio>-<random>` al chat.
* **Meetily Community (gratis, MIT)**: graba audio de sistema de cualquier app (Jitsi, Zoom, teléfono) y transcribe local. Su MCP/CLI/webhooks/diarización son Pro ($10/user/mes) — **el MCP queda redundante con nuestro worker propio** que lee el storage local y deja la ficha en el vault; el resumen lo hace nuestra skill `minuta-reunion`.
* **Diarización** (quién dijo qué): Meet2Notes gratis (incluida + RAG BGE-M3) o Meetily Pro $10 como excepción; fallback: etiquetado manual en 2 clics.
* Límite honesto: el asistente arma la reunión y procesa el audio después — no entra a la llamada. Jitsi self-hosted espera (VPS compartido queda corto para video).

---

# ESTRUCTURA — el asistente sintético del arquitecto

## 1 · Dónde vive cada pieza

```text
┌────────────────────────────────────────────────────────────────┐
│ N1 · VPS del estudio (siempre encendido)                        │
│  · Hermes (bot Telegram propio, memoria, skills, cron)          │
│  · n8n (flujos deterministas: agenda, STT, mail, avisos)        │
│  · dwg-worker (ezdxf: auditoría + cómputos)                     │
│  · Postgres (registro) · hoja (CRM + inbox)                     │
├────────────────────────────────────────────────────────────────┤
│ N2 · PC del estudio (opcional, cuando el arquitecto quiere)     │
│  · sube DWG/renders/audio por Telegram; nada corre obligatorio │
├────────────────────────────────────────────────────────────────┤
│ N3 · Banco de pruebas del operador (PITAUTECH)                  │
│  · OpenCode + Antigravity · ComfyUI · vault desarrollo          │
├────────────────────────────────────────────────────────────────┤
│ Nube (excepción justificada, texto-only en lo sensible)         │
│  · STT · API imagen render · transcripción Meet · videollamada  │
│  · Cal.com · Gmail                                              │
└────────────────────────────────────────────────────────────────┘
```

## 2 · Conexiones y contrato

```text
Arquitecto → Telegram → Hermes
   Hermes ─MCP n8n─► agenda · STT · mail · avisos · health
   Hermes ─MCP dwg──► auditoría DWG · cómputos
   Hermes ─MCP vault► memoria · fichas · skills · log
   Hermes ─API──────► render (API imagen)
   n8n ──webhook────► Hermes (STT listo → armado de minuta)
   Hermes ─cron 07:00► digest + recordatorios
```

**Contrato sobre-de-tarea formal**: entra {tipo, datos, proyecto, nivel}; sale {resultado, rastro, registro}. El archivo viaja como `file_ref` con hash verificable · el verbo define el riesgo mínimo (`publish` siempre D) · `idem_key` da idempotencia · la respuesta trae `provenance` completa (versión entrada, herramienta, parámetros, tiempos, costo) · el registro previo habilita la ejecución. Hermes no sabe qué executor corre: cambia el perfil, el contrato queda.

## 3 · Integraciones (elegida / alternativa / cuándo cambiar)

| Integración | Elegida | Alternativa | Cambiar cuando |
|---|---|---|---|
| Bot Telegram | token nuevo propio del estudio | reusar bot de pruebas (descartado: conflicto de trigger) | — |
| Agenda | Cal.com vía subflujo | Cal.com self-hosted | usuarios múltiples |
| Videollamada | **Jitsi Video** en Cal.com (app store, free ≤25 usuarios/mes) → link auto-generado | meet.jit.si directo para ad-hoc | self-host Jitsi si el volumen lo pide |
| STT | free primero (Gemini audio) | whisper-large-v3-turbo (swap 1 nodo) | free insuficiente |
| Render | API imagen free (Pollinations flux) | Runpod Secure pod on-demand | calidad/consistencia alta |
| DWG | ezdxf en dwg-worker | AutoCAD Core Console en N2 | features de AutoCAD |
| Reuniones Meet | transcripción existente (Fathom hoy) | Meetily Community + worker propio | cuando el flujo propio iguale al actual |
| Mail | Gmail API vía n8n | nodo email n8n · correo self-hosted | si la cuenta duela |
| CRM | hoja (Google Sheet hoy) | Baserow | la hoja duela |

**Balance FLOSS declarado**: núcleo 100% libre — Hermes (MIT) · n8n self-hosted · Jitsi (Apache) · Meetily Community (MIT) · Meet2Notes · ezdxf (MIT) · Postgres · vault markdown+git · Obsidian como visor reemplazable. **Excepciones transitorias con destino libre declarado**: transcripción Meet → Meetily Community · hoja → Baserow · Gmail → correo self-hosted · STT free → whisper.cpp local (Meetily) · render API → ComfyUI local en capa operador.

## 4 · Las 5 piezas de configuración

1. **`config.yaml`** — terminal Docker, `approvals: manual` + `cron_mode: deny`, memoria con `write_approval`, skills versionadas, curador 168h, MCP n8n/vault/dwg `trust: untrusted`. **Completo en Operación §5** de este documento.
2. **`SOUL.md`** — identidad del estudio: idioma y tono propios, pide email antes de agendar, cita lo entendido, jamás inventa disponibilidad, C-D piden aprobación. Contenido en Operación §5.
3. **Bot Telegram nuevo** — token a `~/.hermes/.env`, nunca en repo.
4. **Skills** (7 de arranque): `gestionar-clientes` · `preparar-compromisos` · `redactar-correo-cliente` · `minuta-reunion` · `rendir-con-indicacion` · `auditar-documentacion-cad` · `computar-partidas`. Se escriben en el vault (N3), se prueban con OpenCode, viajan aprobadas al VPS.
5. **Cron + webhooks** — digest 07:00 + recordatorios; webhook n8n al terminar STT.

## 5 · Seguridad, secretos y niveles

* Secretos solo en `~/.hermes/.env` y credenciales n8n — nunca en repos ni prompts.
* Aprobaciones `manual` desde el día uno; cron sin capacidad de preguntar (`cron_mode: deny`) — [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#12. Hallazgos que cambian el diseño|IMPLEMENTACION §12]].
* Niveles por operación: A lectura · B generación aislada · C modificación con aprobación · D publicación externa con aprobación explícita.
* El DWG se procesa con reporte, el original queda intacto (hash verificado); lo que sale a nube es texto de transcript y prompts de render, nunca planos crudos a terceros sin condiciones.

## 6 · El equipo de Bots del estudio (Pipi) + los curadores del taller

Hermes oficialmente soporta **perfiles/Bots/subagentes** (verificado: [[specs/archived/261111-hermes-agentes-usos-estudio|hermes-agentes-usos]]). Un solo Hermes instalado; el equipo son **perfiles** — la regla dura de la doc: dos procesos jamás comparten el mismo perfil.

| Bot (perfil Hermes) | Rol | Skills | Conecta |
|---|---|---|---|
| `default` = **PI Manager** | coordina, atiende el gateway del estudio, delega | todas las de arranque | todo |
| **pipi-docs** | curaduría y memoria (el pipeline de los curadores, en producción) | `analizar-fuente` · `curar-cuaderno` · `diagnosticar-proyecto` | MCP vault + Drive + web · cron ingesta |
| **pipi-pm** | agenda y compromisos | `gestionar-clientes` · `preparar-compromisos` · `redactar-correo` | MCP n8n (Cal, STT, mail) · cron digest |
| **pipi-cad** | planos | `auditar-documentacion-cad` · `computar-partidas` · `comparar-versiones` | MCP dwg-worker · luego N2 AutoCAD por Tailscale |
| **pipi-visual** | imagen y render | `rendir-con-indicacion` · `experto-comfyui` | MCP ComfyUI (Tailscale/pod/API — ver §7) |
| **pipi-bim** | BIM (futuro, cuando haya IFC real) | `validar-modelo-ifc` | FreeCAD + IfcOpenShell |
| **pipi-ideas** | divergencia creativa ("que me siga la corriente") | brainstorm/SCAMPER | modelo barato fijado por Bot (Bot Mode permite pin de modelo por perfil) |

**Los 4 curadores** (Sherlock busca · Brainstormy diverge · Contenidos formatea · Vaultworm conecta) son **subagentes de OpenCode en N3, el taller de Sol** — jamás corren en el VPS de producción. En producción, pipi-docs ejecuta el mismo procedimiento escrito como skills.

**Subagentes efímeros** (`delegate_task`): trabajo paralelo dentro de una tarea (comparar 5 variantes, auditar 3 DWG a la vez).

## 7 · ComfyUI — las 3 rutas de conexión

| Ruta | Cómo | Cuándo conviene | Costo |
|---|---|---|---|
| **1 · Tailscale + N2/N3 con GPU** | ComfyUI con su MCP en la máquina con GPU; el bot la alcanza por red privada | SD1.5/SDXL en 8 GB; workflow versionado con ControlNet/LoRA | $0, usa lo existente |
| **2 · Pod on-demand (Runpod Secure)** | pod con GPU grande al pedir; material derivado no sensible | FLUX.2 9B, video por lote, consistencia alta | por hora (excepción ya decidida) |
| **3 · API imagen free (Pollinations)** | HTTP directo desde n8n/Hermes | variantes rápidas "cambiá el cielo" sin ControlNet fino | $0, calidad menor |

Decisión por tipo de pedido: variante simple → ruta 3 · workflow versionado → ruta 1 si hay GPU, si no ruta 2 · siempre con semilla y log (`reglas-workflows-comfy`). El MCP de ComfyUI ya validado en N3 (`comfyui_comfy_cli`) es el mismo cliente en las 3 rutas: cambia el endpoint, el contrato queda.

## 8 · Inventario MCPs

| MCP | Estado | Rol |
|---|---|---|
| n8n MCP (`n8n.pitau.tech/mcp-server/http`) | activo | Hermes crea/actualiza flujos sin abrir la app |
| ComfyUI MCP (`comfyui_comfy_cli`) | activo N3 | genera, valida contra `/object_info`, encola |
| Rhino MCP (reer-rhino-mcp) | activo N3 | modela, ejecuta GH, exporta |
| vault-mcp (leer/buscar/índice) | activo | acceso a memoria y cuaderno |
| AutoCAD MCP | MVP_01 | runner CAD |
| Drive MCP Google | planificado (OAuth agéntico) | lectura |
| dwg-worker MCP | S3 del sprint | auditoría + cómputos |
| registry MCP | planificado | registro Postgres de tareas/artefactos |

## 9 · El mapa MVPs → Hermes

| MVP | Aporta | Vive en Hermes como |
|---|---|---|
| MVP_01 dibujo IA | lenguaje natural → AutoCAD | skills pipi-cad + MCP runner |
| MVP_02 estándares | layers, CTB, bloques con atributos | contexto `AGENTS.md` + estándar del cómputo |
| MVP_03/03b CalHon | honorarios y gestiones | skill `preparar-entrega` + registro Postgres |
| MVP_04 ComfyUI | motor imagen/video local | skills pipi-visual + MCP ComfyUI (3 rutas) |
| MVP_05 Rhino MCP | Rhino/Grasshopper por Hops | skills pipi-cad + MCP runner |
| MVP_06 agente voz | Telegram voz → Cal.com/STT | flujos n8n que Hermes invoca por MCP |
| MVP_07 Studio OS | sistema completo | este documento |

## 10 · Puesta en marcha (genérica, 6 pasos)

1. Bot nuevo en BotFather → token a secretos
2. Servicio Hermes en el VPS: imagen oficial, volumen, límites, `gateway run`
3. `config.yaml` + `SOUL.md` del estudio
4. MCP n8n-official conectado y probado (listar flujos)
5. Skills de arranque al volumen
6. Cron 07:00 + prueba end-to-end: "agendame mañana 10h con X" → evento + mail

---

# REQUISITOS — el asistente sintético del arquitecto

## 1 · Alcance

**Dentro**: las 14 herramientas operando con registro y trazabilidad, con el paquete de arranque (7 skills) en el primer mes de cada estudio.

**Fuera (al inicio)**: impresora propia remota (mes 2+) · transcripción self-hosted full (piloto propio primero) · CRM completo · multi-usuario junior (cuando la capa operador entre) · ComfyUI local para el arquitecto (render va por API) · el arquitecto manejando n8n (nunca: conectado a flujos).

## 2 · Actores y permisos

| Actor | Puede | No puede |
|---|---|---|
| Arquitecto titular | pide todo por Telegram; aprueba nivel C-D | no toca n8n, ni VPS, ni configuración |
| El asistente (Hermes) | ejecuta A-B automático; prepara C-D y pide aprobación | no manda mail ni publica sin aprobación; no inventa disponibilidad ni datos |
| PITAUTECH (operadora) | administra todo, con acciones registradas | — |
| Junior (futuro, capa operador) | opera lo nivel A y B con agente local | pide aprobación para lo demás |

## 3 · Casos de uso (los 8 de arranque)

| # | Caso | Feliz si |
|---|---|---|
| CU-1 | "Agendame martes 10h con X" | evento en Cal.com con link de video (Meet o Jitsi según tipo) + invitación mail + confirmación con fecha AR |
| CU-2 | "Qué tengo esta semana" | lista con nombres, horas y Refs accionables |
| CU-3 | Audio de reunión → "hacé la minuta" | transcript + resumen + minuta con tipo (interna/cliente) + borrador mail ≤24h |
| CU-4 | Render + "cambiá el cielo" | 2-3 variantes con semilla/parámetros + keeper elegido y registrado |
| CU-5 | DWG + "auditame esto" | informe PDF: capas, escalas, xrefs, bloques, estándares, observaciones clasificadas |
| CU-6 | DWG + "computame" | tabla de partidas con unidades y m² desde bloques con atributos |
| CU-7 | "Preparame para imprimir el juego" | PDF con formato de impresión listo para gestoría |
| CU-8 | Cron 07:00 | digest del día + recordatorios de compromisos por vencer |

## 4 · Requerimientos funcionales

| RF | Requisito | Verificación |
|---|---|---|
| RF-1 | Todo pedido entra y responde por Telegram | 100% de los 8 casos operables desde el celular |
| RF-2 | Cada acción deja registro (tarea, artefacto, aprobación, fecha) | consulta en Postgres por proyecto |
| RF-3 | Minuta distingue tipo de reunión y usa parámetros del estudio | 2 minutas reales comparadas por el arquitecto |
| RF-4 | Render devuelve variantes con semilla y parámetros | portal con ≥1 serie keeper |
| RF-5 | Auditoría DWG no modifica el original | hash del DWG idéntico antes/después |
| RF-6 | Cómputo solo desde bloques estandarizados; avisa qué falta | informe con lista de bloques sin atributos |
| RF-7 | Mail se redacta solo con aprobación previa | 0 mails automáticos sin nivel D |
| RF-8 | Compromisos llevan fecha y avisan antes de vencer | ≥1 aviso recibido y accionado |
| RF-9 | El arquitecto opera sin abrir n8n | demo completa solo desde Telegram |

## 5 · Requerimientos no funcionales

1. **Latencia**: respuesta conversacional < 20 s; minuta < 2 h post-audio; informe DWG < 5 min.
2. **Disponibilidad**: Hermes y n8n 24/7; alerta de caída al operador en < 5 min (health workflow).
3. **Privacidad**: planos nunca a nube genérica; STT procesa audio (excepción aceptada); registro local.
4. **Idioma**: el del estudio, en toda interacción con el arquitecto.
5. **Mantenimiento liviano**: revisión semanal 30 min del operador; skills versionadas en vault.

## 6 · Gobernanza por herramienta

| Herramienta | Nivel de operación |
|---|---|
| Consultas, lectura, digest, avisos | A automático |
| Renders, informes, cómputos, minutas | B automático con registro |
| Agenda, modificación archivos, impresión | C con aprobación en el chat |
| Envío de mails, entrega a cliente, publicación | D con aprobación explícita; el envío lo hace la persona |

## 7 · Métricas de éxito (gate de cada entrega)

| Métrica | Meta |
|---|---|
| Minutas entregadas ≤24h | 100% de reuniones del período de prueba |
| Mensajes respondidos <20s | ≥ 90% |
| Renders con keeper registrado | ≥ 5 series |
| DWG auditados + computados | ≥ 3 reales |
| Mails automáticos sin aprobación | 0 |
| Veces que el arquitecto abrió n8n | 0 |

**Métricas de madurez** ([[specs/archived/261111-sistema-filosofico-practico-arquitectura|sistema filosófico §7]]): trazabilidad 100% con origen, versión, parámetros y aprobador · fuentes ingestadas vs fichas ≥95% · junior opera flujo completo con skill · costo por ejecución visible, éxito >95%.

## 8 · Madurez europea por jurisdicción

CABA código local + encomienda + firma registrada · conurbano municipio + visado previo · Europa normativa local + concurso digital con entrega trazable. El plano es documento legal (Ley 24.335): el portal de entrega guarda licencia, firmante, hash y fecha por proyecto.

## 9 · Reglas del vault (R1-R7, del patrón LLM Wiki)

R1 trazabilidad total (origen, versión, herramienta, parámetros, aprobador) · R2 HITL estricto con equivalencias de aprobación (`s/si/ok/dale`) · R3 frontmatter obligatorio y wikilinks absolutos sin extensión · R4 URLs oficiales verificadas 200 · R5 lenguaje en positivo · R6 cierre de sesión en `raw/sessions/` + fila nueva-arriba en `log.md` · R7 lo que no pasó en la PC de trabajo, no viaja.

## 10 · Rollback

Los flujos n8n equivalentes y la transcripción vigente siguen operativos; si falla una pieza de Hermes, el camino determinista sostiene la capacidad mientras se corrige.

## 11 · Qué NO decide este documento

* Elección final del motor de render por defecto (con la primera corrida real de calidad)
* Wake-on-LAN e impresora propia (mes 2)
* Migración de la transcripción Meet a Meetily (gate propio del piloto)
* Implementación de scripts y comandos — se entregan como archivos didácticos con ejecución HITL ([[AGENTS.md|regla del vault]])

---

# Operación — la instancia concreta

> Cambiar de instancia = reescribir esta sección; los principios de arriba quedan.

## 1 · Instancia piloto: estudio de Emilia Pimenta (35 días)

### 1.0 Dos personas, dos perfiles (el modelo de roles del MVP)

**El grafiquito de la conexión y la división de roles:**

```text
      VOS (SOL)                                    EMILIA
      operadora del sistema                        usuaria del sistema
┌──────────────────────────┐                 ┌──────────────────────────┐
│ N3 · taller              │                 │ celular (principal)      │
│ OpenCode + Antigravity   │                 │ PC (cuando quiere)       │
│ 4 curadores (sherlock,   │                 └────────────┬─────────────┘
│ brainstormy, contenidos, │                              │
│ vaultworm)               │                              │
│ ComfyUI RX 570           │                              │
│ vault de desarrollo      │                              │
└────────────┬─────────────┘                              │
             │ escribe skill / config / Bot               │
             │ aprueba con s                              │
             ▼                                            │
   ┌───────────────────────────── VPS CONTABO ────────────────────────────┐
   │                                                                      │
   │  HERMES — 1 instancia, 1 contenedor, 2 perfiles, 2 gateways          │
   │                                                                      │
   │  perfil DEFAULT = PI Manager          perfil EMILIA                  │
   │  → bot @hermes_pitau_bot (vos)        → bot propio de Emilia         │
   │  │                                    │                              │
   │  │  Bots (perfiles Pipi):             │  SOLO USAR:                   │
   │  │  pipi-docs · pipi-pm               │  agenda · minuta · render     │
   │  │  pipi-cad · pipi-visual            │  auditoría · cómputo          │
   │  │  pipi-ideas (modelo barato)        │  consultas al vault           │
   │  │  (pipi-bim, futuro)                │  ESTRUCTURA INTOCABLE:        │
   │  │                                    │  deny list config/skills      │
   │  │  MCPs: n8n · vault · dwg-worker    │  sin skills de desarrollo     │
   │  │  cron 07:00 · webhooks             │  sin editor de n8n            │
   │  │                                    │  radio de daño = su perfil    │
   │  n8n (Router, STT, mail, health) · dwg-worker (ezdxf) · Postgres     │
   └──────────────────────────────────────────────────────────────────────┘
             │                                            │
             ▼                                            ▼
   Google Sheets (CRM + fuentes)                drives/nube (excepción
   Fathom (Meet) · Cal.com · Gmail              solo transcript-texto)
```

**Flujo de capacidades (una sola vía)**: Sol escribe skill en el vault → `s` → publica al perfil emilia → Emilia la usa por su bot, sin código ni n8n. Si Emilia pide cambiar la estructura, su bot la rechaza o deja el pedido para Sol — la estructura se edita desde N3/CLI, nunca por su chat.

**ChatGPT Plus de Emilia ($20)**: su suscripción podría alimentar el modelo de su perfil vía login OAuth (ruta Codex, a verificar en S1). Si no aplica: OpenRouter con tope de gasto fijo — modelo declarado y medido por perfil.

**Futuro (rama Git por persona)**: cada persona aporta a una rama del mismo repo → su trabajo alimenta la wiki compartida y los procesos; el asistente base se distribuye como profile distribution (`hermes profile install github.com/estudio/asistente-base`). Al inicio, sin permisos complejos: la puerta de escritura es el `s` humano.

### 1.1 Auditoría del VPS Contabo (2026-11-11, solo lectura)

| Dato | Valor | Lectura |
|---|---|---|
| Host | `89.117.73.109` — AMD EPYC, 4 vCPU, 7.8 GB RAM, 72 GB disco | suficiente para el piloto |
| Uptime | 23 días, load 0.08 / 0.04 / 0.05 | tranquilo, sin estrés |
| RAM | 3.1 Gi usados · **4.6 Gi disponibles** | Hermes con límite 3 GB cabe (margen ~1.6 GB) |
| Swap | 2.0 Gi, sin uso | respiración extra |
| Disco | 23 G usados · **50 G libres** (31%) | sobra para imagen Hermes (~2-4 GB) |
| Servicios | 12 contenedores, todos 1/1 healthy, up 3 semanas | n8n · leantime ×2 · chatwoot ×4 · postgres · qdrant · redis ×2 · easypanel + traefik |
| RAM por servicio | n8n 789 MB · sidekiq 556 MB · mysql 502 MB · chatwoot 362 MB · leantime 270 MB | n8n es el más pesado, como corresponde |
| Puertos abiertos | 22 · 53 · 80 · 443 · **2377 · 7946 · 3000** | hallazgo: 2377/7946 (swarm) y 3000 expuestos — revisar firewall con `s` (no tocado en la auditoría) |

**Oportunidad detectada**: **Chatwoot ocupa ~1 GB de RAM total** (4 contenedores) y según [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|VISION §6.9]] está fuera de uso ("Chatwoot, Instagram y WhatsApp quedan fuera por ahora"). Liberarlo daría margen para Hermes con 2 perfiles. **Decisión abierta** — se actúa solo con tu `s`.

**Veredicto**: el VPS actual alcanza para el piloto con Hermes limitado a 2-3 GB. Si empujamos 2 perfiles + dwg-worker + picos de n8n, liberar Chatwoot es la palanca natural.

### 1.2 Datos del piloto

| Dato | Valor |
|---|---|
| Cliente | Emilia Pimenta (estudio 2-4 personas, Argentina) |
| VPS | Contabo 89.117.73.109 (ver §1.1) |
| Bots | `@hermes_pitau_bot` (Sol) + bot propio de Emilia (nombre a definir) — 2 perfiles, 1 contenedor |
| Agenda | subflujo Cal.com MVP_06 reutilizado |
| Reuniones | Fathom (Meet) + audio al bot |
| Render | Pollinations flux free → Runpod si pide calidad |
| DWG | dwg-worker ezdxf, test con DWG del vault |
| Gate final | demo punta a punta + presentación a Emilia |

## 2 · Migración y convivencia — dos bancos

| | **Antigravity + OpenCode** (N3, Sol) | **Hermes** (N1, estudio) |
|---|---|---|
| Qué es | el **taller**: pruebas, diseño, vault, ComfyUI, Rhino | el **sistema entregado**: 24/7 para Emilia |
| Quién | vos, ahora y siempre | Emilia, junior futuro, vos de celular |

**Sí seguís en Antigravity.** **Regla de migración**: una pieza viaja cuando (a) pasó su prueba acá, (b) su dueño la aprobó con `s`, (c) tiene rollback. **No migra**: ComfyUI RX570, Rhino/AutoCAD, vault de desarrollo, OpenCode/Antigravity ([[proyectos/MVP_07-studio-os-sistema/VISION#4.5 Por qué Hermes y no otras opciones|VISION §4.5]]).

## 3 · Camino 2 en paralelo — backend Obsidian y dashboard

### 3.0 Los bracitos operativos

| Bracito | Dónde | Formato | Dueño |
|---|---|---|---|
| Archivos que lee la IA | `raw/` (sessions, research, yt, pdf, reuniones, contenidos, cache JSON, `state.db`, Qdrant) | máquina, inmutable | IA |
| Archivos que lee el humano | `wiki/` + `proyectos/` + `specs/` | Obsidian humano, escritura con `s` | humano + IA |
| Scripts Python | `scripts/<slug>.py` + `_explicado.py` didáctico, comando `P:\Anaconda\envs\comfyenv\python.exe scripts/...` | mano repetible | Sol ejecuta, aprende leyendo |
| Flujos n8n | Router, STT, mail, cron, health | camino determinista | Hermes los invoca por MCP |
| Vista gráfica de avance | dashboard + diagramas (draw.io formal, Mermaid rápido, Excalidraw croquis) | lo que Sol mira construyendo | Sol |

### 3.1 Piezas del Camino 2

* **Inbox único**: Telegram Fuentes → Sheet `Fuentes-Inbox` → ficha canónica → wiki (análisis 1x1 de 53 filas en `raw/research/261111-fuentes-inbox-reporte-1x1.md`).
* **Fuentes v2**: credenciales Google estables (publish OAuth + Service Account — Fix A + Fix B, 15 min), Creador/Categoría en la hoja, tab Creadores + Sugerencias, PDF→fichas, **panel web** accesible del celular y navegadores de visores VR — detalle en [[specs/261111-fuentes-v2-panel-contactos-pdf|fuentes-v2]].
* **Reuniones con contexto**: tab `Contactos` (tipo, contexto, cómo analizar por persona) que inyecta la ficha al agendar y al minutar — misma tab sirve de CRM del piloto.
* **Dashboard tipo video** (3 paneles: Inbox/Digest/Proyectos · grafo D3 · preview `.md`): HTML estático que **solo lee archivos humanos**; `raw/`, caches y SQLite quedan sin UI por diseño. Grafo generado por script (JSON regenerable, nunca editado a mano). Fuente: video [backend con Obsidian](https://www.youtube.com/watch?v=XwEbK3JX5mc).
* **Meetily pilot N3** + worker propio → fichas al vault → skill `minuta-reunion`.
* **Qmd** opcional.

## 4 · Calendario del piloto

### 4.0 El mes (35 días, gates)

| Semana | Entrega | Gate |
|---|---|---|
| S1 | Hermes + bots + perfiles + MCP n8n + skills CU-1/2/8 | Emilia agenda 1 reunión real |
| S2 | CU-3 minuta + cron | 2 minutas reales ≤24h |
| S3 | CU-4 render + CU-5/6 audit + cómputo | 1 DWG real auditado y computado |
| S4 | CU-7 impresión + portal + pulido | demo punta a punta |
| +5d | ensayos, imprevistos | presentación a Emilia |

**Mapping al canon**: el 35d ejecuta el plan T0-T6 de MVP_07 comprimido para el piloto — T0-T1 = DÍA 1 · T2-T4 = DÍA 2 + semana S2-S3 · T5-T6 = S4 y mes siguiente. *(Propuesta — confirmación de I2 pendiente.)*

### 4.1 SPRINT DE CONSTRUCCIÓN EN 2 DÍAS — el núcleo vivo

Objetivo: **Hermes vivo con las capacidades demostrables de punta a punta**.

**DÍA 1 — Sistema vivo** (gate: CU-1, CU-2, CU-8, CU-3 operando en tu celular)

| Bloque | Qué | Tiempo |
|---|---|---|
| **A · VPS + bots + perfiles** | 1) BotFather → `@hermes_pitau_bot` + bot de Emilia (nombre a definir) → tokens a secretos 2) EasyPanel: servicio hermes, imagen `nousresearch/hermes-agent`, volumen `/opt/data`, 3GB/2vCPU, 0 puertos, `gateway run` 3) Perfiles: `default` (PI Manager) + `hermes profile create emilia --description` 4) `.env` por perfil: `TELEGRAM_TOKEN` + `N8N_MCP_TOKEN` 5) `config.yaml` + `SOUL.md` por perfil 6) Test "qué podés hacer" ×2 | 2-3 h |
| **B · MCP n8n + skills base** | 7) Preset `n8n-official` → listar flujos, probar tool Agenda (CU-1) 8) Skills `gestionar-clientes` · `preparar-compromisos` · `redactar-correo-cliente` al vault → publicar a 2 perfiles | 1-2 h |
| **C · Cron** | 9) Cron 07:00: digest + recordatorios 10) Prueba end-to-end: "agendame mañana 10h con Juan" → evento + mail borrador | 1 h |
| **D · STT + minuta** | 11) STT Gemini free en n8n (ADR MVP_06) 12) Skill `minuta-reunion`: transcript → resumen tipo interna/cliente → borrador mail 13) Test real: reunión de 10 min → audio al bot → minuta | 2-3 h |

**DÍA 2 — Motores + demo** (gate: demo completa de 7 capacidades con rastro)

| Bloque | Qué | Tiempo |
|---|---|---|
| **E · Render re-do** | 14) Test Pollinations flux (spec 261103) 15) Skill `rendir-con-indicacion`: imagen+texto → 2-3 variantes con seed 16) Entrega por Telegram | 2 h |
| **F · dwg-worker** | 17) Servicio Python ezdxf en VPS: auditoría capas/escalas/xrefs/bloques 18) Script `computo-partidas.py` (bloques con atributos → tabla) 19) Test con DWG del vault (cocina BHindú) 20) Skills `auditar-documentacion-cad` + `computar-partidas` | 2-3 h |
| **G · Jitsi** | 21) App "Jitsi Video" en Cal.com + evento con ubicación Jitsi 22) Test CU-1 con link Jitsi | 30 min |
| **H · Demo** | 23) Recorrido punta a punta: agenda → reunión → minuta → render → audit → cómputo → PDF 24) Métricas base + registro | 1-2 h |

**Fuera de los 2 días**: portal completo · impresión PDF formato · Meetily pilot + worker · dashboard grafo · lint automatizado · Qmd · onboarding formal de Emilia · presentación final (semana +5).

**Ejecución HITL**: cada paso = comando exacto + script didáctico cuando toque (`scripts/<slug>.py` + `_explicado.py`). Sin tu `s` no hay ejecución.

## 5 · Configuración completa (config.yaml + SOUL)

```yaml
# Identidad: SOUL.md se lee solo desde el HERMES_HOME del perfil (~/.hermes/SOUL.md o profiles/<nombre>/SOUL.md).

# Terminal
terminal:
  backend: docker
  docker_image: "nousresearch/hermes-sandbox:desktop"
  container_cpu: 2
  container_memory: 3072
  container_persistent: true
  env_passthrough: [STUDIO_DB_URL]

# Aprobaciones
approvals:
  mode: manual
  timeout: 300
  cron_mode: deny
  single_query_mode: deny
  unattended_mode: deny
  deny:
    - "git push --force*"
    - "docker compose down*"
    - "*rm -rf*"
    # perfil emilia, además:
    - "*config.yaml*"
    - "*skills/write*"
    - "*n8n*edit*"

# Memoria
memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true

# Skills
skills:
  write_approval: true
  create_dir: /opt/data/vault/skills
  external_dirs:
    - /opt/data/vault/.agents/skills

# Curador
curator:
  enabled: true
  interval_hours: 168
  stale_after_days: 14
  archive_after_days: 30
  consolidate: false
  backup: {enabled: true, keep: 2}

# Cron
cron:
  max_parallel_jobs: 2
  wrap_response: false

# MCP
mcp_servers:
  n8n:
    url: "https://n8n.pitau.tech/mcp-server/http"
    headers:
      Authorization: "Bearer ${N8N_MCP_TOKEN}"   # secreto en ~/.hermes/.env
    trust: untrusted
  vault:
    trust: untrusted
  dwg-worker:
    trust: untrusted
```

**`SOUL.md` (perfil emilia, base)**: quién es el asistente del estudio · idioma y tono rioplatense · pide email antes de agendar · cita lo entendido · jamás inventa disponibilidad ni datos · materiales C-D piden aprobación · la estructura se edita por la operadora, la conversación puede proponer mejoras que quedan registradas como pedidos.

## 6 · Migración semana a semana (piloto)

| Semana | Viaja al VPS | Queda en N3 (taller) | Gate |
|---|---|---|---|
| S1 | instalación base + 2 bots + 2 perfiles + MCP n8n + 3 skills relación | redacción SOUL y skills en el vault | Emilia agenda 1 reunión |
| S2 | skill minuta + cron + webhook STT | prueba flujo minuta en MVP_06 (comparación) | 2 minutas reales ≤24h |
| S3 | skills render + audit + cómputo; dwg-worker | pruebas Comfy local + prototipo ezdxf | 1 DWG real auditado |
| S4 | portal iteraciones + impresión PDF + pulido | demo ensayada, presentación | demo punta a punta |
| +5d | ensayos e imprevistos | — | presentación Emilia |

## 7 · Decisiones abiertas

| # | Decisión | Momento |
|---|---|---|
| 1 | Motor de render por defecto (Pollinations free vs Runpod) | con la primera corrida real |
| 2 | Diarización: Meet2Notes gratis vs Meetily Pro $10 | después de 3 minutas reales |
| 3 | Jitsi self-hosted | si el volumen lo pide (mes 2) |
| 4 | Impresión: gestoría PDF (mes) vs WoL (mes 2+) | S4 |
| 5 | Primer DWG real de prueba: de Emilia (con permiso) o del vault | DÍA 2 bloque F |
| 6 | Credenciales Google: Fix A (publish OAuth) + Fix B (Service Account) | antes del sprint — destraba todo |
| 7 | **Liberar Chatwoot** (~1 GB RAM) para dar margen a Hermes | antes o durante S1 — con tu `s` |
| 8 | **Revisar puertos expuestos** 2377/7946/3000 en firewall | con tu `s` — hallazgo de auditoría |
| 9 | Nombre del bot de Emilia | antes de A1 |
| 10 | M20 mini-servidor Linux: ¿sigue en el diseño mes 2+? | a decidir (I3) |

---

# Antecedentes (absorbidos y archivados en `specs/archived/`)

1. [[specs/archived/261110-manifiesto-fundacional-studio-os|Manifiesto fundacional]] — absorbido en VISION §1
2. [[specs/archived/261111-convergencia-mvps-hermes|Convergencia MVPs]] — absorbido en ESTRUCTURA §9
3. [[specs/archived/261111-sistema-backend-vault-hermes|Backend vault]] — absorbido en ESTRUCTURA §6-8 + Operación §3
4. [[specs/archived/261111-dos-caminos-emilia-35d-sistema-completo|Dos caminos]] — absorbido en VISION §6-7 + Operación
5. [[specs/archived/261111-plan-migracion-hermes-emilia|Plan migración]] — absorbido en Operación §5-6
6. [[specs/archived/261111-sistema-filosofico-practico-arquitectura|Sistema filosófico práctico]] — absorbido en VISION §1 + REQUISITOS §7-8
7. [[specs/archived/261029-filo-vault-v2|Filo vault v2]] — absorbido en VISION §5 + REQUISITOS §9
8. [[specs/archived/261029-filosofia-hermes|Filosofía Hermes]] — absorbido en VISION §1 (manifiesto)
9. [[specs/archived/261111-hermes-agentes-usos-estudio|Hermes agentes y usos]] — absorbido en ESTRUCTURA §6-7 + Operación §1.0
10. `261111-impl-emilia-35d-vision-estructura-requisitos.md` — unificado acá (eliminado)
11. [[raw/research/261111-fuentes-inbox-reporte-1x1|Fuentes-Inbox 1x1]] — análisis del inbox (raw)
12. [[specs/261111-fuentes-v2-panel-contactos-pdf|Fuentes v2 + contactos + PDF + panel]] — build operativo, queda activo
