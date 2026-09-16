---
tipo: metodologia
fecha_creacion: 2026-08-27
ultima_actualizacion: 2026-08-27
tags: [studio-os, plan, cuestionario, emilia-pimenta]
estado: en-progreso
---

# Cuestionario — Plan Studio OS (Emilia Pimenta)

> Respondé directamente en este archivo, debajo de cada pregunta (reemplazá `> _Tu respuesta aquí_`). Podés responder de a una y yo voy ajustando el plan en vivo. Si no sabés algo, poné `NS/NC` o `hipótesis: ...`.

Fuente: [[proyectos/STUDIO_OS-Emilia/presentacion/00-presentacion-studio-os|Deck 16 slides]] + [[Resumen_Propuesta_Emilia_Studio_OS(1).txt|Resumen conceptual]]

**Cómo usar:** Editá este `.md` en Obsidian/VS Code. Cada vez que guardes, avisame y actualizo el plan.

---

## A. Alcance del plan

### A1. ¿Este plan es solo para Emilia o es tu producto replicable (PI Studio OS) con Emilia como piloto?
> **Respuesta (2026-08-27): Ambos — base replicable + capa personalizada Emilia (piloto)**

### A2. ¿Cuál es el éxito mínimo del sprint de 30 días (USD 600) para vos? (ej: mapa validado + prototipo funcionando + roadmap firmado)
> **Respuesta (2026-08-27): Venta Fase 2 — el sprint debe convertir a implementación paga (mapa+prototipo son medios, no fin)**

### A3. ¿La reunión con Emilia vende solo el sprint o ya incluye estimado de Fase 2? ¿Hay techo presupuestario para Fase 2/3?
> **Respuesta (2026-08-27): Solo sprint (USD 600) — Fase 2 se presupuesta post-roadmap**

---

## B. El estudio hoy (organizacional)

### B4. Tamaño y roles de Emilia hoy (titular, juniors, externos, admin). ¿Remoto/presencial? ¿Cuántos proyectos simultáneos y en qué fases?
> **Respuesta (2026-08-27): Estudio chico 2-4 (titular + 1-2 juniors, pocos proyectos simultáneos)**

### B5. ¿Quién decide qué? (¿Emilia decide todo o hay project leads con autonomía? Referencia: `wiki/estudio/escala-decisiones`)
> **Respuesta (2026-08-27): Delega parcial — juniors con autonomía en tareas definidas, Emilia valida decisiones arquitectónicas**

### B6. ¿Cómo es la comunicación interna y con obra hoy? (WhatsApp, Drive, papel, libro de obra físico). ¿Dónde se pierde más tiempo?
> **Respuesta (2026-08-27): Mixto desordenado — un poco de todo sin sistema (chats + Drive + papel)**

---

## C. Flujos de diseño y documentación

### C7. ¿Cómo diseña Emilia? Ordená por frecuencia: croquis mano, referencias/moodboard, CAD, BIM (Revit/ArchiCAD), Rhino/Grasshopper. ¿Qué no quiere cambiar?
> **Respuesta (2026-08-27): NS/NC — a relevar en sprint (hipótesis: croquis+referencias primero, no imponer software)**

### C8. ¿Qué entregables duelen más? (planos legales Ley 24.335, detalles in situ, memorias, renders concurso/cliente)
> **Respuesta (2026-08-27): Todos por igual — sobrecarga general (hipótesis: priorizar representación para prototipo rápido)**

### C9. Flujo de representación actual: `Emilia → junior → modelado → render → corrección`. ¿Cuántas iteraciones y cuánto tarda un render hoy?
> **Respuesta (2026-08-27): Dolor principal = errores, problemas de comunicación, retrabajos (no tiempo puro sino pérdida de intención/traducciones)**

---

## D. Infraestructura y software

### D10. GPUs 24GB subutilizadas (`Resumen:74`): ¿cuántas, modelo, dónde están, pueden quedar 24/7 para ComfyUI local?
> **Respuesta (2026-08-27): Requiere túnel para IA local en el estudio + alternativa RunPod. Mandato: proteger PI, solo modelos con licencia comercial permisiva (OpenRAIL etc.), sin entrenamiento con datos del estudio → IA local prioritaria.**

### D11. Stack actual licenciado: AutoCAD, Revit, Rhino, Office, Drive/Dropbox, Notion/Obsidian, CRM. ¿Vault ya existe o desde cero?
> **Respuesta (2026-08-27): AutoCAD + Lumion + Dropbox + WhatsApp. Sin vault, sin cerebro, documentación desordenada. Desde cero.**

### D12. ¿CDE hoy? ¿Dónde viven los binarios? (`activos/proyectos/` vs `C:\BIM\` vs Drive). ¿Backups y versionado de planos?
> **Respuesta (2026-08-27): CDE propuesto = Google Drive (ya es apéndice del estudio) + vault que indexa. Binarios siguen en Drive. ComfyUI en paralelo a Lumion (no reemplazo). Modelado 3D hoy básico para impresora 3D, evolución propuesta → Rhino (no Revit aún).**

### D13. ¿Restricción de nube? ¿Exige 100% local (planos no salen) o acepta cloud para lo no sensible? (ver `wiki/estudio/decision-arquitectura-ia-privacidad`)
> **Respuesta (2026-08-27): Duda sobre RunPod: ¿afecta confidencialidad de renders? Entendía que datos no se guardan pero hay que proteger PI. Aclarar política de retención/entrenamiento de RunPod vs local puro. Mandato: PI protegida siempre.**

