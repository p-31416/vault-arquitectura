---
fecha: 2026-10-28
tema: Auditoría de Runpod (GPU cloud) para mandato "PI 100% protegida"
slug: runpod-auditoria-pi
idiomas: [es, en]
fuentes_n: 30
fuentes_citadas_n: 46
confianza: alta (legal + docs oficiales Runpod/Tailscale, precios y storage verificados 200) / media en Tailscale-dentro-de-pod (fuente oficial citada + 3 fuentes comunitarias) / baja en residency efectiva (Runpod dice "reasonable efforts")
estado: crudo
investigador: sherlock
destino: raw/contenidos/sherlock-runpod-auditoria-pi.md
wiki_probable: wiki/glosario/entidades/runpod.md + wiki/glosario/software/comfy-cloud-vs-runpod.md + wiki/glosario/conceptos/pi-protegida-cloud-gpu.md (nueva)
---

# Auditoría de Runpod (GPU cloud) — mandato «PI 100% protegida»

Fecha: 2026-10-28 · Zona: `-03:00 America/Argentina/Buenos_Aires`
Objetivo declarado: decidir si el estudio puede enviar material a Runpod bajo el mandato **«PI 100% protegida, nada se entrena, planos legales nunca en cloud»**, y dejar por escrito un perfil de pod mínimo, repetible y reversible.

**Convención de marcado** (separa hecho / interpretación / pregunta):
- **[V] Hecho verificado** — está escrito en la fuente oficial, con URL y estado HTTP.
- **[I] Interpretación** — lectura razonada del estudio, no afirmada por el proveedor.
- **[P] Pregunta abierta** — Runpod no lo documenta; hay que preguntarlo (o probarlo).

> **Advertencia de alcance.** Este informe audita **documentación pública**. Los documentos que el proveedor entrega bajo NDA (SOC 2 Type II completo, ISO 27001, informe de sub-procesores, SOC 2 Bridge Letter 2026) están en el Trust Center con **acceso aprobado**; no se leyeron. Varias conclusiones «condicional» dependen de leerlos.

---

## Resumen ejecutivo

**[V] Runpod NO entrena modelos con datos de clientes — no porque lo diga, sino porque el contrato no lo dice.** Ni la Privacy Policy (7-ago-2025), ni los Terms of Service (24-mar-2026), ni el Data Processing Agreement dicen «no entrenamos con tus datos». La palabra *train* sólo aparece en el marketing («Build, train, and scale AI workloads» = entrená *tus* modelos en sus GPUs). Lo más cercano es ToS §5: licencia de uso «in an aggregated and anonymized form to update and improve the Service», y DPA §5: procesar «solely in accordance with Customer's documented instructions and shall not process it for any other purpose». **[I]** Eso es base contractual suficiente si el DPA está firmado, pero **no es una cláusula de no-entrenamiento**: es un permiso de uso limitado.

**[V] El DPA NO está firmado automáticamente.** «To execute this DPA, Customer must complete the signature block and submit the signed DPA to Runpod via this link... This DPA shall become legally binding only upon completion of all such steps.» (DPA §1). **[I]** Para el mandato de PI, firmar el DPA no es un extra: es el primer requisito.

**[V] Hallazgo de estructura que cambia la decisión: la opción barata es una plataforma en retirada.** «Runpod is no longer accepting new hosts for Community Cloud. Existing Community Cloud resources remain available.» (docs/pods/choose-a-pod). **[I]** El precio Community ($0,22/h la 3090) corresponde a un stock que Runpod ya no amplía: la oferta y el precio van a fragmentarse. El precio Secure Cloud es 2,3× (3090: $0,50/h).

**[V] Hallazgo que endurece el mando: el cifrado de volumen no existe para network volumes.** «Encryption applies only to volume disk. Container disk and network volumes cannot be encrypted.» Y «Network volumes are only available for Pods in the Secure Cloud». **[I]** Traducción operativa: la única combinación con (a) disco persistente, (b) cifrado en reposo por volumen, y (c) Secure Cloud single-tenant, es **volume disk cifrado en Secure Cloud**. El network volume —el único que sobrevive al pod— es justamente el que no se puede cifrar y el que se sigue cobrando con el pod detenido.

**[V] No hay región UK ni LATAM en la lista oficial de data centers.** 28 data centers en el enum de `dataCenterIds`; 7 en la UE/EEE (CZ, FR, NL, RO, SE, NO, IS); ninguno con prefijo UK; ninguno en Sudamérica. **[V]** Y el DPA §4 degrada la promesa: «Where a region is specified by Customer during service instantiation, Runpod will use **reasonable efforts** to allocate a server in a geographically proximate location». **[I]** «Reasonable efforts» no es «garantía de región»: es el punto por donde el mando «PI 100% protegida» se rompe si uno lo lee al pie de la letra.

**Veredicto (detalle en §7):** Runpod **sí** sirve para renders IA y para entrenar LoRAs **sobre material propio no sensible y con licencia compatible**, en Secure Cloud + volumen cifrado + sin puertos + borrado manual al terminar. Runpod **no** sirve para planos legales firmados, material de cliente confidential, cálculos/presupuestos con datos de cliente, ni material de concurso con PI de terceros. Todo lo demás es condicional.

---

## 1. Retención y uso de datos

### 1.a Retención de logs y de red

**[V]** Privacy Policy, §Retention (completo): «We generally retain personal information to fulfill the purposes for which we collected it, including for the purposes of satisfying any legal, accounting, or reporting requirements, to establish or defend legal claims, or for fraud prevention purposes... When we no longer require the personal information we have collected about you, we may either delete it, anonymize it, or isolate it from further processing.»

- **No hay plazo numérico de retención en la Privacy Policy.** → «no documentado».
- **[V]** Privacy Policy, §Security (completo): «We employ a number of technical, organizational and physical safeguards designed to protect the personal information we collect. However, security risk is inherent in all internet and information technologies and we cannot guarantee the security of your personal information.»
- **[V]** Privacy Policy, §Data Processing outside Europe: «We are a U.S.-based company... your personal information will necessarily be accessed and processed in the U.S.» y «the US is not the subject of an 'adequacy decision' under the GDPR».
- **[V]** DPA, definición de *Performance Data*: «any log files, metadata, telemetry data, and other technical performance data automatically generated by the Service relating to the use, performance, efficacy, reliability, and/or accuracy of the Runpod Services».
- **[V]** DPA §18 (Performance Data): Runpod «may collect, use, and disclose Performance Data for its own business purposes, including: (i) accounting, tax, billing, audit, and compliance; (ii) providing, improving, developing, optimizing, and maintaining the Services...» y — crítico — «**this DPA shall not apply to Runpod's Processing of Performance Data, and Performance Data does not constitute Customer Personal Data**».

**[I]** Consecuencia directa del mandato de PI: **la retención de logs/telemetría de la plataforma no está acotada por el DPA**. El DPA protege *tu* contenido; no acota los logs del servicio. Si el log de un pod puede contener material sensible (stdout de un job, un nombre de archivo, un prompt), ese stdout cae en una categoría de retención no acotada contractualmente.

**[V]** Logs de pod: «Pods provide two log types: * Container logs: Application output (stdout) * System logs: Pod lifecycle events (startup, shutdown, errors)» (docs/pods/manage-pods). **No hay ventana de retención documentada** → «no documentado».

**[V]** Sub-procesores que tocan logs (DPA §8, Attachment 2):
- *BetterStack Inc.* — «A log monitoring platform, technical service and **Runpod application logs are sent to BetterStack** for search, analysis, and system monitoring. Sensitive data fields are masked such as usernames and emails, while some low sensitivity data such as IP and Host are captured directly.»
- *Datadog Inc.* — «A SIEM platform that provides application monitoring, infrastructure monitoring, **log management**, and alerting».

**[P]** El texto dice «Runpod application logs». No aclara si el **stdout del pod del cliente** (que se ve en la pestaña *Logs* de la consola) se reenvía a BetterStack/Datadog. Si se reenvía, hay un segundo destino de datos fuera de tu cuenta y fuera del DPA (Runpod actúa como sus propios processor). **Pregunta directa a Runpod antes de subir nada con datos sensibles.**

**[V]** Retención de red: **no documentada**. Runpod no publica política de network flow logs ni de retención de IP-level logs. No hay logs de red del cliente; sí hay «Device data... IP address» del lado de la cuenta (Privacy Policy, *Automatic data collection*), con retención genérica.

### 1.b ¿El cliente es dueño de sus datos?

**[V] SÍ, explícito y sin ambigüedad.** ToS §5 (Intellectual Property Rights): «**We do not assert any ownership over Your Content. You retain full ownership of all of Your Content** and any intellectual property rights or other proprietary rights associated with Your Content.»

Pero la licencia que se queda Runpod es (ToS §5, literal):
> «You grant Runpod a non-exclusive, worldwide, royalty-free and fully paid-up license to: (i) **access and use Your Content to operate and provide the Service to Customer**; and (ii) **use Your Content in an aggregated and anonymized form to update and improve the Service and Runpod's related products and services**.»

**[V]** ToS §2 (Use of the Service; Responsibility for Content): «You agree that we may, **but have no obligation to**, access, store, process, and use any of Your Content.» + modelo de responsabilidad compartida: «Runpod is responsible for protecting the infrastructure that provides the Service... **the Service does not include your applications or Your Content**. Under this shared responsibility model, you are responsible for protecting all data (including Your Content) both at rest and in transit, virtual machine guests, operating system(s)... as well as security configuration of the Service provided by Runpod, including but not limited to firewall, load balancer, object storage, block storage, IP and DNS configuration.»

**[V]** DPA §5 (Instructions): «Runpod shall process Personal Data for the purposes of: (i) processing as required by Customer in its use of the Services; (ii) processing in accordance with the Agreement, this DPA...; (iii) processing to comply with other reasonable instructions provided by Customer...» y «Runpod shall process such data **solely in accordance with Customer's documented instructions and shall not process it for any other purpose**.»

**[V]** Privacy Policy: «This Privacy Policy does not apply to information that we process on behalf of our business customers... Our use of information that we process on behalf of our business customers may be governed by our agreements with such customers.»

**[I]** El cliente es dueño del contenido, pero la arquitectura legal es de *processor* (Runpod) bajo *controller* (el estudio), con el DPA firmado y con instrucciones documentadas como la fuente de autoridad. Si el DPA no está firmado, la Privacy Policy es la que aplica y Runpod queda como controlador de los datos de la cuenta, conFinales propios (marketing, publicidad basada en intereses, "aggregated and anonymized data").

**[I]** Para el mandato de PI hay un segundo titular que suele olvidarse: **el cliente final del estudio**. Si subís material de cliente, el "cliente" del contrato es Runpod y el controlador real de esos datos es *tu* cliente, que no autorizó a Runpod. Eso es un problema de cadena de contractualización, no de Runpod.

