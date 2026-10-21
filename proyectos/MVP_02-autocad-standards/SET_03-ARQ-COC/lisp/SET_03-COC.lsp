; SET_03-COC.lsp — v0.1 base real cocina Tagle
; Ejecutar: SET-03-COC
; NOTA ES: crea capas mínimas + fija metros y escalas 1:50/1:20

(defun c:SET-03-COC (/)
  (vl-load-com) ; NOTA ES: carga API ActiveX
  (foreach l
    '(("A-MURO" 7 "CONTINUOUS")
      ("A-SOLADOS" 250 "CONTINUOUS")
      ("A-CARPINTERIA" 2 "CONTINUOUS")
      ("A-EQUIPAMIENTO" 251 "CONTINUOUS")
      ("A-COTAS" 7 "CONTINUOUS")
      ("A-VISTA-1" 254 "CONTINUOUS")
      ("A-HATCH-SOLADO" 8 "CONTINUOUS"))
    (entmake (list '(0 . "LAYER") '(100 . "AcDbSymbolTableRecord")
      '(100 . "AcDbLayerTableRecord") (cons 2 (car l))
      (cons 62 (cadr l)) (cons 6 (caddr l)) '(70 . 0))))
  (setvar "INSUNITS" 6) ; NOTA ES: metros
  (setvar "LUNITS" 2) ; NOTA ES: decimal
  (setvar "LUPREC" 2) ; NOTA ES: 2 decimales
  (princ "\nSET-03-COC v0.1 aplicado.")
  (princ)
)
