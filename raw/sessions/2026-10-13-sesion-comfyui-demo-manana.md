# Sesión 2026-10-13 — ComfyUI demo mañana (3 actos) + LoRAs a P:

## Qué se hizo
1. Análisis flujos avanzados (ControlNet/LoRA/inpaint/upscale) viables en RX 570 DirectML + nota PA Academy top-5 + 4 links Civitai (2 LoRAs SD1.5, 1 checkpoint Realmix, 1 imagen ejemplo con stacking).
2. Revisión specs pendientes ComfyUI: 4 specs en `specs/` + plan 24h activo + 4 backlogs WF (todo ⬜ Pendiente, bloqueo común: upscalers + IPAdapter + ComfyUI apagado).
3. Mock demo mañana en 3 actos encadenados (txt2img → img2img → estilo marker), JSON API-format listos en `n_06-moodboard/WF/demo-manana/` + `00-README.md` guion + `scripts/demo_manana_notas.md` didáctico.
4. Análisis post Reddit `1hdbru3` (vía Arctic Shift, Reddit da 403): workflow Civitai 972694 FLUX1.Tools+CogVideoX v0.60 — solo RunPod (~23 GB VRAM), valida la estructura 3 actos.
5. Descarga 2 LoRAs a `C:` → movidos a `P:\00-repos\ComfyUI\models\loras\` (pedido usuario) + corrección `lora_name` en demo 03 + default workspace MCP fijado a `P:\00-repos\ComfyUI`.
6. Hallazgo: `P:` ya trae Realmix + Juggernaut + `sd-v1-5-inpainting-fp16` + canny/depth/scribble — demo sin bloqueos de modelos.

## Archivos modificados
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/demo-manana/{00-README.md,workflow_demo_01_txt2img.json,workflow_demo_02_img2img.json,workflow_demo_03_estilo_marker.json}` (nuevos)
- `scripts/demo_manana_notas.md` (nuevo, paralelo didáctico)
- `P:\00-repos\ComfyUI\models\loras\{markerhandsketch-V1,archisketch-v1}.safetensors + sidecars` (nuevos, + copias residuales en `C:\Users\Solch16\ComfyUI\models\loras\`)
- Config MCP `workspace.json` → default `P:\00-repos\ComfyUI`

## Pendiente próximo arranque (usuario prende Comfy luego)
- `corre_comfyui.bat` en P: → `http://127.0.0.1:8188` → `node_info`/`validate` demo 01-03 → Queue en orden → `02-WF-log` + salidas `n_06-B-*`.
- Opcional: limpiar duplicados LoRA en `C:`; acto 4 inpainting con `sd-v1-5-inpainting-fp16`.

## Cerebro-digital
- Topics: comfyui-demo, txt2img, img2img, lora-sketch, flux-tools, workspace-P, hitl-s.
- Entidades: ArchitectureRealmix v1.1, markerhandsketch-V1, archisketch-v1, PH-Archviz-FluxTools v0.60, RX570-DirectML, RunPod-4090.
- Hechos: SD1.5+2CN cabe en 8 GB; FLUX.Tools pide ~23 GB; `C:` era workspace erróneo, `P:` es install activo con inpainting; Reddit bloquea fetch (usar Arctic Shift).

## Agregado — reorganización a 04.02 + reporte @sherlock
- 04.02 es la versión activa (`WF-01/02/03` propios, convención archivo único); MVP_04 cerrado con `RESUMEN-flujos-probados.md` (23 imgs).
- PLAN F1-F8 movido a `04.02/PLANS/` + mapeo a WF-02/WF-03/WF-04-propuesto; F-E WF-03 desbloqueado con LoRAs de hoy; `00-index` 04.02 actualizado.
- @sherlock (task ses_ec7641766ffeuHpE6Obp74BvU7): 22 fuentes, secuencia 7 pasos local, 5 modelos livianos faltantes (RealESRGAN, vae-ft-mse, lineart fp16, pencil-sketch, SD15 respaldo), 13 docs oficiales 200. Hallazgo: depth pre-procesado externo desbloquea F-D sin aux pack.
- RealESRGAN_x4plus descargado y movido a `P:models/upscale_models/` (63.9 MB); servidor vivo lo lista junto a los 2 LoRAs con triggers. Upscale local desbloqueado.

## Agregado — serie WF-04/05/06 + batería del día (cierre)
- Creados WF-04 (6 JSON txt2img+LoRA, esquema 1.x/2.0.0), WF-05 (2.0.x + 2.1.x img2img+LoRA), WF-06 (3.x inpaint + 4.x outpaint), 8 JSON validados, `00-index` 04.02 con WF-04/05/06.
- Corridas: 1.0.0 (173s) + 1.0.1a/b/c SOL randomize (198/136/135s) + ladder markers 0.8/1.0 (150/149s, sweet spot ≈1.0) + ladder sketch 0.8/1.0 (148/164s, sweet spot 0.8-1.0) + 2.1.0 (138s, sin transferencia) + 2.1.1 (126s, tradeoff identidad/estilo). Total día: 11 imágenes nuevas.
- WF-04.md único: prompts ES, §2 inventario, §3 nodo por nodo, §9 log, backlog con agente foto/cine + LoRA propio (receta SANAA/OMA).
- Mañana: F8 (Canny + LoRA) agendado en backlog WF-03.