### 1.c ¿Runpod entrena modelos con datos de clientes?

**[V] NO DOCUMENTADO — no hay ninguna cláusula de no-entrenamiento en Privacy Policy, ToS ni DPA.**

Evidencia del método: barrido literal de los tres documentos por `train | machine learning | artificial intelligence | aggregated and anonymized | improve our models`. Las únicas apariciones de *train* en ToS y Privacy Policy son copies de marketing: «Build, train, and scale AI workloads on Runpod with cloud GPUs, Serverless, and Clusters.» — es decir, **«entrená tus modelos»**, no «entrenamos con tus datos».

Lo más próximo que sí está escrito:
- ToS §5(ii): uso «aggregated and anonymized form to update and improve the Service» (y nota: **no dice «de forma agregada» en ningún punto sobre el dataset de entrenamiento**).
- Privacy Policy, §How we use your personal information: «**To create aggregated, de-identified and/or anonymized data.** We may create aggregated, de-identified and/or anonymized data from your personal information and other individuals' personal information... We may use this aggregated, de-identified and/or anonymized data and share it with third parties for our lawful business purposes.»
- Privacy Policy, *Personal information we collect* incluye «**User-generated content data**, such as photos, images, music, videos, comments, questions, messages, **works of authorship**, and other content or information that you generate, transmit, or otherwise make available on the Service, as well as associated metadata» — es decir, la categoría de dato que abarca el material del estudio.
- DPA §5: procesar «solely in accordance with Customer's documented instructions» (obligación de processor).

**[I]** Traducción operativa honesta: la prohibición de entrenar con datos de clientes **no emana de una cláusula**, emana de la combinación de (a) ToS §5(ii) —licencia limitada a prestar el servicio + forma agregada y anonimizada—, (b) DPA §5 —procesar sólo según instrucciones— y (c) la declaración pública de Runpod en su guía oficial: «Runpod's policy is that *you* control your data – they don't peek into it» y «Runpod does not actively monitor workloads on Secure Cloud». Eso es un **compromiso de hecho, no una garantía contractual nominada**.

**[P]** **Pregunta 1 a Runpod (escribible, sin costo, en <legal@runpod.io> o <help@runpod.io>):** «¿Runpod entrena, fine-tunea o usa para mejora de producto los datos, prompts, imágenes o pesos que subo a un Pod? ¿El contenido de Pods queda excluido del alcance de cualquier uso de Performance Data? ¿Pueden confirmar por escrito que el contenido de Pods, Container disks y Volumes no se usa para entrenar modelos?» — **y pedirlo por escrito** (mail con respuesta, no chat). La respuesta, adjunta al legajo de PI, convierte la interpretación en hecho documentado.

**[P]** **Pregunta 2 (bloqueante para Custom DPA):** el help center dice que la ejecución de BAAs, DPAs o términos bespoke «is reserved for customers with a **committed monthly spend of $3,000 or more**». Con un gasto de $1-2/mes, **no hay palanca contractual para exigir una cláusula de no-entrenamiento**. La única vía es la confirmación escrita.

### 1.d Qué pasa con los datos al detener un pod, y el almacenamiento persistente

**[V]** Ciclos de vida (docs/pods/manage-pods):

| Acción | Qué pasa | Cobro mientras está en ese estado |
|---|---|---|
| **Stop** | «Stopping a Pod releases the GPU and preserves data in `/workspace` (volume disk). **Container disk data is cleared.**» | container disk: **no se cobra** · volume disk: **$0,20/GB/mes** · network volume: **$0,07/GB/mes** |
| **Restart** | Reinicia el contenedor en la misma máquina; puede dejar el pod sin GPU («Zero GPU Pods») | igual que running |
| **Terminate (delete)** | «**Terminating permanently deletes all data not stored in a network volume.**» + ToS/docs: el volume disk se borra al terminar el pod | deja de cobrarse |
| **Saldo $0** | «Pods are automatically stopped when your account balance reaches $0. Pods with a network volume are stopped and their data is preserved, while **Pods without a network volume are terminated and their data cannot be recovered**» | — |

**[V]** Tipos de storage (docs/pods/storage/types + docs/pods/pricing):

| Tipo | Persistencia | Ruta | Cifrado | Precio |
|---|---|---|---|---|
| **Container disk** | se pierde en stop/restart | gestionado por el sistema | **no** (se puede cifrar el storage global AES-256) | $0,10/GB/mes (running); **no se cobra parado** |
| **Volume disk** | hasta que se **termina** el pod | `/workspace` | **SÍ** («Encrypt volume» en la creación del pod) | $0,10/GB/mes running · **$0,20/GB/mes parado** |
| **Network volume** | sobrevive al pod | `/workspace` (reemplaza al volume disk) | **NO** («Container disk and network volumes cannot be encrypted») | $0,07/GB/mes (<1 TB) · $0,05/GB/mes (>1 TB), **facturado por hora y se cobra parado** |
| **Global volume** (beta) | sobrevive al pod | `/workspace` o `/workspace-global` | no documentado | $0,09/GB/mes + IOPS |

**[V] Tres advertencias que el docs repite y que hay que internalizar:**
1. «Network volumes are **only available for Pods in the Secure Cloud**.» → usar network volume implica Secure Cloud.
2. «Network volumes must be attached during Pod creation and cannot be detached later. When attached, the network volume replaces the volume disk at `/workspace`.» → el DC del pod queda atado al del volume.
3. «if your balance stays at $0 and these charges can't be covered, the network volume **may eventually be terminated and its data cannot be recovered**».
4. «Runpod is not designed for long-term cloud storage. Back up critical data to your local machine or a dedicated storage provider.» + regla 3-2-1 recomendada.

**[V]** Cifrado (guía oficial *Keeping Data Secure*, 19-oct-2026): «Runpod automatically encrypts all data on its servers with **AES-256** encryption... Runpod uses **TLS** to secure all data in transit». Y el DPA Attachment 1 (TOMs): «Encryption is used for data in transit and at rest, and this encryption is provided by Amazon Web Services Inc. ("AWS") and Secure Cloud data centers».

**[I]** Para el mandato de PI, la recomendación operativa que sale de esta tabla es: **volume disk cifrado en Secure Cloud, sin network volume**. Se pierde la persistencia entre pods, y eso es exactamente lo que se quiere: el material no sobrevive al job.

---

## 2. Secure Cloud vs Community Cloud

### 2.1 La diferencia estructural

**[V]** ToS §4.2.1 (Community Cloud), literal:
> «Runpod offers **peer-to-peer GPU computing** that connects individual compute providers ("**Hosts**") to compute consumers (the "Community Cloud"). **Runpod has no responsibility for the actions of Hosts**, and Runpod makes no warranty that the Community Cloud Offerings will meet your requirements or be available on an uninterrupted, error-free basis. **Runpod does not make any specific uptime warranties** with respect to the Community Cloud Offerings. **Runpod is only the venue to connect Hosts with consumers, and Runpod is not a party to any interaction** between compute consumer and any Host.»

**[V]** Runpod no acepta nuevos hosts (docs/pods/choose-a-pod): «**Runpod is no longer accepting new hosts for Community Cloud. Existing Community Cloud resources remain available.**»

**[V]** Tabla oficial (docs/pods/choose-a-pod):

| | Secure Cloud | Community Cloud |
|---|---|---|
| Infrastructure | T3/T4 data centers | Peer-to-peer providers |
| Reliability | High redundancy | Variable |
| Best for | Production, sensitive data | Cost-sensitive workloads |
| Pricing | Standard | Competitive |

