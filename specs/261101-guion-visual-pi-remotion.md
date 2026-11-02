---
tipo: metodologia
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-02
tags: [pi, studio-os, remotion, guion-visual, agentes, arquitectura, meta-arquitecto, empresa-sintetica]
idioma: es
---

# PI — guion visual para la presentación y el video

> **Nombre de trabajo:** PI es el nombre del sistema (Sol, matrícula Pi). Studio OS es el producto replicable con piloto Emilia según [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|VISION §6.9]]. «Plataforma de Inteligencia» es expansión editorial solo para el video, no renombra el sistema.
> **Presentación web:** `diagramas/prompt-coach-vs-agentico.html`.
> **Composición Remotion:** `PIStudioOS` en `P:\00-repos\remotion-vault`.
> **Base del sistema:** [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]].
> **Mapa técnico:** [[diagramas/arquitectura-pi-os|arquitectura-pi-os]]. **Dibujo:** el boceto manual de Sol reemplazará los pictogramas vectoriales provisionales cuando esté disponible.

## Idea rectora

Mostrar la evolución de **una relación lineal** a **una empresa sintética de capacidades**. Para PI, la expresión «empresa sintética» nombra un sistema de agentes por rol, memoria y workflows que coordina trabajo del estudio; **las personas conservan diseño, criterio y responsabilidad profesional**.

```text
01 · ARQUITECTO OPERADOR
persona ↔ software (ciclo 1:1)
        ↓
02 · META-ARQUITECTO EN MODO ARTESANAL (Sol hoy)
persona construye y opera varios agentes, terminales y herramientas
        ↓
03 · PI · EMPRESA SINTÉTICA DE CAPACIDADES
cerebro confidencial + Hermes + automatizaciones + roles y workflows
        ↓
04 · META-ARQUITECTO SISTÉMICO
diseña, gobierna, mantiene y amplía el sistema que permite producir arquitectura
```

El lenguaje visual combina **dibujo de arquitectura a mano** (trazo irregular, anotaciones, flechas) con un **grafo técnico vivo**. El árbol nace del mini guion dibujado por Sol, abre ramas por agente y modalidad, y se conecta transversalmente como un rizoma: las skills, fuentes, modelos y recursos pueden ser compartidos.

### Tesis: la IA no nace con los LLM

La inteligencia artificial existe como campo desde los años 1950; Dartmouth propuso el proyecto de investigación de IA en 1955 y realizó el taller seminal en 1956. La contribución contemporánea de los LLM es otra: acercan lenguaje, código y herramientas a más personas, y bajan el costo de mapear procedimientos que antes requerían integración técnica especializada.

> **Tesis de PI:** los LLM ayudan a convertir deuda técnica operativa —procesos repetidos que viven en la cabeza de los seniors, scripts dispersos, estándares difíciles de descubrir y flujos desconectados— en procedimientos legibles, herramientas enlazadas y capacidades mantenibles. El sistema paga esa deuda **cuando** captura, prueba, versiona y conserva esas capacidades; la generación de código por sí sola también requiere mantenimiento.

La capacidad operativa permanente es una hipótesis de diseño medible, no un multiplicador mágico: el gateway queda disponible; cada ejecución usa recursos bajo demanda/agenda y vuelve con evidencia. Se usa la fórmula ya propuesta en la conversación: `P = trabajo útil validado / intervención humana`. Cada comparación se basa en entregables aprobados, minutos de atención humana, tiempo de ejecución/espera, correcciones y costo.

### La pregunta de fondo: el rol del arquitecto en la cuarta revolución industrial

La **Cuarta Revolución Industrial** es el marco narrativo de Sol para una profesión donde software, datos y fabricación se integran al diseño. No es la afirmación de que “la IA empezó ahora”: la disciplina de IA tiene una historia de décadas. La diferencia contemporánea es la interfaz LLM, que vuelve más accesible describir objetivos y construir código/procedimientos con lenguaje natural, y la capa agéntica que coordina esas herramientas.

La tesis profesional que propone PI: el arquitecto ya no necesita medir su aporte solo por cuánto tiempo opera programas. Puede dirigir una infraestructura que ejecuta procedimientos repetibles mientras conserva lo que hace específica su profesión: **definir el problema, establecer estándares, elegir entre alternativas, cuidar el contexto humano y asumir la responsabilidad de la decisión**. La reducción de tiempo senior transferido es una métrica de ese cambio.

## Rol del arquitecto en el flujo aumentado

### La evolución del rol

