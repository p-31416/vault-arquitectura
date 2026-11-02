---
tipo: indice
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-02
tags: [studio-os, pi, arquitectura-sistemas, diagrama, hermes, mvp_07]
idioma: es
---

# Arquitectura de PI — sistema operativo de capacidades

> Gráfico técnico y de producto de PI: integra la conversación «Diseño del sistema operativo», la tesis del Meta-arquitecto sistémico y la empresa sintética con las decisiones vigentes en [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]], [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] y [[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]].
> **Fuentes**: análisis en [[specs/261101-doc-chatgpt-diseno-pi-os|specs/261101]], guion de producción en [[specs/261101-guion-visual-pi-remotion|specs/261101-guion-visual]], transcripción cruda en [[raw/reuniones/2026-11-01-chatgpt-diseno-sistema-operativo-pi|raw/reuniones/2026-11-01]]. La página web y el video abren este mapa como dibujo animado.
> **Código**: [[diagramas/arquitectura-pi-os|arquitectura-pi-os.mmd]] (mermaid editable).

## 1 · El gráfico

> La vista de abajo es la síntesis ejecutiva. El editable [[diagramas/arquitectura-pi-os|.mmd]] añade el inventario de MCP, los lenguajes por rol, los destinos de ejecución, el circuito de aprendizaje y el mantenimiento.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter,Segoe UI,sans-serif'}}}%%
flowchart TB
    classDef human fill:#211b17,stroke:#e4a1a8,color:#f5f3ef
    classDef core fill:#20242b,stroke:#d97706,color:#f5f0e6
    classDef role fill:#1e2b26,stroke:#3f9e7f,color:#e6f4ee
    classDef tool fill:#1c232e,stroke:#5b7f9e,color:#e8eef4
    classDef work fill:#241d2b,stroke:#9e5b7f,color:#f2e6ee
    classDef memory fill:#2b241d,stroke:#b0885b,color:#f5eee4
    classDef upkeep fill:#18232a,stroke:#8ec2ea,color:#e8eef4

    subgraph EVOL["EVOLUCIÓN · operador → meta-arquitecto artesanal → PI → Meta-arquitecto sistémico"]
        direction LR
        OP["1 · Operador<br/>persona ↔ software"] --> META["2 · Meta-arquitecto artesanal<br/>4–6 sesiones · agentes"] --> PISYS["3 · PI / empresa sintética<br/>Hermes · brain local · n8n"] --> META2["4 · Meta-arquitecto sistémico<br/>diseña · mantiene · evoluciona"]
    end

    ARQ(["ARQUITECTO<br/>intención · criterio · aprobación"])
    PERFIL["Experiencia personal<br/>contexto de persona y proyecto"]
    HERM["Hermes core del estudio<br/>memoria · roles · skills · cron"]
    PLAN["Contrato de tarea<br/>entrada · riesgo · costo · calidad"]

    subgraph ROLES["ROLES SINTÉTICOS · cruzan todos los proyectos"]
        direction LR
        CAD["Pipi CAD<br/>AutoLISP · comandos · Python"]
        RHINO["Pipi Rhino<br/>Python · GH/Hops"]
        VIS["Pipi Visual<br/>Comfy workflow/API"]
        DOCS["Pipi Docs<br/>Fathom · vault"]
        PM["Pipi PM<br/>Leantime · n8n · cron"]
        QA["QA / gobernanza<br/>hash · A–D · evidencia"]
    end

    CAP["Biblioteca<br/>skills + workflows probados"]
    MCP["MCPs / APIs<br/>AutoCAD · Rhino · Comfy · Fathom · n8n · Leantime"]

    subgraph EXEC["EJECUCIÓN SEGÚN PERFIL Y CLASE DE DATO"]
        direction LR
        LOCAL["PC local<br/>CAD · Rhino"]
        VPS["VPS 24/7*<br/>Hermes · n8n · registro"]
        GPU["GPU cloud<br/>bajo demanda"]
    end

    subgraph RECORD["TRAZABILIDAD Y CONOCIMIENTO DEL ESTUDIO"]
        direction LR
        DB["PostgreSQL<br/>tarea · ejecución · costo"]
        VAULT["Vault / wiki<br/>método · decisiones · fuentes"]
        ART["Artefactos<br/>entrada/salida · versión · hash"]
    end

    PITA["PITAUTECH / operación<br/>actualización · pruebas · soporte"]
    MAINT["Mantenimiento visible<br/>conectores · skills · backups · costos"]

    ARQ -->|"brief y criterios"| PERFIL --> HERM --> PLAN
    PLAN --> CAD & RHINO & VIS & DOCS & PM & QA
    ROLES <-->|"invoca / reutiliza"| CAP
    ROLES --> MCP --> EXEC
    EXEC --> DB & ART
    DB & ART --> QA -->|"alternativas y excepciones"| ARQ
    QA -->|"feedback revisado"| CAP
    VAULT -->|"respuestas con referencia"| PERFIL
    PITA --> MAINT --> HERM
    MAINT --> MCP & CAP & DB
    PISYS --> HERM
    META2 -.->|"diseña roles, estándares y mantenimiento"| ROLES
    META2 --> MAINT

    METRIC["SE MIDE · Wv/Th · transferencia senior · correcciones · costo/run · mantenimiento"]
    DB -.-> METRIC

    class ARQ,PERFIL,META2 human
    class HERM,PLAN,PISYS core
    class CAD,RHINO,VIS,DOCS,PM,QA role
    class MCP,LOCAL,VPS,GPU tool
    class CAP,DB,VAULT,ART memory
    class PITA,MAINT upkeep
    class METRIC work
