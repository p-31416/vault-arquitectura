---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, registro, postgres, trazabilidad, vault]
idioma: es
---

# ADR-2026-10-28-registro-hibrido-postgres-vault: El registro vive en Postgres y el vault en el texto

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

La trazabilidad de hoy está dispersa en tres formatos distintos: la metadata viaja **dentro del PNG** de cada render (`INDICE-RENDERS.json`), los informes de auditoría CAD viven como **JSON sueltos** en `raw/reports/`, y el método y las decisiones están en **markdown** del vault. `raw/docs/plan-hermes.md` §11 pide un registro central capaz de responder de qué archivo salió un resultado, con qué versión, con qué parámetros, quién lo aprobó y qué depende de qué. El VPS ya tiene Postgres 17 y Qdrant; el vault ya es un repo git privado.

## Decisión

Registro **híbrido**: en el VPS, schema `studio_os` de **Postgres** para lo vivo (proyecto, archivo, versión, tarea, ejecución, artefacto, relación, aprobación) con **escritor único** (API `registry`); en el **vault**, lo narrativo (método, ADRs, decisiones, bitácoras). Base relacional primero; el grafo se evalúa solo cuando exista un caso de uso que lo justifique.

## Alternativas

### Solo archivos en el vault (JSON/CSV versionados)
- Pros: cero infraestructura, versionado con el resto, coherente con el índice de renders que ya funciona.
- Contras: sin consultas entre dominios, sin concurrencia y sin transacciones: el "qué depende de esto" se responde grepando.

### Base de grafos
- Pros: modela el grafo de dependencias de forma natural.
- Contras: el briefing mismo lo pospone (§11:618) y hoy no hay un caso que lo justifique: relacional con tablas de relaciones alcanza.

### Solo Postgres (el vault como consumidor)
- Pros: una sola fuente consultable.
- Contras: el texto que ya existe (método, ADRs, decisiones) quedaría fuera y habría que duplicarlo en dos lugares.

## Consecuencias

### Positivas
- Una consulta responde lo que el norte exige: "de qué salió, con qué versión, quién lo aprobó, qué se desactualizó".
- El vault sigue siendo la memoria legible y versionada; Postgres agrega la capa de estado vivo, sin reemplazarlo.
- El registro habilita la detección de desactualizados: al registrar una versión nueva, el sistema marca los artefactos que dependen de la anterior.

### Negativas
- Un servicio más en el VPS (API `registry`) y un schema que mantener con su backup.
- El registro y el vault pueden desincronizarse si alguien edita el vault a mano.

### Riesgos + mitigación
- **Escrituras directas a la base**: se prohíbe; todo pasa por la API `registry`, que valida y deja traza de quién escribió qué.
- **Divergencia registro ↔ vault**: cada artefacto que referencia un archivo del vault guarda el hash de ese archivo; la sincronización se verifica.
- **Caída del registro**: las tareas que no pueden registrarse **no se ejecutan** (el registro es requisito previo, no un anexo).

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.6 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §2
- wiki: [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] · [[wiki/glosario/software/n8n|n8n]] (Postgres y Redis como contenedores del VPS)
- fuente: `raw/docs/plan-hermes.md` §11 y §15
