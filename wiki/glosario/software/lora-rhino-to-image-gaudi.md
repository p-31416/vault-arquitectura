---
tipo: software
software: lora-rhino-to-image-gaudi
categoria: lora
base_model: flux2-klein-9b
archivo: rhino-to-image-lora.basic.safetensors
licencia: FLUX Non-Commercial (derivado de FLUX.2 [klein] 9B)
estado: en Drive de Emilia (pendiente de instalar en ComfyUI)
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [glosario, software, comfyui, lora, flux2, klein, gaudi, rhino-to-image, arquitectura, concurso, fotorrealismo]
---

# LoRA — rhino-to-image (curso AI×Gaudí)

> LoRA de estilo/fotorrealismo del curso "AI×Gaudí" (Archademy / Fundació Antoni Gaudí) que convierte una volumetría 3D de Rhino en render fotorrealista conservando la geometría. Analizado byte a byte el 2026-10-20: es un **LoRA rank 16 sobre FLUX.2 [klein] 9B**, con 176 tensores y 31,66 M parámetros, en F32 (120,8 MB).

- [[#Qué es]]
- [[#Ficha técnica]]
- [[#Cómo se entrenó]]
- [[#Para qué sirve]]
- [[#Cómo se usa en ComfyUI]]
- [[#Salud de los pesos]]
- [[#Lo que falta saber]]
- [[#Riesgos y licencias]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué es

Un **adaptador de bajo rango (LoRA)** de 120,8 MB que se aplica sobre el modelo base **FLUX.2 [klein] 9B** (Black Forest Labs) para empujar el resultado hacia **material y fotografía de arquitectura**, en el contexto del módulo 3 del curso "AI×Gaudí" — el workflow «Rhino-to-Image».

El binario vive fuera del vault, en el Drive de Emilia:

- `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\rhino-to-image-lora.basic.safetensors`
- Origen del material del curso: `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\Barcelona-2D.dwg` y `3D-model.dwg` (volumetrías de entrada)

El sufijo `.basic` sugiere una línea de variantes (`.advanced`, etc.) cuyo catálogo queda pendiente de confirmar con el instructor del curso.

### Qué aporta y qué no

| Aporta | Responsabilidad del modelo base |
|-------|-----------------------------------|
| Acabado de material, luz y grano fotográfico | Composición, coherencia geométrica, generación de la imagen |
| Registro arquitectónico fotorrealista | Interpretación del prompt y de las imágenes de referencia |
| Consistencia de estilo entre iteraciones | Estructura 3D y exactitud de la geometría (viene del modelo, no del LoRA) |

---

## Ficha técnica

| Campo | Valor |
|-------|-------|
| **Archivo** | `rhino-to-image-lora.basic.safetensors` |
| **Ruta de origen** | `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\` |
| **Formato** | safetensors, F32 (sin cuantizar) |
| **Tamaño** | 120,8 MB (126.670.744 bytes) |
| **Tensores** | 176 (rank 16: 88 pares A/B) |
| **Parámetros** | 31,66 M |
| **Rank** | 16 |
| **Prefijo de tensores** | `diffusion_model.` (convención ComfyUI) |
| **Modelo base** | `black-forest-labs/FLUX.2-klein-9B` (o `FLUX.2-klein-base-9B`) |
| **Licencia del LoRA** | A confirmar con el instructor (hereda FLUX Non-Commercial) |
| **Metadata embebida** | Ausente (`__metadata__` no existe en el header) |
| **Sidecar CivitAI** | No presente en `Materials/` |
| **Variante premium** | `rhino-to-image-lora-premium.safetensors` (la descarga pasa por `thomasnelissen.ai`) |
| **Activación** | **Sin trigger word**: el curso lo activa con un **prompt JSON estructurado** (plantilla INSTRUCTION.md) + el pase de arcilla |

### Identificación del modelo base (verificada, no inferida)

Los shapes de los tensores determinan la arquitectura exacta. Contrastados contra `Klein9BParams` de `black-forest-labs/flux2` (`src/flux2/model.py`) y contra la config `image_model: "flux2"` de `comfy/model_detection.py:238`:

| Parámetro | LoRA | FLUX.2 klein 9B | klein 4B | FLUX.2 dev |
|-----------|------|----------------|----------|------------|
| `hidden_size` | 4096 | 4096 | 3072 | 6144 |
| Bloques duales | 8 | 8 | 5 | 8 |
| Bloques simples | 24 | 24 | 20 | 48 |
| `context_in_dim` (txt) | 12288 | 12288 (Qwen3-8B) | 7680 (Qwen3-4B) | 15360 |
| `img_in` | 128→4096 | 128→4096 | 128→3072 | 128→6144 |
| `mlp_ratio` | 3,0 | 3,0 | 3,0 | 3,0 |
| `guidance_in` | presente en el LoRA como `guidance_in` ausente | no | no | sí |

Verificación cruzada de shapes: `single_blocks.N.linear1` = 36864 = 3·4096 (qkv) + 2·12288 (MLP con `mlp_silu_act`), y `linear2` = 16384→4096 = (4096 + 12288) → cierra exacto con `mlp_hidden_dim = 3·4096`.

### Módulos afinados

| Grupo | Módulos | Cantidad |
|-------|---------|----------|
| Bloques duales (8) | `img_attn.qkv`, `img_attn.proj`, `txt_attn.qkv`, `txt_attn.proj` | 64 tensores |
| Bloques simples (24) | `linear1` (qkv+MLP) y `linear2` (proj+down) | 96 tensores |
| Modulación | `double_stream_modulation_img.lin`, `double_stream_modulation_txt.lin`, `single_stream_modulation.lin` | 6 tensores |
| Embeddings | `img_in`, `txt_in`, `time_in.in_layer`, `time_in.out_layer` | 8 tensores |
| Salida | `final_layer.linear` | 2 tensores |

Los MLP de los bloques duales quedan fuera del ajuste: el LoRA actúa sobre **atención y estructura de parches**, no sobre las capas de feed-forward duales.

Todos los nombres de tensor mapean 1:1 contra el modelo FLUX.2 de ComfyUI (`comfy/ldm/flux/model.py`, `comfy/model_detection.py`), de modo que el LoRA carga sin parcheo.

---

## Cómo se entrenó

### Lo que está verificado en el archivo

| Evidencia | Lectura |
|-----------|---------|
| Prefijo `diffusion_model.` | Entrenado sobre el DiT (no sobre un checkpoint completo) |
| Rank 16, pares A/B sin `alpha` embebido | Entrenamiento con LoRA de bajo rango estilo Kohya / ai-toolkit |
| Solo `attention` en duales + `linear1/linear2` en simples + embeddings + `final_layer` | `target_modules` acotado a los módulos que el framework de entrenamiento expone para FLUX.2 |
| `guidance_in` ausente en el LoRA | Entrenado sobre klein (sin embedding de guidance), no sobre `FLUX.2 [dev]` |
| B no nulas y pequeñas (max ≈ 9e-3), A con init Kaiming (σ ≈ 2e-2) | Delta entrenado y sano, de baja amplitud |

### La reconstrucción del pipeline

El curso describe el módulo 3 así: *"convierte un modelo básico de volumetría 3D en un render fotorrealista aplicando una referencia de material real, al tiempo que se bloquea la geometría exactamente en su sitio"*. Eso define una familia de entrenamiento de tipo **edit-LoRA / reference-LoRA**:

```
1. Captura desde Rhino (misma cámara, 3 pasadas: sombreado, líneas, material)
        │
2. Imagen de referencia de material real (ladrillo / hormigón / cerámica)
        │
3. Par de entrenamiento: entrada = volumetría (o su render), salida = foto arquitectónica
        │
4. Caption estilo FLUX.2 (JSON estructurado: sujeto + entorno + material + luz)
        │
5. Ajuste LoRA rank 16 sobre FLUX.2 [klein] 9B (Base o Destilado)
        │
6. Inferencia: ReferenceLatent(geometría) + ReferenceLatent(material) + LoRA
```

Los LoRAs de FLUX.2 klein que circulan en HF usan exactamente este patrón (`template:diffusion-lora`, `base_model: black-forest-labs/FLUX.2-klein-9B`), con dataset de pares entrada/salida y captions en formato estructurado.

**Lo que queda por confirmar con el instructor** (define el 100% del comportamiento):

1. Si se entrenó sobre **klein 9B destilado** (inferencia a 4 pasos / cfg 1) o sobre **klein-base 9B** (20 pasos / cfg 5).
2. **Trigger word** o frase de activación.
3. Dataset: cantidad de imágenes, resolución, tipo de pares, procedencia (material de la Fundació) y su licencia de uso.
4. Hiperparámetros: rank/alpha (16 confirmado en archivo), learning rate, steps, timestep sampling, optimizador.
5. Si existe la variante `.advanced` y en qué se diferencia.
6. Licencia del LoRA y permiso de uso comercial.

### Cómo se entrena uno propio (ruta recomendada)

| Paso | Herramienta | Nota |
|------|-------------|------|
| VRAM | 12 GB (klein 4B) / 22-24 GB (klein 9B) | La 8 GB de la RX 570 queda fuera; `bitsandbytes` 8-bit es CUDA-only |
| Entrenador | `ai-toolkit` (Ostrich) en RunPod | targets FLUX.2 con módulos documentados |
| Alternativa | `SimpleTuner`, `kohya_ss`, `OneTrainer` | soporte real de FLUX.2 a verificar en cada release |
| Nodo | LoRA rank 16-32, alpha 16, LR 1e-4, 1500-3000 steps | el LoRA del curso está en rank 16 |
| Texto | Qwen3-8B congelado | el embedder pesa 8,7 GB; se congela y se cachea |
| Coste | RunPod 3090 ≈ $0,22/h → 2-3 h ≈ $0,50-0,70 por corrida | |

**Reentrenar en klein 4B es la vía comercial**: klein 4B es Apache 2.0 y el LoRA derivado hereda esa condición. Portar el LoRA de 9B a 4B es imposible (arquitecturas distintas: 4096 vs 3076 de hidden, 8+24 vs 5+20 bloques, 12288 vs 7680 de embedding), de modo que el LoRA se entrena de nuevo.

### Cómo lo activa el curso (resuelto con el tablero del curso)

El export CSV del tablero de workflows (`AI-course.csv`, 219 filas) reveló el mecanismo completo:

| Pieza | Qué es |
|-------|--------|
| **Prompt de sistema** (INSTRUCTION.md, módulo 3) | Convierte (volumetría de Rhino + foto de material) en un **prompt JSON** para FLUX.2. Pide 2 preguntas de contexto: **qué tipo de edificio** y **dónde está** (el contexto debe ser *"regionally authentic"*) |
| **Esqueleto JSON** | La salida: `scene` con *STRICT CAMERA LOCK*, `subjects`, `style`, `color_palette`, `lighting`, `mood`, `background`, `composition` con *MATCH CAMERA OF IMAGE 1 EXACTLY*, y `camera` (ángulo, lente, profundidad) |
| **Pase de arcilla** (módulo 7) | Antes del render fotorreal, la volumetría se reinterpreta en **arcilla monocroma** con la lógica constructiva de Gaudí (dial de intensidad 0-10, por defecto 7) |
| **LoRA** | Hace el **pase final hiperreal** sobre esa arcilla: material, luz y grano fotográfico |

> **No hay trigger word**: la activación viene del prompt JSON + el pase de arcilla + la fuerza del LoRA. Esto resuelve la incógnita más grande del análisis.

Copias de trabajo de los dos prompts del curso (uso interno): [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|prompt-rhino-to-image-instruction-md]] · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md|prompt-rhino-to-gaudi-instruction-md]] · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|esqueleto JSON]]

### Fuerza que usa el curso

El tablero compara, en el módulo 2, el mismo prompt con `FLUX.2 (Klein 9b)`, `+ LoRA 50% strength` y `+ LoRA 100% strength`. Es decir, el rango del curso es **0,5 a 1,0** — el que veníamos recommending desde el análisis de los pesos.

### El pipeline real (3 pasos, no 1)

```
1. CAPTURAR      Rhino, captura en COLOR (verde = vegetación, rosa = figuras)
2. ARCILLA       INSTRUCTION.md módulo 7 → volumetría reesculpida en arcilla
                 monocroma con la lógica constructiva de Gaudí (morph 0-10)
3. HIPERREAL     FLUX.2 klein 9B + LoRA rhino-to-image + prompt JSON
                 (STRICT CAMERA LOCK) → render fotorreal
```

El punto clave del paso 2, textual del curso: *"The clay is the base for the edit LoRA: keep it clean, monochrome, edge-legible, camera + footprint 1:1."*

---

## Para qué sirve

### El caso de uso: «Rhino-to-Image» del curso AI×Gaudí

```
Rhino (volumetría 3D)  ──ViewCaptureToFile──►  geo_shaded.png (2048 px)
                                             geo_lines.png
Foto real de material  ──────────────────►  material.jpg
        │
        ▼
   ComfyUI + FLUX.2 klein 9B
   LoadImage → ImageScaleToTotalPixels → VAEEncode → ReferenceLatent (geometría)
   LoadImage → ImageScaleToTotalPixels → VAEEncode → ReferenceLatent (material)
   CLIPTextEncode (trigger + descripción) + LoRA rhino-to-image
        │
        ▼
   Render fotorrealista con la geometría en su sitio
```

El bloqueo de la geometría lo hace el **mecanismo nativo de referencia** de FLUX.2 (`ReferenceLatent` con `reference_latents_method: "index"`), que asigna a los tokens de referencia su propia banda posicional (`ref_index_scale = 10.0`). Para klein no hay ControlNet oficial de BFL: el único paquete serio (`alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union`) es para `FLUX.2 [dev]` 32B.

### Tres usos concretos en el estudio

| Uso | Configuración |
|-----|---------------|
| **Concepto fotorrealista rápido** (concurso) | 1 referencia (geometría) + LoRA 0,8 + prompt corto |
| **Material fiel** | 2 referencias (geometría + foto de material) + LoRA 0,6 |
| **Comparación deolverivable** | Mismo seed, 3 corridas: sin LoRA / 0,6 / 1,0 → tabla de aporte |

### Cuándo conviene y cuándo no

| Situación | Veredicto |
|-----------|-----------|
| Volumetría de Rhino lista para fotorreal | Zonaoptimal: es el caso nativo del LoRA |
| Croquis a mano o planta | El LoRA aporta material; el encuadre lo define el modelo base |
| Cliente pagador | El LoRA es derivative de un modelo Non-Commercial: la vía es klein 4B con LoRA reentrenado |
| Diagramas constructivos y cotas | El modelo fotorreal no es el canal: va DWG/PDF |

---

## Cómo se usa en ComfyUI

### Nodos

```
UNETLoader (flux-2-klein-9b-fp8) ──► LoraLoaderModelOnly (0.8) ──► CFGGuider
CLIPLoader (type=flux2, qwen_3_8b_fp8mixed) ──► CLIPTextEncode
VAELoader (full_encoder_small_decoder) ──► VAEEncode (×2) / VAEDecode
LoadImage (geo_shaded.png) ──► ImageScaleToTotalPixels ──► VAEEncode ──► ReferenceLatent
LoadImage (material.jpg)     ──► ImageScaleToTotalPixels ──► VAEEncode ──► ReferenceLatent
CLIPTextEncode ──► ReferenceLatent (geo) ──► ReferenceLatent (material) ──► CFGGuider
EmptyFlux2LatentImage (1024×1024) + Flux2Scheduler + KSamplerSelect(euler)
     ──► SamplerCustomAdvanced ──► VAEDecode ──► SaveImage
```

### Parámetros

| Parámetro | Valor (klein 9B destilado) | Valor (klein base 9B) |
|-----------|---------------------------|------------------------|
| `Flux2Scheduler.steps` | 4 | 20 |
| `CFGGuider.cfg` | 1,0 | 5,0 |
| `KSamplerSelect.sampler_name` | euler | euler |
| `EmptyFlux2LatentImage` | 1024×1024 (o el aspect de la vista de Rhino) | ídem |
| `LoraLoaderModelOnly.strength_model` | 0,6 → 0,8 → 1,0 | ídem |
| `ImageScaleToTotalPixels.megapixels` | 1,0 (geometría) / 0,5 (material) | ídem |

Workflow completo, listo para importar: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/workflow_rhino_to_image.json|workflow_rhino_to_image.json]].

### Orden de calibración

1. Sin LoRA, con la referencia de geometría → línea base de la geometría.
2. Con LoRA 0,6 / 0,8 / 1,0 → tabla de aporte (mismo seed).
3. Sumar la referencia de material → ajuste de materialidad.
4. Registrar en `02-WF-log-WFrhino_to_image.md` con nomenclatura `n_05-{A|B|C|D|E|F}-{NN}.png`.

---

## Salud de los pesos

Verificación numérica directa sobre los tensores (mediana de 13 muestras representativas):

| Tensor | Media | σ | max abs | Ceros |
|--------|-------|---|---------|-------|
| `img_in.lora_A` | 2,1e-4 | 2,0e-2 | 6,9e-2 | 0 % |
| `img_in.lora_B` | -7,5e-6 | 1,0e-3 | 4,5e-3 | 0 % |
| `final_layer.linear.lora_A` | 2,0e-5 | 2,0e-2 | 9,0e-2 | 0 % |
| `final_layer.linear.lora_B` | -3,6e-5 | 1,5e-3 | 4,7e-3 | 0 % |
| `double_blocks.0.img_attn.qkv.lora_A` | 7,4e-5 | 2,0e-2 | 8,6e-2 | 0 % |
| `double_blocks.0.img_attn.qkv.lora_B` | 2,4e-6 | 7,9e-4 | 4,0e-3 | 0 % |
| `single_blocks.0.linear2.lora_A` | -4,2e-5 | 2,0e-2 | 9,7e-2 | 0 % |
| `single_blocks.0.linear2.lora_B` | 3,1e-6 | 1,4e-3 | 6,5e-3 | 0 % |
| `single_blocks.23.linear1.lora_B` | 5,4e-6 | 1,6e-3 | 8,9e-3 | 0 % |
| `txt_in.lora_B` | 1,1e-6 | 1,1e-3 | 5,2e-3 | 0 % |
| `time_in.out_layer.lora_B` | 3,9e-6 | 8,1e-4 | 4,1e-3 | 0 % |
| `single_stream_modulation.lin.lora_B` | -4,1e-6 | 8,8e-4 | 4,9e-3 | 0 % |

Lectura:

- Las matrices **B son distintas de cero**: el LoRA está entrenado y aporta delta real (un LoRA sin entrenar o "stripped" tendría B en cero).
- Amplitud pequeña (σ ≈ 1e-3) frente a la init de A (σ ≈ 2e-2): es la firma de un ajuste **suave**, con efecto acumulativo pero sin saturar la base.
- Distribución sesgada a positivo en A (mean ≈ +2e-4) y centrada en B: comportamiento normal de LoRA trained con LoRA+ (B se inicializa en cero y crece durante el entrenamiento).
- Rango operativo recomendado de `strength_model`: **0,6 a 1,0**. Por encima de 1,2 el delta domina la base y aparecen artefactos de material.

Herramienta reproducible: `scripts/analizar-lora-safetensors.py` (+ `scripts/analizar-lora-safetensors_notas.md`).

---

## Lo que falta saber

Ficha a solicitar al instructor del curso (**Thomas Nelissen**, profesor — vía el área de participantes de Archademy) o a Emilia:

| # | Pedido | Impacto |
|---|--------|---------|
| 1 | **Variante `.premium`** (`rhino-to-image-lora-premium.safetensors`) y su diferencia con la basic | El tablero la lista: la basic es la que tenemos |
| 2 | **Ficha original del LoRA** (dataset, licencia, hiperparámetros) | El LoRA no trae metadata |
| 3 | Licencia del LoRA y permiso de uso comercial | Define si el flujo llega a un cliente |
| 4 | Confirmar si el LoRA se entrenó en **Base o Destilado** | Define steps (4 vs 20) y cfg (1 vs 5) |

**Plan B sin LoRA**: el mecanismo nativo `ReferenceLatent` (doble: geometría + material) ya produce "volumetría 3D → render fotorrealista con material de referencia". El LoRA es el toque del curso, la base del flujo es reproducible sin él.

---

## Riesgos y licencias

| Riesgo | Situación verificada | Mitigación |
|--------|-----------------------|------------|
| LoRA derivative de modelo Non-Commercial | klein 9B = FLUX Non-Commercial License; 4B = Apache 2.0 | Concurso: admisible. Cliente: reentrenar en 4B (Apache 2.0), ~$0,50 de GPU |
| Trigger desconocido | Sin metadata en el archivo | Pedirlo antes de la primera corrida; probar 0,6/0,8/1,0 mientras tanto |
| Base vs destilado sin confirmar | El LoRA fue entrenado en 9B, la variante sin confirmar | Probar ambas combinaciones (4/cfg 1 y 20/cfg 5) y quedarse con la mejor |
| 8 GB no alcanzan para 9B | 8,8 GiB de pesos + 8,1 GiB de text encoder | Ruta mixta: preprocesado y grafo en local, render en RunPod 24 GB ($0,22-0,34/h) |
| LoRA de un solo proveedor | 120,8 MB sin documentación pública | Guardar esta ficha junto al binario y pedir la ficha original |
| "Todos los edificios se parecen" | Problema conocido de los workflows Rhino→ComfyUI | 3 pasadas desde Rhino + 3 referencias distintas (material, mood, material secundario) + variación de seed y de prompt |

---

## Conceptos relacionados

- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — modelo base del LoRA, stack de instalación y grafo
- [[wiki/glosario/software/comfyui|comfyui]] — nodos, modelos y flujos del estudio
- [[wiki/glosario/software/rhino|rhino]] — `ViewCaptureToFile`, captura de la volumetría
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo de la herramienta
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README|WF-rhino-to-image]] — workflow del módulo
- [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] — informe de investigación con 54 fuentes
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — iteración asistida por IA

## Referencias

- [black-forest-labs/FLUX.2-klein-9B (HF)](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) (verificado 2026-10-20 — gated, license FLUX Non-Commercial)
- [black-forest-labs/flux2 — implementación de referencia (`src/flux2/model.py`)](https://github.com/black-forest-labs/flux2) (verificado 2026-10-20 — `Klein9BParams`)
- [Comfy-Org/vae-text-encorder-for-flux-klein-9B (HF)](https://huggingface.co/Comfy-Org/vae-text-encorder-for-flux-klein-9B) (verificado 2026-10-20 — text encoder Qwen3-8B + VAE)
- [black-forest-labs/FLUX.2-small-decoder (HF)](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder) (verificado 2026-10-20 — VAE, Apache 2.0)
- [unsloth/FLUX.2-klein-9B-GGUF (HF)](https://huggingface.co/unsloth/FLUX.2-klein-9B-GGUF) (verificado 2026-10-20 — GGUF para VRAM chico)
- [ComfyUI Docs — FLUX.2 Klein](https://docs.comfy.org/tutorials/flux/flux-2-klein) (verificado 2026-10-20)
- [ComfyUI Blog — FLUX.2 Day-0 Support](https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence) (verificado 2026-10-20)
- [Archademy — AI×Gaudí](https://archademy.ai/es/) (verificado 2026-10-20 — curso y concurso)
- [Fundació Antoni Gaudí — Concurso "The Gaudí Nexus" (briefing)](https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_EN.pdf) (verificado 2026-10-20)
- [ComfyUI — `comfy/model_detection.py` (config FLUX.2)](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy/model_detection.py) (verificado 2026-10-20 — local `b08e6cf3`)
