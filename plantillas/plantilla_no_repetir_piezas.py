"""PLANTILLA 3: prohibir que una pieza se repita en la misma palabra.

Copia este archivo a reglas/regla_no_repetir_piezas.py.
Completa la validación antes de cambiar ACTIVA a True.
"""

ACTIVA = False
TIPO = "validacion"
# ORDEN = 50  # Opcional. Si lo omites, se utiliza el orden 50.


def validar(piezas, palabra_original):
    piezas_vistas = set()

    for pieza in piezas:
        if pieza in piezas_vistas:
            return f"la pieza '{pieza}' se repite en la palabra."
        piezas_vistas.add(pieza)

    return None