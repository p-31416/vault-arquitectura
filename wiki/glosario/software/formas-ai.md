---
tipo: software
software: formas-ai
categoria: analisis
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [glosario, software, formas-ai, orquestador, seedream, nanobanana, ideogram, gpt-image, agentes, hermes]
idioma: es
---

# Formas.ai — análisis para el estudio (demo 2026-11-15 + catálogo vivo 2026-11-16)

> AI Design Workspace para arquitectura y 3D (beta 3.5.0). Veredicto del estudio: **orquestador con gran UX, sin modelo propio**; sus habilidades se replican con acceso directo a los mismos motores + el agente del estudio. Deconstrucción flujo por flujo + video: [[wiki/glosario/software/formas-ai-flujos-clase|formas-ai-flujos-clase]].

## Qué es

Workspace IA-nativo: sketch→render fotorrealista (Freeform Studio), modelo 3D→visualización con contexto (3D Model Studio), imagen→3D, video (narrativas, timelapses), integración Trimble SketchUp, importación universal (Rhino 3DM, GLB/GLTF, OBJ, STL, PDF). Chat que orquesta modelos de terceros: **Gemini, Flux Kontext, LUMA, TRIPO, ChatGPT, Stability**. Usuarios visibles: BIG, MVRDV, Gensler, Arup, Columbia, AA, IAAC.

## Modelos vistos en la demo → acceso directo

| Demo Formas              | Modelo real                                        | Acceso directo (Pollinations, catálogo vivo) | Costo directo         | Veredicto demo                                  |
| ------------------------ | -------------------------------------------------- | -------------------------------------------- | --------------------- | ----------------------------------------------- |
| GPT 2.6 Unburst/Sunburst | `openai/gpt-image-2.6-sunburst` (+ variante flare) | `paid_only`, endpoints generations+edits     | ~$0.039/img           | Motion blur, collage, texturas desde imagen web |
| NanoBanana 2.1           | `google/gemini-nano-banana-2.1`                    | `paid_only` (ya probado por el estudio)      | ~$0.039/img           | Interiores (mejor en su clase)                  |
| NanoBanana 2.0           | `google/gemini-nano-banana-2.0`                    | `paid_only` (ya probado)                     | ~$0.03–0.05/img       | Interiores, alternativa a 2.1                   |
| C-Dream 5.0 Pro          | `bytedance/seedream-5.0-pro`                       | `paid_only`                                  | $0.035/img flat       | **Geometría** (mejor de la demo)                |
| Ideogram                 | `ideogram-ai/ideogram-v4-turbo/balanced/quality`   | `paid_only`                                  | $0.03 / $0.06 / $0.10 | Esquemas y formas simplificadas                 |

Los tres modelos a probar con acceso directo: **Seedream 5.0 Pro, GPT-image 2.6 (sunburst/flare), Ideogram v4**. Vía alternativa sin Paid Pollen: OpenRouter lista `google/gemini-nano-banana-2.1` (in imagen+texto → out imagen+texto, ~$0.03–0.05/img, usa el crédito existente del agente).

## Acceso directo verificado 2026-11-16 — OpenRouter Images API (vía única recomendada)

