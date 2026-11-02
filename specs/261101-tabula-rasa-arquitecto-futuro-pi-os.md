---
tipo: metodologia
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [pi, studio-os, arquitectura-sistema, hermes, mvp_07, tabula-rasa, meta-arquitecto]
idioma: es
---

# PI OS — Arquitectura del sistema desde la tabula rasa de Sol

> Diseño experto en software para estudio de 2 personas (Sol técnica + 1 arq), con proyección a mediana escala + desarrollo inmobiliario.
> Fuente primigenia: [[raw/sessions/2026-11-01-sesion-tabula-rasa-pi|sesión tabula rasa]].
> Avanza sobre lo vigente: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]] · [[specs/261101-doc-chatgpt-diseno-pi-os|análisis ChatGPT]].

## 1. Visión — el núcleo del ejercicio

**PI como sistema operativo de capacidades:** integra agentes, herramientas, conocimiento y recursos para transformar procedimientos en capacidades persistentes, versionadas y escalables. Hermes administra agentes y capacidades; n8n conecta eventos y archivos; MCP + API conectan herramientas; los entornos ejecutan el trabajo pesado.

El arquitecto del futuro dirige, valida y decide. El sistema ejecuta, registra y mejora la memoria de la casa. La hora humana avanza hacia dirección; la capacidad productiva avanza desacoplada del tiempo presencial.

Principios que se conservan: libre y abierto cuando aporta valor, automatización antes que IA para lo repetible verificable, humano aprueba lo contractual, trazabilidad total, formatos abiertos, modularidad, reproducibilidad, escalabilidad progresiva.

## 2. Arquitectura lógica — 4 nodos + 1 contrato

```text
Telegram/Web/Panel → Hermes VPS (agente único estudio) → n8n + API + MCP → Runner/puentes → AutoCAD / Rhino+Hops / ComfyUI API / FreeCAD+IfcOpenShell / Unreal futuro
                                        ↓
                    PostgreSQL vivo + vault narrativo + Qdrant sentido + registro aprobaciones
```

- N1 VPS siempre encendido: Hermes + n8n + Postgres + Leantime + Redis + Qdrant + vault canónico.
- N2 PC estudio: AutoCAD + Rhino con puente, runner bajo demanda.
- N3 Banco pruebas: stack completo para validación.
- N4 GPU nube excepción: Comfy Cloud demo + Runpod Secure solo derivado, con DPA, volume cifrado, 0 puertos.

Contrato único — sobre de tarea:

```json
{"task_id": "uuid", "project": "demo", "tool": "audit_dwg", "verbo": "inspect", "input": {"file_ref": "vault://..."}, "riesgo": "A", "approval": "not_required", "idem_key": "audit:demo:001"}
```

Reglas que se mantienen: `file_ref` resoluble contra vault, verbo define riesgo mínimo, `idem_key` otorga idempotencia, respuesta con `provenance` completa, tarea fuera de registro queda en espera.

## 3. Agentes — equipo con memoria propia

- PI Manager coordina, interpreta objetivo en lenguaje natural y delega.
- Pipi CAD documenta y audita AutoCAD con estándares internos.
- Pipi Rhino modela, mide, ejecuta Hops y exporta.
- Pipi Visual opera ComfyUI por API con workflows versionados.
- Pipi BIM inspecciona IFC con FreeCAD + IfcOpenShell.
- Pipi Docs cura reuniones, fuentes y wiki.
- Pipi PM sostiene compromisos, agenda y métricas.

Cada skill incluye objetivo, entradas, herramientas autorizadas, precondiciones, procedimiento, validación, permisos, formato salida, errores y evidencias. Cada ejecución escribe documentación y propone mejora con aprobación. Biblioteca de capacidades con versión, dependencias y compatibilidad.

## 4. Integraciones — una por una con decisión MVP

### 4.1 AutoCAD — fundación que habilita todo

MCP por COM en PC estudio para lectura y auditoría, Core Console para headless, LISP arranque aislado, FreeCAD + ezdxf + ODA como vía libre. Flujo MVP: auditar capas, escalas, referencias, unidades, preparar sheets, publicar PDF con hash intacto. Usar bien AutoCAD abre el camino al resto del sistema.

### 4.2 Rhino + Grasshopper paramétrico

Puente `localhost:9876` + Hops para GH sin pantalla. Evaluación 8 vs 9 antes de T3 por licencia y Hops. Rhino.Compute como candidato R2 headless para geometría masiva. Operaciones con viewport y `Redraw` avanzan con app abierta; extrusión y guardado .3dm avanzan headless.

