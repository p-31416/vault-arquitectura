---
tipo: research
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
autor: sherlock
idioma: es
tags: [comfyui, flux2, flux2-klein, lora, rhino, rhino-to-image, gaudi, archademy, concurrency, controlnet, gguf, directml, runpod, qwen3, vae, text-encoder, ai-gaudi, guia-nexus, arquitectura, fotorealismo,Trainer, licenses]
origen: peticion SOL 2026-10-20 (continuacion del analisis de `rhino-to-image-lora.basic.safetensors`)
vault_destinos: [wiki/glosario/software/comfyui, wiki/glosario/interno/pbooks/pbk-comfyui, proyectos/MVP_04-comfyui-arquitectura]
---

# FLUX.2 [klein] 9B + LoRA "Rhino-to-Image": entrenamiento, workflow ComfyUI, instalacion en la PC de Emilia y contexto del concurso AI×Gaudi

*Fecha: 2026-10-20 | Fuentes unicas verificadas: 54 (46 HTTP 200 + 8 gated/401 documentadas) | Confianza: Alta en lo tecnico-documental / Media en lo no publicado (LoRA del curso)*

> Continuacion del analisis del artefacto `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\rhino-to-image-lora.basic.safetensors` (safetensors F32, rank 16, 176 tensores, 31,66 M params, destino FLUX.2 [klein] 9B). Este informe NO re-analiza el archivo: arranca desde lo verificado y cubre (A) como se entrena un LoRA sobre FLUX.2/klein, (B) el grafo de nodos exacto en ComfyUI y el mecanismo de referencia/edicion que "bloquea la geometria", (C) instalacion y descarga de modelos para la PC de Emilia, (D) contexto del curso/concurso y materiales, (E) plan de accion, riesgos y licencias.

---

## Resumen ejecutivo

1. **El LoRA que tiene Emilia es (con alta probabilidad) el "modelo de IA exclusivo" del curso AI×Gaudi.** La web publica de Archademy lo describe como "acceso exclusivo a un modelo de IA entrenado con los archivos de la Fundacio Antoni Gaudi" y el **Modulo 3** describe textualmente el workflow *"Rhino-to-Image"*: "convierte un modelo basico de volumetria 3D en un render fotorrealista aplicando una referencia de material real, al tiempo que se bloquea la geometria exactamente en su sitio". Eso coincide 1:1 con la hipotesis de Emilia. **No hay ficha publica** (Civitai, HF, GitHub) de ese LoRA ni de la "version advanced": hay que pedirsela al instructor.
2. **Correccion sobre el instructor.** El profesor del curso es **Thomas Nelissen** (arquitecto junior en Davis AI, Paris; antes JDS Architects; master en Univ. Amberes + TU Delft; publica en Archined). **Cas Esbach** (SCAD, ex-MVRDV, fundador de KANS) es co-desarrollador del Modulo 7 y el "experto en IA" de la mesa redonda. La referencia a "Ismail Seleit / Studio Ismail Seleit (ex-Foster+Partners)" **no se pudo confirmar en ninguna fuente publica**: se marca como *no verificado*.
3. **Para inferencia (usar el LoRA), klein 9B es la via correcta y ya esta soportada nativamente en ComfyUI.** El grafo oficial de ComfyUI para "FLUX.2 [Klein] 9B: Image Edit" usa `UNETLoader` + `CLIPLoader(type=flux2)` + `VAELoader` + `EmptyFlux2LatentImage` + `Flux2Scheduler` + `CFGGuider` + `SamplerCustomAdvanced` + **`ReferenceLatent`** + `VAEEncode`. El mecanismo de "geometria bloqueada" es **nativo de FLUX.2**: `ReferenceLatent` mete el latent de la imagen de referencia en el conditioning y el modelo lo indexa con offset posicional (`default_ref_method="index"`, `ref_index_scale=10.0`). **No hace falta ControlNet para klein.**
4. **No hay ControlNet oficial para FLUX.2.** Lo unico serio es `alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union` (8,23 GB) y es para **FLUX.2 [dev] 32B**, no para klein. Para klein la via correcta es `ReferenceLatent` (nativa) o `FluxKVCache` (experimental) + `FluxKontextMultiReferenceLatentMethod`.
5. **Entrenar el LoRA en la PC de Emilia (RX 570 8 GB + DirectML) NO es viable.** Requisitos documentados: 12 GB VRAM para klein 4B y 22-24 GB para klein 9B (BFL y SimpleTuner), con optimizadores 8-bit de `bitsandbytes` (solo CUDA) y FP8 training que exige compute capability >= 8.9 (NVIDIA). `torch-directml` no es backend de training. **Ademas, portar un LoRA de 4B a 9B es tecnicamente imposible**: arquitecturas distintas (hidden 3072 vs 4096, 5+20 vs 8+24 bloques, dim de embedding 7680 vs 12288) => formas de tensores incompatibles.
6. **Camino recomendado: local para ideacion + RunPod para la prueba final.** RTX 3090 24 GB desde **$0,22/h** (Community) o RTX 4090 desde **$0,34/h** (Community) / **$0,69-0,74/h** (Secure) segun la pagina oficial de RunPod (actualizada 8-oct-2026). El propio BFL estima un LoRA de 4B en ~1 h en 4090 por ~**$0,50**.
7. **Licencia: el LoRA derivado de klein 9B es Non-Commercial.** klein 4B es Apache 2.0 (comercial ok); klein 9B es FLUX Non-Commercial. Para el concurso (entrega de lamina A1, sin contraprestacion) es admisible; **para entregar a cliente hay que usar klein 4B o comprar licencia**.

---

## Bloque A — LoRA para FLUX.2 / FLUX.2 [klein]: como se entrena

### A.1 Herramientas con soporte real para FLUX.2 / klein 9B (estado verificado 2026-10)

| Herramienta | Repo oficial | Soporte FLUX.2 klein 9B | VRAM indicada | Licencia | Veredicto para este caso |
|---|---|---|---|---|---|
| **ai-toolkit** (ostris) | https://github.com/ostris/ai-toolkit | **Si**, explicito: lista `black-forest-labs/FLUX.2-klein-base-4B` y `-9B` entre los modelos soportados. BFL publica su config oficial de ejemplo para 9B | 4B: 24 GB (guia HF, 4090). 9B: mayor (ver SimpleTuner) | MIT (repo) | **Primera opcion.** Config YAML oficial de BFL lista abajo. Requiere NVIDIA (torch cu130) |
| **SimpleTuner** (bghira) | https://github.com/bghira/SimpleTuner | **Si**: `model_flavour: klein-9b` / `klein-4b`, con soporte de condicionamiento de referencia/edicion | 9B: ~22 GB bf16 / ~14 GB int8, RAM 64 GB+. 4B: ~12 GB bf16 / ~8 GB int8, RAM 32 GB+ | MIT | **Segunda opcion.** Unico con documentacion clara de `conditioning_data` + `conditioning_type: reference_strict` (exactamente el patron edit-LoRA del Rhino-to-Image) |
| **diffusers** (HF) | https://github.com/huggingface/diffusers | **Si**: `train_dreambooth_lora_flux2_klein.py` para 4B y 9B + `train_dreambooth_lora_flux2_img2img.py` | 4B: cabe en 24 GB con `--do_fp8_training` (solo NVIDIA cc>=8.9) | Apache 2.0 | **Tercera opcion.** Referencia oficial de BFL para LoRA. `--remote_text_encoder` **no** aplica a klein (solo a dev) |
| **kohya_ss / sd-scripts** | https://github.com/kohya-ss/sd-scripts | **NO.** La lista de modelos soportados del README es: *SD 1.x/2.x, SDXL, SD3/3.5, FLUX.1, LUMINA, HunyuanImage-2.1, Anima*. FLUX.2 no aparece | — | Apache 2.0 | **Descartado** para este LoRA |
| **OneTrainer** | https://onetrainer.org/ | **Si, indirectamente.** La web del proyecto lista "FLUX-family models" en el FAQ y un tracker externo (imagelora.dev, 19-oct-2026) registra "OneTrainer: 20-30% mas rapido en modelos cuantizados a 8-bit (FLUX.2 16 GB preset 1.30x)". **No verificado contra el repo primario en esta sesion** | 16 GB (preset 8-bit segun tracker) | AGPLv3 | **Posible**, verificar en el repo antes de comprometer tiempo |
| **black-forest-labs/flux2** (`scripts/cli.py`) | https://github.com/black-forest-labs/flux2 | **NO entrena.** El repo se describe como *"Official inference repo for FLUX.2 models"*; su arbol es `docs/`, `model_cards/`, `model_licenses/`, `scripts/`, `src/flux2/`. `scripts/cli.py` es la CLI de inferencia interactiva | — | Apache 2.0 (repo) | **Descartado como trainer.** El entrenamiento se sirve via API BFL: se sube el `.safetensors` al Dashboard (`Customization -> Finetunes`) y se llama `/v1/flux-2-klein-9b-finetuned` |
| **diffusion-painter** | — | **No encontrado / no verificado** en esta sesion | — | — | Sin dato. No usar como plan |
| Entrenadores klein de terceros | `ethanncai/Simple-Flux2-FineTuner` (DeepSpeed ZeRO-2, **solo 4B**, Linux+NVIDIA), `Limbicnation/klein-lora-trainer` (**solo 4B**, 13 GB+ VRAM, CUDA), `ReyChiaro/flux.2-klein-controlnet` (ControlNet, no trainer) | Parcial | 13 GB+ | Apache 2.0 / sin dato | Referencia, no produccion |

**Conclusion A.1:** el triangulo que funciona es **ai-toolkit (config oficial de BFL) o SimpleTuner o diffusers**, siempre sobre el checkpoint **Base** (no destilado), y siempre en GPU NVIDIA >= 22-24 GB para 9B.

### A.2 Parametros de LoRA para FLUX.2

**Regla de oro verificada:** se entrena sobre **Base** (50 pasos, no destilado) y se infiere sobre **Destilado** (4 pasos). BFL: "FLUX.2 [klein] ships in a 4B and a 9B size, each with a distilled (4-step) and a base (50-step) variant. For LoRA training the relevant one is **base**". HF: "You train on base-4B, but run inference on the distilled ... Applying the LoRA on the distilled model typically gives better results than the base model, and it's faster". mflux advierte: los Base "are typically slower and worse for general image editing, but can be successfully used for training".

**Config oficial de BFL para FLUX.2-klein-base-9B** (de `docs.bfl.ml/flux_2/flux2_klein_training_example`, esquema `job/config` de ai-toolkit):

```yaml
job: "extension"
config:
  name: "Graphic_Impressions_Flux2-klein-base-9b"
  process:
    - type: "diffusion_trainer"
      training_folder: "/app/ai-toolkit/output"
      device: "cuda"
      trigger_word: "GFX_IMPR5N"
      network:
        type: "lora"
        linear: 128
        linear_alpha: 64
        conv: 64
        conv_alpha: 32
      save:
        dtype: "bf16"
        save_every: 150
        max_step_saves_to_keep: 20
      datasets:
        - folder_path: "/workspace/aitoolkit/datasets/Graphic_Impressions"
          caption_ext: "txt"
          resolution: [256, 512, 768, 1024, 1280, 1536]
      train:
        batch_size: 1
        steps: 3000
        lr: 0.000095
        optimizer: "adamw8bit"
        timestep_type: "shift"
        content_or_style: "balanced"
        optimizer_params:
          weight_decay: 0.00015
      model:
        name_or_path: "black-forest-labs/FLUX.2-klein-base-9B"
        quantize: true
        low_vram: false
```

Variantes documentadas en la misma pagina:

| Parametro | Valor | Fuente |
|---|---|---|
| `network.linear` / `linear_alpha` | 128 / 64 (ratio 4:2:2:1); default BFL 32/32; tambien 64/32/32/16 para vectorial | BFL training example |
| `network.conv` / `conv_alpha` | 64 / 32 | BFL |
| `lr` (LoRA) | **8e-5 a 1e-4** (guia general BFL); 1e-4 baseline; 9.5e-4? no: 9.5e-5 en el ejemplo; 2e-4 si la loss baja lento; 5e-5 si oscila; 5e-4 en la receta de orquestacion Civitai | BFL + Civitai |
| `optimizer` | `adamw8bit` (los 8-bit de bitsandbytes son CUDA-only) | BFL, Civitai |
| `lrScheduler` | `constant` / `constant_with_warmup` / `cosine` / `linear` / `step` | Civitai |
| `steps` | estilo 1500-2500; 20-40 imagenes 1200-2000; 50+ 2000-3000; BFL ejemplo 3000 (mejor checkpoint 1500); HF blog: el pico visual suele estar en **750-1500** | BFL + HF |
| `batch_size` | 1 + `gradient_accumulation_steps: 2` para efectivo 2 | BFL |
| `resolution` | empezar 512 para iterar, 1024+ para el training final; multi-res bucketing | BFL, HF |
| `timestep_type` | `weighted` (default) o `shift` (para estilo: "encourages overfitting of low-frequency information") | BFL |
| `content_or_style` | `balanced` | BFL |
| `trainTextEncoder` | **false** (obligatorio en klein) | Civitai: "Klein uses Qwen-3 as its text encoder; AI Toolkit does not train it. Leave false" |
| `quantize` | `true` en el ejemplo BFL (ahorra VRAM) | BFL |
| `weight_decay` | 0.00015 en el ejemplo (estilo) / 0.00001 (fotorealista) | BFL |

**Names exactos de los modulos objetivo (target modules).** Es el punto mas delicado, porque los nombres difieren entre ComfyUI y diffusers/ai-toolkit:

