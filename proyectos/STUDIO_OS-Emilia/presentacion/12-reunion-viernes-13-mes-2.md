---
tipo: proyecto
cliente: Emilia Pimenta
proyecto: Studio OS
ciudad: Argentina
pais: AR
fase: briefing
fecha_creacion: 2026-11-10
ultima_actualizacion: 2026-11-10
estado: presentacion
tags: [reunion, viernes-13, mes-2, meta, hermes, emilia, equipo, costos, concurso]
---

# Reunión viernes 13 — retomar, mostrar y poner meta al mes 2

> Paráfrasis ejecutiva para la reunión: dónde estamos tras 3 semanas (21/10→10/11, con una semana en blanco por enfermedad), qué se muestra en vivo y qué se propone como meta del segundo mes (lunes 16, con corrimiento posible al miércoles 18).

## 1 · Dónde estamos (una carilla)

- **Tres frentes tocados**: Rhino (cortes AIZ y Casa Uruguay, massing Sagrada + CABA) · Comfy (matriz con seed fijo, galería de 119 renders, 17 LoRAs, WF sdxl-vista, calco-estilo, marca de agua, tanda Flow + tanda Pollinations) · Hermes/Sistema Operativo (tabula rasa, plan maestro T1-T9, overview, ingeniería C4, guion con holoarquitecto, Telegram→imagen vía Pollinations, VPS verificado).
- **42 sesiones** registradas en 21 días, 14 specs, 45 scripts, 9 commits. Semana del 04→10/11 en blanco por enfermedad: nada nuevo, nada roto.
- **Tableros listos y enlazados**: puerta única en [11-indice-dashboards.md](11-indice-dashboards.md) (3 vigentes + galería + curso + 5 históricos, sin repetir).
- **Lo pendiente estructural**: Hermes todavía no está conectado; Emilia ejecuta agentes sueltos en n8n pero nada del avance reciente es ejecutable por ella todavía.

## 2 · Qué mostrar en vivo (15 min)

1. [dashboard-quincena.html](dashboard-quincena.html) solapa TEMAS: el mapa de las 3 semanas en 4 tarjetas.
2. [dashboard-concurso.html](dashboard-concurso.html): las 35 corridas para keeper/descartar con Sol.
3. [dashboard-referentes-aixgaudi.html](dashboard-referentes-aixgaudi.html): lenguaje visual del concurso.
4. Cierre con la meta propuesta abajo.

## 3 · Meta mes 2 propuesta (a acordar el viernes)

> **Al lunes 16 (con margen al miércoles 18): Hermes conectado y unificado con los workflows conocidos, trabajando de a 2, con todo avance ejecutable por Emilia.**

- **Hermes conectado**: F0 en el VPS (verificado: entra con 3 GB), Telegram como interfase, registro híbrido Postgres+vault.
- **Unificado con lo conocido**: los workflows que ya funcionan (voz, agenda, render, massing) pasan por Hermes con gobernanza A-D en vez de vivir sueltos en n8n.
- **Equipo de 2**: reparto Sol (criterio + validación) / Emilia (operación diaria) con permisos y memoria por perfil; el avance de cada semana queda ejecutable por Emilia antes del viernes.
- **Último mes en paralelo**: análisis de necesidades y costos por tarea/mes + concurso Gaudí (entrega 16/12).

## 4 · Plan mar 10 → vie 13

| Día | Foco |
|---|---|
| Mar 10 | Puerta única + reporte 21 días al día (hecho hoy) |
| Mié 11 | Ordenar backlog y costos base por tarea |
| Jue 12 | Conectar Hermes (F0) y primera prueba extremo a extremo |
| Vie 13 | Reunión: mostrar tableros, acordar meta mes 2, primer workflow compartido para Emilia |

## 5 · Riesgos

- La semana en blanco comprimió el margen: si F0 se traba, la meta se corre al miércoles 18 sin cambiar el alcance.
- Sin meta de mes 2 hasta el viernes, el avance sigue sin dueño: la reunión la fija o la mueve.
