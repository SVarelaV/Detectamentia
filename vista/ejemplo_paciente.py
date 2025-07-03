from validador_detectamentia import (
    validar_nombre, validar_genero, validar_edad,
    validar_ocupacion, validar_nivel_estudios
)
from ejemplo_paciente import Paciente

def crear_paciente_desde_input():
    try:
        id_paciente = input("ID Paciente: ")
        nombre = validar_nombre(input("Nombre: "))
        apellido1 = validar_nombre(input("Primer Apellido: "))
        apellido2 = validar_nombre(input("Segundo Apellido: "))
        genero = validar_genero(input("Género (Masculino/Femenino/Otro): "))
        edad = validar_edad(int(input("Edad: ")))
        poblacion = input("Población: ").strip()
        ocupacion = validar_ocupacion(input("Ocupación: "))
        nivel_estudios = validar_nivel_estudios(input("Nivel de estudios: "))

        paciente = Paciente(id_paciente, nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivel_estudios)
        print("✅ Paciente creado correctamente:")
        print(paciente)
    except Exception as e:
        print("❌ Error:", e)

crear_paciente_desde_input()

