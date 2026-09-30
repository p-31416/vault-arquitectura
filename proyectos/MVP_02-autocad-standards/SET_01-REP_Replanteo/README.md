---
tipo: indice
set: SET_01-REP
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-28
tags: [mvp_02, SET_01, indice]
---

# SET_01-REP — Replanteo

> Carpeta del SET 01. Norma: `SET_0x-XXX_Descripcion/`. Workflow: spec define el QUÉ, ft define el CÓMO.

## Archivos

| Archivo | Estado | Notas |
|---------|--------|-------|
| `01-spec-SET_01.md` | Parcial | §0 checklist, §2 capas, §4.2 SETEO, §5-§9 pendientes. §7 borrador AutoLISP en metros. |
| `02-ft-SET_01.md` | Parcial | §1 SETEO escrito con 7 pasos; §2-§10 placeholders. El usuario completa manualmente con MCPs. |
| `lisp/` *(vacía)* | Pendiente paso 9 | AutoLISP borrador en spec §7 |
| `docs/` *(vacía)* | Pendiente por ítem | Se reharán paso a paso |

## Carpeta de trabajo vinculada

- **W03-CAD**: `G:\Mi unidad\OS-Emilia\W03-CAD` — carpeta externa con DWG/DWT de trabajo del SET_01 (NO en git, NO en vault). Los `.md` de esta carpeta referencian esos binarios por ruta.

## Binarios — NO en git

**Regla vault**: DWG/DWT/DWS/CTB/PDF nunca en git. Viven en `activos/` (gitignored). Acá solo referencias por ruta.

```
activos/proyectos/mvp_02-autocad-standards/SET_01-REP/
├── SET_01-REP.dwt
├── SET_01-REP.dws
├── EP-ISO.ctb
├── SET_01-REP_bloques.dwg
└── SET_01-REP.las
```
