# indice-renders-comfy — notas

Script que indexa los renders de ComfyUI **leyendo la metadata que el propio ComfyUI graba dentro de cada PNG**.

> Uso:
> ```
> P:\Anaconda\envs\comfyenv\python.exe scripts\indexe-renders-comfy.py --dir "P:\00-repos\ComfyUI\output" --out "proyectos\MVP_04-comfyui-arquitectura" --nombre INDICE-RENDERS
> ```
> Opciones: `--dir` (repetible), `--out`, `--nombre`, `--since YYYY-MM-DD`.

---

## 1. La idea: la trazabilidad vive dentro de la imagen

ComfyUI no guarda la historia de un render en un archivo aparte: **la graba en el PNG**. Al guardar, escribe dos bloques de texto (`tEXt`) en el archivo:

| Clave | Contenido | Formato |
|-------|-----------|---------|
| `prompt` | el grafo del workflow | **API**: `{ "12": { "class_type": "KSampler", "inputs": {...} } }` |
| `workflow` | el mismo grafo | **UI**: `{ "nodes": [...], "links": [...] }` |

Verificado el 2026-10-21 sobre `P:\00-repos\ComfyUI\output`: 80 PNG, **80 con los dos bloques**.

Por qué esto importa: si el índice se arma leyendo las imágenes, **no hay base de datos que mantener ni que se desincronice**. Si una imagen se copia, se archiva o se borra, su historia viaja con ella. Y el prompt se puede volver a copiar en el canvas (es el "arrastrar el PNG de vuelta a ComfyUI" que ya hacía el estudio).

## 2. Cómo se lee un PNG

El formato es una cadena de chunks:

```
[8 bytes]  firma \x89PNG\r\n\x1a\n
[8 bytes]  longitud (uint32 big-endian) + tipo (4 letras)
[N bytes]  datos del chunk
[4 bytes]  CRC
```

El script recorre los chunks y se queda con los de tipo `tEXt` e `iTXt`. En `tEXt` el contenido es `clave\0valor` (latin-1), y el valor se decodifica como UTF-8.

```python
longitud = struct.unpack(">I", cabecera[:4])[0]
tipo = cabecera[4:8]
```

`struct.unpack(">I", ...)` es **big-endian** (a diferencia del `struct` de los headers de safetensors, que es little-endian `<Q`): es el detalle que más hace tropezar.

## 3. Cómo se extrae cada dato

Del grafo en formato API se busca por `class_type`:

| Dato | Nodo | Input |
|------|------|-------|
| Modelo | `CheckpointLoaderSimple` / `UNETLoader` | `ckpt_name` / `unet_name` |
| LoRA | `LoraLoader*` | `lora_name` + `strength_model` |
| Sampler | `KSampler` | `sampler_name` |
| Scheduler | `KSampler` / `Flux2Scheduler` | `scheduler` |
| Steps | `KSampler` / `Flux2Scheduler` | `steps` |
| CFG | `KSampler` / `CFGGuider` | `cfg` |
| Seed | `KSampler` / `RandomNoise` | `seed` / `noise_seed` |
| Resolución | `EmptyFlux2LatentImage` / `EmptyLatentImage` | `width`, `height` |
| Prompt | `CLIPTextEncode` | `text` |
| Nombre del workflow | `SaveImage` | `filename_prefix` |

Los nombres de los nodos se leen del grafo, **no se hardcodean a mano**: por eso el script funciona igual con el `KSampler` viejo, con el `Flux2Scheduler` + `SamplerCustomAdvanced` de FLUX.2, o con un `CFGGuider` + `RandomNoise`.

## 4. Por qué el índice sirve para algo más que ordenar

Con el índice se puede responder, sin buscar archivos:

- ¿qué imágenes usaron el LoRA propio y a qué fuerza?
- ¿qué seed produjo la imagen queeligió el cliente?
- ¿qué prompt de los que funcionaron se puede reusar?
- ¿cuánto se gastó (nº de renders) por flujo?

Y alimenta el dashboard: la galería puede mostrar, bajo cada imagen, su modelo y su seed sin que nadie los escriba a mano.

## 5. Qué falta para que sea automático

Hoy el script se corre a mano. Las dos formas de automatizarlo:

| Opción | Cómo | Nota |
|--------|------|------|
| **Watcher** | Un proceso que mira `output/` y reindexa cuando cambia | Con `watchdog` (o un `while True` con `time.sleep(2)`) |
| **Cron** | Una tarea programada que reindexa cada N minutos | Más simple y no consume recursos; ya hay n8n en el VPS que podría dispararlo |

La opción recommendada es el **cron**: el índice no necesita estar al segundo, y un watcher perpetuo en la PC de estudio es un proceso más que mantener.

## 6. Verificación

Probado el 2026-10-21 sobre `P:\00-repos\ComfyUI\output`: **80 renders, 80 con metadata, 0 sin metadata**. El índice recovery en `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md` + `.json`.
