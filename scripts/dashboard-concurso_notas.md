# dashboard-concurso.py — notas

## Qué resuelve

`galeria-renders.py` muestra **todo** el output de ComfyUI y no sabe de tiempos.
`dashboard-curso.py` es el del curso (SD 1.5, matriz M01–M20, tiempos hardcodeados).
Faltaba una vista chica: **solo las imágenes del concurso, con modelo y segundos reales**.

## Cómo se corre

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-concurso.py
```

Opciones:

- `--out` carpeta del sitio (default `activos/web/concurso`)
- `--comfy` URL del servidor (default `http://127.0.0.1:8188`)

Salida:

```
activos/web/concurso/index.html   ← HTML+CSS+JS en un archivo (abre con doble clic)
activos/web/concurso/datos.json   ← los datos, reutilizables
activos/web/concurso/img/         ← copia de los PNG, SIN reescalar
```

## Decisiones

**El tiempo sale de `/history`, no de un diccionario.** ComfyUI guarda en
`status.messages` dos eventos con timestamp en ms: `execution_start` y
`execution_success`. La resta es el tiempo real de GPU. Si el servidor está
apagado el tablero igual se genera, con `segundos: null` ("sin dato").

**La resolución se lee del PNG, no del grafo.** Se parsean los bytes 16–24
(IHDR) en vez de leer el `EmptyLatentImage` del workflow. Así se evita el bug
del indexador de galería, que informa la resolución **base** (1344×768) y no la
final (2016×1152).

**Las imágenes se copian tal cual** (`shutil.copy2`), sin miniaturas. Si se ven
pixeladas es porque el original no tiene más detalle, no porque el tablero lo
degrade.

**Sin dependencias.** Solo stdlib (`argparse`, `json`, `shutil`, `struct`,
`urllib`, `datetime`). No necesita Pillow ni servidor: funciona con `file://`.

## Para agregar una corrida

1. Encolar en ComfyUI y anotar el `prompt_id`.
2. Copiar el PNG a `activos/proyectos/concurso-gaudi-nexus/fractal-hires/`.
3. Agregar una entrada al bloque `ITEMS` (slug, archivo, modelo, checkpoint,
   prompt_id, workflow, nota).
4. Volver a correr el script.

## Límite conocido

`/history` se vacía al reiniciar ComfyUI. Por eso cada entrada de `ITEMS` trae `segundos_fijo` con el tiempo medido 2026-11-01 (609.26 / 1073.69 / 1165.06 / 409.36 s): cuando `/history` responde, manda el valor vivo; cuando devuelve vacío, el tablero usa el respaldo y lo avisa en consola. Así regenerar con el servidor apagado conserva los tiempos.
