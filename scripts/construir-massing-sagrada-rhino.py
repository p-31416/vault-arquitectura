#! python3
# -*- coding: utf-8 -*-
"""
construir-massing-sagrada-rhino.py
==================================

Construye el massing 2.5D del entorno Sagrada Familia (Eixample, Barcelona)
dentro de Rhino 8, desde la base open descargada con
``scripts/descargar-osm-sagrada.py`` (Overpass, ODbL).

Uso (linea de comandos de Rhino 8)::

    _RunPythonScript "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\scripts\\construir-massing-sagrada-rhino.py"

Via puente MCP: ``python scripts\\rhino-mcp-cli.py exec scripts\\construir-massing-sagrada-rhino.py``

Archivo nuevo sugerido: metros, ``SF-sitio-massing-v01.3dm``.
El script NO guarda el documento (decision del estudio).

Compatible con RhinoPython 3 (CPython), IronPython 2.7 y el puente MCP.
NOTA TECNICA: el puente MCP ejecuta el codigo en un entorno donde las
definiciones ``def`` no quedan visibles para el resto del codigo, por eso
este script es 100 % plano: sin funciones, todo en linea recta.
"""

import json
import math
import os

import Rhino
import System
import rhinoscriptsyntax as rs
import scriptcontext as sc

# NOTA ES: base open (fuera de git) + ancla templo + alturas Eixample.
_base_json = "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\activos\\proyectos\\concurso-gaudi-nexus\\earth2rhino3d\\base\\sagrada_overpass.json"
_lat0 = 41.4036
_lon0 = 2.1744
_por_nivel = 3.1
_default = 21.0
_cos0 = math.cos(math.radians(_lat0))

_lineas = []
if not os.path.exists(_base_json):
    _lineas.append("ERROR: no existe la base: " + _base_json)
    _lineas.append("Corre antes: P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\descargar-osm-sagrada.py")
    print("\n".join(_lineas))
