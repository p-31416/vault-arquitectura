---
tipo: backlog
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, paralelo, backlog]
---

# 04-backlog — WF paralelo cloud ⊕ local

- [ ] **Arrancar ComfyUI local** y validar L1/L2 JSONs vía /object_info (R4)
- [ ] **Login Comfy Cloud** (comfy-cli → `jobs_list where:"cloud"`) y verificar plan/créditos
- [ ] Decidir checkpoint abierto equivalente en el cloud (L3) si Juggernaut XL no está
- [ ] Construir JSON de la **vía L4** con nodos API reales leídos de `list_api_nodes` (no a memoria)
- [ ] L4 requiere **créditos/API key**: confirmar credenciales antes de la primera corrida pagada
- [ ] brandless compare T3-02: si pixel-diff entre L1 y L3 sirve solo con el checkpoint idéntico — si no, lo marca como "no comparable" y pasa a timing-only
- [ ] **SDXL local = 651 s/corrida** (@tim) → los grids C de L2 se reparten en 2 sesiones (ver PLANS, presupuesto de tiempo)
- [ ] **SSD-1B aún sin descargar** (4,5 GB — para el futuro ControlNet Union SDXL, @tim §5/§6): pedir `s` + link HF cuando el bloque SDXL lo necesite (flujo-07)
- [ ] **Renders ya existentes ждать Reusar**: INDICE-RENDERS 94 renders + M01-M20 SD1.5 Sagrada → baseline del test D-migración (T1-12)
- [ ] **Registry triggers if needed**: los renders con estilo Gaudí que genere la matriz entran potencial al dataset del LoRA del concurso ([[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]], trigger `gaudinexusstyle` abierto)
- [ ] **Emplazamiento (fijar seeds de masa)**: @tim §7 — las corridas de masa WF-02 fijan seeds reusables para el inpaint sobre foto CC BY-SA en earth2rhino3d
- [ ] Después del bloque txt2img: migrar la misma matriz a los flujos 2 img2img → 3 img2video (n_07) → 4 img2 3D
- [ ] Capturas del proceso para el material de demostración (1.png "partida" side-by-side cloud-vs-local)
- [ ] ADR derivada: cloud vs local cuando terminen las 44 pruebas (~12+12+10+10)
