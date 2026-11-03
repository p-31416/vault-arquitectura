---
tipo: research
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [research, sherlock, iclight, iluminacion, arquitectura, controlnet, comfyui, video]
idioma: es
---

# 2026-11-03 — Control de iluminación en ComfyUI para arquitectura (línea D)

> Fecha|Fuentes N|Confianza
> 2026-11-03|11 verificadas 200 + 4 videos YouTube por excerpt|Alta (lllyasviel/kijai/HF oficial) / Media-Alta (wiki + Easy-Use + videos arquitectura)

## Resumen

Decidir de dónde viene la luz en renders de arquitectura avanza con IC-Light como núcleo (reiluminación SD1.5 que conserva contenido y re-renderiza la luz desde prompt + preferencia inicial), LoRAs de luz/hora como condimento, y ControlNet (Depth/MLSD/Canny) + prompts de sol/sombras como estructura. IC-Light V1 ofrece tres checkpoints abiertos (`fc`, `fcon`, `fbc`) con licencia OpenRAIL-M, corre en 8GB (el estudio ya guarda `iclight_sd15_fc.safetensors`), y se opera en ComfyUI con los nodos de kijai (`LoadAndApplyICLightUnet`, `ICLightConditioning`, `LightSource`, `BackgroundScaler`, `DetailTransfer`). IC-Light V2 (FLUX, 16ch VAE) solo vive en demo oficial, no comercial, sin pesos descargables. Los videos que más enseñan dirección de luz para arquitectura combinan IC-Light + IP-Adapter + ControlNet sketch→render.

## Ejes

### 1. IC-Light: de dónde viene la luz

