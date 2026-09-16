---
name: article-writing
description: "Redacción larga del estudio (memorias, informes, propuestas concurso, guías, portfolio) con voz propia, sin humo LLM. Se activa con redacta, memoria, informe, propuesta, portfolio, artículo. Usa brand-voice primero si hay VOICE PROFILE; nunca inventa datos."
---

# Article Writing — estudio de arquitectura

> Portado de `vault-lidia` (origen ECC). Acá produce: memorias descriptivas, informes de avance, propuestas de concurso, `proyectos/<cliente>-<proyecto>/documentacion/`, entradas `wiki/` maduras y `activos/marketing/` (texto; binarios por referencia).

## When to Activate
- `redacta`, `memoria`, `informe`, `propuesta`, `concurso`, `portfolio`, `artículo`, `guía`
- Pulir transcripción de reunión (Fathom/OBS) a documento entregable
- Unificar tono con `brand-voice` (correrlo primero si hay muestras)

## Core Rules
1. Abrir con lo concreto: obra, número, plano, render, decisión, foto — después explicar
2. Frases cortas salvo voz intencionalmente expansiva (memoria institucional)
3. Prueba antes que adjetivo (m2, norma, costo, plazo, material, orientación)
4. Nunca inventar hechos, clientes, superficies, normas ni premios
5. Todo dato plano/jurídico con peso legal (Ley 24.335, incumbencia, sello) se cita exacto

## Banned Patterns
- "En el cambiante panorama actual", "game-changer", "cutting-edge", "revolucionario"
- "he aquí por qué importa" como puente vacío
- Arco vulnerable falso, pregunta de cierre solo para engagement, relleno bio
- Verborrea IA que retrasa el dato

## Writing Process
1. Audiencia + propósito (cliente, jurado, municipalidad, interno) + dónde vive (proyecto/documentacion, wiki, specs, marketing)
2. Outline duro: 1 job por sección
3. Secciones abren con prueba/artefacto/conflicto/ejemplo
4. Expandir solo si la frase siguiente gana espacio; cortar plantilla/autobombo
5. Cierre con takeaways accionables, no recap blando

## Estructuras
### Memoria descriptiva
- qué se entrega, partido, programa/m2, sistema constructivo/materialidad, sustentabilidad, normativa cumplida, renders/planos referenciados (`activos/...`)
### Informe avance obra
- período, avance % por rubro, desvíos + causa, decisiones ADR, próximos pasos con fechas, fotos (`activos/proyectos/.../fotos/`)
### Propuesta concurso
- idea en 1 línea, implantación, programa, materialidad, viabilidad normativa/costo/plazo, equipo, entregables por fase

## Quality Gate
- Datos respaldados por fuentes provistas (planos, specs, ADRs, deep-research)
- Sin transiciones genéricas IA; voz = `VOICE PROFILE` o voz operador nítida
- Cada sección aporta algo nuevo; formato según medio (PDF vía pandoc si aplica)

## Origen
Portado de `P:\00-repos\pitau-tech\vault-lidia\.opencode\skills\article-writing\SKILL.md`.
