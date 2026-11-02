---
tipo: aporte
proyecto: concurso-gaudi-nexus
origen: sesion 2026-10-30 (config @tim + demo SDXL + plan doc WF), para la matriz de pruebas en preparacion
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [concurso, gaudi-nexus, workflow, sdxl, convenciones, matriz-pruebas, aporte]
idioma: es
---

# Aporte a la matriz de pruebas — convenciones de WF decididas y receta validada

> Para el agente que arma la matriz de pruebas del concurso: esto es lo que ya está decidido y verificado por @tim + el vault. La matriz concreta de corridas (prompts de la matriz del concurso, se Globales, seeds) la completás vos con esto como base. Nada escrito acá necesita re-verificarse salvo donde se indica.

## 1. Decisiones ya tomadas (no cambiar sin `s` de SOL)

| Decisión | Valor |
|---|---|
| Ubicación de los WF del concurso | `proyectos/concurso-gaudi-nexus/workflows/` |
| Numeración de WF | por **número de módulo del curso** que adaptan: `WF-02-txt2img-sdxl`, `WF-03-rhino-to-image-sdxl`, `WF-07-flujo-gaudi-sdxl` (flujo-01 es protocolo; flujo-04 video = web; flujo-05 3D = servicio externo; flujo-06 = checklist — no generan WF SDXL) |
| Documentación por WF | **UN documento único** `<WF-slug>.md` con dos lectores: sección NT arriba (¿Qué es · Para qué · Qué aporta el humano · Qué se quiere obtener · Parámetros con rangos) + sección TK abajo (tabla de nodos: class_type exacto + columna NO técnico + columna técnico, prompts literales). No crear doc-NT/doc-TK separados (evita multiplicación de archivos; el dashboard ya cubre el resumen NT). Sólo si un doc pasa de ~250 líneas se evalúa dividirlo. |
| JSON del WF | dos archivos: `workflow_<slug>.json` (API format, canónico) + `workflow_<slug>_ui.json` (para arrastrar al canvas de ComfyUI y correrlo manual) |
| Salidas | subcarpeta `salidas/` del WF; binarios gitignored; referencias por ruta en el .md |
| Fuente de la receta SDXL | extender la del WF-04 2.0.0 validado (no duplicar: reusar) |

## 2. Receta SDXL validada en esta máquina (base para WF-02 y sucesivos)

De `proyectos/MVP_04.02-comfyui-arquitectura/WF-04-serie-txt2img/WF-04-serie-txt2img.md` (corrida 2.0.0, 2026-10-15, ✅):

