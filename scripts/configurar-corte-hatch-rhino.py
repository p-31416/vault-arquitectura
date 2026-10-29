#! python3
# -*- coding: utf-8 -*-
"""
configurar-corte-hatch-rhino.py
================================

Configura el **relleno de los cortes con trama** y arma una **lámina nueva**
con el corte de madera, **sin tocar el viewport que ya existe**.

Qué hace, en orden
------------------
1. Activa el **escalado de tramas** del documento (`ModelSpaceHatchScalingEnabled`
   + `ModelSpaceHatchScale`). Es el ajuste que decide si la trama se ve en la
   lámina: con el escalado apagado, el patrón se dibuja en el espacio del modelo
   y en un detalle a 1:30 mide 0,03 mm en el papel (invisible).
2. Escribe el **Section Style** de cada capa de material (patrón, rotación,
   escala y colores de trama y de borde).
3. Crea una **lámina nueva** (`AddPageView`) con un **detalle** (`AddDetailView`).
4. Copia la **cámara** del detalle que ya existe, para que el corte se vea igual.
5. Fija la **escala** del detalle con la secuencia que funciona en Rhino 8
   (`SetActiveDetail` → `ZoomExtents` → `IsProjectionLocked` → `SetScale` →
   `CommitChanges`).
6. **Habilita el clipping plane en el detalle nuevo** (`AddClipViewport`).
7. Redibuja las vistas (`doc.Views.Redraw()`).

NO guarda el documento: el usuario lo guarda a mano.

Cómo se ejecuta
----------------
Desde la línea de comandos de Rhino 8::

    _RunPythonScript "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\scripts\\configurar-corte-hatch-rhino.py"

o a través del puente MCP (que es como lo ejecuta el asistente).
"""

import math

import Rhino
import Rhino.DocObjects
import scriptcontext as sc

# --------------------------------------------------------------------- CONFIG
# NOTA ES: esta es la parte que se toca para cambiar el resultado. Todo lo de
# abajo son datos, no lógica: se pueden editar sin entender el script.

NOMBRE_LAMINA = "UY-CORTE-HATCH"     # nombre de la lámina nueva
NOMBRE_DETALLE = "A-A-HATCH"         # nombre del detalle nuevo
ANCHO_LAMINA_MM = 420.0              # A3
ALTO_LAMINA_MM = 297.0
MARGEN_X_MM = 10.0                   # el detalle arranca a 10 mm del borde
MARGEN_Y_INFERIOR_MM = 22.0

# 1 m del modelo = 33,33 mm en la lamina  ->  escala 1:30
ESCALA_1M_EN_MM_DE_LAMINA = 33.3333

# Separación de la trama en el papel, en mm. A calibrar mirando el resultado.
MODEL_SPACE_HATCH_SCALE = 3.0

# Las 13 capas de material: (capa, patrón, rotación en grados, escala del
# patrón, color de trama, color del borde, ancho del borde)
MATERIALES = [
    ("EST-MAD",           "Hatch1", 45, 1.0, (140, 95, 60),   (60, 40, 25),  1.5),
    ("MAD-MARCO_PINO",    "Hatch2", 45, 1.0, (105, 72, 43),   (45, 30, 18),  1.5),
    ("04-BAST-2.6",       "Hatch1", 90, 1.0, (160, 160, 160), (70, 70, 70),  1.0),
    ("05-AISL-LANAVID",   "Hatch3",  0, 1.0, (235, 215, 120), (90, 80, 40),  1.0),
    ("02-FENOLICO",       "Solid",   0, 1.0, (90, 60, 40),    (40, 25, 15),  1.0),
    ("03-FILM_POL",       "Solid",   0, 1.0, (215, 215, 215), (90, 90, 90),  0.5),
    ("06 TYVEK",          "Solid",   0, 1.0, (240, 240, 235), (100, 100, 95), 0.5),
    ("07-CALV-2.2",       "Solid",   0, 1.0, (150, 150, 150), (60, 60, 60),  1.0),
    ("08-CHAPA-NEGRO",    "Solid",   0, 1.0, (30, 30, 30),    (10, 10, 10),  1.5),
    ("09-ZING-CHAPA_GALV","Solid",   0, 1.0, (180, 185, 190), (80, 82, 85),  1.0),
    ("CARP-MET",          "Solid",   0, 1.0, (70, 70, 70),    (30, 30, 30),  1.5),
    ("CARP-VID",          "Solid",   0, 1.0, (170, 200, 210), (70, 90, 100), 1.0),
    ("01-PLACA YESO",     "Solid",   0, 1.0, (235, 235, 235), (100, 100, 100), 1.0),
]

SALIDA = []


def P(txt):
    # NOTA ES: imprime una linea y la guarda en SALIDA, para que al final se
    # pueda copiar el informe completo de la linea de comandos.
    SALIDA.append(str(txt))
    print(txt)


