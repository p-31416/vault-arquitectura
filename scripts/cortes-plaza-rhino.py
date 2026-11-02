#! python3
# -*- coding: utf-8 -*-
"""
cortes-plaza-rhino.py
=====================

Dos cortes por la plaza (uno en cada sentido) con sus layouts y viewports:
- CORTE A-A (longitudinal E-O): plano vertical XZ en y=0, vista Back, lamina SF-CORTE-AA.
- CORTE B-B (transversal N-S): plano vertical YZ en x=0, vista Right, lamina SF-CORTE-BB.

Laminas A1 apaisado (841 x 594 mm), detalle a 1:2000, proyeccion bloqueada.
Via puente MCP: ``python scripts\\rhino-mcp-cli.py exec scripts\\cortes-plaza-rhino.py``

100 % plano (el puente MCP no deja ver ``def`` ni constantes de modulo).
No guarda el documento (decision del estudio).
Compatible con IronPython 2.7 (sin f-strings) y RhinoPython 3.
"""

import System
import Rhino
import Rhino.DocObjects
import rhinoscriptsyntax as rs
import scriptcontext as sc

# NOTA ES: configuracion. A1 apaisado, 1:2000 -> 1 m del modelo = 0,5 mm en lamina.
_ANCHO = 841.0
_ALTO = 594.0
_MARGEN_X = 15.0
_MARGEN_Y = 25.0
_MM_POR_METRO = 0.5
_CAPA = "SF-CORTES"



# NOTA ES: capa de los planos de corte.
if not rs.IsLayer(_CAPA):
    rs.AddLayer(_CAPA, (220, 40, 40))

_doc = sc.doc
print("unidades: modelo=%s | pagina=%s" % (_doc.ModelUnitSystem, _doc.PageUnitSystem))

# NOTA ES: limpieza de la sonda de prueba (si quedo de una sesion anterior).
for _o in list(_doc.Objects):
    if _o.ObjectType == Rhino.DocObjects.ObjectType.ClipPlane:
        try:
            _nn = _o.Attributes.Name
        except Exception:
            _nn = ""
        if _nn == "TEST-PLANO":
            _doc.Objects.Delete(_o.Id, True)
            print("sonda TEST-PLANO eliminada")

# NOTA ES: definicion de los dos cortes: nombre, plano, tamano, vista, lamina.
_cortes = []
_plano_a = Rhino.Geometry.Plane(
    Rhino.Geometry.Point3d(0.0, 0.0, 85.0),
    Rhino.Geometry.Vector3d(1.0, 0.0, 0.0),
    Rhino.Geometry.Vector3d(0.0, 0.0, 1.0))
_cortes.append(("CORTE-A-A", _plano_a, 1100.0, 340.0,
                Rhino.Display.DefinedViewportProjection.Back,
                "SF-CORTE-AA", "A-A"))
_plano_b = Rhino.Geometry.Plane(
    Rhino.Geometry.Point3d(0.0, 0.0, 85.0),
    Rhino.Geometry.Vector3d(0.0, 1.0, 0.0),
    Rhino.Geometry.Vector3d(0.0, 0.0, 1.0))
_cortes.append(("CORTE-B-B", _plano_b, 1100.0, 340.0,
                Rhino.Display.DefinedViewportProjection.Right,
                "SF-CORTE-BB", "B-B"))

