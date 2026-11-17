---
fecha: 2026-11-17
tema: Hermes AI API image-to-image — evaluación aparte
slug: hermes-ai-api-image-to-image
idiomas: [es, en]
fuentes_n: 4
confianza: alta (docs oficiales api.hermes-ai.net verificadas 17/11)
estado: crudo
---

# Hermes AI API image-to-image — evaluación aparte

Fecha: 2026-11-17
Origen: https://api.hermes-ai.net/models?output=image&category=image-to-image

## Ojo nombres: no es el mismo Hermes

- **Hermes Agent (NousResearch, MIT)** — nuestro agente en VPS, open-source, gateway Telegram, Kanban, skills.
- **Hermes AI API (MIMOS AI LTD, comercial)** — agregador de 125 familias / 19 providers con una API key, async jobs + MCP remoto. Es proveedor, no agente.

Para usarlo en Studio OS sí hay que conectar el agente Hermes. Sin conexión es solo catálogo web.

## Catálogo image-to-image (19)

Nano Banana Pro, Nano Banana 2, Nano Banana 2.1, GPT Image 2.5 / 2.0 / 2.6, FLUX 3, FLUX.2 Dev / Klein 9B, FLUX.1 Kontext Dev, Seedream 5.0 / 5.5 / 4.7, Qwen Image 3.0 / 2.0 / Edit 2511, Grok Imagine Image, Wan 2.5 Preview, Z Image Turbo. Filtros: 4K top, 7 providers (Alibaba, BFL, ByteDance, Google, OpenAI, Qwen, xAI).

Fuente: https://api.hermes-ai.net/models?output=image&category=image-to-image

## Cómo se cobra

- Prepaid credits packs $10 / $25 / $50 / $100 / $200, sin suscripción. Hasta 28% bajo precio oficial según marketing.
- Reserva al aceptar, cobra solo si succeed, devuelve si falla. Idempotency-Key soportado.
- Pricing page hoy devuelve “Loading price…” en todos — no hay número público para presupuestar sin llamar `get_model`. Ver: https://api.hermes-ai.net/pricing

## Cómo se llama

REST async: `POST /api/v1/jobs {model, input}` → 202 + task_id → `GET /api/v1/jobs/{id}` hasta succeed. LLMs sync vía `/api/v1/chat/completions` OpenAI-compatible. Quickstart: https://api.hermes-ai.net/docs/quickstart

MCP remoto: `https://api.hermes-ai.net/mcp` (Streamable HTTP, OAuth 2.1 PKCE o Bearer `HERMES_API_KEY`). Tools: `search_models / get_model / create_task / wait_for_task / get_task / list_tasks / get_balance`. Fuente: https://api.hermes-ai.net/agents/mcp

## Opciones de conexión desde nuestro Hermes Agent

A) **MCP directo (recomendado para probar)** — agregar en `config.yaml`:
```yaml
mcp_servers:
  hermes-ai-api:
    url: "https://api.hermes-ai.net/mcp"
    auth: oauth
    trust: untrusted
    tools:
      include: [search_models, get_model, create_task, wait_for_task, get_task, get_balance]
```
Pro: sin código, respeta niveles A-D (escritura = C). Contra: OAuth por perfil, costo opaco hasta `get_model`.

B) **REST vía n8n determinista** — flujo `pedido → get_model (precio) → create_task → poll → vault`. Pro: costo visible antes de gastar (RF-23), trazable. Contra: hay que escribir el flujo.

C) **Provider plugin propio** — `register_image_gen_provider` como fal/openrouter. Pro: entra al router. Contra: desarrollo y mantenimiento.

## Veredicto para Studio OS

- Hoy seguir con OpenRouter (Nano $0.067/1K, Seedream $0.045) + fal + ComfyUI local, que ya tienen precio verificado y router.
- Hermes AI API queda como **proveedor candidato** para image-to-image cuando publiquen precios estables y convenga por 4K o variantes economy. Probar vía opción A en banco, con tope de créditos $10 y solo material derivado.
- No reemplaza al agente: lo alimenta.
