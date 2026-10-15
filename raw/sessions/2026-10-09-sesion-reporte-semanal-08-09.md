---
tipo: log
fecha: 2026-10-09
sesion: reporte-semanal-08-09
tags: [sesion, reporte-semanal, comfyui, youtube, n8n, leantime, handy, grafo-vr]
estado: completada
---

# Reporte semanal 08 + 09 Oct 2026 — trabajo vault-arquitectura

> Más nuevo → más arriba. Fuente: 8 archivos en `raw/sessions/` (5 del 08/10 + 3 del 09/10).

## Resumen ejecutivo

| Frente                     | Valor creado                                                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ComfyUI + WF-01            | Research 949 líneas verificado + plan 24h didáctico + launcher background reparado + 5 corridas F-01→F-05 con mejor resultado F-05 + IP-Adapter instalado                                  |
| Curación YouTube → Fuentes | Sistema Takeout→doc único operativo (709 videos, 157 canales) + 132 veredictos video + 47 veredictos canal + índice piloto ComfyUI 71 videos + video 1 fichado completo en `wiki/fuentes/` |
| Voz + agenda + equipo      | Handy local en español operativo + loop Fathom→Drive→vault operativo + Agenda Telegram→Cal.com con reserva real verificada + proyecto `O.S_ARQ-Emi` creado y usuaria Emilia invitada       |
| Grafo + VR                 | Modelo de agentes v3 fijado + specs ingesta/vista + diagrama agentes-fuentes v4 + mock 3D + VR editable para Quest                                                                         |

## Ayer 08/10 — 5 sesiones

### 1. ComfyUI plan + fix .bat
- Research @sherlock: `raw/research/2026-10-08-comfyui-workflows-arq.md` (949 líneas, 35+ fuentes, 38 URLs verificadas 200). Top: FLUX.2 klein 4B como default iteración, workaround Rhino→passes + ControlNet Depth 0.85 + Lineart 0.7 + denoise 0.45-0.55 ante MCP Rhino→ComfyUI aún en oportunidad, video LTX-2.3 en RunPod con fallback Wan local.
- Plan 24h: `proyectos/MVP_04-comfyui-arquitectura/PLANS/2026-10-08-plan-tests-24h.md` (37 KB, 15 secciones, 8 bloques, reusa WFs MVP_04).
- Decisión alcance: planos con reglas avanzan con croquis real + ControlNet directo; volumetría rough como vía alterna.
- Fix background: causa raíz = intérprete sistema Python312. Reescrito a `comfyenv\python.exe main.py` detached, chequeo puerto, espera 60s. SOL confirma: ya funciona.
- Estado: pausada, ComfyUI en 8188.

