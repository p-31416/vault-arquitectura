---
tipo: indice
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-10-20
tags: [scripts, automatizacion]
---

# Scripts y automatizaciones

_Automatizaciones para gestión del vault y flujos de trabajo._

## Curación de contenido (YouTube/Chrome)

- `transcribir_youtube.py` — Transcript de un video YT a `raw/yt/transcripts/YYYY-MM-DD_<id>.<lang>.md+.srt+.txt+.origen.json` (.md = envoltorio visible en Obsidian con frontmatter; prefijo ISO = orden cronológico nativo; subs manuales→automáticos primero, fallback faster-whisper local si no hay). Limpieza de artefactos (NBSP, apóstrofes). Notas en `transcribir_youtube_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir_youtube.py <video_id|URL>`.

- `yt_takeout_parser.py` — Parsea Google Takeout (YouTube + Chrome) y genera un documento único con todos los videos guardados agrupados por lista + los canales fuera de scope para revisión. Salida: `raw/yt/videos-y-canales-guardados.md`. Notas en `yt_takeout_parser_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py`. Úsalo cada vez que exportes un Takeout nuevo.
- `yt_titles.py` — Completa título + canal + duración de los videos vía YouTube Data API v3. Cachea en `raw/yt/cache-titulos.json` (solo pide los IDs que faltan, así el gasto de cuota tiende a cero). Requiere `YOUTUBE_API_KEY` en `.env`. Guías: [[wiki/glosario/interno/youtube-data-api-key|youtube-data-api-key]]. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py`.
- `yt_revision.py` — Genera el archivo de revisión manual con SOLO lo pendiente: WL sin clasificar + canales fuera de scope, con columnas vacías para el veredicto del estudio. Salida: `raw/yt/revision-manual.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_revision.py`.
- `yt_creadores.py` — Cruza los canales de Watch Later con suscripciones: suscriptos en scope + creadores solo-WL (no suscriptos) con veredicto agregado + suscriptos fuera. Salida: `raw/yt/creadores.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_creadores.py`.
- `yt_build_index.py` — Genera el índice único `wiki/fuentes/00-index-yt.md` (3 vistas: por listado, por creador, por tag) filtrado por tag. Estado pendiente/procesado desde `raw/yt/index-state.json` (tras el OK, la ruta apunta a `wiki/fuentes/<slug>.md`). Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\yt_build_index.py [tag|all]`.

**Orden de ejecución tras un Takeout nuevo:**
```
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

## Utilidades

- `indice-renders-comfy.py` — Indexa los renders de ComfyUI **leyendo la metadata que el propio ComfyUI graba dentro de cada PNG** (bloques `tEXt` `prompt` y `workflow`): modelo, LoRA y strength, seed, sampler, scheduler, steps, cfg, resolución y prompt. Salida `INDICE-RENDERS.md` + `.json` en la carpeta indicada. Es lo que permite que cada render caiga solo en el índice/dashboard sin base de datos. Notas en `indice-renders-comfy_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\indexe-renders-comfy.py --dir "P:\00-repos\ComfyUI\output" --out "proyectos\MVP_04-comfyui-arquitectura" [--nombre INDICE-RENDERS] [--since YYYY-MM-DD]`.

- `calibrar-loras-comfyui.py` — **Calibra los LoRAs locales**: arma un grafo API por LoRA (CheckpointLoader → LoraLoader → CLIPTextEncode → KSampler → VAEDecode → SaveImage), lo manda a la API HTTP de ComfyUI (`POST /prompt`), espera el render, copia la imagen a `WF-loras-locales/salidas/n_01-G-NN.png` y registra LoRA × strength × seed × segundos × error en `PLANS/calibracion-loras.json`. Compara con seed y prompt fijos para que la diferencia entre imágenes **sea** el LoRA. Notas en `calibrar-loras-comfyui_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py [--solo SD1.5|SDXL] [--fuerzas 0.6,0.8] [--dry-run]`.

- `analizar-lora-safetensors.py` — Audita un `.safetensors` (LoRA o checkpoint) **sin PyTorch**: lee el header, deduce el modelo base (FLUX.2 klein 9B/4B, FLUX.1, dev) verificando los shapes contra las fórmulas del modelo, y revisa la salud de los pesos (en un LoRA la matriz B arranca en cero: si está vacía, el LoRA no aporta delta). Salida por consola + `--json` opcional. Notas en `analizar-lora-safetensors_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\analizar-lora-safetensors.py <archivo.safetensors> [--json SALIDA.json]`.

- `mux_lecciones_curso.py` — Extrae las **transcripciones de las lecciones del curso AI×Gaudí** (Archademy): lee el HTML guardado del área de participantes, empareja cada panel de módulo con su video (Mux) y baja los subtítulos `.vtt` (EN y ES, sin token) → `raw/yt/transcripts/YYYY-MM-DD_mux-<slug>.<lang>.md+.srt+.txt`. Deja además `indice-curso-ai-gaudi.json` con la URL y la contraseña del tablero Miro. Notas en `mux_lecciones_curso_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\mux_lecciones_curso.py "G:\Mi unidad\OS-Emilia\AIxGaudi\My account - Archademy.ai.html" [--out DIR]`.

- `transcribir-leccion-bunny.py` — Transcribe en local la lección del curso que **no tiene subtítulos** (el módulo 6, Round Table): lee el playback id en `indice-curso-ai-gaudi.json`, baja el video del CDN (con el `Referer` que exige), le saca el audio con ffmpeg y lo transcribe con faster-whisper en CPU → `raw/yt/transcripts/YYYY-MM-DD_mux-<slug>.<lang>.md+.srt+.txt`. El video y el audio quedan en `activos/curso-ai-gaudi/videos/`. Notas en `transcribir-leccion-bunny_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir-leccion-bunny.py --modulo round-table --language en`.

- `miro_board_inventory.py` — Inventario de un **tablero de Miro**: separa videos (con id de YouTube listo para transcribir), workflows de ComfyUI (`cloud.comfy.com` y `.json`), tableros, PDFs, modelos, tarjetas y módulos (frames). Dos modos: `--url` + token (`MIRO_ACCESS_TOKEN`, scope `boards:read`, paginación por cursor) o `--file` offline sobre lo exportado (CSV, backup `.rtb`/`.miro` o PDF). Notas en `miro_board_inventory_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\miro_board_inventory.py --url "https://miro.com/app/board/uXjVHRM2XQU=/" --token <token> [--out DIR]`.

- `archademy_curso_inventory.py` — Inventario del **área de participantes del curso AI×Gaudí** (login-gated): lista lecciones, videos, workflows, tableros Miro y PDFs. Dos modos: `--html` (guardar la página con `Ctrl+S` desde el navegador con sesión) o `--url` + `--cookies`/`--cookies-file` (cabecera Cookie de DevTools). Notas en `archademy_curso_inventory_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\archademy_curso_inventory.py --html "C:\descargas\curso.html" [--out DIR]`.

- `genera-template-set01.py` — Genera el DXF base del template SET_01-REP (29 capas, 8 estilos, 3 dimstyles, metros) para convertir a DWT/DWS vía ODA. Notas en `genera-template-set01_notas.md`. Uso: `python scripts\genera-template-set01.py`.

- `ordena-locales.py` — Ordena los locales del plano de replanteo en **orden de lectura** (filas ΔY < 0.30 m, de arriba hacia abajo; dentro de la fila, X creciente) y arma la planilla de locales. Lee el DWG vía ODA File Converter → DXF → `ezdxf` (o un `.dxf` directo). Salida: `docs/orden-locales.md`/`.csv` + `docs/cuadro-locales.md`/`.csv`. Con `--check` solo **verifica** que la numeración `N_LOC` de los bloques `SIMB-LOC_ID` coincida con el orden de lectura (no escribe archivos). Uso: `C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\ordena-locales.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" [--check] [--tol 0.30] [--salida DIR]`. **Requiere `ezdxf`** → va con el **Python 3.12 del sistema** (donde está `ezdxf` 1.4.4), no con `comfyenv` (ese es de ComfyUI).

