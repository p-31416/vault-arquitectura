;;; ============================================================================
;;; SET-01-SIMB-LOC-ID.lsp  --  Bloque de identificacion de locales (v2)
;;; Proyecto: SET_01-REP (REP-ARAOZ) / MVP_02-autocad-standards
;;;
;;; QUE HACE:
;;;   1. Crea el bloque "SIMB-LOC_ID" con:
;;;        - un RECTANGULO de 0.30 x 0.30 m, centrado en el origen del bloque
;;;          (cuadrado: asi entran numeros de dos cifras)
;;;        - un atributo VISIBLE   "N_LOC"   : numero de local (01, 02, ...)
;;;        - un atributo INVISIBLE "TXT_LOC" : nombre del local (no se ve en el
;;;                                      plano, pero sale en la planilla)
;;;   2. Comando SIMB-LOC_ID: rota los locales uno por uno. Pide punto, numero
;;;      y nombre; cuando confirmas el nombre, el comando se reactiva solo
;;;      para el local siguiente con el numero siguiente.
;;;   3. Comando LOC-ID-CHECK: controla el bloque, la numeracion y el ORDEN DE
;;;      LECTURA (X creciente, Y decreciente: izquierda->derecha, arriba->abajo).
;;;
;;; COMO SE USA (AutoCAD LT 2027 / AutoCAD 2027):
;;;   1. APPLOAD -> este archivo -> Load
;;;   2. SIMB-LOC_ID -> click en cada local, de arriba hacia abajo y de
;;;      izquierda a derecha, escribiendo el nombre. Enter en el punto = salir.
;;;   3. LOC-ID-CHECK para verificar (tambien se dispara solo al salir)
;;;
;;; NOTA ES: AutoCAD LT 2024 o superior soporta AutoLISP (comando APPLOAD).
;;; NOTA ES: LT 2023 y anteriores NO lo soportan. LT for Mac, tampoco.
;;; NOTA ES: En LT no hay COM ni ActiveX: todo el control va en AutoLISP.
;;; ============================================================================

;;; ---------------------------------------------------------------------------
;;; Constantes (cambiar aca para ajustar el simbolo)
;;; ---------------------------------------------------------------------------

(defun SET-L:LAYER () "A-SIMBOLO-NPT-PLANTA")   ; capa donde se insertan los locales
(defun SET-L:LAYER-DEF () "0")            ; capa de la DEFINICION del bloque
                                                          ; (en 0 el bloque toma la capa de insercion)
(defun SET-L:BLOQUE () "SIMB-LOC_ID")            ; nombre del bloque
(defun SET-L:RECT-ANCHO () 0.30)                ; ancho del rectangulo (m)
(defun SET-L:RECT-ALTO () 0.30)                 ; alto del rectangulo (m)
(defun SET-L:ALTO-NUM () 0.12)                  ; alto del texto del numero (m)
(defun SET-L:TOL-FILA () 0.30)                  ; tolerancia de fila (m) p/ el control
(defun SET-L:EPS () 0.001)                       ; tolerancia de comparacion (m)

;;; ---------------------------------------------------------------------------
;;; Registro de la sesion (se escribe en raw/reports/loc-id-log.txt)
;;; ---------------------------------------------------------------------------

(setq SET-L:LOG-TEXTO '())

(defun SET-L:Log (txt)
  "Anota una linea en el registro de la sesion."
  (setq SET-L:LOG-TEXTO (cons txt SET-L:LOG-TEXTO)))

(defun SET-L:LogDump (/ f x)
  "Escribe el registro de la sesion en un archivo de texto."
  (setq f (open "P:/00-repos/proyecto-pi/vault-arquitectura/raw/reports/loc-id-log.txt" "w"))
  (if f
    (progn
      (foreach x (reverse SET-L:LOG-TEXTO) (write-line x f))
      (close f))
    (princ "\nNo se pudo escribir el registro de la sesion.")))

(defun SET-L:WorkX () 1000.0)
(defun SET-L:WorkY () 1000.0)

;;; ---------------------------------------------------------------------------
;;; Utilidades
;;; ---------------------------------------------------------------------------

(defun SET-L:Num2 (n)
  "Numero de local con 2 digitos: 1 -> 01, 28 -> 28, 100 -> 100."
  (if (< n 10) (strcat "0" (itoa n)) (itoa n)))

(defun SET-L:Max (lst / m v)
  "Mayor valor de una lista de numeros."
  (foreach v lst (if (or (null m) (> v m)) (setq m v)))
  m)

(defun SET-L:Min (lst / m v)
  "Menor valor de una lista de numeros."
  (foreach v lst (if (or (null m) (< v m)) (setq m v)))
  m)

(defun SET-L:ExisteCapa (nombre / r)
  "Crea la capa si no existe y devuelve el nombre. NO usa el comando -layer
   (dejaba la linea de comandos colgada): se crea con entmake."
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
  nombre)

(defun SET-L:BloqueExiste (nombre / rec)
  "Registro del bloque en la tabla BLOCK, o nil si no existe.
   (tblobjname es mas seguro que tblsearch: devuelve el registro real.)"
  (setq rec (tblobjname "BLOCK" nombre))
  rec)

(defun SET-L:ListaBloques (/ b s)
  "Nombres de todos los bloques definidos en el dibujo (para diagnosticar)."
  (setq b (tblnext "BLOCK" T))
  (while b
    (setq s (strcat s (cdr (assoc 2 b)) "  "))
    (setq b (tblnext "BLOCK")))
  s)

(defun SET-L:NombresInsert (/ ss i e d s)
  "Nombres de bloque de todos los INSERT del dibujo (para diagnosticar)."
  (setq ss (ssget "_X" '((0 . "INSERT"))))
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq e (ssname ss i))
        (if e
          (progn
            (setq d (entget e))
            (setq s (strcat s (cdr (assoc 2 d)) "  "))))
        (setq i (1+ i)))))
  s)

