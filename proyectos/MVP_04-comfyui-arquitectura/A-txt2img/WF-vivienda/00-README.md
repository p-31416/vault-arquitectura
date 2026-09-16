---
tipo: readme
workflow: WF-vivienda
nivel: n_01-txt2img
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [readme, navegacion, vivienda, txt2img, sdxl]
---

# 00-README — Guía de Navegación WF-vivienda

**Flujo:** txt2img vivienda unifamiliar — SDXL (Juggernaut XL v9)  
**Nivel:** n_01-txt2img  
**Modelo:** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`  
**Hardware:** AMD RX 570 8GB VRAM — `--lowvram --cpu-vae` obligatorio

---

## Estructura de la carpeta (orden de lectura)

```
WF-vivienda/
├── 00-README.md                    â† ESTE ARCHIVO — Empezar aquí
├── 01-index.md                     â† Catálogo versiones, config base, prompts
├── 02-WF-log-WFvivienda.md         â† Log TODAS las corridas (extiende index)
├── 03-nodos-WFvivienda.md          â† Config propia de cada nodo (no genérico)
├── 04-backlog.md                   â† Pruebas pendientes, ideas, sugerencias
├── salidas/                        â† Imágenes NOMENCLADAS: n_01-{L}-{NN}.png
├── PLANS/                          â† Planes formales, comparativas, migraciones
├── SPECS/                          â† Especificaciones técnicas, decisiones
└── workflow_txt2img_vivienda_sdxl.json  â† Workflow ComfyUI (fuente)
```

---

## Qué es cada archivo

| Archivo | Para qué sirve | Cuándo leerlo |
|---------|----------------|---------------|
| **00-README.md** | Mapa de la carpeta, convención nombres, cómo usar el flujo | **Siempre primero** |
| **01-index.md** | Versiones ejecutadas, config baseline, prompts base, nodos resumen | Antes de correr tests |
| **02-WF-log-WFvivienda.md** | Detalle de CADA corrida: seed, config, prompt, resultado, observaciones | Durante/después de testear |
| **03-nodos-WFvivienda.md** | Config ESPECÃFICA de cada nodo (valores exactos, justificaciones SDXL) | Al armar/modificar workflow |
| **04-backlog.md** | Lista priorizada de tests pendientes, ideas, dependencias | Para planear siguiente sesión |
| **salidas/** | PNGs con nombre `n_01-{L}-{NN}.png` — 1 por corrida loggeada | Ver resultados visuales |
| **PLANS/** | Documentos `.md` de planes formales (comparativas, migraciones) | Decisiones de arquitectura |
| **SPECS/** | Especificaciones técnicas, requisitos, ADRs del flujo | Documentar decisiones |

---

## Convención de nomenclatura salidas

```
n_01-{LETRA}-{NN}.png
```

| Letra | Significado | Cuándo usar |
|-------|-------------|-------------|
| **A** | Baseline absoluto (3 corridas idénticas) | Inicio de validación modelo |
| **B** | Variación **prompt** (atmósfera, estilo, materiales) | Exploración creativa |
| **C** | Exploración **parámetros** (cfg, sampler, steps, scheduler) | Optimización técnica |
| **D** | Migración **modelo** (SD 1.5 → SDXL, o entre checkpoints) | Decisión de stack |
| **E** | Variación **resolución / aspect ratio** | Validar buckets SDXL |
| **F** | **ControlNet / img2img** | Control geométrico |

> **Regla de oro:** Cada entrada en `02-WF-log-WFvivienda.md` **DEBE** tener su PNG en `salidas/` con el mismo ID.

---

## Referencias cruzadas (hipervínculos)

- `01-index.md` ↔ `02-WF-log-WFvivienda.md` — Index es resumen, Log es detalle
- `01-index.md` → `03-nodos-WFvivienda.md` — Config baseline vs config por nodo
- `04-backlog.md` → `02-WF-log-WFvivienda.md` — Al completar test, mover de backlog a log
- `PLANS/` → `04-backlog.md` — Planes formales nacen de backlog priorizado
- `SPECS/` → `03-nodos-WFvivienda.md` — Specs documentan por qué cada config

---

## Flujo de trabajo estándar (sesión de test)

```mermaid
graph TD
    A[Leer 00-README] --> B[Leer 01-index — config baseline]
    B --> C[Leer 04-backlog — elegir test prioritario]
    C --> D[Abrir workflow_txt2img_vivienda_sdxl.json en ComfyUI]
    D --> E[Ejecutar corrida — anotar seed, config, prompt]
    E --> F[Copiar output a salidas/ n_01-{L}-{NN}.png]
    F --> G[Registrar en 02-WF-log-WFvivienda.md — DETALLE]
    G --> H[Actualizar 01-index.md — fila en tabla versiones]
    H --> I[Mover item de 04-backlog a completado]
    I --> J[¿Más tests? → C : FIN]
```

---

## Referencias externas

- **Ficha modelo:** [[wiki/glosario/software/comfyui#checkpoint--juggernaut-xl-v9|checkpoint-juggernaut-xl-v9]]
- **Troubleshooting AMD:** [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion]]
- **Glosario nodos:** [[wiki/glosario/software/comfyui|nodos ComfyUI]]
- **Reglas workflows:** [[reglas-workflows-comfy]]
- **MVP principal:** [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04]]