---
tipo: log
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [sesion, remotion, video, motion-design, tipografia, ecosistema, mvp]
---

# Sesión 2026-10-05 — Videos educativos del vault con Remotion (arranque + 2 episodios + diseño)

> Cerrada a las 01:15 del 2026-10-06. El trabajo ocurrió enteramente el 05; la nota se escribe con esa fecha y el cruce de medianoche queda anotado acá.

## Qué se hizo

### 1. Decisión de arquitectura (4 ítems, uno por vez)

| Ítem | Decisión |
|---|---|
| Ubicación | `P:\00-repos\remotion-vault` — standalone, fuera del vault, repo git propio. Descartado `proyecto-pi\tools` porque no viaja con el vault y no es repo |
| Audiencia | Onboarding interno del estudio, foco en metodología y estándares. Fuera finanzas/legal por confidencialidad |
| Locución | Sin voz al inicio: texto + música + subtítulos. Se valida layout antes de bloquear audio |
| Capítulo piloto | `ptech-filosofia` (12.2k, el más maduro) |

**Restricción verificada:** `create-video --yes` falla dentro de un repo git. Por eso el proyecto vive en `P:\00-repos\`, no en el vault.

**Licencia:** Remotion es gratis hasta 3 empleados. Si el estudio supera ese número, hay que comprar company license. **Pendiente de confirmar con Sol.**

### 2. Instalación (F1)

- `npx create-video@latest --yes --blank --no-tailwind remotion-vault` → 4.0.533, 278 MB, git init propio
- `npx remotion skills add` → 12 Agent Skills oficiales (`best-practices`, `animations`, `compositions`, `timing`, `render`, `captions`…). Se leyeron `timing`, `sequencing`, `transitions`, `multi-scene-video`, `measuring-text`, `local-fonts` y `video-layout` antes de codear
- `npx remotion add @remotion/transitions` → 4.0.533, alineado
- **Remotion Studio desacoplado** con `Start-Process` + log a archivo, para no bloquear la terminal de trabajo. Abre en `localhost:3000`
- Entorno verificado: Node v24.15.0, npm 11.12.1, FFmpeg 9.0.2, Windows x86_64. Sin necesidad de GPU

### 3. Episodio 1 — Filosofía Pitautech (13 escenas, 2370 f ≈ 79 s)

Fuente: [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]]. Componentes reutilizables: portada, tarjetas, flujo, tabla, cita, glosario, pregunta, cifra. `TransitionSeries` con duración calculada por fórmula (suma − solapes), nunca a mano. **Comiteado** (`551468f`).

### 4. Episodio 2 — Manifiesto del dibujo (9 escenas, 1890 f ≈ 63 s)

Fuente: [[proyectos/MVP_02-autocad-standards/00-filo-mvp_02|manifiesto del dibujo]]. Componentes nuevos: `duelo` (dos columnas enfrentadas + puente) y `principios` (layout adaptativo: 2 items grandes / 3–4 medianos / 5+ compactos numerados) y `ensayo`. **Sin commitear.**

### 5. Rediseño de movimiento (lab)

Diagnóstico de por qué se veía "hecho por IA": una sola curva para todo, staging uniforme, fade en todas las transiciones, fondo muerto, sin ejecución tipográfica. Implementado en `src/componentes/movimiento.tsx` + `tokens.ts`:

- 3 curvas con nombre (`CURVA_TITULAR`, `CURVA_BADGE`, `CURVA_LINEA`)
- Staging no uniforme (`STAGING.foco/acompañante/bloque/marca`)
- Fondo vivo: parallax + halo que respira
- Revelado por líneas con `clip-path`
- Números que cuentan, líneas que se dibujan con `scaleX`
- Grano SVG inline (no `background-image`: Remotion lo prohíbe por no determinismo)
- Barra de progreso de capítulo

**Dos escenas de laboratorio** (`Lab-1-Cifra`, `Lab-2-Tarjetas`) para comparar antes/después en la misma pantalla.

### 6. Investigación del ecosistema (documento de review)

Verificados 7 repos contra `api.github.com` y `api.npmjs.org`. Resultado en [[raw/research/2026-10-05-librerias-remotion-ecosistema|2026-10-05-librerias-remotion-ecosistema]].

**Hallazgos que corrigen la intuición:**

- `av/remotion-bits`: 485★ y 14.260 descargas/mes pero **`"license": null`** → descartado por riesgo legal
- `stefanwittwer/remotion-animated`: 226★ y 5.907 descargas/mes pero **590 días sin push** → abandonado
- `fwextensions/remotion-time`: `updated_at` 2025-10-26 (parece vivo) pero `pushed_at` 2023-09-04 (**1.127 días**)
- `riaz37/remotion-ui` (65★) y `degueba/onda` (24★): proyectos de una persona, 4 meses, 2 forks cada uno, **sin red de seguridad upstream**
- `ibelick/motion-primitives`: 6.467★ y muy activo, pero es UI kit de web sobre framer-motion → rompe el determinismo de frame

**Decisión registrada: escribir los componentes a mano.** Se necesitan ~8 tipos de escena, no 217. Regla asentada: si alguna vez se instala una librería, el código entra **copiado como fuente editable**, nunca importado.

### 7. Tipografía — verificado, no implementado

9 familias confirmadas contra la API de Google Fonts (`latin` + `latin-ext`, cubren tildes y ñ): Space Grotesk, Instrument Serif, JetBrains Mono, Inter, Lora, Archivo, Newsreader, Fraunces, Work Sans. `@remotion/google-fonts` existe en 4.0.533, alineado con Remotion.

Orden de impacto real para que un video no parezca genérico: **1) tipografía · 2) restricción a 4 efectos · 3) cortar contenido · 4) ritmo variable · 5) animación** (la animación es la última, no la primera).

### 8. Regla nueva en `AGENTS.md`

Equivalencias de aprobación: `s`, `si`, `sí`, `ok`, `dale`, `avanzá`, `adelante`, `sí dale`, `go` equivalen a `s`. Cancelan: `n`, `no`, `esperá`, `pará`, `stop`. La aprobación vale solo para lo recién descrito.

## Hallazgo de integridad del vault

**Los estándares CAD del glosario están vacíos.** Las 4 páginas (`capas-layers`, `plot-styles`, `nomenclatura-planos`, `bloques`) son el mismo stub: *"Pendiente de redactar - entrada creada para que el índice sea recorrible"*. 12 de 19 archivos en `standares/` son stubs.

**Pero el estándar CAD real existe**, en `proyectos/MVP_02-autocad-standards/`: manifiesto (6.2k), SET_01 replanteo (24k) y SET_02 uso de suelo DGIUR (33.5k, con tabla real de 21 capas con ACI, lineweight, flag de plot y los "por qué").

Quien entra por `standares/tecnico/00-index` hoy no encuentra nada, aunque el estándar existe. **Es un agujero de onboarding, no solo de video.**

## Archivos modificados

### Vault (`P:\00-repos\proyecto-pi\vault-arquitectura`)

- `raw/research/2026-10-05-librerias-remotion-ecosistema.md` (nuevo, 215 líneas)
- `raw/research/00-index.md` (una fila)
- `AGENTS.md` (regla de equivalencias de aprobación)
- `raw/sessions/2026-10-05-sesion-remotion-videos.md` (esta nota)

**Nada commiteado en el vault.** `git status` mezcla cambios previos ajenos a esta sesión (log.md, opencode.json, MVP_04, wiki/glosario/software/leantime.md, sesiones del 09-30 y 10-05).

### Proyecto de video (`P:\00-repos\remotion-vault`, repo propio)

- `src/tokens.ts` — tokens + 3 curvas + staging + tiempos
- `src/datos/episodio-filosofia.ts` (nuevo) · `src/datos/episodio-manifiesto.ts` (nuevo)
- `src/componentes/base.tsx` · `src/componentes/tarjeta.tsx` (nuevos)
- `src/componentes/movimiento.tsx` (nuevo)
- `src/escenas/portada.tsx` · `src/escenas/escenas.tsx` · `src/escenas/manifiesto.tsx` (nuevos)
- `src/FilosofiaPitautech.tsx` · `src/ManifiestoDibujo.tsx` · `src/lab.tsx` (nuevos)
- `src/Root.tsx` — 4 compositions · `src/Composition.tsx` (borrado, template vacío)
- `.gitignore` — `studio.log`, `studio.err.log`, `renders`, `.agents/`, `skills-lock.json`
- Commit `551468f` solo cubre el episodio 1. **Episodio 2 + lab + movimiento están sin commitear**

## Análisis cerebro-digital

**Topics**

- Remotion como framework de video programático: por qué el proyecto va fuera del vault (regla de binarios) y por qué `create-video` exige estar fuera de un repo git
- Arquitectura de datos separada de componentes: los `.md` del vault son la fuente, `src/datos/` es la selección curada, y cada escena declara su sección de origen para re-sincronizar
- Duración de composición como fórmula, no como constante: `suma(duraciones) − solapes de transición`
- Por qué un video se percibe "generado": una sola curva, staging uniforme, transiciones idénticas, fondo estático
- Identidad de movimiento como requisito de diseño, no como decoración: 3 curvas nombradas + staging no uniforme
- Determinismo de render en video: por qué `background-image`, CSS transitions y framer-motion no sirven en video y sí en web
- Medición de salud de un proyecto open source: `pushed_at` > `updated_at`; estrellas y descargas miden interés, no existencia
- Criterio de descarte de dependencias: licencia ausente = descarte para un estudio que factura, independientemente de la popularidad

**Entidades**

- `P:\00-repos\remotion-vault` — proyecto de video, repo git propio, Remotion 4.0.533, Node v24.15.0
- Compositions registradas: `01-FilosofiaPitautech`, `02-ManifiestoDibujo`, `Lab-1-Cifra`, `Lab-2-Tarjetas`
- Paquetes: `@remotion/transitions`, `@remotion/google-fonts` (4.0.533) · npm global `P:\00-repos\npm-global` (tiene el patrón de shims `.cmd`/`.ps1`)
- Fuentes candidatas: Space Grotesk, Instrument Serif, JetBrains Mono, Inter, Lora, Archivo, Newsreader, Fraunces, Work Sans
- Librerías evaluadas: RemotionUI (217 componentes, MCP `remotion-ui-mcp`), Onda (70 componentes, capa foundation), Remotion Bits (sin licencia), motion-primitives (web), remotion-animated y remotion-time (abandonados)
- Contenido fuente de video: [[wiki/glosario/interno/standares/ptech-filosofia]], [[proyectos/MVP_02-autocad-standards/00-filo-mvp_02]], `SET_01-REP` (24k), `SET_02-GEST_DGIUR_USO` (33.5k)

**Hechos**

1. `create-video --yes` **falla dentro de un repo git**. Por eso el proyecto no puede vivir en `proyecto-pi\tools`.
2. Remotion **prohíbe `background-image`** por no determinismo entre renders. El grano tiene que ser SVG inline.
3. Los hooks de React **no se pueden llamar dentro de `.map()`**. Para listas hace falta una función pura que reciba `frame` como argumento.
4. Un hook con nombre que no empieza por `use` rompe la regla `react-hooks/rules-of-hooks`.
5. RemotionUI y Onda registran compositions en `Root.tsx` automáticamente → hay que commitear antes de instalar.
6. RemotionUI declara explícitamente que **CSS transitions, CSS keyframes y clases de animación Tailwind no se renderizan en video**.
7. El `.gitignore` del template de Remotion **no incluye los logs** del Studio → se commitean por error si no se agregan.
8. La API de GitHub devuelve `"license": null` cuando **no hay archivo de licencia**. No es "desconocida": es ausencia.
9. `updated_at` se mueve con estrellas e issues. `pushed_at` es la única señal de mantenimiento.
10. `Lab-2-Tarjetas` sin fondo visible **no es bug**: las tarjetas son opacas con `flex: 1` y tapan la trama.
11. 12 de 19 archivos de `standares/` son stubs. El estándar CAD real vive en `proyectos/MVP_02-autocad-standards/`.
12. El manifiesto dice 7 peldaños (estándar, template, checklist, automatización, agente, protocolo, validación), no 5, y no incluye "playbook".

## Pendientes

| # | Qué | Estado |
|---|---|---|
| 1 | Commitear episodio 2 + lab + movimiento en `remotion-vault` | Sin commitear |
| 2 | Commitear los 2 archivos del vault | Sin commitear |
| 3 | `Lab-3-Tipos`: 4 combinaciones tipográficas en grilla 2×2 | Diseñado, sin implementar |
| 4 | `EscenaEscalera`: escalera de los 7 peldaños de madurecimiento | Diseñado, sin implementar |
| 5 | Corregir el fondo de `Lab-2-Tarjetas` | Cards opacas tapan la trama |
| 6 | Confirmar tamaño del estudio → define si Remotion necesita company license | **Bloqueante para escalar** |
| 7 | Shim `remotion-vault.cmd` en `npm-global` | Sin hacer |
| 8 | `src/lib/parse-markdown.ts` — parser `.md` → props | Diferido: esperar 2–3 episodios |
| 9 | Render MP4 de ambos episodios | Sin hacer |
| 10 | Música de fondo con licencia verificada | Sin hacer |
| 11 | Decidir si `standares/tecnico/*.md` se rellenan o se redirigen a MVP_02 | Hole de onboarding |
| 12 | `@vaultworm-arq` curar el documento de ecosistema a `wiki/glosario/software/remotion-ecosistema` | Propuesta en el índice |

## Para retomar

El Studio puede seguir corriendo. Si no:

```
Start-Process -FilePath "npm.cmd" -ArgumentList "run","dev" -WorkingDirectory "P:\00-repos\remotion-vault" -RedirectStandardOutput "P:\00-repos\remotion-vault\studio.log" -RedirectStandardError "P:\00-repos\remotion-vault\studio.err.log" -WindowStyle Hidden
```

Siguiente paso acordado: **tipografía antes que librería** (pendiente 3), porque es lo que más cambia la percepción con menos esfuerzo.