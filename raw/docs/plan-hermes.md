# PITAUTECH / pitauOS

## Briefing técnico para agentes de OpenCode

### Integración de Hermes Agent con automatización, CAD, modelado 3D, BIM, visualización y documentación de obra

**Estado:** propuesta de arquitectura técnica en fase de investigación y diseño de MVP.  
**Objetivo:** convertir herramientas y procesos dispersos de un estudio de arquitectura en un sistema de trabajo integrado, trazable y progresivamente automatizable.

---

# 1\. CONTEXTO DEL PROYECTO

Estamos desarrollando una arquitectura tecnológica para asistir a un estudio de arquitectura que realiza:

- Diseño arquitectónico y documentación técnica.
- Dibujo 2D y modelado 3D.
- Modelado paramétrico y geometría computacional.
- BIM y coordinación de información.
- Renders, imágenes, animaciones y videos.
- Documentación, cómputos y presupuestos.
- Seguimiento y documentación de obra.
- Gestión de archivos, comunicaciones y entregables.
- Difusión, presentaciones y contenido audiovisual.

La intención es investigar cómo conectar estas actividades mediante agentes de IA, automatizaciones, APIs, scripts, protocolos MCP y herramientas open source.

La solución debe priorizar la reutilización de herramientas existentes y desarrollar integraciones propias únicamente cuando aporten una capacidad concreta que no esté resuelta.

## Principios rectores

1. **Automatización antes que intervención innecesaria de IA.** Resolver con código determinista las tareas repetitivas y verificables; utilizar modelos de IA para interpretación, clasificación, planificación, generación y resolución de ambigüedades.
2. **Human-in-the-loop.** Las decisiones de diseño, los cambios con impacto contractual, las modificaciones destructivas y la emisión definitiva de documentación deben disponer de aprobación humana según su nivel de riesgo.
3. **Trazabilidad.** Cada resultado debe poder relacionarse con sus archivos de origen, versión, parámetros, herramientas, fecha, responsable y aprobaciones.
4. **Interoperabilidad.** Favorecer estándares abiertos, especialmente IFC, y evitar dependencias innecesarias de un único proveedor.
5. **Arquitectura modular.** Cada herramienta especializada debe poder sustituirse sin reconstruir todo el sistema.
6. **Seguridad y privacidad.** Restringir accesos, aislar servicios, gestionar secretos correctamente y decidir qué información sale del entorno local.
7. **Reproducibilidad.** Los procesos deben poder ejecutarse nuevamente con parámetros conocidos y producir resultados comparables.
8. **Escalabilidad progresiva.** Comenzar con un MVP pequeño y ampliar las capacidades a partir de pruebas reales.

---

# 2\. ENTORNO TECNOLÓGICO CONOCIDO

## Infraestructura existente

- VPS de Contabo.
- Docker para ejecutar servicios.
- n8n autohospedado, versión conocida 2.8.3.
- Chatwoot.
- Panel de administración.
- Dominio de n8n: `n8n.pitau.tech`.
- Correo corporativo alojado en DonWeb.
- Equipo local con 32 GB de RAM DDR3 y GPU AMD de 8 GB, sin NVIDIA.
- Ollama instalado o utilizado para ejecutar modelos locales.

Modelos mencionados previamente:

- `llama3.2`
- `llama3.1:8b`
- `nomic-embed-text`

Este inventario es información de contexto, no una garantía de que todos los componentes sigan instalados o configurados exactamente igual. Verificar el estado actual antes de realizar cambios.

## Información pendiente de relevamiento

Antes de dimensionar el despliegue, inspeccionar:

- RAM, CPU, disco y sistema operativo del VPS.
- Contenedores activos, redes, volúmenes y consumo de recursos.
- Configuración de proxy inverso, TLS y dominios.
- Versiones actuales de n8n y Chatwoot.
- Base de datos real utilizada por cada servicio.
- Backups, política de actualización y recuperación.
- Acceso SSH y mecanismos actuales de administración.
- Versiones de AutoCAD, Rhino, Grasshopper, Twinmotion y ComfyUI.
- Sistema operativo y conectividad del equipo local.
- Disponibilidad de APIs, SDK, MCP y permisos en cada herramienta.

No sobrescribir configuraciones ni reiniciar servicios productivos sin revisar dependencias y preparar un procedimiento de reversión.

---

# 3\. ARQUITECTURA CONCEPTUAL

La propuesta separa la inteligencia que planifica, la automatización que ejecuta procesos y los motores especializados que trabajan con los archivos.

