# SD 1.5 y SDXL — dialecto keyword

> Modelos de lista: descriptores separados por coma, lo importante al principio, pesos explícitos y **negativo obligatorio**. Son los dos modelos que aceptan ControlNet con soltura.

## Estructura confiable

```
sujeto → detalles clave → estilo/medio → encuadre/composición → luz → color/mood → calidad
```

Cuanto antes aparece un término, más peso tiene. La ubicación y la materialidad van primeras: "Barcelona" o "board-formed concrete" no pueden quedar al final.

## Pesos y énfasis

| Sintaxis | Efecto |
|---|---|
| `(term)` | refuerza ~1,1× |
| `(term:1.2)` | refuerza 1,2× |
| `[term]` | debilita |
| `(term:0.8)` | debilita a 0,8× |

Usá pesos para corregir, no para tapar un prompt mal escrito. Si necesitás más de tres pesos, el prompt está mal ordenado.

## Negativo

Obligatorio en ambos. Base del estudio:

```
blurry, low quality, distorted, watermark, text, signature, cartoon, illustration,
warped perspective, melting geometry, bent windows, extra limbs, deformed
```

Agregá el negativo específico del caso: `people` si la escena va vacía, `oversaturated` si el modelo satura, `harsh shadows` si buscás luz difusa.

## SD 1.5

| Parámetro | Valor |
|---|---|
| Resolución nativa | 512×512 (768×512 para formato apaisado) |
| steps | 20–30 |
| cfg | 7–8 |
| sampler / scheduler | `euler_ancestral` + `karras` |
| Negativo | sí, obligatorio |
| LoRA | hasta 250 MB, strength 0,6–0,8 |
| ControlNet | Canny, Depth, Scribble, Lineart, MLSD, Normal, Seg, OpenPose |
| Dónde corre | local RX 570 sin problema |

Necesita refuerzo de calidad: `highly detailed, sharp focus, professional architectural photography`. Es débil en escenas complejas y en texto legible. Un prompt de 30–60 palabras rinde mejor que uno de 120.

Cadena de nodos:

```
CheckpointLoaderSimple → CLIPTextEncode (+) ┐
                        → CLIPTextEncode (−) ┤
EmptyLatentImage ───────────────────────────┴→ KSampler → VAEDecode → SaveImage
```

Con ControlNet, entre el encode y el sampler:

```
LoadImage → ImageScale (512×512, lanczos) → CannyEdgeDetector → ControlNetLoader
          → ControlNetApplyAdvanced → KSampler
```

| Input | low/high | strength | end% |
|---|---|---|---|
| Planta limpia DWG→PNG | 30 / 100 | 1,0 | 0,80 |
| Fachada make2d | 80 / 180 | 0,9 | 0,80 |
| Croquis a mano | 20 / 80 | 0,8 | 0,75 |
| Hidden line Revit | 40 / 120 | 0,9 | 0,80 |

## SDXL

| Parámetro | Valor |
|---|---|
| Resolución nativa | 1024² · 1216×832 exterior · 832×1216 interior |
| steps | 30–35 |
| cfg | 3–4 |
| sampler / scheduler | `dpmpp_2m` + `karras` |
| Negativo | sí, pero más corto |
| LoRA | hasta 900 MB |
| ControlNet | Union (1,5 GB, solo RunPod) |
| Dónde corre | local justo, RunPod recomendado |

Entiende mejor la frase: acepta descriptores naturales, no necesita spam de calidad. Prefijo útil: `photorealistic, raw photo, 8k uhd, highly detailed, canon r5, 24mm tilt-shift` + tipología. Un prompt de 40–80 palabras es el punto dulce.

El `cfg` bajo es lo que más se equivoca al migrar desde SD 1.5: con 7–8 SDXL satura y quema los blancos. Con 3–4 respira.

Cadena de nodos: idéntica a SD 1.5, cambiando el checkpoint. Ese es el argumento del curso: "lo único que cambia es el modelo".

## Errores típicos

| Síntoma | Causa | Corrección |
|---|---|---|
| Geometría derretida | prompt sin anclaje espacial | nombrar el sistema constructivo y el encuadre |
| Blancos quemados en SDXL | cfg heredado de SD 1.5 | bajar a 3–4 |
| Textura plástica | exceso de tags de calidad | quitar `8k, masterpiece, best quality` repetidos |
| Estilo de ilustración | negativo sin `illustration, cartoon` | agregarlos al negativo |
| Ventanas torcidas | falta de ControlNet | Canny o MLSD con strength 0,8–0,9 |

## Fuentes

- SD 1.5 prompt guide — https://stable-diffusion-art.com/prompt-guide/
- Vocabulario de encuadres, lentes, luz y color — https://gist.github.com/lukecav/39431632378a63a7bc3860106943a96a
