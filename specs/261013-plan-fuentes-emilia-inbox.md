# Spec — Inbox de fuentes Emilia: cola, clasificador y rutina diaria

_Fecha: 2026-10-13 · Estado: aprobado por SOL · Origen: sesión plan 2026-10-13 (7 pantallas, terminal sin scroll) · Relacionado: `specs/261009-spec-ingesta-fuentes.md` (ecuación única de ingesta), `proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n.md`, `proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md`_

## 1. Objetivo

Darle a Emilia (móvil, ChatGPT Plus, sin conocimientos técnicos, sin Obsidian ni git) una vía de aporte con fricción cero —links, ideas, shares, libros— que alimente el pipeline existente `sherlock → contenidos → vaultworm-arq` sin que ella escriba jamás directo en el vault. Todo lo crítico vive del lado SOL; su Plus es mejora opcional, nunca requisito.

## 2. Principios (no se reabren)

1. **Emilia nunca escribe en el vault.** Lee (digest Telegram + Drive) y valida (✅/✏️/❌). Riesgo de sobreescritura: cero por construcción.
2. **Independencia de su suscripción.** Si deja Plus, pierde solo sus atajos; la cola, la rutina y el vault siguen iguales.
3. **Un pipeline, N extractores** (`specs/261009-spec-ingesta-fuentes.md:11`): la novedad aquí es solo la *cola de entrada*; el procesamiento no cambia.
4. **Vocabulario controlado común**: la columna Tema usa la misma lista de tags de Sol y Emilia o el merge no sirve.
5. **Append-only + binarios por referencia**: el crudo no se edita; binarios en `activos/` o Drive, nunca en git.
6. **Sin `s` no hay `write` en `wiki/`** (HITL vigente `AGENTS.md`).

## 3. Sheet "Fuentes-Inbox" (la cola visible)

Vive en Drive `OS-Emilia/` → `Fuentes-Inbox` (Google Sheets). Emilia la abre del celu; SOL la ve vía Drive Stream. Espejo de lectura + semáforo; el estado canónico vive en los índices del vault (`raw/research/00-index.md`, `raw/yt/index-state.json`). Sync vault→Sheet, nunca al revés.

| Col | Campo | Quién | Contenido |
|---|---|---|---|
| A | Fecha ingesta | auto (rutina) | YYYY-MM-DD HH:mm AR (entra de la conversación) |
| B | De | auto | Emilia / Sol |
| C | Link | Emilia o Sol | URL pegada |
| D | Tipo | auto (clasificador §4) | YT / IG / WEB / PDF / SHARE / IDEA |
| E | Tema | ✏️ Emilia | 1 línea, vocabulario controlado |
| F | Prioridad | ✏️ Emilia | alta / media / baja |
| G | Estado | máquina | `pendiente` → `en-sherlock` → `en-reporte` → `en-wiki` / `descartado` |
| H | Destino vault | SOL | ruta vault (`wiki/fuentes/…`, `raw/research/…`) |
| I | Nota SOL | SOL | comentario libre |

Regla de oro: Emilia edita SOLO columnas E y F. Todo lo demás lo mueve la automatización o SOL.

## 4. Clasificador por dominio (determinista, sin IA)

Vive en el Router Telegram (extensión) o script chico. Regex sobre la URL, primer match gana:

| Patrón | Tipo | Ruta extractora |
|---|---|---|
| `youtube.com` `youtu.be` `shorts/` | YT | `scripts/transcribir_youtube.py` → `raw/yt/transcripts/` |
| `instagram.com` | IG | links curados → webfetch → ficha (spec ingesta §3.3 opción 1, caption = epígrafe) → `raw/research/` + stub |
| `chatgpt.com/share` | SHARE | `chatgpt_share_fetch` (verificado 2026-10-13 con share "Evaluación gráfica") → `raw/entradas-emilia/` |
| `*.pdf` | LIBRO | pipeline PDF (caso Baudrillard 2026-10-13) / OCR Tesseract pendiente → `raw/pdf/` + Drive |
| otro `http` | WEB | webfetch + verificación 200 → `raw/research/` |
| sin URL / inclasificable | IDEA | stub directo `raw/entradas-emilia/` o lo decide @sherlock |

Cada tipo conserva su camino delineado en el spec de ingesta (revistas §3.1, YT §3.2, IG §3.3, resto §3.4); el clasificador solo elige carril.

## 5. Rutina diaria 07:00 (nube, corre con la PC apagada)

Cron n8n (hermano del Fathom Cron 07:00 AR ya operativo):

