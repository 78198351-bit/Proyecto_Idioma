import re
from alfabeto import normalizar_letra

ACTIVA = True
TIPO = "validacion"
ORDEN = 20

MAX_SILABAS = 3


def contar_silabas(palabra):
    """Aproxima el número de sílabas contando los grupos vocálicos."""
    # Convertimos vocales con acento a su forma base (Á -> A)
    palabra_norm = "".join(normalizar_letra(c) for c in palabra).lower()
    # Encuentra cada grupo de vocales consecutivas
    grupos_vocalicos = re.findall(r"[aeiou]+", palabra_norm)
    return len(grupos_vocalicos)


def validar(piezas, palabra_original):
    """Devuelve None si tiene 3 o menos sílabas, o un mensaje de error si las supera."""
    num_silabas = contar_silabas(palabra_original)

    if num_silabas > MAX_SILABAS:
        return (
            f"la palabra '{palabra_original}' tiene {num_silabas} sílabas; "
            f"el máximo permitido es {MAX_SILABAS}."
        )

    return None