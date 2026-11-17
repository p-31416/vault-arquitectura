---
tipo: index
proyecto: MVP_09-workerFLUX
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-13
tags: [mvp, worker, cloudflare, flux, klein, pollinations, pruebas]
idioma: es
---

# MVP_09-workerFLUX — Generación de imagen vía APIs (sin GPU propia)

> Proyecto interno: explorar, medir y operar la generación de imagen por API (Cloudflare Workers AI + Pollinations) como mano rápida del estudio, sin GPU local. El cerebro sigue en el agente [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]].

- [[proyectos/MVP_09-workerFLUX/01-agente-pi-imagenes|01 Agente pi imágenes (n8n, definición operativa)]]
- [[proyectos/MVP_09-workerFLUX/generaciones/INDICE-GENERACIONES|Registro visual de generaciones]] — las ~50 pruebas con miniaturas, costos y veredictos (barrido + batería W + serie TM + NanoBanana).
- [[proyectos/MVP_09-workerFLUX/flujos/IMG-Generar-CF|IMG Generar CF]] · [[proyectos/MVP_09-workerFLUX/flujos/IMG-Editar-CF|IMG Editar CF]] — fichas de los sub-workflows.

## Vías operativas

| Vía | Modelos | Cuota | Ficha técnica |
|---|---|---|---|
| Cloudflare Workers AI | schnell txt2img, klein-4b txt2img+edit multi-ref | 10.000 Neurons/día, cuenta `pi_img_02` | [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]] |
| Pollinations | schnell, 1.1-pro, z-image, mai-flash, sana, kontext | Grants diarios + x402 | [[wiki/glosario/software/pollinations|pollinations]] |

## Trazabilidad

- Doctrina: [[specs/261112-adr-modelo-antes-que-flujo|modelo→hardware→flujo]] · Batería: [[specs/261112-bateria-worker-consistencia|batería consistencia]] · Miércoles: [[specs/261112-plan-pruebas-rumbo-miercoles|plan miércoles]] · Agente: [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]] · Capacidades: [[wiki/glosario/software/capacidades-agente-imagenes|capacidades]]
