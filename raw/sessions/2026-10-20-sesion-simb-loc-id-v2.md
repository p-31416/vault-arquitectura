---
tipo: sesion
proyecto: estudio-pi
mvp: 02
set: SET_01-REP
software: [autocad, autocad-lt, autolisp, oda, ezdxf]
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [sesion, mvp_02, rep-araoz, replanteo, lisp, locales, atributos, orden-lectura, autolisp, lt]
---

# Sesión 2026-10-20 — `SIMB-LOC_ID` v2: rotulación interactiva de locales + control de orden de lectura

## 1. Qué se hizo

1. **Reformulación del bloque de locales**: el estudio rota los locales a mano con un comando (número automático, se reactiva para el siguiente) en vez de 28 `INSERT` manuales.
2. **Reescritura de `lisp/SET-01-SIMB-LOC-ID.lsp`** (v2):
   - rectángulo del bloque **0.30 × 0.30 m** (cuadrado; el v1 era 0.30 × 0.20 → con 2 cifras a alto 0.12 m el texto no holgaba),
   - comando **`SIMB-LOC_ID`** (nuevo): pide punto → número → nombre, inserta y **vuelve a activarse solo** para el local siguiente; el nombre se repite con Enter; el número se autocompleta (`01`…`28`) y se puede pisar; al salir dispara el control,
   - `MK-SIMB-LOC-ID` **eliminado** (el prefijo "mk" venía del comando *make*, nunca del bloque),
   - `LOC-ID-CHECK` v2: control de la definición del bloque + **orden de lectura** (X creciente / Y decreciente, filas con ΔY < 0.30 m) contrastado contra el `N_LOC` de cada ejemplar.
3. **Auditoría de la numeración del DWG** (28 rótulos leídos del `REP-ARAOZ.dwg`): la numeración legacy de los rótulos viejos **no** cumple el orden de lectura (falta el `07`, hay un `12` duplicado, y en orden de lectura sus números salen `00, 15, 02, 16, 14, 03, 01, 18, 04, …`) → 28 de 28 fuera de orden. El bloque nuevo lo corrige.
4. **Simulación del algoritmo de control** (LISP y Python) contra los 28 locales reales: numeración correcta → 0 desvíos; `07`↔`08` intercambiados → 2 desvíos con el mensaje correcto.
5. **Modo `--check` de `scripts/ordena-locales.py`**: verifica la numeración **fuera** del CAD (mismo criterio que el LISP).
6. **Notas v2** (`lisp/SET-01-SIMB-LOC-ID_notas.md`): flujo de uso, patrón `entmake` con atributos, control de orden, plan B si `entmake` es rechazado, troubleshooting, referencias oficiales verificadas.
7. **Incidente en la primera corrida en AutoCAD LT** (v2.1): el comando insertó 1 local pero el control respondió *"No existe el bloque SIMB-LOC_ID"* → la definición no había quedado registrada en la tabla de bloques. Se endureció el LSP: verificación de cada `entmake`, confirmación del registro con `tblobjname`, `AseguraBloque` que **nunca borra** la definición (antes la borraba y dejaba el nombre ocupado → dibujo sin bloque), `InsertaLocal` que verifica que el bloque exista, `LOC-ID-CHECK` que no aborta si hay ejemplares sin definición, y **nuevo `LOC-ID-DIAG`** para volcar el estado real del dibujo.
8. **Diagnóstico del v2.2** (con captura de la línea de comandos de AutoCAD LT 2027, vía `PrintWindow`): el comando prompting bien (punto → número → nombre) pero **nada se insertaba**. Tres causas: (a) `entmake` del `BLOCK` no lo acepta AutoCAD LT, (b) el `exit` del comando **no cortaba** → seguía pidiendo puntos con el bloque inexistente y el `INSERT` quedaba colgado, (c) el patrón `INSERT`+`ATTRIB` en una sola lista no es robusto. Correcciones: **plan B con el comando `-BLOCK`** (geometría de trabajo en (1000,1000) + ventana de selección), **asociación de atributos con `entappend`**, el comando **corta limpio** si el bloque no está, **definición del bloque en la CAPA 0** (criterio del estudio: el bloque insertado toma la capa de inserción `A-SIMBOLO-NPT-PLANTA`) y **registro de la sesión** (`SET-L:LOG` → `raw/reports/loc-id-log.txt`, incluido en el diagnóstico).
9. **Planilla de niveles** (dato del estudio): se creó `lisp/SET-01-CUADRO-NIVELES.lsp` (comando `CUADRO-NIVELES`: dibuja la tabla MTEXT + LINE en la capa `A-CUADRO-NIVELES`, con alto de fila automático según el espacio) + notas + `docs/planilla-niveles.md`/`.csv`. Se cerró la tarea "planilla de niveles que el estudio transcribe" del log anterior.

