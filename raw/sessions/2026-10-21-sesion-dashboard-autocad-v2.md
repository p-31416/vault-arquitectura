---
tipo: sesion
proyecto: estudio-pi
mvp: 02
set: SET_01-REP
software: [autocad, autocad-lt, autolisp, oda, ezdxf]
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [sesion, mvp_02, dashboard, autocad, rep-araoz, playbooks, bloques]
---

# Sesión 2026-10-21 — Dashboard AutoCAD v2: REP-ARAOZ, playbooks y bloques que faltan

## 1. Qué se hizo

1. **Reescritura del dashboard AutoCAD** (`proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html`): de 149 a ~290 líneas de contenido. El dashboard del 16/10 quedó congelado en el estado previo a las sesiones del 20/10 (entorno LT, bloque de locales, extracción dentro del DWG).
2. **Secciones nuevas**: `0b` entorno real (AutoCAD LT 2027 y qué cambia por versión) · `1` medición v2 del DWG (13/10 vs 20/10) · `2` bloque `SIMB-LOC_ID` con sus 3 aprendizajes de LISP · `3` extracción dentro del DWG (niveles + cuadro de locales) · `4` estado real de los playbooks + deriva detectada · `5` catálogo de bloques **y los que faltan crear** (11 ítems) · `6` 5 LSP + 4 scripts · `10` pendientes separados en "en el CAD" / "en el vault".
3. **Correcciones sobre el estado real**: el pipe a Google Sheet por n8n queda marcado como *en pausa* (decisión 20/10) y no como activo; `DATAEXTRACTION` / `ATTIN` / `ATTOUT` se documentan como inexistentes en LT; el MCP `autocad` (COM) como inutilizable mientras la máquina tenga LT.
4. **Navegación**: el nav pasa de 1 link a 12 anclas de sección + links a los otros 4 dashboards (Mes 1 · Comfy · Estudio OS · Vault) + links `obsidian://` a los documentos fuente.
5. **DoD de SET_01**: se documentan las dos lecturas (PB-01 §3 = 7 cumple / 2 parcial / 1 diferido; auditoría del 16/10 = 6/3/1) y la diferencia queda explicada en el ítem 3 (CTB).
6. **Vía descartada por decisión del estudio (21/10):** el LSP de cuadro de locales (`CUADRO-LOCALES`) no era el camino → se elimina del dashboard (sección 3, tabla de LSP y lista de pendientes) y la planilla de locales queda como CSV en el vault.
7. **Playbooks y wiki actualizados** (con `s` del estudio): PB-01 y PB-02 pasan a `vigente-lt-2027`; `pbk-set01-rep` reescrito con *entorno LT 2027* y *dónde viven los cómputos*; `wiki/glosario/software/autocad.md` gana la sección **AutoCAD LT 2027 — qué cambia**; `wiki/glosario/software/mcp-autocad.md` queda marcado en pausa con la vía sustituta (MCP oficial de Autodesk 2027). Entrada nueva en el `log.md` raíz.
8. **Documento de revisión para el 22/10**: `proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md` — agenda de 30-40 min, cifras ancla y de dónde sale cada una, las 12 secciones del dashboard con su mensaje en una línea, la prueba en vivo en el CAD (bloque de locales, tabla de niveles, lámina horizontal), las 3 preguntas abiertas, los 10 bloques a crear con prioridad, qué se actualizó en el vault y el checklist de la sesión.
9. **Propuesta del Mes 2 (nuevo, a pedido del estudio)**: llevar el sistema de SET_01 a la **escala urbana** sobre el **plano 2D de Barcelona** del concurso, encadenado con **Rhino** (MCP ya instalado) y **ComfyUI** (LoRA ya analizado) → **CAD → Rhino → ComfyUI → lámina A1**.
   - **Medición real del 2D** (ODA → DXF → ezdxf 1.4.4, DWG intacto): **96 capas · 162.396 entidades · 46 bloques · 1.344 INSERTs · 40,4 × 38,7 km de extensión** · `$INSUNITS` 6 (m) con `$MEASUREMENT` 0 (imperial) · 0 de las 22 capas del SET_01 → la taxonomía es temática y funcional (catalán, por Districte 1-10), no de dibujo. Reporte: `raw/reports/barcelona-2d.audit.md` (+ `.json`).
   - **Propuesta `SET_04-URB`**: ~26 capas propias (`URB-` base heredada · `PRO-` propuesta · `REF-` fondo no imprimible, la cartografía entra como xref) · `SET_04-URB.dwt` + `SET-URB.dws` reutilizando `scripts/genera-template-set01.py` · 4 LISP derivados de los que ya funcionan (`SET-URB` capas, `RESUMEN-URB` cuadro urbano, `VISTAS-URB` ventanas por escala, `PLAZA-PLACA` recorte de la plaza) · 38 bloques heredados renombrados con prefijo + 6 de la propuesta, con `PRO-MOBILIARIO` (atributos MATERIAL/CANT/COSTO) como pieza que es a la vez el objeto del premio especial del concurso y la entrada al cuadro urbano.
   - **Análisis de visualización urbana con ComfyUI**: la escala urbana es un problema de **control de líneas**, no de LoRA → planos ilustrados con **SDXL + ControlNet** (canny/depth/scribble sobre el DXF exportado a PNG) y volumetrías/vistas aéreas con **FLUX.2 klein 9B + LoRA `rhino-to-image`** (capturar → arcilla → hiperreal); FLUX.2 klein **no tiene ControlNet nativo** (solo `ReferenceLatent`). La vista aérea sale de la geometría en Rhino con cámara alta + materialidad del LoRA.
   - **Documentos**: `proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano.md` (propuesta completa) + **§10 del dashboard** (versión ejecutiva) + §9 del doc de revisión del 22/10.
