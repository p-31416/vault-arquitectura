---
tipo: spec
fecha_creacion: 2026-11-16
ultima_actualizacion: 2026-11-16
tags: [spec, plan, agentes, hermes, n8n, subagentes, imagen, emilia, deadline]
idioma: es
---

# Plan completo — agentes de imagen y conexión a Hermes

> De un humano → un agente → subagentes. Hermes (agente único del estudio, [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] §4) interpreta y delega; n8n ejecuta lo determinista; el vault es la memoria. Hito 1: **agente n8n funcionando mañana 16:00**. Hoja para Emilia el miércoles: **este plan** (§5 hitos + §7 carril miércoles + dashboard).

## 1. Estado actual (verificado)

- **Hermes diseñado** (MVP_07 VISION/ESTRUCTURA/REQUISITOS): un agente por estudio en el VPS (3 GB, sin puertos, long polling Telegram), MCPs → n8n / vault / registry / runner, memoria real = cuaderno digital en wiki, gobernanza A-D, `s` siempre. T1–T6 en ESTRUCTURA §9.
- **Agente n8n pi imágenes** (`FWGtRuylIqexTigj`): draft validado, sin publicar; cerebro GLM + memoria ON; 5 tools (2 Pollinations txt2img, kontext edit, 2 Cloudflare); sin Telegram.
- **Evidencia**: ~50 pruebas en [[proyectos/MVP_09-workerFLUX/generaciones/INDICE-GENERACIONES|dashboard]]; veredicto nube-vs-Comfy en [[specs/261112-bateria-worker-consistencia|batería]] + [[specs/261112-adr-modelo-antes-que-flujo|ADR]].
- **Formas.ai analizado**: orquestador sin modelo propio; habilidades a copiar en [[wiki/glosario/software/formas-ai|formas-ai]].

## 2. Arquitectura objetivo

```
SOL (Telegram, texto/voz/croquis)
 │ s aprueba C/D
HERMES (VPS, un agente: interpreta, parte el pedido, delega, registra)
 ├── MCP n8n → subagentes de imagen (flujos deterministas, §3)
 ├── MCP vault → memoria: filosofía del estudio, decisiones, briefs, planos
 ├── MCP registry → Postgres: tarea, ejecución, artefacto, aprobación
 ├── MCP runner → PC estudio (SSH atajo, luego P1+P3): ComfyUI, Rhino, archivos
 └── Telegram → grupos por obra + canal bitácora (hoy vía n8n, Hermes después)
```

Regla: Hermes nunca decide C/D; el render no viaja por mail sino al **portal** de iteraciones; la entrega al cliente la manda una persona.

## 3. Subagentes de imagen (n8n, tools del agente único)

| # | Subagente | Hace | Base técnica | Estado |
|---|---|---|---|---|
| S1 | generar / editar base | txt2img + conserva+cambia 1 variable | `generar_cf` / `editar_cf` / kontext | ✅ operan |
| S2 | site | site extraction (foto → contexto) | klein multi-ref | CABA pendiente |
| S3 | textura | busca, extrae 3 opciones, muestra; elección por texto | webfetch + Edit Image composite | a construir |
| S4 | geometria | máscaras por zonas, respeto de plano | Kontext edit (Paid Pollen) → ControlNet Comfy | a construir |
| S5 | estilo | Style Memory del proyecto | LoRA propio klein 4B (pod, ai-toolkit) | a entrenar |
| S6 | contexto | foto Google Maps/Streets como fondo | tool con nota legal de uso | a probar |
| S7 | entrega | galería comparativa + prompts + portal | Edit Image composite + upload | a construir |

### S7b. Loop por Drive (tablet sin Telegram)

