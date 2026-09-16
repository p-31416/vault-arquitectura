# Nivel 05: Rhino MCP — Conexión en Tiempo Real

## Objetivo (futuro)

Conectar Rhino + Grasshopper con ComfyUI vía MCP para un loop de diseño en tiempo real: el arquitecto modela en Rhino, el render se actualiza automáticamente en ComfyUI, y las iteraciones vuelven al modelo.

## Arquitectura propuesta

```
[Rhino 3D] ←→ [Grasshopper] ←→ [Rhino MCP Server] ←→ [Opencode] ←→ [ComfyUI MCP]
                 │                                                    │
                 ▼                                                    ▼
           Export depth map                                    Render + feedback
           Export normal map                                   visual al arquitecto
           Export wireframe
```

## Componentes necesarios

1. **Rhino MCP Server** — Exponer vistas, geometría y depth maps de Rhino como MCP tools
2. **Grasshopper definition** — Exportar depth/normal/wireframe automáticamente
3. **ComfyUI workflow** — ControlNet Depth + Normal para renderizar sobre la geometría exacta
4. **Loop de iteración** — Cambio en Rhino → re-render automático

## Casos de uso

- Modelar un volumen en Rhino y verlo renderizado al instante
- Mover una ventana en Rhino y que el render se actualice
- Probar 10 variantes de material desde Opencode sin tocar Rhino

## Pendiente

- [ ] Investigar Rhino MCP servers existentes (grasshopper-mcp)
- [ ] Definir protocolo de datos (qué exportar de Rhino)
- [ ] Workflow ControlNet con depth maps en tiempo real
- [ ] Prueba de concepto con geometría simple
