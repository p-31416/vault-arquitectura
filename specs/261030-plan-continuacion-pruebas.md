---
tipo: spec
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-11-02
tags: [spec, comfyui, matriz, pruebas, img2img, inpainting, controlnet, sdxl, concurso, flux, lora]
estado: activo
---

# Continuación de las pruebas — campaña de flujos del concurso

> Cómo siguen las pruebas después de las 18 corridas: bloque SDXL (techo de VRAM), barrido de fuerza de LoRA, img2img + inpainting de la Sagrada Familia, ControlNet, formalización de GX-02, el camino Flux klein 9B con el LoRA del curso, el set `sdxl-vista` de 7 WF y los flujos del piloto de YouTube. Cada fase trae su comando, su costo medido o estimado y su gate de revisión.

- [[#0 · Dónde estamos]]
- [[#Fase A · Bloque SDXL (M02, M09–M13)]]
- [[#Fase B · Barrido de fuerza SD 1.5]]
- [[#Fase C · img2img Sagrada Familia]]
- [[#Fase D · Inpainting con máscara]]
- [[#Fase E · ControlNet SD 1.5]]
- [[#Fase F · GX-02 y el pod]]
- [[#Fase G · Camino Flux klein 9B + LoRA rhino→imagen (pod)]]
- [[#Fase H · Set sdxl-vista (7 WF del curso)]]
- [[#Fase I · Piloto YouTube G1–G12]]
- [[#Reglas de campaña]]
- [[#Tabla de límites]]

---

## 0 · Dónde estamos

18/20 filas de la matriz corridas: 14 el 2026-10-29 (bloque SD 1.5 + parámetros) y 4 el 2026-11-01 (SDXL y LoRAs), seed 42, prompt del proyecto. Tiempos medidos: 65–210 s por render en SD 1.5; 409 s con RealVisXL Lightning, 609 s con Juggernaut a 1216×832 y 1073–1165 s con upscale a 2016×1152. Las 18 viven en el tablero (`curso.html`, solapas Repasadas y Matriz) con su `.json` descargable (`workflows/matriz-<ID>.json`, M01 verificado idéntico al embebido en su PNG).

| Frente | Estado |
|---|---|
| M01, M03–M08, M14–M20 | corridos, repasados en tablero |
| M02, M09–M13 (SDXL) | 4 corridas del 2026-11-01; el techo de VRAM con LoRAs rank 128 sigue pendiente |
| Eje fuerza | un solo punto (@0.8); rango 0.6–0.9 sin barrer |
| img2img Sagrada | foto reducida lista (`Temp\opencode\barcelona_1024.jpg`), corrida full-res trabada y cancelada, Comfy relanzado y sano |
| Set `sdxl-vista` (7 WF) | fichas escritas, JSON sin validar contra `/object_info` (R4) |
| Flux klein 9B + `rhino-to-image` | LoRA en disco y clasificado; corre en pod, sin cuenta todavía |

---

## Fase A · Bloque SDXL (M02, M09–M13)

Mide el techo real de VRAM con LoRAs rank 16–128 (hasta 870 MB) bajo `--lowvram --cpu-vae`. Hipótesis a confirmar: hasta 900 MB sin ControlNet.

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque modelo
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque loras_sdxl
```

Costo estimado (a medir en la primera corrida M02): entre 5 y 12 min por render por el paginado a RAM; correr en tanda vigilada. Si hay OOM, el dial es: primero confirmar `batch 1` y resolución 1216×832 ya fijadas, después pasar el bloque al pod. Al terminar: sumar IDs a `EJECUTADAS` en `volcar-grafos-matriz.py`, volcar, agregar filas a `curso.json`, regenerar tablero.

Gate: lectura del techo (¿entran los rank 128?) antes de prometer SDXL local en el WF-02.

---

## Fase B · Barrido de fuerza SD 1.5

Llena el eje fuerza de la Matriz: 6 LoRAs (archviz, sandiese, brutaltech, corbusier, room, superhighrise) × fuerzas 0.4 / 0.6 / 1.0 = 18 corridas. Costo estimado: ~170 s por render → unos 50 min de GPU. Requiere extender `MATRIZ` con filas nuevas (IDs M21–M38, mismo `armar_grafo` con `loras=[(..., f)]`), más sus entradas en `curso.json` y `EJECUTADAS`.

Gate: con tres puntos por LoRA se fija el rango óptimo real (hoy solo se supone 0.6–0.9) y la tarjeta de cada LoRA gana su curva.

---

## Fase C · img2img Sagrada Familia

Foto `barcelona_1024.jpg` (1024×683, ya reducida: la full-res de 2622 px trabó el VAE en CPU fp32 sin posibilidad de cancel entre steps). Tres corridas, denoise 0.4 / 0.6 / 0.8, seed 42, mismo prompt de plaza + catenarias:

- 0.4 conserva la foto, apenas la sueña; 0.6 transforma manteniendo composición; 0.8 casi re-imagina.
- Negativo suma `gruas, construccion, andamios`.

Subir por `upload_image` (único canal válido al `input/`), encolar el grafo LoadImage→VAEEncode→KSampler→VAEDecode→SaveImage, registrar en `curso.json` como módulo 3 (flujo WF-03 adelantado).

---

## Fase D · Inpainting con máscara

Checkpoint en disco: `sd-v1-5-inpainting-fp16.safetensors`. Enmascarar solo cielo/plaza de la foto y generar ahí las luminarias: el resto queda pixel a pixel. La máscara se pinta en ComfyUI (la UI la guarda junto al workflow). Dos corridas (cielo / plaza), seed 42.

Gate: comparar contra img2img 0.6 — ¿el enmascarado conserva mejor las torres?

---

## Fase E · ControlNet SD 1.5

Tres corridas sobre la foto (canny / depth / scribble, modelos en disco), denoise medio, para fijar composición con mano dura y dejar el estilo al prompt. Alimenta el WF-03 formal.

---

## Fase F · GX-02 y el pod

Con las fases A–E medidas, formalizar `workflow_lora_strength.json` → GX-02 (base + LoraLoader + trigger) con revisión de Sol y cierre v1.0.

La comparativa de modelos queda cubierta por las fases G y H: FLUX.2 klein 9B con el LoRA del curso en el pod, y el set SDXL de 7 WF en local. El plan horario que ordena todo esto es [[specs/261102-plan-24h-croquis-lora-laminas|el plan de 24 h del 2026-11-02]]: Sprint 2 (croquis en la plaza real) y Sprint 3–4 (pod + Flux + LoRA de estilo).

---

## Fase G · Camino Flux klein 9B + LoRA rhino→imagen (pod)

El LoRA `rhino-to-image-lora.basic.safetensors` (121 MB, rank 16, F32, `diffusion_model.double_blocks.0–7` + `single_blocks.0–23`, `txt_in` 12288→4096) pertenece a la familia **FLUX.2 klein**. Conviene verificar el repo exacto antes de armar el grafo, porque el template oficial publicado lista variantes 4B y la lectura de tensores apunta a 9B.

| Pieza | Archivo esperado | Carpeta |
|---|---|---|
| Modelo base | `flux-2-klein-9b-fp8.safetensors` | `models/diffusion_models/` |
| Text encoder | `qwen_3_8b_fp8mixed.safetensors` | `models/text_encoders/` |
| VAE | `flux2-vae.safetensors` | `models/vae/` |
| LoRA | `rhino-to-image-lora.basic.safetensors` | `models/loras/` |

Secuencia:

1. Aceptar los términos del repo gated en Hugging Face y guardar el token de lectura.
2. Desplegar el pod (RTX 4090 24 GB, ~USD 0,39/h) con el template de ComfyUI.
3. Correr la vista del `mcp-plaza.3dm` con el LoRA a fuerza 0,8 / 1,0 sobre la misma semilla.
4. Correr el modo **edición con referencias** (1–4 imágenes): viewport de Rhino + foto real de la plaza + croquis en la misma corrida.
5. Registrar tiempo, VRAM y veredicto en la matriz con prefijo `gx-FLUX-*`.

Gate: comparación lado a lado contra WF-03 (SDXL img2img denoise 0,65) sobre la misma geometría. Decide el camino de la lámina principal.

---

## Fase H · Set sdxl-vista (7 WF del curso)

Los 7 flujos del curso viven en [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/01-index|sdxl-vista]], con su ficha y su base documentada:

| WF | Ficha | Corridas previstas |
|---|---|---|
| WF-01 baseline | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-01_sdxl|WF-01]] | 1 control + 1 por modelo alternativo |
| WF-02 interior | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-02_sdxl|WF-02]] | Juggernaut vs RealVisXL v5.0 |
| WF-03 Rhino→render | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-03_sdxl|WF-03]] | denoise 0,50 / 0,65 / 0,75 |
| WF-04 keyframe | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-04_sdxl|WF-04]] | 1 keyframe, luego pasa a LTX i2v |
| WF-05 maqueta 3D | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-05_sdxl|WF-05]] | 1 corrida, luego imagen→3D |
| WF-06 detalle | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-06_sdxl|WF-06]] | 1 corrida + 1 con ControlNet Union |
| WF-07 geometría→piedra | [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/WF-07_sdxl|WF-07]] | denoise 0,45 / 0,55 / 0,62 |

Antes de la primera corrida: R4 contra `/object_info` para los 7 `class_type` y para `ckpt_name`. El catálogo de modelos alternativos y sus licencias está en [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]; el detalle del checkpoint en [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/00-base-modelo|00-base-modelo]].

Gate: una ficha con tres corridas medidas (modelo, denoise y tiempo) por WF antes de tocar el siguiente.

---

## Fase I · Piloto YouTube G1–G12

El piloto de 71 videos ComfyUI del Takeout 2026-10-08 quedó agrupado en 12 grupos de flujos (G1–G12) el 2026-11-01, con orden de construcción propio: txt2img → img2img → img2video en la nube → img2 3D. Hoy el agrupamiento vive como decisión de sesión en [[raw/sessions/2026-11-01-sesion-ia-generativa-visual|la sesión del 2026-11-01]]; la lista de los 12 grupos todavía requiere reconstruirse desde los títulos.

| Fuente | Qué aporta |
|---|---|
| [[wiki/fuentes/00-index-yt|00-index-yt]] | Los 71 videos con creador, duración, tags y estado (1 procesado: architutors) |
| [[raw/yt/creadores|creadores]] | 151 canales con veredicto de Watch Later |
| [[raw/yt/00-index|raw/yt]] | Pipeline de curación y reglas HITL |

Además, el curso AI x Gaudi tiene sus módulos transcriptos, que son la fuente directa de los 7 WF:

| Módulo | Transcript | WF que alimenta |
|---|---|---|
| Text-to-Image | `raw/yt/transcripts/2026-10-21_mux-text-to-image.es.md` | WF-01, WF-02, WF-04, WF-05, WF-06 |
| Image-to-Image | `raw/yt/transcripts/2026-10-21_mux-image-to-image.es.md` | WF-03, WF-07 |
| Image-to-Video | `raw/yt/transcripts/2026-10-21_mux-image-to-video.es.md` | WF-04 → `n_07-img2video` |
| Image-to-3D | `raw/yt/transcripts/2026-10-21_mux-image-to-3d.es.md` | WF-05 → Tripo / Hunyuan3D |
| The Gaudí Workflow | `raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es.md` | WF-07 |

Paso siguiente concreto: reconstruir la tabla G1–G12 desde los 71 títulos de `00-index-yt` y marcar cuáles ya están cubiertos por los 7 WF. Cada grupo que sume un flujo nuevo entra como ficha propia en `workflows/`.

Gate: tabla G1–G12 escrita y cruzada contra los 7 WF, con 1 video de referencia por grupo.

---

## Reglas de campaña

1. Seed 42 fija salvo exploración declarada; una variable por corrida.
2. Toda corrida que entra al tablero trae: imagen + `.json` volcado + fila en `curso.json` + segundos medidos.
3. Nada se marca "repasada" sin tu visto bueno visual (HITL).
4. Foto de entrada siempre ≤1024 px de lado mayor (VAE en CPU fp32).
5. Ante un job trabado más de 10 min sin línea de progreso en el log: no reencolar encima; kill + relanzar por bat (el cancel HTTP no atraviesa un step largo).

## Tabla de límites

| Variable | Permitido (medido o en disco) | Óptimo (evidencia) |
|---|---|---|
| Steps SD1.5 | 10–50 (65–210 s) | 30 (M15 no justifica 3×) |
| CFG | 3–12 | 7 |
| Sampler | euler+normal, dpmpp_2m+karras | euler+normal (base) |
| Resolución SD1.5 | 512²–768² | 768×512 |
| Fuerza LoRA SD1.5 | 0.6–0.9 (rango de trabajo) | 0.8 (único medido) |
| LoRA SD1.5 | ≤250 MB + 2 ControlNet | rank 8–16 casi gratis |
| LoRA SDXL | hipótesis ≤900 MB, sin ControlNet | pendiente Fase A |
| img2img foto | ≤1024 px, denoise 0.4–0.8 | 0.6 (a confirmar Fase C) |
| Steps SDXL | 30–35 (609 s a 1216×832) | 30 (con 4 steps de Lightning: 409 s) |
| Resolución SDXL | 1024² – 1216×832 | 1216×832 |
| Upscale SDXL | 2016×1152 en 1073–1165 s | reservar para cierre de lámina |
| Flux klein 9B | pendiente de pod | fuerza LoRA 0,8–1,0 (a medir) |
