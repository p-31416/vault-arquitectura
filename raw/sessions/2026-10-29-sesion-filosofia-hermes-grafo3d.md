---
tipo: log
fecha: 2026-10-29
tags: [sesion, filosofia, hermes, diagramas, grafo-3d]
---

# Sesión 2026-10-29 — Filosofía Hermes + norma de diagramas + grafo 3D

Checkpoint: se pausa acá, se sigue con filosofía y grafo 3D.

## Qué se hizo

1. **Mapa filosófico del vault**: corte determinista (scripts) vs. agéntico vs. humano con `s`; 7 flujos; matriz por proceso. Decisiones: híbrido (núcleo nuevo + migración selectiva), Hermes 1→N, HITL estricto.
2. **Norma de diagramas aprobada**: draw.io formal / Mermaid rápido / Excalidraw solo croquis. Comparativa viva en `diagramas/prueba-comparativa.md` (mismo G1 en 3 formatos + tabla).
3. **Plugins Obsidian instalados**: Excalidraw v2.29.0 + draw.io v3.1.1 (id `drawio`), registrados en `.obsidian/community-plugins.json`. Hallazgo: el vault no tenía community plugins (por eso el `.excalidraw.md` no abría).
4. **Documento único**: `specs/261029-filo-vault-v2.md` (visión completa + estructura + requisitos enunciados).
5. **Ensayo**: `specs/261029-filosofia-hermes.md` — breve, sin técnica (LM, harness, skill, MCP, Age of Empires, 4ta revolución, 2026/2027).
6. **Gráficos**: `diagramas/flujo-fuentes-wiki-hermes.*` (4 carriles + tabla replicable, 40 celdas) y `diagramas/cerebro-hermes-fractal.*` (4 ramas fractales + rizoma punteado + anillo Hermes, 37 celdas) en drawio+SVG+Mermaid+nota.
7. **Grafo 3D**: `diagramas/cerebro-hermes-fractal-3d.html` (patrón `scripts/grafo-yt-mock.html`, JS verificado `node --check OK`, 23 nodos, panel por ramas, click → ruta vault).

## Archivos creados

- `specs/261029-filo-vault-v2.md`, `specs/261029-filosofia-hermes.md`
- `diagramas/prueba-comparativa.{mmd,excalidraw.md,drawio,drawio.svg,excalidraw.svg,md}`
- `diagramas/flujo-fuentes-wiki-hermes.{mmd,drawio,drawio.svg,md}`
- `diagramas/cerebro-hermes-fractal.{mmd,drawio,drawio.svg,md,3d.html}`
- `.obsidian/plugins/obsidian-excalidraw-plugin/*`, `.obsidian/plugins/drawio/*`, `.obsidian/community-plugins.json`

## Archivos modificados

- `diagramas/prueba-comparativa.md` (§3 Excalidraw + tabla factual), `diagramas/prueba-comparativa.excalidraw.md` (reescrito válido, 18 elementos)

## Pendiente (retomar)

- Seguir con filosofía y grafo 3D (pedido explícito).
- Activación manual pendiente del usuario en Obsidian: Community plugins → Install/Enable (Excalidraw + draw.io), Obsidian ≥ 1.8.7.
- Fila en `log.md` al cierre definitivo.

## Análisis cerebro-digital (Karpathy)

- **Topics**: norma-diagramas-obsidian · harness-vs-modelo · fractal-rizoma-wiki · hitl-estricto · ingest-por-fuente
- **Entidades**: Hermes (Nous, MIT) · Pi (orquestador) · draw.io / diagrams.net · Excalidraw plugin · Karpathy (referente)
- **Hechos**: draw.io gratis forever + plugin Obsidian desktop-only · Excalidraw v2.29.0 pide Obsidian ≥1.8.7 · vault sin community plugins hasta hoy · Mermaid nativo + diff limpio · 3D pattern A-Frame/force-graph reutilizado
