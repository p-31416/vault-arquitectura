# Resumen — Flujo SET_01 Cuadro carpinterías (OS-Emilia)

> Workflow `SET_01 Cuadro carpinterias a Sheets` (`VIQmMEZ9tkDBfKjd`) · Activo · 12 nodos · Webhook `POST /set01-carpinterias` · Verificado 2026-10-16 vía MCP · Doc operativo v1 (2026-10-16)

## Qué hace

Pipe CAD → planilla viva: recibe el cuadro de carpinterías extraído del plano y lo escribe en el Google Sheet `SET_01-REP-carpinterias`, creándolo y ubicándolo en `W03-CAD` si aún no existe.

## Cadena

```
Recibe cuadro (webhook POST /set01-carpinterias)
→ Busca planilla (Drive search SET_01-REP-carpinterias) → Existe planilla (IF)
├─ existe → Limpia hoja → Arma matriz → Escribe rango (PUT .../cuadro!A1:H100)
└─ nueva → Crea planilla (es_AR, hoja cuadro) → Busca carpeta W03-CAD → Mueve a carpeta
           → Limpia hoja nueva → Arma matriz nueva → Escribe rango nueva
```

Matriz de 8 columnas: `categoria,bloque,tipo_id,ancho_m,altura_m,alfeizar,descripcion,cantidad`. Re-posteable sin duplicados (limpia antes de escribir). Producción: `https://n8n.pitau.tech/webhook/set01-carpinterias`. Verificado 13/10: 56 celdas.

## Cómo contribuye

Cierra el loop MVP_02: del bloque con medida en AutoCAD al cómputo en planilla sin re-tipear. Base del EXTRACDAT de obra. Detalle del lado CAD: `presentacion/dashboard-autocad.html`.

## Credenciales que usa

Google Drive + Sheets `ppi-EmiliaOS_*` (webhook sin auth: solo recibe el POST del pipeline CAD).

## Tiempo que ahorra

Cuadro de 42 carpinterías en ~1 min vs tipeo manual + errores a obra. Ahorro logueado del SET: 12-15 h por plano.

## Cotización

Módulo planilla viva: cotiza con el SET_01 CAD (ver dashboard AutoCAD). Reutilizable por tipo de plano en Mes 2.
