;;; ============================================================================
;;; SET-01-NORM-TEXTOS.lsp  --  Normaliza los giros de los textos de bloque
;;; Proyecto: SET_01-REP (REP-ARAOZ) / MVP_02-autocad-standards
;;;
;;; QUE HACE:
;;;   Los textos que viven DENTRO de un bloque (el codigo de muro, el numero de
;;;   vano, la medida de columna) giran con el bloque cuando el bloque se
;;;   inserta con angulo. Eso obliga a corregir el texto ejemplar por ejemplar.
;;;   Este comando lo hace de una: a cada atributo le deja el giro en 0 grados
;;;   (texto siempre horizontal) y le BLOQUEA la posicion, para que de aqui en
;;;   mas no vuelva a girar con el bloque.
;;;
;;; COMANDOS:
;;;   NORM-TEXTOS    revisa y normaliza los atributos de los bloques de las
;;;                  capas indicadas (por defecto SIMB-MURO, A-CARP-02, E-COL)
;;;   NORM-LOCALES  deja en 0 grados los rotulos de local que esten girados
;;;                  (los que quedaron en 90 / 180 / 270)
;;;
;;; COMO SE USA (AutoCAD LT 2027 / AutoCAD 2027):
;;;   1. APPLOAD -> este archivo -> Load
;;;   2. NORM-TEXTOS   (muestra el informe y pide confirmacion)
;;;   3. NORM-LOCALES
;;;   4. UNDO para volver atras, o REGEN
;;;
;;; NOTA ES: "giro 0" = el texto se lee horizontal en el MODELO. Como el viewport
;;; NOTA ES: de REP-PTipo-A1-H quedo con twist 360 (= 0), en la lamina se lee
;;; NOTA ES: horizontal tambien. Si un dia se vuelve a girar el viewport, hay
;;; NOTA ES: que compensar el giro (ver SET-01-HORIZ.lsp).
;;; ============================================================================

(defun SET-N:CapasDef ()
  '("SIMB-MURO" "A-CARP-02" "E-COL"))

(defun SET-N:Attrs (ename / res a)
  ;; Lista de enames de los atributos (ATTRIB) de un INSERT.
  (setq res '())
  (foreach a (entget ename)
    (if (= (cdr (assoc 0 a)) "ATTRIB")
      (setq res (cons (cdr (assoc -1 a)) res))))
  res)

(defun SET-N:Giro (ename / d v)
  (setq d (entget ename))
  (setq v (cdr (assoc 50 d)))
  (if v v 0.0))

(defun SET-N:FijarGiro (ename valor / d v)
  ;; Escribe el giro (grados) en el grupo 50.
  (setq d (entget ename))
  (setq v (assoc 50 d))
  (if v
    (entmod (subst (cons 50 valor) v d))
    (entmod (append d (list (cons 50 valor)))))
  (entupd ename))

(defun SET-N:BloquearPosicion (ename / d v)
  ;; Suma el bit 16 (bloquear posicion) a los flags del atributo (grupo 70).
  ;; Con la posicion bloqueada, el texto no vuelve a girar cuando se mueve o
  ;; gira el bloque.
  (setq d (entget ename))
  (setq v (assoc 70 d))
  (if v
    (entmod (subst (cons 70 (+ (cdr v) 16)) v d))
    (entmod (append d (list (cons 70 16)))))
  (entupd ename))

(defun SET-N:InsertsDe (capa / msp res en)
  (setq msp (vla-get-ModelSpace (vla-get-ActiveDocument (vlax-get-acad-object))))
  (setq res '())
  (vlax-for en msp
    (if (= (vla-get-Layer en) capa)
      (setq res (cons en res))))
  res)

(defun SET-N:Cuenta (capa / inserts atributos a)
  ;; Devuelve (n_inserts n_atributos n_atributos_girados).
  (setq inserts 0)
  (setq atributos 0)
  (setq a 0)
  (foreach en (SET-N:InsertsDe capa)
    (setq inserts (1+ inserts))
    (foreach at (SET-N:Attrs en)
      (setq atributos (1+ atributos))
      (if (/= (SET-N:Giro at) 0.0)
        (setq a (1+ a)))))
  (list inserts atributos a))

;;; ---------------------------------------------------------------------------
;;; Comando principal
;;; ---------------------------------------------------------------------------

(defun c:NORM-TEXTOS (/ capas c tot i attrs n)
  (setq capas (SET-N:CapasDef))
  (princ "\n=== Estado actual (por capa) ===")
  (foreach c capas
    (setq i (SET-N:Cuenta c))
    (princ (strcat "\n  " c
                   "  bloques=" (itoa (nth 0 i))
                   "  atributos=" (itoa (nth 1 i))
                   "  con giro != 0: " (itoa (nth 2 i)))))

  (princ "\n\nSe va a dejar el giro de cada atributo en 0 y bloquear su posicion.\n")
  (if (/= (getkword "\nConfirmar? [S/N] <N>: ") "S")
    (progn (princ "\nCancelado.") (princ) (exit)))

  (setq tot 0)
  (foreach c capas
    (foreach en (SET-N:InsertsDe c)
      (foreach at (SET-N:Attrs en)
        (if (/= (SET-N:Giro at) 0.0)
          (progn
            (SET-N:FijarGiro at 0.0)
            (SET-N:BloquearPosicion at)
            (setq tot (1+ tot)))))))

  (command "_.regen")
  (princ (strcat "\nAtributos normalizados: " (itoa tot)))
  (princ "\nLos bloques NO se movieron: solo cambio el giro y el bloqueo del texto.\n")
  (princ))

;;; ---------------------------------------------------------------------------
;;; Comando: rotulos de locales fuera de norma
;;; ---------------------------------------------------------------------------

(defun c:NORM-LOCALES (/ en n)
  (princ "\n=== Rotulos de local con giro != 0 (capa A-SIMBOLO-NPT-PLANTA) ===")
  (setq n 0)
  (foreach en (SET-N:InsertsDe "A-SIMBOLO-NPT-PLANTA")
    (if (/= (SET-N:Giro en) 0.0)
      (progn
        (princ (strcat "\n  bloque " (cdr (assoc 2 (entget en)))
                       "  giro " (rtos (SET-N:Giro en) 2 2)))
        (setq n (1+ n)))))
  (if (= n 0)
    (progn (princ "\n  (todos en 0) ") (princ) (exit)))
  (if (/= (getkword "\nDejarlos en 0 grados? [S/N] <N>: ") "S")
    (progn (princ "\nCancelado.") (princ) (exit)))
  (foreach en (SET-N:InsertsDe "A-SIMBOLO-NPT-PLANTA")
    (if (/= (SET-N:Giro en) 0.0)
      (SET-N:FijarGiro en 0.0)))
  (command "_.regen")
  (princ (strcat "\nRotulos corregidos: " (itoa n)))
  (princ "\n")
  (princ))

(princ "\nSET-01-NORM-TEXTOS.lsp cargado. Comandos: NORM-TEXTOS, NORM-LOCALES\n")
(princ)
