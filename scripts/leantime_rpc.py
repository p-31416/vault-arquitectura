"""Cliente Leantime del vault — JSON-RPC sobre /api/jsonrpc con x-api-key.

Por que no el MCP: el endpoint /mcp responde initialize pero expone 0 tools
(el plugin MCP Server no los publica). La API JSON-RPC si expone los metodos
del repositorio, y es la via que el vault ya uso para los milestones 443-457.

Uso:
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/leantime_rpc.py <metodo> <params-json>
  ... <metodo> getAllLeantime
"""
import io
import json
import sys
import time
import urllib.error
import urllib.request

BASE = "https://pitautech-leantime.3nq4ow.easypanel.host/api/jsonrpc"
ENV = r"P:\00-repos\proyecto-pi\vault-arquitectura\.env"
PAUSA = 1.6          # segundos entre llamadas (la API tira 429 por minuto)
ESPERA_429 = 20      # pausa larga cuando el limite por minuto se dispara


def _token() -> str:
    """Lee LEANTIME_TOKEN del .env. El valor nunca se imprime."""
    for linea in io.open(ENV, encoding="utf-8", errors="replace"):
        if linea.startswith("LEANTIME_TOKEN"):
            return linea.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("LEANTIME_TOKEN no encontrado en .env")


def rpc(metodo: str, params: dict | None = None) -> dict:
    """Llama un metodo JSON-RPC de Leantime. Reintenta ante 429."""
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": metodo,
                          "params": params or {}}).encode("utf-8")
    req = urllib.request.Request(
        BASE, data=payload,
        headers={"Content-Type": "application/json", "x-api-key": _token()})
    for _ in range(6):
        try:
            r = urllib.request.urlopen(req, timeout=90)
            salida = json.loads(r.read().decode("utf-8", errors="replace"))
            time.sleep(PAUSA)
            return salida
        except urllib.error.HTTPError as e:
            cuerpo = e.read().decode("utf-8", errors="replace")
            if e.code == 429:
                time.sleep(ESPERA_429)
                continue
            time.sleep(PAUSA)
            return {"http": e.code, "body": cuerpo[:400]}
        except Exception as e:
            time.sleep(PAUSA)
            return {"err": str(e)}
    return {"err": "rate-limit"}


def resultado(metodo: str, params: dict | None = None):
    """Como rpc() pero devuelve solo 'result' (o el error)."""
    salida = rpc(metodo, params)
    if "result" in salida:
        return salida["result"]
    return {"__error": salida.get("error", salida)}


def _params(texto: str) -> dict:
    """Lee params desde JSON en linea o desde un archivo con prefijo @."""
    if texto.startswith("@"):
        return json.loads(io.open(texto[1:], encoding="utf-8-sig").read())
    return json.loads(texto)


if __name__ == "__main__":
    if sys.argv[1] == "getAllLeantime":
        metodo = sys.argv[2]
        params = _params(sys.argv[3]) if len(sys.argv) > 3 else {}
        print(json.dumps(resultado(metodo, params), ensure_ascii=False, indent=2))
    else:
        params = _params(sys.argv[2]) if len(sys.argv) > 2 else {}
        print(json.dumps(rpc(sys.argv[1], params), ensure_ascii=False, indent=2))
