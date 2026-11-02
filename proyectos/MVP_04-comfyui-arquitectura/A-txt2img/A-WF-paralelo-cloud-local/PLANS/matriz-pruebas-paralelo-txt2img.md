---
tipo: plan
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, txt2img, paralelo, matriz, tests, comfy-cloud]
---

# Matriz de PRUEBAS paso a paso — txt2img paralelo (local ⟷ cloud · abiertos ⟷ privativos)

> Reglas: [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] (R2 escalado, R4 validación `/object_info` antes de correr).
> Base de convenciones y receta validada: [[proyectos/concurso-gaudi-nexus/workflows/00-aporte-matriz-pruebas|00-aporte-matriz-pruebas (@tim, 2026-10-30)]].
> **A cada corrida queda asentada en [[02-WF-log-paralelo]]** con prompt_id, seed y timestamp.
> Letras por convención MVP_04: A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img · G LoRA.
> **Presupuesto de tiempo (medido por @tim, WF-04 2.0.0)**: SDXL local 1216×832 = **651 s/corrida** → un grid de 3 valores ≈ 32 min; bloque L2 completo ≈ 2-3 h. Los grids C se reparten en 2 sesiones o corren en background. Runtime: `corre_comfyui.bat --directml 0 --force-fp16 --disable-cuda-malloc` + `--lowvram --cpu-vae` para SDXL.
> **Regla de @tim que manda en todas las vías: UNA variable por corrida** (prompt, seed y latente constantes; cada valor del grid C = corrida separada, nunca batch). El humano revisa cada salida una a una antes de la próxima corrida.

## Antes de tocar nada (checklist de arranque)

```
[ ] 1. ComfyUI local up (corre_comfyui.bat) → GET /system_stats OK
[ ] 2. Validar ambos JSONs vía /object_info (R4) — class_type + modelos en models/
[ ] 3. Re-aplicar patch model_management.py:324 si ComfyUI se actualizó (nota @tim)
[ ] 4. comfy cloud: login y confirmar créditos/plan
[ ] 5. L4: confirmar API key/credits y catálogo real de nodos API (list_api_nodes)
[ ] 6. Carpeta salidas/ creada con subfolder propio por vía
```

## Estructura común de cada bloque de test

Cada vía (L1..L4) corre sus tests enumerados. Cada corrida = exactamente un test:
`T{vía}-{nn} · {letra} — descripción`. Ej: `T2-05 · C — cfg 3.5`.

---

## Vía L1 — Local SD1.5 (RX 570) · `workflow_txt2img_estadio.json` — 12 tests

> Checkpoint SD1.5 en disco: `architecturerealmix_v11` (@tim §6). Juggernaut-XL es SDXL y NO aplica acá.

| # | Letra | Test | Cambio |
|---|---|---|---|
| T1-01 | A | Baseline estadio: 3 corridas idénticas | seed fija 42 ×3 |
| T1-02 | B | Prompt "día nublado" vs "golden hour" | solo positive |
| T1-03 | B | Prompt en español vs inglés del mismo edificio | solo idioma |
| T1-04 | C | cfg 2.5 vs 4.5 vs 7 | grid 3 corridas |
| T1-05 | C | steps 15 vs 30 vs 50 | grid 3 corridas |
| T1-06 | C | scheduler: karras vs euler_a | 2 samplers |
| T1-07 | D | checkpoint `architecturerealmix_v11` → `sd-v1-5-inpainting` | D-modelo |
| T1-08 | E | 512×512 vs 512×768 vs 768×512 | 3 aspects |
| T1-09 | F | + ControlNet canny (draft de n_03, croquis) | img2img-light |
| T1-10 | G | LoRA loras-locales (weight 0.6 vs 1.0) | style-transfer |
| T1-11 | E+ | + ImageUpscale (RealESRGAN_x4plus, en disco) + denoise 0.2 | refina |
| T1-12 | A+ | **D-migración**: re-corre el prompt Sagrada M01–M20 (ya corrido SD1.5, en INDICE-RENDERS) migrado a L2-SDXL para comparar | reproducibilidad cruzada |

## Vía L2 — Local SDXL · `A-WF-estadio/workflow_txt2img_estadio_sdxl.json` + `WF-vivienda/...` — 12 tests

> Timing: 651 s/corrida a 1216×832.

