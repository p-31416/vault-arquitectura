---
tipo: research-crudo
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
autor: sherlock
idioma: es
tags: [research, crudo, flux2, klein, lora, rhino, gaudi, comfyui]
informe: "[[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|2026-10-20-flux2-klein-lora-rhino-to-image]]"
---

# Crudo de fuentes — FLUX.2 [klein] 9B + LoRA "Rhino-to-Image" (2026-10-20)

> Extractos literales de las fuentes consultadas. Se conservan en texto plano para re-lectura sin volver a la red. Cada bloque indica la URL y el status de verificacion.

---

## 1. BFL — FLUX.2 [klein] Training (200)

URL: https://docs.bfl.ml/flux_2/flux2_klein_training

> "With open weights available under Apache 2.0 (4B) and FLUX Non-Commercial License (9B), you can create custom models tailored to your specific needs."

> "FLUX.2 \[klein] Base models are ideal for fine-tuning due to their undistilled architecture, which preserves the full training signal."

> "**For klein 4B Base Training** — GPU: NVIDIA with 12GB VRAM (RTX 3060 12GB, RTX 4060 Ti 16GB) — RAM: 32GB system memory
> **For klein 9B Base Training** — GPU: NVIDIA with 22GB VRAM (RTX 3090, RTX 4090) — RAM: 64GB system memory"

> "**Learning Rate** — LoRA Training: 8e-5 to 1e-4 / Full Fine-tuning: 1e-5 to 5e-5 — Lower rates for style, higher for characters"

> "**Training Steps** — Style LoRAs: 1500-2500 steps / Character LoRAs: 1500-3000 steps"

> "**Resolution** — Start with 512px for faster iterations / Use 1024px or higher for final training / Use higher resolution if you want to capture macro details"

> "**Caption Writing** — Use descriptive, detailed captions / Include your trigger word consistently: `[trigger]` / Describe everything visible except the style/concept you want to teach the model"

> "**Community Tools** — AI-Toolkit (All-in-one training suite with GUI and CLI. Optimized for consumer GPUs with 12GB+ VRAM.) / Diffusers (Official Hugging Face library with DreamBooth and LoRA training examples for FLUX.2.)"

> "**ComfyUI** — 1. Place `.safetensors` file in `ComfyUI/models/loras/` 2. Add "Load LoRA" node to your workflow 3. Connect it to your FLUX Klein model 4. Use trigger word in prompts"

---

## 2. BFL — FLUX.2 [klein] Style Training (ejemplo) (200)

URL: https://docs.bfl.ml/flux_2/flux2_klein_training_example

> "Optimal dataset size: 20-40 images / Below 20 images: Insufficient variation for generalization / Above 40 images: Style dilution through excessive variation"
> "This example uses: 27 training images with corresponding caption files."

> "**Step Count by Dataset Size** — Style LoRAs (10-20 images): 1200-1800 steps / Character LoRAs (10-15 images): 800-1200 steps / Medium datasets (20-40 images): 1200-2000 steps / Large datasets (50+ images): 2000-3000 steps"

> "**VRAM Optimization** — Enable `quantize: true` for 8-bit quantization / Reduce resolution to 512x512 / Use `gradient_accumulation_steps: 2` for effective batch size of 2"

> "**Network Dimensions: 4:2:2:1 Ratio** — linear: 128 / linear_alpha: 64 / conv: 64 / conv_alpha: 32 — The larger network (approximately 500MB per model) captures low-frequency details including subtle textures, color relationships, and tonal variations."

> "**Timestep Bias: `shift`** Encourages overfitting of low-frequency information. Textures and colors adopt more rudimentary characteristics, producing unpolished, sketch-like qualities."

> "**Learning Rate: `0.000095`** Decreased from default value. Preserves broken, gestural linework from training data rather than applying smoothing."

> "**Weight Decay: `0.00015`** Increased from default value. Simplifies shapes and colors, reducing compositional complexity and emphasizing bolder, cleaner forms."

> "The 1500-step checkpoint produced optimal results."

> "**Inference Steps: 8** Significantly reduced from typical ranges (20 to 50 steps). Aligns with reduced training duration to preserve soft, painterly, impressionistic qualities."

> "**Adaptation Guidelines** — Photo-realistic styles: Training steps: 7000 / Weight decay: 0.00001 / Sampling steps: 20 to 30 — Graphic/vector styles: Network dimensions: 64:32:32:16 / Dataset size: 15 to 20 images"

Config YAML por defecto (extracto):

```yaml
job: "extension"
config:
  name: "my_first_lora_v1"
  process:
    - type: "diffusion_trainer"
      training_folder: "/app/ai-toolkit/output"
      device: "cuda"
      trigger_word: "TRIGGER WORD HERE"
      network:
        type: "lora"
        linear: 32
        linear_alpha: 32
        conv: 16
        conv_alpha: 16
      save:
        dtype: "bf16"
        save_every: 250
      datasets:
        - folder_path: "/path/to/images/folder"
          caption_ext: "txt"
          resolution: [512, 768, 1024]
      train:
        batch_size: 1
        steps: 3000
        lr: 0.0001
        optimizer: "adamw8bit"
        timestep_type: "weighted"
        content_or_style: "balanced"
      model:
        name_or_path: "black-forest-labs/FLUX.2-klein-base-9B"
        quantize: true
```

Config del ejemplo "Graphic_Impressions" (9B): `linear 128 / linear_alpha 64 / conv 64 / conv_alpha 32`, `save_every 150`, `max_step_saves_to_keep 20`, `resolution [256,512,768,1024,1280,1536]`, `steps 3000`, `lr 0.000095`, `timestep_type: "shift"`, `weight_decay 0.00015`, `model.name_or_path: "black-forest-labs/FLUX.2-klein-base-9B"`, `quantize: true`, `low_vram: false`, `trigger_word: "GFX_IMPR5N"`.

