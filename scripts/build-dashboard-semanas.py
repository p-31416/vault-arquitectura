"""Seccion semanal (4 semanas fijadas por Sol) + despliegue IA. Inyecta en dashboard-mes1-emilia.html. Solo stdlib."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SES = os.path.join(BASE, "raw", "sessions")
DASH = os.path.join(BASE, "proyectos", "STUDIO_OS-Emilia", "presentacion",
                    "dashboard-mes1-emilia.html")

# (id, rango, horas Sol, archivos a repartir proporcional por tamano)
SEMANAS = [
    ("S0", "pre 11/09 (propuesta, fuera de vigencia)", 2.0, []),
    ("S1", "16-22/09 · M1 Vault vivo", 10.5,
     ["2026-09-16-sesion-emilia-playbook-portable"]),
    ("S2", "23-29/09 · M2 (topada a 20 por Sol)", 20.0,
     ["2026-09-24-sesion-cierre-contrato-emilia",
      "2026-09-24-sesion-n8n-mcp-instalacion",
      "2026-09-24-sesion-plan-os-emilia-n8n",
      "2026-09-27-mvp_02-fuentes",
      "2026-09-27-sesion-autodesk-help-mcp",
      "2026-09-27-sesion-fix-indices-wiki",
      "2026-09-28-sesion-alta-emilia-leantime",
      "2026-09-28-sesion-fuentes-wikilinks",
      "2026-09-28-sesion-revision-specs-pendientes"]),
    ("S3", "30/09-06/10 · M3 (fijada 12 por Sol)", 12.0,
     ["2026-09-30-sesion-mcp-7pasos-bloques-nl",
      "2026-09-30-sesion-moodboard-hormigon-madera-v5",
      "2026-10-05-sesion-fix-mcp-leantime",
      "2026-10-05-sesion-remotion-videos",
      "2026-10-05-sesion-set02-gest-dgiur-uso"]),
    ("S4", "07-16/10 · M4+cierre (22hs: 08-09/10 11hs + hoy 8hs + reunion manana 3hs)", 22.0,
     ["2026-10-08-sesion-comfyui-plan-tests-bat-fix",
      "2026-10-08-sesion-curacion-youtube",
      "2026-10-08-sesion-handy-dictado",
      "2026-10-08-sesion-n8n-fathom-agenda",
      "2026-10-08-sesion-wf01-corridas-ipadapter",
      "2026-10-09-sesion-alta-emilia-leantime",
      "2026-10-09-sesion-fuentes-agentes-grafo",
      "2026-10-09-sesion-reporte-semanal-08-09",
      "2026-10-09-sesion-sherlock-chipperfield-ching-canvas",
      "2026-10-09-sesion-vista-grafica-yt",
      "2026-10-09-sesion-wf03-serie-controles",
      "2026-10-13-sesion-baudrillard-pdf-pipeline",
      "2026-10-13-sesion-cierre-mes1-emilia",
      "2026-10-13-sesion-codex-inbox-emilia",
      "2026-10-13-sesion-comfyui-demo-manana",
      "2026-10-13-sesion-mvp06-agente-voz",
      "2026-10-13-sesion-set01-replanteo"]),
]
# Reuniones Emilia medidas por semana: (n_fathom, hs_fathom, presenciales_hs)
REUN = {"S0": (4, 0.0, 0.0), "S1": (4, 3.4, 3.0), "S2": (6, 5.2, 0.0),
        "S3": (2, 1.9, 3.0), "S4": (3, 3.0, 0.0)}

DESPLIEGUE = [
    ("Fathom grabando en las 13 reuniones", "13.5h maquina en paralelo al humano", "API + transcripts"),
    ("n8n cron 07:00 diario + 20 execs", "corre dormido, filtro 26h sin duplicados", "execs 3489-3525"),
    ("Comfy renderizando mientras trabajas (08-09/10)", "~25 min (F-01..F-05 + WF-03) en paralelo a YT/n8n", "sesiones 08/10"),
    ("Descargas desatendidas", "IP-Adapter + CLIP + Parakeet (~30-60 min red, 0 humano)", "08/10"),
    ("YouTube API + registro nocturno", "709 videos en segundos · notas 00:12/01:16 = sistema 24h", "08/10"),
]


def chars(name):
    with open(os.path.join(SES, name + ".md"), encoding="utf-8",
              errors="replace") as f:
        return len(f.read())


def main():
    rows, bars = [], []
    for sid, rango, hs, files in SEMANAS:
        if files:
            pesos = {f: chars(f) for f in files}
            tot = sum(pesos.values()) or 1
            rep = ", ".join(f"{f[5:10]}:{round(hs * pesos[f] / tot, 1)}h"
                            for f in files[:4]) + f" (+{len(files) - 4})" \
                if len(files) > 4 else ", ".join(
                    f"{f[5:10]}:{round(hs * pesos[f] / tot, 1)}h" for f in files)
        else:
            rep = "sin archivo (reporte 11/09)"
        nf, hf, hp = REUN[sid]
        rows.append(f"<tr><td>{sid}<br><span class='small'>{rango}</span></td>"
                    f"<td>{len(files)}</td><td class='est'><b>{hs}h</b></td>"
                    f"<td>{nf}</td><td class='med'>{round(hf + hp, 1)}h</td></tr>")
    for sid, rango, hs, files in SEMANAS:
        if sid == "S0":
            continue
        pct = round(hs / 22 * 100)
        bars.append(f"<div style='margin:4px 0'><span class='small'>{sid}</span> "
                    f"<div style='display:inline-block;background:#6aa8ff;height:14px;width:{pct}%;border-radius:4px;vertical-align:middle'></div> "
                    f"<span class='small'>{hs}h</span></div>")
    dep = "".join(f"<tr><td>{a}</td><td class='med'>{b}</td>"
                  f"<td class='small'>{c}</td></tr>" for a, b, c in DESPLIEGUE)

    html = ("<h2>Semanas (4 + pre) — sesiones y reuniones unificadas</h2>\n"
            "<p class='small'>Totales fijados por Sol 13/10. Reparto por sesion proporcional al tamano del archivo (orientativo). "
            "Reuniones = subconjunto medido (no se suma). Mes 2 se mide exacto.</p>\n"
            "<table><tr><th>Semana</th><th>#Ses</th><th>Hs trabajo</th>"
            "<th>#Fathom</th><th>Hs reuniones</th></tr>\n"
            + "\n".join(rows) + "\n</table>\n" + "".join(bars) +
            "<p><b>Total ventana: 10.5+20+12+22 = 64.5h + 2h pre = 66.5h "
            "(O2: 65).</b></p>\n"
            "<h2>Despliegue IA (maquina en paralelo al humano)</h2>\n"
            "<table><tr><th>Que corre solo</th><th>Tiempo maquina</th><th>Evidencia</th></tr>\n"
            + dep + "\n</table>")

    with open(DASH, encoding="utf-8", errors="replace") as f:
        d = f.read()
    import re
    d = re.sub(r"<h2>Semanas \((4 \+ pre|unificadas)\).*?(?=<h2>Reuniones con Emilia)",
               "", d, count=1, flags=re.S)
    marca = "<h2>Reuniones con Emilia"
    assert marca in d, "sin ancla"
    d = d.replace(marca, html + "\n" + marca, 1)
    with open(DASH, "w", encoding="utf-8") as f:
        f.write(d)
    print("OK 4 semanas + despliegue IA")


if __name__ == "__main__":
    main()
