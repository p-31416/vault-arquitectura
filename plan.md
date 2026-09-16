---
tipo: plan
proyecto: vault-cerebro
cliente: estudios early bird (2 estudios iniciales)
fase: concepto → MVP 1 mes
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [vault, cerebro, opencode, fathom, autocad, comfyui, early-bird, academia]
idioma: es
---

# Plan: Vault Cerebro — Creatividad con Orden para Estudios de Arquitectura

## Resumen ejecutivo

Vault Cerebro mapea procesos del estudio para identificar dónde el uso de IA genera beneficio concreto. Pensado para quien recién comienza a organizarse —sin importar trayectoria— y busca transformar tareas dispersas en flujo con calidad verificada, trazabilidad y mejora semanal.

Cada interacción alimenta el vault, cada reunión se vuelve buscable, cada decisión queda registrada. La IA no reemplaza el criterio profesional: potencia desarrollos puntuales —por ejemplo, estándares de AutoCAD no usan IA en sí, pero usaremos IA para escribir scripts, comandos y rutinas en Lisp/AutoLISP que aceleran y ordenan el trabajo.

Principio guía: la mejora continua como hábito. Cada repetición es oportunidad de refinamiento. El vault es el soporte de esa mejora, con método heredable.

---

## Qué es Cerebro Digital (Karpathy) y cómo se aplica al vault

**Concepto:** técnica de *personal knowledge brain* de Andrej Karpathy — capturar todo en `raw/` (sesiones verbatim), extraer entidades y topics, y promover a conocimiento permanente en `wiki/` con `[[wikilinks]]`.

**Aplicación en Vault Cerebro:**

- `raw/sessions/` y `raw/reuniones/` reciben lo crudo (transcripción Fathom de Meet, fotos de obra, notas)
- El agente del vault (OpenCode) extrae entidades (personas, proyectos, decisiones) y topics candidatos
- Se promueve a `wiki/glosario/software/`, `wiki/glosario/conceptos/`, `wiki/estandares/` y `wiki/lecciones-aprendidas/`
- Cada activo en `proyectos/260907-brain_emilia/` queda linkeado a su ficha wiki, con historial trazable

> Ver [[wiki/glosario/conceptos/cerebro-digital-karpathy|Cerebro digital Karpathy]] para definición completa.

**Técnicas de mejora continua que nutren el vault:**

- **Lean** — eliminar desperdicio (retrabajo de planos, búsqueda de archivos, reuniones sin minuta)
- **PM / Project Management** — mapeo de procesos, tableros, métricas y rituales (ver futuro MCP Leantime como tablero de tareas, ya instalado en VPS local)
- **Otras a investigar:** Kanban, Last Planner, Agile para arquitectura, Kaizen semanal, retrospectivas breves, 5S para archivos

---

## Principios de diseño

- **Lenguaje en positivo:** cada propuesta afirma valor creado y posibilidad abierta
- **Proceso verificable:** normas, registros, evaluaciones y mejora continua semana a semana
- **Pequeñas victorias:** MVPs que demuestran valor tangible en cada entrega
- **Todo interconectado:** vault, wiki, reuniones, AutoCAD, ComfyUI y academia comparten fuente única
- **IA al servicio del desarrollo:** aunque el estándar no use IA, la usamos para generar código (Lisp), automatizar y documentar

---

## Arquitectura Vault Cerebro

```
OpenCode (terminal) + Antigravity IDE  →  OpenCode Zen (tier gratuito)
  Sol: zen + go                         →  Emilia: zen + openai (si necesario)
        ↓
Vault Cerebro (proyectos/ + wiki/ + raw/ + wiki/fuentes/)
        ↓
Fathom MCP  →  raw/  →  wiki/fuentes/ (necesidades cliente, soporte portugués)
  └─→ Agente del vault evalúa cómo automatizar Meet → Fathom → vault → procesado
        ↓
Cowork schedule / GitHub Actions  →  sincronización automática con copia local
        ↓
AutoCAD (rótulos, layers, DWT, bloques dinámicos, Lisp)  ↔  wiki por activo
        ↓
ComfyUI (ControlNet Canny)  →  posproducción de archivo AutoCAD  →  futuro LoRA  →  RunPod si escala
        ↓
Leantime MCP (VPS local, futuro)  →  tablero de tareas (usuario Emilia + URL + pass)
        ↓
Academia (caso de éxito reutilizable)
```

**Entorno de trabajo:**

- Sol: OpenCode Zen + Go
- Emilia: OpenCode Zen + OpenAI (si necesario)
- VPS: Leantime ya instalado local, pendiente crear usuario para Emilia y compartir URL/pass

---

## Semana 1 — Vault Cerebro Vivo (14 hs netas)

**Objetivo verificable:** vault operativo, conectado, con reunión de prueba capturada y sincronización validada. Todo iterable y adaptable al usuario.