| # | Letra | Test | Cambio |
|---|---|---|---|
| T2-01 | A | Baseline estadio 3 idénticas (seed 42 ×3) | repro |
| T2-02 | B | Prompt vivienda vs estadio | 2 prompts |
| T2-03 | B | Negative prompt vacío vs tuned | impacto del negative |
| T2-04 | C | grid cfg {3, 4, 7} | 3 corridas |
| T2-05 | C | grid steps {30, 35, 50} | 3 corridas |
| T2-06 | C | sampler dpmpp_2m+karras vs euler+normal | comparativa |
| T2-07 | D | Juggernaut v9 → otro SDXL en disco (o el nuevo que se descargue) | modelo |
| T2-08 | E | 1216×832 vs 1024×1024 vs 832×1216 | 3 aspects |
| T2-09 | F | + ControlNet dual (depth + canny, valida de WF_v1.1b) | img2img |
| T2-10 | G | LoRA Gaudi (lora-rhino-to-image-gaudi) weight sweep {0.5, 1.0} | estilo |
| T2-11 | E+ | Hires-fix: RealESRGAN ×2 + 2.º KSampler denoise 0.15-0.35 (R2) | upscale |
| T2-12 | — | **Timing**: duración documentada EN CADA corrida | economía GPU |

## Vía L3 — ComfyUI Cloud · mismo grafo de L1/L2 — 10 tests

> El grafo es estándar (CheckpointLoaderSimple → CLIP ×2 → EmptyLatentImage → KSampler → VAEDecode → SaveImage): sin nodos custom, compatible con Comfy Cloud.
> Validar contra el `/object_info` de la plataforma (excepción R4 línea 110). La lib de Comfy Cloud **debe revisarse: no asume que Juggernaut exista** — si falta, se elige el abierto equivalente y se documenta la sustitución.

| # | Letra | Test | Cambio |
|---|---|---|---|
| T3-01 | A | Baseline estadio cloud (3 idénticas) | repro cloud |
| T3-02 | A | Seed idéntico a L2 → **comparar píxel/visual con L2** solo si checkpoint idéntico; sino "no comparable" y pasa a timing | comparabilidad |
| T3-03 | B | mismo prompt del test B (inglés/cloud) | texto |
| T3-04 | C | grid cfg (2-3 corridas) | params |
| T3-05 | C | grid steps (2-3 corridas) | params |
| T3-06 | D | checkpoint que existe solo en el cloud | catálogo |
| T3-07 | E | 1024×1024 (cloud sin límite VRAM) | res |
| T3-08 | F | + ControlNet desde cloud | img2img |
| T3-09 | — | **Timing + créditos por corrida** | economía |
| T3-10 | — | Correr el mismo grafo arrastrando el `_ui.json` al canvas cloud | UX |

## Vía L4 — Privativos vía API nodes — 10 tests

> Requiere API key/créditos (COMFY_API_KEY o cuenta Comfy). Varios providers sin seed determinista: se documenta "sin seed" en el log.

| # | Test | Proveedor/modelo |
|---|---|---|
| T4-01 | Baseline Nano Banana (Gemini) 3 corridas → ¿reproduce? | nano-banana |
| T4-02 | Baseline GPT Image | openai |
| T4-03 | Mismo prompt estadio en cada proveedor + contra L2/L3 | comparativa |
| T4-04 | Prompt estilo editorial (dire banca de @tim rhetoric) | texto |
| T4-05 | Texto embebido en imagen ("cartelería") — qué proveedor mejor | text-render |
| T4-06 | Edit multi-turn (2-3 iteraciones sobre la misma imagen) | nano-banana |
| T4-07 | Seedream / Recraft | alternos |
| T4-08 | Multi-reference: 2-3 refs sobre un render propio + iteración | refs |
| T4-09 | Resolución máx disponible (1MP vs 2K) | res |
| T4-10 | **Costo por corrida** registrado en el log | economía |

---

## Paso a paso por corrida (estándar para TODOS los tests)

1. Confirmar servidor/servicio objetivo vivo y validado (R4)
2. Duplicar/crear el JSON de test con prefijo de salida correcto
3. Encolar: MCP `enqueue_workflow` (local) o comfy-cli/API (cloud)
4. Poll (`queue` → `get_history`) hasta término
5. Guardar salida en `salidas/` con nomenclatura `n_XX-{L}-{NN}`
6. Registrar en [[02-WF-log-paralelo]]: prompt_id, seed, duración, costo (L3/L4), veredicto HUMANO (@tim §4: Sol revisa y clasifica keeper)
7. Si falla → diagnóstico (`get_history action:"diagnose"`) + fail documentado
8. Al cerrar la vía: resumen comparativo (imágenes lado a lado por test B/C/D/E + tabla de tiempos/costos)

## Template de registro por corrida

```
Vía: L? · Test: T?-{nn} · Letra: ? · Fecha: YYYY-MM-DD
prompt_id: · seed: · duración: · costo: · revisado humano: s/-
Salida: n_??-?-??.png · Veredicto: keeper / descartar
```
