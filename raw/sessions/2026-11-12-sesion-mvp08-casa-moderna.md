---
tipo: log
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [sesion, mvp-08, casa-moderna, comfyui, realvis, diagnostico, pod, cloud, lamina]
idioma: es
---

# 2026-11-12 — MVP 08 casa moderna: diagnóstico, 10 flujos YT, F0 keeper RealVis

## Qué se hizo

1. **Reporte Open Higgsfield vs Higgsfield** (pedido inicial Sol): Higgsfield oficial cerrado + `open.higgsfield.ai` API oficial + clones comunidad (Open-Generative-AI ex Open-Higgsfield-AI vía MuAPI, wide-trace, Freefield/OpenField del challenge Comfy $25k). Veredicto en `specs/261112-veredicto-comfy-vs-openhiggsfield.md`: gana Comfy en ráfagas, pod always-on pierde.
2. **Loop captura Rhino → img2img → Telegram** aclarado: Comfy = taller propio, Open-Higgsfield = mostrador que cobra por generación.
3. **Diagnóstico técnico** (`specs/261112-diagnostico-controlnet-inpaint-upscale.md`): servidor vivo 856 nodos, 0 nodos faltantes. Causa de fallos = archivos: 12 workflows pedían `architecturerealmix_v11` ausente (quedó `.tmp`), upscale usaba LatentUpscale (look blando) en vez de ESRGAN, `--lowvram` muerto en DirectML, SDXL+ControlNet 9.4GB > 8GB.
4. **.bat unificados** (`corre_comfy.bat` + background): fuera `--disable-dynamic-vram`, dentro `--reserve-vram 1.0`. Proceso viejo matado, relanzado OK v0.28.0. Atajo a usar: `ComfyUI RX570 (Background).lnk` del escritorio.
5. **10 flujos YT** (`specs/261112-spec-10-flujos-yt.md`): F1 txt2img → F10 loop Telegram, cada uno con Descripción + Objetivo, viabilidad local.
6. **Plan casa→3D→Gaudí** (`specs/261112-plan-pruebas-casa-moderna-3d.md`) + **matriz local/pod/cloud** (`specs/261112-matriz-local-pod-cloud.md`) + **doctrina §5** (local prueba mínimo, pod=local con músculo, Cloud solo lo irremplazable) + **flujo 1** (`specs/261112-flujo01-casa-moderna-concreto-madera.md`).
7. **MVP 08 casa moderna** (nuevo, no dentro de MVP_04): 7 JSON validados 7/7 + `00-README` + `F0-prompt.md` (prompt Buenos Aires entre medianeras, 🔵/🔴, KSampler, 5 pruebas) + `scripts/dashboard-casa.py`. Viejos marcados obsoletos (WF-vivienda, n_02, WF_v5).
8. **F0 T1 Lightning** salió blanda/deformada → **F0b RealVisXL v5.0 1216x832 32 steps seed 42** `casa-F0b-v01_00001_.png` (1.8MB): keeper — hormigón con huellas de encofrado, listones madera, carpintería negra, patio, luz cálida tarde.

## Archivos modificados

- `specs/261112-veredicto-comfy-vs-openhiggsfield.md` (nuevo) · `specs/261112-diagnostico-controlnet-inpaint-upscale.md` (nuevo) · `specs/261112-spec-10-flujos-yt.md` (nuevo) · `specs/261112-plan-pruebas-casa-moderna-3d.md` (nuevo) · `specs/261112-matriz-local-pod-cloud.md` (nuevo, §5 doctrina) · `specs/261112-flujo01-casa-moderna-concreto-madera.md` (nuevo) · `specs/261112-plan-lamina-1000x700.md` (A1 + IA gráfica §3.1/§10)
- `proyectos/MVP_08-casa-moderna/` (nuevo: 00-index, flujos/7 JSON + 00-README + F0-prompt.md + salidas/) · banners obsoleto en WF-vivienda, n_02, WF_v5
- `scripts/dashboard-casa.py` (nuevo) · `proyectos/MVP_08-casa-moderna/flujos/n_09` no — upscale vive en `MVP_04/n_09-upscale/` + copia F5 en MVP_08
- `proyectos/MVP_08-casa-moderna/lamina` no — lámina en `proyectos/concurso-gaudi-nexus/lamina/` + mock `activos/web/lamina-A1/index.html`
- `P:\00-repos\ComfyUI\corre_comfy.bat` + `corre_comfy_background.bat` (flags)

## Análisis cerebro-digital

**Topics:** comfy-vs-openhiggsfield · loop telegram sin agente · diagnóstico nodos vs archivos · flags DirectML · 10 flujos YT · MVP 08 casa moderna · prompt Buenos Aires entre medianeras · keeper RealVis F0b.
**Entidades:** RealVisXL v5.0/Lightning, Juggernaut Ragnarok, IC-Light fc, RealESRGAN_x4plus, RunPod 3090/4090, Comfy Cloud Standard/Creator, MuAPI, Nano Banana, Qwen-Image-Edit, Tripo/Hunyuan3D, CameraAngleSelector.
**Hechos:** modelo local ganador = RealVisXL (Lightning iterar, v5.0 final); F0b keeper 1216x832 seed 42; 7 JSON MVP_08 validados; .bat unificados y servidor relanzado; doctrina local/pod/cloud acordada; mañana sigue F1 cámara sobre keeper F0b.
**Pendiente mañana:** F1 T1–T4 (cámara) sobre `casa-F0b-v01_00001_.png` + F2b sol + dashboard casa con primeras filas.
