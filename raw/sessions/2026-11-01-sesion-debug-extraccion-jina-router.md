---
tipo: log
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [sesion, n8n, telegram-router, jina-reader, api-key, error-handling]
---

# 2026-11-01 — Router Emilia: por qué fallaba la extracción Jina y quedó reparada con API key + ack que avisa

Más nuevo → más arriba · auditado solo lectura durante plan mode (grep de convenios + ejemplo canónico `raw/sessions/2026-10-28-sesion-loras-comfyui-locales.md`)

## Qué se hizo

- **Diagnóstico de la extracción fallida** (exec **3960** del flujo **OS-Emilia — Telegram Router**, `YWpuV5p0vCDTbIHz`): lectura completa de la ejecución vía MCP. El flujo terminó en `status: success` pero el nodo `Extrae Jina` recibió **403 de `r.jina.ai`** — `AbuseAlleviationError (40305)`: *"Anonymous access to domain www.instagram.com blocked until Sun Nov 01 2026 04:19:38 GMT due to previous abuse... DDoS attack suspected: Too many requests"*. No era la config del trigger ni del Sheet: Jina Reader **anónimo** se trackea por IP con rate-limit compartido (20 RPM) y otros usuarios ya habían abusado del dominio instagram.com desde esa IP compartida del server.
- **La cadena del daño**: `Extrae Jina` tiene `onError: continueRegularOutput` → el error siguió el flujo sin fallar → `Parsea Info` no encontró contenido → `titulo: ""` y `tags: ""` → `Append Fuentes Sheet2` **sí escribió la fila** (link/tipo/fecha/de completos, Título y Tags vacíos) → `Ack Fuente Guardada` mandó "Anotado ✓ IG" igual, dando falsa sensación de éxito.
- **Fix 1 — ack que avisa**: expresión nueva en `Ack Fuente Guardada` (edit vía `updateNodeParameters`): si `$('Parsea Info').item.json.titulo` viene vacío, el mensaje suma `⚠️ Jina no extrajo el contenido — completá título y tags a mano`.
- **Fix 2 — API key de Jina**: el estudio creó la key en `https://jina.ai/api-dashboard/key-manager` (login Google/GitHub, nuevas cuentas arrancan con 10M tokens gratis) y se registró como credencial n8n `Jina Reader API Key` (tipo `httpHeaderAuth`, Header `Authorization: Bearer jina_...`). Conexión al nodo: primero `authentication: genericCredentialType` + `genericAuthType: httpHeaderAuth` vía `updateNodeParameters`, después `setNodeCredential`. Beneficio: pasa de **20 RPM anónimas a 500 RPM por key** y la IP deja de ser penalizada por abuso ajeno. Se descartó la vía `.env` local: el flujo corre en el server de n8n y el `.env` del repo jamás lo alcanza.
- **Agrupado visual del canvas** (deuda `[pre-existing] TOP_LEVEL_ITEMS_OVER_CEILING`: 13 cajas vs techo 7) vía `setNodeGroups` — 3 grupos aplicados: **Identidad** (Route Identidad + ST Identidad + ST Entrada) · **Inbox Fuentes** (Has Link → Prepara Fila → Extrae Jina → Parsea Info → Append Fuentes Sheet2 → Ack Fuente Guardada + ST Inbox) · **Agente Voz** (Run Voz Agent). El grupo **Comandos legacy** (Route Telegram Command → Run Fathom Sync + Send Help) fue **rechazado por el server**: gate con 2 salidas externas viola la regla de 1 entrada/1 salida. Total: 13 → 8 cajas.
- **Dos publicaciones** (`publish_workflow`): `7f889b6d` (ack + key) y `e4a475f8` (agrupado final); el flujo quedó activo con la versión agrupada.

## Verificación

- **Test real del studio** (2 links al grupo `os.emi-fuentes`): execs **3962/3963** en `success`. Chequeo con datos reales de la 3962 (discourse.mcneel.com, tipo WEB): título completo — *"Learning to build thin shells using kangaroo, guidance required - Grasshopper - McNeel Forum"* — y **6 tags** (`learning, build, thin, shells, using, kangaroo`). La extracción funciona con la key; el estudio confirmó que ambos mensajes llegaron bien.

## Hallazgos

