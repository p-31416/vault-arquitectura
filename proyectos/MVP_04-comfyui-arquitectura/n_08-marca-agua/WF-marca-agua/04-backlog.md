---
tipo: log
proyecto: MVP_04-comfyui-arquitectura
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [mvp_04, comfyui, marca-de-agua, backlog, n_08]
idioma: es
---

# 04-backlog — WF-marca-agua

- [x] Bug fondo negro (A-01) diagnosticado y fixeado en v1.1 con `ImageInvert` (máscara `1-alfa`).
- [x] Re-corrida A-02 con v1.1: marca pegada limpia, sin fondo negro.
- [x] Semántica de `blend_factor` verificada en A-02: 0.3 deja marca visible y sutil.
- [ ] Posición inferior-derecha automática (v2): leer tamaño de base con nodo de tamaño y calcular `x,y` en vez de fijos.
- [ ] Marca en mosaico / repetida (v2): tiling para fotos de entrega.
- [ ] PDF: fuera de Comfy (`LoadImage` no lee PDF); va por script/n8n — cuenta pendiente en [[proyectos/00-sistema-estudio|00-sistema-estudio]] §7.
- [ ] Encadenar con envío por mail ("mandame el proyecto tal"): n8nAttachments sobre la salida.
