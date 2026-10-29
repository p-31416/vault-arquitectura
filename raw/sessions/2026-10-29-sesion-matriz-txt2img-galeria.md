# 2026-10-29 — Revisión de los siete flujos del concurso + matriz txt2img + galería web de renders

## Qué se hizo

- **Revisión de los flujos del concurso** (lectura de las 7 fichas de `proyectos/concurso-gaudi-nexus/flujos/`): flujo-01 (Introduction) y flujo-02 (Text-to-Image) revisados en detalle, flujo-03 y flujo-07 mapeados contra el grafo existente de WF-rhino-to-image, flujo-04/05/06 leídos para el mapa de plataformas. Corrección detectada en flujo-01: el check de reproducibilidad pide "tres corridas A (seeds 42/77/123)" cuando la letra A son tres corridas **idénticas** con la misma seed.
- **Matriz de text-to-image con prompt y seed fijos**: script nuevo `scripts/matriz-txt2img.py` + notas. 20 filas en 4 bloques (modelo / LoRAs SD 1.5 / LoRAs SDXL / parámetros), prompt único del proyecto (Mercado de Proximidad + Centro de Cultura Digital junto a la Sagrada Família) y seed 42 en todas. **Bloque SD 1.5 corrido: 14/14 renders OK en ~35 min** (65–210 s cada uno).
- **Galería web de renders**: script nuevo `scripts/galeria-renders.py` + notas. Sitio estático (HTML+JS, sin dependencias) con lienzo infinito de pan y zoom, una columna por workflow, color estable por seed, panel de metadata al hacer clic, recorrido lineal con teclado, tira de miniaturas, filtros por workflow/LoRA y búsqueda en prompts. **94 renders** (80 previos + 14 de la matriz), 58 workflows, 54 MB, en `activos/web/galeria/` (fuera de git). JS validado con `node --check`.
- **Documento maestro** `specs/261029-matriz-txt2img-galeria-y-publicacion.md`: protocolo de la matriz, arquitectura de la galería, plan de publicación en `pitau.tech` (servicio nginx estático + labels de Traefik en el VPS de EasyPanel), **tabla de nodos de proveedor pagos y su reemplazo open source** (módulos 3, 4 y 5), y el método del agente constructor de flujos.
- **Índice de renders regenerado**: 94 renders con metadata (la metadata vive dentro del PNG).

## Hallazgos

- **El workflow del video 1 no está en la carpeta del curso**: el Módulo 1 del tablero Miro solo trae tarjetas de instrucciones (Prompt Coach / Comfy Expert). El workflow del video es el grafo básico de 7 nodos del core, sin nodos pagos — y su equivalente del estudio ya existe (`WF04-1.0.0-txt2img-base.json`, 7 nodos, architecturerealmix).
- **Los nodos pagos se concentran en los módulos 3, 4 y 5**; el módulo 2 (comparativa de modelos) no tiene ninguno. Cada uno tiene reemplazo: Topaz/Magnific → RealESRGAN + Hires; Nano Banana 2 / GPT Image → `sd-v1-5-inpainting-fp16` + IC-Light (ya en disco); Seedance → LTX-2 con LoRAs de control; Hunyuan3D/Tripo → ComfyUI-3D-Pack; Nano Banana Pro → Depth Anything 3 + SD1.5 img2img. La única fila donde el reemplazo es realmente peor es Seedance (video).
- **La trazabilidad ya estaba resuelta**: ComfyUI graba `prompt` y `workflow` dentro de cada PNG. Lo que faltaba era la capa de **lectura** (ver y recorrer), no la de captura.
- **El prompt del concurso rinde**: el baseline M01 (SD 1.5 sin LoRA) ya devuelve una calle peatonal fotorreal con mercado, gente y luz de mañana. M03 con el LoRA archviz @0,8 es visiblemente distinto con la misma seed → el delta es atribuible al LoRA, que es exactamente lo que la matriz debe probar.
- **Costo por render medido en el RX 570**: steps 10 → 65 s · steps 50 → 210 s · el resto 120–195 s. El paso 50 cuesta 3× el 10.
- **`caddy-salidas/` no es una carpeta web**: es el output root del MCP de AutoCAD (DWG). La web del estudio es EasyPanel + Traefik en el VPS, con dominio `pitau.tech`.

## Archivos

**Nuevos**

- `scripts/galeria-renders.py` · `scripts/galeria-renders_notas.md`
- `scripts/matriz-txt2img.py` · `scripts/matriz-txt2img_notas.md`
- `specs/261029-matriz-txt2img-galeria-y-publicacion.md`
- `raw/sessions/2026-10-29-sesion-matriz-txt2img-galeria.md`

**Modificados**

- `scripts/00-index.md` (entradas de los dos scripts nuevos)
- `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md` · `.json` (94 renders)
- `log.md`

**Fuera del vault**

- `activos/web/galeria/` — sitio, datos e imágenes (54 MB, gitignored)
- `P:\00-repos\ComfyUI\output\matriz\` — 14 renders de la matriz

## Estado y qué sigue

- **Bloque SDXL de la matriz pendiente** (M02, M09–M13): es el que mide el techo real de VRAM con LoRAs rank 128.
- **Publicación sin decidir**: dominio (`renders.pitau.tech`), si va con basic auth (recomendado: todo lo del concurso) y si la sincronización es manual o automática.
- **Comfy Cloud de pago**: diferido hasta gastar los 400 créditos gratis.
- **Skill del agente constructor**: se escribe después de probar el método a mano (decisión de la sesión).

## Análisis cerebro-digital

**Topics:** matriz-txt2img · galeria-renders · canvas-infinito · publicacion-pitau · nodos-pagos-vs-open-source · comfy-cloud · lora-locales · revision-flujos · gaudi-nexus

**Entidades:** `scripts/matriz-txt2img.py` · `scripts/galeria-renders.py` · `specs/261029-matriz-txt2img-galeria-y-publicacion.md` · `proyectos/concurso-gaudi-nexus/flujos/` (7 fichas) · `P:\00-repos\ComfyUI\output\matriz\` · `activos/web/galeria/` · EasyPanel + Traefik (`pitau.tech`) · `proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.json`

**Hechos:**
- El Módulo 1 del tablero Miro no tiene workflow: solo instrucciones del Prompt Coach y del Comfy Expert.
- 94 renders con metadata; 44 workflows previos + 14 de la matriz.
- El sitio de la galería es un solo `index.html` de ~64 KB sin dependencias: funciona en `file://` y no necesita servidor.
- El plan maestro de workflows (M-C1 a M-C7) sigue siendo el marco de fechas; esta sesión abre el frente de documentación y publicación.
