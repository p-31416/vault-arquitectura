#!/usr/bin/env python3
# NOTA ES: este script es de SOLO LECTURA. Pregunta al VPS cómo está y te lo resume.
# NOTA ES: no instala, no reinicia y no modifica nada del servidor: solo corre comandos de lectura.
# NOTA ES: usa la biblioteca estándar de Python (subprocess), así que no hay que instalar nada.
# NOTA ES: se conecta por SSH usando el alias `contabo` que ya está en tu archivo de configuración SSH.

import argparse
import json
import re
import shutil
import subprocess
import sys

# NOTA ES: el bloque remoto se manda a SSH como un único string.
# NOTA ES: los `echo '===XXX==='` son marcadores: nos permiten separar cada bloque al parsear.
# NOTA ES: todos los comandos son de lectura (free, uptime, df, docker ps, docker stats, docker service ls).
COMANDO_REMOTO = r"""
echo '===MEM==='; free -m
echo '===UPTIME==='; nproc; uptime
echo '===DISK==='; df -h /
echo '===CONT==='; docker ps --format '{{.Names}}|{{.Status}}|{{.Image}}'
echo '===STAT==='; docker stats --no-stream --format '{{.Name}}|{{.MemUsage}}|{{.CPUPerc}}'
echo '===SWARM==='; docker service ls --format '{{.Name}}|{{.Replicas}}|{{.Mode}}'
"""


def parsear_bloques(salida):
    # NOTA ES: la salida de SSH viene con los marcadores que pusimos arriba.
    # NOTA ES: acá armamos un diccionario { 'MEM': 'texto', 'UPTIME': 'texto', ... }.
    bloques = {}
    clave = None
    for linea in salida.splitlines():
        if linea.startswith("===") and linea.endswith("==="):
            clave = linea.strip("= ")
            bloques[clave] = []
        elif clave is not None:
            bloques[clave].append(linea)
    return {k: "\n".join(v).strip() for k, v in bloques.items()}


def a_mb(texto):
    # NOTA ES: las herramientas de Linux escriben la memoria como "736MiB", "1.5GiB" o "800kB".
    # NOTA ES: esta función convierte eso a megabytes (entero) para poder sumar y comparar.
    m = re.match(r"^([\d.]+)\s*([KMG]i?B)$", texto.strip(), re.IGNORECASE)
    if not m:
        return 0
    numero = float(m.group(1))
    unidad = m.group(2).upper()
    if unidad.startswith("G"):
        return int(numero * 1024)
    if unidad.startswith("M"):
        return int(numero)
    return int(numero / 1024)


def parsear_memoria(bloque):
    # NOTA ES: `free -m` imprime dos líneas que nos importan: Mem: y Swap:.
    # NOTA ES: de la de Mem nos quedamos con total, used y available (available es la que cuenta:
    # NOTA ES: incluye la caché que Linux puede liberar en cualquier momento).
    datos = {"total_mb": 0, "usada_mb": 0, "disponible_mb": 0, "swap_total_mb": 0, "swap_usada_mb": 0}
    for linea in bloque.splitlines():
        partes = linea.split()
        if not partes:
            continue
        if partes[0] == "Mem:" and len(partes) >= 7:
            datos["total_mb"] = int(partes[1])
            datos["usada_mb"] = int(partes[2])
            datos["disponible_mb"] = int(partes[6])
        elif partes[0] == "Swap:" and len(partes) >= 4:
            datos["swap_total_mb"] = int(partes[1])
            datos["swap_usada_mb"] = int(partes[2])
    return datos


def parsear_contenedores(bloque):
    # NOTA ES: cada línea de `docker stats` viene como "nombre|189.1MiB / 7.755GiB|0.22%".
    # NOTA ES: nos quedamos con el nombre y los MB de memoria que usa.
    lista = []
    for linea in bloque.splitlines():
        if "|" not in linea:
            continue
        partes = linea.split("|")
        if len(partes) < 2:
            continue
        uso = partes[1].split("/")[0].strip()
        lista.append({"nombre": partes[0].strip(), "memoria_mb": a_mb(uso), "cpu": partes[2].strip() if len(partes) > 2 else ""})
    return lista


def parsear_disco(bloque):
    # NOTA ES: `df -h /` imprime una tabla. La última línea es el sistema de archivos raíz.
    for linea in reversed(bloque.splitlines()):
        partes = linea.split()
        if len(partes) >= 5 and partes[0].startswith("/"):
            return {"sistema": partes[0], "total": partes[1], "usado": partes[2], "disponible": partes[3], "uso_pct": partes[4]}
    return {}


