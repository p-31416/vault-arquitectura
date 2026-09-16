---
tipo: empresa
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-06-28
tags: [lidia, tecnologia, decision, privacidad, arquitectura, workflow, datos-sensibles]
fuentes: []
---

# Decisión: Arquitectura de Trabajo, IA y Privacidad de Datos

> Cómo organizar el trabajo con IA según el nivel de confidencialidad de los datos. Cubre: flujo de datos actual, comparación de modelos (DeepSeek vs Claude vs local), hardware necesario, y modelos de negocio para clientes con datos sensibles (ej. estudios de arquitectura).

---

## 1. ¿Qué es cada cosa?

### Setup actual: Opencode + DeepSeek API

| Componente | Qué es |
|------------|--------|
| **Opencode** | Herramienta open source (MIT) que corre en tu terminal. Conecta cualquier modelo LLM a tu código/archivos. No guarda datos. |
| **DeepSeek V4 Flash** | Modelo de IA chino, vía API. $0.14/M input, $0.28/M output. 1M contexto. |
| **Skills** | Sistema abierto de skills (ingest, query, lint, brand-voice, etc.) — cualquier contribuyente puede crear |

### Alternativa: Claude Code

| Componente | Qué es |
|------------|--------|
| **Claude Code** | Producto cerrado de Anthropic. Terminal + IDE + web. Usa modelos Claude (Sonnet, Opus). |
| **Modelos Claude** | Sonnet 4.6: $3/$15 MTok. Opus 4.8: $5/$25 MTok. |

---

## 2. Tabla comparativa

| Aspecto | Opencode + DeepSeek (actual) | Claude Code |
|---------|------------------------------|-------------|
| **Código** | Open source (MIT) | Cerrado (propietario) |
| **Costo API** | $0.14/$0.28 MTok (Flash) | $3/$15 MTok (Sonnet) |
| | $1.74/$3.48 MTok (Pro) | $5/$25 MTok (Opus) |
| **Costo plan** | Solo API (no hay plan) | Pro $20/mes o API |
| **Contexto** | 1M tokens (nativo) | 200K tokens |
| **Skills/plugins** | Sistema abierto de skills | Skills integradas (cerradas) |
| **MCP** | Sí | Sí |
| **Sub-agentes** | Sí (Task tool) | Sí |
| **Modelos** | Cualquiera (DeepSeek, Claude, GPT, local) | Solo Claude |
| **Open weights** | Sí (DeepSeek se puede auto-hospedar) | No (cerrado) |
| **Origen servidores** | China | EE.UU. |

---

## 3. Privacidad y uso de datos para entrenamiento

### DeepSeek API (setup actual)
- **API no usa datos para entrenar por defecto**. DeepSeek lo declara explícitamente.
- Se puede firmar DPA (Data Processing Agreement) para uso enterprise que garantiza cero entrenamiento.
- Servidores en China. Esto puede ser un problema regulatorio para clientes con requisitos de residencia de datos.
- DeepSeek tiene certificaciones ISO 27001, SOC 2 (enterprise).
- **Riesgo real**: la data viaja a servidores en China. Para datos sensibles de clientes, hay que evaluar si esto es aceptable.

### Claude (Anthropic)

**Planes de consumo (Free, Pro, Max):**
- Por defecto: tus chats **SÍ se usan para entrenar** a menos que hagas opt-out manual
- Opt-out: debes ir a Privacy Settings → desactivar "Help improve Claude"
- Si optás out: retención de 30 días
- Si optás in: retención de hasta 5 años
- **Conversaciones marcadas por safety se usan para entrenar aunque hayas optado out**
- Claude Code desde cuenta Pro = mismo tratamiento (datos usados para entrenar)

**Planes comerciales (Team, Enterprise, API):**
- Por defecto: **NO se usan datos para entrenar**
- Aplica a Claude for Work, Anthropic API, Claude Gov
- Se puede firmar DPA
- Servidores en EE.UU.

### Ollama / Local (100% privado)

