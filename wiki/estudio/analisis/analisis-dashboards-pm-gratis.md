---
tipo: analisis
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [analisis, pm, dashboards, gratis, free, alternativas, plane, github-projects, gitlab, wekan, kanboard, focalboard, leantime, taskca]
estado: borrador
---

# Análisis: Alternativas GRATUITAS (Zero Cost) a Plane para Dashboards y PM

## Premisa: **$0/mes obligatorio**

Sin VPS, sin dominio pagado, sin SaaS per-seat. Solo infraestructura que ya tenés (GitHub/GitLab, Netlify, PCs del equipo).

---

## Opciones Reales (ordenadas por viabilidad para tu caso)

### 1. GitHub Projects (si ya usan GitHub) — **GANADOR PRÁCTICO**

| Qué tenés | Qué NO tenés |
|-----------|--------------|
| ✅ Kanban board nativo | ❌ Gantt nativo (solo timeline beta) |
| ✅ Tabla tipo Excel (campos custom, filtros, agrupados) | ❌ Burndown/velocity automáticos |
| ✅ Roadmap (timeline view) | ❌ Cycles/Sprints formales |
| ✅ Issues = tareas, PRs = trabajo, Milestones = hitos | ❌ Insights/charts avanzados |
| ✅ Labels, assignees, due dates, dependencies | ❌ Wiki nativa (usás MkDocs) |
| ✅ Automatizaciones (GitHub Actions) | ❌ Mobile app dedicada (solo web) |
| ✅ Gratis ilimitado (repo privado + Projects v2) | |
| ✅ Auth = GitHub account (equipo ya tiene) | |
| ✅ API GraphQL completa | |

**Setup: 5 min.** Repo privado → Settings → Projects → New Project (Board/Table/Roadmap).

**Para arquitectura:** Creas un Project "Estudio" con vistas:
- **Kanban por fase**: Concurso → Briefing → Concepto → DD → Planning → Construcción → Entrega
- **Tabla por responsable**: Filtros guardados por persona
- **Roadmap**: Milestones = hitos contractuales (entrega DD, presentación cliente, inicio obra)
- **Issues templates**: `Entregable`, `RFI`, `Revisión`, `Hito`, `Certificación`

**Gap vs Plane:** No hay Gantt real ni burndown automático. Se suple con:
- **GitHub Projects (Table view) + campos `Start date`, `Target date`** → export CSV → gráfico en Excel/Sheets mensual
- **GitHub Actions** que cada lunes genera reporte markdown en `wiki/estudio/reportes/semanal-YYYY-MM-DD.md` (commiteado al vault)

---

### 2. GitLab (si ya usan GitLab) — Equivalente a GitHub Projects

| Feature | GitLab |
|---------|--------|
| Boards (Kanban) | ✅ Issue boards multi-proyecto |
| Roadmap / Gantt | ✅ **Roadmap nativo con dependencias** (mejor que GH) |
| Epics + Issues | ✅ Jerarquía nativa |
| Iterations (Sprints) | ✅ **Cycles formales** con burndown |
| Wiki | ✅ Integrada (pero usás MkDocs) |
| CI/CD | ✅ Para automatizaciones |
| Gratis | ✅ Ilimitado (self-managed o SaaS) |

**Si el repo está en GitLab → usá GitLab. No migres a GitHub solo por PM.**

---

### 3. Plane Cloud (Free Tier) — Solo si aceptás SaaS

| Plan | Límite |
|------|--------|
| **Free** | 1 workspace, **hasta 10 usuarios**, proyectos ilimitados, 1GB storage |
| **Pro** | $8/user/mes |

**Pros:** Plane real, zero setup, Gantt, Cycles, Insights, API.
**Contras:** Datos en EE.UU., límite 10 users (vos 5, OK hoy), futuro incierto (pueden cambiar límites), **no es self-hosted**.

> **Veredicto:** Úsalo **solo para probar 2 semanas** si querés validar UX antes de decidir self-host. Luego migras datos a GitHub Projects o self-host.

---

### 4. Self-hosted en hardware EXISTENTE (PC oficina / NAS / Server viejo)

