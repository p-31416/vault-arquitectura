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

## R2: Escalar según el modelo, no según la época

**Regla:** El escalado de la imagen de entrada depende del modelo del sampler. En **SD1.5** manda R1 (`ImageScale` a 512×512). En **FLUX.2** el escalado es a megapíxeles con `ImageScaleToTotalPixels` y el upscale final es `ImageUpscaleWithModel` + Hires fix.

**Por qué:**
- FLUX.2 está entrenado con imágenes de más resolución: a 512×512 rinde por debajo de lo que puede.
- En los workflows de referencia (Rhino-to-Image) la geometría se escala a **1,0 MP** y la referencia de material a **0,5 MP**, con `lanczos`: la relación de escala entre ambas es la que hace que el material caiga en la escala correcta de la geometría.

**Nodo a usar (FLUX.2):**
```
ImageScaleToTotalPixels
├── upscale_method: "lanczos"
├── megapixels: 1.0   (geometría)  ·  0.5 (referencia de material)
├── resolution_steps: 1
```

**Upscale de salida (cualquier modelo):**
```
ImageUpscaleWithModel (RealESRGAN_x4plus)  →  2.º KSampler denoise 0,15-0,35  →  VAEDecode
```

**Excepciones:**
- `txt2img` puro (no hay input de imagen).
- La imagen final puede ser mayor que la del sampler: el upscale va después.

**Workflows que la aplican:** `proyectos/concurso-gaudi-nexus/workflows/WF-02-texto-a-imagen/` · `WF-03-rhino-a-imagen/` · `WF-05-imagen-a-3d/` · `n_05-rhino-mcp/WF-rhino-to-image/`.

---

## R3: Nomenclatura de salidas del concurso

**Regla:** En la carpeta del concurso (`proyectos/concurso-gaudi-nexus/`), las corridas se nombran `gx-{LETRA}-{NN}.png`, con `gx` por el proyecto (Gaudí Nexus) y la letra con el mismo significado de la tabla de arriba (A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img).

**Por qué:** la convención `n_XX-` identifica el proyecto **MVP**, y estos workflows son del concurso: el prefijo propio evita que se confundan con las corridas de MVP_04.

**Dónde va:** `proyectos/concurso-gaudi-nexus/workflows/WF-<nn>/salidas/` (carpeta fuera de git).

---

## R4: Validación estática antes de la corrida

**Regla:** Todo workflow se valida contra el servidor destino y contra el disco antes de encolar la primera corrida: cada `class_type` y cada widget contra `/object_info`, y cada modelo referenciado contra la carpeta `models/` del servidor. El resultado de la validación queda anotado en el `02-WF-log`.

**Por qué:** un `class_type` inexistente o un nombre de modelo que no está en la carpeta del servidor aparecen recién al encolar, cuando el grafo ya está cargado.

**Cómo:**
```
GET /object_info                    → class_type y widgets disponibles
GET /models  (o /models/<tipo>)     → modelos instalados en el servidor
```

**Excepciones:** los workflows que se ejecutan contra un servicio externo (nodos partner de Comfy Cloud) se validan contra el `object_info` de esa plataforma.

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
| **G** | Test de **LoRA** (fuerza, trigger, base) — añadido 2026-10-28 |

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
