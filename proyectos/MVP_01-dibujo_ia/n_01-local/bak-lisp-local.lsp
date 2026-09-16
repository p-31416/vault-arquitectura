(defun c:LOC ( / oldecho oldlay oldlw
                 plineEnt obj n i pt
                 v1 v2 mid ang perp testPt center outsidePt)

  (defun *error* (msg)
    (setvar "clayer" oldlay)
    (setvar "cmdecho" oldecho)
    (setvar "lwdisplay" oldlw)
    (princ (strcat "\n" (if msg msg "Cancelado.")))
    (princ))

  (vl-load-com)
  (setq oldecho (getvar "cmdecho"))
  (setvar "cmdecho" 0)
  (setq oldlay (getvar "clayer"))
  (setq oldlw (getvar "lwdisplay"))
  (setvar "lwdisplay" 1)

  (vl-cmdf "._layer" "_M" "A-MURO" "_C" "7" "" "_L" "CONTINUOUS" "" "_LW" "0.30" "" "")
  (vl-cmdf "._layer" "_M" "A-PTA-" "_C" "1" "" "_L" "CONTINUOUS" "" "_LW" "0.15" "" "")

  ;; Paso 1: polilinea cerrada
  (setvar "clayer" "A-MURO")
  (command "._pline")
  (while (= 1 (logand 1 (getvar "cmdactive")))
    (command pause))
  (if (null (entlast)) (exit))
  (setq plineEnt (entlast))

  ;; Paso 2: centroide
  (setq obj (vlax-ename->vla-object plineEnt))
  (setq n (fix (vlax-curve-getEndParam obj)))
  (setq center (list 0.0 0.0 0.0))
  (setq i 0)
  (repeat n
    (setq pt (vlax-curve-getPointAtParam obj i))
    (setq center (mapcar '+ center pt))
    (setq i (1+ i)))
  (if (> n 0)
    (setq center (list (/ (car center) n) (/ (cadr center) n) 0.0))
    (exit))

  ;; Paso 3: direccion exterior (primer segmento)
  (setq v1 (vlax-curve-getPointAtParam obj 0))
  (setq v2 (vlax-curve-getPointAtParam obj 1))
  (setq mid (list (/ (+ (car v1) (car v2)) 2.0)
                  (/ (+ (cadr v1) (cadr v2)) 2.0) 0.0))
  (setq ang (angle v1 v2))
  (setq perp (+ ang (/ pi 2)))
  (setq testPt (polar mid perp 0.5))
  (if (< (distance testPt center) (distance mid center))
    (setq perp (- perp pi)))
  (setq outsidePt (polar mid perp 0.5))

  ;; Paso 4: offset uniforme 0.15 (original se conserva)
  (command "._offset" 0.15 plineEnt outsidePt "")

  (setvar "clayer" oldlay)
  (setvar "cmdecho" oldecho)
  (setvar "lwdisplay" oldlw)
  (princ "\n--- LOC: muro 0.15 uniforme ---")
  (princ))

(princ "\nLOCAL.lsp cargado. Comando: LOC")
(princ)
