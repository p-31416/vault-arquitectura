# Notas de `leantime_registrar_horas.py` — registrar horas en Leantime

## Qué resuelve

El vault tiene el flujo `Fathom → specs/ → Leantime`, pero **registrar las horas trabajadas no estaba resuelto**: el MCP de Leantime expone 0 tools y no había ningún método de "time tracking" documentado. Este script lo resuelve con la API JSON-RPC.

## El método (leído del código de Leantime, no de memoria)

Fuente: `app/Domain/Timesheets/Services/Timesheets.php` (repo `Leantime/Leantime`).

```
logTime(int $ticketId, array $params): array|bool
```

| `$params` | obligatorio | qué es |
|---|---|---|
| `dateString` | sí (o `date`+`time`, o `timestamp`) | fecha y hora del trabajo |
| `hours` | sí | número de horas (decimales OK) |
| `kind` | sí | tipo de hora: `GENERAL`, `GENERAL_BILLABLE`, `GENERAL_NOT_BILLABLE`, `PROJECTMANAGEMENT`, `DEVELOPMENT`, `BUGFIXING_NOT_BILLABLE`, `TESTING` |
| `description` | no | texto libre |
| `userId` | no | si el token **no** tiene permiso `timesheets.manage`, el server lo fuerza al usuario de la sesión (nosotros: Sol, `userId 3`) |

Otros métodos de la misma clase, útiles:

| Método | Para qué |
|---|---|
| `getAll(dateFrom, dateTo, ...)` | leer las entradas de un rango |
| `upsertTime(ticketId, params)` | **upsert**: si ya hay entrada para ese ticket+fecha+tipo, actualiza las horas en vez de sumar |
| `deleteTime(id)` | rollback: borrar una entrada |
| `getLoggedHoursForTicketByDate(ticketId)` | horas de una tarjeta por día |
| `getBookedHourTypes()` | el vocabulario de `kind` |

## Las dos trampas que costaron una corrección

### 1. La fecha se desplaza 7 horas por RPC

La instancia corre en **UTC+7**; la UI manda la hora local, el RPC no. Medido:

| `dateString` enviado | `workDate` con que se lee |
|---|---|
| `2026-10-19 12:00:00` | `2026-10-19 19:00:00` ← **este es el que hay que mandar** |
| `2026-10-19 00:00:00` | `2026-10-19 07:00:00` |
| `2026-10-19 19:00:00` | `2026-10-20 02:00:00` ← un día después (el error que cometí) |

Las 15 entradas previas del estudio se leen a las `19:00:00` (fin de jornada). Para llegar a eso por RPC hay que mandar **12:00:00**.

### 2. Dos entradas del mismo ticket+fecha+tipo se fusionan

`logTime` **suma** las horas a la fila existente en vez de crear otra, y concatena las descripciones con un separador `--`. O sea: 2 entradas de 1 h del mismo ticket el mismo día → **1 fila de 2 h con las dos descripciones**. No es un bug: es cómo funciona `addTime`. Está bien para el uso del estudio (una fila por tarjeta por día), pero conviene saberlo antes de cargar.

## Cómo se ejecuta

```powershell
# ver qué se va a cargar, sin escribir nada
P:\Anaconda\envs\comfyenv\python.exe scripts\leantime_registrar_horas.py --dry

# cargar de verdad
P:\Anaconda\envs\comfyenv\python.exe scripts\leantime_registrar_horas.py

# releer las entradas
P:\Anaconda\envs\comfyenv\python.exe scripts\leantime_registrar_horas.py --verificar

# rollback: borrar entradas por id
P:\Anaconda\envs\comfyenv\python.exe scripts\leantime_registrar_horas.py --borrar 51,53
```

## Las entradas que se cargaron el 2026-10-20

Reparto pedido por Sol: 1 h por área por día + 1 h extra de reparto el lunes → **3 h por tema** (lunes 2 h + martes 1 h). Más la reunión con Emilia del miércoles.

| Día | Tarjeta | Área | Horas |
|---|---|---|---|
| 19/10 | `452` Estandares CAD DWT-layers-bloques-rotulos (p4) | cad | 2 |
| 19/10 | `517` Sistema de procesamiento de libros (p4) | fuentes | 2 |
| 19/10 | `571` Flujo Rhino + ComfyUI con estilo propio (p6) | rhino | 2 |
| 19/10 | `448` 8-8 Fathom en raw-reuniones + ficha-sem Emilia (p4) | agentes | 2 |
| 20/10 | `452` | cad | 1 |
| 20/10 | `517` | fuentes | 1 |
| 20/10 | `571` | rhino | 1 |
| 20/10 | `504` Clonar agente + subflujo de agenda con perfil Emilia (p4) | agentes | 1 |
| 21/10 | `533` Cita presencial miercoles 21/10 13:00 (p4) | reunión con Emilia | 3 |

**Total 15 h.** `kind: "GENERAL"` (como las 15 entradas previas).

### Pendiente de rotular

Las 4 h extra del lunes quedaron con la descripción **"Extra lunes 19/10 - 1 h por tema"** porque el rótulo original ("mtb") no se pudo identificar: ni está en el vault, ni en Leantime, y el propio Sol no lo reconhecer. Cuando se sepa qué era, se edita la descripción en la UI de Leantime (o con `updateTime`).

## Límites

- La API tira **429** (límite por minuto) → `scripts/leantime_rpc.py` ya espera 20 s y reintenta.
- Los **Goals** de Leantime no están expuestos por la API (se crean a mano en la UI).
- No hay forma de registrar horas **sin** una tarjeta: `ticketId` es obligatorio.
