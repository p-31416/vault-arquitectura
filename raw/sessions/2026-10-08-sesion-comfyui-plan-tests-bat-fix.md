---
tipo: log
fecha: 2026-10-08
sesion: comfyui-plan-tests-bat-fix
tags: [sesion, comfyui, mvp_04, sherlock, plan-24h, troubleshooting, directml]
estado: pausada
proximo_paso: "Paso 3 del plan — verificar modelos en dropdown CheckpointLoaderSimple de la UI (http://127.0.0.1:8188)"
---

# Sesión 2026-10-08 — ComfyUI arquitectura: research + plan 24h + fix .bat background

> Más nuevo → más arriba. Estado al cierre: **pausada**. ComfyUI corriendo en background (puerto 8188). Próximo paso pendiente del lado de SOL (ver abajo).

## Qué se hizo (orden cronológico)

1. **Research @sherlock (subagente `sherlock`)** — full sweep "ComfyUI para arquitectura" (moodboard, txt2img, exterior vs interior, img2img+IP-Adapter, ControlNet 2026, croquis→render, 3D model→render con foco Rhino, video, pack de nodos, licencias). Idioma ES+EN. Output: `raw/research/2026-10-08-comfyui-workflows-arq.md` (949 líneas, ~90 KB, 35+ fuentes, 38 URLs verificadas 200, 10 gaps). Índice `raw/research/00-index.md` actualizado con la fila al inicio.
   - Top 3 hallazgos: (a) FLUX.2 [klein] 4B Apache 2.0 como default iteración/entrega; (b) **MCP Rhino→ComfyUI nativo NO existe** — workaround: render passes Rhino → img2img + ControlNet Depth 0.85 + Lineart 0.7 + denoise 0.45-0.55; (c) video: LTX-2.3 en RunPod 24 GB, fallback Wan2.2-TI2V-5B local.
2. **Plan 24h didáctico desde cero** — escrito en `proyectos/MVP_04-comfyui-arquitectura/PLANS/2026-10-08-plan-tests-24h.md` (37 KB, 15 secciones). Reusa WFs ya armados del MVP_04 (A-WF-estadio, log-WF-croquis, n_03-WF01-croquis-estadio, 5 WFs moodboard). 8 bloques: setup → txt2img → img2img → ControlNet → SDXL → Rhino 2 img → moodboard → video RunPod (opcional) → cierre con tabla de decisión. Incluye cheat sheet de términos y troubleshooting.
3. **Decisión de alcance con SOL** — se trabaja sobre `MVP_04/`; caso "darle estilo a planos manteniendo reglas": NO con generación (rompe cotas/símbolos) salvo volumetría rough o look artístico con Canny strength alto; se arranca con **croquis real** de SOL (ControlNet directo).
4. **Troubleshooting lanzamiento background** — `corre_comfyui_background.bat` (acceso directo del escritorio `ComfyUI RX570 (Background).lnk` → `P:\00-repos\ComfyUI\corre_comfyui_background.bat`) fallaba: `comfy launch` usaba Python del sistema (`Python312`, sin dependencias) → `ModuleNotFoundError: No module named 'sqlalchemy'` (log `P:\00-repos\ComfyUI\user\comfyui_8188.log` 17:20). El `.bat` normal funciona porque usa el conda env.
5. **Fix del .bat (con `s` de SOL)** — reescrito el bloque de lanzamiento: usa `P:\Anaconda\envs\comfyenv\python.exe main.py` en proceso oculto detached (sobrevive al cierre), mismos PARAMS RX 570 del `.bat` normal, chequeo de puerto ocupado (no duplica instancia), espera verificada hasta 60 s, imprime comando de stop. Verificado el archivo final (94 líneas). SOL confirmó: **"ok ya funciona"**.

## Archivos modificados

| Archivo | Acción | Detalle |
|---|---|---|
| `raw/research/2026-10-08-comfyui-workflows-arq.md` | creado (@sherlock) | informe 949 líneas |
| `raw/research/00-index.md` | editado (@sherlock) | fila 2026-10-08 prependada, `ultima_actualizacion` 2026-10-08 |
| `proyectos/MVP_04-comfyui-arquitectura/PLANS/2026-10-08-plan-tests-24h.md` | creado | plan 37 KB, 15 secciones |
| `P:\00-repos\ComfyUI\corre_comfyui_background.bat` | editado (2 ediciones, con `s`) | launcher conda-env detached; **fuera del vault** (instalación ComfyUI, no versionado) |
| `raw/sessions/2026-10-08-sesion-comfyui-plan-tests-bat-fix.md` | creado | este archivo |

## Pendiente (retomar)

- **Paso 3 del plan:** SOL abre `http://127.0.0.1:8188`, agrega nodo `CheckpointLoaderSimple` y reporta qué modelos ve en el dropdown (esperado: `architecturerealmix_v11.safetensors`, `Juggernaut-XL_v9...`).
- Luego: foto del croquis real → `n_03-controlnet/n_03-WF01-croquis-estadio/00-inputs/` → ControlNet Canny 0.85 sobre ArchitectureRealmix (4 corridas letra F).
- Deadline SOL: mañana 2026-10-09 15:00.

## Análisis cerebro-digital

**Topics:** comfyui-setup-amd-directml, comfy-cli-vs-conda-env, controlnet-croquis-render, rhino-passes-workaround, mcp-rhino-inexistente, plan-didactico-cero, troubleshooting-background-launch, sqlalchemy-dependency.
**Entidades:** ComfyUI (P:\00-repos\ComfyUI, main.py), conda env comfyenv (P:\Anaconda\envs\comfyenv), Python312 sistema (sin deps), RX 570 8GB DirectML, ArchitectureRealmix v1.1, Juggernaut XL v9, ControlNet canny/depth/scribble SD1.5, FLUX.2 klein 4B (pendiente descarga), LTX-2.3 (RunPod), MVP_04 niveles n_01–n_06, @sherlock, @contenidos (pendiente curaduría: `¿Avanzo a curaduría? s/N` sin responder — SOL eligió "leerlo yo primero").
**Hechos:** (1) split-install: código ComfyUI en P:, datos/modelos repartidos entre P: y C:\Users\Solch16\ComfyUI; (2) comfy-cli default workspace ya es P:\00-repos\ComfyUI (log viejo del 24/09 con workspace C: quedó obsoleto); (3) causa raíz del fallo background = intérprete equivocado, no workspace; (4) SOL tiene deadline 2026-10-09 15:00; (5) curaduría @contenidos del research queda en espera.
