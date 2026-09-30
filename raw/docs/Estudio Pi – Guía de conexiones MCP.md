# Guía de conexiones MCP: Claude Code, Codex y OpenCode → AutoCAD y Autodesk
Estudio Pi · 27/09/2026 · Pensado para tu PC con Windows

---

## 1. Resumen: qué se puede conectar hoy

| Servidor | Qué hace | Tipo | Lo mantiene | Claude Code | Codex | OpenCode |
|---|---|---|---|---|---|---|
| Autodesk Product Help | Busca en la ayuda oficial (110+ productos, varios idiomas) | Remoto (HTTP) | Autodesk (oficial) | Sí | Sí | Sí |
| AutoCAD and Civil 3D MCP | Lee y analiza el dibujo abierto | Interno de AutoCAD | Autodesk (oficial) | No (solo Autodesk Assistant) | No | No |
| autocad-mcp (puran-water) | Dibuja en AutoCAD LT 2024+ vía AutoLISP, o genera DXF sin AutoCAD | Local (stdio) | Comunidad | Sí | Sí | Sí |
| autocad-mcp (limuzi013) | Controla AutoCAD 2026 completo vía COM | Local (stdio) | Comunidad | Sí | Sí | Sí |
| Revit Public MCP | Lectura/escritura del modelo Revit 2027.2 | Local (stdio) | Autodesk (tech preview) | Sí | Sí | Sí |
| Fusion MCP / Fusion Data MCP | Modelado en vivo / datos en la nube | Local / Remoto | Autodesk | Sí | Sí | Sí |

Los tres clientes hablan el mismo protocolo, así que cualquier servidor stdio o HTTP funciona en los tres. Solo cambia el formato de la configuración. Los servidores que no son de Autodesk no aparecen documentados para estos tres clientes, pero la configuración es estándar.

---

## 2. Cómo se configura cada cliente

| | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Archivo de config | `~/.claude.json` (local/usuario) o `.mcp.json` en la raíz del proyecto | `~/.codex/config.toml` (global) o `.codex/config.toml` (proyecto de confianza) | `opencode.json` / `opencode.jsonc`, bajo la clave `mcp` |
| Agregar remoto (HTTP) | `claude mcp add --transport http <nombre> <url>` | `codex mcp add <nombre> --url <url>` | `"type": "remote", "url": "..."` |
| Agregar local (stdio) | `claude mcp add --transport stdio <nombre> -- <comando> [args]` | `codex mcp add <nombre> -- <comando>` | `"type": "local", "command": ["...", "..."]` |
| Login OAuth | `/mcp` o `claude mcp login <nombre>` | `codex mcp login <nombre>` | `opencode mcp auth <nombre>` |
| Ver servidores | `/mcp` | `codex mcp list` | `opencode mcp list` |
| Diagnóstico | `/mcp` | `codex mcp --help` | `opencode mcp debug <nombre>` |
| Timeouts | — | `startup_timeout_sec` (10 s), `tool_timeout_sec` (60 s) | `timeout` en ms (5000 por defecto) |
| Limitar herramientas | permisos de Claude Code | `enabled_tools`, `disabled_tools`, `default_tools_approval_mode` | `tools` global o por agente |