Caption de ejemplo (verbatim):

> "GFX_IMPR5N. Close Up Three Quarter Left of a scorpion standing on a rounded rock surface. The scorpion's body angles from the lower left toward the upper right, with both pincers extended forward and the segmented tail arched upward over the back ending in a stinger..."
> **Omitted descriptors:** Solid black background, red highlight, painterly brushstrokes

---

## 3. BFL — FLUX.2 LoRA Inference (200, via indice)

URL: https://docs.bfl.ml/flux_2/flux2_lora_inference

> "Train a LoRA once with the tools of your choice (AI-Toolkit, Diffusers, …), upload it to the BFL Dashboard — where they're surfaced as Finetunes — then serve inference through a managed endpoint."
> "In the **Dashboard** (https://dashboard.bfl.ai/), go to **Customization → Finetunes** and click **+ Add Finetune**. Pick the matching base model, give it a name (lowercase letters, digits, hyphens, and underscores only), optionally set a trigger phrase, and drop in the checkpoint."
> Endpoints: `/v1/flux-2-klein-4b-finetuned`, `/v1/flux-2-klein-9b-finetuned`, `/v1/flux-2-klein-9b-kv-finetuned`, `/v1/flux-2-klein-9b-kv-bf16-finetuned`, `/v1/flux-2-klein-base-4b-finetuned`, `/v1/flux-2-klein-base-9b-finetuned`. "FP8 is the default precision."

---

## 4. HF Blog — "Fine-tune FLUX.2 [klein] with a LoRA under 60 minutes" (200)

URL: https://huggingface.co/blog/black-forest-labs/flux-2-klein-lora — publicado 4-jun-2026, autor Stephen Batifol

> "A LoRA run on the 4B model fits in 24 GB of VRAM, takes about an hour on an RTX 4090, and costs roughly $0.50 if you rent the GPU."

> "FLUX.2 \[klein] ships in a 4B and a 9B size, each with a distilled (4-step) and a base (50-step) variant. For LoRA training the relevant one is **base**"
> "**It fits.** ~13 GB of weights in bf16; a LoRA run lands under 24 GB, so a 4090 or an L4 is enough."
> "**It's the training target.** Distilled models are step-compressed for fast inference; you train against the base checkpoint and the adapter still loads on the distilled model afterward — it's faster and, in our testing, usually gives even better results."

> "15–40 images that share one look"
> "At least 1024 px on the long edge. One `.txt` caption per image, same filename (`img (1).png` → `img (1).txt`)."

> "**Caption the content, never the style** ... Do **not** write "pixel art", "8-bit", "retro game", or "sprite style". If you name the style in the caption, the model learns to depend on that word instead of baking the style into the weights."
> "Pick a trigger word that is **not a real word**: `SPR1TE8`, `RISO_PR1NT`, `ZK_TOON`."

> "**Watch the samples, not the loss.** ... For most style LoRAs the visual peak is around **step 750–1500**, not the final step."

> "You train on base-4B, but run inference on the distilled `FLUX.2-klein-4B` (4 steps) ... Applying the LoRA on the distilled model typically gives better results than the base model, and it's faster"

Edit LoRA:

> "**1\. The dataset is paired.** ... `ugly_kontext/reference/` inputs ... `ugly_kontext/target/` edited outputs + captions ... ai-toolkit pairs `reference/<id>` with `target/<id>` by filename stem"
> "**2\. The caption is an instruction, not a description.** ... `change the photo the cat into an ugly sketch of the same cat` ... No made-up trigger word here."
> "**3\. One line in the config.** Add `control_path:` next to `folder_path:`"
```yaml
datasets:
  - folder_path:  "/workspace/datasets/ugly_kontext/target"     # outputs + captions
    control_path: "/workspace/datasets/ugly_kontext/reference"  # inputs <- makes it an edit LoRA
    caption_ext: "txt"
    resolution: [512]
```
> "Everything else — `arch: "flux2_klein_4b"`, the 128/64/64/32 network, `lr: 1e-4`, `flowmatch`, the base-4B target — is identical to the style config. Edit LoRAs also tend to peak between 1000 and 1750 steps"
> "(klein wants `width` and `height` divisible by 16 with `(W·H)/256 ≤ 4096`; 1024×1024 is safe.)"
> "The dataset was only cats, dogs, and animal groups, but the transformation generalizes ... give it a building and it still applies the same "redraw as a sketch" edit"
> "**The hard part of an edit LoRA is the data, not the training.**"

RunPod: `https://console.runpod.io/deploy?template=0fqzfjy6f3`; video UI: `https://youtu.be/HBNeS-F6Zz8`.

---

## 5. Diffusers — README_flux2.md (200)

URL: https://raw.githubusercontent.com/huggingface/diffusers/main/examples/dreambooth/README_flux2.md

> "**FLUX 2 [klein]**: Available in 4B and 9B parameter variants, using Qwen VL as the text encoder. Much more memory efficient and suitable for consumer hardware."

> "**Remote text encoder is only supported for FLUX.2 [dev]**. FLUX 2 [klein] models use the Qwen VL text encoder and do not support remote text encoding."

> "**Target Modules** ... `--lora_layers="attn.to_k,attn.to_q,attn.to_v,attn.to_out.0,attn.to_qkv_mlp_proj"`"
> "**single DiT blocks**: to target the ith single transformer block, add the prefix `single_transformer_blocks.i`, e.g. - `single_transformer_blocks.i.attn.to_k` — **MMDiT blocks**: ... `transformer_blocks.i.attn.to_k`"
> "**In FLUX2, the q, k, and v projections are fused into a single linear layer named attn.to_qkv_mlp_proj within the single transformer block. Also, the attention output is just attn.to_out, not attn.to_out.0 — it's no longer a ModuleList like in transformer block.**"

