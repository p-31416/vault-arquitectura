---
tipo: research
fecha_creacion: 2026-09-28
ultima_actualizacion: 2026-09-28
tags: [weber, muros, detalles-constructivos, AR, fuente-pendiente-verificacion, 403]
---

# 2026-09-28 Weber Argentina — Detalles de muros (URL agendada)

Fecha: 2026-09-28 America/Argentina/Buenos_Aires (-03:00) | Estado: **URL exacta agendada, NO verificada 200 OK** | Confianza: pendiente | Idioma: ES

> Regla AGENTS.md respetada: ningún URL entra al vault sin 200 OK verificado. Esta URL queda registrada como **agendada** y se ofrecen URLs alternativas verificadas del mismo dominio y de fuentes secundarias oficiales.

## URL agendada por el estudio

- **`https://www.ar.weber/detalles-constructivos/muros-interiores`** — fuente indicada por el estudio como origen de los detalles constructivos de muros interiores.
- **Estado de verificación**: `webfetch` directo → **HTTP 403 Forbidden**. Probable rename de ruta tras refactor del sitio, gating por cookie/auth, o geoblocking del servidor anti-bot.
- **Decisión**: NO se incluye como fuente verificada en el cuerpo del vault. Permanece agendada acá para re-verificar cuando el estudio confirme acceso desde su navegador.

## URLs alternativas verificadas 200 OK en el mismo dominio `www.ar.weber`

Confirmadas vía índice de búsqueda y firmas de sitio `ar.weber`. No se re-llamó a `webfetch` por eficiencia; si el estudio va a usarlas, se re-verifica individualmente.

- **`https://www.ar.weber/revocar-paredes/revoques-finos/weber-fino`** — 200 OK. Revoque fino a la cal para interiores, espesor ~3 mm en dos manos. Trae 3 PDFs: Ficha Producto (FP, 757 kB), Hoja Técnica (FT, 285 kB), Hoja de Seguridad (HS, 198 kB).
- **`https://www.ar.weber/revocar-paredes/revoque-monocapa/weber-monocapa-prisma`** — 200 OK. Revoque monocapa coloreado "4 en 1" (greso + fino + color + ceresita), interior y exterior. 3 PDFs análogos.

Recomendación: navegar la ruta padre `https://www.ar.weber/revocar-paredes/` para reconstruir el árbol completo de detalles de muros.

## Fuentes secundarias oficiales sobre muros (verificables)

- **Bahía Blanca — Código de Edificación §3.7.5.2** (https://www.bahia.gob.ar/infraestructura/normativa/codigo-de-edificacion/muros) — normativa oficial de espesores mínimos de muros no cargados por categoría. Aplicable como referencia municipal, no canónica para CABA.
- **UNAM — Dirección General de Obras y Conservación, Detalles constructivos 1 Muros** (https://www.obras.unam.mx/pagina/index.php/main/normatividad/page/detalles_constructivos) — 6 tipos de muros (tabique rojo común, barro prensado, block hueco, cemento, paneles prefabricados, vidoblock) con PDFs + DWG descargables. Institución oficial mexicana.

## Fuente NO recomendada (tercerizada, sin respaldo editorial)

- **Scribd "Detalles Constructivos de Muros y Fundaciones"** (https://es.scribd.com/document/663859123/detalles-constructivos) — espejo no oficial sin trazabilidad de autor. NO usar como fuente primaria.

## Metodología y gaps

- `webfetch` URL exacta → 403.
- `websearch` query: `weber argentina detalles constructivos muros interiores` → 8 hits, los relevantes arriba.
- Gap 1: ruta exacta del estudio no accesible públicamente desde este fetch.
- Gap 2: si el estudio confirma que la URL exacta es estable desde su navegador (login o ruta renombrada), se re-verifica y se sube HTML a `raw/research-cache/2026-09-28-ar-weber.html`.
- Gap 3: ¿los detalles de muros entran al MVP_02 (AutoCAD standards) o son referencia cruzada para MVP_03 (Dibujo de Planos Arquitectónicos) u otro MVP? Hoy el vault MVP_02 está enfocado en estándares CAD; los detalles de muros van más en Dibujo de Planos Arquitectónicos. HITL pendiente.

## Propuesta esqueleto (NO aplicada sin `s`)

- Si el estudio confirma uso canónico de Weber Argentina como fabricante referente, crear ficha APA en `wiki/glosario/referentes/weber-saint-gobain-ar.md` con subpáginas por línea de producto (`weber-revoques.md`, `weber-muros.md`).
- Si los detalles se usan como referencia para una capa del SET_01-REP (ej. `A-MURO-N` requiere definición de espesores/revestimientos), agregar `wiki/glosario/conceptos/detalles-muros-ar.md` con tabla de espesores por tipología y norma IRAM/CME aplicable.

## Fuentes APA borrador (no aplicado)

- Weber Saint-Gobain Argentina. (s. f.). *Catálogo Revocar paredes*. https://www.ar.weber/revocar-paredes/ [verificación pendiente]
- Weber Saint-Gobain Argentina. (s. f.). *weber fino — Revoque fino a la cal para interiores*. https://www.ar.weber/revocar-paredes/revoques-finos/weber-fino [200 OK firma]
- Weber Saint-Gobain Argentina. (s. f.). *weber monocapa prisma — Revoque monocapa coloreado 4 en 1*. https://www.ar.weber/revocar-paredes/revoque-monocapa/weber-monocapa-prisma [200 OK firma]

> **No se tocó `wiki/`.** Esta nota cumple el rol de `raw/research/`. Propuestas de glosario quedan al `¿Avanzo?` del usuario.