(defun SET-L:BorraEjemplares (nombre / ss i e d)
  "Borra todos los INSERT de un bloque (deja la definicion)."
  (setq ss (ssget "_X" '((0 . "INSERT"))))
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq e (ssname ss i))
        (if e
          (progn
            (setq d (entget e))
            (if (and d (= (cdr (assoc 2 d)) nombre))
              (entdel e))))
        (setq i (1+ i))))))

(defun SET-L:BorraBloque (nombre / rec)
  "Borra la definicion del bloque (solo si quedo sin ejemplares)."
  (setq rec (tblobjname "BLOCK" nombre))
  (if rec (entdel rec))
  rec)

(defun SET-L:Atributos (ename / res a)
  "Lista (tag . valor) de los atributos de un INSERT."
  (setq res '())
  (foreach a (entget ename)
    (if (and (listp a) (= (cdr (assoc 0 a)) "ATTRIB"))
      (setq res (cons (list (cdr (assoc 2 a)) (cdr (assoc 1 a))) res))))
  res)

(defun SET-L:ValorAttr (ename tag / res)
  "Valor de un atributo de un INSERT (nil si no existe o esta vacio)."
  (setq res (SET-L:Atributos ename))
  (cdr (assoc tag res)))

(defun SET-L:PuntoWCS (pt dx dy ang / x y c s)
  "Punto en el mundo: origen del bloque + offset local, rotado por ang (rad)."
  (setq x (car pt))
  (setq y (cadr pt))
  (setq c (cos ang))
  (setq s (sin ang))
  (list (+ x (- (* dx c) (* dy s)))
        (+ y (+ (* dx s) (* dy c)))
        0.0))

(defun SET-L:MismoY (a b)
  "Dos Y son el mismo si difieren menos de 1 mm."
  (< (abs (- a b)) 0.001))

(defun SET-L:InsertaX (res e)
  "Inserta e en res mantendo el orden creciente de X (insercion ordenada)."
  (if (null res)
    (list e)
    (if (< (car e) (car (car res)))
      (cons e res)
      (append (list (car res)) (SET-L:InsertaX (cdr res) e)))))

(defun SET-L:OrdenaX (lst / res e)
  "Ordena una lista de (x y num nombre) de izquierda a derecha (X growing)."
  (foreach e lst (setq res (SET-L:InsertaX res e)))
  res)

(defun SET-L:InsertaDesc (res v)
  "Inserta v en res manteniendo el orden decreciente."
  (if (null res)
    (list v)
    (if (> v (car res))
      (cons v res)
      (append (list (car res)) (SET-L:InsertaDesc (cdr res) v)))))

(defun SET-L:OrdenaDesc (lst / res v)
  "Ordena una lista de numeros de mayor a menor."
  (foreach v lst (setq res (SET-L:InsertaDesc res v)))
  res)

(defun SET-L:YSUnicos (locales / ys l)
  "Lista de Y distintos, de arriba hacia abajo."
  (foreach l locales
    (if (not (SET-L:HayY (cadr l) ys)) (setq ys (cons (cadr l) ys))))
  (SET-L:OrdenaDesc ys))

(defun SET-L:HayY (y ys / v)
  (foreach v ys (if (SET-L:MismoY y v) (return T)))
  nil)

(defun SET-L:HayLocal (l assigned / a)
  "True si el local (x y) ya esta en la lista de asignados."
  (foreach a assigned
    (if (and (equal (car l) (car a)) (equal (cadr l) (cadr a)))
      (return T)))
  nil)

(defun SET-L:Filas (locales tol / ys y members assigned rows l)
  "Agrupa los locales en filas (mismo Y dentro de tol) y ordena cada fila de
   izquierda a derecha. Mismo criterio que scripts/ordena-locales.py."
  (setq ys (SET-L:YSUnicos locales))
  (setq assigned '())
  (setq rows '())
  (foreach y ys
    (setq members '())
    (foreach l locales
      (if (<= (abs (- (cadr l) y)) tol)
        (setq members (cons l members))))
    (if (and members (not (SET-L:HayLocal members assigned)))
      (progn
        (setq members (SET-L:OrdenaX members))
        (setq rows (cons members rows))
        (setq assigned (append assigned members)))))
  (reverse rows))

(defun SET-L:NoAsignados (locales rows / res l todos)
  "Locales que no quedaron en ninguna fila (revisar distancias)."
  (setq res '())
  (setq todos (if rows (apply 'append rows) '()))
  (foreach l locales
    (if (not (SET-L:HayLocal l todos))
      (setq res (cons l res))))
  res)

(defun SET-L:LocalesDelDibujo (/ ss i e d res num nom)
  "Lista de (x y numero nombre) de los ejemplares de SIMB-LOC_ID."
  (setq res '())
  (setq ss (ssget "_X" '((0 . "INSERT"))))
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq e (ssname ss i))
        (if e
          (progn
            (setq d (entget e))
            (if (= (cdr (assoc 2 d)) (SET-L:BLOQUE))
              (progn
                (setq num (SET-L:ValorAttr e "N_LOC"))
                (setq nom (SET-L:ValorAttr e "TXT_LOC"))
                (setq res (cons (list (car (assoc 10 d))
                                       (cadr (assoc 10 d))
                                       (if num num "")
                                       (if nom nom ""))
                                res))))))
        (setq i (1+ i)))))
  res)

(defun SET-L:NumDe (l)
  "Numero del local normalizado a 2 digitos."
  (SET-L:Num2 (atoi (caddr l))))

(defun SET-L:NombreDe (l)
  "Nombre del local (o SIN-NOMBRE si esta vacio)."
  (if (= "" (cadddr l)) "SIN-NOMBRE" (cadddr l)))

(defun SET-L:UltimoNum (locales / m)
  "Mayor numero de local ya presente en el dibujo (0 si no hay ninguno)."
  (setq m 0)
  (foreach l locales
    (if (> (atoi (caddr l)) m) (setq m (atoi (caddr l)))))
  m)

;;; ---------------------------------------------------------------------------
;;; Definicion del bloque
;;; ---------------------------------------------------------------------------

(defun SET-L:RectBloque (/ ents e d xs ys p)
  "Devuelve (ancho alto) del rectangulo del bloque, o nil si no hay."
  (setq ents (block-ent (tblobjname "BLOCK" (SET-L:BLOQUE))))
  (if (null ents) (setq ents '()))
  (foreach e ents
    (setq d (entget e))
    (if (= (cdr (assoc 0 d)) "LWPOLYLINE")
      (foreach p d
        (if (and (listp p) (= (car p) 10))
          (progn
            (setq xs (cons (car (cdr p)) xs))
            (setq ys (cons (cadr (cdr p)) ys)))))))
  (if (and xs ys)
    (list (- (SET-L:Max xs) (SET-L:Min xs))
          (- (SET-L:Max ys) (SET-L:Min ys)))
    nil))

(defun SET-L:TagsBloque (/ ents e d res s r)
  "Descripcion de los atributos definidos en el bloque: tag + visible/invisible."
  (setq ents (block-ent (tblobjname "BLOCK" (SET-L:BLOQUE))))
  (setq res '())
  (foreach e ents
    (setq d (entget e))
    (if (= (cdr (assoc 0 d)) "ATTDEF")
      (setq res (cons (list (cdr (assoc 2 d)) (cdr (assoc 70 d))) res))))
  (setq s "")
  (foreach r res
    (setq s (strcat s (if (= "" s) "" ", ") (car r)
                    (if (= 1 (cadr r)) " (invisible)" " (visible)"))))
  s)

(defun SET-L:EntmakeOK (lista / r)
  "entmake que avisa que entidad fallo (en vez de seguir en silencio)."
  (setq r (entmake lista))
  (if (null r)
    (princ (strcat "\nERROR: AutoCAD no acepto la entidad "
                   (cdr (assoc 0 lista)) " (entmake devolvio nil)."))
    r))

(defun SET-L:CreaBloque (/ capa ancho alto ok r1 r2 r3 r4 r5)
  "Crea la definicion del bloque SIMB-LOC_ID.
   1) intenta con entmake (BLOCK + geometria + 2 ATTDEF + ENDBLK)
   2) si AutoCAD no acepta el BLOCK, lo arma con el comando -BLOCK
   La DEFINICION va en la capa 0: asi el bloque insertado toma la capa de
   insercion (A-SIMBOLO-NPT-PLANTA), que es la convencion de AutoCAD."
  (setq capa (SET-L:LAYER-DEF))
  (setq ancho (SET-L:RECT-ANCHO))
  (setq alto (SET-L:RECT-ALTO))
  (setq ok T)

  ;; 1. Apertura del bloque (base en el origen 0,0)
  (setq r1 (entmakex
    (list '(0. "BLOCK")
          '(100. "AcDbEntity")
          (cons 8 capa)
          '(100. "AcDbBlockBegin")
          (cons 2 (SET-L:BLOQUE))
          (cons 70 0)
          (cons 10 (list 0.0 0.0 0.0))
          (cons 3 (SET-L:BLOQUE))
          (cons 1 ")")
    )))
  (if (null r1)
    (progn
      (SET-L:Log "BLOCK por entmake: RECHAZADO (entmake devolvio nil)")
      (setq ok nil))
    (progn
      (SET-L:Log "BLOCK por entmake: OK")
      ;; 2. Rectangulo (cuadrado) centrado en el origen
      (setq r2 (entmakex
        (list '(0. "LWPOLYLINE")
              '(100. "AcDbEntity")
              (cons 8 capa)
              '(100. "AcDbPolyline")
              (cons 90 4)
              (cons 70 1)
              (cons 43 0.0)
              (cons 10 (list (/ ancho 2.0) (/ alto -2.0)))
              (cons 10 (list (/ ancho 2.0) (/ alto 2.0)))
              (cons 10 (list (/ ancho -2.0) (/ alto 2.0)))
              (cons 10 (list (/ ancho -2.0) (/ alto -2.0)))
        )))
      (if (null r2) (progn (SET-L:Log "LWPOLYLINE por entmake: RECHAZADO") (setq ok nil)))
      ;; 3. Atributo VISIBLE: numero de local (N_LOC)
      (setq r3 (entmakex
        (list '(0. "ATTDEF")
              '(100. "AcDbEntity")
              (cons 8 capa)
              '(100. "AcDbText")
              (cons 10 (list 0.0 0.0 0.0))
              (cons 40 (SET-L:ALTO-NUM))
              (cons 1 "01")
              (cons 50 0.0)
              (cons 41 1.0)
              (cons 51 0.0)
              (cons 7 "Standard")
              (cons 71 0)
              (cons 72 1)
              (cons 11 (list 0.0 0.0 0.0))
              (cons 73 2)
              '(100. "AcDbAttributeDefinition")
              (cons 3 "Numero de local")
              (cons 2 "N_LOC")
              (cons 70 0)
              '(100. "AcDbAttribute")
        )))
      (if (null r3) (progn (SET-L:Log "ATTDEF N_LOC por entmake: RECHAZADO") (setq ok nil)))
      ;; 4. Atributo INVISIBLE: nombre del local (TXT_LOC). flag 70 = 1
      (setq r4 (entmakex
        (list '(0. "ATTDEF")
              '(100. "AcDbEntity")
              (cons 8 capa)
              '(100. "AcDbText")
              (cons 10 (list 0.0 0.25 0.0))
              (cons 40 (SET-L:ALTO-NUM))
              (cons 1 "")
              (cons 50 0.0)
              (cons 41 1.0)
              (cons 51 0.0)
              (cons 7 "Standard")
              (cons 71 0)
              (cons 72 0)
              (cons 11 (list 0.0 0.25 0.0))
              (cons 73 0)
              '(100. "AcDbAttributeDefinition")
              (cons 3 "Nombre del local")
              (cons 2 "TXT_LOC")
              (cons 70 1)
              '(100. "AcDbAttribute")
        )))
      (if (null r4) (progn (SET-L:Log "ATTDEF TXT_LOC por entmake: RECHAZADO") (setq ok nil)))
      ;; 5. Cierre del bloque
      (setq r5 (entmakex
        (list '(0. "ENDBLK")
              '(100. "AcDbEntity")
              (cons 8 capa)
              '(100. "AcDbBlockEnd")
        )))
      (if (null r5) (progn (SET-L:Log "ENDBLK por entmake: RECHAZADO") (setq ok nil)))))

  (if (not ok)
    (progn
      (SET-L:Log "Se descarta la definicion a medias y se intenta con el comando -BLOCK.")
      (if (SET-L:BloqueExiste (SET-L:BLOQUE))
        (progn
          (entmakex (list '(0. "ENDBLK") '(100. "AcDbEntity") (cons 8 capa) '(100. "AcDbBlockEnd")))
          (SET-L:BorraEjemplares (SET-L:BLOQUE))
          (SET-L:BorraBloque (SET-L:BLOQUE))))
    (progn
      (command "_.regen")
      (if (null (SET-L:BloqueExiste (SET-L:BLOQUE)))
        (progn
          (SET-L:Log "El bloque no quedo registrado en la tabla: se intenta con -BLOCK.")
          (setq ok (SET-L:BloquePorComando)))
        (progn
          (SET-L:Log (strcat "Bloque " (SET-L:BLOQUE) " creado: rectangulo "
                             (rtos ancho 2 2) " x " (rtos alto 2 2) " m, definicion en la capa " capa))
          (princ (strcat "\nBloque " (SET-L:BLOQUE) " creado: rectangulo "
                         (rtos ancho 2 2) " x " (rtos alto 2 2) " m (definicion en capa 0).")))))))
  ok)

(defun SET-L:DibujaGeometriaTrabajo (/ ancho alto r1 r2 r3 wx wy)
  "Dibuja en la capa 0 el rectangulo y los dos ATTDEF en un area de trabajo
   lejana del plano (1000,1000). Sirve para armar el bloque con -BLOCK."
  (setq ancho (SET-L:RECT-ANCHO))
  (setq alto (SET-L:RECT-ALTO))
  (setq wx (SET-L:WorkX))
  (setq wy (SET-L:WorkY))
  (setq r1 (entmakex
    (list '(0. "LWPOLYLINE")
          '(100. "AcDbEntity")
          (cons 8 "0")
          '(100. "AcDbPolyline")
          (cons 90 4)
          (cons 70 1)
          (cons 43 0.0)
          (cons 10 (list (- wx (/ ancho 2.0)) (- wy (/ alto 2.0))))
          (cons 10 (list (+ wx (/ ancho 2.0)) (- wy (/ alto 2.0))))
          (cons 10 (list (+ wx (/ ancho 2.0)) (+ wy (/ alto 2.0))))
          (cons 10 (list (- wx (/ ancho 2.0)) (+ wy (/ alto 2.0))))
    )))
  (setq r2 (entmakex
          (list '(0. "ATTDEF")
                '(100. "AcDbEntity")
                (cons 8 "0")
                '(100. "AcDbText")
                (cons 10 (list wx wy 0.0))
                (cons 40 (SET-L:ALTO-NUM))
                (cons 1 "01")
                (cons 50 0.0)
                (cons 41 1.0)
                (cons 51 0.0)
                (cons 7 "Standard")
                (cons 71 0)
                (cons 72 1)
                (cons 11 (list wx wy 0.0))
                (cons 73 2)
                '(100. "AcDbAttributeDefinition")
                (cons 3 "Numero de local")
                (cons 2 "N_LOC")
                (cons 70 0)
                '(100. "AcDbAttribute")
          )))
  (setq r3 (entmakex
          (list '(0. "ATTDEF")
                '(100. "AcDbEntity")
                (cons 8 "0")
                '(100. "AcDbText")
                (cons 10 (list wx (+ wy 0.25) 0.0))
                (cons 40 (SET-L:ALTO-NUM))
                (cons 1 "")
                (cons 50 0.0)
                (cons 41 1.0)
                (cons 51 0.0)
                (cons 7 "Standard")
                (cons 71 0)
                (cons 72 0)
                (cons 11 (list wx (+ wy 0.25) 0.0))
                (cons 73 0)
                '(100. "AcDbAttributeDefinition")
                (cons 3 "Nombre del local")
                (cons 2 "TXT_LOC")
                (cons 70 1)
                '(100. "AcDbAttribute")
          )))
  (list r1 r2 r3))

(defun SET-L:BloquePorComando (/ g w1 w2 args existe)
  "Arma el bloque con el comando -BLOCK (funciona en LT donde entmake de BLOCK
   puede fallar). La geometria se dibuja en el area de trabajo y se mete en el
   bloque por ventana. Si el bloque ya existe, responde que si a redefinirlo."
  (SET-L:Log "Bloque por comando -BLOCK: se dibuja la geometria de trabajo.")
  (setq g (SET-L:DibujaGeometriaTrabajo))
  (if (member nil g)
    (progn
      (SET-L:Log "No se pudo dibujar la geometria de trabajo: se aborta.")
      (SET-L:BorraGeometriaTrabajo)
      nil)
    (progn
      (setq w1 (list (- (SET-L:WorkX) 0.5) (- (SET-L:WorkY) 0.5) 0.0))
      (setq w2 (list (+ (SET-L:WorkX) 0.5) (+ (SET-L:WorkY) 0.5) 0.0))
      (setq existe (SET-L:BloqueExiste (SET-L:BLOQUE)))
      (setq args (list "_.-block" (SET-L:BLOQUE)))
      (if existe (setq args (append args (list "_Y"))))
      (setq args (append args (list (list (SET-L:WorkX) (SET-L:WorkY) 0.0)
                                     (list (SET-L:WorkX) (SET-L:WorkY) 0.0)
                                     "_w" w1 w2 "" "_N")))
      (command args)
      (command "_.regen")
      (if (null (SET-L:BloqueExiste (SET-L:BLOQUE)))
        (progn
          (SET-L:Log "El comando -BLOCK no dejo el bloque registrado.")
          (SET-L:BorraGeometriaTrabajo)
          nil)
        (progn
          (SET-L:Log "Bloque creado con el comando -BLOCK.")
          (SET-L:BorraGeometriaTrabajo)
          T)))))

(defun SET-L:BorraGeometriaTrabajo (/ ss i e d)
  "Borra la geometria de trabajo que quedo suelta (por si -BLOCK no la consumio)."
  (setq ss (ssget "_X" '((0 . "LWPOLYLINE,ATTDEF"))))
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq e (ssname ss i))
        (if e
          (progn
            (setq d (entget e))
            (if (and (equal (car (assoc 10 d)) (SET-L:WorkX))
                     (equal (cadr (assoc 10 d)) (SET-L:WorkY)))
              (entdel e))))
        (setq i (1+ i))))))

(defun SET-L:Filtra10 (d / res p)
  "Saca del entget los vertices (10) de una polilinea, deja el resto."
  (setq res '())
  (foreach p d
    (if (not (and (listp p) (= (car p) 10)))
      (setq res (cons p res))))
  (reverse res))

(defun SET-L:ActualizaRect (/ ents e d ancho alto)
  "Pasa el rectangulo del bloque al tamano actual (0.30 x 0.30) editandolo.
   Se edita en vez de recrear: asi no se pierden los ejemplares ya rotulados."
  (setq ancho (SET-L:RECT-ANCHO))
  (setq alto (SET-L:RECT-ALTO))
  (setq ents (block-ent (tblobjname "BLOCK" (SET-L:BLOQUE))))
  (foreach e ents
    (setq d (entget e))
    (if (= (cdr (assoc 0 d)) "LWPOLYLINE")
      (entmod
        (append
          (SET-L:Filtra10 d)
          (list (list 10 (list (/ ancho 2.0) (/ alto -2.0)))
                (list 10 (list (/ ancho 2.0) (/ alto 2.0)))
                (list 10 (list (/ ancho -2.0) (/ alto 2.0)))
                (list 10 (list (/ ancho -2.0) (/ alto -2.0))))))))
  (command "_.regen"))

(defun SET-L:AseguraBloque (/ r ok)
  "Se asegura de que el bloque exista con el rectangulo correcto.
   NO borra nunca la definicion: si esta danada la rehace con -BLOCK.
   Devuelve T si esta todo bien, nil si no se puede seguir."
  (setq ok T)
  (if (null (SET-L:BloqueExiste (SET-L:BLOQUE)))
    (if (not (SET-L:CreaBloque))
      (setq ok nil))
    (progn
      (setq r (SET-L:RectBloque))
      (cond
        ((null r)
          (SET-L:Log "El bloque existe pero NO tiene el rectangulo: se rehace con -BLOCK.")
          (if (not (SET-L:BloquePorComando))
            (progn
              (princ (strcat "\nNo se pudo rehacer el bloque " (SET-L:BLOQUE) "."))
              (princ "\nBorralo a mano (BLOQUE -> Borrar, o P purge) y volve a correr.")
              (setq ok nil))))
        ((or (> (abs (- (car r) (SET-L:RECT-ANCHO))) (SET-L:EPS))
              (> (abs (- (cadr r) (SET-L:RECT-ALTO))) (SET-L:EPS)))
          (princ (strcat "\nEl rectangulo del bloque es " (rtos (car r) 2 3) " x "
                          (rtos (cadr r) 2 3) " m -> se actualiza a "
                          (rtos (SET-L:RECT-ANCHO) 2 2) " x "
                          (rtos (SET-L:RECT-ALTO) 2 2) " m (los ejemplares ya "
                          "rotulados conservan su numero y su nombre)."))
          (SET-L:ActualizaRect)))))
  (if ok (command "_.regen"))
  ok)

;;; ---------------------------------------------------------------------------
;;; Insercion de un local
;;; ---------------------------------------------------------------------------

(defun SET-L:InsertaLocal (pt num nombre ang / capa e p1 p2 a1 a2)
  "Inserta un local: INSERT + atributo N_LOC (visible) + TXT_LOC (invisible).
   Patron oficial: se crea el INSERT y se le asocian los atributos con
   entappend (la referencia de bloque es el padre del atributo)."
  (setq capa (SET-L:LAYER))
  (if (null (SET-L:BloqueExiste (SET-L:BLOQUE)))
    (progn
      (SET-L:Log "ERROR: el bloque no existe: no se inserta nada.")
      nil)
    (progn
      (setq p1 (SET-L:PuntoWCS pt 0.0 0.0 ang))
      (setq p2 (SET-L:PuntoWCS pt 0.0 0.25 ang))
      (setq e (entmakex (list '(0. "INSERT")
                              '(100. "AcDbEntity")
                              (cons 8 capa)
                              '(100. "AcDbBlockReference")
                              (cons 2 (SET-L:BLOQUE))
                              (cons 10 pt)
                              (cons 41 1.0) (cons 42 1.0) (cons 43 1.0)
                              (cons 50 ang)
                              (cons 66 1))))
      (if (null e)
        (progn
          (SET-L:Log "ERROR: entmake del INSERT devolvio nil (no se inserta).")
          nil)
        (progn
          (setq a1 (entmakex (list '(0. "ATTRIB")
                                   '(100. "AcDbEntity")
                                   (cons 8 capa)
                                   '(100. "AcDbText")
                                   (cons 10 p1)
                                   (cons 40 (SET-L:ALTO-NUM))
                                   (cons 1 num)
                                   (cons 50 ang)
                                   (cons 41 1.0) (cons 51 0.0)
                                   (cons 7 "Standard")
                                   (cons 71 0)
                                   (cons 72 1)
                                   (cons 11 p1)
                                   (cons 73 2)
                                   '(100. "AcDbAttribute")
                                   (cons 2 "N_LOC")
                                   (cons 70 0))))
          (if a1
            (entappend e a1)
            (SET-L:Log "ERROR: no se pudo crear el atributo N_LOC."))
          (setq a2 (entmakex (list '(0. "ATTRIB")
                                   '(100. "AcDbEntity")
                                   (cons 8 capa)
                                   '(100. "AcDbText")
                                   (cons 10 p2)
                                   (cons 40 (SET-L:ALTO-NUM))
                                   (cons 1 nombre)
                                   (cons 50 ang)
                                   (cons 41 1.0) (cons 51 0.0)
                                   (cons 7 "Standard")
                                   (cons 71 0)
                                   (cons 72 0)
                                   (cons 11 p2)
                                   (cons 73 0)
                                   '(100. "AcDbAttribute")
                                   (cons 2 "TXT_LOC")
                                   (cons 70 1))))
          (if a2
            (entappend e a2)
            (SET-L:Log "ERROR: no se pudo crear el atributo TXT_LOC."))
          (SET-L:Log (strcat "local " num " " nombre " en (" (rtos (car pt) 2 2) ", " (rtos (cadr pt) 2 2) ")"))
          (princ (strcat "\n  OK " num "  " nombre))
          e)))))

;;; ---------------------------------------------------------------------------
;;; Comando: rotular locales
;;; ---------------------------------------------------------------------------

(defun c:SIMB-LOC_ID
  (/ *error* pt num nombre ultimo contador locales inicio ok)
  (defun *error* (msg)
    (princ "\nError en el comando (se cancela).")
    (princ "\nCancelado.")
    (princ))
  (setq SET-L:LOG-TEXTO '())
  (SET-L:Log "=== SIMB-LOC_ID ===")
  (if (not (SET-L:AseguraBloque))
    (progn
      (SET-L:Log "No se puede rotular: el bloque no esta disponible.")
      (SET-L:LogDump)
      (princ "\nNo se puede rotular: el bloque no esta disponible. Corre LOC-ID-DIAG.")
      (princ))
    (progn
      (if (/= 6 (getvar "INSUNITS"))
        (princ (strcat "\nOjo: INSUNITS = " (itoa (getvar "INSUNITS")) " (6 = metros).")))
      (setq locales (SET-L:LocalesDelDibujo))
      (setq inicio (SET-L:UltimoNum locales))
      (setq contador inicio)
      (setq ultimo "")
      (princ "\n=== Rotulacion de locales (SIMB-LOC_ID) ===")
      (princ (strcat "\nLocales ya rotulados en el dibujo: " (itoa (length locales))
                     "  (siguiente numero: " (SET-L:Num2 (1+ contador)) ")"))
      (princ "\nClick en cada local de ARRIBA hacia ABAJO y de IZQUIERDA a DERECHA.")
      (princ "\nEnter en el punto = salir.  ESC = cancelar.")
      (setq ok T)
      (while (and ok (setq pt (getpoint "\nPunto de insercion del local <Enter = salir>: ")))
        (setq num (getstring (strcat "\nNumero de local <" (SET-L:Num2 (1+ contador)) ">: ")))
        (if (or (null num) (= num ""))
          (setq num (SET-L:Num2 (1+ contador)))
          (if (> (atoi num) 0)
            (setq num (SET-L:Num2 (atoi num)))
            (progn
              (princ (strcat "\nNumero no valido (" num "): se usa " (SET-L:Num2 (1+ contador))))
              (setq num (SET-L:Num2 (1+ contador))))))
        (setq nombre (getstring (strcat "\nNombre del local (TXT_LOC) <" ultimo ">: ")))
        (if (or (null nombre) (= nombre ""))
          (setq nombre ultimo))
        (if (= "" nombre) (setq nombre "SIN-NOMBRE"))
        (if (null (SET-L:InsertaLocal pt num nombre 0.0))
          (progn (princ "\nSe corta la rotulacion.") (setq ok nil)))
        (setq ultimo nombre)
        (setq contador (1+ contador)))
      (princ (strcat "\nLocales rotulados en esta sesion: " (itoa (- contador inicio)) "\n"))
      (SET-L:LogDump)))
  (c:LOC-ID-CHECK))

;;; ---------------------------------------------------------------------------
;;; Comando: control
;;; ---------------------------------------------------------------------------

(defun c:LOC-ID-CHECK
  (/ locales filas r l i f num n leidos esperado falta rep sinFila tot seq rec)
  (princ "\n=== Control de locales: SIMB-LOC_ID ===")
  (setq rec (SET-L:BloqueExiste (SET-L:BLOQUE)))
  (setq locales (SET-L:LocalesDelDibujo))
  (if (null rec)
    (if (null locales)
      (progn
        (princ (strcat "\nNo existe el bloque " (SET-L:BLOQUE)
                       " ni hay ejemplares rotulados."))
        (princ "\nCorre SIMB-LOC_ID (crea el bloque y rota los locales) o LOC-ID-DIAG para diagnosticar.")
        (princ)
        (exit))
      (progn
        (princ (strcat "\n  Ojo: el bloque " (SET-L:BLOQUE)
                       " no esta en la tabla de bloques, pero hay "
                       (itoa (length locales))
                       " ejemplares rotulados (definicion borrada o renombrada)."))
        (princ "\n  Corre LOC-ID-DIAG para ver el detalle."))))

  (setq r (SET-L:RectBloque))
  (if r
    (princ (strcat "\n  Rectangulo: " (rtos (car r) 2 3) " x " (rtos (cadr r) 2 3)
                   " m" (if (or (> (abs (- (car r) (SET-L:RECT-ANCHO))) (SET-L:EPS))
                               (> (abs (- (cadr r) (SET-L:RECT-ALTO))) (SET-L:EPS)))
                          "  <-- distinto del esperado (0.30 x 0.30)")))
    (princ "\n  El bloque no tiene rectangulo."))
  (princ (strcat "\n  Atributos: " (SET-L:TagsBloque)))

  (setq locales (SET-L:LocalesDelDibujo))
  (setq tot (length locales))
  (princ (strcat "\n=== Ejemplares insertados: " (itoa tot) " ==="))
  (if (> tot 0)
    (progn
      (setq filas (SET-L:Filas locales (SET-L:TOL-FILA)))

      (princ "\n--- Locales en orden de lectura (filas de arriba hacia abajo) ---")
      (setq i 0)
      (foreach f filas
        (foreach l f
          (setq i (1+ i))
          (princ (strcat "\n  " (SET-L:Num2 i) "  " (SET-L:NombreDe l)
                         "   en (" (rtos (car l) 2 2) ", " (rtos (cadr l) 2 2) ")"
                         "   [N_LOC " (SET-L:NumDe l) "]"))))

      ;; --- numeracion: faltantes y repetidos ---
      (setq leidos '())
      (foreach f filas
        (foreach l f (setq leidos (cons (atoi (caddr l)) leidos))))
      (setq tot (length leidos))
      (setq rep '())
      (setq falta '())
      (setq n 1)
      (while (<= n tot)
        (if (not (member n leidos))
          (setq falta (cons n falta))
          (if (> (length (SET-L:Repetidos leidos n)) 0)
            (setq rep (cons n rep))))
        (setq n (1+ n)))
      (princ "\n--- Numeracion ---")
      (princ (strcat "\n  Numeros: " (itoa tot)
                     (if (null rep) (strcat "  sin repetidos")
                      (strcat "  REPETIDOS: " (SET-L:ListaN rep)))
                     (if (null falta) "" (strcat "  FALTANTES: " (SET-L:ListaN falta)))))

      ;; --- orden de lectura ---
      (princ (strcat "\n--- Orden de lectura (X+ / Y-, filas con dY < "
                     (rtos (SET-L:TOL-FILA) 2 2) " m) ---"))
      (setq i 0)
      (setq n 0)
      (foreach f filas
        (foreach l f
          (setq i (1+ i))
          (if (/= (SET-L:Num2 i) (SET-L:NumDe l))
            (progn
              (setq n (1+ n))
              (princ (strcat "\n  FUERA DE ORDEN: el local " (SET-L:NumDe l) " ("
                             (SET-L:NombreDe l) ") en (" (rtos (car l) 2 2) ", "
                             (rtos (cadr l) 2 2) ") le corresponde el "
                             (SET-L:Num2 i)))))))
      (if (= n 0)
        (princ (strcat "\n  OK: los " (itoa tot) " locales estan en orden de lectura."))
        (princ (strcat "\n  " (itoa n) " local(es) fuera de orden.")))

      ;; --- locales sin fila ---
      (setq sinFila (SET-L:NoAsignados locales filas))
      (if sinFila
        (progn
          (princ "\n--- Locales que no entraron en ninguna fila ---")
          (foreach l sinFila
            (princ (strcat "\n  " (SET-L:NombreDe l) " en (" (rtos (car l) 2 2) ", "
                           (rtos (cadr l) 2 2) "): a mas de "
                           (rtos (SET-L:TOL-FILA) 2 2) " m de otra fila.")))))))

  (princ "\n")
  (princ))

(defun SET-L:Repetidos (leidos n / r x)
  "Veces que aparece el numero n en la lista."
  (foreach x leidos (if (= x n) (setq r (1+ r))))
  r)

(defun SET-L:ListaN (lst / s n)
  "Lista de numeros como texto: 3 4 12."
  (setq s "")
  (foreach n lst
    (setq s (strcat s (if (= "" s) "" " ") (SET-L:Num2 n))))
  s)

;;; ---------------------------------------------------------------------------
;;; Comando: diagnostico
;;; ---------------------------------------------------------------------------

(defun SET-L:REPORTE ()
  "Archivo de texto donde el diagnostico queda escrito (para revisarlo desde
   afuera, sin depender de la pantalla)."
  "P:/00-repos/proyecto-pi/vault-arquitectura/raw/reports/loc-id-diag.txt")

(defun SET-L:EscribeLineas (lineas / f x)
  "Escribe una lista de lineas de texto en el archivo de reporte."
  (setq f (open (SET-L:REPORTE) "w"))
  (if f
    (progn
      (foreach x lineas (write-line x f))
      (close f)
      (princ (strcat "\nReporte escrito en " (SET-L:REPORTE))))
    (princ "\nNo se pudo escribir el reporte (revisar permisos de la carpeta).")))

(defun c:LOC-ID-DIAG (/ rec r ss i e d n conAttr lineas ss2 ss3 ss4 x)
  "Muestra el estado real del bloque y de sus ejemplares en el dibujo, y lo
   deja escrito en un archivo de texto para poder revisarlo desde afuera."
  (setq lineas '())
  (setq lineas (cons (strcat "=== Diagnostico SIMB-LOC_ID | " (getvar "DATE") " " (getvar "CDATE") " ===") lineas))
  (setq lineas (cons (strcat "  INSUNITS = " (itoa (getvar "INSUNITS")) " (6 = metros)") lineas))
  (setq lineas (cons (strcat "  CLAYER  = " (getvar "CLAYER")) lineas))
  (setq rec (SET-L:BloqueExiste (SET-L:BLOQUE)))
  (setq lineas (cons (strcat "  Bloque " (SET-L:BLOQUE) ": " (if rec "ENCONTRADO en la tabla" "NO ENCONTRADO en la tabla")) lineas))
  (setq lineas (cons (strcat "  Blocks definidos en el dibujo: " (SET-L:ListaBloques)) lineas))
  (if rec
    (progn
      (setq r (SET-L:RectBloque))
      (setq lineas (cons (strcat "  Rectangulo: " (if r (strcat (rtos (car r) 2 3) " x " (rtos (cadr r) 2 3) " m") "NO SE PUDO LEER (no hay LWPOLYLINE en la definicion)")) lineas))
      (setq lineas (cons (strcat "  Atributos definidos: " (SET-L:TagsBloque)) lineas))))
  (setq lineas (cons (strcat "  Bloques insertados en el dibujo: " (SET-L:NombresInsert)) lineas))
  (setq ss (ssget "_X" '((0 . "INSERT"))))
  (setq n 0)
  (setq conAttr 0)
  (if ss
    (progn
      (setq i 0)
      (repeat (sslength ss)
        (setq e (ssname ss i))
        (if e
          (progn
            (setq d (entget e))
            (if (= (cdr (assoc 2 d)) (SET-L:BLOQUE))
              (progn
                (setq n (1+ n))
                (if (SET-L:Atributos e) (setq conAttr (1+ conAttr)))
                (setq lineas (cons (strcat "    local " (itoa n) "  N_LOC=" (if (SET-L:ValorAttr e "N_LOC") (SET-L:ValorAttr e "N_LOC") "-") "  TXT_LOC=" (if (SET-L:ValorAttr e "TXT_LOC") (SET-L:ValorAttr e "TXT_LOC") "-") "  en (" (rtos (car (assoc 10 d)) 2 2) ", " (rtos (cadr (assoc 10 d)) 2 2) ")") lineas))))
        (setq i (1+ i)))))
  (setq lineas (cons (strcat "  Ejemplares de " (SET-L:BLOQUE) ": " (itoa n) " (con atributos: " (itoa conAttr) ")") lineas))
  ;; el registro de la ultima sesion, si hubo
  (if SET-L:LOG-TEXTO
    (progn
      (setq lineas (cons "--- registro de la sesion ---" lineas))
      (foreach x (reverse SET-L:LOG-TEXTO) (setq lineas (cons (strcat "  " x) lineas)))))
  ;; censo de geometria suelta: si el bloque se creo a medias, quedan restos
  (setq ss2 (ssget "_X" '((0 . "LWPOLYLINE") (8 . "A-SIMBOLO-NPT-PLANTA"))))
  (setq lineas (cons (strcat "  LWPOLYLINE en la capa " (SET-L:LAYER) ": " (itoa (if ss2 (sslength ss2) 0)) "  (0 = normal; >0 = Possible geometria suelta de un bloque a medias)") lineas))
  (setq ss3 (ssget "_X" '((0 . "ATTDEF"))))
  (setq lineas (cons (strcat "  ATTDEF sueltas en el dibujo: " (itoa (if ss3 (sslength ss3) 0)) "  (0 = normal; >0 = rest??s de un bloque a medias)") lineas))
  (setq ss4 (ssget "_X" '((0 . "TEXT") (8 . "A-SIMBOLO-NPT-PLANTA"))))
  (setq lineas (cons (strcat "  TEXT en la capa " (SET-L:LAYER) ": " (itoa (if ss4 (sslength ss4) 0))) lineas))
  (SET-L:EscribeLineas lineas)
  (foreach x lineas (princ (strcat "\n" x)))
  (princ "\n")
  (princ))))