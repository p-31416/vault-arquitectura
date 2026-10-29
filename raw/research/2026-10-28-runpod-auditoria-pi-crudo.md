---
fecha: 2026-10-28
slug: runpod-auditoria-pi
tipo: crudo-por-fuente
tema: Auditoría de Runpod (GPU cloud) — mandato "PI 100% protegida"
investigador: sherlock
informe: raw/research/2026-10-28-runpod-auditoria-pi.md
cache: raw/research-cache/2026-10-28-runpod-auditoria-pi.json
estado: crudo
---

# CRUDO — Auditoría Runpod / PI protegida (2026-10-28)

> Extractos textuales por fuente, tal como fueron leídos. Los textos en inglés son **literales** de la fuente; las notas en español son del investigador. Orden: legales → docs Runpod → Tailscale → alternativas → comunitarias.
> Convención: **[V]** hecho verificado · **[I]** interpretación · **[P]** pregunta abierta.

---

## BLOQUE 1 — LEGALES RUNPOD

### F01 · Privacy Policy — https://www.runpod.io/legal/privacy-policy — **200**
*Last updated on August 7th, 2025. Effective as of August 7th, 2025.*

**Alcance (literal):**
> "This Privacy Policy does not apply to information that we process on behalf of our business customers (such as businesses and other organizations) while providing the Runpod platform to them. Our use of information that we process on behalf of our business customers may be governed by our agreements with such customers."

**Retención (sección completa, literal):**
> "We generally retain personal information to fulfill the purposes for which we collected it, including for the purposes of satisfying any legal, accounting, or reporting requirements, to establish or defend legal claims, or for fraud prevention purposes. To determine the appropriate retention period for personal information, we may consider factors such as the amount, nature, and sensitivity of the personal information, the potential risk of harm from unauthorized use or disclosure of your personal information, the purposes for which we process your personal information and whether we can achieve those purposes through other means, and the applicable legal requirements.
>
> When we no longer require the personal information we have collected about you, we may either delete it, anonymize it, or isolate it from further processing."

**[I]** Sin plazo numérico. «no documentado».

**Security (sección completa, literal):**
> "We employ a number of technical, organizational and physical safeguards designed to protect the personal information we collect. However, security risk is inherent in all internet and information technologies and we cannot guarantee the security of your personal information."

**User-generated content data (categoría que alcanza el material del estudio):**
> "User-generated content data, such as photos, images, music, videos, comments, questions, messages, works of authorship, and other content or information that you generate, transmit, or otherwise make available on the Service, as well as associated metadata."

**To create aggregated, de-identified and/or anonymized data:**
> "We may create aggregated, de-identified and/or anonymized data from your personal information and other individuals' personal information. We make personal information into de-identified and/or anonymized data by removing information that makes the data identifiable to you. We may use this aggregated, de-identified and/or anonymized data and share it with third parties for our lawful business purposes, including to analyze and improve the Service and promote our business."

**Data Processing outside Europe (sección completa):**
> "We are a U.S.-based company and many of our service providers, advisers, partners or other recipients of data are also based in the U.S. This means that, if you use the Service, your personal information will necessarily be accessed and processed in the U.S. It may also be provided to recipients in other countries outside Europe.
>
> It is important to note that that the US is not the subject of an 'adequacy decision' under the GDPR – basically, this means that the U.S. legal regime is not considered by relevant European bodies to provide an adequate level of protection for personal information, which is equivalent to that provided by relevant European laws.
>
> Where we share your personal information with third parties who are based outside Europe, we try to ensure a similar degree of protection is afforded to your personal information."

**Notice to European users:**
- Controller: "Runpod is the controller in respect of the processing of your personal information covered by this Privacy Policy for purposes of European data protection legislation (i.e., the EU GDPR and the so-called 'UK GDPR')."
- Representante: "Prighter Group with its local partners ... European Union (EU), United Kingdom (UK)".
- DPO: `privacy@runpod.io`.
- Bases legales: Contractual Necessity / Legitimate Interests / Compliance with Law / Consent (tabla de 12 propósitos).
- Derecho a reclamar ante la autoridad: EDPB (UE) / ICO (UK).
- **[V]** No hay sección que diga «no entrenamos modelos».

**Búsqueda literal `train|machine learning|artificial intelligence`:**
- Privacy Policy: sólo 1 coincidencia sustantiva → «Build, train, and scale AI workloads on Runpod with cloud GPUs, Serverless, and Clusters.» (copy de marketing, línea 365 del fetch).
- **[I]** Es decir: **cero menciones al entrenamiento con datos de clientes**.

---

### F02 · Terms of Service — https://www.runpod.io/legal/terms-of-service — **200**
*Last Updated: March 24, 2026.*

**§2 Use of the Service; Responsibility for Content (extractos literales):**
> "You acknowledge that any information, data, text, software, music, sound, photographs, graphics, video, messages, tags and/or other materials accessible through the Service (collectively, 'Content'), is the sole responsibility of the party from whom such Content originated."

> "You agree that we may, but have no obligation to, access, store, process, and use any of Your Content. Runpod has no responsibility or liability for the deletion or accuracy of any Content, including Your Content... You are responsible for ensuring all data (including Your Content) is secured with backups and encryption as required to meet applicable laws and industry standards."

> "You acknowledge and agree that data privacy and information security is a shared responsibility between you and Runpod. Runpod is responsible for protecting the infrastructure that provides the Service to you... For the avoidance of doubt, the Service does not include your applications or Your Content. Under this shared responsibility model, you are responsible for protecting all data (including Your Content) both at rest and in transit, virtual machine guests, operating system(s) (including updates and security patches), associated application software, as well as security configuration of the Service provided by Runpod, including but not limited to firewall, load balancer, object storage, block storage, IP and DNS configuration."

**§4.2.1 Community Cloud (literal completo):**
> "Runpod offers peer-to-peer GPU computing that connects individual compute providers ('Hosts') to compute consumers (the 'Community Cloud'). Runpod has no responsibility for the actions of Hosts, and Runpod makes no warranty that the Community Cloud Offerings will meet your requirements or be available on an uninterrupted, error-free basis. Runpod does not make any specific uptime warranties with respect to the Community Cloud Offerings. Runpod is only the venue to connect Hosts with consumers, and Runpod is not a party to any interaction between compute consumer and any Host."

**§5 Intellectual Property Rights (párrafo clave, literal):**
> "We do not assert any ownership over Your Content. You retain full ownership of all of Your Content and any intellectual property rights or other proprietary rights associated with Your Content... You grant Runpod a non-exclusive, worldwide, royalty-free and fully paid-up license to: (i) access and use Your Content to operate and provide the Service to Customer; and (ii) use Your Content in an aggregated and anonymized form to update and improve the Service and Runpod's related products and services."

> "You may delete, or request deletion of Your Content at any time, unless you have shared Your Content with others and they have not deleted it, or it was copied or stored by other users."

**§7 User Content (sobre monitoreo):**
> "Runpod will not actively monitor Content being hosted by Runpod, although Runpod, at its sole discretion, may elect to electronically monitor its network and may disclose any content or records concerning Your account as necessary to satisfy any law, regulation, or other governmental request or to properly operate Our network and protect our customers."

**§12 Term and Termination (extractos):**
> "Runpod reserves the right to terminate these Terms of Use or your access to the Service at any time without cause upon notice to you... WE MAY TERMINATE YOUR USE OR PARTICIPATION IN THE SITE AND THE SERVICE OR DELETE YOUR ACCOUNT AND ANY CONTENT OR INFORMATION THAT YOU POSTED AT ANY TIME, WITHOUT WARNING, IN OUR SOLE DISCRETION."

**§13 Governing Law; Venue:**
> "governed by and construed in accordance with the laws of the State of Delaware... all claims and disputes arising out of or relating to these Terms of Use will be litigated exclusively in the state or federal courts located in the State of New Jersey."

**§14 Arbitration:** arbitration vinculante + renuncia a acción colectiva + jury trial waiver.

**Búsqueda literal `train|machine learning|AI`:**
- ToS: «Build, train, and scale AI workloads on Runpod with cloud GPUs, Serverless, and Clusters.» (marketing, línea 352 del fetch).
- **[I]** Ninguna otra. **El ToS no prohíbe entrenar con datos de clientes.**

---

### F03 · Data Processing Agreement — https://www.runpod.io/legal/data-processing-agreement — **200**

**§1 Introducción (literal, clave):**
> "To execute this DPA, Customer must complete the signature block and required information and submit the signed DPA to Runpod via this link: https://eform.pandadoc.com/?eform=34365310-d8a3-42dd-8393-a42d69150c5d. This DPA shall become legally binding only upon completion of all such steps. Any modifications, alterations, or amendments to the content of this DPA by Customer shall prevent the formation of a binding agreement between the Parties..."

