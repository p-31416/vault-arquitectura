---
tipo: plan
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
estado: borrador
tags: [automatizaciones, inventario, fathom-dual, comfy, filosofia]
idioma: es
---

# Inventario automatizaciones Mes 1 — qué hay, qué falta, cuánto ahorra

> Filosofía: el valor no son las horas trabajadas sino la capacidad liberada + lo imposible sin sistema (ej: ver un link online, mandarlo al grupo, que se analice solo y se recuerde dónde quedó — manualmente imposible). Cada flujo: estado, evidencia, pendiente.

## 1. Telegram Router (VERIFICADO 16/10 vía MCP n8n, 17 nodos reales)

`YWpuV5p0vCDTbIHz`, activo, editado hoy 12:46. Cadena real:
Recibo Mensaje (trigger) → Route Identidad → [Sol → Run Voz Agent | resto → Route Fuentes Group → [Has Link → Prepara Fila → **Extrae Jina** → **Parsea Info** → Append Fuentes Sheet2 → Ack | fallback → Route Telegram Command → [Run Fathom Sync | Send Help]]] + 4 stickies.
Confirmado: **sin `/agendar`, sin Cancel/Modif** (solo Fathom + Help en comandos). Novedad vs v1.3: Jina (extrae artículo del link) + Parseo antes del Sheet.
Evidencia: `get_workflow_details` 16/10. Pendiente: agregar a Emilia al grupo, mover Sheet a `OS-Emilia/`.

## 2. Agente Voz + Agenda (VERIFICADO 16/10 vía MCP, activos)

**Voz TEST `Gpd6NHB4HQdU7ary` (26 nodos: 24+2 notas):** trigger → Detectar Entrada → [Descargar Voz → Transcribir (Google Gemini) → Fijar Texto | Fijar Texto Escrito | callback] → Normalizar → Fijar Contexto → Guardar Mensaje **Redis** → Esperar Lote → Recuperar Redis → Armar Lote → **Agente Voz (OpenRouter Modelo Free + Memoria Postgres + tools Fathom/Agenda)** → Responder Telegram + Limpiar Lote. Sheets `buscar_contacto` y `agregar_contacto` (googleSheetsTool) viven en el Voz.
**Agenda Sub TEST `ygdjqRfXpxKMFWEN` (12 nodos: 11+1 nota):** Agente Agenda (OpenRouter + BufferWindow) + 6 tools Cal.com http (disponibilidad, reuniones, agendar online/presencial, actualizar, cancelar) + Google Calendar tool.
**Limpiar Memoria `uOonS1LWzowvwyns` (6 nodos: 4+2 notas, INACTIVO):** Postgres consultar/borrar sesión + verificar + Redis borrar.
**SET_01 Cuadro carpinterías `VIQmMEZ9tkDBfKjd` (12 nodos, activo, editado hoy 00:55):** webhook → Drive busca/crea planilla → code arma matriz → http escribe rango → mueve carpeta. Es el conteo bloques→planilla corriendo.
**Fathom Core:** cron 07:00 AR corriendo con success diario incl. hoy 16/10 (execs 3564→3772, 26 totales). Sin cambios desde 09/10.

## 2b. Bot personal — despiece a medir por Sol (manual vs sistema, cada verbo cuenta):
* Pedido por voz/texto → parseo (manual: abrir Cal.com + tipear).
* Búsqueda contacto en Sheet (manual: 10 min entre buscar y confirmar).
* Creación booking + invitación (manual: 5 min).
* Confirmación y aviso.
**Total manual fijado por Sol: 15 min por reunión** (10 antes + 5 después, o 15+15 en semanas cargadas; no inflar). Con sistema: 1 mensaje. **Ahorro: ~14 min × 8/mes ≈ 2hs/mes.** Quick win: medir 1 real esta semana y anotar.

## 3. Agente de Emilia (pendiente Mes 2) — credenciales faltantes

