# NOTA ES: segunda tanda — vistas de la plaza como espacio (ronda 2).
import json
import urllib.parse
import urllib.request

TITLES = [
    "File:Place de la Sagrada Família.jpg",
    "File:Barcelona - Plaça de la Sagrada Família - View SE, Waiting in Queue.jpg",
    "File:Barcelona - Plaça de Gaudí - View SW on La Sagrada Família II.jpg",
    "File:Sagrada Familia, Barcelona (P1170690).jpg",
]

params = {
    "action": "query",
    "format": "json",
    "titles": "|".join(TITLES),
    "prop": "imageinfo",
    "iiprop": "url|user|extmetadata|size",
    "iiextmetadatafilter": "Artist|LicenseShortName|UsageTerms|ImageDescription",
}
url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
req = urllib.request.Request(url, headers={"User-Agent": "vault-arquitectura/1.0"})
d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
for pid, pg in d["query"]["pages"].items():
    ii = (pg.get("imageinfo") or [{}])[0]
    meta = ii.get("extmetadata", {})
    desc = (meta.get("ImageDescription") or {}).get("value", "")[:150]
    print("=" * 80)
    print("TITULO:", pg.get("title"))
    print("AUTOR:", ii.get("user"))
    print("LICENCIA:", (meta.get("LicenseShortName") or {}).get("value"))
    print("ANCHOxALTO:", ii.get("width"), "x", ii.get("height"))
    print("DESC:", desc.replace("\n", " "))
    print("URL:", ii.get("url"))