**[V]** El DPA **no** está firmado automáticamente.

**§2 Definiciones (extractos):**
> "**Performance Data** means any log files, metadata, telemetry data, and other technical performance data automatically generated by the Service relating to the use, performance, efficacy, reliability, and/or accuracy of the Runpod Services (certain of which may constitute Personal Data)."

**§3 Detalles del procesamiento:**
> "Runpod collects, uses, and discloses Customer Personal Data solely for the purposes of providing the Services and for such other ancillary purposes consented to by the Customer or as required by law. Processing operations are limited to those required to perform the Services in accordance with the Agreement. Runpod shall not determine the purposes for which or the manner in which Customer Personal Data is processed, and neither Runpod nor its Sub-Processors shall process Customer Personal Data for their own purposes."

**§4 Place of Data Processing (literal completo — LA GRIETA):**
> "Runpod uses third-party data hosting providers (as identified in Attachment 2) to host the Services on servers located throughout the world, including in the United States. Where a region is specified by Customer during service instantiation, Runpod will use **reasonable efforts** to allocate a server in a geographically proximate location. Where cross-border transfer cannot be avoided, legally required authorization mechanisms shall be applied."

**[I]** «Reasonable efforts» ≠ garantía de región asignada.

**§5 Instructions (literal):**
> "Runpod shall process Personal Data for the purposes of: (i) processing as required by Customer in its use of the Services; (ii) processing in accordance with the Agreement, this DPA and any other agreements between the Parties, (iii) processing to comply with other reasonable instructions provided by Customer where such instructions are consistent with the terms of the Agreement, applicable laws and DPA."

> "Runpod shall process such data **solely in accordance with Customer's documented instructions** and shall not process it for any other purpose."

**§7 TOMs:**
> "Runpod shall implement reasonably necessary technical and organizational measures ('TOMs')... The TOMs implemented by Runpod are specified in Attachment 1. Runpod reserves the right to modify the TOMs at any time, provided that any modifications shall not materially decrease the security of Customer Personal Data."

**§8 Sub-Processors:**
> "Upon authorizing any new Sub-Processor to access Personal Data, Runpod will update the list of Runpod's Sub-Processors... Within ten (10) business days of an update to the list of Sub-Processors, Customer shall inform Runpod, in writing, of objections..."

**§12 Deletion or Returning Personal Data:**
> "Upon Customer's request, Runpod shall irretrievably delete or return all Personal Data in accordance with the Agreement, unless retention is required by applicable law."

**§11 DPIA:** "Upon Customer's request, Runpod shall provide reasonable assistance in conducting a DPIA..."

**§13 Information & Audit Rights:** "no more than once per calendar year... Runpod shall permit and contribute to audits, including on-premise inspections... All costs associated with any audit shall be borne solely by Customer."

**§14 Restricted Transfers:** "Any Restricted Transfer shall be subject to the Standard Contractual Clauses and/or the UK Addendum, as applicable." (SCC Decisión de Ejecución (UE) 2021/914; UK Addendum B1.0 del ICO en vigor desde 2022-03-21.)

**§18 Performance Data (literal, clave):**
> "Customer acknowledges that Runpod may collect, use, and disclose Performance Data for its own business purposes, including: (i) accounting, tax, billing, audit, and compliance; (ii) providing, improving, developing, optimizing, and maintaining the Services; (iii) investigating fraud, spam, or wrongful or unlawful use of the Services... Runpod independently determines the purposes and means thereof... For the avoidance of doubt, **this DPA shall not apply to Runpod's Processing of Performance Data, and Performance Data does not constitute Customer Personal Data**."

**[I]** La retención de logs/telemetría de la plataforma **no está acotada por el DPA**.

**Attachment 1 — TOMs (extractos):**
| Medida | Texto literal |
|---|---|
| Encryption | "Encryption is used for data in transit and at rest, and this encryption is provided by Amazon Web Services Inc. ('AWS') and Secure Cloud data centers, approved Sub-Processors (see Attachment 2). Runpod also encrypts data in transit." |
| Integrity | "The Services provide administrative controls for Customer to control who can access files within their firm. **Runpod does not have these rights.**" |
| Resilience | "The Services are hosted on AWS platform and Secure Cloud data centers. These hosting platforms are ISO 27001 and SOC 2 Type 2 certified..." |
| Restoration | "Backup policy and procedures are in place, with daily automated backup reports..." |
| Adicional | "Certification under SOC 2 Type II; End-to-end encryption of data in transit and at rest; Strict role-based access controls... Real-time monitoring and automated workload management systems..." |

**Attachment 2 — Sub-Processors (lista completa, 14):**

| Sub-Processor | Propósito (resumen literal) | Relevancia PI |
|---|---|---|
| **Amazon Web Services Inc.** | "Services and Customer Data is processed with Runpod licensed software, on Amazon Web Services Inc.'s infrastructure." | **CRÍTICO**: AWS es la infraestructura; en Community Cloud el host no es AWS. |
| **Google Workspace - Google Inc.** | "collection of cloud computing, productivity and collaboration tools" | ancillary |
| **Google Cloud - Google Inc.** | idem | ancillary |
| **HubSpot Inc.** | CRM / Sales & Marketing | ancillary |
| **Stripe Inc.** | "payment card information" | ancillary |
| **BetterStack Inc.** | "A log monitoring platform, technical service and **Runpod application logs are sent to BetterStack** for search, analysis, and system monitoring. Sensitive data fields are masked such as usernames and emails, while some low sensitivity data such as IP and Host are captured directly." | **[P]** ¿stdout del pod del cliente? |
| **Cloudflare Inc.** | "a content delivery platform that improves network performance, security and reliability to customers **by caching static content** and optimizing web traffic" | **CRÍTICO** si hay proxy HTTP expuesto: Cloudflare cachea |
| **PlanetScale** | base de datos para ingeniería | ancillary |
| **Docker Inc.** | "managing applications in an isolated environment" | ancillary |
| **Datadog Inc.** | "A SIEM platform that provides application monitoring, infrastructure monitoring, **log management**, and alerting" | **[P]** ¿logs del cliente? |
| **Clerk Inc.** | autenticación de usuarios | ancillary |
| **Tinybird** | data pipelines / analytics | ancillary |
| **DigitalOcean LLC.** | "A cloud infrastructure and hosting platform that manages virtual servers, storage, and networking resources enabling Runpod to deploy, scale, manage applications and services." | infraestructura secundaria |
| **Snowflake Inc.** | data warehouse | ancillary |

**Attachments 3-7:** SCC Module Two + docking clause + Option 2; UK Addendum B1.0; Switzerland Addendum (FADP/FDPIC); State Privacy Laws Addendum (CCPA: "It is the Parties' intent that with respect to any personal information, Runpod is a service provider"); Brazil Addendum (LGPD, ANPD Resolution CD/ANPD 19/2024).

---

### F04 · Compliance — https://www.runpod.io/legal/compliance — **200** *(Updated September 13, 2026)*

> "Runpod Inc. operates an Information Security Management System certified to ISO/IEC 27001:2022 by Sensiba LLP, an ANAB-accredited certification body. **Certificate RUN-ISMS-20260827 is valid from August 27, 2026 through August 26, 2029.** Its scope is limited to the ISMS directly supporting Runpod's services and platform solutions, including the infrastructure, people, and technologies, in accordance with the Statement of Applicability. **Certification covers the management system, not individual products or services.** The certificate is available in the Runpod Trust Center."

> "Runpod has also completed SOC 2 Type II and SOC 3 examinations, and maintains HIPAA and GDPR programs. The Runpod Trust Center lists current compliance resources, including the ISO/IEC 27001:2022 certificate, SOC 2 Type II, SOC 3, HIPAA, GDPR, and the SOC 2 Bridge Letter 2026. Some documents require approved access before download."

**Data Center Partners (literal):**
> "Runpod works with data center and infrastructure partners across regions. **Compliance coverage can vary by workload, region, provider, and deployment model**, so customers should confirm specific requirements with Runpod during security review.
>
> For data residency, private deployment, or region-specific requirements, contact Runpod so the team can review the right configuration and documentation for your workload."

**FAQ:**
> "Where can I get Runpod's SOC 2 report? → Request access through the Runpod Trust Center. Available documents may require approval before download."
> "Can Runpod support compliance-specific requirements? → Runpod can discuss region, deployment, procurement, and compliance requirements during evaluation."

**[I]** Las certificaciones de los datacenters Secure Cloud **no están publicadas individualmente**.

---

### F25 · Help Center — BAA / DPA / compliance filter — https://contact.runpod.io/hc/en-us/articles/50120688006163-How-to-Find-HIPAA-GDPR-Compliant-GPUs-on-Runpod-and-Understand-BAA-Policy — **200** *(March 20, 2026 22:59 Updated, por "Namrata")*

