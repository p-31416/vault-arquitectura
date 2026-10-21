---
tipo: presentacion
cliente: Emilia Pimenta
proyecto: Studio OS
ciudad: Argentina
pais: AR
fase: entrega
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
estado: para-revision
tags: [revision, autocad, rep-araoz, set_01, dashboard, mvp_02]
idioma: es
---

# Revisión AutoCAD — 22/10/2026 (REP-ARAOZ + SET_01)

> Documento de trabajo para revisar mañana lo hecho con **REP-ARAOZ** y el **dashboard AutoCAD** (v2, reescrito el 21/10). Trae: qué se muestra, qué hay que verificar en el CAD, las preguntas abiertas y lo que quedó pendiente.
> Dashboard: `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html` · Bitácora: [[proyectos/MVP_02-autocad-standards/03-log-mvp_02|03-log-mvp_02]] · Sesión: `raw/sessions/2026-10-21-sesion-dashboard-autocad-v2.md`.

---

## 1. La idea de la sesión (30–40 min)

El Mes 1 cerró con una hipótesis: **"no digitalizar al arquitecto, aumentar su capacidad sin quitarle el control"**. Esta revisión muestra el resultado sobre **un plano real** y pide tres decisiones concretas.

| # | Qué revisamos | Dónde | Min |
|---|---|---|---|
| 1 | **El dashboard AutoCAD v2** — qué dice, qué números tiene, qué falta | `dashboard-autocad.html` | 10 |
| 2 | **El plano real** — el bloque de locales, la tabla de niveles, el twist del viewport | AutoCAD LT 2027 en vivo | 15 |
| 3 | **Los playbooks** — PB-01, PB-02 y la puerta única de wiki | vault | 5 |
| 4 | **Decisiones** — bloques a crear, qué queda del camino viejo | este doc | 10 |

---

## 2. Revisión del dashboard — qué hay que mirar

El dashboard es la página que resume el mes de CAD. Antes de mostrarlo, conviene tener claros sus 4 cifras ancla y 3 decisiones que pide.

### 2.1 Las cifras ancla (medidas, no estimadas)

| Cifra | Valor | Cómo se midió |
|---|---|---|
| Capas propias | **29** (más 21 del xref de fondo) | `list_layers` sobre el DWG real |
| Bloques nombrados | **14** en el DWG v2 · **13** en el DWT | catálogo en `docs/bloques-personalizados.md` |
| INSERTs en model | **203** (v2 del 20/10) · 208 (v1 del 13/10) | barrido de entidades |
| Locales numerados | **28** (`01`…`28`) | atributos `Nº`/`DESCRIPCION` de los rótulos `*U482` |
| Cotas | **273** (304 en la v1) | `DIMENSION` en model |
| Ahorro por plano | **12–15 h** (14 h invertidas en el SET) | `docs/desglose-configuraciones.md` |

> **Punto para la conversación:** por qué el número de INSERTs bajó de 208 a 203 y el de cotas de 304 a 273 entre el 13/10 y el 20/10 — lo más probable es limpieza de cotas y de exemplares anónimos durante el trabajo, pero conviene confirmarlo contra el DWG.

### 2.2 Las 12 secciones del dashboard (qué decir de cada una)

| # | Sección | Mensaje en una línea | Estado |
|---|---|---|---|
| 0 | Objetivo Emilia OS | hipótesis → experimento → conclusión del Mes 1 | igual que el 16/10 |
| 0b | **El entorno real: LT 2027** | sin COM, sin `DATAEXTRACTION`, con LSP | **nuevo** |
| 1 | **REP-ARAOZ v2 (medido 20/10)** | 2 layouts, viewport twist 360°, 28 rótulos | **nuevo** |
| 2 | **Bloque `SIMB-LOC_ID`** | número visible, nombre invisible, control de orden | **nuevo** |
| 3 | **Extracción dentro del DWG** | niveles en el DWG; locales en CSV | **nuevo** |
| 4 | **Playbooks: estado real** | qué está vigente, qué está en borrador, qué deriva | **nuevo** |
| 5 | **Bloques: los que faltan crear** | 11 ítems con dueño | **nuevo** |
| 6 | Herramientas: 4 LSP + 4 scripts | qué hace cada uno | actualizado |
| 7 | DWS en vivo | la norma que se cumple sola | igual |
| 8 | Ventana dinámica | 6 pasos, WIPEOUT y atributos | igual |
| 9 | Eficiencia | 7,5 h → 1,5 h por plano | igual |
| 10 | Pendientes | en el CAD / en el vault | **nuevo** |

