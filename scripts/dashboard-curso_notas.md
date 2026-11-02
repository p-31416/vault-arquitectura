# dashboard-curso.py — notas línea por línea

> Archivo paralelo didáctico: cada bloque del script explicado para aprender
> Python leyéndolo. Convención del vault: `sé leerlo`.

## Idea general

La galería (`galeria-renders.py`) ya resolvió lo difícil: leer PNGs, plantilla
HTML con mosaico/lienzo/facetas/Polaroid y auto-refresh. Este script **reusa**
esa plantilla y le hace **cirugía con anclas exactas**: cada cambio exige
encontrar un texto del original una sola vez. Si la galería evoluciona y un
ancla cambia, el script falla con mensaje claro en vez de generar un tablero
roto a medias.

## Bloques

- **`cargar_galeria()`** — `importlib.util.spec_from_file_location` carga un
  `.py` por ruta aunque su nombre tenga guiones (no se puede `import` directo).
  Devuelve el módulo: `gal.HTML`, `gal.servir`, `gal.slug`, `gal.tipo_de`,
  `gal.base_de`, `gal.tono_de`, `gal.cargar_indexador()`.
  # NOTA ES: `spec.loader.exec_module(mod)` ejecuta el archivo importado; como
  # galeria-renders.py protege su `main()` con `if __name__ == "__main__"`, al
  # importarlo no genera nada. Solo importamos definiciones.
- **`FLUJOS` / `LINKS`** — los 7 módulos con video (área de participantes, con
  login), transcripción (ruta del vault), workflow GX, estado y **notas de qué
  se puede cambiar**. Solo el módulo 1 tiene workflow real; el resto marca
  `pendiente` y el panel lo muestra así.
- **`LORAS`** — catálogo filename → {url CivitAI, trigger, observar}.
  Fuente de verdad: `wiki/glosario/software/lora-locales-comfyui.md` (URLs,
  triggers, ranks) + sidecars `.civitai.json` (versiones exactas de archisketch
  y markerhandsketch). "Observar" dice qué característica mirar al repasar.
- **`construir_filas()`** suma `lora_info`: cruza el primer LoRA del PNG con
  `LORAS` y arrastra `strength` desde la metadata (la que la galería ya muestra
  como `@ 0.8`). Sin LoRA del catálogo, `lora_info` es `None` y la caja se oculta.
- **`construir_filas()`** suma `workflow`: ruta relativa del `.json` del grafo
  (campo `workflow` del manifiesto, ej. `workflows/matriz-M01.json`). La
  Polaroid lo muestra en `#wf-box` como link de descarga (misma carpeta del
  sitio, sin backend). Sin workflow, título y caja se ocultan.
- **Cirugía extra (2 anclas más, total 15)**:
  - HTML: tras `#notas-box`, `<h3 id="lora-titulo">` + `<div id="lora-box">`.
  - JS: tras el render de notas, arma la caja con concatenación (`+`, no
    backticks anidados) — nombre @ strength, trigger, qué observar y link de
    descarga; si no hay `lora_info`, oculta título y caja (`display:none`).
  # NOTA ES: en el `.py` se escribe `\\n` para que al JS llegue `\n`: un salto
  # de línea REAL dentro de un literal `"..."` del JS sería error de sintaxis.
- **`inj(plantilla, ancla, reemplazo)`** — `str.count(ancla)` debe dar 1;
  si no, `SystemExit` con el ancla recortada. Es el corazón honesto del script:
  falla fuerte en vez de adivinar.
- **`plantilla_curso(gal)`** — los 13 reemplazos, en orden:
  1. título de la pestaña y de la barra + botón `← Galería` a `index.html`;
  2. `EJES`: entran `modulo` y `flujo`, salen `workflow` y `tags`; se inyectan
     `FLUJOS` y `LINKS` como JSON (`__FLUJOS__`, `__LINKS__`);
  3. el desplegable Agrupar empieza en `módulo`; el estado inicial también;
  4. `seccionDe()` aprende los casos `modulo`/`flujo` (se suma, no se reescribe);
  5. el contador dice "repasadas", no "renders";
  6. **fix `__i`/`__k`**: la galería numera la imagen por posición en la vista
     filtrada pero el mapa `IMG` se numera al generar → con filtros activos se
     ve la imagen de otra fila. Aquí cada fila trae su clave estable `__k`.
  7. el sondeo pasa a `curso-datos.json` (si sondeara `datos.json`, el tablero
     se recargaría con la versión de la galería general);
  8. la Polaroid suma `#notas-box` bajo el prompt;
  9. CSS extra: notas, panel `#flujos` (fijo a la derecha, como `#facetas` a la
     izquierda), tarjetas de flujo;
  10. botón `Flujos` en la barra + `<div id="flujos">` oculto por defecto;
  11. `pintarFlujos()`: fuentes del concurso + una tarjeta por módulo (video,
      transcripción, workflow GX o "pendiente", notas);
  12. arranque: `pintar(); pintarFlujos();`.
  # NOTA ES: el JS inyectado usa template literals con `${...}` dentro de un
  # string Python normal — no hay f-string, así que nada se interpola en Python.
  # El `\\n` dentro del reemplazo de la Polaroid deja `\n` real en el JS final.
