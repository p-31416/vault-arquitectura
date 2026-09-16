---
tipo: playbook
mvp: 05
version: 1.0.0
fecha_creacion: 2026-07-22
ultima_actualizacion: 2026-07-22
tags: [mvp_05, rhino, mcp, playbook, uso]
---

# Playbook: Rhino MCP — Cómo usar Rhino + Grasshopper desde IA

Guía práctica para arquitectos del estudio. Asume que ya instalaste el plugin (si no, ver [[setup-rhino-mcp]]).

---

## 1. Concepto: ¿qué está pasando?

Rhino MCP crea un puente entre tu asistente IA (Opencode, Claude, Copilot) y Rhino 8. El asistente puede:

- **Ver** lo que hay en tu archivo .3dm (objetos, capas, selecciones)
- **Ejecutar** comandos de Rhino (`_Move`, `_Copy`, `_Layer`, etc.)
- **Crear** geometría desde prompts textuales
- **Modificar** propiedades (capas, colores, materiales)
- **Construir** definiciones de Grasshopper desde cero

No reemplaza al arquitecto. Reemplaza los clics repetitivos.

---

## 2. Conexión rápida (si ya instalaste)

Solo dos pasos:

1. En Rhino 8, ejecutá el comando `MCPConnect`
2. Copiá el prompt que aparece y pegalo en tu asistente IA

Listo. Ya podés hablarle a Rhino.

---

## 3. Flujo de trabajo recomendado

### Paso 1: Pedile al asistente que explore el archivo

```
"Decime qué hay en este archivo de Rhino"
```

El asistente ejecuta `get_scene_summary` y te devuelve: cantidad de objetos, capas existentes, tipo de geometría.

### Paso 2: Dále instrucciones concretas

Sé específico. En lugar de "arreglá este modelo", decí:

```
"Tomá todos los objetos de la capa Default y movelos a la capa MUEBLES.
Después seleccioná los círculos y hacé una copia desplazada 5 metros en X."
```

### Paso 3: Iterá sobre el resultado

```
"Ahora cambiale el color a la capa MUROS por gris claro.
Y agrupá todas las líneas que están sueltas en un solo grupo."
```

### Paso 4: Pedí geometría paramétrica (Grasshopper)

```
"Creá una definición de Grasshopper que genere una torre retorcida.
Que tenga sliders para altura, número de pisos y ángulo de torsión."
```

---

## 4. Catálogo de prompts útiles

### Lectura del modelo

| Prompt | Qué hace |
|--------|----------|
| "Qué hay en este archivo?" | Resumen de escena (objetos, capas) |
| "Mostrame las capas" | Lista capas con colores y visibilidad |
| "Qué objetos están seleccionados?" | Info de la selección actual |
| "Cuántos objetos hay en la capa MUROS?" | Filtro por capa |

### Creación de geometría

| Prompt | Qué hace |
|--------|----------|
| "Creá un círculo de radio 5 en el origen" | Círculo en 0,0,0 |
| "Dibujá una línea de 0,0 a 10,10" | Línea recta |
| "Hacé un rectángulo de 20x10" | Rectángulo desde origen |
| "Creá una caja de 10x10x10" | Caja (extrusión) |
| "Modelá esta imagen en 3D" | Modelado desde imagen (referencia) |

### Edición y organización

| Prompt | Qué hace |
|--------|----------|
| "Mové todos los círculos a la capa CIRCULOS" | Reorganiza capas |
| "Copiá la selección 5 metros en X" | Duplica y desplaza |
| "Rotá el grupo 45 grados en Z" | Rotación |
| "Escalá todos los objetos de la capa MOBILIARIO al 50%" | Escala uniforme |
| "Asigná cada objeto a una capa apropiada" | Organización automática |

### Grasshopper

| Prompt | Qué hace |
|--------|----------|
| "Creá una definición que genere una fachada paramétrica" | GH definition desde prompt |
| "Agregále un slider de altura" | Modifica definición existente |
| "Exportá la definición a un archivo" | Guarda .gh en disco |

---

## 5. Ejemplos del mundo real (estudio de arquitectura)

### Escenario A: Organizar un modelo recibido de un colaborador externo

```
Prompt:
"Acabo de importar un modelo de SketchUp que viene todo en Default.
Tomá el modelo, analizá los objetos, y creá capas lógicas:
- MUROS para superficies verticales grandes
- LOSAS para superficies horizontales
- COLUMNAS para elementos lineales verticales
- VENTANAS para aberturas
Asigná cada objeto a su capa y ponele colores distintivos."
```

