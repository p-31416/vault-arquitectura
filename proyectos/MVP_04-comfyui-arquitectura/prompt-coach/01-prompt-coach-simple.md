---
tipo: prompt
mvp: 04
carpeta: prompt-coach
origen: tablero Miro del curso AI x Gaudi, seccion "PROMPT COACH SETUP"
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [mvp_04, comfyui, prompt-coach, sd15, sdxl, flux, video]
idioma: en
---

# Prompt Coach simple (verbatim)

> Es el que el video recomienda: dos preguntas y un link por modelo. Texto completo, sin cortes.

## Texto original

```text
You are an expert prompt coach. When the user inputs a prompt, ask the following questions to understand better their needs. 1. For which model is this prompt meant? 2. Do you want it to be a concise or long prompt?  Use the links below to understand which prompt guides you should access.  SD1.5 (Stable Diffusion 1.5): https://stable-diffusion-art.com/prompt-guide/  SDXL https://gist.github.com/lukecav/39431632378a63a7bc3860106943a96a  Flux.1  https://docs.bfl.ai/quick_start/introduction  Flux.2 https://docs.bfl.ai/quick_start/introduction https://docs.bfl.ai/guides/prompting_summary https://docs.bfl.ai/guides/prompting_unified_basics  LTX-2.3 Video model https://ltx.io/model/model-blog/ltx-2-3-prompt-guide  Kling 3.0 Video model https://kling.ai/quickstart/klingai-video-3-model-user-guide   Seedance 2.0 Video model https://seedance2.ai/guide
```

## Lectura critica

| Elemento | Observacion |
|---|---|
| Las dos preguntas | modelo y largo: son las unicas que el coach necesita para elegir dialecto |
| Link de SDXL | apunta a un gist de **vocabulario** (encuadres, lentes, luz, color), no a una guia de prompting de SDXL |
| Link de Flux.1 y Flux.2 | el mismo `quick_start/introduction` para los dos; la diferencia real esta en `prompting_summary` y `prompting_unified_basics` |
| Link de SD1.5 | `stable-diffusion-art.com/prompt-guide` es comunidad, no documentacion oficial |
| Cobertura | cubre imagen y video, pero no menciona JSON estructurado ni el caso inpaint |

## Como lo mejora `@tim`

1. La pregunta de modelo se responde con la tabla de decision del agente (necesidad → modelo → plataforma), no con una lista de links.
2. El largo se fija por variante: SD 1.5 30–60 palabras, SDXL 40–80, FLUX.2 klein 40–70.
3. El link de SDXL se reemplaza por el playbook interno; el gist se conserva como fuente de vocabulario.
4. Se agrega JSON como dialecto explicito de FLUX.2.

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/00-README|Prompt Coach del curso — archivo]]
- [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/02-prompt-coach-extendido|Prompt Coach extendido]]
- [[wiki/glosario/interno/pbooks/pbk-comfy-agent|pbk-comfy-agent]]

## Referencias

- Tablero del curso — https://miro.com/app/board/uXjVHRM2XQU=/ (verificado 2026-10-20)
- SD 1.5 prompt guide — https://stable-diffusion-art.com/prompt-guide/ (verificado 2026-10-30)
- Vocabulario SDXL — https://gist.github.com/lukecav/39431632378a63a7bc3860106943a96a (verificado 2026-10-30)
