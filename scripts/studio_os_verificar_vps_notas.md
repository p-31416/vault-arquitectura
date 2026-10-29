# Notas · `studio_os_verificar_vps.py`

> Script **de solo lectura**: pregunta al VPS cómo está y arma un informe. No instala, no reinicia y no modifica nada.
> Vive acá: `scripts/studio_os_verificar_vps.py` · se ejecuta desde la PC de desarrollo.

## Para qué sirve

Es el **primer paso de F0** ([[proyectos/MVP_07-studio-os-sistema/02-ft-mvp_07|02-ft-mvp_07]]): deja el **baseline** del servidor antes de meter Hermes. Con ese número se decide si el VPS aguanta los 3 GB del agente o si hay que liberar RAM primero.

El script no decide nada: **muestra**. La decisión la tomamos juntos con el número a la vista.

## Cómo se ejecuta

```
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py
```

Variantes:

```
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py --host contabo
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py --json raw/reports/vps-baseline-2026-10-29.json
```

El alias `contabo` sale de tu configuración SSH (`C:\Users\Solch16\.ssh\config`): apunta a `89.117.73.109` con la clave `P:\.ssh\id_ed25519`. La clave **no** está en el vault y nunca se copia ahí.

## Qué hace, bloque por bloque

| Bloque del script | Qué pregunta al VPS | Para qué lo miramos |
|---|---|---|
| `COMANDO_REMOTO` | arma el bloque de comandos de lectura que viaja por SSH | los marcadores `===MEM===` etc. son los que permiten separar la respuesta al parsear |
| `parsear_bloques()` | corta la salida por los marcadores | devuelve un diccionario con un bloque por dato |
| `a_mb()` | convierte "736MiB" / "1.5GiB" / "800kB" a megabytes | para poder sumar la memoria de todos los contenedores |
| `parsear_memoria()` | lee `free -m` | qué nos importa es **available** (incluye la caché que el sistema puede liberar), no `free` |
| `parsear_contenedores()` | lee `docker stats --no-stream` | ver quién pesa de verdad |
| `parsear_disco()` | lee `df -h /` | espacio del sistema de archivos raíz |
| `veredicto()` | compara la RAM disponible con los 3 GB que pide Hermes | devuelve un veredicto en texto, no una acción |
| `imprimir_texto()` | arma la salida legible | la que vas a leer en la terminal |

## Qué esperar

Con el estado medido el 2026-10-28 (02:10 AR) el resultado era:

```
RAM total          : 7941 MB
RAM usada          : 3082 MB
RAM disponible     : 4858 MB
Swap               : 0 / 2047 MB
Disco raíz         : 23G usados de 72G (31%)
CPU                : 4 núcleos · load average: 0.15, 0.16, 0.06
...
VEREDICTO: OK: entra Hermes con límite de 3 GB y queda margen
```

Si al ejecutarlo el veredicto dice **"NO entra"**, no se instala nada: primero se libera RAM (Chatwoot son ~945 MB y es el candidato natural si no está en uso) o se amplía el VPS.

## Detalles que importan

- **`docker stats --no-stream`** toma una foto puntual: no deja el comando colgado esperando. Es lo que permite que el script termine siempre.
- **El timeout es de 60 segundos**: si el VPS no responde, el script corta con error en vez de quedar esperando.
- **No usa `paramiko` ni ninguna librería extra**: llama al `ssh` del sistema con `subprocess`. Así el script corre con cualquier Python 3.8+ y no hay nada que instalar.
- **Los contenedores de EasyPanel tienen nombres largos** (`pitautech_chatwoot.1.abc123…`) porque es Docker Swarm: eso es normal, no está roto.

## Errores frecuentes

| Síntoma | Causa | Qué hacer |
|---|---|---|
| `No se encontró el comando ssh` | PATH sin OpenSSH | usar Git Bash o instalar OpenSSH |
| `SSH devolvió error 255` | la clave no está accessible o cambió el host | `ssh contabo "echo OK"` a mano; ver [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]] |
| `Permission denied (publickey)` | permisos de la clave en Windows | la clave debe ser solo lectura para tu usuario |
| Tarda mucho | el VPS está saturado | el timeout corta a los 60 s; repetir con `--host` |

## Qué NO hace (a propósito)

- No instala Tailscale, no crea servicios, no reinicia nada.
- No lee ni escribe archivos del vault.
- No manda correo ni avisa a nadie.

Si algún día necesitás que este script haga algo más, primero se escribe en el plan y después en el código: este es el **primer** script del sistema y tiene que ser el más aburrido de todos.