- **Reunión 1 — Miércoles (conceptual, 1.5 hs):** cómo funciona el vault, preguntas, cambios que quieran realizar. Todo es iterable, se adapta al usuario desde el inicio. Incluye relevamiento de recursos de PCs del estudio y recursos locales.
- **Instalación y puesta en marcha sobre repositorio:**
  - Sol: OpenCode Zen + Go
  - Emilia: OpenCode Zen + OpenAI (si necesario)
  - Configuración de OpenCode en `vault-arquitectura` con lectura de `AGENTS.md`
- **Fathom — flujo completo desde creación de reunión:**
  - Creación de reunión en Meet
  - Conexión Fathom (MCP)
  - Extracción automática al vault (`raw/reuniones/`)
  - Procesado hacia `wiki/fuentes/` con extracción de necesidades
  - *Evaluar cómo automatizar este flujo con un agente del vault* (disparador, prompt, formato de salida)
- **Cowork / GitHub Actions:** evaluar schedule para que corra automáticamente y actualice la copia local del repositorio
- **Enseñar todo documentado en vault:** guía viva en `wiki/` con pasos, capturas y criterios, para uso autónomo posterior

| Bloque | Entregable | Horas netas | Valor ref. 15 USD/h |
|---|---|---|---|
| Reunión conceptual + relevamiento | Entendimiento compartido + inventario PCs | 2 hs | 30 USD |
| Instalación OpenCode Zen | Vault conectado y validado con prompt de prueba | 2 hs | 30 USD |
| Fathom desde Meet → vault | Flujo raw → wiki/fuentes con extracción (portugués) + evaluación agente | 5 hs | 75 USD |
| Cowork schedule / GH Actions | Sincronización copia local automática | 3 hs | 45 USD |
| Documentación en vault | Guía amigable para Emilia + registro consumo | 2 hs | 30 USD |
| **Total Semana 1** | **Vault encendido y enseñable** | **14 hs** | **210 USD** |

*Elapsed estimado: 14 hs netas ≈ 18.5 hs elapsed con pomodoros 25+5 y pausas de 30 min entre turnos (jornada tipo 8:30–10:30 / 11:00–13:00 / 13:30–15:30 / 16:30–18:00).*

---

## Semana 2 — Estructura + Representación Inicial con Casa en Construcción (14 hs netas)

**Base:** proyecto de casa ya realizado por el estudio y actualmente en construcción — oportunidad concreta de mejora.

**Objetivo verificable:** estructura de archivos definida y primeros criterios de representación documentados con referentes.

- **Estructura de archivos + mejora sobre seteo actual:** organización de carpetas del vault aplicada a la casa, con primeros ajustes de puntas, bloques de AutoCAD, visual, láminas y rótulos — apuntando a mejora de representación con base ordenada
- **Búsqueda de referentes y carga en carpeta:**
  - Fuentes: página web, Instagram, Facebook, ArchDaily, Pinterest, etc.
  - Evaluación: cómo entran los referentes al sistema, cómo se procesan y qué info se extrae
  - Alimentación de **modelos de visualización**: códigos de colores, manera de representación arquitectónica, paletas, grosores, sombras, texturas
  - Nota: el sistema puede variar entre proyectos; la idea es implementar un sistema de representación bien aceitado y definido, y cuando esté consolidado crear otro
- **Entregable:** estructura aplicada sobre la casa + carpeta de referentes curada + ficha por referente (qué tomar, qué dejar, cómo traducir)

| Bloque | Entregable | Horas |
|---|---|---|
| Curaduría referentes | 20–30 referentes con ficha, cargados en carpeta y evaluados por fuente | 5 hs |
| Análisis y extracción | Códigos de color y criterios de visualización para modelos de representación | 3 hs |
| Aplicación sobre casa | Ajuste de puntas, bloques, láminas y rótulos sobre proyecto real | 4 hs |
| Documentación wiki | Ficha del sistema de representación en `wiki/estandares/` | 2 hs |
| **Total Semana 2** | **Sistema de representación documentado sobre caso real** | **14 hs → 210 USD** |

*Futuro: evaluar LoRA a partir del sistema consolidado.*

---

## Semana 3 — Estándares Básicos AutoCAD + Representación Casa (14 hs netas)

**Objetivo verificable:** estructura de archivos y seteo de estándares básicos de AutoCAD operativos sobre la casa en construcción.

- **Estructura de archivos:** carpetas, nomenclatura y plantilla base del vault aplicada al proyecto de la casa
- **Seteo básico:** puntas, layers normalizados, estilos de texto/cota, plantilla DWT, bloques básicos, láminas y rótulos simples — apuntando a mejora de representación con base sólida
- **Aplicación sobre casa:** ajuste sobre proyecto real en construcción, con validación junto a Emilia
- **Documentación wiki:** ficha por cada estándar en `wiki/estandares/` con guía de uso

| Bloque | Entregable | Horas |
|---|---|---|
| Estructura de archivos | Carpetas + nomenclatura + plantilla vault sobre casa | 3 hs |
| Seteo básico AutoCAD | Layers, puntas, estilos, DWT, bloques básicos, láminas y rótulos | 6 hs |
| Aplicación sobre casa | Ajustes sobre proyecto real + validación | 3 hs |
| Documentación wiki | Fichas de estándares con guía paso a paso | 2 hs |
| **Total Semana 3** | **Estándares básicos operativos sobre caso real** | **14 hs → 210 USD** |

