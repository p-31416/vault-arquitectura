---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: Backlog unificado de futuras pruebas
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
estado: borrador-activo
tags: [concurso, gaudi-nexus, backlog, pruebas, comfyui, sherlock]
idioma: es
---

# 30 — Backlog unificado de futuras pruebas

> Lista única de pruebas pendientes del concurso: las que ya teníamos en YT-01–04 y el reporte, más las líneas nuevas que trae la búsqueda de Sherlock 2026-11-03. Cuando una prueba se corre, se registra en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]] y se marca aquí como hecha.

## Fuentes Sherlock (2026-11-03, links verificados)

| Línea | Crudo | Qué aporta |
|---|---|---|
| A+B crear y reusar custom nodes | [[raw/research/2026-11-03-sherlock-custom-nodes-comfyui|sherlock-custom-nodes]] | guía oficial de nodos, Registry, caso CameraAngleSelector |
| C LoRA de croquis propios | [[raw/research/2026-11-03-sherlock-lora-croquis|sherlock-lora-croquis]] | kohya / ai-toolkit / OneTrainer / Civitai Studio, SD1.5 local + SDXL cloud |
| D control de iluminación | [[raw/research/2026-11-03-sherlock-iluminacion-arquitectura|sherlock-iluminacion]] | IC-Light + nodos kijai, LoRAs de luz, videos de dirección de luz |

## 1. Líneas nuevas desde Sherlock

### Iluminación (prioridad alta — el peso ya está en disco)

- [ ] **L1** — Reiluminar fachada con IC-Light `fc` (en disco): mismo encuadre, sol mañana / tarde / noche. Nodos kijai `LoadAndApplyICLightUnet` + `ICLightConditioning` + `LightSource`. Fuente: [[raw/research/2026-11-03-sherlock-iluminacion-arquitectura|sherlock-iluminacion]] §1–2.
- [ ] **L2** — Rama `fbc` (toda la escena sigue el prompt) vs `fc` con la misma captura; comparar.
- [ ] **L3** — LoRA de luz direccional (ej. `CinelightX SDXL` / `Polyhedron Chiaroscuro`) a fuerza 0,3–0,6 sobre Juggernaut v9 + prompt `warm sunlight from right, long shadows`. Fuente: [[raw/research/2026-11-03-sherlock-iluminacion-arquitectura|sherlock-iluminacion]] §3.
- [ ] **L4** — Croquis → ControlNet MLSD + Depth → IC-Light tarde. Receta §3 del crudo.

### Vistas e iluminación combinadas

- [ ] **V1** — Activar upgrade YT-03 §8 (CameraAngleSelector + LoRA multi-ángulo en pod): primera corrida `front-right quarter view eye-level medium shot` con render propio.

### LoRA de croquis propios

- [ ] **C1** — Dataset 15–40 fotos de croquis + captions de contenido + trigger inventado; entreno piloto SD1.5 local (kohya u OneTrainer, rank 16, 512px). Fuente: [[raw/research/2026-11-03-sherlock-lora-croquis|sherlock-lora-croquis]] §1–3.
- [ ] **C2** — Consolidar estilo ganador en SDXL vía RunPod (ai-toolkit) o Civitai Studio.

### Custom nodes (cuando el flujo lo pida)

- [ ] **N1** — Instalar CameraAngleSelector por git URL + restart (paso previo a V1).
- [ ] **N2** — Andamiaje `comfy node scaffold` para un nodo propio mínimo (ej. prompter de cámaras Gaudí). Fuente: [[raw/research/2026-11-03-sherlock-custom-nodes-comfyui|sherlock-custom-nodes]] §2–3.

## 2. Pendientes YT existentes (unificados aquí, detalle en cada ficha)

| # | Prueba | Estado | Fuente |
|---|---|---|---|
| YT-01-T1–T5 | inpainting árbol / muro cortina / borrar / ventana / material | pendiente corrida | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-01-sdxl-inpainting-diffuseda|YT-01]] §6–7 |
| YT-01-modelos | Ragnarok + LoRA liviano 36 MB + rama ControlNet | pendiente descarga | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-01-sdxl-inpainting-diffuseda|YT-01]] §7 |
| YT-02-video | ver video ítem 15 + extraer receta (rank 8 vs 16, regularización) | pendiente ver | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-02-lora-sdxl-pocas-imagenes|YT-02]] §2–5 |
| YT-03-T1 | vista 15° izquierda casa blanca, comparar 1024 vs 512 | T1-1024 en curso, T1-512 a cargo de Sol | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-03-vista-nueva-desde-render-propio|YT-03]] §6 |
| YT-03-ControlNet | rama unión SDXL promax | pendiente descarga | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-03-vista-nueva-desde-render-propio|YT-03]] §7 |
| YT-04-T1 | primera captura Rhino + corrida T1 | pendiente captura Sol | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-04-rhino-vivo-propio|YT-04]] §6–7 |
| YT-04-watcher | watcher carpeta + GH depth/normal, Rhino MCP | backlog futuro | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-04-rhino-vivo-propio|YT-04]] §7 |
| REP-P-01 | captura Google + dibujo (F-03 depth 0.5) | pendiente Sol | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|reporte]] |
| REP-P-03 | croquis → croquis mejorado | pendiente | [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|reporte]] |

## 3. Matriz del concurso (WF-01–07)

Estados y corridas madre viven en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|00-matriz-pruebas-concurso]]: WF-01 baseline A-02/A-03 (seeds 43/44), WF-02–07 pendientes por stack (FLUX.2, LTX, ComfyUI-3D-Pack, transcripción módulo 6). Este backlog no los duplica: lo nuevo de YT/Sherlock se suma a la matriz cuando se corre.

## 4. Backlogs hermanos (MVP_04, referencia sin duplicar)

- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/04-backlog|backlog WF-rhino-to-image]] — variante GGUF Q4 local, premium del LoRA.
- [[proyectos/MVP_04-comfyui-arquitectura/n_07-img2video/WF/WF_v1.0_ltx_i2v/04-backlog|backlog LTX i2v]] — cadena de video WF-04.
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-paralelo-cloud-local/04-backlog|backlog paralelo cloud-local]] — matriz de 44 tests txt2img.

---
*Más nuevo → más arriba. Log: 2026-11-03 creación por pedido de Sol: unifica pendientes YT-01–04 + reporte P-01/P-03 + líneas A–D de Sherlock.*
