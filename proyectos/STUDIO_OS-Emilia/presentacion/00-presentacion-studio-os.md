---
tipo: presentacion
fecha_creacion: 2026-08-27
ultima_actualizacion: 2026-08-27
tags: [presentacion, studio-os, emilia-pimenta, pitch]
idioma: es
estado: borrador
formato: marp / obsidian-slides / pptx
---

# STUDIO OS — Sistema operativo para el estudio de arquitectura

> Arquitectura del estudio aumentado

**Propuesta para Emilia Pimenta — Resumen conceptual para reunión**

---

<!-- SLIDE 1 — PORTADA -->
# STUDIO OS

### Sistema operativo para el estudio de arquitectura

**Arquitectura del estudio aumentado**

> "No vengo a incorporar herramientas al estudio. Vengo a entender cómo funciona y a diseñar el sistema que conecta lo que ya hacen con las nuevas capacidades tecnológicas."

Emilia Pimenta × Sol — Agosto 2026

*Nota visual: fondo croquis + render, tipografía limpia, sin tecnicismos*

---

<!-- SLIDE 2 — TESIS -->
## La oportunidad

### 4ta Revolución Industrial → trabajo intelectual

En arquitectura, la oportunidad **no es convertirse en técnico**.

Es **aumentar la capacidad del arquitecto** sin quitarle el control.

La arquitecta sigue pensando con:
croquis · referencias · conversación · intuición · experiencia

**La tecnología se incorpora *alrededor* de ese proceso.**

---

<!-- SLIDE 3 — IDEA CENTRAL -->
## La propuesta no es "implementar IA"

Es **analizar y rediseñar el flujo de trabajo** del estudio

para conectar:

**personas ↔ información ↔ herramientas ↔ automatizaciones ↔ IA**

No sumamos herramientas aisladas.
**Diseñamos circulaciones.**

---

<!-- SLIDE 4 — MAPA DE INTERVENCIÓN HUMANA -->
## Principio clave

### Mapa de intervención humana

Cada proceso se analiza para decidir qué hace cada capa:

| Capa | Hace |
|------|------|
| **HUMANO** | decide · interpreta · evalúa · corrige |
| **IA** | genera · transforma · clasifica · propone |
| **AUTOMATIZACIÓN** | transporta · registra · ordena · dispara |
| **INFORMACIÓN** | croquis · imágenes · referencias · modelos · documentos · datos |

> **Pregunta central:** ¿Dónde aporta valor la intervención humana y dónde podemos eliminar traducciones innecesarias?

---

<!-- SLIDE 5 — ARQUITECTO AUMENTADO -->
## Del arquitecto analógico al arquitecto aumentado

| Se conserva | Se agrega |
|-------------|-----------|
| criterio | memoria |
| intención | búsqueda semántica |
| sensibilidad | automatización |
| experiencia | IA · agentes |
| decisión arquitectónica | representación · datos · infraestructura local |

> **"El objetivo no es digitalizar al arquitecto. Es aumentar su capacidad sin quitarle el control sobre la arquitectura."**

---

<!-- SLIDE 6 — EJEMPLO REPRESENTACIÓN -->
## Ejemplo concreto: representación

**Flujo tradicional:**
```
Arquitecta → explicación → junior → interpretación → modelado → render → arquitecta → corrección → junior → nuevo modelado
```
*Muchas traducciones. Pérdida de intención. Tiempo.*

**Flujo aumentado:**
```
Arquitecta → croquis + materiales + referencias → sistema IA → representación → arquitecta → criterio → iteración
```

**Resultado:** menos tiempo · menos pérdida de intención · mayor control · mayor capacidad de iteración

*Visual sugerida: dos líneas de tiempo comparadas, la segunda mucho más corta*

---

<!-- SLIDE 7 — TELEGRAM + COMFYUI -->
## La interfaz puede ser simple

**La complejidad técnica queda detrás de una interfaz cotidiana.**

La arquitecta envía por **Telegram**:
croquis + imagen + indicación de voz/texto

Por detrás:
```
Telegram → agente → interpretación → workflow ComfyUI
→ control de profundidad/geometría → materialidad → modelo especializado
→ generación → resultado enviado de vuelta a Telegram
```

No hay que aprender un software nuevo.
**Se usa lo que ya usan, potenciado.**

*Demo en vivo posible: croquis → 2 min → 4 variantes fotorrealistas*

---

<!-- SLIDE 8 — IA PRIVADA -->
## IA privada

**Infraestructura existente, subutilizada.**

El estudio ya tiene **GPUs de 24 GB**. Hoy no se aprovechan.

Objetivo: construir **capacidad de IA privada**
→ control sobre datos, modelos, workflows y propiedad intelectual

- No hace falta entrenar un modelo gigante desde cero
- Se combinan: modelos base + conocimiento privado + workflows propios + modelos especializados (LoRA)
- Los croquis y planos **no salen del estudio**

*Ver [[wiki/estudio/decision-arquitectura-ia-privacidad|Decisión arquitectura IA y privacidad]] y [[wiki/glosario/referentes/ia-estudios-internacionales|IA en estudios internacionales]]*

---

<!-- SLIDE 9 — EL PLANO DEL ESTUDIO -->
## El "plano" del estudio

**Representar el estudio como una arquitectura.**

No son herramientas sueltas. Son **ambientes conectados por circulaciones de información.**

