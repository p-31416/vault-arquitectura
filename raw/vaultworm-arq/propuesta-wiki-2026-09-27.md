---
tipo: propuesta
fecha: 2026-09-27
zona: -03:00 America/Argentina/Buenos_Aires
proyecto: MVP_02-autocad-standards
fuentes:
  - raw/vaultworm-arq/analysis-MVP_02-doc-maestro-2026-09-27 1.md
  - raw/vaultworm-arq/digest-2026-09-27-mvp_02-fuentes.md
  - raw/sessions/2026-09-27-mvp_02-fuentes.md
estado: propuesta — NO crear en wiki sin `s` de SOL
---

# Propuesta wiki MVP_02 — consolidada 2026-09-27

> Cruce sin duplicados de las 3 fuentes. Respeta reglas de calidad [[wiki/glosario/00-index|glosario/00-index]]: UNICO `.md` por tool (las propuestas `autocad-*` van como secciones `##` en `autocad.md` existente, no como archivos nuevos).

## 1. Entradas wiki propuestas

| # | Destino | Contenido | Fuente | Prioridad |
|---|---------|-----------|--------|-----------|
| 1 | `software/autocad.md` §§ SET-REP/ARQ/EST/ELE/SAN/FAB | Capas por SET (nombres, colores, usos); base del n_01 | Session §3 + Digest | Alta |
| 2 | `interno/standares/tecnico/capas-layers.md` (actualizar) | Prefix system G-/R-/A-/S-/E-/P-/F- como identidad del estándar | Digest + Session §2 | Alta |
| 3 | `interno/standares/tecnico/plot-styles.md` (actualizar) | Monochrome plot + pesos ISO 128-2 (0.13–2 mm) y justificación | Session §§4,7 + Digest | Alta |
| 4 | `interno/standares/tecnico/bloques.md` (actualizar) | Bloques dinámicos + atributos y DATAEXTRACTION→CSV | Analysis + Digest | Alta |
| 5 | `conceptos/kit-estudio-pi.md` (nueva) | Kit DWT+DWS+biblioteca como estándar central del estudio | Analysis §Propuestas | Alta |
| 6 | `conceptos/dwt-dws-standard.md` (nueva) | Flujo DWS + CHECKSTANDARDS + LAYTRANS + Batch Checker | Session §8 + Digest | Alta |
| 7 | `software/autocad.md` § MCP AutoCAD | Servers puran-water/limuzi013, BarryMcAdams, Product Help; funciones y seguridad | Analysis + Session §6 | Media |
| 8 | `conceptos/iso-13567.md` + `conceptos/ncs-standard.md` (nuevas) | Nomenclatura de capas ISO + National CAD Standard USA; tabla equivalencias Studio Pi↔NCS↔ISO↔AEC UK | Session §5 + Digest | Media |
| 9 | `software/autocad.md` § Annotative | Scaling anotativo y dimensionado por viewport | Session §12 (9) | Media |
| 10 | `conceptos/niveles-mvp_02.md` (nueva) | Temario M0–M8 sintetizado (manifiesto + doc maestro + roadmap) | Analysis §Temario | Media |
| 11 | `software/ezdxf.md` (nueva) | Generación DXF sin AutoCAD vía Python | Analysis §Topics | Media |
| 12 | `interno/pbooks/pbk-mvp_02.md` (nueva) | Ecosistema cursos C1–C4+IA, ACP alignment 22/20/29/16/13 %, guía MCP del estudio | Session §§7,13–14 + Digest | Baja |
| 13 | `conceptos/acp-autocad.md` (nueva) | Marco Autodesk Certified Professional y tracking | Analysis + Session §7 | Baja |
| 14 | `software/autocad.md` §§ 3D + Assistant 2027 | Comandos 3D (3DORBIT, PRESSPULL…) y verificación IA de estándares | Session §1 + Analysis | Baja |

## 2. Entidades para referentes

