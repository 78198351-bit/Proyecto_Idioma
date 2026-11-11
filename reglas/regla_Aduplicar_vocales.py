"""Regla de transformación: duplica las vocales de las piezas traducidas."""

ACTIVA = True
TIPO = "transformacion"
# ORDEN = 20 para ejecutarse después del filtrado de licuantes y antes de invertir o añadir el número
ORDEN = 20

VOCALES = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")


def aplicar(piezas, palabra_original):
    """Recorre cada pieza y duplica cualquier carácter que sea una vocal."""
    nuevas_piezas = []

    for pieza in piezas:
        pieza_duplicada = ""
        for caracter in pieza:
            if caracter in VOCALES:
                pieza_duplicada += caracter * 2  # Duplica la vocal (ej. 'a' -> 'aa')
            else:
                pieza_duplicada += caracter
        nuevas_piezas.append(pieza_duplicada)

    return nuevas_piezas