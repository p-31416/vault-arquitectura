---
tipo: adr
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [adr, infra, pm, leantime, self-hosted, gantt, sprints, docker]
estado: propuesto
categoria: infra
numero: 001
---

# ADR-INFRA-001: Leantime Self-Hosted para Project Management con Gantt y Sprints

## Contexto

El estudio necesita **gestión de proyectos real** (tareas, Kanban, Gantt, Sprints/Cycles, dashboards de avance, asignaciones, notificaciones) para equipo de 4-5 personas (arquitectos, dibujantes, BIM managers).

**Restricciones duras:**
- **Costo: $0/mes** (sin VPS pagado, sin SaaS per-seat)
- **Infra actual**: GitHub (repo vault), Netlify (wiki MkDocs), PCs oficina
- **Hardware disponible**: 1 PC/NAS en oficina encendido 24/7 (o horario extendido)
- **Acceso remoto**: Equipo distribuido en Argentina (casa, obra, oficina)

**Alternativas evaluadas y descartadas:**
| Opción | Por qué no |
|--------|------------|
| Plane (self-hosted VPS) | Requiere VPS ~$5/mes (Hetzner) → viola restricción $0 |
| Plane Cloud Free | Límite 10 users, datos en EE.UU., futuro incierto, no self-hosted |
| GitHub Projects v2 | **Bueno para Kanban/Roadmap/Tabla** pero **NO tiene Gantt real ni Sprints con burndown automático** |
| GitLab | Repo en GitHub, migración coste alto |
| Notion/ClickUp/Height Free | Límites de bloques/vistas/storage → insostenible para arquitectura |
| Wekan/Kanboard/Focalboard | Solo Kanban, sin Gantt ni Sprints |
| Oracle Cloud Free Tier | Riesgo de baneo arbitrario, no confiable para producción |

## Decisión

**Adoptar [Leantime](https://github.com/Leantime/leantime) self-hosted en hardware propio (PC oficina / NAS)** como herramienta de Project Management principal, complementando a GitHub Projects (para issues ligeros) y MkDocs (para wiki estática).

**Configuración objetivo:**
- Docker Compose en PC/NAS oficina (Linux/Windows/WSL2)
- Base de datos **SQLite** (zero config, backup simple, suficiente para <20 users)
- Puerto 8080 expuesto en LAN
- Acceso remoto via **Tailscale** (gratis, 100 devices, WireGuard) o **Cloudflare Tunnel** (gratis, HTTPS, auth opcional)
- Backups diarios automáticos a Google Drive / OneDrive / GitHub (repo privado backups) via `rclone`

## Alternativas Consideradas

| Alternativa | Pros | Contras | Por qué no |
|-------------|------|---------|------------|
| **Plane en Oracle Free Tier** | Plane real, gratis | Riesgo baneo, ARM64 (compatibilidad), latencia EE.UU. | No confiable para producción |
| **GitHub Projects + Sheets** | Zero infra, ya tenés auth | Sin Gantt, sin Sprints, burndown manual | Gap funcional crítico para arquitectura |
| **Leantime en Raspberry Pi 4** | Hardware dedicado $50-80 | Compra inicial, mantenimiento HW | PC oficina ya existe, aprovechar |
| **Taiga self-hosted** | Open source, Kanban+Sprints | **Gantt solo en paid**, más pesado (Python+Postgres) | Leantime tiene Gantt gratis |
| **OpenProject self-hosted** | Completo, Gantt, Sprints | Muy pesado (Java/Postgres), curva alta | Overkill para 5 personas |

## Consecuencias

### Positivas
- **Gantt nativo** con dependencias, hitos, línea base, ruta crítica
- **Sprints/Cycles** con planning, review, retro, burndown automático
- **Kanban + Lista + Tabla + Calendar** vistas intercambiables
- **Wiki/Docs integrada** (Markdown) para notas de proyecto rápidas
- **Campos custom** por proyecto: `fase`, `area_m2`, `estado_legal`, `%_avance`, `responsable`
- **Auth**: Email/password, LDAP, OAuth2 (Google, GitHub, GitLab, Azure) → SSO con cuentas del estudio
- **Ligero**: PHP 8.2 + SQLite → corre en 512MB RAM, CPU baja
- **API REST** (básica) + Webhooks para integraciones futuras
- **MIT License** → control total, sin vendor lock-in
- **Backup simple**: un archivo `.sqlite` + carpeta `storage/`

### Negativas / Riesgos / Deuda Técnica
- **Hardware SPOF**: Si PC oficina se apaga/falla → Leantime inaccesible
  - *Mitigación*: Backups diarios off-site; documentar procedimiento de restore en <30 min en otro PC
- **No es "Plane"**: UX diferente, menos pulido, menos integraciones nativas (GitHub, Slack)
  - *Mitigación*: Evaluar migración a Plane self-hosted si presupuesto aparece
- **Mobile**: Solo responsive web (no PWA nativa con offline)
  - *Mitigación*: Tailscale/Cloudflare Tunnel dan acceso web móvil usable
- **Automatizaciones limitadas**: Sin motor de reglas nativo tipo "Si X entonces Y"
  - *Mitigación*: Webhooks + n8n/GitHub Actions para flujos críticos
- **Mantenimiento**: Updates manuales (docker pull + restart), parches seguridad PHP
  - *Mitigación*: Suscribirse a releases GitHub; ventana mensual de mantenimiento

### Trabajo Futuro / Seguimiento
- [ ] Deploy en PC oficina (Docker Compose + SQLite)
- [ ] Configurar Tailscale / Cloudflare Tunnel para acceso remoto
- [ ] Crear workspace "Estudio", invitar 5 usuarios (OAuth Google)
- [ ] Definir Issue Types custom: `Entregable`, `RFI`, `Hito`, `Revisión`, `Certificación`, `Coordinación`
- [ ] Definir Properties custom: `fase`, `area_m2`, `estado_legal`, `%_avance`, `prioridad`
- [ ] Importar issues existentes desde GitHub Projects / CSV
- [ ] Configurar backup diario automático (script + rclone)
- [ ] Documentar runbook: restore, update, troubleshooting
- [ ] Evaluar a los 3 meses: ¿Cubre necesidades? ¿Migrar a Plane si hay presupuesto?

## Referencias

- Repo: https://github.com/Leantime/leantime
- Demo: https://demo.leantime.io (login: demo@leantime.io / demo)
- Docs self-host: https://leantime.github.io/leantime/docs/installation/docker
- Docker Hub: https://hub.docker.com/r/leantime/leantime
- ADR relacionado: [ADR-TOOL-001](../ADR-TOOL-001-mkdocs-netlify-wiki.md) (Wiki MkDocs + Netlify)
- Análisis completo: [[analisis-dashboards-pm-gratis]]