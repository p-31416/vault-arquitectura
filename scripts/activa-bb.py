# activa lamina B-B (para captura)
import scriptcontext as sc

for _pv in sc.doc.Views.GetPageViews():
    if _pv.PageName == "SF-CORTE-BB":
        sc.doc.Views.ActiveView = _pv
        print("activa: SF-CORTE-BB")
        break
