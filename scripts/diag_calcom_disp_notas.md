# NOTA ES: qué hace `scripts/diag_calcom_disp.py`, línea por línea

- **Cabecera (`# ...`)**: declara intención — solo lectura, sin altas ni cambios; documenta los 3 endpoints y el comando exacto para correrlo.
- **`import json, urllib.request, Path`**: solo librería estándar, nada para instalar.
- **`BASE / ENV / API`**: ubica el `.env` en la raíz del vault (un nivel arriba de `scripts/`) y fija la base de la API v2 de Cal.com.
- **`get_key()`**: lee `CAL_COM_SOL_API_KEY` del `.env`. Si está vacía, corta con mensaje (nunca imprime la key).
- **`api_get(path, key, version)`**: hace un GET con header Bearer + versión de API; si hay error HTTP, muestra código y cuerpo recortado en vez de romper.
- **`main()` paso 1**: pide el evento `7467793` e imprime slug, duraciones y `scheduleId` (qué horario laboral usa).
- **`main()` paso 2**: con ese `scheduleId`, pide el schedule e imprime días (0=domingo…6=sábado) y franjas horarias.
- **`main()` paso 3**: pide `selected-calendars` — la lista que SÍ bloquea slots (distinto de "conectados").
- **`if __name__ ...`**: punto de entrada estándar para correrlo como script.

## Cómo leer el resultado

- Si el schedule no lista el día `6` → el sábado está apagado en Cal.com: ningún slot de sábado existirá jamás, aunque Google Calendar esté libre.
- Si `selected-calendars` no incluye tu Google → tus eventos manuales (ej. Delfi CAD) no bloquean slots aunque el calendario esté "conectado".