Entrega triple: **imagen por Telegram + imagen en Drive + mail con link**. Orden: primero Telegram, después Drive-tablet (credenciales existentes).
Ida: el agente sube el render a `Drive/Obra/<obra>/iteraciones/<fecha>-<tema>/01-generada.jpg` + `prompt.md`, manda la imagen por Telegram y el link por **mail** (Gmail) — la tablet no tiene Telegram. Vuelta: SOL abre en la tablet, dibuja encima, la sube como `02-marcada-tablet.jpg`; el **Drive Trigger** de n8n la detecta (por nombre), la toma como referencia para el siguiente edit y avisa por mail que hay material nuevo. Regenerada cae como `03-regenerada.jpg`. Convención de nombres = el contrato; sin renombrar no hay loop. Ojo trampa 11/11: MCP oficial de Drive en preview (OAuth "AI-powered agent") — usar nodos n8n Drive (OAuth existente `ppi-EmiliaOS_Google Drive`) o espejo rclone, no el MCP directo.

Motores de pago SOLO vía OpenRouter (regla 16/11: Pollinations = solo grants gratis, Paid Pollen no se usa): Seedream 5.0 Pro $0.045 (geometría), GPT-image 2.6 a medir (collage/textura), Ideogram/Kontext/1.1-pro sin vía OR verificada (en espera), NanoBanana 2/2.1 ~$0.039 (interiores, también vía OR con crédito existente).

## 4. Conexión a Hermes (según ESTRUCTURA)

1. **T1 cimientos**: vault canónico + red privada + Hermes en VPS + MCP n8n (`https://n8n.pitau.tech/mcp-server/http`, entrada `n8n-official`) + SOUL + skills. El agente n8n de imagen se expone como tool ejecutora.
2. **Memoria**: MEMORY.md chica + cuaderno/wiki como memoria real; skills de imagen (`prompting-arquitectura`, site, textura, estilo) versionadas en el vault.
3. **Interfase**: Telegram hoy (bot n8n/Emilia), Hermes después; temas por obra, aprobaciones registradas. Migración con bot propio y rollback.
4. **Runner (Hermes sigue en el VPS, ESTRUCTURA §2+§3.1+§10)**: solo el runner alcanza la PC del estudio por red privada. Día uno: backend SSH de Hermes (atajo autorizado en ADR puente P1+P3). P1 proxy + P3 runner API entran cuando las tareas sean tool-calls, no comandos. Contrato: file_ref + riesgo + idem_key + provenance. PC apagada → runner_no_disponible.
5. **Límites duros**: Twinmotion sin API pública (asistido, la persona ejecuta); plantas IA en estado débil; 8 GB no corren 9B (pod = excepción); licencias NC fuera de cliente.

## 4.6 Vía 100% virtual — CAD/BIM sin la PC (verificado 2026-11-16)

Todo lo batch (cómputos, conversiones, reportes, inspección) corre virtual; la PC queda solo para lo interactivo.

| Necesidad | Vía virtual | Costo | Fuente oficial |
|---|---|---|---|
| AutoCAD: interrogar DWG, AutoLISP, plot a PDF/DWF | APS Automation API (motor AutoCAD en nube; sin verticales, sí Object Enablers) | 300 min/mes incluidos, luego tokens (~$3/12 min) | [Overview Automation API](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/) · [Tutorial AutoCAD](https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/autocad/) |
| DXF sin AutoCAD: cantidades, capas, áreas | `ezdxf` (Python, corre en el VPS) + ODA File Converter (DWG→DXF gratis) | $0 | ya en ESTRUCTURA §4.1 |
| Revit: cómputos, reportes, documentación | APS Automation for Revit (DB API completa headless) | 300 min/mes incluidos, luego tokens | [Overview](https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/) · [Tutorial Revit](https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/revit/) |
| Revit: inspección desde Hermes | **Revit MCP oficial** (tech preview, enchufa directo al agente) + AEC Data Model API (datos granulares + geometría) | según plan APS | [Anuncio DevCon 2026 + MCPs](https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services) |
| IFC: cómputos y modelo | IfcOpenShell + IfcMCP en el VPS Linux | $0 | ESTRUCTURA §4.3 |
| Rhino: geometría sin escritorio | Rhino.Compute en VM Windows cloud + Hops; conectores en vivo Revit↔Rhino (Data Exchange Live, preview) | VM + licencia Rhino | ESTRUCTURA §4.2 + anuncio Data Exchange Live (mismo blog DevCon) |