| Etapa | Rol del arquitecto | Quién sostiene el flujo |
|---|---|---|
| **Operador 1:1** | Ejecuta instrucciones en una herramienta, espera, revisa y corrige cada ciclo. | La persona, paso a paso. |
| **Meta-arquitecto artesanal** | Configura el entorno, decide qué agente usar, reparte tareas entre sesiones y mantiene conectores, scripts y workflows. | La persona sigue presente como despachador de cada línea de trabajo. |
| **PI · empresa sintética** | Es la infraestructura que organiza roles, permisos, memoria, automatizaciones, recursos y resultados verificables. | Hermes coordina; n8n conecta eventos; scripts y workflows ejecutan tareas autorizadas. |
| **Meta-arquitecto sistémico** | Diseña roles, estándares, conectores, capacidades, políticas y mantenimiento; observa métricas y prioriza la evolución del sistema. | Los arquitectos de proyecto reciben las capacidades listas para usar; el Meta-arquitecto es quien diseña y mantiene esa infraestructura. |

**Cierre narrativo:** la historia termina en el **Meta-arquitecto**, que diseña y mantiene la infraestructura capaz de sostener una empresa sintética. No termina con un arquitecto que solo usa una plataforma. El arquitecto de proyecto sigue definiendo y aprobando su trabajo; el Meta-arquitecto crea las condiciones para que las capacidades del estudio permanezcan disponibles, seguras y reutilizables.

### El Meta-arquitecto como cierre

El cierre es el **Meta-arquitecto sistémico**: la persona que convierte lo aprendido al operar múltiples agentes en diseño del sistema, y luego mantiene ese sistema vivo. El sistema le permite trabajar por objetivos y excepciones en lugar de despachar cada terminal.

En el nivel artesanal, Sol alterna entre sesiones de Antigravity/OpenCode, asigna instrucciones, revisa reportes y mantiene el vault/Wiki. En PI, Hermes ordena y ejecuta procedimientos autorizados sobre un cerebro local/confidencial, con MCP y automatizaciones n8n. Como Meta-arquitecto, Sol configura roles, idiomas de herramienta, skills, estándares, permisos, perfiles local/VPS/cloud, presupuesto, monitoreo y mantenimiento.

Los arquitectos de proyecto reciben una interfaz sencilla para solicitar tareas, revisar alternativas y aprobar hitos. **Son usuarios expertos de la empresa sintética; el protagonista del relato sigue siendo el Meta-arquitecto que la diseña y la evoluciona.**

### Qué conserva y qué delega

| El arquitecto conserva | El asistente personal puede ejecutar dentro del encargo |
|---|---|
| Intención del proyecto, programa, contexto y prioridades. | Descomponer el pedido en tareas y proponer el orden de ejecución. |
| Criterios de diseño, calidad, tolerancias y definición de “listo”. | Seleccionar agentes y capacidades compatibles con el proyecto. |
| Decisiones con ambigüedad proyectual o impacto contractual. | Invocar MCPs, scripts Python, APIs, n8n y workflows aprobados. |
| Revisión de alternativas, aprobaciones críticas y emisión final. | Trabajar en paralelo en Rhino, AutoCAD, ComfyUI, documentación y seguimiento. |
| Responsabilidad profesional y comunicación con el cliente. | Comparar versiones, preparar entregables, registrar fuentes y reportar excepciones. |

La autonomía se asigna **por tarea y por riesgo**, no como permiso total sobre el estudio:

- **Puede avanzar de manera autónoma:** lectura, clasificación, generación de alternativas, informes, operaciones repetibles y reversibles dentro de una carpeta/proyecto autorizado.
- **Se detiene para aprobación:** acciones de escritura sensibles, cambios difíciles de revertir, uso de datos fuera del perfil permitido, selección final de diseño o publicación/emisión contractual.
- **Entrega siempre:** estado, resultado, advertencias, archivos de entrada/salida, herramienta y versión usadas, costo/tiempo y decisiones que necesitan a una persona.

### Contrato del asistente personal sintético

Cada arquitecto dispone de un asistente persistente con una identidad de trabajo, contexto del proyecto y un catálogo de herramientas limitado al rol. El contrato de una tarea especifica:

```text
objetivo + proyecto + entradas autorizadas
rol/agentes + herramientas MCP/API/script permitidas
perfil de ejecución (local · VPS · GPU nube)
criterios de calidad + riesgo + presupuesto/tiempo
puntos de aprobación + forma de registrar procedencia
```

