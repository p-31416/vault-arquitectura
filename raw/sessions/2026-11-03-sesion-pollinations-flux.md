---
tipo: log
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [sesion, pollinations, flux, imagen-ia, n8n, comfyui, runpod, backlog]
idioma: es
---

# 2026-11-03 — Pollinations flux + guía modelos + backlog RunPod

## Qué se hizo

1. Estado Pollinations: key `sk_` activa en `.env`, test plaza Sagrada con `flux.1-schnell` 401 KB OK.
2. Prompt cáscara mejorado EN + 2 pruebas: `flux.1-schnell` 293 KB masa nervada favorita de Sol, `z-image-turbo` 253 KB canopy ramificado con mejor match brief.
3. Segunda prueba flux interior eye-level 444 KB + prueba `flux.1.1-pro` 1280x704 185 KB onda continua, ambas guardadas en activos.
4. Doc `wiki/glosario/software/pollinations.md`: auth `sk_` vs `pk_`, uso GET/POST, 6 flujos F1-F6 para n8n, comparativa flux vs flux.1, modelos gratis-tier, límites, backlog P1-P4.
5. Límites aclarados: anónimo 1 por vez 45 s, con key exploración amplia en flux, saldo en dashboard.
6. Investigación mejor abierto/cerrado/arquitectura: cerrado top Sunburst + NBP, abierto calidad Qwen-2.1 con licencia research, abierto permisivo Z-Image/Qwen-2512/klein 4B Apache 2.0, 8 GB Klein 3 5.6B, archviz NBP + FLUX.2 Pro, LoRA como capa opcional con ControlNet al frente.
7. Guía `wiki/glosario/software/modelos-imagen-arquitectura.md` creada con tablas y referencias verificadas 200.
8. Revisión tutorial Comfy `flux-2-dev` + `flux-2-klein`: stack 18.3 GB, 3 workflows, pod 24 GB $0.22/0.34. Backlog `30-backlog` ampliado con F6-F8.

## Archivos modificados

- `.env` (entrada `POLLINATIONS_API_KEY`, valor aportado por Sol)
- `wiki/glosario/software/pollinations.md` (creado + ampliado flujos + backlog + pruebas)
- `wiki/glosario/software/modelos-imagen-arquitectura.md` (creado)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas.md` (sección FLUX.2 Dev en RunPod F6-F8)
- `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/` (5 jpg: plaza, flux, zimage, interior, flux11pro)
- `raw/sessions/2026-11-03-sesion-pollinations-flux.md` (este cierre)

## Verificación

- Pollinations GET imagen 200 en 4 modelos, archivos con peso verificado por `Get-Item`.
- Webfetch 200: `gen.pollinations.ai/docs`, `enter.pollinations.ai/keys`, `github.com/QwenLM/Qwen-Image-2.1`, `bfl.ai/blog/flux-3-image-klein`, `deepmind.google/.../nano-banana-2-1`, `docs.comfy.org/tutorials/flux/flux-2-dev`, `docs.comfy.org/tutorials/flux/flux-2-klein`.
- Balance 403 esperado por falta de permiso `account:`, key válida con `pollenBudget: null`.
- Grep + Read previos a cada edit, frontmatter completo en wiki.

## Análisis cerebro-digital

**Topics:** Pollinations `sk_` + flux exploración, prompt cáscara EN, flujos n8n F1-F6, top cerrado vs abierto permisivo, archviz NBP/FLUX.2 Pro, LoRA opcional, FLUX.2 Dev pod 24 GB.

**Entidades:** Pollinations (`flux.1-schnell`, `flux.1.1-pro`, `kontext`, `klein`, `z-image-turbo`) · `gen.pollinations.ai` · `enter.pollinations.ai/keys` · ComfyUI 0.3.72+ · RunPod 3090/4090 · `30-backlog-futuras-pruebas` F6-F8 · `modelos-imagen-arquitectura`.

**Hechos:**
- Sol prefiere masa flux para explorar, z-image para match vidrio, interior para escala humana.
- Stack Dev 18.3 GB avanza en pod 24 GB con flujo probado; Klein 4B destilado abre puerta económica.
- Guía modelos deja decisión lista: explorar flux, cerrar flux.1, anclar kontext con foto, entregar NBP/GPT 2.5.
- Queda para próximo ciclo: F4 kontext con foto real, P2 x3 luces, F6 pod arriba, credencial n8n + test `poll:` vs `or:`.