def ejecutar(host):
    # NOTA ES: primero miramos si el comando `ssh` existe en esta computadora.
    if shutil.which("ssh") is None:
        raise RuntimeError("No se encontró el comando `ssh`. Instalá OpenSSH o usá Git Bash.")
    # NOTA ES: `subprocess.run` ejecuta el comando y captura stdout y stderr.
    # NOTA ES: `timeout=60` evita que se quede colgado si el VPS no responde.
    proceso = subprocess.run(
        ["ssh", host, COMANDO_REMOTO],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if proceso.returncode != 0:
        raise RuntimeError(f"SSH devolvió error {proceso.returncode}: {proceso.stderr.strip()}")
    return proceso.stdout


def veredicto(memoria, contenedores):
    # NOTA ES: la decisión que nos importa es una sola: ¿entra Hermes (3 GB) sin ahogar el VPS?
    # NOTA ES: calculamos la suma de memoria de los contenedores y la comparamos con la disponible.
    suma = sum(c["memoria_mb"] for c in contenedores)
    disponible = memoria["disponible_mb"]
    if disponible >= 4096:
        estado = "OK: entra Hermes con límite de 3 GB y queda margen"
    elif disponible >= 3072:
        estado = "AJUSTADO: entra Hermes al límite, pero sin margen: monitorizar swap y uso"
    else:
        estado = "AJUSTADO: NO entra Hermes con 3 GB: hay que liberar RAM o ampliar el VPS"
    return {
        "veredicto": estado,
        "memoria_contenedores_mb": suma,
        "memoria_disponible_mb": disponible,
        "hola_para_hermes_mb": max(0, disponible - 3072),
    }


def imprimir_texto(informe):
    print("=" * 72)
    print("STUDIO OS · INVENTARIO DEL VPS (solo lectura)")
    print("=" * 72)
    m = informe["memoria"]
    print(f"RAM total          : {m['total_mb']} MB")
    print(f"RAM usada          : {m['usada_mb']} MB")
    print(f"RAM disponible     : {m['disponible_mb']} MB")
    print(f"Swap               : {m['swap_usada_mb']} / {m['swap_total_mb']} MB")
    d = informe["disco"]
    print(f"Disco raíz         : {d.get('usado', '?')} usados de {d.get('total', '?')} ({d.get('uso_pct', '?')})")
    print(f"CPU                : {informe['cpu_nucleos']} núcleos · carga {informe['carga']}")
    print()
    print("Contenedores (memoria en MB):")
    for c in sorted(informe["contenedores"], key=lambda x: x["memoria_mb"], reverse=True):
        print(f"  {c['memoria_mb']:>6} MB  {c['nombre']}")
    print()
    v = informe["veredicto_ram"]
    print(f"Memoria de contenedores: {v['memoria_contenedores_mb']} MB")
    print(f"VEREDICTO: {v['veredicto']}")
    print(f"Hueco para Hermes (3 GB): {v['hola_para_hermes_mb']} MB")
    if informe["servicios_swarm"]:
        print()
        print(f"Servicios Swarm activos: {len(informe['servicios_swarm'])}")


def main():
    # NOTA ES: argparse es la forma estándar de pedir opciones por línea de comandos.
    # NOTA ES: --host cambia el alias SSH (por defecto `contabo`) y --json imprime el informe como JSON.
    parser = argparse.ArgumentParser(description="Inventario de solo lectura del VPS para Studio OS")
    parser.add_argument("--host", default="contabo", help="alias SSH del VPS (por defecto: contabo)")
    parser.add_argument("--json", dest="json_salida", help="archivo .json donde volcar el informe")
    args = parser.parse_args()

    try:
        salida = ejecutar(args.host)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    bloques = parsear_bloques(salida)
    memoria = parsear_memoria(bloques.get("MEM", ""))
    contenedores = parsear_contenedores(bloques.get("STAT", ""))
    disco = parsear_disco(bloques.get("DISK", ""))
    servicios = [l for l in bloques.get("SWARM", "").splitlines() if l.strip()]

    carga = "?"
    nucleos = "?"
    for linea in bloques.get("UPTIME", "").splitlines():
        if "load average" in linea:
            carga = linea.split("load average:")[-1].strip()
        elif linea.strip().isdigit():
            nucleos = linea.strip()

    informe = {
        "host": args.host,
        "memoria": memoria,
        "disco": disco,
        "cpu_nucleos": nucleos,
        "carga": carga,
        "contenedores": contenedores,
        "servicios_swarm": servicios,
        "veredicto_ram": veredicto(memoria, contenedores),
    }

    imprimir_texto(informe)
    if args.json_salida:
        with open(args.json_salida, "w", encoding="utf-8") as archivo:
            json.dump(informe, archivo, indent=2, ensure_ascii=False)
        print(f"\nInforme JSON escrito en: {args.json_salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