Hallazgo: OpenRouter expone [Images API](https://openrouter.ai/docs/guides/overview/multimodal/image-generation) (`POST /api/v1/images`, descubrimiento en `/api/v1/images/models`) con **una sola credencial y un solo patrón** para todos: `prompt` + `input_references` (hasta 14) + `seed` + `aspect_ratio` + `resolution` 1K/2K; responde `b64_json` + `usage.cost` (cargo exacto por llamada). [Comparativa oficial de los tres](https://openrouter.ai/compare/bytedance-seed/seedream-5-0-pro/google/gemini-3.1-flash-image/openai/gpt-image-2.5-sunburst) + [ficha Seedream 5.0 Pro](https://openrouter.ai/bytedance-seed/seedream-5-0-pro).

| Modelo                                                   | Rol (veredicto demo)           | Precio verificado                                                                              | Vía                                                                              |
| -------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Seedream 5.0 Pro** (`bytedance-seed/seedream-5-0-pro`) | Geometría                      | **desde $0.045/imagen**                                                                        | OpenRouter Images API o Pollinations $0.035 (Paid Pollen) → **integrar primero** |
| **NanoBanana 2.1** (`google/gemini-nano-banana-2.1`)     | Interiores                     | ~$0.039/img (1290 tok × $0.00003)                                                              | OpenRouter chat o Pollinations → **integrar segundo**                            |
| NanoBanana 2 (`google/gemini-3.1-flash-image`)           | Interiores (alternativa)       | $0.50/M in + $60/M out (~$0.08/img est.)                                                       | OpenRouter → reserva                                                             |
| **GPT-image 2.5/2.6 sunburst**                           | Collage, textura, motion-blur  | $8/M in + $30/M out (cara en texto; imagen a estimar por llamada) / Pollinations ~$0.039–0.055 | OpenRouter o Pollinations → **tercera** (solo textura/collage)                   |
| **Ideogram v4 turbo**                                    | Esquemas, formas simplificadas | $0.03 (turbo)                                                                                  | Pollinations (OpenRouter no la lista en su API) → barata, cuando toquen esquemas |

Orden de integración: Seedream (geometría, la que más duele) → NB 2.1 (interiores, ya probada) → GPT sunburst (textura) → Ideogram (esquemas). Una sola tool n8n contra OpenRouter Images API cubre las cuatro rotando el slug.

Plan de pruebas al límite (sin generar todavía): [[specs/261116-plan-pruebas-modelos-max|plan pruebas modelos max]] — ficha por modelo (mejor uso + benchmark + parámetros), batería común T1–T9 y qué test exprime cada uno, con columna de miniaturas ⏳ para la ejecución.

## Flujos que arma Formas (replicables)

Fórmula base: **modelo + prompt + imagen de referencia**. Componentes vistos:

1. **Site extraction**: foto/sitio → contexto para el render. Hecho por el estudio con Tigre; **pendiente probar con CABA**.
2. **Referencia externa 3D**: partir del propio modelado (quien modela, parte con ventaja). Probado por el estudio (Twinmotion→klein).
3. **Geometrías y máscaras**: control por zonas. Réplica prevista con **Kontext** (edits con máscara) vía el agente, pendiente de cablear.
4. **Textura desde imagen web**: piden una textura y la traen de Google. **Automatización propuesta**: el agente busca, extrae 3 opciones y las muestra; la elección sigue por texto, sin caza manual.
5. **Foto de contexto (Google Maps/Streets)**: viable para probar, con atención al encuadre legal de uso de esas imágenes.

## Habilidades a copiar al agente

1. Control dual materiales/estilo por prompt (precisión tipo Style Memory).
2. Memoria de estilo por proyecto (equivale a nuestro LoRA de proyecto).
3. Multi-ángulo consistente / Viewpoint (nuestro pendiente W4/H3).
4. Importar 3DM/GLB directo + imagen→3D (nuestro loop Trellis→Rhino).
5. Link con SketchUp (vía API/export cuando el estudio lo pida).

## Límites estructurales (por qué replicar en vez de suscribir)

- Suscripción + créditos por uso, costo por operación sin publicar (medible con los 500 créditos free); resultado no-determinista por diseño.
- Memoria entre sesiones acotada: la filosofía del estudio y sus decisiones viven en el vault, fuera de su alcance.
- Conexión con documentación del estudio ausente; **plantas en estado débil** (reconocido en la demo, en desarrollo por feedback).
- Automatizaciones tipo apps, sin agente nativo que despliegue subagentes.
- Curva de aprendizaje de herramienta nueva, fuera del sistema del estudio.

## Visión Hermes

Un humano despliega **un solo agente**, y ese agente despliega **subagentes** (site, textura, máscara, memoria de estilo, entrega). Formas resuelve el "antes y después" para un humano; el estudio lo integra al sistema: el agente n8n como herramienta de Hermes, con la memoria del vault como filosofía persistente.

## Precios Formas (verificado 2026-11-16)

Free 500 créditos iniciales (luego 50/mes) · Starter $19 (750) · Go $35 (1.500, full-res) · **Pro $69 (3.500 + Agent 2.0 + Style Memory + Viewpoint)** · Pro Plus $129 (7.000). Top-ups: 1.500/$39, 3.500/$79, 7.000/$149 (vencen a 3 meses).

## Conceptos relacionados

- [[specs/261112-plan-pruebas-rumbo-miercoles|plan rumbo al miércoles]] — hoja única para Emilia
- [[proyectos/MVP_09-workerFLUX/00-index|MVP_09-workerFLUX]] — pruebas del agente + dashboard
- [[wiki/glosario/software/capacidades-agente-imagenes|capacidades del agente]] — backlog fases 2–4
- [[specs/261112-adr-modelo-antes-que-flujo|ADR modelo-antes-que-flujo]] + [[specs/261112-bateria-worker-consistencia|batería consistencia]]

## Referencias

- [Formas.ai — home (Freeform, 3D Studio, modelos orquestados)](https://www.formas.ai/) (verificado 2026-11-16 — 200)
- [Formas.ai — Pricing (planes, créditos, top-ups)](https://www.formas.ai/pricing) (verificado 2026-11-16 — 200)
