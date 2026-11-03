---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, conclusiones, checkpoint, lora, rhino, runpod, comfyui, n8n]
idioma: es
---

# Conclusiones del concurso — qué manda en el flujo

> Documento vivo de decisiones. Cada fila con evidencia linkea su ficha; lo abierto queda como variable a probar con su criterio de cierre.

## 1. Tesis: checkpoint + LoRA manda

Lo que más mueve el resultado es la **combinación** de base + adaptador, no la base sola. Todo WF del concurso se describe con dos variables:

| Variable | Qué es | Valores en juego |
|----------|--------|------------------|
| **Check Type** | modelo base (arquitectura + pesos) | SD1.5 · SDXL · FLUX.1 dev · FLUX.2 klein 9B/4B · destilados/turbo · Nano Banana (privativo, API) |
| **LoRA type** | adaptador enchufado sobre la base | velocidad · viewport Rhino · estilo archviz · interior · aérea · fachada/material · inpaint |

Cambiar una por corrida, con seed y prompt fijos: esa es la matriz que decide la lámina.

## 2. Check Type — abiertos y privativos

| Base | Estado en el estudio | Dónde corre | Licencia / acceso |
|------|----------------------|-------------|-------------------|
| SD1.5 (`architecturerealmix_v11`) | retirado a `_retirados-sin-uso-comercial`, solo exploración | local RX 570 | autor prohíbe uso comercial |
| SDXL (`Juggernaut-XL_v9`, `RealVisXL V5.0`) | instalados, control del set | local RX 570 | Open RAIL (comercial con cláusula) |
| SDXL destilados/turbo (Lightning, Z-Image Turbo, KREA 2 Turbo) | Lightning instalado y descartado para lámina (vale para iterar); resto a probar | local / pod | según ficha |
| FLUX.1 dev · FLUX.2 klein 9B | stack de 18,3 GB listo, corre en pod | RunPod (24 GB VRAM) | open weights, uso comercial permitido |
| Nano Banana 2 / Pro | nodo API dentro de ComfyUI | Comfy Cloud (créditos) · Google AI Studio/Flow | privativo, por request |

Detalle por modelo: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] · inventario: [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos-recomendados]].

## 3. LoRA type — la variable que falta tabular

| LoRA type | Para qué | Estado |
|-----------|----------|--------|
| Velocidad (LCM / Hyper-SD / DMD2, destilados tipo Lightning) | iterar en pasos en vez de 30-50 | Lightning medido (rápido, flojo para lámina); aceleradores por LoRA a relevar |
| Viewport Rhino → render (`rhino-to-image` basic/premium) | el flujo Rhino-to-Image del curso | basic 120,8 MB en disco; premium pendiente de compra |
| Estilo archviz (`ArcvizXL_V01` y familia) | lenguaje de visualización sobre SDXL | propuesto en WF-02/03, pendiente de descarga |
| Interior | bóvedas, luz volumétrica, material cercano | a relevar (candidatos: RealArchmix XL + sus LoRAs) |
| Aérea / exterior | plaza, contexto Sagrada Família | a relevar |
| Fachada / material (piedra, ladrillo, trencadís) | piel gaudiana sobre geometría (WF-07, denoise 0,55) | a relevar o entrenar propio |
| Inpaint | loggias, barandillas, poblado quirúrgico | camino local `sd-v1-5-inpainting-fp16` + prueba YT-01 |

Cada LoRA nuevo entra con: base compatible, `strength` de referencia, trigger si lo trae, y fila en la matriz.

## 4. Entrenar el LoRA propio del concurso

El curso demuestra que el `rhino-to-image` (rank 16, 120 MB, entrenado con vistas de Rhino) es lo que convierte viewport en lámina. La conclusión para el estudio: **el LoRA propio queda en el roadmap** como el activo que firma la entrega.

- **Primero**: agotar inpaint + LoRAs existentes (cap. 3) con la matriz; el inpaint marca qué zonas piden material propio.
- **Después**: entrenar con nuestras vistas (viewport + renders keeper del concurso), 20-30 imágenes curadas por concepto, sobre la base que gane la comparativa (hoy: Juggernaut v9 local / klein 9B en pod).
- **Criterio de cierre**: el LoRA propio supera al genérico en catenarias que cierran, piedra que se lee y cámara que se queda quieta.

## 5. Rhino: captura, viewport real y giro

