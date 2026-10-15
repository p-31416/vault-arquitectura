# Notas ES — `import_drive_reuniones.py`

Qué hace, en una línea por bloque:

- **Constantes**: define dónde está el vault, las 2 carpetas de Drive Stream (`Reuniones-Internas`, `Reuniones-Clientes`) y el archivo de estado `.import-state.json` que evita duplicar.
- **Regex**: `CALL_RE` saca el `call_id` de las URLs `fathom.video/calls/...`; `DATE_FIELD_RE` y `REC_FIELD_RE` leen los campos `- Fecha:` y `- Recording ID:` del `.md`; `DATE_FILE_RE` usa la fecha del nombre de archivo como respaldo.
- **`load_state` / `save_state`**: lee y guarda el JSON que mapea `carpeta/archivo.md` → nombre importado.
- **`dest_name_for`**: arma el nombre destino con la convención del vault `YYYY-MM-DD-<call_id>.md`; si no hay `call_id`, usa `rec<recording_id>`; último recurso, el nombre original.
- **`main`**: recorre los `*.md` de ambas carpetas; salta los ya importados; copia verbatim (sin tocar el contenido, `raw/` es append-only); nunca pisa un destino existente; con `--dry-run` solo informa sin copiar.
- **Uso**: `python scripts/import_drive_reuniones.py` (real) o con `--dry-run` (simulacro).
