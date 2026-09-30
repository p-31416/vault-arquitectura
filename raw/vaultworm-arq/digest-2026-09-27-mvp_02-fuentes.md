# vaultworm-arq — Digest: 5 Crudos Perplexia MVP_02
> Fecha: 2026-09-27 01:00 AR (-03:00 America/Argentina/Buenos_Aires)
> Fuentes: `raw/docs/` (5 archivos Perplexia) → `raw/sessions/2026-09-27-mvp_02-fuentes.md`
> Tarea: Análisis cruzado de los 5 crudos → proponer entradas wiki y refinamiento de estándares
> **Regla: NO se toca la wiki aún.**

---

## Resumen (5 bullets)

1. **Los 5 crudos forman un sistema completo**: comandos (fuentes oficiales) + documento maestro (plan general) + cursos (ecosistema formativo) + MCP (conexiones de agentes) + SETs (estándares temáticos). Juntos cubren el 100% del alcance MVP_02.
2. **El `Kit temático SETs` es la pieza central**: contiene los 7 SETs completos (GEN, REP, ARQ, EST, ELE, SAN, FAB) con ~60 capas cada uno, equivalencias internacionales, y 40 fuentes verificadas. Es la base para `SET-replanteo-spec.md` existente.
3. **Hay redundancia con el documento maestro**: la sección de comandos del master document se superpone con el crudo de fuentes oficiales; el crudo de SETs ya supera al SET-replanteo-spec.md actual en cobertura (60 capas vs ~60 en DR-* solo).
4. **Los MCP connections (puran-water/limuzi013) son la novedad operativa**: autocad-mcp con funciones commands/layers/blocks/plotstyles/layouts — habilita el "segundo idioma" del manifiesto (IA verificando estándares).
5. **Lo que falta para wiki**: las propuestas de entradas están listas en el raw session (12 items), pero necesitan validación de Sherlock sobre profundidad y jerarquía antes de crear páginas en `wiki/glosario/`.

---

## Topics → destino wiki/propuestas

| Topic | Por qué | Destino propuesto | Prioridad |
|-------|---------|-------------------|-----------|
| SET-REP capas (R-EJES, R-COTP, R-COTA, R-NIVE, R-FUND) | Son el MVP concreto del n_01 | `autocad-set-rep` (glosario) | Alta |
| SET-ARQ capas (A-MURO-N/E/D, A-TABI, A-ABER) | Gramática del dibujo arquitectónico | `autocad-set-arch` (glosario) | Alta |
| SET-EST capas (S-FUND, S-COLU, S-VIGA, S-LOSA) | Estructura como disciplina | `autocad-set-struct` (glosario) | Alta |
| ISO 128-2 weights (0.13-2mm) | Justificación física de pluma | `autocad-plot-styles` (glosario) | Media |
| Prefix system (A-/E-/DR-/REP-/SIMB-) | Identidad del estándar | `autocad-standards-principles` (glosario) | Alta |
| MCP autocad-mcp (puran-water) | Agente que ejecuta comandos | `autocad-mcp-connections` (glosario) | Media |
| ACP alignment (22/20/29/16/13%) | Tracking de certificación | `studio-pi-autocad-eco` (estudio) | Baja |
| Equivalencias NCS↔ISO 13567↔AEC UK | Traducción internacional | `autocad-layer-translator` (glosario) | Media |
| DWS / CHECKSTANDARDS / LAYTRANS | Flujo de verificación | `autocad-drawing-standards-workflow` (glosario) | Media |
| Monochrome plot (sin CTB) | Decisión filosófica + técnica | `autocad-plot-styles` (glosario) | Alta |
| Comandos 3D (3DORBIT, PRESSPULL, EXTRUDE) | C4-3D del ecosistema | `autocad-commands` (glosario/software) | Baja |
| Bloques con attributes (DATAEXTRACTION→CSV) | Computabilidad de bloques | `autocad-blocks-attributes` (glosario) | Media |

---

## Entidades → destino referentes

