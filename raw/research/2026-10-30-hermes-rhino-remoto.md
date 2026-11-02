---
tipo: research
fecha: 2026-10-30
slug: hermes-rhino-remoto
idioma: ES/EN
fuentes_n: 26
confianza: Alta (McNeel + MCP spec + Tailscale + PyPI/GitHub) / Media (casos comunitarios) / Baja (SSH reverso sin fetch, precio VPS Contabo no investigado)
tags: [sherlock, hermes, rhino, rhino-compute, hops, mcp, tailscale, vps, earth2rhino]
---

# 2026-10-30 — Hermes (VPS Contabo Docker) + Rhino 8 en PC: ¿puede un agente remoto usar Rhino desktop?

Fecha|Fuentes N|Confianza: 2026-10-30|26 (14 fetch 200 + 12 snippets)|Alta en oficial McNeel/MCP/Tailscale/PyPI, Media en casos comunitarios, Baja en SSH reverso (sin fetch) y costos Contabo (fuera de alcance)

## Resumen

- Sí, es posible, pero **Rhino solo existe en la PC**: el VPS nunca corre Rhino desktop. El agente Hermes en Docker debe hablar por red con algo que sí corre en la PC.
- `reer-rhino-mcp` (el que usa earth2rhino hoy) solo ofrece **stdio + SSE en `127.0.0.1:8080`**, ambos pensados para **localhost**. No documenta Streamable HTTP ni auth/TLS. Exponerlo directo a internet = no dicho / inseguro. Verificado en README (fetch 200).
- Camino oficial headless de McNeel: **Rhino.Compute** (servidor HTTP con Rhino.Inside, 2400+ llamadas RhinoCommon, librerías py/js/.NET) + **Hops** (componente Grasshopper que oficia de cliente). En PC Windows con licencia normal cuesta $0; en Windows Server/VM cloud cobra **$0.10/core/hora por uptime** (`RHINO_TOKEN`). No corre en macOS.
- Patrón más simple para arrancar (preferencia del estudio): **A. puente expuesto por red privada (Tailscale Serve)** — la PC publica `localhost:9876` solo dentro del tailnet, el contenedor Hermes en el VPS se une al mismo tailnet y llama como si fuera LAN. Sin abrir puertos públicos, con identity headers y ACLs.
- Alternativas: **B. runner con cola en la PC** (la PC hace polling al VPS, cero puertos entrantes, la más robusta en redes de estudio/CGNAT) y **C. Rhino.Compute headless** (la más potente para escalar, pero exige IIS + API key + HTTPS + billing si sale de la PC).
- Lección junio 2026 (ecosistema Nous Hermes Agent, **no** el Hermes propio de Studio OS): desde el hardening de junio 2026 `--insecure` **ya no desactiva auth**; todo bind no-loopback exige provider (password u OAuth) y falla cerrado si no hay. Sirve como norma para el puente earth2rhino: nunca exponer MCP/dashboard sin auth, y si es solo red privada, bindear a `127.0.0.1` + Tailscale.
- Límite duro: **extruir footprints OSM + guardar .3dm puede ser headless**; **viewport/captura/`Redraw`/`rs.Command` con interacción UI/selección en pantalla exigen desktop abierto**.

## Ejes

### 1. `reer-rhino-mcp`: transportes y exposición en red