> Nota doctrina (un agente por estudio, VISION §6.9): el agente n8n pi imágenes (`FWGtRuylIqexTigj`) es tool/subagente S1–S7 invocado por Hermes vía MCP, no segundo agente autónomo. La 2ª instancia Hermes+Ollama local es perfil de modelo futuro, no desplaza el core del VPS.

## 5. Fases y fechas

- **Hito 1 — mañana 16:00**: agente publicado + Telegram conectado (falta ID de SOL + `s`) + límite diario grants medido + crédito OR verificado + cuota CF verificada + `dormi/estar-fiel`. Criterio: pedido por Telegram → imagen full-res en el canal.
- **Miércoles (Emilia)**: hoja única (este plan §5–§7 + dashboard) + demo en vivo del agente + **matriz de pruebas accesibles** (abajo).
- **T2**: S2 site CABA + S3 textura (3 opciones) + S6 contexto Maps.
- **T3**: S4 máscaras Kontext + Seedream/NB/Ideogram/GPT-2.6 como tools conmutables + comparativas lado a lado.
- **T4**: Trellis→GLB→Rhino (pod 24 GB) + S5 LoRA propio klein 4B.
- **T5–T6**: Hermes pleno con skills de imagen + portal de iteraciones + cuaderno ligado a wiki.

### 5.1 Protocolo escala gráfica (S8 paso 0) — sí tiene sentido

La barra de escala en la imagen + declaración textual ("trabajo en metros, la barra = 1 m") + **una dimensión testigo** escrita ("el frente mide 8.64 m") = el VLM calibra y el canvas fijo (1024 px = 10 m) mantiene proporción. El modelo no mide, pero **ancla**: contexto dibujado sobre plano + escala declarada → S8 redibuja → ezdxf/APS impone la medida real → CAD verifica. Sin dimensión testigo no hay escala, solo proporción.

### 5.2 Matriz de pruebas miércoles (<24 h, accesible)

| # | Prueba | Modelo nativo | Vía | Costo | Estado |
|---|---|---|---|---|---|
| 1 | Plano → render fiel | NanoBanana 2.1 (web, manual SOL) | app Gemini | $0 | en curso |
| 2 | Croquis → render | klein-4b (CF, si hay cuota) / sana (grants) | agente/CF | ~0 | cuota 4006 pte |
| 3 | Capacidades Pollinations | schnell/z-image/mai-flash/kontext | catálogo + probes | grants | ✅ parcial |
| 4 | Capacidades Cloudflare | schnell/klein-4b + Neurons por llamada | probe + dashboard | 10k/día | agotada, ver hora reset |
| 5 | Nativos OpenRouter | NB 2.1 (~$0.039) / NB2 (~$0.08) vía Images API | Images API + key existente | crédito OR | a probar |
| 6 | Cerrados pago | Seedream $0.045 / GPT sunburst / Ideogram $0.03 | OpenRouter o Paid Pollen | recarga $1–2 | gateado |
| 7 | Emulación abierta §6.4 | SDXL+CN / klein 4B / ezdxf | local/pod | $0–pod | plan §9 |

### 5.3 3D nativo vs pod — costos en detalle

Ningún modelo de imagen genera 3D nativo: el 3D sale por **reconstrucción** (imagen→3D). Sin pod: **fal Trellis $0.02**, Trellis 2 $0.05, Tripo $0.01/crédito, Hunyuan $0.015 — centavos por pieza, sin máquina. **Pod solo cuando**: entrenar LoRA (~$1–3), ControlNet local a escala, video. Costo pod 3090: $0.22/h prendido (idle quema) + volumen $0.10 corriendo / $0.20 parado + network volume $0.07/GB/mes; sesión 2 h ≈ $0.44. Regla: fal para piezas, pod para entrenamiento y volumen.

## 6. Del croquis al plano en escala + LoRAs propios del estudio

### 6.1 ¿El modelo lo sabe hacer de base? No — la escala se impone afuera

