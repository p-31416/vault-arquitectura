---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, rhino, tiempo-real, controlnet, propio]
idioma: es
---

# YT-04 — Rhino vivo por captura manual (propio)

> Flujo propio, sin video de YouTube. Conecta Rhino 7/8 con ComfyUI en ciclo corto: modelás en Rhino, capturás la vista con `ViewCaptureToFile`, el flujo re-renderiza sobre la misma geometría. Sin MCP server por ahora; la captura manual es el disparador.

## 1. Qué hace

Toma la captura sombreada de Rhino, la ata con ControlNet canny SD1.5 (strength 0,85) y genera un render fotorrealista con el checkpoint SD1.5 liviano para la RX 570. Cada cambio en Rhino es una captura nueva + encolado. Stack 100% en disco, sin descargas.

## 2. JSON

- `workflow_YT-04-rhino-vivo.json` (misma carpeta): grafo en API format, listo para drag-and-drop.
- Entrada esperada en `ComfyUI/input/`: `geo_shaded.png` (captura sombreada 1:1 con la vista que querés renderizar).
- Captura desde Rhino (misma vista, fondo liso):
```cmd
_-ViewCaptureToFile _Enter "C:\out\geo_shaded.png" _Enter 2048 _Enter
```
- Copiar `C:\out\geo_shaded.png` a `ComfyUI/input/` antes de encolar.
- Checkpoint: `sd-v1-5-inpainting-fp16.safetensors` + `control_v11p_sd15_canny.safetensors` (ambos en disco, pareja SD1.5 coherente).
- Validación R4 2026-11-03: `class_type` y widgets contra `/object_info` del server local, checkpoint y ControlNet contra `models/`. Único pendiente: `geo_shaded.png` se resuelve al copiar tu captura.

## 3. Modelo

| Pieza | Dato | Link / estado |
|---|---|---|
| Checkpoint | `sd-v1-5-inpainting-fp16.safetensors` (SD1.5) | en disco `models/checkpoints/` |
| ControlNet | `control_v11p_sd15_canny.safetensors` (SD1.5) | en disco `models/controlnet/` |
| Base | SD1.5 | corre holgado en la RX 570 local |
| Alternativa SDXL | Juggernaut v9 + `XL_controlnet-union-sdxl-1.0` promax | https://huggingface.co/xinsir/controlnet-union-sdxl-1.0 — pendiente de descarga, mejor detalle |

## 4. Nodos y docs oficiales

| # | Nodo | Doc | Función en este flujo |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga SD1.5; salidas MODEL/CLIP/VAE |
| 2 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Captura sombreada de Rhino |
| 3 | `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | Reescala a 512×512 (bilinear, center) [R1] |
| 4 | `ControlNetLoader` | [doc](https://docs.comfy.org/built-in-nodes/ControlNetLoader) | Carga canny SD1.5 |
| 5 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: render fotorrealista misma masa |
| 6 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo de la casa |
| 7 | `ControlNetApplyAdvanced` | [doc](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced) | Ata geometría: strength 0,85, 0–100% |
| 8 | `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Captura → latente |
| 9 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` + `karras`, 25 steps, cfg 7, denoise 0,85, seed 7 |
| 10 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 11 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-YT04-rhino-vivo` |

```
2 ─ IMAGE ─→ 3 ─┬→ 7 (control) ─→ 9 ─→ 10 ─→ 11
                └→ 8 ─ latent ─→ 9
1 ─ MODEL ─→ 9 · 1 ─ CLIP ─→ 5/6 ─→ 7 ─→ 9 (+/−) · 1 ─ VAE ─→ 8/10 · 4 ─ CN ─→ 7
```

## 5. Cómo se usa (loop vivo)

1. En Rhino fijar la vista y capturar a `C:\out\geo_shaded.png` (misma cámara siempre).
2. Copiar a `ComfyUI/input/geo_shaded.png` (sobrescribe la anterior).
3. Encolar. Salida: `gx-YT04-rhino-vivo`.
4. Mover la geometría en Rhino → repetir 1–3. Mismo seed = misma atmósfera entre iteraciones.

## 6. Cuadro de pruebas

Una variable por corrida; el resto del grafo intacto.

| # | Prueba | Cambio en Rhino | Denoise | Qué mirar |
|---|---|---|---|---|
| T1 | Baseline masa | volumen simple sin mover cámara | 0,85 | respeta silueta, material creíble |
| T2 | Mover ventana | desplazar un vano | 0,85 | el vano renderizado sigue al modelo |
| T3 | Strength bajo | misma captura | 0,6 | cuánta libertad toma el render |
| T4 | Strength alto | misma captura | 1,0 | geometría rígida, posible posterizado |

Escalera de strength si ignora la geometría: 0,6 → 0,85 → 1,0. Variante de modelo: repetir T1 en SDXL cuando bajes la unión promax.

## 7. Pendientes

- Primera captura real desde tu Rhino y corrida T1, registrada en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|reporte de corridas]].
- Watcher de carpeta `rhino-vivo/` + Grasshopper depth/normal cuando el loop manual quede corto (backlog de [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/README|n_05-rhino-mcp]]).
- Investigar Rhino MCP server dedicado para disparo automático.

## Referencias

- Flujo Rhino-to-Image del curso: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README|WF-rhino-to-image]]
- Nivel Rhino MCP: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/README|n_05-rhino-mcp]]
- Matriz del concurso: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|00-matriz-pruebas-concurso]]
