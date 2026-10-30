#! python3
# -*- coding: utf-8 -*-
"""
comparar-altos-osm-cm-rhino.py — nuestros altos (>=30 m) vs vecino CADMapper.
Uso: python scripts\rhino-mcp-cli.py exec scripts\comparar-altos-osm-cm-rhino.py
"""
import rhinoscriptsyntax as rs

_lineas = []
_ids_cm = list(rs.ObjectsByLayer("SF-MASSING-CADMAPPER") or [])
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
_lineas.append("cadmapper con altura: %d" % len(_cm))

_osm = list(rs.ObjectsByLayer("SF-MASSING-OSM") or [])
_altos = []
for _i in _osm:
    try:
        _bb = rs.BoundingBox(_i)
    except Exception:
        continue
    _ox = [_p[0] for _p in _bb]
    _oy = [_p[1] for _p in _bb]
    _oz = [_p[2] for _p in _bb]
    _oh = max(_oz) - min(_oz)
    if _oh < 30.0:
        continue
    _ocx = (min(_ox) + max(_ox)) / 2.0
    _ocy = (min(_oy) + max(_oy)) / 2.0
    _altos.append((_ocx, _ocy, _oh))
_lineas.append("osm >=30 m: %d" % len(_altos))
for _k in range(len(_altos)):
    _x = _altos[_k][0]
    _y = _altos[_k][1]
    _h = _altos[_k][2]
    _best = -1.0
    _bd = 1e9
    for _j in range(len(_cm)):
        _ddx = _cm[_j][0] - _x
        _ddy = _cm[_j][1] - _y
        _d = abs(_ddx) + abs(_ddy)
        if _d < _bd:
            _bd = _d
            _best = _cm[_j][2]
    if _best >= 0.0 and _bd < 20.0:
        _lineas.append("osm h=%.1f en (%.0f,%.0f) <-> cm h=%.1f (d=%.1f m) dif=%+.1f" % (_h, _x, _y, _best, _bd, _best - _h))
    else:
        _lineas.append("osm h=%.1f en (%.0f,%.0f) <-> SIN vecino (d=%.1f m)" % (_h, _x, _y, _bd))
print("\n".join(_lineas))
