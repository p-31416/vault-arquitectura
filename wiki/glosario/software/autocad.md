---
tipo: software
software: autocad
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, autocad]
---

# AutoCAD

> Glosario AutoCAD — comandos, funciones AutoLISP y variables del sistema. Migrado de `autocad/` (legacy) a archivo único.

- [Convenciones](#convenciones)
- [Comandos — PLINE](#pline--polilinea)
- [Funciones — entmake](#entmake--crear-entidades-desde-autolisp)
- [Comandos pendientes](#comandos-pendientes)
- [Funciones pendientes](#funciones-pendientes)
- [Variables del sistema](#variables-del-sistema)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Convenciones

- **Comando nativo AutoCAD**: mayúsculas (`LINE`, `PLINE`, `LAYER`)
- **Función AutoLISP**: minúsculas (`entmake`, `command`, `ssget`)
- **Variables del sistema**: con prefijo (`CLAYER`, `CELTYPE`)

> Fuente original: `wiki/glosario/software/autocad/00-index.md` — frontmatter `tipo: indice, tags: [glosario, autocad, wiki, indice]` (2026-06-30).

---

## PLINE — Polilínea

> Fuente: `pline.md` — `comando: PLINE, software: autocad, tipo: comando` (2026-06-30).

### Qué hace

Dibuja una **polilínea**: una secuencia de segmentos conectados (rectos y/o arcos) que forman una sola entidad. A diferencia de `LINE`, una polilínea tiene grosor variable, se puede editar con `PEDIT` y es la base de casi todo el dibujo arquitectónico en AutoCAD (muros, losas, contornos).

### Sintaxis / Cómo se usa

```
PLINE
  Specify start point: (clic o coordenada)
  Specify next point or [Arc/Halfwidth/Length/Undo/Width]:
    → punto siguiente (recto)
    → A (modo arco)
    → W (grosor global)
    → U (deshacer último)
    → C (cerrar)
```

### Opciones clave

| Opción | Qué hace |
|--------|----------|
| `Arc` | Cambia a dibujo de arcos |
| `Width` | Define grosor inicial y final del segmento |
| `Halfwidth` | Como Width pero desde el centro |
| `Length` | Dibuja un segmento con longitud y ángulo del anterior |
| `Close` | Cierra la polilínea al punto inicial |
| `Undo` | Deshace el último segmento |

### Ejemplo en AutoLISP

```lisp
;; Dibujar un rectángulo como polilínea cerrada
(command "PLINE"
  (list 0 0)
  (list 1000 0)
  (list 1000 500)
  (list 0 500)
  "C"
)
```

### Variables del sistema relacionadas

| Variable | Efecto |
|----------|--------|
| `PLINEWID` | Grosor por defecto de nuevas polilíneas (0 = sin grosor) |
| `PLINETYPE` | Controla si se crean como optimizadas (2) o clásicas |
| `PLINEGEN` | Generación de linetype alrededor de vértices |

### Notas del estudio

- Preferir `PLINE` sobre `LINE` para cualquier elemento que represente un componente constructivo (muros, losas, carpinterías). Permite editar grosor, unir, y es compatible con `PEDIT`.
- `PLINEWID` se deja en 0. El grosor visual se asigna por layer o por CTB, no por ancho de polilínea (salvo casos específicos como sombreados gráficos).

---

## entmake — Crear entidades desde AutoLISP

> Fuente: `entmake.md` — `comando: entmake, software: autocad, tipo: funcion` (2026-06-30).

### Qué hace

Crea una **nueva entidad** en la base de datos del dibujo sin ejecutar un comando AutoCAD. Es la forma más directa y controlada de generar geometría desde AutoLISP: le pasás una lista con los códigos DXF de la entidad y AutoCAD la crea al instante.

**Ventaja sobre `command`**: no depende del estado del comando, no afecta variables del sistema, no genera prompts, y es más rápida.

### Sintaxis / Cómo se usa

```lisp
(entmake '((0 . "TIPO") (8 . "LAYER") (10 x y z) ... ))
```

Cada sublista es un **código DXF**:

| Código | Significado |
|--------|-------------|
| `0` | Tipo de entidad (`"LINE"`, `"LWPOLYLINE"`, `"CIRCLE"`, etc.) |
| `8` | Layer |
| `10` | Punto inicial / inserción (coordenada) |
| `11` | Punto final / segundo punto |
| `62` | Color (número; 256 = ByLayer, 0 = ByBlock) |
| `6` | Linetype (`"CONTINUOUS"`, `"DASHED"`, etc.) |
| `370` | Lineweight (en centésimas de mm; -1 = ByLayer) |

### Ejemplo

```lisp
;; Crear una línea en el layer A-WALL
(entmake '(
  (0 . "LINE")
  (8 . "A-WALL")
  (10 0.0 0.0 0.0)
  (11 500.0 0.0 0.0)
  (62 . 7)
  (370 . -1)
))
```

### Funciones relacionadas

| Función | Qué hace |
|---------|----------|
| `entmakex` | Como `entmake` pero devuelve el entity name |
| `entmod` | Modifica una entidad existente |
| `entdel` | Elimina una entidad |

### Notas del estudio

- Usamos `entmake` siempre que sea posible en lugar de `command`. Es más predecible y evita problemas con `OSNAP`, `UCS` y variables del sistema.
- Para `LWPOLYLINE` (polilínea ligera), los vértices se pasan con código `10` repetido (uno por vértice) y un código `90` con el número de vértices.
- Siempre incluir `(8 . "LAYER")`. Si se omite, la entidad va al layer actual.

---

## Comandos pendientes

| Comando | Para qué se usa | MVP relacionado |
|---------|----------------|-----------------|
| `LINE` | Dibujar líneas | MVP_01 |
| `LAYER` / `-LAYER` | Crear y gestionar layers | MVP_02 |
| `HATCH` | Sombreados | MVP_01 |

> Stub — crear sección dedicada cuando se documente cada comando. Ver `00-index.md` legacy.

## Funciones pendientes

| Función | Para qué se usa | MVP relacionado |
|---------|----------------|-----------------|
| `ssget` | Seleccionar entidades | MVP_01 |
| `command` | Ejecutar comandos desde LISP | MVP_01, MVP_02 |
| `entmod` | Modificar entidades existentes | MVP_02 |

## Variables del sistema

| Variable | Para qué se usa | MVP relacionado |
|----------|----------------|-----------------|
| `CLAYER` | Layer actual | MVP_02 |
| `CELTYPE` | Tipo de línea actual | MVP_02 |
| `LUNITS` | Unidades lineales | MVP_02 |

---

## Conceptos relacionados

- [[wiki/glosario/conceptos/bim-metodologia]]
- [[wiki/glosario/conceptos/design-thinking]]

## Referencias

- [Documentación Autodesk — PLINE](https://help.autodesk.com/cloudhelp/2024/ENU/AutoCAD-Core/files/GUID-11883C70-6435-4F80-8FB4-F6E933B8FD94.htm) (verificar con webfetch — migrado de `pline.md`)
- [Documentación Autodesk — entmake (AutoLISP)](https://help.autodesk.com/cloudhelp/2024/ENU/AutoCAD-AutoLISP-Reference/files/GUID-D47983BA-1E5D-417D-85B8-6F3DE5F506BA.htm) (verificar con webfetch — migrado de `entmake.md`)
- [Guía DXF Reference — códigos por grupo](https://help.autodesk.com/cloudhelp/2024/ENU/AutoCAD-DXF-Reference/files/GUID-235B22E0-7B5E-4F1E-8B0A-3C9F0C0F0B1A.htm)
- Comandos pendientes en ayuda Autodesk (patrón `?query=<COMANDO>`, migrado de stubs `autocad/`): [LINE](https://help.autodesk.com/view/ACD/2026/ENU/?query=LINE) · [LAYER](https://help.autodesk.com/view/ACD/2026/ENU/?query=LAYER) · [HATCH](https://help.autodesk.com/view/ACD/2026/ENU/?query=HATCH) · [SSGET](https://help.autodesk.com/view/ACD/2026/ENU/?query=SSGET) · [COMMAND](https://help.autodesk.com/view/ACD/2026/ENU/?query=COMMAND) · [ENTMOD](https://help.autodesk.com/view/ACD/2026/ENU/?query=ENTMOD) · [CLAYER](https://help.autodesk.com/view/ACD/2026/ENU/?query=CLAYER) · [CELTYPE](https://help.autodesk.com/view/ACD/2026/ENU/?query=CELTYPE) · [LUNITS](https://help.autodesk.com/view/ACD/2026/ENU/?query=LUNITS)
