---
tipo: log
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [log, mvp_06, agente-voz, bitacora]
---

# 03-log-mvp_06 — Bitácora

Más nuevo → más arriba

## 2026-10-13 — Workflow TEST creado en n8n para revisión

* Loteo Redis OK con 6 fragmentos (execs 3691-3696: 5 obsoletas + 1 combinada). Bug intermitente -3h en listado vivo; fix REGLA HORAS (no doble conversión) + solo accepted cuentan.

* Sábado sin slots: schedule Working hours Lun-Vie 9-17 (id `2495785`), evento sin schedule propio. Google primario conectado+seleccionado (bloquea). Prompt con horario real. Diagnóstico vía n8n (egress local bloqueado por Cloudflare 1010); temporal archivado.

* Sábado 17/10 sin slots en todo el día (exec 3674): ofrecimiento previo sin validar. Fix REGLA OFRECER en padre (solo proponer validado). Diagnóstico API pendiente: `.env` sin key.

* Bug invitado: sub-agente copió host en vez de ficha (exec 3663/3664, booking `3VfX...` mal + canceló la real `xbZ7...` con autorización). Fix REGLA FICHA + aviso sin-recurrencia-API. Reparado exec 3667: hoy 13:00 180min online con Emilia (`i2pF...`).

* Ciclo completo probado 2026-10-14 (execs 3645/3647/3648/3649/3650/3651): slots viernes OK → alta online 30min (`qxPj...`) → reprogramación directa sin chequeo (REGLA MODIFICAR OK, nuevo uid `hafn...`) → cambio duración vía cancelar+reagendar 60min (`q2uV...`, REGLA DURACION) → cancelación limpia. Listado final: solo vigente la real de Emilia (`xbZ7...`).

* REGLA MODIFICAR: reprogramar va directo a `actualizar_reunion` sin chequeo previo; solo ante conflicto real se consultan slots ignorando el bloque propio. Publicado.

* Key propia `ppi_calcom-Bearer Auth account` en las 6 tools. Exec con filtro trae la reserva `xbZ7...` (Emilia, 14/10 13h, evento `7467793`): lectura + escritura verificadas punta a punta, revisión dual con Ref.

* Lecturas vacías con filtro (`totalItems 0`): la key actual no alcanza los bookings del evento `7467793`. Escritura sí pasa (reservar es acción pública sobre el evento; el host lo pone el evento). Falta API key de la cuenta proyectopi-31416 para lecturas.

* El bot no encuentra la reunión porque la API no la lista: o es evento manual de Google Calendar (sin UID, imposible por Cal.com) o vive bajo otra identidad Cal.com que la key. Test decisorio: URL del booking en UI (¿tiene UID?) vs evento manual.

* Exec 3626: API lista solo 20 viejos (ago-sep, eventos `6690467`/`6966557`); nada de octubre ni del evento `7467793`. Lo que se ve en `/bookings/upcoming` está bajo otra identidad Cal.com que la API key: pedir UID de la URL del booking para comparar.

* Exec 3619: Cal.com sigue con los mismos 20 bookings viejos (cero del bot). El mail de confirmación vino de Google Calendar (evento manual), no de Cal.com: revisar remitente. El agente ahora reporta el evento a las 10:00, no 13:00.

* Exec 3615/3618: ningún booking nuestro persiste en Cal.com (el Ref citado no existe en la API). Duraciones ampliadas a 30/60/180 en tools + prompt. Buffers: se configuran por evento en Cal.com, pestaña Limits & buffers (Before/After, 5–120 min).

* Exec 3618: ningún intento de escritura llegó a Cal.com (lista completa sin uid `xbZ7...` ni evento `7467793`); el evento 13:00 de Google Calendar no lo creó el bot. El Ref citado no existe: no usarlo. Duración 3h excede el máximo 60 del evento.

* Exec 3608: el evento sigue aceptando solo `integration` (la ubicación custom no entró como tipo API) → `agendar_presencial` pasa dirección en texto plano (vía de compatibilidad que LidIA usaba y funciona). Publicado, pendiente reintento.

* Sol habilitó ubicación custom-attendee en el evento `7467793`. Si el tipo mapea a `attendeeDefined`, la tool actual pasa; si el 400 vuelve con otro tipo permitido, se ajusta el payload. Pendiente reintento.

