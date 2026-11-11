"""Regla de transformación: convierte todas las piezas traducidas a mayúsculas."""

ACTIVA = True
TIPO = "transformacion"
# ORDEN = 30 para ejecutarse después de duplicar vocales y antes de invertir o añadir números
ORDEN = 30


def aplicar(piezas, palabra_original):
    """Convierte cada pieza de la lista a mayúsculas."""
    return [pieza.upper() for pieza in piezas]