Ningún modelo de difusión maneja escala métrica real: dibuja plantas plausibles (probado en `WF01-planta`, MVP_04: ilustradas y B&W desde texto) pero sin medida. "10 px = 1 m" funciona como **convención de un pipeline controlado** (canvas fijo + escala fija + vectorizar + verificar en CAD), nunca como conocimiento nativo del modelo. Lo que el modelo sí entiende de un croquis: recintos, vanos, jerarquía de trazo (vía ControlNet scribble/lineart/MLSD + VLM tipo Qwen-VL del stack).

### 6.2 Flujo específico croquis → planta en escala (S8)

1. **Lee**: VLM interpreta el croquis (ambientes, vanos, norte) → programa textual.
2. **Redibuja**: SDXL + ControlNet (scribble/lineart/MLSD según etapa) sobre canvas de escala fija (ej. 1024 px = 10 m).
3. **Calibra**: vectorización + imposición de escala, capas, espesores y defaults del estudio (muro 0.15, vano 0.96) con `ezdxf` (VPS) o APS Automation (nube).
4. **Verifica**: el plano cae en CAD (MVP_01) y pasa standards (MVP_02); el humano firma.

### 6.3 LoRAs por etapa — la propiedad del estudio

Sí hace falta LoRA: uno por modo de visualización, o uno con triggers: `croquis-trazo` (idea), `anteproyecto` (masa + materia), `proyecto` (documentación + folleto). Entrenados sobre material del estudio en **klein 4B (Apache 2.0, render)** y **SDXL (planta)** con ai-toolkit en pod (~1–3 h c/u). Lo cerrado no admite LoRA propio (salvo finetune pago de BFL): **lo abierto es lo que queda**.

### 6.4 Qué se emula de cada modelo cerrado con pesos abiertos

| Cerrado (qué copia) | Emulación abierta (propiedad) | Brecha |
|---|---|---|
| Seedream: geometría | SDXL + ControlNet Union + CN por etapa | menos fotorrealismo crudo |
| NanoBanana: interiores | klein 4B + LoRA `anteproyecto` | 4 refs (no 14) |
| GPT sunburst: textura/collage | klein edit + banco de texturas del estudio (S3) | sin grounding web nativo |
| Ideogram: esquemas | SDXL + scribble + LoRA `croquis-trazo` | ninguna relevante |
| Formas: Style Memory, Viewpoint | LoRA de proyecto + seed fijo + misma referencia | a construir (S5) |

### 6.5 Conexión con todos los MVP

- **MVP_01 dibujo IA**: destino del plano vectorial (lenguaje natural → CAD, defaults, Lisp); S8 le entrega el DXF calibrado.
- **MVP_02 autocad standards**: valida capas/lineweights del plano generado.
- **MVP_03 gestión**: el plano entra al circuito de compromisos/entregas.
- **MVP_04 ComfyUI**: motores + ControlNets + `WF01-planta` (antecedente) + entrenamiento de LoRAs.
- **MVP_04.02 / 05 Rhino**: Hops/Compute para la geometría 3D que el plano referencia.
- **MVP_06 voz**: dictar el programa ("dormitorio al este") manos libres en obra.
- **MVP_07 Studio OS**: Hermes orquesta, vault memoriza, Telegram entrega.
- **MVP_08 casa moderna**: keeper F0 como referencia de identidad.
- **MVP_09 croquis-render**: S0–S3 locales (RealVis) = carril $0 del mismo pipeline.
- **MVP_09 workerFLUX**: carril API del mismo pipeline + dashboard de evidencia.
- **Casos** (aizpurua, tigre, gaudí): bancos de prueba por etapa.

## 7. Carril miércoles — base local + loop 3D (ex-plan 261112, integrado 2026-11-16)

Carril $0 en GPU del estudio; convive con el carril API (nube) y el carril pod. Base: `realvisxlV50_v50Bakedvae.safetensors` (SDXL fp16, ya instalado); ControlNets solo SDXL (Union / xinsir); LoRAs base SDXL/RealVis o propio después; SD1.5 y customs descartados; sin video este año.

### Camino validado por referentes