else:
    with open(_base_json, "r", encoding="utf-8") as _f:
        _data = json.load(_f)
    _nodos = {}
    for _e in _data.get("elements", []):
        # NOTA ES: guardamos lat/lon por id para armar los footprints.
        if _e.get("type") == "node":
            _nodos[_e["id"]] = (_e.get("lat"), _e.get("lon"))
    _ways = [_e for _e in _data.get("elements", []) if _e.get("type") == "way"]
    _lineas.append("ways building: %d | nodos: %d" % (len(_ways), len(_nodos)))

    if not rs.IsLayer("SF-MASSING-OSM"):
        rs.AddLayer("SF-MASSING-OSM", (200, 200, 200))
    if not rs.IsLayer("TESTIGO-SF"):
        rs.AddLayer("TESTIGO-SF", (255, 180, 60))
    if not rs.IsLayer("SF-ORIGEN"):
        rs.AddLayer("SF-ORIGEN", (255, 0, 0))

    _ok = 0
    _salteados = 0
    _c_vacios = 0
    _c_sin_planas = 0
    _c_sin_brep = 0
    _c_sin_add = 0
    _c_excepcion = 0
    _h_nivel = 0
    _h_default = 0
    for _w in _ways:
        # NOTA ES: cada way es un footprint; lo convertimos a metros y extruimos.
        _pts = []
        for _nid in _w.get("nodes", []):
            if _nid in _nodos and _nodos[_nid][0] is not None:
                _la, _lo = _nodos[_nid]
                _pts.append(((_lo - _lon0) * 111320.0 * _cos0, (_la - _lat0) * 110540.0))
        if len(_pts) < 3:
            _salteados += 1
            continue
        # NOTA ES: cerramos el anillo si el way no lo trae cerrado.
        if _pts[0] != _pts[-1]:
            _pts.append(_pts[0])
        _tags = _w.get("tags", {}) or {}
        _h = _default
        try:
            if "height" in _tags:
                _crudo = str(_tags["height"]).replace("m", "").strip().split(" ")[0]
                _h = max(3.0, float(_crudo.replace(",", ".")))
            elif "building:levels" in _tags:
                _h = max(3.0, float(str(_tags["building:levels"]).split(";")[0]) * _por_nivel)
            elif "levels" in _tags:
                _h = max(3.0, float(str(_tags["levels"]).split(";")[0]) * _por_nivel)
        except Exception:
            _h = _default
        if "building:levels" in _tags or "levels" in _tags:
            _h_nivel += 1
        else:
            _h_default += 1
        try:
            _p3d = []
            for (_x, _y) in _pts:
                _p3d.append(Rhino.Geometry.Point3d(_x, _y, 0))
            _crv = sc.doc.Objects.AddPolyline(_p3d)
            if _crv == System.Guid.Empty:
                _salteados += 1
                _c_vacios += 1
                continue
            # NOTA ES: extrusion recta +Y... no: +Z garantizada (el offset por cara
            # NOTA ES: depende de la normal y enterraba la mitad del massing).
            _ext = rs.ExtrudeCurveStraight(_crv, (0, 0, 0), (0, 0, _h))
            sc.doc.Objects.Delete(_crv, True)
            if not _ext:
                _salteados += 1
                _c_sin_brep += 1
                continue
            _cap = rs.CapPlanarHoles(_ext)
            if not _cap:
                # NOTA ES: si no tapa, igual sirve como volumen de referencia.
                _c_sin_planas += 1
            rs.ObjectLayer(_ext, "SF-MASSING-OSM")
            _ok += 1
        except Exception as _ex:
            _salteados += 1
            _c_excepcion += 1
            if _c_excepcion <= 2:
                _lineas.append("EXC ejemplo: %s: %s" % (_ex.__class__.__name__, str(_ex)[:200]))
    # NOTA ES: testigo del templo (caja propia 60x100x172.5 m, NO extruida de OSM).
    try:
        _caja = rs.AddBox([
            (-30, -50, 0), (30, -50, 0), (30, 50, 0), (-30, 50, 0),
            (-30, -50, 172.5), (30, -50, 172.5), (30, 50, 172.5), (-30, 50, 172.5)])
        if _caja:
            rs.ObjectLayer(_caja, "TESTIGO-SF")
            rs.ObjectName(_caja, "TESTIGO-SF-172.5m")
    except Exception as _exc:
        _lineas.append("testigo: no se pudo crear (%s)" % _exc.__class__.__name__)
    # NOTA ES: cruz de origen en (0,0) para orientar el encuadre.
    try:
        _l1 = rs.AddLine((-10, 0, 0), (10, 0, 0))
        _l2 = rs.AddLine((0, -10, 0), (0, 10, 0))
        for _l in (_l1, _l2):
            if _l:
                rs.ObjectLayer(_l, "SF-ORIGEN")
    except Exception:
        pass
    sc.doc.Views.Redraw()
    _lineas.append("extruidos OK: %d | con levels: %d | default 21 m: %d | salteados: %d" % (_ok, _h_nivel, _h_default, _salteados))
    _lineas.append("detalle fallos: polyline_vacia=%d sin_planas=%d sin_brep=%d sin_add=%d excepcion=%d" % (_c_vacios, _c_sin_planas, _c_sin_brep, _c_sin_add, _c_excepcion))
    _lineas.append("capas: SF-MASSING-OSM (massing) + TESTIGO-SF (172.5 m) + SF-ORIGEN (cruz 0,0)")
    _lineas.append("origen local 0,0 = templo 41.4036, 2.1744 | CRS nota: ETRS89/UTM31N EPSG:25831")
    _lineas.append("NO se guardo el documento. Guarda como SF-sitio-massing-v01.3dm y valida BoundingBox (manzana ~133 m).")
    _lineas.append("Atribucion para lamina: Massing (c) OpenStreetMap contributors (ODbL). Sin datos Google.")
    print("\n".join(_lineas))
