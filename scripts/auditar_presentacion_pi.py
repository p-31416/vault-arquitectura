"""Audita los archivos de la presentación PI sin ejecutar Remotion ni modificar datos."""

from __future__ import annotations

import json
from pathlib import Path


# NOTA ES: La raíz se calcula desde este archivo, así sirve desde cualquier carpeta.
RAIZ_VAULT = Path(__file__).resolve().parents[1]

# NOTA ES: Este repositorio contiene la composición Remotion, fuera del vault.
RAIZ_REMOTION = Path(r"P:\00-repos\remotion-vault")

# NOTA ES: Inventario esperado, tomado del opencode.json actual.
MCP_ESPERADOS = {
    "comfyui",
    "n8n-mcp",
    "fathom",
    "fathom-proyectopi",
    "leantime",
    "autodesk-help",
    "autocad",
    "rhino",
}


def auditar_archivos() -> bool:
    """Comprueba que estén las fuentes, la página y la composición nueva."""
    archivos = {
        "guion": RAIZ_VAULT / "specs" / "261101-guion-visual-pi-remotion.md",
        "presentación web": RAIZ_VAULT / "diagramas" / "prompt-coach-vs-agentico.html",
        "composición Remotion": RAIZ_REMOTION / "src" / "PIStudioOS.tsx",
        "registro de composición": RAIZ_REMOTION / "src" / "Root.tsx",
    }
    correctos = True
    for nombre, ruta in archivos.items():
        existe = ruta.is_file()
        estado = "OK" if existe else "FALTA"
        print(f"[{estado}] {nombre}: {ruta}")
        correctos = correctos and existe
    return correctos


def auditar_mcps() -> bool:
    """Compara el inventario documentado con los MCP que están habilitados."""
    ruta = RAIZ_VAULT / "opencode.json"
    configuracion = json.loads(ruta.read_text(encoding="utf-8-sig"))
    habilitados = {
        nombre
        for nombre, datos in configuracion.get("mcp", {}).items()
        if datos.get("enabled") is True
    }
    faltantes = sorted(MCP_ESPERADOS - habilitados)
    adicionales = sorted(habilitados - MCP_ESPERADOS)
    print(f"[INFO] MCP esperados: {len(MCP_ESPERADOS)}; habilitados: {len(habilitados)}")
    if faltantes:
        print(f"[REVISAR] Ya no están habilitados: {', '.join(faltantes)}")
    if adicionales:
        print(f"[INFO] MCP habilitados adicionales: {', '.join(adicionales)}")
    return not faltantes


def auditar_contenido() -> bool:
    """Busca anclas narrativas para detectar una omisión accidental."""
    comprobaciones = {
        "HTML": (
            RAIZ_VAULT / "diagramas" / "prompt-coach-vs-agentico.html",
            ("META-ARQUITECTO", "diseñador de la empresa sintética", "Pipi Visual", "24/7", "MVP_02", "MVP_05", "deuda técnica", "Ask F+P", "Dartmouth"),
        ),
        "Remotion": (
            RAIZ_REMOTION / "src" / "PIStudioOS.tsx",
            ("El Meta-arquitecto diseña la empresa sintética", "PIPI RHINO", "PIPI VISUAL", "SET_01", "P = Wᵥ / Tₕ", "MANTENIMIENTO", "FATHOM"),
        ),
        "Guion": (
            RAIZ_VAULT / "specs" / "261101-guion-visual-pi-remotion.md",
            ("meta-arquitecto sistémico", "empresa sintética", "MVP_02", "MVP_05", "MVP_04.02", "deuda técnica", "Ask F+P", "Dartmouth", "Wᵥ / Tₕ"),
        ),
    }
    todo_ok = True
    for nombre, (ruta, anclas) in comprobaciones.items():
        texto = ruta.read_text(encoding="utf-8")
        ausentes = [ancla for ancla in anclas if ancla.casefold() not in texto.casefold()]
        estado = "OK" if not ausentes else "REVISAR"
        detalle = "" if not ausentes else f" — faltan: {', '.join(ausentes)}"
        print(f"[{estado}] anclas de contenido ({nombre}){detalle}")
        todo_ok = todo_ok and not ausentes
    return todo_ok


def main() -> int:
    """Ejecuta verificaciones de solo lectura y devuelve un código de salida."""
    print("Auditoría local de la presentación PI (solo lectura)\n")
    if not auditar_archivos():
        print("\nResultado: HAY ARCHIVOS PARA RECUPERAR ANTES DE AUDITAR EL CONTENIDO")
        return 1
    resultados = (auditar_mcps(), auditar_contenido())
    if all(resultados):
        print("\nResultado: PRESENTACIÓN LISTA PARA VISTA PREVIA")
        return 0
    print("\nResultado: HAY ELEMENTOS PARA REVISAR")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
