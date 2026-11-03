---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, modelos, comparativa, licencias, alternativas, prompting]
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
| `realvisxlV50_v50LightningBakedvae` | SDXL fp16 destilado 6,46 GiB | **Descartado 2026-11-02** (R3 WF-01, resultado pésimo) | Sí | — (fuera del set) | Open RAIL++-M |
| `architecturerealmix_v11` | SD 1.5 2,1 GB | Retirado a `_retirados-sin-uso-comercial` | **No** | Exploración interna | Autor prohíbe uso comercial |

Los tres SDXL comparten arquitectura, así que **cualquiera entra en los 7 WF cambiando solo `ckpt_name`**. VAE horneado en los tres.

## 3. Comparativa por WF — qué modelo probar en cada uno

| WF | Juggernaut v9 | RealVisXL v5.0 | RealVisXL Lightning | Candidate externo |
|---|---|---|---|---|
| WF-01 baseline | control del set | **comparar primero** | descartado 2026-11-02 | Natty Realistic SDXL v2.0 |
| WF-02 interior bóveda | bueno | **mejor en interior** | descartado 2026-11-02 | RealArchmix XL v3.5 (espacios) |
| WF-03 Rhino → render | bueno | alternativa inmediata | — | **Flux.2 klein 9B + `rhino-to-image`** (RunPod) |
| WF-04 keyframe video | bueno | **mejor piel de imagen** | descartado 2026-11-02 | WAN 2.2 I2V / LTX-2.3 (RunPod) |
| WF-05 maqueta 3D | bueno | **mejor fondo neutro** | — | Tripo / Hunyuan3D (imagen → 3D) |
| WF-06 detalle constructivo | bueno | **más nítido** | — | ControlNet Union SDXL |
| WF-07 geometría → piedra | control | **mejor materialidad** | — | Flux.2 klein 9B (edición con referencia) |

## 4. Candidatos a descargar (con criterio de uso)

| Modelo | Tipo | Tamaño | Por qué suma | Link | Estado |
|---|---|---|---|---|---|
| **Natty Realistic SDXL v2.0** | Checkpoint SDXL | 6,46 GiB | Fotorreal general, descarga abierta, espejos en TensorArt/SeaArt | https://civitai.com/models/1884205/natty-realistic-sdxl | Listo para probar |
| **Juggernaut XL Ragnarok** | Checkpoint SDXL | 6,62 GiB | Versión actual del video YT-01 (modelVersionId 1759168, `juggernautXL_ragnarok.safetensors`, SHA256 verificado) | https://civitai.com/models/133005 | **Instalado 2026-11-02** |
| **RealArchmix XL v3.5** | Checkpoint SDXL fp16 | 6,46 GiB | Espacios + arquitectura + interior + paisaje; compatible con los LoRAs del mismo autor | https://civitai.com/models/1323614?modelVersionId=2066579 | Se destraba con cuenta + token Civitai |
| **RealArchvis XL v5.0** | Checkpoint SDXL | 6,46 GiB | Específico de arquitectura | https://civitai.com/models/533040 | Generation-Only: se consigue en subasta con Buzz; vigilar espejo en CivArchive |
| **ControlNet Union SDXL (promax)** | ControlNet | 2,34 GiB | El del video YT-01 (`XL_controlnet-union-sdxl_promax.safetensors`); entra en WF-03/06/07 | https://huggingface.co/xinsir/controlnet-union-sdxl-1.0 | **Instalado 2026-11-02** |
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

## 6. Prompting por modelo — lo que documenta cada creador

> Los tres SDXL instalados comparten arquitectura, y cada autor publica una receta propia: negativo, sampler, steps y hasta tokens de género fotográfico. Esta sección reúne lo que dicen las fichas oficiales (verificadas 2026-11-02) y marca lo que queda por confirmar. Cambiar de modelo en un WF implica mover **checkpoint + sampler + steps + CFG + negativo** como un bloque.

### 6.1 Gramática común de SDXL (base del set)

Orden que rinde en los 7 WF: `sujeto → sistema constructivo → materialidad → estilo/medio → encuadre → luz → color → calidad`. Lo que aparece primero pesa más: la tipología y el material van al inicio, el adjetivo de calidad queda al final.

| Recurso | Sintaxis | Cuándo |
|---|---|---|
| Refuerzo leve | `(term)` | una palabra clave que el modelo ignora |
| Refuerzo explícito | `(term:1.2)` | sistema constructivo o materialidad |
| Atenuación | `[term]` o `(term:0.8)` | un tag que satura |

Tres pesos como máximo: cuatro pesos señalan un prompt mal ordenado, no falta de énfasis. Negativo de la casa, el que ya traen los 7 WF: `blurry, low quality, distorted, watermark, text, cartoon, illustration, oversaturated`.

### 6.2 Juggernaut XL v9 — el modelo que pide poco negativo

Ficha oficial: [HF RunDiffusion/Juggernaut-XL-v9](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9).

