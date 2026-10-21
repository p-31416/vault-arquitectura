---
tipo: log
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [sesion, comfyui, lora, flux2, klein, gaudi, rhino-to-image, investigacion, emilia, concurso]
---

# Sesión 2026-10-20 — LoRA «Rhino-to-Image» (FLUX.2 klein 9B): análisis, research y fichas

## Qué se hizo

- **Analicé el LoRA** que envió Emilia: `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\rhino-to-image-lora.basic.safetensors` (120,8 MB). Lectura directa del header `.safetensors` (sin ejecutar código) + verificación numérica de los pesos.
- **Identifiqué el modelo base**: FLUX.2 [klein] 9B (Black Forest Labs). Contraste de shapes contra `Klein9BParams` (`black-forest-labs/flux2`, `src/flux2/model.py`) y contra `comfy/model_detection.py:238` (`image_model: "flux2"`) del ComfyUI local (`b08e6cf3`).
- **Lancé `@sherlock`** para investigar LoRAs sobre FLUX.2, entrenamiento, instalación en la PC de Emilia y el contexto del curso/concurso → 54 fuentes verificadas.
- **Escribí las fichas**: LoRA, modelo base, actualización de `comfyui.md` y `pbk-comfyui.md`, workflow `WF-rhino-to-image` (5 archivos + JSON + `salidas/`), script de auditoría + notas, log de sesión y `log.md`.
- **Construí el grafo del workflow** contrastando cada nodo contra el código de ComfyUI local (esto corrigió dos supuestos: `UNETLoader` usa `weight_dtype` y no `weight_name`; `SamplerCustomAdvanced` usa el esquema nuevo `noise`/`guider`/`sampler`/`sigmas`/`latent_image`).

## Hallazgos

- **El LoRA es "el modelo de IA exclusivo" del curso AI×Gaudí**: la web de Archademy lo describe como *"un modelo de IA entrenado con los archivos de la Fundació Antoni Gaudí"*, y el módulo 3 describe el workflow «Rhino-to-Image» exactamente como el que armamos. No hay ficha pública (ni Civitai ni HF) → el **trigger word es el bloqueo** y hay que pedirlo.
- **El instructor es Thomas Nelissen** (Davis AI, París; ex-JDS Architects), con Cas Esbach (ex-MVRDV) como co-autor del módulo 7. "Ismail Seleit" venía de otro curso y queda retirado de la ficha.
- **El bloqueo de geometría es nativo de FLUX.2, no ControlNet**: `ReferenceLatent` ×2 con método `index` (`ref_index_scale = 10.0`). No hay ControlNet oficial de BFL, y el único paquete serio (`alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union`) es para `FLUX.2 [dev]` 32B.
- **Chase de licencia**: klein 9B es FLUX Non-Commercial y el LoRA es derivative → admisible en concurso, y para cliente la vía es klein 4B (Apache 2.0) **reentrenando**, porque portar el LoRA entre 9B y 4B es imposible (4096 vs 3072 de hidden, 8+24 vs 5+20 bloques, 12288 vs 7680 de embedding).
- **La RX 570 de 8 GB no alcanza para 9B**: 8,8 GiB de pesos + 8,1 GiB de text encoder. Con DirectML, `--lowvram` no hace nada (`model_management.py:121` fuerza `lowvram_available = False`); el arranque correcto es `--directml --disable-dynamic-vram --reserve-vram 1.0`.
- **Coste del concurso**: RunPod 3090 a $0,22/h → $2-5 por las 20-40 imágenes finales. Entrenar el LoRA en 4B cuesta ~$0,50 de GPU.
- **Nombres de archivos corregidos**: `Comfy-Org/flux2-klein-9B` fue renombrado a `Comfy-Org/vae-text-encorder-for-flux-klein-9B`; no hay GGUF de city96 para klein 9B (los de `unsloth`).

## Archivos

