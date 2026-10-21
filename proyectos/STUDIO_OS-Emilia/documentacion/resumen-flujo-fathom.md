# Resumen — Flujo Fathom Core (OS-Emilia)

> Workflow `OS-Emilia — Fathom Core` (`UeDkqVZSeLnae5cF`) · Activo · 13 nodos · Cron 07:00 AR + a pedido (`/sync`, Agent Voz) · Versión activa `ffd071f6` (09/10) · Verificado 2026-10-16 vía MCP · Doc operativo v2

## Qué hace

Trae reuniones de Fathom (API, últimas 26 h, con transcript+resumen+action items), clasifica internas vs clientes (por lados emilia/proyectopi/externo, con `[revisar]-` si no hay señal), arma `.md` + Google Doc formateado y los guarda en Drive (`Reuniones-Internas` / `Reuniones-Clientes`). Idempotente en vault por `recording_id`/`call_id`.

## Cadena

```
Cron 07:00 AR (o /sync, o Tool Fathom del Voz) → Fetch Fathom Meetings (26 h)
→ Split → Build Meeting Document (nombre `fecha_slug_recordingid.md`)
→ Build Google Docs Requests (formato) → Classify (clientes/internas)
→ Save .md Drive → Create Google Doc → Move → Apply Formatting
```

Timezone del workflow: `America/Argentina/Buenos_Aires`. Cron con success diario incl. 16/10 (execs 3564→3772, 26 totales).

## Credenciales que usa

Fathom Header Auth `ppi-EmiliaOS_Fathom` · Google Drive `ppi-EmiliaOS_Google Drive` · Google Docs · (Caveat vigente: sin dedup por `recording_id` en corridas manuales — Drive puede acumular copias; el import al vault es inmune).

## Tiempo que ahorra

| Tarea | Manual | Auto | Ahorro |
|---|---|---|---|
| Por reunión (transcribir, formatear, clasificar, subir) | ~15–20 min | ~1 min (exec 3489: 8 reuniones success) | ~15 min c/u |
| Métrica n8n declarada | — | `timeSavedPerExecution: 5` | 5 min/exec |

Ejemplo: 5 reuniones/sem → ~1,2 h/sem ≈ 5 h/mes (ficha cierre: 45 min × 11/mes ≈ 8 h/mes).

## Cotización

Módulo Fathom → Drive + Doc: **USD 60** de referencia (propuesta partnership, incluido). Ahorro que entrega: ~8 h/mes.

## Total automatizaciones (las 3)

Inbox ~8 h/mes + Voz ~4 h/mes + Fathom ~5 h/mes ≈ **17 h/mes** (~4 h/semana) con cotas conservadoras. Método: `(t_manual − t_auto) × N`, con `N` contado en Sheet/ejecuciones; re-medir 1 semana con contador por flujo.
