---
tipo: arquitectura
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
tags: [mvp_07, studio-os, estructura, arquitectura, hermes, mcp, tailscale, runpod, seguridad]
idioma: es
---

# ESTRUCTURA — Studio OS

> Cómo se arma el sistema: **dónde vive cada pieza, cómo se conectan y qué límites tienen**. El *qué* y el *para qué* están en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]; las condiciones y la medición, en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]].
> La traducción de esta arquitectura a piezas concretas de Hermes (configuración, flujos, límites verificados) está en [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].
> Detalle técnico fino (SQL, JSON, comandos) sale el día que exista código: acá va la **forma**, no el código.

## Cómo se reparten los tres documentos

|                  | **VISION**                                                                                                                                   | **ESTRUCTURA** (este)                                                                                                                                                                                                      | **REQUISITOS**                                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **La pregunta**  | ¿qué es y para qué?                                                                                                                          | ¿dónde vive y cómo se conecta?                                                                                                                                                                                             | ¿qué tiene que cumplir y cómo se mide?                                                                                                                                |
| **Qué contiene** | el problema · el recorrido · el cuaderno digital · Hermes en conceptual · el stack elegido con sus alternativas · las decisiones de producto | los 4 nodos · dónde vive cada pieza · el agente y sus conexiones · cada integración con sus opciones · el contrato entre componentes · el modelo de datos · seguridad, secretos, backup y acceso remoto · puesta en marcha | alcance · actores · casos de uso · RF y RNF · criterios de aceptación · gobernanza A-D · regla automatizar/persona · métricas · plan de entrega · decisiones abiertas |
|                  |                                                                                                                                              |                                                                                                                                                                                                                            |                                                                                                                                                                       |

