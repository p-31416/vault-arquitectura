#!/usr/bin/env python3
# NOTA ES: este script publica en el agente los archivos de texto que viven dentro del documento maestro.
# NOTA ES: el documento maestro (00-filo-mvp_07.md) es la UNICA fuente: de ahi se copian SOUL.md y las skills.
# NOTA ES: publica por SSH usando `cat` dentro del contenedor: no toca el host, no reinicia el servicio.
# NOTA ES: usa la biblioteca estandar, no instala nada.

import argparse
import re
import subprocess
import sys
from pathlib import Path

# NOTA ES: la raiz del repo se deduce de la ubicacion de este archivo (scripts/ esta en la raiz).
RAIZ = Path(__file__).resolve().parent.parent
# NOTA ES: el documento maestro: un solo archivo con todo el diseno del sistema.
MAESTRO = RAIZ / "proyectos" / "MVP_07-studio-os-sistema" / "00-filo-mvp_07.md"

# NOTA ES: cada bloque publicable se marca en el maestro con una linea de comentario HTML
# NOTA ES: "<!-- archivo: ruta/dentro/del/vault -->" seguida de un bloque de codigo delimitado.
MARCA = re.compile(r"<!--\s*archivo:\s*(?P<ruta>[^\s>]+)\s*-->")

# NOTA ES: en el contenedor, estos archivos van a su lugar en el volumen /opt/data.
# NOTA ES: el prefijo "hermes/" del vault se quita porque en el contenedor no existe esa carpeta.
DESTINOS = {
    "hermes/SOUL.md": "/opt/data/SOUL.md",
    "hermes/skills/auditar-documentacion-cad/SKILL.md": "/opt/data/skills/auditar-documentacion-cad/SKILL.md",
}


def extraer_bloques(texto):
    # NOTA ES: recorremos el documento linea por linea.
    # NOTA ES: cuando encontramos la marca, buscamos el bloque de codigo que viene despues.
    # NOTA ES: el bloque termina en la linea que solo tiene tres acentos graves.
    bloques = {}
    lineas = texto.splitlines()
    i = 0
    while i < len(lineas):
        coincidencia = MARCA.search(lineas[i])
        if not coincidencia:
            i += 1
            continue
        ruta = coincidencia.group("ruta")
        # NOTA ES: saltamos lineas en blanco hasta encontrar la apertura del bloque de codigo.
        j = i + 1
        while j < len(lineas) and not lineas[j].strip():
            j += 1
        if j >= len(lineas) or not lineas[j].strip().startswith("```"):
            i += 1
            continue
        # NOTA ES: guardamos el contenido del bloque, sin las lineas de la valla.
        contenido = []
        j += 1
        while j < len(lineas) and not lineas[j].strip().startswith("```"):
            contenido.append(lineas[j])
            j += 1
        bloques[ruta] = "\n".join(contenido) + "\n"
        i = j + 1
    return bloques


def ssh(host, comando, entrada=None):
    # NOTA ES: `ssh` con entrada estandar permite mandar el archivo por el pipe sin scp ni archivos temporales.
    # NOTA ES: si entrada es None, el comando solo imprime su salida (lo usamos para leer).
    proceso = subprocess.run(
        ["ssh", host, comando],
        input=entrada,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if proceso.returncode != 0:
        raise RuntimeError(f"SSH devolvio {proceso.returncode}: {proceso.stderr.strip()}")
    return proceso.stdout.strip()


def resolver_contenedor(host):
    # NOTA ES: en Docker Swarm los contenedores se llaman "servicio.1.tarea", no "servicio".
    # NOTA ES: por eso primero sacamos el ID real del contenedor con ese nombre.
    salida = ssh(host, "docker ps --filter name=hermes --format '{{.ID}}' | head -1")
    if not salida:
        raise RuntimeError("No encontre el contenedor de Hermes en el VPS (docker ps --filter name=hermes).")
    return salida


def publicar(host, contenedor, destino, contenido):
    # NOTA ES: `docker exec -i` mantiene abierto el canal de entrada: el texto viaja al contenedor.
    # NOTA ES: dentro, `cat > archivo` lo escribe. El path del contenedor va entre comillas simples.
    comando = f"docker exec -i {contenedor} sh -c 'mkdir -p $(dirname {destino}) && cat > {destino}'"
    ssh(host, comando, entrada=contenido)


def verificar(host, contenedor, destino):
    # NOTA ES: releemos el archivo para confirmar que quedo escrito y con que tamaño.
    return ssh(host, f"docker exec {contenedor} sh -c 'wc -c {destino} && head -1 {destino}'")


def main():
    # NOTA ES: argparse toma las opciones de la linea de comandos.
    # NOTA ES: --dry-run muestra que se publicaria sin tocar el VPS (es el modo seguro para empezar).
    parser = argparse.ArgumentParser(description="Publica SOUL.md y las skills del documento maestro en el agente")
    parser.add_argument("--host", default="contabo", help="alias SSH del VPS (por defecto: contabo)")
    parser.add_argument("--dry-run", action="store_true", help="muestra que haria, sin publicar")
    args = parser.parse_args()

    if not MAESTRO.exists():
        print(f"ERROR: no se encontro el documento maestro en {MAESTRO}", file=sys.stderr)
        return 1

    bloques = extraer_bloques(MAESTRO.read_text(encoding="utf-8"))
    publicables = {ruta: txt for ruta, txt in bloques.items() if ruta in DESTINOS}
    if not publicables:
        print("ERROR: el documento maestro no tiene bloques publicables (marcadores '<!-- archivo: ... -->').", file=sys.stderr)
        return 1

    print("Bloques encontrados en el documento maestro:")
    for ruta, contenido in publicables.items():
        print(f"  {ruta} -> {DESTINOS[ruta]}  ({len(contenido)} caracteres)")

    if args.dry_run:
        print("\nDry run: no se toco el VPS.")
        return 0

    try:
        contenedor = resolver_contenedor(args.host)
        print(f"\nContenedor de Hermes: {contenedor}")
        for ruta, contenido in publicables.items():
            destino = DESTINOS[ruta]
            publicar(args.host, contenedor, destino, contenido)
            print(f"\nPublicado {ruta} -> {destino}")
            print(f"  {verificar(args.host, contenedor, destino)}")
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("\nListo. El agente ya tiene identidad y habilidades nuevas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
