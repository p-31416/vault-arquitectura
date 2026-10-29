---
tipo: metodologia
fecha_creacion: 2026-10-23
ultima_actualizacion: 2026-10-23
tags: [referentes, tags, planilla, scripts, vault-visual]
---

# `referentes_tags.py` — notas

> Vuelca la planilla `raw/referentes/<slug>/tags.csv` al inventario JSON y detecta
> imágenes nuevas en la carpeta (las deja como pendientes).

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_tags.py --slug aixgaudi
```

## Por qué una planilla y no editar el JSON

El JSON tiene estructura (listas dentro de objetos) y se rompe con una coma de más.
El CSV lo abre cualquiera en Excel o Google Sheets sin riesgo.

```python
# NOTA ES: separador ';' porque es el que usa Excel en configuración regional argentina.
# Si fuera ',' las notas con comas romperían las columnas.
filas = list(csv.DictReader(fh, delimiter=";"))
```

## Tags múltiples

```python
# NOTA ES: dentro de una celda, varios valores se separan con '|'.
# "fachada|biomimetica" se transforma en ["fachada", "biomimetica"].
def partir(valor):
    return [v.strip() for v in re.split(r"[|,]", valor or "") if v.strip()]
```

## La carpeta manda

```python
# NOTA ES: cualquier imagen que aparezca en activos/referentes/<slug>/ y no esté en el
# inventario se agrega sola con tema "sin-clasificar". Así entra el material que sube
# Emilia al Drive sin pedirle que respete nombres ni planillas.
```

## Flujo compartido completo

1. Emilia sube imágenes a la carpeta compartida (`activos/referentes/<slug>/` sincronizada desde Drive).
2. `referentes_tags.py` las detecta y las marca `sin-clasificar`.
3. Se completan en `tags.csv` (o directo en el JSON, si son pocas).
4. `referentes_dashboard.py` regenera el tablero.

## Columnas de la planilla

`archivo;obra;autor;anio;ciudad;tema;estrategia;material;representacion;estado;nota;fuente_original`

- `archivo`: nombre exacto del JPG (`ref-01.jpg`). Es la clave de cruce.
- `nota`: una línea de "qué me interesa", en tus palabras.
- `fuente_original`: link al estudio/ArchDaily, no al pin.
