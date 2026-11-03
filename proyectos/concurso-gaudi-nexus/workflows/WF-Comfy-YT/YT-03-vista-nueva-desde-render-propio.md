---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, sdxl, img2img, vista-nueva, propio]
idioma: es
---

# YT-03 — Cambiar punto de vista desde render propio (propio)

> Flujo propio, sin video de YouTube. Toma un render fotorrealista y genera la misma obra desde un punto de vista cercano (±10-15°), manteniendo materiales, luz y sombras. Pensado para probar variantes de cámara de concurso sin remodelar.

## 1. Qué hace

Re-encuadre controlado por img2img con SDXL: el render entra, se escala a 512, se re-muestrea con denoise medio y un positivo que describe la cámara nueva. Denoise 0,65 conserva identidad con libertad suficiente para mover la cámara. Giro grande (+30°) queda para vía RunPod con 3D real.

## 2. JSON

- `workflow_YT-03-vista-nueva.json` (misma carpeta): grafo mínimo en API format, listo para drag-and-drop.
- Entrada esperada en `ComfyUI/input/`: tu render como `PONER-RENDER-PROPIO.png` (idealmente ya 512; si es de otra medida el `ImageScale` lo centra).
- Checkpoint del flujo: `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (instalado local, corre en RX 570).
- Validación R4 2026-11-03: `class_type` y widgets contra `/object_info` del server local, checkpoint contra `models/checkpoints/`. Único pendiente: el nombre del LoadImage se resuelve al subir tu render.

## 3. Modelo

| Pieza | Dato | Link / estado |
|---|---|---|
| Checkpoint | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (SDXL 1.0) | en disco `models/checkpoints/` |
| Base | SDXL 1.0, entrenado a 1024×1024 | corre en la RX 570 local; a 512 rinde más suave y con menos detalle fino (4× menos píxeles por paso, notablemente más rápido) — la referencia de calidad queda en la corrida 1024 |
| ControlNet | `XL_controlnet-union-sdxl-1.0` promax + `DepthAnythingPreprocessor` (comfyui_controlnet_aux), strength 0,15 | https://huggingface.co/xinsir/controlnet-union-sdxl-1.0 — rama opcional, pendiente de descarga |
| IPAdapter | `ip-adapter-plus_sdxl_vit-h` + CLIP-Vision para atar identidad | en disco `models/ipadapter/` · `models/clip_vision/` — rama opcional |
| Licencia checkpoint | Open RAIL-M + cláusula RunDiffusion | ver §2 de [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] |

El JSON corre sin LoRA ni ControlNet para que valide tal cual; la unión SDXL y el IPAdapter se agregan como paso opcional cuando el relleno ignore la morfología.

## 4. Nodos y docs oficiales

| # | Nodo | Doc | Función en este flujo |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga Juggernaut; salidas MODEL/CLIP/VAE |
| 2 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Render propio base |
| 3 | `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | Reescala a 512×512 (lanczos, center): tope de velocidad en RX 570; SDXL rinde pleno a 1024, a 512 entrega vista de prueba más suave |
| 4 | `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Render → latente con el VAE del checkpoint |
| 5 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: misma obra + cámara nueva |
| 6 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo de la casa |
| 7 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` + `karras`, 30 steps, cfg 4, denoise 0,65, seed 7 |
| 8 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 9 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-YT03-vista` |

Extensiones opcionales (no incluidas en el JSON): `LoraLoader` ([doc](https://docs.comfy.org/built-in-nodes/LoraLoader)) con LoRA de archviz entre nodo 1 y 7; `ControlNetLoader` + `ControlNetApplyAdvanced` ([doc](https://docs.comfy.org/built-in-nodes/ControlNetLoader) · [doc](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)) con conditioning positivo/negativo para atar la vista nueva a la morfología.

```
2 ─ IMAGE ─→ 3 ─→ 4 ─ latent ─→ 7 ─→ 8 ─→ 9
1 ─ MODEL ─→ 7 · 1 ─ CLIP ─→ 5 ─→ 7 (+) · 1 ─ CLIP ─→ 6 ─→ 7 (−) · 1 ─ VAE ─→ 4/8
```

## 5. Cómo se usa (3 pasos)

1. Copiar tu render a `ComfyUI/input/` con el nombre `PONER-RENDER-PROPIO.png` (o ajustar el widget del nodo 2).
2. Editar el positivo del nodo 5 con la cámara deseada (izquierda/derecha, picado/contrapicado, altura de ojos).
3. Encolar. Salida: `gx-YT03-vista`.

## 6. Cuadro de pruebas

Una variable por corrida; el resto del grafo intacto.

| # | Prueba | Prompt + (extracto) | Denoise | Qué mirar |
|---|---|---|---|---|
| T1 | 15° a la izquierda | "same building, same materials, new viewpoint 15 degrees to the left, eye-level" | 0,65 | misma obra, cámara movida, sombras coherentes |
| T2 | Contrapicado leve | "same building, low angle view from below, looking up" | 0,6 | verticales a plomo, sin deformar masa |
| T3 | Vista aérea leve | "same building, slightly elevated three-quarter view" | 0,7 | cubierta creíble, entorno continuo |
| T4 | Noche misma cámara | "same viewpoint, night, warm interior light" | 0,55 | conserva encuadre, cambia solo la luz |

Escalera de denoise si pierde identidad: 0,5 (conservador) → 0,65 → 0,8 (libre). Variante de modelo: repetir T1 con RealVisXL v5.0.

## 7. Pendientes

- Probar T1 con tu render propio y registrar en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|reporte de corridas]] con segundos y veredicto.
- Descargar `controlnet-union-sdxl-1.0` promax para la rama ControlNet opcional cuando el relleno ignore la morfología.
- Evaluar vía RunPod con 3D real (Tripo/Hunyuan) para giros mayores a 30°.

## 8. Upgrade: giro real de cámara (Qwen + CameraAngleSelector)

> Camino documentado, pendiente de instalación. El img2img SDXL de arriba cubre pruebas rápidas de cámara en local; este upgrade entrega giro real de punto de vista con control preciso de 96 poses.

**Cómo funciona**: el nodo 3D `ComfyUI_CameraAngleSelector` arma el prompt de cámara y el LoRA de múltiples ángulos ejecuta el giro sobre Qwen-Image-Edit-2511. Formato: `<sks> [azimut] [elevación] [distancia]`, ej. `<sks> front-right quarter view eye-level shot medium shot`. 8 direcciones × 4 alturas (low −30° · eye-level · elevated 30° · high 60°) × 3 planos (close-up · medium · wide).

| Pieza | Dato verificado 2026-11-03 | Estado |
|---|---|---|
| Nodo selector 3D | https://github.com/NickPittas/ComfyUI_CameraAngleSelector (124 stars, instala por git URL en `custom_nodes/` + restart) | pendiente de instalación |
| LoRA multi-ángulo | https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA (Apache-2.0, trigger `<sks>`, strength 0,8–1,0, entrenado con 3000+ renders Gaussian Splatting) | pendiente de descarga |
| Modelo base | `Qwen/Qwen-Image-Edit-2511` | pendiente de descarga, corre en pod |
| Workflow de referencia | `comfyui-workflow-multiple-angles.json`, incluido en el repo del LoRA | pendiente de adaptar a `gx-YT03-vista` |

**Al activarlo**: instalar el nodo, bajar base + LoRA al pod, importar el workflow de referencia con nuestro render y registrar la primera corrida multi-ángulo en el reporte. En local queda solo documentado: Qwen-Image-Edit excede la RX 570.

## Referencias

- Set SDXL solo-vista: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/01-index-sdxl-vista|WF-curso]]
- Matriz del concurso: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|00-matriz-pruebas-concurso]]
- Inpainting oficial ComfyUI: https://docs.comfy.org/tutorials/basic/inpaint
- Nodo Camera Angle Selector (upgrade §8): https://github.com/NickPittas/ComfyUI_CameraAngleSelector
- LoRA multi-ángulo Qwen-Image-Edit-2511 (upgrade §8): https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA
