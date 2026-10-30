# FLUX.1 — dialecto prosa

> Modelo de lenguaje natural: describís la imagen como se la explicarías a una persona. Sin pesos, sin tags de calidad, sin negativo.

## Regla central

**No hay prompt negativo.** Cuando el modelo procesa una negación se queda con el objeto negado: "una fachada sin gente" produce gente. La estrategia es la sustitución: nombrás lo que sí está.

| En vez de… | Escribí… |
|---|---|
| no people | empty, deserted, solitary |
| no text | clean surfaces, unmarked |
| no color | monochrome, grayscale |
| not dark | brightly lit, sun-drenched |
| not modern | traditional, period-accurate |
| no clutter | minimal, pared-down |

Si el flujo tiene un nodo de negativo heredado, va con `ConditioningZeroOut`, no con texto.

## Estructura

```
sujeto → atributos → acción/estado → entorno → estilo/medio → luz → composición → técnico
```

Ejemplo de arquitectura:

```
A low-slung concrete pavilion sits on a rocky plateau above the Mediterranean,
its board-formed walls catching the last horizontal light of the day. Deep window
reveals cut dark bands across the facade while the interior glows warm against
the cooling sky. Shot on a Phase One IQ4 with a 35mm lens, f/8, overcast-to-golden
transition, fine grain, muted earth palette.
```

## Parámetros

| Parámetro | FLUX.1 dev | FLUX.1 schnell |
|---|---|---|
| Resolución | 1024² (o múltiplos de 16) | 1024² |
| steps | 20–28 | 4 |
| cfg / guidance | 1,0 (FluxGuidance aparte) | 1,0 |
| sampler | `euler` + `simple` | `euler` + `simple` |
| Negativo | no | no |
| LoRA | compatible con la base dev | limitado |

`FluxGuidance` es el mando real de adherencia en dev: 2,5–3,5 para seguir el prompt con firmeza, 1,0–2,0 para soltar la composición.

## Cadena de nodos

```
UNETLoader (flux1-dev.safetensors)
DualCLIPLoader (clip_l + t5xxl)
VAELoader (ae.safetensors)
CLIPTextEncode (+) ─ FluxGuidance ─┐
ConditioningZeroOut (negativo) ────┤
EmptyLatentImage ──────────────────┴→ KSampler (cfg 1) → VAEDecode → SaveImage
```

El negativo no desaparece del grafo: se anula. Es el error más común al portar un workflow de SDXL.

## Edición y control estructural

En FLUX.1 el control vive en la familia **Tools**, no en ControlNet:

| Herramienta | Para qué |
|---|---|
| Kontext | edición por instrucción conservando la imagen |
| Canny | control de bordes |
| Depth | control de profundidad |
| Redux | variaciones guiadas por imagen |
| Fill | inpainting / outpainting |

En FLUX.2 estas funciones son nativas: no hace falta la familia Tools.

## Dónde corre

Local RX 570 no alcanza: el text encoder T5 es el que rompe la VRAM. RunPod con 24 GB, o Comfy Cloud.

## Errores típicos

| Síntoma | Causa | Corrección |
|---|---|---|
| Aparece justo lo que evitaba | negativo escrito en texto | usar sustitución positiva |
| Imagen plana | falta de luz explícita | nombrar hora, difusión y dirección |
| Prompt ignorado | `FluxGuidance` en 1,0 | subir a 2,5–3,5 |
| Ruido y estructura rota | 4 steps con dev | dev necesita 20+; schnell es el de 4 |
| Texto ilegible | pedir texto sin comillas | poner las palabras exactas entre comillas |

## Fuentes

- FLUX prompting summary — https://docs.bfl.ai/guides/prompting_summary
- FLUX.2 overview (comparativa de familia) — https://docs.bfl.ai/flux_2/flux2_overview
- Buenas prácticas oficiales de BFL — https://github.com/black-forest-labs/skills/blob/master/skills/flux-image-best-practices/AGENTS.md
