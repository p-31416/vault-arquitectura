---
tipo: log
fecha: 2026-10-16
tags: [sesion, sherlock, research, sheet-links, acceso-bloqueado, cierre]
---

# Sesión 2026-10-16 — Sheet links gid 1838858946 @sherlock + cierre día

## Qué se hizo

- **Pedido SOL**: `@sherlock investiga sobre los links que recibimos en el sheet https://docs.google.com/spreadsheets/d/18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI/edit?gid=1838858946#gid=1838858946`.
- **Delegación @sherlock**: task subagent con prompt extraer links + verificar 200/404 + crudos en `raw/research/`.
- **Resultado**: 0 links. Sheet no público — 4 endpoints (`export?format=csv`, `edit`, `gviz/tq`, `htmlview`) devuelven `401`, exigen login Google. Nada inventado.
- **Respuesta a SOL**: opciones desbloqueo (Anyone with link Viewer + Publish to web / pegar CSV / adjuntar CSV como fuente_binaria).
- **Cierre día**: `cerramos por hoy` → este log.

## Archivos modificados

- `raw/research/2026-10-16-sheet-links-gid-1838858946.md` (madre diagnóstico acceso)
- `raw/research/2026-10-16-sheet-links-gid-1838858946-crudo.md` + `-stub.md`
- `raw/research-cache/2026-10-16-sheet-links-gid-1838858946.json`
- `raw/research/00-index.md` (fila 2026-10-16, estado `bloqueado-acceso`)
- `raw/sessions/2026-10-16-sesion-sheet-links-cierre.md` (este archivo)

## Qué sigue

1. SOL desbloquea sheet (sharing público o CSV pegado).
2. Relanzar `@sherlock investiga sheet links` con contenido visible.
3. Flujo estándar: research → `¿Avanzo? s` → `@contenidos` → `¿Avanzo a wiki?` → `@vaultworm-arq`.

## Cerebro-digital

- Topics: sheet-links-gid-1838858946, acceso-401-google-sheets, sherlock-solo-research, desbloqueo-sharing-csv.
- Entidades: Google Sheets export/gviz/htmlview endpoints, raw/research madre+crudo+stub+cache, 00-index research.
- Hechos: 4×401 verificado 2026-10-16; 0 URLs para verificar; plan por-link listo al desbloquear; sin escritura en wiki/ ni contenidos/.
