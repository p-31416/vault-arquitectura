# Notas de `calibrar-loras-comfyui.py`

Script que calibra **todos los LoRAs instaladas** contra los checkpoints locales, para saber cuál sirve y a qué fuerza.

## Qué problema resuelve

Instalar un LoRA es fácil; saber **si sirve** no. Un LoRA de CivitAI puede venir entrenado sobre otra base, con otro trigger, o simplemente no encajar con el prompt del estudio. La calibración es 1 render por LoRA con parámetros fijos: si dos LoRAs se comparan con la misma seed, la misma resolución y el mismo prompt, la diferencia entre imágenes es **el LoRA**.

## Uso

```powershell
# Tanda completa: 16 LoRAs × strengths 0.6 y 0.8 = 32 renders (~2 h en RX 570)
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py

# Solo una familia de base o una sola fuerza (re-renders puntuales)
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --solo SD1.5
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --fuerzas 0.8

# Ver el plan sin renderizar nada
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --dry-run
```

Requiere ComfyUI corriendo (`corre_comfyui_background.bat`) en `http://127.0.0.1:8188`.

## Cómo funciona (leelo y entendelo)

1. **Arma un grafo en formato API.** Un grafo de ComfyUI en formato API es un diccionario `{id_del_nodo: {class_type, inputs}}`, donde cada input puede ser un valor literal o una referencia `[id_de_origen, indice_de_salida]`. El grafo de este script es:

   ```
   CheckpointLoaderSimple ──model──┐
       ├──clip──────────────────┐   │
       └──vae───────────────┐  │   │
   LoraLoader ──model──┐    │  │   │
       └──clip──────────┼──┐ │  │   │
   CLIPTextEncode(pos) ──┘  │ │  │
   CLIPTextEncode(neg) ─────┘ │  │
   EmptyLatentImage ──────────► │
   KSampler ◄───────────────────┘
       └──► VAEDecode ──► SaveImage
   ```

   **Lo importante:** el `LoraLoader` va *entre* el checkpoint y el sampler. Su salida 0 es el MODEL con el LoRA fusionado y su salida 1 es el CLIP con el LoRA. Los dos `CLIPTextEncode` cuelgan de la salida **1** del LoRA, así el texto también recibe el LoRA (si colgaran del checkpoint, el LoRA afectaría solo a la imagen, no al texto).

2. **Manda el grafo por HTTP.** `POST /prompt` con `{"prompt": grafo, "client_id": ...}` devuelve un `prompt_id`. No usa la librería `requests`: solo `urllib` de la librería estándar.

3. **Espera.** `GET /history/{prompt_id}` devuelve el resultado cuando el render terminó; el script consulta cada 5 s hasta que aparece o se agota el timeout (30 min por render).

4. **Copia la salida.** ComfyUI guarda en `P:\00-repos\ComfyUI\output\<subfolder>\<archivo>.png`; el script lo copia a `WF-loras-locales/salidas/n_01-G-NN.png` con la nomenclatura del vault (letra **G = LoRA**).

5. **Registra todo.** Cada intento (exitoso o fallido) se anexa a `PLANS/calibracion-loras.log` (JSON Lines) y al final se escribe `PLANS/calibracion-loras.json` con LoRA, base, strength, seed, trigger, segundos y error. Un render fallido (OOM típico) **no corta la tanda**: se registra y sigue.

## Parámetros por familia de base (no son intercambiables)

| | SD 1.5 | SDXL |
|---|---|---|
| Checkpoint | `architecturerealmix_v11.safetensors` | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` |
| Resolución | 768×512 | 1216×832 |
| Steps | 30 | 30 |
| CFG | 7 | **4** (SDXL con cfg 7 se quema) |
| Sampler | `euler_ancestral` | `dpmpp_2m` |
| Scheduler | `karras` | `karras` |

Mezclar parámetros entre bases arruina la comparación: por eso están en dos diccionarios (`BASES`) y no en constantes sueltas.

## El trigger va en el prompt

Cada LoRA se activó con una palabra o frase (su `trainedWords`). Va **en el prompt positivo**, no como nombre de archivo:

```
✅  "archviz, architecturerealmix style, modern architecture, ..."
❌  "JJ_Archvizcg_v2.safetensors, architecturerealmix style, ..."
```

El script toma el trigger de la lista `LORAS` (campo `trigger`). Si un LoRA no expone trigger, el campo va vacío y el prompt queda sin prefijo.

## Cuidado con el tiempo

En el RX 570 un render SD 1.5 de 768×512 a 30 steps lleva ~132 s; uno SDXL de 1216×832 lleva bastante más (con `--lowvram --cpu-vae` y LoRAs rank 128, varios minutos). La tanda completa es de ~2 h. Para una primera lectura, conviene `--solo SD1.5 --fuerzas 0.8` (9 renders, ~20 min).

Si hay que cortar: el script no se puede reanudar (no guarda estado), pero `PLANS/calibracion-loras.log` sí tiene el avance, y se puede filtrar con `--solo` / `--fuerzas` para rehacer un subconjunto.
