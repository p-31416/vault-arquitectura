---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: Precedentes — estudios que publicaron LoRAs de estilo con su marca
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: borrador-activo
tags: [concurso, gaudi-nexus, lora, precedentes, licencia, model-card, civitai, huggingface]
idioma: es
---

# Precedentes — estudios que publicaron LoRAs de estilo con su marca

> Responde a [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §6 pregunta 4. Investigación 2026-11-02, 3 precedentes verificados vía `webfetch` (sin 404). Lección madre: la licencia la hereda la base; el model card se redacta con qué es + base + trigger + strength + workflow + ejemplos con metadata.

## 1. Nire Haus — Artchitecture (el precedente estudio más cercano)

- **Qué es:** LoRA entrenado por el estudio creativo Nire Haus para renders exteriores con toque pictórico, para concursos y portfolios.
- **Base:** Flux.1-dev. **Licencia aplicada:** FLUX.1 [dev] Non-Commercial (heredada, figura en la ficha).
- **Tamaño/entrenamiento:** 164 MB, 1000 steps / 33 epochs.
- **Trigger:** `artchitecture`. **Strength:** 0.8–1.0 fuerte, 0.5–0.7 sutil.
- **Cómo redactaron el model card:** 1 frase qué es + quién lo entrenó, para qué sirve (exteriores, residencial, urbano grande), trigger + strength por rangos + compatibilidad + formato SafeTensor. 6–9 imágenes de ejemplo con prompts visibles.
- **Lección para nosotros:** estructura a copiar tal cual; si publicamos sobre klein 9B o dev, el artefacto queda Non-Commercial aunque queramos Apache.

## 2. mnml.ai (mshakour) — flux-arch-realism-lora v2.0 (estudio con funnel comercial)

- **Qué es:** LoRA que vuelve fotorrealista la visualización exterior: texturas, luz, materiales.
- **Base:** Flux.1-dev. **Licencia aplicada:** Non-Commercial en Civitai; en HuggingFace figura `apache-2.0` (discrepancia a auditar antes de citar como ejemplo comercial — para nosotros rige la de la base).
- **Trigger:** `ARCHVIZ` opcional. **Strength:** 0.3–0.8 (más bajo que Nire Haus). Steps 30–50, guidance 3.5.
- **Cómo redactaron el model card:** qué mejora (3 bullets), settings recomendados, trigger, **link a workflow ComfyUI JSON en el repo** + "úsalo online sin código en mnml.ai" (funnel a su producto).
- **Lección para nosotros:** publicar JSON del workflow junto al LoRA + enlace al estudio; trigger corto en mayúsculas funciona como marca (`ARCHVIZ` → nuestro `gaudinexusstyle`).

## 3. MSCHbilly — Arch Soul Portrait v4.0 (autor individual, licencia permisiva)

- **Qué es:** retrato arquitectónico conceptual (perfil humano + fachada), estilo cinematográfico duotono.
- **Base:** ZImageTurbo. **Licencia aplicada:** Apache 2.0 (la base lo permite, y el autor la declara).
- **Entrenamiento:** 3000 steps / 32 epochs, 162 MB. **Trigger:** `arch_soul_portrait`. **Weight:** 0.7–1.0.
- **Cómo redactaron el model card:** serie versionada (v4 madurez del estilo), características del estilo en bullets, tips de prompt ("inside head", "clean gradient background"), trigger inalterado entre versiones.
- **Lección para nosotros:** versionar estilo (`...-v01 → v02`), fijar trigger desde v01 y no cambiarlo, documentar strength por efecto.

## Tabla comparativa

| Estudio/autor | Base | Licencia publicada | Trigger | Strength | Steps | Card incluye |
|---|---|---|---|---|---|---|
| Nire Haus | Flux.1-dev | Non-Commercial | `artchitecture` | 0.5–1.0 | 1000 | qué + base + trigger + strength + ejemplos |
| mnml.ai | Flux.1-dev | Non-Commercial / apache-2.0 en HF | `ARCHVIZ` | 0.3–0.8 | — | settings + JSON workflow + funnel web |
| MSCHbilly | ZImageTurbo | Apache 2.0 | `arch_soul_portrait` | 0.7–1.0 | 3000 | versión + bullets estilo + tips prompt |

## Decisiones para nuestro LoRA

1. Si queremos Apache 2.0 de punta a punta, entrenar sobre klein 4B Base (Apache 2.0), no sobre 9B ni dev — los 2 precedentes sobre dev quedaron Non-Commercial.
2. Model card a copiar: qué es (estilo visual del estudio) + base + trigger `gaudinexusstyle` + strength 0.6–1.0 + 6–8 ejemplos con metadata + link workflow JSON + link estudio.
3. Fijar trigger en v01 y no moverlo; versionar `concurso-gaudi-nexus-style-v01 → v02`.

## Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] — plan madre (§6.4)
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos-recomendados]] — regla ✅ solo comercial verificado
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — LoRA del curso

## Referencias verificadas (2026-11-02, sin 404)

- Ficha Nire Haus (verificada vía webfetch): `https://civitai.com/models/986640/artchitecture-where-art-meets-architecture`
- Ficha mnml.ai Civitai: `https://civitai.com/models/709956/flux-arch-realism-lora`
- Model card mnml.ai HF (verificada vía webfetch, licencia apache-2.0 en página): `https://huggingface.co/mnml-ai/flux-arch-realism-lora`
- Ficha Arch Soul (licencia Apache 2.0 + trigger): `https://civitai.com/models/2514683/arch-soul-portrait-architectural-human-lora-v4`
- Guía licencias Flux (klein 4B Apache vs 9B/dev Non-Commercial): `https://iimagined.ai/blog/train-flux-lora`

---
*Más nuevo → más arriba. Log: 2026-11-02 creación desde pedido Sol + research multi-fuente.*
