#! python3
# -*- coding: utf-8 -*-
"""
inspeccionar-seccion-rhino.py
=============================

Inspección de **solo lectura** de un `.3dm` de Rhino 8 para diagnosticar por qué
el corte 3D se ve **sin hatch** dentro del detalle de la lámina (aunque en la vista
de trabajo el mismo corte sí sale con la trama por material).

Uso (línea de comandos de Rhino 8)::

    _RunPythonScript "P:\\00-repos\\proyecto-pi\\vault-arquitectura\\scripts\\inspeccionar-seccion-rhino.py"

El script **no modifica el documento**: solo lee. El informe sale por la línea de
comandos de Rhino y también se puede recuperar por el puente MCP.

Compatible con RhinoPython 3 (CPython) y con IronPython 2.7.

Qué mira
--------
1. Documento: ruta, unidades, cantidad de objetos/capas/vistas.
2. Planos de corte: cuántos hay, en qué capa, su plano y **todas** sus propiedades
   (se vuelca en bloque, porque la API expone nombres distintos según versión).
3. Capas: color de impresión, ancho de línea y **Estilo de sección** (patrón,
   escala, rotación, colores) — el punto crítico: la escala del patrón decide si
   la trama se lee en el papel.
4. Objetos: cuántos hay de cada tipo y cuántos son sólidos **cerrados** (la
   sección solo se rellena si el objeto se corta de forma cerrada).
5. Vistas y detalles: qué lámina hay, cómo se llama cada detalle, con qué modo de
   visualización y con qué escala.
6. Ajustes de los modos de visualización: los que controlan el relleno del corte
   (*Show fills*, *Use section styles*).
"""

import Rhino
import scriptcontext as sc

# NOTA ES: esto se imprime en la línea de comandos de Rhino, no en un archivo.
# El informe completo se arma en una lista y se devuelve al final, para poder
# mandarlo de vuelta por el puente MCP o copiarlo desde la línea de comandos.
LINEAS = []


def P(texto):
    # NOTA ES: P() es nuestra función de "imprimir". Envuelve el append para que
    # en el futuro se pueda cambiar el destino (archivo, log) en un solo lugar.
    LINEAS.append(str(texto))


def seguro(fn, defecto="n/d"):
    # NOTA ES: "seguro" ejecuta una función y, si falla (API distinta en esta
    # versión de Rhino), devuelve un texto con el error en vez de cortar el informe.
    try:
        return fn()
    except Exception as exc:
        return "%s (error: %s)" % (defecto, exc.__class__.__name__)


def volcar_interesante(objeto, palabras, titulo):
    # NOTA ES: volca los atributos cuyo nombre contiene alguna de las palabras
    # clave. Es más robusto que escribir nombre por nombre: la API de Rhino
    # cambia entre versiones y esto se adapta solo.
    P("   %s:" % titulo)
    try:
        nombres = [n for n in dir(objeto) if not n.startswith("_")]
    except Exception:
        P("      (no se pudo inspeccionar)")
        return
    for nombre in nombres:
        bajo = nombre.lower()
        if any(p in bajo for p in palabras):
            valor = seguro(lambda n=nombre: getattr(objeto, n))
            P("      %s = %s" % (nombre, valor))


