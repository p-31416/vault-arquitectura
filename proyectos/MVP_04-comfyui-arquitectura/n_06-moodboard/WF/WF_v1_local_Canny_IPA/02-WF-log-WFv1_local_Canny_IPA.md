---
tipo: log
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [mvp_04, n_06, log]
---

# 02-WF-log — Más nuevo → más arriba

## 2026-09-10 — v1 COMPLETO vía MCP (134s, success)

- Salida: `salidas/n_06-B-01.png` (origen Comfy `n_06-B-01_00001_.png`, prompt `4908ac63`, 134.46s).
- Params: seed 42, cfg 7, steps 30, euler_ancestral/karras, denoise 1.0, ImageScale lanczos 512, Canny 0.31/0.59, CN canny 0.85/0.0-0.80, Realmimix, input `croquis001.jpg`.
- Lectura: el Canny del croquis guió a interior rústico de madera (vigas + travertino); el prompt toscana aportó materialidad piedra/madera. Letra B válida como variación de prompt.
- Flujo también guardado en librería Comfy: `n_06-moodboard-WF_v1_local_Canny_IPA.json` (abre en canvas).

## 2026-09-10 — v1 encolado vía MCP (render en curso)

- `prompt_id 4908ac63-cdc6-448f-ac72-6759e5144e57` (enqueue OK, queue 1→running).
- Input real: `croquis001.jpg` (el placeholder `mood-product-ref.png` no existe en `input/`; `validate` lo marcó `value_not_in_list` y se sustituyó).
- IPAdapter ausente en el server (`node_info IPAdapter` 0 resultados) → L1 corre ControlNet puro + fallback VAEEncode 0.65 documentado para L2.
- Health al encolar: ComfyUI 0.28.0, torch 2.4.1+cpu, DirectML, checkpoints 2 (Realmimix + Juggernaut), controlnet 3 (canny + depth fp16 + scribble), 0 errores en logs.
- Salida esperada: `salidas/n_06-B-01.png` (se copia al terminar).

## 2026-09-09 — v1 armado, enqueue bloqueado

- Workflow: `workflow_moodboard_local.json` (12 nodos, creado vía `comfyui_create_workflow create + modify`).
- Params: seed 42, cfg 7, steps 30, euler_ancestral/karras, denoise 1.0, Canny 0.31/0.59, CN strength 0.85 start 0.0 end 0.80, ImageScale lanczos 512 crop center, prefijo `n_06-B-01`.
- `validate` + `node_info` + `enqueue` devuelven ECONNREFUSED (Comfy abajo).
- `server_start` falla: `ModuleNotFoundError: No module named 'sqlalchemy'` en `P:\00-repos\ComfyUI\main.py:22` (cadena seeder→scanner→queries→asset).
- `list_local_models` muestra solo Juggernaut XL + scribble 0.6MB (difiere de catálogo Realmimix+Canny+Depth — revisar extra-paths al arrancar).
- Salida esperada: `salidas/n_06-B-01.png` (pendiente).
- Próximo paso: instalar dependencia en el venv de Comfy (`python -m pip install sqlalchemy` o reinstalar requirements), arrancar `corre_comfyui.bat --directml 0 --force-fp16 --disable-cuda-malloc --lowvram`, revalidar y encolar.
