---
tipo: plan
proyecto: moodboard-vault-visual-local
cliente: interno
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [plan, comfyui, moodboard, vault-visual, directml, controlnet, ipadapter, hitl]
idioma: es
estado: plan
---

# Spec — Moodboard L1+L2 local DirectML + vault-visual

> Convierte `Advertising1 - Moodboard Creation.json` (Recraft + GPT-Image, API con costo) en variante 100% local RX 570 8GB DirectML (prohibido CUDA) + define ingesta vault-visual en 3 destinos con ficha 1:1. Estado MCP 2026-09-09: `http://127.0.0.1:8188` inalcanzable (ECONNREFUSED), validación de nodos pendiente al arranque.

## 0. Resumen en 1 línea

L1 Variation (Canny 0.31/0.59 + CN 0.85/0.80 + Realmimix + IPA style 0.65) y L2 Alteration (mood batch CLIPVision + product Canny 0.12/0.39 + IPA 0.8 + denoise 0.75, fallback VAEEncode 0.65) en `WF_v1_local_Canny_IPA/`, salidas `n_06-B-01.png` + `02-WF-log`, ingesta a `activos/` con ficha obligatoria y consulta Dataview/Canvas/Excalidraw local.

## 1. Fuentes leídas

* `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` — 4x LoadImage selects + METHOD 1 Recraft (`RecraftCreateStyleNode:392 realistic_image`, `RecraftStyleV3InfiniteStyleLibrary:395`, `RecraftTextToImageNode`, `BatchImagesNode:409`) + METHOD 2 GPT (`OpenAIGPTImageNodeV2:430 gpt-image-2 1024x1024 seed 1688736571`) + 2x SaveImage + MarkdownNote Quick Intro.
* `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md:15-32` R1 ImageScale 512 (OOM RX 570 ante inputs heterogéneos, SD1.5 nativo 512) + `:76-116` estructura WF (`00-README, 01-index, 02-WF-log, 03-nodos, 04-backlog, salidas/n_XX-{A-F}-NN.png, PLANS/, SPECS/, workflow_*.json`).
* `wiki/glosario/interno/pbooks/pbk-comfyui.md:58-63` Base local RX 570 DirectML (`--directml 0 --force-fp16 --disable-cuda-malloc`, patch WMI model_management.py:324, SD1.5 + 2 CN ok) + `:84-98` pipeline Canny + `:100-145` tablas Canny/Depth + dual Canny 0.75/0.0-0.75 + Depth 0.65/0.0-0.85.
* `wiki/glosario/software/comfyui.md` catálogo — ArchitectureRealmix v1.1 2.1GB SD1.5 (`architecturerealmix_v11.safetensors`, euler_ancestral karras 30 cfg 7) + Canny `control_v11p_sd15_canny.safetensors` 689MB + Depth FP16 689MB + fichas ImageScale (lanczos para arquitectura) / Canny 0.30-0.50 + 0.60-0.80 estructura / ControlNetLoader / ControlNetApplyAdvanced (strength 0.5-0.85, end 0.7-0.8).
* `wiki/glosario/conceptos/vault-visual.md:19-28` — ingesta + curaduría sí/no + consulta ("cocinas toscanas con piedra") + mejora; regla sin ficha no entra.
* `wiki/glosario/conceptos/cerebro-digital-karpathy.md:15-20` — raw → análisis (topics/entidades/hechos) → ingest wiki.
* `AGENTS.md:7,42-55` binarios en `/activos/` gitignored, `.md` solo referencian `[activos/...]` o `` `C:\BIM\...` `` + `:97` docs patrón `/built-in-nodes/<PascalCase>` + `:99` HITL + `:117-123` ComfyUI DirectML.
* `.gitignore:2` `/activos/` + `.obsidian/core-plugins.json` `canvas:true` + `analisis-despliegue-wiki-quartz.md:411` servir `![[...]]` aparte en web.

## 2. Variante LOCAL (propuesta a validar vía MCP)

### L1 Variation — estilo sobre base

```text
LoadImage(producto/base) → ImageScale(lanczos, 512x512, crop center) → Canny(0.31/0.59)
CheckpointLoaderSimple(architecturerealmix_v11) ─┬─ model → KSampler
                                                ├─ clip → CLIPTextEncode(+/-)
                                                └─ vae → VAEDecode
ControlNetLoader(control_v11p_sd15_canny) → ControlNetApplyAdvanced(strength 0.85, start 0.0, end 0.80, image=Canny)
Mood refs Batch → CLIPVision → IPAdapterUnifiedLoader(weight 0.65, style) ─→ KSampler
KSampler(euler_ancestral, karras, 30, cfg 7, denoise 1.0) → VAEDecode → SaveImage(n_06-B-01)
```

### L2 Alteration — producto + mood

```text
Batch mood refs → CLIPVision → IPAdapter(product, weight 0.8)
Product LoadImage → ImageScale 512 → Canny(0.12/0.39) → ControlNet(0.8/0.0-0.80)
KSampler(denoise 0.75, resto igual L1) → VAEDecode → SaveImage(n_06-B-02)
Fallback cuando IPAdapter ausente: VAEEncode(img2img, denoise 0.65) directo al KSampler, misma seed para comparar.
```

### Nodos (docs oficiales)

