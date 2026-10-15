---
tipo: plan
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [plan, vault-web, mkdocs, drive-ingest, n8n, r2, studio-os, emilia, handover-mes1]
estado: propuesta-candidata
cliente: Emilia Pimenta (Studio OS)
idioma: es
origen: conversación 2026-10-08 + @brainstormy (handover previo) + PLAN-015 mkdocs + spec 260924 n8n
---

# Plan — Vault como web privada + ingest Drive (no réplica local)

> Plan candidato guardado el **2026-10-08** para lectura detenida de Sol antes de ejecutar Día 1. **No se ejecuta nada hasta `s` explícito.** La decisión de curaduría manual queda registrada (D3 ✅). Quedan 2 decisiones pendientes: D1 (activar n8n hoy) y D2 (mail semanal de curaduría).

---

## 0 · Resumen en un párrafo

Reemplazar la réplica local del vault por un **vault web servido con MkDocs Material en `studio.pitau.tech`** (mismo VPS, sidecar de n8n) + **ingest diaria desde Drive** vía n8n cron 07:00 AR + **dedup perceptual hash + curaduría manual semanal** para las revistas de Emilia. Backend ya existente (n8n VPS, 7/7 MCPs, Fathom Cron armado) cubre 90% de la parte operativa. Plan ejecutado en 8 días hasta la reunión del 16/10.

---

## 1 · Hallazgos que cambian el plan original

| # | Fuente | Estado previo |
|---|---|---|
| 1 | `pitauOS/.../PLAN-015-RND-mkdocs-jr-web-privada.md` | **Plan canónico**, estado `nuevo`, 8h estimadas, stack `mkdocs + mkdocs-material`. Criterios de aceptación ya escritos: WIKI fuente, EL_ALEPH fichas con drive_url, hosting privado. |
| 2 | `specs/260924-plan-os-emilia-n8n.md` | **4 workflows ya en n8n VPS**, Drive IDs confirmados, Fathom Cron 07:00 AR armado, Cal.com event 7109200. Falta §16.4-16.5 (credenciales `* Emilia` + activar). |
| 3 | `specs/260909-moodboard-vault-visual-local.md` | Pipeline SD1.5 + Canny + IPAdapter para revistas, regla "sin ficha no entra". Pendiente validar nodos al arranque. |
| 4 | `specs/260917-backlog-nextcloud-vps-storage.md` | Nextcloud está en Mes 3. R2 (que vos preferís) lo desplaza y reduce costo. |
| 5 | 7/7 MCPs conectados | Leantime remote (05/10), fathom-proyectopi reparado. n8n nativo no choca con nada. |

---

## 2 · Arquitectura cerrada

```
EMILIA/SOL
  ↓ lee                          ↓ aporta
  [WEB READER]                   [DRIVE Inbox]
studio.pitau.tech                G:\Mi unidad\OS-Emilia\Inbox\
MkDocs Material                 ├ /Revistas/  (imágenes croquis)
nginx + CF Access               └ /Libros/    (PDFs/EPUBs)
                            ↓ cron 07:00 AR
                ┌─────────────────────────────────┐
                │ n8n WF-Revistas-Ingest          │
                │ n8n WF-Libros-Ingest            │
                └─────────────┬───────────────────┘
                              ▼
                ┌─────────────────────────────────┐
                │ PIPELINE                        │
                │ 1. sha256 → dedup exacto        │
                │ 2. pHash → dedup perceptual     │
                │ 3. extract: PDF/EPUB/JPG        │
                │ 4. compress + resize            │
                │ 5. R2 binarios + ficha .md      │
                │ 6. webhook mkdocs rebuild       │
                └─────────────┬───────────────────┘
                              ▼
                ┌─────────────────────────────────┐
                │ repo vault-arquitectura         │
                │ + R2 bucket                     │
                │ + studio.pitau.tech rebuild     │
                └─────────────────────────────────┘
```

| Capa | Tech | Ubicación | Costo |
|---|---|---|---|
| Web reader | MkDocs Material | VPS `pitau.tech` sidecar (puerto 8085, nginx) | $0 |
| Auth | Cloudflare Access | mismo dominio | $0 (≤50 users) |
| Storage binarios | Cloudflare R2 | cuenta R2 nueva | $0.015/GB-mes, 10GB gratis |
| Cron | n8n VPS existente | mismo | $0 |
| Dedup | Python `imagehash` (pHash) + `hashlib.sha256` | Function node en n8n | $0 |
| OCR/libros | Tesseract (cuando llegue) | ya instalado | $0 |
| Búsqueda | Pagefind estática | built-in del sitio | $0 |
| Dominio | `studio.pitau.tech` | subdominio paralelo a `n8n.pitau.tech` | $0 |

