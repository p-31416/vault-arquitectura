---
tipo: proyecto
mvp: 04.02
wf: WF-04-serie-txt2img
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [mvp_04.02, comfyui, txt2img, lora, serie, metodo-cientifico]
estado: activo
---

# WF-04 — Serie txt2img (texto → imagen, + LoRA de estilo)

> Punta a punta desde texto: flujo base con cada modelo, luego el MISMO flujo + LoRA de estilo (el LoRA suma estilo, no reemplaza al modelo). Método científico: cada corrida registra config completa en §5; versiones con esquema familia.mayor.menor.

- [[#1. Ficha]]
- [[#2. Modelos]]
- [[#3. Grafo base 1.0.0 (nodo por nodo)]] — [[#CheckpointLoaderSimple (nodo 1)]] · [[#CLIPTextEncode + / − (nodos 2 y 3)]] · [[#EmptyLatentImage (nodo 4)]] · [[#KSampler (nodo 5) — el motor]] · [[#VAEDecode (nodo 6)]] · [[#SaveImage (nodo 7) + LoraLoader (1.1.x)]]
- [[#4. Prompts]]
- [[#5. Corridas]]
- [[#6. Evaluación]]
- [[#7. Backlog del WF]]
- [[#8. Referencias]]
- [[#9. Log de cambios]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Comparar modelos txt2img para arquitectura y medir qué agrega cada LoRA de estilo sobre el mismo flujo |
| Input | Solo prompt (sin imagen) |
| Output esperado | Serie comparable `salidas/n_04-*.png`, mismo seed 42 salvo 1.0.1 |
| Esquema de versiones | `1.0.x` = mismo flujo, cambio mínimo (seed/prompt) · `1.1.x` = +LoRA (1.1.0 markers, 1.1.1 sketch, 1.1.2 stack) · `2.0.0` = migración SDXL |
| Hardware | RX 570 8GB DirectML, batch 1 |

### Variantes de un vistazo (qué diferencia a cada una)

| Versión | Diferencia | Config | Imagen |
|---|---|---|---|
| `1.0.0` | Baseline foto, seed fija | Realmix, euler 30, cfg 7, seed 42, 768×512 | ![1.0.0](salidas/n_04-1.0.0.png) |
| `1.0.1a/b/c` | Solo cambia la seed (randomize) | seeds 884353843642081 / 740846423981 / 258854604970378 | ![1.0.1a](salidas/n_04-1.0.1a.png) |
| `1.1.0 → 1.1.0c` | +LoRA markers, ladder 0.6/0.8/1.0 | markers, `marker painting, handsketch`, seed 42 | ![1.1.0c](salidas/n_04-1.1.0c.png) |
| `1.1.1 → 1.1.1c` | +LoRA sketch, ladder 0.5/0.8/1.0 | archisketch, `linear`, seed 42 | ![1.1.1c](salidas/n_04-1.1.1c.png) |
| `1.1.2` | Stack markers + sketch | ambos en serie, seed 42 | _(pendiente)_ |
| `2.0.0` | Migración SDXL | Juggernaut, dpmpp_2m/karras 35, cfg 4, 1216×832 | _(pendiente)_ |

Leyenda: `1.0.x` mismo flujo (solo seed/prompt) · `1.1.x` suma LoRA (último dígito = ladder) · `2.0.0` cambia de modelo. Detalle corrida por corrida en §5.

## 2. Modelos (lo que hay en esta PC)

Ruta: `P:\00-repos\ComfyUI\models\`. Verificados visibles por el servidor el 2026-10-14.

| Archivo                                             | Tipo / base                                | Tamaño  | Usado en     | Rol                                               |
| --------------------------------------------------- | ------------------------------------------ | ------- | ------------ | ------------------------------------------------- |
| `architecturerealmix_v11.safetensors`               | Checkpoint SD1.5                           | 1.99 GB | 1.0.x, 1.1.x | Base fotorrealista arquitectura, iteración rápida |
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | Checkpoint SDXL                            | 6.62 GB | 2.0.0        | Entrega, fotorrealismo máximo, ~9 min/imagen      |
| `sd-v1-5-inpainting-fp16.safetensors`               | Checkpoint inpainting SD1.5                | 1.99 GB | WF-06        | Edición localizada (no se usa en esta serie)      |
| `markerhandsketch-V1.safetensors`                   | LoRA SD1.5 (`marker painting, handsketch`) | 9.1 MB  | 1.1.0, 1.1.2 | Estilo croquis marker (Civitai 34384)             |
| `archisketch-v1.safetensors`                        | LoRA SD1.5 (`linear`)                      | 18.1 MB | 1.1.1, 1.1.2 | Estilo línea (Civitai 32757)                      |
| `control_v11p_sd15_canny.safetensors`               | ControlNet                                 | 689 MB  | (WF-03/08)   | Bordes exactos                                    |
| `control_v11f1p_sd15_depth_fp16.safetensors`        | ControlNet fp16                            | 689 MB  | (WF-03/08)   | Volumetría                                        |
| `control_v11p_sd15_scribble.safetensors`            | ControlNet                                 | ~1.4 GB | (WF-03)      | Croquis suelto                                    |
| `RealESRGAN_x4plus.pth`                             | Upscaler                                   | 63.9 MB | (cierre/F8)  | x4 fiel tiled                                     |

Uso por versión: 1.0.x Realmix · 1.1.0 +markers · 1.1.1 +sketch · 1.1.2 ambos · 2.0.0 Juggernaut (`--lowvram --cpu-vae`).

## 3. Grafo base 1.0.0 (nodo por nodo)

`workflow_1.0.0_txt2img_base.json` (7 nodos, formato API). En el canvas: el cable del prompt **positivo entra en verde**, el del **negativo en rojo** al KSampler.

### CheckpointLoaderSimple (nodo 1)

Carga el "cerebro": de él salen MODEL (la UNet que dibuja), CLIP (el traductor texto→vectores) y VAE (el revelador). Cambiar `ckpt_name` = cambiar de artista: Realmix (rápido, arquitectónico) vs Juggernaut (lento, fotorrealista). Todo lo demás del flujo puede quedar igual.

### CLIPTextEncode + / − (nodos 2 y 3)

Traducen texto a condicionamiento. El + describe lo que sí (verde al sampler), el − lo prohibido (rojo al sampler). Qué afecta: vocabulario concreto y fotográfico (`hormigon, ventanales, tilt-shift`) > adjetivos vagos; cada palabra suma o resta peso. Los *triggers* de LoRA van solo en el +.

### EmptyLatentImage (nodo 4)

El lienzo vacío en latente: define proporción y tamaño. SD1.5 nació en 512, así que proporciones derivadas rinden mejor:

| Uso | Resolución | Nota |
|---|---|---|
| Concepto rápido | 512×512 | Mínimo VRAM |
| Fachada apaisada | 768×512 | Default de la serie |
| Retrato/interior | 512×768 | Vertical |
| SDXL entrega | 1216×832 / 832×1216 | Solo 2.0.0 con `--lowvram` |

Más píxeles = más tiempo y VRAM lineal. Nunca mandar tamaños impredecibles (regla R1).

### KSampler (nodo 5) — el motor

Recibe MODEL + condicionamientos + latente y quita ruido por pasos. Qué afecta cada parámetro:

| Parámetro | Qué hace | Rango útil acá |
|---|---|---|
| `seed` | Ruido inicial. **Misma seed = misma imagen** (doc oficial). Ciencia: fija para comparar; exploración: cambiarla | 42 serie · 43 en 1.0.1 |
| `control_after_generate` | Qué hace con la seed tras cada Queue: `fixed` repite, `increment`/`randomize` varían | `fixed` en serie · `randomize` para explorar |
| `steps` | Pasos de refinado. Más = más detalle hasta un techo (~30-40 en SD1.5), siempre más tiempo | 30 (35 en SDXL) |
| `cfg` | Obediencia al prompt. Bajo (3-5) = libre/realista, alto (7-12) = literal pero puede quemar colores | 7 (4 en SDXL) |
| `sampler_name` | Algoritmo de muestreo (euler, dpmpp_2m...). Cambia textura/velocidad, no la composición | euler (dpmpp_2m en SDXL) |
| `scheduler` | Cómo reparte los pasos (normal, karras...). Karras concentra detalle fino al final | normal (karras en SDXL) |
| `denoise` | Cuánto ruido parte: 1.0 = inventa todo (txt2img siempre 1.0); <1 solo tiene sentido con imagen de entrada (WF-05) | 1.0 |

### VAEDecode (nodo 6)

Revela el latente a píxeles visibles usando el VAE del checkpoint. No tiene parámetros: si la imagen sale con colores raros o bordes lavados, el sospechoso es el VAE (o el cfg alto), no este nodo.

### SaveImage (nodo 7) + LoraLoader (1.1.x)

`SaveImage` guarda con prefijo (`WF04-1.0.0` → `WF04-1.0.0_00001_.png`); el PNG guarda prompt + workflow incrustado (arrastrarlo al canvas recupera el flujo). `LoraLoader` (1.1.x) se inserta entre checkpoint y sampler/CLIP: `strength_model`/`strength_clip` 0-1 regulan cuánto tiñe el estilo (0.5-0.6 sutil, 1.0 dominante); varios se encadenan en serie.

1.1.x agregan `LoraLoader` entre 1 y 5/2/3 (modelo y clip del LoRA). 2.0.0 cambia 1/4/5 según §2.

## 4. Prompts

**Base (+, en español):** `estilo architecturerealmix, casa moderna de hormigon, ventanales grandes, fachada minimalista, rodeada de arboles, luz natural suave, fotorrealista, fotografia de arquitectura, 8k`
**Base (−, en español):** `borroso, baja calidad, deformado, marca de agua, texto, firma, caricatura, ilustracion`
> Nota: los *triggers* de LoRA (`marker painting, handsketch, linear`) quedan en inglés porque son palabras exactas entrenadas del modelo.
**1.1.0 (+):** `marker painting, handsketch, modern concrete house, minimalist facade, large windows, architectural sketch`
**1.1.1 (+):** `linear, grey, white background, simple background, modern concrete house, minimalist facade, architectural sketch`
**1.1.2 (+):** `marker painting, handsketch, linear, modern concrete house, minimalist facade, grey, white background, architectural sketch`
**2.0.0 (+):** `photorealistic, raw photo, 8k uhd, masterpiece, modern concrete and glass house, minimalist facade, integrated landscape, golden hour lighting, architectural photography, 24mm tilt-shift`

## 5. Corridas

> Más nuevo → más arriba. Miniatura + config completa (método científico).

| Fecha         | Versión | Seed | Cambio       | Archivo                                                                         | Vista                            | Tiempo     | Calidad                                                              | Nota                                                         |
| ------------- | ------- | ---- | ------------ | ------------------------------------------------------------------------------- | -------------------------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------ |
| 2026-10-14    | 1.0.0   | 42   | baseline     | `salidas/n_04-1.0.0.png` (origen `WF04-1.0.0_00001_.png`, prompt_id `c172c2af`) | ![1.0.0](salidas/n_04-1.0.0.png) | 173s       | ✅ casa moderna vidriada + árboles, luz día coherente, sin artefactos | Input de WF-05/06. Más lento que est. (~90s) — DirectML puro |
| 2026-10-14 | 1.0.1c | 258854604970378 (randomize) | seed libre, prompt inglés | `salidas/n_04-1.0.1c.png` (origen `WF04-1.0.0_00004_.png`, prompt_id `3e29f346`) | ![1.0.1c](salidas/n_04-1.0.1c.png) | 135s | ✅ dos volúmenes + pileta, dusk parejo | Tercera casa distinta: randomize confirmado |
| 2026-10-14 | 1.0.1b | 740846423981 (randomize) | seed libre, prompt inglés | `salidas/n_04-1.0.1b.png` (origen `WF04-1.0.0_00003_.png`, prompt_id `856895ac`) | ![1.0.1b](salidas/n_04-1.0.1b.png) | 136s | ✅ casa vidriada en L + jardín, diurno nublado | Segunda variante, misma calidad |
| 2026-10-14 | 1.0.1a | 884353843642081 (randomize) | seed libre, prompt inglés | `salidas/n_04-1.0.1a.png` (origen `WF04-1.0.0_00002_.png`, prompt_id `66ff2804`) | ![1.0.1a](salidas/n_04-1.0.1a.png) | 198s | ✅ casa patio con pileta, marcos negros, volumetría coherente | Primera corrida SOL en canvas; prompt inglés (previo al pase a español) |
| 2026-10-14 | 1.1.0c | 42 | ladder strength 1.0/1.0 + `on white paper` + `photo` en negativo | `salidas/n_04-1.1.0c.png` (origen `WF04-1.1.0c_00001_.png`, prompt_id `a5d26fab`) | ![1.1.0c](salidas/n_04-1.1.0c.png) | 149s | ✅ estilo marker total: tinta, aguadas, papel blanco, volumetría intacta | Sweet spot del LoRA ≈ 1.0 con prompt de papel |
| 2026-10-14 | 1.1.0b | 42 | ladder strength 0.8/0.8 + `on white paper` + `photo` en negativo | `salidas/n_04-1.1.0b.png` (origen `WF04-1.1.0b_00001_.png`, prompt_id `289cb94b`) | ![1.1.0b](salidas/n_04-1.1.0b.png) | 150s | ✅ híbrido: base foto + trazo a mano en bordes/vegetación, fondo lavado | Transición 0.6→1.0 documentada |
| 2026-10-14 | 1.1.1c | 42 | ladder strength 1.0 (2ª del prefijo b) | `salidas/n_04-1.1.1c.png` (origen `WF04-1.1.1b_00002_.png`, prompt_id `76c52338`) | ![1.1.1c](salidas/n_04-1.1.1c.png) | 164s | ✅ croquis de línea puro sobre blanco, misma volumetría | A 1.0 pierde el poco sombreado de 0.8 |
| 2026-10-14 | 1.1.1b | 42 | ladder strength 0.8 | `salidas/n_04-1.1.1b.png` (origen `WF04-1.1.1b_00001_.png`, prompt_id `c0ee70af`) | ![1.1.1b](salidas/n_04-1.1.1b.png) | 148s | ✅ línea arquitectónica con sombreado leve, fondo blanco | El sketch responde a 0.8 (el markers pedía 1.0): sweet spot 0.8-1.0 |
| 2026-10-14 | 1.1.1 | 42 | +sketch 0.5/0.5, trigger `linear` + fondo simple | `salidas/n_04-1.1.1.png` (origen `WF04-1.1.1_00001_.png`, prompt_id `84c1a55f`) | ![1.1.1](salidas/n_04-1.1.1.png) | 151s | ⚠️ monocromo lavado, sigue foto sin línea: base del ladder | Motivó 1.1.1b/c |
| _(pendiente)_ | 1.1.2   | 42   | stack        | `salidas/n_04-1.1.2.png`                                                        | —                                |            |                                                                      |                                                              |
| _(pendiente)_ | 2.0.0   | 42   | SDXL         | `salidas/n_04-2.0.0.png`                                                        | —                                | ~560s est. |                                                                      | Solo si hay ventana de tiempo                                |

## 6. Evaluación

DoD de la serie: 1.0.0 con volumetría coherente y material legible · 1.1.x preservan composición cambiando solo estilo · 1.1.2 sin barro de triggers · 2.0.0 salto visible de fotorrealismo. Escala /35 de MVP_04 por imagen.

## 7. Backlog del WF

- [ ] Correr 1.0.0 + 1.0.1 (par baseline)
- [ ] Correr 1.1.0/1.1.1/1.1.2 con mismo seed + tabla comparativa estilo
- [ ] Strength-ladder markers (0.4/0.6/0.8) si 1.1.0 no convence (método ref. pixelized-art: 0.66/0.78/1/1.15)
- [ ] 2.0.0 SDXL en ventana larga
- [ ] Evaluaciones /35 con inspección visual
- [ ] Agente foto/cine: asistente que opere ComfyUI con conocimiento de fotografía y cine (tipos de plano, focales, encuadres, luz, composición) para control preciso del punto de vista + prompts optimizados para arquitectura en ComfyUI (lente 24mm tilt-shift, golden hour, regola dei terzi...). Insumo: este §3 + `pbk-comfyui` prompt-packs
- [ ] Entrenar LoRA propio de estilo por referente (ej. SANAA, Koolhaas/OMA): receta — 1) dataset 20-60 imágenes por referente (obra publicada + croquis propios; solo investigación interna por derechos), 2) caption cada imagen con trigger único (`estiloSANAA`, `estiloOMA`) + descripción de materialidad/luz, 3) entrenar con kohya sd-scripts o ai-toolkit (rank 16-32, 1500-3000 steps, base SD1.5) en RunPod RTX 3090 (~$1-2, la RX 570 no entrena), 4) validar con matriz misma-seed vs LoRAs de esta serie, 5) si el estilo prende, versionar como 1.2.x de esta serie

## 8. Referencias

- Oficial txt2img (default workflow, principios de prompt SD1.5): https://docs.comfy.org/tutorials/basic/text-to-image (verificado 200)
- Primera generación (carga de modelo, metadata en PNG): https://docs.comfy.org/get_started/first_generation (verificado 200)
- Tutorial LoRA oficial (strengths, encadenado en serie): https://docs.comfy.org/tutorials/basic/lora (verificado 200 vía @sherlock)
- Sketch→interior render SD1.5 + Lineart + upscale (ref. arquitectura externa): https://github.com/bankaino/comfyui-sketch-to-interior-render
- Combo archviz Canny 0.9-1.0 + Depth 0.7-0.8 + MLSD 0.4-0.6: https://comfyui-wiki.com/en/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui
- Strength-ladder método (0.66/0.78/1/1.15): https://civitai.com/models/550585 (pixelized-art v3)
- LoRA estilo ejemplo (trigger + strength 1): https://civitai.com/models/1083797/art-deco-noveau-style-sd15

## 9. Log de cambios

> Más nuevo → más arriba. Cada cambio en JSON/prompts/params deja una entrada.

| Fecha | Versión | Cambio | Motivo |
|---|---|---|---|
| 2026-10-14 | 1.1.0b/c | Ladder markers 0.8 y 1.0 (misma seed 42, +`on white paper`, +`photo` en negativo): 150/149s → `n_04-1.1.0b/c.png` | 0.6 no movía el estilo; 0.8 híbrido; 1.0 marker total. Sweet spot ≈ 1.0 |
| 2026-10-14 | 1.0.1a/b/c | 3 corridas SOL en canvas (seeds randomize, prompt inglés): 198/136/135s → `n_04-1.0.1a/b/c.png` | Reproducibilidad por seed + randomize funcional; seeds extraídas del PNG |
| 2026-10-14 | doc | §2 inventario local de modelos · §3 expandido nodo por nodo (colores verde/rojo, glosario KSampler con seed/control_after_generate, proporciones de lienzo) · backlog suma agente foto/cine · índice con sub-wikilinks | Pedido SOL: documento único completo estilo A-WF-estadio |
| 2026-10-14 | — | WF creado: 6 JSON (1.0.0/1.0.1/1.1.0/1.1.1/1.1.2/2.0.0) + este md único (ficha, modelos, grafo, prompts, corridas, evaluación, backlog, referencias) | Serie txt2img con método científico; reemplaza esquema multi-archivo de A-WF-estadio |
