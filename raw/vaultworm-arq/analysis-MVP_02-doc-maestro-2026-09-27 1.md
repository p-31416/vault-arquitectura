# vaultworm-arq — Análisis: Documento Maestro MVP_02
> Fecha: 2026-09-27 00:30 AR (-03:00 America/Argentina/Buenos_Aires)
> Fuentes: `proyectos/MVP_02-autocad-standards/Estudio Pi – AutoCAD  documento maestro.md` + `proyectos/MVP_02-autocad-standards/00-filo-mvp_02.md`
> Tarea: ¿Sirve como base para specs y temario del MVP_02?
> **Regla: NO se toca la wiki aún.**

---

## Resumen (5 bullets)

1. **El documento maestro es un tesoro material** pero opera en un registro completamente distinto al del manifiesto filosófico — es instrumental, mientras el manifiesto es poético/lingüístico.
2. **La estructura temática del documento maestro (14 secciones) es directamente convertible en temario del MVP_02**, pero necesita filtros de scope según el manifiesto.
3. **Hay un contraste filosófico real**: el manifiesto dice "el dibujo es un documento y también un lenguaje" — el documento maestro habla del dibujo como *producto técnico* y *servicio profesional*, no como lenguaje.
4. **Lo que falta para specs**: el documento maestro tiene comandos y flujos, pero no tiene los *lineamientos* que el manifiesto pide — no hay definición de qué es un "layer bien nombrado", qué justifica un peso de pluma, qué hace que un estándar sea "el idioma del estudio".
5. **La mitad de las 14 secciones está fuera de scope del MVP_02** según el manifiesto (licencias, configuración de clientes, plan de 15 días, ecosistema de cursos como negocio).

---

## Topics → destino glosario

| Topic | Por qué | Destino |
|-------|---------|---------|
| Comandos AutoCAD (8 clases, ~90 comandos) | Son el léxico del lenguaje del dibujo | `wiki/glosario/software/autocad` (conceptos por comando) |
| DWT / DWS / estándares DWS | Son el "idioma" que el manifiesto pide documentar | `wiki/estandares/tecnico/` eventualmente |
| Bloques dinámicos (visibilidad, stretch, flip) | Gramática visual — cómo se construyen objetos complejos | `wiki/glosario/conceptos/bloques-dinamicos` |
| ACP (Autodesk Certified Professional) | Marco de referencia externo para el estudio | `wiki/glosario/conceptos/ACP-autocad` |
| Autodesk Assistant 2027 | El "segundo idioma" del dibujo — IA verificando estándares | `wiki/glosario/conceptos/autodesk-assistant` |
| MCP (Model Context Protocol) | Arquitectura de agentes — nuevo paradigma | `wiki/glosario/conceptos/mcp` |
| CTB / plot styles | El "tono de voz" del documento impreso | `wiki/estandares/tecnico/` eventualmente |
| Normativa CABA / CAPBA | El "dialecto" municipal que el dibujo debe hablar | `wiki/glosario/referentes/capba` + `wiki/estandares/tecnico/` |
| AEA 90364-7-771 | Referente normativo eléctrico argentino | `wiki/glosario/referentes/aea` |
| AySA | Referente normativo sanitario | `wiki/glosario/referentes/aysa` |
| ezdxf | Alternativa sin AutoCAD — el dibujo sin el instrumento | `wiki/glosario/software/ezdxf` |
| GCBA (Planos CABA) | Template municipal como caso de estudio | `wiki/estandares/tecnico/` eventualmente |

---

## Entidades identificadas

| Entidad | Tipo | Relevancia MVP_02 |
|---------|------|-------------------|
| Estudio Pi | Estudio/entidad | El estudio que documenta los estándares |
| AutoCAD 2027 | Software/versión | La versión base del MVP_02 |
| AutoCAD 2026 | Software/versión | Versión anterior, referencia de compatibilidad |
| AutoCAD LT | Software/variante | Variante ligera, relevante para cursos |
| ACP | Certificación | Marco de alineación para C2 |
| Autodesk Assistant | Funcionalidad IA | Verificación de estándares en 2027 |
| CAPBA Distrito 1 | Organismo | Guía base de planos municipales |
| GCBA | Organismo municipal | Template y carátula reglamentaria CABA |
| AySA | Organismo municipal | Planos sanitarios CABA |
| AEA | Organismo | Reglamentación eléctrica |
| Vicente López | Municipio referente | Modelo de plano |
| Zárate | Municipio referente | Modelo de plano |
| Fusion | Software | Futuro MCP, modelado 3D con IA |
| Revit | Software | Futuro BIM |
| ezdxf | Biblioteca Python | Generación DXF sin AutoCAD |
| limuzi013/autocad-mcp | MCP servidor | Control COM de AutoCAD |
| puran-water/autocad-mcp | MCP servidor | AutoLISP/DXF sin AutoCAD |
| BarryMcAdams/AutoCAD_MCP | MCP servidor | Automatización 2D/3D |
| Autodesk Product Help MCP | MCP servidor | Ayuda oficial remota |
| Claude Code | Cliente | Herramienta de agente |
| Codex | Cliente | Herramienta de agente |
| OpenCode | Cliente | Herramienta de agente |

