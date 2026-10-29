# Notas de `galeria-renders.py`

Genera un sitio web estático para **recorrer** los renders: un lienzo infinito con pan y zoom, una columna por workflow, un panel de metadata al hacer clic y un recorrido lineal con el teclado.

## Por qué existe

Los renders de ComfyUI traen la trazabilidad **dentro del PNG**: dos bloques `tEXt` (`prompt` y `workflow`) con el grafo completo. `indice-renders-comfy.py` traduce eso a una tabla (modelo, LoRA, seed, steps, cfg, prompt).

Pero **una tabla no se recorre**. Comparar dos renders exige abrir dos archivos, mirar el prompt en la terminal y comparar de memoria. Y el problema real de un tablero tipo Miro es peor: todo pegado en un lienzo infinito donde para llegar a la imagen 40 hay que hacer zoom out cientos de veces.

La galería es esa capa que falta: un lugar donde se **ve** lo que se generó y se llega con un clic a lo de al lado.

## Uso

```powershell
# 1. Reindexar (lee la metadata de cada PNG)
P:\Anaconda\envs\comfyenv\python.exe scripts\indice-renders-comfy.py --dir "P:\00-repos\ComfyUI\output" --out "proyectos\MVP_04-comfyui-arquitectura"

# 2. Generar el sitio
P:\Anaconda\envs\comfyenv\python.exe scripts\galeria-renders.py --indice "proyectos\MVP_04-comfyui-arquitectura\INDICE-RENDERS.json" --out "activos\web\galeria" --raiz-indice "P:\00-repos\ComfyUI\output"
```

Sale en `activos/web/galeria/index.html`. Se abre con doble clic (funciona en `file://`, sin servidor).

## Cómo funciona, por partes

### 1 · Copiar las imágenes

El índice guarda rutas **relativas** a la carpeta que se indexó (`--raiz-indice`). El script las copia a `img/` con un nombre numerado (`003_estadio_futbol.png`) para que el orden sea estable y no haya colisiones.

Las filas cuya imagen no se encuentra se descartan: es preferible un índice corto y sin links rotos a uno largo con imágenes que no abren.

### 2 · El color por seed

```python
digest = hashlib.md5(str(semilla).encode("utf-8")).hexdigest()
tono = int(digest[:6], 16) % 360
```

Un `md5` del seed → un número → un matiz HSV. El mismo seed siempre da el mismo color, así que los renders de una misma corrida se reconocen de un vistazo. Se usa `hashlib` (estable entre máquinas y versiones de Python) y no `hash()`, que cambia entre ejecuciones.

### 3 · El layout

Un `div` por workflow (columna), con las imágenes apiladas dentro. El contenedor `#mundo` lleva un `transform: translate(...) scale(...)`: pan y zoom sobre un único elemento, sin recalcular posiciones.

- **Pan**: `mousedown` + `mousemove` (guarda la posición inicial y la delta).
- **Zoom**: `wheel` con `preventDefault`. El truco es recentrar: se calcula dónde estaba el puntero en el mundo antes y después del cambio de escala, y se ajusta la traslación para que ese punto no se mueva.

```js
const nuevo = escala * factor;
tx = px - (px - tx) * (nuevo / escala);   // px = puntero en píxeles de pantalla
ty = py - (py - ty) * (nuevo / escala);
escala = nuevo;
```

### 4 · El panel de detalle

Cada nodo tiene un `click` que llama `seleccionar(i)`: arma la tabla de metadata (modelo, LoRA y fuerza, seed, steps, cfg, sampler, scheduler, resolución, archivo) y vuelca el prompt literal. El prompt va tal cual, sin retocar: es la evidencia de lo que se pidió.

### 5 · El recorrido

`visibles()` devuelve los índices que pasan los filtros. `mover(+1)` avanza dentro de esa lista con módulo, así que `→` al final vuelve al principio. Abajo hay una tira de miniaturas donde la imagen seleccionada se resalta.

### 6 · Los filtros

- **Por workflow**: chips generados desde los datos; click alterna (el mismo chiplo apaga).
- **Solo con LoRA**: para separar rápido "esto es el modelo" de "esto es el LoRA".
- **Búsqueda**: filtra por el prompt, en minúsculas, sobre el texto completo.

## Detalles que importan

- **Sin dependencias**: HTML + CSS + JS en un solo archivo. No hay npm, no hay build, no hay CDN. Se abre offline y dentro de 10 años.
- **El sitio es estático**: no publica nada. Publicar es otro paso (Caddy, EasyPanel, rsync) y esa decisión se toma aparte, con sus reglas de privacidad.
- **`activos/`**: la salida vive en `activos/web/galeria/`, que está en `.gitignore`. Son 54 MB de imágenes: no van al repo.
- **`datos.json`**: la misma información en JSON, para que otro programa (el agente, un tablero, un informe) la consuma sin parsear el HTML.

## Extensiones naturales

- Un `--filtro` por proyecto, para separar renders del concurso de los de prueba.
- Agrupar por seed en vez de por workflow (o toggle entre las dos vistas).
- Exportar la selección actual a un Markdown (el entregable A1 necesita un subconjunto).
