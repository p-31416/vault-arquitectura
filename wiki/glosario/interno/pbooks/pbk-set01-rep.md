---
tipo: playbook
codigo: pbk-set01-rep
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-21
tags: [pbook, set01, replanteo, autocad, dwt, dws, bloques, computos, emilia, autocad-lt]
idioma: es
---

# pbk-set01-rep — Plano de replanteo con SET_01 (puerta única)

> Documento único elevado desde `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/` (documento único + PB-02 + guía JR). Puerta de entrada: qué es, kit, instalación 15', dibujo principio-fin, verificación y cómputos. Detalle medido en proyecto, refs oficiales exactas en PB-02.
> **Actualizado 21/10/2026** — la máquina del estudio tiene **AutoCAD LT 2027** (no el Full). Ver §5.

## 1. Puerta única (orden de lectura)

1. [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/SET_01-REP_completo|SET_01-REP_completo]] — qué es, capas, bloques, estilos, kit, instructivo 15', horas.
2. [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-02-replanteo-desde-0|PB-02-replanteo-desde-0]] — dibujar desde cero, tabla EN/ES con **refs oficiales exactas por comando** (UNITS, LAYER, DIMSTYLE, BLOCK/ATTDEF, BATTMAN/ATTSYNC, DATAEXTRACTION...).
3. [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/guia-jr-replanteo|guia-jr-replanteo]] — versión junior.
4. [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques|REP-ARAOZ-capas-bloques]] — medición madre (49 capas, 13 bloques, 208 INSERTs, ventana paso a paso).
5. [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro-carpinterias]] — cómputos + pipe a Sheet.

## 2. Archivos duros (fuera de git, con el kit)

| Archivo | Ruta hoy | Migra a Drive cuando |
|---|---|---|
| `SET_01-REP.dwt` | `activos/proyectos/mvp_02-autocad-standards/SET_01-REP/` | Definido el SET → `G:\Mi unidad\OS-Emilia\W03-CAD\SET_01-REP\` |
| `SET-REP.dws` | misma carpeta | idem |
| CTB `EP-ISO` | se crea en destino (tabla §5 doc único) | con el kit |
| Planilla cuadro | CSV en el vault (`SET_01-REP_Replanteo/docs/`) | ya vive ahí |
| Lisp SET_01 | **existen 4 LSP** (`HORIZ`, `SIMB-LOC-ID`, `NORM-TEXTOS`, `CUADRO-NIVELES`) | ya está |

## 3. Refs oficiales exactas

Viven en la tabla de PB-02 §0 (una por comando, verificadas): UNITS/DWGUNITS, SCALELISTEDIT, LAYER, STYLE, DIMSTYLE, BLOCK+ATTDEF, BATTMAN/ATTSYNC, BEDIT/FIELD, y BOM vía ATTDEF + DATAEXTRACTION ([artículo oficial BOM](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Creating-a-Bill-of-Materials-BOM-in-AutoCAD-and-AutoCAD-LT.html)). Para temas nuevos: [[wiki/glosario/software/autocad|autocad]] + MCP Autodesk Help.

## 4. Prueba DWS en vivo (5 min, LT vale)

`STANDARDS` → asociar `SET-REP.dws` → `CHECKSTANDARDS` → corregir 1 capa → re-chequear. Fallback: AutoCAD de Emilia.

## 5. El entorno: AutoCAD LT 2027 (vigente, 21/10)

La instalación real es `C:\Program Files\Autodesk\AutoCAD LT 2027`. El AutoCAD 2027 full ya no está instalado (el instalador queda en `P:\autocad\AutoCAD.2027_English_64bit`). Consecuencias operativeas:

| Capacidad | En LT 2027 | Efecto en el SET_01 |
|---|---|---|
| COM / ActiveX externo | no | el MCP `autocad` del vault no llega → el control del CAD va por AutoLISP |
| `DATAEXTRACTION` / `ATTIN` / `ATTOUT` | no (*Unknown command*) | el cómputo sale por LSP: `SET-01-CUADRO-NIVELES` dibuja la tabla dentro del DWG; alternativa oficial en LT: `ATTEXT` + `LIST` |
| `TABLA` + vínculo de datos | sí, pero exige Excel instalado | sin Excel el preview queda vacío → el LSP lee el CSV y dibuja |
| `APPLOAD` (AutoLISP) | sí (desde 2024 en Windows) | los 4 LSP del SET_01 se cargan; con `SECURELOAD = 1` hay que confirmar la ruta |
| MCP oficial de Autodesk 2027 | sí (bundle `AutoCAD-MCP-Server-2027.bundle`, soporta `ACADLT`) | `NETLOAD acmcp.dll` + `MCPCONFIG` + `MCPHTTPSTART` → `localhost:5001/mcp` — pendiente de probar |
| Palettes / DesignCenter / Blocks | sí | el `.xtp` de SET_01 es viable |

## 6. Cómputos: dónde viven (decisión 20/10)

- **Nada de Google Sheets ni n8n** en el circuito: la extracción se hace desde el DWG.
- **Locales (28):** numerados a mano sobre los rótulos legacy `*U482` → planilla en [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-locales|planilla-locales]] (CSV + MD). El bloque nuevo `SIMB-LOC_ID` (`N_LOC` visible + `TXT_LOC` invisible) está creado y probado, con **0 ejemplares** insertados: su uso queda para el próximo plano rotulado.
- **Niveles (14 filas × 3 columnas):** [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-niveles|planilla-niveles]] → tabla dibujada dentro del DWG con `CUADRO-NIVELES` (capa `A-CUADRO-NIVELES`).
- **Carpinterías (42):** [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro-carpinterias]] (CSV). El pipe a Sheet por n8n queda en pausa.

## 7. Minutos (cronometrados Sol, a medir 1 real)

Ventana 1 min ×20 = 20 min · puerta 45 s ×22 = 16.5 min · muros ~1.5hs · columnas 26 min · cotas 304 (~5hs, 2.5hs aceitado). Total ~7.5hs (5hs aceitado) → sistema: mover muros y cómputos solos (camino BIM).
