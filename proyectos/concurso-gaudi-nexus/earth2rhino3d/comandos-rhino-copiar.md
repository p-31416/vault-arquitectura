# Comandos Rhino — copiar y pegar

> Pegar en la **línea de comandos de Rhino 8** (no en la terminal).

## 1. Puente MCP (primero, obligatorio)

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py"
```

Mensaje esperado: `RhinoMCP script loaded. Server started automatically.`

## 2. Massing Sagrada (después del puente)

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\construir-massing-sagrada-rhino.py"
```

## 3. Verificación rápida (opcional)

```
_BoundingBox
_Distance
_Zoom _Extents
```
