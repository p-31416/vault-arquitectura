---
tipo: concepto
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-09-07
tags: [bim, metodologia, iso19650, cde, lod, concepto]
origen: wiki/glosario/conceptos/bim-metodologia.md → wiki/glosario/conceptos/ (externo, investigación)
---

# Metodología BIM Internacional

> **Nota:** Esta página describe el marco teórico BIM tal como lo definen los estándares internacionales. En la práctica, cada estudio lo adapta según su realidad: algunos usan BIM completo, otros CAD con datos estructurados, otros un híbrido. Todas las variantes son válidas. El vault está diseñado para funcionar con cualquier metodología, incluso "BIM mal usado" (parcial, híbrido, en transición).

## ¿Qué es BIM?

Building Information Modeling es una metodología de trabajo colaborativa para la gestión de información de un activo construido a lo largo de todo su ciclo de vida. BIM no es un software ni un modelo 3D — es un **proceso** basado en la generación y gestión de datos estructurados durante el diseño, construcción y operación de un edificio o infraestructura.

El término fue formalizado por Autodesk en 2002, pero sus principios vienen de los años 70 (conceptos de "building product model" de Charles Eastman). Desde 2010, gobiernos como el del Reino Unido comenzaron a exigir BIM en obra pública, impulsando la estandarización global.

## Estándares internacionales

### ISO 19650 — El marco principal

ISO 19650 es la serie de estándares internacionales para la gestión de información usando BIM. Publicada originalmente en 2018 y en revisión 2026, reemplazó a los estándares nacionales previos (principalmente la serie PAS 1192 del Reino Unido).

La serie se compone de:

| Parte | Título | Enfoque |
|-------|--------|---------|
| ISO 19650-1 | Conceptos y principios | Fundamentos de gestión de información, CDE, ciclo de vida |
| ISO 19650-2 | Fase de entrega | Gestión de información durante diseño y construcción |
| ISO 19650-3 | Fase operativa | Gestión de información durante la operación del activo |
| ISO 19650-4 | Intercambio de información | Formatos, IFC, interoperabilidad |
| ISO 19650-5 | Seguridad | Gestión de información sensible, ciberseguridad |
| ISO 19650-6 | Salud y seguridad | Gestión de riesgos en obra |

**Revisión 2026 (en curso):** El borrador de la nueva versión (DIS) se publicó el 10 de marzo de 2026. Los cambios principales son:
- Unificación de las fases de entrega y operación en un solo proceso de 9 pasos
- Cambio de terminología: "BIM Execution Plan" pasa a llamarse "Information Production Plan"
- Enfoque en "gestión de información" en lugar de "BIM" como término
- Integración con ISO 7817 (Level of Information Need) e ISO 29481 (Information Delivery Manuals)
- Publicación estimada de la versión final: 2027

### LOD — Level of Development

El framework LOD fue desarrollado originalmente por AIA (American Institute of Architects) en el formulario G202-2013. Es mantenido por BIMForum, que publica la especificación LOD anualmente (última versión: 2025, también disponible en español).

Define 6 niveles de desarrollo del modelo:

| Nivel | Nombre | Uso | Contenido |
|-------|--------|-----|-----------|
| LOD 100 | Conceptual | Estudios de viabilidad | Masas genéricas, áreas, volúmenes |
| LOD 200 | Esquemático | Anteproyecto | Geometría aproximada, cantidades estimadas |
| LOD 300 | Detallado | Documentación legal | Geometría precisa, coordinación entre disciplinas |
| LOD 350 | Coordinación | Construcción | Interfaces entre sistemas, conexiones |
| LOD 400 | Fabricación | Taller y montaje | Ensambles detallados, especificaciones de fabricación |
| LOD 500 | As-Built | Operación y mantenimiento | Modelo registrado con datos de obra y FM |

La especificación LOD está organizada por Uniformat 2010 e incluye elementos de todas las disciplinas (arquitectura, estructura, MEP).

### Otros estándares relevantes

| Estándar | Origen | Enfoque |
|----------|--------|---------|
| PAS 1192 (UK) | Reino Unido | Predecesor de ISO 19650, aún en uso |
| UK BIM Framework | Reino Unido | Guía nacional alineada con ISO 19650 |
| NBIMS-US | EE.UU. | Estándar nacional BIM de EE.UU. (buildingSMART USA) |
| IFC | buildingSMART | Esquema abierto de datos para interoperabilidad entre softwares |
| BCF (BIM Collaboration Format) | buildingSMART | Formato para gestión de incidencias y comentarios entre plataformas |
| COBie | EE.UU./UK | Formato estructurado para datos de activos en la entrega de obra |

