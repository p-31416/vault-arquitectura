---
tipo: crudo-github
fecha: 2026-10-15
fuente: github-repos
estado: crudo
---

# CRUDO GitHub MCPs + OSArch — 2026-10-15

OpenSCAD:
- https://github.com/quellant/openscad-mcp — `uvx openscad-mcp`, FastMCP Python, OpenSCAD 2021.01 floor, scale/measure/clearance/printability
- https://github.com/petrijr/openscad-mcp — v1.0 minimal stdio local-first, tools ping/list_formats/validate_scad/export_model stl-3mf-off/render_preview png/batch
- https://github.com/format37/openscad-mcp — png+stl + docs resource, remote `mcp-remote https://rtlm.info/openscad/...`
- https://github.com/fboldo/openscad-mcp-server — `npx -y openscad-mcp-server`, render_scad_png + export_scad_stl + skill openscad-iterative
- https://github.com/sergiudanstan/openscad-mcp — create/read/edit/export/preview/animate/check_syntax/cheatsheet/version/examples
- https://github.com/dkpoulsen/openscad-mcp — npm `openscad-mcp`, STL OFF AMF 3MF CSG + PNG SVG DXF PDF
- https://github.com/jhacksman/OpenSCAD-MCP-Server — primitives + scad_code + revision + preview_url/download

FreeCAD:
- https://github.com/spkane/freecad-addon-robust-mcp-server — 255 stars/59 forks, 150+ tools, xmlrpc 9875/socket/embedded, GUI+headless, macros
- https://github.com/ahelja/FreeCAD-MCP — menciona opencode explícito, XML-RPC 9875, QTimer dispatcher, tools status/list/create/edit/move/delete/selection/run_python/capture_view/export STEP IGES STL OBJ PLY 3MF AMF OFF BREP
- https://github.com/LBurny/cadpilot — `uvx cadpilot`, sketches constrain + assemblies joints, XML-RPC
- https://github.com/neka-nat/freecad-mcp — addon workbench Start RPC + `uvx freecad-mcp`
- https://github.com/contextform/freecad-mcp — cross-platform installer + `claude mcp add freecad`
- https://github.com/theosib/FreeCAD-MCP-Server — debug runtime: list_documents/get_document_graph/inspect_object/analyze_shape/sketch_diagnostics/tracked_recompute/execute_script/screenshot 9876
- https://github.com/tspspi/mcpFreeCAD — stdio+remotehttp auth, BREP library, gears/Fasteners/Curves/A2plus
- https://github.com/proximile/FreeCAD-MCP — 57 tools + Docker headless + TRELLIS/ComfyUI/Vision

LibreCAD:
- https://github.com/thebossnow/aiblueprint-mcp — ezdxf→DXF + LibreCAD dxf2png preview, 6 tools drawing/entity/layer/block/annotation/view + offset/fillet/dim+hatch, MIT, debate upstream https://github.com/LibreCAD/LibreCAD/issues/2577
- https://github.com/piexl/CAD-MCP — ezdxf + LibreCAD open demo_drawing.dwg (ref)

Rhino/GH:
- https://github.com/mcneel/RhinoAI — oficial Rhino MCP Platform, mcneel.github.io/RhinoAI
- https://github.com/jingcheng-chen/rhinomcp/ — `uvx rhinomcp@latest`, Package Manager rhinomcp, mcpstart TCP 1999, Rhino+GH single config
- https://github.com/GenEnv/rhino-gh-mcp/blob/main/README.md — .yak rhinogh-mcp, _ToggleMcpService 9876/9999, skills facade-design/bridge-basics
- https://github.com/gramaziokohler/lamcp — `uvx lamcp`, Lamcp_Bridge.ghuser 8765
- https://github.com/goldsmith323/rhino_gh_mcp — 30+ tools HTTP IronPython
- https://github.com/dongwoosuk/rhino-grasshopper-mcp — ML auto-layout DBSCAN/K-means
- https://github.com/brookstalley/cordyceps — 7 tools/100+ acciones, 26929
- https://github.com/EaseHee/rhino-mcp — ~245 tools, IFC/gbXML, STEP/IGES

IFC/Bonsai:
- https://github.com/Show2Instruct/bonsai-mcp — recomendado codegen, 9878, doctor, bonsai://project/scene
- https://github.com/Show2Instruct/ifc-bonsai-mcp — 50+ tools + RAG ChromaDB (legacy)
- https://github.com/nhantruong96/bonsai-mcp — solo semántica IFC, bl_status/bl_set_view/bl_focus_element
- https://github.com/JotaDeRodriguez/Bonsai_mcp — fork BlenderMCP + Bonsai

Unreal/Twinmotion/Blender/Godot:
- https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin — skills/unreal-mcp + hooks
- https://github.com/FFZackFair92/unreal-engine-mcp — Remote Control 30010 + Python, pip -e .
- https://github.com/ATDev-Inc/uemcp — `uvx uemcp`, 40 tools
- https://github.com/groscy/unreal-mcp — Remote Execution 239.0.0.1:6766
- https://github.com/runreal/unreal-mcp — `npx -y @runreal/unreal-mcp`
- https://github.com/ChiR24/Unreal_mcp — EngineWire single tool `unreal` search/describe/execute/configure, 3000/8090 + token
- https://github.com/ScanBIM-Labs/twinmotion-mcp — 5 tools tm_*, Workers + APS OAuth2 + KV, créditos
- https://github.com/ahujasid/blender-mcp — `uvx mcp-for-blender`, auto-setup incl OpenCode
- https://github.com/Raunaksplanet/godot-mcp-server — Node+WS+GDScript 40+ tools, cita opencode
- https://github.com/Utopian-Academy/Genesis — Godot archviz OSM/live-link
- https://github.com/Naxela/Meridian — Blender→Godot one-click bake
- OSArch: https://wiki.osarch.org/bonsai/ , https://wiki.osarch.org/bonsai-installation/ , https://wiki.osarch.org/floss-visualisation-and-documentation/ , https://wiki.osarch.org/blender2godot/ , https://osarch.org/2023/01/22/the-potential-open-source-game-engine-for-blender-bim/
