---
tipo: prompt
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
origen: tablero Miro del curso AI x Gaudi (archademy.ai) - fila 140 del export CSV "AI-course.csv"
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, prompt, json, rhino-to-image, camera-lock, curso-ai-gaudi]
---

# Esqueleto JSON del prompt Rhino-to-Image

> Plantilla de salida del prompt de sistema: es lo que va al nodo CLIPTextEncode.
> Las claves `STRICT CAMERA LOCK` y `MATCH CAMERA OF IMAGE 1 EXACTLY` son las que
> traducen "geometria bloqueada" en lenguaje de prompt.

```json
{
  "scene": "[1–2 sentences. 'A professional highly detailed realistic architecture photography of {typology}. STRICT CAMERA LOCK: Match Image 1 perspective.' Then one sentence naming the transformation: the massing of Image 1 re-skinned in the materiality of Image 2.]",

  "subjects": [
    {
      "description": "[1–2 sentences. State massing preserved exactly from Image 1, then name the facade/material system taken directly from Image 2 (its surfaces, colour, finish). Replace pink figures with realistic pedestrians. No joint details or mm dimensions.]",
      "position": "[1 sentence. Spatial placement relative to Image 1's composition.]",
      "action": "[1 short phrase. Static quality or kinetic impression.]"
    }
  ],

  "style": "[Single sentence. Name the aesthetic/materiality character read directly from Image 2 (no architect reference). Photography by Iwan Baan and {one other photographer}. Phase One IQ4, {lens}, {film stock}, grain/aberration notes.]",

  "color_palette": ["#______","#______","#______","#______","#______","#______"],

  "lighting": "[1–2 sentences. Light quality taken from Image 2: time of day, diffusion, shadow character, interior glow if visible.]",

  "mood": "[2–3 adjectives, then one sentence connecting the mood directly to the atmosphere of Image 2.]",

  "background": "[1–2 sentences. Site, terrain, sky — regionally authentic to the user's stated location. Replace green massing volumes with Piet Oudolf-style vegetation appropriate to that region. Keep brief.]",

  "composition": "[1–2 sentences. 'MATCH CAMERA OF IMAGE 1 EXACTLY.' Then name the perspective type and what it emphasises.]",

  "camera": {
    "angle": "[Short phrase matching Image 1.]",
    "lens": "[Lens choice only.]",
    "depth_of_field": "[Aperture and focus in one phrase.]"
  }
}
```