El asistente puede pedir aclaración cuando falta un dato que cambia el resultado; con un encargo suficientemente definido, arma un grafo de tareas, activa subagentes y comunica avances, excepciones y entregables. La supervisión se concentra en los hitos que requieren criterio, en lugar de seguir cada llamada a herramienta.

**Experiencia personal y arquitectura compartida:** la visión de producto es que cada arquitecto sienta que trabaja con su asistente personal —preferencias, proyectos y permisos relevantes—. La decisión vigente de [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|MVP_07]] es **un Hermes central por estudio**. La forma de ofrecer perfiles/personas con memoria aislada sobre ese núcleo queda como decisión técnica abierta; el guion no presenta una instancia independiente por arquitecto como algo ya implementado.

### Aprendizaje definido: memoria, procedimientos y modelos

La palabra **aprendizaje** describe tres mecanismos diferentes; el video los dibuja como tres anillos, del más inmediato al más costoso:

1. **Memoria de trabajo y de proyecto:** preferencias, estándares, decisiones, contexto y sesiones relevantes que siguen disponibles entre conversaciones. Esto mejora la continuidad; no cambia los pesos del modelo.
2. **Aprendizaje procedimental:** cuando una secuencia produce un resultado revisado, PI puede proponer convertirla en una skill/workflow con fuentes, entradas, dependencias, versión, pruebas y criterios de validación. El arquitecto aprueba su publicación en la biblioteca compartida. Una corrección aislada queda como observación hasta que se prueba.
3. **Aprendizaje estadístico del modelo (ML):** fine-tuning, LoRA u otro entrenamiento de pesos es un proceso distinto y explícito. Requiere datos autorizados, licencia compatible, objetivo medible, evaluación antes/después, versión del modelo y aprobación. El sistema de skills no se presenta como reentrenamiento automático.

```text
resultado → revisión arquitectónica → feedback registrado
         → hipótesis de mejora → prueba en casos representativos
         → aprobación humana → skill/workflow versionado
         → capacidad reutilizable en futuros proyectos
```

Así PI aprende de forma **acumulativa y gobernada**: mantiene memoria útil, convierte procedimientos comprobados en capacidades y trata el entrenamiento del modelo como una línea aparte.

## Empresa sintética: una organización de roles, no un chat gigante

PI se puede representar como una empresa sintética compuesta por **roles de trabajo que cooperan**. Cada rol tiene un objetivo, clases de tarea, lenguajes y herramientas permitidas, capacidades versionadas, recursos de ejecución, criterio de calidad y política de aprobación. Hermes actúa como núcleo de interpretación/delegación; n8n conserva las integraciones deterministas; el vault preserva el conocimiento del estudio.

| Rol/agente | Trabajo que recorre los proyectos | Idioma/herramientas nativas | Evidencia disponible y estado actual |
|---|---|---|---|
| **PI Manager / asistente del arquitecto** | recibe el objetivo, lo traduce a un grafo de tareas, asigna prioridades y devuelve decisiones pendientes | lenguaje natural · Hermes · skills · MCP · cron | Hermes como agente único de estudio está especificado en MVP_07; autonomía por tarea y gobernanza A–D |
| **Pipi CAD** | mantiene estándares de dibujo, audita documentos, compara versiones y prepara paquetes de entrega | comandos AutoCAD · AutoLISP · scripts Python/ezdxf · MCP/API según edición | SET_01-REP y SET_02 tienen estándares y rutinas documentadas. AutoCAD LT 2027 limita COM externo; el MCP oficial de Autodesk para LT figura pendiente de prueba |
| **Pipi Rhino** | importa/inspecciona geometría, calcula cortes, organiza capas, genera vistas y láminas | Python en Rhino/RhinoCommon · Grasshopper/Hops · Rhino MCP | MVP_05 verificó cortes, detalles y láminas en casos AIZ/plaza; guardar/publicar y criterio de dibujo siguen bajo decisión humana |
| **Pipi Visual** | convierte instrucciones/referencias en variantes visuales, imagen y video, y registra el experimento | JSON de workflow · API ComfyUI · Python/nodos · modelo/LoRA/seed | WF-05 probó img2img con seed 42 y denoise 0.4/0.6/0.8; cada workflow conserva su ficha. GPU local primero, cloud bajo perfil/costo |
| **Pipi Docs / conocimiento** | captura reuniones, sintetiza compromisos, organiza fuentes y mantiene la memoria consultable | Fathom · n8n · Markdown/Wikilinks · búsqueda/vault | El flujo reunión→minuta/compromisos→Leantime/vault es el patrón de VISION/ESTRUCTURA; cada afirmación recupera su fuente |
| **Pipi PM / operaciones** | agenda, tareas, recordatorios, estados, digest y métricas | Leantime MCP · Cal.com · Telegram · n8n · cron Hermes | El MCP de Leantime y flujos de agenda/recordatorio están en el stack; un cron autónomo se limita a trabajos autorizados y entrega resultados |
| **QA / guardián de proceso** | verifica entradas/salidas, hash, clases de dato, versión, costos, permisos y criterios de aceptación | scripts de validación · registro PostgreSQL · vault · reglas A–D | REQUISITOS exige tarea registrable, originales intactos y aprobación explícita en C/D |

