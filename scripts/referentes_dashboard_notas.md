---
tipo: metodologia
fecha_creacion: 2026-10-23
ultima_actualizacion: 2026-10-23
tags: [referentes, dashboard, scripts, vault-visual, publicacion]
---

# `referentes_dashboard.py` — notas

> Convierte el inventario JSON + las imágenes en **un solo HTML** navegable por tags.

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_dashboard.py --slug aixgaudi
# -> activos/referentes/aixgaudi/index.html
```

## Un archivo, no un servidor

```python
# NOTA ES: cada imagen se convierte a texto base64 y se pega DENTRO del HTML.
# Resultado: un archivo de ~2,4 MB que se abre con doble clic, se manda por mail
# o se arrastra a Netlify Drop. No necesita servidor, ni carpeta, ni internet.
it["src"] = thumb_b64(p)
```

Con `--relativo` en vez de base64 se referencia la imagen desde el disco (más liviano,
sirve mientras se edita local; para compartir conviene el archivo único).

## Tablero = consulta, no carpeta

```js
// NOTA ES: los filtros son estado, no ubicaciones. Una imagen no "está" en un tablero:
// cumple o no cumple los filtros activos. Dentro de un eje suma (fachada OR piel),
// entre ejes intersecta (tema fachada AND material ladrillo).
for(const [ax,vals] of Object.entries(state.tags)){
  if(!vals.length) continue;
  if(!vals.some(v=>(it.tags[ax]||[]).includes(v))) return false;
}
```

Ejes: `tema · estrategia · material · representacion · estado · uso`.

## Cada vista es un link

```js
// NOTA ES: el estado de navegación se escribe en el hash de la URL. Copiar la barra de
// direcciones comparte exactamente la misma vista con Emilia, sin cuentas ni permisos.
history.replaceState(null,"","#"+p.toString());
```

Ejemplos:

- `#v=Biomimética` → vista guardada
- `#tema=fachada&material=ladrillo` → consulta propia
- `#p=ref-17.jpg` → abre la ficha de ese referente

## Navegación tipo Pinterest

- Muro masonry con `column-count` (respeta proporciones, no recorta).
- Hover muestra obra + tags.
- Clic abre la ficha: imagen grande, nota, tags clicables, link al pin y a la fuente.
- Flechas del teclado recorren la selección filtrada.

## Publicar online (sin servidor propio)

1. Generar el HTML.
2. Arrastrar el archivo a `app.netlify.com/drop`.
3. Netlify devuelve una URL pública.
4. Para actualizar: regenerar y volver a arrastrar (misma URL con deploy nuevo).

Los binarios siguen fuera de git: se publica el HTML autocontenido, no la carpeta `activos/`.
