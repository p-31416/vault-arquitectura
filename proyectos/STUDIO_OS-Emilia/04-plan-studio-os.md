---
tipo: metodologia
fecha_creacion: 2026-08-27
ultima_actualizacion: 2026-08-27
tags: [studio-os, plan, arquitectura-sistemas, emilia-pimenta]
estado: borrador
version: 0.1
origen: 03-cuestionario-plan-studio-os.md (30/30 respuestas 2026-08-27)
---

# Plan Studio OS — Emilia Pimenta (piloto) + base replicable PI

> **Mandato:** PI 100% protegida, modelos con licencia comercial permisiva, sin entrenamiento con datos del estudio. IA local prioritaria (túnel) + RunPod solo si se aclara retención. Objeción #1: "no somos técnicos" → interfaz cotidiana, implementación 2-3 cambios/mes.

**Ficha:** [[proyectos/STUDIO_OS-Emilia/00-index|Emilia — Studio OS]] · Sprint 30 días USD 600 (solo sprint, acreditable) · Éxito = venta Fase 2 · Deck [[proyectos/STUDIO_OS-Emilia/presentacion/00-presentacion-studio-os|16 slides]] · Cuestionario [[proyectos/STUDIO_OS-Emilia/03-cuestionario-plan-studio-os|03-cuestionario]]

---

## 1. Síntesis ejecutiva (arquitecta → arquitecta)

**Contexto validado 2026-08-27:**
Estudio chico 2-4 (titular + 1-2 juniors, delega parcial), mixto desordenado (Dropbox + WhatsApp + papel), sin vault/CDE, sin libro de obra, sin base proveedores, sin CRM (referidos + WhatsApp), honorarios manual/Excel, Lumion + AutoCAD, modelado 3D básico para impresora 3D (evolución → Rhino, no Revit), todo duele por igual pero el dolor agudo es **errores/comunicación/retrabajos por traducciones** (`C9`), no tiempo puro.

**Tesis del plan:** No vendemos IA. Vendemos **reducción de traducciones** con un sistema que respeta cómo diseña Emilia (a relevar) y se opera desde interfaz cotidiana. La tecnología queda detrás.

**Arquitectura en 1 línea:**
`Google Drive (binarios) + Vault Obsidian (índice/CDE/memoria) + Discord (interfaz) → túnel (Tailscale/Cloudflare) → ComfyUI local 24GB (SD1.5 + SDXL) → n8n opcional` con PI local y modelos OpenRAIL.

**Sprint 30 días entrega:** Mapa AS-IS/TO-BE + arquitectura del ecosistema (plano del estudio) + prototipo real ComfyUI en paralelo a Lumion (croquis → variantes) + roadmap Fase 2 modular priorizado + demo. **2-3 cambios/mes** post-sprint.

---

## 2. Principios de arquitectura (sistemas + obra)

1. **Mapa de intervención humana** (`Resumen:41-46`) — cada proceso clasificado: HUMANO (decide/evalúa/corrige) / IA (genera/clasifica/propone) / AUTOMATIZACIÓN (transporta/registra/dispara) / INFORMACIÓN (croquis/planos/referencias). Pregunta: ¿dónde el humano hace trabajo de automatización hoy?
2. **PI 100% protegida** — solo checkpoints con licencia comercial: `ArchitectureRealmix v11` (SD1.5, CreativeML OpenRAIL++M) y `Juggernaut XL v9` (SDXL, OpenRAIL) (`wiki/glosario/software/comfyui.md`, `wiki/estudio/decision-arquitectura-ia-privacidad.md:210`). Nada se usa para entrenar. RunPod solo para no sensible si se verifica política de retención/zero-training; por defecto **local**.
3. **No imponer software** (`Resumen:121-126`) — primero relevar cómo diseña Emilia (croquis/referencias/CAD), después definir pipeline. ComfyUI es transversal, no reemplaza Lumion (paralelo para iteración).
4. **CDE = Google Drive + Vault** — Drive ya es apéndice del estudio (no forzar migración). Vault Obsidian indexa y da memoria/búsqueda semántica; binarios referenciados por ruta (`AGENTS.md`). Evolución futura: `activos/proyectos/<obra>/` espejado a Drive.
5. **Interfaz cotidiana** — dolor "no somos técnicos" → Discord propuesto (vs Telegram/WhatsApp). Ventaja Discord: canales por proyecto/obra, threads, bot, permisos finos, integración n8n/ComfyUI más simple que WhatsApp Business API. Validar en sprint si prefieren WhatsApp (cero cambio hábito) vs Discord (orden). Propuesta: **Discord para obra/representación, WhatsApp sigue para clientes hasta CRM**.
6. **Iteración > perfección** — SD1.5 para variantes rápidas (segundos), SDXL para final (24GB lo permite, ~9 min en LOW_VRAM pero en 24GB nativo 1-2 min). Ambos en misma máquina.