## Conceptos clave

### Common Data Environment (CDE)

Entorno Común de Datos — repositorio único y centralizado donde todo el equipo del proyecto almacena, comparte y gestiona la información. Definido por ISO 19650 como "fuente acordada de información para cualquier proyecto o activo".

El CDE organiza la información en cuatro estados:
1. **Work In Progress (WIP)** — información en desarrollo, solo visible para el equipo que la produce
2. **Shared** — información revisada y compartida con el equipo para coordinación
3. **Published** — información aprobada y publicada para su uso contractual
4. **Archived** — información histórica, mantenida como registro

### CDE en la práctica — el vault como CDE

El concepto CDE aplica perfectamente a este vault. Cada proyecto tiene su carpeta en `proyectos/` con los estados reflejados en la organización de archivos:

| Estado CDE | Equivalente en el vault | Contenido |
|------------|------------------------|-----------|
| WIP | `proyectos/<proyecto>/documentacion/` | Memorias en desarrollo, borradores |
| Shared | `proyectos/<proyecto>/reuniones/` | Notas compartidas con el equipo |
| Published | `proyectos/<proyecto>/entregables/` | Documentos entregados al cliente |
| Archived | `proyectos/archived/` | Proyectos cerrados |

Los binarios (planos, renders) están en `activos/` y se referencian desde los .md. No necesitás una plataforma cloud paga — git + carpetas locales cumplen la función de CDE para un estudio chico.

### BIM Execution Plan (BEP) / Information Production Plan

Documento que define cómo el equipo del proyecto producirá, gestionará y entregará la información requerida. Incluye:
- Roles y responsabilidades
- Estándares y convenciones (nombrado, LOD, software)
- Hitos de entrega de información
- Estrategia de coordinación y clash detection
- Plataforma CDE a utilizar

En la revisión ISO 19650:2026, pasa a llamarse **Information Production Plan**.

### Exchange Information Requirements (EIR)

Documento del cliente/contratante que especifica qué información necesita, en qué formato y en qué momentos del proyecto. Es el punto de partida de todo el proceso de gestión de información.

### Naming convention ISO 19650

ISO 19650:2021 simplificó la convención de nombrado eliminando longitudes fijas de campos. La estructura recomendada es:

```
Proyecto – Originador – Función – Ubicación – Formato – Disciplina – Número
```

Ejemplo: `HOSP-CENTRAL-ARQ-PB-PLANTA-DWG-001`

### Niveles de madurez BIM

| Nivel | Descripción | Colaboración |
|-------|-------------|--------------|
| BIM Level 0 | CAD 2D, archivos sueltos | Sin colaboración |
| BIM Level 1 | CAD 2D + modelos 3D | Colaboración parcial, CDE básico |
| BIM Level 2 | Modelos 3D federados, datos estructurados | Colaboración plena, ISO 19650 |
| BIM Level 3 | Modelo único compartido en la nube | Colaboración en tiempo real (iBIM) |

## Dimensiones BIM

| Dimensión | Enfoque | Información |
|-----------|---------|-------------|
| 2D | Documentación técnica | Planos, cortes, elevaciones |
| 3D | Modelado geométrico | Forma, espacialidad, coordinación |
| 4D | Tiempo | Planificación de obra, secuencia constructiva |
| 5D | Costo | Mediciones, presupuestos, cubicaciones |
| 6D | Sostenibilidad | Análisis energético, ciclo de vida, huella de carbono |
| 7D | Operación y mantenimiento | FM, manuales, garantías, as-built |

## Roles BIM en un estudio

| Rol | Función |
|-----|---------|
| Information Manager | Responsable de la gestión de información del proyecto |
| BIM Coordinator | Coordinación entre disciplinas, clash detection, federación de modelos |
| BIM Modeler | Modelado paramétrico, familias, documentación desde el modelo |
| BIM Manager | Define estándares del estudio, capacita al equipo, audita modelos |
| CDE Administrator | Gestiona la plataforma CDE, permisos, flujos de aprobación |

