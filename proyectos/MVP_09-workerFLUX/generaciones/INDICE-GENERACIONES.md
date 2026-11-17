---
tipo: indice
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-13
tags: [mvp09, generaciones, registro, miniaturas, evidencia]
idioma: es
---

# Índice de generaciones — worker + Pollinations

> Registro visual de corridas (estilo `INDICE-RENDERS.md` de Comfy, pero para el agente/API): cada fila trae miniatura, modelo, costo y veredicto. ~50 pruebas entre `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/` (barrido + batería W + casa + croquis) y `activos/worker-aiz/salidas/` (serie Twinmotion + NanoBanana).

## Barrido Pollinations 2026-11-03 (13 imágenes)

| Miniatura                                                                                                      | Modelo              | Costo  | Veredicto                   |
| -------------------------------------------------------------------------------------------------------------- | ------------------- | ------ | --------------------------- |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux-2026-11-03.jpg)          | flux schnell        | 0.002  | ✅ base exploración          |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-zimage-2026-11-03.jpg)        | z-image-turbo       | 0.004  | ✅ nítido instantáneo        |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux-interior-2026-11-03.jpg) | flux schnell        | 0.002  | ✅ interior                  |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-flux11pro-2026-11-03.jpg)     | flux 1.1-pro        | 0.03   | ✅ lámina                    |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-klein-2026-11-03.jpg)         | klein-4b            | 0.005  | ✅ gran match                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-maiflash-2026-11-03.jpg)      | mai-flash 2.6       | 0.02   | ✅ texto GAUDI NEXUS legible |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-sdxlfree-2026-11-03.jpg)      | sdxl-lightning-free | 0      | ⚠️ débil                    |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-sana-2026-11-03.jpg)          | sana                | 0.0001 | ❌ fuera de brief            |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-kontext-vano-2026-11-03.jpg)  | kontext             | 0.03   | ✅ conserva+cambia (vano)    |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/catenaria-kontext-lamas-2026-11-03.jpg) | kontext             | 0.03   | ✅ conserva+cambia (lamas)   |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/sagrada-plaza-2026-11-03.jpg)           | flux                | 0.002  | ✅ contexto Sagrada          |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/agente-lamina-2026-11-03.jpg)           | agente              | —      | ✅ vía agente                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/agente-firstclass-2026-11-03.jpg)       | agente              | —      | ✅ 334 KB                    |

## Cloudflare 2026-11-12 (cuenta propia)

| Miniatura                                                                                              | Modelo                     | Costo medido            | Veredicto               |
| ------------------------------------------------------------------------------------------------------ | -------------------------- | ----------------------- | ----------------------- |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-schnell-cascara-01.jpg)      | schnell 1024²              | 172.8 Neurons (~58/día) | ✅ base cáscara          |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-klein-edit-ref1-01.jpg)      | klein-4b edit 1 ref        | ~125 Neurons            | ✅ respeta geometría     |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-klein-seed42-01.jpg)         | klein-4b + seed 42         | —                       | ✅ seed aceptado         |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-klein-2refs-01.jpg)          | klein-4b 2 refs            | —                       | ✅ multi-ref OK          |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/sana-saldo-test-2026-11-12.jpg) | sana (Pollinations)        | 0.0001 Pollen           | ✅ pasa con saldo mínimo |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-tm-ext01-volumen.jpg)        | klein-4b edit (captura TM) | Neurons día             | ⏳ primer volumen TM     |

## Batería consistencia W (misma base cáscara)

| Miniatura                                                                                                                                                                             | Cambio                    | Veredicto                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------- |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-1-invierno.jpg)                                                                                           | W1 invierno               | ⏳ tu veredicto                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-2-noche.jpg)                                                                                              | W2 noche                  | ⏳ tu veredicto                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-3-madera.jpg)                                                                                             | W3 madera glulam          | ⏳ tu veredicto                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-4-aerea.jpg)                                                                                              | W4 aérea (límite)         | ✅ bárbaro                     |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-5-multiref.jpg)                                                                                           | W5 2 refs                 | ⏳ tu veredicto                |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-6a-seed42.jpg) ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-6b-seed42.jpg) | W6 seed 42 ×2             | Bytes distintos: seed no fija |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-7-guid-8.jpg) ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-w-7-guid-1_5.jpg) | W7 vano guidance 8 vs 1.5 | ⏳ comparar deriva             |

## Serie casa BA entre medianeras

Base: ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-casa-base.jpg)

