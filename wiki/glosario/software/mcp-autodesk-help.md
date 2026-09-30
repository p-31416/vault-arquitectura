---
tipo: software
software: mcp-autodesk-help
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [glosario, software, mcp, autodesk, ayuda-oficial, opencode]
---

# MCP autodesk-help

> Servidor MCP remoto de la ayuda oficial Autodesk (110+ productos). Solo lectura, sin autenticación en este vault.

- [[#Resumen]]
- [[#Endpoint y configuración]]
- [[#Herramientas]]
- [[#Parámetros de búsqueda]]
- [[#Demo en español]]
- [[#Límites]]
- [[#Estado y verificación]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

Autodesk expone su sistema de ayuda como MCP público. Desde el vault solo se usa para **resolver dudas con fuente primaria** durante el estudio o el curso C1/C2. No edita nada: trae extractos y URLs oficiales para que el agente cite con respaldo.

## Endpoint y configuración

- URL: `https://developer.api.autodesk.com/knowledge/public/v1/mcp`
- Tipo: `remote`, sin auth (HTTP 200 verificado).
- Timeout declarado en `opencode.json`: 30000 ms (el default 5000 queda corto para remoto).

Bloque mínimo en `opencode.json`:

```json
"autodesk-help": {
  "type": "remote",
  "url": "https://developer.api.autodesk.com/knowledge/public/v1/mcp",
  "enabled": true,
  "timeout": 30000
}
```

## Herramientas

| Herramienta | Para qué |
|---|---|
| `get_available_products` | Lista el catálogo canónico con `product_name`, `product_code` y `release_codes` |
| `search_help_content` | Busca por palabra clave en ayuda de producto + versión + idioma |

## Parámetros de búsqueda

| Parámetro | Tipo | Notas |
|---|---|---|
| `query` | string | Hasta 1500 chars, keyword-rich, idioma del `locale` |
| `locale` | enum | 38 locales disponibles (`es_ES`, `en_US`, `pt_BR`, `fr_FR`, `de_DE`, `it_IT`…) |
| `product_code` | enum | Código corto (`ACD` AutoCAD, `RVT` Revit, `CIV3D` Civil 3D, `3DSMAX`…) — preferirlo sobre `product_name` |
| `release_code` | string | Año validado por producto (ej `2027` para ACD) |
| `sources` | array | Opcional: `["product_documentation"]` o `["sfdc_articles"]` para acotar |
| `max_results` | int | 1–50, default 5 |

Recomendación: pasar `product_code` + `release_code` evita ambigüedad entre productos que comparten nombre (`AutoCAD` vs `AutoCAD LT`).

## Demo en español

Prompt útil: `Buscá en la ayuda de AutoCAD 2027, en es_ES, cómo crear un bloque dinámico con estados de visibilidad. use autodesk-help`

Devuelve 5 resultados típicos:
1. Tutorial paso a paso del producto.
2. Cuadro de diálogo del comando (ej `ESTADOVISBLOQUE`).
3. Concepto general (`Acerca del control de visibilidad...`).
4–5. Artículos de soporte (sfdc_articles) cuando hay issues conocidos.

## Límites

- **Solo lectura.** No ejecuta, no dibuja, no consulta tu licencia.
- Devuelve **extractos**, no la página completa: para profundizar abrir la `url` oficial.
- Documentación oficial carga como app JS en algunos `help.autodesk.com/...ADSKMCP_*`: vía MCP funciona, vía `webfetch` puede devolver solo shell.
- Algunos directorios mencionan OAuth: si el cliente lo pide, abre navegador.

## Estado y verificación

- ✅ conectado (verificado `mcp list` 2026-09-27).
- `opencode mcp debug autodesk-help` → `HTTP 200 OK, no auth required or already authenticated`.

---

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/software/mcp-autocad|mcp-autocad]]
- [[wiki/glosario/software/autocad|autocad]]

## Referencias

- Endpoint MCP: https://developer.api.autodesk.com/knowledge/public/v1/mcp (verificado 200 vía MCP 2026-09-27)
- Doc oficial setup: https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html (verificado URL viva, carga como app JS)
- Directorio MCP: https://mcpservers.org/servers/autodesk-product-help-mcp (verificado 2026-09-27 — 200)
- OpenCode MCP servers: https://opencode.ai/docs/mcp-servers/ (verificado 2026-09-27 — 200)
- Anuncio: https://adsknews.autodesk.com/en/news/product-help-mcp-server/
