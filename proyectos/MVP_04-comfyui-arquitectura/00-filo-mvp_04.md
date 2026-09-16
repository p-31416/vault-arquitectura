---
tipo: manifiesto
mvp: 04
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, filo, manifiesto, comfyui, mcp]
---

# MVP_04 — Manifiesto: Diseño Arquitectónico Asistido (ComfyUI MCP)

## Por qué

En la práctica arquitectónica tradicional, transformar un croquis rápido a mano alzada en un render hiperrealista o un modelo base requiere horas de trabajo manual en SketchUp, Rhino, 3ds Max y V-Ray. La "4ta Revolución Industrial" en el diseño permite que modelos de difusión iteren visualmente sobre conceptos arquitectónicos en segundos.

Sin embargo, el uso de IAs generativas suele carecer de **control preciso**. 

Este MVP existe para integrar herramientas generativas de forma **determinista y profesional**, usando **ComfyUI** orquestado a través de agentes IA (vía **MCP - Model Context Protocol**). De esta forma, el agente IA del estudio puede operar ComfyUI en nombre del arquitecto para generar o alterar imágenes directamente desde la terminal.

## Principios (Filosofía PitauTech)

1. **Privacidad y Propiedad Intelectual**: Los croquis y diseños del estudio son información confidencial. **El estándar de ejecución para el MVP y para producción es Local (Self-Hosted)**. Todo el stack de ComfyUI corre en las máquinas del estudio para que ninguna IA en la nube absorba la propiedad intelectual sin permiso. 
2. **Arquitectura Mínima Viable (AMV)**: Solo existen los artefactos que se ejecutan o se miden. Un diagrama de workflow en PDF no sirve; **el workflow de ComfyUI en formato `.json` es el único artefacto válido**, documentado y orquestado directamente desde el agente.
3. **Control Total (ControlNet)**: No usamos "prompts al aire". Todo diseño generativo se restringe geométrica y estructuralmente mediante ControlNets (Canny, Depth, Sketch) para respetar las intenciones del arquitecto.
4. **Agentes como Operadores**: El MCP actúa como puente. Antigravity (Opencode) puede invocar los workflows de ComfyUI pasándoles la imagen del vault.

## Scope

**Qué entra**: Instalación y orquestación local de un servidor ComfyUI MCP, creación de workflows JSON (Croquis a Render), ejecución de renderizados desde Opencode.

**Qué NO entra**: Automatización total de la documentación de obra (ver MVP_01), diseño de BIM a partir del render, modelos en la nube con términos de servicio restrictivos.
