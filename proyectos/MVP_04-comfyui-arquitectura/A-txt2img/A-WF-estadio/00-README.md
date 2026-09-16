---
tipo: flujo
workflow: WF-estadio
nivel: n_01-txt2img
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-24
tags: [estadio, txt2img, arquitectura, sd15, architecture-realmix]
estado: activo
---

# 00-README — Navegación y Uso del Flujo WF-estadio

**Workflow SD 1.5:** `workflow_txt2img_estadio.json`  
**Workflow SDXL (migración):** `workflow_txt2img_estadio_sdxl.json`  
**Modelo SD 1.5:** ArchitectureRealmix v1.1 (`architecturerealmix_v11.safetensors`, ~2 GB)  
**Modelo SDXL:** Juggernaut XL v9 (`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`, 7.11 GB)  
**Hardware:** AMD RX 570 8GB VRAM (DirectML)

---

## Estructura de la carpeta

| Archivo / Carpeta | Descripción | Orden |
|-------------------|-------------|-------|
| `00-README.md` | **Este archivo** — Guía de navegación y uso | 1 |
| `01-index.md` | Catálogo de versiones, nomenclatura, configuraciones mínimas | 2 |
| `02-WF-log-WFestadio.md` | Log detallado de **todas las corridas** (extensión del index) | 3 |
| `03-nodos-WFestadio.md` | Detalle de nodos y **configuraciones propias** del flujo | 4 |
| `04-backlog.md` | Pruebas pendientes, ideas, sugerencias de iteración | 5 |
| `salidas/` | Imágenes generadas, **nomencladas** `n_01-{L}-{NN}.png` | 6 |
| `PLANS/` | Planes de test, comparativas, migraciones (archivos `.md`) | 7 |
| `SPECS/` | Especificaciones técnicas, requisitos, decisiones de diseño | 8 |
| `workflow_txt2img_estadio.json` | Workflow SD 1.5 (API format) — **archivo fuente** | 9 |
| `workflow_txt2img_estadio_sdxl.json` | Workflow SDXL Juggernaut XL (API format) — **archivo fuente** | 10 |

---

## Convención de nomenclatura de salidas

```
n_01-{LETRA}-{NN}.png
```

| Letra | Significado | Ejemplo |
|-------|-------------|---------|
| **A** | Baseline absoluto (3 corridas idénticas, sin cambios) | `n_01-A-01.png` |
| **B** | Variación de **prompt** (atmósfera, estilo, materiales) | `n_01-B-01.png` |
| **C** | Exploración de **parámetros** (cfg, sampler, scheduler, steps) | `n_01-C-01.png` |
| **D** | Migración de **modelo** (ej. SD 1.5 → SDXL) | `n_01-D-01.png` |
| **E** | Variación de **resolución / aspect ratio** | `n_01-E-01.png` |
| **F** | Test de **ControlNet / img2img** | `n_01-F-01.png` |

> **Regla:** Cada corrida registrada en `02-WF-log-WFestadio.md` debe tener su archivo en `salidas/` con el mismo ID.

---

## Cómo usar este flujo

### 1. Preparar entorno
```bat
# SD 1.5 (ArchitectureRealmix) — flags normales
.\corre_comfyui.bat
# Debe incluir: --directml 0 --force-fp16 --disable-cuda-malloc

# SDXL (Juggernaut XL) — flags OBLIGATORIOS 8GB
.\corre_comfyui_sdxl.bat
# Debe incluir: --lowvram --cpu-vae --directml 0 --force-fp16 --disable-cuda-malloc
```

### 2. Cargar workflow
- **SD 1.5:** Arrastrar `workflow_txt2img_estadio.json` a ComfyUI
- **SDXL:** Arrastrar `workflow_txt2img_estadio_sdxl.json` a ComfyUI
- Verificar nodo 1 (CheckpointLoaderSimple) → modelo correcto

### 3. Ejecutar baseline (versión A)
| Parámetro | SD 1.5 | SDXL |
|-----------|--------|------|
| Seed | 42 | 42 |
| Steps | 30 | 35 |
| CFG | 7 | 4 |
| Sampler | euler | dpmpp_2m |
| Scheduler | normal | karras |
| Resolution | 768×512 | 1216×832 |
| Batch | 1 | 1 |

- Queue Prompt → output: `estadio_futbol_XXXXXX_.png` (SD 1.5) / `estadio_sdxl_juggernaut_XXXXXX_.png` (SDXL)
- Copiar a `salidas/n_01-A-01.png`
- Registrar en `02-WF-log-WFestadio.md` y `01-index.md`

### 4. Iterar (B, C, D, E, F)
- Cambiar **una sola variable** por corrida
- Actualizar seed si corresponde
- Queue → copiar a `salidas/` → registrar en log e index

### 5. Documentar
- **01-index.md**: Tabla de versiones + configs mínimas
- **02-WF-log-WFestadio.md**: Detalle completo (prompt, neg, seed, tiempo, VRAM, observaciones)
- **03-nodos-WFestadio.md**: Solo configs propias del flujo (no repetir glosario)
- **04-backlog.md**: Qué probar después

---

## Referencias cruzadas (hipervínculos)

- `01-index.md` ↔ `02-WF-log-WFestadio.md` (cada versión link a su log)
- `03-nodos-WFestadio.md` → `wiki/glosario/software/comfyui.md` (nodos genéricos)
- `PLANS/comparativa-sd15-vs-sdxl.md` — Plan comparativa SD 1.5 vs SDXL
- `SPECS/` — Especificaciones técnicas si aplica

---

## Glosario de nodos (referencia)

| Nodo | Clase | Documentación genérica |
|------|-------|------------------------|
| CheckpointLoaderSimple | `CheckpointLoaderSimple` | [[wiki/glosario/software/comfyui|checkpoint-loader]] |
| CLIPTextEncode (pos/neg) | `CLIPTextEncode` | [[wiki/glosario/software/comfyui|clip-text-encode]] |
| EmptyLatentImage | `EmptyLatentImage` | [[wiki/glosario/software/comfyui|empty-latent-image]] |
| KSampler | `KSampler` | [[wiki/glosario/software/comfyui|k-sampler]] |
| VAEDecode | `VAEDecode` | [[wiki/glosario/software/comfyui|vae-decode]] |
| SaveImage | `SaveImage` | [[wiki/glosario/software/comfyui|save-image]] |

> **Nota:** El detalle de configuración **propia de este flujo** está en `03-nodos-WFestadio.md`. Lo genérico va al glosario.