Fuentes: [Claude Code – MCP](https://code.claude.com/docs/en/mcp) · [Codex – MCP](https://developers.openai.com/codex/mcp) · [OpenCode – MCP servers](https://opencode.ai/docs/mcp-servers/)

Detalles que suelen fallar:
- En Claude Code, el `--` separa las opciones de Claude del comando del servidor. Sin el `--`, Claude interpreta como propios flags del servidor como `--port`. Si en un JSON ponés `url` sin `type`, Claude Code toma la entrada como stdio y la saltea.
- En los archivos de configuración de Windows, las barras de las rutas van dobles en JSON (`C:\\ruta`). En TOML conviene usar comillas simples (`'C:\ruta'`) para que las barras no se interpreten.

---

## 3. Configuraciones listas para copiar

### 3.1 Autodesk Product Help (el primero que conviene conectar)
- Endpoint: `https://developer.api.autodesk.com/knowledge/public/v1/mcp` (Streamable HTTP).
- La [documentación oficial](https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html) lo marca como público y sin autenticación. Algunos directorios mencionan OAuth: si el cliente te pide login, se abre el navegador y listo.
- Herramientas: `get_available_products`, `search_help_content` (por palabra clave, producto, versión e idioma; por ejemplo `es_ES`).

Claude Code:
```bash
claude mcp add --transport http --scope user autodesk-help https://developer.api.autodesk.com/knowledge/public/v1/mcp
```
Codex:
```bash
codex mcp add autodesk-help --url https://developer.api.autodesk.com/knowledge/public/v1/mcp
```
OpenCode (`opencode.json`):
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "autodesk-help": {
      "type": "remote",
      "url": "https://developer.api.autodesk.com/knowledge/public/v1/mcp",
      "enabled": true
    }
  }
}
```
Prueba: "Listá los productos disponibles" y después "Buscá en la ayuda de AutoCAD 2026 en es_ES cómo crear un bloque dinámico con estados de visibilidad".

### 3.2 autocad-mcp de puran-water (AutoCAD LT 2024+ o sin AutoCAD)
- Dos backends ([repo](https://github.com/puran-water/autocad-mcp)):
  - File IPC: necesita Windows 10/11, AutoCAD LT 2024 o superior y Python 3.10+ nativo de Windows (no WSL). Se comunica con AutoCAD a través de un archivo LISP.
  - ezdxf: genera archivos DXF sin tener AutoCAD instalado, en cualquier sistema operativo.
- Instalación: `git clone https://github.com/puran-water/autocad-mcp.git`, después `cd autocad-mcp` y `uv sync`.
- En AutoCAD, ejecutá `APPLOAD` → `lisp-code/mcp_dispatch.lsp`. Conviene agregarlo al Startup Suite.
- Variable `AUTOCAD_MCP_BACKEND`: `auto` (usa File IPC y, si no hay AutoCAD, ezdxf), `file_ipc` o `ezdxf`.
- Ojo: permite ejecutar AutoLISP libre. Es muy potente, pero puede modificar cualquier cosa, así que trabajá sobre copias.

Claude Code:
```bash
claude mcp add --transport stdio --env AUTOCAD_MCP_BACKEND=auto autocad-lt -- C:\ruta\autocad-mcp\.venv\Scripts\python.exe -m autocad_mcp
```
Codex (`~/.codex/config.toml`):
```toml
[mcp_servers.autocad-lt]
command = 'C:\ruta\autocad-mcp\.venv\Scripts\python.exe'
args = ["-m", "autocad_mcp"]
startup_timeout_sec = 20
default_tools_approval_mode = "prompt"

[mcp_servers.autocad-lt.env]
AUTOCAD_MCP_BACKEND = "auto"
```
OpenCode:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "autocad-lt": {
      "type": "local",
      "command": ["C:\\ruta\\autocad-mcp\\.venv\\Scripts\\python.exe", "-m", "autocad_mcp"],
      "environment": { "AUTOCAD_MCP_BACKEND": "auto" },
      "timeout": 20000
    }
  }
}
```

### 3.3 autocad-mcp de limuzi013 (AutoCAD 2026 completo, vía COM)
- Requiere Windows, AutoCAD 2026 completo (no LT) abierto con un dibujo activo, y Python 3.10+ ([ficha](https://glama.ai/mcp/servers/Slacker-LLC/autocad-mcp/tree)).
- Herramientas: capas, líneas, polilíneas, arcos, texto, cotas lineales, inserción de bloques, mover/copiar/borrar, guardar DWG/DXF y captura de pantalla.
- Es más seguro: no tiene un comando libre y solo guarda archivos dentro de una carpeta que vos definís (`ACAD_MCP_OUTPUT_ROOT`).
- No incluye sombreados, impresión, xrefs ni sólidos 3D.
- Instalación: `git clone https://github.com/limuzi013/autocad-mcp.git`, crear el entorno con `py -3 -m venv .venv` e instalar con `.venv\Scripts\python.exe -m pip install .`.