- Paquete PyPI `reer-rhino-mcp` (REER INC, mantenedor `shaw_c`, Python >=3.10, MIT, última 0.1.10; versiones 0.1.1/0.1.6/0.1.7 vistas). Repo `github.com/reer-ide/rhino_mcp`. Requiere Rhino 7+. Instalación `uvx reer-rhino-mcp` + `rhino_script.py` dentro de Rhino (Tools > Script > Run en Rhino 8). [trad. propia — no oficial]
- Arquitectura en dos piezas: (a) script lado-Rhino que levanta un **socket server** que recibe y ejecuta comandos; (b) **MCP Server (`rhino_mcp/server.py`)** que implementa MCP y se conecta a ese script. Herramientas: `get_rhino_scene_info`, `get_rhino_layers`, `execute_code` (Python arbitrario en Rhino), `get_rhino_objects_with_metadata`, `capture_rhino_viewport`, `get_rhino_selected_objects`, `look_up_RhinoScriptSyntax`.
- Dos implementaciones, ambas **locales**:
  - **stdio** para Claude Desktop (`"command": "uvx", "args": ["reer-rhino-mcp"]`).
  - **SSE** alternativo para web clients: corre en **`127.0.0.1:8080`**, conectar a `ws://127.0.0.1:8080/sse`, mensajes a `http://127.0.0.1:8080/messages/`, vía `python -m rhino_mcp.server_sse`. Soporta las mismas ops que stdio.
- **No dicho**: el README no menciona Streamable HTTP, ni auth, ni TLS, ni bind `0.0.0.0`, ni `allow-external`, ni `Origin`/DNS-rebinding. Tampoco documenta exponer el socket Rhino por red. Menciona `supergateway` solo como puente stdio<->SSE.
- Consecuencia: tal como está documentado, `reer-rhino-mcp` **no se puede exponer en red de forma segura por sí solo**; necesita una capa (Tailscale Serve, túnel SSH, o reemplazarlo por un servidor con HTTP + auth).
- Dato útil: el puente propio del estudio (`scripts/rhino-mcp-server-rhino.py` en `localhost:9876` + `scripts/rhino-mcp-cli.py` por stdio) replica el mismo patrón socket-local; el puerto 9876 es el que habría que publicar por red privada, no el stdio.

### 2. Rhino.Compute (headless autohospedable) + Hops

- **Qué es**: servidor web que expone la geometría de Rhino (vía Rhino.Inside) por **HTTP/HTTPS**; cualquier app que haga web requests lo usa. Resuelve definiciones Grasshopper en serie/paralelo y en background asíncrono sin congelar la UI. [trad. propia]
- **Dónde corre**: solo **Windows y Linux** (testeado Ubuntu 24.04, AmazonLinux 2023) vía Rhino.Inside; **no macOS**. Local en PC Windows o en servidor/VM.
- **API que expone**: REST stateless con 2400+ llamadas RhinoCommon (puntos, curvas, superficies, sólidos, meshes,Closest point, intersecciones, meshing, booleanas, área/masa). Librerías: `compute-rhino3d` (Python `pip install compute-rhino3d` + `rhino3dm`), JS, .NET. Endpoints documentados: `/io` + `/solve` (Hops), `/version`, `/recycle-children`, `/launch-children`, `/plugins/gh|rhino/installed`, compresión gzip (builds >=2026-10-13), límite body ~50 MB (`RHINO_COMPUTE_MAX_REQUEST_SIZE`), timeout configurable (`RHINO_COMPUTE_TIMEOUT`).
- **Licencia/costo**: en PC normal usa la **licencia Rhino existente (incluye evaluation), $0 extra**. En **Windows Server** (o Linux Server) exige **Core-Hour Billing: $0.10 por core por hora por uptime (prorrateo por minuto)**, no por uso. Ejemplo oficial: 1 máquina 2 cores 8h/día 30 días = $48/mes; N instancias en misma máquina cuestan igual. Requiere team Cloud Zoo **sin licencias**, tarjeta, `RHINO_TOKEN` como env (`[System.Environment]::SetEnvironmentVariable('RHINO_TOKEN',...)`). Single-computer keys no valen en Server. `idlespan` 1h apaga hijos para ahorrar billing. Dato Brian Gillespie (foro): si Compute corre en la misma máquina que lo pide (Hops local), vale licencia normal; si otra máquina lo llama, va a core-hour.
- **Hops**: componente Grasshopper (Rhino 7/8 Windows, PackageManager `Hops`, pestaña Params > Util) que convierte .gh en **funciones** (inputs = componentes Get con nombre, outputs = Context Bake/Print). Al resolver, envía la definición a un Rhino headless (Compute) y devuelve el resultado. Soporta paralelo por rama DataTree, async sin bloquear UI, caché en memoria y en servidor, `Max Concurrent`, `Child Process Count`. Settings: URL servidor + `API key` (`RhinoComputeKey` header). Por defecto local; para remoto seguir guía `deploy-to-iis`. En macOS no hay Compute local: o REST a Windows remoto o servidor CPython `ghhops_server`.
- **¿Sirve para extruir massing sin abrir desktop?**: sí para la parte geométrica. Compute puede manipular 3DM y correr operaciones Grasshopper/Python sin UI. **No dicho** en la doc un ejemplo "OSM→extrusión" literal, pero la tabla de features (booleanas, extrusiones vía API, AreaMassProperties) lo cubre como capacidad.
- **Seguridad en producción (checklist oficial)**: `RhinoComputeKey` largo y secreto (nunca en páginas/repos), **HTTPS** (por defecto HTTP :80, no mandar key sin TLS), firewall (abrir 80/443 solo a IPs necesarias, RDP solo a IP propia), mantener `--block-private-urls`, no `RHINO_COMPUTE_DEBUG` en internet (filtra stack traces), actualizar (Rhino 7 + .NET5 ya sin parches → migrar a 8), guardar `RHINO_TOKEN` como secreto.

