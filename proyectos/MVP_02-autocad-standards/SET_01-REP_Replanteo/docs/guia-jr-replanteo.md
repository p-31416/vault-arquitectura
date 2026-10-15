---
tipo: metodologia
mvp: 02
set: SET_01-REP
version: 1.0-jr
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, replanteo, autocad, guia, junior, dibujo]
audiencia: dibujante-junior
---

# Guía JR — El plano de replanteo (qué es, cómo leerlo, cómo dibujarlo)

> Para quien maneja lo básico de AutoCAD (`LINEA`, `DESFASE`, `INSERTAR`,
> `COTA`, `TEXTO`) y va a dibujar su primer plano de replanteo con nuestro
> SET. Documento técnico del SET: `SET_01-REP_completo.md`.

## 1. Qué es, en una frase

El replanteo es **pasar las medidas del proyecto al terreno en escala 1:1**:
lo que en el plano está en 1:50, en obra se marca en tamaño real con hilos,
caballetes y cinta. El plano de replanteo es el documento que el capataz lleva
a la obra para saber **dónde va cada cosa** ([grupotrato](https://grupotrato.com/blog/que-debe-tener-un-plano-de-replanteo/),
[FADU](https://tallerac1.wordpress.com/fichas-de-catedra/replanteo-de-la-obra/)).

## 2. Qué contiene (contenidos mínimos)

Todo plano de replanteo, en cualquier estudio, trae lo mismo
([UNAM-FIO](https://aulavirtual.fio.unam.edu.ar/pluginfile.php/323422/mod_resource/content/1/REPLANTEO.pdf)):

| Elemento | Qué es | En nuestro SET |
|---|---|---|
| Ejes de replanteo | 2+ líneas perpendiculares, origen de todas las medidas; van en espacios libres, nunca sobre muros ni huecos de escalera ([FADU](https://eva.fadu.edu.uy/pluginfile.php/3775/mod_resource/content/4/MATERIAL_DE_CONSULTA/MANUAL%20DIDACTICO%20EL%20REPLANTEO-Brunasso.pdf)) | Capa `REP-EJES`, bloque `SIMBOLO DE EJE` |
| Cotas parciales | Medida de cada tramo (de eje a filo de muro, de vano a vano) | `REP-COTAS`, estilo `REPLANTEO 150` |
| Cotas acumuladas | Suma corrida desde el origen; sirve para verificar que las parciales cierran | Mismo estilo, segunda cadena |
| Ejes de vanos | Centro de cada puerta/ventana, acotado a los ejes | Capa `A-CARP-02` |
| Espesores | Ancho de cada muro/tabique/columna, escrito una sola vez | Tags `SIMB-MURO` |
| Niveles | Altura de cada piso respecto al ±0.00 (piso terminado, NPT) | `SIMBOLO NIVEL PISO CORTE` |
| Locales | Nombre de cada ambiente | `ROT-TXT` |

Escala por convención: **1:50**. Modelo siempre en **metros**.

## 3. Cómo LEERLO (antes de dibujar)

1. **Rótulo primero**: nombre del plano, escala, fecha y revisión. Si la
   revisión es vieja, ese plano no se usa ([ingenieriareal](https://ingenieriareal.com/leer-planos-de-casas/)).
2. **Ejes**: ubica los 2 ejes principales (línea y punto, color 81). Todo se
   mide desde ellos.
3. **Cotas escritas mandan**: si una cota dice 2.30, vale 2.30 aunque con la
   regla midas otra cosa (la impresión miente; la cota no).
4. **Parcial + acumulada**: suma las parciales de una cadena y compara con la
   acumulada. Si no cierran, avisa: es un error del plano, no tuyo.
5. **Vanos**: cada abertura tiene su centro acotado y su código (`V01`, `P-1`);
   el código se busca en el cuadro de carpinterías, no se adivina.
6. **Niveles**: verifica el ±0.00 y cada NPT antes de acotar alturas.

## 4. Cómo DIBUJARLO (12 pasos, solo comandos básicos)

Plantilla: `NUEVO` desde `SET_01-REP.dwt` (capas, estilos y cotas ya vienen).

1. Terreno: `LINEA` en `A-TERRENO` (está congelada de referencia; no la muevas).
2. Ejes: `LINEA` en `REP-EJES` + `INSERTAR` → `SIMBOLO DE EJE` en los extremos.
3. Muros: `DESFASE` desde ejes según espesor, capa `A-MURO-MAMP` (medianeros:
   `A-MURO-MED`, bloqueada: avisa antes de tocarla).
4. Columnas/tabiques: `RECTANG` en `E-COL` / `E-TAB`.
5. Vanos: `INSERTAR` → `VENTANA BAJA SIMPLE` o `PUERTA BATIENTE` **al centro
   del vano**, capa `A-CARP-02`. Ajusta largo/ancho con sus pinzamientos
   azules (son bloques dinámicos: no los explotes).
6. Atributos: completa `TIPO` y `ANCHO` al insertar (`V01`, `2.30`).
7. Tags: `INSERTAR` → `SIMB-MURO` sobre cada muro, `SIMBOLO NIVEL PISO CORTE`
   en cada local. Siempre horizontales.
8. Cotas: `COTA` lineal con estilo `REPLANTEO 150` (parciales) y segunda
   cadena (acumuladas) en `REP-COTAS`. Las cotas van **por fuera** de los
   locales ([FADU](https://eva.fadu.edu.uy/pluginfile.php/3775/mod_resource/content/4/MATERIAL_DE_CONSULTA/MANUAL%20DIDACTICO%20EL%20REPLANTEO-Brunasso.pdf)).
9. Textos: `TEXTO` con estilo `cotas-50` para nombres de locales.
10. Sincroniza: `SINCRATR` (ES) / `ATTSYNC` (EN) + `REGENERAR` si un atributo
    no se ve.
11. Verifica: `VERIFICANORMAS` contra `SET-REP.dws`; corrige lo que marque.
12. PDF: layout `REP-PTipo-A1`, `DWG To PDF.pc3`, viewport 1:50 bloqueado.

## 5. Reglas madre (memorizar)

- **No explotar bloques**: se pierden atributos, dinámicos y cómputos.
- **No medir del plano**: se leen las cotas escritas.
- **Capa bloqueada = pedir permiso**: `REP-EJES`, `A-MURO-MED`, `E-COL-EJES`
  no se tocan sin avisar.
- **Cota que no cierra = avisar**, no "arreglarla" en silencio.
- **Todo vano tiene código**; si falta, se consulta, no se inventa.

## 6. Glosario mínimo

- **Eje de replanteo**: línea de referencia inamovible de la obra.
- **Cota parcial / acumulada**: medida del tramo / suma desde el origen.
- **Vano**: abertura en el muro (puerta o ventana).
- **Mocheta**: canto lateral del vano.
- **Filo**: cara del muro (interior o exterior); el plano aclara cuál se acota.
- **NPT**: nivel de piso terminado. **±0.00**: cero altimétrico de la obra.
- **Medianero**: muro sobre el eje divisorio con el vecino.
- **Wipeout**: máscara del bloque que "limpia" el muro detrás del vano.

## 7. Referencias

- Manual didáctico El Replanteo, FADU-Udelar: <https://eva.fadu.edu.uy/pluginfile.php/3775/mod_resource/content/4/MATERIAL_DE_CONSULTA/MANUAL%20DIDACTICO%20EL%20REPLANTEO-Brunasso.pdf>
- Replanteo de la obra, Taller AC1 FADU-UBA: <https://tallerac1.wordpress.com/fichas-de-catedra/replanteo-de-la-obra/>
- TP-7 Replanteo, UNLP: <https://blogs.ead.unlp.edu.ar/produccion/files/2016/09/TP-7-Replanteo-2023.pdf>
- Qué debe tener un plano de replanteo: <https://grupotrato.com/blog/que-debe-tener-un-plano-de-replanteo/>