for _k in range(len(_cortes)):
    _nombre = _cortes[_k][0]
    _plano = _cortes[_k][1]
    _u = _cortes[_k][2]
    _v = _cortes[_k][3]
    _vista = _cortes[_k][4]
    _lamina = _cortes[_k][5]
    _det_nom = _cortes[_k][6]
    print("")
    print("--- %s (%s) ---" % (_nombre, _lamina))

    # NOTA ES: si el plano ya existe se borra y se rehace (repetible).
    for _o in list(_doc.Objects):
        if _o.ObjectType == Rhino.DocObjects.ObjectType.ClipPlane:
            if _o.Attributes.Name == _nombre:
                _doc.Objects.Delete(_o.Id, True)
                print("  plano previo eliminado")
    _attrs = Rhino.DocObjects.ObjectAttributes()
    _attrs.Name = _nombre
    _attrs.LayerIndex = _doc.Layers.FindByFullPath(_CAPA, True)
    # NOTA ES: AddClippingPlane exige al menos un viewport (lista vacia = Empty).
    # Se crea sobre la vista activa y despues se mueve solo al detalle.
    _vista_activa = _doc.Views.ActiveView.ActiveViewportID
    _lista_ini = System.Collections.Generic.List[System.Guid]()
    _lista_ini.Add(_vista_activa)
    _g = _doc.Objects.AddClippingPlane(_plano, _u, _v, _lista_ini, _attrs)
    if str(_g) == "00000000-0000-0000-0000-000000000000":
        print("  ERROR: no se pudo crear el plano")
        continue
    print("  plano creado (normal=%s)" % _plano.Normal)

    # NOTA ES: lamina existente se reutiliza; detalle homonimo se rehace.
    _pag = None
    for _pv in _doc.Views.GetPageViews():
        if _pv.PageName == _lamina:
            _pag = _pv
            break
    if _pag is None:
        _pag = _doc.Views.AddPageView(_lamina, _ANCHO, _ALTO)
        print("  lamina creada: %s" % _lamina)
    else:
        print("  lamina existente: se reutiliza")
    if _pag is None:
        print("  ERROR: sin lamina, se salta este corte")
        continue
    try:
        _dets_previos = list(_pag.GetDetailViews())
    except Exception:
        _dets_previos = []
    for _d in _dets_previos:
        try:
            _nn = _d.Viewport.Name
        except Exception:
            _nn = ""
        if _nn == _det_nom:
            _doc.Objects.Delete(_d.Id, True)
            print("  detalle previo eliminado")
    _izq = Rhino.Geometry.Point2d(_MARGEN_X, _ALTO - _MARGEN_Y)
    _der = Rhino.Geometry.Point2d(_ANCHO - _MARGEN_X, _MARGEN_Y)
    _det = _pag.AddDetailView(_det_nom, _izq, _der, _vista)
    if _det is None:
        print("  ERROR: no se pudo crear el detalle")
        continue
    print("  detalle %s creado (%s)" % (_det_nom, _vista))

    # NOTA ES: el plano recorta SOLO su detalle (Views Clipped del panel).
    # Firmas V8: AddClipViewport(viewport, bool) / RemoveClipViewport(viewport, bool)
    # en el OBJETO plano (no en Attributes). Se agrega el detalle y se saca
    # la vista del modelo que se uso al crearlo.
    try:
        _obj_plano = _doc.Objects.Find(_g)
        _obj_plano.AddClipViewport(_det.Viewport, True)
        _vista_mod = None
        for _vv in _doc.Views:
            try:
                if _vv.ActiveViewportID == _vista_activa:
                    _vista_mod = _vv.ActiveViewport
                    break
            except Exception:
                continue
        if _vista_mod is not None:
            _obj_plano.RemoveClipViewport(_vista_mod, True)
        _obj_plano.CommitChanges()
        print("  plano habilitado solo en el detalle")
    except Exception as _ex:
        print("  AVISO clip: %s" % _ex.__class__.__name__)

    # NOTA ES: secuencia V8 (McNeel/Dale Fugier 2024): activar -> encuadrar ->
    # bloquear proyeccion -> escala -> commit. Sin el commit la escala no aplica.
    try:
        _pag.SetActiveDetail(_det.Id)
    except Exception as _ex:
        print("  AVISO active-detail: %s" % _ex.__class__.__name__)
    try:
        _det.Viewport.ZoomExtents()
    except Exception as _ex:
        print("  AVISO zoom: %s" % _ex.__class__.__name__)
    try:
        _det.DetailGeometry.IsProjectionLocked = True
    except Exception as _ex:
        print("  AVISO lock-proy: %s" % _ex.__class__.__name__)
    try:
        _det.DetailGeometry.SetScale(1.0, _doc.ModelUnitSystem, _MM_POR_METRO, _doc.PageUnitSystem)
    except Exception as _ex:
        print("  AVISO escala: %s" % _ex.__class__.__name__)
    try:
        _det.CommitChanges()
        print("  escala 1:2000 + commit OK")
    except Exception as _ex:
        print("  AVISO commit: %s" % _ex.__class__.__name__)
    try:
        _det.DetailGeometry.IsLocked = True
        print("  detalle bloqueado")
    except Exception:
        print("  (sin bloqueo total: trabar a mano con Detail > Lock)")

_doc.Views.Redraw()
print("")
print("listo. Laminas: SF-CORTE-AA (Back) + SF-CORTE-BB (Right), 1:2000 en A1.")
print("NO se guardo el documento (lo guarda el usuario).")
