---
tipo: indice
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [adr, indice, arquitectura, decisiones]
estado: activo
---

# Índice de ADRs (Architecture Decision Records) — Estudio

> **Convención**: `ADR-<DOMINIO>-<NNN>-<slug>.md`
> Dominios: `INFRA` (infraestructura), `TOOL` (herramientas), `PROC` (procesos), `DATA` (datos), `SEC` (seguridad)

---

## Infraestructura (INFRA)

| Nº | Título | Estado | Fecha | Resumen |
|----|--------|--------|-------|---------|
| [ADR-INFRA-001](ADR-INFRA-001-leantime-selfhosted.md) | **Leantime Self-Hosted para PM con Gantt y Sprints** | Propuesto | 2026-07-24 | PM real ($0/mes) en hardware propio vía Docker + SQLite + Tailscale/CF Tunnel |
| [ADR-INFRA-002](ADR-INFRA-002-vps-dedicado-estudio.md) | **VPS Dedicado para el Estudio (Aislamiento Total)** | Aceptado | 2026-07-24 | VPS propio (Hetzner CX22) para Leantime, Wiki mirror, Backups, Monitoring — aislado de proyectos externos |

---

## Herramientas (TOOL)

| Nº | Título | Estado | Fecha | Resumen |
|----|--------|--------|-------|---------|
| [ADR-TOOL-001](ADR-TOOL-001-mkdocs-netlify-wiki.md) | **Wiki Estática: MkDocs Material + Netlify Identity** | Aceptado | 2026-07-24 | Wiki privada ($0/mes) con auth magic link, wikilinks, search, git-backed |

---

## Procesos (PROC)

| Nº | Título | Estado | Fecha | Resumen |
|----|--------|--------|-------|---------|
| — | *(pendiente)* | — | — | Flujos de trabajo, revisiones, entregas,命名 convenciones |

---

## Datos (DATA)

| Nº | Título | Estado | Fecha | Resumen |
|----|--------|--------|-------|---------|
| — | *(pendiente)* | — | — | Estructura vault, nomenclatura, binarios, backups |

---

## Seguridad (SEC)

| Nº | Título | Estado | Fecha | Resumen |
|----|--------|--------|-------|---------|
| — | *(pendiente)* | — | — | Auth, acceso remoto, secrets, auditoría |

---

## Plantilla para nuevos ADRs

```markdown
---
tipo: adr
fecha_creacion: YYYY-MM-DD
ultima_actualizacion: YYYY-MM-DD
tags: [adr, <dominio>, <tags>]
estado: propuesto|aceptado|rechazado|deprecado|superado
categoria: infra|tool|proc|data|sec
numero: NNN
---

# ADR-<DOMINIO>-<NNN>: <Título corto>

## Contexto
<Situación, restricciones, problema a resolver>

## Decisión
<Qué se decide, con suficiente detalle para implementar>

## Alternativas Consideradas
| Alternativa | Pros | Contras | Por qué no |
|-------------|------|---------|------------|

## Consecuencias

### Positivas
- ...

### Negativas / Riesgos / Deuda Técnica
- ...

### Trabajo Futuro / Seguimiento
- [ ] Acción 1
- [ ] Acción 2

## Referencias
- Enlaces a docs, issues, ADRs relacionados, análisis previos
```