### 3. Patrones "agente cloud (VPS Docker) → Rhino en PC"

#### A. Puente por red privada (Tailscale / WireGuard / ZeroTier) — recomendado arrancar

- **Qué instalar en la PC**: Tailscale + Rhino 8 abierto + puente (`rhino-mcp-server-rhino.py` escuchando `127.0.0.1:9876`). En la PC correr `tailscale serve 9876` (o `tailscale serve --tcp` según protocolo). El servicio queda en `https://<device>.<tailnet>.ts.net` solo dentro del tailnet, con TLS y MagicDNS automáticos.
- **En el VPS**: Tailscale en el contenedor/host (sidecar o `tailscaled`), unido al mismo tailnet con ACLs que solo permitan VPS→PC:9876. Hermes llama a la URL tailnet como si fuera localhost.
- **Tráfico/puertos**: sin abrir puertos públicos; todo va por WireGuard UDP (NAT traversal). DNS restringido a `<tailnet>.ts.net`. Mismo puerto no puede ser Serve (privado) y Funnel (público) a la vez.
- **Riesgos**: si se usa **Funnel** (público) por error, cualquiera con la URL accede — la doc advierte no usarlo para datos sensibles. Con Serve, usar **identity headers** (`Tailscale-User-Login/Name`) y **best practice bindear el backend solo a localhost** para evitar spoofing directo. Regla MCP spec: validar `Origin`, bindear `127.0.0.1`, exigir auth.

#### B. Runner con cola en la PC (polling al VPS)

- **Idea**: invertir la dirección. El VPS expone una cola/API (ej. endpoint Hermes + tabla de jobs); un **worker Python en la PC** hace polling cada N seg, descarga el job (GeoJSON footprints + alturas), lo ejecuta en Rhino desktop abierto (vía `rhino-mcp-cli.py` / `execute_code` / puente :9876), sube el `.3dm`/reporte.
- **Qué necesita en la PC**: Python + Tailscale (o HTTPS saliente, sin inbound), Rhino 8 abierto logueado, worker como servicio/tarea programada. En el VPS: cola + storage + token por job.
- **Puertos/tráfico**: **cero puertos entrantes** en la PC (solo HTTPS saliente al VPS, NAT/CGNAT-friendly). Ideal en redes de estudio con firewall ajeno.
- **Riesgos**: menor superficie (no expone Rhino), pero hay que autenticar el worker (token por máquina, rotación), firmar jobs, y vigilar reintentos/idempotencia. Latencia de polling (segundos). **No verificado con fuente oficial única en esta ronda — patrón arquitectónico estándar, no dicho como "producto"**.

