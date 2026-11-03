---
tipo: metodologia
codigo: pbk-opencode-linux
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [opencode, linux, terminal, console, vault, replica, github, plan-mode, segunda-pc]
idioma: es
---

# pbk-opencode-linux — Vault con OpenCode en Linux (terminal)

> Playbook para levantar `vault-arquitectura` en una segunda computadora con Linux y trabajar con el agente desde la terminal. Ideal cuando el IDE pesado se traba: OpenCode es un binario único de ~200 MB, sin GPU y sin interfaz gráfica.

- [[#Qué llevar]]
- [[#1 · Requisitos]]
- [[#2 · Instalar OpenCode]]
- [[#3 · Conectar la otra cuenta (Console)]]
- [[#4 · Clonar el vault]]
- [[#5 · Abrir el vault con el agente]]
- [[#6 · Qué viaja y qué queda en la PC principal]]
- [[#7 · Costos bajo control]]
- [[#8 · Troubleshooting]]

Relacionado: [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|cuentas Git/GitHub/OpenCode]] · [[wiki/glosario/interno/pbooks/pbk-instalacion-codex|réplica con Codex en Windows]].

## Qué llevar

- La URL del repo: `https://github.com/p-31416/vault-arquitectura.git` (rama `master`).
- Acceso a `opencode.ai/console` con la cuenta que pone los créditos (la otra cuenta).
- 5 minutos y una terminal.

## 1 · Requisitos

```bash
sudo apt update && sudo apt install -y curl tar git
```

Terminal moderna (la de GNOME alcanza; WezTerm/Alacritty/Kitty/Ghostty rinden mejor con el TUI).

## 2 · Instalar OpenCode

```bash
curl -fsSL https://opencode.ai/v2/install | bash
# cerrar y reabrir la terminal (o: source ~/.bashrc)
opencode --version
```

Instala en `~/.opencode/bin/opencode`. Para actualizar: `opencode upgrade`. Ojo: `opencode.ai/install` (sin `/v2`) instala la v1 vieja; la vigente es `/v2/install`.

## 3 · Conectar la otra cuenta (Console)

Zen se retiró el 02/11/2026 y ahora se llama **Console**: mismos créditos pay-as-you-go, misma key. Con la otra cuenta: `opencode.ai/console` → generar API key → en la terminal:

```bash
opencode auth login
```

Elegir el provider de OpenCode Console y pegar la key. Verificar con `opencode auth list`.

## 4 · Clonar el vault

```bash
mkdir -p ~/repos && cd ~/repos
git clone https://github.com/p-31416/vault-arquitectura.git
cd vault-arquitectura
```

## 5 · Abrir el vault con el agente

```bash
opencode
```

Adentro, `Tab` cambia al agente **plan** (solo lectura: analiza sin editar ni ejecutar). El `AGENTS.md` del vault se levanta solo al arrancar. Preguntas de arranque:

- `¿qué es este vault y cómo está organizado?`
- `resumime el estado del proyecto Studio OS según VISION.md`
- `¿qué dashboards hay en presentacion/ y qué muestra cada uno?`

Comandos útiles: `/models` (elegir modelo) · `Esc` (interrumpir) · `/exit` (salir). `/init` no hace falta: el `AGENTS.md` ya existe y se commitea.

Para una sola pregunta sin abrir el TUI: `opencode run "¿qué contiene este vault sobre X?"`.

## 6 · Qué viaja y qué queda en la PC principal

- **Viaja con git**: todo el texto, los 3 HTML de `presentacion/` (imágenes embebidas en base64, se ven con doble clic) y los JSON del set PI.
- **Queda acá**: `activos/` (gitignored: PNG full-res, renders, massing, videos). Los `![[activos/...]]` de los `.md` se ven rotos en Linux: esperado, el detalle vive en cada `raw/sessions/`.
- ComfyUI, Rhino y AutoCAD no corren en esa máquina: es puesto de lectura y consulta.

## 7 · Costos bajo control

Cada respuesta gasta créditos Console de la cuenta conectada. Para leer y preguntar alcanza un modelo liviano (`/models` → familia Haiku o similar). Dejar los modelos frontera para trabajo que lo pida.

## 8 · Troubleshooting

| Síntoma | Vía |
|---|---|
| `opencode: command not found` tras instalar | cerrar y reabrir la terminal, o `source ~/.bashrc` (el instalador agrega `~/.opencode/bin` al PATH) |
| `402` / sin créditos | recargar balance en `opencode.ai/console` (Settings → Billing) |
| El agente quiere escribir | pasar a **plan** con `Tab`, o responder `n` al pedido de permiso |
| Links `activos/` rotos en Obsidian | esperado en la réplica (ver §6); pedir el dato al agente o abrir el HTML de `presentacion/` |
