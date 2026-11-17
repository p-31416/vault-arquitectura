---
tipo: workflow
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp09, workflow, sub-workflow, cloudflare, schnell, tool]
idioma: es
---

# IMG Generar CF (`z0qOpgY5HT1kXoUL`)

> Sub-workflow tool del agente: genera con schnell vía Cloudflare y devuelve miniatura visible. Publicado (requisito para uso como tool).

- **URL**: https://n8n.pitau.tech/workflow/z0qOpgY5HT1kXoUL · **Proyecto**: `pWOSkiVhnAWt5tSi`
- **Trigger**: `Entrada Imagen` (Execute Workflow Trigger) — input `prompt` (string).
- **Credencial**: `cf-WorkersAI` (`cLUDLsbsbLF7fj5F`) en nodo `CF schnell`.

## Nodos

1. **Entrada Imagen** — recibe `prompt` del agente.
2. **CF schnell** — POST JSON `{prompt, steps: 4}` a `/ai/run/@cf/black-forest-labs/flux-1-schnell`. Sin seed (el schema lo rechaza).
3. **B64 a binario** (Code) — `result.image` → binario `data`.
4. **Miniatura** (Edit Image) — resize máximo 384px, jpeg q60.
5. **Thumb b64** (Code) — binario → base64.
6. **Armar respuesta** (Set) — `{image_data_uri, usage_json, motor: cloudflare-schnell}`.

## Costo medido

1024² ≈ **172.8 Neurons** (~58/día dentro de la cuota 10k).

## Versiones

- v1 `CF con miniatura visible v1` (creación + credencial existente asignada vía setNodeCredential).
