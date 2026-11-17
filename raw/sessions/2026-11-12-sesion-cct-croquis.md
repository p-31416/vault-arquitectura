# Sesión 2026-11-12 — F1 cámara + CCT croquis→imagen

## Qué se hizo
- F1 cámara (casa moderna): creado `F1-camara.md` + `workflow_F1b-canny.json` + `workflow_F1c-ipadapter.json`. Regla: prompt→ControlNet→IPAdapter→3D.
- Croquis separados a proyecto propio `cct-centro-cultural-tigre/` (no eran casa moderna): `00-index.md` + `flujos/G0-croquis-imagen.md` + `flujos/salidas/`.
- Corridas G0/G1/G5 en ComfyUI local (RealVis, SDXL únicamente — SD1.5 descartado v01/v02).
- Mejor resultado: `cct-G5-v03-scribble.png` (txt2img + scribble 0.8, primera foto real: malla hunter douglas, acero, madera, verde).
- Plan casa moderna revertido a original (sin croquis).
- ComfyUI detenido (PID 2004) para liberar PC. relanzamiento manual: `P:\00-repos\ComfyUI` con flags `--directml 0 --lowvram --cpu-vae --reserve-vram 1.0`.

## Archivos modificados
- `proyectos/MVP_08-casa-moderna/flujos/F1-camara.md` (nuevo), `workflow_F1b-canny.json`, `workflow_F1c-ipadapter.json`
- `proyectos/cct-centro-cultural-tigre/00-index.md`, `flujos/G0-croquis-imagen.md`, `flujos/salidas/*.png`
- `specs/261112-plan-pruebas-casa-moderna-3d.md` (ida y vuelta, quedó original)

## Cerebro-digital
- Topics: consistencia cámara (denoise), croquis→foto (img2img zona muerta en papel blanco; scribble sí funciona), disciplina de cola 1 trabajo SDXL.
- Hechos: SD1.5+Canny sobre rayado = ruido; v03 scribble 12min = primera foto; v04 interrumpida por corrida manual; OOM límite 9.4GB>8GB.
- Pendiente: G5 v04 (strength 0.7, draft 704×1024) tras reinicio.