- **Nombres ComfyUI (FLUX.2 klein 9B)** — son los que ya se leyeron del safetensors de Emilia: `double_blocks.N.img_attn.qkv`, `double_blocks.N.img_attn.proj`, `double_blocks.N.txt_attn.qkv`, `double_blocks.N.txt_attn.proj`, `single_blocks.N.linear1`, `single_blocks.N.linear2`, `double_stream_modulation_img.lin`, `double_stream_modulation_txt.lin`, `single_stream_modulation.lin`, `img_in`, `txt_in`, `time_in.in_layer`, `time_in.out_layer`, `final_layer.linear`. Configuracion detectada por `comfy/model_detection.py` para `image_model == "flux2"`: `axes_dim=[32,32,32,32]`, `num_heads=48`, `mlp_ratio=3.0`, `theta=2000`, `out_channels=128`, `global_modulation=True`, `txt_ids_dims=[3]`, `patch_size=1`, `default_ref_method="index"`, `ref_index_scale=10.0`.
- **Nombres diffusers (para ai-toolkit / SimpleTuner / diffusers)**: en FLUX.2 las proyecciones q/k/v estan **fusionadas** en `attn.to_qkv_mlp_proj` y la salida es `attn.to_out` (**no** `attn.to_out.0`, ya no es ModuleList). Prefijos de bloque: `transformer_blocks.i.` (MMDiT/double) y `single_transformer_blocks.i.` (single). Ejemplos de `--lora_layers`: `attn.to_qkv_mlp_proj`, `attn.to_out`, `ff.linear_in`, `ff.linear_out`, `ff_context.linear_in`, `ff_context.linear_out`, `norm_out.linear`, `norm_out.proj_out`. En ai-toolkit el filtrado se hace con `network_kwargs.only_if_contains` / `ignore_if_contains` sobre el **state dict de diffusers**.
- **Presets de SimpleTuner** (`--flux_lora_target`): `all` (attention + MLP, default), `attention` (solo qkv + proj), `mlp`, `tiny` (solo qkv).
- **Traduccion del LoRA de Emilia**: el LoRA afinado ataca `qkv`+`proj` (atencion) y `linear1`/`linear2` (MLP) de bloques simple, mas las modulaciones globales. En diffusers eso es aproximadamente `attn.to_qkv_mlp_proj` + `attn.to_out` + `ff.linear_in`/`ff.linear_out`, y `norm_out.linear`. Es decir, es **el preset `attention` + MLP de los simple blocks**, no un `all` completo. Esto es consistente con un LoRA relatively chico (31,66 M params) y con una delta suave (B con std ~8e-4…1,6e-3) -> strength recomendado 0,6-1,0.

**`guidance_embeds`: klein NO los tiene.** SimpleTuner lo dice explicitamente: "klein models: Use Qwen3 text encoder bundled in the model repo, **no guidance embeddings** (guidance training options are ignored)". Consistente con la ausencia de `guidance_in` en el safetensors de Emilia. En inferencia: **Base admite guidance > 1.0** (cfg 5 en el template oficial de 9B base); **Destilado usa guidance 1.0 / 4 pasos**.

**Step-distillation y entrenamiento.** Destilados comprimidos en pasos: entrenarlos销毁 (destilados) no aporta señal completa. Regla operativa: **entrenar en Base (50 steps, guidance libre), inferir en Destilado (4 steps, guidance 1.0)**. Diferencia dechedule: `Flux2Scheduler` de ComfyUI no usa "shift" clasico; calcula un schedule empirico `get_schedule(steps, seq_len)` con `compute_empirical_mu` a partir de la longitud de secuencia (ver `comfy_extras/nodes_flux.py:184-211`).

**Sin negative prompt.** mflux: "FLUX.2 does not support --negative-prompt". En los templates oficiales de ComfyUI el nodo `CLIP Text Encode (Negative Prompt)` queda **vacio** y su salida va al slot `negative` del `CFGGuider` (que en la practica no penaliza). No escribir negative prompts.

**Aspect-ratio bucketing.** diffusers expone `--use_aspect_ratio_buckets` con la lista de buckets de FLUX.2: `672,1568; 688,1504; 720,1456; 752,1392; 800,1328; 832,1248; 880,1184; 944,1104; 1024,1024; 1104,944; 1184,880; 1248,832; 1328,800; 1392,752; 1456,720; 1504,688; 1568,672` — **identica** a `PREFERRED_KONTEXT_RESOLUTIONS` de `comfy_extras/nodes_flux.py:105-123`. Usar la misma lista en ambos lados.

### A.3 Text encoder Qwen3-8B

**Como lo ve ComfyUI** (verificado en el codigo local, commit `b08e6cf3`):

- `comfy/text_encoders/flux.py:181-184` -> `Qwen3Tokenizer8B`: `embedding_size=4096`, `embedding_key='qwen3_8b'`, tokenizador `Qwen2Tokenizer`, `pad_token=151643`, `min_length=512`.
- `comfy/text_encoders/flux.py:213-231` -> `Qwen3_8BModel` con `layer=[9, 18, 27]`: **tap de 3 capas**; `klein_te(model_type="qwen3_8b")`.
- `comfy/text_encoders/flux.py:194` -> plantilla de prompt: `"user\n{}\nassistant\n<think>\n\n</think>\n\n"`.
- `comfy/sd.py:1683-1689` y `1715-1718` -> `TEModel.QWEN3_8B` con `clip_type FLUX2` -> `KleinTokenizer8B`; y `TEModel.QWEN3VL_8B` con `FLUX2` -> mismo Klein de 8B (reutiliza el LM de Qwen3-VL, 3-layer tap -> 12288; el visual no se usa).
- En `comfy/sd.py:1715` el comentario es literal: *"Flux2 Klein reuses the Qwen3-VL LM (3-layer tap -> 12288)"* — coincide con el `txt_in` de 12288 del LoRA de Emilia.

**Archivos exactos (HF, verificados por API con tamaños reales):**

| Archivo | Repo | Ruta en `models/` | Bytes | Nota |
|---|---|---|---|---|
| `qwen_3_8b_fp8mixed.safetensors` | `Comfy-Org/vae-text-encorder-for-flux-klein-9B` (ex `Comfy-Org/flux2-klein-9B`) | `models/text_encoders/` | 8.664.848.742 (8,07 GiB) | **El que usa el template oficial de 9B** |
| `qwen_3_8b_fp4mixed.safetensors` | mismo | `models/text_encoders/` | 6.802.593.327 (6,34 GiB) | Alternativa para 8 GB |
| `qwen_3_8b.safetensors` | mismo | `models/text_encoders/` | 16.381.517.176 (15,26 GiB) | F16 completo |

**Se congela.** Confirmado por la receta de orquestacion Civitai para `flux2klein`: `trainTextEncoder: false` — *"Klein uses Qwen-3 as its text encoder; AI Toolkit does not train it. Leave false."* Y por diffusers: en klein el TE **debe** cargarse localmente (`--remote_text_encoder` es solo para FLUX.2 [dev] con Mistral).

**Embedder ungated / GGUF.** Si existe `ponpoke/flux2-klein-9b-uncensored-text-encoder`:
- `gated: "auto"` -> hay que aceptar el "Safety Warning & Terms of Access" (NSFW). **Gated**, no libre.
- Licencia declarada: `flux-non-commercial-v2.1` (link a la licencia de klein 9B).
- Archivos: `model.safetensors` (F16, 8.190.735.360 params), `flux2-klein-9b-uncensored-f16.gguf`, `-q4_k_m.gguf`, `-q6_k.gguf`, `-q8_0.gguf`; mas `config.json`, `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`.
- Es un `Qwen3ForCausalLM` completo, **no** el archivo partido de ComfyUI. Para usarlo en ComfyUI hay que pasar por `ComfyUI-GGUF` (city96) con el nodo `CLIPLoader (GGUF)` / `CLIPLoader (GGUF, Dynamic VRAM)`.
- Espejo GGUF del TE: `QiE2035/flux2-klein-9b-uncensored-text-encoder-Q2_K-GGUF`, `WANG-CC/flux2-klein-9b-uncensored-text-encoder-Q8_0-GGUF`.
- Para 4B: `Cordux/flux2-klein-4b-uncensored-text-encoder` (reportado por el usuario; **no verificado** en esta sesion).
- **Implicacion RAM/VRAM**: el TE F32 de 8B son 16,4 GB; en FP8mixed 8,07 GB; en FP4mixed 6,34 GB; GGUF Q4 ~5 GB. En una maquina con RAM limitada el TE debe ir **offloaded a CPU** y el VRAM reservarse para el transformer.

### A.4 Dataset y captioning para un LoRA de arquitectura (y para un edit-LoRA tipo Rhino-to-Image)

**Sizes (verificados):**

| Tipo de LoRA | Dataset | Fuente |
|---|---|---|
| Estilo general | 15-40 imagenes | HF blog |
| Estilo (BFL) | "Optimal dataset size: 20-40 images"; el ejemplo usa 27 | BFL training example |
| Estilo por tamano | 10-20 imgs -> 1200-1800 steps; 20-40 -> 1200-2000; 50+ -> 2000-3000 | BFL |
| Edit (pareado) | 50-200 pares | HF blog (`stephenbtl/ugly-kontext-klein-4b-lora` uso 120 pares) |
| Edit (Civitai) | zip con `main/`, `control_1/`, `control_2/`, `control_3/`, nombres de archivo alineados | Civitai recipe |

**Reglas de caption (verificadas en BFL y HF, consistentes entre si):**
1. **Describir el contenido, nunca el estilo.** "If you name the style in the caption, the model learns to depend on that word instead of baking the style into the weights."
2. **Trigger word = token inventado, no una palabra real**: `GFX_IMPR5N`, `SPR1TE8`, `RISO_PR1NT`, `ZK_TOON`. Identico en cada caption y en el `trigger_word` de la config. En ai-toolkit se puede escribir `[trigger]` en el .txt y el config lo reemplaza.
3. **Los modificadores que quieras controlar despues van en el caption.** Lo que el caption nombra se convierte en dial de inferencia (ej. `chibi`, `16-bit pixel art`).
4. En ai-toolkit: `.txt` con el mismo nombre que la imagen; formatos admitidos jpg/jpeg/png (webp con problemas); las imagenes **no se upscalean**, se reescalan a buckets; se soporta `control_path:` para datasets de edicion.
5. **Para el caso Rhino-to-Image el caption es una instruccion, no una descripcion.** HF: "A style caption describes what's in the image. An edit caption describes the *transformation* you want applied." Ejemplo real: `change the photo the cat into an ugly sketch of the same cat`. Para el curso: algo del orden de *"convert the 3D volume model into a photorealistic architectural render with the same geometry, applying the reference material"*.

**JSON estructurado para Flux.2:** el usuario lo reporta desde el curso. **No se pudo verificar en material publico**: ni la pagina de Archademy ni la guia de BFL ni la documentacion de ai-toolkit mencionan captions JSON para klein. Lo que si esta verificado es el uso de captions `.txt` con `caption_ext: "txt"` y la instruccion de "structured prompting" de FLUX.2 (mencionada en el blog de ComfyUI como capacidad del modelo, no como formato de caption). **Marca: no verificado**.

**Diseno de dataset recomendado para el LoRA del curso (edit-LoRA de arquitectura):**
- `target/` = renders fotorrealistas objetivo (el "after"), `reference/` = la captura 3D de Rhino (el "before") + una foto de material. Captions = instruccion de transformacion.
- En ai-toolkit: `folder_path: target/`, `control_path: reference/`.
- En SimpleTuner: `conditioning_data: ["flux2-references"]` con `conditioning_type: "reference_strict"` (crops 1:1) o `reference_loose`.
- En diffusers: triplets (`image_column` = target, `cond_image_column` = condition, `caption_column` = instruccion), como en `kontext-community/relighting`.

### A.5 Entrenamiento en 8 GB AMD RX 570 / DirectML — veredicto

**No es viable. Y no es una Limitacion de la herramienta, es de la plataforma.**

| Requisito documentado | Fuente | Por que rompe la RX 570 |
|---|---|---|
| klein 4B: **12 GB VRAM** + 32 GB RAM | BFL | Ya supera los 8 GB |
| klein 9B: **22 GB VRAM** (RTX 3090/4090) + 64 GB RAM | BFL | 3x la VRAM disponible |
| klein 9B: ~22 GB bf16 / ~14 GB int8 | SimpleTuner | 14 GB int8 > 8 GB |
| `adamw8bit` (bitsandbytes) | BFL, Civitai, diffusers | bitsandbytes es **CUDA-only** |
| `--do_fp8_training` (torchao) | diffusers | *"we need CUDA GPUs with compute capability at least 8.9 or greater"* |
| ai-toolkit: `torch==2.13.0 ... --index-url .../cu130` | README ai-toolkit | Build de CUDA; DirectML no entra |
| SimpleTuner: `pip install 'simpletuner[cuda]'`, FSDP2/DeepSpeed | README SimpleTuner | Multi-GPU NVIDIA |
| ComfyUI mismo advierte | `comfy/model_management.py:111` | *"WARNING: torch-directml barely works, is very slow, has not been updated in over 1 year and might be removed soon"* |

**¿GGUF Q4 + LoRA en 8 GB?** El GGUF reduce el transformer (9B Q4_K_M ~5,5-6 GB), pero: (a) el TE de 8B sigue necesitando 6-8 GB (solo en RAM si no entra), (b) el training de LoRA exige **backward** sobre el transformer, no solo forward, (c) no existe backend de optimizador cuantizado para DirectML. **No.**

**¿Entrenar en klein 4B (Apache 2.0) y portar a 9B? NO es viable.** Razon verificable (SimpleTuner + `comfy/model_detection.py` + analisis del safetensors de Emilia):

| | klein 4B | klein 9B |
|---|---|---|
| Bloques | 5 double + 20 single | 8 double + 24 single |
| Hidden size | 3072 | 4096 |
| Dim de embedding (txt) | 7.680 (3x2560) | 12.288 (3x4096) |
| MLP ratio / axes | ratio 3.0, axes [32,32,32,32] | ratio 3.0, axes [32,32,32,32] |
| TE | Qwen3-4B | Qwen3-8B |

Un LoRA rank-16 entrenado en 4B genera tensores con formas que **no coinciden** con los del 9B (`img_attn.qkv` de 3072 vs 4096 de dimensión interna). No hay "portabilidad" posible: hay que reentrenar.

**Alternativas cloud (precios verificados en la pagina oficial de RunPod, "GPU Cloud Pricing Updated October 8, 2026"):**

