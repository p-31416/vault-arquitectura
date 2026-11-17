---
tipo: plan
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [credenciales, oauth, service-account, fuentes-v2, panel, contactos-contexto, pdf-fichas, floss]
idioma: es
---

# Fuentes v2 · Contactos con contexto · PDF→fichas · Panel web · Credenciales sin reconexión

> Extiende el [[specs/261111-plan-maestro-studio-os|plan maestro]] (§7 Camino 2) con lo pedido hoy: credenciales Google estables, panel de fuentes con creadores y categorías, reuniones con contexto de quién es, PDFs que generan fichas, y panel accesible desde el celular (y cualquier navegador de visor/VR, porque es web estática). Todo FLOSS-first.

---

# 1 · Credenciales Google: por qué se desconectan y cómo dejar de reconectarlas

## 1.1 Causa raíz

Las credenciales OAuth de Google **no expiran por tiempo** — expiran porque la app está en estado **"Testing"** en Google Cloud Console. Apps en Testing emiten refresh tokens que mueren a los **7 días**. Cada reconexión manual que hiciste (caso 08/10 en MVP_06) es eso: el refresh token vencido.

## 1.2 Fix A — Publicar la app OAuth (5 minutos, cero código)

```text
1. Google Cloud Console → APIs & Services → OAuth consent screen
2. Estado de publicación: Testing → "PUBLISH APP" (In production)
3. Los refresh tokens nuevos ya no vencen a los 7 días
4. Reconectar una vez cada credencial OAuth de n8n → queda estable
```

* Con scopes sensibles, Google muestra una pantalla de advertencia a usuarios externos — se acepta una vez con tu cuenta y listo. En modo de prueba interna con Workspace la advertencia no aparece.
* Cubre: Gmail OAuth2, Drive, Sheets, Docs — todas las credenciales OAuth de n8n.

## 1.3 Fix B — Service Account para Sheets (sin OAuth, estable por diseño)

Para el flujo que escribe en Google Sheets (Router Fuentes) y para lecturas server-side, la credencial **Service Account** no usa OAuth:

```text
1. Google Cloud Console → IAM → Service Accounts → crear SA
2. Crear key JSON → cargar en n8n como credencial "Google Sheets (Service Account)"
3. Compartir el Sheet con el email de la SA (editor) — una vez
4. El flujo escribe sin OAuth, sin expiración, sin reconexión
```

**Decisión propuesta**: Fix A para todas las credenciales OAuth existentes (Gmail, Drive) + Fix B para el flujo del Router/Sheets. Ambos FLOSS-neutros (Son credenciales de Google, pero eliminan la fragilidad).

## 1.4 Cadencia que queda

La revisión mensual de 15 min de MVP_06 baja a: saldo OpenRouter + salud Redis/Postgres. Las credenciales Google salen de la lista.

---

# 2 · Fuentes v2 — panel con creadores y categorías

## 2.1 Sheet `Fuentes-Inbox` extendido

Columnas nuevas sobre las existentes (Fecha/De/Link/Tipo/Título/Estado/Destino/Nota/Tags):

| Columna nueva | Contenido | Quién la llena |
|---|---|---|
| **Creador** | canal/cuenta (canal YT, @cuenta IG, autor web) | flujo n8n (Jina/oEmbed ya trae autor) |
| **Categoría** | IA · arquitectura · BIM · gestión · referente · herramienta · hype | flujo n8n propone + Sol corrige |
| **Veredicto** | tren · hype · aporte | Sol (o curaduría asistida) |

**Tab nuevo `Creadores`**: una fila por creador (nombre, plataforma, qué publica, categoría dominante, confianza alta/media/baja, seguir/descartar). Cada fuente queda ligada a su creador — así el panel agrupa por canal, no solo por link suelto.

**Tab nuevo `Sugerencias`**: propuestas del agente (cron semanal): "este creador acumula 5 aportes, seguilo"; "esta categoría está vacía, falta BIM"; lista corta y accionable.

## 2.2 Flujo Router v2 (cambios mínimos)

1. `Parsea Info` extrae también **creador** (author_name de oEmbed YT; cuenta IG del lector Jina ya disponible)
2. Nodo nuevo `Clasifica` (agente con las 7 categorías canon + reglas MVP_02/Studio OS) escribe Categoría propuesta
3. Si el link es **PDF** → rama nueva (§4)
4. Si falta título (Jina falló) → el ack ⚠️ ya existente avisa; el panel marca la fila

## 2.3 Categorías canon

`IA` (modelos, agentes, prompts) · `arquitectura` (proyectos, referentes, concursos) · `BIM` (IFC, FreeCAD, estándares) · `gestión` (honorarios, TAD, CRM, n8n) · `software` (herramientas instalables) · `referente` (estudios, obras, maestros) · `hype` (engagement-bait — se archiva con oportunidad, no se borra).

---

# 3 · Reuniones con contexto — quién es quién

## 3.1 Tab `Contactos` (la hoja de clientes evolucionada)

| Columna | Contenido |
|---|---|
| Nombre · email · organización | datos base (ya existen en `clientes-contactos`) |
| **Tipo** | cliente · socia-gestiones · proveedor · comitente · colega · interno |
| **Contexto** | 3-5 líneas: quién es, qué proyecto, qué pasó la última vez |
| **Cómo analizar** | parámetros para minuta/informe: qué mirar, qué priorizar, tono |
| **Última interacción** | fecha + link a la minuta en el vault |

