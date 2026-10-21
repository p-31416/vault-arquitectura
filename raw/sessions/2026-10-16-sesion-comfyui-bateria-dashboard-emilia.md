# Sesión 2026-10-16 — batería ComfyUI + dashboard demo Emilia

## Qué se hizo
- Batería 5h en RX 570 (ComfyUI 0.28.0, cola libre): 1.1.2 stack (196s) + matriz WF-05 2.0.x 0.4/0.6/0.8 (120/143/143s) + outpaint 4.0.0 (273s, casa vecina sin corte) + SDXL 2.0.0 (651s, pabellón dusk) + F8 Canny+LoRA (210s, geometría idéntica, estilo no entra a denoise 0.5 → hipótesis F8b 0.65-0.7).
- WF-04/05/06 + WF-03 docs actualizados: §5 con miniaturas, §9 logs, WF-04 §2 inventario + §3 nodo por nodo + backlog (agente foto/cine, LoRA propio SANAA/OMA con receta).
- Creados: WF-04 (6 JSON), WF-05 (+2.1.0), WF-06 (2 JSON), WF-03 F8 JSON, PLAN F1-F8 → 04.02/PLANS con mapeo a WF existentes.
- Inpaint con SOL: MaskEditor/mask-output/MaskToImage, regla blanco=reemplaza; F-02/F-03: el prompt manda (ventanas→muro), diagnóstico @sherlock registrado en WF-02 §6 (máscara vacía, polaridad, grow 16-32, InpaintModelConditioning).
- Modelos: 2 LoRAs + RealESRGAN a P:, workspace default P:, 00-index 04.02 con WF-04/05/06.
- Dashboard `presentacion/dashboard-comfy.html`: 36 miniaturas, tiempos medidos (~2.7'/img), estilo 05-propuesta modo oscuro con 4 tabs, galería ordenada por versión, links a salidas/JSONs/carpetas/Obsidian, Mes 2 + logros. Linkeado con dashboard-mes1.

## Archivos clave
- `proyectos/MVP_04.02-comfyui-arquitectura/{WF-04-serie-txt2img,WF-05-img2img-croquis,WF-06-inpaint-outpaint,WF-03-serie-controles,WF-02-inpainting-ventanas,00-index.md,PLANS/}`
- `proyectos/STUDIO_OS-Emilia/presentacion/{dashboard-comfy.html,dashboard-mes1-emilia.html}`
- `proyectos/MVP_04-comfyui-arquitectura/RESUMEN-flujos-probados.md`

## Pendiente
- F8b (denoise 0.65-0.7), WF-03 T2 + F-B/C JSONs, WF-06 3.0.x/4.0.1, WF-02 test 2, backlog LoRA propio, backlog agente foto/cine.

## Cerebro-digital
- Topics: comfyui-bateria, lora-ladder, inpaint-debug, dashboard-emilia, mcp-paralelo.
- Entidades: Realmix, Juggernaut-XL-v9, markers-1.0, archisketch-0.8, RealESRGAN, SD1.5-inpainting.
- Hechos: sweet spots markers≈1.0/sketch≈0.8-1.0; tradeoff img2img+LoRA 0.65/0.8; CN retiene identidad pero frena estilo a denoise bajo; seed fija=reproducibilidad; ~2.7 min/img medidos.
