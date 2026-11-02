---
tipo: analisis
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [analisis, ia, comfyui, a1111, fooocus, controlnet, lora, inpainting, upscaling, higgsfield, open-higgsfield, runpod, ai-horde, render, generacion-imagenes, generacion-video]
estado: borrador
---

# Análisis: IA generativa — ComfyUI y alternativas (local, cloud, por-uso)

*2026-11-01 · Fuentes: ~30 verificadas (ver [[#Referencias]]) · Confianza: alta en capacidades, media en precios (flagged)*

## Resumen

Comparativa de las interfaces de generación con IA (ComfyUI, A1111, Forge, Fooocus, InvokeAI), las rutas de cómputo (GPU local RX 570, GPU RunPod, PC del estudio) y las plataformas de generación por-uso (Open Higgsfield, fal.ai, Replicate, AI Horde, Cloudflare Workers AI). Contexto: skill `comfy-prompting` operativa, `MVP_04-comfyui-arquitectura` en curso, GPU AMD RX 570 (DirectML, sin CUDA).

**Conclusión anticipada**: quedarse en ComfyUI como hub (supera a A1111/Fooocus en las 4 capacidades nucleares y es el único vivo para modelos nuevos); generación barata bajo demanda vía APIs pay-per-uso (FLUX schnell ~$0,003/imagen); AI Horde como respaldo gratuito FLOSS.

---

## 1. Interfaces locales: ComfyUI vs A1111 vs Fooocus (y derivados)

### 1.1 Matriz por capacidades nucleares

| Capacidad | A1111 (WebUI) | ComfyUI | Fooocus |
|-----------|---------------|---------|---------|
| **ControlNet** | ✅ Extensión oficial, dropdowns simples, preprocesadores integrados. Flujo de una pestaña | ⭐ **Mejor del ecosistema**: 2.000+ nodos custom (ControlNet AUX: pose/canny/depth/normal/segment; tile; IPAdapter) y encadenamiento de múltiples ControlNets con pesos por etapa | ⚠️ Solo ImagePrompt/FaceSwap internos — ControlNet no expuesto al usuario |
| **LoRA** | ✅ Varias por prompt (`<lora:nombre:0.8>`), miniaturas, presets | ⭐ Nodo por LoRA con peso individual (UNet/CLIP separados), combinables en cadena, programables vía API/MCP | ✅ LoRA opcional, un slider de peso |
| **Inpainting** | ✅ Pestaña clásica + sketch + mask-blur + extensiones outpaint | ⭐ Inpaint modelos dedicados (Flux Fill, SDXL inpaint), nodos de máscara expandida, App Mode para exponer como formulario | ✅ Inpaint/outpaint guiado de 1 click (su nicho) |
| **Upscaling** | ✅ Tab Extras: ESRGAN incorporado, tile + fix | ⭐ ESRGAN + tile + SUPIR/FaceDetailer, encadenable en un único flujo | ✅ "+1.5× Upscale (Slow)" de 1 click |
| **Modelos 2026 (Flux, Z-Image, Qwen-Image, Wan, Seedance/LTX)** | ❌ Congelado ~2024; mejor vía fork Forge | ⭐ Soporte día-1 de casi todo modelo nuevo | ❌ Proyecto casi inactivo desde 2024 |
| **AMD (DirectML/ZLUDA)** | ⚠️ Fork `stable-diffusion-webui-amdgpu` (DirectML/ZLUDA) | ✅ DirectML nativo (setup actual del estudio); fork ComfyUI-Zluda disponible | ⚠️ Fork DirectML existe; base inactiva |
| **Estado del proyecto** | 145k★, desarrollo **detenido** (Forge es sucesor) | ~136k★, **activo**, App Mode (mar-2026) | Congelado |
| **Filosofía** | Pestañas: prompt → sliders → generate | Grafo de nodos: pipeline programable, compartible, automatizable | Interfaz mínima "Midjourney-like" |

### 1.2 Otros frontends evaluados de pasada

| Tool | Qué es | Veredicto para el estudio |
|------|--------|---------------------------|
| **Forge** (sucesor de A1111) | Form-UI moderna, mejor gestión VRAM; fork AMD con `--use-zluda` (+30-50% vs DirectML) | Única alternativa local real; experimental en Polaris (requiere `fixforrx580.bat`) |
| **InvokeAI** | Canvas tipo Photoshop (Unified Canvas), inpaint/outpaint top | ROCm Linux/WSL solamente; RX 570 (gfx803) sin soporte → descartado local |
| **SwarmUI** | Wrapper sobre backend ComfyUI | Redundante: simplifica UI pero mantiene lo que molesta |
| **Krita AI Diffusion** | Plugin de Krita que usa backend ComfyUI | Interesante como cliente de dibujo *encima* del ComfyUI existente (no reemplazo) |
| NodeTool / ComfyGrid / ComfyBox / etc. | Frontends varios sobre ComfyUI | Curiosidades; no agregan capacidades |

**Referencia de ecosistema**: [awesome-alternative-uis-for-comfyui](https://github.com/light-and-ray/awesome-alternative-uis-for-comfyui).

---

## 2. Rutas de cómputo y su economía

| Ruta | Costo | Alcance | Cuándo conviene |
|------|-------|---------|-----------------|
| **A. GPU local RX 570 (actual)** | $0 | SD 1.5 fluido, SDXL con recaudos; DirectML ~30-50% más lento que CUDA equivalente | Imágenes simples, tests, flujo diario liviano |
| **B. RunPod pod** | ~$0,89/h (RTX 4090, oct-2026); solo mientras corre | Todo el stack pesado (Flux, LTX-2.3, Seedance local, LoRA training vía AI-toolkit) | Picos de render, entrenamiento; ya integrado al MCP (pod ↔ local) |
| **C. PC del estudio prendida** | electricidad + amortización de una GPU usada (3060 12GB / 4060 Ti 16GB) | Server LAN de ComfyUI que tanto la PC de casa como el estudio consumen vía `--comfyui-url` | Uso diario sostenido; RunPod queda para picos |
| **D. Comfy Cloud (oficial)** | $20/mes fijos, ~4.200 créditos | ComfyUI en browser, GPU grande | ⚠️ **Rechaza instalar custom nodes** → inutiliza el stack actual de nodos del estudio; solo tiene sentido si se abandonan los workflows propios |

Notas de costos (fechas de lectura oct-2026, propias o de wireflow/iimagined; flag: cambian con frecuencia — re-verificar antes de comprometer):
- RunPod RTX 4090 listado a $0,89/h; ThinkDiffusion/RunComfy 24GB ~$1,75/h; H100 RunComfy ~$4,49/h.
- Comfy Cloud: $20/mo, créditos; **sin instalación de custom nodes propios** (límite estructural).
- GPU en RX 570: DirectML ok SD1.5; SDXL "tight"; Flux en teoría fuera.

---

## 3. Plataformas pay-per-use: "consola API" (una factura, pagás por generación)

### 3.1 Open Higgsfield (la consola API oficial de Higgsfield)

Cómo funciona ([docs.higgsfield.ai](https://docs.higgsfield.ai/), verificado 2026-11-01):
1. **Sign up → API key** formato `Key {id}:{secret}` en header.
2. **POST** por modelo: `https://api.higgsfield.ai/{proveedor}/{modelo}/{funcion}/v1.0` (JSON por modelo).
3. **Asincrónico**: respuesta con `request_id` + `status_url` (polling) o webhook + `cancel_url`.
4. **Outputs se retienen 7 días** — descargar a almacenamiento propio apenas termina.
5. SDK Python/TS + **MCP oficial** + CLI (agregados 2026).
6. Al 2026-10: promo "cashback 100% del gasto API" y descuentos por modelo (30-50% en varios).

Catálogo y precios vistos en la propia consola (oct-2026):
- **Imagen**: Soul 2 $0,003/img · Z-Image Turbo $0,015 · Ideogram 4.0 $0,030 · Recraft 4.1 $0,035 · Qwen Image 3 $0,040 · Grok Imagine 2.0 $0,040 · Marketing Studio (4K) $0,014.
- **Video (por segundo)**: Wan 3.0 $0,025 · Kling 3.0 $0,042 · Kling 4.0 $0,110 · Seedance 2.5 $0,144 · Cinema Studio 4.0 $0,206 (modelo exclusivo propio).

Lectura: con Soul 2 a $0,003/imagen, **un mes de Comfy Cloud ($20) compra ~6.600 imágenes ahí**. Pay-per-use gana a cualquier suscripción en volumen bajo/medio.

⚠️ Aclaración "open-source": Higgsfield **NO es open source** ni de plataforma ni de modelos ([ayuda oficial](https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms)). "Open" se refiere solo a la consola API abierta a developers. Los forks `open-higgsfield-*` en GitHub (TechBeme, wide-trace, strategist922, thehiggsfieldai) son **UIs MIT pero la generación sigue cobrándose** con keys de Freepik / Higgsfield / fal / Muapi — FLOSS de interfaz, no de cómputo.

### 3.2 Alternativas de la misma forma (consola API pay-per-use)

| Plataforma | Diferencial | Precios ref (oct-2026, flagged) |
|------------|-------------|-------------------------------|
| **fal.ai** ⭐ | Host más rápido, catálogo enorme, MCP propio, playground web | FLUX schnell $0,003/img; SDXL $0,0013 |
| **Replicate** | Catálogo community, versioned models, MCP | FLUX schnell $0,003/img |
| **DeepInfra** | El más barato en open weights | FLUX-1-schnell **$0,001/img** |
| **KIE.ai** | Barato en modelos premium | Imagen 4 $0,020/img |
| **WaveSpeed AI** | Streaming rápido | FLUX Dev $0,005/img |
| **Muapi** | Barato + presets de cámara estilo Higgsfield | FLUX schnell $0,003/img |
| **Novita AI** | GPU coverage + web chat | variable |
| **OpenRouter / Together / Cloudflare** | Agregadores / edge | Cloudflare: ~230 img FLUX/day gratis |
| **Consolas oficiales de fabricante** (BFL, Google AI Studio, Ideogram, Recraft, Freepik) | Sin margen de agregador; Freepik suma banco de recursos | variable |

### 3.3 Higgsfield (SaaS completo) — contexto

Si la necesidad fuera "presets de cámara + product video + Soul", el SaaS de Higgsfield (desde ~$19/mes hasta Ultra $129/mes) cubre más modelos por suscripción que nadie. Para un estudio de arquitectura ese eje (Ads/producto/influencer) queda fuera del core, por lo que la consola API con pago por uso es la variante que encaja.

---

## 4. Generación $0 / FLOSS para un agente (Hermes)

Objetivo: que el agente produzca **imágenes simples** sin costo fijo y con alternativas cuando la GPU local no rinde.

| Opción | Licencia | Qué da | Catch |
|--------|----------|--------|-------|
| **ComfyUI local + MCP** (ya instalado) | FLOSS, $0 | Hermes genera vía tool call hoy; SD1.5/SDXL en DirectML alcanza para "simple"; calidad de arquitectura con ControlNet ya funciona | RX 570: lenta en 768px+, Flux fuera |
| **AI Horde** ([aihorde.net](https://aihorde.net)) ⭐ | FLOSS (Haidra, nonprofit), $0 | API REST gratis con key anónima `0000000000`; registro free + kudos sube prioridad; inpaint/ControlNet/Alchemy; ~20 workers activos al 2026-11 | Cola: minutos (anónimo); menos control de modelo |
| **Cloudflare Workers AI** | free con cuenta propia, no open-source | ~230 imágenes FLUX schnell/día (10,000 neurons free/día); Apache (comercial OK) | Servicio cerrado detrás; quota diaria |
| **Pollinations** (legacy `/prompt/`) | degradado 2026 | URL sin key | Modelo anonymous limitado; tratar como best-effort |
| **fal/DeepInfra/Replicate** | pay-per-use | FLUX schnell $0,001-0,003/img | Pago por uso (mínimo implicado) |
| Script propio `diffusers` headless (SD1.5 en RX 570) | FLOSS, $0 | Camino mínimo UI-less, se integra a `scripts/` del vault (reglas HITL) | Mantenimiento propio |

---

## 5. Decisión recomendada (estado actual del estudio)

```
HUB                    → ComfyUI (mantener) — gana en ControlNet/LoRA/inpaint/upscaling y es el único vivo
IMÁGENES SIMPLES       → ComfyUI MCP con Hermes ($0) + AI Horde como respaldo FLOSS ($0)
GENERACIÓN PRO         → APIs pay-per-use: DeepInfra/fal (FLUX schnell) y Open Higgsfield (Soul/Marketing)
VIDEO                  → Kling/Wan/Seedance vía consola API (Open Higgsfield) o nodos API de ComfyUI
CÓMPUTO PESADO (pico)  → RunPod pod (ya soportado por el MCP)
CÓMPUTO PESADO (base)  → PC del estudio con GPU dedicada (evaluar al momento de compra)
COMFY CLOUD $20        → Descartada mientras el stack use custom nodes propios
A1111/Forge/Fooocus    → Sin cambio: documentados para decisiones futuras
```

Referencia cruzada: [[wiki/estudio/adr-001-comfyui-mcp|ADR-001 ComfyUI MCP]] · [[wiki/glosario/software/comfyui|ComfyUI]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod]] · [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP_04-comfyui-arquitectura]]

---

## 6. Metodología

**Queries** (websearch, 2026-11-01): alternativas locales a ComfyUI (2 series), consolas cloud ComfyUI (3 series), Higgsfield + alternativas de video (2 series), APIs de generación gratuitas (3 series),_specs de AI Horde (2 series), y lectura directa de docs.higgsfield.ai + open.higgsfield.ai (webfetch) para precios y ciclo de vida de requests.

**Fuentes con datos live al 2026-11-01**: open.higgsfield.ai (precios leídos en fetch directo), docs.higgsfield.ai, aihorde.net (stats red en vivo), inferencehub.org (ranking precios oct-2026).

## Referencias

- https://github.com/comfyanonymous/ComfyUI (hub + App Mode)
- https://github.com/light-and-ray/awesome-alternative-uis-for-comfyui (mapa de UIs alternativas)
- https://github.com/lshqqytiger/stable-diffusion-webui-amdgpu-forge (Forge-AMD, DirectML/ZLUDA)
- https://github.com/ChharithOeun/stable-diffusion-amd-windows (DX12/DirectML path, RX 570 en tabla)
- https://open.higgsfield.ai/ (consola API oficial, precios live)
- https://docs.higgsfield.ai/ (lifecycles API, keys, retention 7d)
- https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms (aclaración "open")
- https://aihorde.net/ + https://stablehorde.net/api (AI Horde, FLOSS, key anónima)
- https://toolfreebie.com/free-image-generation-api (Cloudflare Workers AI ~230 img/día)
- https://inferencehub.org/best/cheapest-image-gen-apis (ranking precios por imagen, oct-2026)
- https://visuals.fm/compare/higgsfield-vs-runway (agregación de modelos vs editor)
- https://www.runcomfy.com/ (setup cloud basada en ComfyUI)

*Precios marcados con "ref" son precios de listado leídos en una fecha específica y cambian con frecuencia.*

---

## Próximos pasos vinculados

- [ ] **ADR** derivado: "Stack de IA generativa del estudio" (mantener ComfyUI + RunPod para picos + APIs pay-per-use)
- [ ] Script `horde-test` para probar la vía AI Horde con Hermes (pendiente de `s`, reglas HITL en `scripts/`)
- [ ] Si se evalúa el PC del estudio como server: cotizar GPU dedicada (3060 12GB / 4060 Ti 16GB usadas, 12-16 GB VRAM mínimo)
- [ ] Re-verificar cifras de precios antes de cualquier compra (cambian mensual)

> ⚠️ Precios leídos en fechas específicas (oct-2026): re-verificar antes de reusar cualquier cifra.
