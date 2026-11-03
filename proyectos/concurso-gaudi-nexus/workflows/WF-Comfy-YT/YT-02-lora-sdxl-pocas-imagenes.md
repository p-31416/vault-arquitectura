---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: YT-02 — Entrena tu LoRA con pocas imágenes en SDXL
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: pendiente-ver-video
tags: [concurso, gaudi-nexus, comfyui, youtube, lora, sdxl, kohya, dataset]
idioma: es
---

# YT-02 — Entrena tu propio LoRA con POCAS imágenes en SDXL

> Video pasado por Sol 2026-11-02 (ítem 15 playlist). Estado: ficha creada con metadatos verificados vía búsqueda; transcripción completa pendiente de ver el video. Relevancia directa: Plan B kohya SDXL de [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §4 + estrategia dataset chico para `gaudinexusstyle`.

## 1. Video

- Título: "Entrena tu propio LoRA con POCAS imágenes en Stable Diffusion XL (Tutorial)" (ES).
- URL: `https://www.youtube.com/watch?v=IikYM9tb_GE&list=PLmQpFKkkTXQFj2NLaW8H1wjwQYGCbdZnc&index=15`
- Tesis: enseñarle al modelo tu estilo con pocas imágenes sobre SDXL.
- Recursos que cita (verificar al ver): imágenes regularización `https://github.com/ALEXOTANO/ai-regularization-images-man` + gist con preset de parámetros. Timestamp visto en índice: 10:28 Parámetros de entrenamiento.

## 2. JSON

Pendiente: extraer si el autor publica workflow (kohya SS o ai-toolkit) o reconstruir receta mínima (rank 16, LR 1e-4, 2000 steps) según plan.

## 3. Modelo

Base del video: SDXL 1.0 (licencia OpenRAIL, publicable). Para nosotros: si el dataset `gaudinexusstyle` no llega a 30–40 imágenes, esta receta de pocas imágenes es el camino; si supera, vale klein 4B según plan.

## 4. Nodos

Pendiente al ver: tabla función + link doc oficial (kohya SS GUI / ai-toolkit / Civitai on-site).

## 5. Cuadro de pruebas

- Pocas (8–12) vs dataset 40: ¿el estilo se fija o hace overfit?
- Con vs sin imágenes regularización del repo citado.
- Rank 8 vs 16 en SDXL.

## 6. Referencias

- Video: `https://www.youtube.com/watch?v=IikYM9tb_GE&list=PLmQpFKkkTXQFj2NLaW8H1wjwQYGCbdZnc&index=15`
- Plan: [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §2 (dataset) y §4 (Plan B kohya SDXL)
- Precedentes: [[proyectos/concurso-gaudi-nexus/lora-precedentes-estudios|lora-precedentes-estudios]]

---
*Más nuevo → más arriba. Log: 2026-11-02 creación ficha desde pedido Sol, metadatos verificados vía búsqueda, video pendiente de ver.*
