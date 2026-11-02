---
tipo: research
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [research, sherlock, imagen-ia, api, n8n, telegram, gemini, nano-banana, openrouter, openai, recraft, freepik, comfyui, concurso-gaudi-nexus]
idioma: es
---

# Modelos de imagen vía API + conocimiento de lugar + n8n/Telegram

*Fecha: 2026-11-01 · Fuentes: 38 (20 con fetch 200 verificado) · Confianza: alta en precios oficiales (Google, OpenAI, Recraft, Freepik, Stability, Telegram, n8n) · media en disponibilidad comercial (Adobe, Playground) · alta en los dos descartes estructurales (Midjourney sin API pública, sin LoRA público de Sagrada Família)*

**Objetivo (SOL):** elegir y cablear un generador de imagen por API para un estudio de arquitectura argentino que compite en *Gaudí Nexus* (plaza junto a la Sagrada Família). Restricciones reales: hardware local AMD RX 570 8 GB / DirectML / ComfyUI (solo SDXL), imágenes que salen blandas, SDXL no conoce el sitio, y se quiere disparar desde Telegram vía n8n con un agente LLM que redacte el prompt. Pagar API está permitido.

---

## Resumen

1. **Midjourney queda descartado por contrato, no por precio.** Su documentación oficial declara que *no provee API* y que la automatización de interacciones está estrictamente prohibida ([docs.midjourney.com, Community Guidelines](https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines), fetch 200). Todo lo que se venda como "API de Midjourney" es un wrapper de terceros.
2. **DALL·E ya no existe como opción.** `dall-e-2` y `dall-e-3` se retiraron de la API de OpenAI el **2026-05-12**; en Azure el retiro fue el **2026-03-04**. El reemplazo son los GPT Image: `gpt-image-2.5-sunburst` / `-flare` (GA), `gpt-image-2`, y `gpt-image-1.5` / `-mini` (retiran **2026-12-01**). `gpt-image-1` se apagó el **2026-10-23**.
3. **El ganador técnico para "conocer el lugar" no es un modelo más grande: es grounding + imágenes de referencia.** Gemini (Nano Banana) acepta **hasta 14 imágenes de referencia** (10 objetos + 4 personajes en NB 2.1 / 3.1 Flash; en Pro: 6 objetos + 5 personajes + 3 de estilo) y, en NB 2.1 y 3.1 Flash, **Google Search e Image Search como herramienta** para anclar la generación a datos e imágenes reales. Eso es exactamente el problema de "la plaza junto a la Sagrada Família".
4. **No existe LoRA público de la Sagrada Família** (verificado por búsqueda en Civitai y Hugging Face: solo menciones incidentales en prompts de ejemplo y LoRAs de arquitectura genéricos, uno de ellos *non-commercial*). Un LoRA propio es posible pero exige dataset propio, no lo resuelve la comunidad.
5. **La imagen blanda del pipeline local es un error de técnica, no del modelo.** El upscale en espacio latente distorsiona el ruido gaussiano y necesita denoise alto (≈0.55) para re-sintetizar; a denoise 0.35 sobre latente casi solo interpola. El upscale en espacio de píxeles (tile/Ultimate SD Upscale) trabaja bien a ≈0.25. Con el pipeline actual (latent x1.5 + denoise 0.35) el resultado esperable *es* una imagen blanda.
6. **Precio de entrada real, por imagen (2026-11-01):** Nano Banana 2.1 ≈ **USD 0.0336** (1K) · Nano Banana 2 Lite ≈ **USD 0.0336** · Qwen Image 2.1 Turbo **USD 0.0141** · Seedream 4.5 **USD 0.04** · Recraft V4.1 Flash **USD 0.007** · Freepik Imagen 4 Fast **USD 0.02** · gpt-image-2 low **USD 0.006**.
7. **Precio de la mejor calidad:** Nano Banana Pro ≈ **USD 0.134** (1K/2K) y **USD 0.24** (4K) · gpt-image-2 high 1024² **USD 0.211** (~1536×1024 USD 0.165) · gpt-image-2.5 ≈ **USD 0.006** por 196 tokens de salida en el ejemplo oficial, con tarifa USD 30/1M tokens de imagen.
8. **n8n + Telegram es viable y barato**: Telegram Trigger (con descarga de archivos) → agente LLM redacta prompt → HTTP Request a la API → nodo Convert to File (base64→binario) → Telegram sendPhoto. El único requisito duro es que el **Telegram Trigger de n8n necesita webhook público HTTPS**; sin eso (instalación local sin túnel) hay que usar el modo polling de otro nodo o un túnel.

---

## Ejes

### A. OpenRouter y el mercado de APIs de imagen (2026-11)

**A.1 El catálogo de OpenRouter es la lista más limpia de ids reales.** La consulta a `https://openrouter.ai/api/v1/images/models` (fetch 200, 2026-11-01) devuelve ids verificables, entre ellos:

- `google/gemini-3-pro-image` · `google/gemini-3.1-flash-image` · `google/gemini-3.1-flash-lite-image`
- `openai/gpt-image-2`
- `black-forest-labs/flux.2-pro` · `black-forest-labs/flux.2-klein-4b`
- `bytedance-seed/seedream-4.5`
- `qwen/qwen-image-2.1-turbo` · `qwen/qwen-image-2.1-pro` · `qwen/qwen-image-3-pro`
- `sourceful/riverflow-v2.6-pro`

Aparecen truncados y **sin verificar** en la misma respuesta: `flux-3`, `seedream-5.0`, `gpt-image-2.5-flare` / `-sunburst`, `krea/k3-edit`. No se citan como disponibles hasta confirmar su endpoint.

**A.2 Precios por endpoint (USD, consulta 2026-11-01, [ok] fuente OpenRouter):**

| Endpoint | Tarifa declarada | Lectura práctica |
|---|---|---|
| `gemini-3-pro-image` | `output_image` 0.00012/token · `input_image` 0.000002/token | USD 120 / 1M tokens de imagen → coincide con Google |
| `gemini-3.1-flash-image` | `output_image` 0.000066 (Vertex US) / 0.00006 (AI Studio) | USD 66 / 1M vs USD 60 / 1M de Google → +10 % vía Vertex |
| `gemini-3.1-flash-lite-image` | `output_image` 0.00003 | USD 30 / 1M |
| `openai/gpt-image-2` | `output_image` 0.00003 · `input_image` 0.000008 · `input_text` 0.000005 · refs 0–16 · streaming | Ej. informado: 1536×864 high ≈ USD 0.13, 94 s |
| `black-forest-labs/flux.2-pro` | USD 0.03 / MP · refs 0–8 | 1 MP ≈ 0.03 |
| `black-forest-labs/flux.2-klein-4b` | USD 0.014 / MP · refs 0–4 | el más barato de la familia FLUX.2 |
| `bytedance-seed/seedream-4.5` | USD 0.04 / imagen · `input_image` 0 · n 1–10 · refs 0–14 | refs gratis, ideal iteración |
| `qwen/qwen-image-3-pro` | USD 0.04 / imagen 1K · USD 0.075 / imagen 2K · `input_image` 0.003 · refs 0–3 | 2K casi el doble |

