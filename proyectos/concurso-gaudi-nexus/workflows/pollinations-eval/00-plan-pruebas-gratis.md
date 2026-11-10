---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: Plan de pruebas gratis Pollinations text-to-image
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
estado: borrador-activo
tags: [concurso, gaudi-nexus, pollinations, pruebas, text-to-image, n8n, telegram]
idioma: es
---

# Plan de pruebas gratis Pollinations text-to-image

> Todo lo testeable con costo cero o grants en el workflow `Eval imagen Telegram — Pollinations vs OpenRouter` (`YLrbR8z4sPHPnJBy`). OpenRouter queda desactivado durante esta tanda, tal como pide Sol.

## Dónde abrir el flujo

- n8n → Workflows → buscar `Eval imagen Telegram` → ID `YLrbR8z4sPHPnJBy`.
- URL directa estimada: `https://n8n.pitau.tech/workflow/YLrbR8z4sPHPnJBy` (misma instancia de `N8N_MCP_TOKEN`).
- Nodos: `Telegram Trigger` → `ElegirMotor (Switch)` → `HTTP Pollinations` / `HTTP OpenRouter (deshabilitado)` → `Binario foto (Code)` → `Enviar foto`.

## Lo desconectado

| Punto | Estado | Acción |
|---|---|---|
| `HTTP Pollinations` credencial | Auth `httpTemplatedCustomAuth` creada pero credencial vacía | En n8n UI: abrir nodo → Credentials → crear Header Auth `Authorization: Bearer sk_...` (valor en `.env` `POLLINATIONS_API_KEY`) → Save → Test |
| Workflow | Inactivo (`active: false`) | Activar tras cargar credencial |
| `HTTP OpenRouter` | Deshabilitado (`disabled: true`) | Dejar así durante tanda gratis |
| Modelo actual | `google/gemini-2.5-flash-image` legacy vía `POST /v1/images/generations` | Migrar a flux en T1 |
| `Telegram Trigger` | Webhook registrado al activar | Tras activar, mandar `poll: hola` al bot para validar |

## Prompt base cáscara

```text
distant wide-angle view across plaza toward Sagrada Familia Barcelona, lightweight inverted catenary concrete shell pavilion with glass roof, thin white shell parametric ribbed structure, open stone plaza, trees, people for scale, Eixample facades background, warm dusk light, photorealistic architectural photography, ultra detailed
```

## Tanda gratis T1–T10

| # | Prueba | Modelo | Endpoint | Params | Costo | Éxito |
|---|---|---|---|---|---|---|
| T1 | Base flux rápida | `black-forest-labs/flux.1-schnell` (`flux`) | `GET /image` | 1280x720, seed 7, nologo | 0.002 | Cáscara legible, Sagrada presente |
| T2 | Base flux variada | mismo flux | `GET /image` | mismo prompt, seed timestamp | 0.002 | 3 variantes distintas votables |
| T3 | Fino flux.1 | `black-forest-labs/flux.1.1-pro` | `GET /image` | 1280x704, seed 7 (múltiplo 32) | 0.03 | Curva continua + Sagrada completa |
| T4 | Nítido turbo | `tongyi-mai/z-image-turbo` (`z-image`) | `GET /image` | 1280x720, seed 7 | 0.004 | canopy + vidrio enmarcando Sagrada |
| T5 | Instantáneo sana | `lykon/dreamshaper-8-lcm` (`sana`) | `GET /image` | 1024x1024, seed 7 | 0.0001 | Mood rápido para grupo |
| T6 | Interactivo klein | `black-forest-labs/flux.2-klein-4b` (`klein`) | `GET /image` | 1280x720, seed 7 | 0.005 | Geometría + edición futura |
| T7 | Texto preciso | `microsoft/mai-image-2.6-flash` | `GET /image` | 1280x720, seed 7 | 0.00001425 + tokens | Cartelería legible |
| T8 | SDXL rápido | `community/scriptsnsenses-sys/sdxl-lightning-free` | `GET /image` | 1024x1024, seed 7 | 0 | Alternativa 0 Pollen |
| T9 | POST compatible | `flux.1-schnell` | `POST /v1/images/generations` `response_format:url` | mismo prompt + width/height/seed | 0.002 | URL pública + caption motor/costo |
| T10 | Interior flux | `flux.1-schnell` | `GET /image` | 1280x720, seed 21, prompt interior eye-level | 0.002 | Sagrada enmarcada entre nervios |

Prompt interior T10:

```text
eye-level view from inside lightweight inverted catenary concrete shell pavilion with glass roof, thin white parametric ribs overhead filtering daylight, polished stone floor reflecting, framed view toward Sagrada Familia towers through open side, people walking, trees at edges, soft morning light, photorealistic architectural interior photography, ultra detailed
```

## Variantes de parámetros

- `seed`: 7 fijo para repetir, timestamp para variar desde Telegram.
- `width/height`: 1280x720 libre en schnell/z-image, 1280x704 en 1.1-pro (múltiplos de 32).
- `nologo=true`, `enhance=false/true`, `safe=true` para metadatos.
- `model`: cambiar solo ese query para rotar T1–T8 con el mismo cableado.
- `Prefer: respond-async` + `GET /v1/jobs/{id}` + `GET /v1/jobs/{id}/result` para 2K cuando el render crezca.
- `POST /v1/chat/completions` con model flux para agente que redacta y genera en un paso.

## Orden sugerido

1. Cargar credencial + activar + `poll: hola`.
2. T1, T2, T10 (mismo flux, 3 miradas).
3. T4, T5, T6 (rotación barata).
4. T3, T7 (lámina + texto).
5. T9 (cableado POST para caption con costo).
6. Registrar cada corrida en `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/` + reporte `20-reporte-corridas-YT`.

## Registro

- Pruebas ya corridas 2026-11-03: plaza 401 KB, flux 293 KB, z-image 253 KB, interior 444 KB, flux11pro 185 KB.
- Detalle motores y límites: [[wiki/glosario/software/pollinations|pollinations]].
- Backlog madre: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas|30-backlog-futuras-pruebas]].
