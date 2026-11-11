"""Regla de validación: prohíbe palabras originales con 3 o más consonantes seguidas."""

from alfabeto import normalizar_letra

ACTIVA = True
TIPO = "validacion"
ORDEN = 20

MAX_CONSONANTES_SEGUIDAS = 3
VOCALES = set("AEIOU")


def validar(piezas, palabra_original):
    """Devuelve un error si la palabra original tiene 3 o más consonantes seguidas."""
    contador_consonantes = 0

    for caracter in palabra_original:
        letra_norm = normalizar_letra(caracter)

        # Si es una letra y no es vocal, incrementamos el contador
        if letra_norm.isalpha() and letra_norm not in VOCALES:
            contador_consonantes += 1
            if contador_consonantes >= MAX_CONSONANTES_SEGUIDAS:
                return (
                    f"la palabra original '{palabra_original}' tiene "
                    f"{MAX_CONSONANTES_SEGUIDAS} o más consonantes seguidas."
                )
        else:
            # Una vocal o carácter no alfabético reinicia la racha de consonantes
            contador_consonantes = 0

    return None