Croquis → render por partes con consistencia (seed + referencia fija, no regenerar) → imagen→3D → Rhino → iterar. Referentes: denkaTa (viewport→Canny+Depth+3 LoRA), ArchiGen (ControlNet Union, denoise 0.3–0.55, el ojo decide), Lescop (Kontext/Flux+CN), Desktop Architect (SDXL+LoRA+CN→Hunyuan3D/TRELLIS.2), eCAADE 2025 (SDXL+LoRA propio+CN fachadas).

### Trellis (loop 3D)

Microsoft Research, MIT. v2 (4B) + Pixl3D nativos en ComfyUI core, PBR completo; piso 24 GB → **va en pod** (3090 $0.22/h), no el miércoles. GLB importa directo a Rhino: cierra el loop 2D→3D→BIM.

### Batería RealVis → subagentes

| # | Prueba | Subagente |
|---|---|---|
| 1 | txt2img × 3 seeds (línea base) | S1 |
| 2 | Croquis → render img2img 0.4–0.6 | S1/S4 |
| 3 | Inpaint por partes (vano, lamas, zócalo) | S4 |
| 4 | ControlNet SDXL Union canny+depth | S4 |
| 5 | LoRA Arcviz/Massing sobre RealVis | S5 |
| 6 | klein edit multi-ref | S1 |
| 7 | Kontext conserva+cambia | S1 |
| 8 | Trellis → GLB → Rhino (pod) | T4 |

### Miércoles en el estudio (12–16 GB)

Llevar: workflows JSON RealVis img2img+inpaint y SDXL ControlNet Union, volumetría PNG + 1–2 fotos ref, prompts/seeds ganadores, modelos en pendrive. Correr pruebas 1–5 en GPU real (minutos), medir tiempo/VRAM, traer renders + workflow validado. Trellis y klein 9B quedan para el pod.

## 8. Plan de integración punto por punto (matriz miércoles)

Cada fila de §6.4 (emulación) y §4.6 (vía virtual) → MVP dueño + estado:

| Punto | Dueño | Estado / costo |
|---|---|---|
| Seedream geometría → SDXL+Union+CN | MVP_04 (S4) | a probar miércoles (RealVis local) |
| NB interiores → klein 4B + LoRA anteproyecto | MVP_09 workerFLUX + pod T4 | operativo CF / LoRA dic |
| GPT textura → klein edit + banco S3 | MVP_09 (S3) | a construir |
| Ideogram esquemas → SDXL scribble + LoRA trazo | MVP_04 + MVP_09-croquis | a probar |
| Style Memory/Viewpoint → LoRA proyecto + seed | MVP_04 (S5) | dic |
| AutoCAD/DWG vía APS o ezdxf | MVP_01 + MVP_02 | APS free tier / ezdxf $0 |
| Revit vía APS + Revit MCP | MVP_07 ESTRUCTURA §4.3 | MCP tech preview |
| IFC vía IfcOpenShell/IfcMCP | MVP_07 (VPS) | $0, ya instalable |
| Rhino vía Hops/VM | MVP_05 + runner | VM = costo horario |
| Video vía fal (S9) | T5+ | excluido hasta fin de año |
| 3D vía Trellis/Tripo fal | T4 | $0.01–0.05/pieza, sin pod |

MCPs ya conectados (n8n, vault, registry, runner, AutoCAD COM, ComfyUI) + abiertos por conectar (FreeCAD 3.1k⭐, Bonsai, IfcMCP oficial, Revit MCP, DrawMCP).

## 9. Trazabilidad
- MVP_07: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]
- Imagen: [[proyectos/MVP_09-workerFLUX/01-agente-pi-imagenes|agente]] · [[wiki/glosario/software/capacidades-agente-imagenes|capacidades]] · [[wiki/glosario/software/formas-ai|formas-ai]] · [[wiki/glosario/software/modelos-imagen-arquitectura|modelos]]
- Doctrina: [[specs/261112-adr-modelo-antes-que-flujo|ADR]] · [[specs/261112-bateria-worker-consistencia|batería]] · [[specs/261112-plan-pruebas-rumbo-miercoles|miércoles (integrado aquí §7)]]
