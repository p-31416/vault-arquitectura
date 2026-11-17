---
tipo: workflow
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp09, workflow, sub-workflow, cloudflare, klein, edicion, tool]
idioma: es
---

# IMG Editar CF (`oNRtmK7lSesgx3cQ`)

> Sub-workflow tool del agente: edita una imagen vía klein-4b multipart (hasta 1 ref por llamada) y devuelve miniatura visible. Publicado.

- **URL**: https://n8n.pitau.tech/workflow/oNRtmK7lSesgx3cQ · **Proyecto**: `pWOSkiVhnAWt5tSi`
- **Trigger**: `Entrada Editar` — inputs `image_url` (string, pública) + `prompt` (string, instrucción conserva+cambia).
- **Credencial**: `cf-WorkersAI` (`cLUDLsbsbLF7fj5F`) en nodo `CF klein edit`.
- **Grupo canvas**: `Edición klein` (7 nodos no-trigger).

## Nodos

1. **Entrada Editar** — `image_url` + `prompt` del agente.
2. **Bajar imagen** — GET con `responseFormat: file` → binario `data`.
3. **Achicar ref** (Edit Image) — resize máximo 512px (límite Workers AI: refs <512px).
4. **CF klein edit** — POST **multipart** (`bodyParameters` con `parameterType`: prompt/width/height `formData` + `input_image_0` `formBinaryData`). JSON rechazado por CF (5006). Steps fijo 4.
5. **B64 a binario** → **Miniatura** 384 → **Thumb b64** (igual que IMG Generar CF).
6. **Armar respuesta** — `{image_data_uri, usage_json, motor: cloudflare-klein-edit}`.

## Lección técnica

`bodyParameters` con `parameterType` es la forma correcta del multipart en n8n (verificado en docs + runtime). La estructura `parameters.parameters` valida en schema pero CF nunca recibe el prompt ("prompt is required").

## Costo medido

~125–175 Neurons por edit (~80/día). klein-9b: error 3043 el 2026-11-12, reintentar.

## Versiones

- v1 creación + `Diagnóstico` (prompt fijo) + `Multipart vía bodyParameters` + `Credencial real + grupo canvas` + publish.
