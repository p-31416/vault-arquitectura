# -*- coding: utf-8 -*-
"""
Axonometria militar 30/60 en Rhino 8 (ejemplo: modulo de platform frame).
=============================================================================

Arma, de punta a punta, la representacion axonometrica "militar" (30/60) de un
MODULO REAL de platform frame: grilla de vigas primarias y secundarias, losa de
entrepiso con vacio circular, columnas y dos planos delimitadores para cortes.

Produce:

  (A) VISTA AXONOMETRICA 3D  -> camara paralela (azimut 45, elevacion 35.264).
      Los tres ejes se dibujan a 30/30/90 en pantalla. Es la axonometria 3D
      navegable: admite planos delimitadores, cortes, sombras, render.

  (B) DIBUJO MILITAR EXACTO  -> proyeccion paralela OBLICUA sobre el plano
      frontal (Transform.ProjectAlong). Anchos y alturas en verdadera
      magnitud; la profundidad se dibuja a 30 de la horizontal (60 de la
      vertical), escala 1 (militar) o 1/2 (cabinet).

  (C) IMPRESION  -> capas con espesor de trazo, cajetin con titulo/escala/
      angulo, y el dibujo en escala 1:50 listo para plot (ver el script
      hermano axonometria-militar-imprimir.py).

COMO EJECUTARLO
----------------
  1) Rhino 8: Tools > Script > Run... > este archivo. (Menu > Archivo)
  2) O por MCP (comunitario reer-rhino-mcp): la tool `execute_rhino_code` con
     el contenido de este archivo.
  3) Reejecutarlo es idempotente: borra las capas AXO_* y vuelve a crearlas.

VERIFICACION
------------
  Al final imprime el angulo real del eje de profundidad (debe dar 30.00) y la
  direccion de proyeccion usada.

---

REFERENCIAS (verificadas)
--------------------------
  - Rhino 8 > PlanoDelimitador / SeccionesDeCorte:
    https://docs.mcneel.com/rhino/8/help/es-es/commands/clippingplane.htm
  - Corte selectivo (Rhino 8):
    https://www.rhino3d.com/es/features/clipping/selective-clipping/
  - API Transform.ProjectAlong (proyeccion paralela oblicua):
    https://mcneel.github.io/rhinocommon-api-docs/api/RhinoCommon/html/M_Rhino_Geometry_Transform_ProjectAlong.htm
  - API Intersection.BrepPlane (curvas de seccion):
    https://mcneel.github.io/rhinocommon-api-docs/api/RhinoCommon/html/M_Rhino_Geometry_Intersect_Intersection_BrepPlane.htm
  - API ObjectTable.AddClippingPlane (plano delimitador):
    https://developer.rhino3d.com/api/rhinocommon/rhino.docobjects.tables.objecttable/addclippingplane
  - Tutorial de perspectiva militar (referencia del estudio):
    https://www.youtube.com/watch?v=yXpm6yGVBI0
"""

# NOTA ES: TODO el script vive dentro de la funcion axonometria_militar().
# Eso lo hace inmune a como lo ejecute el Motor de MCP de Rhino, que hace
# exec(codigo, globals, locals): con esa forma las funciones de primer nivel
# quedan en 'locals' y no se encuentran entre si (NameError: 'log').
# Dentro de una funcion contenedora, cada funcion interna cierra sobre las
# variables de la contenedora (closure) y todo se resuelve bien.