### Escenario B: Generar variantes de un partido formal

```
Prompt:
"En este modelo hay una curva spline que define la fachada principal.
Copiala 3 veces, escalá cada copia 80%, 60% y 40%,
y movelas 10 metros en Y para tener 4 opciones visibles."
```

### Escenario C: Preparar un archivo para exportar a Revit

```
Prompt:
"Antes de exportar, asegurate de que:
1. Todos los muros estén en capa MUROS (color gris)
2. Todas las losas en capa LOSAS (color azul claro)
3. No haya objetos en Default
4. Todo esté agrupado por tipo
5. Eliminá las geometrías duplicadas"
```

### Escenario D: Fachada paramétrica rápida

```
Prompt:
"Creá una definición de Grasshopper que divida una superficie rectangular
en una grilla de paneles. Cada panel debe poder variar su profundidad
con un atractor de puntos. Usá sliders para:
- Cantidad de divisiones en U y V
- Profundidad máxima del panel
- Radio del atractor"
```

---

## 6. Buenas prácticas

### HACÉ

- **Sé específico**: en lugar de "ordená esto", decí "poné todos los círculos en capa CIRCULOS"
- **Iterá de a poco**: un cambio por paso, verificá, seguí
- **Usá nombres de capa que ya existen**: el asistente puede listarlas primero
- **Pedí confirmación**: "mostráme qué cambiarías antes de hacerlo" (si el asistente soporta el modo)
- **Verificá visualmente**: mirá Rhino después de cada operación importante

### NO HAGAS

- **No pidas todo junto**: "ordená, modelá, renderizá, exportá" en un solo prompt — el asistente se confunde
- **No asumas que vio algo que no seleccionaste**: si seleccionaste objetos en Rhino, el asistente no lo sabe automáticamente. Pedile que seleccione.
- **No dejes Rhino abierto sin uso**: si crashea, el asistente lo detecta y puede reiniciarlo
- **No uses Rhino 7**: el plugin requiere Rhino 8+

---

## 7. Integración con el vault

### Guardar resultados exitosos

Cuando generes algo útil (una definición de GH, un script, un modelo organizado):

```
"Exportá esta definición a activos/proyectos/<proyecto>/grasshopper/definicion.gh"
```

### Documentar en la wiki

Después de un workflow exitoso, crear entrada en:
- `wiki/glosario/software/rhino/` — tips y configuraciones
- `wiki/glosario/software/rhino/ejemplos/` — prompts probados con resultados

### Combinar con MVP_04 (ComfyUI)

Flujo completo:

```
1. Tomá un croquis del vault → ComfyUI genera render de referencia
2. Usá el render como guía → Rhino MCP modela la geometría base
3. Iteración: "cambialo a esto" → el agente modifica el modelo
4. Exportá a formato para Revit (BIM)
```

---

## 8. Troubleshooting rápido

| Síntoma | Causa probable | Solución |
|---------|---------------|----------|
| "No veo Rhino" | Plugin no instalado o MCP desconectado | Ejecutá `MCPConnect` de nuevo |
| "Hizo algo pero no lo veo" | Geometría lejos del origen | `Zoom → Extents` en Rhino |
| "Dice que hizo pero no pasó nada" | Capa oculta o freeze | Revisá el panel de capas |
| Rhino crashea | Prompt muy complejo o bug | Reiniciá Rhino y simplificá el prompt |
| Grasshopper no funciona | GH2 requiere Rhino 9 | Usá `gh_` tools en vez de `gh2_` |
| El asistente no encuentra objetos | No se los mostraste | Primero pedí `get_scene_summary` |

---

## 9. Referencias

- Documentación oficial: https://mcneel.github.io/RhinoMCP/
- GitHub / Issues: https://github.com/mcneel/RhinoMCP
- Foro AI + Rhino: https://discourse.mcneel.com/c/rhino/artificial-intelligence-rhino/162
- Rhino 8 download: https://www.rhino3d.com/download

---

## 10. Checklist de uso diario

- [ ] Rhino 8 abierto con el modelo cargado
- [ ] `MCPConnect` ejecutado al inicio de la sesión
- [ ] Asistente conectado (verificá con "qué ves en el archivo?")
- [ ] Trabajás por pasos: leer → modificar → verificar
- [ ] Cambios importantes guardados en .3dm antes de cada prompt complejo
- [ ] Resultados exportados a `activos/` si corresponde