| Entidad | Tipo | Fuente | Destino |
|---------|------|--------|---------|
| Autodesk | Entidad software | Crudo 1, 2, 3 | `wiki/glosario/entidades/autodesk` |
| CAPBA | Entidad reguladora | Crudo 2, 5 | `wiki/glosario/referentes/capba` |
| GCBA | Entidad municipal | Crudo 2, 3 | `wiki/glosario/referentes/gcba` |
| AEA | Entidad profesional | Crudo 2, 3 | `wiki/glosario/referentes/aea` |
| AySA | Entidad servicios | Crudo 2, 3 | `wiki/glosario/referentes/aysa` |
| ISO 13567 | Estándar internacional | Crudo 5 | `wiki/glosario/conceptos/iso-13567` |
| NCS | Estándar internacional | Crudo 5 | `wiki/glosario/conceptos/ncs-standard` |
| ISO 19650 | Estándar internacional | Crudo 5 | `wiki/glosario/conceptos/iso-19650` |
| IRAM | Entidad certificación | Crudo 5 | `wiki/glosario/referentes/iram` |
| puran-water (limuzi013) | Persona/referente | Crudo 4 | `wiki/glosario/referentes/puran-water` |
| Javi Lapina | Persona/referente | Crudo 5 | `wiki/glosario/referentes/javi-lapina` |
| Fernando Montaño | Persona/referente | Crudo 3 | `wiki/glosario/referentes/fernando-montano` |
| arqMANES | Estudio | Crudo 5 | `wiki/glosario/referentes/argmanes` |
| ModelPro Academy | Entidad formación | Crudo 3 | `wiki/glosario/referentes/modelpro` |
| CAD Intentions | Entidad recursos | Crudo 5 | `wiki/glosario/referentes/cad-intentions` |
| Civil Survey Solutions | Entidad topografía | Crudo 5 | `wiki/glosario/referentes/civil-survey` |

---

## Hechos → mantener vs desechar

### Reutilizables (mantener)
- SET-REP como MVP concreto del n_01 ✅ (ya en SET-replanteo-spec.md)
- Prefix system A-/E-/DR-/REP-/SIMB- ✅ (ya documentado)
- Monochrome plot decision ✅ (ya en PLAN y SET)
- ISO 128-2 weights ✅ (ya documentado)
- MCP autocad-mcp connection ✅ (ya en Guía MCP)
- ACP alignment percentages ✅ (tracking futuro)

### Refinamiento necesario
- SET-ARQ/EST/ELE/SAN/FAB capas necesitan estar en SET-replanteo-spec.md o dividirse en specs separadas
- Las 40 fuentes verificadas necesitan ser auditadas una por una (URL check)
- Los equivalencias internacionales necesitan una tabla visual en wiki

### Desechar / archivar
- Plan de 15 días (futuro, no estándar)
- Precios de licencias (efímero)
- Configuración de clientes (operativo, no estándar)

---

## Propuestas de refinamiento para @sherlock

1. **Completar SET-ARQ, SET-EST, SET-ELE, SET-SAN, SET-FAB**: el crudo tiene las capas pero no tienen el nivel de detalle que tiene SET-REP (comandos, colores, tips, LISP). ¿Se crean specs paralelos o se complementa la existente?
2. **Auditoría de URLs**: de las 40 fuentes, verificar cuántas siguen activas
3. **Generar tabla de equivalencias**: Studio Pi → NCS → ISO 13567 → AEC UK como tabla visual markdown
4. **Mapear comandos a SETs**: qué comando sirve para qué capa/SET (cruzar crudo 1 con crudo 5)
5. **Definir scope de wiki**: ¿12 entradas o agrupadas en 4-5 más grandes?
6. **DWT template**: crear un DWT base que incluya los SET-GEN + SET-REP capas como punto de partida

---

## Fuentes

- Crudo 1: `raw/docs/AutoCAD – Fuentes oficiales y comandos (EN).md`
- Crudo 2: `raw/docs/Estudio Pi – AutoCAD  documento maestro.md`
- Crudo 3: `raw/docs/Estudio Pi – Ecosistema de cursos AutoCAD.md`
- Crudo 4: `raw/docs/Estudio Pi – Guía de conexiones MCP.md`
- Crudo 5: `raw/docs/Estudio Pi – Kit temático  SETs de estándar CAD.md`
- Session: `raw/sessions/2026-09-27-mvp_02-fuentes.md`
