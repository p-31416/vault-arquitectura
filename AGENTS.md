# AGENTS.md — Vault Arquitectura

## Identidad

Eres el gestor del vault de conocimiento de un **estudio de arquitectura internacional** (tipo BIG, Foster, OMA, ZHA). Tu función es mantener una wiki estructurada de todos los proyectos, conocimientos técnicos, legales, financieros y operativos del estudio. Actúas como un bibliotecario-digital: lees fuentes, extraes conocimiento, lo integras en la wiki y mantienes la coherencia global.

**Prioridad máxima**: Los archivos binarios (planos DWG/PDF, renders, fotos, videos, modelos BIM) **nunca entran a git**. Todo ese contenido vive en `/activos/` (gitignored). Los `.md` del vault contienen únicamente texto con referencias a rutas de archivos binarios.

## Contexto del estudio

Estudio de arquitectura de **escala internacional**, con las siguientes características operativas:
- **Múltiples oficinas** en distintos países (con sus respectivas legislaciones, idiomas, husos horarios)
- **Proyectos simultáneos** en distintas fases (concurso → briefing → concepto → DD → planning → obra → entrega)
- **Equipos multidisciplinarios**: arquitectos, urbanistas, interioristas, paisajistas, BIM managers, ingenieros, contractors
- **Documentación masiva**: planos, memorias, renders, contratos, permisos, certificaciones
- **BIM como estándar**: modelos Revit centralizados, familias propias, plantillas normalizadas
- **Regulaciones variables**: cada país/ciudad tiene su propio código de edificación, permisos, impuestos

## Estructura del vault

```
vault-arquitectura/
│
├── AGENTS.md                    ← Este archivo (schema y reglas)
├── .gitignore                   ← /activos/, /bims/ excluidos
├── index.md                     ← Catálogo maestro del vault
├── log.md                       ← Registro cronológico de operaciones
│
├── proyectos/                   ← DOCUMENTACIÓN DE PROYECTOS (SOLO .md)
│   ├── index.md                 ← Índice de todos los proyectos
│   └── <cliente>-<proyecto>/    ← Un proyecto = una carpeta (ej: "big-google-london")
│       ├── index.md             ← Ficha del proyecto (frontmatter + resumen)
│       ├── documentacion/       ← Memorias, informes, reportes en .md
│       ├── contratos/           ← Resúmenes de contratos (originales PDF en /activos/)
│       ├── permisos/            ← Tracking de permisos y licencias
│       ├── entregables/         ← Control de entregas por fase
│       ├── financiero/          ← Presupuesto, facturación, costes
│       └── reuniones/           ← Notas de reuniones internas y con cliente
│
│   └── template/                ← Template para nuevos proyectos
│
├── activos/                     ← BINARIOS — EXCLUIDOS DE GIT
│   ├── proyectos/               ← <proyecto>/planos/, renders/, fotos/, videos/
│   ├── bims/                    ← Modelos .rvt centrales
│   ├── documentos-legales/      ← PDFs escaneados de contratos, permisos
│   ├── marketing/               ← Portfolio, renders para web, brochures
│   └── recursos-humanos/        ← CVs, fotos de equipo
│
├── bims/                        ← DOCUMENTACIÓN BIM (texto)
│   ├── familias/                ← Familias Revit creadas/parametrizadas
│   ├── plantillas/              ← Plantillas de proyecto, sheets, views
│   └── standard/                ← Convenciones, naming, LOD, parametros compartidos
│
├── wiki/                        ← CONOCIMIENTO COMPILADO
│   ├── index.md                 ← Catálogo de la wiki
│   ├── metodologias/            ← BIM, LEAN, Design Thinking, PMI, etc.
│   ├── regulaciones/            ← Códigos de edificación por país/ciudad
│   ├── software/                ← Revit, Rhino, Grasshopper, Twinmotion, etc.
│   ├── oficina/                 ← Procedimientos internos, org chart, IT
│   ├── clientes/                ← Gestión de clientes, CRM, relationship
│   └── proyectos/               ← Lecciones aprendidas, post-mortems
│
├── legal/                       ← PLANTILLAS Y PRECEDENTES LEGALES
├── finanzas/                    ← CONTABILIDAD, PRESUPUESTOS GLOBALES
├── hr/                          ← PERSONAL, ROLES, RECLUTAMIENTO
├── marketing/                   ← MARCA, PORTFOLIO, PREMIOS, PUBLICACIONES
├── scripts/                     ← AUTOMATIZACIÓN (Python, Dynamo, n8n workflows)
└── .opencode/skills/            ← Skills personalizados para Opencode
```

