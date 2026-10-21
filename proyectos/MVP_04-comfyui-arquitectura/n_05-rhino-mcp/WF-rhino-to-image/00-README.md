---
tipo: proyecto
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, workflow, flux2, klein, lora, gaudi, rhino-to-image]
---

# WF-rhino-to-image — «Rhino-to-Image» con FLUX.2 [klein] 9B

> Flujo del módulo 3 del curso "AI×Gaudí" (Archademy / Fundació Antoni Gaudí): convierte una volumetría 3D de Rhino en render fotorrealista conservando la geometría en su sitio, usando el LoRA `rhino-to-image-lora.basic.safetensors` sobre FLUX.2 [klein] 9B.

## Qué hace

Toma dos imágenes de referencia (la **volumetría** capturada desde Rhino y una **foto de material real**), las pasa a latentes de referencia con el mecanismo nativo de FLUX.2, y genera un render fotorrealista donde la geometría se mantiene en su posición.

## El pipeline real del curso (3 pasos)

El tablero de workflows del curso (`AI-course.csv`, 219 filas) revela que **no es un paso, son tres**:

```
1. CAPTURAR   Rhino, captura EN COLOR → verde = vegetación, rosa = figuras
2. ARCILLA    INSTRUCTION.md (módulo 7) → la volumetría se reinterpreta en ARCILLA
              MONOCROMA con la lógica constructiva de Gaudí (dial 0-10, por defecto 7)
3. HIPERREAL  FLUX.2 klein 9B + LoRA rhino-to-image + prompt JSON con STRICT CAMERA LOCK
```

Del texto del curso: *"The clay is the base for the edit LoRA: keep it clean, monochrome, edge-legible, camera + footprint 1:1."*

| Prompt del curso (copiado al vault) | Qué hace |
|--------------------------------------|----------|
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|prompt-rhino-to-image-instruction-md]] | Convierte (volumetría + foto de material) en prompt JSON; pide tipo de edificio y ubicación |
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md|prompt-rhino-to-gaudi-instruction-md]] | Reinterpreta la geometría en arcilla con la lógica de Gaudí (variante B, nombra a Gaudí) |
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|prompt-rhino-to-image-esqueleto-json]] | La plantilla JSON de salida (la que va al CLIPTextEncode) |

## Orden de lectura

| Archivo | Contenido |
|---------|-----------|
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/01-index|01-index.md]] | Versiones, configs mínimas, precondiciones |
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/02-WF-log-WFrhino_to_image|02-WF-log-WFrhino_to_image.md]] | Log de corridas (se escribe al correr) |
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/03-nodos-WFrhino_to_image|03-nodos-WFrhino_to_image.md]] | Configs propias del flujo (lo genérico está en el glosario) |
| [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/04-backlog|04-backlog.md]] | Pendientes y experimentos |

## Fichas de referencia

- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — ficha del LoRA (rank 16, F32, 176 tensores, salud de pesos, licencia)
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — modelo base, stack de instalación, arquitectura
- [[wiki/glosario/software/comfyui|comfyui]] — nodos y catálogo de modelos
- [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] — informe con 54 fuentes verificadas

## Estado

| Ítem | Estado |
|------|--------|
| Workflow (API format) | ✅ `workflow_rhino_to_image.json` — construcción validada contra el código de ComfyUI local (`b08e6cf3`), pendiente de validación en vivo con el server |
| LoRA en `models/loras/` | ⬜ Pendiente de copia desde el Drive de Emilia |
| Stack FLUX.2 (9B + TE + VAE) | ⬜ Pendiente (RunPod 24 GB) |
| Imágenes de referencia | ⬜ Pendiente de exportar desde Rhino |
| Trigger word | ⬜ A confirmar con el instructor del curso |
| Primera corrida | ⬜ Pendiente |

## Precondiciones antes de la primera corrida

1. **Modelos instalados** (ver [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] para los comandos de descarga).
2. **LoRA copiado** a `P:\00-repos\ComfyUI\models\loras\`.
3. **Referencias exportadas desde Rhino** con la misma cámara y las 3 pasadas:

```cmd
:: Rhino — 3 pasadas desde la misma vista, fondo liso
_-ViewCaptureToFile _Enter "C:\out\geo_shaded.png" _Enter 2048 _Enter
_-ViewCaptureToFile _Enter "C:\out\geo_lines.png"  _Enter 2048 _Enter
```

4. **Foto de material real** en `C:\out\material.jpg` (ladrillo, hormigón o cerámica del proyecto).
5. Las dos imágenes cargadas en `ComfyUI/input/` con los nombres `geo_shaded.png` y `material.jpg`.

## Ejecución

En el pod (RunPod con ComfyUI + CUDA): subir el LoRA a `models/loras/`, abrir ComfyUI, `Load` → importar `workflow_rhino_to_image.json`, ajustar `strength_model` y el prompt, y `Queue`.

En local (RX 570 8 GB, DirectML): posible con offload del text encoder a RAM; el tiempo por imagen sube a minutos.

```cmd
P:\Anaconda\envs\comfyenv\python.exe -s P:\00-repos\ComfyUI\main.py --directml --disable-dynamic-vram --reserve-vram 1.0
```

## Calibración en 4 corridas (mismo seed)

| Corrida | `strength_model` | Referencia de material | Pregunta que responde |
|---------|------------------|-----------------------|----------------------|
| A | 0,0 (nodo puenteado) | sí | ¿Cuánto aporta la referencia? |
| B | 0,6 | sí | ¿El LoRA aporta materialidad? |
| C | 0,8 | sí | Punto óptimo de trabajo |
| D | 1,0 | sí | ¿Satura? |

Después: misma matriz con la **variante base** (steps 20, cfg 5) para confirmar en qué variante se entrenó el LoRA.

Nomenclatura de salidas: `n_05-{A|B|C|D}-{NN}.png` en `salidas/`.
