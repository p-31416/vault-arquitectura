---
tipo: concepto
mvp: 04
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, workflow, comfyui]
---

# Workflow: Croquis a Render Vía MCP

## El Concepto

La Cuarta Revolución Industrial aplicada a la arquitectura elimina el trabajo mecánico de texturización inicial y seteo de luces. A través de este MVP, un arquitecto puede tomar una foto de su **libro de obra** o cuaderno de bocetos y pedirle al agente:

> "Agente, aplica el workflow de render exterior a este croquis (`activos/proyectos/google-london/fotos/croquis_01.jpg`), con estilo 'minimalista, concreto y cristal'."

## Cómo funciona técnicamente

1. **El Agente (Opencode)** recibe la instrucción.
2. **Lee la imagen** del croquis desde la carpeta `activos/`.
3. **Prepara el payload**: Toma el archivo `workflow_exterior.json` (el verdadero artefacto ejecutable AMV de este proceso) y reemplaza los parámetros:
   - Nodo de imagen de entrada -> `croquis_01.jpg`
   - Nodo de prompt -> "Minimalist architecture, concrete and glass, photorealistic, architectural photography"
4. **Llama al MCP (`run_workflow`)**: El servidor MCP transmite el request a la instancia local de ComfyUI (`127.0.0.1:8188`).
5. **ComfyUI procesa**: 
   - Usa un **ControlNet de tipo Sketch o Canny** para asegurar que los bordes y fugas de la perspectiva del arquitecto se mantengan intactas.
   - Aplica el modelo Stable Diffusion base para el render.
6. **Retorno**: El MCP recupera la imagen generada y el Agente la guarda en `activos/proyectos/google-london/renders/render_v01.png`.

## Implicancias para el Estudio

- **Iteración Rápida**: Un concepto se valida visualmente en segundos frente al cliente.
- **Control (No al azar)**: Gracias a ControlNet, la IA no "inventa" el diseño volumétrico, solo lo materializa.
- **Seguridad de Datos**: Al ejecutarse en hardware local y ser orquestado localmente por Opencode, ningún render secreto (ej. concurso) se filtra en nubes públicas.
