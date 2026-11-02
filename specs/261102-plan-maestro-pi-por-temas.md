---
tipo: metodologia
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [pi, plan-maestro, hermes, mcp, modelos, licencias, gaudi, moodboard-lora]
idioma: es
---

# Plan maestro PI por temas — del 1 a 5 al sistema

> Fuente primigenia: [[raw/sessions/2026-11-01-sesion-tabula-rasa-pi|tabula rasa]] + diseño en [[specs/261101-tabula-rasa-arquitecto-futuro-pi-os|PI OS]].
> Base vigente: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].

## T1 Reunión → documentación

Hoy: Fathom graba, agente guía hace PM, cal.com pendiente en VPS.
Propuesta: webhook Fathom → n8n agrupa meetings repetidos → minuta con decisiones + compromisos con fecha → Leantime + recordatorio Telegram + mail con formato casa que envía persona.
Cierre: AC-14 una sola entrada por reunión, AC-15 aviso previo, AC-16 mail desde compromisos.

## T2 Agentes y reparto — cuántos y qué hace cada uno

PI Manager coordina. Pipi CAD audita y documenta. Pipi Rhino modela + Hops + exporta. Pipi Visual opera ComfyUI por API. Pipi BIM inspecciona IFC. Pipi Docs cura fuentes y wiki. Pipi PM sostiene agenda y métricas.
Hoy resuelto: Rhino 2D/3D + Rhino→imagen. En curso: paramétrico con catenarias Gaudí + Comfy a fondo.
Cada skill versionada con entradas, herramientas, validación y evidencias. Cada ejecución mejora memoria con aprobación.

## T3 MCPs — conexiones con documentación

