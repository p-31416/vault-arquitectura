---
tipo: proyecto
proyecto: concurso-gaudi-nexus
origen: informe de @tim (subagente), sesion 2026-10-30, verificado contra fuentes oficiales
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [concurso, gaudi-nexus, lora, entrenamiento, flu2, klein-4b, publicacion, civitai, huggingface, runpod]
idioma: es
---

# LoRA de estilo propio del concurso Gaudí Nexus — plan (v2026-10-30)

> Objetivo de SOL: entrenar un LoRA con el estilo visual de las imágenes del concurso y publicarlo como modelo propio (nuestro). Informe generado por @tim; nada se entrena sin el `s` de SOL.

## 1. Resumen ejecutivo

**Recomendación: LoRA de estilo sobre FLUX.2 [klein] 4B Base (Apache 2.0), entrenado en RunPod con ai-toolkit, publicado en Civitai + HuggingFace bajo Apache 2.0.**

- La licencia decide: klein **4B** es Apache 2.0 (verificado en la model card de HF) → un LoRA derivado se publica y se usa comercialmente. klein **9B** es FLUX Non-Commercial → un LoRA sobre 9B hereda esa restricción y queda fuera del objetivo "que sea nuestro".
- El curso ya dió la receta de referencia (rank 16, 176 tensores, F32) — la replicamos sobre 4B con nuestro dataset y nuestro trigger.
- Local (RX 570 8 GB, DirectML) aporta curación, captioning y validación SD 1.5/SDXL; el entrenamiento corre en RunPod: 3090 Community $0,22/h × 2–3 h ≈ **$0,50–0,70 por corrida**.
- El dataset ya existe: **80 renders con metadata completa** en `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md` + las salidas de los WF del concurso.
- El criterio de la Fundació ("lógica constructiva, no imitación de estilo") juega a favor: el LoRA captura el estilo visual del estudio y la lógica la aporta el proyecto.

## 2. Receta de entrenamiento

**Base:** `black-forest-labs/FLUX.2-klein-base-4B` (gated, Apache 2.0 — pedir acceso con la cuenta HF del estudio). Base undistilled = señal de entrenamiento completa (doc oficial BFL).

### Dataset (30–60 imágenes, objetivo inicial 40)

| Fuente | Cuántas | Nota |
|---|---|---|
| Renders WF-rhino-to-image + WF del concurso (`salidas/`, indexados en INDICE-RENDERS) | 25–35 | Ya traen seed/steps/cfg/prompt en la metadata PNG |
| Moodboard del concurso (`activos/proyectos/concurso-gaudi-nexus/`) | 5–10 | Referencias de material/luz |
| Capturas Rhino (3 pasadas, misma cámara) | 5 | Ancla de geometría |

- **Resolución:** 1024px mínimo (doc BFL); los renders de klein salen a 1024² — perfectos tal cual.
- **Cap por concepto:** máx. 15 por categoría (fachada / interior / massing / detalle material) para que el LoRA aprenda el estilo y la distribución de conceptos.
- **Captions:** lenguaje natural estilo FLUX.2 (el mismo dialecto del prompt JSON que ya usamos), describiendo todo lo visible **excepto el estilo** — el estilo lo absorbe el trigger. Trigger propio: **`gaudinexusstyle`** al inicio de cada caption. Naming: `NNN_concepto_caption.txt` junto a cada imagen (convención ai-toolkit: imagen y `.txt` mismo nombre).

### Hiperparámetros

| Parámetro | Valor | Justificación |
|---|---|---|
| rank / alpha | 16 / 16 | El LoRA del curso usa rank 16 y funcionó; liviano (~30–60 MB en 4B) |
| LR | 1e-4 | Rango BFL para estilo: 8e-5–1e-4 |
| steps | 2000 (rango BFL estilo: 1500–2500) | Con checkpoint cada 500 steps para elegir el mejor |
| batch | 1 | Dataset chico, VRAM holgada |
| resolución | 1024px, multi-aspect | ai-toolkit maneja buckets |
| optimizer | AdamW 8-bit | Estándar ai-toolkit |

- **Validación con seeds fijos:** 3 prompts de validación (fachada exterior WS / interior MLS / massing aérea) × 3 seeds fijos, sampleados cada 500 steps dentro de ai-toolkit. Una variable por corrida: v01 receta base; v02 cambia steps; v03 cambia LR. Cada corrida se registra en `02-WF-log-WFloraestilo.md` con la nomenclatura `n_XX-{A–G}-{NN}.png` (letra **G = LoRA**, ya en reglas).

**Dónde corre:** RunPod, template one-click de ai-toolkit (blog oficial de BFL en HF: ~$0,50/corrida en 4090; en 3090 Community $0,22/h sale menos). La RX 570 queda para curar, captionar y comparar resultados.

## 3. Plan de publicación

| Pieza | Decisión propuesta |
|---|---|
| Plataforma principal | **Civitai** (comunidad de LoRAs; wizard con trigger words, training params y licencia) |
| Espejo | **HuggingFace** (model card con `base_model: adapter:black-forest-labs/FLUX.2-klein-base-4B`) |
| Licencia del artefacto | **Apache 2.0** (hereda de klein 4B; en Civitai se marcan los permisos: permitir merges, permitir vender imágenes generadas, requerir crédito) |
| Nomenclatura | `concurso-gaudi-nexus-style-v01` → `...-v02` por corrida |
| Trigger word | `gaudinexusstyle` |
| Model card mínimo | Qué es (estilo visual del estudio para arquitectura fotorrealista), base model, trigger, recommended settings (strength 0,6–1,0; destilado 4 steps/cfg 1 · base 20 steps/cfg 5), 6–8 imágenes de ejemplo con metadata, link al estudio |
| Metadata embebida | ai-toolkit escribe trigger en el header del `.safetensors` (el LoRA del curso la carecía — nosotros lo hacemos bien) |

