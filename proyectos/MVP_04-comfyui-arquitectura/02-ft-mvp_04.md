---
tipo: plan-tecnico
mvp: 04
version: 1.0.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [mvp_04, plan-tecnico, comfyui, mcp, instalacion]
---

# MVP 04 — Plan Técnico v1.0.0

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────┐
│                   PC del Estudio                      │
│                                                       │
│  ┌──────────┐    MCP (stdio)    ┌──────────────────┐ │
│  │ Opencode │ ◄──────────────► │ artokun/         │ │
│  │ (agente) │                   │ comfyui-mcp      │ │
│  └──────────┘                   │ (Node.js ≥22)    │ │
│                                 └────────┬─────────┘ │
│                                          │ HTTP       │
│                                 ┌────────▼─────────┐ │
│                                 │  ComfyUI          │ │
│                                 │  127.0.0.1:8188   │ │
│                                 │  v0.28.0          │ │
│                                 └────────┬─────────┘ │
│                                          │            │
│                          ┌───────────────┴───────┐    │
│                          │  Modelos / LoRAs       │    │
│                          │  C:\Users\Solch16\     │    │
│                          │  ComfyUI\models\       │    │
│                          └───────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

## Configuración del Entorno

### 1. ComfyUI (ya instalado)

**Ruta**: `C:\Users\Solch16\ComfyUI\`
**Versión**: 0.28.0
**GPU**: AMD 8GB (DirectML)

Para AMD con DirectML, ComfyUI necesita lanzarse con:
```bash
python main.py --directml
# o si usás el comfy-cli:
comfy launch -- --directml
```

Si hay problemas de memoria, agregar:
```bash
python main.py --directml --lowvram --gpu-only
```

### 2. MCP Server (artokun/comfyui-mcp)

Ya está operativo — se conecta a `http://127.0.0.1:8188`.

**Verificar conexión** desde Opencode:
```
comfyui_health_check  →  debe devolver GPU, versión, cola vacía
comfyui_list_local_models  →  lista los checkpoints instalados
```

### 3. Modelos mínimos requeridos

| Modelo | Tipo | VRAM | Propósito |
|--------|------|------|-----------|
| ArchitectureRealmix v1.1 | Checkpoint SD1.5 | ✅ instalado | Renders arquitectónicos generales |
| Z-Image Turbo GGUF Q4_K_S | Checkpoint (GGUF) | ~4GB | Turbo rápido para iteración |
| 4x_foolhardy_Remacri | Upscaler | ~100MB | Upscale 4x de renders |

Ver [[modelos-recomendados]] para descargas y configuración.

## Nivel 01: txt2img (Texto → Render)

### Workflow base: `workflow_txt2img_exterior.json`

```
[CLIP Text Encode] ──positivo──┐
                                ├──► [KSampler] ──► [VAE Decode] ──► [Save Image]
[CLIP Text Encode] ──negativo──┘          │
                                          │ seed: variable
[Checkpoint Loader] ──modelo──────────────┘ steps: 20-30
                                          cfg: 7
                                          sampler: euler
```

### Prompts arquitectura (test batch)

**Exterior:**
```
"modern architecture, concrete and glass facade, clean lines, 
minimalist design, photorealistic, architectural photography, 
soft natural lighting, 8K, highly detailed"
```

**Interior:**
```
"modern living room, floor-to-ceiling windows, warm wood accents, 
white walls, minimalist furniture, natural light, architectural 
photography, photorealistic, 8K"
```

**Parameter sweep recomendado:**
| Parámetro | Rango test | Default |
|-----------|-----------|---------|
| steps | 20-40 | 30 |
| cfg | 5-10 | 7 |
| sampler | euler, dpmpp_2m, dpmpp_sde | euler |
| scheduler | normal, karras, exponential | normal |
| seed | 5 variantes | random |

### Comando MCP para ejecutar

```
comfyui_generate_image(
  prompt="...",
  negative_prompt="low quality, blurry, distorted",
  checkpoint="architecturerealmix_v11.safetensors",
  width=1024, height=768,
  steps=30, cfg=7,
  sampler="euler",
  batch_size=4  # 4 variantes de seed
)
```

## Nivel 02: img2img (Croquis/Foto → Render)

### Workflow base: `workflow_croquis_a_render.json`

