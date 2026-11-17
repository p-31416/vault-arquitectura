---
tipo: software
software: software-libre-vs-pago
categoria: analisis
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [glosario, software, floss, licencias, open-weights, vps, aps, comercial]
idioma: es
---

# Software libre vs pago — ficha viva del estudio

> Qué es abierto (propiedad), qué es pago, dónde corre (VPS/nube/local) y cómo se integra. Regla: FLOSS-first (RF-24); licencias edu/NC fuera de producción (RNF-16). APS free tier = 300 min/mes por motor, independiente de cualquier licencia de escritorio.

## Modelos de imagen

| Modelo | Licencia | Comercial | VPS/pod | Nube API | Costo ref |
|---|---|---|---|---|---|
| klein 4B | Apache 2.0 | ✅ | pod | CF/Pollinations | grants–$0.005 |
| Z-Image-Turbo | Apache 2.0 | ✅ | pod/liviano | $0.005/MP (fal) | centavos |
| FLUX.3 Image Klein | Kommunity (<$5M) | ⚠️ con tope | pod (BF16 24 GB / INT8 8 GB) | BFL/Pollinations | $0.05/img |
| Qwen-Image-2.1 | research | ❌ (vía acuerdo) | pod 24 GB | — | mirar, no cliente |
| SDXL 1.0 | OpenRAIL | ✅ | local/pod | — | ecosistema legacy |
| Seedream / NB / GPT / Ideogram | API comercial | ✅ (plan pago) | — | OpenRouter/Pollinations/fal | $0.03–0.15/img |

## Software CAD/BIM/oficina

| Pieza | Licencia | Comercial | VPS | Nube | Local | Integración |
|---|---|---|---|---|---|---|
| ezdxf / ODA Converter / LibreCAD / QCAD CE | MIT/GPL/freeware | ✅ | ✅ CLI | — | ✅ | scripts + n8n |
| FreeCAD BIM / Bonsai / IfcOpenShell / IfcMCP | LGPL/GPL | ✅ | ✅ headless | — | ✅ | MCP directo |
| Blender | GPL | ✅ | headless | — | ✅ | MCP/scripts |
| AutoCAD completo | suscripción | ✅ pagando | ❌ | APS Automation | ✅ PC/COM | MCP PC o APS HTTP |
| AutoCAD edu | edu | ❌ producción | — | — | aprendizaje | — |
| Revit | suscripción | ✅ pagando | ❌ | APS + Revit MCP | ✅ PC | MCP/APS |
| Rhino + Hops/Compute | licencia | ✅ pagando | ❌ (Linux) | VM Windows | ✅ PC | Hops/MCP |
| Rhino reemplazo abierto | — | — | parcial (CadQuery) | — | — | hueco real |
| Hermes / n8n / vault / Postgres / Tailscale | MIT/propio/freemium | ✅ | ✅ | — | ✅ | núcleo |

## Guía de compra diferida (qué pagar y cuándo)

1. Ahora ($1–2): Paid Pollen (kontext/Seedream/NB/Ideogram) + OpenRouter credits existentes.
2. Por uso: tokens APS al agotar free tier; créditos fal (video/3D por segundos).
3. Excepción: pod GPU (LoRA ~$1–3, Trellis/sesión ~$0.44 + storage) — nunca suscripción fija antes de medir.
4. Nunca: licencias edu para producción; modelos NC para cliente; suscripciones que emulan lo abierto.

## Conceptos relacionados

- [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4 · Las integraciones, una por una|ESTRUCTURA §4]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS RF-24/RNF-16]] · [[wiki/glosario/software/modelos-imagen-arquitectura|modelos]] · [[wiki/glosario/software/formas-ai|formas-ai]]
