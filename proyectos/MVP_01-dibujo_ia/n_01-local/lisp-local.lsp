(defun c:LOC ( / oldecho oldlay oldlw
                 plineEnt offsetEnt obj n i pt
                 v1 v2 mid ang perp testPt center outsidePt
                 addVano clickPt doorWidth vanoWidth halfWidth
                 innerObj innerClosest innerDist totalLen innerB1 innerB2
                 outerObj outerClosest outerDist outerB1 outerB2)

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

  ;; Paso 4: offset uniforme 0.15
  (command "._offset" 0.15 plineEnt outsidePt "")
  (setq offsetEnt (entlast))

  ;; Paso 5: vano opcional
  (setvar "cmdecho" oldecho)
  (initget "S N")
  (setq addVano (getkword "\nAgregar vano? [S/N] <S>: "))
  (setvar "cmdecho" 0)
  (if (or (null addVano) (= (strcase addVano) "S"))
    (progn
      (setvar "cmdecho" oldecho)
      (setq clickPt (getpoint "\nSeleccione punto del vano en el muro: "))
      (initget "80 90 100")
      (setq doorWidth (getint "\nAncho de vano [80/90/100] <90>: "))
      (if (null doorWidth) (setq doorWidth 90))
      (setq vanoWidth (+ doorWidth 6))
      (setq halfWidth (/ vanoWidth 2.0))
      (setvar "cmdecho" 0)

      ;; puntos de quiebre — polilinea interior
      (setq innerObj (vlax-ename->vla-object plineEnt))
      (setq innerClosest (vlax-curve-getClosestPointTo innerObj clickPt))
      (setq innerDist (vlax-curve-getDistAtPoint innerObj innerClosest))
      (setq totalLen (vlax-curve-getDistAtParam innerObj (vlax-curve-getEndParam innerObj)))

      (setq innerB1 (- innerDist halfWidth))
      (if (< innerB1 0) (setq innerB1 (+ innerB1 totalLen)))
      (setq innerB2 (+ innerDist halfWidth))
      (if (> innerB2 totalLen) (setq innerB2 (- innerB2 totalLen)))

      ;; puntos de quiebre — polilinea exterior
      (setq outerObj (vlax-ename->vla-object offsetEnt))
      (setq outerClosest (vlax-curve-getClosestPointTo outerObj clickPt))
      (setq outerDist (vlax-curve-getDistAtPoint outerObj outerClosest))
      (setq outerLen (vlax-curve-getDistAtParam outerObj (vlax-curve-getEndParam outerObj)))

      (setq outerB1 (- outerDist halfWidth))
      (if (< outerB1 0) (setq outerB1 (+ outerB1 outerLen)))
      (setq outerB2 (+ outerDist halfWidth))
      (if (> outerB2 outerLen) (setq outerB2 (- outerB2 outerLen)))

      ;; break interior
      (command "._break" plineEnt "_F"
               (vlax-curve-getPointAtDist innerObj innerB1)
               (vlax-curve-getPointAtDist innerObj innerB2))

      ;; break exterior
      (command "._break" offsetEnt "_F"
               (vlax-curve-getPointAtDist outerObj outerB1)
               (vlax-curve-getPointAtDist outerObj outerB2))

      ;; unir puntas
      (setq innerObj (vlax-ename->vla-object plineEnt))
      (setq outerObj (vlax-ename->vla-object offsetEnt))
      (setq innerStart (vlax-curve-getStartPoint innerObj))
      (setq innerEnd (vlax-curve-getEndPoint innerObj))
      (setq outerStart (vlax-curve-getStartPoint outerObj))
      (setq outerEnd (vlax-curve-getEndPoint outerObj))

      (if (< (distance innerStart outerStart) (distance innerStart outerEnd))
        (progn
          (command "._line" innerStart outerStart "")
          (command "._line" innerEnd outerEnd ""))
        (progn
          (command "._line" innerStart outerEnd "")
          (command "._line" innerEnd outerStart "")))))

  (setvar "clayer" oldlay)
  (setvar "cmdecho" oldecho)
  (setvar "lwdisplay" oldlw)
  (princ "\n--- LOC: muro 0.15 uniforme + vano ---")
  (princ))

(princ "\nLOCAL.lsp cargado. Comando: LOC")
(princ)
