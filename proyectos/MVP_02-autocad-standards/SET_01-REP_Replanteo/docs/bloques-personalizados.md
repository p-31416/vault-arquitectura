---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, autocad, bloques, atributos, dinamico]
origen_medicion: G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg (ODA-a-DXF + ezdxf)
estado: v0.1
---

# Bloques personalizados del estudio — uso, estados y escalas

> Sector exclusivo de bloques, aparte del playbook de replanteo ([[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques|REP-ARAOZ-capas-bloques]]). Wiki intacta.
> Medición base: §2 de ese doc (13 nombrados, 208 INSERTs).

## 1. Regla madre: los bloques no se explotan

Explotar (`DESCOMPONER`) rompe el sistema: se pierden atributos (adiós `DATAEXTRACTION` y cómputos), parámetros dinámicos y `WIPEOUT`, y cada vano pasa a ser líneas sueltas fuera de norma. Corrección: `DESHACER` inmediato + `SINCRATR` si hubo redefinición.

## 2. Catálogo

| Bloque | Capa inserción | Punto inserción | Atributos | Ejemplares |
|---|---|---|---|---|
| `VENTANA BAJA SIMPLE` | `A-CARP-02` | Centro del vano | `TIPO`, `ANCHO` (h 0.06, `SIMB-CARP`); futuro: `H_ALFEIZAR/H_COLOCACION`, `H_VENTANA` | 20 (16 variantes) |
| `PUERTA BATIENTE` | `A-CARP-02` | Eje de apertura | `ANCHO`, `PUERTA`, `ALFEIZAR`, `ALTURA`, `DESCRIPCION` | 22 (12 variantes) |
| `SIMB-MURO` | `SIMB-MURO` | Centro del tag | `MURO` (def `M0`, h 0.10) | 89 |
| `SIMBOLO DE EJE` | `E-EJES` | Cruce de ejes | `EJE` (h 0.25) | 20 |
| `SIMBOLO NIVEL PISO CORTE` | `A-SIMBOLO-NPT-PLANTA` | Punto de nivel | `NPT`, `DESCRIPCION`, `Nº` | 29 |
| `C40.20` | `E-COL` / `A-COTA-1-50` | Centro columna | — | 26 |
| `Tabela_Esquadrias` | paper/detalle | Esquina tabla | vía `MTEXT` | 1 |
| Carátula `G-CART-MEPA` | `ROT-*` (paper) | Esquina inferior derecha (IRAM 4508) | 7 + `ESCALA` con `CAMPO` al viewport | 1 por lámina |

## 3. Posiciones y escalas

- Inserción al centro en vanos y tags: funciona en todas las escalas y fija el acotado (vanos a ejes, mampostería a filos).
- Estados por escala (backlog, §16 del doc madre): `SIMB-REP` (símbolo mínimo) → `50` (detalle medio + cota) → `100+DETALLE` (atributos hoy ocultos visibles). Cada estado amplía información sin cambiar el bloque.
- Textos anotativos `EP-2.5/EP-3.5`; en bloques, `ATTDEF` con altura 0 donde manda la definición.

## 4. Tag siempre horizontal (giro 0) en bloque que rota

Caso: `SIMB-MURO` — el símbolo acompaña al muro pero `MURO` se lee horizontal.
Fuente: [atributos horizontales al girar el bloque](https://www.autodesk.com/es/support/technical/article/caas/sfdcarticles/sfdcarticles/ESP/how-to-keep-attributes-horizontal-while-rotating-a-block-in-AutoCAD.html).

1. `EDITARBLOQUE` → `ATTDEF MURO` → Propiedades → Posición de bloqueo = Sí.
2. Parámetro de punto sobre el atributo (cadena independiente, pinzamientos 0) + acción de desplazamiento solo del atributo.
3. Parámetro de rotación cuyo conjunto incluye geometría + punto, **sin el atributo**. Guardar.
4. `SINCRATR` → `SIMB-MURO` → Sí → `REGENERAR`.
5. Lote existente: Selección rápida tipo `Attribute` capa `SIMB-MURO` → Rotación 0.

Vale igual para `VENTANA BAJA SIMPLE` si suma rotación a futuro.

## 5. Mantenimiento

- Editar siempre por `EDITARBLOQUE` → `ADMINATRIB` con aplicadas a existentes → `SINCRATR` + `REGENERAR` (caso §5 del doc madre).
- Alta de bloque nuevo: definir → insertar piloto → medir con `ezdxf`/MCP → Registrar en esta tabla → entrar al DWT/DWS.