> "**LoRA Rank and Alpha** — `--rank`: Defines the dimension of the trainable LoRA matrices. `--lora_alpha`: A scaling factor for the LoRA's output. The LoRA update is scaled by lora_alpha / lora_rank."
> "**A common starting point is to set `lora_alpha` equal to `rank`.**"

> "**FP8 training** with `torchao`: enable FP8 training by passing `--do_fp8_training`. **Since we are utilizing FP8 tensor cores we need CUDA GPUs with compute capability at least 8.9 or greater.**"

> "**QLoRA: Low Precision Training with Quantization** ... `--bnb_quantization_config_path` to enable 4-bit NF4 quantization."

> "**Aspect Ratio Bucketing** ... `--aspect_ratio_buckets="672,1568;688,1504;720,1456;752,1392;800,1328;832,1248;880,1184;944,1104;1024,1024;1104,944;1184,880;1248,832;1328,800;1392,752;1456,720;1504,688;1568,672"`"

> "**Training Image-to-Image** ... you need a dataset containing triplets: Condition image / Target image / Instruction"

---

## 6. black-forest-labs/flux2 (200)

URL: https://github.com/black-forest-labs/flux2

> "**Official inference repo for FLUX.2 models**" (descripcion del repo)
> "This repo contains minimal inference code to run image generation & editing with our FLUX.2 open-weight models."
> "You can start an interactive session to do both text to image generation as well as editing (one or multiple) images with the following command: `PYTHONPATH=src python scripts/cli.py`"

Tabla de licencias del README:

| Model | Step-distilled | Guidance-distilled | T2I | Edit 1 ref | Edit multi-ref | License |
|---|---|---|---|---|---|---|
| FLUX.2 [klein] 4B | Yes | Yes | Yes | Yes | Yes | apache-2.0 |
| FLUX.2 [klein] 9B | Yes | Yes | Yes | Yes | Yes | FLUX Non-Commercial |
| FLUX.2 [klein] 9B KV | Yes | Yes | Yes | Yes | Yes | FLUX Non-Commercial |
| FLUX.2 [klein] 4B Base | No | No | Yes | Yes | Yes | apache-2.0 |
| FLUX.2 [klein] 9B Base | No | No | Yes | Yes | Yes | FLUX Non-Commercial |
| FLUX.2 [dev] | No | Yes | Yes | Yes | Yes | FLUX Non-Commercial |

> "**Which Model Should I Use?** — Fine-tuning, LoRA training → \[klein\] Base or FLUX.2 \[dev\]"
> "**Distilled vs Base:** Use **Distilled** (4-step) for production apps and real-time generation / Use **Base** (50-step) for fine-tuning, LoRA training, and maximum flexibility"
> "**Licensing:** 4B models are Apache 2.0. 9B models use the FLUX.2-dev Non-Commercial License"
> "The FLUX.2 autoencoder ... is released under Apache 2.0"

---

## 7. ai-toolkit README (200)

URL: https://raw.githubusercontent.com/ostris/ai-toolkit/main/README.md

Modelos soportados (extracto): `black-forest-labs/FLUX.1-dev`, `black-forest-labs/FLUX.2-dev`, `black-forest-labs/FLUX.2-klein-base-4B`, `black-forest-labs/FLUX.2-klein-base-9B`, `black-forest-labs/flux-3-image-klein-base`, ...

> "### Manual installation — Requirements: python >=3.10 (3.12 recommended) / Nvidia GPU with enough ram to do what you need / python venv / git"
> "pip3 install --no-cache-dir torch==2.13.0 torchvision==0.28.0 torchaudio==2.11.0 --index-url https://download.pytorch.org/whl/cu130"

> "**Training Specific Layers** ... you can use the `only_if_contains` network kwargs ... The naming conventions of the layers are in diffusers format"

> "**Dataset Preparation** ... The text files should be named the same as the images but with a `.txt` extension ... You can add the word `[trigger]` in the caption file and if you have `trigger_word` in your config, it will be automatically replaced. ... Images are never upscaled but they are downscaled and placed in buckets for batching."

> "**Training in Runpod** — I maintain an official Runpod Pod template here: `https://console.runpod.io/deploy?template=0fqzfjy6f3`"

`config/examples/` (API GitHub, 200): **no** existe `train_lora_flux2_klein_4b.yaml` (404). Hay `train_lora_flux_24gb.yaml`, `train_lora_flux_kontext_24gb.yaml`, `train_lora_flex2_24gb.yaml`, `train_lora_qwen_image_24gb.yaml`, etc. El esquema vigente (`job`/`config`/`process`) es el que usa el ejemplo oficial de BFL.

---

## 8. SimpleTuner — FLUX.2 Quickstart (200)

URL: https://raw.githubusercontent.com/bghira/SimpleTuner/main/documentation/quickstart/FLUX2.md

| Variant | Transformer | Text Encoder | Total Blocks | Default |
|---|---|---|---|---|
| dev | 12B params | Mistral-3 (24B) | 56 (8+48) | |
| klein-9b | 9B params | Qwen3 (bundled) | 32 (8+24) | yes |
| klein-4b | 4B params | Qwen3 (bundled) | 25 (5+20) | |

> "**klein models**: Use Qwen3 text encoder bundled in the model repo, **no guidance embeddings** (guidance training options are ignored)"

> "| klein-4b | ~12GB | ~8GB | 32GB+ | / | klein-9b | ~22GB | ~14GB | 64GB+ |"
> "**Recommended for klein-9b**: Single 24GB GPU (RTX 3090/4090, A5000) / **Recommended for klein-4b**: Single 16GB GPU (RTX 4080, A4000)"

> "**Embedding Dimension**: 15,360 for dev (3×5,120), 12,288 for klein-9b (3×4,096), 7,680 for klein-4b (3×2,560)"

> "**LoRA Targets** — `all` (default): All attention and MLP layers / `attention`: Only attention layers (qkv, proj) / `mlp`: Only MLP/feed-forward layers / `tiny`: Minimal training (just qkv layers)"