#### Túnel SSH reverso (variante rápida)

- `ssh -R 9876:localhost:9876 vps` desde la PC expone el puente en el VPS como localhost. Necesita solo OpenSSH + key en la PC, sin Tailscale. Riesgo: si el VPS se compromete, el túnel es puerta a la PC; exige `GatewayPorts no`, key dedicada, `autossh`/servicio, y firewall en VPS. **No fetch de doc oficial en esta ronda — no dicho, gap explícito**.

#### C. Hops/Compute remoto

- **En la PC**: instalar Rhino.Compute (bootstrap `deploy-to-iis`), IIS, `RhinoComputeKey`, HTTPS (`configure-compute-for-https`), firewall solo IP del VPS, `--block-private-urls`, `RHINO_TOKEN` solo si fuera Server (en PC Win normal no hace falta).
- Hermes (Python `compute-rhino3d`) llama `Util.url = "https://pc.tailnet:443/" + apiKey`, o Hops apunta al servidor remoto. Para Grasshopper puro, el .gh de massing (inputs: curvas footprint + altura) se resuelve headless.
- **Riesgos**: los del checklist McNeel + billing por uptime si se mueve a Server. Debug/gzip/timeout tunables.

#### Riesgo transversal: dashboards/MCP expuestos (junio 2026)

- Docs Nous Hermes Agent (ecosistema **distinto** al Hermes Studio OS, se cita como lección): tras el **hardening junio 2026**, `--insecure` es **no-op**; todo bind no-loopback (`0.0.0.0`/LAN) **engancha auth gate** (password u OAuth) y **falla cerrado** (no arranca) si no hay provider. Password solo para red confiable/VPN, nunca internet directo. `GET /api/status` es pública pero `/api/ws` y `/api/pty` exigen ticket. Guías comunitarias (sudolabs 2026-06-03, nyagah.me 2026-06-26) recomiendan Tailscale + `--host 0.0.0.0` + token pineado, o `127.0.0.1` + túnel.
- **No encontrado**: fuente de un "incidente dashboards Hermes expuestos junio 2026" como breach concreto. Solo hardening + guías de exposición segura. Se marca como **sin fuente encontrada / no dicho** si se buscaba breach.

### 4. Cómo lo resuelven otros proyectos agénticos con Rhino (máx. 3, con link)

