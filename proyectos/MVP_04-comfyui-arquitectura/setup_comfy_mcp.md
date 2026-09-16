---
tipo: playbook
mvp: 04
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, mcp, setup, comfyui]
---

# Configuración del MCP de ComfyUI para Opencode

Este documento detalla cómo levantar y orquestar el servidor MCP para ComfyUI de forma local, asegurando la privacidad de la propiedad intelectual del estudio.

## Prerrequisitos

- **ComfyUI Local:** Instalado y corriendo (por defecto en `http://127.0.0.1:8188`).
- **Node.js:** Necesario para ejecutar el servidor MCP.
- **Opencode:** El agente en la terminal de Antigravity.

## Instalación del Servidor MCP

Se utiliza el paquete oficial de MCP de ComfyUI que permita la ejecución e interrogación de flujos de trabajo localmente.

### Paso 1: Configurar el archivo MCP de Opencode

Opencode (y Antigravity) configuran sus servidores MCP mediante archivos JSON en `.gemini/antigravity-ide/mcp/` o la configuración propia de la terminal.

Debemos registrar un nuevo servidor MCP apuntando al script de ejecución de ComfyUI. 
El comando principal a usar a través de `npx` (ejemplo oficial):

```json
{
  "mcpServers": {
    "comfyui-mcp": {
      "command": "npx",
      "args": ["-y", "@comfyorg/comfyui-mcp"],
      "env": {
        "COMFYUI_URL": "http://127.0.0.1:8188"
      }
    }
  }
}
```

### Paso 2: Habilitación en Opencode

1. Con ComfyUI corriendo localmente en el puerto 8188.
2. Iniciar la sesión de Opencode. El agente detectará el MCP de ComfyUI disponible.
3. El agente podrá listar herramientas como `run_workflow` conectándose a tu máquina.

## Principio AMV aplicado

No hay scripts sueltos ni diagramas. La validación de que esta integración funciona es ejecutar el MCP y lograr un `run_workflow` exitoso inyectando un `.json` local.
