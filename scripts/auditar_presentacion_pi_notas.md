---
tipo: software
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [pi, presentacion, remotion, auditoria, python, tutorial]
idioma: es
---

# Notas didácticas — `auditar_presentacion_pi.py`

## Cómo ejecutarlo

Desde la raíz del vault, cuando quieras comprobar los archivos:

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\auditar_presentacion_pi.py
```

El script es **solo lectura**: revisa que existan la página, el guion y la composición Remotion; compara los MCP habilitados con el inventario esperado; y busca frases ancla para detectar omisiones de contenido. Código de salida `0` significa listo para vista previa; `1` indica que hay algo que revisar.

## Recorrido línea por línea

| Línea(s) del `.py` | Qué hace | Idea de Python |
|---:|---|---|
| 1 | Resume el propósito en la docstring del módulo. | La docstring es la descripción que `help()` muestra para un archivo/módulo. |
| 3–5 | Activa anotaciones futuras e importa JSON y `Path`. | `json` lee el archivo de configuración; `Path` arma rutas sin concatenar cadenas a mano. |
| 9–10 | Calcula la raíz del vault a partir de la ubicación del script. | `__file__` es la ruta del `.py`; `parents[1]` sube desde `scripts/` al vault. |
| 12–13 | Define la ruta conocida del repo de Remotion. | Una ruta cruda `r"..."` evita que `\` se interprete como escape. |
| 15–24 | Guarda el conjunto de ocho MCP esperados. | Un `set` facilita diferencia de conjuntos y evita duplicados. |
| 27 | Declara `auditar_archivos`, que devuelve `True` o `False`. | Una función reúne una verificación para poder repetirla y leerla aparte. |
| 29–35 | Relaciona cada nombre con su ruta y muestra `OK` o `FALTA`. | Un diccionario une etiquetas legibles con objetos `Path`. |
| 36–41 | Acumula el resultado de cada existencia. | `and` mantiene el resultado falso si falta cualquier archivo. |
| 44 | Declara la verificación del inventario MCP. | El retorno booleano permite combinarla después con otras auditorías. |
| 46–47 | Abre y parsea `opencode.json` como UTF-8. | `utf-8-sig` también acepta un BOM si el editor lo guardó así. |
| 48–52 | Extrae las entradas con `enabled: true`. | Comprensión de conjunto: filtra y construye una lista única en una expresión. |
| 53–54 | Calcula MCP que faltan y MCP adicionales. | `A - B` devuelve elementos que están en un conjunto y no en el otro. |
| 55–59 | Informa diferencias sin mostrar cabeceras ni valores secretos. | El script imprime nombres MCP, nunca credenciales de los encabezados. |
| 62 | Declara la auditoría del contenido escrito. | Separa comprobaciones temáticas de las rutas y del inventario MCP. |
| 64–78 | Define anclas para HTML, Remotion y guion. | Cada tupla tiene una ruta y un conjunto de textos que esperamos encontrar. |
| 79 | Abre el documento como texto UTF-8. | `read_text()` devuelve el contenido completo; aquí no se escribe nada. |
| 80 | Busca las anclas ausentes, sin distinguir mayúsculas. | `casefold()` es una normalización robusta para comparar texto sin caso. |
| 81–84 | Imprime el estado y actualiza el resultado acumulado. | Una lista vacía de ausentes se evalúa como `False`, así que `not ausentes` da `True`. |
| 91–102 | Primero comprueba archivos; si falta alguno, termina sin intentar abrirlo. Después ejecuta MCPs y anclas, y devuelve estado. | El sistema operativo interpreta `0` como éxito y un número distinto de cero como incidencia; el retorno temprano evita un error de ruta confuso. |
| 105–106 | Solo llama a `main()` al ejecutar este archivo directamente. | `__name__ == "__main__"` permite importar funciones sin iniciar la auditoría. |

## Qué significa cada resultado

- `OK`: archivo presente o contenido esperado encontrado.
- `FALTA`: falta uno de los archivos de entrega.
- `REVISAR`: el inventario o una frase ancla cambió y hay que contrastar la página con la fuente.
- `PRESENTACIÓN LISTA PARA VISTA PREVIA`: las comprobaciones de archivos, conectores y contenido pasaron.

El control no reemplaza abrir Remotion Studio y revisar el video visualmente. Ese paso lo haces vos en la terminal y en la interfaz de Remotion.