**[V]** Guía oficial *Keeping Data Secure* (19-oct-2026): «On Runpod, this means using *Secure Cloud* instances rather than Community instances. Community GPU pods share a host machine with other customers (they're still isolated at the software level with container tech, but for highly sensitive use cases you may want absolute isolation). **Secure Cloud gives you a dedicated machine/GPU that is not shared with others.**» y «**Your GPU and its host are single-tenant** – no other user's pods will run on the same machine. There's reduced risk of side-channel attacks or noisy neighbors.»

**[V]** Guía oficial *Hosting and Running Private AI Agents*: «Secure Cloud runs on **Runpod-owned data center hardware** with enterprise-grade isolation; **your model weights, input data, and inference outputs never leave Runpod-controlled infrastructure**».

**[V]** Ruta de datos (docs/references/security-and-compliance): «Your Pods and workers run in a multi-tenant environment with **containerized isolation**... For sensitive workloads requiring enhanced security, **Secure Cloud operates in T3/T4 data centers** with enterprise-grade security, high reliability, redundancy, and fast response times.» + «Runpod's terms of service **prohibit hosts from inspecting your Pod/worker data** or analyzing your usage patterns. Any violation results in immediate removal from the platform.»

### 2.2 Certificaciones y SLA

**[V]** Página Compliance (13-sep-2026):
- «Runpod Inc. operates an Information Security Management System certified to **ISO/IEC 27001:2022** by Sensiba LLP, an ANAB-accredited certification body. **Certificate RUN-ISMS-20260827** is valid from August 27, 2026 through August 26, 2029. Its scope is **limited to the ISMS** directly supporting Runpod's services and platform solutions... **Certification covers the management system, not individual products or services.**»
- «Runpod has also completed **SOC 2 Type II and SOC 3** examinations, and maintains **HIPAA and GDPR programs**.»
- Documentos (SOC 2 Type II, ISO 27001, SOC 3, HIPAA, GDPR, SOC 2 Bridge Letter 2026) disponibles vía Trust Center, «Some documents require approved access before download».
- «**Compliance coverage can vary by workload, region, provider, and deployment model**, so customers should confirm specific requirements with Runpod during security review.»
- «For data residency, private deployment, or region-specific requirements, **contact Runpod** so the team can review the right configuration.»

**[V]** Trust Center (trust.runpod.io, vía índice): Runpod holds «SOC 2 Type 2, SOC 3, and ISO/IEC 27001:2022, and maintains active HIPAA and GDPR programs»; **31 regiones globales** declaradas en el tagline del Trust Center.

**[V]** Certificaciones de los **datacenters** de Secure Cloud: **no documentadas individualmente**. Lo único escrito es: «Secure Cloud provides vetted infrastructure partners who meet enterprise security standards including **SOC 2, ISO 27001, and PCI DSS** certifications» (docs/references/security-and-compliance) y «The third-party data centers underlying Secure Cloud additionally maintain their own certifications» (guía de agentes). **No hay lista pública de partners ni de sus certificados.**

**[V] SLA: no hay SLA público de Pods.** El único "SLA-backed uptime" está en **Reserved Clusters** (contrato enterprise, "custom pricing", "SLA-backed uptime"). Para Pods on-demand: sin SLA; y para Community Cloud, ToS dice explícitamente «does not make any specific uptime warranties». Guía oficial (agentes): «Holding these certifications does not itself satisfy GDPR or HIPAA compliance; they demonstrate security controls are in place, which is a prerequisite, **not a substitute**, for regulatory compliance. Always confirm which certifications apply to **the specific infrastructure tier your workload runs on**, not the provider's organization as a whole.»

**[I]** Traducción para el mandato de PI: **no hay SLA de confidencialidad, de disponibilidad ni de residencia** para un Pod on-demand, ni en Secure ni en Community. La protección del dato descansa en: aislamiento de contenedor, cifrado en reposo/tránsito, y el deber de Runpod como processor. Si el estudio necesita una garantía contractual de no-revelación, el camino es Reserved Clusters / contrato enterprise — fuera de rango de gasto.

---

## 3. Regiones

### 3.1 Qué regiones existen hoy

**[V]** Enum oficial de `dataCenterIds` (API reference, `POST /v1/pods` y `POST /v1/endpoints`) — **28 data centers**:

| Región | Data centers | País |
|---|---|---|
| **UE** | EU-CZ-1 | Rep. Checa |
| | EU-FR-1 | Francia |
| | EU-NL-1 | Países Bajos |
| | EU-RO-1 | Rumanía |
| | EU-SE-1 | Suecia |
| **EEE (no UE)** | EUR-NO-1 | Noruega |
| | EUR-IS-1 / EUR-IS-2 / EUR-IS-3 | Islandia |
| **USA** | US-CA-2, US-DE-1, US-GA-1, US-GA-2, US-IL-1, US-KS-2, US-KS-3, US-NC-1, US-TX-1, US-TX-3, US-TX-4, US-WA-1 | 12 |
| **CA** | CA-MTL-1, CA-MTL-2, CA-MTL-3 | Canadá |
| **APAC** | AP-JP-1, OC-AU-1 | Japón, Australia |

- **UE: sí, 5 data centers.** (Holanda EU-NL-1 y Francia EU-FR-1 son los más razonables para el estudio por latencia desde Argentina.)
- **UK: no documentado / no existe en el enum oficial.** No hay `UK-*`. (Runpod sí ofrece **UK Addendum** del ICO en el DPA y UK GDPR en la Privacy Policy — es decir, hay cobertura legal UK pero no infraestructura UK listada.)
- **Argentina / LATAM: no documentado / no existe.** Ningún DC en Sudamérica. El enum continental de la API (`DataCenterRegion`) **sí** incluye `SOUTH_AMERICA` como valor posible de filtro, lo que sugiere que la plataforma contempla la región, pero **no hay ningún data center sudamericano publicado**.
- **[V]** `runpodctl datacenter list` es declarado «authoritative» para el set actual («Datacenter IDs are region-prefixed... `runpodctl datacenter list` is authoritative — the set grows over time»).

**[V]** Data centers **con Global networking** (17): CA-MTL-3, EU-CZ-1, EU-FR-1, EU-NL-1, EU-RO-1, EU-SE-1, EUR-IS-2, OC-AU-1, US-CA-2, US-GA-1, US-GA-2, US-IL-1, US-KS-2, US-NC-1, US-TX-3, US-TX-4, US-WA-1. **[I]** Nota: los 5 DCs de la UE están todos incluidos → **el path privado oficial funciona en la UE**.

### 3.2 Cómo se elige la región al crear un pod

**[V]** Tres mecanismos, según la superficie:
1. **Consola (web)**: en *Deploy Pod* → *Additional filters* → *Security & compliance* (seleccionar la certificación/política: el filtro muestra sólo GPUs aplicables) y el toggle **Global Networking** arriba de la página, que filtra a los pods con soporte de red privada. Además, si hay **network volume** adjunto, se elige su data center en *Storage → New Network Volume* y eso **restringe** el pod a ese DC.
2. **API**: `dataCenterIds` (lista de DCs donde puede caer el pod) + `dataCenterPriority` (`availability` —default— = responde a la disponibilidad real de la máquina; `custom` = siempre intenta los DCs en el orden que le des). Y `cloudType` (`SECURE` default / `COMMUNITY`).
3. **CLI**: `runpodctl pod create --data-center-ids "US-GA-1"`.

**[V]** Al crear un **network volume** se pide un data center, y un volume **restringe** los workers/pods a ese DC («Attaching a single network volume constrains worker deployments to that volume's datacenter»).

**[I]** El punto ciego del mando: si dejás `dataCenterPriority: availability` (el default) **no estás eligiendo región**: estás pidiendo «la región que tenga GPU libre ahora». Para que «los datos no salen de la UE» sea una decisión y no una casualidad, hay que fijar `dataCenterPriority: custom` con `dataCenterIds` = la UE, y **verificar en la consola, después del deploy, en qué DC cayó el pod**.

### 3.3 ¿Afirmación oficial sobre GDPR?

**[V]** Sí, dos, y con alcance acotado:

1. docs/references/security-and-compliance, §GDPR compliance: «**Runpod is fully compliant with the General Data Protection Regulation (GDPR) for data processed in European data center regions.** The platform implements comprehensive policies, procedures, and technical measures to meet GDPR requirements.» + «For lawful transfer of personal data outside the EU, Runpod uses appropriate mechanisms such as **adequacy decisions, standard contractual clauses, or binding corporate rules**.»
2. Catálogo v2 de data centers: cada DC expone un array `compliance` con valores `GDPR`, `ISO_IEC_27001`, `ISO_14001`, `PCI_DSS`, `HITRUST`, `SOC_1_TYPE_2`, `SOC_2_TYPE_2`, `SOC_3_TYPE_2`, `ITAR`, `FISMA_HIGH`, `HIPAA`, `RENEWABLE`, y permite filtrar `compliance=GDPR`.

**[V]** Pero la afirmación está **acotada a la región**, y el DPA la relativiza (DPA §4, *Place of Data Processing*):
> «Runpod uses third-party data hosting providers (as identified in Attachment 2) to host the Services on servers located throughout the world, including in the United States. **Where a region is specified by Customer during service instantiation, Runpod will use reasonable efforts to allocate a server in a geographically proximate location.** Where cross-border transfer cannot be avoided, legally required authorization mechanisms shall be applied.»

**[V]** Y Privacy Policy: «your personal information will necessarily be accessed and processed in the U.S.» (con sub-procesores en US: AWS, Google, Cloudflare, Datadog, Stripe, HubSpot, DigitalOcean, Snowflake, Docker, PlanetScale, BetterStack, Tinybird, Clerk).

**[I] El riesgo real, en una línea:** «GDPR-compliant for data processed in EU regions» describe el *status legal de Runpod*, no una *garantía de que tu dato no sale de la UE*. Si el dato es PI de personas (datos personales de clientes), el plano de control relevante es: ¿el material que subo es PI? Y bajo este mandato, **no lo es** (ver §7): por eso la pregunta de residencia no bloquea — porque la regla operativa es no subir PI.

**[V]** Lo que sí es exigible y está escrito: DPA §12 (Deletion): «Upon Customer's request, Runpod shall **irretrievably delete or return all Personal Data** in accordance with the Agreement, unless retention is required by applicable law.» + §13 (Information & Audit Rights) + §11 (DPIA).

---

## 4. Exposición de red

### 4.1 Cómo se desactiva o restringe el proxy público

**[V]** docs/pods/configuration/expose-ports: el proxy HTTP se habilita por el campo **«Expose HTTP Ports (Max 10)»** del template o del pod (Template → *Edit Template*; o Pod → *Edit Pod*). URL resultante: `https://[POD_ID]-[INTERNAL_PORT].proxy.runpod.net`.

**[V]** Limitaciones y comportamiento (literal):
> «The HTTP proxy route includes several intermediaries: `User → Cloudflare → Runpod Load Balancer → Your Pod`»
> - «**100-second timeout**: Cloudflare enforces a maximum connection time of 100 seconds... closes with a `524` error.»
> - «**HTTPS only**: All connections are secured with HTTPS, even if your internal service uses HTTP.»
> - «**Public accessibility**: Your service becomes publicly accessible. While the Pod ID provides some obscurity, implement proper authentication in your application.»

**[V]** Desactivarlo = **dejar el campo de puertos vacío** (no hay toggle explícito de «desactivar proxy» documentado; el proxy sólo existe si hay puertos declarados). **[I]** Y como el proxy es público por diseño, la única mitigación real es: no exponer puertos + autenticación en la app + (opcional) filtro en la consola.

### 4.2 Cómo se restringen los «Direct TCP Ports»

**[V]** Mismo campo, distinto: **«Expose TCP Ports»** en el template o pod → el pod recibe **IP pública** con mapeo de puertos (ej. `213.173.109.39:13007 -> :22`). Notas oficiales:
- «Public IP addresses **may change for Community Cloud Pods if your Pod is migrated or restarted**, but they **should remain stable for Secure Cloud Pods**.»
- «External port mappings **change whenever your Pod resets**.»
- Puertos simétricos: declarar un número **≥ 70000** para pedir mapeo interno=externo; se leen de `RUNPOD_TCP_PORT_<n>`.
- «Pods do not support UDP connections.»

**[I]** Los Direct TCP Ports son **la superficie de ataque más grande**: IP pública + puerto abierto + sin WAF. Para el mandato de PI, la regla es **no exponer TCP ports**, y el único acceso remoto es el **SSH proxied** (§4.4).

### 4.3 La forma oficial de exponer un servicio sólo en red privada

**[V] Global networking** (docs/pods/networking) — es la respuesta oficial de Runpod:
- «Global networking creates a **secure, private network** that connects all your Pods within your Runpod account... as if they were on the same local network, regardless of their physical location across different data centers.»
- «provides each Pod with a **private IP address accessible only to other Pods in your account**. This creates an isolated network layer **separate from the public internet**... The network operates at **100 Mbps** between Pods, providing reliable connectivity... while maintaining security through **complete isolation from external networks**.»
- DNS interno: `POD_ID.runpod.internal` (ej. `abc123xyz.runpod.internal:5432`).
- «Services running on networked Pods are automatically accessible to other Pods **without exposing ports publicly**. Simply bind your service to all interfaces (`0.0.0.0`) and connect using the internal DNS name.»
- Best practice oficial: «**Never expose ports on Pods running sensitive services** like databases, cache servers, or internal APIs; instead, use global networking for these components.»
- Limitaciones: «only available for **NVIDIA GPU Pods**»; 17 data centers (los 5 de la UE incluidos); 100 Mbps.

**[I] Y acá está la limitación de fondo:** Global networking es **pod ↔ pod dentro de la misma cuenta Runpod**. **No da acceso desde el estudio** (la PC del estudio o el servidor del estudio). Para llegar desde el estudio a un pod sin abrir puertos, la vía oficial documentada es el **SSH proxied** de Runpod.

### 4.4 Acceso desde el estudio sin abrir puertos (ruta oficial Runpod)

**[V]** docs/pods/configuration/use-ssh: «**All Pods provide a basic SSH connection that is proxied through Runpod's systems.** This method does not support commands like SCP or SFTP.» → comando: `ssh [POD_ID]-[PUERTO]@ssh.runpod.io -i ~/.ssh/id_ed25519`.

**[V]** El SSH con IP pública («SSH over exposed TCP») es **otro camino** y requiere `Expose TCP Ports: 22` + sshd dentro del pod → **[I] queda PROHIBIDO por el perfil de pod** (§7).

**[I]** La combinación que sí es auditable: **SSH por `ssh.runpod.io` + port-forward local de SSH**. El tráfico va por los sistemas de Runpod (que son un sub-procesador del stack), no por un puerto público del pod. No es una VPN, pero no expone superficie pública del pod.

### 4.5 Tailscale DENTRO de un pod

**[V] Runpod NO documenta Tailscale.** Verificado sobre el índice oficial completo de la documentación (`https://docs.runpod.io/llms.txt`): la única coincidencia de «private network» es *Global networking*. **No existe ninguna página de Runpod sobre Tailscale, WireGuard, VPN ni acceso remoto por overlay.** Esto es un dato duro y hay que decirlo así en el legajo: **cualquier receta de Tailscale en Runpod es de terceros, no del proveedor**.

**[V] Lado Tailscale (oficial)** — *Userspace networking mode (for containers)* (tailscale.com/docs/concepts/userspace-networking, validado 12-nov-2025):
- «Tailscale works on Linux systems using a device driver called `/dev/net/tun`... **However, not all Linux systems support `/dev/net/tun`.** For example, some container-based app platforms like Heroku and Google Cloud Run do not. For those environments, **userspace networking mode** offers a different way of running, where `tailscaled` functions as a **SOCKS5 or HTTP proxy** which other processes in the container can connect through.»
- Comando canónico:
  ```
  tailscaled --tun=userspace-networking --socks5-server=localhost:1055 --outbound-http-proxy-listen=localhost:1055 &
  tailscale up --auth-key=<your-auth-key>
  ```
- «**Userspace networking mode is primarily for serverless environments. We recommend using it with ephemeral nodes and auth keys.**»
- «The Tailscale Docker image supports a `TS_USERSPACE` parameter that is equivalent to `tailscaled --tun=userspace-networking`.»
- SOCKS5 desde v1.8; HTTP proxy desde v1.16.
- Consumo desde la app: `ALL_PROXY=socks5://localhost:1055/ HTTP_PROXY=http://localhost:1055/ http_proxy=http://localhost:1055/ ./my-app`.
- Auth keys: `tailscale up --auth-key=<key>`; existen **auth keys efímeras** (se limpian al apagar el nodo) y se recomiendan para nodos efímeros; también existen tags y `--advertise-tags` para ACL.

**[V] Lado Runpod (oficial), sobre el «template propio con tailscaled en el mismo contenedor»:**
- docs/pods/overview §Limitations: «**Docker Compose is not supported:** Runpod runs Docker for you, so you cannot spin up your own Docker instance or use Docker Compose on Pods.»
- docs/pods/manage-pods §Troubleshooting: «**Docker Compose not working** | Not supported. Use a **custom template with your dependencies baked in**.»
- docs/pods/templates/overview: un template contiene «Container image, Hardware specifications, **Network settings** (Exposed HTTP and TCP ports), **Environment variables**, **Startup commands**».
- → **[I] Confirmado: la forma correcta es un template propio (Custom) con `tailscaled` instalado en la imagen y arranca en el *startup command*.** No hay `docker-compose`, no hay sidecar, no hay `systemd`.

**[V] Fuentes comunitarias (NO oficiales, nivel 1-2 — a verificar antes de confiar):**
- `github.com/koshimazaki/tailscale-runpod`: «Must use `--tun=userspace-networking` (no kernel TUN in containers)»; «Must persist state to `/workspace/` to survive restarts»; «**Browser auth required — authkey doesn't work reliably in unprivileged containers**» ← **contradice la recomendación oficial de Tailscale** (que sí recomienda auth keys con nodos efímeros); «Works on RunPod, Vast.ai, Lambda Labs, Paperspace».
- `huggingface.co/RyderJ/lessemf-pod` (`tailscale_setup.sh`): detecta `/dev/net/tun`; si no existe usa `--tun=userspace-networking --socks5-server=localhost:1055`; `tailscale up --reset --authkey="$TAILSCALE_AUTH_KEY" --hostname=... --ssh`; recomienda **auth key con tag** (`tag:runpod`) para ACL.
- `gist.github.com/snghrsw/...` (start command de Runpod con Tailscale + ComfyUI + Syncthing): `tailscaled --tun=userspace-networking &` + `tailscale up --ssh --hostname=comfy-runpod --authkey=... --accept-routes`.

**[I] El problema de fondo que ninguna de las dos partes resuelve explícitamente:** en **userspace mode**, `tailscaled` **no crea una interfaz de red real**. El tráfico *saliente* del pod puede ir por SOCKS5/HTTP proxy (`ALL_PROXY`). El **tráfico entrante desde el estudio al pod** (que es lo que un operador quiere para abrir el ComfyUI o scar datos) **no es un flujo documentado por Tailscale en modo userspace**: Tailscale documenta `tailscale serve` / `funnel` para publicar un servicio del nodo al tailnet, pero eso lo hace **público dentro del tailnet**, no privado-al-estudio, y requiere que el nodo esté correctamente registrado. **[P]** Hay que probarlo antes de depender de él.

**[I] Qué recomienda cada lado, resumido:**

| | Runpod (oficial) | Tailscale (oficial) | Conclusión operativa |
|---|---|---|---|
| Red privada | **Global networking**: pod↔pod, IP privada, `.runpod.internal`, 100 Mbps, 17 DCs (incluye los 5 UE) | Tailnet: nodo↔nodo, WireGuard, `tailscale serve`/`funnel` | **Usar Global networking** para el aislamiento interno. No inventar. |
| VPN estudio↔pod | **No documentado** (no hay VPN, no hay WireGuard, no hay Tailscale) | userspace networking para contenedores sin `/dev/net/tun`, con SOCKS5/HTTP proxy + auth keys | **Tailscale = no soportado por Runpod.** Es un añadido no auditado. |
| Acceso remoto seguro | **SSH proxied** por `ssh.runpod.io` (sin puerto público) | `tailscale ssh` | **Usar el SSH proxied** como vía oficial de entrada. |
| Estado de la recomendación | **«Never expose ports on Pods running sensitive services»** | **«We recommend using it with ephemeral nodes and auth keys»** | Coinciden en spirit: pod efímero, cero puertos, entrada única y autenticada. |

---

## 5. Precio

### 5.1 Granularidad, almacenamiento y red

**[V]** docs/pods/pricing:
- «Pods are billed by the **second** for compute and storage, with **no fees for data ingress or egress**.»
- Storage: «Storage is billed **per-second** for container and volume disks, and **hourly** for network volumes. **You are not charged if the host machine is unavailable.**»
- Savings plans: **deprecados** («can no longer be purchased»).
- On-demand: «You must have at least **one hour's worth of credits** for your selected configuration to deploy an on-demand instance.»
- Límites de cuenta: **spend limit default $80/hora**; auto-stop a saldo $0.
- «Runpod is not designed for long-term cloud storage.»

**[V]** Red/salida: **$0**. No hay cargo de ingress ni egress en Pods (docs/pods/pricing y docs/pods/overview: «Pods are billed by the second with no fees for ingress/egress»). **[I]** Esto es una ventaja real frente a proveedores que cobran por byte (ver Vast.ai, §6).

### 5.2 Precios vigentes (USD/hora, on-demand) — runpod.io/pricing, actualizado **2026-10-08**

| VRAM | GPU | Community Cloud | Secure Cloud | Secure vs Community |
|---|---|---|---|---|
| **24 GB** | RTX A5000 | $0,16 | $0,27 | ×1,7 |
| | **RTX 3090** | **$0,22** | **$0,50** | ×2,3 |
| | **L4** | **$0,44** | **$0,59** | ×1,3 |
| | **RTX 4090** | **$0,34** | **$0,89** | ×2,6 |
| | RTX Pro 6000 MIG 24 GB | $0,50 | $0,69 | ×1,4 |
| **48 GB** | RTX A6000 | $0,33 | $0,59 | ×1,8 |
| | **A40** | **$0,35** | **$0,59** | ×1,7 |
| | L40 | $0,69 | $0,82 | ×1,2 |
| | RTX 6000 Ada | $0,74 | $0,99 | ×1,3 |
| | L40S | $0,79 | $1,09 | ×1,4 |
| | RTX Pro 6000 MIG 48 GB | $1,00 | $1,29 | ×1,3 |
| **80 / 96 GB** | A100 PCIe (80) | $1,19 | $1,79 | ×1,5 |
| | A100 SXM (80) | $1,39 | $1,79 | ×1,3 |
| | RTX Pro 6000 (96) | $1,69 | $2,49 | ×1,5 |
| | H100 PCIe (80) | $1,99 | $2,89 | ×1,5 |
| | H100 NVL (94) | $2,59 | $3,19 | ×1,2 |
| | H100 SXM (80) | $2,69 | $3,99 | ×1,5 |

**[V]** Storage (runpod.io/pricing, mismo documento): Container Disk $0,10/GB/mes · Volume Disk running $0,10 / **stopped $0,20**/GB/mes · Network Storage Standard **$0,07/GB/mes (<1 TB) / $0,05 (>1 TB)** · Network Storage High-Performance $0,14/GB/mes.

**[V]** Serverless (mismo doc, para comparación): 3090/L4/A5000/MIG24GB $0,69/h · 4090 $1,10/h · A6000/A40 $1,22/h · L40S/6000Ada/MIG48 $1,75/h.

**[I]** El vault (`wiki/glosario/software/comfy-cloud-vs-runpod.md`, `wiki/glosario/software/flux2-klein-9b.md`) hoy registra **sólo precios Community** (3090 $0,22/h · 4090 $0,34/h · A40 $0,35/h). Esos valores **siguen vigentes** (página fechada 2026-10-08, verificada 2026-10-28), así que no hay corrección de número: **falta agregar la columna Secure Cloud**, que es la que corresponde usar bajo el mandato de PI. La diferencia 3090: $0,22 → $0,50/h; 4090: $0,34 → $0,89/h.

**[I]** Orden de magnitud para el estudio: un lote de 20-40 renders finales con FLUX.2 klein 9B en 3090 → 2-4 h → **$1,00-2,00 en Community / $2,50-5,00 en Secure**. Un LoRA de 4B: ~$0,50 / ~$1,15. Sigue siendo «$1-5 por evento», no un gasto de infraestructura.

### 5.3 Lo que el precio NO cubre (lo que hay que auditar antes de habilitar)

**[V]** Los costos que aparecen si el pod queda parado: volume disk $0,20/GB/mes, network volume $0,07/GB/mes, y la regla 3-2-1 de backups. **[I]** Un pod olvidado con 100 GB de volume disk parado = $20/mes; con un network volume de 200 GB = $14/mes. El «costo del olvido» supera el costo del trabajo.

---

## 6. Alternativas (sólo fuente oficial)

### 6.1 Cuadro comparativo

| Proveedor | Residencia | ¿Efímero? | Granularidad | GPU 24 GB | GPU 48 GB | GPU 80 GB | Egress | Privacidad |
|---|---|---|---|---|---|---|---|---|
| **Runpod Secure** | UE/EEUU/… (28 DC) | sí (container disk) | **por segundo** | 3090 $0,50 · 4090 $0,89 · L4 $0,59 | A40 $0,59 · L40S $1,09 | A100 PCIe $1,79 · H100 PCIe $2,89 | **$0** | ISO 27001 (ISMS), SOC 2 II, SOC 3, programas GDPR/HIPAA; single-tenant T3/T4; **sin SLA público** |
| **Runpod Community** | idem | sí | por segundo | 3090 $0,22 · 4090 $0,34 | A40 $0,35 | A100 PCIe $1,19 | $0 | **peer-to-peer**; Runpod «sólo el venue»; sin uptime warranty; **Runpod ya no acepta hosts nuevos** |
| **Scaleway (FR)** | **sólo Europa** (PAR1/PAR2, WAW2) | sí (power off / terminate) | **por minuto** (GPU) | **L4 €0,75** | **L40S €1,40** | H100 PCIe €2,73 | **sin cargo** | «stores all its data in Europe... not subject to any extraterritorial legislation, fully compliant with the principles of the GDPR»; **SLO 99,5%** para GPU |
| **OVHcloud (FR)** | Francia (Gravelines, Paris) | sí (AI Notebooks: storage local efímero; auto-stop 7 días) | **por minuto** | **L4 €0,75** · A10 €0,76 | **L40S €1,40** | A100 €2,75 · H100 €2,80 | traffic in/out opcional | Proveedor francés, DCs europeos; **AI Notebooks** con workspace en Object Storage y 10 GB gratis 30 días |
| **Nebius (NL/UE)** | UE (Finlandia, Francia, Islandia) + US + UK | sí | por hora (+ spot) | — | **L40S $1,55** | H100 $4,50 | **$0** | Trust Center propio; SOLID/EU; K8s + Soperator free; spot desde $0,79/h |
| **Vast.ai** | hosts UE **sí**, **sin garantía contractual de residencia** | sí | **por segundo** | depende del host | depende del host | depende del host | **por byte** (in y out, tarifa del host) | **marketplace peer-to-peer** → mismo modelo de riesgo que Community Cloud |
| **Hetzner (DE)** | Alemania (FSN1/NBG1) + Helsinki | **no** (dedicado) | por mes | RTX 4000 SFF Ada 20 GB **€232,30/mes** + €114 setup | — | GEX131 (2× RTX 4000) a consultar | tráfico **ilimitado** | **Máximo control**: root, SO propio, datos en Europa, GDPR Art. 28, sin terceros en el camino de datos |

### 6.2 Lectura para el mandato de PI

**[V] Scaleway** (scaleway.com/en/gpu-instances/ y /en/ai-solutions/): «**guaranteed data residency within Europe**»; zonas «Paris: PAR1 PAR2 · Warsaw: WAW2»; «Scaleway stores all its data in Europe and thus, it is not subject to any extraterritorial legislation, and fully compliant with the principles of the GDPR»; «simple, pay-as-you-go billing with **no egress or lock-in**»; precios L4 €0,75/h, L40S €1,40/h, H100 PCIe €2,73/h. Billing (docs/instances/faq): «**GPU Instances: Billed per minute of uptime**... other resources—such as public IP addresses and storage volumes—are billed for their entire allocation period, **regardless of whether the Instance is powered off**». SLO 99,5% para GPU Instances.

**[V] OVHcloud** (ovhcloud.com/fr/public-cloud/prices/ + docs.ovhcloud.com): L4 €0,75/h, A10 24 GB €0,76/h, L40S €1,40/h, A100 80 GB €2,75/h, H100 €2,80/h; «Notre datacenter "France (Gravelines)" offre la plus grande variété de GPU». AI Notebooks: «tarification simple et flexible... à la minute»; «**Stockage local éphémère** du notebook... cet espace de stockage n'est pas conservé lorsque vous arrêtez ou supprimez votre notebook»; «Les 10 premiers Go sont gratuits pendant 30 jours consécutifs une fois votre notebook arrêté».

**[V] Nebius** (nebius.com/prices): H100 $4,50/h on-demand (spot desde $0,79), H200 $5,40, B200 $8,50, RTX PRO 6000 $1,80, L40S desde $1,55; «**Networking: Egress/Ingress traffic — Free**»; Shared Filesystem $0,08/GiB/mes; Block volumes $0,053-0,118/GiB/mes; Object storage $0,0147/GiB/mes; K8s y Soperator **Free**.

**[V] Vast.ai** (docs.vast.ai/guides/pricing): «Vast.ai is a **marketplace, not a fixed-price provider**. Hosts set their own rates»; «GPU compute, **per-second**»; «**Storage, continuous while the instance exists, including when it is stopped**. Delete the instance to stop storage billing»; «**Bandwidth, per byte for both ingress and egress**. Rates are host-set»; modelos On-demand / Reserved / Interruptible / Serverless (`min_workers: 0`).

**[V] Hetzner** (docs.hetzner.com/robot/dedicated-server/server-lines/gpu-server/ + price-adjustment 15-jun-2026 + hetzner.com/de/dedicated-rootserver/gex44): GEX44 = RTX 4000 SFF Ada **20 GB GDDR6 ECC**, i5-13500, 64 GB DDR4, 2× 1,92 TB NVMe, FSN1 (Falkenstein); **€232,30/mes excl. IPv4 + €114 setup** (post-ajuste 15-06-2026) ≈ €0,29/h equivalente; GEX131 (RTX PRO 6000, para training) en NBG1/Nuremberg y Helsinki desde €1.197,30/mes; tráfico ilimitado; Data Processing Agreement GDPR Art. 28.

**[I] Para el mandato de PI, el orden de preferencia sería:**
1. **Runpod Secure Cloud en EU-NL-1 o EU-FR-1** — sólo si el material es no sensible. Es el más barato por segundo y el más rápido de operar. Suena contradictorio con PI, pero el dato decisive es qué subís.
2. **Scaleway GPU Instances en PAR2** — si lo que se busca es **residencia garantizada en Europa +GDPR nativo sin extraterritorialidad**, a cambio de granularidad por minuto y SLO 99,5%. Para la PI de cliente que sí sea PI (datos personales), Scaleway es el que tiene el argumento de soberanía más limpio. L4 €0,75/h ≈ $0,82, comparable al L4 de Runpod Secure ($0,59).
3. **OVHcloud AI Notebooks (Gravelines)** — la opción más cerca del «notebook efímero con almacenamiento local descartable» que da el mandato, con granularidad por minuto. Es la opción con el perfil de datos más limpio para material no reutilizable.
4. **Hetzner GEX44 dedicado** — el único con **control total y sin terceros**, y el único con **tráfico ilimitado**. Contra: 20 GB VRAM (no alcanza para FLUX.2 9B fp8 + LoRA), no es efímero, costo mensual fijo (€232) que sólo se justificaría con uso sostenido.
5. **Nebius** — para quien necesite GPU de 48-96 GB con Free egress y compliance fuerte; carísimo por hora on-demand para nuestro volumen.
6. **Vast.ai** — **descartado para PI**: es el mismo modelo peer-to-peer que Community Cloud, con almacenamiento que se cobra parado y **egress por byte**. Es una alternativa de precio, no de privacidad.

---

## 7. Conclusión accionable

### 7.1 Qué se puede mandar a Runpod y qué no

**Veredicto de una línea:** Runpod es aceptable **únicamente** como capacidad de cómputo efímera para material derivado y no sensible, con Secure Cloud + volumen cifrado + cero puertos + borrado manual; es **inaceptable** para cualquier cosa que sea PI de cliente o instrumento legal.

**[I] Regla de decisión (la más simple y la que más protege):** si el material no puede salir del estudio por política propia, no lo mandes por proveedor. El proveedor no mejora la política. La pregunta útil no es «¿Runpod entrena con mis datos?» sino «¿este material puede estar en un disco ajeno a mi control, en un datacenter que no controlo, sin SLA y con una entidad jurídica de cobertura que el DPA todavía no firmé?».

### 7.2 Tabla puede / no puede / condicional

| # | Clase de material | Veredicto | Condiciones / fundamento |
|---|---|---|---|
| **1** | **Planos legales DWG/PDF firmados** (instrumento contractual y registral — Ley 24.335) | **NO PUEDE** | **(a)** Ya están en el estudio y en el vault local, que es el control. **(b)** ToS §2: el cliente es responsable de «protecting all data... both at rest and in transit... including security configuration of the Service provided by Runpod». **(c)** Sin SLA de confidencialidad para Pods on-demand. **(d)** La regla del propio estudio: planos legales nunca en cloud. **[I]** No hay aquí una duda técnica: hay una regla de estudio, y la regla manda. |
| **2** | **Cálculos y presupuestos** | **CONDICIONAL** — sólo agregados anonimizados | **Puede**: un pliego estandarizado, un PLN, la memoria de cálculo y un presupuesto **de concurso**, sin costos reales ni datos de cliente, si el cliente lo autoriza por escrito. **No puede**: estructura de costos del estudio, margenes, precios de honorarios, o cualquier cifra que identifique al cliente. **[I]** El vector de fuga aquí no es el discriminador legal sino el **uso no autorizado**: un presupuesto en un pod es un documento que sale del control de versiones del estudio. Subir un PDF ya producido de render, no la fuente editable. |
| **3** | **Material de cliente confidential** (documentación del cliente, recias, surveys, fotos de obra, BIM, correos) | **NO PUEDE** | **(a)** No hay autorización del titular hacia un sub-procesador. **(b)** El «cliente» contractual es Runpod; el controlador real de ese dato es *tu* cliente, que no consintió. **(c)** Community Cloud: el host es un tercero independiente. **(d)** El mandato «PI 100% protegida» lo veta por definición. **[I]** Excepción conceivable: Secure Cloud + volumen cifrado + acceso por SSH proxied + destrucción documentada, **sólo** con autorización expresa y escrita del cliente en el contrato, y sólo para material que el cliente ya clasifique como de riesgo bajo. |
| **4** | **Material de concurso con PI de terceros** (material fuente del AI×Gaudí, de la Fundació, de otro equipo) | **NO PUEDE** | **(a)** PI de un tercero, no del estudio: no hay derecho a subirlo. **(b)** El material del curso tiene licencia no-comercial (ver `wiki/glosario/software/lora-rhino-to-image-gaudi.md` y `flux2-klein-9b.md` — a re-verificar). **(c)** Derivado: un render de material de terceros sigue siendo material de terceros. **[I]** Distinguir: el material **fuente** no va; los **resultados** (categoría 5) pueden, si el modelo y la licencia lo permiten. |
| **5** | **Renders e imágenes IA derivados de material propio** | **CONDICIONAL** — sí, con 5 condiciones | **(1)** La entrada al pod es material **derivado/anonimizado** (capturas de render de Rhino, PNG, no el DWG). **(2)** Secure Cloud + volume disk con **«Encrypt volume»** ON + **sin** network volume. **(3)** **Cero** «Expose HTTP Ports» y **cero** «Expose TCP Ports»; acceso sólo por SSH proxied `ssh.runpod.io`. **(4)** El modelo tiene licencia compatible con el uso comercial (verificar FLUX.1 [dev] = Non-Commercial vs. los Apache-2.0 del vault — **no resuelto en esta auditoría**). **(5)** Uso del **pod**, no de Public Endpoints ni de Comfy Cloud (que sí tienen retención propia). **[V]** Fundamento de la condición (5): Public Endpoints y Comfy Cloud son servicios con retención yelemetry de plataforma; el pod es cómputo efímero. |
| **6** | **Modelos y LoRA de entrenamiento** | **CONDICIONAL** | **Puede**: el **LoRA resultante** (pesos) — se entrena con un modelo base público y sale del pod; los pesos no son PI de terceros. **No puede**: el **dataset de entrenamiento** si es material de cliente o de tercero. **Condiciones**: (i) dataset = material propio autorizado o público con licencia de entrenamiento; (ii) Secure Cloud + volumen cifrado + sin puertos; (iii) el LoRA del curso AI×Gaudí («el modelo de IA exclusivo» del curso) tiene **licencia no-comercial** → **no** sirve para entrega de cliente: hay que resolver la licencia antes de entrenar. **[P]** Verificar la licencia del LoRA del curso y la de FLUX.2 [klein] antes de cualquier corrida que termine en entrega. |

### 7.3 Qué auditar ANTES de habilitarlo

| # | Ítem | Cómo | Por qué bloquea |
|---|---|---|---|
| 1 | **Firmar el DPA** | Completar el bloque de firma y enviarlo por el link de PandaDoc del DPA §1 | Sin DPA firmado, la Privacy Policy es la que aplica y Runpod es **controlador** (con fines propios). Con DPA firmado, Runpod es **processor** y está atado a tus instrucciones. **Es el requisito #1.** |
| 2 | **Confirmación escrita de no-entrenamiento** | Mail a legal@runpod.io / help@runpod.io: ¿se usa el contenido de Pods/Volumes/Container disks para entrenar o mejorar modelos? ¿queda excluido del alcance de Performance Data? | Es lo único que convierte la interpretación (§1.c) en hecho auditable. No hay cláusula; hay que producirla. |
| 3 | **Confirmar el alcance de los logs** | Preguntar si el stdout del pod va a BetterStack/Datadog y cuál es la ventana de retención | Si sí, hay un segundo destino fuera del DPA con retención no acotada. |
| 4 | **Leer el Trust Center** | trust.runpod.io — SOC 2 Type II, ISO 27001, SOC 3 Bridge Letter 2026, lista de sub-procesores | Es la evidencia que un auditor de cliente va a pedir. Si no lo podés adjuntar, no habilités. |
| 5 | **Verificar el DC real después del deploy** | Consola → detalle del pod → campo de data center; y `runpodctl datacenter list` | La región pedida es un filtro de disponibilidad, no una garantía (DPA §4). |
| 6 | **Revisar la cadena de sub-procesores** | DPA §8 Attachment 2: AWS, Google Workspace, Google Cloud, HubSpot, Stripe, BetterStack, Cloudflare, PlanetScale, Docker, Datadog, Clerk, Tinybird, DigitalOcean, Snowflake | Cada uno es un punto de contacto potencial del material. En particular **Cloudflare** (cache del proxy HTTP) y **DigitalOcean**. |
| 7 | **Firmar la política interna de PI del estudio** (mini-política de privacidad, pendiente según `wiki/glosario/entidades/runpod.md`) | Documento propio | El mandato «PI 100% protegida» no está escrito en ningún contrato del estudio; está en la cabeza. |
| 8 | **Verificar licencias de modelos** | FLUX.1 [dev] (Non-Commercial) vs. FLUX.2 klein (Apache 2.0, según vault) | Un render con licencia incompatible NO se puede entregar. |

### 7.4 Perfil de pod mínimo (para que la operación sea repetible y reversible)

Este es el bloque que hay que dejar escrito en `proyectos/MVP_04-comfyui-arquitectura/` (o `raw/`) y que puede ejecutarse tal cual. **Es reversible**: todo lo que se sube se borra, y nada depende de estado que sobreviva al pod.

```
PERFIL DE POD — RUNPOD "PI-LIMPIO" v1        (vigente 2026-10-28)

IDENTIDAD Y CONTRATO
  cuenta_runpod      : <cuenta del estudio, no personal>
  dpa                : FIRMADO (obligatorio antes del primer pod)
  confirmacion_email : adjunta en el legajo (no-entrenamiento + logs)

CLOUDS
  cloud_type         : SECURE            # nunca COMMUNITY (peer-to-peer, sin hosts nuevos)
  data_center_ids    : [EU-NL-1, EU-FR-1]  (agregar EU-RO-1 / EU-SE-1 si hay stock)
  data_center_priority: custom          # no "availability" -> no es una decisión si no
  compliance_filter  : GDPR              # Deploy Pod > Additional filters > Security & compliance
  global_networking  : ON solo si hay 2+ pods del mismo job

STORAGE
  container_disk     : 20 GB             # efímero: TODO lo temporal vive acá
  volume_disk        : 100 GB
  encrypt_volume     : ON                # única unidad con cifrado por volumen
  network_volume     : NO                # sin cifrado + se cobra parado + ata el DC
  global_volume      : NO                # beta, sin cifrado

RED
  expose_http_ports  : (vacío)           # nada público; ni Jupyter
  expose_tcp_ports   : (vacío)           # nada público; ni SSH por IP
  jupyter_password   : <secret>         # sólo si se abre 8888 en una sesión puntual
  acceso             : ssh <pod>-<puerto>@ssh.runpod.io -i <key>   # SSH proxied
  tailscale          : OFF por defecto   # si se activa: template propio + auth key
                                        #   efímera + tag + estado en /workspace

IMAGEN / ARRANQUE
  template           : propio (Custom)   # NO docker-compose: no existe en Runpod
  startup            : tailscaled --tun=userspace-networking \
                        --socks5-server=localhost:1055 &   # sólo si tailscale=ON
                        tailscale up --auth-key=$TAILSCALE_AUTH_KEY --hostname=...
  secrets            : Runpod Secrets / env vars   # nunca en la imagen ni en el repo

DATOS QUE ENTRAN  (lista blanca; todo lo demás, no)
  [OK] capturas PNG/JPG de render de Rhino (derivados)
  [OK] workflows ComfyUI (.json) sin rutas ni notas del estudio
  [OK] modelos base públicos y LoRAs con licencia compatible
  [NO] DWG / DXF / RVT / IFC / PDF firmados
  [NO] material de cliente (sin autorización escrita)
  [NO] cálculos, presupuestos, correspondencia
  [NO] material de concurso de terceros

CIERRE (siempre, en este orden)
  1. descargar resultados  ->  vault local / activo local
  2. verificarlos (hash + autoría + licencia) ANTES de borrar
  3. TERMINATE del pod        (no stop: stop deja el volume disk y lo cobra)
  4. borrar el volume disk   (implicado por terminate)
  5. verificar /user/storage : NO debe quedar ningún volume
  6. registrar en el legajo: pod_id, data_center real, horas, USD, qué entró y qué salió
  7. confirmar saldo y spend limit (alert de saldo bajo activa)

COSTO
  minimo_creditos     : 1 h de GPU
  spend_limit         : 5 USD/h      # default de Runpod = 80 USD/h: bajarlo
  alerta_saldo_bajo   : ON
  presupuesto_mensual : 10 USD       # si se supera, se abre revisión de PI
```

**[I] Por qué este perfil es reversible:** (a) el único estado persistente es el volume disk, y se borra con `terminate`; (b) no hay red pública; (c) no hay dependencia de Runpod más allá del cómputo; (d) la lista blanca de datos que entran está escrita y es audit-able; (e) el legajo por corrida permite reconstruir qué pasó.

### 7.5 Las 3 decisiones que quedan abiertas

1. **¿Se firma el DPA y se pide la confirmación escrita de no-entrenamiento antes del primer pod, o Runpod queda como proveedor no contractualizado?** Sin DPA firmado, todo este informe es irrelevante desde el punto de vista legal. **Decisión de Emilia/Sol, no técnica.**
2. **¿El material del concurso (categoría 4) y el LoRA del curso (categoría 6) tienen licencia compatible con entrega a cliente?** Si la respuesta es no, la ruta de render en cloud del concurso queda cerrada y hay que volver al local (8 GB) o al شراكة de un tercero. **Requiere leer la licencia del LoRA del curso AI×Gaudí y la de FLUX.2 [klein].**
3. **¿Se acepta que el material de cliente confidential siga siendo 100% local (o Nextcloud del estudio), o se abre la excepción Secure Cloud con autorización escrita del cliente?** Hoy la tabla dice no puede; la decisión es si esa línea se mueve o no. **Decisión de política de estudio.**

---

## Fuentes

Verificadas con `webfetch` (HTTP 200), salvo indicación:

1. Runpod, Inc. (2025, 7 de agosto). *Privacy Policy*. https://www.runpod.io/legal/privacy-policy — `idioma_original: en` [trad. propia — no oficial] — **200**. *Effective as of August 7th, 2025.*
2. Runpod, Inc. (2026, 24 de marzo). *Terms of Service*. https://www.runpod.io/legal/terms-of-service — `idioma_original: en` [trad. propia — no oficial] — **200**. *Last Updated: March 24, 2026.*
3. Runpod, Inc. *Data Processing Agreement*. https://www.runpod.io/legal/data-processing-agreement — `idioma_original: en` [trad. propia — no oficial] — **200**. *(7 attachments: TOMs, Sub-Processors, SCC, UK Addendum, Switzerland Addendum, State Privacy Laws, Brazil Addendum.)*
4. Runpod, Inc. (2026, 13 de septiembre). *Compliance*. https://www.runpod.io/legal/compliance — `idioma_original: en` [trad. propia — no oficial] — **200**.
5. Runpod, Inc. (2026, 8 de octubre). *GPU Cloud Pricing*. https://www.runpod.io/pricing — `idioma_original: en` [trad. propia — no oficial] — **200**. *Updated October 8, 2026.*
6. The Runpod Team. (2026, 19 de octubre). *Keeping Data Secure: Best Practices for Handling Sensitive Data with Cloud GPUs*. https://www.runpod.io/articles/guides/keep-data-secure-cloud-gpus — `idioma_original: en` [trad. propia — no oficial] — **200**.
7. Runpod. (s.f.). *Hosting and Running Private AI Agents*. https://www.runpod.io/articles/guides/hosting-and-running-private-ai-agents — `idioma_original: en` [trad. propia — no oficial] — **citada** (texto íntegro en el índice de búsqueda; no fetcheada).
8. Runpod. (s.f.). *Data security and legal compliance*. https://docs.runpod.io/references/security-and-compliance — `idioma_original: en` [trad. propia — no oficial] — **200**.
9. Runpod. (s.f.). *Pricing (Pods)*. https://docs.runpod.io/pods/pricing — `idioma_original: en` [trad. propia — no oficial] — **200**.
10. Runpod. (s.f.). *Storage options*. https://docs.runpod.io/pods/storage/types — `idioma_original: en` [trad. propia — no oficial] — **200**.
11. Runpod. (s.f.). *Network volumes*. https://docs.runpod.io/storage/network-volumes — `idioma_original: en` [trad. propia — no oficial] — **200**.
12. Runpod. (s.f.). *Global networking*. https://docs.runpod.io/pods/networking — `idioma_original: en` [trad. propia — no oficial] — **200**.
13. Runpod. (s.f.). *Expose ports*. https://docs.runpod.io/pods/configuration/expose-ports — `idioma_original: en` [trad. propia — no oficial] — **200**.
14. Runpod. (s.f.). *Manage Pods*. https://docs.runpod.io/pods/manage-pods — `idioma_original: en` [trad. propia — no oficial] — **200**.
15. Runpod. (s.f.). *Maintenance, outages, and data safety*. https://docs.runpod.io/pods/maintenance-and-outages — `idioma_original: en` [trad. propia — no oficial] — **200**.
16. Runpod. (s.f.). *Overview (Pods)*. https://docs.runpod.io/pods/overview — `idioma_original: en` [trad. propia — no oficial] — **200**.
17. Runpod. (s.f.). *Choose a Pod*. https://docs.runpod.io/pods/choose-a-pod — `idioma_original: en` [trad. propia — no oficial] — **200**.
18. Runpod. (s.f.). *Overview (Pod templates)*. https://docs.runpod.io/pods/templates/overview — `idioma_original: en` [trad. propia — no oficial] — **200**.
19. Runpod. (s.f.). *Connect to a Pod with SSH*. https://docs.runpod.io/pods/configuration/use-ssh — `idioma_original: en` [trad. propia — no oficial] — **200**.
20. Runpod. (s.f.). *Connection options*. https://docs.runpod.io/pods/connect-to-a-pod — `idioma_original: en` [trad. propia — no oficial] — **200**.
21. Runpod. (s.f.). *Zero GPU Pods on restart*. https://docs.runpod.io/pods/troubleshooting/zero-gpus — `idioma_original: en` [trad. propia — no oficial] — **200**.
22. Runpod. (s.f.). *List data centers (API v2)*. https://docs.runpod.io/api-reference-v2/catalog/list-data-centers — `idioma_original: en` [trad. propia — no oficial] — **200**.
23. Runpod. (s.f.). *runpodctl datacenter*. https://docs.runpod.io/runpodctl/reference/runpodctl-datacenter — `idioma_original: en` [trad. propia — no oficial] — **200**.
24. Runpod. (s.f.). *Documentation index (llms.txt)*. https://docs.runpod.io/llms.txt — **200**. *(Usado como índice maestro y como prueba negativa: no contiene ninguna entrada sobre Tailscale.)*
25. Runpod. (2026, 20 de marzo). *How to Find HIPAA/GDPR-Compliant GPUs on Runpod and Understand BAA Policy*. Runpod Help Center. https://contact.runpod.io/hc/en-us/articles/50120688006163-How-to-Find-HIPAA-GDPR-Compliant-GPUs-on-Runpod-and-Understand-BAA-Policy — `idioma_original: en` [trad. propia — no oficial] — **200**.
26. Runpod. (s.f.). *Runpod Trust Center*. https://trust.runpod.io/ — `idioma_original: en` [trad. propia — no oficial] — **citada** (índice de búsqueda; el contenido requiere acceso aprobado).
27. Runpod. (s.f.). *Create a new Pod (API reference)*. https://docs.runpod.io/api-reference/pods/POST/pods — `idioma_original: en` [trad. propia — no oficial] — **citada** (enum de `dataCenterIds`, `dataCenterPriority`, `cloudType`; URL oficial, no fetcheada).
28. Tailscale Inc. (2025, 12 de noviembre). *Userspace networking mode (for containers)*. https://tailscale.com/docs/concepts/userspace-networking — `idioma_original: en` [trad. propia — no oficial] — **citada** (texto íntegro en el índice de búsqueda; no fetcheada).
29. Vast.ai. (s.f.). *Pricing overview*. https://docs.vast.ai/guides/pricing — `idioma_original: en` [trad. propia — no oficial] — **200**.
30. Scaleway SAS. (s.f.). *AI solutions*. https://www.scaleway.com/en/ai-solutions/ — `idioma_original: en` [trad. propia — no oficial] — **200**. *(Precios L4 €0,75/h · L40S €1,40/h · H100 PCIe €2,73/h; «Keep sensitive data in Europe».)*
31. Scaleway SAS. (s.f.). *GPU instances*. https://www.scaleway.com/en/gpu-instances/ — `idioma_original: en` [trad. propia — no oficial] — **citada** (zonas PAR1/PAR2/WAW2, «guaranteed data residency within Europe»).
32. Scaleway SAS. (s.f.). *Instances FAQ*. https://www.scaleway.com/en/docs/instances/faq/ — `idioma_original: en` [trad. propia — no oficial] — **200**. *«GPU Instances: Billed per minute of uptime».*
33. OVH SAS. (s.f.). *Tarif Cloud — comparatif Public Cloud*. https://www.ovhcloud.com/fr/public-cloud/prices/ — `idioma_original: fr` — **citada** (tabla oficial de precios GPU).
34. OVH SAS. (2026, 27 de enero). *AI Notebooks — Facturation et cycle de vie*. https://docs.ovhcloud.com/fr/guides/public-cloud/ai-machine-learning/ai-notebooks-billing.md — `idioma_original: fr` — **200**.
35. Nebius B.V. (s.f.). *AI Cloud pricing*. https://nebius.com/prices — `idioma_original: en` [trad. propia — no oficial] — **200**.
36. Hetzner Online GmbH. (s.f.). *GPU Server — Possible configurations and add-ons*. https://docs.hetzner.com/robot/dedicated-server/server-lines/gpu-server/ — `idioma_original: en` [trad. propia — no oficial] — **citada**.
37. Hetzner Online GmbH. (2026, 8 de julio). *Price Adjustment 15 June 2026*. https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/ — `idioma_original: en` [trad. propia — no oficial] — **citada**. *(GEX44-1: €232,30/mes excl. IPv4 + €114 setup.)*
38. Hetzner Online GmbH. (s.f.). *GEX44*. https://www.hetzner.com/de/dedicated-rootserver/gex44 — `idioma_original: de` — **citada**.

### Fuentes comunitarias (nivel 1-2; **no** son fuente oficial — se reportan como tales)

39. koshimazaki. (2026, 30 de enero). *tailscale-runpod*. GitHub. https://github.com/koshimazaki/tailscale-runpod — `idioma_original: en` — **citada**.
40. RyderJ. (s.f.). *tailscale_setup.sh*. Hugging Face. https://huggingface.co/RyderJ/lessemf-pod/blob/main/tailscale_setup.sh — `idioma_original: en` — **citada**.
41. snghrsw. (s.f.). *runpod start script* (Tailscale + ComfyUI + Syncthing). GitHub Gist. https://gist.github.com/snghrsw/5e671a4db380ca0a1e57178f72b475ea — `idioma_original: en` — **citada**.
42. Kretzschmar, A. (2024, 7 de febrero). *Contain your excitement: A deep dive into using Tailscale with Docker*. Tailscale Blog. https://tailscale.com/blog/docker-tailscale-guide — `idioma_original: en` — **citada**.

### URLs descartadas (reportadas por completitud)

- `https://docs.runpod.io/pods/overview/secure-cloud` — **404**. La página de Secure Cloud no existe en esa ruta; el contenido equivalente está en `/pods/overview#pod-types` y `/pods/choose-a-pod`.
- `https://api.runpod.io/v2/catalog/datacenters` — **401** (requiere `Authorization: Bearer`). El catálogo de DCs con `compliance` por datacenter es la vía autenticada para el filtro GDPR.
- `https://www.scaleway.com/en/gpu-instances/pricing/` — **404**.
- `https://docs.nebius.com/compute/regions/` — **404**.
- `https://www.scaleway.com/en/pricing/gpu/` — **no descargable** (>5 MB); se usó `/en/ai-solutions/` como fuente de precios oficial.

### Descartadas por no ser fuente oficial (comparadores comerciales)

`gpufinder.dev`, `gpuperhour.com`, `spheron.network/blog`, `serversearcher.com`, `nasdaq.com/press-release` (nota de prensa de Nebius). Sus cifras no se usaron; sólo se conservaron como pistas de búsqueda, y todos los precios citados en §6 provienen de páginas de precio del propio proveedor.

---

## Metodología

### Queries ejecutadas (websearch)

| Idioma | Query | Resultado útil |
|---|---|---|
| EN | `Runpod docs Secure Cloud privacy data centers SOC 2` | 8 (incl. docs/references/security-and-compliance, trust.runpod.io, legal/compliance, list-data-centers API) |
| EN | `Runpod Tailscale pod private network userspace proxy auth key` | 6 (tailscale.com/docs/concepts/userspace-networking; 3 fuentes comunitarias) |
| EN | `runpod data center locations list regions "EU-NL-1" "US-KS-2" secure cloud` | 8 (enum oficial de `dataCenterIds`; docs/pods/networking; blog de expansión) |
| EN | `Scaleway GPU instances elastic per second documentation lifecycle one hour site:docs.scaleway.com` | 5 (docs/instances/faq, docs/instances/..., docs/gpu/...) |
| EN | `OVHcloud GPU instances AI Notebooks pricing France official site:ovhcloud.com` | 5 (tarif public cloud; docs AI Notebooks billing) |
| ES/EN | `Hetzner dedicated GPU server GEX44 price official site:hetzner.com GPU` | 5 (página GEX44, price adjustment, docs GPU server) |
| EN | `Scaleway GPU elastic... / Nebius AI studio data residency Europe / Vast.ai EU hosts` | 9 (precios oficiales de Scaleway, Nebius, Vast.ai) |

### URLs fetchadas con estado

| # | URL | Estado | Aporte principal |
|---|---|---|---|
| 1 | https://www.runpod.io/legal/privacy-policy | **200** | Retención genérica, Security, notice europeo, sub-procesadores |
| 2 | https://www.runpod.io/legal/terms-of-service | **200** | Propiedad del contenido, licencia agregada, Community Cloud "venue", Delaware/NJ, arbitraje |
| 3 | https://www.runpod.io/legal/data-processing-agreement | **200** | DPA no firmado, TOMs, Performance Data fuera del DPA, "reasonable efforts", SCC/UK/BR/CH |
| 4 | https://www.runpod.io/legal/compliance | **200** | ISO 27001 RUN-ISMS-20260827, SOC 2 II, SOC 3, HIPAA/GDPR, cobertura varía por región |
| 5 | https://www.runpod.io/pricing | **200** | Tabla completa Community vs Secure, storage, serverless |
| 6 | https://www.runpod.io/articles/guides/keep-data-secure-cloud-gpus | **200** | AES-256/TLS, Secure single-tenant, "you control your data", preguntas frecuentes |
| 7 | https://docs.runpod.io/references/security-and-compliance | **200** | GDPR por región, multi-tenancy, host access policy |
| 8 | https://docs.runpod.io/pods/pricing | **200** | Por segundo, sin ingress/egress, tabla storage running/stopped, límites de cuenta |
| 9 | https://docs.runpod.io/pods/storage/types | **200** | 4 tipos, cifrado sólo en volume disk, redimensionado, terminate |
| 10 | https://docs.runpod.io/storage/network-volumes | **200** | Sólo Secure Cloud, atado a DC, $0/balance, no desenganchable |
| 11 | https://docs.runpod.io/pods/networking | **200** | Global networking, 17 DCs, 100 Mbps, `.runpod.internal` |
| 12 | https://docs.runpod.io/pods/configuration/expose-ports | **200** | Proxy HTTP + Direct TCP, timeout 100 s, IP pública, simétricos |
| 13 | https://docs.runpod.io/pods/manage-pods | **200** | Stop/start/restart/terminate, logs, "Docker Compose not supported" |
| 14 | https://docs.runpod.io/pods/maintenance-and-outages | **200** | Mantenimiento planificado, 3-2-1, "no guarantee of recovery" |
| 15 | https://docs.runpod.io/pods/overview | **200** | Secure vs Community, limitaciones (sin Compose/UDP/Windows), sin fees de egress |
| 16 | https://docs.runpod.io/pods/choose-a-pod | **200** | Tabla Secure/Community, **"no longer accepting new hosts"** |
| 17 | https://docs.runpod.io/pods/templates/overview | **200** | Componentes de un template (network settings, startup commands) |
| 18 | https://docs.runpod.io/pods/configuration/use-ssh | **200** | SSH proxied por `ssh.runpod.io` vs. SSH sobre IP pública |
| 19 | https://docs.runpod.io/pods/connect-to-a-pod | **200** | Web terminal / SSH / JupyterLab / VS Code, `JUPYTER_PASSWORD` |
| 20 | https://docs.runpod.io/pods/troubleshooting/zero-gpus | **200** | Pérdida de GPU al reiniciar, migración de pod |
| 21 | https://docs.runpod.io/api-reference-v2/catalog/list-data-centers | **200** | `compliance` por DC, enum de regiones, filtro GDPR |
| 22 | https://docs.runpod.io/runpodctl/reference/runpodctl-datacenter | **200** | `runpodctl datacenter list` autoritativo, `--data-center-ids` |
| 23 | https://docs.runpod.io/llms.txt | **200** | Índice completo de la doc → prueba negativa sobre Tailscale |
| 24 | https://contact.runpod.io/hc/en-us/articles/50120688006163-... | **200** | Filtro Security & compliance; umbral de $3.000/mes para BAA/DPA bespoke |
| 25 | https://docs.vast.ai/guides/pricing | **200** | Marketplace, per-second, storage cobrada parado, bandwidth por byte |
| 26 | https://www.scaleway.com/en/ai-solutions/ | **200** | Precios GPU + "Keep sensitive data in Europe" |
| 27 | https://www.scaleway.com/en/docs/instances/faq/ | **200** | GPU por minuto; storage e IP se cobran apagado |
| 28 | https://docs.ovhcloud.com/fr/guides/public-cloud/ai-machine-learning/ai-notebooks-billing.md | **200** | Storage local efímero, granularidad por minuto, auto-stop 7 días |
| 29 | https://nebius.com/prices | **200** | Precios on-demand/spot, egress free, storage |
| 30 | https://tailscale.com/kb/1080/docker | **200** (redirect → CLI reference) | La URL canónica de Docker no resolvió; se usó /docs/concepts/userspace-networking |
| 31 | https://docs.runpod.io/pods/overview/secure-cloud | **404** | Descartada |
| 32 | https://api.runpod.io/v2/catalog/datacenters | **401** | Requiere bearer token |
| 33 | https://www.scaleway.com/en/gpu-instances/pricing/ | **404** | Descartada |
| 34 | https://docs.nebius.com/compute/regions/ | **404** | Descartada |

### Gaps declarados

- **No se leyeron** los documentos del Trust Center (SOC 2 Type II completo, ISO 27001, informe de sub-procesores, Bridge Letter 2026): requieren acceso aprobado. Es el gap #1.
- **No se pudo listar** el inventario vivo de data centers ni su matriz `compliance` por DC: la API de catálogo exige token. El enum de 28 DCs viene de la API reference oficial; la matriz compliance-por-DC **no** pudo consultarse sin cuenta.
- **No hay** página oficial de Runpod sobre Tailscale (probado sobre llms.txt). El comportamiento de Tailscale-in-userspace dentro de un pod de Runpod **no está auditado** por el proveedor: la recomendación oficial de Runpod es Global networking + SSH proxied.
- **Retención numérica de logs**: no documentada en ningún lugar público (Privacy Policy, DPA, docs). Sólo la definición de *Performance Data* y su exclusión del DPA.
- **Licencias**: FLUX.1 [dev] (Non-Commercial) vs. FLUX.2 [klein] (Apache 2.0) y la licencia del LoRA del curso AI×Gaudí **no** se re-verificaron en esta auditoría (fuera de alcance): quedan pendientes de la decisión #2.
- **Sin verificación empírica**: no se desplegó ningún pod. Los comportamientos de red (proxy, TCP, SSH proxied, userspace de Tailscale) son los documentados, no observados.
- **Italiano**: no se buscó; la documentación de Runpod es íntegramente en inglés y no hay versión en italiano (gap declarado, sin impacto).

---

## Propuestas wiki (esqueleto — NO ejecutado)

> `@vaultworm-arq` / `@contenidos` procesan esto. `@sherlock` no escribe en `wiki/`.

**A. `wiki/glosario/entidades/runpod.md` — actualizar** (§PI nuevo)
- Nuevo §«Mandat PI» con: propiedad del contenido (ToS §5), ausencia de cláusula de no-entrenamiento, DPA sin firmar, Performance Data fuera del DPA, Community Cloud en retirada, «reasonable efforts» de región.
- §Actualizar: precios con columna Secure Cloud (2026-10-08).
- Referencias: las 5 legales + 4 de docs.

**B. `wiki/glosario/software/comfy-cloud-vs-runpod.md` — actualizar**
- Sección §Runpod: sumar Secure Cloud y el filtro de compliance; agregar tabla de 6 clases de material.
- Sección §Precios: agregar columna Secure Cloud; nota de que los valores Community no cambiaron.

**C. `wiki/glosario/conceptos/pi-protegida-cloud-gpu.md` — NUEVA**
- Definición del mandato «PI 100% protegida» como política de estudio (no de proveedor).
- Checklist de 8 ítems previa a la habilitación de cualquier proveedor de cómputo cloud.
- Perfil de pod mínimo (el bloque de arriba) + regla 3-2-1.
- Tabla de 6 clases de material (puede / no puede / condicional) — reutilizable para Comfy Cloud, Vast.ai, Scaleway.
- «Conceptos relacionados»: [[wiki/glosario/conceptos/vault-visual|vault-visual]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/entidades/runpod|runpod]] · [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] (≥2).

**D. `wiki/glosario/interno/pbooks/pbk-comfyui.md` — actualizar §RunPod**
- Reemplazar el bloque «RunPod: cuándo y cómo» por el perfil de pod + la regla de cierre (terminate, no stop).
- Referencia al perfil y a la tabla de material.

**E. `wiki/glosario/software/flux2-klein-9b.md` + `lora-rhino-to-image-gaudi.md` — actualizar §licencias**
- Dejar asentado que la licencia (Non-Commercial vs. Apache 2.0) es condición habilitante para la ruta cloud, y que no está resuelta.

**F. Destinos de investigación (no wiki)**
- `raw/contenidos/sherlock-runpod-auditoria-pi.md` — stub pendiente-formato (lo escribe `@contenidos`, no `@sherlock`).
- `proyectos/MVP_04-comfyui-arquitectura/` — archivo `perfil-pod-runpod.md` con el bloque del perfil (ejecutable).
- `specs/260910-plan-trimestral-unificado-studio-os-emilia.md` §10 — volcar las 3 decisiones abiertas.

### Dependencias vault (tocadas por este informe, sin escribir)

`[[wiki/glosario/entidades/runpod|runpod]]` · `[[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]]` · `[[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]` · `[[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]]` · `[[wiki/glosario/software/comfyui|comfyui]]` · `[[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]]` · `[[proyectos/MVP_04-comfyui-arquitectura/regles-workflows-comfy|reglas-workflows-comfy]]` · `[[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral §10]]` · `[[proyectos/STUDIO_OS-Emilia/reuniones/2026-08-28-reunion-diagnostico-2hs|reunión 2026-08-28 (D13 + I27 PI protegida)]]` · `[[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research FLUX.2 klein LoRA (2026-10-20)]]`
