"""Carga las cards de los 2 planes del 19/10 en Leantime (proyecto 4 + proyecto nuevo del concurso).

Que hace:
  1) repara el sprint vacio 27 (creado por un probe) -> lo convierte en S1 del proyecto 4
  2) crea el sprint S1 del proyecto del concurso
  3) crea los milestones M-A1..M-A4 (proyecto 4) y M-B1..M-B6 (proyecto concurso)
  4) crea las cards con sus subtasks (upsertSubtask) y links a milestone + sprint
  5) deja el estado final en un JSON para asentar en el vault

Idempotente por headline: si la card ya existe en el proyecto, no la duplica.

Uso:
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/carga_leantime_planes_261019.py [--dry-run]
"""
import io
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from leantime_rpc import rpc, resultado  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "raw" / "reuniones" / "leantime-carga-261019-estado.json"

PROY_EMI = 4
USU_EMILIA = 5
USU_SOL = 1

# --- Estado de columnas LPS -> estados Leantime (ver getStatusLabels) ---
COL = {"backlog": 3, "make-ready": 3, "sprint": 3, "en-curso": 4,
       "revision": 2, "bloqueado": 1, "hecho": 0}
PRIORIDAD = {"critica": 1, "alta": 2, "media": 3, "baja": 4}


def card(codigo, headline, duenio, pom, milestone, columna, cierre, subtareas, source=""):
    """Arma una card del plan. subtareas = lista de (sufijo, texto, minutos)."""
    return {
        "codigo": codigo,
        "headline": headline,
        "duenio": duenio,
        "pom": pom,
        "milestone": milestone,
        "columna": columna,
        "cierre": cierre,
        "source": source,
        "subtareas": subtareas,
    }


def mil(milestone_id, nombre, proyecto, fecha, description=""):
    return {"id": milestone_id, "headline": nombre, "projectId": proyecto,
            "dateToFinish": fecha, "description": description}


# ---------------------------------------------------------------- PLAN AGENTES
MIL_A = [
    mil("M-A1", "M-A1 Curso entregado + chat compartido (20/10)", PROY_EMI, "2026-10-20",
        "Entrega del trabajo del curso con tasa pagada, solicitud de prórroga y link del chat compartido."),
    mil("M-A2", "M-A2 Agenda de Emilia viva (21/10)", PROY_EMI, "2026-10-21",
        "Bot respondiendo, cal.com de Emilia con su evento, Calendar de Emilia leída, chat_id en el Router "
        "y clones de agente + subflujo publicados. Go/No-Go: 1 reserva real desde el chat de Emilia."),
    mil("M-A3", "M-A3 Metodo de catalogacion + biblioteca (22/10)", PROY_EMI, "2026-10-22",
        "Método escrito por Emilia, copia de la biblioteca en su Drive, Sheet compartido y 1 libro procesado."),
    mil("M-A4", "M-A4 Modelos Comfy + agente semanal (23/10)", PROY_EMI, "2026-10-23",
        "3 modelos comparados con luz cálida + preset + agente semanal con botones funcionando."),
]

