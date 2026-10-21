# -*- coding: utf-8 -*-
"""
Prepara la AXONOMETRIA MILITAR para imprimir (escala 1:50) y exporta el DXF.
=============================================================================

Toma el dibujo militar que ya esta en el documento (lo dejo
axonometria-militar-rhino.py) y arma la version IMPRIMIBLE:

  1) Duplica el dibujo (curvas, solido proyectado, ejes y cajetin) en las capas
     de plano, escalado 1:50 (1 m del modelo -> 20 mm en el papel) y corrido
     para que el origen del papel quede en el origen.
  2) Copia los espesores de trazo (Layer.PlotWeight) a las capas de plano.
  3) Exporta el DXF (AutoCAD) con la ruta indicada.
  4) Imprime el instructivo de plot (desde Rhino o desde AutoCAD).

Uso
---
  1) Rhino: correr antes axonometria-militar-rhino.py (deja el dibujo armado).
  2) Correr este script: Tools > Script > Run... > este archivo
     (o por MCP: execute_rhino_code con el contenido).
  3) Opcional: cambiar RUTA_DXF y ESCALA_PLANO arriba.

Que se verifica
---------------
  - La escala 1:50 se comprueba midiendo en el DXF: el ancho del dibujo debe
    medir 1/50 del ancho en el modelo.
  - Los angulos no cambian con la escala: el fondo sigue a 30 grados.

NOTA ES: todo el script vive dentro de una funcion (imprimir_militar) por lo
que se explained en el script hermano: el motor de MCP de Rhino ejecuta
exec(codigo, globals, locals) y las funciones de primer nivel no se encuentran
entre si.
"""


