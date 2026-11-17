---
tipo: indice
mvp: 04.03
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_04, v04-03, casa-moderna, flujos, sdxl, local]
idioma: es
---

# MVP 04.03 — casa moderna (flujos vigentes, todo local $0)

> Reemplaza los flujos viejos SD1.5/Juggernaut-lento (marcados `OBSOLETO — ver MVP 08`, sin borrar).
> Base canónica: RealVisXL V5.0 estándar 1216x832, 32 steps, cfg 4, seed 42 (keeper F0b verificada 2026-11-12). Salidas: `casa-{WF}-v{NN}-{variante}.png`.

## Cómo abrir y ver antes de correr

Entradas y salidas van encadenadas por nombre: la salida de F0 (`salidas/casa-F0b-v01-T3-steps40-keeper.png`) es la entrada de F1/F2/F4. Copiarla a `P:\00-repos\ComfyUI\input\`.

1. Arrastrar el JSON a `http://127.0.0.1:8188`. Leer nodos y params abajo. Recién entonces encolar.
2. Si el LoadImage pide otro archivo, se edita el widget (F3: tu foto con máscara pintada, opacidad ~75%; F5: la keeper final que elijas).
3. La salida sale sola versionada por flujo: `casa-{WF}-v{NN}-...` (SaveImage `filename_prefix`). Nada se llama `PONER-` al salir.

## Los 7 flujos

### F0 — base casa hormigón+madera, canónica RealVis (`workflow_F0b-casa-base_realvis.json`)
Descripción: txt2img que genera la keeper `salidas/casa-F0b-v01-T3-steps40-keeper.png` (verificada 2026-11-12: hormigón encofrado + listones + carpintería negra, patio, tarde).
Objetivo: punto de partida único; todo lo demás parte de esta imagen, no de prompts nuevos.
Prompt + KSampler + 5 pruebas: [[proyectos/MVP_08-casa-moderna/flujos/F0-prompt|F0-prompt]] (positivo 🔵 en azul, negativo 🔴 en rojo).

> Archivado: `workflow_F0-casa-base_lightning.json` → `_archivados/` (Lightning 512 salió blanda/deformada; queda solo como referencia de iteración rápida, NO es base).

### F1 — cámara (`workflow_F1-camara.json`, RealVis 20 steps cfg 4, denoise 0.6)
Descripción: misma casa desde otro ángulo sin remodelar. Variantes (editar prompt nodo 5 y encolar): 15° izquierda / low-angle / aérea leve / noche misma cámara.
Objetivo: vistas lámina en minutos (~7 min c/u). Si pierde identidad: bajar a 0.5; si no se mueve: subir a 0.7.
Entrada lista en `ComfyUI/input/`: `casa-F0b-v01-T3-steps40-keeper.png`.

### F2a — relight IC-Light (`workflow_F2a-relight-iclight.json`) 🗃️ DEPRECADO 2026-11-12
Requiere base SD1.5 y la regla del estudio es píxel final RealVis (ver spec miércoles: SD1.5 descartado). Sol solo por F2b. No borrar: queda como referencia pod.

### F2b — relight denoise (`workflow_F2b-relight-denoise.json`, denoise 0.4)
Descripción: cambio día→noche por img2img suave, 100% local Lightning.
Objetivo: workhorse de sol local mientras F2a espera base.

### F3 — inpaint muebles (`workflow_F3-inpaint-muebles.json`, denoise 0.8)
Descripción: pinta zona + texto; solo esa zona cambia.
Objetivo: agregar muebles / cambiar un paño sin tocar el resto.

### F4 — material (`workflow_F4-material.json`, denoise 0.55)
Descripción: cambia hormigón↔listones manteniendo volumetría y cámara.
Objetivo: biblioteca de 5 estilos §5 del spec con misma seed.

### F5 — upscale (`workflow_F5-upscale.json`)
Descripción: RealESRGAN_x4plus sobre la keeper final.
Objetivo: lámina nítida. En RX 570 correr por mitades o reservar para cierre.

## Registro y dashboard

Cada corrida: `salidas/casa-{WF}-v{NN}-{variante}.png` + fila en `scripts/dashboard-casa.py` ITEMS + `activos/web/casa-moderna/index.html` (generar con `P:\Anaconda\envs\comfyenv\python.exe scripts/dashboard-casa.py`).
