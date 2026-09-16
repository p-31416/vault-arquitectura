---
tipo: analisis
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [analisis, pm, dashboards, plane, obsidian, integracion, arquitectura-sistema]
estado: borrador
---

# Análisis: Integración de Dashboards y Gestión de Proyectos en el Ecosistema del Estudio

## 1. Contexto y Problema

**Situación actual:**
- Vault Obsidian (`wiki/`, `proyectos/`) como **fuente de verdad documental** (playbooks, templates, legales, estándares, lecciones aprendidas).
- Despliegue wiki estática vía **MkDocs + Netlify** (acceso web, auth, búsqueda, versión).
- **Falta total** de: gestión de tareas, Kanban, Gantt, seguimiento de hitos, dashboards de avance, daily/weekly reviews, asignación de responsables, alertas.

**Necesidad declarada:**
> "Que cualquiera del estudio se loggee y vea la wiki correspondiente con playbooks, templates, etc. **Y además** gráficos, dashboards de avances, tareas diarias/semanales/mensuales, evaluaciones."

**Restricciones:**
- Equipo: 4-5 personas (arquitectos, dibujantes, BIM managers).
- Presupuesto: $0-10/mes (estudio argentino, sin presupuesto SaaS per-seat).
- Infra: Git repo + Netlify (wiki), sin servidor propio hoy.
- Habilidad técnica: Media (arquitectos, no devs full-time).

---

## 2. Qué es Plane (y por qué aparece en la conversación)

### Definición
**Plane** es una herramienta de **gestión de proyectos open-source** (MIT license), **self-hosted**, tipo **Linear / Jira / Height / ClickUp** pero moderno, rápido y diseñado para equipos de producto/ingeniería/arquitectura.

### Stack técnico
- **Frontend**: Next.js (React), TypeScript, Tailwind.
- **Backend**: Django (Python), GraphQL (Strawberry), Celery (tareas async).
- **DB**: PostgreSQL.
- **Cache/Queue**: Redis.
- **Auth**: JWT, OAuth2 (Google, GitHub, GitLab, Microsoft, SAML/OIDC en roadmap).
- **Despliegue**: Docker Compose / Kubernetes / Railway / Render / Fly.io.

### Funcionalidades clave (v0.23+, 2024-2025)

| Módulo | Qué resuelve para arquitectura |
|--------|--------------------------------|
| **Workspaces** | Un workspace = tu estudio. Proyectos aislados o compartidos. |
| **Projects** | Cada `cliente-proyecto-ciudad` = un Project en Plane. |
| **Issues / Work Items** | Tareas, hitos, RFI, entregables, revisiones. Tipos customizados. |
| **Cycles (Sprints)** | Iteraciones de 1-4 semanas. Planning, review, retro, burndown automático. |
| **Modules (Views)** | **Kanban**, **Lista**, **Gantt**, **Calendar**, **Tabla** (Excel-like), **Roadmap**. |
| **Pages / Docs** | Wiki interno **dentro de Plane** (Markdown, bloques, embeds). |
| **Properties custom** | Campos: `fase` (concurso/dd/construcción), `area_m2`, `responsable`, `prioridad`, `estado_legal`, `certificado_%`. |
| **Filters + Saved Views** | "Mis tareas esta semana", "Entregables vencidos", "RFI pendientes cliente X". |
| **Charts / Insights** | Burndown, velocity, cumulative flow, lead time, cycle time, throughput. |
| **Automations** | "Si issue pasa a 'En revisión' → notificar a arquitecto a cargo". |
| **API + Webhooks** | Sincronizar con GitHub/GitLab, notificar a Slack/Email, crear issues desde webhook. |
| **Import** | CSV, JSON, Jira, Linear, Asana, Trello, GitHub Projects. |

### Diferencia con Obsidian + Plugins (Dataview, Tasks, Projects, Kanban)

