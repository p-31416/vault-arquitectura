---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
estado: borrador
tags: [cierre-mes1, pomodoros, leantime, calculadora-costos, n8n, studio-os]
idioma: es
---

# Cierre Mes 1 + cómputo real + calculadora — Studio OS Emilia

> Mes 1: 16/09 → 16/10/2026. Reunión cierre: 14/10. Límite contractual: viernes 16/10. Contrato final en [[proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia-2026-09-24|contrato 24/09]] (adelanto 300 abonado 22/09, próxima Factura C 600 el 16/10 vence 23/10).

## SPEC

Objetivo hoy 13/10: dejar lo mayor verificado para presentar mañana un reporte de cierre con números reales y abrir Mes 2 EXPERIMENTAR con precio anclado a horas liberadas.

Enfoque aprobado: cada plan avanza en pomodoros de 25 min que avanzan a Leantime como tasks ≤25 min interlinkeadas, con registro de horas del botón de Leantime como cómputo exacto. Proyecto Leantime: `O.S_ARQ-Emi` id 4, usuaria Emilia id 5 **aceptada el 13/10** (ver [[specs/260929-alta-emilia-leantime|alta Leantime]] y sesión 09/10).

Base técnica: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n v1.3]] + manual [[proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n|playbook Emilia v1.0]] + plan [[specs/260924-plan-os-emilia-n8n|plan OS-Emilia n8n]] + trimestral [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]] + esquema [[specs/260909-esquema-mes1-60hs-studio-os-emilia|esquema Mes 1]].

## PLAN semanal

* Hoy 13/10: verificación técnica + limpieza + factura lista + demo Leantime.
* Mañana 14/10: presentación de todo lo trabajado en el mes (reporte cierre Mes 1 en vivo con Emilia).
* Jue 15/10 tarde → vie 16/10 mañana: ventana M4 cierre real. Vie 16 mañana: factura C 600. Vie 16 post-mediodía: reunión cierre real con Emilia (horario a confirmar ~12-14h, agendar en Cal.com).

Tipos de hora para el cuadrito réplica: `arq | n8n-build | api | data | prompt-eng | qa | docs | devops-vps | seguridad`.

## TASKS — checklist hoy 13/10

### A. Limpieza y verificación n8n — VERIFICADO 13/10 (corre en Drive)

- [x] A1 Reserva prueba cancelada / sin choque (verificado por Sol 13/10).
- [x] A2 Duplicados Drive resueltos: Fathom Core solo levanta últimas 26h (`created_after -26h`), sin copias `(1)(2)(3)`.
- [x] A3 Fathom Core `OS-Emilia-Fathom Core` ejecutado hoy 07:00 OK, con división Internas/Clientes.
- [x] A4 `/help` + `/sync` operativos en Telegram.
- [x] A5 `clientes-contactos` en edición activa por Sol (base `clientes.csv` + filas reales).

### B. Leantime con Emilia aceptada — CARGADO 13/10 en proyecto 4

- [x] B1 Proyecto `O.S_ARQ-Emi` id 4 + usuaria Emilia id 5 aceptada, rol `inherit`.
- [x] B2 Milestones creados: M1 id 443 + M2 id 444 + M3 id 445 + M4 id 446 (renombrado 13/10: cierre real jue 15 tarde → vie 16 mediodía, timeline 15→16/10). Tasks O1/O2/O3 + KR + cierre ids 447-453 + factura 454 + reunión cierre 455 + doc Codex 456, con `planHours 0.42` linkeadas por `milestoneid`. GOAL: crear a mano en UI (la API no expone servicio Goals) y linkear M1-M4. Verificar en `https://pitautech-leantime.3nq4ow.easypanel.host/projects/showProject/4`.

### C. Números cierre Mes 1 (2h, 5 pomodoros)

- [ ] C1 Tabla tracking 60hs por bloque (vault/Fathom/CAD/doc/reuniones) con desvío vs planificado.
- [ ] C2 Medición 3 procesos manual vs sistema (ej: buscar plano 15→2 min, presupuesto 2h→0.5h, informe obra).
- [ ] C3 Cálculo ahorro proyectado ≥12hs/mes como base ROI Mes 2.
- [ ] C4 Factura C 600 USD: se emite vie 16/10 mañana (vence 23/10: saldo Mes 1 + Mes 2 adelantado).
- [ ] C5 Borrador roadmap Mes 2 EXPERIMENTAR con precio por módulo anclado a horas liberadas.
- [ ] C6 Agendar reunión cierre real vie 16/10 post-mediodía con Emilia en Cal.com (propuesta ~12-14h, confirmar disponibilidad) + acta.
- [ ] C7 Doc evaluación Codex/ChatGPT Mes 2: PC vs celular, versión online vs escritorio (la online no iguala capacidades desktop), definición de dispositivo de uso de Emilia.
- [ ] C8 Estándares CAD (en curso por Sol): bloques referencia replanteo de muros + documentación curso miniobras + bloques propios + demo conteo de bloques a planilla (solo CAD, sin BIM, sin 3D). Meta Mes 2: CAD bien usado de un tipo de plano.