**Filtro de compliance (literal):**
> "When deploying a Pod, you can apply a compliance filter directly from the deployment page.
> 1. Log in to your Runpod account. 2. Go to the Deploy Pod page. 3. Open Additional filters. 4. Select Security & compliance. 5. Choose the compliance certification or policy you want to use. 6. Runpod will show only the GPUs that are applicable for that selection."

**Umbral para acuerdos a medida (literal — BLOQUEANTE):**
> "Execution of custom legal agreements, including: BAAs, DPAs, bespoke or custom contract terms is reserved for customers with a **committed monthly spend of $3,000 or more**.
>
> This threshold reflects the legal and executive resources required to support negotiation, custom risk allocation, and ongoing agreement management."

**Recursos listados:** Runpod Trust Center (trust.runpod.io) · Runpod Standard DPA (www.runpod.io/legal/data-processing-agreement) · Compliance Overview · Security Overview.

---

### F26 · Trust Center — https://trust.runpod.io/ — **citada** (contenido vía índice de búsqueda; el acceso real requiere aprobación)

> "Runpod is the AI Developer Cloud... All of it runs across **31 global regions**, so you can place workloads in the jurisdictions your policies require.
>
> Runpod holds **SOC 2 Type 2, SOC 3, and ISO/IEC 27001:2022**, and maintains active **HIPAA and GDPR** programs. Current reports, the SOC 2 Bridge Letter 2026, and the Data Processing Agreement are listed below. **Some documents require approved access.**"

Compliance list: GDPR · HIPAA · ISO/IEC 27001:2022 · SOC 2 Type 2 · SOC 3.
Documents: SOC 2 Bridge Letter 2026 · COMPLIANCE HIPAA · COMPLIANCE ISO/IEC 27001:2022 · COMPLIANCE SOC 2 Type 2 · COMPLIANCE SOC 3.

---

## BLOQUE 2 — DOCS RUNPOD

### F07 · Data security and legal compliance — https://docs.runpod.io/references/security-and-compliance — **200**

> "Your Pods and workers run in a multi-tenant environment with containerized isolation that prevents other users from accessing your data. Each Pod/worker operates in its own container with strict separation from other workloads. For sensitive workloads requiring enhanced security, **Secure Cloud operates in T3/T4 data centers** with enterprise-grade security, high reliability, redundancy, and fast response times."

> "Runpod's terms of service **prohibit hosts from inspecting your Pod/worker data** or analyzing your usage patterns. Any violation results in immediate removal from the platform. For workloads requiring the highest level of security, Secure Cloud provides vetted infrastructure partners who meet enterprise security standards including **SOC 2, ISO 27001, and PCI DSS** certifications."

> "**Runpod is fully compliant with the General Data Protection Regulation (GDPR) for data processed in European data center regions.** The platform implements comprehensive policies, procedures, and technical measures to meet GDPR requirements."

> "For servers hosted in GDPR-compliant regions like the European Union, Runpod maintains clear procedures for the collection, storage, processing, and deletion of personal data... For lawful transfer of personal data outside the EU, Runpod uses appropriate mechanisms such as adequacy decisions, standard contractual clauses, or binding corporate rules."

**[I]** La afirmación de GDPR es **por región**, no global.

---

### F09 · Pods / Pricing — https://docs.runpod.io/pods/pricing — **200**

> "Pods are billed by the **second** for compute and storage, with **no fees for data ingress or egress**. Find the latest GPU pricing on the Runpod console during Pod deployment."

**Storage pricing (tabla literal):**

| Storage type | Running Pod | Stopped Pod | Notes |
|---|---|---|---|
| Container disk | $0.10/GB/month | Not charged | Temporary; erased when Pod stops |
| Volume disk | $0.10/GB/month | **$0.20/GB/month** | Persistent; retained until Pod deleted |
| Network volume | $0.07/GB/month (< 1TB) | $0.07/GB/month | Permanent; portable between Pods |
| (network >1TB) | $0.05/GB/month | $0.05/GB/month | |

> "Storage is billed per-second for container and volume disks, and hourly for network volumes. **You are not charged if the host machine is unavailable.**"

> "**Runpod is not designed for long-term cloud storage.** Back up critical data to your local machine or a dedicated storage provider."

**Savings plans:** "Savings plans are deprecated and can no longer be purchased."

**On-demand:** "**You must have at least one hour's worth of credits** for your selected configuration to deploy an on-demand instance."

**Account limits:**
> "**Minimum balance**: Pods are automatically stopped when your account balance reaches $0. Pods with a network volume are stopped and their data is preserved, while Pods without a network volume are terminated and their data cannot be recovered."
> "**Spend limit**: Default limit of $80/hour across all resources."

---

### F10 · Storage options — https://docs.runpod.io/pods/storage/types — **200**

**Tabla comparativa (literal):**

| | Container disk | Volume disk | Network volume | Global volume |
|---|---|---|---|---|
| Persistence | Lost on stop/restart | Retained until Pod deleted | Retained independently | Retained independently |
| Mount path | System-managed | /workspace (default) | /workspace (replaces volume disk) | /workspace, or /workspace-global |
| Performance | Fastest (local) | Fast (local) | Variable (network) | Variable (optimized for reads) |
| Shareable | No | No | Yes | Yes (across Pods in any data center) |
| Resizable | Yes | Increase only | Yes | Automatic |
| Cost | $0.10/GB/month | $0.10 running / $0.20 stopped | $0.07 (<1TB) / $0.05 beyond | $0.09/GB/month + IOPS |
| Best for | OS, temp files, cache | Models, datasets, checkpoints | Shared data, portable storage | Model weights, read-heavy shared assets |

**Volume disk — cifrado (literal):**
> "You can encrypt your volume disk to protect sensitive data. When encryption is enabled, the volume is encrypted at rest on the host machine, and only your Pod can access the data.
>
> To enable encryption when creating a Pod, select the **Encrypt volume** checkbox in the Pod creation flow.
>
> **WARNING**: Your encryption key cannot be retrieved, and bring your own key is not supported. Runpod securely stores your key and passes it only to your container image at runtime.
>
> **NOTE**: **Encryption applies only to volume disk. Container disk and network volumes cannot be encrypted.**"

**Network volume (literal):**
> "Network volumes must be attached during Pod creation and cannot be detached later. When attached, the network volume replaces the volume disk at `/workspace`."

**Global volume (literal):** "Global volumes are in beta. Features and behavior may change before general availability." / "A Pod supports one global volume and one network volume at a time."

**Modificar capacidad:** "volume disk size can only be increased, not decreased" + "Editing a running Pod resets it completely, erasing all data that isn't stored in your `/workspace` directory."

---

### F11 · Network volumes — https://docs.runpod.io/storage/network-volumes — **200**

> "Network volumes are backed by high-performance NVMe SSDs with transfer speeds of 200-400 MB/s (up to 10 GB/s peak)."

**Pricing:** "First 1 TB: $0.07/GB/month · Beyond 1 TB: $0.05/GB/month"

**Advertencia de saldo (literal):**
> "When your account balance reaches $0, Pods with an attached network volume are stopped and your data is preserved on the volume. **Storage charges continue to accrue while the Pod is stopped, so if your balance stays at $0 and these charges can't be covered, the network volume may eventually be terminated and its data cannot be recovered.**"

**CRÍTICO (literal):**
> "**Network volumes are only available for Pods in the Secure Cloud.**"

**Restricción de DC (literal):**
> "Attaching a single network volume constrains worker deployments to that volume's datacenter, which may limit GPU availability and reduce failover options."
> "You can only select one network volume per datacenter."
> "Data does not sync automatically between volumes."

**Creación:** "Select a data center, enter a name, and specify size in GB. Select a storage tier: Standard or High-Performance (available in select data centers)." · "Volume size can be increased later but cannot be decreased. For volumes beyond 4 TB, contact support."

---

### F12 · Global networking — https://docs.runpod.io/pods/networking — **200**

> "Global networking creates a secure, private network that connects all your Pods within your Runpod account. This feature enables Pod-to-Pod communication as if they were on the same local network, regardless of their physical location across different data centers.
>
> **WARNING**: Global networking is currently only available for NVIDIA GPU Pods."

> "Global networking provides each Pod with a **private IP address accessible only to other Pods in your account**. This creates an isolated network layer **separate from the public internet**... The network operates at **100 Mbps** between Pods, providing reliable connectivity for most inter-Pod communication needs while maintaining security through **complete isolation from external networks**."

**Cómo se habilita (literal):**
> "1. Navigate to the Pods section and click Deploy. 2. At the top of the page, toggle **Global Networking** to filter and show only Pods with networking support. 3. Select your desired GPU configuration and complete the deployment process."

