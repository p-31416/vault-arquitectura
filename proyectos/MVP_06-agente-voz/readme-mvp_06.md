---
tipo: readme
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [readme, mvp_06, agente-voz, telegram, n8n, guia]
---

# MVP_06 — Agente de voz Telegram + n8n (lenguaje natural)

Si abrís este proyecto por primera vez, empezá acá.

## Qué es esto

Un **agente Telegram que entiende lenguaje natural hablado y escrito** y crea reuniones reales en Cal.com, cancela, modifica, lista próximas y sincroniza Fathom a pedido más cron automático. Reutiliza la lógica de reserva ya resuelta en los Cores existentes (Agenda, Cancel, Modif, Fathom) y la expone mediante un agente IA — **sin comandos con slash** en el camino principal.

## Estado

Proyecto interno del estudio, fase concepto. Pruebas con la cuenta Proyecto Pi (`proyectopi.31416@gmail.com`). Producción Emilia queda intacta hasta validación 8/10.

## Cómo está organizado

```text
MVP_06-agente-voz/
├── readme-mvp_06.md    ← Este archivo. Puerta de entrada.
├── 01-spec-mvp_06.md   ← Documento canónico único: SPEC + flujo + nodos + ADRs + plan.
├── 02-ft-mvp_06.md     ← Plan técnico de construcción (apunta al spec, se expande al construir).
└── 03-log-mvp_06.md    ← Bitácora (se abre con la primera construcción).
```

## Dónde leer

* Plan completo: [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|01-spec-mvp_06]]
* Manual de uso: [[proyectos/MVP_06-agente-voz/documentacion/manual-uso-agente-voz|manual-uso-agente-voz]]
* Credenciales y mantenimiento: [[proyectos/MVP_06-agente-voz/documentacion/credenciales-conexiones|credenciales-conexiones]]
* Antecedente superado: [[specs/261013-agente-voz-telegram-os|spec 261013]] ( lives en `specs/`, apunta acá)
* Referencia técnica OS-Emilia (Cores reutilizados): [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia]]
* Modelo de entrada audio/texto + Redis: workflow n8n `LidIA_V5.0-PROD-Ycloud_Wsp` (`pw5OHhXNjeXSnD3u`)
* Modelo de agenda IA: workflow n8n `LidIA_V5.0-SWF_Agenda` (`w8iMJ01WGCSxvSMg`)
