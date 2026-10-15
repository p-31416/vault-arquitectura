---
tipo: indice
mvp: 04.02
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [mvp_04.02, comfyui, readme, paso-a-paso]
---

# README — MVP 04.02

> Puerta de entrada. Si es tu primera vez con ComfyUI, seguí este orden exacto.

- [[#Orden de lectura]]
- [[#Paso a paso para correr WF-01]]
- [[#Si algo falla]]

## Orden de lectura (15 min)

1. Este README (estás acá).
2. [[proyectos/MVP_04.02-comfyui-arquitectura/pbook-comfy_setup|pbook-comfy_setup]] — qué instalación usamos (manual Python + conda env, NO Desktop App en esta fase).
3. [[proyectos/MVP_04.02-comfyui-arquitectura/comfy-tratamiento-datos|comfy-tratamiento-datos]] — regla del estudio: concursos y datos de cliente, SOLO en local.
4. [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] — obligatorio antes de crear o modificar un WF (escalado 512, nomenclatura `n_XX-{L}-{NN}.png`).
5. [[proyectos/MVP_04.02-comfyui-arquitectura/WF-01-planta-ilustrada/WF-01-planta-ilustrada|WF-01-planta-ilustrada]] §2 — modelo sugerido para el primer test.

## Paso a paso para correr WF-01

1. **Lanzar ComfyUI:** doble-click al acceso directo del escritorio `ComfyUI RX570 (Background)` → esperar `[OK]` → abrir `http://127.0.0.1:8188`.
2. **Preparar input:** exportar la planta a PNG (negro sobre blanco, sin cotas chicas ni textos) → guardar como `WF-01-planta-ilustrada/inputs/planta-01.png`.
3. **Cargar workflow:** arrastrar `WF-01-planta-ilustrada/workflow_planta_canny_v1.json` a la UI.
4. **Setear nodos:** según §3 del WF (LoadImage → tu planta, Canny strength 0.9 / end 0.8, checkpoint ArchitectureRealmix).
5. **Prompts:** según §4 del WF (planta ilustrada, NO render perspectivo).
6. **Correr 3 veces** (seeds distintas) → guardar en `salidas/` como `n_01-F-01.png`, `n_01-F-02.png`, `n_01-F-03.png`.
7. **Registrar** cada corrida en §5 del WF (más nuevo arriba).
8. **Evaluar** en §6 y decidir el siguiente WF.

## Si algo falla

- Puerto 8188 sin respuesta → relanzar el `.bat` del escritorio (NO duplica instancia: avisa si ya corre).
- OOM / VRAM llena → botón `Free VRAM` en la UI o reiniciar; detalle en [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] § Troubleshooting.
- Canny no guía → strength ≥ 0.8, end 0.8, ImageScale lanczos 512 (ver §3 del WF).
