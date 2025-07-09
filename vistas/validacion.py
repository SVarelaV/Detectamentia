import re

# --- FUNCIONES DE SANITIZACIÓN Y LISTAS ---

def sanitize_input(value: str) -> str:
    value = ''.join(c for c in value if c.isprintable())
    return value.strip()

# Listas válidas
ocupaciones_validas = [
    "Jubilado", "Estudiante", "Trabajador no cualificado", "Trabajador cualificado",
    "Empleado de oficina", "Profesional técnico", "Profesional universitario",
    "Directivo", "Autónomo o empresario", "Campo o agricultura"
]

niveles_validos = [
    "Sin estudios", "Primaria", "Secundaria", "Bachillerato / FP Medio",
    "FP Superior / Universidad incompleta", "Universidad / Grado universitario",
    "Máster / Posgrado", "Doctorado"
]

generos_validos = ["Masculino", "Femenino", "Otro"]
roles_validos = ["paciente", "profesional"]
frecuencias = ["Nunca", "Ocasional", "Frecuente"]
calidades_sueno = ["Mala", "Regular", "Buena"]
niveles_actividad = ["Sedentario", "Moderado", "Activo"]

# --- VALIDACIONES SIMPLES ---

def validar_texto(texto: str) -> bool:
    texto = sanitize_input(texto)
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,50}$", texto))

def validar_genero(genero: str) -> bool:
    return sanitize_input(genero) in generos_validos

def validar_edad(edad: str) -> bool:
    edad = sanitize_input(edad)
    return edad.isdigit() and 50 <= int(edad) <= 120

def validar_poblacion(poblacion: str) -> bool:
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,100}$", sanitize_input(poblacion)))

def validar_email(email: str) -> bool:
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$', sanitize_input(email)))

def validar_fecha(fecha: str) -> bool:
    return bool(re.match(r"\d{2}-\d{2}-\d{4}", sanitize_input(fecha)))

def validar_binario(valor: str) -> bool:
    return valor.strip() in ["0", "1"]

def validar_entero_rango(valor: str, minimo: int, maximo: int) -> bool:
    return valor.strip().isdigit() and minimo <= int(valor) <= maximo

def validar_float_rango(valor: str, minimo: float, maximo: float) -> bool:
    try:
        v = float(valor.strip())
        return minimo <= v <= maximo
    except ValueError:
        return False

# --- FUNCIONES INTERACTIVAS CENTRALIZADAS ---

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

def pedir_binario(mensaje):
    valor = input(f"{mensaje} (1=Sí, 0=No): ")
    while not validar_binario(valor):
        print("❌ Valor inválido.")
        valor = input(f"{mensaje} (1=Sí, 0=No): ")
    return int(valor)

def pedir_entero_rango(mensaje, minimo, maximo):
    valor = input(f"{mensaje} ({minimo}-{maximo}): ")
    while not validar_entero_rango(valor, minimo, maximo):
        print("❌ Valor fuera de rango.")
        valor = input(f"{mensaje} ({minimo}-{maximo}): ")
    return int(valor)

def pedir_float_rango(mensaje, minimo, maximo):
    valor = input(f"{mensaje} ({minimo}-{maximo}): ")
    while not validar_float_rango(valor, minimo, maximo):
        print("❌ Valor fuera de rango.")
        valor = input(f"{mensaje} ({minimo}-{maximo}): ")
    return float(valor)

def pedir_texto_validado(mensaje):
    valor = input(mensaje)
    while not validar_texto(valor):
        print("❌ Texto inválido.")
        valor = input(mensaje)
    return valor

def pedir_email():
    valor = input("Email: ")
    while not validar_email(valor):
        print("❌ Email inválido.")
        valor = input("Email: ")
    return valor

def pedir_fecha():
    valor = input("Fecha (DD-MM-YYYY): ")
    while not validar_fecha(valor):
        print("❌ Fecha inválida.")
        valor = input("Fecha (DD-MM-YYYY): ")
    return valor
