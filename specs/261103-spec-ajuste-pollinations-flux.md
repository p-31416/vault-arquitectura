---
tipo: spec
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [spec, pollinations, flux, n8n, telegram, text-to-image, concurso, hermes]
estado: activo
---

# Spec plan Pollinations gratis — quick wins y escala hacia Hermes

> Empezar por wins rápidos en Telegram con flux, escalar a router + edición con foto, y dejar el contrato listo para que Hermes opere los mismos tools. Aplicado en n8n: `HTTP Pollinations` ya pide `flux.1-schnell`, caption ya dice `Pollinations - flux`.

- [[#Objetivo]]
- [[#Estado actual]]
- [[#Fase 0 Conexión]]
- [[#Fase 1 Quick wins]]
- [[#Fase 2 Escala gratis]]
- [[#Fase 3 Contrato Hermes]]
- [[#Fase 4 RunPod Comfy]]
- [[#Gates]]
- [[#Costos]]
- [[#Riesgos]]

## Objetivo

Probar todo lo testeable gratis en Pollinations para lo que el local resuelve con límite, con quick wins hoy y escala pensada para que Hermes opere mejor después: mismos endpoints, mismos prompts, contrato de tools estable.

## Estado actual

Workflow `Eval imagen Telegram — Pollinations vs OpenRouter` (`YLrbR8z4sPHPnJBy`), inactivo, 7 nodos. Aplicado por MCP 2026-11-03: modelo `black-forest-labs/flux.1-schnell` + prompt con limpieza de prefijo + caption flux.

| Punto | Estado |
|---|---|
| `HTTP Pollinations` auth | Template `httpTemplatedCustomAuth` vacío, falta credencial en UI |
| Modelo | flux schnell (gratis real) vía `POST /v1/images/generations` |
| `HTTP OpenRouter` | Deshabilitado, queda así |
| Activación | Pendiente tras credencial |

## Fase 0 Conexión

Quick win de 15 minutos, todo en UI:

1. Crear Header Auth `Authorization: Bearer sk_...` (valor en `.env` `POLLINATIONS_API_KEY`) y asignarla al nodo `HTTP Pollinations`. Test → 200.
2. Activar workflow.
3. Mandar `poll: hola` al bot.

## Fase 1 Quick wins

Solo flux + prompts ya validados en directo, para comparar Telegram contra directo:

- Q1 = T1 cáscara lejana seed 7 (referencia ya generada, 293 KB).
- Q2 = T2 mismo prompt seed timestamp, 3 variantes votables en el grupo.
- Q3 = T10 interior eye-level seed 21 (referencia ya generada, 444 KB).

Registro: `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/` + reporte `20-reporte-corridas-YT`.

## Fase 2 Escala gratis

Router por prefijos en `ElegirMotor`: `flux:` schnell, `flux1:` 1.1-pro 1280x704, `z:` z-image-turbo, `sana:`, `klein:`, resto → flux. Más rama `img:`: foto del chat (Download Images ON) + instrucción hacia `POST /v1/images/edits` con `kontext-pro`. Tanda T3–T9 del plan (`proyectos/concurso-gaudi-nexus/workflows/pollinations-eval/00-plan-pruebas-gratis.md`).

## Fase 3 Contrato Hermes

Diseño ya, build del agente después. Hermes expone estos tools sobre los endpoints ya probados:

```json
{"tool": "pollinations.generate", "input": {"prompt": "texto", "model": "flux.1-schnell", "width": 1280, "height": 720, "seed": 7}}
{"tool": "pollinations.edit", "input": {"image": "binary", "instruction": "conserva torres, agrega cáscara + vidrio", "model": "flux.1-kontext-pro"}}
{"tool": "pollinations.async_poll", "input": {"job_id": "id", "hasta": "succeeded"}}
```

El workflow Eval queda como fallback manual con el mismo contrato.

## Fase 4 RunPod Comfy

Cuando el concurso pida geometría exacta o LoRA propio: F6–F8 del backlog (`30-backlog-futuras-pruebas.md`), Klein 4B destilado primero, Dev vía pod 24 GB. Pollinations cubre iteración; RunPod cubre control.

## Gates

- G0: credencial 200 + `poll: hola` devuelve foto con caption flux.
- G1: Q1–Q3 en activos + comparativa directo vs Telegram.
- G2: router + rama `img:` funcionando, T3–T9 registradas.
- G3: contrato Hermes validado contra tools reales.
- G4: primera corrida pod registrada.

## Costos

flux 0.002 (5 Pollen rinden ~2.500), z-image 0.004, klein 0.005, 1.1-pro y kontext 0.03, sana 0.0001, mai-flash 0.00001425 + tokens, sdxl-lightning-free 0. Gemini legacy fuera de la tanda por costo mayor.

## Riesgos

- Timeout en 2K: cubierto con 180 s + async.
- Cache repetida: seed fijo repite, timestamp varía.
- Webhook Telegram: pide workflow activo para recibir mensajes.
- Pod con costo de mantenimiento: entra solo en Fase 4, con gate de gasto previo.
