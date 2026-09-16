---
tipo: readme
mvp: 01
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [readme, mvp_01, guia, reglas]
---

# MVP_01 — Guía y Reglas del Framework

Si abrís este proyecto por primera vez, empezá acá.

## Qué es esto

Un **framework de dibujo asistido por IA** que empieza en AutoCAD y está diseñado para trasladarse a Revit, Rhino, Grasshopper, Blender, ComfyUI y cualquier herramienta futura. La idea es simple: **usar lenguaje natural para dibujar arquitectura**, partiendo de la práctica real del estudio (defaults opinados, progresión natural, documentación viva).

## Cómo está organizado

```
MVP_01-dibujo_ia/
│
├── readme-mvp_01.md          ← Este archivo. Puerta de entrada.
├── 00-filo-mvp_01.md         ← Manifiesto (visión, principios, por qué)
├── 01-spec-mvp_01.md         ← Spec viva (acuerdo macro + historial)
├── 02-ft-mvp_01.md           ← Plan técnico global (roadmap, decisiones)
├── 03-log-mvp_01.md          ← Transiciones entre niveles
│
├── n_01-local/               ← Nivel 1 — Local (LOC)
│   ├── 01-spec-n_01.md       ←   Acuerdo macro del nivel (fases A-D)
│   ├── 02-ft-n_01.md         ←   Paso a paso técnico
│   ├── 03-log-n_01.md        ←   Bitácora (fallos, iteraciones)
│   ├── lisp-local.lsp        ←   Código AutoLISP activo (comando `LOC`)
│   └── bak-lisp-local.lsp    ←   Backup pre-modificación
│
├── n_02-.../                 ← Próximo nivel
└── ...
```

## Las 5 piezas del framework

Cada archivo responde una pregunta distinta. El número indica orden conceptual:

| Archivo | Pregunta | Rol | Se lee |
|---------|----------|-----|--------|
| `00-filo-` | **¿Por qué?** | Manifiesto | Para entender el propósito. Solo global. |
| `01-spec-` | **¿Qué logramos?** | Acuerdo macro | Antes de trabajar. Define alcance y criterio de éxito. |
| `02-ft-` | **¿Cómo se hace?** | Plan técnico | Después de spec. Paso a paso para implementar. |
| `03-log-` | **¿Qué falló?** | Bitácora | Durante y después. Fallos e iteraciones. |
| `readme-` | **¿Cómo navego?** | Guía | **Este archivo.** Organización y reglas. |

### Ciclo por nivel

```
1. 01-spec-n_XX.md  → qué queremos lograr
2. 02-ft-n_XX.md    → cómo lo implementamos
3. lisp-*.lsp       → lo escribimos
4. 03-log-n_XX.md   → registramos fallos durante la impl.
```

## Nomenclatura

### Archivos raíz

| Archivo | Rol |
|---------|------|
| `readme-mvp_01.md` | Puerta de entrada |
| `00-filo-mvp_01.md` | Manifiesto |
| `01-spec-mvp_01.md` | Spec viva |
| `02-ft-mvp_01.md` | Roadmap técnico global |
| `03-log-mvp_01.md` | Transiciones entre niveles |

### Dentro de cada nivel `n_XX-*/`

| Archivo | Rol |
|---------|------|
| `01-spec-n_XX.md` | Acuerdo macro del nivel |
| `02-ft-n_XX.md` | Plan técnico paso a paso |
| `03-log-n_XX.md` | Bitácora de fallos e iteraciones |
| `lisp-{nombre}.lsp` | Código AutoLISP activo |
| `bak-lisp-{nombre}.lsp` | Backup del .lsp anterior (se crea antes de modificar uno funcional) |

## Responsabilidades (quién modifica qué)

| Archivo | Quién lo modifica | Cuándo |
|---------|------------------|--------|
| `00-filo-*` | **Solo el usuario o revisión planificada**** | Nunca la IA |
| `01-spec-*` | **Solo el usuario o revisión planificada** | Nunca la IA | Semanal / Quincenal |
| `readme-*` | IA | Cuando haya algo nuevo que un novato deba saber |
| `02-ft-*` | IA | Cada cambio que mofifica al plan |
| `03-log-*` | IA | Cada cambio "raw" crudo |
| `lisp-*.lsp` | IA | Durante iteraciones |
| `bak-lisp-*` | IA | Antes de modificar un lisp funcional |

> `AGENTS.md` es del vault, no del MVP. No mezclar.

## Reglas

1. **Spec es la guía**: se crea primero. Desarrollo nunca se desvía de spec.
2. **Monitor de coherencia**: si hay desvío necesario, se actualiza spec primero.
3. **Subdivisión**: si un nivel crece, avisar antes de subdividir.
4. **Sin subcarpetas**: solo los 4 archivos por nivel.
5. **Un solo `.lsp` activo** por nivel (el que se carga en AutoCAD). Los `.bak-lisp-` son copias de seguridad pre-modificación.
6. **Backup antes de cambiar**: antes de modificar un `lisp-` que funciona, crear `bak-lisp-{nombre}.lsp` (como AutoCAD crea `.bak` al guardar).
7. **Defaults opinados**: muro 0.15m, vano 0.96m (opciones 80→86, 90→96, 100→106 cm), paso mínimo 0.80m, apertura interior. Todo en metros.
8. **Fases progresivas**: A (uniforme) ✅ → B (vano) → C (variable×segmento) → D (puerta completa). Cada fase se valida antes de pasar a la siguiente.

## Cómo probar un `.lsp`

Para cada nivel, el script AutoLISP se prueba en AutoCAD siguiendo estos pasos:

1. **Abrí AutoCAD** con un dibujo nuevo
2. **Cargá el script**: `APPLOAD` → buscá `lisp-{nombre}.lsp` en la carpeta del nivel
3. **Ejecutá el comando**: escribí el comando definido en la barra de comandos (ej: `LOC`)
4. **Seguí los prompts**: punto inicial, punto final, parámetros, etc.
5. **Verificá visualmente**:
   - Layers creados con colores, tipos de línea y espesores correctos
   - Geometría esperada (muros, puertas, marcos, arcos)
   - Overrides de propiedades (DASHED, RGB, lineweight)
6. **Documentá los resultados** en `03-log-n_XX.md`:
   - ✅ Checklists (marcá lo que funciona)
   - ❌ Fallos detectados (describí el comportamiento incorrecto)
   - 💡 Ideas que surjan durante la prueba
7. **Reportá a la IA** para iterar

### Checklist tipo para cualquier nivel

```
- [ ] Comando se ejecuta sin errores
- [ ] Layers se crean automáticamente con parámetros correctos
- [ ] Geometría principal correcta
- [ ] Overrides de propiedades funcionan (linetype, color, lw)
- [ ] Defaults se aplican cuando se omite el input
- [ ] Validaciones funcionan (mínimos, máximos)
- [ ] Variables del sistema se restauran al final
```

## Vinculación con el vault

Cuando un nivel se completa, su conocimiento pasa a `wiki/`. El vault es el repositorio de lo terminado; `proyectos/MVP_01-dibujo_ia/` contiene el proceso en vivo.
