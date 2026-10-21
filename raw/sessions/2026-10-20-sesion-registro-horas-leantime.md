---
tipo: log
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [leantime, horas, timesheets, pm, session]
---

# Sesión 2026-10-20 — Registro de horas trabajadas en Leantime (15 h)

## Qué se hizo

Sol pidió registrar en Leantime las horas del **lunes 19/10 (4 h)** y del **martes 20/10 (4 h)**, repartidas en cuatro áreas (**cad**, **fuentes**, **rhino**, **n8n-leantime-fathom-agentes**), más 4 h extra del lunes y la reunión de 3 h del miércoles 21/10.

Reparto final (3 h por tema: lunes 2 h + martes 1 h), **15 h en total**:

| Día | Tarjeta | Área | Horas |
|---|---|---|---|
| 19/10 | `452` Estandares CAD DWT-layers-bloques-rotulos (p4) | cad | 2 |
| 19/10 | `517` Sistema de procesamiento de libros (p4) | fuentes | 2 |
| 19/10 | `571` Flujo Rhino + ComfyUI con estilo propio (p6) | rhino | 2 |
| 19/10 | `448` 8-8 Fathom en raw-reuniones + ficha-sem Emilia (p4) | agentes | 2 |
| 20/10 | `452` / `517` / `571` / `504` | cad / fuentes / rhino / agentes | 1 c/u |
| 21/10 | `533` Cita presencial miercoles 21/10 13:00 (p4) | reunión con Emilia | 3 |

`kind: "GENERAL"` (igual que las 15 entradas previas). Verificado con relectura del timesheet: 8 h el lunes, 4 h el martes, 3 h el miércoles.

## Lo que hubo que descubrir

1. **Leantime no expone el time tracking por MCP ni por las clases conocidas**: el servicio no se llama `TimeTracking` sino **`Timesheets`** (`leantime.rpc.Timesheets.Timesheets.*`).
2. **El método es `logTime(ticketId, params)`** con `params.{dateString, hours, kind, description}`; `kind` es obligatorio y hay 7 valores (`GENERAL`, `GENERAL_BILLABLE`, `GENERAL_NOT_BILLABLE`, `PROJECTMANAGEMENT`, `DEVELOPMENT`, `BUGFIXING_NOT_BILLABLE`, `TESTING`). Rollback: `deleteTime(id)`.
3. **La fecha se desplaza 7 h por RPC** (la instancia está en UTC+7 y el RPC no convierte como la UI): para que una entrada se lea `19:00:00` hay que mandar `dateString` con `12:00:00`. Con `19:00:00` la entrada cae **un día después**. Medido con entradas de prueba (creadas y borradas).
4. **`logTime` suma en vez de crear**: misma tarjeta + misma fecha + mismo tipo → incrementa la fila existente y concatena las descripciones con `--`. Por eso el lunes quedaron 4 filas de 2 h (1 h de trabajo + 1 h extra) en vez de 8 filas de 1 h.
5. **Primer intento falló**: 9 entradas con las fechas corridas (+7 h). Se borraron con `deleteTime` (ids 36, 38, 40, 42, 44, 45, 46, 47, 48) y se recargaron con las fechas corregidas (ids 51, 53, 55, 57, 59, 60, 61, 62, 63).

## Pendiente

Las 4 h extra del lunes quedaron rotuladas **"Extra lunes 19/10 - 1 h por tema"**: el rótulo original que dio Sol ("mtb") no se pudo identificar —no está en el vault, no está en Leantime y el propio Sol no lo reconoce—, así que no se inventó un significado. Se renombra en la UI (o con `updateTime`) cuando se sepa qué era.

## Archivos del vault

- `scripts/leantime_registrar_horas.py` (nuevo) — cliente de time tracking: `--dry`, `--verificar`, `--borrar`.
- `scripts/leantime_registrar_horas_notas.md` (nuevo) — la API explicada línea por línea y las dos trampas.
- `wiki/glosario/software/leantime.md` — nueva sección "Horas — time tracking" + fila en la tabla de métodos + índice.
- `log.md` (entrada del 20/10).

## Análisis cerebro-digital

**Topics:** time tracking en Leantime, API JSON-RPC de Leantime, desfase de zona horaria en la API, imputación de horas por tarjeta, convención de fin de jornada (19:00).

**Entidades:** servicio `Timesheets` (`app/Domain/Timesheets/Services/Timesheets.php`), métodos `logTime` / `upsertTime` / `deleteTime` / `getAll` / `getBookedHourTypes` / `getLoggedHoursForTicketByDate`; tickets `452` (cad, p4), `517` (fuentes, p4), `571` (rhino, p6), `448` y `504` (agentes, p4), `533` (reunión, p4); proyectos 4 (`O.S_ARQ-Emi`) y 6 (`Proyecto Pi - Concurso Gaudi Nexus`); entradas 51-63.

**Hechos verificados:**
1. El RPC de Leantime resuelve argumentos por nombre (`{"ticketId": N, "params": {...}}`) — es lo que usa el script, con fallback a posicional.
2. La instancia corre en UTC+7 y el RPC no aplica la conversión que hace la UI: el desfase es de +7 h en las horas.
3. `logTime` upserta por ticket+fecha+tipo: nunca duplica, suma.
4. El `kind` "GENERAL" de las 15 entradas previas está fuera del vocabulario actual de la UI (que ofrece `GENERAL_BILLABLE`, `GENERAL_NOT_BILLABLE`, `PROJECTMANAGEMENT`, `DEVELOPMENT`, `BUGFIXING_NOT_BILLABLE`, `TESTING`); se mantuvo "GENERAL" por pedido de Sol, por consistencia con el histórico.
