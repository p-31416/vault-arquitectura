---
tipo: especificaciones
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [especificaciones, framework, vivo]
---

# Especificaciones del Framework

Documento VIVO. La sección superior es la especificación actual del framework en su último nivel. Las secciones inferiores registran la evolución nivel a nivel.

---

## Nivel 01 — Muro + Puerta (ACTUAL)

### Entrada del usuario

| Parámetro | Default | Opciones |
|-----------|---------|----------|
| Punto inicial (A) | — | Pick en pantalla |
| Punto final (B) | — | Pick en pantalla |
| Centro de puerta (P) | — | Pick sobre la línea del muro |
| Espesor de muro | 0.15 m | 0.10, 0.12, 0.15, 0.18, o input libre |
| Lado de apertura | Interior | Clic del lado interior |
| Ancho de vano | 0.88 m | Mínimo 0.80 m paso |

### Geometría del muro

1. Polilínea abierta de A a B (eje) en `A-MURO`
2. Offset bidireccional de ±(espesor/2) para caras del muro
3. Las caras se rompen en el vano de la puerta

### Geometría de la puerta

```
<-- 0.88 m (vano total) -->
<-- 0.03 --><-- 0.82 --><-- 0.03 -->
[ marco ]  [ hoja 0.80 paso ]  [ marco ]
```

| Elemento | Medida | Nota |
|----------|--------|------|
| Ancho mínimo de paso | 0.80 m | Libre una vez abierta |
| Vano total entre muros | 0.88 m | 0.80 + 0.03 + 0.03 + holgura |
| Marco (cada lado) | 0.04 m x 0.10 m | Rectángulo centrado en espesor |
| Hoja de puerta | ~0.82 m | Se dibuja abierta a 90° |

**Marco**: dos rectángulos de 0.04 m x 0.10 m en extremos del vano, centrados en el espesor del muro. Capa `A-PTA-`.

**Hoja**: línea desde bisagra (borde interior del marco) que gira 90° hacia el interior. Longitud = ~0.82 m.

**Arco de apertura**: desde carpintería interior hasta punta de la puerta. Dibujado en `A-PTA-` con override: DASHED, RGB 251,251,251, lw 0.05 mm.

### Layers

| Layer | Tipo línea | Color | Espesor | Uso |
|-------|------------|-------|---------|-----|
| `A-MURO` | Continua | Blanco (7) | 0.30 mm | Eje y caras de muro |
| `A-PTA-` | Continua | Rojo (1) | 0.15 mm | Marco, hoja. Arco: override DASHED/RGB 251,251,251/lw 0.05 |

### Secuencia de dibujo (AutoLISP)

1. Pedir punto A, punto B
2. Dibujar polilínea eje A-B en A-MURO
3. Offset bidireccional = espesor/2
4. Pedir punto P sobre la línea (o ingresar distancia desde A)
5. Calcular vano (default 0.88 m), centrarlo en P
6. Romper segmento de muro en el vano
7. Dibujar marco (2 rectángulos 0.04x0.10) en A-PTA-
8. Dibujar hoja de puerta (línea a 90° interior) en A-PTA-
9. Dibujar arco de apertura en A-PTA- (override: DASHED, 251,251,251, lw 0.05)
10. Verificar que el paso mínimo sea >= 0.80 m

### Implementación

| Archivo | Propósito |
|---------|-----------|
| `n_01-local/01-spec-n_01.md` | Acuerdo macro del nivel (local, muros por segmento, puerta) |
| `n_01-local/02-ft-n_01.md` | Plan técnico de implementación |
| `n_01-local/03-log-n_01.md` | Bitácora de fallos e iteraciones |
| `n_01-local/lisp-local.lsp` | Script AutoLISP, comando `LOC` |

---

## Historial de cambios

### De 00 → Nivel 01 (creación)

- Geometría base: polilínea abierta + offset bidireccional
- Puerta: vano 88 cm, marco 4x10 centrado en espesor, hoja a 90° interior
- Capa A-MURO: continuous, blanco, 0.30 mm
- Capa A-PTA-: continuous, rojo, 0.15 mm (marco, hoja, arco)
- Arco apertura en A-PTA- con override: DASHED, RGB 251,251,251, lw 0.05 mm
- Dirección de apertura determinada por clic del usuario (lado interior)
- Implementado en AutoLISP, comando `MP`
- Manifiesto en [[proyectos/MVP_01-dibujo_ia/00-filo-mvp_01|00-filo-mvp_01]]
- Pivote de n_01-muro_puerta a n_01-local: el comando MP se reemplaza por LOC (local cerrado con muros concéntricos)
