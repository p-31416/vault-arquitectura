---
tipo: research
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [research, sherlock, lora, sketch, croquis, sdxl, sd15, kohya, ai-toolkit, onetrainer, civitai]
idioma: es
---

# 2026-11-03 — Entrenar un LoRA de croquis propios (línea C)

> Fecha|Fuentes N|Confianza
> 2026-11-03|9 verificadas 200 + 4 sketch de apoyo|Alta (kohya/ai-toolkit/OneTrainer/Civitai oficial) / Media (guías comunitarias de estilo) / Alta (recomendación SD1.5 para RX 570)

## Resumen

Entrenar un LoRA de línea propia con pocas imágenes avanza con dataset chico bien curado (15–40 imágenes para estilo, 10–30 para personaje), caption que describe contenido sin nombrar el estilo, trigger inventado, regularización ligera y 500–2000 pasos con rank 16–32. Para correr en RX 570 8GB DirectML la base aprobada es SD1.5 (512px, ~8GB+ en entrenamiento, inferencia fluida local); SDXL (1024px, 12–16GB+) rinde mejor en calidad de línea pero pide RunPod/RunComfy Cloud o Civitai on-site. Las tres vías aprobadas son kohya sd-scripts (script + control total), ostris ai-toolkit (UI + YAML + RunPod template, MIT), OneTrainer (GUI por pestañas, presets `#sdxl 1.0 LoRA`, AGPL-3.0), más Civitai Training Studio (sin GPU local, ~500 Buzz SDXL/SD1, 30 días de retención). El hallazgo que más potencia el concurso Gaudí Nexus es el edit-LoRA de FLUX.2 klein (120 pares input→sketch enseñan la transformación, no solo el estilo) como puente entre foto de maqueta y croquis.

## Ejes

### 1. Dataset chico + captioning + regularización para estilo de línea

- Cantidad: estilo 15–40 (BFL klein), estilo Illustrious ~50, personaje 10–30, sketch SD1.5 18–21 (paper few-shot). Calidad supera cantidad: fondos variados, poses variadas, sin blur/duplicados, 1024px lado largo para SDXL, 512px para SD1.5.
- Captioning: una `.txt` por imagen, mismo nombre. Para estilo: describir contenido, nunca el estilo ("caption the content, never the style"); trigger inventado no-palabra (`SPR1TE8`, `xyzsketchstyle`, `spltbear`) al inicio de cada caption. Para SD1.5 valen tags cortos booru; para SDXL/FLUX valen frases naturales.Herramientas aprobadas: WD14 Tagger / BLIP / BLIP2 (kohya, OneTrainer), auto-label de Civitai (gratis, 1200/día, tags o captions según base), ChatGPT con prompt "describe solo contenido".
- Regularización: no repetir mismo fondo, shuffle tokens/tags, buckets multirresolución (SD1.5: 384–640; SDXL: 896–1152), noise_offset 0.03–0.05 para estilos intensos, min_snr_gamma 5 (SD1.5/SDXL), EMA para datasets chicos, 10–20 checkpoints para elegir por ojo (no por loss). Overfit se reconoce cuando todo prompt deriva a una imagen de training → bajar pasos, bajar rank a 16, o elegir epoch temprana.

### 2. Qué base conviene con RX 570 8GB

- SD1.5: entrena desde ~8GB, 512px, batch 1–4, steps 400–500 efectivos para prueba, 2000–4000 para estilo final; inferencia local fluida en DirectML; LoRA de 6–144 MB; ecosistema más grande de LoRAs de sketch (pen-sketch, old-sketch, minimalist-line). Aprobada como base de iteración local.
- SDXL: 1024px nativa, mejor composición y línea fina, LoRA 86–435 MB; entrenamiento 12–16GB+ (4060 Ti 8GB ya sufre sin offload); en RX 570 solo inferencia con modelos livianos (Juggernaut v9, RealVisXL) y entrenamiento delegado a RunPod (template ai-toolkit ~$0.50/run en 4090) o Civitai Studio (~500 Buzz). Aprobada como base de calidad final.
- Decisión para el estudio: prototipar estilo en SD1.5 local (cero costo, iteración rápida), consolidar en SDXL vía cloud, y reservar FLUX.2 klein 4B (Apache-2.0, 24GB, ~1h en 4090) para edit-LoRA foto→croquis cuando haya 50–200 pares.

### 3. Vías aprobadas (3+1)

