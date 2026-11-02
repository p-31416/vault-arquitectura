# volcar-grafos-matriz_notas.md — notas línea por línea

> Archivo paralelo didáctico: cada bloque del script explicado para aprender
> Python leyéndolo. Convención del vault: `sé leerlo`.

## Idea general

Las corridas de la matriz se encolaron con grafos construidos en memoria por
`armar_grafo()` — el PNG resultante no trae el `.json` en un archivo
descargable. Este script **regenera el mismo grafo** (misma fila, mismo
prompt, misma seed) y lo guarda en `activos/web/galeria/workflows/`, al lado
de las imágenes del tablero, para descargarlo desde cada tarjeta.

## Bloques

- **`cargar_matriz()`** — `importlib.util.spec_from_file_location` carga un
  `.py` por ruta aunque su nombre tenga guiones (igual que
  `dashboard-curso.py` hace con la galería). Devuelve el módulo con `MATRIZ`,
  `armar_grafo`, `PROMPT_PROYECTO` y `SEED`.
  # NOTA ES: importar el módulo NO corre la matriz: el `main()` está
  # protegido por `if __name__ == "__main__"`. Solo importamos definiciones.
- **`EJECUTADAS`** — las 14 filas corridas el 2026-10-29 (SD 1.5 +
  parámetros). Las SDXL (M02, M09–M13) se agregan cuando se corran: basta
  sumar sus IDs.
- **`main()`** — por cada fila ejecutada: `armar_grafo(fila, PROMPT_PROYECTO,
  SEED)` y `json.dump` con indent a `matriz-<ID>.json`. No corre nada: solo
  reconstruye el grafo determinista que ya corrió.