**A.3 La documentación de OpenRouter confirma el contrato**: `/api/v1/images/models` para descubrir, parámetros por endpoint (no hay un esquema único) y playground para probar sin código ([docs OpenRouter, image-generation](https://openrouter.ai/docs/guides/overview/multimodal/image-generation), fetch 200).

**A.4 Lectura para el estudio.** OpenRouter sirve como *agregador con una sola factura y una sola clave*, y permite cambiar de familia sin reescribir el workflow de n8n. El costo es un margen: en Gemini 3 Pro Image coincide exacto; en 3.1 Flash Image cuesta ~10 % más que ir directo a AI Studio. Para volumen bajo (concurso) la comodidad gana; para volumen alto conviene clave directa.

---

### B. Conocimiento de lugar: qué tan mal lo hacen los modelos abiertos

**B.1 La evidencia académica es explícita y usa la Sagrada Família como caso.** El paper *When Cultures Meet: Multicultural Text-to-Image Generation* (ACL 2026 Findings, [aclanthology.org/2026.findings-acl.1783.pdf](https://aclanthology.org/2026.findings-acl.1783.pdf), snippet) toma la Sagrada Família como *landmark* de España y mide una métrica de desviación semántica (ΔS) sobre SDXL, DALL·E 3 y FLUX. La conclusión del género: los modelos reproducen estereotipos de cultura, no arquitectura específica.

**B.2 El benchmark WISE lo cuantifica.** [arxiv.org/abs/2503.07265](https://arxiv.org/abs/2503.07265) (fetch 200): 1.000 prompts, 25 subdominios, métrica *WiScore*, 20 modelos (10 text-to-image + 10 multimodal unificado). Hallazgo central: **limitaciones significativas para integrar conocimiento de mundo** en la generación. Traducido al proyecto: pedirle a SDXL "plaza frente a la Sagrada Família" produce *una* basílica neogótica plausible, no *esa* basílica.

**B.3 No hay atajo comunitario.** Búsqueda dirigida en Civitai y Hugging Face: **no existe un LoRA público dedicado a la Sagrada Família**. Lo que aparece es (a) una mención incidental en el prompt de ejemplo de un modelo de cartas (`Wakkamaruh/balatro-poker-cards`), y (b) LoRAs genéricos de arquitectura (`civitai.com/models/709956/flux-arch-realism-lora`, **licencia non-commercial**; `wangkanai/sdxl-fp16-loras`, genérico). Conclusión: el conocimiento del sitio hay que **inyectarlo**, no esperarlo.

**B.4 Las tres formas reales de inyectarlo, en orden de eficacia:**

1. **Imágenes de referencia + edición** (la más fuerte). Subir 3–8 fotos reales del sitio (plaza, fachada, entorno del Eixample) y pedir una intervención. Gemini acepta hasta 14 refs; Seedream 4.5 acepta 14 con `input_image` a costo 0; gpt-image-2 acepta 16 en edición.
2. **Grounding con búsqueda de imágenes** (solo Gemini NB 2.1 y 3.1 Flash): `tools: [{type:"google_search", search_types:["web_search","image_search"]}]`. El modelo trae contexto visual real antes de generar. Aviso oficial: en modo *web* search las imágenes recuperadas **no** se pasan al generador y quedan excluidas de la respuesta; para eso está *image* search.
3. **LoRA propio** (último recurso). Requiere dataset propio etiquetado; en 8 GB con DirectML es caro y lento. Freepik/Magnific vende *entrenamiento* de LoRA de estilo a USD 1.367 (quality medium/high) y USD 2.901 (ultra), y de personaje a USD 1.367–2.901 — dato útil si se quiere un estilo de estudio, no un lugar.

**B.5 Corolario de método.** Para este concurso, el prompt de texto sirve para **intención** (material, luz, programa); la **identidad del lugar** se resuelve con fotos de referencia o grounding. Cualquier evaluación que compare modelos solo con texto está midiendo la cosa equivocada.

---

### C. Alternativas a Midjourney (con licencia comercial y acceso programático)

**C.1 Descartes estructurales primero.**

- **Midjourney — sin API.** La documentación oficial de *Community Guidelines* lo dice sin ambigüedad: *"Midjourney does not provide an API, nor provide third-party apps or scripts, and automating interactions with Midjourney service is strictly prohibited"* ([docs.midjourney.com](https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines), fetch 200). Riesgo contractual directo para un estudio que factura.
- **Playground AI — sin API pública.** El Help Center oficial: *"We only provide API access to a select number of partners... prioritizing potential partners whose users will generate more than 1M images a month"* ([help.playgroundai.com](https://help.playgroundai.com/en/articles/6861708-does-playground-ai-have-an-api-i-can-access-to-generate-images)). El plan Pro Plus (USD 36/mes anual, 45 mensual) incluye *pedir* acceso. Licencia comercial worldwide royalty-free. Fuera de alcance por volumen.
- **Bing Image Creator / DALL·E — extinguido.** Ver Resumen §2.

**C.2 Google Gemini / Nano Banana — la familia más completa.**

Fuente primaria: [aistudio.google.com/docs/pricing](https://aistudio.google.com/docs/pricing) (fetch 200, 2026-11-01) y [aistudio.google.com/docs/image-generation](https://aistudio.google.com/docs/image-generation) (fetch 200).

| Modelo | id | Tarifa oficial | Por imagen (derivado) |
|---|---|---|---|
| Nano Banana Pro | `gemini-3-pro-image` | input USD 2/1M (texto e imagen); output texto USD 12/1M; **output imagen USD 120/1M** | 1K/2K (1.120 tok) **USD 0.134** · 4K (2.000 tok) **USD 0.24** |
| Nano Banana 2.1 | `gemini-nano-banana-2.1` | output imagen USD 30/1M | 1K **USD 0.0336** · 2K (1.680) **USD 0.0504** · 4K (3.780) **USD 0.113** |
| Nano Banana 2 | `gemini-3.1-flash-image` | output imagen USD 60/1M | 512px (747) **USD 0.045** · 1K **USD 0.067** · 2K **USD 0.101** · 4K (2.520) **USD 0.151** |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | input USD 0.25/1M; output texto USD 1.50/1M; **output imagen USD 30/1M** | 1K **USD 0.0336** |
| Nano Banana (legacy) | `gemini-2.5-flash-image` | — | **USD 0.039** · retira **2027-03-15** |

Capacidades que importan acá (misma doc):

- **Resoluciones** 1K / 2K / 4K; 3.1 Flash agrega 512 px.
- **Hasta 14 referencias**: NB 2.1 y 3.1 Flash → 10 objetos de alta fidelidad + 4 personajes; Pro → 6 objetos + 5 personajes + 3 de estilo.
- **Grounding**: `google_search` (web) en todos; **image_search** solo NB 2.1 y 3.1 Flash.
- **Thinking mode**: genera "thought images" intermedias que *no se cobran*, para razonar la composición antes de la salida final.
- **Aspect ratios nuevos** en NB 2.1 y 3.1 Flash: 1:4, 4:1, 1:8, 8:1 (útil para fajas urbanas y cortes verticales de cartel).
- **SynthID**: toda imagen generada lleva marca de agua invisible. Relevante para presentaciones de concurso: es detectable, no es una firma visible.
- **Endpoint** documentado hoy: `POST https://generativelanguage.googleapis.com/v1beta/interactions` con headers `x-goog-api-key`, `Content-Type: application/json`, `Api-Revision: 2026-05-20` y body `{model, input:[{type:"text",text:"..."}], response_format:{type:"image", mime_type:"image/png", aspect_ratio:"16:9", image_size:"2K"}}`. Las imágenes vuelven en base64 dentro de `interaction.output_image.data`.
  - **Nota de implementación:** la mayoría de los tutoriales de 2024–2025 usan el surface viejo `:generateContent` con `responseModalities`. Conviene confirmar contra la cuenta real cuál surface responde antes de escribir el workflow; la doc actual de AI Studio ya muestra `interactions`.

Free tier (snippet de [aistudio.google.com/docs/rate-limits](https://aistudio.google.com/docs/rate-limits)): TPD por modelo — 3 Pro Image Preview 2.000.000; 3.1 Flash Image Preview 1.000.000; 3.1 Flash Lite Image 2.000.000; 2.5 Flash Image Preview 3.000.000. Sirve para validar el flujo sin tarjeta; **los términos del free tier para uso comercial del estudio deben confirmarse aparte** (gap declarado).

**C.3 OpenAI GPT Image — la mejor edición por instrucción.**

Fuente: [developers.openai.com, image generation](https://developers.openai.com/api/docs/guides/image-generation) y fichas de modelo (snippets oficiales, 2026-11).

- Modelos vigentes: `gpt-image-2.5-sunburst` (edición precisa), `gpt-image-2.5-flare` (rápido), `gpt-image-2`, y `gpt-image-1.5` / `-mini` (retiran **2026-12-01**).
- **2.5 (token-based)**: USD 8/1M imagen entrada · 2/1M caché · **30/1M imagen salida** · 5/1M texto entrada · 1.25/1M caché. Ejemplo oficial: 196 tokens de salida → **USD 0.00588**.
- **gpt-image-2 (por imagen)**: 1024² low **0.006** / medium **0.053** / high **0.211**; 1536×1024: 0.005 / 0.041 / 0.165. Tamaños arbitrarios `WIDTHxHEIGHT` múltiplos de 16, aspecto entre 1:3 y 3:1, `n` 1–10.
- **Edición**: hasta **16 imágenes** de referencia por request, PNG/WebP/JPG < 50 MB cada una; `input_fidelity` high/low. Es el argumento más fuerte para "respetá esta fachada y cambiá la plaza".
- Liquidez del catálogo: el retiro escalonado (oct-2026, dic-2026) obliga a fijar versión explícita en el workflow.

**C.4 Recraft — la única con vectores nativos y la trampa de licencia del plan free.**

Fuente: [recraft.ai/docs/api-reference/pricing](https://www.recraft.ai/docs/api-reference/pricing) (fetch 200).

- Unidad: **USD 1 = 1.000 units**; paquetes prepagos, sin vencimiento.
- Raster: V4.1 Flash **USD 0.007**; V4.1 / V4.1 Utility **0.035**; V4 Styles **0.035**; V4 / V3 **0.04**; V2 **0.022**.
- **Vector**: V4.1 **USD 0.08**; V4 / V3 / V4.1 **0.08**; V4 Styles **0.05**; V2 **0.044**.
- Pro raster 2K: V4.1 **0.21**; V4 **0.25**; V4 Styles **0.10**. Pro vector: **0.30** / **0.12**.
- Herramientas: image-to-image, inpaint, outpaint, replace/generate background **0.04**; creative upscale **0.25**; enhance details (V4.1 Pro) **0.21**; crisp upscale **0.004**; remove background **0.01**; vectorize **0.01**.
- **Alerta de licencia** ([recraft.ai/pricing](https://www.recraft.ai/pricing), fetch 200): *"Images generated on the Free plan are owned by Recraft. They are publicly visible in the community gallery and are not licensed for commercial use."* Los planes pagos sí dan propiedad y derechos comerciales. **Para un concurso, nunca usar el plan free de Recraft.**
- El vector es diferencial para el estudio: lockups de cartelería, diagramas y piezas de presentación sin pasar por Illustrator.

**C.5 Freepik (ahora Magnific) — el catálogo más ancho bajo una API.**

- Rebranding: desde **2026-04-28** toda la plataforma se vende como **Magnific**; `api.freepik.com` y `api.magnific.com` conviven durante la migración (snippet, blog de terceros — *no confirmado en fuente oficial*).
- Precio por operación ([tr.freepik.com/api/pricing](https://tr.freepik.com/api/pricing), snippet): **Mystic** 1K **USD 0.069**, 2K **0.119**, 4K **0.38**; **Nano Banana Pro** 1K **0.10**, 2K **0.15**, 4K **0.30**; **Nano Banana Pro Flash** 1K **0.095**, 2K **0.143**, 4K **0.19**, con Google Search +0.018; **Seedream v4.5** **0.04**; **Seedream v3/v4** 0.032; **Flux 2 Pro 1K** **0.04**; **Flux Pro 1.1** 0.043; **Flux Dev** 0.012; **HyperFlux** 0.161; **Imagen 4 Fast** **0.02**; **Imagen 4 Ultra** 0.06; **Z-Image** **0.02**; **Classic Fast** **0.005**; **Runway t2i** 0.10.
- Entrenamiento de LoRA: estilo quality medium **USD 1.367**, high/ultra **2.901**; personaje high **1.367**, ultra **2.901**.
- Planes UI ([freepik.com/pricing](https://www.freepik.com/pricing), snippet): Free USD 0; Premium USD 20/mes (~240.000 créditos/año); Premium+ USD 45/mes (~600.000 + ~10 modelos de imagen "ilimitados"); Pro USD 280/mes (~4 M). "Ilimitado" aplica a ~10 modelos y excluye 4K de Nano Banana y el entrenamiento de LoRA. Licencia comercial de IA incluida.
- Lectura: **Red Flag de consistencia** — el precio de Mystic aparece a USD 0.069/imagen en la página de precios de API y a ~USD 0.004/imagen en un texto de terceros de septiembre 2026. Se toma el valor de la página oficial y se marca el otro como no confirmado. Presupuestar con el número caro.

**C.6 Stability AI — el piso de precio verificable.**

Fuente: [docs.stability.ai/pricing](https://docs.stability.ai/pricing) (fetch 200). 1 crédito = **USD 0.01**; 25 créditos gratis al registrarse. Stable Image Ultra **8 créditos = USD 0.08**; SD 3.5 Large **6.5 = 0.065**; Stable Image Core **3 = 0.03**; SDXL 1.0 desde **0.9 = 0.009**. Útil como "tercero barato" y para ControlNet clásico, pero sin conocimiento de lugar ni grounding.

**C.7 Ideogram — tipografía, no lugar.**

Free tier; Plus **USD 20/mes** (2.400 créditos); Pro **USD 60/mes** (7.500); Team **USD 30/usuario/mes** (3.600/usuario); **30 créditos gratis por semana** con login Google/Apple/Microsoft; API con API keys; uso comercial sujeto a ToS ([docs.ideogram.ai FAQ](https://docs.ideogram.ai/frequently-asked-questions), fetch 200). Fuerte en texto dentro de imagen (carteles del concurso), débil como generador de sitio.

**C.8 Leonardo — pago por uso, sin fee.**

[Pricing & plans FAQ](https://docs.leonardo.ai/docs/pricing-and-plans-faq) (fetch 200, actualizado 2026-09-01): la API es **pay-as-you-go, sin cargo mensual**; calculadora de precios; créditos descontados en tiempo real; el plan web Essential es USD 10/mes anual (8.500 fast tokens) — dato de tercero, no de la doc de API.

**C.9 Krea — API pública con MCP.**

[krea.ai/pricing](https://www.krea.ai/pricing) (fetch 200): Free **100 units/día**; imágenes por plan según modelo (Nano Banana 2 Lite 198/794/1.588; Qwen Image ~562/2.250/4.500; Qwen Image 2.1 y 3 (1K) 168/675/1.350; Recraft V4 ~168/675/1.350; Recraft V4.1 Flash 964/3.857/7.714; Seedream 4 225/900/1.800; Seedream 4.5 168/675/1.350; Runway Gen-4 Image ~112/450/900); entrenamiento de LoRA hasta 50 imágenes. API en [api.krea.ai](https://api.krea.ai/) (fetch 200) con playground, `docs.krea.ai`, tokens por workspace y **MCP** (`https://api.krea.ai/mcp`). Precio por endpoint en [krea.ai/app/api/pricing](https://www.krea.ai/app/api/pricing) (no fetch: gap).

**C.10 Pollinations — el "gratis sin registro" real, con asteriscos.**

[text.pollinations.ai/APIDOCS.md](https://text.pollinations.ai/APIDOCS.md) (fetch 200): `https://image.pollinations.ai/prompt/{prompt}` sin clave, rate-limited por IP; key en `enter.pollinations.ai`; **USD 0.01 por request** vía x402 (USDC en Base); **sin garantía de uptime**. Sirve para prototipar el workflow de n8n hoy, no para entregar.

**C.11 Qwen / Alibaba — el mejor precio por imagen con calidad alta.**

- `qwen-image-2.1-turbo`: **USD 0.014133/imagen** (Beijing, Virginia, Frankfurt, Tokyo, Hong Kong) y **0.016** (Singapur); **RPM 120** ([alibabacloud.com, ficha del modelo](https://www.alibabacloud.com/help/es/model-studio/qwen-image-2-1-turbo), snippet).
- `qwen-image-2.0-pro`: **¥0.5/imagen** en Beijing y ¥0.550443 en Singapur, pero **RPM 2** — inutilizable para un bot interactivo.
- `qwen-image-3.0-pro`: hasta **2048×2048**, **6 salidas** por llamada, prompt negativo, 1–3 referencias, mismo id para generar y editar; `wan2.7-image-pro` llega a **4096×4096** ([docs.qwencloud.com](https://docs.qwencloud.com/developer-guides/getting-started/image-models), snippet).
- Free: **ModelScope** da API gratis de Qwen-Image-2.1 a 1 crédito/llamada con techo de ~250/día, con cuenta de Alibaba Cloud verificada — dato de **blog de tercero**, no confirmado en fuente oficial. **Qwen Chat no es una API** (el repo oficial no lo menciona; un chat no se scriptea).

**C.12 Hugging Face Spaces — gratis con techo, y para el estudio es un "no" operativo.**

[Spaces overview](https://huggingface.co/docs/hub/spaces-overview) (fetch 200): crear un Space Gradio o Docker **requiere plan pago** (PRO personal o Team/Enterprise); las cuentas free pueden hostear **hasta 2 Spaces Gradio en ZeroGPU**. CPU Basic gratis (2 vCPU / 16 GB / 50 GB no persistente); GPU: T4 small **USD 0.40/h**, L4 **0.80/h**, A10G **1.00/h**, L40S **1.80/h**, A100 80 GB **2.50/h**, RTX PRO 6000 **2.75/h**. Los Spaces gratuitos **duermen** por inactividad. Sirve para correr un modelo pesado puntual, no para un bot 24/7.

**C.13 Adobe Firefly API — existe, precio sin confirmar.**

[developer.adobe.com/firefly-services/docs/firefly-api](https://developer.adobe.com/firefly-services/docs/firefly-api/) (fetch 200): API oficial con **Image5** (4 MP nativos, *Instruct Edit* en lenguaje natural), **Custom Models** (entrenar sujeto/estilo, referenciar por asset id), **Composite Operations** (Object/Adaptive/Precise Composite con harmonización 0–100 %) y **Upscale** 2×/4×/6× con dos modos (User Assets vs Generated Image, este último para no alucinar detalle al ampliar). El precio **no está en la ruta pública** (`/guides/pricing/` devuelve **404**); un comparador de terceros lista Firefly Standard USD 9.99/mes con 2.000 créditos generativos — **no confirmado**. El *Upscale API* es lo más interesante para el problema de nitidez.

---

### D. n8n + Telegram: el cableado y sus límites duros

**D.1 Límites de Telegram (fuente oficial).**

[core.telegram.org/bots/api#sending-files](https://core.telegram.org/bots/api#sending-files) (fetch 200):

| Vía | Foto | Otros archivos |
|---|---|---|
| Envío por **URL** | **5 MB** | **20 MB** |
| **Multipart** (upload) | **10 MB** | **50 MB** |
| **Bot API server local** | — | descarga ilimitada / subida **2.000 MB** |

[core.telegram.org/bots/faq](https://core.telegram.org/bots/faq) (fetch 200): **1 mensaje/segundo por chat** (se toleran ráfagas cortas), **20 mensajes/minuto por grupo**, **~30 mensajes/segundo** en difusión masiva; al exceder devuelve **429 con `retry_after`**. Paid Broadcasts sube el techo a 1.000/s (0.1 Stars por mensaje sobre los 30 gratis), requiere 100.000 Stars y 100.000 MAU. Texto: **4.096 caracteres** por mensaje, **1.024** de caption.

Para el caso: un render 2K en PNG pesa 3–8 MB → **entra por multipart sin problema**; uno 4K puede rozar el límite y conviene mandar JPEG calidad 90 o redimensionar.

**D.2 Nodo Telegram Trigger de n8n.**

[docs.n8n.io, Telegram Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/) (fetch 200): eventos `Message`, `Callback Query`, `Edited Message`, etc.; opciones clave **Download Images/Files** (con **Image Size**) y **Restrict to Chat IDs / User IDs**. Es lo que permite recibir la foto de referencia del arquitecto y pasarla como input al modelo.

**D.3 Nodo HTTP Request — lo que hace falta para bases64 y binarios.**

[docs.n8n.io, HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) (fetch 200):

- **Send Body → Form-Data** permite un parámetro de tipo **n8n Binary File** (nombre de campo + campo binario de entrada) → multipart real.
- **Send Body → n8n Binary File** manda el contenido de un archivo como cuerpo entero.
- **Response → Response Format: File** guarda la respuesta en un campo binario (con **Put Output in Field**). Es la vía limpia cuando la API devuelve la imagen cruda.
- **Response → Never Error** y **Include Response Headers and Status** para manejar 429/500 sin romper el flujo.
- **Timeout** en milisegundos — **ponerlo explícito**: el valor por defecto de n8n puede cortar una generación de 4K que tarda 60–120 s.
- **Batching** (items/batch + intervalo) para respetar el rate limit de Telegram.
- **Import cURL**: pegar el `curl` de la doc del proveedor y queda configurado (los valores entran como string — para números/booleanos usar *Using JSON*).

**D.4 El problema de base64 y la solución canónica.**

Gemini (y gpt-image-2) devuelven la imagen **en base64 dentro del JSON**, no como binario. Encadenar:

1. HTTP Request → respuesta JSON con `output_image.data` (string base64).
2. Nodo **Convert to File** → operación *Convert Base64 to Binary* (o un Code node con `Buffer.from(data,'base64')`).
3. Nodo **Telegram → Send Photo** con *Binary File* apuntando al campo generado.

Si en cambio la API devuelve un **URL** (Qwen/DashScope guarda en OSS y devuelve URL temporal de 24 h; Seedream igual), el paso 1 es HTTP Request con *Response Format: File* sobre esa URL, y el resto igual. Ojo: **Qwen purga la tarea y las URLs a las 24 h** — hay que bajar la imagen en el mismo flujo.

**D.5 Blueprint del workflow (5 nodos + 1 agente).**

```
[Telegram Trigger: Message, Download Images/Files = ON, Image Size = large]
        │
        ▼
[AI Agent / LLM: redacta prompt técnico]
   · system prompt = brief del estudio (materiales, luz, encuadre, "no inventar la basílica:
     describe la intervención", idioma del prompt en EN)
   · tools: ninguno o un vector store con el brief del concurso
   · output: JSON {prompt, aspect_ratio, image_size, refs[]}
        │
        ▼
[Code: arma body  {model, input:[{type:"text",text}, {type:"image",data:base64,...}], response_format}]
        │
        ▼
[HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/interactions
   headers: x-goog-api-key, Api-Revision: 2026-05-20
   Timeout: 180000 · Never Error: ON · Response: JSON]
        │
        ├─► [IF status 200]
        │        ▼
        │   [Convert to File: base64 → binary (campo "data")]
        │        ▼
        │   [Telegram: Send Photo · Binary File · caption con el prompt usado]
        │
        └─► [IF 429/5xx] → [Wait retry_after] → reintento (máx 2)
```

Variantes que conviene parametrizar desde el mensaje de Telegram: `/nb21` (Nano Banana 2.1, barato) vs `/nbpro` (Nano Banana Pro, con thinking y 14 refs) vs `/local` (cae a ComfyUI en la LAN vía HTTP, sin costo).

**D.6 Los tres gotchas reales del montaje.**

1. **Telegram Trigger necesita webhook público HTTPS.** n8n registra el webhook contra la API de Telegram; si n8n vive en una PC de estudio sin IP pública ni túnel (Cloudflare Tunnel / ngrok / Tailscale Funnel), el trigger **no recibe nada**. Alternativas: túnel, o un bot propio en Python con long-polling (`getUpdates`) que empuje a n8n por webhook interno.
2. **Timeout del HTTP Request.** Una generación 2K/4K tarda 15–120 s. Sin `Timeout` explícito el nodo corta y se pierde el trabajo ya cobrado.
3. **Rate limit.** Un grupo de Telegram con 4 personas pidiendo renders en ráfaga choca con los 20 msg/min del grupo. El nodo *Batching* + `Wait` con `retry_after` lo resuelve; sin eso, 429 en cascada.

**D.7 Precedente publicado.** La plantilla [n8n #10466, "AI Image Generation and Editing with Google Gemini and Telegram Bot"](https://www-staging.n8n.io/workflows/10466-ai-image-generation-and-editing-with-google-gemini-and-telegram-bot) (snippet) hace exactamente este patrón: Telegram Trigger + HTTP Request a Nano Banana + devolución de imagen. Sirve como esqueleto importable, con la salvedad de que puede estar escrita contra el surface viejo de la API.

---

### E. Tabla comparativa final

Precio = por imagen, USD, 2026-11-01. "Conocimiento de lugar" evalúa si el modelo sabe qué es la Sagrada Família **sin** referencias.

| Modelo | Proveedor | Acceso API | Precio/imagen | Conocimiento de lugar | Edición con referencia | Licencia comercial | ¿n8n? |
|---|---|---|---|---|---|---|---|
| **Nano Banana Pro** (`gemini-3-pro-image`) | Google | Directa + OpenRouter | **0.134** (1K/2K) · **0.24** (4K) | **Alto** + grounding web | **Hasta 14 refs** (6 obj + 5 pers + 3 estilo) | Sí (pago); free tier a confirmar | Sí |
| **Nano Banana 2.1** (`gemini-nano-banana-2.1`) | Google | Directa + OpenRouter | **0.0336** (1K) · 0.0504 (2K) · 0.113 (4K) | **Alto** + web **e image** search | 14 refs (10 obj + 4 pers) | Sí (pago) | Sí |
| **Nano Banana 2** (`gemini-3.1-flash-image`) | Google | Directa + OpenRouter | 0.045 (512) · 0.067 (1K) · 0.101 (2K) · 0.151 (4K) | Alto + image search | 14 refs | Sí | Sí |
| **Nano Banana 2 Lite** | Google | Directa | **0.0336** | Medio (sin multi-ref) | Limitada (no multi-turn) | Sí | Sí |
| **Nano Banana legacy** (`gemini-2.5-flash-image`) | Google | Directa | 0.039 (retira 2027-03-15) | Medio | Sí | Sí | Sí |
| **GPT Image 2.5** (sunburst/flare) | OpenAI | Directa + OpenRouter* | ~**0.0059** / 196 tok salida (30/1M) | Medio-alto | **16 refs**, `input_fidelity` | Sí | Sí |
| **GPT Image 2** | OpenAI | Directa | 0.006 low · 0.053 med · **0.211 high** (1024²) | Medio-alto | 16 refs | Sí | Sí |
| **Seedream 4.5** | ByteDance | OpenRouter · Freepik | **0.04** (refs gratis) | Medio | 14 refs | Sí (vía proveedor) | Sí |
| **Qwen Image 3.0 Pro** | Alibaba | QwenCloud | 0.04 (1K) · 0.075 (2K) | Medio (texto/layout fuerte) | 1–3 refs | Sí | Sí |
| **Qwen Image 2.1 Turbo** | Alibaba | QwenCloud | **0.0141** | Medio | 10 refs (serie 2.1) | Sí | Sí (RPM 120) |
| **FLUX.2 Pro** | BFL | OpenRouter · Freepik | 0.03/MP | Bajo-medio | 8 refs | Sí (API comercial) | Sí |
| **FLUX.2 klein 4B** | BFL | OpenRouter | **0.014/MP** | Bajo | 4 refs | Apache 2.0 (pesos) | Sí |
| **Recraft V4.1 Flash** | Recraft | Directa | **0.007** | Bajo | No edita (modelo de gen) | **Free plan: NO comercial** | Sí |
| **Recraft V4.1 / +vector** | Recraft | Directa | 0.035 raster · **0.08 vector** · 0.21 pro 2K | Bajo | image-to-image 0.04 | Pago: sí | Sí |
| **Mystic** | Freepik/Magnific | Directa | 0.069 (1K) · **0.119 (2K)** · 0.38 (4K) | Medio (estilo propio) | refs de estilo y estructura | Sí (licencia IA comercial) | Sí |
| **Stable Image Ultra** | Stability | Directa | **0.08** | Bajo | ControlNet clásico | Sí | Sí |
| **SDXL 1.0 / SD3.5 Large** | Stability | Directa | 0.009 / 0.065 | Bajo | ControlNet/IP-Adapter | Sí | Sí |
| **Ideogram** | Ideogram | Directa | plan 20–60 USD/mes | Bajo | edición | Sujeto a ToS | Sí |
| **Leonardo** | Leonardo | Directa | pay-as-you-go (calc.) | Medio | sí | Sí | Sí |
| **Krea** | Krea | Directa + **MCP** | por unidad; free 100/día | Depende del modelo elegido | sí | Sí | Sí (MCP) |
| **Pollinations** | Pollinations | URL GET | **0.01/request** (o free rate-limited) | Bajo | limitada | Revisar ToS | Sí (GET simple) |
| **SDXL local (Juggernaut/RealVis)** | ComfyUI propio | HTTP local | **0.00** (electricidad) | **Nulo** (necesita refs/LoRA) | img2img + ControlNet | Sí (pesos abiertos) | Sí (LAN) |
| **Midjourney** | Midjourney | **— sin API —** | n/a | Alto (estético) | — | — | **No** |
| **Playground AI** | Playground | **solo partners >1M img/mes** | plan 36 USD/mes | Medio | sí | Sí | **No operativo** |
| **Adobe Firefly (Image5)** | Adobe | API oficial | **no publicado** (404 pricing) | Medio | Instruct Edit + Custom Models + Upscale 6× | Sí | Sí |

\* `gpt-image-2` sí está en OpenRouter; `gpt-image-2.5` no aparece confirmado en el catálogo de imágenes.

---

### F. Recomendación en tres escenarios

**F.1 Escenario "gratis / validar el flujo" (costo 0)**

- **Motor:** Gemini free tier con clave de AI Studio, `gemini-nano-banana-2.1` (el modelo recomendado por Google para nuevos proyectos) o `gemini-3.1-flash-lite-image` cuando el volumen apriete.
- **Fallback:** Pollinations por GET para probar el workflow sin clave; HF Space ZeroGPU si hace falta un modelo que no está en Gemini.
- **Local:** ComfyUI SDXL **solo** para lo que no requiere identidad de lugar (moodboards, texturas, variantes de material) — y **arreglando el upscale** (ver F.4).
- **Para qué sirve:** dejar el bot de Telegram funcionando de punta a punta en una tarde y medir latencia real.
- **Riesgo:** los términos del free tier de Google para uso comercial del estudio **no están confirmados** en esta búsqueda. No entregar piezas de concurso generadas en free tier hasta leerlos.

**F.2 Escenario "barato de producción" (≈ USD 0.03 por imagen, ~USD 7 por 200 imágenes)**

- **Motor principal:** `gemini-nano-banana-2.1` a **USD 0.0336** (1K) o **0.0504** (2K). Es el mejor equilibrio precio/capacidad: image search grounding, 14 refs, 4K opcional a 0.113.
- **Alternativa de costo:** `qwen-image-2.1-turbo` **USD 0.0141** con RPM 120 (aguanta un bot), o Recraft V4.1 Flash **USD 0.007** si el pedido es vectorial/gráfico (no arquitectónico).
- **Variedad de estilo:** Seedream 4.5 **0.04** con 14 refs a costo 0 → iterar la misma foto de base en cinco estéticas distintas cuesta 0.20.
- **Ahorro estructural:** pasar de 1K a 2K solo en la imagen elegida. 1K para explorar, 2K/4K para la lámina final.
- **n8n:** self-hosted (gratis) + Telegram, con `/nb21` por defecto.

**F.3 Escenario "mejor calidad" (≈ USD 0.13–0.24 por imagen, ~USD 13–24 por 100)**

- **Motor:** `gemini-3-pro-image` (**Nano Banana Pro**) con *thinking mode*, 14 refs y **image search grounding**, a 2K normalmente (0.134) y 4K solo para la entrega (0.24). Es el único que combina razonamiento de composición, fidelidad de texto y anclaje a imágenes reales del sitio.
- **Segundo motor para edición quirúrgica:** `gpt-image-2.5-sunburst` con `input_fidelity: high` y 16 refs. Cuando el pedido es "respetá esta fachada exactamente y cambiá solo la plaza", el control por instrucción de OpenAI suele ganar.
- **Nitidez final:** Adobe **Upscale API** (modo *Generated Image Upsampler*, 2×/4×/6×) está diseñado específicamente para no inventar detalle al ampliar generaciones — resuelve el "look blando" sin volver a samplear.
- **Presentación:** Recraft **vector** (0.08) para la cartelería y los diagramas del tablero; así el raster generado nunca se estira en la lámina.

**F.4 El arreglo del pipeline local (independiente del escenario)**

El síntoma "imagen blanda" con `1344×768 → latent ×1.5 → 2016×1152 @ denoise 0.35` tiene causa documentada ([ComfyUI discussion #1002](https://github.com/Comfy-Org/ComfyUI/discussions/1002), fetch 200): el upscale latente amplía un tensor de ruido gaussiano, y eso **no es** un upscale de imagen. Consecuencias prácticas del hilo y del glosario ([aiofm.info, hi-res-fix](https://aiofm.info/en/glossary/hi-res-fix)):

- Latent upscale **después del refiner**, nunca antes; y con denoise **≥ ~0.55** para que el sampler re-sintetice estructura. A 0.35 el modelo apenas corrige: de ahí la sensación de "borroso".
- **Alternativa superior:** upscale en espacio de píxeles (tile/Ultimate SD Upscale, ESRGAN + pasada de denoise **0.20–0.30**). Es el rango donde agrega microdetalle sin cambiar la composición.
- En 8 GB con DirectML: tiles de 512–768 px, 20–28 pasos, y **no** intentar 2K de una pasada.

Orden recomendado para el nuevo pipeline local: `txt2img 1024×1024 (o 1216×832) → refiner/hires-fix a denoise 0.55 → upscale por tiles a denoise 0.25 → (opcional) ESRGAN 4× → downscale a la resolución objetivo`. Cuesta más segundos, pero es el único camino que produce microdetalle en una RX 570.

---

### G. Referencias

**Google / Gemini** [en]
1. Google AI Studio — *Pricing*. https://aistudio.google.com/docs/pricing — fetch 200 (2026-11-01). Tarifas, tokens por resolución, modelos GA y retiros.
2. Google AI Studio — *Nano Banana image generation*. https://aistudio.google.com/docs/image-generation — fetch 200. Endpoint `interactions`, `response_format`, 14 refs, grounding web/image, SynthID, aspect ratios.
3. Google AI Studio — *Rate limits*. https://aistudio.google.com/docs/rate-limits — snippet. TPD por modelo (free tier).
4. `https://ai.google.dev/gemini-api/docs/pricing` — **timeout** en 4 rutas probadas; se usa `aistudio.google.com` como fuente equivalente. Limitación declarada.

**OpenAI** [en]
5. OpenAI — *Image generation guide*. https://developers.openai.com/api/docs/guides/image-generation — snippet oficial. Costos por token de GPT Image 2.5, tabla por imagen de GPT Image 2, retiro de `gpt-image-1` (2026-10-23).
6. OpenAI — *GPT-Image-1 (ficha)*. https://developers.openai.com/api/docs/models/gpt-image-1 — snippet oficial. Estado "Shut down".
7. OpenAI — *Image generation tool (Responses API)*. https://developers.openai.com/api/docs/guides/tools-image-generation — snippet oficial. Modelos soportados y `gpt-image-2.5-sunburst`/`-flare`.
8. Microsoft Learn — *Image generation models from OpenAI*. https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/dall-e — snippet. Retiro de `dall-e-3` en Azure (2026-03-04) y matriz de disponibilidad.

**OpenRouter** [en]
9. OpenRouter — *Images models (API)*. https://openrouter.ai/api/v1/images/models — fetch 200. Ids reales del catálogo.
10. OpenRouter — *Image generation guide*. https://openrouter.ai/docs/guides/overview/multimodal/image-generation — fetch 200. Contrato y parámetros por endpoint.
11. OpenRouter — `…/api/v1/images/models/<id>/endpoints` — fetch 200 por modelo. Tarifas `output_image` / `input_image`.

**Alternativas** [en]
12. Recraft — *API pricing*. https://www.recraft.ai/docs/api-reference/pricing — fetch 200. Unidades, raster/vector, herramientas.
13. Recraft — *Pricing & plans*. https://www.recraft.ai/pricing — fetch 200. Licencia del plan free (imágenes propiedad de Recraft, sin uso comercial).
14. Freepik — *API pricing*. https://tr.freepik.com/api/pricing — snippet. Precio por operación (Mystic, Nano Banana, Flux, Seedream, Imagen).
15. Freepik — *Pricing plans*. https://www.freepik.com/pricing — snippet. Planes, créditos, "ilimitado", licencia comercial IA.
16. Freepik — *Docs pricing*. https://jp.freepik.com/ai/docs/pricing — snippet. Créditos por plan y features.
17. Stability AI — *Pricing*. https://docs.stability.ai/pricing — fetch 200. Créditos a USD 0.01 y costo por modelo.
18. Ideogram — *FAQ*. https://docs.ideogram.ai/frequently-asked-questions — fetch 200. Planes, créditos gratis, uso comercial, API keys.
19. Leonardo — *Pricing and plans FAQ*. https://docs.leonardo.ai/docs/pricing-and-plans-faq — fetch 200 (act. 2026-09-01). API pay-as-you-go, sin fee.
20. Krea — *Pricing*. https://www.krea.ai/pricing — fetch 200. Free 100 units/día e imágenes por plan/modelo.
21. Krea — *API*. https://api.krea.ai/ — fetch 200. Playground, tokens de workspace, MCP.
22. Pollinations — *API docs*. https://text.pollinations.ai/APIDOCS.md — fetch 200. Endpoint GET libre, x402 USD 0.01, sin SLA.
23. Adobe — *Firefly API overview*. https://developer.adobe.com/firefly-services/docs/firefly-api/ — fetch 200. Image5, Custom Models, Composite, Upscale.
24. Adobe — *Firefly API pricing*. https://developer.adobe.com/firefly-services/docs/firefly-api/guides/pricing/ — **404**. Precio no publicado: gap declarado.
25. Playground AI — *Pricing*. https://playground.com/design/pricing — snippet. Free/Pro/Pro Plus, licencia, "API para partners".
26. Playground AI — *Help: API access*. https://help.playgroundai.com/en/articles/6861708-does-playground-ai-have-an-api-i-can-access-to-generate-images — snippet. Acceso solo por solicitud (>1M img/mes).
27. Midjourney — *Community Guidelines*. https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines — fetch 200. Sin API; automatización prohibida.
28. Alibaba Cloud — *qwen-image-2.1-turbo*. https://www.alibabacloud.com/help/es/model-studio/qwen-image-2-1-turbo — snippet. USD 0.014133/img, RPM 120.
29. Alibaba Cloud — *Qwen-Image API*. https://www.alibabacloud.com/help/en/model-studio/qwen-image-api — snippet. Resoluciones, 1–6 salidas, 24 h de retención.
30. QwenCloud — *Image generation models*. https://docs.qwencloud.com/developer-guides/getting-started/image-models — snippet. `qwen-image-3.0-pro`, `wan2.7-image-pro`, `z-image-turbo`.
31. Hugging Face — *Spaces overview*. https://huggingface.co/docs/hub/spaces-overview — fetch 200. ZeroGPU free (2 Spaces), tarifas GPU, sleep.

**Lugar / conocimiento de mundo** [en]
32. *When Cultures Meet: Multicultural Text-to-Image Generation*. ACL 2026 Findings. https://aclanthology.org/2026.findings-acl.1783.pdf — snippet. Sagrada Família como landmark de España; ΔS sobre SDXL, DALL·E 3, FLUX.
33. *WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation*. https://arxiv.org/abs/2503.07265 — fetch 200. 1.000 prompts, 25 subdominios, WiScore, 20 modelos.
34. Civitai — *FLUX Arch Realism LoRA*. https://civitai.com/models/709956/flux-arch-realism-lora — snippet. LoRA genérico de arquitectura, licencia **non-commercial**.
35. Hugging Face — `Wakkamaruh/balatro-poker-cards` — snippet. Única aparición de "sagrada familia" como texto de prompt de ejemplo; **no** es un LoRA del edificio.

**Telegram / n8n** [en]
36. Telegram — *Bot API: Sending files*. https://core.telegram.org/bots/api#sending-files — fetch 200. 5/20 MB por URL; 10/50 MB multipart; 2.000 MB con server local.
37. Telegram — *Bots FAQ*. https://core.telegram.org/bots/faq — fetch 200. 1 msg/s por chat, 20/min por grupo, ~30/s masivo, 429 + `retry_after`, Paid Broadcasts 1.000/s.
38. n8n — *Telegram Trigger*. https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/ — fetch 200. Eventos, *Download Images/Files*, restricción por chat.
39. n8n — *Telegram node*. https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/ — fetch 200. Operaciones y credenciales.
40. n8n — *HTTP Request*. https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/ — fetch 200. Form-Data + n8n Binary File, Response Format File, Timeout, Never Error, batching.
41. n8n — *Workflow 10466 (Gemini + Telegram)*. https://www-staging.n8n.io/workflows/10466-ai-image-generation-and-editing-with-google-gemini-and-telegram-bot — snippet. Precedente del patrón.

**ComfyUI / nitidez** [en]
42. ComfyUI — *Discussion #1002: latent upscale vs pixel upscale*. https://github.com/Comfy-Org/ComfyUI/discussions/1002 — fetch 200. Distorsión del ruido gaussiano; latente ≥0.55, píxeles ~0.25.
43. AIOFM — *Hi-Res Fix (glosario)*. https://aiofm.info/en/glossary/hi-res-fix — fetch 200. Definición operativa del upscale en dos pasos.

**Gaps declarados**

- `ai.google.dev/gemini-api/docs/*` — timeout sistemático (4 rutas). Se sustituyó por `aistudio.google.com/docs/*`.
- Adobe Firefly API — sin página de precios pública (404).
- Krea — precio por endpoint no verificado (página detrás de app).
- Precio de Mystic (Freepik) — discrepancia de ~17× entre la página oficial de API y un texto de terceros de septiembre; se presupuesta con el valor oficial.
- Free tier de Gemini para **uso comercial del estudio** — no confirmado.
- ModelScope "API gratis de Qwen-Image-2.1 ~250/día" — solo fuente terciaria.
- `flux-3`, `seedream-5.0`, `gpt-image-2.5-flare/sunburst`, `krea/k3-edit` en OpenRouter — vistos truncados, **no verificados**.
- n8n: comportamiento exacto del Telegram Trigger sin dominio público (webhook vs. fallback) — no documentado en la página del nodo; verificar en la instancia.

---

## Metodología

**Queries (2026-11-01, ES/EN):**

| Idioma | Query | Resultado |
|---|---|---|
| EN | image generation API models list openrouter image endpoints | Catálogo + precios por endpoint |
| EN | gemini image generation pricing per image nano banana pro | Fuente oficial (aistudio) |
| EN | Gemini API image generation response_format aspect_ratio image_size 4K | Endpoint `interactions`, 14 refs |
| EN | WISE benchmark world knowledge text-to-image | arXiv 2503.07265 |
| EN | multicultural text-to-image Sagrada Familia landmark | ACL 2026 Findings |
| EN | sagrada familia lora civitai huggingface | Sin LoRA dedicado |
| EN | latent upscale vs pixel upscale denoise comfyui | Discussion #1002 |
| EN | midjourney api official policy automation | Prohibición explícita |
| EN | telegram bot api sending files limits photo multipart | 5/10 MB foto; 20/50 otros |
| EN | telegram bot api rate limits 30 per second 20 per minute group | FAQ oficial |
| EN | n8n http request node binary file response format file timeout | Doc del nodo |
| EN | n8n telegram trigger download images webhook | Doc del trigger |
| EN | OpenRouter image model pricing gpt-image-2 gemini-3-pro-image | Tarifas |
| EN | OpenAI API pricing image gpt-image-1 per image DALL-E 3 still available | Retiros + tarifas 2.5 |
| EN | recraft api pricing units vector raster | Docs de pricing |
| EN | freepik API pricing mystic nano banana credits | Tabla por operación |
| EN | stability ai pricing credits stable image ultra | USD 0.01/crédito |
| EN | ideogram pricing plans commercial use api | Planes + ToS |
| EN | leonardo ai api pricing pay as you go | Sin fee mensual |
| EN | krea api pricing image models | Free 100 units/día |
| EN | playground ai public api partners | Solo partners >1M/mes |
| EN | adobe firefly api pricing image5 | 404 en pricing |
| EN | huggingface spaces zerogpu free tier gpu pricing | 2 Spaces gratis, tarifas/h |
| EN | pollinations api free image generation | GET libre + x402 |
| ES | Qwen Chat gratis generación de imágenes límites | ModelScope ~250/día (tercero); Chat ≠ API |
| ES | qwen image 2.1 turbo precio por imagen | USD 0.014133, RPM 120 |

**URLs con fetch 200 (20):** aistudio.google.com/docs/pricing · aistudio.google.com/docs/image-generation · openrouter.ai/api/v1/images/models · openrouter.ai/docs/guides/overview/multimodal/image-generation · arxiv.org/abs/2503.07265 · github.com/Comfy-Org/ComfyUI/discussions/1002 · aiofm.info/en/glossary/hi-res-fix · docs.midjourney.com/…/Community-Guidelines · core.telegram.org/bots/api#sending-files · core.telegram.org/bots/faq · docs.n8n.io/…/telegramtrigger/ · docs.n8n.io/…/n8n-nodes-base.telegram/ · docs.n8n.io/…/httprequest/ · docs.stability.ai/pricing · krea.ai/pricing · api.krea.ai · recraft.ai/pricing · recraft.ai/docs/api-reference/pricing · developer.adobe.com/firefly-services/docs/firefly-api/ · huggingface.co/docs/hub/spaces-overview · docs.ideogram.ai/frequently-asked-questions · docs.leonardo.ai/docs/pricing-and-plans-faq · text.pollinations.ai/APIDOCS.md.

**Errores de red:** `ai.google.dev` (4 rutas, timeout) · `developer.adobe.com/…/guides/pricing/` (404) · `https://playground.com/pricing` (solo snippet, sin cuerpo) · caché `raw/research-cache/` inexistente al inicio (creada con este informe).

---

## Propuestas wiki (esqueleto — no ejecutar, no escribir `wiki/`)

- `wiki/glosario/software/nano-banana.md` (nueva) — familia Gemini image: 5 modelos, precios por resolución, 14 refs, grounding imagen, SynthID, endpoint `interactions`.
- `wiki/glosario/software/openrouter.md` (actualizar § imagen) — catálogo `/api/v1/images/models`, tarifas `output_image`, margen vs directo.
- `wiki/glosario/software/gpt-image.md` (nueva) — 2.5 sunburst/flare, 2, 1.5/1-mini; retiros 2026-10-23 y 2026-12-01; 16 refs; tamaños múltiplos de 16.
- `wiki/glosario/software/recraft.md` (nueva) — vectores nativos, USD 0.007–0.30, **licencia free no comercial**.
- `wiki/glosario/software/freepik-magnific.md` (nueva) — rebranding 2026-04-28, tabla por operación, entrenamiento de LoRA propio.
- `wiki/glosario/software/n8n-telegram-bot-imagen.md` (nueva) — blueprint de 6 nodos, base64, Timeout, rate limit, webhook público.
- `wiki/glosario/conceptos/conocimiento-de-lugar-t2i.md` (nueva) — ΔS/WiScore, por qué texto ≠ identidad de sitio, 3 vías de inyección (refs / grounding / LoRA).
- `wiki/glosario/conceptos/upscale-latente-vs-pixel.md` (nueva) — denoise ≥0.55 latente / 0.25 píxeles; corrige el pipeline SDXL del estudio.
- `wiki/glosario/interno/pbooks/pbk-comfyui.md` (§ nitidez y § API externas) — orden txt2img → refiner → tiles → ESRGAN.
- `wiki/glosario/entidades/openai.md`, `google-deepmind.md` (§ imagen) — sólo si el glosario ya los tiene como entidad.
- `proyectos/concurso-gaudi-nexus/` — nota de decisión: motor por defecto Nano Banana 2.1, entrega con Nano Banana Pro 4K, edición quirúrgica con gpt-image-2.5.

*Pendiente de formato: `@contenidos` decide si esto va a `raw/contenidos/` y con qué recorte. Este informe no escribe `wiki/`.*