### Cadena común a cada proyecto

```text
cliente / brief / agenda
 → reunión y decisiones (Fathom → transcripción → minuta → compromisos)
 → sitio y referencias (fuentes citadas → contexto/3D cuando aplica)
 → proyecto (AutoCAD estándares → Rhino/geometría → Comfy imagen/video)
 → documentación y entregas (paquete + QA + aprobación nivel D)
 → obra y seguimiento (fotos/incidencias/tareas)
 → memoria del estudio (vault/wiki + skills aprobadas)
```

Las áreas de agentes cubren el ciclo entero, no únicamente modelado e imagen. En cada paso el sistema automatiza lo repetible y rastreable; la persona decide el contenido de diseño, el significado de la evidencia y la comunicación contractual.

Los agentes **no son un organigrama que reemplaza al estudio**. Son roles reproducibles dentro del ciclo de cada proyecto; una misma persona puede revisar varias ramas y una skill probada puede servir a varios roles.

### El flujo aumentado, desde el encargo hasta una capacidad compartida

```text
1 · ARQUITECTO: objetivo + proyecto + criterio de calidad + límites
2 · ASISTENTE PI: contexto autorizado + plan de tareas + puntos de decisión
3 · HERMES: asigna subagentes y skills; n8n mueve eventos deterministas
4 · AGENTES: CAD (AutoLISP) · Rhino (Python/GH) · Visual (Comfy JSON/API)
              · Docs (Fathom/vault) · PM (Leantime/cron)
5 · ROUTER: estación local · VPS · GPU cloud, según datos/permisos/costo
6 · REGISTRO: archivo/versión · herramienta · parámetros · tiempo/costo · origen
7 · ARQUITECTO: revisa alternativas, decide diseño y aprueba lo crítico
8 · MANTENIMIENTO: feedback → prueba → skill/workflow versionado → nueva tarea
```

Este es el salto buscado: **el arquitecto entrega el input de dirección una vez; el sistema conserva la capacidad de ejecutar y coordinar entre sesiones**. La respuesta regresa con entregables y las excepciones que requieren juicio. El agente administra tareas en límites asignados; la persona mantiene control sobre el criterio.

### Deuda técnica: qué absorbe PI y qué pasa a mantener

La tesis de PI trata la deuda técnica como **trabajo repetido, conocimiento tácito e integraciones frágiles que pueden documentarse, probarse y ponerse al servicio del estudio**. Los LLM bajan el costo de leer código y escribir en distintos lenguajes; la deuda se reduce cuando esos artefactos quedan testeados y mantenidos, no por la generación de código en sí.

| Deuda repetitiva del estudio | Capacidad PI que la sistematiza | Mantenimiento visible |
|---|---|---|
| Estándar CAD solo en la cabeza del dibujante | plantilla/DWT + reglas + AutoLISP + auditoría de lectura | versiones de AutoCAD, rutinas, CTB/layers y pruebas de compatibilidad |
| Cortes, tramas y láminas repetidos por proyecto | playbook + scripts Rhino + presets de Layout | API Rhino, librería de casos, screenshots/escala y regresiones |
| Workflows Comfy aislados y prompts que se pierden | JSON versionado + modelo/LoRA/seed + prueba comparativa | cambios de nodos, dependencias, licencia, VRAM, costo y calidad |
| Reuniones, tareas y decisiones dispersas | Fathom → n8n → minuta/Leantime/vault | credenciales, endpoints, cron, fallos y calidad de clasificación |
| Respuestas que dependen de un senior | Wiki/vault con enlaces y procedencia + asistente de consulta | deduplicar, actualizar, marcar obsoleto y mantener backlinks |

