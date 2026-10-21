# NOTA ES: `import_fathom_ppi_manual.py` línea por línea

- **Docstring:** qué replica (plantilla y nombre del Fathom Core) y uso con el Python de `comfyenv`.
- **`VAULT/RAW/DRIVE/STATE`:** rutas fijas. `RAW` es el crudo del vault, `DRIVE` es la carpeta
  `G:\Mi unidad\OS-Emilia\Reuniones-Internas`, `STATE` es `.import-state.json` (idempotencia).
- **`build_md(item)`:** arma el `.md` con `## Datos` (fecha, recording ID, URL, participantes,
  clasificación Internas, origen manual), `## Resumen` (texto Fathom verbatim),
  `## Action items` (con timestamp y responsable) y `## Transcripcion` verbatim con
  `[timestamp] hablante:` por turno. Nada se resume ni se edita: el crudo no se toca.
- **`main()`:** lee el JSON de lista Fathom, por cada reunión calcula el nombre
  `fecha_emilia-proyectopi_recordingid.md`, salta si ya existe (salvo `--force`),
  escribe en `raw/`, copia a Drive y registra en el state.
- **Cuándo usarlo:** cuando haya reuniones en el Fathom Proyecto Pi que el cron de Emilia
  no trae (ventana 26h, otra cuenta). El Google Doc queda para el Fathom Core o carga manual.