``` text
USUARIO / EQUIPO DEL ESTUDIO
             |
             v
   INTERFAZ DE INTERACCIÓN
 Telegram / chat / interfaz web
             |
             v
       HERMES AGENT
 Interpretación, planificación,
 herramientas, memoria y delegación
             |
             v
      CAPA DE INTEGRACIÓN
     MCP / APIs / adaptadores
             |
       +-----+------------------+
       |                        |
       v                        v
      n8n               SERVICIOS PROPIOS
 Flujos de negocio      Scripts / workers
 Notificaciones        Colas / validadores
       |                        |
       +------------+-----------+
                    |
                    v
       MOTORES ESPECIALIZADOS
       |          |          |
       v          v          v
    AutoCAD     Rhino      ComfyUI
       |       Grasshopper    |
       v          |           v
  Planos DWG      v       Imágenes
  PDF, tablas   Geometría   Variantes
                  |
                  v
             IFC / BIM
                  |
                  v
        Twinmotion / video
                    |
                    v
       REGISTRO DE PROYECTO
 Versiones / fuentes / resultados /
 parámetros / incidencias / aprobaciones
```

El diagrama expresa una arquitectura objetivo, no integraciones que ya estén implementadas.

## Responsabilidad de cada componente

### Hermes Agent

Actúa como agente orquestador: recibe objetivos, interpreta instrucciones, planifica pasos, selecciona herramientas, utiliza contexto y memoria, delega tareas cuando resulta útil y presenta resultados.

La documentación oficial describe ejecución de herramientas, terminal, archivos, navegación web, subagentes, tareas programadas y extensiones mediante MCP.

Documentación:
https://hermes-agent.nousresearch.com/docs

### n8n

Orquesta procesos definidos y repetibles:

- Recibir eventos y solicitudes.
- Coordinar secuencias de servicios.
- Aplicar reglas de negocio.
- Gestionar reintentos y errores.
- Enviar notificaciones.
- Registrar estados.
- Conectar sistemas externos.

Hermes y n8n son complementarios. No es necesario convertir cada flujo de n8n en una habilidad autónoma del agente ni delegar al modelo tareas que un flujo determinista resuelve de forma más fiable.

### Servicios y adaptadores propios

Encapsulan las operaciones técnicas específicas de arquitectura. Por ejemplo, un servicio puede recibir una solicitud validada para auditar un DWG y devolver un informe estructurado.

Las interfaces deben ser estables, documentadas y comprobables sin depender de una conversación con el agente.

### Herramientas de diseño y documentación

AutoCAD, Rhino, Grasshopper, IFC, ComfyUI y Twinmotion siguen siendo los motores especializados. Hermes no reemplaza sus capacidades nativas: las coordina mediante integraciones adecuadas.

### Registro central del proyecto

Debe conservar información suficiente para responder:

- ¿De qué archivo salió este resultado?
- ¿Qué versión se procesó?
- ¿Qué parámetros se utilizaron?
- ¿Qué herramientas y modelos intervinieron?
- ¿Quién aprobó el cambio?
- ¿Qué otros documentos deben revisarse si cambia este elemento?
- ¿Podemos reproducir el resultado?

---

# 4\. HERMES AGENT: INVESTIGACIÓN E INTEGRACIÓN

Hermes está en evaluación. Antes de adoptarlo como pieza central, realizar una prueba de concepto.

## Capacidades a comprobar

1. Instalación y operación en Docker.
2. Persistencia de configuración, sesiones, habilidades y memoria.
3. Integración con proveedores de modelos.
4. Uso de herramientas y ejecución de comandos.
5. Integración con servidores MCP locales y remotos.
6. Interacción con APIs HTTP.
7. Comunicación mediante Telegram u otra interfaz.
8. Gestión de permisos y aprobaciones.
9. Recuperación después de reinicios.
10. Ejecución de procesos prolongados y manejo de fallos.
11. Comportamiento ante instrucciones ambiguas.
12. Registro de acciones y posibilidad de auditar resultados.

Documentación oficial:

- General: https://hermes-agent.nousresearch.com/docs
- Docker: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/
- Herramientas: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools

Consultar las versiones vigentes de la documentación antes de escribir la configuración de despliegue.

## Diseño de habilidades

Las habilidades deben representar procedimientos reutilizables, no solamente prompts extensos.

Ejemplos:

- `diagnosticar-proyecto-arquitectonico`
- `auditar-documentacion-cad`
- `generar-variantes-visuales`
- `validar-modelo-ifc`
- `preparar-entrega-de-proyecto`
- `documentar-visita-de-obra`
- `comparar-versiones-de-documentacion`