PLAN_A = [
    card("A1", "Entregar trabajo del curso + compartir chat", "emilia", 5, "M-A1", "sprint",
         "Plataforma con la entrega + tasa pagada + solicitud de prorroga escrita + link del chat compartido con Sol.",
         [("A1.1", "Cerrar el topico 5 (imagenes + escritura)", 25),
          ("A1.2", "Escribir la conclusion", 25),
          ("A1.3", "Regenerar el PDF y subirlo a la plataforma", 25),
          ("A1.4", "Pagar la tasa y escribir la solicitud de prorroga con el motivo", 25),
          ("A1.5", "Compartir el link del chat con Sol", 10)],
         "reunion 16/10 20:33, resumen ts 1292 / transcripcion 00:22:45"),
    card("A2", "Listado de referencias consolidado", "emilia", 2, "M-A1", "sprint",
         "Listado unico pegado + cotejo firmado de que no falta ninguna fuente.",
         [("A2.1", "Pedir a la IA el listado unificado sin perder ninguna referencia", 10),
          ("A2.2", "Chequear que esten todas las citas leidas", 15)],
         "reunion 16/10 20:33, transcripcion 00:39:00-00:39:24"),
    card("B1", "Activar bot OS.emi-pi con mensaje", "emilia", 1, "M-A2", "sprint",
         "El bot responde con el menu de comandos y el chat_id de Emilia queda visible para Sol.",
         [("B1.1", "Mensaje al bot y lectura de la respuesta", 5)],
         "reunion 16/10 20:33, resumen ts 1487 / transcripcion 00:25:20"),
    card("B2", "Credencial de Google Calendar de Emilia", "ambos", 1, "M-A2", "make-ready",
         "El agente de agenda lee el calendario de Emilia y devuelve un slot real.",
         [("B2.1", "Emilia autoriza Google Calendar desde la UI de n8n (OAuth2 -> Connect)", 20),
          ("B2.2", "Sol la pega en la tool leer_calendario del agente de agenda", 5)],
         "reunion 16/10 20:33, transcripcion 00:32:05"),
    card("B3", "Copia de biblioteca de revistas en su Drive", "emilia", 1, "M-A3", "sprint",
         "Emilia tiene copia propia y deja de depender del acceso de un tercero.",
         [("B3.1", "Duplicar la carpeta compartida y verificar acceso completo", 25)],
         "reunion 16/10 20:33, transcripcion 00:39:12"),
    card("B4", "Catalogo + publicacion de fotos de obras", "emilia", 4, "M-A3", "sprint",
         "Catalogo de 30 fotos con metadata + 1 publicacion hecha.",
         [("B4.1", "Elegir 30 fotos (criterio: material propio, sin derechos de terceros)", 25),
          ("B4.2", "Catalogarlas con tema + lugar + anio", 50),
          ("B4.3", "Escribir el pie de foto de la primera tanda", 25),
          ("B4.4", "Publicar una tanda", 25)],
         "reunion 16/10 20:33, transcripcion 00:44:40-00:45:00"),
    card("B5", "3 modelos Comfy con luz calida", "ambos", 4, "M-A4", "sprint",
         "3 comparaciones documentadas + preset guardado con luz calida.",
         [("B5.1", "Listar los modelos disponibles y sus estilos", 25),
          ("B5.2", "Probar 3 modelos sobre el mismo croquis y comparar", 50),
          ("B5.3", "Guardar el prompt + modelo ganador como preset", 25),
          ("B5.4", "Escribir una nota de 5 lineas con el criterio de luz elegido", 25)],
         "reunion 16/10 20:33, transcripcion 00:56:50-00:58:38"),
    card("B6", "Metodo de catalogacion acordado", "ambos", 2, "M-A3", "sprint",
         "Metodo de una carilla, con la diferencia contra la Sheet anotada para el siguiente ajuste.",
         [("B6.1", "Emilia escribe que campos quiere ver en cada fuente", 25),
          ("B6.2", "Definir la regla de seleccion (si / no / revisar) y su vocabulario de tags", 25),
          ("B6.3", "Contrastar con las columnas vivas del Sheet Fuentes-Inbox", 25)],
         "reunion 16/10 20:33, transcripcion 00:08:07 y 00:43:00"),
    card("B7", "Stack de trabajo en el PC de Emilia", "ambos", 4, "M-A2", "make-ready",
         "La cita del miercoles cierra con Emilia operando sobre su propio vault.",
         [("B7.1", "Actualizar Obsidian + git pull del vault", 25),
          ("B7.2", "Conectar su ChatGPT al sistema", 25),
          ("B7.3", "codex mcp list con Fathom visible", 25),
          ("B7.4", "1 ficha del vault alimentada por ella con verificacion de Sol", 25)],
         "reunion 16/10 20:33, transcripcion 00:42:21"),
    card("C1", "Conectar cal.com de Emilia", "sol", 3, "M-A2", "sprint",
         "1 reserva real a nombre de Emilia, con Meet en el mail.",
         [("C1.1", "Cargar la API key de la cuenta de Emilia", 25),
          ("C1.2", "Crear su eventType propio con durations 30/60/120 min", 25),
          ("C1.3", "Prueba de booking real + link de Meet", 25)],
         "reunion 16/10 20:33, resumen ts 1831 / transcripcion 00:30:31"),
    card("C1b", "Clonar agente + subflujo de agenda con perfil Emilia", "sol", 5, "M-A2", "sprint",
         "Los 2 clones activos con perfil Emilia + 1 reserva real creada desde el chat de Emilia.",
         [("C1b.1", "Clonar Agenda Sub TEST -> Agenda Sub Emilia y cambiar credenciales + leer_calendario", 50),
          ("C1b.2", "Clonar Agent Voz TEST -> Agent Voz Emilia y cambiar allowlist, Redis, Postgres, prompt y Tool Agenda", 50),
          ("C1b.3", "Agregar la rama de Emilia en Route Identidad del Router con su chat_id", 25),
          ("C1b.4", "Publicar los 3 workflows y correr las 10 pruebas de aceptacion", 25)],
         "guion config-agente-agenda-emilia.md (19/10)"),
    card("C2", "Cargar chat_id de Emilia en el Router", "sol", 1, "M-A2", "sprint",
         "1 link enviado por Emilia aparece en el Sheet con De = emi.",
         [("C2.1", "Leer el chat_id desde la ejecucion del trigger y pegarlo en el nodo de identidad", 25)],
         "reunion 16/10 20:33, transcripcion 00:06:38"),
    card("C3", "Calendario que lee el agente + evento 60 min", "sol", 3, "M-A2", "make-ready",
         "El agente devuelve slots de los calendarios correctos y Emilia ya no cae en el fallback de comandos.",
         [("C3.1", "Definir el calendario de trabajo de Emilia (profesional / personal)", 25),
          ("C3.2", "Ajustar el evento 60 min con Meet", 25),
          ("C3.3", "Verificar que el filtro por chat_id deja pasar a Emilia", 25)],
         "reunion 16/10 20:33, transcripcion 00:31:00-00:34:14"),
    card("C4", "Compartir Sheet + mover a OS-Emilia/", "sol", 1, "M-A3", "backlog",
         "Emilia abre la hoja desde el celu y ve sus filas.",
         [("C4.1", "Compartir la hoja con el mail de Emilia + moverla a la carpeta OS-Emilia/", 25)],
         "reunion 16/10 20:33, transcripcion 00:06:05"),
    card("C5", "Sistema de procesamiento de libros", "ambos", 4, "M-A3", "backlog",
         "1 libro procesado de punta a punta con su ficha y su crudo.",
         [("C5.1", "Separar el tema en su propia carpeta (misma logica que el sistema de Telegram)", 25),
          ("C5.2", "Definir la ficha por libro (titulo, tema, indice/glosario, tapa)", 50),
          ("C5.3", "Definir el pipeline (entrada -> crudo -> Obsidian -> wiki)", 50),
          ("C5.4", "Probar con 1 libro y 1 revista", 25)],
         "reunion 16/10 20:33, transcripcion 00:50:42"),
    card("C6", "Prueba con textos sin imagenes", "sol", 2, "M-A3", "backlog",
         "El pipeline rinde con material sin imagenes y el tiempo de revision queda anotado.",
         [("C6.1", "Corrida con 1 revista escaneada sin imagenes", 25),
          ("C6.2", "Medir cuanto se automatiza vs. lo que queda curaduria", 25)],
         "reunion 16/10 20:33, transcripcion 00:39:30"),
    card("C7", "Canal de avisos al cliente (decision)", "sol", 1, "M-A3", "backlog",
         "1 parrafo con el canal elegido y su costo mensual estimado.",
         [("C7.1", "Comparar Telegram propio vs. WhatsApp Business (costo de mensajes salientes)", 25)],
         "reunion 16/10 20:33, transcripcion 00:36:05"),
    card("C8", "Cerrar el agente semanal de arquitectura", "sol", 3, "M-A4", "backlog",
         "El lunes Emilia recibe el reporte con sus 2 botones funcionando.",
         [("C8.1", "Cerrar el informe semanal con el boton de quedarse/rechazar por tema", 50),
          ("C8.2", "Verificar el worker que toma la imagen y la publica", 25),
          ("C8.3", "Documentarlo en el playbook", 25)],
         "reunion 16/10 20:33, transcripcion 00:14:19"),
    card("D1", "Llamada corta lunes 19/10", "ambos", 1, "M-A1", "sprint",
         "Fecha de entrega anotada en el plan y en Leantime.",
         [("D1.1", "Confirmar la fecha real de entrega del curso", 25)],
         "reunion 16/10 20:33, transcripcion 00:59:20"),
    card("D2", "Cita presencial miercoles 21/10 13:00", "ambos", 3, "M-A2", "sprint",
         "Agenda viva con los dos calendarios + lista de lo que sigue con duenio y fecha.",
         [("D2.1", "Ejecutar B2 (credencial de Calendar)", 25),
          ("D2.2", "Ejecutar C1b (clones de agente + subflujo con perfil Emilia)", 75),
          ("D2.3", "Revisar que queda abierto del bot de agenda y de la biblioteca", 25)],
         "reunion 16/10 20:33, resumen ts 3543 / guion 19/10"),
]

