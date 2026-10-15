---
tipo: research-sherlock
fecha: 2026-10-15
slug: cad-abierto-mcp-opencode
fuentes_n: 34
confianza: Alta (oficial 10/10 verificado 200) / Media-Alta (GitHub activos + OSArch)
idioma: ES/EN
entregado_por: sherlock
estado: pendiente-formato
timezone: America/Argentina/Buenos_Aires
---

# 2026-10-15 CAD abierto + MCPs Opencode — hallazgos brutos verificados

Fecha: 2026-10-15 | Fuentes N: 34 | Confianza: Alta oficial, Media-Alta comunidad

## Resumen

OpenSCAD (lenguaje .scad propio, base C++), FreeCAD 1.1.4 (núcleo C++ + Python + Qt, workbenches BIM/Draft/Part), LibreCAD 2.2.x (C++/Qt4→Qt5, GPLv2, 2D DXF) cubren CAD abierto en Windows 10/11 64-bit y Linux Mint Xfce (Ubuntu-based: `apt install`, AppImage, PPA). Los tres tienen MCPs operables desde Opencode vía `type: local` stdio: OpenSCAD 7+ variantes (quellant/RobertCoop `uvx openscad-mcp` la más completa, petrijr v1.0 minimal, fboldo STL+PNG, sergiudanstan CRUD+cheatsheet), FreeCAD 7+ variantes (spkane robust 255 stars/150+ tools recomendado estudio, ahelja con mención explícita `opencode`, LBurny cadpilot con `uvx cadpilot`, neka-nat, theosib debug, tspspi remotehttp), LibreCAD sin API viva — vía `thebossnow/aiblueprint-mcp` (ezdxf→DXF + `dxf2png` preview, MIT, corre sin licencia). Rhino+Grasshopper: oficial `mcneel/RhinoAI` + `jingcheng-chen/rhinomcp` (`uvx rhinomcp`, comando `mcpstart`, cubre Rhino y GH en un plugin) + `GenEnv/rhino-gh-mcp` (yak + skills facade-design) + `gramaziokohler/lamcp` (ETH, `uvx lamcp`) + `brookstalley/cordyceps` + `EaseHee/rhino-mcp` (~245 tools). IFC-BIM abierto: `IfcMCP` oficial dentro de IfcOpenShell (`docs.ifcopenshell.org/ifcmcp.html`, `pip install '.[mcp]'`, `claude mcp add --transport stdio ifc -- ifcmcp`) + `Show2Instruct/bonsai-mcp` (recomendado, codegen, 11 tools QUERY/EDIT, puerto 9878) + `nhantruong96/bonsai-mcp` (solo semántica IFC, sin mesh crudo) + `JotaDeRodriguez/Bonsai_mcp` (fork BlenderMCP). Unreal: oficial Epic `dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor` (plugin ModelContextProtocol + AllToolsets, `http://127.0.0.1:8000/mcp`, `ModelContextProtocol.StartServer`, `GenerateClientConfig`) + `EpicGames/unreal-engine-skills-for-claude-code-plugin` + comunidad `FFZackFair92/unreal-engine-mcp` (sin compilar C++, Remote Control + Python), `ATDev-Inc/uemcp` (`uvx uemcp`, cero install UE), `groscy/unreal-mcp`, `runreal/unreal-mcp`, `ChiR24/Unreal_mcp EngineWire`. Twinmotion: sin API pública — solo `ScanBIM-Labs/twinmotion-mcp` remoto vía APS (`tm_import_rvt`, `tm_render_image` hasta 8K, `tm_export_video`, requiere `x-scanbim-api-key` + créditos). Alternativas open gratuitas viz/arq: Blender 4.x + Bonsai (NativeIFC, GPL), FreeCAD BIM workbench, Godot 4.6 + Genesis (Utopian-Academy, import GLB/FBX/OBJ/.blend + OSM) + Meridian (Naxela, Blender→Godot one-click, lightmap bake) + Blender2Godot (OSArch), Material Maker, Poly Haven. Opencode acepta todos los stdio (`mcpServers` legacy vs `mcp` + `type:local/command[]/environment` + `type:remote/url/headers`, ver `opencode.ai/docs/mcp-servers/` verificado 200 + `opencode.json` del vault con 7 MCPs activos como ejemplo).

