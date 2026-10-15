---
tipo: playbook
mvp: 04
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [comfyui, infraestructura, setup, mcp]
---

# Playbook: Opciones de Setup para ComfyUI

Este playbook analiza las distintas formas de instalar y correr ComfyUI en el estudio, comparando su complejidad, mantenimiento y adecuación al flujo de trabajo diario de los arquitectos.

## Opciones de Instalación

### 1. ComfyUI Desktop App (Recomendada para producción local)
Recientemente lanzada, es una aplicación empaquetada (tipo instalador para Windows/Mac/Linux) que incluye su propio entorno de Python aislado.
- **Simplicidad**: **ALTA**. Se instala como cualquier programa (`.exe` o `.dmg`).
- **Mantenimiento**: Muy bajo. Actualiza la UI y las dependencias internamente sin requerir conocimientos de terminal.
- **Caso de uso**: Ideal para el equipo de arquitectura. Nadie necesita saber qué es `pip` o `venv`. Simplemente abren la app y ejecutan workflows locales.
- **MCP Compatibilidad**: Al correr localmente, expone el mismo puerto `8188`, por lo que el MCP puede orquestarlo perfectamente.

### 2. Instalación Manual vía Python / Git (Estado actual)
La forma tradicional mediante `git clone` y la creación de un entorno virtual de Python.
- **Simplicidad**: **BAJA**. Requiere manejo de terminal, dependencias CUDA, PyTorch, xformers, etc.
- **Mantenimiento**: Alto. Actualizar nodos a menudo rompe dependencias (el famoso "dependency hell").
- **Caso de uso**: Ideal solo para desarrollo avanzado, pruebas de nodos experimentales o R&D (tu configuración actual). 

### 3. Comfy Cloud (SaaS)
La plataforma oficial en la nube de ComfyOrg.
- **Simplicidad**: **MÁXIMA**. Cero instalación, se opera desde el navegador.
- **Mantenimiento**: Nulo. El hardware (GPUs) y el software lo mantienen ellos.
- **Caso de uso**: Ideal para validación rápida (MVP), o cuando no se dispone de GPUs potentes (laptops de viaje).
- **Contrapartida**: Requiere pago por uso/subscripción, y plantea dudas sobre el tratamiento de datos (ver `comfy-tratamiento-datos.md`).

## Decisión Arquitectónica para el Estudio

1. **Para pruebas inmediatas (MVP)**: Podemos usar tu instalación actual de Python o Comfy Cloud para probar el MCP.
2. **Para despliegue en la oficina**: Se debe estandarizar el uso de **ComfyUI Desktop App**. Esto bajará la barrera de entrada para los arquitectos del equipo, estandarizando la infraestructura sin que se rompan sus entornos de trabajo.
