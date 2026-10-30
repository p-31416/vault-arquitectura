# FLUX.2 — dialecto prosa + JSON

> El modelo de mayor comprensión de la familia: acepta prosa larga y capas, entiende JSON estructurado, códigos hex y hasta 4 imágenes de referencia (klein) o 10 (max). **No tiene prompt negativo** y **klein no hace upsampling**: lo que escribís es lo que recibe.

## Prosa (por defecto)

Estructura: `sujeto → acción/estado → estilo → contexto → luz → técnico`.

Largo según variante:

| Variante | Largo ideal | Por qué |
|---|---|---|
| klein 4B / 9B | 40–70 palabras | sin upsampling: cada palabra cuenta |
| pro / max / flex | 30–80 palabras (hasta 80+) | el upsampling completa lo que falta |

Orden de prioridad: sujeto → acción clave → estilo crítico → contexto esencial → detalles secundarios. El modelo pesa más lo que viene primero.

Para fotorrealismo, nombrar cuerpo, lente y stock rinde más que decir "professional photo":

```
A weathered concrete pavilion on the Catalan coast at blue hour, its deep window
reveals glowing warm against the cool facade. Shot on a Phase One IQ4 with a 35mm
lens at f/5.6, Kodak Portra 400, soft overcast diffusion, muted earth palette.
```

## JSON estructurado

Esquema base oficial:

```json
{
  "scene": "overall scene description",
  "subjects": [
    {
      "description": "detailed subject description",
      "position": "where in frame",
      "action": "what they're doing"
    }
  ],
  "style": "artistic style",
  "color_palette": ["#hex1", "#hex2", "#hex3"],
  "lighting": "lighting description",
  "mood": "emotional tone",
  "background": "background details",
  "composition": "framing and layout",
  "camera": {
    "angle": "camera angle",
    "lens": "lens type",
    "depth_of_field": "focus behavior"
  }
}
```

Cuándo conviene JSON:

- producción con estructura repetible entre corridas
- escenas con varios sujetos y relaciones entre ellos
- iteración quirúrgica: cambiar un bloque y dejar el resto intacto
- automatización por script o por el MCP

Cuándo conviene prosa: exploración rápida, un solo sujeto, fase divergente. La regla del curso es explícita: en el doble diamante inicial manda el prompt corto, sin JSON; el JSON entra cuando ya hay una dirección elegida.

### Variante del estudio (arquitectura, FLUX.2 klein)

```json
{
  "scene": "[1–2 frases. 'Professional highly detailed realistic architectural photography of {tipología}. STRICT CAMERA LOCK: match Image 1 perspective.' + una frase que nombra la transformación]",
  "subjects": [
    {
      "description": "[masa preservada de la Imagen 1 + sistema de fachada tomado de la Imagen 2]",
      "position": "[ubicación espacial respecto de la composición de la Imagen 1]",
      "action": "[cualidad estática o impresión cinética]"
    }
  ],
  "style": "[carácter material leído de la Imagen 2 + 'Photography by Iwan Baan and {fotógrafo}'. Phase One IQ4, {lente}, {stock}, grano]",
  "color_palette": ["#______", "#______", "#______", "#______", "#______", "#______"],
  "lighting": "[calidad de luz de la Imagen 2: hora, difusión, sombra, glow interior]",
  "mood": "[2–3 adjetivos + una frase que ata el mood a la atmósfera de la Imagen 2]",
  "background": "[sitio, terreno, cielo — regionalmente auténtico a la ubicación declarada]",
  "composition": "[1–2 frases. 'MATCH CAMERA OF IMAGE 1 EXACTLY.' + tipo de perspectiva]",
  "camera": {
    "angle": "[frase corta que coincide con la Imagen 1]",
    "lens": "[solo la lente]",
    "depth_of_field": "[apertura y foco en una frase]"
  }
}
```

Constantes del estudio (heredadas del curso):

- **Iwan Baan** siempre como primera referencia de fotógrafo; el segundo se elige por contexto.
- **Phase One IQ4** siempre como cuerpo.
- **Seis hex exactos**: 3–4 derivados de la materialidad, 1–2 de la luz y el cielo.
- Cada valor, 1–2 frases, 15–30 palabras. Sin dimensiones milimétricas ni detalles de junta.

### Lógica de lente (arquitectura)

| Escenario | Lente | Razón |
|---|---|---|
| Masa vertical alta | 24mm tilt-shift | corrige verticales convergentes |
| Composición horizontal amplia | 24–28mm | capta la extensión sin distorsión |
| Exterior de rango medio | 35mm | perspectiva natural |
| Detalle comprimido / íntimo | 50mm | aplana la profundidad, acentúa la superficie |
| Detalle de fachada / material | 85mm | aísla la textura |
| Aérea / vista de pájaro | 35mm | campo equilibrado en altura |

