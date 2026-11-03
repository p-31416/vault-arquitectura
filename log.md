---
tipo: log
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-11-01
tags: [log, historico]
---

# Log de operaciones

Más nuevo → más arriba

## 2026-11-02 — Membrana catenaria Kangaroo: .gh v1/v2 + trazabilidad a fuentes

- **Definición paramétrica** `activos/proyectos/concurso-gaudi-nexus/grasshopper/membrana-catenaria.gh` → `v2` (34 objetos, 41 cables, 0 obsoletos, verificado por API): `MeshPlane` → anclas en 4 esquinas → `EdgeLengths` + `Load` → `Solver` → espejo en XY a bóveda → `Show` + `TriRemesh`. Después: esquinas a altura independiente (`H1–H4`) y malla de piso con depresión editable (`Prof` vía `Point Deform`). Sin columnas: apoya en el plano `z=0`.
- **En escena Rhino**: membrana doble curvatura (catenaria X 7,5/0,6 × Y 8/0,8 invertida, 10 apoyos) + teselado triangular `s=1,2` + capas `CASCARA/CAMINO/VERDE/APOYOS/PISO/PROGRAMA_M2`. Loft reglado anterior eliminado (175 objetos), capas renombradas a definitivo.
- **Fix v2**: el `Anchor` recibía 121 vértices contra 4 objetivos (`Index out of range` en cascada) → ahora `Anchor.P` toma las 4 esquinas.
- **Trazabilidad documentada** en [[proyectos/concurso-gaudi-nexus/membrana-catenaria-gh|membrana-catenaria-gh]]: Parametric Monkey (verificado 200) + Makert Fig. 6 10×10 con carga puntual (verificado 200, réplica `fig6-malla-10x10.gh` pendiente de puente activo). Fila agregada en el índice del concurso.
- **Puente Rhino intermitente** (`10061`/`10054`): cae y se relanza con `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`. Nota: `import math` + `def` que usa `math` falla en el servidor MCP ( scope ); resuelto con bucles inline.

## 2026-11-02 — Plan maestro PI por temas: MCPs, modelos, licencias y lámina Gaudí + System Overview + set ingeniería punto por punto + guion alineado + índice maestro

- **Índice** `00-index.md` con sección Specs y diagramas nov-2026 (5 specs + ingeniería C4 + mapa PI) y fecha al 2026-11-02. **GUIA-LECTURA** §6 con lo nuevo nov-2026. Html sin "provisional": holoarquitecto como rol que dirige.
- **Cross-links**: plan maestro ↔ overview ↔ ingeniería ↔ guion, mismo sistema PI con holoarquitecto, un Hermes por estudio, A-D, L0-L4, C-01 a C-13.

- **Guion** `specs/261101-guion-visual-pi-remotion.md` alineado: nombre PI vs Studio OS vs editorial aclarado, ramas Comfy con L0-L4 y controles F, costos 4+1 con VISION §5 y RNF-10, sección Alineación 2026-11-02 con trazabilidad a VISION/ESTRUCTURA/REQUISITOS + plan maestro + overview + ingeniería.

- **V1** contexto validado en `arquitectura-pi-os.mmd`. **V2** `pi-stakeholders.mmd` titular/arq2/operador/cliente con A-D. **V3** `pi-bpmn-asis-tobe.mmd` 10 pasos hoy vs con PI. **V4** `pi-journeys.mmd` pedir→aprobar→recibir. **E4** `pi-er-registro.mmd` proyecto/archivo/tarea/artefacto/aprobación. **R1** `pi-casos-uso.mmd` C-01 a C-13. **R4** `pi-maquina-estados.mmd` pendiente→validando→espera→ejecutando→hecha/stale. Documento cerrado en `pi-system-ingenieria.md` con qué es cada documento y siglas.
- **Rename 2026-11-02**: se adopta **holoarquitecto** y se retira `Meta²` provisional (omniArquitecto descartado). Propagado en guion, `arquitectura-pi-os.md/.mmd`, `prompt-coach-vs-agentico.html`, `pi_studio_remotion_notas.md` y anchors de `auditar_presentacion_pi.py`. Raw histórico conserva `Meta²` como testimonio.

- **Spec nuevo** `specs/261102-system-overview-pi.md`: overview texto + Mermaid con entry points (Telegram/CLI/webhook/cron/API), Hermes con Prompt/Provider/Dispatch, storage SQLite+Postgres+vault+Qdrant y backends docker/ssh/MCP — mapeo directo de tu diagrama a N2 Windows, M20 y GPU nube.
- **Ingeniería C4** `diagramas/pi-system-ingenieria.md` + `pi-system-ingenieria-c4.mmd` + `pi-system-ingenieria-componentes.mmd` + `pi-system-ingenieria-despliegue.mmd`: L2 contenedores con puertos y protocolos, L3 componentes que mapea tu ASCII a PI, despliegue N1-N4 por Tailscale y secuencia sobre-de-tarea con tabla de contratos.

- **Spec nuevo** `specs/261102-plan-maestro-pi-por-temas.md`: T1 reunión→doc, T2 reparto agentes, T3 tabla MCP con docs verificadas, T4 matriz open/pago/cloud/local + T4.1 entradas L0-L4 con ControlNet/inpaint/outpaint versionados, T5 licencias por jurisdicción con matriz verificación + checklist CABA/conurbano/Europa + firma y tokenización, T6 gestión + obra, T7 firma local Llama, T8 loop moodboard→LoRA con dataset curado y strength calibrado, T9 evolución diaria + flujo lámina Gaudí con catenarias paramétricas.
- **Responde**: multi-PC al mismo Hermes por Telegram + Tailscale + `vault://pruebas/`, Windows enchufada como N2 ejecución, M20 Linux como mini-cloud con límites (orquesta y valida, GPU avanza en nube).

## 2026-11-01 (noche) — Tabula rasa Pi: transcripción primigenia + arquitectura PI OS para MVP 2 personas

- **Tabula rasa** `raw/sessions/2026-11-01-sesion-tabula-rasa-pi.md`: voz literal de Sol (matrícula Pi 3.14.16, cuarta revolución, meta-arquitecto con 4-6 agentes Antigravity, estándares internos antes que BIM) + cita filosófica-humana + decisiones punto por punto.
- **Diseño experto** `specs/261101-tabula-rasa-arquitecto-futuro-pi-os.md`: Hermes agente único, contrato con `file_ref` y gobernanza A-D, ComfyUI por API (concurso primero, custom después), Rhino puente+Hops con evaluación 9, BIM FreeCAD+IfcOpenShell, Unreal futuro, entradas croquis/volumetría/texto/voz/imagen, secretaría todo junto, MVP Sol técnica + 1 arq escalable a mediana + desarrollo inmobiliario.
- **Trazabilidad**: VISION/ESTRUCTURA/REQUISITOS/IMPLEMENTACION-HERMES + meta-arquitecto + ptech-filosofia + transcript ChatGPT + MVP_02/04/05.

## 2026-11-01 (tarde) — Router Emilia: extracción Jina reparada con API key, ack que avisa y canvas agrupado

- **Diagnóstico exec 3960 del Router** (`YWpuV5p0vCDTbIHz`): la fila llegaba al Sheet con Título y Tags vacíos — **403 de `r.jina.ai`** (`AbuseAlleviationError 40305`, acceso anónimo a instagram.com bloqueado por abuso de terceros, 20 RPM por IP compartida) que pasaba silencioso por `onError: continueRegularOutput` y el ack igual mandaba "Anotado ✓".
- **Dos fixes**: (1) el ack ahora suma **"⚠️ Jina no extrajo — completá título y tags a mano"** cuando el título queda vacío; (2) credencial nueva **`Jina Reader API Key`** (`httpHeaderAuth`, `Bearer jina_...`) del portal `jina.ai/api-dashboard/key-manager` conectada al nodo `Extrae Jina` — pasa de 20 RPM anónimas a **500 RPM por key** y sin bloqueos de dominio por IP.
- **Canvas agrupado en 3 grupos** (13 → 8 cajas de 1.º nivel): **Identidad** · **Inbox Fuentes** (cadena Has Link → Ack) · **Agente Voz**. El grupo "Comandos legacy" lo rechazó el server (gate con 2 salidas externas); los 4 nodos sueltos no pueden agruparse por reglas de conectividad — queda tolerado a 1 del techo 7.
- **Verificado con test real** (execs 3962/3963, links del estudio): título completo + 6 tags del link de discourse.mcneel.com — la extracción funciona con la key.
- **Dos publicaciones al flujo activo**: `7f889b6d` (ack + key) → `e4a475f8` (agrupado). Deuda menor: completar filas antiguas del `Fuentes-Inbox` con Título vacío (a mano o re-mandando el link).
- **Sesión:** `raw/sessions/2026-11-01-sesion-debug-extraccion-jina-router.md`.

## 2026-10-30 (tarde) — Studio OS: guía de lectura para explicar el sistema, y el agente ya tiene nombre y dirección

- **Documento nuevo** `proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA.md` (82 líneas): los cuatro documentos en una línea · **12 recorridos por tema** con sección y línea exacta (el sistema en 10 minutos, infraestructura, integraciones, cuaderno digital, gobernanza, métricas, plazos, costos) · orden mínimo de una hora y qué se puede saltear · **7 preguntas que va a hacer Emilia** con la respuesta corta y dónde está · lo que falta escribir · contexto fuera de la carpeta.
- **Nombre del agente decidido:** se usa **Hermes** como plataforma y como persona — dirección **`hermes@agents.pitau.tech`**. Cero renombrado en los documentos (122 menciones).
- **DNS verificado (solo lectura):** `pitau.tech` **no tiene MX** (agregar el del subdominio no toca nada existente) · A `pitau.tech` = `89.117.73.109` · **`agents.pitau.tech` ya resuelve** al VPS por el comodín `*.pitau.tech` · NS en **Donweb** (no Cloudflare), así que el MX se agrega en el panel del registrador.
- **Academia de Nico (pymbu) — no extraíble:** `academy.pymbu.com` es un portal de membresía **GoHighLevel** (SPA); devuelve el mismo shell de 2,4 KB y cinco rutas de API probadas caen en el catch-all. `?source=communities` no cambia el permiso. Queda pendiente que el usuario guarde la clase como PDF/HTML en `raw/pdf/` o la transcriba.
- **Coherencia:** `VISION.md` y `REQUISITOS.md` ahora nombran al cuarto documento (la tabla de "tres documentos" queda igual); `proyectos/00-index.md` arranca la fila con la guía.
- **Enlaces verificados con script:** 62 en la guía + 21 en VISION + 16 en REQUISITOS, **0 rotos**. Se corrigieron tres anclas que usaban guion en lugar del em dash real (U+2014) y un enlace a `specs/260909-esquema-mes1-60hs-studio-os-emilia`, que no existe, reemplazado por `specs/261013-plan-cierre-mes1-calculadora-emilia`.
- **Sesión:** `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` (Continuación 12).

## 2026-10-30 — Filosofía Hermes + grafos: documento único, ensayo, norma de diagramas y grafo 3D macro→micro

- **Documento único** `specs/261029-filo-vault-v2.md`: visión completa (7 flujos, corte determinista/agéntico/contractual, HITL estricto) + estructura + requisitos enunciados. Decisiones: híbrido, Hermes 1→N, `s` siempre.
- **Ensayo** `specs/261029-filosofia-hermes.md`: breve sin técnica (LM, harness, skill, MCP, Age of Empires, 4ta revolución) + §7 reescrito (sesión @brainstormy: 12 relaciones → 5) + §8 relaciones + §9 manifiesto de 3 líneas.
- **Norma de diagramas**: draw.io formal / Mermaid rápido / Excalidraw croquis. Comparativa viva `diagramas/prueba-comparativa.md` + plugins instalados (Excalidraw 2.29.0, draw.io 3.1.1, `community-plugins.json`); pendiente activación manual en Obsidian.
- **Gráficos**: `flujo-fuentes-wiki-hermes` (4 carriles + tabla replicable, 40 celdas) y `cerebro-hermes-fractal` (drawio 37 celdas + SVG + mmd + nota) + **grafo 3D** `cerebro-hermes-fractal-3d.html` (44 nodos, capas pineadas macro→micro, invariante verificado: 66 links sin violaciones, JS OK). Fuentes propuestas ⭐: audio, croquis, CAD.
- **Sesiones:** `raw/sessions/2026-10-29-sesion-filosofia-hermes-grafo3d.md` (checkpoint) + `raw/sessions/2026-10-30-sesion-cierre-filosofia-grafo.md` (cierre).

## 2026-10-29 (noche) - Studio OS en cuatro documentos: la arquitectura traducida a Hermes Agent, con cada capacidad verificada en la documentación oficial

- **Cuarto documento del proyecto** `proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES.md` (569 líneas, 15 secciones): qué resuelve Hermes sin escribir código · las 5 piezas a configurar (`config.yaml`, `SOUL.md`, `AGENTS.md`, skills, cron + webhooks) · ocho flujos (A fuentes de Drive, B mantener la wiki, C seguridad, D registro, E cuaderno y croquis, F compromisos, G webhooks/Fathom, H entregas) · lo que Hermes no hace · los hallazgos que cambian el diseño · `config.yaml` completo propuesto · 5 decisiones abiertas · 15 referencias con URL.
- **Hallazgos que corrigen lo que habíamos supuesto:** Hermes guarda en **SQLite `state.db` con FTS5, no Postgres** (el registro propio sigue en Postgres aparte) · el backend **Docker saltea las aprobaciones de comandos peligrosos**, así que el gobierno A-D tiene que vivir en el toolset y no solo en `approvals` · la memoria persistente es a propósito chica (**2.200 caracteres** en `MEMORY.md`, **1.375** en `USER.md`) · **un solo agente por `HERMES_HOME`** (el segundo perfil con Ollama va con perfil propio) · los jobs de cron **no pueden preguntar** (`cron_mode: deny`) y **no recuerdan la corrida anterior** · `read_file` convierte pdf/docx/xlsx/pptx **y avisa** de un PDF escaneado pero **no hace OCR**.
- **Configuración revisada contra la referencia real de MCP** (`/docs/reference/mcp-config-reference`): se cambiaron las claves inventadas por las que existen — `tools.include` en lugar de `tools_allow`, `auth: oauth` (OAuth 2.1 con PKCE, token en `~/.hermes/mcp-tokens/`), `trust: untrusted` (toda tool de escritura pide aprobación), `headers.Authorization: Bearer ${N8N_MCP_TOKEN}` para n8n y `${env:VAR}` para secretos desde `~/.hermes/.env`. **No hay clave `soul:`**: `SOUL.md` se carga solo si existe en `HERMES_HOME`.
- **Riesgo con fecha documentado:** el MCP oficial de Google Drive (`https://drivemcp.googleapis.com/mcp/v1`) está en *Developer Preview* y desde el **11/11/2026** Google rechaza clientes OAuth que no estén marcados como *"AI-powered agent"*. La recomendación queda en tres variantes (A1 MCP oficial · A2 skill `google-workspace` · A3 espejo con rclone) con A3 como base de archivo y A1 para lo nuevo.
- **VISION recortada a visión pura** (~300 líneas): §4.3, §4.6/4.7, §6.2, §6.4, §6.5, §6.6 y §6.7 reemplazadas por resúmenes de 1-3 líneas con puntero a `ESTRUCTURA`/`REQUISITOS`; §6.8 quedó con tres preguntas de producto.
- **Limpieza:** borrado `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` (la carpeta quedó con los cuatro documentos) · tres typos con caracteres CJK corregidos en `ESTRUCTURA.md` · grep de ideogramas sin coincidencias en el proyecto.
- **Enlaces:** `ESTRUCTURA.md` (encabezado) y `proyectos/00-index.md` apuntan ahora al cuarto documento.
- **Sesión:** `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` (Continuación 11).

## 2026-10-29 (tarde) — Matriz txt2img con prompt y seed fijos, galería web de renders y tabla de nodos pagos → open source

- **Revisión de los siete flujos** del concurso (fichas de `proyectos/concurso-gaudi-nexus/flujos/`): flujo-01 y flujo-02 en detalle, flujo-03 y flujo-07 contra el grafo existente, flujo-04/05/06 para el mapa de plataformas. Corrección detectada: flujo-01 pide "tres corridas A (seeds 42/77/123)" cuando A son tres corridas **idénticas** con la misma seed.
- **Matriz txt2img** (script nuevo `scripts/matriz-txt2img.py` + notas): 20 filas en 4 bloques — modelo · LoRAs SD 1.5 · LoRAs SDXL · parámetros — con **un prompt** (el del proyecto: Mercado de Proximidad + Centro de Cultura Digital junto a la Sagrada Família) y **seed 42** en todas las filas, para que la diferencia entre dos imágenes sea la variable y nada más. **Bloque SD 1.5 corrido: 14/14 OK en ~35 min** (65–210 s por render). Los renders caen en `output/matriz/` y aparecen solos en la galería.
- **Galería web de renders** (script nuevo `scripts/galeria-renders.py` + notas): sitio estático de un solo `index.html` (~64 KB, sin dependencias, funciona en `file://`) con **lienzo infinito** de pan y zoom al estilo Magnific, una columna por workflow, **color estable por seed**, panel de metadata completa al hacer clic, recorrido lineal con teclado y tira de miniaturas, filtros por workflow/LoRA y búsqueda en los prompts. **94 renders** (80 previos + 14 de la matriz) en 58 workflows, 54 MB en `activos/web/galeria/` (fuera de git). JS validado con `node --check`.
- **Documento maestro** `specs/261029-matriz-txt2img-galeria-y-publicacion.md`: protocolo de la matriz, arquitectura de la galería, plan de publicación en `pitau.tech` (servicio nginx estático + labels de Traefik en el VPS de EasyPanel) y el **agente constructor de flujos** (docs → spec → validación contra `/object_info` → grafo API → corrida → log) como sustituto del Prompt Coach del curso.
- **Tabla de nodos de proveedor pagos y su reemplazo open source** (módulos 3, 4 y 5): Topaz/Magnific → RealESRGAN + Hires (local) · Nano Banana 2 / GPT Image → `sd-v1-5-inpainting-fp16` + IC-Light (ya en disco) · Seedance 2.0 → LTX-2 con LoRAs de control (pod) · Hunyuan3D / Tripo → ComfyUI-3D-Pack (pod) · Nano Banana Pro → Depth Anything 3 + SD1.5 img2img (local). **El módulo 2 no tiene nodos pagos.** La única fila donde el reemplazo es realmente peor es Seedance (video).
- **Hallazgos:** el workflow del video 1 **no está en la carpeta del curso** (el Módulo 1 de Miro solo trae instrucciones del Prompt Coach) — su equivalente del estudio ya existe (`WF04-1.0.0-txt2img-base.json`); la trazabilidad ya estaba resuelta porque ComfyUI graba `prompt` y `workflow` dentro del PNG, lo que faltaba era la capa de lectura; `caddy-salidas/` no es una carpeta web sino el output root del MCP de AutoCAD.
- **Verificación visual:** el baseline M01 (SD 1.5, sin LoRA) ya devuelve una calle peatonal fotorreal con mercado, gente y luz de mañana; M03 con el LoRA archviz @0,8 es visiblemente distinto con la misma seed → el delta es atribuible al LoRA.
- **Sesión:** `raw/sessions/2026-10-29-sesion-matriz-txt2img-galeria.md`.

## 2026-10-28 (noche) — LoRAs de ComfyUI que corren en la infra local: catálogo verificado, 17 LoRAs instaladas y workflow de calibración

- **Investigación + instalación**: 16 LoRAs de arquitectura bajadas de CivitAI y **validadas una por una** con el lector de safetensors de ComfyUI (17/17 sanas, base deducida de la metadata embebida `ss_base_model_version`): 9 de SD 1.5 (rank 8–128) para ArchitectureRealmix y 7 de SDXL (rank 16–128) para Juggernaut XL, más el LoRA FLUX del curso ya presente.
- **Criterio de elegibilidad local documentado**: SD 1.5 ≤250 MB con 2 ControlNet · SDXL hasta 900 MB **sin** ControlNet (Union no entra) · FLUX/SD3/Qwen imposible local (`models/text_encoders/` vacío) → RunPod 24 GB.
- **Ficha nueva** [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]]: catálogo con base, rank, tamaño, trigger, id de CivitAI y estado + **qué hace cada flag del launch** (`--directml 0`, `--force-fp16`, `--lowvram`, `--cpu-vae`, `--cache-ram 2 8`, `--preview-method auto`, `--disable-dynamic-vram`) y los tres parches locales (VRAM DirectML en `comfy/model_management.py:321`, Canny en CPU por `F.pad` de kornia, logger).
- **Errores del vault corregidos**: (a) `comfyui.md` apuntaba a CivitAI #119936 como "Architectural Visualization" — **ese id es "Action - Eating Watermelon"**, ahora apunta al #191596 real; (b) `pbk-comfyui.md` atribuía `dpt_hybrid` a `comfyui_controlnet_aux`, **pack no instalado** — el core 0.28 trae Depth Anything V3 y SD Pose nativos; (c) los SDXL de 870 MB–1,3 GB quedan explícitamente para RunPod.
- **Trampas de descarga documentadas**: un LoRA de CivitAI puede devolver la **página de login** en vez del binario (detectar por `content-type: text/html`), CivitAI **no soporta Range** (una descarga cortada no se puede reanudar) y el tamaño del archivo **no** prueba que un safetensors esté sano (verificar con `safe_open`).
- **5 LoRAs piden login de CivitAI** (brutalista SD1.5 y XL, Building Info Concepts Sheets, ArchViz de ArteFactoryLab, JJ's Skyscraper): con `CIVITAI_API_TOKEN` se bajan; sin token, tres ya tienen sustituto instalado. El mirror de HF del brutalista de JJ es la **variante FLUX**, no la local.
- **Aceleración documentada, no instalada** (decisión del estudio): LCM-LoRA SD1.5/SDXL e Hyper-SD con URLs verificadas; `sdxl-lightning`, `control-lora`, `TCD-SDXL` y `detail-tweaker` devuelven 401 desde esta red. El sampler `lcm` ya es nativo en ComfyUI 0.28.
- **Workflow de calibración nuevo** `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/` (5 documentos + 2 grafos API + script): 1 render por LoRA con seed 42, prompt fijo y strengths 0,6 y 0,8 → nomenclatura `n_01-G-NN.png` (letra **G = LoRA**, añadida a la leyenda en `reglas-workflows-comfy.md`).
- **Script nuevo** `scripts/calibrar-loras-comfyui.py` + notas: arma el grafo con `LoraLoader` entre el checkpoint y el sampler, lo manda por la API HTTP de ComfyUI, espera, copia la salida al vault y registra LoRA × strength × segundos × error en `PLANS/calibracion-loras.json`.
- **Renders pendientes**: la tanda de 32 se abortó a pedido del estudio (job `99eeabec` cancelado, sin imágenes generadas) — queda para la próxima sesión, empezando por SD 1.5 strength 0,8.
- **Sesión:** `raw/sessions/2026-10-28-sesion-loras-comfyui-locales.md` · **Informe:** `raw/research/2026-10-28-loras-comfyui-locales.md`.

## 2026-10-28 (tarde) — Los 7 workflows del curso AI×Gaudí: fichas de flujo, plan maestro y carpeta del concurso

- **Seis fichas de flujo nuevas** en `proyectos/concurso-gaudi-nexus/flujos/` — la transcripción de cada módulo del curso **hecha flujo**: pasos con el nodo exacto y su valor, los prompts literales, las reglas que el instructor explica y la lista de lo que el video deja vacío (marcado como "no dicho en el video"). Cada ficha cierra con dos secciones añadidas por el estudio: **"Cómo lo adaptamos"** (qué hace el curso · qué hacemos nosotros · por qué) y **"Checks contra el criterio del jurado"**. Fuentes verbatim: [[raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.es|M1]] · [[raw/yt/transcripts/2026-10-21_mux-text-to-image.es|M2]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-image.es|M3]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-video.es|M4]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.es|M5]] · [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es|M7]].
- **Plan maestro** [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|specs/261028-plan-workflows-adaptados-curso-ai-gaudi]]: los 7 workflows uno por módulo en orden de curso, la **matriz de adaptación** (9 diferencias entre el curso y nuestra pila), el **ciclo de construcción y revisión de 6 pasos con gate humano**, los milestones **M-C1 a M-C7** (31/10 → 12/12, entrega 16/12) y el sprint 1 con 22 pomodoros.
- **Adaptación clave (decidida por el usuario):** local 8 GB para las pruebas + pod de RunPod para el render FLUX.2 klein 9B; los nodos privados del curso (Nano Banana 2/Pro, Seedance 2.0, Tripo, Topaz) se reemplazan por la vía abierta (FLUX.2 en modo edición, SDXL + ControlNet + DA3, LTX, ComfyUI-3D-Pack, RealESRGAN + Hires) y el plan de Comfy Cloud queda como techo de gasto a relevar.
- **Nueva carpeta del concurso** `proyectos/concurso-gaudi-nexus/` — `index.md` · `flujos/00-index.md` · `workflows/00-index.md` (mapa WF ↔ módulo ↔ plataforma ↔ precondiciones) · `criterio/criterio-jurado.md` (checklist de cierre, en borrador hasta la transcripción del módulo 6).
- **Módulo 6 (Round Table) tiene vía:** el CDN del curso responde 403 sin el `Referer` del player y con él entrega el `play_720p.mp4` (538 MB) → nuevo script `scripts/transcribir-leccion-bunny.py` + notas (descarga → ffmpeg → faster-whisper en CPU → `raw/yt/transcripts/`), que completa el circuito junto a `mux_lecciones_curso.py`.
- **Reglas nuevas del estudio** en `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md`: **R2** (el escalado depende del modelo: `ImageScaleToTotalPixels` a megapíxeles en FLUX.2, `ImageScale` 512² en SD1.5) · **R3** (nomenclatura `gx-{LETRA}-{NN}.png` para el concurso) · **R4** (validación estática contra `/object_info` y contra el disco antes de la primera corrida).
- **Estado real medido de la máquina:** ComfyUI v0.28.0 con DirectML (servidor apagado), `architecturerealmix_v11` + `Juggernaut-XL_v9` + `sd-v1-5-inpainting`, ControlNet canny/depth/scribble, IPAdapter + CLIP-ViT-H, Depth Anything 3, RealESRGAN, IC-Light y el **LoRA del curso `rhino-to-image-lora.basic` (120,8 MB) ya en disco**; falta el stack FLUX.2 (18,3 GB), LTX, el pack 3D y `comfyui_controlnet_aux`.
- **Sesión:** `raw/sessions/2026-10-28-sesion-workflows-adaptados-gaudi.md`.

