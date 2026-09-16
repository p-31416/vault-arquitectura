---
name: deep-research
description: "Investigación profunda multi-fuente con websearch/webfetch. Se activa con research, deep dive, investigar, estado del arte. Para normativa argentina, materiales, referentes (BIG, Foster, OMA, ZHA) y software. Entrega informe citado apto para wiki/glosario (Conceptos relacionados + Referencias verificadas sin 404)."
---

# Deep Research — estudio de arquitectura

> Portado de `vault-lidia` y adaptado: allá exigía MCPs firecrawl/exa; acá se usa `websearch` + `webfetch` disponibles en este vault. Todo hallazgo con valor permanente termina en `wiki/` con frontmatter y `[[wikilinks]]` (ver `AGENTS.md`).

## When to Activate

- Usuario dice `research`, `deep dive`, `investigar`, `estado del arte`
- Hay que ampliar `## Referencias` de una entrada `wiki/glosario/**` (obligatorio: oficial + ≥1 externa verificada)
- Normativa (Código Civil y Comercial, códigos edificación municipales, Ley 24.335, propiedad horizontal), materiales, costos obra ARG, software/BIM, referentes

## Workflow

### 1) Objetivo (1-2 preguntas)
- ¿Para decidir, aprender o escribir (memoria, spec, entrada wiki)?
- ¿Alcance: Argentina / CABA-municipal / internacional? ¿Profundidad?

### 2) Plan en 3-5 sub-preguntas
Ej. tema "fachadas ventiladas cerámicas en CABA":
- Sistema + normativa aplicable CABA
- Costos y proveedores ARG
- Referentes (qué estudios lo usan)
- Lecciones/patologías

### 3) Búsqueda multi-fuente
- `websearch` 2-3 variaciones por sub-pregunta, 15-30 fuentes únicas
- Priorizar: oficial/normativa/académica > estudios/referentes > blogs > foros
- Recencia: preferir últimos 12 meses salvo normativa vigente

### 4) Lectura profunda
- `webfetch` 3-5 URLs clave a markdown/texto. Si 404/error → descartar y reportar (regla vault: verificar enlaces antes de citar)

### 5) Síntesis con salida al vault
```markdown
# <Tema>: informe
*Fecha: YYYY-MM-DD | Fuentes: N | Confianza: Alta/Media/Baja*

## Resumen (3-5 líneas)
## 1. <Eje> (con citas inline)
## 2. <Eje>
## Decisiones para el estudio
## Fuentes (1 línea c/u)
## Metodología (queries, fuentes analizadas, gaps)
```

- Si va a `wiki/glosario/**`: cumplir UNICO `.md` por tool, índice interno `[[#...]]`, `## Conceptos relacionados` ≥2 wikilinks, `## Referencias` verificadas
- Si es decisión de obra/concurso/BIM/ComfyUI → proponer ADR (`architecture-decision-records`)
- Si es memoria/informe → pasar a `article-writing` con `brand-voice`

## Quality Rules
1. Toda afirmación con fuente. Sin fuente = marcar no verificado
2. Cruzar: 1 sola fuente = flag
3. Separar hecho vs inferencia/estimación
4. Gaps explícitos ("datos insuficientes")
5. Nunca inventar URLs, normas ni cifras

## Origen
Portado de `P:\00-repos\pitau-tech\vault-lidia\.opencode\skills\deep-research\SKILL.md` — adaptado de MCPs firecrawl/exa a `websearch/webfetch` y a schema `vault-arquitectura` (`AGENTS.md`).
