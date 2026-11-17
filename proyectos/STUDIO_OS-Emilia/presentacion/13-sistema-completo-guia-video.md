---
tipo: presentacion
fecha_creacion: 2026-11-17
ultima_actualizacion: 2026-11-17
tags: [presentacion, studio-os, pi, cliente-no-tecnico, hermes, guia-video]
idioma: es
estado: borrador
formato: obsidian-md
---

# PI · Studio OS — El sistema completo en un solo documento

> Para la arquitecta titular. Sin tecnicismos. Este texto avanza como presentación al cliente y como guía del próximo video Remotion.
> Base viva en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · guion en [[specs/261101-guion-visual-pi-remotion|guion visual PI]].

**Idea en una frase:** un estudio chico trabajando con memoria, registro y compañía de un estudio grande, con el celular como puerta y la firma siempre en manos de la arquitecta.

**Cómo leer:** Parte 1 historia · Parte 2 lo que recibe · Parte 3 un día de uso · Parte 4 equipo invisible · Parte 5 piezas que ya existen · Parte 6 método · Parte 7 guía del video.

---

## 1 · La historia en 4 pasos — arquitecto, meta-arquitecto, empresa sintética, mirada completa

### 1.1 Arquitecto operador — una persona, una computadora

La arquitecta dibuja, espera el render, corrige, reenvía mail, anota compromiso en papel suelto. Todo avanza mientras ella está presente frente a la máquina. Capacidad limitada por horas y atención.

Video: lazo 1:1 que se cierra una y otra vez.

### 1.2 Meta-arquitecto artesanal — una directora con varios ayudantes

Sol hoy opera así: abre varias sesiones, reparte tareas entre agentes, sostiene scripts, workflows y vault. Produce más, con más mantenimiento. Cada línea de trabajo pide su atención.

El hallazgo: diseñar el proceso de diseño avanza hacia actividad de primer orden. Ver [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]].

Video: se multiplica la pantalla, los reportes vuelven al vault, una mano cura memoria.

### 1.3 PI · empresa sintética de capacidades — el sistema sostiene el flujo

PI organiza roles, memoria, automatizaciones y registros. Hermes coordina, n8n mueve eventos, los motores ejecutan en el lugar adecuado. La arquitecta pide por Telegram, recibe resultado con origen y aprueba lo importante. La computadora de ella avanza apagada si quiere.

Empresa sintética nombra un sistema de agentes por rol, memoria y workflows que coordina trabajo del estudio. Las personas conservan diseño, criterio y responsabilidad profesional.

Video: cerebro cuidado → Hermes → roles y workflows → ejecución local / VPS / GPU → registro + aprobación.

### 1.4 Meta-arquitecto sistémico — quien diseña y cuida el sistema + nota holo

El cierre es la arquitecta que diseña, gobierna y amplía el sistema que permite producir arquitectura. Observa métricas, versiones, costos, permisos y convierte aprendizaje validado en capacidad compartida.

Nota holoarquitecto (?): en borradores apareció `holoarquitecto` como imagen de mirada completa (holos = todo). Decisión vigente para el video: el protagonista final es el **meta-arquitecto sistémico**; `holo` queda como placa poética de esa mirada completa, con 5 pilares: cerebro cuidado, wiki viva, agenda que avisa, agentes por rol, mejora continua. Así el video continúa este documento sin cambiar nombres.

---

## 2 · Lo que el estudio recibe — 8 capacidades contadas en idioma de obra

| # | Pedido en el celular | Respuesta del sistema |
|---|---|---|
| 1 | "Agendame martes 10h con Juan" | Evento en agenda con link de video + invitación + confirmación en fecha argentina |
| 2 | "Qué tengo esta semana" | Lista clara con horas, personas y enlaces de acción |
| 3 | Audio de reunión → "hacé la minuta" | Resumen por tipo interna / cliente + minuta + borrador de mail en 24 h |
| 4 | Foto o render + "cambiá el cielo, piso de madera" | 2-3 variantes con semilla y parámetros, keeper elegido y registrado en portal |
| 5 | DWG + "auditame esto" | Informe PDF: capas, escalas, referencias, bloques, estándares, observaciones ordenadas, original intacto |
| 6 | DWG + "computame" | Tabla de partidas desde bloques con atributos, con aviso de lo que falta estandarizar |
| 7 | "Preparame el juego para imprimir" | PDF con formato de entrega listo para gestoría |
| 8 | Cada mañana 07:00 | Digest del día + avisos de compromisos por vencer |

Regla madre: la máquina prepara lo verificable, la persona firma planos, envía mails y entrega al cliente. Planos como documentos legales, Ley 24.335.

