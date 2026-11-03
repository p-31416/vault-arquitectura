---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: 10 prompts prueba Nexus — visión, estructura, requisitos y qué probamos
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: borrador-activo
tags: [concurso, gaudi-nexus, comfyui, prompts, sdxl, flux, yt]
idioma: es
---

# 10 prompts prueba Nexus — visión / estructura / requisitos

> Fuente: dictado Sol 2026-11-02 + [[proyectos/concurso-gaudi-nexus/03-programa-punto-a-punto|programa]] + [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos]]. Cada ficha trae visión (qué se ve), estructura (nodos), requisitos (modelo + VRAM + dónde corre) y qué probamos. Reporte de resultados en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]]. Formas de fijar Sagrada en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/11-diez-formas-sagrada-familia|11-diez-formas-sagrada-familia]].

Regla estudio: láminas solo con modelos ✅ (Juggernaut v9, RealVisXL v5.0 + Lightning, inpainting, ControlNets lllyasviel). ArchitectureRealmix solo tests internos (⛔ comercial).

## P-01 captura Google + dibujo encima → foto intervenida

- **Visión:** captura aérea Plaza Sagrada Familia con trazo triangular fractal encima, Sagrada intacta al fondo.
- **Estructura:** LoadImage → ImageScale 512 (R1 SD1.5) / 1.0 MP (R2 FLUX) → ControlNet scribble + canny → KSampler img2img denoise 0.4–0.6 → VAEDecode → Save.
- **Requisitos:** local SDXL Juggernaut v9 o RealVis Lightning 4–6 pasos CFG 1–2. Pod opcional FLUX.2 klein 9B si hay 18 GB.
- **Prompt ES/EN:** `aerial plaza in front of Sagrada Familia Passion facade, keep silhouette intact, thin triangular fractal paving overlay, market stalls, photorealistic, morning light / vista aérea plaza frente Pasión, mantener silueta intacta, teselado triangular fino, puestos, fotorrealista`.
- **Qué probamos:** si respeta geometría Sagrada con denoise 0.5 vs 0.65.

## P-02 croquis → fotorrealista (Rhino-to-image)

- **Visión:** masa cruda Rhino + foto material (hormigón crudo Pasión + textil) → render fotorrealista, geometría clavada.
- **Estructura:** 2× LoadImage (geometría 1.0 MP + material 0.5 MP lanczos) → ControlNet depth + canny → KSampler denoise 0.75 → upscale RealESRGAN + 2º denoise 0.2.
- **Requisitos:** pod FLUX.2 / local SDXL Juggernaut para prueba rápida con denoise 0.6.
- **Prompt:** `walkable parabolic shell plaza, catenary vault stone + ceramic trencadis fractal paving, Sagrada Familia background intact, photorealistic 35mm f8 morning`.
- **Qué probamos:** fidelidad formal (lock geométrico) vs riqueza material.

## P-03 croquis → croquis mejorado (no fotorrealista)

- **Visión:** mismo croquis, línea más limpia, sombras suaves, sigue siendo dibujo.
- **Estructura:** LoadImage → ControlNet scribble weight 0.7 → KSampler denoise 0.3–0.4 + LoRA `markerhandsketch-V1` 0.5 → Save sin upscale.
- **Requisitos:** local SD1.5 ArchitectureRealmix (solo interno) o SDXL + marker LoRA. 512² R1.
- **Prompt:** `clean architectural marker sketch, same viewpoint, catenary shells, thin lines, soft shadows, not photorealistic`.
- **Qué probamos:** denoise bajo que no inventa, útil para iterar con Emilia.

## P-04 inpainting plaza: borrar autos / poner verde

- **Visión:** misma foto plaza, autos fuera, arbustos en ausencias fractal.
- **Estructura:** LoadImage + máscara → `sd-v1-5-inpainting-fp16` → KSampler denoise 0.8 solo máscara → Save. Ver [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-01-sdxl-inpainting-diffuseda|YT-01]].
- **Requisitos:** local, 2 GB VRAM. Ideal RX 570.
- **Prompt máscara:** `shrubs in fractal gaps, permeable paving, no cars`.
- **Qué probamos:** máscara manual vs auto (SAM) y coherencia borde.

## P-05 puesto 1 apoyo: masa → tensado austero

