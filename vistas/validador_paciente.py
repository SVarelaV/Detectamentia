
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
    "Sin ocupación / Nunca trabajó", "Desempleado/a", "Jubilado/a", "Ama/o de casa",
    "Estudiante", "Trabajador/a no cualificado/a", "Trabajador/a cualificado/a",
    "Empleado/a administrativo/a o de oficina", "Técnico/a o profesional de nivel medio",
    "Profesional universitario/a", "Directivo/a o Ejecutivo/a", "Empresario/a o autónomo/a",
    "Agricultor/a o trabajador/a del campo", "Otro (especificar)"
]

niveles_validos = [
    "Sin escolarización", "Educación primaria incompleta", "Educación primaria completa",
    "Educación secundaria incompleta", "Educación secundaria completa",
    "Bachillerato o equivalente incompleto", "Bachillerato o equivalente completo",
    "Estudios universitarios incompletos", "Estudios universitarios completos",
    "Estudios de posgrado / máster", "Doctorado o equivalente"
]

generos_validos = ["masculino", "femenino", "otro"]

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