1. Lee links nuevos del grupo + Sheet (`estado = pendiente`).
2. YT → transcript · WEB → texto webfetch · IG/SHARE → stub `pendiente-formato` · PDF → cola OCR.
3. Actualiza columna G del Sheet.
4. Emite digest a Telegram (~07:30) en lenguaje cotidiano:

> 3 fuentes nuevas: 1. IG Chipperfield (foto) 2. YT MoureDev (transcript ok) 3. share ChatGPT (idea). Respondé 1/2/3 para priorizar.

La respuesta de Emilia escribe columna F. Lo priorizado pasa a @sherlock → reporte @contenidos → gate `¿Avanzo? s/N` de SOL → wiki → `log.md`.

## 6. Puentes GPT↔vault de Emilia (verificados, opcionales)

1. **App Google Drive en ChatGPT (oficial, verificado 200).** Ajustes → Apps → Google Drive → conectar su cuenta: su GPT lee el Sheet y el digest en vivo. Límite documentado: cuentas personales tienen *live access only*, sin índice sincronizado (suficiente para este uso). Ref: `https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt` (verificado 2026-10-13).
2. **GPT Action → webhook n8n (Mes 2).** Su GPT "Studio OS" con 2 endpoints propios (`guardar-link`, `ver-estado`): ella dice "guardá este link" y entra a la cola hablando. Nota de futuro: OpenAI migra GPTs personalizados hacia Plugins (`help.openai.com` Configuring actions in GPTs); diseñar la Action mínima y portable, nunca como dependencia.
3. **Proyecto "Studio OS" en su ChatGPT.** Instrucciones permanentes + rúbrica de 6 atributos (jerarquía de líneas, pochés, tramas, cotas, profundidad gráfica, composición — su share del 2026-10-13) + digest archivado. Su rutina diaria conversa sobre el digest con criterio estable.

Ninguna vía escribe al vault: todas desembocan en la cola (§3) y pasan por curaduría SOL.

## 7. Implementación por cortes

- **Corte 1 (inaugural):** Sheet + clasificador (links web/IG + shares, ambos carriles) + rutina digest solo-lectura. Fetch de shares semi-manual (SOL corre el script con su link) hasta validar ritmo.
- **Corte 2:** `chatgpt_share_fetch.py` + notas didácticas (patrón `scripts/*_notas.md`), rama inbox en Router Telegram, `raw/entradas-emilia/` + regla AGENTS.md.
- **Corte 3:** digest con botones ✅/✏️/❌, sync vault→Sheet, Proyecto Studio OS en su ChatGPT + app Drive.
- **Mes 2:** export periódico ChatGPT→Drive, GPT Action → n8n, obsolescencia del fetch manual.

## 8. Criterio de done del corte 1

Un link de cada carril (web/IG + share) entra por Telegram, aparece en el Sheet con tipo auto, Emilia prioriza respondiendo el digest, y lo priorizado llega a `raw/` con stub trazable — sin que ella abra nada fuera del celu.

## 9. Rama inbox en Router (implementado 2026-10-13, sin IA)

Mismo bot `emiliaospi_bot`, grupo nuevo "Fuentes". Sin nodos de IA: dos Switch v3.4 deterministas + Sheets append + ack.

- `Route Fuentes Group`: regla `String(chat.id) == FUENTES_CHAT_ID` → rama inbox; fallback extra → `Route Telegram Command` intacto (Agenda nunca ve los links).
- `Has Link`: `text contains "http"` → `Append Fuentes Sheet`; fallback extra → `Reply Solo Links` ("Acá solo guardo links 🔗").
- `Append Fuentes Sheet2` (nodo Sheets `append` con `defineBelow` creado vía ops —el vía SDK caía a `autoMap`—): columnas A→I con refs simples a `Prepara Fila`. Verificado 2026-10-14 con fila real `["2026-10-14 8:41","Cliente","https://youtu.be/…","YT","","","pendiente"]`. `Prepara Fila` (Set): fecha AR, de, link por `entities[0]` slice, tipo YT/IG/SHARE/LIBRO/WEB por `indexOf` + ternarios (el parser n8n rechaza `function/for/var`).
- `Ack Fuente Guardada`: "Guardado ✓ en la cola de fuentes. Estado: pendiente."

Pendientes de cableado (test card): ~~crear Sheet con fila de encabezado A1:I1~~ HECHO 2026-10-14 (ID `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI`, `https://docs.google.com/spreadsheets/d/18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI/edit`, cableado en `Append Fuentes Sheet`; falta mover a carpeta Drive `OS-Emilia/` + compartir con Emilia) · crear grupo "Fuentes" + agregar bot y Emilia · mandar un link y leer `chat_id` de la ejecución · pegar `FUENTES_CHAT_ID` real (actual: `0`, rama inalcanzable).
