---
tipo: vision
mvp: 07
cliente: Estudio (interno)
proyecto: Studio OS — sistema operativo del estudio de arquitectura
ciudad: CABA
pais: Argentina
fase: especificacion
fecha_inicio: 2026-10-28
fecha_estimada_entrega: s/d
ultima_actualizacion: 2026-10-28
estado: activo
tags: [mvp_07, studio-os, vision, hermes, stack, opensource, free-first, cuaderno-digital]
idioma: es
---

# VISION — Studio OS

> El hilo del sistema: **qué es, para quién, con qué piezas se arma y hacia dónde va**.
> Las decisiones de construcción van en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] y las condiciones que tiene que cumplir cada parte, en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]].
> Base: `raw/docs/plan-hermes.md` (briefing técnico) + lo que ya está instalado en el vault y en el VPS.

## Cómo se reparten los tres documentos

| | **VISION** (este) | **ESTRUCTURA** | **REQUISITOS** |
|---|---|---|---|
| **La pregunta** | ¿qué es y para qué? | ¿dónde vive cada pieza y cómo se conecta? | ¿qué tiene que cumplir y cómo se mide? |
| **Qué contiene** | el problema · el recorrido del trabajo · el cuaderno digital · Hermes en conceptual · el stack elegido con sus alternativas · las decisiones de producto | los 4 nodos · el agente y cómo se instala · cada integración con sus opciones · el contrato común · el registro y el grafo · seguridad, secretos, backup y acceso remoto | alcance · actores y permisos · casos de uso como historias · RF y RNF con trazabilidad · criterios de aceptación · gobernanza A-D · métricas · plan por fases |
| **Qué NO contiene** | detalle técnico (SQL, JSON, comandos) | las condiciones de aceptación | el relato |

