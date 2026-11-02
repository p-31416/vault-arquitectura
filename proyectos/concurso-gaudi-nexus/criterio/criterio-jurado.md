---
tipo: criterio
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: borrador
tags: [concurso, gaudi-nexus, jurado, checklist, gaudi-nexus]
idioma: es
---

# Criterio del jurado — checklist de cierre de los workflows

> Este documento es el **criterio de aceptación** de los siete workflows: cada punto que salga del módulo 6 (Round Table, con Cas Esbach) se convierte en un check que el workflow tiene que satisfacer para pasar a v1.0.
>
> **Estado: borrador.** La fuente es la transcripción local del módulo 6, que está pendiente (ver [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-06-round-table|flujo-06]]). El esqueleto de abajo ya está en uso: cada ficha de flujo trae su sección "Checks contra el criterio del jurado", y esos checks son la primera versión de este checklist.

## De dónde sale la tesis

El módulo 7 ya deja expuesta la apertura de Cas Esbach, y con ella la tesis que este checklist operacionaliza:

> Entre copiar la apariencia y entender la lógica subyacente va a haber una brecha, y esa es la que hay que cerrar.

> No vamos a intentar reducir la esencia de Gaudí a un LoRA; vamos a encontrar la esencia de Gaudí en el workflow.

De ahí se derivan tres criterios que el estudio puede verificar en cada workflow:

| # | Criterio | Cómo se verifica en un workflow |
|---|----------|----------------------------------|
| C1 | **La lógica constructiva antes que la apariencia** | el grafo re-esculta la geometría con reglas (catenarias, aberturas parabólicas, columnas arbóreas, bóvedas de compresión) y la estética llega en un segundo paso |
| C2 | **La geometría es del equipo** | el LoRA y los modelos de referencia aplican material sobre la volumetría propia y la dejan en su sitio |
| C3 | **El método es parte de la entrega** | cada imagen entregable conserva su grafo, su prompt y su seed, de modo que el before/after se puede mostrar |

## Checks por módulo (primera versión, a confirmar con la transcripción)

| Módulo | Checks que el workflow tiene que satisfacer |
|--------|---------------------------------------------|
| 1 · base | misma seed → misma imagen · el prompt queda registrado en los metadatos · el grafo es reproducible |
| 2 · texto a imagen | una variable por corrida · la referencia de autor elegida queda documentada como decisión de proyecto · el resultado es evidencia, no punto de partida |
| 3 · rhino a imagen | la geometría es propia y el LoRA no la altera · el encuadre es un parámetro de proyecto (STRICT CAMERA LOCK) · el marcado en negro de los planos es una decisión documentada · la escala real sale de la cota |
| 4 · video | el edificio queda quieto y se mueve el entorno · el encuadre va a la altura de los ojos · el costo del clip queda registrado |
| 5 · 3D | geometría pura antes que estética (el AO como paso clave) · multiview para que el modelo no invente la parte de atrás · escala verificada contra cota |
| 6 · mesa redonda | el checklist maestro (este documento) |
| 7 · flujo Gaudí | el dial deja registro de cuánta lógica entra · el prompt del agente se lee antes de pegarlo · la estética es una elección de proyecto documentada · el encuadre en detalle de fachada |

## Qué falta

| Ítem | Estado |
|------|--------|
| Transcripción del módulo 6 | pendiente |
| Criterios que el jurado explicita de forma literal | pendiente |
| Si el jurado pondera el before/after en la lámina | pendiente (tensión abierta entre `261019` y `research:672`) |
| Cantidad de puntos del checklist final | 5 a 7 estimados |

## Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-06-round-table|Ficha del módulo 6]] · [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-07-gaudi-workflow|Ficha del módulo 7]] · [[proyectos/concurso-gaudi-nexus/workflows/00-index|Workflows del concurso]] · [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|Plan maestro]] · [[specs/261019-plan-concurso-gaudi-nexus-ia|Plan del concurso]]
