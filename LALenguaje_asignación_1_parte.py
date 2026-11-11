# CREADOR DE UN IDIOMA SECRETO — versión 2
# Edita las secciones 1 y 2. No necesitas modificar el menú ni las funciones.
import random

# 1. EQUIVALENCIAS A-Z (EDITA AQUÍ)
# Puedes usar números, letras o combinaciones. No uses guiones dentro de los valores.
EQUIVALENCIAS = {
    "A": "Zr", "B": "uo",  "C": "na", "D": "pl", "E": "7",
    "F": "kj", "G": "op", "H": "ñm",  "I": "er", "J": "ug",
    "K": "hg",  "L": "67", "M": "bs", "N": "77",  "O": "sw",
    "P": "qw", "Q": "xs",  "R": "vc", "S": "tre", "T": "we",
    "U": "jd", "V": "gu", "W": "0",  "X": "dt", "Y": "ft",
    "Z": "9",
}

# 2. REGLAS PARA INVENTAR PALABRAS (EDITA AQUÍ)
# Reglas 1-3 están activas desde el inicio.
MIN_PIEZAS = 2                 # Regla 1: mínimo de equivalencias por palabra
MAX_PIEZAS = 6                 # Regla 2: máximo de equivalencias por palabra
REPETIR_PIEZA_SEGUIDA = False  # Regla 3: permitir repetir la misma pieza seguida

# Reglas 4-7 son opcionales: quita el # para activar una o varias.
# Usa una equivalencia completa de la sección 1 como valor.a
REGLAS_EXTRA = {
     "iniciar_con": "op",  # Regla 4: la palabra empieza con esta pieza
     "terminar_con": "we",  # Regla 5: la palabra termina con esta pieza
    # "contener": "mu",     # Regla 6: la palabra contiene esta pieza
    # "prohibir": "xo",     # Regla 7: la palabra no puede contener esta pieza
}

# No necesitas editar estas variables.
DICCIONARIO = []
PALABRAS_GENERADAS = []

def registrar(palabra, significado, origen):
    """Guarda una entrada sin borrar otras que compartan el mismo código."""
    for entrada in DICCIONARIO:
        if entrada["palabra"] == palabra and entrada["origen"] == origen:
            if origen == "Generada" and significado != "Sin significado asignado":
                entrada["significado"] = significado
                return
            elif origen == "Transformada" and entrada["significado"] != significado:
                continue
            else:
                return
    DICCIONARIO.append({"palabra": palabra, "significado": significado, "origen": origen})

def ver_equivalencias():
    for letra, valor in EQUIVALENCIAS.items():
        print(f"{letra} -> {valor}")

def transformar_palabra():
    texto = input("Escribe una palabra o frase para transformar: ").strip()
    if not texto:
        print("No escribiste ningún texto.")
        return

    resultados = []
    agregadas = 0
    for original in texto.split():
        piezas = []
        contiene_letras = False
        for caracter in original:
            letra = caracter.upper()
            if letra in EQUIVALENCIAS:
                piezas.append(EQUIVALENCIAS[letra])
                contiene_letras = True
            else:
                piezas.append(caracter)  # Conserva signos de puntuación y números
        secreta = "-".join(piezas)
        resultados.append(secreta)
        if contiene_letras:
            registrar(secreta, original, "Transformada")
            agregadas += 1

    print("Resultado:", " ".join(resultados))
    if agregadas:
        print(f"Se agregaron {agregadas} palabra(s) transformada(s) al diccionario.")

def cumple_reglas(piezas):
    if not MIN_PIEZAS <= len(piezas) <= MAX_PIEZAS:
        return False
    if not REPETIR_PIEZA_SEGUIDA and any(piezas[i] == piezas[i - 1] for i in range(1, len(piezas))):
        return False
    if "iniciar_con" in REGLAS_EXTRA and piezas[0] != REGLAS_EXTRA["iniciar_con"]:
        return False
    if "terminar_con" in REGLAS_EXTRA and piezas[-1] != REGLAS_EXTRA["terminar_con"]:
        return False
    if "contener" in REGLAS_EXTRA and REGLAS_EXTRA["contener"] not in piezas:
        return False
    if "prohibir" in REGLAS_EXTRA and REGLAS_EXTRA["prohibir"] in piezas:
        return False
    return True

