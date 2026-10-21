# Onboarding Emilia al agente de voz — 1 agente, N perfiles

> Fecha: 2026-10-16 · Proyecto: `MVP_06-agente-voz` · Relacionado: Router v2 (`Route Identidad`), `specs/261013-plan-fuentes-emilia-inbox.md`

## 1. ¿Uno o dos agentes? UNO con perfiles

Un solo `Agente Voz TEST` atiende a ambos. Lo que cambia por persona NO es el agente (prompt, memoria, herramientas) sino el **perfil**: `{ chat_id, cal_cred, eventTypeId, hoja_clientes, drive, fathom_cred }`. La memoria ya separa por `sessionKey = chat.id`; el Redis batch ya usa key por chat.

Por qué no duplicar: dos agentes = doble prompt que mantener, doble costo LLM, doble memoria que diverge. El único punto donde n8n obliga a ramificar es la **credencial** (no admite expresiones): cada llamada externa existe 2 veces (una por cred) con un Switch por perfil delante. Eso ya existe en la práctica: Cores prod (Emilia) vs TEST (Sol).

## 2. Matriz de perfiles

| Dato | Sol (TEST, hoy) | Emilia (prod, mañana) | Estado |
|---|---|---|---|
| `chat_id` | `8459099332` | pendiente (leer de ejecución cuando entre al grupo) | MAÑANA |
| Cal.com Bearer | `Cal.com API Key` (`zdNucNjAM21guAuR`) | `ppi-EmiliaOS_Cal.com` (`3MvZXPNH8LrDYPZS`) | existe |
| Cal.com eventTypeId | pendiente (fail-closed hoy) | `7109200` (30 min, Meet) | existe |
| Hoja clientes | `clientes-sol-test` (crear copia) | `clientes-contactos` (`1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`) | existe |
| Drive | `OS-Sol` (crear + 2 subcarpetas) | `OS-Emilia` (existe) | crear Sol |
| Fathom | key Sol o team (`recorded_by` Sol) | `ppi-EmiliaOS_Fathom` | existe |
| Google Sheets OAuth | — | `ppi-EmiliaOS_Google Sheets` (`yb1G3uAHS2QqK1wu`) | **RECONECTAR** |
| Telegram | mismo bot `emiliaospi_bot` | mismo bot | ok |
| Postgres memoria | tabla `studio_os_test`, `sessionKey=chat.id` | misma tabla, separa solo | ok |
| Redis batch | key `studio_os_test_<chat>` | misma, separa solo | ok |
| Modelo | OpenRouter free (`gpt-5.6-luna`) | mismo | ok |

## 3. Cambios para activar el perfil Emilia (sin duplicar flujos)

1. **Router**: regla `chat_id == <id Emilia>` → `Run Voz Agent` con `profile: emilia` (hoy solo Sol rutea; resto cae a comandos).
2. **Subflujos agenda**: envolver cada llamada Cal.com/hoja en Switch `profile` → rama `sol` (cred Sol) / rama `emilia` (cred EmiliaOS existente). Los Cores prod de Emilia ya usan sus creds: reutilizar, no copiar.
3. **System prompt**: inyectar perfil (nombre, zona `America/Argentina/Buenos_Aires`, eventType, carpeta Drive) — 1 bloque, no 2 prompts.
4. **Regla de oro Cal.com** (incidente 2026-10-15): mover/cancelar siempre desde bot o Cal.com, nunca desde Google Calendar (huérfana el uid y el cancel rebota; el agente aborta la creación por seguridad — verificado).

## 4. Checklist reunión mañana (15 min)

- [ ] Agregar a Emilia al grupo os.emi-fuentes + que mande 1 mensaje → leer su `chat_id` de la ejecución.
- [x] Reconectar `ppi-EmiliaOS_Google Sheets` (Credentials → Reconnect) — hoy caído, traba appends y agenda.
- [ ] Setear regla Emilia en `Route Identidad` + `profile: emilia` en `Run Voz Agent`.
- [ ] Probar voz con SU voz: "agendá prueba mañana 10:00" → verificar en Cal.com → borrar la prueba.
- [ ] Crear vistas con filtro en Fuentes-Inbox (Ver Sol / Ver Emi).
