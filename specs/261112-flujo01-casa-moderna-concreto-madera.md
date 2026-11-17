---
tipo: spec
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador
tags: [spec, flujo01, casa-moderna, concreto, madera, exterior, parametros, twinmotion]
---

# Flujo 1 — casa moderna hormigón + madera, vista exterior (configurable como Twinmotion/D5)

> Primer flujo del estudio. Sin prompt coach: la gente elige parámetros (botones/formulario/Telegram) y un constructor determinista arma el prompt. Misma volumetría, varios estilos. El agente IA (Hermes) entra después, sobre este mismo contrato.

## 1. Descripción

Genera la casa moderna simple (hormigón + madera, exterior) con controles explícitos de ubicación, entorno, iluminación, cámara y estilo — lo básico que se configura en Twinmotion/D5/Lumion — sin escribir prompts a mano.
Objetivo: que cualquier persona del estudio produzca variantes coherentes de la misma volumetría tocando solo parámetros, y que cada variante quede registrada (parámetro + seed + modelo) para la lámina.

## 2. Parámetros configurables (el "panel Twinmotion")

| Parámetro | Opciones | Qué mueve en el flujo |
|---|---|---|
| `ubicacion` | `barrio-jardin` / `ladera-bosque` / `costero` / `urbano-medianeras` | fondo + vegetación del prompt + referencia de entorno |
| `hora` | `manana` / `mediodia` / `tarde` (default) / `noche` | prompt luz + (noche: interior cálido encendido) |
| `temp_luz` | `calida` (3000-3500K) / `neutra` (4500K) / `fria` (6500K) | adjetivos prompt (`warm golden` / `neutral daylight` / `cool overcast`); Kelvin exacto queda para fase 2, hoy son 3 presets |
| `camara` | `eye-level 24mm` / `aerea-suave` / `low-angle` / `axon-30-60` | prompt cámara + (F3: denoise 0.6-0.7 sobre keeper) |
| `estilo_muro` | `hormigon-tabla` / `hormigon-liso` / `hormigon-pigmentado` / `listones-madera` / `mixto-base-hormigon` | prompt material + variante (ver §5) |
| `tipo_vista` | `exterior` (este flujo) / `interior` | cambia checkpoint + LoRA (ver §3) |

Exterior vs interior cambian modelo: exterior usa RealVisXL/Juggernaut + LoRA fachada; interior usará Juggernaut + LoRA interior (`ArcvizXL_V01`, `room`) + prompt de calidez. Mismo panel, distinto preset base.

## 3. Mapeo parámetro → modelo/LoRA (local RX 570)

| Vista | Checkpoint | LoRA | Sampler |
|---|---|---|---|
| exterior día | RealVisXL v5.0 1216x832 (iterar: Lightning 512) | `ArcvizXL_V01` 0.6 / `Architecture_Building` 0.5 | dpmpp_2m/karras 30-35, cfg 3-4 |
| exterior noche | mismo + prompt interior encendido | mismo | mismo + denoise F5 si parte de keeper día |
| interior | Juggernaut v9 1216x832 | `ArcvizXL_V01` 0.7 + `room` 0.4 | dpmpp_2m/karras 35, cfg 4 |

## 4. Sin coach: constructor determinista de prompt

Nada de LLM redactando. Regla fija, auditable:

```text
photorealistic, raw photo, modern single-family house, {estilo_muro}, {ubicacion},
{hora} {temp_luz} light, sharp shadows, {camara}, 8k uhd, architectural photography
+ negativo fijo estudio
```

La persona toca botones (Telegram/n8n o formulario), el constructor arma el string y lo registra en `02-WF-log` junto a seed 42 + modelo. El agente Hermes futuro solo rellena estos mismos campos — el contrato no cambia.

## 5. Misma volumetría, 4+1 estilos (aprende con el tiempo)

Seed y cámara fijas, solo cambia `estilo_muro`. Biblioteca inicial de hormigones que crece por corrida:

