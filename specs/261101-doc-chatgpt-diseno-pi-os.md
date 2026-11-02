---
tipo: metodologia
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [studio-os, pi, diseño-sistema, hermes, chatgpt, visión, estructura, requisitos, mvp_07]
idioma: es
---

# Diseño de PI — análisis estructurado de la conversación «Diseño del sistema operativo»

> **Fuente**: la conversación íntegra vive en [[raw/reuniones/2026-11-01-chatgpt-diseno-sistema-operativo-pi|raw/reuniones — transcripción cruda]] (share canónico: `chatgpt.com/share/6ae73f14-62ac-83ea-89c9-0243b2ba5dc1`).
> **Relación con el vault**: este documento organiza lo que la conversación propone en **visión / estructura / requisitos / variantes**, y cruza cada punto contra lo ya decidido en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]], [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] y [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]. Donde el ChatGPT adelanta algo que el vault ya decidió distinto, se marca ⚠ y gana la decisión del vault.

## Índice

- [[#1 · Visión — qué es PI]]
- [[#2 · Estructura — cómo está armado]]
- [[#3 · Requisitos — la demo y las reglas]]
- [[#4 · Variantes y opciones predilectas]]
- [[#5 · Ideas nuevas que el vault todavía no tenía]]
- [[#6 · Frases y narrativa para reutilizar]]
- [[#7 · Pendientes que abren hacia MVP_07]]

---

# 1 · Visión — qué es PI

## 1.1 La tesis central

La conversación llega a una definición en cinco capas que conviene tener como norte:

> **PI · Architectural Operating System — un sistema operativo de capacidades para arquitectura.** Un entorno que integra agentes, herramientas de diseño, modelos computacionales, conocimiento técnico y automatizaciones para transformar procedimientos profesionales en capacidades persistentes, reutilizables y escalables.

El principio de fondo:

> El conocimiento humano se transforma en capacidad operativa. La capacidad se convierte en infraestructura. La infraestructura permite multiplicar la producción **sin multiplicar proporcionalmente las horas humanas**.

## 1.2 El problema de partida: la hora humana

El modelo de trabajo actual se organiza alrededor de `Trabajo = Personas × Horas`:

- El arquitecto operaba **cada herramienta** manualmente (ida y vuelta con la computadora: pide render, recibe render, cambia a mano, vuelve a pedir).
- La fórmula de velocidad que propone la propia Sol: velocidad de resolución `V_r = (K_a × E) / T`, donde el conocimiento acumulado (`K_a`) y la experiencia (`E`) son lo que hace más efectiva la tarea — pero el tiempo disponible sigue siendo la limitación dura.
- La IA y el trabajo paralelo con agentes rompen ese cálculo: **el recurso escaso deja de ser la capacidad de ejecución y pasa a ser la capacidad de dirección, validación y decisión**.

El ChatGPT propone tres fórmulas en lugar de una:

| Dimensión | Qué mide | Fórmula propuesta |
|---|---|---|
| A. Tiempo humano | minutos de atención efectiva del arquitecto | — |
| B. Tiempo de ejecución | cuánto tarda la infraestructura | — |
| C. Trabajo concurrente | tareas que avanzan mientras el humano hace otra cosa | `P = W_v / T_h` (trabajo útil *validado* sobre intervención humana) |

Registro mínimo que exige el modelo (para que la productividad paralela sea demostrable y no marketing): tiempo transcurrido, tiempo efectivo de ejecución, intervención humana, tiempo de espera, resultado producido, resultado aprobado.

## 1.3 Las tres dimensiones de PI

La conversación termina definiendo PI con tres lecturas separables:

1. **PI como sistema operativo**: la infraestructura que hace funcionar todo.
2. **PI como fábrica de capacidades**: el mecanismo para investigar, crear, validar, versionar y distribuir skills nuevas.
3. **PI como sistema de conocimiento**: la memoria que conserva el trabajo acumulado y lo hace evolucionar.

El estudio de arquitectura es una *instancia* de implementación; cada estudio configura su propia infraestructura de inteligencia sobre el mismo sistema.

## 1.4 El cambio de paradigma (los hombres palito)

- **Modelo tradicional**: humano ↔ computadora. La máquina amplifica la capacidad de *ejecución* del humano; cada tarea requiere una intervención y una respuesta.
- **Modelo agéntico**: humano + sistema de agentes. El humano diseña un sistema que amplifica su capacidad de *decisión*; los agentes especializados (Rhino, CAD, Visual, Docs) usan tanto la computadora como la nube, y el resultado vuelve como entregable + conocimiento acumulado.

Frase que encapsula la diferencia con el material del concurso (prompt coach): *"la diferencia entre utilizar inteligencia artificial y trabajar con una infraestructura de inteligencia artificial es que, en el segundo caso, el usuario deja de operar cada herramienta y comienza a administrar capacidades."*

---

# 2 · Estructura — cómo está armado

## 2.1 La unidad no es el agente: es la capacidad

La idea estructural más importante de la conversación. Un agente (ej. Pipi Rhino) tiene **capacidades** que pueden reutilizar los demás agentes; la capacidad tiene vida independiente del agente que la ejecuta:

| Concepto | Función | Ejemplo (el dibujo de Sol: un rinoceronte con manitos) |
|---|---|---|
| **Agente** | quién ejecuta | el rinoceronte que maneja Rhino y AutoCAD |
| **Skill** | qué sabe hacer | el camino mapeado una vez a mano y repetido: ubicación → Google Maps abierto → extraer 3D → lámina → viewport → cortes → rótulo |
| **Herramienta** | con qué lo hace | cada línea que se cuelga de la manito: internet, un video aprendido y transcripción guardada con su link |
| **Workflow** | en qué secuencia combina capacidades | el flujo de ComfyUI convertido en metadatos reproducibles |
| **Conocimiento** | de dónde aprendió y cómo se valida | procedencia de cada fuente (video ≠ docs oficial ≠ prueba propia) y criterios de verificación |

## 2.2 Las capas del sistema (arquitectura final de la conversación)

```text
┌────────────────────────────────────────────────────────────────┐
│ PI · Arquitectura de inteligencia — interfaz única             │
│ Web · Telegram · Chat · Panel de proyectos                     │
└──────────────┬─────────────────────────────────────────────────┘
               ▼
┌────────────────────────────────────────────────────────────────┐
│ Capa de agentes — Hermes                                        │
│ Pipi CAD · Pipi Rhino · Pipi Visual · Pipi BIM · Pipi Docs ·    │
│ Pipi PM (coordinador: PI Manager)                               │
└──────────────┬─────────────────────────────────────────────────┘
               ▼
┌────────────────────────────────────────────────────────────────┐
│ Orquestación e integración — n8n + API + MCP                    │
│ eventos · aprobaciones · colas · notificaciones · cron          │
└──────────────┬─────────────────────────────────────────────────┘
               ▼
┌────────────────────────────────────────────────────────────────┐
│ Capa de ejecución (entornos intercambiables)                    │
│ AutoCAD/Rhino · ComfyUI/Video · Blender/IFC · GPU local/cloud   │
└──────────────┬─────────────────────────────────────────────────┘
               ▼
┌────────────────────────────────────────────────────────────────┐
│ Infraestructura y memoria compartida                            │
│ PostgreSQL · archivos · base vectorial · registro de actividad  │
│ versiones · permisos · biblioteca de capacidades                │
└────────────────────────────────────────────────────────────────┘
```

Separaciones de responsabilidad que la conversación insiste en mantener:

- **Hermes** administra agentes y capacidades; NO es la plataforma completa (PI conserva identidad, base, interfaz y contratos propios).
- **n8n** conecta sistemas y ejecuta automatizaciones por eventos; NO es el cerebro del sistema y debe ser reemplazable por workers propios.
- **MCP + APIs** son el cómo de las herramientas; **los entornos de ejecución** hacen el trabajo pesado.
- ⚠ En el vault la capa de integración de escritorio es **runner propio con sobre de tarea + MCP stdio vía proxy** ([[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4 · Las integraciones, una por una|ESTRUCTURA §4]]), que es la misma idea con más verificación que las conversaciones genéricas.

## 2.3 El package manager de capacidades

La conversación extiende la unidad «capacidad» a nivel plataforma: las skills deberían poder **versionarse, tener dependencias y compatibilidades**, como los paquetes de un sistema operativo. Contrato conceptual de skill propuesto en la conversación (ejemplo conceptual, no configuración lista para instalar):

```yaml
name: architectural-render-from-rhino
version: 1.0.0
description: Genera representaciones visuales desde un modelo Rhino.
inputs:      [model_3dm, camera, visual_style, resolution]
dependencies: [rhino-export, comfyui-api, image-storage]
execution:   { environment: gpu-cloud, timeout: configurable }
validation:  [output_exists, image_resolution, source_model_preserved]
approval:    { required: true }
```

Ecosistema resultante: un arquitecto desarrolla la capacidad de documentación municipal, otro la de calcular superficies, otro extrae geometría de cartografía — se validan, se versionan y se incorporan a distintas instalaciones de PI. **La verdadera unidad de crecimiento de PI no es la cantidad de agentes instalados sino la cantidad de capacidades verificadas disponibles por estudio.**

## 2.4 Workflows invocables (la pata ComfyUI)

Un workflow deja de ser «algo que alguien ejecuta a mano» para convertirse en **capacidad invocable por agente**, con identificador, entradas admitidas, parámetros, modelos requeridos, recursos computacionales, salidas esperadas, tiempo y costos estimados. Las formas de multiplicar la producción con esto:

| Operación | Qué sucede |
|---|---|
| Ejecución | un workflow produce un resultado |
| Batch | un workflow procesa múltiples entradas o variaciones |
| Paralelismo | varios workflows simultáneos (ej. 5 flujos distintos para 5 estrategias de representación) |
| Pipeline | varios workflows encadenados |
| Orquestación | un agente decide qué ejecutar y cuándo |

⚠ decisión del vault ya tomada: los flujos de ComfyUI están versionados bajo reglas propias ([[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]), con ComfyUI detrás de PI y fuera de la vista de las tareas cotidianas.

## 2.5 Los agentes de la conversación vs los del vault

| Conversación | Vault hoy (MVP_02/03/04/05/06/07) |
|---|---|
| **Pipi Rhino** (geometría, cortes) | MVP_05 Rhino-MCP: cortes, tramas, hojas en producción |
| **Pipi CAD** (estándares, auditoría AO) | MVP_02 estándar AutoCAD + MCP por COM en estudio |
| **Pipi Visual / Comfy** (imagen/video) | MVP_04 y 04.02 (matriz txt2img, loras, workflows adaptados del curso AI x Gaudí) |
| **Pipi BIM** (IFC) | hipótesis pendiente — sin IFC real del estudio aún |
| **Pipi Docs** (reuniones, conocimiento) | El circuito fuentes→wiki→Hermes (digest n8n, sherlock, contenidos, vaultworm) |
| **Pipi PM** (tareas, seguimiento) | Leantime + workflows n8n de agenda/reporte |

---

# 3 · Requisitos — la demo y las reglas

## 3.1 Las cuatro condiciones para que la demo sea convincente

La conversación fija precisamente cuatro criterios de aceptación para cualquier demo de PI:

1. **Autonomía real** — el agente completa la tarea sin que la persona intervenga paso a paso.
2. **Trazabilidad** — se puede ver qué hizo, qué archivos utilizó, qué herramientas ejecutó y qué resultó.
3. **Disponibilidad** — puede recibir peticiones aun con la PC personal apagada (24/7 real).
4. **Control** — permisos, límites de ejecución, aprobaciones y registros; *un agente autónomo no necesita tener las llaves de toda la casa*.

⚠ En MVP_07 estas mismas cuatro están en REQUISITOS en versión más exigente: SOBRE DE TAREA, gobernanza A-D y comandos con lista negra que no se saltea ni en modo automático.

## 3.2 La demo recomendada: operación completa, no colección de herramientas

Formato: **5-8 minutos**, tres escenas.

- **Escena A · El estudio tiene una necesidad** — solicitud por Telegram: «busca la ubicación, consigue el modelo 3D de ese terreno, prepara una lámina con vistas y cortes y guarda los resultados».
- **Escena B · Los agentes trabajan en paralelo en distintas computadoras** — 3 estaciones (Rhino en la PC o servidor, AutoCAD en otra, ComfyUI cloud con GPU).
- **Escena C · El humano revisa, decide y aprueba** — PI entrega el informe, el arquitecto abre la lámina, pide ajustes (como jefe de taller, no como operador).

La pregunta abierta al final de la conversación — qué escena demostrar (A. estudio autónomo / B. producción generativa / C. operación arquitectónica completa) y ante qué público — quedó sin responder del lado humano; **hay que decidirla**. La hipótesis del modelo: C convence más comercialmente (estudios clientes), A demuestra la innovación tecnológica (jurado del concurso AI x Gaudí).

## 3.3 Costos y presupuesto de la demo de menor infraestructura

- **Infra actual verificada en la conversación**: VPS ~US$5 (se está pagando ~$7 por ubicación premium) + Comfy Cloud US$20 = **~US$27/mes** y un entorno operable 24/7 — n8n como capa de flujos (mail, Telegram texto/voz, Cal.com para reuniones, Fathom a carpeta por automatización ya implementada).
- La conversación agrega un matiz que conviene conservar: **disponibilidad permanente del sistema ≠ agentes ejecutando todo el tiempo**. Algunos procesos con GPU corren bajo demanda (ej. una PC con GPU libre o en horarios programados) y el sistema seguiría «disponible» (Hermes escuchando).
- Los 5 workflows simultáneos y los 30 min de video/lote de Comfy Cloud son límites del plan a verificar antes de meterlos en el cálculo económico (y conviene medir el consumo real de créditos por tipo de generación).

## 3.4 El presupuesto en 4 compartimientos

La conversación separa los números que suelen mezclarse:

1. **Infraestructura fija** (VPS, dominios, almacenamiento, backups)
2. **Inferencia** (tokens, modelos, APIs)
3. **GPU** (horas de imagen/video — preferir coste por entrega/proyecto antes que un plan mensual fijo sin haber medido)
4. **Licencias** (Rhino, AutoCAD, Twinmotion, servicios que las requieran)

## 3.5 Las métricas sugeridas (panel del sistema)

Agentes activos por día/semana/mes · sesiones por agente y período · tiempo de ejecución por tarea · **documentos generados por período** · skills creadas (acumulativo) · workflows creados (acumulativo) · problemas resueltos por categoría · **reutilización de capacidades** (n.º ejecuciones reutilizadas) · **intervenciones humanas por tarea** · **tasa de éxito**. Y dos indicadores de cierre de la conversación:

- **Capital de conocimiento acumulativo** — cuánto conocimiento operativo nuevo entró al sistema.
- **Capacidad de producción desacoplada del tiempo humano** — cuántas tareas el sistema resuelve sin que el arquitecto esté presente durante la ejecución. **Este es el indicador económico clave** (5 agentes una hora ≠ 1 tarea perfecta en 3 minutos).

## 3.6 Aplicación: los 3 niveles de control

La conversación termina dejando definida una palanca de autonomía configurada por tarea:

- **Asistido** — el agente propone y una persona ejecuta o aprueba cada paso.
- **Supervisado** — el agente ejecuta procedimientos conocidos y solicita aprobación en puntos críticos.
- **Autónomo** — el agente ejecuta lo previamente autorizado dentro de límites de permisos, coste y calidad.

⚠ El vault ya tiene este mapa formalizado como **niveles de riesgo A-D (gobernanza)** en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo|REQUISITOS §7]]: la conversación coincide en lo sustancial; el formato del vault es el que manda.

---

# 4 · Variantes y opciones predilectas

Todas las bifurcaciones que la conversación explícita marca, con la elección preferente del ChatGPT y el cruce contra lo decidido en el vault:

| Decisión | Opciones que plantea | Predilecta del ChatGPT | Vault (decisión vigente) | Δ |
|---|---|---|---|---|
| Cerebro del sistema | plataforma propia vs colección de agentes | PI como sistema con identidad propia donde Hermes es SOLO el entorno de agentes | igual (Hermes en VPS como agente único; su identidad y su DB propia en etapas tempranas) — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#10 · Decisiones técnicas|ESTRUCTURA ADR-1]] | ✅ alineado |
| Modelo del agente | proveedor configurable por tarea | modelo económico para clasificar, modelo más capaz para razonar, locales donde se pueda | OpenCode Go ahora → 2ª instancia con Ollama → OpenRouter como excepción — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3.3 Qué modelo usa|ESTRUCTURA §3.3]] | ✅ alineado (⚠ matiz: Go se reserva para desarrollar PI, no como motor ilimitado de inferencia de los agentes de producción) |
| Base de datos | PostgreSQL central / vectorial | Postgres + pgvector; **MinIO/S3 para archivos pesados** | Postgres para lo vivo + **Qdrant** ya corriendo + vault como memoria legible; blobs fuera de la base (archivos en disco/vault) — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#6 · El registro central y el grafo|ESTRUCTURA §6]] | ⚠ pgvector y MinIO quedan como notas abiertas del lado vault (Qdrant ya hace lo vectorial) |
| Vigilancia tecnológica | Telegram: canal vs grupo | **PI Radar**: canal (difusión) + grupo (comunidad) vinculados, privado → abierto | ya existe de base: digest diario por Telegram (sesiones 09/16) + sherlock para fuentes — [[proyectos/MVP_04-comfyui-arquitectura|portal concurso]] | 🆕 PI Radar es un workflow n8n de construcción fácil (3 etapas) |
| Infraestructura en 3 niveles | económica / híbrida / total-control | empezar por **híbrida** (VPS + estaciones + GPU cloud) | coherente con 4 nodos ESTRUCTURA (VPS + PC + banco + GPU nube) | ✅ alineado |
| GPU cloud | Runpod Secure vs alternativas europeas | Runpod Secure bajo demanda (DPA firmado, sin entrenamiento, volumen cifrado, 0 puertos); alternativa europea (Scaleway/OVH FR) anotada | Runpod Secure con esas mismas condiciones — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4.4 Imágenes (IA)|ESTRUCTURA §4.4]] y ADR Runpod | ✅ alineado (⚠ matiz: para la demo del concurso, Comfy Cloud USD 20 es la infra concreta; Runpod es la excepción formal del vault) |
| Dibujo → 3D (la bandera) | imagen generativa vs geometría editable | la tesis «si lo puedo dibujar, lo puedo tener en 3D»: **generar imagen ≠ construir geometría editable** | el cuaderno digital (croquis escaneados → wiki) es el camino análogo — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#8 · El cuaderno digital: cómo se construye|ESTRUCTURA §8]] | 🆕 concretar flujo croquis→3D→render→teléfono |
| BIM abierto | FreeCAD(BIM) vs IfcOpenShell+Bonsai | IfcOpenShell + Bonsai (Blender) | FreeCAD + IfcOpenShell — [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4.3 IFC / BIM|ESTRUCTURA §4.3]] | ⚠ Bonsai como alternativa a evaluar |
| Rhino sin pantalla | estación con Rhino vs **Rhino.Compute** (API REST de geometría/GH) | Rhino.Compute para operaciones de geometría y Grasshopper vía API | lo decidido es MCP stdio + Hops; Rhino.Compute es un candidato real nuevo para completar el modo R2 (headless) | 🆕 evaluar (licencia y costos de producción antes de presupuestar el escalado) |
| Equipo > 5 personas | interfaz web con roles | **los usuarios NO trabajan con agentes: trabajan con proyectos, solicitudes y capacidades** (Inicio · Proyectos · Solicitar capacidad · Revisión/aprobación) | mismo principio en el vault: la persona pide en lenguaje natural, la tecnología queda debajo | 🆕 producto multiusuario (Etapa 5 del plan) |
| Escalabilidad técnica de forma | Docker Compose SQL/worker/queue | Postgres + Redis colas + n8n queue mode | la arquitectura actual — igual en espíritu | ✅ alineado |

---

# 5 · Ideas nuevas que el vault todavía no tenía

Candidatas a incorporar (ninguna decide sola; van a backlog):

1. **PI Resource Manager**: capa que DECIDE DÓNDE correr cada tarea (GPU local libre→local; ocupada→cloud; necesita app de una PC→programar; requiere aprobación→espera; urgente→prioridad). Los perfiles nube-propio/local ya existen en MVP_07, pero el router automático de colocación está por construirse. ⚠ Es la misma idea que perfiles + sobre de tarea ya definidos: el router hay que construirlo sobre el contrato del vault, no al lado.
2. **Package manager de capacidades** (§2.3): skills con versión, dependencias, compatibilidades y catálogo validado. Es la caja de instrumentos abierta que puede crecer con aportaciones de creadores externos — la extensión natural del catálogo de skills de [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].
3. **PI Radar como vigilancia tecnológica en 3 etapas** (interno → estudio → Academia PI), con 6 áreas de vigilancia (modelos, herramientas/workflows, agentes y desarrollo, arquitectura y diseño, creadores de contenido, ecosistema FOSS) y la regla de **diferenciar novedad de actualización** (¿qué cambió respecto de la versión anterior?) con fuente original, fecha y enlace en cada entrada.
4. **El experimento de 30 días de productividad documentada** — registrar de verdad (tareas completadas, correcciones, horas humanas conservadas, costo por ejecución, tiempo efectivo vs tiempo de espera) y terminar con un caso propio, no con promesas. «La primera demostración de PI sos vos trabajando con PI».
5. **PI Visual Studio como MVP con la demo más completa** (subir Rhino/croquis/referencia → PI elige workflow, decide GPU local/cloud, genera alternativas, QA, aprobación, archiva trazabilidad) — es la evolución natural de la matriz txt2img y una cara concreta para explicar el concurso.
6. **El teléfono como ventana de aprobación**: visualización/aprobación de procesos que corren en otra computadora — llegar alternativas por Telegram, elegir, pedir cambios. Resonante con la regla de gobernanza del vault (aprobación queda registrada).
7. **Los 4 presupuestos compartimentados** (§3.4) para el futuro dashboard financiero del estudio.

---

# 6 · Frases y narrativa para reutilizar

## 6.1 La historia personal (hilo de 5 actos sugerido)

1. **Hace 6 meses: cambiar la pregunta** — Soy arquitecta. Durante años usé herramientas digitales para resolver problemas de arquitectura; en abril empecé a estudiar IA y programación asistida, incluyendo contenidos de ingeniería informática.
2. **El descubrimiento: el problema no es el software** — cuántas horas profesionales se dedican a operar herramientas, transferir información y repetir procedimientos que pueden sistematizarse.
3. **El experimento: dejar de trabajar uno a uno** — agentes especializados que usan herramientas y entornos de ejecución diferentes.
4. **La consecuencia: multiplicar la capacidad** — mientras trabajo en un modelo, otros procesos investigan, verifican, generan imagen o preparan archivos; el tiempo humano se concentra en dirigir, decidir y validar.
5. **El proyecto: PI** — un sistema operativo de capacidades para estudios de arquitectura.

Cierre: **«La pregunta ya no es cuánto puede producir un arquitecto en ocho horas. La pregunta es cuánto puede producir cuando deja de usar esas ocho horas para operar cada herramienta.»**

Otra: **«La primera demostración de PI sos vos trabajando con PI.»**

## 6.2 Distinciones de lenguaje (guion anti-humo)

- **Modelo** (pesos entrenados) ≠ **producto** (ChatGPT) ≠ **agente** (OpenCode/Hermes) ≠ **plataforma de workflows** (ComfyUI) ≠ **familia de modelos** (FLUX).
- **Software libre / open source** (licencia de código) ↔ **open weights** (pesos descargables con condiciones) ↔ **propiedad por API** ↔ **workflow abierto**. Un modelo con pesos abiertos no es open source; un workflow abierto no implica modelos abiertos. Distinción fundamental para diseñar PI bajo FOSS.
- **Disponibilidad del sistema** ≠ **agentes siempre corriendo** — Hermes puede estar disponible 24/7 y las GPU trabajan bajo demanda: es administración de recursos computacionales.
- **Novedad** ≠ **actualización** de un modelo: registrar el delta contra la versión anterior.
- **Imagen generada** ≠ **geometría 3D editable** — para arquitectura se necesitan ambas, y la IA no reemplaza la validación geométrica.

---

# 7 · Pendientes que abren hacia MVP_07

| Pendiente | Cuándo | Enlazar con |
|---|---|---|
| Elegir la **demo del concurso** (A/B/C) y su público — v. §3.2 | antes de la entrega | [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso]], [[proyectos/concurso-gaudi-nexus/00-index|concurso-gaudi-nexus]] |
| Definir si entra **Rhino.Compute** como modo R2 del runner | ADR corto | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3.4 Los modos de ejecución|ESTRUCTURA §3.4]], ADR puente |
| **Router de recursos** (colocación automática de tareas por disponibilidad/coste) | tramo T3+ | ESTRUCTURA §9, sobre de tarea |
| **Bonsai/Blender** como 2ª vía BIM vs FreeCAD | cuando exista IFC real | ESTRUCTURA §4.3 |
| **PI Radar** fase 1 (n8n + 5 fuentes iniciales de la conversación: novedades OpenAI/Anthropic, GitHub Hermes+OpenCode, ComfyUI y ecosistema, canales YouTube elegidos) | próximo, junto al digest existente | [[proyectos/MVP_04-comfyui-arquitectura|portal concurso]], digest diario |
| Catálogo de skills con **versión/dependencias** (package manager) | cuadro de proyección T5 | IMPLEMENTACION-HERMES (SOUL, skills) |
| Panel de métricas (10 indicadores de §3.5 + los 2 de capital y desacople) | con T2 registro activo | REQUISITOS §9 |

---

## Referencias verificadas (en la propia conversación, por el share)

- Documentación y repositorios mencionados por el modelo con `Cite`/`Link` internos (la conversación los verificó en su búsqueda del 22/09 y 31/10): Hermes Agent (arquitectura interna y docs), ComfyUI (repo oficial + docs agentes + Comfy API despliegue de workflows como servicios), Rhino.Compute (docs oficial REST de Rhino/GH), IfcOpenShell + Bonsai (OpenBIM), n8n (queue mode con Redis/PostgreSQL y requerimiento S3), OpenCode Go (límites del proveedor).
- Los cinco workflows de ComfyUI versionados y las reglas propias: [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]].
- Contexto del study OS emprendido antes de la conversación: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].