| Aspecto | Valor |
|---------|-------|
| **Datos** | Nunca salen de tu máquina |
| **Entrenamiento** | No. No hay servicio remoto. |
| **Costo** | Solo hardware (GPU + electricidad) |
| **Calidad** | Modelos open-source (Llama 4, Qwen 3.5, Mistral, DeepSeek open weights) |
| **Rendimiento** | Depende del hardware — modelos 7B-70B viables con GPU moderna |

---

## 4. Costos estimados

Basado en uso típico de Opencode como agente del vault (sesiones largas con ~500K tokens de contexto cada una):

| Escenario | DeepSeek V4 Flash | Claude Sonnet 4.6 | Claude Opus 4.8 |
|-----------|-------------------|-------------------|-----------------|
| **Por sesión típica** (~500K in, ~50K out) | ~$0.084 | ~$2.25 | ~$3.75 |
| **50 sesiones/mes** (uso moderado) | ~$4.20 | ~$112 | ~$187 |
| **200 sesiones/mes** (uso intensivo) | ~$16.80 | ~$450 | ~$750 |

DeepSeek es **~35-100x más barato** que Claude por token.

Si se usara plan Pro de Claude ($20/mes) + Claude Code incluido:
- Beneficio: costo fijo, no por token
- Limitación: los datos van a entrenar modelos a menos que hagas opt-out manual
- No aplica para uso comercial/empresa (solo consumer plan)

---

## 5. Ventajas y desventajas

### Opencode + DeepSeek (actual)

**Ventajas:**
- Costo drásticamente menor (~$4-17/mes vs ~$112-450/mes)
- Open source — podés auditar, modificar, contribuir
- Skills personalizables (los que ya tenemos funcionando)
- DeepSeek V4 Flash tiene 1M de contexto (vs 200K de Claude)
- Podés cambiar de modelo sin cambiar de herramienta (DeepSeek → Claude API → local)
- DeepSeek tiene open weights — se puede auto-hospedar si es necesario

**Desventajas:**
- Servidores en China — riesgo regulatorio para clientes que exijan residencia de datos
- DeepSeek es menos conocido/venerado que Claude (percepción de marca)
- Calidad del modelo puede ser inferior en tareas muy complejas de razonamiento
- No hay un "plan" fijo — pagás por token, puede escalar con uso intensivo

### Claude Code

**Ventajas:**
- Modelo Claude Sonnet/Opus — considerado estado del arte en razonamiento y coding
- Datos en EE.UU. (más aceptable para clientes argentinos que China)
- Plan comercial (Team/Enterprise): sin entrenamiento con tus datos por defecto
- Integración directa con ecosistema Anthropic
- Percepción de marca más fuerte para clientes enterprise

**Desventajas:**
- Costo 35-100x mayor que DeepSeek
- Cerrado — no podés ver cómo funciona ni modificarlo
- Solo usa modelos Claude (no podés switchear)
- Plan Pro ($20/mes): tus datos se usan para entrenar por defecto (opt-out manual necesario)
- Sin skills personalizables como tenemos en Opencode
- Contexto limitado a 200K tokens

---

## 6. Preguntas para la decisión

Respondé estas preguntas para determinar si vale la pena pagar Claude:

### Sobre privacidad de datos

1. **¿Algún cliente actual o potencial te exige que los datos no salgan de Argentina?** → Si la respuesta es SÍ, ninguna API cloud es suficiente. Necesitás Ollama + modelo local.
2. **¿Algún cliente exige que los datos no vayan a China específicamente?** → DeepSeek no es viable. Claude API (comercial) o local son las opciones.
3. **¿Tus clientes son inmobiliarias pequeñas/medianas que no preguntan por esto?** → DeepSeek API alcanza. La probabilidad de que un cliente inmobiliario medio te pida auditoría de datos es baja.

### Sobre calidad del modelo

4. **¿En las sesiones de trabajo, sentís que DeepSeek no entiende algo que Claude entendería?** → Si has tenido frustración recurrente, vale probar Claude.
5. **¿Las tareas que hacés conmigo son principalmente: leer documentos, estructurar información, escribir archivos .md?** → DeepSeek V4 Flash es suficiente para esto. Claude no haría un trabajo notablemente mejor.
6. **¿Estás haciendo tareas de código complejo (n8n, Python, integraciones) donde un error de razonamiento cuesta horas?** → Claude podría justificarse aquí.

