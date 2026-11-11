"""PLANTILLA 2: exigir que la palabra secreta contenga un número.

Copia este archivo a reglas/regla_contiene_numero.py.
Completa la validación antes de cambiar ACTIVA a True.
"""

ACTIVA = False
TIPO = "validacion"
# ORDEN = 50  # Opcional. Si lo omites, se utiliza el orden 50.


def validar(piezas, palabra_original):
    palabra_secreta = "".join(piezas)
    contiene_numero = False

    for caracter in palabra_secreta:
        if caracter.isdigit():
            contiene_numero = True
            break

    if not contiene_numero:
        return "la traducción debe contener al menos un número."

    return None
