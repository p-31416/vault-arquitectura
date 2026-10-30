---
tipo: indice
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [studio-os, guia-lectura, emilia, explicar-sistema]
idioma: es
---

# Guía de lectura — qué documento consultar para explicar Studio OS

> Para qué sirve: preparar una explicación del sistema sin leer los cuatro documentos completos (1.591 líneas). Acá está **qué leer según qué haya que explicar**, con la sección y la línea exacta de cada cosa.
> Los cuatro documentos viven en esta carpeta: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].

## 1 · Los cuatro documentos en una línea

| Documento | La pregunta que responde | Qué tiene | Líneas |
|---|---|---|---|
| [[proyectos/MVP_07-studio-os-sistema/VISION\|VISION]] | ¿qué es y para qué? | el problema · el recorrido del trabajo · el cuaderno digital · Hermes conceptual · el stack con sus alternativas · las decisiones de producto | 338 |
| [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA\|ESTRUCTURA]] | ¿dónde vive cada pieza y cómo se conecta? | los 4 nodos · el agente · cada integración · el contrato entre componentes · registro y grafo · seguridad y backup · puesta en marcha · 6 ADR | 380 |
| [[proyectos/MVP_07-studio-os-sistema/REQUISITOS\|REQUISITOS]] | ¿qué tiene que cumplir y cómo se mide? | alcance · actores · 13 casos · 20 RF · 15 RNF · 18 criterios de aceptación · gobernanza A-D · métricas · plan T0-T6 | 304 |
| [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES\|IMPLEMENTACION-HERMES]] | ¿con qué piezas reales de Hermes se arma? | las 5 piezas a configurar · 8 flujos · lo que Hermes no hace · hallazgos verificados · `config.yaml` · 15 referencias | 569 |

Regla de lectura: **VISION primero siempre**. Los otros tres se consultan por tema, no de corrido.

## 2 · Según qué haya que explicar