**DNS interno:** `POD_ID.runpod.internal` (ej. `abc123xyz.runpod.internal:5432`).
**Servicios internos:** "Simply bind your service to all interfaces (`0.0.0.0`) and connect using the internal DNS name."

**Security best practices (literal):**
> "Global networking provides network isolation, but proper security practices remain essential. **Never expose ports on Pods running sensitive services** like databases, cache servers, or internal APIs; instead, use global networking for these components. Even within your private Pod network, you should implement authentication between services."

**Data centers soportados (17, tabla literal):**
`CA-MTL-3` (Canada) · `EU-CZ-1` (Rep. Checa) · `EU-FR-1` (Francia) · `EU-NL-1` (Países Bajos) · `EU-RO-1` (Rumanía) · `EU-SE-1` (Suecia) · `EUR-IS-2` (Islandia) · `OC-AU-1` (Australia) · `US-CA-2` · `US-GA-1` · `US-GA-2` · `US-IL-1` · `US-KS-2` · `US-NC-1` · `US-TX-3` · `US-TX-4` · `US-WA-1`

> "Choose data centers strategically based on: Geographic proximity for lower latency · **Compliance requirements for data residency** · Availability of specific GPU types"

---

### F13 · Expose ports — https://docs.runpod.io/pods/configuration/expose-ports — **200**

**HTTP proxy (literal):**
> "Runpod's HTTP proxy provides the easiest way to expose web services from your Pod... To configure HTTP ports during Pod deployment, click **Edit Template** and add a comma-separated list of ports to the **Expose HTTP Ports (Max 10)** field."
> URL: `https://[POD_ID]-[INTERNAL_PORT].proxy.runpod.net`

**Limitaciones (literal):**
```
User → Cloudflare → Runpod Load Balancer → Your Pod
```
> "**100-second timeout**: Cloudflare enforces a maximum connection time of 100 seconds. If your service doesn't respond within this time, the connection closes with a `524` error."
> "**HTTPS only**: All connections are secured with HTTPS, even if your internal service uses HTTP."
> "**Public accessibility**: Your service becomes publicly accessible. While the Pod ID provides some obscurity, implement proper authentication in your application."

**Direct TCP (literal):**
> "**Pods do not support UDP connections.**"
> "In your Pod or template configuration, follow the same steps as for HTTP ports, but add ports to the **Expose TCP Ports** field. This enables direct TCP forwarding with a public IP address."
> Ejemplo: `TCP port 213.173.109.39:13007 -> :22`
> "**Public IP addresses may change for Community Cloud Pods if your Pod is migrated or restarted, but they should remain stable for Secure Cloud Pods.**"
> "External port mappings change whenever your Pod resets."

**Symmetrical ports:** "specify port numbers above 70000 in your TCP configuration" → `RUNPOD_TCP_PORT_70000`.

**Security considerations (literal):**
> "**Implement authentication**: Both HTTP proxy and TCP access make your services publicly accessible. Always implement proper authentication and authorization in your applications."
> "**Use HTTPS for sensitive data**: While the proxy automatically provides HTTPS, TCP connections do not. Implement TLS in your application when handling sensitive data over TCP."

**Common use cases:** "**Database connections**: Use TCP with proper security measures. Consider using Runpod's global networking for internal-only databases."

---

### F14 · Manage Pods — https://docs.runpod.io/pods/manage-pods — **200**

**Stop (literal):**
> "Stopping a Pod releases the GPU and preserves data in `/workspace` (volume disk). **Container disk data is cleared.**
>
> **WARNING: You'll still be charged for volume disk storage while stopped.** Terminate the Pod if you don't need to retain your environment."
> "When using a network volume, your `/workspace` data is preserved whether you stop or terminate the Pod."

**Terminate (literal):**
> "**CAUTION: Terminating permanently deletes all data not stored in a network volume.** Export important data first."

**Start:** "Note: You may be allocated **zero GPUs** if capacity has changed."
**Restart:** "Unlike stopping and starting, restarting can't leave you with zero GPUs."
**Update:** "Editing a running Pod resets it completely, erasing all data not stored in `/workspace` or a network volume."

**Logs (literal):**
> "Pods provide two log types: * **Container logs**: Application output (stdout) * **System logs**: Pod lifecycle events (startup, shutdown, errors)"

**Troubleshooting (literal):**
> "| **Docker Compose not working** | Not supported. Use a **custom template** with your dependencies baked in. |"

---

### F15 · Maintenance, outages, and data safety — https://docs.runpod.io/pods/maintenance-and-outages — **200**

> "Runpod operates on **shared infrastructure**. Like any cloud platform, maintenance and unexpected outages can occur."
> "During a maintenance window, Runpod does not charge you for the time your pod is unavailable."
> "Hardware failures and sudden crashes can happen without warning... Runpod may only be able to notify you after the outage has begun."

**Data safety (literal):**
> "Pods use temporary container storage by default. If your pod is interrupted, restarted, stopped, or terminated, any data that is only stored on container storage will be lost."
> "**Runpod cannot guarantee recovery of data stored only on ephemeral container disk.**"

**Regla 3-2-1 (literal):**
> "3 copies of your data · 2 different storage types (for example, a network volume and an external object store) · 1 copy stored offsite or in a separate location"

---

### F16 · Pods Overview — https://docs.runpod.io/pods/overview — **200**

**Pod types (literal):**
> "**Secure Cloud:** Operates in T3/T4 data centers, providing high reliability and security for enterprise and production workloads.
> **Community Cloud:** Connects individual compute providers to users through a vetted, secure peer-to-peer system, with competitive pricing options."

**Pricing (literal):** "Pods are billed by the second with no fees for ingress/egress."

**Limitations (literal):**
> "* **Docker Compose is not supported:** Runpod runs Docker for you, so you cannot spin up your own Docker instance or use Docker Compose on Pods.
> * **UDP connections are not supported:** Pods only support TCP and HTTP connections.
> * **Windows is not supported:** Pods do not currently support Windows."

**Storage (literal):** "container disk (Temporary storage that exists only while a Pod is running, and is completely lost when the Pod is stopped or deleted)... volume disk (Persistent storage that remains available for the duration of the Pod's lease... Mounted at /workspace by default)... optional network volume (Persistent storage that exists independently of your other compute resources. Can be attached to multiple Pods or Serverless endpoints to share data between machines.)"

---

### F17 · Choose a Pod — https://docs.runpod.io/pods/choose-a-pod — **200**

**Tabla Secure vs Community (literal):**

| | Secure Cloud | Community Cloud |
|---|---|---|
| Infrastructure | T3/T4 data centers | Peer-to-peer providers |
| Reliability | High redundancy | Variable |
| Best for | Production, sensitive data | Cost-sensitive workloads |
| Pricing | Standard | Competitive |

**NOTA CRÍTICA (literal):**
> "**Runpod is no longer accepting new hosts for Community Cloud. Existing Community Cloud resources remain available.**"

**MIG (literal):**
> "RTX PRO 6000 Multi-Instance GPU (MIG) slices are partitioned GPU instances with dedicated memory and compute. **Available on Secure Cloud only.** All MIG slices use Blackwell architecture."

**Workload → GPU (literal):**
| Workload | Recommended GPU tier | Minimum VRAM |
|---|---|---|
| Image generation (SDXL, Flux) | Mid-range (RTX 4090, L4, PRO 6000 MIG 24GB) | 16–24 GB |
| 3D rendering | Mid-range with RT cores | 16–24 GB |
| LLM training/fine-tuning | High-end (A100, H100) | 40–80 GB |

---

### F18 · Pod templates — https://docs.runpod.io/pods/templates/overview — **200**

> "Templates contain all components needed to launch a fully configured Pod:
> * **Container image**: The Docker image with all software packages and dependencies.
> * **Hardware specifications**: Container disk size, volume size, and mount paths.
> * **Network settings**: Exposed HTTP and TCP ports for web UIs or APIs.
> * **Environment variables**: Pre-configured settings that customize application behavior.
> * **Startup commands**: Instructions that run when the Pod launches."

Tipos: Official (full Runpod support) · Community (Discord only, sin soporte) · **Custom (Self-supported)**.

---

### F19 · Connect to a Pod with SSH — https://docs.runpod.io/pods/configuration/use-ssh — **200**

**Basic SSH (literal):**
> "**All Pods provide a basic SSH connection that is proxied through Runpod's systems.** This method does not support commands like SCP (Secure Copy Protocol) or SFTP (SSH File Transfer Protocol)."
> `ssh 8y5rumuyb50m78-6441103b@ssh.runpod.io -i ~/.ssh/id_ed25519`

