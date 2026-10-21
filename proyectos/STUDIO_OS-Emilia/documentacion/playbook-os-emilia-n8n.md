---
tipo: manual
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha: 2026-10-16
version: 2.0
tags: [manual, telegram, fathom, cal-com, drive, studio-os, emilia]
---

# Studio OS — Qué hacen tus automatizaciones (guía para Emilia)

> v2.0 — Reemplaza v1.0: la agenda ahora se habla en lenguaje natural (voz o texto), sin comandos con slash. Todo se opera desde Telegram, con la computadora apagada.

## 0 · El sistema en 30 segundos

Tenés un asistente privado en Telegram (`@emiliaospi_bot`) conectado a tres cosas: tus reuniones de Fathom, tu agenda de Cal.com y tu carpeta de Drive `OS-Emilia`. Le hablás o escribís normal, él ejecuta. Cada mañana a las 07:00 además trabaja solo: trae las reuniones nuevas del día anterior y las archiva.

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

## 2 · Flujo Agenda (hablado, sin comandos)

**Qué hace:** crea una reunión real en tu Cal.com y **le manda la invitación por email a tu invitado** automáticamente. A vos te llega la confirmación por Telegram y el evento aparece en tu calendario.

**Cómo se usa:** le escribís o hablás normal, como a una secretaria:

```
agendame con María González mañana a las 10
cancelá la del jueves
cambiala a las 17
qué tengo esta semana
```

- El bot resuelve el contacto en tu hoja `clientes-contactos` y, si falta el email, te lo pide.
- Antes de escribir en tu agenda siempre muestra el resumen y pide Confirmar.
- Si pedís por voz, cita lo que entendió antes de confirmar.

**Qué recibe tu invitado:** un email de Cal.com con la fecha, la hora y el link de la videollamada. En la reunión de cierre definimos el evento de 1 hora con Google Meet y queda configurado.

**Qué tenés que tener:** tu hoja `clientes-contactos` al día (columnas `nombre`, `email`, `activo`). Cada contacto que agregues ahí después se agenda solo con el nombre, sin dictar el email.

**Regla de oro:** mover y cancelar siempre desde el bot (o Cal.com), nunca desde Google Calendar — editar en Google huérfana el turno en Cal.com y el próximo cambio rebota.

## 2b · Links al grupo Fuentes (memoria del estudio)

Mandá links de YouTube, Instagram, notas o libros al grupo Fuentes. El bot los anota solo (responde "Anotado ✓") y quedan en la cola `Fuentes-Inbox` para analizarse y recordarse dónde quedó cada uno.

## 3 · Comandos del bot (solo 2)

| Comando | Qué hace |
|---|---|
| `/help` | Muestra la ayuda |
| `/sync` | Trae ahora mismo las reuniones nuevas de Fathom (sin esperar a las 07:00) |

Todo lo demás (agendar, cancelar, modificar, listar) se habla en lenguaje natural, sin slash.

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
- **El bot me pide el email:** ese nombre no está en `clientes-contactos`. Pasale nombre + email y lo agrega solo.
- **El bot no responde:** escribime por el canal habitual y lo revisamos. Tus reuniones de Fathom y tu Cal.com siguen intactos: el bot solo lee y organiza, nunca borra.
- **Quiero cambiar la duración o la videollamada por defecto:** lo vemos juntas (es una configuración única en Cal.com, no algo de todos los días).

---

*Documento vivo v2.0 — cierre Mes 1. Referencia técnica (para el equipo): `arquitectura-n8n-os-emilia.md` v2 + `resumen-flujo-voz.md` + `resumen-flujo-agenda-sub.md`.*