* Exec 3605 (presencial Emilia 14/10 13h): cadena perfecta (planilla→email, slots→libre, agendar_presencial con params exactos) pero Cal.com 400: el evento `7467793` solo admite location `integration`; falta habilitar dirección en el evento. Día bien dicho (miércoles 14).

* Mantenimiento `OS-Studio — Limpiar Memoria TEST` (`uOonS1LWzowvwyns`, en la carpeta, inactivo): borra sesión Postgres `8459099332` + key Redis del TEST. Espejo acotado de `LidIA_Postgres`.

* Exec 3593: el agente no llamó a la planilla (0 tools, siguió el hilo viejo pidiendo email) → REGLA 1 en prompt: buscar_contacto primero siempre, sin excepción. Publicado.

* "No encontré a Emilia": el filtro exacto no matcheó "Emilia Pimenta" vs "Emilia Pimenta Lombardi" → `buscar_contacto` ahora devuelve planilla completa y el agente matchea tolerante (mayúsculas/acentos/parcial). Publicado.

* Exec 3588 con Luna: "Jueves 15/10: 14:00 a 15:30 — Natacha cad (Google Calendar)", tildes OK, ambas fuentes consultadas. Día + encoding corregidos.

* Cred `Google Calendar account` creada por Sol → `leer_calendario` activado con calendario primario y publicado. Exec 3582: revisión dual OK, encontró "Natacha cad" 15/10 14-15:30 de Google Calendar. Detalle: dijo miércoles, el 15/10 es jueves (slip menor del LLM).

* `leer_calendario` existe en el subflujo pero quedó desactivado (gris): `primary` no resuelve sin credencial válida y trababa el publish. Se publica el resto; se reactiva al crear `proyectopi-Calendar`.

* Revisión ciega a Google Calendar: `obtener_reuniones` solo ve bookings Cal.com (los 20 listados son del evento LidIA 6690467); la reunión del jueves de Sol está creada a mano en Google Calendar. Fix: tool `leer_calendario` (cred `pitau.tech_Calendar`, calendario `primary`) + prompt dual con dedup por fecha+título. Bloqueante: esa credencial está vencida, reconectar en n8n UI.

* Modelo principal → `openai/gpt-5.6-luna` (slug verificado en docs OpenRouter, tools + tool_choice OK, ~$0.40/mes a este volumen). Publicado. Subflujo sigue en free.

* Exec 3572: lote fragmentado + modelo devolvió vacío → Telegram 400. Fix: fallback anti-vacío en Responder + publicado (`dbdaae70`). Si el floor repite vacíos, se pasa a Luna.

* Exec 3570 con versión vieja publicada (modelo free + sin sheet tools) → publicado el borrador actual (`97ddbbc9`: flash-lite floor + anti-razonamiento + 4 tools). Re-probar.

* Modelos: free falló (exec 3570) → `gemini-2.5-flash-lite:floor` en principal. Comparativa: a este volumen (~30 turnos/día) todos salen <$1/mes, así que decide fiabilidad+español, no precio. Fallback elegido: GPT-5.6 Luna (stack probado de LidIA) antes que DeepSeek (más barato pero harness nuevo + routing mixto).

* Exec 3570: el modelo free (`openrouter/free`) devolvió su razonamiento en inglés sin llamar tools → swap a `gemini-2.5-flash-lite:floor` ($0.10/M) + prompt anti-razonamiento en el principal. Subflujo sigue en free (pasó sus tests).

* eventTypeId `7467793` activo: prompt + `lengthInMinutes` + desdoble `agendar_online`/`agendar_presencial` (`attendeeDefined`). Tests solo-lectura OK: exec 3567 listar (20 reuniones, respuesta correcta) y exec 3568 slots con ID real (mañana 10–11 sin lugar; agent resolvió fecha e ID bien, 3.4s, sin errores). Pendiente: escritura real + Telegram cred + ventana voz.

* Auditoría de cuentas (pedido Sol): en Proyecto Pi = Cal.com API Key (5 tools), OpenRouter, Redis, Postgres (tabla `studio_os_test`), Gemini STT. Compartido/genérico pendiente = 3 nodos Telegram con cred genérica (cambiar a `emiliaospi_bot`). Lado Emilia = planilla `clientes-contactos` (decisión Sol) + Fathom Core (key + carpetas OS-Emilia: no disparar sync en pruebas).