## Ejes

### 1. CAD abierto — lenguajes, docs oficiales, instalación Windows + Mint Xfce

- OpenSCAD: lenguaje declarativo propio `.scad` (`cube/sphere/cylinder/translate/rotate/linear_extrude`, `$` vars, `echo/render`), engine C++. Docs: `https://openscad.org/documentation.html` [trad. propia: tutorial 9 capítulos + User Manual + Language Reference + CheatSheet] (verificado 200), manual Wikibooks `https://en.wikibooks.org/wiki/OpenSCAD_User_Manual` + offline `https://files.openscad.org/documentation/` + repo `https://github.com/openscad/openscad-documentation/`. Instalación: `https://openscad.org/downloads` (200): Windows 7+ x86 exe/zip + `winget install --id=OpenSCAD.OpenSCAD -e`; Linux Debian/Ubuntu `sudo apt-get install openscad`, Fedora `yum install openscad`, Arch `pacman -S openscad`, AppImage x86_64 + ARM64, Docker, nightly OBS.
- FreeCAD 1.1.4 (2026-09-28): núcleo C++ (OpenCASCADE) + scripting Python + UI Qt, extensible por workbenches. Docs: `https://www.freecad.org/downloads` (200, estable 1.1.4, Windows 10+ installer/portable, Linux AppImage x86_64/aarch64) + `https://wiki.freecad.org/Download/en` + `https://wiki.freecad.org/index.php` (hubs Users/Power users) + `https://wiki.freecad.org/Python_scripting_tutorial/en` [trad: Python controla FreeCAD: crear objetos, modificar geometría y UI, vía consola, macros, scripts externos] + DevHandbook bindings C++→Python + mirror docs `https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Installing_on_Linux.md` (cita Mint: `Many Linux distributions are based on Ubuntu... like Linux Mint... sudo add-apt-repository ppa:freecad-maintainers/freecad-stable / sudo apt install freecad freecad-doc`) y `Installing_on_Windows.md`. Mint Xfce: preferir PPA stable o AppImage (`chmod +x *.AppImage`) por sobre `apt install freecad` de Universe (desactualizado).
- LibreCAD 2.2.x: C++/Qt (Qt4→Qt5 obligatorio en 2.2.0), GPLv2, 2D DXF/DWG (vía LibreDWG), 30+ idiomas. Docs: `https://librecad.org/` (200) + `https://docs.librecad.org/en/latest/getstart/install.html` (200) [trad: estable vs nightly, Windows exe, Linux repos + AppImage v2.2.1+, build from source] + `https://github.com/LibreCAD/LibreCAD/releases/tag/downloads-latest` + wiki `https://github.com/LibreCAD/LibreCAD/wiki/Download` + manual PDF. Instalación: Windows EXE desde GitHub; Mint/Ubuntu `sudo apt-get install librecad` (viejo, sin `dxf2png`) → para MCP previews usar AppImage oficial v2.2.1+.
- Lenguajes resumen: OpenSCAD .scad; FreeCAD Python (usuario) + C++ (core); LibreCAD C++ sin scripting (su API es el DXF).

### 2. Rhino + Grasshopper MCPs