> "**Optional edit / reference conditioning** ... choose a `conditioning_type` ... `conditioning_type=reference_strict` when you need crops aligned 1:1 with the edit image. `reference_loose` allows mismatched aspect ratios."

> "Training with `flux_guidance_value=1.0` works well for most use cases / At inference, use normal guidance values (3.0-5.0)"

---

## 9. ComfyUI — Docs FLUX.2 Klein (200)

URL: https://docs.comfy.org/tutorials/flux/flux-2-klein

> "Two 4B types: Base (undistilled) for maximum flexibility and fine-tuning; Distilled (4-step) for speed-first deployments"
> "Performance: distilled \~1.2s (5090) · 8.4GB VRAM; base \~17s (5090) · 9.2GB VRAM"
> "Editing support: style transforms, semantic edits, object replacement/removal, multi-reference composition, iterative edits"

Descargas listadas: `qwen_3_4b.safetensors`, `flux-2-klein-base-4b-fp8.safetensors`, `flux-2-klein-4b-fp8.safetensors`, `flux2-vae.safetensors`; para 9B: `flux-2-klein-base-9b-fp8.safetensors`, `flux-2-klein-9b-fp8.safetensors`, `qwen_3_8b_fp8mixed.safetensors` (8.07 GB), `flux2-vae.safetensors`.

> "[NOTE] For diffusion models, please visit BFL's repo, accept the agreement, and then download the models."

Templates 9B: `image_flux2_text_to_image_9b.json`, `image_flux2_klein_image_edit_9b_base.json`, `image_flux2_klein_image_edit_9b_distilled.json`.

---

## 10. Comfy-Org/workflow_templates — Text to Image 9B (200, JSON leido)

URL: https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image_9b.json

MarkdownNote del propio template (verbatim):