- **Captura de pantalla**: es lo que usa el curso y funciona con el LoRA entrenado para eso; vale como entrada, con la geometría dibujada mandando.
- **Viewport en tiempo real**: es la herramienta correcta (Rhino → ComfyUI por viewport, no por PNG suelto); queda como vía a montar para iterar sin exportar.
- **Cambio de perspectiva**: el giro se resuelve con **flujo que gira** (turntable / multiview 4 vistas, WF-05) en vez de pedirlo por prompt; la cámara queda como variable del grafo, no del texto.

## 6. Dónde corre cada cosa

| Venue | Para qué | Costo |
|-------|----------|-------|
| **Comfy local** (RX 570) | todo SDXL/SD1.5, inpaint, preparación 3D, validación R4 | $0 |
| **RunPod** (pod A5000/4090) | FLUX.2 klein 9B + LoRA, LTX video, 3D-Pack | ~$0,16-0,34/h, solo minutos de trabajo |
| **Comfy Cloud** | Nano Banana, calibración puntual Seedance (400 créditos/mes free) | créditos por corrida |

**n8n como mayordomo**: vive en el VPS y prende el pod, encola el JSON, recoge la salida por `/history` + `/view`, avisa por Telegram y apaga. El pod factura minutos reales; el resto del día sale $0 de GPU. Receta y checklist: [[proyectos/concurso-gaudi-nexus/workflows/00-pod-comfyui-unificado|00 — Pod ComfyUI unificado]] §5.

## 7. Orden RunPod: un solo documento (ejecutado 2026-11-02)

Los cinco `00-*` de `WF-Comfy-YT` se fusionaron en [[proyectos/concurso-gaudi-nexus/workflows/00-pod-comfyui-unificado|00 — Pod ComfyUI unificado]] (montar + pagar + instalar + Comfy-vs-pod + n8n). Viejos superseded, pendiente borrado físico.

## 8. Formatos en CivitAI: safetensors vs GGUF vs Diffusers

Lo que cambia entre pestañas de descarga es el **empaque de los mismos pesos**, y cada empaque pide su loader:

| Formato | Qué es | En ComfyUI | Cuándo elegirlo |
|---------|--------|------------|-----------------|
| **SafeTensors** (`.safetensors`) | pesos en un solo archivo, sin código ejecutable (reemplazo seguro del pickle) | `CheckpointLoaderSimple` (SD1.5/SDXL todo-en-uno) · `UNETLoader` + text encoder + VAE por separado (Flux) | default: el que corre en local y en pod sin nodos extra |
| **GGUF** (`.gguf`, Q4_K_S / Q8_0…) | cuantización llama.cpp: mismo modelo, menos GB y menos VRAM a cambio de pérdida fina | custom node ComfyUI-GGUF (`UnetLoaderGGUF`, CLIP GGUF); el checkpoint normal no lo abre | VRAM corta o iteración rápida (ej. Z-Image Turbo Q4 ~4 GB, ERNIE Turbo) |
| **Diffusers** (carpeta: `model_index.json` + `transformer/` + `text_encoder/` + `vae/` + `scheduler/`) | repo modular de HuggingFace, piezas intercambiables | nodos `DiffusersLoader` | Flux/SD3 cuando se quiere mezclar piezas (otro VAE, otro encoder) o bajar del repo oficial |
| **Legacy** (`.ckpt` / `.pt` / `.pth`) | pickle de PyTorch, ejecuta código al cargar | ComfyUI los abre, el estudio los evita | nunca descargar: pedir la versión `.safetensors` del mismo modelo |

Reglas de campaña: un formato por variable (no comparar GGUF contra fp8 como si fueran el mismo modelo); el SHA256 se registra del archivo real descargado; GGUF implica anotar custom node + loader en la ficha del WF.

## 9. Flux cuantizado: sí, con su loader y su techo

Se corre cuantizado hoy: klein 9B GGUF Q4 ≈ 5,7 GB + text encoder aparte, con `ComfyUI-GGUF` + `UnetLoaderGGUF`, y el LoRA `rhino-to-image` se aplica igual sobre el cuantizado. Fuentes: [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] (tabla VRAM + § GGUF) · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/04-backlog|backlog WF-rhino-to-image]].

| Variante Flux | VRAM aprox | Dónde | Techo conocido |
|---------------|------------|-------|----------------|
| klein 9B fp8 | ~9,4 GB + TE 8,7 GB | pod 24 GB | vía principal de lámina |
| klein 9B GGUF Q4 | ~5,7 GB + TE a RAM | pod chico / PC con offload | inferencia sí; entrenar LoRA encima no (el backward pide CUDA ≥ 8.9, research 2026-10-20) |
| klein 4B GGUF Q4 | ~3 GB + TE a RAM | local RX 570, iteración | calidad por debajo del 9B, vale para probar encuadre |
| Schnell / Z-Image Turbo GGUF | 4-8 GB, 4-8 steps | local RX 570 | concepto y velocidad, no lámina final |

