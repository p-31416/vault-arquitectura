---
tipo: manifiesto
fecha_creacion: 2026-11-10
ultima_actualizacion: 2026-11-10
tags: [studio-os, mvp_07, manifiesto-fundacional, hermes, filosofia, plan-30d]
idioma: es
---

# Manifiesto fundacional — Studio OS como ventaja del estudio

> Pieza compañera de [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]. Amplía la filosofía y fija el plan 30 días. Deja VISION y los documentos fundacionales intactos.

## 1. La ventaja que sostiene este proyecto

Los estudios de arquitectura incorporan IA como botón aislado en cada programa. Esa capa crea normalidad nueva: generar texto o imagen suelta deja de diferenciar.

La ventaja del estudio avanza en otro plano: **sistema con memoria, registro y reglas**, donde cada plano, modelo, render y acta conserva origen, versión, parámetros y aprobación. Ese sistema vive en [[proyectos/MVP_07-studio-os-sistema/VISION#1 · Qué es y por qué|VISION §1]] y se opera con [[proyectos/MVP_07-studio-os-sistema/VISION#4 · Hermes, conceptualmente|Hermes]].

Menos del 20% del sector aplica IA en flujo real. La ventana de oportunidad permanece abierta para quien llega con sistema auditable mientras la norma todavía se forma.

## 2. Filtro tren / hype / aporte

Criterio único, en línea con [[proyectos/MVP_07-studio-os-sistema/VISION#1.4 El norte (el único criterio de éxito)|VISION §1.4]]:

> Un resultado suma cuando deja rastro explicable y acelera el paso de junior a senior.

| Señal | Lectura | Respuesta del estudio |
|---|---|---|
| **Tren** | Transforma práctica durable: ControlNet con respeto geométrico, MCP que une CAD + vault + agente, Fathom hacia minuta con compromiso y fecha | Se incorpora con skill escrita y registro |
| **Hype** | Brillo sin rastro: workflow viral semanal, modelo sin licencia clara, demo sin semilla ni log | Queda en observación, fuera del sistema |
| **Aporte Studio OS** | Entra al ecosistema con parámetros versionados, portal y memoria curada | Se mantiene y evoluciona |

## 3. ComfyUI y n8n: del armado de nodos al diseño de sistema

La programación por nodos avanza hacia commodity. El valor migra:

`armar workflows → diseñar sistema que elige, valida, registra y mantiene`

* ComfyUI aporta motor de imagen y video con control geométrico. La receta por corrida queda en `02-WF-log` con semilla y parámetros, según [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]].
* n8n aporta orquestación determinista para agenda, recordatorios y sincronización. La operatoria conversacional vive en [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|MVP_06 agente voz]].
* Hermes aporta interpretación, memoria de trabajo, skills y cron. El detalle conceptual vive en [[proyectos/MVP_07-studio-os-sistema/VISION#4 · Hermes, conceptualmente|VISION §4]] y la guía de lectura en [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]].

El estudio evita quedar detrás de la ejecución de flujos. Diseña el sistema una vez, lo sostiene con mantenimiento liviano, y dedica energía a probar lo nuevo con criterio.

## 4. Principio de mantenimiento liviano

* Automatización primero para lo repetible y verificable. IA para interpretar, clasificar y proponer.
* Hermes ejecuta, el arquitecto aprueba. Niveles A-D definidos en [[proyectos/MVP_07-studio-os-sistema/VISION#6.6 Los niveles de riesgo (la regla de gobierno)|VISION §6.6]].
* Cuaderno digital como memoria de la casa, capa visual de la wiki. Ver [[proyectos/MVP_07-studio-os-sistema/VISION#3 · El cuaderno digital|VISION §3]].
* Contrato estable por MCP: si cambia el modelo, cambia el perfil, la tarea conserva forma.

## 5. Plan 30 días — Hermes demostrable con el concurso como banco de pruebas

Caso: [[proyectos/concurso-gaudi-nexus/index|The Gaudí Nexus]]. Entrega 16/12/2026. Sirve como excusa productiva para probar el ecosistema completo.

**Semana 0 — delineación (esta semana):**
Fijar 3 historias Hermes demostrables: agenda por voz en Telegram, Fathom hacia minuta con compromiso y fecha con aviso, experto-ComfyUI hacia portal con log completo para lámina A1.

**Semana 1 — cimientos visibles:**
Hermes TEST con agenda real, digest 07:00 y registro. Meta: 8/10 mensajes en menos de 20s, 0 bookings sin confirmación.

**Semana 2 — motores concurso:**
Cadena croquis / Rhino hacia ComfyUI hacia portal. Cada corrida con modelo, prompt, seed, sampler y veredicto keeper / descartar. Alimenta matriz Gaudí en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|Matriz de pruebas]].

**Semana 3 — sistema:**
Cuaderno enlazado con minuta y entrega trazable. Ensayo demo: Telegram hacia Cal.com hacia Drive y vault hacia portal hacia paquete entrega.

**Semana 4 — presentación:**
Lámina concurso más demo Hermes en vivo. Métrica: un junior opera el flujo completo con skill sin consulta al senior.

## 6. Relación con MVP_07

Este manifiesto acompaña a [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]], [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]], [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] y [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]] sin modificarlos. Toda decisión de construcción y todo criterio de aceptación conserva su fuente canónica en MVP_07. Este documento fija filosofía y ritmo, MVP_07 fija construcción y medida.

## Referencias

* [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]
* [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]]
* [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|MVP_06 spec agente voz]]
* [[proyectos/concurso-gaudi-nexus/index|Gaudí Nexus index]]
* [[specs/261102-plan-maestro-pi-por-temas|Plan maestro T1-T9]]
* [[specs/261102-system-overview-pi|System overview]]