### 2.3 Lo que el dashboard **no** muestra (a propósito)

- El LISP de cuadro de locales: **vía descartada** el 21/10. No se menciona como pendiente.
- El pipe a Google Sheet por n8n: figura como **en pausa** desde el 20/10, no como activo.
- El MCP `autocad` (COM): figura como **en pausa** mientras la máquina tenga LT.

---

## 3. Revisión del plano — la prueba en vivo

> Todo esto se hace en **AutoCAD LT 2027** (no Full). Recordar: LT no se puede automatizar desde afuera; la prueba es manual, en sesión.

### 3.1 El bloque de locales `SIMB-LOC_ID`

| Paso | Comando | Qué se ve |
|---|---|---|
| 1 | `APPLOAD` → `SET-01-SIMB-LOC-ID.lsp` | aviso de ruta no confiable (`SECURELOAD`) → Sí / Continuar |
| 2 | `SIMB-LOC_ID` | pide punto → número → nombre; **se reactiva solo** para el local siguiente. Enter en el nombre = repite el anterior; Enter en el número = automático |
| 3 | 2 locales de prueba | rectángulo 0,30 × 0,30 m con el número visible |
| 4 | `LOC-ID-CHECK` | lista de locales + control de orden de lectura |
| 5 | `U` | deshacer los 2 de prueba |

**Qué mirar:**
- [ ] El bloque se registra en la tabla de bloques (si no: `LOC-ID-DIAG` vuelca el estado).
- [ ] El rectángulo mide 0,30 × 0,30 m y el número entra a 0,12 m de alto.
- [ ] La capa del ejemplar es `A-SIMBOLO-NPT-PLANTA` (la definición va en capa 0).
- [ ] `LOC-ID-CHECK` no reporta faltantes ni repetidos con 2 ejemplares.
- [ ] Al salir, el control dice qué local está fuera de orden y cuál le corresponde.

> **Recordatorio técnico (por si vuelve a fallar):** AutoCAD LT **no acepta el `entmake` de un bloque** → la vía que funciona es el comando `-BLOCK` (geometría de trabajo en 1000,1000 + ventana de selección). Y `entdel` sobre el registro de un bloque **no libera el nombre**: si el bloque quedó a medias, `BLOQUE → Borrar` (o `P purge`) antes de volver a correrlo.

### 3.2 Los 28 locales (estado real)

| Comprobación | Resultado |
|---|---|
| Locales numerados | **28** (`01`…`28`), sin repetidos ni faltantes |
| Fuera de la planilla | `N=00 AMBIENTE` (planta baja, no es un local numerado) |
| Totales | DORMITORIO ×6 · BAÑO ×4 · BALCON ×4 · COC.-LAV. ×4 · ESTAR-COM. ×4 · TOILETTE ×2 · PALIER · ESCALERA · ASCENSOR I · ASCENSOR II |
| Orden de lectura | la numeración a mano **no** lo sigue (dato informativo, no se corrige) |
| Ejemplares de `SIMB-LOC_ID` en el DWG | **0** → los 28 numerados son los rótulos legacy `*U482` |

### 3.3 La tabla de niveles

Comando `CUADRO-NIVELES` → dibuja la tabla (MTEXT + LINE) en la capa `A-CUADRO-NIVELES`, con alto de fila 7 mm en paper / 0,70 m en modelo.

- [ ] La tabla se dibuja en el layout `REP-PTipo-A1-H`.
- [ ] `CUADRO-NIVELES-ACT` la actualiza en el sitio (borra solo lo que está dentro de la caja).
- [ ] `CUADRO-NIVELES-VAL` muestra el CSV sin dibujar.

### 3.4 El plano horizontal

- [ ] El layout `REP-PTipo-A1-H` imprime con el modelo **landscape** (viewport `1EC35` con twist 360°).
- [ ] Los rótulos de locales se leen **horizontales** en la lámina.
- [ ] La regla queda escrita: **compensación = (−twist) mod 360**.