| Capacidad | Servidor MCP | Doc oficial verificada | Estado |
|---|---|---|---|
| Hermes base, memoria, skills, cron, webhooks | hermes-agent | https://hermes-agent.nousresearch.com/docs/ | verificado 29/10 en IMPLEMENTACION §15 |
| Orquestación determinista | n8n-official | https://hermes-agent.nousresearch.com/docs/ | preset n8n-official contra endpoint propio |
| Drive lectura puntual | drivemcp.googleapis.com/mcp/v1 | https://developers.google.com/workspace/drive/api/guides/configure-mcp-server | Developer Preview, OAuth agente desde 11/11/2026 |
| Rhino local | puente propio 9876 + Hops | https://developer.rhino3d.com/guides/compute/hops-component | puente local, Hops oficial |
| Rhino headless candidato R2 | Rhino.Compute | https://developer.rhino3d.com/guides/compute/compute-faq | a evaluar, billing core-hour en Server |
| ComfyUI visual | comfy-mcp por API | https://github.com/comfyanonymous/ComfyUI | API + colas, workflows versionados |
| IFC abierto | IfcMCP + IfcOpenShell | https://ifcopenshell.org/ | con FreeCAD, hasta IFC real |
| Vault + registro | mcp propio estudio | [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#5 · El contrato entre componentes\|ESTRUCTURA §5]] | file_ref + sobre de tarea |

Seguridad: Tailscale tailnet, cero puertos públicos, backend Docker 3GB, `approvals.mode: manual`, `cron_mode: deny`, toolset mínimo por ruta, secretos en `.env` 600 fuera del repo.

## T4 Modelos — matriz open / pago / cloud / local

Estrategia: probar con mismo prompt y seed 42, medir tiempo, VRAM, costo y licencia comercial.

| Uso | Local | Cloud excepción | Nota |
|---|---|---|---|
| Texto, clasificación, contratos privados | Qwen3, Llama 3.1 en Ollama | OpenRouter solo puntual | contratos y firmas permanecen locales |
| Imagen base | SD1.5 + LoRAs casa | — | iteración rápida RX570 |
| Imagen final | SDXL Juggernaut + LoRAs | Comfy Cloud demo, Runpod Secure derivado | matriz txt2img vigente |
| Video | LTX-2 local corto | cloud por lote | Seedance queda como referencia externa |
| 3D | ComfyUI-3D-Pack en pod | — | geometría editable valida en Rhino |

Regla: workflow permanece estable, modelo rota por compatibilidad de nodos y licencia.

### T4.1 Entradas — validación punto 1

Escala de esfuerzo que pediste: texto primero, croquis después, referencias como plus. Cada nivel abre un flujo distinto con resultado comparable.

| Nivel | Qué le pasas a la IA | Flujo | Nodos clave | Parámetros guía |
|---|---|---|---|---|
| L0 Texto solo | prompt + estilo + cámara | txt2img | `CheckpointLoaderSimple → CLIPTextEncode → KSampler → VAEDecode` | SD1.5 512² cfg 7-8 steps 20-30 euler_ancestral karras / SDXL 1024² cfg 3-4 dpmpp_2m / FLUX.1 prosa cfg 1 steps 20-28 |
| L1 Texto + referencia | foto material, moodboard, imagen previa | IPAdapter / ReferenceLatent | `LoadImage → ImageScaleToTotalPixels → IPAdapter / ReferenceLatent → KSampler denoise 0,5-0,75` | FLUX.2: geo 1,0 MP + mat 0,5 MP lanczos, LoRA 0/0,6/0,8/1,0 |
| L2 Croquis mano / tablet / escaneo | lápiz, tinta, línea gruesa | img2img + Sketch/Canny | `LoadImage → ImageScale 512² → CannyEdgeDetector → ControlNetApplyAdvanced → KSampler denoise 0,6-0,9` | SD1.5: denoise 0,65 base, 2 ControlNet en serie si suma sketch |
| L3 Gráfico técnico | planta, corte, volumetría sombreada, render arcilla | Depth / Normal / Lineart | `LoadImage → DepthAnything / Lineart → ControlNetApply → KSampler` | preserva geometría, denoise 0,4-0,6 para no deformar |
| L4 Collage | recortes, fotos mixtas, entorno + objeto | Segmentación + inpaint/outpaint | `SAM → máscara → InpaintModelConditioning → KSampler denoise 0,7-1,0` / `Outpainting` para cielo/entorno | máscara feather 32-64, Tile para coherencia |

Controles disponibles, todos versionados como letra F con subíndice:

- Canny: bordes y croquis, el más fiel al trazo.
- Depth / Normal: volumetría y escala, el que sostiene 3D→imagen.
- Lineart / Sketch / Scribble: dibujo a mano y tablet.
- Segmentation: collage por zonas, cada máscara con prompt propio.
- IPAdapter / ReferenceLatent: estilo y material sin copiar geometría.
- Tile / Upscale: RealESRGAN_x4plus + 2.º KSampler denoise 0,15-0,35 para lámina.
- Inpaint: cambia fachada, vano o material dentro de máscara.
- Outpaint: extiende entorno, cielo y contexto urbano.
- OpenPose: personas de escala en recorridos.

Contrato por corrida: modelo declarado + prompt copiable + negativo solo en SD1.5/SDXL + cadena `A → B → C` + resolución/steps/cfg/sampler/seed/strength + log en `02-WF-log` con nomenclatura `n_XX-{A-G}-{NN}` y `gx-` en concurso. R1 escala a 512² en SD1.5, R2 a megapíxeles en FLUX.2, R4 valida contra `/object_info` antes de encolar.

## T5 Licencias y legal por jurisdicción

CABA, conurbano y Europa comparten exigencia de trazabilidad y cambian código y firma. Plano como documento legal Ley 24.335: cada entrega ata archivo, versión, parámetros y aprobador.

| Programa | Esquema | Implicancia estudio | Verificación |
|---|---|---|---|
| Unreal | gratis hasta 1M USD facturación anual, asiento en EULA Epic | habilita custom y VR en MVP sin costo inicial, escala a gemelo y recorrido | verificar EULA vigente + fecha en spec antes de facturar |
| Twinmotion | paraguas Unreal, sin API pública | asistido R3, Hermes prepara y persona ejecuta, ideal para anteproyecto rápido | verificar límite y modo offline en T&C |
| Rhino | compra perpetua + upgrade pago, educa con límite comercial | puente + Hops hoy, Compute a evaluar, licencia por puesto atada a Zoo/Cloud Zoo | verificar T&C educa vs comercial + Core-Hour $0,10 en Server antes de presupuestar |
| AutoCAD | suscripción estudio, completa habilita Core Console y APS Design Automation | auditoría y publicación headless avanzan con completa, LT avanza hacia lectura | verificar titularidad y APS en cuenta Autodesk |
| ComfyUI + SD/SDXL/FLUX klein | GPL + OpenRAIL + Apache 2.0 según pieza | solo modelos con licencia comercial permisiva, nada entrena con material estudio, Runpod con DPA y borrado | matriz por modelo con link y hash |
| FreeCAD, Blender, IfcOpenShell, Qdrant, n8n self-hosted | libres | base del sistema propio, primera opción en cada pieza nueva | verificar GPL/AGPL/LGPL por servicio |

Jurisdicción: Capital Federal avanza con código local + encomienda + firma registrada. Conurbano avanza con municipio + visado previo. Europa avanza con normativa local + concurso digital con entrega trazable. El sistema guarda jurisdicción por proyecto y propone checklist y plantilla.

Para tokenización futura: firmas digitales + licencias comerciales trazables desde hoy abren puertas en concursos internacionales digitales. Cada activo guarda licencia, firmante, hash y fecha.

## T6 Gestión interna + obra

Leantime como tablero, Telegram por obra con temas, libro de obra digital con foto + fecha + tags + incidencia + resolución, catálogo con EXIF + Qwen-VL, portal de iteraciones en vez de mail, cuaderno digital tipo libro ligado a wiki.

## T7 Firma local privada

OLlama local para contratos, inserción firma digital, mantenimiento programado. El sistema global recibe hash y acta, el contenido sensible permanece en la máquina.

## T8 Moodboard → estilo → LoRA

Teléfono alimenta `activos/moodboard/<proyecto>/` con fecha y autor. Hermes etiqueta con Qwen-VL, propone tags y archiva con procedencia. Cada ciclo corre flujo que genera moodboard sintético con 6-9 variantes comparables. La selección curada por persona alimenta dataset con licencia verificada para LoRA de estilo casa con versión, trigger, strength calibrado 0/0,6/0,8/1,0 y validación en matriz. Loop: acumular → sintetizar → curar → entrenar → versionar → reutilizar. El LoRA resultante vive como capacidad versionada del estudio, con ficha, ejemplos y límites de uso.

## T9 Evolución diaria

Curador archiva skills sin uso, lint semanal propone sin aplicar, métricas: trazabilidad 100%, autonomía junior, ahorro, éxito >95%, costo por ejecución visible. Cada ejecución deja entidades, topics y hechos.

## Flujo ejemplo — lámina entrega concurso Gaudí

1. Reunión breve + Fathom → minuta con alcance lámina.
2. Rhino parametriza catenarias con Hops, exporta vistas y cortes.
3. CAD audita y arma hoja A3 1:50 con rótulo.
4. Visual corre txt2img + img2img croquis + ControlNet + 3D a imagen.
5. PM arma paquete con índice, Docs registra procedencia, persona aprueba y envía.
6. Cambio de modelo marca dependientes `stale` y propone rehacer.

Base concurso: [[proyectos/concurso-gaudi-nexus/00-index|Gaudí Nexus]] + [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso]].
Rol que dirige: [[specs/261101-guion-visual-pi-remotion|holoarquitecto]]. Overview: [[specs/261102-system-overview-pi|system overview]]. Ingeniería: [[diagramas/pi-system-ingenieria|pi-system-ingenieria]].

## Próximos pasos

1. T0 inventario solo lectura Windows enchufada + M20.
2. Tailnet + runner prueba `audit_dwg` + `rhino_scene_info` en carpeta `vault://pruebas/`.
3. Cal.com en VPS + webhook Fathom.
4. Matriz Comfy concurso + portal mínimo.
5. Catenarias paramétricas Gaudí como test GH.
