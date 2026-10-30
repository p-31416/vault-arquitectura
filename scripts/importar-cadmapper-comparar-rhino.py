#! python3
# -*- coding: utf-8 -*-
"""
importar-cadmapper-comparar-rhino.py
====================================

Importa el .3dm de CADMapper a la escena abierta (mcp-plaza.3dm) en capa
propia desplazada +1000 m en X, para comparar lado a lado con el massing OSM.
Informa bbox y distribucion de alturas de ambas capas.

Uso via puente MCP: ``python scripts\\rhino-mcp-cli.py exec scripts\\importar-cadmapper-comparar-rhino.py``

100 % plano (el puente MCP no deja ver ``def`` ni constantes de modulo).

Licencia CADMapper: ODbL (OSM) + USGS/NASA dominio publico — ver
``activos/.../earth2rhino3d/base/cadmapper/LICENSE-cadmapper.txt``.
"""

import System
import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

# NOTA ES: rutas fijas del vault + desplazamiento de comparacion.
_ruta_cm = "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\activos\\proyectos\\concurso-gaudi-nexus\\earth2rhino3d\\base\\cadmapper\\cadmapper-barcelona-catalonia-es.3dm"
_dx = 1000.0

_lineas = []
if not rs.IsLayer("SF-MASSING-CADMAPPER"):
    rs.AddLayer("SF-MASSING-CADMAPPER", (120, 170, 255))

_f3d = Rhino.FileIO.File3dm.Read(_ruta_cm)
if _f3d is None:
    _lineas.append("ERROR: no se pudo leer " + _ruta_cm)
    print("\n".join(_lineas))
else:
    _lineas.append("objetos cadmapper en archivo: %d" % _f3d.Objects.Count)
    _xf = Rhino.Geometry.Transform.Translation(_dx, 0.0, 0.0)
    _ok = 0
    _salto = 0
    for _o in _f3d.Objects:
        try:
            _g = _o.Geometry.Duplicate()
            _g.Transform(_xf)
            _id = sc.doc.Objects.Add(_g)
            if str(_id) == "00000000-0000-0000-0000-000000000000":
                _salto += 1
                continue
            rs.ObjectLayer(_id, "SF-MASSING-CADMAPPER")
            _ok += 1
        except Exception:
            _salto += 1
    _lineas.append("importados OK: %d | salteados: %d (desplazamiento +%.0f m en X)" % (_ok, _salto, _dx))
    # NOTA ES: bbox + alturas de ambas capas para la comparacion.
    for _capa in ("SF-MASSING-OSM", "SF-MASSING-CADMAPPER"):
        _ids = list(rs.ObjectsByLayer(_capa) or [])
        if not _ids:
            _lineas.append("%s: VACIA" % _capa)
            continue
        _b = rs.BoundingBox(_ids)
        _xs = [_p[0] for _p in _b]
        _ys = [_p[1] for _p in _b]
        _zs = [_p[2] for _p in _b]
        _lineas.append("%s: n=%d x[%.1f, %.1f] y[%.1f, %.1f] z[%.1f, %.1f]" % (
            _capa, len(_ids), min(_xs), max(_xs), min(_ys), max(_ys), min(_zs), max(_zs)))
    # NOTA ES: distribucion de alturas por objeto (top 5 mas altos de cada capa).
    for _capa in ("SF-MASSING-OSM", "SF-MASSING-CADMAPPER"):
        _ids = list(rs.ObjectsByLayer(_capa) or [])
        _hs = []
        for _i in _ids:
            try:
                _bb = rs.BoundingBox(_i)
                _zz = [_p[2] for _p in _bb]
                _hs.append(max(_zz) - min(_zz))
            except Exception:
                pass
        _hs.sort()
        if _hs:
            _lineas.append("%s alturas: n=%d min=%.1f med=%.1f max=%.1f" % (
                _capa, len(_hs), _hs[0], _hs[len(_hs) // 2], _hs[-1]))
    sc.doc.Views.Redraw()
    _lineas.append("NO se guardo el documento.")
    print("\n".join(_lineas))
