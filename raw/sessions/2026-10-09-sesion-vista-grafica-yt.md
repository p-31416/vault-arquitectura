# 2026-10-09 — Vista gráfica YT: brainstorm, spec simplificado, mock 3D + VR editable

tags: [sesion, vista-grafica, youtube, fuentes, grafo-3d, vr, brainstormy, noda]

## Qué se hizo
- Sesión @brainstormy sobre `specs/261009-spec-vista-grafica-yt.md`: 16 ideas + 3 wildcards, Top 3 JTBD y revisión punto a punto (terminal del usuario con lectura acotada, 1 pregunta por vez).
- Decisiones de Sol: frontmatter extendido (fecha_video + fecha_ingesta, url verificada 200 OK), naming `video_id.md` + alias, malla completa de links, 3 MOCs (luego simplificado), colores por tag.
- Spec simplificado a pedido: solo vista gráfica de `wiki/fuentes/00-index-yt.md` (piloto comfyui 71 videos, 3 vistas en tabla → nodos video/tag/creador). Sin MOCs, sin Next, sin Fase 2.
- Aclaración de fuentes: notas derivadas solo con metadatos (`videos-y-canales-guardados.md` + `index-state.json` + `cache-titulos.json`); @contenidos cura en `raw/contenidos/` y `wiki/fuentes/` (ej. `comfyui-for-architects-architutors.md`), la vista solo linkea.
- Mock `scripts/grafo-yt-mock.html` iterado: 2D → 3D con peso por links → panel lateral de #hashtags filtrable → links blancos gruesos con partículas → etiquetas 3D siempre visibles + links con label origen→destino.
- Versión VR `scripts/grafo-yt-vr.html` (A-Frame + 3d-force-graph-vr, MIT): Enter VR en Quest, luego editable desde Quest (modos navegar/agregar/linkear, renombre, export JSON, localStorage).
- Investigación Noda: importa CSV solo en versión paga (`noda.io/documentation/csv.html`, vía Drive o USB-C). Sol pidió vía gratuita open source → queda no prioritaria.
- Verificación app Steam Mind Map VR: VR Only + Windows + SteamVR, solo voz, 9 reviews, 2018, cerrada — descartada.
- Seguridad red: servidor local expone `scripts/` a la LAN; en casa con antena propia avanza tranquilo; levantar solo durante la prueba.
- Servidor local NO levantado (Sol: "despues seguimos, TERMINAMOS").

## Archivos modificados
- `specs/261009-spec-vista-grafica-yt.md` (simplificado + §5 pendiente VR/Noda + cómo abrir en Quest + edición Quest)
- `scripts/grafo-yt-mock.html` (nuevo: mock 3D + hashtags + etiquetas + links visibles)
- `scripts/grafo-yt-vr.html` (nuevo: VR WebXR + edición con controles Quest)

## Pendiente siguiente ciclo
- Probar `grafo-yt-vr.html` en Quest (servidor + Enter VR + modos edición).
- Generar JSON único de 71 + 5 nodos investigar (o `yt_build_notes.py` + `noda-yt.csv` si se retoma Noda).
- Decidir plugin Obsidian 3D Graph para el día a día en PC.

## Cerebro-digital
- Topics: vista-grafica-yt, notas-atomicas-video-tag-creador, frontmatter-extendido, mock-3d-peso, hashtags-filtro, vr-editable-quest, noda-csv-pago, steam-mindmap-descartada.
- Entidades: spec 261009-vista-grafica, index-yt 71 comfyui, video RAMs89SS6cM (única ✅ curada), videos puente WFHlgwl6jno / JWln_5jm4Ic, scripts grafo-yt-mock.html / grafo-yt-vr.html.
- Hechos: spec simplificado a solo vista gráfica el 2026-10-09; VR editable implementado sin probar en headset; servidor local pendiente de levantar; red casera propia.
