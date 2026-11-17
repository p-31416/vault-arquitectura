---
tipo: playbook
codigo: pbk-pi-imagenes
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-12
tags: [pbook, pi-imagenes, agente, n8n, pollinations, cloudflare, prompting, arquitectura]
idioma: es
---

# pbk-pi-imagenes — Playbook operativo del agente pi imágenes

> Manual de uso del agente de imágenes del estudio (primera clase, n8n): qué sabe hacer, cómo pedirle, recetario por tipología y ciclo de mejora. La definición viva está en el agente: https://n8n.pitau.tech/projects/pWOSkiVhnAWt5tSi/agents/FWGtRuylIqexTigj. El spec de construcción vive en [[specs/261103-spec-ajuste-pollinations-flux|spec agente]].

- [[#Qué hace]]
- [[#Capacidades verificadas]]
- [[#Cómo pedirle (manual de uso)]]
- [[#Recetario por tipología]]
- [[#Lentes y constantes]]
- [[#Ciclo de mejora]]
- [[#Vía Cloudflare (cuota diaria)]]
- [[#Checklist antes de publicar]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué hace

**pi imágenes** conversa (hoy por Preview, mañana Telegram) y genera o edita imágenes con Pollinations: interpreta el pedido en español, arma el prompt EN con el Prompt Coach, elige motor (flux schnell explorar / 1.1-pro lámina / z-image nítido / mai-flash texto / kontext edición), ejecuta el tool y devuelve imagen + caption (motor, costo, seed). Sin prefijos, sin copy-paste.

## Capacidades verificadas

| Capacidad | Estado | Evidencia |
|---|---|---|
| Elegir motor según pedido | OK | Test Gaudí: eligió schnell; test lámina: eligió 1.1-pro solo |
| Prompt EN con coach | OK | Estructura vista→cierre, prosa en positivo, sin JSON ni comillas |
| Declarar supuestos | OK | "Supuesto: toma aérea oblicua..." / "asumo edit, misma cámara" |
| Ofrecer siguiente paso | OK | Propone lámina, edits o regenerar al cerrar |
| Memoria de conversación | OK | Recuerda última imagen y supuestos dentro de la session |
| Editar con foto (kontext) | Tool lista, sin test en agente | Validada a mano vía API (vano + lamas) |
| Texto en imagen (mai-flash) | Tool pendiente | Probada a mano (`GAUDI NEXUS` legible) |
| NanoBanana | Descartada | `paid_only`: grants no la cubren; gate: Paid Pollen |
| Modelos con imagen de entrada | OK | GLM 5.3 Flash ve fotos y video |
| schnell vía Cloudflare | OK | txt2img `prompt`+`steps` (sin `seed`), JSON base64, 172.8 Neurons/1024² |
| klein-4b edit vía Cloudflare | OK | Multipart hasta 4 refs, steps fijo 4; respeta geometría a ojo |
| `editar_cf` (tool del agente) | OK | Sub-workflow IMG Editar CF: URL + instrucción → miniatura visible; test 2026-11-12 OK |

Límite conocido: dims y seed fijos por tool (la API rechaza strings); la variación sale del prompt. Loop con foto de Telegram pendiente de upload a URL.

## Cómo pedirle (manual de uso)

| Lo que pedís | Lo que recibís |
|---|---|
| `casa patio de adobe en el desierto al mediodía, vista aérea` | Exploración flux + caption + oferta de lámina/edits |
| `hacela lámina` / `versión final` | Re-generación 1.1-pro 1280x704 |
| `más luz / abrí un vano` sobre la última | Edit kontext conserva+cambia (1 variable) |
| `cartel que diga X` | mai-flash (tool pendiente, hoy lo resuelve con flux) |

Reglas que ya conoce: máximo 3 edits seguidos, después regenera; ante ambigüedad declara y actúa; caption siempre con motor y costo.

## Recetario por tipología

**Casa urbana entre medianeras (BA):** street-level view from across the narrow street, modern infill house between party walls, exposed board-formed concrete structure, warm wood slats and black steel details, ground floor set back with glass, Buenos Aires urban fabric facades both sides, overcast noon light, photorealistic architectural photography, 35mm.

**Cáscara catenaria (concurso):** ver skill `prompt-cascara-gaudi` — vista lejana + shell paramétrico + Sagrada al fondo + dorado.

**Interior:** eye-level, nervios filtrando luz, piso pulido reflejante, vista enmarcada al fondo, luz suave de mañana.

**Cartelería:** nombrar el texto entre comillas simples en el pedido; el agente usa mai-flash.

## Lentes y constantes

Vertical alta 24mm tilt-shift (corrige fuga); apaisado amplio 24-28mm; exterior medio 35mm (natural); detalle/material 50-85mm. Cierre: Phase One IQ4, Portra 400 (cálido) / Fuji Pro 400H (nublado elegante) / CineStill 800T (noche), foto por Iwan Baan.

## Ciclo de mejora

Cada corrida `call_agent` deja: prompt usado, tool elegido, URL, costo. Patrón de mejora: si elige mal motor → ajustar instructions; si el prompt falla → mover la regla a la skill; si falta motor → nuevo tool (mai-flash, nanobanana con Paid Pollen). Bitácora: este pbook + spec (sección build log).

## Estado de cuenta y límites reales (hallazgo 2026-11-03)

Tras ~20 imágenes de prueba en el día, la cuenta quedó sin grants: POST (`/v1/images/generations`, `/v1/images/edits`) devuelve 402, GET con key también 402, y anónimo 401 (IP throttled por volumen). El agente lo detectó solo, probó 3 motores y dejó el prompt armado. Lecciones: los grants diarios tienen techo real; el test BA quedó en espera de recarga (grant de mañana o x402 desde $0.01). `GET /image` con key funcionó todo el día hasta agotar saldo — es la ruta más barata.

## Mejoras pendientes (análisis)

1. **Pre-chequeo de saldo**: tool liviana `GET /account/key` antes de generar; si 402, el agente avisa sin gastar iteraciones.
2. **Seed variable**: hoy fijo en 7 por restricción de tipos (números fijos en el sub-workflow); exponer seed como input AI del workflow-tool para variar sin tocar código.
3. **Más motores**: agregar tools `z-image` y `mai-flash` con el mismo patrón sub-workflow (barato, sin $fromAi en URL).
4. **Edits con foto de Telegram**: falta upload a `media.pollinations.ai` para convertir el binario en URL pública; hoy kontext solo acepta URL pegada.
5. **NanoBanana**: gateado a Paid Pollen (toda la familia es `paid_only`).
6. **Telegram**: integración pendiente del ID del usuario (`allowedUsers`); sin eso el agente solo vive en Preview.
7. **Publicar**: draft validado, falta `s` explícito.

## Vía Cloudflare (cuota diaria)

Segunda mano del agente además de Pollinations: 10.000 Neurons/día gratis (resetea 00:00 UTC), sin tarjeta. Token `pi_img_02` (90 días, `.env`). Detalle técnico en [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]].

| Pedido | Motor | Costo medido |
|---|---|---|
| Exploración diaria (cáscara, casa patio) | schnell 1024² | ~172.8 Neurons (~58/día) |
| Edit con referencia (volumetría → render) | klein-4b, 1–4 refs multipart | ~cuota equivalente (~80/día) |
| Lámina final | Pollinations 1.1-pro (no Cloudflare) | 0.03 Pollen |

Reglas: schnell sin `seed` (el schema lo rechaza); klein steps fijo en 4; si Cloudflare da 403 revisar IP/expiración del token; si da rate-limit, volver a Pollinations con goteo.

## Checklist antes de publicar
- [ ] `validate_agent` sin errores
- [ ] `call_agent` con pedido genérico y de concurso, ambas URL válidas
- [ ] Telegram: `accessMode private` + `allowedUsers` con tu ID
- [ ] Publicar solo con `s`, conectar canal y mandar primera imagen real

## Conceptos relacionados

- [[wiki/glosario/software/pollinations|pollinations]]
- [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]]
- [[wiki/glosario/software/capacidades-agente-imagenes|capacidades + backlog del agente]]
- [[wiki/glosario/software/modelos-imagen-arquitectura|modelos-imagen-arquitectura]]
- [[wiki/glosario/referentes/black-forest-labs|black-forest-labs]]
- [[specs/261103-spec-ajuste-pollinations-flux|spec agente pi imágenes]]

## Referencias

- [n8n AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) (verificado 2026-11-03 — 200, Tools Agent desde v1.82)
- [n8n Telegram Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/) (verificado 2026-11-03 — 200, Download Images + restricción por chat/user)
- [Pollinations image models](https://gen.pollinations.ai/models) (verificado 2026-11-03 — 200, catálogo vivo con precios y `paid_only`)
