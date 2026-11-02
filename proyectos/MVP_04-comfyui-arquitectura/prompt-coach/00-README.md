---
tipo: prompt
mvp: 04
carpeta: prompt-coach
origen: tablero Miro del curso AI x Gaudi (archademy.ai), seccion "PROMPT COACH SETUP"
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [mvp_04, comfyui, prompt, prompt-coach, curso-ai-gaudi, flux2, json]
idioma: es
---

# Prompt Coach del curso — archivo

> Los tres prompts de sistema que el curso entrega en el tablero de Miro, extraidos del export CSV `AI-course.csv` (seccion `MODULE 1 - INTRODUCTION`) y archivados verbatim para que `@tim` los use como fuente. Cada archivo conserva el texto original y marca con honestidad lo que el export no trajo.

## Los tres prompts

| # | Archivo | Que hace | Largo del original |
|---|---|---|---|
| 01 | [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/01-prompt-coach-simple\|Prompt Coach simple]] | Pregunta modelo + largo y deriva a la guia de cada modelo | 854 caracteres, completo |
| 02 | [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/02-prompt-coach-extendido\|Prompt Coach extendido]] | Dos modos (full-frame / inpaint) + playbooks por familia | 6.064 + 6.002 + 3.068 chars; **Branch A y B completos** (corte en la 3ª regla de Hard-won) |
| 03 | [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/03-flux2-prompt-refiner\|FLUX.2 Architectural Prompt Refiner]] | Tres concept cards con referente de autor + JSON de 10 claves | 6.859 caracteres, tablas vacias en el export |

## Como se relacionan con `@tim`

| Pieza del curso | Que toma `@tim` | Que agrega el estudio |
|---|---|---|
| Coach simple | la pregunta inicial: modelo y largo | tabla de decision con plataforma (local / RunPod / Cloud) |
| Coach extendido | el criterio de dialecto por familia | playbooks verificados contra docs oficiales |
| Refiner FLUX.2 | las constantes: Iwan Baan, Phase One IQ4, 6 hex, film stock, lens logic | esqueleto JSON del modulo 3 y el `STRICT CAMERA LOCK` |
| — | — | video: LTX-2.3, Kling 3.0, Seedance 2.0 |

## Estado de las fuentes

- **Coach simple:** completo. Sus links son la base del router del skill `comfy-prompting`.
- **Coach extendido:** ✅ completado (2026-10-30). Branch A y Branch B (inpaint region-only: mask checks, estructura de 6 pasos, skeleton, failure triage, nota de links) verbatim desde el export. Corte restante: 3ª regla de "Hard-won rules" (`- **M`) y el párrafo final de node settings para inpaint latente.
- **Refiner:** las tablas "JSON Template" y "Lens Selection Logic" quedaron vacias en el export. El template se recupera del esqueleto JSON del modulo 3 y del esquema oficial de BFL; la logica de lentes quedo reconstruida en `references/flux2.md`.
- **Link muerto:** el refiner apunta a `docs.bfl.ai/guides/prompting_guide_flux2_klein`, que hoy devuelve 404. La guia vigente es `https://docs.bfl.ai/guides/prompting_guide_flux2` y el overview `https://docs.bfl.ai/flux_2/flux2_overview`.

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|INSTRUCTION.md Rhino-to-Image]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|Esqueleto JSON del prompt]]
- [[proyectos/concurso-gaudi-nexus/flujos/flujo-02-text-to-image|flujo-02 — text to image]]
- [[wiki/glosario/interno/pbooks/pbk-comfy-agent|pbk-comfy-agent — playbook de @tim]]

## Referencias

- Tablero del curso — https://miro.com/app/board/uXjVHRM2XQU=/ (verificado 2026-10-20, requiere login)
- FLUX.2 prompting guide — https://docs.bfl.ai/guides/prompting_guide_flux2 (verificado 2026-10-30)
- FLUX.2 overview — https://docs.bfl.ai/flux_2/flux2_overview (verificado 2026-10-30)
