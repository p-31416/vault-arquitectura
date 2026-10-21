---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [emilia, os-studio, n8n, cal-com, sesion-2026-10-21, agenda, checklist]
---

# Qué le pedimos a Emilia — sesión del miércoles 21/10 (13:00)

Guía de la sesión: Emilia **va a tener su propio flujo completo** (agente de voz propio + subagente de agendamiento propio + su cuenta Cal.com). Antes de la sesión solo falta que nos dé **3 datos** y que haga **2 clics**.

Complementa [[proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21]] (arquitectura y plan) y [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia]] (guion original).

---

## 1. Lo que YA está listo (no hay que pedirle nada)

| Pieza | Estado |
|---|---|
| Cuenta Cal.com de Emilia | 3 tipos de reunión creados: **7563141** presencial · **7563142** online/Meet · **7563143** libre (oculto). Slots verificados (8/día, 09-16) |
| Calendario destino | ya estaba conectado en Cal.com (`arq.emiliapimentalombardi@gmail.com`) → **las reservas caen en su calendario** y Cal.com le resta sus ocupados |
| Flujo de voz propio | `OS-Studio — Agent Voz Emilia` — Telegram (texto + voz con Gemini), debounce Redis `studio_os_emilia_<chat_id>`, memoria `studio_os_emilia` |
| Subagente de agendamiento propio | `OS-Studio — Agenda Sub Emilia` — 7 tools contra **su** cuenta Cal.com, con sus 3 event types |
| Despacho por identidad | `OS-Studio — Voz Dispatcher` — tu chat va a tu flujo, el de ella al de ella |
| Planilla de clientes | la misma compartida (`clientes-contactos` / hoja `clientes`) |

---

## 2. Los 3 datos que hay que pedirle

| # | Qué le pido | Para qué sirve | Dónde se carga |
|---|---|---|---|
| **1** | **Su `chat_id` de Telegram** (o que mande un mensaje al bot y lo sacamos de la ejecución) | que su chat entre a **su** flujo y no al tuyo | 2 lugares: Router `YWpuV5p0vCDTbIHz` → `Route Telegram Command` → regla 2 → `rightValue`; y `Fa2AlIDqUntSWMrw` → `Detectar Entrada Emilia` → `const PERMITIDO = 999999999;` |
| **2** | **La dirección del estudio** | que las reuniones presenciales tengan ubicación | Cal.com → event type `7563141` → Location → Address. (En el bot, `agendar_presencial` **no** manda dirección: la hereda del event type → se actualiza en un solo lugar) |
| **3** | **Que comparta su calendario profesional con `proyectopi.31416@gmail.com`** | que el agente vea también lo que ella agenda a mano (`leer_calendario`) | Google Calendar → configuración del calendario → "Compartir con usuarios" |

> El `chat_id` se lee solo: en n8n → `OS-Emilia — Telegram Router` → ejecuciones → la última → `Recibo Mensaje` → `message.chat.id`. Es un número (ej. `8459099332` es el tuyo).

---

## 3. Preguntas para confirmar (no bloquean)

| # | Pregunta | Para qué | Dónde |
|---|---|---|---|
| 4 | ¿Está bien el horario **L-V 9 a 17**? | los slots disponibles | ya está en Cal.com (schedule "Horas laborables") |
| 5 | ¿Qué duraciones quiere ofrecer? (60 / 120 / 180) | las opciones de la reunión | **solo en la UI de Cal.com**: la API responde `success` pero **no aplica** `metadata.multipleDuration` (ver [[wiki/glosario/software/leantime#Lecciones técnicas de hoy (20/10)\|notas de la sesión]]) |
| 6 | ¿El ET "Disponibilidad libre" (7563143) tiene que ser 24/7? | asignarle el schedule "Disponibilidad 24/7" (`2527411`, ya creado) | UI de Cal.com (misma limitación de la API) |
| 7 | ¿Usa el bot por **voz**, por **texto** o por los dos? | validar la transcripción de Gemini | prueba en vivo |
| 8 | ¿Quiere que el bot proponga **2 horarios** alternativos cuando le piden uno? | prompt del agente | opcional |
| 9 | ¿El email de contacto es `arq.emiliapimentalombardi@gmail.com`? | confirmador de invitados | ya está en Cal.com |
| 10 | ¿Usa el calendario personal aparte del profesional? | segundo calendario en `leer_calendario` (fase 2) | opcional |

---

## 4. Prueba en vivo (10 min, en este orden)

1. **Texto**: que mande "hola" → el bot responde desde **su** flujo.
2. **Agenda online**: "agendame una reunión con Juan Pérez (juan@test.com) el jueves 22 a las 11" → confirmar → queda en **su** Cal.com **y** en **su** Google Calendar.
3. **Ver**: "¿qué reuniones tengo esta semana?" → lista las suyas (no las tuyas).
4. **Mover**: "mové la de Juan a las 15" → `actualizar_reunion`.
5. **Cancelar**: "cancelala" → `cancelar_reunion`.
6. **Voz**: que mande un audio con un pedido → el bot transcribe y responde.
7. **Presencial**: "agendame una presencial con Juan el viernes 23 a las 10" → aparece la dirección real.
8. **Contacto nuevo**: que pida una reunión con alguien que no está en la planilla → el bot da de alta el contacto.

Checklist: [ ] texto · [ ] online · [ ] ver · [ ] mover · [ ] cancelar · [ ] voz · [ ] presencial · [ ] contacto nuevo

---

## 5. Lo que YA NO hay que decidir (quedó cerrado)

- **Un solo trigger de Telegram** (obligatorio: 1 webhook por bot) → el Router reparte y el Voz Dispatcher decide el flujo.
- **Un flujo por persona**: el de ella no comparte Redis, ni memoria, ni credencial de Cal.com, ni agent types.
- **La planilla de clientes es una sola** (compartida con vos) — a pedido de que no se dupliquen los contactos.
- **El calendario destino es el profesional**; el personal, en fase 2, como free/busy (no bloquea).
- **No hace falta autorizar nada de Google**: el calendario de Emilia ya estaba conectado en Cal.com.
- **No hace falta que el bot sea otro**: es el mismo `@emiliaospi_bot`, con un flujo distinto por `chat_id`.

---

## 6. Si algo falla en la sesión

| Síntoma | Qué mirar | Arreglo |
|---|---|---|
| No entra ningún mensaje al bot | el webhook de Telegram | desactivar y **volver a publicar** `OS-Emilia — Telegram Router` |
| El bot responde "no puedo leer tu calendario" | falta compartir el calendario | punto 3 de la sección 2 |
| El bot no encuentra el contacto | la planilla | verificar el email; el bot da de alta el contacto solo |
| Agendar da error de slots | el horario L-V 9-17 | probar dentro del horario, o ampliar el schedule en Cal.com |
| El bot quedó mudo después de un mensaje | Redis con mensajes viejos | `OS-Studio — Limpiar Memoria TEST` (borra la memoria y la cola del chat) |
| Voz no transcribe | la credencial de Gemini | `Google Gemini(PaLM) Api account` en `Transcribir Voz` |

**Rollback de la arquitectura**: el flujo de Emilia es un workflow aparte (`Fa2AlIDqUntSWMrw`) → se archiva y el bot vuelve a ser solo tuyo, sin tocar nada más.
