# 2026-10-30 — Sesión earth2rhino: massing Sagrada en Rhino + CADMapper + fotos plaza

## Qué se hizo

- **Fase A**: transcripción 2 videos YT (`transcribir_youtube.py`): video 01 demo visual 1 cue (whisper local confirmó 0 voz), video 02 Heron completo 80 líneas. Trazabilidad `generado_por` agregada a `.md` + `.origen.json` + parche permanente del script.
- **Fase B** en `proyectos/concurso-gaudi-nexus/earth2rhino3d/`: 2 fichas + `comparativa-metodos.md` + `00-index.md`.
- **@sherlock**: licencias Google (4 cláusulas que prohíben derivado) + 7 alternativas open → `raw/research/2026-10-29-earth2rhino-open-alternativas.md`.
- **Fase C massing**: base OSM Overpass (1054 ways, 474 con levels, bbox 600 m templo 41.4036/2.1744 — se corrigió bbox que apuntaba 1,7 km al sur) → `scripts/construir-massing-sagrada-rhino.py` (plano sin `def`, `System.Guid.Empty`, extrusión +Z) → 1045 sólidos + testigo 172,5 m + cruz origen. Verificado por MCP (bbox, top, iso).
- **Alturas auditadas** (`auditar-alturas-osm.py`): 34,1 = levels 11, 37,2 = levels 12 (Edifici Califòrnia); 580 sin levels → default 21 m. Comparación CADMapper: mayoría coincide a 1 m (offset sistemático −1), minoría discrepa (sub-piezas).
- **CADMapper**: `cadmapper-barcelona-catalonia-es.3dm` (4 MB, ciudad completa 5599 obj) importado, licencia ODbL + dominio público (gap cerrado), alineado templo-con-templo, cota cero por objeto. Capturas overlay top + 2 iso.
- **Fotos Commons**: 10 CC BY-SA (7 plaza + 3 basílica) en `ref/` + thumbs + `fotos-plaza-commons.md` con atribución para rótulo.
- **Bitácora end-to-end**: `bitacora-massing-v01.md` (§1b con links OSM revisables a mano).

## Archivos (nuevos con `+`, modificados con `~`)

+ `earth2rhino3d/{00-index,comparativa-metodos,ficha-video-01,02,plan-implementacion-rhino,bitacora-massing-v01,fotos-plaza-commons,comandos-rhino-copiar}.md`
+ `scripts/{descargar-osm-sagrada,construir-massing-sagrada-rhino,auditar-alturas-osm,commons-sagrada,descargar-commons-sagrada,commons-plaza,descargar-plaza,commons-plaza2,descargar-plaza2,generar-thumbs-ref,importar-cadmapper-comparar-rhino,auditar-cadmapper-rhino,alinear-comparar-cadmapper-rhino,comparar-altos-osm-cm-rhino,apoyar-cota-cero-rhino,apoyar-objetos-cota-cero-rhino}.py` (+ 2 `_notas.md`)
+ `activos/.../earth2rhino3d/{base/sagrada_overpass.json, base/cadmapper/, ref/ (10 fotos), ref/thumbs/ (10), salidas/ (5 png)}`
~ `scripts/00-index.md` · `scripts/transcribir_youtube.py` (generado_por permanente) · `earth2rhino3d/{00-index,plan-implementacion-rhino}.md` · `bitacora-massing-v01.md`
~ `raw/research/00-index.md` (fila sherlock)

## Pendiente próxima sesión

1. Función Hermes `earth2rhino-massing` location-agnóstica (generalizar scripts con `--lat --lon --radio` + `meta.json`, ficha formato SKILL).
2. Refino alturas con Catastro donde OSM/CM discrepen > 3 m.
3. Guardar `mcp-plaza.3dm` final con todo adentro (el usuario guarda; scripts no guardan).
4. Composite plaza: foto Commons + captura iso + propuesta → WF-03 `rhino-to-image`.

## Análisis cerebro-digital

**Topics:** earth2rhino · massing-osm · cadmapper-overlay · rhino-mcp-bridge · overpass · commons-cc-by-sa · cota-cero · google-tos-eea-block · wf03-rhino-to-image
**Entidades:** `mcp-plaza.3dm` (43 MB, G:\) · `cadmapper-barcelona-catalonia-es.3dm` (4 MB) · `SF-MASSING-OSM` (1045) · `SF-MASSING-CADMAPPER` (5599) · `TESTIGO-SF` (172,5 m) · bbox templo 41.4036/2.1744 · Txllxt TxllxT + MB-one (Commons) · Brian Washburn/Heron
**Hechos:** Google 3D Tiles bloqueado EEA + ToS prohíbe derivado → vía open OSM+ICGC+Catastro; levels×3,1 validado vs CADMapper (±1 m); puente MCP no tolera `def`/Guid/offset-por-cara (3 fixes documentados); scripts Rhino nunca guardan (el arquitecto guarda); fotos plaza CC BY-SA listas con atribución.