- **Visión:** mástil único + membrana triangular, hormigón crudo + textil, 3 tipos.
- **Estructura:** txt2img base SDXL 1216×832 30 pasos → img2img ControlNet canny 0.6 para variantes.
- **Requisitos:** local RealVisXL v5.0 estándar 30–35 pasos CFG 3–4 / Lightning para R rápida.
- **Prompt:** `single-mast tensile market stall, raw concrete base Passion facade texture, technical textile membrane, triangular, austere, Sagrada Familia far background`.
- **Qué probamos:** 3 tipos = 3 fachadas, agregación de a 1 / de a varias.

## P-06 vecinal -1 m: sección cáscara acústica + techo verde

- **Visión:** corte cáscara catenaria invertida, descubierto → semicubierto → cubierto -1 m con techo verde arriba, 50 dentro + 100 fuera.
- **Estructura:** img2img desde sección Rhino + ControlNet depth fuerte 0.8.
- **Requisitos:** local SDXL + depth Anything 3. Pod FLUX para final.
- **Prompt:** `inverted catenary shell section, acoustic panels, green roof above, open semi-covered covered sequence descending 1m, neighbors gathering`.
- **Qué probamos:** legibilidad sección vs invento IA.

## P-07 mirador recorrido: estación lejos / estación cerca (zoom)

- **Visión:** 2 encuadres misma lengua: lejos obra completa + cerca material Pasión.
- **Estructura:** mismo seed, 2 prompts, ControlNet depth fijado para no mover geometría.
- **Requisitos:** local Lightning 4 pasos para iterar zoom, estándar para final.
- **Prompts:** `distant view entire Sagrada Familia from fractal path lookout` / `close-up raw concrete Passion texture, analytical framing`.
- **Qué probamos:** zoom fractal sin que cambie Sagrada (ver 10 formas).

## P-08 cocina bóvedas: interior 2 cocinas

- **Visión:** salita abovedada con 2 cocinas independientes, 20+20, vapor y luz cálida.
- **Estructura:** txt2img interior SDXL + IPAdapter material ladrillo/bóveda si hay.
- **Requisitos:** local Juggernaut 1216×832.
- **Prompt:** `small vaulted community kitchen, two independent kitchens, 20 people each, fresh market produce, warm light`.
- **Qué probamos:** aforo creíble y extracción visible.

## P-09 oficina vidrio en T: interior moderno teselado

- **Visión:** caja vidrio en cruce T, muebles teselados encastrables, 8 puestos.
- **Estructura:** txt2img interior + ControlNet canny muebles.
- **Requisitos:** local RealVisXL.
- **Prompt:** `glass office box at plaza crossing, 8 workstations, interlocking triangular furniture, modern open, Sagrada glimpse through glass`.
- **Qué probamos:** transparencia sin reflejos que tapan.

## P-10 lengua-puente vidrio + estereoestructura ramificada

- **Visión:** piso fino con patrón + ramificación biomímica vidrio casi invisible uniendo 3 fachadas y dos parques.
- **Estructura:** img2img aérea + ControlNet scribble del puente dibujado a mano.
- **Requisitos:** pod FLUX ideal / local SDXL denoise 0.5.
- **Prompt:** `thin patterned floor linking three facades, branching glass stereostructure almost invisible, biomimetic, connecting two parks, Sagrada intact`.
- **Qué probamos:** "pasa desapercibida" vs protagonista.

## Modelos: cuándo SDXL local vs Flux pod vs cuantizado

| Caso | Modelo | Dónde | Por qué |
|------|--------|-------|---------|
| Iterar rápido P-03/P-04/P-07R | RealVisXL Lightning 4–6 pasos CFG 1–2 | local RX 570 | minutos, no 651 s |
| Calidad final P-02/P-05/P-06 | RealVisXL v5.0 30–35 pasos / Juggernaut v9 | local | ✅ comercial, BakedVAE (vae vacío) |
| Geometría + material fino | FLUX.2 klein 9B fp8 + Qwen3-8B | pod | 18.3 GB, no entra local |
| Cuantizado liviano futuro | Z-Image Turbo GGUF Q4_K_S ~4 GB / Flux schnell GGUF Q4 ~8 GB | local/pod | 8 pasos turbo, Apache 2.0, probar como alternativa Lightning |
| Inpaint liviano | sd-v1-5-inpainting-fp16 | local | 2 GB, ideal RX 570 |

Flags RX 570 verificados: `--directml 0 --force-fp16 --disable-cuda-malloc --lowvram --cpu-vae`.

---
*Más nuevo → más arriba. Log: 2026-11-02 creación set 10 prompts desde dictado Sol + matriz pruebas + modelos-recomendados.*
