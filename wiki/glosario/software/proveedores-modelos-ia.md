---
tipo: software
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [software, modelos, huggingface, civitai, civarchive, licencias, seguridad, safetensors, arquitectura]
idioma: es
---

# Proveedores de modelos abiertos (pesos SDXL y amigos)

> Dónde conseguir checkpoints/LoRA/ControlNet, con qué límites gratis, qué seguridad aplica y qué alternativas existen. Investigación de mercado 2026-11-01 (ver Metodología). Regla madre del estudio: **solo `.safetensors` + SHA256 verificado** antes de correr.

## Hugging Face — fuente primaria de pesos

- **Descargas**: URLs `resolve/main/...` directas y estables. Límites gratis (doc oficial): Hub API 1.000 req/5 min · descargas 5.000/5 min con cuenta (3.000 anónimo) · Inference Providers **$0,10/mes** · ZeroGPU Spaces 5 min GPU/día.
- **Gated** (= el "login required" de HF, verificado en `FLUX.1-dev` → `"gated":"auto"`): cuenta + aceptar licencia + token. Por repo y por licencia, predecible.
- **Licencias legibles por máquina** (`cardData.license`): `creativeml-openrail-m`, `openrail++`, `apache-2.0`. Leer igual la ficha antes de uso comercial en láminas.
- **Seguridad**: ClamAV + pickle-import scan en cada push + secrets scanning. Incidentes reales 2026 (pickle que exfiltraba keys en pipeline de eval; *ShadowPickle* evade scanners) → solo safetensors mitiga de raíz.
- Capacidades extra: repos git, formato diffusers, Spaces/Gradio como API, datasets.

## Civitai — descubrimiento + generación onsite

- **Descargas**: gratis e ilimitado **salvo decisión del creador**: anónimo ✅ (RealVisXL V5.0, verificado con SHA256) · login required ⛔ (RealArchmix XL v3.5, `requires login`) · **Generation-Only** = no descargable por diseño, solo onsite (RealArchvis XL v5.0, verificado en su ficha).
- **Generar onsite**: Buzz diario gratis + memberships Bronze $10 (10 k/mes) · Silver $25 · Gold $50 · packs pay-per-use. SDXL está en el extremo barato.
- **Seguridad**: `pickleScanResult` + `virusScanResult` por archivo (visto en cada respuesta de su API). Licencias por modelo (`allowCommercialUse`: Image/Rent/Sell).
- **Capacidades extra**: imágenes con prompt incluido (oro para estudiar prompts de arquitectura), API orchestration (AIR URN), Vault storage.
- Tokens: una sola key de cuenta cubre todo lo autenticado (sin scopes granulares; los presets Read Only/Creator/AI Services son para apps OAuth). Guardarla como contraseña, revocable.

## Otros proveedores (chequeados 2026-11-01)

| Proveedor | Qué es | Uso para el estudio |
|---|---|---|
| **CivArchive** (civarchive.com) | Archivo espejo multi-plataforma (ModelScope, Yodayo, PixAI, SeaArt) con **SHA256 por archivo**, "Add Mirror", uploader Civitai→HF y torrents | Vigilar para RealArchvis (hoy solo espeja a Civitai) |
| **TensorArt / SeaArt** | Espejos + generación onsite | Tienen Natty SDXL v2 y arch-models |
| **ModelScope** (Alibaba) | Espejo chino, SDK + git clone | Plan B si HF/Civitai caen |
| **Mage.space** | Corre modelos online; exclusivas del autor de RealVisXL | Solo online, no descarga |
| **Replicate / fal.ai** | Pay-per-run, NO entregan pesos | No sirven para local |
| **John6666 (HF)** | Mirrors diffusers de RealArchMix/RealArchvis v1-v3, licencia `creativeml-openrail-m` | Formato carpeta, no prioritario |

## Modelos de arquitectura en el mercado