Cada habilidad debería indicar:

- Objetivo.
- Datos de entrada.
- Herramientas autorizadas.
- Precondiciones.
- Procedimiento.
- Criterios de validación.
- Permisos requeridos.
- Acciones que necesitan aprobación.
- Formato de salida.
- Tratamiento de errores.
- Evidencias que deben conservarse.

No asumir que Hermes tiene una integración nativa con AutoCAD, Rhino, Grasshopper, IFC, Twinmotion o ComfyUI. Investigar cada conexión y construir adaptadores cuando sea necesario.

---

# 5\. INTEGRACIÓN CON AUTOCAD

## Objetivo

Automatizar tareas de dibujo, revisión, preparación de documentación y publicación de entregables, empezando por operaciones de bajo riesgo.

## Posibles tecnologías

Investigar la API .NET de AutoCAD, AutoLISP, scripts de comandos y otros mecanismos compatibles con la versión instalada.

Documentación de referencia:
https://help.autodesk.com/

Verificar las capacidades exactas según versión, licencia, sistema operativo y tipo de instalación.

## Herramientas propuestas

### `inspect_dwg`

- Inspeccionar estructura del archivo.
- Identificar capas, bloques, referencias externas y unidades.
- Extraer propiedades relevantes.
- Informar problemas de lectura o dependencias faltantes.

### `audit_dwg`

- Comprobar convenciones de nombres.
- Revisar capas y propiedades gráficas.
- Detectar referencias externas faltantes.
- Verificar unidades y configuraciones.
- Comparar propiedades con reglas del estudio.

### `prepare_sheet`

- Aplicar configuraciones previamente definidas.
- Preparar layouts y parámetros de publicación.
- Verificar que las referencias necesarias estén disponibles.
- Generar un informe de validación.

### `publish_pdf`

- Publicar documentación a partir de una configuración aprobada.
- Registrar fecha, archivo fuente, versión y resultado.
- Verificar que los archivos de salida existan y sean legibles.

### `compare_dwg`

- Comparar versiones mediante propiedades y geometría cuando resulte técnicamente viable.
- Detectar diferencias.
- Clasificarlas según reglas.
- Generar un informe de cambios.

### `extract_quantities`

- Extraer cantidades desde entidades o bloques que dispongan de semántica suficiente.
- Exportar datos a CSV, JSON o tablas.
- Informar las limitaciones y elementos que no pudieron clasificarse.

**Importante:** una línea en CAD no equivale necesariamente a un muro, y una polilínea no equivale automáticamente a una superficie computable. Los cómputos requieren reglas explícitas, convenciones de dibujo o datos semánticos fiables.

## Criterio de implementación

Empezar por inspección, auditoría y publicación. Avanzar a modificaciones automáticas cuando las pruebas demuestren que los resultados son fiables.

---

# 6\. INTEGRACIÓN CON RHINO Y GRASSHOPPER

## Objetivo

Conectar el razonamiento del agente con operaciones de geometría, modelado paramétrico y generación controlada de modelos.

## Tecnologías a investigar

- RhinoCommon.
- Rhino Python y las APIs disponibles en la versión instalada.
- Grasshopper.
- Rhino.Compute, si resulta compatible con el entorno y el caso de uso.
- Formatos 3DM, STEP, DXF, IFC y otros intercambios pertinentes.

Referencia oficial:
https://developer.rhino3d.com/

Referencia de Rhino.Compute:
https://developer.rhino3d.com/guides/compute/

## Herramientas propuestas

### `inspect_3dm`

Extraer objetos, capas, tipos de geometría, unidades y propiedades relevantes.

### `generate_geometry`

Crear geometría a partir de parámetros validados y operaciones permitidas.

### `run_grasshopper`

Ejecutar una definición de Grasshopper con entradas explícitas y devolver resultados, métricas y errores.

### `measure_geometry`

Calcular superficies, longitudes, volúmenes y otras métricas, verificando unidades y validez geométrica.

### `export_model`

Preparar exportaciones en formatos acordados y validar que el archivo generado pueda abrirse.

## Casos de uso

- Generación paramétrica de alternativas.
- Evaluación geométrica de variantes.
- Estudios de superficies y volúmenes.
- Exploración de envolventes.
- Preparación de geometría para visualización.
- Automatización de tareas repetitivas de modelado.
- Cálculo de métricas y generación de tablas.

