---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, modelos, comparativa, licencias, alternativas]
idioma: es
---

# Modelos SDXL para los 7 WF — qué probar, qué esperar, qué licencia

> Este documento conecta el set `sdxl-vista` con el análisis de modelos del estudio. La regla del set: **un solo modelo intercambiable por corrida** (`ckpt_name` en el nodo 1), seed fija, resto del grafo intacto. Así la comparación mide modelo y nada más.

## 1. Dónde vive el análisis

| Documento | Qué aporta |
|---|---|
| [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos-recomendados v1.4.0]] | Inventario de lo instalado, licencias fila por fila, settings por modelo, tabla de límites |
| [[wiki/estudio/analisis/analisis-ia-generativa-comfyui-alternativas|análisis IA generativa + alternativas]] | Comparativa ComfyUI vs A1111 vs Fooocus, consolas API, opciones $0 |
| [[wiki/glosario/software/proveedores-modelos-ia|proveedores-modelos-ia]] | HF, Civitai, CivArchive, tiers gratis, límites de descarga |
| [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|research 2026-11-01]] | 24 motores, precios por imagen, estado de Midjourney/DALL·E, conocimiento de sitio |
| [[specs/261030-plan-continuacion-pruebas|plan de pruebas]] | Campaña de flujos: fases A–F, gates y costo por corrida |
| [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz del concurso]] | Las filas vivas, los IDs y los segundos medidos |

## 2. Instalados hoy (probables sin descargar nada)

