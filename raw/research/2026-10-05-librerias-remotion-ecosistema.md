---
tipo: research
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [remotion, video, motion-design, ecosistema, dependencias, codigo]
---

# 2026-10-05 Librerías del ecosistema Remotion

Fecha: 2026-10-05 America/Argentina/Buenos_Aires (-03:00) | Fuentes: 16 verificadas | Confianza: Alta (datos de API, no de documentación)

> **Por qué este documento**: para producir los videos educativos del estudio con Remotion hay que decidir si se usa una librería de componentes o se escriben a mano. La pregunta no es "cuál es más popular" sino "cuál sigue existiendo dentro de un año". Este documento registra la evidencia para que la decisión sea revisable.

- [[#1. Metodología]]
- [[#2. Tabla comparativa]]
- [[#3. Paquetes oficiales de Remotion]]
- [[#4. Fichas por repositorio]]
- [[#5. Los dos candidatos para nuestro caso]]
- [[#6. Descartados y por qué]]
- [[#7. Conclusión]]
- [[#8. Qué re-verificar y cuándo]]
- [[#9. Referencias]]

## 1. Metodología

### De dónde sale cada campo

| Campo | Fuente | Nota |
|---|---|---|
| Estrellas, forks, issues, licencia | `api.github.com/repos/{owner}/{repo}` | Campo `license` de la API: si devuelve `null` es que **no hay archivo de licencia**, no que sea "desconocida" |
| **Mantenimiento** | Campo `pushed_at` de la misma API | Ver nota crítica abajo |
| Fecha de creación | Campo `created_at` | Sirve para medir antigüedad real del proyecto |
| Uso real | `api.npmjs.org/downloads/point/last-month/{pkg}` | Ventana de 30 días: 2026-09-05 a 2026-10-04 |
| Versión publicada | `registry.npmjs.org/{pkg}/latest` | Útil cuando el repo no tiene tags |

### La nota crítica: `pushed_at`, no `updated_at`

`updated_at` **se mueve con estrellas, issues y forks**. Un proyecto abandonado con mucha popularity sigue teniendo `updated_at` reciente. La señal de mantenimiento es `pushed_at`, que solo cambia cuando alguien sube commits.

El caso de este documento lo demuestra: [[wiki/glosario/software/remotion-time|remotion-time]] tiene `updated_at: 2025-10-26` (parece vivo) pero `pushed_at: 2023-09-04` (lleva 3 años sin un commit). Y `remotion-animated` tiene 226 estrellas y 5.907 descargas mensuales con **590 días sin push**.

### Regla de decisión que se desprende

Estrellas y descargas miden interés. `pushed_at` mide si el proyecto existe. Para una dependencia que se va a copiar al proyecto y usar por años, importa el segundo.

## 2. Tabla comparativa

Datos consultados el **2026-10-05**.

| Repositorio | Estrellas | Último push | Días sin push | Descargas/30d | Licencia | Issues | Forks | Veredicto |
|---|---|---|---|---|---|---|---|---|
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 62.050 | 2026-10-05 | **0** | 7.295.316 | propia | 234 | 4.803 | Base. Sostenido por empresa |
| [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) | 6.467 | 2026-09-28 | 7 | 13.908 | MIT | 35 | 272 | Descartado: no es de Remotion |
| [av/remotion-bits](https://github.com/av/remotion-bits) | 485 | 2026-09-15 | 20 | 14.260 | **ninguna** | 1 | 27 | Descartado: sin licencia |
| [stefanwittwer/remotion-animated](https://github.com/stefanwittwer/remotion-animated) | 226 | 2025-02-22 | **590** | 5.907 | MIT | 0 | 18 | Descartado: abandonado |
| [riaz37/remotion-ui](https://github.com/riaz37/remotion-ui) | 65 | 2026-09-29 | 6 | 814 | MIT | 5 | 2 | Viable con precaución |
| [degueba/onda](https://github.com/degueba/onda) | 24 | 2026-08-07 | 59 | 267 | MIT | 8 | 2 | Viable con precaución |
| [fwextensions/remotion-time](https://github.com/fwextensions/remotion-time) | 19 | 2023-09-04 | **1.127** | 186 | MIT | 1 | 1 | Descartado: abandonado |

**Ninguno de los repos archivados** (`archived: false` en todos): ninguno fue marcado como archivado por sus autores. El abandono es silencioso.

## 3. Paquetes oficiales de Remotion

Estos sí están sostenidos por la casa madre, que hace push diario. Son la base sana del proyecto.

| Paquete | Qué resuelve | Para nuestro caso |
|---|---|---|
| `@remotion/transitions` | Transiciones entre escenas (`fade`, `slide`, `wipe`, `flip`, `clockWipe`) | Ya instalado. Todas las escenas del video pasan por acá |
| `@remotion/paths` | Utilidades de paths SVG: `getLength`, `getPointAtLength`, `evolvePath`, `interpolatePath` | **El camino para dibujar la escalera y los conectores** |
| `@remotion/shapes` | Generadores de formas SVG: `makeCircle`, `makePolygon` | Iconos y nodos del diagrama |
| `@remotion/fonts` / `@remotion/google-fonts` | Carga de fuentes determinista en render | Necesario para el cambio tipográfico |
| `@remotion/layout-utils` | `measureText`, `fitText`, `fillTextBox` | Que el texto no desborde nunca |
| `@remotion/media-utils` | Duración y dimensiones de audio/video | Para cuando agreguemos locución |
| `@remotion/mcp` | MCP oficial de Remotion (MIT, 4.0.473) | Expone docs a agentes |

Todos alineados en versión `4.0.533` (= la de Remotion). Regla de la casa: **instalar con `--save-exact` y mantener todos los `@remotion/*` en la misma versión**.

## 4. Fichas por repositorio

### av/remotion-bits — 485 estrellas, sin licencia

El más usado del ecosistema (14.260 descargas/mes) y el único con **ausencia de licencia**: la API devuelve `"license": null`.

- **Qué trae**: gráficos, transiciones, revelados de texto, sistemas de partículas, escenas 3D
- **MCP**: sí. `npx remotion-bits mcp`, con las herramientas `find_remotion_bits` y `fetch_remotion_bit`
- **Cómo entra**: dos vías. Como paquete npm (import directo, caja negra) o copiando fuentes con `jsrepo`
- **Riesgo**: **legal**. Sin licencia no hay permiso de uso explícito. Para un estudio que factura, es un riesgo que no compensa
- **Lo bueno**: 1 issue abierto, el mejor curation ratio de todos

### riaz37/remotion-ui — 65 estrellas, 4 meses

El de mayor catálogo: **217 componentes + 18 transiciones**, organizados por carril de movimiento.

- **Qué trae**: primitivas, escenas, charts, captions, 3D, shaders, motion graphics, composiciones completas
- **MCP**: sí. `remotion-ui-mcp` expone `list-components`, `search-components`, `get-component-detail`, `get-install-command`. También publica `llms.txt` y una agent skill
- **Cómo entra**: `npx remotion-ui@latest add <nombre>`. Los componentes se **copian** como `.tsx` al proyecto; nunca se importan del paquete npm
- **Regla del proyecto**: irreversible. El CLI **registra compositions en `Root.tsx` automáticamente**, así que hay que commitear antes de instalar
- **Riesgo**: proyecto de una sola persona, 4 meses de antigüedad, 0 suscriptores y 2 forks. Sin red de seguridad upstream
- **Regla declarada por sus autores**: *"Nunca uses CSS transitions, CSS keyframes ni clases de animación Tailwind: no se renderizan en video"*. Todo el movimiento va con `useCurrentFrame()`, `interpolate()` y `spring()`

### degueba/onda — 24 estrellas, casi sin uso

70 componentes + 18 transiciones, sobre una capa foundation propia.

- **Lo distintivo**: es la única con **sistema de diseño real**. Tokens (`COLOR`, `FONT`, `SPACING`), movimiento (`DURATION`, `STAGGER`, `SPRING_SMOOTH`, `HOUSE_EASE`) y hooks (`useEntrance`, `useStaggeredEntrance`, `useTextReveal`)
- **Por qué importa acá**: el problema de que un video se vea "armado" es de identidad de movimiento. Onda obliga a que todo el video use la misma grilla. Es exactamente la medicina que hace falta acá
- **Cómo entra**: `npx ondajs add <nombre>`, fuente copiada, dependencias de foundation incluidas
- **Tipos**: todo tipado con Zod, cada componente expone su schema
- **Riesgo**: 267 descargas/mes y 59 días sin push. Proyecto de una persona con 2 forks

### ibelick/motion-primitives — 6.467 estrellas, muy activo, pero no sirve

El más popular con diferencia y el más mantenido (push hace 7 días).

- **Qué es**: un UI kit para **web**, construido sobre `motion` (framer-motion) y Tailwind CSS
- **Por qué se descarta**: no es una librería de Remotion. `framer-motion` anima por reloj del navegador, no por frame. En video eso rompe el determinismo: el mismo frame renderizado dos veces puede dar resultados distintos
- **Además**: exige Tailwind, que en este proyecto se descartó a propósito en la creación

### stefanwittwer/remotion-animated — 226 estrellas, abandonado

API declarativa (`<Animated />`) con animaciones encadenables.

- **Descartado**: último commit el **2025-02-22**, hace 590 días
- **Lección**: sus 5.907 descargas mensuales son en su mayoría de gente que ya lo tiene instalado. Descarga alta no significa proyecto vivo

### fwextensions/remotion-time — 19 estrellas, abandonado

Hooks basados en segundos en vez de frames. Utilísimo conceptualmente (evita tener que pensar en frames), pero:

- **Último commit**: 2023-09-04, hace 3 años. La versión publicada sigue siendo `0.0.3`
- **Descartado** por abandono

## 5. Los dos candidatos para nuestro caso

Si en algún momento se decide usar librería, estos son los componentes que resuelven la escalera de madurecimiento que necesitamos:

| Necesidad | RemotionUI | Onda |
|---|---|---|
| Escalera de peldaños ascendentes | `timeline-steps`, `roadmap-lanes` | `progress-steps`, `timeline` |
| Conectores que se dibujan | `connector-lines`, `path-draw`, `arrow-annotate` | `draw-on`, `node-graph` |
| Números que cuentan | `counter` | `count-up` |
| Escalonado no uniforme | `stagger-children`, `staggered-fade-up` | `useStaggeredEntrance` + `STAGGER` |
| Fondo con grano | `animated-noise-grain`, `dynamic-grid` | `grain-overlay`, `dynamic-grid` |
| Árbol / jerarquía | `org-chart-build`, `file-tree-reveal` | `node-graph` |
| Transiciones | 18 (incluye `directional-wipe`) | 18 (incluye `glassWipe`, `dipToColor`) |
| Cuando haya voz | `srt-caption-track`, `word-pop-captions` | `captions` |

## 6. Descartados y por qué

| Descarte | Motivo |
|---|---|
| **av/remotion-bits** | **Sin licencia.** Riesgo legal en un estudio que factura |
| **stefanwittwer/remotion-animated** | 590 días sin push |
| **fwextensions/remotion-time** | 3 años sin push |
| **ibelick/motion-primitives** | No es de Remotion. Rompe el determinismo de frame |
| **riaz37/remotion-ui** *(por ahora)* | 65 estrellas, 4 meses, proyecto de una persona. Se deja disponible, no se adopta |
| **degueba/onda** *(por ahora)* | 24 estrellas, 267 descargas/mes. Se deja disponible, no se adopta |

## 7. Conclusión

El proyecto de videos vive en `P:\00-repos\remotion-vault`, standalone y con su propio git.

**Decisión: escribir los componentes a mano.** Fundamento:

1. **Las dos librerías con sistema de diseño son casi huérfanas** (65★ y 24★, dos forks cada una, de una sola persona). Adoptarlas significa heredar ese riesgo.
2. **La única con adopción real no tiene licencia.** El riesgo legal no compensa los 16 charts.
3. **Necesitamos ~8 tipos de escena, no 217.** La escalera de madurecimiento son unas 60 líneas con `@remotion/paths` y las curvas que ya están en `tokens.ts`.
4. **Copiar fuente ajena tiene un costo oculto**: queda código que no entiende ninguno de los dos y que hay que mantener para siempre. Escribirlo propio es más barato cuando el volumen es bajo.

**Regla que queda asentada para el futuro**: si algún día se instala una librería, el código entra **copiado como fuente editable**, nunca importado como paquete. Así una dependencia abandonada no rompe el render.

**Lo que sí se descarta de esta decisión**: las 18 transiciones y los 16 charts por los que RemotionUI es cómodo. Cuando un episodio necesite un chart de verdad, esa es la señal para revisitarla.

## 8. Qué re-verificar y cuándo

| Qué | Cuándo | Cómo |
|---|---|---|
| `pushed_at` de los 7 repos | Cada 90 días | `api.github.com/repos/{owner}/{repo}` |
| Licencia de `av/remotion-bits` | Cada 90 días | mismo endpoint, campo `license` |
| Versión de Remotion | Antes de cada episodio nuevo | `npm view remotion version` |

Criterio de re-apertura: si **Onda** o **RemotionUI** superan 500 estrellas **y** mantienen push en los últimos 60 días, la decisión se revisa con evidencia nueva.

## 9. Referencias

Todas verificadas el 2026-10-05.

- Core Remotion — https://www.remotion.dev/docs — 200 — https://github.com/remotion-dev/remotion
- Lista de recursos de Remotion (catálogo de librerías) — https://www.remotion.dev/docs/resources — 200
- `@remotion/paths` — https://www.remotion.dev/docs/paths — 200
- `@remotion/shapes` — https://www.remotion.dev/docs/shapes — 200
- Instalación y requisitos de sistema — https://www.remotion.dev/docs — 200 — "Node 16 o Bun 1.0.3"; FFmpeg incluido desde v4.0
- CLI `create-video` — https://www.remotion.dev/docs/cli/create-video — 200 — confirma que `--yes` falla dentro de un repo git
- FFmpeg en Remotion — https://www.remotion.dev/docs/ffmpeg — 200 — auto-instalación desde v3.3, embebido desde v4.0
- Licencia de Remotion — https://github.com/remotion-dev/remotion/blob/main/LICENSE.md — 200 — gratis hasta 3 empleados
- RemotionUI — https://github.com/riaz37/remotion-ui — 200 · https://remotionui.com/docs/components/browse — 200
- Onda — https://github.com/degueba/onda — 200 · https://remotion.onda.video/docs/catalog — 200
- Remotion Bits — https://github.com/av/remotion-bits — 200 · https://www.npmjs.com/package/remotion-bits — 200
- motion-primitives — https://github.com/ibelick/motion-primitives — 200 · https://motion-primitives.com/docs — 200
- remotion-animated — https://github.com/stefanwittwer/remotion-animated — 200
- remotion-time — https://github.com/fwextensions/remotion-time — 200
- Datos numéricos: `api.github.com/repos/{owner}/{repo}` y `api.npmjs.org/downloads/point/last-month` — 200

### Contexto en el vault

- [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] —material del episodio 1 de video
- [[proyectos/MVP_02-autocad-standards/00-filo-mvp_02|manifiesto del dibujo]] — material del episodio 2
- [[wiki/glosario/software/ffmpeg|ffmpeg]] — aunque Remotion v4 lo embebe, está en el stack

### Destinos wiki propuestos

- `wiki/glosario/software/remotion` — la herramienta y su pipeline desde markdown
- `wiki/glosario/software/remotion-ecosistema` — este documento, curado

Pendiente de curación por `@vaultworm-arq`.