| Miniatura | Cambio |
|---|---|
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-casa-h-1-noche.jpg) | H1 noche, luz cálida |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-casa-h-2-lluvia.jpg) | H2 lluvia, asfalto mojado |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-casa-h-3-aerea.jpg) | H3 aérea, techo + manzana |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-casa-h-4-vano.jpg) | H4 portón vidriado, resto idéntico |

## Batería T1 — misma casa, dos contextos (2026-11-17)

Prompt: hormigón a la vista de tablas + aluminio negro + madera + voladizo, estilo moderno. Escena A = manzana BA entre medianeras; escena B = misma casa en campo.

| Miniatura | Prueba | Veredicto |
|---|---|---|
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t1a-schnell-manzana.jpg) | P1A schnell CF: manzana (172.8 N) | ✅ hormigón + aluminio + voladizo |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t1b-schnell-campo.jpg) | P1B schnell CF: campo (172.8 N) | ✅ mismo lenguaje, arboleda + tierra |
| ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t1a-klein-manzana.jpg) | P3A klein CF edit sobre P1A (multipart, guidance 3.5) | ✅ frontal simétrico + lamas madera |
| — | P2 schnell Pollinations (grants) | ⏳ bloqueado: balance 0.0007 < 0.002 |

Hallazgo: klein-4b en CF **no tiene txt2img** (exige imagen) — P3 = edit sobre P1, todo en nube, nada local.

## Croquis reales Tigre → render (centro cultural)

| Croquis                                                                                     | Render                                                                                                               | Veredicto                                                                           |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| ![](../../../activos/croquis/pajaro.jpg) (aéreo conjunto)                                   | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-croquis-tigre-pajaro-aereo.jpg) (950 KB)   | ✅ layout respetado                                                                  |
| ![](../../../activos/croquis/azcona-croquis001.jpg) (contrapicado)                          | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-croquis-tigre-azcona-fachada.jpg) (716 KB) | ✅ gesto intacto                                                                     |
| proxy bordes casa                                                                           | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-croquis-a-render-01.jpg) (696 KB)          | ✅ calibración                                                                       |
| ![](../../../activos/croquis/croquis-fin0006.jpg) (croquis centro cultural)                 | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t9-croquis-fin0006.jpg)                    | ✅ hormigón + hierro negro + deck madera + parasoles perforados + motion blur        |
| corrección: piel = aluminio microperforado (no hormigón) + fuera columna hormigón 1er plano | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t9b-croquis-fin0006.jpg)                   | ❌ sin cambio: el modelo ignoró el edit (2 variables juntas)                         |
| solo quitar columna (guidance 8)                                                            | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t9c-croquis-fin0006.jpg)                   | ✅ solo columnas negras, resto idéntico                                              |
| piel = hormigón revestido con paneles perforados fijos a nivel ventana                      | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t9d-croquis-fin0006.jpg)                   | ⚠️ sin cambio real: dif 13.6/255 = ruido, el edit no aterriza                       |
| desde cero: croquis + prompt completo corregido (piel aluminio + solo columnas negras) | ![](../../../activos/proyectos/concurso-gaudi-nexus/pollinations-tests/cf-t9e-croquis-fin0006.jpg) | ❌ veredicto SOL: hizo cualquier cosa (pierde el encuadre del croquis) |

Prompt T9 (copiar a NB/Flow): `Photorealistic close-up of an exterior double-height space in a cultural center, at the eye level of a person standing on the upper floor. Background: exposed concrete structure, columns and beams. Thin black steel columns and floating railing. Wood deck floor. A person in the foreground leaning over the railing with slight motion blur. Exterior cladding of Hunter Douglas type sunscreens: modular perforated aluminum panels with different perforated dot transparency patterns. Second plane: concrete structure. Far background: museum interior structure with distant curtain wall. Overcast daylight, phone photo.`

## Serie worker-aiz — Twinmotion → klein (2026-11-12, `activos/worker-aiz/salidas/`)

Fuentes en `activos/worker-aiz/fuentes/` (original + *-512 para la API). Hallazgos de la serie: receta fiel = solo materiales + guidance 1.5; sanitarios exactos se fijan en TM (klein insiste en wall-hung); ventana marco negro lograda, inodoro con pie no logrado.

### Exterior (STO + aluminio negro)

