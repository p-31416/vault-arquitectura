# pone ambos detalles en Shaded (las caras del corte se leen macizas)
import Rhino
import scriptcontext as sc

_sh = Rhino.Display.DisplayModeDescription.FindByName("Shaded")
print("modo: " + str(_sh.EnglishName))
for _pv in sc.doc.Views.GetPageViews():
    if _pv.PageName == "SF-CORTE-AA" or _pv.PageName == "SF-CORTE-BB":
        for _d in list(_pv.GetDetailViews()):
            try:
                _d.Viewport.DisplayMode = _sh
                _d.CommitChanges()
                print(str(_pv.PageName) + ": Shaded OK")
            except Exception as _ex:
                print(str(_pv.PageName) + ": " + _ex.__class__.__name__)
sc.doc.Views.Redraw()