---

## Referentes

| Referente | Fuente | Verificado |
|-----------|--------|------------|
| CAPBA Distrito 1 | capbauno.org | Sí — https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf |
| GCBA | buenosaires.gob.ar | Sí — https://buenosaires.gob.ar/gcaba_historico/armado-de-planos |
| AEA | aea.org.ar | Sí — https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf |
| AySA | aysa.com.ar | Sí — https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf |
| Vicente López | vicentelopez.gov.ar | Sí — https://www.vicentelopez.gov.ar/contenido/archivos/2024-06-26-945-archivo.pdf |
| Zárate | zarate.gob.ar | Sí — https://zarate.gob.ar/wp-content/uploads/2024/03/ESPECIFICACIONES-PARA-LA-PRESENTACION-DE-PLANOS-2024.pdf |
| Autodesk | help.autodesk.com | Sí — múltiples URLs verificadas en el doc |

---

## Hechos/decisiones reutilizables vs. infra efímera

### Reutilizables (van al vault/estándares)
- Estructura del "Kit Estudio Pi" (DWT + DWS + biblioteca de bloques) — es el estándar central
- 8 clases de C1 con comandos organizados — es el vocabulario del lenguaje
- Tabla de bloques mínimos para planos municipales — es la gramática visual
- Arquitectura del "Agente Estudio Pi" — es el framework de implementación
- Comandos clave por clase — son las palabras del idioma

### Efímera (no va al estándar)
- Plano de 15 días — es logística, no estándar
- Comparativa de clientes Claude Code/Codex/OpenCode — es infra de herramienta
- Precios de licencias — información transitoria
- Configuración técnica de MCPs — es setup, no estándar

---

## Análisis de contraste: Manifiesto vs. Documento Maestro

| Dimensión | Manifiesto (00-filo) | Documento Maestro |
|-----------|---------------------|-------------------|
| **Registro** | Filosófico/lingüístico ("el dibujo es un lenguaje") | Instrumental/técnico ("comando L, comando C") |
| **Propósito** | Definir por qué existen los estándares | Definir cómo se usan los comandos |
| **Audiencia** | El dibujante como hablante del idioma | El alumno como usuario de la herramienta |
| **Abstracción** | Alta — principios, filosofía | Baja — comandos, sintaxis, parámetros |
| **Tono** | Reflexivo, poético, generativo | Práctico, instructivo, compilatorio |
| **Relación con "estándar"** | El estándar es la voz propia del estudio | El estándar es un archivo DWS con reglas |

**Diagnóstico**: El documento maestro es el *diccionario* de un idioma que el manifiesto intenta definir el *alma*. Necesitan mutuamente — pero operan en registros diferentes. El documento maestro no tiene las respuestas que el manifiesto pregunta.

---

## ¿Qué sirve para armar specs del MVP_02?

### ✅ APTO para specs (se puede convertir)

1. **Sección 4 (C1: Comandos por clase)** → Base para el nivel `n_01-layers` y `n_03-text-dims`. Los comandos de capas (LAYER, LT, LAYISO) y texto (STYLE, MTEXT, DIM) son el núcleo.
2. **Sección 5.2 (Programa C2)** → Base para los niveles `n_02-plot`, `n_03-text-dims`, `n_04-templates`. Clase 1 ya menciona DWT + capas + estilos + tipos de línea.
3. **Sección 5.3 (Biblioteca mínima municipal)** → Base para `n_05-bloques`. Define qué bloques necesita el estudio.
4. **Sección 8 (C4: 3D/CNC)** → Fuente para un futuro `n_07-3d` si el scope del MVP_02 se expande.
5. **Sección 9 (Agente IA)** → Contexto para el AutoLISP y el MCP que aplican estándares.
6. **Sección 5.1 (Alineación ACP)** → Justificación del por qué ciertos comandos están en cierto orden (peso 22%, 20%, 29%, etc.)

### ⚠️ APTO con filtro (necesita adaptación)

