# -*- coding: utf-8 -*-
"""
Cliente CLI del MCP de Rhino (reer-rhino-mcp) para Windows.
=============================================================

Permite operatear Rhino desde la terminal SIN depender de que el servidor MCP
este registrado en el IDE: levanta el servidor MCP por stdio, habla JSON-RPC
con el y ejecuta la tool que le pidas.

Uso
---
  # listar tools
  py -3 rhino-mcp-cli.py tools

  # ejecutar un script Python dentro de Rhino (contenido de archivo)
  py -3 rhino-mcp-cli.py exec scripts\axonometria-militar-rhino.py

  # ejecutar una linea de codigo
  py -3 rhino-mcp-cli.py exec "import Rhino; print(Rhino.RhinoApp.Version)"

  # capturar el viewport a PNG
  py -3 rhino-mcp-cli.py shot salida.png

  # listar capas / escena
  py -3 rhino-mcp-cli.py scene
  py -3 rhino-mcp-cli.py layers

Requisito
---------
Rhino 8 abierto con `scripts/rhino-mcp-server-rhino.py` corriendo (el servidor
del lado Rhino escucha en localhost:9876).
"""

import base64
import json
import os
import subprocess
import sys

UVX = r"C:\Users\Solch16\AppData\Local\Programs\Python\Python312\Scripts\uvx.exe"
SERVER = ["--with", "mcp<2", "reer-rhino-mcp"]


def _enviar(proc, mensaje):
    """Escribe un mensaje JSON-RPC (una linea) al servidor."""
    proc.stdin.write(json.dumps(mensaje) + "\n")
    proc.stdin.flush()


def _recibir(proc):
    """Lee la siguiente respuesta JSON valida del servidor."""
    while True:
        linea = proc.stdout.readline()
        if not linea:
            return None
        linea = linea.strip()
        if not linea:
            continue
        try:
            return json.loads(linea)
        except ValueError:
            continue  # avisos del servidor


def _conectar():
    """Arranca el servidor MCP y completa el handshake initialize."""
    proc = subprocess.Popen([UVX] + SERVER, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            universal_newlines=True, encoding="utf-8",
                            errors="replace", bufsize=1)
    _enviar(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                   "params": {"protocolVersion": "2024-11-05",
                              "capabilities": {},
                              "clientInfo": {"name": "rhino-mcp-cli",
                                             "version": "1.0"}}})
    _recibir(proc)
    _enviar(proc, {"jsonrpc": "2.0", "method": "notifications/initialized"})
    return proc


def _llamar(proc, nombre, argumentos, id_tool=2):
    """Ejecuta una tool MCP y devuelve el texto de la respuesta."""
    _enviar(proc, {"jsonrpc": "2.0", "id": id_tool, "method": "tools/call",
                   "params": {"name": nombre, "arguments": argumentos}})
    while True:
        respuesta = _recibir(proc)
        if respuesta is None:
            return "SIN RESPUESTA (el servidor se cerro)"
        if respuesta.get("id") == id_tool:
            contenido = respuesta.get("result", {}).get("content", [])
            partes = []
            for item in contenido:
                if item.get("type") == "text":
                    partes.append(item.get("text", ""))
            return "\n".join(partes) if partes else json.dumps(respuesta)[:2000]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    comando = sys.argv[1].lower()
    proc = _conectar()
    try:
        if comando == "tools":
            _enviar(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list",
                           "params": {}})
            while True:
                r = _recibir(proc)
                if r is None:
                    break
                if r.get("id") == 2:
                    for tool in r["result"]["tools"]:
                        print("- %s: %s" % (tool["name"],
                                            tool["description"].split("\n")[0]))
                    break

        elif comando == "exec":
            if len(sys.argv) < 3:
                print("Falta el codigo o el archivo .py")
                return 1
            ruta = sys.argv[2]
            if os.path.isfile(ruta):
                with open(ruta, "r", encoding="utf-8") as manija:
                    codigo = manija.read()
                print("[ejecutando archivo] %s (%d caracteres)" % (ruta, len(codigo)))
            else:
                codigo = ruta
                print("[ejecutando linea] %s" % codigo)
            print(_llamar(proc, "execute_rhino_code", {"code": codigo}))

        elif comando == "shot":
            destino = sys.argv[2] if len(sys.argv) > 2 else "rhino-viewport.png"
            max_size = int(sys.argv[3]) if len(sys.argv) > 3 else 1400
            anotaciones = False
            if len(sys.argv) > 4:
                anotaciones = sys.argv[4].lower() in ("1", "true", "si", "yes")
            _enviar(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                           "params": {"name": "capture_rhino_viewport",
                                      "arguments": {"max_size": max_size,
                                                    "show_annotations": anotaciones}}})
            guardado = False
            while not guardado:
                r = _recibir(proc)
                if r is None:
                    print("SIN RESPUESTA")
                    return 1
                if r.get("id") != 2:
                    continue
                for item in r.get("result", {}).get("content", []):
                    if item.get("type") == "image":
                        with open(destino, "wb") as manija:
                            manija.write(base64.b64decode(item["data"]))
                        print("captura guardada en %s" % destino)
                        guardado = True
            if not guardado:
                print("La tool no devolvio imagen")

        elif comando == "scene":
            print(_llamar(proc, "get_rhino_scene_info", {}))

        elif comando == "execshot":
            # ejecuta un script y captura el viewport en la MISMA sesion MCP
            if len(sys.argv) < 4:
                print("Uso: execshot <archivo.py> <salida.png> [max_size]")
                return 1
            ruta = sys.argv[2]
            destino = sys.argv[3]
            max_size = int(sys.argv[4]) if len(sys.argv) > 4 else 1400
            with open(ruta, "r", encoding="utf-8") as manija:
                codigo = manija.read()
            print(_llamar(proc, "execute_rhino_code", {"code": codigo}))
            _enviar(proc, {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                           "params": {"name": "capture_rhino_viewport",
                                      "arguments": {"max_size": max_size,
                                                    "show_annotations": False}}})
            while True:
                r = _recibir(proc)
                if r is None:
                    print("SIN RESPUESTA")
                    return 1
                if r.get("id") != 3:
                    continue
                for item in r.get("result", {}).get("content", []):
                    if item.get("type") == "image":
                        with open(destino, "wb") as manija:
                            manija.write(base64.b64decode(item["data"]))
                        print("captura guardada en %s" % destino)

        elif comando == "layers":
            print(_llamar(proc, "get_rhino_layers", {}))

        elif comando == "selected":
            print(_llamar(proc, "get_rhino_selected_objects", {}))

        else:
            print("Comando desconocido: %s" % comando)
            return 1
    finally:
        try:
            proc.stdin.close()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
    return 0


if __name__ == "__main__":
    sys.exit(main())
