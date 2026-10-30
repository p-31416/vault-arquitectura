#! python3
# -*- coding: utf-8 -*-
"""
apoyar-objetos-cota-cero-rhino.py — baja CADA objeto a z=0 (no la capa).
Uso: python scripts\rhino-mcp-cli.py exec scripts\apoyar-objetos-cota-cero-rhino.py
Lento a proposito (un objeto por vez): ~6600 objetos, varios minutos.
"""
import rhinoscriptsyntax as rs

_lineas = []
for _capa in ("SF-MASSING-CADMAPPER",):
    _ids = list(rs.ObjectsByLayer(_capa) or [])
    _mov = 0
    _dmax = 0.0
    _dmin = 1e9
    for _i in _ids:
        try:
            _bb = rs.BoundingBox(_i)
        except Exception:
            continue
        _zs = [_p[2] for _p in _bb]
        _mz = min(_zs)
        if abs(_mz) < 0.01:
            if _mz < _dmin:
                _dmin = _mz
            continue
        rs.MoveObject(_i, (0.0, 0.0, -_mz))
        _mov = _mov + 1
        if _mz > _dmax:
            _dmax = _mz
        if _mz < _dmin:
            _dmin = _mz
    _lineas.append("%s: n=%d movidos=%d offset_min=%.2f offset_max=%.2f" % (_capa, len(_ids), _mov, _dmin, _dmax))
    _b = rs.BoundingBox(list(rs.ObjectsByLayer(_capa) or []))
    _zs = [_p[2] for _p in _b]
    _lineas.append("%s ahora: z %.2f a %.2f" % (_capa, min(_zs), max(_zs)))
print("\n".join(_lineas))
