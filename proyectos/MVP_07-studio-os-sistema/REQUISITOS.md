---
tipo: requisitos
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
tags: [mvp_07, studio-os, requisitos, rf, rnf, criterios, metricas, plan]
idioma: es
---

# REQUISITOS — Studio OS

> Qué tiene que cumplir el sistema y **cómo se sabe que lo cumple**. El *qué* y el *para qué* están en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]; el *dónde vive y cómo se conecta*, en [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]].
> Estilo: documento de requisitos de software (casos, RF/RNF, criterios de aceptación, métricas y plan de entrega).

## Cómo se reparten los tres documentos

| | **VISION** | **ESTRUCTURA** | **REQUISITOS** (este) |
|---|---|---|---|
| **La pregunta** | ¿qué es y para qué? | ¿dónde vive y cómo se conecta? | ¿qué tiene que cumplir y cómo se mide? |
| **Qué contiene** | el problema · el recorrido · el cuaderno digital · Hermes en conceptual · el stack elegido con sus alternativas · las decisiones de producto | los 4 nodos · dónde vive cada pieza · el agente y sus conexiones · cada integración con sus opciones · el contrato entre componentes · el modelo de datos · seguridad, secretos, backup y acceso remoto · puesta en marcha | alcance · actores · casos de uso · RF y RNF · criterios de aceptación · gobernanza A-D · regla automatizar/persona · métricas · plan de entrega · decisiones abiertas |

