;;; ============================================================================
;;; SET-01-HORIZ.lsp  --  Horizontalaizacion de rotulos de locales (capa NPT)
;;; Proyecto: SET_01-REP (REP-ARAOZ) / MVP_02-autocad-standards
;;;
;;; QUE HACE:
;;;   Lee el angulo de giro (twist) de los VIEWPORT del layout elegido y
;;;   calcula el angulo de compensacion para que los rotulos de locales
;;;   (capa A-SIMBOLO-NPT-PLANTA = "LOCALES+NIVELES") se lean HORIZONTALES
;;;   en la lamina impresa.
;;;
;;; POR QUE HACE FALTA (medido en REP-ARAOZ.dwg el 2026-10-19):
;;;   En el layout REP-PTipo-A1-H el viewport del plano (handle 1EC35) tiene
;;;   twist = 270 grados. El viewport gira TODO el model space 270 grados al
;;;   imprimir, asi que un texto dibujado a 0 grados en el modelo se ve a 270
;;;   grados en la lamina: vertical, leyendo de abajo hacia arriba.
;;;   Para que un texto del modelo aparezca horizontal en el papel:
;;;       COMPENSACION = (- twist) mod 360     (con twist 270 -> 90)
;;;   El layout REP-PTipo-A1 tiene su viewport del plano (70FE) con twist = 0,
;;;   por eso alli los rotulos se ven horizontales sin tocar nada.
;;;
;;; COMANDOS:
;;;   HORIZ-ANALIZA   informa (no modifica nada): viewports + twist + rotulos
;;;   HORIZ-APLICA    aplica la compensacion a los rotulos de la capa NPT
;;;   HORIZ-RESTAURA  devuelve los rotulos a su rotacion original
;;;   HORIZ-VP0       deja el twist de un viewport en 0 (alternativa sin tocar
;;;                   el modelo: el plano vuelve a quedar vertical en la hoja)
;;;
;;; COMO SE USA (AutoCAD LT 2027 / AutoCAD 2027):
;;;   1. APPLOAD -> elegir este archivo -> Load
;;;   2. HORIZ-ANALIZA (Enter) y leer el reporte
;;;   3. HORIZ-APLICA y confirmar
;;;   4. UNDO o HORIZ-RESTAURA si algo no cierra
;;;
;;; NOTA ES: No usa COM ni VBA: solo AutoLISP + vlax (ActiveX interno), que es
;;; NOTA ES: lo unico que AutoCAD LT permite (help oficial ACDLT 2027).
;;; ============================================================================

(vl-load-com)

;;; ---------------------------------------------------------------------------
;;; Utilidades
;;; ---------------------------------------------------------------------------

(defun SET-H:GetLayout (name / doc lays lay l)
  ;; Devuelve el objeto Layout con ese nombre, o nil.
  (setq doc (vla-get-ActiveDocument (vlax-get-acad-object)))
  (setq lays (vla-get-Layouts doc))
  (vlax-for l lays
    (if (= (vla-get-Name l) name)
      (setq lay l)))
  lay)

(defun SET-H:RotEnt (ent / d v)
  ;; Rotacion en GRADOS de una entidad (grupo 50 del DXF).
  ;; TEXT/MTEXT/INSERT guardan aqui el giro; 0 si no tienen grupo 50.
  (setq d (entget ent))
  (setq v (cdr (assoc 50 d)))
  (if v v 0.0))

(defun SET-H:Mod50 (ent nuevo / d v)
  ;; Escribe un nuevo giro (grados) en el grupo 50 de la entidad.
  ;; Si la entidad no tiene grupo 50, lo agrega.
  (setq d (entget ent))
  (setq v (assoc 50 d))
  (if v
    (entmod (subst (cons 50 nuevo) v d))
    (entmod (append d (list (cons 50 nuevo)))))
  (entupd ent))

(defun SET-H:Mod360 (a / r)
  ;; Modulo 360 que tambien funciona con numeros negativos
  ;; (en AutoLISP "rem" conserva el signo del dividendo).
  (setq r (rem (fix (* a 1000.0)) 360000.0))
  (if (< r 0.0) (setq r (+ r 360000.0)))
  (/ r 1000.0))

(defun SET-H:Compensa (twist) (SET-H:Mod360 (- 0.0 twist)))

(defun SET-H:TwistViewport (ent / d v)
  ;; Twist (giro de la vista) de un VIEWPORT, en GRADOS (grupo 50 del DXF).
  (setq d (entget ent))
  (setq v (cdr (assoc 50 d)))
  (if v v 0.0))

(defun SET-H:ModTwistViewport (ent nuevo / d v)
  ;; Escribe el twist del viewport (grupo 50).
  (setq d (entget ent))
  (setq v (assoc 50 d))
  (if v
    (entmod (subst (cons 50 nuevo) v d))
    (entmod (append d (list (cons 50 nuevo)))))
  (entupd ent))