Pendiente en la máquina: instalar `ComfyUI-GGUF` (specs 261028 lo lista como faltante) y correr la variante GGUF Q4 local con TE offloaded que pide el backlog.

## 10. Prompting por familia + configs generales

Cada familia habla su dialecto; cambiar de modelo implica mover checkpoint + sampler + steps + CFG + negativo como un bloque. Detalle completo: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] §6.

| Familia | Prompt | Negativo | Sampler / sched | Steps | CFG |
|---------|--------|----------|-----------------|-------|-----|
| SDXL (gramática casa) | orden: sujeto → sistema constructivo → materialidad → estilo/medio → encuadre → luz → color → calidad; `(term:1.2)` máx 3 pesos | casa (7 términos); en Juggernaut probar vacío | `dpmpp_2m` + `karras` | 30-40 | 3-7 (4 = fotorreal) |
| RealVisXL v5.0 | igual + token de género fotográfico | el del autor (apunta a ilustración/3D) | `dpmpp_sde` 30+ o `dpmpp_2m` 50+ | 30 / 50+ | 3-4 |
| DiT turbo (Z-Image, Schnell, KREA) | descriptivo completo, prosa corrida | vacío o mínimo | `euler` + `simple` | 4-8 | 1.0 |
| FLUX.2 klein 9B | prosa 40-70 palabras; JSON con bloques cuando hay multi-imagen o repetición | sin negativo (`ConditioningZeroOut`) | `SamplerCustomAdvanced` + `Flux2Scheduler` + `CFGGuider` | 4 destilado / 20 base | 1 / 5 |
| FLUX.2 klein img2img | declarar rol de cada imagen en orden de entrada + `STRICT CAMERA LOCK` / `MATCH CAMERA OF IMAGE 1 EXACTLY` | — | mismo stack Flux | según denoise | 1 / 5 |

## 11. Entrenar en CivitAI vs en el pod

CivitAI entrena en su web (trainer clásico + Training Studio): subir 15-30 imágenes o un zip, auto-caption (tags para SD, lenguaje natural para Flux), elegir base, pagar en Buzz y retirar epochs (máx 20 visibles, retención 30 días; publicar fija un epoch). Motores Kohya / AI-Toolkit / Musubi según base; bases: SD1.5, SDXL (+Pony, Illustrious), Flux.1 Dev, Flux.2 Dev, klein 4B/9B Base, Chroma, Qwen, ZImage; video: Hunyuan, Wan 2.1, LTX2.

Costos de referencia oct-2026 (el precio exacto se muestra antes de enviar): 500 Buzz SD/SDXL/klein 4B (~$0,50) · 1000 klein 9B/Z-Image (~$1) · 2000 Flux.1/Qwen/Chroma (~$2); 1000 Buzz = $1, y el Buzz gratuito ganado también paga.

| | CivitAI on-site | Pod RunPod + ai-toolkit |
|---|---|---|
| Costo LoRA klein 4B | ~$0,50 en Buzz (hasta $0 con Buzz ganado) | ~$0,50-0,70 de GPU |
| Control | parámetros del wizard, hasta 5 corridas en paralelo | total: rank, LR, steps, epochs, samples, cualquier base |
| Dataset | sube a su storage, retención 30 días | volumen cifrado que desaparece al terminar el pod |
| Resultado | epochs 30 días; privado exige membresía; público = descargable por la comunidad | `.safetensors` propio, licencia según base (4B Apache 2.0 publicable) |
| Espera | cola variable, rapid Flux en minutos | 2-3 h por corrida, sin cola |

Veredicto: el LoRA del concurso se entrena en el pod (control + IP + cadena Apache 2.0); CivitAI queda para experimentos rápidos de estilo. Plan completo: [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §4.

Guías oficiales (verificadas 2026-11-02): https://education.civitai.com/using-civitai-the-on-site-lora-trainer · https://education.civitai.com/civitais-guide-to-training-studio/

## Referencias

- Fichas unificadas: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-index|WF-curso/00-index]]
- Matriz: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro]]
- Videos YT: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index|WF-Comfy-YT]] · inpaint: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-01-sdxl-inpainting-diffuseda|YT-01]]
- Research costos: [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|research 2026-11-01]]