Ejemplo real: *Emilia* → tipo cliente · contexto: titular del estudio piloto, proyecto Studio OS, gates semanales · cómo analizar: minuta orientada a decisiones y fechas, tono directo. *Socia de gestiones* → tipo socia-gestiones · cómo analizar: minuta orientada a plazos municipales y documentación.

## 3.2 Cómo se usa

1. **Al agendar**: cuando el subflujo Cal.com crea un evento, el agente busca el contacto por nombre/email en `Contactos` → inyecta el contexto en la confirmación ("reunión con Emilia — proyecto Studio OS, última interacción 08/11").
2. **Al minutar**: la skill `minuta-reunion` recibe la ficha del contacto → el resumen sigue los parámetros de su columna "cómo analizar" (reunión interna de gestión ≠ reunión con cliente).
3. **Antes de la reunión**: "¿quién es Juan?" → ficha completa con historial de minutas del vault.
4. **Extrapolación a Emilia**: la misma tab Contactos es la base del CRM de la entrega — llega con datos, no vacía.

## 3.3 Privacidad y nivel

El contexto vive en tu Sheet/vault (nube de archivos propia, nivel C de lectura con aprobación en flujos). Nada sale a terceros.

---

# 4 · PDF → fichas (retomar la ingesta)

Camino en el mismo Router v2:

```text
PDF al grupo Fuentes (o Drive con el flujo existente)
  → materializa en /fuentes/<proyecto>/<año>/ (rclone o descarga)
  → read_file convierte (y avisa si es escaneado → OCR decide aparte)
  → skill analizar-fuente: tipo, fecha, emisor, hechos con página, entidades
  → ficha en raw/ con frontmatter + fila en Fuentes-Inbox con Creador/Categoría
  → log + índice actualizados (patrón Karpathy §1 del plan maestro)
```

El original nunca entra a git. Estado del patrón: ya especificado en [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#3. Flujo A — Análisis de fuentes que están en un Drive|IMPLEMENTACION §3]]; el Router v2 lo conecta a la hoja de fuentes.

---

# 5 · Panel web v1 — ver fuentes desde el celular (y visores VR)

## 5.1 Qué es

Página estática HTML (una sola URL) que **lee el CSV publicado** de `Fuentes-Inbox` y muestra:

```text
┌──────────────────────────────────────────────────────────┐
│  FUENTES — panel del estudio          [IA][arq][BIM][…]  │
│                                                          │
│  Chips de categoría + veredicto + creador                │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🟣 ComfyUI Tripo + GPT + Seedance     YT  · IA     │  │
│  │    canal: ComfyUI oficial  ·  aporte  ·  14-oct    │  │
│  │ 🔴 Shenzhen FCC 64.000m²               IG · arq    │  │
│  │    @todo_sobre_arquitectura · aporte · 15-oct      │  │
│  └────────────────────────────────────────────────────┘  │
│  Creadores · Sugerencias · Última sync: hoy 07:05        │
└──────────────────────────────────────────────────────────┘
```

* **Fuente de datos**: `Publish to web` del Sheet (CSV público de solo lectura) → el panel lo fetch-ea y renderiza. Sin backend, sin base de datos, sin pagar nada.
* **FLOSS**: HTML + JS vanilla (sin framework) servido donde ya servimos web (activos/web o VPS).
* **Acceso móvil/VR**: es una web — se abre del celular, tablet, o navegador de un visor VR sin instalar nada.
* **Escalado**: cuando el panel v1 ande, se integra al dashboard 3-paneles del plan maestro (Inbox tab = este panel); cuando llegue Hermes, el cron 07:00 alimenta la sección Sugerencias.

## 5.2 Niveles

Publicar el CSV de fuentes por link = nivel D puntual (una vez, datos de fuentes públicas que ya compartiste por Telegram — decidís vos). Alternativa sin publicación: el panel lee vía Service Account (Fix B) con endpoint mínimo — mes 2 si la publicación no te cierra.

---

# 6 · Orden de construcción (bloques con s)

| Bloque | Qué | Depende de |
|---|---|---|
| **C1 · Credenciales** | Fix A (publish app) + Fix B (SA para Sheets) — 15 min | nada — primero, destraba todo |
| **C2 · Router v2** | columnas Creador/Categoría + Clasifica + ack v2 | C1 |
| **C3 · Contactos** | tab Contactos + inyección en agenda + en minuta | C1 ( lectura SA) |
| **C4 · PDF→fichas** | rama PDF del Router + skill analizar-fuente | C2 |
| **C5 · Panel v1** | HTML + CSV publicado + chips | C2 (columnas nuevas) |
| **C6 · Creadores+Sugerencias** | tab Creadores + cron semanal de sugerencias | C2 |

Bloques C1-C3 caen dentro del sprint de 2 días del plan maestro (suman ~2h); C4-C6 la semana siguiente.

## Referencias

* [[specs/261111-plan-maestro-studio-os|Plan maestro]] §7 · [[specs/archived/261111-sistema-backend-vault-hermes|backend vault]] (dashboard, Karpathy) · [[specs/archived/261111-sistema-filosofico-practico-arquitectura|sistema filosófico]] §4 (bracitos: este spec opera en el bracito scripts + flujos n8n; el panel es la vista gráfica de avance) · [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|MVP_06]] (Router, STT, credenciales) · [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura Router]]
