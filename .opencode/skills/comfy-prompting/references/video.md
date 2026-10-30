# Video — LTX-2.3 · Kling 3.0 · Seedance 2.0

> En video el prompt no describe una imagen: describe **qué cambia y cuándo**. Movimiento, cámara y tiempo son parte de la receta, no un extra.

## Estructura confiable

```
escena/sujeto → acción/movimiento → cámara → luz/mood/estilo → (audio/diálogo) → ritmo/duración
```

Reglas:

- El movimiento se describe **secuencial y desenredado**: primero qué se mueve, después cómo, después en qué orden.
- La cámara se nombra con su término técnico: `pan`, `tilt`, `dolly in`, `orbit`, `handheld`, `POV`, `crane`.
- Para planos de varios beats, desglose plano por plano o segundo por segundo.
- La duración se declara cuando el modelo la acepta.

## LTX-2.3

| Aspecto | Detalle |
|---|---|
| Carácter | rápido, orientado a tiempo real |
| Fuerte en | imagen→video, movimiento acotado y claro |
| Débil en | prompts largos y ambiguos |
| Duración | clips cortos, extensibles por etapas |
| Dónde corre | RunPod (local no viable) |

Prompt de recorrido arquitectónico:

```
Fixed tripod time-lapse. The building remains completely static. Clouds drift
across the sky, sunlight and shadows shift from morning to night, people move
along the balcony, plants sway gently. No camera movement.
```

Prompt de acercamiento:

```
Cinematically zoom in on the facade tiles, ending in an extreme close-up.
During the zoom, all four seasons pass: summer at the start, then rainy autumn,
then snowy winter, then spring at the close-up.
```

Regla de imagen→video: `strength ≈ 0,6`. En 1,0 la imagen se congela y no hay movimiento.

Cadena de nodos (2 etapas):

```
LoadImage (render final) → LTX-2 base (i2v) → LTX-2 upscale latente ×2 → VHS_VideoCombine (MP4)
```

Con control: `ltx-2-19b-IC-LoRA-{Depth,Canny,Pose}-Control` + `ltx-2-19b-distilled-lora-384`.

## Kling 3.0

| Aspecto | Detalle |
|---|---|
| Carácter | narrativa multi-shot con audio nativo |
| Fuerte en | diálogo, consistencia de personaje, acentos |
| Duración | hasta 15 s |
| Timestamps | sí: "at the 4th second…" |

Estructura con diálogo: etiquetar cada hablante.

```
Shot 1 (0–4s): Wide shot of the plaza at dawn, empty stone paving, soft mist.
Shot 2 (4–9s): Slow dolly in toward the pavilion entrance; a guide steps out.
GUIDE: "The market opens at seven."
Shot 3 (9–15s): Cut to the interior, warm light, people arranging stalls.
```

## Seedance 2.0

| Aspecto | Detalle |
|---|---|
| Carácter | desglose estructurado de escena |
| Fuerte en | acción, persecución, escenas generales y diálogo |
| Idioma | bilingüe **EN + ZH**: conviene escribir ambos |
| Estructura | arquetipo de escena + dinámica de espacio + firma de cámara |

Arquetipos y su firma de cámara:

| Arquetipo | Qué cambia | Cámara |
|---|---|---|
| Journey | posición en el espacio: ruta, vuelo, río, caminata | tracking, aérea, travelling lateral |
| Atmosphere | nada cambia: el mood es el contenido | push-in lento o plano fijo; micro-cambios |
| Reveal | oculto → visible: puerta, niebla, esquina | pan, crane, dolly reveal |
| Pursuit | distancia que se cierra o se abre | perseguido adelante, perseguidor atrás |
| Duel | dominancia que alterna | cámara baja del lado dominante |
| Impact | buildup lento → golpe rápido → aftermath lento | punto de contacto al centro |
| Confrontation | dominancia que cambia por intercambio | OTS cerrado, cruce de eje |
| Interrogation | asimétrico: uno extrae, el otro resiste | contrapicado al que pregunta, push-in al silencio |
| Negotiation | equilibrado: ambos necesitan algo | encuadre simétrico, tamaños de plano iguales |

## Errores típicos

| Síntoma | Causa | Corrección |
|---|---|---|
| Video congelado | strength 1,0 en i2v | bajar a ~0,6 |
| Movimiento caótico | varias acciones en una frase | una acción por beat |
| Deriva de estilo | sin ancla de luz | declarar hora y calidad de luz |
| Personaje cambia | sin referencia consistente | usar imagen de referencia + describir rasgos |
| Corte abrupto | beats sin duración | timestamps por beat |

## Fuentes

- LTX-2.3 prompt guide — https://ltx.io/model/model-blog/ltx-2-3-prompt-guide
- Kling 3.0 user guide — https://kling.ai/quickstart/klingai-video-3-model-user-guide
- Seedance 2.0 guide — https://seedance2.ai/guide