## BIM en las fases del proyecto

| Fase | Actividad BIM |
|------|--------------|
| Concurso / Briefing | Modelo conceptual (LOD 100-200), análisis de viabilidad |
| Anteproyecto | Desarrollo de geometría, coordinación básica (LOD 200) |
| Proyecto legal | Modelo detallado, documentación legal desde el modelo (LOD 300) |
| Proyecto ejecutivo | Coordinación entre disciplinas, clash detection (LOD 350) |
| Construcción | Modelo de taller, planificación 4D, cubicaciones 5D (LOD 400) |
| Entrega | Modelo as-built, documentación FM, COBie (LOD 500) |

## BIM accesible para Argentina (sin Revit ni suscripciones cloud)

BIM no requiere Revit ni una suscripción de Autodesk. La metodología funciona con cualquier software que pueda producir y gestionar datos estructurados. Para un estudio argentino con costos en USD acotados:

### Software alternativo

| Software | Licencia | Costo | Ideal para |
|----------|----------|-------|------------|
| **BricsCAD Pro** | Perpetua (no suscripción) | ~$700 una vez | CAD + BIM, familiar para usuarios de AutoCAD |
| **ArchiCAD** | Perpetua (Graphisoft) | ~$2.500 una vez | BIM nativo, muy usado en estudios chicos |
| **FreeCAD** | Open source (LGPL) | $0 | Modelado paramétrico, exportación IFC |
| **Blender + BIM addon** | Open source (GPL) | $0 | Modelado 3D + flujo BIM vía IFC |
| **AutoCAD LT** | Suscripción anual | ~$400/año | Alternativa barata si solo necesitás 2D |
| **DraftSight** | Perpetua (Dassault) | ~$200 una vez | Sustituto de AutoCAD, formato DWG |

Ninguno requiere conexión cloud permanente ni almacenamiento en servidores de terceros.

### CDE económico (sin suscripción cloud)

| Solución | Costo | Cómo funciona |
|----------|-------|---------------|
| **Git + carpeta local** | $0 | El vault mismo — versionado de .md, activos en carpeta compartida |
| **Nextcloud** (self-hosted) | $0 (software) + hosting | CDE propio con control total de datos |
| **Syncthing** | $0 | Sincronización P2P entre máquinas del equipo |
| **Dropbox / Google Drive** | ~$10-30/mes | Familiar, conocido, sin configuración técnica |

### Flujo híbrido CAD→BIM recomendado para estudio ARG

```
1. AutoCAD / BricsCAD      →  2D legal, planos en DWG
    + IFC export
          ↓
2. FreeCAD / Blender BIM   →  Modelo 3D paramétrico (LOD 200-300)
    + IFC export
          ↓
3. Vault (este repositorio) →  Documentación estructurada en .md
    + Referencias a archivos binarios
          ↓
4. CDE (Nextcloud / carpeta compartida) →  Distribución al equipo
```

No necesitás dar el salto completo a Revit de golpe. Podés trabajar BIM-consciente desde AutoCAD + IFC, e ir subiendo de nivel cuando el estudio crezca.

### Regla práctica

> Si tu estudio puede comprar una licencia perpetua de BricsCAD o ArchiCAD, tenés BIM por los próximos 5-10 años sin pagar un dólar más en software. El costo de 2 años de Revit + Autodesk Cloud equivale a una licencia perpetua de ArchiCAD.

## Recursos

### YouTube (canales recomendados)