## 2026-10-28 — Studio OS delineado: visión, estructura, requerimientos, 8 ADRs y el proyecto MVP_07

- **Nuevo proyecto `proyectos/MVP_07-studio-os-sistema/`** — el sistema operativo del estudio: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|readme]] · [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo]] (documento vivo: visión → estructura → requerimientos → roadmap F0-F6 → cierre del MVP → 8 preguntas abiertas) · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec]] (sobre de tarea, DDL `studio_os`, API del runner, perfil de pod, `SOUL.md`, sincronización del vault) · [[proyectos/MVP_07-studio-os-sistema/02-ft-mvp_07|02-ft]] (plan de construcción: F0 con 11 tareas verificadas, F1, F2, inventario de scripts con sus comandos, 13 pruebas de aceptación, riesgos y reversión, y los primeros 90 minutos).
- **Ocho ADRs en `specs/`** (formato Nygard liviano, skill `architecture-decision-records`): [[specs/ADR-2026-10-28-agente-hermes-en-vps|agente Hermes en el VPS]] · [[specs/ADR-2026-10-28-nodo-gpu-runpod-secure|nodo GPU Runpod Secure]] · [[specs/ADR-2026-10-28-puente-mcp-p1-p3|puente MCP P1+P3]] · [[specs/ADR-2026-10-28-registro-hibrido-postgres-vault|registro híbrido Postgres+vault]] · [[specs/ADR-2026-10-28-un-agente-por-estudio|un agente por estudio]] · [[specs/ADR-2026-10-28-vault-canónico-en-vps|vault canónico en el VPS]] · [[specs/ADR-2026-10-28-telegram-como-interfase|Telegram como interfase]] · [[specs/ADR-2026-10-28-perfiles-de-ejecucion|perfiles de ejecución]].
- **Auditoría de Runpod (29 fuentes oficiales)** en `raw/research/2026-10-28-runpod-auditoria-pi.md` — corrige el plan anterior: **no hay cláusula de no-entrenamiento** en ToS/Privacy Policy/DPA (hay que pedirla por escrito), **el DPA no está firmado por defecto**, los *Performance Data* quedan **fuera del DPA** (retención de logs sin plazo), **Community Cloud deja de aceptar hosts** (el precio barato se va; Secure cuesta ×2,3: 3090 $0,50/h), cifrado solo en volume disk, 28 datacenters (5 UE, sin UK ni LATAM) y **Tailscale no está documentado por Runpod**. Alternativas con residencia UE verificadas: Scaleway FR y OVHcloud FR (L4 €0,75/h). Tabla de material: planos legales, material de cliente confidential y material de concurso con PI de terceros **no pueden** ir a la nube.
- **Medición del VPS (solo lectura, SSH `contabo`)**: 4.858 MB de RAM disponibles sobre 7.941 MB, load 0,15, 50 GB de disco libres, Docker Swarm con 12 servicios → **Hermes entra sin ampliar** (`--memory=3g --cpus=2`). Riesgo anotado: `n8nio/n8n:latest` sin versión pineada.
- **Hechos verificados que cambian el diseño**: **Rhino.Compute** es headless y autohospedable (y trae **Hops**, el Grasshopper headless de Rhino 8) → la geometría no necesita el escritorio; **APS Design Automation no cubre AutoCAD LT** → la vía cloud de AutoCAD queda bloqueada por licencia; el nombre oficial es **Runpod** (una sola R mayúscula) y "RunPod" está deprecado (el vault lo usa en ~15 lugares: corrección pendiente); el dashboard de Hermes exige auth en bind no-loopback desde el endurecimiento de junio 2026 (escáneres plantaron una backdoor SSH).
- **Decisiones del usuario:** arrancar con **Hermes en el mismo VPS**; nodo GPU **Runpod Secure**; **un agente del estudio**; **Telegram** como interfase (n8n ahora, Hermes después, con temas por obra y canal de bitácora); **registro híbrido** (Postgres `studio_os` + vault); **puente P1+P3**; **vault canónico en el VPS** con GitHub como espejo; MVP = **caso AIZ + render IA**; el banco de pruebas es esta PC (AutoCAD estudiantes, Rhino, ComfyUI, Twinmotion, Unreal) con la regla *si no pasó en P:, no viaja a G:*.
- **Reglas de Karpathy incorporadas al agente** (`SOUL.md`): pensar antes de actuar · simplicidad primero · cambios quirúrgicos · ejecución contra objetivo verificable, más el mandato de PI y los niveles de riesgo A-D con aprobación humana.
- **Kit de F0 listo para ejecutar**: `scripts/studio_os_verificar_vps.py` + `_notas.md` (inventario del VPS **de solo lectura** por SSH, con veredicto RAM para Hermes) · `proyectos/MVP_07-studio-os-sistema/deploy/00-f0-comandos.md` (7 pasos con comandos copiables, verificación y reversión) · `deploy/hermes.compose.yml` (servicio Swarm: volumen nombrado, límite 3 GB, **cero puertos publicados** porque el gateway de Telegram hace long polling y la API 8642/dashboard 9119 quedan apagados hasta que hagan falta) · `hermes/SOUL.md` (identidad del agente, versionada en el vault) · `hermes/skills/auditar-documentacion-cad/SKILL.md` (primera habilidad, con precondiciones, validaciones y evidencias).
- **Consolidación en un único documento** (a pedido del usuario: "tiene que ser un único documento"): todo el sistema quedó en **un solo archivo**, `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` (9 secciones: visión · estructura · requerimientos · roadmap y cierre del MVP · contratos técnicos · las 8 decisiones en formato Nygard · plan de construcción · comandos de F0 · anexos). Los archivos `01-spec-mvp_07.md`, `02-ft-mvp_07.md`, `deploy/00-f0-comandos.md`, `deploy/hermes.compose.yml`, `hermes/SOUL.md`, `hermes/skills/auditar-documentacion-cad/SKILL.md` y los 8 `specs/ADR-2026-10-28-*.md` quedan **fusionados** en el maestro (pendiente de borrar). El `readme-mvp_07.md` quedó como puerta mínima y `scripts/studio_os_publicar_hermes.py` + `_notas.md` hacen que la fuente siga siendo única: extraen §9.2 y §9.3 del maestro y los publican en el agente por SSH. Nota técnica: en Docker Swarm los contenedores se llaman `servicio.1.tarea`, así que `docker exec hermes` no funciona y hay que resolver el ID real primero.
- **Reset del proyecto y `VISION.md`**: el usuario pidió empezar de cero ("creaste muchos archivos y no entiendo nada") y que en este proyecto los archivos se nomenclen **VISION · ESTRUCTURA · REQUISITOS**. Escrito `proyectos/MVP_07-studio-os-sistema/VISION.md` (14 secciones en 5 bloques: qué es y por qué · el recorrido del trabajo del estudio y dónde entra el agente · Hermes conceptualmente · el stack delineado en tabla con las alternativas libres/open source primero · principios, habilidades, modos de ejecución, niveles de riesgo, camino en 3 tramos, decisiones tomadas y preguntas abiertas con sus opciones). Borrados 16 archivos redundantes (9 del proyecto, los 8 `specs/ADR-2026-10-28-*.md` y `studio_os_publicar_hermes.py` + notas); se conservan el research de Runpod, el log de sesión, `studio_os_verificar_vps.py` y `00-filo-mvp_07.md` como borrador técnico que se borra cuando existan ESTRUCTURA y REQUISITOS. Decisiones nuevas del usuario: **GPU local primero** (la nube es excepción), **n8n se mantiene**, **Ollama local en vez de modelo en la nube** (a definir dónde), **conectar opencode ↔ Hermes**, y **rehacer el orden de fases desde cero** una vez escritas VISION y ESTRUCTURA.
- **`VISION.md` reescrito con el recorrido real del estudio**: el usuario_PASSó_ su propio ciclo de trabajo (cliente → reunión → compromisos → cuaderno → planos → 3D → render → obra → entregas → memoria) y se ajustó el documento: el **CRM es una hoja** (Google Sheets) y no un CRM; los **compromisos llevan fecha** y avisan por Telegram (el mail al cliente lo arma el agente con el formato del estudio y lo manda una persona); el render **no viaja por mail** sino a un **portal** de iteraciones; las **entregas las manda una persona** con el paquete preparado y queda registro con fecha; la **memoria mejora sola** con Hermes. Se agregó el **cuaderno digital** (método *commonplace book* de Leonardo da Vinci, video "El hábito de Leonardo da Vinci que me ha quitado el móvil de las manos", Maialen Lleó) como artefacto central: la parte manual es del arquitecto, la parte automatizada es de Hermes. Se agregaron al stack 6 filas libres (Google Sheets/Baserow/NocoDB · Quartz/MkDocs · PhotoPrism/Piwigo · Nextcloud+Memories/Immich · Qwen-VL/CLIP/exiftool/OpenCV · plantillas+Gmail API) y 3 habilidades nuevas (`gestionar-clientes`, `preparar-compromisos`, `redactar-correo-cliente`, `experto-comfyui`, `publicar-iteraciones`, `curar-cuaderno`), y 2 preguntas abiertas (visión por computadora en obra · dónde viven las fotos).
- **`VISION.md` reescrito con el criterio del usuario** (revisión conjunta del 28/10): el problema se reenmarca — *"las soluciones son de herramientas y no estamos hablando de sistemas"* + comunicación + auditabilidad + **el conocimiento accesible a un junior para que le cueste menos horas al senior** (§1.3 y §1.5). Se agrega el **reparto de los tres documentos** (qué es visión / estructura / requisitos) arriba del archivo. El **cuaderno digital** pasa a sección propia (§3): desarrollo interno, **tipo libro a pantalla completa en horizontal**, con **croquis escaneados** y **ligado a las entradas de la wiki** (es la capa visual de la wiki) más una interfaz gráfica auxiliar. Se Justifica por qué **Hermes** y no OpenClaw / Claude Code / Codex (§4.5) y se aclara que **OpenCode + Antigravity** son para el desarrollo propio. Modelos: **OpenCode Go** hoy → **Ollama** en el estudio → OpenRouter si hace falta (§4.6). Stack corregido: **AutoCAD versión completa** (no LT, habilita la vía cloud), **FreeCAD** como opción libre y siempre abierta en la otra PC de desarrollo (Linux), **Rhino 8 vs Rhino 9 + Hops**, BIM por FreeCAD + IfcOpenShell, **Unreal** para lo custom y escalable a VR, Postgres + MySQL de Leantime, Leantime como gestor de proyectos, alternativas libres para reuniones (Jitsi/LiveKit + faster-whisper) y agenda self-hosted. Se agregan la **regla de automatizar vs. hacerlas a mano** (§6.2, "se automatiza el trabajo, no la responsabilidad") y **cuándo Telegram y cuándo Discord** (§6.5). Secretos, backup y acceso remoto salen del stack de visión: son de ESTRUCTURA.
- **Los tres documentos del proyecto, sin mezclas**: se definió la regla de reparto (**VISIÓN** = qué es y para qué · **ESTRUCTURA** = dónde vive y cómo se conecta · **REQUISITOS** = qué tiene que cumplir y cómo se mide) y se **movió** el contenido que estaba en el lugar equivocado. Ahora existen `proyectos/MVP_07-studio-os-sistema/{VISION,ESTRUCTURA,REQUISITOS}.md` y nada más. **VISION.md** conserva el problema, el recorrido, el cuaderno digital, Hermes en conceptual, el stack con sus alternativas, las decisiones de producto y las preguntas de producto; las conexiones del agente, los modos de ejecución, el modelo, la matriz de automatizar/persona, los niveles A-D, el camino y el detalle de las preguntas técnicas **salieron** de ahí. **ESTRUCTURA.md** (nuevo) lleva la vista general, dónde vive cada pieza, el agente y sus conexiones, las integraciones una por una, el contrato entre componentes, el registro y el grafo, seguridad/secretos/backup/acceso remoto, cómo se construye el cuaderno digital, la puesta en marcha y las 6 decisiones técnicas en formato Nygard. **REQUISITOS.md** (nuevo) lleva alcance y no-alcance, actores y permisos, 13 casos de uso, RF-01 a RF-20 con trazabilidad, RNF-01 a RNF-15, 18 criterios de aceptación Given/When/Then, la gobernanza A-D, la matriz de qué automatiza el agente y qué hace la gente, 9 métricas con baseline, 11 decisiones abiertas con impacto y momento, y el plan de entrega por tramos T0-T6. Borrado el `00-filo-mvp_07.md` (borrador técnico): su contenido quedó distribuido en los tres documentos y en el historial de git.

## 2026-10-27 (tarde 9) — Causa raíz del corte sin hatch hallada + scripts de configuración listos (pendiente de ejecutar)

- **Causa raíz (documentada en la ayuda oficial):** no era el `Pattern Scale` del Section Style sino **"Enable hatch scaling"** de *File > Properties > Hatch*. El manual: **Enabled** → "Hatch patterns in model viewports are scaled by the **Model space hatch scale** value" · **"Hatch patterns in detail views print with the same scale regardless of the zoom factor"**; **Disabled** → "Hatch patterns will not scale". Con el escalado apagado la trama se dibuja en el espacio del modelo → a 1:30 mide **0,03 mm en el papel** → invisible en la lámina y visible en la vista de trabajo. **§9.15 reescrito** con el mecanismo correcto (y la tabla del `Pattern Scale` queda como el caso "escalado desactivado").
- **Segundo hallazgo — `SetScale` está roto en Rhino 8:** un usuario de McNeel (junio 2024) lo reportó y **Dale Fugier publicó el script que sí funciona**: `SetActiveDetail` → `ZoomExtents` → `IsProjectionLocked = True` → `SetScale(...)` → **`CommitChanges()`** (sin este último paso la escala no aplica). Documentado en §11.12.
- **API de Section Styles de Rhino 8 verificada** con un probe sobre el 8.5 (los 14 miembros escribibles de `SectionStyle`, `Layer.SetCustomSectionStyle(SectionStyle)`, `plano.Attributes.AddClipViewport(id)`, `doc.ModelSpaceHatchScalingEnabled` / `doc.ModelSpaceHatchScale`, `doc.Views.Redraw()`) → nuevo **§10.9**.
- **Nuevo script `scripts/configurar-corte-hatch-rhino.py` + notas** (7 fases: escalado de tramas → 13 Section Styles → lámina `UY-CORTE-HATCH` + detalle `A-A-HATCH` a 1:30 → copia de cámara → secuencia de SetScale de V8 → `AddClipViewport` del plano → `doc.Views.Redraw()`). **No guarda el documento** (decisión del usuario). Se acompaña de `scripts/inspeccionar-seccion-rhino.py` (inspección de solo lectura) ya creado.
- **Decisiones del usuario:** vista nueva en una **lámina aparte** (el corte A queda intacto) · las **13 capas de material** con patrón · **no guardar**.
- **Bloqueo:** el **puente MCP está caído** (puerto 9876 sin listener; log del puente termina el 26/10 08:36) y el MCP responde `WinError 10061`. Rhino sí está corriendo con `3D-casa_uruguay_clase.3dm` (12 MB, vista `[iso]`). Falta que el usuario ejecute en Rhino: `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`.
- **Riesgo abierto:** si la madera del DWG es **malla** o superficie abierta, no hay sección que rellenar → la inspección lo define y se decide (convertir o contorno).
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 8) — La lámina en blanco y negro con los hatches del corte: las 4 palancas y el matiz de layout

- **Pregunta del usuario:** cómo hacer para que la vista del layout muestre en blanco y negro y los hatches del corte como en la pantalla. Documentado en **§11.7** (subsección nueva) y en la tabla de errores.
- **Las cuatro palancas, que se confunden entre sí:**
  1. **Ver en pantalla cómo va a salir impreso** → `PrintDisplay` (o el menú del título del viewport → *Print Preview*): la vista muestra los **colores y anchos de impresión**. La **vista previa del diálogo `Print`** muestra el resultado final, con la conversión a gris incluida.
  2. **Imprimir en blanco y negro** → `Print` → **Output color** → **Black and white** ("converts colors to gray scale").
  3. **Fondo blanco** → `Print` → *Visibility* → desmarcar *Background color* (y *Background bitmap* / *Wallpaper*); en el detalle, el fondo lo define el modo de visualización → *Options > View > Display Modes > [modo] > Viewport > Background* → *Solid color* blanco o *Transparent*.
  4. **Hatches del corte iguales a la pantalla** → en el **modo del detalle**: *Objects > Clipping Planes* → **Use section styles** + **Show fills**; el relleno toma el color del **Section Style**, que **pisa el color de impresión**.
- **Matiz documentado:** en la lámina mandan las propiedades **Layout / Detail Print Color** y **Layout / Detail Print Width** de la capa, no las de `Print Color` / `Print Width` (que son para imprimir desde el espacio de modelo).
- **Consecuencia de diseño:** en blanco y negro los materiales **no se distinguen por color → se distinguen por patrón**. Eso vuelve críticas las dos reglas ya documentadas: **un patrón por material** (§10.6) y **`Pattern Scale` a la escala del papel** (§9.15 → 90 para 3 mm a 1:30). Para línea negra clásica: *Boundary → Color* negro y *Hatch → Pattern Color* negro o `By Object` con la capa en negro; el *Width Scale* del borde (1,0 / 1,5) es el peso de la línea del corte.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 7) — Lectura del `.3dm` (sin Rhino), script de inspección de solo lectura y diagnóstico del patrón de trama

- **Inspección del archivo:** el `.3dm` de Rhino 8 va **comprimido** → el escaneo de cadenas del binario no revela ni capas ni ajustes. Se comprobó que **no hay `rhino3dm` instalado** en los tres Python disponibles (`P:\Anaconda\envs\comfyenv\python.exe`, `P:\Anaconda\python.exe`, `python`), y que `rhino3dm` tampoco serviría: no expone Estilos de sección ni ajustes de modo de visualización.
- **El puente MCP está caído** (puerto 9876 sin listener; el log termina el 26/10 08:36) → para inspeccionar el documento vivo hace falta **un comando del usuario** en Rhino: `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`.
- **Archivo en trabajo detectado:** `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay_clase.3dm` (11,5 MB, 27/10 08:23), más reciente que `3D-casa_uruguay_02.3dm` (0,8 MB, 07:14).
- **Nuevo script `scripts/inspeccionar-seccion-rhino.py` + `scripts/inspeccionar-seccion-rhino_notas.md`**: inspección de **solo lectura** dentro de Rhino 8 que vuelca (1) los planos de corte con todas sus propiedades, (2) las capas con su **Estilo de sección** (patrón, escala, rotación, colores), (3) los objetos por tipo y cuántos son **cerrados**, (4) las láminas y sus detalles con modo de visualización y escala, y (5) dónde viven *Show fills* / *Use section styles*. Escrito en Python 3 compatible con IronPython 2.7, con `# NOTA ES:` línea por línea.
- **Nuevo §9.15 — el patrón de la trama no se lee en la lámina**: la trama del corte se dibuja en el **espacio del modelo**, así que con `Pattern Scale` = 1,0 (1 mm de patrón) a 1:30 el patrón mide **0,03 mm en el papel** → se ve liso o gris. Fórmula: `Pattern Scale = (separación deseada en el papel × escala) / separación base` → para 3 mm de papel a 1:30, **Pattern Scale = 90**; tabla de valores para 1:20 / 1:30 / 1:50; y la advertencia de que **la hoja AIZ tiene el mismo problema** (1,0 a 1:50).
- **Respuesta sobre la regeneración de la vista:** Rhino 8 **no tiene comando `Redraw`**. Las vías de forzar el redibujado son: cambiar el modo de visualización (`SetDisplayMode`), `Zoom` → `Extents`, apagar/prender el plano (`Disable`/`EnableClippingPlane`), restaurar una vista guardada, o `SetRedrawOff`/`SetRedrawOn` (solo scripting). Y el control decisive: **File > Print > Preview** reevalúa el dibujo → si la trama aparece en la vista previa y no en pantalla, el archivo está bien y lo que falla es la caché de pantalla.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 6) — Corte A resuelto: viewport re-armado, escala 1:30 y guía de los hatch en el detalle

- **Resuelto por el usuario:** el `ClippingPlane` del corte A se veía "a medias" / "como si fueran dos" (`SelClippingPlaneInViewport` → "No objects added to selection", o sea **ningún plano recortaba esa vista**). La causa fue el **viewport mal armado**: la solución fue **re-armar el detalle** con `Detail` → `Add` (nuevo detalle), `Scale`, `Projection` y `Lock`, y volver a tildar el detalle en *Views Clipped* → *Layout Space*.
- **La escala del corte A quedó en 1:30:** 1 unidad de layout en **mm** = **0,03 m** del modelo (se escribe `1` y `0.03`, **con punto decimal**). Equivalencias: 1 mm de papel = 30 mm de modelo · 1 m del modelo mide **33,3 mm** en la hoja.
- **Tabla de escalas ampliada** (§11.4) con **1:30** y **1:40**, y con la tabla de **cuánto modelo entra en el detalle** de 400 × 270 mm: a 1:30 entran **12 × 8,1 m** → si el corte tiene que abarcar la casa completa (≈14 m) no alcanza, y las escalas que sí entran son **1:40** (16 × 10,8 m) o **1:50** (20 × 13,5 m).
- **Nuevo §9.14 — el corte se ve en el detalle pero sin hatch**: checklist de 7 puntos, porque el relleno de la sección lo dibuja el **modo de visualización** y el detalle tiene **su propio modo** → 1) el modo del detalle debe ser el mismo que el de la vista de trabajo (Shaded; el relleno solo existe en modos shaded) · 2) en *Options > View > Display Modes > [modo] > Objects > Clipping Planes*: **Show fills** ON y **Use section styles** ON · 3) el plano en `By Layer` · 4) los objetos en `By Layer` (no `By Clipping Plane`) · 5) la capa con *Detail On* encendido y Section Style ≠ `None` · 6) la sección del objeto debe ser **cerrada** (una superficie abierta o una malla no se rellenan) · 7) si el relleno sale plano en vez de tramado, es *Use section styles* apagado.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 5) — Corte A: `SelClippingPlaneInViewport` sin selección → batería de 3 pruebas documentada (§9.13)

- **Resultado de la prueba del usuario:** `SelClippingPlaneInViewport` → **"No objects added to selection"** → hecho concluyente: **ningún clipping plane está recortando esa vista**. Lo que se ve como "corte" (y la impresión de "dos planos") **no es un recorte vivo** en esa vista.
- **Nuevo §9.13 — "El corte que no es un corte": 3 pruebas para separar las causas**, en orden:
  1. **¿En qué vista estabas?** El comando actúa sobre la vista activa → correrlo con el **detalle del corte A activado** (doble clic) y por separado en la isométrica. Si en el detalle devuelve *No objects*, el plano recorta el modelo pero **no el detalle** → se tilda en *Views Clipped* → *Layout Space*.
  2. **¿Geometría o redibujado viejo?** `Zoom` → `Extents` en esa vista: si el fantasma desaparece → era la caché de la sección del plano borrado (re-crear la vista guardada + revisar *Named views set clipping planes*); si sigue → es geometría.
  3. **Si es geometría:** el DWG trajo el **corte 2D de inicio** junto con la base 3D, y según la opción de importación **`Convert wide polylines to surfaces`** ese 2D puede haber entrado como **superficies** — que dentro del modelo se ven exactamente como un plano de corte. Se localiza con ventana de selección + `What` (tipo y capa) y se apaga la capa; la salida prolija es moverla a `REF-2D` o reimportar con la opción **OFF**.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 4) — El corte fantasma (un plano, se ven dos) diagnosticado + receta completa del viewport de detalle y del texto de la hoja

