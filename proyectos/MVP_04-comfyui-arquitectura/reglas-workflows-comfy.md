---
tipo: regla
mvp: 04
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19
tags: [mvp_04, comfyui, reglas, workflows, estandares]
---

# Reglas para Creación de Workflows en ComfyUI

Reglas obligatorias al construir o modificar workflows de ComfyUI. Aplican a todos los niveles (n_01–n_05).

---

## R1: Siempre escalar inputs de imagen a 512x512

**Regla:** Todo flujo que reciba una imagen de entrada (local, de internet, o generada previamente) DEBE incluir un nodo `ImageScale` (o `ImageResize`) que fije la resolución a **512x512** antes de que la imagen llegue al sampler o a cualquier nodo consumidor.

**Por qué:**
- Las imágenes de entrada vienen de fuentes heterogéneas (fotos de celular, croquis escaneados, renders previos, descargas de internet) con resoluciones impredecibles.
- ComfyUI no valida dimensiones antes de enviar a VRAM. Una imagen de 4000x3000 en un RX 570 (8GB VRAM) causa OOM instantáneo.
- SD 1.5 está entrenado a 512x512. Alimentar con otras resoluciones produce artefactos o crops inesperados.

**Nodo a usar:**

```
ImageScale
├── upscale_method: "nearest-exact"  (para ControlNet) o "bilinear" (para img2img)
├── width: 512
├── height: 512
├── crop: "center"
```

**Dónde va en el pipeline:**

```
LoadImage / UploadImage
        │
        ▼
   ImageScale (512x512)   ← SIEMPRE AQUÍ
        │
        ▼
  ┌─────┴─────┐
  │           │
ControlNet  KSampler
(preproc)   (img2img)
```

**Excepciones:**
- `txt2img` puro (no hay input de imagen → no aplica)
- Upscale final (la imagen de salida puede ser mayor, pero el input al sampler sigue siendo 512x512)

**Ejemplo de workflow affected:**
- `n_02-img2img/log-WF-croquis/workflow_img2img_croquis.json` — el croquis de entrada necesita este nodo
- `n_03-controlnet/workflow_controlnet_canny.json` — la imagen de control necesita este nodo

---

## Convenciones para workflows (agregar reglas aquí)

Las reglas se acumulan a medida que se descubren durante el desarrollo. Formato:

```
## R{n}: Título corto

**Regla:** Descripción de la obligación.
**Por qué:** Razón técnica.
**Nodo a usar:** Configuración del nodo.
**Dónde va:** Posición en el pipeline.
**Excepciones:** Cuándo no aplica.
```

---

## Estructura estándar de carpetas (movida de `AGENTS.md` 2026-09-10)

**OBLIGATORIO:** Todos los workflows ComfyUI en `proyectos/` deben seguir esta estructura:

```
proyectos/<MVP>/<nivel>/WF-<nombre>/
├── 00-README.md              # Guía navegación y uso (prefijo 00- = primero)
├── 01-index.md               # Catálogo versiones, nomenclatura, configs mínimas
├── 02-WF-log-WF<nombre>.md   # Log detallado TODAS las corridas (extiende index)
├── 03-nodos-WF<nombre>.md    # Configs PROPIAS del flujo (lo no genérico)
├── 04-backlog.md             # Pruebas pendientes, ideas, sugerencias iteración
├── salidas/                  # Imágenes generadas, NOMENCLADAS n_XX-{L}-{NN}.png
├── PLANS/                    # Planes de test, comparativas, migraciones (.md)
├── SPECS/                    # Especificaciones técnicas, requisitos, decisiones diseño
├── workflow_<nombre>.json    # Workflow ComfyUI (API format) — archivo fuente
└── workflow_<nombre>_sdxl.json  # Variante SDXL si aplica
```

**Convención nomenclatura salidas:** `n_XX-{LETRA}-{NN}.png`
| Letra | Significado |
|-------|-------------|
| **A** | Baseline absoluto (3 corridas idénticas, sin cambios) |
| **B** | Variación de **prompt** (atmósfera, estilo, materiales) |
| **C** | Exploración de **parámetros** (cfg, sampler, scheduler, steps) |
| **D** | Migración de **modelo** (ej. SD 1.5 → SDXL) |
| **E** | Variación de **resolución / aspect ratio** |
| **F** | Test de **ControlNet / img2img** |

**Archivos obligatorios y su orden:**
1. `00-README.md` — Navegación y uso del flujo
2. `01-index.md` — Catálogo de versiones + configs mínimas
3. `02-WF-log-WF<nombre>.md` — Log detallado (extensión del index, hipervínculos cruzados)
4. `03-nodos-WF<nombre>.md` — Solo configs propias (lo genérico va al glosario wiki)
5. `04-backlog.md` — Pendientes, ideas, sugerencias

**Carpetas obligatorias:**
- `salidas/` — Imágenes nomencladas
- `PLANS/` — Planes de test, comparativas, migraciones
- `SPECS/` — Specs técnicas, requisitos, decisiones de diseño

**Reglas:**
- NO archivos sueltos en la raíz del WF (todo en subcarpetas o archivos numerados)

## Integración con el vault

- Renders generados → `activos/proyectos/<proyecto>/renders/`
- Documentar workflows exitosos en `wiki/glosario/software/comfyui.md` (comandos) y `wiki/glosario/interno/pbooks/` (playbooks pbk-*)
- Los modelos grandes no se commitean a git
