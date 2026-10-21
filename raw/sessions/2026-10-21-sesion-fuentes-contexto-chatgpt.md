---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [fuentes, gaudi, chatgpt, project, google-drive, emilia, leantime, investigacion]
---

# Sesión 2026-10-21 (madrugada) — El corpus AI×Gaudí como contexto de ChatGPT para Emilia

## Qué se pidió

Sol: que el trabajo de **análisis de fuentes** tenga su parte de **"cómo implementar eso"** en el plan, replicado sobre el corpus del concurso (el que está en la carpeta del Drive de AI×Gaudí), y que hay que resolver **cómo compartirlo con el ChatGPT de Emilia** — ella lo usa mucho desde el celular — **sin que sus sesiones y el Vault se pisen**. Y que mañana haya una pestaña abierta para probar.

## Qué se hizo

### 1. Estado real del corpus (medido, no supuesto)

- Carpeta fuente (Drive, solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography` → **31 PDF** (30 fuentes + `0. INDEX.pdf`).
- En el vault: **32 fichas** + **31 transcripciones** en `raw/pdf/` (Gate 0 v2 ya ejecutado el 20/10).
- El PDF que Sol nombraba como ejemplo es el **"Bio Inspired Design Approach Analysis"** (PDF 24, parametrismo, 7 p).
- En el Drive, junto: `AIxGaudi/Materials` (2 DWG de Barcelona, el LoRA de rhino-to-image, el CSV del curso) y `Fuentes-Aleph/Fuentes-Inbox.gsheet` (el inbox de links, que es otra cosa).

### 2. La decisión de fondo (doc de OpenAI, verificada 21/10)

**Los custom GPT se retiran.** Las cuentas personales (Free/Go/Plus/Pro) **ya no pueden crear ni publicar GPTs**; los existentes siguen usándose. Retiro: 11/12/2026 en Enterprise; migración a *Plugins* apuntada al 17/09/2026. La misma doc contrapone GPT vs **proyecto compartido** y deja claro que el proyecto es lo multi-jugador y lo vivo.

**La vía: proyecto compartido + app de Google Drive.**
- Los proyectos se **comparten por link o invitación**, en web **y en la app móvil** (todos los planes).
- *Add source → Google Drive* acepta el **link de un archivo o una carpeta**.
- Dentro de un proyecto, la app de Drive **no pre-indexa**: consulta en vivo → siempre fresca.
- Límites: 5 / 25 / 40 archivos por proyecto según plan; 10 por tanda.

**La coexistencia con sus sesiones: sí, y limpia.**
1. El proyecto es un espacio aparte (y ella puede mover chats suyos adentro si quiere).
2. Los proyectos compartidos usan **memoria solo-del-proyecto**: no leen sus memorias personales, sus instrucciones globales ni conversaciones de afuera → el corpus no se le mezcla.
3. El Drive es la **copia compartida**; el vault sigue siendo el original (fichas con copyright marcado).
4. La **API** sirve para el lado vault (n8n), no para la app del celular (no acepta API keys).

### 3. Ítem de Leantime

Card `589` — "Fuentes del concurso: corpus AIxGaudi como contexto para el ChatGPT de Emilia" (proyecto 4 `O.S_ARQ-Emi`, milestone `463` M-A3 — Método de catalogación + biblioteca, sprint 27, **5,04 h**), con **8 subtareas** `590`-`597` (1 pom cada una, salvo la exportación de fichas con 4).

| # | Subtarea | h |
|---|---|---|
| 590 | Decidir el material de contexto: fichas procesadas, PDF crudos o ambos (pregunta a Emilia) | 0,42 |
| 591 | Exportar las 32 fichas a `AIxGaudi/Bibliography-procesada` (6 archivos por lote temático) | 1,68 |
| 592 | Compartir esa carpeta con la cuenta de Google de Emilia | 0,42 |
| 593 | Conectar la app Google Drive en el ChatGPT de Emilia | 0,42 |
| 594 | Crear el Project "AI×Gaudí" y añadir la carpeta como fuente | 0,42 |
| 595 | Probar desde el celular; sus chats normales intactos | 0,42 |
| 596 | Escribir las instrucciones del contexto (qué es, cómo citar, qué no hacer) | 0,84 |
| 597 | Documentar en el vault y cerrar la card | 0,42 |

### 4. Las 4 pestañas para mañana

1. `chatgpt.com` → **Settings → Plugins → Google Drive** → conectar la cuenta.
2. `chatgpt.com` → **New project** "AI×Gaudí" → Project settings (instrucciones) → **Add source** → link de la carpeta del Drive.
3. `drive.google.com` → compartir `Bibliography-procesada` con el correo de Emilia y copiar el link.
4. `chatgpt.com/g/gpts` → verificar que no se pueden crear GPTs nuevos (deja de ser discusión y queda documentado).

Al final: desde el celular, abrir el link del proyecto → aparece en su barra lateral → mismo contexto.

### 5. Recomendación

**Subir las fichas procesadas, no los PDF crudos**: ya están curadas (resumen, páginas, figuras referenciadas, avisos de copyright) y el retrieval sobre texto limpio rinde mucho mejor. El PDF original queda a un clic vía la app de Drive. Estructura: 1 hub (`00-INDICE.md`) + 6 archivos por lote temático = 7 archivos, holgadamente debajo de los 10 por tanda.

## Archivos del vault

- `proyectos/STUDIO_OS-Emilia/documentacion/fuentes-contexto-chatgpt-emilia.md` (nuevo) — decisión, vía, coexistencia, las 4 pestañas, los 5 pasos, estructura de exportación e instrucciones del contexto, con las 6 referencias de OpenAI.
- `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` — §7 pregunta 6 para Emilia + §9 registro de cambios.
- `log.md` (entrada del 21/10).

## Cerebro-digital

**Topics:** OpenAI custom GPTs en retirada · ChatGPT Projects y project-only memory · Google Drive app dentro de ChatGPT · corpus AI×Gaudí · pipeline de fuentes por gates · reparto Drive/vault como fuente única.

**Entidades:** card `589` + subtareas `590`-`597` · proyecto 4 `O.S_ARQ-Emi` · milestone `463` M-A3 · sprint 27 · `raw/pdf/` (32 fichas, 31 transcripciones) · `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography` (31 PDF) · `AIxGaudi/Materials` · `Fuentes-Aleph/Fuentes-Inbox.gsheet` · doc de OpenAI `10169521-chatgpt-projects`.

**Hechos verificados:** (1) las cuentas personales no pueden crear custom GPTs y el retiro es el 11/12/2026 (Enterprise), con migración a Plugins al 17/09/2026; (2) los Projects son compartibles por link/invitación en web y móvil, y usan memoria solo-del-proyecto → no tocan las conversaciones ni memorias personales de los miembros; (3) en un proyecto se puede pegar un link de carpeta de Google Drive como fuente, y la app no pre-indexa (consulta en vivo); (4) los límites de archivos por proyecto son 5 (Free) / 25 (Go, Plus) / 40 (Edu, Pro, Business, Enterprise), con 10 por tanda; (5) el corpus ya está extraído (Gate 0 v2) y lo que falta es la curaduría (gates 1-3) más esta vía de compartición.
