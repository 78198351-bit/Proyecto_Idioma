"""Regla de transformación: asegura que la palabra traducida empiece con una vocal."""

ACTIVA = True
TIPO = "transformacion"
# ORDEN = 15 para ejecutarse antes de invertirse o añadirse un número al final
ORDEN = 15

# Pieza de vocal predeterminada a añadir al inicio (por ejemplo, "Zr" equivale a la letra 'A')
VOCAL_PREDETERMINADA = "Zr"
VOCALES = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")


def aplicar(piezas, palabra_original):
    """Si la primera pieza no empieza con una vocal, le antepone VOCAL_PREDETERMINADA."""
    if not piezas:
        return piezas

    # Revisa si la primera pieza comienza con una carácter vocálico
    primer_caracter = piezas[0][0] if piezas[0] else ""

    if primer_caracter not in VOCALES:
        return  piezas +[VOCAL_PREDETERMINADA]

    return piezas