La IA puede ayudar a traducir una intención de diseño a parámetros y operaciones, pero la ejecución geométrica debe apoyarse en código verificable y controles de validez.

---

# 7\. BIM E INTEROPERABILIDAD IFC

## Objetivo

Construir una capa de información arquitectónica que permita inspeccionar modelos, extraer propiedades, validar entregables y relacionar datos con documentación.

## Tecnología principal a evaluar

IfcOpenShell:
https://docs.ifcopenshell.org/

También se deben investigar las herramientas open source compatibles con los formatos y flujos reales del estudio.

## Herramientas propuestas

### `inspect_ifc`

- Leer el esquema y la estructura del archivo.
- Identificar entidades.
- Extraer relaciones y propiedades disponibles.
- Comprobar unidades y datos generales.

### `extract_properties`

Obtener propiedades, materiales, clasificaciones, cantidades y relaciones que realmente existan en el modelo.

### `validate_ifc`

Validar estructura, propiedades obligatorias, reglas del proyecto y convenciones de intercambio.

### `compare_ifc`

Comparar versiones y detectar cambios en entidades, propiedades y relaciones.

### `export_schedule`

Generar tablas de elementos y cantidades según reglas explícitas.

### `prepare_bcf_issues`

Investigar la creación o actualización de incidencias mediante BCF cuando sea compatible con las herramientas participantes.

## Criterios de interoperabilidad

- Conservar identificadores persistentes cuando corresponda.
- No depender exclusivamente del nombre de un objeto.
- Registrar unidades y sistemas de coordenadas.
- Diferenciar cantidades modeladas de cantidades calculadas.
- Documentar pérdidas o transformaciones producidas durante las exportaciones.
- Comprobar la fidelidad de los intercambios mediante casos de prueba.

IFC debe tratarse como una capa de interoperabilidad y datos, no como garantía automática de que todos los programas conservarán toda la información.

---

# 8\. COMFYUI LOCAL: IMÁGENES Y CONTENIDO VISUAL

## Objetivo

Integrar la generación y transformación de imágenes en flujos de diseño, presentación y producción audiovisual, aprovechando la instalación local existente cuando sea viable.

Documentación oficial:
https://docs.comfy.org/

## Arquitectura propuesta

Hermes interpreta la solicitud y selecciona un flujo aprobado. Un servicio de integración valida los parámetros y envía el trabajo a ComfyUI. Después consulta su estado, recupera los resultados y registra los archivos producidos.

Investigar la API de ejecución, las colas de trabajos, el historial y los mecanismos de notificación disponibles en la versión instalada.

## Herramientas propuestas

- `list_workflows`
- `validate_workflow`
- `submit_visual_job`
- `watch_job`
- `collect_outputs`
- `register_visual_result`

## Casos de uso

1. Transformar croquis en imágenes conceptuales.
2. Explorar materiales e iluminación.
3. Generar alternativas visuales controladas.
4. Producir variaciones a partir de una imagen de referencia.
5. Convertir documentación gráfica en recursos para presentación.
6. Preparar material para videos y publicaciones.
7. Crear imágenes de avance de proyecto.

## Condiciones técnicas

- Inspeccionar GPU, memoria disponible y tiempos reales de ejecución.
- Verificar compatibilidad de nodos y modelos con la GPU AMD y el backend instalado.
- Registrar versiones de workflows, nodos, modelos, semillas y parámetros cuando corresponda.
- Mantener los originales y separar resultados aprobados de pruebas.
- Gestionar trabajos concurrentes y colas para evitar saturar el equipo.

El agente debe distinguir entre una imagen conceptual, una visualización de un modelo real y una representación fiel del proyecto. La generación visual no debe modificar silenciosamente información técnica aprobada.

---

# 9\. TWINMOTION, RENDERS Y VIDEO

## Objetivo

Conectar el modelo de diseño con la producción de visualizaciones y presentaciones.

## Ruta inicial a investigar

Rhino → Datasmith Direct Link → Twinmotion.

Documentación oficial:
https://dev.epicgames.com/documentation/es-es/twinmotion/datasmith-direct-link-workflow-in-twinmotion

Validar la compatibilidad entre versiones, el comportamiento de las actualizaciones y qué elementos se conservan en el intercambio.

También investigar los flujos desde AutoCAD e IFC según los formatos y versiones utilizados en el estudio.

## Automatizaciones potenciales