### 4.3 ComfyUI por API — motor visual

API con colas como vía principal, CLI para debug, cloud como excepción. Orden MVP: primero flujos del concurso (txt2img, img2img croquis a render, ControlNet depth/canny, 3D a imagen), después custom complejos (batch, paralelismo, pipeline, orquestación por agente). Cada corrida registra modelo, LoRA, seed, sampler, pasos, cfg, resolución, prompt, costo y hash en portal, con [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows]] vigentes.

### 4.4 BIM abierto

FreeCAD + IfcOpenShell + IfcMCP para inspeccionar, extraer, validar y comparar. Bonsai queda para ciclo posterior con IFC real del estudio.

### 4.5 Visualización futura

Unreal a futuro con MCP oficial y escala a VR. Twinmotion acompaña como asistido R3: Hermes prepara, la persona ejecuta, el sistema registra.

### 4.6 Entradas del flujo arquitectónico

Croquis escaneado hacia wiki + cuaderno digital tipo libro, volumetría 3D hacia .3dm editable, texto y voz hacia minuta y tareas, imagen referencia hacia exploración visual. Maqueta 3D y SketchUp ingresan por `file_ref` y avanzan hacia estándar casa en T6.

### 4.7 Secretaría — todo junto desde el inicio

Telegram con temas por obra + canal bitácora + aprobaciones con botones. Fathom agrupa meetings repetidos y produce minuta con decisiones. Compromisos con qué entregar y fecha, con aviso previo. Cal.com + Google Calendar vivos. Correo con formato casa: Hermes redacta, la persona envía. Métricas: trazabilidad 100%, tiempo junior avanzando con autonomía, ahorro en automatizadas, éxito, costo por ejecución, RAM y swap visibles.

## 5. Gobernanza y seguridad

Nivel A lectura automática, B generación aislada en carpeta controlada, C modificación con aprobación y copia más reversión, D publicación o acción externa con aprobación explícita de versión concreta. Superficie cerrada: red privada Tailscale, cero puertos públicos, secretos en `.env` 600 fuera del repo, backup restic/borg verificable con restauración probada. Planos legales y material sensible permanecen en entorno estudio.

## 6. Plan T0-T4 para 2 personas

- T0 Inventario con script solo lectura: RAM, disco, servicios.
- T1 Cimientos: vault canónico VPS, red privada, Hermes con SOUL y skills, MCP n8n.
- T2 Contrato y registro: schema Postgres, API escritura única, validador sobre.
- T3 Primer motor: auditoría DWG real caso AIZ con hash intacto.
- T4 Interfase: Telegram + aprobaciones + digest + recordatorios.
- T5-T6 quedan para imagen con procedencia, cuaderno navegable y piloto en obra con entregas.

Criterios de aceptación vigentes en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#6 · Criterios de aceptación|REQUISITOS §6]]: AC-01 a AC-05 contrato, AC-06 a AC-07 CAD, AC-08 a AC-09 riesgo, AC-12 disponibilidad con estado explícito, AC-14 a AC-18 reuniones y cuaderno.

## 7. Decisiones que este spec deja tomadas

| Decisión      | Elección MVP                            | Alternativa que queda para ciclo posterior |
| ------------- | --------------------------------------- | ------------------------------------------ |
| ComfyUI       | API                                     | CLI debug, cloud excepción                 |
| Flujos        | concurso primero                        | custom complejos después                   |
| Rhino red     | puente + Hops                           | Rhino.Compute R2, runner con cola          |
| Rhino versión | evaluar 9                               | quedarse en 8                              |
| BIM           | FreeCAD + IfcOpenShell                  | Bonsai con IFC real                        |
| Visualización | Unreal futuro                           | Twinmotion asistido                        |
| Entradas      | croquis, volumetría, texto, voz, imagen | maqueta, modelado rhino pleno en T6        |
| Secretaría    | todo junto                              | avance por fases                           |
| Escala        | Sol técnica + 1 arq                     | mediana + desarrollo inmobiliario          |

## Referencias verificadas en vault

- [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] · [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]] · [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]]
- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] · [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] · [[specs/261029-filosofia-hermes|filosofía Hermes]]
- [[raw/reuniones/2026-11-01-chatgpt-diseno-sistema-operativo-pi|transcript ChatGPT]] · [[specs/261101-doc-chatgpt-diseno-pi-os|análisis ChatGPT]]
- [[proyectos/MVP_02-autocad-standards/readme-mvp_02|MVP_02]] · [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|MVP_05]] · [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04]] · [[raw/research/2026-10-30-hermes-rhino-remoto|Hermes Rhino remoto]]