(defun SET-H:Viewports (lay / blk res en)
  ;; Lista de (handle . twist-grados) de los VIEWPORT de un layout.
  (setq res '())
  (setq blk (vla-get-Block lay))
  (vlax-for en blk
    (if (= (vla-get-ObjectName en) "AcDbViewport")
      (progn
        (setq res
          (cons
            (cons (vla-get-Handle en)
                  (SET-H:TwistViewport (vlax-vla->ename en)))
            res)))))
  res)

(defun SET-H:Rotulos (capa / msp res en)
  ;; Lista de enames INSERT de model space en la capa pedida.
  (setq msp (vla-get-ModelSpace (vla-get-ActiveDocument (vlax-get-acad-object))))
  (setq res '())
  (vlax-for en msp
    (if (and (= (vla-get-ObjectName en) "AcDbBlockReference")
             (= (vla-get-Layer en) capa))
      (setq res (cons (vlax-vla->ename en) res))))
  res)

(defun SET-H:Atributos (ent / res a)
  ;; Lista de enames de los atributos (ATTRIB) de un INSERT.
  ;; entget de un bloque referencia ya trae los ATTRIB encadenados: cada uno
  ;; arranca con (-1 . handle) y sigue con (0 . "ATTRIB").
  (setq res '())
  (foreach a (entget ent)
    (if (= (cdr (assoc 0 a)) "ATTRIB")
      (setq res (cons (cdr (assoc -1 a)) res))))
  res)

(defun SET-H:XDataOrig (ent valor)
  ;; Guarda la rotacion original del bloque en XData "SET_HORIZ" para poder
  ;; deshacer con HORIZ-RESTAURA. El XData va al final de la lista de entget:
  ;;   (1001 . "NOMBRE_APP") (1000 . "dato") (-3 . "NOMBRE_APP")
  (entmod
    (append (entget ent)
            (list (cons 1001 "SET_HORIZ")
                  (cons 1000 (rtos valor 2 3))
                  (cons -3 "SET_HORIZ"))))
  (entupd ent))

(defun SET-H:LeerXDataOrig (ent / d res)
  ;; Lee del XData la rotacion original guardada (nil si no hay).
  ;; El grupo 1000 solo existe dentro del XData, asi que es seguro buscarlo.
  (setq res nil)
  (setq d (entget ent '("SET_HORIZ")))
  (if (assoc 1000 d)
    (setq res (atof (cdr (assoc 1000 d)))))
  res)

(defun SET-H:PreguntarLayout (/ r)
  (setq r (getkword
    "\nLayout objetivo [REP-PTipo-A1-H/REP-PTipo-A1] <REP-PTipo-A1-H>: "))
  (if (= r "REP-PTipo-A1") "REP-PTipo-A1" "REP-PTipo-A1-H"))

(defun SET-H:PlanViewport (twists / mejor it)
  ;; Elige el viewport "del plano": el primero con giro distinto de cero.
  ;; (en REP-ARAOZ.dwg hay uno solo: 1EC35 con 270 en el layout -H)
  (setq mejor nil)
  (foreach it twists
    (if (and (/= (cdr it) 0.0) (not mejor))
      (setq mejor it)))
  mejor)

;;; ---------------------------------------------------------------------------
;;; Comandos
;;; ---------------------------------------------------------------------------

(defun c:HORIZ-ANALIZA (/ lay twists vp comp n cuenta c r it e)
  (setq lay (SET-H:GetLayout (SET-H:PreguntarLayout)))
  (if (null lay)
    (progn (princ "\nNo se encontro el layout.") (princ) (exit)))

  (setq twists (SET-H:Viewports lay))
  (princ (strcat "\n=== LAYOUT " (vla-get-Name lay) " ==="))
  (foreach it twists
    (princ (strcat "\n  Viewport " (car it) "  twist = " (rtos (cdr it) 2 0) " grados")))

  (setq vp (SET-H:PlanViewport twists))
  (if (null vp)
    (princ "\n  (ningun viewport con giro: los rotulos ya se ven horizontales)")
    (progn
      (setq comp (SET-H:Compensa (cdr vp)))
      (princ (strcat "\n  Viewport del plano: " (car vp)
                     " -> compensacion necesaria = " (rtos comp 2 0) " grados"))))

  (setq n 0)
  (setq cuenta '())
  (foreach e (SET-H:Rotulos "A-SIMBOLO-NPT-PLANTA")
    (setq n (1+ n))
    (setq r (SET-H:RotEnt e))
    (setq cuenta (cons (list r (cdr (assoc 2 (entget e)))) cuenta)))

  (princ (strcat "\n  Rotulos de locales en A-SIMBOLO-NPT-PLANTA: " (itoa n)))
  (if (= n 0)
    (princ "\n  (no hay INSERT en esa capa)")
    (progn
      (princ "\n  Giro actual de cada rotulo y como queda en la lamina:")
      (foreach c cuenta
        (princ (strcat "\n    rot " (rtos (car c) 2 3) "  bloque " (cadr c)
                       "  -> en la lamina a " (rtos (SET-H:Mod360 (+ (car c) (if vp (cdr vp) 0.0))) 2 0)
                       " grados")))))

  (princ "\n  Siguiente paso: HORIZ-APLICA (aplica la compensacion).")
  (princ "\n")
  (princ))

(defun c:HORIZ-APLICA (/ lay twists vp comp e orig atrib n)
  (setq lay (SET-H:GetLayout (SET-H:PreguntarLayout)))
  (if (null lay)
    (progn (princ "\nNo se encontro el layout.") (princ) (exit)))

  (setq twists (SET-H:Viewports lay))
  (setq vp (SET-H:PlanViewport twists))
  (if (null vp)
    (progn (princ "\nNo hay viewport con giro: no hace falta compensar.") (princ) (exit)))

  (setq comp (SET-H:Compensa (cdr vp)))
  (princ (strcat "\nCompensacion a aplicar: " (rtos comp 2 0) " grados"))
  (princ "\nAfecta: capa A-SIMBOLO-NPT-PLANTA (rotulos de locales)")
  (if (/= (getkword "\nConfirmar? [S/N] <N>: ") "S")
    (progn (princ "\nCancelado.") (princ) (exit)))

  (setq n 0)
  (foreach e (SET-H:Rotulos "A-SIMBOLO-NPT-PLANTA")
    (setq orig (SET-H:RotEnt e))
    (if (null (SET-H:LeerXDataOrig e))
      (SET-H:XDataOrig e orig))
    (SET-H:Mod50 e comp)
    ;; los atributos (DESCRIPCION / No) giran con el bloque: hay que fijarlos
    (foreach atrib (SET-H:Atributos e)
      (SET-H:Mod50 atrib comp))
    (setq n (1+ n)))

  (princ (strcat "\nRotulos actualizados: " (itoa n)))
  (princ "\nDeshacer: UNDO o comando HORIZ-RESTAURA\n")
  (princ))

(defun c:HORIZ-RESTAURA (/ lay e orig atrib n)
  (setq lay (SET-H:GetLayout (SET-H:PreguntarLayout)))
  (if (null lay)
    (progn (princ "\nNo se encontro el layout.") (princ) (exit)))
  (if (/= (getkword "\nRestaurar rotulos a su giro original? [S/N] <N>: ") "S")
    (progn (princ "\nCancelado.") (princ) (exit)))

  (setq n 0)
  (foreach e (SET-H:Rotulos "A-SIMBOLO-NPT-PLANTA")
    (setq orig (SET-H:LeerXDataOrig e))
    (if orig
      (progn
        (SET-H:Mod50 e orig)
        (foreach atrib (SET-H:Atributos e)
          (SET-H:Mod50 atrib orig))
        (setq n (1+ n)))))
  (princ (strcat "\nRotulos restaurados: " (itoa n)))
  (princ "\n")
  (princ))

(defun c:HORIZ-VP0 (/ lay twists vp blk ent)
  ;; Alternativa: dejar el twist del viewport en 0 (el plano vuelve a quedar
  ;; vertical en la hoja y el modelo no se toca).
  (setq lay (SET-H:GetLayout (SET-H:PreguntarLayout)))
  (if (null lay)
    (progn (princ "\nNo se encontro el layout.") (princ) (exit)))
  (setq twists (SET-H:Viewports lay))
  (setq vp (SET-H:PlanViewport twists))
  (if (null vp)
    (progn (princ "\nNo hay viewport con giro.") (princ) (exit)))
  (princ (strcat "\nViewport " (car vp) " twist actual = " (rtos (cdr vp) 2 0)))
  (if (/= (getkword "\nDejarlo en 0 grados? [S/N] <N>: ") "S")
    (progn (princ "\nCancelado.") (princ) (exit)))
  (setq blk (vla-get-Block lay))
  (vlax-for ent blk
    (if (= (vla-get-ObjectName ent) "AcDbViewport")
      (if (= (vla-get-Handle ent) (car vp))
        (SET-H:ModTwistViewport (vlax-vla->ename ent) 0.0))))
  (princ "\nTwist del viewport = 0. REGEN para ver el cambio.\n")
  (princ))

(princ "\nSET-01-HORIZ.lsp cargado. Comandos: HORIZ-ANALIZA, HORIZ-APLICA, HORIZ-RESTAURA, HORIZ-VP0\n")
(princ)
