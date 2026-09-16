---
tipo: adr
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [adr, infra, vps, dedicated, isolation, studio, leantime, mkdocs, nginx]
estado: aceptado
categoria: infra
numero: 002
---

# ADR-INFRA-002: VPS Dedicado para el Estudio (Aislamiento Total)

## Contexto

El estudio maneja **datos sensibles de clientes**: contratos, legales, planos, certificaciones, finanzas, modelos BIM. Proyectos con terceros (ej. sociedad con Lidia) requieren **aislamiento estricto de datos, accesos y responsabilidades**.

**Decisión previa:** ADR-INFRA-001 adoptó Leantime self-hosted para PM con Gantt/Sprints.
**Decisión previa:** ADR-TOOL-001 adoptó MkDocs + Netlify para wiki estática pública/privada.

**Nueva restricción:** Separación física y lógica entre infraestructura del estudio y proyectos externos/colaboraciones.

## Decisión

**Contratar un VPS dedicado exclusivamente para el estudio** (Hetzner CX22 o superior) que hospede:

| Servicio | Dominio | Propósito |
|----------|---------|-----------|
| **Leantime** | `pm.estudio.ar` | Project Management real (Gantt, Sprints, Kanban, Wiki interna) |
| **MkDocs (mirror local / staging)** | `wiki-internal.estudio.ar` | Wiki privada con auth, preview de PRs, backup local |
| **Nginx/Caddy Reverse Proxy** | `*.estudio.ar` | TLS automático (Let's Encrypt), routing, security headers |
| **Backups automatizados** | — | rclone → Wasabi/Google Drive/OneDrive (off-site daily) |
| **Monitoring** | `monitor.estudio.ar` | Netdata / Uptime Kuma (opcional) |

**Proyectos externos (Lidia, colaboraciones)** → **infraestructura separada** (SaaS free hoy, VPS propio mañana si exige).

## Alternativas Consideradas

| Alternativa | Pros | Contras | Por qué no |
|-------------|------|---------|------------|
| **1 VPS compartido (multi-tenant Docker)** | $5/mes total | **Riesgo fuga datos**, configs compartidas, un fallo afecta todo, backups mezclados | Viola principio aislamiento cliente |
| **Leantime multi-workspace en 1 VPS** | Una app, menos mantenimiento | Workspaces no son aislamiento real (misma BD, misma app, mismo usuario root) | Cliente auditoría rechaza |
| **VPS dedicado por proyecto** | Aislamiento total | $5-10/mes por proyecto, gestión múltiple | Overkill para colaboraciones puntuales |
| **SaaS para todo (Plane Cloud, Leantime Cloud)** | Zero ops | Datos en EE.UU., límites users, vendor lock-in, $8-15/user/mes | No cumple confidencialidad ni presupuesto |

## Consecuencias

### Positivas
- **Aislamiento total**: Datos del estudio nunca tocan infra de terceros
- **Cumplimiento**: Cliente puede auditar VPS del estudio sin ver nada de Lidia
- **Control total**: SSH, Docker, backups, monitoring, DNS, firewall → todo del estudio
- **Escalabilidad**: Si crece el equipo → upgrade a CPX21 (8GB RAM) en 1 click
- **Costo predecible**: ~$5-12/mes (Hetzner) + ~$7/mes (Wasabi 1TB backups) = **<$20/mes total**
- **Backup soberano**: rclone a Wasabi (S3 compatible, EU/US, $6.99/TB) o Google Drive (gratis 15GB)
- **Disaster recovery documentado**: Restore Leantime + Wiki en <30 min en VPS nuevo

### Negativas / Riesgos / Deuda Técnica
- **Un VPS = SPOF** (Single Point of Failure)
  - *Mitigación*: Backups diarios off-site + runbook restore probado mensualmente
- **Mantenimiento propio**: Updates OS, Docker, Leantime, Nginx, certs
  - *Mitigación*: Ventana mensual 1ra semana; `unattended-upgrades` security; watchtower para containers
- **Costo fijo mensual** (aunque bajo)
  - *Mitigación*: $5-12/mes es <1 hora honorario arquitecto; ROI inmediato
- **Conocimiento sysadmin básico requerido**
  - *Mitigación*: Documentación en wiki (runbooks); 1 persona del equipo "tech lead" infra

## Configuración Objetivo (VPS Estudio)

### Hardware recomendado
| Proveedor | Plan | Specs | Costo estimado ARS (jul 2026) |
|-----------|------|-------|-------------------------------|
| **Hetzner** | **CX22** | 2 vCPU, 4GB RAM, 40GB SSD, 20TB traffic | **~$5.000** |
| Hetzner | CPX21 | 3 vCPU, 8GB RAM, 80GB SSD, 20TB traffic | ~$12.000 |
| DigitalOcean | Basic 2GB | 1 vCPU, 2GB RAM, 50GB SSD | ~$12.000 (USD) |
| Contabo | VPS S | 4 vCPU, 8GB RAM, 200GB SSD | ~$6.000 |

> **Recomendación:** **Hetzner CX22** (€4.50/mes). Mejor red, CPU dedicated, SSD NVMe, factura en EUR (estable), API/Console excelente.

### Docker Compose Stack (archivo único en `/opt/estudio/docker-compose.yml`)

```yaml
version: '3.8'

services:
  # --- REVERSE PROXY + TLS ---
  caddy:
    image: caddy:2-alpine
    container_name: estudio-caddy
    ports:
      - "80:80"
      - "443:443"
      - "443:443/udp"
    volumes:
      - ./caddy/Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
      - caddy_config:/config
    networks:
      - estudio_frontend
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true

  # --- LEANTIME (PM Principal) ---
  leantime:
    image: leantime/leantime:latest
    container_name: estudio-leantime
    environment:
      - APP_URL=https://pm.estudio.ar
      - DB_CONNECTION=sqlite
      - APP_KEY_FILE=/run/secrets/leantime_app_key
      - SESSION_DRIVER=database
      - CACHE_DRIVER=database
      - QUEUE_CONNECTION=database
    volumes:
      - leantime_data:/var/www/html/storage
    networks:
      - estudio_backend
    secrets:
      - leantime_app_key
    depends_on:
      - caddy
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 1G
        reservations:
          memory: 512M

  # --- MKDOCS MIRROR / STAGING (Opcional) ---
  wiki-mirror:
    image: python:3.11-alpine
    container_name: estudio-wiki-mirror
    working_dir: /wiki
    command: >
      sh -c "pip install -q mkdocs mkdocs-material mkdocs-mermaid2-plugin
             mkdocs-git-revision-date-localized-plugin mkdocs-print-site-plugin
             mkdocs-wikilinks-plugin mkdocs-minify-plugin &&
             mkdocs build --clean --strict"
    volumes:
      - ./wiki-source:/wiki:ro
      - wiki_mirror_output:/wiki/site
    networks:
      - estudio_backend
    profiles:
      - mirror
    restart: "no"

  # --- BACKUP SERVICE ---
  backup:
    image: alpine:3.20
    container_name: estudio-backup
    command: >
      sh -c "apk add --no-cache rclone sqlite postgresql-client &&
             echo '0 2 * * * /backup.sh' | crontab - &&
             crond -f"
    volumes:
      - ./backup:/backup:ro
      - leantime_data:/source/leantime:ro
      - wiki_mirror_output:/source/wiki:ro
      - backup_logs:/var/log/backup
    environment:
      - RCLONE_CONFIG=/backup/rclone.conf
    networks:
      - estudio_backend
    restart: unless-stopped
    profiles:
      - backup

  # --- MONITORING (Opcional) ---
  netdata:
    image: netdata/netdata:stable
    container_name: estudio-netdata
    ports:
      - "19999:19999"
    volumes:
      - netdata_lib:/var/lib/netdata
      - netdata_cache:/var/cache/netdata
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro
    environment:
      - NETDATA_CLAIM_TOKEN=${NETDATA_CLAIM_TOKEN}
      - NETDATA_CLAIM_URL=https://app.netdata.cloud
    networks:
      - estudio_monitoring
    restart: unless-stopped
    profiles:
      - monitoring
    cap_add:
      - SYS_PTRACE
    security_opt:
      - apparmor:unconfined

networks:
  estudio_frontend:
    name: estudio_frontend
  estudio_backend:
    name: estudio_backend
    internal: true
  estudio_monitoring:
    name: estudio_monitoring
    internal: true

volumes:
  leantime_data:
    name: estudio_leantime_data
  wiki_mirror_output:
    name: estudio_wiki_mirror
  caddy_data:
    name: estudio_caddy_data
  caddy_config:
    name: estudio_caddy_config
  netdata_lib:
    name: estudio_netdata_lib
  netdata_cache:
    name: estudio_netdata_cache
  backup_logs:
    name: estudio_backup_logs

secrets:
  leantime_app_key:
    file: ./secrets/leantime_app_key.txt
```

### Caddyfile (`/opt/estudio/caddy/Caddyfile`)

```caddyfile
{
    admin off
    email admin@estudio.ar
}

pm.estudio.ar {
    reverse_proxy estudio-leantime:80
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "SAMEORIGIN"
        Referrer-Policy "strict-origin-when-cross-origin"
    }
}

wiki-internal.estudio.ar {
    root * /wiki/site
    file_server
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
        X-Content-Type-Options "nosniff"
        X-Frame-Options "SAMEORIGIN"
    }
}

monitor.estudio.ar {
    basicauth {
        admin ${MONITOR_PASSWORD_HASH}
    }
    reverse_proxy estudio-netdata:19999
}
```

### Backup Script (`/opt/estudio/backup/backup.sh`)

```bash
#!/bin/sh
set -eu

DATE=$(date +%F_%H-%M)
DEST="wasabi:estudio-backups/${DATE}"

echo "[$(date)] Iniciando backup..."

# 1. Leantime SQLite + storage
sqlite3 /source/leantime/database.sqlite ".backup /tmp/leantime_${DATE}.sqlite"
tar -czf /tmp/leantime_storage_${DATE}.tar.gz -C /source/leantime storage/

# 2. Wiki mirror (si existe)
if [ -d /source/wiki ]; then
    tar -czf /tmp/wiki_${DATE}.tar.gz -C /source/wiki .
fi

# 3. Subir a Wasabi (S3 compatible)
rclone copy /tmp/leantime_${DATE}.sqlite "${DEST}/leantime/" --progress
rclone copy /tmp/leantime_storage_${DATE}.tar.gz "${DEST}/leantime/" --progress
[ -f /tmp/wiki_${DATE}.tar.gz ] && rclone copy /tmp/wiki_${DATE}.tar.gz "${DEST}/wiki/" --progress

# 4. Limpiar temporales
rm -f /tmp/leantime_${DATE}.sqlite /tmp/leantime_storage_${DATE}.tar.gz /tmp/wiki_${DATE}.tar.gz

# 5. Retención: borrar backups > 30 días en Wasabi
rclone delete "wasabi:estudio-backups" --min-age 30d --rmdirs

echo "[$(date)] Backup completado."
```

### Secrets (generar una vez)

```bash
# En /opt/estudio/secrets/
openssl rand -base64 32 > leantime_app_key.txt
chmod 600 leantime_app_key.txt

# Para monitor basicauth (Caddy)
# caddy hash-password --plaintext 'tu-password-seguro'
# pegar hash en .env como MONITOR_PASSWORD_HASH
```

---

## Runbook Operativo (Resumen)

| Tarea | Frecuencia | Comando / Acción |
|-------|------------|------------------|
| **Deploy inicial** | Una vez | `cd /opt/estudio && docker compose up -d` |
| **Update Leantime** | Mensual | `docker compose pull leantime && docker compose up -d leantime` |
| **Update Caddy** | Mensual | `docker compose pull caddy && docker compose up -d caddy` |
| **Update OS** | Mensual | `apt update && apt upgrade -y && reboot` (ventana mantenimiento) |
| **Backup verify** | Semanal | Revisar logs `/var/log/backup/` + test download 1 archivo Wasabi |
| **Restore test** | Mensual | `docker run --rm -v estudio_leantime_data:/data alpine sh -c "sqlite3 /data/database.sqlite .dump" | head -20` |
| **Certificados TLS** | Automático | Caddy renueva solo (Let's Encrypt) |
| **Escalado RAM** | Si >80% uso | Upgrade Hetzner CX22→CPX21 (reboot 2 min) |

---

## Costos Mensuales Estimados (ARS, Julio 2026)

| Ítem | Proveedor | Costo USD | Costo ARS (aprox) |
|------|-----------|-----------|-------------------|
| **VPS CX22** | Hetzner | €4.50 | **$5.000** |
| **Backups 500GB** | Wasabi Hot Storage | $3.50 | **$3.500** |
| **Dominio .ar** | NIC.ar / registrador | $0.15/mes | **$150** |
| **Monitoring (Netdata Cloud)** | Netdata | Free (10 nodes) | $0 |
| **Total** | | **~$8.15** | **~$8.650** |

> **Comparación:** 1 hora honorario arquitecto senior ≈ $15.000-25.000 ARS.  
> **ROI:** El VPS se paga solo con **evitar 30 min de problemas de sincronización / pérdida de datos / auditoría fallida**.

---

## Próximos Pasos (Esta Semana)

- [ ] Contratar VPS Hetzner CX22 (Ubuntu 24.04, SSH key, región Nuremberg/Falkenstein)
- [ ] Configurar DNS: `pm.estudio.ar`, `wiki-internal.estudio.ar`, `monitor.estudio.ar` → IP VPS
- [ ] Clonar repo `vault-arquitectura` en VPS → `/opt/estudio/wiki-source`
- [ ] Crear estructura `/opt/estudio/` con `docker-compose.yml`, `caddy/`, `backup/`, `secrets/`
- [ ] Generar secrets (`leantime_app_key`, `MONITOR_PASSWORD_HASH`)
- [ ] Configurar rclone → Wasabi (bucket `estudio-backups`)
- [ ] `docker compose up -d` → verificar HTTPS + login Leantime
- [ ] Invitar 5 usuarios del equipo a Leantime (OAuth Google)
- [ ] Configurar GitHub Projects ↔ Leantime sync (issues ↔ work items) via webhook/Action
- [ ] Documentar runbook en `wiki/estudio/it/runbook-vps-estudio.md`
- [ ] Programar test de restore mensual en calendario del equipo

---

## Referencias

- ADR relacionado: [ADR-INFRA-001 Leantime Self-Hosted](../ADR-INFRA-001-leantime-selfhosted.md) (decide Leantime como PM)
- ADR relacionado: [ADR-TOOL-001 MkDocs + Netlify](../ADR-TOOL-001-mkdocs-netlify-wiki.md) (wiki pública en Netlify, mirror privado aquí)
- Hetzner Cloud: https://www.hetzner.com/cloud
- Caddy Docs: https://caddyserver.com/docs/
- Leantime Docker: https://hub.docker.com/r/leantime/leantime
- Wasabi: https://wasabi.com/pricing/
- rclone: https://rclone.org/
- Netdata: https://www.netdata.cloud/