---
tipo: arquitectura
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [dos-caminos, emilia-30d, hermes, sistema-completo, operador-local, arquitecto-cloud, computos, minuta, render-redo]
idioma: es
---

# Dos caminos — entrega Emilia 35 días y sistema completo del estudio

> Separación pedida por Sol: (1) lo que se entrega a Emilia en ~1 mes + 5 días, (2) el diseño del sistema completo de cómo se trabaja en un estudio de arquitectura con asistentes sintéticos. La capa que se construye primero es la del arquitecto (la más importante); el diseño abarca todo el sistema.
> Compañeros: [[specs/261110-manifiesto-fundacional-studio-os|manifiesto]] · [[specs/261111-sistema-backend-vault-hermes|backend vault]] · [[specs/261111-convergencia-mvps-hermes|convergencia MVPs]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].

---

# CAMINO 1 — Entrega Emilia (35 días)

## 1 · Lo que el agente hace por Emilia (alcance del mes)

| # | Capacidad | Cómo | Nivel A-D |
|---|---|---|---|
| 1 | **Re-rendir con indicación** | manda render + texto o marca encima ("cambiá el cielo a atardecer") → el agente prepara img2img/inpaint → devuelve 2-3 variantes con semilla y parámetros | B auto (entrega), D si sale al cliente |
| 2 | **Informe de archivos AutoCAD** | sube DWG por Telegram → auditoría server-side (layers, escalas, xrefs, bloques, estándares MVP_02) → informe en PDF con observaciones clasificadas | B auto |
| 3 | **Cómputos** | del mismo DWG: bloques con atributos → tabla de cómputo (unidades, m², partidas) → planilla/PDF | B auto |
| 4 | **Impresión remota** | PDF listo para gestoría / imprenta; impresora propia requiere máquina encendida en destino (decisión abierta, ver §4) | C con aprobación |
| 5 | **Reuniones: el bot pide la reunión** | habla al bot por Telegram → agenda en Cal.com con invitación por mail (ya probado en MVP_06) | C con confirmación |
| 6 | **Transcripción + minuta con contexto** | sube audio de la reunión al bot (o Meet vía Fathom) → STT server-side → resumen bajo parámetros del estudio → distingue **reunión interna vs reunión con cliente** → arma minuta → **borrador de mail listo para enviar** | B el resumen, D el mail (persona aprueba) |
| 7 | **No necesita la computadora prendida** | STT y auditoría corren en servidor; su PC solo entra cuando ella quiere | — |

## 2 · La pregunta Hermes — respuesta

**Sí, vamos por Hermes ya.** Razones:

1. Está decidido en [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|VISION §6.9]]: Hermes es el agente de cara al cliente.
2. `config.yaml`, `SOUL.md`, skills, cron y MCP ya están especificados pieza por pieza en [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]] — el costo de instalarlo es conocido.
3. Lo que pedís — Emilia **conectada a flujos, sin manejar n8n** — es exactamente el patrón Hermes: Hermes interpreta, y llama a los flujos n8n por MCP (`n8n-official`). Emilia nunca abre n8n.
4. Cada capacidad nueva se escribe como **skill** (archivo con procedimiento): sobrevive al mes, se reutiliza en el sistema completo.

**Falla segura**: MVP_06 (Agent Voz n8n) queda intacto como camino de prueba de Sol. Hermes recibe **su propio bot Telegram nuevo** — cero conflicto de trigger, migración sin apagar nada.

## 3 · Arquitectura de la entrega

```text
Emilia (celular / PC cuando quiere)
  → Telegram → bot Hermes (token propio)
      Hermes en VPS (memoria + skills + aprobaciones)
        ├─ MCP n8n → flujos deterministas:
        │    · Agenda Cal.com (subflujo MVP_06, reutilizado)
        │    · STT Gemini free → swap whisper-turbo (ADR MVP_06 ya resuelto)
        │    · Mail (Hermes redacta, Emilia aprueba y manda)
        │    · Render vía API imagen (Pollinations flux free / Runpod pod on-demand para calidad)
        │    · Health + avisos
        ├─ MCP runner DWG → worker server-side (ezdxf en el VPS: audit + cómputos, sin AutoCAD)
        └─ MCP vault → memoria, fichas, log
```

Puntos clave:
* **STT server-side** — el audio viaja al bot; el motor corre en nube (texto de transcript es la excepción de nube ya aceptada). La PC de Emilia apagada no afecta nada.
* **DWG sin AutoCAD en el VPS**: auditoría de capas/escalas/bloques/xrefs y cómputos por atributos corren con `ezdxf` (Python, Linux, headless). AutoCAD completo queda para la capa operador (Camino 2).
* **Fathom sigue** para Meet vinculadas (cloud, ya integrado). Meetily queda en el Camino 2 como piloto propio; para Emilia, subir el audio al bot es universal (presencial, Zoom, Meet).

## 4 · Decisión abierta: impresión

Imprimir necesita una máquina en el destino. Opciones: (a) PDF a gestoría/imprenta por mail — cero infra, (b) PC del estudio con Wake-on-LAN y cola de impresión — mes 2+, (c) servicio de impresión con API — a investigar. Propuesta para el mes: (a) con formato de impresión preparado por el agente.

## 5 · Plan 35 días

