---
tipo: metodologia
mvp: 02
set: SET_01-REP
version: 2.2-archivo
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, replanteo, autocad, playbook, instructivo, emilia]
estado: unico-para-presentar
---

# SET_01-REP — Plano de Replanteo (documento único)

> Puerta de entrada única al SET de replanteo: qué es, qué incluye el kit,
> cómo instalarlo en otra PC y cómo dibujar el plano de principio a fin.
> Detalle medido: `docs/REP-ARAOZ-capas-bloques.md` · Bloques:
> `docs/bloques-personalizados.md` · Cómputos: `docs/cuadro-carpinterias.md` +
> `cuadro-carpinterias.csv` · Horas y ahorro:
> `docs/desglose-configuraciones.md` · Spec técnico: `01-spec-SET_01.md`.

## 1. Qué es

El plano de replanteo fija el **sistema de referencia** desde el cual se mide
toda la obra: ejes, cotas parciales/acumuladas, vanos, niveles y columnas.
Escala 1:50, modelo en metros (`INSUNITS 6`). Base medida:
`REP-ARAOZ.dwg` (49 capas, 13 bloques, 304 cotas, 208 inserts).

## 2. Capas (29 propias + 20 xref)

| Capa | ACI | Línea | Estado | Uso |
|---|---|---|---|---|
| `REP-EJES` | 81 | DASHDOTX2 | bloq | Ejes de replanteo |
| `REP-COTAS` | 41 | — | — | Cotas de replanteo |
| `A-COTA-1-50` | 250 | — | — | Cotas 1:50 |
| `A-EJES` / `A-EJES-VACIOS` | 90 / 113 | DASHDOT | bloq | Ejes arq / vacíos |
| `E-EJES` / `E-COL-EJES` / `IE-EJEX` | 10 / 254 / 32 | —/—/DASHDOT | cong/bloq | Ejes est / columnas / IE |
| `A-MURO-MAMP` / `A-MURO-MED` | 24 / 11 | — | —/bloq | Mampostería / medianeros |
| `E-COL` / `E-COL-H` / `E-TAB` / `E-TAB-H` | 5 / 251 / 166 / 251 | — | —/bloq/—/bloq | Columnas / tabiques |
| `A-TERRENO` | 163 | — | cong | Terreno referencia |
| `A-CARP-02` | 251 | — | — | Vanos dinámicos |
| `SIMB-CARP` / `AR-CUADRO DE VANO` | 33 / 1 | — | — | Atributos carpintería |
| `SIMB-MURO` / `A-SIMBOLO-NPT-PLANTA` | 251 / 251 | — | — | Tags muro / NPT |
| `A-EQUIP-` / `A-SOLADOS` / `CONDUCTOS` | 8 / 250 / 3 | — | — | Fondo |
| `0` / `0-REF` / `Defpoints` | 7 | — | —/cong+bloq/— | Base / xref / nodos |
| `ROT-HOJA` / `ROT-TXT` / `ROT-VP` | 5 / 174 / 130 | — | paper | Rótulo y viewports |

Xref `ARQ-ARAOZ|*` (20): fondo del base; congeladas hoy `A-TERRENO`,
`HATCHMUROS`, `NUMLOC`, `PROYECCIONES`, `REP-EJES`, `TEXTO`.

## 3. Bloques (13)

- Dinámicos con `WIPEOUT` (limpia el muro, evita gruesos): `VENTANA BAJA
  SIMPLE` (20 ej., `TIPO/ANCHO`) y `PUERTA BATIENTE` (22 ej., 5 atributos).
- Tags: `SIMB-MURO` (89), `SIMBOLO DE EJE` (20), `SIMBOLO NIVEL PISO CORTE`
  (29), `C40.20` (26), tabla `Tabela_Esquadrias`, carátula con `CAMPO` de escala.
- **Regla madre: no se explotan** (se pierden atributos, dinámicos y cómputos).
- Tag siempre horizontal: rotación excluye al atributo (§15 doc madre).

## 4. Estilos

- Cotas: `COTAS-ARQ-50` ×152 (tick `_ArchTick`) + `REPLANTEO 150` ×152
  (punta `_Open90`). Destino: `EP-ARQ`.
- Textos (9): `cotas-50` (0.16), `COTAS`, `style2`, `Standard`, `MBA25`,
  `ROMANS`, `ROT` (rótulo, mm). Destino: `EP-2.5/EP-3.5`.
- Comandos ES/EN + atajos: tabla §14 del doc madre (regla `_COMANDO`).

## 5. Kit instalable (qué hay en `activos/.../SET_01-REP/`)

| Archivo | Qué es | Estado |
|---|---|---|
| `SET_01-REP.dwt` | Plantilla: 29 capas, 8 estilos, 3 cotas, metros | Generado y verificado ida/vuelta |
| `SET-REP.dws` | Norma para `VERIFICANORMAS` | Generado (misma base) |
| `EP-ISO.ctb` | Grosores por color (tabla abajo) | Crear en destino (§6 paso 4) |
| Plotter `DWG To PDF.pc3` | Viene con AutoCAD | Elegir en `PAGESETUP` (§6 paso 5) |

CTB punto de partida (serie ISO, se ajusta con prueba de ploteo):

| ACI | mm | Capas |
|---|---|---|
| 24, 11, 1, 81, 5 | 0.50 | Muros, columnas, ejes replanteo, rótulo |
| 90, 113, 41, 10, 254, 32 | 0.35 | Ejes, cotas replanteo |
| 163, 166, 3, 33 | 0.25 | Terreno, tabiques, conductos, simb |
| 250, 251, 7, 8 | 0.18 | Cotas, carpinterías, base |
| 130, 174 | no plot | Viewports, textos rótulo |

## 6. Instructivo PC de Emilia (15 min)

1. Copiar `activos/.../SET_01-REP/` a la PC (misma ruta o `G:\Mi unidad\OS-Emilia\W03-CAD\SET_01-REP\`).
2. En AutoCAD LT: `OPCIONES` → Archivos → ruta de plantillas → agregar la carpeta → `NUEVO` desde `SET_01-REP.dwt`.
3. Verificar: `UNIDADES` decimal metros, `LISTA` de capas (29), estilos (`ESTILO`, `ESTILOCOTA`).
4. CTB: `TRAZAR` → tabla nueva `EP-ISO` → cargar tabla §5 → guardar en carpeta de estilos (`OPCIONES` → Archivos → ruta de tablas).
5. Lámina: layout `REP-PTipo-A1`, `ADMINPAGINAS` → `DWG To PDF.pc3` → A1 apaisado 841×594 → viewport 1:50 (`ZOOM 20 XP` con modelo en metros) → bloquear vista.
6. Dibujar (§12 doc madre, 12 pasos): terreno → ejes → muros → vanos (`INSERTAR` al centro) → tags → cotas → textos → `SINCRATR` + `REGENERAR` → `VERIFICANORMAS` → PDF.
7. Cómputos: `EXTRACDAT` a CSV → `POST` al webhook del cuadro (ver doc cómputos) → verifica en el Sheet de `W03-CAD`.

## 7. Horas y backlog

14 h invertidas (10 h en ~24 pomodoros + 4 h); ahorro ~12–15 h por plano;
payback en el primer plano (detalle y supuestos en desglose). Backlog mes
próximo (§16 doc madre): visibilidades por escala, cotas dinámicas, capas de
instalaciones, playbook separado ítem por ítem, pase a wiki.