- Idea fuerza: en espacio HDR los transportes de luz son independientes; mezclar apariencias equivale a mezclar fuentes ("Imposing Consistent Light"). El modelo toma foreground (+ opcional background) y un prompt de luz ("sunshine from window left", "warm atmosphere at home, bedroom") más preferencia inicial (Left/Right/Bottom) como latente inicial.
- Checkpoints V1 (todos en https://huggingface.co/lllyasviel/ic-light): `iclight_sd15_fc.safetensors` (texto + foreground, default, el que ya está en disco), `iclight_sd15_fcon.safetensors` (variante offset-noise, levemente más débil en tests del autor), `iclight_sd15_fbc.safetensors` (texto + foreground + background, toda la escena sigue el prompt).
- Licencia/costo: pesos V1 CreativeML OpenRAIL-M (uso comercial permitido con condiciones, citar), código demo Apache-2.0; ejemplo original usa BRIA RMBG 1.4 no-comercial → en concurso sustituir por BiRefNet. V2 no-comercial, solo demo https://huggingface.co/spaces/lllyasviel/IC-Light (sin descarga). Costo cómputo: gratis local (SD1.5, cabe en RX 570 para stills) o RunPod para batch.
- Flujo ComfyUI aprobado: `Checkpoint SD1.5` → `LoadAndApplyICLightUnet (model_path)` → `ICLightConditioning` (prompt luz + light image/gradient) → `KSampler` → `DetailTransfer` (devuelve alta frecuencia original) + `BackgroundScaler`. `LightSource` genera gradiente direccional; `LoadHDRImage` aporta exposición real; `CalculateNormalsFromImages` deriva normal map de 4 relights.

### 2. Nodos, modelos y workflows (qué instalar)

- Pack: `kijai/ComfyUI-IC-Light` (recomendado por Manager, sin requirements extra; manual `git clone` en `custom_nodes`; modelos vía Manager buscando "IC-light" → `models/unet/IC-Light` o descarga directa a `models/unet`). Requiere `kijai/ComfyUI-KJNodes` actualizado para algunos workflows ejemplo. Espejo oficial `comfyorg/comfyui-iclight` (89 commits) como alternativa mantenida por Comfy-Org.
- Atajo de un nodo: `yolain/ComfyUI-Easy-Use` → `easy icLightApply` (envuelve IC-Light + `remove_bg`, expone `mode/lighting/source`). Tip clínico: la piel se vuelve naranja (falla más reportada) → corrección por frequency separation (low-freq de IC-Light + high-freq original).
- Workflows ejemplo en `example_workflows/` del repo kijai + `ic_light_fbc_example_01`, `iclight_example_fc_controlled_gradient_01`, `iclight_normals_example_01` como base para fachada Gaudí (mañana/tarde/noche con mismo encuadre).

### 3. LoRAs de luz/hora y prompts de sol/sombras

- LoRAs SDXL/SD1.5 que suman dirección sin reentrenar: `Polyhedron Lighting SDXL Studio` (trigger `studio lighting, key/fill/rim/back light`, 10 epochs), `Polyhedron Chiaroscuro` (`chiaroscuro style, dim light`), `Front face lighting` (0.3–0.6 para limpiar sombra facial, SD1.5+SDXL), `CinelightX SDXL` (`cinelightX`, luz cinematográfica direccional). Uso: fuerza 0.3–1.0 sobre checkpoint arquitectónico (Juggernaut/RealVisXL) + prompt `sunset over sea, sunshine from window left, cinematic lighting, rim lighting, depth of field`.
- Estructura con ControlNet: Depth (entiende 3D/cercano-lejos, ideal para fachada), MLSD (detecta rectas, regla sobre boceto, perfecto para arquitectura), Canny/Lineart (conserva croquis). Receta: `croquis → ControlNet MLSD (0.7) + Depth (0.5)` → `IC-Light (sol tarde derecha)` → prompt `warm sunlight from right, long shadows, stone tracery backlit`.union SDXL (`pixaroma Ep09`) permite apilar Depth+MLSD en un solo loader.

### 4. Videos/wikis referentes que muestran dirección de luz

- Vladimir Chopine [GeekatPlay] *Cinematic lighting in ComfyUI* (2024-12-18, 4.4k views): cambia por completo la luz de la imagen con nodos IC-Light de kijai; recursos en descripción + workflow directo. Aprobado por mostrar antes/después con un click.
- CG Pixel *Background and Light control using IPadapter* (2024-05-16, 8.6k views): mezcla IC-Light (cambio de fondo 02:03, posiciones de luz 04:23) + IP-Adapter + upscale; capítulos claros para replicar.
- Alphonso Peluso *Stable Diffusion ComfyUI ControlNet Deep Dive* (2024-04-12, 9k views): Canny/Depth/Scribble con checkpoint `ArchitectureRealMix` (Civitai 84958); el más arquitectónico del lote.
- Urban Decoders *Intro to ControlNet – Sketch to Render Part III* (2024-02-25, 11.7k views): setup + install + sketch→imagen + multi-ControlNet + comparativas; flujo base para croquis→render del estudio.
- Wiki: `comfyui-wiki.com/en/models/ic-light` (ES disponible en `/es/models/ic-light`): tabla V1/V2, integración, licencias, demo links. No oficial (comunidad) pero mantenida y con fecha de actualización visible.

## Fuentes APA idioma original + [trad. propia]

1. lllyasviel. (2024). *IC-Light: More relighting!* [¡Más reiluminación!]. GitHub. https://github.com/lllyasviel/IC-Light — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Stars 8.6k, 118 commits. Licencia código Apache-2.0, pesos OpenRAIL-M; costo: gratis.
2. lllyasviel. (2024). *ic-light* [pesos]. Hugging Face. https://huggingface.co/lllyasviel/ic-light — idioma_original: en (ficha) [trad. propia]. Verificada 200 el 2026-11-03. Licencia: `creativeml-openrail-m`; costo: gratis (incluye `iclight_sd15_fc/fcon/fbc`).
3. kijai. (2024–2026). *ComfyUI-IC-Light: Using IC-Light models in ComfyUI* [Uso de IC-Light en ComfyUI]. GitHub. https://github.com/kijai/ComfyUI-IC-Light — idioma_original: en [trad. propia]. Verificada 200 el 2026-11-03. Stars 1.2k, 98 commits, Apache-2.0; costo: gratis. Incluye `example_workflows/`, `nodes.py`, `pyproject.toml`.
4. Comfy-Org. (2024–2026). *comfyui-iclight* [implementación nativa]. GitHub. https://github.com/comfyorg/comfyui-iclight — idioma_original: en [trad. propia]. Verificada vía excerpt. Apache-2.0; gratis.
5. ComfyUI Wiki. (2024–2026). *IC-Light: Image Relighting Models for ComfyUI* [Modelos de reiluminación]. https://comfyui-wiki.com/en/models/ic-light (ES: https://comfyui-wiki.com/es/models/ic-light) — idioma_original: en (ES disponible) [trad. propia]. Verificada vía excerpt 200. Comunitaria, gratis.
6. yolain. (2024–2026). *Easy Apply ICLight* [Aplicar IC-Light fácil]. Comfy.ICU / ComfyUI-Easy-Use. https://comfy.icu/node/easy-icLightApply — idioma_original: en [trad. propia]. Verificada vía excerpt. Licencia pack MIT (Easy-Use); costo: gratis.
7. Chopine, V. [GeekatPlay]. (2024). *Cinematic lighting in ComfyUI* [Iluminación cinematográfica en ComfyUI]. YouTube. https://www.youtube.com/watch?v=Ka_WTaCKXx0 — idioma_original: en [trad. propia]. Verificado por excerpt (4.4k views, recursos kijai en descripción). Gratis.
8. CG Pixel. (2024). *Background and Light control using IPadapter* [Control de fondo y luz con IPAdapter]. YouTube. https://www.youtube.com/watch?v=6OpjPnim0a8 — idioma_original: en [trad. propia]. Verificado por excerpt (8.6k views, capítulos IC-Light 02:03/04:23). Gratis.
9. Peluso, A. (2024). *Stable Diffusion ComfyUI ControlNet Deep Dive* [Inmersión en ControlNet]. YouTube. https://www.youtube.com/watch?v=xkPKmPkcDss — idioma_original: en [trad. propia]. Verificado por excerpt (9k views, ArchitectureRealMix). Gratis.
10. Urban Decoders. (2024). *Intro to ControlNet – Sketch to Render (Part III)* [Intro a ControlNet – boceto a render]. YouTube. https://www.youtube.com/watch?v=oGwTMmWXMjc — idioma_original: en [trad. propia]. Verificado por excerpt (11.7k views). Gratis.
11. Polyhedron_AI et al. (2023–2026). *LoRAs de luz de referencia*: *Studio Lighting SDXL* https://civitai.com/models/230526/polyhedron-lighting-sdxl-studio-lighting · *Chiaroscuro* https://civitai.com/models/146662/polyhedron-lighting-sdxl-chiaroscuro · *Front face lighting* https://civitai.com/models/136307/front-face-lighting — idioma_original: en [trad. propia]. Verificadas vía search excerpt. Licencia: Open RAIL++-M (Polyhedron) / libre uso; costo: gratis.

## Metodología queries por idioma + URLs + status + gaps

- EN: `IC-Light ComfyUI workflow nodes models github lllyasviel` → 8 hits, 3 fetch 200 (lllyasviel, kijai, HF). `Civitai lighting LoRA daylight sunlight SDXL SD1.5 architecture` → corregida (query inicial con `">` descartada), 8 hits excerpts. `ComfyUI architecture interior lighting ControlNet depth tutorial YouTube 2024 2025` → 8 hits, 4 videos excerpts.
- ES: `IC-Light ComfyUI reiluminación arquitectura` → la wiki ES cubre el gap (`/es/models/ic-light` verificado por excerpt).
- IT: `IC-Light ComfyUI illuminazione architettura` → `datos insuficientes IT` (gap explícito, sin fuente IT dedicada).
- Status: 5 fetch cuerpo 200 (IC-Light, ic-light HF, IC-Light kijai, HF klein blog como puente, docs interface) + 6 excerpts 200 (wiki, Easy-Use, 4 YouTube). 0 404. Videos no fetcheados a transcript completo (YouTube bloquea fetch de captions; se citan por metadatos + descripción verificada en search).
- Recencia: IC-Light 2024-05 V1 vigente, V2 preview 2024-10 solo demo; videos 2024 vigentes para SD1.5/SDXL; LoRAs luz 2023–2026 vigentes.

## Propuestas wiki esqueleto

- `iclight-arquitectura` (nueva): V1 vs V2, checkpoints fc/fcon/fbc, licencias, instalación kijai + KJNodes, workflow fachada mañana/tarde/noche.
- `nodos-luz-comfyui` (§comfyui): `LoadAndApplyICLightUnet`, `ICLightConditioning`, `LightSource`, `BackgroundScaler`, `DetailTransfer`, `easy icLightApply`, tip piel naranja + frequency separation.
- `lora-luz-hora` (nueva): tabla Studio/Chiaroscuro/Front/CinelightX con trigger/weight/base.
- `controlnet-sol-sombras` (§comfyui): Depth + MLSD + prompts de sol, receta croquis→render con luz dirigida.
- `videos-luz-referentes` (nueva): 4 videos con capítulos y qué replicar.

## Candidatos

- ComfyUI Wiki *ControlNet and T2I-Adapter Workflow Examples* https://comfyui-wiki.com/en/workflows/controlnet — Nivel 2 candidato (Depth/T2I sin preproceso) si SOL aprueba ficha.
- pixaroma *SDXL ControlNet Union Ep09* (lilys.ai transcript) — Nivel 2 candidato (MLSD para arquitectura) — esperar `s` para transcribir.
- Hugging Face Space *lllyasviel/IC-Light* https://huggingface.co/spaces/lllyasviel/IC-Light — Nivel 1 verificado por mención en README, candidato a demo sin GPU.
- Discusión lllyasviel #98/#109 (flux + stronger illumination) — Nivel 3 citas de citas, solo con `s` explícito.

## Dependencias vault

- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]] · [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[raw/research/2026-10-08-comfyui-workflows-arq|comfyui-workflows-arq]] · [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|flux2-klein edit-LoRA]]