- Preparar y validar los modelos de origen.
- Comprobar rutas y referencias.
- Crear listas de vistas y cámaras.
- Organizar entregables por escena y versión.
- Registrar imágenes y videos exportados.
- Relacionar los renders con la versión del modelo utilizada.
- Preparar material para presentaciones y redes.

## Límite importante

No asumir que Twinmotion ofrece una API capaz de realizar cualquier operación que un usuario ejecuta en su interfaz.

Antes de automatizar controles, exportaciones o configuración de escenas, comprobar qué capacidades están expuestas oficialmente. Cuando no exista una API apropiada, evaluar automatización de interfaz o procesos asistidos, siempre con validación y recuperación ante fallos.

---

# 10\. DOCUMENTACIÓN, OBRA Y GESTIÓN DEL CONOCIMIENTO

Esta capa puede aportar valor incluso antes de automatizar todo el modelado.

## Casos de uso

### Libro digital de obra

- Registrar visitas, fechas y responsables.
- Clasificar fotografías y observaciones.
- Relacionar incidencias con sectores, elementos y documentos.
- Generar borradores de actas e informes.
- Mantener historial de resolución.
- Solicitar validación antes de emitir documentos oficiales.

### Gestor documental

- Indexar archivos.
- Clasificar documentos.
- Detectar duplicados.
- Identificar versiones.
- Registrar dependencias.
- Encontrar documentación relacionada.
- Preparar paquetes de entrega.

### Asistente técnico

- Consultar especificaciones y documentación de referencia.
- Responder con citas a las fuentes utilizadas.
- Identificar información faltante.
- Generar listas de comprobación.
- Diferenciar datos verificados de inferencias.

### Cómputos y presupuestos

- Extraer datos desde fuentes estructuradas.
- Aplicar fórmulas deterministas.
- Mantener unidades y criterios de medición.
- Registrar precios, fechas y procedencia de los valores.
- Generar un informe de partidas pendientes de validación.

### Producción de contenido

- Convertir avances aprobados en material de presentación.
- Preparar guiones, descripciones y publicaciones.
- Relacionar cada pieza con el proyecto y los recursos originales.
- Evitar publicar imágenes o datos sin autorización.

---

# 11\. REGISTRO CENTRAL Y GRAFO DE DEPENDENCIAS

La visión de largo plazo es representar el proyecto como un grafo de elementos relacionados.

Ejemplo:

``` text
Croquis
   |
   v
Modelo Rhino
   |
   +------> Modelo IFC
   |            |
   v            v
Render      Cómputos
   |            |
   v            v
Video       Presupuesto
   |
   v
Presentación
```

El grafo real debe permitir múltiples relaciones, bifurcaciones y versiones.

## Entidades iniciales

- Proyecto.
- Archivo.
- Versión.
- Elemento modelado.
- Parámetro.
- Ejecución de proceso.
- Resultado.
- Fuente documental.
- Incidencia.
- Aprobación.
- Usuario o responsable.
- Entrega.

## Relaciones iniciales

- `derived_from`
- `depends_on`
- `generated_by`
- `validated_by`
- `approved_by`
- `supersedes`
- `references`
- `belongs_to`
- `resolves`

## Ejemplo de funcionamiento deseado

Si cambia un parámetro del modelo Rhino:

1. Registrar la nueva versión.
2. Identificar los productos que dependen de ella.
3. Marcar como potencialmente desactualizados los renders, exportaciones o documentos pertinentes.
4. Determinar qué procesos pueden volver a ejecutarse.
5. Solicitar aprobación si el cambio afecta documentación oficial.
6. Registrar las nuevas salidas y sus relaciones.

No es necesario construir un grafo distribuido complejo desde el inicio. Para el MVP, una base relacional con tablas de versiones, relaciones y ejecuciones puede ser suficiente. Evaluar una base de grafos cuando exista un caso de uso que lo justifique.

---

# 12\. DESPLIEGUE EN EL VPS

## Propuesta inicial

Hermes puede convivir con n8n y otros servicios en el mismo VPS, siempre que los recursos disponibles sean suficientes.

Distribución lógica:

- Hermes: contenedor independiente.
- n8n: servicio existente.
- Chatwoot: servicio existente.
- Base de datos: servicio propio o compartido según la arquitectura ya instalada.
- Adaptadores y workers: servicios independientes cuando corresponda.
- Almacenamiento de resultados: volúmenes o servicio de archivos.
- Proxy inverso: punto de entrada controlado.

Cada servicio debe conservar sus propios volúmenes, configuración, permisos y procedimiento de recuperación.

## Condiciones de seguridad

