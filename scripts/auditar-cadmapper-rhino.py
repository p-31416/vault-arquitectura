#! python3
# -*- coding: utf-8 -*-
"""
auditar-cadmapper-rhino.py — tipos de objeto + top altos con centroide (plano).
Uso via puente MCP: python scripts\rhino-mcp-cli.py exec scripts\auditar-cadmapper-rhino.py
"""
import rhinoscriptsyntax as rs

_lineas = []
for _capa in ("SF-MASSING-OSM", "SF-MASSING-CADMAPPER"):
    _ids = list(rs.ObjectsByLayer(_capa) or [])
    _tipos = {}
    _altos = []
    for _i in _ids:
        try:
            _t = rs.ObjectType(_i)
        except Exception:
            _t = "?"
        _tipos[_t] = _tipos.get(_t, 0) + 1
        try:
            _bb = rs.BoundingBox(_i)
            _xs = [_p[0] for _p in _bb]
            _ys = [_p[1] for _p in _bb]
            _zs = [_p[2] for _p in _bb]
            _h = max(_zs) - min(_zs)
            _altos.append((_h, (min(_xs) + max(_xs)) / 2.0, (min(_ys) + max(_ys)) / 2.0))
        except Exception:
            pass
    _lineas.append("%s: n=%d tipos=%s" % (_capa, len(_ids), _tipos))
    _altos.sort()
    _altos.reverse()
    for _k in range(min(8, len(_altos))):
        _lineas.append("  top%d: h=%.1f cx=%.1f cy=%.1f" % (_k + 1, _altos[_k][0], _altos[_k][1], _altos[_k][2]))
print("\n".join(_lineas))
