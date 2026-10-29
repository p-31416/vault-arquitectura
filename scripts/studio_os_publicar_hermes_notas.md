# Notas · `studio_os_publicar_hermes.py`

> Publica en el agente los archivos de texto que viven **dentro del documento maestro**. Es la herramienta que hace verdadera la regla "un solo documento": el maestro es la fuente y el script copia lo que el agente necesita.

## Para qué sirve

El agente (Hermes) necesita dos cosas que son texto: su **identidad y reglas** (`SOUL.md`) y sus **habilidades** (`skills/*/SKILL.md`). Esas dos cosas están escritas dentro de `proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07.md` (§9.2 y §9.3), marcadas con una línea de comentario HTML.

Este script **extrae** esos bloques y los **publica** dentro del contenedor del agente, en el volumen `/opt/data`. Así el texto se edita en un solo lugar (el documento maestro, versionado en git) y llega al agente sin pasos manuales.

## Cómo se ejecuta

Primero, en modo seguro, para ver qué haría:

```
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_publicar_hermes.py --dry-run
```

Después, la publicación real:

```
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_publicar_hermes.py
```

## Qué hace, bloque por bloque

| Bloque | Qué hace |
|---|---|
| `MARCA` | la expresión regular que reconoce `<!-- archivo: ruta -->` en el maestro |
| `DESTINOS` | el mapa de "ruta en el vault" → "ruta en el contenedor" (`hermes/` se quita, porque en el contenedor no existe) |
| `extraer_bloques()` | recorre el maestro y guarda el contenido de cada bloque marcado |
| `ssh()` | el helper de SSH: si le pasás texto, lo manda por la entrada estándar (así el archivo viaja por el pipe, sin scp ni temporales) |
| `resolver_contenedor()` | **trampa de Swarm**: los contenedores no se llaman `hermes`, sino `hermes.1.tarea`. Por eso primero saca el ID real con `docker ps --filter name=hermes` |
| `publicar()` | `docker exec -i <id> sh -c 'cat > /opt/data/...'` |
| `verificar()` | relee el archivo y muestra tamaño y primera línea |

## Qué esperar

```
Bloques encontrados en el documento maestro:
  hermes/SOUL.md -> /opt/data/SOUL.md  (3.482 caracteres)
  hermes/skills/auditar-documentacion-cad/SKILL.md -> /opt/data/skills/.../SKILL.md  (2.914 caracteres)

Contenedor de Hermes: 7f3c9d2e1f4a
Publicado hermes/SOUL.md -> /opt/data/SOUL.md
  3482 /opt/data/SOUL.md
  # SOUL — Agente del estudio (Studio OS)
```

## Detalles que importan

- **No reinicia nada**: escribe archivos y verifica. El gateway los toma en la próxima sesión.
- **No toca el host**: solo escribe dentro del volumen `/opt/data` del contenedor.
- **No borra**: si un archivo deja de estar en el maestro, el script no lo borra del volumen (queda el anterior). Si eso molesta, se borra a mano.
- **Stdlib solamente**: `argparse`, `re`, `subprocess`, `pathlib`.

## Errores frecuentes

| Síntoma | Causa | Qué hacer |
|---|---|---|
| `No encontre el contenedor de Hermes` | el servicio no está desplegado o se llama distinto | `ssh contabo "docker ps --filter name=hermes"` y ver el nombre real |
| `SSH devolvio 255` | la clave no está accessible | `ssh contabo "echo OK"` a mano; ver [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]] |
| `no tiene bloques publicables` | el maestro no tiene los marcadores `<!-- archivo: ... -->` | revisar §9.2 y §9.3 del maestro |
| El agente no cambia de personalidad | el gateway ya tenía la sesión abierta | reiniciar el servicio: `docker service restart <servicio-hermes>` |

## Qué NO hace (a propósito)

- No edita el documento maestro: solo lo lee.
- No publica secretos: `SOUL.md` y las skills son texto público del estudio.
- No toca `config.yaml`: la configuración del agente se cambia con `hermes config set`, no desde acá.