- Oficial McNeel `https://github.com/mcneel/RhinoAI` — `Rhino MCP Platform`, guías en `mcneel.github.io/RhinoAI`, soporta Claude Desktop/Code, Copilot, Codex, Gemini.
- `https://github.com/jingcheng-chen/rhinomcp` — controla Rhino 3D y Grasshopper en lenguaje natural, un plugin + `uvx rhinomcp@latest`, bridge TCP 127.0.0.1:1999, comandos `mcpstart/mcpstop`, tools `gh_create_document/gh_search_components/gh_add_component/gh_connect_components/gh_set_parameter_value/gh_run_solution/gh_build_graph` + captura viewport + RhinoScript-Python/RhinoCommon C#.
- `https://github.com/GenEnv/rhino-gh-mcp` v0.2.6 — server Python + plugins `.yak` (`rhinogh-mcp-grasshopper/.gha` + `rhinogh-mcp-rhino/.rhp`), comandos `_PackageManager/_ToggleMcpService`, skills `facade-design` (7 tipologías + .gh refs) + `rhino-gh-bridge-basics`, `.mcpb` Desktop Extension.
- `https://github.com/gramaziokohler/lamcp` (ETH Gramazio Kohler) — `claude mcp add lamcp --scope user -- uvx lamcp` + `Lamcp_Bridge.ghuser` (HTTP 127.0.0.1:8765), tools `run_python_script/list_grasshopper_objects/add_python_component/solve_grasshopper/save_grasshopper_document/capture_*`.
- Otros: `https://github.com/goldsmith323/rhino_gh_mcp` (30+ tools, HTTP bridge IronPython), `https://github.com/dongwoosuk/rhino-grasshopper-mcp` (ML auto-layout DBSCAN/K-means), `https://github.com/brookstalley/cordyceps` (7 tools/100+ acciones, puerto 26929), `https://github.com/EaseHee/rhino-mcp` (~245 tools, IFC/gbXML import-export, STEP/IGES/STL/OBJ).
- Requisito común: Rhino 8 + Windows (McNeel), bridge local loopback, Opencode `type:local`.

### 3. IFC-BIM abierto — IfcOpenShell / Bonsai

- `https://docs.ifcopenshell.org/ifcmcp.html` (200) — `IfcMCP is an MCP server that exposes IfcOpenShell query and edit tools... holding the IFC model in memory` [trad. propia: expone query/edit sin I/O entre llamadas]. Install: `pip install '.[mcp]'` en `src/ifcmcp`, uso `claude mcp add --transport stdio ifc -- ifcmcp` / `{"mcpServers":{"ifc":{"type":"stdio","command":"ifcmcp"}}}`. Usable como librería Python sin MCP.
- `https://github.com/Show2Instruct/bonsai-mcp` (recomendado) — `MCP client --stdio--> bonsai-mcp --127.0.0.1:9878--> Blender addon (bpy+Bonsai+IfcOpenShell)`, 11 tools `[QUERY]/[EDIT]` (`execute_ifc_code/execute_blender_code`), recursos `bonsai://project/scene`, prompts `model-audit/visual-verify`, `uv run bonsai-mcp doctor`. Requiere Blender 3.6+ (4.x rec), Bonsai desde `bonsaibim.org`, `uv`.
- `https://github.com/Show2Instruct/ifc-bonsai-mcp` (previo, 50+ tools + RAG ChromaDB + Trimesh) — legacy, migrar a bonsai-mcp.
- `https://github.com/nhantruong96/bonsai-mcp` — `query, view through Blender viewport, edit with IFC semantics (IfcOpenShell+Bonsai). No raw mesh tools` [trad: edita con semántica IFC, nunca mesh crudo]; `ifc_*` funciona con Blender cerrado, `bl_*` requiere Blender+Bonsai+addon (Start Server, 127.0.0.1:9876).
- `https://github.com/JotaDeRodriguez/Bonsai_mcp` — fork BlenderMCP + Bonsai, `uv run tools.py`, addon `addon.py`.
- Base: `https://bonsaibim.org/` (200) + `https://docs.bonsaibim.org/studio/quickstart/installation.html` (Blender→Preferences→Get Extensions→Bonsai→Install) + `https://extensions.blender.org/add-ons/bonsai/` + `https://docs.ifcopenshell.org/ifcopenshell-python/installation.html` (PyPI/ZIP/Conda/Docker) + `https://wiki.osarch.org/bonsai-installation/` + `https://wiki.osarch.org/bonsai/`. Bonsai Studio Alpha Win/Mac/Linux, Blender 5.1/5.2 + Python 3.13.