| Si hay que explicar… | Leer, en este orden | Tiempo |
|---|---|---|
| **El sistema en 10 minutos** (cliente, reunión corta) | [[proyectos/MVP_07-studio-os-sistema/VISION#1 · Qué es y por qué\|VISION §1]] (40) → [[proyectos/MVP_07-studio-os-sistema/VISION#2 · El recorrido del trabajo del estudio\|§2]] (82) → [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas\|§6.9]] (315) | 10 min |
| **Qué cambia en el día a día** del estudio | [[proyectos/MVP_07-studio-os-sistema/VISION#2 · El recorrido del trabajo del estudio\|VISION §2]] (82): tabla de 9 pasos, de "entra un cliente" a "entregas" | 5 min |
| **Qué es Hermes** y qué no hace | [[proyectos/MVP_07-studio-os-sistema/VISION#4 · Hermes, conceptualmente\|VISION §4]] (138) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#1. Resumen: qué resuelve Hermes sin escribir código\|IMPLEMENTACION §1]] (17) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#11. Lo que Hermes no hace (y sigue siendo nuestro)\|§11]] (435) | 10 min |
| **Dónde vive cada cosa** (infraestructura) | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#1 · Vista general\|ESTRUCTURA §1]] (45) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#2 · Dónde vive cada pieza\|§2]] (67) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3 · El agente\|§3]] (86) | 15 min |
| **Cómo se conectan AutoCAD, Rhino y ComfyUI** | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4 · Las integraciones, una por una\|ESTRUCTURA §4]] (134) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#5 · El contrato entre componentes\|§5]] (219) | 15 min |
| **El cuaderno digital** | [[proyectos/MVP_07-studio-os-sistema/VISION#3 · El cuaderno digital\|VISION §3]] (103) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#8 · El cuaderno digital: cómo se construye\|ESTRUCTURA §8]] (278) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#7. Flujo E — El cuaderno digital y los croquis\|IMPLEMENTACION §7]] (353) | 15 min |
| **Quién decide y qué puede tocar el agente** | [[proyectos/MVP_07-studio-os-sistema/VISION#6.6 Los niveles de riesgo (la regla de gobierno)\|VISION §6.6]] (289) → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo\|REQUISITOS §7]] (191) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#5. Flujo C — Seguridad, permisos y niveles A-D\|IMPLEMENTACION §5]] (259) | 20 min |
| **Qué se compromete y cómo se mide** | [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#4 · Requerimientos funcionales\|REQUISITOS §4]] (115) → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#6 · Criterios de aceptación\|§6]] (164) → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#9 · Métricas\|§9]] (226) | 20 min |
| **Plazos y en qué orden se construye** | [[proyectos/MVP_07-studio-os-sistema/VISION#6.7 El camino en tres tramos\|VISION §6.7]] (295) → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#11 · Plan de entrega\|REQUISITOS §11]] (268) | 10 min |
| **Qué se configura el día uno** | [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#2. Las cinco piezas que hay que configurar\|IMPLEMENTACION §2]] (38) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES\|IMPLEMENTACION §13]] (464) | 15 min |
| **Por qué un plano necesita trazabilidad** (Ley 24.335) | [[proyectos/MVP_07-studio-os-sistema/VISION#1.3 El problema\|VISION §1.3]] (58) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#6 · El registro central y el grafo\|ESTRUCTURA §6]] (246) → [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#6. Flujo D — Registro y trazabilidad\|IMPLEMENTACION §6]] (330) | 10 min |
| **Costos de nube y GPU** | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#10 · Decisiones técnicas\|ESTRUCTURA §10]] (344, ADR Runpod) → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#10 · Decisiones abiertas (con impacto y momento)\|REQUISITOS §10]] (250) | 10 min |

## 3 · El orden mínimo para leerlo todo

Una hora, y queda el sistema entero en la cabeza:

1. [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] completo (338 líneas, ~25 min).
2. [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#1 · Vista general|ESTRUCTURA §1]] a [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3 · El agente|§3]] (45-133, ~15 min): los 4 nodos, dónde vive cada pieza, el agente.
3. [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#6 · Criterios de aceptación|REQUISITOS §6]], [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo|§7]] y [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#11 · Plan de entrega|§11]] (164-225 y 268-292, ~10 min).
4. [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#1. Resumen: qué resuelve Hermes sin escribir código|IMPLEMENTACION §1]], [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#2. Las cinco piezas que hay que configurar|§2]] y [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#11. Lo que Hermes no hace (y sigue siendo nuestro)|§11]] (17-49 y 435-448, ~10 min).

Se puede saltear sin culpa: ESTRUCTURA §10 (los 6 ADR son para decidir, no para explicar), REQUISITOS §12 (trazabilidad) y IMPLEMENTACION §3 a §10 (los 8 flujos son manual de operación).

## 4 · Las preguntas que va a hacer Emilia, y dónde está la respuesta

| Pregunta | Respuesta corta | Dónde |
|---|---|---|
| ¿Esto me reemplaza? | No. Ejecuta lo repetitivo; el criterio y la aprobación quedan en el arquitecto | [[proyectos/MVP_07-studio-os-sistema/VISION#4.4 Qué NO hace (y no va a hacer)\|VISION §4.4]] (161) · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#8 · Qué automatiza el agente y qué hace la gente\|REQUISITOS §8]] (210) |
| ¿Tengo que aprender algo técnico? | No: se usa por Telegram, en castellano, como se le escribe a un colega | [[proyectos/MVP_07-studio-os-sistema/VISION#6.5 Cuándo Telegram y cuándo Discord\|VISION §6.5]] (283) |
| ¿Quién decide qué? | Tres niveles: el agente propone, la persona aprueba, nadie firma por otro | [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo\|REQUISITOS §7]] (191) |
| ¿Mis planos y mis clientes quedan en internet? | El vault y los datos viven en un servidor propio; la nube es excepción y con condiciones | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#7 · Seguridad, secretos, backup y acceso remoto\|ESTRUCTURA §7]] (264) |
| ¿Qué pasa si se equivoca? | Los comandos peligrosos piden aprobación; hay una lista negra que no se saltea ni con modo automático | [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#5.2 Aprobación de comandos peligrosos\|IMPLEMENTACION §5.2]] (272) |
| ¿Cuánto tarda en verse algo? | Tramo 1 (cimientos) primero: inventario, agente con memoria, primeras herramientas de lectura | [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#11 · Plan de entrega\|REQUISITOS §11]] (268) |
| ¿Cuánto cuesta? | La nube es la excepción; el resto corre en el servidor y en la PC del estudio | [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#10 · Decisiones abiertas (con impacto y momento)\|REQUISITOS §10]] (250) |

## 5 · Qué todavía no está escrito

- **ComfyUI y correo propio**: decididos el 30/10 (skill oficial de ComfyUI + nuestros scripts como respaldo; correo self-hosted en `hermes@agents.pitau.tech`). Faltan redactar los dos flujos en IMPLEMENTACION.
- **Skills opcionales**: relevadas, sin sección todavía.
- **Preguntas de producto abiertas**: [[proyectos/MVP_07-studio-os-sistema/VISION#6.8 Las preguntas abiertas (las de producto)\|VISION §6.8]] (305) — qué se automatiza primero, cómo se publica el cuaderno, qué pasa con las fotos de obra.
- **Decisiones de construcción abiertas**: [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#10 · Decisiones abiertas (con impacto y momento)\|REQUISITOS §10]] (250) — dónde vive el modelo, Tailscale vs alternativas, Rhino 8 vs 9, DPA de Runpod.

## 6 · Fuera de esta carpeta, pero a mano

- [[proyectos/STUDIO_OS-Emilia/00-index|STUDIO_OS-Emilia]] — el piloto: fases comerciales, entregables y documentación vigente.
- [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os|Plan Studio OS v0.1]] — arquitectura de sistemas y roadmap modular previo.
- `proyectos/STUDIO_OS-Emilia/Resumen_Propuesta_Emilia_Studio_OS.txt` — el resumen conceptual que ya leyó.
- [[specs/261013-plan-cierre-mes1-calculadora-emilia|Cierre del Mes 1 con números reales]] — horas, costos y calculadora; sirve para hablar de plata sin inventar.
- `raw/docs/plan-hermes.md` — el briefing técnico original (1.013 líneas); es la fuente, no la lectura.

---

**Si solo hay tiempo para una cosa**: [[proyectos/MVP_07-studio-os-sistema/VISION#1 · Qué es y por qué|VISION §1]] (40-80) y [[proyectos/MVP_07-studio-os-sistema/VISION#2 · El recorrido del trabajo del estudio|§2]] (82-101). Con esas dos secciones se explica el sistema completo en cinco minutos.