- No exponer la base de datos a Internet.
- No entregar a Hermes acceso irrestricto a la base interna de n8n.
- Crear credenciales específicas y de mínimo privilegio.
- Mantener secretos fuera del repositorio.
- Evitar publicar puertos de administración innecesarios.
- Restringir la API de Hermes mediante autenticación y controles de red.
- Mantener separados los entornos de prueba y producción.
- Revisar las consecuencias de conceder acceso al terminal, navegador y archivos.
- Configurar límites de ejecución y mecanismos para detener procesos repetitivos.
- Mantener backups comprobables.

La documentación oficial de Hermes describe el despliegue en Docker, la persistencia mediante volúmenes y la exposición opcional del gateway. Revisar también las medidas de seguridad antes de habilitar interfaces externas.

No instalar todavía hasta relevar el VPS y definir un procedimiento reversible.

## Conexión con herramientas del equipo local

AutoCAD, Rhino, Grasshopper, Twinmotion y ComfyUI pueden seguir ejecutándose en el equipo local.

El VPS no necesita ejecutar las aplicaciones gráficas para coordinar sus procesos, siempre que exista un mecanismo de comunicación adecuado.

Posible arquitectura:

``` text
Hermes en VPS
      |
      v
API / cola autenticada
      |
      v
Agente puente local
      |
      +--> AutoCAD
      +--> Rhino / Grasshopper
      +--> ComfyUI
      +--> Exportaciones
```

El agente puente es una pieza por desarrollar y validar. Debe aceptar únicamente operaciones autorizadas, comprobar entradas y devolver resultados estructurados.

Priorizar una conexión segura iniciada desde el equipo local o mediante VPN. Evitar exponer el equipo de trabajo directamente a Internet.

---

# 13\. CONTRATOS DE LAS HERRAMIENTAS

Todas las integraciones deben seguir un contrato común, aunque cada adaptador utilice tecnologías distintas.

Ejemplo conceptual de solicitud:

``` json
{
  "task_id": "uuid",
  "project_id": "project-001",
  "tool": "inspect_3dm",
  "input": {
    "file_ref": "project/model.3dm"
  },
  "requested_by": "agent",
  "approval": "not_required"
}
```

Ejemplo conceptual de respuesta:

``` json
{
  "task_id": "uuid",
  "status": "completed",
  "outputs": [],
  "warnings": [],
  "errors": [],
  "provenance": {
    "input_version": "version-id",
    "tool_version": "version",
    "completed_at": "ISO-8601"
  }
}
```

Estos ejemplos son un contrato de diseño ilustrativo, no un esquema definitivo ni una API ya existente.

## Requisitos comunes

- Identificador único de ejecución.
- Validación de entradas.
- Estados explícitos.
- Errores estructurados.
- Registro de tiempos.
- Límites de recursos.
- Idempotencia cuando corresponda.
- Reintentos controlados.
- Referencias a archivos, no rutas arbitrarias proporcionadas por el modelo.
- Trazabilidad de entradas y salidas.
- Pruebas unitarias y de integración.

Los adaptadores deben impedir que una instrucción ambigua termine modificando o sobrescribiendo archivos originales.

---

# 14\. PLAN DE IMPLEMENTACIÓN POR FASES

Las fases se proponen como hipótesis de planificación. Su duración real depende de las versiones, el estado del entorno y la complejidad descubierta durante el diagnóstico.

## Fase 0 — Inventario y prueba de viabilidad

- Inspeccionar el VPS y los servicios existentes.
- Revisar el repositorio de OpenCode.
- Identificar versiones de aplicaciones.
- Consultar la documentación oficial.
- Definir casos de prueba.
- Medir recursos y restricciones.
- Elaborar un mapa de integraciones confirmadas, posibles y pendientes.

**Entregable:** diagnóstico técnico y matriz de viabilidad.

## Fase 1 — Hermes y capa de herramientas

- Probar Hermes en un entorno controlado.
- Verificar persistencia y reinicio.
- Probar una integración MCP o HTTP.
- Definir contratos de herramientas.
- Establecer permisos y logs.
- Conectar una operación de solo lectura.

**Entregable:** agente capaz de ejecutar una herramienta limitada y devolver resultados verificables.

## Fase 2 — AutoCAD y documentación

- Implementar inspección de archivos.
- Auditar capas y referencias.
- Generar un informe.
- Preparar publicación de PDF.
- Registrar resultados y errores.

**Entregable:** flujo de auditoría y publicación con datos de prueba.

## Fase 3 — Rhino y Grasshopper

