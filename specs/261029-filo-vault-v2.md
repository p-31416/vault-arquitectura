---
tipo: metodologia
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [filosofia, vault-v2, studio-os, hermes, diagrama]
---

# Filo Vault v2 — documento único

> Todo el sistema en un archivo: visión → estructura → requisitos.
> Nace de la sesión filosófica del 29/10/2026 y absorbe lo vigente de [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|documento maestro MVP_07]] sin duplicarlo.
> Núcleo nuevo + migración selectiva (híbrido): lo canónico viaja, lo efímero queda.

- [[#1 · Visión]]
- [[#2 · Estructura]]
- [[#3 · Requisitos]]

---

# 1 · Visión

## 1.1 La frase

> **El vault es la memoria verificable del estudio; los scripts son su mano repetible; los agentes son su criterio asistido; la persona aprueba lo contractual.**

## 1.2 Las fuentes alimentan una wiki común

Cuatro agentes, una sola wiki. Sherlock busca afuera, Brainstormy diverge, Contenidos formatea, Vaultworm (honor al bookworm) conecta. Ninguno escribe en `wiki/` sin `s` humano.

| Fuente | Ejemplos | Crudo en | Quién |
|---|---|---|---|
| Video | YouTube, grabado propio, captura OBS | `raw/yt/transcripts/` | Sherlock transcribe, Contenidos formatea |
| Imagen | Instagram, captura, JPG, foto de obra | `raw/referentes/` | Contenidos ficha, Vaultworm conecta |
| Texto | Revista de arquitectura, artículo, paper científico | `raw/pdf/` + ficha | Sherlock extrae, Contenidos extiende |

Doble vía de carga: manual (tirar a carpeta) y asistida (Sherlock como buscador cuando un tema se necesita de cero). Fronteras en [[diagramas/prueba-comparativa|prueba comparativa]] y [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|filo MVP_07]].

## 1.3 La wiki fractal, iterable, rizomática

Tres propiedades que la hacen navegable y eterna:

- **Fractal** (Mandelbrot: recursividad = lo mismo a menor escala): cada nodo se desmenuza en hijos del mismo tipo, cada vez más simples. Ej. `comfyui` → `lora-locales-comfyui` → `WF-loras-locales/`.
- **Iterable** (repetible): el mismo pipeline corre para 1 o 100 fuentes sin cambiar.
- **Rizomática** (entrada por cualquier punto): cada ficha lleva Front Matter (tipo, fechas, tags) + `Conceptos relacionados ≥2` + índice `[[#Encabezado exacto]]`, así se ubica sin releer todo. Camino canónico: entro por LLM y llego a cómo ese LM se comporta dentro de Hermes.

## 1.4 Sistema propio vs. ventana de ChatGPT

| Ventana de ChatGPT (ni siquiera Codex) | Sistema propio |
|---|---|
| Diálogo sin memoria verificable | Vault versionado + registro Postgres |
| Flujos aislados que otros enseñan | Pipeline completo fuente → wiki → ejecución |
| Vos ejecutás con manos humanas limitadas | La IA como mano ilimitada de tus herramientas |
| Sin Front Matter, sin registro, sin `s` | Trazabilidad: origen, versión, parámetros, aprobador |

## 1.5 Hermes: más que un LLM

Hermes es LLM + MCPs-brazos + registro. La IA traduce lenguaje natural a binario, el idioma de la máquina: un salto cuantitativo de tareas. Pi es el CEO-orquestador: ante cada encargo deriva a búsqueda web o a registro wiki, y siempre pasa por revisión humana antes de registrar. Ensayo filosófico completo: [[specs/261029-filosofia-hermes|filosofía de Hermes]].

## 1.6 La mano, el tiempo, el dinero

Procesos claros = tiempo ahorrado = dinero = tiempo liberado para diseñar al doble (iterar más, no diseñar menos). Corte por MVP:

- **Determinista, sin IA**: mover Fathom → Drive una vez por día al terminar la reunión, archivar lo que llega por Telegram, indexar, auditar. Ya existe en [[scripts/00-index|scripts]].
- **Agéntico, con `s`**: buscar, sintetizar, proponer. Falta automatizar esta mitad del proceso.
- **Contractual, humano siempre**: publicar, enviar, sobrescribir.

HITL estricto: todo `wiki/` y toda ejecución piden `s` explícito (`s/si/ok/dale`), sin vías auto-aprobadas ni en lectura. Ver [[AGENTS.md|reglas]].

## 1.7 Cuarta revolución + arquitectura de sistemas + agentes personales

Como el vapor cambió el tiempo en la primera revolución, la IA cambia el tiempo en la cuarta: es tecnología que se volverá invisible y automatizada. 2026 se alinea con los agentes personales — ese es el futuro inmediato y conviene sumarse antes posible.

Aclaración nominal: `arquitectura (AEC)` vs. `arquitectura de sistemas` comparten nombre y distinto objeto; el vault usa siempre `AEC` para traer resultados de arquitectura y construcción.

Esta visión se traduce en [[#2 · Estructura]] y [[#3 · Requisitos]].

---

# 2 · Estructura (enunciado + norma de diagramas aprobada 29/10)

Puertas: `00-index` · `wiki/00-index` · `proyectos/00-index`. Ramas del glosario: software / entidades / referentes / conceptos / interno. Inbox `raw/` append-only. Proyectos `<cliente>-<proyecto>-<ciudad>/` + `template_arq/`. Specs con ADRs fusionados. Scripts en par didáctico (`<slug>.py` + `<slug>_notas.md`). Binarios por referencia en `activos/` (gitignored).

## Norma de diagramas (aprobada)

- **draw.io**: G1-G3 y todo diagrama de sistema (formal UML/BPMN/C4, librerías técnicas, SVG acotado sin scroll). Editable en Obsidian vía plugin `draw.io` (desktop-only, local/offline).
- **Mermaid**: diagramas rápidos inline que Pi genera en el momento (texto, nativo, diff limpio).
- **Excalidraw**: solo croquis de presentación y anotación de capturas/renders (plugin instalado v2.29.0, siempre exportar acotado).
- Comparativa viva: [[diagramas/prueba-comparativa|prueba comparativa]].
- Gráfico operativo (29/10): [[diagramas/flujo-fuentes-wiki-hermes|flujo fuentes → scripts → raw → agentes → wiki → Hermes]] — 4 carriles con scripts reales por fuente, tabla replicable y composición Hermes (LLM + harness + skills, Karpathy).
- Gráfico filosófico (29/10): [[diagramas/cerebro-hermes-fractal|cerebro fractal y rizomático]] — las 4 ramas con idéntica subdivisión, rizoma punteado, centro cerebro y anillo Hermes (memoria + MCPs + mantiene + mejora).

Evolución Hermes: empieza un agente del estudio, luego perfiles por persona, runners a evaluar (puente P1+P3 mediante).

---

# 3 · Requisitos (enunciado, a desarrollar siguiente ciclo)

R1 Trazabilidad total (origen, versión, herramienta, parámetros, aprobador) · R2 HITL estricto con equivalencias de aprobación vigentes · R3 Frontmatter obligatorio y wikilinks absolutos sin extensión · R4 URLs oficiales verificadas 200 · R5 Lenguaje en positivo · R6 Cierre de sesión en `raw/sessions/` + fila nueva-arriba en `log.md` · R7 Si no pasó en P:, no viaja a G:.