| Aspecto | Obsidian + Plugins | Plane |
|---------|-------------------|-------|
| **Multi-usuario real** | ❌ Archivos locales, sync manual, conflictos | ✅ DB central, locking, permisos, auditoría |
| **Vistas Kanban/Gantt/Calendar** | ⚠️ Básicas, solo local | ✅ Nativas, performantes, drag-drop real |
| **Dashboards / Gráficos** | ⚠️ DataviewJS / Charts plugin (manual, frágil) | ✅ Insights automáticos, burndown, velocity |
| **Ciclos / Sprints** | ❌ Manual (Templater + calendar) | ✅ Cycles con dates, planning, review, auto-burndown |
| **Notificaciones / Inbox** | ❌ No | ✅ Inbox, email, webhook, Slack |
| **Permisos / Roles** | ❌ No | ✅ Admin / Member / Viewer / Custom roles |
| **Mobile / Web access** | ❌ Solo app móvil (solo lectura/edición simple) | ✅ PWA completa, responsive |
| **API / Integraciones** | ❌ Solo file-based | ✅ GraphQL API, Webhooks, GitHub/GitLab sync |
| **Costo** | $0 (local) | $5-10/mes (VPS) + tiempo setup |
| **Curva de aprendizaje** | Alta (plugins, sintaxis, YAML) | Media (UI tipo Linear, intuitiva) |

> **Conclusión:** Obsidian es **knowledge base personal/equipo técnico**. Plane es **project management multi-usuario real**. No se sustituyen; se complementan.

---

## 3. Arquitectura de Integración Propuesta: "Wiki + PM"

### Diagrama mental

```
┌─────────────────────────────────────────────────────────────────┐
│                     EQUIPO (4-5 usuarios)                       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│  OBSIDIAN     │  │   PLANE       │  │   MKDOCS      │
│  (Local)      │  │   (VPS Web)   │  │   (Netlify)   │
│               │  │               │  │               │
│ - Daily notes │  │ - Tasks/Kanban│  │ - Playbooks   │
│ - Templates   │  │ - Gantt/Charts│  │ - Templates   │
│ - Detalles    │  │ - Cycles      │  │ - Legales     │
│   constructivos│  │ - Insights    │  │ - Estándares  │
│ - BIM notes   │  │ - Docs/Notes  │  │ - Lecciones   │
│ - Zettelkasten│  │ - Wiki ligera │  │   aprendidas  │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │   Links bidireccionales (URLs)       │
        └──────────────┬───────────────────────┘
                       ▼
            ┌───────────────────────┐
            │   GIT REPO (Fuente)   │
            │   vault-arquitectura  │
            └───────────────────────┘
```

### Reglas de oro (Single Source of Truth)

| Dominio | Source of Truth | Por qué |
|---------|----------------|---------|
| **Conocimiento técnico, playbooks, templates, legales, estándares** | **Vault Obsidian → MkDocs** | Versionable, buscable, público/privado controlado, ligero, offline-first |
| **Tareas, hitos, asignaciones, avances, dashboards, ciclos, evaluaciones** | **Plane** | Multi-usuario, vistas nativas, notificaciones, API, web, mobile |
| **Notas de obra, daily notes, zettelkasten, borradores, thinking** | **Obsidian local** | Personal, rápido, plugins poderosos, sin fricción |
| **Modelos BIM, planos, renders, PDFs escaneados** | **`/activos/` (gitignored) + referencias en MkDocs/Plane** | Binarios fuera de git, rutas referenciadas |

### Integración práctica (cómo linkear)

| Desde | Hacia | Cómo |
|-------|-------|------|
| MkDocs (wiki) | Plane Project | Link en sidebar / página del proyecto: `[Ver tablero en Plane →](https://plane.estudio.ar/workspace/estudio/project/google-london-hq)` |
| Plane Issue/Module | MkDocs doc | Campo `wiki_url` en Property custom → botón "Abrir spec" |
| Plane Doc (wiki ligera) | MkDocs | `> Ver versión completa en [Wiki del Estudio](https://wiki.estudio.ar/wiki/proyectos/google-london-hq)` |
| Obsidian (local) | Plane | Plugin `obsidian-plane` (community) o URL en frontmatter: `plane_url: "https://plane.estudio.ar/issue/EST-123"` |
| Git Commit | Plane Issue | Convención: `git commit -m "EST-123: Ajuste planta baja según RFI-04"` → Plane auto-linkea si configuras GitHub/GitLab integration |

---

## 4. Opciones de Despliegue de Plane (Costo Real Argentina 2026)