## 4. Costo/tiempo comparado

| Ruta | Costo | Tiempo | Veredicto |
|---|---|---|---|
| Local RX 570 (DirectML) | $0 GPU | Entrenamiento inviable: ai-toolkit y sd-scripts requieren CUDA; `bitsandbytes` 8-bit es CUDA-only | Curación + validación de inferencia SD1.5/SDXL |
| RunPod 3090 Community — **klein 4B** | **$0,50–0,70/corrida** | 2–3 h por corrida | **Ruta recomendada** (BFL: 4B pide 12 GB VRAM en la 3090 entra justa) |
| RunPod 3090/4090 — klein 9B | $0,70–1,20/corrida | 3–4 h | Solo si 4B queda corto en calidad; el artefacto publicado quedaría Non-Commercial |
| RunPod 3090 — SDXL (kohya) | ~$0,50/corrida | ~2 h | Plan B: kohya soporta SDXL; licencia OpenRAIL permite publicar |
| Civitai on-site trainer | Buzz (créditos de la cuenta) | Cola variable | Soporta engine AI-Toolkit para "Flux2 Klein", pero el dataset sube a su storage (retención 30 días) — para material del concurso se prefiere RunPod, disco que desaparece al terminar el pod |

**Presupuesto total del experimento:** 3–4 corridas + validación ≈ **$3–5 USD**. Coherente con el presupuesto del concurso ya estimado ($2–5 de renders).

## 5. Decisiones que piden `s` de SOL

1. Aprobar el gasto RunPod (~$3–5) y crear cuenta/API key si falta.
2. Aprobar el trigger `gaudinexusstyle` (o proponer otro).
3. Decidir si el dataset v1 se entrena sobre renders generados con klein 9B (calidad máxima) o klein 4B (cadena de licencias 100% Apache 2.0 de punta a punta).
4. `s` para escribir la estructura del WF (`proyectos/concurso-gaudi-nexus/workflows/WF-lora-estilo/`) y la propuesta de ficha para @vaultworm-arq.

## 6. Preguntas legales → @sherlock (verificado lo central, quedan los bordes)

1. **Outputs de klein 9B como training data de un LoRA comercial:** la FLUX Non-Commercial License regula el uso del modelo y sus outputs; usar esos renders para entrenar un artefacto Apache 2.0 que se publica es zona gris → leer la cláusula exacta del texto de licencia de BFL.
2. **Derechos sobre imágenes de obra de Gaudí** usadas en el moodboard (fotos de terceros: fotógrafos, Fundació) — qué puede entrar al dataset y con qué crédito.
3. **El concurso:** ¿usar los renders con premio en metálico cuenta como uso comercial bajo Non-Commercial? (pregunta ya abierta en la ficha del LoRA del curso).
4. **Precedentes:** estudios que publicaron LoRAs de estilo con su marca (qué licencia aplicaron y cómo redactaron el model card).

## 7. Experimento E1 — primer `¿Avanzo?`

**E1 — dataset + primera corrida (~$1):**
1. Curar 40 imágenes del acervo (INDICE-RENDERS + salidas del concurso + moodboard) → `activos/proyectos/concurso-gaudi-nexus/lora-dataset-v01/`.
2. Escribir 40 captions con trigger `gaudinexusstyle` (los redacta @tim, SOL los revisa).
3. Una corrida RunPod 3090: ai-toolkit, klein-base-4B, rank 16, LR 1e-4, 2000 steps, checkpoints cada 500.
4. Validar los 4 checkpoints con los 3 prompts × 3 seeds fijos y elegir v01.

## 8. Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS|INDICE-RENDERS]] — los 80 renders con metadata (dataset candidato)
- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]] — el proyecto
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — el LoRA del curso (receta de referencia)
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — modelo base, stack de instalación
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — base local RX 570

## 9. Fuentes verificadas (2026-10-30, sin 404)

- Model card `black-forest-labs/FLUX.2-klein-4B` (HuggingFace) — Apache 2.0, nota de release que confirma 9B Non-Commercial
- `https://docs.bfl.ai/flux_2/flux2_klein_training` — hiperparámetros, hardware, community tools
- README `ostris/ai-toolkit` — soporte klein-base-4B/9B
- Blog HF de BFL "Fine-tune FLUX.2 [klein] with a LoRA under 60 minutes" — template RunPod ~$0,50
- `https://runpod.io/pricing` (2026-10-08: 3090 Community $0,22/h, 4090 $0,34/h, A5000 $0,16/h)
- README `kohya-ss/sd-scripts` — FLUX.2 klein fuera de su matriz de soporte
- `education.civitai.com` — upload wizard, licencias, on-site trainer

## 10. Contexto leído

`proyectos/concurso-gaudi-nexus/index.md` · ficha del LoRA del curso · `raw/sessions/2026-10-20-sesion-lora-rhino-to-image.md` · `raw/sessions/2026-10-28-sesion-loras-comfyui-locales.md` · `raw/research/2026-10-20-miro-curso/` (secciones LoRA LINKS / TRAINING / COMPARISON — frames vacíos en el export; útil en cards de MODULE 2: comparación con/sin LoRA al 50% y 100%) · pbk-comfyui. Nota: la delegación a @sherlock quedó pendiente por límite de profundidad; la verificación central la hizo @tim directo sobre fuentes oficiales.
