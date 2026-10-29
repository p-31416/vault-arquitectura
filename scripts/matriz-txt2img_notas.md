# Notas de `matriz-txt2img.py`

Corre la **matriz de variantes de text-to-image** con prompt y seed fijos: una variable por fila, para que la diferencia entre dos imágenes sea atribuible.

## El problema que resuelve

Comparar modelos o LoRAs "en general" no dice nada: en cada prueba cambian el prompt, la seed, el estilo y el modelo, y el resultado no se puede leer. Con **un prompt, una seed y una variable por fila**, el delta visible *es* la variable. Es el protocolo del curso (mismo prompt, misma seed, una variable por corrida) y el mismo que usa `calibrar-loras-comfyui.py`.

## Uso

```powershell
# Ver el plan sin renderizar
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --dry-run --bloque todos

# El bloque rápido: todo lo SD 1.5 (14 renders, ~35 min)
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque sd15

# El bloque pesado: LoRAs de SDXL (5 renders, varios minutos cada uno)
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque loras_sdxl

# Con el prompt del curso en vez del prompt del proyecto
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --prompt curso
```

Requiere ComfyUI corriendo en `http://127.0.0.1:8188`.

## Cómo está armado

### La fila

Cada fila de `MATRIZ` declara **qué variable cambia** y los overrides:

```python
{"id": "M16", "bloque": "parametros", "base": "sd15", "titulo": "cfg 3",
 "variable": "cfg", "loras": [], "trigger": "", "over": {"cfg": 3.0}},
```

- `base` decide el checkpoint, la resolución y los parámetros por defecto.
- `loras` es una lista de `(archivo, fuerza)` — puede encadenar varias.
- `trigger` es la palabra que el LoRA aprendió: va **en el prompt**, nunca el nombre del archivo.
- `over` pisa lo que esta fila cambia.

### El grafo

Se arma con la misma estructura de siempre:

```
CheckpointLoaderSimple ──model(0)──┐
    ├──clip(1)──────────────────┐  │
    └──vae(2)───────────────┐  │  │
LoraLoader (×N en cadena) ──┼──┼──┤
    ├──model(0)─────────────┘  │  │
    └──clip(1)──────────────────┘  │
CLIPTextEncode(pos) ◄──────────────┘   ← cuelga de la salida CLIP del LoRA
CLIPTextEncode(neg) ◄─────────────────┘
EmptyLatentImage ──► KSampler ──► VAEDecode ──► SaveImage
```

**El detalle que importa:** los `CLIPTextEncode` cuelgan de la salida 1 (CLIP) del `LoraLoader`, no de la del checkpoint. Así el prompt también recibe el LoRA; si colgaran del checkpoint, el LoRA solo afectaría a la imagen y su palabra clave no activaría nada.

Las LoRAs se encadenan: la salida MODEL de una es la entrada MODEL de la siguiente.

### La corrida

`POST /prompt` devuelve un `prompt_id`; después se consulta `GET /history/{id}` cada 5 s hasta que aparece. Un render que falla (OOM, por ejemplo) **no corta la tanda**: se registra el error y sigue con la fila siguiente. Eso importa, porque en SDXL con LoRAs rank 128 un OOM es esperable y no debería abortar el bloque entero.

### La salida

Los renders caen en `P:\00-repos\ComfyUI\output\matriz\<base>\<ID>_00001_.png`, con el prefijo puesto en el `SaveImage`. Como el índice y la galería leen **toda** la carpeta de output, los renders nuevos aparecen solos en la galería: no hay paso de registro manual.

La tabla de resultados se escribe en `activos/web/galeria/matriz-txt2img.md` después de cada fila (así, si se corta la tanda, queda el avance) y el JSON completo al final.

## Los bloques

| Bloque | Filas | Qué mide | Tiempo |
|---|---|---|---|
| `modelo` | M01–M02 | el salto SD 1.5 → SDXL | ~10 min |
| `loras_sd15` | M03–M08 | el aporte de cada LoRA en SD 1.5 | ~17 min |
| `loras_sdxl` | M09–M13 | lo mismo en SDXL + el techo de VRAM | ~40 min |
| `parametros` | M14–M20 | steps · cfg · sampler · resolución | ~17 min |
| `sd15` | todo lo SD 1.5 | el atajo para la primera lectura | ~35 min |

## Detalles que importan

- **La seed 42 es la de todo el estudio.** Comparar la matriz contra los renders viejos del VF-estadio (que también usaban 42) permite ver si el prompt del proyecto rinde más o menos que el del estadio.
- **`steps 10` tarda la mitad** (65 s contra 135 s): sirve de termómetro de si el costo viene de los pasos o de otra cosa.
- **El negativo es el mismo en todas las filas.** Si variara, contaminaría la comparación.
- **El prompt del proyecto nombra la Sagrada Família y el programa** (Mercado de Proximidad + Centro de Cultura Digital). Es el primer render de texto del concurso: si esto no funciona, el problema no es el modelo.

## Extensiones naturales

- Un bloque `controlnet` (canny/depth/scribble sobre una captura de Rhino).
- Un bloque `inpaint` con la volumetría del concurso.
- Guardar el prompt por fila en un archivo, para poder reusarlo en el pod.