- **`onError: continueRegularOutput` convierte un fallo de datos en un fallo silencioso**: el sheet recibe la fila igual (metadatos del mensaje: autoría/fecha/tipo/link son previos a la extracción), así que el error solo se ve en las celdas vacías de Título/Tags. El aviso en el ack repara la visibilidad de punta a punta.
- **El régimen anónimo de Jina es un recurso colectivo, no propio**: el bloqueo llegó etiquetado como sospecha de DDoS (`DDoS attack suspected`) por abuso de terceros — el contraste del tiempo de respuesta lo confirma: 3,1 s anónimo vs 37 ms con key.
- **El MCP `setNodeCredential` sobre un HTTP Request exige previa de auth**: subir la credencial sin `authentication + genericAuthType` devuelve primero "does not accept credential 'httpHeaderAuth'" (engañoso; el schema del nodo sí la acepta en `HttpRequestV45Credentials`) y después "credentialName: Required" (el op exige los tres campos: id + key + name).
- **Node groups: un gate no se puede agrupar**: `Route Telegram Command` y `Route Fuentes Group` tienen 2 salidas externas (regla de 1 entrada/1 salida), y agrupar sus ramas muertas por separado da dos micro-grupos de 1 nodo sin ganancia real. Más adelante, si el router se parte en 2 flujos conectados por `Execute Sub-workflow`, los Comandos sí podrán agruparse (entrada/salida limpia).
- **El contador de cajas del warning pesa las sticky notes**: el trigger `Recibo Mensaje` queda fuera del conteo (los triggers están prohibidos en grupos) pero los stickies sí cuentan como cajas; con 3 grupos el total bajó de 13 a 8 sobre techo 7, y el warning se marca `[pre-existing]` como deuda admisible.

## Archivos

**En el vault (nuevo)**

- `raw/sessions/2026-11-01-sesion-debug-extraccion-jina-router.md` (este archivo)
- `log.md` (entrada del 01/11 arriba + frontmatter al día)

**Fuera del vault (n8n cloud, `https://n8n.pitau.tech`)**

- Flujo `YWpuV5p0vCDTbIHz` **OS-Emilia — Telegram Router**: versión activa nueva `e4a475f8` (agrupado; antes `7f889b6d` con ack + key)
- Credencial nueva `Jina Reader API Key` — id **`O9nflrVfOBg4VGI1`** (httpHeaderAuth, `Authorization: Bearer jina_...`), proyecto personal PI

## Estado y qué sigue

- **Deuda menor 1** — Completar filas antiguas del Sheet `Fuentes-Inbox` con Título/Tags vacíos (execs ~3957–3970): a mano o re-mandando el link al bot (re-ingesta completa). Requiere `s`.
- **Deuda menor 2** — Cajas del canvas: 8 vs 7, tolerancia justificada (los 4 sueltos son gates/ramas muertas que las reglas de conectividad prohíben agrupar). El split del router en 2 flujos (comandos ↔ resto) lo cierra a futuro.
- **Radical opcional** — Fallback de extractor si Jina vuelve a fallar con otro dominio (llamada B de la propuesta original: un segundo reader en la cadena o el scrape directo). Con la key el bloqueo de dominio desaparece, así que se aplaza sin riesgo inmediato.

## Análisis cerebro-digital

**Topics:** jina-reader-api-key · rate-limits-anonimo · abuse-alleviation-error · error-handling-n8n · continue-regular-output · ack-telegram · node-groups-sdk · conectividad-1-entrada-1-salida · canvas-agrupado · telegram-router-emilia · google-sheets-append · header-auth-credencial

**Entidades:** `OS-Emilia — Telegram Router` (n8n `YWpuV5p0vCDTbIHz`, 17 nodos, activo) · credencial `Jina Reader API Key` (`O9nflrVfOBg4VGI1`) · `jina.ai/api-dashboard/key-manager` (portal de keys) · execs **3960** (debug, 03:27) · **3962/3963** (test OK, 16:13-16:14) - doc de Google Sheets `Fuentes-Inbox` (docId `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI`) · dos builds publicadas `7f889b6d` y `e4a475f8` · token bot `emiliaospi_bot` · grupo `-5417177870` (os.emi-fuentes)

**Hechos:**
- Jina Reader anónimo: 20 RPM trackeadas por IP con penalización *por dominio objetivo* (instagram bloqueado hasta las 04:19 GMT del 01/11 por abuso colectivo); con API key: 500 RPM trackeadas por key y sin bloqueos de dominio anónimo.
- El 403 Jina entra igual de silencioso por `onError: continueRegularOutput`, y el sheet recibe la fila con metadatos completos pero Título/Tags vacíos — el punto único de detección existe y es el ack (ya con alerta).
- Para asignar una credencial httpHeaderAuth a un HTTP Request vía MCP hacen falta 3 campos (id + key + name) y la previa de `authentication: genericCredentialType` + `genericAuthType: httpHeaderAuth`; sin la previa el mensaje de error es engañoso ("does not accept credential").
- Las reglas de node groups del SDK rechazan gates con 2 salidas externas y ramas muertas sueltas — el fix estructural para agrupar `Comandos` es partir el router en 2 flujos unidos por Sub-workflow.
- Nueva key gratuita de Jina arranca con 10M tokens; la key no expira y los tokens quedan en la cuenta, no en la key.
