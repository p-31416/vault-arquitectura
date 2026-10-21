---
tipo: metodologia
estado: backlog
fecha_creacion: 2026-09-17
ultima_actualizacion: 2026-09-17
tags: [backlog, infra, vps, cloud, storage, nextcloud, studio-os, emilia]
origen: "Reuniones jueves 2026-09-17 (I·II·III) + pedido 2026-09-19 anotar VPS/Cloud/Storage Nextcloud"
---

# Backlog — VPS / Cloud + Storage para Nextcloud (Studio OS Emilia)

> **Estado al 2026-09-29: BACKLOG CORRECTO — para Mes 3 / roadmap 2027. Sin cambios.**

> **Tema backlog** — no bloquea Mes 1-2 del plan trimestral. Se evalúa en Mes 3 / roadmap 2027 cuando el Vault y Drive piloto estén estabilizados.

## Motivación

Evolucionar desde Google Drive piloto hacia **soberanía de datos**: Nextcloud self-hosted donde el estudio controla archivos, versiones, permisos y backups. Alineado con filosofía Vault local + privacidad desde el inicio (modelos locales, metadatos trazables).

## Opciones a evaluar

| Opción | Componentes | Pros | Contras / a medir |
|---|---|---|---|
| **VPS pequeño + volumen** | 1 VPS (2 vCPU/4 GB) + volumen Block Storage 200–500 GB | Simple, control total, costo fijo | Backups, uptime, scaling manual |
| **VPS + S3-compatible** | VPS app + B2 / Wasabi / R2 para files | Storage barato, ilimitado, versionado | Latencia, egress, complejidad |
| **Cloud managed** | Hetzner Storage Box + VPS / contenedor Nextcloud AIO | Soporte, backups incluidos | Vendor lock, costo |
| **Híbrido** | Drive piloto + Nextcloud en paralelo (sync selectivo) | Migración gradual, riesgo bajo | Doble mantenimiento temporal |

## Qué incluye la evaluación

- Sizing (usuarios, GB/mes, thumbnails, OnlyOffice/Collabora)
- Costos 12 meses por opción (VPS + storage + backup offsite + dominio/SSL)
- SSO con Google (`ark.emiliapimenta`) + 2FA
- Migración Drive → Nextcloud (rclone / Nextcloud migrator) + nomenclatura y permisos
- Backup 3-2-1 (snapshot VPS + copia S3 offsite + local)
- Métricas: disponibilidad, tiempo restore, costo/GB, soberanía vs. comodidad

## Criterios de aceptación (para salir de backlog)

- [ ] Tabla comparativa con 3 opciones + T-shirt sizing (S/M/L) y costo mensual
- [ ] PoC 1 semana en VPS de prueba con 2 usuarios + 10 GB reales del proyecto Magenta
- [ ] Decisión sí/no documentada en [[specs/260910-plan-trimestral-unificado-studio-os-emilia#10. Stack, privacidad y RunPod|plan §10]]

## Referencias

- Plan vigente: [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]]
- Crudos jueves: `raw/reuniones/2026-09-17-*-I·II·III.md` + reporte `raw/reuniones/2026-09-17-reporte-emilia-jueves.md`
- Stack actual: Drive piloto + Vault Obsidian + Fathom/Cal (Mes 1)

## Estado

`backlog` — etiquetar en Leantime `backlog/infra` para Mes 3.
