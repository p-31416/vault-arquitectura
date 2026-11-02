---
tipo: backlog
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, img2video, backlog]
---

# 04-backlog — WF_ltx_i2v

- [ ] Arrancar ComfyUI (`127.0.0.1:8188`) y validar JSON contra `/object_info` (R4) — anotar resultado en 02-WF-log
- [ ] Confirmar nombre del nodo i2v en la build actual (`LTXVImgToVideo` puede haber sido renombrado con el release LTX 2.3) — ajustar JSON si hace falta
- [ ] Decidir ruta de la **primera corrida en nube** (aprobado "ese se prueba en nube"):
  - [ ] RunPod pod (4090, deadman del MCP) — instalar paquete `ltx-2.3-img2vid` con `apply_manifest`
  - [ ] o Comfy Cloud / API nodes (Kling/Seedance) si el costo de GPU no justifica
- [ ] Instalar LTX-2.3 checkpoint + text encoder gemma + LoRAs distill (24-46GB) — pendiente de `s` local
- [ ] Corrida A baseline (3× mesma seed) con render de salida del WF de n_02/n_03 como start frame
- [ ] Referencias del piloto YT: Paul Hansen IMG2VIDEO (`hpireXqXuU0`), MiniMax H3 (`S9O3FPumX4Q`), tute img→video oficial ComfyUI (`Yuw8F4E4-7Y`)
- [ ] ¿Audio? LTX-2.3 trae sync audio (ruta completa del pack); decisión tras primera corrida muda
- [ ] img2 3D (flujo 4) — mkdir `n_08-img23d` con Hunyuan3D o API node; referencias piloto: Hunyuan 3D concept (`EuAe-4nXFSk`), 3D Characters→Blender (`cXXNUR_wu60`)