```
[1] ENTRADA / VISIBILIDAD          [6] OBRA
    web · redes · referencias          libro digital · fotos · incidencias
           ↕                                      ↕
[2] CLIENTES  â†——→  [3] DISEÑO  â†——→  [4] REPRESENTACIÓN  â†——→  [5] PROYECTOS
    CRM · reuniones     croquis · CAD/BIM/Rhino      ComfyUI · video      tareas · entregables
           ↕               ↕                                      ↕               ↕
[7] ADMINISTRACIÓN  â†——→  [8] PROVEEDORES  â†——→  [9] MEMORIA / CONOCIMIENTO
    honorarios · contratos    contactos · precios      grafo · búsqueda semántica
```

> **La clave visual son las CIRCULACIONES** — no mostrar solo herramientas, sino cómo circula la información.

*Visual sugerida: planta arquitectónica con 9 ambientes y flechas de circulación, estilo diagrama BIG/OMA*

---

<!-- SLIDE 10 — GRAFO DE CONOCIMIENTO -->
## Cada proyecto alimenta la memoria

**Del archivo aislado al grafo conectado.**

```
material → proyecto → detalle → plano → proveedor → precio → fotografía → decisión → resultado
```

**Consulta posible (búsqueda semántica):**
> "Mostrame proyectos donde usamos hormigón visto y qué proveedores utilizamos."

El conocimiento deja de estar encerrado en carpetas aisladas.
**Se vuelve consultable, reutilizable, acumulativo.**

*Visual: grafo de nodos interconectados, similar a Obsidian Graph View*

---

<!-- SLIDE 11 — LIBRO DIGITAL + ASISTENTE -->
## Obra y día a día, sin fricción

**Libro digital de obra:**
Foto desde celular / Telegram → identificación automática de proyecto → fecha → ubicación → incidencia → registro en carpeta correspondiente

*La fotografía cotidiana se convierte en información estructurada.*

**Asistente del estudio (voz/chat):**
- ¿Qué reuniones tengo hoy?
- ¿Qué clientes están activos?
- ¿Qué presupuestos están pendientes?
- ¿Qué tengo que cobrar?
- ¿Qué quedó pendiente de la reunión?
- ¿Qué proveedores usamos para este material?
- ¿Qué proyectos anteriores sirven como referencia?

---

<!-- SLIDE 12 — WEB + CRM -->
## La entrada también es parte del sistema

```
web → consulta → calificación → CRM → reunión → propuesta → seguimiento → proyecto
```

Captar y gestionar clientes **dentro del mismo ecosistema**, no en herramientas desconectadas.

- Web y redes → visibilidad
- Formulario / WhatsApp / mail → captura
- CRM → seguimiento y pipeline
- Propuesta → vinculada a honorarios y contratos

Todo trazable. Todo en un mismo lugar.

---

<!-- SLIDE 13 — DISEÑO ADAPTADO -->
## Diseño adaptado al arquitecto

**No imponer software.**

Primero entendemos cómo diseña *este* estudio:
croquis · imágenes · referencias · modelado básico · CAD · BIM · Rhino/Grasshopper

Después definimos el **pipeline adecuado.**

ComfyUI funciona como **línea transversal de representación** — se adapta a cualquier punto de partida.

---

<!-- SLIDE 14 — SPRINT 30 DÃAS -->
## Implementación inicial: Sprint de 30 días

**9 pasos en 30 días:**

1. Relevamiento del estudio
2. Mapa completo de procesos
3. Auditoría tecnológica y de infraestructura
4. Identificación de oportunidades
5. Arquitectura del ecosistema
6. Selección de un proyecto real
7. Prototipo de representación con IA local
8. Demo del resultado
9. Roadmap de implementación por prioridades

> **No es un "diagnóstico".**
> Es *"30 días para entender el estudio, descubrir qué capacidad ya existe dentro de él y construir un primer prototipo funcionando."*

---

<!-- SLIDE 15 — VALOR Y MODELO -->
## Valor y modelo de negocio

**Sprint 30 días: USD 600**

- Fee acreditable a la primera etapa si se avanza
- Entregables: mapa de procesos + arquitectura del ecosistema + prototipo funcionando + roadmap priorizado

**Después del sprint:**

| Fase | Descripción |
|------|-------------|
| **Fase 2** | Implementación modular (por prioridades) |
| **Fase 3** | Soporte y evolución mensual |
| **Futuro** | Componentes reutilizables PI Studio OS para otros estudios |

**Métricas de impacto:**
tiempo de búsqueda · tiempo de representación · traducciones/intermediarios · tareas repetitivas · tiempo administrativo · velocidad de respuesta · retrabajo · recuperación de conocimiento · utilización de infraestructura

---

<!-- SLIDE 16 — CIERRE -->
## Cierre

### STUDIO OS

> "El objetivo no es digitalizar al arquitecto. Es aumentar su capacidad sin quitarle el control sobre la arquitectura."

**Próximo paso: Sprint de 30 días**

¿Agendamos el relevamiento?

---

**Subtítulos posibles para Studio OS:**
- Arquitectura del estudio aumentado
- Infraestructura intelectual para estudios de arquitectura
- Del estudio aislado al estudio conectado
- Del arquitecto analógico al arquitecto aumentado

*Contacto: Sol — [mail/tel] — Vault / demos en vivo*