* Reparto conserje/ejecutor: contactos al principal (`buscar_contacto` movido + `agregar_contacto` nueva con append y verificación de duplicado, prompt con flujo buscar→agregar→ficha completa); subflujo ejecutor puro (sin planilla, exige ficha completa, sin `location` en payload = videollamada default del evento). Email siempre obligatorio; presenciales con dirección después.

* Limpieza instancia (pedido Sol): archivados `LidIA_Eval_Extractor_5.2.0` y `LidIA Test Pipeline v5.1` por MCP. `LidIA WEB` y `prospeccion-Lidia` no disponibles en MCP (`availableInMCP:false`): archivar a mano en UI. `LidIA_Postgres` se conserva activo.

* Planilla: Sol asoció `clientes-contactos` real al tool (se descarta la copia `clientes-sol-test`); al reasociar se cayó el filtro y se repuso (`nombre` = `$fromAI`, `returnAllMatches`). Decisión registrada en spec §1.
* Memoria del sub-agente: se mantiene Simple Memory por ejecución (patrón LidIA); la conversación vive en el Postgres del Agent Voz.
* Tool `buscar_contacto` agregada al subflujo (lookup `nombre` → email en planilla, cred Sheets EmiliaOS): el agente busca email en planilla antes de pedirlo. Apunta a `clientes-sol-test` pendiente de crear.
* Patrón corregido a subflujo con agente adentro (modelo `w8iMJ01WGCSxvSMg`): el Agent Voz ya no automatiza la reserva con tools directas.
* Nuevo `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`, 10 nodos, inactivo): trigger `query` → agente + memoria por ejecución + 5 tools Cal.com con tu `Cal.com API Key`; `eventTypeId 0` fail-closed hasta cargar tu eventTypeId real (solo lectura funciona).
* TEST reconfigurado (24 nodos): salen Tool Agendar/Cancelar/Modificar, entra 1 Tool Agenda → subflujo; queda Tool Fathom. Prompt del agente actualizado.

* Creado `OS-Studio — Agent Voz TEST (revision)` (`Gpd6NHB4HQdU7ary`, 26 nodos, inactivo): Trigger con allowlist `8459099332` a nivel `chatIds` → Detectar → Tipos audio/texto/callback → STT Gemini → W01/W02 → Redis batch 12s → Agent `openrouter/free` + Postgres `studio_os_test` + 4 tools (Agenda/Cancel/Modif/Fathom Cores) → respuesta.
* n8n autoasignó `Telegram account` genérica en los 3 nodos Telegram: cambiar a `emiliaospi_bot-Telegram account` antes de probar.
* NO activar: roba el webhook al Router de producción. Revisión solo en canvas + execs manuales.
* Límite conocido: los tools escriben en el Cal.com de Emilia hasta cablear tu `eventTypeId`; pruebas vivas solo en modo lista (`/cancel`).

## 2026-10-13 — chat_id Sol confirmado y documentado

* `chat_id` Sol con `os.emi-pi`: `8459099332` (vía execs del Router). Registrado en spec §3 (tabla perfiles + nodo Auth) y en matriz de credenciales como allowlist TEST. Falta el de Emilia (su `/start`, M4).

## 2026-10-13 — Spec v2: valor, agenda-leer, docs, tasks pomodoro

* Se agrega §2 propuesta de valor (contactos catalogados, datos propios, revisión de agenda, por qué IA vs comandos) + ADR revisar-agenda con `tool Agenda-leer`.
* Normas n8n fijadas: normalizadores W01+W02, Redis batch, Switch v3.4.
* Nuevos `documentacion/manual-uso-agente-voz.md` + `documentacion/credenciales-conexiones.md` + §7 operativa.
* TASKS detalladas por pomodoro para trabajar con `@fathom-pm` → Leantime.

## 2026-10-13 — Creación del proyecto

* Se crea `MVP_06-agente-voz` como proyecto propio, separado de Studio OS Emilia (decisión [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|ADR-2026-10-13-proyecto-propio-mvp_06]]).
* Spec canónica única en `01-spec-mvp_06.md`; antecedente [[specs/261013-agente-voz-telegram-os|spec 261013]] pasa a superado.
* Pendiente: infra Sol (`OS-Sol`, hoja copia, `eventTypeId`, fila perfiles) + construcción TEST.
