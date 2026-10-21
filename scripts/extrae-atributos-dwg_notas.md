---
tipo: nota
script: scripts/extrae-atributos-dwg.py
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, computo, atributos, dataextraction, csv, n8n]
---

# Notas — `scripts/extrae-atributos-dwg.py`

> Extrae los **valores de atributos** de los bloques de un DWG a planillas (CSV + Markdown + JSON), sin necesidad de AutoCAD. Es el gemelo offline del `DATAEXTRACTION` nativo.

## 1. Por qué existe

AutoCAD LT 2027 **no se puede automatizar por COM** (doc oficial ACDLT 2027), así que el `DATAEXTRACTION` nativo queda atado a la sesión manual. Este script hace la misma tarea **offline**: convierte el DWG con ODA File Converter y lee el DXF con `ezdxf`. Sirve para:

- re-extraer cuadros cuando se editan atributos (1 minuto, sin abrir AutoCAD),
- alimentar el pipe n8n → Google Sheet del estudio,
- tener el dato verificado antes de tocar el DWG.

## 2. Uso

```powershell
# desde la raiz del vault
python scripts/extrae-atributos-dwg.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" `
       --salida "proyectos\MVP_02-autocad-standards\SET_01-REP_Replanteo\docs"

# mandar el CSV de carpinterias al webhook (sobrescribe la planilla de Google)
python scripts/extrae-atributos-dwg.py "G:\...\REP-ARAOZ.dwg" --salida "..." --post-n8n
```

- Python 3.10+ con `ezdxf` (`pip install ezdxf`).
- ODA File Converter solo hace falta si la entrada es `.dwg` (lo busca en `C:\Program Files\ODA\ODAFileConverter *\`).

## 3. Qué sale

| Archivo | Contenido |
|---|---|
| `atributos-a-carp-02.csv` | 42 vanos: `ANCHO`, `PUERTA`, `ALFEIZAR`, `ALTURA`, `DESCRIPCION`, `TIPO` + posición y giro |
| `atributos-simb-muro.csv` | 89 tags de muro: `MURO` (M1…M6, H1, H2, T1…T8) + posición y giro |
| `atributos-a-simbolo-npt-planta.csv` | 29 rótulos de locales: `DESCRIPCION`, `N` |
| `atributos-e-ejes.csv` | 20 marcas de eje: `EJE` |
| `atributos-e-col.csv` | 21 columnas `C40.20` |
| `cuadros-atributos.md` | los cuadros ya agrupados (vanos / muros / locales / ejes) |
| `atributos.json` | dump completo |

## 4. Detalles que importan

- **Normalización de tags**: en el DWG conviven `DESCRIPCIÓN` (con tilde) y `DESCRIPCION` (sin tilde), y el número de local es `Nº` o `N°` según el bloque. `normaliza_tag()` los deja en ASCII (`DESCRIPCION`, `N`) para que la planilla no tenga columnas duplicadas ni vacías.
- **Giros**: la columna `rot_grados` es la rotación del *bloque*; los atributos heredan ese giro. Girar los rótulos 90° **no cambia ningún valor** de atributo → los cuadros siguen vigentes después de la corrección.
- **Lo que NO sale**: el metro de cada muro. El atributo `MURO` dice el *tipo* (M1, M3…), no el largo: el largo hay que sacarlo de la geometría de `A-MURO-MAMP` / `A-MURO-MED` (o de las cotas). Para eso hace falta un script aparte que asocie cada tag a su muro.
- **Webhooks**: `--post-n8n` usa `https://n8n.pitau.tech/webhook/set01-carpinterias` (documentado en `docs/cuadro-carpinterias.md`). **Sobrescribe** el contenido de la planilla: usarlo solo cuando el CSV esté revisado.

## 5. Camino nativo en AutoCAD (para cuando se quiera dentro del CAD)

> **Ojo: en AutoCAD LT no existe.** Artículo oficial de Autodesk: *"AutoCAD LT doesn't support data extraction commands"* → `DATAEXTRACTION`, `ATTIN` y `ATTOUT` devuelven *Unknown command* en LT. La alternativa oficial en LT es **`ATTEXT`** (extrae valores de atributos a un archivo de texto con plantilla) y `LIST`.

| Comando | Qué hace | ¿En LT 2027? |
|---|---|---|
| `DATAEXTRACTION` | asistente: objetos → propiedades → atributos → XLS/CSV; puede insertar la tabla en el dibujo | **no** |
| `-DATAEXTRACTION` | igual pero **scriptable**, con archivo `.dxe` de definición | **no** |
| `ATTEXT` | exporta los valores de atributo de una selección a un archivo con plantilla | **sí** (alternativa oficial en LT) |
| `LIST` | vuelca la descripción de la geometría seleccionada | **sí** |
| ActiveX `GetAttributes` | `BlockReference.GetAttributes` → `TagString` / `TextString` | dentro de AutoLISP, **sí** |

> La vía que estamos usando (`extrae-atributos-dwg.py`) es el equivalente **offline** del `DATAEXTRACTION`: funciona sin AutoCAD y con LT. Para dejar la planilla **dentro del DWG** (decisión del estudio 20/10) hay que dibujarla con LISP (filas `MTEXT` en paper space) → comando `CUADRO-LOCALES`, a construir.

Fuentes oficiales:
- Extracción de información de atributos: https://help.autodesk.com/view/OARX/2027/PTB/?guid=GUID-C34E2AE8-A2D0-4781-8B5B-BC3E226E8B94
- Objeto `Attribute` (ActiveX): https://help.autodesk.com/view/OARX/2027/RUS/?guid=GUID-E24E7CA0-0120-4C55-BADB-46D701B8D4CB
- **LT sin comandos de extracción** (`DATAEXTRACTION`/`ATTIN`/`ATTOUT` → *Unknown command*; usar `ATTEXT` o `LIST`): https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unknown-command-when-attempting-to-use-data-extraction-features-in-AutoCAD-LT.html
