---
tipo: ft
fecha_creacion: 2026-06-30
tags: [ft, dibujo-ia, autocad, autolisp, framework]
estado: borrador
---

# FT: Plan Técnico del Framework de Dibujo Asistido por IA para AutoCAD

> **`ft`** = framework técnico. Es el paso a paso para lograr lo que `spec` define. Global: roadmap de niveles y decisiones técnicas. Por nivel: implementación concreta desde el hito anterior.

## Prompt original (textual)

> necesito saber si el vault sirve por ejemplko para procesar mis pensamientos primero sobre la arquitectura. por ejemplo, desarrollos que me gustan hacer para este ecosistema.. es por ejemplo.. quiero enseñarle a la IA a dibujar en "autocad", pero antes de construir un MCP.. quiero que pueda pensarlo como  lo ahria yo y que lo documente.. como por ejemplo.. tienes que dibujar una polilinea abierta que en algun lado tenga una puerta.. de minimo 80 .. entonces va a ser una polilinea abierta con un offset.. de 15 (despues deberia poderle darle el ancho a cada lado porque van a ser distintos independientemente entonce squiza encesito que sean multilineas que se empalman, y que donde marco que va la puerta se inserta una puerta, con su linea de apertura punteada, debo decirle para que lado abre, para adentro siempre por default. y que ese bloque de puestar con unos rectangulos simil marco de la puerta en 5x10cm. a cada lado , marco centrado en el centro del espesor del muro (adaptado a si el muro es de 10,12,15,18. elegir espesor variable ej. por default 15 y se puede cambiar rapidamente a 12,15,18 y si es mas, entrada del usuario. algo asi? y despues ir complejizandolo ? yo se ue existen software , pero a mi me interesa crear un framework de lo que creemos, que registre tecnología, arma una "filosofia", un documento .md (o editar AGENTS) y que antes de ejecutar nada crees un plan en.md para que pueda leerlo y editarlo, y que guardes este prompt textual

## Progresión por niveles

### Nivel 1 — Muro simple + puerta
- Polilínea **abierta** con offset bidireccional (espesor default 0.15m)
- Se empieza con offset simple; más adelante se prueba multilínea, si no aporta beneficio se descarta
- Puerta en punto indicado sobre el muro:
  - Ancho mínimo de paso: **0.80 m**
  - Vano entre muros: **0.88 m** (0.80 + 0.03 m de marco c/lado × 2 lados + holgura)
  - Marco: dos rectángulos de **0.04 m × 0.10 m** en los extremos del vano, centrados en el espesor del muro
  - Hoja de puerta: línea que marca la apertura a **90°** con respecto a la pared, hacia el **interior**
  - Arco de apertura: desde la carpintería interior hasta la punta de la puerta, línea punteada
- **Layers**:
  - `A-MURO`: tipo línea **continua**, color **blanco (white)**, espesor **0.30 mm**
  - `A-PTA-`: tipo línea **continua**, color **rojo (red)**, espesor **0.15 mm** (marco, hoja)
  - Arco apertura: dibujado en `A-PTA-` con override **DASHED**, RGB **251,251,251**, lw **0.05 mm**
- en la capa `A-MURO` Espesor de muro variable rápido: toggle entre 0.10, 0.12, 0.15, 0.18 m (default 0.15). Input libre para otros.

### Nivel 2 — Muro multilínea asimétrico
- Anchos independientes por lado
- Empalme de multilíneas en esquinas
- Espesor rápido: toggle entre 0.10, 0.12, 0.15, 0.18 m
- Input libre para otros espesores

### Nivel 3 — Ventanas + vanos
- Inserción de ventanas en muros
- Variantes de carpintería (corrediza, abrir, oscilobatiente)
- Líneas de apertura (abrir, plegar)
- Alfeizares y antepechos

### Nivel 4 — Capas y objetos anotativos
- Asignación automática de layers (estándar del estudio: `A-MURO`, `A-PUER`, `A-VENT`)
- Texto de dimensionamiento automático (se mantiene sin escalar o con una proporción adecuada definida por uno, desde el punto de inserción del texto ó variandolo)
- Escalas anotativas para planos de obra (para las cotas de dimensión unicamente, cambia tipo flecha)


### Nivel 5 — Bloques paramétricos
- Librería de bloques del estudio (muebles, sanitarios, cocinas)
- Empezaremos por una habitación vacia, luego 1 habitación con mueble, y luego mas habitaciones.baño, cocina, por nivel de detalles. y definir un bloque base ej "ducha" que despues tenga alguna variación de modelo que se pueda ejecutar con una variable o entrada del usuario. con lineas por detras del bloque.
- Inserción con parámetros de rotación, escala, visibilidad

### Nivel 6 — Planta parcial
- Composición: muros + puertas + ventanas + cotas + bloques parametricos
- Grilla estructural opcional. la grilla se dibuja en una layer distinta a la de los muros. tiene que ver con los ejes. y que tambien se puedan acotar los ejes.
- Exportación a layout/listado

### Nivel 7 — MCP server
- Envolver la lógica AutoLISP en un MCP server
- La IA conversa directamente con AutoCAD vía MCP (tiempo real) -esto en algun lado debiera quedar documentado mi trabajo con el MCP en tiempo real como cuando hablamos en antigravity con el agente en ese caso) por si en un futuro me interesa replicarlo
- Comandos en lenguaje natural → LSP → AutoCAD

## Tecnología

| Capa | Herramienta | Estado |
|------|-------------|--------|
| Lógica de dibujo | AutoLISP (.lsp) | A implementar |
| Documentación | Markdown (.md) en vault | Este plan |
| Pruebas | Carga manual en AutoCAD | Próximo |
| Futuro | MCP server (Python) | Nivel 7 |

## Estructura del proyecto

Las convenciones completas (nomenclatura, reglas, subdivisiones) están en `readme-mvp_01.md` — leer antes de trabajar.

Cada nivel en su carpeta `n_XX-nombre/` con 4 archivos: 01-spec, 02-ft, 03-log, lisp-*.lsp. Archivos raíz con prefijo numérico que indica orden conceptual.

```
proyectos/MVP_01-dibujo_ia/
├── readme-mvp_01.md  ← Puerta de entrada (reglas, navegación)
├── 00-filo-mvp_01.md ← Manifiesto (visión, principios)
├── 01-spec-mvp_01.md ← Spec viva del framework
├── 02-ft-mvp_01.md   ← Plan técnico general (roadmap, decisiones)
├── 03-log-mvp_01.md  ← Transiciones entre niveles
│
├── n_01-local/
│   ├── 01-spec-n_01.md    ← Acuerdo macro del nivel
│   ├── 02-ft-n_01.md      ← Plan técnico del nivel
│   ├── 03-log-n_01.md     ← Bitácora (fallos, iteraciones)
│   └── lisp-local.lsp     ← Script AutoLISP (comando LOC)
│
├── n_02-multilinea/   ← (próximo nivel)
└── ...
```

## Estado de decisiones

| Decisión | Estado |
|----------|--------|
| Software de entrada | ✅ AutoCAD (filosofía se traslada a Revit después) |
| Tipo de línea | ✅ Polilínea abierta con offset (multilínea se prueba después) |
| Ancho mínimo puerta | ✅ 0.80 m paso / 0.88 m vano total |
| Marco | ✅ 0.04 m × 0.10 m, dos rectángulos, centrados en espesor muro |
| Apertura | ✅ 90° hacia interior, arco punteado |
| Layer A-MURO | ✅ Continua, blanco, 0.30 mm |
| Layer A-PTA- | ✅ Continua 0.15 mm, rojo (marco/hoja) |
| Arco apertura | ✅ DASHED, RGB 251,251,251, lw 0.05, en A-PTA- |
| Default muro | ✅ 0.15 m (toggle rápido: 0.10, 0.12, 0.15, 0.18, + input libre) |

## Pasos siguientes

1. ✅ Plan creado y revisado
2. ✅ Decisiones técnicas tomadas (tabla arriba)
3. ✅ Crear `00-filo-mvp_01.md` — manifiesto del framework
4. ✅ Crear `01-spec-mvp_01.md` — spec vivo + historial de cambios
5. ✅ `n_01-local/01-spec-n_01.md` — acuerdo macro del nivel
6. ✅ `n_01-local/02-ft-n_01.md` — plan técnico de implementación
7. ✅ `n_01-local/lisp-local.lsp` — script comando LOC (rediseño desde MP)
8. 🔲 Escribir lisp-local.lsp con nuevo algoritmo
9. 🔲 Probar en AutoCAD, iterar
8. 🔲 Probar en AutoCAD, iterar
9. 🔲 Repetir para nivel 2...