**Total infraestructura nueva: $0** salvo R2 cuando Emilia pase 10GB. VPS no se toca.

---

## 3 · Revistas: política anti-inundación con curaduría manual

**Decisión D3 ✅ (2026-10-08):** curaduría manual primero.

Flujo:

1. **sha256 binario** → idénticas = descartar (sin revisar)
2. **pHash perceptual 8×8** → si similitud ≤6 bits con una ya guardada, descartar + log
3. **Día 50 tope** → excedente va a `staging/excedente-<YYYY-MM-DD>/` con auto-purge 7 días
4. **Domingo 22:00 AR** un n8n "Resumen semanal" envía mail con: total procesado en la semana, cuántas pasaron filtro, cuántas quedaron en staging, link directo a la carpeta staging para aprobar/descartear en lote
5. **Revisión manual** desde Drive o desde una UI web mínima — el comando Telegram `/vault approve/skip` queda para Mes 2

| Caso | Destino | Razón |
|---|---|---|
| Revista inédita pasa filtros | `activos/revistas/<origen>/<slug>-<YYYY-MM-DD>-NN.jpg` (JPEG q=70, max 1024px) + ficha `.md` 1:1 con frontmatter tipo `referente` | base curada |
| Variante muy similar ya vista | descartar + log en `raw/ingest/discard-<YYYY-MM-DD>.md` | auditoría semanal |
| Excedente del día | `staging/excedente-<YYYY-MM-DD>/` auto-purge 7 días | cola |
| Libro PDF/EPUB | `wiki/raw/<libro>-<slug>-<YYYY-MM-DD>.md` (extracto) + cover thumb en `activos/libros/<slug>-cover.jpg` | bajo vol, alto valor |

---

## 4 · Cambios vs el handover anterior

| Pieza previa (de la propuesta @brainstormy 08/10) | Acción |
|---|---|
| Bloque A.1 — 5 cambios naming/index raíz | **SE MANTIENE** |
| Bloque A.2 — Banner doble capa (frontmatter + footer) | **SE MANTIENE** (la web lo lee automáticamente) |
| Bloque A.3 — 2 Excalidraw nuevos (Mapa Handover, Anatomía Glosario) | **PASA A MES 2** — la web muestra relaciones via wikilinks nativamente |
| Bloque A.4 — Archivar 2 specs obsoletas (`ghingest6etapas` + `telegram-vault`) | **SE EJECUTA** el 13/10 |
| Bloque A.5 — Archivar MVP_01 + MVP_04 | **NO SE EJECUTA** (vos dijiste "los MVPs están bien") |
| Bloque B — 5 specs críticos | **SE REEMPLAZA** (ver §5) |
| Bloque C — Demo reunión | **SE REESCRIBE** (ver §7) |
| C.6 PDF deck | cambia por link a `studio.pitau.tech` + credenciales + one-pager |

---

## 5 · Las 3 piezas críticas reales para 16/10 (reemplazan Bloque B)

1. **n8n §16.4-16.5 ejecutado** — credenciales `* Emilia` reales (Telegram, Cal.com, Fathom, Drive) + Router + Fathom Core + Fathom Cron **activos**
2. **MkDocs en VPS sirviendo la wiki** — `studio.pitau.tech` resuelve con Cloudflare Access, página inicial con nav priorizado (conceptos + proyecto Emilia + specs trimestral), rebuilt en push
3. **WF-Revistas-Ingest funcionando con pHash + 50/día** — Emilia tira archivos a `Inbox/`, al día siguiente están en la web con ficha

---

## 6 · Cronograma 8 días

| Día | Fecha | Sesión | Entregable verificable |
|---|---|---|---|
| **1** | Hoy 08/10 (jue) | Confirmar dirección + activar n8n §16.4-16.5 (credenciales `* Emilia`) + crear Telegram bot + primera prueba Fathom | workflows activos, `/help` responde 200 |
| **2** | 09/10 (vie) | MkDocs install en VPS · `mkdocs.yml` mínimo · tema Material · nav priorizado · nginx + Cloudflare Access `studio.pitau.tech` | URL responde con auth |
| **3** | 10/10 (sáb) | n8n WF-Revistas-Ingest + WF-Libros-Ingest: trigger Watch Drive, pHash, sha256, límite 50/día, R2 upload, ficha `.md`, webhook mkdocs rebuild | WF guardado, validado en seco |
| **4** | 11/10 (dom) | Prueba E2E real: Emilia tira 5 imágenes → run manual WF → confirma pHash + R2 + mkdocs rebuild + fichas | 5 entradas nuevas |
| **5** | 12/10 (lun) | Activar cron 07:00 AR real · envío del mail semanal de curaduría (config; el primer envío será el domingo 12/10 noche) | cron automático corre |
| **6** | 13/10 (mar) | Archivar 2 specs obsoletas → `specs/archived/2026-09-pre-firma/` con nota de baja | `archived/` poblado |
| **7** | 14/10 (mié) | **Rehearsal completo del handover nuevo** (web + cron + perceptual hash funcionando) | ensayo 60 min |
| **8** | 15/10 (jue) | Carta de acceso al vault (`proyectos/STUDIO_OS-Emilia/handover/16-10/acceso-vault.md`) + one-pager Mes 2 PDF + envío a Emilia 24h antes | mail enviado |
| **9** | 16/10 (vie) | **Reunión Mixta 60-75 min** | demo OK |