def axonometria_militar():
    """Ejecuta la axonometria militar 30/60 sobre el modulo de platform frame."""

    import math
    import os
    import System

    import Rhino
    import scriptcontext as sc

    from Rhino.Geometry import (Point3d, Vector3d, Plane, Box, Cylinder, Circle,
                                Brep, Transform, Interval, TextDot, TextEntity)
    from Rhino.DocObjects import ObjectAttributes, Layer

    # =============================================================================
    # CONFIGURACION -- cambiar aca y reejecutar
    # =============================================================================

    # Angulo del eje de profundidad en el dibujo militar, en grados sobre la
    # horizontal. 30 = militar clasico (el mismo angulo que 60 sobre la
    # vertical). 60 = la variante "profundidad empinada".
    ANGULO_RECESO_GRADOS = 30.0

    # Escala del eje de profundidad. 1.0 = militar (cavalier 30/1).
    # 0.5 = cabinet (el fondo se dibuja a la mitad de su largo real).
    ESCALA_RECESO = 1.0

    # True = la profundidad retrocede hacia la IZQUIERDA del dibujo.
    MIRRAR_PROFUNDIDAD = False

    # Modulo de platform frame (todo en metros).
    BAY = 3.0                 # luz de la grilla
    N_BAYS = 3                # 3 x 3 luces -> 9.0 x 9.0 m
    LADO = BAY * N_BAYS       # 9.00 m
    VIGA_RIZ = 0.35           # ancho de la viga primaria
    VIGA_ALT = 0.60           # alto de la viga primaria
    VIGA_SEC_ANCH = 0.20      # ancho de la viga secundaria
    VIGA_SEC_ALT = 0.40       # alto de la viga secundaria
    COL_SEC = 0.30            # seccion de columna
    COL_ALT = 2.60            # altura de columna bajo las vigas
    LOSA_ESP = 0.18           # espesor de la losa de entrepiso
    VACIO_DIAM = 2.60         # diametro del vacio circular en la losa

    # Donde se deja el dibujo militar 2D, separado del modelo 3D (en Y).
    DISTANCIA_DIBUJO_2D = -14.0

    # Camara axonometrica 3D.
    # 35.264 grados es la elevacion EXACTA que hace que los ejes de planta se
    # dibujen a 30 de la horizontal (60 de la vertical).
    AZIMUT_AXONOMETRICA = 45.0
    ELEVACION_AXONOMETRICA = 35.264389682754654

    # Cajetin (titulo) del dibujo militar.
    TITULO = "MODULO PLATFORM FRAME - AXONOMETRIA MILITAR 30/60"
    SUBTITULO = ("Sistema de entramado de vigas con losa de entrepiso y vacio "
                 "central. Proyeccion paralela oblicua 30-60.")
    ESCALA_TEXTO = "ESCALA 1:50"

    # Capas del script.
    CAPA_MODELO = "AXO_ESTRUCTURA"
    CAPA_LOSA = "AXO_LOSA"
    CAPA_CORTES = "AXO_CORTES"
    CAPA_DIBUJO = "AXO_MILITAR_2D"
    CAPA_DIBUJO_SOLIDO = "AXO_MILITAR_SOLIDO"
    CAPA_EJES = "AXO_EJES"
    CAPA_CAJETIN = "AXO_CAJETIN"

    # Espesores de trazo para imprimir (mm). Rhino 8: Layer.PlotWeight.
    PESOS = {
        CAPA_MODELO: 0.50,
        CAPA_LOSA: 0.35,
        CAPA_CORTES: 0.70,
        CAPA_DIBUJO: 0.25,
        CAPA_DIBUJO_SOLIDO: 0.25,
        CAPA_EJES: 0.18,
        CAPA_CAJETIN: 0.18,
    }

    # =============================================================================
    # UTILIDADES
    # =============================================================================

    def log(mensaje):
        """Escribe en la consola de Python de Rhino."""
        print(mensaje)

    def paso(nombre, funcion):
        """Ejecuta un paso tolerante a fallos: si uno falla, el resto sigue."""
        log("")
        log("> " + nombre)
        try:
            return funcion()
        except Exception as exc:
            log("  [FALLO] " + nombre + ": " + str(exc))
            return None

    def limpiar_capas():
        """Borra (o crea vacias) las capas AXO_* para que el script sea repetible."""
        for nombre in PESOS:
            indice = sc.doc.Layers.FindByFullPath(nombre, -1)
            if indice >= 0:
                capa = sc.doc.Layers[indice]
                for obj in sc.doc.Objects.FindByLayer(capa):
                    sc.doc.Objects.Delete(obj, True)
                capa.IsVisible = True
            else:
                nueva = Layer()
                nueva.Name = nombre
                indice = sc.doc.Layers.Add(nueva)
            capa = sc.doc.Layers[indice]
            capa.PlotWeight = PESOS[nombre]
            capa.PlotColor = sc.doc.Layers[indice].PrintColor \
                if hasattr(sc.doc.Layers[indice], "PrintColor") else capa.PlotColor

    def obtener_capa(nombre):
        """Devuelve el objeto Layer por nombre, creandolo si hace falta."""
        indice = sc.doc.Layers.FindByFullPath(nombre, -1)
        if indice < 0:
            nueva = Layer()
            nueva.Name = nombre
            indice = sc.doc.Layers.Add(nueva)
        return sc.doc.Layers[indice]

    def atributos(nombre, capa_nombre):
        """Arma ObjectAttributes con nombre y capa (LayerIndex, no SetLayer)."""
        attrs = ObjectAttributes()
        attrs.Name = nombre
        attrs.LayerIndex = obtener_capa(capa_nombre).Index
        return attrs

    def objetos_de_capa(nombres):
        """Devuelve los objetos con geometria que viven en las capas indicadas."""
        salida = []
        for nombre in nombres:
            indice = sc.doc.Layers.FindByFullPath(nombre, -1)
            if indice < 0:
                continue
            for obj in sc.doc.Objects.FindByLayer(sc.doc.Layers[indice]):
                if obj.Geometry is not None:
                    salida.append(obj)
        return salida

    def ver_capas(nombres, mostrar):
        """Muestra u oculta capas (True/False)."""
        for nombre in nombres:
            indice = sc.doc.Layers.FindByFullPath(nombre, -1)
            if indice >= 0:
                sc.doc.Layers[indice].IsVisible = mostrar

    def centro_y_caja(objetos):
        """Devuelve (centro, caja envolvente) del conjunto de objetos."""
        caja = Rhino.Geometry.BoundingBox.Empty
        for obj in objetos:
            if obj.Geometry is None:
                continue
            caja.Union(obj.Geometry.GetBoundingBox(True))
        return caja.Center, caja

    def viewport_nombre(nombre):
        """Devuelve el viewport con ese nombre (o el activo si no existe)."""
        for v in sc.doc.Views.GetViewList(True, False):
            if v.ActiveViewport.Name == nombre:
                return v.ActiveViewport
        return sc.doc.Views.ActiveView.ActiveViewport

    def caja_entre(x0, x1, y0, y1, z0, z1):
        """Crea una caja (Brep) dados sus limites en los tres ejes."""
        plano = Plane(Point3d(x0, y0, z0), Vector3d(0, 0, 1))
        return Box(plano, Interval(0, x1 - x0), Interval(0, y1 - y0),
                   Interval(0, z1 - z0)).ToBrep()

    # =============================================================================
    # 1) MODELO: modulo de platform frame
    # =============================================================================

    def crear_platform_frame():
        """Modulo de platform frame: grilla de vigas + losa con vacio + columnas.

        NOTA ES: la logica constructiva es la del estudio: vigas primarias en X,
        vigas secundarias encajadas en Y, losa de entrepiso encima y columnas
        en los nodos. El vacio circular es el caso de vacio de entrepiso.
        """
        solidos = []

        # --- vigas primarias (eje X) ---------------------------------------
        for i in range(N_BAYS + 1):
            y = i * BAY
            brep = caja_entre(-0.20, LADO + 0.20,
                              y - VIGA_RIZ / 2.0, y + VIGA_RIZ / 2.0,
                              -VIGA_ALT, 0.0)
            attrs = atributos("VIGA_RIZ_%02d" % (i + 1), CAPA_MODELO)
            solidos.append(sc.doc.Objects.AddBrep(brep, attrs))

        # --- vigas secundarias (eje Y), encajadas bajo las primarias --------
        n_sec = N_BAYS * 2 + 1
        for j in range(n_sec):
            x = j * (LADO / (n_sec - 1))
            brep = caja_entre(x - VIGA_SEC_ANCH / 2.0, x + VIGA_SEC_ANCH / 2.0,
                              -0.20, LADO + 0.20,
                              -VIGA_SEC_ALT, 0.0)
            attrs = atributos("VIGA_SEC_%02d" % (j + 1), CAPA_MODELO)
            solidos.append(sc.doc.Objects.AddBrep(brep, attrs))

        # --- columnas en los nodos ------------------------------------------
        nodos = []
        for i in (0, N_BAYS):
            for j in (0, N_BAYS):
                nodos.append((i * BAY, j * BAY))
        nodos.append((LADO / 2.0, LADO / 2.0))
        for k, (x, y) in enumerate(nodos):
            brep = caja_entre(x - COL_SEC / 2.0, x + COL_SEC / 2.0,
                              y - COL_SEC / 2.0, y + COL_SEC / 2.0,
                              -VIGA_ALT - COL_ALT, -VIGA_ALT)
            attrs = atributos("COLUMNA_%02d" % (k + 1), CAPA_MODELO)
            solidos.append(sc.doc.Objects.AddBrep(brep, attrs))

        # --- losa de entrepiso con vacio circular ----------------------------
        losa = caja_entre(0, LADO, 0, LADO, 0.0, LOSA_ESP)
        centro = Plane(Point3d(LADO / 2.0, LADO / 2.0, -1.0),
                       Vector3d(0, 0, 1))
        circulo = Circle(centro, VACIO_DIAM / 2.0)
        vacio = Cylinder(circulo, LOSA_ESP + 2.0).ToBrep(True, True)
        resultado = Brep.CreateBooleanDifference([losa], [vacio],
                                                 sc.doc.ModelAbsoluteTolerance)
        if resultado:
            for k, brep in enumerate(resultado):
                attrs = atributos("LOSA_%02d" % (k + 1), CAPA_LOSA)
                solidos.append(sc.doc.Objects.AddBrep(brep, attrs))
        else:
            attrs = atributos("LOSA_01", CAPA_LOSA)
            solidos.append(sc.doc.Objects.AddBrep(losa, attrs))

        log("  Platform frame: %d vigas primarias (%.2f x %.2f), %d secundarias "
            "(%.2f x %.2f), %d columnas, losa %.2f con vacio D%.2f." %
            (N_BAYS + 1, VIGA_RIZ, VIGA_ALT, n_sec, VIGA_SEC_ANCH, VIGA_SEC_ALT,
             len(nodos), LOSA_ESP, VACIO_DIAM))
        log("  Modulo: %.2f x %.2f m, luces de %.2f m." % (LADO, LADO, BAY))
        return solidos

    # =============================================================================
    # 2) LA MATRIZ DE LA PROYECCION MILITAR (el corazon del script)
    # =============================================================================

    def direccion_proyeccion(angulo_grados, escala, mirror):
        """Devuelve la direccion de proyeccion para la perspectiva militar.

        MATEMATICA (plano frontal de dibujo, profundidad en +Y):

            El plano de proyeccion es y = 0.
            Un rayo parte de p = (x, y, z) y viaja en la direccion d.
            Choca contra y = 0 cuando y + t*dy = 0, o sea t = -y/dy.
            El impacto tiene coordenadas de dibujo:

                U = x - y * (dx/dy)        (horizontal del dibujo)
                V = z - y * (dz/dy)        (vertical del dibujo)

            Quiero:
                eje X  ->  U = 1 , V = 0     (ancho en verdadera magnitud)
                eje Z  ->  U = 0 , V = 1     (altura en verdadera magnitud)
                eje Y  ->  U = k*cos(a), V = k*sin(a)  (profundidad a 30, escala k)

            De ahi sale:
                dx = -k*cos(a)*dy
                dz = -k*sin(a)*dy

        NOTA ES: esta es la "proyeccion paralela oblicua" de manual. No es
        perspective (no hay punto de fuga) y no es axonometrica ortogonal (el
        eje de profundidad NO esta acortado: entra a escala 1).
        """
        a = math.radians(angulo_grados)
        k = escala
        dy = 1.0
        signo = 1.0 if mirror else -1.0
        d = Vector3d(signo * k * math.cos(a), dy, -k * math.sin(a))
        d.Unitize()   # Unitize() MUTA el vector (no hay propiedad Unitized)
        return d

    def verificar_angulo(direccion, angulo_grados, escala):
        """Recalcula el angulo real del eje de profundidad proyectado y lo imprime.

        NOTA ES: control de calidad del script. Si el numero impreso no
        coincide con el angulo pedido, la matriz esta mal.
        """
        dy = direccion.Y
        if abs(dy) < 1e-9:
            raise RuntimeError("La direccion de proyeccion es paralela al plano.")
        u = -direccion.X / dy      # componente horizontal del eje Y proyectado
        v = -direccion.Z / dy      # componente vertical del eje Y proyectado
        largo = math.sqrt(u * u + v * v)
        angulo_real = math.degrees(math.atan2(v, u)) % 360.0

        log("  Direccion de proyeccion: (%.4f, %.4f, %.4f)" %
            (direccion.X, direccion.Y, direccion.Z))
        log("  Eje de profundidad -> U = %.4f , V = %.4f  (largo %.4f)" % (u, v, largo))
        log("  Angulo real sobre la horizontal: %.2f grados (pedido %.2f)" %
            (angulo_real, angulo_grados))
        log("  Escala del fondo: %.3f (militar = 1.000)" % largo)
        return angulo_real

    # =============================================================================
    # 3) DIBUJO MILITAR 2D (proyeccion paralela oblicua)
    # =============================================================================

    def proyectar_curvas(curvas, xform, capa_nombre, prefijo):
        """Proyecta una lista de curvas con una transformacion y las mete al doc.

        NOTA ES: GeometryBase.Transform(xform) MUTA la geometria (no hay flag
        inPlace), por eso se duplica antes.
        """
        agregadas = []
        for i, curva in enumerate(curvas):
            if curva is None:
                continue
            proyectada = curva.Duplicate()
            if not proyectada.Transform(xform):
                continue
            attrs = atributos("%s_%03d" % (prefijo, i + 1), capa_nombre)
            sc.doc.Objects.AddCurve(proyectada, attrs)
            agregadas.append(proyectada)
        log("  %d curvas proyectadas en la capa %s." % (len(agregadas), capa_nombre))
        return agregadas

    def proyectar_solido(brep, xform):
        """Proyecta el SOLIDO a la militar y lo mete al documento.

        NOTA ES: proyectar el solido (y no solo sus aristas) deja una cara
        plana con la silueta: eso se ve CON MASA en el viewport.
        """
        copia = brep.Duplicate()
        if not copia.Transform(xform):
            return None
        attrs = atributos("MILITAR_SOLIDO", CAPA_DIBUJO_SOLIDO)
        sc.doc.Objects.AddBrep(copia, attrs)
        return copia

    def crear_ejes_referencia(xform):
        """Dibuja la triada de ejes proyectada (X, Y, Z) para ver los 30/60.

        NOTA ES: es la prueba de lectura del dibujo. La linea proyectada del
        eje Y tiene que salir a 30 grados; la del X horizontal; la del Z
        vertical.
        """
        origen = Point3d(0, 0, 0)
        largo = 2.0
        ejes = [("X", Vector3d(1, 0, 0)),
                ("Y", Vector3d(0, 1, 0)),
                ("Z", Vector3d(0, 0, 1))]

        for nombre, vector in ejes:
            linea = Rhino.Geometry.Line(origen, origen + vector * largo)
            proyectada = linea.ToNurbsCurve()
            proyectada.Transform(xform)
            attrs = atributos("EJE_" + nombre, CAPA_EJES)
            sc.doc.Objects.AddCurve(proyectada, attrs)
            try:
                punto = proyectada.Points[proyectada.Points.Count - 1].Location
                dot = TextDot(nombre, punto)
                sc.doc.Objects.AddTextDot(dot, atributos("ETIQUETA_" + nombre,
                                                         CAPA_EJES))
            except Exception as exc:
                log("  (no se pudo rotular el eje %s: %s)" % (nombre, exc))
        log("  Triada de ejes proyectada: X horizontal, Z vertical, Y a 30 grados.")

    # =============================================================================
    # 4) CAJETIN (para imprimir)
    # =============================================================================

    def crear_cajetin(xform, ancho, alto):
        """Arma el cajetin (recuadro + textos) en el plano del dibujo.

        NOTA ES: el cajetin vive en el plano del dibujo militar (y = -14), con
        la misma matriz de proyeccion, asi que sale ortogonal al papel.
        """
        # Rectangulo del cajetin: en coordenadas de dibujo, debajo del dibujo.
        y0 = -2.60
        y1 = -0.40
        x0 = 0.0
        x1 = ancho * 0.75

        plano_papel = Plane(Point3d(0, 0, 0), Vector3d(1, 0, 0),
                            Vector3d(0, 0, 1))

        # La transformacion del cajetin: proyectar (x, 0, z) con la militar y
        # sumar la traslacion en Y.
        def punto_dibujo(u, v):
            p = Point3d(u, 0.0, v)
            p.Transform(xform)
            return p

        rect = Rhino.Geometry.Polyline([punto_dibujo(x0, y0), punto_dibujo(x1, y0),
                                        punto_dibujo(x1, y1), punto_dibujo(x0, y1),
                                        punto_dibujo(x0, y0)])
        sc.doc.Objects.AddCurve(rect.ToNurbsCurve(),
                                atributos("CAJETIN_MARCO", CAPA_CAJETIN))

        textos = [
            (TITULO, x0 + 0.30, y1 - 0.55, 0.28),
            (SUBTITULO, x0 + 0.30, y1 - 0.95, 0.16),
            (ESCALA_TEXTO + "   |   PROYECCION PARALELA OBLICUA 30-60   |   "
             + str(sc.doc.ModelUnitSystem), x0 + 0.30, y0 + 0.35, 0.18),
        ]
        for i, (texto, u, v, alto) in enumerate(textos):
            try:
                # TextEntity vive en un plano; se usa el plano del dibujo.
                entidad = TextEntity(plano_papel, punto_dibujo(u, v), texto, alto)
                sc.doc.Objects.AddText(entidad, atributos("CAJETIN_TXT_%02d" % (i + 1),
                                                          CAPA_CAJETIN))
            except Exception:
                try:
                    dot = TextDot(texto, punto_dibujo(u, v))
                    sc.doc.Objects.AddTextDot(dot, atributos("CAJETIN_TXT_%02d" % (i + 1),
                                                            CAPA_CAJETIN))
                except Exception as exc:
                    log("  (no se pudo escribir el texto %d: %s)" % (i + 1, exc))
        log("  Cajetin generado (%.1f x %.1f) con titulo y escala." %
            (x1 - x0, y1 - y0))

    # =============================================================================
    # 5) CORTES: planos delimitadores + curvas de seccion
    # =============================================================================

    def curvas_de_seccion(brep, plano, etiqueta):
        """Extrae las curvas de interseccion de un solido con un plano infinito.

        NOTA ES: BrepPlane devuelve la tupla (ok, curvas, puntos).
        """
        tolerancia = sc.doc.ModelAbsoluteTolerance
        salida = Rhino.Geometry.Intersect.Intersection.BrepPlane(brep, plano,
                                                                 tolerancia)
        curvas = salida[1] if isinstance(salida, tuple) and len(salida) >= 2 else []
        curvas = [c for c in (curvas or []) if c is not None]
        log("  Seccion %s: %d curvas." % (etiqueta, len(curvas)))
        return curvas

    def crear_plano_delimitador(plano, nombre, vista_ids):
        """Crea un plano delimitador (clipping plane) en las vistas indicadas.

        NOTA ES: la normal del plano apunta hacia la mitad que QUEDA VISIBLE.
        """
        diag = LADO * 1.4
        guid = sc.doc.Objects.AddClippingPlane(plano, diag, diag, vista_ids,
                                               atributos(nombre, CAPA_CORTES))
        if guid == System.Guid.Empty:
            raise RuntimeError("No se pudo crear el plano delimitador " + nombre)
        log("  Plano delimitador %s creado." % nombre)
        return guid

    def excluir_del_corte(ids_objetos, indices_capa):
        """Deja fuera del recorte a los objetos/layers indicados.

        NOTA ES: es el CORTE SELECTIVO de Rhino 8. Sin esto, los planos
        delimitadores recortan tambien el dibujo militar 2D (que vive en el
        mismo modelo) y el dibujo sale mutilado.
        """
        for obj in sc.doc.Objects:
            if not isinstance(obj, Rhino.DocObjects.ClippingPlaneObject):
                continue
            geometria = obj.ClippingPlaneGeometry
            geometria.ParticipationListsEnabled = True
            geometria.SetClipParticipation(ids_objetos, indices_capa, True)
            obj.CommitChanges()
            log("  Corte selectivo: %s excluye %d objetos / %d capas." %
                (obj.Attributes.Name, len(ids_objetos), len(indices_capa)))

    # =============================================================================
    # 6) VISTAS
    # =============================================================================

    def fijar_vista(vp, origen, eje_x, eje_y, encuadrar=True):
        """Fija la vista con un plano de vista explicito (SetToPlanView).

        NOTA ES: SetToPlanView(origen, ejeX, ejeY) define el plano de la vista
        (eje X a la derecha, eje Y hacia arriba) en paralelo. Es la via
        robusta: a mano, con SetCameraLocation, el viewport en paralelo no
        respeta la direccion (Redraw la reescribe) y los metodos de zoom
        (ZoomBoundingBox / ZoomExtents) restauran la camara anterior.
        """
        vp.ChangeToParallelProjection(True)
        vp.SetToPlanView(origen, eje_x, eje_y, False)
        sc.doc.Views.Redraw()
        if encuadrar:
            vp.ZoomExtents()
            sc.doc.Views.Redraw()

    def vista_axonometrica_3d(objetos):
        """Camara paralela en axonometrica: azimut 45, elevacion 35.264.

        NOTA ES: por que 35.264 grados y no 30: con azimut 45 y elevacion t, los
        ejes de planta se dibujan a atan(sin t) de la horizontal. Para que ese
        angulo sea exactamente 30 hace falta sin(t) = tan(30), o sea
        t = asin(tan(30)) = 35.264 grados.
        """
        centro, caja = centro_y_caja(objetos)
        az = math.radians(AZIMUT_AXONOMETRICA)
        el = math.radians(ELEVACION_AXONOMETRICA)
        direccion = Vector3d(math.cos(el) * math.sin(az),
                             math.cos(el) * math.cos(az),
                             math.sin(el))
        eje_x = Vector3d(math.sin(az), -math.cos(az), 0)
        eje_y = Vector3d.CrossProduct(eje_x, direccion)

        # En la vista 3D se ocultan las capas del dibujo plano: lo que se ve es
        # el SOLIDO en axonometria, no un alzado tumbado en el piso.
        ver_capas([CAPA_DIBUJO, CAPA_DIBUJO_SOLIDO, CAPA_EJES, CAPA_CAJETIN],
                  False)
        fijar_vista(viewport_nombre("Perspective"), centro, eje_x, eje_y)
        sc.doc.Views.Redraw()
        log("  Camara paralela: azimut %.1f, elevacion %.3f." %
            (AZIMUT_AXONOMETRICA, ELEVACION_AXONOMETRICA))

    def vista_frontal(objetos):
        """Camara frontal paralela, para mirar el dibujo militar 2D sin escorzo."""
        centro, caja = centro_y_caja(objetos)
        ver_capas([CAPA_DIBUJO, CAPA_DIBUJO_SOLIDO, CAPA_EJES, CAPA_CAJETIN],
                  True)
        fijar_vista(viewport_nombre("Front"), centro, Vector3d(1, 0, 0),
                    Vector3d(0, 0, 1))
        sc.doc.Views.Redraw()
        log("  Camara frontal paralela (para ver el dibujo militar).")

    # =============================================================================
    # PROGRAMA PRINCIPAL
    # =============================================================================

    log("=" * 74)
    log("AXONOMETRIA MILITAR %g/%g - modulo de platform frame" %
        (ANGULO_RECESO_GRADOS, 90.0 - ANGULO_RECESO_GRADOS))
    log("Unidades del documento: %s" % str(sc.doc.ModelUnitSystem))
    log("=" * 74)

    paso("0. Capas y espesores de trazo", limpiar_capas)

    modelo = paso("1. Modulo de platform frame", crear_platform_frame)
    if modelo is None:
        log("Sin modelo: se aborta.")
        return

    # NOTA ES: los planos de corte se aplican a las vistas ortogonales, NO al
    # viewport "Perspective" (la axonometrica 3D): asi se ve el modulo entero
    # en 3D y el corte se ve en las vistas donde tiene sentido.
    vista_ids = [v.ActiveViewport.Id for v in sc.doc.Views.GetViewList(True, False)
                 if v.ActiveViewport.Name != "Perspective"]

    # --- Cortes -------------------------------------------------------------
    # Corte A: horizontal a la altura del encajonado de las vigas secundarias.
    z_corte = -VIGA_SEC_ALT / 2.0
    plano_a = Plane(Point3d(0, 0, z_corte), Vector3d(0, 0, -1))
    # Corte B: vertical por el centro (por el vacio de la losa).
    plano_b = Plane(Point3d(LADO / 2.0, 0, 0), Vector3d(-1, 0, 0))

    # NOTA ES: AddBrep devuelve un Guid, no un objeto.
    solido_principal = sc.doc.Objects.FindId(modelo[0]).Geometry

    secciones = paso("2. Curvas de seccion", lambda: (
        curvas_de_seccion(solido_principal, plano_a,
                          "A (horizontal z=%.2f)" % z_corte)))
    if secciones is None:
        secciones = []

    paso("3. Planos delimitadores (corte visual)", lambda: (
        crear_plano_delimitador(plano_a, "CORTE_A", vista_ids),
        crear_plano_delimitador(plano_b, "CORTE_B", vista_ids)))

    # --- Matriz de proyeccion ----------------------------------------------
    def _matriz():
        direccion = direccion_proyeccion(ANGULO_RECESO_GRADOS,
                                          ESCALA_RECESO,
                                          MIRRAR_PROFUNDIDAD)
        verificar_angulo(direccion, ANGULO_RECESO_GRADOS, ESCALA_RECESO)
        # Plano del dibujo: y = 0 (plano frontal).
        plano_dibujo = Plane(Point3d(0, 0, 0), Vector3d(1, 0, 0),
                             Vector3d(0, 0, 1))
        proyeccion = Transform.ProjectAlong(plano_dibujo, direccion)
        return Transform.Multiply(Transform.Translation(0, DISTANCIA_DIBUJO_2D, 0),
                                  proyeccion)

    xform = paso("4. Matriz de proyeccion militar", _matriz)
    if xform is None:
        log("Sin matriz: no se puede dibujar.")
        return

    # --- Dibujo militar -----------------------------------------------------
    def _dibujo():
        for guid in modelo:
            brep = sc.doc.Objects.FindId(guid).Geometry
            proyectar_solido(brep, xform)
        aristas = []
        for guid in modelo:
            brep = sc.doc.Objects.FindId(guid).Geometry
            aristas.extend(list(brep.Edges))
        proyectar_curvas(aristas, xform, CAPA_DIBUJO, "ARISTA")
        proyectar_curvas(secciones, xform, CAPA_DIBUJO, "CORTE")
        crear_ejes_referencia(xform)

    paso("5. Dibujo militar 2D", _dibujo)

    paso("5b. Corte selectivo (el dibujo 2D queda fuera del recorte)", lambda: (
        excluir_del_corte(
            [obj.Id for obj in objetos_de_capa([CAPA_DIBUJO, CAPA_DIBUJO_SOLIDO,
                                                CAPA_EJES, CAPA_CAJETIN])],
            [sc.doc.Layers.FindByFullPath(CAPA_DIBUJO, -1),
             sc.doc.Layers.FindByFullPath(CAPA_DIBUJO_SOLIDO, -1),
             sc.doc.Layers.FindByFullPath(CAPA_EJES, -1),
             sc.doc.Layers.FindByFullPath(CAPA_CAJETIN, -1)])))

    paso("6. Cajetin", lambda: crear_cajetin(xform, LADO, LADO))

    # --- Vistas -------------------------------------------------------------
    objetos_3d = objetos_de_capa([CAPA_MODELO, CAPA_LOSA])
    objetos_dibujo = objetos_de_capa([CAPA_DIBUJO, CAPA_EJES, CAPA_CAJETIN])

    paso("7. Vista frontal (encuadre del dibujo militar)",
         lambda: vista_frontal(objetos_dibujo or objetos_3d))
    paso("8. Vista axonometrica 3D (estado final)",
         lambda: vista_axonometrica_3d(objetos_3d or objetos_dibujo))

    try:
        # NOTA ES: en Rhino 8 el enum DisplayMode no se puede importar desde
        # Rhino.Display y RhinoApp.RunCommand no existe en Python: la via que
        # funciona es RhinoApp.RunScript (o ExecuteCommand).
        Rhino.RhinoApp.ExecuteCommand(sc.doc, "_Shaded")
        sc.doc.Views.Redraw()
    except Exception as exc:
        log("  (no se pudo cambiar el modo de visualizacion: %s)" % exc)

    log("")
    log("=" * 74)
    log("LISTO. Como verificar:")
    log("  1) Vista 3D (Perspective): el modulo en axonometrica 30/60 con el")
    log("     entramado, la losa con el vacio y los planos de corte.")
    log("  2) Vista 2D (Front): el dibujo militar con el cajetin.")
    log("     En la capa %s, la linea del eje Y tiene que salir a %g grados." %
        (CAPA_EJES, ANGULO_RECESO_GRADOS))
    log("  3) Impresion: scripts\\axonometria-militar-imprimir.py (escala 1:50,")
    log("     exporta DXF y deja el plot listo en Rhino).")
    log("=" * 74)


axonometria_militar()
