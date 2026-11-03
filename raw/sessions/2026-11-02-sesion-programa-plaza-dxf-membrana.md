---
tipo: sesion
fecha: 2026-11-02
tags: [sesion, concurso-gaudi-nexus, programa, catenaria, kangaroo, cadmapper, dxf, rhino]
---

# Sesión 2026-11-02 — Programa en plaza + membrana Kangaroo + DXF para AutoCAD

> Cierre de día: de la cáscara paramétrica al programa dibujado sobre el CADMapper y exportado a DXF. **Ojo de estado**: lo de Rhino quedó en memoria, el `.3dm` en disco NO se guardó (las capas `PROG-*` viven solo en la sesión abierta).

## 1. Qué se hizo

### A. Membrana catenaria paramétrica (mañana)
- **Teselado triangular tipo Escher + cáscara demo**: loft de catenaria transversal con ola longitudinal + grilla triangular `s=1,2` drapeada (172 triángulos, 1/4 a verde). Volcado a Rhino y verificado en viewport.
- **Investigación Parametric Monkey** (`parametricmonkey.com/2015/10/10/catenary-curves`): componente `Catenary` matemático vs Kangaroo físico (mesh, no NURBS), membranas y estructuras anidadas. Resumen entregado a Sol.
- **Membrana invertida transitable**: especificación `L=8, LONG=30, H=2,5, espesor 0,4, rebaje DIG=1,0` → luz centro 3,1 m. Volcada a Rhino con piso a −1,0.
- **Membrana de doble curvatura** (reemplaza el loft reglado): catenaria en X (`7,5 m / flecha 0,6`) × catenaria en Y (`8 m / flecha 0,8`), mesh de 403 vértices, 10 apoyos puntuales cada 7,5 m, planta baja libre. Teselado triangular redrapeado (172). Loft viejo eliminado (175 objetos), capas renombradas a definitivo (`CASCARA/CAMINO/VERDE/APOYOS/PISO`).

### B. Definición Grasshopper Kangaroo (tarde, lo más largo del día)
- **Generador programático del `.gh`**: construido objeto por objeto vía API de Grasshopper dentro de Rhino (GUIDs resueltos por nombre, `AddSource`, sliders con dominio). Archivo único final: `activos/proyectos/concurso-gaudi-nexus/grasshopper/membrana-catenaria.gh` (36 objetos, 12 sliders).
- **Red real**: `Rectangle → MeshPlane → Show → Solver.GoalObjects` (+ `EdgeLengths`, `Load`, `Anchor` 4 esquinas) → `ConstructMesh` desde `Solver.V` + caras originales → `Mirror` XY → `TriRemesh` (`Length = s_tri`) + `Point Deform` en piso con `Prof`. Esquinas a altura independiente (`H1–H4`), sin columnas (apoya en plano `z=0`).
- **Tres bugs encontrados y corregidos con docs oficiales** (grasshopperdocs + tutorial CMU):
  1. `Anchor` recibía 121 vértices contra 4 objetivos (`Index out of range` en cascada) → `Anchor.P` toma las 4 esquinas.
  2. `TriRemesh.Target` espera una **malla**, no un número → el slider `s_tri` va a **`Length`** ("Target edge length"). Era el `Data conversion failed from Number to Mesh`.
  3. El `Show` va **antes** del Solver (su salida son goals); la malla resuelta se extraía de `Solver.O` (árbol mixto: mallas + líneas + números → `Invalid cast: Line » GeometryBase` intermitente). Fix determinístico: `ConstructMesh(V + caras)`.
  4. `Boundary Surfaces` antes del `Area` para el centroide del piso (cierra el warning naranja de `Point Deform`).
- **Verificación**: documento registrado en `DocumentServer` + solve + volcado por componente → **0 errores, 0 warnings**. (Lección: el solve headless sin registrar no computa e informa limpio en falso; el flag `Enabled` no se serializa en el `.gh`.)
- Quedó pendiente la **réplica Fig. 6 de Makert** (malla 10×10 con carga puntual en un vértice) para cuando el puente esté estable.

