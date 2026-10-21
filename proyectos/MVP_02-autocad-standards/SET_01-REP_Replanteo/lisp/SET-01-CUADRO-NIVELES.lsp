;;; ============================================================================
;;; SET-01-CUADRO-NIVELES.lsp  --  Planilla de niveles (el CSV es la fuente)
;;; Proyecto: SET_01-REP (REP-ARAOZ) / MVP_02-autocad-standards
;;;
;;; QUE HACE:
;;;   Lee el CSV de la planilla (docs/planilla-niveles.csv) y dibuja la tabla
;;;   en el DWG. Editas el CSV -> CUADRO-NIVELES-ACT -> la tabla se actualiza.
;;;   El CSV es la UNICA fuente de datos: el dibujo es su vista.
;;;
;;; COMANDOS:
;;;   CUADRO-NIVELES        dibuja la tabla (o la actualiza si ya existe)
;;;   CUADRO-NIVELES-ACT    actualiza la tabla del dibujo desde el CSV
;;;   CUADRO-NIVELES-NUEVO  borra la tabla y la dibuja de nuevo en otro punto
;;;   CUADRO-NIVELES-VAL    muestra el CSV en la linea de comandos
;;;
;;; POR QUE NO UN VINCULO DE DATOS (DATA LINK) DE AUTOCAD:
;;;   El vinculo de datos de AutoCAD (DATALINK) necesita Excel instalado o el
;;;   proveedor ACE OLE DB para leer un CSV. En esta maquina no hay ninguno de
;;;   los dos (doc oficial ACDLT 2027: "Microsoft Excel must be installed to
;;;   use Microsoft Excel data links"), asi que el vinculo no llega ni a
;;;   preview. Esta version hace lo mismo con AutoLISP: el CSV manda.
;;;
;;; USO (AutoCAD LT 2027 / AutoCAD 2027):
;;;   1. APPLOAD -> este archivo -> Load
;;;   2. CUADRO-NIVELES -> click en el punto de insercion
;;;   3. (opcional) LAYOUT -> REP-PTipo-A1-H -> ESPACIO PAPER
;;;   4. CUADRO-NIVELES-ACT cada vez que cambia el CSV
;;;
;;; NOTA ES: cada corrida deja un registro en raw/reports/cuadro-niveles.txt
;;; ============================================================================

;;; ---------------------------------------------------------------------------
;;; Parametros
;;; ---------------------------------------------------------------------------

(defun SET-N:CSV ()
  "El CSV con los datos: es la fuente de verdad de la planilla."
  "P:/00-repos/proyecto-pi/vault-arquitectura/proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-niveles.csv")

(defun SET-N:LAYER () "A-CUADRO-NIVELES")   ; capa de la tabla
(defun SET-N:ESTILO () "Standard")            ; estilo de texto

(defun SET-N:ALTO-FILA ()
  "Alto de fila de la tabla. 7 mm en paper space, 0.70 m en modelo."
  (if (= 0 (getvar "CVPORT")) 7.0 0.70))

(defun SET-N:ALTO-TXT (alto) (/ alto 1.8))

(defun SET-N:ANCHO-COL (i)
  "Ancho de la columna i (1, 2, 3), segun el alto de fila."
  (let ((a (SET-N:ALTO-FILA)))
    (cond ((= i 1) (* a 5.0))
          ((= i 2) (* a 3.8))
          (T (* a 4.0)))))

(defun SET-N:NOTAS ()
  "Textos al pie de la planilla (no van en el CSV: son texto fijo)."
  (list
    "Niveles en metros, sobre el nivel 0.00 de planta baja."
    "Exterior (balcon): 5 cm por debajo del nivel interior terminado."
    "9 PISO: plantas técnicas. 32.06 es la altura máxima (tanque)."))

(defun SET-N:TITULO () "PLANILLA DE NIVELES - REP-ARAOZ")

;;; ---------------------------------------------------------------------------
;;; Estado de la tabla en el dibujo (para poder actualizarla en el sitio)
;;; ---------------------------------------------------------------------------

(setq SET-N:PUNTO nil)     ; punto de insercion de la tabla
(setq SET-N:CAJA nil)      ; (xmin ymin xmax ymax) de la tabla
(setq SET-N:CAPA "A-CUADRO-NIVELES")
(setq SET-N:LOG-TEXTO '())

;;; ---------------------------------------------------------------------------
;;; Lectura del CSV (la fuente de datos)
;;; ---------------------------------------------------------------------------

(defun SET-N:QuitaBOM (linea)
  "Saca el BOM (3 bytes) del inicio de la primera linea del CSV."
  (if (and (> (strlen linea) 3)
           (= (char-code (substr linea 1 1)) 239)
           (= (char-code (substr linea 2 1)) 187)
           (= (char-code (substr linea 3 1)) 191))
    (substr linea 4)
    linea))

(defun SET-N:Separa (linea / celdas i ch)
  "Separa una linea de CSV por comas (sin comillas ni saltos)."
  (setq celdas '())
  (setq i 1)
  (while (<= i (strlen linea))
    (setq ch (substr linea i 1))
    (if (= ch ",")
      (progn (setq celdas (cons "" celdas)) (setq i (+ i 1)))
      (progn
        (setq celdas (cons (strcat (car celdas) ch) celdas))
        (setq i (+ i 1)))))
  (setq celdas (cons (if celdas (car celdas) "") celdas))
  (reverse celdas))

(defun SET-N:LeeCSV (/ f line filas)
  "Devuelve la lista de filas del CSV (cada fila, una lista de celdas).
   nil si no se puede abrir el archivo."
  (setq f (open (SET-N:CSV) "r"))
  (if (null f)
    nil
    (progn
      (while (setq line (read-line f))
        (setq filas (cons (SET-N:Separa (SET-N:QuitaBOM line)) filas)))
      (close f)
      (reverse filas))))

;;; ---------------------------------------------------------------------------
;;; Registro de la corrida (raw/reports/cuadro-niveles.txt)
;;; ---------------------------------------------------------------------------

(defun SET-N:Log (txt)
  (setq SET-N:LOG-TEXTO (cons txt SET-N:LOG-TEXTO)))

(defun SET-N:LogDump (/ f x)
  (setq f (open "P:/00-repos/proyecto-pi/vault-arquitectura/raw/reports/cuadro-niveles.txt" "w"))
  (if f
    (progn
      (foreach x (reverse SET-N:LOG-TEXTO) (write-line x f))
      (close f))
    (princ "\nNo se pudo escribir el registro.")))

;;; ---------------------------------------------------------------------------
;;; Utilidades de dibujo
;;; ---------------------------------------------------------------------------

(defun SET-N:ExisteCapa (nombre / r)
  "Crea la capa si no existe. NO usa el comando -layer (dejaba la linea de
   comandos colgada en el prompt de opciones): se crea con entmake."
  (if (null (tblsearch "LAYER" nombre))
    (progn
      (setq r (entmake (list '(0. "LAYER")
                              '(100. "AcDbSymbolTableRecord")
                              '(100. "AcDbLayerTableRecord")
                              (cons 2 nombre)
                              (cons 70 0)
                              (cons 62 7)
                              (cons 6 "Continuous"))))
      (if (null r)
        (progn
          (command "_.-layer" "_N" nombre "")
          (princ (strcat "\nCapa creada: " nombre))))))
  (if (null (tblsearch "LAYER" nombre))
    (progn (SET-N:Log "La capa no se pudo crear: se dibuja en la capa 0") "0")
    nombre))

(defun SET-N:Linea (p1 p2)
  (entmakex (list '(0. "LINE")
                   (cons 8 SET-N:CAPA)
                   (cons 10 p1)
                   (cons 11 p2))))

(defun SET-N:MTexto (p ancho texto alto alineacion)
  (entmakex (list '(0. "MTEXT")
                   (cons 8 SET-N:CAPA)
                   (cons 10 p)
                   (cons 40 alto)
                   (cons 41 ancho)
                   (cons 1 texto)
                   (cons 7 (SET-N:ESTILO))
                   (cons 50 0.0)
                   (cons 71 alineacion))))

(defun SET-N:BorraTabla (/ ss i e d x y)
  "Borra las entidades de la tabla anterior (solo las de su caja)."
  (if SET-N:CAJA
    (progn
      (setq ss (ssget "_X" (list '(0 . "MTEXT,LINE") (cons 8 SET-N:CAPA))))
      (if ss
        (progn
          (setq i 0)
          (repeat (sslength ss)
            (setq e (ssname ss i))
            (if e
              (progn
                (setq d (entget e))
                (setq x (car (assoc 10 d)))
                (setq y (cadr (assoc 10 d)))
                (if (and x y
                         (>= x (nth 0 SET-N:CAJA)) (<= x (nth 2 SET-N:CAJA))
                         (>= y (nth 1 SET-N:CAJA)) (<= y (nth 3 SET-N:CAJA)))
                  (entdel e))))
            (setq i (1+ i)))))
      (SET-N:Log "Tabla anterior borrada."))))

(defun SET-N:DibujaTabla (filas pto / alto txt-alto anchos alineaciones x0 y0 total
                                   i j fila n ytop xleft xcelda anchoCelda ymin)
  "Dibuja la tabla con los datos del CSV en el punto pto."
  (setq alto (SET-N:ALTO-FILA))
  (setq txt-alto (SET-N:ALTO-TXT alto))
  (setq anchos (list (SET-N:ANCHO-COL 1) (SET-N:ANCHO-COL 2) (SET-N:ANCHO-COL 3)))
  (setq alineaciones (list 1 2 2))
  (setq total (+ (car anchos) (cadr anchos) (caddr anchos)))
  (setq n (length filas))
  (setq x0 (car pto))
  (setq y0 (cadr pto))
  (SET-N:MTexto (list x0 (+ y0 (* alto 0.45)) (* alto 8.8))
                (SET-N:TITULO) (* txt-alto 1.4) 1)
  (setq i 0)
  (foreach fila filas
    (setq ytop (- y0 (* i alto)))
    (setq j 0)
    (setq xleft x0)
    (foreach anchoCelda anchos
      (setq xcelda (+ xleft (* alto 0.30)))
      (SET-N:MTexto (list xcelda (- ytop (* alto 0.30))) (- anchoCelda (* alto 0.60))
                    (nth j fila) txt-alto (nth j alineaciones))
      (setq xleft (+ xleft anchoCelda))
      (setq j (1+ j)))
    (setq i (1+ i)))
  (setq i 0)
  (repeat (1+ n)
    (SET-N:Linea (list x0 (- y0 (* i alto)) 0.0) (list (+ x0 total) (- y0 (* i alto)) 0.0))
    (setq i (1+ i)))
  (setq xleft x0)
  (foreach anchoCelda anchos
    (SET-N:Linea (list xleft y0 0.0) (list xleft (- y0 (* n alto)) 0.0))
    (setq xleft (+ xleft anchoCelda)))
  (SET-N:Linea (list xleft y0 0.0) (list xleft (- y0 (* n alto)) 0.0))
  (setq i 0)
  (foreach fila (SET-N:NOTAS)
    (SET-N:MTexto (list x0 (- (- y0 (* n alto)) (* alto 0.45) (* i alto 0.85)) 0.0)
                  total fila (* txt-alto 0.85) 1)
    (setq i (1+ i)))
  (setq ymin (- y0 (* n alto)))
  (setq SET-N:PUNTO pto)
  (setq SET-N:CAJA (list (- x0 (* alto 0.5)) (- ymin (* alto 1.8))
                          (+ x0 total (* alto 0.5)) (+ y0 (* alto 1.0))))
  (SET-N:Log (strcat "Tabla dibujada de " (rtos x0 2 3) ", " (rtos y0 2 3)
                      " a " (rtos (+ x0 total) 2 3) ", " (rtos ymin 2 3))))

;;; ---------------------------------------------------------------------------
;;; Comando 1: dibujar o actualizar
;;; ---------------------------------------------------------------------------

(defun c:CUADRO-NIVELES (/ *error* pto filas ncols nrows)
  (defun *error* (msg)
    (SET-N:Log "ERROR en CUADRO-NIVELES.")
    (SET-N:LogDump)
    (princ "\nError en CUADRO-NIVELES (se corta).")
    (princ))
  (setq SET-N:LOG-TEXTO '())
  (SET-N:Log "=== CUADRO-NIVELES ===")
  (setq filas (SET-N:LeeCSV))
  (if (null filas)
    (progn
      (SET-N:Log (strcat "No se pudo leer el CSV: " (SET-N:CSV)))
      (SET-N:LogDump)
      (princ (strcat "\nNo se pudo leer el CSV: " (SET-N:CSV))))
    (progn
      (setq nrows (length filas))
      (setq ncols (length (car filas)))
      (SET-N:Log (strcat "CSV: " (itoa nrows) " filas x " (itoa ncols) " columnas"))
      (SET-N:Log (strcat "Espacio: " (if (= 0 (getvar "CVPORT")) "paper" "modelo")
                          " | alto de fila: " (rtos (SET-N:ALTO-FILA) 2 3)))
      (if SET-N:PUNTO
        (progn
          (SET-N:CAPA (SET-N:ExisteCapa (SET-N:LAYER)))
          (SET-N:BorraTabla)
          (SET-N:DibujaTabla filas SET-N:PUNTO)
          (SET-N:LogDump)
          (princ (strcat "\nPlanilla de niveles ACTUALIZADA desde el CSV (" (itoa nrows) " filas)."))
          (princ "\n"))
        (progn
          (setq SET-N:CAPA (SET-N:ExisteCapa (SET-N:LAYER)))
          (setq pto (getpoint "\nPunto de insercion de la planilla de niveles: "))
          (if (null pto)
            (progn
              (SET-N:Log "Cancelado en el punto de insercion.")
              (SET-N:LogDump)
              (princ "\nCancelado."))
            (progn
              (SET-N:DibujaTabla filas pto)
              (command "_.zoom" "_w"
                       (list (- (car pto) (* (SET-N:ALTO-FILA) 0.5))
                             (- (- (cadr pto) (* (length filas) (SET-N:ALTO-FILA))) (* (SET-N:ALTO-FILA) 1.8)) 0.0)
                       (list (+ (car pto) (* (SET-N:ANCHO-COL 1) (SET-N:ALTO-FILA)) (* (SET-N:ALTO-FILA) 0.5))
                             (+ (cadr pto) (* (SET-N:ALTO-FILA) 1.0)) 0.0))
              (SET-N:LogDump)
              (princ (strcat "\nPlanilla de niveles dibujada (" (itoa nrows) " filas) en la capa "
                             SET-N:CAPA " (hice zoom a la tabla)."))
              (princ "\n")))))))
  (princ))

;;; ---------------------------------------------------------------------------
;;; Comando 2: actualizar la tabla desde el CSV
;;; ---------------------------------------------------------------------------

(defun c:CUADRO-NIVELES-ACT (/ filas pto)
  (if (null SET-N:PUNTO)
    (progn
      (princ "\nTodavia no hay ninguna planilla dibujada en esta sesion: corré CUADRO-NIVELES.")
      (princ))
    (progn
      (setq filas (SET-N:LeeCSV))
      (if (null filas)
        (princ (strcat "\nNo se pudo leer el CSV: " (SET-N:CSV)))
        (progn
          (setq SET-N:CAPA (SET-N:ExisteCapa (SET-N:LAYER)))
          (SET-N:BorraTabla)
          (SET-N:DibujaTabla filas SET-N:PUNTO)
          (command "_.regen")
          (princ (strcat "\nPlanilla actualizada desde el CSV (" (length filas) " filas)."))
          (princ "\n")))))
  (princ))

;;; ---------------------------------------------------------------------------
;;; Comando 3: dibujar de nuevo en otro punto
;;; ---------------------------------------------------------------------------

(defun c:CUADRO-NIVELES-NUEVO (/ filas pto)
  (setq filas (SET-N:LeeCSV))
  (if (null filas)
    (princ (strcat "\nNo se pudo leer el CSV: " (SET-N:CSV)))
    (progn
      (setq SET-N:CAPA (SET-N:ExisteCapa (SET-N:LAYER)))
      (SET-N:BorraTabla)
      (setq pto (getpoint "\nPunto de insercion de la planilla de niveles: "))
      (if pto
        (progn
          (SET-N:DibujaTabla filas pto)
          (command "_.regen")
          (princ "\nPlanilla dibujada en el nuevo punto.")
          (princ "\n")))))
  (princ))

;;; ---------------------------------------------------------------------------
;;; Comando 4: ver el CSV
;;; ---------------------------------------------------------------------------

(defun c:CUADRO-NIVELES-VAL (/ filas fila)
  (princ "\n=== Contenido del CSV de la planilla de niveles ===")
  (setq filas (SET-N:LeeCSV))
  (if (null filas)
    (princ "\nNo se pudo leer el CSV.")
    (progn
      (foreach fila filas
        (princ (strcat "\n  " (car fila) "  |  " (cadr fila) "  |  " (caddr fila))))
      (princ "\n")))
  (foreach fila (SET-N:NOTAS) (princ (strcat "\n  " fila)))
  (princ "\n")
  (princ))

(princ "\nSET-01-CUADRO-NIVELES.lsp cargado.\n")
(princ "  Comandos: CUADRO-NIVELES (dibuja/actualiza) | CUADRO-NIVELES-ACT (actualiza)\n")
(princ "            CUADRO-NIVELES-NUEVO (dibuja en otro punto) | CUADRO-NIVELES-VAL (ver el CSV)\n")
(princ)
