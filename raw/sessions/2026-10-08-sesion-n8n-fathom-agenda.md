---
tipo: log
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [sesion, n8n, fathom, cal-com, telegram, drive, studio-os, emilia]
---

# Sesión 2026-10-08 — Loop Fathom→Drive→vault + Agenda Cal.com real

Más nuevo → más arriba

## Resumen

Jornada completa en n8n (instancia `n8n.pitau.tech`, carpeta OS-Emilia): se terminó y verificó end-to-end el loop de reuniones (Fathom→Drive→vault→análisis) y se reescribió la Agenda sin mock (Telegram→Cal.com con reserva real). Todo verificado por API vía MCP `n8n-mcp`. Quedó pendiente de Sol: cancelar la reserva de prueba en cal.com/bookings y la limpieza de duplicados en Drive.

## n8n + Fathom (mañana/tarde)

- **Publicados y activos (5/5 OS-Emilia):** Fathom Core (`UeDkqVZSeLnae5cF`), Format Google Doc (`LysH41yu1s5wXkPz`), Fathom Cron 07:00, Telegram Router (`YWpuV5p0vCDTbIHz`), Agenda mock (`UTkII2kd3RHDlizo`). Después: merge a canvas único (Cron+Format absorbidos y archivados) y Agenda reescrita.
- **Credenciales:** Drive + Docs OAuth reconectados por Sol en n8n UI (estaban expirados desde el 24/09); Sheets reconectada más tarde. Fathom Emilia y Telegram `emiliaospi_bot` ya cableados.
- **Fixes verificados:** `jsonBody` con objeto crudo → serializado; wiring `Restore → Move → Apply` (referencia por nombre); `folderId` faltante (`.gdoc` caían en raíz); nombres opción A `fecha_participantes_recid`; canvas único con pairing `$('Classify Meeting').item` (MergeBack con Code descartados: pairing inestable en Code); `created_after −26h` en el Fetch (fin de duplicados); timezone workflow a `America/Argentina/Buenos_Aires`.
- **Filtro por lados:** clasificación por unión invitados + hablantes del transcript + `recorded_by` mapeados a emilia/proyectopi/externo. Solo emilia+proyectopi → internas; externo → clientes; cero señal → internas + `[revisar]-`. Las 2 del 03/10 (vinícola, Leticia+Vanessa) a Clientes; 6 a Internas. `calendar_invitees_domains_type` de Fathom no es confiable; `shared_with` no trae mails.
- **Import vault:** nuevo `scripts/import_drive_reuniones.py` (+ notas): Drive Stream → `raw/reuniones/YYYY-MM-DD-<call_id>.md`, idempotente. 8 reuniones adentro.
- **Análisis:** `@fathom-pm` vía task no corre en este entorno (free tier); análisis del 827502057 hecho inline como propuesta.

## Agenda Cal.com (noche)

- **Reescritura sin mock:** parseo `/agendar DD/MM[/AA] HH:MM Nombre [emails]` (año implícito, AR→UTC, validaciones) → email en mensaje o lookup en `clientes-contactos`/`clientes` (hoja creada por Sol desde `clientes.csv`) → reserva real evento 7109200 (30 min) → confirmación Telegram con Ref.
- **Hallazgo:** IFs creados por API no evalúan (rama 0 siempre, test y producción); migrados los 4 a Switch v3.4 como el Router. Canvas reordenado.
- **Verificación producción:** `/agendar 09/10 15:00 Sol` → hoja resolvió email → reserva `gnCrXcR1j3mz8Hd9THXhyh` accepted + confirmación Telegram. **Pendiente:** Sol cancela en cal.com/bookings.
- **Pendiente mañana (reunión con Emilia):** crear evento 60 min con Google Meet en Cal.com (no se puede por API) y pasarme el eventTypeId para swap.

## Documentos

- Nuevo `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md` (v1.2, técnico nodo por nodo) y `playbook-os-emilia-n8n.md` v1.0 (manual para Emilia, para presentar el 09/10).
- Log: entradas (1)–(10) del 2026-10-08.

## Archivos modificados

- n8n: `UeDkqVZSeLnae5cF` (canvas único + lados + `created_after` + timezone), `UTkII2kd3RHDlizo` (agenda real + Switches), archivados `2gUlVXu7xk1Jd12s` + `LysH41yu1s5wXkPz`. Router intacto.
- Vault: `scripts/import_drive_reuniones.py`, `scripts/import_drive_reuniones_notas.md`, `raw/reuniones/` (8 archivos + `.import-state.json`), `proyectos/STUDIO_OS-Emilia/documentacion/{arquitectura-n8n-os-emilia.md,playbook-os-emilia-n8n.md,clientes.csv}`, `log.md`, planes en `raw/brainstorm/b-2026-10-08-{handover-mes1,vault-web-drive-ingest}.md`.

## Análisis cerebro-digital

### Topics

- Loop reuniones end-to-end operativo (Fathom→Drive→vault) con clasificación por lados y sin duplicados.
- Agenda por Telegram con reserva real verificada; IF-vs-Switch como lección de la instancia n8n.
- Documentación doble: técnica (equipo) + manual (Emilia) para la reunión del 09/10.

### Entidades

- `OS-Emilia` (5→3 workflows activos), `clientes-contactos` (hoja), evento Cal.com 7109200 (30 min; 60 min + Meet pendiente), `@emiliaospi_bot`, `raw/reuniones/` (8), `chat_id` 8459099332 (Sol testeando; NO usar como filtro — el filtro será el de Emilia).

### Hechos

- Execs clave: 3489/3495/3500/3503 (Fathom success), 3505 (lote vacío con filtro fecha), 3525 (reserva real `gnCrXcR1j3mz8Hd9THXhyh`).
- Cal.com no tocado salvo lectura; Drive reconectado por Sol; Sheets reconectado por Sol; YouTube quedó en pausa (sin credential, solo doc).
- Pendientes de Sol: cancelar reserva prueba, limpiar duplicados Drive, crear evento 60 min + Meet con Emilia.