- **Síntoma reportado por el usuario:** en el corte A hay **un solo** clipping plane, pero se ve **como si fueran dos**. El plano anterior fue borrado y su corte sigue apareciendo.
- **Causa documentada y verificada** (*Tools > Options > View*): la opción **"Named views set clipping planes"** — "Restoring a named view also restores the **enable state** of the clipping planes saved with the view". Las **Named views guardan el estado de recorte**: si la vista se guardó con el plano viejo activo, al restaurarla vuelve ese corte, y **borrar el plano no lo saca de la vista guardada**.
- **Test decisivo documentado:** `SelClippingPlaneInViewport` selecciona los planos que recortan la vista actual → si selecciona **uno solo** y aun así se ven dos cortes, el segundo **no es un plano**: es estado guardado o redibujado viejo.
- **Solución documentada en §9.12** (en orden): 1) desmarcar *Named views set clipping planes* en *Options > View* (y si hace falta *Named views set CPlane* / *set projection*) · 2) volver a restaurar la vista · 3) **re-crear la vista guardada** (`NamedView` → *Save as*, nombre nuevo, desde el estado actual) · 4) forzar el redibujado (§9.11).
- **Nuevo §11.12 — Receta completa del viewport de detalle, de principio a fin**: preparación del documento (unidades, *Enable layout space scaling*, Section Styles) → la lámina (A3 landscape 420 × 297 mm) → el detalle (`Detail` → `Add` de (10,22) a (410,292) = 400 × 270 mm → `Projection` → `Scale` `20`/`1` → `Lock` → *Title* `A-A` → *Display mode*) → el corte dentro del detalle (*Views Clipped* → *Layout Space*, `Depth = 0`, *Section Style* `By Layer`) → **verificación de la escala con `Distance`** → el marco (*Print Width*) → texto → impresión. Incluye la trampa de que `Projection` **no tiene axonométrica 30/60** (esa es cámara de una vista guardada: `CopyViewportToDetail` o `NamedView` → *Import from 3dm file*).
- **Nuevo §11.13 — El texto de la hoja: rótulos, escalas y referencias**, en tres familias: **datos de la lámina** (`Text` en espacio de papel, con las alturas 5 mm / 3,5 mm / 3 mm / 2,5 mm que se usaron en AIZ) · **leyenda de materiales** (`Text` + muestra de trama con `Hatch`) · **referencias numeradas** (`Dot`, que se dibuja en **espacio de pantalla** y no cambia con el zoom, con *Secondary text*; y `Leader` para las llamadas con flecha, con *Text gap* y *Landing*). Se documenta **la regla de tamaño**: con **"Enable layout space scaling"** activado el texto dentro del detalle imprime a su tamaño nominal; sin eso, a 1:50 un texto de 3 mm en el papel necesita **150 mm** en el modelo. Incluye los **Text Fields** (`%<Area("id")\*2>%`, `CurveLength`, `Volume`) para rótulos dinámicos.
- Cheatsheet +3 filas (`Dot`, `Leader`, `Hatch`) y 6 URLs nuevas verificadas 200.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 3) — Vistas por defecto, estilos visuales, tabla de escalas y diagnóstico del corte a medias

- **Nuevo §9.8–§9.12 en la guía** (todo verificado contra la ayuda oficial de Rhino 8):
  - **Vistas por defecto:** `SetView` (World Top / Bottom / Left / Right / Front / Back / Perspective + las del PlanoC) e `Isometric` (`NE` / `NW` / **`SE`** / `SW` + `ZoomExtents`, siempre en **proyección paralela** mirando desde el cuadrante hacia el origen). En este proyecto: **`Isometric SE`** + `SetView World Top/Bottom/Left`. Incluye la navegación (`Pan`, `RotateView`, `Zoom`, `UndoView`, `Turntable`, `WalkAbout`…).
  - **Vistas guardadas** (`NamedView`): *Save as* · *Restore* · **Import from 3dm file** · *Create Using Widget* · *Edit by looking* · *Animation*. Dato clave: **la axonométrica 30/60 de AIZ (`axo3060`) no es una vista estándar sino una vista guardada** → se trae al archivo nuevo importándola desde `set-ej_corte_A3-1-50.3dm`.
  - **Estilos visuales** (Tools > Options > View > Display Modes): los 11 modos (Wireframe, Shaded, Raytraced, Rendered, Ghosted, X-Ray, **Technical**, **Artistic**, Pen, Monochrome, Arctic) con su uso en el proyecto, `SetDisplayMode` y sus atajos, y los grupos de ajustes (Viewport, Shading, Visibility, Lighting, Grid, Objects, Shadows).
  - **El corte dentro de un modo visual** (Objects > Clipping Planes): **Use section styles** · **Show fills** (solo modos shaded) · *Show edges* + *Edge thickness* · *Shade selected plane* + *Transparency %*. **Si "Use section styles" está apagado, el corte no sale con el hatch del material.**
  - **Cómo se regenera la vista**: cambiar el modo de visualización · `Zoom Extents` · apagar/prender el plano (`Disable`/`EnableClippingPlane`) · mover el plano · restaurar una vista guardada.
  - **Diagnóstico del layout de corte A** (el corte sale a medias, "como si hubiera otro plano"): tabla de 8 causas con su comprobación y su solución — el plano no habilitado en ese detalle (*Views Clipped* → *Layout Space*), **dos** planos activos (`SelClippingPlaneInViewport`), `Custom Depth` con `Depth` > 0, "Use section styles"/"Show fills" apagados, estar mirando la cara de atrás (`Invert direction`), la vista sin regenerar, el color del Section Style pisando el print color, y el corte que no sale en el PDF.
- **Tabla de escalas del viewport** (§11.4 ampliada): con lámina en mm y modelo en m — **1:500** (`2`/`1`) · **1:200** (`5`/`1`) · **1:100** (`10`/`1`) · **1:50** (`20`/`1`) · **1:25** (`40`/`1`) · **1:20** (`50`/`1`) · **1:10** (`100`/`1`), con la equivalencia "1 mm en la hoja = X/1000 m en el modelo" (el enunciado del usuario: 1 mm = 0,01 m → **1:10**), la regla inversa "1 m del modelo mide 1000/X mm" y la tabla de **cuánto modelo entra en el detalle** de 400 × 270 mm (1:50 → 20 × 13,5 m).
- **Los tres sitios donde hay escala**: el detalle (el que manda), el `Print` (*On paper = In model*) y el *Model space scale* del estilo de anotación.
- **Cheatsheet** +8 comandos (`SetView`, `Isometric`, `NamedView`, `SetDisplayMode`, `SelClippingPlaneInViewport`, `Zoom`, `Enable`/`DisableClippingPlane`) y **errores frecuentes** +7 filas.
- **Verificación:** las 52 URLs del documento comprobadas por HTTP HEAD → todas **200**.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde 2) — La hoja: layout, viewport de detalle, escala y texto en papel documentados

- **Nuevo §11 en la guía** (`01-comandos-rhino-8.md`): la lámina (`Layout` / `LayoutProperties`: nombre, cantidad inicial de detalles, impresora, tamaño A3, orientación, ancho y alto en mm) · las **3 formas de crear el viewport de detalle** (`Detail` a mano · `CopyViewportToDetail` para traicionar la cámara de un viewport de modelo · `ImportLayout` para traer la lámina entera de otro `.3dm`) · la **tabla de variantes de configuración** del viewport con la elegida (AIZ: `AIZ-CORTE-A`, axonometría 30/60 en paralelo, Shaded, 1:50, `Lock`, `No Print` en el marco, clipping plane habilitado dentro del detalle) y las variantes según el uso (corte de obra / axonométrica de presentación / planta de obra / detalle constructivo) · la **escala** con su tabla 1:20 / 1:50 / 1:100 y su verificación · el **texto en el espacio de papel** (`Text`: paso a paso, altura en unidades de layout, `Mask`, `Text Field`, alineación) · los **estilos de anotación** y el **gotcha del DWG** · el **`Print`** con los valores de esta lámina.
- **El dato clave de la escala:** el número que se tipea en cada prompt del `Scale Value` está **en las unidades de ese espacio** (`___ <units> on layout` / `___ <units> in model`). Con la lámina en **mm** y el modelo en **m**, la escala 1:50 se escribe **20** y **1** — no 1 y 50. Verificación: **1,00 m del modelo = 20,0 mm en el papel** (el número medido en AIZ).
- **Gotcha descubierta en la ayuda oficial:** el comando `Open` **desactiva "Enable layout space scaling"** cuando se abre un DWG/DXF en Rhino → en este archivo (importado de DWG) hay que **activarlo** en *File > Properties > Annotation*, para que los textos de las cotas dentro del detalle conserven tamaño fijo en el papel.
- **Numeración corrida** al insertar el capítulo: la guía quedó en 0–15 (cheatsheet §12, errores §13, bitácora §14, referencias §15) y se ajustaron las referencias cruzadas.
- **12 URLs nuevas verificadas 200**: `text.htm` · `documentproperties/annotation.htm` · `print.htm` · `copyviewporttodetail.htm` · `importlayout.htm` · `layoutproperties.htm` · `importannotationstyles.htm` · `seldetail.htm` · `rotateview.htm` · `tiltview.htm` · `printdisplay.htm` · `commands/detail.htm`.
- **Corrección técnica:** una edición anterior dejó 8 caracteres corruptos (armenio) en la tabla de variantes de configuración → reemplazados por PowerShell a nivel de bytes y verificado que el documento no tiene caracteres fuera del latino.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 (tarde) — Section Styles por capa documentados + convención de nombres de comando en inglés

