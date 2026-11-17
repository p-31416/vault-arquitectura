---
tipo: flujo
mvp: 08
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_08, F1, camara, viewpoint, casa-moderna, sdxl, realvis]
idioma: es
---

# F1 — cámara (misma casa, otro punto de vista)

> JSON canónico: `workflow_F1-camara.json` — RealVisXL V5.0 estándar (`realvisxlV50_v50Bakedvae.safetensors`), a partir de la keeper F0 (`casa-F0b-v01_*.png` copiada a `P:\00-repos\ComfyUI\input\`). Si tu JSON aún dice `realvisxlV50_v50LightningBakedvae.safetensors`, cambia el `ckpt_name` al estándar: el Lightning 512 sale blando y pierde carpintería negra / listones.
> Convención fija del estudio: **positivo en azul, negativo en rojo**. En el canvas: clic derecho en el nodo → Color → azul/rojo (el título 🔵/🔴 ya viene en el JSON).

## Respuesta corta a la pregunta de la sesión

Sí, F1 es "le doy la imagen keeper + le digo con el prompt qué quiero y me devuelve la imagen". La fidelidad la manda el `denoise`:

- `0.45-0.55` = identidad alta, movimiento chico (corrección de encuadre, 5-10°).
- `0.60` = equilibrio (15° lateral, low-angle leve).
- `0.65-0.75` = movimiento grande (aérea, noche misma cámara), la casa se reinventa más y hay que fijar con IPAdapter/ControlNet.

Con img2img puro el prompt solo sugiere, no garantiza geometría. Para giro preciso ver § "Vía precisa imagen + 3D" abajo.

## Positivo (🔵 — lo único que cambia entre variantes)

Base (15° izquierda, misma tarde):

```text
same modern single-family house in Buenos Aires as input image,
same board-formed concrete facade, black steel frames, dark timber slats,
urban context between party walls, small front patio,
new viewpoint 15 degrees to the left, eye-level street view,
late afternoon warm light, long soft shadows,
architectural photography, sharp focus, highly detailed
```

Variantes (una por corrida, resto idéntico):

```text
// V-low: same house, low-angle view from sidewalk, looking slightly up, same materials and light
// V-aerea: same house, slightly elevated three-quarter view, full facade, same materials, same afternoon light
// V-noche: same house, same camera as input, blue hour night, warm interior lights on, street lamps on
```

Bloques: identidad (same house + materiales) → cámara nueva → luz → cierre foto. La identidad va primero para anclar.

## Negativo (🔴 — fijo del estudio, no se toca)

```text
blurry, low quality, distorted, deformed, ugly,
different house, different facade, different materials,
suburban villa, countryside, forest, beach,
cartoon, illustration, painting, drawing,
watermark, text, signature, logo,
oversaturated, overexposed, underexposed, grain, noise,
people, cars
```

## KSampler — valores F1 (RealVis estándar)

| Param | Normal F1 | Rango que se puede tocar | Efecto |
|---|---|---|---|
| seed | 42 fija | 42 fija (no se rota en F1) | fija identidad; cambiar seed = otra casa |
| steps | 32 | 28–40 | +steps = más detalle fino, +tiempo lineal |
| cfg | 4 | 3–5 | +cfg = más obediencia al viewpoint, riesgo de quemado |
| sampler | dpmpp_2m | dpmpp_2m | el de F0, no se cambia en F1 |
| scheduler | karras | karras | el de F0 |
| denoise | 0.60 | 0.45–0.75 (la perilla F1) | bajo = fiel, alto = se mueve más |
| tamaño | 1216×832 | igual que la keeper F0 | no reescalar a 512 en F1 final (solo draft) |
| modelo | RealVis estándar | no Lightning en F1 final | Lightning = draft rápido, estándar = lámina |

> Draft rápido: Lightning 512, 6 steps, cfg 1.5, denoise 0.6 para previsualizar el encuadre en minutos. La keeper sale siempre del estándar.

## Cómo funciona denoise en F1 (leer antes de tocar nada)

El denoise es cuánta imagen original se conserva: `0.0` = devuelve la keeper tal cual, `1.0` = la ignora y genera de cero (equivale a F0).

- T1 (0.55) vs T2 (0.65) con misma seed y mismo prompt: **misma intención de cámara**, T1 más fiel a medianeras/carpintería, T2 gira más pero inventa más.
- Si pierde identidad (cambia el hormigón, desaparece la medianera): bajar a 0.5 y reforzar el positivo con `same ... as input image`.
- Si no se mueve (casi igual a la keeper): subir a 0.7 en pasos de 0.05, nunca de a 0.2.

## 5 pruebas mínimas F1 (una variable por prueba, seed 42 siempre)

| # | Cambio | Esperado | Salida |
|---|---|---|---|
| T1 | base 15° izquierda, denoise 0.60 | giro visible, casa reconocible ✅ | `casa-F1cam-v01-15izq.png` |
| T2 | denoise 0.50 (mismo prompt) | más fiel, giro menor | comparar lado a lado vs T1 |
| T3 | denoise 0.70 (mismo prompt) | giro mayor, vigilar materiales | si inventa, se descarta |
| T4 | V-low low-angle, denoise 0.60 | contrapicado leve vereda | `casa-F1cam-v02-low.png` |
| T5 | V-noche misma cámara, denoise 0.60 | blue hour + interiores cálidos | `casa-F1cam-v03-noche.png` |

Veredicto Sol (keeper/descartar) → la ganadora alimenta F2–F5. Registrar en dashboard casa + reporte 20.

## Escala F1: prompt → ControlNet → IPAdapter → 3D (sin destruir geometría)

| Nivel | Qué fija | Nodos + pesos | Cuándo usar |
|---|---|---|---|
| F1a prompt (hecho) | nada, solo sugiere | `workflow_F1-camara.json`, denoise 0.6 | giros chicos 5-15°, pruebas rápidas |
| F1b Canny | bordes / carpintería / medianeras | `workflow_F1b-canny.json`: `Canny 0.31/0.59` + `control_sdxl_canny_fp16` strength 0.75, end 0.8, denoise 0.6 | misma cámara o giro leve: mantiene dibujo sin congelar volumen |
| F1c IPAdapter | identidad material | `workflow_F1c-ipadapter.json`: `IPAdapterAdvanced standard 0.6`, end 0.8, denoise 0.6 | el hormigón/listones se lavan: sube identidad sin tocar prompt |
| F1d Depth (siguiente) | volúmenes / masas | requiere preprocesador depth (hoy no instalado) + `control_v11f1p_sd15_depth` solo diagnóstico SD1.5 | giro grande: mantiene proporciones mejor que Canny |
| F1e 3D final (pod) | cámara exacta yaw/pitch/radius | `camera-comfyUI` warp + inpaint o MetaView/Qwen-Edit | objetivo final: la geometría la manda el 3D, el prompt solo rellena ocluidos |

Canny = líneas (fachada, carpintería, medianera). Depth = masas (qué está delante/detrás, cuánto gira el volumen). Para cambiar ángulo sin destruir: Canny alto (0.75-0.9) congela demasiado y no deja girar; Depth medio (0.6-0.75) deja girar manteniendo proporciones. Regla: giro leve → Canny; giro real → Depth o 3D.

Aviso local RX 570 8GB: SDXL RealVis (6.9GB) + Canny SDXL (2.5GB) = 9.4GB, va justo. Si OOM: baja a 1024×704 draft, o corre F1b en SD1.5 solo como chequeo geométrico (nunca imagen final). CAD del vault: `[[wiki/glosario/software/comfyui|comfyui]]` § Canny 0.31/0.59, ControlNetApplyAdvanced 0.7-0.9.

## Vía precisa imagen + 3D (lo que viste de "girar la cámara")

Lo que encontraste existe y es familia Zero123 → SV3D → ViewCrafter → MetaView: de una foto + un 3D (o depth estimado) se re-renderiza la vista pedida con yaw/pitch/radius. Funciona así: depth → nube de puntos → reproyección geométrica → inpaint solo de lo ocluido.

Por qué hoy queda fuera del MVP_08 local ($0, RX 570 8GB, DirectML/CPU):

- Zero123 / SV3D: objetos con fondo blanco, 256/576 px, necesitan checkpoint `stable-zero123` / `SV3D_p` que no tienes; en casa con medianeras y patio falla y deforma.
- ViewCrafter + DUSt3R: video orbital 576×1024, 18–23 GB VRAM en A100 + CUDA + PyTorch3D. Tu estación no lo sostiene.
- MetaView (ECCV 2026, Qwen-Image-Edit + Depth Anything 3, yaw/pitch/radius, 8 steps Lightning, trigger `镜头视角转到指定位置`): checkpoint 26.5 GB fp8 + encoder 9 GB + VAE + `DA3-GIANT-1.1`, corre en 16 GB con streaming CUDA. En 8 GB con offload a RAM queda para pod, no para local.
- Lo que sí corre local y es la vía precisa realista: warp por depth + inpaint (principio GenWarp / StereoDiffusion Fast / `camera-comfyUI`: `DepthEstimator → DepthToPointCloud → TransformPointCloud → ProjectPointCloud` + inpaint SD1.5 que ya tienes `sd-v1-5-inpainting-fp16`). La geometría manda y el prompt solo rellena huecos.

Recomendación estudio: F1 actual (img2img + denoise) para láminas de esta semana; abrir F1b-precisa solo cuando se instale el pack `camera-comfyUI` + `Depth Anything` y se pruebe en pod o en local por mitades. Referencias verificadas: `https://comfyanonymous.github.io/ComfyUI_examples/3d/` · `https://huggingface.co/Wherebot101/MetaView-ComfyUI` · `https://github.com/Drexubery/ViewCrafter` · `https://github.com/Alexankharin/camera-comfyUI`.

## Entrada / salida

Entrada: keeper F0 en `P:\00-repos\ComfyUI\input\` (`casa-F0b-v01_00001_.png`). Salidas: `casa-F1cam-v{NN}` (F1a prompt) · `casa-F1b-canny-v{NN}` (F1b) · `casa-F1c-ipa-v{NN}` (F1c). Abrir el JSON en `http://127.0.0.1:8188`, leer nodos y recién encolar.
