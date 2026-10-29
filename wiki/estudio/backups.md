---
tipo: oficina
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-10-22
tags: [estudio, backups, vps, disaster-recovery, politica]
---

# Backups del vault y del VPS

> Política de respaldo del estudio. Volver a [[wiki/estudio/00-index|índice padre]].

## Estado actual (2026-10-22)

| Qué | Cómo | Estado |
|-----|------|--------|
| **Vault (Obsidian)** | `git push` a GitHub | ✅ Activo (cada sesión) |
| **VPS — dump Leantime (MySQL)** | Manual, `mysqldump` + gzip | ⚠️ Solo backup pre-upgrade (22/10) |
| **VPS — snapshot Contabo** | Desde Customer Control Panel | ❌ No configurado |
| **VPS — volumes Docker** | — | ❌ Sin respaldo |
| **n8n — workflows** | Viven en Postgres del VPS | ❌ Sin export periódico |
| **Leantime — storage** (archivos adjuntos) | Volumen Docker | ❌ Sin respaldo |

## Estrategia objetivo 3-2-1

Tres copias, dos medios, una off-site:

1. **Dump automático diario** de MySQL (Leantime) + Postgres (n8n) → comprimido
2. **Snapshot semanal del VPS** desde el panel Contabo
3. **Copia off-site** via rclone a Wasabi o Google Drive

## Cómo hacer backup manual (hoy)

```bash
# Desde la PC local
ssh contabo

# Backup Leantime (MySQL)
docker exec pitautech_leantime-db mysqldump -umysql -p'PASSWORD' pitautech | gzip > /opt/backups/leantime_$(date +%F).sql.gz

# Backup n8n (Postgres)
docker exec pitautech_postgres pg_dump -U postgres n8n | gzip > /opt/backups/n8n_$(date +%F).sql.gz

# Verificar
ls -lh /opt/backups/
```

> **Nota:** los passwords están en los env de cada servicio. Obtenerlos con:
> `docker inspect <container> --format '{{range .Config.Env}}{{println .}}{{end}}' | grep PASSWORD`

## Restaurar

```bash
# Leantime
gunzip -c /opt/backups/leantime_YYYY-MM-DD.sql.gz | docker exec -i pitautech_leantime-db mysql -umysql -p'PASSWORD' pitautech

# n8n
gunzip -c /opt/backups/n8n_YYYY-MM-DD.sql.gz | docker exec -i pitautech_postgres psql -U postgres n8n
```

## Pendiente de implementar

- [ ] Backup diario automático (cron en el VPS o workflow n8n)
- [ ] Snapshot semanal desde Contabo CCP
- [ ] Export periódico de workflows n8n (JSON)
- [ ] rclone → almacenamiento off-site (Wasabi o Drive)
- [ ] Test de restore mensual

**Diseño completo de backup:** ver `backup.sh` en [[wiki/estudio/adrs/ADR-INFRA-002-vps-dedicado-estudio|ADR-INFRA-002]] (apunta al diseño Hetzner; adaptar rutas al VPS actual Contabo).

**Durante incidentes:** el backup pre-upgrade del 22/10 está en el VPS en `/opt/backups/`.