| Opción | Costo mensual | Complejidad | Performance | Backups | Recomendación |
|--------|---------------|-------------|-------------|---------|---------------|
| **VPS Hetzner CX22 (2 vCPU, 4GB RAM, 40GB SSD) + Docker Compose** | **~€4.50 / ~$5.000 ARS** | Media (1 tarde) | ✅ Excelente | Cron + pg_dump + rclone a S3/Wasabi | **GANADOR** |
| DigitalOcean Droplet 2GB + Docker | $12 USD | Media | ✅ Bueno | Snapshots ($$) | Caro para ARS |
| Railway / Render / Fly.io (managed) | $5-10 USD | Baja | ✅ Bueno | Automático | Pago en USD, factura extranjera |
| Self-hosted en PC oficina (Tailscale + Docker) | $0 (hardware existente) | Media | ⚠️ Depende uplink | Manual | Solo si IP fija / buen uplink / 24x7 |
| Plane Cloud (plane.so) | $0-8/user/mes | Cero | ✅ Mejor | Automático | **Pago en USD**, datos en EE.UU. |

### Setup mínimo en VPS (docker-compose.yml)

```yaml
# /opt/plane/docker-compose.yml
version: '3.8'
services:
  plane-db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: plane
      POSTGRES_USER: plane
      POSTGRES_PASSWORD_FILE: /run/secrets/postgres_password
    volumes:
      - plane_db_data:/var/lib/postgresql/data
      - ./backups:/backups
    secrets:
      - postgres_password
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U plane"]
      interval: 10s
      timeout: 5s
      retries: 5

  plane-redis:
    image: redis:7-alpine
    volumes:
      - plane_redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  plane-api:
    image: makeplane/plane:latest
    command: ["api"]
    environment:
      DATABASE_URL: postgresql://plane:{{POSTGRES_PASSWORD}}@plane-db:5432/plane
      REDIS_URL: redis://plane-redis:6379/0
      SECRET_KEY_FILE: /run/secrets/secret_key
      ALLOWED_HOSTS: "plane.estudio.ar,localhost"
      CSRF_TRUSTED_ORIGINS: "https://plane.estudio.ar"
      CORS_ALLOWED_ORIGINS: "https://wiki.estudio.ar"
      EMAIL_BACKEND: django.core.mail.backends.smtp.EmailBackend
      EMAIL_HOST: smtp.tu-proveedor.com
      EMAIL_PORT: 587
      EMAIL_HOST_USER_FILE: /run/secrets/email_user
      EMAIL_HOST_PASSWORD_FILE: /run/secrets/email_pass
      DEFAULT_FROM_EMAIL: "Plane Estudio <plane@estudio.ar>"
    depends_on:
      plane-db:
        condition: service_healthy
      plane-redis:
        condition: service_healthy
    secrets:
      - postgres_password
      - secret_key
      - email_user
      - email_pass
    deploy:
      resources:
        limits:
          memory: 1G

  plane-web:
    image: makeplane/plane:latest
    command: ["web"]
    environment:
      NEXT_PUBLIC_API_URL: "https://plane.estudio.ar/api"
      NEXT_PUBLIC_WS_URL: "wss://plane.estudio.ar/ws"
    depends_on:
      - plane-api

  plane-worker:
    image: makeplane/plane:latest
    command: ["worker"]
    environment:
      DATABASE_URL: postgresql://plane:{{POSTGRES_PASSWORD}}@plane-db:5432/plane
      REDIS_URL: redis://plane-redis:6379/0
      SECRET_KEY_FILE: /run/secrets/secret_key
    depends_on:
      plane-db:
        condition: service_healthy
      plane-redis:
        condition: service_healthy
    secrets:
      - postgres_password
      - secret_key
    deploy:
      resources:
        limits:
          memory: 512M

  plane-beat:
    image: makeplane/plane:latest
    command: ["beat"]
    environment:
      DATABASE_URL: postgresql://plane:{{POSTGRES_PASSWORD}}@plane-db:5432/plane
      REDIS_URL: redis://plane-redis:6379/0
      SECRET_KEY_FILE: /run/secrets/secret_key
    depends_on:
      plane-db:
        condition: service_healthy
      plane-redis:
        condition: service_healthy
    secrets:
      - postgres_password
      - secret_key

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certbot/conf:/etc/letsencrypt:ro
      - ./certbot/www:/var/www/certbot:ro
    depends_on:
      - plane-web
      - plane-api
    restart: unless-stopped

volumes:
  plane_db_data:
  plane_redis_data:

secrets:
  postgres_password:
    file: ./secrets/postgres_password.txt
  secret_key:
    file: ./secrets/secret_key.txt
  email_user:
    file: ./secrets/email_user.txt
  email_pass:
    file: ./secrets/email_pass.txt
```

