# NOTA ES: `leantime_rpc.py` línea por línea

- **Docstring:** por qué este script existe (el MCP `/mcp` de Leantime responde `initialize` pero
  publica **0 tools**; la API JSON-RPC sí expone los métodos del repositorio y es la vía que el
  vault ya usó para los milestones 443-457). Da el comando de uso.
- **`BASE` / `ENV`:** endpoint único `POST /api/jsonrpc` y ruta del `.env` con la credencial.
- **`PAUSA` / `ESPERA_429`:** la API tira *"Too many requests per minute"*; entre llamadas se espera
  1,6 s y ante un 429 se espera 20 s antes de reintentar (6 intentos).
- **`_token()`:** lee `LEANTIME_TOKEN` del `.env`. **El valor nunca se imprime ni se loguea.**
- **`rpc(metodo, params)`:** arma el sobre JSON-RPC 2.0, lo manda con `x-api-key` y devuelve el
  JSON completo. Ante 429 reintenta; ante otro error HTTP devuelve el código + un fragmento del
  cuerpo; ante excepción de red devuelve `{"err": ...}`.
- **`resultado(metodo, params)`:** envoltorio que devuelve solo la clave `result` (o el error bajo
  `__error`) para no repetir el parseo en cada llamada.
- **`__main__`:** modo `getAllLeantime` (imprime el `result` de un método de lectura, con params
  opcionales en JSON) o modo directo (manda un método y sus params e imprime la respuesta entera).
- **Cuándo usarlo:** para leer estado (proyectos, tickets, milestones, sprints) y para crear
  milestones, cards y subtasks. Los Goals no están expuestos por la API: se crean en la UI.
- **Higiene:** el token viaja solo en el header; el repo y el vault guardan nombres e IDs, nunca
  secretos.
