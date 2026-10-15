---
tipo: manual
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha: 2026-10-08
version: 1.0
tags: [manual, telegram, fathom, cal-com, drive, studio-os, emilia]
---

# Studio OS — Qué hacen tus automatizaciones (guía para Emilia)

> Este documento explica, sin tecnicismos, los dos flujos automáticos de tu Studio OS: **reuniones** (Fathom) y **agenda** (Cal.com). Todo se opera desde Telegram, con la computadora apagada.

## 0 · El sistema en 30 segundos

Tenés un asistente privado en Telegram (`@emiliaospi_bot`) conectado a tres cosas: tus reuniones de Fathom, tu agenda de Cal.com y tu carpeta de Drive `OS-Emilia`. Vos le escribís, él ejecuta. Cada mañana a las 07:00 además trabaja solo: trae las reuniones nuevas del día anterior y las archiva.

## 1 · Flujo Reuniones (automático)

**Qué hace:** cada mañana a las 07:00 trae tus reuniones nuevas de Fathom y guarda, por cada una, dos archivos en tu Drive:

- Un documento de texto (`.md`) con resumen, acuerdos, tareas pendientes y transcripción completa.
- Un documento de Google (`.gdoc`) con el mismo contenido, formateado para leer.

**Dónde aparece:** en tu Drive, carpeta `OS-Emilia`:

| Carpeta | Qué va ahí |
|---|---|
| `Reuniones-Internas` | Reuniones solo entre vos y Proyecto Pi. Se nombran `fecha_emilia-proyectopi_ID.md` |
| `Reuniones-Clientes` | Reuniones con alguien más (clientes, proveedores). Se nombran `fecha_emilia-nombre-cliente_ID.md` |

La clasificación es automática: si participa alguien fuera del equipo, va a Clientes.

**Qué tenés que hacer vos:** nada. Solo que tus reuniones se graben en Fathom como siempre. Si querés traerlas en el momento sin esperar a las 07:00, mandale `/sync` al bot.

## 2 · Flujo Agenda (a pedido)

**Qué hace:** crea una reunión real en tu Cal.com y **le manda la invitación por email a tu invitado** automáticamente. A vos te llega la confirmación por Telegram y el evento aparece en tu calendario.

**Cómo se usa:** un solo mensaje al bot, con este formato:

```
/agendar DD/MM HH:MM Nombre
```

Ejemplos reales:

```
/agendar 15/12 10:00 Sol Test
/agendar 09/10 15:00 María González mariag@mail.com
```

- La **fecha y hora** son las de Argentina (el sistema convierte solo).
- Si ponés el **email al final**, lo usa directamente.
- Si **no ponés email**, lo busca en tu hoja `clientes-contactos` por el nombre. Si no lo encuentra, el bot te avisa y te pide que reenvíes el mensaje agregando el email.

**Qué recibe tu invitado:** un email de Cal.com con la fecha, la hora y el link de la videollamada. Hoy las reuniones salen de 30 minutos con link de Cal Video; en la reunión de mañana definimos juntos el evento de 1 hora con Google Meet y queda configurado.

**Qué tenés que tener:** tu hoja `clientes-contactos` al día (columnas `nombre`, `email`, `activo`). Cada contacto que agregues ahí después se agenda solo con el nombre, sin escribir el email.

## 2b · Cambiar o cancelar una reunión (sin códigos)

No necesitás saber ningún código. Pedí la lista y elegí:

```
/cancel
```

El bot te muestra tus próximas reuniones, cada una con su botón **Cancelar esta reunión**. Tocás el botón de la que quieras cancelar y listo: se cancela en Cal.com y se avisa por email.

```
/modif
```

El bot te muestra la lista numerada. Respondés con el número y la nueva fecha y hora:

```
/modif 1 10/10 17:00
/modif 2 18:00
```

Si ponés solo la hora, se entiende el mismo día de esa reunión. Si sabés el código (empieza con `Ref:` en los mensajes de confirmación), también vale `/modif <Ref> DD/MM HH:MM` y `/cancel <Ref>` directo.

## 3 · Comandos del bot

| Comando | Qué hace |
|---|---|
| `/help` | Muestra la ayuda con los comandos |
| `/sync` | Trae ahora mismo las reuniones nuevas de Fathom (sin esperar a las 07:00) |
| `/agendar DD/MM HH:MM Nombre [email]` | Crea la reunión en Cal.com e invita por email |
| `/cancel` | Lista tus próximas reuniones con botón para cancelar |
| `/modif` | Lista numerada; después `/modif N DD/MM HH:MM` o `/modif N HH:MM` |

## 4 · Tu mapa de carpetas en Drive

```
OS-Emilia/
├── Reuniones-Internas/     ← reuniones del equipo (automático, 07:00 o /sync)
├── Reuniones-Clientes/     ← reuniones con terceros (automático, 07:00 o /sync)
├── Contratos/              ← documentos del proyecto
└── clientes-contactos      ← tu hoja de contactos (la alimentás vos)
```

## 5 · Si algo no sale (preguntas frecuentes)

- **Mandé `/sync` y no aparece nada nuevo:** no había reuniones nuevas desde la última sincronización. Todo lo ya traído no se duplica.
- **Mandé `/agendar` y me dice que no entiende:** revisá el formato — `/agendar` + fecha `DD/MM` + hora `HH:MM` + nombre. Sin comas ni guiones.
- **Me dice que no encontró el email:** ese nombre no está en `clientes-contactos`. Agregalo a la hoja, o reenviá el mensaje con el email al final.
- **El bot no responde:** escribime por el canal habitual y lo revisamos. Tus reuniones de Fathom y tu Cal.com siguen intactos: el bot solo lee y organiza, nunca borra.
- **Quiero cambiar la duración o la videollamada por defecto:** lo vemos juntas (es una configuración única en Cal.com, no algo de todos los días).

---

*Documento vivo v1.0 — acompaña la reunión del 09/10. Referencia técnica (para el equipo): `arquitectura-n8n-os-emilia.md`.*
