# Sesión 2026-10-09 — WF-03 serie controles (versionado 4-pos + IC-Light)

## Qué se hizo

1. Log versionado X.Y.Z.W para `MVP_04.02/WF-03-serie-controles` (W=mínimo, Z=medio, Y=pipeline, X=enfoque). Corrección de ubicación: primer intento en carpeta vieja `MVP_04` eliminado, trabajo real en `MVP_04.02`.
2. Verificado que el link del canvas (`#5cc3dfe9…`) = workflow UI embebido en `WF03-FA_00001_.png` (img2img 9 nodos, seed 42, denoise 0.6).
3. Corridas F-A con método científico (una variable por vez, seed 42 fijo):
   - `3.0.0.0` baseline denoise 0.6 (208 s) — OK.
   - `3.0.0.1` solo prompts sunset + sol derecha (190 s) — el sol no se movió.
   - `3.0.0.3` denoise 0.8 mismo prompt (145 s) — sigue diurno + se apagó el brillo interior.
   - Conclusión: img2img no relocaliza el sol desde base diurna (límite documentado).
4. Base sunset regenerada por txt2img — salió otra casa (con pileta); pendiente decisión base-02 vs descartar.
5. Investigación web: opciones KSampler (doc oficial) + IC-Light (nodo exacto para luz direccional, compatible SD1.5).
6. Instalado `ComfyUI-IC-Light` (git clone) + modelo `iclight_sd15_fc.safetensors` (1.7 GB en `models/unet/IC-Light/`). Patrones de flujo extraídos de ejemplos oficiales.
7. Documentado IC-Light en `wiki/glosario/software/comfyui.md` (modelo + nodos + 6 referencias verificadas).

## Archivos modificados

- `proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/WF-03-serie-controles.md` (§4 matriz con Versión, §5 tabla con Vista + prompts + diagnósticos)
- `proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/salidas/n_03-F-A-v3.0.0.{0,1,3}.png` (gitignored, con metadata arrastrable)
- `wiki/glosario/software/comfyui.md` (secciones IC-Light)
- `P:\00-repos\ComfyUI\custom_nodes\ComfyUI-IC-Light\` + `P:\00-repos\ComfyUI\models\unet\IC-Light\` (fuera del vault)
- Eliminado: `proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/02-WF-log-WF01-4pos.md` (ubicación errónea)

## Pendiente próxima sesión

- Usuario reinicia ConfUI (auto-restart bloqueado: MCP apunta a `C:\Users\Solch16\ComfyUI` sin `main.py`; install real en `P:\00-repos\ComfyUI`; sin ComfyUI-Manager).
- Verificar nodos IC-Light, armar y correr `3.1.0.0` (luz derecha), decidir destino base-sunset.

## Análisis cerebro-digital

**Topics:** versionado-4pos, img2img-denoise-limits, relighting-direccional, ic-light-sd15, directml-rx570, wiki-software-unico.
**Entidades:** WF-03-serie-controles, architecturerealmix_v11, base-01.png, IC-Light FC, kijai/ComfyUI-IC-Light, lllyasviel, ComfyUI 0.28.0.
**Hechos:** (1) seed fijo 42 = reproducibilidad total; re-encolar no varía. (2) denoise ≤0.8 no mueve el sol en img2img diurno. (3) denoise 0.8 apagó ventanas iluminadas. (4) txt2img mismo seed + distinto prompt = otra casa. (5) IC-Light FC solo SD1.5; dirección vía LightSource, no vía prompt. (6) Sin Manager: installs por git clone + curl manual; restart manual por el usuario.
