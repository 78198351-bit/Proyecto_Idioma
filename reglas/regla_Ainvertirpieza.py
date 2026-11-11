"""Regla de transformación: invierte el orden de las piezas traducidas."""

ACTIVA = True  # Activada para que el traductor la ejecute
TIPO = "transformacion"
ORDEN = 40  # Se ejecuta con orden 40 (antes del orden 50 por defecto)


def aplicar(piezas, palabra_original):
    """Devuelve la lista de piezas con el orden completamente invertido."""
    return piezas[::-1]