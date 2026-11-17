---
fecha: 2026-11-17
tema: Hermes mejoras sept-nov 2026 + sistemas creadores + imagen y video con Hermes
slug: hermes-sistemas-imagen-video
idiomas: [es, en]
fuentes_n: 20
confianza: alta (docs oficiales Hermes + OpenRouter + releases verificados)
estado: crudo
investigador: opencode
destino: wiki/glosario/conceptos/system-first-piezas-intercambiables.md
---

# Hermes mejoras + sistemas + imagen/video con Hermes (17/09–17/11/2026)

Fecha: 2026-11-17 · Zona: -03:00 America/Argentina/Buenos_Aires
Objetivo: dejar 20 fuentes verificadas de últimos 2 meses para decidir qué entra a Studio OS.

## Mejoras Hermes core

1. **v0.23.0 Hearth Release — 05/11/2026** — Webapp en browser, un gateway dueño de sesión, group chats, imágenes inline, rewind. https://hermes-ai.net/changelog/
2. **v0.22.0 Threshold Release — 14/10/2026** — setup guiado, conectores Gmail/Linear/Notion, local models un click llama.cpp, SemVer, 600 plugins. https://www.tao.media/nous-research-ships-hermes-agent-threshold-release-with-guided-setup-app-connectors-and-one-click-local-models/
3. **v0.22.4 patch — 21/10/2026** — saca pills, fix WhatsApp, approval chip por perfil. https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.4
4. **Cambios main 24/10/2026** — cron con MCPs nombrados, approvals con args, fix Docker Desktop. https://bwotec.com/hermes-yesterday-2026-10-24/
5. **v0.22.1 — 14/10/2026** — model picker, providers. https://freedom.tech/posts/2026-10-14-hermes-agent-0-22-1/

## Kanban multi-agente

6. **Kanban oficial** — board `~/.hermes/kanban.db`, tools vs CLI, delegate vs Kanban. https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
7. **Kanban tutorial** — 4 historias con dashboard. https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial
8. **Kanban Orchestrator — 13/11/2026** — planner + workers, dispatcher 60s. https://juliangoldie.com/hermes-agent-kanban-orchestrator/
9. **PR #151014 hermes-fal-video — 08/11/2026** — edit/extend/references FAL. https://github.com/NousResearch/hermes-agent/pull/151014
10. **PR kanban store port — 10/11/2026** — multi-tenant. https://github.com/NousResearch/hermes-agent/pull/152413

## Imagen con Hermes

11. **Skill ComfyUI v5.1.0** — txt2img, Wan T2V vía API. https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-comfyui
12. **PR imagegen — 08/11/2026** — estudio Desktop, budget mensual. https://github.com/NousResearch/hermes-agent/pull/147403
13. **Issue #149298 — 05/11/2026** — capabilities por modelo. https://github.com/NousResearch/hermes-agent/issues/149298
14. **Marketplace hermes-fal-video** — Kling 4.0 edit. https://hermes-agent.nousresearch.com/marketplace/hermes-fal-video

## Video con Hermes

15. **Video provider plugin docs** — `video_generate(prompt,image_url?)`. https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin
16. **PR iv-studio — 11/11/2026** — H3 local gratis. https://github.com/NousResearch/hermes-agent/pull/153664
17. **PR Continuo — 11/11/2026** — film-studio 209 tools. https://github.com/NousResearch/hermes-agent/pull/153383

## Sistemas creadores MCP

18. **Treza pipeline MCP — 28/10/2026** — make/run/poll con costo previo. https://www.trezalabs.com/blog/how-to-connect-hermes-agent-to-a-video-pipeline-mcp
19. **Revid 18 video MCP — 22/10/2026** — comparativa. https://www.revid.ai/blog/best-video-mcp-servers
20. **Starpop MCP — 03/11/2026 / Hero MCP — 09/11/2026** — ads y tratamiento como MCP. https://starpop.ai/blog/updates/2026-11-03-the-starpop-mcp-is-here · https://herovideo.ai/updates/agent-mcp-release-november-2026

## Costos imagen verificados 17/11

- Nano Banana 2: $0.50 in / $60 image-out / $3 texto por 1M (~$0.067 en 1K). https://openrouter.ai/google/gemini-3.1-flash-image
- Seedream 5.0 Pro: $0.045 base / $0.09 en 2K / $0.003 ref. https://openrouter.ai/bytedance-seed/seedream-5-0-pro

## Dónde entra

- Core → ESTRUCTURA §3 + §10 + IMPLEMENTACION §12-13
- Kanban → ESTRUCTURA §4.7 + §6
- Imagen → ESTRUCTURA §4.4 + MVP_04
- Video → VISION §6.9 (excluido hasta T5+) + ESTRUCTURA §4.5
- Creadores MCP → ESTRUCTURA §5 contrato (patrones costo previo, async+poll)
