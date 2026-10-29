---
tipo: wf-readme
workflow: WF-loras-locales
nivel: n_01-txt2img
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [wf, txt2img, lora, calibracion, rx570, sd15, sdxl]
estado: activo
---

# 00-README — WF-loras-locales

Workflow de **calibración de LoRAs locales**: 1 render por LoRA con parámetros fijos, para comparar cuál sirve y a qué fuerza.

**Modelos:** ArchitectureRealmix v1.1 (SD 1.5) · Juggernaut XL v9 (SDXL)
**Hardware:** AMD RX 570 8 GB · DirectML · `--lowvram --cpu-vae --force-fp16`
**Salidas:** `salidas/n_01-G-NN.png` (letra **G = LoRA**)

---

## Qué hay que saber antes de tocar nada

- La comparabilidad es el objetivo: **misma seed, misma resolución, mismo prompt, mismo sampler** en todas las corridas. Si cambia uno, la comparación se rompe.
- El **trigger** de cada LoRA va en el prompt positivo (ver `03-nodos-WFloraslocales.md`).
- La letra **G** se suma a la leyenda A–F de `reglas-workflows-comfy.md`.
- Las imágenes de `salidas/` están **gitignored** (binarios efímeros); el valor de este WF está en el log y en la ficha del glosario.

## Archivos

| Archivo | Qué es |
|---|---|
| `00-README.md` | Este documento |
| `01-index.md` | Catálogo: qué LoRA va con qué salida y qué config |
| `02-WF-log-WFloraslocales.md` | Log de cada corrida (más nuevo arriba) |
| `03-nodos-WFloraslocales.md` | Wiring del `LoraLoader` y mapa de triggers |
| `04-backlog.md` | Pendientes y decisiones abiertas |
| `workflow_loras-locales.json` | Grafo API SD 1.5 (con `LoraLoader`) |
| `workflow_loras-locales_sdxl.json` | Grafo API SDXL (con `LoraLoader`) |
| `PLANS/calibracion-loras.json` | Salida del script: LoRA × strength × segundos × error |
| `PLANS/calibracion-loras.log` | Log incremental (JSON Lines) del script |
| `salidas/` | Renders `n_01-G-NN.png` |

## Cómo correr

```powershell
# ComfyUI arriba
P:\00-repos\ComfyUI\corre_comfyui_background.bat

# Tanda completa: 32 renders (~2 h)
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py

# Subconjunto rápido: 9 renders (~20 min)
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --solo SD1.5 --fuerzas 0.8
```

Explicación línea por línea del script: `scripts/calibrar-loras-comfyui_notas.md`.

## Criterio de lectura de los resultados

| Pregunta | Dónde se responde |
|---|---|
| ¿El LoRA cambia algo respecto del baseline? | Comparar contra `n_01-A-01.png` del WF-estadio (misma seed 42) |
| ¿0,6 o 0,8? | Par de imágenes consecutivas del mismo LoRA |
| ¿Vale la pena el costo en VRAM? | `PLANS/calibracion-loras.json` → `segundos` por LoRA |
| ¿Cabe en el RX 570? | Que la fila tenga `error: null` (OOM = no cabe) |

## Referencias

- [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] — catálogo de LoRAs locales
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook del stack
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/00-README|WF-estadio]] — baseline de referencia