def main():
    doc = sc.doc
    LINEAS[:] = []

    P("=" * 70)
    P("ARCHIVO      : %s" % doc.Path)
    P("UNIDADES     : modelo=%s | layout=%s" % (doc.ModelUnitSystem, doc.LayoutUnitSystem))
    P("OBJETOS      : %d" % doc.Objects.Count)
    P("CAPAS        : %d" % doc.Layers.Count)
    P("VISTAS       : %d" % doc.Views.Count)
    P("=" * 70)

    # ---------------------------------------------------------------- 1. PLANOS
    P("")
    P("--- 1. PLANOS DE CORTE ---------------------------------------------")
    n_planos = 0
    for obj in doc.Objects:
        if obj.ObjectType == Rhino.DocObjects.ObjectType.ClipPlane:
            n_planos += 1
            P("PLANO #%d  id=%s  nombre=%r  capa=%r"
              % (n_planos, obj.Id, obj.Attributes.Name, obj.Attributes.LayerName))
            geometria = seguro(lambda o=obj: o.Geometry)
            P("   geometria: %s" % geometria)
            volcar_interesante(
                obj,
                ["depth", "section", "label", "flip", "clip", "name", "plane", "view"],
                "propiedades del plano")
    if n_planos == 0:
        P("   (no hay planos de corte en el documento)")

    # ------------------------------------------------------------------ 2. CAPAS
    P("")
    P("--- 2. CAPAS (estilo de seccion = el relleno del corte) -------------")
    for i in range(doc.Layers.Count):
        capa = doc.Layers[i]
        P("CAPA %r  visible=%s  color_impr=%s  ancho=%s"
          % (capa.Name, capa.Visible, capa.PrintColor, seguro(lambda c=capa: c.PrintWidth)))
        volcar_interesante(capa, ["section", "style", "pattern"], "estilo de seccion")

    # ---------------------------------------------------------------- 3. OBJETOS
    P("")
    P("--- 3. OBJETOS POR TIPO (la seccion solo rellena si es cerrada) ------")
    por_tipo = {}
    cerrados = 0
    abiertos = 0
    for obj in doc.Objects:
        clave = str(obj.ObjectType)
        por_tipo[clave] = por_tipo.get(clave, 0) + 1
        if clave == "Polysurface" or clave == "Mesh" or clave == "Extrusion":
            estado = seguro(lambda o=obj: o.Geometry.IsClosed)
            if estado is True:
                cerrados += 1
            elif estado is False:
                abiertos += 1
    for clave in sorted(por_tipo):
        P("   %-28s %d" % (clave, por_tipo[clave]))
    P("   geometrias cerradas=%d  abiertas=%d" % (cerrados, abiertos))

    # ----------------------------------------------------------------- 4. VISTAS
    P("")
    P("--- 4. VISTAS Y DETALLES (la lamina y sus viewports) -----------------")
    for i in range(doc.Views.Count):
        vista = doc.Views[i]
        P("VISTA %d  nombre=%r  tipo=%s" % (i, vista.Name, seguro(lambda v=vista: v.Type)))
        detalles = seguro(lambda v=vista: v.Details, [])
        for det in detalles or []:
            P("   DETALLE  nombre=%r" % seguro(lambda d=det: d.Attributes.Name))
            P("      pagina      = %r" % seguro(lambda d=det: d.Attributes.PageName))
            P("      modo        = %s" % seguro(lambda d=det: d.Attributes.DisplayMode))
            P("      layer       = %r" % seguro(lambda d=det: d.Attributes.LayerName))
            volcar_interesante(det, ["scale", "camera", "target", "display"], "detalle")

    # ------------------------------------------- 5. AJUSTES DE LOS MODOS (V8)
    P("")
    P("--- 5. AJUSTES DE LOS MODOS DE VISUALIZACION -----------------------")
    P("   (aca vive 'Show fills' y 'Use section styles')")
    for etiqueta, contenedor in [
        ("RhinoApp.Settings", seguro(lambda: Rhino.RhinoApp.Settings)),
        ("RhinoApp", Rhino.RhinoApp),
    ]:
        if contenedor is None:
            continue
        P("   %s:" % etiqueta)
        try:
            nombres = [n for n in dir(contenedor) if not n.startswith("_")]
        except Exception:
            continue
        for nombre in nombres:
            if "display" in nombre.lower():
                valor = seguro(lambda n=nombre: getattr(contenedor, n))
                P("      %s = %s" % (nombre, valor))

    P("")
    P("=" * 70)
    return "\n".join(LINEAS)


INFORME = main()
print(INFORME)
