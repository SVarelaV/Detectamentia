# servicios/servicio_paciente.py

from controlador.dominios.paciente import Paciente
from controlador.gestores.pacientes import Pacientes
from vistas.validador_paciente import (
    sanitize_input, validar_texto, validar_genero, validar_edad,
    validar_poblacion, validar_ocupacion, validar_nivel_estudios
)

class CrearPaciente:
    def __init__(self):
        self.modelo = Pacientes()

    def crear_paciente(self, datos_dict: dict) -> Paciente:
        """
        Recibe un diccionario desde la capa vista, lo valida, lo transforma
        en objeto Paciente y lo guarda usando la capa modelo.
        """
        try:
            # Validación
            nombre = sanitize_input(datos_dict["nombre"])
            if not validar_texto(nombre):
                raise ValueError("Nombre inválido")
            apellido1 = sanitize_input(datos_dict["apellido1"])
            apellido2 = sanitize_input(datos_dict["apellido2"])
            if not (validar_texto(apellido1) and validar_texto(apellido2)):
                raise ValueError("Apellidos inválidos")
            genero = sanitize_input(datos_dict["genero"])
            if not validar_genero(genero):
                raise ValueError("Género inválido")
            edad = int(sanitize_input(str(datos_dict["edad"])))
            if not validar_edad(str(edad)):
                raise ValueError("Edad inválida")
            poblacion = sanitize_input(datos_dict["poblacion"])
            if not validar_poblacion(poblacion):
                raise ValueError("Población inválida")
            ocupacion = sanitize_input(datos_dict["ocupacion"])
            if not validar_ocupacion(ocupacion):
                raise ValueError("Ocupación inválida")
            nivel = sanitize_input(datos_dict["nivelEstudios"])
            if not validar_nivel_estudios(nivel):
                raise ValueError("Nivel de estudios inválido")

            # Crear objeto dominio
            paciente = Paciente(nombre, apellido1, apellido2, genero, edad, poblacion, ocupacion, nivel)

            # Guardar en modelo
            guardado = self.modelo.agregar(paciente)
            if not guardado:
                raise Exception("No se pudo guardar el paciente.")

            return paciente  # Siempre devuelve un objeto

        except Exception as e:
            print(f"❌ Error en ServicioPaciente.crear_paciente: {e}")
            raise
