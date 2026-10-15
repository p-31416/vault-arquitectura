# Spec — Vista gráfica del índice YouTube (notas atómicas + grafo Obsidian)

_Fecha: 2026-10-09 · Estado: simplificado — solo vista gráfica · Piloto: comfyui (71 videos) · Base: `wiki/fuentes/00-index-yt.md`_

## 1. Objetivo

`wiki/fuentes/00-index-yt.md` hoy trae 3 vistas en tabla (por listado, por creador, por tag). Todo el piloto es `comfyui`. Quiero ver esas 3 vistas como grafo en Obsidian, con la misma info, en forma de nodos y links.

## 2. Diseño mínimo

### Notas a generar en `wiki/fuentes/yt/`

| Nota | Ruta | Contenido |
|---|---|---|
| Video | `<video_id>.md` | Frontmatter: tipo, video_id, titulo, creador, url (verificada 200 OK), fecha_video, fecha_ingesta, tags, estado ⏳/✅ + links a su creador y a todos sus tags |
| Tag | `tag-<slug>.md` | 1 línea + lista de videos linkeados |
| Creador | `creador-<slug>.md` | Canal + lista de videos linkeados |

Malla completa: cada video linkea a `[[creador-<slug>]]` + a cada `[[tag-<slug>]]`. Con eso el grafo arma los 3 cortes: listado = todos los nodos video, creador = cúmulos por creador, tag = cúmulos por tag.

Ejemplo con 2 filas reales:

`JWln_5jm4Ic.md` linkea `[[tag-comfyui]] [[tag-nanobanana]] [[creador-comfyui]]`
`WFHlgwl6jno.md` linkea `[[tag-comfyui]] [[tag-blender]] [[creador-comfyui]]`

### Cómo se ve en Obsidian

1. Abro vault `P:\00-repos\proyecto-pi\vault-arquitectura`
2. `Ctrl+G` grafo → filtro `path:wiki/fuentes/yt`
3. Groups por color: `comfyui` naranja, resto por tag
4. Resultado: 1 cúmulo grande comfyui (71), con sub-cúmulos por tag y por creador visibles al hacer zoom

### Cómo se genera

Script `yt_build_notes.py`: lee `wiki/fuentes/00-index-yt.md` + `raw/yt/index-state.json` y genera las notas. La ingesta queda intacta, solo derivo vistas. Todo regenerable: ante diferencia, manda el índice y se regenera.

## 3. Done

Con filtro `path:wiki/fuentes/yt` veo: todos los videos como nodos, agrupados por tag y por creador, con colores. Captura en cierre como evidencia.

## 4. Alcance

Solo vista gráfica del índice actual. Curaduría y Fase 2 web quedan para ciclos siguientes, con propuesta dedicada.

## 5. Pendiente (2026-10-09 — probar luego)

### Cómo abrirlo en el VR (Quest)

1. En PC (misma WiFi que el Quest), serví la carpeta:
   `P:\Anaconda\envs\comfyenv\python.exe -m http.server 8000 --directory scripts`
2. Averiguá la IP de la PC (`ipconfig` → IPv4, ej. `192.168.1.50`).
3. En Quest Browser abrí: `http://TU-IP-PC:8000/grafo-yt-vr.html`.
4. Tocá **Enter VR**. Controles: gatillo = clic/arrastrar nodo, grip + mover = rotar, joystick = volar.
5. Modos: navegar / agregar (gatillo al vacío crea `investigar-N`) / linkear (gatillo en A + gatillo en B). Renombre con `id | nombre`. Botón **ver JSON** para copiar al vault.

- [ ] Probar `scripts/grafo-yt-vr.html` en Quest Browser (Enter VR) con servidor local. Versión editable: 3 modos (navegar / agregar / linkear con gatillo), renombre `id | nombre`, export JSON, persistencia en localStorage del Quest.
- [ ] Abrir el grafo en Noda VR vía CSV: generar `noda-yt.csv` (nodos = videos + tags + 1 nodo por tema a investigar; links = video→tag) e importar desde Drive o por USB-C en `\Android\data\com.codingleap.noda\files` (requiere versión paga para CSV — queda como vía paga, NO prioritaria). Ref: `https://noda.io/documentation/csv.html`.
- [ ] Vía gratuita open source (prioritaria): `scripts/grafo-yt-vr.html` (A-Frame + 3d-force-graph-vr, MIT) en Quest Browser + plugin Obsidian 3D Graph en PC. Cero costo, mismo JSON.
- [ ] Sembrar nodos `Tipo: investigar` (ej. `4K entrega final`, `puente comfyui+blender`, `workflow arq img2img`) para navegar con guía en vez de arrancar de cero.
