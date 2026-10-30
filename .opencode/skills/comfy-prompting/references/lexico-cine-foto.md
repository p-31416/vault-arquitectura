# Léxico de cine y fotografía

> Vocabulario compartido por todos los modelos. La lista es la misma; lo que cambia es cómo se empaqueta: tag con peso en SD 1.5/SDXL, frase en FLUX, clave de cámara en el JSON de FLUX.2.

## 1. Encuadre (shot size)

| Término | Qué muestra |
|---|---|
| EWS — Extreme Wide Shot | el edificio como punto en el territorio |
| WS / LS — Wide / Long Shot | el edificio completo con su entorno |
| FS — Full Shot | el objeto completo, encuadre justo |
| MLS / MWS — Medium Long / Medium Wide | tres cuartos del volumen |
| Cowboy Shot | de medio muslo hacia arriba |
| MS — Medium Shot | porción significativa, contexto reconocible |
| MCU — Medium Close Up | detalle con algo de contexto |
| CU — Close Up | un elemento: una ventana, una junta |
| ECU — Extreme Close Up | textura pura |
| Macro | poro del material, fibra, grano |

## 2. Ángulo y vista

| Término | Efecto |
|---|---|
| Eye level | neutralidad, escala humana |
| Low angle / worm's-eye | monumentalidad, el edificio domina |
| High angle / bird's-eye | legibilidad del conjunto, control |
| Hip level · knee level · ground level | variaciones de escala percibida |
| Dutch angle | tensión, inestabilidad |
| Over-the-shoulder | relación entre dos elementos |
| Three-quarter view | volumen y dos fachadas a la vez |
| Frontal / rear / profile | ortodoxia de elevación |
| Oblique | fuga, profundidad |
| Aerial / helicopter | territorio y tejido urbano |
| Top-down / overhead | planta legible |
| Isometric / axonometric | volumetría sin fuga |
| Cross-sectional | corte como imagen |
| POV | el espectador dentro de la escena |
| Panoramic | amplitud horizontal extrema |
| Reflection view | duplicación en agua o vidrio |

## 3. Lentes

| Lente | Uso |
|---|---|
| 14mm | distorsión dramática, espacio comprimido |
| 24mm tilt-shift | verticales rectas en torre |
| 24–28mm | amplitud horizontal sin deformar |
| 35mm | perspectiva natural, el estándar documental |
| 50mm | compresión suave, intimidad |
| 85mm | aislamiento del detalle, retrato de fachada |
| 100mm macro | material en primer plano |
| 135mm | compresión fuerte, fondo laminado |
| 200mm | aplanamiento extremo, capas urbanas |

Filtros y efectos ópticos: polarizador, ND, filtro degradado, flare, halación, aberración cromática, viñeteado.

## 4. Luz

| Término | Carácter |
|---|---|
| Golden hour | cálida, direccional, sombras largas |
| Blue hour | fría, ambiente, luces interiores encendidas |
| Overcast | difusa, plana, revela material |
| Hard noon | contraste brutal, sombras duras |
| Rembrandt | clásica, triángulo de sombra |
| Butterfly | frontal alta, glamour |
| Rim / edge light | separa el volumen del fondo |
| Bounce | rebote suave desde el piso o un plano |
| Volumetric | haces visibles en polvo o niebla |
| Low-key | predominio de sombra |
| High-key | predominio de luz |
| Practical lights | luces dentro de la escena |
| Subsurface scattering | luz que atraviesa materiales translúcidos |

## 5. Película y cuerpo

| Stock | Carácter |
|---|---|
| Kodak Portra 400 | naturalismo cálido, piel y piedra |
| Kodak Ektar 100 | saturación, contraste, paisaje |
| Fuji Velvia 50 | hipersaturación, cielos dramáticos |
| Fuji Pro 400H | pastel, nublado, elegante |
| Kodak Tri-X 400 | monocromo de alto contraste |
| Ilford HP5 | grano documental |
| CineStill 800T | tungsteno, halación, noche |

