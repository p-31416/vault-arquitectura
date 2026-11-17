# Sesión 2026-11-16 — Formas.ai + agente para mañana 16:00

> Retoma generación de imágenes. Demo Formas.ai (SOL, 2026-11-15) → ficha wiki + plan con deadline.

## Hecho

1. Fetch home + pricing Formas.ai (200): orquestador (Gemini, Flux Kontext, Luma, Tripo, ChatGPT, Stability) + workspace propio; Pro $69/3.500 créditos; costo por operación sin publicar.
2. Catálogo Pollinations vivo: `openai/gpt-image-2.6-sunburst/flare` ~$0.039 (el "Unburst" de la demo = Sunburst), `bytedance/seedream-5.0-pro` $0.035, `ideogram-v4-turbo/balanced/quality` $0.03/0.06/0.10 — los tres `paid_only` (gate: Paid Pollen); NanoBanana 2.0/2.1 ya probados.
3. Ficha wiki creada: [[wiki/glosario/software/formas-ai|formas-ai]] (modelos→acceso directo, flujos replicables, veredictos demo, límites, visión Hermes, precios).

## Pendiente (deadline: mañana 16:00, agente funcionando)

- [ ] Telegram user ID de SOL + `s` + publish del agente (`FWGtRuylIqexTigj`)
- [ ] Recarga Paid Pollen $1–2 → kontext + NanoBanana + Seedream + GPT-2.6 + Ideogram operativos
- [ ] Cuota Cloudflare (ver dashboard hora de renovación) → `dormi/estar-fiel`
- [ ] Hoja única Emilia: refrescar [[specs/261112-plan-pruebas-rumbo-miercoles|plan]] con Formas + veredicto nube-vs-Comfy + estado agente
- [ ] Pruebas: site extraction CABA, textura automática (agente trae 3 opciones), máscaras con Kontext, Seedream-geometría vs NB-interiores
- [ ] Plan completo escrito: [[specs/261116-plan-agentes-hermes|plan agentes + Hermes]] (arquitectura 1→N, 7 subagentes S1–S7, conexión T1, fases hasta T6)
- [x] Vía 100% virtual CAD/BIM (§4.6 del plan): APS Automation AutoCAD/Revit verificado en docs oficiales + Revit MCP oficial (DevCon 2026) + Rhino.Compute en VM cloud; precio APS con 403 para bots (no enlazado, cifras citadas de página oficial)
- [x] Análisis modelos imagen con precios OpenRouter: Seedream $0.045, NB2.1 ~$0.039, GPT sunburst $8/$30 por Mtok, Ideogram turbo $0.03; Images API = vía única (14 refs + seed + cost por llamada); orden: Seedream → NB2.1 → GPT → Ideogram
- [x] Router classifier + ficha viva (capacidades): tabla pedido→modelo con costos, APIs `/images/models`, `/endpoints`, `/auth/key` verificadas; cron semanal + review loop propuestos; detectado `seedream-5-5` nuevo a evaluar
- [x] §6 plan: croquis→plano en escala (S8: VLM + ControlNet + canvas fijo + calibración ezdxf/APS + verificación MVP_01/02), LoRAs por etapa (croquis/anteproyecto/proyecto en klein 4B + SDXL), tabla emulación open-weights, conexión con los 12 MVP + casos
- [x] Ficha modelos: matriz flujos nativos por modelo (10 modelos × 11 capacidades, fuentes BFL + OpenRouter verificadas), ranking base abierta (FLUX 3 Klein → klein 4B → Qwen-2.1 → Z-Turbo, XL relegado), decisiones actualizadas
- [x] Plan miércoles 261112 integrado al plan Hermes 261116 (§7 carril miércoles: base RealVis, camino, Trellis, batería 1–8 → subagentes, qué llevar/correr, referentes); 261112 queda como antecedente con puntero
- [x] Deconstrucción clase Formas: [[wiki/glosario/software/formas-ai-flujos-clase|flujos-clase]] (12 flujos edge/textura/paramétrico/detail/collage/canvas/style/quadraditos/Astra/floorplan/Cartesian + video S9 con precios fal + 12 creadores + bibliografía oficial; Astra = GPT-6 agentes CAD vía MCP, AEC Mag verificado)
- [x] Padres actualizados: VISION (4 decisiones 16/11) + ESTRUCTURA §3.3/§4 (licencias + base abierta) + REQUISITOS (RF-21–24, RNF-16, video fuera) + ficha viva [[wiki/glosario/software/software-libre-vs-pago|software-libre-vs-pago]]
- [x] Plan Hermes: §5.1 escala gráfica (barra + testigo + canvas fijo), §5.2 matriz pruebas miércoles, §5.3 3D pod-vs-fal, §9 integración punto→MVP; LoRAs = entrega diciembre
- [x] Plan pruebas al límite: [[specs/261116-plan-pruebas-modelos-max|modelos-max]] (fichas GPT2.6/NB2.1/NB2.0/Seedream/Ideogram + benchmarks + batería T1–T9 + qué test exprime cada uno, miniaturas ⏳ sin generar)
- [x] Regla 16/11: Pollinations SOLO gratis (límite diario a medir) · pago SOLO OpenRouter — aplicada en HTML (veredicto + P★ + FREE), plan §3/§5, router; Kontext/Ideogram/1.1-pro sin vía OR → en espera
- [x] Reorden: Seedream pago ÚLTIMO · NB todo en web/Flow (igual croquis+texto que app; API suma seed/refs/costo/batch) · Sunburst fuera de T1 (solo específico) + GPT-image-1-mini barato (~$0.01) · klein=FLUX.2 CF · schnell=FLUX.1 CF+Pol · T1 a aprobar (6 modelos, ~$0.20)
- [x] T1 ejecutado P1+P3 (CF, cuota renovada): P1A manzana + P1B campo schnell (172.8 N c/u) + P3A klein edit frontal simétrico; P2 bloqueado (grants 0.0007<0.002); hallazgo klein-CF sin txt2img; registrado en dashboard
- [x] T9 croquis-fin0006 (centro cultural) con klein CF gratis: hormigón + hierro negro + deck + parasoles perforados + motion blur ✅ — registrado en dashboard
- [x] T9b/T9c correcciones: T9b SIN CAMBIO (klein ignoró 2 variables juntas — verificado visualmente, error mío darlo por bueno); T9c solo quitar columna (guidance 8, 1 variable) ✅ — regla: 1 variable por pasada
- [x] T9d medido objetivamente: dif 13.6/255 = ruido, el edit no aterriza; klein-4b CF devuelve variantes, no ejecuta cambios semánticos finos — marcado ⚠️ en dashboard; opciones: NB web manual, Seedream/GPT pago con OK, Kontext (grants insuficientes)
- [x] T9e desde cero (croquis + prompt completo corregido): dif 61/255, piel perforada protagonista ✅ — regla: corrección grande = regenerar, no editar
- [x] Loop Drive para tablet (S7b en plan): 01-generada + prompt.md → mail con link → markup en tablet → 02-marcada → Drive Trigger → 03-regenerada; convención de nombres = contrato; MCP oficial en preview, usar nodos n8n
- [x] Entrega triple (Telegram + Drive + mail) + matriz HTML Apple-style [[diagramas/matriz-modelos-proveedores|matriz-modelos-proveedores.html]]: inputs aceptados + precios + cableado n8n por modelo y proveedor
- [ ] REGLA (pedido SOL): el HTML no se ve en Obsidian — cada entrega HTML avisa cómo abrirla (doble click → navegador); por defecto preferir formatos nativos Obsidian (md, excalidraw, mermaid, svg embebido)