- Inspeccionar geometría.
- Ejecutar una operación geométrica controlada.
- Medir resultados.
- Probar un flujo paramétrico.
- Validar exportación.

**Entregable:** herramienta reproducible de modelado o medición.

## Fase 4 — ComfyUI y visualización

- Inventariar workflows.
- Validar parámetros.
- Enviar trabajos.
- Recuperar imágenes.
- Registrar procedencia.
- Medir rendimiento del hardware local.

**Entregable:** generación visual integrada con un proyecto de prueba.

## Fase 5 — IFC e interoperabilidad

- Leer un IFC de prueba.
- Extraer propiedades.
- Validar reglas.
- Exportar tablas.
- Comparar dos versiones.

**Entregable:** auditoría básica de información BIM.

## Fase 6 — Twinmotion y producción

- Verificar el flujo Datasmith.
- Identificar operaciones automatizables.
- Vincular salidas a versiones de modelo.
- Registrar renders y videos.

**Entregable:** cadena de visualización documentada, con los pasos automáticos y manuales claramente diferenciados.

## Fase 7 — Integración y piloto

- Unificar registro de ejecuciones.
- Añadir relaciones de dependencias.
- Probar errores y recuperación.
- Validar permisos.
- Medir ahorro de tiempo y tasa de fallos.
- Documentar procedimientos de operación.

**Entregable:** MVP demostrable en un proyecto real o representativo.

---

# 15\. PRUEBAS DE ACEPTACIÓN

Cada módulo debe tener criterios objetivos.

Ejemplos:

- El sistema detecta un archivo faltante y lo informa sin detener silenciosamente todo el flujo.
- Una auditoría genera el mismo resultado ante las mismas entradas y versiones, dentro de las tolerancias definidas.
- Un archivo original permanece intacto durante una prueba de publicación.
- Un trabajo de ComfyUI permite recuperar sus salidas y relacionarlas con su solicitud.
- La extracción IFC informa las propiedades inexistentes en lugar de inventarlas.
- Un cambio de modelo identifica los productos dependientes pertinentes.
- Un fallo de red produce un estado de error recuperable.
- Un reinicio no elimina la configuración persistente.
- Una acción de riesgo requiere la aprobación prevista.
- Los logs no exponen secretos ni información innecesaria.

Registrar los resultados de cada prueba, las versiones involucradas y los defectos pendientes.

---

# 16\. SEGURIDAD Y GOBERNANZA

Clasificar las operaciones por nivel de riesgo.

### Nivel A — Lectura

Ejemplos: listar archivos autorizados, inspeccionar capas, leer propiedades IFC, consultar el estado de un trabajo.

Automatización permitida después de validar permisos.

### Nivel B — Generación aislada

Ejemplos: crear un informe, generar una imagen, exportar una tabla a una carpeta de resultados.

Permitir en directorios controlados, con límites y trazabilidad.

### Nivel C — Modificación

Ejemplos: modificar un DWG, sobrescribir un modelo, alterar un workflow o cambiar datos de un proyecto.

Exigir validaciones, copia de seguridad y aprobación según el caso.

### Nivel D — Publicación o acción externa

Ejemplos: emitir documentación contractual, enviar entregables oficiales, publicar contenido o modificar registros productivos.

Exigir aprobación explícita y conservar evidencia de la acción.

Las acciones de mayor riesgo deben contar con permisos específicos, controles previos y procedimientos de reversión. La autonomía del agente debe aumentar a partir de evidencia de fiabilidad, no solamente de que una demostración haya funcionado una vez.

---

# 17\. CRITERIOS DE EVALUACIÓN DEL MVP

Medir el sistema por su utilidad operacional.

Indicadores iniciales:

- Tiempo de ejecución manual frente a automatizada.
- Porcentaje de ejecuciones exitosas.
- Porcentaje de resultados que requieren corrección.
- Tiempo de recuperación ante fallos.
- Porcentaje de resultados con trazabilidad completa.
- Cantidad de operaciones que necesitan intervención humana.
- Coste por ejecución.
- Recursos consumidos en VPS y equipo local.
- Facilidad para actualizar herramientas.
- Capacidad para reproducir resultados.

No optimizar solamente la cantidad de tareas automatizadas. Priorizar los procesos que reducen errores, tiempos de búsqueda, trabajo repetitivo y fricción entre disciplinas.

---

# 18\. INSTRUCCIONES PARA EL AGENTE DE OPENCODE

Actúa como arquitecto de software e investigador técnico del proyecto Pitautech/pitauOS.

