---
name: auditar-documentacion-cad
description: Audita un archivo CAD del estudio contra las reglas del estudio (capas, escalas, referencias externas, unidades, nomenclatura) y devuelve un informe con observaciones clasificadas, dejando el original intacto. Úsala cuando pidan auditar, revisar o controlar un DWG/DXF antes de una entrega.
---

# auditar-documentacion-cad

> Habilidad derivada de los playbooks del estudio: [[proyectos/MVP_02-autocad-standards/readme-mvp_02|MVP_02 estándares AutoCAD]] y [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-01-SET-informe|PB-01 informe SET]]. Herramienta de ejecución: `audit_dwg` del runner.

## Objetivo

Detectar, antes de una entrega, los desvíos que hacen que un plano no sea publicable: escalas de viewport, referencias externas rotas, unidades, nomenclatura de capas y propiedades gráficas.

## Entradas

| Campo | Qué es | Obligatorio |
|---|---|---|
| `file_ref` | referencia del archivo resuelta contra el vault (nunca una ruta libre) | sí |
| `rules_ref` | identificador del juego de reglas (ej. `audit-aiz-v2`) | sí |
| `proyecto` | slug del proyecto | sí |
| `scope` | `completo` o `capas` (lista de capas a revisar) | no |

## Herramientas autorizadas

- `audit_dwg` (runner, perfil local) — nivel **A**, sin aprobación.
- `registry` (escritor único) — para registrar la ejecución y su artefacto.
- `vault` (lectura) — para resolver `file_ref` y las reglas.

**No** uses AutoCAD para modificar nada en esta habilidad. Si el pedido incluye "corregir", cortá acá y pedí aprobación para una tarea de nivel C.

## Precondiciones

1. El archivo está registrado en el registro con su clase (`plano_legal`, `modelo`, etc.).
2. Existe un `rules_ref` versionado. Si no existe, **no inventes reglas**: avisá y pedí cuál.
3. La herramienta `audit_dwg` está disponible en el runner.

## Procedimiento

1. Resolvé `file_ref` contra el vault. Si no resuelve → `file_not_resolvable` y cortá.
2. Registrá la tarea (riesgo A) antes de ejecutar.
3. Pedí el hash del original y **guardalo**: es la prueba de que no lo tocaste.
4. Ejecutá la auditoría contra el juego de reglas `rules_ref`.
5. Clasificá cada observación:
   - **bloqueante** — impide publicar (escala de viewport inexistente, referencia externa rota, unidades mezcladas).
   - **advertencia** — no impide publicar pero se repite en cada entrega (capa sin convención, rótulo desactualizado).
   - **observación** — contexto para quien decide.
6. Escribí el informe como artefacto (nivel B, carpeta de resultados) y asocialo al original con `derived_from`.
7. Cerrá la ejecución con su tiempo y su herramienta.

## Criterios de validación

- El informe nombra **capas y entidades concretas**, no "hay cosas raras".
- Cada bloqueo tiene su corrección propuesta en una frase.
- El hash del original antes y después **es idéntico**.
- La misma entrada con las mismas reglas produce el mismo informe (idempotente por `idem_key`).

## Permisos requeridos

Lectura del archivo y escritura en la carpeta de resultados. **Ninguno** sobre el original.

## Acciones que necesitan aprobación

Ninguna dentro de esta habilidad. Si el pedido incluye corregir, publicar o enviar: eso es una tarea nueva de nivel **C** o **D** y requiere aprobación explícita antes de ejecutarse.

## Formato de salida

1. **Resumen en una línea**: cantidad de bloqueantes, advertencias y observaciones.
2. **Bloqueantes**: capa/objeto · qué falla · corrección propuesta.
3. **Advertencias**: agrupadas por tipo.
4. **Observaciones**: lo que el humano tiene que mirar.
5. **Procedencia**: archivo, versión, hash antes/después, herramienta y versión, reglas aplicadas, tiempo.

## Errores

| Situación | Respuesta |
|---|---|
| El runner no está disponible | `runner_no_disponible` + motivo + qué hacer para habilitarlo |
| Falta el `rules_ref` | `rules_ref_desconocido` + las reglas disponibles |
| El archivo no resuelve | `file_not_resolvable` |
| La auditoría falla a mitad | registrá la ejecución como `failed` con el error real y **no** devuelvas informe parcial como si fuera completo |

## Evidencias que se conservan

- La ejecución en el registro con parámetros, tiempos y herramienta.
- El informe como artefacto con su hash.
- El hash del original antes y después.
- La relación `derived_from` entre el informe y el archivo auditado.
