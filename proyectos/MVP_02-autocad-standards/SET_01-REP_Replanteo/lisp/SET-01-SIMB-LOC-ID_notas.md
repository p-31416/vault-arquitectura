---
tipo: nota
set: SET_01-REP
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, lisp, bloque, locales, atributos, planilla, autolisp, lt]
---

# Notas — `SET-01-SIMB-LOC-ID.lsp` v2 (rotulación interactiva de locales)

> Archivo: `lisp/SET-01-SIMB-LOC-ID.lsp` · AutoCAD LT 2027 · `APPLOAD`.
> v2 (20/10/2026): el bloque pasa de 0.30 × 0.20 a **0.30 × 0.30 m** y el comando
> `MK-SIMB-LOC-ID` se reemplaza por **`SIMB-LOC_ID`**, que inserta un local por
> vez y se reactiva solo para el siguiente.

## 1. Qué crea

Bloque `SIMB-LOC_ID` en la capa `A-SIMBOLO-NPT-PLANTA`:

| Elemento | Definición | Visible |
|---|---|---|
| Rectángulo | **0.30 × 0.30 m** (cuadrado), **centrado en el origen** del bloque | sí |
| `N_LOC` | atributo, alto 0.12 m, alineación centro/centro en (0,0), default `01` | **sí** (el número) |
| `TXT_LOC` | atributo, alto 0.12 m, en (0, 0.25), default vacío, flag de atributo **1 = invisible** | **no** (el nombre, sale en la planilla) |

El origen del bloque está en el **centro del rectángulo** → al insertar, el `INSERT`
queda donde apuntás y el número queda centrado. Cuadrado y no 0.30 × 0.20 porque
con dos cifras (`01`…`28`) el texto de 0.12 m necesita el ancho completo.

**Por qué el bloque no tiene prefijo `MK`**: `MK` era el nombre del *comando* v1
(`MK-SIMB-LOC-ID`, de *make*). El bloque siempre se llamó `SIMB-LOC_ID`. En la v2
el comando se llama igual que el bloque: un solo nombre.

## 2. Comandos

| Comando | Qué hace |
|---|---|
| `SIMB-LOC_ID` | **rota los locales**: pide punto → número → nombre, inserta y vuelve a activarse para el siguiente. Al salir, dispara el control de orden |
| `LOC-ID-CHECK` | control: definición del bloque, ejemplares, numeración (faltantes/repetidos) y **orden de lectura** |
| `LOC-ID-DIAG` | **diagnóstico**: qué bloques hay en el dibujo, cuáles están insertados, si el bloque existe, tamaño del rectángulo y atributos de cada local |

`MK-SIMB-LOC-ID` (v1) **ya no existe**: se lo reemplaza por `SIMB-LOC_ID`.

## 3. Uso (el flujo del día a día)

```
APPLOAD → SET-01-SIMB-LOC-ID.lsp → Load
SIMB-LOC_ID
  Punto de insercion del local <Enter = salir>:   ← click (arriba izq del local)
  Numero de local <01>:                            ← Enter (toma 01)
  Nombre del local (TXT_LOC) <>:                   ← DORMITORIO + Enter
  →  OK 01  DORMITORIO
  Punto de insercion del local <Enter = salir>:   ← click (siguiente local)
  Numero de local <02>:                            ← Enter
  Nombre del local (TXT_LOC) <DORMITORIO>:        ← Enter (repite el nombre)
  ...
  Punto de insercion del local <Enter = salir>:   ← Enter = salir
  → control automático (LOC-ID-CHECK)
```

Reglas del flujo:

- **El número viene solo** (`01`, `02`, `03`…). Si escribís otro, manda el tuyo
  (se normaliza a 2 dígitos: escribís `7` → `07`).
- **El nombre se repite**: si apretás Enter en el nombre, se usa el del local
  anterior (útil con `DORMITORIO`, `BAÑO`, `BALCON`).
- **El comando sigue vivo** entre locales: no hay que volver a invocarlo.
- Al retomar una sesión, el comando arranca en el **número siguiente al más alto
  que ya existe** en el dibujo (no duplica números).
- **Orden de clic**: de **arriba hacia abajo** y dentro de cada fila de
  **izquierda a derecha**. Es el orden de lectura y es lo que valida el control.
- Si el dibujo tiene el bloque viejo (0.30 × 0.20), el comando lo **actualiza en
  el sitio** (edita el rectángulo de la definición) → los ejemplares ya
  rotulados conservan su número y su nombre.

## 4. Control de orden de lectura (`LOC-ID-CHECK`)

Es la respuesta a *"¿de verdad se puede chequear que estén bien numerados en X+ / Y−?"*: **sí**.

El control hace, con el mismo criterio que `scripts/ordena-locales.py`:

