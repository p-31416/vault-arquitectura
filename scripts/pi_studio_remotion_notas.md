---
tipo: software
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [pi, remotion, motion-design, tutorial, studio-os]
idioma: es
---

# Notas de lectura — composición `PIStudioOS`

El video se implementa como React + TypeScript (`.tsx`) porque Remotion compone cada fotograma desde componentes React. Estas notas acompañan `P:\00-repos\remotion-vault\src\PIStudioOS.tsx`; la auditoría didáctica en Python está en [[scripts/auditar_presentacion_pi_notas|auditar_presentacion_pi_notas]].

## Cómo mirar la vista previa y exportar

Desde `P:\00-repos\remotion-vault`:

```powershell
npm run lint
npm run dev
```

Remotion Studio abre las composiciones en el navegador; elegí `03-PIStudioOS`. Para exportar el MP4:

```powershell
npx remotion render src/index.ts 03-PIStudioOS out/PIStudioOS.mp4
```

## Mapa de lectura del TSX

| Líneas | Bloque | Para qué sirve |
|---:|---|---|
| 1–28 | Imports, duración, paleta y curva de movimiento | Reutiliza tokens del proyecto y fija 1920×1080 a 30 fps por el registro global en `Root.tsx`. |
| 30–64 | `revelar`, `progresoTrazo`, `Trazo` | Funciones puras: dado un frame, calculan cuánto aparece un texto o cuánto se ha dibujado una línea. |
| 66–165 | `Plano`, `Encabezado`, `Etiqueta` | Fondo de retícula, jerarquía tipográfica y rótulos comunes. |
| 168–222 | `Persona`, `Computadora`, `Nodo` | Pictogramas SVG provisionales y cajitas de servicio (VPS/tarea); el boceto original puede reemplazar las figuras. `Nodo` dibuja las dos tarjetas de la escena holoarquitecto. |
| 224–266 | `Flecha` | Dibuja conexiones por trazo y revela la punta al final; cada marcador tiene ID propio para que las ramas se mantengan diferenciadas. |
| 268–296 | `BaseEscena` | Monta el fondo, el título y el pie de página compartidos. |
| 298–319 | `EscenaPI` | Presenta PI y la relación arquitecta–computadora. |
| 320–340 | `EscenaUnoAUno` | Anima el ciclo de ida y vuelta: el próximo paso espera atención humana. |
| 341–380 | `EscenaMetaArquitecto` | 4–6 sesiones, herramientas de desarrollo y la secuencia reportes → wiki → mantenimiento. |
| 381–419 | `EscenaPersistente` | Flujo holoarquitecto: brief → perfil/asistente → Hermes compartido → plan → roles → evidencia → revisión → skill aprobada. Incluye la distinción de gateway disponible 24/7 vs ejecución por demanda/agenda. |
| 420–454 | `EscenaFractal` | Cinco roles, cada uno con lenguaje/capacidad (AutoLISP, Python/GH, Comfy JSON/API, Fathom/Markdown, n8n/Leantime) y ejemplos del vault. |
| 455–486 | `EscenaRecursos` | Sobre de tarea enruta a local, VPS o GPU cloud; añade datos, licencias, permisos y costo de mantenimiento. |
| 487–527 | `EscenaComfy` | Texto, imagen, video y voz llegan a un workflow; salida registra procedencia y revisión. |
| 528–562 | `EscenaCierre` | Cierra en el Meta-arquitecto: fórmula, transferencia senior, trabajo aprobado, costo y mantenimiento. No termina en el arquitecto usuario. |
| 563–599 | `ESCENAS`, duración total y composición | Suma duraciones y resta el solape de las transiciones para calcular el render exacto. |

## Cómo se sincroniza el movimiento

`useCurrentFrame()` entrega el fotograma actual. `interpolate()` traduce un intervalo de fotogramas a opacidad, desplazamiento o `strokeDashoffset`. Como Remotion puede pedir cualquier fotograma sin renderizar los anteriores, no se usa un reloj del navegador ni `setTimeout`.

`ESCENAS` guarda duración, nombre y componente. `TransitionSeries` los enlaza con transiciones; `duracionPIStudioOS()` calcula `suma de escenas − (cantidad de transiciones × duración de transición)`. El registro de la composición vive en `Root.tsx` con ID `03-PIStudioOS`.

## Alcance visual

- Los flechines representan dirección y no causalidad automática: cada tarea se registra, se ejecuta en un recurso y retorna para revisión.
- La rama 24/7 describe disponibilidad del gateway; GPU y agentes trabajan según agenda o demanda.
- «Cinco líneas de trabajo potenciales» comunica paralelismo ilustrativo; no es una medición de rendimiento ni un compromiso de productividad.
- Los trazos son vectoriales temporales hasta integrar el mini guion dibujado por Sol.
