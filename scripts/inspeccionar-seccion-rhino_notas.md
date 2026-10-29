# Notas — `inspeccionar-seccion-rhino.py`

Script **de solo lectura** que se ejecuta **dentro de Rhino 8** para diagnosticar por qué el
corte 3D se ve **sin hatch** en el detalle de la lámina, aunque en la vista de trabajo el
mismo corte sí muestre la trama por material.

## Cómo se usa

En la **línea de comandos de Rhino 8** (no en la terminal):

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\inspeccionar-seccion-rhino.py"
```

El informe sale por la línea de comandos de Rhino. Para tenerlo en texto y poder pegarlo en el
vault, la vía cómoda es el **puente MCP**: con el puente levantado, el mismo script se puede
ejecutar desde el asistente y el resultado vuelve como texto.

Alternativa sin abrir Rhino: leer el `.3dm` con la librería `rhino3dm` (openNURBS) desde
Anaconda. **No está instalada** en este equipo y no hace falta: `rhino3dm` lee geometría y
capas, pero **no** expone los Estilos de sección ni los ajustes de los modos de visualización,
que es justamente lo que hay que revisar.

## Qué mira y por qué

| Bloque | Qué lee | Por qué importa |
|---|---|---|
| 1. Planos de corte | cantidad, capa, geometría y **todas** sus propiedades | el *Section Style* del plano decide si el relleno viene de la capa (`By Layer`) o del plano (`Custom`) |
| 2. Capas | color de impresión, ancho y **Estilo de sección** | la **escala del patrón** de la trama: si el patrón mide 1 mm en el modelo, en la lámina a 1:30 mide 0,03 mm → invisible |
| 3. Objetos por tipo | cuántos hay y cuántos son **cerrados** | el manual dice: la sección se rellena solo "when a clipping plane intersects a 3-D object **and the section is closed**" → una malla o una superficie abierta no se rellenan |
| 4. Vistas y detalles | lámina, nombre del detalle, **modo de visualización**, cámara y escala | el detalle tiene su **propio** modo de visualización: ahí pueden estar apagados *Show fills* y *Use section styles* |
| 5. Ajustes de los modos | dónde viven *Show fills* y *Use section styles* | sin *Use section styles* el relleno sale con un color genérico en vez de la trama del material |

## Las tres hypotheses que este script separa

1. **El modo del detalle** no es el mismo que el de la vista de trabajo, o en ese modo están
   apagados *Show fills* / *Use section styles*.
2. **La escala del patrón de la trama** es la del modelo: en la lámina (a 1:30) el patrón se
   reduce 30 veces y deja de leerse → hay que subir la *Pattern Scale* para que la trama mida
   unos milímetros en el papel.
3. **Los objetos no son sólidos cerrados** (son mallas o superficies abiertas): entonces no
   hay sección que rellenar.

## Notas de código (para aprender)

- `P(texto)` centraliza la impresión: todo el informe se arma en la lista `LINEAS` y se
  devuelve con `return`, así el mismo script sirve para imprimir en Rhino o para mandar el
  texto por otro canal.
- `seguro(fn, defecto)` envuelve cada consulta: la API de RhinoCommon cambia entre versiones
  y un atributo que no exista en esta versión no debe cortar el informe.
- `volcar_interesante(objeto, palabras, titulo)` recorre `dir(objeto)` y vuelca los atributos
  cuyo nombre contiene alguna palabra clave. Es la forma robusta de preguntar "¿qué
  propiedades tiene esto?" sin saber de antemano cómo se llaman.
- `obj.ObjectType == Rhino.DocObjects.ObjectType.ClipPlane` es cómo se detectan los planos
  de corte.
- El script **no** llama a `doc.Modify()`, ni agrega, borra o mueve nada: es de lectura.

## Verificación hecha

- Escrito y verificado como sintaxis de Python 3 (compatible con IronPython 2.7: no usa
  f-strings, ni anotaciones, ni `match`).
- **No ejecutado todavía**: requiere el puente MCP levantado o el `_RunPythonScript` manual
  dentro de Rhino.
