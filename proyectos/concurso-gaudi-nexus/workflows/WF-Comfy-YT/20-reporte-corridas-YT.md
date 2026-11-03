---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: Reporte corridas YT-Nexus — probamos / sucedió / funcionó
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: borrador-activo
tags: [concurso, gaudi-nexus, reporte, pruebas, comfyui]
idioma: es
---

# Reporte corridas YT-Nexus — probamos / sucedió / funcionó

> Hoja viva punto a punto que pide Sol: qué probamos, qué sucedió, funcionó o no, miniatura, configuración, y si no funcionó cuál fue la solución. Entrada más nueva arriba. Binarios en `salidas/` fuera de git, aquí solo referencia + miniatura. Prompts en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/10-prompts-prueba-nexus|10-prompts-prueba-nexus]]. Fondo Sagrada en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/11-diez-formas-sagrada-familia|11-diez-formas-sagrada-familia]]. Matriz madre en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|00-matriz-pruebas-concurso]].

## Template por corrida (copiar)

```
### gx-X-NN — P-0? / F-0? — fecha
- Probamos:
- Config: modelo + sampler/steps/CFG/seed + resolución + denoise + JSON
- Miniatura: ![[salidas/gx-X-NN.png|420]]
- Sucedió:
- Veredicto Sol: keeper / no funcionó
- Solución si no funcionó:
- Costo/tiempo:
```

## Corridas

### Pendiente — P-01 captura Google + dibujo (F-03 depth 0.5)

- Probamos: pendiente primera corrida Sol
- Config: RealVisXL Lightning 4 pasos CFG 1.5 seed 42 1216×832 denoise 0.5
- Miniatura: —
- Sucedió: —
- Veredicto Sol: —
- Solución: si inventa Sagrada → bajar a 0.4 o pasar a F-01 inpaint con máscara

### Pendiente — P-03 croquis → croquis mejorado

- Probamos: pendiente
- Config: SDXL + markerhandsketch 0.5 denoise 0.35 512 R1
- Miniatura: —
- Sucedió: —
- Veredicto Sol: —
- Solución: si se fotorrealiza solo → bajar denoise a 0.3 y quitar upscale

---
*Más nuevo → más arriba. Log: 2026-11-02 creación hoja reporte viva a pedido Sol.*
