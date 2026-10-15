"""
yt_titles.py — Trae los TITULOS, CANAL y DURACION de los videos guardados
usando la YouTube Data API v3, y los cachea en disco para no gastar cuota.

POR QUE ESTE SCRIPT EXISTE
--------------------------
Google Takeout solo guarda el 'video_id' de cada video guardado. No trae el
titulo, ni el canal, ni la duracion. Con la APIkey de la YouTube Data API v3
podemos completar esa informacion.

CUANTA CUOTA GASTA
------------------
La API da 10.000 unidades por dia por proyecto (gratis).
Una llamada a 'videos.list' cuesta 1 unidad, sin importar si pides 1 video o 50.
Tus videos: ~709 (259 Watch Later + 450 listas tematicas).
  -> 709 videos / 50 por llamada = ~15 llamadas = ~15 unidades.
  -> 0.15% de la cuota diaria. Se puede re-correr上百 veces al ano sin problema.

El detalle importante: 'search.list' cuesta 100 unidades y esta PROHIBIDO por
defecto en proyectos nuevos. Por eso este script usa 'videos.list' (1 unidad),
que ya trae titulo + canal + duracion de paso.

CACHE
-----
Los resultados se guardan en raw/yt/cache-titulos.json.
Si volves a correr el script, solo pide los IDs que FALTAN en el cache.
 Asi el gasto de cuota es practicamente cero en las siguientes corridas.

COMO EJECUTARLO
---------------
    P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py

Requiere: YOUTUBE_API_KEY en el archivo .env de la raiz del vault.
"""

import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------- NOTA ES:
# Rutas base.
VAULT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura")
TAKEOUT = Path(r"C:\Users\Solch16\Downloads\Takeout")
YTDIR = TAKEOUT / "YouTube y YouTube Music"
CACHE = VAULT / "raw" / "yt" / "cache-titulos.json"
ENVFILE = VAULT / ".env"

# El endpoint de la API. 'videos' + 'list' + 'part=snippet,contentDetails'
API_URL = "https://www.googleapis.com/youtube/v3/videos"

# La API acepta maximo 50 IDs por llamada (limite documentado por Google).
LOTE = 50


def leer_api_key():
    """Lee YOUTUBE_API_KEY del archivo .env sin usar librerias externas."""
    # NOTA ES: no usamos python-dotenv para no sumar dependencias. Es un archivo
    # simple con lineas 'CLAVE=valor'. Lo leemos a mano.
    if not ENVFILE.exists():
        raise SystemExit(f"ERROR: no existe {ENVFILE}")
    for linea in ENVFILE.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if linea.startswith("#") or "=" not in linea:
            continue
        clave, _, valor = linea.partition("=")
        if clave.strip() == "YOUTUBE_API_KEY":
            return valor.strip().strip('"').strip("'")
    raise SystemExit("ERROR: YOUTUBE_API_KEY no esta en .env")


def recolectar_video_ids():
    """Devuelve el set de todos los video_id de tus playlists de Takeout."""
    # NOTA ES: glob() con patron tolerante porque el nombre de la carpeta depende
    # del idioma del sistema ('listas de reproduccion' vs 'de reproducción').
    candidatos = [p for p in YTDIR.glob("*reproducci*n*") if p.is_dir()]
    if not candidatos:
        raise SystemExit(f"ERROR: no encuentro las playlists en {YTDIR}")
    listdir = candidatos[0]

    ids = set()
    for p in listdir.glob("*.csv"):
        # saltear el CSV maestro (indice de listas), no tiene videos
        if p.stem.lower().startswith(("lista", "listas")):
            continue
        with open(p, encoding="utf-8-sig", newline="") as f:
            rd = csv.reader(f)
            next(rd, None)  # header
            for r in rd:
                if r and r[0].strip():
                    ids.add(r[0].strip())

    print(f"Video IDs encontrados en Takeout: {len(ids)}")
    return ids


