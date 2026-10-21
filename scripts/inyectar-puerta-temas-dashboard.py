"""Inyecta en el dashboard general la seccion 'la puerta': los 6 temas del estudio
y donde esta cada cosa (para ver desde un solo archivo).

Por que un script y no editar el HTML a mano: el dashboard se regenera con
scripts/build-dashboard-semanas.py, asi que la puerta tiene que poder
reinyectarse sola y sin duplicar nada. El bloque va entre marcadores y se
borra antes de escribir => correrlo dos veces deja el HTML igual.

Uso:
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/inyectar-puerta-temas-dashboard.py --dry
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/inyectar-puerta-temas-dashboard.py
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRES = os.path.join(BASE, "proyectos", "STUDIO_OS-Emilia", "presentacion")
DASH = os.path.join(PRES, "dashboard-mes1-emilia.html")

INI = "<!-- PUERTA-TEMAS -->"
FIN = "<!-- /PUERTA-TEMAS -->"

# --------------------------------------------------------------------- datos
# (tema, estado en una linea, [rutas del vault], dashboard enlazado)
TEMAS = [
    ("Fuentes · AIxGaudi",
     "31 PDF -> 32 fichas + 31 transcripciones. Gate 0 listo; faltan los gates 1-3 (sherlock, contenidos, wiki).",
     ["raw/pdf/00-index.md",
      "specs/261020-plan-procesado-fuentes-pdf-gaudi.md",
      "proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md"],
     "dashboard-vault.html"),
    ("Agentes Telegram",
     "El bot con dos flujos (Sol y Emilia) + despachador por chat_id. Probado end-to-end.",
     ["specs/261019-plan-agentes-telegram-agenda-emilia.md",
      "proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21.md",
      "proyectos/STUDIO_OS-Emilia/documentacion/que-le-pedimos-a-emilia-2026-10-21.md",
      "proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia.md"],
     "dashboard-estudio-os.html"),
    ("CAD / SET",
     "SET_01 replanteado con 2 playbooks, SET_02 y SET_03 especificados, dashboard v2 al dia.",
     ["proyectos/MVP_02-autocad-standards/03-log-mvp_02.md",
      "proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-01-SET-informe.md",
      "proyectos/STUDIO_OS-Emilia/presentacion/07-revision-autocad-2026-10-22.md"],
     "dashboard-autocad.html"),
    ("Comfy",
     "6 workflows (F-01..F-06) + LoRA rhino-to-image (FLUX.2 klein 9B) + 3 modelos con luz calida.",
     ["proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.md",
      "proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/03-nodos-WFrhino_to_image.md",
      "proyectos/MVP_04.02-comfyui-arquitectura/PLANS/PLAN-F1-F8-lora-inpaint-outpaint.md"],
     "dashboard-comfy.html"),
    ("Leantime",
     "2 planes cargados (33 cards, 85 subtasks) + 15 h registradas. Item 589: corpus -> ChatGPT.",
     ["wiki/glosario/software/leantime.md",
      "scripts/leantime_registrar_horas.py",
      "raw/reuniones/leantime-carga-261019-estado.json"],
     None),
    ("Estudio · comercial",
     "1.800 por trimestre, 60 h por mes. Propuesta del viernes y propuesta del mes 2 (CAD urbano).",
     ["proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes.md",
      "proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano.md",
      "proyectos/STUDIO_OS-Emilia/00-index.md"],
     None),
]

PENDIENTES = [
    ("1. chat_id de Emilia", "placeholder 999999999 en 2 lugares: Router (regla 2, rightValue) y "
     "Detectar Entrada Emilia (PERMITIDO). Se lee de la ejecucion cuando ella mande un mensaje. Despues: publicar."),
    ("2. Direccion del estudio", "Cal.com, event type 7563141 (presencial) -> Location -> Address. "
     "El bot la hereda del evento: se actualiza en un solo lugar."),
    ("3. Calendario de Emilia", "que lo comparta con proyectopi.31416@gmail.com -> leer_calendario deja de dar error."),
]


def tarjeta(tema, estado, rutas, dash):
    """Una tarjeta: el tema, el estado y las rutas del vault (como texto, no links)."""
    interior = (f'<div class="k">{tema}</div><h3>{estado}</h3>'
                + "<p>" + "<br>".join(f"<code>{r}</code>" for r in rutas) + "</p>")
    if dash:
        return (f'<a class="card" href="{dash}">{interior}'
                f'<p style="margin-top:8px"><b>&rarr; abrir el dashboard de {tema.split(" ")[0].lower()}</b></p></a>')
    return f'<div class="card">{interior}</div>'


def seccion():
    """Arma el HTML de la seccion completa."""
    filas = "".join(tarjeta(*t) for t in TEMAS)
    pend = "".join(
        f'<div class="card"><div class="k">{t}</div><p>{d}</p></div>' for t, d in PENDIENTES)
    return (
        f'{INI}\n'
        '<div class="k" style="margin-top:26px">La puerta: 6 temas, donde esta cada cosa</div>\n'
        '<h2 id="temas">Todo el estudio <em>desde un solo archivo.</em></h2>\n'
        '<p class="lead">Las rutas de abajo son del <b>vault</b> (se abren en Obsidian, no aqui). '
        'Los dashboards son HTML autocontenidos y viajan con el repo. '
        'El detalle por tema (sesiones trabajadas, .md creados y dashboards) esta en '
        '<code>proyectos/STUDIO_OS-Emilia/presentacion/09-agenda-reunion-2026-10-21.md</code>.</p>\n'
        f'<div class="grid g3" style="margin-top:12px">{filas}</div>\n'
        '<div class="k" style="margin-top:26px">Antes de la reunion (13:00) — 3 pendientes</div>\n'
        f'<div class="grid g3" style="margin-top:8px">{pend}</div>\n'
        f'{FIN}\n')


def main():
    dry = "--dry" in sys.argv
    with io.open(DASH, encoding="utf-8", errors="replace") as f:
        d = f.read()
    antes = len(d)

    # 1) (re)inyectar el bloque de la puerta: primero se borra el anterior
    d = re.sub(re.escape(INI) + r".*?" + re.escape(FIN) + r"\n?", "", d, flags=re.S)
    ancla = '<div class="k" style="margin-top:26px">Eficiencia = Resultados / Recursos</div>'
    assert ancla in d, "no encontre el ancla de insercion"
    d = d.replace(ancla, seccion() + ancla, 1)

    # 2) pestana en el nav (idempotente)
    if 'href="#temas"' not in d:
        d = d.replace('<a href="#sesiones">Sesiones</a>',
                      '<a href="#temas">Temas</a>\n<a href="#sesiones">Sesiones</a>', 1)

    # 3) la ruta del doc de la reunion en los toplinks (idempotente).
    #    Se mira SOLO el bloque toplinks: la ruta tambien aparece dentro de la
    #    seccion de la puerta, y con un "if ruta not in d" la comprobacion
    #    daria falso positivo y nunca se agregaria.
    m = re.search(r'(<p class="toplinks">)(.*?)(</p>)', d, re.S)
    if m and "09-agenda-reunion-2026-10-21.md" not in m.group(2):
        d = (d[:m.start(2)] + m.group(2)
             + " · <code>09-agenda-reunion-2026-10-21.md</code>" + d[m.end(2):])

    if dry:
        print("[dry] el HTML cambiaria: %d -> %d bytes" % (antes, len(d)))
        print("[dry] seccion de la puerta: %d bytes" % len(seccion()))
        return
    with io.open(DASH, "w", encoding="utf-8") as f:
        f.write(d)
    print("OK puerta inyectada: %d -> %d bytes" % (antes, len(d)))


if __name__ == "__main__":
    main()
