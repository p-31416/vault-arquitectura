---
tipo: software
software: Pollinations
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [glosario, software, pollinations, imagen-ia, n8n, telegram, concurso-gaudi-nexus]
idioma: es
---

# Pollinations

Generación de imagen por API con tier gratis real. Lo usa el estudio para prototipar el bot de Telegram → n8n → imagen sin pagar.

- [[#Descripción]]
- [[#Autenticación]]
- [[#Uso básico imagen]]
- [[#Workflow n8n Telegram]]
- [[#Flujos con flux para n8n]]
- [[#Prompt cáscara catenaria Sagrada Familia]]
- [[#Backlog pruebas futuras]]
- [[#Modelos gratuitos]]
- [[#Límites]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Descripción

API unificada texto / imagen / video / audio en `https://gen.pollinations.ai`. Para imagen alcanza un `GET` con el prompt en la URL. Sin SLA, ideal para iterar concurso, no como único motor de entrega final.

Key del estudio en `.env` como `POLLINATIONS_API_KEY=sk_...` (server-to-server, permiso `image`).

## Autenticación

Dos tipos de key (docs nov-2026):

| Tipo | Prefijo | Uso |
|---|---|---|
| Secret key | `sk_` | API requests. La que usa n8n. Permisos por modelo + budgets. Nunca en browser. |
| App key | `pk_` | Solo `client_id` OAuth. Desde 2026-11-01 mandar `pk_` directo da `401`. Frontend usa Pollinations Pay / BYOP para canjear `sk_` temporal. |

Formas de mandar:

- Header: `Authorization: Bearer TU_SK_`
- Query: `?key=TU_SK_`

Listar modelos (`GET /models`, `/image/models`) no necesita auth. Crear key en `enter.pollinations.ai/keys`. Consent default docs: cap 5 Pollen / 7 días expiración, editable.

### Qué hace

Valida `sk_` + descuenta Pollen por request.

### Sintaxis / Cómo se usa

```powershell
$key = ((Get-Content ".env" | Where-Object { $_ -match "^POLLINATIONS_API_KEY=" }) -replace "^POLLINATIONS_API_KEY=","").Trim()
Invoke-RestMethod -Headers @{Authorization="Bearer $key"} https://gen.pollinations.ai/account/balance
```

### Ejemplo

```powershell
$prompt = [uri]::EscapeDataString("plaza contemporanea frente a la Sagrada Familia al atardecer")
$url = "https://gen.pollinations.ai/image/$prompt?model=black-forest-labs/flux.1-schnell&width=1280&height=720&seed=7&nologo=true"
Invoke-WebRequest -Uri $url -Headers @{Authorization="Bearer $key"} -OutFile catenaria.jpg -TimeoutSec 120
```

### Uso en vault

- `proyectos/concurso-gaudi-nexus/` para vistas rápidas de plaza.
- `raw/sessions/2026-11-02-sesion-telegram-pollinations.md` pipe original.

---

## Uso básico imagen

```text
GET https://gen.pollinations.ai/image/{prompt}?model={id}&width=1280&height=720&seed=7&nologo=true
```

Params útiles: `model`, `width`, `height`, `seed` (fija para repetir, `timestamp` para evitar cache), `nologo=true`, `enhance=false`, `key` como alternativa al header.

## Workflow n8n Telegram

Ya creado: `Eval imagen Telegram — Pollinations vs OpenRouter` (`YLrbR8z4sPHPnJBy`).

```text
[Telegram Trigger: Message, Download Images = ON]
  → [Switch por prefijo: or: → OpenRouter, resto → Pollinations]
  → [HTTP Request GET a gen.pollinations.ai/image/... con Bearer sk_]
  → [Code a binario]
  → [Telegram Send Photo con caption motor+costo]
```

Pendiente: completar credencial `sk_` en el nodo Pollinations + activar + probar `poll:` vs `or:`.

## Flujos con flux para n8n

Avanzan de exploración veloz hacia entrega cuidada, todos con la misma `sk_`.

### F1 — txt2img veloz con flux.1-schnell (alias `flux`)

Exploración masiva de cáscara. 0.002 Pollen, respuesta en segundos, ideal para iterar en Telegram.

```text
GET https://gen.pollinations.ai/image/{prompt-url}?model=black-forest-labs/flux.1-schnell&width=1280&height=720&seed={seed}&nologo=true
```

n8n: `Telegram Trigger` → `HTTP Request GET` (`Response Format: File`, `Timeout: 120000`) → `Telegram Send Photo`. `seed=timestamp` para variar, `seed` fijo para repetir.

Probado 2026-11-03 seed 7: cáscara maciza nervada, composición fuerte, vidrio con presencia leve. Favorito de Sol para masa.

### F2 — txt2img cuidado con flux.1.1-pro

Mismo prompt, adherencia fina y dimensiones precisas. 0.03 Pollen. Requiere `width` y `height` en múltiplos de 32 (ej 1280x704).

```text
GET https://gen.pollinations.ai/image/{prompt-url}?model=black-forest-labs/flux.1.1-pro&width=1280&height=704&seed=7&nologo=true
```

Probado 2026-11-03 seed 7, 8 s, 185 KB: [activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux11pro-2026-11-03.jpg] — onda continua iluminada, vanos ovalados, Sagrada completa a la derecha. Mejor lectura de curva invertida + luz cálida.

n8n: mismo cableado que F1, solo cambia `model` + resolución múltiplo de 32.

### F3 — OpenAI-compatible POST para n8n Code

Entrega `b64_json` o `url`, cómoda paraCaption con motor + costo.

```json
POST https://gen.pollinations.ai/v1/images/generations
{
  "model": "black-forest-labs/flux.1-schnell",
  "prompt": "distant wide-angle view across plaza toward Sagrada Familia...",
  "width": 1280, "height": 720, "seed": 7,
  "response_format": "url"
}
```

n8n: `HTTP Request POST JSON` → `IF response_format=url` → `HTTP GET File` → `Send Photo`; con `b64_json` → `Convert to File` directo.

### F4 — Edición con referencia (kontext / klein)

Ancla la Sagrada real: foto de plaza + instrucción de intervención.

```text
POST https://gen.pollinations.ai/v1/images/edits
Form-Data: image=@plaza.jpg, prompt="conserva fachada y torres, agrega cáscara invertida de hormigón + vidrio en primer plano", model=black-forest-labs/flux.1-kontext-pro
```

Modelos: `flux.1-kontext-pro` (alias `kontext`, 0.03, instrucción fina) y `flux.2-klein-4b` (alias `klein`, 0.005, gen + edición hasta 2.4 MP). n8n: `Telegram Trigger Download Images=ON` → `HTTP POST Form-Data Binary` → `Send Photo`.

### F5 — Async para renders largos

Evita corte de timeout en n8n con `Prefer: respond-async`, luego sondeo.

```bash
curl -sS "https://gen.pollinations.ai/image/{prompt}?model=black-forest-labs/flux.1.1-pro" \
  -H "Authorization: Bearer $KEY" -H "Prefer: respond-async"
# → 202 {id} → GET /v1/jobs/{id} hasta succeeded → GET /v1/jobs/{id}/result -o final.jpg
```

n8n: `HTTP` → `Wait 5s` → `HTTP poll` en loop hasta `succeeded`.

### F6 — Chat multimodal que devuelve imagen

El mismo agente redacta y genera, útil para sufijo de estilo por expresión.

```json
POST https://gen.pollinations.ai/v1/chat/completions
{"model":"black-forest-labs/flux.1-schnell","messages":[{"role":"user","content":"A lighthouse at dawn"}]}
```

Devuelve Markdown con embed + URL pública en header `Link`. n8n: `AI Agent` → `HTTP` → `Send Photo`.

### flux vs flux.1.1-pro

| | `flux.1-schnell` (flux) | `flux.1.1-pro` (flux.1) |
|---|---|---|
| Costo | 0.002 Pollen, exploración amplia | 0.03 Pollen, entrega cuidada |
| Velocidad | Segundos, ideal Telegram | ~8 s en 1280x704, igual ágil |
| Adherencia | Masa fuerte, detalle sintético | Curva continua + luz coherente, Sagrada completa |
| Resolución | 1280x720 libre | Múltiplos de 32 (usar 1280x704) |
| Uso sugerido | 20 variantes por tarde, vota en grupo | 3 finalistas para lámina |

Cierre: F1 para abrir abanico, F2 para cerrar lámina, F4 con foto real para identidad de lugar, F5 cuando el render crezca a 2K.

## Prompt cáscara catenaria Sagrada Familia

Original ES:

```text
cascara de hormigon con cubierta de vidrio con curva catenaria invertida en la plaza de la sagrada familia vista desde lejos
```

Mejorado EN (probado 2026-11-03, seed 7, 1280x720):

```text
distant wide-angle view across plaza toward Sagrada Familia Barcelona, lightweight inverted catenary concrete shell pavilion with glass roof, thin white shell parametric ribbed structure, open stone plaza, trees, people for scale, Eixample facades background, warm dusk light, photorealistic architectural photography, ultra detailed
```

Resultados 2026-11-03:

- flux: [activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux-2026-11-03.jpg] — 293 KB. Cáscara maciza nervada, 3 pináculos detrás. Composición fuerte, vidrio poco legible. Favorito de Sol.
- z-image-turbo: [activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-zimage-2026-11-03.jpg] — 253 KB. Canopy de hormigón ramificado + cubierta vidrio, Sagrada enmarcada al fondo. Mejor match al brief catenaria invertida + vidrio.
- Test previo plaza: [activos/proyectos/concurso-gaudi-nexus/pollinations-tests/sagrada-plaza-2026-11-03.jpg] — 401 KB.
- flux interior (seed 21, 1280x720): [activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux-interior-2026-11-03.jpg] — 444 KB. Vista eye-level desde dentro, nervios filtrando luz, piso pulido reflejante, Sagrada enmarcada al fondo.

```text
eye-level view from inside lightweight inverted catenary concrete shell pavilion with glass roof, thin white parametric ribs overhead filtering daylight, polished stone floor reflecting, framed view toward Sagrada Familia towers through open side, people walking, trees at edges, soft morning light, photorealistic architectural interior photography, ultra detailed
```

Lectura: escribir siempre en EN, fijar vista (`distant wide-angle view`), material + estructura (`thin white shell parametric ribbed`), contexto (`Eixample facades`), luz (`warm dusk light`) y cierre foto (`photorealistic architectural photography`).

## Modelos gratuitos

Catálogo live `GET /image/models` 2026-11-03 (103 modelos totales). Gratis-tier = `paid_only=false`:

| Modelo | Precio Pollen | Alias | Nota |
|---|---|---|---|
| `community/scriptsnsenses-sys/flux-2-dev-free` | 0 | — | FLUX 2 Dev gratis, loguea prompts |
| `community/scriptsnsenses-sys/sdxl-lightning-free` | 0 | — | SDXL Lightning gratis |
| `microsoft/mai-image-2.6-flash` | 0.00001425 + tokens | — | Fotorreal + texto preciso |
| `lykon/dreamshaper-8-lcm` | 0.0001 | `sana`, `dreamshaper` | Casi instantáneo, detalle simple |
| `community/MarcosFRG/sdxl-lightning` | 0.0012 | — | SDXL 1024px rápido |
| `black-forest-labs/flux.1-schnell` | 0.002 | `flux` | Rápido, recomendado default |
| `tongyi-mai/z-image-turbo` | 0.004 | `z-image` | Instantáneo, nítido upscaleado |
| `black-forest-labs/flux.2-klein-4b` | 0.005 | `flux-klein`, `klein` | Gen + edición hasta 2.4 MP |
| `black-forest-labs/flux.1.1-pro` | 0.03 | — | Dimensiones precisas |
| `black-forest-labs/flux.1-kontext-pro` | 0.03 | `kontext` | Edición por instrucción |

`sana` es alias de `dreamshaper-8-lcm`, no modelo separado. `flux` = `flux.1-schnell`, 0 Pollen efectivo en cuenta con grants.

## Límites

- Anónimo clásico: 1 imagen por vez, ~45 s entre pedidos, error 402 hasta siguiente slot, modelo libre rotativo.
- Con key: gasta Pollen real, budget = límite no saldo aparte. Revisar en `GET /account/balance`.
- Sin garantía de uptime. No mandar piezas finales solo desde acá.
- Telegram: foto por URL 5 MB, multipart 10 MB. Render 2K PNG entra, 4K mejor en JPG 90.
- n8n: `Timeout` explícito 120-180 s, si no corta generaciones largas ya cobradas.
- Privacidad: modelos `free` comunitarios pueden loguear prompts.

## Backlog pruebas futuras

Backlog madre del concurso: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas|30-backlog-futuras-pruebas]] — unifica YT-01–04 + reporte + líneas Sherlock A–D. Las pruebas Pollinations alimentan ese backlog y se registran en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]] cuando se corren.

Pendientes Pollinations vinculados:

- **P1** — F4 kontext con foto real de plaza: conserva torres, agrega cáscara + vidrio. Conexión directa con L1–L4 de iluminación y V1 de vistas del backlog.
- **P2** — F2 flux.1.1-pro en 3 variantes luz (mañana / tarde / noche) del mismo seed 7, para votar final de lámina.
- **P3** — F1 flux con sufijo de estilo por expresión en n8n (v2 del pipe Telegram), luego expansor de prompt.
- **P4** — F5 async en 2K para la elegida, mide latencia real y costo Pollen por imagen.

Fuente madre: `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas.md`.

## Conceptos relacionados

- [[wiki/glosario/software/n8n]]
- [[wiki/glosario/software/telegram]]
- [[wiki/glosario/software/comfyui]]
- [[wiki/glosario/software/proveedores-modelos-ia]]

## Referencias

- [Pollinations Docs — Authentication](https://gen.pollinations.ai/docs#tag/authentication) (verificado 2026-11-03 — 200)
- [Pollinations Keys](https://enter.pollinations.ai/keys) (verificado 2026-11-03 — 200)
- [Pollinations Models](https://gen.pollinations.ai/models) (verificado 2026-11-03 — 200)