1. Toma todos los ejemplares de `SIMB-LOC_ID` y su punto de inserción.
2. **Arma las filas**: dos locales son de la misma fila si la diferencia de Y es
   menor a **0.30 m** (tolerancia de fila). Las filas se ordenan de arriba hacia
   abajo (Y decreciente).
3. **Ordena cada fila de izquierda a derecha** (X creciente).
4. **Compara** esa secuencia de posiciones contra el `N_LOC` de cada bloque: el
   local que cae en la posición *i* debería llevar el número *i*.

Salida:

```
--- Orden de lectura (X+ / Y-, filas con dY < 0.30 m) ---
  OK: los 28 locales estan en orden de lectura.
```

o, si algo quedó mal:

```
  FUERA DE ORDEN: el local 08 (DORMITORIO) en (20.99, -3.06) le corresponde el 07
  FUERA DE ORDEN: el local 07 (BALCON) en (-1.32, -5.26) le corresponde el 08
```

También avisa: números repetidos, números faltantes, locales sin nombre y
locales que no entraron en ninguna fila (a más de 0.30 m del resto de su fila).

> **Dato de contraste con el estado anterior**: los rótulos viejos (`*U323` /
> `*U324`, atributos `DESCRIPCION` y `N`) **no** cumplían el orden de lectura:
> faltan el `07`, hay un `12` duplicado y en orden de lectura sus números salen
> `00, 15, 02, 16, 14, 03, 01, 18, 04, …`. El bloque nuevo lo corrige: el
> comando numera solo y en orden de lectura.

## 5. Cómo está hecho (para leerlo)

El LSP está en AutoLISP puro (sin Visual LISP, sin ActiveX), porque **AutoCAD LT
no expone COM ni ActiveX hacia afuera**: todo el control tiene que vivir
dentro del DWG.

| Parte | Qué hace | Para qué |
|---|---|---|
| `SET-L:*` (constantes) | capa, nombre de bloque, 0.30 × 0.30, alto 0.12, tolerancia 0.30 | los parámetros que se tocan están todos arriba |
| `SET-L:Num2` | `1 → "01"` | dos dígitos siempre |
| `SET-L:OrdenaX` / `SET-L:OrdenaDesc` | ordenamientos escritos a mano (inserción ordenada) | AutoLISP no tiene `sort`; y `vl-sort` no está garantizado en LT |
| `SET-L:Filas` | arma las filas (ΔY < 0.30) y las ordena por X | el corazón del control de orden |
| `SET-L:LocalesDelDibujo` | lee los ejemplares: `N_LOC`, `TXT_LOC`, punto | alimentar el control |
| `SET-L:CreaBloque` | `entmake` de `BLOCK` + `LWPOLYLINE` + 2 `ATTDEF` + `ENDBLK` | el símbolo |
| `SET-L:ActualizaRect` | `entmod` de la `LWPOLYLINE` | pasar de 0.30 × 0.20 a 0.30 × 0.30 sin perder los ejemplares |
| `SET-L:InsertaLocal` | `entmake` de `INSERT` + 2 `ATTRIB` | el local |
| `SET-L:Atributos` / `SET-L:ValorAttr` | leen los atributos de un `INSERT` | `(entget)` de un bloque con atributos trae los `ATTRIB` embebidos después del grupo 66 |

### El patrón de `entmake` con atributos (lo importante)

```lisp
(entmake
  (append
    (list '(0 . "INSERT") ... '(66 . 1))   ; 66 = 1 → "siguen atributos"
    (list '(0 . "ATTRIB") ... '(66 . 1))  ; primer atributo: hay otro atrás
    (list '(0 . "ATTRIB") ... '(66 . 0)))) ; último atributo: fin de la serie
```

- El **grupo 66** en el `INSERT` avisa que la serie de atributos sigue; el
  `66 = 0` del último atributo la cierra (patrón oficial de AutoCAD).
- El **orden de los atributos** define el orden en que AutoCAD los pregunta al
  insertar: `N_LOC` primero, `TXT_LOC` después.
- Los atributos se posicionan en **WCS** (coordenadas de mundo): el código 10
  del `ATTRIB` no es relativo al origen del bloque, es el punto absoluto. Por
  eso `SET-L:PuntoWCS` suma el punto de inserción al offset local del bloque
  (0,0) para el número y (0, 0.25) para el nombre.
- El atributo **invisible** se marca con el **flag 70 = 1** en el `ATTDEF`:
  no se ve ni se imprime, pero el dato queda guardado en el DWG y sale en la
  extracción.

### Atajo de los números de dos cifras

Con alto de texto 0.12 m, el ancho de un dígito ≈ 0.6 × 0.12 = 0.072 m; dos
dígitos ≈ 0.15 m. Entran cómodo en los 0.30 m de lado del cuadrado, y hasta
tres dígitos entrarían.

## 6. Prueba en sesión (no se puede automatizar desde afuera)