---

## 3. Estado AS-IS (validado) vs TO-BE

### AS-IS (hoy)
```
Entrada: referidos → WhatsApp (sin trazabilidad) → Excel honorarios manual
Diseño: croquis? (a relevar) → AutoCAD → Lumion (render) → WhatsApp corrección → retrabajo
Proyectos/Docs: Dropbox desordenado, sin vault, sin versionado planos legales
Obra: sin libro formal, fotos WhatsApp sueltas, sin proveedor DB
Memoria: en cabeza de Emilia, no consultable
```

### TO-BE (objetivo Fase 2, iterativo)
```
Entrada: referidos/IG → form/bot Discord/WhatsApp → CRM ligero (Notion/Leantime/HubSpot free) → pipeline
Diseño: croquis+referencias → Drive → bot Discord "render" → ComfyUI local (SD1.5/SDXL) → Vault → Lumion solo para final
Proyectos: Drive (binarios) + Vault (índice, frontmatter, [[wikilinks]]) + versionado + checklist entregables
Obra (Fase 2 tardía): foto Discord → n8n → Drive/activos + Vault registro (fecha/obra/incidencia) → libro digital
Proveedores/Memoria: DB proveedores + grafo Vault (material→proyecto→detalle→proveedor→precio→foto)
Administración: MVP_03 calculadora honorarios (CPAU) → presupuesto → contrato → facturación vinculada a proyecto
```

**Plano del estudio (9 ambientes + circulaciones)** — visual para deck Fase 2: dibujar planta con flechas, no lista de tools (`Resumen:79-91`).

---

## 4. Arquitectura técnica propuesta

### 4.1 Infraestructura

| Capa | Propuesta inicial | Alternativa | Notas PI |
|------|-------------------|-------------|----------|
| **GPU** | Workstation 24GB existente en estudio, 24/7 con ComfyUI (`P:\00-repos\ComfyUI`, DirectML optimizado) | RunPod GPU cloud (ephemeral pod) | Local = PI segura. RunPod: verificar que pod es efímero, disco destruido al terminar, y TOS "no training on customer data". Usar solo para batch no sensible hasta auditar |
| **Túnel** | **Tailscale** (recomendado) o Cloudflare Tunnel → expone ComfyUI/n8n sin abrir puertos, acceso Sol remoto para soporte | Ngrok | Tailscale es VPN mesh, más privado. Cloudflare Tunnel es HTTP tunnel, también válido |
| **CDE** | Google Drive (binarios) + Vault Obsidian local (índice, `.md` con referencias a `activos/` o `drive://`) | NAS local futuro | Drive TOS: datos en Google sí se almacenan pero no se usan para entrenar modelos fundacionales públicos; para PI máxima, cifrar sensible o mantener local |
| **Orquestación** | n8n local (opcional Fase 2) para Discord → ComfyUI → Drive/Vault | Make/Zapier | n8n self-hosted = PI protegida, sin costo |
| **Memoria** | Vault Obsidian + búsqueda semántica local (embeddings locales via Ollama/Qwen) | Algolia/Notion AI | Local embeddings = PI protegida |

