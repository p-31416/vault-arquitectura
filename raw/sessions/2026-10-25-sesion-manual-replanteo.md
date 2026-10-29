# Sesión 2026-10-25 — Manual de replanteo y cómputo (ítems 1–10)

## Qué se hizo
- Revisión del pedido: mapear el proceso completo de dibujo de un plano de replanteo (de arquitectura a cómputo) y publicar la información en el vault.
- Análisis read-only de `REP-ARAOZ.dwg` vía conversión ODA a DXF en temp: 1.987 entidades, 60 capas, 201 INSERT, 258 cotas, 98 tags `SIMB-MURO`, 41 carpinterías, 21 columnas, 29 locales (00–28).
- Lectura de correcciones manuscritas del 29/09 (`correcciones/0929-Emi-*.pdf` + JPG Sol): renumerar locales, eliminar pared marcada, ventanas faltantes en balcones, símbolo en capa equivocada, consulta de revestimientos a Sra. Froda.
- Definiciones aportadas por el usuario: H1/H2 = herrería de barandas exteriores; B1–B3 = barandas interiores de escalera de incendio; T = tabiques estructurales de hormigón; M7/M8 = muros con revestimiento cerámico (una o dos caras, caso cocina-cocina).
- Revisión ítem por ítem del manual (10 ítems), sin escribir archivos del vault ni ejecutar entregables. Ítems 1–10 aprobados en borrador conversacional.
- Decisión: ítem 8 (automatizaciones LISP/Python) queda en backlog registrado, no se ejecuta ahora.

## Archivos modificados
- Ninguno dentro del repo. Solo temporales fuera del vault (`C:\Users\Solch16\AppData\Local\Temp\opencode\`: DXF convertido, PNG de correcciones, OCR, áreas).

## Cerebro-digital
- Topics: replanteo, cómputo de obra, bloques dinámicos, planillas, taxonomía de muros, herrería, AutoCAD LT.
- Entidades: REP-ARAOZ (plano REP.-02, planta tipo 2–7, obra Araoz 865), Emilia Pimenta (autora), Sra. Froda (revestimientos), SET_01-REP, M1–M8 / T / H / B.
- Hechos: el detalle define M1–M8 pero 21 tags T/H/B estaban sin definición (ahora definidos verbalmente); muros dibujados con caras sueltas, no computables automáticamente; planillas embebidas como OLE (5 OLE2FRAME en ROT-TXT); A-CIELO cubre solo núcleos húmedos (62,65 m² únicos); LT 2027 sin COM/DATAEXTRACTION, con AutoLISP.
- Pendiente: redactar `docs/manual-replanteo-computo.md` + páginas wiki (`tecnico/replanteo.md`, `tecnico/computos.md`, actualización de bloques/capas/nomenclatura/índice). Requiere `s` explícita.