### 4. Unreal Engine + Twinmotion

- Oficial Epic `https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor` (200) — `Unreal MCP embeds an MCP server inside the Unreal Editor process... over local HTTP` [trad: embebe MCP dentro del editor]. Setup: habilitar plugins ModelContextProtocol + AllToolsets (+ToolsetRegistry auto), `Editor Preferences>Model Context Protocol>Auto Start Server` (`http://127.0.0.1:8000/mcp`), comandos `ModelContextProtocol.StartServer [port]/StopServer/RefreshTools/GenerateClientConfig <ClaudeCode|Cursor|VSCode|Gemini|Codex|All>`, tool-search (`list_toolsets/describe_toolset/call_tool`), solo HTTP+SSE, loopback sin auth. Repo skills `https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin`.
- Comunidad sin compilar C++: `https://github.com/FFZackFair92/unreal-engine-mcp` (Remote Control API + Python Editor Script Plugin, stdio→HTTP 30010, `ue_project_create`), `https://github.com/ATDev-Inc/uemcp` (`uvx uemcp`, cero install UE, 40 tools, `ue_python` escape hatch), `https://github.com/groscy/unreal-mcp` (Remote Execution 239.0.0.1:6766), `https://github.com/runreal/unreal-mcp` (`npx -y @runreal/unreal-mcp`), `https://github.com/erhansiraci/ue-mcp` (22 tools + 4 resources + 6 prompts), `https://github.com/ChiR24/Unreal_mcp` EngineWire (un tool `unreal` con `search/describe/execute/configure`, HTTP 3000 + WS 8090 + token).
- Twinmotion (cerrado, base UE, sin REST pública): solo `https://github.com/ScanBIM-Labs/twinmotion-mcp` remoto Cloudflare Workers + APS OAuth2 (`https://twinmotion-mcp.itmartin24.workers.dev/mcp`, mirrors `https://mcp.scanbimlabs.io/twinmotion`), 5 tools `tm_import_rvt/tm_set_environment/tm_render_image (hasta 8K)/tm_export_video (MP4/MOV/WebM)/tm_list_scenes`, auth `x-scanbim-api-key` o `Authorization: Bearer sk_scanbim_*`, créditos (50 free), latencia traducción 5-60 min, geometría vía OBJ para UE/Blender. No operable 100% local/offline.

### 5. Alternativas open-source gratuitas arq/viz — ventajas/limitaciones, docs, MCPs

- Blender 4.x + Bonsai (NativeIFC): ventaja modelado+documentación+4D/5D + Python total, costo 0, Linux Mint excelente; limitación curva aprendizaje, dibujo 2D legal débil vs AutoCAD (planos como docto legal Ley 24.335 → validar CPAU/MEPA). Docs `bonsaibim.org/studio.html`, OSArch. MCP `https://github.com/ahujasid/blender-mcp` (`uvx mcp-for-blender`, auto-setup clientes incl. OpenCode) + `zorak1103/blender-mcp` (HTTP 8400) + `djeada/blender-mcp-server` (22-27 tools) + `j4flmao/go_blender_mcp` (Go binario, config Opencode documentada) + `ricky-yosh/blender-mcp` (Godot export GLB).
- FreeCAD BIM workbench: ventaja paramétrico + TechDraw + IFC export + FEM; limitación UI fragmentada, renders básicos (derivar a Blender). Docs + videos `Video_tutorials_for_architectural_design` (Yorik van Havre playlists, Barcelona Pavilion 17 videos, Eklavya 11 videos).
- Godot 4.6 archviz realtime open (MIT): `https://github.com/Utopian-Academy/Genesis` (import GLB/FBX/OBJ/.blend + live link, OSM + foto aérea + sol real + 360/tours), `https://github.com/Naxela/Meridian` (Blender→Godot one-click, materiales/luces/cámaras/probes, bake Cycles, GDScript attach, export Win/Web/Android), `https://wiki.osarch.org/blender2godot/` (alpha GPL) + artículo `https://osarch.org/2023/01/22/the-potential-open-source-game-engine-for-blender-bim/`. MCP `https://github.com/Raunaksplanet/godot-mcp-server` (Node+WS+GDScript addon, 40+ tools, cita `opencode` explícito). Ventaja ejecutable standalone sin filtrar BIM, VR/Web; limitación sin GI pathtracing nivel UE, librería assets menor.
- Utilidades: `https://wiki.osarch.org/floss-visualisation-and-documentation/` (Material Maker, NeoTextureEdit, Poly Haven, ShareTextures), Sweet Home 3D + Blender workflow, Regard3D+Blender+FreeCAD fotogrametría.
- Comparativa rápida: fotorrealismo max UE5+Twinmotion (cerrado, gratis AEC pero no open) > Blender Cycles/Eevee (open, suficiente concurso/anteproyecto) > Godot (open, interactivo/web) > FreeCAD TechDraw (open, legal 2D).