### Sobre costo

7. **¿Tu presupuesto mensual para herramientas IA es flexible o acotado?** → DeepSeek: ~$5-20/mes. Claude API: ~$100-500/mes.
8. **¿Preferís un costo fijo mensual (plan) o pagar por uso?** → Claude Pro $20/mes es fijo pero tus datos entrenan. Claude API no tiene plan fijo, es por token.
9. **¿Cuántas horas por semana usás el agente?** → Si son muchas horas, DeepSeek es la opción económicamente racional.

### Sobre flexibilidad futura

10. **¿Querés poder cambiar de modelo sin cambiar de herramienta?** → Opencode soporta cualquier modelo (DeepSeek, Claude, GPT, Gemini, local). Claude Code solo Claude.
11. **¿Te importa que la herramienta sea open source?** → Opencode sí, Claude Code no.
12. **¿Planeás tener más personas usando el agente (Matio, futuro equipo)?** → Con Opencode cada uno necesita su propia API key. Con Claude Team son $25/asiento/mes.
13. **¿Considerás que el skill "brand-voice" o "article-writing" pueden ser útiles para contenido de LidIA?** → Esos skills existen en Opencode, no en Claude Code.

---

## 7. Recomendaciones según perfil

| Perfil | Recomendación |
|--------|---------------|
| **Bootstrapping, sin clientes con exigencias de datos** | ✅ Seguir con Opencode + DeepSeek |
| **Cliente pide residencia de datos en Argentina** | 🔄 Opencode + Ollama (modelo local en VPS) |
| **Cliente pide "no China"** | 🔄 Opencode + Claude API (comercial, no entrena) |
| **Necesitás máxima calidad de razonamiento** | 🔄 Opencode + Claude Sonnet 4.6 (solo cambiar API key en config) |
| **Querés plan fijo sin preocuparte por tokens** | ⚠️ Claude Pro $20/mes + opt-out manual de entrenamiento. O Claude Team $25/asiento. |
| **Cero tolerancia a datos fuera de tu control** | ✅ Opencode + Ollama (100% local, VPS propio) |

---

## 8. Caso especial: datos altamente confidenciales (ej. estudios de arquitectura)

> Planos, imágenes de proyectos, diseños de clientes, propiedad intelectual — datos que **no pueden salir de su infraestructura bajo ningún concepto**.

### El problema real

No importa cuánto confíes en la API que uses (DeepSeek, Claude, GPT). Cuando enviás datos a un servidor externo:

1. **Los datos salen de la máquina** — viajan por internet a un servidor que no controlás
2. **Los términos pueden cambiar** — mañana actualizan la política y lo que no se usaba para entrenar, ahora sí
3. **Un breach del proveedor** expone los datos
4. **GitHub privado** tampoco es suficiente — el repo existe en servidores de Microsoft

La única garantía real: **que los datos nunca salgan de la máquina del cliente**.

### Dos perspectivas distintas

Es clave separar dos casos porque cambia completamente la arquitectura:

| | **Para vos / LidIA** | **Para un estudio de arquitectura (cliente)** |
|---|---|---|
| **Hardware** | Tu PC (quizás sin GPU). VPS (sin GPU). | La PC del estudio. **Comprada por ellos**. |
| **Presupuesto** | $10-100/mes | Tienen presupuesto para hardware profesional |
| **Datos** | Wiki, leads, roadmap | **Planos, imágenes, PI de sus clientes** |
| **Restricción** | Ninguna específica (hoy) | **Cero datos pueden salir** |

### Para el cliente: la solución es su hardware

Si un estudio de arquitectura necesita procesar planos con IA **sin que los datos salgan de su red**, la solución no es tu VPS. Es **su PC con GPU**:

```
PC del estudio de arquitectura
    │
    ├── GPU: RTX 3060/4060+ (12-16GB VRAM)
    │   → $300-500 una sola vez (lo compra el cliente)
    │
    ├── Ollama + modelo 7B-14B
    │   → DeepSeek open weights, Qwen 3.5, Llama 4
    │   → Corre a 30-50 tok/s (fluido)
    │
    ├── Opencode + Ollama
    │   → Procesa planos, extrae metadatos, genera docs
    │   → Cero llamadas a internet
    │
    └── Gitea local (opcional)
        → Git interno sin GitHub
```