### Stock por mood

| Stock | Carácter |
|---|---|
| Kodak Portra 400 | naturalismo cálido, tonos suaves, sombras levantadas |
| Kodak Ektar 100 | color saturado, contraste alto, paisajes vivos |
| Fuji Velvia 50 | hipersaturación, cielos dramáticos |
| Fuji Pro 400H | pastel, desaturado, elegancia de día nublado |
| Kodak Tri-X 400 | monocromo de alto contraste |
| Ilford HP5 | grano marcado, carácter documental |
| CineStill 800T | tungsteno, halación cinematográfica, noche e interior |

## Parámetros

| Parámetro | klein 9B |
|---|---|
| Resolución | múltiplos de 16, de 64×64 a 4 MP; 1024² como base |
| steps | 4 (destilado) · 20 (base) |
| cfg | 1 (destilado) · 5 (base) |
| scheduler | `Flux2Scheduler` |
| sampler | `SamplerCustomAdvanced` (no `KSampler`) |
| Negativo | no |
| Referencias | hasta 4 imágenes |
| VRAM | ~24 GB |

Escalado de entradas (R2 del vault):

```
ImageScaleToTotalPixels  upscale_method=lanczos  megapixels=1.0  → geometría
ImageScaleToTotalPixels  upscale_method=lanczos  megapixels=0.5  → referencia de material
```

La relación 1,0 / 0,5 es la que hace caer el material a la escala correcta de la geometría.

## Cadena de nodos (klein 9B)

```
UNETLoader (flux2-klein-9b) ─────────────┐
CLIPLoader (qwen3-8b) ───────────────────┤
VAELoader (flux2-vae) ───────────────────┤
LoadImage geo ─ ImageScaleToTotalPixels 1.0 MP ─ VAEEncode ─┐
LoadImage material ─ ImageScaleToTotalPixels 0.5 MP ─ VAEEncode ─┤
                                              ReferenceLatent ×2 ─┤
CLIPTextEncode (+) ──────────────────────────────────────────────┤
Flux2Scheduler ──────────────────────────────────────────────────┤
CFGGuider ───────────────────────────────────────────────────────┤
SamplerCustomAdvanced (noise · guider · sampler · sigmas · latent) ┘
        → VAEDecode → ImageUpscaleWithModel (RealESRGAN_x4plus) → SaveImage
```

Diferencias que rompen el port desde FLUX.1: el sampler es `SamplerCustomAdvanced`, el guía es `CFGGuider`, el text encoder es Qwen3-8B (no T5), y el VAE es el de FLUX.2.

## Lo que klein no hace

- no hace **prompt upsampling**: escribí el prompt completo
- no tiene **grounding search** (eso es max)
- no acepta más de **4 referencias**
- no tiene **ControlNet oficial** de BFL: el control geométrico se hace con `ReferenceLatent`

## Multi-referencia

Cuando hay varias imágenes, declarar el rol de cada una en el prompt, en el mismo orden en que entran:

```
The massing and camera come from image 1. The material, colour temperature and
surface finish come from image 2. The vegetation belongs to image 3.
```

Sin esa declaración el modelo mezcla roles y la geometría se pierde.

## Errores típicos

| Síntoma | Causa | Corrección |
|---|---|---|
| Geometría alterada | cámara no bloqueada | `STRICT CAMERA LOCK` + `MATCH CAMERA OF IMAGE 1 EXACTLY` |
| Material a escala equivocada | ambas entradas a 1,0 MP | referencia a 0,5 MP |
| Prompt ignorado a medias | 4 steps con variante base | base: 20 steps, cfg 5 |
| Resultado genérico | prompt corto en klein | 40–70 palabras con luz y cámara explícitas |
| JSON sin efecto | modelo distinto de FLUX.2 | JSON solo en FLUX.2 |
| Personas flotando | figuras rosas del massing sin reemplazo | describir el reemplazo por peatones reales |

## Fuentes

- FLUX.2 overview — https://docs.bfl.ai/flux_2/flux2_overview
- Prompting guide FLUX.2 [pro]/[max] — https://docs.bfl.ai/guides/prompting_guide_flux2
- Guía técnica unificada (aspect ratios, negativos, upsampling) — https://docs.us.bfl.ai/guides/prompting_unified_technical
- FLUX.2 [klein] generación rápida — https://help.bfl.ai/articles/7592221790-how-do-i-generate-quickly-with-flux-2-klein
- Buenas prácticas BFL — https://github.com/black-forest-labs/skills/blob/master/skills/flux-image-best-practices/AGENTS.md
