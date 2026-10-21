# Rhino MCP comunitario (`reer-rhino-mcp`) — Notas de instalación y uso

Cómo quedó cableado el control de Rhino por IA en este estudio, y por qué no
usamos todavía el MCP oficial de McNeel.

---

## Por qué comunitario y no el oficial

| | McNeel Rhino MCP Platform (oficial) | `reer-rhino-mcp` (comunitario) |
|---|---|---|
| Estado | Requiere **Rhino 8.19+** (build `rh8_19`) | Funciona con **Rhino 7/8** |
| Rhino local | **8.5** (oct-2024) → incompatible | 8.5 ✓ |
| Transporte | Router stdio propio (`rhino-mcp-router.exe`) | Servidor stdio por `uvx` + socket a Rhino |
| Instalación en Rhino | Plugin Yak | Un script Python que corre dentro de Rhino |
| Herramientas | ~40 (`list_objects`, `set_camera`, `get_viewport_image`, `run_python`, `run_command`, `gh_*`…) | 7 (`get_rhino_scene_info`, `get_rhino_layers`, `execute_code`, `capture_rhino_viewport`, `get_rhino_selected_objects`, `get_rhino_objects_with_metadata`, `look_up_RhinoScriptSyntax`) |
| Licencia | MIT (McNeel) | MIT (REER, INC.) |

**Decisión de ahora**: usar el comunitario para no frenar el trabajo. **Cuando
Rhino 8 se actualice a 8.19+**, se migra al oficial (el router es más
potente: maneja crash recovery, levanta Rhino solo y expone `set_camera` /
`run_command`).

---

## Estado en esta máquina (verificado 2026-10-19)

- Rhino **8.5.24072.13001** en `C:\Program Files\Rhino 8`.
- Plugin `Rhino-MCP-Platform`: **no instalado** (no hay paquete Yak ni
  `Plug-ins\MCP`).
- Router oficial: **no existe** `%APPDATA%\McNeel\Rhinoceros\ai\bin\rhino-mcp-router.exe`.
- `uv` / `uvx`: instalados en
  `C:\Users\Solch16\AppData\Local\Programs\Python\Python312\Scripts\`.
- Paquete `reer-rhino-mcp` **v0.1.10** en PyPI (console script:
  `reer-rhino-mcp = rhino_mcp.server:main`).

---

## Puesta en marcha (3 pasos)

### 1. Script del lado Rhino

En Rhino 8: `Tools > Script > Run...` → elegir
`scripts/rhino-mcp-server-rhino.py`.

En la consola de Python de Rhino debe aparecer:

```
RhinoMCP script loaded. Server started automatically.
To stop the server, run: stop_server()
```

> **Patch local aplicado** (2026-10-19): el archivo original importa
> `rhinoscriptsyntax` de forma directa, y en Rhino 8 esa librería vive en la
> carpeta `lib` del plug-in IronPython, que no siempre está en el `sys.path`
> del motor RhinoPython 3. El bloque `PATCH LOCAL` busca esa carpeta con
> `glob` y la agrega al `sys.path` antes de reintentar el import. Si actualizás
> el archivo desde GitHub, volvé a aplicar el patch.

### 2. Servidor MCP (ya cableado)

`opencode.json` → bloque `rhino`:

```json
"rhino": {
  "type": "local",
  "command": ["C:/Users/Solch16/AppData/Local/Programs/Python/Python312/Scripts/uvx.exe", "--with", "mcp<2", "reer-rhino-mcp"],
  "enabled": true,
  "timeout": 60000
}
```

> **Por qué el `--with "mcp<2"`** (verificado 2026-10-19): sin ese pin, `uvx`
> instala `mcp` 2.x y el paquete revienta al arrancar con
> `ModuleNotFoundError: No module named 'mcp.server.fastmcp'` — en mcp 2.x
> `FastMCP` pasó a llamarse `MCPServer`. El pin resuelve `mcp` 1.x y el
> servidor levanta bien.

Con el pin, el probe devuelve las 7 tools (`initialize` + `tools/list` OK):

| Tool | Uso en el estudio |
|---|---|
| `execute_rhino_code(code)` | Correr `axonometria-militar-rhino.py` dentro de Rhino y armar el dibujo |
| `capture_rhino_viewport(layer, show_annotations, max_size)` | Traer la imagen de la vista para verificarla sin salir de la terminal |
| `get_rhino_scene_info()` | Resumen de capas y objetos (chequeo rápido del estado) |
| `get_rhino_layers()` | Listado de capas (organización del modelo) |
| `get_rhino_selected_objects()` | Qué tiene seleccionado el arquitecto ahora |
| `get_rhino_objects_with_metadata(...)` | Inventario de objetos con filtros |
| `look_up_RhinoScriptSyntax(function_name)` | Documentación de comandos Rhino desde la terminal |

> Ojo con la tool de código: su documentación dice "Rhino 7 con IronPython 2.7,
> sin f-strings". El script de la axonometría está escrito **compatible con
> ambos motores** (Python 2.7 y 3): usa `%` para formatear, sin f-strings, sin
> type hints.

### 3. Reiniciar opencode

Las tools MCP se cargan al arrancar el cliente: **cerrá y volvé a abrir
opencode** para que aparezca el server `rhino`.

---

## Herramientas disponibles y para qué usarlas

(La tabla está en el paso 2, arriba.)

## Cliente CLI: `scripts/rhino-mcp-cli.py`

Un cliente propio que habla JSON-RPC con el servidor MCP por stdio. Sirve para
operatear Rhino **desde la terminal, sin reiniciar opencode** (el server MCP
del IDE solo se carga al arrancar el cliente).

```
py -3 scripts/rhino-mcp-cli.py tools
py -3 scripts/rhino-mcp-cli.py exec scripts\axonometria-militar-rhino.py
py -3 scripts/rhino-mcp-cli.py shot salida.png 1600
py -3 scripts/rhino-mcp-cli.py execshot setup.py salida.png 1600
py -3 scripts\rhino-mcp-cli.py scene
```

`shot` acepta un 4to argumento para las anotaciones (`1` las muestra, `0` no).

## Receta: axonometría militar 30/60 con cortes (ya probada)

```
1. En Rhino: Tools > Script > Run... > scripts\rhino-mcp-server-rhino.py
   (si el puerto 9876 ya esta ocupado, se dice "Server is already running")
