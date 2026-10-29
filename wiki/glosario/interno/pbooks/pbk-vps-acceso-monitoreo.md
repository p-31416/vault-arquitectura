---
tipo: metodologia
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
tags: [playbook, vps, ssh, contabo, monitoreo, uptime, alertas, easypanel]
idioma: es
---

# pbk-vps-acceso-monitoreo — Acceso SSH y monitoreo del VPS

> **Canónico**: cómo conectarse al VPS, qué monitorea, y cómo llegan las alertas.
> Runbook operativo: [[wiki/estudio/it/runbook-vps-estudio|runbook-vps-estudio]]
> Alertas de seguridad: [[wiki/glosario/interno/pbooks/pbk-alertas-contabo|pbk-alertas-contabo]]

## Acceso SSH

### Configuración (ya activa en la PC local)

Archivo `C:\Users\Solch16\.ssh\config`:

```
Host contabo
    HostName 89.117.73.109
    User root
    IdentityFile P:/.ssh/id_ed25519
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

**Conectar:** `ssh contabo`

| Elemento | Ubicación | Nota de seguridad |
|----------|-----------|-------------------|
| Clave privada | `P:\.ssh\id_ed25519` | **Fuera del vault y git** — nunca compartir |
| Clave pública | `P:\.ssh\id_ed25519.pub` | Instalada en el VPS (nombre `pitautech-contabo`) |
| Fingerprint | `SHA256:AY6xLTblklI55sbAXc3eJ7e7fZZWdMCCcc12mW0fEA8` | Verificar al reconectar |

### Comandos de verificación rápida

```bash
ssh contabo "echo OK"                          # ¿responde?
ssh contabo "docker service ls"                # servicios
ssh contabo "uptime"                           # carga
ssh contabo "df -h / && free -h"              # disco y RAM
```

### Si la clave no funciona

1. Verificar que el archivo existe: `dir P:\.ssh\`
2. Verificar permisos (Windows): la clave debe ser solo lectura para el usuario
3. Reconectar con verbose: `ssh -v contabo`
4. Como último recurso: contraseña desde Contabo CCP → `my.contabo.com` → VPS → Access Data → `ssh root@89.117.73.109`

## Monitoreo — 3 capas

### Capa 1 — UptimeRobot (externo, cubre host caído)

| Dato | Valor |
|------|-------|
| Servicio | [uptimerobot.com](https://uptimerobot.com) — gratis |
| Monitorea | `https://n8n.pitau.tech` cada 5 min |
| Alerta | Telegram + email |
| **Por qué es clave** | Corre **fuera** del VPS → funciona aunque el VPS esté muerto |

**Setup (paso a paso, ~6 min, gratis):**

1. Ir a `https://uptimerobot.com` → **Register** (sin tarjeta) → verificar casilla
2. Dashboard → **Add New Monitor**:
   - Monitor Type: `HTTPS(s)`
   - Friendly Name: `VPS pitau.tech`
   - URL: `https://n8n.pitau.tech`
   - Monitoring Interval: `5 minutes`
   - **Create Monitor**
3. Dashboard → **Alert Contacts** → **Add Alert Contact** → Type: `Telegram` → seguir guía de autorización → elegir **chat personal** (no grupo)
4. Verificar: llega mensaje de prueba → monitor verde ✅

**Qué cubre:**

| Escenario | ¿Alerta? |
|-----------|----------|
| VPS Contabo caído | ✅ (caso 20/10) |
| n8n no responde | ✅ |
| Leantime caído solo | ⚠️ solo si también cae n8n |
| Servicio interno caído | ❌ (lo cubre workflow n8n, pendiente) |

### Capa 2 — n8n Workflow "Salud VPS" (interno, cubre apps caídas)

| Dato | Valor |
|------|-------|
| Corre en | El propio VPS (n8n) |
| Frecuencia | Cada 5 minutos |
| Chequea | HTTP de n8n + Leantime |
| Alerta | Telegram → chat de Sol |

**Limitación:** si el host cae, este workflow también cae → por eso existe la Capa 1.

### Capa 3 — Revisión manual

```bash
# Semanal
ssh contabo "docker service ls"    # todo 1/1
ssh contabo "docker ps"            # nada en Restart
```

## Recibir alertas

| Alerta | Canal | Quién recibe |
|--------|-------|-------------|
| VPS/hostname caído | UptimeRobot → Telegram | Sol (privado) |
| App (n8n/Leantime) no responde | n8n workflow → Telegram | Sol (privado) |
| Mail de seguridad Contabo | n8n workflow Gmail → Telegram | Sol (privado) |

> **Regla:** todos los workflows de alerta usan solo `Telegram sendMessage` (output) — **nunca `Telegram Trigger`** (input) — para no robarle el webhook al Router existente.

## Portabilidad

Para replicar en otro VPS/usuario:

1. **SSH:** generar clave nueva (`ssh-keygen -t ed25519`), instalar en el VPS nuevo, crear `Host` en `~/.ssh/config`
2. **UptimeRobot:** cambiar URL del monitor
3. **n8n workflow salud:** cambiar URLs en el Set/HTTP Request
4. **n8n workflow Contabo:** cambiar credencial Gmail + chat_id de destino
5. **Telegram:** cada usuario su propio `chat_id` personal

## Referencias

- Runbook: [[wiki/estudio/it/runbook-vps-estudio]]
- Alertas Contabo: [[wiki/glosario/interno/pbooks/pbk-alertas-contabo|pbk-alertas-contabo]]
- n8n: [[wiki/glosario/software/n8n]]
- UptimeRobot: https://uptimerobot.com/ (verificado 2026-10-22)
- EasyPanel docs: https://easypanel.io/docs (verificado 2026-10-22)
