---
tipo: concepto
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [glosario, concepto, system-first, modularidad, studio-os, loop-engineering]
idioma: es
---

# System First — piezas intercambiables

> Lo primero es el sistema. La IA acompaña como herramienta extra sobre una base que entrega con trazabilidad completa.

- [[#Origen en el estudio]]
- [[#Los 5 linajes]]
- [[#Tabla aportes → referente]]
- [[#Horizonte 2027]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Origen en el estudio

Esta página resume la filosofía System First del estudio y sus referentes en ingeniería de sistemas.

Raíz metodológica en [[proyectos/MVP_01-dibujo_ia/00-filo-mvp_01|filo MVP_01]]: documentar procesos, dibujar con lenguaje natural, validar en AutoCAD desde práctica docente, proyectar la misma metodología hacia Revit, Rhino, Grasshopper, Blender y ComfyUI.

Integración en sistema en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION Studio OS §1.6 + principio 10]]: el sistema sostiene la entrega, cada pieza se cambia por contrato, los loops medidos multiplican la capacidad.

Principios heredados:

- Menor esfuerzo posible: del pensamiento a la pantalla con fricción mínima
- Biblioteca viva de decisiones del estudio, revisable por humanos, con defaults opinados
- Progresión por niveles que incorpora lo anterior y se prueba en plano real
- Espíritu software-agnóstico, MCP como envoltura en lenguaje natural
- Tablero y trazo a mano como origen, ControlNet hacia materia construible

## Los 5 linajes

### 1. Unix modular

Filosofía Unix: programas que hacen una cosa bien y trabajan juntos mediante interfaz universal de texto. Regla de composición, separación entre política y mecanismo, piezas chicas unidas por contrato claro.

Aporte a Studio OS: el pipe como antepasado del loop auditoría → comparación → entrega.

### 2. Software libre

Copyleft y licencias que mantienen el uso, copia, modificación y redistribución. Desarrollo disperso que suma mejoras desde muchos lugares.

Aporte a Studio OS: base abierta con licencia comercial propia, privativo solo donde hoy aporta valor exclusivo.

### 3. Arquitectura por contrato

Pipes-and-filters, Ports and Adapters, microservicios, contenedores: lo que circula es el contrato, la implementación se reemplaza sin romper el resto.

Aporte a Studio OS: AutoCAD, Rhino+Hops, FreeCAD, ComfyUI como implementaciones reemplazables del mismo contrato de tarea.

### 4. Plataformas e IDP

Kubernetes como plataforma para construir plataformas. IDP con portal Backstage, golden paths, self-service con guardrails, multi-tenancy por workspaces aislados.

Aporte a Studio OS: un punto único por estudio, golden paths que acercan al junior a calidad senior, escala hacia muchos equipos.

### 5. MCP + Agent Skills

MCP spec stateless con primitivas Tools / Resources / Prompts. Patrones Mesh, Gateway agregador y Jerárquico Router. Agent Skills con progressive disclosure: el saber procedimental se carga solo cuando la tarea lo pide.

Aporte a Studio OS: Hermes como router, skills como `auditar-documentacion-cad` y `experto-comfyui`, loops con semilla, parámetros y registro.

## Tabla aportes → referente

| Aporte del estudio | Referente en sistemas | Qué toma Studio OS |
|---|---|---|
| System First, pensar como ingenieros de sistemas | Filosofía Unix, regla de composición | Contrato antes que herramienta |
| Fichas intercambiables | Arquitectura por contrato, Gateway MCP | Cambiar motor sin reconstruir sistema |
| Todo abierto con licencia propia | Software libre, Apache 2.0 / MIT / GPL | Propiedad como base de continuidad |
| Escalar a muchos usuarios y equipos | IDP, Kubernetes, workspaces | Un agente por estudio, multi-equipo |
| Multiplicar capacidad del estudio | Golden paths, Skills progresivos | Menos horas senior por entrega |
| De prompt a loop engineering | MCP stateless + Skills AAIF | Trazabilidad: archivo, versión, params, aprobación |

## Horizonte 2027

De prompt engineering a loop engineering: loops medibles que se repiten y mejoran sobre una base que ya entrega el mismo render con menos horas. Presente iterativo, un día a la vez, con norte en capacidad multiplicada.

## Conceptos relacionados

- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — rol que diseña sistemas que diseñan arquitectura
- [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] — aprobación humana como gate
- [[wiki/glosario/conceptos/bim-metodologia|bim-metodologia]] — trazabilidad y CDE
- [[wiki/glosario/conceptos/lean|lean]] — valor, flujo, mejora continua
- [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] — capacidad, automatizar fricción

## Referencias

Fuentes verificadas 2026-11-16, sin 404:

- Filosofía Unix, modularidad e interfaz universal: https://www.linfo.org/unix_philosophy.html
- Arquitectura MCP, host / cliente / servidor, stateless: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
- MCP + Agent Skills bajo AAIF, progressive disclosure: https://opensource.googleblog.com/2026/11/scaling-ai-agents-open-standards-mcp-aaif.html
- Patrones MCP multi-agente, híbrido, mesh y gateway: https://developer.ibm.com/articles/mcp-architecture-patterns-ai-systems/
- IDP modular y escalable, golden paths: https://openchoreo.dev/