**Nuevos**
- `wiki/glosario/software/lora-rhino-to-image-gaudi.md` — ficha del LoRA
- `wiki/glosario/software/flux2-klein-9b.md` — ficha del modelo base y su stack
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/` — `00-README.md`, `01-index.md`, `02-WF-log-WFrhino_to_image.md`, `03-nodos-WFrhino_to_image.md`, `04-backlog.md`, `workflow_rhino_to_image.json`, `salidas/README.md`
- `scripts/analizar-lora-safetensors.py` + `scripts/analizar-lora-safetensors_notas.md`
- `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` (este archivo)
- `raw/research/2026-10-20-flux2-klein-lora-rhino-to-image.md` + `-crudo.md` + `raw/research-cache/2026-10-20-flux2-klein-lora-rhino-to-image.json` (producidos por `@sherlock`)

**Modificados**
- `wiki/glosario/software/comfyui.md` — 2 secciones nuevas (FLUX.2 klein 9B, LoRA rhino-to-image), filas en el catálogo de modelos y de LoRAs, enlaces
- `wiki/glosario/software/00-index.md` — 2 filas
- `wiki/glosario/interno/pbooks/pbk-comfyui.md` — flujo nuevo en el catálogo y el mapa de decisión, sección Rhino-to-Image, 3 troubleshooting
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/README.md` — enlace al WF
- `scripts/00-index.md` — entrada del script nuevo
- `log.md` — entrada de la sesión

## Análisis cerebro-digital

**Topics:** lora-auditoria, safetensors-header, flux2-klein-9b, reference-latent, controlnet-ausencia, directml-vram, runpod-costos, licencias-no-comercial, curso-ai-gaudi, concurso-gaudi-nexus, rhino-export-capturas.

**Entidades:** `rhino-to-image-lora.basic.safetensors` · `black-forest-labs/FLUX.2-klein-9B` · `FLUX.2-klein-base-9B` · `FLUX.2-klein-4B` (Apache 2.0) · `Comfy-Org/vae-text-encorder-for-flux-klein-9B` (Qwen3-8B) · `black-forest-labs/FLUX.2-small-decoder` (VAE) · `unsloth/FLUX.2-klein-9B-GGUF` · `alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union` · nodos `UNETLoader`, `LoraLoaderModelOnly`, `CLIPLoader(type=flux2)`, `VAELoader`, `ImageScaleToTotalPixels`, `ReferenceLatent`, `FluxKontextMultiReferenceLatentMethod`, `CFGGuider`, `Flux2Scheduler`, `KSamplerSelect`, `RandomNoise`, `SamplerCustomAdvanced` · `Barcelona-2D.dwg`, `3D-model.dwg` · Thomas Nelissen · Cas Esbach · Archademy · Fundació Antoni Gaudí · RunPod 3090/4090.

**Hechos:** el LoRA es rank 16 / F32 / 176 tensores / 31,66 M params, con matrices B no nulas (σ ≈ 1,3e-3) → entrenado y sano; los MLP de los bloques duales quedan fuera del ajuste (solo atención duales + `linear1`/`linear2` simples + embeddings + modulaciones + `final_layer`); el archivo no trae metadata (`__metadata__` ausente) ni sidecar Civitai; el LoRA solo aplica a klein 9B; el mecanismo de referencia de FLUX.2 es `index` con `ref_index_scale = 10.0`; con DirectML `--lowvram` queda sin efecto.

## Continuación (misma sesión) — Dashboard del concurso + extracción de material del curso

- **Dashboard de ComfyUI actualizado** (`proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html`, el del cierre de Mes 1 del 16/10): pasó de 4 a 5 tabs con el **tab 4 · Concurso** (motor FLUX.2 klein 9B + LoRA del curso, stack a descargar, flujo WF-rhino-to-image, cómo se entrenó el LoRA, riesgo de licencia, plan en 3 etapas con costos, y lo que falta pedir al instructor). Además: filas nuevas en la tabla de modelos, la tarjeta "Ingeniería inversa" actualizada, y el tab Mes 2 con el pipeline del concurso y la entrega 16/12.
- **Verificado que las dos fuentes del curso están login-gated**: `archademy.ai/my-account/my-competitions/214/?tab=course` devuelve el formulario de acceso; `miro.com/app/board/uXjVHRM2XQU=/` devuelve la app sin sesión.
- **Instrumental de extracción construido y probado**:
  - `scripts/miro_board_inventory.py` + `_notas.md` — inventario del tablero Miro (videos con id de YouTube, workflows, tableros, PDFs, tarjetas, módulos). Modos API (token `boards:read`, paginación por cursor) y offline (parseo del `.miro` exportado, que es un ZIP).
  - `scripts/archademy_curso_inventory.py` + `_notas.md` — inventario del área de participantes (lecciones, videos, workflows, PDF, modelos). Modos `--html` (Ctrl+S con sesión) y `--url` + cookies.
  - Ambos probados con archivos de laboratorio: detección correcta de videos/YouTube/workflows/Miro/PDF.
