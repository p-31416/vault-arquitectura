---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
estado: aprobado
tags: [unificado, quick-wins, cierre-mes1, mes2, fuentes, n8n, studio-os]
idioma: es
---

# Plan unificado Studio OS — 23 specs hacia 4 vivos + quick wins

> Origen: revisión bottom-up 2026-10-16 con SOL (worker → inventario → reporte horas → fuentes → calculadora → MCPs → Mes 2). Relacionado: `specs/261016-worker-sherlock-fuentes.md`, `specs/archived/261016-inventario-automatizaciones-mes1.md` (foto 16/10), `specs/261013-plan-fuentes-emilia-inbox.md` (§10-11 nuevos), `specs/261009-spec-ingesta-fuentes.md`, `specs/261013-plan-cierre-mes1-calculadora-emilia.md`, `specs/archived/261013-reporte-horas-mes1-emilia.md` (evidencia), `proyectos/STUDIO_OS-Emilia/presentacion/06-dashboard-cierre-mes1.md`. Archivados con mapa en `specs/archived/README.md`.

## 1. Objetivo

Avanzar con lo construido hacia valor visible para Emilia: 1 hoja con ahorro por flujo, dashboard con tracking por bloque, fuentes que avanzan solas hacia wiki, Mes 2 semana a semana. Todo con PC apagada incluida vía nube (n8n VPS + GitHub Actions).

## 2. Los 4 vivos (todo lo demás archiva o referencia)

| Vivo | Incluye specs previos | Estado |
|---|---|---|
| A. Cierre Mes 1 + dashboard | 261013-cierre + 261013-reporte-horas + 260909-esquema-60hs + 260910-trimestral + 06-dashboard | Dashboard base 13/10, tracking por bloque queda para QW4 |
| B. Fuentes inbox + worker | 261009-ingesta + 261013-inbox (§10-11) + 261016-worker + 260909-threads + 260909-plan-accion-web + 261009-vista-yt | Router 17 nodos verificado, Sheet header hecho, grupo + chat_id + worker dispatch quedan para QW1/QW6 |
| C. OS-Emilia n8n | 260924-plan-n8n + arquitectura v1.3 + playbooks + 261013-voz-telegram + 260929-alta-leantime + 260909-fathom-specs | Fathom Core canvas único + Agenda/Cancel/Modif verificados, hardening queda para QW5/QW8 |
| D. Mes 2 EXPERIMENTAR | 261013-backlog-mes2 + 260917-nextcloud + MVP_02/04/06 + 261013-calculadora | 3 módulos (Agente IA 5hs + CAD 6.7hs + Comfy 4.2hs), precio anclado a horas liberadas |

Archivan como referencia: 260907-telegram-vault (reemplazado por Router), 260907-ghl-* (superado comercial), 260909-github-actions (intacto como backlog, worker lo retoma), 260909-moodboard-local (avanza en Mes 2-C).

## 3. Análisis completado (evidencia 16/10)

- **Telegram Router `YWpuV5p0vCDTbIHz`:** 17 nodos reales, Jina + Parseo + Append Sheet2, `/sync` + `/help` operativos. Queda: grupo Fuentes + `FUENTES_CHAT_ID` + mover Sheet a `OS-Emilia/` + compartir.
- **Agenda/Cancel/Modif:** reserva real `gnCrXcR1j3mz8Hd9THXhyh` 08/10, lista con botones, Switch v3.4 patrón verificado. Queda: hoja clientes reales + evento 60 min Meet + filtro chat_id.
- **Fathom Core `UeDkqVZSeLnae5cF`:** cron 07:00 + `/sync`, ventana 26h, doble salida md + Doc, clasificación por lados. Queda: dedup Bot State.
- **Fuentes:** Sheet ID `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI` con header A1:I1 + append verificado 14/10. YT perfecto, IG viable, SHARE por probar con 1 link Emilia. Rama IDEA + PDF-link diseñada §10.
- **Horas:** 19.5hs reuniones + 58-65hs humano + 1h máquina medida. Calculadora `scripts/calculadora-costo-flujo-n8n.py` verificada: réplica 128.33 + operativo 39.36/mes. Queda: subir a Leantime + tracking por bloque.
- **Leantime:** proyecto 4 + Emilia id 5 aceptada 13/10 + M1-M4 + tasks 443-457. Goals a mano en UI.
- **MCPs (7 en `opencode.json`):** comfyui local, n8n-mcp remote, fathom (Emilia), fathom-proyectopi (propio), leantime, autodesk-help (docs oficial en playbooks), autocad (SETs estándares).
- **Emilia Plus:** App Drive + Proyecto Studio OS + shares hacia cola, todo curaduría SOL. Presencial: actualizar Obsidian + Codex Sign in Plus + 1 ficha en vivo.