- **Generalistas que rinden en arquitectura**: Juggernaut XL (**v13 Ragnarok**, feb-2026 — candidato a probar) · RealVisXL V5/V5-Lightning (en disco) · CyberRealistic XL V9 · Realities Edge XL 3.0 · **Natty Realistic SDXL v2.0** (ago-2025, 78 reviews muy positivas, fp16 + espejos).
- **Arquitectura-específicos**: RealArchvis v5.0 (solo onsite) · RealArchmix XL v3.5/v3.0-Lightning (login) · LoRAs (ArcvizXL_V01, SLskyscraperrenderingXL ya en disco) · `BMT-FloorPlan-Kontext-LoRA` en HF (¡floor plans!) · segmentadores de fachadas (segformer, para preproceso ControlNet).
- **Licencias confirmadas**: RealVisXL = Open RAIL++-M ([realvisxl.com](https://realvisxl.com/)) · realarchmix v3.5 HF = `creativeml-openrail-m` · **Juggernaut XL v9 = Open RAIL-M + cláusula extra**: prohibido APIs pagas sin licencia (`juggernaut@rundiffusion.com`; renders para clientes OK) · **ArchitectureRealMix v1.1 = ⛔ NO comercial** ([Civitai 84958](https://civitai.com/models/84958)) · lllyasviel ControlNet SD1.5 = `openrail` · runwayml inpainting = Open RAIL-M.

## Regla operativa del estudio

1. **HF = fuente primaria de pesos** (URLs estables, licencia legible, SHA256).
2. **Civitai = descubrimiento** (imágenes+prompts) + descarga si es anónima; cuenta+token para el resto; *Generation-Only* = no descargable nunca.
3. SHA256-check en cada descarga grande + solo safetensors.
4. RealArchvis: "solo onsite con Buzz" o vigilar mirror en CivArchive/torrents.

## GPU gratis para correr ComfyUI (sin RunPod ni cloud pago)

> Verificado 2026-11-01. Las cuotas cambian seguido: re-verificar antes de planificar tandas.

| Vía | Cuota gratis | Hardware | Sirve para |
|---|---|---|---|
| **Kaggle** ⭐ | ~30 h GPU/semana, sesiones 12 h, disco 20 GB. Requiere teléfono verificado + Internet ON | T4x2 (P100 retirada sep-2026) | **Un ComfyUI entero** vía notebook (guía Comflowy). Tandas pesadas 1-2 tardes/semana. Apagar al terminar (consume cuota en idle). Congestión en horas pico |
| **Google Colab free** | T4 variable, ~12 h/sesión, límites no publicados | T4 | ⚠️ **Riesgo de ToS**: uso intensivo de SD puede banear la cuenta Google. No plan A |
| **HF ZeroGPU** | 5 min GPU/día con cuenta (2 min anónimo), RTX Pro 6000 | Compartida | Solo Spaces Gradio — **probar un modelo antes de descargarlo** (51 Spaces con RealVisXL V5.0, 100 con Lightning). No corre tus WF JSON |
| **Lightning AI** | 15 créditos/mes (~22 h T4), un Studio | T4 | Desarrollo, no corridas largas |
| **Comfy Cloud free** | 400 créditos de prueba | Cloud | 1-2 corridas de referencia |
| Modal $30 starter / GCP $300 trial | Temporales o avanzados | Varios | Plan C |

**Estrategia $0 del estudio**: día a día → RX 570 local (Lightning 4-6 steps) · probar modelo → ZeroGPU Space · tanda pesada semanal → Kaggle T4x2 de noche.

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[wiki/glosario/software/lora-locales-comfyui|LoRAs locales en ComfyUI]]
- [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod]]
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|Modelos recomendados MVP_04]]

## Referencias

- https://huggingface.co/docs/hub/rate-limits (límites gratis, 5-min windows)
- https://huggingface.co/docs/inference-providers/en/rate-limits ($0,10/mes free)
- https://huggingface.co/docs/hub/security-pickle (pickle + ClamAV scans)
- https://developer.civitai.com/site/guide/getting-started (token: una key cubre todo)
- https://developer.civitai.com/site/oauth/scopes (presets: Read Only/Creator/AI Services)
- https://developer.civitai.com/orchestration/reference (RateLimit-Policy, free tier best-effort)
- https://education.civitai.com/civitais-guide-to-membership-tiers (Bronze/Silver/Gold + Buzz)
- https://realvisxl.com/ (licencia Open RAIL++-M, params oficiales)
- https://civarchive.com/models/533040 (RealArchvis: Generation-Only, SHA256 espejo)
- https://civitai.com/models/139562 (RealVisXL V5.0, ficha + descargas)