```
[Load Image] ──croquis──┐
                         ├──► [KSampler] ──► [VAE Decode] ──► [Save Image]
[CLIP Text Encode] ──────┘     │
                         denoise: 0.4-0.8
```

**Denoise por caso de uso:**
| Denoise | Efecto | Uso |
|---------|--------|-----|
| 0.3-0.4 | Cambio sutil de materiales/texturas | Iterar sobre render existente |
| 0.5-0.6 | Cambio de estilo manteniendo composición | Croquis → render conceptual |
| 0.7-0.8 | Reinvención manteniendo bordes | Croquis suelto → render |

### Flujo completo desde Opencode

```
1. User: "tomá este croquis y hace un render exterior moderno"
2. Agente: upload_image("activos/proyectos/X/croquis_01.jpg")
3. Agente: comfyui_generate_image(
     prompt="modern architecture...",
     control_image="croquis_01.jpg",  # img2img
     denoise=0.6,
     checkpoint="architecturerealmix_v11.safetensors"
   )
4. Output → activos/proyectos/X/renders/render_v01.png
5. User: "cambiá el concreto por piedra"
6. Agente: denoise=0.4, prompt modificado → render_v02.png
```

## Nivel 03: ControlNet (Control Geométrico)

### Depth ControlNet (desde modelo 3D)

Pipeline:
```
[Load Image] ──depth_map──┐
                           ├──► [ControlNet Apply] ──► [KSampler] ──► [Save]
[Preprocessor Depth] ─────┘           │
[CLIP Text Encode] ──prompt───────────┘
```

**Preprocesadores útiles para arquitectura:**
| Preprocesador | Uso | Input ideal |
|--------------|-----|-------------|
| Depth (MiDaS) | Preservar profundidad espacial | Render base / foto |
| Canny | Preservar líneas y bordes | Planta, corte, croquis |
| Lineart | Líneas exactas tipo plano | DWG export, CAD |
| MLSD | Líneas rectas (paredes, ventanas) | Fachadas, interiores |

**Strength recomendado:**
| ControlNet | Strength | Cuándo |
|-----------|----------|--------|
| Depth | 0.8-1.0 | Quiero mantener la forma 3D exacta |
| Canny | 0.6-0.9 | Quiero mantener bordes pero permitir relleno |
| Sketch | 0.5-0.7 | Croquis a mano alzada → render |
| MLSD | 0.7-0.9 | Fachadas, planos de elevación |

## Nivel 04: Video (Futuro)

Pipeline propuesto:
```
[Render] ──► [LTX-2.3 I2V] ──► [Walkthrough animado] ──► [Upscale 4x] ──► [RIFE interpolación]
```

Hardware requerido: 12GB+ VRAM (AMD), 24GB+ recomendado (NVIDIA).

## Nivel 05: Rhino MCP (Futuro)

```
[Rhino] ──MCP──► [Export view + depth] ──► [ComfyUI ControlNet] ──► [Render]
         ◄──MCP── [Update model based on render]
```

## ADRs Técnicos

### ADR-001: Backend GPU — AMD DirectML

**Contexto**: ComfyUI no detecta CUDA en AMD. Usa `privateuseone`.
**Decisión**: Usar `--directml` flag. Si hay nodos incompatibles, correr en CPU para esos pasos.
**Alternativa futura**: ROCm (Linux) o PyTorch DirectML backend mejorado.

### ADR-002: Formato de workflows

**Decisión**: Todos los workflows se guardan en formato API JSON (no UI).
**Razón**: AMV — el .json es el artefacto ejecutable. El formato UI incluye datos de layout que no aportan a la ejecución headless.

### ADR-003: Modelo primario vs secundario

**Decisión**: ArchitectureRealmix v1.1 como modelo primario (ya instalado, SD 1.5, fine-tuneado para arquitectura). Z-Image Turbo GGUF como secundario (turbo, <8GB).

## Referencias

- [[01-spec-mvp_04]] — Especificaciones
- [[modelos-recomendados]] — Guía de modelos
- [[wiki/estudio/adr-001-comfyui-mcp]] — ADR de adopción
- [artokun/comfyui-mcp docs](https://comfyui-mcp.artokun.io/docs)
- [ComfyUI AMD setup](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#amd-gpus)
