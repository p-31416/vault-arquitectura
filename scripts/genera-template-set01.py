# NOTA ES: genera el DXF base del template SET_01-REP con todo lo medido en REP-ARAOZ.
# NOTA ES: capas (29, color ACI + tipo de linea + congelada/bloqueada), estilos de
# NOTA ES: texto (9), estilos de cota (3), tipos de linea, unidades metros.
# NOTA ES: salida: TEMP/SET_01-REP_base.dxf -> luego ODA lo pasa a DWG/DWT/DWS.
# NOTA ES: uso: python scripts/genera-template-set01.py
import ezdxf
from pathlib import Path

OUT = Path(r"C:\Users\Solch16\AppData\Local\Temp\opencode\SET_01-REP_base.dxf")

# NOTA ES: (nombre, color ACI, tipo de linea, congelada, bloqueada).
CAPAS = [
    ("0", 7, "Continuous", False, False),
    ("0-REF", 7, "Continuous", True, True),
    ("A-CARP-02", 251, "Continuous", False, False),
    ("A-COTA-1-50", 250, "Continuous", False, False),
    ("A-EJES", 90, "DASHDOT", False, True),
    ("A-EJES-VACIOS", 113, "DASHDOT", False, True),
    ("A-EQUIP-", 8, "Continuous", False, False),
    ("A-MURO-MAMP", 24, "Continuous", False, False),
    ("A-MURO-MED", 11, "Continuous", False, True),
    ("A-SIMBOLO-NPT-PLANTA", 251, "Continuous", False, False),
    ("A-SOLADOS", 250, "Continuous", False, False),
    ("A-TERRENO", 163, "Continuous", True, False),
    ("AR-CUADRO DE VANO", 1, "Continuous", False, False),
    ("CONDUCTOS", 3, "Continuous", False, False),
    ("E-COL", 5, "Continuous", False, False),
    ("E-COL-EJES", 254, "Continuous", False, True),
    ("E-COL-H", 251, "Continuous", False, True),
    ("E-EJES", 10, "Continuous", True, False),
    ("E-TAB", 166, "Continuous", False, False),
    ("E-TAB-H", 251, "Continuous", False, True),
    ("IE-EJEX", 32, "DASHDOT", True, True),
    ("REP-COTAS", 41, "Continuous", False, False),
    ("REP-EJES", 81, "DASHDOTX2", False, True),
    ("ROT-HOJA", 5, "Continuous", False, False),
    ("ROT-TXT", 174, "Continuous", False, False),
    ("ROT-VP", 130, "Continuous", False, False),
    ("SIMB-CARP", 33, "Continuous", False, False),
    ("SIMB-MURO", 251, "Continuous", False, False),
]
# NOTA ES: Defpoints la crea AutoCAD solo; no se precrea.

# NOTA ES: (nombre, fuente, altura fija 0=por entidad, ancho).
ESTILOS = [
    ("cotas-50", "simplex.shx", 0.16, 0.9),
    ("COTAS", "simplex.shx", 0.0, 0.8),
    ("style2", "simplex.shx", 0.0, 1.0),
    ("Standard", "arial.ttf", 0.0, 1.0),
    ("MBA25", "arial.ttf", 0.05, 1.0),
    ("ROMANS", "calibril.ttf", 0.06, 0.7),
    ("ROT", "calibril.ttf", 0.25, 0.8),
    ("Style-Arial_1", "arial.ttf", 0.0, 1.0),
]

doc = ezdxf.new("R2018")
doc.header["$INSUNITS"] = 6  # NOTA ES: metros.
doc.header["$MEASUREMENT"] = 1  # NOTA ES: metrico.
doc.header["$LUNITS"] = 2  # NOTA ES: decimal.
doc.header["$LUPREC"] = 2  # NOTA ES: 2 decimales.

# NOTA ES: tipos de linea: si el template no los trae, se agregan simples.
LTYPES = {
    "DASHDOT": ("A,.75,-.25,0,-.25", "Eje punto-raya"),
    "DASHDOTX2": ("A,1.5,-.5,0,-.5", "Eje punto-raya doble (simple)"),
    "DASHED": ("A,.75,-.5", "Oculta"),
}
existentes = {lt.dxf.name.upper() for lt in doc.linetypes}
for nombre, ( patron, descrip) in LTYPES.items():
    if nombre not in existentes:
        doc.linetypes.new(nombre, dxfattribs={
            "description": descrip, "pattern": patron})

existentes_capas = {l.dxf.name for l in doc.layers}
for nombre, color, lt, fz, lk in CAPAS:
    if nombre in existentes_capas:
        continue  # NOTA ES: '0' ya viene en el template, se conserva.
    capa = doc.layers.new(nombre, dxfattribs={
        "color": color, "linetype": lt.upper()})
    if fz:
        capa.freeze()
    if lk:
        capa.lock()

existentes_estilos = {s.dxf.name for s in doc.styles}
for nombre, fuente, altura, ancho in ESTILOS:
    if nombre in existentes_estilos:
        st = doc.styles.get(nombre)  # NOTA ES: actualiza el existente.
        st.dxf.font = fuente
        st.dxf.height = altura
        st.dxf.width = ancho
        continue
    doc.styles.new(nombre, dxfattribs={
        "font": fuente, "height": altura, "width": ancho})

# NOTA ES: puntas de flecha como bloques simples (tick + abierta 90).
tick = doc.blocks.new("_ArchTick")
tick.add_line((-0.05, -0.05), (0.05, 0.05))
abierta = doc.blocks.new("_Open90")
abierta.add_line((0, 0), (0.1, 0.03))
abierta.add_line((0, 0), (0.1, -0.03))

# NOTA ES: dimstyles medidos (vars clave; resto default ISO).
doc.dimstyles.new(
    "COTAS-ARQ-50",
    dxfattribs={"dimtxsty": "COTAS", "dimdec": 2, "dimblk": "_ArchTick",
                "dimasz": 0.1, "dimexe": 0.1, "dimexo": 0.05,
                "dimgap": 0.1, "dimclrd": 256, "dimclrt": 256})
doc.dimstyles.new(
    "REPLANTEO 150",
    dxfattribs={"dimtxsty": "cotas-50", "dimdec": 2, "dimblk": "_Open90",
                "dimasz": 0.2, "dimexe": 0.0, "dimexo": 0.05,
                "dimgap": 0.03, "dimclrd": 256, "dimclrt": 256})

doc.saveas(OUT)
print("OK ->", OUT)
print("capas:", len(doc.layers), "| estilos:", len(doc.styles),
      "| cotas:", len(doc.dimstyles))
