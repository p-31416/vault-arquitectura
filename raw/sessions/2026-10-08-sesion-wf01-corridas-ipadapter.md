---
tipo: log
fecha: 2026-10-08
sesion: wf01-planta-ilustrada-corridas-ipadapter
tags: [sesion, comfyui, mvp_04.02, wf-01, controlnet, canny, ipadapter, inpainting, upscale]
estado: pausada
proximo_paso: "Fase B: F-06 IP-Adapter con ref-3 (@bit_arq) sobre la planta — copiar refs a ComfyUI input y encolar"
---

# Sesión 2026-10-08 (parte 2) — WF-01 planta ilustrada: corridas F-01..F-05 + install IP-Adapter

> Más nuevo → más arriba. Estado al cierre: **pausada**. ComfyUI 0.28.0 corriendo (PID 15620) con nodos IPAdapter cargados (35). Cola vacía, VRAM libre.

## Qué se hizo

1. **Estructura MVP_04.02 creada** — `proyectos/MVP_04.02-comfyui-arquitectura/` con `00-index.md`, `README.md`, 2 docs movidos desde MVP_04 (notas redirect dejadas), `WF-01-planta-ilustrada/` con archivo único 7 secciones + JSON base copiado de `n_03-WF01` Canny.
2. **Input SOL** — `inputs/P01-AIZPURUA.JPG` (planta monoambiente con baño/terraza, 311×494) + 3 refs en `inputs/ref/` (MON blueprint, terracota cálida, @bit_arq B&W fotorrealista = target).
3. **F-01 (ES, seed 42, 193 s)** — baseline español, Canny 0.9/end 0.8, 512². Respeta líneas, texto deformado ("MENCTA"). prompt_id `510e7a1f`.
4. **F-02 (EN, seed 42, 102 s)** — test A/B idioma. Muebles más definidos, más rápida. prompt_id `ea43aeac`. Conclusión: EN rinde mejor en SD1.5.
5. **F-03 (EN + fixes, seed 42, 134 s)** — latent/scale 512×832 (aspecto real), Canny 0.25/0.55, end 1.0, pista de ambientes en prompt. MEJORA CLARA: baño/escalera/terraza reconocibles, "TERRAZA" casi legible. prompt_id `c369f7f7`.
6. **F-04 (img2img sin Canny, denoise 0.35, 103 s) — FALLIDA 2/5** — delirio: movió el baño, cambió muebles, vació planta baja. Lección registrada: 2ª pasada siempre CON Canny. prompt_id `38e7aa76`.
7. **F-05 (img2img F-03 + Canny 0.9/end 1.0, denoise 0.25, 141 s)** — conserva F-03 + texturas/sombras sutiles, look ref-3 en SD1.5. Mejor resultado del día. prompt_id `058aa972`.
8. **Fase A dual Canny+Depth — BLOQUEADA**: no hay preprocesador de profundidad instalado (sin `comfyui_controlnet_aux`) y ComfyUI-Manager no responde (sin rutas) → no instalable por Manager. Se pivoteó a pulido img2img (F-04/F-05).
9. **Install IP-Adapter (Fase B setup, completo)** — clonado `ComfyUI_IPAdapter_plus` en `custom_nodes/`, instalado `accelerate` en conda env, descargado `ip-adapter-plus_sd15.safetensors` (93.6 MB, verificado 83 tensores) + CLIP ViT-H (vino fp32 2.4 GB → convertido a fp16 1.2 GB, verificado 521 tensores), reinicio manual de ComfyUI (la tool de restart no resuelve el path P:), 35 nodos IPAdapter verificados cargados.
10. **Backlog anotado en WF-01 §7** — WF-02 inpainting (dibujar ventanas, estilo video "ComfyUI For Architecture - Simple SDXL Inpainting Workflow" https://www.youtube.com/watch?v=px8POauudLY, probar SD1.5 primero) + WF-03 upscale (upscaler 4x liviano OK en RX 570, duda solo Hires Fix).
11. **Incidente OOM** — tildón por VRAM llena (caché de corrida MCP + canvas simultáneo). Recuperado con `clear_vram`, cola vacía. Regla: de a una cosa por vez.

## Archivos modificados

| Archivo | Acción |
|---|---|
| `proyectos/MVP_04.02-comfyui-arquitectura/` (carpeta completa) | creada |
| `.../00-index.md`, `README.md` | creados |
| `.../pbook-comfy_setup.md`, `comfy-tratamiento-datos.md` | movidos desde MVP_04 |
| `proyectos/MVP_04-comfyui-arquitectura/pbook-comfy_setup.md`, `comfy-tratamiento-datos.md` | notas redirect |
| `WF-01-planta-ilustrada/WF-01-planta-ilustrada.md` | creado + §4 ES/EN + §5 5 corridas + §7 backlog WF-02/WF-03 |
| `WF-01-planta-ilustrada/workflow_planta_canny_v1.json` | copiado + imagen/prompts/strength actualizados |
| `P:\00-repos\ComfyUI\input\P01-AIZPURUA.JPG` | copiado (LoadImage solo lee de ahí) |
| `P:\00-repos\ComfyUI\custom_nodes\ComfyUI_IPAdapter_plus\` | clonado |
| `P:\00-repos\ComfyUI\models\ipadapter\ip-adapter-plus_sd15.safetensors` | descargado |
| `P:\00-repos\ComfyUI\models\clip_vision\CLIP-ViT-H-14....safetensors` | descargado + convertido fp16 |
| `P:\00-repos\ComfyUI\corre_comfyui_background.bat` | arreglado (sesión parte 1) |
| `raw/sessions/2026-10-08-sesion-wf01-corridas-ipadapter.md` | este archivo |

## Pendiente (retomar)

- [ ] Pasar `WF01-planta_00001..00005_.png` de `P:\00-repos\ComfyUI\output\` → `salidas/n_01-F-0X.png`
- [ ] Completar §6 Evaluación del WF-01 con decisión SOL
- [ ] Fase B: copiar 3 refs a ComfyUI `input/` + F-06 IP-Adapter (ref-3, weight 0.6-0.8) + Canny
- [ ] WF-02 inpainting (ventanas) + WF-03 upscale
- [ ] Curaduría @contenidos del research 2026-10-08 (en espera desde parte 1)

## Análisis cerebro-digital

**Topics:** wf01-planta-ilustrada, test-ab-idioma-es-en, canny-fidelidad-lineas, img2img-delirio-sin-control, ipadapter-install, clip-vision-fp16, oom-rx570-recovery, manager-ausente, inpainting-backlog, upscale-backlog.
**Entidades:** P01-AIZPURUA.JPG, ArchitectureRealmix v1.1, Canny 0.9/end 1.0, IPAdapter_plus (35 nodos), CLIP ViT-H fp16 1.2 GB, refs MON/terracota/bit_arq, WF01-planta_00001..00005, PID 15620.
**Hechos:** (1) EN > ES en SD1.5 para prompts arquitectura; (2) aspecto real (512×832) fue el fix de mayor impacto en formas; (3) 2ª pasada sin Canny = delirio garantizado; (4) sin aux-pack no hay Depth → dual-depth queda para próximo ciclo con install manual; (5) Manager inalcanzable → installs por git+pip manual; (6) fp16 de CLIP vision necesario en 8 GB.