1. **Sección 3 (Ecosistema de cursos)** → Útil para entender el marco general, pero el MVP_02 no es un plan de cursos. Los cursos son el vehículo; el MVP_02 es el contenido.
2. **Sección 7 (C3: Municipal)** → Da contexto de quién recibe el dibujo, pero las jurisdicciones específicas son scope de otro MVP.
3. **Sección 11 (Plan de 15 días)** → Logística, no estándar. Solo el "Kit Estudio Pi" concept es relevante.

### ❌ FUERA DE SCOPE del MVP_02

1. **Sección 2 (Fuentes oficiales)** — Son referencias, no estándares. Van al glosario de fuentes.
2. **Sección 9.1 (Panorama MCP)** — Infraestructura técnica, no estándar de dibujo.
3. **Sección 10 (Configuración clientes)** — Setup, no estándar.
4. **Sección 12 (Licencias)** — Administrativo, no estándar.
5. **Sección 1 (Situación actual)** — Contexto puntual, no reutilizable como estándar.

---

## Qué falta para que sea temario completo

El documento maestro **no tiene** (y el manifiesto pide que se defina):

1. **Catálogo de layers con nombre, color, linetype, lineweight y descripción** — El checklist #1 del spec (01-spec) dice que falta esto
2. **CTB oficial con registro de cada peso de pluma y su justificación** — El checklist #2 del spec
3. **Text styles y dimension styles estándar documentados** — El checklist #3
4. **Template DWT base con todos los estándares** — El checklist #4
5. **Justificación filosófica de cada standard** — El manifiesto pide "opinados pero justificados"
6. **Reglas de naming de planos** — El checklist #6 del spec menciona el naming
7. **AutoLISP por nivel que automatice la configuración** — El checklist #5
8. **Definición de "qué es un layer bien nombrado" según el idioma del estudio** — Esto no existe en ningún lado aún

**El vacío central**: El documento maestro tiene los *comandos* (el vocabulario) pero no tiene los *lineamientos* (la gramática, la sintaxis, el significado). El manifiesto tiene la *filosofía* (el alma) pero no tiene la *aplicación* (la gramática). El MVP_02 necesita construir la gramática — y eso es lo que son los niveles `n_01` a `n_06`.

---

## Estructura de temario propuesta (sintetizada)

Basada en el documento maestro + manifiesto + roadmap del 02-ft:

```
MVP_02 — Temario Oficial
│
├── MÓDULO 0: Filosofía y Fundamento (del manifiesto 00-filo)
│   ├── El dibujo como documento y lenguaje
│   ├── El estándar como puente entre libertad y empatía
│   ├── Cada estudio tiene su idioma
│   └── El estándar evolutivo
│
├── MÓDULO 1: Layers y Nomenclatura (n_01) ← del doc: Clase 5, Secciones 4/5.2
│   ├── Naming conventions del estudio
│   ├── Colores, linetypes, lineweights
│   ├── Comandos: LAYER, LT, LAYISO, LAYOFF, QSELECT
│   └── Justificación: por qué cada layer se llama así (ADR)
│
├── MÓDULO 2: Plot Styles y Grosores (n_02) ← del doc: Sección 5.2 clase 8
│   ├── CTB oficial del estudio
│   ├── Pesos de pluma y su justificación
│   ├── Comandos: PAGESETUP, PLOT, CTB/STB
│   └── Justificación: por qué el muro se plotea con peso 0.35 (ADR)
│
├── MÓDULO 3: Text y Dimension Styles (n_03) ← del doc: Clases 6/7, Secciones 4/5.2
│   ├── Text styles estándar
│   ├── Dimension styles con variantes anotativas (1:50, 1:100, 1:200)
│   ├── Comandos: STYLE, DIM, DIMSTYLE, MLEADER
│   └── Justificación: tamaños tipográficos y su razón
│
├── MÓDULO 4: Templates DWT (n_04) ← del doc: Secciones 5.2 clase 1, 5.3
│   ├── Kit Estudio Pi: DWT + DWS + biblioteca
│   ├── Unidades, capas por norma, estilos
│   ├── Layouts con carátula
│   └── Justificación: qué contiene cada template y por qué
│
├── MÓDULO 5: Bloques Estándar (n_05) ← del doc: Secciones 5.3, 5.4
│   ├── Bloques dinámicos (puerta, ventana, rótulo, carátula)
│   ├── Atributos y DATAEXTRACTION
│   ├── Biblioteca mínima municipal
│   └── Justificación: qué bloque existe y para qué se usa
│
├── MÓDULO 6: Naming y Presentación (n_06) ← del doc: Secciones 7, 11
│   ├── Convenciones de naming de archivos
│   ├── Convenciones de naming de planos
│   ├── PDF, firma, carga en TAD
│   └── Justificación: la lógica del nombre como lenguaje
│
├── MÓDULO 7: Agente IA y AutoLISP (transversal) ← del doc: Secciones 9/11
│   ├── MCP y arquitectura del agente
│   ├── AutoLISP que aplica estándares por módulo
│   ├── DWS + CHECKSTANDARDS
│   └── Justificación: el estándar se aplica con herramientas
│
└── MÓDULO 8: Fuentes y Referentes (de apoyo) ← del doc: Secciones 2/14
    ├── Comando Reference (oficiales)
    ├── Normativa (AEA, CAPBA, GCBA, AySA)
    ├── ACP como marco de alineación
    └── Verificación: cada fuente con nota [^n]
```