# ---------------------------------------------------------------- PLAN CONCURSO
MIL_B = [
    mil("M-B1", "M-B1 Inscripcion pagada y registrada (19/10)", 0, "2026-10-19",
        "Sol + Emilia inscriptos. Cerrado el 19/10."),
    mil("M-B2", "M-B2 Bases -> checklist de entregables (20/10)", 0, "2026-10-20",
        "2 problemas formulados + requisitos tecnicos leidos + lista con responsable y fecha."),
    mil("M-B3", "M-B3 Flujo Rhino + ComfyUI con estilo propio (22/10)", 0, "2026-10-22",
        "1 entrega con sello propio reproducible + reglas de trabajo escritas."),
    mil("M-B4", "M-B4 Entrega protegida documentada (23/10)", 0, "2026-10-23",
        "1 PDF convertido en imagen plana no ampliable + ficha del procedimiento."),
    mil("M-B5", "M-B5 Nota de honorarios por propiedad intelectual (23/10)", 0, "2026-10-23",
        "3 opciones de cobro + criterio de escasez + insumo compartido con Emilia y Kiki."),
    mil("M-B6", "M-B6 Entrega del concurso (16/12/2026)", 0, "2026-12-16",
        "Entregables del concurso cerrados y archivos subidos a la plataforma."),
]

