# activa lamina A-A (para captura)
import scriptcontext as sc

for _pv in sc.doc.Views.GetPageViews():
    if _pv.PageName == "SF-CORTE-AA":
        sc.doc.Views.ActiveView = _pv
        print("activa: SF-CORTE-AA")
        break