La **deuda del sistema** también queda a la vista: conectores MCP, librerías, scripts, modelos, skills, permisos, backups, observabilidad y costo por ejecución. PITAUTECH opera esa capa con tiempo y presupuesto explícitos; el estudio conserva sus estándares y las decisiones de arquitectura.

### Conocimiento privado del estudio y LLM internos

El objetivo no requiere empezar entrenando un modelo propio. La base inicial es el **conocimiento privado consultable**: vault/wiki, estándares, documentación de proyectos y fuentes, con clases de acceso y permisos. RAG/recuperación con citas permite que el asistente responda desde ese corpus. Un modelo local o privado es un perfil de despliegue para clases de datos sensibles; fine-tuning se evalúa aparte.

Hay casos documentados en firmas internacionales, que se presentan como ejemplos concretos:

- **Foster + Partners:** Ask F+P usa LLM y búsqueda semántica sobre guías de diseño internas; la entrevista lo describe como herramienta en beta para el personal. También utilizaron Stable Diffusion alojado localmente para sugerir sobre modelos ya diseñados.
- **Zaha Hadid Architects:** NVIDIA documenta infraestructura local para proteger IP, uso de archivo propietario y LoRAs/modelos personalizados dentro de un pipeline de trabajo.

Estos casos muestran que archivo interno, investigación aplicada, infraestructura controlada y herramientas propias forman una vía posible; **no establecen que todos los estudios europeos tengan un LLM privado** ni que PI necesite entrenamiento de pesos para su primera versión.

### Costos, operación y continuidad