---

## Propuestas wiki (sin tocar, solo proponer)

| Entrada propuesta | Tipo | Origen | Destino previsto |
|-------------------|------|--------|------------------|
| `autocad` | software | Doc maestro (comandos) | `wiki/glosario/software/autocad` |
| `ezdxf` | software | Doc maestro (sección 9.10.3) | `wiki/glosario/software/ezdxf` |
| `mcp-autocad` | concepto | Doc maestro (sección 9) | `wiki/glosario/conceptos/mcp-autocad` |
| `kit-estudio-pi` | concepto | Doc maestro (idea central) | `wiki/glosario/conceptos/kit-estudio-pi` |
| `dwt-dws-standard` | concepto | Doc maestro + manifiesto | `wiki/glosario/conceptos/dwt-dws-standard` |
| `ACP-autocad` | concepto | Doc maestro (sección 5.1) | `wiki/glosario/conceptos/ACP-autocad` |
| `CAPBA` | referente | Doc maestro (sección 5.3) | `wiki/glosario/referentes/CAPBA` |
| `GCBA-planos` | referente | Doc maestro (sección 7) | `wiki/glosario/referentes/GCBA` |
| `AEA-90364` | referente | Doc maestro (sección 6) | `wiki/glosario/referentes/AEA` |
| `Estudio-Pi` | entidad | Doc maestro | `wiki/glosario/entidades/Estudio-Pi` |
| `niveles-MVP_02` | concepto | Roadmap 02-ft + doc maestro | `wiki/glosario/conceptos/niveles-MVP_02` |

---

## Preguntas para SOL

1. **¿El "Kit Estudio Pi" (DWT+DWS+blocks) es el estándar central del MVP_02 o es un artefacto?** — El manifiesto dice que los `.md` son la fuente de verdad y los binarios cuelgan de ellos. El Doc Maestro propone lo contrario (el DWT como kit central). ¿Quién define qué cuelga de qué?

2. **¿El documento maestro es un "MVP_02.5" o un MVP_03?** — El Doc Maestro cubre temas que el roadmap del MVP_02 no menciona (MCP, agente IA, 3D/CNC, licencias). ¿Es parte del MVP_02 o es otro proyecto?

3. **¿Las secciones 12 y 13 (licencias, plan de 15 días) necesitan su propio MVP o son logística?** — El manifiesto dice que scope = layer standards, plot styles, text/dim styles, templates, bloques, naming. Las licencias están fuera.

4. **¿El Doc Maestro reemplaza al 00-filo o lo complementa?** — El manifiesto tiene la filosofía; el doc maestro tiene el material. ¿El estándar de MVP_02 es la filosofía documentada o el manual de comandos?

5. **¿El agente IA (sección 9) es parte del MVP_02 o es un MVP separado?** — El manifiesto dice "AutoLISP como enforcement" — el Doc Maestro propone un MCP/IA como enforcement. Son compatibles pero de alcance muy distinto.

---

## Estado wiki

- **No se toca la wiki** — según instrucción explícita del usuario
- Todas las propuestas de entrada quedan aquí como sugerencias pendientes de aprobación de SOL

---

## Decisiones SOL (pendientes de marca)

- [ ] **Pendiente** — Aprobar/descartar estructura de temario propuesta
- [ ] **Pendiente** — Definir relación Doc Maestro vs. Manifiesto vs. Specs
- [ ] **Pendiente** — Decidir si el Doc Maestro es MVP_02 o MVP_03
- [ ] **Pendiente** — Aprobar/descartar propuestas de entrada wiki

---

> *Report generado por vaultworm-arq según metodología curatorial. Sin modificar la wiki. Pendiente de revisión humana.*
