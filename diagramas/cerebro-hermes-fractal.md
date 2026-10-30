---
tipo: indice
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [diagrama, filosofia, hermes, wiki, fractal, rizoma]
---

# Cerebro fractal y rizomático — cómo las fuentes alimentan a Hermes

Filosofía en palabras: [[specs/261029-filosofia-hermes|filosofía de Hermes]]. Flujos con scripts reales: [[diagramas/flujo-fuentes-wiki-hermes|flujo fuentes → wiki → Hermes]].

![[diagramas/cerebro-hermes-fractal.drawio.svg|900]]

Editable: [[diagramas/cerebro-hermes-fractal.drawio|drawio]] · texto: [[diagramas/cerebro-hermes-fractal.mmd|mmd]].

## Versión 3D

`diagramas/cerebro-hermes-fractal-3d.html` — mismo grafo en 3D (patrón `scripts/grafo-yt-mock.html`): abrir en el navegador con doble click (pide internet por el CDN). Verde al centro = cerebro; links blancos = alimentan; rosa = rizoma; violeta = anillo Hermes. Panel lateral para aislar cada rama; click en esfera muestra su ruta del vault.

## Cómo se lee (de arriba hacia abajo)

**1. Todo sale de un nodo: FUENTES.** Sin intermedios, FUENTES se abre en tipos (📽 video, 📷 imagen, ⌨️ texto, reunión + propuestas ⭐). De cada tipo salen los subtipos (YouTube/MKV/portales; JPG/PNG/captura/IG; revista/libro/paper/tesis; Fathom/Meet). De cada subtipo sale su procesamiento (⚙ script → transcript/ficha/minuta). Esa repetición idéntica a menor escala es lo fractal.

**Fuentes propuestas (⭐, no manejadas aún):** 🎙 audio (podcasts, notas de voz → faster-whisper), ✏️ croquis (cuaderno escaneado → `curar-cuaderno`, VISION §3), 📐 CAD (DWG base → `audita-dwg.py`). Candidatas a futuro: modelos 3D/BIM, correo, TikTok/X, normativa CPAU.

**2. Las líneas punteadas son el rizoma.** Un transcript cita un paper, una ficha visual dialoga con la ficha de video, una foto de obra resuelve un compromiso de minuta. Conexiones cruzadas entre ramas, sin jerarquía: se entra por cualquier punto y se llega al mismo cerebro.

**3. El centro es el cerebro.** La wiki común con Front Matter ubicable. Nada entra sin `s`; nada sale sin registro.

**4. Hermes la usa en tres tiempos.** Lee por `vault-mcp` (leer, buscar, índice). Su memoria real es el cuaderno digital —lo que queda—; su memoria de sesión es scratch —lo que se borra—. Mueve sus brazos por MCP (AutoCAD, Rhino, ComfyUI, n8n, Vault, Registro). Mantiene con `curar-cuaderno`, digest 07:00 y lint. Mejora proponiendo entradas y refunds, siempre con `s`.

**5. El harness sostiene todo.** Docker, cron, Telegram y Postgres abajo; skills escritas arriba; LLM intercambiable en el medio. Por eso no se abandona (Karpathy): lo que se mantiene es el andamiaje, no el modelo.
