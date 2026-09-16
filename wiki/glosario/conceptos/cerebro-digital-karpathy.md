---
tipo: concepto
concepto: cerebro-digital-karpathy
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, karpathy, cerebro-digital, raw, software-2-0, zero-to-hero]
idioma: es
---

# Cerebro digital — Karpathy

> Técnica de *personal knowledge brain* de Andrej Karpathy extrapolada al vault: cada sesión bruta (`raw/sessions/` y `raw/research/`) se analiza para extraer **entidades**, **topics** y **hechos** que luego se promueven a conocimiento permanente.

- [[#Flujo]]
- [[#Método Zero to Hero y Software 2.0]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Flujo

1. **Raw** — `raw/sessions/YYYY-MM-DD-sesion-<slug>.md` (verbatim, qué se hizo + archivos modificados) y `raw/research/YYYY-MM-DD-<tema>.md` (research verificado @sherlock)
2. **Análisis** — sección `## Análisis cerebro digital (Karpathy)` con:
   - Topics candidatos a `wiki/glosario/software/` o `wiki/glosario/conceptos/`
   - Entidades (clientes, proyectos, herramientas, modelos; personas internas excluidas por regla)
   - Hechos/decisiones reutilizables vs. infra efímera
3. **Ingest** — promover a `wiki/` / `wiki/glosario/` con curaduría HITL (`¿Avanzo? s/N`).

## Método Zero to Hero y Software 2.0

Actualización 2026-09-09 desde research Karpathy (22 fuentes): Zero to Hero aporta el método de estudio del vault — construir desde cero en código (micrograd → makemore → GPT + Tokenizer) con syllabus público y repos reproducibles, patrón que el estudio traslada a ComfyUI / DirectML y scripts didácticos paralelos. Software 2.0 (código escrito por optimización) enmarca el vault computable: prompts, LoRAs y workflows como pesos versionables junto al Software 1.0 escrito por humanos. El gist `llm-wiki` consolida el pipeline *raw → compilado → query* con context windows largos. Ver referente [[wiki/glosario/referentes/andrej-karpathy|andrej-karpathy]].

## Conceptos relacionados

- [[wiki/glosario/referentes/andrej-karpathy|andrej-karpathy]]
- [[wiki/glosario/conceptos/sdd-spec_driven_development|sdd-spec_driven_development]]
- [[wiki/glosario/conceptos/vault-visual|vault-visual]]
- [[wiki/glosario/referentes/big-bjarke-ingels-group|big-bjarke-ingels-group]]

## Referencias

- Gist `llm-wiki` — patrón Karpathy: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (verificado 2026-09-07 — 200)
- Curso *Zero to Hero* (syllabus oficial): https://karpathy.ai/zero-to-hero.html (verificado 2026-09-09 — 200)
- Sitio personal Karpathy: https://karpathy.ai/ (verificado 2026-09-09 — 200)
- La wiki es tuya (vault-arquitectura): [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|Cierre de sesión]] (`raw/sessions/` cerebro-digital)
- Ejemplo canónico en este vault: [[raw/sessions/2026-09-07-sesion-unificacion-cuentas-proyectopi|sesión 2026-09-07 unificación cuentas]]
- Insumo research: [[raw/research/2026-09-09-karpathy-legado|research Karpathy 2026-09-09]]

> Este concepto avanza con Emilia (Lean, Design Thinking).