PLAN_B = [
    card("E1", "Inscribirse en el concurso con los datos de los dos", "emilia", 3, "M-B1", "sprint",
         "CERRADO 19/10: ya inscriptos Sol + Emilia. Falta guardar el comprobante y volcar los plazos a la agenda.",
         [("E1.1", "Leer la convocatoria y confirmar que datos pide por persona", 25),
          ("E1.2", "Completar la inscripcion con el nombre de Sol y un mail accesible por el", 25),
          ("E1.3", "Guardar el comprobante y volcar los plazos a la agenda", 15)],
         "reunion 16/10 19:31, resumen ts 792 / transcripcion 00:55:47"),
    card("E2", "Enviar el TCC a Sol para lectura", "emilia", 1, "M-B1", "make-ready",
         "Sol tiene el material para leer.",
         [("E2.1", "Mandar el articulo con el listado de referencias por topico", 25)],
         "reunion 16/10 19:31, transcripcion 00:32:40"),
    card("E3", "Conversar con Kiki sobre reparto de honorarios por etapas", "emilia", 2, "M-B5", "backlog",
         "Criterio de reparto por etapas anotado por escrito y compartido con Sol.",
         [("E3.1", "Preparar el planteo: que etapa vale que y por que el proyecto no puede seguir pesando 40%", 25),
          ("E3.2", "Reunion de trabajo con Kiki y registro del criterio acordado", 25)],
         "reunion 16/10 19:31, transcripcion 00:20:16"),
    card("E4", "Fijar el criterio de estilo de la entrega", "ambos", 1, "M-B3", "sprint",
         "Regla escrita que se puede pasar a cualquier entrega.",
         [("E4.1", "Anotar la regla: croquis + variacion leve de perspectiva, sin render realista", 25)],
         "reunion 16/10 19:31, transcripcion 00:52:31"),
    card("F1", "Pagar la inscripcion y pasar links de la convocatoria", "sol", 2, "M-B1", "sprint",
         "CERRADO 19/10: inscripcion hecha. Falta reenviar links y comprobante a Emilia.",
         [("F1.1", "Pagar la inscripcion con la tarjeta", 25),
          ("F1.2", "Reenviar los links y el comprobante a Emilia", 15)],
         "reunion 16/10 19:31, transcripcion 00:55:33"),
    card("F2", "Traducir las bases a una lista de tareas para Emilia", "sol", 2, "M-B2", "sprint",
         "Checklist de entregables enviada, con responsable y fecha por item.",
         [("F2.1", "Volcar los requisitos del concurso como checklist con responsable", 25),
          ("F2.2", "Enviar la lista y acordar en la llamada del lunes que falta", 20)],
         "reunion 16/10 19:31, resumen ts 3543 / transcripcion 00:12:33"),
    card("F3", "Procedimiento de entrega protegida (PDF -> imagen)", "sol", 4, "M-B4", "make-ready",
         "1 PDF convertido en imagen plana no ampliable + ficha con el procedimiento.",
         [("F3.1", "Definir los criterios de la imagen entregable (formato, pixeles, que se ve y que no)", 25),
          ("F3.2", "Construir el paso a paso local (sin subir el plano a un conversor online)", 50),
          ("F3.3", "Probarlo con 1 plano real del estudio", 25),
          ("F3.4", "Documentarlo como ficha de estudio", 25)],
         "reunion 16/10 19:31, transcripcion 00:26:32"),
    card("F4", "Nota de honorarios por PI + tokenizacion de disenos", "sol", 5, "M-B5", "backlog",
         "Nota de 1-2 carillas con 3 opciones y una recomendacion.",
         [("F4.1", "Relevar como se cobran hoy y donde se rompe el modelo por m2", 50),
          ("F4.2", "Modelar la licencia limitada (ej. 10 usos unicos) como unidad de valor", 50),
          ("F4.3", "Contrastar con el marco que ya estudia el socio (tokenizacion)", 25),
          ("F4.4", "Escribir la nota con 3 opciones de cobro y su dificultad de aplicacion", 25),
          ("F4.5", "Compartir la nota con Emilia y Kiki como insumo de E3", 15)],
         "reunion 16/10 19:31, transcripcion 00:56:00"),
    card("F5", "Flujo Rhino + ComfyUI con estilo propio", "ambos", 4, "M-B3", "make-ready",
         "1 entrega con sello propio, reproducible desde los presets.",
         [("F5.1", "Definir el encadenamiento Rhino -> viewport ComfyUI -> imagen y video", 25),
          ("F5.2", "Probar el flujo sobre un caso real del estudio", 50),
          ("F5.3", "Aplicar el criterio de estilo propio y descartar el look IA notoria", 25),
          ("F5.4", "Guardar los parametros como preset reutilizable", 25)],
         "reunion 16/10 19:31, transcripcion 00:43:07"),
    card("F8", "Dejar el flujo documentado para el que venga despues", "sol", 2, "M-B3", "backlog",
         "Documento de reglas + crudo accesible.",
         [("F8.1", "Escribir la secuencia de trabajo como reglas (que va antes, que se revisa, que se entrega)", 50),
          ("F8.2", "Dejar el crudo y los links de referencia accesibles", 25)],
         "reunion 16/10 19:31, transcripcion 00:48:51"),
    card("G1", "Definir los 2 problemas que la propuesta debe resolver", "ambos", 2, "M-B2", "sprint",
         "2 enunciados de problema escritos, con el requisito de no tapar la Sagrada Familia.",
         [("G1.1", "Formular el problema del exceso de turismo en la plaza", 25),
          ("G1.2", "Formular el problema del desplazamiento de los vecinos y el vinculo entre ambos mundos", 25)],
         "reunion 16/10 19:31, resumen ts 300 / transcripcion 00:05:00"),
    card("G2", "Repasar las bases y fijar la lista de entregables", "ambos", 2, "M-B2", "sprint",
         "La lista de entregables de F2 queda cerrada con Emilia.",
         [("G2.1", "Leer juntos los requisitos tecnicos (texto->imagen, edicion, video, 3D, modelo IA)", 25),
          ("G2.2", "Marcar el modelo de IA de la Fundacion: que acceso exige y que se entrega", 25)],
         "reunion 16/10 19:31, transcripcion 00:12:33"),
    card("G3", "Jornada de trabajo del concurso los domingos", "ambos", 4, "M-B3", "backlog",
         "1 jornada hecha con entregable por sesion, registrada en raw/sessions.",
         [("G3.1", "Cerrar la agenda del domingo con el entregable del dia", 25),
          ("G3.2", "Preparar el material de arranque de la jornada", 25),
          ("G3.3", "Guardar el avance en el vault al cerrar cada jornada", 25)],
         "reunion 16/10 19:31, transcripcion 00:13:17"),
]