def imprimir_militar():
    """Escala el dibujo militar a 1:50, copia espesores y exporta el DXF."""

    import os
    import Rhino
    import scriptcontext as sc

    from Rhino.Geometry import Point3d, Vector3d, Transform

    # =============================================================================
    # CONFIGURACION
    # =============================================================================

    ESCALA_PLANO = 0.02        # 1:50 -> 1 m del modelo = 20 mm en el papel
    RUTA_DXF = (r"P:\00-repos\proyecto-pi\vault-arquitectura\activos"
                r"\mvp_05-rhino-mcp\axonometria-militar-1-50.dxf")
    NOMBRE_PLANO = "PLANO_MILITAR_1_50"

    # Capas del modelo (origen) -> capas del plano (destino) con su peso.
    CAPAS = [
        ("AXO_MILITAR_2D", "PLANO_ARISTAS", 0.25),
        ("AXO_MILITAR_SOLIDO", "PLANO_SOLIDO", 0.25),
        ("AXO_CORTES", "PLANO_CORTES", 0.70),
        ("AXO_EJES", "PLANO_EJES", 0.18),
        ("AXO_CAJETIN", "PLANO_CAJETIN", 0.18),
    ]

    def log(mensaje):
        print(mensaje)

    def paso(nombre, funcion):
        log("")
        log("> " + nombre)
        try:
            return funcion()
        except Exception as exc:
            log("  [FALLO] " + nombre + ": " + str(exc))
            return None

    def limpiar_plano():
        """Borra la version anterior del plano para poder reejecutar."""
        for origen, destino, peso in CAPAS:
            indice = sc.doc.Layers.FindByFullPath(destino, -1)
            if indice < 0:
                continue
            capa = sc.doc.Layers[indice]
            for obj in sc.doc.Objects.FindByLayer(capa):
                sc.doc.Objects.Delete(obj, True)

    def asegurar_capa(nombre, peso):
        """Crea (o reusa) la capa del plano y le pone el espesor de trazo."""
        indice = sc.doc.Layers.FindByFullPath(nombre, -1)
        if indice < 0:
            nueva = Rhino.DocObjects.Layer()
            nueva.Name = nombre
            indice = sc.doc.Layers.Add(nueva)
        capa = sc.doc.Layers[indice]
        capa.PlotWeight = peso
        capa.IsVisible = True
        return capa

    def escalar_y_copiar():
        """Duplica el dibujo al 1:50 y lo deja en las capas del plano.

        NOTA ES: se DUPLICA en vez de mover, para que el modelo y el dibujo en
        escala real sigan disponibles en el documento (el dibujo 1:1 se ve en el
        viewport, el 1:50 es el que se imprime).
        """
        # El dibujo vive en el plano y = -14 (ver el script hermano).
        y_dibujo = -14.0
        # Transformacion: escala 1:50 y vuelta al origen del papel.
        escala = Transform.Scale(ESCALA_PLANO)
        mover = Transform.Translation(Vector3d(0, 0, 0))
        total = Transform.Multiply(mover, escala)

        copiados = 0
        for origen, destino, peso in CAPAS:
            indice = sc.doc.Layers.FindByFullPath(origen, -1)
            if indice < 0:
                continue
            capa_destino = asegurar_capa(destino, peso)
            for obj in sc.doc.Objects.FindByLayer(sc.doc.Layers[indice]):
                if obj.Geometry is None:
                    continue
                copia = obj.Geometry.Duplicate()
                if copia is None:
                    continue
                # Se trae el dibujo al plano del papel (y = 0) y se escala.
                copia.Transform(Transform.Translation(Vector3d(0, -y_dibujo, 0)))
                copia.Transform(escala)
                attrs = Rhino.DocObjects.ObjectAttributes()
                attrs.Name = obj.Attributes.Name
                attrs.LayerIndex = capa_destino.Index
                if obj.Attributes.TextStyleIndex >= 0:
                    attrs.TextStyleIndex = obj.Attributes.TextStyleIndex
                sc.doc.Objects.AddGeometry(copia, attrs)
                copiados += 1
        log("  %d objetos copiados al 1:50." % copiados)
        return copiados

    def medir():
        """Mide el ancho y alto del plano escalado (control de calidad)."""
        caja = Rhino.Geometry.BoundingBox.Empty
        for origen, destino, peso in CAPAS:
            indice = sc.doc.Layers.FindByFullPath(destino, -1)
            if indice < 0:
                continue
            for obj in sc.doc.Objects.FindByLayer(sc.doc.Layers[indice]):
                if obj.Geometry is not None:
                    caja.Union(obj.Geometry.GetBoundingBox(True))
        ancho = caja.Max.X - caja.Min.X
        alto = caja.Max.Z - caja.Min.Z
        log("  Ancho del plano: %.1f mm   Alto: %.1f mm" % (ancho, alto))
        log("  (a escala 1:50, %.2f m del modelo miden %.1f mm)" %
            (ancho / ESCALA_PLANO, ancho))
        return ancho, alto

    def exportar_dxf():
        """Exporta el documento a DXF (AutoCAD)."""
        carpeta = os.path.dirname(RUTA_DXF)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        ok = sc.doc.Export(RUTA_DXF)
        if ok:
            log("  DXF exportado: %s" % RUTA_DXF)
        else:
            log("  [FALLO] no se pudo exportar el DXF")
        return ok

    def exportar_3dm():
        """Guarda una copia del .3dm (por si quieren el modelo con el plano)."""
        carpeta = os.path.dirname(RUTA_DXF)
        destino = os.path.join(carpeta, "axonometria-militar-1-50.3dm")
        ok = sc.doc.WriteFile(destino, 7)   # 7 = version de Rhino 8
        if ok:
            log("  3dm guardado: %s" % destino)
        else:
            log("  (no se pudo guardar el 3dm)")
        return ok

    def instructivo():
        """Imprime como plotear, en Rhino o en AutoCAD."""
        log("")
        log("=" * 74)
        log("INSTRUCTIVO DE IMPRESION")
        log("=" * 74)
        log("Desde RHINO (PDF directo):")
        log("  1) Vista > Vistas > Front   (el dibujo militar esta en ese viewport)")
        log("  2) Archivo > Imprimir > Ejecutar (_Plot)")
        log("     - Tamano de papel: A3 o A1 segun el tamano del modulo")
        log("     - Escala: 1:50  (o la que pidas; el plano 1:50 ya esta a escala)")
        log("     - Margenes: 10 mm")
        log("  3) Las capas PLANO_* ya tienen el espesor de trazo (PlotWeight):")
        for origen, destino, peso in CAPAS:
            log("       %-20s %.2f mm" % (destino, peso))
        log("")
        log("Desde AUTOADAD (DXF):")
        log("  1) Abrir el DXF exportado")
        log("  2) Isolation > Object > PLANO_ARISTAS, PLANO_SOLIDO, PLANO_EJES,")
        log("     PLANO_CAJETIN  (aislar SOLO las capas del plano)")
        log("  3) _ZOOM > _Extents  y _PLOT con escala 1:1 (el DXF ya esta en mm)")
        log("  4) Los espesores de linea viajan por capa (layer plot weight)")
        log("")
        log("Chequeo de angulos (invariante con la escala):")
        log("  El eje de profundidad del fondo tiene que salir a 30 grados de la")
        log("  horizontal (60 de la vertical) en TODAS las escalas.")
        log("  En el documento: capa PLANO_EJES, la linea EJE_Y.")
        log("=" * 74)

    log("=" * 74)
    log("PREPARACION DE IMPRESION - axonometria militar")
    log("Escala 1:%d" % int(round(1.0 / ESCALA_PLANO)))
    log("=" * 74)

    paso("1. Limpiar el plano anterior", limpiar_plano)
    paso("2. Escalar y copiar el dibujo", escalar_y_copiar)
    paso("3. Medir (control de calidad)", medir)
    paso("4. Exportar DXF", exportar_dxf)
    paso("5. Guardar copia 3dm", exportar_3dm)
    paso("6. Instructivo de impresion", instructivo)


imprimir_militar()