| Hardware | Qué corre | Costo real |
|----------|-----------|------------|
| **PC oficina (Windows/Linux) 24/7** | Docker Compose (Plane, Wekan, Focalboard, Kanboard) | $0 (electricidad existente) |
| **NAS (Synology/QNAP/TrueNAS)** | Docker / Portainer nativo | $0 |
| **Raspberry Pi 4 (4-8GB)** | Plane (lento), Wekan, Kanboard, Focalboard | ~$50-80 una vez |
| **VPS gratis (Oracle Cloud Free Tier)** | 4 ARM cores, 24GB RAM, 200GB | **$0 para siempre** (siempre que Oracle no te bannee) |

#### Oracle Cloud Free Tier (la "VPS gratis" real)

```bash
# 4 ARM Ampere cores, 24GB RAM, 200GB Block Volume
# Ubuntu 22.04/24.04 ARM64
# Plane corre bien en ARM64 (imagen multi-arch)
```

**Riesgos:** Oracle banea cuentas sin aviso (uso bajo, regiones específicas, "always free" abuse). **No confíes producción crítica solo acá.** Úsalo como **staging / prueba / backup**.

**Setup Plane en Oracle (ARM64):**
```yaml
# docker-compose.yml - igual que doc anterior pero:
# image: makeplane/plane:latest  (multi-arch, corre en ARM64)
# Limitar memoria: deploy.resources.limits.memory: 2G (api), 1G (web), 512M (worker)
```

---

### 5. Alternativas Open Source Self-Hosted MÁS LIVIANAS que Plane

| Tool | Stack | RAM mínima | Gantt | Cycles/Sprints | Kanban | Mobile/PWA | Complejidad |
|------|-------|------------|-------|----------------|--------|------------|-------------|
| **Wekan** | Meteor (Node) + MongoDB | 1GB | ❌ | ❌ | ✅ Excelente | ✅ PWA | Baja |
| **Kanboard** | PHP + SQLite/MySQL | 256MB | ❌ | ❌ | ✅ Bueno | ❌ | Muy baja |
| **Focalboard** | Go + PostgreSQL/SQLite | 512MB | ❌ | ❌ | ✅ Tipo Notion | ✅ PWA | Baja |
| **Leantime** | PHP + MySQL | 512MB | ✅ **Sí** | ✅ **Sí** | ✅ | ❌ | Media |
| **Taskca** | Go + SQLite | 128MB | ❌ | ❌ | ✅ Simple | ❌ | Muy baja |
| **Restya Board** | Node + MongoDB | 512MB | ❌ | ❌ | ✅ | ❌ | Media |

#### Leantime — **La única con Gantt + Cycles gratis y ligera**

```bash
# docker-compose.yml
version: '3.8'
services:
  leantime:
    image: leantime/leantime:latest
    ports:
      - "8080:80"
    environment:
      - DB_CONNECTION=sqlite
      - APP_URL=http://localhost:8080
    volumes:
      - leantime_data:/var/www/html/storage
    restart: unless-stopped

volumes:
  leantime_data:
```

- **Gantt nativo** con dependencias
- **Sprints/Cycles** con burndown
- **Kanban + Lista + Tabla**
- **Wiki/Docs integrada** (Markdown)
- **Campos custom** por proyecto
- **PHP + SQLite** → corre en Raspberry Pi / NAS / PC viejo sin sudar
- **Auth**: Email/password, LDAP, OAuth2 (Google, GitHub, GitLab, Azure)
- **Mobile**: Responsive web (no PWA nativa pero usable)

> **Veredicto:** Si tenés un PC/NAS 24/7 y querés **Gantt + Sprints + Kanban gratis sin VPS** → **Leantime**.

---

### 6. Notion / ClickUp / Height (Free Tier SaaS) — Solo si aceptás vendor lock-in

