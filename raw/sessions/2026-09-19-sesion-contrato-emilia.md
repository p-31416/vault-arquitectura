---
tipo: log
fecha: 2026-09-19
proyecto: STUDIO_OS-Emilia
participantes: [Sol, Emilia Pimenta]
tags: [sesion, contrato, legal, studio-os, pdf, chrome, weasyprint, vault]
---

# Sesión 2026-09-19 — Contrato Studio OS × Emilia — revisión punto por punto para envío lunes 21/09

## Qué se hizo

Revisión completa del contrato para envío a Emilia (abogada) el lunes 21/09, punto por punto en terminal, con generación de PDF fiel desde el .md.

**6 puntos acordados y aplicados:**
1. **190h trimestrales totales ~16h/sem promedio** — eliminado “3h/día” de todo el pack (`por día|3h/día` = 0 hits). Distribución 25/50/25. 3hs semanales ahora aclaradas como reuniones semanales (1 semanal + presencial cada 15 días, ver TERCERA).
2. **Tipo de cambio:** promedio Oficial BNA vendedor + MEP vendedor vía El Cronista del día de facturación (fecha 16), fallback Ámbito/BNA — factura fecha 16 vence 23 (1 semana margen).
3. **Mora 5% mensual + suspensión** alineado en detallado, wiki y finanzas.
4. **Terminación:** 20 días aviso + penalización **30%** sobre saldo pendiente (ajustado de 40%→30% a pedido) + prorrateo hitos/horas.
5. **PI y Datos:** tratamiento por cuenta y orden Ley 25.326 + derechos de uso con listas SÍ/NO anonimizable detalladas. Frase “El Programa queda habilitado...” movida antes de las listas. Sin “resumen breve”.
6. **Fechas:** firma lunes 21/09/2026, vigencia 21/09–21/12/2026, trabajo anticipado mié 16/09 reconocido, pagos mensuales día 16→23 (Mes 0/300 16/09→23/09, Mes1/600 16/10→23/10, Mes2/600 16/11→23/11, Mes3/300 16/12→23/12). Factura C a CUIT RI facilitado por Clienta.

**Formato y PDF:**
- Eliminado “Plantilla” y “AVISO LEGAL” del encabezado — ahora solo `CONTRATO DE PRESTACIÓN DE SERVICIOS — Studio OS — Programa I+D` y header `PITAUTECH / Arq. M. Sol Azcona` (sutil 7pt) + `Studio OS — Programa I+D`.
- Todas las cláusulas con franja gris #f2f2f2 + borde negro 3px (PRIMERA a NOVENA).
- ANEXO I movido al final en hoja separada con page-break, tabla S1-S4 + infraestructura + hitos W01-W04 + OKRs con glosario W=semana. Título sin paréntesis.
- Párrafo cotización dólar en 8pt italic cursiva; Datos para transferencia resaltados en recuadro gris con borde negro.
- Compacto legible: @page 14/15mm, font 9.5pt/1.32 → 5 páginas (de 7).
- NOVENA: Autorización para case study con 4 compromisos y 5 días aprobación.
- Horas adicionales: ±10% se absorben (18hs vs 16hs), superiores se reportan.
- PDF fiel generado vía `scripts/md_a_pdf_contrato.py` (markdown → HTML + CSS paged media → Chrome headless --print-to-pdf) y `scripts/muestra_contrato_chrome.py`. WeasyPrint descartado por falta de GTK libgobject-2.0-0.

## Archivos modificados

- `proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia.md` — 180 líneas, 8 cláusulas + NOVENA + Anexo I al final, umbral ±10%, Factura C, PI listas, firma 21/09
- `proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia.pdf` — 208.830 bytes, 5 páginas, 19/09 20:xx, Chrome headless
- `wiki/legal/contrato-servicios-studio-os.md` — alineado 190h/16h/W01-W04/16→23/5%/30%/20d
- `wiki/finanzas/terminos-facturacion.md` — alineado 16→23, Oficial+MEP, 5%
- `scripts/md_a_pdf_contrato.py` — CSS compacto 14mm/9.5pt + header PITAUTECH/Arq. M. Sol Azcona, footer sin plantilla
- `scripts/muestra_contrato_chrome.py` + `scripts/muestra_contrato_reportlab.py` — muestras Chrome 115KB vs ReportLab 5KB
- `temp/muestras-pdf/contrato-muestra.html` + `temp/muestras-pdf/contrato-studio-os-emilia.tmp.html` — temporales

## Pendiente para lunes 21/09

- [ ] Completar datos bancarios y CUITs/domicilios/mails Prestadora en CUARTA y encabezamiento
- [ ] Revisión final con Emilia (abogada) — pulido redacción si hace falta para bajar a 4 páginas
- [ ] Copiar PDF final a `/activos/documentos-legales/STUDIO_OS-Emilia/` y subir a Drive piloto S1

## Análisis cerebro-digital

**Topics:** contrato prestación servicios I+D, facturación mensual 16→23, tipo cambio Oficial+MEP, mora 5%, terminación 30%, propiedad intelectual anonimizable, case study, Anexo I Mes 1 OBSERVAR, infraestructura VPS/n8n/Leantime/Bóveda, W01-W04, OKRs

**Entidades:** Emilia Pimenta (arq.emiliapimentalombardi@gmail.com, RI), María Sol Azcona / Pitau-Tech (Arq. M. Sol Azcona), Nayara Alvares Campos (Brasil), MAGENTTA vinícola, PITAUTECH

**Hechos:**
- Firma lunes 21/09/2026, vigencia 21/09–21/12/2026, inicio anticipado mié 16/09
- 190h trimestrales ~16h/sem, 3hs semanales reuniones (1 semanal + presencial cada 15)
- Pagos: 300 16/09→23/09, 600 16/10→23/10, 600 16/11→23/11, 300 16/12→23/12
- Tipo cambio día 16 vía El Cronista, fallback Ámbito/BNA
- Mora 5% mensual + suspensión, terminación 20 días + 30% saldo
- Anexo I S1-S4 ~16hs c/u, W01 día5, W02 día10, W03 día15, W04 día20, OKRs ≥12hs/mes
- PDF actual 5 páginas, 208.830 bytes, Chrome headless
