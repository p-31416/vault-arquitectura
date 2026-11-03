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

### gx-B-01 segunda vuelta — foto Fluk + estilo croquis — 2026-11-02 23:54

- Probamos: geometría `catenaria-flux-2026-11-03.jpg` (foto Fluk: cáscara nervada + pináculos + plaza con gente y árboles) + estilo `azcona-croquis006.jpg`, mismo v2 (CN 1.0, strong 0.85, denoise 0.45). Salida: `P:\00-repos\ComfyUI\output\gx-B-01_00002_.png`.
- Sucedió: composición conservada (cáscara, pináculos, plaza) y por fin hay materia (metal, cielo, solado). Pero el detalle fino se derritió: gente fantasma, árboles en manchas verdes, interior embarrado, vidrio fundido. El estilo-croquis impuso tratamiento de dibujo sobre los detalles de la foto.
- Veredicto Sol: **descartar** ("hizo cualquier cosa").
- Solución: preservar la foto — denoise 0.45→0.3, style 0.85→0.5 (solo tinte), CN 1.0→0.8. Próxima: gx-B-03.

### gx-B-01 — IPAdapter calco→estilo v2 512 — 2026-11-02 23:27

- Probamos: calco `azcona-croquis002.jpg` (fachada líneas) + estilo `azcona-croquis006.jpg` (aérea marcador gris + verde leve), CN canny 1.0, strong style 0.85, denoise 0.45, 50 pasos CFG 3.0.
- Config: Juggernaut v9, 512², seed 42. Salida: `P:\00-repos\ComfyUI\output\gx-B-01_00001_.png`.
- Sucedió: geometría clavada (el CN funcionó, sin deformación) pero sigue croquis: apenas un verde lavado, nada de sunscreen metálico ni hormigón. Causa raíz: la referencia 006 **es otro croquis** (grises + verde leve), no el editado Photoshop con materiales — el IPAdapter copió fielmente... un estilo de croquis.
- Veredicto Sol: **descartar** ("pésima").
- Solución: apuntar el nodo estilo al verdadero editado Photoshop con materiales (sunscreen, hormigón, vidrio, verde) + aflojar CN a 0.7 + denoise 0.6 para que las superficies puedan materializarse. Próxima: gx-B-02.

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