### 6. MCPs operables desde Opencode (config probada vault)

- Opencode soporta `type:local/command[]/environment/cwd` y `type:remote/url/headers/oauth` (`https://opencode.ai/docs/mcp-servers/` 200 + `https://opencode.ai/docs/config/`). Vault usa `mcp` (no `mcpServers`), `command` array, `environment` (no `env`), ejemplo vivo `P:/00-repos/proyecto-pi/vault-arquitectura/opencode.json` (7 MCPs: comfyui local npx, autocad local exe, n8n/fathom/leantime/autodesk remote).
- Todos los MCPs stdio listados son operables: OpenSCAD (`uvx openscad-mcp` / `npx -y openscad-mcp-server` / `uv run`), FreeCAD (`uvx freecad-mcp` / `uvx cadpilot` / `python -m`), Rhino (`uvx rhinomcp@latest` / `uvx lamcp`), Bonsai (`uv run --directory /path/to/bonsai-mcp bonsai-mcp`), Blender (`uvx mcp-for-blender`), Godot (node build/index.js), Unreal (uvx uemcp / npx @runreal/unreal-mcp / HTTP proxy). Twinmotion solo `type:remote` + header API key.
- Patrón Opencode ejemplo: `{"mcp":{"openscad":{"type":"local","command":["uvx","openscad-mcp"],"enabled":true},"freecad-robust":{"type":"local","command":["uv","run","--directory","/path/to/freecad-addon","freecad-mcp"],"enabled":true},"bonsai":{"type":"local","command":["uv","run","--directory","/path/to/bonsai-mcp","bonsai-mcp"],"enabled":true},"twinmotion":{"type":"remote","url":"https://twinmotion-mcp.itmartin24.workers.dev/mcp","headers":{"x-scanbim-api-key":"{env:SCANBIM_KEY}"},"enabled":true}}}` — adaptar paths, no commitear secrets (usar `{env:VAR}` + global config).
- Atención contexto: MCPs grandes (245 tools Rhino, 150+ FreeCAD robust) consumen tokens → habilitar por agente (`tools: {"rhino*":false}` global + `agent: {arq:{tools:{"rhino*":true}}}`), ver docs Opencode Manage/Per agent.

## Fuentes APA idioma original + [trad. propia]