### 4.2 Modelos y licencias (auditoría)

- **SD1.5:** `architectureRealmix_v11.safetensors` (2.1GB) — licencia OpenRAIL++M, permite uso comercial, derivados, sin restricción NC. Ver `wiki/glosario/software/comfyui.md`
- **SDXL:** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (7.11GB) — licencia OpenRAIL++M similar, requiere atribución. En 24GB VRAM entra sin `--lowvram`.
- **ControlNets:** `control_v11p_sd15_canny / depth` (FP16) — locales, sin telemetría.
- **Prohibidos:** cualquier checkpoint con CC BY-NC o que exija no-comercial. Verificar cada modelo en Civitai/HF antes de instalar.

### 4.3 Flujo prototipo sprint (vertical slice)

```
[Emilia/Junior] --croquis.jpg + prompt voz/texto--> [Discord canal #renders]
        ↓
[n8n o bot simple] interpreta → arma payload ComfyUI API
        ↓
[ComfyUI local 24GB] Workflow: LoadImage → ControlNet (Canny/Depth) → CLIP SD1.5 o SDXL → KSampler → VAE → Save
        ↓
[Output] 4 variantes SD1.5 (30-60s) + 1 SDXL (90-120s) → repost a Discord thread + copia a Drive/Vault (salidas/n_XX-...)
        ↓
[Emilia] criterio → reacciona con emoji / pide iteración → nuevo ciclo sin junior intermediario
```

**Workflow base:** reutilizar `proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/` (Canny/Depth) + `A-txt2img` para txt2img. Documentar según `03-nodos-WF*.md`.

### 4.4 Discord vs WhatsApp/Telegram — decisión sprint

| Criterio | Discord | WhatsApp | Telegram |
|----------|---------|----------|----------|
| **Adopción Emilia hoy** | Baja (hay que enseñar) | Alta (ya usan) | Media |
| **Orden por proyecto** | Excelente (canales/threads) | Malo (chats mezclados) | Medio |
| **Bot ComfyUI** | Fácil (webhook n8n) | Difícil (Business API) | Fácil |
| **PI** | Datos en Discord (US) pero no sensibles si solo croquis no final | Meta ve mensajes | Telegram cloud |
| **Recomendación** | **Propuesta inicial para renders/obra** | Seguir para clientes hasta CRM | Descartar si Discord avanza |

**Plan:** Sprint valida con Emilia. Si rechaza Discord, fallback a WhatsApp manual (sin bot, solo Drive + ComfyUI local operado por junior).

---

## 5. Sprint 30 días — plan operativo (USD 600)

**Objetivo sprint:** Vender Fase 2. Entregables = prueba de que el sistema reduce traducciones sin volverlos técnicos.

| Semana | Actividad | Entregable | Responsable | Validación |
|--------|-----------|------------|-------------|------------|
| **1** | Relevamiento (2-3 entrevistas 60-90 min + shadowing 1 día) | Mapa AS-IS (9 ambientes + flujos + dolores) | Sol + Emilia + 1 junior | Emilia firma mapa |
| **1-2** | Auditoría tech (GPUs 24GB, Drive, Lumion, AutoCAD, red, túnel) | Informe tech + inventario + test ComfyUI local (SD1.5+SDXL en 24GB) | Sol | ComfyUI responde via Tailscale |
| **2** | Matriz intervención humana + oportunidades (impacto/esfuerzo) | Matriz priorizada + 3 quick wins | Sol | Priorización con Emilia |
| **2-3** | Arquitectura TO-BE (plano del estudio + grafo) | Diagrama planta + propuesta CDE (Drive+Vault) + política PI | Sol | Aprobación diagrama |
| **3** | Prototipo vertical (1 proyecto real Emilia, 3-5 croquis) | Bot Discord → ComfyUI funcionando, 8-12 variantes (SD1.5+SDXL) en Drive/Vault | Sol + junior | Emilia evalúa: ¿reduce retrabajo? |
| **4** | Demo + Roadmap Fase 2 + métricas | Presentación roadmap modular (2-3 cambios/mes) + presupuesto Fase 2 por módulo + métricas baseline | Sol | Decisión Go/No-Go Fase 2 |

