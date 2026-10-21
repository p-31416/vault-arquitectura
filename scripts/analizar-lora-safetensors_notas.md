# analizar-lora-safetensors — notas

Script para auditar cualquier archivo `.safetensors` (LoRA o checkpoint) sin depender de PyTorch: lee el header, deduce el modelo base y revisa si los pesos aprendieron algo.

> Uso: `P:\Anaconda\envs\comfyenv\python.exe scripts\analizar-lora-safetensors.py <archivo.safetensors> [--json SALIDA.json]`
>
> Ejemplo real: `P:\Anaconda\envs\comfyenv\python.exe scripts\analizar-lora-safetensors.py "G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\rhino-to-image-lora.basic.safetensors"`

---

## 1. Qué es un `.safetensors`

Es un contenedor binario con una estructura fija y trivial:

```
┌───────────────────────────────────────────────┐
│ 8 bytes   N = tamaño del header (uint64 LE)   │
├───────────────────────────────────────────────┤
│ N bytes   header JSON                        │
│           {                                 │
│             "diffusion_model.img_in.weight":  │
│               {"dtype": "F32",                │
│                "shape": [4096, 128],          │
│                "data_offsets": [0, 2097152]}, │
│             ...                              │
│             "__metadata__": {...}   (opcional)│
│           }                                  │
├───────────────────────────────────────────────┤
│ resto     datos binarios de los tensores      │
└───────────────────────────────────────────────┘
```

Dos ideas para leerlo:

- **El header es un índice**: dice el nombre de cada tensor, su tipo de dato, sus dimensiones y en qué byte del archivo están sus bytes. Con eso se puede saber todo sin leer los datos.
- **`data_offsets` son absolutos respecto del inicio de la zona de datos**, o sea `8 + N`. Es el error clásico: sumar el offset al principio del archivo.

## 2. Cómo se lee el header (línea por línea)

```python
with open(ruta, "rb") as f:
    n = struct.unpack("<Q", f.read(8))[0]      # 8 bytes: uint64 little-endian
    header = json.loads(f.read(n).decode("utf-8"))
```

- `struct.unpack("<Q", ...)` lee 8 bytes como número sin signo de 64 bits **little-endian** (el `<` es el endianness, `Q` el tipo).
- `f.read(n)` lee exactamente los bytes del header.
- El header es **JSON**, no un formato binario: se puede abrir con cualquier editor y leerlo con los ojos.

## 3. Cómo se deduce el modelo base de un LoRA

Un LoRA guarda, por cada capa que se afina, **dos** matrices:

- `lora_A.weight` con forma `[rank, in_features]`
- `lora_B.weight` con forma `[out_features, rank]`

El `rank` es la dimensión baja de la factorización (aquí 16). Con esas formas se lee la arquitectura:

| Dato | De dónde sale |
|------|---------------|
| `hidden_size` | forma de `txt_in.lora_B.weight` → `[4096, 16]` → hidden = 4096 |
| `rank` | segunda dimensión de la misma matriz → 16 |
| `context_in_dim` | forma de `txt_in.lora_A.weight` → `[16, 12288]` |
| bloques duales | contar índices distintos en `double_blocks.N.` |
| bloques simples | contar índices distintos en `single_blocks.N.` |

Con esos cinco números se busca un perfil conocido en la tabla `PERFILES` del script (que está sacada de `black-forest-labs/flux2` y de `comfy/model_detection.py` de ComfyUI).

**Verificación cruzada**: no alcanza con que los números "se parezcan". El script recalcula los shapes con las fórmulas del modelo y los compara con los del archivo:

```
linear1  = 3*hidden + 2*mlp_hidden   (mlp_hidden = hidden * mlp_ratio)
linear2  = hidden + mlp_hidden
modul. doble = 6*hidden
```

Para klein 9B: `3*4096 + 2*12288 = 36864` ✓ y `4096 + 12288 = 16384` ✓. Si los shapes del archivo coinciden con las fórmulas, la identificación no es una suposición.

## 4. Cómo se revisa la salud de los pesos

Idea clave: **en un LoRA la matriz B arranca en cero**. El delta que se aplica al modelo base es `B @ A` (multiplicación matricial), así que un LoRA recién inicializado no cambia nada.

- Si **B es todo ceros** → el LoRA está sin entrenar, o fue "stripped" (se le borraron los pesos a propósito). No aporta nada.
- Si **B tiene valores** → hay delta real.

Por eso el script mide sobre las matrices B: media, desvío estándar, máximo absoluto y porcentaje de ceros. Seusa `array.array("f")` para leer los float32 del binario sin depender de numpy.

En el LoRA del curso: σ ≈ 1,3e-3 y 0 % de ceros → **entrenado y sano**, con amplitud baja (delta suave). Eso indica un strength de trabajo de 0,6 a 1,0.

## 5. Qué NO puede decir el script

- **El trigger word**: no está en los shapes. Solo aparece en la metadata (`ss_trigger_words`) o en la ficha del autor. Si la metadata no está, hay que pedirlo.
- **El dataset**: tampoco está. Salvo que el archivo traiga `ss_dataset` en la metadata.
- **La licencia**: hay que leerla del repositorio de origen.

Por eso la última sección del informe se titula "QUÉ FALTA EN LA FICHA": el script separa lo verificado de lo pendiente de confirmar con el instructor.

## 6. Los 3 casos de uso

| Quiero… | Cómo |
|----------|------|
| Saber si un `.safetensors` es un LoRA o un checkpoint | `es_lora` (¿tiene pares A/B?) |
| Saber sobre qué modelo hay que cargarlo | `perfil reconocido` + verificación de shapes |
| Saber si el LoRA está entrenado | `% de ceros` en las matrices B |
| Comparar dos LoRAs | `--json` y diff de los dos JSON |

## 7. Errores que ya están resueltos en el script

| Trampa | Cómo se evitó |
|--------|---------------|
| Leer los offsets desde el principio del archivo | los datos empiezan en `8 + N` |
| Asumir little-endian | `struct.unpack("<Q", ...)` lo fija explícitamente |
| Confundir `shape[0]` con `shape[1]` | se lee el rol según el nombre del tensor (A vs B) |
| Recorrer 120 MB en cada corrida | muestreo de hasta 12 matrices B |
| Romper con tildes al imprimir | `PYTHONIOENCODING=utf-8` en el comando de uso |

## 8. Verificación cruzada contra el análisis manual

El análisis del 2026-10-20 se hizo primero a mano (PowerShell, lectura directa del header) y después con este script. Ambos coinciden: 176 tensores, 31,66 M parámetros, rank 16, hidden 4096, 8 duales + 24 simples, contexto 12288, perfil FLUX.2 [klein] 9B, B no nulas.