---

## 3 · Un día con el sistema — de punta a punta

> 09:12 Telegram: "Agendame mañana 10h con la cliente de Tigre por Jitsi". Hermes agenda, manda invitación, confirma en el chat.
> 11:30 Reunión por Jitsi. Audio al bot. A la tarde llega minuta + compromisos con fecha + borrador de mail para enviar.
> 16:00 Foto de croquis + "volvélo render cálido de tarde". Llegan 3 opciones con parámetros. La arquitecta elige una, queda guardada con su semilla.
> 18:20 DWG + "audit y cómputo". Informe + planilla, con hash que muestra original intacto.
> 07:00 día siguiente: digest con lo de hoy y aviso de entrega que vence mañana.

Todo deja rastro: de qué archivo salió, con qué versión y herramienta, con qué parámetros, quién aprobó, cuánto costó en tiempo y cómputo.

---

## 4 · El equipo invisible — como empleados, con una sola persona de contacto

### 4.1 Hermes — hablás con uno, él organiza al resto

Pensalo como una oficina chica que funciona bien: vos hablás con una sola persona de confianza por Telegram, ella reparte el trabajo al resto del equipo y vuelve con todo listo y anotado.

Ese es Hermes: vive en el servidor del estudio, siempre disponible. Recibe tu pedido, lo parte en pasos, lo pasa a los especialistas, junta el resultado y te lo entrega con su origen. Detalle técnico en [[specs/261116-plan-agentes-hermes|plan agentes Hermes]] y [[specs/261102-system-overview-pi|system overview]].

Roles claros: Sol diseña el sistema y supervisa la estructura. Emilia aporta al usarlo cada día: cada pedido, cada elección, cada corrección alimenta la memoria de la casa.

Por detrás, ese agente cuenta con conectores que leen archivos y programas del estudio y con ayudantes automáticos que mueven papeles entre agenda, mail y archivo. Emilia nunca abre nada técnico, solo conversa.

### 4.2 Los ππ (pipi) — empleados por oficio, mismo idioma

ππ se lee pipi y se escribe con doble pi como guiño a Pi. Cada ππ atiende un oficio:

| Equipo | Oficio | Qué hace por vos |
|---|---|---|
| PI Manager | encargada general | entiende tu pedido, arma el plan, reparte y reúne |
| ππ-pm (pipi-pm) | agenda y compromisos | agenda, resumen 07:00, recordatorios, minutas |
| ππ-docs (pipi-docs) | memoria y cuaderno | guarda fichas, decisiones, quién es quién por obra |
| ππ-cad (pipi-cad) | planos | revisa láminas, cuenta partidas, compara versiones |
| ππ-visual (pipi-visual) | imagen | prepara variantes y guarda la elegida con sus datos |
| ππ-bim (pipi-bim) | modelo futuro | revisa modelo 3D cuando el estudio lo use |
| ππ-ideas (pipi-ideas) | exploración | propone rumbos y referentes para elegir |

Mismo acuerdo en todos: entra pedido con proyecto, sale resultado con rastro y con tu visto donde importa.

### 4.3 El taller — quienes preparan, sin atender clientes

Sherlock busca afuera · Brainstormy abre opciones · Contenidos da forma legible · Vaultworm conecta y cuida la memoria. Trabajan en la máquina de Sol, preparan procedimientos que luego viajan aprobados al servidor. En el día a día, ππ-docs aplica ese mismo saber.

### 4.4 Subagentes de imagen — 7 pasos del render fiel

S1 base · S2 lugar y contexto · S3 textura con 3 opciones · S4 forma con respeto de plano · S5 estilo propio del estudio · S6 foto de fondo con uso declarado · S7 entrega comparada en portal + Telegram + Drive para tablet. Con tablet: 01-generada → 02-marcada-tablet → 03-regenerada, por nombre de archivo.

### 4.5 Tablero general — hoy Leantime, reparto entre personas y ππ

Hoy las tareas viven en Leantime. El tablero general junta en una sola vista lo de Hermes y lo propio: qué hace cada persona y qué hace cada ππ, en qué estado está y cuándo se entrega.

Emilia mira un solo lugar. Sol supervisa el reparto y cuida la estructura. Cada tarea muestra responsable, humano o sintético, y deja rastro al cerrarse.

---

## 5 · Las piezas que ya existen — MVPs integrados