- **`construir_filas()`** — por cada entrada del manifiesto: metadata del PNG
  vía el indexador (`fila_de` + bloques tEXt `prompt` → grafo → `tipo_de`,
  `base_de`, `clases`, `hsl`) y encima la curaduría (`modulo`, `flujo`,
  `titulo`, `notas`). La curaduría manda: lo escribe el equipo al repasar.
- **`copiar_y_generar()`** — copia a `img-curso/NNN_slug.png`, asigna `__k`,
  escribe `curso.html` (plantilla + 5 reemplazos `__X__`) y `curso-datos.json`
  (versión = sello de tiempo para el sondeo).
- **`sincronizar_workflows()`** — copia cada `workflow_fuente` a la misma
  carpeta con el nombre `workflow_gx`. Compara bytes: si ya está al día no
  toca nada. Ese es el mecanismo "ver en Comfy": la pestaña Workflows del
  sidebar lista esos JSON.
- **`firma()`** — huella del manifiesto + mtimes de las imágenes para el modo
  `--serve` (vigila cada 15 s y regenera solo si algo cambió).
- **`manifiesto_inicial()`** — si no existe `curso.json`, lo crea con M01
  (baseline) y M03 (verificación visual hecha). Después crece a mano: agregar
  una fila y regenerar.
- **`TEMA` + `construir_curso()`** — solapa Curso 1:1 del tablero Miro: cada
  entrada tiene su tarjeta (qué es, a qué refiere, módulo, dónde corre) con
  lista de links. Links SOLO con HTTP 200 verificado (CSV, inventario Miro,
  los 3 del curso); lo demás queda "ver Miro". Clic en tarjeta → fullscreen
  (`abrirCarta` + overlay `#carta-full`, cierra con ✕, fondo o Escape).
- **Cirugía de solapas (5 anclas más)**: botones Repasadas/Curso en la barra,
  `<div id="curso-panel">` de área completa, `CURSO`/`TEMA` como JSON,
  `pintarCurso()` (banner del tema + tarjetas agrupadas por categoría con
  badge de color por dónde corre) + `solapa()` que alterna las vistas, y
  `pintarCurso()` en el arranque.
- **`sincronizar_workflows()` + `aplicar_anotaciones()` + `huella_contenido()`**
  — el sync escribe la copia GX solo si falta o si la fuente cambió (huella
  del grafo SIN anotaciones: quita nodos `GX ·` y títulos gestionados). Tus
  movimientos en el canvas sobreviven a la regeneración. Al escribir, hornea:
  títulos editoriales en los 7 nodos + 4 notas `MarkdownNote` amarillas
  (qué es fijo, dónde entra el LoRA, dónde se calibra, resolución).
  # NOTA ES: `Note`/`MarkdownNote` son nodos de FÁBRICA del frontend
  # (sin custom nodes): fuente verificada en el bundle instalado
  # `comfyui_frontend_package/static` — `src/extensions/core/noteNode.ts`
  # dice `isVirtualNode = true` con widget `text` multiline/markdown y
  # `serialize_widgets = true`. Forma serializada: `type`, `title`,
  # `properties.text` y `widgets_values: [texto]`, sin inputs/outputs.
  # El validador los reporta como tipos faltantes (ESPERADO: no existen en
  # el backend). Verificado 2026-10-30: la conversión librería→API
  # (`get_workflow`) SUELTA los nodos `GX ·` sola — el grafo encolado sale
  # con los 7 nodos pelados y corre sin tocar nada (render WF04-1.0.0_00005_
  # OK, seed 42). Solo un POST directo del UI-JSON a /prompt los arrastraría.
- **`main()`** — CLI (`--out`, `--curso`, `--serve`, `--una-vez`), una pasada,
  informe por terminal. Sin `--serve` termina; el servidor de la galería que
  ya corre (8890) sirve `curso.html` igual porque vive en la misma carpeta.
- **`SEGUNDOS` + `EJES_MATRIZ` + solapa Matriz** — la matriz de testeo como
  gráfico: 6 ejes (steps, cfg, resolución, sampler, LoRA·fuerza, LoRA·identidad)
  con lo MEDIDO (miniaturas + segundos, clic = Polaroid) contra el ÓPTIMO
  (bandera ▼; banda sombreada = rango de trabajo 0.6–0.9 en fuerza).
  `mid` (M01…) y `segundos` viajan en cada fila; `MATRIZ` se inyecta como JSON.
  La intensidad del LoRA también se lee en la tarjeta (pill `@ 0.8` en mosaico
  y lienzo; la Polaroid ya la mostraba).

## Cómo agregar una repasada (flujo de trabajo)

1. Correr el flujo en ComfyUI y elegir la imagen.
2. Agregar una fila a `activos/web/galeria/curso.json`: archivo, módulo,
   flujo, título y **notas de qué se puede cambiar**.
3. Regenerar: `P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-curso.py`
4. Recargar `http://127.0.0.1:8890/curso.html` (o esperar 12 s: se recarga solo).