- **Convención de nombres fijada por el usuario:** los comandos se nombran **en inglés primero** (lo que se tipea) y, entre paréntesis, la traducción de Rhino en español. Se aplicó a todo el §9 y §10 de la guía, y quedó anotada en el encabezado del documento.
- **Nuevo §10 — Section Styles: cómo se hace el relleno por material** (documentado desde la ayuda oficial `popup_moreinformation/sectionstyle.htm`, `commands/layer.htm`, `properties/object.htm` y el User's Guide *Clip & Section | Intro to Section Styles*):
  - Los tres niveles y cuál manda: **por clipping plane** (`Section Style` = `By Layer` / `Custom`), **por capa** (`None` / `Custom`) y **por objeto** (`By Layer` / `By Parent` / `By Clipping Plane` / `Custom`).
  - El diálogo campo por campo: **Hatch** (Pattern · Pattern Color · Pattern Rotation · Pattern Scale · Background · Section open objects) y **Boundary** (Show · Linetype · Width Scale · Color).
  - Paso a paso por capa: Layers panel → columna **Section Style** → click en la celda → `Custom` → diálogo → OK/Apply. Con atajo multi-capa: `Ctrl`+click en el panel de capas.
  - **Por qué cada capa tiene que estar diferenciada:** el plano de corte llena cada objeto con el estilo de su capa → capa en `None` = corte sin relleno; todas las capas con el mismo estilo = corte uniforme y se pierde la lectura de materiales. Es la lección de AIZ (3 de 7 capas con Section Style → el resto del corte sin rellenar).
  - Tabla de los 13 materiales con patrón, color, rotación, escala y ancho de borde; las capas de referencia quedan en `None`.
  - **Los Section Styles no viajan con el import de un DWG** (son propiedad del documento): la vía rápida para llevarlos al archivo nuevo es `LayerStateManager` (Layer States → Save → Import → Restore), que restaura también el Section Style.
- **§9 reescrito con nombres en inglés** y ampliado: se agregó **§9.3 "how to work with clipping planes, day to day"** (mover, redimensionar, profundidad, invertir, recorte por objeto/capa/vista, nombre y etiqueta, guardar como Named View o Named CPlane, borrar) y **§9.6** con el camino corto de la sección al dibujo (9 comandos con sus opciones).
- **Avance del usuario:** el `ClippingPlane` ya está creado en `3D-casa_uruguay_02.3dm` y los **Section Styles ya configurados**. La bitácora §13.5 y §13.6 quedaron actualizadas con el estado real.
- **Verificación:** las 32 URLs del documento comprobadas por HTTP HEAD → todas **200** (el único 403 fue una URL malformada por el regex de chequeo, no un enlace roto del documento).
- **Navegación documentada** (a pedido del usuario, verificada contra el *User's Guide — Navigation & Display* de McNeel y la página *Mouse options*): en la **isométrica** (perspectiva) el **botón derecho orbita**, `Shift` + botón derecho hace **pan**, `Ctrl` + botón derecho hace **zoom** (suave) y la rueda hace zoom escalonado. En las vistas paralelas (Top / Front / Right) el botón derecho hace pan y `Shift` + botón derecho rota. Quedó en la subsección **Navegación con el mouse** del cheatsheet (§11) y como nota operativa en la bitácora §13.5.
- **Idioma:** la prosa de §9 y §10 quedó en español (el vault es en español) manteniendo **comandos, opciones y rutas de menú en inglés**, que es como aparecen en la interfaz del Rhino del usuario, con la traducción del comando entre paréntesis.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-27 — Casa Uruguay: 3D importado del DWG en un archivo nuevo + capítulo del plano delimitador documentado (bitácora viva)

- **Corrección de un error propio:** la guía de comandos afirmaba que *"en AIZ el corte falló porque el modelo era malla"*. **El corte de AIZ salió bien** —la hoja A3 a 1:50 quedó hecha y renderizada—; lo pendiente fue el **relleno por material** (3 de 7 capas con Section Style) y una geometría abierta. Corregido en la guía (§0) y en la ficha del proyecto, con la regla que queda: cada material con su Section Style desde el arranque.
- **Investigación en la ayuda oficial de Rhino 8 en español** (13 URLs verificadas 200 el 27/10): la familia de cortes de Rhino 8 **no está en la barra Sólidos** — vive en la barra nueva **Secciones** (menú *Dibujo > Secciones*), en **Visualización** (`PlanoDelimitador`) y en **Plano / Creación de superficies** (`PlanoDeCorte`). Nombres ES/EN documentados: `PlanoDelimitador`/`ClippingPlane`, `PlanoDeCorte`/`CutPlane`, `SeccionesDeCorte`/`ClippingSections`, `VerSeccionesDeCorte`/`ViewClippingSections`, `ExtraerSeccionesDeCorte`, `ExtraerSegmentosDeCorte`, `DibujosDeCorte`, `DibujoDeCorteAnidado`, `Sección`/`Section`.
- **Diagnóstico del corte invisible en la isométrica:** un plano delimitador recorta **solo las vistas donde está habilitado** → se prende en Propiedades > *"Vistas delimitadas"* o con `ActivarPlanoDelimitador` teniendo la vista activa. Causas documentadas: rectángulo del widget más chico que el modelo (el widget se pone **rojo** cuando el plano no intersecta la caja de los objetos), lado visible invertido (`Invertir dirección`), profundidad ≠ 0.
- **Nuevo §9 en la guía de comandos:** insertar el plano (5 variantes; `Vertical` desde la vista Planta es la más simple para un corte de obra), los 6 interruptores para prender/apagar, la configuración completa (12 propiedades del plano delimitador), el camino corto de la sección al dibujo (9 comandos) y la receta del corte `A-A`.
- **Nuevo §12 — bitácora viva** de `3D-casa_uruguay_02.3dm`: import del DWG ✅ (con la tabla de opciones de importación de DWG y el porqué de cada una), escala ✅, verificación del contenido ⏳, plano de corte ⏳, capas + Section Style ⏳. La bitácora sigue creciendo a medida que avanza el modelado.
- **Contexto del trabajo:** el usuario importa `CAD-UY-xa-RHINO_02.dwg` (5,3 MB, dibujado en **metros** → entra 1:1, sin conversión) en un archivo nuevo `3D-casa_uruguay_02.3dm`; el DWG trae el 3D de base y el corte 2D de inicio. Los viewports ya establecidos de la hoja AIZ se reutilizan.
- **Modo de trabajo:** el agente documenta y guía; el modelado lo ejecuta el usuario. Sin ejecuciones de Rhino ni llamadas al MCP.
- **Sesión:** `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md`.

## 2026-10-26 (mañana) — Casa Uruguay: 3D en Rhino 8 arrancado desde el PDF de Arraigada (escala verificada + 17 capas + guía de comandos)

- **Puente MCP relanzado:** Rhino se había reiniciado a las 06:14 sin el script → puerto 9876 vacío (`WinError 10061`). Relanzado con `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`.
- **Hallazgo:** el usuario ya tenía importado el PDF de *Casa frente al mar* (Diego Arraigada, Manantiales, Uruguay, 2011, 140 m²) en `set-01-uy.3dm` — 100.557 objetos (96.136 polylines + 3.001 hatches), 35 MB, **ya en metros**. Se respetó su trabajo en vez de reimportar.
- **Calibración verificada:** la escala gráfica de cada planta mide **exactamente 5,000000 m** (x 13,281836→18,281836 en PLANTA 1 y PLANTA 2), con ticks a 1,000 y 2,000 m: es la barra `0·1·2·5` del PDF. **El import ya está a escala real**, no hay que reescalar. Dato de contexto: las plantas publicadas están a ~1:175, no a 1:50 → la barra manda, no la escala nominal.
- **17 capas creadas** con Section Style propio: 13 de material con los nombres del estudio (`EST-MAD`, `CARP-MET`, `CARP-VID`, `MAD-MARCO_PINO`, `01-PLACA YESO`, `02-FENOLICO`, `03-FILM_POL`, `04-BAST-2.6`, `05-AISL-LANAVID`, `06 TYVEK`, `07-CALV-2.2`, `08-CHAPA-NEGRO`, `09-ZING-CHAPA_GALV`) + 4 de referencia (`REF-PDF-P5`, `REF-PDF-P6`, `REF-TXT`, `00-EJES`). Cada material con patrón y color → los cortes saldrán con hatch por material desde el primer día.
- **Archivo nuevo:** `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay.3dm` (mismo nombre que el DWG gemelo `3D-casa_uruguay.dwg`); el original `set-01-uy.3dm` queda intacto. La escritura a Drive tardó ~6 min.
- **Guía de comandos del proyecto:** `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8.md` — importar PDF, `Line`/`Polyline`/`InterpCrv`, `Box` para parantes, `ExtrudeCrv` (opciones `Solid`, `BothSides`, `Direction`), `Offset` + `PlanarSrf` + `ExtrudeCrv` para **dar espesor a una polilínea**, **chapa sinusoidal de alto de onda 0,036 m** en 6 pasos, **zinguerías** con `Sweep1`, y `PushPull` / `MoveFace` / `Gumball` para extender o mover una cara de un sólido en el espacio. Cheatsheet y errores frecuentes incluidos.
- **Fricción detectada y corregida:** el MCP de AutoCAD no entraba a **AutoCAD LT 2027** — `tools/autocad-mcp/autocad_mcp/acad_core.py:60` solo probaba los ProgID `25.1`, `25` y el genérico, y el registro de Windows tiene `AutoCAD.Application.26`. Se agregó `Application.26` al `PROG_IDS` (fuente y copia instalada en el venv); entra en vigor al reiniciar el servidor MCP.
- **Pendientes:** separar el import en `REF-PDF-P5`/`REF-PDF-P6`, redibujar la planta y extruir a sólidos (alturas de la pág. 6: +250, +263, +285, +295, +300 cm), construir chapa/zinguerías/parantes, y la hoja A3 con corte 3D y pie de página.
- **Sesión:** `raw/sessions/2026-10-26-sesion-casa-uruguay-rhino.md`.

## 2026-10-25 (noche) — Rhino 8: corte 3D en hoja A3 a 1:50 construido y verificado + docu unificada en un solo playbook

- **Puente MCP caído y relanzado:** el script `scripts/rhino-mcp-server-rhino.py` vive dentro del proceso Rhino, así que al reabrir Rhino el puerto 9876 queda vacío (`WinError 10061`). Se relanzó desde la línea de comandos con `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`. El playbook interno `pbook-rhino-mcp.md` todavía indica `MCPConnect`, que no existe en esta instalación: pendiente de corregir.
- **Archivo medido por MCP (solo lectura):** `set-ej_corte.3dm` — 161 objetos (159 mallas, 158 cerradas + 1 abierta `Object_3`, y 1 clipping plane `A-A`), unidades en metros, capas de material `3D-EP-MAD` 84 · `3D-MURÒ` 45 · `3D-REV-01` 15 · `3D-LOSA` 8 · `3D-VIDRIO` 5 · `3D-SOL-EXT01` 1 · `3D-BASE` 1; section style configurado solo en 3 de las 7 capas; bbox 10,37 × 22,00 × 18,15 m; 4 viewports (`axo3060`, `Top`, `Front`, `Right`) ya en proyección paralela.
- **Hoja A3 a 1:50 construida y verificada:** página `AIZ-CORTE-A` (420 × 297 mm) con un detalle de 400 × 270 mm en (10, 22)–(410, 292), cámara `axo3060` 30/60 en paralelo y Shaded, clipping `A-A` habilitado dentro del detalle y pie de hoja de 2 líneas en espacio papel (5 mm + 3 mm). Escala medida sobre la hoja: **1,00 m del modelo = 20,0 mm**.
- **Hallazgo de encaje:** el set completo a 1:50 necesita 447 × 488 mm y el A3 útil ofrece 400 × 277 mm; el recorte definitivo lo hace el propio plano de corte, porque el lado visible (X ≥ 575) proyecta 19,94 × 13,88 m → 398,8 × 277,5 mm a 1:50.
- **Docu unificada:** los tres documentos (`01-protocolo-cortes`, `02-playbook-corte-hatch-iso`, `03-plan-corte-3d-hoja-a3-1-50`) se fusionaron en **un solo playbook**: `proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8.md`, con el estado verificado del archivo, los 8 ítems con su estado, el resultado de la corrida y una tabla de lecciones de API de Rhino 8 (escala del detalle, setters de cámara de solo lectura, `SetPageAsActive` para texto en espacio papel, `doc.Save()` con `IsLocked`).
- **Fricción encontrada:** un `doc.Open` sobre el mismo archivo abierto dejó un diálogo modal, venció el timeout del MCP y el documento quedó `IsLocked` → `doc.Save()` devuelve `False`. Se resolvió con `SaveAs` a otra ruta y copia del archivo. La versión verificada quedó en `G:\Mi unidad\E#E.EDU\mora\set-ej_corte_A3-1-50.3dm` y en `activos/mvp_05-rhino-mcp/01-AIZ/set-ej_corte.3dm`.
- **Pendientes:** section style en las 4 capas sin estilo, Custom Depth de 1,00 m, resolver la malla abierta, imprimir el PDF vectorial (desmarcando "Clipping planes") y reemplazar el `.3dm` original de Drive cuando Rhino libere el archivo.
- **Sesión:** `raw/sessions/2026-10-25-sesion-rhino-corte-a3-1-50.md`.

## 2026-10-22 (tarde/noche) — Seguridad VPS: CVE PHP parcheado, SSH verificado y documentación infra completada

- **Alerta Contabo CVE-2026-109618/109619 (PHP RCE, CVSS 9.2):** recibida el 21/10. Leantime corría **PHP 8.3.30** (vulnerable, se exigía 8.3.36). **Resuelto:** backup MySQL (`/opt/backups/leantime_pre_upgrade_20261022.sql.gz`, 62K, 30 tablas) → `docker service update --image leantime/leantime:3.12.0 pitautech_leantime` → migración BD por CLI (`bin/leantime db:migrate --no-interaction` → OK) → verificado PHP **8.3.36**, contenedor healthy, HTTP 200.
- **Alerta Contabo CVE-2026-99999 (kernel, CVSS 9.3):** Contabo parcheó y reinició el host el 17-18/10 (coincide con uptime de 3 días al 22/10). Kernel `6.8.0-147-generic` parcheado. **Sin acción requerida** del lado del usuario.
- **SSH verificado por primera vez:** `ssh contabo` funciona (alias en `C:\Users\Solch16\.ssh\config`, clave `P:\.ssh\id_ed25519` → `pitautech-contabo`). **La clave privada nunca se leyó ni se expuso**; solo se usó el alias. `.gitignore` actualizado con `*.pem`, `id_*`, `ssh-key*` para blindar contra commits accidentales.
- **Auditoría del VPS (12 servicios Swarm):** n8n, Leantime 3.12.0, MySQL 9, Postgres 17, Redis 7 (×2), Chatwoot 4.12.1 + sidekiq 4.9.1 ⚠️, pgvector 17, Qdrant, EasyPanel, Traefik. Disco 31%, RAM 3.2/7.8 GB, load 0.00. **Hallazgo:** contenedor leftover `mystifying_shannon` de pruebas → eliminado. **Chatwoot sidekiq desincronizado** (v4.9.1 vs v4.12.1) → flag pendiente.
- **Docs obsoletas corregidas:** `wiki/glosario/software/n8n.md` (decía "no activo" con 10 workflows → reescrito "activo"), `ADR-INFRA-002` (Hetzner → sección "Estado de Implementación" con realidad Contabo/EasyPanel + 12 servicios), `backups.md` (stub vacío → política 3-2-1 con comandos), `anexo-stack-subencargados.md` (fila VPS ampliada), `wiki/estudio/00-index.md` (sección IT con runbook), `pbooks/00-index.md` (2 entradas nuevas).
- **Docs nuevas:** `wiki/estudio/it/runbook-vps-estudio.md` (ficha, acceso, mapa servicios, checklist post-caída, mantenimiento, incidentes), `pbk-vps-acceso-monitoreo.md` (SSH + 3 capas de monitoreo), `pbk-alertas-contabo.md` (flujo de respuesta a alertas CVE).
- **Pendientes documentados (sin ejecutar):** UptimeRobot (plan paso a paso en `pbk-vps-acceso-monitoreo`), n8n workflows (ingest Contabo + salud VPS — pendiente `s`), Chatwoot no se usa → 4 contenedores en RAM ociosa (pendiente decisión), apt upgrade 50 paquetes (pendiente ventana), backup automático diario, snapshot Contabo. Todo detallado en `runbook-vps-estudio.md` §Planes pendientes.
- **Sesión:** `raw/sessions/2026-10-22-sesion-vps-seguridad-monitoreo.md`.

## 2026-10-22 (noche) — Rhino para la entrega de la casa: investigación, creadores y reajuste a reunión 09:00

- **Pedido de Sol:** un documento en reportes que sintetice la investigación + mapa de creadores + cruce con los **47 videos `rhino`** del Takeout, y una ruta de modelado en Rhino para una **casa de tres niveles** desde un plano 2D de AutoCAD, con plantas, cortes y A3 en PDF.
- **Nuevo** `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` (294 líneas): síntesis de 11 fuentes verificadas 200 (guía McNeel *PushPull for Architects*, `Block`/`Insert`/`Layout`/`Print`/`Make2D`, How to Rhino, UGR, Discourse, rhinomcp) + mapa de **16 canales** + cruce sin duplicados + flujo de 10 pasos, cronograma, riesgos y checklist.
- **Nuevo** `specs/261022-ruta-modelado-casa-rhino.md` (141 líneas), aprobado y luego reajustado por dos hechos: **la reunión es mañana 09:00** (no 17:00) y **AutoCAD LT no modela en 3D**. LT queda para `AUDIT`/`PURGE`/`WBLOCK`/`DIST`; todo el 3D en Rhino. PDF v1 se exporta esta noche; cierre duro mañana **08:30**.
- **Flujo DWG ajustado:** `Insert` como bloque en `CAD-BASE` → duplicar → `Explode` sólo la copia en `CAD-WORK` → offset/extrusión; base original intacta y removible. Plantas superpuestas en Z=0 se separan por capa con `SelLayer` + `Move`.
- **Ficha de contenidos:** `raw/contenidos/2026-10-22-modelar-casa-rhino.md` (259 líneas, `propuesta`) generada por `@contenidos`; frenó en su gate y no tocó `wiki/`. Promoción a `wiki/fuentes` queda para después de la reunión.
- **Rhino:** 8.5.24072 está instalado, pero el puente MCP rechaza conexión (10061); falta correr `rhino_script.py` dentro de Rhino (Tools → RhinoScript → Run).
- **Decisión de cierre:** si no se consigue AutoCAD full, se avanza con Rhino. Sin commit: todo queda en el working tree.


## 2026-10-21 (madrugada) — Las fuentes del concurso como contexto de ChatGPT para Emilia (item `589` en Leantime)

- **Pedido de Sol:** que el análisis de fuentes se pueda replicar sobre el corpus del concurso (carpeta `AIxGaudi/Bibliography`, 31 PDF) y **compartirlo con el ChatGPT de Emilia sin romperle las sesiones que usa desde el celular**.
- **Hallazgo que define la vía (doc de OpenAI, oct/2026):** los **custom GPT están en retirada** — las cuentas personales (Free/Go/Plus/Pro) **ya no pueden crear ni publicar GPTs**; el retiro es el 11/12/2026 en Enterprise y la migración a *Plugins* apunta al 17/09/2026. La alternativa oficial y la adecuada para un equipo es el **proyecto compartido**: **se comparte por link o invitación, en web y en la app móvil**, y usa **memoria solo-del-proyecto** (no lee sus memorias personales ni conversaciones de afuera) → **sus chats quedan intactos y el corpus no se le mezcla**.
- **La vía concreta:** proyecto "AI×Gaudí" + **app de Google Drive conectada** (en un proyecto se puede pegar el link de una **carpeta** como fuente: *Add source → Google Drive*; la app **no pre-indexa** dentro del proyecto → consulta en vivo, siempre fresca). Límites: 5 archivos (Free) / 25 (Go, Plus) / 40 (Edu, Pro, Business, Enterprise) por proyecto, 10 por tanda.
- **Fuente única:** el vault sigue siendo el original (32 fichas + 31 transcripciones en `raw/pdf/`); el Drive es la copia compartida. **La API es para el lado vault** (n8n), no para la app del celular.
- **Leantime:** card `589` "Fuentes del concurso: corpus AIxGaudi como contexto para el ChatGPT de Emilia" (proyecto 4, milestone `463` M-A3, sprint 27, 5,04 h) + 8 subtareas `590`-`597` (decidir el material · exportar las fichas al Drive en 6 lotes · compartir la carpeta · conectar la app de Drive · crear el Project · probar desde el celular · escribir las instrucciones del contexto · documentar).
- **Documento nuevo:** `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` — la decisión de fondo, la vía, la respuesta a la coexistencia, **las 4 pestañas para abrir mañana**, los 5 pasos con pomodoros, la estructura de la exportación y las instrucciones del contexto.
- **Spec actualizado:** `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` §7 (pregunta 6 para Emilia) y §9 (registro de cambios).

## 2026-10-21 (madrugada) — El dashboard general pasa a ser la puerta (y todo a GitHub)

- **Pedido de Sol:** el "documento que engloba todo" debe ser **el dashboard** (`proyectos/STUDIO_OS-Emilia/presentacion/dashboard-mes1-emilia.html`), que ya es la entrada al resto; los `.md` **no hace falta que sean links** (se ve en otra computadora → importa la ruta del vault) y después hay que **subir todo a GitHub**.
- **Nuevo** `scripts/inyectar-puerta-temas-dashboard.py` + `_notas.md` → inyecta en el dashboard general la sección **"la puerta"**: los **6 temas** (fuentes · agentes Telegram · CAD/SET · Comfy · Leantime · estudio) con el estado en 1 línea + las **rutas del vault como texto** + el link a su dashboard; y abajo la franja con los **3 pendientes** de la reunión con Emilia. Además agrega la pestaña **"Temas"** al nav y la ruta del doc de la reunión a los `toplinks`.
- **Por qué un script y no editar el HTML:** el dashboard se regenera con `scripts/build-dashboard-semanas.py`, así que la puerta tiene que poder reinyectarse sola. Es **idempotente** (marcadores `<!-- PUERTA-TEMAS -->`; verificado 36541 → 36541 → 36541 bytes) y tiene `--dry`.
- **Verificado:** `check-dashboard-css.py` → 0 clases sin estilo; captura con Chrome headless → la sección se ve bien y el resto del dashboard quedó intacto; los 4 dashboards hermanos **ya** enlazaban al mes1 (no hizo falta retrofit).
- **Índice:** `proyectos/STUDIO_OS-Emilia/00-index.md` → la sección "Documentación vigente" arranca ahora con el **dashboard general** como puerta.
- **GitHub:** subidos los 300+ cambios acumulados de las sesiones (n8n de Emilia, corpus AI×Gaudí, CAD/SET, Comfy, dashboards, scripts, wiki, specs) a `master` → `origin`, para poder revisar el trabajo desde otra computadora.

## 2026-10-21 (madrugada) — Índice de la reunión: un solo documento con los temas a ver

- **Pedido de Sol:** "genera los documentos que registren esta forma de trabajo" + "**un SOLO DOCUMENTO APARTE** con el ítem de los temas que tenemos que ver en la reunión (sesiones trabajadas, .md creados y dashboards) sobre fuentes, agentes Telegram, CAD/SET, Comfy, etc".
- **Nuevo** `proyectos/STUDIO_OS-Emilia/presentacion/09-agenda-reunion-2026-10-21.md` → el documento único, con **6 temas** (fuentes · agentes Telegram · CAD/SET · Comfy · Leantime · estudio) y, por cada uno, tres bloques: **sesiones trabajadas** (con link a `raw/sessions/`), **.md creados** (con link a `specs/`, `proyectos/`, `raw/`) y **dashboards** (con link al HTML). Cierra con los 3 pendientes de Emilia y un **orden sugerido de 60 min** para la reunión.
- **Documentos actualizados con la forma de trabajo de hoy:**
  - `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` → nueva §2.b **"la forma más simple: un documento compartido en el Drive"** (un solo `.md` con índice + extractos por fuente; ella lo abre o adjunta en ChatGPT, desde el celular; el vault sigue siendo el original; sus ediciones vuelven por la sincronización y las baja el importador). El proyecto de ChatGPT queda como envoltorio opcional, no requisito.
  - `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` → **v2.1**: mapa de 9 workflows con los 3 nuevos (`Fa2AlIDqUntSWMrw` voz de Emilia · `2JogeOoT3Wjq2ncH` agenda de Emilia · `Msh31moofBKBwZId` despachador), el diagrama con las dos ramas y la nueva **§5.b** con el detalle de los flujos de Emilia (allowlist, Redis, memoria, credenciales, tools, eventos de Cal.com y las pruebas end-to-end).
  - `proyectos/STUDIO_OS-Emilia/00-index.md` → sección **"Documentación vigente (21/10)"** con los 8 documentos de trabajo (así se llega a todo desde la puerta del proyecto).
- **Inventario real (medido, no supuesto):** 88 sesiones en `raw/sessions/`, 10 specs, 5 dashboards HTML en `proyectos/STUDIO_OS-Emilia/presentacion/`, 2 grafos VR en `scripts/`.

## 2026-10-21 (madrugada) — Emilia con su propio flujo: agente de voz + subagente de agendamiento propios

- **Decisión de Sol:** Emilia deja de compartir el flujo de voz y **tiene el suyo completo** (Redis, memoria Postgres, prompt, credencial de Cal.com y subagente de agendamiento propios). La arquitectura pasa de "1 agente + dispatcher de Cal.com" a **"1 flujo por persona + un despachador de flujos"**.
- **Nuevo** `OS-Studio — Agent Voz Emilia` (`Fa2AlIDqUntSWMrw`, 23 nodos): Telegram (voz con Gemini + texto), debounce Redis `studio_os_emilia_<chat_id>`, memoria `studio_os_emilia`, `Tool Agenda Emilia` → su Agenda Sub, tool de Fathom con `source: telegram-voz-emilia`.
- **Nuevo** `OS-Studio — Voz Dispatcher` (`Msh31moofBKBwZId`): extrae el `chat_id` y manda el mensaje al flujo de Sol (`8459099332`) o al de Emilia.
- **Router** (`YWpuV5p0vCDTbIHz`): su nodo `Run Voz Agent` ahora apunta al Voz Dispatcher. **Tu flujo de voz** (`Gpd6NHB4HQdU7ary`) volvió a su forma final: `Tool Agenda` directo a tu Agenda Sub (sin dispatcher ni marcador `[chat:ID]`), allowlist solo tuya y claves Redis `studio_os_test_8459099332` (así `Limpiar Memoria TEST` sigue funcionando). **Archivado** el `OS-Studio — Agenda Dispatcher` intermedio.
- **Pruebas:** el Dispatcher enrutó el chat de Emilia a su flujo (respondió con **su** Cal.com) y el tuyo a tu flujo (**Telegram real entregado**, `message_id 277` desde `@emiliaospi_bot`).
- **Documento nuevo:** `proyectos/STUDIO_OS-Emilia/documentacion/que-le-pedimos-a-emilia-2026-10-21.md` — los 3 datos a pedirle mañana, 7 preguntas de confirmación, guion de prueba en vivo (8 pasos) y qué NO hay que decidir.
- **Lecciones:** (1) el SDK de n8n es la única vía fiel para clonar (el MCP stringifica booleanos y aplana colecciones) pero **agota el tiempo del MCP con payloads de ~16 KB** → hay que recortar; (2) los `subnodes` van **dentro** de `config`; (3) los `id` de las asignaciones de un Set son obligatorios; (4) el SDK tolera un nodo destino de varias ramas; (5) un Code node debe **conservar el item de entrada** (si no, el flujo destino falla con "Key parameter is empty"); (6) un `executeWorkflow` necesita `workflowInputs.schema`, que solo se puede crear por SDK; (7) `restore_workflow_version` puede fallar por purga de historial.

## 2026-10-21 (tarde) — Mes 2 CAD: propuesta de la escala urbana sobre el 2D de Barcelona (CAD → Rhino → ComfyUI)

- **La propuesta:** el sistema de SET_01 (capas, DWT/DWS, LISP, bloques con atributos, cómputos) llevado a la **escala urbana**, sobre el `Barcelona-2D.dwg` del concurso (27,9 MB, en `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\`), encadenado con **Rhino** (MCP ya instalado) y **ComfyUI** (LoRA `rhino-to-image` ya analizado) → **CAD → Rhino → ComfyUI → lámina A1 del Gaudí Nexus** (entrega 16/12).
- **Medición del 2D (ODA File Converter → DXF → ezdxf 1.4.4, DWG intacto):** **96 capas · 162.396 entidades · 46 bloques (38 con nombre) · 1.344 INSERTs · 34.574 TEXT · 43.032 HATCH · 40,4 × 38,7 km de extensión** (X 409.693→450.137 m, Y 4.560.549→4.599.261 m) · `$INSUNITS` 6 (m) con `$MEASUREMENT` 0 (imperial) · 1 layout (`Layout1`) · **0 de las 22 capas del SET_01** → la taxonomía es temática y funcional (catalán, por Districte 1-10: manzanas, parterres, equipamientos, red viaria, metro con 492 inserts), no de dibujo. **120× más denso** que el replanteo. Reporte en `raw/reports/barcelona-2d.audit.md`.
- **`SET_04-URB` (propuesta):** ~26 capas propias (`URB-` base heredada · `PRO-` propuesta · `REF-` fondo no imprimible; la cartografía entra como xref y no se renombra a mano) · `SET_04-URB.dwt` + `SET-URB.dws` reutilizando `scripts/genera-template-set01.py` · 4 LISP derivados de los que ya funcionan: `SET-URB` (crea capas), `RESUMEN-URB` (el cuadro urbano: m², equipamientos, cobertura verde), `VISTAS-URB` (ventanas 1:500 / 1:1000 / 1:5000), `PLAZA-PLACA` (recorte interactivo de la plaza) · 38 bloques heredados renombrados con prefijo + 6 nuevos, con **`PRO-MOBILIARIO`** (atributos MATERIAL/CANT/COSTO) que es a la vez el objeto del **premio especial** del concurso y la pieza que entra al cuadro urbano.
- **Análisis de visualización urbana con ComfyUI:** la escala urbana es un problema de **control de líneas**, no de LoRA → **planos ilustrados con SDXL + ControlNet** (canny/depth/scribble sobre el DXF exportado a PNG; dual canny 0,3 + depth 1,0 ya validado) y **volumetrías y vistas aéreas con FLUX.2 klein 9B + LoRA `rhino-to-image`** (capturar → arcilla monocolor → hiperreal). **FLUX.2 klein no tiene ControlNet nativo** (solo `ReferenceLatent`): el LoRA aporta materialidad y sello propio, nunca fidelidad de trazo. La vista aérea sale de la geometría en Rhino con cámara alta, no de un texto.
- **Documentos:** `proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano.md` (propuesta completa) · **§10 del dashboard AutoCAD** (versión ejecutiva) · §9 del documento de revisión del 22/10.
- **Bug corregido:** `scripts/audita-dwg.py` usaba `doc.blocks.names()`, que ya no existe en ezdxf 1.4.4 → `doc.blocks.block_names()` con fallback. El script no corría desde la actualización de ezdxf.

## 2026-10-21 — Dashboard AutoCAD v2 + playbooks actualizados al entorno LT 2027

- **Dashboard AutoCAD reescrito** (`proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html`): el del 16/10 estaba congelado antes de las sesiones del 20/10. Ahora tiene 12 secciones: entorno LT 2027 · medición v2 de REP-ARAOZ · bloque `SIMB-LOC_ID` · extracción dentro del DWG · estado real de los playbooks · **bloques que faltan crear** · 4 LSP + 4 scripts · pendientes. HTML validado (0 desbalances).
- **Hallazgo de entorno que manda sobre el método:** la instalación viva es **AutoCAD LT 2027** (`C:\Program Files\Autodesk\AutoCAD LT 2027`); el Full 2027 fue desinstalado (instalador en `P:\autocad\AutoCAD.2027_English_64bit`). En LT **no hay COM externo** (el MCP `autocad` del vault queda en pausa), **no existen `DATAEXTRACTION`/`ATTIN`/`ATTOUT`**, y el **vínculo de datos exige Excel instalado** (no está) → la automatización y el cómputo pasan por **AutoLISP** (`APPLOAD` sí existe en LT 2024+ Win) y por LSP que dibuja la tabla dentro del DWG.
- **Vía descartada (21/10):** el LSP de cuadro de locales (`CUADRO-LOCALES`) no era el camino → la planilla de locales vive como CSV en el vault (`docs/planilla-locales.*`) y la fuente en el DWG son los 28 rótulos numerados a mano.
- **Playbooks actualizados:** PB-01 y PB-02 pasan a `vigente-lt-2027` (PB-02 §3 documenta las 4 vías de cómputo reales en LT; PB-01 §2 lista los 4 LSP y §3 el DoD con el ítem 8/9 al día). `wiki/glosario/interno/pbooks/pbk-set01-rep.md` reescrito con las secciones *entorno LT 2027* y *dónde viven los cómputos*. `wiki/glosario/software/autocad.md` gana la sección **AutoCAD LT 2027 — qué cambia**; `wiki/glosario/software/mcp-autocad.md` queda marcado en pausa con la vía sustituta (MCP oficial de Autodesk 2027, `MCPHTTPSTART` → `localhost:5001/mcp`, pendiente de prueba).
- **Documento de revisión para el 22/10:** `proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md` (revisión del trabajo CAD + checklist de revisión del dashboard + 3 puntos a confirmar + bloques pendientes).
- **Sesión:** `raw/sessions/2026-10-21-sesion-dashboard-autocad-v2.md`.

## 2026-10-20 (tarde) → 21/10 — El VPS `pitau.tech` se cayó y volvió: n8n + Leantime + panel EasyPanel

- **Síntoma:** `n8n.pitau.tech` (89.117.73.109) dejó de responder en TCP 443 y 22; lo mismo `panel.pitau.tech` y `pitautech-leantime.3nq4ow.easypanel.host` — **los tres servicios viven en la misma IP del VPS**, así que se cayó el host completo. Desde el estudio internet anda (GitHub 200) → no es la conexión local.
- **Alcance:** el bot de Telegram (n8n) y Leantime quedaron offline. **Sin pérdidas**: las 15 h recién cargadas en Leantime ya estaban confirmadas en la base; los 3 event types de Emilia viven en Cal.com (externo); los documentos del vault están escritos.
- **Última operación antes de la caída:** `move_workflows_to_folder` (mover los 2 workflows nuevos a la carpeta `OS-Emilia / MVP06-Agente_Voz_telegram`) → la llamada cortó con *"socket connection closed unexpectedly"*.
- **No se puede recuperar desde el estudio**: no hay SSH al host y el panel de EasyPanel está en la misma IP caída → el reinicio hay que hacerlo desde el panel del proveedor.
- **21/10: el VPS volvió.** Verificado: los 4 workflows **activos** y con la versión activa = la del borrador (`1c745d12` el Router, `fae63d66` el agente de voz), **movimiento de carpeta completado** (los 2 nuevos están en `OS-Emilia / MVP06-Agente_Voz_telegram`), **cadena de Emilia probada** (agente → Dispatcher → Agenda Sub Emilia → respuesta correcta) y **cadena de Sol sin regresión** (`leer_calendario` sigue trayendo su Google Calendar → la credencial sobrevivió al reinicio). **Leantime volvió con las 15 h** ✓.
- **Aprendizaje:** el `description` de un workflow se actualiza en el sitio (no crea versión nueva) → los pendientes quedaron anotados en la descripción de los 4, visibles en la lista de n8n.
- **Checklist de arranque tras una caída:** (1) ¿n8n responde? (2) ¿los 4 workflows están activos y con `versionId == activeVersionId`? (3) mensaje de prueba al bot — si no responde, desactivar y **volver a publicar** el Router (re-registra el webhook de Telegram); (4) las credenciales OAuth no se ven afectadas si la `encryptionKey` del VPS no cambió.

## 2026-10-20 — LoRA «Rhino-to-Image» (FLUX.2 klein 9B): análisis, research y fichas

- **Analizado** el LoRA del curso AI×Gaudí (`G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\rhino-to-image-lora.basic.safetensors`, 120,8 MB): **FLUX.2 [klein] 9B**, rank 16, F32, 176 tensores, 31,66 M params, sin metadata embebida. Matrices B no nulas (σ ≈ 1,3e-3) → delta entrenado y sano; strength de trabajo 0,6-1,0. Identificación verificada por shapes contra `black-forest-labs/flux2` y `comfy/model_detection.py`.
- **Research `@sherlock`** (54 fuentes verificadas): `raw/research/2026-10-20-flux2-klein-lora-rhino-to-image.md` + `-crudo.md` + cache. Hallazgos: el LoRA es "el modelo de IA exclusivo" del curso; el bloqueo de geometría es **nativo** (`ReferenceLatent` ×2, método `index`), sin ControlNet oficial para klein; el instructor es **Thomas Nelissen** (Cas Esbach, co-autor del módulo 7); 9B no entra en la RX 570 de 8 GB → RunPod 3090 ($0,22/h), $2-5 por el concurso; `--lowvram` no hace nada con DirectML (`model_management.py:121`).
- **Workflow nuevo** `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/` (5 fichas + `workflow_rhino_to_image.json` + `salidas/`). Grafo validado contra el código de ComfyUI local (`b08e6cf3`): `UNETLoader` usa `weight_dtype` (no `weight_name`) y `SamplerCustomAdvanced` usa el esquema nuevo `noise`/`guider`/`sampler`/`sigmas`/`latent_image`.
- **Fichas**: `wiki/glosario/software/lora-rhino-to-image-gaudi.md` (nueva) · `wiki/glosario/software/flux2-klein-9b.md` (nueva) · `wiki/glosario/software/comfyui.md` (2 secciones + catálogo) · `wiki/glosario/software/00-index.md` · `wiki/glosario/interno/pbooks/pbk-comfyui.md` (flujo + troubleshooting).
- **Script**: `scripts/analizar-lora-safetensors.py` + `_notas.md` — auditoría de `.safetensors` sin PyTorch (deduce el modelo base y revisa la salud de los pesos). Probado sobre el LoRA del curso.
- **Riesgo de licencia abierto**: klein 9B es FLUX Non-Commercial y el LoRA es derivative → admisible en concurso; para cliente, klein 4B (Apache 2.0) reentrenando (el portado de LoRA entre 9B y 4B es imposible por arquitectura).
- **Pendiente**: copiar el LoRA a `models/loras/`, descargar el stack FLUX.2 en el pod, exportar las 3 capturas desde Rhino, y pedir a Emilia/instructor el trigger word, el modelo base exacto, la variante `.advanced` y el workflow JSON del módulo 3.
- **Dashboard del concurso**: `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html` (el del cierre de Mes 1 del 16/10) pasó de 4 a 5 tabs con el **tab 4 · Concurso**: motor FLUX.2 klein 9B + LoRA del curso, stack a descargar (18,3 GB), flujo WF-rhino-to-image, cómo se entrenó el LoRA, riesgo de licencia (Non-Commercial vs Apache 2.0), plan en 3 etapas ($0 / ~$1 / $2-5) y entrega 16/12. Además: filas nuevas en la tabla de modelos, tarjeta "Ingeniería inversa" actualizada y el tab Mes 2 con el pipeline del concurso.
- **Extracción del material del curso** (Miro + Archademy, ambos login-gated — verificado): scripts nuevos `scripts/miro_board_inventory.py` y `scripts/archademy_curso_inventory.py` (+ notas), probados con archivos de laboratorio. Inventarían videos (con id de YouTube listo para `scripts/transcribir_youtube.py`), workflows de ComfyUI, tableros y PDFs. Guía del circuito completo en `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md`.
- **Formato de export de Miro corregido**: hoy el backup es `.rtb` (solo owner/co-owner) y el export para participantes es **CSV** — el script ya parsea CSV, backup (ZIP y binario) y PDF. **Los videos del curso traen subtítulos** ("siete módulos en inglés con subtítulos"), así que la transcripción va por `scripts/transcribir_youtube.py` sin descargar video. Datos del concurso verificados: entrega **16/12/2026 23:59 GMT-7**, lámina A1 ≤15 MB JPEG (+A4 opcional), premios 6.000/2.000/1.000 USD + Premio de Diseño de la Fundació 1.000.
- **Tablero del curso recibido y procesado** (`AI-course.csv`, 219 filas → 72 secciones): es el índice de recursos y prompts del curso, no un tablero de workflows. Hallazgos: (a) existe la **variante `.premium`** del LoRA (`rhino-to-image-lora-premium.safetensors`, descarga vía `thomasnelissen.ai`); (b) **no hay trigger word**: la activación es un **prompt JSON estructurado** con *STRICT CAMERA LOCK*; (c) el curso compara con **LoRA al 50 % y al 100 %**; (d) el pipeline real tiene **3 pasos** (captura en color → **pase de arcilla** con la lógica constructiva de Gaudí → pase hiperreal con LoRA). Extraídos al vault los dos INSTRUCTION.md (módulo 3 y módulo 7) y el esqueleto JSON.
- **Método de guardado del HTML simplificado**: `Ctrl+A` → `Ctrl+C` → pegar en Bloc de notas → guardar como `curso.txt` (UTF-8). El script acepta texto plano.
- **Página del curso es dinámica** (WooCommerce: `/my-account/my-competitions/214/` = pedido nº 214, la pestaña `course` se arma por sesión vía XHR) → `Ctrl+S` no sirve. Se agrego al script el **modo JSON** (recorre en profundidad la respuesta de un XHR o la salida del colector de consola) y a la guía el **colector de consola** de una línea, que copia al portapapeles todos los iframes/videos/links de la página.
- **El LoRA premium todavía no está en** `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\` (solo `basic`, `AI-course.csv` y los 2 DWG): falta confirmar dónde quedó.
- **Transcripciones del curso listas**: el HTML guardado de `G:\Mi unidad\OS-Emilia\AIxGaudi\My account - Archademy.ai.html` resultó suficiente — los videos están embebidos con **Mux** y cada módulo expone sus subtítulos `.vtt` (EN y ES) en el CDN de Bunny/Mux **sin token** (200 directo). Nuevo script `scripts/mux_lecciones_curso.py` (+ notas): baja los subtítulos y los escribe en `raw/yt/transcripts/` con la convención del vault (md + srt + txt). Resultado: **6 de 7 módulos transcritos** (Introduction 1268 cues · Text-to-Image 659 · Image-to-Image 1047 · Image-to-Video 333 · Image-to-3D 249 · Gaudí Workflow 454); el *Round Table* no tiene subtítulos (404). Bonus: la página trae la **contraseña del tablero Miro** (`Gaudi2026`).
- **Decisión de infraestructura documentada** (`wiki/glosario/software/comfy-cloud-vs-runpod.md`): **Comfy Cloud Standard ($20) no alcanza para el concurso** — no deja importar modelos propios (solo Creator $35+) y el upload directo de archivos grandes no existe todavía; **en Comfy Cloud no se entrena** en ningún plan (no hay nodos de entrenamiento en la lista aprobada). Verificado contra la documentación oficial (precios, retención, Partner Nodes, telemetría de Desktop) y RunPod (precios, borrado del disco al terminar el pod). Veredicto: **híbrido** — local 8 GB para iterar, Comfy Cloud **Free** (400 cr = ~25 min de GPU) para probar los workflows oficiales, **RunPod 3090 $0,22/h** para producción 9B y entrenamiento → **$1-2 por mes**.
- **Dashboard de ComfyUI ampliado a 6 tabs** (galería intacta y mandando): tab 4 · Concurso, tab 5 · Mes 2 (el cuadro dónde renderizar, las 5 pruebas del mes, la pregunta de fondo y las decisiones) y tab 6 · **Método** (las 5 capas hacia un asistente que ejecuta, la impronta del estudio y Hermes vs OpenClaw).
- **Recolector de renders** (`scripts/indice-renders-comfy.py` + notas): lee la metadata que ComfyUI graba dentro de cada PNG (bloques `tEXt` `prompt` y `workflow`) y arma `INDICE-RENDERS.md/.json` con modelo, LoRA y strength, seed, sampler, steps, cfg, resolución y prompt. **80 renders, 100% con metadata.** Sin base de datos: la trazabilidad vive en la imagen.
- **Diseño de la evolución a asistente** (`proyectos/MVP_04-comfyui-arquitectura/evolucion-asistente-estudio.md`): 5 capas (ejecución local + MCP · contrato JSON · índice · interfaz Gradio · agente), el paralelo con el tablero del curso, la impronta como tres artefactos (schema + LoRA propio + índice) y hoja de ruta en 5 etapas con criterio de cierre.

## 2026-10-20 — Horas trabajadas registradas en Leantime (15 h) + cliente de time tracking

- **Registrado en Leantime**: 4 h del lunes 19/10 + 4 h del martes 20/10 repartidas en **cad, fuentes, rhino y n8n-leantime-fathom-agentes** (1 h por área por día + 1 h extra de reparto el lunes → **3 h por tema**), más la reunión de **3 h** del miércoles 21/10 con Emilia. Total **15 h**, `kind: GENERAL`, en las tarjetas `452` (cad), `517` (fuentes), `571` (rhino, p6), `448` y `504` (agentes), `533` (reunión).
- **Descubierto el time tracking de Leantime**: el servicio no se llama `TimeTracking` sino **`Timesheets`** → `leantime.rpc.Timesheets.Timesheets.logTime(ticketId, {dateString,hours,kind,description})`, con rollback en `deleteTime(id)` y lectura en `getAll`.
- **Dos trampas medidas**: (1) la **fecha se desplaza 7 h por RPC** (la instancia está en UTC+7 y el RPC no convierte como la UI) → para que una entrada se lea `19:00:00` hay que mandar `12:00:00`; (2) `logTime` **suma** en vez de crear: mismo ticket+fecha+tipo → incrementa la fila y concatena las descripciones con `--`.
- **Primer intento con fechas corridas (+7 h)**: 9 entradas borradas con `deleteTime` y recargadas con las fechas correctas (ids 51-63). Verificado por relectura: 8 h el lunes, 4 h el martes, 3 h el miércoles.
- **Pendiente de rotular**: las 4 h extra del lunes quedaron como "Extra lunes 19/10 - 1 h por tema" porque el rótulo original ("mtb") no se pudo identificar (ni está en el vault ni en Leantime, y Sol tampoco lo reconoce). Se renombra en la UI cuando se sepa qué era.
- **Archivos**: `scripts/leantime_registrar_horas.py` + `_notas.md` (nuevos, con `--dry` / `--verificar` / `--borrar`), `raw/sessions/2026-10-20-sesion-registro-horas-leantime.md` (nuevo), `wiki/glosario/software/leantime.md` (sección "Horas — time tracking" + tabla de métodos), `log.md`.

## 2026-10-20 — Cal.com de Emilia configurada + bot de agenda armado (4 workflows, probado end-to-end)

- **Cal.com de Emilia** (operado desde n8n; la API responde **403 Cloudflare 1010** desde la PC): creados los event types **7563141** presencial, **7563142** online (Meet) y **7563143** libre (oculto), más el schedule "Disponibilidad 24/7" **2527411**. `GET /v2/slots` verificado: 8 slots/día (09-16) en ET-A y ET-B.
- **Hallazgo que cancela el paso más frágil del plan:** el Google Calendar de Emilia **ya estaba conectado** en Cal.com (`arq.emiliapimentalombardi@gmail.com`, `credentialId 2605522`) y es el destination calendar → las reservas ya caen en su calendario y Cal.com ya le resta los ocupados. **No hay OAuth que hacer mañana.**
- **n8n:** nuevo `OS-Studio — Agenda Sub Emilia` (`2JogeOoT3Wjq2ncH`, agente con las 7 tools sobre sus event types) y nuevo `OS-Studio — Agenda Dispatcher` (`CVvxZgn0AipO6dV0`, enruta por `chat_id`); parcheados `Agent Voz TEST` (`Gpd6NHB4HQdU7ary`: allowlist por `String()`, Redis por chat, respuesta al chat de origen, Tool Agenda → Dispatcher) y `Telegram Router` (`YWpuV5p0vCDTbIHz`: la regla 2 del switch pasa de `/help` a identidad de Emilia). **Publicados** (los subflujos de Execute Workflow exigen estar publicados).
- **Arquitectura:** 1 flujo de voz compartido + 1 Dispatcher, en vez de 2 clones de voz + 2 de agenda. Evita el swap del webhook de Telegram (1 por bot) y el riesgo de cortar el bot de Sol; **el aislamiento se mantiene** porque la credencial de Cal.com vive dentro de cada subflujo de agenda.
- **Pruebas:** el agente llamó `obtener_reuniones` con los 3 ET IDs correctos; el Dispatcher enrutó a `Run Agenda Emilia`; el flujo de voz completo respondió bien para Emilia y **sin regresión para Sol** (respondió con su agenda real).
- **Pendiente 21/10:** `chat_id` real de Emilia (2 reemplazos: Router `rightValue` + `permitidos` en el `jsCode`), dirección del estudio en ET 7563141, y compartir su calendario con `proyectopi.31416@gmail.com`. Opcional en la UI de Cal.com: duraciones 120/180 y el schedule 24/7 del ET libre.
- **Lecciones (para wiki, pendiente de `s`):** (1) `/v2/event-types` de Cal.com solo existe con `cal-api-version: 2024-06-11` y su body usa `length`; (2) la API responde `success` pero **no aplica** `metadata.multipleDuration` ni `scheduleId`; (3) el MCP de n8n **stringifica** los parámetros (`addNode`/`updateNodeParameters`) y con `sendBody: "true"` el body no viaja → usar `create_workflow_from_code` (SDK) o `setNodeParameter` sobre hojas de string; (4) editar un workflow no cambia lo que se ejecuta: hay que **publicar**; (5) el `pinData` del MCP stringifica → allowlists con `String(...)`.
- **Archivos:** `proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21.md`, `raw/sessions/2026-10-20-sesion-agenda-emilia-cal-com-n8n.md`.

## 2026-10-19 — Carga a Leantime de los 2 planes del 16/10 (33 cards + 85 subtasks)

- **Hallazgo:** el MCP de Leantime (`/mcp`) responde `initialize` pero **`tools/list` devuelve `tools: []`** — el plugin MCP Server no publica ninguna tool aunque `opencode mcp list` lo muestre conectado. La vía que funciona es la **API JSON-RPC** `POST /api/jsonrpc` (`leantime.rpc.*`), la misma del 13/10.
- **Cargado:** proyecto 4 `O.S_ARQ-Emi` → sprint 27 `S1 Agentes + agenda Emilia (19/10-23/10)`, milestones 461-464 (M-A1..M-A4), **20 cards + 52 subtasks**, 45,52 h · proyecto 6 **nuevo** `Proyecto Pi - Concurso Gaudi Nexus` → sprint 28, milestones 537-542 (M-B1..M-B6, entrega 16/12), **13 cards + 33 subtasks**, 29,59 h. Miembros: Emilia + Pitau Tech en ambos. 0 cards sin subtasks, 0 subtasks huérfanos.
- **Nuevo:** `scripts/leantime_rpc.py` (+ `_notas.md`) · `scripts/carga_leantime_planes_261019.py` (+ `_notas.md`) · estado final en `raw/reuniones/leantime-carga-261019-estado.json`.
- **Aprendizajes API (documentados en `wiki/glosario/software/leantime`):** el id creado vuelve como array `[458]` · `updateTicket` exige `values.id` y siempre `type` + `projectId` · los subtasks se crean con `addTicket` + `type: 'subtask'` + `dependingTicketId` (`upsertSubtask` no anda por RPC) · `quickAddMilestone` nace sin sprint y se linkea después · la membresía se carga con `Projects.editUserProjectRelations` (lista completa, reemplaza) · 429 por minuto → 1,6 s entre llamadas · **Goals no expuestos**: se crean a mano en la UI.
- **Sesión:** `raw/sessions/2026-10-19-sesion-guion-agente-agenda-emilia.md`.

## 2026-10-19 — Guion del miércoles: agente de agenda de Emilia (Cal.com + Calendar)

- **Nuevo:** `proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia.md` — documento operativo de la cita presencial del mié 21/10 13:00: arquitectura objetivo (agente + subagente-subflujo, clon del perfil de Sol), **3 claves a pedirle a Emilia** (API key de Cal.com v2, autorización OAuth de Google Calendar, definición de sus calendarios + evento de 60 min con Meet), tabla de **cambios nodo a nodo** en los 3 workflows (7 tools de agenda + 26 del agente + 1 rama del Router), guion de 8 bloques (2 h), 10 pruebas de aceptación, riesgos y rollback en 1 minuto.
- **Decisiones de Sol:** concurso **ya inscripto** (Sol + Emilia) con **entrega 16/12/2026** · carril del concurso en **proyecto Leantime propio** `Proyecto Pi — Concurso Gaudí Nexus`, separado del contrato Studio OS × Emilia · foco de la semana en dejar configurado el agente de agenda de Emilia.
- **Actualizado:** `specs/261019-plan-concurso-gaudi-nexus-ia.md` (M-B1 cerrado, M-B6 = 16/12, tablero y preguntas 1/2/3/5 resueltas) · `specs/261019-plan-agentes-telegram-agenda-emilia.md` (nueva task C1b "clonar agente + subflujo con perfil Emilia" = 5 pom, D2 pasa a 3 pom, 20 cards, M-A2 y preguntas 3/7 con guion).
- **Base técnica verificada por MCP n8n** (workflows, 26+12+17 nodos, 28 credenciales con sus IDs): `OS-Studio — Agent Voz TEST` `Gpd6NHB4HQdU7ary` · `OS-Studio — Agenda Sub TEST` `ygdjqRfXpxKMFWEN` · `OS-Emilia — Telegram Router` `YWpuV5p0vCDTbIHz` · credencial Emilia Cal.com `ppi-EmiliaOS_Cal.com` (`3MvZXPNH8LrDYPZS`) ya existente.
- **Sesión:** `raw/sessions/2026-10-19-sesion-guion-agente-agenda-emilia.md`.

## 2026-10-19 — @fathom-pm: tareas de las 2 últimas reuniones del 16/10 (agentes Telegram + concurso Gaudí Nexus)

- **Analizado:** reunión 20:33 "OS Emilia: agentes de Telegram + ComfyUI" (720 turnos) y reunión 19:31 "Concurso Gaudí Nexus" (592 turnos), importadas el 19/10 desde la cuenta Fathom Proyecto Pi (ver entrada de import abajo). `action_items` viene vacío en ambas: las tareas se derivaron del `## Resumen` (Próximos pasos) y de la `## Transcripcion` completa, cada una con su timestamp de origen.
- **Creado:** `specs/261019-plan-agentes-telegram-agenda-emilia.md` (19 tareas · M-A1…M-A4 · 19 cards Leantime en el proyecto 4) + `specs/261019-plan-concurso-gaudi-nexus-ia.md` (13 tareas · M-B1…M-B6 · 13 cards, tablero propio del estudio).
- **Carga pomodoro:** subtasks ≤25 min, tope 16/día por persona (Emilia 42 pom · Sol 56 pom en la semana 19→25/10), WIP ≤2, cada task cita milestone + OKR o `sin-alineacion`.
- **Leantime:** plan de carga listo (sprint `S1` + milestones + cards con `planHours` 0,42 h por pomodoro); **a la espera del "s" de Sol** — no se ejecutó ninguna carga.
- **Dashboard:** 23 → 26 reuniones transcriptas + links a los 2 specs nuevos en `proyectos/STUDIO_OS-Emilia/presentacion/06-dashboard-cierre-mes1.md`.
- **Sesión:** `raw/sessions/2026-10-19-sesion-fathom-pm-tareas-emilia-16oct.md`.
- **AFECTA:** `specs/261019-plan-agentes-telegram-agenda-emilia.md`, `specs/261019-plan-concurso-gaudi-nexus-ia.md`, `proyectos/STUDIO_OS-Emilia/presentacion/06-dashboard-cierre-mes1.md`, `raw/sessions/2026-10-19-sesion-fathom-pm-tareas-emilia-16oct.md`, `log.md`.

## 2026-10-19 — 3 reuniones con Emilia (16/10) importadas de Fathom Proyecto Pi

- **API:** `api.fathom.ai/external/v1/meetings` con `FATHOM_API_KEY_PROYECTOPI`, `created_after=2026-10-09` → 8 reuniones; filtro por hablante deja 3 con Emilia Pimenta Lombardi (16/10) y descarta 2 de Delfina (19/10).
- **Import:** `scripts/import_fathom_ppi_manual.py` sobre JSON filtrado → `raw/reuniones/2026-10-16_emilia-proyectopi_193621124.md` (529 turnos), `_193639289.md` (592), `_193660891.md` (720) + copia Drive `Reuniones-Internas` + 3 claves en `.import-state.json`.
- **Contenido:** obra/iluminación+flujo CAD (18:34), concurso "Gaudí Nexus" + tokenización de diseños (19:31), agentes OS/Telegram + ComfyUI con LoRA propio (20:33).
- **Dual de cuentas:** 2 de las 3 ya existían en Drive desde el n8n Core con `recording_id` propio (193639372, 193661028); la de 18:34 faltaba. Queda pendiente criterio de dedup entre cuentas.
- **Sesión:** `raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct.md`.
- **AFECTA:** `raw/reuniones/2026-10-16_emilia-proyectopi_*.md`, `raw/reuniones/.import-state.json`, Drive `Reuniones-Internas`, `raw/sessions/2026-10-19-sesion-import-fathom-emilia-16oct.md`, `log.md`.

## 2026-10-16 — Dashboard Vault fuentes→wiki (cierra serie Mes 1)

- **Nuevo:** `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-vault.html` estilo propuesta-embebido en modo oscuro (6 tabs: Flujo / Agentes / Carpetas / Mes 1 / Mes 2 auto / Demo). Gráfico captura→sherlock→contenidos→gate-s→vaultworm→wiki, tabla tareas+carpetas `raw/`→`wiki/fuentes/`, agente Telegram en grupo Fuentes (“Anotado ✓”→Sheet) + propuesta Mes 2: link→Sheet→worker 07:30→raw→solo recibir para leer.
- **Linkeado:** `dashboard-mes1-emilia.html` (toplinks + card Vault ya con dashboard propio) + `dashboard-estudio-os.html` (→ Vault).
- **Sesión:** `raw/sessions/2026-10-16-sesion-dashboard-vault-fuentes.md`.
- **AFECTA:** `presentacion/dashboard-vault.html`, `dashboard-mes1-emilia.html`, `dashboard-estudio-os.html`, `log.md`.

## 2026-10-16 — 3 Google Docs listos + cron dual diseñado

- **Backfill:** WF `ChXP1UpOM8U9ImSJ` (SDK clon cadena Docs, exec 3782 6/6) → 3 Docs con formato en Internas, 9 parciales limpiados, WF archivado. Dashboard a 23 reuniones.
- **Cron dual (§9 arquitectura):** un cron, rama PPI (Fetch + Split clonados) hacia Build intacto; pre-requisito UI: credencial `ppi-PPI_Fathom` Header X-Api-Key; dedup fecha/título fase 2.
- **Sesión:** `raw/sessions/2026-10-16-sesion-gdoc-backfill-cron-dual.md`.
- **AFECTA:** Drive Internas (3 Docs), `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md`, `06-dashboard-cierre-mes1.md`, `scripts/gen_backfill_gdoc_09oct.py`, `log.md`.

## 2026-10-16 — Rescate 3 reuniones 09/10 Fathom Proyecto Pi

- **Hallazgo:** Drive llegaba al 26-9; en tu Fathom Pi había 3 reuniones con Emilia del 09/10
  (Emi OS 16:15 + conocimiento 17:47 + automatización/Comfy 18:48, ~1h c/u, 557-801 turnos).
- **Import manual:** `2026-10-09_emilia-proyectopi_191472132/191509492/191524949.md`
  en `raw/reuniones/` + Drive Internas + state, formato Core. Script reutilizable
  `scripts/import_fathom_ppi_manual.py` (+ `_notas.md`).
- **Contenido clave Mes 1:** Emi OS + DWF iPad + baño PB · vault/agentes/Leantime + cita 14/10 ·
  agente IA /agendar + LoRA firma + collage + RAM.
- **Queda:** Google Doc ×3, tasks a Leantime (fathom-pm), dashboard a 23 reuniones, Fathom Pi al Core.
- **Sesión:** `raw/sessions/2026-10-16-sesion-rescate-fathom-09oct.md`.
- **AFECTA:** `raw/reuniones/` (3 nuevos + state), Drive Internas (3 copias), `scripts/import_fathom_ppi_manual.py`, `log.md`.

## 2026-10-16 — Mes 1 listo para presentar (81hs + 13.5hs/mes)

- **Dashboard:** 81hs (65+16) · 63 sesiones · 20+1 reuniones · SET_01 objeto real · tabla ahorro 13.5hs/mes · capacidad 0.22 · payback mes 7.
- **Cierre:** C1-C3 tildados 16/10. **Trimestral §4:** nota Nayara→replanteo. **Fathom Sol:** patrón Emilia dado por hecho.
- **Sesión:** `raw/sessions/2026-10-16-sesion-mes1-presentacion-emilia.md`.
- **AFECTA:** `proyectos/STUDIO_OS-Emilia/presentacion/06-dashboard-cierre-mes1.md`, `specs/261013-plan-cierre-mes1-calculadora-emilia.md`, `specs/260910-plan-trimestral-unificado-studio-os-emilia.md`, `log.md`.

## 2026-10-16 — Auditoría 24 specs: reducción a 8 vivos + mapa

- **Vivos (8 en `specs/`):** trimestral 260910, n8n 260924, ingesta 261009, inbox 261013 (§10-11), worker 261016, cierre 261013, backlog Mes 2 261013, unificado 261016.
- **Archivados (16 en `specs/archived/` con `git mv`):** telegram-vault, ghl x2, vault_cerebro, fathom-specs, esquema-60hs, github-actions, moodboard, plan-accion-web, threads, nextcloud, alta-leantime, vista-yt, voz-telegram, reporte-horas, inventario. Mapa en `specs/archived/README.md`.
- **Completo:** Router 17 nodos, Agenda/Cancel/Modif real, Fathom Core 07:00, Sheet header, Leantime Emilia, calculadora, reporte evidencia, Thread 1 Sherlock.
- **Lo ve Sol:** QW1-QW8 (grupo+chat_id, share GPT, rama IDEA, horas Leantime + factura 600, evento Meet, worker dispatch, presencial Codex, dedup) + probar ffmpeg e2e + grafo YT + croquis 60X.
- **Sesión:** `raw/sessions/2026-10-16-sesion-auditoria-reduccion-specs.md`.
- **AFECTA:** `specs/archived/` (16 movidos + README), `specs/261016-plan-unificado-studio-os-quickwins.md`, `log.md`.

## 2026-10-16 — Unificación 23 specs hacia 4 vivos + 8 quick wins

- **Análisis:** worker nube (Actions) + Router n8n 17 nodos conviven: captura instantánea en VPS, enriquecimiento programado en nube, PC apagada incluida.
- **Editado:** `specs/261013-plan-fuentes-emilia-inbox.md` §10 rama IDEA + PDF-link (sin URL entra como IDEA, PDF va a worker) + §11 Plus no-técnica (celu + presencial Codex Sign in Plus + 1 share prueba).
- **Creado:** `specs/261016-plan-unificado-studio-os-quickwins.md` (4 vivos A-D, hoja manual vs sistema vs capacidad nueva, QW1-QW8, Mes 2 S1-S4, 7 MCPs).
- **Sesión:** `raw/sessions/2026-10-16-sesion-unificacion-planes-quickwins.md`.
- **AFECTA:** `specs/261013-plan-fuentes-emilia-inbox.md`, `specs/261016-plan-unificado-studio-os-quickwins.md`, `log.md`.

## 2026-10-09 — s #2 cumplido: @contenidos fichó video 1 (formato spec v3 §13)

- **Regenerado:** `raw/contenidos/2026-10-09-comfyui-for-architects-architutors.md` (177 líneas: resumen 5 bullets + ficha colegio + índice verbatim con timestamps + glosario 19 términos + gate). Estado `fichado`, nada en `wiki/`.
- **Hallazgo:** img2img SketchUp→render con Flux1 + Flux Kontext Image Scale + KSampler + DualCLIP; 2000px; prompts scandi/industrial/tropical. Destino propuesto: `wiki/estudio/comfyui-flux-kontext-img2img` + fuente curada + glosario comfyui vía @vaultworm-arq.
- **Pendiente:** s #3 (@vaultworm-arq conecta + galería local).
- **AFECTA:** `raw/contenidos/2026-10-09-comfyui-for-architects-architutors.md`, `log.md`.

## 2026-10-09 — Transcripts con prefijo fecha ISO (opción A, sin subcarpetas)

- **Cambio:** salidas `YYYY-MM-DD_<id>.*` (orden cronológico nativo por texto) + caché tolerante con/sin prefijo. Renombrados los 4 del video 1, idempotencia verificada (re-corrida = cache hit, sin re-descarga).
- **AFECTA:** `scripts/transcribir_youtube.py`, `scripts/transcribir_youtube_notas.md`, `scripts/00-index.md`, `raw/yt/transcripts/`, `log.md`.

## 2026-10-09 — Gráfico v4: banda FUENTES + fuentes propuestas

- **Agregado:** banda superior con 10 tipos (web, YT, IG, PDF texto, audio, scan, fotos obra, libros, Pinterest, ArchDaily) + nota de propuestos (newsletters, TikTok, X, catálogos fabricantes). Técnica: export escena + offset +290 + import, con un traspié (regex sin `_`, canvas restaurado del .excalidraw.md, re-aplicado 51/51 verificado en PNG).
- **Espejos:** `.mmd` v4 + spec §3.4 (4 filas nuevas).
- **AFECTA:** `diagramas/agentes-fuentes.*`, `specs/261009-spec-ingesta-fuentes.md`, `log.md`.

## 2026-10-09 — Flujo v3 adelgazado: Sherlock slim + stub + Vaultworm semanal

- **Modelo:** Sherlock SOLO exterior (transcript por fuente + stub `pendiente-formato`, o reporte links; sin wiki, no formatea) → Contenidos FORMATEA (template+desarrolla, único acceso wiki/fuentes, OK→mueve+borra) → Vaultworm 1/semana (barre fuentes, alimenta glosario/estudio) → Vistas (Obsidian+web+VR).
- **Grabado en:** descripciones + reglas de `.opencode/agents/{sherlock,contenidos,vaultworm-arq}.md`, spec ingesta v5 §12, `diagramas/agentes-fuentes.*` v3 (verificado legible).
- **AFECTA:** `.opencode/agents/*.md` (3), `specs/261009-spec-ingesta-fuentes.md`, `diagramas/agentes-fuentes.*`, `log.md`.

## 2026-10-09 — Gráfico para Emilia: qué hace cada agente (Excalidraw)

- **Archivos:** `diagramas/agentes-fuentes.excalidraw.md` (editable en Obsidian) + `diagramas/agentes-fuentes.png` (1017×1405, verificado legible) + `diagramas/agentes-fuentes.mmd` (fuente). 4 bandas (Sherlock→gates SOL→Contenidos→Vaultworm→Vistas), construido a mano por coordenadas (el conversor mermaid solapaba títulos).
- **AFECTA:** `diagramas/agentes-fuentes.*`, `log.md`.

## 2026-10-09 — Fix tag tachado: workflow:img2img → workflow-img2img

- **Causa:** `:` inválido en tags Obsidian (no indexa, se ve roto). Era formato propuesto en el piloto — corregido a guion + regla de higiene grabada en spec §8.
- **AFECTA:** `wiki/fuentes/comfyui-for_architects-architutors.md`, `specs/261009-spec-ingesta-fuentes.md`, `log.md`.

## 2026-10-09 — Convención nombres wiki/fuentes + renombre (tema primero, _ intra / - inter)

- **Convención:** `{tema_ppal}-{tema_secundario}-{canal}`, `_` entre palabras del segmento, `-` entre segmentos, software = tema cuando aplica, colisión → fecha al final. Grabada en spec ingesta §8 + regla @contenidos.
- **Renombre:** `comfyui-for-architects-architutors.md` → `comfyui-for_architects-architutors.md` + index-state + hub regenerado (5 links ✅ verificados).
- **AFECTA:** `wiki/fuentes/comfyui-for_architects-architutors.md`, `wiki/fuentes/00-index-yt.md`, `raw/yt/index-state.json`, `specs/261009-spec-ingesta-fuentes.md`, `.opencode/agents/contenidos.md`, `log.md`.

## 2026-10-09 — OK video 1: ficha movida a wiki/fuentes (protocolo mover-borrar estrenado)

- **Modelo fijado:** raw/contenidos = solo pendientes (se vacía al aprobar) · raw/transcripts invisible al humano · @contenidos solo escribe wiki/fuentes · hub renombrado a `wiki/fuentes/00-index-yt.md` (aparece primero) · regla grabada en `.opencode/agents/contenidos.md` + spec ingesta v4 + `yt_build_index.py` (estado apunta a ruta wiki).
- **Movida:** `wiki/fuentes/comfyui-for-architects-architutors.md` (102 líneas, tipo fuente, estado en-wiki, ↩ crudo) · stub de raw borrado físicamente · hub regenerado (71 videos, fila 30 ✅ con link).
- **Pendiente:** s #3 (@vaultworm-arq conecta a glosario/estudio + galería local).
- **AFECTA:** `wiki/fuentes/comfyui-for-architects-architutors.md`, `wiki/fuentes/00-index-yt.md`, `raw/yt/index-state.json`, `.opencode/agents/contenidos.md`, `scripts/yt_build_index.py`, `specs/261009-spec-ingesta-fuentes.md`, `specs/261009-spec-vista-grafica-yt.md`, `scripts/00-index.md`, `log.md`.

## 2026-10-09 — Fix visibilidad Obsidian: .md envoltorio por transcript

- **Cambio:** `transcribir_youtube.py` ahora genera 4 archivos por video (`.md` visible con frontmatter + `.srt` + `.txt` + `.origen.json`). Regenerado video 1, verificado limpio en Obsidian.
- **AFECTA:** `scripts/transcribir_youtube.py`, `scripts/transcribir_youtube_notas.md`, `scripts/00-index.md`, `raw/yt/transcripts/`, `log.md`.

## 2026-10-09 — Paso 1 ejemplo completo: script + transcript video 1 (s #1 cumplido)

- **Nuevos:** `scripts/transcribir_youtube.py` + `scripts/transcribir_youtube_notas.md` (subs manuales→auto primero, fallback Whisper local, limpieza NBSP/apóstrofes, `.origen.json` trazabilidad). Bugs del día: regex `0-0`, línea muerta, encoding latin-1.
- **Transcript:** `raw/yt/transcripts/RAMs89SS6cM.en.srt+.txt` (44 líneas, manual-sub EN, limpio; testigo `voilà` intacto). Sin Whisper: la vía liviana alcanzó.
- **Pendiente:** s #2 (@contenidos ficha formato spec v3 §13) → s #3 (@vaultworm-arq conecta + galería local).
- **AFECTA:** `scripts/transcribir_youtube.py`, `scripts/transcribir_youtube_notas.md`, `scripts/00-index.md`, `raw/yt/transcripts/`, `log.md`.

## 2026-10-09 — Spec ingesta v3: handoff con gate + ficha colegio + canvas imágenes

- **Ampliado:** `specs/261009-spec-ingesta-fuentes.md` v3 — §12 protocolo Sherlock→gate SOL→Contenidos→backlog→Vaultworm por lote (mermaid), §13 ficha bibliográfica estilo colegio (autor/tipo/fecha/índice verbatim/glosario), §14 canvas de imágenes (visión app propia + paso 1 página MkDocs + arranque con ejemplo de ~5 fichas).
- **AFECTA:** `specs/261009-spec-ingesta-fuentes.md`, `log.md`.

## 2026-10-09 — Spec ingesta v2: diagrama + agentes + ficha biblioteca + image-first

- **Ampliado:** `specs/261009-spec-ingesta-fuentes.md` v2 — diagrama mermaid del flujo con 3 agentes, tabla de límites @sherlock/@contenidos/@vaultworm-arq, formato único de ficha de biblioteca, principio image-first (la imagen como puerta de entrada al referente), trazabilidad wiki↩crudo obligatoria, ejemplo trabajado revista+YT+IG.
- **AFECTA:** `specs/261009-spec-ingesta-fuentes.md`, `log.md`.

## 2026-10-09 — Specs ingesta de fuentes + vista gráfica YT (2 agentes en paralelo)

- **Nuevos:** `specs/261009-spec-ingesta-fuentes.md` (ecuación única: revistas PDF scan texto+imágenes por epígrafe, YT API+Takeout, IG en 3 opciones, bowls Sol/Emilia + merge compartido) y `specs/261009-spec-vista-grafica-yt.md` (notas atómicas video/tag/creador → grafo Obsidian emerge; piloto 71 comfyui; filtros 4K/creador/puentes; Fase 2 visor 2D→3D declarada).
- **Pendiente:** `s` de Sol para disparar Agente 1 (ingesta) + Agente 2 (vista-grafo) en paralelo.
- **AFECTA:** `specs/261009-spec-ingesta-fuentes.md`, `specs/261009-spec-vista-grafica-yt.md`, `log.md`.

## 2026-10-09 — `/cancel` con botones + `/modif` con lista numerada (verificados en producción)

- **`/cancel`:** sin Ref lista próximas con botón inline (`cancel:<uid>`) por reunión; el tap vuelve al Router como callback y se sintetiza `/cancel <uid>`. Directo con Ref intacto. Verificado: cancelación real dede el botón.
- **`/modif`:** `/modif` lista numerada; `/modif N DD/MM HH:MM`; `/modif N HH:MM` (mismo día de esa reunión); `/modif Ref DD/MM HH:MM`. Pick por índice + Compute Start. Verificado: `/modif 1 15:00` movió 16:00→15:00 (nuevo Ref, anterior dado de baja por Cal.com).
- **Lección 2:** `leftValue` sin prefijo `=` compara el texto crudo → siempre fallback. Estandarizado al patrón con `=` en los 6 Switch nuevos.
- **Playbook Emilia** actualizado (§2b + comandos). Limpieza pendiente: cancelar la reunión de prueba movida (Ref nuevo en el mensaje de confirmación).
- **AFECTA:** n8n Cancel `B7gGFGcD89vKfc5k` + Modif `c08s62Lo9EmAEJJf` + Router (callback), doc v1.2 (§0, fix 10–12), playbook v1.0 (§2b, §3), `log.md`.

## 2026-10-08 (10) — Manual para Emilia: `playbook-os-emilia-n8n.md` v1.0

- **Nuevo:** guía sin tecnicismos de los dos flujos (Reuniones automático 07:00 + `/sync`; Agenda con `/agendar` + hoja `clientes-contactos`), comandos del bot, mapa de Drive y FAQ. Lista para presentar el 09/10. Referencia técnica: `arquitectura-n8n-os-emilia.md`.
- **AFECTA:** `proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n.md`, `log.md`.

## 2026-10-08 (9) — Agenda Core real sin mock: reserva por Telegram verificada (exec 3525)

- **Flujo:** `/agendar DD/MM HH:MM Nombre [emails]` → parseo real (año implícito, AR→UTC, validaciones) → email en mensaje o lookup en `clientes-contactos`/`clientes` (match normalizado, solo activos) → Cal.com evento 7109200 (30 min, `America/Argentina/Buenos_Aires`) → confirmación Telegram con Ref. Cal.com avisa al invitado por email solo.
- **Hallazgo:** IFs creados por API no evalúan (rama 0 siempre, test y producción); migrados los 4 a Switch v3.4 como el Router. Canvas reordenado (fila principal + rama Sheets abajo).
- **Verificación:** `/agendar 09/10 15:00 Sol` → hoja resolvió `proyectopi.31416@gmail.com` → reserva `gnCrXcR1j3mz8Hd9THXhyh` ("Reunión de 30 min entre Emilia Pimenta Lombardi y Sol", accepted) → confirmación Telegram. Pendiente: Sol cancela en cal.com/bookings.
- **AFECTA:** n8n `UTkII2kd3RHDlizo` (versión `453e84ce`), Drive (hoja `clientes-contactos`), doc v1.2 (§4, fix 9), `log.md`.

## 2026-10-08 (8) — Timezone workflow a `America/Argentina/Buenos_Aires`

- **Causa:** el trigger 07:00 corría en hora del servidor (UTC = 04:00 AR). Funcional igual por la ventana 26h, pero no era lo pactado.
- **Fix:** `setWorkflowSettings` con timezone AR, verificado en vivo. Estado estable: Drive con 2 clientes + 6 internas; el cron 07:00 AR trae solo lo nuevo.
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (settings), doc v1.2 (§1), `log.md`.

## 2026-10-08 (7) — Fetch solo último día: `created_after` −26h (exec 3505 success, lote vacío)

- **Problema:** el Fetch traía todo el historial en cada corrida → 8 re-escrituras y copias `(1)(2)(3)` en Drive. Corrías manuales agravaban.
- **Fix:** query param `created_after = {{ $now.minus({ hours: 26 }).toISO() }}` en `Fetch Fathom Meetings` (parámetro documentado en la API oficial). Ventana 26h cubre el cron 07:00 con 2h de solape. Verificado exec 3505: `items: []`, success sin escribir nada.
- **Nota:** backfills (reuniones viejas no procesadas) requieren corrida manual con ventana ampliada; el cron diario ya no las toca.
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (versión `ffd071f6`), doc v1.2 (§1, fix 8, caveat 1), `log.md`.

## 2026-10-08 (6) — Filtro por lados en builder: invitados + hablantes (exec 3503 success)

- **Problema:** clasificación solo por `calendar_invitees` — las 8 reuniones caían en Internas aunque la vinícola del 03/10 tenía 2 clientas hablando (Leticia 248 + Vanessa 20 segmentos). Además `calendar_invitees_domains_type` de Fathom miente (`one_or_more_external` en las 8) y `shared_with` no trae mails.
- **Fix:** `sideOf()` mapea cada nombre/mail a emilia/proyectopi/externo sobre la unión invitados + hablantes del transcript + `recorded_by`. Externo presente → `clientes`; cero señal → internas + `[revisar]-` (cierra el quirk del spec §5). Nombre por lados + líneas de evidencia (`Invitados calendario`, `Hablantes en transcript`, `Grabado por`) en el `.md`.
- **Verificación:** exec 3503 `success` — las 2 del 03/10 a `Reuniones-Clientes` (`2026-10-03_emilia-vanessa-ferreira-leticia-gentilini_*.md`), las 6 restantes a Internas como `emilia-proyectopi`. En el camino: fix de `invitees` duplicado + `date` TDZ (el reemplazo había abarcado las declarations).
- **Pendiente:** limpieza de Drive (borra Sol; próxima corrida regenera 6+2 limpio) + re-import al vault de los 8 con contenido enriquecido.
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (versión `52cc8643`), doc v1.2, `log.md`.

## 2026-10-08 (5) — Canvas único n8n: Cron + Core + Docs en `UeDkqVZSeLnae5cF` (exec 3500 success)

- **Merge:** el Core absorbió el trigger 07:00 y la cadena de Docs; la rama confluye en cadena compartida Save → Create → Move → Apply con pairing `$('Classify Meeting').item` en expresiones. Descartados los MergeBack (Code no resuelve pairing de forma estable: Save devuelve solo `{id}`, `$input.first/item` inconsistentes por modo). Cron (`2gUlVXu7xk1Jd12s`) y Format (`LysH41yu1s5wXkPz`) archivados. Router intacto (referencia por ID).
- **Notas:** `setWorkflowMetadata` (rename) devuelve 500 del servidor — nombre sin cambiar, sin impacto. Lote grande de 18 ops también dio 500; por lotes chicos funciona.
- **Doc:** `arquitectura-n8n-os-emilia.md` v1.1 con la estructura nueva.
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (versión `28524385`), archivados Cron + Format, doc v1.1, `log.md`.

## 2026-10-08 (4) — Doc técnico n8n nodo por nodo: `arquitectura-n8n-os-emilia.md`

- **Nuevo:** `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` v1.0 — referencia de los 5 workflows OS-Emilia con tabla por nodo (tipo, credential, expresiones clave), lógica del builder, historial de los 5 fixes del día con versiones, caveats (dedup, `chat_id`, mock, quirk `needsReview`) y cómo probar. Verificado contra API: conexiones del Router (fallback → Send Help) incluidas.
- **AFECTA:** `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md`, `log.md`.

## 2026-10-08 (3) — `.gdoc` a su carpeta: builder envía `folderId` (exec 3495 success)

- **Causa:** `Build Meeting Document` no enviaba `folderId`; el sub-workflow creaba el Google Doc en la raíz de Mi unidad y el Move no tenía destino. Los 8 `.gdoc` de hoy estaban en la raíz.
- **Fix:** el builder mapea `folder` internas/clientes a su Folder ID y lo incluye en el output; Create y Move lo consumen. Verificado: corrida 3495 `success`, `.gdoc` nuevos en `Reuniones-Internas/`. Versión Core `4babe389`.
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (versión `4babe389`), `log.md`.

## 2026-10-08 (2) — Nombres Drive opción A `fecha_participantes_recid` (exec 3492 success)

- **Cambio:** `Build Meeting Document` (Fathom Core) arma `fileName` con slug de participantes (nombre o local-part del mail, máx 60) + `recording_id`, en vez de slug de título. Verificado: `2026-10-03_emilia-pimenta-lombardi_189333562.md` — sin "impromptu". Versión Core `a3a73dad`.
- **Import inmune:** `import_drive_reuniones.py` resolvió los 8 renombrados a los mismos destinos por `call_id` (0 importados, 8 omitidos).
- **AFECTA:** n8n `UeDkqVZSeLnae5cF` (versión `a3a73dad`), `log.md`.

## 2026-10-08 — Loop Fathom→Drive→vault verificado end-to-end (exec 3489 success) + import Drive→raw/reuniones

- **Publicados y activos (5/5 OS-Emilia):** Fathom Core (`UeDkqVZSeLnae5cF`), Format Google Doc (`LysH41yu1s5wXkPz`), Fathom Cron 07:00 AR (`2gUlVXu7xk1Jd12s`), Telegram Router (`YWpuV5p0vCDTbIHz`), Agenda mock (`UTkII2kd3RHDlizo`). Cal.com no se tocó (pedido explícito).
- **Creds:** Fathom Emilia ✅ (fetch pasa), Telegram `emiliaospi_bot` ✅ cableado (sin filtro chat_id aún), Drive + Docs OAuth reconectados por Sol en n8n UI (antes: `needs to be reconnected`, exec 3473/3475 fallaban en `Save Internal Meeting`).
- **Fix 1 — `Apply Google Docs Formatting`:** `jsonBody` interpolaba objeto → `[object Object]`; se serializa en Code node (`batchUpdateJson`) — versión `46e197f9`.
- **Fix 2 — misma:** el cableado es `Restore → Move → Apply`, el `$json` del Apply es salida del Move (sin `batchUpdateJson`); se referencia `$('Restore Format Requests')` por nombre en `url` + `jsonBody` — versión `8ac83b6f`.
- **Verificación:** exec 3489 `success` sin error; 8 reuniones en `G:\Mi unidad\OS-Emilia\Reuniones-Internas\` (.md + Google Doc formateado).
- **Import vault:** nuevo `scripts/import_drive_reuniones.py` (+ `_notas.md`) — copia `.md` de Drive Stream a `raw/reuniones/YYYY-MM-DD-<call_id>.md`, idempotente con `.import-state.json`. Importados 7 nuevos (24/09 ×2, 26/09 ×3, 03/10 ×2) + 827502057 previo; 26 duplicados omitidos.
- **Caveat dedup:** Fathom Core no tiene control por `recording_id` (Data Table `OS-Emilia — Bot State` existe pero sin conectar, spec §16.2) — cada corrida re-escribe todo y Drive acumula copias `(1)(2)(3)`. El import del vault es inmune (idempotente por `call_id`). Fix real pendiente: state check en el Core + filtro de fecha.
- **Análisis:** `@fathom-pm` vía task no corre en este entorno (free tier); análisis del 827502057 hecho inline como propuesta (anexar sección IV al reporte del día, spec terreno-Brasil si amerita).
- **Pendiente:** filtro `chat_id` en Router (Emilia manda `/start`, se setea y se publica); borrar copias `(1)-(4)` en Drive; reconectar Sheets real para agenda no-mock (Mes 2).
- **AFECTA:** n8n (5 workflows publicados, 2 versiones Format), `scripts/import_drive_reuniones.py`, `scripts/import_drive_reuniones_notas.md`, `raw/reuniones/` (8 archivos), `raw/reuniones/.import-state.json`, `log.md`.

## 2026-10-05 (2) — MCP `fathom-proyectopi` reparado: `env` → `environment` (+ 2 bugs silenciosos) — 7/7 MCP

- **Síntoma:** `✗ fathom-proyectopi failed (MCP error -32000: Connection closed)` — mismo síntoma genérico que Leantime, causa totalmente distinta.
- **Causa raíz:** la clave del bloque en `opencode.json` era `env` cuando la correcta es **`environment`** (confirmado en docs oficiales opencode.ai/docs/mcp-servers → opciones del MCP local). Con `env` la variable se **ignora en silencio**: el servidor muere con `FATHOM_API_KEY env var is required` (capturado al correr `npx -y @luminarylane/fathom-mcp-server` a mano y ver su stderr en JSON) y opencode solo reporta el `Connection closed` genérico.
- **Diagnóstico:** handshake manual `initialize` + `tools/list` por stdin con la variable inyectada a mano → 4 tools (`fathom_list_meetings`, `fathom_get_summary`, `fathom_get_transcript`, `fathom_search_meetings`). `opencode mcp debug fathom-proyectopi` → "not a remote server": el subcomando `debug` solo aplica a MCP remotos/OAuth.
- **Fix `opencode.json`:** `fathom-proyectopi` → `environment: { "FATHOM_API_KEY": "{env:FATHOM_API_KEY_PROYECTOPI}" }` + `timeout: 30000` (el default de opencode es 5000 ms y el arranque en frío de `npx` lo supera).
- **Bugs silenciosos con la misma causa:** `comfyui` y `autocad` también usaban `env` → sus variables se ignoraban. `COMFYUI_URL` coincidía con el default (8188) y no se notaba; `ACAD_MCP_OUTPUT_ROOT` **sí** importaba: las salidas CAD se escribían fuera de `activos/caddy-salidas`. Ambos corregidos a `environment`.
- **Verificación:** `opencode mcp list` → **7/7 ✓ connected** (antes 5/7).
- **Wiki:** `wiki/glosario/software/opencode.md` → nueva sección [[#Trampas MCP verificadas]] (tabla de 4 trampas + método de diagnóstico en 4 pasos + advertencia del caso silencioso), fila `fathom-proyectopi` agregada a la tabla MCP, filas `comfyui`/`autocad` con `environment`, `ultima_actualizacion` 2026-10-05, y corregido heading `## Conceptos relacionados` duplicado.
- **AFECTA:** `opencode.json`, `wiki/glosario/software/opencode.md`, `log.md`, `raw/sessions/2026-10-05-sesion-fix-mcp-leantime.md`.

## 2026-10-05 — MCP Leantime reparado: `remote` + `x-api-key` sobre subdominio EasyPanel (URL canónica)

- **Síntoma:** `✗ leantime failed (MCP error -32000: Connection closed)` con 6/7 MCP OK.
- **Causa 1 — puente local inexistente:** la config llamaba `node …/node_modules/leantime-mcp/bin/leantime-mcp.js` y ese paquete ya no estaba instalado (lo arrastró una reinstalación de opencode). El paquete `leantime-mcp` está **deprecado oficialmente** (Leantime 3.10.3+ habla Streamable HTTP directo).
- **Causa 2 — URL equivocada + certificado autofirmado:** la config apuntaba a `https://pitau.tech/mcp`, que es el **panel de EasyPanel** (cert `CN=Easypanel`, sin SAN) y no Leantime. Node: `self-signed certificate`. `n8n.pitau.tech` sí tiene Let's Encrypt y por eso ese MCP siempre anduvo.
- **Diagnóstico:** URL real `https://pitautech-leantime.3nq4ow.easypanel.host` → `/mcp` responde 401 (existe, pide credencial); cert `*.3nq4ow.easypanel.host` issuer Let's Encrypt `YE2`; probe JSON-RPC `initialize` con `x-api-key` → **200 con respuesta MCP válida** (`Authorization: Bearer` sobre la API key `lt_…` → `Invalid API Key`).
- **Fix `opencode.json`:** bloque `leantime` pasa de `local` (binario + `--token … --insecure`) a `type: remote` + `url` del subdominio de la app + `headers: {"x-api-key": "{env:LEANTIME_TOKEN}"}` + `timeout: 30000`. Efecto extra: el token deja de quedar impreso en `opencode mcp list` (quedó registrado en claro en la sesión del 2026-09-27).
- **Verificación:** `opencode mcp list` → 7 servers, `✓ leantime connected`. Queda pendiente reiniciar la sesión OpenCode para que las herramientas de Leantime queden cargadas. `fathom-proyectopi` sigue en rojo (`npx @luminarylane/fathom-mcp-server`, tema aparte).
- **Wiki:** creada `wiki/glosario/software/leantime.md` (instalación/VPS, MCP remoto, credenciales `lt_`→`x-api-key` vs PAT→Bearer, diagnóstico replicable, lección `pitau.tech` ≠ subdominio de app) + fila Leantime en `wiki/glosario/software/00-index.md` + fila MCP actualizada en `wiki/glosario/software/opencode.md`. Refs verificadas 200: docs.leantime.io (MCP), marketplace.leantime.io (plugin MCP Server), github.com/leantime/leantime-mcp, leantime.io/pricing.
- **AFECTA:** `opencode.json`, `wiki/glosario/software/leantime.md`, `wiki/glosario/software/00-index.md`, `wiki/glosario/software/opencode.md`, `raw/sessions/2026-10-05-sesion-fix-mcp-leantime.md`, `log.md`.

## 2026-09-30 — Codex 101 Brais + pbook instalación Codex (canónico) — Codex CLI + GPT-5.6

- **Video corregido:** `https://www.youtube.com/watch?v=af1KAQCD7mk` (Brais Moure — Codex + GPT-5.6) verificado 200 — corrige `irR8437xihg` previo (opencode). Guardado en `raw/contenidos/2026-09-30-codex-101-brais.md` (propuesta HITL) + deprecado `raw/contenidos/2026-09-30-opencode-101-brais-codex.md` → `descartado-corregido`.
- **Nuevos pbooks canónicos:** `wiki/glosario/interno/pbooks/pbk-codex_101_Brais.md` (Codex 101 Brais: install.sh/ps1, npm, Sign in with ChatGPT, CLI/Desktop/IDE/Cloud, AGENTS.md, MCPs, Skills, Sol/Terra/Luna) + `wiki/glosario/interno/pbooks/pbk-instalacion-codex.md` (réplica vault Windows: CLI+Desktop, sandbox elevated/unelevated, MCPs espejo fathom/fathom-proyectopi/leantime/autodesk-help/autocad vía `~/.codex/config.toml`, rutina sin PC n8n Cron 07:00 vs GitHub Actions 10 UTC) + alias `pbk-codex-instalacion.md` → canónico. Curado por `@contenidos`.
- **Índice:** `wiki/glosario/interno/pbooks/00-index.md` — añade `pbk-instalacion-codex` en Infraestructura + `pbk-codex_101_Brais` en Agentes.
- **Proyectos:** `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` v1.0 ahora apunta al canónico `pbk-instalacion-codex` + ref Brais.
- **Verificación:** refs 200 sin 404 (developers.openai.com/codex/*, github.com/openai/codex, youtube af1KAQCD7mk). MCPs Codex listos para Emilia: `fathom` (OAuth Emilia) + `fathom-proyectopi` + `leantime` + `autocad` + `autodesk-help` — `.env` se configura en su PC.
- **AFECTA:** `raw/contenidos/2026-09-30-codex-101-brais.md`, `raw/contenidos/2026-09-30-opencode-101-brais-codex.md`, `wiki/glosario/interno/pbooks/pbk-codex_101_Brais.md`, `wiki/glosario/interno/pbooks/pbk-instalacion-codex.md`, `wiki/glosario/interno/pbooks/pbk-codex-instalacion.md`, `wiki/glosario/interno/pbooks/00-index.md`, `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md`, `log.md`.

## 2026-09-10 — AGENTS.md slim 393→125 (9 pasos)

- P1 Contexto AR → `wiki/estudio/00-index.md` (sección primera, íntegro); AGENTS 2 líneas.
- P2 Árbol regenerado desde disco → `standares/oficina/estructura-carpetas.md` (template ideal); AGENTS puntero.
- P3 Frontmatter mergeado a `template_arq` (+`ultima_actualizacion`); campo `oficina:` eliminado del spec y de Principios.
- P4 Glosario partido: reglas de calidad → `wiki/glosario/00-index.md`; conducta → `vaultworm-arq.md`; árbol regenerado; AGENTS 2 líneas.
- P5 Ingest/Query/Lint → `pbk-agentes-vaultarq.md` (tasks las corre otro agente, sin duplicar).
- P6 Bloque BIM borrado (rutas sobreviven en `revit.md`/`bim-familias.md`).
- P7 ComfyUI duplicado verbatim borrado (28 líneas ×2 → 2 líneas puntero a `pbk-comfyui`).
- P8 Estructura WF → `reglas-workflows-comfy.md` (sección aparte, sin renombres históricos); Scripts → puntero.
- P9 Estándares unificados en `interno/standares/` (movidas `oficina/`+`tecnico/`, 14 refs retargeteadas, `wiki/estandares/00-index` redirige); 7 refs `AGENTS.md:NNN` vivas → anchors (resto en log/raw intocables); auditoría 268 links → 0 rotos.
- **AFECTA:** `AGENTS.md` (393→125), `wiki/estudio/00-index.md`, `estructura-carpetas.md`, `template_arq/00-index.md`, `glosario/00-index.md`, `vaultworm-arq.md`, `pbk-agentes-vaultarq.md`, `reglas-workflows-comfy.md`, `interno/standares/*`, 7 archivos refs, `log.md`.

## 2026-09-09 — Propuesta viernes: Caso Fundador #01 + HTML + 2 conceptos

- Sesión `@brainstormy` (36 ideas + Top 3 + wildcards, crudo `raw/brainstorm/b-2026_09_09-1.md`): referentes (ZHA A+I, Foster ARD, Hypar, EvolveLAB, Lumera/Elevated/AI50), modelo IA Lab Partnership, portfolio como subsidio, bundle early bird + academia, puesta en escena viernes.
- Propuesta: `proyectos/STUDIO_OS-Emilia/presentacion/04-propuesta-viernes-lab-partnership.md` (Caso #01, sprint 56 hs, 600 fundador, trimestre) + `propuesta-viernes-caso-fundador.html` (scroll + hoja A4 firmable) + esquema `03-propuesta-viernes-esquema.md` desarrollado (desglose hs, tabla mercado, ritmo 2×7h).
- Conceptos nuevos: `wiki/glosario/conceptos/vault-visual.md` + `ia-lab-partnership.md` (+ filas en `conceptos/00-index.md`); entregables en `proyectos/STUDIO_OS-Emilia/00-index.md`.
- Decisiones SOL: piloto Casa masterplan, Drive + mail dedicado, Adapt1 descartado, 15 hs→14 hs/sem (56 hs sprint), ancla mercado 2.500 → fundador 600.
- **AFECTA:** `presentacion/04-propuesta-viernes-lab-partnership.md`, `presentacion/propuesta-viernes-caso-fundador.html`, `presentacion/03-propuesta-viernes-esquema.md`, `wiki/glosario/conceptos/{vault-visual,ia-lab-partnership}.md`, `conceptos/00-index.md`, `proyectos/STUDIO_OS-Emilia/00-index.md`, `log.md`.

## 2026-09-09 — Fathom conectado + 4 reuniones Emilia analizadas (previo propuesta viernes)

- MCP oficial Fathom (`https://api.fathom.ai/mcp`, OAuth) declarado en `opencode.json` y autenticado con cuenta pitau.tech (`mcp list` → connected). Cambio futuro a proyectopi: `logout` + re-auth.
- Descargados transcript + summary + action items de 4 calls 28/08 a `raw/reuniones/2026-08-28-<callid>.md` (~52-59 min c/u): 802902095 (tesis open-source/Adapt1), 802992698 (infra/PCs/Magenta), 803065252 (dashboard/honorarios/piloto Magenta), 803125998 (Vinícola Gema/plan 30 días/valores).
- Análisis simultáneo (4 subagentes en paralelo) → `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta.md`: objetivos acordados O1-O6 vs abiertos A1-A7 (valores, alcance F1, piloto único, 2hs/semana, Adapt1, archivos, cobro cambios), mapa N1-N8, señales comerciales y estructura sugerida propuesta viernes.
- Agentes `@fathom-pm` + `@contenidos` creados (`.opencode/agents/`, skills espejo) y registrados en `pbk-agentes-vaultarq.md` + `opencode.md`; `specs/260909-agente-reuniones-fathom-specs.md` en dos tracks; skills importados: deep-research, architecture-decision-records, article-writing, brand-voice, excalidraw-skill.
- **AFECTA:** `opencode.json`, `raw/reuniones/*`, `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta.md`, `.opencode/agents/fathom-pm.md`, `.opencode/agents/contenidos.md`, `.opencode/skills/{fathom-pm,contenidos,deep-research,architecture-decision-records,article-writing,brand-voice,excalidraw-skill}/*`, `specs/260909-agente-reuniones-fathom-specs.md`, `pbk-agentes-vaultarq.md`, `opencode.md`, `log.md`.

## 2026-09-09 — Glosario: coautores sprint, design-thinking, dedup SDD, charlas Bañón/Berkel, migración a anchors nativos

- **jake-knapp:** nueva `## El equipo del sprint` (Zeratsky: empezar-por-el-final; Kowitz: story-centered design; Margolis: entrevista 5 actos; Burka: sentido startup) + `## Bibliografía` (*Sprint* S&S 2016 ISBN 9781501121746, *Make Time* Crown 2018 ISBN 9780525572435, *Click*) + fichas S&S/Google Books en Referencias.
- **design-thinking:** reescrito completo (era stub de 5 líneas): origen IDEO+d.school, tabla 5 modos con trampas, 7 mindsets, giro 2016 proceso→habilidades (Carter), traducción a arquitectura. Link viejo Stanford `me113/d.school.html` confirmado 404 → reemplazado por `me113/d_thinking.html`.
- **SDD dedup:** eliminado `wiki/glosario/entidades/sdd-spec_driven_development.md` (SDD es concepto); nota en `entidades/00-index.md` + `conceptos/sdd` §9.
- **ben-van-berkel:** nueva `## The New Understanding (2011)` (Current Work League 1-feb-2011, Cooper Union, modera Stan Allen; tesis post-crisis + 4 tópicos; entrevista Wessner 2-feb) + 3 links archleague/cooper.
- **carlos-banon:** nueva `## NXT BLD 2026` (tesis 3 capas + agency-led workflows + "Form follows you", demo con Yiping Goh) desde fetch de nxtbld.com.
- **Anchors nativos:** índices `[texto](#slug)` → `[[#Encabezado exacto]]` en sdd, kanban, design-thinking, jake-knapp, design-sprint, braintrust-pixar, seguridad-psicologica, marco-creativo, bjarke-ingels, ben-van-berkel, carlos-banon, fredy-fortich; cross-file `[[...#slug]]` → `[[...#Encabezado exacto]]` en sdd. Causa raíz de "links que no andan" en Obsidian.
- **Auditorías:** script scopado `wiki/glosario/**` → 0 absolutos rotos (solo placeholder intencional en template); índices referentes/software verificados fila por fila (todos resuelven); externas verificadas 200 (taschen ×2, kanban.university, epa jitkanban, spec-kit, unstudio, big.dk/people, nxtbld, mvrdv fortich).
- **AFECTA:** `wiki/glosario/referentes/jake-knapp.md`, `ben-van-berkel.md`, `carlos-banon.md`, `bjarke-ingels.md`, `fredy-fortich.md`; `wiki/glosario/conceptos/design-thinking.md`, `sdd-spec_driven_development.md`, `kanban.md`, `design-sprint.md`, `braintrust-pixar.md`, `seguridad-psicologica-aristotle.md`, `marco-creativo-google-pixar.md`; `wiki/glosario/entidades/00-index.md`; `log.md`; `raw/sessions/2026-09-09-sesion-glosario-fixes.md`.

## 2026-09-09 — Marco creativo Google + Pixar (base pitau-tech)

- **Conceptos (4):** nuevas `wiki/glosario/conceptos/design-sprint.md` (GV 5 días + adaptación a anteproyecto), `braintrust-pixar.md` (braintrust + dailies + plussing + ugly babies + braintrust semanal del estudio), `seguridad-psicologica-aristotle.md` (Aristotle + Work Rules + 20% time + libro de obra sin culpa), `marco-creativo-google-pixar.md` (síntesis 5 pilares + traducción a estudio ARG + plan 4 semanas + antipatrones).
- **Referentes (4):** nuevos `wiki/glosario/referentes/google.md` (org, con Bock/Doerr/Edmondson/Buchheit como menciones sin ficha), `pixar-animation-studios.md` (org), `ed-catmull.md` y `jake-knapp.md` (personas). Índices `conceptos/00-index.md` y `referentes/00-index.md` actualizados.
- **Fuentes verificadas:** gv.com/sprint, whatmatters.com (OKR Playbook), hbr.org R0809D, atlassian.com (braintrust), nytimes Aristotle, wikipedia side_project_time, books.google Work Rules, design.google, techcrunch sprint, forbes ugly-babies, mckinsey Catmull, d3.harvard kaizen — todas 200. NO citar: rework.withgoogle.com (404, URL vieja de Aristotle).
- **AFECTA:** `wiki/glosario/conceptos/*`, `wiki/glosario/referentes/*`, índices, `log.md`.

## 2026-09-09 — software/ a UNICO .md (fin carpetas legado)

- Migrados a archivo único navegable: `ffmpeg.md`, `obs.md`, `gohighlevel.md` (6 etapas como secciones) + 6 stubs (`revit, rhino, grasshopper, twinmotion, unreal-engine, impresion-3d`). `autocad.md/comfyui.md/faster-whisper.md` ya cubrían su legado (verificado, sin pérdida).
- Eliminadas 10 carpetas: `faster-whisper ffmpeg gohighlevel obs grasshopper impresion-3d revit rhino twinmotion unreal-engine`.
- Retargets: `opencode.md` → `pbk-config_ctas_git_github_opencode` (nombre truncado roto por renombre); filas `00-index` a singles; `template.md` reescrito a patrón single-file; `AGENTS.md` sin excepción legado.
- Auditoría: 267 links índices → 0 rotos, 0 `../` (restan solo ejemplos en código y placeholders intencionales).
- **AFECTA:** `wiki/glosario/software/*`, `AGENTS.md`, `specs/260907-telegram-vault.md`, `log.md`.

## 2026-09-09 — Regla links agendada en AGENTS.md

- `AGENTS.md` (Nombrado + Glosario regla 6): convención de links obligatoria — entre archivos `[[ruta/desde/raíz|alias]]` sin extensión ni `../`; índice interno `[[#Encabezado exacto]]` (nunca `[texto](#slug)` por tildes); carpetas no se enlazan; excepción portable GitHub `[texto](#slug-ascii)`.
- Motivo: índice de `pbk-config_ctas_git_github_opencode` con slugs a mano no saltaba en Obsidian.
- **AFECTA:** `AGENTS.md`, `log.md`.

## 2026-09-09 — Fix anchors índice pbk-config_ctas (Obsidian)

- Problema: índice superior `[texto](#slug)` no saltaba en Obsidian (2 de 8 anchors con tildes: `verificación`, `conexión`).
- Fix: índice convertido a links nativos Obsidian `[[#Encabezado]]` (resuelven por texto del header, inmunes a slugificación). Wikilinks y URLs externas ya verificados OK.
- Nota: `[[#...]]` no renderiza en GitHub web; se prioriza Obsidian (lector declarado). Si un índice debe ser portable, usar `[texto](#slug-ascii-sin-tildes)`.
- **AFECTA:** `wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode.md`, `log.md`.

## 2026-09-09 — Links rotos restantes resueltos

- `backlog-n_03_WF01.md`: `[[../tests/README]]` → `[[n_02-img2img/tests/README|tests n_02 (referencia)]]` (no existe tests en n_03; se enlaza metodología de tests más cercana con alias explícito).
- Creadas 2 páginas que los specs referenciaban: `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-07-obra-balcarce.md` (andamio minuta Telegram) y `wiki/raw/2026-09-07-ghl-6-etapas-transcripcion.md` (andamio transcript GHL, crea `wiki/raw/`).
- Auditoría final: 298 links en índices → 0 rotos, 0 `../`. Restan solo placeholders intencionales (`[[...]]` en 2 análisis, `otro-referente` en template).
- **AFECTA:** `backlog-n_03_WF01.md`, 2 archivos nuevos, `log.md`.

## 2026-09-09 — Reparación encoding + links de índices

- **Mojibake:** 35 `.md` con `â"œâ"€â"€` reparados a UTF-8 real (`├──`, `—`, `→`, tildes). Causa: UTF-8 leído como cp1252 y re-guardado. `log.md` excluido (inmutable, 78 líneas con mojibake — pendiente decisión).
- **Links:** 297 links de índices auditados → 111 rotos + 8 `[[../]]` → 0. Regla: rutas absolutas desde raíz (`[[wiki/...]]`), sin `../`, sin barras residuales, carpetas como texto o link a su índice.
- **Stubs:** 21 (8 comandos AutoCAD, 6 nodos ComfyUI, 6 índices software, `MVP_04/00-index.md`). **Rename:** `output_log-n_03-WF01.md` → `output_log-n_03_WF01.md`.
- **Pendiente:** `[[../tests/README]]` en backlog n_03 (sin destino), 2 páginas de pipeline por crear (transcript GHL, minuta Balcarce).
- **AFECTA:** 35 `.md` reparados + ~40 con links reescritos + 21 nuevos + `raw/sessions/2026-09-09-sesion-fix-encoding-links.md`, `log.md`.

## 2026-09-09 — PM + ComfyUI + plan semanal (spec vault-cerebro)

- **Mejora continua (9 fichas):** nuevas `wiki/glosario/conceptos/kanban.md`, `agile-arquitectura.md`, `last-planner-system.md`, `kaizen.md`, `retrospectivas.md`, `cinco-s-5s-archivos.md`, `pm-project-management.md`, `okr-goals.md`; `lean.md` ampliado (8 desperdicios del estudio). Índice `conceptos/00-index.md` actualizado.
- **Playbooks:** nuevo `pbk-pm_vault.md` (Leantime: tasks/subtasks/sprints/milestones/GOALS-OKR, Kanban+LPS diario, rituales, MCP futuro) y `pbk-comfyui-arquitectura.md` (canónico: txt2img/img2img/Canny/Depth/otros CN/dual/upscale/video LTX/RunPod/prompt-packs/DoD). Índice `pbooks/00-index.md` actualizado.
- **Spec:** `specs/260907-vault_cerebro.md` suma cuadro maestro Semanas 0–4 + checklist instalación (inventario → OpenCode → Antigravity → Fathom → GH Actions → Leantime → ComfyUI Sol/Emilia) + links a fichas nuevas.
- **Script:** nuevo `scripts/inventario-hardware.ps1` (CPU/RAM/GPU-VRAM real/monitores/discos/red/software/ComfyUI/CAD; salida .md+.json a `raw/sessions/`). Índice `scripts/00-index.md` actualizado.
- **AFECTA:** `wiki/glosario/conceptos/*`, `wiki/glosario/interno/pbooks/*`, `specs/260907-vault_cerebro.md`, `scripts/*`, `log.md`.

## 2026-09-08 — Playbook: Separación y Gestión de Cuentas (Git, GitHub, OpenCode)

- **Nuevo Playbook:** Creado `wiki/glosario/interno/pbooks/pbk-cuentas-git-github-opencode.md` documentando la arquitectura de cuentas segregadas (`proyectopi.31416@gmail.com` vs `pitau.tech@gmail.com`).
- **Detalle de capas:**
  1. Git: Directiva `includeIf` en `.gitconfig`, config condicional y `.git/config` local.
  2. GitHub CLI: Prioridad de `GH_TOKEN` en `.env` vs `hosts.yml`.
  3. OpenCode: Perfiles aislados (`P:\00-repos\.opencode-profiles\proyecto-pi\` vs `pitau\`), rutas de `auth.json`, logs de ejecución y protocolo para uso temporal cruzado (conectar/desconectar con `opencode auth logout`).
- **Índice:** Actualizado `wiki/glosario/interno/pbooks/00-index.md` con categoría *Infraestructura, Cuentas y Entorno*.
- **AFECTA:** `wiki/glosario/interno/pbooks/pbk-cuentas-git-github-opencode.md`, `wiki/glosario/interno/pbooks/00-index.md`, `log.md`.

## 2026-09-08 — CalHon recuperado: MVP_03 Gest + MVP_03b PyDO

- **Recuperado:** `P:\devs\CalHon\` (CalHon — Honorarios CPAU, K=640M ICC junio 2026, Cuadro 5+6 + Clarín ARQ) migrado al vault como **MVP_03b-calhon-pdo** — `proyectos/MVP_03b-calhon-pdo/` con `codigo/` (Vite 8 + React 19 + jsPDF), `docs/` (ADRs/FEATURES/CHANGELOG/PAGOS), `readme-mvp_03b.md`. Origen `P:\devs\CalHon\` queda como respaldo.
- **Renombrado:** `proyectos/MVP_03-calculadora-honorarios` → `proyectos/MVP_03-calhon-gest` (CalHon Gest — honorarios gestiones TAD, curva USD/Oro + CPAU Cuadro 8). `readme-mvp_03.md` actualizado con cross-link a MVP_03b.
- **Índice:** `proyectos/00-index.md:18` ahora lista ambos: `MVP_03-calhon-gest` (gestiones) y `MVP_03b-calhon-pdo` (PyDO + monto de obra).
- **Puertos:** PyDO → `http://localhost:5173` (CalHon — Honorarios CPAU), Gest → `http://localhost:5174` (Calculadora de Honorarios). Verificados 200 OK.
- **AFECTA:** `proyectos/MVP_03-calhon-gest/`, `proyectos/MVP_03b-calhon-pdo/`, `proyectos/00-index.md`, `P:\devs\CalHon\` (origen)

## 2026-09-07 — Sesión cierre: glosario 4 ramas + vaultworm-arq + Telegram

- **Regla glosario:** `AGENTS.md:157` reescrita a 4 ramas `wiki/glosario/software|entidades|referentes|conceptos` â€” toda entrada `wiki/glosario/**` exige `## Conceptos relacionados` â‰¥2 wikilinks + `## Referencias` con bÃºsqueda web verificada + referente en `wiki/glosario/referentes/` si aplica. Estructura actualizada.
- **Referentes:** `wiki/glosario/referentes/00-index.md`, `template.md`, `andrej-karpathy.md` (gist Karpathy + 3 fuentes 200)
- **Renombre:** `bookworm` â†’ `vaultworm-arq` en `raw/vaultworm-arq/`, `.opencode/agents/vaultworm-arq.md` (`@vaultworm-arq`), `.github/workflows/vaultworm-arq.yml`, `.obsidian/workspace.json`
- **Agente:** `.opencode/agents/vaultworm-arq.md` (temp 0.3, rawâ†’digest iterativo) + `raw/vaultworm-arq/digest-2026-09-07.md` (5 topics, entidades, referentes) + workflow push `raw/sessions/**` / lunes 09:00 AR
- **Telegram:** `.env:14` `TELEGRAM_BOT_TOKEN`/`CHAT_ID` para `vaultworm_arqbot` (grupo con Emilia) â€” plan: digest.mdâ†’PDF via pandoc + `sendDocument` + inline âœ…/âœï¸/âŒ, feedback via n8n `getUpdates` â†’ issue/commit
- **SesiÃ³n:** `raw/sessions/2026-09-07-sesion-glosario-vaultworm-arq-telegram.md`
- **AFECTA:** `AGENTS.md`, `wiki/glosario/{00-index,software,conceptos,referentes}/`, `wiki/software/index.md`, `.opencode/agents/vaultworm-arq.md`, `.github/workflows/vaultworm-arq.yml`, `raw/vaultworm-arq/`, `.env`

## 2026-09-07 â€” UnificaciÃ³n wiki/software â†’ wiki/glosario (elimina carpeta)

- **Eliminada:** `wiki/software/` completa (19 archivos). Todo relocalizado sin pÃ©rdida.
- **Conceptos (externo):** `wiki/software/bim-metodologia.md` â†’ `wiki/glosario/conceptos/bim-metodologia.md` (tipo: concepto, origen externo, ISO 19650/LOD/CDE). Propio irÃ¡ a `wiki/glosario/interno/standares/` (tec-/ops-)
- **Referentes (externo):** `wiki/software/ia-arquitectura-estudios-internacionales.md` â†’ `wiki/glosario/referentes/ia-estudios-internacionales.md` (global) + `zha-hadid-architects.md`, `big-bjarke-ingels-group.md`, `mvrdv.md`, `foster-partners.md` (individuales)
- **Software (comandos):** `wiki/software/comfyui/nodos/*` + `modelos/*` â†’ `wiki/glosario/software/comfyui/nodos/*` + `modelos/*` (unificado, arquitectura-realmix conservado). `wiki/software/glosario/{ffmpeg,faster-whisper,obs,gohighlevel}` â†’ `wiki/glosario/software/{...}` (correcciÃ³n ruta duplicada)
- **Interno (propio):** creado `wiki/glosario/interno/` con `standares/00-index.md` (tec-/ops- vacÃ­o, a definir) y `pbooks/00-index.md` + `pbk-comfyui-controlnet.md`, `pbk-comfyui-flujos-index.md`, `pbk-troubleshooting-reconexion.md` (ex- `wiki/software/comfyui/flujos/` y `playbooks/`)
- **Actualizados:** `AGENTS.md` (estructura vault, glosario 5 ramas, esquema interno, workflows), `00-index.md`, `wiki/00-index.md`, `wiki/glosario/00-index.md`, `wiki/glosario/referentes/00-index.md`, `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/software/00-index.md`, `wiki/glosario/software/comfyui/00-index.md`, + bulk fix 30 archivos con `wiki/software/*` â†’ `wiki/glosario/*`
- **VacÃ­a ahora:** `wiki/estandares/` queda para espejo operativo, canÃ³nica es `wiki/glosario/interno/standares/`
- **AFECTA:** 19 moves + 4 creates + 30 bulk fixes, `AGENTS.md`, Ã­ndices

## 2026-09-07 â€” SesiÃ³n GHL transcripciÃ³n â†’ vault automÃ¡tico + cierre

- **SesiÃ³n documentada:** `raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault.md` â€” objetivo: transcribir academia GHL (sin descarga) para alimentar vault sin desperdiciar conocimiento, aplicado a diagnÃ³stico Emilia (ciclo 6 etapas: relevamiento â†’ producciÃ³n)
- **Plan ingest:** `specs/260907-ghl-ingest-6-etapas.md` (captura sin descarga â†’ transcripciÃ³n â†’ raw â†’ vault)
- **Plan automÃ¡tico:** `specs/260907-ghl-extraccion-automatica.md` â€” pipeline `OBS mkv â†’ ffmpeg â†’ faster-whisper (CPU) â†’ wiki/raw/*.md` en 1 comando, resto automÃ¡tico. 100% libre (MIT/Apache, 0 licencia)
- **Script:** `scripts/transcribir_ghl.py` â€” `OBS mkv â†’ ffmpeg extrae mp3 â†’ faster-whisper medium/es/int8 â†’ .txt/.srt + wiki/raw/*.md` con autodetecciÃ³n ffmpeg y reutilizaciÃ³n audio
- **Glosario registrado:** `wiki/glosario/software/ffmpeg/ffmpeg-extract-audio.md`, `wiki/glosario/software/faster-whisper/transcribe.md`, `wiki/glosario/software/obs/captura-pantalla-audio.md`, `wiki/glosario/software/gohighlevel/index.md` (Ã­ndice 6 etapas), + Ã­ndices ffmpeg/faster-whisper/obs
- **PrÃ³ximo paso:** usuario graba primer video con OBS â†’ corre `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/.../captura.mkv"` â†’ pega `wiki/raw/*.md` â†’ se ejecuta ingest completo (metodologÃ­a + 6 entradas glosario GHL + servicios Pitau Tech + 07-propuesta-diagnostico)
- **AFECTA:** `raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault.md`, `specs/260907-ghl-extraccion-automatica.md`, `scripts/transcribir_ghl.py`, 6 entradas glosario, `proyectos/STUDIO_OS-Emilia/documentacion/`

## 2026-09-07 â€” CorrecciÃ³n Vault Cerebro (ortografÃ­a) + Plan detallado por semanas

- **CorrecciÃ³n:** `vault-cerbero` â†’ `vault-cerebro` en `specs/260907-vault_cerebro.md`, `proyectos/00-index.md` y `proyectos/260907-brain_emilia/00-index.md` + tags normalizados `[vault, cerebro, opencode, fathom, autocad, comfyui, early-bird, academia]`
- **Plan reescrito (240 lÃ­neas, UTF-8):** objetivo para quien reciÃ©n comienza a organizarse (mapeo de procesos + identificaciÃ³n de beneficio IA), uso de IA para scripts Lisp/AutoLISP aunque el estÃ¡ndar no use IA, definiciÃ³n de Cerebro Digital Karpathy aplicado al vault, lean/PM y tÃ©cnicas PM a investigar, MCP Leantime en VPS (pendiente usuario Emilia + URL/pass)
- **Semanas marcadas por puntos:** Semana 1 (miÃ©rcoles conceptual + instalaciÃ³n OpenCode Zen Sol: zen+go / Emilia: zen+openai + Fathom desde Meet â†’ vault con agente + schedule + docu), Semana 2 (casa en construcciÃ³n + referentes web/Instagram/ArchDaily/Pinterest â†’ modelos de visualizaciÃ³n), Semana 3 (flujo ComfyUI posprocesa AutoCAD â€” prueba simple previa a ofrecer), Semana 4 (documentaciÃ³n + clase)
- **Acentos corregidos:** reescritura UTF-8 de `specs/260907-vault_cerebro.md` y `plan.md`
- **AFECTA:** `specs/260907-vault_cerebro.md`, `plan.md`, `proyectos/00-index.md`, `proyectos/260907-brain_emilia/00-index.md`

## 2026-09-07 â€” Cierre sesiÃ³n Vault Cerbero + Brain Emilia (raw/sessions)

- **SesiÃ³n cerrada:** `raw/sessions/2026-09-07-sesion-vault-cerbero-brain-emilia.md` â€” brainstorm IA estudios internacionales (22 ideas + Atelier AutÃ³mata), principios (lenguaje positivo, creatividad con orden), plan Vault Cerbero (Week 1: OpenCode+OpenAI Emilia+Fathom, Week 2: representaciÃ³n Emiliaâ†’Lora/Canny), specs/260907-vault_cerbero, proyecto 260907-brain_emilia, SDD via opencode, 00-index en 36 carpetas, workflow GitHub Actions retirado por SPEC FIRST
- **AFECTA:** `raw/sessions/2026-09-07-sesion-vault-cerbero-brain-emilia.md`, `specs/260907-vault_cerbero.md`, `wiki/glosario/conceptos/sdd-spec_driven_development.md`

## 2026-09-07 â€” SDD Spec-Driven Development + SPEC FIRST

- **Concepto creado:** `[[wiki/glosario/conceptos/sdd-spec_driven_development|sdd-spec_driven_development]]` â€” con Ã­ndice interactivo, Â§1 CÃ³mo se aplica al vault-arquitectura al principio, flujo hÃ­brido Spec Kit + template liviano via opencode, y conexiones con [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] y [[wiki/glosario/software/opencode/00-index|opencode]]
- **Entidad creada:** `[[wiki/glosario/entidades/sdd-spec_driven_development|sdd (entidad)]]` â€” registry que enlaza al concepto
- **Workflow retirado:** `.github/workflows/opencode-vault.yml` eliminado por crearse sin spec previo â€” se recrea solo tras `âœ“ spec` + `âœ“ plan` (SPEC FIRST)
- **Flujo hÃ­brido validado:** Spec Kit via opencode (`specify init --integration opencode` + `/speckit.*`) + template liviano `specs/YYMMDD-{tema}_*.md` como fuente Ãºnica. Ambas vÃ­as convergen en `/specs/`.
- **Ãndices actualizados:** `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/entidades/00-index.md`
- **AFECTA:** `wiki/glosario/conceptos/sdd-spec_driven_development.md`, `wiki/glosario/entidades/sdd-spec_driven_development.md`, `.github/workflows/opencode-vault.yml` (retirado)

## 2026-09-07 â€” Proyecto 260907-brain_emilia + Vault Cerbero

- **Proyecto creado:** `proyectos/260907-brain_emilia/00-index.md` â€” Vault Cerbero vinculado a `[[specs/260907-vault_cerbero]]` (Plan Vault Cerbero)
- **Spec:** `specs/260907-vault_cerbero.md` â€” Week 1 Vault + OpenCode + OpenAI (cuenta Emilia) + Fathom MCP + schedule cowork, Week 2 representaciÃ³n con Emilia â†’ Lora + Canny, Semanas 3â€“4 Kit AutoCAD documentado. ConvenciÃ³n `YYMMDD-{tema_snake}` activa.
- **Estructura:** `proyectos/260907-brain_emilia/{documentacion,workflows,apps,agentes,reuniones}/` â€” planes solo en `/specs/`, proyecto solo con workflows/apps/docu agentes, linkeado via wikilinks
- **Ãndice actualizado:** `proyectos/00-index.md` â€” entrada 260907-brain_emilia
- **AFECTA:** `specs/260907-vault_cerbero.md`, `proyectos/260907-brain_emilia/00-index.md`, `proyectos/00-index.md`

## 2026-09-07 â€” Plan ingest GHL 6 etapas â†’ vault Pitau Tech (para diagnÃ³stico Emilia)

- **Plan creado:** `specs/260907-ghl-ingest-6-etapas.md` â€” pipeline completo: captura sin descarga (GHL bloquea) â†’ transcripciÃ³n â†’ raw â†’ vault â†’ glosario â†’ servicios Pitau Tech
- **Problema resuelto:** GHL academia no permite descarga directa. Soluciones documentadas: A) ExtensiÃ³n GoHighLevel Downloader (HLS nativo + Wistia/Vimeo/Loom â†’ MP4) [github.com/serpapps/gohighlevel-downloader](https://github.com/serpapps/gohighlevel-downloader) / [Chrome Web Store](https://chromewebstore.google.com/detail/downloader-for-gohighlevel/lcnajelpdoefgoilcihnpkofabpafjgd), B) OBS Studio / Win+Alt+R, C) Audacity WASAPI loopback (solo audio, ideal para vault)
- **TranscripciÃ³n:** `faster-whisper` local CPU (medium) o TurboScribe/WhisperAI en nube â€” sin subir binarios sensibles a wiki (solo refs a `activos/reuniones/ghl-academia/`)
- **Destino vault:** `wiki/raw/` (verbatim) â†’ `wiki/estudio/metodologia-ciclo-6-etapas.md` + `wiki/estudio/servicios-pitau-tech-arquitectura.md` + 6 entradas `wiki/glosario/software/gohighlevel/` + `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md` (HOY)
- **Mapeo 6 etapas â†’ diagnÃ³stico Emilia:** 1.relevamiento=DiagnÃ³stico Studio OS, 2.analisis=Blueprint TO-BE, 3.implementaciÃ³n=Build mini-prototipo, 4.pruebas=QA interno, 5.entrenamiento=capacitaciÃ³n 30min, 6.producciÃ³n=Go-live + Go/No-Go Fase 2. Sprint 30d USD 600 = etapas 1+2 completas
- **Directorios creados:** `wiki/raw/`, `wiki/glosario/software/gohighlevel/`, `proyectos/STUDIO_OS-Emilia/documentacion/`
- **PrÃ³ximo paso:** usuario pega transcript/audio â†’ se ejecutan Â§5-Â§7 del plan en una vuelta
- **AFECTA:** `specs/260907-ghl-ingest-6-etapas.md`, `wiki/raw/`, `wiki/glosario/software/gohighlevel/`

## 2026-07-28 â€” MigraciÃ³n glosario: proyectos â†’ wiki

- **Movido:** `proyectos/glosario/` â†’ `wiki/glosario/software/` (conocimiento permanente)
- **Eliminado staging:** el glosario ya no tiene fase de staging. Se escribe directamente en la wiki
- **Skill eliminada:** `glosario-sync` ya no es necesaria
- **Actualizados:** todos los wikilinks de `proyectos/glosario/` â†’ `wiki/glosario/software/`
- **AFECTA:** `AGENTS.md`, `index.md`, `proyectos/00-index.md`, `wiki/software/00-index.md`, `proyectos/MVP_02-autocad-standards/*`

## 2026-07-24 â€” Corrida txt2img estadio seed=43 (n_01-C-01)

- **Workflow ejecutado:** `workflow_txt2img_estadio.json` desde API ComfyUI
- **Seed:** 43 (vs seed=42 de baselines A-01/A-02)
- **Output:** `estadio_futbol_00009_.png` â†’ copiado a `proyectos/MVP_04-comfyui-arquitectura/n_01-txt2img/log-WF-estadio/salidas/n_01-C-01.png`
- **DocumentaciÃ³n actualizada:** `prompts-log.md`, `index.md`, `log.md`

## 2026-07-24 â€” Corrida SDXL txt2img estadio seed=42 (n_01-D-01) â€” MIGRACIÃ“N SDXL

- **Workflow ejecutado:** `workflow_txt2img_estadio_sdxl.json` (Juggernaut XL v9)
- **Modelo:** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (7.11 GB, SDXL)
- **Seed:** 42 (mismo seed que baseline SD 1.5 A-01/A-02 para comparativa directa)
- **Config SDXL:** steps=35, cfg=4, sampler=dpmpp_2m, scheduler=karras, res=1216Ã—832
- **Flags AMD 8GB:** `--lowvram --cpu-vae --directml 0 --force-fp16 --disable-cuda-malloc`
- **Tiempo:** 561.86s (~9.3 min) en LOW_VRAM mode
- **Output:** `estadio_sdxl_juggernaut_00001_.png` â†’ copiado a `proyectos/MVP_04-comfyui-arquitectura/n_01-txt2img/WF-estadio/salidas/n_01-D-01.png`
- **DocumentaciÃ³n actualizada:** `01-index.md`, `02-WF-log-WFestadio.md`, `PLANS/comparativa-sd15-vs-sdxl.md`, `log.md`
- **Comparativa SD 1.5 vs SDXL:** Primer punto de datos (seed 42) completado para decisiÃ³n migraciÃ³n

## 2026-07-24 â€” Lanzamiento de ComfyUI

- **Servidor ComfyUI iniciado**: Lanzamiento del backend de generaciÃ³n de imÃ¡genes local con GPU AMD RX 570 de 8GB optimizado mediante DirectML y FP16 (`corre_comfyui.bat`) para su uso en el vault.

## 2026-07-19 â€” n_03-controlnet v1.1x: scribble test + DA3 bug + bug log & output log

- **v1.1a.1 interior prompt**: v1.1a_02 revelÃ³ que el prompt exterior (`grandstands, stadium bowl, pitch`) ignoraba la composiciÃ³n del croquis (vista interior del estadio). Fix: prompt reorientado a interior (`stadium interior view, looking up from the pitch, rows of empty seats, steel roof structure overhead`) + strength 0.85 + end 0.85. Backup `BAK_v1.1a.0__scribble.json` creado. Documentado en [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/workflow_log-n_03_WF01|workflow_log-n_03_WF01]]
- **v1.1a scribble test**: Primera corrida `n_03-v1.1a-scribble-01` con ControlNet Scribble directo sobre croquis (~90s)
- **B-002 DA3Inference**: Bug `missing required positional argument: 'mode'` detectado en v1.1b Dual Canny+Depth. SoluciÃ³n: seleccionar `mono` en el widget mode del nodo DA3Inference. Documentado en [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]]
- **bug_log-WF_v1.1x.md dividido**: Ahora hay bug_log separado por workflow: [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1a_scribble|bug_log-WF_v1.1a_scribble]] (v1.1a Scribble) y [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]] (v1.1b Dual). El archivo original quedÃ³ como stub de redirecciÃ³n.
- **output_log-n_03-WF01.md creado**: CatÃ¡logo de todos los outputs organizado por versiÃ³n (1.0, 1.1a, 1.1b) con tabla de parÃ¡metros, outputs y evaluaciones. Prefijos internos: 1.0-index, 1.0-outputs, 1.1a-index, 1.1a-outputs, 1.1b-index, 1.1b-outputs
- **index-n_03_WF01.md actualizado**: Nuevos enlaces a output_log y bug_log

## 2026-06-28

- **CreaciÃ³n del vault**: Estructura inicial creada basada en vault-lidia (Pitautech), adaptada para estudio de arquitectura.
- **Archivos creados**: AGENTS.md, .gitignore, index.md, log.md
- **Directorios**: proyectos/, activos/, bims/, wiki/, legal/, finanzas/, hr/, marketing/, scripts/
- **Template de proyecto**: creado en proyectos/template/

## 2026-06-28 â€” SesiÃ³n con Sol

- **Contexto corregido en AGENTS.md**: PasÃ³ de "estudio internacional multi-oficina" a **contexto argentino real**: oficina en Argentina, equipo remoto nacional, planos como documentos legales (incumbencia profesional Ley 24.335), realidad de obra con papel y celular.
- **ReestructuraciÃ³n profunda del vault**: Se eliminaron todas las carpetas sobrantes de la raÃ­z (`bims/`, `legal/`, `finanzas/`, `hr/`, `marketing/`) y se moviÃ³ su contenido al `wiki/`. La raÃ­z ahora tiene solo: `wiki/`, `proyectos/`, `activos/`, `scripts/`.
- **Nuevo wiki**: 8 secciones â€” practica-profesional, legal, finanzas, estandares (con subsecciones tecnico/ y oficina/), software, estudio, clientes, lecciones-aprendidas. TODO el conocimiento del estudio vive dentro de `wiki/`.
- **`wiki/oficina/` renombrada a `wiki/estudio/`** para evitar confusiÃ³n con `wiki/estandares/oficina/`. `estudio/` contiene escala de decisiones, roles, procedimientos, IT, RRHH.
- **Se eliminÃ³ contenido genÃ©rico internacional** (impuestos UK/DK, GDPR, etc.) y se reemplazÃ³ con contenido especÃ­fico argentino (CPAU, Ley 24.335, IVA/IIBB/Ganancias, cÃ³digos municipales).
- **Perfil de Sol confirmado**: Arquitecta argentina y consultora de IA. Busca centralizar, digitalizar y modernizar la operaciÃ³n del estudio.
- **VisiÃ³n â€” captura desde obra**: Pipeline telÃ©fono/tablet â†’ activos/ â†’ transcripciÃ³n â†’ .md estructurado. Digitalizar el libro de obra en tiempo real.
- **Objetivo de producto**: El vault diseÃ±ado para ser replicable en otros estudios (3ros interesados). Se documentarÃ¡ la metodologÃ­a en `wiki/estudio/metodologia-vault.md` como manual del producto.
- **InvestigaciÃ³n BIM**: Se creÃ³ `wiki/estandares/tecnico/bim-metodologia.md` con investigaciÃ³n completa sobre metodologÃ­a BIM internacional: ISO 19650 (incluyendo revisiÃ³n 2026), LOD Specification 2025, CDE, dimensiones BIM, roles, estÃ¡ndares, recursos multimedia (YouTube, podcasts), thought leaders, y referencias oficiales citadas. GenÃ©rico, sin marca.
- **Movido a wiki/software/**: La pÃ¡gina de metodologÃ­a BIM se moviÃ³ de `estandares/tecnico/` a `software/` por ser mÃ¡s afÃ­n a filosofÃ­a/herramienta que a estÃ¡ndar tÃ©cnico. Se agregÃ³ secciÃ³n "FilosofÃ­a y metodologÃ­a" en el Ã­ndice de software.
- **Secciones aÃ±adidas a bim-metodologia.md**: CDE en la prÃ¡ctica (vault como CDE), y BIM accesible para Argentina (alternativas a Revit: BricsCAD, ArchiCAD, FreeCAD, Blender; CDE sin suscripciÃ³n cloud; flujo hÃ­brido CADâ†’BIM recomendado para estudio ARG).
- **InvestigaciÃ³n IA en estudios internacionales**: Se creÃ³ `wiki/software/ia-arquitectura-estudios-internacionales.md` con investigaciÃ³n detallada sobre cÃ³mo ZHA, BIG, MVRDV, Foster + Partners, UNStudio, Gensler y otros integran IA en sus flujos. Incluye herramientas (Midjourney, Stable Diffusion, D5 Render, NVIDIA Omniverse, CarbonSpace), unidades internas de IA, proyectos destacados (Terminus AI City, IPAI Campus, CODE), fuentes citadas, thought leaders y recursos multimedia.
- **Archivo movido**: `decision-arquitectura-trabajo-ia-privacidad.md` â†’ `wiki/estudio/decision-arquitectura-ia-privacidad.md` (estaba suelto en raÃ­z).
- **activos/ vaciado**: Se eliminaron todos los subdirectorios de plantilla dentro de `activos/`. Cada estudio lo completa segÃºn su estructura.


- **2026-10-08** - Pipeline de curacion YouTube+Chrome: Takeout parseado (157 canales, 709 videos, 434 marcadores) en doc unico raw/yt/videos-y-canales-guardados.md, con titulos/canal/duracion via YouTube Data API v3 (646 de 655, 14 unidades de cuota). Scripts yt_titles.py + yt_takeout_parser.py con notas didacticas. Guia de API key + metodologia + template de briefing semanal. 6 bugs resueltos: encoding con tildes del Takeout, headers de CSV, sufijos -videos, pipes que rompen tablas markdown, tags por substring, contexto de carpeta.

- **2026-10-08 (cont.)** - Tags ampliados en yt_takeout_parser.py: 8 tags nuevos (3dsmax, video-ia, audio-ia, opencode, remotion, dibujo, gestion, whatsapp) + stemming de plurales + filtro de fechas + 7 categorias amplias con columna Cat y SLUG_CAT. Efecto: sin-clasificar 157->131; ia-agentes-code 196, software-arq 134, ia-imagen 124. Verificado 709/709 filas OK.

- **2026-10-08 (cont.)** - Archivo de revision manual: nuevo scripts/yt_revision.py genera raw/yt/revision-manual.md (300 lineas) con SOLO lo pendiente: 131 WL sin-clasificar + 113 canales fuera, con columnas para veredicto. Dos modos: editar en Obsidian o pasar numeros en el chat.

- **2026-10-08 (cont.)** - Veredictos 1-60 dictados: filosofia 13, otros 22, rescatar 21, descartar 3, proyecto 1 (+MAGNIFIC WL#135 = 61 en veredictos.json). Tags nuevos: decentraland, tecnologia, architettura, ia suelto. sin-clasificar 131->51. Filosofia/personal = listados no analizados. Backfill de veredictos en revision-manual. Sigue desde #61.

- **2026-10-08 (cont.)** - Veredictos 61-131: rescatar 19, otros 46, descartar 8 (total 132 en veredictos.json). Tags: gaussian-splatting, gemma, herramienta, cerebro-digital, d5. sin-clasificar fuera del top-20. Backfill revision-manual completo 1-131. 3 conflictos para confirmar (120 TEDx, 121 arq-tech, 110 IA en buckets personal).

- **2026-10-08 (cont.)** - Creadores con WL: nuevo scripts/yt_creadores.py genera raw/yt/creadores.md (151 canales distintos en WL, 101 NO suscriptos, con veredicto agregado). Verificado 151 filas OK, 0 mojibake.

- **2026-10-08 (cont.)** - Veredictos Parte 2: 47 canales rescatados (arq+IA 14, software 16, IA 5, construccion 4, creadores 3, estudios 1, metaverso 4 nueva). Scope 44->91, fuera 113->66. Registro en canales-veredictos.json conciliado exacto. Backfill 47 filas. Bugs: tedeschi/ted, especialista 3d, pixeleasel.

- **2026-10-08 (cont.)** - Borrado raw/yt/revision-manual.md (revision completa). Veredictos preservados: 132 videos + 47 canales en JSONs.

- **2026-10-08 (cont.)** - Veredictos Parte B (15 revit, 16 comfyui, 22/29 charlas reconfirmados, 80 dibujo): los 5 ya estaban bien, se fijaron en veredictos.json (135 total). Regenerados doc + creadores.

- **2026-10-09** - Indice unico wiki/fuentes/index-yt.md (3 vistas, piloto comfyui 71 videos, script yt_build_index.py, estado en index-state.json). Primer @contenidos: RAMs89SS6cM (img2img Flux Kontext, transcript parcial declarado, gate s/N pendiente). Fila marcada procesada en el indice.

- **2026-10-09** - Instalado en comfyenv (con s): yt-dlp 2026.08.19 + faster-whisper 1.2.1 (mismas versiones que stack pitauOS). Invocar yt-dlp via `python -m yt_dlp` (Scripts no esta en PATH). Pendiente: scripts/transcribir_youtube.py + primera corrida (RAMs89SS6cM).
