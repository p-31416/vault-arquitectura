---
tipo: flujo
proyecto: cct-centro-cultural-tigre
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [cct, croquis, controlnet, canny, comfyui, local]
idioma: es
---

# G0 — croquis CCT → imagen (piloto local)

> Entradas inmutables en `activos/croquis/`. Copiar a `P:\00-repos\ComfyUI\input\` antes de encolar. Lo limpio de Photoshop (cómo llegamos a esa imagen limpia) queda para después; ahora la prueba es croquis → imagen.

## Pipeline local (SDXL únicamente, regla del estudio)

```text
LoadImage (copia del croquis) → ImageScale (832×1216 vertical / 1216×832 apaisada, lanczos)
→ VAEEncode → KSampler (RealVisXL V5.0 estándar, dpmpp_2m/karras 32 pasos cfg 4, denoise 0.6-0.75)
→ VAEDecode → SaveImage
```

Sin SD1.5 para nada: el Canny SD1.5 sobre rayado denso genera ruido y el modelo chico no levanta fotorrealismo (v01/v02 descartadas). Si se necesita amarre geométrico, es ControlNet SDXL (`control_sdxl_canny_fp16`, 9.4GB — va justo en 8GB, probar a 1024×704 si OOM) o vía pod. B/N pide denoise alto (falta color) + prompt material explícito; color editado pide denoise bajo + IPAdapter para no lavar lo pintado. Cada proyecto con su prompt: nada de bloques casa moderna en CCT.

## Disciplina de cola (la máquina se tilda si se apila)

Cola verificada vacía tras cancelar (running 0, pending 0). Reglas: un solo trabajo SDXL por vez, nunca encolar encima de otro corriendo; VRAM libre ~1GB con RealVis cargado; si se tilda, cancelar + reiniciar ComfyUI antes de reencolar. Resoluciones grandes (1024×1216) primero en draft 1024×704 si hay cuelgues.

## Salidas (miniaturas, una por corrida)

### G0 — pájaro directo txt2img (Lightning 6 pasos, seed 42)

[![cct-G0-v01 pájaro aéreo río + parasoles](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/thumbs/cct-G0-v01-pajaro-aereo.jpg)](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/cct-G0-v01-pajaro-aereo.png)

Veredicto: arquitectura presente (barras + parasoles + río + verde), técnica derivó a acuarela sepia en vez de tinta B/N (cfg 1.5 obedece poco el negativo). Siguiente: versión B/N en RealVis estándar 32 pasos cfg 4.

### G1 — detalle Azcona v01 (Canny SD1.5, denoise 0.75) ❌ descartar

[![cct-G1-v01 detalle Azcona quemado](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/thumbs/cct-G1-v01-detalle.jpg)](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/cct-G1-v01-detalle.png)

Veredicto: quemada y abstracta (sobreexpuesta, hormigón lavado, sin vanos legibles). Causa: denoise 0.75 alto + Canny 0.31/0.59 que lee el rayado del croquis como textura + base inpainting SD1.5. Siguiente: v02 con denoise 0.55 (una variable por corrida).

### G1 — detalle Azcona v02 (Canny SD1.5, denoise 0.55) ❌ descartar

[![cct-G1-v02 detalle ruido azul](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/thumbs/cct-G1-v02-detalle.jpg)](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/cct-G1-v02-detalle.png)

Veredicto: ruido azul/rosa siguiendo las líneas, nada fotorrealista. Diagnóstico: el Canny del rayado denso es puro ruido y el SD1.5 a 512 no levanta fotorrealismo de un croquis a mano. Se abandona la vía SD1.5 para este croquis. Siguiente: v03 SDXL RealVis estándar img2img vertical 832×1216, denoise 0.7, sin ControlNet (calidad foto primero, geometría después).

### G1 v03 + G5 fin0003 — canceladas (máquina tildada, sin salida)

v03 (prompt genérico con restos casa moderna: timber slats, party walls — error, se archiva como referencia mala) y G5 (prompt rico fin0003 aprobado) se cancelaron porque la máquina se tildó con trabajos apilados. Cola verificada vacía. El prompt G5 queda guardado abajo, listo para reencolar tras reinicio con disciplina de un trabajo por vez.

Prompt G5 aprobado (no reescribir, reutilizar tal cual):

```text
photorealistic, raw photo, 8k uhd, architectural photography, lateral side view of a cultural center in Tigre Argentina, third-floor height viewpoint looking across an open double-height patio, exterior of modular perforated gray metal sunshades like hunter douglas, exposed concrete beams, black aluminum window frames, open foreground double height with wooden pergola covered in green vines, glass railing around inner patio with wooden deck floor, view deep into the cultural center interior, small undefined sketch-style person silhouette standing in the patio, another tiny person far inside the hall, late afternoon warm light, long soft shadows, 24mm tilt-shift lens, sharp focus, highly detailed
```

Params: RealVis estándar, 1024×1216, dpmpp_2m/karras 32 pasos cfg 4, denoise 0.65, seed 42. Entrada: `cct-croquis-fin0003.jpg` (copia de [activos/croquis/Azcona-croquis-fin0003 (1).jpg], ya en input).

### G5 — fin0003 v01 (RealVis, denoise 0.65) ⚠️ a medio camino

[![cct-G5-v01 fin0003 limpio pero dibujo](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/thumbs/cct-G5-v01-fin0003.jpg)](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/cct-G5-v01-fin0003.png)

Veredicto: geometría perfecta pero NO es foto — es tu croquis limpio (líneas B/N, personitas apenas modeladas, pérgola y baranda intactas). Causa: denoise 0.65 conserva demasiado trazo y el modelo lo renderiza como contenido. Siguiente: v02 denoise 0.8 (suelta la línea, arriesga geometría).

### G5 — fin0003 v03 (txt2img + scribble SDXL 0.8, denoise 1.0) ⚠️ primera imagen real

[![cct-G5-v03 scribble foto malla perforada](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/thumbs/cct-G5-v03-scribble.jpg)](activos/proyectos/cct-centro-cultural-tigre/flujos/salidas/cct-G5-v03-scribble.png)

Veredicto: primera foto de verdad (12 min). Materiales presentes: malla metálica perforada tipo hunter douglas, columnas acero, vigas madera pérgola, verde, deck. Falta: vista más frontal que tu lateral de 3er piso, sin doble altura interior legible ni personitas. Siguiente: v04 strength 0.7 + prompt con patio/personas primero (una variable).

### G5 v04 — interrumpida (disputa de cola, sin salida)

Draft 704×1024 strength 0.7: interrumpida en KSampler al arrancar la corrida manual de Sol en canvas (misma máquina, un solo trabajo por vez). Cola libre para su corrida. La receta v04 queda vigente para reencolar cuando el canvas libere.

## 4 pruebas (una variable por corrida, seed 42)

| # | Entrada | Prompt guía | Denoise | Qué mirar | Salida |
|---|---|---|---|---|---|
| G1 | [activos/croquis/azcona-croquis001.jpg] | hormigón + parasol + madera, alero y vigas | 0.65-0.8 | respeta alero/vigas, sin vanos inventados | `cct-G0-v01-detalle.png` |
| G2 | [activos/croquis/croquis-fin0001.jpg] | patio interior, luz, figura escala | 0.7 | profundidad patio, figura coherente | `cct-G0-v02-interior.png` |
| G3 | [activos/croquis/pajaro.jpg] | conjunto + verde, vista aérea | 0.75 | masas legibles | reservar si tarda |
| G4 | [activos/croquis/LAMINAS-baja.jpg] (recorte) | fidelidad al color Photoshop | 0.45-0.55 + IPAdapter 0.5 | no lavar lo editado | keeper candidata |

## Negativo fijo

```text
blurry, low quality, distorted, watermark, text, cartoon, deformed, people, cars
```
