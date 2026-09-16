---
tipo: log
mvp: 01
fecha_creacion: 2026-06-30
tags: [log, mvp_01, transiciones]
---

# Log Global MVP_01

Registro de transiciones entre niveles del MVP. Se actualiza cuando se completa un nivel y se define el siguiente.

## Nivel 00 → Nivel 01

### Fecha
2026-06-30

### Transición
Creación del MVP. Nivel 01 (Muro + Puerta) definido e implementado.

### Logros
- Geometría base: polilínea abierta + offset bidireccional (default 15cm)
- Puerta: vano 88cm, marco 4x10 centrado en espesor, hoja a 90° interior
- Layers estándar: A-MURO (continuous/white/0.30mm), A-PTA- (continuous/red/0.15mm)
- Arco de apertura en A-PTA- con override DASHED/251,251,251/lw 0.05mm
- Comando `MP` implementado en AutoLISP

### Aprendizajes
- A-MURO no debe ser DASHED (solo el arco lleva ese tipo de línea)
- El nombre A-PUER no seguía el estándar → A-PTA-
- El arco necesita lw 0.05mm y color 251,251,251 para verse bien al plotear
- `break` es menos predecible que dibujar dos segmentos separados para el vano

### Pendientes para n02
- Probar en AutoCAD (validación visual)
- Verificar ltscale para tipo DASHED del arco
- Decidir si el eje del muro va a Defpoints o capa congelada
