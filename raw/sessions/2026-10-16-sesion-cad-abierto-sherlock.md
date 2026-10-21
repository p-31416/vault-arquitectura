---
tipo: log
fecha: 2026-10-16
tags: [sesion, sherlock, research, cad-abierto, mcp, opencode, github-sync]
---

# Sesión 2026-10-16 — Research CAD abierto + MCPs + consolidación sherlock + sync GitHub

## Qué se hizo

- **Research CAD/BIM/viz abierto**: informe OpenSCAD + FreeCAD 1.1.4 + LibreCAD 2.2.x (Win + Mint Xfce, lenguajes, docs verificadas 200) + MCPs FreeCAD robust / RhinoMCP / IfcMCP oficial / Unreal MCP Epic / Twinmotion APS + alternativas Blender+Bonsai+Godot. Ver `raw/research/2026-10-15-cad-abierto-mcp-opencode.md` (34 fuentes).
- **Subagente @sherlock**: exterior multi-fuente (docs + GitHub + YouTube), madre + 3 crudos + stub + cache + fila en `raw/research/00-index.md`.
- **Corrección convención**: todo el research consolidado a `raw/research/` (5 archivos `2026-10-15-cad-abierto-*`); `raw/contenidos/` liberado para `@contenidos`. Regla ajustada en `.opencode/agents/sherlock.md` (cierre en research, prohibido wiki y contenidos).
- **GitHub**: commit `2bb94b7` pusheado a `origin/master` (197 archivos texto/código). Binarios PNG/JPG/PDF excluidos vía `.gitignore` ampliado (MVP_04.02 inputs/salidas/ref, diagramas png, presupuestos pdf).

## Archivos modificados

- `raw/research/2026-10-15-cad-abierto-mcp-opencode.md` + stub + 3 crudos + `00-index.md`
- `.opencode/agents/sherlock.md` (descripción + misión + regla global)
- `.gitignore` (binarios MVP_04.02 + diagramas + presupuestos)
- Sync masivo vault (sessions, specs, scripts, wiki, proyectos — solo texto)

## Qué sigue

1. Leer madre `raw/research/2026-10-15-cad-abierto-mcp-opencode.md`.
2. Seguir por research sherlock: `¿Avanzo a curaduría? s/N` → `@contenidos` reporte legible → `¿Avanzo a wiki?` → `@vaultworm-arq` a glosario software.
3. Binarios pendientes van por `activos/`, nunca por git.

## Cerebro-digital

- Topics: cad-abierto-win-mint-xfce, mcp-freecad-robust, rhinomcp-gh, ifcmcp-bonsai-nativo, unreal-mcp-local, twinmotion-solo-remoto-aps, godot-archviz-meridian, sherlock-solo-research-sin-contenidos, git-sin-binarios.
- Entidades: OpenSCAD .scad, FreeCAD 1.1.4 Python+OCCT, LibreCAD 2.2 DXF, Bonsai/IfcOpenShell, RhinoMCP, Unreal MCP :8000/mcp, twinmotion-mcp ScanBIM, Meridian/Genesis Godot, opencode.json type local/remote.
- Hechos: 10/10 docs oficiales 200 verificados; sin MCP nativo LibreCAD vivo; sin MCP local Twinmotion; commit 2bb94b7 limpio sin binarios; próxima puerta = curaduría contenidos.
