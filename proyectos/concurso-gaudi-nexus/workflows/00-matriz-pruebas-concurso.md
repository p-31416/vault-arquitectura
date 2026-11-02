---
tipo: plan
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
origen: fusión [[proyectos/concurso-gaudi-nexus/workflows/00-aporte-matriz-pruebas|00-aporte-matriz-pruebas (@tim)]] + [[proyectos/concurso-gaudi-nexus/workflows/00-index|00-index WF concurso]] + matriz paralelo 2026-11-01
tags: [concurso, gaudi-nexus, matriz, pruebas, workflows, comfyui]
idioma: es
---

# Matriz de pruebas — concurso Gaudí Nexus (organizada por flujos)

> Total: **~59 corridas** en 5 WFs generativos + 2 WFs de protocolo/check (sin corridas). Convenciones: [[proyectos/concurso-gaudi-nexus/workflows/00-index|00-index]] · salidas `gx-{A..G}-{NN}.png` (R3) · reglas [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|R1-R4]].
> **Regla madre (@tim)**: una variable por corrida. El humano (Sol) revisa cada salida una a una → keeper/descartar antes de avanzar.
> La pata txt2img local↔cloud↔API es la de [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-paralelo-cloud-local/PLANS/matriz-pruebas-paralelo-txt2img|matriz paralelo MVP_04]] — esta matriz es la del concurso y sus WFs.
>
> **Tablero polaroid**: `activos/web/concurso/index.html` (4 corridas 01/11 con segundos de `/history`, resolución IHDR, mosaico + clic). Regenerar: `P:\Anaconda\envs\comfyenv\python.exe scripts/dashboard-concurso.py`. Cada corrida nueva suma una fila aquí + una entrada en `ITEMS` del script.

## Cuadro de lógica (ampliable en Obsidian)

![matriz de pruebas](activos/diagramas/matriz-pruebas-concurso.png)
> Fuente editable: `proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso.excalidraw.md` (abrir con el plugin Excalidraw: zoom/pan nativos, sin scroll gigante).

## Mapa

