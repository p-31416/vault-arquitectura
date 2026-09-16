---
tipo: entidad
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [entidad, runpod, gpu, comfyui, infraestructura, ptech]
---

# RunPod

Plataforma GPU cloud para escalado de flujos ComfyUI (elaboración gráfica y videos para arquitectura) cuando el recurso local no alcanza. Uso previsto: **Mes 2 en adelante**, documentado como entidad para trazabilidad.

## Índice

- [[#Uso en Studio OS]]
- [[#Características]]
- [[#Privacidad]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Uso en Studio OS

- **Flujo:** `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json` (demo genérica mañana) + futuros flujos ComfyUI de elaboración gráfica y video
- **Cuándo:** Mes 2 EXPERIMENTAR, si la base Vault está aceitada y se requiere escalado
- **Modelo:** GPU efímera, pago por uso, templates ComfyUI

## Características

- GPUs cloud (A100, 4090, etc.) con ComfyUI preinstalado
- Escalado para moodboards, videos, batch de imágenes referentes
- Alternativa a GPU local 24GB del estudio cuando se necesita más cómputo

## Privacidad

Desde el inicio, análisis de imágenes con **modelos locales**. Si se usa modelo comercial en RunPod, queda anotado con metadatos (imagen + nomenclatura + versionado automático + doc WF-log) — ver `[[specs/260910-plan-trimestral-unificado-studio-os-emilia#10. Stack, privacidad y RunPod|specs trimestral §10]]` y mini-política de privacidad (pendiente contrato).

## Conceptos relacionados

- [[wiki/glosario/conceptos/ptech-filosofia|ptech-filosofia]] — Filosofía Pitautech (I+D, proyecto como unidad de aprendizaje)
- [[wiki/glosario/conceptos/ptech-metricas-friccion|ptech-metricas-friccion]] — Métricas tiempo humano vs máquina
- [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04 ComfyUI]] — Flujos y reglas
- [[specs/260910-plan-trimestral-unificado-studio-os-emilia|Plan trimestral unificado]] — Mes 2 RunPod

## Referencias

- RunPod — https://www.runpod.io/ (verificado 2026-09-10 — 200) — plataforma GPU cloud
- `[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]` — Plan trimestral §10
- `raw/brainstorm/Pitautech_Propuesta_I+D_Arquitectura_Vault.md` — visión escalado