LT no expone COM → el MCP `autocad` del vault no llega. La prueba es tuya, en
la sesión de AutoCAD LT 2027.

| # | Paso | Qué hay que ver |
|---|---|---|
| 1 | `APPLOAD` → `SET-01-SIMB-LOC-ID.lsp` → *Load* | `SET-01-SIMB-LOC-ID.lsp v2 cargado. Comandos: SIMB-LOC_ID, LOC-ID-CHECK` |
| 2 | `SIMB-LOC_ID` | `Bloque SIMB-LOC_ID creado: rectangulo 0.30 x 0.30 m.` y el primer prompt de punto |
| 3 | click + Enter + `PRUEBA` + Enter | `OK 01  PRUEBA` y el rectángulo 0.30 × 0.30 con el `01` centrado |
| 4 | click + Enter + Enter | `OK 02  PRUEBA` (repite el nombre) |
| 5 | Enter (salir) | control automático: lista de 2 locales, `OK: los 2 locales estan en orden de lectura` |
| 6 | `U` (deshacer) hasta borrar los 2 de prueba, `Q` | limpio para empezar de verdad |

Si en el paso 3 el comando no aparece: `SECURELOAD` / `TRUSTEDPATHS`.

## 7. Troubleshooting

| Síntoma | Causa | Solución |
|---|---|---|
| `Comando desconocido` al escribir `SIMB-LOC_ID` | el LSP no cargó | `APPLOAD` de nuevo; el archivo debe estar en `TRUSTEDPATHS` (o usar *Cargar al inicio*) |
| `Seguridad: no se puede cargar` | `SECURELOAD` con carpeta no confiable | `OPCCIONES → Archivos → Ubicaciones de confianza` → agregar la carpeta del `.lsp` |
| `AutoCAD LT 2023` o anterior | AutoLISP no existe en LT antes de 2024 | usar LT 2024+ (acá tenés 2027) |
| `ERROR: no se pudo crear el local ... (entmake devolvio nil)` | el `entmake` con atributos fue rechazado | plan B: insertar a mano con `INSERTAR` → `SIMB-LOC_ID` (el bloque tiene los atributos definidos, los tipea AutoCAD) y después `LOC-ID-CHECK` |
| El número no avanza | se escribió a mano un valor | el control lo marca como `FUERA DE ORDEN` |
| El rectángulo sigue 0.30 × 0.20 | el bloque del dibujo es el viejo y tiene otros ejemplares | el comando lo actualiza solo; si no, `BLOQUE → Editar` y cambiar el rectángulo |
| Faltan locales en el control | están a más de 0.30 m del resto de su fila | el control los lista como "no entraron en ninguna fila" |
| "No existe el bloque SIMB-LOC_ID" | la definición no llegó a crearse (o quedó a medias) | `LOC-ID-DIAG` muestra qué hay en el dibujo; si el bloque está roto: `BLOQUE → Borrar` (o `P purge`) y volvés a correr `SIMB-LOC_ID` |

## 7.1 v2.1 / v2.2 — qué cambió y por qué

**Lo que pasó en la primera corrida en AutoCAD LT (20/10)**: el comando insertó
1 local pero el `LOC-ID-CHECK` respondió *"No existe el bloque SIMB-LOC_ID"*: la
definición **no había quedado registrada** en la tabla de bloques. En la v2.1 y
v2.2 el LSP quedó así:

1. **Verifica cada `entmake`**: `SET-L:EntmakeOK` / `entmakex` avisa qué entidad
   no aceptó AutoCAD (BLOCK, LWPOLYLINE, ATTDEF, ENDBLK) en vez de seguir
   como si nada.
2. **Confirma el registro** del bloque con `tblobjname` antes de rotular.
3. **Plan B sin `entmake` de bloque**: si AutoCAD no acepta el `BLOCK`, el
   bloque se arma con el **comando `-BLOCK`** (que sí funciona en LT): se dibuja
   el rectángulo y los dos `ATTDEF` en un área de trabajo lejana del plano
   (1000, 1000), se meten en el bloque por ventana de selección y la geometría
   de trabajo se borra. Si el bloque ya existe, responde *"Sí"* a redefinirlo.
4. **Nunca borra la definición**: `entdel` sobre el registro de un bloque no
   libera el nombre (queda ocupado hasta el PURGE) → si la definición está
   dañada, la rehace con `-BLOCK`; si tampoco puede, avisa y para.
5. **Inserción con `entappend`** (patrón oficial): se crea el `INSERT` y se le
   asocian los dos `ATTRIB` con `entappend` (la referencia de bloque es el padre
   del atributo). Es más robusto que meter el `INSERT` y los `ATTRIB` en una
   sola lista de `entmake`.