- [[#1 · Vista general]]
- [[#2 · Dónde vive cada pieza]]
- [[#3 · El agente]]
- [[#4 · Las integraciones, una por una]]
- [[#5 · El contrato entre componentes]]
- [[#6 · El registro central y el grafo]]
- [[#7 · Seguridad, secretos, backup y acceso remoto]]
- [[#8 · El cuaderno digital: cómo se construye]]
- [[#9 · Puesta en marcha]]
- [[#10 · Decisiones técnicas]]
- [[#11 · Qué NO decide este documento]]

---

# 1 · Vista general

```text
                     ┌─────────── RED PRIVADA (Tailscale / Headscale / NetBird) ───────────┐
                     │                                                                   │
  ┌──────────────────▼───────────────┐   ┌────────────────────┐   ┌───────────────────▼──────────────────┐
  │ N1 · VPS (siempre encendido)      │   │ N2 · PC DEL ESTUDIO│   │ N4 · GPU EN LA NUBE (excepción)      │
  │ Hermes (agente) · n8n · Postgres  │◄─►│ AutoCAD · Rhino    │   │ ComfyUI 24 GB · Runpod Secure       │
  │ Leantime · Redis · Qdrant         │   │ Twinmotion · Unreal│   │ solo material derivado y no sensible  │
  │ Fathom · Cal.com · el vault       │   │ (runner bajo demanda)│  │ 0 puertos · volume cifrado           │
  └───────────────────────────────────┘   └────────────────────┘   └────────────────────────────────────┘
                     ┌────────────────────────────────────────────────────────┐
                     │ N3 · BANCO DE PRUEBAS (esta PC) — stack completo        │
                     │ AutoCAD · Rhino · ComfyUI (RX 570) · Twinmotion · Unreal │
                     │ OpenCode + MCP · el vault · scripts                      │
                     └────────────────────────────────────────────────────────┘
```

**Cuatro lugares, un solo contrato.** El agente no sabe (y no necesita saber) en cuál está ejecutando: lo que cambia es el **perfil** (qué herramienta, qué clase de dato admite, qué costo).

---

# 2 · Dónde vive cada pieza

| Pieza | Dónde | Por qué | Quién la opera |
|---|---|---|---|
| **Hermes** (agente) | VPS, contenedor | siempre encendido, memoria y skills persistentes | PITAUTECH |
| **n8n** (orquestación) | VPS | ya está, con MCP oficial y flujos deterministas | PITAUTECH |
| **PostgreSQL** (registro) | VPS | ya está; el registro necesita consultas | PITAUTECH |
| **Leantime** (proyectos) | VPS | ya está, con su MySQL | PITAUTECH |
| **Fathom** (reuniones) | nube | graba y transcribe; alternativa OSS a evaluar | el estudio |
| **Cal.com** (agenda) | nube ahora → self-hosted después | ya configurado con la cuenta del estudio | el estudio |
| **El vault / la wiki** | repo git, canónico en el VPS + espejo en GitHub | es la memoria y el cuaderno; versionado y append-only | PITAUTECH |
| **Qdrant** (búsqueda semántica) | VPS | ya está; sirve para encontrar por sentido y no por palabra | PITAUTECH |
| **Google Sheets** (clientes) | nube | simple, y alcanza para un estudio chico | el estudio |
| **AutoCAD, Rhino, Twinmotion, Unreal** | PC del estudio | son licencias del estudio y necesitan la máquina | el estudio |
| **ComfyUI** | PC del estudio / esta PC | la GPU del estudio es más chica; para pruebas, esta | el estudio / PITAUTECH |
| **Pod de GPU** | Runpod Secure | los 9B no entran en 8 GB; se prende bajo demanda | PITAUTECH |

---

# 3 · El agente

## 3.1 Cómo se instala

- Imagen oficial `nousresearch/hermes-agent`, comando `gateway run`, en **Docker Swarm vía EasyPanel** (igual que n8n, Leantime y Chatwoot: se actualiza y se revierte como los demás).
- **Volumen nombrado** para `/opt/data` (config, `.env`, sesiones, memoria, skills, cron, `state.db`): nada de bind mount, porque la base usa WAL y un bind sobre 9p/virtiofs se corrompe.
- **Límite de memoria y CPU** (`3 GB` / `2 vCPU`): el VPS tiene 8 GB y siete servicios más; sin tope, el contenedor puede tumbar n8n.
- **Cero puertos publicados**: el gateway de Telegram hace *long polling* (sale, no entra). La API y el dashboard quedan apagados hasta que algo externo los necesite, y entonces van por la red privada.
- **Trampa de Swarm**: los contenedores se llaman `servicio.1.tarea`; `docker exec hermes` no existe. Hay que resolver el ID real primero.

## 3.2 A qué se conecta

| Conexión | Para qué | Nota |
|---|---|---|
| **MCP → n8n** | correr los flujos deterministas (Fathom→minuta→Leantime, digest, agenda) | entrada oficial `n8n-official` contra `https://n8n.pitau.tech/mcp-server/http` |
| **MCP → vault** | leer, buscar, indexar; escribir **solo con aprobación** | es el acceso a la memoria y al cuaderno |
| **MCP → registry** | registrar cada tarea, ejecución, artefacto y aprobación | el registro es el que deja rastro |
| **MCP → runner** | ejecutar sobre los archivos (AutoCAD, Rhino, ComfyUI) | por la red privada, nunca por internet |
| **Chat → Telegram** | la puerta de entrada del estudio | grupos por obra con temas + canal de bitácora |
| **Skills** | los procedimientos escritos | viven en el vault y se publican al volumen |
| **Cron** | recordatorios de compromisos, digest, barridos | lo que corre sin que nadie pregunte |

## 3.3 Qué modelo usa

| Etapa | Modelo | Por qué |
|---|---|---|
| Ahora | **OpenCode Go** (suscripción USD 10) | ya está paga y sirve para el primer tramo |
| Después | **segunda instancia de Hermes en el estudio con Ollama** (modelo local) | el material del estudio no sale de la red |
| Si hace falta | **OpenRouter** con API y precio definidos | capacidad puntual, con el costo a la vista |

**Opciones de modelo local**: Ollama con modelos abiertos (Qwen 3, Llama 3.1). **Dónde vive** (esta PC con 32 GB, el VPS con 8 GB o la nube) es una decisión abierta: en ESTRUCTURA se compara el costo en RAM y la dependencia de que la máquina esté prendida.

## 3.4 Los modos de ejecución

El agente necesita trabajar con archivos que viven en programas de escritorio. Hay cinco formas, y **el sistema no debería notar la diferencia**:

| Modo | Cómo corre | Ideal para | Trampa |
|---|---|---|---|
| **L · Local** | el agente y el programa están en la misma máquina | desarrollo y pruebas | atado a esa máquina |
| **R1 · Puente con la app abierta** | el agente habla con AutoCAD o Rhino por su API, con el programa abierto | lo que el estudio ya hace | el programa tiene que estar abierto |
| **R2 · Headless** | el programa corre sin pantalla (AutoCAD Core Console) | auditorías y publicaciones desatendidas | no todos los programas lo tienen |
| **R3 · Asistido** | el agente prepara el trabajo y la persona lo ejecuta | Twinmotion y todo lo contractual | hay un humano en el medio, y está bien |
| **R4 · Nube** | el trabajo pesado corre en un nodo alquilado | modelos grandes, video | el material sale: solo derivado |

Sobre esos modos se construyen **tres perfiles**: **nube oficial** (herramientas del fabricante), **nube propia** (GPU alquilada) y **local** (la PC del estudio). El contrato de tarea es el mismo en los tres.

---

# 4 · Las integraciones, una por una

## 4.1 AutoCAD (documentación)

| | |
|---|---|
| **Opciones** | **AutoCAD versión completa** (con su Core Console para lo headless) · **FreeCAD** (GPL, también BIM, corre en Linux) · LibreCAD · QCAD · ODA File Converter · ezdxf (solo DXF) |
| **Elegida** | AutoCAD completo en el estudio · FreeCAD como alternativa libre y siempre abierta en la otra PC de desarrollo |
| **Para qué** | auditar DWG (capas, escalas, referencias externas, unidades), preparar sheets, publicar PDF, comparar versiones |
| **Límites** | la versión **LT no habilita la vía cloud** (APS Design Automation); con la versión completa, sí. En la PC del estudio el MCP ya habla con AutoCAD por COM |
| **Trampa conocida** | el LISP de arranque (`acad.lsp`) es incompatible con Core Console y rompe la publicación en segundo plano: hay que aislarlo |

## 4.2 Rhino y Grasshopper (modelo)

| | |
|---|---|
| **Opciones** | **Rhino 8** (ya) · **Rhino 9** (a comparar) + **Hops** · FreeCAD · Blender + Bonsai · OpenSCAD · CadQuery / OCP |
| **Elegida** | Rhino (8 o 9, a comparar) + **Hops** para Grasshopper sin pantalla |
| **Para qué** | inspeccionar el `.3dm`, medir, ejecutar definiciones de Grasshopper, exportar; hoy ya se hacen cortes, tramas y hojas |
| **Límites** | sin la aplicación abierta no hay geometría: de ahí Hops y el runner con watchdog |
| **Pendiente** | diferencias Rhino 8 vs 9 (licencia, versiones, Hops) |

## 4.3 IFC / BIM

| | |
|---|---|
| **Opciones** | **FreeCAD** (módulo BIM) · **IfcOpenShell** (LGPL) + su **IfcMCP** oficial · Bonsai (Blender) · xBIM |
| **Elegida** | FreeCAD + IfcOpenShell |
| **Para qué** | inspeccionar, extraer propiedades, validar y comparar modelos |
| **Límite** | **no hay un IFC real del estudio todavía**: hasta que exista, esto es una hipótesis |

## 4.4 Imágenes (IA)

| | |
|---|---|
| **Opciones** | **ComfyUI** (GPL) + SD 1.5 / SDXL (OpenRAIL) + FLUX.2 klein 4B (Apache 2.0) · versión cloud de Comfy · **Runpod** (GPU en la nube) |
| **Elegida** | ComfyUI local en esta PC (RX 570) para las pruebas → flujos para probar en la infraestructura del estudio (cada 15 días) → cloud de Comfy o Runpod como excepción |
| **Para qué** | render fotorreal, variantes controladas, el flujo Rhino→imagen del concurso |
| **Límites** | los 8 GB no alcanzan para 9B: la GPU en la nube es **la excepción**, no la regla. Los modelos deben tener licencia comercial permisiva |

## 4.5 Visualización

| | |
|---|---|
| **Opciones** | **ComfyUI** (IA) · **Unreal Engine** (gratis hasta 1 M USD de facturación, con MCP oficial, escala a realidad virtual) · Blender · Twinmotion (ya) · Enscape / Lumion |
| **Elegida** | ComfyUI para lo visual con IA · Unreal para lo custom y escalable |
| **Límites** | **Twinmotion no expone API pública**: todo lo que sea automatizar en él es "asistido" (la persona ejecuta) |

## 4.6 Reuniones

| | |
|---|---|
| **Opciones** | **Fathom** (hoy) · **Jitsi** (Apache) o **LiveKit** (MIT) para la llamada + **faster-whisper** (ya, MIT) para transcribir · alternativa open source a Fathom (a verificar) |
| **Elegida** | Fathom mientras no duela |
| **Por qué** | Google Meet corta la grabación; conviene saber cuál es el reemplazo antes de que sea un problema |
| **Detalle** | cuando Fathom repite la misma reunión en varios *meetings*, el agente los agrupa antes de resumir |

## 4.7 Agenda y proyectos

| | |
|---|---|
| **Agenda** | **Cal.com** (gratis ahora → self-hosted con usuarios después, hay que ver cómo se instala) · Proton Cal · Radicale |
| **Proyectos** | **Leantime** (ya, con su MySQL) · Vikunja · Taiga · OpenProject |
| **Decisión** | seguimos con Leantime salvo que se Evaluation |

## 4.8 Datos de clientes y portal

| | |
|---|---|
| **Clientes** | **Google Sheets** (simple y alcanza) · Baserow (MIT) · NocoDB (AGPL) · Directus |
| **Cuaderno y portal** | **Quartz** (MIT) · MkDocs Material · Nextcloud + Pages · Obsidian Publish (pago) |
| **Fotos de obra** | Nextcloud + Memories · Immich · o el vault con tags |
| **Requisito** | el cuaderno tiene que ser **accesible para alguien sin conocimientos técnicos** (Emilia) |

## 4.9 Red privada, acceso remoto y secretos

| | |
|---|---|
| **Red privada** | **Tailscale** (gratis hasta 100 equipos) · **Headscale** (BSD: Tailscale autohospedado) · **NetBird** (BSD) · WireGuard. Hoy se usa Tailscale; la comparación va en §10 |
| **Acceso remoto** | **SSH sobre la red privada** (lo que ya se usa) · Tailscale SSH · MeshCentral (Apache) · RustDesk (AGPL). La opción más segura es la que **no abre puertos al internet**: hoy, SSH por tailnet |
| **Secretos** | las claves de las APIs (Telegram, n8n, Google, Runpod) viven en el `.env` del servicio, con permisos 600, **fuera del repo**: en un repo, una clave se filtra con el primer push |
| **Backup** | copia automática y cifrada de lo que no se puede recuperar (el vault, la base, las configuraciones). **restic** (BSD) o **borg**: incrementales, cifrados y verificables |

---

# 5 · El contrato entre componentes

Todos los componentes hablan el mismo idioma: **un sobre de tarea**. Así el registro, la aprobación y la trazabilidad son iguales para todos.

```json
{
  "task_id": "uuid", "project": "aiz", "tool": "audit_dwg", "verbo": "inspect",
  "input": { "file_ref": "vault://…", "rules_ref": "audit-aiz-v2" },
  "riesgo": "A", "approval": "not_required", "requested_by": "hermes",
  "idem_key": "audit:aiz:cad-u-y:2026-10-28"
}
```

**Reglas que no se rompen**:

| Regla | Por qué |
|---|---|
| El archivo viaja como `file_ref` (una referencia que se resuelve contra el vault), **nunca como ruta** | el modelo no puede elegir un archivo ni escribir donde quiere |
| El verbo define el nivel de riesgo por defecto y **no se puede bajar** | `publish` siempre es D |
| `idem_key` es única | los reintentos no duplican trabajo |
| La respuesta trae `provenance` (versión de entrada, herramienta y versión, parámetros, tiempos, costo) | sin eso no hay auditabilidad |
| Una tarea que no se puede registrar **no se ejecuta** | el registro es requisito previo, no un anexo |

**La respuesta** es siempre estructurada: `status`, `outputs`, `warnings`, `errors`, `provenance`.

---

# 6 · El registro central y el grafo

**Registro** (PostgreSQL, schema propio): lo vivo. **Vault**: lo narrativo (método, decisiones, bitácoras, el cuaderno).

| Entidad | Qué guarda |
|---|---|
| `proyecto` · `archivo` · `version` | qué hay y en qué versión (con hash) |
| `tarea` · `ejecucion` | qué se pidió y qué se ejecutó (perfil, herramienta, parámetros, tiempos, costo) |
| `artefacto` | qué salió (ref, hash, metadata) |
| `relacion` | cómo se conectan: `derived_from` · `depends_on` · `generated_by` · `validated_by` · `approved_by` · `supersedes` |
| `aprobacion` | quién aprobó, cuándo y sobre qué contenido (hash) |

**Un solo escritor**: todo entra por la API del registro. Si alguien escribe directo en la base, se pierde la trazabilidad.

**El grafo** es una vista sobre esas relaciones, no otra base: sirve para una pregunta que ya se hace — *"si cambio el modelo, ¿qué queda desactualizado?"* — y para marcar los dependientes como `stale`.

---

# 7 · Seguridad, secretos, backup y acceso remoto

| Tema | Decisión de estructura |
|---|---|
| **Superficie pública** | el sistema no tiene puertos públicos: todo por la red privada. El dashboard de Hermes exige autenticación y, desde junio 2026, **falla cerrado** si el bind no es local y no hay proveedor de auth (el incidente real: escáneres entraron por dashboards expuestos y plantaron una backdoor SSH) |
| **Privilegios** | credenciales específicas por servicio, de mínimo privilegio; el agente no tiene acceso a las bases internas de n8n ni a los archivos binarios |
| **PI** | el **registro de clases de dato** (plano legal, cálculo, material de cliente, material de concurso, render derivado, modelo) decide si un perfil puede tocar un archivo. Un perfil que no admite esa clase **rechaza la tarea antes de ejecutarla** |
| **Nube** | Runpod exige DPA firmado, confirmación escrita de no-entrenamiento, volume cifrado, 0 puertos y borrado manual. Los *Performance Data* (logs) quedan **fuera** del DPA: lo que llega al pod se trata como expuesto a ese operador |
| **Secretos** | `.env` por servicio, permisos 600, fuera de git. En el repo, una clave se filtra con el primer push |
| **Backup** | restic o borg sobre el vault, la base y las configuraciones; copia **verificable** (una copia que no se probó no es un backup) |
| **Acceso remoto** | SSH por la red privada. Si se necesita acceso desde fuera (soporte), se habilita Tailscale SSH conephemeral keys, no abrir el puerto 22 |

---

# 8 · El cuaderno digital: cómo se construye

**Requisito (de VISION)**: tipo libro, pantalla completa, horizontal, con los croquis escaneados y **ligado a las entradas de la wiki**.

| Pieza | Cómo | Opciones (libres primero) |
|---|---|---|
| **Escaneo** | foto o escaneo → archivo + metadata (fecha, proyecto, tipo) | el propio móvil con una app de escaneo; o el flujo de Hermes con un modelo de visión (Qwen-VL) que etiqueta |
| **Anclaje a la wiki** | cada croquis escaneado queda referenciado desde la entrada del wiki que documenta | enlaces entre `.md` + el índice del vault |
| **Publicación** | el cuaderno se publica como sitio navegable | **Quartz** (MIT) · MkDocs Material · Nextcloud + Pages |
| **Navegación** | índice visual, filtros por proyecto, tipo y fecha | los mismos, más una portada con índice |
| **Interfaz gráfica auxiliar** | lo que se consulta de un vistazo: mapa, filtros, galería | a definir; puede ser la portada del cuaderno |

**El principio**: si el cuaderno vive aparte de la wiki, vuelve a ser un archivo más. Tiene que ser **la capa visual de la wiki**.

---

# 9 · Puesta en marcha

Orden de arranque, con el criterio de cierre de cada tramo. El detalle de comandos vive en el plan de entrega ([[proyectos/MVP_07-studio-os-sistema/REQUISITOS#11 · Plan de entrega|REQUISITOS]]).

| Tramo | Qué se hace | Criterio de cierre |
|---|---|---|
| **T0 · Inventario** | relevar el VPS y el equipo local con un script de solo lectura | números reales de RAM, disco y servicios |
| **T1 · Cimientos del agente** | remoto canónico del vault · red privada · Hermes en el VPS · MCP de n8n · `SOUL` y skills | el agente responde con el vault montado y la memoria persiste tras reiniciar |
| **T2 · Contrato y registro** | schema del registro · API de escritura única · validador del sobre | una tarea real queda registrada con procedencia |
| **T3 · Primer motor** | runner + auditoría de planos | una auditoría de un DWG real del caso AIZ, con hash del original intacto |
| **T4 · Interfase** | Telegram: temas por obra, canal de bitácora, aprobaciones | un pedido desde Telegram y una aprobación que queda registrada |
| **T5 · Imagen y cuaderno** | flujo de render · cuaderno digital en modo mínimo | cuatro variantes con metadata y un cuaderno navegable |
| **T6 · Piloto** | obra, entregas, cliente | el sistema auditado en un proyecto real |

---

# 10 · Decisiones técnicas

Formato Nygard. Las decisiones de **producto** están en [[proyectos/MVP_07-studio-os-sistema/VISION#9 · Las decisiones ya tomadas|VISION §9]]; estas son de construcción.

### ADR · Hermes en el VPS como agente único del estudio

**Contexto.** El vault ya tiene OpenCode con 8 MCP y un bot de Telegram en n8n que agenda, manda digest y sincroniza Fathom. Falta el agente que interprete pedidos y coordine tareas sobre archivos reales. La documentación oficial de Hermes (verificada 28/10/2026) muestra imagen oficial, gateway supervisado por s6, cliente MCP nativo, memoria y skills, y una entrada de catálogo `n8n-official` que conecta con nuestro endpoint. Medición del VPS: 4.858 MB de RAM disponibles.

**Decisión.** Hermes corre en el mismo VPS como servicio Swarm, con límite de 3 GB, sin puertos publicados, con n8n como motor de flujos y el vault como única memoria.

**Alternativas.** *OpenClaw*: más canales pero Node y shell local; la capacidad está en el MCP, el contrato y el índice, no en el shell. *OpenCode + n8n sin Hermes*: resuelve mucho pero no aporta shell ni memoria. *Agente dentro de n8n*: funciona para agenda, pero queda atado a flujos.

**Consecuencias.** *Positivas*: un agente que interpreta y delega con MCP nativo; el producto puede mudarse de VPS a una PC sin reescribir el cerebro. *Negativas*: 3 GB de los 4.858 disponibles (margen real); configuración de MCP duplicada; dos superficies de herramientas. *Riesgos*: doble memoria → el vault manda y las escrituras pasan por el MCP con aprobación; dashboard expuesto → solo red privada con auth.

### ADR · El puente hacia las herramientas de la PC

**Contexto.** AutoCAD, Rhino y ComfyUI se manejan con MCP **stdio** en la máquina donde corren. Con Hermes en el VPS quedan al otro lado de la red. Las operaciones de escritura necesitan que las reglas de riesgo se apliquen **del lado que ejecuta**.

**Decisión.** Dos piezas: **P1** = proxy que convierte los MCP stdio locales en endpoints HTTP streamable en la red privada, para lectura; **P3** = runner propio con API de tareas, para escritura, con validación, nivel de riesgo, copia, aprobación y reversión. **Atajo inicial**: Hermes tiene backend de terminal SSH, así que desde el primer día puede operar la PC del estudio sin construir el proxy; el proxy entra después, cuando las tareas sean llamadas de herramientas y no comandos.

**Alternativas.** *Solo proxy*: deja el control de riesgo en el cliente. *Solo runner*: obliga a reimplementar cada capacidad. *SSH inverso por puerto*: frágil con varios puertos.

**Consecuencias.** *Positivas*: los MCP existentes no se tocan; el runner declara "no disponible" en vez de fallar en silencio. *Negativas*: dos piezas que mantener. *Riesgos*: el puente de Rhino ya se cayó una vez → watchdog con estado explícito; inyección de prompt → el runner no acepta rutas del modelo.

### ADR · El registro vive en PostgreSQL y el vault en el texto

**Contexto.** La trazabilidad de hoy está dispersa: la metadata viaja dentro del PNG de cada render, los informes de auditoría son JSON sueltos en `raw/reports/`, y el método está en markdown.

**Decisión.** Registro híbrido: schema propio en PostgreSQL para lo vivo, con **escritor único** (API del registro); el vault para lo narrativo. Relacional primero; el grafo es una vista sobre las relaciones.

**Alternativas.** *Solo archivos en el vault*: sin consultas entre dominios. *Base de grafos*: el briefing mismo lo pospone. *Solo PostgreSQL*: el texto que ya existe quedaría fuera.

**Consecuencias.** *Positivas*: una consulta responde lo que el norte exige; el vault sigue siendo la memoria legible. *Negativas*: un servicio más y un schema que mantener. *Riesgos*: escrituras directas → prohibidas; divergencia registro/vault → cada artefacto guarda el hash del archivo que referencia; caída del registro → las tareas no se ejecutan.

### ADR · Runpod Secure como excepción de GPU

**Contexto.** Los modelos de 9B no entran en 8 GB. Auditoría de 29 fuentes oficiales (28/10/2026): **no hay cláusula de no-entrenamiento** en ToS, Privacy Policy ni DPA; **el DPA no está firmado por defecto**; los *Performance Data* quedan fuera del DPA; **Community Cloud deja de aceptar hosts** y el cifrado solo aplica a *volume disk*; **Tailscale no está documentado** por Runpod.

**Decisión.** Runpod Secure bajo demanda, con DPA firmado, confirmación escrita de no-entrenamiento, volume cifrado, 0 puertos y borrado manual; **solo material derivado y no sensible**. La alternativa europea (Scaleway/OVHcloud FR, ~€0,75/h) queda anotada como opción de residencia UE.

**Alternativas.** *Community Cloud*: en retirada y peer-to-peer. *Scaleway/OVHcloud FR*: residencia UE y GDPR, precio apenas mayor, sin integración verificada con nuestro stack. *100% local*: inviable con 8 GB.

**Consecuencias.** *Positivas*: 24 GB bajo demanda por segundo, sin capacidad ociosa. *Negativas*: el precio útil se duplica; el DPA y la confirmación escrita bloquean el primer pod si nadie los pide. *Riesgos*: material sensible → prohibido por política; logs fuera del DPA → lo que llega al pod se trata como expuesto.

### ADR · El vault canónico en el VPS

**Contexto.** El vault es un repo git privado que hoy vive en la PC de desarrollo. El agente vive en el VPS y necesita leer y escribirlo; el estudio necesita seguir trabajando en él.

**Decisión.** El VPS es el remoto canónico (repositorio bare + clon de trabajo) y el PC del estudio trabaja contra ese remoto por SSH sobre la red privada. **GitHub privado queda como espejo** y canal de emergencia.

**Alternativas.** *GitHub como canónico*: ata el VPS a un servicio externo. *Sync por Drive*: sin diffs ni atomicidad. *Solo en la PC del estudio*: el agente deja de poder leer cuando la PC está apagada.

**Consecuencias.** *Positivas*: el agente funciona aunque las PCs estén apagadas; una sola verdad con historia. *Negativas*: hay que operar el repositorio bare y la sincronización. *Riesgos*: divergencia entre clones → conflictos explícitos, sin `reset --hard`; force-push → prohibido.

### ADR · Tailscale, y las alternativas que quedan sobre la mesa

**Contexto.** Hace falta una red privada entre el VPS, el banco y la PC del estudio, sin abrir puertos.

**Decisión.** **Tailscale** (gratis hasta 100 equipos, WireGuard, nombres por MagicDNS, Tailscale SSH). **Headscale** (el servidor de Tailscale autohospedado, BSD) queda como opción si el tailnet tiene que ser propio; **NetBird** (BSD) como alternativa con su propia interfaz de gestión.

**Alternativas.** *Cloudflare Tunnel*: expone por HTTP público; útil para portales, no para red privada. *WireGuard puro*: más trabajo de configuración y sin descubrimiento de nombres.

**Consecuencias.** *Positivas*: red en minutos, sin puertos abiertos, acceso por nombre. *Negativas*: dependencia de un servicio de correo para la autenticación del tailnet (Tailscale) — a considerar si eso molesta en un estudio. *Riesgos*: equipos que se caen del tailnet → hay que documentar el reingreso.

---

# 11 · Qué NO decide este documento

- **Las condiciones que cada parte tiene que cumplir y cómo se mide** → [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]
- **El detalle técnico** (SQL, JSON, comandos, plantillas): sale el día que exista código.
- **Las alternativas de producto** (qué hacer, para quién): [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]