**Backup automático (cron diario):**
```bash
# /etc/cron.daily/plane-backup
#!/bin/bash
docker exec plane-db pg_dump -U plane plane | gzip > /backups/plane_$(date +%F).sql.gz
rclone copy /backups/ wasabi:plane-backups/ --max-age 30d
```

---

## 5. Matriz de Decisión: ¿Qué herramienta para qué?

| Necesidad | Herramienta | Por qué |
|-----------|-------------|---------|
| **Leer playbook de detalle constructivo** | MkDocs (wiki) | Estático, versionado, buscable, offline-ready |
| **Ver dashboard de avance del proyecto "Google London HQ"** | Plane (Module: Gantt + Charts) | Gráficos reales, multi-usuario, filtros por fase/área |
| **Asignar tarea "Revisar RFI-12" a dibujante con fecha** | Plane (Issue + Cycle) | Notificación, due date, responsable, tracking |
| **Daily note personal: "Hoy resolví RFI-12, mañana avanzo planta 3"** | Obsidian (Daily Note + Tasks plugin) | Privado, rápido, linked a `[[RFI-12]]` |
| **Evaluación mensual de carga de equipo** | Plane (Insights → Velocity + Workload) | Datos reales, no manuales |
| **Biblioteca de detalles constructivos (templates)** | MkDocs (wiki/estandares) + `activos/` | Binarios referenciados, no duplicados |
| **Checklist de entrega de fase DD** | Plane (Module: Checklist/Table view) | Estados, asignados, comentarios, historia |
| **Acta de reunión con cliente** | Obsidian (reuniones/) → MkDocs | Contexto, decisiones, links a issues Plane |
| **Modelo BIM central (Revit .rvt)** | `activos/bims/` + referencia en MkDocs/Plane | Fuera de git, ruta única |

---

## 6. Roadmap de Implementación (Fases)

### Fase 0: Esta semana (Decisión y Setup Wiki)
- [ ] Aprobar arquitectura "Wiki (MkDocs) + PM (Plane) + Knowledge (Obsidian)"
- [ ] Desplegar MkDocs en Netlify con Identity (ya documentado)
- [ ] Validar estructura `proyectos/<cliente>-<proyecto>/` en vault

### Fase 1: Semana 1-2 (Plane en VPS)
- [ ] Contratar VPS Hetzner CX22 (~$5/mes)
- [ ] Deploy Plane con docker-compose + nginx + Let's Encrypt
- [ ] Configurar DNS: `plane.estudio.ar` → VPS IP
- [ ] Crear workspace "Estudio", invitar 5 usuarios (Google OAuth)
- [ ] Definir **Issue Types** custom: `Entregable`, `RFI`, `Hito`, `Revisión`, `Certificación`
- [ ] Definir **Properties** custom por proyecto: `fase`, `area_m2`, `estado_legal`, `%_avance`
- [ ] Crear 1 proyecto piloto real (ej. `google-london-hq`)
- [ ] Importar tareas existentes desde Excel/CSV/Obsidian

### Fase 2: Semana 2-3 (Integración Wiki ↔ Plane)
- [ ] Añadir enlace "Ver en Plane" en cada `proyectos/<proyecto>/00-index.md` (MkDocs)
- [ ] Añadir Property `wiki_url` en Plane → botón "Ver especificación"
- [ ] Documentar convención de naming: `EST-123` = issue key Plane
- [ ] Configurar GitHub/GitLab integration en Plane (auto-link commits)

