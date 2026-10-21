---
tipo: proyecto
cliente: Emilia Pimenta
proyecto: Studio OS
ciudad: Argentina
pais: AR
fase: briefing
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-16
estado: presentacion
tags: [dashboard, cierre-mes1, presentacion, studio-os]
---

# Dashboard cierre Mes 1 — Studio OS × Emilia

> Reunión cierre · 30 min · Formato: demo en vivo (Telegram + Drive + Leantime + CAD). Detalle técnico: [[specs/261013-plan-cierre-mes1-calculadora-emilia|plan cierre]] + [[specs/archived/261013-reporte-horas-mes1-emilia|reporte horas]] + [[specs/261016-plan-unificado-studio-os-quickwins|unificado quick wins]]. Semana 19/10: [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes Telegram + agenda]] + [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso Gaudí Nexus]].

## 1. El mes en un número

81hs trabajadas · 63 sesiones · 26 reuniones transcriptas (3 del 16/10 importadas desde Fathom Proyecto Pi) + dump 13/10 · Fathom Core 07:00 + Router/Agenda/Cancel/Modif corriendo · SET_01 replanteo como objeto real · adelanto 300 cobrado, factura 600 el viernes.

## 2. Esperado vs logrado (contrato + Anexo I)

| Frente | Esperado Mes 1 | Logrado al 13/10 |
|---|---|---|
| Vault vivo M1 | Vault + Fathom + agentes | ✅ Vault operativo + 20 transcripts + Router/Agenda/Cancel/Modif |
| Adopción O1 | 8 reuniones + rituales 2×/sem | 🔄 26 transcripts sí (incluye 09/10 ×3 PPI y 16/10 ×3 PPI), 1 aporte/sem Emilia por Telegram (cero wiki), demo /sync + /agendar por ella |
| Números O2 | 60hs + 3 procesos + roadmap | ✅ 81hs (65 al 13/10 + 16 semana cierre) / 3 procesos medidos / roadmap Mes 2 anclado a 13.5hs/mes |
| Herramientas O3 | 8 fichas + flujo + 20-30 refs + 12hs/mes | ✅ Flujos + SET_01 replanteo + 20 research + ahorro ~13.5hs/mes |
| Pagos | 300 + 600 | 300 cobrado 22/09 / 600 sale vie 16 |

## 3. MVPs tocados en el mes

| MVP | Qué se hizo | Evidencia |
|---|---|---|
| MVP_01 dibujo IA | Bloques por lenguaje natural (7 pasos: vano, puerta, ventanas) | Sesión 30/09 + log n_02 |
| MVP_02 estándares CAD | SET_01 replanteo (objeto real Mes 1, reemplaza Nayara): spec + ft + ADR único + 2 playbooks + DWT 13 bloques + LSP 29 capas + SET_02 DGIUR + auditoría REP-ARAOZ | Sesiones 27-28/09, 30/09, 05/10, 13/10, 16/10 |
| MVP_03b presupuestos | Presupuesto generado 02/10 | PDF 02/10 |
| MVP_04 ComfyUI | Research 949 líneas + plan 24h + moodboard v5 | Sesiones 19/09, 30/09, 08/10 |
| MVP_04.02 | WF-01 F-01..F-05 + IP-Adapter + WF-03 controles | Sesiones 08-09/10 |
| MVP_06 voz | Handy + Parakeet español operativo | Sesión 08/10 |
| Emilia OS (nuevo) | Bot Telegram + Cal.com + Fathom→Drive, cron 07:00 | [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura v1.3]] |
| Ingesta/agentes | YT 709 videos + Sherlock/Contenidos + PDF pipeline + Leantime | Specs 261009 + sesiones 08-09/10, 13/10 |

MVP_03 y MVP_05: base previa, sin sesión del mes.

## 4. Sesiones (63) y reuniones (26+1)

* **Contrato/legal (3):** 19/09 revisión · 24/09 cierre y PDF final · pack legal.
* **n8n (6+):** 24/09 plan + 5 continuaciones · 08/10 loop + agenda real · 13-14/10 inbox + rama IDEA.
* **CAD (10+):** metodología, fuentes, índices, bloques NL, SET_02, SET_01 playbooks + ADR 16/10.
* **ComfyUI/imagen (6):** moodboard, research, WF-01, WF-03, curación, VR.
* **Ingesta/agentes (8+):** YT 709 videos, grafo, Sherlock (20 research), PDF Baudrillard, Leantime, worker nube.
* **Voz/video/infra (4):** Handy, Remotion, MCPs, playbook 16/09.
* **Cierre (8):** 13/10 ×5 + 14/10 router + 16/10 ×4 (unificación, auditoría, SET_01, inbox).
* **Reuniones:** 28/08 ×4 · 11/09 ×4 · 17/09 ×4 · 24/09 ×2 · 26/09 ×3 · 03/10 ×2 + dump 13/10 + 09/10 ×3 Fathom Proyecto Pi (Emi OS + conocimiento + automatización/Comfy, md + Doc en Internas) + 16/10 ×3 Fathom Proyecto Pi (obra/CAD · concurso Gaudí Nexus · OS Emilia agentes + ComfyUI; planes en [[specs/261019-plan-agentes-telegram-agenda-emilia|agentes + agenda]] y [[specs/261019-plan-concurso-gaudi-nexus-ia|concurso]]).

## 5. Ahorro medido (base precio Mes 2)

| Flujo | Manual | Sistema | Ahorro/mes |
|---|---|---|---|
| Agendar ×8 | 15 min | 1 mensaje | ~1.9hs |
| Fathom ×11 | 45 min | 5 min revisión | ~7.3hs |
| Buscar plano ×20 | 15 min | 2 min | ~4.3hs |
| **Total** | | | **~13.5hs/mes ≥ 12hs meta** |

Capacidad liberada 0.22 · ROI Mes 1 0.17 · payback mes 7 (1.800 → 3.960 USD/año).

## 5. Demos en vivo (15 min, ella opera)

1. `/sync` desde su celular → .md en Drive.
2. `/agendar` un cliente real suyo → invitación por email.
3. `/cancel` y `/modif` con botones.
4. CAD: conteo bloques→planilla.

## 6. Cierre y Mes 2 (5 min)

* O1 al 50%: mañana instalamos tu Codex desktop y cerramos el otro 50% (PC vs celular, vault sincronizado).
* Vie 16 mañana: factura 600. Vie 16 post-mediodía: reunión cierre real.
* Mes 2: un tipo de plano bien usado en CAD + Codex + evento 60 min con Meet.

## 7. Semana 19/10 — planes de reuniones (16/10)

* 2 reuniones analizadas (Fathom `action_items` vacío → tareas derivadas del resumen + transcripción completa): [[specs/261019-plan-agentes-telegram-agenda-emilia|agentes Telegram + agenda + ComfyUI]] y [[specs/261019-plan-concurso-gaudi-nexus-ia|concurso Gaudí Nexus]].
* 32 tareas con dueño, criterio de cierre y pomodoros ≤25 min (≤16/día por persona) · hitos M-A1…M-A4 y M-B1…M-B6.
* Carga a Leantime preparada (19 cards en el proyecto 4 + 13 cards en el tablero del concurso), a la espera del visto bueno de Sol.