### D. Calculadora costo réplica v0.1 — VERIFICADA 13/10

- [x] D1 Despiece flujos en pomodoros: Router 3 + Agenda 6 + Cancel/Modif 4 + Fathom 8 + agente/voz/memoria 6 = 27 pomodoros = 11.25hs.
- [x] D2 Script `scripts/calculadora-costo-flujo-n8n.py` + `scripts/calculadora-costo-flujo-n8n_notas.md` (runnable, solo stdlib). Comando: `P:\Anaconda\envs\comfyenv\python.exe scripts/calculadora-costo-flujo-n8n.py --ejemplo-emilia`.
- [x] D3 Variables con defaults a confirmar: tokens 2000/500 por exec × 900 exec/mes + VPS 15 + mantenimiento 2hs×12.
- [x] D4 Resultado verificado: réplica USD 128.33 + operativo USD 39.36/mes (tokens **0.36**, ínfimo) + valor USD 180/mes + 1.2× inversión + payback réplica 0.7 mes. Task Leantime id 457 en M4.

## Estado Goals al 13/10 (revisión Sol)

### O1 Adopción — 50% (At Risk)

Vault trabajado siempre por Sol; Emilia no sincroniza manual ni opera Antigravity/Codex desktop — trabaja con GPT online, que no iguala capacidades desktop. Plan remedial mañana 14/10 para cerrar el 50%: definir dispositivo (PC vs celular), instalar Codex desktop + vault sincronizado en su PC, primera ficha alimentada por ella en vivo con verificación personal de Sol. Doc soporte: task 456.

### O2 Números reales — reporte base 16/09→13/10

* 30 sesiones en `raw/sessions/` + 11 transcripts Fathom en `raw/reuniones/` (17/09, 24/09, 26/09, 03/10).
* Sol confirma el total de horas de su registro (número en su cabeza); desde hoy la metodología oficial es carga de horas en Leantime con el botón Time Tracking por task ≤25 min, visible para Emilia. Metodología: 1 task = 1 pomodoro 25 min (`planHours 0.42`); al terminar cada bloque se registra el tiempo real en el botón; el desvío plan vs real sale del propio Leantime.
* Pendiente: Sol sube las horas del mes a Leantime antes del vie 16.

### O3 Herramientas — lista de lo construido en el mes

* Automatización Telegram → evoluciona a agente IA (Router + Agenda + Cancel/Modif + Fathom Core, [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n]]).
* [[proyectos/MVP_01-dibujo_ia|MVP_01 dibujo IA]] + [[proyectos/MVP_02-autocad-standards|MVP_02 estándares CAD]] (bloques replanteo muros, miniobras, conteo bloques→planilla sin BIM/3D).
* [[proyectos/MVP_04-comfyui-arquitectura|MVP_04 ComfyUI]] en dos etapas (+ [[proyectos/MVP_04.02-comfyui-arquitectura|MVP_04.02]]: WF-01 planta ilustrada, IP-Adapter, serie controles).
* [[proyectos/MVP_06-agente-voz|MVP_06 agente voz]] (Handy + Parakeet español) + [[proyectos/MVP_05-rhino-mcp|MVP_05 Rhino MCP]] + [[proyectos/MVP_03-calhon-gest|MVP_03 honorarios]].
* MCPs conectados: Leantime, n8n, Fathom, Autodesk; Vault con agentes + ingesta (specs 261009).
* Plan Comfy: Emilia sin Comfy instalado. Opción A: flujo upscale armado para correr en PC Emilia (bajar modelos primero, ver qué pasa). Opción B: probar en PC Sol los modelos de croquis vistos hoy y llevar demo. Decisión mañana.
* Pendiente: revisar link de Emilia con sus conversaciones GPT (pasar el link).

## GOAL — cómo completarlo a mano (exacto, 10 min)

