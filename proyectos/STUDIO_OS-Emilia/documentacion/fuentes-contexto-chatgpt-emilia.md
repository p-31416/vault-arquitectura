---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [fuentes, gaudi, ai-gaudi, chatgpt, project, google-drive, emilia, concurso, sesion-2026-10-21]
---

# Fuentes del concurso como contexto de trabajo para Emilia (ChatGPT + Drive)

Qué hay que implementarse para que el corpus **AI×Gaudí** (31 PDF ya extraídos a 32 fichas) sea contexto de trabajo de Emilia, **sin romperle las sesiones de ChatGPT que usa desde el celular**.

Ítem de Leantime: card `589` + 8 subtareas (`590`-`597`), en el proyecto 4 → milestone `463` (M-A3 — Método de catalogación + biblioteca), sprint 27.

---

## 1. La decisión de fondo: los custom GPT no son la vía (oct/2026)

OpenAI **está retirando los custom GPTs**:

- Las cuentas personales (**Free, Go, Plus, Pro**) **ya no pueden crear ni publicar GPTs nuevos**; los que existen siguen usándose y editándose.
- Retiro previsto: **11/12/2026** en workspaces Enterprise. La migración a **Plugins** apunta al **17/09/2026**.
- En los workspaces **Business / Enterprise / Edu** se siguen creando, según permisos.

→ **No apostamos por un GPT custom.** La misma documentación de OpenAI contrapone las dos cosas y define cuál es para qué:

| | Custom GPT | **Project compartido** |
|---|---|---|
| Jugadores | uno solo (tú y el chat) | **equipo**: los miembros ven las contribuciones de los demás |
| Contenido | estático, curado por un experto | vivo, crece con el uso |
| Uso | conocimiento reutilizable entre áreas | **central de contexto para un trabajo compartido** |

Lo que queremos es lo segundo: un **proyecto compartido** con el corpus.

## 2. La vía: Project compartido + app de Google Drive

| Pieza | Qué permite (verificado en la doc de OpenAI) |
|---|---|
| **Projects** | cantidad ilimitada; **compartibles por link o invitación** en web **y en la app móvil** (Free, Go, Plus, Pro, Business, Enterprise, Edu) |
| **Add source → Google Drive** | se pega el **link de un archivo o una carpeta** del Drive y queda como fuente del proyecto |
| **App de Google Drive** | conectada, se le pregunta por cualquier archivo/carpeta que la cuenta pueda abrir; dentro de un proyecto **no pre-indexa** → consulta en vivo, siempre fresca |
| **Límites** | archivos por proyecto: **5** (Free) · **25** (Go, Plus) · **40** (Edu, Pro, Business, Enterprise); **10 por tanda**; 512 MB y 2 M tokens por archivo |

## 2.b La forma más simple: **un documento compartido en el Drive**

Lo más simple que funciona, y lo que se **(Decisión de Sol, 21/10)**: en vez de un proyecto de ChatGPT, **un documento en el Drive que ella abre o adjunta**, y listo.

```
Drive: OS-Emilia/AIxGaudi/Fuentes-Visibles/
  └─ AIxGaudi-briefing.md      <- 1 documento: índice + por fuente: metadata, extracto, figuras, punteros
```

- **Emilia**: en el ChatGPT (web o celular) abre el archivo del Drive — con la app de Google Drive conectada, o adjuntándolo — y pregunta. Sus chats normales quedan intactos (nada se comparte, nada se sincroniza).
- **El vault**: el `.md` es del vault, el Drive es la copia compartida. Cuando ella edita o agrega algo, la sincronización lo trae de vuelta y el importador (patrón de `scripts/import_drive_reuniones.py`) lo copia a `raw/` → commit.
- **Sin plan de pago, sin límites de archivos y sin retirement de GPTs**: un archivo, una carpeta, un link.
- **Con el proyecto de ChatGPT** el contexto queda fijo y con memoria propia; sin él, ella adjunta el documento cuando lo necesita. **El proyecto es el envoltorio opcional, no el requisito.**

**Qué lleva el documento** (para que sirva de contexto y no de texto muerto): por fuente → título, autor, año, idioma, páginas, palabras, **el extracto** (los primeros ~1.000-1.500 caracteres útiles: resumen/abstract) y la lista de figuras con página; y el puntero al PDF original (en el Drive) y a la transcripción completa (en el vault).

> El extracto va porque el texto completo tiene copyright: **al Drive compartido va extractos breves con atribución** (misma regla que la wiki); la transcripción entera sigue en `raw/`, de uso interno.

## 3. La respuesta a "¿coexisten sus sesiones con el Vault?" → **sí, y de forma limpia**

