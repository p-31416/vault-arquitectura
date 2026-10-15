---
tipo: log
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-09-07
tags: [log, historico]
---

# Log de operaciones

Más nuevo → más arriba

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
