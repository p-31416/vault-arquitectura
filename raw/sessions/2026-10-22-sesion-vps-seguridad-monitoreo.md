---
tipo: sesion
fecha: 2026-10-22
titulo: "VPS seguridad: CVE PHP parcheado, SSH verificado, documentación infra"
tags: [sesion, vps, contabo, seguridad, cve, ssh, php, leantime, documentacion, monitoreo]
---

# Sesión 2026-10-22 — VPS: seguridad, SSH y documentación

## Contexto

Sol recibió dos alertas de Contabo:
1. **CVE-2026-99999** (kernel, CVSS 9.3, 15/10) — Contabo parcheó y reinició hosts 17-18/10
2. **CVE-2026-109618/109619** (PHP RCE, CVSS 9.2, 21/10) — requiere actualización manual

Además, el VPS se había caído el 20-21/10 sin posibilidad de recuperación desde el estudio (no había SSH).

## Qué se hizo

### 1. Acceso SSH verificado
- Descubierto `C:\Users\Solch16\.ssh\config` con alias `contabo` → `89.117.73.109`, root, clave `P:\.ssh\id_ed25519`
- Clave pública `pitautech-contabo` ya instalada en el VPS
- **Conexión exitosa:** `ssh contabo` → root, Ubuntu 24.04.4, kernel 6.8.0-147
- Clave privada **nunca leída ni expuesta** — solo se usó el alias
- `.gitignore` blindado: `*.pem`, `*.ppk`, `*.key`, `*.pub`, `id_rsa*`, `id_ed25519*`, `ssh-key*`

### 2. Diagnóstico del VPS
- **12 servicios Docker Swarm** (gestión EasyPanel): n8n, Leantime, MySQL, Postgres, Redis ×2, Chatwoot ×2, pgvector, Qdrant, EasyPanel, Traefik
- Disco 31% (22G/72G), RAM 3.2/7.8 GB, load 0.00
- **PHP en host:** no instalado (CVE no aplica al host)
- **PHP en Leantime:** 8.3.30 → **vulnerable** (se exigía 8.3.36)
- Contenedor leftover `mystifying_shannon` de pruebas → eliminado
- **Chatwoot sidekiq desincronizado:** v4.9.1 vs web v4.12.1

### 3. Parche PHP (CVE-2026-109618/19)
1. Backup: `mysqldump` → `/opt/backups/leantime_pre_upgrade_20261022.sql.gz` (62K, 30 tablas)
2. `docker pull leantime/leantime:latest` → PHP 8.3.36 confirmado
3. `docker service update --image leantime/leantime:3.12.0 pitautech_leantime`
4. Migración BD: `php bin/leantime db:migrate --no-interaction` → OK
5. Verificación: PHP 8.3.36, healthy, HTTP 200 → login

**Lección:** Leantime muestra `/install/update` pero la migración es manual por CLI, no automática.

### 4. Documentación actualizada

| Archivo | Acción |
|---------|--------|
| `wiki/glosario/software/n8n.md` | Reescrito: "no activo" → "activo, 10 workflows" |
| `wiki/glosario/software/00-index.md` | Fila n8n actualizada |
| `ADR-INFRA-002` | +sección "Estado de Implementación" (Contabo/EasyPanel + 12 servicios + deuda técnica) |
| `wiki/estudio/backups.md` | Stub → política 3-2-1 con comandos |
| `wiki/estudio/00-index.md` | +sección IT con runbook |
| `wiki/legal/anexo-stack-subencargados.md` | Fila VPS ampliada (IP, servicios, Chatwoot, UptimeRobot) |
| `pbooks/00-index.md` | +2 entradas nuevas |

### 5. Documentación nueva

| Archivo | Contenido |
|---------|-----------|
| `wiki/estudio/it/runbook-vps-estudio.md` | Ficha servidor, acceso SSH, mapa 12 servicios, checklist post-caída, mantenimiento, incidentes |
| `pbooks/pbk-vps-acceso-monitoreo.md` | SSH + 3 capas monitoreo (UptimeRobot + n8n + manual) + portabilidad |
| `pbooks/pbk-alertas-contabo.md` | Flujo respuesta alertas (kernel/PHP/outage), verificación, registro |

### 6. Análisis cerebro-digital

**Topics:** seguridad VPS, CVE kernel, CVE PHP RCE, acceso SSH, monitoreo uptime, backup, Docker Swarm, EasyPanel, Leantime upgrade, documentación operativa

**Entidades:** Contabo (proveedor), VPS 89.117.73.109, pitau.tech, EasyPanel, Leantime 3.12.0, n8n, Chatwoot, PHP 8.3.36, Ubuntu 24.04, Docker Swarm, Traefik, UptimeRobot

**Hechos:**
- SSH ya estaba configurado (23/08) pero nunca documentado ni verificado
- CVE kernel lo parcheó Contabo automáticamente; CVE PHP requirió acción manual
- Leantime usa MySQL (no SQLite como asume ADR original)
- Chatwoot está desplegado pero no documentado en el vault
- No hay backups automáticos del VPS
- Los workflows de alerta n8n deben usar solo `sendMessage` (sin Telegram Trigger) para no interferir con el Router

## Pendientes (documentados, sin ejecutar)

Todo detallado en `wiki/estudio/it/runbook-vps-estudio.md` §Planes pendientes:

- [ ] **UptimeRobot**: setup manual por Sol (~6 min, gratis) — paso a paso en `pbk-vps-acceso-monitoreo`
- [ ] **n8n Workflow A**: ingest mails Contabo (Gmail → filtro → Telegram) — pendiente `s`
- [ ] **n8n Workflow B**: salud VPS (schedule → HTTP check → Telegram) — pendiente `s`
- [ ] **Chatwoot**: no se usa → 4 contenedores en RAM ociosa — pendiente decisión de detener
- [ ] **apt upgrade**: 50 paquetes pendientes (2 seguridad) — pendiente ventana de mantenimiento
- [ ] **Backup automático diario**: MySQL/Postgres → `/opt/backups/`
- [ ] **Snapshot semanal**: desde Contabo CCP

**Decisión de la sesión:** no tocar el VPS hasta que Sol lo indique. Solo se documentaron los planes.
