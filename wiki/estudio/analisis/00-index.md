---
tipo: indice
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-11-01
tags: [analisis, indice, estudios, evaluaciones]
estado: activo
---

# Índice de Análisis Técnicos — Estudio

> Documentos de evaluación, comparativas y estudios previos a decisiones (ADRs).

---

## Despliegue e Infraestructura

| Documento | Tema | Estado | Fecha |
|-----------|------|--------|-------|
| [analisis-despliegue-wiki-quartz.md](analisis-despliegue-wiki-quartz.md) | **Wiki estática: Quartz vs MkDocs vs otros** — Auth, hosting, costos, wikilinks, graph view | Borrador | 2026-07-24 |

---

## Project Management & Dashboards

| Documento | Tema | Estado | Fecha |
|-----------|------|--------|-------|
| [analisis-integracion-dashboards-pm.md](analisis-integracion-dashboards-pm.md) | **Integración dashboards en ecosistema** — Qué es Plane, arquitectura Wiki+PM+Obsidian, roadmap | Borrador | 2026-07-24 |
| [analisis-dashboards-pm-gratis.md](analisis-dashboards-pm-gratis.md) | **Alternativas $0/mes a Plane** — GitHub Projects, GitLab, Leantime, Oracle Free Tier, Wekan, Kanboard | Borrador | 2026-07-24 |

---

## IA & Generación de Imágenes

| Documento | Tema | Estado | Fecha |
|-----------|------|--------|-------|
| [analisis-ia-generativa-comfyui-alternativas.md](analisis-ia-generativa-comfyui-alternativas.md) | **ComfyUI vs A1111 vs Fooocus + alternativas** — Interfaces locales (ControlNet/LoRA/inpaint/upscaling), rutas de cómputo (RX 570 / RunPod / PC estudio / Comfy Cloud), consolas API pay-per-use (Open Higgsfield, fal, DeepInfra) y generación $0 (AI Horde) | Borrador | 2026-11-01 |

---

## Pendientes / Próximos Análisis

- [ ] **Leantime vs Plane vs GitHub Projects** — Comparativa detallada features/UX/mantenimiento
- [ ] **Autenticación remota: Tailscale vs Cloudflare Tunnel vs VPN** — Para acceso a Leantime self-hosted
- [ ] **Backup strategy: rclone + Google Drive/OneDrive/Wasabi** — Automatización, restore testing
- [ ] **BIM workflow: Revit + Speckle/BCF + Vault** — Integración modelos con wiki y PM
- [ ] **IA en arquitectura: ComfyUI + ControlNet + LoRA training** — Pipeline renders conceptuales *(parcialmente cubierto por analisis-ia-generativa-comfyui-alternativas.md; falta pipeline técnico ControlNet + LoRA training)*

---

## Relación con ADRs

Cada análisis debe derivar en **0 o más ADRs** (decisiones formales). Ver [ADRs índice](../adrs/00-index.md).

| Análisis | ADRs resultantes |
|----------|------------------|
| analisis-despliegue-wiki-quartz.md | *pendiente: ADR-TOOL-001 MkDocs + Netlify* |
| analisis-integracion-dashboards-pm.md | [ADR-INFRA-001 Leantime Self-Hosted](../adrs/ADR-INFRA-001-leantime-selfhosted.md) |
| analisis-dashboards-pm-gratis.md | *pendiente: ADR-INFRA-002 GitHub Projects / Leantime* |
| analisis-ia-generativa-comfyui-alternativas.md | *pendiente: ADR stack IA generativa (mantener ComfyUI + RunPod + APIs por-uso)* |