10. **Bug corregido en `scripts/audita-dwg.py`**: `doc.blocks.names()` ya no existe en ezdxf 1.4.4 → `doc.blocks.block_names()` con fallback. El script no corría con ningún DWG desde la actualización de ezdxf.

## 2. Archivos modificados

| Archivo | Qué |
|---|---|
| `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html` | reescrito con el estado real al 21/10 (mismo sistema visual) + §10 propuesta Mes 2 |
| `proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md` | nuevo — documento de revisión para mañana |
| `proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano.md` | nuevo — propuesta del Mes 2 (escala urbana, SET_04-URB, cadena Rhino + ComfyUI) |
| `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-01-SET-informe.md` | `vigente-lt-2027`: kit con 4 LSP, DoD 8/9 al día, ADR-D corregido |
| `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-02-replanteo-desde-0.md` | `vigente-lt-2027`: §3 con las 4 vías de cómputo reales, §1 pasos 9-10 con límites del entorno, §1.5 con `SIMB-LOC_ID` y `GEN-NIVEL` |
| `wiki/glosario/interno/pbooks/pbk-set01-rep.md` | reescrito: entorno LT 2027 + dónde viven los cómputos |
| `wiki/glosario/software/autocad.md` | nueva sección **AutoCAD LT 2027 — qué cambia** + MCP `autocad` en pausa |
| `wiki/glosario/software/mcp-autocad.md` | en pausa por entorno + vía sustituta + corrección de un carácter corrupto |
| `scripts/audita-dwg.py` | fix de compatibilidad con ezdxf 1.4.4 (`block_names()`) |
| `raw/reports/barcelona-2d.audit.md` + `.json` | medición del plano 2D de Barcelona |
| `log.md` | entrada del 21/10 |
| `raw/sessions/2026-10-21-sesion-dashboard-autocad-v2.md` | esta sesión |

## 3. Cerebro digital

**Topics:** dashboard-reportable-v2 · entorno-por-versión (Full vs LT 2027) · COM no disponible en LT · DATAEXTRACTION inexistente en LT · DATALINK exige Excel · extracción dentro del DWG (decisión 20/10) · bloque de locales con atributos visible/invisible · plan B `-BLOCK` cuando `entmake` de bloque no se registra · `entdel` no libera el nombre de bloque · compensación de twist = (−twist) mod 360 · DoD SET_01 en dos lecturas.

**Entidades:** `dashboard-autocad.html` · `REP-ARAOZ.dwg` v2 · `SIMB-LOC_ID` · `N_LOC` / `TXT_LOC` · `SET-01-SIMB-LOC-ID.lsp` v2.2 · `SET-01-CUADRO-NIVELES.lsp` v4 · `SET-01-HORIZ.lsp` · `SET-01-NORM-TEXTOS.lsp` · `CUADRO-LOCALES` (a crear) · `SET_01-REP.dwt` / `SET-REP.dws` · PB-01 / PB-02 · `pbk-set01-rep` · `GEN-NIVEL` · `A-CARP-PU-088` · `COC-BM-600` · `COC-PU-BAT` · viewport `1EC35` · layout `REP-PTipo-A1-H`.