| Parámetro | Documentado por el autor |
|---|---|
| Negativo | **arrancar vacío** y agregar solo lo que aparezca en la imagen; los negativos cargados restan más de lo que suman |
| Steps / CFG | 30–40 · 3–7 (CFG bajo = más realismo) |
| Sampler | DPM++ 2M Karras |
| Resolución | 832×1216 retrato · 1216×832 paisaje |
| VAE | horneado |
| Hi-res | `4xNMKD-Siax_200k` · 15 steps · denoise 0,3 · 1,5× |

Tokens que el autor declara útiles: `Architecture Photography`, `Interior Photography`, `Landscape Photography`, `Hyperdetailed Photography`, `Cinematic Movie`, `Still Mid Shot Photo`. Estilo: frase descriptiva corrida con el token de género fotográfico al cierre.

Desvío consciente del set: nuestros WF llevan negativo de 7 términos. Prueba barata que queda agendada: **misma seed y mismo prompt con negativo vacío**, para medir si el negativo de la casa suma o estorba en este modelo.

### 6.3 RealVisXL v5.0 — negativo obligatorio y sampler con nombre propio

Ficha oficial: [Civitai 139562](https://civitai.com/models/139562/realvisxl-v50) · espejo [HF SG161222/RealVisXL_V5.0](https://huggingface.co/SG161222/RealVisXL_V5.0).

Estado en el set: **descartado 2026-11-02** (R3 WF-01, resultado pésimo). La receta queda como referencia del autor, no como recomendación.

| Parámetro | Documentado por el autor |
|---|---|
| Negativo (foto, Civitai) | `(worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth` |
| Negativo (retrato, HF) | `bad hands, bad anatomy, ugly, deformed, (face asymmetry, eyes asymmetry, deformed eyes, deformed mouth, open mouth)` |
| Estándar | DPM++ SDE Karras **30+ steps** · o DPM++ 2M Karras **50+ steps** |
| Lightning | DPM++ SDE Karras o DPM++ SDE · **4–6 steps** · CFG **1–2** |
| Hi-res | DPM++ 2M Karras · 25+ steps de hires · `4x-NMKD-Superscale-SP_178000_G` o `4x-UltraSharp` · denoise 0,1–0,3 · 1,1–1,5× |
| Extras | Clip skip 1 · ENSD 31337 |

El CFG del estándar queda a criterio: la ficha describe sampler y steps, y el 3–4 del set viene de la tabla de límites del estudio. Para arquitectura conviene el negativo de Civitai (apunta a ilustración y 3D, que es lo que rompe una fachada); el de HF está pensado para rostros.

Consecuencia sobre el set: nuestro `dpmpp_2m` + 30–35 steps queda **por debajo** de los 50+ que el autor pide para ese sampler. Tres caminos:

1. mantener `dpmpp_2m` y subir a 50 steps (más lento, ~+60 % de tiempo de muestreo);
2. pasar a `dpmpp_sde` + `karras` a 30 steps — el estándar que el autor nombra primero;
3. seguir con 30/4 y asumir que la corrida mide el modelo bajo la receta de la casa.

La corrida 2 del protocolo usa el camino 3 a propósito: mide modelo, no receta. El camino 2 queda como corrida 4 opcional.

Lightning a 30 steps y CFG 4 sale lavado porque el destilado está calibrado para 4–6 steps y CFG 1–2; los 409 s medidos corresponden a esa receta corta, no a la larga.

### 6.4 Natty Realistic SDXL v2.0 — la receta más corta

Ficha oficial: [Civitai 1884205](https://civitai.com/models/1884205/natty-realistic-sdxl).

| Parámetro | Documentado por el autor |
|---|---|
| Steps | 24–31 (prefiere 31) |
| CFG | 3–5 |
| Sampler | Euler a Normal · DPM++ 2M Normal · DPM++ 2M Karras |
| Detalle de rostro | detailer YOLOv2 (en ComfyUI equivale a FaceDetailer del Impact Pack; los 7 WF trabajan sin detailer) |
| Negativo | la ficha presenta receta de sampler y steps; el negativo de la casa cubre el resto |

Ventaja operativa: 24–31 steps entra en la ventana de 30 del set, así que este candidato se prueba sin tocar la receta.

### 6.5 RealArchmix XL v3.5 y RealArchvis XL v5.0 — fichas por verificar

Las páginas quedan detrás de cuenta o de Generation-Only, así que su prompting documentado sigue **sin verificar**. Mientras tanto rige la gramática SDXL con negativo de la casa, y cualquier token que publique el autor se anota en la matriz al momento de la descarga. Ambas fichas comparten la advertencia de licencia de la §2.

### 6.6 Flux.2 klein 9B + `rhino-to-image` — otro dialecto

Fuente interna: `.opencode/skills/comfy-prompting/references/flux2.md`; docs BFL en las referencias. Klein trabaja **sin prompt negativo** y sin upsampling de prompt: lo que se escribe es lo que recibe.

| Parámetro | klein 9B |
|---|---|
| Estilo | prosa de 40–70 palabras; JSON estructurado cuando hay varias imágenes o repetición entre corridas |
| Negativo | sin prompt negativo; el nodo `ConditioningZeroOut` cumple esa función |
| Steps / CFG | 4 / 1 destilado · 20 / 5 base |
| Sampler | `SamplerCustomAdvanced` + `Flux2Scheduler` + `CFGGuider` |
| Referencias | hasta 4 imágenes |
| Escala de entradas | geometría a 1,0 MP · referencia de material a 0,5 MP |

Reglas que este modelo sí escucha: declarar el rol de cada imagen **en el orden en que entran** ("massing y cámara de la imagen 1, material y temperatura de color de la imagen 2") y blindar la cámara con `STRICT CAMERA LOCK` + `MATCH CAMERA OF IMAGE 1 EXACTLY`.

### 6.7 Resumen operativo para los 7 WF

| Modelo | Negativo | Steps | CFG | Sampler |
|---|---|---|---|---|
| Juggernaut v9 | vacío (por probar) | 30–40 | 3–7 | `dpmpp_2m` + `karras` |
| RealVisXL v5.0 | el del autor (§6.3) | 30 con SDE · 50+ con 2M | 3–4 | `dpmpp_2m` o `dpmpp_sde` |
| RealVisXL Lightning (descartado 2026-11-02) | el del autor (§6.3) | 4–6 | 1–2 | `dpmpp_sde` + `karras` |
| Natty v2.0 | el de la casa | 24–31 | 3–5 | `euler_a` o `dpmpp_2m` |
| Flux.2 klein 9B | — | 4 destilado · 20 base | 1 · 5 | `SamplerCustomAdvanced` |

## 7. Cómo se prueba un modelo alternativo (protocolo)

1. Copiar el `.json` del WF y cambiar **solo** `ckpt_name`.
2. Mantener seed y prompt del WF: la comparación es modelo contra modelo.
3. Nombrar la salida con el prefijo `gx-<WF>-<modelo>-<seed>`.
4. Registrar en la matriz: modelo, segundos, VRAM observada, veredicto.
5. Dos modelos como máximo por sesión: cada SDXL a 1024² ronda los 7–10 min en la RX 570.

Tiempos medidos de referencia (RX 570, `--lowvram --cpu-vae`): 1216×832 en 609 s; 1216×832 con upscale a 2016×1152 en 1073 s (Juggernaut) y 1165 s (RealVisXL); Lightning en 409 s.

## 8. Qué evaluar en cada comparación

- **Geometría:** las catenarias cierran donde deben; las columnas ramificadas mantienen lógica estructural.
- **Material:** piedra, ladrillo y trencadís se leen como materiales, no como textura.
- **Perspectiva:** líneas verticales rectas, sin edificios fundidos.
- **Luz:** coherencia de sombras entre arcos y suelo.
- **Escala humana:** proporción creíble de personas y vegetación.
- **Artefactos:** manos, barandillas, textos inventados, marcas de agua.

## 9. Cómo se descargan los modelos (método verificado 2026-11-02)

- Token: `CIVITAI_API_TOKEN` en `.env` raíz (preset **Read Only** alcanza: incluye ModelsRead; el tope de Buzz no aplica a descargas; sin límite publicado salvo 429 anti-abuso).
- Método que funcionó: `curl.exe -L -C - --retry 5 -H "Authorization: Bearer $t"` (reanuda con `-C`; el primer intento de Ragnarok se cortó a 0,66 GB y se completó así).
- Verificar siempre: tamaño en GB + SHA256 cuando el hash oficial se conoce (Ragnarok `dd08fa32…` = mismos bytes que el video YT-01); después R en el navegador de ComfyUI.
- Pendiente: el `download_model` del agente sigue sin poder anclar el `models/` (el servidor reporta `main.py` relativo). Fix: lanzar con ruta absoluta (`"%COMFYUI_PATH%\main.py"` en el `.bat`) + reiniciar ComfyUI + reconectar MCP.

## Referencias

- Set de flujos: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/01-index-sdxl-vista|sdxl-vista]]
- Base común: [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-base-modelo|00-base-modelo]]
- Plan de pruebas: [[specs/261030-plan-continuacion-pruebas|plan de continuación de pruebas]]
- Fichas de modelo (verificadas 2026-11-02):
  - Juggernaut XL v9 — https://huggingface.co/RunDiffusion/Juggernaut-XL-v9
  - RealVisXL V5.0 — https://civitai.com/models/139562/realvisxl-v50 · https://huggingface.co/SG161222/RealVisXL_V5.0
  - Natty Realistic SDXL — https://civitai.com/models/1884205/natty-realistic-sdxl
- Prompting por familia (skill interno del estudio): `.opencode/skills/comfy-prompting/references/sd15-sdxl.md` · `flux2.md` · `workflows-por-modelo.md`
- FLUX.2 prompting (BFL): https://docs.bfl.ai/guides/prompting_guide_flux2 · https://help.bfl.ai/articles/7592221790-how-do-i-generate-quickly-with-flux-2-klein