## 4. Hoja para Emilia — manual vs sistema vs capacidad nueva

| Flujo | Manual | Con sistema | Ahorro |
|---|---|---|---|
| Agendar reunión | 15 min (10 antes + 5 después) | 1 mensaje voz/texto | ~14 min × 5/sem ≈ 5hs/mes |
| Nota de voz (transcribir + contexto + memoria) | ~8 min (escuchar + anotar + archivar) | 0 (Gemini + Redis + Postgres) | ~8 min × 5/sem ≈ 3hs/mes |
| Link inbox → memoria | ~10 min (captura + clasifica + archiva + recordar) | link al grupo, resto solo | ~10 min × 25/sem ≈ 18hs/mes |
| Traer reunión Fathom | 45 min (ver + resumir + archivar) | 0 (cron + md + Doc) | ~45 min × 11/mes ≈ 8hs/mes |
| Fuente online → memoria | se pierde | link al grupo + análisis solo | capacidad nueva |
| Croquis Comfy | 60 min aceitado | ~1 min proceso | 60X a validar Mes 2 |
| Documentación oficial | búsqueda manual dispersa | Autodesk Help MCP en playbooks | capacidad nueva |

Fórmula: `Ahorro = T_manual − (T_revisión + T_máquina)`. **Eficiencia = Resultados / Recursos: tardar la mitad documentando = ganar el doble (2X).** O2 = lo que costó (65hs), O3 = lo que queda y ahorra (≥12hs/mes).

## 5. Quick wins ordenados (próximos 7 días)

| # | Quick win | Esfuerzo | Desbloquea | Dueño |
|---|---|---|---|---|
| QW1 | Grupo Fuentes + bot + Emilia, leer chat_id, pegar `FUENTES_CHAT_ID`, mover Sheet a `OS-Emilia/` + compartir | 15 min | toda la cola fuentes | Sol + Emilia |
| QW2 | 1 share ChatGPT Emilia → carril SHARE → `raw/entradas-emilia/` | 10 min | puente GPT↔vault | Emilia manda, Sol corre |
| QW3 | Rama IDEA + PDF-link en Router (2 Switch + append, patrón `Prepara Fila`) | 30 min | ideas con texto entran, PDFs van a worker | Sol en n8n |
| QW4 | Subir 65hs a Leantime + tabla tracking por bloque + 3 procesos manual vs sistema | 1h | dashboard con números + base ROI Mes 2 | Sol |
| QW5 | Evento Cal 60 min Meet + hoja clientes reales + filtro chat_id Router | 45 min | agenda lista para clientes reales | Sol + Emilia |
| QW6 | Worker `sherlock-fuentes.yml` dispatch manual + ver commit `raw/research/` + Sheet `procesado` | 20 min | valida nube con PC apagada, precede vaultworm | Sol en GitHub |
| QW7 | Presencial: actualizar Obsidian + Codex desktop Sign in Plus + `codex mcp list` + 1 ficha en vivo | 1h | Emilia aporta con criterio, O1 avanza hacia 100% | Sol + Emilia |
| QW8 | Dedup Bot State en Fathom Core + rotar token expuesto `create-user-emilia.ps1:4` | 1h | cero re-escrituras + seguridad | Sol |

Orden sugerido: QW1 → QW2 → QW3 hoy (cola viva), QW4 → QW5 mañana (números + agenda), QW6 lunes (clase worker + digest), QW7 presencial, QW8 cierre.

## 6. Mes 2 semana a semana (16hs de 60hs, resto sprints + soporte)

- **S1:** QW4-QW6 cerrados + Agente IA Telegram en lenguaje natural (12 pomodoros ≈ 5hs, reusa Agenda/Cal/Sheets). Ahorro 5hs/mes.
- **S2:** CAD un tipo de plano bien usado SET_01 + conteo→planilla + clase (16 pomodoros ≈ 6.7hs). Ahorro 12-15hs por plano.
- **S3:** Comfy en su PC upscale o croquis + modelos + instructivo (10 pomodoros ≈ 4.2hs). Ahorro a medir S1 Mes 2 con 1 croquis real.
- **S4:** Medición + roadmap Mes 3 (Nextcloud, monitoreo VPS, plugin Leantime, RunPod, YT Nivel 2).

Cada módulo cierra con ahorro medido en Leantime + demo + ficha wiki. Propuesta comercial anclada a horas liberadas.

## 7. Criterio de done del unificado

Link al grupo → Sheet con tipo auto → worker `raw/research/` + `procesado` → contenidos `raw/contenidos/` → gate `s` → `wiki/fuentes/` → vaultworm semanal → glosario, todo con PC apagada, con hoja 1 carilla y dashboard con tracking visibles para Emilia.
