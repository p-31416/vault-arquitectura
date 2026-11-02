#! python3
# -*- coding: utf-8 -*-
"""
construir-massing-caba-rhino.py
===============================

Construye el massing 2.5D del recorte Obelisco (CABA, 600x600 m)
dentro de Rhino, desde la base GCBA filtrada con
``scripts/filtrar-tejido-caba.py`` (Tejido Urbano, CC-BY-2.5-AR).

Uso (linea de comandos de Rhino)::

    _RunPythonScript "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\scripts\\construir-massing-caba-rhino.py"

Archivo nuevo sugerido: metros, ``CABA-obelisco-massing-v01.3dm``.
El script NO guarda el documento (decision del estudio, igual que en Sagrada).

IronPython 2.7 / RhinoPython 3 compatible. 100 % plano: el puente MCP
ejecuta sin ``def`` visibles (bug ya documentado en Sagrada).
"""

import json
import os

import Rhino
import System
import rhinoscriptsyntax as rs
import scriptcontext as sc

# NOTA ES: base filtrada (fuera de git) + altura real del catastro GCBA.
# Aqui NO hay regla levels x 3.1: la altura viene en metros de fotogrametria.
_base_json = "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\activos\\research\\2026-11-01-massing-caba\\caba-tejido-obelisco.json"

_lineas = []
if not os.path.exists(_base_json):
    _lineas.append("ERROR: no existe la base filtrada: " + _base_json)
    _lineas.append("Corre antes: P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\filtrar-tejido-caba.py")
    print("\n".join(_lineas))
else:
    with open(_base_json, "r", encoding="utf-8") as _f:
        _data = json.load(_f)
    _vuls = _data.get("vols", [])
    _origen = _data.get("origen", [])
    _lineas.append("volumenes: %d | origen local: lat %s lon %s" % (len(_vuls), _origen[0], _origen[1]))

    if not rs.IsLayer("CABA-MASS-TEJIDO"):
        rs.AddLayer("CABA-MASS-TEJIDO", (200, 200, 200))
    if not rs.IsLayer("CABA-ORIGEN"):
        rs.AddLayer("CABA-ORIGEN", (255, 0, 0))

    _ok = 0
    _salteados = 0
    _c_sin_brep = 0
    _c_excepcion = 0
    for _v in _vuls:
        _xs = _v.get("x", [])
        _ys = _v.get("y", [])
        if len(_xs) < 3 or len(_xs) != len(_ys):
            _salteados += 1
            continue
        # NOTA ES: extrusion recta +Z con altura REAL del Tejido (h viene en metros).
        _h = max(3.0, float(_v.get("h", 3.0)))
        try:
            _p3d = []
            for _i in range(len(_xs)):
                _p3d.append(Rhino.Geometry.Point3d(_xs[_i], _ys[_i], 0.0))
            _crv = sc.doc.Objects.AddPolyline(_p3d)
            if _crv == System.Guid.Empty:
                _salteados += 1
                continue
            _ext = rs.ExtrudeCurveStraight(_crv, (0, 0, 0), (0, 0, _h))
            sc.doc.Objects.Delete(_crv, True)
            if not _ext:
                _salteados += 1
                _c_sin_brep += 1
                continue
            # NOTA ES: CapPlanarHoles igual que Sagrada (14 sin tapa sirven igual).
            rs.CapPlanarHoles(_ext)
            rs.ObjectLayer(_ext, "CABA-MASS-TEJIDO")
            _ok += 1
        except Exception as _ex:
            _salteados += 1
            _c_excepcion += 1
            if _c_excepcion <= 2:
                _lineas.append("EXC ejemplo: %s: %s" % (_ex.__class__.__name__, str(_ex)[:200]))

    # NOTA ES: cruz de origen (0,0) para encuadrar, igual que SF-ORIGEN.
    try:
        _l1 = rs.AddLine((-10, 0, 0), (10, 0, 0))
        _l2 = rs.AddLine((0, -10, 0), (0, 10, 0))
        for _l in (_l1, _l2):
            if _l:
                rs.ObjectLayer(_l, "CABA-ORIGEN")
    except Exception:
        pass

    sc.doc.Views.Redraw()
    _lineas.append("extruidos OK: %d | salteados: %d (sin_brep=%d excepcion=%d)" % (_ok, _salteados, _c_sin_brep, _c_excepcion))
    _lineas.append("capas: CABA-MASS-TEJIDO (alturas reales GCBA) + CABA-ORIGEN (cruz 0,0)")
    _lineas.append("NO se guardo el documento. Guarda como CABA-obelisco-massing-v01.3dm.")
    _lineas.append("Atribucion para lamina: Tejido Urbano (c) Gobierno de la Ciudad de Buenos Aires (CC-BY 2.5 AR).")
    print("\n".join(_lineas))