OFICIAL (10/10 200):
- OpenSCAD. (s.f.). Documentation. https://openscad.org/documentation.html [trad. propia — no oficial]
- OpenSCAD. (s.f.). Downloads. https://openscad.org/downloads [trad. propia]
- FreeCAD. (2026). Downloads (v1.1.4). https://www.freecad.org/downloads [trad. propia]
- FreeCAD Wiki. (s.f.). Download / Installing on Linux / Python scripting tutorial. https://wiki.freecad.org/Download/en [trad. propia]
- LibreCAD. (s.f.). Free Open Source 2D CAD. https://librecad.org/ [trad. propia]
- LibreCAD Docs. (s.f.). Download and Install. https://docs.librecad.org/en/latest/getstart/install.html [trad. propia]
- IfcOpenShell. (s.f.). IfcMCP. https://docs.ifcopenshell.org/ifcmcp.html [trad. propia]
- Bonsai. (s.f.). Beautiful, detailed, and data-rich OpenBIM. https://bonsaibim.org/ [trad. propia]
- Epic Games. (s.f.). Unreal MCP in Unreal Editor. https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor [trad. propia]
- OpenCode. (2026). MCP servers. https://opencode.ai/docs/mcp-servers/ [trad. propia]

COMUNIDAD/GitHub (verificado vía search, sin 404):
- Quellant / RobertCoop. openscad-mcp. https://github.com/quellant/openscad-mcp
- Petri Jr. openscad-mcp. https://github.com/petrijr/openscad-mcp
- Fboldo. openscad-mcp-server. https://github.com/fboldo/openscad-mcp-server
- Sergiu Danstan. openscad-mcp. https://github.com/sergiudanstan/openscad-mcp
- SpKane. freecad-addon-robust-mcp-server (255 stars). https://github.com/spkane/freecad-addon-robust-mcp-server
- Ahelja. FreeCAD-MCP (menciona opencode). https://github.com/ahelja/FreeCAD-MCP
- LBurny. cadpilot (`uvx cadpilot`). https://github.com/LBurny/cadpilot
- Neka-Nat. freecad-mcp. https://github.com/neka-nat/freecad-mcp
- Thebossnow. aiblueprint-mcp (ezdxf+LibreCAD). https://github.com/thebossnow/aiblueprint-mcp
- McNeel. RhinoAI. https://github.com/mcneel/RhinoAI
- Jingcheng Chen. rhinomcp. https://github.com/jingcheng-chen/rhinomcp/
- GenEnv. rhino-gh-mcp. https://github.com/GenEnv/rhino-gh-mcp/blob/main/README.md
- Gramazio Kohler. lamcp. https://github.com/gramaziokohler/lamcp
- Show2Instruct. bonsai-mcp. https://github.com/Show2Instruct/bonsai-mcp
- Show2Instruct. ifc-bonsai-mcp. https://github.com/Show2Instruct/ifc-bonsai-mcp
- Nhan Truong. bonsai-mcp (semántica IFC). https://github.com/nhantruong96/bonsai-mcp
- Epic Games. unreal-engine-skills-for-claude-code-plugin. https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin
- FFZackFair92. unreal-engine-mcp. https://github.com/FFZackFair92/unreal-engine-mcp
- ATDev-Inc. uemcp (`uvx uemcp`). https://github.com/ATDev-Inc/uemcp
- ScanBIM-Labs. twinmotion-mcp. https://github.com/ScanBIM-Labs/twinmotion-mcp
- Ahujasid. blender-mcp (`uvx mcp-for-blender`). https://github.com/ahujasid/blender-mcp
- Raunaksplanet. godot-mcp-server. https://github.com/Raunaksplanet/godot-mcp-server
- Utopian-Academy. Genesis (Godot archviz). https://github.com/Utopian-Academy/Genesis
- Naxela. Meridian (Blender→Godot). https://github.com/Naxela/Meridian
- OSArch. Bonsai / FLOSS Visualisation. https://wiki.osarch.org/bonsai/ ; https://wiki.osarch.org/floss-visualisation-and-documentation/