### 2. Curación YouTube (sesión más larga)
- Sistema: Takeout → `scripts/yt_takeout_parser.py` → `raw/yt/videos-y-canales-guardados.md` (1692 líneas, 197 KB) + `00-index` + template briefing + cache API 646 entradas + `yt_titles.py` + 2 fichas wiki metodología/API-key.
- Base: 157 canales (44 en scope inicial), 709 videos (259 Watch Later + 450 en 15 carpetas), 434 marcadores Chrome en 36 carpetas.
- 6 bugs resueltos con lección: encoding Takeout por glob, headers CSV por índice, sufijo vídeos por `_norm()`, pipes escapados `\|` (296 filas), tags por regex con límites de palabra, contexto carpeta como tag.
- Ampliación: 8 tags nuevos + stemming plurales + filtro fechas + 7 categorías amplias + columna Cat. Efecto: vibe-coding 9→39, agents 25→41, llm 67→86.
- Veredictos SOL Parte 1 (131 ítems 1→131 + MAGNIFIC WL#135 = 132 en `veredictos.json`) + Parte 2 canales 47 rescatados (`canales-veredictos.json`, scope 44→91) + 5 blindados Parte B (total 135). `revision-manual.md` creado para revisión enfocada y luego borrado tras revisión total, fuente de verdad en JSON.
- Efecto final: `sin-clasificar` 157→51, fuera del top-20. Top: llm 207, arq 119, n8n 90, comfyui 80. Categorías: ia-agentes-code 400, diseno-arq 208.
- Infra: `yt_revision.py` (reusa TAGS por import, 2 modos revisión), `yt_creadores.py` → `creadores.md` (151 canales WL, 101 solo-WL), `yt_build_index.py` → `wiki/fuentes/index-yt.md` piloto comfyui 71 videos + primer @contenidos video architutors RAMs89SS6cM (11.6 KB, fila ✅).

### 3. Handy dictado — completada
- Handy v0.9.8 x64 (19.6 MB) instalado en `P:\00-repos\Handy` (P: raíz deniega escritura).
- Modelo SOL: Parakeet V3 español `parakeet-tdt-0.6b-v3` Q8_0 (705 MB, Vulkan RX 570). Cache HF mudado a P: (1.41 GB) + Junction `C:...\.cache\huggingface` → P:.
- Guía tap: foco → Ctrl+Espacio → hablar → Ctrl+Espacio → pega. Nota terminal: paste `Shift+Insert`. SOL confirma: excelente ya funciona.

### 4. n8n Fathom + Agenda
- Loop Fathom→Drive→vault operativo: 5 workflows OS-Emilia → canvas único (Cron+Format absorbidos), Router intacto. Credenciales Drive/Docs/Sheets reconectadas por SOL. Fixes: `jsonBody` serializado, wiring Restore→Move→Apply, `folderId`, nombres `fecha_participantes_recid`, pairing `$('Classify Meeting').item`, `created_after -26h` deja lote limpio, timezone America/Argentina/Buenos_Aires.
- Clasificación por lados (invitados + hablantes + recorded_by): 2 del 03/10 a Clientes, 6 a Internas.
- Import vault: `scripts/import_drive_reuniones.py` idempotente → 8 reuniones en `raw/reuniones/`.
- Agenda reescrita con reserva real: parseo `/agendar DD/MM[/AA] HH:MM Nombre [emails]` + lookup `clientes-contactos` + evento 7109200 30 min. Producción: `/agendar 09/10 15:00 Sol` → reserva `gnCrXcR1j3mz8Hd9THXhyh` accepted + Telegram OK. IFs migrados a Switch v3.4.
- Docs: `arquitectura-n8n-os-emilia.md` v1.2 + `playbook-os-emilia-n8n.md` v1.0 para presentar 09/10.

### 5. WF-01 corridas + IP-Adapter — pausada
- Estructura `MVP_04.02-comfyui-arquitectura/` + `WF-01-planta-ilustrada.md` 7 secciones + JSON base Canny. Input SOL: `P01-AIZPURUA.JPG` 311×494 + 3 refs (MON, terracota, @bit_arq target).
- F-01 ES 193s baseline → F-02 EN 102s (EN rinde mejor SD1.5) → F-03 EN + 512×832 + Canny 0.25/0.55 (mejora clara) → F-04 img2img denoise 0.35 2/5 con deriva (lección: 2ª pasada siempre CON Canny) → F-05 img2img F-03 + Canny 0.9 denoise 0.25 141s (mejor del día).
- Fase A dual Canny+Depth en pausa (falta `controlnet_aux`, Manager caído) → pivote a pulido img2img.
- IP-Adapter completo: repo clonado + accelerate + `ip-adapter-plus_sd15` 93.6 MB (83 tensores) + CLIP ViT-H fp32 2.4 GB → fp16 1.2 GB (521 tensores) + reinicio manual + 35 nodos OK. OOM recuperado con `clear_vram` (regla: de a una cosa por vez).

## Hoy 09/10 — 3 sesiones

### 6. Alta Emilia Leantime
- MCP responde `initialize` 200 pero catálogo vacío → alta por MCP queda para siguiente ciclo (revisar plugin MCP Server).
- Alta API JSON-RPC: proyecto `O.S_ARQ-Emi` id 4 creado (cliente Pitautech id 1, reintento ASCII tras Parse error por em-dash).
- Usuaria Emilia id 5 status `i` invitada pendiente de aceptar. Totales: 3 usuarios, 3 proyectos. `.env` íntegro.
- Flujo contraseña con docs oficiales (invite email + link, fallback copiar link desde User Management).

### 7. Fuentes, agentes y grafo (piloto video 1 completo)
- Video 1 `RAMs89SS6cM`: `transcribir_youtube.py` + notas → transcript subtítulos manuales EN → envoltorio Obsidian → prefijo fecha ISO → @contenidos ficha spec §13 → OK → movido a `wiki/fuentes/comfyui-for_architects-architutors.md`, borrado raw, hub ✅. Protocolo mover-borrar estrenado.
- Modelo agentes v3 en 3 `.opencode/agents/*.md` + spec ingesta v5 §12: Sherlock exterior, Contenidos único acceso `wiki/fuentes`, Vaultworm semanal, Vistas.
- Specs: `261009-spec-ingesta-fuentes.md` v1→v5 + `261009-spec-vista-grafica-yt.md`.
- Convenciones: `wiki/fuentes/{tema_ppal}-{tema_secundario}-{canal}`, tags con guion, hub `00-index-yt.md`.
- Gráfico Emilia: `diagramas/agentes-fuentes.{png,excalidraw.md,mmd}` v4 verificado PNG.
- Instalado: yt-dlp 2026.08.19 + faster-whisper 1.2.1 en comfyenv.

### 8. Vista gráfica YT + VR
- Brainstormy 16 ideas + 3 wildcards, Top 3 JTBD. Decisiones SOL: frontmatter extendido (fecha_video + fecha_ingesta, URL 200), naming `video_id.md` + alias, malla completa links, colores por tag.
- Spec simplificado a solo vista gráfica `00-index-yt.md` (71 videos → nodos video/tag/creador).
- `scripts/grafo-yt-mock.html` (3D + peso + panel #hashtags + etiquetas visibles + partículas) + `scripts/grafo-yt-vr.html` (A-Frame WebXR, Enter VR Quest, modos navegar/agregar/linkear, export JSON, localStorage).
- Noda CSV solo versión paga → avanza por vía abierta. Steam Mind Map VR descartada (VR Only, 2018, 9 reviews, solo voz).
- Servidor local pendiente de levantar (SOL: después seguimos).

## Planes activos

- ComfyUI 24h: Paso 3 dropdown CheckpointLoader → foto croquis → ControlNet Canny 0.85 ArchitectureRealmix (4 corridas letra F). Deadline SOL 09/10 15:00.
- WF-01 Fase B: F-06 IP-Adapter ref-3 weight 0.6-0.8 + Canny → WF-02 inpainting ventanas (ref `px8POauudLY`, probar SD1.5 primero) → WF-03 upscale liviano.
- YT Nivel 2 GO/NO-GO: `yt_rss_check.py` + `yt_briefing_gen.py` + n8n CRON lunes 8:00 + Telegram.
- Reunión Emilia: llevar playbook n8n + PNG agentes-fuentes + specs + convenciones. Crear evento 60 min + Meet en Cal.com.
- Pilotos: revista (Tesseract + PyMuPDF), 3 links IG, Video 2 lote ComfyUI de a 1, `s` #3 vaultworm + primera página-galería local.

## Pendientes consolidados

### Lado SOL
- Ver dropdown `http://127.0.0.1:8188` y reportar modelos visibles
- Pasar `WF01-planta_00001..00005_.png` output → `salidas/n_01-F-0X` + decisión §6 Evaluación
- Copiar 3 refs a `ComfyUI\input\` para F-06
- Cancelar reserva prueba en `cal.com/bookings`
- Limpiar duplicados Drive + crear evento 60 min con Meet y pasar eventTypeId
- Probar dictado diario ES; en terminal, paste `Shift+Insert`
- Probar `grafo-yt-vr.html` en Quest

### Siguiente ciclo
- Triage + `catalogo-watch-later.md` 259 + veredicto 66 canales fuera + homepage `wiki/estudio/noticias/`
- Limpieza `raw/yt/_preview-2026-10-08/` (3 previews superseded)
- Curaduría @contenidos research ComfyUI (en espera, SOL lee primero)
- JSON único 71+5 / `yt_build_notes.py` + decidir plugin Obsidian 3D Graph
- Optimizar HF 1.41→0.7 GB con `mklink` elevado
- Leantime: rotar token expuesto en `create-user-emilia.ps1:4`, revisar plugin MCP 0 tools, asignar Emilia a `O.S_ARQ-Emi` tras aceptar invite

## Análisis cerebro-digital

**Topics:** comfyui-plan-24h, wf01-canny-ipadapter, curacion-yt-takeout, veredictos-hitl, handy-parakeet-es, fathom-drive-vault-loop, agenda-calcom-real, leantime-jsonrpc, ingesta-fuentes-v3, vista-grafica-vr-quest.
**Entidades:** MVP_04 / MVP_04.02, ArchitectureRealmix v1.1, IPAdapter_plus 35 nodos, CLIP ViT-H fp16, P01-AIZPURUA, OS-Emilia n8n, Cal.com 7109200, O.S_ARQ-Emi id 4, Emilia id 5, architutors RAMs89SS6cM, Handy Parakeet V3, Quest VR.
**Hechos:** launcher background reparado y verificado; EN supera ES en SD1.5; aspecto real como fix de mayor impacto; 2ª pasada siempre con Canny; Manager caído → installs manuales; MCP Leantime con catálogo vacío al 09/10; protocolo mover-borrar verificado; spec gráfica simplificada a solo vista.