| Miniatura | Prueba | Veredicto |
|---|---|---|
| ![](../../../activos/worker-aiz/salidas/ext01-volumen-v2.jpg) | v2: STO gris oscuro + baranda hierro | ✅ v2 |
| ![](../../../activos/worker-aiz/salidas/ext01-volumen-v3.jpg) | v3: STO + 1 buña lineal única + corredizas aluminio negro | ✅ v3 (muro derecho bajo pendiente: próxima captura TM) |
| ![](../../../activos/worker-aiz/salidas/ext01-volumen-v3-MOD.jpg) | Variante MOD sobre v3 | ⏳ tu veredicto |

### Baño 1 (microcemento + porcelanato)

| Miniatura                                                        | Prueba                           | Veredicto           |
| ---------------------------------------------------------------- | -------------------------------- | ------------------- |
| ![](../../../activos/worker-aiz/salidas/bano1-microcemento.jpg)  | Base: microcemento + porcelanato | ✅ base baño         |
| ![](../../../activos/worker-aiz/salidas/bano1-cielorraso.jpg)    | Cielorraso junta tomada          | ✅                   |
| ![](../../../activos/worker-aiz/salidas/bano1-madera-negro.jpg)  | Madera + negro                   | ⏳ tu veredicto      |
| ![](../../../activos/worker-aiz/salidas/bano1-guid15-minimo.jpg) | Guidance 1.5, cambio mínimo      | ✅ receta fiel       |
| ![](../../../activos/worker-aiz/salidas/bano1-flux2dev.jpg)      | Vía flux-2-dev                   | ⏳ comparar vs klein |

### Interiores TM (dormi / estar / baños / lavadero)

| Miniatura                                                    | Prueba                  | Veredicto                               |
| ------------------------------------------------------------ | ----------------------- | --------------------------------------- |
| ![](../../../activos/worker-aiz/salidas/dormi-render.jpg)    | Dormi fiel (materiales) | ✅ render (fiel fino pendiente de cuota) |
| ![](../../../activos/worker-aiz/salidas/episo-render.jpg)    | Estar fiel (materiales) | ✅ render (fiel fino pendiente de cuota) |
| ![](../../../activos/worker-aiz/salidas/bano2-render.jpg)    | Baño 2                  | ✅ render                                |
| ![](../../../activos/worker-aiz/salidas/lavadero-render.jpg) | Lavadero                | ✅ render                                |

## NanoBanana 2.1 (app, aporte SOL — `activos/worker-aiz/salidas/nano_banana-/`)

7 renders (origen: app de Gemini, fuera del agente; prompt inferido del nombre de archivo). Origen TM = miniatura de la captura de partida (`activos/worker-aiz/fuentes/`):

| Origen TM                                                    | Render NB                                                                                                        | Pedido inferido                                  | Veredicto |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --------- |
| ![](../../../activos/worker-aiz/fuentes/1P-BAÑO02-512.jpg)   | ![](../../../activos/worker-aiz/salidas/nano_banana-/necesito_que_renderices_fotorrealista_esta_a29cc741_2K.jpg) | Render fotorrealista baño ducha (2.7 MB)         | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/2P-LAVADERO-512.jpg) | ![](../../../activos/worker-aiz/salidas/nano_banana-/la_baranda_debe_continuar__horizontal__6eef7524_2K.jpg)     | Baranda continua horizontal en balcón (2.8 MB)   | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/1P-BAÑO-512.jpg)     | ![](../../../activos/worker-aiz/salidas/nano_banana-/agregale_a_la_puerta_algun_12925b20_2K.jpg)                 | Agregar [elemento] a la puerta del baño (2.1 MB) | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/EPISO-512.jpg)       | ![](../../../activos/worker-aiz/salidas/nano_banana-/EPISO.JPG_4d7f935b_2K.jpg)                                  | Estar (2.6 MB)                                   | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/1P-DORMI-512.jpg)    | ![](../../../activos/worker-aiz/salidas/nano_banana-/1P-DORMI.JPG_3e965650_2K.jpg)                               | Dormi (1.9 MB)                                   | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/ext-01-512.jpg)      | ![](../../../activos/worker-aiz/salidas/nano_banana-/ext-01.JPG_1ff2a4b7.jpg)                                    | Exterior ext-01 (356 KB)                         | ⏳         |
| ![](../../../activos/worker-aiz/fuentes/2P-LAVADERO-512.jpg) | ![](../../../activos/worker-aiz/salidas/nano_banana-/imagen_2b8be9d4.jpg)                                        | Lavadero, sin prompt visible (380 KB)            | ⏳         |