Para calcular la capacidad operativa permanente se mantienen visibles las cuatro partidas de [[proyectos/MVP_07-studio-os-sistema/VISION#5 · El stack delineado|VISION §5]] más mantenimiento humano, en línea con [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#5 · Requerimientos no funcionales|REQUISITOS RNF-10]]:

1. **Núcleo siempre disponible:** VPS, almacenamiento, backup, red privada y monitoreo.
2. **Modelos:** suscripciones/tokens o inferencia local; se mide costo por tarea y por perfil.
3. **Ejecución pesada:** GPU local/cloud según tamaño del modelo, duración y datos admitidos.
4. **Mantenimiento humano:** actualizar MCPs y scripts, probar workflows, revisar skills, restaurar backups, resolver fallas y curar el vault.

Hermes Gateway y cron mantienen tareas accesibles/programables cuando el host está activo. Eso libera la supervisión continua del proceso; la disponibilidad real, el costo y las tareas que pasan sin humano se registran por ejecución. La productividad se calcula con el trabajo validado y el tiempo de intervención humana, no con la cantidad de agentes encendidos.

### Línea narrativa para la presentación

> **El arquitecto define el norte y los límites. Su asistente personal organiza el trabajo, activa especialistas y herramientas, ejecuta procedimientos autorizados y vuelve con resultados trazables. El arquitecto decide qué significa una buena solución, aprueba los hitos y convierte el aprendizaje validado en una capacidad compartida.**

En el dibujo, una línea continua conecta arquitecto y asistente; las ramas autónomas se despliegan desde el asistente hacia los especialistas. Las aprobaciones aparecen como umbrales visibles y el feedback vuelve al árbol como una nueva capacidad validada.

## Storyboard propuesto — ~86 segundos, 16:9

Composición 1920×1080, 30 fps, sin locución en la primera versión; música y textos cinéticos. La duración es una meta de edición, no una promesa de rendimiento operativo.

| N.º | Duración aprox. | Texto en pantalla                                       | Dibujo / acción animada                                                                                                                                                                                | Idea que debe quedar                                                                                                    |
| --: | --------------: | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
|  01 |             8 s | **PI · Plataforma de Inteligencia** / para arquitectura | Se dibuja el símbolo PI como un sello técnico; una línea de lápiz dibuja al arquitecto y su computadora.                                                                                               | Presentar PI como sistema, no como modelo de IA.                                                                        |
|  02 |            10 s | **1:1 · una persona, una computadora**                  | Flecha de ida: instrucción; flecha de vuelta: resultado. Se cierra un lazo; la persona modifica y vuelve a empezar.                                                                                    | El ciclo manual está limitado por atención humana y disponibilidad del equipo.                                          |
|  03 |            13 s | **Meta-arquitecto · 4–6 sesiones, una directora**       | Se multiplica la interfaz de desarrollo: Antigravity/OpenCode, agentes, MCPs, scripts, GitHub y n8n. Los reportes vuelven al vault; una mano cura índices, enlaces y conocimiento.                     | La capacidad crece y también crece el trabajo de integración/mantenimiento; Sol sigue dirigiendo cada sesión.           |
|  04 |            11 s | **PI · la empresa sintética se pone en marcha**          | Cerebro local/confidencial → Hermes → n8n/MCP → roles y workflows → ejecución local/VPS/GPU → registro + aprobación. | El sistema creado por el Meta-arquitecto sostiene el flujo completo entre proyectos. |
|  05 |            15 s | **Una empresa sintética de roles y lenguajes**          | Grafo fractal: AutoCAD/AutoLISP · Rhino/Python/GH · Comfy/JSON/API · Docs/Fathom-vault · PM/Leantime-n8n · QA/registro. Ramas conectadas por capacidades compartidas.                                  | Cada rol se ocupa de tareas del ciclo del estudio; cada skill/idioma está conectado al programa real.                   |
|  06 |            13 s | **Tres estaciones · un mismo contrato de tarea**        | CAD/Rhino local; Hermes/n8n/registro en VPS; Comfy en GPU local/cloud. En el borde exterior aparecen actualizaciones, pruebas, backups, permisos y costo por ejecución.                                | El sistema libera operación repetida y hace visible su costo de mantenimiento.                                          |
|  07 |            11 s | **Comfy · una capacidad, muchas entradas**              | Texto/voz/croquis/imagen/video → WF versionado → GPU local o nube → resultado + metadata + review. Al costado, una prueba real recorre denoise 0.4/0.6/0.8.                                            | Una tarea visual deja un procedimiento reproducible; la imagen y la geometría editable siguen siendo salidas distintas. |
|  08 |            10 s | **El Meta-arquitecto diseña lo que sigue**              | El Meta-arquitecto ocupa el centro del grafo: revisa métricas, versiones, costos, permisos, backlog y feedback validado. Los arquitectos de proyecto aparecen usando capacidades a su alrededor. | El cierre es quien diseña y mantiene el sistema; no un usuario final de la plataforma. |

Duración total de escenas: 91 s; con 7 transiciones de 20 frames, duración final estimada = 86.3 s.

La empresa sintética es la infraestructura de trabajo que aparece en escena 04; escena 08 devuelve la cámara al **Meta-arquitecto** como protagonista del futuro de la profesión.

## Mapa técnico que aparece en la web desplegable

### Sistema de agentes y MCPs que ya están configurados

Los nombres se toman de `opencode.json`; los nodos muestran funciones ilustrativas, no una afirmación de que Hermes ya esté conectado a todos ellos. El modelo vigente de MVP_07 tiene **un núcleo Hermes por estudio**. La experiencia de “asistente personal” se propone como identidad/contexto y acceso por arquitecto; crear una instancia Hermes separada por persona requiere decisión posterior.

| Nodo de PI | Conectores reales del vault | Ejecución / aplicación |
|---|---|---|
| Pipi Comfy | `comfyui` | ComfyUI y workflows; GPU local o cloud según el perfil y la disponibilidad. |
| Pipi CAD | `autocad`, `autodesk-help` | AutoCAD local por COM; consulta de documentación Autodesk. |
| Pipi Rhino | `rhino` | Modelado/consulta desde Rhino en la máquina conectada. |
| Pipi Docs | `fathom`, `fathom-proyectopi`, `n8n-mcp` | Reuniones, automatizaciones y traslado de datos hacia el vault. |
| Pipi PM | `leantime`, `n8n-mcp` | Tareas, cronogramas y reportes. |
| PI / entorno común | `fathom`, `autodesk-help` y el resto de la biblioteca según tarea | Registro, fuentes y soporte transversal. |

Inventario completo en la configuración: `comfyui`, `n8n-mcp`, `fathom`, `fathom-proyectopi`, `leantime`, `autodesk-help`, `autocad`, `rhino`.

### Lenguaje nativo y ejemplos que ya existen

La especialización es por **tarea y dominio**, no solo por programa. El agente selecciona el lenguaje de cada herramienta y deja la prueba para el entorno que la ejecuta.

| Rol/capacidad | Lenguaje o contrato | Ejemplo real del vault | Estado que se representa |
|---|---|---|---|
| **Pipi CAD** | comandos CAD · AutoLISP · Python/ezdxf para inspección externa | SET_01: LSP de normalización/símbolos + auditoría de DWG en `scripts/audita-dwg.py`; estándares, plantillas y capas documentadas en MVP_02 | rutinas y auditorías existen. AutoCAD LT 2027 limita COM externo; el MCP oficial Autodesk para LT está pendiente de prueba. |
| **Pipi Rhino** | Rhino Python/RhinoCommon · Grasshopper/Hops · MCP | `scripts/cortes-plaza-rhino.py`: dos cortes A1 en una plaza; playbook AIZ con hoja A3 1:50 medida y verificada | ejemplo de scripts generados y depurados con el puente; cada modelo/hoja sigue con revisión del arquitecto. |
| **Pipi Visual** | workflow JSON · API de ComfyUI · prompts/modelos/LoRA | WF-05: img2img sobre la misma base y seed 42, comparación de denoise 0.4/0.6/0.8 | corridas registradas; modelos y GPU se eligen por hardware, licencia, privacidad y costo. |
| **Pipi Docs / PM** | flujos n8n · API/MCP · Markdown | patrón de reunión Fathom → minuta/compromisos → Leantime/vault; agenda y recordatorios por Telegram | automatización determinista + agente para interpretar y documentar; el envío externo conserva aprobación. |
| **QA / biblioteca** | Python · hashes · validaciones · Git | `audita-dwg.py`, registro de artefactos, repos y estándares | las pruebas deterministas verifican; una skill candidata se publica después de evaluación/aprobación. |

**Regla para la animación:** “hablar AutoLISP”, “hablar Python de Rhino” o “entender el grafo JSON de Comfy” significa operar con el contrato real de esa herramienta, generar o seleccionar el artefacto adecuado, validarlo y ejecutarlo en el perfil permitido. La generación de código por sí sola no cuenta como capacidad lista.

### Ramas de Comfy

```text
Pipi Comfy
├── entradas L0-L4: texto · texto+referencia · croquis/mano/tablet · gráfico técnico · collage
├── controles F: Canny · Depth/Normal · Lineart/Sketch · Segmentación · IPAdapter · Tile · Inpaint/Outpaint · OpenPose
├── workflows: text-to-image · image-to-image · modelo 3D-a-imagen · image-to-video
├── ejecución: ComfyUI local · Comfy Cloud/API · GPU cloud bajo demanda
└── salida: imagen/video + parámetros + modelo/workflow + procedencia + revisión
```

La animación evita presentar un render generado como modelo geométrico. Para el flujo arquitectónico, **imagen visual** y **geometría editable** aparecen en ramas relacionadas pero distintas.

### Capas comunes a todas las ramas

```text
SOLICITUD
  → PI Manager / Hermes (interpretar, elegir capacidad, delegar)
  → herramienta y workflow (MCP, API, script Python, n8n)
  → recurso (VPS · PC local · estación CAD · GPU cloud)
  → registro + artefacto (PostgreSQL/vault, versión, fuente y costo)
  → revisión/aprobación humana
```

GitHub se representa como repositorio de código, historial de cambios y colaboración; no como MCP dentro del inventario actual. Antigravity se representa como entorno de programación que Sol mencionó, no como un conector verificado en `opencode.json`.

## Fórmula y lenguaje de medición

```text
P = Wᵥ / Tₕ

P  = trabajo útil validado por unidad de atención humana
Wᵥ = entregables que pasan revisión/aceptación
Tₕ = tiempo de intervención humana
```

Registrar además tiempo transcurrido, tiempo de ejecución, tiempo de espera, correcciones y costo. **El dibujo puede mostrar una expansión multiplicativa de líneas de trabajo; la presentación evita afirmar una mejora exponencial demostrada.** El resultado se calibra con el experimento real de productividad y tareas aprobadas.

**Capacidad operativa permanente** significa que PI tiene un gateway, memoria, skills y colas disponibles para iniciar tareas por pedido/evento/agenda, sujeto a servidor, herramientas y permisos disponibles. No significa que todos los agentes o las GPUs ejecuten sin pausa. La contribución humana se mide como intención + criterio + aprobación; la del sistema, como trabajo válido que progresa entre esas intervenciones.

La economía del sistema se registra en partidas separadas: **infraestructura fija** (VPS, red, almacenamiento, backup) · **modelos** (suscripción/API o inferencia local) · **GPU** (imágenes/video por ejecución) · **licencias** (AutoCAD, Rhino, etc.) · **mantenimiento humano** (compatibilidad, pruebas, actualización, soporte). El costo queda visible por ejecución y por mes, en línea con [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#5 · Requerimientos no funcionales|REQUISITOS §5 RNF-10]].

## Evidencia externa para la narrativa

La narrativa separa **hechos documentados**, **tesis de PI** y **proyección de diseño**. Las fuentes respaldan una historia larga de IA, sistemas agénticos, equipos internos de investigación y casos de conocimiento privado; no validan una predicción de productividad exponencial ni que todas las firmas usen un LLM privado.

1. **Andrew Ng y Chuck Whitten, Bain & Company (22-04-2026)**: distinguen copilotos de sistemas que razonan, colaboran y coordinan; Andrew Ng describe el crecimiento de los workflows agentic y plantea que el trabajo humano sigue siendo central. También subraya confiabilidad, datos y checkpoints humanos como trabajo necesario. [Entrevista completa](https://www.bain.com/es-es/insights/winning-in-the-agentic-era-a-conversation-with-andrew-ng).
2. **Anthropic Engineering (19-12-2024)**: separa workflows de agentes y describe patrones de enrutamiento, paralelización y orquestador-trabajadores; aconseja empezar simple, medir resultados y sumar complejidad cuando aporta valor. El artículo advierte que parte del ecosistema descrito ha evolucionado. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
3. **Hermes Agent, documentación oficial (consulta 01-11-2026)**: documenta memoria persistente entre sesiones y tareas programadas en el gateway. Es evidencia de una implementación concreta de capacidades persistentes, no una predicción del conjunto de la industria. [Memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) · [Scheduled Tasks/Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron).
4. **Dartmouth (1955/1956)**: la propuesta de agosto de 1955 convoca el proyecto de verano de 1956 que establece IA como campo de investigación. La formulación precisa para el guion es: “la IA tiene una historia de décadas; los LLM actuales cambian el interfaz y el acceso a construir sistemas”, no que la tecnología haya aparecido ahora. [Historia institucional de Dartmouth](https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth).
5. **Foster + Partners / Ask F+P (Construction Management, 16-04-2024)**: entrevista a Martha Tsigkari documenta una aplicación interna con LLM y búsqueda semántica sobre guías de diseño, además de Stable Diffusion alojado localmente para proponer sobre modelos que el equipo ya diseñó. La entrevista describe Ask F+P en beta. [Entrevista sobre ARD, IA y gemelos digitales](https://constructionmanagement.co.uk/foster-partners-rd-taking-ai-and-digital-twins-to-the-next-stage/).
6. **Zaha Hadid Architects (NVIDIA Customer Story, 2026)**: el caso publicado por NVIDIA describe infraestructura local, archivo de imágenes propietario, modelos/LoRAs ajustados y herramientas internas de producción. Es un caso documentado junto a un proveedor de hardware, no una medida de adopción de todo el mercado. [ZHA + NVIDIA](https://www.nvidia.com/en-us/case-studies/zaha-hadid-architects-with-omniverse-and-usd/).

La ficha del vault [[wiki/glosario/referentes/ia-estudios-internacionales|IA en estudios internacionales]] reúne más ejemplos. La presentación toma los casos anteriores como evidencia específica; separa de ellos la propuesta de PI.

## Alineación 2026-11-02 con VISION / ESTRUCTURA / REQUISITOS

> Verificación punto por punto: nombre PI vs Studio OS aclarado arriba; un Hermes por estudio con perfiles abiertos según [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#10 · Decisiones técnicas|ESTRUCTURA §10]] ADR-1; gobernanza A-D y contrato file_ref según [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#5 · El contrato entre componentes|ESTRUCTURA §5]]; casos C-01 a C-13 y AC en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]; entradas L0-L4 y controles en [[specs/261102-plan-maestro-pi-por-temas|plan maestro T4.1]]; overview en [[specs/261102-system-overview-pi|system overview]]; ingeniería C4 en [[diagramas/pi-system-ingenieria|pi-system-ingenieria]].

## Decisiones de producción

- El video usa el mini guion de Sol como referencia principal cuando lo comparta; hasta entonces los dibujos vectoriales son provisionales.
- La composición se añade a Remotion como `PIStudioOS`; los cambios no pisan la composición de filosofía ni los cambios locales existentes en `Root.tsx`/`tokens.ts`.
- La presentación web conserva fuentes y accesos técnicos para quien quiera profundizar; el video comprime la historia a ocho escenas.
- La interfaz, cada estación y cada línea de agente deben leerse claramente a 1080p: pocos rótulos simultáneos, acercamientos progresivos y conexiones dibujadas por trazos.
- No se instala ninguna librería nueva; se reutiliza Remotion 4.0.533 y `@remotion/transitions` existentes.