| Entidad | Destino | Por qué | Prioridad |
|---------|---------|---------|-----------|
| CAPBA Distrito 1 | `referentes/capba.md` | Guía base de planos municipales; URL verificada | Alta |
| GCBA | `referentes/gcba.md` | Template y carátula reglamentaria CABA; URL verificada | Alta |
| AEA (Asociación Electrotécnica Argentina) | `referentes/aea.md` | Reglamentación eléctrica 90364; URL verificada. ⚠️ Session dice "Escritores" — corregir | Alta |
| AySA | `referentes/aysa.md` | Planos sanitarios CABA; URL verificada. ⚠️ Session trae `ayesa.com.ar` (typo) — usar `aysa.com.ar` | Alta |
| IRAM | `referentes/iram.md` | Certificación argentina citada en SETs | Media |
| Autodesk | `entidades/autodesk.md` | Creador AutoCAD, fuente oficial de comandos | Media |
| puran-water / limuzi013 | `referentes/puran-water.md` | Creador autocad-mcp (OSS) | Media |
| ISO (13567, 19650) | Verificar `conceptos/bim-metodologia.md` antes de duplicar (19650 ya existe ahí) | Media |
| Vicente López / Zárate | `referentes/` solo si SOL confirma valor como modelos de plano municipal | Baja |
| Javi Lapina, Fernando Montaño, arqMANES, ModelPro, CAD Intentions, Civil Survey | `referentes/` solo con ≥1 fuente verificada (hoy sin verificar) | Baja |

## 3. Conceptos transversales

| Término | Destino propuesto | Nota |
|---------|-------------------|------|
| monochrome (plot sin CTB) | `interno/standares/tecnico/plot-styles.md` § | Decisión filosófica + técnica ya tomada |
| CTB / STB | Mismo destino | Tono de voz del impreso |
| annotative | `software/autocad.md` § Annotative | Scaling por viewport |
| prefix system (A-/E-/DR-/REP-) | `interno/standares/tecnico/capas-layers.md` § | Identidad del estándar |
| ISO 128-2 weights | `interno/standares/tecnico/plot-styles.md` § | Justificación física de pluma |
| DWS / CHECKSTANDARDS / LAYTRANS | `conceptos/dwt-dws-standard.md` | Flujo de verificación |
| DATAEXTRACTION | `interno/standares/tecnico/bloques.md` § | Computabilidad de bloques |
| Equivalencias NCS↔ISO↔AEC UK | `conceptos/iso-13567.md` + tabla visual | Traducción internacional |
| ACP % (22/20/29/16/13) | `interno/pbooks/pbk-mvp_02.md` | Tracking, no estándar |
| DoD | Sin respaldo en las 3 fuentes — no proponer hasta que aparezca en specs | Descartado por ahora |

## 4. Lo que NO va a wiki

| Descartado | Por qué |
|------------|---------|
| Precios de licencias | Efímero, cambia por trimestre |
| Plan de 15 días | Logística de curso, no estándar |
| Configuración clientes MCP (Claude/Codex/OpenCode) | Setup operativo, no conocimiento permanente |
| Comparativa de clientes IA | Infra de herramienta, se desactualiza |
| Sección "Situación actual" del doc maestro | Contexto puntual, no reutilizable |
| Ecosistema de cursos como negocio | Vehículo comercial, fuera del scope MVP_02 |
| Fusion / Revit como entradas nuevas | Alcance futuro (BIM/3D); Revit ya tiene `.md` |
| `Estudio-Pi` como entidad | El estudio es el autor del vault, no una entrada; queda como pregunta para SOL |
| URLs sin auditar (40 fuentes) | Pasar auditoría 404 de @sherlock antes de citar en `## Referencias` |

> Preguntas para SOL: ¿Kit Estudio Pi como estándar central o artefacto? ¿Doc maestro = MVP_02 o MVP_03? ¿12 entradas o agrupar en 4–5? ¿`s` para crear las 5 de prioridad Alta?