**Full SSH (literal):**
> "For full SSH capabilities, including SCP and SFTP for file transfers, you need to rent an instance that supports a public IP address... if you're using a custom template, ensure that **TCP port 22 is exposed** and that the SSH daemon is running inside your Pod."
> `ssh root@213.173.108.12 -p 17445 -i ~/.ssh/id_ed25519`

**Autenticación:** "Runpod does not require a password for SSH connections, as authentication is handled entirely through your SSH key pair."
**Override por pod:** "you can override the default by setting the `SSH_PUBLIC_KEY` environment variable for this Pod."

---

### F20 · Connection options — https://docs.runpod.io/pods/connect-to-a-pod — **200**

| Method | Best for | Persistence | Setup |
|---|---|---|---|
| Web terminal | Quick commands, debugging | Session-based | None |
| SSH | Long-running processes | Persistent | SSH client |
| JupyterLab | Data science, notebooks | Session-based | Template-dependent |
| VS Code/Cursor | Full development environment | Persistent | Extension |

**JupyterLab (literal):**
> "Set the `JUPYTER_PASSWORD` environment variable to configure JupyterLab authentication. **If not set, some templates use a default password shown in the Pod logs.**"
> `https://[POD_ID]-8888.proxy.runpod.net`

---

### F21 · Zero GPU Pods on restart — https://docs.runpod.io/pods/troubleshooting/zero-gpus — **200**

> "When you deploy a Pod, it's assigned to a GPU on a specific physical machine. This creates a link between your Pod and that particular piece of hardware. As long as your Pod is running, that GPU is exclusively reserved for you. When you stop your Pod, you release that specific GPU, allowing other users to rent it. Your Pod's volume storage remains on the physical machine, but the GPU slot becomes available."
> "The most effective way to avoid this issue is to use **network volumes**."

---

### F22 · API v2 — List data centers — https://docs.runpod.io/api-reference-v2/catalog/list-data-centers — **200**

**Endpoint:** `GET https://api.runpod.io/v2/catalog/datacenters` — `security: bearerAuth: []` → **401 sin token**.

**Query params:** `include` (GPU_AVAILABILITY, CPU_AVAILABILITY) · `regions` (OR semantics) · `networkVolumeTypes` (AND) · `compliance` (AND; ejemplo `GDPR,SOC_2_TYPE_2`) · `globalNetwork` (boolean).

**Enums literales:**
- `DataCenterRegion`: `NORTH_AMERICA`, **`SOUTH_AMERICA`**, `EUROPE`, `ASIA`, `MIDDLE_EAST`, `AFRICA`, `OCEANIA`, `ANTARCTICA`, `UNKNOWN`
- `Compliance`: `GDPR`, `ISO_IEC_27001`, `ISO_14001`, `PCI_DSS`, `HITRUST`, `SOC_1_TYPE_2`, `SOC_2_TYPE_2`, `SOC_3_TYPE_2`, `ITAR`, `FISMA_HIGH`, `HIPAA`, `RENEWABLE`
- `VolumeType`: `STANDARD`, `HIGH_PERFORMANCE`

**Ejemplo de respuesta (literal):**
```json
{ "id": "US-KS-2", "name": "US Kansas 2", "region": "NORTH_AMERICA",
  "globalNetwork": true, "networkVolumeTypes": ["STANDARD","HIGH_PERFORMANCE"],
  "compliance": ["SOC_2_TYPE_2","ISO_IEC_27001"] }
```

**[I]** El enum de regiones incluye `SOUTH_AMERICA` pero **ningún data center sudamericano está publicado** en el enum de `dataCenterIds` de la API de creación de pods.

---

### F23 · runpodctl datacenter — https://docs.runpod.io/runpodctl/reference/runpodctl-datacenter — **200**

> "`runpodctl datacenter list` — List the datacenters you can deploy to, with GPU availability in each one. **Datacenters that aren't open for deployment aren't listed.**"
> "The `location` field is the datacenter's region, such as `NORTH_AMERICA`, `EUROPE`, or `ASIA`."
> `runpodctl pod create --template-id runpod-torch-v21 --gpu-id "NVIDIA RTX 4090" --data-center-ids "US-GA-1"`
> "Datacenter IDs are region-prefixed; ... `runpodctl datacenter list` is authoritative — the set grows over time; run it for the current list." (de runpod-plugins-official, GitHub)

---

### F27 · API reference — Create a new Pod — https://docs.runpod.io/api-reference/pods/POST/pods — **citada** (URL oficial, no fetcheada)

**`cloudType`** (default `SECURE`): "Set to SECURE to create the Pod in Secure Cloud. Set to COMMUNITY to create the Pod in Community Cloud."

**`dataCenterIds`** — enum completo (28):
```
EU-RO-1, CA-MTL-1, EU-SE-1, US-IL-1, EUR-IS-1, EU-CZ-1, US-TX-3, EUR-IS-2,
US-KS-2, US-GA-2, US-WA-1, US-TX-1, CA-MTL-3, EU-NL-1, US-TX-4, US-CA-2,
US-NC-1, OC-AU-1, US-DE-1, EUR-IS-3, CA-MTL-2, AP-JP-1, EUR-NO-1, EU-FR-1,
US-KS-3, US-GA-1
```

**`dataCenterPriority`** (default `availability`): "Set to availability to respond to current machine availability. Set to custom to always try to rent machines from data centers in the order specified in dataCenterIds."

**[I]** Sin `UK-*` ni `*AR*`/`*BR*`/`*CL*` en el enum.

---

### F24 · Índice de documentación — https://docs.runpod.io/llms.txt — **200**

Índice maestro de ~400 páginas. Entradas sobre Pods: `pods/overview`, `pods/pricing`, `pods/choose-a-pod`, `pods/manage-pods`, `pods/maintenance-and-outages`, `pods/connect-to-a-pod`, `pods/configuration/use-ssh`, `pods/configuration/connect-to-ide`, `pods/configuration/expose-ports`, `pods/networking`, `pods/storage/types`, `pods/storage/transfer-files`, `pods/storage/cloud-sync`, `pods/templates/*`, `pods/troubleshooting/*`, `storage/*`, `references/security-and-compliance`, `references/gpu-types`, `api-reference-v2/catalog/list-data-centers`.

**Búsqueda `tailscale|wireguard|vpn|private network` en el índice completo → 1 única coincidencia:**
> "Global networking — https://docs.runpod.io/pods/networking.md: Connect your Pods through a secure private network for internal communication."

**[V] PRUEBA NEGATIVA: Runpod no documenta Tailscale, WireGuard, VPN ni overlay de acceso remoto en ningún lugar de su documentación oficial.**

---

### F05 · Pricing (marketing) — https://www.runpod.io/pricing — **200** *(Updated October 8, 2026; dateModified 2026-10-08)*

> "Thousands of GPUs across **30+ regions**. Simple pricing plans for teams of all sizes, designed to scale with you."

**Pods — tabla oficial (USD/hora), Community vs Secure:**

| VRAM | GPU | vCPU/RAM | Community | Secure |
|---|---|---|---|---|
| 24 GB | RTX A5000 | 9/25 | $0.16 | $0.27 |
| 24 GB | **RTX 3090** | 16/125 | **$0.22** | **$0.50** |
| 24 GB | L4 | 12/50 | $0.44 | $0.59 |
| 24 GB | RTX 4090 | 6/41 | $0.34 | $0.89 |
| 24 GB | RTX Pro 6000 MIG 24GB | 4/31 | $0.50 | $0.69 |
| 32 GB | RTX 5090 | 9/35 | $0.69 | $1.19 |
| 48 GB | RTX A6000 | 9/50 | $0.33 | $0.59 |
| 48 GB | **A40** | 9/50 | **$0.35** | **$0.59** |
| 48 GB | L40 | 8/94 | $0.69 | $0.82 |
| 48 GB | RTX 6000 Ada | 10/167 | $0.74 | $0.99 |
| 48 GB | L40S | 16/94 | $0.79 | $1.09 |
| 48 GB | RTX Pro 6000 MIG 48GB | 8/62 | $1.00 | $1.29 |
| 80 GB | A100 PCIe | 8/117 | $1.19 | $1.79 |
| 80 GB | A100 SXM | 16/125 | $1.39 | $1.79 |
| 80 GB | H100 PCIe | 16/188 | $1.99 | $2.89 |
| 80 GB | H100 SXM | 20/125 | $2.69 | $3.99 |
| 94 GB | H100 NVL | 16/94 | $2.59 | $3.19 |
| 96 GB | RTX Pro 6000 | 16/188 | $1.69 | $2.49 |
| 141 GB | H200 | 24/276 | $3.59 | $5.29 |
| 180 GB | B200 | 28/283 | $5.98 | $7.99 |
| 288 GB | B300 | 32/251 | $6.94 | $8.99 |

