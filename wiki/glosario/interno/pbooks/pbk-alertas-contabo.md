---
tipo: metodologia
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
tags: [playbook, contabo, seguridad, cve, php, kernel, alertas, incidentes, vps]
idioma: es
---

# pbk-alertas-contabo — Respuesta a alertas de seguridad de Contabo

> **Canónico**: qué hacer cuando llega un mail de alerta de seguridad de Contabo al VPS.
> Correo destino: Gmail (filtro automático → Telegram vía n8n).
> Runbook del VPS: [[wiki/estudio/it/runbook-vps-estudio|runbook-vps-estudio]]

## Flujo de respuesta

```
Llega mail de Contabo
    ↓
Se clasifica (ver tipos abajo)
    ↓
Se verifica el estado real del VPS por SSH
    ↓
Se aplica el fix correspondiente
    ↓
Se verifica que el fix funcionó
    ↓
Se registra en log.md
```

## Tipos de alerta

### 1. CVE de kernel (el proveedor lo parchea)

**Ejemplo:** CVE-2026-99999 (CVSS 9.3, 2026-10-15) — Contabo parcheó y reinició hosts el 17-18/10.

| Qué hace Contabo | Qué hacer de tu lado |
|------------------|---------------------|
| Parchea el kernel | Verificar: `ssh contabo "uname -r"` |
| Reinicia el host | Checklist post-caída (runbook) |
| Los servicios arrancan solos | Verificar servicios: `docker service ls` |

**Verificación:**
```bash
ssh contabo "uname -r"     # kernel actual
ssh contabo "uptime"       # cuándo arrancó
ssh contabo "docker service ls"  # todo 1/1
```

**No requiere acción del usuario** más allá de verificar que todo volvió.

### 2. CVE de aplicación (el usuario debe actualizar)

**Ejemplo:** CVE-2026-109618/109619 (PHP RCE, CVSS 9.2, 2026-10-21) — Contabo **no puede** parchearlo, pide actualización manual.

**Caso Leantime/PHP (resuelto 2026-10-22):**

| Paso | Comando/Acción | Estado |
|------|---------------|--------|
| 1. Backup | `mysqldump` + gzip a `/opt/backups/` | ✅ Hecho |
| 2. Verificar versión vulnerable | `docker exec <cont> php -v` | 8.3.30 🔴 |
| 3. Buscar imagen nueva | `docker pull leantime/leantime:latest` → verificar PHP | 8.3.36 ✅ |
| 4. Actualizar | `docker service update --image leantime/leantime:3.12.0 pitautech_leantime` | ✅ Hecho |
| 5. Migrar BD | `docker exec <cont> php bin/leantime db:migrate --no-interaction` | ✅ Hecho |
| 6. Verificar | `php -v` + HTTP 200 + contenedor healthy | ✅ Hecho |

> **Lección:** Leantime muestra `/install/update` al detectar cambio de versión → la migración de BD es manual por CLI, no automática.

### 3. Outage / caída del host

**Síntomas:** SSH no responde, web no responde, UptimeRobot alerta.

**Acción:**
1. Revisar [contabo-status.com](https://contabo-status.com/) — ¿hay incidente anunciado?
2. Si el status dice "rolled out" y el VPS no arranca → Contabo CCP → verificar estado del servidor
3. Si vuelve → checklist post-caída (runbook)

### 4. Mantenimiento programado

Contabo anuncia ventanas de mantenimiento. Acción: revisar qué servicios se ven afectados, planificar backup previo si hay reboot.

## Categorías de correos Contabo

| Remitente/Asunto | Tipo | Urgencia |
|-----------------|------|----------|
| "critical Linux kernel vulnerability" | Kernel (ellos parchean) | Baja — verificar post-reboot |
| "PHP project released fixes" / "CVE" | Aplicación (vos parcheás) | **Alta** — hacerlo hoy |
| "maintenance" | Mantenimiento | Media — planificar |
| "outage" / "incident" | Caída | Alta — verificar servicios |

## Verificación post-fix

```bash
# Todo en uno
ssh contabo "docker service ls && docker ps --format '{{.Names}} {{.Status}}' && uptime"

# PHP específico
ssh contabo "docker exec \$(docker ps --filter name=leantime --format '{{.Names}}' | head -1) php -v"

# HTTP
curl -s -o /dev/null -w "%{http_code}" https://n8n.pitau.tech
curl -s -o /dev/null -w "%{http_code}" https://pitautech-leantime.3nq4ow.easypanel.host
```

## Registro

**Siempre** registrar en `log.md`:
- Fecha del incidente/alerta
- Qué se detectó
- Qué se hizo
- Resultado de la verificación

## Referencias

- Contabo Status: https://contabo-status.com/
- Contabo Support: https://contabo.com/en/customer-support/
- PHP Security Advisories: https://www.php.net/ChangeLog-8.php (verificado 2026-10-22)
- Ubuntu CVE: https://ubuntu.com/security/cves (verificado 2026-10-22)
- Runbook: [[wiki/estudio/it/runbook-vps-estudio]]
- Monitoreo: [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]]