1. **`rhino3dm-mcp` (EaseHee, PyPI 0.6.0, 2026-05-20)** — el más cercano a lo pedido. Tres transportes: **stdio, Streamable HTTP, Docker/TCP**. Modo standalone (rhino3dm, sin Rhino, ~242 tools, edita .3dm) + modo bridge (plugin C# en Rhino 8, TCP `:4242`/named pipe/unix socket, ~245 tools, RhinoCommon+Grasshopper+Roslyn/C#). Comandos: `rhino-mcp --transport http --host 127.0.0.1 --port 8765` (dev) vs `--host 0.0.0.0 --port 8765 --allow-external --stateless` (claude.ai remote, solo tras túnel ngrok/Cloudflare; `--allow-external` desactiva protección DNS-rebinding). Registro por capacidad (si no hay bridge, no registra tools bridge). Repositorio `github.com/EaseHee/rhino-mcp`.
2. **RhinoAiMCP (Food4Rhino, 39.8k descargas)** — plugin Rhino 7/8 Win/Mac, MCP server **dentro** de Rhino, V2 nativa con skills 3D/2D + componentes GH, multi-agente. Conexión vía `mcp-remote http://127.0.0.1:3001/mcp` (Claude Desktop `npx mcp-remote`). Todo documentado como localhost; para remoto exige la misma capa (VPN/túnel).
3. **RhinoAI oficial McNeel (Rhino-MCP-Platform, Rhino 9 `AI` + `MCPConnect`)** — dos modos: **dentro** (panel chat dockeado, usa selección y pantalla) y **fuera** (MCP server, `MCPConnect`, el asistente puede lanzar/reiniciar Rhino, manejar varias sesiones 8/9 a la vez, abrir/guardar/switch files, sobrevivir a crash vía router, combinar con otras tools). Open source MIT (`mcneel.github.io/RhinoAI`). Sigue exigiendo Rhino en la máquina local; para VPS vale el mismo patrón red privada/cola.

### 5. Límites duros: qué exige desktop vs qué puede ser headless

- **Exige desktop abierto (display)**: `capture_rhino_viewport` / screenshots (`rhino_screenshot`), `Redraw`, pipeline `Rhino.Display`, `GetGumballPlane`, comandos con interacción UI (`CRhinoGetString` sin command line falla — foro Rhino.Inside C++ 2025-08-07: "there is no Rhino UI for command to interact with"), `rs.Command` con prompts, selección en pantalla, render a viewport, `DrawViewportWires/Meshes` previews de GH. Eventos estáticos no se lanzan para headless salvo watcher con `includeHeadlessDocuments:true`, y en hilo no-UI (exige thread-safety, no asumir UI thread).
- **Puede ser headless**: crear geometría (puntos/curvas/sólidos/extrusiones/booleanas), `RhinoDoc.CreateHeadless(template)` / `OpenHeadless(path)` (desde 7.0; overload con `ArchivableDictionary` desde 8.21), importar/guardar `.3dm` (`FileIO`, `SaveAs`), medir (`AreaMassProperties`, `VolumeMassProperties`, `rhino_schedule_by_layer`), manipular capas/materiales/user-text, correr definiciones GH vía Compute (`/solve`). `rhino3dm` standalone incluso edita `.3dm` sin Rhino.
- **Zona gris earth2rhino**: descargar OSM/Overpass + proyectar a EPSG:25831 + extruir + guardar = **headless OK (puede correr en VPS o en Compute)**. `BoundingBox` geométrico OK headless; `CustomRenderMeshesBoundingBox(viewportInfo,...)` necesita viewport = desktop. `shot`/viewport = desktop. `rs.Command("Make2D"/"Render"/...)` = desktop (usa doc activo/display). Regla: si la llamada toca `ActiveDoc`/`ActiveSpace`/viewport/display, desktop; si toca `Rhino.Geometry`/`File3dm`/headless doc, headless.

## Fuentes (APA, idioma original + [trad. propia])

- REER, INC. (2025). *RhinoMCP — Rhino Model Context Protocol Integration* (README). Código y PyPI `reer-rhino-mcp`. [Fuente EN; trad. propia al ES en ejes 1] — https://github.com/reer-ide/rhino_mcp/blob/main/README.md — status 200 verificado 2026-10-30 vía webfetch.
- Python Software Foundation. (2025). *reer-rhino-mcp · PyPI* (versiones 0.1.1/0.1.6/0.1.7/0.1.10, MIT, Python >=3.10). [EN; trad. propia] — https://pypi.org/project/reer-rhino-mcp — status 200 (search excerpt).
- Payne, A. (2026). *Frequently Asked Questions — Rhino.Compute*. McNeel Developer Docs. [EN; trad. propia] — https://developer.rhino3d.com/guides/compute/compute-faq — 200.
- Gillespie, B. (2026). *Licensing & Billing — Core-Hour Billing ($0.10/core/hour)*. McNeel Developer Docs. [EN; trad. propia] — https://developer.rhino3d.com/guides/compute/core-hour-billing — 200.
- Baer, S., Davidson, S., & Payne, A. (2024). *The Hops Component*. McNeel Developer Docs. [EN; trad. propia] — https://developer.rhino3d.com/guides/compute/hops-component — 200.
- Payne, A. (2022). *What is Hops* + *How Hops Works*. McNeel Developer Docs. [EN; trad. propia] — https://developer.rhino3d.com/guides/compute/what-is-hops/ — 200 (search).
- McNeel. (s.f.). *RhinoDoc.CreateHeadless / OpenHeadless (API RhinoCommon)*. [EN; trad. propia] — https://developer.rhino3d.com/api/rhinocommon/rhino.rhinodoc/createheadless y .../openheadless — 200 excerpt.
- McNeel Forum — Dale F. (2025). *SDK Rhino.Inside C++: ExecuteCommand() and headless mode* (sin UI no hay command line). [EN; trad. propia] — https://discourse.mcneel.com/t/sdk-rhino-inside-c-executecommand-and-headless-mode/208135 — 200.
- Model Context Protocol. (2026). *Streamable HTTP (spec 2026-07-28): Origin MUST 403, SHOULD localhost, SHOULD auth*. [EN; trad. propia] — https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http — 200.
- Model Context Protocol / Python SDK. (s.f.). *Authorization — MCP server as OAuth 2.1 resource server; stdio has no Authorization header*. [EN; trad. propia] — https://py.sdk.modelcontextprotocol.io/v2/run/authorization — 200 (search).
- Tailscale. (2026). *Tailscale Serve* (tailnet privado, `tailscale serve 3000`, identity headers, localhost-only best practice, Serve vs Funnel). [EN; trad. propia] — https://tailscale.com/docs/features/tailscale-serve — 200.
- EaseHee. (2026). *rhino3dm-mcp 0.6.0 · PyPI* (stdio/Streamable HTTP/Docker-TCP, bridge TCP :4242, standalone/bridge). [EN; trad. propia] — https://pypi.org/project/rhino3dm-mcp/ — 200.
- RhinoAiMCP. (2025). *Food4Rhino page* (`mcp-remote http://127.0.0.1:3001/mcp`, Rhino 7/8). [EN; trad. propia] — https://www.food4rhino.com/en/app/rhinoaimcp — 200 (search).
- McNeel. (2026). *Rhino & Artificial Intelligence / RhinoAI (AI + MCPConnect, multi-sesión, sobrevive crash)*. [EN; trad. propia] — https://www.rhino3d.com/for/ai y https://www.rhino3d.com/new-source/features/rhino-ai/ — 200 (search).
- Nous Research. (2026). *Hermes Web Dashboard (auth gate, --insecure no-op desde junio 2026, fail-closed)*. [EN; trad. propia; ecosistema distinto a Studio OS Hermes] — https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard — 200.
- Nous Research. (2026). *hermes-agent SECURITY.md (loopback vs --host 0.0.0.0, allowlist, no exponer sin VPN/firewall)*. [EN; trad. propia] — https://github.com/NousResearch/hermes-agent/blob/main/SECURITY.md — 200 (search).
- Sudolabs / Nyagah, A. (2026-06). *Cómo conectar Hermes Desktop a backend remoto vía Tailscale (pin token, --host 0.0.0.0, --insecure)*. [EN; trad. propia] — https://sudolabs.nz/blog/how-to-connect-the-hermes-desktop-app-to-a-remote-hermes-backend-the-clean-way y https://nyagah.me/articles/hermes-desktop-tailscale — 200 (search).

## Metodología

- Queries ES/EN (IT n/a: docs McNeel/MCP/Tailscale solo EN): `reer-rhino-mcp github/PyPI`, `Rhino.Compute docs headless`, `Hops remote solve`, `Rhino MCP remote agent`, `Tailscale expose localhost`, `Core-Hour Billing`, `MCP Streamable HTTP auth`, `Rhino headless limitations`, `"Hermes" dashboard junio 2026`. 2-3 variaciones × eje, 26 URLs únicas.
- Verificación: webfetch a README reer, compute-faq, core-hour-billing, hops-component, streamable-http spec, tailscale-serve, pypi rhino3dm-mcp, hermes dashboard. Resto vía search excerpts oficiales. Sin 404 en citados. Descartados: 0 (todos 200/excerpt válido).
- Gaps: (a) SSH reverso sin fetch oficial — no inventar flags; (b) costo Contabo/VPN no investigado; (c) breach "dashboards Hermes expuestos junio 2026" sin fuente — solo hardening; (d) `reer-rhino-mcp` no documenta auth/TLS/remoto — no dicho; (e) IT sin fuentes.

## Propuestas wiki (esqueleto, no escribir)

- `hermes-rhino-remoto` (nueva, software/infra): A/B/C + decisión + checklist seguridad (key, HTTPS, firewall, localhost-only).
- `reer-rhino-mcp` (nueva o § en `rhino`): stdio + SSE 127.0.0.1:8080, socket-local, sin auth — no exponer directo.
- `rhino-compute` (§ en `rhino`): REST + billing $0.10/core/h + Hops como cliente.
- `tailscale-serve-estudio` (nueva o § en `tailscale`): `serve` vs `funnel`, identity headers.
- Concepto `agente-cloud-rhino-local` (nueva): runner/cola vs puente vs Compute.

## Tabla comparativa — 3 arquitecturas

|  | A. Puente por red privada (Tailscale Serve) | B. Runner con cola en la PC | C. Rhino.Compute headless |
|---|---|---|---|
| **Qué es** | PC publica `localhost:9876` solo en tailnet; Hermes (VPS Docker) lo llama como LAN | Worker en PC hace polling a cola del VPS, ejecuta en Rhino desktop, sube .3dm | Rhino.Compute (IIS + API key + HTTPS) en PC/VPS; Hermes llama REST `/solve` |
| **Pro** | Mínimo cambio (mismo puente), sin puertos públicos, TLS+ACL gratis, latencia baja | Cero inbound (CGNAT/firewall OK), más robusta, auditable por jobs | Oficial McNeel, paralelo/async, escala, sin desktop para geometría |
| **Contra** | Requiere Tailscale en VPS+PC; si PC duerme/apaga, cae; SSE/puente sin auth sigue confiando en tailnet | Hay que programar worker+cola+reintentos; latencia polling; desktop debe estar abierto igual | Más piezas (IIS, certs, key, plugins para RhinoComputeUser); billing si sale a Server; viewport/render siguen desktop |
| **Costo** | $0 (Tailscale free/personal; licencia Rhino existente) | $0 (solo dev worker) | PC local $0; en Server $0.10/core/h uptime (~$48/mes 2c 8h×30d) + VM |
| **Complejidad** | Baja (instalar Tailscale, 1 comando serve, ACL) | Media (cola + worker servicio + tokens) | Alta (deploy-IIS, HTTPS, key, logs, update) |
| **Seguridad** | Alta si Serve (privado) + backend localhost-only + no Funnel; validar Origin/auth a nivel app | Alta (sin inbound; auth worker→VPS por token; firmar jobs) | Alta si checklist McNeel (key, HTTPS, firewall, block-private-urls, no DEBUG, secreto RHINO_TOKEN) |
| **Sirve earth2rhino hoy** | Sí directo (Overpass en VPS o PC + extruir vía puente) | Sí (job = bbox+alturas → .3dm) | Sí parcial (extruir/guardar headless; captura/Redraw desktop aparte) |

**Recomendación (simple primero)**: arrancar con **A. Tailscale Serve** para el piloto (1 PC + 1 VPS, mismo tailnet, `tailscale serve 9876`, Hermes por URL tailnet, nada público). En paralelo diseñar **B** como destino (worker/cola) cuando haya 2+ PCs o red de estudio restrictiva. **C** solo si el massing se vuelve servicio (múltiples concursos, paralelo, sin depender de una sesión desktop).

---
*Fuentes verificadas 200 el 2026-10-30. "No dicho" marca capacidad no documentada. Timezone -03:00 America/Argentina/Buenos_Aires.*