def seguro(fn, defecto="n/d"):
    # NOTA ES: ejecuta algo y devuelve un texto de error en vez de cortar el
    # script. La API de Rhino cambia entre versiones y asi el script sigue.
    try:
        return fn()
    except Exception as exc:
        return "%s (error: %s)" % (defecto, exc.__class__.__name__)


def indice_patron(doc, nombre):
    # NOTA ES: los patrones de trama del documento son una lista; cada Section
    # Style guarda el INDICE del patron, no el nombre. Por eso hay que buscar
    # el indice del patron que se quiere usar.
    for i in range(doc.HatchPatterns.Count):
        if doc.HatchPatterns[i].Name == nombre:
            return i
    return None


def color_rgb(tripla):
    # NOTA ES: Rhino.Color toma los tres canales en 0..255.
    return Rhino.Color(tripla[0], tripla[1], tripla[2])


def buscar_detalle_existente(doc):
    # NOTA ES: para que el corte nuevo se vea igual que el que ya esta, se
    # busca el primer detalle de cualquier lamina y se le copia la camara.
    for pagina in doc.Views.GetPageViews():
        for det in pagina.Details:
            return pagina, det
    return None, None


def main():
    doc = sc.doc
    SALIDA[:] = []
    P("=" * 68)
    P("ARCHIVO : %s" % doc.Path)
    P("unidades: modelo=%s | pagina=%s" % (doc.ModelUnitSystem, doc.PageUnitSystem))
    P("=" * 68)

    # ------------------------------------------- 1) ESCALADO DE TRAMAS
    P("")
    P("--- 1) ESCALADO DE TRAMAS (la causa del corte invisible) ----------")
    P("  antes: enabled=%s | escala=%s"
      % (doc.ModelSpaceHatchScalingEnabled, doc.ModelSpaceHatchScale))
    doc.ModelSpaceHatchScalingEnabled = True
    doc.ModelSpaceHatchScale = MODEL_SPACE_HATCH_SCALE
    P("  despues: enabled=%s | escala=%s"
      % (doc.ModelSpaceHatchScalingEnabled, doc.ModelSpaceHatchScale))

    # ------------------------------------------- 2) SECTION STYLES POR CAPA
    P("")
    P("--- 2) SECTION STYLE DE LAS CAPAS DE MATERIAL ---------------------")
    aplicadas = 0
    for (nombre, patron, rotacion, esc_patron, col_trama, col_borde, ancho_borde) in MATERIALES:
        capa = None
        for i in range(doc.Layers.Count):
            if doc.Layers[i].Name == nombre:
                capa = doc.Layers[i]
                break
        if capa is None:
            P("  %-22s (la capa no existe en este archivo)" % nombre)
            continue
        idx = indice_patron(doc, patron)
        if idx is None:
            P("  %-22s (el patron %s no esta cargado)" % (nombre, patron))
            continue
        ss = Rhino.DocObjects.SectionStyle()
        ss.HatchIndex = idx
        ss.HatchScale = esc_patron
        # NOTA ES: la rotacion de la API esta en RADIANES, no en grados.
        ss.HatchRotationRadians = math.radians(rotacion)
        ss.HatchPatternColor = color_rgb(col_trama)
        ss.HatchPatternPrintColor = color_rgb(col_trama)
        ss.BoundaryVisible = True
        ss.BoundaryColor = color_rgb(col_borde)
        ss.BoundaryPrintColor = color_rgb(col_borde)
        ss.BoundaryWidthScale = ancho_borde
        ss.BackgroundFillColor = Rhino.Color(255, 255, 255)
        ok = seguro(lambda c=capa, s=ss: c.SetCustomSectionStyle(s))
        if ok is None:
            aplicadas += 1
            P("  %-22s patron=%-8s rot=%-3s esc=%-4s borde=%s  OK"
              % (nombre, patron, rotacion, esc_patron, ancho_borde))
        else:
            P("  %-22s ERROR: %s" % (nombre, ok))
    P("  capas con estilo aplicado: %d de %d" % (aplicadas, len(MATERIALES)))

    # ------------------------------------------- 3) LAMINA NUEVA + DETALLE
    P("")
    P("--- 3) LAMINA NUEVA + DETALLE ------------------------------------")
    pagina_existente = None
    for pv in doc.Views.GetPageViews():
        if pv.Name == NOMBRE_LAMINA:
            pagina_existente = pv
            break
    if pagina_existente is not None:
        P("  la lamina %s ya existe: se reutiliza" % NOMBRE_LAMINA)
        pagina = pagina_existente
    else:
        pagina = doc.Views.AddPageView(NOMBRE_LAMINA, ANCHO_LAMINA_MM, ALTO_LAMINA_MM)
        P("  lamina creada: %s" % (pagina.Name if pagina else "FALLO"))

    if pagina is None:
        P("  no se pudo crear la lamina: se corta aca")
        return "\n".join(SALIDA)

    # Si ya existe un detalle con ese nombre, se borra y se rehace (para poder
    # repetir el script sin acumular laminas).
    for det in list(pagina.Details):
        if seguro(lambda d=det: d.Attributes.Name) == NOMBRE_DETALLE:
            doc.Objects.Remove(det.Id, True)
            P("  detalle previo %s eliminado" % NOMBRE_DETALLE)

    izq = Rhino.Geometry.Point2d(MARGEN_X_MM, ALTO_LAMINA_MM - MARGEN_Y_INFERIOR_MM)
    der = Rhino.Geometry.Point2d(ANCHO_LAMINA_MM - MARGEN_X_MM, MARGEN_Y_INFERIOR_MM)

    # NOTA ES: se usa la misma proyeccion que el detalle que ya existe, para
    # que el corte se vea desde el mismo lado.
    proyeccion = Rhino.Display.DefinedViewportProjection.Right
    pagina_ref, det_ref = buscar_detalle_existente(doc)
    if det_ref is not None:
        p_ref = seguro(lambda d=det_ref: d.DetailGeometry.Projection)
        if p_ref is not None:
            proyeccion = p_ref
        P("  detalle de referencia: %s | proyeccion=%s"
          % (seguro(lambda d=det_ref: d.Attributes.Name), p_ref))

    detalle = pagina.AddDetailView(NOMBRE_DETALLE, izq, der, proyeccion)
    if detalle is None:
        P("  no se pudo crear el detalle: se corta aca")
        return "\n".join(SALIDA)
    P("  detalle creado: %s" % NOMBRE_DETALLE)

    # ------------------------------------------- 4) COPIAR LA CAMARA
    if det_ref is not None:
        cam = seguro(lambda d=det_ref: d.Viewport.Camera)
        if cam is not None:
            # NOTA ES: el orden importa. Primero la direccion, despues el
            # objetivo, y al final el vector "arriba" (CameraUp).
            seguro(lambda dd=detalle: dd.DetailGeometry.SetCameraDirection(cam.Direction))
            seguro(lambda dd=detalle: dd.DetailGeometry.SetCameraTarget(cam.Target, True))
            seguro(lambda dd=detalle: setattr(dd.DetailGeometry, "CameraUp", cam.Up))
            P("  camara copiada: target=%s" % (cam.Target,))

    # ------------------------------------------- 5) ESCALA (secuencia V8)
    # NOTA ES: en Rhino 8 el metodo SetScale solo funciona si el detalle esta
    # activo y despues se hace CommitChanges. Es la secuencia que publica
    # McNeel (Dale Fugier, 2024).
    pagina.SetActiveDetail(detalle.Id)
    seguro(lambda: detalle.Viewport.ZoomExtents())
    seguro(lambda: setattr(detalle.DetailGeometry, "IsProjectionLocked", True))
    seguro(lambda: detalle.DetailGeometry.SetScale(
        1.0, doc.ModelUnitSystem, ESCALA_1M_EN_MM_DE_LAMINA, doc.PageUnitSystem))
    seguro(lambda: detalle.CommitChanges())
    P("  escala: 1 m del modelo = %.4f mm en la lamina  (1:30)" % ESCALA_1M_EN_MM_DE_LAMINA)

    # ------------------------------------------- 6) HABILITAR EL CORTE
    P("")
    P("--- 6) CLIPPING PLANE HABILITADO EN EL DETALLE NUEVO -------------")
    n = 0
    for obj in doc.Objects:
        if obj.ObjectType == Rhino.DocObjects.ObjectType.ClipPlane:
            attrs = obj.Attributes
            # NOTA ES: AddClipViewport agrega este viewport a la lista de vistas
            # que recorta el plano (es el "Views Clipped" del panel de propiedades).
            r = seguro(lambda a=attrs: a.AddClipViewport(detalle.Id))
            if r is None:
                obj.Attributes = attrs
                n += 1
                P("  plano %r habilitado en el detalle nuevo" % obj.Attributes.Name)
            else:
                P("  plano %r: %s" % (obj.Attributes.Name, r))
    P("  planos de corte: %d" % n)

    # ------------------------------------------- 7) REDIBUJAR
    pagina.SetPageAsActive()
    doc.Views.ActiveView = pagina
    # NOTA ES: Redraw fuerza el recalculo de todas las vistas. Es lo que hace
    # falta cuando el corte o la trama quedaron con el resultado anterior.
    seguro(lambda: doc.Views.Redraw())
    P("")
    P("  listo. NO se guardo el documento (lo guarda el usuario).")
    return "\n".join(SALIDA)


INFORME = main()
print(INFORME)