**Storage (misma página):** Container Disk $0.10/GB/mo · Volume Disk running $0.10 / idle $0.20 · Network Storage Standard under 1TB $0.07 / over 1TB $0.05 · Network Storage High-Performance $0.14.

**Serverless (misma página):** 24 GB (L4, A5000, 3090, MIG 24GB) $0.69/h · 4090 $1.10/h · 48 GB (A6000, A40) $1.22/h · 48 GB PRO (L40S, 6000 Ada, MIG 48GB) $1.75/h · 32 GB 5090 $1.58/h · 80 GB A100 $2.72/h · 96 GB RTX 6000 Pro $3.49/h · 100 GB H100 $4.79/h · 180 GB B200 $8.64/h · 141 GB H200 $5.93/h · 280 GB B300 $10.65/h.

**Clusters:** H200 SXM $6.35/h · A100 SXM $2.15/h · L40S/H100 SXM/B200 "Contact sales".
**Reserved Clusters:** "SLA-backed uptime, and discounted rates for enterprises scaling to 10,000+ GPUs."

**[V]** JSON-LD `description` de la página (meta): "Rent H100 80GB from $1.99/hr, RTX 4090 from $0.34/hr".

---

### F06 · Keeping Data Secure — https://www.runpod.io/articles/guides/keep-data-secure-cloud-gpus — **200** *(Updated October 19, 2026; published 2025-07-11)*

**Cifrado (literal):**
> "**Runpod automatically encrypts all data on its servers with AES-256 encryption**, so if you store files on a Runpod volume or container disk, they're encrypted by default." / "Runpod uses **TLS** to secure all data in transit".

**Secure Cloud (literal):**
> "For sensitive data, always choose the most isolated option. On Runpod, this means using *Secure Cloud* instances rather than Community instances. Community GPU pods share a host machine with other customers (they're still isolated at the software level with container tech, but for highly sensitive use cases you may want absolute isolation). **Secure Cloud gives you a dedicated machine/GPU that is not shared with others.**"
> "**Your GPU and its host are single-tenant** – no other user's pods will run on the same machine. There's reduced risk of side-channel attacks or noisy neighbors affecting your environment."

**Puertos (literal):**
> "**Avoid opening unnecessary ports on your pod.** If you do expose a service (like a web app) on a port, consider restricting access (Runpod's advanced networking allows private clusters, etc., if needed for enterprise setups)."

**FAQ — propiedad de datos (literal):**
> "**Runpod's policy is that *you* control your data – they don't peek into it.** If you need to be sure data is wiped, you can delete volumes manually. Also, any snapshots or images you create from a pod are saved in your account's context and are not public unless you share them."

**FAQ — borrado (literal):**
> "By default, when a pod is terminated, its ephemeral container storage is deleted. If you stored data on that container (and not on a persistent volume), it's gone once the pod is removed – which is actually desirable for sensitive data, as it leaves no trace."

**Logs (literal):**
> "**Be mindful of logs and outputs**: Sometimes sensitive information can creep into log files (for instance, if you accidentally log a few samples of your dataset or print a secret by mistake). **Scrub logs of any secrets or personal data.**"

**Auditoría (literal):**
> "**Logs and monitoring for compliance**: Maintain an audit trail of what you did on the cloud: which data was uploaded, who accessed the environment, when was it terminated. This can be as simple as keeping a journal or saving console logs."

**[I]** La propia guía de Runpod recomienda **no subir material sensible** («If your policies forbid cloud use entirely, you might look into on-premise solutions or hybrid approaches where only non-sensitive parts go to the cloud.»).

---

### F07b · Hosting and Running Private AI Agents — https://www.runpod.io/articles/guides/hosting-and-running-private-ai-agents — **citada** (índice de búsqueda)

> "**Secure Cloud:** Runpod-owned T3/T4 data center hardware, enterprise-grade isolation. Runpod is SOC 2 Type II certified and holds SOC 3 and ISO/IEC 27001:2022. The third-party data centers underlying Secure Cloud hold their own certifications. For agents running in Secure Cloud, you're not sharing hardware with unknown community GPU providers."

> "**Persistent encrypted volumes**: model weights and any data cached to disk stay inside your Runpod account, encrypted at rest. **Container and volume disks are billed per second; network volumes (shareable across pods) are billed hourly.**"

> "Secure Cloud runs on **Runpod-owned data center hardware** with enterprise-grade isolation; **your model weights, input data, and inference outputs never leave Runpod-controlled infrastructure**."

> "Holding these certifications does not itself satisfy GDPR or HIPAA compliance; they demonstrate security controls are in place, which is a prerequisite, **not a substitute**, for regulatory compliance. Always confirm which certifications apply to **the specific infrastructure tier your workload runs on**, not the provider's organization as a whole."

> "**On-premises** — For workloads with the strictest data residency requirements – where data must physically stay within a specific jurisdiction and cannot transit through a cloud provider's infrastructure – on-premises GPU hardware remains the only fully private option."

---

## BLOQUE 3 — TAILSCALE

### F28 · Userspace networking mode — https://tailscale.com/docs/concepts/userspace-networking — **citada** (texto íntegro en índice de búsqueda; *Last validated Nov 12, 2025*)

> "Tailscale works on Linux systems using a device driver called `/dev/net/tun`, which lets you start the VPN tunnel as though it were any other network interface like Ethernet or Wi-Fi.
>
> However, not all Linux systems support `/dev/net/tun`. For example, some container-based app platforms like Heroku and Google Cloud Run do not. For those environments, **userspace networking mode offers a different way of running, where `tailscaled` functions as a SOCKS5 or HTTP proxy which other processes in the container can connect through.**
>
> Note: Userspace networking mode with SOCKS5 is available in Tailscale v1.8 or later. The HTTP proxy is available in Tailscale v1.16 or later."

> "You can enable userspace networking from the Tailscale CLI by passing the `--tun=userspace-networking` flag to `tailscaled` before running `tailscale up`. You can also use a SOCKS5 proxy and an HTTP proxy on the same port:
> ```shell
> tailscaled --tun=userspace-networking --socks5-server=localhost:1055 --outbound-http-proxy-listen=localhost:1055 &
> tailscale up --auth-key=<your-auth-key>
> ```
> **Userspace networking mode is primarily for serverless environments. We recommend using it with ephemeral nodes and auth keys** (as shown above)."

> "The Tailscale Docker image supports a `TS_USERSPACE` parameter that is equivalent to `tailscaled --tun=userspace-networking`."

> "After Tailscale is authenticated, your application can connect using a SOCKS5 or HTTP proxy or both. Many widely used networking packages support these proxies already, generally by setting the `ALL_PROXY` and `HTTP_PROXY` environment variables... Some libraries use `http_proxy` instead of `HTTP_PROXY`."

**Key auth (de la misma doc, flag `tailscale up`):** `--auth-key=<key>` ("Provide an auth key to automatically authenticate the node as your user account"), `--advertise-tags=<tag>`, `--ssh`, `--accept-routes`, `--reset`.

**[I]** En modo userspace **no hay interfaz de red real**: el tráfico saliente del pod puede ir por SOCKS5/HTTP proxy. El **tráfico entrante** desde el estudio al pod no es un flujo documentado en este modo.

### F30 · Tailscale CLI — https://tailscale.com/kb/1080/docker — **200** *(redirect → "Tailscale CLI", Last validated Jul 30, 2026)*

**`tailscale up` (flags relevantes, literal):**
- `--accept-routes` — "Accept subnet routes that other nodes advertise."
- `--advertise-exit-node` — "Offer to be an exit node for outbound internet traffic from the Tailscale network. Defaults to not offering to be an exit node."
- `--advertise-routes=<ip>` — "Expose physical subnet routes to your entire Tailscale network."
- `--auth-key=<key>` — "Provide an auth key to automatically authenticate the node as your user account. For a best practice when handling the `--auth-key` value, refer to Securely handle an auth key."
- `--advertise-tags=<tag>` — "Advertise tags that this node will be associated with. You must be listed in TagOwners to be able to do this."
- `--hostname=<name>` — "Set the hostname of the node instead of the one provided by the OS."
- `--operator=<user>` — "Specify a Unix username other than `root` to operate `tailscaled`."
- `--reset` — (flag del CLI `down`/`up` en versiones recientes; usado en scripts comunitarias)
- `--shields-up` — "Block incoming connections from other devices on your Tailscale network."
- `--ssh` — "Run a Tailscale SSH server, permitting access per the tailnet administrator's declared access policy."

**`tailscale logout` (literal):** "When you log out of Tailscale on an **ephemeral node**, the node will be removed from your tailnet immediately."

