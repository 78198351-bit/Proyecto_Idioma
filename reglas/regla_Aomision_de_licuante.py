from alfabeto import normalizar_letra

ACTIVA = True
TIPO = "transformacion"
# ORDEN = 10 asegura que se ejecute ANTES de invertir la palabra o añadir el número final
ORDEN = 10

LICUANTES = {"B", "C", "D", "F", "G", "P", "T"}
LIQUIDAS = {"L", "R"}


def aplicar(piezas, palabra_original):
    """Detecta grupos como BL, CR, TR y elimina la pieza correspondiente a la licuante."""
    letras = [normalizar_letra(c) for c in palabra_original if c.isalpha()]

    indices_a_omitir = set()
    i = 0

    while i < len(letras) - 1:
        # Detectamos el par (ejemplo: 'T' y 'R' en "TREN")
        if letras[i] in LICUANTES and letras[i + 1] in LIQUIDAS:
            indices_a_omitir.add(i)  # Omite la primera letra del par (la licuante)
            i += 2  # Avanzamos para no evaluar la líquida como inicio de otro grupo
        else:
            i += 1

    # Retornamos únicamente las piezas que no corresponden a los índices omitidos
    return [pieza for idx, pieza in enumerate(piezas) if idx not in indices_a_omitir]