| Canal | Por | Enfoque |
|-------|-----|---------|
| [The B1M](https://youtube.com/@TheB1M) | Fred Mills | Noticias y documentales de construcción y BIM |
| [Balkan Architect](https://youtube.com/@balkanarchitect) | — | Tutoriales de Revit y AutoCAD para arquitectos |
| [That BIM Girl](https://youtube.com/@ThatBIMGIRL) | Jacqueline | Tips de Revit, carrera BIM, workflows |
| [Aussie BIM Guru](https://youtube.com/@AussieBIMGuru) | Gavin Crump | Workflows BIM profesionales, Revit |
| [BIM Pure](https://youtube.com/@bimpure) | Nicolas Catellier | Cursos y tips avanzados de Revit |
| [BIM HUB](https://youtube.com/@BIMHUB) | — | Tutoriales de Revit, Navisworks, BIM 360 |
| [AEC Workbench](https://youtube.com/@AECWorkbench) | Bill Debevc | Dynamo, automatización, tecnología AEC |
| [BIM Corner](https://youtube.com/@bimcorner) | — | Ingenieros compartiendo conocimiento BIM práctico |
| [BIM me UP!](https://youtube.com/@BIMmeup) | Lejla Secerbegovic | IFC, openBIM, interoperabilidad |
| [Novatr](https://youtube.com/@Novatr) | — | Charlas de expertos sobre carrera BIM |

### Podcasts

| Podcast | Anfitrión(es) | Enfoque |
|---------|---------------|---------|
| Future Construct | Amy Peck + Mark Oden | Innovación tecnológica en AEC, BIM, IA |
| The BIM Podcast | — | Discusiones sobre BIM y construcción digital |
| Simplified BIM | — | Conceptos BIM explicados de forma accesible |

### Thought leaders y referentes

| Nombre | Redes | Aportación |
|--------|-------|------------|
| Fred Mills | [LinkedIn](https://linkedin.com/in/fredmills), [YouTube](https://youtube.com/@TheB1M) | Fundador de The B1M, divulgación global de construcción |
| Gavin Crump | [LinkedIn](https://linkedin.com/in/gavincrump), [YouTube](https://youtube.com/@AussieBIMGuru) | Aussie BIM Guru, educación BIM profesional |
| Nicolas Catellier | [LinkedIn](https://linkedin.com/in/nicolascatellier), [YouTube](https://youtube.com/@bimpure) | BIM Pure, formación Revit avanzada |
| Lejla Secerbegovic | [LinkedIn](https://linkedin.com/in/lejla-secerbegovic), [YouTube](https://youtube.com/@BIMmeup) | OpenBIM, IFC, interoperabilidad |
| Jacqueline (That BIM Girl) | [LinkedIn](https://linkedin.com/in/thatbimgirl), [YouTube](https://youtube.com/@ThatBIMGIRL) | Diseño Manager en Tesla, tips Revit |
| Bill Debevc | [LinkedIn](https://linkedin.com/in/billdebevc), [YouTube](https://youtube.com/@AECWorkbench) | Dynamo, automatización AEC |
| Mark Oden | [LinkedIn](https://linkedin.com/in/markoden) | CEO de BIM Designs, Inc., co-host Future Construct |
| David Churcher | — | Autor principal de ISO 19650-1 y -2 |
| Charles Eastman | — | Pionero, creador del concepto de Building Product Model (años 70) |
| Randy Deutsch | [LinkedIn](https://linkedin.com/in/randydeutsch) | Autor de "BIM and Integrated Design", profesor UIUC |
| Finith Jernigan | — | Autor de "BIG BIM little bim", pionero en adopción BIM |

## Referencias oficiales

- [ISO 19650-1: Concepts and Principles](https://www.iso.org/standard/68078.html) — ISO
- [ISO 19650-2: Delivery Phase](https://www.iso.org/standard/68080.html) — ISO
- [BIMForum LOD Specification 2025](https://bimforum.org/resource/lod-level-of-development-lod-specification/) — Descarga gratuita (inglés y español)
- [UK BIM Framework](https://www.ukbimframework.org/) — Guía nacional alineada con ISO 19650
- [buildingSMART International](https://www.buildingsmart.org/) — IFC, BCF, openBIM
- [BSI — ISO 19650 Training and Certification](https://www.bsigroup.com/en-GB/products-and-services/standards/iso-19650-building-information-modelling-bim/)
- [Autodesk — Levels of Development in BIM](https://www.autodesk.com/solutions/bim-levels-of-development)
- [Designing Buildings Wiki — Common Data Environment](https://www.designingbuildings.co.uk/wiki/Common_data_environment_CDE)
- [Proposed changes to ISO 19650 (marzo 2026)](https://buildindigital.com/proposed-changes-to-iso-19650/) — Build in Digital
- [ISO 19650 Revision 2026: Shift from BIM to IM](https://graitec.com/uk/blog/iso-19650-revision-2026) — Graitec
- [ISO 19650 Changes Explained (2026 Update)](https://rebim.io/iso-19650-changes-2026) — REBIM
- [NBS — BIM Toolkit](https://www.thenbs.com/bim-toolkit) — Recursos prácticos para implementación BIM