---

## Semana 4 — Documentación y Clase Explicatoria (10 hs netas + 2 hs clase)

**Objetivo verificable:** todo lo realizado en Mes 1 documentado y enseñado para uso autónomo. Estructura + estándares básicos como cierre de Mes 1.

- **Documentación entregada:** vault y Fathom, estructura de archivos, seteo básico AutoCAD (rótulos, layers, DWT, bloques), sistema de representación inicial — cada activo con su ficha wiki
- **Clase explicatoria:** repaso de todo lo realizado en el mes, con demostración en vivo y entrega de accesos (Leantime, vault, flujos)
- **Cierre con métrica de mejora:** qué se mapeó, dónde aportó IA (scripts Lisp), y próximos ciclos de mejora

| Entregable | Horas |
|---|---|
| Consolidación documentación | 6 hs |
| Preparación clase | 4 hs |
| Clase explicatoria | 2 hs |
| **Total Semana 4** | **Cierre enseñable Mes 1** | **12 hs → 180 USD** |

> **Mes 2 (previsto):** flujo ComfyUI que posprocesa salida de AutoCAD (ControlNet Canny, prueba simple previa a ofrecer, evaluación RunPod) — se activa solo cuando Mes 1 esté aceitado.

---

## Leantime MCP — Tablero de tareas (futuro cercano, Mes 2)

- Estado: Leantime ya instalado en VPS local
- Pendiente: crear usuario para Emilia, compartir URL y pass, conectar MCP al vault para que tareas de reuniones y specs alimenten el tablero automáticamente
- Beneficio: PM liviano con Kanban, métricas y mejora continua integrada al vault
- Nota Mes 1: foco en estructura + estándares básicos; Leantime se integra como tablero cuando el flujo base esté aceitado

---

## Valor y pricing early bird

**Anclaje de valor completo (mes referencia):**
- Desarrollo focalizado: 52 hs netas (Semanas 1–3: 42 hs + Semana 4: 10 hs) → 780 USD
- Clase: 2 hs → 30 USD
- Presencial quincenal: 2 jornadas → 200 USD
- **Total mes valor referencia: ~1010 USD (rango comunicado 800–1200 USD)**

**Early bird bonificado (grupo inicial y futuro caso de éxito para academia):**
- Semana 1: 210 USD
- Semana 2: 210 USD
- Semana 3: 210 USD
- Semana 4: 180 USD
- Presencial quincenal incluido como inversión en vínculo (200 USD mes)
- **Presentación recomendada:** 200 USD reuniones (12 hs mes) + 100 USD capacitación inicial como hito, con desarrollo por hito a 15 USD hora neta — transparencia que celebra inversión fundadora

**Objetivo del early bird:** mapear procesos y demostrar dónde el uso de IA (incluso escribiendo Lisp/AutoLISP para estándares) genera valor reutilizable para la academia.

---

## Métricas de éxito

- Horas liberadas de gestión por semana (objetivo Semana 1: 5 hs liberadas)
- Reuniones transcriptas y buscables (objetivo: 100% con entrada wiki en 24 hs)
- Activos documentados con wiki viva (objetivo mes: 8 fichas + prompt-packs)
- Consumo OpenCode Zen registrado semanalmente (transparencia)
- Ritual semanal "Victoria + Mejora" 15 min con 3 victorias registradas por semana en `log.md`
- Sistema de representación adoptado sobre casa en construcción y replicable a próximo proyecto

---

## Cronograma y ritmo

- **Ritmo optimizado con IA:** franjas 8:30–10:30 / 11:00–13:00 / 13:30–15:30 / 16:30–18:00, hasta 4 jornadas intensivas por semana, 14 hs netas asignadas a este proyecto
- **Hitos presenciales:** Miércoles Semana 1 (conceptual + relevamiento), Semana 3 validación flujo ComfyUI, Semana 4 clase de cierre
- **Validación ComfyUI simple:** probar flujo mínimo en Semana 3 antes de ofrecerlo como servicio

---

## Próximos pasos

1. Validar este plan (Mes 1: estructura + estándares básicos)
2. Semana 1 — Miércoles: reunión conceptual + instalación OpenCode Zen (Sol: zen+go, Emilia: zen+openai) + Fathom desde Meet con agente del vault
3. Semana 2 — Estructura de archivos + representación inicial sobre casa en construcción + referentes multi-fuente
4. Semana 3 — Estándares básicos AutoCAD completos sobre la casa
5. Semana 4 — Entregar documentación y clase de cierre Mes 1
6. Mes 2 — Probar flujo ComfyUI simple que posprocesa AutoCAD (solo si Mes 1 está aceitado)

---

## Referencias

- `AGENTS.md` — schema del vault y estructura proyectos/wiki
- `wiki/glosario/conceptos/cerebro-digital-karpathy` — Cerebro digital y aplicación al vault
- `wiki/glosario/conceptos/sdd-spec_driven_development` — SDD via opencode (SPEC FIRST)
- `proyectos/260907-brain_emilia/00-index.md` — ficha del proyecto linkeada a este spec
