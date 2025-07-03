
import re
from datetime import datetime

OCUPACIONES_VALIDAS = [
    "Sin ocupación", "Jubilado", "Estudiante", "Trabajador no cualificado", "Trabajador cualificado",
    "Empleado de oficina", "Profesional técnico", "Profesional universitario", "Directivo",
    "Autónomo o empresario", "Campo o agricultura", "Otro"
]

NIVELES_ESTUDIOS_VALIDOS = [
    "Sin estudios", "Primaria", "Secundaria", "Bachillerato / FP Medio",
    "FP Superior / Universidad incompleta", "Universidad / Grado universitario",
    "Máster / Posgrado", "Doctorado"
]

ROLES_VALIDOS = ["paciente", "profesional"]

JUEGOS_VALIDOS = ["Stroop", "N-back", "Par"]

def validar_nombre(nombre):
    if not nombre or not nombre.isalpha():
        raise ValueError("Nombre inválido.")
    return nombre.strip()

def validar_genero(genero):
    if genero not in ["Masculino", "Femenino", "Otro"]:
        raise ValueError("Género inválido.")
    return genero

def validar_edad(edad):
    if not (50 <= edad <= 120):
        raise ValueError("Edad fuera de rango válido.")
    return edad

def validar_ocupacion(ocupacion):
    if ocupacion not in OCUPACIONES_VALIDAS:
        raise ValueError("Ocupación no válida.")
    return ocupacion

def validar_nivel_estudios(nivel):
    if nivel not in NIVELES_ESTUDIOS_VALIDOS:
        raise ValueError("Nivel de estudios no válido.")
    return nivel

def validar_email(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
        raise ValueError("Correo electrónico inválido.")
    return email

def validar_rol(rol):
    if rol not in ROLES_VALIDOS:
        raise ValueError("Rol no válido.")
    return rol

def validar_password(password):
    if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"\d", password):
        raise ValueError("Contraseña insegura. Debe tener al menos 8 caracteres, una mayúscula y un número.")
    return password

def validar_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Formato de fecha inválido. Debe ser DD/MM/AAAA.")

def validar_clinico_binario(valor, campo):
    if valor not in [0, 1]:
        raise ValueError(f"{campo} debe ser 0 (No) o 1 (Sí).")
    return valor

def validar_rango(valor, minimo, maximo, campo):
    if not (minimo <= valor <= maximo):
        raise ValueError(f"{campo} debe estar entre {minimo} y {maximo}.")
    return valor

def validar_categorico(valor, opciones, campo):
    if valor not in opciones:
        raise ValueError(f"{campo} debe ser uno de: {', '.join(opciones)}.")
    return valor

def validar_nombre_juego(nombreJuego):
    if nombreJuego not in JUEGOS_VALIDOS:
        raise ValueError("Nombre del juego no válido.")
    return nombreJuego
