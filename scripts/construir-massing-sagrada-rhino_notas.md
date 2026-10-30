# Notas — `construir-massing-sagrada-rhino.py`

Script que se ejecuta **dentro de Rhino 8** y levanta el massing 2.5D del entorno
Sagrada desde la base open (`activos/.../earth2rhino3d/base/sagrada_overpass.json`,
ODbL, 1054 ways, 474 con `levels`).

## Cómo se usa

1. En Rhino 8, archivo nuevo en **metros**: `SF-sitio-massing-v01.3dm`.
2. En la línea de comandos (no en la terminal):

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\construir-massing-sagrada-rhino.py"
```

3. El informe sale por la línea de comandos. El script **NO guarda**.
4. Con el puente MCP levantado (`rhino-mcp-server-rhino.py`, puerto 9876),
   el asistente puede verificar con `get_scene_summary` + `BoundingBox`.

## Qué hace y por qué

| Bloque | Qué hace | Por qué importa |
|---|---|---|
| Lee Overpass JSON | footprints + nodos, sin QGIS | evita instalar QGIS para arrancar |
| `latlon_a_xy` | equirectangular alrededor del templo (41.4036, 2.1744) | error < 1 m en 600 m, suficiente para massing |
| `altura_de_tags` | `height` > `levels×3,1` > default 21 m manzana Eixample | OSM Sagrada trae 0 `height` y 474 `levels`: sin default quedaría plano |
| Capas | `SF-MASSING-OSM` + `TESTIGO-SF` (caja 60×100×172,5 m) + `SF-ORIGEN` | el templo NO se extruye de OSM: testigo propio aparte |
| Sin guardar | deja el save al arquitecto | regla del estudio en flujos 3D |

## Validación (gate humano)

- `BoundingBox` de una manzana ≈ 133 m de lado.
- Testigo mide 172,5 m (`Distance` en Z).
- Vista isométrica SE + `Zoom Extents`: el Eixample se lee en retícula con chamfers.
- Captura para el vault antes de densificar.

## Si falla

- `ERROR: no existe la base` → correr `P:\Anaconda\envs\comfyenv\python.exe scripts\descargar-osm-sagrada.py`.
- Overpass 502/429 → reintentar en 5 min (el script rota 3 endpoints).
- Rhino sin objetos → revisar que el archivo esté en metros y el script se corrió con `_RunPythonScript`.