---

## 7 · Demo del 16/10 (reescrita)

| # | Sección | Duración | Qué se muestra |
|---|---|---|---|
| 0 | Gancho 30" | 5 min | "Emilia, en vez de bajarte el vault a tu compu, lo leés en la web. Y en vez de pegarme transcripciones, vos depositás en Drive y yo proceso una vez al día. Hoy te muestro las dos cosas funcionando." |
| 1 | El Mes 1 en 1 imagen | 5 min | Anillo trimestral Excalidraw + 3 fechas clave (24/09 firma, 05/10 fix MCPs, 16/10 handover) |
| 2 | Demo web en vivo | 12 min | Abrir `studio.pitau.tech` · navegar glosario + proyecto Emilia + spec trimestral · probar búsqueda · mostrar que también funciona en celu |
| 3 | Demo cron Drive | 12 min | Vos mismo/a tirás 3 PDFs en `Inbox/Revistas/` desde el celu · botón "procesar ahora" → WF corre → 30s después, vault rebuildeado + ficha creada |
| 4 | Recap Mes 1 | 8 min | Tabla actualizada: 5 críticos hechos, 7 diferibles a Mes 2, 2 specs archivadas |
| 5 | Mes 2 + cierre | 8 min | ROI payback Excalidraw + 3 palancas del Mes 2 (alcance/velocidad/profundidad) |
| 6 | Q&A | 15 min | — |

---

## 8 · Decisiones registradas

**Tomadas:**

- **D3** ✅ — Política revistas = curaduría manual primero (vos, 2026-10-08)
- PLAN-015 mkdocs RND: implementación acelerada al 16/10 (implicado por tu dirección)
- n8n §16.4-16.5: activación Día 1 (implicado por tu dirección)
- Stack cerrado: VPS actual + R2 + MkDocs + n8n + Cloudflare Access
- MVP_01 + MVP_04 NO se archivan
- A.3 Excalidraw nuevos pasan a Mes 2
- 50 archivos/día conservador

**Pendientes (necesitan tu `s`/N tras leer este plan):**

- **D1** — ¿Activamos §16.4-16.5 n8n hoy mismo (Día 1)? O esperás al 16/10 con calma
- **D2** — ¿El mail semanal de curaduría (paso 4 del anti-inundación) sale ya configurado desde el Lunes 12 o lo posponés a Mes 2?

---

## 9 · Próximo paso (post-`s`)

Cuando confirmes:
1. Guardar este plan en `raw/brainstorm/` (este mismo archivo es el guardado)
2. Arrancar **Día 1**: tareas reales en VPS sin tocar lo existente
3. Reportar al cierre del Día 1 con qué anduvo y qué no

---

## 10 · Referencias cruzadas (para abrir al ejecutar)

- Plan mkdocs RND canónico: `P:\00-repos\pitau-tech\pitauOS\99-SPECS_PLANS\BACKLOG_PLANS\PLAN-015-RND-mkdocs-jr-web-privada.md`
- n8n workflow armado: `specs/260924-plan-os-emilia-n8n.md` (especialmente §16.4-16.5)
- Pipeline moodboard LOCAL: `specs/260909-moodboard-vault-visual-local.md`
- Vault visual concepto: `wiki/glosario/conceptos/vault-visual.md`
- Cerebro digital Karpathy: `wiki/glosario/conceptos/cerebro-digital-karpathy.md`
- Backlog Nextcloud desplazado: `specs/260917-backlog-nextcloud-vps-storage.md`
- Plan trimestral vigente: `specs/260910-plan-trimestral-unificado-studio-os-emilia.md`
- Proyecto Emilia: `proyectos/STUDIO_OS-Emilia/00-index.md`
- Handover candidato previo (guardado el 2026-10-08 mañana): `raw/brainstorm/b-2026-10-08-handover-mes1.md`
- AGENTS.md reglas del vault (HITL, formato, etc.)

---

*Generado por Sol + @brainstormy el 2026-10-08 America/Argentina/Buenos_Aires — pendiente `s` para Día 1.*
