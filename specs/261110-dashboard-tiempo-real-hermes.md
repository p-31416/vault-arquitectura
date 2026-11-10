---
tipo: spec
fecha_creacion: 2026-11-10
ultima_actualizacion: 2026-11-10
tags: [spec, hermes, dashboard, tiempo-real, emilia, web, foolproof, gobernanza]
estado: propuesta
---

# Dashboards vivos con Hermes: tiempo real + acceso web de Emilia + a prueba de no-técnicos

> Cómo los tableros dejan de ser archivos que regenera Sol y pasan a ser vistas vivas: se actualizan ante cada cambio, Emilia los mira por web y carga información sin poder romper nada.

## 1 · Objetivo

- **Vivo**: cada cambio del vault (sesión, corrida, referente) regenera los tableros en minutos, sin intervención manual.
- **Web para Emilia**: una URL que abre en el celular, siempre al día, con las vistas que a ella le sirven (TEMAS, selección concurso, referentes por programa).
- **A prueba de no-técnicos**: Emilia nunca edita `.md` ni corre scripts; si algo entra mal validado, se rechaza con explicación en lenguaje normal y nada se rompe.

## 2 · Arquitectura (3 piezas)

| Pieza | Qué hace | Dónde vive |
|---|---|---|
| **Detector** | mira `git status` cada 5 min (cron) o recibe webhook post-push | VPS `contabo`, al lado del vault canónico |
| **Regenerador** | corre los scripts (`dashboard-quincena.py --hasta hoy`, `dashboard-concurso.py`, `galeria-renders.py`, `referentes_dashboard.py`) y valida la salida | mismo VPS, entorno `comfyenv` espejo o solo-stdlib |
| **Servidor** | publica los HTML + `datos.json` (los JSON ya son una API lista para usar) | `pitau.tech/tableros/` (nginx estático) o Tailscale si se quiere cerrado |

Regla de oro: **regenerar es idempotente** — correr dos veces da lo mismo que una. Si un script falla, se conserva la versión anterior y se avisa por Telegram.

## 3 · Contrato anti-desconfiguración (el corazón foolproof)

1. **Emilia no toca archivos**: manda foto, audio o texto por Telegram → Hermes transcribe/clasifica.
2. **Validación antes de escribir**: frontmatter completo, tags del vocabulario cerrado (`TEMAS`, ejes de referentes), wikilinks con ruta absoluta sin extensión, binarios solo como referencia a `activos/`.
3. **Vista previa antes de publicar**: Hermes muestra el diff en lenguaje normal ("voy a sumar 1 corrida al tablero concurso") y espera `s` en pasos C/D.
4. **Append-only**: las sesiones y la matriz solo crecen por abajo/arriba según su regla; nunca se reescriben entradas viejas. Todo es reversible por git.
5. **Chequeo automático del tablero**: tras regenerar, `node --check` al JS, cero placeholders `__DATOS__`, conteo de items > 0. Si algo falla, se publica la versión anterior.
6. **Los scripts no se tocan por chat**: cambiar un generador exige PR con `s` explícito de Sol y corrida de prueba.

## 4 · Fases

| Fase | Alcance | Gate |
|---|---|---|
| F0 (hoy) | regeneración manual + `presentacion/` commiteado (hecho: quincena, concurso, historia, referentes) | tableros al día en GitHub |
| F1 | cron en VPS cada 15 min + `pitau.tech/tableros/` | URL pública para Emilia |
| F2 | skill Hermes `actualizar-tableros` + entrada por Telegram con validación §3 | Emilia carga sin tocar el vault |
| F3 | portal Emilia: sus vistas fijas (TEMAS, selección, referentes por programa) con links compartibles | usa diario sin ayuda |

## 5 · Costos y límites

- Servir estáticos cuesta ~0 (nginx ya corre en el VPS).
- Regenerar no usa GPU ni LLM salvo que Hermes redacte el resumen (un llamado corto por cambio).
- Límite explícito: `activos/` (renders full-res) nunca se publica ni se sincroniza; lo web lleva miniaturas embebidas.
