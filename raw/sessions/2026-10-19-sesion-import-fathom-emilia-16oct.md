---
tipo: log
fecha: 2026-10-19
tags: [sesion, fathom, emilia, import-manual, vault]
---

# Sesión 2026-10-19 — import 3 reuniones con Emilia (16/10) desde Fathom Proyecto Pi

## Qué se hizo

- Consulta a la API Fathom (`api.fathom.ai/external/v1/meetings`, key `FATHOM_API_KEY_PROYECTOPI` del `.env`,
  `include_transcript/summary/action_items=true`, `created_after=2026-10-09`) → 8 reuniones nuevas de la cuenta.
- Filtro por hablante: 3 con **Emilia Pimenta Lombardi** (16/10) + 3 con **Delfina Pagnotta** (19/10, sin Emilia → descartadas)
  + 3 del 09/10 ya importadas (omitidas).
- Import con `scripts/import_fathom_ppi_manual.py` (sin cambios de código) sobre el JSON filtrado:
  - `raw/reuniones/2026-10-16_emilia-proyectopi_193621124.md` (529 turnos)
  - `raw/reuniones/2026-10-16_emilia-proyectopi_193639289.md` (592 turnos)
  - `raw/reuniones/2026-10-16_emilia-proyectopi_193660891.md` (720 turnos)
- Copia a `G:\Mi unidad\OS-Emilia\Reuniones-Internas\` + 3 claves nuevas en `raw/reuniones/.import-state.json` (47 en total).
- Verificación: UTF-8 sin caracteres de reemplazo, secciones `## Datos / ## Resumen / ## Action items / ## Transcripcion` completas.

## Contenido de las 3 reuniones

- **18:34 — Obra y flujo CAD (193621124):** cambio tardío del cliente a puertas de madera maciza → rediseño de
  iluminación de techo; baños a 73 cm de paso; sofás 3,35 m sin consultar → suspensión de rieles; falta de manual
  de procesos y uso de CAD sin precisión (27 vs 28 cm) como freno de productividad; flujo con bloques/precisión
  como alternativa pragmática al BIM. Tasks: Emilia (riel de luz,layout con Tatiana, plano de replanteo univ),
  Pi (plano de replanteo + libro de iluminación y sombras).
- **19:31 — Concurso "Gaudí Nexus" (193639289):** mercado + centro cultural cerca de la Sagrada Família con
  ComfyUI/Rhino/SD de punta a punta; IA como amenaza al honorario por m² → tokenización de diseños y cobro por
  propiedad intelectual; protección de IP enviando JPG de baja resolución; jurado con MVRDV; inscripción €175.
  Tesis de neuroarquitectura de Emilia apoyada en IA.
- **20:33 — OS Emilia: agentes + ComfyUI (193660891):** agentes de Telegram que catalogan enlaces a Sheet,
  bot `OS.emi-pi` para agendar (cal.com + Google Calendar), flujo de investigación en 3 etapas (raw → Obsidian → wiki),
  ComfyUI con LoRA propio (estilo Chipperfield dibujado a mano, luz cálida en lugar del naranja saturado) para entregas
  de quinto año en formato libro/collage. Cita: miércoles 13:00, conectar calendario de Emilia.

## Hallazgos de la sesión

- **Dual de cuentas:** las mismas reuniones del 16/10 ya existían en Drive desde el n8n Fathom Core con `recording_id`
  propios (193639372, 193661028), porque Emilia las graba desde su cuenta. El import manual de la cuenta Pi agrega
  los 3 crudos faltantes (el Core no cubrió la de 18:34). No se duplicaron en el vault: las versiones Drive quedan
  en Drive.
- **Action items:** las 3 reuniones del 16/10 vienen con `action_items` vacío en la API (solo la de 09/10 "Emi OS" trae 3);
  los próximos pasos se leen del resumen.
- **Acentos:** la API devuelve el nombre del hablante con acento en algunos casos (`Emília Pimenta` el 09/10);
  el import actual no normaliza el nombre, solo ordena el slug por fecha + `recording_id`.

## Queda

- Google Doc de las 3 (el Core solo genera el de la cuenta de Emilia; carga manual o backfill).
- Actualizar el dashboard de reuniones (23 → 26 en `presentacion/06-dashboard-cierre-mes1.md`).
- Criterio de deduplicación entre las dos cuentas antes de que el cron dual corra en paralelo (mismo `recording_id`
  no es la misma clave entre cuentas: usar fecha + duración + participantes).
