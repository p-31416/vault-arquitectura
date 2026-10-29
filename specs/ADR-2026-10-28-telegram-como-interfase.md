---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, telegram, interfaz, n8n, fathom, calcom]
idioma: es
---

# ADR-2026-10-28-telegram-como-interfase: Telegram es la interfase del estudio, con n8n como motor y Hermes como cerebro

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

El plan del 27/08 (`04-plan-studio-os.md` §4.4) propuso Discord como interfase y dejó la decisión abierta; el relevamiento respondió "Discord, a evaluar". Hoy hay un bot de Telegram en n8n funcionando (`@emiliaospi_bot`): agenda en Cal.com, mueve y cancela reuniones, dispara el digest de las 07:00 y sincroniza Fathom a Drive. Fathom graba las reuniones y es el único origen de *intención*. Telegram tiene grupos con **temas** y canales, y los bots leen `message_thread_id`. El riesgo actual: si Hermes también habla Telegram, quedan dos bots hablando con el estudio.

## Decisión

**Telegram es la interfase del estudio**, en tres superficies: **1 grupo por obra con temas** por frente (AutoCAD, Rhino-3D, Render-IA, Obra, Comercial), **1 canal de bitácora** con lo que el sistema hizo, y **chat privado** para pedidos rápidos y **aprobaciones con botones inline**. La migración es por etapas: **fase 1** el bot sigue en n8n (agenda, digest, Fathom) mientras se construye el resto; **fase 2**, con el MVP aprobado, **el token migra a Hermes** y n8n queda como motor invocado por Hermes vía MCP. **Discord** queda para la mesa de iteración visual y el canal de método (el material sensible no sale del Drive/vault); **WhatsApp** sigue para clientes; **Fathom** es el tronco: reunión → minuta → decisiones → Leantime → vault.

## Alternativas

### Discord como interfase principal
- Pros: canales por obra, threads, permisos finos, embeds para renders.
- Contras: hay que enseñar una herramienta nueva ("no somos técnicos" es la objeción principal); el bot ya existe en Telegram; y el material de cliente en Discord implica salida a servidores de EE.UU.

### WhatsApp como interfase
- Pros: hábito cero del estudio, adoption inmediato.
- Contras: la API de negocio complica los botones y los hilos; sin orden por obra; el estudio ya tiene Telegram.

### Solo dashboard web
- Pros: control total y mejor visualization.
- Contras: no es la interfase del día del estudio; el público objetivo no es técnico.

## Consecuencias

### Positivas
- Una sola voz hacia el estudio, con un camino único de migración y rollback explícito.
- Las aprobaciones quedan **en el mismo canal donde se discute**: el HITL se cierra en el lugar natural.
- Se reutiliza el trabajo ya hecho: agenda Cal.com, digest y Fathom no se reimplementan.

### Negativas
- La migración del webhook de Telegram hay que probarla con criterio de rollback (y hay que tener el bot de n8n listo para volver).
- El bot tiene que entender **temas** (`message_thread_id`): es un cambio real en el flujo, no un detalle de configuración.
- Telegram es la interfase, no la memoria: si el canal se pierde, la trazabilidad sigue en el registro.

### Riesgos + mitigación
- **Dos bots activos a la vez**: durante la migración solo uno tiene el token; el otro queda en modo lectura y se apaga con evidencia.
- **Ruido en el canal**: las notificaciones inmediatas son solo accionables (terminó, falló, espera aprobación); el resto va al digest diario.
- **PII y material sensible en el chat**: los archivos se referencian por `file_ref` del vault, no se mandan como adjuntos al canal.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.6 y §2.10 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §6
- wiki: [[wiki/glosario/software/telegram|telegram]] · [[wiki/glosario/software/n8n|n8n]] (flujos Fathom→minuta→Leantime y bot) · [[wiki/glosario/software/leantime|leantime]]
- proyecto: [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os|04-plan-studio-os]] §4.4 y §8
- sesión: [[raw/sessions/2026-10-28-sesion-delinear-pitauos|sesión 2026-10-28]]