**`tailscale ssh` (literal):** "When your local node is in userspace-networking mode and can't make a direct connection, use `tailscale ssh`. This sets up an SSH `ProxyCommand` to connect through the local `tailscaled` daemon."

**`tailscale serve` / `funnel`:** `serve` limita al tailnet; `funnel` publica a internet.

---

## BLOQUE 4 — ALTERNATIVAS (FUENTE OFICIAL)

### F29 · Vast.ai — Pricing overview — https://docs.vast.ai/guides/pricing — **200**

> "Vast.ai is a **marketplace, not a fixed-price provider**. Hosts set their own rates and compete for your business, so prices vary with supply, demand, GPU model, location, and host reliability. You pay by the second for compute and continuously for storage."

| Model | Priority | Best for |
|---|---|---|
| On-demand | High | Production, time-sensitive jobs, guaranteed uptime |
| Reserved | High | Long-running projects (up to 50% off by pre-paying) |
| Interruptible | Low (bidded) | Fault-tolerant workloads; often 50%+ cheaper |
| Serverless | Managed | Bursty inference (`min_workers: 0`) |

> "What you're billed for:
> * **GPU compute**, per-second while the instance is in a billable state.
> * **Storage**, continuous while the instance exists, **including when it is stopped**. Delete the instance to stop storage billing.
> * **Bandwidth**, **per byte for both ingress and egress**. Rates are host-set; check before picking data-intensive offers."

**[I]** Vast.ai = mismo modelo de riesgo de privacidad que Community Cloud (marketplace peer-to-peer) + storage cobrada parado + egress por byte. Alternativa de precio, no de privacidad.

---

### F30 · Scaleway — AI solutions — https://www.scaleway.com/en/ai-solutions/ — **200**

> "### Keep sensitive data in Europe
> Scaleway stores all its data in Europe and thus, it is not subject to any extraterritorial legislation, and fully compliant with the principles of the GDPR."

> "### GPU Instances
> ### H100 PCIe GPU Instance — **€2.73/hour** (~€1,993/month)
> ### RENDER GPU — **€1.24/hour** (~€891/month) — Dedicated Tesla P100s
> ### L4 GPU Instance — **€0.75/hour** (~€548/month)
> ### L40S GPU Instance — **€1.4/hour** (~€1,022/month)"

> "Predictable, transparent pricing — Eliminate the CAPEX barrier and the fear of hidden costs with simple, pay-as-you-go billing with **no egress or lock-in**."

> "DC5 (par2) is one of Europe's greenest data centers, with a PUE of 1.16 (vs. the 1.55 industry average)."

---

### F31 · Scaleway — GPU instances — https://www.scaleway.com/en/gpu-instances/ — **citada**

> "Train, fine-tune, and serve your AI models on the market's most powerful GPUs with **guaranteed data residency within Europe**.
>
> Available zones: **Paris: PAR1 PAR2** · **Warsaw: WAW2**
>
> ### True digital sovereignty — Your training datasets, models, and user data are hosted in Europe and completely protected from extraterritorial laws.
> ### Predictable, transparent pricing — ... simple, pay-as-you-go billing with no egress or lock-in."

---

### F32 · Scaleway — Instances FAQ — https://www.scaleway.com/en/docs/instances/faq/ — **200**

> "How are Instances billed?
> * CPU Instances: Billed per hour of uptime (including startup and standby time).
> * **GPU Instances: Billed per minute of uptime** (including startup and standby time), except for RENDER-S GPU Instances, which are billed per hour."

> "**Keep in mind that while compute resources follow this usage-based billing model, other resources—such as public IP addresses and storage volumes—are billed for their entire allocation period, regardless of whether the Instance is powered off.**"

**Power off (literal):**
> "- Hard reboot: ... data is kept on the Local Storage.
> - **Power off**: All local volume data is transferred to a volume store, and your physical node is released back to the pool of available machines.
> - **Terminate**: Your Instance and its volumes are permanently deleted, but the attached flexible IP is preserved.
> - **Standby**: Your Instance is stopped, but its data remains in the Local Storage. The Instance is still allocated to your account and can be restarted anytime.
>
> **Important: The standby mode is charged as a running Instance.** To avoid being billed for an unused Instance, power it off and ensure no IPs or allocated storage are left in use."

**SLO (de la doc de elección de GPU Instance):** "The service level objective (SLO) for all GPU Instance types is **99.5%**."

**[I]** No hay opción "per-second" ni "efímera con expiración automática". El equivalente a "datos que desaparecen" es `Power off` + `Terminate`.

---

### F33 · OVHcloud — Tarif Cloud Public — https://www.ovhcloud.com/fr/public-cloud/prices/ — **citada** (tabla oficial)

**Instances GPU (extracto, Prix HT/heure):**
| Nombre | Mémoire | vCore | GPU | Prix HT/h | Prix HT/mois |
|---|---|---|---|---|---|
| l4-90 | 90 Go | 22 | 1× L4 (24 Go) | **0,75 €** | 540 € |
| a10-45 | 42 Go | 30 | 1× A10 (24 Go) | **0,76 €** | ~554,80 € |
| l40s-90 | 90 Go | 15 | 1× L40S (48 Go) | **1,40 €** | 1 008 € |
| a100-180 | 180 Go | 15 | 1× A100 (80 Go) | **2,75 €** | 1 100 € |
| h100-380 | 380 Go | 30 | 1× H100 (80 Go) | **2,80 €** | 1 940 € |
| rtx5000-28 | 28 Go | 4 | 1× Quadro RTX5000 (16 Go) | 0,36 € | ~262,80 € |

> "Notre datacenter **"France (Gravelines)"** offre la plus grande variété de GPU. Sachez que la région de Paris propose également des GPU dont les H200."

---

### F34 · OVHcloud — AI Notebooks, Facturation et cycle de vie — https://docs.ovhcloud.com/fr/guides/public-cloud/ai-machine-learning/ai-notebooks-billing.md — **200** *(lastUpdated 2026-01-27)*

> "AI Notebooks est lié à un projet Public Cloud. L'ensemble du projet est facturé en fin de mois, en mode paiement à l'usage."

> "**Attention :** Par défaut, votre AI Notebook s'arrête automatiquement après **7 jours consécutifs passés à l'état RUNNING**."

**Inclus (literal):**
> "- Ressources de calcul CPU/GPU dédiées
> - **Stockage local éphémère du notebook** (la taille dépend des ressources de calcul sélectionnées). Les 10 premiers Go sont gratuits.
> - Stockage distant du workspace (optionnel)
> - Trafic réseau entrant/sortant (optionnel)"

**Granularidad (literal):**
> "Les tarifs de calcul sont indiqués par heure pour faciliter la lecture des prix, mais **la granularité de facturation reste à la minute**."

**Storage local éphémère (literal):**
> "Chaque ressource de calcul (CPU ou GPU) est fournie avec du stockage local, que l'on peut considérer comme **éphémère puisque cet espace de stockage n'est pas conservé lorsque vous arrêtez ou supprimez votre notebook**... Ce stockage n'est pas facturé car il est directement lié à la ou les ressources de calcul."

**Workspace (literal):**
> "Par défaut, un conteneur Object Storage distant sera monté sur votre notebook à l'emplacement `/workspace`... Les 10 premiers Go sont gratuits pendant 30 jours consécutifs une fois votre notebook arrêté, puis vous payez au tarif d'OVHcloud Object Storage."

**DELETING (literal):**
> "Une fois supprimé, il n'existera plus. **Ses données internes du dossier `/workspace` ne seront pas supprimées automatiquement** après la suppression du notebook. Si vous êtes sûr(e) de vouloir les supprimer, vous pouvez les retrouver et les supprimer dans le conteneur `notebooks_workspace` de votre Object Storage, sous le répertoire de l'ID du notebook."

**[I]** Ojo: el `/workspace` de OVHcloud **no** se borra con el notebook (hay que borrarlo a mano en Object Storage). Es el mismo patrón de "el volumen sobrevive al pod" que en Runpod → hay que putear el cierre.

---

### F35 · Nebius — AI Cloud pricing — https://nebius.com/prices — **200**

| Item | vCPU | RAM GB | Preemptible GPU-hour | On-demand GPU-hour |
|---|---|---|---|---|
| NVIDIA HGX B300 | 24 | 346 | from $0.99 | $9.50 |
| NVIDIA HGX B200 | 20 | 224 | from $0.99 | $8.50 |
| NVIDIA HGX H200 | 16 | 200 | from $0.79 | $5.40 |
| **NVIDIA HGX H100** | 16 | 200 | **from $0.79** | **$4.50** |
| **NVIDIA RTX PRO 6000** | 24 | 218 | from $0.79 | **$1.80** |
| **NVIDIA L40S (Intel)** | 8-40 | 32-160 | from $0.74 | **from $1.55** |
| NVIDIA L40S (AMD) | 16-192 | 96-1152 | from $0.90 | from $1.82 |

