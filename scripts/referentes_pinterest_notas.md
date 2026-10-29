---
tipo: metodologia
fecha_creacion: 2026-10-23
ultima_actualizacion: 2026-10-23
tags: [referentes, pinterest, scripts, vault-visual, ingesta]
---

# `referentes_pinterest.py` — notas

> Baja un tablero **público** de Pinterest a `activos/referentes/<slug>/` y mantiene
> `raw/referentes/<slug>/referentes.json` con una ficha por pin.

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts/referentes_pinterest.py `
  --board "https://ar.pinterest.com/proyectopi31416/aixgaudi/" --slug aixgaudi
```

## Por qué RSS y no scraping

Pinterest expone `https://.../<usuario>/<tablero>.rss` sin login para tableros públicos.

```python
# NOTA ES: el tablero se pide como XML, no como HTML. El HTML pesa 1,3 MB de JavaScript
# y no trae los datos servidos: el RSS sí trae pin, imagen y fecha en texto plano.
titulo, pins = parsear_rss(fetch(board + ".rss"))
```

Cada `<item>` trae: link al pin, miniatura `i.pinimg.com/236x/...`, título, descripción y fecha.

## De miniatura a imagen real

```python
# NOTA ES: el RSS solo publica la miniatura de 236 px. La imagen buena se arma con el
# mismo hash en otra carpeta del CDN: /originals/dd/dd/dd/<hash>.jpg  (máx. 736 px en pins viejos).
def url_original(h):
    return f"https://i.pinimg.com/originals/{h[:2]}/{h[2:4]}/{h[4:6]}/{h}.jpg"
```

Dos aprendizajes que costaron una corrida cada uno:

- **403 al bajar imágenes**: el CDN exige `Referer: https://ar.pinterest.com/`. Sin ese header, el navegador funciona y `urllib` no.
- **Hash de 32 caracteres**: al extraer con regex hay que quedarse con el **último** grupo. Juntar los tres segmentos de carpeta con el hash duplica el prefijo (`ecf02c` + hash) y la URL da 403.

## Merge, no duplicado

```python
# NOTA ES: el tablero se relee entero cada vez. Para no perder los tags que ya escribimos,
# las fichas se buscan por pin_id y, si el mismo archivo se re-pineó, por imagen_hash.
prev = existentes.get(pin["pin_id"]) or por_hash.get(pin["imagen_hash"])
```

Reglas del script:

- Conserva `tags`, `nota`, `autor` y `estado` de las fichas existentes.
- El mismo archivo subido dos veces (mismo hash) cuenta una sola vez.
- Las fichas nuevas entran con `tema: [sin-clasificar]` y `uso: [<slug>]`.
- Corre con `--dry-run` para inventariar sin descargar.

## Límites reales

| Tema | Estado |
|---|---|
| Tablero público | funciona sin login |
| Tablero secreto | el RSS devuelve vacío → plan B: capturas o export manual |
| Resolución | 736 px máximo; para lámina final conviene recuperar la fuente original |
| Link de origen del pin | el RSS no lo expone: se completa a mano en `tags.csv` o en la ficha |
| Volumen | un tablero chico tarda segundos; sin pausas entre descargas el CDN puede rate-limitar |

## Uso interno

Las imágenes quedan en `activos/` (gitignored). El `.md`/`.json` guarda solo rutas y metadatos: nunca se versionan binarios.
