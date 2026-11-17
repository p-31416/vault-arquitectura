---
tipo: software
software: capacidades-agente-imagenes
categoria: catalogo
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [glosario, software, pi-imagenes, capacidades, roadmap, n8n, pollinations, cloudflare]
idioma: es
---

# Capacidades del agente pi imágenes + qué más se le puede agregar

> Catálogo vivo: lo que el agente hace hoy (verificado), lo que puede hacer con los proveedores actuales, y el backlog priorizado. El manual de uso diario vive en [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]].

- [[#Lo que hace hoy (verificado)]]
- [[#Operaciones posibles por proveedor]]
- [[#Operaciones locales gratis (nodo Edit Image)]]
- [[#Qué más se le puede agregar (backlog priorizado)]]
- [[#Lo que queda afuera (decisiones)]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Lo que hace hoy (verificado)
| Capacidad | Cómo | Estado |
|---|---|---|
| txt2img exploración | `generar_cf` → schnell Cloudflare 1024², ~173 Neurons | ✅ Test BA + pabellón, imagen visible en Preview |
| txt2img lámina | `generar_lamina` → 1.1-pro 1280x704, 0.03 Pollen | ✅ Test concurso |
| txt2img nítido/barato | `generar_explorar` → schnell/z-image Pollinations | ✅ Barrido 13 imgs |
| Edición conserva+cambia | `editar_imagen` → kontext-pro, 1 variable, máx 3 seguidas | ✅ Vano + lamas |
| Texto legible en imagen | mai-flash (vía Pollinations) | ✅ `GAUDI NEXUS` legible |
| Caption con motor+costo | Instructions +スキル | ✅ Todos los tests |
| Memoria de sesión | memory n8n | ✅ Recuerda última imagen |
| Prompting ES→EN | 2 skills (concurso + general) | ✅ Estructura vista→cierre |

## Router de modelos — el agente elige según el pedido (classifier)

Dos capas: **tabla de reglas** (el cerebro la consulta primero) + **criterio LLM** (si el pedido no encaja, GLM decide y registra por qué). Cada generación alimenta la columna rendimiento.

| Pedido | Modelo | Por qué | Costo verificado |
|---|---|---|---|
| Geometría, respetar plano, exterior TM | Seedream 5.0 Pro | mejor geometría (demo Formas) | $0.045 (OpenRouter) / $0.035 (Pollinations) |
| Interiores fotorrealistas | NanoBanana 2.1 | mejor interiores (demo + serie TM) | ~$0.039 |
| Textura, collage, motion-blur | GPT-image 2.6 sunburst | veredicto demo | $8/M in + $30/M out (medir `usage.cost` por llamada) |
| Esquemas, formas simplificadas | Ideogram v4 turbo | veredicto demo | $0.03 |
| Exploración barata / idea rápida | schnell / z-image / sana | costo ~0 | grants / CF |
| Texto legible en imagen | mai-flash 2.6 / GPT sunburst | `GAUDI NEXUS` legible probado | $0.02 / a medir |
| Lámina concurso | 1.1-pro | probado 1280x704 | 0.03 Pollen |

Novedad en catálogo 2026-11-16: existe `seedream-5-5` (sucesor de 5.0) — a evaluar antes de fijar el default de geometría.

## Ficha viva y auto-actualización

APIs verificadas 2026-11-16 (todas responden hoy): `GET /api/v1/images/models` (catálogo, 68 modelos) + `/images/models/{id}/endpoints` (precio por proveedor) + `GET /api/v1/auth/key` (401 sin key; con la credencial OpenRouter devuelve uso/límite = consumo medido). Diseño:

1. **Cron semanal n8n** `ficha-modelos-refresh`: lee catálogo + endpoints de los 6 modelos, compara precio/novedades contra esta ficha; si algo cambia (precio, modelo nuevo tipo seedream-5-5) avisa por Telegram y propone actualizar (con `s`).
2. **Medidor de gasto**: misma corrida consulta `/auth/key` → gasto acumulado OpenRouter; Pollinations vía balance de grants.
3. **Review loop**: cada tool registra pedido → modelo → `usage.cost` → veredicto; el veredicto ajusta la tabla router (para qué rinde cada uno, con evidencia del dashboard).

## Operaciones posibles por proveedor

**Cloudflare Workers AI** (cuota 10k Neurons/día, cuenta `pi_img_02`): schnell txt2img (verificado); **klein-4b txt2img + edición hasta 4 refs multipart** (verificado a mano, tool del agente pendiente = fase 2). Sin seed en schnell, steps fijo en klein. Sin video, sin upscale, sin TTS verificado.

**Pollinations** (SOLO grants gratis, límite diario a medir): schnell Exploration y modelos community. Todo lo pago (`paid_only`) va por OpenRouter, no por Paid Pollen (regla 16/11).

**OpenRouter** (crédito existente del agente): `google/gemini-nano-banana-2.1` (verificado 2026-11-13: in image+text → out image+text, ~$0.03–0.05/img) vía chat/completions con image_url. Sin credencial nueva: reutiliza la del agente (`OpenRouter account`).

Comparativa NB 2.1 (2026-11-13, catálogo vivo): Pollinations oficial ~$0.039/img (1290 tok × 0.00003) vs OpenRouter ~$0.03–0.05 → empate técnico; Pollinations gana por simplicidad (mismo patrón kontext). Otras vías: proxies community `vendouple/nano-banana-pro` $0.10 y `tomdacatto` $0.25 (**paid=False**: salen de grants, sin Paid Pollen — probado: pide balance ≥0.1, tenemos 0.0008) y API directa de Google.

**FLUX 3 sin pod**: Pollinations lista `black-forest-labs/flux-3-image-klein` y `flux-3-image` (full $0.05064/img, Paid Pollen); pesos abiertos `flux-3-image-klein-comfy` viables en pod 24 GB.

**BFL API directa** (a verificar, con costo): inpainting Fill, outpaint Expand, erase con máscara, blur-removal, bounding boxes (FLUX 3), LoRA propio servido (finetune_id). Todo pago por imagen, derechos comerciales incluidos.

## Operaciones locales gratis (nodo Edit Image)

Sin modelo ni costo, dentro de n8n o como paso de sub-workflow: resize, crop, rotate, blur, border, composite (montar 2 imágenes), draw, text (rótulos/tarjas), transparent, shear, multiStep, information. Sirven para: miniaturas (ya en uso), marcas de agua, comparativas lado a lado, recortes a formato lámina, texto de cartel provisorio.

## Qué más se le puede agregar (backlog priorizado)

**Fase 2 — edición y control (sin costo nuevo):**
1. Tool `editar_cf`: klein-4b multi-ref como sub-workflow (igual patrón que `generar_cf`): el agente edita con referencias sin gastar Pollen.
2. Seed control: exponer seed en `IMG Generar` (hoy fijo en 7) para series reproducibles.
3. Tamaños: 512 (rápido) / 1024 (default) / lámina 1280x704 como input del tool.
4. Comparativa lado a lado: sub-workflow composite (2 renders + caption) para decidir entre variantes.
5. Upscale: lane Real-ESRGAN local/Comfy o vía API paga para la lámina final.

**Fase 3 — entrega y robustez:**
6. Telegram: conectar canal (falta ID usuario + `s` + publish) = la entrega real de imágenes full-res.
7. Pre-chequeo de saldo/cuota: tool liviano antes de generar (Pollen balance / Neurons día).
8. Manejo de errores: reintento con fallback de proveedor (CF→Pollinations) cuando uno cae (como el 503 de hoy).
9. Galería de sesión: al cerrar, montaje de todas las variantes + prompts (trazabilidad concurso).
10. Edits con foto de Telegram: upload a URL pública (falta pieza) para kontext con foto real.

**Fase 4 — frontera (con costo o pod):**
11. Outpaint/expand e inpaint con máscara (BFL Fill/Expand o kontext).
12. Background removal (BFL Erase o BiRefNet en pod) para recortes de concurso.
13. Image→3D Trellis (pod 24 GB, GLB→Rhino) — documentado en plan miércoles.
14. FLUX 3 Image Klein vía API (bounding boxes, 10 refs) cuando se justifique el costo.
15. NanoBanana con Paid Pollen (grounding + 14 refs) — gateado a recarga.

## Lo que queda afuera (decisiones)

- Video: excluido hasta fin de año (decisión 2026-11-12).
- LoRA del curso en el agente: no se usa por ahora.
- SD1.5/Juggernaut/Lightning: descartados como base (solo RealVis baked en Comfy).
- Modelos `paid_only` sin recarga previa: el agente no los ofrece.

## Conceptos relacionados

- [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]] — manual de uso diario
- [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]] — vía Cloudflare en detalle
- [[wiki/glosario/software/pollinations|pollinations]] — vía Pollinations en detalle
- [[specs/261112-plan-pruebas-rumbo-miercoles|plan rumbo al miércoles]] — camino RealVis + Trellis
- [[specs/261112-adr-modelo-antes-que-flujo|ADR modelo-antes-que-flujo]] — doctrina

## Referencias

- [n8n Edit Image node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage/) (operaciones: resize/crop/blur/composite/text)
- [BFL docs — FLUX 3 Image Klein](https://docs.bfl.ai/flux_3/flux3_image_klein) (verificado 2026-11-12 — 200)
- [Cloudflare — Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) (verificado 2026-11-12 — 200)
