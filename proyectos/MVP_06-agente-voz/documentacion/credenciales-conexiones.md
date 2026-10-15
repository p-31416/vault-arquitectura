---
tipo: documentacion
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [documentacion, mvp_06, credenciales, n8n, mantenimiento]
---

# Credenciales y conexiones — Agente de voz (mantenimiento)

> Regla dura: los secretos viven solo en credenciales n8n cifradas. Nunca en repos, workflows, mensajes, logs ni capturas. En docs solo nombres e IDs públicos.

## Matriz

| Credencial n8n | Tipo | Usada en | Mantenimiento |
|---|---|---|---|
| Allowlist `chat_id` Sol `8459099332` | ID de chat Telegram (no es secreto, es config) | Auth allowlist TEST | Confirmado 2026-10-13 vía execs del Router; el de Emilia se agrega en M4 con su `/start` |
| `emiliaospi_bot-Telegram account` | Telegram API (token BotFather) | Trigger + envíos + file:get del TEST | Rotar solo si se expone; tras rotar, reconectar nodos y reactivar webhook |
| `Cal.com API Key` (Sol) | Bearer Cal.com v2 | Tools Agenda + Agenda-leer TEST | Revisar vigencia trimestral; `cal-api-version: 2024-08-13` en headers |
| `ppi-EmiliaOS_Cal.com` (Emilia, M4) | Bearer Cal.com v2 | Perfil Emilia | Idem; evento `7109200` (+60min+Meet tras reunión) |
| `ppi-EmiliaOS_Fathom` / key Sol | Header `X-Api-Key` | Fetch Fathom + tool Sync | Una por cuenta Fathom; verificar `GET /meetings` 200 con `limit=1` |
| `ppi-EmiliaOS_Google Drive` / Drive Sol | OAuth2 Drive | Save `.md` en carpetas perfil | **Expira**: reconectar en n8n UI si un exec falla en Save (caso 08/10) |
| `Google Docs account` | OAuth2 Docs | Create Doc + Apply formato | Idem Drive, misma reconexión |
| `ppi-EmiliaOS_Google Sheets` / Sheets Sol | OAuth2 Sheets | Lookup `clientes` por perfil | Columnas obligatorias `nombre,email,activo`; solo filas activas |
| `OpenRouter account` | OpenRouter API | Agent chat + HTTP STT pago | Vigilar saldo + `usage.cost` por mensaje; `max_price` como techo |
| `Redis account` | Redis | Batch `studio_os_ID` | Sin mantenimiento;TTL implícito por delete tras agregar |
| `Postgres account` | Postgres | Memory `sessionKey=chat.id` | Vigilar tamaño tabla de memoria; backup con el VPS |
| Data Table `OS-Bot-Profiles` | n8n Data Table | Perfiles sol/emilia | Backup antes de cada cambio; 1 fila por usuario |

## Cadencia

* **Mensual 15 min:** abrir n8n → verificar conexiones OAuth (Drive/Docs/Sheets) → saldo OpenRouter → 1 mensaje de prueba voz + 1 texto → revisar execs con error.
* **Ante fallo Save/Transcribe/Agent:** este doc dice qué credencial tocar antes de culpar al flujo.
* **Auditoría:** cada booking deja `Ref uid`; cada STT deja `usage.cost`; cada sync deja conteo por carpeta.
