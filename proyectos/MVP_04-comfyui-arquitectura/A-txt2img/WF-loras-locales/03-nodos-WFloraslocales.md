---
tipo: nodos
workflow: WF-loras-locales
nivel: n_01-txt2img
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [nodos, lora, loraloader, trigger, rx570]
---

# 03-nodos — WF-loras-locales

Configs **propias** de este flujo. Lo genérico (KSampler, VAEDecode, CheckpointLoader) está en [[wiki/glosario/software/comfyui|comfyui]].

---

## Grafo

```
CheckpointLoaderSimple ──model(0)──┐
    ├──clip(1)──────────────────┐  │
    └──vae(2)───────────────┐  │  │
                            │  │  │
LoraLoader ◄───────────────┘  │  │   inputs: lora_name, strength_model, strength_clip
    ├──model(0)──────────────┼──┼──┐
    └──clip(1)───────────────┘  │  │
                                │  │
CLIPTextEncode (pos) ◄───────────┘  │   text = "{trigger}, {prompt_base}"
CLIPTextEncode (neg) ◄──────────────┘   text = negative
                                 │
EmptyLatentImage ──────────────────┤
        │                           │
        └────────► KSampler ◄───────┘
                      │
                   VAEDecode (vae ← checkpoint, salida 2)
                      │
                   SaveImage (prefix = loras/n_01-G-NN)
```

## `LoraLoader` — las dos cosas que importan

1. **Va entre el checkpoint y el sampler.** Si se coloca después del `KSampler` no fusiona nada; si se coloca antes del `CheckpointLoader`, el checkpoint no existe todavía.
2. **Los `CLIPTextEncode` cuelgan de la salida 1 del LoRA**, no de la salida 1 del checkpoint. Así el *texto* también recibe el LoRA. Si colgaran del checkpoint, el LoRA solo_MODEL_ (la imagen) y el prompt no se activaría.

| Input | Valor | Nota |
|---|---|---|
| `lora_name` | nombre exacto del `.safetensors` | con extensión |
| `strength_model` | 0,6 / 0,8 | misma cifra que `strength_clip` en esta calibración |
| `strength_clip` | 0,6 / 0,8 | a 1,0 los LoRAs de estilo saturan el texto |

## Mapa de triggers

| Archivo | Trigger en el prompt |
|---|---|
| `JJ_Archvizcg_v2.safetensors` | `archviz` |
| `sandiese.safetensors` | `architecture, building, grey_background` |
| `xsarchitectural-10superhighrisebuilding.safetensors` | `architectural renderings, bird's-eye view` |
| `room.safetensors` | `room` |
| `landscape_architecture_sketch.safetensors` | `sketch, architecture, building` |
| `Le Corbusier 2.2.7.2_sd1.5-000016.safetensors` | `zhuai_pb, brutalism` |
| `BrutalistTech-20.safetensors` | `brutaltech, cement` |
| `archisketch-v1.safetensors` | `linear` |
| `markerhandsketch-V1.safetensors` | `marker painting, handsketch` |
| `Architectural_Massing.safetensors` | — (sin trigger publicado) |
| `Architecture_Building.safetensors` | — |
| `ArcvizXL_V01.safetensors` | `archviz 1` |
| `bookstore-xl.safetensors` | `mrares, bookstore` |
| `isometric-v1.safetensors` | `isometric style` |
| `SLskyscraperrenderingXL_V1.0.safetensors` | — |
| `baroque_architecture-000006.safetensors` | — |

> **Error ya cometido una vez (2026-10-28):** el primer grafo encolado usaba el *nombre del archivo* en el prompt (`"JJ_Archvizcg_v2.safetensors, architecturerealmix style..."`). El trigger va en el prompt; el nombre del archivo, solo en el widget `lora_name`.

## Notas de VRAM en el RX 570

- Los LoRAs **rank 128** (`ArcvizXL_V01`, `bookstore-xl`, `SLskyscraperrenderingXL`) son los que miden el techo real: son los que pueden hacer fallar el render con OOM.
- `--cpu-vae` + `--lowvram` son obligatorios para SDXL con LoRA rank 128.
- Si un render falla, `PLANS/calibracion-loras.json` lo registra con `error` y la tanda continúa.

## Referencias

- [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] — catálogo con base, rank y tamaño
- `scripts/calibrar-loras-comfyui_notas.md` — el grafo explicado línea por línea