- `chequea-lisp.py` — Valida que un `.lsp` tenga los paréntesis balanceados (ignora comentarios y cadenas) y lista los comandos `c:` definidos. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\chequea-lisp.py <archivo.lsp>`.

- `inventario-hardware.ps1` — Relevamiento Semana 0 (Vault Cerebro): CPU, RAM por slot, GPU + VRAM real (WMI), discos, monitores EDID, red, Python/Git/Node/VSCode/OpenCode, ComfyUI (`P:\00-repos\ComfyUI`), CAD/BIM instalado. Salida: consola + `.md` + `.json` en `raw/sessions/`. Uso: `powershell -ExecutionPolicy Bypass -File scripts\inventario-hardware.ps1`.

## Studio OS (MVP_07)

- `studio_os_verificar_vps.py` — **Solo lectura**: inventaría el VPS por SSH (alias `contabo`) y devuelve RAM total/usada/disponible, swap, disco, carga, memoria por contenedor y un **veredicto** sobre si entran los 3 GB de Hermes con margen. No instala ni reinicia nada. Notas en `studio_os_verificar_vps_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py [--host contabo] [--json SALIDA.json]`. Es el **primer paso de F0**: deja el baseline antes de meter el agente ([[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|documento maestro]] §8.1).

- `studio_os_publicar_hermes.py` — Extrae del **documento maestro** (§9.2 `SOUL.md` y §9.3 skill, marcados con `<!-- archivo: ... -->`) los archivos de texto que el agente necesita y los publica dentro del contenedor por SSH. Resuelve el ID real del contenedor (en Swarm se llaman `servicio.1.tarea`), escribe con `docker exec -i ... cat >` y verifica. Notas en `studio_os_publicar_hermes_notas.md`. Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_publicar_hermes.py [--host contabo] [--dry-run]`.

## Pendientes
- [ ] `studio_os_migrar_sql.py` — aplica el DDL del schema `studio_os` en el Postgres del VPS (F1)
- [ ] `studio_os_contrato_validar.py` — valida el sobre de tarea (JSON Schema + reglas verbo→riesgo) (F1)
- [ ] `studio_os_registry.py` — API del registro, escritor único (F1)
- [ ] `studio_os_runner.py` — API de tareas del runner, con control de riesgo del lado que ejecuta (F2)
- [ ] `studio_os_vault_mcp.py` — MCP del vault: leer, buscar, índice; escribir solo con aprobación (F1)
- [ ] `studio_os_pod_runpod.py` — crea/detiene/borra el pod GPU con el perfil acordado (F4)
