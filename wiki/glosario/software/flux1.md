---
tipo: software
software: flux1
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [glosario, software, flux1, imagen-ia, comfyui, pollinations, arquitectura]
---

# FLUX.1

Familia base 12B rectified flow transformer de Black Forest Labs: schnell veloz Apache 2.0 para exploración, dev con calidad plena para detalle, pro vía API para producción, kontext para edición por instrucción.

- [[#Descripción]]
- [[#schnell]]
- [[#dev]]
- [[#pro]]
- [[#kontext]]
- [[#Uso en vault]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Descripción

12B params, salida competitiva frente a alternativas cerradas. Schnell genera en 1–4 pasos vía latent adversarial diffusion distillation. Licencia schnell Apache 2.0 (uso personal, científico y comercial). Ecosistema: 283 adapters, 76 finetunes, Diffusers + ComfyUI de día cero. Generación siguiente: FLUX.2 y FLUX 3 (ver [[wiki/glosario/software/modelos-imagen-arquitectura|modelos-imagen-arquitectura]] y [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]).

## schnell

Motor gratis de exploración del estudio vía [[wiki/glosario/software/pollinations|Pollinations]] (`alias flux`, 0.002 Pollen).

### Qué hace

Texto a imagen veloz para abrir abanico de variantes.

### Sintaxis / Cómo se usa

```text
GET https://gen.pollinations.ai/image/{prompt-url}?model=black-forest-labs/flux.1-schnell&width=1280&height=720&seed=7&nologo=true
```

```python
from diffusers import FluxPipeline
import torch
pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()
image = pipe("A cat holding a sign that says hello world", guidance_scale=0.0, num_inference_steps=4, max_sequence_length=256).images[0]
```

### Ejemplo

Prompt cáscara concurso probado 2026-11-03 seed 7, 293 KB, favorito de Sol para masa:

```text
distant wide-angle view across plaza toward Sagrada Familia Barcelona, lightweight inverted catenary concrete shell pavilion with glass roof, thin white shell parametric ribbed structure, open stone plaza, trees, people for scale, Eixample facades background, warm dusk light, photorealistic architectural photography, ultra detailed
```

### Uso en vault

- `proyectos/concurso-gaudi-nexus/` vistas rápidas + tanda T1/T2/T10.
- `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux-2026-11-03.jpg`.

---

## dev

Variante abierta con calidad plena, 12B, para detalle donde schnell queda corto.

### Qué hace

Texto a imagen con adherencia fina, ideal lámina.

### Sintaxis / Cómo se usa

```python
from diffusers import FluxPipeline
pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
```

### Ejemplo

Mismo prompt cáscara a 1024px, 20–28 pasos, cfg medio.

### Uso en vault

- Alternativa local cuando el pod corre la familia completa.
- Referencia de calidad frente a schnell en eval A/B.

---

## pro

Versión API de máxima adherencia, vía proveedores (`bfl.ml`, `replicate.com`, `fal.ai`).

### Qué hace

Producción con prompt following pleno y texto legible.

### Sintaxis / Cómo se usa

```text
GET https://gen.pollinations.ai/image/{prompt-url}?model=black-forest-labs/flux.1.1-pro&width=1280&height=704&seed=7&nologo=true
```

Resolución en múltiplos de 32 (usar 1280x704).

### Ejemplo

Cáscara onda continua 2026-11-03, 8 s, 185 KB: `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux11pro-2026-11-03.jpg`.

### Uso en vault

- Tanda T3 (3 finalistas lámina).

---

## kontext

Edición por instrucción sobre la familia 1.x (`alias kontext`, 0.03 Pollen).

### Qué hace

Conserva fachada y torres, agrega cáscara + vidrio en primer plano.

### Sintaxis / Cómo se usa

```text
POST https://gen.pollinations.ai/v1/images/edits
Form-Data: image=@plaza.jpg, prompt="conserva fachada y torres, agrega cáscara invertida de hormigón + vidrio", model=black-forest-labs/flux.1-kontext-pro
```

### Ejemplo

Tanda T8 con 1–3 fotos reales de plaza.

### Uso en vault

- n8n: `Telegram Trigger Download Images=ON` → `HTTP POST Form-Data Binary` → `Send Photo`.

---

## Uso en vault

- Exploración: schnell vía [[wiki/glosario/software/pollinations|Pollinations]] + [[wiki/glosario/software/n8n|n8n]] + [[wiki/glosario/software/telegram|Telegram]].
- Lámina: pro / 1.1-pro.
- Espec rival y licencias: [[wiki/glosario/software/modelos-imagen-arquitectura|modelos-imagen-arquitectura]].

## Conceptos relacionados

- [[wiki/glosario/referentes/black-forest-labs|black-forest-labs]]
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]
- [[wiki/glosario/software/comfyui|comfyui]]
- [[wiki/glosario/software/pollinations|pollinations]]
- [[wiki/glosario/software/modelos-imagen-arquitectura|modelos-imagen-arquitectura]]

## Referencias

- [FLUX.1-schnell — Hugging Face oficial](https://huggingface.co/black-forest-labs/FLUX.1-schnell) (verificado 2026-11-03 — 200, Apache 2.0, 12B, 1–4 pasos)
- [Black Forest Labs — web oficial](https://blackforestlabs.ai) (verificado 2026-11-03 — 200)
- [Tutorial externo ComfyUI FLUX.2 Dev](https://docs.comfy.org/tutorials/flux/flux-2-dev) (verificado 2026-11-03 — 200, workflows + pesos)