- **Guía del circuito completo** en `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md`: cómo bajar el export de Miro, cómo sacar la cabecera Cookie para Archademy, cómo transcribir los videos con `scripts/transcribir_youtube.py` y dónde queda cada cosa en el vault.

### Archivos (continuación)

**Nuevos**
- `scripts/miro_board_inventory.py` + `scripts/miro_board_inventory_notas.md`
- `scripts/archademy_curso_inventory.py` + `scripts/archademy_curso_inventory_notas.md`
- `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md`

**Modificados**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html` — tab 4 · Concurso + modelos + Mes 2
- `scripts/00-index.md` — 2 entradas
- `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` (este archivo) · `log.md`

### Segunda vuelta — formato de export y descarga de videos

- **Corrección sobre el export de Miro**: hoy ya no se exporta `.miro`; el backup es **`.rtb`** (solo owner/co-owner) y el export disponible para participantes es **CSV** ("Export to spreadsheet", todos los planes). El script se ajustó para los cuatro casos: **CSV** (una fila por item con texto + URL + tags), **backup `.rtb`/`.miro`** (ZIP → JSON con más items; si no es ZIP → **escaneo binario de URLs**), **PDF** (URLs y textos por página) y **API** (token `boards:read`).
- **Hallazgo clave para los videos**: la web de Archademy dice *"siete módulos en inglés (con subtítulos)"*. O sea que **no hace falta descargar el video**: `scripts/transcribir_youtube.py` lee los subtítulos (manuales → automáticos → si no, baja solo el audio y usa faster-whisper local). Para plataformas que no sean YouTube: `python -m yt_dlp --cookies-from-browser chrome "<url>"`.
- **Datos del concurso verificados** (web pública): entrega 16/12/2026 23:59 GMT-7 · lámina A1 ≤15 MB JPEG (+A4 opcional) · tema "Mercado de Proximidad" + "Centro de Cultura Digital" y la plaza de la Sagrada Família · premios 6.000/2.000/1.000 USD + Premio de Diseño de la Fundació 1.000 + 10 menciones + 50 finalistas · inscripción 175 USD/equipo hasta el 4/11 · 7 módulos en inglés con subtítulos · profesores Thomas Nelissen y Cas Esbach.
- **Verificación con archivos de laboratorio**: CSV (5 filas → 2 videos con id, 1 workflow, 1 Miro, 1 modelo) y backup binario (3 URLs recuperadas) → ambos modos funcionan.

### Archivos (segunda vuelta)

**Modificados**
- `scripts/miro_board_inventory.py` + `scripts/miro_board_inventory_notas.md` — soporte CSV, `.rtb`/`.miro` (ZIP y binario) y PDF
- `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md` — formato de export recomendado, datos del concurso, ruta de transcripción
- `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` (este archivo) · `log.md`

### Tercera vuelta — el tablero del curso (AI-course.csv)

- **Recibido** `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\AI-course.csv` (98 KB, 219 filas) → inventariado con `scripts/miro_board_inventory.py` → `raw/research/2026-10-20-miro-curso/`.
- **El tablero no es de workflows**: es el **índice de recursos y prompts** del curso. 72 secciones, 147 tarjetas. Se mejoró el script para detectar secciones (tarjetas en mayúsculas) y agrupar el contenido.
- **Tres hallazgos que cambian el plan**:
  1. **Existe la variante premium** del LoRA: `rhino-to-image-lora-premium.safetensors` (la descarga pasa por `thomasnelissen.ai`).
  2. **No hay trigger word**: la activación es un **prompt JSON estructurado** con `STRICT CAMERA LOCK` / `MATCH CAMERA OF IMAGE 1 EXACTLY`. Queda resuelta la incógnita más grande del análisis del LoRA.
  3. **El curso usa el LoRA al 50 % y al 100 %** (comparación del módulo 2) → coincide con el rango 0,6-1,0 que veníamos recommending desde el análisis de los pesos.
- **El pipeline real tiene 3 pasos**, no 1: captura en color de Rhino (verde=vegetación, rosa=figuras) → **pase de arcilla monocroma** con la lógica constructiva de Gaudí (dial 0-10, por defecto 7) → **pase hiperreal** con FLUX.2 klein 9B + LoRA + prompt JSON. Frase del curso: *"The clay is the base for the edit LoRA: keep it clean, monochrome, edge-legible, camera + footprint 1:1."*
- **Extraído al vault** (uso interno): `prompt-rhino-to-image-instruction-md.md` (INSTRUCTION.md del módulo 3), `prompt-rhino-to-gaudi-instruction-md.md` (INSTRUCTION.md del módulo 7, variante B) y `prompt-rhino-to-image-esqueleto-json.md` (la plantilla JSON de salida), los tres en `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/`.
- **Contenido completo del tablero**: 7 módulos con sus workflows (`IMPORTABLE IN COMFY` / `NOT IMPORTABLE IN COMFY`): IMAGE-EDIT FLUX.2 KLEIN 9B, RHINO-TO-IMAGE, SPECTRUM, UPSCALING 1-4 (SeedVR2, TOPAZ, FLUX.1, Krea); prompts de módulo 5 (imagen→3D: maqueta blanca, normal map, viewport Rhino); el "Seedance director" (módulo 4); los system prompts del PROMPT COACH y del COMFY EXPERT; y las Claude Skills `nanobanana` y `seedance-director` (instalables con `gemini extensions install`).

### Archivos (tercera vuelta)

**Nuevos**
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md.md`
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md.md`
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json.md`
- `raw/research/2026-10-20-miro-curso/miro-inventario.md` + `.json`