> La API no expone servicio Goals (verificado `Service doesn't exist`), así que el GOAL va en la UI. Límite conocido de Leantime: **1 milestone por goal** (issue #2939), por eso creamos 3 goals, 1 por OKR.

1. Abrir `https://pitautech-leantime.3nq4ow.easypanel.host/projects/showProject/4` → menú izquierda **Goals** → **Create Goal** (o New Goal).
2. Goal 1: título `O1 Adopción — vault en uso diario`. Métrica tipo `number`: inicio 0, actual 8, meta 8 (cargado 13/10). Fechas 16/09→16/10. **Link Milestone** → `M1 Vault vivo`.
3. Goal 2: título `O2 Números reales — 60hs + ROI Mes 2`. Métrica `number`: inicio 0, actual 65, meta 60 (cargado 13/10). Mismas fechas. **Link Milestone** → `M4 Cierre real` (id 446 recuperado a milestone 13/10: si no aparece, recargar).
4. Goal 3: título `O3 Herramientas — ahorro ≥12hs/mes`. Métrica `number`: inicio 0, actual (ahorro medido a hoy), meta 12. **Link Milestone** → `M3 Estándares CAD`.
5. Volver a Goals y verificar: 3 goals con barra de milestone + valor actual. Cada vez que completes tasks, sube el `Current Value` a mano (la API no lo mueve solo).

## Presentación mañana 14/10 — guion (30 min) + cierre del día

1. **Contrato y números (5 min):** 190h trimestrales, adelanto 300 cobrado 22/09, Factura C 600 el vie 16 (vence 23/10). Mostrar M4 en Gantt.
2. **Vault + Fathom en vivo (7 min):** `/sync` trae la última reunión a Drive (Internas/Clientes), cron 07:00 corriendo, 8 reuniones en `raw/reuniones/`.
3. **Agenda en vivo (5 min):** `/agendar` con email real → booking Cal.com + invitación por email + confirmación con Ref. Mostrar `/cancel` y `/modif`.
4. **CAD (7 min):** bloques replanteo de muros + docs curso miniobras + bloques propios + demo conteo de bloques a planilla (solo CAD, sin BIM, sin 3D).
5. **Números Mes 1 (3 min):** tracking 60hs por bloque + 3 procesos manual vs sistema + ahorro ≥12hs/mes como base de precio Mes 2.
6. **Mes 2 + cierre (3 min):** Codex PC vs celular (doc 456), CAD bien usado de un tipo de plano, evento 60 min con Meet, cierre real vie 16 post-mediodía + factura vie 16 mañana.
7. **Cierre del día de hoy:** con este spec cerrado, la presentación de mañana queda armada. Al fin del día repasamos el guion 1-6 y tildamos M1-M4.

## MILESTONES y OKRs — checklist firmado Mes 1 (contrato + Anexo I + esquema)

> Fuente firmada: [[specs/260909-esquema-mes1-60hs-studio-os-emilia|esquema Mes 1]] + [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]] + contrato 24/09 (190h trimestrales, Anexo I S1-S4 + hitos W01-W04). Objeto: Nayara Brasil, operado como Magenta en 17/09.

### Milestones (Go/No-Go)

- [x] M1 Vault vivo (W01 día 5): vault operativo en PC Emilia + 1 reunión Fathom transcripta en `raw/reuniones/` + guía wiki + agentes agenda/transcripción funcionando. Verificado 13/10 (A1-A5).
- [ ] M2 Representación (W02 día 10): carpeta 20-30 referentes con ficha qué tomar/dejar + códigos color/visual + sistema representación v0 + demo moodboard genérica.
- [ ] M3 Estándares CAD (W03 día 15): DWT/layers/puntas/bloques/láminas/rótulos + apoyo Lisp con IA, validados sobre objeto de estudio + fichas `wiki/estandares/`.
- [ ] M4 Cierre (ventana jue 15 tarde → vie 16 mediodía): doc Mes 1 completa + clase 2h dada + accesos Leantime/vault + roadmap Mes 2 + factura 600 emitida vie 16 mañana + reunión cierre real vie 16 post-mediodía + acta S4.

### Goals / OKRs Mes 1

- [ ] O1 Adopción: 8/8 reuniones transcriptas vía Fathom en `raw/reuniones/` <24h + Emilia alimenta 1 ficha/sem con autonomía + 8/8 rituales (Lun 0.5h + Mié 1.5h) + 1 junior opera solo en S4.
- [ ] O2 Números reales: 60hs trackeadas por bloque con desvío <10% + 3 procesos medidos manual vs sistema + roadmap M2 con precio anclado a horas liberadas.
- [ ] O3 Herramientas: 8 fichas wiki vivas + 1 flujo Fathom→vault funcionando + 20-30 referentes curados + ahorro proyectado ≥12hs/mes medido en S4.

### Emilia OS — criterios de aceptación MVP (para tildar con Emilia 14/10)

- [x] Agenda: `/agendar DD/MM HH:MM Nombre [email]` crea booking real Cal.com + invita por email + confirma en Telegram con Ref. Verificado 08/10 (reserva `gnCrXcR1j3mz8Hd9THXhyh`).
- [x] Reconfiguración: `/cancel` lista con botón + `/modif N DD/MM HH:MM` reprograma sin pedir Ref. Verificado 08/10.
- [x] Fathom: `/sync` + cron 07:00 `America/Argentina/Buenos_Aires` guardan .md + Google Doc en `Reuniones-Internas/Clientes` sin duplicados. Verificado 13/10 (exec 07:00 OK).
- [ ] Hoja `clientes-contactos` al día (`nombre,email,activo`) + evento 60 min con Google Meet definido + Router cerrado al `chat_id` de Emilia.

## Fuentes

* [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia v1.3]]
* [[proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n|playbook-os-emilia-n8n v1.0]]
* [[specs/260924-plan-os-emilia-n8n|plan-os-emilia-n8n]]
* [[specs/260929-alta-emilia-leantime|alta-emilia-leantime]]
* [[proyectos/STUDIO_OS-Emilia/reuniones/2026-09-11-reporte-fathom-emilia-hoy|reporte Fathom 11/09]]
* Sesión [[raw/sessions/2026-10-08-sesion-n8n-fathom-agenda|sesión 08/10 n8n]] con execs 3489/3495/3500/3505/3525.