### Fase 3: Semana 3-4 (Operación y Dashboards)
- [ ] Crear **Cycles** de 2 semanas (sprints de documentación/entrega)
- [ ] Configurar **Modules**: Kanban por fase, Gantt por hito, Tabla por responsable
- [ ] Activar **Insights**: Burndown, Velocity, Cumulative Flow
- [ ] Definir **Saved Views** por rol:
  - Arquitecto: "Mis revisiones pendientes", "Hitos críticos próximos 14 días"
  - Dibujante: "Mis tareas esta semana", "Entregables vencidos"
  - BIM Manager: "Coordinaciones abiertas", "Choques pendientes"
- [ ] Entrenamiento 30 min al equipo (grabado)

### Fase 4: Continuo
- [ ] Revisión mensual: ¿Los dashboards sirven? ¿Faltan propiedades? ¿Ciclos muy largos/cortos?
- [ ] Automatizaciones: "Issue tipo RFI → notificar a arquitecto + cliente"
- [ ] Evaluar migración de docs internos de Plane a MkDocs (o viceversa) según uso real

---

## 7. Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Equipo no adopta Plane (usa solo WhatsApp/Email) | Alta | Alto | **Fase 1 obligatoria**: todo tracking en Plane. Cero tareas por WhatsApp. Liderazgo usa y exige. |
| VPS se cae / se pierde datos | Baja | Crítico | Backups diarios a Wasabi/S3 + test de restore mensual. Snapshots VPS semanales. |
| Plane consume mucha RAM en VPS 4GB | Media | Medio | Limitar `memory` en docker-compose. Monitorear con `htop` / Netdata. Upgrade a 8GB si needed ($9/mes). |
| Doble mantenimiento (MkDocs + Plane Docs) | Media | Medio | **Regla**: Docs técnicos/largos → MkDocs. Notas de proyecto/cortas → Plane Docs. Link cruzado. |
| Obsidian vault se desincroniza (Syncthing conflicts) | Media | Bajo | Git como source of truth. Syncthing solo para trabajo en curso. Commit diario obligatorio. |
| Plane Cloud se vuelve pago obligatorio | Baja | Medio | Self-hosted = control total. MIT license. Fork propio si proyecto muere. |

---

## 8. Conclusión y Recomendación Final

> **No intentes hacer dashboards en MkDocs/Obsidian Publish.** Es reinventar Jira mal, en HTML estático, sin multi-usuario real.

> **No intentes usar Obsidian como PM multi-usuario.** Es single-player con sync artesanal.

### Arquitectura ganadora (probada en estudios de 5-20 personas):

| Capa | Herramienta | Costo | Esfuerzo setup |
|------|-------------|-------|----------------|
| **Wiki pública/privada (conocimiento estático)** | **MkDocs Material + Netlify Identity** | $0 | 1 día |
| **Project Management (tareas, dashboards, ciclos, equipo)** | **Plane self-hosted en VPS Hetzner** | **~$5/mes** | 1 tarde |
| **Knowledge base personal/equipo técnico (notas, daily, zettel)** | **Obsidian + Syncthing/Git** | $0 | Ya lo tenés |
| **Binarios (planos, BIM, renders, PDFs)** | **`/activos/` (gitignored) + referencias** | $0 | Ya definido |

**Próximo paso accionable:** Aprobar gasto de **$5-7/mes (≈ $5.000-7.000 ARS)** para VPS Hetzner y agendar **mañana** el deploy de Plane. En 4 horas tenés PM real corriendo. En 2 días el equipo trabajando con dashboards.

---

## 9. Referencias y Enlaces Útiles

- **Plane**: https://plane.so | https://github.com/makeplane/plane
- **Plane Self-host Docs**: https://plane.so/self-hosted
- **Hetzner Cloud**: https://www.hetzner.com/cloud (CX22 = 4.50€/mes)
- **Wasabi Hot Storage**: https://wasabi.com (~$6.99/TB/mes, para backups)
- **MkDocs Material**: https://squidfunk.github.io/mkdocs-material/
- **Netlify Identity**: https://docs.netlify.com/visitor-access/identity/
- **Syncthing**: https://syncthing.net/ (sync vault entre equipo)
- **Obsidian Plane Plugin (community)**: https://github.com/plynr/obsidian-plane (experimental)