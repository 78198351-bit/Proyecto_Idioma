"""Equivalencias editables del alfabeto original al idioma secreto."""

# Cada letra se convierte en una pieza (símbolo, sílaba o combinación).
# Los estudiantes pueden cambiar estos valores para crear su propio alfabeto.
ALFABETO = {
    "A": "Zr",
    "B": "uo",  
    "C": "na", 
    "D": "pl", 
    "E": "7",
    "F": "kj", 
    "G": "op", 
    "H": "de",  
    "I": "er", 
    "J": "ug",
    "K": "23git",  
    "L": "67", 
    "M": "oi", 
    "N": "77",  
    "O": "sw",
    "P": "qw", 
    "Q": "xs",  
    "R": "et", 
    "S": "tre", 
    "T": "we",
    "U": "jd", 
    "V": "gu", 
    "W": "0",  
    "X": "dt", 
    "Y": "pq",
    "Z": "9", # La regla de reemplazo convierte esta pieza en 0.
}


def normalizar_letra(letra):
    """Convierte vocales acentuadas a su forma base; conserva la Ñ."""
    letra = letra.upper()
    if letra == "Ñ":
        return "Ñ"

    equivalencias = {
        "Á": "A", "À": "A", "Ä": "A",
        "É": "E", "È": "E", "Ë": "E",
        "Í": "I", "Ì": "I", "Ï": "I",
        "Ó": "O", "Ò": "O", "Ö": "O",
        "Ú": "U", "Ù": "U", "Ü": "U",
    }
    return equivalencias.get(letra, letra)