**RACI sprint:**
- **Responsable:** Sol (consultoría, arquitectura, prototipo)
- **Accountable:** Emilia (decisiones, croquis, validación)
- **Consulted:** Junior (operativa diaria, test Discord)
- **Informed:** — (estudio chico)

**Condiciones comerciales reiteradas:** USD 600, 50/50 o 100% adelantado, acreditable a Fase 2 si avanza en 30 días post-demo. Incluye diagrama, prototipo, roadmap. No incluye implementación Fase 2 ni licencias.

---

## 6. Roadmap Fase 2 modular (post-sprint, 2-3 cambios/mes)

Priorizado por dolor "todo duele pero retrabajo es agudo" + adopción moderada.

### Módulo 1 (mes 1-2) — Cimientos + Representación paralela
- Vault mínimo viable: `proyectos/<cliente>-<proyecto>/` + `index.md` con frontmatter + referencias a Drive ([[proyectos/template_arq/00-index|template de proyecto]])
- Discord #renders operativo + ComfyUI local (SD1.5 para iterar, SDXL para final) en paralelo a Lumion
- Capacitación Rhino básico (desde 3D impresión → Rhino) — 2 talleres
- **Métrica:** iteraciones/semana, tiempo corrección, retrabajos evitados

### Módulo 2 (mes 3-4) — Clientes + Honorarios
- CRM ligero (Leantime self-hosted o HubSpot free) → `web/IG → consulta → CRM → reunión → propuesta`
- MVP_03 calculadora honorarios integrada (CPAU Cuadro 8, USD/ARS) → presupuesto/contrato vinculado a proyecto
- **Métrica:** tiempo presupuesto, leads perdidos, facturación

### Módulo 3 (mes 5-6) — Memoria + Proveedores
- Grafo Vault: `material → proyecto → detalle → proveedor → precio → foto` + búsqueda semántica local
- DB proveedores (Notion/Obsidian Dataview) con evaluación
- **Métrica:** tiempo búsqueda, consultas tipo "hormigón visto" resueltas en <2 min

### Módulo 4 (post-6) — Libro digital obra (diferido a pedido)
- Foto Discord/WhatsApp → n8n → Drive/activos + Vault `reuniones/YYYY-MM-DD-obra.md` + libro digital
- **Métrica:** fotos registradas vs perdidas, incidencias trazadas

> Cada módulo = presupuesto cerrado. Estudio chico no absorbe big bang.

---

## 7. Métricas y baseline (a levantar semana 1)

Baseline sprint (medir hoy para comparar):

| Métrica | Cómo medir hoy | Meta Fase 2 |
|---------|----------------|-------------|
| Tiempo búsqueda info (planos, detalles, fotos) | Test 3 consultas reales (H23 a definir) | <2 min con Vault |
| Tiempo ciclo representación (croquis → variante) | Cronometrar Lumion + correcciones | -50% con SD1.5 |
| Cantidad traducciones/intermediarios por render | Contar pasos `Emilia→junior→...` | -1 intermediario |
| Retrabajos por mala comunicación | # correcciones por proyecto | -30% |
| Tiempo admin presupuestos/honorarios | Horas/mes Excel manual | -40% con MVP_03 |
| Utilización GPU 24GB | % uso actual vs con ComfyUI | >60% uso productivo |

---

## 8. Riesgos y mitigaciones (sistemas + obra)