| Modelo | Base | Estado | Comercial | Rinde en | Licencia |
|---|---|---|---|---|---|
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2` | SDXL 6,62 GiB | Instalado | Sí, con cláusula | Los 7 WF | CreativeML Open RAIL-M + cláusula RunDiffusion (prohíbe desplegarlo tras APIs pagas) |
| `realvisxlV50_v50Bakedvae` | SDXL fp16 6,46 GiB | Instalado 2026-11-01 | Sí | WF-01/02/06 (calidad final) | Open RAIL++-M |
| `realvisxlV50_v50LightningBakedvae` | SDXL fp16 destilado 6,46 GiB | Instalado 2026-11-01 | Sí | Barrido rápido y previsualización | Open RAIL++-M |
| `architecturerealmix_v11` | SD 1.5 2,1 GB | Retirado a `_retirados-sin-uso-comercial` | **No** | Exploración interna | Autor prohíbe uso comercial |

Los tres SDXL comparten arquitectura, así que **cualquiera entra en los 7 WF cambiando solo `ckpt_name`**. VAE horneado en los tres.

## 3. Comparativa por WF — qué modelo probar en cada uno

| WF | Juggernaut v9 | RealVisXL v5.0 | RealVisXL Lightning | Candidate externo |
|---|---|---|---|---|
| WF-01 baseline | control del set | **comparar primero** | iteración en 4–6 steps | Natty Realistic SDXL v2.0 |
| WF-02 interior bóveda | bueno | **mejor en interior** | previsualizar luz | RealArchmix XL v3.5 (espacios) |
| WF-03 Rhino → render | bueno | alternativa inmediata | — | **Flux.2 klein 9B + `rhino-to-image`** (RunPod) |
| WF-04 keyframe video | bueno | **mejor piel de imagen** | keyframe rápido | WAN 2.2 I2V / LTX-2.3 (RunPod) |
| WF-05 maqueta 3D | bueno | **mejor fondo neutro** | — | Tripo / Hunyuan3D (imagen → 3D) |
| WF-06 detalle constructivo | bueno | **más nítido** | — | ControlNet Union SDXL |
| WF-07 geometría → piedra | control | **mejor materialidad** | — | Flux.2 klein 9B (edición con referencia) |

## 4. Candidatos a descargar (con criterio de uso)

| Modelo | Tipo | Tamaño | Por qué suma | Link | Estado |
|---|---|---|---|---|---|
| **Natty Realistic SDXL v2.0** | Checkpoint SDXL | 6,46 GiB | Fotorreal general, descarga abierta, espejos en TensorArt/SeaArt | https://civitai.com/models/1884205/natty-realistic-sdxl | Listo para probar |
| **Juggernaut XL v13 Ragnarok** | Checkpoint SDXL | ~6,6 GiB | Mejora anatomía y manos frente a v9/v11 | Buscar "Juggernaut Ragnarok" en Civitai | Verificar descarga antes |
| **RealArchmix XL v3.5** | Checkpoint SDXL fp16 | 6,46 GiB | Espacios + arquitectura + interior + paisaje; compatible con los LoRAs del mismo autor | https://civitai.com/models/1323614?modelVersionId=2066579 | Se destraba con cuenta + token Civitai |
| **RealArchvis XL v5.0** | Checkpoint SDXL | 6,46 GiB | Específico de arquitectura | https://civitai.com/models/533040 | Generation-Only: se consigue en subasta con Buzz; vigilar espejo en CivArchive |
| **ControlNet Union SDXL** | ControlNet | ~1,5 GB | Control geométrico unificado para SDXL; entra en WF-03/06/07 | https://huggingface.co/xinsir/controlnet-union-sdxl-1.0 | Descarga directa |
| **4x_foolhardy_Remacri** | Upscaler | 67 MB | Cierre de lámina sin re-muestrear | https://huggingface.co/uwg/upscaler/tree/main/ESRGAN | Licencia CC BY-NC: solo exploración |
| **4x-ClearRealityV1** | Upscaler | ~70 MB | Alternativa de nitidez para láminas | https://huggingface.co/Kim2091/ClearRealityV1 | Licencia CC BY-NC: solo exploración |

Regla del estudio: para entregables de cliente van **Juggernaut v9, RealVisXL v5.0 y sus LoRAs comerciales**. Todo lo marcado como Generation-Only, NC o sin `allowCommercialUse` confirmado queda en exploración interna.

## 5. El LoRA del curso, que cambia el juego en WF-03

`rhino-to-image-lora.basic.safetensors` (121 MB, rank 16, F32) convierte un **viewport de Rhino** en imagen. Arquitectura Flux 8B (8 double + 24 single blocks, `txt_in` 12288→4096), así que va con **FLUX.2 klein 9B**, no con SDXL.

| Pieza | Archivo | Carpeta |
|---|---|---|
| Modelo base | `flux-2-klein-9b-fp8.safetensors` | `models/diffusion_models/` |
| Text encoder | `qwen_3_8b_fp8mixed.safetensors` | `models/text_encoders/` |
| VAE | `flux2-vae.safetensors` | `models/vae/` |
| LoRA | `rhino-to-image-lora.basic.safetensors` | `models/loras/` |

Consecuencia práctica: **WF-03 tiene dos caminos**. El local (SDXL img2img, denoise 0,65) mide la brecha; el camino Flux corre en RunPod y es el candidato a lámina final. La comparación entre ambos es la decisión de mayor peso del día 2.

## 6. Cómo se prueba un modelo alternativo (protocolo)

1. Copiar el `.json` del WF y cambiar **solo** `ckpt_name`.
2. Mantener seed y prompt del WF: la comparación es modelo contra modelo.
3. Nombrar la salida con el prefijo `gx-<WF>-<modelo>-<seed>`.
4. Registrar en la matriz: modelo, segundos, VRAM observada, veredicto.
5. Dos modelos como máximo por sesión: cada SDXL a 1024² ronda los 7–10 min en la RX 570.

Tiempos medidos de referencia (RX 570, `--lowvram --cpu-vae`): 1216×832 en 609 s; 1216×832 con upscale a 2016×1152 en 1073 s (Juggernaut) y 1165 s (RealVisXL); Lightning en 409 s.

## 7. Qué evaluar en cada comparación

- **Geometría:** las catenarias cierran donde deben; las columnas ramificadas mantienen lógica estructural.
- **Material:** piedra, ladrillo y trencadís se leen como materiales, no como textura.
- **Perspectiva:** líneas verticales rectas, sin edificios fundidos.
- **Luz:** coherencia de sombras entre arcos y suelo.
- **Escala humana:** proporción creíble de personas y vegetación.
- **Artefactos:** manos, barandillas, textos inventados, marcas de agua.

## Referencias

- Set de flujos: [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/01-index|sdxl-vista]]
- Base común: [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/00-base-modelo|00-base-modelo]]
- Plan de pruebas: [[specs/261030-plan-continuacion-pruebas|plan de continuación de pruebas]]