**Hechos (verificados contra fuentes del vault):**
- El DWG del 20/10 tiene **2 layouts** (se eliminó `REP-PTipo-A1`), viewport `1EC35` con **twist 360°**, 50 capas, 14 bloques nombrados, 312 anónimos, 203 INSERTs, 273 cotas.
- Los **28 rótulos** numerados a mano siguen el orden de lectura en **0 de 28** casos → dato informativo, no se corrige.
- El bloque `SIMB-LOC_ID` tiene **0 ejemplares** en el DWG: los locales numerados siguen siendo los rótulos legacy `*U482`.
- `CUADRO-NIVELES` (v4) **lee el CSV** y dibuja la tabla (MTEXT + LINE) en la capa `A-CUADRO-NIVELES`; la alternativa nativa (`-TABLE` + vínculo `niveles`) exige Excel instalado, que no está en la máquina.
- AutoCAD LT 2027 **sí** tiene `APPLOAD`, `TABLA` y `STANDARDS`; **no** tiene `DATAEXTRACTION`, `ATTIN`, `ATTOUT` ni COM externo.
- El MCP oficial de Autodesk 2027 (`AutoCAD-MCP-Server-2027.bundle`) soporta `ACADLT`: `NETLOAD acmcp.dll` + `MCPHTTPSTART` → `localhost:5001/mcp` — **todavía sin probar en LT**.
- Los scripts de CAD corren con **Python 3.12 del sistema** (donde vive `ezdxf` 1.4.4), no con `comfyenv`.

## 4. Pendientes

### En el CAD (lo corre el estudio)
- [ ] Insertar los 28 ejemplares de `SIMB-LOC_ID` (`SIMB-LOC_ID` → `LOC-ID-CHECK`) y verificar fuera del CAD con `ordena-locales.py --check`.
- [ ] Probar el LSP en LT con 2 locales de prueba → deshacer.
- [ ] Decidir qué se hace con el local de prueba de la primera corrida.
- [ ] Probar el MCP oficial de Autodesk en LT.

### En el vault (aprobado por el estudio el 21/10 — hecho)
- [x] Actualizar PB-01 y PB-02 (LT 2027 vigente · sin `DATAEXTRACTION` · sin pipe a Sheet) y `pbk-set01-rep`.
- [x] Actualizar `wiki/glosario/software/autocad.md` y `wiki/glosario/software/mcp-autocad.md` (COM en pausa con LT).
- [x] Entrada en el `log.md` raíz.
- [x] Documento de revisión para el 22/10 en `/presentacion`.

### En el vault (siguen pendientes)
- [ ] PDFs de PB-01 y PB-02 para Drive `W03-CAD/SET_01-REP/`.
- [ ] Crear `GEN-NIVEL` y regenerar el DWT con los bloques nuevos (13 + `SIMB-LOC_ID`).
- [ ] `SET-REPLANTEO` (el LSP que crea las 29 capas).
- [ ] Regenerar `cuadro-locales.*` y `orden-locales.*` conservando los números a mano (`--conservar-numeros`).
- [ ] Entrada de bitácora en `03-log-mvp_02.md` con el resultado de la sesión del 22/10.
- [ ] **Mes 2:** crear `proyectos/MVP_02-autocad-standards/SET_04-URB_Urbano/` con el spec del SET urbano (capas `URB-`/`PRO-`/`REF-`, DWT/DWS, 4 LISP, bloques) a partir de `08-propuesta-mes2-cad-urbano.md`.
- [ ] **Mes 2:** tabla de mapeo de las 96 capas catalanas → taxonomía `URB-*` (con `scripts/audita-dwg.py`, ya arreglado y funcionando).

## 5. DÓNDE QUEDAMOS

El dashboard AutoCAD ya refleja el estado real del 21/10: entorno LT, medición v2, bloque de locales, extracción en el DWG, estado de los playbooks y la lista de bloques que faltan. Los playbooks y la wiki ya están alineados con la máquina (LT 2027) y hay un documento de revisión para el 22/10.

**Lo que se descartó por decisión del estudio (21/10):** la idea de dibujar el cuadro de locales con un LSP (`CUADRO-LOCALES`). No era la vía → la planilla de locales vive como CSV en el vault y la fuente en el DWG son los 28 rótulos numerados a mano.

**La arista del Mes 2 quedó propuesta y medida:** el mismo sistema de SET_01 llevado a la escala urbana sobre el `Barcelona-2D.dwg` (96 capas · 162.396 entidades · 40 km · 120× el replanteo), encadenado con Rhino (MCP ya instalado) y ComfyUI (LoRA ya analizado) → **CAD → Rhino → ComfyUI → lámina A1 del Gaudí Nexus (16/12)**. Falta la decisión de arranque: **el recorte de trabajo (plaza 1:500 / barrio 1:1000 / ciudad 1:5000)**.

**El siguiente bloque de trabajo es `GEN-NIVEL`** (nivel dinámico con visibilidades Corte/Vista/Planta) y, en paralelo, insertar los 28 ejemplares de `SIMB-LOC_ID` en REP-ARAOZ.

**Para retomar mañana (22/10):** abrir `proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md` — es el guion de la revisión (cifras ancla, prueba en vivo en el CAD, 3 preguntas abiertas, bloques a crear, checklist).