Tu misión es convertir este briefing en una implementación incremental, verificable y mantenible.

## Primera tarea: diagnóstico

Antes de programar:

1. Inspecciona el repositorio actual y sus convenciones.
2. Identifica la estructura de carpetas, lenguajes, dependencias, documentación y pruebas.
3. Detecta si ya existen adaptadores, servicios, workflows o configuraciones relacionadas con Hermes, n8n, MCP, CAD, BIM o ComfyUI.
4. Comprueba qué partes están implementadas y cuáles son solamente ideas.
5. Identifica inconsistencias y decisiones técnicas pendientes.
6. Contrasta las capacidades de las herramientas con documentación oficial vigente.
7. Separa explícitamente hechos comprobados, hipótesis y preguntas abiertas.

No reemplaces componentes existentes sin demostrar por qué es necesario.

## Segunda tarea: diseño

Proponer:

- Arquitectura de componentes.
- Diagrama de secuencia de una ejecución.
- Límites de responsabilidad.
- Contratos de herramientas.
- Modelo de datos mínimo.
- Gestión de archivos y versiones.
- Estrategia de autenticación y permisos.
- Registro y observabilidad.
- Estrategia de pruebas.
- Plan de despliegue y reversión.

Priorizar soluciones simples, modulares y compatibles con el entorno existente.

## Tercera tarea: MVP

Seleccionar una sola integración inicial de bajo riesgo. Como opción preferida, evaluar una herramienta de inspección de archivos o un flujo de ComfyUI que no sobrescriba originales.

Implementar:

- Una interfaz bien definida.
- Validación de entradas.
- Ejecución controlada.
- Respuesta estructurada.
- Gestión de errores.
- Pruebas automatizadas.
- Documentación de uso.
- Ejemplo de ejecución reproducible.

La elección final debe basarse en el estado real del repositorio y en las capacidades comprobadas del entorno.

## Reglas de trabajo

- No inventar endpoints, capacidades de APIs ni herramientas nativas.
- Consultar documentación oficial y registrar las fuentes.
- No asumir que un protocolo MCP existe para cada aplicación.
- No exponer secretos en el código, logs o commits.
- No alterar servicios productivos sin autorización.
- No ejecutar acciones destructivas sin aprobación.
- No agregar dependencias innecesarias.
- No construir una arquitectura distribuida compleja antes de demostrar su necesidad.
- Documentar decisiones técnicas y alternativas descartadas.
- Mantener los cambios pequeños, testeables y reversibles.
- Informar qué se implementó, qué se verificó y qué queda pendiente.

## Formato del informe inicial

Entregar:

1. Resumen del estado actual del repositorio.
2. Arquitectura existente.
3. Integraciones encontradas.
4. Matriz de capacidades confirmadas y pendientes.
5. Riesgos técnicos y de seguridad.
6. Propuesta de MVP.
7. Archivos que sería necesario crear o modificar.
8. Pruebas de aceptación.
9. Próximo paso recomendado.

**Primera prioridad:** entender el sistema existente antes de añadir otro agente. El resultado esperado es una arquitectura que conecte las herramientas de manera fiable, no una colección de automatizaciones aisladas.

---

# 19\. DOCUMENTACIÓN OFICIAL DE REFERENCIA

- Hermes Agent: https://hermes-agent.nousresearch.com/docs
- Hermes en Docker: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Hermes y MCP: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/
- Hermes y herramientas: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
- Autodesk: https://help.autodesk.com/
- Rhino Developer: https://developer.rhino3d.com/
- Rhino.Compute: https://developer.rhino3d.com/guides/compute/
- IfcOpenShell: https://docs.ifcopenshell.org/
- ComfyUI: https://docs.comfy.org/
- Twinmotion Datasmith Direct Link: https://dev.epicgames.com/documentation/es-es/twinmotion/datasmith-direct-link-workflow-in-twinmotion

Estas referencias son puntos de partida. El agente debe comprobar las páginas vigentes y la compatibilidad con las versiones reales antes de implementar.

---

## VISIÓN FINAL

Pitautech busca construir una capa de inteligencia operacional para estudios de arquitectura: un sistema que comprenda el proyecto, coordine herramientas especializadas, automatice procesos verificables y conserve la trazabilidad entre intención, modelo, documentación, visualización y obra.

El valor diferencial no reside en generar una imagen o ejecutar un script aislado. Reside en **conectar los procesos, preservar el conocimiento y hacer que cada resultado forme parte de un sistema coherente, auditable y reutilizable**.