- **kohya sd-scripts** (`train_network.py` / `sdxl_train_network.py`): rank 16, `network_dim`, `network_alpha`, dataset `.toml` con repeats/resolución/buckets, `mixed_precision fp16`, `sdpa`, sample cada N steps. Máximo control, CLI, Windows/Linux, Python 3.10.
- **ostris ai-toolkit** (UI `localhost:8675` o CLI `run.py config.yml`): `trigger_word`, `network linear 16/alpha 16`, `steps 2000`, `lr 1e-4`, `quantize`, `cache_latents_to_disk`, `resolution [512,768,1024]`, `ema`, sample prompts con trigger. Template RunPod oficial + video 2 min. Soporta SDXL + SD1.5 + FLUX/Qwen/Z-Image en el mismo marco.
- **OneTrainer** (GUI): preset `#sdxl 1.0 LoRA` / `#SD1.5 LoRA`, pestañas general→model→data→concepts→training→sampling→LoRA (rank 16 SD1.5, 8–16 SDXL, alpha 1.0), multi-resolución por lista, captioning BLIP/WD14 integrado, TensorBoard, backups automáticos. Ideal para quien prefiere no tocar YAML.
- **Civitai Training Studio** (on-site, sin GPU): tipo Character/Style/Concept + base (SD1.5/SDXL/Pony/Illustrious/ZImage Turbo/Flux.1), auto-label, trigger opcional, steps con guía "each image seen ~N×" (style ~50×, character ~35×), 1–20 checkpoints, sample prompts (1 cerca de training + 1 en setting nuevo + 1 con outfit distinto), precio vivo en Buzz, reintento y `Train further`, retención 30 días. La vía clásica queda en retirada.

### 4. Evidencia sketch/arquitectura que respalda el camino

- `sketch and study drawing style SDXL` (Civitai 220411, SDXL 1.0, 86 MB, trigger `sketch simple background`, weight 0.8–1.5) demuestra merge de LoRAs con mismo dataset y distintos parámetros para línea clásica; dataset público disponible.
- `WorthyHuman1/Sketch_LoRA` (SDXL, fp16, RTX 4050 16h) documenta prompts `sketch, rough lineart, pencil drawing, unfinished illustration` y fuerza 0.6–1.0.
- `Sketch Line Qwen` (Apache-2.0, trigger `spltbear, sketch`) y `Sketch Illustrious` (trigger `sketch, pencil sketch, hand-drawn`) confirman que el trigger vive en captions/prompts de ejemplo aunque `trainedWords` esté vacío.
- `Minimalist Line Style SD1.5` (144 MB, trigger `minima2023`, weight 0.4–1.0) aporta receta de prompts simples + negativos `borders, photo, cg` para línea limpia de logos/bocetos.
- Paper few-shot (`yukaryote finetuning_sd.pdf`, 18–21 imgs, LoRA + ControlNet lineart) valida que 20 imágenes alcanzan para estilo con batch 2, lr 5e-5, 1000 epochs.

## Fuentes APA idioma original + [trad. propia]

1. kohya-ss. (2024–2026). *sd-scripts* [scripts de entrenamiento]. GitHub. https://github.com/kohya-ss/sd-scripts — idioma_original: en/ja [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Stars 7.3k, 2720 commits. Licencia: ASL 2.0 mayormente (partes MIT/BSD); costo: gratis (GPU propia).
2. kohya-ss. (s. f.). *How to use the LoRA training script train_network.py* [Cómo usar train_network.py]. GitHub Docs. https://github.com/kohya-ss/sd-scripts/blob/main/docs/train_network.md — idioma_original: en/ja [trad. propia]. Verificada vía excerpt 200. Gratis.
3. ostris. (2024–2026). *ai-toolkit: The ultimate training toolkit for finetuning diffusion models* [toolkit definitivo para fine-tuning]. GitHub. https://github.com/ostris/ai-toolkit — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Stars 12.5k, MIT; costo: gratis (GPU propia o RunPod ~$0.50/run 4090).
4. Nerogar. (2024–2026). *OneTrainer: one-stop solution for Diffusion training* [solución integral]. GitHub. https://github.com/Nerogar/OneTrainer — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Stars 3.3k, AGPL-3.0; costo: gratis.
5. Nerogar. (s. f.). *Onboarding Guide for Newcomers* [Guía de inicio]. OneTrainer Wiki. https://github.com/Nerogar/OneTrainer/wiki/Onboarding-Guide-for-Newcomers — idioma_original: en [trad. propia]. Verificada vía excerpt 200. Gratis.
6. Civitai. (2026). *Civitai's Guide to Training Studio* [Guía de Training Studio]. Civitai Education. https://education.civitai.com/civitais-guide-to-training-studio/ — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Costo: Buzz (SDXL/SD1 ~ precio base, pago Blue→Yellow/Green, reembolso si falla, retención 30 días).
7. Civitai. (s. f.). *SDXL & SD1 LoRA training* [Entrenamiento LoRA SDXL y SD1]. Civitai Developer. https://developer.civitai.com/orchestration/recipes/training-sdxl-sd1 — idioma_original: en [trad. propia]. Verificada vía excerpt 200. Costo: 500 Buzz default; base default Juggernaut XL (SDXL) / 127227 (SD1.5).
8. Black Forest Labs / Batifol, S. (2026). *Fine-tune FLUX.2 [klein] with a LoRA under 60 minutes* [Afinar FLUX.2 klein en menos de 60 min]. Hugging Face Blog. https://huggingface.co/blog/black-forest-labs/flux-2-klein-lora — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Licencia modelos Apache-2.0; costo: ~$0.50 GPU rentada / gratis con GPU 24GB propia. Clave: dataset estilo 15–40 + edit pareado 50–200 + `control_path`.
9. Poly42 / aihowto et al. (2023–2025). *Sketch LoRAs de referencia*: *sketch and study drawing style SDXL* https://civitai.com/models/220411/sketch-and-study-drawing-style · *Sketch_LoRA SDXL* https://huggingface.co/WorthyHuman1/Sketch_LoRA · *Sketch Line Qwen* https://civitai.com/models/1893683/sketch-line — idioma_original: en [trad. propia]. Verificadas vía search excerpt (Civitai/HF 200 en listado). Licencias: Civitai default / Apache-2.0 (Qwen sketch); costo: gratis (descarga) o generación con Buzz.

