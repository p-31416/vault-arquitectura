---
name: brand-voice
description: "Perfil de voz del estudio desde material real (memorias, propuestas, portfolio, mails que funcionaron). Se activa con voz del estudio, tono, perfila mi escritura. Produce VOICE PROFILE reutilizable para article-writing. No crea ficheros con huella de voz sin permiso explícito."
---

# Brand Voice — estudio de arquitectura

> Portado de `vault-lidia` (origen ECC). Acá la fuente no es X/launch-notes sino: memorias, propuestas de concurso ganadas, portfolio, mails a clientes/comitentes que funcionaron, `wiki/` madura. Sin material real no se inventa voz.

## When to Activate
- `voz del estudio`, `tono`, `escribe como nosotros`, `perfila mi escritura`
- Contenido recurrente (memorias, Instagram obra, portfolio, mails) necesita sistema reutilizable, no imitación one-off

## Source Priority (estudio)
1. Memorias/propuestas recientes que ganaron o conformaron al cliente
2. Portfolio y brochures (`activos/marketing/`)
3. Mails/notas a comitentes que funcionaron
4. `wiki/` y `documentacion/` de proyectos con tono ya asentado

## Workflow
1. Juntar 5-20 muestras; preferir recientes salvo que el usuario marque canónicas
2. Separar "voz concurso/portfolio" (pública) de "voz obra/interna" (trabajo) si se bifurcan
3. Extraer: ritmo/longitud, compresión vs explicación, tecnicismos vs llano, números/normas/materiales, transiciones, lo que nunca hace
4. Output: bloque `VOICE PROFILE` corto y reutilizable en sesión (no crítica literaria)

## Defaults estudio (si hay poco material)
- Directo, concreto, mensurable (m2, material, norma, plazo)
- Números y sistema constructivo antes que adjetivos
- Tono sobrio profesional AR; lunfardo/marketing solo si el material lo trae
- Sin humo startup ("disruptivo", "revolucionario", "excited to share")

## Hard Bans
- Hooks curiosos falsos, "no X, solo Y", "sin relleno", minúsculas forzadas
- Cadencia LinkedIn-thought-leader, preguntas bait, journey del fundador genérico

## Persistence
- Reutilizar último `VOICE PROFILE` confirmado en la sesión
- Solo guardar a disco (`wiki/estudio/voz-*.md` o donde pida SOL) con permiso explícito — nunca fichero trackeado con huella personal sin `s`

## Downstream
Canónico para `article-writing`, memorias, portfolio, mails. Si otro skill tiene media captura de voz, manda este.

## Origen
Portado de `P:\00-repos\pitau-tech\vault-lidia\.opencode\skills\brand-voice\SKILL.md`.