---

## 4. Las 3 preguntas abiertas (necesitan respuesta del estudio)

| # | Pregunta | Contexto | Impacto |
|---|---|---|---|
| 1 | **Balcón del 1 PISO:** 3,88 (4 cm) o 3,87 (5 cm)? | El CSV tiene 3,87 como exterior y quedó un 3,88 en el balcón | 1 celda de la tabla de niveles |
| 2 | **Planta baja:** ¿exterior y balcón van en 0,00 o llevan otra cota? | Hoy la fila dice "–" | 1 celda de la tabla de niveles |
| 3 | **9 PISO (planta técnica):** ¿32,06 es el tanque (altura máxima) y 26,56 / 28,26 / 30,66 son los tres niveles de la misma planta técnica? | 4 valores en la misma fila | 4 celdas de la tabla de niveles |

> Regla ya confirmada: **exterior y balcón son el mismo valor = interior − 0,05 m**.

---

## 5. Los bloques que faltan crear (decisión del estudio)

| # | Bloque | SET | Qué tiene que hacer | Prioridad |
|---|---|---|---|---|
| 1 | `SIMB-LOC_ID` | SET_01 | **ya existe** (v2.2, probado) → falta insertar los 28 ejemplares | **alta** |
| 2 | `GEN-NIVEL` | SET_01 | nivel dinámico con visibilidades Corte/Vista/Planta + `Block Table` que alinea `NPT` + grip de altura gráfica | **alta** |
| 3 | `A-CARP-PU-088` · `SIMB-NIV-NPT` · `SIMB-LOC-01` · `SIMB-CORTE-01` | SET_02 | los 4 dinámicos del plano de uso municipal | media |
| 4 | `GCBA-CRTL-PLANO_USO` · `GCBA-CRTL-PLANO_UNICO` | SET_02 | carátulas del plano de uso | media |
| 5 | `COC-BM-600` · `COC-PU-BAT` | SET_03 | bajo mesada con stretch + pileta + flip; puerta con lookup 0/45/90 | media |
| 6 | 11 bloques de equipo de cocina | SET_03 | un bloque por equipo (medidos, sin convertir) | baja |
| 7 | visibilidades por escala | SET_01 | `SIMB-REP` → `50` → `100+DETALLE` | baja |
| 8 | `SET_01-REP_bloques.dwg` + paleta `.xtp` | SET_01 | biblioteca madre + paleta compartida por Drive | baja |
| 9 | bloques de disciplina `SAN-` / `ELE-` | genéricos | bibliotecas por disciplina, fuera de la memoria del DWT | baja |
| 10 | agrupar / purgar anónimos | SET_01 / SET_03 | 312 anónimos `*D` / `*U` → bloques con nombre o purga | baja |

> **Pregunta para Emilia:** ¿el orden 1 → 2 → 3 es el que conviene, o el DWT del SET_01 ya está completo como está y el foco pasa a SET_02 (trámite municipal)?

---

## 6. Qué se actualizó en el vault (21/10)

| Documento | Qué cambió |
|---|---|
| `dashboard-autocad.html` | reescrito: 12 secciones con el estado real (LT 2027, v2 del DWG, bloque de locales, extracción en el DWG, bloques pendientes) |
| `playbooks/PB-02-replanteo-desde-0.md` | `vigente-lt-2027`: §3 documenta las 4 vías de cómputo reales en LT; §1 paso 9-10 con el límite del entorno; §1.5 con `SIMB-LOC_ID` y `GEN-NIVEL` |
| `playbooks/PB-01-SET-informe.md` | `vigente-lt-2027`: kit con los 4 LSP, DoD ítems 8/9 al día, ADR-D corregido |
| `wiki/glosario/interno/pbooks/pbk-set01-rep.md` | reescrito: secciones *entorno LT 2027* y *dónde viven los cómputos* |
| `wiki/glosario/software/autocad.md` | nueva sección **AutoCAD LT 2027 — qué cambia** |
| `wiki/glosario/software/mcp-autocad.md` | marcado en pausa (sin COM en LT) + vía sustituta (MCP oficial de Autodesk) |
| `log.md` | entrada del 21/10 |

