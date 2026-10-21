# Orden de locales — REP-ARAOZ.dwg

> Fuente: rotulos A-SIMBOLO-NPT-PLANTA (DESCRIPCION / N) · tolerancia de fila: 0.30 m · INSUNITS=6 (metros)
> Archivo de trabajo: `activos/.../W03-CAD` (binario externo al vault).

## Filas (de arriba hacia abajo, de izquierda a derecha)

### Fila 1

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 01 | 01 | AMBIENTE | 18.584 | -0.929 | 270.0 |

### Fila 2

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 02 | 02 | BAÑO | 4.459 | -1.654 | 0.0 |
| 03 | 03 | BAÑO | 18.467 | -1.881 | 0.0 |

### Fila 3

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 04 | 04 | DORMITORIO | 1.746 | -2.708 | 0.0 |
| 05 | 05 | DORMITORIO | 6.151 | -2.689 | 0.0 |
| 06 | 06 | DORMITORIO | 16.402 | -2.671 | 0.0 |

### Fila 4

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 07 | 07 | DORMITORIO | 20.994 | -3.063 | 0.0 |

### Fila 5

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 08 | 08 | BALCON | -1.32 | -5.261 | 0.0 |
| 09 | 09 | BALCON | 24.473 | -5.142 | 0.0 |

### Fila 6

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 10 | 10 | ESTAR-COM. | 18.101 | -5.732 | 0.0 |

### Fila 7

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 11 | 11 | ESTAR-COM. | 3.52 | -6.541 | 0.0 |

### Fila 8

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 12 | 12 | TOILETTE | 5.733 | -6.932 | 0.0 |

### Fila 9

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 13 | 13 | COC. - LAV. | 19.007 | -8.531 | 0.0 |

### Fila 10

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 14 | 14 | COC. - LAV. | 3.282 | -8.862 | 0.0 |

### Fila 11

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 15 | 15 | COC. - LAV. | 10.22 | -9.703 | 0.0 |
| 16 | 16 | COC. - LAV. | 12.478 | -9.703 | 0.0 |

### Fila 12

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 17 | 17 | ESTAR-COM. | 5.581 | -10.786 | 0.0 |
| 18 | 18 | ESTAR-COM. | 18.16 | -10.843 | 0.0 |

### Fila 13

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 19 | 19 | BALCON | -0.516 | -11.203 | 0.0 |
| 20 | 20 | BALCON | 24.779 | -11.176 | 0.0 |

### Fila 14

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 21 | 21 | PALIER | 9.609 | -12.341 | 0.0 |

### Fila 15

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 22 | 22 | DORMITORIO | 2.151 | -14.131 | 0.0 |
| 23 | 23 | ASCENSOR I | 10.559 | -14.186 | 180.0 |
| 24 | 24 | ESCALERA | 14.922 | -14.08 | 0.0 |
| 25 | 25 | DORMITORIO | 20.513 | -14.06 | 0.0 |

### Fila 16

| orden | N_LOC | TXT_LOC | X | Y | giro |
|---|---|---|---|---|---|
| 26 | 26 | BAÑO | 5.03 | -14.675 | 0.0 |
| 27 | 27 | ASCENSOR II | 8.18 | -14.75 | 0.0 |
| 28 | 28 | BAÑO | 18.192 | -14.97 | 0.0 |

## Control

- Locales detectados: **28** en **16 filas**
- Números repetidos: ninguno
- Locales sin nombre: 0
- Orden de lectura (X+ / Y-, filas ΔY < 0.30 m): OK, la numeración coincide con el orden de lectura
- Insertar `SIMB-LOC_ID` en este orden (número = N_LOC, nombre = TXT_LOC).

> **Numeración legacy (rótulos viejos `*U323` / `*U324`)**: los `N` que ya trae el dibujo (00, 01, 02… con el `07` ausente y un `12` duplicado) **no** siguen el orden de lectura — en orden de lectura salen `00, 15, 02, 16, 14, 03, 01, 18, 04, …`. La numeración de esta tabla (`01`…`28`) es la del bloque nuevo `SIMB-LOC_ID`, que se inserta con el comando `SIMB-LOC_ID` (número automático, en orden de lectura) y se controla con `LOC-ID-CHECK`.