- [[#1 · Qué es y por qué]]
- [[#2 · El recorrido del trabajo del estudio]]
- [[#3 · El cuaderno digital]]
- [[#4 · Hermes, conceptualmente]]
- [[#5 · El stack delineado]]
- [[#6 · Principios, habilidades, modos, riesgos, camino y preguntas]]

El cuarto documento, [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]], baja los tres a piezas reales de Hermes: qué se configura, qué flujo cubre cada pieza y qué no puede hacer. La ruta de lectura por tema está en [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]].

---

# 1 · Qué es y por qué

## 1.1 Qué es

**Studio OS** es el sistema que le falta a un estudio de arquitectura para trabajar como se trabaja en un estudio grande, pero con el costo de un estudio chico.

Une **AutoCAD, Rhino, Grasshopper, Twinmotion, Unreal y ComfyUI** con la vida real del estudio —las reuniones, las decisiones, la obra— de modo que **cada plano, modelo, render y acta quede atado a su origen, a su versión y a quien lo aprobó**, y una IA (**Hermes**) ejecute el trabajo repetitivo dejando las decisiones en manos del arquitecto.

No es un producto para un cliente puntual: es la **base replicable** que PITAUTECH vende como servicio, con el estudio de Emilia Pimenta como piloto.

## 1.2 Para quién

| | |
|---|---|
| **El estudio** (2-4 personas) | dibuja, modela, renderiza, entrega y va a obra. Quiere trabajar mejor sin volverse técnicos |
| **PITAUTECH** | opera el sistema: instala, mantiene y hace que ande |
| **El arquitecto** | es el que decide. El sistema ejecuta, pero no elige por él |

## 1.3 El problema

**El problema de hoy es que las soluciones son de herramientas y no de sistemas.** Cada programa resuelve su parte y nadie los une. Y en arquitectura el trabajo **es un sistema**: entradas → decisiones → planos → modelo → imagen → entrega → obra. Hoy ese sistema existe solo en la cabeza de las personas, y se rompe en tres lados:

1. **Comunicación.** Las decisiones se toman en reuniones y mensajes. Quien llega tarde, o entra como junior, tiene que reconstruir todo desde cero preguntando.
2. **Auditabilidad.** No se sabe de qué archivo salió un resultado, con qué versión se hizo ni quién lo aprobó. Un plano es un documento legal: sin trazabilidad no hay defensa.
3. **Conocimiento.** El conocimiento de la casa está en los seniors. Si un junior tiene que preguntar todo, **el senior pierde horas que debería estar cobrando como diseño y no como transferencia de lo que ya sabe**. Ahí se despartician recursos.

Por eso el sistema no es "una IA que ayuda": es un **sistema con memoria, registro y reglas**.

## 1.4 El norte (el único criterio de éxito)

> **Un resultado sirve si se puede explica**: de qué archivo salió, con qué versión, con qué herramienta y con qué parámetros se hizo, y quién lo aprobó.

Si eso no está, el resultado no cuenta, por lindo que sea. Ese criterio decide el orden de todo lo demás.

## 1.5 La segunda pregunta (la del junior)

> **¿Cuánto cuesta que un junior pueda trabajar como un senior?**

En horas del senior que se ahorran. Es la métrica que importa: el estudio no crece por tener más gente, crece porque la gente nueva llega más rápido a la calidad de la gente vieja.

---

# 2 · El recorrido del trabajo del estudio

Así trabaja hoy un estudio de arquitectura, paso por paso, y qué hace el sistema en cada uno.

| Paso | Cómo se hace hoy | Qué hace el sistema | Quién decide |
|---|---|---|---|
| **1 · Entra un cliente** | mensaje suelto (referido, IG, WhatsApp) | **mini CRM**: una hoja con nombre, contacto y mail (Instagram a futuro). El agente lo agrega solo | la titular |
| **2 · Reunión** | Meet + Fathom | Fathom graba y transcribe. Cuando la misma reunión aparece repetida en varios *meetings*, el agente **los agrupa**. Sale una minuta con lo decidido | la titular |
| **3 · Compromisos** | quedan en el chat | cada compromiso queda con **qué hay que entregar y con qué fecha**. El agente avisa por Telegram antes de que venza, y arma el mail con el formato del estudio | la titular (el mail lo manda una persona) |
| **4 · El cuaderno** | carpetas sueltas + memoria | **cuaderno digital**: escalas investigadas, croquis personales, resultados de la IA y qué documentación hay, cada cosa en su carpeta y con su referencia | el arquitecto |
| **5 · Documentación (planos)** | AutoCAD a mano, publicar PDF | **auditoría** del DWG (capas, escalas, referencias, unidades) y publicación con registro; el original no se toca | el arquitecto (nivel D: aprueba) |
| **6 · Modelo 3D** | Rhino a mano: cortes, tramas, hoja | inspección y medición del modelo, ejecutar Grasshopper (por **Hops**, sin pantalla), exportar | el arquitecto |
| **7 · Render / imagen IA** | prompts a mano en el ComfyUI | un **agente experto en ComfyUI** con sus skills: prepara el trabajo con sus parámetros y semilla, y deja las iteraciones en un **portal** (por mail pesan demasiado) | el arquitecto |
| **8 · Obra** | fotos sueltas en el celular | visita de obra: fotos indexadas con tags, e incidencias con su resolución | el arquitecto |
| **9 · Entregas** | PDF + mail | el agente arma el paquete; **la persona escribe el mail y adjunta**. Queda registro de la entrega con su fecha | el arquitecto (nivel D) |
| **10 · Memoria** | en la cabeza de cada uno | la **memoria del sistema**: cada sesión deja entidades, topics y hechos, y **Hermes la mejora** | el estudio |

**Lo que se ve en la tabla**: el agente entra en 8 de los 10 pasos. **En ninguno decide el criterio**: prepara, ejecuta lo verificable y devuelve la decisión.

---

# 3 · El cuaderno digital

Es **un desarrollo interno nuestro** (no del proveedor): la primera versión la hacemos nosotros. Es la pieza que convierte conocimiento personal en conocimiento de la casa.

## 3.1 Qué es

Un cuaderno digital de todo lo que el estudio piensa, dibuja, mide y genera, con **visualización tipo libro: a pantalla completa, en sentido horizontal**, para poder recorrer en orden cómo se fue hablando, planeando y dibujando.

| | |
|---|---|
| **La parte manual** | del arquitecto: los croquis a mano, las escalas que investigó, las decisiones, las correcciones |
| **La parte automatizada** | de Hermes: escanear, indexar, etiquetar, conectar, resumir y devolver |

## 3.2 Cómo se ve

- **Tipo libro, pantalla completa, horizontal**: se recorre como se recorre un cuaderno, no como se recorre una carpeta.
- **Croquis escaneados** como contenido de primera clase, no como anexos.
- **Ligado a la wiki**: el cuaderno es la **capa visual de la wiki**, no un sitio aparte. Cada croquis escaneado cuelga de la entrada de la wiki que documenta (un proyecto, un material, una decisión). Si la wiki es el texto, el cuaderno es la lámina.
- **Una interfaz gráfica auxiliar** para navegarlo: índice visual, filtros por proyecto, por tipo, por fecha.

## 3.3 Por qué

1. **Digitalizar el cuaderno convierte el conocimiento personal en conocimiento de la casa**: hoy el cuaderno del arquitecto se va con el arquitecto.
2. **El escaneo de croquis es lo que hoy se pierde**: es la información más barata de capturar y la más cara de reconstruir.
3. **Con la wiki detrás, el cuaderno se vuelve consultable**: "¿qué croquis tengo deCover de timber?" y la respuesta aparece con su contexto.
4. **El agente lo mejora**: cada sesión deja entidades, topics y hechos; el cuaderno crece sin que nadie lo ordene a mano.

**Cómo se construye** (escaneo, anclaje a la wiki, publicación e interfaz de navegación) está en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#8 · El cuaderno digital: cómo se construye|ESTRUCTURA §8]].

## 3.4 Referencia

[El hábito de Leonardo da Vinci que me ha quitado el móvil de las manos — *Commonplace book*](https://www.youtube.com/watch?v=A2S-lzsb3gw) (Maialen Lleó, 12:35). El vault ya tenía esta idea anotada como proyecto: *"#14 davinci-notebook: cuaderno digital tipo Da Vinci con todo"*.

---

# 4 · Hermes, conceptualmente

## 4.1 Qué es

**Hermes** (Nous Research, licencia MIT) es un **agente**: un programa que recibe un objetivo en lenguaje natural, lo interpreta, elige qué herramientas usar, recuerda lo que aprendió y puede delegar partes a subagentes.

No es un chat con IA: es un **proceso con memoria y herramientas**, que se instala en Docker y sigue andando.

## 4.2 Qué hace

| Capacidad | En la práctica |
|---|---|
| **Interpretar** | convierte "auditá el DWG de AIZ" en pasos concretos con sus datos |
| **Usar herramientas** | llama a las herramientas por **MCP** (AutoCAD, Rhino, ComfyUI, n8n, el vault, el registro) |
| **Recordar** | memoria persistente por proyecto + el **cuaderno digital** como memoria real del estudio |
| **Ejecutar procedimientos** | **skills**: recetas escritas (auditar documentación CAD, comparar versiones, preparar una entrega, ser experto en ComfyUI) |
| **Delegar** | reparte partes a subagentes cuando conviene |
| **Trabajar solo** | **cron**: tareas programadas (el digest de las 07:00, los recordatorios de compromisos, los barridos) |

## 4.3 Cómo se conecta

Se conecta por **MCP** (las herramientas), por **chat** (Telegram, la puerta del día a día), por **skills** (los procedimientos escritos) y por **cron** (lo que corre solo). El detalle de cada conexión está en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3 · El agente|ESTRUCTURA §3]].

## 4.4 Qué NO hace (y no va a hacer)

- No inventa herramientas, endpoints ni capacidades: si algo no existe, lo dice.
- No ejecuta nada de riesgo sin que alguien lo apruebe.
- No modifica un archivo original: escribe aparte y deja el original intacto.
- No es la memoria: la memoria es el cuaderno digital. La memoria de Hermes es de trabajo.
- No decide el criterio del arquitecto.

## 4.5 Por qué Hermes y no otras opciones

| Alternativa | Por qué no |
|---|---|
| **OpenClaw** (MIT) | muchos canales y gateway local, pero es Node y su memoria vive en su propia app. El veredicto del vault fue que **la capacidad está en el MCP, el contrato y el índice, no en el shell**. Hermes es más parecido a lo que ya somos (n8n + Telegram + vault + agentes) |
| **Claude Code / Codex** | muy buenos escribiendo código, pero **cerrados**: no se pueden hostear en el VPS del estudio, no tienen memoria ni gateway multiusuario, y el material del estudio no puede pasar por ellos |
| **Un agente dentro de n8n** (LIDIA V5) | ya funciona para la agenda, pero queda atado a flujos: no escala a tareas sobre archivos ni a memoria |

**Y una aclaración de roles**: nosotros, para el desarrollo propio, seguimos usando **OpenCode** (+ Antigravity). Eso es una herramienta de desarrollo. **De cara al cliente, el agente es Hermes.**

## 4.6 Qué modelo usa

**Hoy: OpenCode Go** (la suscripción de USD 10). **Después: una segunda instancia de Hermes en el estudio, con Ollama** (modelo local), para que el material del estudio no salga de la red. **Si hace falta: OpenRouter** con una API y un precio definidos, solo para lo que justifique cloud. La comparación y las condiciones, en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3 · El agente|ESTRUCTURA §3.3]].

---

# 5 · El stack delineado

Una fila por pieza. **Siempre primero las alternativas libres y open source**; el criterio es: se elige la libre salvo que el estudio ya tenga la licencia pagada y la alternativa no dé lo mismo.

| Pieza | Alternativas (libres / open source primero) | Elegida hoy | Costo y licencia |
|---|---|---|---|
| **Agente (cara al cliente)** | **Hermes** (MIT) · OpenClaw (MIT) · Claude Code / Codex (cerrados) | **Hermes** | gratis, MIT, se hospeda en el VPS |
| **Herramienta de desarrollo (nuestra)** | **OpenCode** (+ Antigravity) | **OpenCode** | tu suscripción |
| **Modelos de lenguaje** | **Ollama** + modelos abiertos (Qwen 3, Llama 3.1) · **OpenRouter** (API) · **OpenCode Go** (suscripción) | **OpenCode Go** hoy → Ollama en el estudio → OpenRouter si hace falta | de USD 10/mes a USD 0 |
| **Imágenes (IA)** | **ComfyUI** (GPL) + SD 1.5 / SDXL (OpenRAIL) + FLUX.2 klein 4B (Apache 2.0) · versión cloud de Comfy · **Runpod** (GPU en la nube) | **ComfyUI local en esta PC (RX 570)** para las pruebas; después, flujos para probar en la infraestructura del estudio (cada 15 días) y, si hace falta, cloud de Comfy o Runpod | gratis; la nube es excepción |
| **Orquestación** | **Node-RED** (Apache) · Windmill (AGPL) · **n8n** (self-hosted gratis) | **n8n** | gratis |
| **Red privada** | **Tailscale** (gratis hasta 100 equipos) · **Headscale** (BSD: Tailscale autohospedado) · **NetBird** (BSD) · WireGuard | **Tailscale**; Headscale y NetBird se comparan en ESTRUCTURA | gratis |
| **Registro de datos** | **PostgreSQL** (ya) · MySQL/MariaDB (el de Leantime) · SQLite · DuckDB · Neo4j (grafo) | **PostgreSQL** para el registro + **MySQL** de Leantime | gratis |
| **Gestor de proyectos** | **Leantime** (ya) · Vikunja (AGPL) · Taiga (AGPL) · OpenProject (GPL) | **Leantime** | gratis |
| **Búsqueda semántica** | **Qdrant** (Apache 2.0, ya) · sqlite-vec (MIT) · Meilisearch (MIT) | Qdrant — **para qué sirve se define en ESTRUCTURA** | gratis |
| **CAD 2D y 3D** | **AutoCAD versión completa** (+ su Core Console para lo headless) · **FreeCAD** (GPL, también BIM, corre en Linux) · LibreCAD (GPL) · QCAD (GPL) · ODA File Converter (gratis) · ezdxf (MIT, solo DXF) | **AutoCAD completo** en el estudio · **FreeCAD** como opción libre y siempre abierta, en la otra PC de desarrollo (Linux) | AutoCAD: licencia del estudio · FreeCAD: gratis |
| **3D y paramétrico** | **Rhino 8** (ya) · **Rhino 9** (a comparar) + **Hops** (Grasshopper sin pantalla) · FreeCAD · Blender + Bonsai · OpenSCAD · CadQuery / OCP | **Rhino** (+ Hops), y comparar Rhino 8 contra Rhino 9 | licencia del estudio |
| **BIM / IFC** | **FreeCAD** (módulo BIM) · **IfcOpenShell** (LGPL) + su IfcMCP · Bonsai (Blender) · xBIM (MIT) | **FreeCAD** + IfcOpenShell | gratis |
| **Visualización** | **ComfyUI** (IA) · **Unreal Engine** (gratis hasta 1 M USD de facturación, con MCP oficial, escala a realidad virtual) · Blender · Twinmotion (ya) · Enscape / Lumion | **ComfyUI** para lo visual con IA · **Unreal** para lo custom y escalable | gratis |
| **Reuniones** | **Jitsi** (Apache) o **LiveKit** (MIT) para la llamada · **faster-whisper** (ya, MIT) para transcribir · alternativa open source a Fathom (a verificar) | **Fathom** hoy (Google Meet corta la grabación: hay alternativa) | free tier |
| **Agenda** | **Cal.com** (self-hosted gratis) · Proton Cal · **Radicale** (GPL) | **Cal.com** gratis ahora; **self-hosted con usuarios** después (a instalar) | gratis |
| **Chat con el estudio** | **Telegram** (canales y temas) · **Discord** (canales e hilos) · Mattermost (MIT) | **Telegram**; **Discord** cuando lo que se comparte es visual (ver §6.5) | gratis |
| **Clientes (datos)** | **Google Sheets** (gratis) · **Baserow** (MIT) · **NocoDB** (AGPL) · Directus (AGPL) | **Google Sheets** (simple); alternativa self-hosted si empieza a doler | gratis |
| **Cuaderno digital (publicación)** | **Quartz** (MIT) · MkDocs Material (MIT) · Nextcloud + Pages · Obsidian Publish (pago) · SilverBullet / Joplin | a definir en ESTRUCTURA, con el requisito: **público, tipo libro, sin conocimientos técnicos** | gratis |
| **Portal de iteraciones** | Quartz / MkDocs · **PhotoPrism** (AGPL) · **Piwigo** · Nextcloud + Memories | Quartz sobre el índice de renders | gratis |
| **Fotos de obra** | Nextcloud + Memories (búsqueda y tags) · **Immich** (AGPL) | a definir (§6.8) | gratis, self-hosted |
| **Visión por computadora** | **Qwen-VL** (Apache 2.0) en Ollama · **CLIP / SigLIP** (Apache/MIT) · **exiftool** (libre) · **OpenCV** (Apache 2.0) | a definir (§6.8) | gratis, local |
| **Correo al cliente** | plantillas en el vault + **Gmail API** · nodo de email de n8n | Hermes redacta; lo manda una persona o el propio Hermes con aprobación previa | gratis |
| **Chatwoot · Instagram · WhatsApp** | — | **no se usan por ahora** | — |

**Las cuatro notas honestas de esta tabla:**

1. **Lo que el estudio ya paga** (AutoCAD, Rhino, Twinmotion) se mantiene: cambiarlas es tirar plata y método. Lo que se busca es que **el resto del sistema sea libre**.
2. **AutoCAD versión completa** (en lugar de LT) además habilita la vía cloud oficial para el trabajo desatendido. Es un cambio de licencia con consecuencias.
3. **Lo más caro del sistema no es la licencia: es la GPU** (y el modelo). Los 8 GB de la máquina no alcanzan para los modelos de 9B, así que hay una excepción de pago, y conviene que sea la excepción y no la regla.
4. **Cuaderno, portal y fotos pueden salir gratis** y con software libre: son páginas y carpetas, no productos.

**Lo que sale de esta tabla y va a ESTRUCTURA** (porque es *cómo se implementa*, no *qué es*): secretos, backup, acceso remoto y la comparación Headscale/NetBird/Tailscale.

---

# 6 · Principios, habilidades, modos, riesgos, camino y preguntas

## 6.1 Los principios

1. **Libre y open source cuando se pueda.** Cada pieza elige la opción libre salvo que el estudio ya tenga la licencia pagada o que no exista alternativa equivalente.
2. **Automatización antes que IA.** Lo repetible y verificable se resuelve con código determinista. La IA interpreta, clasifica y propone.
3. **Human-in-the-loop.** Toda decisión de diseño, todo cambio con impacto contractual y toda emisión definitiva la aprueba una persona.
4. **Trazabilidad y auditabilidad.** Cada resultado se puede relacionar con su archivo, versión, parámetros, herramienta, fecha, responsable y aprobaciones. Y **el conocimiento de la casa** queda accesible para cualquiera del equipo.
5. **Interoperabilidad.** Formatos abiertos (IFC, glTF, SVG, Markdown) y no atarse a un solo proveedor.
6. **Arquitectura modular.** Cada pieza se puede cambiar sin reconstruir el sistema.
7. **Seguridad y privacidad.** Se decide qué sale del entorno del estudio y qué no. Los planos son documento legal: no salen.
8. **Reproducibilidad.** Un proceso se puede volver a ejecutar con los mismos parámetros y dar un resultado comparable.
9. **Escalabilidad progresiva.** Se empieza con un MVP chico y se amplía con pruebas reales.

## 6.2 La regla de automatizar vs. hacerlas a mano

**Se automatiza el trabajo, no la responsabilidad.** El agente hace el trabajo repetible y verificable; las personas deciden, se comunican con el cliente y se hacen cargo. Y el filtro es económico: **se automatiza lo que se repite**.

La matriz completa (qué hace el agente, qué hace la gente y por qué) está en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#8 · Qué automatiza el agente y qué hace la gente|REQUISITOS §8]].

## 6.3 Las habilidades (procedimientos escritos del agente)

Cada habilidad es un archivo con: objetivo, entradas, herramientas autorizadas, precondiciones, procedimiento, criterio de validación, permisos, formato de salida, errores y evidencias.

**Del cliente y la relación**

| Habilidad | Qué resuelve |
|---|---|
| `gestionar-clientes` | alta y seguimiento mínimo: nombre, contacto, mail, y qué se le entregó |
| `preparar-compromisos` | convierte una reunión en compromisos con **qué entregar y con qué fecha**, y arma el recordatorio |
| `redactar-correo-cliente` | arma el mail con el formato del estudio a partir de los compromisos (lo manda una persona) |

**Del trabajo de diseño**

| Habilidad | Qué resuelve |
|---|---|
| `auditar-documentacion-cad` | auditar un DWG/DXF contra las reglas del estudio y devolver observaciones clasificadas, sin tocar el original |
| `comparar-versiones-de-documentacion` | qué cambió entre dos versiones de un juego de planos |
| `preparar-entrega-de-proyecto` | armar el paquete de entrega con su índice y su evidencia |
| `validar-modelo-ifc` | revisar un modelo BIM (entra cuando haya un IFC real del estudio) |
| `experto-comfyui` | el agente como especialista en ComfyUI: prepara el trabajo, controla parámetros y registra cada corrida |
| `publicar-iteraciones` | deja las iteraciones de render en el portal, con sus parámetros y su semilla |

**De la obra y el conocimiento**

| Habilidad | Qué resuelve |
|---|---|
| `documentar-visita-de-obra` | visita de obra: fecha, fotos con tags, incidencias y su resolución |
| `curar-cuaderno` | mantiene el cuaderno digital: escanea, indexa, etiqueta, conecta y devuelve lo que hay |
| `diagnosticar-proyecto-arquitectonico` | "¿qué sé de este proyecto?" armando lo que hay en la wiki |

## 6.4 Los modos de ejecución

Hay **cinco formas** de que el agente trabaje con archivos que viven en programas de escritorio: en la misma máquina, con el programa abierto, sin pantalla, asistido por una persona, o en la nube. El detalle de cada modo y los tres perfiles que se construyen sobre ellos están en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#3 · El agente|ESTRUCTURA §3.4]].

**Lo que importa acá es el principio**: el sistema **no debería notar la diferencia** entre un modo y otro. El contrato de tarea es el mismo, y lo único que cambia es el perfil (qué herramienta, qué clase de dato admite, qué costo).

## 6.5 Cuándo Telegram y cuándo Discord

**Telegram** es el chat de trabajo interno: avisos, aprobaciones, recordatorios y preguntas al agente, ordenados en grupos por obra con **temas** por frente. **Discord** es para conversaciones con material **visual** compartido (iteraciones de render), con gente fuera del estudio, ordenadas en canales e hilos.

**Regla**: una sola superficie por tipo de conversación. El mismo tema no se duplica en las dos. La comparación con las alternativas libres está en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#4 · Las integraciones, una por una|ESTRUCTURA §4.8]].

## 6.6 Los niveles de riesgo (la regla de gobierno)

**A** lectura (automático) · **B** generación aislada (automático, en carpeta controlada) · **C** modificación (**con aprobación**) · **D** publicación o acción externa (**con aprobación explícita**).

El nivel lo define la operación, no el agente. Lo que se permite en cada nivel, qué evidencia queda y cómo se revoca, está en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo|REQUISITOS §7]].

## 6.7 El camino en tres tramos

| Tramo | Qué pasa | Por qué en ese orden |
|---|---|---|
| **1 · Cimientos** | inventario real del entorno · el agente instalado y con memoria · las primeras herramientas de solo lectura · el registro que deja rastro | sin esto no hay nada que mostrar ni nada que auditar |
| **2 · Motores** | AutoCAD · Rhino/Grasshopper · ComfyUI · el flujo de render · los compromisos con fecha | son los programas con los que el estudio trabaja hoy |
| **3 · Sistema** | el cuaderno digital a fondo · Twinmotion · IFC · el registro con grafo · el piloto en un proyecto real | recién acá deja de ser un conjunto de automatizaciones y pasa a ser un sistema auditable |

El plan detallado, con criterios de entrada y salida por tramo, está en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#11 · Plan de entrega|REQUISITOS §11]].

## 6.8 Las preguntas abiertas (las de producto)

| # | Pregunta | Opciones |
|---|---|---|
| 1 | **Qué se automatiza primero**: la auditoría de planos · los compromisos con fecha · el cuaderno digital · la documentación de obra | la que más duela hoy en el estudio |
| 2 | **Cómo se publica el cuaderno** para que lo use Emilia sin conocimientos técnicos | Quartz · MkDocs · Nextcloud + Pages · otro |
| 3 | **Qué pasa con las fotos de obra**: modelo de visión local que etiqueta y propone incidencias · solo EXIF y tags manuales · dejarlo para más adelante | a definir con el piloto |

Las decisiones de construcción (dónde vive el modelo, si n8n se queda, red privada, Rhino 8 vs 9, el DPA de Runpod) están en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#10 · Decisiones abiertas|REQUISITOS §10]], con su impacto y el momento en que hay que tomarlas.

## 6.9 Las decisiones ya tomadas

| Decisión | Fecha |
|---|---|
| El producto se llama **Studio OS** y es replicable; el piloto es el estudio de Emilia | 28/10/2026 |
| **Hermes** es el agente de cara al cliente (OpenCode es para nuestro desarrollo) | 28/10/2026 |
| **n8n** como orquestador | 28/10/2026 |
| **AutoCAD versión completa** (no LT) | 28/10/2026 |
| **Un agente por estudio** (no uno por persona) | 28/10/2026 |
| **Telegram** como interfase del día a día; Discord para lo visual | 28/10/2026 |
| **Registro híbrido**: PostgreSQL para lo vivo, vault para lo narrativo | 28/10/2026 |
| **Runpod Secure** como excepción de GPU, con condiciones previas | 28/10/2026 |
| El **cuaderno digital** es un desarrollo interno, tipo libro, ligado a la wiki | 28/10/2026 |
| El "CRM" es **una hoja**, no un CRM | 28/10/2026 |
| Los compromisos llevan **fecha** y avisan por **Telegram** | 28/10/2026 |
| Las iteraciones de render van a un **portal**, no por mail | 28/10/2026 |
| Las **entregas las manda una persona**: el sistema prepara y deja registro | 28/10/2026 |
| **Chatwoot, Instagram y WhatsApp** quedan fuera por ahora | 28/10/2026 |

## 6.10 Qué NO decide este documento

- **Dónde vive cada pieza ni cómo se conecta** (incluye secretos, backup, acceso remoto y la comparación Tailscale / Headscale / NetBird) → [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]]
- **Qué condiciones tiene que cumplir cada parte y cómo se mide** → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]
- **El detalle técnico** (contratos, tablas, código): sale el día que exista código.
