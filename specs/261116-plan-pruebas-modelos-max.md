---
tipo: spec
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [spec, plan, pruebas, modelos, limites, openrouter, pollinations, cloudflare, n8n]
idioma: es
---

# Plan de pruebas al límite por modelo (demo Formas, vía OpenRouter)

> Objetivo: explotar cada modelo al máximo para saber en qué es mejor y cablear el agente después. Sin generar todavía: primero el plan, las miniaturas caen en la ejecución. Modelos: GPT-image 2.6, NanoBanana 2.1/2.0, Seedream 5.0 Pro (+ Ideogram testigo).

## Ficha por modelo (qué es mejor + benchmark verificado + parámetros)

| Modelo (slug OR) | Mejor para | Benchmark verificado | Parámetros nativos (OR/Pollinations) |
|---|---|---|---|
| GPT-image 2.6 sunburst/flare (`openai/gpt-image-2.6-sunburst`) | Collage, textura, motion-blur, póster con texto, edición multi-turno con máscara | Arena T2I: 2.5 Sunburst 1424.6 top + texto 1466 (2.6 hereda familia) | refs, seed, aspecto; $8/M in + $30/M out |
| NanoBanana 2.1 (`google/gemini-nano-banana-2.1`) | Interiores fotorrealistas, iteración con base real | Arena 1327.8; VibeDex NBP archviz 4.62; grounding + 14 refs + SynthID | 14 refs, in/out imagen+texto, 1K/2K/4K; ~$0.039/img |
| NanoBanana 2.0 (`google/gemini-nano-banana-2.0`) | Alternativa interiores, reserva de 2.1 | familia NB (sin benchmark propio verificado) | generations+edits (paid_only); ~$0.03–0.05 |
| Seedream 5.0 Pro (`bytedance-seed/seedream-5-0-pro`) | Geometría, juicio contextual | 6/8 Rangy; $0.045 OR / $0.035 Pollinations | **14 refs**, seed, aspecto, 1K/2K |
| Ideogram v4 turbo (`ideogram-ai/ideogram-v4-turbo`) | Esquemas, formas simplificadas | veredicto demo Formas | $0.03 (Pollinations; OR no lista) |

Fuentes: [comparativa OR](https://openrouter.ai/compare/bytedance-seed/seedream-5-0-pro/google/gemini-3.1-flash-image/openai/gpt-image-2.5-sunburst) · [Seedream OR](https://openrouter.ai/bytedance-seed/seedream-5-0-pro) · benchmarks en [[wiki/glosario/software/modelos-imagen-arquitectura|modelos]].

## Batería común (misma base, compara modelos)

Base: captura TM + croquis Tigre. Cada test: prompt EN + contexto declarado + costo `usage.cost`.

| ID | Prueba al límite | Qué estresa | Miniatura |
|---|---|---|---|
| T1 | Fotorrealismo puro (TM→foto) | techo de calidad | ⏳ |
| T2 | Conserva+cambia 1 variable | obediencia vs invento | ⏳ |
| T3 | Multi-ref al máximo (2→6→14) | cuántas refs aguanta fiel | ⏳ |
| T4 | Texto exacto en imagen (`GAUDI NEXUS`, cartel obra) | tipografía | ⏳ |
| T5 | Resolución/aspecto (1:1→16:9→4K) | escalado, costo | ⏳ |
| T6 | Seed ×2 + guidance alta/baja | reproducibilidad | ⏳ |
| T7 | Máscara: cambiar solo un paño | control zonal | ⏳ |
| T8 | Grounding/búsqueda (solo NB) | contexto real | ⏳ |
| T9 | Croquis→render + plano→ref | lectura de dibujo | ⏳ |

## Por modelo: qué test lo exprime (plan de ejecución)

- **Seedream**: T3 (14 refs, geometría con 6→14), T1 (fotorrealismo), T5 (2K). Límite a buscar: ¿a cuántas refs pierde la geometría?
- **NB 2.1**: T8 (grounding), T2 (interiores fieles), T3 (14 refs), T7. Límite: wall-hung/invento en densos.
- **NB 2.0**: espejo de 2.1 (T1/T2) para decidir cuál queda.
- **GPT 2.6**: T4 (póster), T7 (máscara multi-turno), T2 (collage/textura), motion-blur. Límite: costo por llamada (medir `usage.cost`).
- **Ideogram**: T9 esquemas + T4 simple. Límite: ¿supera a scribble abierto?

## Vías y cableado n8n (después de la batería)

Una sola tool contra OpenRouter Images API rota el slug (Seedream/NB/GPT); Ideogram y grants vía Pollinations; CF como carril $0. Cada tool registra pedido → modelo → costo → veredicto (review loop del router).

## Conceptos relacionados

- [[wiki/glosario/software/formas-ai|formas-ai]] · [[wiki/glosario/software/capacidades-agente-imagenes|router]] · [[wiki/glosario/software/modelos-imagen-arquitectura|modelos]] · [[proyectos/MVP_09-workerFLUX/generaciones/INDICE-GENERACIONES|dashboard]]
