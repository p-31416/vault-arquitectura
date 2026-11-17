---
tipo: log
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [sesion, pollinations, flux, agentes-n8n, pi-imagenes, spec, playbook, backlog]
idioma: es
---

# 2026-11-12 — Sesión pi imágenes: agente n8n + spec único + playbook + barrido

18. **Operativo hoy (balance real)**: GET con key 200 pero POST flux 402 (balance 0.0012, pide 0.0020); costo-0 community (dev-free, sdxl-free) devuelven 503 ambos; GET klein 512 anduvo una vez y luego 402 (goteo mínimo); sana POST 0.0001 pasa y se guardó `sana-saldo-test-2026-11-12.jpg` (37 KB, b64_json). Matriz klein queda esperando goteo/recarga/x402.

19. **Workers AI a fondo**: klein-4b acepta edición multi-ref (multipart input_image_0..3, steps fijo 4) — no es solo txt2img; FLUX.3 Image Klein nuevo (5.6B, 4K, Kommunity License <$5M); Comfy Cloud free actual = 5 corridas. Wiki actualizada (cloudflare-workers-ai.md + tabla licencias + free tier).

20. **Investigación modelos arquitectura**: qué significa open-weight en BFL; mapa nov-2026 (Qwen-2.1 #1 NC, FLUX3-Image-Klein Kommunity <$5M, klein4B Apache, Z-Turbo Apache); solo-GPU en 3 formas (pod/serverless/API); 8 creadores YT priorizados; recomendación (explorar klein4B, replicar FLUX3-Klein, LoRA propio en 4B). Volcado en `comfy-cloud-vs-runpod.md` (open weights, mapa, solo-GPU, creadores, recomendación + 5 refs).

## Qué se hizo (continuación, tarde)

11. **Aclaración dónde leer capacidades**: `pollinations.md` (F1–F6 línea 118, modelos gratis línea 235) = proveedor; `pbk-pi-imagenes.md` (Qué hace, Capacidades, Estado de cuenta, Mejoras) = agente.
12. **Verificación "videos de FLUX free"**: la mayoría de opciones murieron en 2026 (Together pasó a solo-lectura, fal/Replicate solo trial, AI Studio 429). Free real hoy: Pollinations con techo, Cloudflare ~230/día, Comfy local/Cloud-free.
13. **Comfy Cloud**: admitido que el free tier es demo (400 créd/mes), no tier de trabajo. Cloud = pago.
14. **Cloudflare Workers AI verificado** (docs 2026-10-20): 10.000 Neurons/día gratis, flux-1-schnell ~170 imgs/día, klein-4b ~80/día; REST `POST /client/v4/accounts/{ID}/ai/run/...` conectable al agente vía HTTP Request (pide cuenta + token). GLM 5.3 ahí exige pago; LLMs free: llama/qwen/gpt-oss/glm-4.7-flash.
15. **Licencias FLUX verificadas** (BFL oficial): klein 4B/4B Base Apache 2.0 (comercial libre) vs 9B/dev/kontext-dev Non-Commercial; schnell Apache 2.0. klein 4B = el que escala al hardware del estudio.
16. **Billing RunPod verificado** (docs): GPU por segundo con pod prendido (idle quema), storage separado (volumen parado $0.20/GB/mes), Stop vs Terminate, Serverless por ejecución. Hábito: modelos en network volume + Terminate. 2 h en 3090 ≈ $0.44.
17. **Wiki actualizada** (`comfy-cloud-vs-runpod.md`): secciones Licencias + Cómo cobra RunPod + 8 referencias verificadas 2026-11-12.
21. **ADR conclusión del mes**: `specs/261112-adr-modelo-antes-que-flujo.md` (aceptada) + entrada en `log.md`. Doctrina: modelo → hardware → flujo; carriles klein4B / FLUX3-Klein / Z-Turbo; camino en 5 pasos.
22. **Plan rumbo al miércoles**: `specs/261112-plan-pruebas-rumbo-miercoles.md` — GPUs estudio 12–16 GB (plan B: klein 4B fp8 + SDXL ControlNet), LoRA no se usa por ahora, cuenta Cloudflare existente (faltan Account ID + token para primera prueba).
23. **Reescritura del plan (decisiones firmes)**: base RealVisXL V5 BakedVAE (fuera Juggernaut/Lightning/SD1.5); Trellis MIT 24 GB = pod (GLB→Rhino); LoRAs SDXL (Arcviz/Massing/adondlin); sin video; camino croquis→partes→3D→Rhino validado por 5 referentes (denkaTa599, ArchiGen, Lescop, DesktopArchitect, eCAADe).
24. **Docs oficiales por modelo**: verificada `docs.bfl.ai/flux_3/flux3_image_klein` (200: upsampler obligatorio, pesos Comfy, guía LoRA) + índice oficial BFL completo + tutorial Comfy flux-3-klein (200); sección nueva en `modelos-imagen-arquitectura.md` con tabla doc/API/Comfy/pesos/guías por modelo.
25. **Cloudflare primera prueba real (cuenta usuario)**: token `pi_img_01` verificado activo (Workers AI Read+Write confirmados); schnell 1024² OK 769 KB / 172.8 Neurons (schema sin seed); klein-4b edit 1 ref OK 652 KB. Token expuesto en chat → rotar por `pi_img_02`. Imágenes: `cf-schnell-cascara-01.jpg`, `cf-klein-edit-ref1-01.jpg`.
26. **Rotación completa**: `pi_img_02` creada por el usuario, guardada en `.env`, verificada activa.
27. **Playbook del primera clase actualizado**: `pbk-pi-imagenes.md` suma sección Vía Cloudflare (qué admite, costos medidos, reglas) + 2 filas en Capacidades + link cruzado.
28. **Agente conectado a Cloudflare**: credencial `cf-WorkersAI` creada por el usuario; tool `generar_cf` (HTTP schnell + header auth) agregado vía 2 mutaciones + instructions con carril CF como default; `validate_agent` OK; `call_agent` test BA OK (eligió generar_cf, caption con Neurons). Telegram: integrations vacío — nada conectado, nada pisado. Draft sin publicar.
29. **Sub-workflow IMG Generar CF** (`z0qOpgY5HT1kXoUL`, publicado): trigger prompt → CF schnell → Code b64→binario → EditImage resize 384 → Code bin→b64 → Set {image_data_uri, usage_json, motor}. Credencial existente asignada vía setNodeCredential. Tool del agente cambiado de nodo a workflow; instructions piden `![render](image_data_uri)`. Test pabellón OK: el agente embebió la imagen en markdown. Ver render real en Preview.
30. **Documento de capacidades**: `wiki/glosario/software/capacidades-agente-imagenes.md` — lo verificado hoy, operaciones por proveedor, Edit Image gratis, backlog fases 2-4 (15 ítems), afuera (video, LoRA, SD1.5). Link desde el playbook.
31. **Editar con referencia — SÍ se puede (2 vías)**: kontext URL (con saldo) + klein-4b multipart Cloudflare (cuota gratis). JSON rechazado por CF (multipart obligatorio); forma exacta n8n = `bodyParameters` con parameterType (docs verificadas). Sub-workflow `IMG Editar CF` (`oNRtmK7lSesgx3cQ`, 8 nodos, publicado): baja URL → resize 512 → klein multipart → thumb 384 → data URI. Tool `editar_cf` agregado al agente + instructions; `validate_agent` OK; test placeholder→pabellón OK con imagen embebida. Playbook fase 2 ítem 1 cerrado.
32. **Batería worker**: klein-4b acepta seed (42 OK, 184 KB) y 2 refs (316 KB OK); klein-9b error interno 3043 en 1024 y 512 (reintentar); chat completions qwen3-30b OK (cerebro gratis de respaldo). Imágenes: `cf-klein-seed42-01.jpg`, `cf-klein-2refs-01.jpg`.
33. **Batería consistencia W1–W7** (spec `261112-bateria-worker-consistencia.md`): misma base real `cf-schnell-cascara-01-512.jpg`; invierno/noche/madera/aérea/multi-ref/seed×2/guidance 8vs1.5 — 9 JPG generados (`cf-w-*`). Seed 42 no idéntica a nivel byte. Mapeo Comfy→worker en el spec.
34. **Serie casa BA**: base `cf-casa-base.jpg` (medianeros + calle) + 4 edits misma imagen: noche, lluvia, aérea, vano vidriado (`cf-casa-h-*`). Hallazgo: seed no fija imagen en destilados; consistencia = referencia, no seed.
35. **Croquis→render**: proxy de bordes `cf-croquis-proxy-512.jpg` → `cf-croquis-a-render-01.jpg` (696 KB) OK. Falta prueba con croquis real del usuario.
36. **Croquis reales Tigre (activos/croquis)**: `pajaro.jpg` (aéreo conjunto) → `cf-croquis-tigre-pajaro-aereo.jpg` (950 KB): pabellones bajos + patios + río, respeta layout; `azcona-croquis001.jpg` (contrapicado fachada) → `cf-croquis-tigre-azcona-fachada.jpg` (716 KB): hormigón visto + reveals, gesto del croquis intacto. Croquis→render VALIDADO con material del estudio.
37. **Reporte visual**: primero en `specs/261112-reporte-bateria-worker-imagenes.md`, movido a `proyectos/MVP_09-workerFLUX/generaciones/INDICE-GENERACIONES.md` — las ~30 pruebas con miniaturas embebidas, prompts, veredictos y trazabilidad.
38. **Miniaturas faltantes — causa y fix**: los embeds usaban `\|300` (pipe escapado, Obsidian no renderiza) + 5 typos de rutas (`gaudiange`, `proyectosDto`, `concurso/gaudi`, `pollrations`, `lamas-2023`) + un archivo con coma (`cf-w-7-guid-1,5.jpg` renombrado a `1_5`). Verificado 37/37 enlaces contra disco.
39. **MVP_09-workerFLUX documentado**: `00-index.md` + `01-agente-pi-imagenes.md` (tools, skills, corridas, pendiente) + `flujos/IMG-Generar-CF.md` + `flujos/IMG-Editar-CF.md` (nodos, credencial, lección multipart, costos).
40. **Miniaturas, causa final**: el `|` de `![|300]` rompía las celdas (pipe = separador de columnas) → texto literal + tabla dividida. Fix: `![](...)` sin tamaño. Archivo limpio, 37/37 enlaces verificados.
41. **Reescritura limpia del índice**: el primer bloque de la tabla había quedado con formatos mezclados (`![ | 300]`); archivo reescrito completo, tablas compactas 4 columnas, sin pipes dentro de celdas. Verificado sin restos.
42. **Brief Twinmotion**: carpeta `activos/capturas_tm/` creada; brief de estilo en `proyectos/MVP_09-workerFLUX/brief-estilo-tm.md` (exterior Tarquini + aluminio negro; interiores muebles realistas, escalera abierta, látex blanco, cielorraso junta tomada; baños microcemento + porcelanato). Pruebas de a una cuando lleguen las capturas.
43. **TM ext-01 (primera captura real con marcas)**: `activos/capturas_tm/ext-01.JPG` → `cf-tm-ext01-volumen.jpg` (411 KB). Marcas rojo/azul eliminadas; torre izquierda gris con buñas horizontales (volumen diferenciado); muro azul apenas más bajo; carpinterías negras con paños vidriados (PB conserva un partidor medio — iterar si molesta).
44. **Carpeta worker-aiz**: `activos/worker-aiz/{fuentes,salidas}/` creada; ext-01 + ref 512 copiadas a fuentes. Reintento v2 (`salidas/ext01-volumen-v2.jpg`, 609 KB, guidance 8): buñas más finas, Tarquini gris con grano, ambas ventanas corredizas arriba, luz de mañana suave. Muro derecho apenas bajó (reintentar más fuerte si hace falta); PB con partidor central propio de corrediza de 2 hojas.
45. **ext-01 v3** (`salidas/ext01-volumen-v3.jpg`, 485 KB, guidance 8): corrección del usuario — NO rallado: revoque plástico texturado tipo STO gris oscuro en torre + gris claro resto + UNA buña lineal única por nivel; baranda de hierro en terraza; ambas ventanas torre corredizas. Marcas fuera, cámara intacta. Pendiente: altura muro derecho (quedó para próximo ajuste).
46. **ext-01 v4** (`salidas/ext01-volumen-v4.jpg`, 435 KB, sobre v3 limpia con tus 4 marcas amarillas): buñas con rehundido y sombra; baranda moderna de barrotes al filo de losa separada de la carpintería; raja superior con marco negro; ventana superior en oscilo-batiente abierta con manija. Cámara y materiales intactos.
47. **v4 ELIMINADA** por pedido (hizo cualquier cosa). Interiores: recorte de iconos TM (crop 45px) + resize 512 de las 5 capturas a `worker-aiz/fuentes/`. **Baño 1** (`salidas/bano1-microcemento.jpg`, 558 KB): microcemento gris con llana + porcelanato gran formato + artefactos en su lugar — layout intacto, muy bueno.
48. **Baño 1 iteraciones**: recorte derecha 12% (`bano1-recorte.jpg`) + cielorraso al filo de ventana y sin papel (`bano1-cielorraso.jpg`, 426 KB, sin ver aún) → piso porcelanato símil madera + carpinterías negras (`bano1-madera-negro.jpg`, 525 KB): ducha/mampara/espejo/grifería en negro mate, veteado madera en piso, cielorraso bajo, sin papel. Muy bueno.
49. **Baño inodoro (límite del modelo)**: `bano1-inodoro-ventana.jpg` (544 KB) ventana con marco negro OK pero inodoro colgado; reintento explícito `bano1-inodoro-pie.jpg` (501 KB) sigue colgado + artefacto logo. klein-4b insiste en wall-hung (sesgo de training). Decisión: inodoro exacto se modela en Twinmotion, no por IA.
50. **Un render por captura** (`salidas/`): `dormi-render.jpg` (600 KB, ropa de cama realista + junta tomada), `lavadero-render.jpg` (482 KB, lavarropas + pileta + blancos), `episo-render.jpg` (555 KB, estar abierto + escalera + muebles diseño), `bano2-render.jpg` (615 KB, microcemento + porcelanato + inodoro de pie visible). Los 4 conservan cámara y layout.
51. **Interiores densos — límite klein-4b**: con restyle grande inventa/mezcla detalles. Antídotos probados sobre baño 1: `bano1-guid15-minimo.jpg` (444 KB, guidance 1.5 + 1 sola variable = fiel al original) y `bano1-flux2dev.jpg` (588 KB, FLUX.2-dev anda en CF: más rico pero deriva la cámara). Regla: interiores = 1 variable por pasada + guidance baja; exteriores = klein libre.
52. **Cuota CF agotada**: error 4006 daily free allocation (10k Neurons) tras ~25 generaciones. Resetea 00:00 UTC (21:00 AR). Reintentos fieles de dormi/estar quedan para mañana.
53. **Precios NB + FLUX 3 (2026-11-13)**: catálogo vivo parseado con Python (437 modelos). NB2.1 oficial ~$0.039 vs OpenRouter ~$0.03–0.05 (empate); proxies community vendouple $0.10 / tomdacatto $0.25 con paid=False (salen de grants; probe: pide balance ≥0.1, tenemos 0.0008). FLUX 3 en Pollinations (klein + full $0.05064) y pesos klein-comfy para pod 24GB. CF sigue en 4006 a las 03:02 UTC — reset no cayó a medianoche, ver dashboard.
54. **Cierre 2026-11-13 00:05 AR**: MVP_09 documentado (índice, agente, 2 flujos, registro visual 37/37 OK en Obsidian); agente con 5 tools (CF default) validado y testeado; worker-aiz con serie TM (ext v2/v3, baño×4, 4 interiores, regla fidelidad); pendientes: cuota CF (ver dashboard), Telegram ID + publish, klein-9b, dormi/estar fieles, proxies NB con grants ≥0.1.
55. **Veredicto nube-vs-Comfy + dashboard (2026-11-13)**: asentado en batería (sección Veredicto) y ADR (adenda); INDICE-GENERACIONES actualizado a ~50 pruebas (serie worker-aiz + NanoBanana app + cf-tm-ext01). Regla: exploración/estación/hora/mood/croquis → nube; geometría, identidad, print, privacidad → Comfy.

## Qué se hizo

1. **Workflow Eval Telegram** (`YLrbR8z4sPHPnJBy`): modelo cambiado de gemini legacy a `flux.1-schnell`, caption a flux, auth simplificada a Header Auth, credencial `ppi-Pollinations(sk-)` creada en UI y enlazada por MCP. Quedó verificado sin warnings, inactivo, pendiente activar + `poll: hola` real.
2. **Barrido Pollinations (13 imágenes guardadas)**: flux, z-image, interior, flux.1, klein-4b, mai-flash (cartel GAUDI NEXUS legible), sdxl-free, sana (fuera de brief), kontext vano + lamas (loop conserva+cambia validado x2), agente-lamina, agente-firstclass, plaza.
3. **Spec único** (`specs/261103-spec-ajuste-pollinations-flux.md`): consolida plan T1–T10, variantes, conexiones, registro y agente. Wiki intacta.
4. **Wiki nueva**: `pollinations.md` (registro como generador, flujos F1–F6, límites, por qué gratis), `modelos-imagen-arquitectura.md`, `flux1.md`, referente `black-forest-labs`, backlog F6–F8 en `30-backlog-futuras-pruebas.md`.
5. **Agente de primera clase `pi imágenes`** (`FWGtRuylIqexTigj`): creado tras corregir projectId (`pWOSkiVhnAWt5tSi`) y modelo a `openrouter/z-ai/glm-5.3-flash` (alias con `~` rechazado). 3 tools node + skill genérica + skill concurso con when-use. Validado OK, `call_agent` OK (cabaña genérica + exploración Gaudí).
6. **Workflow agente `Emilia Imagenes - Telegram`** (`neldyz3v1gz5cZ7q`): Telegram Trigger + AI Agent GLM + memoria + parser + extractor con fallback texto + envío foto. Debug real: modelo con `~` inválido, dims como string dan 400, parser con schema auto-generado erróneo, regex sin comillas, URL con wrapper. Test punta a punta OK salvo envío (chat de prueba falso).
7. **Sub-workflow `IMG Generar`** (`voMAYlv6d280QjSW`, publicado): GET determinista para que el agente genere sin `$fromAi` en URL (restricción del runtime).
8. **Playbook** `pbk-pi-imagenes.md`: capacidades, manual de uso, recetario, lentes, ciclo de mejora, checklist, billing real, mejoras pendientes.
9. **Billing real**: grants agotados tras ~18 generaciones (POST y GET con key → 402, anónimo 401 throttled). NanoBanana analizada: toda `paid_only`, NB2.1 ~0.034, Pro ~0.134. x402 desde $0.01 como vía de recarga.
10. **Investigaciones**: mejor abierto/cerrado/arquitectura (Qwen-2.1 vs Apache-2.0, NBP vs FLUX.2 Pro), FLUX.2 Dev tutorial Comfy vs RunPod, endpoint edits (sin mask, kontext sí), comparativa GLM vs GPT Luna vs Haiku (GLM gana precio).

## Archivos modificados

- `specs/261103-spec-ajuste-pollinations-flux.md` (reescrito 2 veces: consolidación + solo-agente)
- `wiki/glosario/software/pollinations.md` (nuevo + registro generador)
- `wiki/glosario/software/modelos-imagen-arquitectura.md`, `flux1.md`, `referentes/black-forest-labs.md` (nuevos)
- `wiki/glosario/interno/pbooks/pbk-pi-imagenes.md` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas.md` (F6–F8)
- `activos/.../pollinations-tests/` (13 jpg)
- n8n: Eval actualizado, `Emilia Imagenes - Telegram`, `IMG Generar` publicado, agente `pi imágenes` draft validado
- `scripts/pollinations_eval.py` creado y eliminado (el usuario prefirió plan en spec)

## Pendiente mañana

1. Chequear saldo Pollen (1 GET barato); si 402, recargar x402 o esperar grant.
2. Matriz klein vía Pollinations (seeds 7/21/42 + interior + vs flux).
3. ID de Telegram del usuario para `allowedUsers` + `s` para publicar agente y conectar canal.
4. Decidir Eval vs Agente (mismo bot, un solo activo).

## Análisis cerebro-digital

**Topics:** agente primera clase vs nodo AI, $fromAi restricciones, billing Pollen real, loop conserva+cambia, spec único, playbook operativo, replicabilidad local/cloud.

**Entidades:** pi imágenes (FWGtRuylIqexTigj) · GLM 5.3 Flash · IMG Generar (voMAYlv6d280QjSW) · Eval (YLrbR8z4sPHPnJBy) · ppi-Pollinations(sk-) · Pollinations (flux/kontext/mai/z-image/klein/sana) · NanoBanana paid_only · x402.

**Hechos:**
- El agente de primera clase funciona de punta a punta con tests reales; el bloqueo fue billing, no código.
- Los grants diarios tienen techo real (~18 imgs mixtas); el anónimo también throttlea por IP.
- `$fromAi` no va en URL (restricción runtime) → patrón sub-workflow publicado como solución.
- Dims Pollinations exigen números; strings dan 400 siempre.
- Klein API ya probado con gran match; klein Comfy local imposible (9.2GB vs 8GB); mañana klein vía Pollinations de nuevo.
- Falta el ID de Telegram del usuario para cerrar Parte 2 y publicar.