1. **Un proyecto es un espacio aparte.** Sus chats de siempre (los que usa desde el celular) siguen intactos, y además puede **mover** chats suyos al proyecto si quiere.
2. **Memoria solo-del-proyecto.** Los proyectos compartidos usan *project-only memory*: **no leen** sus memorias personales, sus instrucciones globales ni conversaciones de afuera del proyecto. → El corpus no se le "mezcla" con su vida en ChatGPT.
3. **El Drive queda como fuente única, no como copia.** El vault sigue siendo el original (fichas + transcripciones en `raw/pdf/`, con el copyright marcado); el Drive es la **copia compartida** que ChatGPT puede leer.
4. **La API es para el lado vault, no para el celular.** Si mañana se quiere consultar el corpus desde n8n (el agente), va por la API; la app del celular no acepta API keys.

## 4. Las 4 pestañas para abrir mañana

| # | URL | Qué hacer | Quién |
|---|---|---|---|
| 1 | `https://chatgpt.com/` → **Settings → Plugins** (o *Apps*) → **Google Drive** → Connect | Conectar la cuenta de Google que tiene `OS-Emilia` | Emilia (con Sol al lado) |
| 2 | `https://chatgpt.com/` → sidebar → **New project** → "AI×Gaudí" → **Project settings** (instrucciones) → **Add source** → link de la carpeta del Drive | Crear el proyecto y pegarle la carpeta | Sol + Emilia |
| 3 | `https://drive.google.com/drive/folders/…` → carpeta `OS-Emilia/AIxGaudi/` → **Compartir** | Compartir `Bibliography-procesada` con el correo de Emilia y copiar el link | Sol |
| 4 | `https://chatgpt.com/g/gpts` | **Verificar** que no se pueden crear GPTs nuevos → deja de ser una discusión y queda documentado | Sol |

Y al final, en el celular de ella: abrir el link del proyecto compartido → le aparece en la barra lateral → misma pregunta, mismo contexto.

## 5. Los 5 pasos (con su pomodoro)

| # | Paso | Card | Pom |
|---|---|---|---|
| 1 | Decidir el material de contexto: **fichas procesadas (32 .md)**, PDF crudos, o ambos → **pregunta a Emilia** | `590` | 1 |
| 2 | Exportar las fichas a la carpeta del Drive `AIxGaudi/Bibliography-procesada`, agrupadas en los **6 lotes temáticos** (biomimicria · morfogénesis · estructura · parametrismo · historia · fractales) | `591` | 4 |
| 3 | Compartir esa carpeta con la cuenta de Google de Emilia | `592` | 1 |
| 4 | Conectar la app de Google Drive en el ChatGPT de ella | `593` | 1 |
| 5 | Crear el Project "AI×Gaudí" y pegarle la carpeta como fuente | `594` | 1 |
| 6 | Probar desde el celular y comprobar que sus chats normales siguen intactos | `595` | 1 |
| 7 | Escribir las **instrucciones del contexto** (qué es el corpus, cómo citar, qué no hacer) | `596` | 2 |
| 8 | Documentar en el vault y cerrar la card | `597` | 1 |

**Total: 5,04 h (12 pomodoros).**

### Recomendación para el paso 1

**Las fichas procesadas, no los PDF crudos.** Motivos: ya están curadas (resumen, páginas, figuras referenciadas, avisos de copyright) y el retrieval sobre texto limpio rinde mucho mejor que sobre 31 PDF escaneados. El PDF original sigue a un clic: la app de Drive lo abre cuando hace falta la fuente primaria.

**Estructura de la exportación** (1 archivo por lote temático, 6 en total → holgadamente debajo de los 10 por tanda):

```
Drive: OS-Emilia/AIxGaudi/Bibliography-procesada/
  ├─ 00-INDICE.md                    (hub: las 32 fichas, 1 línea cada una)
  ├─ L1-biomimicria.md               (8 fichas)
  ├─ L2-morfogenesis.md              (7)
  ├─ L3-estructura.md                (6)
  ├─ L4-parametrismo.md              (3)
  ├─ L5-historia-y-obra.md           (5)
  └─ L6-fractales.md                 (1)
```

## 6. Instrucciones del contexto (base para el paso 7)

> Sos el copiloto de investigación del estudio. Tu contexto es el corpus AI×Gaudí: 30 fuentes sobre Gaudí (biomimicria, morfogénesis, estructura, parametrismo, historia, fractales) con ficha y transcripción por documento.
> Reglas: (1) citá siempre el **slug del documento** y la página; (2) si no está en el corpus, decilo — no inventes; (3) distinguí lo que la fuente **afirma** de lo que el estudio **infiere**; (4) el corpus es de consulta interna: no lo reproduzcas entero en respuestas, resumí; (5) avisá cuando una afirmación del corpus contradiga otra fuente.

## 7. Sin plan de pago: se puede igual

Sol no tiene plan pago de ChatGPT (Free). **No es bloqueo**, con dos matices:

