---
tipo: software
software: cloudflare-workers-ai
categoria: proveedor-ia
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [glosario, software, cloudflare, workers-ai, flux, klein, gratis, n8n, proveedor]
idioma: es
---

# Cloudflare Workers AI — GPU gratis con cuota diaria

> Plataforma de inferencia serverless de Cloudflare: llamás modelos por REST, sin alquilar GPU ni instalar nada. Incluye FLUX.1 schnell y FLUX.2 klein 4B en el tier gratis. La vía del estudio para generación diaria sin depender de los grants de Pollinations.

- [[#Qué es]]
- [[#Precio: Neurons y cuota gratis]]
- [[#Modelos de imagen que sirven al estudio]]
- [[#Cómo se llama (REST)]]
- [[#Conexión con el agente n8n]]
- [[#Modelos de texto (el cerebro, no la mano)]]
- [[#Límites y cuidados]]
- [[#Cuándo usar cada proveedor]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué es

Workers AI es la capa de inferencia de Cloudflare: los modelos corren en GPUs de Cloudflare y vos los invocás por HTTP. No hay pods, no hay instalación, no hay ComfyUI. Pagás (o no) por **Neurons**, la unidad de cómputo de la plataforma. Todo resetea a diario.

## Precio: Neurons y cuota gratis

- **10.000 Neurons/día gratis**, todos los días, resetea 00:00 UTC. Sin tarjeta.
- Excedente (plan Workers Paid): $0.011 cada 1.000 Neurons.
- Se consulta el consumo en el dashboard de Cloudflare (AI → Workers AI).

## Modelos de imagen que sirven al estudio| Modelo | ID | Costo estimado 1024² | Rinde diario gratis |
|---|---|---|---|
| FLUX.1 schnell | `@cf/black-forest-labs/flux-1-schnell` | ~58 Neurons | ~170 imgs |
| FLUX.2 klein 4B | `@cf/black-forest-labs/flux-2-klein-4b` | ~126 Neurons | ~80 imgs |
| FLUX.2 klein 9B | `@cf/black-forest-labs/flux-2-klein-9b` | ~1364 Neurons el primer MP | ~7 imgs |
| FLUX.2 dev | `@cf/black-forest-labs/flux-2-dev` | según tiles × pasos | decenas |

Estimaciones propias desde la tabla oficial (tiles + steps). Lo relevante: schnell y klein-4b dan producción diaria real gratis; el 9B queda para pruebas puntuales.

Verificado en cuenta real 2026-11-12 (batería):
- schnell: acepta `prompt` + `steps`, **sin** `seed` (5006 si se envía). 1024² = 172.8 Neurons.
- klein-4b: multipart, acepta `seed` (verificado 42), `width`/`height`, `guidance`; 1–2 refs verificadas (edit simple 652 KB, 2-refs 316 KB).
- klein-9b: multipart aceptado pero **error interno 3043** en 1024 y 512 el 2026-11-12 — reintentar otro día.
- Chat completions OpenAI-compatible (`/ai/v1/chat/completions`): qwen3-30b responde OK — vía para cerebro LLM gratis si hiciera falta.

### Edición con referencia (klein-4b, no solo txt2img)

A diferencia de schnell, klein-4b unifica generación y edición: acepta **hasta 4 imágenes de entrada** (`input_image_0..3`, binario, cada una <512px) y el prompt puede referenciarlas por índice ("take the subject of image 1 and style it like image 0"). Es el reemplazo natural de kontext para el loop conserva+cambia, con cuota diaria en vez de grants. Steps fijo en 4 (destilado); width/height 256–1920, seed y guidance configurables. Se manda como `multipart/form-data`, no JSON:

```sh
curl --request POST \
  --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-4b' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'prompt=take the subject of image 1 and style it like image 0' \
  --form 'input_image_0=@foto_base.jpg' \
  --form width=1024 \
  --form height=1024
```

## Cómo se llama (REST)

Sin SDK ni worker propio: HTTP directo.

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-1-schnell \
  -X POST \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -d '{ "prompt": "catenary concrete shell pavilion at golden hour", "steps": 4 }'
```

Requisitos previos (una sola vez, en el navegador): cuenta Cloudflare gratis → copiar **Account ID** → crear **API Token** con permiso Workers AI. Se guardan en `.env` (`CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`).

Verificado 2026-11-12 en cuenta real: el schema REST de schnell acepta `prompt` + `steps` (**sin** `seed`, lo rechaza con 5006); responde JSON `{result: {image: base64, usage: {neurons}}}` — una 1024² costó 172.8 Neurons (~58/día a ese tamaño). klein-4b por multipart con 1 referencia funciona (652 KB, geometría de base respetada a ojo).

## Conexión con el agente n8n

Entra por el nodo **HTTP Request** que el agente ya usa: POST a la URL de arriba, header `Authorization: Bearer`, body JSON con el prompt armado por el agente. La respuesta es JSON con la imagen en base64 (`result.image`) — el nodo la decodifica y el flujo sigue igual que con Pollinations (Telegram foto). Sin plugin, sin código, solo credenciales nuevas. Token `pi_img_02`: 90 días, sin filtro IP (decisión 2026-11-12; la 01 se rotó por exposición en chat).

## Modelos de texto (el cerebro, no la mano)

Workers AI también expone LLMs con endpoint compatible OpenAI (`/ai/v1/chat/completions`). Gratis: llama, qwen, gpt-oss, glm-4.7-flash. Atención: **`glm-5.3-flash` exige método de pago** en Cloudflare, así que el cerebro del agente sigue en OpenRouter; Cloudflare aporta la mano (imagen).

## Licencias: qué modelo te deja hacer qué

- **klein 4B (FLUX.2) — Apache 2.0**: correr, vender, fine-tunear. Todo libre.
- **klein 9B / dev / kontext dev (FLUX.2) — FLUX Non-Commercial**: solo test/evaluación; trabajo de cliente exige licencia paga o vía API.
- **FLUX.3 Image Klein (5.6B, 4K nativo, bounding boxes, multi-ref) — FLUX Kommunity License**: imágenes generadas usables comercialmente si se factura <$5M/año (revisar outputs y declarar IA donde la ley pida); fine-tunes comerciales requieren licencia BFL. Base (para entrenar) + destilado (rápido) + cuantizados INT8/FP8/NVFP4.
- **Vía Workers AI no corrés pesos**: usás la API del proveedor (zero data retention declarado). Las imágenes son tuyas y usables comercialmente; la restricción NC de "no correr pesos" no aplica.

## Límites y cuidados

- La cuota es diaria y no acumula: lo que no se usa se pierde a las 00:00 UTC.
- Algunos modelos (fronterizos y el GLM 5.3) piden billing aunque no lo uses: leer la nota "require a paid billing method" antes de elegir modelo.
- Retención de datos: es Cloudflare (ver términos del proveedor); para material sensible del concurso aplican las mismas reglas que con cualquier nube.

## Cuándo usar cada proveedor

| Caso | Proveedor |
|---|---|
| Exploración diaria, volumen (decenas/día) | Cloudflare (cuota predecible) |
| Edición con referencia (kontext) y pro puntual | Pollinations con grants/recarga |
| NanoBanana con grounding, video, 3D | Pollinations pago (Paid Pollen) |
| ControlNet, inpaint fino, LoRA propio | ComfyUI local / pod |

## Conceptos relacionados

- [[wiki/glosario/software/pollinations|pollinations]] — el otro proveedor de imagen (grants, kontext, paid-only)
- [[wiki/glosario/software/flux1|flux1]] — familia FLUX.1
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — klein 9B del concurso
- [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] — dónde renderizar y con qué licencia
- [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]] — playbook del agente pi imágenes

## Referencias

- [Cloudflare — Workers AI pricing (10.000 Neurons/día, tabla por modelo)](https://developers.cloudflare.com/workers-ai/platform/pricing/) (verificado 2026-11-12 — 200)
- [Cloudflare — Modelo flux-1-schnell (endpoint REST, parámetros)](https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/) (verificado 2026-11-12 — 200)
- [Cloudflare — Changelog klein-4b en Workers AI (multipart, input_image_0..3, steps fijo 4)](https://developers.cloudflare.com/changelog/post/2026-01-15-flux-2-klein-4b-workers-ai/index.md) (verificado 2026-11-12 — 200)
- [Comfy — FLUX 3 Image Klein (5.6B, 4K, Kommunity License, <$5M)](https://comfy.org/flux-3-image-klein) (verificado 2026-11-12 — 200)
- [BFL — Cómo funciona el licenciamiento FLUX (open-weights vs API)](https://help.bfl.ai/articles/9272590838-can-i-use-the-api-for-a-commercial-application) (verificado 2026-11-12 — 200)
