---
tipo: indice
fecha_creacion: 2026-10-23
ultima_actualizacion: 2026-10-23
tags: [referentes, indice, vault-visual, pinterest, concurso]
---

# Referentes visuales

> Imágenes de referencia (Pinterest, capturas, Drive) convertidas en un tablero
> navegable por tags. Una imagen se guarda una vez y se encuentra por muchos ejes.

- [[#Qué resuelve]]
- [[#Flujo]]
- [[#Tableros]]
- [[#Publicar y compartir]]
- [[#Comandos]]

## Qué resuelve

Pinterest organiza por tableros: una carpeta y listo. Acá el tablero es una **consulta**:
la misma imagen aparece en todas las vistas que le correspondan sin mover archivos.

Ejes de tag (se consolidan a medida que crece el material):

`tema · estrategia · material · representacion · estado · uso`

## Flujo

1. **Ingesta:** tablero público de Pinterest → `referentes_pinterest.py` (imagen + ficha).
2. **Clasificación:** `raw/referentes/<slug>/tags.csv` (editable en Excel/Sheets).
3. **Publicación:** `referentes_dashboard.py` → un HTML autocontenido.

Emilia puede sumar material subiéndolo a la carpeta compartida: el script detecta
las imágenes nuevas y las deja como `sin-clasificar` hasta que les pongamos tags.

## Tableros

| Slug | Tema | Estado | Referentes |
|---|---|---|---|
| `aixgaudi` | Concurso AIxGAUDI — biomimética, ramificación, topografía | prototipo | 25 |

Cada tablero vive en `activos/referentes/<slug>/` (binarios, fuera de git) y su
inventario en `raw/referentes/<slug>/referentes.json`.

## Publicar y compartir

- **Local:** abrir `activos/referentes/<slug>/index.html`.
- **Online:** arrastrar ese archivo a `app.netlify.com/drop` → URL pública.
- **Vistas:** cada combinación de filtros queda en la URL (`#tema=fachada&material=ladrillo`).
- **Ficha suelta:** `#p=ref-13.jpg` abre un referente puntual para mandar por mail.

## Comandos

```powershell
# traer un tablero publico
P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_pinterest.py --board "<url>" --slug <slug>

# volcar la planilla de tags + detectar imagenes nuevas
P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_tags.py --slug <slug>

# regenerar el tablero
P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_dashboard.py --slug <slug>
```

Notas didácticas: [[scripts/referentes_pinterest_notas|pinterest]] ·
[[scripts/referentes_tags_notas|tags]] · [[scripts/referentes_dashboard_notas|dashboard]]
