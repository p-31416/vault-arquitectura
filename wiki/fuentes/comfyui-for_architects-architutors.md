---
tipo: fuente
fecha_creacion: 2026-10-09
ultima_actualizacion: 2026-10-09
video_id: RAMs89SS6cM
url: https://www.youtube.com/watch?v=RAMs89SS6cM
idioma: en
fecha_ingesta: 2026-10-09
tags: [comfyui, arq, viz, ia-imagen, flux, flux-kontext, workflow-img2img, mvp_04]
crudo: raw/yt/transcripts/2026-10-09_RAMs89SS6cM.en.md
quien_guardo: sol
estado: en-wiki
---

# ComfyUI for Architects — architutors

> Fuente curada de referencia para el estudio: tutorial img2img con Flux1 + Flux Kontext en ComfyUI Cloud que transforma imagen base de SketchUp en render realista. Incluye valor para [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP 04 ComfyUI arquitectura]] como receta croquis→render adaptable a flujo local.

## Resumen

- Construye desde cero un workflow img2img en la versión cloud gratuita de ComfyUI para crear renders realistas de proyectos de arquitectura desde una imagen base.
- Usa como base una imagen de modelo 3D exportada de SketchUp, cargada con Load Image y normalizada con Image Resize by Longer Side a 2000 píxeles.
- El grafo combina preparación de imagen + VAE + modelo de difusión Flux1 + LoRA + muestreo KSampler con condicionamiento DualCLIP / CLIP Text Encode / Reference Latent / Conditioning Zero Out / Flux Guidance + decodificación VAE Decode hacia Save Image.
- El control de fidelidad a la referencia vive en Flux Kontext Image Scale: valores altos conservan la geometría base, valores bajos abren interpretación estilística.
- El cierre invita a iterar con prompts de texturas, materiales, iluminación y vibra (Scandinavian minimalism, Industrial chic, Tropical resort) con reuso del mismo workflow cambiando imagen y prompt.

## Ficha bibliográfica

```yaml
autor: [architutors]
titulo: "ComfyUI for Architects"
tipo: video
fecha_fuente: no consta en transcript # ingesta: 2026-10-09; duracion aportada por SOL: 10:22
editorial_medio: "YouTube"
origen_binario: https://www.youtube.com/watch?v=RAMs89SS6cM
crudo: raw/yt/transcripts/2026-10-09_RAMs89SS6cM.en.md
quien_guardo: sol
estado: en-wiki
temas: [comfyui, img2img, viz-arq, flux, flux-kontext, render-arq, sketchup, prompt-arq, mvp_04]
```

Video: https://www.youtube.com/watch?v=RAMs89SS6cM
Crudo verbatim: `raw/yt/transcripts/2026-10-09_RAMs89SS6cM.en.md` (+ gemelos `.txt` / `.srt`)
Duración: 10:22 — Idioma: en

## Índice del tutorial

1. [00:00:00] Intro — uso de la versión cloud gratuita de ComfyUI para renders realistas + mención de tutorial previo con Qwen.
2. [00:00:27] Load Image — doble clic, escribir Load Image, arrastrar al canvas.
3. [00:00:38] Subida de base — imagen de modelo 3D exportada de SketchUp, importar como punto de partida.
4. [00:00:56] Image Resize by Longer Side — definición de dimensiones en píxeles, valor aplicado 2000.
5. [00:01:16] Flux Kontext Image Scale — grado de respeto a la imagen de referencia: valores altos conservan geometría, valores bajos liberan estilo.
6. [00:01:32] VAE Encode — compresión de la imagen hacia latent space.
7. [00:01:37] Load VAE — traductor entre píxeles y latent space, salida conectada a VAE Encode.
8. [00:02:28] Load Diffusion Model + Load LoRA — incorporación del modelo Flux1 y LoRA como condimento de estilo.
9. [00:03:27] KSampler — cocción de ruido latente aleatorio hacia imagen refinada, con entradas de modelo y latente.
10. [00:03:47] DualClipLoader + [00:04:03] CLIP Text Encode + [00:04:15] Reference Latent + Conditioning Zero Out + [00:04:20] Flux Guidance — condicionamiento enriquecido conectado con KSampler.
11. [00:05:22] VAE Decode + [00:05:45] Save Image — decodificación con salida de KSampler y modelo VAE hacia imagen final.
12. [00:06:15] Prompt + [00:07:25] Run — texturas, materiales, iluminación y vibra, ejecución con render en segundos en cloud.
13. [00:08:25] Iteración — variación de prompts y valores con exploración de estilos.
14. [00:09:28] Cierre — un tipo de workflow ComfyUI para renders de arquitectura e interiorismo.

## Glosario del video

- Load Image — nodo de entrada de imagen base.
- Image Resize by Longer Side — normalización por lado mayor, 2000 px en la demo cloud.
- Flux Kontext Image Scale — regulador de fidelidad a la referencia.
- VAE Encode — compresión píxel → latente.
- Load VAE — traductor píxel ↔ latente.
- Load Diffusion Model — pesos de generación, familia Flux1 en este workflow.
- Load LoRA — adaptador de matiz estilístico.
- Flux1 — checkpoint de difusión aplicado.
- KSampler — motor de muestreo desde ruido latente.
- DualClipLoader — carga pareada de modelos CLIP para condicionamiento enriquecido.
- CLIP Text Encode — entrada de prompt textual.
- Reference Latent — guía desde latente de referencia.
- Conditioning Zero Out — anulación de condicionamiento de prompt.
- Flux Guidance — guía que mantiene el workflow en rumbo.
- VAE Decode — decodificación latente → píxel.
- Save Image — cofre de salida del render final.
- Qwen — modelo del tutorial hermano mencionado en la intro.
- SketchUp — origen de la imagen base 3D.
- ComfyUI cloud version — entorno gratuito usado en la demo.

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP 04 ComfyUI arquitectura]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas workflows ComfyUI]]
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|Modelos recomendados]]

## Referencias

| # | Fuente | URL | Nota |
|---|---|---|---|
| 1 | Video architutors (esta ficha) | https://www.youtube.com/watch?v=RAMs89SS6cM | primaria, duración 10:22 |
| 2 | Comfy Org oficial | https://comfy.org | oficial |
| 3 | ComfyUI GitHub oficial | https://github.com/Comfy-Org/ComfyUI | oficial |
| 4 | Modelo Flux.1-dev HuggingFace | https://huggingface.co/black-forest-labs/FLUX.1-dev | oficial, familia Flux 12B |
| 5 | Docs ComfyUI Flux.2 Klein | https://docs.comfy.org/tutorials/flux/flux-2-klein | oficial |

> Material de terceros (architutors), de uso interno del estudio.
