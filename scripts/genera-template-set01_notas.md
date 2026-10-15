# Notas didácticas — `genera-template-set01.py`

> Cómo leer este script si estás aprendiendo Python: cada bloque comentado con
> `# NOTA ES:` explica qué hace y por qué, en tu idioma.

## Qué hace

1. Crea un dibujo DXF nuevo (`ezdxf.new("R2018")`) con unidades en **metros**
   (`$INSUNITS = 6`), sistema métrico y formato decimal 2 decimales.
2. Crea las **28 capas** del SET con color ACI, tipo de línea y estado
   (congelada/bloqueada) medidos en `REP-ARAOZ.dwg`. `Defpoints` no se crea:
   la genera AutoCAD sola.
3. Crea los **8 estilos de texto** con fuente, altura y ancho medidos.
4. Crea las **puntas de flecha** `_ArchTick` y `_Open90` como bloques mínimos
   (un tick y una flecha abierta) y los **2 dimstyles** que las usan.
5. Guarda en `%TEMP%\SET_01-REP_base.dxf`. De ahí, ODA File Converter lo pasa
   a DWG y se copia a `.dwt` (plantilla) y `.dws` (norma) en `activos/`.

## Por qué DXF + ODA

`ezdxf` solo escribe DXF. ODA traduce fiel a DWG (formato ACAD2018, que abre
LT y completo). `.dwt` y `.dws` son contenedores DWG con otra extensión.

## Limitaciones honestas

- Los tipos de línea `DASHDOTX2` quedan como aproximación simple (el complejo
  con texto de AutoCAD se define en la PC destino o se importa del DWG base).
- El layout `REP-PTipo-A1`, viewport, CTB y PC3 se crean en la PC de Emilia
  con el instructivo (5–10 min), porque dependen de impresora y papel.