Propio, por texto y por voz (agendamiento + fuentes). Checklist de conexión:
* [ ] API Key Cal.com de SU cuenta + evento 60 min con Google Meet (no sale por API, con ella).
* [ ] Su `chat_id` Telegram (manda `/start`, se lee de la ejecución).
* [ ] Agregarla al grupo Fuentes + Sheet `Fuentes-Inbox` compartida (ella edita E+F).
* [ ] Fathom: su cuenta ya conectada; falta la de Proyecto Pi (ver §5).
* [ ] Prueba manual de Sol: 1 agendamiento voz + 1 texto + 1 link al grupo (en curso).

## 4. Voz + memoria (según Sol, documentar en Mes 2)

Texto/voz, caché Redis, memoria largo plazo Postgres, contactos: buscar y agregar por voz/texto al Sheet, modelo GPT, agenda Cal.com + calendar. Falta: diagrama nodo por nodo como la arquitectura v1.3.

## 5. Fathom sync 07:00 (verificado, Emilia conectada) — pipeline completo

Cron diario + `/sync`: trae últimas 26h, clasifica Internas/Clientes, guarda .md (crudo para vault) + Google Doc. Credencial: **Emilia** (confirmado por Sol).
Lo que falta del pipeline (quick wins ordenados):
1. Drive → crudo: script `import_drive_reuniones.py` existe; falta cron/cableado para que entre solo a `raw/reuniones/`.
2. Análisis por agente (fathom-pm): minuta → tasks, hoy manual.
3. Subida a Leantime en tasks de 30 min (metodología Mes 2).
4. Mail resumen a Emilia: Fathom ya manda automático, pero se puede mejorar y personalizar (plantilla propia con próximos pasos).
> Conteo n8n UI = nodos funcionales + sticky notes. Router 17 (13+4) · Voz 26 (24+2) · Agenda 12 (11+1) · Limpiar 6 (4+2) · SET_01 12 (12+0).
Falta: conectar Fathom de Proyecto Pi. **Dedup**: el mismo meeting grabado en 2 cuentas genera 2 `recording_id` distintos (dual 17/09 verificado) → el dedup NO es por ID sino por fecha/hora+título+participantes. A evaluar antes de conectar el segundo.

## 6. Mantenimiento + worker (comparativa pedida por Sol)

Router/flujo chico: borrado de memoria del agente y reintentos. **Worker fuentes→crudo en preparativo.**
* Dentro n8n: cron+code nativo, vive con las credenciales, costo cero. Límite: sin funciones en expresiones, payloads simples.
* Fuera (script propio): Python libre + LLM a gusto para PDF/OCR pesado; hay que hostearlo y darle credenciales.
* Regla: determinista y programado adentro; pesado o con IA, afuera con gate `s/N`.
Falta definir: qué analiza (resumen vs full), dónde escribe, frecuencia, gate.

## 7. Minutos salvados (base para pasar números)

| Flujo | Manual | Con sistema | Ahorro |
|---|---|---|---|
| Agendar reunión | 15 min (10 antes + 5 después; 15+15 en cargadas) | 1 mensaje | ~14 min × 8/mes ≈ 2hs/mes |
| Traer reunión Fathom | 45 min (ver + resumir + archivar + pasar al crudo) | 0 (cron + .md + Doc) | ~45 min × 11/mes ≈ 8hs/mes |
| Fuente online → memoria | imposible (se pierde) | link al grupo + análisis solo | ∞ (capacidad nueva) |
| Croquis (Comfy, a validar Mes 2) | 60 min aceitado (volumetría+render+croquis+scan+Photoshop; 180→120→60 con práctica) | ~1 min proceso LoRA | **60X** |

## 8. Decisiones a definir (guía)

1. Worker: alcance, destino, frecuencia, gate.
2. Pi Fathom: conectar sí/no + regla dedup por fecha/título (nunca por ID).
3. Agente Emilia: cuenta Cal.com + grupo + prueba.
4. Comfy: validar 60X con 1 croquis real (medir ambos tiempos) antes de prometerlo.
5. Minutos: pasar esta tabla a la calculadora como segundo caso (hoy solo cubre n8n).