**Storage:** Shared Filesystem $0.0800/GiB/month · WEKA $0.1000/GiB/month · Object Storage Standard $0.0147/GiB/month · Block volumes $0.0530-0.1180/GiB/month.

**Otros (literal):**
> "Networking: Egress/Ingress traffic — **Free**"
> "Networking: Public IP address — **Free**"
> "Managed Service for Kubernetes — **Free**"
> "Managed Soperator (Slurm on Kubernetes) — Free"

> "All prices are shown without any applicable taxes, including VAT." / "There is a minimum payment amount: $25 for the first payment."

**Token Factory (nebius.com/ai-studio):** serverless (evaluación/prototipos) + dedicated endpoints (producción, "regional placement" controlado).

**[I]** No hay SKU de 24 GB de consumo; el on-demand es 3-5× más caro que Runpod Secure para la misma GPU. Egress gratis y K8s/Slurm gratis = advantages reales para cualquier proyecto de training serio.

---

### F36 · Hetzner — GPU server — https://docs.hetzner.com/robot/dedicated-server/server-lines/gpu-server/ — **citada**

> "GEX server types are configured with fixed hardware, varying the number of drives and RAM capacity. You cannot order additional hardware; instead, you must upgrade to a different server model to obtain more drives or RAM."

**Modelos GEX (extracto):**

| Model | GPU | vRAM | RAM | Notas |
|---|---|---|---|---|
| GEX44 | NVIDIA RTX 4000 SFF Ada Gen | 20 GB GDDR6 | 64 GB DDR4 | FSN1 (Falkenstein) |
| GEX45 | | | | |
| GEX63 | | | | |
| GEX130 | NVIDIA RTX PRO 6000 | | hasta 256 GB DDR5 | |
| GEX131 | | | 256/512/768 GB DDR5 ECC | para training |
| GEX430 | | | | 8× RTX |

**GEX44 (página oficial de producto):** "i5-13500 · 64 GB DDR4 · 2× 1.92 TB NVMe (Gen3) · 1 GBit/s · Traffic: **Unlimited** · Available location: **FSN 1**" · "20 GB GDDR6 ECC Grafikspeicher" · "306,8 TFLOPS".

### F37 · Hetzner — Price Adjustment 15 June 2026 — https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/ — **citada** *(Last change 2026-07-08)*

> "Falkenstein: | Servertype | Monthly price excl. IPv4 in € | Setup fee in € | ... | **GEX44-1 | 232.30 | 114.00** |"

> "Nuremberg and Helsinki: ... GEX131-1 1,197.30 / 599.00 · GEX131-2 1,797.30 / 899.00 · GEX131-3 2,297.30 / 1,149.00"

> "The price adjustment took effect for new orders and cloud instance rescales starting on the 15 June 2026; 8 AM CEST."

**[I]** GEX44 ≈ €232,30/mes + €114 de alta = ~€0,29/h equivalente. Con 20 GB VRAM. Para el flujo del estudio (FLUX.2 klein 9B fp8 ≈ 9 GB de pesos + TE 8,7 GB) **no alcanza**: el TE no entra en 20 GB junto a los pesos. Es una máquina de inferencia ligera, no de training ni de FLUX.2 9B.

---

## BLOQUE 5 — COMUNITARIAS (NO OFICIALES)

### F39 · koshimazaki/tailscale-runpod — https://github.com/koshimazaki/tailscale-runpod — **citada** *(2026-01-30)*

> ```bash
> curl -fsSL https://tailscale.com/install.sh | bash && /usr/sbin/tailscaled --tun=userspace-networking --state=/workspace/tailscale.state & sleep 5 && tailscale up --ssh
> ```
> "**No exposed ports to the public internet**" · "Persistent Tailscale IP across pod restarts" · "**Most cloud GPU containers don't have Tailscale in their default apt repos, so the official install script is required.**"

> "### Why This Skill? Standard Tailscale docs don't cover the container-specific requirements for cloud GPU platforms. This skill includes the gotchas we discovered:
> 1. Must use `--tun=userspace-networking` (no kernel TUN in containers)
> 2. Must use `--ssh` flag (enables Tailscale's built-in SSH server for container environments)
> 3. Must persist state to `/workspace/` to survive restarts
> 4. **Browser auth required — authkey doesn't work reliably in unprivileged containers**"

**[I]** El punto 4 contradice la recomendación oficial de Tailscale («We recommend using it with ephemeral nodes and auth keys»). Es una fuente no oficial: **probar antes de depender**.

### F40 · RyderJ/lessemf-pod — tailscale_setup.sh — https://huggingface.co/RyderJ/lessemf-pod/blob/main/tailscale_setup.sh — **citada**

> ```bash
> if [ -e /dev/net/tun ]; then
>   tailscaled --state=/tmp/tailscaled.state >> "$LOG" 2>&1 &
> else
>   tailscaled --state=/tmp/tailscaled.state --tun=userspace-networking --socks5-server=localhost:1055 >> "$LOG" 2>&1 &
> fi
> tailscale up --reset --authkey="$TAILSCALE_AUTH_KEY" --hostname="$HOSTNAME" --ssh >> "$LOG" 2>&1
> ```
> "Requires TAILSCALE_AUTH_KEY set in RunPod environment variables. **Use a tagged auth key (tag:runpod) for ACL-controlled SSH access.**"

### F41 · snghrsw — runpod start script (gist) — https://gist.github.com/snghrsw/5e671a4db380ca0a1e57178f72b475ea — **citada**

> `tailscaled --tun=userspace-networking &` → `tailscale up --ssh --hostname=comfy-runpod --authkey=${TAILSCALE_AUTHKEY} --accept-routes`
> + ComfyUI + Syncthing (`--no-browser -gui-address=127.0.0.1:8384`) + aria2 para descarga de modelos.

**[I]** Patrón de producción real: Tailscale en userspace + ComfyUI + Syncthing (para bajar resultados al estudio sin salir por el proxy HTTP).

### F42 · Kretzschmar — Tailscale + Docker — https://tailscale.com/blog/docker-tailscale-guide — **citada** *(2024-02-07)*

> "To use an auth key we need to generate one using the admin console... `Expiration: 7 days` · `Ephemeral: ...`"

**[I]** Confirma que las auth keys pueden ser **efímeras** y con expiración corta → el modelo correcto para un pod descartable.

---

## BLOQUE 6 — DESCARTES

| URL | Estado | Motivo |
|---|---|---|
| https://docs.runpod.io/pods/overview/secure-cloud | **404** | La página de Secure Cloud no existe en esa ruta (contenido equivalente en `/pods/overview#pod-types`) |
| https://api.runpod.io/v2/catalog/datacenters | **401** | Requiere `Authorization: Bearer` → sin inventario vivo de DCs ni matriz compliance por DC |
| https://www.scaleway.com/en/gpu-instances/pricing/ | **404** | Usar `/en/pricing/gpu/` (>5 MB, no descargable) → se usó `/en/ai-solutions/` |
| https://docs.nebius.com/compute/regions/ | **404** | No existe esa ruta |
| https://tailscale.com/kb/1080/docker | **200** (redirect → CLI reference) | La URL canónica de Docker no resolvió al artículo esperado |
| gpufinder.dev · gpuperhour.com · spheron.network/blog · serversearcher.com · nasdaq.com/press-release | 200 | **Comparadores comerciales, no fuente oficial.** Sus cifras NO se usaron; todos los precios de §6 del informe salen de páginas de precio del propio proveedor. |

---

## Notas de método

- **Herramienta de lectura:** `webfetch` (markdown/text) sobre URLs oficiales. Las páginas `.md` de `docs.runpod.io` devuelven markdown limpio (Mintlify) y son la fuente primaria de la documentación técnica.
- **Índice maestro:** `https://docs.runpod.io/llms.txt` (200) usado para (a) descubrir rutas y (b) como **prueba negativa** sobre Tailscale.
- **Búsquedas negativas documentadas:** barrido literal de Privacy Policy, ToS y DPA por `train | machine learning | artificial intelligence | aggregated and anonymized | improve our models` (sólo copies de marketing) y por `Confidential | Retention | SLA | uptime | Governing Law | Supplement`.
- **Sin verificación empírica:** no se desplegó ningún pod. Todos los comportamientos de red y de ciclo de vida son **documentados**, no observados.
- **Idioma:** todo el material de Runpod/Tailscale/Scaleway/Nebius/Hetzner/Vast.ai es en inglés (Scaleway/Hetzner/OVHcloud tienen versión francesa/americana). No hay material en italiano: gap declarado, sin impacto.
