---
tipo: manual
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [manual, mvp_06, telegram, agente-voz, uso]
---

# Manual de uso — Agente de voz Telegram

> Hablale o escribile con normalidad. Sin comandos, sin sintaxis. Todo funciona con la computadora apagada.

## 0. El sistema en 30 segundos

Tenés un asistente privado en Telegram conectado a tu agenda de Cal.com, tus reuniones de Fathom y tu carpeta de Drive. Le hablás por voz o le escribís, él ejecuta y confirma. Cada mañana a las 07:00 además trabaja solo: trae las reuniones nuevas y las archiva.

## 1. Hablarle por voz

Mantené el micrófono y hablá español normal, 10 a 60 segundos, siempre con el **nombre** del contacto:

* "Agendame mañana a las 10 con Juan Pérez"
* "Cancelá la reunión del jueves con María"
* "Cambiala a las 5 de la tarde"
* "Qué tengo esta semana"
* "Sincronizá mis reuniones"

El bot cita lo que entendió y pide confirmación antes de escribir en tu agenda. Si un nombre suena parecido a varios contactos, te propone candidatos.

## 2. Escribirle

Vale lo mismo por texto, con las mismas frases. Si preferís precisión, agregá fecha y hora (`mañana 15/10 10:00 con Juan`).

## 3. Revisar tu agenda

* "Qué tengo esta semana" — lista con fecha, contacto y código de cada reunión.
* "Cuándo veo a Juan" — filtra por contacto.
* "Listame las próximas" — las siguientes 5 con sus códigos.
* Cada reunión trae su código (`Ref:`): con ese código cancelás o modificás en el mismo chat ("cancelá la `Ref:abc123`", "movela al viernes 11:00").

## 4. Agendar, cancelar, modificar

* **Agendar:** decí fecha, hora y contacto. Si falta el email lo busca en tu planilla `clientes`; si no está, te lo pide y lo agenda igual con el email que le des.
* **Cancelar:** pedí la lista o nombrá la reunión; tocá el botón **Cancelar esta reunión** o confirmá por texto.
* **Modificar:** "movela al viernes a las 11" o "el 2 a las 18:00" sobre la lista numerada.
* Tu invitado recibe el email de Cal.com con fecha, hora y link de videollamada automáticamente.
* **Regla de oro:** mové y cancelá siempre desde el bot (o Cal.com), nunca desde Google Calendar — editar en Google huérfana el turno en Cal.com y el próximo cambio rebota (verificado 2026-10-15: cancel de ref huérfana rechazado).

## 5. Reuniones (Fathom, automático + a pedido)

* **Automático:** cada mañana 07:00 archiva las reuniones nuevas en tu Drive (`Reuniones-Internas` / `Reuniones-Clientes`).
* **A pedido:** "sincronizá mis reuniones" las trae en el momento y te dice cuántas guardó en cada carpeta.
* Si mandás "sincronizá" y no aparece nada nuevo, es que no había reuniones nuevas: lo ya traído no se duplica.

## 6. Tus contactos (la planilla manda)

El bot solo conoce los contactos de tu planilla `clientes` (`nombre,email,activo`) — nunca los de tu teléfono. Para agendar con alguien nuevo tenés dos caminos: agregá 1 fila a la planilla, o decile nombre y email al bot y él lo agrega solo (verifica antes que no exista). Todo invitado recibe siempre su invitación por email.

## 7. Tus datos quedan en tu ecosistema

Reuniones, contactos y decisiones quedan en tu Drive, tu vault y tu Leantime — no en la nube de una app de asistente de pago. Cada uso mejora el sistema.

## 8. Si algo no sale

* **No entendió un nombre:** repetilo más despacio o escribilo; si hay candidatos, elegí de la lista.
* **Dice que no encontró el email:** ese nombre no está en la planilla — agregalo o reenviá con el email.
* **El bot no responde:** avisá por el canal habitual; tu Cal.com y tu Fathom siguen intactos (el bot solo lee y organiza, nunca borra).
* **Dice que no pudo cancelar:** no toques nada en Google — el turno quedó huérfano ahí; gestioná el cambio en Cal.com y avisá para re-sincronizar. Por seguridad el bot nunca crea la reunión nueva si falló la cancelación.
* **Un audio muy largo (+2 min):** dividilo en partes.
