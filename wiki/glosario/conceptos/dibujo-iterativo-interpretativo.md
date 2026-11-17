---
tipo: concepto
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [dibujo, iteracion, controlnet, modulo-feria, croquis-render]
idioma: es
---

# Dibujo iterativo interpretativo

Método del estudio donde el croquis a mano con precisión disponible guía a la IA, que traduce dirección marcada hacia materia constructiva en iteración continua.

- [[#Definición]]
- [[#Sistema modular feria — octógono hacia triángulos]]
- [[#Loop escribir-referenciar-marcar-iterar]]
- [[#ControlNet interpretativo — del trazo a viga-columna]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Definición

**Dibujo iterativo interpretativo** — escribir intención + aportar imagen de referencia + marcar y dibujar arriba + IA que interpreta + volver a dibujar.

Nace del tablero técnico elegido a los 7 años y del gusto por dibujar como modo de pensar. La mano abre el proyecto, la máquina acompaña con resolución construible. Fuente primaria en [[raw/sessions/2026-11-12-sesion-filosofia-tablero-modular|sesión tablero modular 2026-11-12]].

## Sistema modular feria — octógono hacia triángulos

Octógono / hexágono que se parte en 2, 3, 4 hacia triángulos que conforman otra pisada. Conviven piezas enteras y fragmentos.

Cada fragmento porta un espacio de feria con modulación compartida, que funciona junto con vecinos y funciona con autonomía propia. Misma matriz en doble lectura: en abierto como feria extendida sobre plaza, en cerrado como mercado modular contenido. Ensayado en contexto [[proyectos/concurso-gaudi-nexus/index|Gaudí Nexus]], con alcance conceptual que trasciende el concurso hacia otros croquis.

## Loop escribir-referenciar-marcar-iterar

1. Texto con intención propia — lo que quiero lograr escrito en lenguaje natural
2. Imagen de referencia — tipo Google como base material y atmosférica
3. Trazo encima — marco y dibujo arriba con la precisión disponible en ese momento
4. Respuesta IA — interpreta el conjunto y devuelve materia y atmósfera
5. Nuevo trazo — ajusta dirección y vuelve a iterar

La precisión humana aporta dirección, la IA aporta resolución constructiva. La pluma como ritual muestra la oportunidad: trazo siempre disponible, con papel digital que recibe marca inmediata.

## ControlNet interpretativo — del trazo a viga-columna

Canny / Scribble como puente interpretativo, que toma líneas marcadas y las vuelve viga y columna de hormigón, vano y cubierta, con lógica constructiva legible.

Aplica [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas workflows]] R1 escala de entrada + R2 escala por modelo + R4 validación estática, en niveles n_02 croquis → render y n_03 ControlNet de [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04]]. Filosofía madre en [[proyectos/MVP_01-dibujo_ia/00-filo-mvp_01|filo MVP_01]]: lenguaje natural como interfaz entre lo que pienso y lo que aparece en pantalla.

## Conceptos relacionados

- [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] — supervisión y firma humana en cada iteración
- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — diseño del sistema que produce arquitectura
- [[wiki/glosario/conceptos/diseno-colaborativo|diseno-colaborativo]] — co-diseño humano + máquina
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] — raw hacia entidades hacia wiki como memoria computable
- [[proyectos/MVP_01-dibujo_ia/00-filo-mvp_01|filo MVP_01]] — manifiesto dibujo asistido por IA
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas workflows]] — R1, R2, R4 para croquis y ControlNet

## Referencias

- ControlNet original — Adding Conditional Control to Text-to-Image Diffusion Models (Zhang, Rao, Agrawala): https://github.com/lllyasviel/ControlNet — 200 verificado 2026-11-12 — Canny, Scribble, Depth como controles espaciales
- ComfyUI Wiki — guías y workflows de la comunidad: https://comfyui-wiki.com — 200 verificado 2026-11-12 — referencia práctica para nodos ControlNet en ComfyUI
- `raw/sessions/2026-11-12-sesion-filosofia-tablero-modular.md` — fuente primaria voz Sol
