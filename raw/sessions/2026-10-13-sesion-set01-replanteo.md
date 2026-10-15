# Sesión 2026-10-13 — SET_01-REP replanteo + kit instalable

## Qué se hizo
- Guía JR `docs/guia-jr-replanteo.md` v1.0 (qué es, contenidos mínimos, cómo leerlo en 6 pasos, cómo dibujarlo en 12 pasos con comandos básicos, 5 reglas madre, glosario, 4 fuentes académicas: FADU-Udelar, FADU-UBA, UNLP, UNAM-FIO).
- SET_01 v2.2-archivo: nombres canónicos = archivo real (29 propias + 20 xref); equivalencia Kit R-/A-/S-/G-.
- `docs/`: madre v0.5 (capas, bloques, estilos, MCA LT, MCP paso a paso, DWT/DWS, playbook 12 pasos, 30 comandos ES/EN, §16 backlog), bloques-personalizados v0.1, desglose-configuraciones v0.1 (87 ítems, 10h+4h=14h, ahorro 12–15h/plano), cuadro-carpinterias + CSV (V01×6/2.30, V02×10/1.10, PV01×4/1.75, P-1×5/0.90, P-2×16/0.80, P-3×1/1.00).
- Pipe `EXTRACDAT→n8n→Sheets` andando (workflow VIQmMEZ9tkDBfKjd, webhook set01-carpinterias, rango cuadro!A1:H100); incidente papelera W03-CAD resuelto (trashed false).
- Kit: `activos/.../SET_01-REP/SET_01-REP.dwt` + `SET-REP.dws` generados con `scripts/genera-template-set01.py` (+notas), verificados ida/vuelta (29 capas, 8 estilos, 3 cotas, INSUNITS 6).
- Documento único `SET_01-REP_completo.md` para presentar mañana + instructivo PC Emilia.
- Método: DWG externo no se toca; ODA→DXF en %TEMP% + ezdxf; wiki intacta.

## Archivos modificados
- `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/{01-spec-SET_01.md,SET_01-REP_completo.md,docs/*}`
- `proyectos/MVP_02-autocad-standards/03-log-mvp_02.md` (2 filas)
- `scripts/{genera-template-set01.py,genera-template-set01_notas.md,00-index.md}`
- `activos/proyectos/mvp_02-autocad-standards/SET_01-REP/{SET_01-REP.dwt,SET-REP.dws}` (gitignored)
- `wiki/glosario/software/mcp-autocad.md` (referencia oficial verificada)

## Análisis cerebro-digital
- Topics: estándares CAD replanteo, bloques dinámicos+atributos, cómputos automáticos, n8n→Sheets, plantillas DWT/DWS, instructivos cross-PC.
- Entidades: REP-ARAOZ.dwg, VENTANA BAJA SIMPLE, EP-2.5/EP-3.5/EP-ISO, ODA 25.12.0, ezdxf 1.4.4, AutoCAD LT 2027 (sin COM), PC Emilia, W03-CAD.
- Hechos: 49 capas/13 bloques/304 cotas medidos; MCP autocad exige AutoCAD completo; pipe reemplaza contenido; horas 14h; backlog: visibilidades, cotas dinámicas, capas instalaciones, playbook aparte, pase wiki (preguntado, sin respuesta — retomar).
