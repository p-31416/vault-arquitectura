---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, juggernaut, modelo-base, nodos, licencia]
idioma: es
---

# Base común de los 7 WF SDXL — modelo, nodos y reglas

> Documento de lectura. Cubre lo que comparten [[#Los 7 flujos]]. Cada WF tiene su ficha propia (WF-01 a WF-07). Ningún flujo fue validado contra servidor: la R4 (`/object_info`) sigue pendiente.

## 1. El modelo

**Juggernaut XL v9 — RunDiffusion Photo v2**, checkpoint SDXL de fotorrealismo, co-desarrollado por KandooAI y RunDiffusion.

| Dato | Valor |
|---|---|
| Archivo | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` |
| Tamaño | 7,11 GB |
| Carpeta | `ComfyUI/models/checkpoints/` |
| Licencia | CreativeML Open RAIL-M (uso comercial permitido, con restricciones de uso del anexo) |
| VAE | **Incluido en el checkpoint** — se toma del slot 2 del loader |
| SHA256 | `c9e3e68f89b8e38689e1097d4be4573cf308de4e3fd044c64ca697bdb4aa8bca` |

Links (verificados 2026-11-02, HTTP 200):

- Hugging Face: https://huggingface.co/RunDiffusion/Juggernaut-XL-v9
- Civitai: https://civitai.com/models/133005/juggernaut-xl
- Ficha Comfy Hub: https://comfy.org/hub/models/local/juggernaut-xl-v9-rundiffusionphoto-v2
- Descarga directa: https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors

### Ajustes recomendados por el autor

| Parámetro | Valor |
|---|---|
| Resolución | 1216×832 (horizontal) · 832×1216 (vertical) |
| Sampler | DPM++ 2M Karras (`dpmpp_2m` + `karras`) |
| Steps | 30–40 |
| CFG | 3–7 (más bajo = más realismo) |
| Negativo | arrancar liviano; los negativos largos suelen restar |
| Hi-Res fix | 4xNMKD-Siax_200k · 15 steps · denoise 0,3 · 1,5× |

Los 7 WF usan `cfg 4` y `dpmpp_2m`/`karras`, dentro del rango recomendado. `cfg 4` es el punto bajo: gana realismo y pierde obediencia al prompt.

## 2. Nodos compartidos

Todos los flujos arman el grafo con estos nodos nativos. Documentación oficial de cada uno:

| Nodo | Documentación | Qué hace en estos WF |
|---|---|---|
| `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga el checkpoint y expone tres salidas: MODEL (0), CLIP (1), VAE (2) |
| `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Convierte texto en conditioning. Dos instancias: positivo (2) y negativo (3) |
| `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | Lienzo vacío de ruido; define ancho, alto y batch. Solo en txt2img |
| `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | El motor: agrega ruido según seed y denoise, y lo quita en `steps` pasos guiado por el modelo y los dos conditioning |
| `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles. Usa el VAE del slot 2 del checkpoint |
| `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Guarda el PNG con `filename_prefix`; el prefijo `gx-` ordena la salida del concurso |
| `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Abre una imagen del `input/`. Presente en WF-03 y WF-07 |
| `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | Redimensiona a 1024² con `bilinear` y `crop: center` antes de codificar |
| `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Píxeles → latente. Reemplaza a `EmptyLatentImage` en los img2img |

## 3. Anatomía de los dos tipos

**txt2img** (WF-01, 02, 04, 05, 06):

```
CheckpointLoaderSimple ─┬─ MODEL ─────────────────→ KSampler ─→ VAEDecode ─→ SaveImage
                        ├─ CLIP  ─→ CLIPTextEncode(+) ─┘        ↑
                        ├─ CLIP  ─→ CLIPTextEncode(−) ─┘        │
                        └─ VAE ──────────────────────────────────┘
EmptyLatentImage ─── latent ───────────────────────→ KSampler
```

**img2img** (WF-03, WF-07):

```
LoadImage ─→ ImageScale(1024²) ─→ VAEEncode ─→ KSampler(denoise < 1) ─→ VAEDecode ─→ SaveImage
```

La única diferencia real entre los dos es de dónde sale el latente y el valor de `denoise`. Todo lo demás es idéntico.

## 4. Cambios que aplican a los siete

| Quiero | Cómo | Efecto | Cuidado |
|---|---|---|---|
| Otra relación de aspecto | `EmptyLatentImage` con lados múltiplos de 64 | SDXL rinde en ~1 MP: 1216×832, 1024×1024, 1280×768 | Bajar de 768 px de lado mayor degrada la composición |
| Más de una imagen | `batch_size` en `EmptyLatentImage` | Una corrida, N salidas | Cada imagen suma VRAM; en 8 GB conviene batch 1 |
| Otra composición | `seed` | Cambio total de la escena | Con seed fija el grafo repetido devuelve el mismo PNG (caché) |
| Más detalle | `steps` 30 → 40 | Microdetalle | Sobre 45 el costo sube y la ganancia se aplana |
| Más obediencia al texto | `cfg` 4 → 6–7 | Respeta mejor el prompt | Pierde el aire fotográfico; sobre 8 aparecen artefactos |
| Otra estética de muestreo | `sampler_name` / `scheduler` | `euler`+`normal` da un resultado más limpio; `dpmpp_2m_sde`+`karras`, más textura | Conviene cambiar de a una variable y comparar con la misma seed |
| Estilo propio | Insertar `LoraLoader` entre el checkpoint y el sampler | Aplica un LoRA sin tocar el modelo | Documentación: https://docs.comfy.org/built-in-nodes/LoraLoader |
| Composición forzada | Insertar `ControlNetLoader` + `ControlNetApplyAdvanced` | La geometría la manda la imagen de control | Suma ~1,2 GB de VRAM por modelo de control |
| Nitidez final | Agregar `UpscaleModelLoader` + `ImageUpscaleWithModel` | Sube resolución sin re-muestrear el latente | Es el camino correcto: el `LatentUpscale` con denoise bajo solo interpola |

## 5. Reglas de campaña (heredadas de la matriz)

1. Una variable por corrida; seed registrada.
2. Toda corrida que entra a la matriz suma: PNG + `.json` + fila en `curso.json` + segundos medidos.
3. `≤1024 px` de lado mayor cuando el VAE corre en CPU (caso RX 570 con `--cpu-vae`).
4. Cambio de seed obligatorio para forzar una corrida nueva (ComfyUI cachea grafos idénticos).

## Los 7 flujos

| WF | Ficha | Tipo |
|---|---|---|
| WF-01 | `WF-01_sdxl.md` | txt2img 1024² — baseline |
| WF-02 | `WF-02_sdxl.md` | txt2img 1216×832 — interior bóveda |
| WF-03 | `WF-03_sdxl.md` | img2img 0,65 — Rhino → render |
| WF-04 | `WF-04_sdxl.md` | txt2img 1280×768 — keyframe de video |
| WF-05 | `WF-05_sdxl.md` | txt2img 1024² — maqueta para 3D |
| WF-06 | `WF-06_sdxl.md` | txt2img 1024² — detalle constructivo |
| WF-07 | `WF-07_sdxl.md` | img2img 0,55 — geometría → piedra |

## Referencias

- Índice del set: [[proyectos/concurso-gaudi-nexus/WF-curso/01-index-sdxl-vista|sdxl-vista]]
- Matriz de pruebas: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz del concurso]]
- Modelos recomendados: [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|v1.4.0]]
- Otros SDXL a probar + LoRA del curso: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]
- Análisis de alternativas: [[wiki/estudio/analisis/analisis-ia-generativa-comfyui-alternativas|análisis IA generativa]]
- Proveedores y tiers gratis: [[wiki/glosario/software/proveedores-modelos-ia|proveedores-modelos-ia]]
- Plan de pruebas: [[specs/261030-plan-continuacion-pruebas|plan de continuación de pruebas]]