| | Con plan Free | Qué hacer |
|---|---|---|
| Crear y compartir un proyecto | ✓ se puede (proyectos ilimitados; compartir por link o invitación) | — |
| Tope de archivos **subidos** al proyecto | **5** (Free) | no importa: el contexto entra como **1 link a la carpeta del Drive**, no como archivos subidos → el tope de subidas no aplica |
| Colaboradores | 5 (Free) | alcanza (ustedes dos) |
| Custom GPT | ✗ ni en Plus/Pro | no se usa |
| Library con Drive dentro | ✗ en web para Plus/Pro/Enterprise… (rolling out) | no hace falta: se usa la app de Drive **dentro** del proyecto |

**Y lo de "ver la sesión pero no participar":** pasa cuando se comparte **un chat suelto** (queda como lectura). Para participar los dos hay que compartir **el proyecto**: el dueño invita y el otro entra como miembro; con **acceso de edición** puede además tocar las instrucciones del contexto, agregar archivos e invitar a otros.

| Se comparte | El otro puede |
|---|---|
| un chat suelto (link) | **ver** ✗ no participar |
| **el proyecto** (link "anyone with the link" o invitación) | **participar**: ver los chats del proyecto, escribir, y con "edit" editar instrucciones y archivos |

→ Para que los dos trabajen el corpus: **el proyecto se comparte, no el chat**. El dueño decide el nivel (chat o edit).

## 8. El bucle: del ChatGPT al Vault y a GitHub

**No existe conector nativo de ChatGPT a GitHub.** Pero el puente se arma con dos piezas que ya tenemos:

### Vía A — la app de Drive con escritura (gratis, recomendada)

```
ella trabaja en el proyecto compartido
   → le pide: "guardá este análisis en la carpeta Bibliography-procesada"
   → la app de Google Drive escribe el .md en el Drive   (pide confirmación; requiere scopes de escritura)
   → el importador del vault lo levanta del Drive        (patrón ya existente: scripts/import_drive_reuniones.py)
   → queda en raw/ + se commitea
```

La app de Drive en ChatGPT puede **crear, actualizar, mover, compartir y borrar** archivos, si los permisos de Google y del workspace lo permiten. El vault sigue siendo el que decide qué entra a `wiki/` (gates) y qué se commitea.

### Vía B — un script del vault que pregunta al corpus (para automatizar)

```
scripts/consultar_corpus.py  →  (API de OpenAI con la key del vault, o el OpenRouter que ya usa n8n)
   → arma el contexto porRecovery (topical: las fichas del lote pertinente, NO las 480k palabras)
   → escribe la respuesta en raw/  →  @contenidos la cura  →  wiki/
```

Ojo con el costo: meter el corpus entero (~480.000 palabras ≈ 640k tokens) en cada llamada es caro. **Se recupera por tema** (5-20k tokens por consulta) → centavos por consulta. La API se factura aparte del plan de ChatGPT (con créditos propios).

### Lo que NO se mueve por ChatGPT

El corpus que debe quedar **permanente en la wiki** sigue su camino propio y con gates: `@sherlock` (gates 1) → `@contenidos` (gates 2-3) → `wiki/fuentes/`. El proyecto de ChatGPT es para **consultar y trabajar**, no para escribir la wiki.

## 9. Lo que NO hacemos (y por qué)

| No | Por qué |
|---|---|
| Custom GPT | las cuentas personales no pueden crearlos y se retiran (11/12/2026) |
| Subir los 31 PDF al proyecto | 40 archivos es el tope y el retrieval sobre PDF escaneado es malo; van las fichas |
| Que el Vault sea el "servidor" de contexto | la app del celular no acepta API keys; el Drive es lo que ChatGPT sabe leer |
| Un proyecto por persona con copias | el proyecto compartido + memoria solo-del-proyecto ya aísla sin duplicar |

## 10. Referencias (verificadas 21/10/2026)

- Projects in ChatGPT (archivos por plan, *Add links from apps*, compartir por link, project-only memory): https://help.openai.com/en/articles/10169521-chatgpt-projects
- Google Drive app and setup in ChatGPT (conectar la cuenta, permisos): https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt
- Creating and editing GPTs (retiro de los custom GPTs): https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- Sharing and publishing GPTs (niveles de compartir): https://help.openai.com/en/articles/8798878-sharing-and-publishing-gpts
- Connected apps in ChatGPT (apps y plugins): https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt
- Using Library to manage files in ChatGPT (Drive dentro de la Library; en móvil, "support will follow"): https://help.openai.com/en/articles/20001052-using-library-to-manage-files-in-chatgpt

Relacionado: [[specs/261020-plan-procesado-fuentes-pdf-gaudi]] · [[proyectos/STUDIO_OS-Emilia/documentacion/que-le-pedimos-a-emilia-2026-10-21]]