**Lo que sigue pendiente de `s`:** PDFs de PB-01 y PB-02 para Drive `W03-CAD/SET_01-REP/` · regenerar el DWT con `SIMB-LOC_ID` · `SET-REPLANTEO` (el LSP que crea las 29 capas) · probar el MCP oficial de Autodesk en LT.

---

## 7. Checklist de la sesión

### En el CAD (el estudio opera)
- [ ] `APPLOAD` del LSP y aviso de ruta no confiable
- [ ] `SIMB-LOC_ID` con 2 locales de prueba
- [ ] `LOC-ID-CHECK` y `LOC-ID-DIAG`
- [ ] deshacer la prueba
- [ ] `CUADRO-NIVELES` (dibujar + `-ACT` + `-VAL`)
- [ ] comprobar la lámina horizontal (viewport `1EC35`)

### Decisiones del estudio
- [ ] 3 preguntas de la §4 respondidas
- [ ] orden de creación de bloques (§5)
- [ ] ¿el `SIMB-LOC_ID` se inserta en REP-ARAOZ o queda para el próximo plano?
- [ ] ¿se prueba el MCP oficial de Autodesk en LT?
- [ ] **Mes 2 — la arista urbana:** ¿el recorte de trabajo es la **plaza** (1:500), el **barrio** (1:1000) o la **ciudad** (1:5000)? → abre el `SET_04-URB` (propuesta en §9)

### Cierre
- [ ] actualización de `cuadro-locales.*` y `orden-locales.*` conservando los números a mano
- [ ] PDFs de PB-01 / PB-02 al Drive
- [ ] entrada de bitácora en `03-log-mvp_02.md`

---

## 8. Lo que el Mes 1 dejó demostrado

> Mover muros y que los cómputos salgan solos, con o sin BIM. El SET deja el plano a un paso de BIM trabajando 100% en AutoCAD.

| Frente | Antes | Ahora |
|---|---|---|
| Sistema de referencia | 7,5 h por plano manual | ~1,5 h con el SET |
| Cómputos | a mano, con errores de tipeo | atributos del bloque + tabla (en el DWG o en CSV) |
| Norma | criterio del arquitecto | DWS que AutoCAD hace cumplir sola |
| Bloques | líneas sueltas | 13 en el DWT + atributos, sin explotar nunca |
| Conocimiento | en la cabeza de cada uno | 4 LSP + 4 scripts + wiki, documentados |

**Eficiencia = mitad de tiempo = doble.** Ahorro logueado 12–15 h por plano; payback en el primer plano.

---

## 9. Mes 2 — la arista que se propone

> Propuesta completa: [[proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano|08-propuesta-mes2-cad-urbano]] · Dashboard §10.

**La idea:** el mismo sistema de SET_01 (capas, DWT/DWS, LISP, bloques con atributos, cómputos) aplicado a la **escala urbana**, sobre el **plano 2D de Barcelona** del concurso, y encadenado con **Rhino** (MCP ya instalado) y **ComfyUI** (LoRA ya analizado): **CAD → Rhino → ComfyUI → lámina A1**.

**Lo medido hoy** (ODA → DXF → ezdxf, DWG intacto): 96 capas · 162.396 entidades (120× el replanteo) · 46 bloques · 40,4 × 38,7 km de extensión · `$INSUNITS` 6 (m). 0 de las 22 capas del SET_01 → la taxonomía urbana es thematic, no de dibujo. Reporte: `raw/reports/barcelona-2d.audit.md`.

**Lo que el SET_04 aporta:** ~26 capas propias (`URB-` base · `PRO-` propuesta · `REF-` fondo) · `SET_04-URB.dwt` + `SET-URB.dws` con el generador que ya existe · 4 LISP derivados de los que ya funcionan (`SET-URB`, `RESUMEN-URB`, `VISTAS-URB`, `PLAZA-PLACA`) · 38 bloques heredados renombrados + 6 de la propuesta (incluido `PRO-MOBILIARIO`, que es a la vez el objeto del **premio especial** del concurso y la pieza que entra al cuadro urbano).

**La decisión que abre todo:** el **recorte de trabajo** — plaza (1:500) · barrio (1:1000) · ciudad (1:5000).