VIDEO (YouTube, sin transcript descargado — queda para @contenidos Fase 2):
- Yorik van Havre playlists — BIM Workbench / Barcelona Pavilion (17 videos). https://www.youtube.com/user/yorikvanhavre/playlists
- FreeCAD BIM Beginner Tutorials playlist. https://www.youtube.com/playlist?list=PL3wRqQUPtE16yw_c1TnRYJmz37y2ZRTLm
- Deltahedra. FreeCAD BIM - Architecture - Complete Beginner Tutorial (2025-01-24). https://www.youtube.com/watch?v=IV-nv9ygZPM
- Arif K. Rafiq. FreeCAD Part Scripting in Python Episode 025. https://www.youtube.com/watch?v=yp6yBTcdcII
- FinePointCGI (citado por OSArch) — Blender→Godot 4 Alpha workflow. Vía https://osarch.org/2023/01/22/the-potential-open-source-game-engine-for-blender-bim/

## Metodología queries por idioma + URLs + status + gaps

- ES: `FreeCAD official wiki documentation download install Windows Linux Mint` → 200 (8 resultados, 1 Anubis-block en Installing_on_Linux wiki, fallback a GitHub mirror 200)
- EN: `openscad.org documentation download manual language` → 200 (7)
- EN: `LibreCAD librecad.org wiki manual download install` → 200 (7, 1 404 `docs.librecad.org/` raíz, se usa `/en/latest/` 200)
- EN: `FreeCAD MCP server Model Context Protocol github` → 200 (8)
- EN: `Rhino Grasshopper MCP server Model Context Protocol github` → 200 (9)
- EN: `IfcOpenShell Bonsai BIM MCP server github` → 200 (7)
- EN: `Unreal Engine MCP server github Twinmotion` (2 intentos, 1 429 reintentado fast ok) → 200 (8+7)
- EN: `open source free architecture visualization Blender Godot archviz OSArch alternative` → 200 (8)
- EN: `FreeCAD Python scripting language C++ tutorial YouTube architecture BIM` → 200 (8)
- EN: `opencode MCP server configuration json open source how to add` → 200 (8)
- EN: `Blender MCP server opencode Claude Godot MCP server github` → 200 (8)
- EN: `OpenSCAD MCP server github` → 200 (8)
- EN: `LibreCAD MCP server github` → 200 (incluye issue LibreCAD #2577 con debate aiblueprint vs mcp_bridge)
- Webfetch 200: openscad.org/documentation.html, openscad.org/downloads, freecad.org/downloads, librecad.org, docs.librecad.org install, docs.ifcopenshell.org/ifcmcp, bonsaibim.org, opencode.ai/docs/mcp-servers, dev.epicgames unreal-mcp (9/9 + 1 truncado largo IfcMCP pero 200)
- Gaps: `datos insuficientes IT` (no se buscó IT, software anglo); sin MCP nativo LibreCAD vivo (solo ezdxf indirecto + fork TCP experimental); sin MCP local Twinmotion (solo remoto con créditos); versiones exactas OpenSCAD en Mint repos varían por release (verificar `apt policy openscad` en máquina); transcripts YouTube no descargados (yt-dlp es owner @contenidos, no sherlock); conteo estrellas GitHub volátil a fecha corte.

## Propuestas wiki (esqueleto, no crear)

- `wiki/glosario/software/openscad` (nueva) · `freecad` (actualizar BIM/Python) · `librecad` (nueva) · `bonsai`/`ifcopenshell` (nueva) · `rhino-grasshopper-mcp` · `unreal-engine-mcp` · `twinmotion` · `godot-archviz` · `blender-mcp` · concepto `mcp-opencode-arq`
- Destinos: [[wiki/glosario/software/comfyui|comfyui]] (patrón MCP ya usado) · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[wiki/glosario/conceptos/bim-metodologia|bim-metodologia]] · proyectos MVP Autocad/Comfy
- Dependencias vault: [[wiki/glosario/software/00-index|índice software]] · [[raw/contenidos/sherlock-cad-abierto-mcp-opencode|stub]] · `opencode.json`

¿Avanzo a curaduría? (s/N) para que @contenidos genere reporte legible raw/contenidos/ con ¿Avanzo a wiki?
