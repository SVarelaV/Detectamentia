import re

# Función de sanitización
def sanitize_input(value: str) -> str:
    """
    Elimina caracteres no imprimibles y espacios extra.
    """
    value = ''.join(c for c in value if c.isprintable())
    value = value.strip()
    return value

# Listas válidas
ocupaciones_validas = [
    "Jubilado",
    "Estudiante",
    "Trabajador no cualificado",
    "Trabajador cualificado",
    "Empleado de oficina",
    "Profesional técnico",
    "Profesional universitario",
    "Directivo",
    "Autónomo o empresario",
    "Campo o agricultura"
]


niveles_validos = [
    "Sin estudios",
    "Primaria",
    "Secundaria",
    "Bachillerato / FP Medio",
    "FP Superior / Universidad incompleta",
    "Universidad / Grado universitario",
    "Máster / Posgrado",
    "Doctorado"
]

generos_validos = ["Masculino", "Femenino", "Otro"]

# Funciones de validación

def validar_texto(texto: str) -> bool:
    texto = sanitize_input(texto)
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,50}$", texto))

def validar_genero(genero: str) -> bool:
    genero = sanitize_input(genero)
    return genero.lower() in generos_validos

def validar_edad(edad: str) -> bool:
    edad = sanitize_input(edad)
    return edad.isdigit() and 50 <= int(edad) <= 120

def validar_poblacion(poblacion: str) -> bool:
    poblacion = sanitize_input(poblacion)
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,100}$", poblacion))

def validar_ocupacion(ocupacion: str) -> bool:
    ocupacion = sanitize_input(ocupacion)
    return ocupacion in ocupaciones_validas

def validar_nivel_estudios(nivel: str) -> bool:
    nivel = sanitize_input(nivel)
    return nivel in niveles_validos

# Funciones interactivas

def mostrar_opciones(lista):
    for i, opcion in enumerate(lista, 1):
        print(f"{i}. {opcion}")

def seleccionar_opcion(lista, mensaje):
    while True:
        print(f"\n{mensaje}")
        mostrar_opciones(lista)
        entrada = input("Selecciona una opción (número): ").strip()
        if entrada.isdigit():
            idx = int(entrada) - 1
            if 0 <= idx < len(lista):
                return lista[idx]
        print("❌ Opción no válida. Intenta de nuevo.")
