---
tipo: spec
mvp: 04
version: 1.0.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, spec, comfyui, mcp, arquitectura]
---

# MVP 04 — Spec v1.0.0: Creación de Arquitectura desde Texto vía ComfyUI MCP

## Propósito

Integrar ComfyUI como motor de generación arquitectónica orquestado vía MCP, resolviendo el problema de **iteración lenta de renders** en el estudio. Transformar descripciones textuales, croquis, modelos 3D y planos en renders arquitectónicos en segundos, manteniendo control geométrico y privacidad de datos.

## Alcance

### Niveles (progresivos)

| # | Nivel | Input | Output | Técnica | Estado |
|---|-------|-------|--------|---------|--------|
| 01 | txt2img | Prompt textual | Render arquitectónico | txt2img + seed variation | 🔜 Pendiente |
| 02 | img2img | Croquis/foto + prompt | Render estilizado | img2img + denoise | 🔜 Pendiente |
| 03 | ControlNet | Plano/3D depth/canny + prompt | Render con geometría exacta | ControlNet (Depth/Canny/Sketch) | 🔜 Pendiente |
| 04 | Video | Render/imagen | Walkthrough animado | LTX-2.3 / WAN img2vid | 📅 Futuro |
| 05 | Rhino MCP | Modelo Rhino 3D | Render en tiempo real | Rhino MCP + depth maps | 📅 Futuro |

### Criterios de éxito (v1.0.0)

- [ ] Workflow txt2img funcional desde Opencode → render en `activos/proyectos/`
- [ ] 5+ prompts arquitectónicos documentados con resultados
- [ ] Integración MCP operativa (artokun/comfyui-mcp)
- [ ] Pipeline img2img croquis→render con ControlNet
- [ ] Documentación de modelos recomendados (AMD 8GB y hardware ideal)

### Lo que entra

- Instalación y configuración de artokun/comfyui-mcp
- Creación de workflows .json (AMV) para cada nivel
- Ejecución desde Opencode vía MCP tools
- Privacidad local-first (datos nunca salen de la máquina)
- Documentación de modelos, prompts y workflows

### Lo que NO entra (v1.0.0)

- Automatización BIM (ver MVP_01)
- Conexión Rhino en tiempo real (n_05 — futuro)
- Animación profesional (n_04 — futuro)
- Entrenamiento de LoRAs propios del estudio
- Despliegue en servidor compartido del estudio

## Stack tecnológico

| Componente | Elección | Razón |
|------------|----------|-------|
| Motor generación | ComfyUI v0.28.0 | Modular, open-source, ecosistema más amplio |
| MCP server | artokun/comfyui-mcp | 108 tools, 32 skills, local-first, MIT |
| Orquestador | Opencode (agente) | Terminal del vault, MCP nativo |
| Modelo base (AMD) | ArchitectureRealmix v1.1 + Z-Image Turbo GGUF | <8GB VRAM, calidad arquitectónica |
| Modelo base (ideal) | Flux.1 Dev / SDXL | Calidad superior para renders finales |
| Control geométrico | ControlNet (Depth / Canny / Sketch) | Preserva intención del arquitecto |
| Almacenamiento | `activos/proyectos/` (gitignored) | Binarios fuera de git |
| GPU actual | AMD 8GB (DirectML) | Tests locales |
| GPU ideal | NVIDIA RTX 4090 24GB+ / RTX 6000 Ada | Producción |

## Referencias

- [[00-filo-mvp_04]] — Manifiesto y filosofía
- [[02-ft-mvp_04]] — Plan técnico detallado
- [[modelos-recomendados]] — Guía de modelos para arquitectura
- [[03-log-mvp_04]] — Bitácora de iteraciones
- [[wiki/estudio/adr-001-comfyui-mcp]] — ADR de adopción
- [[wiki/glosario/referentes/ia-estudios-internacionales]] — IA en estudios globales