| WF | Corre en | Precondiciones | # corridas | Estado |
|----|----------|----------------|-----------:|--------|
| [[#WF-01 — base (protocolo)]] | local | ninguna |  · checklist | pendiente |
| [[#WF-02 — texto a imagen]] | local + pod | FLUX.2 klein 9B (pod) | 13 | **en curso · 4 corridas hechas** |
| [[#WF-03 — rhino a imagen]] | pod + local | capturas Rhino + FLUX.2 pod | 14 | grafo ya existe |
| [[#WF-04 — imagen a video]] | pod (+ Comfy Cloud) | modelos LTX (pod) | 10 | pendiente |
| [[#WF-05 — imagen a 3D]] | local + pod | ComfyUI-3D-Pack | 10 | pendiente |
| [[#WF-06 — round table]] | local | audio del módulo |  · checklist | script listo |
| [[#WF-07 — flujo Gaudí]] | pod | INSTRUCTION.md var B + LoRA | 12 | pendiente |

**Infraestructura faltante** (al 2026-11-01): pod RunPod sin configurar · FLUX.2 klein 18,3 GB (pod) · modelos LTX (pod) · ComfyUI-3D-Pack (pod) · SSD-1B 4,5 GB (local, opcional).

## Corridas ejecutadas — 2026-11-01

Cuatro corridas locales, todas `success`, 0 USD de nube.

| Test | WF | Modelo | Resolución | Duración | Salida |
|---|---|---|---:|---:|---|
| gx-A-01 | WF-02 | Juggernaut-XL v9 | 1216×832 | 609 s | `r-01-baseline.png` |
| T-H1 | WF-02 hires | Juggernaut-XL v9 | 2016×1152 | 1074 s | `t-h1-juggernaut.png` |
| T-H2 | WF-02 hires | RealVisXL v5.0 | 2016×1152 | 1165 s | `t-h2-realvisxl.png` |
| T-H3 | WF-02 hires | RealVisXL v5.0 Lightning | 2016×1152 | 409 s | `t-h3-lightning.png` |

> Prompt: [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|programa fractal]] §11 (vista aérea). Grafo hires: 1344×768 → latent upscale ×1.5 → 2.º KSampler denoise 0.35–0.4. Binarios en `activos/proyectos/concurso-gaudi-nexus/fractal-hires/` (fuera de git). Log: [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-fractal-hires/02-WF-log-fractal-hires|02-WF-log-fractal-hires]].

![[activos/proyectos/concurso-gaudi-nexus/fractal-hires/r-01-baseline.png|420]]
![[activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h1-juggernaut.png|420]]
![[activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h2-realvisxl.png|420]]
![[activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h3-lightning.png|420]]

**Veredicto**: pendiente revisión 1×1 de Sol (keeper / descartar).
**Hallazgo**: las corridas 2 y 3 del baseline salieron cacheadas (0,02 s y 0,01 s) → gx-A-02/A-03 necesitan seeds 43/44 para ser renders reales.

## Corridas ejecutadas — 2026-11-02 (WF-01 exploratorias, trabajo de la semana)

Cuatro corridas locales 512² en el día, todas `success`, 0 USD de nube. Comparan checkpoint con prompt fijo (las dos primeras) y prueban prompting en español + receta del autor (las dos últimas). Tiempos vivos de `/history`, con respaldo en el script del tablero.

| Test | WF | Modelo | Prompt | Resolución | Duración | Salida |
|---|---|---|---|---|---:|---|
| w01-juggernaut | WF-01 | Juggernaut-XL v9 | protocolo catenarias, seed 7 | 512×512 | 354 s | `sdxl-vista/w01-juggernaut-512.png` |
| w01-realvisxl | WF-01 | RealVisXL v5.0 | mismo prompt, seed aleatoria | 512×512 | 390 s | `sdxl-vista/w01-realvisxl-512.png` |
| w01-mosaicos | WF-01 | RealVisXL Lightning | mosaicos Escher + colores tierra Pasión (es) | 512×512 | 334 s | `sdxl-vista/w01-lightning-mosaicos-512.png` |
| w01-pasion | WF-01 | RealVisXL Lightning | fachada Pasión + receta autor (dpmpp_sde, cfg 1.5) | 512×512 | 445 s | `sdxl-vista/w01-lightning-pasion-512.png` |

> Tablero: `activos/web/concurso/index.html` (8 imágenes con las 4 de hoy). Binarios en `activos/proyectos/concurso-gaudi-nexus/sdxl-vista/` (fuera de git). prompt_id en `scripts/dashboard-concurso.py` (`ITEMS`).

---

## WF-01 — base (protocolo) · sin corridas
Checklist: leer grafo base del curso → fijar protocolo de comparación (mismo seed/cfg/steps entre plataformas) → decidir plataforma por WF. Su salida ES esta matriz + la run-book de corridas.

## WF-02 — texto a imagen · 13 corridas
Base receta validada (@tim §2): Juggernaut-XL v9 · 1216×832 · 35/4 · dpmpp_2m+karras · seed 42 · 651 s/corrida local. Corpus Sagrada M01–M20 (INDICE-RENDERS) como puente de migración.

| Test | Dónde | Qué corre |
|---|---|---|
| gx-A-01..03 | local | Baseline SDXL ×3 (seed 42) — **A-01 ✅ 609 s** · A-02/A-03 pendientes (seeds 43/44) |
| gx-B-01 | local | Prompt Sagrada es/en (mismo seed) |
| gx-B-02 | local | Prompt modular vs libre |
| gx-C-01..03 | local | cfg {3, 4, 7} |
| gx-C-04..05 | local | steps {30, 50} |
| gx-D-01 | local | SD1.5 architecturerealmix_v11 (mismo prompt) |
| gx-D-02 | pod | FLUX.2 klein 9B (cuando stack esté) |
| gx-E-01 | local | 1024² vs 1216×832 |
| gx-G-01/02 | local | LoRA curso 50% vs 100% |
| T-H1..03 | local | Hires fractal ×1.5 (2016×1152): Juggernaut · RealVisXL · Lightning — ✅ 3/3 |

## WF-03 — rhino a imagen · 14 corridas
Base: `workflow_rhino_to_imagen.json` (existe). FLUX.2 escalado R2 (geometría 1,0 MP · material 0,5 MP).

| Test | Dónde | Qué corre |
|---|---|---|
| gx-A-01..03 | pod | Baseline masa+material (denoise 0.75, ×3) |
| gx-B-01 | pod | Prompt interior vs exterior (misma masa) |
| gx-C-01..03 | pod | Denoise {0.4 calco, 0.6 re-estilo, 0.8 reinvención} |
| gx-D-01/02/03 | pod | ControlNet: canny solo / depth solo / dual 1:1 |
| gx-D-04 | pod | Dual + foto material 0,5 MP (R2) |
| gx-E-01 | local | Upscale RealESRGAN ×4 + 2.º denoise 0.15–0.35 |
| gx-F-01 | local | Inpaint emplazamiento sobre foto CC BY-SA plaza |
| gx-F-02 | pod | Seed de masa fijada para reuso (@tim §7) |
| gx-A-04 | pod | Re-run baseline 48 h después (determinismo) |

## WF-04 — imagen a video (LTX) · 10 corridas
Base: `workflow_video_ltxi2v.json` (n_07 v1.0). Start frame = render de WF-03.

| Test | Dónde | Qué corre |
|---|---|---|
| gx-A-01..03 | pod | Baseline i2v 4 s · 8 steps · cfg 1 · strength 0.6 (×3) |
| gx-B-01 | pod | Prompt "dolly in" vs "cámara estática" |
| gx-C-01/02 | pod | strength {0.4, 0.8} |
| gx-C-03 | pod | duración 4 s vs 8 s (frames 8n+1) |
| gx-D-01 | pod | Timelapse trípode fijo (fotos reales) |
| gx-D-02 | pod | Interpolación de fotogramas |
| gx-E-01 | pod | Audio sync ON vs OFF |
| gx-A-04 | pod/cloud | Timing + créditos por corrida |

## WF-05 — imagen a 3D · 10 corridas
Hunyuan3D / Tripo. ComfyUI-3D-Pack pendiente (pod).

| Test | Dónde | Qué corre |
|---|---|---|
| gx-A-01..03 | pod | Baseline Hunyuan3D sobre masa renderizada (×3) |
| gx-B-01 | pod | Tripo vs Hunyuan3D, misma entrada |
| gx-C-01..03 | local | 3 de las 9 preparaciones de imagen del curso |
| gx-D-01 | pod | Texture toggle ON vs OFF |
| gx-E-01 | local | Export OBJ → import Rhino a cota real (check 1:1) |
| gx-D-02 | pod | Polycount bajo vs alto |
| gx-D-03 | pod | Iteración de detalle (round 2) |

## WF-06 — round table · sin corridas
Criterio del jurado (Cas Esbach): lógica constructiva sobre apariencia. Checklist de auditoría final de todos los keepers.

## WF-07 — flujo Gaudí · 12 corridas
Dos pasos: paso 1 arcilla (txt2img controlado) + paso 2 = WF-03 con INSTRUCTION.md var B. Dial de intensidad 0–10.

| Test | Dónde | Qué corre |
|---|---|---|
| gx-A-01..03 | pod | Paso 1 arcilla baseline (×3) |
| gx-C-01..06 | pod | **Dial intensidad {0, 2, 4, 6, 8, 10}** (ControlNet depth/canny) |
| gx-G-01 | pod | LoRA concurso 50% vs 100% |
| gx-F-01 | pod | Paso 2 (WF-03) con INSTRUCTION B sobre el mejor dial |

---

## Presupuesto

| Bloque | Corridas | Tiempo GPU | Costo |
|---|---:|---|---|
| WF-02 local (SDXL 651 s) | 10 | ~1 h 50 m + revisión | $0 |
| WF-03 pod (FLUX.2) | 14 | ~1 h 20 m | pod |
| WF-04 pod (LTX) | 10 | ~1 h | pod |
| WF-05 | 10 | ~1 h | pod + local |
| WF-07 pod | 12 | ~1 h 10 m | pod |
| **Total** | **59** | **≈ 5 h 30 m GPU** | pod ≈ **$5–6** (4090 $0,89/h) |

## Loop de cada corrida (estándar)

1. Aviso de corrida a Sol (HITL); una corrida a la vez en pruebas pagadas
2. JSON del test validado R4 contra el servidor destino
3. Encolar (MCP local · comfy-cli/API pod-cloud)
4. Poll → salida en `salidas/` como `gx-{L}-{NN}`
5. Registrar en `02-WF-log` del WF: prompt_id, seed, duración, costo, veredicto
6. Sol revisa keeper/descartar → próxima corrida (una variable)
7. Si falla → diagnóstico (`get_history action:"diagnose"`) + fail documentado

## Template de registro

```
WF-0? · Test gx?-? · letra ? · fecha
prompt_id: · seed: · duración: · costo: · revisión Sol: keeper / descartar
salida: salidas/gx?-?-??.png
```