| MVP | Qué aporta al sistema | Vive como |
|---|---|---|
| MVP_01 dibujo IA | lenguaje natural → AutoCAD | skills pipi-cad |
| MVP_02 estándares | layers, CTB, bloques con atributos | condición del cómputo |
| MVP_03 / 03b CalHon | honorarios y gestiones | registro + entrega trazable |
| MVP_04 ComfyUI | motor imagen / video local | skills pipi-visual, 3 rutas: máquina con GPU, pod por hora, API rápida |
| MVP_05 Rhino MCP | Rhino / Grasshopper por puente | skills pipi-cad para geometría |
| MVP_06 agente voz | Telegram voz → agenda + transcripción | flujos que Hermes invoca |
| MVP_07 Studio OS | sistema completo | este documento |
| MVP_08 casa moderna | keeper de identidad material | referencia de estilo |
| MVP_09 croquis-render + workerFLUX | carril local $0 + carril nube medido | batería de pruebas y dashboard |

Casos reales que alimentan: Aizpurúa, centro cultural Tigre, concurso Gaudí Nexus.

---

## 6 · Método — simple de contar, firme al operar

**Mapa de intervención:** Humano decide e interpreta · IA propone y transforma · Automatización transporta y registra · Información circula con origen.

**Niveles de riesgo en idioma claro:**

- A lectura y consulta — avanza solo
- B generación aislada (render, informe, minuta) — avanza solo y registra
- C modificación y agenda — pide su toque en el chat
- D envío y publicación — pide aprobación explícita, el envío lo hace persona

**Tres hábitos:** todo con origen y versión · nada valioso solo en la cabeza de una persona · mejora validada avanza hacia skill compartida.

Resultado → revisión → aprendizaje registrado → prueba → aprobación → capacidad reutilizable.

---

## 7 · Guía para el video Remotion — continuación directa de este documento, 86 segundos

Composición `PIStudioOS`, 1920×1080, 30 fps, textos cinéticos, música. Sin locución en primera versión.

| Escena | Seg | Texto en pantalla | Qué se dibuja | Parte de este doc que usa |
|---|---|---|---|---|
| 01 | 8 | PI · Plataforma de Inteligencia para arquitectura | Sello PI + arquitecta y computadora a lápiz | Portada |
| 02 | 10 | 1:1 una persona, una computadora | Flecha ida y vuelta, lazo que se repite | §1.1 |
| 03 | 13 | Meta-arquitecto artesanal, una directora | Múltiples pantallas, reportes al vault, mano que cura | §1.2 |
| 04 | 11 | PI, la empresa sintética en marcha | Cerebro → Hermes → roles → ejecución → registro | §1.3 + §4 |
| 05 | 15 | Una empresa de roles y lenguajes | Grafo: CAD · Rhino · Comfy · Docs · PM · QA conectados | §4 + §5 |
| 06 | 13 | Tres estaciones, un mismo contrato | Local / VPS / GPU, con costo y mantenimiento visibles | §6 |
| 07 | 13 | Comfy, una capacidad, muchas entradas | Texto / voz / croquis → workflow → resultado + semilla, prueba denoise 0.4 / 0.6 / 0.8 | §2 capacidades 4 + §4.4 |
| 08 | 10 | El meta-arquitecto diseña lo que sigue | Centro del grafo con métricas, arquitectas usando capacidades alrededor + placa holo 5 pilares | §1.4 |

Fórmula visible solo si suma: `P = trabajo validado / atención humana`, con tiempo, correcciones y costo al pie. La expansión se muestra como líneas de trabajo que crecen, con edición prudente.

Fuentes del relato separadas en 3 capas: hechos documentados (Foster, ZHA, Hermes docs, Dartmouth 1955/56) · tesis PI (deuda operativa avanza hacia capacidad con registro) · proyección de diseño (estudio aumentado). Detalle en [[specs/261101-guion-visual-pi-remotion|guion]].

---

## Anexo A · Glosario en 10 líneas

Hermes: coordinador · Pipi: perfil por oficio · Skill: procedimiento aprobado y versionado · Vault: memoria consultable · Trazabilidad: origen + versión + parámetros + aprobador · Digest: resumen 07:00 · Keeper: variante elegida · Seed: semilla que permite repetir · Portal: página de iteraciones · HITL: persona aprueba lo importante.

## Anexo B · Próximos pasos — 35 días, sprint 2 días

Semana 1 Hermes + bots + agenda · Semana 2 minutas · Semana 3 render + auditoría DWG · Semana 4 entrega + portal + demo. Gate final: demo punta a punta solo desde el celular.

> Mensaje para cerrar la reunión: "Vengo a entender cómo funciona el estudio y a diseñar el sistema que conecta lo que ya hacen con nuevas capacidades, con la firma siempre en sus manos."
