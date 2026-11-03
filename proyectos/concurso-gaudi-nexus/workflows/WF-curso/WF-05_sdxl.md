---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-05, txt2img, maqueta, 3d]
idioma: es
---

# WF-05 — Maqueta aislada 1024² (preparación 3D)

> JSON: `workflow_WF-05_sdxl.json` · 7 nodos · 1024×1024 · seed 5 · 30 steps · cfg 4
> Estado: sin validar contra servidor (R4 pendiente).

## 1. Qué tipo de flujo es

**Txt2img de objeto aislado.** Genera el módulo catenario como maqueta sobre fondo gris neutro, en vista de tres cuartos y con sombras suaves. Es la imagen de entrada del flujo imagen→3D (`Tripo`, `Hunyuan3D`, `Meshy`).

El prompt evita deliberadamente el contexto urbano: fondo limpio y objeto centrado, para que el modelo 3D tenga silueta clara.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

Alternativa: **RealVisXL v5.0**, que resuelve mejor el fondo neutro y las sombras de estudio. Comparativa en [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "isolated catenary module maquette, branching fractal column study, neutral grey studio background, soft shadows, product photography, three-quarter view, sharp geometry edges" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo del set **+ "cluttered background, people"** |
| 4 | `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | 1024×1024, batch 1 |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, denoise 1,0, seed 5 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF05-prep3d` |

## 4. Parámetros y por qué

| Parámetro | Valor | Razón |
|---|---|---|
| Resolución | 1024×1024 | Objeto centrado, margen parejo en los cuatro lados |
| Steps | 30 | Bordes limpios sin gastar tiempo |
| CFG | 4 | Fidelidad al concepto de maqueta |
| Seed | 5 | Fija la silueta de partida |
| Negativo extra | `cluttered background, people` | Fondo limpio para el recorte 3D |

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Fondo blanco puro | "neutral grey" → "pure white seamless background" | Mejor para recorte automático |
| Vista frontal | "three-quarter view" → "front elevation view" | Más fácil de modelar, menos información de volumen |
| Vista superior | "top-down orthographic view" | Útil para planta en 3D |
| Material de maqueta | Añadir "white plaster model" o "cardboard model" | Cambia de render a maqueta física |
| Objeto más complejo | Añadir "two modules joined" | Sube la dificultad del 3D |
| Serie de vistas | Cuatro corridas con seeds distintas y mismo prompt | Cuatro caras del módulo |

Para imagen→3D conviene una sola pieza, bien separada del fondo, con sombra suave y sin elementos delgados que el modelo 3D pueda fusionar.

## 6. Qué mirar en el resultado

Silueta cerrada del módulo, columnas que nacen y mueren dentro del cuadro, sombra única y coherente, fondo uniforme, bordes nítidos en la unión de material y aire.

## 7. Pendientes

- R4 contra `/object_info`.
- Definir el nodo de imagen→3D (Tripo / Hunyuan3D / Meshy) y su costo por generación.