### C. Programa sobre el CADMapper + DXF (noche)
- **Programa oficial**: `proyectos/concurso-gaudi-nexus/03-programa-punto-a-punto.md`, hipótesis media **H1750** (A 787,5 / B 437,5 / C 262,5 / D 262,5). Primera pasada con D en 240 → corregido a exacto.
- **8 polilíneas cerradas** con m² exactos + rótulos, capas `PROG-*`, metadata y `m2` en UserText, ubicadas en la mancha libre SO del templo (templo en 490,623 h=170 m; mapa de ocupación por celdas 25 m): A-MERCADO 550 · A-VECINAL 237,5 · B-EXPO 307,5 · B-MIRADOR 130 · C-COCINA 262,5 · D-ADMIN 100 · D-LOGIST 112,5 · D-ASEOS 50 = **1750,0**.
- **DXF para AutoCAD**: `activos/proyectos/concurso-gaudi-nexus/earth2rhino3d/salidas/programa-H1750.dxf` (8 capas, 8 LWPOLYLINE cerradas suma 1750,0 + 8 TEXT, `$INSUNITS` metros). Generado offline con `ezdxf` 1.4.4 (Python 3.12) porque `sc.doc.Export` de un doc con 5600 objetos cuelga el hilo del puente MCP.
- **Dolores del puente MCP**: caídas `10061`/`10054` reiteradas; relanzamientos de Rhino con `/runscript` (dos intentos fallidos por quoting: doble backslash y flag sin comillas — forma que funciona: `/runscript="_RunPythonScript P:\...\x.py"`). Regla aprendida: nunca pedir `get_scene_info` sobre el CADMapper completo (cuelga el worker); trabajar solo con `execute` liviano + `capture`.

### D. Respuestas y doc
- Cómo ver m² de una polilínea (`Area` / Propiedades / UserText `m2`), cómo abrir Grasshopper, qué es `Sketch` según docs oficiales de McNeel (comando de dibujo a mano alzada, no un tipo de objeto).
- Trazabilidad escrita en `proyectos/concurso-gaudi-nexus/membrana-catenaria-gh.md` (+ fila en índice del concurso) con Parametric Monkey y Makert verificados 200.

## 2. Archivos modificados / creados

| Archivo | Cambio |
|---------|--------|
| `activos/.../grasshopper/membrana-catenaria.gh` | Creado y parcheado hasta v-final (36 objs, 12 sliders, 0 errores). `-v2` creado y eliminado: queda uno solo |
| `activos/.../earth2rhino3d/salidas/programa-H1750.dxf` | Nuevo (8 capas, 8 polys + 8 textos, suma 1750,0) |
| `proyectos/concurso-gaudi-nexus/membrana-catenaria-gh.md` | Nuevo: método, archivos, fuentes, reglas |
| `proyectos/concurso-gaudi-nexus/index.md` | +1 fila al doc anterior |
| `log.md` | 3 entradas del día |
| Rhino `cadmapper-...-es.3dm` | Guardado por Sol 23:46 con capas `PROG-*` + snapshot versionado en `salidas/cadmapper-programa-H1750.3dm` (par del DXF) |

## 3. Pendiente (próxima sesión)

1. ~~Guardar el `.3dm` con las capas `PROG-*`~~ Hecho por Sol 23:46 (in place + snapshot en `salidas/`).
2. Réplica Fig. 6 Makert (`fig6-malla-10x10.gh`): malla 10×10 + carga puntual en un vértice.
3. Probar el `.gh` en editor con Sol (sliders `H1–H4`, `Peso`, `Factor`, `Prof`, `idx`) y hornear `CASCARA/CAMINO/PISO` definitivos.
4. Decidir hipótesis final H1500/H1750/H2000 con Emilia.

## Análisis cerebro-digital

- **Topics**: membrana-catenaria-kangaroo · programa-H1750-sobre-plaza · dxf-ezdxf-offline · puente-mcp-inestable · verificacion-headless-real
- **Entidades**: Sol · Kangaroo2 Solver/Show/TriRemesh/Anchor/EdgeLengths/Load · CADMapper Barcelona (5599 objs, templo 170 m en 490,623) · ezdxf 1.4.4 · Parametric Monkey · Makert/Alves PPar.10335
- **Hechos**: H1750 exacto dibujado (1722,5→1750,0 tras corrección D) · .gh final 36 objs 0 errores verificados con solve registrado · DXF 8+8 verificado por lectura · puente MCP inestable ante escenas grandes y exports bloqueantes (`sc.doc.Export` cuelga el worker) · `runscript` requiere comillas exactas · Enabled no se serializa en .gh
