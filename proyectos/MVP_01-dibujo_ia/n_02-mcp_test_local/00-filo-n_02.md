---
tipo: manifiesto
nivel: n02
nombre: mcp_test_local
fecha_creacion: 2026-09-29
ultima_actualizacion: 2026-09-29
tags: [manifiesto, mcp, lenguaje-natural, hipotesis, autocad, n02]
idioma: es
---

# Manifiesto — Dibujo por lenguaje natural vía MCP

> `00-filo` responde **¿por qué?**. Es el level statement: el problema, la hipótesis en palabras del usuario y por qué esta línea del estudio merece un marco de medición formal.
>
> La letra menuda: la hipótesis original es del usuario y se transcribe textual. Todo lo demás de este documento es propuesta del asistente y queda abierto a revisión.

---

## 1 · El problema

El estudio dibuja en AutoCAD con comandos nativos. Cada geometría se traduce hoy en tres pasos: umbral de *picker*, teclado de parámetros, y verificación ocular del resultado. La intención conceptual — *un ambiente de 4×4 con un vano de 0.96* — existe en la cabeza del arquitecto y se pierde en la traducción a coordenadas.

Ese costo es invisible en un proyecto grande y muy visible en una etapa específica: **el primer trazo**. La versión que se descarta —el boceto, la prueba de proporción, el esquema de circulación— es exactamente la que más geste se paga en AutoCAD, porque nadie la justifica con horas de producción.

## 2 · La hipótesis

> *"Por medio de lenguaje natural podemos manejar a AutoCAD via LLM para dibujar un plan de arquitectura e ir completándolo."*
> — formulada por el usuario, 2026-09-29

Es una hipótesis fecunda y es una hipótesis vaga, y en este proyecto la vaguedad es el objeto de trabajo, no un defecto de redacción. Tiene tres vaguedades que el nivel se ocupa de volver precisas:

| Vagueza | Pregunta que hay que responder |
|---|---|
| **¿Qué** se dibuja? | ¿Un rectángulo? ¿Un local? ¿Un proyecto? La respuesta cambia la complejidad geométrica en varios órdenes de magnitud |
| **¿Cómo se mide** que salió bien? | Un dibujo correcto a ojo puede tener 40 mm de error. El criterio de acierto necesita ser un número, no una impresión |
| **¿Qué pasa cuando se dibuja por partes?** | La parte *ir completándolo* es la más difícil y la única que puede fallar de forma silenciosa: cada paso parece bien y el resultado acumulado no |

La tercera es la que más importa, y es la que ninguna herramienta comercial mide.

## 3 · Por qué importa para el estudio

**Velocidad en la etapa exploratoria.** Automatizar el primer trazo libera al arquitecto de la mecánica del comando y le devuelve el juicio sobre la forma.

**Trazabilidad en texto legible.** Un prompt es un documento. *"El ambiente pasó de 4×4 a 5.2×3.6 porque el pasillo quedó corto"* queda escrito, fechada y atribuida a una decisión, en lugar de quedar en la memoria de quien dibujó.

**Continuidad de escala.** La hipótesis es que el mismo instrumento sirve para un muro, para un local y para un proyecto completo. Si se sostiene, desaparece el salto de escalón entre boceto y plano.

**Costo marginal de la corrección.** En un sistema que dibuja rápido, errar cuesta menos. Este es un argumento real a favor de la herramienta, siempre que el costo de *verificar* se mida junto con el costo de *dibujar*.

## 4 · Por qué esta línea exige método y no entusiasmo

Dos razones, y la segunda es la que manda.

**Razón epistemológica.** Es la única línea del framework donde la respuesta fácil — *obvio que funciona* — es peligrosa. Una herramienta que a veces acierta y a veces no, sin que sepamos cuándo, es peor que no tenerla, porque la confianza se calibra mal. *justamnete de esto está hablando brais moure en su curso de desarrollo con IA, en los ultimos meses la confianz bajo del 30% porque usan mal la IA*

**Razón legal.** En Argentina el plano es un instrumento contractual y registral (Ley 24.335 de Ordenamiento Territorial y Uso del Suelo y su reglamentación). Un desvío de 15 mm en una medianera es un conflicto de obra, no un detalle gráfico. Los resultados de este nivel son **material de trabajo** y llegan al documento contractual a través de una compuerta de verificación humana firmada. *el plano es documento y lenguaje universal entre arquitectos*

De ahí sale la regla que gobierna todo el nivel:

> **Cada corrida de este nivel se registra. Un resultado que no se midió no cuenta como evidencia, y un acierto que no se registró no se puede citar después.**

## 5 · El instrumento

```
Intención (ES)
     │
     ▼
    LLM ──── el operador: interpreta, decide, corrige
     │
     ▼
    MCP ──── el transporte: API, sin criterio
     │
     ▼
  AutoCAD ── el taller: geometría real, con unidades reales
     │
     ▼
    DWG
     ▲
     │
  Verificación humana ── quién firma, quién relee, quién se hace cargo
```

La analogía es de un laboratorio de instrumentación: el LLM es un operador con criterio propio, el MCP es el cable, y AutoCAD es el aparato. Un operador introduce error. Antes de confiarle un resultado hay que **caracterizar el error del instrumento**, que es literalmente el primer experimento de este nivel.

## 6 · Alcance de esta línea

**Cubre**: geometría métrica verificable en model space — polilíneas, líneas, arcos, rectángulos, capas, medidas, coordenadas.

**Queda para el siguiente ciclo**: cotas, rebajes de nivel, incumbencias normativas, coherencia entre capas BIM y parámetros, y firma profesional. Cada uno de estos requiere juicio profesional y trazabilidad contractual, y ninguno se resuelve con una polilínea correcta.

## 7 · Lo que este nivel no promete

En positivo, porque así se lee mejor:

- Promete **medir** antes de concluir. Si la hipótesis se sostiene, va a sostenerse con números, no con demostraciones.
- Promete **registrar los fallos** con el mismo detalle que los aciertos. Un nivel con bitácora de solo aciertos no sirve para decidir.
- Promete **degradar con elegancia**: si MCP y lenguaje natural no resultan superiores al comando nativo, esa información es un resultado valioso y cierra la línea con dignity.

## 8 · Contexto y referencias

- Nivel previo: [[proyectos/MVP_01-dibujo_ia/n_01-local/01-spec-n_01|n_01-local]] — geometría del local y comando `LOC` en AutoLISP
- Marco del framework: [[proyectos/MVP_01-dibujo_ia/00-filo-mvp_01|00-filo-mvp_01]] — por qué existe el framework de dibujo asistido por IA
- Guía de navegación: [[proyectos/MVP_01-dibujo_ia/readme-mvp_01|readme-mvp_01]]
- Instrumentación experimental: [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/01-spec-n_02|01-spec-n_02]] (hipótesis operacionalizada, variables, criterios)
- Procedimiento y métricas: [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/02-ft-n_02|02-ft-n_02]]
- Bitácora de corridas: [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/03-log-n_02|03-log-n_02]]

---

## 9 · Trazabilidad de este documento

| Fecha | Qué cambió | Quién |
|---|---|---|
| 2026-09-29 | Creación. Hipótesis transcrita del usuario. Nombre del nivel `n_02-mcp_test_local` | asistente |

> **BORRADOR** — `00-filo` es documento del usuario. Este texto es propuesta del asistente a la espera de revisión.
