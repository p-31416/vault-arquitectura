# audita-dwg-com.py — Notas didacticas

Auditoria DWG via **COM directo** contra AutoCAD abierto. A diferencia de `audita-dwg.py` (ezdxf, no requiere AutoCAD, pero no lee DWG nativo sin ODA), este script habla con la sesion AutoCAD abierta y puede leer TODO el model space sin timeout.

## Como correrlo

```powershell
py -3 scripts\audita-dwg-com.py
```

Requisitos:
- AutoCAD completo (no LT) abierto con un dibujo activo.
- El paquete `pywin32` (ya viene en el venv de `autocad-mcp`).
- Si no esta: `& "P:/00-repos/proyecto-pi/tools/autocad-mcp/.venv/Scripts/python.exe" -m pip install pywin32`.

## Que hace

1. `win32com.client.GetObject(Class="AutoCAD.Application")` agarra la sesion COM viva.
2. Toma `doc.ActiveDocument` (no abre ni guarda nada).
3. Lee variables (`INSUNITS`, `EXTMIN`, `EXTMAX`) — las mismas que expusieron las tools del MCP.
4. Itera `doc.Layouts`, `doc.Layers`, `doc.Blocks` (filtrando `*Model_Space` y `*Paper_Space`).
5. Itera `doc.ModelSpace` entidad por entidad, contando por tipo (mapeo `ObjectName` → nombre legible: `AcDbPolyline` → `POLYLINE`, `AcDbBlockReference` → `INSERT`, etc).
6. Captura muestra de textos (`TEXT`) e inserts (`INSERT`) para entender que dice el plano.
7. Compara contra `SPEC_LAYERS` (las 22 del SET_01) y reporta delta.
8. Escribe `raw/reports/audit-<stem>.json` + `.md`.

## Diferencia con audita-dwg.py

| | ezdxf (`audita-dwg.py`) | COM directo (`audita-dwg-com.py`) |
|---|---|---|
| Requiere AutoCAD abierto | No | **Si** |
| Lee DWG nativo | Solo con ODA File Converter instalado | **Si** |
| Walk de model space | Lento, limitado por `max_scan` | Completo, sin tope |
| Bloques definidos | Si, via `doc.blocks` | Si, via `doc.Blocks` |
| Hace cambios | No (solo lectura) | Podria (este script solo lee) |

## Cuando usar cada uno

- **`audita-dwg.py`:** auditoria offline / sin AutoCAD / scripts CI. Necesita ODA en sistema.
- **`audita-dwg-com.py`:** auditoria interactiva con AutoCAD abierto. Sin tope de entidades.

## Extensiones futuras

- Salida a `raw/reports/<fecha>-audit-<stem>.md` con timestamp (hoy usa `<stem>`).
- Capturar screenshot via `acad.ActiveDocument.Window...` o via la herramienta del MCP `autocad`.
- Volcar entidades con sus coordenadas para analisis posterior.
