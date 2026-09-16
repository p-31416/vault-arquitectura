---
tipo: metodologia
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fase: briefing
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-11
estado: vigente
tags: [plan, trimestral, 190hs, 60hs-mes, ptech, studio-os, vigente, lectura-specs]
---

# Plan trimestral unificado — Studio OS Emilia · +190hs (3×~64hs) · Sep-Dic 2026

> **Lectura única en `/specs` (Obsidian):** [[specs/260910-plan-trimestral-unificado-studio-os-emilia|este plan]] concentra filosofía, programa 90 días, detalle Mes 1-3, calendario, métricas y mantenimiento. Fuente filosofía: [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] (extraída de `raw/brainstorm/Pitautech_Propuesta_I+D_Arquitectura_Vault.md`). Detalle operativo Mes 1: [[specs/260909-esquema-mes1-60hs-studio-os-emilia|esquema Mes 1]]. Propuesta cliente: [[proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes|05-propuesta-comercial-viernes]].

## Índice

- [[#1. Filosofía — ROL IA como JR iterable y meta arquitecto]]
- [[#2. Programa 90 días — Observar / Experimentar / Sistematizar]]
- [[#3. Mes a mes — qué avanza y qué queda]]
- [[#4. Mes 1 detallado — Nayara Brasil + Vault + representación]]
- [[#5. Calendario — 3h/día · Presencial cada 15 días · Sprints y milestones]]
- [[#6. OKRs y métricas — horas dedicadas vs horas que libera cada sistema]]
- [[#7. Inversión — 4 pagos (300/600/600/300 = 1.800)]]
- [[#8. Mantenimiento y continuidad — reunión 15 días antes del cierre]]
- [[#9. Demo genérica — moodboard ComfyUI para mañana]]
- [[#10. Stack, privacidad y RunPod]]
- [[#11. Entregables por mes — tangibles evaluables]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

---

## 1. Filosofía — ROL IA como JR iterable y meta arquitecto

**Pitautech propone capacidad prevista 3h/día (60hs/mes) — el valor está en lo que produce.** Programa I+D donde la capacidad expresa disponibilidad y planificación; el valor avanza con investigación, prototipos, procesos, documentación reutilizable y conocimiento que queda en el estudio. [[wiki/glosario/interno/standares/ptech-filosofia#Idea central — capacidad, no horas|ptech-filosofia — capacidad prevista, valor en lo producido]]

**ROL IA en el estudio:**

> La IA avanza como **JR con capacidades limitadas, reglas exactas, iterable y mejorable**, que elimina fricción con criterio medible. Libera tiempo para que el arquitecto proyecte.

- **Meta arquitecto:** quien diseña el sistema que diseña arquitectura (meta-design Fischer & Giaccardi 2004 + Design Technology BIG/Foster). Neologismo Pitautech legítimo. Ver [[wiki/glosario/interno/standares/ptech-filosofia#Tres modos del conocimiento|Tres modos]].
- **Meta arquitectura:** arquitectura de segundo orden — CDE/Vault + agentes HITL que producen arquitectura. Ver `raw/research/2026-09-09-meta-arquitecto-pitautech.md`.
- **Primera función:** recordar. Reunión → transcripción → temas/decisiones/pendientes → Vault → agenda. [[wiki/glosario/interno/standares/ptech-filosofia#La primera función de la IA — recordar|ptech-filosofia]]
- **Ciclo I+D como método científico:** observación → pregunta → hipótesis → investigación → experimento → resultado → evaluación → protocolo → implementación → aprendizaje. Registro por pomodoros; resultados como unidad de valor.

**Ganancia para quien la aplique desde ahora:** tareas automatizables donde hoy se desperdicia recurso (nombrar, ordenar, configurar, transcribir, buscar, clasificar, documentar) avanzan hacia sistema y liberan capacidad cognitiva para investigar, imaginar, proyectar y decidir. [[wiki/glosario/interno/standares/ptech-filosofia#I+D como método científico aplicado|I+D método]]

---

## 2. Programa 90 días — Observar / Experimentar / Sistematizar

| Mes | Foco | Pregunta | Qué avanza |
|---|---|---|---|
| **1 OBSERVAR** | Relevamiento, mapa operativo, fricciones, auditoría, Vault inicial | ¿Cómo trabaja realmente el estudio? | Vault encendido + sistema representación + estándares CAD sobre objeto de estudio |
| **2 EXPERIMENTAR** | Prototipos, agentes, automatizaciones, Vault, taxonomías | ¿Qué podemos transformar? | Primeras automatizaciones con ahorro medido, moodboard y flujos ComfyUI |
| **3 SISTEMATIZAR** | Evaluación, protocolos, capacitación, roadmap | ¿Qué aprendimos y qué avanza hacia sistema? | Procesos reproducibles + equipo operando con autonomía + roadmap 2027 + mejoras implementadas si corresponde |

**Principio:** todos los meses dejan **algo tangible, mejorable, evaluado, documentado y abierto a debate** (filosofía Google/Pixar — Design Sprint + Braintrust). Mes 1 con mayor peso en observación y victorias rápidas.

**Mantenimiento incluido:** Sep / Oct / Nov + mediados de Dic, con menos presencialidad (ver §8).

---

## 3. Mes a mes — qué avanza y qué queda

### Mes 1 OBSERVAR — 60hs

- Vault con agentes para alimentar base de conocimiento (brain-karpathy)
- Agente agenda reuniones (probado vault-lidia) — creación + link Google Meet
- Agente Fathom transcripciones → análisis tareas → procesamiento al Vault
- Nomenclaturas, orden carpetas + instalación en PC Emilia
- Análisis representación Emilia (S2) — búsqueda referentes, revistas físicas/escaner, web, almacenamiento, moodboard
- Objeto de estudio: **entrega Nayara Alvares Campos — Brasil (ya realizada)**

### Mes 2 EXPERIMENTAR — 60hs

- Prototipos y agentes con experimentación presente siempre (método científico I+D)
- Investigación tecnológica, automatizaciones, integración reuniones, procesamiento transcripciones
- Taxonomías, referencias, conexiones entre sistemas, primeras pruebas
- Flujos elaboración gráfica y videos para arquitectura con ComfyUI (ver RunPod §10)
- Sprints semanales con entregable tangible

### Mes 3 SISTEMATIZAR — 60hs

- Todo verificado, implementación de mejoras si corresponde
- Documentación, manuales, protocolos, capacitación, consolidación del conocimiento
- Roadmap y prioridades para 2027
- Evaluación final + reunión continuidad 15 días antes del cierre (ver §8)

---

## 4. Mes 1 detallado — Nayara Brasil + Vault + representación

**Objeto de estudio Mes 1:** entrega **Nayara Alvares Campos — Brasil** (implementación Vault con agentes sobre base ya entregada).

| Semana | Horas | Temas | Entregable verificable |
|---|---|---|---|
| **S1 Vault vivo** | 15h | Filosofía, inventario PCs, Meet→Vault (Fathom), agentes (agenda + transcripción → Vault), nomenclaturas, instalación PC Emilia, sync | Vault operativo + 1 reunión transcripta muestra + guía wiki + agentes funcionando |
| **S2 Representación** | 15h | Búsqueda referentes láminas (ArchDaily, revistas físicas con escáner, web), almacenamiento, moodboard, análisis elaboración gráfica | Carpeta 20-30 referentes con ficha (qué tomar/dejar) + demo moodboard genérica + códigos visuales |
| **S3 Estándares CAD** | 15h | Estructura archivos + DWT, layers, puntas, bloques, láminas, rótulos + apoyo IA Lisp + validación sobre Nayara | Estándares operativos sobre objeto de estudio + fichas `wiki/estandares/` |
| **S4 Cierre** | 15h | Consolidación, clase 2h, roadmap Mes 2, retro, acta | Doc Mes 1 completa + clase + accesos Leantime + roadmap + log métricas |

**Sprints y milestones:**

- **Sprint semanal:** 15hs (3h/día ×5) — entregable tangible cada viernes
- **Daily async:** avance documentado en Vault (sin reunión), Lun check 0.5h + Mié sesión 1.5h (presencial S1+S3, virtual S2+S4)
- **Milestones:** M1 día 5 Vault+Fathom · M2 día 10 sistema visual · M3 día 15 estándares sobre Nayara · M4 día 20 todo enseñable + roadmap

---

## 5. Calendario — 3h/día · Presencial cada 15 días · Sprints y milestones

**Ritmo:** 3h/día × 20 días = 60hs/mes · 6 pomodoros/día (25+5) · Franjas 8:30-18:00
**Presenciales (2/mes):** Mié S1 (conceptual + relevamiento, 1.5-2h) + Mié S3 (validación CAD + referentes, 1.5h) — incluidos en las 60hs
**Virtuales (6/mes):** Lun 0.5h ×4 + Mié S2 y S4 1.5h ×2 + Vie async
**Disponibilidad estudio:** 2hs/sem (Mié 1.5h + Lun 0.5h)

```
Sep (M1): S1 Presencial | S2 Virtual | S3 Presencial | S4 Virtual+clase
Oct (M2): S1 Presencial | S2 Virtual | S3 Presencial | S4 Virtual
Nov (M3): S1 Presencial | S2 Virtual | S3 Presencial | S4 Virtual
Dic:      mediados dic — cierre y reunión continuidad (15 días antes, ver §8) con menos presencialidad
```

---

## 6. OKRs y métricas — horas dedicadas vs horas que libera cada sistema

**Cálculo trimestral:** capacidad +190hs → objetivo **≥36hs/mes liberadas** al cierre (acumulativo, base medida 12hs/mes Mes 1).

### OKRs Mes 1

- **O1 Adopción:** 100% reuniones (8) en `raw/reuniones/` <24hs, Emilia alimenta 1 ficha/sem con autonomía, 1 junior opera solo en S4
- **O2 Números reales:** 60hs trackeadas por bloque con desvío <10%, 3 procesos medidos manual vs con sistema (buscar plano 15→2min, presupuesto 2h→0.5h, informe obra), roadmap M2 con precio anclado a horas liberadas
- **O3 Herramientas:** 8 fichas wiki + estándares sobre Nayara, 1 flujo Fathom→Vault + 20-30 referentes, ahorro proyectado ≥12hs/mes

### Métricas — [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]]

| Métrica | Fórmula | Fuente | Dónde se loguea |
|---|---|---|---|
| **Ahorro por flujo** | `T_manual − T_sistema` | Toggl + n8n estimated time | `log.md` + ficha lecciones |
| **Ahorro mensual** | `Ahorro × Frecuencia/mes` | Frecuencia observada | `ptech-metricas-friccion` |
| **ROI** | `Ahorro_mes / T_invertido` | Horas invertidas en crear sistema | Spec interno |
| **Capacidad liberada** | `Ahorro_mes / 60hs` | Objetivo ≥0.17 Mes 1 | OKR |
| **Tiempo humano vs máquina** | `T_humano (revisión) vs T_máquina (ejecución)` | Sherlock minutos execution + Fathom duración (captura, minuta, tareas, Leantime carga) | Log agente |
| **Tiempo ahorrado** | `T_humano_manual − (T_humano_revisión + T_máquina)` | Resta | Métrica principal |

**Log de retorno (interno, detallado):** cada ejecución de agente registra minutos (Sherlock búsquedas, Fathom captura → minuta → análisis → listado tareas → carga Leantime VPS). Si no es perfecto, se usa tiempo estimado n8n por flujo, como en n8n. Ver [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]].

### Retorno para siempre — ejemplo trimestral (60hs → 36hs/mes liberadas, [[wiki/glosario/conceptos/payback|payback]] mes 7)

Inversión: **+190hs (1.800 USD)** (180 programa + 10 mantenimiento bonificado). Parte de lo que se paga **es retorno para siempre**.

| Mes | Inversión acumulada | Ahorro nuevo | Ahorro mensual acumulado | ROI acumulado | Liberado acumulado |
|---|---|---|---|---|---|
| 1 | 60hs | +12hs/mes | 12hs/mes | 0.20 (12/60) | 12hs |
| 2 | 120hs | +12hs/mes | 24hs/mes | 0.30 (36/120) | 36hs |
| 3 | +190hs (180+10 bonif) | +12hs/mes | 36hs/mes | 0.38 (72/190) | 72hs |
| 4 | +190hs | 0 | 36hs/mes | 0.57 (108/190) | 108hs |
| 6 | +190hs | 0 | 36hs/mes | 0.95 (180/190) | 180hs |
| 7 ([[wiki/glosario/conceptos/payback|payback]]) | +190hs | 0 | 36hs/mes | 1.14 (216/190) | 216hs |
| 12 | +190hs | 0 | 36hs/mes | 2.08 (396/190) | 396hs |

**Lectura cliente:** en **7 meses** recuperas las +190hs invertidas. Desde mes 8, cada mes de 36hs liberadas es ganancia neta para siempre (396hs/año ≈ 2.1× la inversión). A 10 USD/h = **3.960 USD/año liberados** con inversión de 1.800 USD. Ver detalle en [[wiki/glosario/interno/standares/ptech-metricas-friccion#Ejemplo trimestral — el estudio recupera la inversión y luego libera para siempre|ptech-metricas-friccion]].

> **Auditoría 2026-09-11:** escenario +10hs/mes daba 30hs/mes, payback mes 8 y 330hs/año (1.74x). Con medido +12hs/mes, ritmo Mes 3 avanza a 36hs/mes, acumulado Mes 3 a 72hs, payback a mes 7 y año a 396hs (2.08x).

---

## 7. Inversión — 4 pagos (300/600/600/300 = 1.800)

| Hito | Importe | Cuándo | Nota |
|---|---|---|---|
| Adelanto Mes 1 | **USD 300** | Al firmar (50% Mes 1) | Reserva capacidad 60hs Mes 1 |
| Fin Mes 1 | **USD 600** | Cierre S4 + clase | Saldo Mes 1 + Mes 2 por adelantado |
| Fin Mes 2 | **USD 600** | Cierre Mes 2 |  |
| Saldo entregable | **USD 300** | Entrega final Mes 3 | Cierre + documentación + roadmap |
| **Total trimestral +190hs** | **USD 1.800** | 3 meses Observar/Experimentar/Sistematizar | Pesos al oficial del día |

Incluye cada mes: investigación, diseño, prototipado, implementación, documentación y acompañamiento 3h/día.
Queda para siguiente ciclo con ahorro medido como base: licencias y academia (1 asiento bonus Mes 1).

Referencia mercado: auditoría sprint 2-4 semanas 2.500-3.500 mediana sin prototipo ni enseñanza — este programa avanza con prototipo + capacitación incluida y Vault que queda en el estudio.

---

## 8. Mantenimiento y continuidad — reunión 15 días antes del cierre

Mantenimiento **incluido durante los 3 meses** (Sep/Oct/Nov + mediados Dic con menos presencialidad). **15 días antes del cierre** (fines de Nov) reunión para definir continuidad: qué sigue, qué queda en mantenimiento, qué escala.

---

## 9. Demo genérica — moodboard ComfyUI para mañana

Demo genérica para entender el flujo (no sobre Nayara aún):

- **Flujo:** `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json` (ya verificado, adaptado a recursos)
- **Input:** imágenes genéricas ArchDaily + revistas escaneadas (no Nayara)
- **Futuro:** análisis elaboración gráfica y videos para arquitectura con ComfyUI → RunPod ([[wiki/glosario/entidades/runpod|RunPod]] como entidad, ver §10) para escalar
- **Entrega mañana:** demo en vivo 2-3 min, sin exponer datos sensibles

---

## 10. Stack, privacidad y RunPod

**Stack Mes 1:** Obsidian Vault + OpenCode Zen + Antigravity · Fathom Meet → `raw/reuniones/` → `wiki/fuentes/` · Drive piloto + mail dedicado · DWT/layers/bloques + Lisp con IA · Leantime VPS Kanban

**Privacidad desde el inicio:** análisis de imágenes con **modelos locales**. Si se usa modelo comercial, queda anotado con metadatos (imagen + nomenclatura + versionado automático + doc WF-log). Política de privacidad mini a entregar el viernes junto con contrato de servicio básico (pendiente que me pases el documento para adaptar).

**RunPod:** documentado como entidad [[wiki/glosario/entidades/runpod|RunPod]] (ver §10 y `ptech-filosofia`), para flujos ComfyUI a futuro con escalado.

---

## 11. Entregables por mes — tangibles evaluables

Todos los meses dejan algo **tangible, mejorable, evaluado, documentado y abierto a debate** (Google/Pixar — Design Sprint + Braintrust).

| Mes | Entregable tangible | Evaluación |
|---|---|---|
| 1 | Vault operativo + referentes + estándares sobre Nayara + clase | Medición manual vs automatizado, retro S4 |
| 2 | Prototipos + moodboard + automatizaciones + taxonomías | Test con ahorro medido, debate |
| 3 | Procesos verificados + mejoras implementadas si corresponde + documentación + roadmap | Verificación final + reunión continuidad |

---

## Conceptos relacionados

- [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] — Filosofía Pitautech (capacidad prevista 3h/día — valor en lo producido, Vault memoria computable, I+D método, visión estudio que aprende)
- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — meta arquitecto + meta arquitectura + arquitectura de sistemas (Fischer 2004 → BIG/Foster/ZHA)
- [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] — HITL, JR iterable con guardrails por confianza
- [[wiki/glosario/conceptos/diseno-colaborativo|diseno-colaborativo]] — co-diseño, underdesign, SER, Braintrust + seguridad psicológica
- [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]] — Métricas fricción (ahorro, ROI, humano vs máquina, log retorno)
- [[wiki/glosario/conceptos/okr-goals|okr-goals]] — OKRs trimestrales
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — Vault con fotos/imágenes + curaduría
- [[wiki/glosario/entidades/runpod|RunPod]] — Entidad escalado ComfyUI

## Referencias

- `raw/brainstorm/Pitautech_Propuesta_I+D_Arquitectura_Vault.md` (18 capítulos, fuente I+D)
- `raw/research/2026-09-09-meta-arquitecto-pitautech.md` (18 fuentes 200, meta arquitecto + Design Technology BIG/Foster)
- [[specs/260909-esquema-mes1-60hs-studio-os-emilia]] + [[proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes]]
- [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os]] — arquitectura Drive+Vault+Túnel
- Contrato servicio básico + mini-política privacidad — **pendiente que me pases documento para adaptar antes del viernes**
