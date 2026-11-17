---
tipo: spec
agente: pi-imagenes
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp09, agente, n8n, pi-imagenes, tools, primera-clase]
idioma: es
---

# Agente pi imágenes (n8n, primera clase)

> Definición operativa del agente. Playbook de uso diario: [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]]. Capacidades: [[wiki/glosario/software/capacidades-agente-imagenes|capacidades]].

- **URL**: https://n8n.pitau.tech/projects/pWOSkiVhnAWt5tSi/agents/FWGtRuylIqexTigj
- **ID**: `FWGtRuylIqexTigj` · Proyecto `pWOSkiVhnAWt5tSi` · Estado: **draft validado, sin publicar**
- **Cerebro**: `openrouter/z-ai/glm-5.3-flash` · Memoria n8n ON · Budget USD 1/mes (alerta 50%)
- **Integraciones**: ninguna conectada (Telegram pendiente de ID + `s` + publish)

## Tools

| # | Tool | Tipo | Qué hace |
|---|---|---|---|
| 0 | `generar_explorar` | workflow → IMG Generar | txt2img Pollinations schnell/z-image, 1280x720, seed 7 fijo |
| 1 | `generar_lamina` | workflow → IMG Generar | txt2img Pollinations 1.1-pro, 1280x704 |
| 2 | `editar_imagen` | nodo HTTP → Pollinations `/v1/images/edits` (cred `ppi-Pollinations(sk-)`) | kontext-pro conserva+cambia, 1 variable |
| 3 | `generar_cf` | workflow → IMG Generar CF | schnell Cloudflare 1024², devuelve miniatura visible |
| 4 | `editar_cf` | workflow → IMG Editar CF | klein-4b multipart 1 ref, devuelve miniatura visible |

IDs: IMG Generar `voMAYlv6d280QjSW` · IMG Generar CF `z0qOpgY5HT1kXoUL` · IMG Editar CF `oNRtmK7lSesgx3cQ`. Credenciales: `ppi-Pollinations(sk-)` (`zygMsDWvgbNf1Fwg`), `cf-WorkersAI` (`cLUDLsbsbLF7fj5F`, token `pi_img_02`, 90 días, sin filtro IP).

## Skills

- `prompt-cascara-gaudi` — base cáscara concurso + lentes + conserva+cambia (solo concurso/Sagrada).
- `prompting-arquitectura` — guía general vista→cierre + particularidades por motor.

## Historial de corridas (tests)

| Fecha | Pedido | Tool elegido | Resultado |
|---|---|---|---|
| 2026-11-12 | Cabaña genérica + exploración Gaudí | generar_explorar | OK |
| 2026-11-12 | Casa BA medianeras | generar_cf | OK, caption con Neurons |
| 2026-11-12 | Pabellón jardín | generar_cf (sub-workflow) | OK, imagen embebida en Preview |
| 2026-11-12 | Editar placeholder → pabellón | editar_cf | OK, imagen embebida + caption |

## Pendiente

- [ ] Telegram: ID usuario → `allowedUsers` → `s` → publish → primera imagen real por canal
- [ ] klein 9B: reintentar cuando Workers AI lo estabilice (error 3043 el 2026-11-12)
- [ ] Seed/tamaños como inputs AI (hoy fijos)
