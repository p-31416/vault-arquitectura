# 2026-10-28 — Workflows adaptados del curso AI×Gaudí: las siete fichas de flujo y el plan maestro

## Qué se hizo

- **Lectura de las seis transcripciones del curso** (módulos 1, 2, 3, 4, 5 y 7; EN + ES, 4.010 cues) y extracción del flujo de cada uno: pasos con el nodo exacto y su valor, prompts literales, modelos mencionados, reglas del instructor y la lista explícita de lo que el video **no dice**.
- **Seis fichas de flujo** escritas en `proyectos/concurso-gaudi-nexus/flujos/` (módulos 1 a 5 y 7), cada una con su tabla de adaptación y sus checks contra el criterio del jurado.
- **Plan maestro** `specs/261028-plan-workflows-adaptados-curso-ai-gaudi.md`: los 7 workflows uno por módulo en orden de curso, la matriz de adaptación (9 diferencias curso → nuestra pila), el ciclo de construcción y revisión de 6 pasos con gate humano, milestones M-C1 a M-C7 y el sprint 1 con 22 pomodoros.
- **Carpeta del concurso** `proyectos/concurso-gaudi-nexus/`: `index.md`, `flujos/00-index.md`, `workflows/00-index.md`, `criterio/criterio-jurado.md` y la ficha del módulo 6 en estado "pendiente de transcripción".
- **Script nuevo** `scripts/transcribir-leccion-bunny.py` + notas: baja el video del módulo 6 del CDN del curso y lo transcribe en local con faster-whisper.
- **Reglas nuevas** R2, R3 y R4 en `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md`.
- **`.gitignore`**: agregadas las carpetas `salidas/`, `inputs/`, `ref/` y `assets/` del proyecto del concurso.

## Hallazgos

- **El CDN del curso responde 403 sin `Referer`**: con `Referer: https://iframe.mediadelivery.net/` entrega el `play_720p.mp4` de cada módulo (el módulo 6 pesa 538 MB). Esto abre la transcripción local del módulo 6, que expone 404 en sus dos pistas de subtítulos.
- **El LoRA del curso ya está en la máquina**: `models/loras/rhino-to-image-lora.basic.safetensors` (120,8 MB). El `README` de `WF-rhino-to-image` todavía lo lista como pendiente.
- **El grafo del módulo 3 ya existe**: 23 nodos en API format, con doble `ReferenceLatent` encadenado, `FluxKontextMultiReferenceLatentMethod` con método `index`, `Flux2Scheduler` de 4 pasos, `CFGGuider` con cfg 1,0 y `SamplerCustomAdvanced` con `euler` y seed 42. Falta documentarlo en la carpeta nueva y correrlo.
- **El stack FLUX.2 no está instalado**: faltan transformer fp8, text encoder Qwen3-8B y VAE Flux2 (18,3 GB). En la PC (8 GB, DirectML) FLUX.2 klein 9B no entra; el pod de RunPod es la vía.
- **Los nodos core cubren el preprocesado que el curso resuelve con nodos de pago**: `Canny` y `LoadDA3Model`/`DA3Render` están disponibles sin instalar packs, lo que habilita la preparación 3D del módulo 5 en local (el AO, que el video llama "la favorita").
- **`comfyui_controlnet_aux` no está instalado**: hoy solo corren `Canny` y DA3; el pack 3D cubre el resto en el pod.
- **Discrepancia de flags entre la skill y los `.bat`**: `corre-comfyui.md` usa un juego reducido y una ruta vieja (`P:\00-repos\vault-arquitectura`); `pbk-comfyui.md:63` documenta un launch distinto al de `corre_comfyui.bat`.
- **Tensión de plataforma documentada**: `comfy-cloud-vs-runpod.md` pone el render 9B en RunPod y el plan Studio OS fija "nunca concurso en cloud". Queda como ADR-002, con las cuatro reglas de costo cero de PI como puente.
- **Tensión de registro visual**: `261019` pide croquis con variación leve de perspectiva; `research:672` propone axonometría renderizada con before/after. Es la pregunta abierta #1 del plan.

## Archivos

**Nuevos**

- `specs/261028-plan-workflows-adaptados-curso-ai-gaudi.md`
- `proyectos/concurso-gaudi-nexus/index.md`
- `proyectos/concurso-gaudi-nexus/flujos/00-index.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-01-intro-generative-ai.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-02-text-to-image.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-03-image-to-image.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-04-image-to-video.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-05-image-to-3d.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-06-round-table.md`
- `proyectos/concurso-gaudi-nexus/flujos/flujo-07-gaudi-workflow.md`
- `proyectos/concurso-gaudi-nexus/workflows/00-index.md`
- `proyectos/concurso-gaudi-nexus/criterio/criterio-jurado.md`
- `scripts/transcribir-leccion-bunny.py` · `scripts/transcribir-leccion-bunny_notas.md`
- `raw/sessions/2026-10-28-sesion-workflows-adaptados-gaudi.md`

**Modificados**

- `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md` (R2, R3, R4)
- `scripts/00-index.md` (entrada del script nuevo)
- `.gitignore` (carpetas del concurso)
- `log.md` (entrada del 28/10 arriba)

## Análisis cerebro-digital

**Topics:** workflows-adaptados · curso-ai-gaudi · gaudi-nexus · comfyui · runpod · comfy-cloud · lora-rhino-to-image · flux2-klein-9b · reference-latent · nanobanana · seedance · tripo · hunyuan3d · ltx · faster-whisper · bunny-stream · milestone-m-c1

**Entidades:** `proyectos/concurso-gaudi-nexus/` (carpeta nueva del concurso) · `specs/261028-plan-workflows-adaptados-curso-ai-gaudi.md` (plan maestro) · WF-01 a WF-07 (workflows planificados) · M-C1 a M-C7 (milestones) · ADR-002 (nube vs. local, pendiente) · `raw/yt/transcripts/2026-10-21_mux-*.{es,en}.md` (6 transcripciones fuente) · `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/workflow_rhino_to_image.json` (grafo existente a versionar) · `P:\00-repos\ComfyUI` (instalación local, v0.28.0) · CDN del curso `vz-4ced3a48-15e.b-cdn.net` (library Bunny `719269`)

**Hechos:**
- El CDN del curso exige el header `Referer: https://iframe.mediadelivery.net/`; sin él responde 403.
- El módulo 6 (Round Table) es el único sin subtítulos: 404 en sus dos pistas.
- Siete módulos, siete workflows: el módulo 6 no aporta grafo, aporta el criterio de cierre.
- La matriz de adaptación tiene nueve filas: Comfy Cloud → pod, LoRA → local+pod, Nano Banana 2 → FLUX.2 edición, Nano Banana Pro → SDXL+ControlNet+DA3, Seedance → LTX, Tripo → ComfyUI-3D-Pack, Topaz → RealESRGAN+Hires, prompt coach → proyecto Claude, secrets HF → scp al pod.
- Los workflows del curso se cierran con tres corridas A y una B, y cada cierre exige la revisión del arquitecto.
- El costo del concurso completo con la ruta local+pod es de $1-2; las suscripciones de Comfy Cloud quedan como techo de gasto a relevar.
- El stack FLUX.2 son 18,3 GB y no entra en la PC de 8 GB con DirectML.
- El LoRA `rhino-to-image` basic (120,8 MB) ya está en `models/loras/`.
- R1 (escala 512²) es de la era SD1.5; en FLUX.2 el escalado es a megapíxeles (1,0 MP geometría · 0,5 MP material).
