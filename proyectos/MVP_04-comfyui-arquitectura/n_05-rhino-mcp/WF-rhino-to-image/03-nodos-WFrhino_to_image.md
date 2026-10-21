---
tipo: guia
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, workflow, nodos, flux2, klein, lora, rhino]
---

# WF-rhino-to-image — configs propias del flujo

> Solo lo específico de este flujo. Los nodos genéricos están en [[wiki/glosario/software/comfyui|comfyui]].

## Estructura del grafo

```
UNETLoader ─► LoraLoaderModelOnly ─► CFGGuider ─┬─► SamplerCustomAdvanced ─► VAEDecode ─► SaveImage
                                                │        ▲
CLIPLoader(flux2) ─► CLIPTextEncode(+) ─► ReferenceLatent(geo) ─► ReferenceLatent(material)
                   │                             ▲                     ▲
                   │                        VAEEncode            VAEEncode
                   └─► CLIPTextEncode(−)    (geo_shaded)         (material.jpg)
                                                        ▲            ▲
                                          ImageScaleToTotalPixels (×2)

EmptyFlux2LatentImage ─► SamplerCustomAdvanced.latent_image
Flux2Scheduler ─► SamplerCustomAdvanced.sigmas
KSamplerSelect(euler) ─► SamplerCustomAdvanced.sampler
RandomNoise(seed) ─► SamplerCustomAdvanced.noise
```

## Por qué este orden

| Decisión | Motivo |
|----------|--------|
| `LoraLoaderModelOnly` entre `UNETLoader` y `CFGGuider` | El LoRA parchea el modelo antes de armar el guider; así laLoRA afecta también al cálculo de sigmas |
| Doble `ReferenceLatent` encadenado | `ReferenceLatent` acumula latentes de referencia (`append=True`): geometría y material conviven en el mismo conditioning |
| `FluxKontextMultiReferenceLatentMethod` con `index` | Es el método por defecto del modelo (`default_ref_method = "index"`, `ref_index_scale = 10.0`): reparte los tokens de referencia en su banda posicional |
| `Flux2Scheduler` en lugar de `BasicScheduler` | Las sigmas de FLUX.2 dependen del largo de la secuencia → el scheduler necesita `width`/`height` explícitos |
| `SamplerCustomAdvanced` (esquema nuevo) | Recibe `noise`/`guider`/`sampler`/`sigmas`/`latent_image`; `steps` y `cfg` viajan dentro del guider y de las sigmas |
| `CFGGuider.cfg = 1,0` | Klein está destilado a 4 pasos: la guía escala 1 reproduce el comportamiento de la destilación |

## Referencia de material

| Ajuste | Valor | Motivo |
|--------|-------|--------|
| `ImageScaleToTotalPixels.megapixels` (material) | 0,5 | La foto de material aporta textura, no geometría: con menos resolución el modelo la usa como guía de superficie y no como composición |
| `ImageScaleToTotalPixels.megapixels` (geometría) | 1,0 | La volumetría define el encuadre: necesita resolución completa |
| `upscale_method` | `lanczos` | Conserva líneas de Rhino sin aliasing (regla de escalado del glosario) |

## Prompt

FLUX.2 responde mejor a frases estructuradas; el curso usa un **prompt JSON** generado por su prompt de sistema.

Esqueleto oficial (copiado del tablero del curso): [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|prompt-rhino-to-image-esqueleto-json]]

```json
{"scene": "[1–2 sentences. 'A professional highly detailed realistic architecture photography of {typology}. STRICT CAMERA LOCK: Match Image 1 perspective.' Then one sentence naming the transformation: the massing of Image 1 re-skinned in the materiality of Image 2.]",
 "subjects": [{"description": "[… State massing preserved exactly from Image 1, then name the facade/material system taken directly from Image 2 … Replace pink figures with realistic pedestrians. No joint details or mm dimensions.]",
               "position": "[1 sentence. Spatial placement relative to Image 1's composition.]",
               "action": "[1 short phrase. Static quality or kinetic impression.]"}],
 "style": "[… read directly from Image 2 (no architect reference). Photography by Iwan Baan and {one other photographer}. Phase One IQ4, {lens}, {film stock}, grain/aberration notes.]",
 "color_palette": ["#______","#______","#______","#______","#______","#______"],
 "lighting": "[… taken from Image 2: time of day, diffusion, shadow character, interior glow if visible.]",
 "mood": "[2–3 adjectives, then a sentence connecting the mood to the atmosphere of Image 2.]",
 "background": "[… regionally authentic to the user's stated location. Replace green massing volumes with Piet Oudolf-style vegetation appropriate to that region.]",
 "composition": "[1–2 sentences. 'MATCH CAMERA OF IMAGE 1 EXACTLY.' Then name the perspective type and what it emphasises.]",
 "camera": {"angle": "[Short phrase matching Image 1.]", "lens": "[Lens choice only.]", "depth_of_field": "[Aperture and focus in one phrase.]"}}
```