| Componente | Costo (una vez) | Lo paga |
|------------|----------------|---------|
| GPU (RTX 4060 12GB) | ~$350 | El cliente |
| Ollama + modelo | Gratis | — |
| Opencode | Gratis (open source) | — |
| Instalación y config | Horas de consultoría | El cliente (vos) |

**Vs. pagar API por meses**: en 3-4 meses de API (~$300-450) ya pagaste la GPU. El cliente tiene GPU propia, datos seguros, y cero dependencia mensual.

### Para vos / LidIA: la solución es híbrida

Tu máquina quizás no corre Ollama bien. Tu VPS tampoco. Pero tampoco necesitás privacidad absoluta para el vault interno. Entonces:

```
Para LidIA: DeepSeek API (setup actual)
    → $5-20/mes, datos salen pero no son planos de nadie
    → Si algún cliente sensible aparece, se evalúa caso a caso

Para ese cliente: Opencode + Ollama en su PC con GPU
    → Vos instalás, configurás, y facturás la consultoría
    → Ellos tienen su agente local, 100% off-line
    → Nadie más ve sus datos
```

### Hardware real necesario para modelos locales

**Correr modelos local requiere recursos.** No es magia. Esto es lo que necesita cada tamaño de modelo:

| Modelo | Tamaño | RAM mínima | GPU recomendada | Velocidad esperada | Calidad |
|--------|--------|-----------|-----------------|-------------------|---------|
| **Qwen 2.5 7B / Mistral 7B** | 7B | 8GB RAM | GPU 8GB+ (RTX 3060) | 5-15 tok/s CPU / 40-60 tok/s GPU | Buena — estructurar documentos, clasificar |
| **Qwen 3.5 14B / DeepSeek V3 Q4** | 14B | 16GB RAM | GPU 12GB+ (RTX 4060) | 2-6 tok/s CPU / 30-50 tok/s GPU | Muy buena — analizar planos, extraer datos |
| **Qwen 3.5 32B / Llama 4 70B Q4** | 32-70B | 32GB RAM | GPU 24GB+ (RTX 4090) | 1-3 tok/s CPU / 15-30 tok/s GPU | Excelente — comparable a Claude |

**Para un estudio de arquitectura**, un modelo 14B (Qwen 3.5 o DeepSeek open weights) alcanza bien:

- Extraer metadatos de planos
- Generar descripciones de proyectos
- Clasificar imágenes
- Responder preguntas sobre documentación

Corre en una **RTX 4060 (~$350)** a buena velocidad.

### Niveles de confidencialidad

| Nivel | Dueño del hardware | Stack | Garantía |
|-------|-------------------|-------|----------|
| **LidIA interno** | Vos (VPS) | GitHub privado + DeepSeek API | No entrena, pero pasa por externo |
| **Cliente estándar** | Vos (VPS) | GitHub privado + Claude API comercial | No entrena, EE.UU. |
| **Cliente sensible** | **Él** (su PC) | Opencode + Ollama en su máquina | **Cero datos salen de su red** |
| **Estudio arquitectura** | **Él** (su PC con GPU) | Opencode + Ollama + sin internet | **Total — datos nunca existen fuera** |

### Costos reales

| Opción | Costo | Privacidad | Rendimiento | Para quién |
|--------|-------|------------|-------------|------------|
| **DeepSeek API** | ~$5-20/mes | Media (China) | Excelente | LidIA (vos) |
| **Claude API comercial** | ~$100-500/mes | Media (EE.UU.) | Excelente | Clientes sin restricción |
| **Ollama en PC del cliente (GPU propia)** | **GPU $350 una vez** + $0/mes | **Total** | Excelente | **Estudios, datos sensibles** |
| **Ollama en VPS sin GPU** | $30-50/mes | Total | Bajo (lento) | No recomendado |

### Modelos de negocio para clientes con datos sensibles

**Opción A — Todo en la máquina del cliente (recomendada para estudios)**

