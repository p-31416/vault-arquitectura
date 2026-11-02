---
tipo: log
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [sesion, ia-generativa, comfyui, analisis, mvp_04, workflows, higgsfield]
---

# 2026-11-01 — Sesión: IA generativa, alternativas y flujo img2video (MVP_04)

## Qué se hizo

1. **Research**: alternativas a ComfyUI/ComfyUI Cloud/Higgsfield → matriz de UIs locales (A1111, Forge, Fooocus, InvokeAI), consolas API pay-per-use (Open Higgsfield explicado leyendo docs+consola live), opciones $0 (AI Horde, Cloudflare Workers AI).
2. **Comparativa A1111 vs ComfyUI vs Fooocus** por ControlNet/LoRA/inpainting/upscaling → ComfyUI gana 4/4 y es el único vivo; decisión: mantener hub.
3. **Piloto YT (71 videos ComfyUI)** del Takeout 2026-10-08: análisis temático → 12 grupos de flujos (G1-G12) con orden de construcción JSON sugerido. Sol fijó su propio orden: txt2img → img2img → **img2video (nube)** → img2 3D.
4. **Construcción flujo 3**: txt2img e img2img ya existían; se creó `n_07-img2video` con WF_v1.0 (LTX 2.3 i2v, JSON + docs estándar). img2 3D queda en backlog del 04 de n_07.
5. Decisión pendiente de prueba: RunPod **no se usa todavía** (SKO); ComfyUI local estaba apagado al cerrar → validación `/object_info` (R4) pendiente para la primera corrida.

## Archivos modificados

| Archivo | Acción |
|---|---|
| `wiki/estudio/analisis/analisis-ia-generativa-comfyui-alternativas.md` | **nuevo** — informe comparativo completo |
| `wiki/estudio/analisis/00-index.md` | nueva sección IA + fecha + fila ADR-relación |
| `proyectos/MVP_04-comfyui-arquitectura/n_07-img2video/` | **nuevo** — 01-index + WF_v1.0_ltx_i2v/{workflow JSON, 02-WF-log, 03-nodos, 04-backlog} |
| `proyectos/MVP_04-comfyui-arquitectura/00-index.md` | link a n_07 + fecha |

## Análisis cerebro-digital

**Topics:** alternativas-ia-imagen, open-higgsfield-api, pay-per-use-vs-suscripcion, ai-horde-floss, comfyui-vs-a1111-vs-fooocus, controlnet-lora-inpaint-upscale, piloto-yt-comfyui-71, grupos-flujos-G1-G12, txt2img-img2img-existentes, img2video-ltx-2-3-i2v, img2-3d-hunyuan-backlog, runpod-sin-activar

**Entidades:** MVP_04-comfyui-arquitectura, n_07-img2video, WFltx_i2v/Open Higgsfield, fal.ai, DeepInfra, Replicate, Cloudflare Workers AI, AI Horde, Comfy Cloud, RunPod, LTX-2.3 gemma, architutors (única ficha ✅ del piloto), za_Lab, Urban Decoders, Paul Hansen

**Hechos:**
- Orden de construcción aprobado por Sol: 1 txt2img → 2 img2img → 3 img2video-nube → 4 img2 3D; pasos 1-2 pueden generar exactamente con el mismo seed y lo nuevo de hoy es el 3.
- Validación del JSON de n_07 contra `/object_info` queda como R4-pendiente; probable redirect de nodo `LTXVImgToVideo` en builds LTX-2.3.
- Piloto YT: 1/71 fichado (architutors); los 12 grupos se armaron desde títulos, requieren visual de cada uno para confirmar el groupo exacto de nodos.
- Análisis comparativo subido con precios flagged (cambian mensual); ADR del stack pendiente de derivar del informe.

## Bloque 2 — descarga de modelos SDXL (2026-11-01, tarde)

