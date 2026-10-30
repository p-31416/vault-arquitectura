# 2026-10-30 — Tablero del curso AI×Gaudí + notas en el canvas + img2img Sagrada Familia

## Qué se hizo

- **Tablero del curso** (`scripts/dashboard-curso.py` + notas): genera `activos/web/galeria/curso.html` con el formato v2 de la galería (mosaico, lienzo, facetas, Polaroid, auto-refresh) pero con fuente curada — **solo las repasadas** (`curso.json`, inicia con M01+M03). Panel **Flujos** con los 7 módulos (video del área, transcripción, workflow GX o "pendiente", notas de qué cambiar). 404 inicial: el `--out` relativo se resolvió contra otro cwd; regenerado desde la raíz del vault, HTTP 200 en `:8890/curso.html`.
- **Caja LoRA en la Polaroid**: catálogo de los 17 LoRAs (fuente: `lora-locales-comfyui.md` + sidecars) con link CivitAI + trigger + strength + **qué observar**. M03 → JJ_Archvizcg_v2 #191596 verificado en `curso-datos.json`.
- **Sync GX + notas estilo n8n en el canvas**: `GX-01-modulo1-base-txt2img.json` con 7 títulos editoriales + 4 notas `MarkdownNote` amarillas. Nodos de nota verificados en el fuente del frontend 1.45.21 instalado (`noteNode.ts`: `isVirtualNode`, widget `text`, `serialize_widgets`). El sync no pisa tus retoques (huella sin anotaciones + conserva posiciones; fix `__i`/`__k` heredado de la galería).
- **Prueba de ejecución**: el conversor suelta las notas solo → grafo de 7 nodos encolado headless OK (`WF04-1.0.0_00005_.png`, seed 42, prompt real del WF04). Queda en tus manos apretar Queue en Comfy como prueba en vivo.
- **Prompt plaza Sagrada Familia**: txt2img (`GX-plaza-gaudi_00001_.png`) capta plaza+torres+luz pero las catenarias quedan sugeridas; las torres salen genéricas → pasamos a img2img con foto real (`G:\Mi unidad\OS-Emilia\AIxGaudi\Referentes\Barcelona_(4720368660).jpg`, Sagrada desde el parque, 2622×1748).
- **img2img trabado**: denoise 0.6 sobre la foto full-res dejó el job clavado dentro del VAE en CPU fp32 (cancel imposible entre steps). Lección: **bajar la foto a ≤1024 px antes** (SD1.5 es nativo ~512). Foto reducida lista en `Temp\opencode\barcelona_1024.jpg` (1024×683).
- **Restart manual**: el restart MCP se negó (resuelve el install en `C:\Users\Solch16\ComfyUI` sin `main.py`; el real es `P:\00-repos\ComfyUI` lanzado por bat). Kill del PID 16264 (commandline verificado) + relanzamiento idéntico al bat. Comfy sano: 0.28.0, cola vacía, sin errores.

## Archivos

**Nuevos (vault)**

- `scripts/dashboard-curso.py` · `scripts/dashboard-curso_notas.md`
- `raw/sessions/2026-10-30-sesion-dashboard-curso-notas-img2img.md`

**Modificados (vault)**

- `scripts/00-index.md` (entrada dashboard-curso)

**Fuera del vault (no van al commit)**

- `P:\00-repos\ComfyUI\user\default\workflows\GX-01-modulo1-base-txt2img.json` (11 nodos: 7 + 4 notas)
- `P:\00-repos\ComfyUI\output\WF04-1.0.0_00005_.png` · `GX-plaza-gaudi_00001_.png`
- `P:\00-repos\ComfyUI\input\Barcelona_(4720368660).jpg` (subida verificada en LoadImage)
- `activos/web/galeria/curso.html` + `curso-datos.json` + `curso.json` + `img-curso/` (gitignored)

## Estado y qué sigue (mañana)

1. Subir `barcelona_1024.jpg` y re-correr el img2img (mismo grafo, denoise 0.6).
2. Revisar salida → sumar como repasada a `curso.json` + regenerar tablero.
3. Módulo 2: armar `workflow_lora_strength.json` → GX-02 (comparativa de modelos queda para el pod).
4. Apretar Queue en Comfy sobre GX-01 (prueba en vivo de las notas).

## Análisis cerebro-digital

**Topics:** dashboard-curso · solo-repasadas · lora-info-civitai · markdownnote-virtual · sync-respetuoso · img2img · cpu-vae-fp32 · restart-manual · workspace-mismatch

**Entidades:** `scripts/dashboard-curso.py` · `activos/web/galeria/curso.html` · `GX-01-modulo1-base-txt2img.json` (11 nodos) · `noteNode.ts` (frontend 1.45.21) · `Barcelona_(4720368660).jpg` · `barcelona_1024.jpg` · `WF04-1.0.0_00005_.png` · `GX-plaza-gaudi_00001_.png` · PID 16264 · `corre_comfyui_background.bat`

**Hechos:**
- El frontend trae `Note`/`MarkdownNote` de fábrica (`isVirtualNode`): la cola los salta, el backend nunca los ve.
- El conversor librería→API suelta los nodos de nota solo (verificado: 11→7).
- VAE en CPU fp32 + foto 2622 px = job clavado imposible de cancelar por HTTP; la salida es kill + relanzar.
- El restart MCP no resuelve instalaciones lanzadas por bat (mismatch `C:\Users\Solch16\ComfyUI` vs `P:\00-repos\ComfyUI`).
- Quirk del workspace activo (autodetectado C:) vs default guardado (P:) sigue pendiente de resolución.