```
El cliente compra una GPU (RTX 4060 ~$350)
    → Vos instalás Opencode + Ollama en su máquina
    → Ellos procesan localmente: planos, imágenes, documentos
    → Vos facturás consultoría de instalación + soporte
    → Cero datos salen de su PC
```

| Para el cliente | Para vos |
|----------------|----------|
| Compra GPU una vez (~$350) | Facturás instalación + configuración |
| Sin costo mensual recurrente | Facturás soporte si lo necesita |
| Datos 100% seguros en su máquina | No necesitás hardware propio |
| Dependencia técnica: vos | Relación comercial sin riesgo de datos |

**Opción B — El cliente te financia una workstation para vos**

El cliente te **compra una PC de escritorio dedicada** para que trabajes sus datos. La máquina es de ellos, pero está físicamente con vos (o en tu oficina).

```
Cliente paga PC con GPU (~$1200-1800 una vez)
    │
    ├── PC dedicada para el proyecto de ese cliente
    │   ├── GPU: RTX 4070+ (a partir de 12GB VRAM)
    │   ├── RAM: 32GB
    │   ├── Disco: 1-2TB NVMe
    │   └── SO: Windows/Linux
    │
    ├── Trabajás desde esa máquina
    │   ├── Ollama + modelo 14B-32B (fluido con GPU)
    │   ├── Opencode (local, sin APIs externas)
    │   ├── Vault del cliente en esa PC (no sube a ningún lado)
    │   └── Nada de lo que hacés sale de ahí
    │
    └── Beneficio para el cliente
        ├── Datos nunca salen de su propiedad (la PC es de él)
        ├── GPU dedicada a su proyecto (no compartida)
        └── No necesita aprender ni mantener nada
```

| Ventajas | Desventajas |
|----------|-------------|
| Trabajo fluido con GPU dedicada | Ocupa espacio físico |
| Datos nunca salen de la máquina del cliente | Una PC por cliente (si son varios) |
| Sin costos de API | Necesitás lugar físico |
| Facturás la consultoría + la PC | Logística de envío/entrega |
| El cliente descuenta la PC como gasto | |

**Comparativa de modelos**

| Aspecto | Opción A (GPU en cliente) | Opción B (te financian PC) | Opción C (API cloud, actual) |
|---------|--------------------------|---------------------------|------------------------------|
| **Dónde quedan los datos** | En la PC del cliente | En la PC que compró el cliente (en tu poder) | En servidores externos |
| **Rendimiento** | Depende GPU del cliente | Controlás vos el hardware | Excelente (modelos grandes) |
| **Costo recurrente** | $0/mes | $0/mes | $5-500/mes según API |
| **Costo inicial** | GPU ~$350 | PC completa ~$1200-1800 | $0 |
| **Escalabilidad** | Una GPU por cliente | Una PC por cliente | Una API key, escalá al toque |
| **Lo paga** | El cliente | El cliente | Vos (LidIA) |
| **Dependencia técnica del cliente** | Media (tiene la máquina) | Baja (todo lo manejás vos) | Nula (es tu setup) |

**Recomendación:** Para estudios con datos muy sensibles y presupuesto, la **Opción B** es la más potente. Te da una workstation dedicada que corre modelos 14B-32B con fluidez, sin que ningún dato salga de una máquina que pagó el cliente. Para estudios más chicos, la **Opción A** (GPU en su máquina + vos instalás) es más ligera.

**Nunca necesitás que el VPS de LidIA corra modelos localmente.** El VPS sigue siendo para git, n8n, y procesos internos de LidIA. La inferencia local va en la máquina del cliente o en la workstation que te financiaron.

---

## 9. Tu setup actual: ¿cómo fluyen los datos realmente?

> Antes de decidir entre modelos o modalidades, entendé exactamente por dónde pasa tu información hoy y qué tan segura está cada capa.

### Diagrama de flujo actual