- **RealVisXL V5.0 Lightning fp16 BakedVAE** (6.46 GiB): Civitai v798204/fileId 711904 → `P:\00-repos\ComfyUI\models\checkpoints\` — **SHA256 coincide**, servidor lo lista sin reinicio.
- **RealVisXL V5.0 fp16 BakedVAE** (6.46 GiB): Civitai v789646/fileId 703211 → misma carpeta — **SHA256 coincide**.
- **RealArchvis XL v5.0: BLOQUEADO.** Civitai 401 en todas sus versiones (creador deshabilitó descargas anónimas, una responde `Unauthorized`). Sin `CIVITAI_API_TOKEN` en el entorno. Pivot: estándar RealVisXL como 2.º modelo (variante Q de la misma familia); RealArchvis queda en sugeridos con el desbloqueo documentado.
- Hallazgo infra: el servidor vivo (PID 5176) corre con CWD `P:\00-repos\ComfyUI` (relativo `main.py` solo existe ahí) — `C:\Users\Solch16\ComfyUI` es NIEBLA (0-byte Juggernaut suelto). Flags de arranque: `--directml 0 --force-fp16 --disable-cuda-malloc --lowvram --cpu-vae --disable-dynamic-vram`.
- `modelos-recomendados.md` v1.2.0: filas 2b/2c, instalados, config RealVisXL (doc oficial del creador), nota BakedVAE (vae/ vacío), estado RealArchvis/RealArchMix.

**Topics +:** descarga-modelos-sdxl, realvisxl-v5-lightning, realvisxl-v5-standard, sha256-verificado, civitai-401-realarchvis, bakedvae, servidor-cwd-P, modelos-recomendados-v1.2

## Bloque 3 — investigación de mercado de proveedores (2026-11-01, tarde)

- **HF**: límites gratis verificados (API 1k/5min, descargas 5k/5min, Inference $0,10/mes); `FLUX.1-dev` → `"gated":"auto"` (el equivalente HF al login).
- **Civitai**: Buzz diario gratis + Bronze $10/Silver $25/Gold $50; escaneos pickle+virus por archivo; RealArchvis v5.0 = **Generation-Only (no descargable por diseño)**.
- **Alternativas**: CivArchive (espejos + SHA256 + torrents — vigilar RealArchvis), TensorArt/SeaArt, ModelScope, Mage.space.
- **Licencias confirmadas**: RealVisXL = Open RAIL++-M (realvisxl.com); realarchmix v3.5 HF = creativeml-openrail-m.
- **Candidatos nuevos**: Natty Realistic SDXL v2.0, Juggernaut XL v13 Ragnarok.
- Wiki: **nuevo** `wiki/glosario/software/proveedores-modelos-ia.md` (+ fila en 00-index software); `modelos-recomendados.md` v1.3.0.

**Topics +:** proveedores-modelos-ia, huggingface-limits, civitai-buzz, generation-only, civarchive, gated-models, natty-sdxl, juggernaut-ragnarok, open-rail-licenses

## Bloque 4 — baseline R-01 en curso (2026-11-01, noche)

- Wiki: sección GPU gratis en `proveedores-modelos-ia.md` + tabla tiers en `modelos-recomendados.md` v1.4.0 (índice software ya apunta).
- R-01/T2-01: workflow vivienda SDXL validado R4 (0 errores) → batch ×3 seed 42 en `paralelo-R01-baseline` (jobs abafea6c…/cee1d6b7…/f9e66751…, 1 running + 2 pending a las 23:16 UTC). Estimado ~33 min. Log en `02-WF-log-paralelo.md`.
- Pendiente: cierre de tanda (veredicto + salidas), R-02+ y vía L4.

## Bloque 5 — WF fractal hires (2026-11-01, noche)

- Prompt: los 2 del §11 de `reinterpretacion-programa-fractal.md` (aéreo mandala + eye-level). Se usa el aéreo.
- Nuevo `A-txt2img/A-WF-fractal-hires/` (00-README, 01-index, 02-log, 03-nodos, 04-backlog + 4 JSON).
- Grafo: base 1344×768 → KSampler → LatentUpscale ×1.5 → KSampler denoise 0.35-0.4 → VAE. R4: 3/3 válidos.
- Encolado batch `batch_70b64909` (T-H1 Juggernaut 30+20 steps · T-H2 RealVisXL 30+20 · T-H3 Lightning 6+4). Nano Banana JSON listo (`GeminiImageNode`, 16:9) pero **bloqueado: requiere login Comfy org con créditos**.
- Flux: sin checkpoint local — fuera de esta tanda.

## Bloque 6 — dashboards, diagnóstico de pixelado y research de APIs (2026-11-01, cierre)

- **Corrida fractal hires cerrada**: batch `batch_70b64909` 3/3 OK. Juggernaut 1073,69 s · RealVisXL 1165,06 s · Lightning 409,36 s (todos 2016x1152). R-01 baseline 1216x832 609,26 s; las seeds 2 y 3 salieron de caché (0,02 s) → un solo render real.
- **Dashboards**: `galeria-renders.py` regenerado (100 renders, `activos/web/galeria`). Se aclaró que el tablero del usuario era **`curso.html`** (curso AI x Gaudi, 14 items SD 1.5 con `architecturerealmix_v11` — modelo retirado por licencia).
- **Nuevo**: `scripts/dashboard-concurso.py` + `_notas.md` → `activos/web/concurso/` (4 polaroids, mosaico + clic). Tiempos leídos de `/history` (`execution_start`→`execution_success`), resolución leída del IHDR del PNG (evita el bug del indexador que informa la resolución base).
- **Causa del pixelado (diagnóstico técnico)**: el `LatentUpscale` a denoise 0.35 solo interpola. Según ComfyUI #1002, latente necesita ≥0,55; tiles en píxeles funcionan a 0,20–0,30. Pipeline correcto: `txt2img → refiner 0,55 → tiles 0,25 → ESRGAN`.
- **Research @sherlock**: `raw/research/2026-11-01-modelos-imagen-n8n-telegram.md` (24 motores, 43 refs). Hallazgos: (a) Midjourney no tiene API y prohíbe automatizar; (b) DALL·E retirado de la API 2026-05-12; (c) **ningún modelo abierto conoce el lugar y no hay LoRA público de la Sagrada Família** → el conocimiento de sitio lo aporta la referencia (Gemini: 14 imágenes + image search grounding); (d) costos 2026-11-01: Recraft Flash 0,007 · Qwen 2.1 Turbo 0,014 · Nano Banana 2.1 0,0336 · Nano Banana Pro 0,134 (4K 0,24) · gpt-image-2 high 0,211; (e) n8n + Telegram viable, bloqueante = webhook público HTTPS.
- **LoRA en Comfy Cloud**: se puede importar (solo `.safetensors`, hasta 100 GB, privado) **en planes Creator/Pro/Team**; requiere subirlo antes a un repo público de Civitai o HuggingFace (la carga directa desde disco está en roadmap).

**Topics +:** dashboard-concurso, polaroid, history-timing, ihdr, latent-upscale-denoise, comfyui-1002, openrouter-imagen, nano-banana, midjourney-sin-api, comfy-cloud-byol