Reglas del prompt de sistema (resumen operativo):

| Regla | Por qué |
|-------|---------|
| Cada valor: 1-2 frases, 15-30 palabras | FLUX.2 responde mejor a campos acotados |
| Sin detalles de junta ni cotas en mm | La geometría la pone la referencia, no el texto |
| Sin referencia a nombres de estudios | El estilo se lee de la foto, no de la memoria del modelo |
| `STRICT CAMERA LOCK` + `MATCH CAMERA OF IMAGE 1 EXACTLY` | Es la traducción textual del "bloqueo de geometría" |

### El paso de arcilla (módulo 7)

Antes del pase fotorreal, la volumetría se reinterpreta en **arcilla monocroma** con la lógica constructiva de Gaudí. Reglas del prompt oficial ([[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md|prompt-rhino-to-gaudi-instruction-md]]):

| Dial | Transformación |
|------|----------------|
| 0-2 | Los soportes se inclinan, las superficies se abomban en sillas shallow, los dinteles se arquean |
| 3-5 | Arcos catenarios, aberturas parabólicas, intradorsos ondulantes, soportes afilados |
| **6-8 (por defecto 7)** | Costillas catenarias completas · las juntas se abren en ramifications de bóvedas · columnas arbóreas · interior abovedado abierto · bocas hiperboloides |
| 9-10 | La masa se disuelve en un organismo continuo (nave de la Sagrada Família / cripta de la Colònia Güell) |

Reglas fijas en todos los niveles: cámara, perspectiva, huella, número de plantas, programa y ritmo de vanos. Y la prohibición explícita del *decorado* (mosaico, trencadís, vidriera): *"structural Gaudí, not decorated Gaudí"*.

## Strength del LoRA

| Valor | Comportamiento esperado |
|-------|-------------------------|
| 0,0 | Material genérico de FLUX.2; la referencia manda |
| **0,5** | **Valor que usa el curso** en su comparación del módulo 2 ("FLUX.2 Klein 9b + LoRA 50% strength") |
| 0,6-0,8 | Rango de trabajo recomendado para el estudio |
| 1,0 | **Segundo valor del curso** ("+ LoRA 100% strength"): máximo carácter |
| >1,2 | El delta domina la base: aparecen artefactos y repetición de textura |

## Exportación desde Rhino

```cmd
:: 3 pasadas desde la MISMA cámara (crítico: la geometría y la foto de material
:: tienen que compartir punto de vista para que la referencia sea coherente)
_-ViewCaptureToFile _Enter "C:\out\geo_shaded.png" _Enter 2048 _Enter
_-ViewCaptureToFile _Enter "C:\out\geo_lines.png"  _Enter 2048 _Enter
```

Fondos: liso (blanco o neutro) para la geometría; fondo real para la foto de material.

## Variantes de configuración

| Variante | Cambios | Cuándo |
|----------|---------|--------|
| Base (20 steps, cfg 5) | `Flux2Scheduler.steps=20`, `CFGGuider.cfg=5.0` | Si el LoRA se entrenó sobre `klein-base-9B` |
| GGUF local | `UnetLoaderGGUF` en lugar de `UNETLoader` + `ComfyUI-GGUF` | VRAM 8 GB con offload del text encoder |
| Sin LoRA | puentear el nodo `LoraLoaderModelOnly` | Línea base de aporte |
| Una sola referencia | desconectar `ReferenceLatent` (material) | Cuándo la foto de material confunde la composición |