def cargar_cache():
    """Carga el cache de titulos si existe."""
    if CACHE.exists():
        data = json.loads(CACHE.read_text(encoding="utf-8"))
        print(f"Cache existente: {len(data)} titulos")
        return data
    print("Cache vacio (primera corrida)")
    return {}


def guardar_cache(cache):
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print(f"Cache guardado: {len(cache)} titulos -> {CACHE}")


def fetch_lote(ids, api_key):
    """Pide un lote de <=50 videos. Devuelve dict id -> {titulo, canal, duracion}."""
    params = urllib.parse.urlencode(
        {
            "part": "snippet,contentDetails",
            "id": ",".join(ids),
            "key": api_key,
            # NOTA ES: 'fields' es una optimizacion de Google. Le pedimos SOLO lo
            # que necesitamos, no el JSON completo. Reduce el ancho de banda y
            # es la practica recomendada oficialmente.
            "fields": "items(id,snippet(title,channelTitle),contentDetails(duration))",
        }
    )
    req = urllib.request.Request(f"{API_URL}?{params}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"ERROR de la API ({e.code}):\n{detalle[:600]}")
    except urllib.error.URLError as e:
        raise SystemExit(f"ERROR de red: {e.reason}")

    out = {}
    for item in data.get("items", []):
        vid = item.get("id")
        if not vid:
            continue
        snip = item.get("snippet", {})
        cont = item.get("contentDetails", {})
        out[vid] = {
            "titulo": snip.get("title", ""),
            "canal": snip.get("channelTitle", ""),
            "duracion": iso8601_a_min(cont.get("duration", "")),
        }
    return out


def iso8601_a_min(iso):
    """Convierte duracion ISO 8601 de YouTube a '12:34' o '1:23:45'.

    YouTube devuelve formato ISO: 'PT15M51S' = 15 minutos 51 segundos.
    NO usamos datetime porque el formato ISO de Google no es parseable por
    datetime.fromisoformat() en Python (usa 'P' en vez de 'T' al inicio).
    """
    # NOTA ES: regex simple para extraer horas, minutos, segundos.
    m = re.match(
        r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or ""
    )
    if not m:
        return ""
    h, mi, s = m.groups()
    h = int(h or 0)
    mi = int(mi or 0)
    s = int(s or 0)
    if h:
        return f"{h}:{mi:02d}:{s:02d}"
    return f"{mi}:{s:02d}"


def main():
    api_key = leer_api_key()
    print(f"API key encontrada ({len(api_key)} caracteres)")

    todos = recolectar_video_ids()
    cache = cargar_cache()

    faltan = [v for v in todos if v not in cache]
    print(f"Faltan traer: {len(faltan)}")

    if not faltan:
        print("Todo cacheado. No hace ninguna llamada a la API.")
        return

    # Calcular cuantas llamadas van a hacer
    llamadas = (len(faltan) + LOTE - 1) // LOTE
    print(f"Voy a hacer ~{llamadas} llamadas ({llamadas} unidades de 10.000 diarias)\n")

    for i in range(0, len(faltan), LOTE):
        lote = faltan[i : i + LOTE]
        n = i // LOTE + 1
        print(f"  [{n}/{llamadas}] pidiendo {len(lote)} videos...", end=" ", flush=True)
        resultado = fetch_lote(lote, api_key)
        cache.update(resultado)
        print(f"-> {len(resultado)} titles")
        # NOTA ES: pausa de 200ms entre llamadas. Es cortesia con la API de Google
        # y evita que nos bloqueen por rate-limiting si someday son mas videos.
        if i + LOTE < len(faltan):
            time.sleep(0.2)

    guardar_cache(cache)

    # Reporte final: cuantos quedaron sin titulo (videos borrados/privados)
    sin_titulo = [v for v in todos if v not in cache]
    if sin_titulo:
        print(f"\nSin titulo (borrados/privados/no accesibles): {len(sin_titulo)}")
        for v in sin_titulo[:10]:
            print(f"  - {v}")

    print(f"\nListo. Ahora corré scripts/yt_takeout_parser.py para regenerar el doc.")


if __name__ == "__main__":
    main()