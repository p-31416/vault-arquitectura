---
tipo: legal
fecha_creacion: 2026-09-12
ultima_actualizacion: 2026-09-12
tags: [legal, datos-personales, dpa, studio-os]
idioma: es
---

# DPA — Acuerdo de Encargado del Tratamiento (art. 25 Ley 25.326)

> Texto base para firma (2 carillas). Anexo del [[wiki/legal/contrato-servicios-studio-os|Contrato Marco]]. Original firmado en `/activos/documentos-legales/STUDIO_OS-Emilia/`.

## Roles

**RESPONSABLE:** Estudio de Emilia Pimenta (decide fines y medios sobre datos de sus clientes, agenda y equipo).
**ENCARGADO:** PITAUTECH (trata datos por cuenta y orden del RESPONSABLE, solo con instrucciones documentadas, en su VPS y herramientas).

## 1. Datos alcanzados

Contacto y CRM (nombres, mails, teléfonos), calendario y disponibilidad, reuniones grabadas (voz, imagen, transcripción Fathom), contenido del Vault, métricas de uso. Incluye datos de terceros (caso Nayara — Brasil).

## 2. Finalidad e instrucciones

Solo alimentar la memoria computable del estudio: flujo Fathom → raw/reuniones/ → wiki/fuentes/ → Leantime → Bóveda. Los datos del estudio jamás se usan para entrenar modelos ni para otros clientes.

## 3. Subencargados autorizados

Contabo (VPS, UE), Fathom (transcripción, EEUU), Cal.com (agenda, EEUU), Google (Drive/Calendar/Meet, EEUU), GitHub (repositorio privado, EEUU), OpenRouter/OpenAI (modelos OpenCode Zen/Muse Spark y ChatGPT, EEUU). n8n y Leantime corren self-hosted en el VPS (internos). Cambios con aviso y derecho de oposición en 15 días.

## 4. Transferencias internacionales

El RESPONSABLE consiente las transferencias a UE y EEUU listadas (arts. 5 y 60 Ley 25.326). Fase conceptual bajo secreto profesional se procesa solo en local (ComfyUI/Ollama, sin transferencia).

## 5. Medidas y plazos

Acceso mínimo por rol, 1 asiento Leantime, cifrado en tránsito, separación por cliente, backups. Crudos de reunión <24hs, luego solo minuta curada. Brechas: aviso en 72hs a AAIP y titulares.

## 6. Cierre

Al fin del programa: devolución del Vault exportable + borrado certificado del VPS y herramientas. Derecho de auditoría de logs para el RESPONSABLE.

## Referencias

- AAIP Protección de datos — https://www.argentina.gob.ar/aaip/datospersonales
- Transferencias internacionales — https://www.argentina.gob.ar/transferencias-internacionales