## 2. Archivos creados / modificados

| Archivo | Qué |
|---|---|
| `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/lisp/SET-01-SIMB-LOC-ID.lsp` | v2: rect 0.30 × 0.30, `SIMB-LOC_ID` interactivo, `LOC-ID-CHECK` con control de orden |
| `.../lisp/SET-01-SIMB-LOC-ID_notas.md` | notas v2 (didácticas + troubleshooting + fuentes) |
| `scripts/ordena-locales.py` | modo `--check` (verifica numeración vs orden de lectura, no escribe archivos) + línea de control en el `.md` generado |
| `proyectos/MVP_02-autocad-standards/03-log-mvp_02.md` | entrada de bitácora (al principio) |
| `raw/sessions/2026-10-20-sesion-simb-loc-id-v2.md` | esta sesión |

## 3. Cerebro digital

**Topics**: rotulación interactiva de locales · autoincremento de atributos · `entmake` de `INSERT` + `ATTRIB` con grupo 66 · atributos invisibles (flag 70 = 1) · geometría compartida de bloque (actualizar el rectángulo con `entmod` en vez de recrear y perder ejemplares) · AutoLISP puro sin Visual LISP (compatibilidad LT) · orden de lectura (X+ / Y−) como criterio de numeración · control automático dentro del DWG (LT no tiene COM ni `DATAEXTRACTION`).

**Entidades**: `SIMB-LOC_ID` · `N_LOC` (visible) · `TXT_LOC` (invisible) · `A-SIMBOLO-NPT-PLANTA` · `*U323` / `*U324` (rótulos legacy) · `LOC-ID-CHECK` · `SET-01-SIMB-LOC-ID.lsp` · `scripts/ordena-locales.py --check` · AutoCAD LT 2027 · ODA File Converter 25.12.

**Hechos (verificados)**:
- **AutoCAD LT 2027 sí tiene `APPLOAD`**: AutoLISP está disponible en AutoCAD LT **desde la versión 2024** (help oficial ACDLT 2027). En LT 2023 y anteriores `APPLOAD` = *Comando desconocido*; AutoLISP no existe en LT for Mac.
- El grupo **66** de `INSERT` se honra solo para inserts ("attributes follow") y el `66 = 0` del último atributo cierra la serie (patrón oficial de `entmake` con atributos).
- Los atributos se posicionan en **WCS**: el código 10 del `ATTRIB` es absoluto, no relativo al origen del bloque.
- En `entget` de un bloque con atributos, los `ATTRIB` vienen **embebidos** en la lista después del grupo 66 → se leen con `assoc 0` = `"ATTRIB"`.
- La numeración legacy del DWG (atributo `N` de los rótulos) tiene 28 valores entre `00` y `28` con el `07` ausente y el `12` duplicado, y **no sigue el orden de lectura** (28/28 fuera de orden).
- `ezdxf` **no está en `P:\Anaconda\envs\comfyenv`** (ni en el Python base de Anaconda): ese env es de ComfyUI. Está en el **Python 3.12 del sistema** (`C:\Users\Solch16\AppData\Local\Programs\Python\Python312`, ezdxf 1.4.4) → los scripts de CAD (`ordena-locales.py`, `extrae-atributos-dwg.py`) se corren con ese intérprete, no con `comfyenv`. Verificado: `ordena-locales.py --check` sobre el `REP-ARAOZ.dwg` real → 28 locales en 16 filas, fuente = rótulos legacy (el control de orden no aplica hasta que existan ejemplares de `SIMB-LOC_ID`).
- La instalación real es **AutoCAD LT 2027** (`C:\Program Files\Autodesk\AutoCAD LT 2027`); el MCP `autocad` del vault (COM) no llega a LT → la prueba del LSP es manual, en sesión.
- **LT 2027 con `SECURELOAD = 1` y `TRUSTEDPATHS` vacío** (registro `HKCU\Software\Autodesk\AutoCAD LT\R33\ACADLT-A101:409\Profiles\<<Unnamed Profile>>\Variables`): al cargar el `.lsp` desde `P:\...` salta el aviso *"Ruta de búsqueda de archivo conf."* → hay que contestar Sí/Continuar (o agregar la carpeta a *Ubicaciones de confianza*).
- **`entdel` sobre el registro de un bloque no libera el nombre**: la definición queda marcada y el nombre sigue ocupado hasta el PURGE → por eso `SET-L:AseguraBloque` (v2.1) **no borra** la definición en ningún caso.
- La v2.1 además verifica **cada `entmake`** (qué entidad no aceptó AutoCAD), confirma el **registro** del bloque con `tblobjname` antes de insertar, y trae `LOC-ID-DIAG` para volcar el estado real del dibujo.
- **AutoCAD LT no acepta el `entmake` de un bloque `BLOCK`** (o no lo registra): la vía que funciona es el **comando `-BLOCK`** (dibujar la geometría en un área de trabajo y meterla por ventana de selección). En LT no hay COM ni ActiveX → todo el control va en AutoLISP.
- **`exit` dentro de un `defun` no corta la ejecución** del comando: usaba `(exit)` para abortar y el `SIMB-LOC_ID` seguía prompting con el bloque inexistente (por eso "insertaba" y no se veía nada). Ahora el comando corta con un flag.
- **`entdel` sobre el registro de un bloque NO libera el nombre**: la definición queda marcada y el nombre sigue ocupado hasta el PURGE → `AseguraBloque` no borra la definición en ningún caso.
- **AutoCAD LT 2027 con `SECURELOAD = 1` y `TRUSTEDPATHS` vacío** → al cargar un `.lsp` desde `P:\...` salta el aviso *"Ruta de búsqueda de archivo conf."* → hay que contestar Sí/Continuar.
- Se puede **capturar la línea de comandos de AutoCAD sin mandarle teclas** con la API `PrintWindow` (flag 2) → sirve para leer el estado real de la sesión desde la terminal. `SetForegroundWindow` no funciona (Windows lo bloquea) y `Ctrl+V` en AutoCAD es `PASTECLIP` (pegar objeto), no pegar texto.

