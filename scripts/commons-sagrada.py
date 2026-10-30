# NOTA ES: consulta autor + licencia + URL de candidatas Commons (plaza Sagrada).
import json
import urllib.parse
import urllib.request

TITLES = [
    "File:Place de la Sagrada Família 2.jpg",
    "File:Barcelona - Plaça de la Sagrada Família - View NNE on La Sagrada Família - Passion façade I.jpg",
    "File:Barcelona - Plaça de la Sagrada Família - View NE on La Sagrada Família - Passion façade I.jpg",
    "File:Plaça de la Sagrada Família.JPG",
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
    print("=" * 80)
    print("TITULO:", pg.get("title"))
    print("AUTOR:", ii.get("user"))
    print("LICENCIA:", (meta.get("LicenseShortName") or {}).get("value"))
    print("ANCHOxALTO:", ii.get("width"), "x", ii.get("height"))
    print("URL:", ii.get("url"))
