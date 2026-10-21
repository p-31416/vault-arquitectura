# Notas de `inyectar-puerta-temas-dashboard.py` — la puerta del dashboard general

## Qué resuelve

El dashboard `dashboard-mes1-emilia.html` es la **puerta de entrada** al resto del vault (los otros 4 dashboards ya lo enlazan). Le faltaba lo que se pedía: **un solo archivo desde donde ver los 6 temas y dónde está cada cosa** (fuentes · agentes Telegram · CAD/SET · Comfy · Leantime · estudio) + los 3 pendientes de la reunión con Emilia.

## Por qué un script y no editar el HTML a mano

El dashboard ya se regenera con `scripts/build-dashboard-semanas.py` (que inyecta la sección de semanas y de despliegue IA con el mismo patrón: ancla + borrado por regex + inyección). Si la puerta estuviera a mano, la próxima vez que corra ese script se perdería. Con este script, la puerta **se reinyecta sola**.

## Cómo funciona

1. **Ancla de inserción**: `<div class="k" style="margin-top:26px">Eficiencia = Resultados / Recursos</div>` → la puerta queda entre los números del mes y el pitch del 2X (arriba, no al final).
2. **Marcadores** `<!-- PUERTA-TEMAS -->` … `<!-- /PUERTA-TEMAS -->`: antes de escribir, el bloque anterior se borra con un regex → **correrlo dos veces deja el HTML igual** (verificado: 36541 → 36541 → 36541 bytes).
3. **Pestaña en el nav**: `<a href="#temas">Temas</a>` antes de "Sesiones" (idempotente).
4. **Ruta del doc de la reunión en los `toplinks`**: se busca **solo dentro del bloque `<p class="toplinks">`** — si se comprobara la ruta en todo el archivo, daría falso positivo (la ruta también está dentro de la sección de la puerta) y nunca se agregaría.

## Reglas de contenido que respeta

- **Las rutas del vault van como texto** (`<code>`), no como links: se van a ver en otra computadora, donde lo que sirve es el camino dentro del vault (se abren en Obsidian). Los **dashboards sí son links** (son HTML autocontenidos que viajan con el repo).
- Los `.md` de la puerta apuntan a las **fichas y specs principales** de cada tema, no a todo.
- Los **3 pendientes** (chat_id de Emilia · dirección del estudio · calendario) van al final de la sección, con el detalle de dónde tocar.

## Uso

```powershell
# ver qué cambiaría, sin escribir
P:\Anaconda\envs\comfyenv\python.exe scripts\inyectar-puerta-temas-dashboard.py --dry

# inyectar (idempotente)
P:\Anaconda\envs\comfyenv\python.exe scripts\inyectar-puerta-temas-dashboard.py

# comprobar el CSS del HTML resultante
P:\Anaconda\envs\comfyenv\python.exe scripts\check-dashboard-css.py dashboard-mes1-emilia.html
```

## Para cambiar el contenido

Los temas y los pendientes están en dos listas al principio del script (`TEMAS` y `PENDIENTES`): se editan ahí y se vuelve a correr. El HTML no se toca a mano.

## Verificación hecha (21/10)

- Inyección idempotente: 32318 → 36494 bytes, y dos corridas más sin cambios.
- `check-dashboard-css.py`: 0 clases sin estilo.
- Captura con Chrome headless: la sección se ve bien (6 tarjetas en 3 columnas + franja de pendientes), el nav muestra la pestaña "Temas" y el resto del dashboard quedó intacto.