```
VOS (tu máquina local)
    │
    ├── Antigravity (IDE / plataforma cloud)
    │   └── Tu código, archivos abiertos, entorno de desarrollo
    │       └── Antigravity ve esto (está en su servidor)
    │
    ├── Opencode (terminal, open source)
    │   └── Lee archivos de tu disco local
    │       → Envía fragments a la API de DeepSeek
    │       → Recibe respuestas y las escribe en tu disco
    │   └── NO guarda nada en servidores externos
    │
    ├── DeepSeek API (modelo)
    │   └── Recibe: prompts + contexto de tu vault
    │         (fragments de .md, .txt, lo que estés procesando)
    │   └── Procesa: en servidores en China
    │   └── Devuelve: respuestas
    │   └── Política: NO usa datos para entrenar (API)
    │
    └── Vault (archivos .md en tu disco)
        ├── raw/ + wiki/ → git push a GitHub (privado)
        └── GitHub → servidores de Microsoft (EE.UU.)
```

### ¿Qué se expone en cada capa?

| Capa | Ve tus archivos | Guarda datos | Riesgo |
|------|----------------|-------------|--------|
| **Tu disco local** | Todo | Sí | Seguro (solo vos) |
| **Antigravity** | Lo que tengas abierto en el IDE | Sí (entorno cloud) | ⚠️ **Cloud IDE** — sus servidores ven tu código abierto |
| **Opencode** | Lo que lee del vault | No (open source, no guarda) | ✅ Bajo |
| **DeepSeek API** | Los fragments que envía Opencode | No entrena (API), pero existe en sus servidores durante la request | ⚠️ Sale de tu red, pasa por China |
| **GitHub privado** | Tu vault completo | Sí (repo privado) | ⚠️ Microsoft aloja tus datos, pero nadie más los ve |

### ¿Qué tan seguro es realmente?

**Para vos / LidIA (datos internos):** Riesgo bajo. No hay información bancaria ni planos de clientes. DeepSeek no entrena con API, GitHub privado no expone nada. Es un nivel de riesgo aceptable para documentación de producto.

**Para un estudio de arquitectura con planos:** ❌ No aceptable. Los fragments viajan a China vía DeepSeek, el vault está en GitHub (Microsoft), y Antigravity como cloud IDE ve los archivos abiertos. Demasiadas superficies de exposición.

### El problema de almacenamiento pesado (planos, renders, video)

Los archivos de arquitectura no son solo texto. Son archivos pesados:

| Tipo de archivo | Tamaño típico | Impacto en Opencode |
|----------------|---------------|---------------------|
| **Plano DWG/PDF** | 5-50 MB | Opencode no lee binarios — necesitás extraer texto/metadatos antes |
| **Render (PNG/JPG)** | 10-200 MB | Opencode no procesa imágenes — necesitás un modelo multimodal |
| **Video (MP4)** | 200 MB - 2 GB | No va por API. Imposible de enviar como contexto. |
| **Documento técnico (PDF)** | 1-20 MB | Opencode sí lee PDFs (extrae texto, hasta ~2000 líneas mostradas) |

**El cuello de botella real no es la IA, es el formato.** Opencode + DeepSeek trabajan con **texto**. Para procesar planos, renders o videos necesitás:

1. **Extraer metadatos** del archivo (nombre, fecha, tamaño, tipo) con scripts
2. **Convertir a texto** lo convertible (OCR en planos PDF, transcripción de audio)
3. **Descriptores manuales** para imágenes (el cliente describe qué hay en el render)
4. **Guardar los binarios** en el sistema de archivos (no dentro del vault git)

### Arquitectura recomendada para estudios con archivos pesados

```
PC del estudio
    │
    ├── Archivos pesados (planos DWG, renders PNG, videos MP4)
    │   └── Se guardan en carpetas aparte del vault
    │   └── NO se suben a git (solo texto va al repo)
    │
    ├── Scripts de extracción
    │   └── Extraen metadatos: nombre, fecha, cliente, tipo
    │   └── Convierten PDF a texto, extraen capas de DWG
    │   └── Generan .md con la metadata + ruta al archivo original
    │
    ├── Opencode + Ollama (local)
    │   └── Procesa solo los .md con metadata
    │   └── Nunca ve los binarios (no hace falta)
    │
    └── Wiki generada
        └── Contiene referencias a los archivos originales
        └── "Plano de planta — cliente X — ver en /archivos/planos/"
```

**Regla de oro:** en el vault solo entra **texto**. Los binarios (planos, renders, videos) se quedan en el sistema de archivos del estudio, organizados por carpeta. El vault referencia su ubicación pero no los contiene.