| Riesgo | Prob | Impacto | Mitigación |
|--------|------|---------|------------|
| "No somos técnicos" → abandono Discord/ComfyUI | Alta | Alto | Interfaz Discord simple (1 comando), capacitación 30 min, fallback WhatsApp manual, soporte Tailscale remoto |
| RunPod confidencialidad (PI) | Media | Alto | **Local por defecto**. RunPod solo si TOS confirma zero-retention + ephemeral. Auditar antes de usar. Nunca planos legales/concurso en cloud |
| Drive como CDE → desorden persiste | Media | Medio | Vault como índice obligatorio + checklist `proyectos/<obra>/00-index.md` + 1 junior como librarian |
| GPUs 24GB no 24/7 (ruido, energía, OT) | Media | Medio | ComfyUI on-demand via Tailscale wake-on-LAN, no 24/7 fijo |
| Estudio chico → sin tiempo para 2-3 cambios/mes | Media | Alto | Módulos pequeños, cada uno <4h capacitación, champion = Emilia + 1 junior con incentivo |
| Modelos sin licencia comercial → riesgo legal | Baja | Alto | Checklist licencias (OpenRAIL only) en `wiki/glosario/software/comfyui.md` |

---

## 9. Decisiones abiertas para sprint (a validar con Emilia)

1. **Discord vs WhatsApp** para renders/obra — test 1 semana cada uno si duda
2. **Túnel:** Tailscale (recomendado) vs Cloudflare Tunnel — según IT del estudio
3. **Vault hosting:** Obsidian local + Drive sync vs Quartz self-hosted (`wiki/estudio/analisis/analisis-despliegue-wiki-quartz.md`)
4. **RunPod:** ¿usar para batch SDXL no sensible o 100% local siempre? — auditar TOS RunPod 2026

---

## 10. Próximos pasos inmediatos

- [ ] Sol valida este plan (este archivo)
- [ ] Agendar relevamiento semana 1 con Emilia (2h) + pedir 3-5 croquis y 1 proyecto real para prototipo
- [ ] Test técnico: instalar ComfyUI en GPU 24GB Emilia + Tailscale + SD1.5+SDXL (ver `proyectos/MVP_04-comfyui-arquitectura/pbook-comfy_setup.md`)
- [ ] Preparar demo corta (croquis genérico → 4 variantes) para reunión de venta sprint (si "no definido" J28, proponer remota 30 min + demo)
- [ ] Actualizar deck con diagrama "plano del estudio" como planta (Figma/Excalidraw) y grafo Vault

---

## 11. Referencias vault

- Fuente conceptual: [[Resumen_Propuesta_Emilia_Studio_OS(1).txt]]
- Deck: [[proyectos/STUDIO_OS-Emilia/presentacion/00-presentacion-studio-os]]
- Guion: [[proyectos/STUDIO_OS-Emilia/presentacion/01-guion-presentacion]]
- Anexo sprint: [[proyectos/STUDIO_OS-Emilia/presentacion/02-anexo-sprint]]
- Cuestionario completo: [[proyectos/STUDIO_OS-Emilia/03-cuestionario-plan-studio-os]]
- Privacidad IA: [[wiki/estudio/decision-arquitectura-ia-privacidad]]
- IA estudios internacionales: [[wiki/glosario/referentes/ia-estudios-internacionales]]
- Estándares oficina: [[wiki/glosario/interno/standares/oficina/00-index]]
- MVP calculadora: [[proyectos/MVP_03-calhon-gest/readme-mvp_03]]
- ComfyUI workflows: [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04]]

> **Nota PI RunPod:** Pendiente verificar 2026-08-27 TOS RunPod: pods son efímeros (disco destruido al detener), no entrenan modelos con datos de usuario, pero logs/network pueden retenerse 7-30 días. Para PI máxima, preferir local. Documentar decisión en `wiki/estudio/decision-arquitectura-ia-privacidad.md` post-auditoría.