- **Modelo**: `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (6,62 GB en disco)
- **Cadena**: `CheckpointLoaderSimple` → `CLIPTextEncode` (+/−) → `EmptyLatentImage` 1216×832 → `KSampler` (`dpmpp_2m` / `karras`, 35 steps, cfg 4, seed 42 fixed) → `VAEDecode` → `SaveImage`
- **Runtime**: ComfyUI con `corre_comfyui.bat` → `--directml 0 --force-fp16 --disable-cuda-malloc` + SDXL con `--lowvram --cpu-vae`; tiempo de corrida real **651 s** a 1216×832
- **Patch conocido**: `comfy/model_management.py:324` (DirectML reporta 1 GB fantasma) — re-aplicar si se actualiza ComfyUI
- JSON de referencia ya en disco: `workflow_2.0.0_txt2img_sdxl.json` + `workflow_txt2img_estadio_sdxl.json` + `workflow_txt2img_vivienda_sdxl.json`

## 3. Rangos de parámetros (dashboard + curso, citados en fichas flujo-02)

| Parámetro | Default del WF | Rango probado | Efecto (literal del curso `[HH:MM:SS]`) |
|---|---|---|---|
| Seed | 42 (fixed) | fixed / randomize | fixed = misma imagen exacta; randomize = nueva en cada corrida `[00:05:40]` |
| Steps | 35 (SDXL) | 5 → 10 → 20 (SD1.5, curso); 30–35 SDXL; límite práctico 50 | 5 = sin terminar, 10 = mejor, 20 = idéntica a 10 (determinista, se puede rastrear) `[00:09:08]` |
| CFG | 4 (SDXL) | 1 crudo → 8 bueno (SD1.5) / 20 satura; SDXL óptimo 3–4–7 | "la cantidad de creatividad" `[00:10:05]` |
| Sampler | `dpmpp_2m/karras` | euler con 30 steps/normal (WF-02 inpaint SD1.5) | el validated SDXL usa dpmpp_2m+karras |
| Resolución | 1216×832 | nativas SDXL (832–1216); FLUX mejor a 1024² `[00:14:03]` | EmptyLatentImage define proporción `[00:03:29]` |
| Strength LoRA (cuando lo usemos) | 1,0 comparativa | 0,5 sutil / 1,0 estilo completo | comparativa módulo 2 `[00:42:xx]` (ficha flujo-02) |
| Denoise (img2img, WF-03) | 0,75 | 0,4 calco / 0,6 re-estilo / 0,8 reinvención | dashboard-comfy § WF-05 |

## 4. Naming y protocolo de revisión manual (uno por uno)

- Salidas `n_XX-{A–G}-{NN}.png` según [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] (R3; letra G = LoRA).
- Loop acordado con SOL: `s` → se escribe el WF (doc + JSONs) → SOL arrastra el `_ui.json` al canvas y corre → **revisa la salidas manualmente, una a una** → joint issue la próxima corrida o `s` al siguiente flujo. **Una variable por corrida** (prompt, seed y latente constantes; cambia steps o cfg o modelo o strength).
- Qué aporta el humano (ponerlo así en cada doc NT): elige el prompt, mueve seed/steps/cfg/strength dentro de los rangos, revisa cada `n_XX` y etiqueta el keeper para la lámina.
- Bitácora: conecta con [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas|04-bitacora-corridas]] cuando una corrida sea repetible.

## 5. Mapeo flujos del curso → WF a crear (para la matriz)

| Flujo (ficha en `flujos/`) | WF a crear | Base sobre la que se extiende | Qué aporta SDXL local a la matriz |
|---|---|---|---|
| flujo-02 · text-to-image | `WF-02-txt2img-sdxl` | WF-04 2.0.0 (§2) | comparativa con/sin LoRA al 50/100 % — local no corre FLUX.2; SDXL es el piso de calidad de la casa |
| flujo-03 · rhino-to-image | `WF-03-rhino-to-image-sdxl` | WF-05 (croquis) + WF-03 (controles, dual ControlNet validado) masa + foto material; el paso final fotorreal se mantiene como variante/RunPod | img2img desde vista masiva + foto de material |
| flujo-07 · flujo Gaudí | `WF-07-flujo-gaudi-sdxl` | SSD-1B (~4,5 GB) para tener ControlNet Union SDXL en VRAM local (Juggernaut no deja espacio); receta que se calibra cuando se llegue | dial de intensidad 0-10 con ControlNet depth/canny |
| flujo-01 · protocolo | no genera WF (protocolo de comparación) | — | define cómo se comparan las corridas |
| flujo-04 · imagen a video | no SDXL (Seedance 2.0, web) | skill `seedance-director` | — |
| flujo-05 · imagen a 3D | no SDXL (Hunyuan3D/Tripo) | — | — |
| flujo-06 · round table | no genera WF (checklist de cierre) | — | criterio del jura para auditar la matriz completa |

## 6. Lo que puede completar la matriz de pruebas con lo ya hecho

- **Cards**: ya existen 94 renders con metadata en `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md` (incluidas la M01–M20 corridas SD1.5 sobre el prompt de la Sagrada) — la matriz puede reusar el mismo prompt migrado a dialecto SDXL para comparar modelos.
- **Modelos en disco (verificados)**: Juggernaut-XL_v9 (SDXL), architecturerealmix_v11 (SD1.5), sd-v1-5-inpainting-fp16, 16 LoRAs, 3 ControlNet SD1.5, RealESRGAN_x4plus. SSD-1B **aún no está descargado** (4,5 GB — pedir `s` + link de HF).
- **Dashboard**: `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html` documenta cada WF con cadena + rangos — un lugar más donde anclar las corridas de la matriz.
- **Docs**: cada WF nuevo anota en su .md la ficha del flujo del curso como fuente (timestamps) y qué cambió respecto del curso (nodos ±§).

## 7. Pendientes conexos (fuera de la matriz, pero colisionan si no se avisa)

- **LoRA del concurso** (`proyectos/concurso-gaudi-nexus/lora-estudio-plan.md`): el trigger `gaudinexusstyle` y la decisión klein 4B vs 9B siguen abiertos; si la matriz genera new renders con el estilo del concurso, curarlos ya como candidatos al dataset (40 objetivo).
- **Emplazamiento real** (decisión de SOL): WF-02 txt2img del concurso produce la masa; el emplazamiento en la plaza se hace en la correría del WF-03/E1 (inpaint sobre foto CC BY-SA de `earth2rhino3d/ref/` + massing como calibración de cámara/máscara). La matriz conviene que fije seeds de la masa para poder reusarlos cuando llegue el emplazamiento.

## 8. Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]]
- [[proyectos/concurso-gaudi-nexus/flujos/00-index|flujos — fichas del curso]]
- [[proyectos/MVP_04.02-comfyui-arquitectura/WF-04-serie-txt2img/WF-04-serie-txt2img|WF-04 — receta SDXL validada]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]
- [[proyectos/STUDIO_OS-Emilia/presentacion/dashboard-comfy.html|dashboard-comfy]] (referencia visual, no wikilink)
