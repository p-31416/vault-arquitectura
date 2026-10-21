"""NOTA ES: Verificador de paréntesis y estructura básica para archivos AutoLISP.
NOTA ES: NO ejecuta el Lisp: solo cuenta paréntesis ignorando comentarios (;)
NOTA ES: y cadenas de texto ("..."). Devuelve el número de línea del desbalance.
NOTA ES: Uso: python chequea-lisp.py <archivo.lsp>
"""

import sys
from pathlib import Path


def chequea(texto):
    nivel = 0
    linea = 1
    en_cadena = False
    i = 0
    while i < len(texto):
        c = texto[i]
        if c == '\n':
            linea += 1
            i += 1
            continue
        if en_cadena:
            if c == '\\':
                i += 2
                continue
            if c == '"':
                en_cadena = False
            i += 1
            continue
        if c == '"':
            en_cadena = True
            i += 1
            continue
        if c == ';':
            while i < len(texto) and texto[i] != '\n':
                i += 1
            continue
        if c == '(':
            nivel += 1
        elif c == ')':
            nivel -= 1
            if nivel < 0:
                return linea, nivel
        i += 1
    return linea, nivel


def main():
    p = Path(sys.argv[1])
    linea, nivel = chequea(p.read_text(encoding='utf-8', errors='replace'))
    if nivel == 0:
        print("OK: parentesis balanceados (%s)" % p.name)
    else:
        print("DESBALANCE nivel=%d (ultima linea %d) en %s" % (nivel, linea, p.name))
    # Reporta comandos definidos
    for n, l in enumerate(p.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
        if l.strip().lower().startswith('(defun c:'):
            print("  comando en linea %d: %s" % (n, l.strip()[:70]))


if __name__ == '__main__':
    main()