Cuerpos: Phase One IQ4 (medio formato, referencia del estudio) · Fujifilm X-T5 · Canon R5 · Hasselblad X2D.

Fotógrafos de referencia: Iwan Baan · Hélène Binet · Julien Lanoo · Rory Gardiner · Simone Bossi.

## 6. Materiales (término exacto en inglés)

| Español | Inglés de prompt |
|---|---|
| Hormigón visto con encofrado de tabla | board-formed concrete |
| Hormigón martelinado | bush-hammered concrete |
| Hormigón prefabricado | precast concrete |
| Acero corten | weathering steel / corten |
| Bronce anodizado | bronze-anodised |
| Aluminio anodizado | anodised aluminium |
| Travertino | travertine |
| Mármol veteado | veined marble |
| Piedra caliza | limestone |
| Ladrillo visto | exposed brick |
| Madera laminada | glulam timber |
| Madera carbonizada | charred timber / shou sugi ban |
| Muro cortina | curtain wall |
| Doble piel | double-skin facade |
| Brise-soleil | brise-soleil |
| Celosía | screen / lattice |
| Pérgola | pergola |
| Voladizo | cantilever |
| Retranqueo | setback |
| Patio interior | courtyard |
| Lucernario | skylight |
| Claraboya | rooflight |
| Junta | joint |
| Revestimiento | cladding |
| Alféizar | sill |
| Dintel | lintel |
| Pilar | piloti / column |
| Viga | beam |
| Solera | slab |
| Muro de carga | load-bearing wall |

## 7. Color

Esquemas: monocromático · análogo · complementario · complementario dividido · triádico · cuadrado · rectángulo · 60-30-10.

En FLUX.2 el color se ata a un objeto con hex: "the facade is #8C8A85" rinde mejor que "usa gris #8C8A85".

## 8. Movimiento de cámara (video)

`pan` · `tilt` · `dolly in/out` · `truck` · `crane` · `orbit` · `handheld` · `steadicam` · `POV` · `whip pan` · `push-in` · `pull-back` · `tracking` · `static hold` · `time-lapse` · `hyperlapse`.

## 9. Cómo se empaqueta en cada dialecto

| Concepto | SD 1.5 / SDXL | FLUX.1 / FLUX.2 | JSON FLUX.2 |
|---|---|---|---|
| Encuadre | `wide shot, low angle` | "a wide shot from a low angle" | `camera.angle` |
| Lente | `24mm tilt-shift` | "shot on a 24mm tilt-shift" | `camera.lens` |
| Luz | `golden hour, rim light` | "in the last horizontal light of the day" | `lighting` |
| Material | `board-formed concrete` | "board-formed concrete catching the light" | `subjects[0].description` |
| Stock | `kodak portra 400, film grain` | "Kodak Portra 400, fine grain" | `style` |
| Paleta | `muted earth palette` | "muted earth palette" | `color_palette` (6 hex) |
| Mood | `melancholic, quiet` | "a quiet, melancholic stillness" | `mood` |

Regla: en keyword el término va **solo y con coma**; en prosa va **dentro de una frase con verbo**; en JSON va **en la clave que le corresponde**. Poner "24mm tilt-shift" en `mood` es tan grave como no ponerlo.

## 10. Lo que no se escribe

- Adjetivos vacíos: "sleek", "modern", "beautiful", "stunning".
- Tags de calidad apilados en FLUX (`8k, masterpiece, best quality`): no aportan y compiten por atención.
- Dimensiones milimétricas y detalles de junta: el modelo no los resuelve.
- Negaciones en FLUX: se sustituyen por descripción positiva.

## Fuentes

- Vocabulario de encuadres, lentes, luz y color — https://gist.github.com/lukecav/39431632378a63a7bc3860106943a96a
- Ultimate guide to camera shots — https://www.studiobinder.com/blog/ultimate-guide-to-camera-shots/
- Buenas prácticas BFL — https://github.com/black-forest-labs/skills/blob/master/skills/flux-image-best-practices/AGENTS.md
