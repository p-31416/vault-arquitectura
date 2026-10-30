#! python3
# -*- coding: utf-8 -*-
"""
alinear-comparar-cadmapper-rhino.py — lleva el CADMapper a origen (templo con
templo) y compara alturas edificio a edificio (plano, via MCP).
Uso: python scripts\rhino-mcp-cli.py exec scripts\alinear-comparar-cadmapper-rhino.py
"""
import rhinoscriptsyntax as rs

_lineas = []
_ids_cm = list(rs.ObjectsByLayer("SF-MASSING-CADMAPPER") or [])
# NOTA ES: centroide del objeto mas alto (templo, h=170) medido en auditoria.
_cx, _cy = 1490.4, 623.3
rs.MoveObjects(_ids_cm, (-_cx, -_cy, 0.0))
_lineas.append("cadmapper movido (templo con templo): dx=%.1f dy=%.1f" % (-_cx, -_cy))

# NOTA ES: indice de centroides cadmapper (solo piezas con altura >= 1 m).
_cm = []
for _i in _ids_cm:
    try:
        _bb = rs.BoundingBox(_i)
    except Exception:
        continue
    _bxs = [_p[0] for _p in _bb]
    _bys = [_p[1] for _p in _bb]
    _bzs = [_p[2] for _p in _bb]
    _bh = max(_bzs) - min(_bzs)
    if _bh < 1.0:
        continue
    _ccx = (min(_bxs) + max(_bxs)) / 2.0
    _ccy = (min(_bys) + max(_bys)) / 2.0
    _cm.append((_ccx, _ccy, _bh))
_lineas.append("cadmapper con altura>=1m: %d" % len(_cm))

# NOTA ES: los 12 mas altos OSM vs vecino cadmapper mas cercano (radio 20 m).
_osm = list(rs.ObjectsByLayer("SF-MASSING-OSM") or [])
_m = []
for _i in _osm:
    try:
        _bb = rs.BoundingBox(_i)
    except Exception:
        continue
    _ox = [_p[0] for _p in _bb]
    _oy = [_p[1] for _p in _bb]
    _oz = [_p[2] for _p in _bb]
    _ocx = (min(_ox) + max(_ox)) / 2.0
    _ocy = (min(_oy) + max(_oy)) / 2.0
    _oh = max(_oz) - min(_oz)
    _m.append((_ocx, _ocy, _oh))
_m.sort()
_m.reverse()
_comp = 0
for _k in range(min(12, len(_m))):
    _x = _m[_k][0]
    _y = _m[_k][1]
    _h = _m[_k][2]
    _best = -1.0
    _bd = 1e9
    for _j in range(len(_cm)):
        _dx = _cm[_j][0] - _x
        _dy = _cm[_j][1] - _y
        _d = abs(_dx) + abs(_dy)
        if _d < _bd:
            _bd = _d
            _best = _cm[_j][2]
    if _best >= 0.0 and _bd < 20.0:
        _lineas.append("osm h=%.1f en (%.0f,%.0f) <-> cadmapper h=%.1f (d=%.1f m) dif=%+.1f" % (_h, _x, _y, _best, _bd, _best - _h))
        _comp = _comp + 1
_lineas.append("comparados: %d" % _comp)
print("\n".join(_lineas))