---

## E. Representación / ComfyUI

### E14. ¿Qué visualizaciones necesitan más? (anteproyecto, concurso, interiores, urbano). ¿Tenés 3-5 croquis de Emilia para prototipo?
> **Respuesta (2026-08-27): NS/NC — sin croquis aún, se consiguen en sprint**

### E15. ¿Telegram es su interfaz diaria o usan WhatsApp? ¿Aceptan bot de Telegram o debe ser WhatsApp? (`Resumen:65`)
> **Respuesta (2026-08-27): Propuesta: Discord (no Telegram/WhatsApp) — evaluar como interfaz para ComfyUI + obra**

### E16. ¿Priorizamos SD1.5 rápido (ArchitectureRealmix) o calidad SDXL (Juggernaut XL) si tienen 24GB de sobra?
> **Respuesta (2026-08-27): Ambos — SD1.5 para iteración rápida, SDXL (Juggernaut XL) para final (24GB lo permite)**

---

## F. Clientes, administración, honorarios

### F17. ¿Cómo entra trabajo hoy? (web, IG, referidos, licitaciones). ¿Tienen CRM o todo en cabeza/Excel/WhatsApp?
> **Respuesta (2026-08-27): Referidos + WhatsApp, sin CRM formal**

### F18. ¿Cómo calculan honorarios? ¿Usan CPAU / `MVP_03-calculadora-honorarios`? ¿Presupuestos/contratos dónde están?
> **Respuesta (2026-08-27): Manual / Excel, sin MVP_03 aún**

### F19. ¿Fricción mayor en admin: presupuestos, seguimiento de pagos, o retrabajo?
> **Respuesta (2026-08-27): Todo — administración desbordada**

---

## G. Obra y proveedores

### G20. ¿Libro de obra hoy 100% papel? ¿Fotos con celular se suben o se pierden? ¿Cuántas obras simultáneas?
> **Respuesta (2026-08-27): Nada formal — sin libro de obra, fotos sueltas**

### G21. ¿Querés flujo Foto → Telegram → `vault/activos/proyectos/<obra>/fotos/` con fecha/ubicación/incidencia automática? (`Resumen:102`)
> **Respuesta (2026-08-27): Sí, pero después — primero representación, libro digital en Fase 2 posterior**

### G22. ¿Base de proveedores existe? ¿Formato?
> **Respuesta (2026-08-27): No existe — en cabeza/WhatsApp, sin base estructurada**

---

## H. Memoria / grafo de conocimiento

### H23. ¿El ejemplo "proyectos con hormigón visto y proveedores" (`Resumen:99`) es real? Dame 2-3 consultas que hoy tardan horas.
> **Respuesta (2026-08-27): NS/NC — a validar en relevamiento con 2-3 consultas reales**

### H24. ¿Qué conocimiento quieren reutilizar? (detalles, cómputos, lecciones aprendidas, referentes). ¿Vault en Obsidian les cierra?
> **Respuesta (2026-08-27): Obsidian/vault — quieren memoria estructurada**

---

## I. Restricciones y NFRs

### I25. ¿Presupuesto mensual tolerable post-sprint para hosting/automatización (n8n, VPS, embeddings)? ¿Self-hosted o SaaS?
> **Respuesta (2026-08-27): NS/NC — roadmap lo define (hipótesis: mínimo, priorizar local+Drive)**

### I26. ¿Nivel de adopción tolerable? (1-2 cambios/mes o todo ya). ¿Quién sería el champion interno?
> **Respuesta (2026-08-27): Moderado 2-3 cambios/mes — ritmo iterativo (champion a definir, hipótesis Emilia + 1 junior)**

### I27. ¿Seguridad/compliance innegociable? (planos legales no salen del país, PI de concursos, firma digital)
> **Respuesta (2026-08-27): PI 100% protegida — nada se entrena, solo modelos con licencia comercial permisiva (OpenRAIL etc.)**

---

## J. Presentación misma

### J28. ¿Reunión remota o presencial? ¿Cuánto tiempo (15/30/45 min)? ¿Demo en vivo o solo slides?
> **Respuesta (2026-08-27): No definido — a coordinar**

### J29. ¿Qué objeción anticipás más fuerte? (precio, tiempo, "no somos técnicos", "ya probamos IA")
> **Respuesta (2026-08-27): "No somos técnicos" — miedo a complejidad técnica**

### J30. ¿Deck como template replicable para otros estudios o 100% personalizado a Emilia?
> **Respuesta (2026-08-27): Ambos — base replicable + capa Emilia (consistente con A1)**

---

## Notas libres

> _Agregá acá cualquier contexto que no entró arriba_

---

## Progreso

- [ ] A. Alcance (A1-A3)
- [ ] B. Estudio hoy (B4-B6)
- [ ] C. Flujos diseño (C7-C9)
- [ ] D. Infra (D10-D13)
- [ ] E. ComfyUI (E14-E16)
- [ ] F. Clientes/admin (F17-F19)
- [ ] G. Obra/proveedores (G20-G22)
- [ ] H. Memoria (H23-H24)
- [ ] I. NFRs (I25-I27)
- [ ] J. Presentación (J28-J30)

> Cuando completes un bloque, avísame y genero el plan en `04-plan-studio-os.md`.