| Tool | Free Tier | Límite real para equipo 5 |
|------|-----------|---------------------------|
| **Notion** | Ilimitado personal, **1000 bloques** workspace team | 1000 bloques = ~10 páginas medianas. **Insuficiente**. |
| **ClickUp** | Unlimited tasks, 100MB storage, **Gantt 1 view**, Dashboards limitados | Usable pero **Gantt solo 1 vista**, dashboards básicos. |
| **Height** | Ilimitado personal, **2.000 tasks** team | 2k tasks OK, pero **no Gantt en free**, no self-host. |
| **Taiga** | Open source, SaaS free hasta 5 users | Kanban + Epics + Sprints, **Gantt solo paid**. |

**Conclusión:** SaaS free tiers tienen **trampas** (límites de bloques, vistas, storage). Para arquitectura con planos, docs, entregables → **chocarás el límite en semanas**.

---

## Matriz de Decisión: $0/mes Obligatorio

| Tu situación | Mejor opción | Por qué |
|--------------|--------------|---------|
| **Repo en GitHub + no tenés servidor 24/7** | **GitHub Projects (v2)** | Ya tenés auth, issues, PRs, Actions. Board + Table + Roadmap. Zero setup. |
| **Repo en GitLab + no tenés servidor 24/7** | **GitLab (Boards + Roadmap + Iterations)** | Roadmap/Gantt nativo + Iterations (sprints) gratis. |
| **Tenés PC/NAS 24/7 en oficina + querés Gantt + Sprints** | **Leantime (Docker + SQLite)** | PHP ligero, Gantt real, Cycles, Kanban, Wiki, OAuth. Corre en Raspberry Pi. |
| **Tenés PC/NAS 24/7 + querés Plane exacto** | **Plane en Oracle Cloud Free Tier (ARM)** | Plane real, gratis, pero riesgo de baneo. Backup diario a GitHub/Wasabi. |
| **Solo Kanban simple, sin Gantt, sin Sprints** | **Wekan / Kanboard / Focalboard** | Más livianos, zero config, pero **menos features PM**. |
| **Quieren probar Plane UX antes de decidir** | **Plane Cloud Free (10 users)** | 2 semanas gratis, luego export CSV/JSON → migra a GitHub Projects o Leantime. |

---

## Recomendación Específica para TU Estudio (Argentina, 5 personas, GitHub, $0)

### Opción A: **GitHub Projects (v2) + MkDocs + GitHub Actions** — **Pragmática, zero infra**

```yaml
# .github/workflows/weekly-report.yml
name: Weekly PM Report
on:
  schedule:
    - cron: '0 8 * * 1'  # Lunes 8 AM Argentina
  workflow_dispatch:
jobs:
  report:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - name: Generate report
        uses: actions/github-script@v7
        with:
          script: |
            // Query GitHub Projects v2 via GraphQL
            // Generar markdown con: tareas abiertas/cerradas, por responsable, por fase, vencidas
            // Escribir a wiki/estudio/reportes/semanal-${{ github.run_id }}.md
      - name: Commit & Push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add wiki/estudio/reportes/
          git commit -m "chore: weekly PM report ${{ github.run_id }}" || exit 0
          git push
```

**Vistas en GitHub Projects (crearlas una vez):**
1. **Kanban por Fase** (columna = `Fase` custom field)
2. **Tabla "Mi semana"** (filter: `assignee:@me` + `due date:this week`)
3. **Roadmap "Hitos 2026"** (view: Roadmap, group by Milestone)
4. **Tabla "Entregables vencidos"** (filter: `due date < today` + `status != Done`)

**Gap vs Plane:** No burndown automático. **Solución:** Export CSV semanal → Google Sheets / Excel con plantilla de burndown → link en MkDocs.

---

### Opción B: **Leantime en PC oficina / NAS** — **Completa (Gantt + Sprints), self-hosted gratis**

**Requisitos:**
- 1 PC/NAS encendido 24/7 (o horario extendido 8-20hs)
- Docker instalado
- Puerto 8080 accesible en LAN (o Tailscale para acceso remoto)

**Setup (15 min):**
```bash
# En el PC/NAS
git clone https://github.com/Leantime/leantime.git
cd leantime
docker compose up -d
# Abrir http://PC-OFICINA:8080
# Setup admin, crear workspace, invitar equipo (email o Google OAuth)
```