## 4. Pendientes

- [ ] **Probar en AutoCAD LT** (no se puede automatizar): `APPLOAD` → `SIMB-LOC_ID` → 2 locales de prueba → `LOC-ID-CHECK` → deshacer. Checklist en las notas §6.
- [ ] **Diagnóstico de la primera corrida**: `LOC-ID-DIAG` en el DWG de la sesión → ver si `SIMB-LOC_ID` quedó en la tabla de bloques y qué hay insertado; si el bloque quedó a medias, `BLOQUE → Borrar` (o `P purge`) y volver a correr `SIMB-LOC_ID`.
- [ ] **Decidir qué se hace con el local de prueba** que quedó insertado (el que el estudio insertó en la primera corrida) → borrar con `U` o `E` antes de rotular los 28.
- [ ] **Rotular los 28 locales** en el orden de lectura de `docs/orden-locales.md` (filas de arriba hacia abajo, izq→der).
- [ ] Decidir qué se hace con los rótulos legacy `*U323`/`*U324` (hoy no se tocan: conviven con los bloques nuevos en la misma capa).
- [ ] Verificar la numeración **fuera** del CAD (una vez insertados los 28): `C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\ordena-locales.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" --check` → debe dar `OK: los 28 locales estan en orden de lectura`.
- [ ] `lisp/SET-01-CUADRO-LOCALES.lsp` (comando `CUADRO-LOCALES`): CSV + tabla dibujada dentro del DWG (LT no tiene `DATAEXTRACTION`).

## 5. DÓNDE QUEDAMOS — para retomar

**Decisiones del estudio (20/10, esta sesión):**
- **28 locales** (no 24), numeración `01`…`28` **con cero**, en **orden de lectura** (X+ / Y−).
- Los rótulos legacy **no se tocan**.
- `MK-SIMB-LOC-ID` **eliminado**: el comando es `SIMB-LOC_ID`, igual que el bloque.

**Cómo se usa (lo que corre el estudio):**

| Paso | Comando | Qué |
|---|---|---|
| 1 | `APPLOAD` → `SET-01-SIMB-LOC-ID.lsp` | carga (LT 2027 lo soporta) |
| 2 | `SIMB-LOC_ID` | click en cada local **de arriba hacia abajo, izq→der**; Enter en el nombre = repite el anterior; Enter en el número = usa el automático |
| 3 | Enter (salir) | dispara el control: lista de locales + `OK: los 28 locales estan en orden de lectura` |
| 4 | `LOC-ID-CHECK` | control manual cuando haga falta (numera, nombres, orden) |

**Si algo sale mal:** el control dice exactamente qué local está fuera de orden y cuál le corresponde; y si el `entmake` con atributos es rechazado, el plan B es `INSERTAR` → `SIMB-LOC_ID` a mano (el bloque ya tiene los `ATTDEF` definidos).

**Siguiente paso al retomar:** probar el LSP en AutoCAD LT con 2 locales de prueba y, si el `entmake` funciona, rotular los 28 en el orden de `docs/orden-locales.md`.