**Modificados**
- `scripts/miro_board_inventory.py` — detección de secciones en CSV
- `wiki/glosario/software/lora-rhino-to-image-gaudi.md` — activación sin trigger, variante premium, pipeline de 3 pasos, fuerza 0,5/1,0
- `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README.md` y `03-nodos-WFrhino_to_image.md` — pipeline real, prompt oficial, dial de arcilla
- `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md` — contenido del tablero, guardado del HTML simplificado
- `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` (este archivo) · `log.md`

## Continuación 2 (21/10) — Transcripciones del curso resueltas

- **El HTML guardado por Emilia** (`G:\Mi unidad\OS-Emilia\AIxGaudi\My account - Archademy.ai.html`, 213 KB, con su carpeta `_files`) resultó **suficiente**: los iframes y los `data-module` están en el markup.
- **Plataforma de video identificada: Mux** (`iframe.mediadelivery.net/embed/{env}/{playback_id}`), con el player Plyr + hls.js. Los 7 módulos con video: `intro-generative-ai`, `text-to-image`, `image-to-image`, `image-to-video`, `image-to-3d`, `round-table`, `gaudi-workflow` (+ el panel `miro-board`, sin video).
- **Los subtítulos son la transcripción**: cada video expone `https://{prefijo}.b-cdn.net/{PLAYBACK_ID}/captions/{en|es}.vtt`, que se descargan **sin token ni cabeceras** (200 directo). El `playlist.m3u8` sí da 403, pero no hace falta.
- **Nuevo script `scripts/mux_lecciones_curso.py` (+ notas)**: empareja panel ↔ iframe (con la trampa de que `data-module` también está en los tabs del nav), baja los VTT, los convierte a SRT/TXT y los escribe en `raw/yt/transcripts/` con la convención del vault. Deja `indice-curso-ai-gaudi.json`.
- **Resultado: 6 de 7 módulos transcritos** (EN y ES): Introduction 1268 cues · Text-to-Image 659 · Image-to-Image 1047 · Image-to-Video 333 · Image-to-3D 249 · Gaudí Workflow 454. El *Round Table* responde 404 en subtítulos (queda pendiente bajar el audio y pasarle faster-whisper).
- **Bonus**: la página trae la **contraseña del tablero Miro** (`archademy-miro-pw-code` = `Gaudi2026`) y su URL → el tablero se abre sin permisos.
- **Pendiente de Emilia**: el **LoRA premium** no aparece en `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\` (solo `basic`, `AI-course.csv` y los 2 DWG).

### Archivos (continuación 2)

**Nuevos**
- `scripts/mux_lecciones_curso.py` + `scripts/mux_lecciones_curso_notas.md`
- `raw/yt/transcripts/2026-10-21_mux-<modulo>.{en,es}.md+.srt+.txt` (12 archivos) + `indice-curso-ai-gaudi.json`

**Modificados**
- `scripts/00-index.md` · `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md` · `log.md` · este archivo

### Continuación 3 (21/10) — Infraestructura, dashboard ampliado y el salto a "asistente que ejecuta"

- **Decisión de infraestructura documentada** en `wiki/glosario/software/comfy-cloud-vs-runpod.md`, con fuentes verificadas: **Comfy Cloud Standard ($20) no sirve para el concurso** (no deja importar modelos propios; el upload directo de archivos grandes no existe todavía) y **en Comfy Cloud no se entrena en ningún plan** (los nodos de entrenamiento no están en la lista aprobada) → el Creator ($35) solo habilita *usar* un LoRA ya entrenado, y aun así importado desde CivitAI/HF. Veredicto: híbrido (local 8 GB para iterar · Comfy Cloud **Free** 400 cr ≈ 25 min de GPU para probar los workflows oficiales · RunPod 3090 $0,22/h para producción 9B y entrenamiento) = **$1-2 por mes**. Privacidad: prompts e imágenes quedan en la cuenta de Comfy (retención "el tiempo necesario para operar y mejorar"), y con Partner Nodes además van al proveedor; en el pod, disco cifrado que **no deja rastro al terminar el pod**. Regla propuesta: material del concurso **no pasa por el Comfy Agent**.
- **Dashboard de ComfyUI ampliado a 6 tabs** (la galería queda intacta y mandando): tab 4 · Concurso, tab 5 · **Mes 2** (el cuadro dónde renderizar con límites y costos reales, las 5 pruebas del mes con criterio de cierre, la pregunta de fondo y las 4 decisiones a tomar) y tab 6 · **Método** (las 5 capas hacia un asistente que ejecuta, la impronta del estudio y Hermes vs OpenClaw).
- **Recolector de renders**: `scripts/indice-renders-comfy.py` (+ notas) lee la metadata que ComfyUI graba dentro de cada PNG (bloques `tEXt` `prompt` y `workflow`) y arma `INDICE-RENDERS.md/.json` con modelo, LoRA y strength, seed, sampler, steps, cfg, resolución y prompt. Resultado: **80 renders, 100% con metadata**. Clave de diseño: sin base de datos — la trazabilidad vive dentro de la imagen.
- **Diseño de la evolución a asistente**: `proyectos/MVP_04-comfyui-arquitectura/evolucion-asistente-estudio.md` — 5 capas (0 ejecución local+MCP · 1 contrato JSON · 2 índice · 3 interfaz Gradio · 4 agente), el paralelo con el tablero del curso (el mismo índice, pero con metadata y que se regenera solo), la impronta como tres artefactos (schema + LoRA propio + índice) y hoja de ruta A→E con criterio de cierre. Verificado: Comfy documenta conexiones MCP **Local** y **Cloud** (la local es la que sirve: el Agente de Cloud no alcanza los archivos de la casa); **Hermes Agent** (Nous, MIT) con cliente MCP nativo + memoria + skills que se auto-mejoran + cron + 7 backends; **OpenClaw** (MIT) con gateway local, 29 canales, `mcp.servers` + `openclaw mcp serve`; y tres bases Gradio sobre ComfyUI (`comfy-webui` con API semántica y MCP, `comfy-headless` con Queue & History, `ComfyUI_to_webui`).

### Archivos (continuación 3)

**Nuevos**
- `wiki/glosario/software/comfy-cloud-vs-runpod.md`
- `proyectos/MVP_04-comfyui-arquitectura/evolucion-asistente-estudio.md`
- `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md` + `.json`
- `scripts/indice-renders-comfy.py` + `scripts/indice-renders-comfy_notas.md`

**Modificados**
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html` — 6 tabs
- `proyectos/MVP_04-comfyui-arquitectura/00-index.md` · `wiki/glosario/software/00-index.md` · `wiki/glosario/software/comfyui.md` · `wiki/glosario/interno/pbooks/pbk-comfyui.md` · `scripts/00-index.md` · `log.md` · este archivo

