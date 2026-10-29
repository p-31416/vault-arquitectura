---
tipo: readme
mvp: 07
cliente: Estudio (interno)
proyecto: Studio OS — sistema operador del estudio de arquitectura
ciudad: CABA
pais: Argentina
fase: especificacion
fecha_inicio: 2026-10-28
fecha_estimada_entrega: s/d
ultima_actualizacion: 2026-10-28
estado: activo
tags: [readme, mvp_07, studio-os, pitauos, hermes, mcp, tailscale, runpod, trazabilidad]
idioma: es
---

# MVP_07 — Studio OS

> **Todo el sistema está en un solo documento:** [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07 · documento maestro]].
> Este archivo es solo la puerta de entrada.

## Qué es Studio OS

El **sistema operativo de un estudio de arquitectura**: une AutoCAD, Rhino, Twinmotion y (después) Unreal con la vida real del estudio —reuniones, decisiones, obra— para que **cada plano, modelo, render y acta quede atado a su origen, a su versión y a quien lo aprobó**, y una IA ejecute el trabajo repetitivo dejando las decisiones en manos del arquitecto.

Es **producto**: base replicable, con el estudio de Emilia como piloto.

## Norte (el criterio único)

> Cualquier resultado se puede explicar: de qué archivo salió, con qué versión, con qué herramienta y parámetros, y quién lo aprobó. Sin eso, cuenta como fallo.

## Estado

Diseño cerrado el 2026-10-28 (visión, estructura, requerimientos, contratos, plan y 8 decisiones). **La implementación arranca por F0** (fundaciones en el VPS). Primer sistema completo: caso **AIZ + render IA**.

## El documento maestro

[[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07.md]] — un solo archivo, nueve secciones:

1. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#1 · Visión|Visión]] · 2. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#2 · Estructura|Estructura]] · 3. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#3 · Requerimientos|Requerimientos]] · 4. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#4 · Roadmap y cierre del MVP|Roadmap y cierre del MVP]] · 5. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#5 · Contratos técnicos|Contratos técnicos]] · 6. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#6 · Decisiones|Decisiones]] (las 8 ADRs, en formato Nygard) · 7. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#7 · Plan de construcción|Plan de construcción]] · 8. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#8 · Comandos de F0|Comandos de F0]] · 9. [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07#9 · Anexos|Anexos]] (compose, `SOUL.md`, skill)

## Lo que vive fuera del documento (por ser código o runtime)

| Qué | Dónde | Por qué |
|---|---|---|
| Inventario del VPS | `scripts/studio_os_verificar_vps.py` + `_notas.md` | código: se ejecuta, no se lee |
| Publicación de identidad y skills | `scripts/studio_os_publicar_hermes.py` + `_notas.md` | código: extrae §9.2 y §9.3 del maestro y los publica en el agente |
| La auditoría de nube | `raw/research/2026-10-28-runpod-auditoria-pi.md` | research con 29 fuentes oficiales |
| La sesión de delineado | `raw/sessions/2026-10-28-sesion-delinear-pitauos.md` | bitácora |

## Contexto externo

- `raw/docs/plan-hermes.md` — el briefing técnico que originó el diseño.
- `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md` — el plan comercial del piloto (su §4 queda reemplazado por el maestro).
