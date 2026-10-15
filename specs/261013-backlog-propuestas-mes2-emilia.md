---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
estado: borrador
tags: [backlog, mes2, propuestas, roi, studio-os]
idioma: es
---

# Backlog + propuestas Mes 2 EXPERIMENTAR — Studio OS Emilia

> Mes 2 (600 USD, cubierto por Factura C 600 del vie 16): ¿Qué podemos transformar? Prototipos, agentes y automatizaciones con ahorro medido. Base: [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]] + [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura v1.3 §6]] + [[specs/260917-backlog-nextcloud-vps-storage|backlog Nextcloud]].

## 1. Hardening Mes 1 (≤2hs, entra con el cierre)

* [ ] Filtro `chat_id` Router (cuando Emilia mande `/start`).
* [ ] Evento Cal.com 60 min con Google Meet + swap `eventTypeId` (no sale por API, con Emilia).
* [ ] Hoja `clientes-contactos` con reales (hoy 1 fila test).
* [ ] Dedup Data Table `Bot State` en Fathom Core (hoy mitigado con `created_after -26h`).
* [ ] Rotar token expuesto en `create-user-emilia.ps1:4`.
* [ ] Revisar link GPT de Emilia + duraciones 11/09.

## 2. Propuestas Mes 2 (3 módulos, precio anclado a ahorro)

### A. Agente IA en lenguaje natural (12 pomodoros ≈ 5hs)

Telegram deja comandos estrictos → agente con OpenRouter + memoria/Redis + botones→mail. Reusa Agenda/Cal/Sheets ya verificados.
**Ahorro:** agenda 30min×8 reuniones + fricción formato = ~5hs/mes. **ROI:** se paga en el primer mes.

### B. CAD: un tipo de plano bien usado (16 pomodoros ≈ 6.7hs)

SET_01 replanteo aplicado + conteo bloques→planilla + clase + DWT/DWS instalados en su PC.
**Ahorro medido en log MVP_02:** ~12-15hs por plano, payback en el primer plano. **ROI:** inmediato.

### C. Comfy en su PC (10 pomodoros ≈ 4.2hs)

Flujo upscale o croquis + modelos descargados + instructivo. Decisión: probar croquis en PC Sol, llevar demo, instalar en la de ella.
**Ahorro:** iteraciones de representación sin operador (a medir S1 Mes 2).

**Total propuesto:** ~16hs de 60hs Mes 2. Resto: sprints, soporte 3h/día, medición y roadmap Mes 3.

## 3. Backlog Mes 3 / 2027 (no entra a Mes 2)

| Ítem | Fuente | Target |
|---|---|---|
| Nextcloud self-hosted (soberanía datos) | [[specs/260917-backlog-nextcloud-vps-storage|spec]] | Mes 3 / 2027 |
| Monitoreo VPS (Uptime Kuma + alerta Telegram) | Plan n8n §12 | Mes 3 |
| Plugin MCP Leantime (0 tools) para Fathom→specs→Leantime | Sesión 09/10 | Mes 3 |
| RunPod: auditar retención antes de batch no sensible | Plan trimestral §10 | Mes 3 |
| YouTube Nivel 2 (RSS + briefing semanal n8n) | Reporte 08-09 | Mes 3 |
| Remotion episodios + VR Quest | 05/10, 09/10 | Backlog |
| MVP_03 honorarios + MVP_05 Rhino | Base previa | A demanda |

## 4. Criterio de aceptación Mes 2

Cada módulo cierra con ahorro medido (manual vs sistema) cargado en Leantime + demo con Emilia + ficha wiki. Sin medición no hay M3.
