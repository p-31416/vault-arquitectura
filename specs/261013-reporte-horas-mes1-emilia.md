---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
estado: borrador
tags: [reporte-horas, mes1, humano-vs-maquina, studio-os]
idioma: es
---

# Reporte horas Mes 1 (16/09→13/10) — humano vs máquina

> Metodología: **evidencia** (duraciones medidas en transcripts, execs y corridas) + **estimación** (bloques por día, a confirmar por Sol). Humano y máquina corren en paralelo: no se suman linealmente. Ahorro = `T_manual − (T_revisión + T_máquina)`.

## 1. Reuniones Fathom medidas

| Fecha | Reuniones | Duración medida | Estado |
|---|---|---|---|
| 17/09 (I, II, III) | 827314240, 827407566, 827500181 | 596+678+400s = **27.9 min** | Summary Fathom |
| 17/09 (IV) | 827502057 | ~42 min | Último timestamp transcript |
| 24/09 ×2 | 837009769, 837064604 | ~60 + ~59 min | Último timestamp (a confirmar) |
| 26/09 ×3 | 838837607, 838850462, 838864496 | ~60 + ~60 + ~58 min | Ídem |
| 03/10 ×2 | 847923513, 847933022 | ~59 + ~57 min | Ídem (vinícola Leticia+Vanessa) |
| 11/09 ×4 | 820017531, 820123815, 820234213, 820330871 | s/d (sin timestamps) | Estimar con Sol ~30-60 min c/u |

**Subtotal medido reuniones (actualizado 13/10 vía API Fathom + dump `raw/reuniones/2026-10-13-fathom-mes-dump.json` + corrección Sol): ~13.5hs en 13 Fathom** (17/09 59.9+59.9+42+42min API/transcript — los "segs" del summary Fathom no valen + 24/09 119min + 26/09 178min + 03/10 116min + 09/10 180min) **+ 6hs en 2 presenciales (16 y 30/09) = ~19.5hs en reuniones.** 11/09 ×4 s/d. Excluidas: 06/10 Patricia y 07/10 Priscila (no Emilia). La captura Fathom es tiempo máquina en paralelo al humano.

## 2. Sesiones humanas por día (estimación a confirmar)

| Día | Sesiones (archivos) | Trabajo | Est. |
|---|---|---|---|
| 16/09 | playbook portable | Visita 14:30-18:30 + inventario + stack | 4.0h |
| 17/09 | fathom-dual + trabajo | Ingest 3 reuniones + estándares CAD + PC | 3.5h |
| 19/09 | contrato + metodología/moodboard + fathom-dual | PDF 5 págs Chrome + repo curado + quartz | 6.0h |
| 24/09 | cierre contrato + plan n8n (5 continuaciones) + n8n-mcp | Contrato final + 4 workflows + OAuth + Drive + tests Telegram/Cal/Fathom | 8.5h |
| 27/09 | mvp_02 fuentes + autodesk-mcp + fix índices | Perplexity CAD + MCP Help + auditoría REP-ARAOZ | 4.0h |
| 28/09 | alta leantime + wikilinks + revisión 14 specs | Spec 29/09 + scripts + marcado pendientes | 3.0h |
| 30/09 | mcp 7 pasos bloques NL + moodboard v5 | Bloques lenguaje natural + WF_v5 fachada | 3.0h |
| 05/10 | fix mcp + remotion + SET_02 | 7 MCPs + 2 episodios video + DGIUR | 5.0h |
| 08/10 | 5 sesiones (curación YT larga + n8n + comfy + handy + WF-01) | Día completo | 9.0h |
| 09/10 | 7 sesiones (leantime + agentes + reporte + VR) | Día completo | 8.0h |
| 11/09 | 4 reuniones (reporte, sin archivo sesión) | Propuesta + ROI 12h/mes | 2.0h |
| 13/10 | baudrillard PDF + cierre (esta) | Pipeline + spec cierre | 2.0h |

**Subtotal estimado humano: ~58-65hs.** Sol confirma su número y lo sube a Leantime (botón Time Tracking por task).

## 3. Horas máquina medidas (agentes, en paralelo)

* **ComfyUI:** F-01 193s + F-02 102s + F-05 141s + WF-03 (208+190+145s) = **~16 min** render medido (F-03/F-04 s/d). Descargas desatendidas: IP-Adapter 93.6 MB + CLIP 2.4 GB→1.2 GB + Parakeet 705 MB (~30-60 min red, sin humano).
* **n8n:** ~20 execs (fixes 1-12, 3489→3525) × ~30-60s = **~15 min** ejecución.
* **Fathom:** grabación = duración reuniones (~8.4hs, paralela).
* **YouTube API:** 646 títulos cache + 709 videos indexados, `videos.list` = 1 unidad c/u (segundos).
* **Remotion:** 2 episodios (79s + 63s video) — render s/d.
* **Whisper:** sin corrida (video 1 usó subtítulos manuales).

**Máquina atendida total medida: ~1h + descargas desatendidas.** El resto del valor está en sistemas que desde ahora ahorran 12hs/mes.

## 4. Punteo herramientas del mes (O3)

* **Agentes:** Sherlock (exterior: Chipperfield, Ching, Comfy research 949 líneas/38 URLs), Contenidos (ficha video 1 + Baudrillard a `wiki/fuentes`), Vaultworm (spec, semanal), Brainstormy (VR YT), Fathom-PM (minutas→Vault→Leantime).
* **PDFs:** pipeline `raw/pdf/` espejo de `raw/yt/` + `activos/fuentes/` + Baudrillard curado; Autodesk Help MCP + documento maestro con wikilinks.
* **YouTube API:** Takeout→parser (709 videos/157 canales/132 veredictos) + índice piloto 71 + grafo 3D/VR Quest.
* **Voz:** Handy + Parakeet V3 ES operativo (MVP_06).
* **n8n Emilia OS:** Router + Agenda real + Cancel/Modif + Fathom Core canvas único (cron 07:00, filtro 26h, lados emilia/proyectopi/externo).
* **CAD:** MVP_02 SETs + bloques NL (7 pasos) + auditoría REP-ARAOZ vía MCP AutoCAD; bloques replanteo + miniobras + conteo→planilla (en curso).
* **Leantime:** proyecto 4 + Emilia id 5 + M1-M4 (443-446) + tasks 447-456 + GOAL manual (3 goals).
* **Video:** Remotion 2 episodios + excalidraw agentes-fuentes v4.

## 5. Qué falta para cerrar números + rituales reales

* Rituales Mes 1 (real, a diferencia del esquema 8/8): semanales Lun+Mié no cumplidos 2×/semana; **presenciales 2×3hs = 6hs (16/09 primer día + 30/09)**. Anotar en acta S4.
* O2 vs O3: **O2 = lo que costó** (65hs, procesos medidos) / **O3 = lo que queda y ahorra** (herramientas, ≥12hs/mes). Así se presenta.
* [ ] Sol confirma total humano y lo carga en Leantime (tasks 447-456 + nuevas si hace falta).
* [ ] 11/09: duraciones Fathom (abrir links del reporte).
* [ ] Comfy F-03/F-04 + renders Remotion: s/d, no bloquean.
* [ ] Con esto, O2 queda medido y la calculadora tiene base real.