* https://docs.comfy.org/built-in-nodes/ImageScale
* https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple
* https://docs.comfy.org/built-in-nodes/ControlNetLoader
* https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced
* https://docs.comfy.org/built-in-nodes/CLIPTextEncode
* https://docs.comfy.org/built-in-nodes/KSampler
* https://docs.comfy.org/built-in-nodes/VAEDecode
* https://docs.comfy.org/built-in-nodes/VAEEncode
* https://docs.comfy.org/built-in-nodes/LoadImage
* https://docs.comfy.org/built-in-nodes/SaveImage
* Canny + IPAdapter: custom (`comfyui_controlnet_aux`, `ComfyUI_IPAdapter_plus`), guía https://docs.comfy.org/controlnet-guide

## 3. Flujo MCP (validado parcial, ejecución pendiente)

Estado 2026-09-09:

* `comfyui_get_system_stats health` → ECONNREFUSED `http://127.0.0.1:8188`.
* `comfyui_install_comfyui environment` → `reachable:false`, workspace `C:\Users\Solch16\ComfyUI`.
* `comfyui_list_local_models list` → solo Juggernaut XL + scribble 0.6MB (difiere de catálogo Realmimix+Canny+Depth instalados — revisar extra-paths al arrancar).
* `comfyui_create_workflow node_info ImageScale` → mismo ECONNREFUSED (esperado sin Comfy arriba).

Secuencia cuando Comfy esté arriba (la ejecuta el agente tras `s flujo`):

1. Arranque terminal: `P:\00-repos\ComfyUI\corre_comfyui.bat` (o `python main.py --directml 0 --force-fp16 --disable-cuda-malloc --lowvram`).
2. `comfyui_create_workflow action node_info` (CheckpointLoaderSimple, ControlNetLoader, ControlNetApplyAdvanced, IPAdapterUnifiedLoader, CLIPVision).
3. `create (txt2img Realmimix) + modify (inyecta ImageScale/Canny/CN/IPA) + validate`.
4. `comfyui_enqueue_workflow enqueue` batch L1+L2 (o `run_template` cuando haya pack).
5. Guardar `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v1_local_Canny_IPA/workflow_moodboard_local.json` + `salidas/n_06-B-01.png` (+ `-B-02`) + entrada `02-WF-log` (seed/cfg/steps/sampler/strength/end/denoise/IPA/modelos).

Destino canónico:

```text
proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v1_local_Canny_IPA/
├── 00-README.md / 01-index.md / 02-WF-log-WFv1_local_Canny_IPA.md / 03-nodos-WFv1.md / 04-backlog.md
├── salidas/n_06-B-01.png
├── PLANS/ / SPECS/
└── workflow_moodboard_local.json
```

## 4. Ingesta vault-visual (3 destinos + ficha 1:1)

* `activos/videos/ytb-<canal>-<slug>.mkv` — bruto audiovisual.
* `activos/proyectos/<obra>/referentes/YYYY-MM-DD-<origen>-<slug>-NN.jpg` — ej. `2026-09-09-pinterest-cocina-toscana-01.jpg`.
* `activos/proyectos/<obra>/renders/n_06-B-01.png` — promoción desde `WF/.../salidas/`.
* Ficha hermana mismo basename:

```yaml
---
tipo: referente
fecha_creacion: 2026-09-09
origen: pinterest
proyecto: casa-masterplan
elemento: cocina
estilo: [toscana]
material: [piedra]
curaduria: pendiente
---
```

Regla: sin ficha no entra. Curaduría titular sí/no; lo usado en entregas se marca; lo no usado 90 días se archiva.

## 5. Consulta visual (simulación local)

Dataview (Obsidian local lee gitignored):

```dataview
TABLE elemento, estilo, material, curaduria
FROM "activos/proyectos/casa-masterplan/referentes"
WHERE curaduria = "si" AND contains(estilo, "toscana") AND contains(material, "piedra") AND contains(elemento, "cocina")
```

* Canvas (core-plugins `canvas:true`): file-nodes a cada ficha + imagen, aristas `inspira → n_06-B-01`.
* Excalidraw: `![[activos/proyectos/.../2026-09-09-pinterest-cocina-toscana-01.jpg]]` embebido local. En web (Quartz/MkDocs) ese gitignored queda fuera — servir aparte (`analisis-despliegue-wiki-quartz.md:411`).
* Código opcional (solo con `s codigo`): `scripts/index_referentes.py` + `scripts/index_referentes_notas.md` con `# NOTA ES:` línea a línea. Ejecución por vos: `P:\Anaconda\envs\comfyenv\python.exe scripts/index_referentes.py`, luego `¿Avanzo a ejecutar? s/N`.

## 6. DoD

* [ ] Comfy DirectML arriba + `node_info` confirma CL/CN/IPA.
* [ ] `workflow_moodboard_local.json` validado (`validate` sin errores).
* [ ] `salidas/n_06-B-01.png` (+ `-B-02` L2) + `02-WF-log` (seed/cfg/strength/end/denoise).
* [ ] Render final promovido a `activos/proyectos/<obra>/renders/`.
* [ ] Fichas referentes con `curaduria: si` para lo usado.
* [ ] Wiki (`wiki/glosario/conceptos/moodboard.md` vía `@vaultworm-arq`) solo tras `s` explícito.

## 7. Gates HITL

* `¿Avanzo? s/N` → fase flujo (MCP enqueue + guardado WF).
* `¿Avanzo con código index_referentes? s/N` → genera scripts didácticos.
* `¿Avanzo a ejecutar? s/N` → vos ejecutás en terminal.
* `¿Avanzo a curaduría? s/N` → `@vaultworm-arq` + `@contenidos` hacia wiki.