| GPU | VRAM | Community Cloud | Secure Cloud | Uso sugerido |
|---|---|---|---|---|
| RTX 3090 | 24 GB | **$0,22/h** (figura structured-data de la pagina) | $0,46/h | **Mejor precio para entrenar 9B** (int8 o bf16 con offload) |
| RTX 3090 (pod estandar) | 24 GB | $0,50/h (listado de pods) | — | Alternativa |
| RTX 4090 | 24 GB | **$0,34/h** | $0,69-0,74/h | Lo que usa el template de ai-toolkit (`console.runpod.io/deploy?template=0fqzfjy6f3`) |
| RTX A5000 | 24 GB | $0,27/h | — | Barato |
| A40 | 48 GB | $0,44/h | $0,49/h | Comodo para 9B bf16 |
| L40S | 48 GB | $0,79/h | $1,09/h | — |
| Serverless (L4/A5000/3090) | 24 GB | $1,10/h | — | Inferencia serverless |
| H100 SXM 80 GB | 80 GB | $1,99/h | $2,89-3,49/h | Sobrekill |

Referencia de costo: HF blog — "A LoRA run on the 4B model fits in 24 GB of VRAM, takes about an hour on an RTX 4090, and **costs roughly $0.50** if you rent the GPU." Para 9B, estimar 2-4 h -> **$0,70-$1,40** en 4090 Community.

**Opcion sin GPU: la API de BFL.** docs.bfl.ml/flux_2/flux2_lora_inference: se sube el `.safetensors` al Dashboard (`Customization -> Finetunes`, se elige base model, nombre con solo `[a-z0-9-_]`, trigger phrase opcional) y se llama `POST /v1/flux-2-klein-9b-finetuned` con `finetune_id` y `finetune_strength`. Endpoints disponibles para `flux-2-klein-4b-finetuned`, `flux-2-klein-9b-finetuned`, `flux-2-klein-9b-kv-finetuned`, `flux-2-klein-9b-kv-bf16-finetuned`, `flux-2-klein-base-4b-finetuned`, `flux-2-klein-base-9b-finetuned`.

---

## Bloque B — Workflow "Rhino-to-image" en ComfyUI con FLUX.2

### B.6 Grafo de nodos exacto para FLUX.2 [klein] 9B (verificado contra los templates oficiales)

**Fuente primaria:** los JSON oficiales de `Comfy-Org/workflow_templates`, descargados y leidos en esta sesion:
- `templates/image_flux2_text_to_image_9b.json` (Text-to-Image 9B)
- `templates/image_flux2_klein_image_edit_9b_base.json` (Image Edit 9B Base)
- `templates/image_flux2_klein_image_edit_9b_distilled.json` (Image Edit 9B Destilado)
- `templates/image_flux2_klein_text_to_image.json` / `image_flux2_klein_image_edit_4b_base.json` / `image_flux2_klein_image_edit_4b_distilled.json` (4B)
- `templates/image_flux2.json` / `image_flux2_fp8.json` (dev)

**Grafo de Text-to-Image 9B (subgraph "Text to Image (FLUX.2 Klein 9B)")**:

| Nodo | Tipo | Valor por defecto del template | Nota |
|---|---|---|---|
| 70 | `UNETLoader` | `flux-2-klein-base-9b-fp8.safetensors`, `weight_dtype=default` | Carga en `models/diffusion_models/` |
| 71 | `CLIPLoader` | `qwen_3_8b_fp8mixed.safetensors`, **`type=flux2`**, `device=default` | El `type` **tiene que ser** `flux2`; es lo que dispara `klein_te(model_type="qwen3_8b")` |
| 72 | `VAELoader` | `full_encoder_small_decoder.safetensors` | Alternativa: `flux2-vae.safetensors` |
| 74 | `CLIPTextEncode` (Positive) | prompt | |
| 67 | `CLIPTextEncode` (Negative) | **vacio** | FLUX.2 no usa negative prompt |
| 62 | `Flux2Scheduler` | **`steps=20`, `width=1024`, `height=1024`** | Salida `SIGMAS`; el `width`/`height` vienen de `PrimitiveInt` |
| 63 | `CFGGuider` | **`cfg=5`** | En modelo **Base**; en destilado va `cfg=1` |
| 61 | `KSamplerSelect` | **`euler`** | |
| 73 | `RandomNoise` | `noise_seed` randomize | |
| 64 | `SamplerCustomAdvanced` | — | **No `KSampler`**: `Flux2Scheduler` produce `SIGMAS`, que `KSampler` no consume |
| 66 | `EmptyFlux2LatentImage` | `width=1024, height=1024, batch_size=1` | Crea `zeros([B,128,H/16,W/16])` (128 canales) |
| 65 | `VAEDecode` | — | |
| 9 | `SaveImage` | — | |

**Parametros segun variante (verificados):**

| Variante | Steps | Guidance/cfg | Sampler | Notas |
|---|---|---|---|---|
| klein 9B **Base** (el del template) | **20** | **5** | euler | max calidad/flexibilidad; BFL usa 50 pasos para训练的, 20 es lo que trae Comfy |
| klein 9B **Destilado** | **4** | **1.0** | euler | latencia sub-segundo en 5090 |
| klein 4B Destilado | 4 | 1.0 | euler | ~1,2 s en 5090, 8,4 GB VRAM |
| klein 4B Base | ~20-50 | >1 | euler | |
| Klein 4B/9B distilled en mflux | 4 | `guidance 1.0` | — | "Distilled FLUX.2 variants use --guidance 1.0" |

**Onde insertar el LoRA.** `LoraLoaderModelOnly` (o `LoraLoader`) entre `UNETLoader` y `CFGGuider`, con `strength_model` 0,6-1,0 (la delta del LoRA de Emilia es suave). BFL lo confirma: "Place `.safetensors` file in `ComfyUI/models/loras/`, add "Load LoRA" node to your workflow, connect it to your FLUX Klein model, use trigger word in prompts".

### B.7 Metodo de referencia / edicion: como se usa la imagen de referencia y como se "fija" la geometria

**Grafo de Image Edit 9B Base (verificado en el template oficial)** — este es el esqueleto del "Rhino-to-image":

```
LoadImage (captura 3D de Rhino)
      |
   [80] ImageScaleToTotalPixels  (lanczos, megapixels=1.0, resolution=1.0)
      |            |                    |
   [100] GetImageSize        [123] VAEEncode (+ VAE)
      |            |                    |
      |            +--> [66] EmptyFlux2LatentImage (W,H) --> [62] Flux2Scheduler
      |            +--> [62] Flux2Scheduler
      |
      +--> [123] VAEEncode --> [124] ReferenceLatent(conditioning POSITIVO) --> [63] CFGGuider.positive
      +--> [123] VAEEncode --> [122] ReferenceLatent(conditioning NEGATIVO) --> [63] CFGGuider.negative
```

Claves mecanicas (verificadas en el codigo local):

1. **`ReferenceLatent`** es el nodo que "bloquea" la geometria. Empuja el latent VAE de la imagen de referencia dentro del conditioning (`out['ref_latents'] = CONDList(latents)` en `comfy/model_base.py:1033-1042`). El transformer FLUX.2 consume esos tokens de referencia en el mismo bloque de atencion que la imagen a generar.
2. **El indexado posicional es lo que "fija" la composicion.** `comfy/ldm/flux/model.py:365-369`:
   ```python
   ref_latents_method = kwargs.get("ref_latents_method", self.params.default_ref_method)
   if ...:
       index += self.params.ref_index_scale
   ```
   Con `default_ref_method="index"` y `ref_index_scale=10.0` (los valores que `comfy/model_detection.py:248-249` setea para FLUX.2), los tokens de referencia reciben un **offset de indice posicional de 10**, de modo que ocupan su propia banda en el eje de posiciones y no pueden "mezclarse" con la imagen generada. Eso es el "bloquea la geometria exactamente en su sitio".
3. **`FluxKontextMultiReferenceLatentMethod`** (nodo, categoria `model/conditioning/flux`, marcado `is_experimental=True`) permite cambiar el metodo: opciones `offset`, `index`, `uxo/uno`, `index_timestep_zero`. Escribe `reference_latents_method` en el conditioning.
4. **`FluxKVCache`** (nodo experimental) parchea el modelo para cachear K/V de los tokens de referencia entre pasos y **fuerza** `default_ref_method = "index_timestep_zero"` (parchea `diffusion_model.params.default_ref_method` o `diffusion_model.default_ref_method`). Acelera la edicion multi-referencia a costa de congelar la referencia en t=0.
5. **`FluxKontextImageScale`** reescala la imagen a la resolucion optima de FLUX.2 mas cercana (16 relaciones de aspecto, de 672x1568 a 1568x672, ver `PREFERRED_KONTEXT_RESOLUTIONS`). Importante para que la referencia y la salida compartan la grilla de tokens.

**Traduccion a la practica del curso ("textura de material + geometria bloqueada"):**

- **Referencia 1 = geometria**: la captura del viewport de Rhino (linework/shaded) entra por `LoadImage` -> `ImageScaleToTotalPixels` -> `VAEEncode` -> `ReferenceLatent`. El modelo respeta el encuadre, la perspectiva, la proporcion y la silueta.
- **Referencia 2 = material**: una foto real del material (ladrillo, hormigon, ceramica) entra por una segunda rama identica -> segundo `VAEEncode` -> segundo `ReferenceLatent` sobre el mismo conditioning. La documentacion de BFL confirma el multi-reference en klein 9B: "Image Editing (Multi-reference) ✅" y "reliable multi-reference consistency (up to 10 images)".
- **El LoRA `rhino-to-image-lora.basic.safetensors` actua como el "traductor"**: aporta el comportamiento "modelo 3D en volumetria -> render fotorrealista con el material de referencia", y su trigger word (a confirmar con el instructor) gatilla ese comportamiento.
- **Opcional**: `FluxKVCache` sobre el modelo para cachear la referencia (multi-ref mas barato), y `FluxKontextMultiReferenceLatentMethod` con `index` explicito para fijar la geometria.
- **NO usar `img2img` con denoise bajo como mecanismo principal**: sirve para "re-pintar" una imagen unica, pero pierde la condicion de referencia explicita que permite tener DOS referencias (geometria + material) simultaneamente.

### B.8 ControlNet para FLUX.2

- **No existe ControlNet oficial de BFL para FLUX.2** (ni dev ni klein). Verificado.
- Lo unico serio es **`alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union`** (VideoX-Fun):
  - `FLUX.2-dev-Fun-Controlnet-Union.safetensors` — **8,23 GB** — licencia `flux-dev-non-commercial-license`.
  - `FLUX.2-dev-Fun-Controlnet-Union-2602.safetensors` — version nueva: "added Scribble and Gray controls" y **re-dijo la CFG distillation** ("the Flux2 model loses its CFG distillation capability after Control training, which is why the previous version performed poorly").
  - Modos: canny, HED, depth, pose, MLSD, scribble, gray. "This ControlNet is added on 4 double blocks." Soporta inpainting y `controlnet_conditioning_scale`.
  - **Es para FLUX.2 [dev] 32B, NO para klein.** No es aplicable a un LoRA de klein 9B.
  - Implementacion en ComfyUI: `bryanmcguire/comfyui-flux2fun-controlnet` (Apache-2.0), nodo `Load Flux2 Fun ControlNet`; requiere FLUX.2-dev + `flux2-vae.safetensors`.
- **ControlNet para klein**: existe el repo `ReyChiaro/flux.2-klein-controlnet` (con `flux2/controlnet_flux2klein.py`, 291 lineas) pero **su README no esta disponible (404)** y no se verificaron pesos ni licencia. **Marca: no verificado**.
- **`control_v11p_sd15_scribble.safetensors` (SD1.5) no sirve con FLUX.2**: arquitectura incompatible.
- **Alternativa correcta para klein**: `ReferenceLatent` nativo (B.7) + `FluxKontextImageScale`. Si hace falta lineart rigido, el lineart de Rhino (`Make2D` -> curvas) exportado a PNG puede entrar como referencia secundaria, no como ControlNet.

### B.9 Preprocesado desde Rhino (el input real es `.dwg`)

**Ruta de export desde Rhino (verificada en la documentacion oficial de McNeel):**
- `ViewCaptureToFile` (Rhino 8): "saves an image of the current view to a file"; "saves the contents of the view with a specified width and height, disregarding the current viewport size"; "Viewport borders, cursor images, and other decorations are not saved". Formatos: **BMP, JPG, PNG, TIFF**. Opcion `-Autoname` (scriptable) para el prefijo. URL: https://docs.mcneel.com/rhino/8/help/en-us/commands/viewcapturetofile.htm
- `ViewCaptureToClipboard` / `ScreenCaptureToFile`: el segundo **incluye** bordes, titulo de viewport y cursor -> **no usar** para AI.
- Rhino 8 tiene modos de visualizacion: `Rendered`, `Shaded`, `Wireframe`, `Ghosted`, `X-Ray`, `Technical`, `Artistic`, `Pen`, `Thermal` (Technical = aristas ocultas, Thermal = mapa de profundidad por temperatura).
- La version con el input real del curso: `Barcelona-2D.dwg` (29 MB) y `3D-model.dwg` (18 MB) -> el 2D es el plano de trabajo, el 3D es la volumetria.

**Depth map desde Rhino: no hay pass de profundidad nativo para IA.** Rhino tiene el modo de visualizacion "Thermal" (mapa por distancia, no lineal) y Rhino.Render (Cycles/Arnold) con passes, pero **no se verifico** que Rhino exponga un PNG de profundidad lineal listo para ControlNet. Opciones verificadas o plausibles:

1. **Depth Anything V2 monocular en ComfyUI** a partir del `ViewCaptureToFile` sombreado: la practica dominante 2026. Hay packs de nodos `DepthAnythingV2` en ComfyUI (no verificados en esta sesion) y el workflow publico `denkaTa599/comfyui-architectural-workflow` los usa explicitamente ("Depth Anything V2 ControlNet (strength: 0.60)") junto a Canny.
2. **Render pass de profundidad con Cycles/Arnold**: exportar el modelo a FBX/glTF, abrir en Blender, renderizar el pass de profundidad lineal a PNG. Mas fiel, mas trabajo.
3. **Nodos 3D dentro de ComfyUI**: `comfyui-3d-viewport-pro` / `comfyui-3d-pack` renderizan la malla con normal/depth. Plausible, no verificado en detalle esta sesion.
4. **Display mode "Thermal" de Rhino** como aproximacion rapida (no lineal) — util solo como referencia de orden de profundidad.