**Acceso remoto (fuera de oficina):**
- **Tailscale** (gratis hasta 100 devices): Instalar en PC servidor + laptops equipo → `http://leantime.tailnet:8080` funciona en cualquier red.
- **Cloudflare Tunnel** (gratis): `cloudflared tunnel run --url http://localhost:8080` → URL `https://plane.estudio.ar` gratis con auth opcional.

**Backup (cron diario en el PC):**
```bash
# backup-leantime.sh
docker exec leantime-db sqlite3 /var/www/html/storage/database.sqlite .dump | gzip > ~/backups/leantime_$(date +%F).sql.gz
# Subir a Google Drive / OneDrive / GitHub (repo privado backups) via rclone
```

---

### Opción Híbrida Realista (lo que yo haría hoy)

| Necesidad | Herramienta | Costo |
|-----------|-------------|-------|
| **Wiki estática + Auth** | MkDocs + Netlify Identity | $0 |
| **Issues + Kanban + Roadmap + Tabla + Automatizaciones** | **GitHub Projects v2** | $0 |
| **Gantt ocasional / Burndown mensual** | Export CSV → Google Sheets (plantilla) | $0 |
| **Daily notes + Zettelkasten + Templates** | Obsidian + Syncthing/Git | $0 |
| **Sprints formales + Burndown automático + Gantt nativo** | **Leantime en PC oficina (opcional, fase 2)** | $0 |

**Empieza con Opción A (GitHub Projects).** Si en 2 meses el equipo pide "Gantt real" o "Sprints con burndown automático" → levantás Leantime en el PC de la oficina (15 min) y migras los issues (CSV import).

---

## Checklist de Migración a GitHub Projects (Hoy)

- [ ] Repo privado `vault-arquitectura` en GitHub (org del estudio)
- [ ] Settings → Projects → "New project" → "Board" → Nombre: "Estudio - PM"
- [ ] Custom fields (Settings → Fields):
  - `Fase` (Single select: Concurso, Briefing, Concepto, DD, Planning, Construcción, Entrega)
  - `Tipo` (Single select: Entregable, RFI, Revisión, Hito, Certificación, Coordinación)
  - `Área` (Single select: Arquitectura, Estructuras, Instalaciones, BIM, Legal, Gestión)
  - `Responsable` (User)
  - `Fecha inicio` (Date)
  - `Fecha objetivo` (Date)
  - `% Avance` (Number 0-100)
- [ ] Issue Templates (`.github/ISSUE_TEMPLATE/`):
  - `entregable.yml`, `rfi.yml`, `revision.yml`, `hito.yml`
- [ ] Vistas guardadas:
  - "Kanban por Fase" (Board, group by `Fase`)
  - "Mis tareas esta semana" (Table, filter: `assignee:@me` AND `Fecha objetivo` this week)
  - "Roadmap Hitos" (Roadmap, group by Milestone)
  - "Entregables vencidos" (Table, filter: `Fecha objetivo < today` AND `status != Done`)
- [ ] Milestones = Hitos contractuales (Entrega DD, Presentación Cliente, Inicio Obra, Recepción Provisoria)
- [ ] GitHub Action: Weekly report → `wiki/estudio/reportes/`
- [ ] Link en MkDocs: cada `proyectos/<proyecto>/00-index.md` → `[Ver tablero en GitHub Projects](https://github.com/orgs/estudio/projects/1/views/1?query=proyecto:google-london-hq)`

---

## Conclusión

**No necesitás Plane (ni VPS) para empezar.**

| Si... | Hacé esto hoy |
|-------|---------------|
| **Ya usan GitHub** | **GitHub Projects v2** → 15 min setup → Kanban + Roadmap + Tabla + Automatizaciones gratis para siempre |
| **Ya usan GitLab** | **GitLab Boards + Roadmap + Iterations** → nativo, gratis, Gantt incluido |
| **En 3 meses faltan Gantt/Sprints** | Levantás **Leantime** en PC oficina/NAS (Docker, SQLite, 15 min) → migras CSV |

**El documento completo está en:** `wiki/estudio/analisis-dashboards-pm-gratis.md`