| Semana | Entrega | Gate |
|---|---|---|
| S1 | Hermes instalado en VPS + bot propio + MCP n8n + skills esqueleto (agenda, compromisos, correo) | Emilia agenda 1 reunión real |
| S2 | Reuniones: audio → STT → minuta con tipo (interna/cliente) → mail borrador | 2 reuniones reales con minuta ≤24h |
| S3 | Render re-do + informe DWG + cómputo | 1 DWG real auditado y computado |
| S4 | Impresión (a), pulido, portal de iteraciones, demo ensayada | demo completa de punta a punta |
| +5 días | ensayo, imprevistos, presentación con concurso Gaudí | presentación a Emilia |

**Métricas de éxito**: 100% minutas ≤24h · render re-do <10 min por variante · informe DWG con 0 toques del original · Emilia opera todo desde el celular sin abrir n8n.

---

# CAMINO 2 — Sistema completo: cómo se trabaja en un estudio con asistentes sintéticos

## 1 · Las dos capas (la tesis)

| | **Capa operador** (dibujante, junior) | **Capa arquitecto** (titular, Emilia, Sol) |
|---|---|---|
| Relación con la máquina | trabaja toda la jornada en su PC | está arriba, decide, a veces lejos |
| Asistente | **agente local** junto a su AutoCAD/Rhino/Comfy (OpenCode + MCPs en su máquina) | **agente cloud** (Hermes VPS + n8n): celular, PC apagada, 24/7 |
| Qué hace el asistente | ejecuta con él: audita mientras dibuja, computa, rendereiza, compara versiones | ejecuta para él: agenda, minutas, informes, entregas, recordatorios |
| Comparte | el mismo vault, el mismo registro, las mismas **skills** | idem |

**El contrato es uno.** Las skills (auditar-documentacion-cad, computar-partidas, preparar-entrega, minuta-reunion) son los mismos archivos `.md` en ambas capas: el operador las corre local mientras dibuja; el arquitecto las pide por Telegram desde la playa. Lo que cambia es el **runtime**, no el procedimiento. Esa es la pieza que hace extrapolable el sistema a un estudio con N humanos: cada humano que entra, toma su asistente sintético, y el conocimiento de la casa vive en el vault compartido.

## 2 · El recorrido completo (10 pasos del estudio con el sistema)

| Paso | Capa | Qué hace el asistente | Qué hace el humano |
|---|---|---|---|
| 1 Entra cliente | arquitecto | mini CRM, alta | decide si atiende |
| 2 Reunión | arquitecto | agenda, transcribe, minuta con contexto tipo | aprueba minuta y mail |
| 3 Compromisos | arquitecto | extrae con fecha, avisa antes de vencer | valida fecha |
| 4 Croquis / idea | operador | digitaliza, indexa al cuaderno | dibuja |
| 5 Planos | operador | audita estándares mientras dibuja, computa | firma el plano (Ley 24.335) |
| 6 Modelo 3D | operador | inspecciona, exporta, corre GH | modela |
| 7 Render / IA | ambos | operador corre local; arquitecto pide variantes con indicación | elige keeper |
| 8 Obra | operador/arquitecto | indexa fotos, incidencias | resuelve |
| 9 Entrega | arquitecto | arma paquete con registro | escribe el mail y manda |
| 10 Memoria | sistema | cada sesión deja entidades, topics, hechos; lint mantiene la wiki | cura qué queda |

## 3 · Reglas del sistema completo (heredadas y fijadas)

1. **Máquina ejecuta, humano decide y firma** — niveles A-D en [[proyectos/MVP_07-studio-os-sistema/VISION#6.6 Los niveles de riesgo (la regla de gobierno)|VISION §6.6]].
2. **Formato humano vs formato de máquina** — UI solo para lo que el humano lee ([[specs/261111-sistema-backend-vault-hermes|backend vault §VISION 1]]).
3. **Libre primero, nube como excepción** ([[proyectos/MVP_07-studio-os-sistema/VISION#5 · El stack delineado|VISION §5]]).
4. **Trazabilidad total** — de qué archivo salió, con qué versión, quién aprobó.
5. **El estándar hace posible el cómputo** — MVP_02 (bloques con atributos, capas) es la condición para que el cómputo sea automático: la disciplina de dibujo alimenta al sistema.

## 4 · Qué NO decide este documento

* Worker DWG definitivo (ezdxf vs AutoCAD Core Console en N2) — se resuelve con el primer DWG real de la S3.
* Modelo STT final (Gemini free vs whisper-turbo) — ADR MVP_06 ya tiene el swap en 1 nodo; se mide con las reuniones reales.
* Wake-on-LAN e impresión propia — mes 2.
* Implementación de scripts y comandos — se entregan en archivos didácticos `scripts/<slug>.py` + `_explicado.py` con tu ejecución y `s` explícito ([[AGENTS.md|regla HITL]]).

---

## Preguntas para cerrar (respondeme con número + respuesta)

1. ¿Bot Telegram de Hermes nuevo y separado de `emiliaospi_bot`, con MVP_06 como falla segura? (recomendado: sí)
2. ¿Emilia prueba con **meetings Meet + Fathom** (zero install) o sube **audio al bot** (universal, requiere que grabe)? — propuesta: ambas, Fathom mientras Meet sea la norma.
3. ¿Impresión (a) PDF a gestoría para el mes? — o preferís investigar (c) servicio con API.
4. ¿El primer DWG real de la S3 es uno de Emilia (con permiso) o uno del vault (BHindú/cocina)?

Con tus 4 respuestas, armo el SPEC ejecutable de la S1 (Hermes install VPS, checklist de piezas con comandos para tu terminal) y arrancamos el día siguiente.