```

## 2 · Cómo leerlo

- **El Meta-arquitecto es el cierre del relato**: diseña, gobierna, mantiene y amplía PI. La empresa sintética es el sistema que construye; los arquitectos de proyecto usan sus capacidades sin operar la arquitectura técnica.
- **Núcleo vigente**: un Hermes por estudio, según [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|VISION §6.9]]. Un asistente por arquitecto se plantea como perfil/contexto personal sobre un núcleo común; instancias Hermes aisladas por persona requieren una decisión de producto/arquitectura.
- **La unidad que crece** es la biblioteca de capacidades (skills versionadas con dependencias y validación); los agentes las consumen. «La verdadera unidad de crecimiento de PI no es la cantidad de agentes instalados sino la cantidad de capacidades verificadas que puede poner a disposición de cada estudio».
- **Los entornos de ejecución son intercambiables**: el agente no decide dónde vive el trabajo pesado; lo decide el perfil de la tarea (local si la GPU está libre, cloud si está ocupada, programado si la app vive en una PC apagada). Eso es el **PI Resource Manager** propuesto, a construir sobre el sobre de tarea del vault.
- **Toda ejecución queda registrada; C/D esperan aprobación explícita**: la regla de gobernanza A–D ya formalizada en [[proyectos/MVP_07-studio-os-sistema/REQUISITOS#7 · Gobernanza por nivel de riesgo|REQUISITOS §7]].
- **Aprendizaje no equivale a entrenamiento**: memoria de trabajo, skills aprobadas y ajuste de pesos son mecanismos separados.
- **La deuda técnica se hace gestionable**: scripts, conectores, workflows, seguridad, backups, compatibilidad y soporte pasan a un ciclo visible de mantenimiento.
- **La medición** es la que permite demostrar el salto: mismas horas humanas, más capacidad — tiempo humano, tiempo efectivo de ejecución, tiempo de espera, tareas validadas, reutilización y **producción desacoplada del tiempo humano**.
- Mapeo con el vault: los entornos coinciden con los nodos de [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA#1 · Vista general|ESTRUCTURA §1]] (VPS · PC del estudio · banco · GPU nube). Telegram es la interfaz cotidiana vigente; una web multiusuario queda como producto posterior.
- **Personal vs. compartido:** VISION mantiene un Hermes core por estudio. PI puede ofrecer al arquitecto un perfil/contexto de trabajo personal sobre ese núcleo; aislar una instancia por persona queda como decisión a evaluar.

## 3 · Variantes de despliegue (las 3 configuraciones de la conversación)

| | A · Económica | B · Híbrida (predilecta) | C · Control total |
|---|---|---|---|
| Cómo | VPS + PC + GPU cloud bajo demanda, máximo aprovechamiento de lo existente | VPS (núcleo) + estaciones ejecutoras + GPU cloud + interfaz web | servidor propio, GPU dedicada, NAS redundante, modelos locales |
| Fortaleza | coste mínimo | cada tarea corre donde es más eficiente | soberanía sobre datos, modelos y ejecución |
| Limitación | capacidades locales atadas a PCs encendidas | gestionar conectividad y disponibilidad | inversión y mantenimiento de hardware |

**Perfil predilecto: B, híbrido.** El MVP_07 diseña un núcleo persistente en VPS, estaciones locales para CAD/geometría y GPU cloud como excepción. La composición lo presenta como dirección de despliegue; cada integración y estación se valida por fase en [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES|IMPLEMENTACION-HERMES]].

## 4 · Gráfico para explicar (la cara pública)

- `diagramas/prompt-coach-vs-agentico.html` — presentación visual **operador → meta-arquitecto artesanal → PI/empresa sintética → Meta-arquitecto sistémico**, con flujo aumentado, casos MVP, lenguajes de herramientas, mantenimiento, MCPs, privacidad, fórmula y fuentes.
- `diagramas/arquitectura-pi-os.mmd` — el mapa técnico editable (mermaid).
- `P:\00-repos\remotion-vault\src\PIStudioOS.tsx` — composición Remotion `03-PIStudioOS`, ocho escenas animadas del flujo a empresa sintética.
- [[scripts/00-index|scripts]] — `auditar_presentacion_pi.py` valida archivos, MCPs activos y anclas de contenido (solo lectura).

## 5 · Relación con otros diagramas

- [[diagramas/cerebro-hermes-fractal|cerebro-hermes-fractal]] — la memoria fractal del vault (dónde piensa Hermes).
- [[diagramas/flujo-fuentes-wiki-hermes|flujo-fuentes-wiki-hermes]] — el ciclo del conocimiento (tex → wiki → Hermes).
- [[diagramas/agentes-fuentes|agentes-fuentes]] — el circuito de los agentes Sherlock/contenidos.
- [[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]] — la arquitectura formal con ADR del MVP_07.
