---
tipo: nota
set: SET_01-REP
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, lisp, atributos, giro, muros, carpinteria, columnas]
---

# Notas — `SET-01-NORM-TEXTOS.lsp` (giro de los textos de bloque)

> Archivo: `lisp/SET-01-NORM-TEXTOS.lsp` · `APPLOAD` · comandos `NORM-TEXTOS` y `NORM-LOCALES`.

## 1. Qué resuelve

El texto que vive **dentro** de un bloque (código de muro, número de vano, medida de columna) gira con el bloque cuando el bloque se inserta con ángulo. Corregirlo ejemplar por ejemplar es lo que se venía haciendo a mano.

Este comando lo resuelve de una, **sin mover los bloques**:

1. a cada `ATTRIB` le deja el **giro en 0°** → el texto queda horizontal en el modelo,
2. le **bloquea la posición** (bit 16 del grupo 70) → de ahí en más no vuelve a girar ni a moverse con el bloque.

## 2. Estado medido del archivo (20/10, guardado por el estudio)

| Capa | Bloques | Atributos | Con giro ≠ 0 |
|---|---|---|---|
| `SIMB-MURO` | 95 | 95 | **79** (90° 16 · 180° 22 · 270° 41) |
| `A-CARP-02` | 41 | 41 | **33** (90° 14 · 180° 3 · 270° 16) |
| `E-COL` | 21 | 21 | **17** (90° 7 · 180° 4 · 270° 6) |

Y 2 rótulos de locales fuera de norma: uno en 270° y otro en 180° (`ASCENSOR I`).

## 3. Uso

1. `APPLOAD` → `SET-01-NORM-TEXTOS.lsp` → *Load*
2. `NORM-TEXTOS` → informe por capa (bloques, atributos, cuántos con giro) → pide confirmación
3. `NORM-LOCALES` → deja en 0° los rótulos de local girados
4. `REGEN` / `REGENERAR` para ver el resultado; `UNDO` para volver atrás

## 4. Advertencias

- **No mueve nada**: solo cambia el giro y el bloqueo del texto. La geometría del bloque (la hoja de la puerta, la flecha del muro) sigue girando con el bloque — que es lo correcto.
- **Con la posición bloqueada**, si después hay que mover el bloque, el texto se queda en el lugar viejo: hay que moverlo a mano o desbloquearlo.
- **El giro 0 es respecto del modelo**: como el viewport `1EC35` de `REP-PTipo-A1-H` quedó con twist 360 (= 0), el texto se lee horizontal también en la lámina. Si un día se gira el viewport, hay que compensar (ver `SET-01-HORIZ.lsp`).
- No se puede probar desde acá: AutoCAD LT no expone COM (doc oficial ACDLT 2027) → se verifica en la sesión con el informe del comando.