> "## Model Links
> - [Hugging Face:Comfy-Org/flux2-klein-9B](https://huggingface.co/Comfy-Org/flux2-klein-9B)
> - [ModelScope:Comfy-Org/flux2-klein-9B](https://modelscope.cn/models/Comfy-Org/flux2-klein-9B)
> **diffusion_models**
> - [flux-2-klein-base-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9b-fp8/resolve/main/flux-2-klein-base-9b-fp8.safetensors)
> - [flux-2-klein-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8/resolve/main/flux-2-klein-9b-fp8.safetensors)
> **text_encoders**
> - [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) (8.07 GB)
> **vae**
> - [full_encoder_small_decoder.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors) (238 MB)"

Valores por defecto leidos del JSON (subgraph "Text to Image (FLUX.2 Klein 9B)"):
- `KSamplerSelect.widgets_values = ["euler"]`
- `Flux2Scheduler.widgets_values = [20, 1024, 1024]`
- `CFGGuider.widgets_values = [5]`
- `EmptyFlux2LatentImage.widgets_values = [1024, 1024, 1]`
- `UNETLoader.widgets_values = ["flux-2-klein-base-9b-fp8.safetensors", "default"]`
- `CLIPLoader.widgets_values = ["qwen_3_8b_fp8mixed.safetensors", "flux2", "default"]`
- `VAELoader.widgets_values = ["full_encoder_small_decoder.safetensors"]`
- `CLIPTextEncode` (Negative Prompt).widgets_values = [""]
- Nodos: `RandomNoise`, `SamplerCustomAdvanced`, `VAEDecode`, `SaveImage`, `PrimitiveInt` (Width/Height).

---

## 11. Comfy-Org/workflow_templates — Image Edit 9B Base (200, JSON leido)

URL: https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base.json

Subgraph "Image Edit (FLUX.2 Klein 9B)" — nodos adicionalesrespecto del T2I:
- `ImageScaleToTotalPixels` (widgets: `lanczos`, 1, 1) — nodo 80
- `GetImageSize` — nodo 100
- `VAEEncode` — nodo 123 (pixels <- ImageScaleToTotalPixels, vae <- VAELoader)
- `ReferenceLatent` — nodos 122 (conditioning negativo) y 124 (conditioning positivo), ambos con `latent` <- VAEEncode
- `EmptyFlux2LatentImage` — nodo 66, con width/height <- GetImageSize
- `Flux2Scheduler` — nodo 62, con width/height <- GetImageSize
- `CFGGuider` — nodo 63, positive <- ReferenceLatent(124), negative <- ReferenceLatent(122)
- Subgrafo de multi-referencia: id `65c22b29-59aa-496b-89c6-55a603658670`, con inputs `reference_image1` / `reference_image2` (dos `LoadImage`)

Prompt de ejemplo del template: *"Change the camera angle to a first-person driver's perspective looking through the steering wheel at the dashboard and windshield, maintaining the same white minimalist interior style and lighting"*.

Segundo grupo (multi-ref): *"Apply the yellow "C" logo to the center hub of the steering wheel, and change the steering wheel color to royal blue matching the logo background, while maintaining the same interior style, lighting, camera angle, and all other elements unchanged"*.

---

## 12. Codigo local de ComfyUI (commit b08e6cf3) — extractos

`comfy/model_detection.py:235-250`:

```python
if any_suffix_in(state_dict_keys, key_prefix, 'double_blocks.0.img_attn.norm.key_norm.', ["weight", "scale"]) and (...):
    dit_config = {}
    if '{}double_stream_modulation_img.lin.weight'.format(key_prefix) in state_dict_keys:
        dit_config["image_model"] = "flux2"
        dit_config["axes_dim"] = [32, 32, 32, 32]
        dit_config["num_heads"] = 48
        dit_config["mlp_ratio"] = 3.0
        dit_config["theta"] = 2000
        dit_config["out_channels"] = 128
        dit_config["global_modulation"] = True
        dit_config["mlp_silu_act"] = True
        dit_config["qkv_bias"] = False
        dit_config["ops_bias"] = False
        dit_config["default_ref_method"] = "index"
        dit_config["ref_index_scale"] = 10.0
        dit_config["txt_ids_dims"] = [3]
        patch_size = 1
```

`comfy/ldm/flux/model.py:41-42`:
```python
default_ref_method: str = "offset"
ref_index_scale: float = 1.0
```
`comfy/ldm/flux/model.py:365-369`:
```python
ref_latents_method = kwargs.get("ref_latents_method", self.params.default_ref_method)
...
    index += self.params.ref_index_scale
```

`comfy/model_base.py:1033-1042`:
```python
ref_latents = kwargs.get("reference_latents", None)
if ref_latents is not None:
    latents = []
    for lat in ref_latents:
        latents.append(self.process_latent_in(lat))
    out['ref_latents'] = comfy.conds.CONDList(latents)
    ref_latents_method = kwargs.get("reference_latents_method", None)
    if ref_latents_method is not None:
        out['ref_latents_method'] = comfy.conds.CONDConstant(ref_latents_method)
```

`comfy/text_encoders/flux.py:181-184`:
```python
class Qwen3Tokenizer8B(sd1_clip.SDTokenizer):
    def __init__(self, embedding_directory=None, tokenizer_data={}):
        tokenizer_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "qwen25_tokenizer")
        super().__init__(tokenizer_path, pad_with_end=False, embedding_directory=embedding_directory,
                         embedding_size=4096, embedding_key='qwen3_8b', tokenizer_class=Qwen2Tokenizer, ...)
```
`comfy/text_encoders/flux.py:194`:
```python
self.llama_template = "user\n{}\nassistant\n<think>\n\n</think>\n\n"
```
`comfy/text_encoders/flux.py:213-215`:
```python
class Qwen3_8BModel(sd1_clip.SDClipModel):
    def __init__(self, device="cpu", layer=[9, 18, 27], ...):
```

`comfy/sd.py:1715-1718`:
```python
elif clip_type in (CLIPType.FLUX, CLIPType.FLUX2):  # Flux2 Klein reuses the Qwen3-VL LM (3-layer tap -> 12288); visual unused.
    klein_model_type = "qwen3_8b" if te_model == TEModel.QWEN3VL_8B else "qwen3_4b"
```

`comfy_extras/nodes_flux.py:37-57`:
```python
class EmptyFlux2LatentImage(io.ComfyNode):
    node_id="EmptyFlux2LatentImage"
    ...
    io.Int.Input("width", default=1024, ...), io.Int.Input("height", default=1024, ...), io.Int.Input("batch_size", default=1, ...)
    latent = torch.zeros([batch_size, 128, height // 16, width // 16], ...)
```

`comfy_extras/nodes_flux.py:105-123` (PREFERRED_KONTEXT_RESOLUTIONS): 672x1568, 688x1504, 720x1456, 752x1392, 800x1328, 832x1248, 880x1184, 944x1104, 1024x1024, 1104x944, 1184x880, 1248x832, 1328x800, 1392x752, 1456x720, 1504x688, 1568x672.

`comfy_extras/nodes_flux.py:153-181`:
```python
class FluxKontextMultiReferenceLatentMethod(io.ComfyNode):
    display_name="Edit Model Reference Method"
    io.Combo.Input("reference_latents_method", options=["offset", "index", "uxo/uno", "index_timestep_zero"], advanced=True)
    is_experimental=True
```

`comfy_extras/nodes_flux.py:213-233`:
```python
class Flux2Scheduler(io.ComfyNode):
    io.Int.Input("steps", default=20, min=1, max=4096), io.Int.Input("width", default=1024, ...), io.Int.Input("height", default=1024, ...)
    seq_len = (width * height / (16 * 16))
    sigmas = get_schedule(steps, round(seq_len))
```

`comfy_extras/nodes_flux.py:264-301`:
```python
class FluxKVCache(io.ComfyNode):
    display_name="Flux KV Cache"
    description="Enables KV Cache optimization for reference images on Flux family models."
    is_experimental=True
    ...
    m.add_object_patch("diffusion_model.params.default_ref_method", "index_timestep_zero")
```

`comfy/model_management.py:109-121`:
```python
directml_enabled = False
if args.directml is not None:
    logging.warning("WARNING: torch-directml barely works, is very slow, has not been updated in over 1 year and might be removed soon, please don't use it, there are better options.")
    import torch_directml
    directml_enabled = True
    ...
    lowvram_available = False #TODO: need to find a way to get free memory in directml before this can be enabled by default.
```

`comfy/cli_args.py:144`:
```python
vram_group.add_argument("--lowvram", action="store_true", help="Doesn't do anything if dynamic vram is enabled. If dynamic vram isn't being used this option makes the text encoders run on the CPU.")
```

`comfy/cli_args.py:148-153`:
```python
parser.add_argument("--reserve-vram", type=float, default=None, ...)
parser.add_argument("--vram-headroom", type=float, default=0, ...)
parser.add_argument("--disable-dynamic-vram", action="store_true", help="Disable dynamic VRAM and use estimate based model loading.")
```

---

## 13. HF API — inventarios y tamaños (200)

| Repo | Dato |
|---|---|
| `black-forest-labs/FLUX.2-klein-9b-fp8` | `gated: "auto"`, `license_name: flux-non-commercial-license`, `flux-2-klein-9b-fp8.safetensors` = **9.433.061.528 bytes** |
| `black-forest-labs/FLUX.2-klein-base-9B` | `gated: "auto"`, `safetensors.parameters.BF16 = 9.078.581.248`, contiene `flux-2-klein-base-9b.safetensors`, `transformer/`, `text_encoder/` (4 shards), `vae/`, `tokenizer/` |
| `Comfy-Org/vae-text-encorder-for-flux-klein-9B` | `qwen_3_8b.safetensors` 16.381.517.176 / `qwen_3_8b_fp4mixed.safetensors` 6.802.593.327 / `qwen_3_8b_fp8mixed.safetensors` 8.664.848.742 / `split_files/vae/flux2-vae.safetensors`; `license_name: flux-non-commercial-license` |
| `black-forest-labs/FLUX.2-small-decoder` | `license: apache-2.0`; `full_encoder_small_decoder.safetensors`, `small_decoder.safetensors`, `diffusion_pytorch_model.safetensors` (62.373.347 params F32) |
| `unsloth/FLUX.2-klein-9B-GGUF` | `license_name: flux-non-commercial-license`; `gguf.total` 9.078.581.248; `totalFileSize` 18.157.197.600; 18 quants Q2_K -> BF16 |
| `ponpoke/flux2-klein-9b-uncensored-text-encoder` | `gated: "auto"` ("Safety Warning & Terms of Access"), `license_name: flux-non-commercial-v2.1`; `model.safetensors` F16 8.190.735.360 params; GGUF f16/q4_k_m/q6_k/q8_0 |

---

## 14. Archademy (200) — https://archademy.ai/es/

> "Tendrás acceso completo a nuestro programa de formación en IA: seis módulos ... siete módulos" (la pagina alterna "seis"/"siete"; el listado real es de 7)

> "**El profesor del curso: Thomas Nelissen**"

> "### Módulo 3 — De imagen a imagen
> Una vez que tengas una primera idea, así es como la perfeccionas: ampliando la imagen para conseguir una mayor resolución y utilizando **el flujo de trabajo** característico del curso, **«Rhino-to-Image»**, que convierte un modelo básico de volumetría 3D en un render fotorrealista aplicando una referencia de material real, al tiempo que se bloquea la geometría exactamente en su sitio. También se trata la edición precisa con IA (eliminar o añadir elementos, retocar zonas concretas) y la fusión de varias imágenes."

> "### Módulo 7 — El flujo de trabajo de Gaudí
> El módulo final y más emblemático del curso: un método en dos pasos —desarrollado junto con el arquitecto Cas Esbach— que, en primer lugar, reinterpreta la geometría de tu modelo 3D a través de la lógica estructural de Gaudí y, a continuación, aplica materiales fotorrealistas sobre él. El resultado no es una copia de su estética, sino un edificio moldeado por el mismo razonamiento que él utilizó hace más de un siglo."

> "### Módulo 6 — Mesa redonda: Gaudí y el papel del arquitecto en la era de la IA
> Un grupo de expertos —el historiador especializado en Gaudí Jos Tomlow (co-reconstructor del modelo colgante original de Gaudí), Gijs Rikken, de MVRDV; el diseñador computacional Arturo Tedeschi; y el formador Thomas Nielsen— debaten junto con el experto en IA Cas Esbach..."

> "Conversión de texto a imagen y edición de imágenes con IA / Vídeo generado por IA para una presentación arquitectónica / Reconstrucción en 3D a partir de imágenes generadas por IA / **Acceso exclusivo a un modelo de IA entrenado con los archivos de la Fundació Antoni Gaudí**"

> "**¿Por qué ComfyUI?** ... Te da **control total** sobre cada paso: bloquea la geometría y solo cambia el estilo. Sin detalles inventados. Sin formas que cambien de una versión a otra."

> "### El Gaudí Nexus
> El Gaudí Nexus te pide que diseñes la respuesta: un **«Mercado de Proximidad» y un «Centro de Cultura Digital»**, junto con una reconfiguración completa de la plaza que lo rodea. ... Este proyecto no pretende, precisamente, imitar las formas de Gaudí. Se trata de aplicar su **lógica constructiva** ..."

Jurado (bios): **Thomas Nelissen** — "arquitecto junior en **Davis AI**, en París ... Antes de unirse a Davis, dirigió la integración de la IA en **JDS Architects**, en París, creando flujos de trabajo a medida y entrenando sus propios modelos para apoyar el trabajo del estudio en concursos internacionales. Thomas ha impartido clases sobre IA generativa a estudiantes de arquitectura en la Universidad de las Artes ArtEZ, y su investigación sobre los flujos de trabajo de diseño asistidos por IA se ha publicado en Archined." — **Cas Esbach** — "Profesor en la SCAD ... más de seis años como arquitecto y jefe de proyecto en MVRDV ... ha trabajado tanto en BIG en Nueva York, en Derksen|Windt en Delft y en Civic Projects en Chicago ... fundador de KANS, un estudio de diseño creado en 2025." — Gijs Rikken (MVRDV) — Bibiana Sciortino (Fundació) — Joseph Tomlow — Ishan Pal Singh — Jasmy Chen.

Calendario y premios: $175/$295/$345 por equipo (max 4 personas, un pago) · entrega **16 de diciembre (23:59 GMT-7)** · resultados 4 de febrero · premios 6.000/2.000/1.000 + 1.000 (Premio de Diseño Fundació) + 10 menciones + 50 finalistas · FAQ: "**¿Qué tengo que presentar?** Una lámina en formato A1 en línea con tu proyecto (máx. 15 MB, JPEG). También hay una lámina opcional en formato A4 si quieres optar al Premio de Diseño de la Fundació Antoni Gaudí".

Briefings: `https://archademy.ai/wp-content/uploads/2026/08/GxAI_BRIEFING_ES.pdf` · `https://archademy.ai/wp-content/uploads/2026/09/GxAI_BRIEFING_EN.pdf` · `https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_ES.pdf`.

---

## 15. Fundació Antoni Gaudí — concurso (200)

URL: https://fundacionantoniogaudi.org/concurso-de-arquitectura-y-diseno-ai-x-gaudi/

> "Para guiar las exploraciones formales y espaciales con la lógica constructiva y estructural de Gaudí, los participantes dispondrán de **un modelo de IA exclusivo, entrenado con el material documental específico**, y la formación para aprender a dominar ese entorno paramétrico basado en nodos."
> "Fecha límite para el envío de las propuestas: 16/12/2026"
> "Adicionalmente se otorgará un premio independiente al mejor diseño de mobiliario u objeto arquitectónico inspirado en los métodos de Gaudí."

URL: https://en.fundacionantoniogaudi.org/ai-x-gaudi-architecture-and-design-competition/ (200) — "Deadline for submission of proposals: 2026/12/16".

---

## 16. Civitai API — busqueda "gaudi lora" (200)

URL: https://civitai.com/api/v1/models?query=gaudi%20lora&limit=10

Resultados (NINGUNO es el LoRA del curso):
- `JJ's Gaudi Archi` (jjhuang) — SDXL 1.0 (`JJsGaudiArchi_XL.safetensors`, trigger "Gaudi Archi") + SD 1.5 (`JJsGaudiArchi.safetensors`)
- `antonio gaudi-facade` (ArchiZHS_YQBen) — SD 1.5, `antonio gaudi-facade 10.safetensors`, trigger "antonio gaudi"
- `antonio gaudi-detial` (ArchiZHS_YQBen) — SD 1.5, trigger "antonio gaudi"
- `designed by Antoni Gaudi [SDXL] 305` (TangBohu) — SDXL, `tbh305-sdxl.safetensors`, trigger "designed by Antoni Gaudi"
- `designed by Antoni Gaudi [FLUX] 305` (TangBohu) — **Flux.1 D**, `designed_by_Antoni_Gaudi_FLUX_305.safetensors`
- `designed by Antoni Gaudi 305` (TangBohu) — SD 1.5

**Conclusion: no existe ficha publica del LoRA de la Fundacio ni del instructor.**

---

## 17. ControlNet FLUX.2 (200)

URL: https://huggingface.co/alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union/raw/main/README.md

> "FLUX.2-dev-Fun-Controlnet-Union.safetensors | ControlNet weights for Flux2. The model supports multiple control conditions such as Canny, HED, Depth, Pose and MLSD. This ControlNet is added on 4 double blocks."
> "FLUX.2-dev-Fun-Controlnet-Union-2602.safetensors | Compared to the previous version of the model, we have added Scribble and Gray controls. Similar to Z-Image-Turbo, the Flux2 model loses its CFG distillation capability after Control training, which is why the previous version performed poorly. Building upon the previous version, we trained on a better dataset and performed CFG distillation after training, resulting in superior performance."
> "You can adjust controlnet_conditioning_scale for stronger control and better detail preservation."
> Tamaño: 8.23 GB. Licencia: `flux-dev-non-commercial-license`.

URL: https://github.com/bryanmcguire/comfyui-flux2fun-controlnet (200) — nodo `Load Flux2 Fun ControlNet`; requisitos: ComfyUI con soporte Flux, **FLUX.2-dev** base model, `flux2-vae.safetensors`, Python 3.10+, PyTorch 2.0+; licencia Apache-2.0.

URL: https://github.com/ReyChiaro/flux.2-klein-controlnet — repo existente con `flux2/controlnet_flux2klein.py` (291 lineas); **README.md no disponible (404)** -> soporte/pesos **no verificados**.

---

## 18. Rhino — ViewCaptureToFile (200)

URL: https://docs.mcneel.com/rhino/8/help/en-us/commands/viewcapturetofile.htm

> "The ViewCaptureToFile command saves an image of the current view to a file. ViewCaptureToFile saves the contents of the view with a specified width and height, disregarding the current viewport size. Viewport borders, cursor images, and other decorations are not saved."
> "Choose the location, file type, and name for the bitmap file. BMP, JPG, PNG and TIFF formats are supported."
> "The image saved is automatically given a name with the current date, time, and a custom prefix. Use the Autoname option in the -scriptable command, -ViewCaptureToFile, to customize the prefix."

---

## 19. ArchiGen AI — metodo de 3 pasadas desde Rhino (200)

URL: https://archigenai.com/comfyui-rhino-architects-workflow-2026.html (18-may-2026)

> "We export three image passes from Rhino, all from the same camera, at 2048 pixels on the long side, with the model in shaded display mode and the linework turned off.
> **Pass 1. The depth map** — Rhino's built-in display mode for depth is workable but not ideal. We use the free Lands Design display mode or a custom display mode with edges hidden, color set to a black-to-white linear ramp by Z distance from camera, and no shadows. ... This is the file that goes into the ControlNet Depth node in ComfyUI. If this pass is wrong, nothing else can recover it.
> **Pass 2. The line drawing**
> **Pass 3. The flat shaded view** — This is the pass that most Reddit workflows skip, and it is the pass that fixes the 'all my buildings look like the same building' problem."
> "IP-Adapter (Flat Shaded reference). Weight 0.4. Material guidance, soft enough that the model still has room to add weathering and atmosphere."
> "Steps 28, CFG 4.5, sampler dpmpp_2m, scheduler karras."

Advertencia: la pieza declara que "Nora Sinclair, Vista Studios" es "ArchiGen's AI editorial persona, not a human architect or practitioner". Tomar como referencia tecnica, no como fuente primaria.

---

## 20. denkaTa599 — Advanced Flux Arch Workflow (200)

URL: https://github.com/denkaTa599/comfyui-architectural-workflow

> "Goal: The purpose of this workflow is to transform a basic, low-resolution 3D viewport render into a high-quality, photorealistic architectural masterpiece. It uses advanced multi-conditioning techniques to dictate materials, mood, and precise geometry."
> "1. The Multi-LoRA Stack ... 1. Canny Edge ControlNet (strength: 0.75) ... 2. Depth Anything V2 ControlNet (strength: 0.60) ... 3. 3-Stage Generation & Upscaling"
> "2. Provide your base 3D image. 3. Provide three specific reference images (Main Material, Mood/Lighting, Secondary Material)."
> "System Requirements: GPU: NVIDIA RTX 5080 (or equivalent with 16GB VRAM) / RAM: 64GB DDR5"
> Archivo: `Advanced_Flux_Arch_Workflow.json` (11.532 bytes). Usa **FLUX.1 (dev)**, no FLUX.2.

---

## 21. RunPod — precios (200 via indice; pagina oficial "Updated October 8, 2026")

URL: https://www.runpod.io/pricing · https://www.runpod.io/gpu-models/rtx-4090

- RTX 3090 24 GB — Community **$0,22/h** · Secure $0,46/h (schema JSON-LD de la pagina)
- RTX 3090 (pod, 24 GB / 125 GB RAM / 16 vCPU) — $0,50/h
- RTX 4090 24 GB — Community **$0,34/h** · Secure **$0,74/h** ("Rent NVIDIA RTX 4090 GPUs from $0.74/hr. Community Cloud $0.34/hr Secure Cloud $0.74/hr")
- RTX A5000 24 GB — $0,27/h (pod)
- A40 48 GB — Community $0,44/h · Secure $0,49/h
- L40S 48 GB — Community $0,79/h · Secure $1,09/h
- H100 SXM 80 GB — Community $1,99/h · Secure $2,89-$3,49/h
- Serverless (L4 / A5000 / 3090 / MIG 24 GB) — $1,10/h
- RTX 6000 Ada — $0,99/h; RTX 4000 Ada — $0,28/h; RTX Pro 6000 — $1,69/h community / $1,99/h secure

---

## 22. YouTube — verificaciones oEmbed (HTTP 200 = video existe y es embebible)

| URL | Respuesta oEmbed |
|---|---|
| https://www.youtube.com/watch?v=IApOVLuPeqU | `{"title":"AI Rendering with ComfyUI","author_name":"Parametric","author_url":"https://www.youtube.com/@parametriconline"}` |
| https://www.youtube.com/watch?v=demZCRuImQ0 | `{"title":"Flux2 Klein 9B Just Nailed Inpainting | ComfyUI Tutorial","author_name":"AxiomGraph","author_url":"https://www.youtube.com/@AxiomGraph"}` |
| https://www.youtube.com/watch?v=elm00WQ03vw | `{"title":"3D to Final Image 2026 AI Workflow","author_name":"Arch Viz Artist","author_url":"https://www.youtube.com/@ArchVizArtist"}` |
| https://www.youtube.com/watch?v=RAMs89SS6cM | `{"title":"ComfyUI for Architects: Generate Renders in Minutes (Not Hours)","author_name":"architutors","author_url":"https://www.youtube.com/@architutors"}` |
| https://www.youtube.com/watch?v=Y8N6kjJBXqg | `{"title":"ComfyUI Tutorial | Turn Any Image into a 3D Model in Seconds","author_name":"architutors",...}` |
| https://www.youtube.com/watch?v=HBNeS-F6Zz8 | `{"title":"How to Use AI Toolkit on Runpod","author_name":"Ostris AI","author_url":"https://www.youtube.com/@ostrisai"}` |
| https://www.youtube.com/watch?v=u-lQWqsDWSM | `{"title":"Crea Imágenes Gratis con Flux 1 y Comfyui en una RTX 3070 8gb VRAM","author_name":"Comarca IA",...}` |
| https://www.youtube.com/watch?v=7u9r6t3m2aA | **HTTP 401** (2 intentos) -> **no verificado** |

Descripciones relevantes (via indice de busqueda):

- `IApOVLuPeqU`: "In this tutorial, we will go through a complete AI rendering workflow using ComfyUI to stylize architectural images from Rhino ... We'll cover: -How to prepare Rhino viewcaptures for AI input -Setting up ComfyUI and accessing the shared workflow via provided URLs -Using ControlNet to preserve edge fidelity and architectural structure -Applying IP Adapter for style transfer and visual enhancement -Adjusting prompts, resolution, and conditioning strength for optimal results -Exporting and compiling your final renderings" — premiered Oct 1, 2025.
- `demZCRuImQ0` (18-01-2026): capitulos "Workflow / Add Object / Multi Round Editing / Remove Objects / Edit Text / Multi Reference Editing / Change Cloth"; usa LanPaint (github.com/scraed/LanPaint).
- `elm00WQ03vw`: "we show our full AI + ArchViz workflow, from clay render to final Photoshop polish, including Flux Klein".
- `7u9r6t3m2aA` (30-01-2026): lista `https://huggingface.co/Comfy-Org/vae-text-encorder-for-flux-klein-4b/tree/main/split_files/diffusion_models` y `.../flux2-dev/tree/main/split_files/vae`; "PNG is the workflow!!!".

---

## 23. Fuentes marcadas como NO VERIFICADAS / 404

| URL | Status | Motivo |
|---|---|---|
| https://raw.githubusercontent.com/ReyChiaro/flux.2-klein-controlnet/main/README.md | 404 | El repo existe pero no tiene README en `main` |
| https://raw.githubusercontent.com/ostris/ai-toolkit/main/config/examples/train_lora_flux2_klein_4b.yaml | 404 | Ese archivo no existe en `config/examples/` |
| https://www.youtube.com/oembed?url=...v=7u9r6t3m2aA | 401 | Video no embebible / ID dudoso |
| https://www.youtube.com/watch?v=TWSFej_S_bY | sin fetch | Solo visto en resultados de busqueda |
| "Ismail Seleit" / "Studio Ismail Seleit" / "ex-Foster+Partners" | sin resultados | No aparece en ninguna fuente publica consultada |
| `Cordux/flux2-klein-4b-uncensored-text-encoder` | sin fetch | Reportado por el usuario; no verificado |
| `city96/FLUX.2-klein-9B-GGUF` | sin resultados | No existe repo de pesos de city96 para klein 9B (el nodo es suyo; los pesos son de unsloth) |
| Texto plano de `GxAI_BRIEFING_ES.pdf` | no extraido | PDF 200 (20 pag.) pero requiere OCR/parseo |
