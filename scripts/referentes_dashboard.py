"""
referentes_dashboard.py — genera un tablero HTML navegable por tags a partir del
inventario JSON + las imagenes de una carpeta.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/referentes_dashboard.py ^
        --slug aixgaudi

Salida:
    activos/referentes/<slug>/index.html   (un solo archivo, imagenes embebidas)

Ese HTML se abre en cualquier navegador, se manda por mail/WhatsApp o se publica
arrastrandolo a Netlify Drop. Los filtros quedan en la URL: cada vista es un link
compartible (#tema=fachada&material=hormigon).
"""
import argparse
import base64
import io
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

ANCHO_THUMB = 520
CALIDAD = 80


def thumb_b64(path):
    if Image:
        im = Image.open(path).convert("RGB")
        if im.width > ANCHO_THUMB:
            im = im.resize((ANCHO_THUMB, round(im.height * ANCHO_THUMB / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=CALIDAD, optimize=True, progressive=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


PLANTILLA = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITULO__ · referentes</title>
<style>
  :root{
    --bg:#0d0e11; --panel:#15171c; --panel2:#1b1e24; --line:#272b33;
    --txt:#eef0f4; --dim:#9aa2b1; --acc:#d7ff3e; --acc2:#ff6a3d;
    --r:14px;
  }
  *{box-sizing:border-box}
  html,body{margin:0;background:var(--bg);color:var(--txt);
    font-family:ui-sans-serif,system-ui,"Segoe UI",Inter,Roboto,Arial,sans-serif}
  a{color:inherit}
  header{position:sticky;top:0;z-index:30;background:rgba(13,14,17,.86);
    backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
  .bar{display:flex;gap:18px;align-items:center;padding:14px 22px;flex-wrap:wrap}
  .brand{display:flex;align-items:center;gap:10px;min-width:0}
  .dot{width:9px;height:9px;border-radius:50%;background:var(--acc);box-shadow:0 0 14px var(--acc)}
  .brand h1{font-size:16px;margin:0;letter-spacing:.02em;white-space:nowrap}
  .brand small{color:var(--dim);font-size:12px;white-space:nowrap}
  .tools{display:flex;gap:10px;margin-left:auto;align-items:center;flex:1 1 340px;justify-content:flex-end}
  input[type=search]{flex:1 1 240px;max-width:340px;padding:10px 14px;border-radius:999px;
    border:1px solid var(--line);background:var(--panel);color:var(--txt);font-size:13px;outline:none}
  input[type=search]:focus{border-color:#3d4450}
  button{font:inherit;cursor:pointer;border-radius:999px;border:1px solid var(--line);
    background:var(--panel);color:var(--txt);padding:9px 14px;font-size:12.5px;transition:.15s}
  button:hover{border-color:#464e5c;background:var(--panel2)}
  button.acc{background:var(--acc);color:#12140c;border-color:var(--acc);font-weight:600}
  nav.views{display:flex;gap:8px;overflow-x:auto;padding:0 22px 12px;scrollbar-width:none}
  nav.views::-webkit-scrollbar{display:none}
  .chip{white-space:nowrap;border-radius:999px;padding:7px 13px;font-size:12px;border:1px solid var(--line);
    background:transparent;color:var(--dim)}
  .chip:hover{color:var(--txt)}
  .chip.on{background:var(--txt);color:#0d0e11;border-color:var(--txt);font-weight:600}
  .wrap{display:grid;grid-template-columns:230px 1fr;gap:0;min-height:calc(100vh - 120px)}
  aside{border-right:1px solid var(--line);padding:18px 16px 60px;position:sticky;top:112px;
    align-self:start;max-height:calc(100vh - 112px);overflow:auto}
  aside h3{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);
    margin:18px 0 8px;font-weight:600}
  aside h3:first-child{margin-top:0}
  .fchip{display:flex;justify-content:space-between;gap:8px;width:100%;text-align:left;margin:3px 0;
    border-radius:9px;background:transparent;border:1px solid transparent;color:var(--dim);padding:6px 9px;font-size:12.5px}
  .fchip:hover{background:var(--panel);color:var(--txt);border-color:var(--line)}
  .fchip.on{background:var(--acc);color:#12140c;font-weight:600;border-color:var(--acc)}
  .fchip .n{opacity:.65;font-variant-numeric:tabular-nums}
  .clear{width:100%;margin-top:16px;font-size:11.5px;color:var(--acc2);background:transparent;border:none;text-align:left}
  main{padding:18px 22px 80px;min-width:0}
  .masonry{column-count:4;column-gap:14px}
  @media(max-width:1600px){.masonry{column-count:3}}
  @media(max-width:1100px){.masonry{column-count:2}}
  @media(max-width:860px){.wrap{grid-template-columns:1fr}aside{position:static;max-height:none;
    border-right:none;border-bottom:1px solid var(--line);padding-bottom:14px}
    aside .fgroup{display:none} aside.open .fgroup{display:block} main{padding-top:12px}}
  @media(max-width:620px){.masonry{column-count:1}.bar{padding:12px 14px}nav.views{padding:0 14px 10px}main{padding:12px 14px 70px}}
  .card{break-inside:avoid;margin:0 0 14px;border-radius:var(--r);overflow:hidden;background:var(--panel);
    position:relative;cursor:zoom-in;border:1px solid transparent;transition:.18s}
  .card:hover{border-color:#3b4250;transform:translateY(-2px)}
  .card img{width:100%;height:auto;display:block}
  .ov{position:absolute;inset:auto 0 0 0;padding:26px 12px 11px;
    background:linear-gradient(transparent,rgba(8,9,12,.92));opacity:0;transition:.18s}
  .card:hover .ov{opacity:1}
  .t{font-size:12.5px;font-weight:600;line-height:1.25;margin-bottom:6px}
  .pills{display:flex;gap:5px;flex-wrap:wrap}
  .pill{font-size:10px;padding:3px 7px;border-radius:999px;background:rgba(255,255,255,.12);
    color:#dfe3ea;border:1px solid rgba(255,255,255,.08)}
  .badge{position:absolute;top:10px;left:10px;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;
    padding:4px 8px;border-radius:999px;background:rgba(10,11,14,.72);border:1px solid rgba(255,255,255,.14);color:#cfd5df}
  .empty{color:var(--dim);font-size:13.5px;max-width:520px;line-height:1.6;padding:40px 0}
  .empty b{color:var(--txt)}
  #lb{position:fixed;inset:0;z-index:60;background:rgba(6,7,9,.95);display:none;
    grid-template-columns:1fr 380px}
  #lb.on{display:grid}
  #lb .img{display:flex;align-items:center;justify-content:center;padding:34px;min-width:0}
  #lb .img img{max-width:100%;max-height:calc(100vh - 68px);object-fit:contain;border-radius:10px}
  #lb .side{background:var(--panel);border-left:1px solid var(--line);padding:26px 24px;overflow:auto;position:relative}
  #lb h2{font-size:19px;margin:0 0 6px;line-height:1.25}
  #lb .sub{color:var(--dim);font-size:12.5px;margin-bottom:20px}
  #lb .lab{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin:20px 0 7px}
  #lb .nota{font-size:13px;line-height:1.55;color:#cfd5df;background:var(--panel2);padding:12px 14px;border-radius:10px}
  #lb .links{display:flex;flex-direction:column;gap:8px;margin-top:20px}
  #lb .links a{font-size:12.5px;text-decoration:none;padding:9px 12px;border:1px solid var(--line);
    border-radius:9px;color:var(--txt);display:flex;justify-content:space-between}
  #lb .links a:hover{border-color:#4a5262}
  .x{position:absolute;top:16px;right:16px}
  .navbtns{display:flex;gap:8px;margin-top:22px}
  @media(max-width:900px){#lb{grid-template-columns:1fr;grid-template-rows:1fr auto}
    #lb .img{padding:14px}#lb .side{border-left:none;border-top:1px solid var(--line);max-height:46vh}}
  footer{border-top:1px solid var(--line);padding:22px;color:var(--dim);font-size:12px;line-height:1.7}
  footer b{color:var(--txt)}
  .toast{position:fixed;left:50%;bottom:28px;transform:translate(-50%,20px);background:var(--acc);
    color:#12140c;font-weight:600;font-size:12.5px;padding:10px 18px;border-radius:999px;opacity:0;
    pointer-events:none;transition:.2s;z-index:90}
  .toast.on{opacity:1;transform:translate(-50%,0)}
</style>
</head>
<body>
<header>
  <div class="bar">
    <div class="brand">
      <span class="dot"></span>
      <h1>__TITULO__</h1>
      <small id="count"></small>
    </div>
    <div class="tools">
      <input id="q" type="search" placeholder="Buscar obra, autor, material, nota...">
      <button id="share">Copiar vista</button>
    </div>
  </div>
  <nav class="views" id="views"></nav>
</header>

<div class="wrap">
  <aside id="aside">
    <button class="chip" id="toggle" style="display:none;width:100%;margin-bottom:10px">Filtros</button>
    <div id="facets"></div>
    <button class="clear" id="clear">Limpiar filtros</button>
  </aside>
  <main>
    <div class="masonry" id="grid"></div>
    <div class="empty" id="empty" style="display:none"></div>
  </main>
</div>

<div id="lb">
  <div class="img"><img id="lbimg" alt=""></div>
  <div class="side" id="lbside"></div>
</div>

<footer>
  <b>Como sumar referentes:</b> Emilia sube imagenes a la carpeta compartida del Drive →
  <code>scripts/referentes_pinterest.py</code> trae los boards publicos y
  <code>scripts/referentes_dashboard.py</code> regenera este tablero.
  Las imagenes quedan sin clasificar hasta que les asignamos tags. Cada vista de filtros es un link: se copia y se comparte.
</footer>

<div class="toast" id="toast">Vista copiada</div>

<script>
const DATA = __DATA__;
const AXES = DATA.ejes;
const ORDEN_EJES = ["tema","estrategia","material","representacion","programa","escala","estado","uso"];
const ETIQUETA = {tema:"Tema",estrategia:"Estrategia",material:"Material",
  representacion:"Representación",programa:"Programa",escala:"Escala",estado:"Estado",uso:"Uso"};
const VISTAS = [
  {n:"Todo", s:{}},
  {n:"Shortlist", s:{tags:{estado:["shortlist"]}}},
  {n:"Mercado", s:{tags:{programa:["mercado"]}}},
  {n:"Cultura", s:{tags:{programa:["cultura"]}}},
  {n:"Plaza", s:{tags:{programa:["plaza"]}}},
  {n:"Fachadas y pieles", s:{tags:{tema:["fachada","piel"]}}},
  {n:"Biomimética", s:{tags:{tema:["biomimetica"]}}},
  {n:"Estructura", s:{tags:{tema:["estructura"]}}},
  {n:"Generado con IA", s:{tags:{representacion:["ia"]}}},
  {n:"Pendientes", s:{pend:true}},
  {n:"Descartados", s:{tags:{estado:["descartado"]}}}
];

let state = {q:"", tags:{}, view:"Todo"};
let actual = 0, lista = [];

function tagsDe(it){ return Object.values(it.tags||{}).flat().filter(Boolean); }
function tituloDe(it){ return it.obra || it.titulo || "Sin título"; }
function fechaDe(it){ return it.fecha_alta || ""; }

function pendiente(it){
  const t = it.tags||{};
  return (t.tema||[]).includes("sin-clasificar") || !tagsDe(it).length;
}

function match(it){
  if(state.view==="Pendientes" && !pendiente(it)) return false;
  if(state.view!=="Pendientes" && pendiente(it) && state.view!=="Todo") return false;
  if(state.q){
    const hay = [it.titulo,it.obra,it.autor,it.ciudad,it.anio,it.nota,it.descripcion,
      ...tagsDe(it)].join(" ").toLowerCase();
    if(!hay.includes(state.q.toLowerCase())) return false;
  }
  for(const [ax,vals] of Object.entries(state.tags)){
    if(!vals||!vals.length) continue;
    const tiene = it.tags[ax]||[];
    if(!vals.some(v=>tiene.includes(v))) return false;
  }
  return true;
}

function contar(){
  const map = {};
  DATA.items.forEach(it=>{
    AXES.forEach(ax=>{
      const vals = (it.tags[ax]||[]);
      vals.forEach(v=>{
        map[ax] = map[ax]||{};
        map[ax][v] = (map[ax][v]||0)+1;
      });
    });
  });
  return map;
}

function pintarFacets(){
  const cont = contar();
  const html = ORDEN_EJES.filter(ax=>cont[ax]).map(ax=>{
    const vals = Object.entries(cont[ax]).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
    return `<div class="fgroup"><h3>${ETIQUETA[ax]||ax}</h3>` + vals.map(([v,n])=>{
      const on = (state.tags[ax]||[]).includes(v);
      return `<button class="fchip ${on?"on":""}" data-ax="${ax}" data-v="${v}">
        <span>${v}</span><span class="n">${n}</span></button>`;
    }).join("") + `</div>`;
  }).join("");
  document.getElementById("facets").innerHTML = html;
}

function pintarVistas(){
  document.getElementById("views").innerHTML = VISTAS.map(v=>
    `<button class="chip ${state.view===v.n?"on":""}" data-view="${v.n}">${v.n}</button>`
  ).join("");
}

function pills(it, max=4){
  const t = tagsDe(it).filter(x=>x!=="sin-clasificar" && x!==DATA.slug).slice(0,max);
  return t.map(x=>`<span class="pill">${x}</span>`).join("");
}

function pintarGrid(){
  lista = DATA.items.filter(match);
  document.getElementById("count").textContent =
    `${lista.length} de ${DATA.items.length} referentes · ${DATA.actualizado}`;
  const g = document.getElementById("grid");
  g.innerHTML = lista.map((it,i)=>{
    const ia = (it.tags.representacion||[]).includes("ia");
    return `<article class="card" data-i="${i}">
      ${ia?'<span class="badge">IA</span>':''}
      <img loading="lazy" src="${it.src}" alt="${tituloDe(it)}">
      <div class="ov"><div class="t">${tituloDe(it)}</div><div class="pills">${pills(it)}</div></div>
    </article>`;
  }).join("");
  const e = document.getElementById("empty");
  if(!lista.length){
    e.style.display="block";
    e.innerHTML = state.view==="Pendientes"
      ? `<b>Todo clasificado.</b><br>Cuando Emilia suba imágenes a la carpeta compartida del Drive, aparecen acá hasta que les asignemos tags.`
      : `<b>Sin resultados.</b><br>Probá quitar algún filtro o buscar otra palabra.`;
  } else e.style.display="none";
}

function aplicarVista(n){
  const preset = (VISTAS.find(v=>v.n===n)||{}).s || {};
  state.view = n;
  state.tags = {};
  Object.entries(preset.tags||{}).forEach(([ax,vals])=>state.tags[ax]=[...vals]);
}

function pintar(){
  pintarFacets(); pintarVistas(); pintarGrid(); escribirHash();
}

function escribirHash(){
  const p = new URLSearchParams();
  p.set("v", state.view);
  if(state.q) p.set("q", state.q);
  Object.entries(state.tags).forEach(([ax,vals])=>{ if(vals.length) p.set(ax, vals.join(",")); });
  if(document.getElementById("lb").classList.contains("on") && lista[actual]) p.set("p", lista[actual].archivo);
  history.replaceState(null,"","#"+p.toString());
}

function leerHash(){
  const p = new URLSearchParams(location.hash.slice(1));
  if(p.get("v")) aplicarVista(p.get("v"));
  if(p.get("q")){ state.q = p.get("q"); document.getElementById("q").value = state.q; }
  AXES.forEach(ax=>{ const v = p.get(ax); if(v) state.tags[ax] = v.split(",").filter(Boolean); });
  return p;
}

document.addEventListener("click", ev=>{
  const f = ev.target.closest("[data-ax]");
  if(f){
    const ax=f.dataset.ax, v=f.dataset.v;
    const arr = state.tags[ax] = state.tags[ax]||[];
    const i = arr.indexOf(v);
    i>=0 ? arr.splice(i,1) : arr.push(v);
    if(!arr.length) delete state.tags[ax];
    if(state.view!=="Todo" && state.view!=="Pendientes") state.view="Todo";
    return pintar();
  }
  const vw = ev.target.closest("[data-view]");
  if(vw){ aplicarVista(vw.dataset.view); return pintar(); }
  const card = ev.target.closest(".card");
  if(card) return abrir(+card.dataset.i);
  const tag = ev.target.closest("[data-tag]");
  if(tag){
    const ax=tag.dataset.ax, v=tag.dataset.tag;
    state.tags = {[ax]:[v]};
    cerrar(); return pintar();
  }
});

document.getElementById("q").addEventListener("input", e=>{
  state.q = e.target.value; pintarGrid(); escribirHash();
});
document.getElementById("clear").addEventListener("click", ()=>{
  state.tags={}; state.q=""; state.view="Todo";
  document.getElementById("q").value=""; pintar();
});
document.getElementById("share").addEventListener("click", async ()=>{
  try{ await navigator.clipboard.writeText(location.href); }catch(e){}
  const t=document.getElementById("toast"); t.classList.add("on");
  setTimeout(()=>t.classList.remove("on"),1400);
});

function abrir(i){
  actual = i;
  const it = lista[i]; if(!it) return;
  const lb = document.getElementById("lb");
  document.getElementById("lbimg").src = it.src;
  const autor = [it.autor, it.anio, it.ciudad].filter(Boolean).join(" · ");
  const tags = ORDEN_EJES.filter(ax=>(it.tags[ax]||[]).length).map(ax=>
    `<div class="lab">${ETIQUETA[ax]||ax}</div><div class="pills">` +
    it.tags[ax].map(v=>`<button class="pill" style="cursor:pointer" data-tag="${v}" data-ax="${ax}">${v}</button>`).join("") +
    `</div>`).join("");
  document.getElementById("lbside").innerHTML = `
    <button class="chip x" id="lx">Cerrar</button>
    <h2 style="padding-right:70px">${tituloDe(it)}</h2>
    <div class="sub">${autor||"Autor / año / ciudad a completar"}</div>
    <button class="chip" id="lcopy">Copiar link de este referente</button>
    ${it.nota?`<div class="lab">Qué me interesa</div><div class="nota">${it.nota}</div>`:""}
    ${tags}
    <div class="links">
      ${it.url?`<a href="${it.url}" target="_blank" rel="noopener">Abrir pin <span>↗</span></a>`:""}
      ${it.fuente_original?`<a href="${it.fuente_original}" target="_blank" rel="noopener">Fuente original <span>↗</span></a>`:""}
      <a href="mailto:?subject=Referente:%20${encodeURIComponent(tituloDe(it))}&body=${encodeURIComponent(it.url||location.href)}">Compartir por mail <span>↗</span></a>
    </div>
    <div class="navbtns">
      <button id="prev">← Anterior</button><button id="next">Siguiente →</button>
    </div>`;
  lb.classList.add("on");
  document.getElementById("lx").onclick = cerrar;
  document.getElementById("prev").onclick = ()=>saltar(-1);
  document.getElementById("next").onclick = ()=>saltar(1);
  document.getElementById("lcopy").onclick = async ()=>{
    try{ await navigator.clipboard.writeText(location.href); }catch(e){}
    const t=document.getElementById("toast"); t.textContent="Link del referente copiado";
    t.classList.add("on"); setTimeout(()=>t.classList.remove("on"),1400);
  };
  escribirHash();
}
function saltar(d){ if(!lista.length) return; abrir((actual+d+lista.length)%lista.length); }
function cerrar(){
  document.getElementById("lb").classList.remove("on");
  const p = new URLSearchParams(location.hash.slice(1));
  p.delete("p");
  history.replaceState(null,"","#"+p.toString());
}

document.addEventListener("keydown", e=>{
  if(!document.getElementById("lb").classList.contains("on")) return;
  if(e.key==="Escape") cerrar();
  if(e.key==="ArrowLeft") saltar(-1);
  if(e.key==="ArrowRight") saltar(1);
});

const hp = leerHash();
if(window.innerWidth<=860) document.getElementById("toggle").style.display="block";
document.getElementById("toggle").onclick = ()=>document.getElementById("aside").classList.toggle("open");
pintar();
const abrirArchivo = hp.get("p");
if(abrirArchivo){
  const idx = lista.findIndex(x=>x.archivo===abrirArchivo);
  if(idx>=0) abrir(idx);
}
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Inventario JSON + imagenes -> dashboard HTML")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--raiz", default=".")
    ap.add_argument("--json", default=None, help="ruta del inventario (default: raw/referentes/<slug>/referentes.json)")
    ap.add_argument("--out", default=None, help="HTML de salida (default: activos/referentes/<slug>/index.html)")
    ap.add_argument("--relativo", action="store_true", help="referenciar imagenes por ruta en vez de embeberlas")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    carpeta = raiz / "activos" / "referentes" / args.slug
    json_path = Path(args.json) if args.json else raiz / "raw" / "referentes" / args.slug / "referentes.json"
    out = Path(args.out) if args.out else carpeta / "index.html"

    data = json.loads(json_path.read_text(encoding="utf-8"))
    faltan = [i for i in data["items"] if not (carpeta / i["archivo"]).exists()]
    items = []
    for it in data["items"]:
        p = carpeta / it["archivo"]
        if not p.exists():
            continue
        it = dict(it)
        it["src"] = it["archivo"] if args.relativo else thumb_b64(p)
        items.append(it)

    payload = {
        "slug": args.slug,
        "titulo": data.get("titulo") or args.slug,
        "board": data.get("board", ""),
        "actualizado": datetime.now().strftime("%Y-%m-%d"),
        "ejes": data.get("ejes") or ["tema", "estrategia", "material", "representacion", "uso", "estado"],
        "items": items,
    }
    html = (PLANTILLA
            .replace("__TITULO__", payload["titulo"])
            .replace("__DATA__", json.dumps(payload, ensure_ascii=False)))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    peso = out.stat().st_size / 1024
    print(f"[ok] {len(items)} referentes -> {out} ({peso:.0f} KB)")
    if faltan:
        print(f"[!] {len(faltan)} fichas sin imagen (se omiten): " +
              ", ".join(i["archivo"] for i in faltan[:8]))


if __name__ == "__main__":
    sys.exit(main())