def ver_reglas():
    print(f"Regla 1 — mínimo de piezas: {MIN_PIEZAS}")
    print(f"Regla 2 — máximo de piezas: {MAX_PIEZAS}")
    print("Regla 3 — repetir una pieza seguida:", "Sí" if REPETIR_PIEZA_SEGUIDA else "No")
    nombres = {
        "iniciar_con": "Regla 4 — comenzar con",
        "terminar_con": "Regla 5 — terminar con",
        "contener": "Regla 6 — contener la pieza",
        "prohibir": "Regla 7 — prohibir la pieza",
    }
    for clave, nombre in nombres.items():
        estado = f"{REGLAS_EXTRA[clave]} (activa)" if clave in REGLAS_EXTRA else "desactivada"
        print(f"{nombre}: {estado}")

def generar_palabra():
    if not EQUIVALENCIAS:
        print("Añade equivalencias en la sección 1 antes de generar palabras.")
        return
    if MIN_PIEZAS < 1 or MAX_PIEZAS < MIN_PIEZAS:
        print("Revisa MIN_PIEZAS y MAX_PIEZAS en la sección 2.")
        return
    valores = list(EQUIVALENCIAS.values())
    for regla, pieza in REGLAS_EXTRA.items():
        if pieza not in valores:
            print(f"La regla '{regla}' usa una pieza que no existe en EQUIVALENCIAS.")
            print("Cambia ese valor por una equivalencia definida en la sección 1.")
            return

    # Busca una combinación que cumpla las reglas activas.
    for _ in range(5000):
        piezas = [random.choice(valores) for _ in range(random.randint(MIN_PIEZAS, MAX_PIEZAS))]
        if cumple_reglas(piezas):
            palabra = "-".join(piezas)
            if palabra not in PALABRAS_GENERADAS:
                PALABRAS_GENERADAS.append(palabra)
            registrar(palabra, "Sin significado asignado", "Generada")
            print("Palabra inventada:", palabra)
            print("Se agregó al diccionario. Usa la opción 4 para asignarle un significado.")
            return
    print("No se encontró una palabra que cumpla todas las reglas activas.")
    print("Prueba cambiar una regla o ampliar el mínimo y máximo de piezas.")

def asignar_significado():
    if not PALABRAS_GENERADAS:
        print("Primero genera una palabra con la opción 3.")
        return
    print("Palabras generadas:")
    for numero, palabra in enumerate(PALABRAS_GENERADAS, start=1):
        significado = next((e["significado"] for e in DICCIONARIO
                            if e["palabra"] == palabra and e["origen"] == "Generada"),
                           "Sin significado asignado")
        print(f"{numero}. {palabra} — {significado}")
    try:
        numero = int(input("Número de la palabra: "))
        if not 1 <= numero <= len(PALABRAS_GENERADAS):
            print("Número fuera de la lista.")
            return
    except ValueError:
        print("Escribe un número válido.")
        return
    palabra = PALABRAS_GENERADAS[numero - 1]
    significado = input(f"¿Qué significa '{palabra}'?: ").strip()
    if significado:
        registrar(palabra, significado, "Generada")
        print("Significado guardado en el diccionario.")
    else:
        print("No se guardó un significado vacío.")

def ver_diccionario():
    if not DICCIONARIO:
        print("El diccionario todavía está vacío.")
        return
    print("\n=== MI DICCIONARIO ===")
    for entrada in DICCIONARIO:
        print(f"{entrada['palabra']} = {entrada['significado']} [{entrada['origen']}]")

# 3. MENÚ (no necesitas editar esta parte para comenzar)
while True:
    print("\n=== CREADOR DE IDIOMA SECRETO ===")
    print("1. Ver equivalencias A-Z")
    print("2. Transformar una palabra o frase (se guarda en el diccionario)")
    print("3. Generar una palabra nueva según las reglas (se guarda en el diccionario)")
    print("4. Asignar significado a una palabra generada")
    print("5. Consultar mi diccionario")
    print("6. Ver las siete reglas")
    print("7. Salir")
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        ver_equivalencias()
    elif opcion == "2":
        transformar_palabra()
    elif opcion == "3":
        generar_palabra()
    elif opcion == "4":
        asignar_significado()
    elif opcion == "5":
        ver_diccionario()
    elif opcion == "6":
        ver_reglas()
    elif opcion == "7":
        print("¡Hasta luego! El diccionario se conserva solo mientras el programa está abierto.")
        break
    else:
        print("Opción no válida: elige un número del 1 al 7.")
