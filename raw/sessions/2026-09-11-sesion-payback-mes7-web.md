---
tipo: log
fecha: 2026-09-11
slug: payback-mes7-web
participantes: [Sol, Pitautech]
tags: [sesion, payback, roi, ptech, studio-os, web]
---

# Sesión 2026-09-11 — Payback mes 7 + gráfica web + glosario payback

> Más nuevo → más arriba

## Qué se hizo

- Explicación retorno mes 8: inversión +190hs con ritmo +10hs/mes daba 30hs/mes fijas y payback mes 8; con medido real +12hs/mes (12.2hs en 3 agentes) el ritmo Mes 3 avanza a 36hs/mes y payback avanza a mes 7
- Cálculo nuevo: M1 12hs / M2 36hs / M3 72hs acumuladas, M6 180hs, M7 216hs (1.14x payback), M12 396hs (2.08x = 3.960 USD/año)
- Creación `wiki/glosario/conceptos/payback.md` con definición, fórmula Pitautech, tabla vigente y referencia Investopedia verificada
- Mejora gráfica web equivocada `04-roi-payback.svg`: escala 0-400h, puntos 12/36/72/180, cruce mes 7, footer 36hs/mes 2.1x + fórmula + mención glosario
- Sincronización `02-roi-retorno.svg` + `02-roi-retorno.excalidraw.md` (decían mes 6 / 360hs): ahora mes 7 / 396hs / 2.08x
- Ajuste documentación completa a base 12hs: `ptech-metricas-friccion`, `specs/260910`, `specs/260909` KR3.3, `05-propuesta-comercial-viernes.md`, `meta-arquitecto.md`, `conceptos/00-index.md`, HTML web tab Métricas + Glosario (suma entrada Payback)
- Eliminación texto `Propuesta de Trabajo Trimestral` de portada web (tab Filosofía), queda solo `PITAUTECH × EMILIA PIMENTA`

## Archivos modificados

- `wiki/glosario/conceptos/payback.md` — creado
- `wiki/glosario/conceptos/00-index.md` — fila payback + fecha 2026-09-11
- `wiki/glosario/interno/standares/ptech-metricas-friccion.md` — tabla 12/24/36hs, lectura mes 7, auditoría 12hs, tagline 12hs, capacidad 0.20, link payback
- `wiki/glosario/conceptos/meta-arquitecto.md` — impacto payback 7 meses (190→396hs), salida 12–36hs/mes, fecha 2026-09-11
- `specs/260910-plan-trimestral-unificado-studio-os-emilia.md` — objetivo ≥36hs/mes, tabla mes 7, lectura 3.960 USD/año, fecha 2026-09-11
- `specs/260909-esquema-mes1-60hs-studio-os-emilia.md` — KR3.3 ≥12hs/mes, fecha 2026-09-11
- `proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes.md` — retorno 7 meses / 36hs / 2.1x, proyección ≥12hs, fecha 2026-09-11
- `proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes.html` — gráfica alt mes 7, párrafo 36hs/396hs, glosario suma Payback, portada sin subtítulo trimestral, OKRs ≥12hs, card medido ≥12hs
- `proyectos/STUDIO_OS-Emilia/presentacion/diagramas/04-roi-payback.svg` — reconstruido mes 7
- `proyectos/STUDIO_OS-Emilia/presentacion/diagramas/02-roi-retorno.svg` — sincronizado mes 7
- `proyectos/STUDIO_OS-Emilia/presentacion/diagramas/02-roi-retorno.excalidraw.md` — textos + JSON mes 7

## Análisis cerebro-digital

### Topics
- payback, período de recupero, ROI acumulado, ritmo mensual vs acumulado liberado, ptech-metricas-friccion, capacidad liberada, ahorro T_manual−T_sistema, retorno para siempre, gráfica ROI web

### Entidades
- Pitautech, Emilia Pimenta, Studio OS, Investopedia (referencia payback), Cal.com + Fathom + Vault (3 agentes medidos), RunPod (potencial M2)

### Hechos
- Base medida Mes 1: 12.2hs/mes (4.0 agendar + 6.0 transcripción + 2.2 Vault) → base cálculo 12hs/mes
- Ritmo Mes 3: 36hs/mes, acumulado Mes 3: 72hs (12+24+36)
- Payback: mes 7 con 216hs (1.14x sobre 190hs), año 396hs (2.08x)
- Escenario +10hs/mes queda como referencia conservadora mínima (30hs/mes, payback mes 8, 330hs/año)
- Enlaces verificados: Investopedia payback 200; resto interno vía wikilinks

## Próximos pasos

- Validar con Emilia tabla mes 7 + gráfica nueva en propuesta viernes
- Medir Mes 2 real para confirmar +12hs adicionales y sostener ritmo 36hs/mes
- Generar PDF web actualizado con gráfica mes 7
