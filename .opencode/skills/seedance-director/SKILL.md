---
name: seedance-director
description: "Director de prompts de video Seedance 2.0 (notación EN+ZH del curso AI x Gaudi). Convierte una descripción de escena en un JSON array con prompt EN + ZH: action (persecución, duelos), general (paisajes, viajes, atmósfera) y diálogo (confrontación, interrogatorio). Se activa cuando SOL pide un prompt de Seedance, describe una escena para video, o pide desglose de escena cinematográfico. Para otros modelos de video usar el reference video.md del skill comfy-prompting."
---

# seedance-director — skill de video Seedance 2.0

Fuente: sticky `seedance-director` del curso AI x Gaudi (archive verbatim: `references/fuente-verbatim-01.md`). El texto original del curso queda literal en la fuente; acá está el contrato resumido y las reglas duras del estudio.

## Qué hace

Recibe una descripción de escena en texto plano (+/− imágenes de referencia) y devuelve **solo un JSON array** con dos objetos: `{"lang":"en","prompt":"..."}` primero, `{"lang":"zh","prompt":"..."}` después. Sin explicaciones, sin markdown, sin texto alrededor. Prompt = una línea continua con etiquetas inline:

`Style & Mood:` → `Narrative Summary:` (opcional) → `Dynamic Description:` → `Static Description:` → `Audio:` (sólo diálogo)

**Chinese = native rewrite**, no traducción: sintaxis natural de director de cine chino (~1.800 chars hard cap; recorte en orden Narrative → Static → Style → Dynamic nunca entero).

## Reglas de extracción

- **Tipo de escena**: action / general / dialogue (o híbrido). Decide el set de arquetipos.
- **Duración**: la que pidan; default 10 s; **hard cap 15 s**.
- **Cámara**: todo movimiento/ángulo que SOL nombre (`dolly in`, `low-angle`, `tracking`) **debe** aparecer en el prompt final, EN y ZH — instrucción del user overridea defaults.
- **Inventario silencioso** previo: personajes, locación, props, estilo/atmósfera. Personajes y props vienen de lo que SOL dio; lo ambiental (dust, sparks, partículas) y el comportamiento de cámara se pueden añadir. Excepción: si el pedido implica crear la escena ("armá un paisaje", "dos tipos peleando"), se inventa el soporte (locación, props, ambiente) — los personajes nombrados conservan solo los atributos dados.
- **Regla de edad (CRITICAL)**: nunca describir personajes por edad en ningún idioma; etiquetas funcionales ("a figure in a wool cloak") o rol + ropa + acción.

## Arquetipos (router)

- **Action**: Persecución / Duelo (ventaja alternada, nunca > 1 beat consecutivo; dominancia continua = asalto unilateral) / Impacto.
- **General**: Journey / Reveal / Atmosphere (nada cambia; el mood ES el contenido).
- **Dialogue**: Confrontación / Interrogatorio / Negociación. ~25–30 palabras habladas caben en 15 s; si hay más: conserve el power-shift + 1 setup + 1 reacción, lo demás → comportamiento físico.

## Reglas del motor Seedance (de la fuente)

- Beats de acción = intención + técnica nombrada, no biomecánica: "spinning back kick connects" sí; la descomposición articular ("el antebrazo rota 45°") se comprime al nombre del golpe. Fuerza y dirección ("driven into the car, metal buckling") sí; la enumeración paso a paso del desastre, afuera.
- Continuidad espacial se re-ancora después de cada corte (posiciones + dirección).
- ≤ 3 personajes trackeados; par de acción + vector de interacción por shot.
- Salida de frame = corte implícito: lo que sale de frame desaparece para el resto del shot; la coreografía salida + re-entrada queda para shots separados.
- Reflejos (en peines, hojas, charcos, espejos) se evitan: Seedance distorsiona la geografía de escena al renderizarlos; se describe lo visible o audible en directo ("The air smells of pine" no; "Pine needles covering the ground, wind moving through branches" sí).
- Micro-expresiones como física ("jaw clenches, nostrils flare") sí; etiquetas de emoción ("looks angry") se convierten en el gesto físico que las muestra.
- Cortes: **double contrast obligatorio** (cambia shot size + modo de cámara en cada corte); regla de 180°; inserts de 0,3–0,5 s beat-free con motivo causal y sujeto nombrado.

## Antislop (palabras prohibidas EN)

breathtaking, stunning, captivating, mesmerizing, awe-inspiring, masterfully, meticulously, exquisitely, beautifully crafted, cinematic masterpiece, visual feast, a symphony of, seamlessly, effortlessly, flawlessly, cutting-edge, state-of-the-art, next-level, rich tapestry, vibrant tapestry, kaleidoscope of, elevate, unlock, unleash, harness, groundbreaking, a testament to, speaks volumes, resonates deeply. (Lista ZH completa en `references/fuente-verbatim-01.md`.)

Regla de positivo del vault: en lugar de negar, elegís el término concreto que sí hace el trabajo ("pale gold rays", "fern-covered floor", "lens flare in CineStill register").

## Referencias de cámara (apéndice A)

Angles (low/high/dutch/bird's-eye/worm's-eye/eye-level/OTS) · focales 14–24/35–50/85–200/macro · movimientos (tracking, dolly, crane, pan, tilt, whip-pan, orbit, push-in, pull-back, handheld, Steadicam, aerial) · slow-motion/speed ramp/freeze · transiciones (smash cut, match cut, whip-pan, hard cut, L-cut). Tabla EN+ZH en la fuente.

## Cómo se usa en el estudio (adaptación)

1. La llamás con `@tim video seedance <escena>` o `@tim seedance <descripción>` — Tim pasa por acá, no por el reference `video.md`.
2. El output JSON va directo al prompt de Seedance 2.0 (web/RunPod); el `<Audio>` conserva el idioma original del diálogo, sin traducir.
3. Si hay imágenes de referencia (Rhino, foto de contexto), se usa la notación `<<<image_n>>>` con leyenda antes del primer label.
4. Para LTX-2.3 o Kling 3.0 se sigue usando `references/video.md` del skill ComfyUI; esta skill es especifica de Seedance 2.0.
5. La corrida se registra según `reglas-workflows-comfy.md` y sumá la fila a [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas|04-bitacora-corridas]] cuando sea repetible.