2. py -3 scripts\rhino-mcp-cli.py exec scripts\axonometria-militar-rhino.py
   -> log con "Angulo real sobre la horizontal: 30.00 grados"
3. py -3 scripts\rhino-mcp-cli.py shot axonometria-3d.png 1600
4. Para el dibujo 2D de frente: un snippet que ponga la vista frontal y
   después el shot (la captura usa la vista activa).
```

Salidas verificadas: `activos/mvp_05-rhino-mcp/axonometria-militar-3d.png` y
`...-2d.png`.

---

## Flujo de trabajo con la axonometría militar

```
1. El arquitecto abre Rhino con el modelo y corre el script del lado Rhino.
2. Vos: "ejecutá scripts/axonometria-militar-rhino.py en Rhino"
   -> el agente usa `execute_rhino_code` y devuelve el log (incluye la
      verificación del ángulo: debe decir 30.00 grados).
3. Vos: "capturá el viewport"
   -> el agente usa `capture_rhino_viewport` y te devuelve la imagen.
4. Si algo falla: el log del paso dice qué pasó (el script tolera fallos por
   paso, así que se ve exactamente dónde se rompe).
```

---

## Migración futura al MCP oficial

1. Actualizar Rhino 8 a **8.19+** (descargador de rhino3d.com/download).
2. `& "C:\Program Files\Rhino 8\System\Yak.exe" install Rhino-MCP-Platform`
   (o `PackageManager` dentro de Rhino).
3. Reiniciar Rhino, correr `MCPConnect` → la ventana imprime la línea de
   configuración.
4. Reemplazar el bloque `rhino` de `opencode.json` por:

```json
"rhino": {
  "type": "local",
  "command": ["C:/Users/Solch16/AppData/Roaming/McNeel/Rhinoceros/ai/bin/rhino-mcp-router.exe", "--default-version", "8"],
  "enabled": true,
  "timeout": 120000
}
```

Flags del router: `--default-version 8|9|WIP` (o `-v`), `--startup-timeout
<seg>` (default 120), `--rhino-exe 8=<ruta de Rhino.exe>`.

Docs: https://mcneel.github.io/RhinoAI/docs/

---

## Fuentes

- Paquete: https://pypi.org/project/reer-rhino-mcp/
- Repo: https://github.com/reer-ide/rhino_mcp
- MCP oficial: https://mcneel.github.io/RhinoAI/docs/
- Yak (plugin oficial): https://rhinopackages.github.io/package/Rhino-MCP-Platform