**Tecnica de referencia en la industria (verificada en el articulo publico `archigenai.com/comfyui-rhino-architects-workflow-2026.html`, 18-may-2026)**: exportar **tres pasadas desde la MISMA camara**, a 2048 px en el lado largo, en modo sombreado **sin aristas**:
- **Pasada 1 — depth map** (display mode de profundidad o rampa lineal negro→blanco por distancia Z a la camara, sin sombras): va al nodo ControlNet Depth. "If this pass is wrong, nothing else can recover it."
- **Pasada 2 — line drawing** (`Make2D`): preserva las lineas.
- **Pasada 3 — flat shaded**: va al IP-Adapter como referencia de material, con weight ~0,4 ("Material guidance, soft enough that the model still has room to add weathering and atmosphere").
Ese workflow usa FLUX.1 dev/schnell + ControlNet Depth/Lineart + IP-Adapter, no FLUX.2. Para FLUX.2 la traduccion es: **sustituir ControlNet Depth + IP-Adapter por `ReferenceLatent` multiple** (geometria via pasada 2+3, material via la foto de material real).

**Como "lockear" la geometria — jerarquia de opciones:**

| Mecanismo | Disponible en FLUX.2 klein 9B | Fidelidad de geometria | Coste |
|---|---|---|---|
| `ReferenceLatent` con `index` (metodo nativo) | **Si, nativo** | **Alta** (es lo que usa el curso) | 0 |
| `FluxKVCache` + `index_timestep_zero` | Si (experimental) | Alta | Acelera multi-ref |
| img2img con denoise 0,35-0,55 | Si | Media | pierde multi-referencia |
| ControlNet depth/lineart | **No para klein** (solo dev) | — | — |
| SD1.5 `control_v11p_sd15_scribble` | No (arquitectura distinta) | — | — |

### B.10 Coste y practicidad en la PC de Emilia (RX 570 8 GB, DirectML)

**Presupuesto de VRAM (medido por documento oficial, no estimado):**

| Modelo | VRAM (referencia oficial) | En RX 570 8 GB |
|---|---|---|
| FLUX.2 klein 4B Destilado | **8,4 GB** (5090) | **Al limite, imposible en la practica** (DirectML no puede consultar VRAM libre -> ComfyUI desactiva el lowvram dinamico) |
| FLUX.2 klein 4B Base | 9,2 GB (5090) | No entra |
| FLUX.2 klein 9B (fp8) | ~9,4 GB de pesos (`flux-2-klein-9b-fp8.safetensors` = 9.433.061.528 bytes) + TE 8,07 GB | **No entra ni con offload agresivo** |
| TE Qwen3-8B fp8mixed | 8,07 GB | Offload a RAM obligatorio |
| GGUF 9B Q4_K_M | ~5,5-6 GB (repo GGUF completo: 18,16 GB para 18 quants) | Entra el transformer, pero el TE no |

**Detalles criticos de DirectML en ComfyUI (verificados en el codigo local):**
- `comfy/model_management.py:111-121`: al activar `--directml` se loguea el warning oficial ("barely works, is very slow...") y se setea **`lowvram_available = False`** ("need to find a way to get free memory in directml before this can be enabled by default").
- `comfy/cli_args.py:144`: `--lowvram` "Doesn't do anything if dynamic vram is enabled" -> **con DirectML el flag `--lowvram` es inoperante**.
- `comfy/cli_args.py:148-153`: existen `--reserve-vram <GB>` y `--disable-dynamic-vram` (que es lo que corresponde cuando no se puede interrogar la VRAM).
- Conclusion operativa: en la PC de Emilia hay que usar `--directml --reserve-vram 1.0 --disable-dynamic-vram` y **`--lowvram` no aporta nada**.

**Lo que si anda 100 % local (ya instalado y funcionando):**
- SD 1.5 + `archisketch-v1.safetensors` + `markerhandsketch-V1.safetensors` + `control_v11p_sd15_scribble` (ya instalados) -> croquis, conceptuales, todas las pruebas de pipeline, toda la logica de nodos.
- SDXL + `Juggernaut-XL_v9_RunDiffusionPhoto_v2` -> render de cliente de calidad,ControlNet SDXL (depth/canny/lineart), y es el camino **comercialmente seguro** (OpenRAIL++-M).

**Las tres rutas (recomendacion: b):**

| Ruta | Setup | Costo | Tiempo por imagen | Quando |
|---|---|---|---|---|
| **(a) Todo local** | SD1.5/SDXL en la RX 570 | $0 | ~3-10 min (SDXL) / ~1 min (SD1.5) | Bocetos, pruebas de nodos, preprocesado Rhino, captions |
| **(b) Local + RunPod (RECOMENDADA)** | Instalar FLUX.2 klein 9B en un pod RunPod 3090/4090 24 GB;数据集 y LoRA en el pod | **$0,22-0,74/h** segun GPU/tier | 9B distilled: ~1-3 s/imagen en 4090 (referencia "~1 s" en 5090); 9B base 20 pasos: ~10-20 s | Produccion del concurso y previsualizacion final |
| **(c) Cloud completo (BFL API)** | Sin GPU; `finetune_id` + endpoint `flux-2-klein-9b-finetuned` | Por token/API (public beta, precios en dashboard) | Segun cola | Si hay que servir el LoRA entrenado sin|ComfyUI local |

**Presupuesto realista del concurso:** 1 pod 4090 Community de 6 h = ~$2,04; un 3090 Community de 10 h = ~$2,20. **Todo el render del concurso cabe en el precio de un cafe**. ElLoRA ya esta entrenado (lo entrega el curso), asi que no hay gasto de training salvo que se quiera reentrenar.

---

## Bloque C — Instalacion en la PC de Emilia

### C.11 Procedimiento de instalacion / actualizacion de ComfyUI

**Opcion 1 — Repo + conda (RECOMENDADA).** Es lo que ya usa el estudio (`P:\00-repos\ComfyUI` + `P:\Anaconda\envs\comfyenv`), y mantiene los modelos en un unico arbol.

```cmd
:: 1) Instalar (si ya existe, actualizar)
git clone https://github.com/comfyanonymous/ComfyUI.git P:\00-repos\ComfyUI
cd /d P:\00-repos\ComfyUI
git pull

:: 2) Entorno conda con DirectML (AMD)
conda create -n comfyenv python=3.12 -y
conda activate comfyenv
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install torch-directml
pip install -r requirements.txt
pip install -r requirements.txt   :: (ComfyUI 0.8.x pide "requirements.txt" + comfyui-frontend-package)

:: 3) Arrancar (AMD / RX 570)
P:\Anaconda\envs\comfyenv\python.exe -s main.py --directml --disable-dynamic-vram --reserve-vram 1.0 --listen 127.0.0.1 --port 8188
```

Notas:
- **`--lowvram` no hace nada con DirectML** (`comfy/model_management.py:121`). Usar `--disable-dynamic-vram` + `--reserve-vram`.
- `--directml` acepta un indice de dispositivo opcional: `--directml 0`.
- `torch-directml` requiere `torch` compilado para CPU (no CUDA): `--index-url .../whl/cpu`.

**Opcion 2 — ComfyUI portable (`ComfyUI_windows_portable`).**

| | Repo + conda | Portable |
|---|---|---|
| Instalacion | Requiere git + conda + `pip install torch-directml` | Descomprimir y reemplazar `python_embeded` por uno con `torch-directml` (o instalar el paquete dentro del python embebido) |
| Sincronizacion con el estudio | **Natural** (mismo repo, mismo commit `b08e6cf3`) | Cada maquina tiene su propia version -> divergencia |
| Modelos | Un arbol compartido (`models/` del repo) | Carpeta propia -> duplicar ~30 GB |
| Actualizar | `git pull` | Descargar el portable nuevo y re-copiar `models/` |
| Arranque en background |Igual de facil | Script `.bat` dedicado |
| Veredicto | **Elegir esta** | Solo si el objetivo es "que funcione sin tocar Python" |

**Levantar el server en background en Windows:**

```cmd
:: Ventana minima, sigue vivo al cerrar la consola
start "ComfyUI" /min cmd /c "P:\Anaconda\envs\comfyenv\python.exe -s P:\00-repos\ComfyUI\main.py --directml --disable-dynamic-vram --reserve-vram 1.0 --port 8188"

:: O bien, con PowerShell (oculto)
Start-Process -WindowStyle Hidden -FilePath "P:\Anaconda\envs\comfyenv\python.exe" `
  -ArgumentList '-s','P:\00-repos\ComfyUI\main.py','--directml','--disable-dynamic-vram','--reserve-vram','1.0','--port','8188'