- [[#1 · Alcance]]
- [[#2 · Actores y permisos]]
- [[#3 · Casos de uso]]
- [[#4 · Requerimientos funcionales]]
- [[#5 · Requerimientos no funcionales]]
- [[#6 · Criterios de aceptación]]
- [[#7 · Gobernanza por nivel de riesgo]]
- [[#8 · Qué automatiza el agente y qué hace la gente]]
- [[#9 · Métricas]]
- [[#10 · Decisiones abiertas]]
- [[#11 · Plan de entrega]]

El cuarto documento, [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]], dice con qué piezas reales de Hermes se cumple cada requisito y cuáles quedan fuera de su alcance. La ruta de lectura por tema está en [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]].

---

# 1 · Alcance

## 1.1 Dentro del alcance

El sistema cubre **el ciclo completo del estudio**: entra un cliente, hay una reunión con compromisos, se dibuja, se modela, se renderiza, se entrega, se documenta la obra y el conocimiento queda guardado.

Sobre todo eso, el sistema hace tres cosas:

1. **Ejecuta** el trabajo repetitivo y verificable.
2. **Registra** de dónde sale cada resultado y quién lo aprobó.
3. **Mejora la memoria** de la casa: el cuaderno digital y la wiki.

## 1.2 Fuera del alcance (por ahora)

| Fuera | Por qué |
|---|---|
| Reemplazar AutoCAD, Rhino o Twinmotion | son licencias del estudio y herramientas maduras: el sistema las conduce, no las sustituye |
| Un CRM completo | un estudio de arquitectura no tiene un flujo de clientes que lo justifique |
| BIM como fin | no hay un IFC real del estudio todavía |
| Twindmotion o Unreal automatizados | no hay API pública: es trabajo asistido |
| Multi-estudio | el producto se valida con un piloto |
| Base de grafos dedicada | un grafo de verdad sobre las relaciones del registro alcanza |
| Un panel propio | la interfase del día a día es Telegram; el portal es para el cuaderno y las iteraciones |

---

# 2 · Actores y permisos

| Actor | Qué hace | Qué puede |
|---|---|---|
| **Arquitecto titular** | decide diseño, aprueba, entrega | todo; es quien aprueba lo nivel C y D |
| **Junior** | ejecuta tareas definidas | opera lo nivel A y B; pide aprobación para lo demás |
| **PITAUTECH (operador)** | instala, mantiene, da soporte | acceso de administración (perfil separado, con sus acciones registradas) |
| **El agente (Hermes)** | prepara, ejecuta lo verificable, registra | nivel A y B automático; C y D solo con aprobación; **no** accede a bases internas ni a binarios |
| **El cliente** | recibe, aprueba por mail | solo ve lo que se le envía |

**El principio**: el agente **no es actor responsable**. La responsabilidad de decidir y de comunicarse es siempre de una persona.

---

# 3 · Casos de uso

## 3.1 Del cliente y la relación

| id | Caso | Quién | Resultado esperado |
|---|---|---|---|
| **C-01** | Alta de cliente | titular | queda en la hoja de clientes: nombre, contacto, mail (Instagram a futuro) y qué se le entregó |
| **C-02** | Reunión con compromisos | titular | minuta con lo decidido y lista de compromisos, **cada uno con qué entregar y con qué fecha** |
| **C-03** | Recordatorio de compromiso | agente | aviso por Telegram antes de que venza, con el contexto de la reunión |
| **C-04** | Mail al cliente | titular | el agente redacta el mail con el formato del estudio a partir de los compromisos; **una persona lo revisa y lo manda** |

## 3.2 Del trabajo de diseño

| id | Caso | Quién | Resultado esperado |
|---|---|---|---|
| **C-05** | Auditoría de documentación CAD | arquitecto | informe con observaciones clasificadas (bloqueante / advertencia / observación), el original intacto |
| **C-06** | Comparación de versiones | arquitecto | qué cambió entre dos versiones, con la fecha de cada cambio |
| **C-07** | Preparación de entrega | arquitecto | paquete de entrega con índice, y registro de lo que se entregó y cuándo |
| **C-08** | Validación de un modelo IFC | arquitecto | el modelo se revisa contra las reglas del proyecto (entra cuando exista un IFC real) |
| **C-09** | Variantes visuales | arquitecto | el trabajo sale con sus parámetros y su semilla, y las iteraciones quedan en el portal |
| **C-10** | Modelo 3D y Grasshopper | arquitecto | medición, ejecución de la definición y exportación, con el original intacto |

## 3.3 De la obra y el conocimiento

| id | Caso | Quién | Resultado esperado |
|---|---|---|---|
| **C-11** | Visita de obra | arquitecto | fecha, fotos con tags, incidencias y su resolución |
| **C-12** | Cuaderno digital | arquitecto | el cuaderno es navegable tipo libro y cada croquis escaneado cuelga de su entrada de la wiki |
| **C-13** | "¿Qué sé de este proyecto?" | cualquier persona del equipo | respuesta con lo que hay en el cuaderno y en la wiki, con sus referencias |

---

# 4 · Requerimientos funcionales

| id | Requerimiento | Casos | Nivel |
|---|---|---|---|
| **RF-01** | El cliente se registra con sus datos y con lo que se le entregó | C-01 | A |
| **RF-02** | Una reunión produce minuta, decisiones y compromisos con fecha | C-02 | A |
| **RF-03** | Las reuniones repetidas en varios *meetings* se agrupan en una sola entrada | C-02 | A |
| **RF-04** | El agente avisa por Telegram cuando un compromiso está por vencer | C-03 | B |
| **RF-05** | El agente redacta el mail al cliente con el formato del estudio; el envío es de una persona | C-04 | B → D |
| **RF-06** | La auditoría de un DWG devuelve observaciones clasificadas, nombrando capas y entidades concretas | C-05 | A |
| **RF-07** | El hash del archivo original es idéntico antes y después de cualquier operación | C-05, C-07, C-10 | — |
| **RF-08** | La comparación de versiones devuelve las diferencias con su fecha | C-06 | A |
| **RF-09** | La entrega se arma con su índice y queda registrada con fecha | C-07 | D |
| **RF-10** | Un modelo IFC se puede inspeccionar, validar y comparar | C-08 | A |
| **RF-11** | Cada render queda con su metadata (modelo, LoRA, semilla, sampler, pasos, cfg, resolución, prompt) | C-09 | B |
| **RF-12** | Las iteraciones se publican en un portal consultable (no por mail) | C-09 | B |
| **RF-13** | El modelo 3D se puede inspeccionar, medir y ejecutar en Grasshopper sin pantalla | C-10 | A/B |
| **RF-14** | Una visita de obra queda con fecha, fotos con tags e incidencias con su resolución | C-11 | B |
| **RF-15** | El cuaderno se puede recorrer en orden y muestra los escaneos de croquis | C-12 | B |
| **RF-16** | Cada croquis escaneado está referenciado desde la entrada de wiki que documenta | C-12 | B |
| **RF-17** | Toda búsqueda sobre el conocimiento devuelve la referencia de la fuente | C-13 | A |
| **RF-18** | Toda tarea queda registrada con origen, versión, herramienta, parámetros, tiempos y responsable | todos | A |
| **RF-19** | Un cambio de versión marca los productos dependientes como desactualizados y propone qué rehacer | C-06, C-10 | A |
| **RF-20** | Las aprobaciones quedan con persona, hora y contenido aprobado | C-04, C-07, C-09 | — |

---

# 5 · Requerimientos no funcionales

| id | Requerimiento | Cómo se mide |
|---|---|---|
| **RNF-01 · Auditabilidad** | el 100% de los resultados tiene procedencia completa (archivo, versión, herramienta, parámetros, responsable) | % de resultados con trazabilidad completa |
| **RNF-02 · Conocimiento accesible** | un junior puede resolver una consulta de un proyecto anterior **sin preguntarle a un senior** | minutos que un junior tarda en encontrar y aplicar lo que hay |
| **RNF-03 · Reproducibilidad** | la misma entrada con los mismos parámetros da el mismo resultado | comparación de corridas repetidas |
| **RNF-04 · Idempotencia** | repetir una tarea con la misma clave no duplica trabajo | conteo de ejecuciones por clave |
| **RNF-05 · PI: nada sale sin permiso** | los planos legales, los cálculos, el material de cliente confidential y el material de concurso con PI de terceros **nunca** salen del entorno del estudio | auditoría de salidas por perfil |
| **RNF-06 · Secretos** | ninguna clave vive en el repositorio | revisión del `.env` y del repo |
| **RNF-07 · Superficie expuesta** | el sistema no expone puertos públicos; los accesos remotos son autenticados y auditados | inventario de puertos del VPS |
| **RNF-08 · No destructive** | ninguna operación escribe sobre un archivo original sin copia y reversión | hash del original antes/después |
| **RNF-09 · Degradación clara** | si una herramienta no está disponible, el sistema lo dice (estado explícito), nunca inventa un resultado | escenarios de indisponibilidad probados |
| **RNF-10 · Costo acotado** | el gasto mensual de modelo y GPU es visible por ejecución y por mes | costo por ejecución y mensual |
| **RNF-11 · Recursos del VPS** | el sistema completo (agente, n8n, base, tablero, búsqueda) convive con la RAM disponible sin swap activo | RAM libre y swap del VPS |
| **RNF-12 · Modularidad** | cada pieza (modelo, red, base, herramienta) se puede cambiar sin reconstruir el resto | prueba de recambio documentada |
| **RNF-13 · Interoperabilidad** | los datos que salen del estudio se exportan en formatos abiertos (IFC, glTF, SVG, Markdown) | revisión de exportaciones |
| **RNF-14 · Respaldo comprobable** | existe una copia cifrada de lo que no se puede recuperar, y se **probó** restaurándola | prueba de restauración |
| **RNF-15 · Accesible sin conocimientos técnicos** | el cuaderno y el portal se usan sin saber técnica (lo usa Emilia) | prueba con alguien no técnico |

---

# 6 · Criterios de aceptación

Cada criterio es un check objective. Formato: **Dado / Cuando / Entonces**.

| # | Criterio | Módulo |
|---|---|---|
| **AC-01** | Dado un archivo sin `file_ref`, cuando se pide una tarea, entonces se rechaza con `file_not_resolvable` | contrato |
| **AC-02** | Dado un sobre con `verbo: publish` y `riesgo: A`, cuando se valida, entonces se rechaza | contrato |
| **AC-03** | Dada una tarea repetida con la misma `idem_key`, cuando se vuelve a pedir, entonces devuelve la ejecución previa y no crea una nueva | contrato |
| **AC-04** | Dada una tarea registrada, cuando se consulta, entonces devuelve origen, versión, herramienta, parámetros, tiempos y responsable | registro |
| **AC-05** | Dada una versión nueva de un archivo, cuando se registra, entonces los artefactos que dependían de la anterior quedan marcados `stale` y se propone qué rehacer | registro |
| **AC-06** | Dada una auditoría de un DWG, cuando termina, entonces el hash del original es idéntico al de antes | CAD |
| **AC-07** | Dada una auditoría, cuando se lee el informe, entonces nombra capas y entidades concretas, y cada bloqueante trae su corrección propuesta | CAD |
| **AC-08** | Dada una tarea de nivel D sin aprobación, cuando se intenta ejecutar, entonces queda en `awaiting_approval` y no se ejecuta | riesgo |
| **AC-09** | Dada una acción C o D aprobada, cuando se registra, entonces quedan persona, hora y hash del contenido aprobado | riesgo |
| **AC-10** | Dado un trabajo de imagen, cuando termina, entonces sus salidas se recuperan con su metadata y quedan en el índice | imagen |
| **AC-11** | Dado un pod de GPU en marcha, cuando se revisa, entonces no tiene puertos públicos y entra a la red privada | seguridad |
| **AC-12** | Con la PC del estudio apagada, cuando se pide una tarea al runner, entonces responde `runner_no_disponible` con el motivo, y no hay resultado inventado | disponibilidad |
| **AC-13** | Con el sistema andando, cuando se reinicia el servicio del agente, entonces la configuración, la memoria y las sesiones siguen ahí | persistencia |
| **AC-14** | Dada una reunión grabada en varios *meetings*, cuando se resume, entonces aparece una sola entrada con todos los compromisos | reunión |
| **AC-15** | Dado un compromiso con fecha, cuando se acerca el vencimiento, entonces llega el recordatorio por Telegram | compromiso |
| **AC-16** | Dado un mail al cliente, cuando se revisa, entonces sale de los compromisos de la reunión y usa el formato del estudio | cliente |
| **AC-17** | Dado un croquis escaneado, cuando se busca su entrada de wiki, entonces se llega desde el cuaderno y desde la wiki | cuaderno |
| **AC-18** | Dados los logs del sistema, cuando se revisan, entonces no contienen claves ni secretos | seguridad |

---

# 7 · Gobernanza por nivel de riesgo

| Nivel | Alcance | Automatización | Evidencia que queda |
|---|---|---|---|
| **A · Lectura** | listar, inspeccionar, leer, comparar | automática | ejecución con procedencia |
| **B · Generación aislada** | informe, imagen, tabla, export a carpeta de resultados | automática, en carpeta controlada | ejecución + artefacto + hash |
| **C · Modificación** | modificar un DWG, sobrescribir un modelo, alterar un workflow | **requiere aprobación** | copia del original, aprobación (persona, hora, hash) y reversión |
| **D · Publicación o acción externa** | emitir documentación contractual, **mandar mail al cliente**, publicar contenido | **requiere aprobación explícita** | evidencia completa de la acción (qué se envió, a quién, con qué contenido) |

**Reglas transversales**

1. El nivel lo define la **operación**, no el agente ni quien la pide.
2. La aprobación se pide **en el canal donde se pidió la tarea**, con botones, y se registra.
3. Una tarea sin registro **no se ejecuta**.
4. Una tarea sin aprobación vigente **no se ejecuta**.
5. Lo aprobado es **una versión concreta**: si el contenido cambia, hay que volver a aprobar.

---

# 8 · Qué automatiza el agente y qué hace la gente

| El agente lo hace | Lo hace una persona | Por qué |
|---|---|---|
| Recopilar, indexar, etiquetar, resumir, comparar, verificar | | repetible y verificable: no hay criterio en juego |
| Preparar un informe, una tabla, un paquete de entrega | | sale de un dato que ya está |
| Armar el mail al cliente con el formato del estudio | **revisar y mandar** | el tono y el compromiso son de la casa |
| Publicar documentación contractual | **aprobar** (nivel D) | es un instrumento legal |
| Proponer una lectura de un croquis escaneado o de una foto de obra | **decidir qué significa** | requiere criterio |
| Armar el recordatorio de un compromiso | | es mecánica |
| Limpiar y resolver la documentación | | el agente propone, el arquitecto decide |

**La regla**: *se automatiza el trabajo, no la responsabilidad.* Y el filtro es económico: **se automatiza lo que se repite**. Una automatización que se usa una vez por mes no vale su mantenimiento.

---

# 9 · Métricas

## 9.1 Qué se mide

| Métrica | Por qué importa | Meta |
|---|---|---|
| **Tiempo de un junior para resolver una consulta de un proyecto anterior** | es la métrica del negocio: menos horas del senior | la que se defina en el piloto |
| **% de resultados con trazabilidad completa** | es el norte, literal | **100%** |
| **Tiempo manual vs. automatizado** por tipo de tarea | demuestra el ahorro | −50% en las tareas automatizadas |
| **% de ejecuciones exitosas** | calidad del sistema | >95% |
| **% de resultados que requieren corrección** | si sube, la automatización está fallando | <10% |
| **Tiempo de recuperación ante un fallo** | cuánta vida cuesta | <15 min |
| **Costo por ejecución y por mes** (modelo + GPU) | sustainability | visible y acotado |
| **RAM libre y swap del VPS** | el límite real del sistema | swap en 0 |
| **Búsquedas al vault resueltas sin preguntar a un senior** | el efecto del cuaderno digital | en aumento |

## 9.2 Baseline (se levanta en el primer tramo)

Antes de automatizar nada se cronometra cómo se hace hoy: auditar un DWG, publicar un PDF, sacar un corte, generar una tanda de renders, y responder "¿qué sé del proyecto X?".

Sin baseline no hay forma de demostrar ahorro.

---

# 10 · Decisiones abiertas (con impacto y momento)

| # | Decisión | Impacto si no se decide | Antes de |
|---|---|---|---|
| 1 | ¿Dónde vive el modelo del agente? (esta PC con 32 GB / el VPS con 8 GB / nube) | el agente no arranca | T1 |
| 2 | ¿Cómo se conectan OpenCode y Hermes? | el desarrollo propio no puede delegar | T1 |
| 3 | ¿n8n se queda o migra a Node-RED/Windmill? | la orquestación queda atada a una licencia | T2 |
| 4 | ¿Qué se automatiza primero? | el primer tramo no tiene criterio de cierre | T2 |
| 5 | ¿La PC del estudio lleva runner propio o se resuelve con cloud? | el modo R1/R2 queda sin soporte | T3 |
| 6 | ¿Cómo se publica el cuaderno para alguien sin conocimientos técnicos? | el cuaderno no llega a quien lo necesita | T5 |
| 7 | ¿Visión por computadora en obra? (modelo local / solo EXIF y tags / después) | las fotos quedan sin indexar más allá del tag | T6 |
| 8 | ¿Dónde viven las fotos de obra? (Nextcloud+Memories / Immich / el vault) | hay que elegir dónde queda el archivo | T6 |
| 9 | ¿Rhino 8 o Rhino 9? | la licencia y el flujo de Grasshopper | T3 |
| 10 | ¿Se firma el DPA de Runpod y se pide la confirmación de no-entrenamiento? | el nodo GPU no se puede usar | T5 |
| 11 | ¿El producto se ofrece como servicio mensual o como instalación por estudio? | define el perfil de despliegue | T6 |

---

# 11 · Plan de entrega

El plan sigue las fases del briefing (`raw/docs/plan-hermes.md` §14) reordenadas por criterio de valor, y se rearma con VISION y ESTRUCTURA encima de la mesa.

| Tramo | Fases del briefing que cubre | Qué se entrega | Criterio de salida |
|---|---|---|---|
| **T0 · Inventario** | Fase 0 | números reales del VPS y del equipo local | baseline documentado |
| **T1 · Cimientos del agente** | Fase 1 | vault canónico, red privada, Hermes en el VPS, MCP de n8n, `SOUL` y skills | AC-13, AC-18 |
| **T2 · Contrato y registro** | Fase 1 (parte 2) | sobre de tarea, schema del registro, API de escritura única | AC-01 a AC-05 |
| **T3 · Primer motor** | Fase 2 | auditoría de planos de punta a punta sobre el caso real | AC-06, AC-07, AC-09, AC-12 |
| **T4 · Interfase** | Fase 7 (parcial) | Telegram con temas, canal de bitácora, aprobaciones, digest | AC-08, AC-14, AC-15, AC-16 |
| **T5 · Imagen y cuaderno** | Fases 3 y 4 | flujo de render con procedencia y cuaderno digital navegable | AC-10, AC-11, AC-17 |
| **T6 · Piloto** | Fases 5, 6 y 7 | obra, entregas, cliente, y el sistema auditado en un proyecto real | AC-09, AC-14, AC-18 + métricas |

**Las tres primeras tareas concretas** (con comandos y scripts) están en el tramo T0-T1 de [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#9 · Puesta en marcha|ESTRUCTURA §9]].

**Reglas de construcción**

1. Nada se instala ni se ejecuta sin un `s` explícito.
2. Cada tramo se cierra con **criterios de aceptación**, no con "ya funciona".
3. Cada cambio en el VPS queda en el log de sesión y en el log del vault.
4. Si un tramo no cierra, se frena ahí: no se pasa al siguiente.

---

# 12 · Trazabilidad

| Origen | Dónde se usó |
|---|---|
| `raw/docs/plan-hermes.md` §13 (contratos) | §4 RF-01 a RF-04, §5 RNF-03 y RNF-04 |
| `raw/docs/plan-hermes.md` §14 (fases) | §11 plan de entrega |
| `raw/docs/plan-hermes.md` §15 (pruebas) | §6 criterios de aceptación |
| `raw/docs/plan-hermes.md` §16 (niveles A-D) | §7 gobernanza |
| `raw/docs/plan-hermes.md` §17 (métricas) | §9 |
| `raw/docs/plan-hermes.md` §5 a §10 (integraciones y casos) | §3 casos de uso |
| `proyectos/STUDIO_OS-Emilia/03-cuestionario-plan-studio-os.md` | §1 alcance, §5 RNF-02, §9 baseline |
| `raw/research/2026-10-28-runpod-auditoria-pi.md` | §5 RNF-05, §10 decisión 10 |