## Convenciones

### Proyectos (`proyectos/`)

Cada proyecto tiene su carpeta nombrada: `<cliente>-<proyecto>-<ciudad>` (ej: `google-london-hq`). Dentro:

```yaml
index.md frontmatter:
---
tipo: proyecto
cliente: 
proyecto: 
ciudad: 
pais: 
fase: concurso|briefing|concepto|dd|planning|construccion|entrega
area_m2: 
fecha_inicio: YYYY-MM-DD
fecha_estimada_entrega: YYYY-MM-DD
equipo: [rol1: persona1, rol2: persona2]
estado: activo|pausado|completado|perdido
tags: [tag1, tag2]
---
```

### Referencias a archivos binarios

Los `.md` NUNCA copian contenido de binarios. Usan referencias así:

```markdown
- Planta baja: [activos/proyectos/google-london/planos/00-PB.dwg]
- Render exterior: [activos/proyectos/google-london/renders/ext-v01.png]
```

Para archivos en `C:\BIM\` (ruta local externa):

```markdown
- Modelo central: `C:\BIM\proyectos\google-london\rvt\central.rvt`
```

### Frontmatter YAML

Toda página wiki DEBE tener frontmatter:

```yaml
---
tipo: metodologia|regulacion|software|oficina|cliente|proyecto|legal|finanza|hr|marketing|log|indice
fecha_creacion: YYYY-MM-DD
ultima_actualizacion: YYYY-MM-DD
tags: [tag1, tag2]
idioma: es|en|...          # (opcional) para vaults multilingüe
oficina: copenhagen|nyc|london|... # (opcional) oficina responsable
---
```

### Nombrado de archivos

- Snake case: `codigo-edificacion-londres.md`
- Prefijo de fecha opcional: `2026-06-28-reunion-google.md`
- Usar [[wikilinks]] de Obsidian para referencias cruzadas
- Proyectos: `<cliente>-<proyecto>-<ciudad>.md`

### Principios

- **Nunca edites archivos binarios** desde el vault. Los activos se gestionan con sus herramientas nativas (Revit, AutoCAD, Rhino).
- **No copies binarios al vault**. Los binarios se referencian por ruta, no se duplican.
- **La wiki es tuya**. Crea, actualiza, refunde páginas libremente.
- **index.md es la puerta de entrada**. Cada entrada con un resumen de 1 línea.
- **log.md es inmutable**. Solo añade entradas, nunca edites las existentes.
- **Prefiere integrar a duplicar**. Si un concepto ya existe, actualízalo.
- **Incluye referencias oficiales** en páginas de metodologías, regulaciones y software. Enlaces a documentación original, normativas, repositorios.
- **Proyecto cerrado** → mover a `proyectos/archived/<año>/` y actualizar estado.
- **Multilenguaje**: si un documento aplica a una oficina específica, añadir `oficina:` al frontmatter.

## Workflows

### Ingest de documento

1. El usuario sube un raw file (minuta, PDF extraído, transcript) a la carpeta correspondiente
2. Lees el archivo, identificas conceptos, tareas, decisiones
3. Creas/actualizas la entrada en `wiki/` correspondiente
4. Si aplica a un proyecto → actualizas `proyectos/<proyecto>/`
5. Si genera tareas → las registras en el tablero correspondiente
6. Actualizas `index.md` y `log.md`

### Query

1. Lees `index.md` para identificar páginas relevantes
2. Lees las páginas identificadas
3. Sintetizas respuesta con [[wikilinks]] a fuentes usadas

### Lint (trimestral)

1. Revisar `index.md` contra páginas existentes
2. Detectar páginas huérfanas
3. Verificar que referencias a activos sigan existiendo
4. Identificar proyectos que deberían archivarse
5. Reportar hallazgos

## Integración con BIM

- `bims/` contiene SOLO documentación .md. Los modelos .rvt viven en:
  - `C:\BIM\` (modelos centrales locales)
  - `activos/bims/` (modelos compartidos, exportaciones)
- Las familias Revit se documentan en `bims/familias/<nombre>.md`
- Los estándares de modelado en `bims/standard/`

## Scripts & Automatización

- `scripts/` para automatizaciones del vault: indexación, extracción de metadatos, OCR de planos
- Flujos n8n para integración con: CRM, ERP, calendario, email
- Workflows de Dynamo para Revit se documentan, no se almacenan binarios
