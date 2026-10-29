---
tipo: oficina
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
tags: [runbook, vps, contabo, easypanel, ssh, infra, operaciones, incidentes]
---

# Runbook VPS del Estudio

> Guía operativa del VPS Contabo. Acceso, servicios, mantenimiento y recuperación. Volver a [[wiki/estudio/00-index|índice padre]].
>
> Playbooks relacionados: [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]] · [[wiki/glosario/interno/pbooks/pbk-alertas-contabo|pbk-alertas-contabo]]

## Ficha del servidor

| Dato | Valor |
|------|-------|
| Proveedor | **Contabo** (UE) — [my.contabo.com](https://my.contabo.com) |
| IP | **89.117.73.109** |
| Dominio | `pitau.tech` |
| Plan | VPS S — 4 vCPU, 8 GB RAM, ~72 GB SSD |
| SO | Ubuntu 24.04.4 LTS |
| Kernel | 6.8.0-147-generic |
| Orquestación | **EasyPanel** (Docker Swarm) |
| Reverse proxy | Traefik 3.6.7 + Let's Encrypt |
| Panel | `https://panel.pitau.tech` (cert autofirmado `CN=Easypanel`) |
| Status Contabo | [contabo-status.com](https://contabo-status.com/) |

## Acceso

### SSH (desde la PC local)

```bash
ssh contabo
```

| Dato | Valor |
|------|-------|
| Alias | `contabo` |
| Config | `C:\Users\Solch16\.ssh\config` |
| Clave privada | `P:\.ssh\id_ed25519` (fingerprint `SHA256:AY6xLTblk...`) |
| Usuario | `root` |
| Puerto | `22` |
| IP | `89.117.73.109` |

> **Seguridad:** la clave privada vive en `P:\.ssh\` — **fuera del vault y fuera de git**. El `.gitignore` excluye `*.pem`, `id_*`, `ssh-key*`.

### Paneles web

| Panel | URL | Uso |
|-------|-----|-----|
| Contabo CCP | `https://my.contabo.com` | Reinicio VPS, contraseñas, snapshots, facturación |
| EasyPanel | `https://panel.pitau.tech` | Gestión de servicios Docker, logs, updates |

## Mapa de servicios (12 servicios Swarm)

```
Traefik (80/443) ─── TLS + routing
├── n8n.pitau.tech ────────── pitautech_n8n (n8nio/n8n:latest)
├── panel.pitau.tech ──────── easypanel
├── *.easypanel.host ──────── pitautech_leantime (leantime:3.12.0)
│                             pitautech_chatwoot (chatwoot:v4.12.1)
└── Internos (sin exposición):
    ├── pitautech_leantime-db (mysql:9)
    ├── pitautech_postgres (postgres:17) — memoria agentes n8n
    ├── pitautech_redis (redis:7) — cola mensajes n8n
    ├── pitautech_chatwoot-sidekiq (chatwoot:v4.9.1) ⚠️ desincronizado
    ├── pitautech_chatwoot-db (pgvector/pgvector:pg17)
    ├── pitautech_chatwoot-redis (redis:7)
    ├── pitautech_qdrant (qdrant:v1.16)
    └── easypanel-traefik (traefik:3.6.7)
```

**Salud verificada 2026-10-22:** 12/12 servicios 1/1 · disco 31% · RAM 3.2/7.8 GB · load 0.00

## Comandos útiles

```bash
# Estado de servicios
ssh contabo "docker service ls"

# Estado de contenedores
ssh contabo "docker ps --format 'table {{.Names}}\t{{.Status}}'"

# Logs de un servicio
ssh contabo "docker service logs pitautech_n8n --tail 50"

# Reiniciar un servicio
ssh contabo "docker service update --force pitautech_leantime"

# Actualizar imagen de un servicio
ssh contabo "docker service update --image leantime/leantime:3.12.0 pitautech_leantime"

# Uso de disco y RAM
ssh contabo "df -h / && free -h"

# Paquetes pendientes
ssh contabo "apt list --upgradable 2>/dev/null | wc -l"
```

## Checklist post-caída

> Promovido de `log.md` (2026-10-20/21) — cuando el VPS cae y vuelve.

1. **¿VPS responde?** `ssh contabo "echo OK"` o `curl https://n8n.pitau.tech`
2. **¿n8n responde?** Abrir `https://n8n.pitau.tech` — verificar HTTP 200
3. **¿Workflows activos?** En n8n: los 4 principales deben estar `active` y con `versionId == activeVersionId`
4. **Mensaje de prueba al bot** — si no responde, desactivar y **volver a publicar** el Router (re-registra el webhook de Telegram)
5. **Leantime** — abrir `https://pitautech-leantime.3nq4ow.easypanel.host` — verificar login
6. **Contenedores** — `docker ps` debe mostrar todos `Up`
7. **Credenciales OAuth** — no se ven afectadas si la `encryptionKey` no cambió

## Mantenimiento programado

| Tarea | Frecuencia | Comando/Acción |
|-------|------------|----------------|
| Verificar servicios | Semanal | `docker service ls` — todo 1/1 |
| Updates del host | Mensual | `apt update && apt upgrade -y` + reboot en ventana |
| Update Leantime | Cuando haya release + CVE | Verificar Docker Hub → `docker service update --image` |
| Update n8n | Mensual | EasyPanel → update image |
| Backup MySQL/Postgres | **Diario (objetivo)** | Ver [[wiki/estudio/backups]] |
| Snapshot VPS | Semanal | Desde Contabo CCP |
| Test restore | Mensual | Verificar que los dumps se pueden importar |
| Revisar alertas Contabo | Cuando lleguen mail | Ver [[wiki/glosario/interno/pbooks/pbk-alertas-contabo]] |

## Incidentes conocidos

| Fecha | Incidente | Resolución |
|-------|-----------|------------|
| 2026-10-17/18 | Contabo parcheó kernel CVE-2026-99999 → reboot del host | Automático del proveedor |
| 2026-10-20/21 | VPS caído ~18h (TCP 443+22 sin respuesta) | Volvió solo; verificación checklist post-caída |
| 2026-10-21 | CVE-2026-109618/19 (PHP RCE, CVSS 9.2) | Leantime 3.7.3→3.12.0, PHP 8.3.30→8.3.36 (22/10) |

## Planes pendientes (documentados, sin ejecutar)

> Registrados 2026-10-22. Ejecutar cuando Sol lo indique.

### 1. UptimeRobot — monitoreo externo (alta prioridad)

Setup manual por Sol (~6 min, gratis). Paso a paso completo en [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]] §Monitoreo → Capa 1.

Resumen: crear cuenta → monitor HTTPS `https://n8n.pitau.tech` cada 5 min → alerta Telegram chat personal. **Cubre el caso "host caído" que el 20/10 no se detectó a tiempo.**

### 2. n8n workflows de alerta (media prioridad)

Pendientes de crear en n8n (requiere `s` explícito):

| Workflow | Trigger | Función |
|----------|---------|---------|
| **Ingest Contabo** | Gmail OAuth2 (ya configurado) | Filtra mails Contabo → Telegram a Sol + log Sheets |
| **Salud VPS** | Schedule cada 5 min | HTTP check n8n + Leantime → Telegram a Sol si falla |

**Regla:** ambos usan solo `Telegram sendMessage` (output), **sin Telegram Trigger** → cero conflicto con el Router.

### 3. Chatwoot — no se usa (baja prioridad)

4 contenedores desplegados (web v4.12.1, sidekiq v4.9.1 ⚠️ desincronizado, db, redis) consumiendo RAM sin uso. **Opción:** detener servicios para liberar recursos:
```bash
docker service scale pitautech_chatwoot=0 pitautech_chatwoot-sidekiq=0 pitautech_chatwoot-db=0 pitautech_chatwoot-redis=0
```
Reversible: `=1` para levantar de nuevo. **Pendiente de decisión de Sol.**

### 4. apt upgrade (baja prioridad)

50 paquetes pendientes (2 de seguridad). Requiere reboot (~1-2 min caída). **No urgente.** Ejecutar en ventana de mantenimiento:
```bash
ssh contabo "apt update && apt upgrade -y && reboot"
```
Verificar servicios post-reboot con el checklist de arriba.

### 5. Backup automático diario (media prioridad)

Ver [[wiki/estudio/backups]]. Objetivo: cron en VPS que haga `mysqldump` + `pg_dump` diario a `/opt/backups/`.

### 6. Snapshot semanal Contabo (baja prioridad)

Desde `my.contabo.com` → VPS → Snapshots. Configurar manual o verificar si Contabo lo ofrece automático.

## Referencias

- Contabo Status: https://contabo-status.com/
- EasyPanel Docs: https://easypanel.io/docs
- ADR: [[wiki/estudio/adrs/ADR-INFRA-002-vps-dedicado-estudio|ADR-INFRA-002 VPS Dedicado]]
- Backups: [[wiki/estudio/backups|Política de backups]]