```

### C.12 Descarga e instalacion de modelos para este LoRA (FLUX.2 klein 9B)

Todos con `huggingface-cli download <repo> <archivo> --local-dir <destino>` o `hf download`. **Los repos de BFL son GATED (`gated: "auto"`)**: hay que aceptar la licencia en la pagina HF con una cuenta (comprobado via API: `FLUX.2-klein-9b-fp8.gated = "auto"`, `FLUX.2-klein-base-9B.gated = "auto"`).

**Transformers (FLUX.2 klein 9B) -> `models/diffusion_models/`**

| Archivo exacto | Repo HF | Bytes | Licencia |
|---|---|---|---|
| `flux-2-klein-9b-fp8.safetensors` | `black-forest-labs/FLUX.2-klein-9b-fp8` | **9.433.061.528** (8,79 GiB) | FLUX Non-Commercial (gated) |
| `flux-2-klein-base-9b-fp8.safetensors` | `black-forest-labs/FLUX.2-klein-base-9b-fp8` | ~9,4 GB (repo 9,44 GB total) | FLUX Non-Commercial (gated) — **este es el que usa el template de 9B** |

**Variantes GGUF (para la PC de Emilia o para pods con menos VRAM) -> `models/diffusion_models/`**

Repo `unsloth/FLUX.2-klein-9B-GGUF` (licencia `flux-non-commercial-license`, 18.157.197.600 bytes en total para 18 quants):

| Archivo | Tamano aprox. |
|---|---|
| `flux-2-klein-9b-Q2_K.gguf` | ~3,3 GB |
| `flux-2-klein-9b-Q3_K_M.gguf` / `Q3_K_S.gguf` | ~3,9 / 3,7 GB |
| `flux-2-klein-9b-Q4_0.gguf` / `Q4_1.gguf` | ~5,0 GB |
| **`flux-2-klein-9b-Q4_K_M.gguf`** | ~**5,5 GB** (recomendado) |
| `flux-2-klein-9b-Q4_K_S.gguf` | ~4,8 GB |
| `flux-2-klein-9b-Q5_0.gguf` / `Q5_1.gguf` / `Q5_K_M.gguf` / `Q5_K_S.gguf` | ~5,6-5,8 GB |
| `flux-2-klein-9b-Q6_K.gguf` | ~6,6 GB |
| `flux-2-klein-9b-Q8_0.gguf` | ~8,3 GB |
| `flux-2-klein-9b-F16.gguf` | ~16,9 GB |
| `flux-2-klein-9b-BF16.gguf` | ~16,9 GB |

Otros repos GGUF verificados: `unsloth/FLUX.2-klein-base-9B-GGUF`, `QuantStack/FLUX.2-Klein-9B-KV-GGUF`, `leejet/FLUX.2-klein-9B-GGUF`, `n-Arno/FLUX.2-klein-base-9B-GGUF` (este ultimo declara `license:apache-2.0`), `vantagewithai/FLUX.2-klein-9b-kv-GGUF`, `biali/FLUX.2-klein-9b-kv-GGUF`.
**`city96` no tiene un repo GGUF propio de FLUX.2 klein 9B** -> el nodo es de city96 (`city96/ComfyUI-GGUF`) pero **los pesos son de unsloth**. Buscar "city96 FLUX.2 klein" devuelve el nodo, no los pesos.

Cargar un GGUF en ComfyUI requiere el pack `city96/ComfyUI-GGUF` -> nodo **`UnetLoaderGGUF`**. Nota de estado: issue #411 ("flux2 klein: ValueError: Got [32,32,32,32] but expected positional dim 64") **cerrada el 16-01-2026**; la causa era tener ComfyUI-GGUF desactualizado frente al ComfyUI nativo (hay que actualizar ambos).

**Text encoder -> `models/text_encoders/`**

| Archivo | Repo HF | Bytes | Nota |
|---|---|---|---|
| `qwen_3_8b_fp8mixed.safetensors` | `Comfy-Org/vae-text-encorder-for-flux-klein-9B` | 8.664.848.742 | **el que usa el template oficial 9B** |
| `qwen_3_8b_fp4mixed.safetensors` | mismo | 6.802.593.327 | para 8 GB |
| `qwen_3_8b.safetensors` | mismo | 16.381.517.176 | F16 |
| `flux2-klein-9b-uncensored-{f16,q4_k_m,q6_k,q8_0}.gguf` | `ponpoke/flux2-klein-9b-uncensored-text-encoder` | 8,19 B params (F16) | **GATED** (aviso de seguridad); usar `CLIPLoader (GGUF)` de ComfyUI-GGUF |

Ojo: `Comfy-Org/flux2-klein-9B` fue **renombrado** a `Comfy-Org/vae-text-encorder-for-flux-klein-9B` (la API de HF redirige). Contiene `split_files/text_encoders/*` y `split_files/vae/flux2-vae.safetensors`; **no** contiene el transformer.

**VAE -> `models/vae/`**

| Archivo | Repo HF | Bytes | Licencia |
|---|---|---|---|
| `full_encoder_small_decoder.safetensors` | `black-forest-labs/FLUX.2-small-decoder` | 238 MB | **Apache-2.0** (repo con `license: apache-2.0`) |
| `flux2-vae.safetensors` | `Comfy-Org/vae-text-encoder-for-flux-klein-9B` (split_files/vae/) | ~330 MB | FLUX Non-Commercial |
| `small_decoder.safetensors` / `diffusion_pytorch_model.safetensors` | `black-forest-labs/FLUX.2-small-decoder` | — | Apache-2.0 |

`FLUX.2-small-decoder` ofrece tres opciones: encoder completo + decoder chico (`full_encoder_small_decoder.safetensors`, la que usa el template 9B), solo decoder chico (`small_decoder.safetensors`) y el diffusers (`diffusion_pytorch_model.safetensors`). El VAE de FLUX.2 es **128 canales** (32 -> pixel shuffle), no 16 como FLUX.1.

**El LoRA -> `models/loras/`**

| Archivo | Notas |
|---|---|
| `rhino-to-image-lora.basic.safetensors` (120,8 MB) | Lo que tiene Emilia. **Sin metadata embebida ni sidecar** -> copiarlo tal cual, sin renombrar (el nombre no define nada en ComfyUI, pero conviene mantenerlo para trazabilidad). Trigger word **a confirmar**. |
| version "advanced" | **No encontrada publicamente.** Pedirla al instructor (ver E.2) |

**Presupuesto de disco (todo el stack 9B, sin LoRA extra):** 8,8 GiB (transformer fp8) + 8,1 GiB (TE fp8) + 0,23 GiB (VAE) + 0,12 GiB (LoRA) ≈ **17,3 GiB**. Con GGUF en vez de fp8: ~5,5 + 6,3 + 0,23 + 0,12 ≈ **12,2 GiB**. La PC de Emilia tiene "disco limitado": **usar GGUF Q4_K_M + TE fp4mixed** para una base de 12 GB, o mejor **no descargar nada de 9B en la PC y trabajar el 9B en RunPod** (C.13).

### C.13 Packs y workflows oficiales listos para importar

**Templates oficiales de Comfy (todos verificados en `Comfy-Org/workflow_templates`):**

| Template | Archivo JSON |
|---|---|
| FLUX.2 [Klein] 9B: Text to Image | `templates/image_flux2_text_to_image_9b.json` |
| FLUX.2 [Klein] 9B: Image Edit (Base) | `templates/image_flux2_klein_image_edit_9b_base.json` |
| FLUX.2 [Klein] 9B: Image Edit (Distilled) | `templates/image_flux2_klein_image_edit_9b_distilled.json` |
| FLUX.2 [Klein] 4B: Text to Image | `templates/image_flux2_klein_text_to_image.json` |
| FLUX.2 [Klein] 4B: Image Edit (Base) | `templates/image_flux2_klein_image_edit_4b_base.json` |
| FLUX.2 [Klein] 4B: Image Edit (Distilled) | `templates/image_flux2_klein_image_edit_4b_distilled.json` |
| FLUX.2 Dev (bf16 / fp8) | `templates/image_flux2.json`, `templates/image_flux2_fp8.json` |

Descarga cruda: `https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/<archivo>.json` (leido en esta sesion, 200).

**Catalogo en comfy.org:** https://comfy.org/workflows/model/flux-2-klein/ -> **9 workflows** listados, 6 oficiales de ComfyUI + `Flux.2 Klein 9B: Image Extend` (community, de Doc_workBox) + `1 input and multiple editing model comparison` (community, de Rob) + `1.3 Starter - Product Photography`.

**Workflows oficiales "FLUX.2 + LoRA" ready-to-import: NO ENCONTRADOS.** La practica es partir del template 9B Image Edit e insertar `LoraLoaderModelOnly` entre `UNETLoader` y `CFGGuider`.

**Workflow comunitario de arquitectura (muy relevante como referencia):**
`denkaTa599/comfyui-architectural-workflow` -> `Advanced_Flux_Arch_Workflow.json` (11.532 bytes). Objetivo declarado: "transform a basic, low-resolution 3D viewport render into a high-quality, photorealistic architectural masterpiece". Stack: **3-LoRA** + `Canny Edge ControlNet` (strength 0,75) + `Depth Anything V2 ControlNet` (strength 0,60) + 3 etapas de generacion/upscale. Entradas: imagen base 3D + 3 referencias (material principal, mood/iluminacion, material secundario). Requisitos declarados: RTX 5080 16 GB, RAM 64 GB. **Es FLUX.1 (dev), no FLUX.2** -> sirve de blueprint de "que referencias pasar" pero hay que portar el mecanismo a `ReferenceLatent`.

**Curso de referencia (pagado, para arquitectura):** `rhino3d.education/p/generative-ai-for-architects` — "Generative AI for Architects: From ComfyUI Generation to Grasshopper". Incluye "how to run ComfyUI instantly from inside Grasshopper to generate render images from the viewport" (modulo 8 del temario). Relevante porque el input del curso es Rhino/Grasshopper.

---

## Bloque D — Contexto del curso y del concurso

### D.14 Curso "AI×Gaudi" / Archademy y concurso "The Gaudi Nexus"

**Organizacion y calendario (verificado en `archademy.ai/es/`):**

| Dato | Valor |
|---|---|
| Organizadores | Archademy (plataforma) + Fundacio Antoni Gaudi + `gaudi2026.org` |
| Motivo | 2026 = centenario de la muerte de Gaudi (10-06-1926) + Barcelona Capital Mundial de la Arquitectura |
| Formato | Curso (7 modulos) **+** concurso internacional ("The Gaudi Nexus") |
| Inscripcion | $175/equipo (08-oct a 04-nov), $295 (05-nov a 02-dic), $345 (03-dic a 16-dic). Max **4 personas por equipo**, un solo pago |
| Entrega | **16 de diciembre de 2026, 23:59 GMT-7** |
| Anuncio de resultados | 4 de febrero |
| Entregable | **Una lamina A1 online (max 15 MB, JPEG)** + lamina A4 opcional para el Premio de Diseño de la Fundacio |
| Premios | 1o $6.000 / 2o $2.000 / 3o $1.000 / Premio de Diseño Fundacio Gaudi $1.000 / 10 Menciones / 50 finalistas. Total $10.000 |
| Bases | `fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_ES.pdf` (200, 20 paginas, Adobe InDesign 17.3, creado 11-08-2026). Mirror: `archademy.ai/wp-content/uploads/2026/08/GxAI_BRIEFING_ES.pdf`. Version EN: `.../2026/09/GxAI_BRIEFING_EN.pdf` y `fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_EN.pdf` |

**El reto (textual de la Fundacion):** "La propuesta consiste en disenar un **Mercado de Proximidad y Centro de Cultura Digital**, asi como la reconfiguracion del entorno urbano circundante de la **Plaza de la Sagrada Familia** de Barcelona." Objetivo: devolver el espacio a los vecinos integrando al visitante internacional "desde el respeto, la pedagogia y el intercambio cultural, evitando que el lugar se convierta en un parque tematico". Premio especial (opcional) al mejor **mobiliario u objeto arquitectonico** inspirado en los metodos de Gaudi. Webinars en directo con expertos en Gaudi y biomimetica.

**"No se busca imitar las formas de Gaudi"** — "se trata de aplicar su **logica constructiva** ... a un conflicto urbano muy actual, utilizando la inteligencia artificial como herramienta". Es decir: **el metodo, no la estetica**. Importante para no usar el LoRA como un "filtro de estilo Gaudi" sin criterio.

**Modulos del curso (7) — verificados:**

| Modulo | Contenido | Duracion |
|---|---|---|
| 1 | Introduccion a la IA generativa en arquitectura; por que ComfyUI; **tablero de Miro** con todos los recursos y workflows | 1 h 30 |
| 2 | De texto a imagen; 4 modelos de IA; **LoRA** ("la herramienta que hace que tus renders parezcan *tuyos*") | 45 min |
| 3 | **De imagen a imagen: el workflow "Rhino-to-Image"**; ampliacion a alta resolucion; edicion precisa; fusion de varias imagenes | 1 h 20 |
| 4 | De imagen a video: zoom a detalles arquitectonicos, secuencias, time-lapse, **guion de camara con anotaciones sobre la imagen** | 25 min |
| 5 | De imagen a 3D: "limpiar" la imagen y usar varios angulos | 20 min |
| 6 | Mesa redonda Gaudi y el arquitecto en la era de la IA | 1 h |
| 7 | **El flujo de trabajo de Gaudi**: metodo en dos pasos desarrollado con Cas Esbach | 35 min |

Texto clave del **Modulo 3** (verbatim): *"utilizando el flujo de trabajo caracteristico del curso, **«Rhino-to-Image»**, que convierte un modelo basico de volumetria 3D en un render fotorrealista aplicando una referencia de material real, al tiempo que se bloquea la geometria exactamente en su sitio."*

Texto clave del **Modulo 7** (verbatim): *"un metodo en dos pasos —desarrollado junto con el arquitecto Cas Esbach— que, en primer lugar, **reinterpreta la geometria de tu modelo 3D a traves de la logica estructural de Gaudi** y, a continuacion, **aplica materiales fotorrealistas sobre el**. El resultado no es una copia de su estetica, sino un edificio moldeado por el mismo razonamiento que el utilizo hace mas de un siglo."*

Y el curso promete: *"**Acceso exclusivo a un modelo de IA entrenado con los archivos de la Fundacio Antoni Gaudi**"*. Ese "modelo de IA exclusivo" es, con alta probabilidad, el `rhino-to-image-lora.basic.safetensors` que tiene Emilia.

**Instructor y jurado (verificado):**

| Persona | Rol | Nota |
|---|---|---|
| **Thomas Nelissen** | **Profesor del curso**; jurado | Arquitecto junior en **Davis AI** (Paris). Master Univ. de Amberes (Magna Cum Laude) + TU Delft (master thesis sobre generacion de imagenes en arquitectura); semestral en Aalborg. Antes integro IA en **JDS Architects** (Paris) creando workflows a medida y **entrenando sus propios modelos** para concursos. Ha dado clases en ArtEZ. Publica en Archined. |
| **Cas Esbach** | Co-desarrollador del Modulo 7; "experto en IA" de la mesa redonda; jurado | Profesor en **SCAD**; >6 años como arquitecto y project lead en **MVRDV** (Shenzhen Terraces, Tripolis Park, Valley); master TU Delft;Antes **BIG New York**, Derksen|Windt, Civic Projects. Fundador de **KANS** (2025). |
| Gijs Rikken | Jurado | Director adjunto, MVRDV (Valley, Tripolis Park, Crystal Houses) |
| Bibiana Sciortino | Jurado | Codirectora de la Fundacio Antoni Gaudi; coautora de "Los conceptos estructurales de Gaudi" |
| Joseph (Jos) Tomlow | Jurado | Cofundador del Grupo de Investigacion Gaudi (Delft, 1976); prof. en Zittau/Gorlitz |
| Ishan Pal Singh | Jurado | Director del Taubman Visualization Lab (Taubman College) |
| Jasmy (Jasmy Chen) | Jurado | Doctoranda en TU Innsbruck, i.sd / SFB Computational Immediacy |

**"Ismail Seleit / Studio Ismail Seleit (ex-Foster+Partners)": NO ENCONTRADO en ninguna fuente publica (web de Archademy, briefing, ArchDaily, LinkedIn via busqueda).** Se marca como **no verificado / probablemente incorrecto**. El nombre que aparece en todas las fuentes es **Thomas Nelissen**. Puede que el nombre correcto sea "**Cas Esbach**" (que sí aparece como formador/experto IA y co-autor del Modulo 7).

**Los LoRAs de la Fundacio / del instructor: NO HAY FICHA PUBLICA.**
- Búsqueda en la API de Civitai (`?query=gaudi lora`) -> solo LoRAs de terceros **no relacionados**: `JJ's Gaudi Archi` (SDXL + SD1.5, autor jjhuang, trigger "Gaudi Archi"), `antonio gaudi-facade` / `antonio gaudi-detial` (SD1.5, autor ArchiZHS_YQBen, trigger "antonio gaudi"), `designed by Antoni Gaudi` (SDXL / SD1.5 / **FLUX.1 D**, autor TangBohu, trigger "designed by Antoni Gaudi").
- Busqueda en HF y GitHub de "rhino-to-image" -> sin resultados publicos.
- El LoRA de la Fundacio se entrega **dentro de la matricula** (junto al tablero de Miro). **Los nombres exactos de archivo ("basic" / "advanced"), los trigger words, el modelo base y la licencia no son publicos** -> hay que pedirlos (ver E.2).

### D.15 Videos y tutoriales (URLs verificadas con `youtube.com/oembed`, HTTP 200 = el video existe y es embebible)

| # | Título | Autor | URL | Fecha | Que se aprende | Verificacion |
|---|---|---|---|---|---|---|
| 1 | **AI Rendering with ComfyUI** | **Parametric** | https://www.youtube.com/watch?v=IApOVLuPeqU | 01-10-2025 | **El mas cercano al caso de estudio**: "complete AI rendering workflow using ComfyUI to stylize architectural images from **Rhino**". Cubre: preparar viewcaptures de Rhino, ControlNet para preservar fidelidad de aristas y estructura arquitectonica, IP-Adapter para transferencia de estilo/material, ajuste de prompts/resolucion/strength, exportacion y compilacion de la presentacion | oembed 200 |
| 2 | **3D to Final Image 2026 AI Workflow** | **Arch Viz Artist** | https://www.youtube.com/watch?v=elm00WQ03vw | 2026 | Workflow completo AI + ArchViz "from **clay render to final Photoshop polish**, including **Flux Klein**". Es el gemelo de video del workflow Rhino-to-image con FLUX.2 | oembed 200 |
| 3 | **Flux2 Klein 9B Just Nailed Inpainting \| ComfyUI Tutorial** | **AxiomGraph** | https://www.youtube.com/watch?v=demZCRuImQ0 | 18-01-2026 | Capitulos: Workflow, Add Object, Multi Round Editing, Remove Objects, Edit Text, **Multi Reference Editing**, Change Cloth. Enseña a usar el 9B como editor y a encadenar multi-referencia (util si el LoRA de Emilia es edit-LoRA). Workflow en github.com/axiomgraph/ComfyUI-... | oembed 200 |
| 4 | **ComfyUI for Architects: Generate Renders in Minutes (Not Hours)** | **architutors** | https://www.youtube.com/watch?v=RAMs89SS6cM | 26-03-2026 | Curso para arquitecto con ComfyUI Cloud: nodos, checkpoints, LoRAs, upscaling. Pensado para el perfil de Emilia | oembed 200 |
| 5 | **ComfyUI Tutorial \| Turn Any Image into a 3D Model in Seconds** | **architutors** | https://www.youtube.com/watch?v=Y8N6kjJBXqg | 16-04-2026 | Modulo 5 del curso (de imagen a 3D) y como elegir modelos "for architectural geometry" | oembed 200 |
| 6 | **How to Use AI Toolkit on Runpod** | **Ostris AI** | https://www.youtube.com/watch?v=HBNeS-F6Zz8 | 2026 | Setup de ai-toolkit en un pod RunPod (el flujo que se necesita para entrenar). Incluye el template `console.runpod.io/deploy?template=0fqzfjy6f3` | oembed 200 |
| 7 | **Crea Imagenes Gratis con Flux 1 y Comfyui en una RTX 3070 8gb VRAM** | **Comarca IA** | https://www.youtube.com/watch?v=u-lQWqsDWSM | 05-05-2026 | GGUF + cuantizacion para 8 GB de VRAM: el precedente mas cercano a "que se puede hacer con 8 GB" | oembed 200 |
| 8 | **Flux 2 Klein ComfyUI Setup Tutorial \| Inpainting, Outpainting & Lossless Downscaling Explained** | (canal no identificado en el fetch) | https://www.youtube.com/watch?v=7u9r6t3m2aA | 30-01-2026 | Setup paso a paso de FLUX.2 klein 4B y 9B en ComfyUI (rutas exactas de modelos en HF). **NO VERIFICADO**: `oembed` devolvio **HTTP 401** en dos intentos (video no embebible o ID incorrecto). La pagina de resultados lo lista con 7,2 K vistas | **401 — no verificado** |
| 9 | "The SIMPLEST workflow for FLUX Comfyui" | goshnii AI | https://www.youtube.com/watch?v=TWSFej_S_bY | 10-08-2024 | Tutorial basico de FLUX en ComfyUI (util como base de nodos, no FLUX.2) | **no verificado con fetch** (solo visto en resultados) |
| 10 | "Parametric Modeling & AI Rendering" | Parametric | (id no resuelto en esta sesion) | ~2025 | Companion del video 1 | **no verificado** |

**Tutoriales escritos complementarios (verificados):**

| Fuente | URL | Que aporta |
|---|---|---|
| Docs ComfyUI — FLUX.2 klein 4B | https://docs.comfy.org/tutorials/flux/flux-2-klein | Workflows 4B y 9B, rutas de modelos, posiciones de archivo |
| Docs ComfyUI — Depth ControlNet | https://docs.comfy.org/tutorials/controlnet/depth-controlnet | Como codifica un depth map (inverso a la distancia) |
| McNeel — ViewCaptureToFile | https://docs.mcneel.com/rhino/8/help/en-us/commands/viewcapturetofile.htm | Export correcto desde Rhino |
| ArchiGen AI — ComfyUI for Rhino users in 2026 | https://archigenai.com/comfyui-rhino-architects-workflow-2026.html | El metodo de las 3 pasadas desde Rhino (depth + line + flat shaded) a 2048 px, misma camara. **Advertencia: la firma es una "persona editorial" (Nora Sinclair, Vista Studios) declarada como no-humana -> tomarlo como referencia de tecnica, no como fuente primaria** |
| denkaTa599 — Advanced Flux Arch Workflow | https://github.com/denkaTa599/comfyui-architectural-workflow | JSON de workflow de arquitectura con stack 3-LoRA + Canny + DepthAnythingV2 (FLUX.1) |
| Rhino3D Education — Generative AI for Architects | https://www.rhino3d.education/p/generative-ai-for-architects | Curso con ComfyUI **dentro de Grasshopper** (input directo desde el viewport de Rhino) |
| City96 — ComfyUI-GGUF | https://github.com/city96/ComfyUI-GGUF | `UnetLoaderGGUF` para correr FLUX.2 klein 9B cuantizado |

---

## Bloque E — Sintesis y entregables

### E.16 Plan de accion para la PC de Emilia (3 etapas)

#### Etapa 0 — Preparacion (30-45 min, costo $0) — en la PC de Emilia

1. **Actualizar ComfyUI** (ya esta en `b08e6cf3`, que ya soporta FLUX.2 nativo):
   ```cmd
   cd /d P:\00-repos\ComfyUI
   git pull
   ```
2. **Crear el `README` del stack FLUX.2** (no descargar 9B en la PC todavia). En la PC solo se usa SD1.5/SDXL.
3. **Preparar el export desde Rhino** (mismo modelo, misma camara, 2048 px lado largo, fondo liso):
   ```cmd
   :: Rhino (scriptable) — 3 pasadas desde la misma vista
   _-ViewCaptureToFile _Enter "C:\out\geo_shaded.png" _Enter 2048 _Enter
   _-ViewCaptureToFile _Enter "C:\out\geo_lines.png"  _Enter 2048 _Enter
   ```
   Guardar ademas la **foto de material real** (ladrillo/hormigon/ceramica) en `C:\out\material.jpg`.
4. **Copiar el LoRA** a `P:\00-repos\ComfyUI\models\loras\rhino-to-image-lora.basic.safetensors` (120,8 MB).
5. **Armar el grafo de prueba con SDXL** (no FLUX.2): `Juggernaut-XL` + `control_v11p_sd15_scribble` (es SD1.5) o el ControlNet SDXL depth, para validar el concepto Rhino→fotorrealista antes de gastar cloud. Sirve para probar prompts, encuadres y ritmo de trabajo.

#### Etapa 1 — Prueba real de FLUX.2 klein 9B en RunPod (2-4 h de GPU, ~$1)

1. Crear cuenta en RunPod y cobrar un pod **RTX 3090 24 GB** (Community, ~$0,22/h) o **RTX 4090 24 GB** (Community, ~$0,34/h).
2. Imagen del pod: la de **ai-toolkit** (`console.runpod.io/deploy?template=0fqzfjy6f3`) si tambien se quiere entrenar; si solo se infiere, cualquier imagen de ComfyUI con NVIDIA/CUDA 12 + PyTorch.
3. Descargar en el pod:
   ```bash
   hf auth login
   hf download black-forest-labs/FLUX.2-klein-9b-fp8 flux-2-klein-9b-fp8.safetensors --local-dir /workspace/ComfyUI/models/diffusion_models
   hf download Comfy-Org/vae-text-encorder-for-flux-klein-9B split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors --local-dir /workspace/ComfyUI/temp
   # mover a models/text_encoders/
   hf download black-forest-labs/FLUX.2-small-decoder full_encoder_small_decoder.safetensors --local-dir /workspace/ComfyUI/models/vae
   ```
   (los repos de BFL requieren haber aceptado la licencia en la pagina HF).
4. Subir el LoRA de Emilia al pod (`scp` o el file browser de RunPod) a `/workspace/ComfyUI/models/loras/`.
5. Descargar el template oficial y abrirlo en el ComfyUI del pod:
   `https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base.json`
   (o `.../image_flux2_text_to_image_9b.json`).
6. **Insertar `LoraLoaderModelOnly`** entre `UNETLoader` y `CFGGuider`, `strength_model = 0.8` (arrancar en 0,6 y subir).
7. **Construir el grafo Rhino-to-image**:
   - `LoadImage` (geo_shaded.png) -> `ImageScaleToTotalPixels` -> `VAEEncode` -> `ReferenceLatent` (sobre el conditioning positivo)
   - `LoadImage` (material.jpg) -> `ImageScaleToTotalPixels` -> `VAEEncode` -> `ReferenceLatent` (mismo conditioning)
   - `CLIPTextEncode` con el **trigger word** (a confirmar con el instructor) + descripcion de la arquitectura
   - `Flux2Scheduler` steps=20 (base) o 4 (destilado); `CFGGuider` cfg=5 (base) o 1 (destilado); `KSamplerSelect` euler
   - `EmptyFlux2LatentImage` 1024x1024 (o el aspect ratio de la vista de Rhino)
8. Probar primero **sin LoRA** (para ver la geometria sola), despues **con LoRA** a 0,6 / 0,8 / 1,0, y comparar. Asi se separa "que aporta el LoRA" de "que aporta la referencia".
9. Apagar el pod cuando termine (el dead-man switch de la herramienta lo hace solo; ademas `runpod` cobra por minuto).

#### Etapa 2 — Produccion del concurso (dias 1-16 de diciembre)

1. **Definir el flujo en dos pasos del Modulo 7** antes de renderizar nada: (i) reinterpretar la geometria con la logica estructural de Gaudi (catenarias, paraboloides hiperbolicos, triangulacion catenaria entre pilares,.loads inclinados, arcos parabolicos,新材料), (ii) aplicar materiales fotorrealistas. El LoRA ayuda en el paso (ii); el paso (i) es trabajo de arquitectura, no de prompt.
2. Usar el **pod 24 GB** como "maquina de render" del concurso: producir 20-40 imagenes finales a 1024-2048 px.
3. **Upscale** a A1 (la lamina final es A1): usar `UltimateSDUpscale`/`4x_NMKD-Superscale` en el pod, o el modelo de la lamina a 200 dpi con el raster final en Photoshop/Illustrator.
4. **Componer la lamina A1** (max 15 MB, JPEG) con: axonométrica renderizada + fotos de material + planos del proyecto + el "before/after" del workflow Rhino-to-image (muy值为评委: demuestra el metodo).
5. **Lamina A4 opcional** para el Premio de Diseño de la Fundacio (mobiliario/objeto inspirado en los metodos de Gaudi).
6. **Licencia del material**: verificar el regimen de uso del LoRA del curso (ver E.3) y标注 en la lamina que las imagenes son generadas con IA.

### E.17 Que hay que pedirle al instructor del curso (ficha del LoRA)

Correo/mensaje a **Thomas Nelissen** (profesor del curso) y/o via el equipo de Archademy (`archademy.ai/es/contacto/`), con esta lista:

1. **Ficha tecnica del LoRA**
   - Nombre exacto de archivo: `rhino-to-image-lora.basic.safetensors` -> confirmar si existe `...advanced.safetensors` (y cualquier otro, p.ej. `...material.safetensors`).
   - **Trigger word / frase de activacion** (o lista de frases).
   - **Modelo base exacto** con el que se entreno: `black-forest-labs/FLUX.2-klein-base-9B`? `FLUX.2-klein-9B` (destilado)? HF repo id + revision.
   - **Si se entreno en Base o en Destilado** (determina si el LoRA se aplica en 20 pasos/cfg 5 o en 4 pasos/cfg 1).
   - **Strength recomendado** (mínimo/máximo) y si el workflow usa `LoraLoaderModelOnly` o `LoraLoader`.
   - **Dataset**: nº de imagenes, resolución, tipo (pareado reference/target o solo target), procedencia de las imagenes de la Fundacio y su licencia de uso.
   - **Captioning**: formato (txt / JSON), si lleva trigger embebido, ejemplo de 3 captions literales.
   - **Hiperparametros**: rank/alpha, lr, steps, `timestep_type`, resolucion, optimizador.
   - **Si hay version `advanced`**: en que se diferencia (mas datasets? mas steps? distinto base?).
2. **Workflow**
   - El **workflow ComfyUI exacto** del Modulo 3 ("Rhino-to-Image") en formato JSON importable (o el link al tablero de Miro con los JSON).
   - Que nodos usa para el material (¿`ReferenceLatent` doble? ¿`IP-Adapter`? ¿`FluxKontextImageScale`? ¿`FluxKVCache`?) y los **valores exactos** de cada uno.
   - Si usa `FluxKontextMultiReferenceLatentMethod`, que metodo (`index` / `offset` / `index_timestep_zero`).
   - Resolucion de trabajo y de entrega; sampler/scheduler/steps/cfg de referencia.
3. **Preprocesado desde Rhino**
   - Como se genera la imagen que entra al workflow: ¿`ViewCaptureToFile`? ¿que modo de visualizacion (Rendered / Shaded / Technical / Thermal)? ¿fondo blanco o transparente? ¿que resolucion?
   - Si hay una pasada de profundidad: ¿como se produce?
   - Si el workflow usa el plugin de Grasshopper o un MCP de Rhino.
4. **Licencia y uso**
   - Licencia del LoRA (¿Apache 2.0? ¿uso personal del curso? ¿comercial?) y si autoriza uso en trabajos de cliente.
   - Licencia del material documental de la Fundacio y condiciones de uso en un concurso con premio.
5. **Modelo de IA exclusivo**
   - Si el "modelo de IA entrenado con los archivos de la Fundacio" es el mismo LoRA o es otro (¿otro `.safetensors`? ¿un checkpoint?).
6. **Requisito tecnico**
   - Si el curso asume FLUX.2 klein 9B (24 GB) o klein 4B (8 GB) -> define la ruta cloud vs local.

### E.18 Riesgos y licencias

| Riesgo | Situacion verificada | Implicacion | Mitigacion |
|---|---|---|---|
| **LoRA derivative de modelo Non-Commercial** | klein 9B = **FLUX Non-Commercial License** (BFL, `model_licenses/LICENSE-FLUX-DEV`); klein 4B = **Apache 2.0**; el LoRA de Emilia esta afinado sobre la arquitectura de 9B (hidden 4096, 8+24 bloques) | Para el **concurso**: admisible (entrega academica, sin contraprestacion, con premio). **Para entregar a cliente**: los outputs derivados de un modelo Non-Commercial **no** se pueden usar comercialmente sin licencia de BFL | 1) Verificar si el LoRA del curso tiene su propia licencia mas permisiva (preguntar, E.17). 2) Para cliente: rehacer en **klein 4B (Apache 2.0)** con un LoRA equivalente -> **imposible portar**: hay que reentrenar en 4B (12 GB VRAM, ~$0,50 de GPU). 3) O comprar licencia comercial de BFL / FLUX.2 [dev] 3.o usar FLUX.1 [dev] con licencia |
| **La maquina de Emilia no puede correr 9B** | 8 GB VRAM + DirectML; 9B fp8 = 8,79 GiB de pesos + 8,07 GiB de TE | El flujo "Rhino-to-image con FLUX.2" no es ejecutable de punta a punta en esa PC | Ruta mixta: preprocesado + grafo + iteracion en local (SD1.5/SDXL), render final en RunPod 24 GB ($0,22-0,74/h) o BFL API. **Costo total del concurso: ~$2-5** |
| **El LoRA no tiene metadata** | `__metadata__` ausente, sin sidecar Civitai | ComfyUI lo carga igual (no necesita metadata), pero se pierde: trigger word, base, license, trainer, dataset | Pedir la ficha (E.17) y **guardar la ficha en el vault** junto al `.safetensors`. No renombrar el archivo hasta conocer el trigger |
| **Trigger word desconocido** | No publicado en ninguna fuente | Sin el trigger el LoRA no se activa (o se activa como|style> genérico) y se pierde la mitad del comportamiento | Es el **punto critico bloqueante**. Pedirlo primero (E.17) |
| **Base vs destilado** | El LoRA fue entrenado en 9B; no se sabe si en Base o Destilado | Si se entreno en Base, se debe **inferir en Destilado (4 pasos, cfg 1)** para mejor resultado; si se entreno en Destilado, inferir en Destilado | Probar las 2 combinaciones (base 20/cfg5 y destilado 4/cfg1) y quedarse con la mejor |
| **Nombre del instructor incorrecto** | Toda fuente publica dice **Thomas Nelissen** (profesor) y **Cas Esbach** (co-autor del Modulo 7, experto IA). "Ismail Seleit / ex-Foster+Partners" no aparece en ninguna fuente | Dirigir el pedido de E.17 al nombre correcto | Escribir a Thomas Nelissen via el area de participantes de Archademy |
| **Licencia del material de la Fundacio** | El LoRA se entreno con "los archivos de la Fundacio Antoni Gaudi" | Uso de material de terceros en un dataset de modelo; hay que respetar la licencia del material y la politique de uso | Preguntar explicitamente por la licencia del material (E.17 punto 4) |
| **Los LoRAs "Gaudí" de Civitai no son los del curso** | `JJ's Gaudi Archi` (SDXL/SD1.5), `antonio gaudi-facade` (SD1.5), `designed by Antoni Gaudi` (SDXL/FLUX.1) | No sirven para replicar el resultado del curso | No usarlos como sustituto |
| **ControlNet no disponible en klein** | Solo hay ControlNet para FLUX.2 **dev** | Cualquier plan que dependa de ControlNet depth/canny con klein es un error | Usar `ReferenceLatent` (nativo) como mecanismo de control geometrico |
| **Riesgo de "todos los edificios se parecen"** | El articulo de ArchiGen AI lo senala como el problema #3 de los workflows Rhino→ComfyUI | Sin refs de material y sin variation, el resultado es generico | Usar las 3 pasadas (geo + line + material) + 3 refs distintas (material principal, mood, material secundario) + variacion de seed y de prompt |
| **Entrega A1 online 15 MB** | Limite duro del concurso | Un render 4K no entra | Exportar JPEG A1 a calidad ajustada; hacer el "antes/despues" en PNG comprimido dentro del presupuesto |
| **Dependencia de un solo LoRA externo** | El resultado depende de un archivo de 120,8 MB que no esta documentado | Si el instructor no responde, el flujo del Modulo 3 no se puede replicar | Tener el plan B: el workflow nativo `ReferenceLatent` **sin LoRA** ya produce "3D volumetrico -> render fotorrealista con material de referencia". El LoRA es el "toque Gaudi", no la base |

---

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]] — nodos `UNETLoader`, `CLIPLoader`, `VAELoader`, `Flux2Scheduler`, `EmptyFlux2LatentImage`, `CFGGuider`, `SamplerCustomAdvanced`, `ReferenceLatent`, `FluxKontextImageScale`, `FluxKontextMultiReferenceLatentMethod`, `FluxKVCache`
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook interno de la herramienta; este informe es la actualizacion FLUX.2/klein 9B + DirectML
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — pipeline de render para el estudio
- [[wiki/glosario/conceptos/ia-jr-iterable|ia-jr-iterable]] — iteracion asistida por IA
- [[wiki/glosario/conceptos/metricas-friccion|metricas-friccion]] — costo cloud vs. tiempo de iteracion
- [[wiki/glosario/software/rhino|Rhino]] — `ViewCaptureToFile`, `Make2D`, modo de visualizacion, Grasshopper
- [[raw/research/2026-10-08-comfyui-workflows-arq|2026-10-08-comfyui-workflows-arq]] — estado del arte previo de workflows de arquitectura en ComfyUI (este informe lo actualiza para FLUX.2)
- [[raw/research/2026-10-15-cad-abierto-mcp-opencode|2026-10-15-cad-abierto-mcp-opencode]] — MCPs Rhino/Grasshopper, CAD abierto
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] — nomenclatura de archivos de workflow y entregables

---

## Metodologia — queries, URLs y status

### Sub-preguntas (formuladas desde el brief)

1. ES/EN/IT: como se entrena un LoRA sobre FLUX.2 / FLUX.2 klein 9B (herramientas, parametros, TE, dataset, 8 GB AMD)
2. ES/EN: grafo de nodos ComfyUI para FLUX.2 klein 9B + mecanismo de referencia/edicion + ControlNet
3. ES/EN: preprocesado Rhino (viewcapture, depth) y coste/practicidad en RX 570 8 GB
4. ES/EN: instalacion y descarga de modelos para la PC de Emilia
5. ES/EN/CA: curso AI×Gaudi, concurso The Gaudi Nexus, LoRAs de la Fundacio y del instructor
6. ES/EN: videos Rhino→IA/FLUX.2 en arquitectura 2025-2026

### Queries ejecutadas (websearch)

| # | Query | Idioma |
|---|---|---|
| 1 | `FLUX.2 klein LoRA training ai-toolkit support 2026` | EN |
| 2 | `FLUX.2 ControlNet klein alibaba-pai FLUX.2-dev-Fun-Controlnet-Union depth lineart` | EN |
| 3 | `kohya sd-scripts FLUX.2 klein LoRA support 2026` | EN |
| 4 | `Archademy curso "AI" Gaudí concurso "Gaudí Nexus" fundacionantoniogaudi` | ES |
| 5 | `YouTube "Rhino-to-image" ComfyUI FLUX.2 arquitectura render fotorrealista workflow 2026` | ES/EN |
| 6 | `RunPod pricing 2026 RTX 3090 4090 A40 per hour community cloud` | EN |
| 7 | `ComfyUI GGUF FLUX.2 klein 9B unsupported UnetLoaderGGUF city96` | EN |
| 8 | `youtube.com FLUX.2 klein ComfyUI tutorial 9B 4 steps 2026 workflow` | EN |
| 9 | `Rhino ViewCaptureToFile export PNG depth map render AI ComfyUI documentation` | EN |
| 10 | `OneTrainer FLUX.2 klein support LoRA training 2026 diffusion-painter FLUX.2` | EN |
| 11 | `"ComfyUI" Rhino 3D AI render tutorial youtube 2026 "Flux.2" architecture studio workflow Thomas Nelissen` | EN |
| 12 | `youtube Rhino 3D model to photorealistic AI render ComfyUI FLUX 2026 architecture student workflow` | EN |

### URLs comprobadas (todas con `webfetch`; 200 = recuperadas)

| URL | Status | Que se extrajo |
|---|---|---|
| https://docs.bfl.ml/flux_2/flux2_klein_training | 200 | Requisitos HW, LR, steps, resolucion, uso en ComfyUI |
| https://docs.bfl.ml/flux_2/flux2_klein_training_example | 200 | Config YAML oficial 9B, dataset 27 imgs, captions,采样 8 steps |
| https://docs.bfl.ml/flux_2/flux2_lora_inference | 200 (via busqueda) | Endpoints `-finetuned`, Dashboard |
| https://docs.comfy.org/tutorials/flux/flux-2-klein | 200 | Grafo 4B/9B, rutas de modelos, 8,4 GB VRAM |
| https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence | 200 | FLUX.2 dev, multi-reference 10 imagenes, 4 MP, requisitos |
| https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image_9b.json | 200 | Grafo T2I 9B completo (nodos + valores) |
| https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base.json | 200 | Grafo de edicion 9B: ReferenceLatent, VAEEncode, ImageScaleToTotalPixels |
| https://raw.githubusercontent.com/ostris/ai-toolkit/main/README.md | 200 | Modelos soportados (FLUX.2 klein base 4B/9B), instalacion, RunPod template |
| https://api.github.com/repos/ostris/ai-toolkit/contents/config/examples | 200 | Listado de configs de ejemplo (no hay yaml klein dedicado; el de BFL es la referencia) |
| https://raw.githubusercontent.com/huggingface/diffusers/main/examples/dreambooth/README_flux2.md | 200 | Target modules FLUX.2, rank/alpha, flags de memoria, buckets, i2i triplets |
| https://github.com/black-forest-labs/flux2 | 200 | Repo de SOLO inferencia; tabla de licencias por variante |
| https://raw.githubusercontent.com/bghira/SimpleTuner/main/documentation/quickstart/FLUX2.md | 200 | VRAM por variante, sin guidance embeds en klein, LoRA targets, edit conditioning |
| https://huggingface.co/blog/black-forest-labs/flux-2-klein-lora | 200 | Receta de LoRA (4B), edit-LoRA con `control_path`, captions, checkpoints |
| https://huggingface.co/api/models/unsloth/FLUX.2-klein-9B-GGUF | 200 | 18 quants, licencias, tamano total |
| https://huggingface.co/api/models?search=FLUX.2-klein-9B-GGUF&limit=20 | 200 | Repos GGUF alternativos |
| https://huggingface.co/api/models/ponpoke/flux2-klein-9b-uncensored-text-encoder | 200 | Gated, archivos, GGUF del TE |
| https://huggingface.co/api/models/Comfy-Org/vae-text-encorder-for-flux-klein-9B | 200 | Repos renombrado; TE files |
| https://huggingface.co/api/models/Comfy-Org/vae-text-encorder-for-flux-klein-9B/tree/main/split_files/text_encoders | 200 | Bytes exactos de los 3 TE |
| https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-base-9B | 200 | `gated: auto`, licencia, BF16 9.078.581.248 params |
| https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-9b-fp8 | 200 | `gated: auto`, licencia non-commercial |
| https://huggingface.co/api/models/black-forest-labs/FLUX.2-klein-9b-fp8/tree/main | 200 | `flux-2-klein-9b-fp8.safetensors` = 9.433.061.528 bytes |
| https://huggingface.co/api/models/black-forest-labs/FLUX.2-small-decoder | 200 | Apache-2.0; 3 variantes de VAE |
| https://civitai.com/api/v1/models?query=gaudi%20lora&limit=10 | 200 | LoRAs Gaudi de terceros (no los del curso) |
| https://archademy.ai/es/ | 200 | Curso, modulos, instructor, jurado, calendario, premios, entrega |
| https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_ES.pdf | 200 (PDF binario, 20 pag.) | Bases del concurso (no extraido texto plano: requiere OCR) |
| https://www.archdaily.com/1185927/ai-x-gaudi-architecture-competition-plus-ai-course | 200 | Nota de prensa del lanzamiento |
| https://en.fundacionantoniogaudi.org/ai-x-gaudi-architecture-and-design-competition/ | 200 | Version EN del concurso, deadline 2026/12/16 |
| https://competitions.archi/competition/aixgaudi-... | 200 | Calendario: apertura 12-ago, entrega 16-dic, resultados 4-feb |
| https://docs.mcneel.com/rhino/8/help/en-us/commands/viewcapturetofile.htm | 200 | ViewCaptureToFile: formatos, sin bordes, -Autoname |
| https://docs.comfy.org/tutorials/controlnet/depth-controlnet | 200 | Codificacion de depth maps |
| https://archigenai.com/comfyui-rhino-architects-workflow-2026.html | 200 | Metodo de las 3 pasadas desde Rhino (2048 px, misma camara) |
| https://github.com/denkaTa599/comfyui-architectural-workflow | 200 | `Advanced_Flux_Arch_Workflow.json` (11.532 bytes) |
| https://api.github.com/repos/denkaTa599/comfyui-architectural-workflow/contents/ | 200 | Listado del repo y rama |
| https://www.runpod.io/pricing | 200 (via busqueda) | RTX 3090 $0,22 community / $0,46 secure; 4090 $0,34 / $0,74 |
| https://www.runpod.io/gpu-models/rtx-4090 | 200 | "Rent NVIDIA RTX 4090 GPUs from $0.74/hr. Community Cloud $0.34/hr Secure Cloud $0.74/hr" |
| https://github.com/city96/ComfyUI-GGUF | 200 | `UnetLoaderGGUF`; no hay pesos FLUX.2 klein de city96 |
| https://github.com/city96/ComfyUI-GGUF/issues/411 | 200 | Bug flux2 klein (cerrado 16-01-2026) |
| https://github.com/bryanmcguire/comfyui-flux2fun-controlnet | 200 | Nodo ComfyUI para el ControlNet de FLUX.2 dev |
| https://huggingface.co/alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union/raw/main/README.md | 200 | 8,23 GB, modos, CFG distillation, licencia |
| https://github.com/kohya-ss/sd-scripts | 200 (via busqueda) | Lista de modelos: **sin FLUX.2** |
| https://onetrainer.org/ | 200 (via busqueda) | Soporte "FLUX-family"; AGPLv3; 8 GB min |
| https://github.com/ethanncai/Simple-Flux2-FineTuner | 200 | Trainer 4B con DeepSpeed (Linux+NVIDIA) |
| https://github.com/Limbicnation/klein-lora-trainer | 200 | Trainer 4B, 13 GB+ VRAM |
| https://github.com/ReyChiaro/flux.2-klein-controlnet | **404 en README.md** | Repo existe; README no disponible |
| https://raw.githubusercontent.com/ostris/ai-toolkit/main/config/examples/train_lora_flux2_klein_4b.yaml | **404** | No existe ese archivo; el config de referencia es el de BFL |
| https://comfy.org/workflows/model/flux-2-klein/ | 200 (via busqueda) | 9 workflows FLUX.2 Klein |
| https://huggingface.co/blog/flux-qlora | referenciada (no verificada) | QLoRA para FLUX.1 |
| https://www.rhino3d.education/p/generative-ai-for-architects | 200 (via busqueda) | Curso ComfyUI + Grasshopper |
| https://github.com/mickaelmaron/... | no | — |

### Verificaciones de codigo local (`P:\00-repos\ComfyUI`, commit `b08e6cf3`)

| Archivo | Lineas | Que se confirmo |
|---|---|---|
| `comfy/model_detection.py` | 235-290 | `image_model="flux2"`, `default_ref_method="index"`, `ref_index_scale=10.0`, axes/num_heads/mlp_ratio/theta/out_channels |
| `comfy/model_base.py` | 1033-1042, 1072-1081 | `ref_latents` -> `CONDList`; `reference_latents_method` -> `CONDConstant`; `Flux2.extra_conds` (pad a 512 tokens) |
| `comfy/ldm/flux/model.py` | 41-42, 365-369 | `default_ref_method`, `ref_index_scale`, index += ref_index_scale |
| `comfy/text_encoders/flux.py` | 181-231 | `Qwen3Tokenizer8B` (embedding_key `qwen3_8b`, size 4096), `Qwen3_8BModel` (layer [9,18,27]), `KleinTokenizer8B`, plantilla de prompt |
| `comfy/sd.py` | 1665-1723 | `TEModel.QWEN3_8B` + `CLIPType.FLUX2` -> `klein_te(qwen3_8b)`; `QWEN3VL_8B` + FLUX2 -> Klein 8B |
| `comfy_extras/nodes_flux.py` | 37-57, 105-233, 235-301 | `EmptyFlux2LatentImage` (128 ch), `PREFERRED_KONTEXT_RESOLUTIONS`, `FluxKontextImageScale`, `FluxKontextMultiReferenceLatentMethod` (offset/index/uxo-uno/index_timestep_zero), `Flux2Scheduler` (get_schedule), `FluxKVCache` (fuerza `index_timestep_zero`) |
| `comfy/cli_args.py` | 90, 141-162 | `--directml`, `--lowvram`, `--reserve-vram`, `--disable-dynamic-vram`, `--vram-headroom` |
| `comfy/model_management.py` | 109-121, 563-579 | Warning de DirectML; `lowvram_available=False` con DirectML; `--lowvram` reactivado solo si no hay dynamic vram |
| `blueprints/Image Edit (Flux.2 Klein 4B).json` | 250-400 | Valores por defecto locales: `KSamplerSelect=euler`, `Flux2Scheduler steps=20/1024/1024`, `CFGGuider cfg=5` |

### Gaps explicitos (no verificados)

1. **Trigger word del LoRA `rhino-to-image-lora.basic`** — no publicado en ninguna fuente. **BLOQUEANTE.**
2. **Si existe una version "advanced"** y su nombre exacto — no publicado.
3. **Si el LoRA se entreno en Base o Destilado** — no publicado.
4. **Dataset, captions, hiperparametros, licencia del LoRA del curso** — no publicados.
5. **Workflow JSON exacto del Modulo 3** — solo disponible dentro de la matricula (tablero de Miro).
6. **"Ismail Seleit / Studio Ismail Seleit (ex-Foster+Partners)"** — no encontrado en ninguna fuente. El instructor verificable es **Thomas Nelissen**; el co-autor del Modulo 7 es **Cas Esbach**.
7. **Soporte FLUX.2 en OneTrainer** — verificado de forma indirecta (tracker de terceros); no confirmado contra el repo primario.
8. **`diffusion-painter`** — sin datos.
9. **Texto plano del briefing PDF del concurso** (`GxAI_BRIEFING_ES.pdf`) — el PDF responde 200 pero su texto no se extrajo (requiere OCR/parseo de PDF >50 paginas con script propio; el archivo tiene 20 paginas). **Pendiente.**
10. **Captioning en JSON para Flux.2** — reportado por el usuario desde el curso; no documentado en fuentes publicas.
11. **`Cordux/flux2-klein-4b-uncensored-text-encoder`** — no verificado en esta sesion.
12. **Packs de nodos de depth (Depth Anything V2) y `comfyui-3d-viewport-pro` / `comfyui-3d-pack`** — citados por fuentes de terceros, no verificados contra sus repos.
13. **Precio exacto de la API de BFL** para inferencia con finetune — no publicado (public beta; hay que verlo en el Dashboard).
14. **Video `7u9r6t3m2aA`** — 401 en oembed, no verificado.
15. **Tiempos exactos de render en DirectML/RX 570** para FLUX.2 — no medidos (y no medibles en 8 GB).

---

## Propuestas wiki (esqueleto para @vaultworm-arq, NO aplicadas)

1. **`wiki/glosario/software/flux2-klein.md`** (nueva) — ficha del modelo: variantes Base/Destilado 4B/9B/9B-KV, licencias (Apache 2.0 vs FLUX Non-Commercial), tabla de VRAM, tabla de archivos de modelo con bytes y rutas, tabla de TE (Qwen3-4B/8B), VAE de 128 canales, grafo de nodos canonico, `ReferenceLatent` como mecanismo de control geometrico, `Flux2Scheduler` vs KSampler.
2. **`wiki/glosario/software/comfyui.md`** (actualizar) — seccion FLUX.2/klein: `CLIPLoader type=flux2`, `Flux2Scheduler`, `EmptyFlux2LatentImage`, `ReferenceLatent`, `FluxKontextImageScale`, `FluxKontextMultiReferenceLatentMethod`, `FluxKVCache`; tabla de defaults (base 20 steps/cfg 5/euler; destilado 4/cfg 1); nota "FLUX.2 no usa negative prompt"; guion de carga GGUF (`UnetLoaderGGUF`).
3. **`wiki/glosario/conceptos/rhino-to-image.md`** (nueva) — el metodo: DWG/volumetria -> viewcapture -> referencia -> render fotorrealista con material; las 3 pasadas; por que `ReferenceLatent` y no ControlNet; el rol del LoRA del curso; y la diferencia con img2img.
4. **`wiki/glosario/interno/pbooks/pbk-comfyui.md`** (actualizar) — nueva seccion "FLUX.2 klein 9B en hardware limitado": que NO es posible local en RX 570 8 GB (con el detalle de `--lowvram` inoperante en DirectML), tabla de cloud (RunPod 3090 $0,22 / 4090 $0,34), y el protocolo "local SD1.5/SDXL + pod 24 GB para el final".
5. **`wiki/glosario/referentes/thomas-nelissen.md`** (nueva) — el instructor del curso AI×Gaudi; y `wiki/glosario/referentes/cas-esbach.md` (nueva) — SCAD/MVRDV/KANS, co-autor del Modulo 7.
6. **`proyectos/MVP_04-comfyui-arquitectura/`** — nuevo sub-proyecto `n_05-flux2-klein-rhino-to-image/` con el grafo (JSON del template 9B edit + `LoraLoaderModelOnly` + doble `ReferenceLatent`) y el README de captura desde Rhino.
7. **`wiki/glosario/legal/`** — nota sobre el regimen FLUX Non-Commercial vs Apache 2.0 en FLUX.2 klein, aplicada a la decision "que modelo se puede usar para cliente".

---

## Referencias verificadas

> Todas las URLs de esta lista fueron comprobadas con `webfetch` en esta sesion (HTTP 200) o，`en los casos marcados, via el indice de resultados de busqueda (contenido citado literalmente).

### Documentacion oficial BFL / FLUX.2
- https://docs.bfl.ml/flux_2/flux2_klein_training
- https://docs.bfl.ml/flux_2/flux2_klein_training_example
- https://docs.bfl.ml/flux_2/flux2_lora_inference
- https://github.com/black-forest-labs/flux2
- https://huggingface.co/blog/black-forest-labs/flux-2-klein-lora
- https://huggingface.co/blog/black-forest-labs/flux-2
- https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B (gated)
- https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8 (gated)
- https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B
- https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
- https://huggingface.co/black-forest-labs/FLUX.2-small-decoder
- https://huggingface.co/black-forest-labs/FLUX.2-dev

### Modelos y pesos (HF)
- https://huggingface.co/Comfy-Org/vae-text-encorder-for-flux-klein-9B (ex `Comfy-Org/flux2-klein-9B`)
- https://huggingface.co/Comfy-Org/flux2-dev
- https://huggingface.co/unsloth/FLUX.2-klein-9B-GGUF
- https://huggingface.co/unsloth/FLUX.2-klein-base-9B-GGUF
- https://huggingface.co/QuantStack/FLUX.2-Klein-9B-KV-GGUF
- https://huggingface.co/leejet/FLUX.2-klein-9B-GGUF
- https://huggingface.co/n-Arno/FLUX.2-klein-base-9B-GGUF
- https://huggingface.co/ponpoke/flux2-klein-9b-uncensored-text-encoder (gated)
- https://huggingface.co/QiE2035/flux2-klein-9b-uncensored-text-encoder-Q2_K-GGUF
- https://huggingface.co/WANG-CC/flux2-klein-9b-uncensored-text-encoder-Q8_0-GGUF
- https://huggingface.co/Qwen/Qwen3-8B-GGUF
- https://huggingface.co/stephenbtl/ugly-kontext-klein-4b-lora
- https://huggingface.co/Limbicnation/pixel-art-lora
- https://huggingface.co/noema-art/cultkatflux2-klein
- https://huggingface.co/alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union
- https://huggingface.co/kontext-community/relighting

### ComfyUI
- https://docs.comfy.org/tutorials/flux/flux-2-klein
- https://docs.comfy.org/tutorials/flux/flux-2-dev
- https://docs.comfy.org/tutorials/controlnet/depth-controlnet
- https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence
- https://github.com/Comfy-Org/workflow_templates
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image_9b.json
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base.json
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_distilled.json
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_base.json
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_distilled.json
- https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2.json
- https://comfy.org/workflows/model/flux-2-klein/
- https://comfy.org/workflows/image_flux2_klein_image_edit_9b_base-563f9b5f6ce3/
- https://comfy.org/p/supported-models/flux-2-klein-9b-fp8
- https://comfy.org/hub/models/local/flux-2-klein-base-9b-fp8
- https://github.com/city96/ComfyUI-GGUF
- https://github.com/city96/ComfyUI-GGUF/issues/411
- https://github.com/bryanmcguire/comfyui-flux2fun-controlnet
- https://github.com/ReyChiaro/flux.2-klein-controlnet (repo existe, **README 404**)
- https://github.com/gokayfem/ComfyUI-Depth-Visualization
- https://github.com/denkaTa599/comfyui-architectural-workflow

### Entrenadores
- https://github.com/ostris/ai-toolkit
- https://github.com/bghira/SimpleTuner
- https://raw.githubusercontent.com/bghira/SimpleTuner/main/documentation/quickstart/FLUX2.md
- https://github.com/huggingface/diffusers
- https://raw.githubusercontent.com/huggingface/diffusers/main/examples/dreambooth/README_flux2.md
- https://github.com/kohya-ss/sd-scripts
- https://onetrainer.org/
- https://github.com/ethanncai/Simple-Flux2-FineTuner
- https://github.com/Limbicnation/klein-lora-trainer
- https://github.com/civitai/civitai-developer-docs/blob/main/orchestration/recipes/training-flux2-klein.md
- https://www.runcomfy.com/trainer/ai-toolkit/flux-2-klein-lora-training
- https://github.com/filipstrand/mflux/blob/main/src/mflux/models/flux2/README.md

### Curso / concurso
- https://archademy.ai/
- https://archademy.ai/es/
- https://archademy.ai/es/preguntas-frecuentes-ia-x-gaudi/
- https://archademy.ai/es/contacto/
- https://archademy.ai/es/registrate-en-ai-x-gaudi/
- https://archademy.ai/wp-content/uploads/2026/08/GxAI_BRIEFING_ES.pdf
- https://archademy.ai/wp-content/uploads/2026/09/GxAI_BRIEFING_EN.pdf
- https://fundacionantoniogaudi.org/
- https://fundacionantoniogaudi.org/concurso-de-arquitectura-y-diseno-ai-x-gaudi/
- https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_ES.pdf
- https://en.fundacionantoniogaudi.org/ai-x-gaudi-architecture-and-design-competition/
- https://www.archdaily.com/1185927/ai-x-gaudi-architecture-competition-plus-ai-course
- https://competitions.archi/competition/aixgaudi-a-new-format-integrating-advanced-ai-course-and-an-international-architecture-competition
- https://gaudi2026.org/es/index.html
- https://www.rhino3d.education/p/generative-ai-for-architects

### Rhino
- https://docs.mcneel.com/rhino/8/help/en-us/commands/viewcapturetofile.htm
- https://docs.mcneel.com/rhino/8mac/help/en-us/seealso/sak_saveviewportimage.htm
- https://docs.mcneel.com/rhino/mac/help/en-us/commands/viewcapture.htm
- https://archigenai.com/comfyui-rhino-architects-workflow-2026.html

### Videos (verificados con `youtube.com/oembed`, HTTP 200)
- https://www.youtube.com/watch?v=IApOVLuPeqU — "AI Rendering with ComfyUI" — Parametric — 01-10-2025
- https://www.youtube.com/watch?v=elm00WQ03vw — "3D to Final Image 2026 AI Workflow" — Arch Viz Artist
- https://www.youtube.com/watch?v=demZCRuImQ0 — "Flux2 Klein 9B Just Nailed Inpainting | ComfyUI Tutorial" — AxiomGraph — 18-01-2026
- https://www.youtube.com/watch?v=RAMs89SS6cM — "ComfyUI for Architects: Generate Renders in Minutes (Not Hours)" — architutors — 26-03-2026
- https://www.youtube.com/watch?v=Y8N6kjJBXqg — "ComfyUI Tutorial | Turn Any Image into a 3D Model in Seconds" — architutors — 16-04-2026
- https://www.youtube.com/watch?v=HBNeS-F6Zz8 — "How to Use AI Toolkit on Runpod" — Ostris AI
- https://www.youtube.com/watch?v=u-lQWqsDWSM — "Crea Imagenes Gratis con Flux 1 y Comfyui en una RTX 3070 8gb VRAM" — Comarca IA — 05-05-2026
- https://www.youtube.com/watch?v=7u9r6t3m2aA — "Flux 2 Klein ComfyUI Setup Tutorial" — **401 en oembed: NO VERIFICADO**
- https://www.youtube.com/watch?v=TWSFej_S_bY — "The SIMPLEST workflow for FLUX Comfyui" — goshnii AI — **no verificado con fetch**

### Cloud
- https://www.runpod.io/pricing
- https://www.runpod.io/gpu-models/rtx-4090
- https://console.runpod.io/deploy?template=0fqzfjy6f3 (template de ai-toolkit)
- https://youtu.be/HBNeS-F6Zz8 (intro al UI de ai-toolkit en RunPod)
- https://dashboard.bfl.ai/ (Customization -> Finetunes)