1. `hormigon-tabla` — board-formed, vetas horizontales marcadas.
2. `hormigon-liso` — visto liso, poros finos.
3. `hormigon-pigmentado` — gris cálido / terroso.
4. `listones-madera` — revestimiento vertical madera oscura.
5. `mixto` — base hormigón + volumen superior listones (default concurso).

Cada keeper suma su prompt de material a la biblioteca del estudio (`presets-escala-pequena-urbano.md`). Con el tiempo los adjetivos que funcionan quedan; los que derriten detalle se podan.

## 6. Iteración: cambios sobre la imagen anterior (dos modos, sin agente)

Modo A — global (re-estilo): la salida anterior entra como input img2img con denoise 0.5-0.65 + nuevo `estilo_muro` o `hora`. Cambia todo manteniendo masa.
Modo B — zona (máscara + texto): se pinta la zona sobre la misma foto + instrucción corta (`cambia este muro a listones de madera`). Solo esa zona cambia (F4). Sin máscara dibujada, el texto solo no localiza: la regla es *texto = qué, máscara = dónde*.

## 7. Puntos que pediste (respuesta directa)

- **Viewpoint / CameraAngleSelector y por qué decía "upgrade pod":** el selector + LoRA multi-ángulo exigen la base Qwen-Image-Edit-2511 (~20GB+, 24GB VRAM) — imposible en tu RX 570. Por eso el upgrade era pod. Para probar local ahora: YT-03 SDXL T1–T4 (±15°, low-angle, aérea, noche, denoise 0.55-0.7) sobre tu keeper. Mismo resultado práctico en giros chicos, $0.
- **Inpaint:** YT-01 (SDXL) + YT-03-alt (SD1.5 validado R4) listos; nodos y modelos existen en disco. Falta solo pintar máscara y encolar.
- **Cambio de sol:** IC-Light `fc` en disco (L1 backlog) — misma imagen, otra hora. Sin regenerar.
- **Marcar con cursor:** dos vías: máscara ComfyUI (opacidad ~75%, zona un poco más grande) o círculo/flecha roja sobre la foto + instrucción "el rojo es indicación, quítalo" (técnica módulo 3 [01:13:31]). La segunda no necesita abrir ComfyUI.
- **Sketch to render:** tienes los sketches + SD1.5 ausente — usar SDXL: scribble vía ControlNet SDXL simple o calco→RealVisXL denoise 0.4-0.6. Dual pesado (9.4GB) no entra local.
- **Upscale armado sin correr:** `proyectos/MVP_04-comfyui-arquitectura/n_09-upscale/workflow_upscale_esrgan.json` (LoadImage + UpscaleModelLoader RealESRGAN + ImageUpscaleWithModel + SaveImage), validado contra `/object_info`, sin encolar. En tu disco no corre full-res por VRAM: corre por mitades o queda para pod.
- **Imagen→3D sin nodo propietario:** el propietario es el nodo API Tripo (pago). Opción abierta: nodos `Tripo*`/`Hunyuan3D` ya visibles en tu `/object_info` vía ComfyUI-3D-Pack en pod, o `F-02 composit` (render + máscara sobre foto real, $0, control total). Para el concurso, F-02 rinde más que malla 3D.
- **Video:** no ahora (excede 8GB). Queda WF-04 LTX para pod.
- **Hermes vía Tailscale después:** Hermes hablará contra este mismo contrato (parámetros §2 + cola ComfyUI por API) a través de la red Tailscale. Nada del flujo cambia: hoy lo rellena la persona, mañana lo rellena Hermes. Tailscale solo es el cable seguro entre Telegram/Hermes y tu ComfyUI.

## 8. Gates

- G0: keeper `casa-base.png` mixto tarde eye-level (seed 42).
- G1: 4 estilos §5 misma seed/cámara + noche + low-angle.
- G2: 1 iteración modo A + 1 modo B registradas.
- G3: upscale JSON validado (hecho) + 1 prueba local por mitades.