### Costos de almacenamiento

| Medio | Capacidad típica | Costo |
|-------|-----------------|-------|
| Disco local del estudio | 1-2 TB | Ya lo tienen |
| NAS local | 4-12 TB | $200-600 una vez |
| Google Drive / OneDrive | 1 TB (plan pago) | $10-20/mes |
| Git (GitHub) | ❌ NO para binarios | Repos con archivos pesados son impracticables |

**Git no es para archivos pesados.** Un repo con planos de 50 MB cada uno se vuelve inmanejable en días. Los binarios van al sistema de archivos, no al vault.

---

## 10. Sobre Chatwoot + WhatsApp Business API

### Pregunta: ¿hay algún problema de privacidad si la conversación sigue en Chatwoot?

**No, Chatwoot no agrega riesgo adicional.** El riesgo ya existe desde que usás WhatsApp.

**Cómo fluyen los datos con Chatwoot:**

```
Cliente envía mensaje
    → Meta Cloud (WhatsApp Business API)
        → n8n en VPS recibe webhook
            → n8n decide: responde el agente IA O deriva a humano
            → Si deriva: n8n envía el mensaje a Chatwoot
                → Chatwoot muestra la conversación al asesor humano
                → El asesor responde desde Chatwoot
                    → Chatwoot → n8n → Meta Cloud → Cliente
```

**¿Quién ve los datos?**

| Capa | Ve la conversación | Datos expuestos |
|------|-------------------|-----------------|
| **Meta (WhatsApp)** | Sí | ✅ **Nombre y teléfono del lead** — esto lo expone WhatsApp siempre. Es inherente al medio. |
| **OpenRouter / LLM** | El prompt (fragments) | Solo lo que necesita para responder. No persiste. |
| **Chatwoot** | Sí | La conversación completa, visible para el asesor humano. |
| **n8n VPS** | Sí (en memoria) | Datos en tránsito durante el flujo. |

**La pregunta real:** el nombre y teléfono del lead **ya los tiene Meta** por el simple hecho de usar WhatsApp. No hay forma de evitarlo — es el canal. Chatwoot no empeora ni mejora eso. Solo le da una interfaz al asesor para gestionar la conversación.

**Para un estudio de arquitectura:** si usan WhatsApp para comunicarse con clientes, Meta ya ve los mensajes. El riesgo adicional del LLM (OpenRouter/GPT-5 mini) es mínimo comparado con eso. Si la confidencialidad es crítica, el canal no debería ser WhatsApp — tendría que ser una app propia con cifrado extremo a extremo controlado.

---

## 11. Conclusión general

**Opencode no está atado a DeepSeek.** Esa es la clave. Podés cambiar de modelo con una línea de configuración. Hoy usamos DeepSeek porque es 35x más barato y suficiente para las tareas del vault.

La pregunta real no es "Opencode vs Claude Code". Es **"qué modelo necesito para qué tarea"**. Con Opencode podés tener ambos:

- DeepSeek V4 Flash para el día a día del vault ($4/mes)
- Claude Sonnet/Opus para tareas complejas puntuales cuando lo necesites

O directamente, si la privacidad es crítica:
- Ollama con modelo open-source en tu VPS (costo cero de API)

No hay una razón técnica para migrar a Claude Code. La flexibilidad de Opencode + la posibilidad de elegir el modelo según la tarea es más potente que un producto cerrado.

---

## 12. Referencias oficiales

- [Opencode — open source](https://github.com/anomalyco/opencode)
- [DeepSeek API Pricing](https://api-docs.deepseek.com)
- [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html)
- [DeepSeek Terms of Use](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html)
- [Claude Code overview](https://code.claude.com)
- [Claude Pricing](https://claude.com/pricing)
- [Anthropic Privacy Center — Is my data used for training? (Consumer)](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- [Anthropic Privacy Center — Is my data used for training? (Commercial)](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)
- [Ollama — Local LLM runtime](https://ollama.com)
- [CloudZero — LLM API Pricing Comparison 2026](https://www.cloudzero.com/blog/llm-api-pricing-comparison)
