#! python3
# -*- coding: utf-8 -*-
"""
apoyar-cota-cero-rhino.py — baja cada capa de massing a z=0 (plano comun).
Uso: python scripts\rhino-mcp-cli.py exec scripts\apoyar-cota-cero-rhino.py
"""
import rhinoscriptsyntax as rs

_lineas = []
for _capa in ("SF-MASSING-OSM", "SF-MASSING-CADMAPPER", "TESTIGO-SF", "SF-ORIGEN"):
    _ids = list(rs.ObjectsByLayer(_capa) or [])
    if not _ids:
        _lineas.append("%s: vacia" % _capa)
        continue
    _b = rs.BoundingBox(_ids)
    _zs = [_p[2] for _p in _b]
    _minz = min(_zs)
    _maxz = max(_zs)
    if abs(_minz) < 0.01:
        _lineas.append("%s: ya en cero (z %.2f a %.2f)" % (_capa, _minz, _maxz))
        continue
    rs.MoveObjects(_ids, (0.0, 0.0, -_minz))
    _lineas.append("%s: bajada %.2f m (z ahora 0.00 a %.2f)" % (_capa, _minz, _maxz - _minz))
print("\n".join(_lineas))