def _existing(proyecto: int) -> dict:
    """headline -> id de las cards ya cargadas en un proyecto."""
    mapa = {}
    for t in resultado("leantime.rpc.Tickets.Tickets.getAll") or []:
        if t.get("projectId") == proyecto and t.get("type") == "task":
            mapa.setdefault(t["headline"], t["id"])
    return mapa


def _id(salida) -> int:
    """La API devuelve el id como array de 1 elemento ([458])."""
    r = salida.get("result")
    if isinstance(r, list) and r:
        return int(r[0])
    if isinstance(r, int):
        return r
    return 0


def _crear_milestone(m, proyecto: int, fecha: str) -> int:
    """Crea un milestone y devuelve su id."""
    salida = rpc("leantime.rpc.Tickets.Tickets.quickAddMilestone", {
        "params": {
            "headline": m["headline"],
            "projectId": proyecto,
            "priority": 3,
            "status": 3,
            "dateToFinish": m["dateToFinish"],
            "description": m["description"],
            "tags": "",
        }})
    mid = _id(salida)
    if not mid:
        print("   ERROR milestone", m["headline"], "->", json.dumps(salida)[:200])
    return mid


def _crear_card(c, proyecto: int, milestone_id: int, sprint_id: int, duenio_id: int,
                colaboradores: list, fecha: str) -> int:
    """Crea la card y sus subtasks. Devuelve el id de la card (0 si falla)."""
    descripcion = (f"Origen: {c['source']}\n"
                   f"Cierre: {c['cierre']}\n"
                   f"Plan: {c['pom']} pomodoros (25 min) | duenio: {c['duenio']}")
    salida = rpc("leantime.rpc.Tickets.Tickets.addTicket", {
        "values": {
            "headline": c["headline"],
            "type": "task",
            "description": descripcion,
            "projectId": proyecto,
            "milestoneid": milestone_id,
            "sprint": sprint_id,
            "status": COL[c["columna"]],
            "priority": PRIORIDAD["media"],
            "planHours": round(c["pom"] * 0.42, 2),
            "hourRemaining": round(c["pom"] * 0.42, 2),
            "dateToFinish": fecha,
            "editorId": duenio_id,
            "collaborators": colaboradores,
            "acceptanceCriteria": c["cierre"],
        }})
    card_id = _id(salida)
    if not card_id:
        print("   ERROR card", c["headline"], "->", json.dumps(salida)[:250])
        return 0
    for sufijo, texto, minutos in c["subtareas"]:
        sub = rpc("leantime.rpc.Tickets.Tickets.addTicket", {
            "values": {
                "headline": f"{sufijo} {texto}",
                "type": "subtask",
                "description": f"{minutos} min | cierre: {c['cierre']}",
                "projectId": proyecto,
                "milestoneid": milestone_id,
                "sprint": sprint_id,
                "status": COL[c["columna"]],
                "priority": PRIORIDAD["media"],
                "planHours": round(minutos / 60, 2),
                "hourRemaining": round(minutos / 60, 2),
                "dateToFinish": fecha,
                "editorId": duenio_id,
                "dependingTicketId": card_id,
                "acceptanceCriteria": texto,
            }})
        if not _id(sub):
            print("   ERROR subtask", sufijo, "->", json.dumps(sub)[:200])
    return card_id


