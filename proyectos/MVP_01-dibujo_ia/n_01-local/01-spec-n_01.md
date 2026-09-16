---
tipo: spec
nivel: n01
nombre: local
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [spec, n01, local, muro, puerta]
---

# Spec n01 — Local (LOC)

## Propósito

Dibujar un **local arquitectónico** (habitación cerrada) con muros y una puerta. El usuario dibuja una polilínea cerrada del espacio interior, los muros se generan por offset exterior, y se marca dónde va la puerta.

## Comando

`LOC` (de "local")

## Fases

El spec se desglosa en fases progresivas. Cada fase se completa y valida antes de pasar a la siguiente.

### Fase A — Muro uniforme automático ✅

| Desde | Hasta |
|-------|-------|
| Usuario dibuja polilínea cerrada | Offset exterior uniforme 0.15 m generado |

**Flujo:**
1. Usuario dibuja polilínea cerrada del interior del local (clics + `C` para cerrar)
2. El script detecta automáticamente el lado exterior (opuesto al centroide)
3. Offset uniforme de 0.15 m hacia el exterior
4. La polilínea original se conserva (cara interior del muro)
5. El offset queda en `A-MURO`

**Sin preguntas intermedias.** Un solo comando, muro completo.

### Fase B — Vano (actual)

| Desde | Hasta |
|-------|-------|
| Muro generado (Fase A) | Vano cortado en ambas caras, puntas conectadas |

**Flujo:**
1. Después del offset, el script pregunta: _*"Agregar vano? [S/N] <S>"*_
2. **S** → usuario cliquea un punto del muro donde va la abertura
3. Selecciona medida: 80 / 90 / 100 (corresponde a vano de 86 / 96 / 106 cm, incluyendo 3 cm por lado para futuro marco)
4. El script calcula el punto centrado en el clic sobre cada polilínea (interior y exterior)
5. Aplica `_break` con `_F` (first point) en ambas polilíneas, abriendo un vano de ancho `doorWidth + 6` centrado en el punto clicado
6. Une las puntas abiertas correspondientes con segmentos de línea (corte de muro en planta)
7. **N** → el comando termina sin vano

**Medidas de vano:**
| Opción | Vano total | Marco futuro (3 cm c/lado) | Luz de paso |
|--------|-----------|---------------------------|-------------|
| 80     | 0.86 m    | 0.03 + 0.03               | 0.80 m      |
| 90     | 0.96 m    | 0.03 + 0.03               | 0.90 m      |
| 100    | 1.06 m    | 0.03 + 0.03               | 1.00 m      |

**Justificación:** centrada. El punto clicado es el centro del vano.

### Fase C — Muro por segmento con selección visual (siguiente)

| Desde | Hasta |
|-------|-------|
| Polilínea cerrada dibujada | Cada segmento con su espesor, offset individual, esquinas limpiadas con fillet R=0 |

**Flujo:**
1. Usuario dibuja polilínea cerrada del interior
2. El script pregunta: *"¿Mismo espesor para todos los segmentos? [S/N] <S>:"*
   - **S** → offset uniforme automático (como Fase A)
   - **N** → entra al flujo interactivo por segmento:
3. Se explota la polilínea → cada segmento es una entidad independiente (línea)
4. El script itera sobre cada segmento:
   - **Ilumina** el segmento actual (lo resalta visualmente)
   - Pide al usuario: *"Marque el segmento con clic"* (confirmación visual)
   - Muestra el selector de espesor junto al cursor: `[0.10/0.12/0.15/0.18] <0.15>`
   - Guarda el espesor y aplica offset exterior a ese segmento
5. Una vez procesados todos los segmentos, se aplica `_fillet R=0` entre adyacentes
6. Se eliminan las líneas originales (explotadas)

**Defaults de espesor:**
- 0.15 m (default general)
- Toggles rápidos: 0.10, 0.12, 0.15, 0.18 m
- Input libre: cualquier valor positivo

### Fase D — Puerta completa con marco y hoja (futuro)

| Desde | Hasta |
|-------|-------|
| Vano generado (Fase B) | Puerta insertada con marco y hoja |

(Se define cuando Fase C esté estable)

## Incluye

- Polilínea cerrada del espacio interior (usuario la dibuja) ✅
- Offset exterior automático (Fase A: uniforme 0.15; Fase C: por segmento) ✅ Fase A
- Vano con `_break` y conexión de puntas (Fase B) ✅ implementado
- Default de espesor: 0.15 m, toggles 0.10/0.12/0.15/0.18, input libre
- Layers estándar: `A-MURO` (continuous/white/0.30mm), `A-PTA-` (continuous/red/0.15mm)
- Puerta (Fase D):
  - Ancho mínimo de paso: 0.80 m
  - Vano total: 0.88 m (0.80 + 0.03 + 0.03 + holgura)
  - Marco: dos rectángulos 0.04×0.10 m centrados en espesor del muro
  - Hoja: abre 90° hacia el interior
  - Arco de apertura: DASHED, RGB 251,251,251, lw 0.05mm

## Excluye

- Encuentros entre locales (se resuelve después)
- Ventanas, vanos, mobiliario
- Cotas, anotaciones, escalas

## Principios de diseño

1. El usuario dibuja el interior del local → los muros se generan hacia afuera
2. Fases progresivas: uniforme → vano → variable → puerta completa
3. Siempre que se pueda, se usan comandos nativos de AutoCAD (`_pline`, `_offset`, `_break`) en vez de calcular la geometría en LISP
4. Los defaults son opinados (0.15 m, vano 90 → 0.96 m) pero overrideables

## Criterio de éxito

**Fase A:** `LOC` produce muro offset 0.15 m uniforme, capa correcta, sin input intermedio. ✅
**Fase B:** `LOC` permite agregar vano centrado con clic + medida, break en ambas caras, puntas conectadas.
**Fase C:** `LOC` permite definir espesor por segmento mediante clic + selector visual.
**Fase D:** `LOC` produce local completo con muros variables + puerta correcta.