## Queda

### Hecho hoy (21/10) — cerrado

- LoRA `rhino-to-image` **copiado y verificado por SHA-256** en `P:\00-repos\ComfyUI\models\loras\` (era el `.basic`; el `.premium` no llegó a la carpeta).
- `workflow_rhino_to_image.json` **montado y validado contra el ComfyUI vivo** (23 nodos, 0 warnings; los únicos 5 errores son los 3 modelos y las 2 imágenes de referencia que faltan).
- 6 de 7 módulos del curso **transcritos** (EN+ES) + los 3 prompts oficiales extraídos + el tablero del curso inventariado (72 secciones).
- Dashboard de ComfyUI a **6 tabs** (galería mandando) + el cuadro de infraestructura + el índice de renders vivo (80/80 con metadata).
- Wiki: 2 fichas nuevas (`lora-rhino-to-image-gaudi`, `flux2-klein-9b`, `comfy-cloud-vs-runpod`), `comfyui.md` y `pbk-comfyui.md` actualizados, 4 scripts nuevos con sus notas.

### Pendiente (para la próxima sesión)

| # | Qué | Quién | Bloquea |
|---|-----|-------|----------|
| 1 | **Bajar el stack FLUX.2** en un pod 3090 (9,4 GB + 8,7 GB + 238 MB) y correr la matriz de aporte del LoRA (mismo seed: sin LoRA / 0,5 / 0,8 / 1,0) | requiere OK de gasto (~$1) | P1, P2 |
| 2 | **Exportar desde Rhino** las 3 pasadas con la misma cámara + la foto de material | Emilia | P1 |
| 3 | **Bajar los `.json` oficiales** del tablero (`RHINO-TO-IMAGE`, `IMAGE-EDIT FLUX.2 KLEIN 9B`) y diffearlos contra el nuestro | Emilia (password `Gaudi2026`) | P1 |
| 4 | **Pedir al instructor**: trigger word, base exacta (Base vs Destilado), variante `.advanced`, dataset y licencia del material de la Fundació, workflow JSON del módulo 3 | Emilia | ajuste fino del flujo |
| 5 | **Round Table**: bajar el audio (57,6 min) y pasarlo por faster-whisper | 30 min de CPU | transcripción completa |
| 6 | **Curaduría `@contenidos`** de las 12 transcripciones → `wiki/fuentes/` | 15 min + revisión | material del curso searchable |
| 7 | **Decidir infraestructura**: ¿dónde producir? (RunPod $1-2 / Cloud $20 / Creator $35 / local 4B) y qué es la "computadora con Linux" | Emilia + Sol | ruta de producción |
| 8 | **Presupuesto del mes** y arranque de P3 (LoRA propio en klein 4B) | Sol | 3-7/11 |
| 9 | **Automatizar el índice** (cron vía el n8n del VPS) y **armar la interfaz Gradio** | 1-2 días | etapas B y C de la hoja de ruta |
| 10 | **ADR**: nube como ruta de render · klein 9B (concurso) vs 4B reentrenado (clientes) | Sol | tipo: ADR |
- **Primera corrida comparativa**: strength 0,0 / 0,6 / 0,8 / 1,0 con el mismo seed, y repetir con la variante base (20 steps, cfg 5).
- **ADR pendientes**: nube como ruta de render; klein 9B para concurso vs reentrenamiento en 4B para clientes.
- **Extracción del curso**: Emilia abre el tablero Miro y exporta (`.miro`) y guarda la página del área de participantes → correr los dos scripts → transcribir los videos con `scripts/transcribir_youtube.py` → `@contenidos` para la curaduría.