def main() -> None:
    dry = "--dry-run" in sys.argv
    estado = {"sprints": {}, "proyectos": {}, "milestones": {}, "cards": {}, "subtasks": 0}

    # 1) sprint 27 (vacio, del probe) -> S1 del proyecto 4
    if not dry:
        r = rpc("leantime.rpc.Sprints.Sprints.editSprint", {"params": {
            "id": 27, "name": "S1 Agentes + agenda Emilia (19/10-23/10)",
            "projectId": PROY_EMI, "startDate": "2026-10-19", "endDate": "2026-10-23"}})
        estado["sprints"]["S1-plan-A"] = {"id": 27, "respuesta": r.get("result", r)}
        time.sleep(1.5)
    else:
        estado["sprints"]["S1-plan-A"] = {"id": 27, "respuesta": "dry-run"}

    # 2) proyecto del concurso
    if dry:
        proy_conc = 0
    else:
        r = rpc("leantime.rpc.Projects.Projects.addProject", {"values": {
            "name": "Proyecto Pi - Concurso Gaudi Nexus",
            "details": "Carril propio del estudio: concurso Gaudi Nexus (mercado + centro cultural cerca de la Sagrada Familia). Entrega 16/12/2026. Fuera del contrato Studio OS x Emilia: las horas se registran aparte.",
            "clientId": 1, "type": "project", "psettings": "restricted",
            "assignedUsers": [{"id": USU_EMILIA, "projectRole": ""}, {"id": USU_SOL, "projectRole": ""}]}})
        proy_conc = _id(r)
        if not proy_conc:
            print("ERROR proyecto concurso:", json.dumps(r)[:250])
    estado["proyectos"]["concurso"] = {"id": proy_conc, "nombre": "Proyecto Pi - Concurso Gaudi Nexus"}

    # 3) sprint del concurso
    if not dry and proy_conc:
        r = rpc("leantime.rpc.Sprints.Sprints.addSprint", {"params": {
            "name": "S1 Bases + primer flujo (19/10-23/10)",
            "projectId": proy_conc, "startDate": "2026-10-19", "endDate": "2026-10-23"}})
        sprint_b = _id(r)
        estado["sprints"]["S1-plan-B"] = {"id": sprint_b, "respuesta": r.get("result", r)}
        time.sleep(1.5)
    else:
        sprint_b = 0
        estado["sprints"]["S1-plan-B"] = {"id": 0, "respuesta": "dry-run"}

    # 4) milestones + 5) cards
    for etiqueta, plan, milestones, proyecto, sprint_id in [
        ("A", PLAN_A, MIL_A, PROY_EMI, 27),
        ("B", PLAN_B, MIL_B, proy_conc, sprint_b),
    ]:
        ms_ids = {}
        for m in milestones:
            if dry or not proyecto:
                ms_ids[m["id"]] = 0
                continue
            mid = _crear_milestone(m, proyecto, m["dateToFinish"])
            ms_ids[m["id"]] = mid
            estado["milestones"][m["id"]] = {"id": mid, "projectId": proyecto}
            time.sleep(1.5)
        ya = _existing(proyecto) if (proyecto and not dry) else {}
        for c in plan:
            if c["headline"] in ya:
                estado["cards"][c["codigo"]] = {"id": ya[c["headline"]], "headline": c["headline"],
                                              "projectId": proyecto, "existia": True}
                continue
            duenio = USU_EMILIA if c["duenio"] == "emilia" else USU_SOL
            colabs = [USU_SOL, USU_EMILIA] if c["duenio"] == "ambos" else []
            mid = ms_ids.get(c["milestone"], 0)
            fecha = milestones[[m["id"] for m in milestones].index(c["milestone"])]["dateToFinish"] if c["milestone"] in ms_ids else "2026-10-23"
            if dry or not proyecto:
                estado["cards"][c["codigo"]] = {"id": 0, "headline": c["headline"], "dry": True}
                continue
            cid = _crear_card(c, proyecto, mid, sprint_id, duenio, colabs, fecha)
            estado["cards"][c["codigo"]] = {"id": cid, "headline": c["headline"],
                                            "projectId": proyecto, "milestone": c["milestone"],
                                            "duenio": c["duenio"], "pom": c["pom"]}
            estado["subtasks"] += len(c["subtareas"])
            time.sleep(1.5)

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"proyecto_concurso": proy_conc,
                      "cards": len(estado["cards"]),
                      "milestones": len([m for m in estado["milestones"].values() if m["id"]]),
                      "subtasks": estado["subtasks"],
                      "estado": str(SALIDA)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