## Metodología queries por idioma + URLs + status + gaps

- EN: `kohya sd-scripts LoRA training guide official github` → 8 hits, fetch 200 repo + docs. `ostris ai-toolkit LoRA training guide SDXL SD1.5` → 8 hits, fetch 200 repo + RunComfy guide. `OneTrainer LoRA training guide SDXL SDXL` → 8 hits, fetch 200 repo + wiki. `Civitai on-site LoRA trainer guide` → 8 hits, fetch 200 Training Studio. `sketch architecture LoRA training small dataset style line Civitai` → 8 hits, excerpts verificados (HF/Civitai listados 200, sin fetch cuerpo por paywall login).
- ES: `entrenar LoRA croquis propios pocas imágenes` → gap: material ES escaso, se prioriza EN oficial + trad. propia.
- IT: `allenare LoRA schizzi architettura poche immagini` → `datos insuficientes IT` (gap explícito).
- Status: 5 fetch cuerpo 200 (kohya, ai-toolkit, OneTrainer, Training Studio, HF klein blog) + 4 excerpts 200 (docs train_network, wiki onboarding, developer SDXL/SD1, sketch models). 0 404.
- Recencia: todo 2024–2026 vigente; Training Studio 2026-10-26 (beta por defecto, clásica en retirada).

## Propuestas wiki esqueleto

- `lora-croquis-propio` (nueva): dataset 15–40, captioning sin estilo, trigger inventado, regularización, tabla SD1.5 vs SDXL vs klein para RX 570/RunPod.
- `kohya-sd-scripts` (§software): `train_network.py`, `.toml`, rank/alpha, sample por ojo.
- `ai-toolkit-ostris` (§software): UI+YAML, RunPod template, `control_path` para edit.
- `onetrainer` (§software): presets, pestañas, backup/TensorBoard.
- `civitai-training-studio` (§software): tipos, Buzz, epochs, `Train further`.
- `sketch-lora-referencia` (§estilo): 4 LoRAs con trigger/weight/base.

## Candidatos

- Civitai Education *LoRA Training Glossary* https://education.civitai.com/tag/lora-training — Nivel 2 candidato (vocabulario rank/alpha/steps) si SOL aprueba.
- Civitai article *Optimal Parameters for Style LoRA on Illustrious* https://civitai.com/articles/25645/optimal-parameters-for-style-lora-training-on-the-illustrious-model-civitai — Nivel 2 candidato (50 imgs, 3000 steps, Prodigy, noise_offset) para estilo arquitectónico.
- Hugging Face *FLUX.2 klein training docs* https://docs.bfl.ai/flux_2/flux2_klein_training_example — Nivel 2 candidato (YAML exacto) — esperar `s`.
- Paper *Fine-tuning ControlNet and Stable Diffusion for Few-Shot Style Transfer* https://yukaryote.github.io/assets/pdf/finetuning_sd.pdf — Nivel 1 verificado por excerpt (18–21 imgs), candidato a ficha académica.

## Dependencias vault

- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]] · [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|flux2-klein-lora]] · [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|modelos-imagen]]