Codex (según la documentación del propio repo):
```toml
[mcp_servers.autocad-mcp]
command = 'C:\ruta\.venv\Scripts\autocad-mcp.exe'

[mcp_servers.autocad-mcp.env]
ACAD_MCP_OUTPUT_ROOT = 'C:\EstudioPi\salidas'
```
Claude Code:
```bash
claude mcp add --transport stdio --env ACAD_MCP_OUTPUT_ROOT=C:\EstudioPi\salidas autocad -- C:\ruta\.venv\Scripts\autocad-mcp.exe
```
OpenCode:
```json
"autocad": {
  "type": "local",
  "command": ["C:\\ruta\\.venv\\Scripts\\autocad-mcp.exe"],
  "environment": { "ACAD_MCP_OUTPUT_ROOT": "C:\\EstudioPi\\salidas" }
}
```
Prueba: pedile al agente que llame a `autocad_status` con AutoCAD abierto.

### 3.4 Para más adelante (BIM y fabricación)
- Revit Public MCP (tech preview): solo funciona con Revit 2027.2 y el add-on instalado, con un modelo abierto. Hay tres variantes: Read, Write y Experimental. Autodesk documenta la configuración para Claude Desktop y Cursor ([setup](https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_RevitMcp_setting_up_revit_mcp_server_html)), y el mismo ejecutable stdio se puede usar en los tres clientes:
  `C:\Program Files\Autodesk\Revit 2027 MCP Server Read-Tools Technical Preview\Autodesk.RevitMcpServer.Stdio.exe` con el argumento `--ManageConfigurationWithAutodeskRevitPluginInstaller=true`.
- Fusion: el MCP local se activa en Preferences > General > API y permite modelar en vivo. El Fusion Data MCP es remoto y usa login con OAuth ([Fusion MCPs](https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW)). Es muy útil para el curso de 3D, impresión y CNC.

---

## 4. Qué combinación te conviene

| Escenario | Combinación |
|---|---|
| Aprender y preparar clases | Product Help + tus manuales en una carpeta Markdown (el agente los lee como archivos) |
| Tenés AutoCAD LT 2024+ | Product Help + puran-water (File IPC) |
| Tenés AutoCAD 2026 completo | Product Help + limuzi013 (COM), más la verificación de estándares (DWS) dentro de AutoCAD |
| No querés depender de la licencia (cuenta de estudiante) | puran-water en modo `ezdxf`: el agente genera DXF (bloques, carátulas, planillas) sin abrir AutoCAD, y vos los abrís y revisás después |
| Pasar a BIM / fabricación | Revit MCP 2027.2 / Fusion MCP |

Qué cliente elegir:
- Claude Code: el más simple para empezar. Se configura con un comando y tiene el panel `/mcp`.
- Codex: el que más controla la seguridad. Permite elegir qué herramientas se habilitan y pedir aprobación antes de cada acción (`default_tools_approval_mode = "prompt"`). Además comparte la misma configuración con la app de escritorio y la extensión del IDE.
- OpenCode: open source y permite usar distintos modelos. Sirve para comparar costos entre proveedores, y tiene el comando `opencode mcp debug` para diagnosticar.

---

## 5. Buenas prácticas de seguridad
1. Trabajá siempre sobre copias del DWG y con una carpeta de salida dedicada.
2. Activá la aprobación manual de herramientas, sobre todo con servidores que ejecutan LISP.
3. Revisá el código de los MCP comunitarios antes de instalarlos: no son oficiales.
4. Poné la configuración en el proyecto (`.mcp.json` o `.codex/config.toml`) solo si la querés compartir; nunca guardes claves ahí.

## 6. Próximo paso sugerido
Hacé una prueba de 1 hora en tu PC: (1) conectá Product Help en Claude Code; (2) instalá puran-water en modo `ezdxf` y pedile al agente "creá un DXF con las capas del Kit Estudio Pi y un bloque de puerta de 0,80 m"; (3) abrí el DXF en AutoCAD y revisalo.