6. **El comando no sigue si el bloque no está**: el `exit` no cortaba la
   ejecución y el comando seguía prompting con el bloque inexistente (por eso
   "insertaba" sin que apareciera nada). Ahora corta limpio y avisa.
7. **La definición del bloque va en la CAPA 0** (criterio del estudio): así el
   bloque insertado **toma la capa de inserción** (`A-SIMBOLO-NPT-PLANTA`),
   que es la convención de AutoCAD. El `INSERT` va en la capa del proyecto.
8. **Registro de la sesión** (`SET-L:LOG`): cada paso se anota y se escribe en
   `raw/reports/loc-id-log.txt`; el diagnóstico (`LOC-ID-DIAG`) lo incluye en
   `raw/reports/loc-id-diag.txt` → se puede revisar **desde afuera** de AutoCAD
   sin depender de la pantalla.

## 7.2 Cómo se carga (la vía corta)

En la carpeta de soporte de AutoCAD LT
(`%APPDATA%\Autodesk\AutoCAD LT 2027\R33\enu\Support\`) está el cargador
`SET-01-LOAD.lsp`, que hace tres cosas:

```lisp
(load "P:/.../SET-01-SIMB-LOC-ID.lsp")   ; carga el LSP canonico del vault
(SET-L:AseguraBloque)                   ; crea/repara el bloque
(LOC-ID-DIAG)                            ; escribe el diagnostico
```

En AutoCAD alcanza con escribir:

```
(load "SET-01-LOAD.lsp")
```

(así se evita pegar la ruta larga del vault).

**Plan B (el `entmake` falla)**: el bloque ya queda creado con sus `ATTDEF`
(`N_LOC` y `TXT_LOC`), así que `INSERTAR` → `SIMB-LOC_ID` funciona igual: pide
el número y el nombre. Es más tedioso (28 inserts a mano, sin autoincremento),
pero no se pierde nada.

## 8. Lo que NO hace

- **No toca los rótulos viejos** (`*U323` / `*U324` con `DESCRIPCION` y `N` en
  `A-SIMBOLO-NPT-PLANTA`): quedan conviviendo con los bloques nuevos hasta que
  el estudio los apague o borre a mano.
- No genera la planilla ni dibuja el cuadro de locales dentro del DWG (esa
  herramienta, `CUADRO-LOCALES`, es un LSP aparte que todavía no existe).
- No ordena ni renumera: el control **informa**, corregir es decisión del
  estudio.

## 9. Referencias oficiales (verificadas 20/10/2026)

- AutoLISP en AutoCAD LT (disponible desde LT 2024) + `APPLOAD`: https://help.autodesk.com/view/ACDLT/2027/RUS/?guid=GUID-5FB57480-C9BE-4E3D-BEDF-D86035928FFA
- LT 2023 y anteriores no soportan AutoLISP (`APPLOAD` = *Comando desconocido*): https://www.autodesk.com/es/support/technical/article/caas/sfdcarticles/sfdcarticles/ESP/Unable-to-load-lisp-in-AutoCAD-LT.html
- Crear/cargar un `.lsp` (tutorial oficial): https://help.autodesk.com/view/ACDLT/2027/PLK/?guid=GUID-3B8EDFF1-A130-434F-B615-7F2EC04322EE
- Atributos: definición, asociación y **modos** (invisible / constante / verificar): https://help.autodesk.com/view/ACD/2027/PTB/?guid=GUID-67A2DDAD-2217-412F-8AEF-D4495192F45B
- `entmake` (grupo 66 honored only for insert objects) + objetos no soportados en LT: https://help.autodesk.com/view/OARX/2027/RUS/?guid=GUID-D47983BA-1E5D-417D-85B8-6F3DE5F506BA
- Códigos de grupo de `INSERT` (66 = siguen atributos): https://help.autodesk.com/view/OARX/2027/ESP/?guid=GUID-28FA4CFB-9D5E-4880-9F11-36C97578252F
- Códigos de grupo de `ATTRIB` (70 = flags, 1 = no visible): https://help.autodesk.com/view/OARX/2027/ESP/?guid=GUID-7DD8B495-C3F8-48CD-A766-14F9D7D0DD9B

## 10. Archivos relacionados

| Archivo | Qué |
|---|---|
| `scripts/ordena-locales.py` | calcula el orden de lectura desde el DWG (mismo criterio) y con `--check` verifica la numeración **fuera** del CAD · `C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\ordena-locales.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" --check` (el `ezdxf` vive en ese Python 3.12 del sistema, no en `comfyenv`) |
| `docs/orden-locales.md` / `.csv` | los 28 locales en 16 filas, con el orden de inserción |
| `docs/cuadro-locales.md` / `.csv` | planilla de locales (`N_LOC` / `TXT_LOC` / X / Y) |
| `scripts/chequea-lisp.py` | valida que el `.lsp` tenga los paréntesis balanceados |
